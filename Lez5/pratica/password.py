import random as r
stringa = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789|\\!£$%&/()=?^-.,;:@é*#/*+{}[]"


lung = int(input("lung password: "))
quant = int(input("quantità: "))

for q in range(quant):
    for i in range(lung):
        print(r.choice(stringa), end="")
    print()

