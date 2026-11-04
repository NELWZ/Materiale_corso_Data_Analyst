print(2+2)
print(2-1)
print(2*6)
print(4/2)
print((2 + 5) - (7/2) + 2 * 2 / (12 * 5))

print(5 * 2)
print (5*2)
print       (   5                    *2                                  )

print("2 + 2")

print('15' * 6)
print('ciao' * 6)
# ================================================================ #
s = '_' * 60

print(s)

nome = "Celeste"
cognome = "Rossi"

anni = 26
altezza = 1.72
print(f"Mi chiamo {nome} {cognome} ho {anni} anni e sono alta {altezza}m")

print(f'2 + 2 = {2 + 2}')

# CHIAVE = VALORE
chiave = "valore"

colore = "Viola"

# === REGOLE === #
'non usare gli spazi nei nomi delle varibili'
# colore semaforo = "rosso" → NO pliz

coloresemaforo = "verde"
coloreSemaforo = "giallo"
colore_semaforo = "rosso"

'non iniziare una variabile con un numero'

# 1nome = "Marco" → NO
nome1 = "Luca"
_7162838721798 = 15

'non usare i simboli nelle variabili'
#@[]{}!"£$%&/()=?^-+*/.,:;°§<>|\→☼♫↓←█▄☺☻♥♦♣♠◘○"

# +nome = 'Marta' → NO 

nome_persona = "panda"

_ = 15
_______________________________________ = 10.25

'non usare le parole riservate a python'

# print = 15
# if = 12.14

'CASE-SENSITIVE'
ciao = 1
Ciao = 2
CIAO = 3

Print = "ciao"

print(Print)

# ========================================= #
'TIPI DI DATI'
'''
Dato Numerico
    ► intero → int() → int(3.14) ► 3 | int('15') ► 15
    ► reale | decimale → float() → float(5) ► 5.0

Dato letterale
    stringa → str() → str(12) ► "12"

Dato booleano
    bool() → bool(15) ► True | bool(0) ► False
'''
print(s)

numero = input("scrivi un numero: ") # è una stringa

print(int(numero) * 2)
'''
int() ► str()       → 15 ► str(15) → "15"
int() ► float()     → 15 ► float(15) → 15.0
int() ► bool()      → 15 ► bool(15) → True

float() ► int()     → 3.14 ► int(3.14) → 3
float() ► str()     → 3.14 ► str(3.14) → "3.14"
float() ► bool()    → 3.14 ► bool(3.14) → True

str() ► int()       → '25' ► int("25") → 25 | 'panda' ► int("panda") → ERRORE
str() ► float()     → '25' ► float("25") → 25.0 | 'Ciao' ► float("Ciao") → ERRORE
str() ► bool()      → '25' ► bool("25") → True | '' ► bool("") → False
'''

'la virgola si usa per separare i dati'
'il punto si usa per due cose'
'1-accedere al dato, funzione, classe...'
'2-per segnare un numero mobile → 3.14, 1.25'