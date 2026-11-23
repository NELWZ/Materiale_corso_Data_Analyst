import json
import os
from datetime import datetime
from typing import Optional


class Utente:
    """Rappresenta un singolo utente nell'albero."""
    
    def __init__(self, id_utente: int, nome: str, referente_id: Optional[int] = None):
        self.id = id_utente
        self.nome = nome
        self.referente_id = referente_id  # chi lo ha portato (padre)
        self.figli = []  # utenti portati da questo utente
        self.data_iscrizione = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "referente_id": self.referente_id,
            "figli": self.figli,
            "data_iscrizione": self.data_iscrizione
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Utente":
        u = cls(data["id"], data["nome"], data["referente_id"])
        u.figli = data["figli"]
        u.data_iscrizione = data["data_iscrizione"]
        return u


class GestionaleAlbero:
    """Gestisce l'intero albero degli utenti."""
    
    FILE_DATI = "utenti_albero.json"
    
    def __init__(self):
        self.utenti: dict[int, Utente] = {}
        self.prossimo_id = 1
        self.carica_da_file()
    
    # ---------- PERSISTENZA ----------
    def salva_su_file(self):
        dati = {
            "prossimo_id": self.prossimo_id,
            "utenti": [u.to_dict() for u in self.utenti.values()]
        }
        with open(self.FILE_DATI, "w", encoding="utf-8") as f:
            json.dump(dati, f, indent=2, ensure_ascii=False)
    
    def carica_da_file(self):
        if not os.path.exists(self.FILE_DATI):
            return
        with open(self.FILE_DATI, "r", encoding="utf-8") as f:
            dati = json.load(f)
        self.prossimo_id = dati["prossimo_id"]
        for u_dict in dati["utenti"]:
            u = Utente.from_dict(u_dict)
            self.utenti[u.id] = u
    
    # ---------- OPERAZIONI ----------
    def aggiungi_utente(self, nome: str, referente_id: Optional[int] = None) -> Utente:
        """Aggiunge un utente. Se referente_id è None, è una radice."""
        if referente_id is not None and referente_id not in self.utenti:
            raise ValueError(f"Referente {referente_id} non esistente!")
        
        nuovo = Utente(self.prossimo_id, nome, referente_id)
        self.utenti[nuovo.id] = nuovo
        self.prossimo_id += 1
        
        if referente_id is not None:
            self.utenti[referente_id].figli.append(nuovo.id)
        
        self.salva_su_file()
        return nuovo
    
    def cerca_utente(self, id_utente: int) -> Optional[Utente]:
        return self.utenti.get(id_utente)
    
    def cerca_per_nome(self, nome: str) -> list[Utente]:
        nome_lower = nome.lower()
        return [u for u in self.utenti.values() if nome_lower in u.nome.lower()]
    
    def discendenti(self, id_utente: int) -> list[Utente]:
        """Restituisce tutti i discendenti (figli, nipoti, ecc.) di un utente."""
        if id_utente not in self.utenti:
            return []
        risultato = []
        stack = list(self.utenti[id_utente].figli)
        while stack:
            figlio_id = stack.pop()
            figlio = self.utenti[figlio_id]
            risultato.append(figlio)
            stack.extend(figlio.figli)
        return risultato
    
    def discendenti_diretti(self, id_utente: int) -> list[Utente]:
        """Solo i figli diretti."""
        if id_utente not in self.utenti:
            return []
        return [self.utenti[fid] for fid in self.utenti[id_utente].figli]
    
    def genealogia(self, id_utente: int) -> list[Utente]:
        """Catena di referenti: [radice, ..., utente]."""
        catena = []
        corrente = self.utenti.get(id_utente)
        while corrente:
            catena.append(corrente)
            if corrente.referente_id is None:
                break
            corrente = self.utenti.get(corrente.referente_id)
        return list(reversed(catena))
    
    def livello(self, id_utente: int) -> int:
        """Profondità nell'albero (radice=0)."""
        return len(self.genealogia(id_utente)) - 1
    
    def radici(self) -> list[Utente]:
        return [u for u in self.utenti.values() if u.referente_id is None]
    
    def elimina_utente(self, id_utente: int, riassegna_a: Optional[int] = None):
        """Elimina un utente. I figli possono essere riassegnati."""
        if id_utente not in self.utenti:
            raise ValueError("Utente non trovato")
        
        utente = self.utenti[id_utente]
        
        # rimuovi dai figli del padre
        if utente.referente_id is not None:
            padre = self.utenti[utente.referente_id]
            padre.figli.remove(id_utente)
        
        # gestisci i figli
        for figlio_id in utente.figli:
            figlio = self.utenti[figlio_id]
            if riassegna_a is not None and riassegna_a in self.utenti:
                figlio.referente_id = riassegna_a
                self.utenti[riassegna_a].figli.append(figlio_id)
            else:
                figlio.referente_id = utente.referente_id
                if utente.referente_id is not None:
                    self.utenti[utente.referente_id].figli.append(figlio_id)
        
        del self.utenti[id_utente]
        self.salva_su_file()
    
    # ---------- VISUALIZZAZIONE ----------
    def stampa_albero(self, id_utente: Optional[int] = None, prefisso: str = ""):
        """Stampa ricorsivamente l'albero (o sottoalbero)."""
        if id_utente is None:
            for radice in self.radici():
                self._stampa_nodo(radice.id, "")
        else:
            self._stampa_nodo(id_utente, "")
    
    def _stampa_nodo(self, id_utente: int, prefisso: str):
        u = self.utenti[id_utente]
        print(f"{prefisso}└── [{u.id}] {u.nome} (liv. {self.livello(u.id)})")
        for figlio_id in u.figli:
            self._stampa_nodo(figlio_id, prefisso + "    ")
    
    def statistiche(self) -> dict:
        livelli = {}
        for u in self.utenti.values():
            l = self.livello(u.id)
            livelli[l] = livelli.get(l, 0) + 1
        return {
            "totale_utenti": len(self.utenti),
            "radici": len(self.radici()),
            "distribuzione_livelli": livelli,
            "utente_con_piu_figli": max(
                self.utenti.values(),
                key=lambda u: len(u.figli),
                default=None
            ).nome if self.utenti else None
        }


# ============== INTERFACCIA CLI ==============
def menu():
    gest = GestionaleAlbero()
    
    while True:
        print("\n" + "=" * 50)
        print("  GESTIONALE UTENTI AD ALBERO")
        print("=" * 50)
        print("1. Aggiungi utente")
        print("2. Cerca utente per ID")
        print("3. Cerca per nome")
        print("4. Mostra albero completo")
        print("5. Mostra sottoalbero di un utente")
        print("6. Mostra genealogia (catena referenti)")
        print("7. Mostra discendenti di un utente")
        print("8. Elimina utente")
        print("9. Statistiche")
        print("0. Esci")
        
        scelta = input("\nScelta: ").strip()
        
        try:
            if scelta == "1":
                nome = input("Nome utente: ").strip()
                ref = input("ID referente (vuoto se radice): ").strip()
                ref_id = int(ref) if ref else None
                u = gest.aggiungi_utente(nome, ref_id)
                print(f"✓ Utente creato: ID={u.id}, Nome={u.nome}")
            
            elif scelta == "2":
                id_u = int(input("ID: "))
                u = gest.cerca_utente(id_u)
                if u:
                    print(f"ID: {u.id}\nNome: {u.nome}\nReferente: {u.referente_id}"
                          f"\nFigli diretti: {u.figli}\nIscritto: {u.data_iscrizione}")
                else:
                    print("✗ Utente non trovato")
            
            elif scelta == "3":
                nome = input("Nome (anche parziale): ")
                risultati = gest.cerca_per_nome(nome)
                if risultati:
                    for u in risultati:
                        print(f"  [{u.id}] {u.nome} (ref: {u.referente_id})")
                else:
                    print("✗ Nessun risultato")
            
            elif scelta == "4":
                if not gest.utenti:
                    print("(Albero vuoto)")
                else:
                    gest.stampa_albero()
            
            elif scelta == "5":
                id_u = int(input("ID utente: "))
                gest.stampa_albero(id_u)
            
            elif scelta == "6":
                id_u = int(input("ID utente: "))
                catena = gest.genealogia(id_u)
                print(" → ".join(f"[{u.id}] {u.nome}" for u in catena))
            
            elif scelta == "7":
                id_u = int(input("ID utente: "))
                disc = gest.discendenti(id_u)
                print(f"Totale discendenti: {len(disc)}")
                for u in disc:
                    print(f"  [{u.id}] {u.nome} (liv. {gest.livello(u.id)})")
            
            elif scelta == "8":
                id_u = int(input("ID utente da eliminare: "))
                ref = input("Riassegna figli a (ID, vuoto = al padre): ").strip()
                ref_id = int(ref) if ref else None
                gest.elimina_utente(id_u, ref_id)
                print("✓ Utente eliminato")
            
            elif scelta == "9":
                stats = gest.statistiche()
                for k, v in stats.items():
                    print(f"  {k}: {v}")
            
            elif scelta == "0":
                print("Arrivederci!")
                break
            else:
                print("Scelta non valida")
        
        except ValueError as e:
            print(f"✗ Errore: {e}")
        except Exception as e:
            print(f"✗ Errore imprevisto: {e}")


if __name__ == "__main__":
    menu()