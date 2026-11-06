import time, os

ore = int(input("ore: "))
minuti = int(input("minuti: "))
secondi = int(input("secondi: "))

while True:
    if ore == minuti == secondi == 0: 
        print("=== TEMPO SCADUTO ===")
        break
    
    if secondi >= 0:
        if secondi > 0:
            secondi -= 1
        
        if secondi == 0 and minuti >= 0:
            if minuti > 0:
                minuti -= 1
                secondi = 59
        
            if minuti == 0 and ore >= 0:
                if ore > 0:
                    ore -= 1
                    minuti = 59
    print("=== SIAMO IN PAUSA ===")
    print(f"{ore}:{minuti}:{secondi}")
    time.sleep(1)
    os.system("cls")