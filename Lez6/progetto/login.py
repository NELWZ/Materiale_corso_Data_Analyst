import database as db


def login():
    print("=== LOGIN ===")
    username = input("Username: ").strip().capitalize()
    password = input("Password: ")
    
    if username not in db.utenti:
        print("ERRORE: Credenziali non valide")
    else:
        dati = db.utenti[username]
        if not dati['attivo']: 
            print("SEI STATO DISATTIVATO")
        elif dati['password'] == password:
            print("LOGIN RIUSCITO")
        else:
            print("CREDENZIALI NON VALIDE")
