spesa = []

print("=== FOR ===")
for i in range(5):
    spesa.append(input("nome prodotto: "))
    print(spesa)

spesa.clear()
print("=== WHILE ===")
numero_prodotti = 5
while True:
    spesa.append(input("nome prodotto: "))
    print(spesa)
    numero_prodotti -= 1
    if numero_prodotti == 0:
        break
