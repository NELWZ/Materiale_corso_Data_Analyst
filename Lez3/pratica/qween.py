import tkinter as tk
from tkinter import messagebox


class TimerApp:
    """Timer professionale con dark mode e controllo completo."""

    # Palette dark mode (Catppuccin-inspired)
    COLORS = {
        "bg": "#1e1e2e",
        "surface": "#313244",
        "surface_hover": "#45475a",
        "fg": "#cdd6f4",
        "fg_dim": "#a6adc8",
        "accent": "#89b4fa",
        "green": "#a6e3a1",
        "red": "#f38ba8",
        "yellow": "#f9e2af",
        "blue": "#89dceb",
        "border": "#585b70",
    }

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Timer Pro")
        self.root.geometry("420x380")
        self.root.configure(bg=self.COLORS["bg"])
        self.root.resizable(False, False)

        # Stato
        self.ore = self.minuti = self.secondi = 0
        self.total_seconds = 0
        self.job = None
        self.running = False
        self.paused = False

        self._build_ui()

    # ---------- UI ----------
    def _build_ui(self):
        # Titolo
        title = tk.Label(
            self.root,
            text="⏱  TIMER PRO",
            font=("Segoe UI", 18, "bold"),
            bg=self.COLORS["bg"],
            fg=self.COLORS["accent"],
        )
        title.pack(pady=(18, 10))

        # Frame input
        input_frame = tk.Frame(self.root, bg=self.COLORS["bg"])
        input_frame.pack(pady=8)

        labels = ("Ore", "Min", "Sec")
        self.entries = []
        for i, lbl in enumerate(labels):
            col = tk.Frame(input_frame, bg=self.COLORS["bg"])
            col.grid(row=0, column=i, padx=10)

            tk.Label(
                col, text=lbl, font=("Segoe UI", 10),
                bg=self.COLORS["bg"], fg=self.COLORS["fg_dim"]
            ).pack()

            entry = tk.Entry(
                col, width=5, font=("Consolas", 14, "bold"),
                bg=self.COLORS["surface"], fg=self.COLORS["fg"],
                insertbackground=self.COLORS["fg"],
                relief="flat", bd=0, justify="center",
                highlightthickness=1,
                highlightbackground=self.COLORS["border"],
                highlightcolor=self.COLORS["accent"],
            )
            entry.pack(ipady=6)
            entry.insert(0, "0")
            entry.bind("<FocusIn>", lambda e, ent=entry: ent.select_range(0, tk.END))
            self.entries.append(entry)

        # Display
        self.display = tk.Label(
            self.root, text="00:00:00",
            font=("Consolas", 42, "bold"),
            bg=self.COLORS["surface"], fg=self.COLORS["fg"],
            relief="flat", padx=30, pady=12,
            highlightthickness=1,
            highlightbackground=self.COLORS["border"],
        )
        self.display.pack(pady=18)

        # Status
        self.status = tk.Label(
            self.root, text="Pronto",
            font=("Segoe UI", 9, "italic"),
            bg=self.COLORS["bg"], fg=self.COLORS["fg_dim"],
        )
        self.status.pack()

        # Pulsanti
        btn_frame = tk.Frame(self.root, bg=self.COLORS["bg"])
        btn_frame.pack(pady=15)

        buttons = [
            ("▶  Avvia", self.COLORS["green"], self.avvia),
            ("❚❚ Pausa", self.COLORS["yellow"], self.pausa),
            ("■  Stop",  self.COLORS["red"],   self.stop),
            ("⟲  Reset", self.COLORS["blue"],  self.reset),
        ]
        for text, color, cmd in buttons:
            self._make_button(btn_frame, text, color, cmd).pack(side=tk.LEFT, padx=5)

    def _make_button(self, parent, text, color, command):
        btn = tk.Button(
            parent, text=text, command=command,
            font=("Segoe UI", 10, "bold"),
            bg=self.COLORS["surface"], fg=color,
            activebackground=self.COLORS["surface_hover"],
            activeforeground=color,
            relief="flat", bd=0, padx=12, pady=6,
            cursor="hand2",
            highlightthickness=1,
            highlightbackground=color,
        )
        # Hover effect
        btn.bind("<Enter>", lambda e, b=btn, c=color: b.config(bg=self.COLORS["surface_hover"]))
        btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.COLORS["surface"]))
        return btn

    # ---------- Logica ----------
    def _aggiorna_display(self):
        self.display.config(text=f"{self.ore:02d}:{self.minuti:02d}:{self.secondi:02d}")

    def _set_status(self, text, color=None):
        self.status.config(text=text, fg=color or self.COLORS["fg_dim"])

    def _read_inputs(self):
        try:
            h = int(self.entries[0].get() or 0)
            m = int(self.entries[1].get() or 0)
            s = int(self.entries[2].get() or 0)
        except ValueError:
            messagebox.showwarning("Input non valido", "Inserisci solo numeri interi.")
            return None
        if not (0 <= h <= 99 and 0 <= m <= 59 and 0 <= s <= 59):
            messagebox.showwarning("Input non valido", "Ore: 0-99, Min: 0-59, Sec: 0-59")
            return None
        if h == m == s == 0:
            messagebox.showinfo("Timer", "Imposta un tempo maggiore di 0.")
            return None
        return h, m, s

    def avvia(self):
        if self.paused:
            # Riprendi
            self.paused = False
            self.running = True
            self._set_status("In esecuzione...", self.COLORS["green"])
            self._tick()
            return

        if self.running:
            return

        data = self._read_inputs()
        if data is None:
            return
        self.ore, self.minuti, self.secondi = data
        self.total_seconds = self.ore * 3600 + self.minuti * 60 + self.secondi
        self.running = True
        self._set_status("In esecuzione...", self.COLORS["green"])
        self._tick()

    def _tick(self):
        if not self.running or self.paused:
            return

        self._aggiorna_display()

        if self.ore == self.minuti == self.secondi == 0:
            self.running = False
            self._set_status("✓ Tempo scaduto", self.COLORS["yellow"])
            self.root.bell()
            messagebox.showinfo("Timer", "⏰ Tempo scaduto!")
            return

        # Decrementa
        if self.secondi > 0:
            self.secondi -= 1
        elif self.minuti > 0:
            self.minuti -= 1
            self.secondi = 59
        elif self.ore > 0:
            self.ore -= 1
            self.minuti = 59
            self.secondi = 59

        self.job = self.root.after(1000, self._tick)

    def pausa(self):
        if not self.running:
            return
        if self.paused:
            self.avvia()  # riprendi
            return
        self.paused = True
        if self.job:
            self.root.after_cancel(self.job)
            self.job = None
        self._set_status("⏸  In pausa", self.COLORS["yellow"])

    def stop(self):
        self.running = False
        self.paused = False
        if self.job:
            self.root.after_cancel(self.job)
            self.job = None
        self.ore = self.minuti = self.secondi = 0
        self._aggiorna_display()
        self._set_status("■  Fermato", self.COLORS["red"])

    def reset(self):
        self.stop()
        for e in self.entries:
            e.delete(0, tk.END)
            e.insert(0, "0")
        self._set_status("Pronto")


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()