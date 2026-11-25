import pandas as pd
from utili import *
import matplotlib.pyplot as plt

df = pd.read_csv('vendite.csv')
tst("Esercizio 4")

print(f"righe: {df.shape[0]} | Colonne: {df.shape[1]}")

s()
colonne_numeriche = ['prezzo_unitario','quantità', 'totale', 'sconto', 'totale_scontato', 'età_cliente']

problemi_tipi = [ col for col in colonne_numeriche if df[col].dtype == "object"]

if problemi_tipi:
    print(f"Colonne non numeriche: {problemi_tipi}")

print("Tipi di dato: tutte le colonne sono numeriche")

fatturato_per_prodotto = (df.groupby("prodotto")['totale_scontato'].sum().round(2).sort_values(ascending=False))

tst("fatturato netto per prodotto")
s()
c = 0
for p, f in fatturato_per_prodotto.items(): print(f"{p}: €{f}")

somma_per_prodotto = fatturato_per_prodotto.sum()
somma_totale = round(df['totale_scontato'].sum(), 2)

tst("somma grezza per prodotto")
print(somma_per_prodotto)

tst('somma totale')
print(f'€{somma_totale}')

if abs(somma_per_prodotto - somma_totale) > 0.01: print("Le due somme non coincidono")
else: print("Somme coincidono")

tst('quantità venduta per prodotto')
quantita_per_prodotto = (df.groupby('prodotto')['quantità'].sum().sort_values(ascending=False))

qpp = quantita_per_prodotto


for p, q in qpp.items():
    print(f"{p}: {q}")
    
s(n=0)
somma_qpp = qpp.sum()
print(f"Somma prodotti: {somma_qpp}")

if somma_qpp <= 0:
    print('non ci sono prodotti')

# top 5 per fatturato

tst("top 5 per fatturato")
top5_fatturato = fatturato_per_prodotto.head(5)

for pos, (prod, val) in enumerate(top5_fatturato.items(), start=1):
    print(f"{pos} - {prod: <12} €{val: >5,.2f}")

s()
top5_quantita = quantita_per_prodotto.head(5)

for pos, (prod, val) in enumerate(top5_quantita.items(), start=1):
    print(f"{pos} - {prod: <12} {val: >6} pezzi")


set_fatturato = set(top5_fatturato.index)
set_quantita = set(top5_quantita.index)

tst('confronto tra i due ranking')
print("Solo nel top fatturato: ", sorted(set_fatturato - set_quantita))
print('Solo nel top quantità: ', sorted(set_quantita - set_fatturato))
print("Entrambi: ", sorted(set_fatturato and set_quantita))

print(set_fatturato)
print(set_quantita)


confronto = pd.DataFrame({
    'fatturato_netto': top5_fatturato,
    'fatturato_venduta': top5_quantita
})

tst('confronto top 5')
print(confronto)

s()
prod_top_fatt = top5_fatturato.index[0]
righe_prodotto = df[df['prodotto'] == prod_top_fatt]
pezzi_venduti = righe_prodotto['quantità'].sum()
prezzo_medio = righe_prodotto['prezzo_unitario'].mean()

tst('info')
print(f"Fatturato netto: €{round(top5_fatturato.iloc[0], 2)}")
print(f"Pezzi venduti: {pezzi_venduti}")
print(f"prezzo medio: €{round(prezzo_medio, 2)}")
# TODO
print(f"Numero di vendite: {len(righe_prodotto)}")


def grafico_top5():
    top5_fatturato = fatturato_per_prodotto.head(5)
    top5_quantita = quantita_per_prodotto.head(5)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    # [::-1] ► reverse
    ax1.barh(top5_fatturato.index[::-1], top5_fatturato.values[::-1])
    ax1.set_title("Top 5 per fatturato netto")
    ax1.grid()
    # fatturato
    for i, v in enumerate(top5_fatturato.values[::-1]):
        ax1.text(v, i, f"€{round(v, 0)}", va="center")
    
    #quantità
    ax2.barh(top5_quantita[::-1], top5_quantita[::-1])
    ax2.grid()
    for i, v in enumerate(top5_quantita.values[::-1]):
        ax2.text(v, i, f"{v}", va="center")
    fig.savefig("grafico.png")
    
grafico_top5()