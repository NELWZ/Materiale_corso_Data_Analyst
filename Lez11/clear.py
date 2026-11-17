import pandas as pd
from utili import *

# carica il file
df = pd.read_csv('vendite_sporco.csv')
print(df)
tst(f"Iniziale: {df.shape[0]} righe x {df.shape[1]} colonne")

# === DUPLICATI === #
n_dup = df.duplicated().sum()
tst(f"duplicati: {n_dup}")

# elimina i duplicati
df = df.drop_duplicates().reset_index(drop=True)

tst(f"Rimossi {n_dup} duplicati =► {len(df)} righe")

# Sistemiamo i valori numerici
numeriche = ['prezzo_unitario', 'quantità', 'sconto', 'totale', 'totale_scontato', 'età_cliente']

for col in numeriche:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Valori NaN
df.loc[(df['prezzo_unitario'] <= 0 | (df['prezzo_unitario'] > 10000), 'prezzo_unitario' )] = pd.NA
df.loc[(df['quantità'] < 1) | (df['quantità'] > 10), "quantità"] = pd.NA
df.loc[(df['sconto'] < 0) | (df['sconto'] > 1), "sconto"] = pd.NA
df.loc[(df['età_cliente'] < 18) | (df['età_cliente'] > 75), "età_cliente"] = pd.NA

# Catergoria
df['categoria'] = df['categoria'].astype('string').str.strip().str.lower()


# Date
df['data'] = pd.to_datetime(df['data'], errors='coerce', format="%Y-%m-%d")

df['mese'] = df['data'].dt.month
df['giorno_settimana'] = df['data'].dt.day_name()

# totali
df['totale'] =( df['prezzo_unitario'] * df['quantità']).round(2)
df['totale_scontato'] = (df['totale'] * (1- df['sconto'])).round(2)

# GESTIONE NaN
df = df.dropna(subset=['data', 'prezzo_unitario', 'quantità', 'totale', 'totale_scontato'])

df['sconto'] = df['sconto'].fillna(0)
df['categoria'] = df['categoria'].fillna('Sconosciuta')
df['regione'] = df['regione'].fillna('Sconosciuta')
df['città'] = df['città'].fillna('Sconosciuta')
df['tipo_di_cliente'] = df['tipo_di_cliente'].fillna("Sconosciuto")
df['metodo_di_pagamento'] = df['metodo_di_pagamento'].fillna('Sconosciuto')
df['età_cliente'] = df['età_cliente'].fillna(df['età_cliente'].median())
df = df.reset_index(drop=True)

tst(f"Finale: {df.shape[0]} righe x {df.shape[1]} colonne")
tst(f"NaN residui: {df.isnull().sum()}")


# PULRE IL PRODOTTO