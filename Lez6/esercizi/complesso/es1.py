studenti = []

scelta = 0
while scelta != "5":
    print("1. Aggiungi studente")
    print("2. Report")
    print("3. Migliore")
    print("4. Cerca")
    print("5. Esci")
    scelta = input("Scelta: ")

    if scelta == "1":
        nome = input("Nome: ")
        eta = int(input("Età: "))
        voti = []
        n = int(input("Quanti voti? "))
        for i in range(n):
            v = float(input("Voto: "))
            voti.append(v)
        studente = {
            "nome": nome,
            "eta": eta,
            "voti": voti,
            "media": sum(voti) / len(voti)
        }
        studenti.append(studente)

    elif scelta == "2":
        if not studenti:
            print("Nessuno studente registrato.")
        else:
            i = 0
            while i < len(studenti):
                s = studenti[i]
                print(f"{s['nome']} ({s['eta']}) - media: {s['media']}")
                if s["media"] >= 8:
                    print("  Eccellente")
                elif 6 < s["media"] < 8:
                    print("  Buono")
                else:
                    print("  Da migliorare")
                i = i + 1

    elif scelta == "3":
        if not studenti:
            print("Nessuno studente registrato.")
        else:
            migliore = None
            media_max = float("-inf")
            for s in studenti:
                if s["media"] > media_max:
                    media_max = s["media"]
                    migliore = s
            print("Migliore:", migliore["nome"])

    elif scelta == "4":
        cercato = input("Nome da cercare: ")
        trovato = False
        for s in studenti:
            if s["nome"] == cercato:
                trovato = True
                break
        if trovato:
            print("Trovato")
        else:
            print("Non trovato")

    elif scelta == "5":
        print("Ciao")

    else:
        print("Scelta non valida")