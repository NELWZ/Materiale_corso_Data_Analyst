import matplotlib.pyplot as plt

nomi = ['Celeste', 'Marco', 'Alessia', 'Luca', 'Aurora']
voti = [10, 6, 2, 4, 8]

plt.bar(nomi, voti, color=['#00bd32', '#de9f00', '#de3f00', '#de6f00', '#719600'], edgecolor="black", linewidth=5)

plt.show()

