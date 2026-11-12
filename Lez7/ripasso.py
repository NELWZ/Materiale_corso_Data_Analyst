#? === PRINT === #
print() #^ → evoca la funzione print
#! 'sarà inutile'

print('ciao mondo')
print(2+2)

#& 'print è una funzione per il DEBUG'

# === VARIABILI === #
'per creare una varibaile'
'nome_variabile = dato'
#& chiave = valore
nome_persona = "Celeste"
eta = 25

#? A COSA MI SERVE?
'conservare i dati dentro un contenitore'
a,s,d,f,h,j = 1,2,3,4,5,6

x = 5
y = 3.14

'se la variabile NON esiste: viene creata'
z = 9

'se la variabile ESISTE viene aggiornata'
z = 10
z = "panda"

#~ può avere molti tipi di dati

'=== TIPI DI DATI ==='

'''
STRINGHE
    ╚→ "stringa" | '15'
    'Nome "Marco" non esiste nel Database'
    "prendi l'ombrello"
    ↓
    "Nome \"Marco\" non esiste nel Database"
    'prendi l\'ombrello'

NUMERICI
    ╚→ INTERI → 1 | 5 | 20 ► anni = 25 | caramelle = 500 | kg = 450
    ╚→ DECIMALE → 3.14 | 0.5 | 1.25 ► altezza = 1.65 | altro = 0.025

BOOLEANO
    ╚→ CONTROLLO ► True | False ► finito = False | caldo = True
'''

#! 'C:\Users\avare\Desktop\L\Libs\docs'
#* 'C:\\Users\\avare\\Desktop\\L\\Libs\\docs'
#* 'C:/Users/avare/Desktop/L/Libs/docs'

print\
    (\
        2\
            +2) # print(2+2)

x = \
    5 # x= 5
x \
    = \
        5 # → x = 5

if \
x == \
5\
:
    \
                    (\
                        'ciao')

if x == 5:
    print("ciao")

# ==================================================== #
x = "15"

y = int(x)

'''
str() → int() ► int("15") → 15
str() → float() ► float('15') → 15.0
str() → bool() ► bool('15') → True

int() → str() ► str(15) → "15"
int() → float() ► float(15) → 15.0
int() → bool() ► bool(0) → False

float() → str() ► str(3.14) → "3.14"
float() → int() ► int(3.14) → 3
float() → bool() ► bool(3.14) → True

bool(-5) → True
bool(5) → True
bool(0) → False

bool('ciao') → True
bool("") → False
list(15) → [15]
list('ciao') → ['ciao'] 
'''

# ========================================================================= #
#^ CONDIZIONI ^#

semaforo = "rosso"
ferma = False

if semaforo == "rosso":
    ferma = True
elif semaforo == "giallo":
    ferma = True
elif semaforo == "verde":
    ferma = False
else:
    print("Errore")

'''
if → se ► se una condizione è Vera: succede qualcosa
elif → altrimenti se una condizione è Vera: succede qualcos'altro
else → altrimenti: succede qualcos'altro
'''
#! complessa
x = 5
y = 10
if (x > 2 and y < 20) and (x < 10 or y <= 10) and (y > 5 or x in [1,2,3]):
        print("ok")


#? === WHILE LOOP === #
num = int(input("Numero: ")) 
print(type(num))
molt = 0
massimo = int(input("limite: "))
while True:
    print(f"{num} x {molt} = {num * molt}")
    molt += 1
    if molt > massimo:
        molt = 0
        break

while molt > massimo:
    print(f"{num} x {molt} = {num * molt}")
    molt += 1


#^ === FOR LOOP === ^#
parola_da_ripetere = input("parola da ripetere: ")
quante_volte_deve_ripetere = int(input("quante volte: ")) 

for conto_quante_volte_deve_essere_ripetuto in range(quante_volte_deve_ripetere):
    print(parola_da_ripetere)

# ================================================================== #

secondi = 50

for tempo in range(secondi):
    print(secondi)
    secondi -= 1
    

#^ === LISTE === ^#

#           0       1       2        3       4      5       6
lista = ['Rosso','Verde','Viola','Giallo','Rosa','Bianco','Blu']

lista[4] #? → Rosa
lista[6] 

print(lista[0]) # → Rosso
print(lista[1]) # → Verde
print(lista[2]) # → Viola
print(lista[3]) # → Giallo
print(lista[4]) # → Rosa
print(lista[5]) # → Bianco
print(lista[6]) # → Blu

indice = 0

while indice < len(lista):
    print(lista[indice])
    indice += 1

for i in lista:
    print(i)

for i in range(len(lista)):
    print(lista[i])

#!        0123...                    27
parola = "il panda gioca nella giungla"

print(len(parola))

parola[5] # n

for lettera in parola:
    print(lettera)
    # i
    # l
    #  
    # ...
    # a

#! === DIZIONARI === !#
database = {
    'dipendenti': [
        {
            'id': 1,
            'nome': "Marco",
            'cognome': 'Rossi',
            'anni': 25,
            'stipendio': 35000,
            'email': 'rossimario@gmail.com'
        },
        {
            'id': 2,
            'nome': "Luca",
            'cognome': 'Verde',
            'anni': 45,
            'stipendio': 24500,
            'email': 'verdiluca@gmail.com'
        }],
    'prodotti': [
        {
            'id': 'p1',
            'categoria': 'elet.',
            'nome': 'computer',
            'quant': 2500,
            'costo_pz': '€799.99'
        }
    ]
    }

dati = database['prodotti'][0]['costo_pz'].replace("€", "")
conv = float(dati)
conv -= 5
print(conv)

# === FUNZIONE PERSONALE === #
def nome():
    print("ciao mondo")

nome()

max()
int()
float()
bool()
str()
print()
range()
len()
type()


