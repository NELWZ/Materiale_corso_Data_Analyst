import random

dado = random.randint(1, 6)

numero = int(input("indovina il numero da 1 a 6: "))

if numero == dado:
    print(f"Hai vinto, il numero è {dado}")
else:
    print(f"Non hai vinto, il numero era {dado}")

