"Se un'azione si ripete più di una volta: deve essere automatica"
import random
punti_giocatore =  0
punti_computer = 0

# === WRITE === #
def write_file(nome_file, metodo="w"):
    with open(nome_file, metodo) as f:
        f.write(str(punti_giocatore))

if int(input("numero: ")) == random.randint(1, 6):
    print("Hai vinto")
    punti_giocatore += 1
    # === SALVO I PUNTI IN UN FILE === #
    write_file('puntig.txt')
else:
    print("Hai perso")
    punti_computer += 1
    # === SALVO I PUNTI IN UN FILE === #
    write_file('puntic.txt', 'a')
print(f"PUNTI TOTALI\nGiocatore: {punti_giocatore}\nComputer: {punti_computer}")

import mysql.connector as msc

def conn(u='root', p='', h='localhost', c='utf8mb4', d=None, pr=3306):
    return msc.connect(
        user=u,
        password=p,
        host=h,
        charset=c,
        database=d,
        port=pr
    )

# conn()

# conn(u="new_utente")

# conn(h="new_host")

# conn(u='new_u', pr=80)
