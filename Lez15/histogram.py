import matplotlib.pyplot as plt
import random

def colors(x=10):
    colori = ["#7a0d0d","#37ce20","#e6af19","#211cc1","#c127ac","#04596c"]
    lista = []
    for _ in range(x):
        lista.append(random.choice(colori))
    return lista

colori = colors(100)

voti = [random.randint(1, 10) for _ in range(100)]
plt.legend()
plt.grid()
plt.hist(voti,color='blue', density=True, orientation="horizontal", label="testo", align="left")

plt.show()