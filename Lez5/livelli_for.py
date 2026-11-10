# =========================================== #
# === LIVELLO 1 === #
'ciclo for semplice'

'for variabile in range(numero):'
for i in range(10):
    break

# === LIVELLO 2 === #
'for variabile in range(minimo, massimo):'
for i in range(5, 10):
    break
    # 0 → ❌
    # 1 → ❌
    # 2 → ❌
    # 3 → ❌
    # 4 → ❌
    # 5 → ✔️
    # 6 → ✔️
    # 7 → ✔️
    # 8 → ✔️
    # 9 → ✔️


# === LIVELLO 3 === #
'for variabile in range(minimo, massimo, passo):'

for i in range(2, 10, 2):
    break
    # 0 ❌
    # 1 ❌
    # 2 ✔️
    # 3 ❌
    # 4 ✔️
    # 5 ❌
    # 6 ✔️
    # 7 ❌
    # 8 ✔️
    # 9 ❌
