# pip install python-dotenv
# python -m pip install python-dotenv

import os
from dotenv import load_dotenv

# NON protegge le credenziali 
'ISOLA i pachetti'

'il modulo venv: crea un ambiente virtuale per isolare le librerie Python di un progetto'

load_dotenv() # legge il file .env e carica le variabili

db_password = os.getenv("DB_PASSWORD")

print("fatto")
print(db_password)

db_password = "DB_PASSWORD"
print(db_password)

