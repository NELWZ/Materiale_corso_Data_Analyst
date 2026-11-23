import pandas as pd
import matplotlib.pyplot as plt

file = "Lez15/vendite.csv"

df = pd.read_csv(file)

mesi = df['Mese']
vendite = df['Vendite']


media_vendite = vendite.mean()

plt.figure(figsize=(10, 5))

# barre
plt.bar(mesi, vendite, color="skyblue", edgecolor="black")

# linea
plt.axhline(media_vendite, color="purple", linestyle='--', label=f"Media: {round(media_vendite, 0)}")

plt.title("Vendite Mensili | Gen-Giu", fontsize=25)
plt.xlabel("Mesi", fontsize=22)
plt.ylabel('Vendite', fontsize=22)

plt.legend()
plt.grid(axis='y', linestyle="--")
plt.savefig("grafico")
plt.show()


