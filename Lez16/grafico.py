import matplotlib.pyplot as plt
from utili import *

def crea_grafici(df):
    tst("report visivo (grafico)")

    if 'spesa' not in df.columns or 'nome' not in df.columns:
        print("Dati mancanti")
        return
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    
    spese_per_nome = df.groupby("nome")['spesa'].sum()
    
    ax1.bar(spese_per_nome.index, spese_per_nome.values)
    ax1.set_title("Spesa Totale per Cliente")
    
    ax1.grid()
    
    plt.show()