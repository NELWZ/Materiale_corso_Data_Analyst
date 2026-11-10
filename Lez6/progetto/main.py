import registrazione    # registrazione.py
import login            # login.py
import gestione         # gestione.py
import recupero         # recupero.py
import time

# ==================================================== #

while True:
    time.sleep(0.4)
    print("=== MENU PRINCIPALE ===")
    time.sleep(0.4)

    
    print("1-Registrazione")
    time.sleep(0.4)

    print("2-Login")
    time.sleep(0.4)

    print("3-Elenca Utenti")
    time.sleep(0.4)

    print("4-Cerca Utente")
    time.sleep(0.4)

    print("5-Disattiva Utente")
    time.sleep(0.4)

    print("6-Attiva Utente")
    time.sleep(0.4)

    print("7-Recupera Password")
    time.sleep(0.4)

    print("8-Esci")
    time.sleep(0.4)

    
    scelta = input(": ")
    
    if scelta == "1":
        registrazione.registra()
    elif scelta == "2":
        login.login()
    elif scelta == "3":
        gestione.elenca()
    elif scelta == "4":
        gestione.cerca()
    elif scelta == "5":
        gestione.disattiva()
    elif scelta == "6":
        gestione.attiva()
    elif scelta == "7":
        recupero.recupera()
    elif scelta == "8":
        break
    else:
        time.sleep(0.4)
        print("Scelta non valida")