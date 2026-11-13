from geraci import File
# === GESTIONE-FILE === 

#^ === ESEMPIO 1 === 
contenuto = File('note.txt').read()
print(contenuto)

'''
#^ === DOCS === 
File('note.txt') ► #? Crea un oggetto che rappresenta
.read() ► #? Legge il file
'''

#^ === ESEMPIO 2 === 
File('note.txt').write("contenuto del file")

'''
#^ === DOCS === 
File('note.txt') ► #? Crea un oggetto che rappresenta
.write() ► #? Scrive nel file e sovrascrive tutto il contenuto
'''


#^ === ESEMPIO 3 === 
File('note.txt').write('Riga 1').append("\nRiga 2").append("\nRiga 3")


#^ === ESEMPIO 4 === 
new_file = File('note.txt').copy('backup.txt')


#^ === ESEMPIO 5 === 
File('note.txt').move('percorso/della/nuova/cartella')


#^ === ESEMPIO 6 === 
File('nome_vecchio.txt').rename("nome_nuovo.txt")

'cambia nome e sposta'
File('percorso/file/note.txt').rename("nuovo/percorso/file/backup.txt")

#^ === ESEMPIO 7 === 
File("note.txt").delet()


#^ === ESEMPIO 8 === 
info = File('note,txt').info()

info.size_human # 12 B
info.sha256 # hasg SHA-256 
info.size # dimensioni in byte

#^ === ESEMPIO 9 === 
'VERIFICARE SE ILFILE ESISTE'
if File('note.txt').exists():
    print("esiste")
else:
    print("'non esiste")


#? ============================================================ #
#^ === OPERAZIONI SU DIRECTORY ====

from geraci import Folder

'Creare una cartella #! nel percorso di questo file python'
Folder('nome_cartella').create()

#& === DOVE CREARE LA CARTELLA ===
Folder('percorso/dove/creare/nome_cartella').create()

'Elencare tutto il contenuto'

for contenuto in Folder('nome_cartella').list():
    print(contenuto)
    
#& === CARTELLA IN UN PERCORSO DIVERSO === 
for contenuto in Folder('percorso/dove/creare/nome_cartella').list():
    print(contenuto)

'WALK RICORSIVO'
for elemento in Folder("my_project").walk():
    print(elemento)


'CALCOLARE DIMENSIONE TOTALE'
totale = Folder('nome_cartella').size()
print(totale)

'ELIMINARE UNA CARTELLA'
Folder('nome_cartela').delete()

'ELIMINARE UNA CARTELLA RICORSIVAMENTE'
Folder('nome_cartella').delete(recursive=True)

'SINCRONIZZARE DUE CARTELLE'
Folder('sorgente').sync('destinazione')

#HACK ======================================================================
'COMPRIMERE FILE E CARTELLE'
from geraci import File, Folder
File('documento.pdf').compress('doc.zip')
Folder('foto').compress('le_foto.tar.gz')

'DECOMPRIMERE - EXTRACT FILE O CARTELLE'
from geraci import decompress

decompress('doc.zip', 'cartella_decompressa')


