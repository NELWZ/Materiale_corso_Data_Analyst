import os

USERS_FILE = "./Lez8/project/users.txt"

#! VARIABILI GLOBALI 
utenti = {}
esito = False
messaggio = ""

def carica_utenti():
    global utenti
    # reset dizionario per sicurezza
    utenti = {}
    
    #WARN crea il file pronto a scrivere
    with open(USERS_FILE, "a") as f:
        pass # non scriviamo nulla
        
    
    #? legge tutto il contenuto
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        contenuto = f.read()
    
    #^ righe del file → variabile appena creata
    righe = contenuto.split("\n")
    
    i = 0
    while i < len(righe):
        riga = righe[i].strip()
        #! SE la riga presa è diversa dal nulla
        if riga != "": 
            parti = riga.split("|")
        i = i + 1 # i += 1
    
def salva_utente(username, password):
    with open(USERS_FILE, 'a') as f:
        f.write(username + "|" + password + "\n")
        #f.write(f"{username}|{password}\n")

def stampa_utenti():
    carica_utenti()
    if not utenti:
        print("Nessun utente nel database")
    else:
        print("=== UTENTI ===")
        for u in utenti:
            print(f"• {u}")
    
