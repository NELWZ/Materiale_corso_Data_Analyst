# Le chiavi API non devono essere in chiaro
# pip install groq
file = "C:\\Users\\avare\\Desktop\\GRAPI.txt"

with open(file, 'r', encoding='utf-8') as f:
    api = f.read()

GROQ_API_KEY = api

MODEL = 'openai/gpt-oss-20b'

MAX_RIGHE_CSV = 50

