import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1", port=3306,
    user="root", password=""
)
cur = conn.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS scuola")

