# Simulazione Test d'Ingresso  Data Analyst Junior

---

## Come funziona

- **Durata:** 90 minuti (i colloqui veri danno 60–90 min quindi prova in 60)
- **Modalità:** apri un notebook, leggi il contesto, risolvi o sa vscode chi se ne frega, la non avrai vscode
- **Dataset:** usa `vendite_sporco.csv`  usa uno dei geenratori fatti da noi
- **Regola:** non usare AI per il codice (soluzioni) puoi usarlo per imparare e capire

---

## 🏢 Contesto aziendale (leggilo, è importante)

> *Sei candidato per un ruolo di Data Analyst Junior in **RetailNova**, una catena di negozi. Il tuo futuro capo ti manda un file esportato dal gestionale, `vendite_sporco.csv`, con una nota:*
>
> *"Il file è come ce l'ha passato l'IT. Non fidarti troppo. Fammi sapere cosa trovi, pulisci il necessario e dammi 3 numeri che mi servono per la riunione di domani: quanto vendiamo, dove, e a chi. Se hai tempo, dimmi anche cosa non torna."*
>
> *Benvenuto in azienda.*

Questa è **realistica**: nessuno ti dà dati puliti, e il capo non ti chiede 20 tabelle — ti chiede un riassunto.

---

## Parte 1  Ispezione

### Traccia 1.1 — La prima occhiata

Carica il file e rispondi **stampando**:

- Quante righe e colonne ha?
- Quanti valori mancanti ci sono per colonna?
- Quali colonne dovrebbero essere numeriche ma non lo sono?

> **Cosa valutano:** se apri i dati prima di toccarli. Il 70% dei candidati si butta a fare `groupby` senza sapere che colonna è di che tipo.

### Traccia 1.2  Diagnosi

Identifica **almeno 5 tipi di problemi diversi** presenti nel file. Per ognuno, scrivi in un commento:

- In quale colonna si trova
- Un esempio di valore
- Perché è un problema

> **Cosa valutano:** se sai distinguere "mancante" da "impossibile" da "incoerente". Sono tre problemi diversi con tre soluzioni diverse.

---

## Parte 2  Pulizia (25 min)

### Traccia 2.1 — Pulizia completa

Scrivi una pipeline di pulizia. Alla fine, il DataFrame deve passare questi controlli:

```python
assert df["prezzo_unitario"].notna().all()
assert df["quantità"].notna().all()
assert df["data"].notna().all()
assert (df["prezzo_unitario"] > 0).all()
assert (df["quantità"] > 0).all()
assert df["sconto"].between(0, 1).all()
assert df.duplicated().sum() == 0
```

Per **ogni decisione** (eliminare riga, riempire con un valore, scartare una colonna) aggiungi un commento che spieghi **perché**.

> **Cosa valutano:** la cosa più importante di tutta la prova. Un candidato che mette `fillna(0)` su tutto viene scartato. Uno che scrive "riempio `sconto` con 0 perché assenza di sconto registrato = sconto non concesso" viene assunto.

### Traccia 2.2 — Il giudizio

Rispondi a voce (o in un commento):

- Quante righe hai perso? Quali controlli le hanno eliminate?
- Cosa hai **deciso di non** buttare, e perché?
- Se ti accorgi che una colonna ha il 40% di valori mancanti, la elimini? La riempi? Dipende da cosa?

> **Cosa valutano:** se sai motivare una scelta. Non esiste "la pulizia giusta": esiste "la pulizia giustificata".

---

## Parte 3  Analisi (30 min)

### Traccia 3.1 I 3 numeri del capo

Il capo ti ha chiesto **tre numeri**. Stampali in modo chiaro:

```
[1] Fatturato totale netto: € X.XXX,XX
[2] Regione top per fatturato: XXXX (€ X.XXX,XX)
[3] Tipo di cliente top per fatturato: XXXX (€ X.XXX,XX)
```

> **Cosa valutano:** se sai rispondere a una domanda di business, non solo fare `sum()`. Il formato di output conta: il capo non legge DataFrame, legge numeri.

### Traccia 3.2 Il dettaglio per categoria

Produci una tabella (stampata o come DataFrame) con, per ogni categoria:

- fatturato netto
- numero di vendite
- scontrino medio
- sconto medio

Ordinala per fatturato decrescente.

> **Cosa valutano:** se sai usare `.agg()` con più funzioni. È il comando più usato in assoluto nella vita da analyst.

### Traccia 3.3 Il prodotto "strano"

Il capo ha un sospetto: *"Secondo me ci sono prodotti che vendono poco ma fatturano tanto, e altri il contrario. Mi confermi?"*

- Trova i **top 5 prodotti per fatturato**.
- Trova i **top 5 prodotti per quantità venduta**.
- I due ranking coincidono? Scrivi **una frase** che spieghi la differenza come se la dicessi al capo.

> **Cosa valutano:** se sai unire due analisi e **raccontarle**. La frase è più importante delle due tabelle.

### Traccia 3.4 Analisi temporale

- Calcola il fatturato per mese.
- **Domanda:** c'è un trend? O è rumore? Con 500 righe su 12 mesi, quanto ti fidi di un mese che va "male"? Scrivi la risposta.

> **Cosa valutano:** il **senso critico**. Un candidato che dice "a marzo vendiamo poco" senza chiedersi se è statistica o caso, viene scartato. Uno che dice "i numeri mensili ballano del 20%, con questi volumi non posso concludere niente" viene assunto.

---

## Parte 4 Le domande "cattive" (15 min)

Rispondi per iscritto, in un file di testo o in un commento nel codice. **Sono le domande che separano chi sa usare pandas da chi sa fare l'analyst.**

### Domanda 4.1

Il capo dice: *"Fammi il fatturato per città."* Tu gli dai `sum` o `mean`? E se lui risponde *"no, intendevo lo scontrino medio"*? Cosa cambia?

### Domanda 4.2

Hai due colonne: `totale` e `totale_scontato`. Il capo dice: *"il fatturato totale è la somma di tutte e due, no?"* Cosa rispondi?

### Domanda 4.3

Hai pulito i dati e hai perso il 15% delle righe. Il capo ti chiede: *"ma quindi hai buttato via il 15% del fatturato?"* Cosa rispondi? (attenzione: è una domanda trabocchetto)

### Domanda 4.4

Nella tabella per categoria, "Elettronica" fattura il 40%. Il capo dice: *"allora investiamo tutto sull'elettronica!"* Cosa gli fai notare prima che prenda una decisione sbagliata?

### Domanda 4.5

Il file conteneva una colonna `sconto` con valori tipo `"20%"`. Tu l'hai convertita in `NaN`. Un collega ti dice: *"dovevi trasformarla in 0.20, non buttarla!"* Chi ha ragione? E se avesse ragione lui, come avresti fatto?

> **Cosa valutano:** il **pensiero critico** e la capacità di **comunicare con un non-tecnico**. Nei colloqui veri, questa parte pesa quanto il codice.
