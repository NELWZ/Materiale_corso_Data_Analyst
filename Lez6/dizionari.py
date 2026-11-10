# === DIZIONARI === #
dizionario = {}
'diz = {chiave: valore, key: value}'

info = {
    'palla': 'qualcosa che rimbalza',
    'matita': 'serve per disegnare',
    'cane': 'animale domestico',
    'gatto': 'il re del mondo che ti giudica male'
}

g = info['gatto']
# print(g)

gatto = 'il re del mondo che ti giudica male'

# ================================================================== #

# === AGGIUNGERE I DATI === #
'se esiste si aggiorna, se non esiste viene creato'

dati = {
    'nome': 'Celeste', 
    'cognome': 'Rossi', 
    'anni': 25
    }

print(dati)
# dove[chiave] = valore

dati['animale'] = "cane"
print(dati)

dati['cognome'] = "Verdi"
print(dati)

# === ELIMINARE I DATI === #
'del da_dove[chiave]'

del dati['animale']
print(dati)

# === CHIAVI === #
chiavi = dati.keys()
print(chiavi)

# === VALORI === #
valori = dati.values()
print(valori)

print("_" * 60)
for chiave, valore in dati.items():
    print(f"Chiave: {chiave} - Valore: {valore}")
