import random

moneta = random.randint(1, 2)

scelta = int(input("1-Testa | 2-Croce: "))

if scelta == moneta:
    print("Hai vinto")
else:
    print("Hai perso")

print("Hai vinto") if scelta == moneta else print("Hai perso")

