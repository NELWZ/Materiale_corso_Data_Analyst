import pandas as pd
def s(l=60, c="_"): print(c * l)

df = pd.read_csv('frutta.csv')

print(df)
s()

t = df.head()
print(t)
s()

t = df.head(2)
print(t)
s()

c = df.tail()
print(c)
s()

c = df.tail(2)
print(c)
s()

f = df.shape
print(f)
s()
u = df['frutto'].unique()
print(u)
s()
nu = df['frutto'].nunique()
print(nu)
s()
# df['totale'] = df['quantita'] * df['prezzo']
df['totale'] = round((df['quantita'] * df['prezzo']), 2)
print(df)
s()

print(max(df['totale']))
s()

print(round(sum(df['totale']), 2))
s()

print(min(df['totale']))
s()

gr1 = df.groupby('frutto')['quantita'].sum().round(2)
print(gr1)
s()

gr2 = df.groupby('frutto')['quantita'].sum().idxmax()
print(gr2)
s()

gr3 = df.groupby('frutto')['totale'].sum().round(2)
print(gr3)
s()

gr4 = df.groupby("frutto")['totale'].mean().round(2)
print(gr4)
s()

r = df['frutto'].value_counts()
print(r)

df.to_csv("frutta.csv")


