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
# === ESERCIZIO 3 === #
"""
Crea un programma che chiede all'utente di 
inserire dei numeri interi uno alla volta. 

Il ciclo while deve continuare finché l'utente 
inserisce un numero diverso da 0. 

Alla fine, stampa la somma totale di 
tutti i numeri inseriti.
"""
# === ESERCIZIO 4 === #
"""
Fai scegliere all'utente tra "sasso", "carta" o "forbici" tramite input(). 

Genera una scelta casuale per il computer usando 
random.choice(["sasso", "carta", "forbici"]). Tramite le condizioni, confronta 
le due scelte, stabilisci chi ha vinto (o se è pareggio) e stampa il risultato. 

Usa un ciclo while per permettere di rigiocare finché l'utente non digita "esci".
"""

# === ESERCIZIO 5 === #
"""
USA RANDOM
Crea un programma in cui l'utente lancia due dadi a 6 facce (genera due numeri
casuali da 1 a 6 con random.randint(1, 6)). 

Stampa i due valori ottenuti e la loro somma. 

Chiedi poi all'utente tramite un ciclo while se vuole 
ripetere il lancio ("s/n") o fermarsi.
"""

# === ESERCIZIO 6 === #
"""
Simula il lancio di una monetina usando random.randint(1, 2) 
(dove ad esempio 1 è "Testa" e 2 è "Croce"). 

Chiedi prima all'utente di puntare su "testa" o "croce" con un input().
Estrai il lancio casuale, confrontalo con la scelta dell'utente e stampa se ha 
indovinato o ha perso, tenendo il conto delle partite vinte in un ciclo while
finché non decide di smettere.
"""

# === ESERCIZIO 7 === #
"""
USA TIME (time.sleep(sec))
Chiedi all'utente di inserire un numero intero positivo. Tramite un 
ciclo while, crea un conto alla rovescia che stampa ogni numero fino ad 
arrivare a 0, stampando infine la scritta "Tempo scaduto!".

"""

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
pas = input("immetti_password: ")

while True:
    conf_pas=input("conferma_password: ")
    if conf_pas == pas :
        print("Benvenuto")
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

numero_segreto = 5
tentativi = 0
max_tentativi = 3

while tentativi < max_tentativi:
    numero = int(input("Indovina il numero: "))
    tentativi += 1

    if numero == numero_segreto:
        print("Complimenti! Hai indovinato!")
        break

    elif numero < numero_segreto:
        print("Troppo basso!")

    else:
        print("Troppo alto!")

if tentativi == max_tentativi and numero != numero_segreto:
    print("Hai esaurito i tentativi!")
    print("Il numero segreto era:", numero_segreto)


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
numero = int(input("Inserisci un numero intero: "))

while True:
    numero = int(input("Inserisci un numero intero: "))
    if numero == 0:
        print(f"Somma totale: [somma]")
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
