# === ESERCIZIO 1 === #
"""
Chiedi all'utente di impostare una password
iniziale (salvandola in una variabile). 

Dopodiché, tramite un ciclo while, chiedi 
continuamente di inserire la password finché 
non corrisponde a quella corretta. 

Quando viene indovinata, stampa un 
messaggio di benvenuto.
"""
# === CODICE === #

pu = input("password: ")

while True: # infinito
    password = input("conferma password: ")
    if password == pu:
        print("no way")
        break

# === ESERCIZIO 2 === #
"""
Imposta un numero segreto fisso (es. 7). 
L'utente ha a disposizione massimo 3 tentativi 
per indovinarlo inserendo un numero da tastiera. 

Usa un ciclo while e le condizioni per dire se il 
numero inserito è troppo alto o troppo 
basso, interrompendo il ciclo se finiscono 
i tentativi o se viene indovinato.
"""

numero = 6

tentativi = 3

while True:
    if tentativi <= 0:
        print("tentativi finiti!")
        break
    indovina = int(input("Indovina il numero: "))
    tentativi -= 1 # tentativi = tentativi - 1
    
    if indovina > numero:
        print("troppo grande")
    elif indovina < numero:
        print("troppo piccolo")
    else:
        print("waw hai vinto")
        break

# === ESERCIZIO 3 === #
"""
Crea un programma che chiede all'utente di 
inserire dei numeri interi uno alla volta. 

Il ciclo while deve continuare finché l'utente 
inserisce un numero diverso da 0. 

Alla fine, stampa la somma totale di 
tutti i numeri inseriti.
"""

somma = 0

while True:
    numero = int(input("inserisci un numero: "))
    if numero == 0:
        print(f"somma totale: {somma}")
        break
    somma += numero


# === ESERCIZIO 4 === #
"""
Fai scegliere all'utente tra "sasso", "carta" o "forbici" tramite input(). 

Genera una scelta casuale per il computer usando 
random.choice(["sasso", "carta", "forbici"]). Tramite le condizioni, confronta 
le due scelte, stabilisci chi ha vinto (o se è pareggio) e stampa il risultato. 

Usa un ciclo while per permettere di rigiocare finché l'utente non digita "esci".
"""

import random
nome_giocatore = input("inserisci il tuo nome: ")
nome_computer = "Computer"
mosse = ["sasso", "carta", "forbici"]
Computer = random.choice(mosse)
while True:

    if nome_giocatore == nome_computer:
        print("pareggio")
    elif (nome_giocatore == "sasso" and nome_computer == "forbici") or (nome_giocatore == "carta" and nome_computer == "sasso") or (nome_giocatore == "forbici" and nome_computer == "carta"):
        print("hai vinto")
    elif (nome_computer == "sasso" and nome_giocatore == "forbici") or (nome_computer == "carta" and nome_giocatore == "sasso") or (nome_computer == "forbici" and nome_giocatore == "carta"):
        print("hai perso")
        
    scelta = input("vuoi rigiocare? (si/esci):")
    if scelta == "esci":
        break
    elif scelta == "si":
        nome_giocatore = input("inserisci il tuo nome: ")
        Computer = random.choice(mosse)
    else:
        print("scelta non valida")





# === ESERCIZIO 5 === #
"""
USA RANDOM
Crea un programma in cui l'utente lancia due dadi a 6 facce (genera due numeri
casuali da 1 a 6 con random.randint(1, 6)). 

Stampa i due valori ottenuti e la loro somma. 

Chiedi poi all'utente tramite un ciclo while se vuole 
ripetere il lancio ("s/n") o fermarsi.
"""
import random
punti = 0
while True:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    somma = dado1 + dado2
    print(f"i dadi sono: {dado1} e {dado2}\nsomma: {somma}")
    scelta = input("vuoi rigiocare? (s/n): ")
    if scelta == "n":
        break


# === ESERCIZIO 6 === #
"""
Simula il lancio di una monetina usando random.randint(1, 2) 
(dove ad esempio 1 è "Testa" e 2 è "Croce"). 

Chiedi prima all'utente di puntare su "testa" o "croce" con un input().
Estrai il lancio casuale, confrontalo con la scelta dell'utente e stampa se ha 
indovinato o ha perso, tenendo il conto delle partite vinte in un ciclo while
finché non decide di smettere.
"""


import random
punti = 0
while True:
    moneta = random.randint(1, 2)
    scelta = input("testa o croce? (esci per terminare): ")
    if scelta == "esci":
        break
    elif scelta == "testa" and moneta == 1:
        print("hai vinto")
        punti += 1
    elif scelta == "croce" and moneta == 2:
        print("hai vinto")
        punti += 1
    else:
        print("hai perso")
        
    print(f"PUNTI: {punti}")

# === ESERCIZIO 7 === #
"""
USA TIME (time.sleep(sec))
Chiedi all'utente di inserire un numero intero positivo. Tramite un 
ciclo while, crea un conto alla rovescia che stampa ogni numero fino ad 
arrivare a 0, stampando infine la scritta "Tempo scaduto!".
"""
import time
tempo = int(input("inserisci i secondi: "))
while True:
    print(f"secondi: {tempo}")
    time.sleep(1)
    tempo -= 1
    if tempo <= 0:
        print("tempo scaduto!")
        break

# === ESERCIZIO 8 === #
"""
Un utente ha a disposizione al massimo 3 tentativi per inserire il PIN 
corretto (es. 1234). Se sbaglia, decrementa i tentativi rimasti. Se sbaglia 
per 3 volte di seguito, il programma stampa "Carta bloccata" e termina il 
ciclo while. Se lo azzecca prima, stampa "Accesso consentito".
"""
PIN = "1234"
print(PIN)
tentativi = 3
while True:
    if tentativi == 0:
        print("Carta bloccata")
        break
    numero = input("indovina il PIN: ")
    tentativi -= 1
    if numero == PIN:
        print("Sei dentro")
        break

# BRUTE FORCE #

t = 0

while True:
    num = random.randint(0000,9999)
    t += 1
    print(num)
    if str(num) == PIN:
        print(f"indovincato in {t} tentativi")

# === ESERCIZIO 9 === #
"""
Chiedi all'utente di inserire una serie di numeri positivi, fermandoti 
quando inserisce un numero negativo. Utilizzando le condizioni all'interno del 
ciclo while, tieni traccia del numero più grande inserito finora e 
stampalo alla fine.
"""
massimo = 0
while True:
    numero = int(input("inserisci un numero: "))
    if numero < 0:
        print(f"il numero più grande è: {massimo}")
        break
    elif numero > massimo:
        massimo = numero

