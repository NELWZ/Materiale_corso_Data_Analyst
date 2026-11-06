# importato il file random.py
import random

nome = input("Nome: ")
# variabile "giocatore" che è un input
giocatore = input("sasso-carta-forbici: ")

# variabile "scelta_pc" contiene una tupla stringhe
scelte_pc = ('sasso', 'carta', 'forbici')

# variabile "computer" contiene la scelta casuale dei dati
computer = random.choice(scelte_pc)

# stampiamo la scelta del computer
print(f"Il computer ha scelto: {computer}")

# === CONDIZIONI === #
'SE computer è identica a quella del giocatore'
if computer == giocatore:
    print("Siete Pari")

# PERDE IL COMPUTER #
elif giocatore == "sasso" and computer == "forbici":
    print(f"Ha vinto {nome}")
elif giocatore == "carta" and computer == "sasso":
    print(f"Ha vinto {nome}")
elif giocatore == "forbici" and computer == "carta":
    print(f"Ha vinto {nome}")
# PERDE IL GIOCATORE #
elif giocatore == "sasso" and computer == "carta":
    print("Ha vinto il computer")
elif giocatore == "carta" and computer == "forbici":
    print("Ha vinto il computer")
elif giocatore == "forbici" and computer == "sasso":
    print("Ha vinto il computer")
else:
    print(f'la scelta "{giocatore}" non è valida')
    