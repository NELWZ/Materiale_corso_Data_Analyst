# === ESEMPIO ===
import os

def crea_cartella(nome, debug=False):
    if not os.path.exists(nome):
        os.mkdir(nome)
        if debug:
            print(f'Cartella "{nome}" è  stata creata')
    else:
        if debug:
            print(f'La cartella "{nome}" esiste già')

def elimina_cartella(nome, debug=False):
    if os.path.exists(nome):
        os.rmdir(nome)
        if debug:
            print(f'La cartella "{nome}" è stata eliminata')
    else:
        if debug:
            print(f'La cartella "{nome}" non esiste')

crea_cartella('esempio', True)
elimina_cartella('esempio', True)
