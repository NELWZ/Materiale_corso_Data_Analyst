# === RIPASSO === #
'VARIABILI → CHIAVE = VALORE'
# chiave = valore
numero = 15
numero = 5

numero = numero + 1 # 6

print(numero + 1)
print(numero)

x = numero + 1

x = x * 2 # → x *= 2
x = x + 1 # → x += 1
x = x - 1 # → x -= 1
x = x / 2 # → x /= 2


unavariabilemoltolungainquestocaso = 15

unavariabilemoltolungainquestocaso += 1

unavariabilemoltolungainquestocaso = unavariabilemoltolungainquestocaso + 1


# === TIPI DI DATI === #
'''
NUMERICI
    ╚→ int() → interi → anni = 25
    ╚→ float() → decimali → altezza = 1.75

STRINGHE
    ╚→ str() → 'parola' "frase"

BOOLEANI 
    ╚→ True & False → fame = True | sonno = False | Luce = True | Rotto = False
'''

# === OCNDIZIONI === #
'''
IF      → se → if True:
ELIF    → altrimenti se → elif True:
ELSE    → altrimenti → else:

==========================================================
== → UGUALE A → 5 == 5 ► True
!= → DIVERSO DA → 5 != 5 ► False | 5 != 4 ► True
>  → MAGGIORE DI → 5 > 3 ► True
>= → MAGGIORE DI O UGUALE A → 5 >= 5 ► True
<  → MINORE DI → 5 < 15 ► True
<= → MINORE DI O UGUALE A → 5 <= 5 ► True | 5 <= 10 ► True
____________________________________________________________________
AND → E → if 5 > 2 and 7 < 15: ► True and True = True
OR  → O → if 5 > 2 or 7 > 8: ► True or False = True
IN  → IN → if "a" in "ciao" ► True
NOT → NON E' → if "a" not in "buono" ► True
'''

# === IMPORT === #
'serve per importare i moduli'
import random
import time
import os
from datetime import datetime
import tkinter as tk
import pandas as pd
from colorsys import hls_to_rgb as htr

# === LISTE === #
frutta = ['mela', 'uva', 'kiwi']

# === ADD DATA === #
'APPEND() → dove.append(cosa)'

frutta.append("ananas") # → ['mela', 'uva', 'kiwi', 'ananas']

'INSERT() → dove.insert(posizione, cosa)'
frutta.insert(2, 'pesca') # → ['mela', 'uva', 'pesca', 'kiwi', 'ananas']

# === DELETE DATA === #
'REMOVE() → da_dove.remove(cosa)'
frutta.remove('kiwi') # → ['mela', 'uva', 'pesca', 'ananas']

'POP() → da_dove.pop() | da_dove.pop(posizione)'
frutta.pop() # → ['mela', 'uva', 'pesca']

frutta.pop(0) # → ['uva', 'pesca']

'CLEAR() → da_dove.clear()'
frutta.clear() # → []
"→↓←↑ ► 24 | 25 | 26 | 27"
"-►    ◄-"
# === INDICI === #

#         0    1    2    3    4    5    6    7
lista = ['D1','D2','D3','D4','D5','D6','D7','D8']
#        -8   -7   -6   -5   -4   -3   -2   -1


lista # ['D1','D2','D3','D4','D5','D6','D7','D8']

lista[5] # D6
lista[-6] # D3

# === SLICING === #
lista[2:5] # → ['D3','D4','D5']

# === WHILE === #
'LOOP INFINITO'

'''
while True: → fino a quando io sono True: eseguo il codice dentro di me
'''

while True:
    print("infinito")
    break
    # finito

# ... 



