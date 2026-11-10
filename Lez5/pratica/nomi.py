from random import choice as c
from random import randint as r

nomi = ['Marco','Giulia',
        'Luca','Pietro',
        'Alessia','Martina',
        'Giovanni','Andrea',
        'Celeste','Roy']

cognomi = ['Rossi','Gilbert',
        'Falco','Grizl',
        'Lawrence','Kotila',
        'Camacho','Kienzle',
        'Martínez','Jensen']

anni = []
for i in range(10):
    anni.append(r(20, 60))

for i in range(5):
    presenta = f"Mi chiamo {c(nomi)} {c(cognomi)} ho {c(anni)} anni"
    print(presenta)
