# === LISTA === #
# 'Una lista può contenere QUALSIASI TIPO DI DATO'
lista_vuota = []
  
lista_str = ['A','B','C','D','E','F','G']
  
lista_num = [1,2,3.14,4,0.5,1.65,7,8,9]
  
lista_mix = [True, lista_num, [5,8,7], 'panda', False, 2+2, {}, int(), print()]


nome = "Celeste" # → VARIABILE
nomi = ['Celeste', 'Marco', 'Luca', 'Giulia', 'Pietro'] # → LISTA

# ===================================================================== #

frutta = ['kiwi', 'mela', 'anguria', 'uva']
print(frutta)

# === AGGIUNGERE I DATI === #

# append() → dove.append(dato)

frutta.append("pesca")
print(frutta)

# insert() → dove.insert(index, dato)

frutta.insert(2, "pera")
print(frutta)

# === RIMUOVERE I DATI === #
# remove() → da_dove.remove(dato)

frutta.remove("anguria")
print(frutta)

# pop() → da_dove.pop() | da_dove.pop(index)

frutta.pop()
print(frutta)

frutta.pop(1)
print(frutta)

# === ELIMINARE I DATI === #
frutta.clear()

print()
print('▄' * 60)
print()

# ===================================================================== #
# indici 0    1    2    3    4    5    6    7
dati = ['D1','D2','D3','D4','D5','D6','D7','D8']
#       -8   -7   -6   -5   -4   -3   -2   -1
print(dati)

print()
print('▄' * 60)
print()


# dove[indice]
print(dati[5])

# dove[-indice]
print(dati[-7])


# ===================================================================== #

# SLICING #
#        0    1    2    3    4    5    6    7
dati = ['D1','D2','D3','D4','D5','D6','D7','D8']
#       -8   -7   -6   -5   -4   -3   -2   -1

print(dati[2:5])

# === LEN === #
print(len('ciao'))
print(len(dati))

print("▄" * 60)
indice = 0
while True:
  d = dati[indice]
  print(d)
  indice += 1

  if indice >= len(dati):
    break


