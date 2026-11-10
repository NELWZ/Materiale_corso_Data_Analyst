stats_giocatore = {
	"vita": 100,
	"vita_massima": 100,
	"mana": 50,
	"mana_massimo": 50,
	"attacco": 10,
	"attacco_magico": 8,
	"difesa": 5,
	"difesa_magica": 4,
	"velocita": 7,
	"agilita": 6,
	"forza": 10,
	"intelligenza": 8,
	"destrezza": 7,
	"costituzione": 9,
	"fortuna": 5,
	"precisione": 80,
	"probabilita_critico": 10,
	"danno_critico": 150,
	"schivata": 5,
	"blocco": 5,
	"resistenza_fisica": 10,
	"resistenza_fuoco": 0,
	"resistenza_ghiaccio": 0,
	"resistenza_elettrica": 0,
	"resistenza_veleno": 0,
	"rigenerazione_vita": 1,
	"rigenerazione_mana": 2,
	"esperienza": 0,
	"livello": 1,
	"punti_esperienza_prossimo_livello": 100,
	"punti_stat_disponibili": 0,
	"punti_abilita_disponibili": 0,
	"oro": 0,
	"peso_inventario": 0,
	"capacita_inventario": 50,
	"fame": 0,
	"sete": 0,
	"energia": 100,
	"energia_massima": 100,
	"reputazione": 0,
	"carisma": 5,
	"furtivita": 5,
	"percezione": 6,
	"resistenza": 8,
	"disciplina": 5,
	"morale": 100,
	"velocita_attacco": 1.0,
	"portata_attacco": 1.5,
	"danno_minimo": 8,
	"danno_massimo": 12,
	"armatura": 5,
	"scudo": 0,
	"livello_minaccia": 1,
	"tempo_recupero": 0,
	"durata_effetti": 0,
	"livello_avvelenamento": 0,
	"livello_bruciatura": 0,
	"livello_congelamento": 0,
	"livello_stordimento": 0,
    'colpito': False
}

danno = 50


# vedo i dati



for c, v in stats_giocatore.items():
    print(f"chiave: {c} -  Valore: {v}")



print(stats_giocatore['colpito'])
print(stats_giocatore['vita'])
input("colpisci: ")
stats_giocatore['colpito'] = True

print(stats_giocatore['colpito'])

if stats_giocatore['colpito']:
    stats_giocatore['vita'] -= danno

print(stats_giocatore['vita'])
