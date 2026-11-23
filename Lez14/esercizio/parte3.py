quant = int(input("Qunti prodotti hai preso: "))

totale = 0
for p in range(quant):
    spesa = float(input(f"Qaunto costa il prodotto {p+1}: "))
    totale += spesa
print(f"In totale hai speso: €{totale:.2f}")

