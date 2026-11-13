def s(c="_", l=60):
    print(c * l)

s()
s('ciao', 5)
s('-', 20)
s('+', 100)
s('.', 1)
s('=', 51)
s(':', 26)
s('▄', 5)


import random

def dado(minimo=1, massimo=6):
    dado = random.randint(minimo, massimo)
    numero = int(input(f"idovina il numero da {minimo} a {massimo}: "))
    
    if dado == numero:
        print("Hai vinto")
    else:
        print(f'hai perso, il numero era {dado}')

# dado()
# dado(5, 10)
# dado(1, 20)
# dado(50, 100)

def crea_file(nome_file="file.txt", metodo="a", contenuto=""):
    with open(nome_file, metodo) as file:
        file.write(contenuto)


crea_file('mario.txt', 'a', 'ciao mario')
crea_file('luca.txt', 'w', 'ciao luca rossi')
crea_file()

def saluto():
    print('ciao celeste')

saluto()

def saluto2(nome):
    print(f"ciao {nome}")

saluto2("marco")
saluto2("luca")
saluto2("mario")