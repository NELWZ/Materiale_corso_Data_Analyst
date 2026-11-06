import random

registered = False

nomi = []
punteggi = []
punti = 0

vite = 3

while True:
    if vite == 0:
        if input("continuare? s/n: ") == "s":
            punteggi.append(punti)
            punti = 0
            vite = 3
            registered = False
            print("PUNTEGGIO")
            print(nomi)
            print(punteggi)
        else:
            i = 0
            while i < len(nomi):          # FIX: was `i > len(nomi)` → IndexError / never ran correctly
                print(f"Nome: {nomi[i]} - Punti: {punteggi[i]}")
                i += 1
            break

    if not registered:
        nome = input("nome player:")
        while len(nome) < 3 or nome in nomi:
            if nome in nomi:
                print("Utente già presente")
            else:
                print("il nome deve essere più lungo di 3 lettere")
            nome = input("nome player:")
        registered = True
        nomi.append(nome)

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    somma = num1 + num2

    risultato = int(input(f"{num1} + {num2} = "))
    if risultato == somma:
        print(f"Giusto! fa {somma} +1 punto")
        punti += 1
        print(f"PUNTI TOTALI: {punti}")
    else:
        vite -= 1
        print(f"No! {num1} + {num2} non fa {risultato} ma fa {somma} | Hai perso una vita | Vite rimaste:  {vite}")