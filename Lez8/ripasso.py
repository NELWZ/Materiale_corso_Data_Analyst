#^ === VARIABILI ===
# sono dei contenitori di dati
chiave = "valore"
x = 5
l = ['cosa1', 'cosa2', 3,4,5]
d = {"chiave":  'valore'}

spesa = ['pane', 'mele', 'uva', 'biscotti']

spesa = {'pane':5, 'mele':'rosse', 'uva':'2kg', 'biscotti': 'al cioccolato'}

database = ['Mario', 'Luca', 'Alessia']

database = {'mario': ['email', 'password', 'id'], 'Luca': ['dati'], 'Alessia': ['dati']}

db = {
    'utenti': {
        'nomi': ['Mario', 'Luca', 'Alessia'],
        'cognomi': ['Mario', 'Luca', 'Alessia'],
        'anni': ["25",29,35],
        'stipendio': ['€1500', 2300, 500]
    }
}

anni_mario = db['utenti']['anni'][0]
numero_anni_mario = int(anni_mario)
numero_anni_mario += 1
print(numero_anni_mario)

#^ === TIPI DI DATI === #

'''
STRINGHE
    ╚→ str() → 'ciao' | "ciao" | "3.14" |
    nome = "Celeste"

NUMERI
    ╚→ INTERI → int() ► 1 | 25 | 40 |
    anni = 25
    ╚→ DECIMALI → float() ► 3.14 | 0.5 | 9.99 |
    altezza = 1.72

BOOLEANI
    ╚→ CONTROLLO → True | False
    attivo = True
'''

#^ === CONDIZIONI === #
colore = "verde"
possiamo_passare = True

#! === BLOCCO DEL SEMAFORO === 
if colore == "verde":
    possiamo_passare = True
elif colore == "giallo":
    possiamo_passare = False
else:
    possiamo_passare = False

#? === BLOCCO INFO === 
if possiamo_passare:
    print("passa")
else:
    print("fermati")

#^ === WHILE === 
while True:
    #! infinito
    break

# === WHILE CONTROLLATO === 
x = 10

while x > 0:
    print('ciao')
    x -= 1

#^ === FOR LOOP ===
for i in range(5):
    print('ciao')

for v in range(10):
    print('ciao')
    break

for v in range(-5, 10):
    print("ciao")
    # 0 = NO
    # 1 = NO
    # 4 = NO
    # 5 = SI
    # ...
    # 9 

# 1 2 3 4 5 6 7 8 9 10
# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
# 0 1 2 3 4 5 6 7 8 9

#& ======== FUNZIONI ======== &#
'LIVELLO 1'
def s1():
    print("_" * 60)

s1()

'LIVELLO 2'
def s2(l, c):
    print(c * l)

s2(20, "-")
s2(40, "▄")
s2(50, ".")
s2(60, "_")

'LIVELLO 3'
def s3(l=60, c="="):
    print(c * l)

s3()
s3(20)
s3(c="_")
s3(15, 'ciao')
s3(l=40, c='*')



