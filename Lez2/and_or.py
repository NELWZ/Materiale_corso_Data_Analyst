'''
or → altrimenti | o
and → e | oppure
'''

voto = 7

# SE il voto è maggiore di 6 e minore di 8: buono → RANGE
if voto >= 6 and voto < 8:
    print('buono')

if voto >= 6:
    if voto < 8:
        print("buono")

nome = "Marco"

if nome == "Marco" or nome == "Luca" or nome == "Sarah":
    print("VIP")

else:
    print("Non sei VIP")

