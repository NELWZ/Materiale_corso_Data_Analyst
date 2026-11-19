import secrets
from datetime import datetime, timedelta
from db import esegui
from security import hash_password, verify_password

# === REGISTRAZIONE === #
def registra(username: str, email: str, password: str):
    username = username.strip()#.capitalize() # MaRCO → Marco
    email = email.strip().lower()
    if len(username) < 3:
        return {'ok': False, 'errore': 'username troppo corto'}
    if '@' not in email or '.' not in email:
        return {'ok': False, 'errore': 'email non valida'}
    if len(password) < 8:
        return {'ok': False, 'errore': 'password non valida'}
    
    # utente esiste nel database
    esiste = esegui(
        'SELECT id FROM utenti WHERE username = %s OR email = %s',
        (username, email), fetch='one',)
    
    if esiste:
        return {'ok': False, 'errore': 'utente già presente'}
    
    # se tutto funziona ed è tutto verificato (password, username, email)
    nuovo_id = esegui(
        'INSERT INTO utenti (username, email, password_hash) VALUES (%s, %s,%s)',
        (username, email, hash_password(password)),
    )
    return {'ok': True, 'id': nuovo_id}
    
# === LOGIN NELDATABASE === #
def login(username:str, password: str):
    username = username.strip()
    utente = esegui(
        'SELECT id, username, email, password_hash FROM utenti WHERE username = %s',
        (username,), fetch='one',
    )
    
    if not utente:
        return {'ok': False, 'errore': 'credenziali non valide'}
    
    if not verify_password(password, utente['password_hash']):
        return {'ok': False, 'errore': 'credenziali non valide'}
    
    utente.pop('password_hash')
    return {'ok': True, 'utente': utente}
    
def genera_token_recupero(email: str):
    email = email.strip().lower()
    utente = esegui('SELECT id FROM utenti WHERE email = %s', (email,), fetch="one")

    if not utente:
        return {'ok': False, 'errore': 'utente non esiste'}
    
    token = secrets.token_urlsafe(32)
    scade = datetime.now() + timedelta(minutes=15)

    esegui(
        'INSERT INTO reset_tokens (utente_id, token, scade_il) VALUES (%s, %s, %s)',
        (utente['id'], token, scade),
    )
    return {'ok': True, 'token': token, 'scade': scade}

def reset_password(token: str, nuova_password: str):
    if len(nuova_password) < 8:
        return {'ok': False, 'errore': 'password troppo corta'}

    riga = esegui(
        'SELECT id, utente_id, scade_il, usato FROM reset_tokens WHERE token = %s',
        (token,), fetch = 'one',
    )
    
    if not riga:
        return {'ok': False,'errore': 'token non valido'}
    if riga['usato']:
        return {'ok': False,'errore': 'token già usato'}
    if riga['scade_il'] < datetime.now():
        return {'ok': False,'errore': 'token scaduto'}
        
    esegui(
        'UPDATE utenti SET password_hash = %s WHERE id = %s',
        (hash_password(nuova_password), riga['utente_id']),
    )
    
    esegui('UPDATE reset_tokens SET usato = TRUE WHERE id = %s', (riga['id'],))
    return {'ok': True, 'messaggio': 'password aggiornata'}
    
# === CAMIO PASSWORD === #
def cambia_password(username: str, vecchia: str, nuova:str):
    if len(nuova) < 8:
        return {'ok': False, 'errore': 'password troppo corta'}
    
    utente = esegui(
        'SELECT id, password_hash FROM utenti WHERE username = %s',
        (username,), fetch='one',
    )
    if not utente:
        return {'ok': False, 'errore': 'utente non esiste'}
    if not verify_password(vecchia, utente['password_hash']):
        return {'ok': False, 'errore': 'vecchia password errata'}
    esegui(
        'UPDATE utenti SET password_hash = %s WHERE id = %s',
        (hash_password(nuova), utente['id']),
    )
    return {'ok': True, 'messaggio': 'password cambiata'}

def pulisci_token_scaduti():
    from db import get_connection
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM reset_tokens WHERE scade_il < NOW() - INTERVAL 1 DAY")
    n = cur.rowcount
    conn.commit()
    cur.close()
    conn.close()
    return n
