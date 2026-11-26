import pandas as pd
from config import MAX_RIGHE_CSV
import os

def leggi_csv(percorso):
    if not os.path.exists(percorso):
        return None
    
    df = pd.read_csv(percorso)
    return df

def prepara_contesto_per_ai(df, nome_file="file.csv"):
    righe = []
    righe.append(f"=== CONTESTO DATI: {nome_file} ===")
    righe.append(f'Righe totali: {df.shape[0]}')
    righe.append(f"Colonne totali: {df.shape[1]}")
    
    righe.append('=== COLONNE E TIPI ===')
    for col in df.columns:
        righe.append(f"{col}: {df[col].dtype}")
    
    righe.append('=== VALORI MANCANTI ===')
    mancanti = df.isnull().sum()
    for col, n in mancanti.items():
        if n > 0:
            righe.append(f"{col}: {n} mancanti ({n / len(df) * round(100, 1)}%)")
    if mancanti.sum() == 0:
        righe.append("Non ci sono valori mancanti")

    numeriche = df.select_dtypes(include=['number']).columns.tolist()
    if numeriche:
        righe.append("=== STATISTICHE NUMERICHE ===")
        desc = df[numeriche].describe().round(2)
        righe.append(desc.to_string())
    
    righe.append(f"=== PRIME {min(MAX_RIGHE_CSV, len(df))} RIGHE ===")
    righe.append(df.head(MAX_RIGHE_CSV).to_string())
    
    testuali = df.select_dtypes(include=['object', 'string']).columns.tolist()
    if testuali:
        righe.append("=== COLONNE TESTUALI (vaori frequenti) ===")
        for col in testuali:
            top = df[col].value_counts().head(5)
            righe.append(f"{col}")
            righe.append(top.to_string())
    return "\n".join(righe)

def chiedi_pulizia_a_ai(df):
    contesto = prepara_contesto_per_ai(df)
    prompt = f"""Sei un data analyst esperto. Ti passo la descrizione di un DataFrame padas. 
Analizza i problemi di qualità dei dati e suggerisci una strategia di pulizia.
{contesto}

Rispondi in italiano, in modo concreto:
1. Elenca i problemi che vedi (valori mancanti, tipi sbagliati, valori impossibili)
2. Per ogni problema, scrivi un codice python (pandas) per risolverlo.
3. Spiega brevemente ogni scelta.

Non inventare dati che non vedi. se qualcosa non è chiarp, dillo."""

    return prompt