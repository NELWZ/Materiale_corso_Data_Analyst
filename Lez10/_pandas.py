import pandas as pd

def s(l=60):
    print('_' * l)

dati = {
    'nomi': [f'Nome{i}' for i in range(1, 51)],
    'cognomi': [f'Cognome{i}' for i in range(1, 51)],
    'stipendi': [1200 + i * 25 for i in range(50)]
}

# print(dati)
# s()

# for k,v in dati.items():
#     print(k,v)
# s()

# DATAFRAME
df = pd.DataFrame(dati)
print(df)



