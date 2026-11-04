# variabile di nome "semaforo" con un valore colore
semaforo = 'ciao'

# SE la variabile "semaforo" ha un valore identico a "rosso"
if semaforo == "rosso":
    # stampo "FERMO"
    print('FERMO')

# ALTRIMENTI SE la variabile "semaforo" ha un valore identico al "giallo"
elif semaforo == "giallo":
    # stampo "Attento"
    print("Attento")

# ALTRIMENTI SE la variabile "semaforo" ha un valore identico al "verde"
elif semaforo == "verde":
    # stampo "Puoi passare"
    print("Puoi passare")

# ALTRIMENTI → Qualsiasi valore abbia la variabile "semaforo" che non sia "rosso, giallo o verde"
else:
    # stampo "Colore non valido"
    print("Colore non valido")

