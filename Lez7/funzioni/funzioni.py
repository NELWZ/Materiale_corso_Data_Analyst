#! === FUNZIONI === !#
'La funzione è un blocco di codice che puoi usare e ri-usare'
#? NON TI RIPETERE ?#

databases = ['dati']

def crea_db():
    nome_database = input("nome_db: ")

    if nome_database in databases:
        print("nome non valido")
    else:
        databases.append(nome_database)
    print(databases)