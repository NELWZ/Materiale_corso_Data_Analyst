'''
conta quante lettere "a" ci sono in una parola o frase
'''
parola = "PANDA".lower()

'devo salvare dentro qualcosa il totale delle lettere'
contatore = 0

'devo sapere la lunghezza della mia parola'
len(parola)

for l in parola:
    if l == "a":
        contatore += 1
print(contatore)




