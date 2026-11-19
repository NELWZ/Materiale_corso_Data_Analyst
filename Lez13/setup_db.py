import mysql.connector as msc

DB_NAME = 'auth_system'

def setup():
    conn = msc.connect(
        user="root",
        password="",
        host="localhost",
        charset="utf8mb4"
    )
    # creiamo un cursore
    cur = conn.cursor()
    
    # === CREIAMO UN DATABASE SE NON ESISTE ===
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} CHARACTER SET utf8mb4")
    
    # === USIAMO IL DATABASE NELLA conn ===
    # metodo II
    cur.execute(f'USE {DB_NAME}')

    # === CREIAMO LA TABELLA utenti ===
    cur.execute("""
                CREATE TABLE IF NOT EXISTS utenti (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(0) NOT NULL UNIQUE,
                    email VARCHAR(120) NOT NULL UNIQUE,
                    password_hash VARCHAR(255) NOT NULL,
                    creato_il TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """)
    
    cur.execute("""
                CREATE TABLE IF NOT EXISTS reset_tokens (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    utente_id INT NOT NULL,
                    token VARCHAR(64) NOT NULL UNIQUE,
                    scade_il TIMESTAMP NOT NULL,
                    usato BOOLEAN DEFAULT FALSE,
                    FOREIGN KEY (utente_id) REFERENCES utenti(id) ON DELETE CASCADE
                )
                """)
        
    conn.commit()
    cur.close()
    conn.close()
    print("Tutto fatto!")

def reset_all():
    # ELIMINIAMO TUTTI I DATI
    conn = msc.connect(user='root', password='', host='localhost')
    cur = conn.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {DB_NAME}")
    print(f"Database {DB_NAME} è stato distrutto")
    conn.commit()
    cur.close()
    conn.close()

