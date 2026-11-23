import mysql.connector as msc

conn = msc.connect(
    user="root",
    password="yTHYVltTJOFVOqwlVLkBLEkCvbaitPxJ",
    host="gondola.proxy.rlwy.net",
    port=43587,
    charset="utf8mb4",
    connection_timeout=15
)
print(conn.is_connected())

cur = conn.cursor()

def mostra_db():
    cur.execute("SHOW DATABASES")

    for d in cur:
        print(d)

def crea_db():
    cur.execute("CREATE DATABASE IF NOT EXISTS test")

mostra_db()