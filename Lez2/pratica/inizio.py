# COSA CREARE?
'Si parte SEMPRE da una variabile'
nome = 'Sarah'
cognome = "Rossi"
eta = 25
patente = False

print(f"Ciao, mi chiamo {nome} {cognome}, ho {eta} anni, domani faccio {eta+1} anni")
print(f"{nome}{cognome}.{eta}@gmail.com")

if eta >= 18 and not patente:
    print(f"{nome} puo prendere la patente")
