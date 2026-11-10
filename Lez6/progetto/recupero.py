import database as db

def recupera():
    print("=== RECUPERO PASSWORD ===")
    nome = input("Username: ").strip().capitalize()
    
    if nome not in db.utenti:
        print("ERRORE: utente non trovato")
    else:
        dati = db.utenti[nome]
        
        if not dati['attivo']:
            print("ERRORE: account disattivato")
        else:
            print(f"DOMANDA DI SICUREZZA\n{dati['domanda']}")
            risposta = input("Risposta: ")
            if risposta == dati['risposta']:
                nuova_p = input("Crea un nuova password: ")
                if len(nuova_p) < 8:
                    print(f"ERRORE: Password è troppo corta, hai inserito {len(nuova_p)}/8 minimo")
                else:
                    conf_nuova_p = input("Conferma password: ")
                    if conf_nuova_p == nuova_p:
                        dati['password'] = nuova_p
                        print("Password modificata")
                    else:
                        print("Le password non coincidono")
            else:
                print("ERRORE: Risposta sbagliata")
