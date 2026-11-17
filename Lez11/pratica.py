import pandas as pd
from utili import *

# === PARTE 1 === #
#FILE = 'C:/Users/avare/Desktop/pratica_vendite.csv'

FILE = './Lez11/pratica_vendite.csv'

# carico il file 
df = pd.read_csv(FILE)

# p(df)
# p(df.head())
# p(df.tail(3))
# p(df.shape) 
# p(df.dtypes)
# p(df.isnull())
# p(df.isnull().sum())

# === PARTE 2 === #

df['prezzo'] = pd.to_numeric(df['prezzo'], errors="coerce")
p(f"NaN in prezzo: {df['prezzo'].isnull().sum()}")


df['quantita'] = pd.to_numeric(df['quantita'], errors="coerce")
p(f"NaN in quantita: {df['quantita'].isnull().sum()}")
s()
p(df)
df = df.dropna(subset=["prezzo"])
p(df)

s()
p(df['quantita'])
df['quantita'] = df['quantita'].fillna(1)
df['citta'] = df['citta'].fillna('Sconosciuta')
s()
p(df['quantita'])

df['totale'] = df['quantita'] * df['prezzo']

p(df['totale'])


# gruppo
gr1 = df.groupby('prodotto')['totale'].sum()
p(gr1)

gr2 = df.groupby('prodotto')['totale'].sum().sort_values(ascending=False)
p(gr2)



df['data'] = pd.to_datetime(df['data'])

p(df.groupby('data')['totale'].sum())


df.to_csv('new.csv')