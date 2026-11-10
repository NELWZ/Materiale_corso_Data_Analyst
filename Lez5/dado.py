from random import randint as r

tent = int(input("numero di tentativi: "))
while True:
    if tent <= 0:
        break
    dado = r(1, 6)

    numero = int(input("Numero: "))
    tent -= 1
    if numero == dado:
        print("Hai vinto")
    else:
        print('Hai perso')

tent = input("quanti tentativi: ")
for t in range(int(tent)):
    dado = str(r(1, 6))
    numero = input("Numero: ")
    if dado != numero:
        print("Hai perso")
    else:
        print("Hai vinto")
