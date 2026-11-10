database = []

persona1 = {
    'id': 1,
    'nome': 'Mario',
    'cognome': 'Rossi',
    'eta': 30,
    'citta': 'Roma',
    'studi': {'scuola_media': 9, 'scuola_sup': 95, 'inglese': 'C2'}
}

database.append(persona1)


persona2 = {
    'id': 2,
    'nome': 'Luca',
    'cognome': 'Verde',
    'eta': 26,
    'citta': 'Torino'
}

database.append(persona2)

for u in database:
    pass#print(u)

print(database[0])
nome = database[0]['nome']
print(nome)


studi = database[0]['studi']
print(studi)

inglese = database[0]['studi']['inglese']
print(inglese)


db = {'dati_utente': [1,2,3,[1,2,[5,6,9,8,[8,5,2,[['dato']]]],],4]}


print(db)

chiave = db['dati_utente']
print(chiave)

i3 = db['dati_utente'][3]
print(i3)
i2d3 = db['dati_utente'][3][2][4][3][0][0]
print(i2d3)


d = {'k1': False, 'k2':[], 'k3':5, 'k4':'ciao', 'k5':{}}

d['k1'] = True
if d['k1']:
    pass

d['k2'].append("ciao")
d['k2'].insert(0, 'panino')
d['k2'].clear()
if "panino" in d['k2']:
    pass

d['k3'] += 5
d['k3'] -= 2

if d['k3'] > 5:
    pass


