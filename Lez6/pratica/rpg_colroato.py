# ==== RPG GAME CON COLORAMA ==== #
import random
from time import sleep as sl
from colorama import init, Fore, Back, Style

# Inizializza colorama (autoreset evita di dover resettare manualmente)
init(autoreset=True)

# === COSTANTI COLORI / STILI === #
LINEA = Style.BRIGHT + Fore.CYAN + "═" * 70
SOTTOLINEA = Fore.CYAN + "─" * 70
TITOLO = Style.BRIGHT + Fore.YELLOW
TESTO = Fore.WHITE
OK = Style.BRIGHT + Fore.GREEN
ERRORE = Style.BRIGHT + Fore.RED
INFO = Style.BRIGHT + Fore.CYAN
WARN = Style.BRIGHT + Fore.YELLOW
MAGENTA = Style.BRIGHT + Fore.MAGENTA
BLU = Style.BRIGHT + Fore.BLUE


# === FUNZIONI DI SUPPORTO === #
def box(titolo, colore=Fore.CYAN):
    """Stampa un'intestazione in un box decorativo."""
    print(colore + "╔" + "═" * 68 + "╗")
    print(colore + "║" + Style.BRIGHT + Fore.WHITE + f" {titolo}".ljust(68) + colore + "║")
    print(colore + "╚" + "═" * 68 + "╝")


def barra(valore, massimo, lunghezza=20, colore_pieno=Fore.GREEN, colore_vuoto=Fore.RED):
    """Disegna una barra di progresso colorata."""
    if massimo <= 0:
        massimo = 1
    pieni = int((valore / massimo) * lunghezza)
    pieni = max(0, min(lunghezza, pieni))
    barra_str = colore_pieno + "█" * pieni + colore_vuoto + "░" * (lunghezza - pieni) + Style.RESET_ALL
    return f"[{barra_str}] {valore}/{massimo}"


def crea_nemico(nomi):
    return {
        'nome': random.choice(nomi),
        'vita': random.randint(20, 50),
        'att': random.randint(2, 10),
        'drop_xp': random.randint(5, 15),
        'drop_oro': random.randint(5, 20)
    }


def mostra_stats(player):
    print(SOTTOLINEA)
    print(TITOLO + "  📊  STATISTICHE PLAYER")
    print(SOTTOLINEA)
    print(INFO + f"  👤 Nome:     " + TESTO + player['nome'])
    print(OK +   f"  ❤️  Vita:     " + barra(player['vita'], player['vita_max'], colore_pieno=Fore.GREEN))
    print(BLU +  f"  💧 Mana:     " + barra(player['mana'], player['mana_max'], colore_pieno=Fore.BLUE, colore_vuoto=Fore.BLACK))
    print(MAGENTA + f"  ⚔️  Attacco:  " + TESTO + str(player['att']))
    print(WARN + f"  ⭐ Livello:  " + TESTO + str(player['livello']))
    print(WARN + f"  ✨ XP:       " + TESTO + f"{player['xp']}/{player['xp_next']}  " +
          INFO + f"(mancano {int(player['xp_next'] - player['xp'])} XP)")
    print(WARN + f"  💰 Oro:      " + TESTO + str(player['oro']))
    print(SOTTOLINEA)


def mostra_nemico(nemico):
    print(SOTTOLINEA)
    print(ERRORE + f"  👹 {nemico['nome']} ti sta attaccando!")
    print(SOTTOLINEA)
    print(ERRORE + f"  ❤️  Vita Nemico:    " + barra(nemico['vita'], 50, colore_pieno=Fore.RED, colore_vuoto=Fore.BLACK))
    print(ERRORE + f"  ⚔️  Attacco Nemico: " + TESTO + str(nemico['att']))
    print(SOTTOLINEA)


# === SETUP INIZIALE === #
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

nomi = ['Lupo', 'Orso', 'Orco', 'Goblin']
nemico = crea_nemico(nomi)

# === SCHERMATA INIZIALE === #
print(LINEA)
box("⚔️  BENVENUTO NELL'RPG  ⚔️", Fore.YELLOW)
print(LINEA)
print(INFO + "  Preparati all'avventura, " + WARN + player['nome'] + INFO + "!")
sl(0.8)

# === LOOP PRINCIPALE === #
while True:
    if player['vinto']:
        player['vinto'] = False
        nemico = crea_nemico(nomi)

    sl(0.2)
    mostra_nemico(nemico)

    # === MOSSA PLAYER === #
    print(TITOLO + "  🎯 SCEGLI LA TUA MOSSA")
    print(OK +    "  [1] ⚔️  Attacca")
    print(BLU +   "  [2] 🧪 Pozioni")
    print(WARN +  "  [3] 🏃 Scappa")
    scelta = input(INFO + "  ➤ Scelta: " + TESTO).strip()
    print(SOTTOLINEA)

    # === AZIONE ATTACCA === #
    if scelta == "1":
        sl(0.2)
        print(OK + f"  ⚔️  {player['nome']} colpisce {nemico['nome']}!")
        sl(0.2)
        nemico['vita'] -= player['att']
        print(ERRORE + f"  💥 Hai inflitto {player['att']} danni!")

        if nemico['vita'] <= 0:
            nemico['vita'] = 0
            player['vinto'] = True
            sl(0.2)
            print(Style.BRIGHT + Fore.GREEN + "  ✨═══════════════════════════════════✨")
            print(Style.BRIGHT + Fore.GREEN + f"     🏆 NEMICO SCONFITTO! 🏆")
            print(Style.BRIGHT + Fore.GREEN + "  ✨═══════════════════════════════════✨")
            sl(0.3)
            player['oro'] += nemico['drop_oro']
            player['xp'] += nemico['drop_xp']
            print(WARN + f"  💰 +{nemico['drop_oro']} oro   " + MAGENTA + f"✨ +{nemico['drop_xp']} XP")
            sl(0.5)

            # === LEVEL UP === #
            if player['xp'] >= player['xp_next']:
                player['livello'] += 1
                player['xp'] = 0
                player['xp_next'] = int(player['xp_next'] * 1.2)
                player['vita_max'] += random.randint(10, 20)
                player['att'] += random.randint(2, 6)
                player['mana_max'] += random.randint(5, 10)
                player['vita'] = player['vita_max']
                player['mana'] = player['mana_max']
                sl(0.3)
                print(Style.BRIGHT + Fore.YELLOW + "  ╔═══════════════════════════════════╗")
                print(Style.BRIGHT + Fore.YELLOW + f"  ║  🌟 LEVEL UP! Livello {player['livello']}!  ║")
                print(Style.BRIGHT + Fore.YELLOW + "  ╚═══════════════════════════════════╝")
                print(OK + "  ❤️  Vita al massimo! Attacco aumentato!")

        else:
            # === DANNO AL PLAYER (solo se nemico vivo) === #
            sl(0.2)
            print(ERRORE + f"  👹 {nemico['nome']} ti attacca per {nemico['att']} danni!")
            player['vita'] -= nemico['att']
            if player['vita'] <= 0:
                player['vita'] = 0
                print(Style.BRIGHT + Fore.RED + "╔═══════════════════════════════════╗")
                print(Style.BRIGHT + Fore.RED + "║          💀 HAI PERSO 💀          ║")
                print(Style.BRIGHT + Fore.RED + "╚═══════════════════════════════════╝")
                break

    # === AZIONE POZIONI === #
    elif scelta == "2":
        print(BLU + "  🎒 INVENTARIO:")
        if not player['inventario']:
            print(WARN + "     (vuoto)")
        for i, p in enumerate(player['inventario'], 1):
            icona = "❤️ " if "hp" in p else "💧" if "mp" in p else "⚔️ "
            print(TESTO + f"     {i}. {icona} {p}")
        print(SOTTOLINEA)
        usa = input(INFO + "  ➤ Nome pozione (INVIO per uscire): " + TESTO).strip()
        if usa == "":
            continue

        if usa in player['inventario']:
            # Pozione HP
            if "hp" in usa:
                if player['vita'] < player['vita_max']:
                    player['inventario'].remove(usa)
                    player['vita'] = min(player['vita'] + 50, player['vita_max'])
                    print(OK + f"  🧪 Pozione usata: ❤️  +50 Vita!")
                else:
                    print(WARN + "  ⚠️  Non hai bisogno di curarti la vita.")
            # Pozione MP
            elif "mp" in usa:
                if player['mana'] < player['mana_max']:
                    player['inventario'].remove(usa)
                    player['mana'] = min(player['mana'] + 10, player['mana_max'])
                    print(BLU + f"  🧪 Pozione usata: 💧 +10 Mana!")
                else:
                    print(WARN + "  ⚠️  Non hai bisogno di mana.")
            else:
                print(WARN + "  ⚠️  Questa pozione non è ancora utilizzabile.")
        else:
            print(ERRORE + "  ❌ Pozione non trovata nell'inventario.")

    # === AZIONE SCAPPA === #
    elif scelta == "3":
        print(WARN + "  🏃 Hai scappato dal combattimento...")
        sl(0.5)
        break
    else:
        print(ERRORE + "  ❌ Scelta non valida!")

    # === RECAP === #
    sl(0.5)
    mostra_stats(player)
    sl(1.0)