import csv
import random

def apply_seed(s=None):
    if s is not None:
        random.seed(s)

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
    ('Matera', 'Basilicata')
]

categorie = ['Elettronica', 'Casa', 'Sport', 'Alimentari', 'Abbigliamento']

prodotti = {
    "Elettronica": ['Telefono', 'Laptop', 'Tablet', 'Cuffie', 'Microfono'],
    "Casa": ['Lampada', 'Divano', 'Tappeto','Piatti','Sedie'],
    "Sport": ['Panca','Manubri','Dischi','Zaino','Guanti'],
    "Alimentari": ['Pasta', 'Pane', 'Monster', 'Olio', 'Farina'],
    "Abbigliamento": ['Maglietta','Jeans','Giacca','Felpa','Scarpe']
}

prezzi = {
    'Elettronica': (50, 3500),
    'Casa': (15, 6580),
    'Sport': (10,2000),
    'Alimentari': (2,250),
    'Abbigliamento': (10,150)
}

MAX_RIGHE = 500
FILE = "vendite.csv"

righe = []

for i in range(MAX_RIGHE):
    mese = random.randint(1, 12)
    giorno = random.randint(1, 28)
    data = f"2024-{mese:02d}-{giorno:02d}"

    citta, regione = random.choice(citta_regioni)
    categoria = random.choice(categorie)
    prodotto = random.choice(prodotti[categoria])

    prezzo_min, prezzo_max = prezzi[categoria]
    prezzo_unit =round(random.uniform(prezzo_min, prezzo_max), 2) 
    quantita = random.randint(1, 10)

    totale = round(prezzo_unit * quantita, 2)
    
    if random.random() < 0.2:
        sconto = round(random.uniform(0.05, 0.30), 2)
    else:
        sconto = 0.0
    
    totale_scontato = round(totale * (1 - sconto), 2)
    cliente = random.choice(['Nuovo', 'Fedele', 'VIP'])
    eta = random.randint(18, 75)
    pagamento = random.choice(['Carta', 'Contanti', 'Bonifico', 'PayPal'])
    
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
        'metodo_di_pagamento': pagamento
    })


if not righe:
    raise ValueError("Nessuna riga generata.")

with open(FILE, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=righe[0].keys())
    writer.writeheader()
    writer.writerows(righe)
    