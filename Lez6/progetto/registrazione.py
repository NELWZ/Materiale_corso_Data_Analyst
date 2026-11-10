import database as db

def registra():
    print("=== REGISTRAZIONE ===")
    username = input("Scegli username: ").strip().capitalize()
    
    if len(username) < 3:
        print("ERRORE: lunghezza non valida")
    elif username in db.utenti:
        print("Nome utente già esiste")
    else:
        password = input("Crea una password: ")
        if len(password) < 8:
            print("Minimo 8 caratteri")
        else:
            conferma_password = input("Conferma password: ")
            if conferma_password != password:
                print("Errore: Le password sono diverse")
            else:
                email = input('Email: ').strip().lower()
                if "@" not in email or "." not in email:
                    print("Errore: Email non valida")
                else:
                    domanda = input("SCEGLI UNA DOMANDA DI SICUREZZA\n: ").strip().lower()
                    risposta = input("Risposta: ").strip().lower()
                    db.utenti[username] = {
                        'password': password,
                        'email': email,
                        'domanda': domanda,
                        'risposta': risposta,
                        'attivo': True
                    }
                    print("REGISTRAZIONE COMPLETATA")
                    print(f"Utenti totali: {len(db.utenti)}")
                
            
        
    