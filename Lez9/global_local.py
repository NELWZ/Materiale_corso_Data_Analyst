#NOTE === VARIABILI GLOBALI E LOCALI ===

#? === COSA E' UNA VARIABILE LOCALE?
#* una varibile LOCALE è una variabile definita (creata)
#* dentro una FUNZIONE: esiste solo mentre la
#* funzione è in esecuzione
def bar_():
    prz_cornetto = 1.99 #^ VARIABILE LOCAL

#? === COSA è UNA VARIABILE GLOBALE?
#* una variaile GLOBALE è una variabile definita (creata)
#* a livello di modulo (fuori da qualsiasi funzione o classe)
#* definita dentro il nostro codice.
#* è visibile in TUTTO IL FILE 
#^ VISIBILE in LETTURA anche dentro le funzioni

soldi = 100 # GLOBALE PER TUTTO IL CODICE

def banca_(): # è uno spazio LOCALE
    soldi += 1
    
def banca_con_il_permesso():
    global soldi
    soldi -= 100

#~ Modello LEGB
#^ LOCAL        → variabile è dentro una fuznione
#^ ENCLOSING    → variabile nella funzione esterna (funzioni annidate)
#^ GLOBAL       → variabile a livello di modulo → DENTRO il tuo file
#^ BUILT-IN     → varibili, funzioni e metodi di python → print, max, min, len

#! ========================================================= #
'quando scrivi x: Python cerca in L, poi E, poi G, poi B'

#NOTE === VARIABILE LOCALE SEMPLICE ===
def calcola():
    risultato = 10 + 5 # LOCALE esiste SOLO qui dentro
    print(risultato)

# calcola() # STAMPA IL 15 → CREA la variabile

'print(risultato) → SyntaxError → la variabile #! NON esiste'

def armadio():
    giacca = "di pelle" # LOCALE
    print(f"indosso la mia giacca {giacca}")

# armadio()


#NOTE === VARIABILE GLOBALE SEMPLICE ===

soldi = 100.0 #^ variabile GLOBALE
'disponibile a TUTTO il codice ma non alle funzioni'

def negozio(prz_ogg):
    global soldi
    if soldi >= prz_ogg:
        print("lo puoi comprare")
        soldi -= prz_ogg
    else:
        print("costa troppo")
    
def bar():
    global soldi
    cornetto = 1.20
    if soldi >= cornetto:
        print("cornetto preso")
        soldi -= cornetto

# negozio(119.99)
# negozio(99.99)

sito = "miosito.it"

def america():
    global sito # rednilo GLOBALE anche per questa funzione LOCALE
    print(sito)
    if '.it' in sito:
        print("The site is Italian")
    sito = "mysite.com"

#america()

risparmio = 500.56 # GLOBALE
risparmio += soldi


def banca():
    risparmio = 599.99
    risparmio -= 50
    print(risparmio)

# print(risparmio)
# banca()
# print(risparmio)


