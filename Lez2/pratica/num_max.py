'''
crea una variabile "nome" assegna un valore stringa (" ')
verifica se il nome è "Marta"
stampa che è VIP
altrimenti stampa che non è VIP
'''
# === CODICE === #
#katia
# creiamo una variabile "nome" le diamo un valore str
nome = "Andrea"

# SE la variabile "nome" ha un valore identico a "Katia"
if nome == "Katia":
    # stampiamo "VIP"
    print(f"{nome} VIP")

# ALTRIMENTI SE la variabile "nome" ha un valore identico a "Luca"
elif nome == "Luca":
    # stampiamo "VIP"
    print(f"{nome} VIP")

# ALTRIMENTI → QUALSIASI valore al di fuori di "Katia" e "Luca"
else:
    # stampiamo non è VIP
    print(f"{nome} non è VIP")

