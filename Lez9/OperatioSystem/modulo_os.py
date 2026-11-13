#? === MODULO OS → Sistema Operativo === 
import os
'modulo ↑ → Operation System'

#^ === FUNZIONI FONDAMENTALI DEL MODULO OS ===

#& === GETCWD ===
# get current working directory
#? Cos'è?
'Restituisce una "stringa" con il percorso assoluto della directory di lavore corrente'

#? A cosa serve?
'Per sapere "dove siamo nel filesystem → da quale cartella il programma sta operando"'

#? Quando si usa?
"all'inizio di uno script, per fare il debug"

#? Perchè si usa?
'Si usa per evitare errori di percorso'

#~ ESEMPIO 
percorso_attuale = os.getcwd()
#! print(f"NOI SIAMO QUI DENTRO: {percorso_attuale}")


#& === CHDIR ===
# Change Directory (percorso file)
#? Cos'è?
'Cambia la directory di lavoro'

#? A cosa serve?
"per spostardi da un percorso  all'altro"

#? Quando si usa?
'Quando il tuo script deve operare(lavorare) in una cartella diversa'

#? Perchè si usa?
'Per comodità:  per evitare di ripetere i  percorsi'

#~ ESEMPIO  I
# print(f"Noi siamo: {os.getcwd()}")
# os.chdir("./Lez1")
# print(f"Noi siamo: {os.getcwd()}")


#~ ESEMPIO II
# os.chdir('C:\\Users\\avare\\Desktop\\Python')
# os.system('dir')

# os.chdir('./Lez6')
# os.system('dir')


#! ============================================================= #
#^ === PATH.EXISTS === #
'path.exists ► esistenza del percorso'
#? Cos'è?
'Una verifica se una cartella o file esistono'

#? A cosa serve?
'Per verificare la presenza di un certo file o cartella'

#? Quando si usa?
'Tutte quelle volte in cui devi verificare un file'
if not os.path.exists("file.txt"):
    open("file.txt", "x")


#? Perchè si usa?
'per evitare errori brutti'

os.path.exists('carciofo.txt') # ► False ► file non esiste
os.path.exists('./Lez9') # ► True ► Questa cartella esiste

def esempio():
    if os.path.exists("cartella_1"):
        print("La cartella esiste")
        print("Elimino la cratella...")
        
        #! Viene eliminata
        os.rmdir("cartella_1")
        
        print("Cartella iliminata")
    else:
        print("La cartella non esiste")
        print("creo la cartella...")
        
        #* Viene creata
        os.mkdir("cartella_1")
        
        print("cartella creata")


#^ === MKDIR & MAKEDIRS === #
'Maker Directory ► Crea una cartella'
'Maker Directoryes ► Crea un percorso di cartelle'

#? Cos'è?
'os.mkdir("nome cartella")► Crea UNA SOLA directory'
'os.makedirs("nome cartella)► Crea una catena di cartelle'

#? A cosa serve?
'Serve per creare cartelle organizzate'

#? Quando si usa?
'Tutte quelle volte in cui serve una directory'

#? Perchè si usa?
'Per ordine del tuo codice'


#~ ESEMPIO 
'CREIAMO UNA CARTELLA'
if not os.path.exists('esempio'):
    pass#os.mkdir("esempio")

#^ exp_dir = "./tmp/codice/exp_001/outputs"

#^ os.makedirs(exp_dir, exist_ok=True)

#! os.rmdir('tmp') # ERRORE


#^ === REMOVE === #
#? Cos'è?
'remove è una funzione OS che permette ri eliminare un file'

#? A cosa serve?
'A eliminare uno o più file'

#? Quando si usa?
'Quando dobbiamo eliminare i file'

#? Perchè si usa?
'Per eliminare i file'
f = ['file.txt', 'nome.txt', 'punti_moneta.txt']
for files in f:
    if os.path.exists(files):
        os.remove(files)