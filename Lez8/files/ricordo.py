# ===================================================================== #

#^ APRIAMO IL FILE E LO LEGGIAMO
with open("nome.txt", "r") as f:
    #& Variabile nome = LETTUTRA DEL CONTENUTO DEL FILE
    nome = f.read()
    #? bool(contenuto del file) → SE il file ha qualcosa dentro
    if nome:
        #? print
        print(f"Ciao {nome}")
    #! ALTRIMENTI → se il file non ha nessun contenuto dentro
    else:
        # variabile per prendere il nome utente
        x = input("come ti chiami?\n: ")
        
        #* APRIAMO IL FILE E SCRIVIAMO DENTRO
        with open("nome.txt", "w") as f:
            #~ SCRIVIAMO DENTRO I CONTENUTO DELLA x (il nome utente)
            f.write(x)




