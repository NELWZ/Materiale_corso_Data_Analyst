#& === WITH OPEN ===
'''
#? === MANIPOLAZIONE DEI FILE ===
#! CREARE UN FILE
↓
x → CREA UN FILE | SE IL FILE ESISTE ► ERRORE
↓
with open('nome_file.txt', 'x') as variabile:
    pass

#^ SCRIVERE DENTRO UN FILE
↓
w → SE IL FILE NON ESISTE | LO CREA E POI CI SCRIVE DENTRO
↓
SE IL FILE ESISTE | SCRIVE DENTRO
↓
w = WRITE AND OVERWRITE → SCRIVI E SOVRASCRIVI TUTTO
↓
with open("nome_file.txt", "w") as varibile:
    variabile.write("CONTENUTO CHE DEVE ESSERE UNA STRINGA")

#^ SCRIVERE DENTRO UN FILE
a → SE IL FILE NON ESISTE | LO CREA E SCRIVE DENTRO 
↓
SE IL FILE ESISTE → AGGIUNGE IL CONTENUTO ALLA FINE
↓
with open("nome_file.txt", "a") as variabile:
    variabile.write("contenuto dentro il file")

#^ LETTURA DEL FILE
r → READ ► LEGGI IL CONTENUTO DEL FILE
↓
SE IL FILE NON ESISTE = ERRORE
↓
with open("nome_file.txt", "r") as variabile:
    variabile.read() 
'''

