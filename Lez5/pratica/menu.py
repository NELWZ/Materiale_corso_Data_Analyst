piatti = ['purè', 'pizza', 'tortellini', 'hamburger', 'cotoleta', 'carbonara']

prezzi = [2.99, 6.85, 3.0, 4.99, 5.0, 6.65]

totale = 0

for o in range(5):
    ordine = input("piatto: ")
    if ordine in piatti:
        p = piatti.index(ordine)
        totale += prezzi[p]
    else:
        print("Piatto non è nel menù")

print(f"Totale: €{totale}")

