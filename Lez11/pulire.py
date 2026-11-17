import pandas as pd
from utili import *

df = pd.read_csv('./Lez11/vendite.csv')

# === QUANTI VALORI UNICI CI SONO ===
tst("valori unici")
unici = df['citta'].unique()
print(unici)


tst("contatore di valori unici")
ripetiz = df['citta'].value_counts()
print(ripetiz)

tst("convertire una colonna in numero")
txt("prima", 0)
print(df['prezzo'])
df['prezzo'] = pd.to_numeric(df['prezzo'], errors='coerce')

"errors='coerce' ► se non riesci a convertire metti NaN"
"errors='raise' ► se non riesci a convertire evoca l'errore"

txt("dopo", 0)
print(df['prezzo'])

tst("valori")
print(df['prezzo'].dtype)

tst("riempiamo i valori mancanti")
txt('opzione 1 ► riempiamo | PRIMA', 0)
print(df['quantita'])
df['quantita'] = df['quantita'].fillna(value=1)


txt('opzione 1 ► riempiamo | DOPO', 0)
print(df['quantita'])

s(n=1)

df['citta'] = df['citta'].fillna("Sconosciuta")
print(df['citta'])


txt('opzione 2 ► ELIMINAZIONE ', 0)
s()

# txt("prima", 0)
# print(df)

#df = df.dropna()

# txt('dopo', 0)
# print(df)

tst("controllo finale")

somma_nulli = df.isnull().sum()
print(somma_nulli)

tst("info utili")
info = df.describe()
print(info)

tst("filtrare le righe")

milano = df[df['citta'] == 'Milano']
print(milano)


tst("raggruppare")
'groupby'

gr1 = df.groupby('citta')['prezzo'].sum()
print(gr1)


gr2 = df.groupby('prodotto')['prezzo'].sum().sort_values(ascending=False)
print(gr2)

tst('ordinare')

ordine = df.sort_values('quantita').head(3)
print(ordine)