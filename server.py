#!/usr/bin/env python3
"""
Mini-XAMPP: un finto server MySQL locale, in Python puro, per esercitarsi con mysql.connector.

- Funziona su Windows, macOS e Linux (serve solo Python 3.10+ e pip).
- Nessun download di MySQL/MariaDB/XAMPP.
- Parla il protocollo MySQL vero: mysql.connector si collega come a un server normale.
- Dietro le quinte i dati stanno in file SQLite (uno per database) in ~/.mini_xampp/

LIMITI (leggi!): NON e' MySQL. Il SQL viene tradotto in SQLite, quindi ENGINE=, FOREIGN KEY,
tipi, charset, permessi e messaggi di errore possono comportarsi in modo diverso da un MySQL vero.
Va bene per imparare connect/cursor/execute/fetch/commit. Non va bene per testare qualcosa
che andra' in produzione su MySQL.

Uso:
    python mini_xampp.py                  # apre la finestra
    python mini_xampp.py --headless       # senza GUI (terminale)
    python mini_xampp.py --port 3307
"""
import argparse
import asyncio
import os
import queue
import re
import shutil
import sqlite3
import subprocess
import sys
import threading
from pathlib import Path

REQUIRED = ["mysql-mimic==3.0.5", "sqlglot", "mysql-connector-python"]
DATA_DIR = Path.home() / ".mini_xampp"
DEFAULT_PORT = 3306
HOST = "127.0.0.1"


# ----------------------------------------------------------------------------------------------
# Dipendenze
# ----------------------------------------------------------------------------------------------
def deps_ok() -> bool:
    try:
        import mysql_mimic  # noqa: F401
        import sqlglot  # noqa: F401
        return True
    except ImportError:
        return False


def install_deps(log=print) -> bool:
    log("Installo le dipendenze: " + " ".join(REQUIRED))
    cmd = [sys.executable, "-m", "pip", "install", "--quiet", *REQUIRED]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        log(r.stderr.strip() or r.stdout.strip())
        return False
    return deps_ok()


# ----------------------------------------------------------------------------------------------
# Server
# ----------------------------------------------------------------------------------------------
def _db_path(name: str) -> Path:
    safe = re.sub(r"[^A-Za-z0-9_\-]", "_", name)
    return DATA_DIR / f"{safe}.db"


def list_databases():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    return sorted(p.stem for p in DATA_DIR.glob("*.db"))


_SQLITE_TO_MYSQL = {"INTEGER": "int", "INT": "int", "TEXT": "text", "REAL": "double", "BLOB": "blob", "NUMERIC": "decimal"}


def build_schema():
    """{db: {table: {col: type}}} per SHOW TABLES / DESCRIBE / information_schema."""
    schema = {}
    for db in list_databases():
        con = sqlite3.connect(_db_path(db))
        try:
            tables = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")]
            schema[db] = {}
            for t in tables:
                cols = {}
                for _, cname, ctype, *_rest in con.execute(f'PRAGMA table_info("{t}")'):
                    base = (ctype or "TEXT").split("(")[0].strip().upper()
                    cols[cname] = _SQLITE_TO_MYSQL.get(base, base.lower() or "text")
                schema[db][t] = cols
        finally:
            con.close()
    return schema


def make_server(port: int, log):
    """Costruisce il server. Importa le librerie qui, cosi' la GUI puo' installarle prima."""
    from mysql_mimic import MysqlServer, Session
    from mysql_mimic.connection import Connection
    from mysql_mimic.auth import IdentityProvider, NativePasswordAuthPlugin, User
    from mysql_mimic.errors import MysqlError
    from mysql_mimic.results import ColumnType, ResultColumn, infer_type
    from sqlglot import exp
    from sqlglot.errors import SqlglotError

    class AcceptAllPlugin(NativePasswordAuthPlugin):
        """Per le lezioni: qualunque utente e qualunque password entrano."""

        def password_matches(self, user, scramble, nonce):
            return True

        def empty_password_quickpath(self, user, scramble):
            return True

    class AcceptAllIdentity(IdentityProvider):
        def get_plugins(self):
            return [AcceptAllPlugin()]

        async def get_user(self, username):
            return User(name=username, auth_plugin=AcceptAllPlugin.name)

    # --- patch minimo: la libreria non permette di restituire affected_rows / last_insert_id
    # per INSERT/UPDATE/DELETE. Senza, cursor.rowcount e cursor.lastrowid valgono sempre 0.
    if not getattr(Connection, "_mini_patched", False):
        _orig_ok = Connection.ok

        def _ok(self, **kwargs):
            pending = getattr(self.session, "_pending_ok", None)
            if pending is not None and not kwargs:
                self.session._pending_ok = None
                kwargs = {"affected_rows": pending[0], "last_insert_id": pending[1]}
            return _orig_ok(self, **kwargs)

        Connection.ok = _ok
        Connection._mini_patched = True

    class SqliteSession(Session):
        def __init__(self):
            self._database = None
            super().__init__()
            self._con = None
            self._con_db = None
            self._pending_ok = None

        @property
        def database(self):
            return self._database

        @database.setter
        def database(self, value):
            if value and not _db_path(value).exists():
                raise MysqlError(f"Unknown database '{value}'", 1049)
            self._database = value

        async def handle_query(self, sql, attrs):
            if re.match(r"^\s*SHOW\s+(DATABASES|SCHEMAS)\s*;?\s*$", sql, re.I):
                log(f"[{self.username or '?'}@{self.database or '-'}] {sql.strip()}")
                names = ["information_schema", "mysql"] + list_databases()
                return [(n,) for n in names], ["Database"]
            head = re.sub(r"\s+", " ", sql).strip().rstrip(";").strip().upper()
            if head in ("COMMIT", "ROLLBACK", "BEGIN", "START TRANSACTION"):
                log(f"[{self.username or '?'}@{self.database or '-'}] {head}")
                if self._con is not None:
                    if head == "COMMIT":
                        self._con.commit()
                    elif head == "ROLLBACK":
                        self._con.rollback()
                return [], []
            try:
                return await super().handle_query(sql, attrs)
            except SqlglotError as e:
                first = re.sub(r"\x1b\[[0-9;]*m", "", str(e)).strip().splitlines()[0]
                raise MysqlError(f"You have an error in your SQL syntax; {first}", 1064)

        # -- connessione SQLite per il database selezionato
        def _connection_for_db(self):
            if not self.database:
                raise MysqlError("No database selected", 1046)
            if self._con is None or self._con_db != self.database:
                if self._con is not None:
                    self._con.close()
                path = _db_path(self.database)
                if not path.exists():
                    raise MysqlError(f"Unknown database '{self.database}'", 1049)
                self._con = sqlite3.connect(path, check_same_thread=False, timeout=5)
                self._con_db = self.database
            return self._con

        async def schema(self):
            return build_schema()

        async def close(self):
            if self._con is not None:
                try:
                    self._con.rollback()
                finally:
                    self._con.close()

        def _autocommit(self) -> bool:
            val = self.variables.get("autocommit", 1)
            return str(val).upper() not in ("0", "OFF", "FALSE")

        async def query(self, expression, sql, attrs):
            flat = re.sub(r"\s+", " ", sql).strip()[:300]
            log(f"[{self.username or '?'}@{self.database or '-'}] {flat}")

            # --- CREATE / DROP DATABASE
            if isinstance(expression, exp.Create) and (expression.args.get("kind") or "").upper() in ("DATABASE", "SCHEMA"):
                name = expression.this.name
                path = _db_path(name)
                if path.exists():
                    if expression.args.get("exists"):
                        return [], []
                    raise MysqlError(f"Can't create database '{name}'; database exists", 1007)
                DATA_DIR.mkdir(parents=True, exist_ok=True)
                sqlite3.connect(path).close()
                self._pending_ok = (1, 0)
                return [], []

            if isinstance(expression, exp.Drop) and (expression.args.get("kind") or "").upper() in ("DATABASE", "SCHEMA"):
                name = expression.this.name
                path = _db_path(name)
                if not path.exists():
                    if expression.args.get("exists"):
                        return [], []
                    raise MysqlError(f"Can't drop database '{name}'; database doesn't exist", 1008)
                if self._con is not None and self._con_db == name:
                    self._con.close()
                    self._con = None
                path.unlink()
                if self.database == name:
                    self.database = None
                return [], []

            # --- transazioni
            if isinstance(expression, exp.Commit):
                if self._con is not None:
                    self._con.commit()
                return [], []
            if isinstance(expression, exp.Rollback):
                if self._con is not None:
                    self._con.rollback()
                return [], []

            # --- tutto il resto: traduci MySQL -> SQLite ed esegui
            con = self._connection_for_db()
            try:
                sqlite_sql = expression.sql(dialect="sqlite")
                cur = con.execute(sqlite_sql)
            except sqlite3.IntegrityError as e:
                msg = str(e)
                if "UNIQUE" in msg or "PRIMARY KEY" in msg:
                    raise MysqlError(f"Duplicate entry ({msg})", 1062)
                raise MysqlError(msg, 1364)
            except sqlite3.OperationalError as e:
                msg = str(e)
                if "locked" in msg:
                    raise MysqlError("Lock wait timeout exceeded; try restarting transaction", 1205)
                if msg.startswith("no such table"):
                    raise MysqlError(f"Table '{self.database}.{msg.split(':')[-1].strip()}' doesn't exist", 1146)
                if msg.startswith("table") and "already exists" in msg:
                    raise MysqlError(msg.replace("table", "Table", 1), 1050)
                if msg.startswith("no such column"):
                    raise MysqlError(f"Unknown column '{msg.split(':')[-1].strip()}' in 'field list'", 1054)
                raise MysqlError(msg, 1064)
            except sqlite3.Error as e:
                raise MysqlError(str(e), 1064)

            if cur.description:  # SELECT & co.
                rows = cur.fetchall()
                cols = []
                for i, d in enumerate(cur.description):
                    sample = next((r[i] for r in rows if r[i] is not None), None)
                    ctype = infer_type(sample) if sample is not None else ColumnType.NULL
                    cols.append(ResultColumn(name=str(d[0]), type=ctype))
                return rows, cols

            # INSERT / UPDATE / DELETE / DDL
            if self._autocommit():
                con.commit()
            is_insert = isinstance(expression, exp.Insert)
            self._pending_ok = (max(cur.rowcount, 0), cur.lastrowid if is_insert else 0)
            return [], []

    server = MysqlServer(session_factory=SqliteSession, identity_provider=AcceptAllIdentity(), host=HOST, port=port)
    return server


class ServerThread:
    """Gira in un thread con il suo event loop, cosi' la GUI Tk non si blocca."""

    def __init__(self, port: int, log):
        self.port, self.log = port, log
        self.loop = None
        self.server = None
        self._ready = threading.Event()
        self.error = None
        self.thread = threading.Thread(target=self._run, daemon=True)

    def start(self):
        self.thread.start()
        self._ready.wait(10)
        return self.error is None

    def _run(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        try:
            self.server = make_server(self.port, self.log)
            self.loop.run_until_complete(self.server.start_server())
        except OSError as e:
            self.error = f"Porta {self.port} non disponibile: {e}"
            self._ready.set()
            return
        except Exception as e:  # noqa: BLE001
            self.error = f"{type(e).__name__}: {e}"
            self._ready.set()
            return
        self._ready.set()
        try:
            self.loop.run_forever()
        finally:
            self.loop.close()

    def stop(self):
        if not self.loop or not self.server:
            return

        async def _close():
            self.server.close()
            await self.server.wait_closed()

        fut = asyncio.run_coroutine_threadsafe(_close(), self.loop)
        try:
            fut.result(5)
        except Exception:  # noqa: BLE001
            pass
        self.loop.call_soon_threadsafe(self.loop.stop)
        self.thread.join(3)


# ----------------------------------------------------------------------------------------------
# GUI
# ----------------------------------------------------------------------------------------------
def run_gui(port: int):
    import tkinter as tk
    from tkinter import messagebox, scrolledtext

    root = tk.Tk()
    root.title("Mini-XAMPP (MySQL locale)")
    root.geometry("720x560")

    logq: "queue.Queue[str]" = queue.Queue()
    state = {"srv": None}

    top = tk.Frame(root, padx=10, pady=8)
    top.pack(fill="x")
    tk.Label(top, text="Host:").grid(row=0, column=0, sticky="w")
    tk.Label(top, text=HOST, font=("TkFixedFont", 10, "bold")).grid(row=0, column=1, sticky="w", padx=(4, 16))
    tk.Label(top, text="Porta:").grid(row=0, column=2, sticky="w")
    port_var = tk.StringVar(value=str(port))
    tk.Entry(top, textvariable=port_var, width=7).grid(row=0, column=3, padx=(4, 16))
    status = tk.Label(top, text="● fermo", fg="#b00020", font=("TkDefaultFont", 10, "bold"))
    status.grid(row=0, column=4, sticky="w")

    btns = tk.Frame(root, padx=10)
    btns.pack(fill="x")

    snippet = tk.Text(root, height=9, font=("TkFixedFont", 10), padx=6, pady=4)
    snippet.pack(fill="x", padx=10, pady=(8, 4))

    def refresh_snippet():
        p = port_var.get().strip() or str(DEFAULT_PORT)
        snippet.config(state="normal")
        snippet.delete("1.0", "end")
        snippet.insert(
            "1.0",
            "import mysql.connector\n\n"
            "conn = mysql.connector.connect(\n"
            f'    host="{HOST}", port={p},\n'
            '    user="root", password=""\n'
            ")\n"
            "cur = conn.cursor()\n"
            'cur.execute("CREATE DATABASE IF NOT EXISTS scuola")\n',
        )
        snippet.config(state="disabled")

    logbox = scrolledtext.ScrolledText(root, height=12, font=("TkFixedFont", 9), state="disabled")
    logbox.pack(fill="both", expand=True, padx=10, pady=(4, 10))

    def log(msg: str):
        logq.put(msg)

    def pump():
        try:
            while True:
                m = logq.get_nowait()
                logbox.config(state="normal")
                logbox.insert("end", m + "\n")
                logbox.see("end")
                logbox.config(state="disabled")
        except queue.Empty:
            pass
        root.after(150, pump)

    def set_running(running: bool):
        status.config(text="● attivo" if running else "● fermo", fg="#1b7f2a" if running else "#b00020")
        start_btn.config(state="disabled" if running else "normal")
        stop_btn.config(state="normal" if running else "disabled")

    def start():
        if not deps_ok():
            if messagebox.askyesno("Dipendenze", "Mancano le librerie Python necessarie.\nInstallarle ora con pip?"):
                log("Installazione dipendenze in corso...")
                root.update_idletasks()
                if not install_deps(log):
                    messagebox.showerror("Errore", "Installazione fallita. Guarda il log.")
                    return
            else:
                return
        try:
            p = int(port_var.get())
        except ValueError:
            messagebox.showerror("Errore", "Porta non valida")
            return
        srv = ServerThread(p, log)
        if not srv.start():
            messagebox.showerror("Errore", srv.error or "Avvio fallito")
            log(srv.error or "Avvio fallito")
            return
        state["srv"] = srv
        refresh_snippet()
        log(f"Server in ascolto su {HOST}:{p}  (dati in {DATA_DIR})")
        set_running(True)

    def stop():
        srv = state["srv"]
        if srv:
            srv.stop()
            state["srv"] = None
            log("Server fermato.")
        set_running(False)

    def reset():
        if state["srv"]:
            messagebox.showinfo("Reset", "Ferma prima il server.")
            return
        if messagebox.askyesno("Reset", f"Cancellare TUTTI i database in\n{DATA_DIR} ?"):
            shutil.rmtree(DATA_DIR, ignore_errors=True)
            log("Tutti i dati cancellati.")

    def open_folder():
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        if sys.platform.startswith("win"):
            os.startfile(DATA_DIR)  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            subprocess.run(["open", str(DATA_DIR)])
        else:
            subprocess.run(["xdg-open", str(DATA_DIR)])

    def copy_snippet():
        root.clipboard_clear()
        root.clipboard_append(snippet.get("1.0", "end").strip())
        log("Codice di connessione copiato negli appunti.")

    start_btn = tk.Button(btns, text="Start", width=10, command=start)
    stop_btn = tk.Button(btns, text="Stop", width=10, command=stop, state="disabled")
    start_btn.pack(side="left")
    stop_btn.pack(side="left", padx=6)
    tk.Button(btns, text="Copia codice", command=copy_snippet).pack(side="left", padx=6)
    tk.Button(btns, text="Apri cartella dati", command=open_folder).pack(side="left", padx=6)
    tk.Button(btns, text="Reset dati", command=reset).pack(side="right")

    def on_close():
        stop()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    refresh_snippet()
    pump()
    log("Premi Start. NB: e' un'emulazione SQLite del protocollo MySQL, non MySQL vero.")
    root.mainloop()


# ----------------------------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="Mini-XAMPP: finto server MySQL locale in Python")
    ap.add_argument("--port", type=int, default=DEFAULT_PORT)
    ap.add_argument("--headless", action="store_true", help="senza GUI")
    args = ap.parse_args()

    if not deps_ok() and args.headless and not install_deps():
        sys.exit("Impossibile installare le dipendenze.")

    if args.headless:
        srv = ServerThread(args.port, print)
        if not srv.start():
            sys.exit(srv.error)
        print(f"Server MySQL (emulato) su {HOST}:{args.port} - Ctrl+C per uscire")
        try:
            while True:
                threading.Event().wait(1)
        except KeyboardInterrupt:
            srv.stop()
    else:
        run_gui(args.port)


if __name__ == "__main__":
    main()