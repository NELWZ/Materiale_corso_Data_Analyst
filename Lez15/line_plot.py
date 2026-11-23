# pip install matplotlib
# python pip install matplotlib
# pip3 install matplotlib

import matplotlib.pyplot as plt

x = [4,3,2,1]
y = [4,5,3,2]

plt.title("GRAFICO A LINEE")
plt.xlabel("Info X")
plt.ylabel("Info Y")
plt.grid(color="purple")
plt.plot(x, y, color="green")
plt.show()


