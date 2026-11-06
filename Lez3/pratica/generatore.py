import random
import time

tentativi = 0
while True:
    time.sleep(0.01)
    numero = random.randint(1, 1000)
    tentativi += 1
    print(numero)
    if numero == 500:
        print(f"indovinato in {tentativi} tentativi")
        break
