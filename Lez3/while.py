# === CICLO INFINITO WHILE === #
'FINO A QUANDO IO SONO TRUE: TI ESEGUO IL CODICE DENTRO DI ME'
'break → BLOCCA IL CICLO'
import random

contatore = 0
while True:
    numero_casuale = random.randint(1,999)
    print(numero_casuale)
    if contatore == 10:
        break
    contatore += 1



