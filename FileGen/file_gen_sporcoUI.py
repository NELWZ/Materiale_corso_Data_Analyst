import csv
import random
import os
import time
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

# ═══════════════════════════════════════════════════════════
# CONFIGURAZIONE
# ═══════════════════════════════════════════════════════════
def mostra_configurazione():
    """Mostra una finestra di configurazione e restituisce i parametri."""
    bg, panel, field = '#1b2638', '#2b394d', '#152237'
    accent, text, muted = '#38bdf8', '#f3f4f6', '#b0bac8'
    root = tk.Tk()
    root.title('FileGen | Generatore CSV sporchi')
    root.configure(bg=bg)
    root.resizable(False, False)
    root.geometry('900x680')
    root.option_add('*Font', ('Segoe UI', 11))
    result, entries = {}, {}

    header = tk.Frame(root, bg=bg)
    header.pack(fill='x', padx=30, pady=(26, 18))
    tk.Label(header, text='FILEGEN', bg=bg, fg=accent,
             font=('Segoe UI', 11, 'bold')).pack(anchor='w')
    tk.Label(header, text='Generatore di dataset CSV', bg=bg, fg=text,
             font=('Segoe UI', 24, 'bold')).pack(anchor='w', pady=(5, 4))
    tk.Label(header, text='Configura i dati e genera i file in pochi secondi.',
             bg=bg, fg=muted).pack(anchor='w')

    card = tk.Frame(root, bg=panel, padx=22, pady=18)
    card.pack(fill='x', padx=30, pady=(0, 18))
    fields = [
        ('seed', 'Seed casuale', '42'),
        ('rows', 'Righe per file', '50'),
        ('count', 'Numero di file', '5'),
        ('prefix', 'Prefisso dei file', 'file_sporco'),
    ]
    for row, (key, label, default) in enumerate(fields):
        tk.Label(card, text=label, bg=panel, fg=text, anchor='w').grid(
            row=row, column=0, sticky='w', padx=(0, 18), pady=5)
        entry = tk.Entry(card, bg=field, fg=text, insertbackground=text,
                         relief='flat', highlightthickness=1,
                         highlightbackground='#374151', highlightcolor=accent,
                         width=32, font=('Segoe UI', 11))
        entry.insert(0, default)
        entry.grid(row=row, column=1, sticky='ew', ipady=9, pady=5)
        entries[key] = entry
        if key == 'seed':
            seed_disabled = tk.BooleanVar(value=False)

            def aggiorna_seed():
                entries['seed'].configure(
                    state='disabled' if seed_disabled.get() else 'normal')

            tk.Checkbutton(
                card, text='Disattivato (None)', variable=seed_disabled,
                command=aggiorna_seed, bg=panel, fg=text,
                activebackground=panel, activeforeground=text,
                selectcolor=field, highlightthickness=0
            ).grid(row=row, column=2, sticky='w', padx=(10, 0))

    percent_vars = {}
    percent_fields = [
        ('dirty', 'Righe con errori gravi (0–100%)', 25),
        ('empty', 'Probabilità celle vuote (0–100%)', 4),
        ('duplicates', 'Percentuale duplicati (0–100%)', 3),
    ]
    for row, (key, label, default) in enumerate(percent_fields, start=len(fields)):
        tk.Label(card, text=label, bg=panel, fg=text, anchor='w').grid(
            row=row, column=0, sticky='w', padx=(0, 18), pady=5)
        value = tk.IntVar(value=default)
        tk.Scale(card, from_=0, to=100, orient='horizontal', resolution=1,
                 variable=value, bg=panel, fg=text, troughcolor=field,
                 activebackground=accent, highlightthickness=0,
                 showvalue=True, length=260, font=('Segoe UI', 10)).grid(
                     row=row, column=1, sticky='ew', pady=4)
        percent_vars[key] = value
    card.columnconfigure(1, weight=1)

    folder_var = tk.StringVar(value=os.getcwd())
    row_index = len(fields) + len(percent_fields)
    tk.Label(card, text='Cartella di destinazione', bg=panel, fg=text,
             anchor='w').grid(row=row_index, column=0, sticky='w',
                              padx=(0, 18), pady=5)
    folder_row = tk.Frame(card, bg=panel)
    folder_row.grid(row=row_index, column=1, sticky='ew', pady=5)
    tk.Entry(folder_row, textvariable=folder_var, bg=field, fg=text,
             insertbackground=text, relief='flat', highlightthickness=1,
             highlightbackground='#374151', highlightcolor=accent,
             font=('Segoe UI', 11)
             ).pack(side='left', fill='x', expand=True, ipady=9)

    def scegli_cartella():
        selected = filedialog.askdirectory(initialdir=folder_var.get(), parent=root)
        if selected:
            folder_var.set(selected)

    tk.Button(folder_row, text='Sfoglia', command=scegli_cartella,
                bg='#374151', fg=text, activebackground='#4b5563',
                activeforeground=text, relief='flat', padx=12, cursor='hand2'
                ).pack(side='left', padx=(8, 0), ipady=4)

    def genera():
        try:
                seed_value = entries['seed'].get().strip()
                seed = (None if seed_disabled.get() or not seed_value
                    else int(seed_value))
                rows = int(entries['rows'].get())
                count = int(entries['count'].get())
                dirty = percent_vars['dirty'].get() / 100
                empty = percent_vars['empty'].get() / 100
                duplicates = percent_vars['duplicates'].get() / 100
                prefix = entries['prefix'].get().strip()
                folder = folder_var.get().strip()
                if not 1 <= rows <= 100_000_000:
                    raise ValueError('Le righe devono essere comprese tra 1 e 100 milioni.')
                if not 1 <= count <= 10_000:
                    raise ValueError('Il numero di file deve essere compreso tra 1 e 10.000.')
                if any(not 0 <= value <= 1 for value in (dirty, empty, duplicates)):
                    raise ValueError('Le percentuali devono essere comprese tra 0 e 1.')
                if not prefix or not os.path.isdir(folder):
                    raise ValueError('Inserisci un prefisso e seleziona una cartella valida.')
                if rows * count > 1_000_000 or count > 100:
                    if not messagebox.askyesno(
                        'Generazione impegnativa',
                        f'La richiesta creerà {rows * count:,} righe complessive '
                        f'in {count:,} file. Potrebbero servire molto tempo e spazio '
                        'su disco. Vuoi continuare?', parent=root
                    ):
                        return
                result.update(seed=seed, rows=rows, count=count, dirty=dirty,
                            empty=empty, duplicates=duplicates, prefix=prefix,
                            folder=folder)
                root.destroy()
        except ValueError as exc:
            messagebox.showerror('Parametri non validi', str(exc), parent=root)

    footer = tk.Frame(root, bg=bg)
    footer.pack(fill='x', padx=30, pady=(0, 24))
    tk.Label(footer, text='Lascia vuoto il seed per ottenere dati diversi ogni volta.',
             bg=bg, fg=muted, font=('Segoe UI', 10)).pack(side='left')
    tk.Button(footer, text='GENERA CSV', command=genera, bg=accent,
              fg='#082f49', activebackground='#7dd3fc', activeforeground='#082f49',
              relief='flat', font=('Segoe UI', 11, 'bold'), padx=22,
              pady=12, cursor='hand2').pack(side='right')
    root.bind('<Return>', lambda _event: genera())
    root.mainloop()
    return result


config = mostra_configurazione()
if not config:
    raise SystemExit

SEED = config['seed']
MAX_RIGHE = config['rows']
QUANTO_SPORCO = config['dirty']
PCT_CELLE_VUOTE = config['empty']
PCT_DUPLICATI = config['duplicates']
NUMERO_FILES = config['count']
FILE_OUT = [os.path.join(config['folder'], f"{config['prefix']}_{i+1}.csv")
            for i in range(NUMERO_FILES)]

if SEED is not None:
    random.seed(SEED)

# ═══════════════════════════════════════════════════════════
# ANAGRAFICHE
# ═══════════════════════════════════════════════════════════
citta_regioni = [
    ('Milano', 'Lombardia'),
    ('Roma', 'Lazio'),
    ('Napoli', 'Campania'),
    ('Torino', 'Piemonte'),
    ('Palermo', 'Sicilia'),
    ('Genova', 'Liguria'),
    ('Bologna', 'Emilia-Romagna'),
    ('Firenze', 'Toscana'),
    ('Bari', 'Puglia'),
    ('Venezia', 'Veneto'),
    ('Matera', 'Basilicata'),
]

categorie = ['Elettronica', 'Casa', 'Sport', 'Alimentari', 'Abbigliamento']

prodotti = {
    "Elettronica":   ['Telefono', 'Laptop', 'Tablet', 'Cuffie', 'Microfono'],
    "Casa":          ['Lampada', 'Divano', 'Tappeto', 'Piatti', 'Sedie'],
    "Sport":         ['Panca', 'Manubri', 'Dischi', 'Zaino', 'Guanti'],
    "Alimentari":    ['Pasta', 'Pane', 'Monster', 'Olio', 'Farina'],
    "Abbigliamento": ['Maglietta', 'Jeans', 'Giacca', 'Felpa', 'Scarpe'],
}

prezzi = {
    'Elettronica':   (50, 3500),
    'Casa':          (15, 6580),
    'Sport':         (10, 2000),
    'Alimentari':    (2, 250),
    'Abbigliamento': (10, 150),
}

# Sconti "veri" plausibili per categoria (per rendere i dati meno piatti)
sconto_tipico = {
    'Elettronica':   (0.03, 0.15),
    'Casa':          (0.05, 0.25),
    'Sport':         (0.05, 0.20),
    'Alimentari':    (0.02, 0.10),
    'Abbigliamento': (0.10, 0.35),
}

metodi_pagamento = ['Carta', 'Contanti', 'Bonifico', 'PayPal']
tipi_cliente = ['Nuovo', 'Fedele', 'VIP']

# ═══════════════════════════════════════════════════════════
# INIEZIONE DIFETTI
# ═══════════════════════════════════════════════════════════
# --- 2) Difetti "gravi" su una % di righe ------------------
def inietta_difetto(riga):
    """Sceglie un tipo di errore e lo applica. Ritorna il nome dell'errore."""
    errore = random.choice([
        'spazi_categoria', 'maiuscole_categoria', 'categoria_errata',
        'citta_regione_incoerente', 'citta_con_spazi', 'regione_errata',
        'data_slash', 'data_invertita', 'data_futura', 'data_testo',
        'prezzo_negativo', 'prezzo_zero', 'prezzo_testo', 'prezzo_enorme',
        'quantita_negativa', 'quantita_zero', 'quantita_testo',
        'eta_minorenne', 'eta_troppo_alta', 'eta_testo',
        'sconto_negativo', 'sconto_oltre_100', 'sconto_percentuale',
        'totale_incoerente', 'totale_negativo',
        'prodotto_fuori_categoria', 'metodo_typo',
    ])

    if errore == 'spazi_categoria' and riga['categoria']:
        riga['categoria'] = f" {riga['categoria'].lower()} "
    elif errore == 'maiuscole_categoria' and riga['categoria']:
        riga['categoria'] = riga['categoria'].upper()
    elif errore == 'categoria_errata':
        riga['categoria'] = random.choice(['Eletronica', 'Sportivo', 'N/D', ''])
    elif errore == 'citta_regione_incoerente':
        # città giusta, regione sbagliata
        riga['regione'] = random.choice(
            [r for _, r in citta_regioni if r != riga['regione']]
        )
    elif errore == 'citta_con_spazi' and riga['città']:
        riga['città'] = f"  {riga['città']} "
    elif errore == 'regione_errata':
        riga['regione'] = random.choice(['Regione sconosciuta', 'N/D', ''])
    elif errore == 'data_slash':
        riga['data'] = riga['data'].replace('-', '/')
    elif errore == 'data_invertita' and riga['data']:
        a, m, g = riga['data'].split('-')
        riga['data'] = f"{g}/{m}/{a}"
    elif errore == 'data_futura':
        riga['data'] = f"2025-{random.randint(1,12):02d}-{random.randint(1,28):02d}"
    elif errore == 'data_testo':
        riga['data'] = random.choice(['ieri', 'domani', 'N/D', ''])
    elif errore == 'prezzo_negativo':
        riga['prezzo_unitario'] = -round(random.uniform(5, 500), 2)
    elif errore == 'prezzo_zero':
        riga['prezzo_unitario'] = 0
    elif errore == 'prezzo_testo':
        riga['prezzo_unitario'] = random.choice(['non disponibile', 'N/D', 'gratis', ''])
    elif errore == 'prezzo_enorme':
        riga['prezzo_unitario'] = round(random.uniform(50000, 999999), 2)
    elif errore == 'quantita_negativa':
        riga['quantità'] = -random.randint(1, 10)
    elif errore == 'quantita_zero':
        riga['quantità'] = 0
    elif errore == 'quantita_testo':
        riga['quantità'] = random.choice(['molte', 'una', 'N/D', ''])
    elif errore == 'eta_minorenne':
        riga['età_cliente'] = random.randint(5, 17)
    elif errore == 'eta_troppo_alta':
        riga['età_cliente'] = random.randint(100, 150)
    elif errore == 'eta_testo':
        riga['età_cliente'] = random.choice(['sconosciuta', 'N/D', ''])
    elif errore == 'sconto_negativo':
        riga['sconto'] = -round(random.uniform(0.05, 0.5), 2)
    elif errore == 'sconto_oltre_100':
        riga['sconto'] = round(random.uniform(1.1, 2.0), 2)
    elif errore == 'sconto_percentuale':
        riga['sconto'] = f"{random.randint(5, 40)}%"
    elif errore == 'totale_incoerente':
        riga['totale'] = round(random.uniform(10000, 50000), 2)
    elif errore == 'totale_negativo':
        riga['totale'] = -round(random.uniform(100, 5000), 2)
    elif errore == 'prodotto_fuori_categoria':
        # prodotto di un'altra categoria
        altra = random.choice([c for c in categorie if c != riga['categoria']])
        riga['prodotto'] = random.choice(prodotti[altra])
    elif errore == 'metodo_typo':
        riga['metodo_di_pagamento'] = random.choice(
            ['carta', 'CARTA', 'paypal ', 'Bonifico Bancario', 'Contanti?']
        )
    return errore

def genera_riga():
    mese, giorno = random.randint(1, 12), random.randint(1, 28)
    data = f'2024-{mese:02d}-{giorno:02d}'
    citta, regione = random.choice(citta_regioni)
    categoria = random.choice(categorie)
    prodotto = random.choice(prodotti[categoria])
    pmin, pmax = prezzi[categoria]
    prezzo_unit = round(random.uniform(pmin, pmax), 2)
    quantita = random.randint(1, 10)
    totale = round(prezzo_unit * quantita, 2)
    if random.random() < 0.22:
        smin, smax = sconto_tipico[categoria]
        sconto = round(random.uniform(smin, smax), 2)
    else:
        sconto = 0.0
    cliente = random.choices(tipi_cliente, weights=[0.5, 0.35, 0.15], k=1)[0]
    return {
        'data': data, 'città': citta, 'regione': regione,
        'categoria': categoria, 'prodotto': prodotto,
        'prezzo_unitario': prezzo_unit, 'quantità': quantita,
        'totale': totale, 'sconto': sconto,
        'totale_scontato': round(totale * (1 - sconto), 2),
        'tipo_di_cliente': cliente, 'età_cliente': random.randint(18, 75),
        'metodo_di_pagamento': random.choices(
            metodi_pagamento, weights=[0.5, 0.15, 0.20, 0.15], k=1)[0],
    }


def applica_difetti(riga):
    if random.random() < QUANTO_SPORCO:
        inietta_difetto(riga)
    for campo in riga:
        if random.random() < PCT_CELLE_VUOTE:
            riga[campo] = ''
    for campo in ('prezzo_unitario', 'totale', 'totale_scontato'):
        valore = riga[campo]
        if isinstance(valore, (int, float)) and random.random() < 0.02:
            riga[campo] = str(valore).replace('.', ',')
    return riga


def avvia_generazione():
    n_dup = round(MAX_RIGHE * PCT_DUPLICATI)
    unita_totali = NUMERO_FILES * (MAX_RIGHE + n_dup)
    finestra = tk.Tk()
    finestra.title('FileGen | Generazione in corso')
    finestra.geometry('620x230')
    finestra.resizable(False, False)
    finestra.protocol('WM_DELETE_WINDOW', lambda: annulla())
    tk.Label(finestra, text='Generazione dei CSV',
             font=('Segoe UI', 16, 'bold')).pack(anchor='w', padx=24, pady=(20, 8))
    stato = tk.Label(finestra, text='Preparazione...', font=('Segoe UI', 10))
    stato.pack(anchor='w', padx=24)
    barra = ttk.Progressbar(finestra, maximum=unita_totali, mode='determinate')
    barra.pack(fill='x', padx=24, pady=12)
    dettagli = tk.Label(finestra, text='', font=('Segoe UI', 10))
    dettagli.pack(anchor='w', padx=24)
    stato_lavoro = {'annullato': False, 'file': None, 'scritti': 0,
                    'inizio': time.monotonic()}

    def annulla():
        stato_lavoro['annullato'] = True
        stato.configure(text='Annullamento in corso...')

    tk.Button(finestra, text='Annulla', command=annulla).pack(anchor='e', padx=24, pady=12)

    def aggiorna():
        totale = stato_lavoro['scritti']
        trascorso = max(time.monotonic() - stato_lavoro['inizio'], 0.001)
        velocita = totale / trascorso
        eta = (unita_totali - totale) / velocita if velocita else 0
        percento = totale * 100 / unita_totali
        barra['value'] = totale
        dettagli.configure(
            text=f'{totale:,} / {unita_totali:,} righe ({percento:.1f}%)  |  '
                 f'{velocita:,.0f} righe/s  |  tempo residuo ~{eta / 60:.1f} min')

    def passo(file_index=0, indice_riga=0, fase='dati', writer=None,
              campione=None, handle=None):
        if stato_lavoro['annullato']:
            if handle:
                handle.close()
            finestra.destroy()
            messagebox.showwarning('Generazione annullata',
                                   'La generazione è stata interrotta. I file già creati possono essere incompleti.')
            return
        try:
            budget = 2000
            while budget and file_index < NUMERO_FILES:
                if handle is None:
                    if SEED is not None:
                        random.seed(SEED)
                    handle = open(FILE_OUT[file_index], 'w', encoding='utf-8', newline='')
                    writer = csv.DictWriter(handle, fieldnames=list(genera_riga().keys()))
                    writer.writeheader()
                    campione = []
                    indice_riga, fase = 0, 'dati'
                if fase == 'dati' and indice_riga < MAX_RIGHE:
                    riga = applica_difetti(genera_riga())
                    writer.writerow(riga)
                    if len(campione) < 10_000:
                        campione.append(riga.copy())
                    indice_riga += 1
                elif fase == 'dati':
                    fase = 'duplicati'
                elif indice_riga < n_dup:
                    writer.writerow(random.choice(campione).copy())
                    indice_riga += 1
                else:
                    handle.close()
                    handle = None
                    file_index += 1
                    indice_riga, fase = 0, 'dati'
                    continue
                stato_lavoro['scritti'] += 1
                budget -= 1
            if file_index >= NUMERO_FILES:
                aggiorna()
                finestra.destroy()
                messagebox.showinfo(
                    'Generazione completata',
                    f'Creati {NUMERO_FILES:,} file.\n'
                    f'Righe per file: {MAX_RIGHE + n_dup:,} '
                    f'(incluse {n_dup:,} copie duplicate).\n'
                    f'Righe totali scritte: {unita_totali:,}.',
                )
                print(f'Creati {NUMERO_FILES:,} file: {FILE_OUT[0]} ... {FILE_OUT[-1]}')
                return
            stato.configure(text=f'File {file_index + 1:,} di {NUMERO_FILES:,}: {os.path.basename(FILE_OUT[file_index])}')
            aggiorna()
            finestra.after(1, lambda: passo(file_index, indice_riga, fase, writer, campione, handle))
        except (OSError, csv.Error, ValueError) as exc:
            if handle:
                handle.close()
            finestra.destroy()
            messagebox.showerror('Errore durante la generazione',
                                 f'{exc}\n\nGenerazione interrotta; i file incompleti non sono stati rimossi.')

    finestra.after(50, passo)
    finestra.mainloop()


avvia_generazione()
