from random import randint as r
#~ === LIVELLO 1 → FUNZIONE SEMPLICE === #
'def nome_funzione():'

def saluto():
    print('ciao mondo')

#? === USARE === #
#^ saluto()

#! === ESEMPI ===
def somma_semplice():
    print(2+2)
#^ somma_semplice()

def timer():
    import time
    secondi = int(input("secondi: "))
    for t in range(secondi):
        print(f"S: {secondi}")
        time.sleep(1)
        secondi -= 1
    print("Tempo scaduto")

#^ timer()

#& === LIVELLO 2 === 
'FUNZIONI MODULARI'

def saluto_2(nome):
    print(f"ciao {nome}")

#?=== EVOCAZIONE DELLA FUNZIONE === #
#^ saluto_2('Sarah')
#^ saluto_2('Panda')
#^ saluto_2('Celeste')
#^ saluto_2('Pietro')
#^ saluto_2(2+2)
#^ saluto_2(True)
#^ saluto_2([1,2,3])
#^ saluto_2(input())
#^ saluto_2(timer())


#! === ESEMPI === !#
def somma(a, b):
    print(a + b)

#^ somma(2, 6)
#^ somma(15.2, 3.14)
#^ somma(True, True)
#^ somma('ciao ', 'Panda')
#^ somma([1,2,3], [4,5,6])
#^ somma(r(1,20), r(1,20))
#^ somma(r(1,20), r(1,20))
#^ somma(r(1,20), r(1,20))
#^ somma(r(1,20), r(1,20))
#^ somma(r(1,20), r(1,20))
#^ somma(r(1,20), r(1,20))
#^ somma(r(1,20), r(1,20))

# ====================================== #
def ciao():
    print("ciao Sarah")

def _ciao(nome):
    print(f"ciao {nome}")

#^ ciao() # ciao Sarah
#^ ciao() # ciao Sarah
#^ ciao() # ciao Sarah

#^ _ciao("Sarah")
#^ _ciao("Pietro")
#^ _ciao("Celeste")
# ====================================== #

#! esempio 2 #

database = []

def crea_utente(id, nome, cognome, email):
    utente = {
        'id': id,
        'nome': nome,
        'cognome': cognome,
        'email': email
        }
    database.append(utente)



#^ crea_utente(1,'Marco', 'Rossi', 'rossimarco@gmail.com')

#^ crea_utente(id=2, nome='Luca', cognome="Verdi", email="verdiluca@gmail.com")
#^ crea_utente(cognome="Falco", id=3, email="falcoandrea@gmail.com", nome="Andrea")

#^ crea_utente(input("ID: "), input("None: "), input("Cognome: "), input("Email: "))

#^ i, n, c, e = input('ID: '),input('Nome: '),input('Congome: '),input('Email: ')

#^ crea_utente(i,n,c,e)


#& === LIVELLO 3 === 
def crea_utenti(id=1, nome='Marco', cognome='Rossi', email='rossimarco@gmail.com'):
    utente = {
        'id': id,
        'nome': nome,
        'cognome': cognome,
        'email': email
        }
    if utente in database:
        print("ERRROE: Utente è già presente nel Database")
    else:
        database.append(utente)
    
#? === EVOCAZIONE === ?#
crea_utenti()

crea_utenti(2, 'Luca', 'Verdi', 'verdiluca@gmail.com')



#! === ESEMPIO === !#
# print()
# print(2)
# print(2+2)
# print('ciao')
# print()
# print()
# print(end='-')
# print(end='-')
# print(end='!')
# print(end='ciao')

#^ ======================================================================================= #
'LIVELLO 1'

def saluto1():
    print("Ciao Marco")

print("=== LIVELLO 1 ===")

saluto1()
saluto1()
saluto1()
saluto1()
saluto1()

print("=== LIVELLO 2 ===")

def saluto2(nome):
    print(f"Ciao {nome}")

saluto2("Celeste")
saluto2("Panda")
saluto2(5 * 5 + 2)
saluto2([1,2,3,4,5,6])


print("=== LIVELLO 3 ===")

def saluto3(nome="Celeste"):
    print(f"Ciao {nome}")

saluto3()
saluto3()
saluto3()
saluto3()

print("________________________________________")

saluto3('Pietro')
saluto3('Marco')
saluto3(True)
saluto3(2+2)
saluto3({'id': 1})
