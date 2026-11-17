# === PANDAS & VENV RIPASSO === 
'VENV =► Virtual Enviroment'

'Apri il terminale (dentro la nostra cartella)'

# WINDOWS
'python -m venv .nome_venv'

# MAC & LINUX
'python3 -m venv .nome_venv'

# ========================================== #
'PIP INSTALL =► Serve per installare i moduli esterni'

# WINDOWS
'pip install nome-modulo'

# MAC & LINUX
'pip3 install nome-modulo'

# SE PIP NON FUNZIONA

# WINDOWS
'python -m pip install nome-modulo'

# MAC & LINUX
'python3 -m pip install nome-modulo'


# ========================================== #

'PANDAS & FILE CSV'
'import pandas as pd'

# COSA VUOI FARE        COMANDO
'''
• Aprire CSV                        pd.read_csv("file.csv")
• Vedere la Tabella             df.head() | df.head(n=numero)
• Vedere la Coda                df.tail() | df.tail(n=numero)
• Vedere Tipi                       df.dtypes
• Vedere NaN                      df.isnull()
• Contare NaN                    df.isnull().sum()
• Colonne                           df.columns
'''





