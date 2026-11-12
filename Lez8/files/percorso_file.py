#^ === PERCORSI FILE === #
percorso = "C:/percorso/del/tuo/file.txt"
file = "C:\\percorso\\del\\tuo\\file.txt"

locale = "C:/Users/avare/Desktop/Python"
percorso_globale ="./Lez8/files/ricordo.py"

pg = percorso_globale

with open(pg, 'r') as f:
    codice = f.read()

print(codice)