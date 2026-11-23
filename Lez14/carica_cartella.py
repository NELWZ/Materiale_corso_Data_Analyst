import mysql.connector as msc
import os

CARTELLA = 'Lez14/imgs'
ESTENSIONI = ('.jpg','.jpeg','.png','.gif','.webp','.bmp')

conn = msc.connect(user="root", password="", host="localhost", database="cartella")

cur = conn.cursor()

cur.execute("""
            create table if not exists immagini (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(50) NOT NULL UNIQUE,
                percorso_originale VARCHAR(500),
                dimensione INT,
                tipo VARCHAR(20),
                dati BLOB NOT NULL,
                caricata_il TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)
conn.commit()

file_immagini = [
    f for f in os.listdir(CARTELLA)
    if f.lower().endswith(ESTENSIONI)
    ]

print(file_immagini)

caricate = 0
saltate = 0

for nome_file in file_immagini:
    percorso = os.path.join(CARTELLA, nome_file)
    
    if not os.path.isfile(percorso):
        continue
    
    with open(percorso, 'rb') as f:
        dati = f.read()
        
    
    dimensione = len(dati)
    estensione = os.path.splitext(nome_file)[1].lower()

    # controlla se esiste già un immagine del db
    cur.execute("SELECT id FROM immagini WHERE nome=%s", (nome_file,))
    if cur.fetchone():
        print("immagine presente")
        saltate += 1
        continue

    # inseriamo i file
    cur.execute("""
                INSERT INT immagini (nome, percorso_originale, dimensione, tipo, dati)
                VALUES (%s,%s,%s,%s,%s)
                """,
                (nome_file, percorso, dimensione, estensione, dati)
                )
    caricate += 1
    
    conn.commit()
    