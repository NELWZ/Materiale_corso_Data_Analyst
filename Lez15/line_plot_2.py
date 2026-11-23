import matplotlib.pyplot as plt

x = [1,5,6,8,9]
y = [4,2,1,5,2]
z = [7,5,3,6,5]
plt.plot(x, y, label="Cose", color="green",  marker='o')
plt.plot(x, z, label="Altro", color="purple", linewidth=15)
plt.plot(y, x, label="Non so", color="black")

plt.legend()
plt.show()

