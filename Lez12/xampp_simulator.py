import sys
import random
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Evita l'interfaccia sfocata su Windows con display ad alta risoluzione (DPI scaling)
if sys.platform == 'win32':
    try:
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass

BG = '#f1f1f1'
GREEN = '#27833b'


class XamppSimulator:
    def __init__(self, root):
        self.root = root
        root.title('XAMPP Control Panel Simulator')
        root.geometry('900x600')
        root.minsize(860, 580)
        root.configure(bg=BG)
        root.protocol('WM_DELETE_WINDOW', self.quit_app)

        self.services = {
            'Apache': {'running': False, 'ports': '80, 443', 'pid': None},
            'MySQL': {'running': False, 'ports': '3306', 'pid': None},
            'FileZilla': {'running': False, 'ports': '21, 14147', 'pid': None},
            'Mercury': {'running': False, 'ports': '25, 110, 143', 'pid': None},
            'Tomcat': {'running': False, 'ports': '8080, 8009', 'pid': None},
        }
        self.windows = {}
        self.build_ui()
        self.log('XAMPP Simulator initialized.')
        self.log('Ready. This application does not start real services.')

    # ---------- UI ----------
    def build_ui(self):
        top = tk.Frame(self.root, bg=BG)
        top.pack(side='top', fill='x', padx=16, pady=(12, 6))
        tk.Label(top, text='XAMPP', font=('Segoe UI', 25, 'bold'), fg='#333', bg=BG).pack(side='left')
        tk.Label(top, text='CONTROL PANEL  •  SIMULATOR', font=('Segoe UI', 10), fg='#777', bg=BG).pack(side='left', padx=12, pady=(12, 0))

        # Logs e controlli vengono impacchettati PRIMA del corpo centrale:
        # se la finestra si restringe, a ridursi è l'area centrale e non log/pulsanti.
        log_frame = tk.LabelFrame(self.root, text='Logs', font=('Segoe UI', 10, 'bold'), bg=BG, padx=6, pady=6)
        log_frame.pack(side='bottom', fill='both', padx=16, pady=(0, 12))
        scrollbar = ttk.Scrollbar(log_frame, orient='vertical')
        scrollbar.pack(side='right', fill='y')  # prima della Text, così non sparisce mai
        self.log_box = tk.Text(log_frame, height=9, bg='#fff', fg='#333', font=('Consolas', 9),
                               wrap='word', state='disabled', yscrollcommand=scrollbar.set)
        self.log_box.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.log_box.yview)

        control = tk.Frame(self.root, bg=BG)
        control.pack(side='bottom', fill='x', padx=16, pady=(0, 8))
        tk.Button(control, text='Start All', width=12, command=self.start_all).pack(side='left', padx=(0, 5))
        tk.Button(control, text='Stop All', width=12, command=self.stop_all).pack(side='left', padx=5)
        self.status = tk.Label(control, text='Status: Ready', bg=BG, fg='#555', anchor='w')
        self.status.pack(side='left', padx=15)

        main = tk.Frame(self.root, bg=BG)
        main.pack(side='top', fill='both', expand=True, padx=16, pady=6)

        modules = tk.LabelFrame(main, text='Modules', font=('Segoe UI', 10, 'bold'), bg=BG, padx=8, pady=8)
        modules.pack(side='left', fill='both', expand=True)
        for col, text in enumerate(['Service', 'PID', 'Port(s)', 'Actions']):
            tk.Label(modules, text=text, font=('Segoe UI', 9, 'bold'), bg=BG, fg='#444').grid(
                row=0, column=col, padx=5, pady=5, sticky='w')

        self.rows = {}
        for i, name in enumerate(self.services, start=1):
            name_lbl = tk.Label(modules, text=name, font=('Segoe UI', 10), bg=BG, width=10, anchor='w')
            name_lbl.grid(row=i, column=0, padx=5, pady=5, sticky='w')
            pid = tk.Label(modules, text='—', bg=BG, width=9, anchor='w')
            pid.grid(row=i, column=1, padx=5, pady=5, sticky='w')
            tk.Label(modules, text=self.services[name]['ports'], bg=BG, width=13, anchor='w').grid(
                row=i, column=2, padx=5, pady=5, sticky='w')
            actions = tk.Frame(modules, bg=BG)
            actions.grid(row=i, column=3, padx=3, pady=3)
            start = tk.Button(actions, text='Start', width=6, command=lambda n=name: self.start_service(n))
            start.pack(side='left', padx=2)
            stop = tk.Button(actions, text='Stop', width=6, command=lambda n=name: self.stop_service(n), state='disabled')
            stop.pack(side='left', padx=2)
            admin = tk.Button(actions, text='Admin', width=6, command=lambda n=name: self.admin(n))
            admin.pack(side='left', padx=2)
            self.rows[name] = {'name': name_lbl, 'pid': pid, 'start': start, 'stop': stop, 'admin': admin}

        side = tk.Frame(main, bg=BG, width=150)
        side.pack(side='right', fill='y', padx=(10, 0))
        side.pack_propagate(False)
        for label, cmd in [('Config', self.config_dialog), ('Netstat', self.netstat), ('Shell', self.shell_info),
                           ('Explorer', self.explorer_info), ('Services', self.services_info),
                           ('Help', self.help_info), ('Quit', self.quit_app)]:
            tk.Button(side, text=label, width=17, command=cmd).pack(fill='x', pady=3)
        tk.Label(side, text='SIMULATION MODE', fg='#a33', font=('Segoe UI', 9, 'bold'), bg=BG).pack(pady=(18, 2))
        tk.Label(side, text='No real server processes', fg='#777', bg=BG, font=('Segoe UI', 8)).pack()

    # ---------- Logging ----------
    def log(self, text):
        stamp = datetime.now().strftime('%H:%M:%S')
        self.log_box.configure(state='normal')
        self.log_box.insert('end', f'[{stamp}] {text}\n')
        self.log_box.see('end')
        self.log_box.configure(state='disabled')

    # ---------- Service control ----------
    def _new_pid(self):
        used = {s['pid'] for s in self.services.values() if s['pid']}
        while True:
            pid = random.randint(1200, 9800)
            if pid not in used:
                return pid

    def start_service(self, name, quiet=False):
        service = self.services[name]
        if service['running']:
            if not quiet:
                self.log(f'{name} is already running.')
            return False
        service['running'] = True
        service['pid'] = self._new_pid()
        row = self.rows[name]
        row['pid'].config(text=str(service['pid']))
        row['name'].config(bg='#b6e8b9')  # evidenzia il modulo attivo, come in XAMPP
        row['start'].config(state='disabled')
        row['stop'].config(state='normal')
        if not quiet:
            self.status.config(text=f'Status: {name} started', fg=GREEN)
        self.log(f'{name}: started successfully (simulated). PID {service["pid"]}; ports {service["ports"]}.')
        return True

    def stop_service(self, name, quiet=False):
        service = self.services[name]
        if not service['running']:
            if not quiet:
                self.log(f'{name} is not running.')
            return False
        service['running'] = False
        service['pid'] = None
        row = self.rows[name]
        row['pid'].config(text='—')
        row['name'].config(bg=BG)
        row['start'].config(state='normal')
        row['stop'].config(state='disabled')
        self.close_window(name)
        if not quiet:
            self.status.config(text=f'Status: {name} stopped', fg='#555')
        self.log(f'{name}: stopped (simulated).')
        return True

    def start_all(self):
        changed = [self.start_service(n, quiet=True) for n in self.services]
        if any(changed):
            self.status.config(text='Status: all services started (simulated)', fg=GREEN)
        else:
            self.log('All services are already running.')

    def stop_all(self):
        changed = [self.stop_service(n, quiet=True) for n in list(self.services)]
        if any(changed):
            self.status.config(text='Status: all services stopped', fg='#555')
        else:
            self.log('No services are running.')

    # ---------- Dialogs ----------
    def admin(self, name):
        if not self.services[name]['running']:
            messagebox.showwarning('Service stopped', f'{name} is not running. Start it first (simulated).')
            return
        if name == 'MySQL':
            self.open_window('MySQL', self.build_phpmyadmin)
            self.log('Admin: phpMyAdmin opened (simulated).')
        elif name == 'Apache':
            self.open_window('Apache', self.build_dashboard)
            self.log('Admin: XAMPP dashboard opened (simulated).')
        else:
            messagebox.showinfo('Admin', f'{name} admin action is simulated.')
            self.log(f'Admin clicked for {name} (simulated).')

    def open_window(self, service, builder):
        win = self.windows.get(service)
        if win and win.winfo_exists():
            win.lift()
            win.focus_force()
            return
        win = tk.Toplevel(self.root)
        self.windows[service] = win
        builder(win)

    def close_window(self, service):
        win = self.windows.pop(service, None)
        if win and win.winfo_exists():
            win.destroy()

    def build_dashboard(self, win):
        win.title('Welcome to XAMPP - http://localhost/dashboard/ (simulated)')
        win.geometry('560x320')
        win.configure(bg='#fff')
        tk.Label(win, text='Welcome to XAMPP for Windows 8.2.12', font=('Segoe UI', 16, 'bold'),
                 bg='#fff', fg='#fb7a24').pack(pady=(24, 8))
        tk.Label(win, text='You have successfully installed XAMPP on this system!\n(simulated: nothing is really installed)',
                 bg='#fff', fg='#444', font=('Segoe UI', 10)).pack(pady=6)
        row = tk.Frame(win, bg='#fff')
        row.pack(pady=20)
        for label, cmd in [('Applications', None), ('phpMyAdmin', self.admin_from_dashboard), ('Webalizer', None), ('FAQs', None)]:
            tk.Button(row, text=label, width=14,
                      command=cmd or (lambda l=label: messagebox.showinfo(l, 'Simulated page.', parent=win))).pack(side='left', padx=4)
        tk.Label(win, text='Apache/2.4.58 (Win64) OpenSSL/3.1.3 PHP/8.2.12 Server at localhost Port 80',
                 bg='#fff', fg='#888', font=('Consolas', 8)).pack(side='bottom', pady=10)

    def admin_from_dashboard(self):
        if self.services['MySQL']['running']:
            self.admin('MySQL')
        else:
            messagebox.showerror('phpMyAdmin', '#2002 Cannot connect: MySQL is not running (simulated).')

    def build_phpmyadmin(self, win):
        win.title('localhost / 127.0.0.1 | phpMyAdmin 5.2.1 (simulated)')
        win.geometry('820x500')
        win.minsize(700, 420)
        win.configure(bg='#fff')
        data = {
            'information_schema': [('TABLES', 0, 'Aria'), ('COLUMNS', 0, 'Aria'), ('USER_PRIVILEGES', 0, 'Aria')],
            'mysql': [('user', 3, 'Aria'), ('db', 2, 'Aria'), ('proxies_priv', 1, 'Aria')],
            'performance_schema': [('events_waits_current', 0, 'PERFORMANCE_SCHEMA')],
            'phpmyadmin': [('pma__bookmark', 0, 'InnoDB'), ('pma__history', 0, 'InnoDB')],
            'test': [('utenti', 12, 'InnoDB'), ('ordini', 48, 'InnoDB')],
        }
        bar = tk.Frame(win, bg='#e8eef7')
        bar.pack(fill='x')
        tk.Label(bar, text='phpMyAdmin', font=('Segoe UI', 13, 'bold'), bg='#e8eef7', fg='#235a81').pack(side='left', padx=10, pady=6)
        tk.Label(bar, text='Server: 127.0.0.1   User: root@localhost', bg='#e8eef7', fg='#555').pack(side='right', padx=10)

        body = tk.Frame(win, bg='#fff')
        body.pack(fill='both', expand=True)
        tree = ttk.Treeview(body, show='tree', selectmode='browse')
        tree.pack(side='left', fill='y')
        for db, tables in data.items():
            node = tree.insert('', 'end', iid=db, text=db)
            for t, _, _ in tables:
                tree.insert(node, 'end', text=t)

        right = tk.Frame(body, bg='#fff')
        right.pack(side='left', fill='both', expand=True, padx=10, pady=8)
        title = tk.Label(right, text='Server: 127.0.0.1', font=('Segoe UI', 11, 'bold'), bg='#fff', anchor='w')
        title.pack(fill='x')
        info = tk.Label(right, justify='left', anchor='w', bg='#fff', fg='#333', font=('Consolas', 9),
                        text='Server version: 10.4.32-MariaDB\nProtocol version: 10\n'
                             'Server charset: UTF-8 Unicode (utf8mb4)\nWeb server: Apache/2.4.58 (Win64)\n'
                             'Database client: libmysql - mysqlnd 8.2.12')
        info.pack(fill='x', pady=8)
        cols = ('Table', 'Rows', 'Type', 'Collation')
        table = ttk.Treeview(right, columns=cols, show='headings', height=10)
        for c in cols:
            table.heading(c, text=c)
            table.column(c, width=120, anchor='w')
        table.pack(fill='both', expand=True)

        def on_select(_event=None):
            sel = tree.selection()
            if not sel:
                return
            db = sel[0] if sel[0] in data else tree.parent(sel[0])
            title.config(text=f'Server: 127.0.0.1  »  Database: {db}')
            info.config(text=f'{len(data[db])} tables in {db} (simulated data)')
            table.delete(*table.get_children())
            for t, rows, eng in data[db]:
                table.insert('', 'end', values=(t, rows, eng, 'utf8mb4_general_ci'))

        tree.bind('<<TreeviewSelect>>', on_select)

    def config_dialog(self):
        messagebox.showinfo('Config', 'Configuration menu (simulator):\n\nApache, PHP, MySQL, phpMyAdmin configuration entries would appear here.')
        self.log('Config menu opened.')

    def netstat(self):
        running = [f'{n}: {s["ports"]}' for n, s in self.services.items() if s['running']]
        messagebox.showinfo('Netstat (simulated)', '\n'.join(running) if running else 'No simulated services running.')
        self.log('Netstat view opened.')

    def shell_info(self):
        messagebox.showinfo('Shell', 'A terminal would open in real XAMPP.\nThis simulator does not execute commands.')
        self.log('Shell requested; execution disabled in simulator.')

    def explorer_info(self):
        messagebox.showinfo('Explorer', 'File explorer action is simulated.\nNo folders are opened.')
        self.log('Explorer requested (simulated).')

    def services_info(self):
        messagebox.showinfo('Services', 'Windows services management is not available in this simulator.')
        self.log('Services menu opened.')

    def help_info(self):
        messagebox.showinfo('Help', 'XAMPP Control Panel Simulator\n\nStart/Stop buttons change simulated service state only.\nNo Apache, MySQL, PHP, or other services are installed or launched.')
        self.log('Help opened.')

    def quit_app(self):
        if any(s['running'] for s in self.services.values()):
            if not messagebox.askyesno('Quit', 'Some (simulated) services are still running.\nQuit anyway?'):
                return
        self.root.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    app = XamppSimulator(root)
    root.mainloop()