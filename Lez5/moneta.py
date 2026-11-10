from random import choice as c

scelte = ['testa', 'croce']
moneta = c(scelte)

lancio = moneta

indovina = input("testa o croce: ")
print(moneta)

if indovina == lancio:
    print("Hai vinto")
else:
    print("Hai perso")

# =================================================== #

moneta = c(['testa', 'croce'])

indovina = input("testa o croce: ")

if indovina == moneta:
    print("hai vinto")
else:
    print('hai perso')
    
# =================================================== #
if input("testa o croce: ") == c(['testa', 'croce']):
    print("hai vinto")
else:
    print("hai perso")

# =================================================== #
print("hai vinto") if input("testa o croce: ") == c(['testa', 'croce']) else print("hai perso")
