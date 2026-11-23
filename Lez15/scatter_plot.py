import matplotlib.pyplot as plt
import random

def num(x=10):
    lista = []
    for n in range(x):
        lista.append(random.randint(100, 500))
    return lista

altezze = num(50)
pesi = num(50)


def colors(x=10):
    colori = ["#7a0d0d","#37ce20","#e6af19","#211cc1","#c127ac","#04596c"]
    lista = []
    for _ in range(x):
        lista.append(random.choice(colori))
    return lista

colorandom = colors(50)
print(colorandom)

plt.scatter(altezze, pesi, s=100, c=colorandom)
plt.show()


