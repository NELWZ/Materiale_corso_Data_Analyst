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
# === CODICE === #
numero_segreto = 7
tentativi = 3

while True:
    if tentativi == 0:
        print("tentaivi finiti")
        break
    numero = int (input("inserisci il numero: "))
    tentativi -= 1
    if numero > numero_segreto:
        print (f"numero troppo grande, tentativi rimasti: {tentativi}")
    elif numero < numero_segreto:
        print(f"numero troppo piccolo, tentativi rimasti: {tentativi}")
    else:
        print ("indovinato")
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
    numero = int(input("inserisci un numero intero: "))
    if numero == 0:
        print (f"somma totale: {somma}")
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

while True:
    giocatore = input ("sasso/carta/forbici: ")
    if giocatore == "": break
    
    scelta_pc = "sasso", "carta", "forbici"

    computer = random.choice (scelta_pc)

    #pari
    if giocatore == computer:
        print (f"pareggio, il computer ha scelto: {computer}")
    #vince il giocatore
    elif giocatore == "sasso" and computer == "forbici":
        print (f"Hai vinto, il computer ha scelto: {computer}")
    elif giocatore == "carta" and computer == "sasso":
        print (f"Hai vinto, il computer ha scelto: {computer}")
    elif giocatore == "forbici" and computer == "carta":
        print (f"Hai vinto, il computer ha scelto: {computer}")
    #vince il computer
    elif giocatore == "sasso" and computer == "carta":
        print (f"Hai perso, il computer ha scelto: {computer}")
    elif giocatore == "carta" and computer == "forbici":
        print (f"Hai perso, il computer ha scelto: {computer}")
    elif giocatore == "forbici" and computer == "sasso":
        print (f"Hai perso, il computer ha scelto: {computer}")
    else:
        print ("Scelta non valida")


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

while True:
    numero1 = random.randint (1,6)
    numero2 = random.randint (1,6)

    print (f"Primo dado: {numero1}")
    print (f"Secondo dado: {numero2}")

    somma = numero1 + numero2
    print (f"la somma dei due dadi è: {somma}")
    
    continua = input ("continuare? (s/n): ")
    if continua == "n":
        print ("=== FINE===")
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
while True:
    moneta = random.randint (1,2)
    indovina = input("testa o croce: ")
    if indovina == "":
        break

    elif indovina == "testa" and moneta == 1: 
        print ("hai vinto")
    elif indovina == "croce" and moneta == 2:
        print ("hai vinto")
    else:
        print ("Hai perso")





# === ESERCIZIO 7 === #
"""
USA TIME (time.sleep(sec))
Chiedi all'utente di inserire un numero intero positivo. Tramite un 
ciclo while, crea un conto alla rovescia che stampa ogni numero fino ad 
arrivare a 0, stampando infine la scritta "Tempo scaduto!".

"""

import time

tempo = int(input("inserisci un numero: "))

while True:
    if tempo <= 0:
        print ("Tempo scaduto!")
        break
    print (f"Secondi: {tempo}")
    tempo -= 1
    time.sleep(1)

# === ESERCIZIO 8 === #
"""
Un utente ha a disposizione al massimo 3 tentativi per inserire il PIN 
corretto (es. 1234). Se sbaglia, decrementa i tentativi rimasti. Se sbaglia 
per 3 volte di seguito, il programma stampa "Carta bloccata" e termina il 
ciclo while. Se lo azzecca prima, stampa "Accesso consentito".
"""

# === ESERCIZIO 9 === #
"""
Chiedi all'utente di inserire una serie di numeri positivi, fermandoti 
quando inserisce un numero negativo. Utilizzando le condizioni all'interno del 
ciclo while, tieni traccia del numero più grande inserito finora e 
stampalo alla fine.
"""



