from random import choice

mosse = ['testa', 'croce']
punti_at = 0
punti_max = 0

#^ LETTURA FILE
with open('punti_moneta.txt', "r") as f:
    punti = f.read()
    'se esiste il contenuto nel file'
    if punti:
        punti_max = int(punti)

t = int(input("Qunate partite?\n: "))

for i in range(t):
    moneta = choice(mosse)
    indovina = input("testa o croce: ").lower()
    if moneta == indovina:
        print("hai vinto")
        punti_at += 1
        if punti_at > punti_max:
            punti_max = punti_at
    else:
        print("hai perso")

print("=== PUNTI ===")
print(f"Punteggio attuale: {punti_at}")
print(f"Punteggio Massimo: {punti_max}")

# === SALVA I PUNTI MASSIMI === #
with open("punti_moneta.txt", "w") as f:
    f.write(f"{punti_max}")
