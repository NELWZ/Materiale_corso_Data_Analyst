import pandas as pd
from utili import *

# carico il file csv per leggerlo da pandas
df = pd.read_csv('vendite_sporco.csv')


tst("print DataFrame")
# Prende le prime 5 righe e Ultime 5 righe
p(df)

tst('testa - default')
# Prende le prime 5 righe
testa = df.head()
p(testa)

tst('coda - default')
# Prende le ultime 5 righe
coda = df.tail()
print(coda)

tst('testa primi 2 dati')

testa = df.head(n=2)
print(testa)

tst("coda ultimi 2 dati")
coda = df.tail(2)
print(coda)


tst('tipi di dati')
dati = df.dtypes

print(dati)

tst('forma')
forma = df.shape
print(forma)

