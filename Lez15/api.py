# === REQUESTS === #
"Cos'è un API"
'''
Immagina un ristorante: Tu sei il "CLIENTE", la cucina è il server con tutti i dati.
per prendere i dati tu non entri in cucina: chiami il cameriere e ordini a lui i piatti da portare
lui: va in cuna (server) fa una richiesta (chiede se i piatti esistono)
se si può ti porta il piatto.
'''
from utili import *
import requests as cameriere

# cucina
piatto = "https://randomuser.me/api"

for i in range(5):
    ordine = cameriere.get(piatto)

    # STATUS CODE
    'NO = 404'
    'SI = 200'

    sato = ordine.status_code
    print(ordine)

    dati = ordine.json()
    # print(dati)
    s()

    ris = dati['results'][0]['name']['first']
    print(ris)
    s()

    info = dati['info']
    # print(info)


