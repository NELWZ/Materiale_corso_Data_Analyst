# === RIPASSO === #
print() # print è una funzione Built-in di python
print(2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2)
print("ciao mondo")

variabili = "contenitori di dati con un nome scelto da noi"

nome = "Celeste"
cognome = "Rossi"
anni = 25
altezza = 1.72

# tipi di dati 
'stringhe → str()'

x = "ciao io sono una stringa"
y = 'ciao anche io sono una stringa'

# numerici
anni = 25
pi = 3.14

x = 5

y = x + 5 # x originale non varia: rimane sempre 5

x = x + 5
x += 5

# +=
# -=
# *=
# /=

# Condizioni
if x:
    pass
elif x:
    pass
else:
    pass

# indentazioni
if x: # A
    if y: # B → BA
        pass # codice B
    elif x: # C → CA
        pass # codice  C
    else: # D → DA
        if x: # E → ED
            pass # codice  E
        elif y: # F → FD
            if x: # G → GF
                pass # codice F 
            else: # H → HF
                pass # codice H
        else: # J → JD 
            pass # codice J 
else: # K
    pass # codice K

if x:
 pass
if x:
 if y:
  pass

# ============================================================================= #
'operatori di confronto'
'''
==
!=
>
>=
<
<=
or
not
in
is
'''

# booleani
True
False

can_open = False
can_print = True
if can_open:
    f = open("file.txt", 'r')
    if can_print:
        print(f)


lista = []

x = [1,2,3,4,5,6,7,8,9]

ldl = [[[[[[[[[[]]]]]]]]]]

dato = [1,2,3,4,5,[1,2,3,4,[1,2,3,[1,2,['dato'],3,4,5,6],4],5,6],[1,2,3],6,7,8,9]

lista.append('dato, si mette alla fine della lista')

lista.insert(0, 'il dato che sta nella posizione 0')

lista.remove('dato da rimuovere')
lista.pop() # leimina ultimo dato
lista.pop(2) # elimina il dato con indice 2

lista.clear()

dizionari = {}
{
    'chiave': 'valore',
    'nomi': ['Celeste', 'Marco', 'Luca', 'Sarah'],
    'indirizzo': {
        'città': 'Reggio Calabria',
        'CAP': 15245,
        'n_civico': 78
    },
    input(): 5,
    print(): print(),
    [1,2,3,4]: True
}

def funzione():
    return 'livello 1'

print(funzione()) # 'livello 1'

def lista():
    return [1,2,3,4,5,6]

lista()[2] # 3

x = lista() # [1,2,3,4,5,6]

lista().append("ciao")

while False:
    pass

while True:
    break

x = 10

while x > 0:
    print(x)
    x -= 1

for variabile in range(9):
    break


with open("file.txt", "r", encoding='utf-8') as variabile:
    variabile.read()


import random as r
import groq as gr
import chat_semplice as cs
import antigravity as a
from chat_semplice import get_api as ga



import pandas as pd

dati = {
    'nomi': ['Celeste','Sarah','Alessia','Luca','Marco','Andrea'],
    'vendite': ['tavolo','computer','tazza','divano','panda','mouse'],
    'prezzi': [152.25,6325.25,32.00,36.58, 'abc', ""]
}

df = pd.DataFrame(dati)

print(df)

