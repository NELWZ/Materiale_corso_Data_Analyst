# ======== MENU ======== #
primi_piatti = {
    'carbonara': 4.99,
    'lasagna': 7.50,
    'tortellini': 3.20,
    'pizza margherita': 5.0, 
    }

bevande = {
    'acqua liscia': 2.0,
    'acqua frizzante': 3.0,
    'cola': 3.50,
    'coca-cola': 4.99,
    'fanta': 3.99,
    'monster': 7.99
}

totale = []
numero_piatti = int(input("quanti piatti ordinare?\n: "))

for p in range(numero_piatti):
    cat = input("1-primi piatti\n2-bevande\n: ")
    if cat == "1":
        print(primi_piatti.keys())
        nome_piatto = input("nome piatto: ")
        if nome_piatto in primi_piatti:
            totale.append(primi_piatti[nome_piatto])
    else:
        print(bevande.keys())
        bevanda = input("nome bevanda: ")
        if bevanda in bevande:
            totale.append(bevande[bevanda])

print(f"Totale da pagare: €{sum(totale)}")