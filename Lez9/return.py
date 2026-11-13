# === RETURN === #
'blocca la funzione e ritorna il valore'
def somma(lista):
    return sum(lista)

lista = [5,5,5,5,50]
somma(lista) # somma della lista

x = somma(lista) # 70

#? somma() → 70

x = 70
# print(x)
# x = sum(lista)
# print(x)
# x = somma(lista)
# print(x)
# ============================== #

def utenti(nome, cognome, email):
    database = {}
    utente = {'nome': nome,'cognome': cognome,'email': email}
    database['utente1'] = utente
    
    return database

u = utenti('Mario', 'Rossi', 'rossimario@gmail.com')

# print(u)

def uno():
    return 1

x = uno() + 5

# print(x)

def numero(n=0):
    return n

x = numero(50)

print(x * 5)



'Bloccare una funzione e RITORNARE un valore'
'Trasformare la vostra funzione in un vero e proprio VALORE'


def nome():
    return "Celeste"

print(f"Ciao {nome()}")


