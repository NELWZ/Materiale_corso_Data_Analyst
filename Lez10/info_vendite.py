import pandas as pd

def s(l=50, c=":"):
    print(l * c + "\n")

def txt(t=""):
    print(f"◄===== {t} =====►")

#^ === APRIRE (LEGGERE) UN FILE ===
'creare un DataFrame'
df = pd.read_csv('./Lez10/vendite.csv')

# print(df)

txt("TESTA")
testa = df.head() # PRIME 5 RIGHE
s()
print(testa)
txt('CODA')
coda = df.tail(n=2) # ULTIME 5 RIGHE
s()
print(coda)
s()

txt("FORMA")
forma = df.shape # (righe, colonne) ► (6, 5)
print(forma)
s()


txt("COLONNA")
colonna = df.columns # COLONNE
print(colonna)
s()

txt("INFO")
info = df.info() # MOSTRA DELLE INFORMAZIONI
print(info)
s()

txt("DATA TYPE")
tipo_data = df.dtypes

print(tipo_data)
s()

txt("IS NULL")

nullo = df.isnull()
print(nullo)

txt("SOMMA DEI NULL")
somma_nullo = df.isnull().sum()
print(somma_nullo)
