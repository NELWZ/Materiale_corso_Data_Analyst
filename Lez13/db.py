import mysql.connector as msc

DB_NAME = "auth_system"
CONFIG = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'charset': 'utf8mb4',
}

def get_connection(with_db: bool = True):
    cfg = CONFIG.copy()
    if with_db:
        cfg['database'] = DB_NAME
    return msc.connect(**cfg)

def esegui(query: str, params: tuple=(), fetch: str=None):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    
    cur.execute(query, params)
    
    if fetch == "one": 
        risultato = cur.fetchone()
    elif fetch == "all":
        risultato = cur.fetchall()
    else:
        conn.commit()
        risultato = cur.lastrowid
    
    cur.close()
    conn.close()
    return risultato













