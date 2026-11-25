import csv
import random
import os
import tkinter as tk
from tkinter import filedialog, messagebox

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
    root.option_add('*Font', ('Segoe UI', 10))
    result, entries = {}, {}

    header = tk.Frame(root, bg=bg)
    header.pack(fill='x', padx=24, pady=(22, 14))
    tk.Label(header, text='FILEGEN', bg=bg, fg=accent,
             font=('Segoe UI', 10, 'bold')).pack(anchor='w')
    tk.Label(header, text='Generatore di dataset CSV', bg=bg, fg=text,
             font=('Segoe UI', 20, 'bold')).pack(anchor='w', pady=(3, 2))
    tk.Label(header, text='Configura i dati e genera i file in pochi secondi.',
             bg=bg, fg=muted).pack(anchor='w')

    card = tk.Frame(root, bg=panel, padx=18, pady=14)
    card.pack(fill='x', padx=24, pady=(0, 14))
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
                         width=28)
        entry.insert(0, default)
        entry.grid(row=row, column=1, sticky='ew', ipady=7, pady=4)
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
                 showvalue=True, length=220).grid(
                     row=row, column=1, sticky='ew', pady=2)
        percent_vars[key] = value
    card.columnconfigure(1, weight=1)

    folder_var = tk.StringVar(value=os.getcwd())
    row_index = len(fields) + len(percent_fields)
    tk.Label(card, text='Cartella di destinazione', bg=panel, fg=text,
             anchor='w').grid(row=row_index, column=0, sticky='w',
                              padx=(0, 18), pady=5)
    folder_row = tk.Frame(card, bg=panel)
    folder_row.grid(row=row_index, column=1, sticky='ew', pady=4)
    tk.Entry(folder_row, textvariable=folder_var, bg=field, fg=text,
             insertbackground=text, relief='flat', highlightthickness=1,
             highlightbackground='#374151', highlightcolor=accent
             ).pack(side='left', fill='x', expand=True, ipady=7)

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
                if rows < 1 or count < 1:
                    raise ValueError('Righe e numero di file devono essere maggiori di zero.')
                if any(not 0 <= value <= 1 for value in (dirty, empty, duplicates)):
                    raise ValueError('Le percentuali devono essere comprese tra 0 e 1.')
                if not prefix or not os.path.isdir(folder):
                    raise ValueError('Inserisci un prefisso e seleziona una cartella valida.')
                result.update(seed=seed, rows=rows, count=count, dirty=dirty,
                            empty=empty, duplicates=duplicates, prefix=prefix,
                            folder=folder)
                root.destroy()
        except ValueError as exc:
            messagebox.showerror('Parametri non validi', str(exc), parent=root)

    footer = tk.Frame(root, bg=bg)
    footer.pack(fill='x', padx=24, pady=(0, 20))
    tk.Label(footer, text='Lascia vuoto il seed per ottenere dati diversi ogni volta.',
             bg=bg, fg=muted, font=('Segoe UI', 9)).pack(side='left')
    tk.Button(footer, text='GENERA CSV', command=genera, bg=accent,
              fg='#082f49', activebackground='#7dd3fc', activeforeground='#082f49',
              relief='flat', font=('Segoe UI', 10, 'bold'), padx=18,
              pady=10, cursor='hand2').pack(side='right')
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
# GENERAZIONE RIGHE "PULITE" (base)
# ═══════════════════════════════════════════════════════════
righe = []

for _ in range(MAX_RIGHE):
    mese = random.randint(1, 12)
    giorno = random.randint(1, 28)
    data = f"2024-{mese:02d}-{giorno:02d}"

    citta, regione = random.choice(citta_regioni)
    categoria = random.choice(categorie)
    prodotto = random.choice(prodotti[categoria])

    pmin, pmax = prezzi[categoria]
    prezzo_unit = round(random.uniform(pmin, pmax), 2)
    quantita = random.randint(1, 10)
    totale = round(prezzo_unit * quantita, 2)

    # Sconto applicato al ~22% delle righe, con range per categoria
    if random.random() < 0.22:
        smin, smax = sconto_tipico[categoria]
        sconto = round(random.uniform(smin, smax), 2)
    else:
        sconto = 0.0
    totale_scontato = round(totale * (1 - sconto), 2)

    cliente = random.choices(
        tipi_cliente, weights=[0.5, 0.35, 0.15], k=1
    )[0]  # più nuovi che VIP, realistico
    eta = random.randint(18, 75)
    pagamento = random.choices(
        metodi_pagamento, weights=[0.5, 0.15, 0.20, 0.15], k=1
    )[0]

    righe.append({
        'data': data,
        'città': citta,
        'regione': regione,
        'categoria': categoria,
        'prodotto': prodotto,
        'prezzo_unitario': prezzo_unit,
        'quantità': quantita,
        'totale': totale,
        'sconto': sconto,
        'totale_scontato': totale_scontato,
        'tipo_di_cliente': cliente,
        'età_cliente': eta,
        'metodo_di_pagamento': pagamento,
    })

# ═══════════════════════════════════════════════════════════
# INIEZIONE DIFETTI
# ═══════════════════════════════════════════════════════════

# --- 1) Celle vuote (le più comuni nei CSV reali) ----------
for riga in righe:
    for campo in riga:
        if random.random() < PCT_CELLE_VUOTE:
            riga[campo] = ''

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
        riga['data'] = riga['data'].replace('-', '/')       # 2024/03/07
    elif errore == 'data_invertita':
        a, m, g = riga['data'].split('-')
        riga['data'] = f"{g}/{m}/{a}"                        # 07/03/2024
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

n_difettosi = 0
for riga in righe:
    if random.random() < QUANTO_SPORCO:
        inietta_difetto(riga)
        n_difettosi += 1

# --- 3) Alcune celle numeriche diventano float con virgola ---
# (simula CSV esportati da Excel in locale IT)
for riga in righe:
    for campo in ('prezzo_unitario', 'totale', 'totale_scontato'):
        val = riga[campo]
        if isinstance(val, (int, float)) and random.random() < 0.02:
            riga[campo] = str(val).replace('.', ',')   # "12,50"

# --- 4) Duplicati in coda ---------------------------------
n_dup = round(len(righe) * PCT_DUPLICATI)
for _ in range(n_dup):
    righe.append(random.choice(righe).copy())

# ═══════════════════════════════════════════════════════════
# SCRITTURA
# ═══════════════════════════════════════════════════════════
if not righe:
    raise ValueError("Nessuna riga generata.")

for i in range(NUMERO_FILES):
    with open(FILE_OUT[i], 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=righe[0].keys())
        writer.writeheader()
        writer.writerows(righe)

print(f"    Creato {FILE_OUT}")
print(f"   Righe totali:     {len(righe)}")
print(f"   Righe 'pulite':   {len(righe) - n_difettosi - n_dup}")
print(f"   Righe difettose:  {n_difettosi}")
print(f"   Duplicati:        {n_dup}")