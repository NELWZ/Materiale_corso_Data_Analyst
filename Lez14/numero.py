import random

with open("punti.txt", 'a') as f:
    pass

punti = 0
#  load
with open("punti.txt", 'r') as f:
    c = f.read()
    if c:
        punti = int(c)
        
def mat():
    global punti
    numero1 = random.randint(1, 10)
    numero2 = random.randint(1, 10)

    somma = numero1 + numero2

    ris = int(input(f"{numero1} + {numero2} = "))

    if ris == somma:
        print("Hai vinto")
        punti += 1
    else:
        print(f"no, fa {somma}")
    print(f"punti: {punti}")
    with open("punti.txt", 'w') as f: f.write(str(punti))
    
    ripr = input("ti va un'altra partita?\n: ")
    if ripr == "no":
        return
    else:
        mat()
    
mat()