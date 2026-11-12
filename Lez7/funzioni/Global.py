import random

#? === SOMMA ===
def somma():
    c = 1
    somma = 0
    while True:
        numero = float(input(f"inserisci il numero_{c}: "))
        c += 1
        if numero == 0:
            break
        somma += numero
    print(somma)

#^ === RIPETITORE ====
def ripeti():
    parola = input("parola da ripetere: ")
    num_volte = int(input("numero di volte: "))
    for x in range(num_volte):
        print(parola)

#! === DADO === 
def dado():
    dado = random.randint(1,6)
    numero = int(input("indovina il numero: "))
    if numero == dado:
        print("hai vinto")
    else:
        print("hai perso")