# =================================================================== #
'built-in function'
#& === PRINT ===
'stampante'
print()
print('CIAO')
print(2+2)

#& === TYPE === 
'verifica il TIPO di dato'
type(15) # class int
type('ciao') # class str

#& === LEN === 
'verifica la lunghezza di un dato'
parola = 'ciao'
len(parola) # 4

lista = [1,2,3,4,5,6,7,8,9]
len(lista) # 9


#& === INT === 
'Converte altri tipi di dati in intero'
int(3.14)   # → 3
int("15")   # → 15
int(True)   # → 1
int(False)  # → 0
#! int("ciao") # → ERRORE

#& === FLOAT === 
'Converte altri tipi di dati in decimale'
float(5)        # → 5.0
float('15')     # → 15.0
float(True)     # → 1.0
float(False)    # → 0.0
#! float('panda')  # → ERRORE

#& === STR === 
'Converte altri tipi di dati in stringa'
str(15)     # → "15"
str(3.14)   # → "3.14"
str(True)   # → "True"
str(False)  # → "False"

#& === BOOL === 
'Converte altri tipi di dati in booleano'
bool(15)        # → True
bool(3.14)      # → True
bool(-5)        # → True
bool(0)         # → False
bool('ciao')    # → True
bool('')        # → False

#& === LIST ===
list('abc') # → ['a', 'b', 'c']

#& === DICT === 
dict(a=1, b=2, c=3) # {'a': 1, 'b': 2, 'c': 3}
utenti = {'nome': 'Marco', 'cognome': 'Rossi', 'eta': 25, 'email': 'rossimarco@gmail.com'}
utenti = dict(nome="Marco", cognome="Rossi", eta=25, email="rossimario@gmail.com")

#& === RANGE ===
for i in range(0): pass
print(range(5))
list(range(5)) # [0,1,2,3,4]
print(list(range(5)))

a = list(range(4, 21, 2))
print(a)
# metodo 1
numeri = [0,1,2,3,4,5,6,7,8,9]

# metodo 2
lista = []
for numero in range(10):
    lista.append(numero) # [0,1,2,3,4,5,6,7,8,9]

# metodo 3
lista = [numero for numero in range(10)] # [0,1,2,3,4,5,6,7,8,9]

print([i for i in range(10)])

import time
secondi = 5

for s in range(secondi):
    print(secondi)
    secondi -= 1
    time.sleep(1)

#& === EXEC === 
#! exec("import time; secondi = 5; [print(s) or time.sleep(1) for s in range(secondi, 0, -1)]")
exec('print("ciao mondo"); x = 5; print(x)')

# leggi nella cartella Lez5 il file prod.py

# === FOR ===

for i in range(10):
    pass

for i in range(5, 10):
    pass

for i in range(1, 10, 2):
    pass
    # 0 → NO
    # 1 → SI
    # 2 → NO
    # 3 → SI

for i in range(10, 1, -4):
    pass
    # 10
    # 9
    # 8
    # ...
    # 1

#& === SUM ===
sum([1,2,3,4,5,6,7])
sum((5,8,7,5,6,9,5))

lista = [77,5,85,69,32,5,0]
sum(lista)

#& === MAX ===
max([1,2,3,4,5]) # 5
max((5,8,6,5,4,7,9,)) # 9

prezzi = [99,88,6,35,25]
max(prezzi) # 99

#& === MIN ===
min([1,2,3,4,5]) # 1
min((5,8,6,5,4,7,9,)) # 4

prezzi = [99,88,6,35,25]
min(prezzi) # 6

#& === ABS ===
abs(-7) # 7

#& === ROUND ===
round(2.2545875, 2) # 2.25
round(2.2545875, 1) # 2.2
round(2.2545875, 0) # 2.
round(2.2545875, 10) # 2.2545875000

#& === SORTED ===
lista = [8,5,3,2,1]
sorted(lista) # [1,2,3,5,8]
sorted(lista, reverse=True) # [1,2,3,5,8] → [8,5,3,2,1]
sorted(['b', 'c', 'a', 'A', 'D']) # [A,D,a,b,c]
sorted('Bogdan', 'Caterina', 'Alessia') # ['Alessia', 'Bogdan', 'Caterina']
sorted('Bogdan', 'Caterina', 'alessia') # ['Bogdan', 'Caterina', 'alessia]

#& === ISINSTANCE ===
dato = 5
isinstance(dato, int) # → True
isinstance(dato, float) # → False

#& === NEXT ===
'Ritorna il prossimo elemento di un iteratore'
#? ITERATORE → RIPETITORE
#^ ITERABILE → PUO' ESSERE ITERATO
lista = [1,'@',"?",4,[],True]
for dato in lista:
    pass#print(dato)

stringa = "ciao panda"
numero = (125458758659856325412548, 58562554558855, 14525788569663325)

it = iter([1,2,3])
next(it) # 1
next(it) # 2
next(it) # 3

it = iter('ciao')
next(it) # c
next(it) # i
next(it) # a
next(it) # o


#! stringhe
#& === STRIP ===
'ciao'.strip() # TOGLIE SOLO LI SPAZI ALL'INIZIO E ALLA FINE
'                   ciao          '.strip() # 'ciao'
'nome '.strip() # → 'nome
'   cognome '.strip() # → 'cognome
' città'.strip() # → 'cottà

#& === LOWER ===
'Ciao'.lower() # → 'ciao'
'CIAO'.lower() # → 'ciao'
'CIao'.lower() # → 'ciao'
'CiAO'.lower() # → 'ciao'
'mario@gmail.com'
'MarIO@GMAIL.coM'.lower() # → mario@gmail.com

#& === UPPER ===
'ciao'.upper() # → 'CIAO'
'cIao'.upper() # → 'CIAO'
'cIAO'.upper() # → 'CIAO'
'CiAo'.upper() # → 'CIAO'
def txt(x=""):
    print(f"=== {x} ===".upper())

txt() # === ===
txt("ciao") # === CIAO ===

#& === CAPITALIZE ===
'mario'.capitalize() # → Mario
'MaRIO'.capitalize() # → Mario
'MARIO'.capitalize() # → Mario


#& === OPEN ===
'serve per arpire e manipolare i file con python'

