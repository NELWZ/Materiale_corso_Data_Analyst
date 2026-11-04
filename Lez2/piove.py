print("Tu: posso uscire fuori?")
print("Mamma: fuori piove?")

risposta1 = 'si'

if risposta1 == 'si':
    print("Mamma: hai l'ombrello?")
    risposta2 = 'no'
    
    if risposta2 == "si":
        print("Mamma: esci")
    elif risposta2 == "no":
        print("Mamma: stai a casa")
    else:
        print("Non ho capito")
    
if risposta1 == 'no':
    print("Mamma: esci")

else:
    print("Mamma: non ho capito")