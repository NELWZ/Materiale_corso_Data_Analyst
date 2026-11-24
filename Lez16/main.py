import os
import pandas as pd
from utili import *
from analizzatore import analizza_dati
from pulitore import pulsici_dati
from grafico import crea_grafici

def carica_csv(nome_file):
    return pd.read_csv(nome_file)


def main():
    nome_file = input("nome file: ").strip()
    
    if not os.path.exists(nome_file):
        print("File non esiste")
        return

    df = carica_csv(nome_file)
    
    analizza_dati(df)
    
    df_pulito = pulsici_dati(df)
    
    crea_grafici(df_pulito)
    # salvate il file qui con pd.read...
    nome_file_pulito = "pulito_" + nome_file
    
main()