# pip install mysql-connector-python
# python -m pip install mysql-connector-python

import mysql.connector as msc

conn = msc.connect(
    user="root",
    password="",
    host="localhost",
    database="utenti"
)

verifica = conn.is_connected()
if verifica:
    print("Tutto OK")

# CREIAMO UN CIRSORE DENTRO IL NOSTRO DATABASE
cursore = conn.cursor()

# === CREA DATABASE === #
def crea_db(nome_db):
    cursore.execute(f"CREATE DATABASE IF NOT EXISTS {nome_db}")
    print(f"DB Creato {nome_db}")
    
# crea_db("utenti")


def elimina_db(nome_db):
    cursore.execute(f"DROP DATABASE IF EXISTS {nome_db}")
    print(f"Database {nome_db} eliminato")

# elimina_db("utenti")

def mostra_db():
    cursore.execute("SHOW DATABASES")
    for  (db, ) in cursore:
        print(db)

def crea_tab():
    cursore.execute("""
            CREATE TABLE IF NOT EXISTS persone (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(50) NOT NULL,
                cognome VARCHAR(50) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE,
                anni INT,
                creato_il TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)
    conn.commit()

# crea_tab()


def insert_tab(nome, cognome, email, anni):
    sql = "INSERT INTO persone (nome, cognome, email, anni) VALUES (%s, %s, %s, %s)"
    valori = (nome, cognome, email, anni)
    
    cursore.execute(sql, valori)
    conn.commit()

# insert_tab('Marco', 'Falco', 'marcofalco@gmail.com', 26)
# insert_tab('Sarah', 'Verdi', 'verdisarah@gmail.com', 20)
# insert_tab('Luca', 'Grigi', 'grigiluca@gmail.com', 35)
# insert_tab('Alessia', 'Ricca', 'riccaalessia@gmail.com', 32)

def insert_many():
    sql = "INSERT INTO persone (nome, cognome, email, anni) VALUES (%s, %s, %s, %s)"
    dati = [
        ('Luigi', 'Alber', 'alberluigi@gmail.com', 20),
        ('Antonio', 'Gres', 'gresantonio@gmail.com', 39),
        ('Aurora', 'Pangocciola', 'pangocciolaurora@gmail.com', 42),
    ]
    cursore.executemany(sql, dati)
    conn.commit()

# insert_many()

def leggere_utenti():
    cursore.execute('SELECT * FROM persone')
    for (i, n, c, e, a, t) in cursore:
        print(f"Nome: {n}")
        print(f"Cognome: {c}")
        print(f"Email {e}")
        print(f"Anni: {a}")
        print("▄" * 60)

# leggere_utenti()

# === UPDATE === #
def aggiorna_dati(tab, dato, cond, val):
    sql = f"UPDATE {tab} SET {dato} = %s WHERE {cond} = %s"
    valori = val
    cursore.execute(sql, val)
    conn.commit()

aggiorna_dati('persone', 'email', 'id', ('newemail@gmail.com', 6))
aggiorna_dati('persone', 'cognome', 'anni', ('new_cognome', 21))