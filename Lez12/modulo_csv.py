# pip install python-csv
import csv

with open("vendite.csv", 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for riga in reader:
        print(riga)
    

print("=" * 60)
# LEGGERE I FILE COME DIZIONARI
with open("vendite.csv", 'r', encoding='utf-8') as f:
    reader= csv.DictReader(f)
    for riga in reader:
        print(f"{riga['citta']} ► {riga['prezzo']}")
        
print("=" * 60)


righe = [
    {'data':  '2024-01-01', 'città': 'Milano', 'totale': 100.85},
    {'data':  '2024-01-02', 'città': 'Roma', 'totale': 45.00}
]

with open('file.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['data', 'città', 'totale'])
    writer.writeheader()
    writer.writerows(righe)
