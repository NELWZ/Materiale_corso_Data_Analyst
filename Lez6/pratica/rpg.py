# ==== RPG GAME ==== #
import random
from time import sleep as sl
s = "_" * 80
player = {
    'nome': 'Eroe',
    'vita': 100,
    'vita_max': 100,
    'mana': 50,
    'mana_max': 50,
    'att': 10,
    'livello': 1,
    'xp': 0,
    'xp_next': 50,
    'oro': 0,
    'inventario': ['poz_hp', 'poz_mp', 'poz_at'],
    'vinto': False
}

nomi = ['Lupo','Orso','Orco','Goblin']
nemico = {
    'nome': random.choice(nomi),
    'vita': random.randint(20, 50),
    'att': random.randint(2, 10),
    'drop_xp': random.randint(5, 15),
    'drop_oro': random.randint(5, 20)}

while True:
    # === GENERATORE NEMICO === #
    if player['vinto']:
        player['vinto'] = False
        nemico = {
            'nome': random.choice(nomi),
            'vita': random.randint(20, 50),
            'att': random.randint(2, 10),
            'drop_xp': random.randint(5, 15),
            'drop_oro': random.randint(5, 20)}
    sl(0.2)
    print(f"Un {nemico['nome']} ti sta attacando")
    # === NEMICO STATS === #
    v = nemico['vita']
    a = nemico['att']
    sl(0.2)
    print(f"Vita Nemico: {v}")
    sl(0.2)
    print(f"Attacco Nemico: {a}")
    print(s)
    # === MOSSA PLAYER === #
    scelta = input("1-Attacca\n2-Pozioni\n3-Scappa\n: ")
    
    print(s)
    sl(0.2)
    # === CONDIZIONI === #
    if scelta == "1":
        print(f"{player['nome']} ha colpito {nemico['nome']}")
        sl(0.2)
        
        # === FORMULA DANNO === #
        nemico['vita'] -= player['att']
        print(f"Hai inflitto {player['att']} danni")
        
        # uccidiamo il nemico
        if nemico['vita'] <= 0:
            nemico['vita'] = 0
            player['vinto'] = True
            print("NEMICO SCONFITTO")
            # === PREMIO === #
            player['oro'] += nemico['drop_oro']
            player['xp'] += nemico['drop_xp']
            
            print(f'Hai ricevuto +{nemico["drop_oro"]} oro e +{nemico["drop_xp"]} XP')
            sl(0.5)
            # === XP FORMULA === #
            if player['xp'] >= player['xp_next']:
                player['livello'] += 1
                player['xp'] = 0
                player['xp_next'] *= 1.2
                player['vita_max'] += random.randint(10, 20)
                player['att'] += random.randint(2, 6),
                player['mana_max'] += random.randint(5, 10)
                player['vita'] = player['vita_max']
                player['mana'] = player['mana_max']
                
        sl(0.2)
        print(s)
        
        # === DANNO AL PLAYER === #
        print(f"{nemico['nome']} ha fatto {nemico['att']} danni")
        player['vita'] -= nemico['att']
        print(s)
        sl(0.2)
        if player['vita'] <= 0:
            player['vita'] = 0
            # === MORTE PLAYER === #
            print("=== HAI PERSO ===")
            break
    elif scelta == "2":
        for p in player['inventario']:
            print(p)
        usa = input("Nome pozione (PREMI INVIO PER USCIRE): ")
        if usa == "":
            continue
        else:
            if usa in player['inventario']:
                
                if "hp" in usa and player['vita'] < player['vita_max']:
                    # === ELIMINARE LA POZIONE === #
                    player['inventario'].remove(usa)
                    player['vita'] += 50
                    if player['vita'] >= player['vita_max']:
                        player['vita'] = player['vita_max']
                    print("POZIONE USATA: +50 VITA")
                else:
                    print("Non hai bisogno di curarti la vita")
                if "mp" in usa and player['mana'] < player['mana_max']:
                    player['inventario'].remove(usa)
                    player['mana'] += 10
                    if player['mana'] >= player['mana_max']:
                        player['mana'] = player['mana_max']
                    print("POZIONE USATA: +10 MANA")
                else:
                    print("Non hai bisogno di usare la pozione")
    elif scelta == "3":
        break
    else:
        print("scelta non valida")
    # === RECAP === #
    print("=== PLAYER STATS ===")
    print(f"Vita: {player['vita']}")
    print(f"Mana: {player['mana']}")
    print(f"Att: {player['att']}")
    print(f"Livello: {player['livello']}")
    print(f"XP: {player['xp']}/{player['xp_next']}")
    print(f"Mancano {player['xp_next'] - player['xp']} XP per illivello {player['livello'] + 1}")
    print(s)
    sl(1.0)