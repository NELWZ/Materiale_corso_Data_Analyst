import pandas as pd 
from pathlib import Path

file = './Lez10/sporco.csv'

def check(nome_file):
    fp = Path(nome_file)
    if not fp.exists():
        return False
    return True

def load_file(nome_file):
    if check(nome_file):
        df = pd.read_csv(nome_file)
        return df
    
def info(nome_file, debug=False):
    df = load_file(nome_file)
    val_null = df.isnull()
    val_null_sum = df.isnull().sum()
    
    if debug:
        print(df)
        print(val_null)
        print(val_null_sum)
        
    return f"{df}\n{val_null}\n{val_null_sum}"

info(file, False)

i = info(file)

print(i)




