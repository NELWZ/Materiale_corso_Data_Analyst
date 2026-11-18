# ===================================== #
'Async non è "Python più veloce"'
'è solo un modo per dire a python "mentre aspetti una funzione fai altro"'
import asyncio
import time
from random import randint as r

async def chiama_apia(nome):
    print(f"inizio {nome}")
    await asyncio.sleep(5)
    print(f"finito {nome}")
    return f"dati_{nome}"

async def chiama_apib(nome):
    print(f"inizio {nome}")
    await asyncio.sleep(6)
    print(f"finito {nome}")
    return f"dati_{nome}"

async def chiama_apic(nome):
    print(f"inizio {nome}")
    await asyncio.sleep(2)
    print(f"finito {nome}")
    return f"dati_{nome}"


async def main():
    inizio = time.time()
    await asyncio.gather(
        chiama_apia('A'),
        chiama_apib('B'),
        chiama_apic('C'),
    )

    print(f"Tempo totale: {time.time() - inizio:.1f}s")

asyncio.run(main())









