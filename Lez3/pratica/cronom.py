import time

secondi = 0
minuti = 0
ore = 0

# === ciclo infinito === #
while True:
    secondi += 1
    if secondi >= 60:
        secondi = 0
        minuti += 1
    if minuti >= 60:
        minuti = 0
        ore += 1
    
    print(f"{ore}:{minuti}:{secondi}")
    time.sleep(1)




