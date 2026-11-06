# =============== RIPASSO =============== #
'PRINT'
print(2+2)
print()
print('cose')

# =============== VARIABILI =============== #
key = "value"

nome = "Celeste"
numero = 15
pi = 3.14
freddo = False

# =============== TIPI DI DATI =============== #

'''
'DATI NUMERICI'
    ╚→ INTERO → int() ► int(3.14) → 3
    ╚→ DECIMALE → float() ► float(True) → 1.0

'DATI LETTERALI'
    ╚→ STRINGHE → str() ► str(12) → "12"

'DATI BOOLEANI'
    ╚→ CONTROLLO → bool() ► bool(5) → True
'''

# =============== CONDIZIONI =============== #
'''
IF → SE
_______________________________
fame = True
if fame:
    print("mangio")
_______________________________

ELIF → ALTRIMENTI SE
_______________________________
elif not fame:
    print("non mangio")
_______________________________

ELSE → ALTRIMENTI

_______________________________
else:
    print("non ne ho idea a questo puto")
_______________________________
'''
# =============== OPERATORI LOGICI DI CONFRONTO =============== #

'== → uguale a → 5 == 5 ► True | "5" == 5 ► False'
nome = "Sarah"
if nome == "Marco":
    print("Sei VIP")
# ______________________________________________________________
'> → maggiore di → 5 > 7 ► False | 11 > 5 ► True | "ciao" > "ok" ► True'
anni = 20
if anni > 17:
    print("ormai sei grande")
# ______________________________________________________________

'< → minore di → 15 < 18 ► True | 15 < 12 ► False'
if anni < 18:
    print("sei ancora troppo piccolo per la patente")
# ______________________________________________________________
'>= → maggiore di o uguale a → 5 >= 5 ► True | 5 >= 2 ► True'
if anni >= 18:
    print("waw")
# ______________________________________________________________
'<= → minore di o uguale a → 5 <= 5 ► True | 15 <= 20 ► True'
# ______________________________________________________________
'AND → e | anche → 5 == 5 and 7 > 2 ► True'
'''
True AND True = True → 10 > 5 and 5 < 10 ► True
False AND True = False → 5 > 7 and 5 < 10 ► False
True AND False = False → 10 > 5 and 5 > 10 ► False
False AND False = False → 5 == 2 and 8 > 12 ► False
'''
password = "123"
nome_utente = "Andrea"

if password == "1256" and nome_utente == "Andrea12":
    print("Login riuscito")
# ______________________________________________________________
'OR → o | oppure → 5 == 5 or 7 > 12 ► True'
'''
True OR True = True → 'ciao' == 'ciao' or 5 == 5 ► True
False OR True = True → 5 > 7 or 12 < 15 ► True
True OR False = True → 5 > 2 or 12 < 5 ► True
False or False = False → 5 == 2 or 2 == 5 ► False
'''
nome = "Marco"

if nome == "Marco" or nome == "Sarah" or nome == "Celeste":
    print("Sei VIP")
# ______________________________________________________________
'IN → in | dentro → "ciao" in "ciao, mi chiamo Celeste" ► True'

vocali = "aeiou"

if "a" in vocali:
    print("è una vocale")
# ______________________________________________________________
'NOT → non è'
sonno = False

if sonno == False:
    print("ok")

if not sonno:
    print("ok")
# ______________________________________________________________


