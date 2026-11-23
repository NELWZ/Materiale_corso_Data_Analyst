import matplotlib.pyplot as plt

fette = [150 , 130, 165, 122]
etichette = ['Mela', 'Uva', 'Mandarino', 'Ananas']

plt.pie(fette, 
        labels=etichette, 
        autopct="%1.1f%%",
        colors=['yellow', 'green', 'purple', 'blue'],
        shadow=True,
        rotatelabels=False,
        startangle=85,
        explode=[0.12,0.12,0.12,0.12],
        labeldistance=0.5,
        radius=1.0,
        pctdistance=1.1
        )

plt.show()


