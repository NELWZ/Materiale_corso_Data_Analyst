import random
import time

s = "_" * 60
nome_giocatore = input("inserisci il tuo nome: ")
time.sleep(0.5)
punti_computer = 0
punti_giocatore = 0

mosse = ('sasso', 'carta', 'forbici')
    
while True:
    # === GAME OVER === #
    if punti_computer >= 5 or punti_giocatore >= 5:
        if punti_giocatore > punti_computer:
            time.sleep(0.5)
            print(f"{nome_giocatore} ha vinto la partita")
        else:
            time.sleep(0.5)
            print("il computer ha vinto la partita")
        break
    # ====================================================== #
    print(s)
    giocatore = input("sasso | carta | forbici: ")
    
    while True:
        if giocatore not in mosse:
            time.sleep(0.5)
            print("SCELTA NON VALIDA")
            time.sleep(0.5)
            giocatore = input("sasso | carta | forbici: ")
        if giocatore in mosse:
            break
    

    computer = random.choice(mosse)
        
    print(s)
    time.sleep(0.5)
    print(f'computer ha scelto: {computer}')
    
    # === PARI === #
    if giocatore == computer:
        print("Siete pari")
    
    # === VINCE IL PLAYER === #
    elif giocatore == "sasso" and computer == "forbici":
        time.sleep(0.5)
        print(f"{nome_giocatore} ha vinto| +1 punto per {nome_giocatore}")
        punti_giocatore += 1
    elif giocatore == "carta" and computer == "sasso":
        time.sleep(0.5)
        print(f"{nome_giocatore} ha vinto| +1 punto per {nome_giocatore}")
        punti_giocatore += 1
    elif giocatore == "forbici" and computer == "carta":
        time.sleep(0.5)
        print(f"{nome_giocatore} ha vinto| +1 punto per {nome_giocatore}")
        punti_giocatore += 1
    
    # === VINCE IL COMPUTER === #
    else:
        time.sleep(0.5)
        print("ha vinto il computer! +1 punto")
        punti_computer += 1
    
    