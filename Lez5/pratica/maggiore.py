# === MAGGIORE TRA TUTTI I NUMERI === #

numeri = []

quant = int(input("quanti numeri: "))

massimo = 0

for n in range(quant):
    numero = int(input('numero: '))
    numeri.append(numero)
    
print(max(numeri))

