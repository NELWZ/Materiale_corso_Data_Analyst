#!=== SOLO LIVELLO 3 === #
from time import sleep as s
database = []

# === CREIAMO UNA FUNZIONE PER AGGIUNGERE UTENTI === #

def aggiungi_utente(id=1, nome="test1", congome="test1", email="test@gmail.com", password="testpswd"):
    utente = {'id': id, 'nome': nome, 'congome': congome, 'email': email, 'password': password}
    
    if utente not in database:
        database.append(utente)
        print(f'Utente {utente["nome"]} aggiunto nel database')
    else:
        print(f'ERRORE: Utente "{utente["nome"]}" già presente')

s(0.5)
print("print(database) ↓ ")
print(database)

s(1)
print("aggiungi_utente() ↓ ")
aggiungi_utente()
s(1)
print("aggiungi_utente() ↓ ")
aggiungi_utente()
s(0.5)
print(database)

aggiungi_utente(2, 'Marco', 'Rossi', 'rossimarco@gmail.com', 'marco123')
s(0.5)
aggiungi_utente(2, 'Marco', 'Rossi', 'rossimarco@gmail.com', 'marco123')
s(0.5)

aggiungi_utente(3, 'Luca', 'Verdi', 'lucaverdi@gmail.com', 'luca123')
s(0.5)
aggiungi_utente(4, 'Celeste', 'Falcon', 'falconceleste@gmail.com', 'celeste123')
s(0.5)

for dati in database:
    print(dati)
    s(0.2)