import sys
import os
import subprocess

from auth import *
from setup_db import *
from utili import *
from time import sleep

actions = [
        'Registrati',
        'Login',
        'Reset Password',
        'Cambia Password',
        'Pulisci Token',
        'Esci']

can_choose = True

def menu():
    global can_choose
    if can_choose:
        can_choose = True
        tst('menu')
        for i in range(len(actions)):
            print(f"{i+1} - {actions[i]}")
            sleep(0.2)

def  chiedi(prompt: str):
    sleep(0.2)
    return input(prompt).strip()

def main():
    global can_choose
    utente_loggato = None
    
    while True:
        
        menu()
        if can_choose:
            scelta = chiedi("Scelta: ")
        if scelta == 'reset': reset_all()
        elif scelta == "set": setup()
        elif scelta in ['cls','clear','c']:
            comando = ["cmd", "/c", "cls"] if os.name == "nt" else ["clear"]
            subprocess.run(comando, check=False)
            
        elif scelta == "1":
            can_choose = True
            tst('registrazione')
            u = chiedi("Username: ")
            e = chiedi('Email: ')
            password = chiedi("Password: ")
            r = registra(username=u, email=e, password=password)
            if r['ok']: 
                sleep(0.2)
                print(f"Registrato ID: {r['id']}")
            else:
                print(r['errore'])
        elif scelta == "2":
            can_choose = True
            tst("login")
            u = chiedi("Username: ")
            password = chiedi("Password: ")
            r = login(username=u, password=password)
            if r['ok']:
                utente_loggato = r['utente']
                sleep(0.2)
                print(f"Login riuescito.\nBello averti di nuovo {utente_loggato['username']}")
            else:
                sleep(0.2)
                print(f"{r['errore']}")
                can_choose = False
                scelta = "1"
                
        elif scelta == "3":
            tst("recupero password")
            e = chiedi("Email: ")
            r = genera_token_recupero(e)
            if not r['ok']:
                sleep(0.2)
                print(r['errore'])
                continue
            
            if 'token' in r:
                sleep(0.2)
                print(f'Token: {r['token']}')
                sleep(0.2)
                print(f"SCADE IL: {r['scade']}")
                sleep(0.2)
                print('controlla la tua email')
            else:
                sleep(0.2)
                print(r['messaggio'])
            
            token = chiedi("Inserisci il token ricevuto: ")
            nuova = chiedi('Nuova Password: ')
            r2 = reset_password(token=token, nuova_password=nuova)
            if r2['ok']:
                sleep(0.2)
                print(r2['messaggio'])
            else:
                print(r2['errore'])
        elif scelta == "4":
            if not utente_loggato:
                sleep(0.2)
                print("non sei loggato")
                can_choose = False
                scelta = "2"
                continue
            tst("cambio password")
            vecchia = chiedi("vecchia password: ")
            nuova = chiedi("nuova password: ")
            r = cambia_password(utente_loggato['username'], vecchia, nuova)
            if r['ok']:
                sleep(0.2)
                print(r['messaggio'])
            else:
                sleep(0.2)
                print(r['errore'])
        
        elif scelta == "5":
            n = pulisci_token_scaduti()
            sleep(0.2)
            print(f"Rimossi {n} token scaduti")
        elif scelta == "6":
            return sys.exit(0)
        else:
            tst('scelta non valida')

if __name__ == '__main__':
    main()





