# UTILI è il mio file  TOTALMENTE OPZIONALE
'tst("parola") ► ◄===== PAROLA =====►'
'↑ si trova nel file utils.py ↑'
from utili import *

# Creo la funzione che analizza i dati dal file
def analizza_dati(df):
    # titolo stampato
    tst("analisi del file")
    # controllo le celle VUOTE (NaN)
    txt("celle vuote", u=0)
    # verifico se i valori sono null e faccio la somma
    mancanti = df.isnull().sum()
    
    # condizioni servono per verificare SE il file aperto ha i valori mancanti
    if mancanti.sum() == 0:
        tst("nessun valore mancante")
    else:
        # ciclo for per leggere le colonne e quantità
        for colonna, quantita in mancanti.items(): # mancanti è un dizionario
            if quantita > 0:
                print(f"Colonna {colonna}: {quantita} valori mancanti")

    for colonna in df.columns:
        righe = df[df[colonna].isnull()].index.tolist()

        if righe:
            print(f"Colonna: {colonna}")
            print(f"Righe con valori nulli: {righe}")
    
    # === Controllo valori DUPLICATI
    tst("verifico valori duplicati")
    # faccio la somma dei valori duplicati
    duplicati = df.duplicated().sum()
    
    # condizioni per verifiicare se i valori ci sono
    if duplicati == 0:
        tst("nessun valore deuplicato trovato")
    else:
        print(f"Trovate {duplicati} righe identiche da eliminare")

    # === Controllo TIPI DI DATI
    'verifichiamo i tipi di dati nel file, se sono lettere, numeri o altro'
    tst("verifico i tipi di dati")
    # ciclo for per vedere dentro ogni colonna il tipo di dato
    for colonna, tipo in df.dtypes.items(): 
        print(f"► {colonna}: {tipo}")
    
    # === Valori Minimi e Massimi
    tst("Stats base")
    for colonna in df.columns:
        if df[colonna].dtype == 'int64' or df[colonna].dtype == 'float64':
            minimo = df[colonna].min() # Valori
            massimo = df[colonna].max() # Valori
            print(f"{colonna}: Min = {minimo} - Max: {massimo}")
            if massimo > 100000:
                print("File troppo grande")
            if minimo < 0:
                print("Ci sono i valori negativi")
    s()


if __name__ == "__main__":
    import pandas as pd
    df = pd.read_csv('dati_sporchi.csv')
    analizza_dati(df)
