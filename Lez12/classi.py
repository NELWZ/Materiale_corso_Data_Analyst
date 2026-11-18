# === CLASSI === #

'voglio creare le pizze'

class Forno:
    # === BUILDER ===
    def __init__(self, gusto, prezzo, quantita):
        self.var_gusto = gusto
        self.var_prezzo = prezzo
        self.var_quantita = quantita
        
    def info(self):
        return f"Ho le pizze al gusto di {self.var_gusto} costano €{self.var_prezzo} a pizza e ne ho sfornate {self.var_quantita}"

sfornata1 = Forno(gusto="Nutella", prezzo=6.99, quantita=15)
sfornata2 = Forno(gusto="Piccante", prezzo=7.99, quantita=2)

print(sfornata1.info())

# ====================================================== 

class Persona1:
    def __init__(self, nome, cognome):
        self.var_nome = nome
        self.var_cognome = cognome
        
    def info(self):
        return f"La persona si chiama {self.var_nome} {self.var_cognome}"

p1 = Persona1(nome="Marco", cognome="Rossi")
p2 = Persona1(nome="Luca", cognome="Verdi")

print(p1.var_nome)
print(p1.var_cognome)

print(p1.info())

print(p2.var_nome)
print(p2.var_cognome)

print(p2.info())

class Fabr:
    def __init__(self, modello, colore, peso, km, cavalli, cilindrata) -> None:
        self.var_modello = modello
        self.var_colore = colore
        self.var_peso = peso
        self.var_km = km
        self.var_cavalli = cavalli
        self.var_cilindrata = cilindrata
        self.var_data = '2015'
        
        def info(self):
            return
        
        def comportamento(self):
            return f"La amcchina {self.var_modello} raggiunge {self.var_km}km"

mac1 = Fabr(modello='Panda', colore="bianco", peso=368, km=180, cavalli=60, cilindrata=152)

m = mac1.var_modello
print(m)


class Persona:
    def __init__(self, nome, cognome, eta) -> None:
        self.var_nome = nome
        self.var_cognome = cognome
        self.var_eta = eta
        

marco = Persona(nome="Marco", cognome="Rossi", eta=25)

class Info(Persona):
    def __init__(self, nome, cognome, eta, lavoro, altezza, patente) -> None:
        super().__init__(nome, cognome, eta)
        self.var_lavoro = lavoro
        self.var_altezza = altezza
        self.var_patente = patente

class Scuola(Info):
    def __init__(self, nome, cognome, eta, lavoro, altezza, patente) -> None:
        super().__init__(nome, cognome, eta, lavoro, altezza, patente)
        
        
class Pulizia:
    def __init__(self, lettura, analisi, scrittura) -> None:
        self.lettura = lettura
        self.analisi = analisi
        self.scrittura = scrittura
        
class Csv(Pulizia):
    def __init__(self, lettura, analisi, scrittura, struttura, fomat) -> None:
        super().__init__(lettura, analisi, scrittura)
        self.struttura = struttura
        self.fomat = fomat
        
        
class Excel(Csv):
    def __init__(self, lettura, analisi, scrittura, struttura, fomat, formule) -> None:
        super().__init__(lettura, analisi, scrittura, struttura, fomat)
        self.forumle = formule