# === LOGIN === #
# DENTRO AL NOSTRO DATABASE SALVATI 
email_db = "mariorossi@gmail.com"
password_db = "mario123"

# DATI DI ACCESSO 
email_utente = input("Inserisci la tua email: ")
password_utente = input("inserisci la tua password: ")

# SE email_utente è identica alla email_db
if email_utente == email_db:
    if password_utente == password_db:
        print("login riuscito")
    else:
        print("login fallito")
else:
    print("login fallito")
