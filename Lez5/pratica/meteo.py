'''
Crea una lista con i giorni della settimana. 
Usa un ciclo for per scorrere i giorni. 
Per ogni giorno, genera casualmente 
("Sole", "Pioggia", "Nuvolo") usando 
random.choice(). Se piove per 3 giorni 
consecutivi, stampa un avviso "Allerta Maltempo!".
'''
import random as r

giorni = ['Lunedì','Martedì','Mercoledì','Giovedì','Venerdì','Sabato','Domenica']
meteo = ['Sole', 'Pioggia', 'Nuvoloso']

for g in range(len(giorni)):
    tempo = r.choice(meteo)
    print(f"{g}: {tempo}") 
