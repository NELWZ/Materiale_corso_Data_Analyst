# PRATICA #
'''
Scrivere un programma che dato una lista vuota chiamata "spesa"
possa fare: 1 aggiungere dati, rimuovere i dati, stampare i dati

-----------------------------------------------------
1-aggiungi
2-rimuovi
3-stampa

noi dobbiamo scegliere 1 | 2 | 3
se 1 → creiamo la logica per aggiungere i dati (append)
altrimenti se è 2 → creiamo la logica per rimuovere i dati (remove)
altrimenti → creiamo la logica per stampare i dati (print)

'''
# VARIABILE DELLA LISTA
spesa = []

# CICLO WHILE TRUE
while True:
  # INPUT → PER input("1-aggiungi | 2-rimuovi | 3-stampa: ")
  scelta = input("1-Aggiungi\n2-Rimuovi\n3-Mostra\n: ")
  # CONDIZIONI → if scelta == 1
  if scelta == "1":
    prodotto = input("nome prodotto da aggiungere: ")
    if prodotto in spesa:
      print(f'Prodotto "{prodotto}" è già presente nella lista. Continuare?')
      if input("s/n: ") == "s":
        spesa.append(prodotto)
        print(f'"{prodotto}" aggiunto!')
    else:
        spesa.append(prodotto)
        print(f'"{prodotto}" aggiunto!')
      
    
  elif scelta == "2":
    prodotto = input("nome prodotto da rimuovere: ")
    if prodotto in spesa:
      spesa.remove(prodotto)    
  elif scelta == "3":
    print(spesa)
  else:
    print("scelta non valida")
















