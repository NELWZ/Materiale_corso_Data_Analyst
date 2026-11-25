import csv
import random
import secrets
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk


def apply_seed(seed=None):
    """Imposta il generatore casuale globale, se serve a chi importa il modulo."""
    if seed is not None:
        random.seed(seed)


CITTA_REGIONI = [
    ('Milano', 'Lombardia'), ('Roma', 'Lazio'), ('Napoli', 'Campania'),
    ('Torino', 'Piemonte'), ('Palermo', 'Sicilia'), ('Genova', 'Liguria'),
    ('Bologna', 'Emilia-Romagna'), ('Firenze', 'Toscana'), ('Bari', 'Puglia'),
    ('Venezia', 'Veneto'), ('Matera', 'Basilicata'),
]

CATEGORIE = ['Elettronica', 'Casa', 'Sport', 'Alimentari', 'Abbigliamento']

PRODOTTI = {
    'Elettronica': ['Telefono', 'Laptop', 'Tablet', 'Cuffie', 'Microfono'],
    'Casa': ['Lampada', 'Divano', 'Tappeto', 'Piatti', 'Sedie'],
    'Sport': ['Panca', 'Manubri', 'Dischi', 'Zaino', 'Guanti'],
    'Alimentari': ['Pasta', 'Pane', 'Monster', 'Olio', 'Farina'],
    'Abbigliamento': ['Maglietta', 'Jeans', 'Giacca', 'Felpa', 'Scarpe'],
}

PREZZI = {
    'Elettronica': (50, 3500), 'Casa': (15, 6580), 'Sport': (10, 2000),
    'Alimentari': (2, 250), 'Abbigliamento': (10, 150),
}

CAMPI = [
    'data', 'città', 'regione', 'categoria', 'prodotto', 'prezzo_unitario',
    'quantità', 'totale', 'sconto', 'totale_scontato', 'tipo_di_cliente',
    'età_cliente', 'metodo_di_pagamento',
]


def crea_righe(numero_righe, seed=None):
    rng = random.Random(seed)
    righe = []
    for _ in range(numero_righe):
        mese = rng.randint(1, 12)
        giorno = rng.randint(1, 28)
        citta, regione = rng.choice(CITTA_REGIONI)
        categoria = rng.choice(CATEGORIE)
        prezzo_min, prezzo_max = PREZZI[categoria]
        prezzo_unit = round(rng.uniform(prezzo_min, prezzo_max), 2)
        quantita = rng.randint(1, 10)
        totale = round(prezzo_unit * quantita, 2)
        sconto = round(rng.uniform(0.05, 0.30), 2) if rng.random() < 0.2 else 0.0

        righe.append({
            'data': f'2024-{mese:02d}-{giorno:02d}',
            'città': citta,
            'regione': regione,
            'categoria': categoria,
            'prodotto': rng.choice(PRODOTTI[categoria]),
            'prezzo_unitario': prezzo_unit,
            'quantità': quantita,
            'totale': totale,
            'sconto': sconto,
            'totale_scontato': round(totale * (1 - sconto), 2),
            'tipo_di_cliente': rng.choice(['Nuovo', 'Fedele', 'VIP']),
            'età_cliente': rng.randint(18, 75),
            'metodo_di_pagamento': rng.choice(['Carta', 'Contanti', 'Bonifico', 'PayPal']),
        })
    return righe


def scrivi_csv(percorso, numero_righe, seed=None):
    righe = crea_righe(numero_righe, seed)
    with percorso.open('w', encoding='utf-8-sig', newline='') as file_csv:
        writer = csv.DictWriter(file_csv, fieldnames=CAMPI, delimiter=',')
        writer.writeheader()
        writer.writerows(righe)


class FileGenApp:
    BG = '#252b33'
    PANEL = '#303943'
    FG = '#edf1f5'
    MUTED = '#b6c0ca'
    ACCENT = '#55b6a8'

    def __init__(self, root):
        self.root = root
        root.title('FileGen — Generatore CSV')
        root.geometry('620x600')
        root.minsize(560, 510)
        root.configure(bg=self.BG)

        style = ttk.Style(root)
        style.theme_use('clam')
        style.configure('.', background=self.BG, foreground=self.FG, font=('Segoe UI', 10))
        style.configure('TFrame', background=self.BG)
        style.configure('Card.TFrame', background=self.PANEL)
        style.configure('TLabel', background=self.BG, foreground=self.FG)
        style.configure('Card.TLabel', background=self.PANEL, foreground=self.FG)
        style.configure('Hint.TLabel', background=self.BG, foreground=self.MUTED)
        style.configure('TEntry', fieldbackground='#f1f3f5', foreground='#20262d', padding=7)
        style.configure('Primary.TButton', background=self.ACCENT, foreground='#102421',
                        padding=(14, 9), font=('Segoe UI', 10, 'bold'))
        style.map('Primary.TButton', background=[('active', '#70c8bb')])
        style.configure('TButton', padding=(9, 6))

        container = ttk.Frame(root, padding=26)
        container.pack(fill='both', expand=True)
        ttk.Label(container, text='Generatore CSV', font=('Segoe UI', 20, 'bold')).pack(anchor='w')
        ttk.Label(container, text='Crea dati di vendita pronti da usare, in uno o più file.',
                  style='Hint.TLabel').pack(anchor='w', pady=(3, 18))

        card = ttk.Frame(container, style='Card.TFrame', padding=20)
        card.pack(fill='both', expand=True)
        card.columnconfigure(1, weight=1)

        self.righe_var = tk.StringVar(value='500')
        self.file_var = tk.StringVar(value='1')
        self.nome_file_var = tk.StringVar(value='vendite')
        self.nomi_casuali_var = tk.BooleanVar(value=False)
        self.seed_var = tk.StringVar(value='')
        self.cartella_var = tk.StringVar(value=str(Path.cwd()))

        self._campo(card, 0, 'Righe per file', self.righe_var)
        self._campo(card, 1, 'Numero di file', self.file_var)
        self._campo(card, 2, 'Nome file (senza estensione)', self.nome_file_var)
        ttk.Checkbutton(card, text='Usa nomi casuali per ogni file',
                        variable=self.nomi_casuali_var).grid(
                            row=3, column=0, columnspan=3, sticky='w', pady=6)
        self._campo(card, 4, 'Seed (opzionale)', self.seed_var)
        ttk.Label(card, text='Cartella di destinazione', style='Card.TLabel').grid(
            row=5, column=0, sticky='w', pady=(12, 4))
        ttk.Entry(card, textvariable=self.cartella_var).grid(
            row=6, column=0, columnspan=2, sticky='ew', padx=(0, 9))
        ttk.Button(card, text='Sfoglia…', command=self.scegli_cartella).grid(row=6, column=2)

        ttk.Label(card, text='CSV UTF-8', style='Card.TLabel').grid(
            row=7, column=0, columnspan=3,
                                            sticky='w', pady=(14, 0))

        self.genera_button = ttk.Button(container, text='Genera file', style='Primary.TButton',
                                        command=self.genera)
        self.genera_button.pack(fill='x', pady=(16, 8))
        self.stato = tk.StringVar(value='Pronto. Imposta i parametri o usa i valori predefiniti.')
        ttk.Label(container, textvariable=self.stato, style='Hint.TLabel',
                  wraplength=560).pack(anchor='w')

    @staticmethod
    def _campo(parent, riga, testo, variabile):
        ttk.Label(parent, text=testo, style='Card.TLabel').grid(
            row=riga, column=0, sticky='w', pady=6)
        ttk.Entry(parent, textvariable=variabile, width=18).grid(
            row=riga, column=1, columnspan=2, sticky='w', padx=(12, 0), pady=6)

    def scegli_cartella(self):
        cartella = filedialog.askdirectory(initialdir=self.cartella_var.get())
        if cartella:
            self.cartella_var.set(cartella)

    def genera(self):
        try:
            numero_righe = int(self.righe_var.get())
            numero_file = int(self.file_var.get())
            nome_file = self.nome_file_var.get().strip()
            if nome_file.lower().endswith('.csv'):
                nome_file = nome_file[:-4]
            if not nome_file or nome_file in {'.', '..'} or any(
                    separatore in nome_file for separatore in ('/', '\\')):
                raise ValueError('Inserisci un nome file valido, senza cartelle o estensione.')
            seed_testo = self.seed_var.get().strip()
            seed = int(seed_testo) if seed_testo else None
            cartella = Path(self.cartella_var.get()).expanduser()
            if not 1 <= numero_righe <= 1_000_000:
                raise ValueError('Le righe per file devono essere tra 1 e 1.000.000.')
            if not 1 <= numero_file <= 1000:
                raise ValueError('Il numero di file deve essere tra 1 e 1.000.')
            if not cartella.is_dir():
                raise ValueError('Seleziona una cartella di destinazione esistente.')
        except ValueError as errore:
            messagebox.showerror('Parametri non validi', str(errore), parent=self.root)
            return

        self.genera_button.configure(state='disabled')
        try:
            nomi_usati = set()
            for indice in range(numero_file):
                if self.nomi_casuali_var.get():
                    nome_generato = f'{nome_file}_{secrets.token_hex(4)}'
                    while nome_generato in nomi_usati:
                        nome_generato = f'{nome_file}_{secrets.token_hex(4)}'
                    nomi_usati.add(nome_generato)
                else:
                    nome_generato = f'{nome_file}_{indice + 1:03d}'
                percorso = cartella / f'{nome_generato}.csv'
                seed_file = seed + indice if seed is not None else None
                scrivi_csv(percorso, numero_righe, seed_file)
            self.stato.set(f'Completato: {numero_file} file × {numero_righe} righe in {cartella}')
            messagebox.showinfo('Operazione completata',
                                f'Creati {numero_file} file CSV in:\n{cartella}', parent=self.root)
        except OSError as errore:
            messagebox.showerror('Errore di scrittura', str(errore), parent=self.root)
        finally:
            self.genera_button.configure(state='normal')


if __name__ == '__main__':
    finestra = tk.Tk()
    FileGenApp(finestra)
    finestra.mainloop()
    