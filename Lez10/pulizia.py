import pandas as pd
from pathlib import Path as p

# pip install pathlib
# python -m pip install pathlib

'MAC & LINUX'
# pip3 install pathlib


file = './Lez10/sporco.csv'
#^ === CARICAMENTO === #
fp = p(file)

if not fp.exists():
    pass

df = pd.read_csv(fp)

# print(df)

# === DEBUG INFO === #
df.info()

# === VAORI MANCANTI ===
value_null = df.isnull()
print(value_null)

# SOMMA (sum) dei valori mancanti per ogni categoria nel file
value_null = df.isna().sum()
print(value_null)

