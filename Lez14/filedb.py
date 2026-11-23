# BLOB = (Binary Large Object)
'''
1-crea una connection al database
2-crea un database
3-usa il tuo dabase
4-dento il database crea una tabella ↓

CREATE TABLE imnagini (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    foto_profilo BLOB
)
'''

# import _mysql_connector as msc

# connection 

# cursor

'LEGGERE IL FILE IN BINARIO'

with open('foto.png', 'rb') as f:
    dati_binari = f.read()


'cursore.execute ("INSERT INTO imnagini (nome, foto_profilo) VALUES (%s, %s)", ("Marco", dat_binari))'

'conn.commit()'

# === SCARICARE UN  FILE DAL DATABASE === #

'cursore.execute("SELECT nome, foto_profilo FROM immagini WHERE id=%s", (1,))'
'risultato = cursore.techone()'

'''
if risultato:
    nome, foto_profilo = rilsultato
    with open(f'foto_{nome}', 'wb') as f:
        f.write(foto_profilo)
else:
    print('foto non esiste')
'''


