from random import choices as c
from time import sleep as s

soldi = 1000

slot = ['🍋','🍉','🍒']

while True:
    if soldi <= 0:
        print("Hai perso ogni soldo")
        break
    s(0.1)
    print(f"SALDO TOTALE: €{soldi}")
    s(0.1)
    gioco = input("Giochi? s/n: ")
    if gioco == "n":
        print(f"Ti porti a cas un totale di €{soldi}")
        break
    giri = int(input("numero giri: "))
    s(0.1)
    if soldi >= 20 * giri:
        print(f"Hai puntato €{20 * giri}")
        s(0.1)
        soldi -= 20 * giri
        for i in range(giri):
            risultato = c(slot, k=3, )
            print("▄" * 15)
            s(0.1)
            for r in risultato:
                print(r, end=" | ")
                s(0.1)
            if risultato[0] == risultato[1] == risultato[2]:
                print("► Waw hai vinto €100")
                s(0.1)
                soldi += 100 
            print()
    else:
        s(0.1)
        print(f"Non hai abbastanza soldi\nHai €{soldi}/{20*giri}")
