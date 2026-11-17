#^ === VENV === #
#? Virtual Enviroment
'''
• Cos'è?
È un contenitore isolato per il tuo progetto Python. Immaginalo come una "stanza sterile" in laboratorio: tutto ciò che entra (librerie, pacchetti) rimane dentro, e nulla di esterno contamina l'interno, né viceversa. Tecnicamente, è una directory che contiene una copia di Python e i suoi pacchetti installati localmente.
• Perché si usa?
Per evitare il "Dependency Hell" (Inferno delle Dipendenze).

    Senza venv, installi pandas 2.0 globalmente. Domani un altro progetto richiede pandas 1.3. Crash.
    Garantisce riproducibilità: chi clona il tuo repo può ricostruire esattamente il tuo ambiente usando requirements.txt.
    Protegge il sistema operativo: non sporchi Python globale con pacchetti sperimentali.

• Quando si usa?
Sempre. Ogni volta che inizi un nuovo progetto Python, prima ancora di scrivere una riga di codice. Anche per uno script veloce di analisi dati: crea un venv. È un'abitudine professionale, non un'opzione.
• Dove si usa?
Nel terminale/shell del tuo sistema operativo (macOS/Linux: Terminal; Windows: PowerShell o CMD). Si attiva nella directory radice del tuo progetto.
'''
#& === STEP BY STEP ===

#! DOBBIAMO ESSERE SICURI di essere nella nostra cartella

'aprire il terminale'

#? scrivi nel terminale
# WINDOWS
'python -m venv .nome_venv'

# MAC & LINUX
'python3 -m venv .nome_venv'

# ======================================================== #
#^ === ATTIVARE IL NOSTRO VIRTUAL ENVIROMENT === #
# WINDOWS 
'.nome_venv/Scripts/Activate'

# MAC & LINUX
'source .nome_venv/bin/activate'


#^ === DISATTIVARE IL NOSTRO VIRTUAL ENVIROMENT === #
# WINDOWS 
'.nome_venv/Scripts/Deactivate'

# MAC & LINUX
'source .nome_venv/bin/deactivate'


# ===================================================
#? INSTALLARE PANDAS
# WINDOWS
'pip install pandas'
'python -m pip install pandas'

# MAC & LINUX
'pip3 install pandas'


# === AGGIORNARE PIP ==='
# WINDOWS
'python -m pip install --upgrade pip'

# MAC & LINUX
'python3 -m pip install --upgrade pip'