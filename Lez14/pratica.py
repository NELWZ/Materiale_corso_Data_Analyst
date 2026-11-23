import random 
budget = 100
borsa = {}
totale = 0

for p in range(5):
    prodotto = input("nome prodotto: ")
    borsa[prodotto] = random.randint(1, 20)
    
totale = sum(borsa.values())

print(f"In totale ti costa: €{totale}")

if budget >= totale:
    soldi_rimanenti = budget - totale
    print(f"Ti rimangono €{soldi_rimanenti}")
else:
    print("Non hai i soldi")


if budget >= totale:
    budget -= totale
    print(f"Ti rimangono €{budget}")
else:
    print("Non hai i soldi")

