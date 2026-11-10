import database  as db

def elenca():
    print("=== ELENCO UTENTI ===")
    print(f"Utenti totali: {len(db.utenti)}")
    for nome in db.utenti:
        dati = db.utenti[nome]
        if dati['attivo']:
            stato = "ATTIVO"
        else:
            stato = "DISATTIVATO"
        print(f"• {nome} | {dati['email']} | {stato}")

def cerca():
    print("=== CERCA UTENTE ===")
    nome = input("Username da cercare: ").strip().capitalize()
    if nome in db.utenti:
        dati = db.utenti[nome]
        print("TROVATO")
        print("_" * 40)
        print(f"Userame: {nome}")
        print(f"Email: {dati['email']}")
        print(f"Stato: {dati['attivo']}")
    else:
        print(f'Nessun utente trovato con il nome "{nome}"')

def disattiva():
    print("=== DISATTIVA UTENTE ===")
    nome = input("Username da disattivare: ").strip().capitalize()
    if nome in db.utenti and db.utenti[nome]['attivo']:
        db.utenti[nome]['attivo'] = False
        print(f'Utente "{nome}" disattivato')
    else:
        print(f'Utente "{nome}" non trovato')

def attiva():
    print("=== ATTIVA UTENTE ===")
    nome = input("Username da attivare: ").strip().capitalize()
    if nome in db.utenti and not db.utenti[nome]['attivo']:
        db.utenti[nome]['attivo'] = True
        print(f'Utente "{nome}" è stato attivato')
    else:
        print("ERRORE")
    
    