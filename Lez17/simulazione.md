# Colloquio Data Analyst Junior

---

## Prova 1 - Il file rotto

Competenza testata: ispezione e diagnosi dei dati.

Dataset: `vendite_sporco.csv` 

Contesto:
Sei appena entrato in RetailNova. Il tuo collega è in ferie e ti lascia un file con una nota: "Questo è l'export del gestionale. Non fidarti. Dimmi cosa c'è che non va."

Consegna:
Produci un report di diagnosi che stampi:

1. Quante righe e colonne ha il file.
2. Quanti valori mancanti per colonna.
3. Quali colonne dovrebbero essere numeriche ma sono `object` (elencale).
4. Quanti duplicati esatti ci sono.
5. Almeno 4 tipi diversi di problema trovati, con un esempio di valore per ciascuno (es. "prezzo_unitario contiene 'N/D': stringa in colonna numerica").

Output atteso: un blocco di `print()` leggibile.

---

## Prova 2 - Pulisci senza buttare roba buona

Competenza testata: pulizia dati con scelte motivate.

Dataset: `vendite_sporco.csv`.

Contesto:
Il capo ti dice: "Pulisci il file. Ma attenzione: non buttare via righe che possiamo recuperare. E se butti, dimmi perché."

Consegna:
Produci un DataFrame `df_pulito` che:

- Non abbia duplicati.
- Abbia le colonne numeriche come numerici (`prezzo_unitario`, `quantità`, `sconto`, `totale`, `totale_scontato`, `età_cliente`).
- Non abbia valori impossibili: prezzo minore o uguale a 0 oppure maggiore di 10000, quantità minore di 1 o maggiore di 10, sconto fuori da [0,1], età fuori da [18,75].
- Abbia `data` come datetime, gestendo i formati misti: `"2024-03-07"`, `"2024/03/07"`, `"07/03/2024"`.
- Abbia `categoria` normalizzata: `" elettronica "` diventa `"Elettronica"`, `"Eletronica"` diventa `"Elettronica"`, `"Sportivo"` diventa `"Sport"`.
- Abbia i numeri con virgola italiana (`"12,50"`) recuperati come `12.50`, non buttati.
- Passi questi controlli:

```python
assert df_pulito["prezzo_unitario"].notna().all()
assert df_pulito["quantità"].notna().all()
assert df_pulito["data"].notna().all()
assert (df_pulito["prezzo_unitario"] > 0).all()
assert (df_pulito["quantità"] > 0).all()
assert df_pulito["sconto"].between(0, 1).all()
assert df_pulito.duplicated().sum() == 0
```

Per ogni decisione, un commento che spiega perché.

---

## Prova 3 - I tre numeri per la riunione

Competenza testata: aggregazioni e output per un non-tecnico.

Dataset: `vendite_pulito.csv`.

Contesto:
Il capo ha una riunione tra un'ora. Ti scrive: "Dammi tre numeri: quanto vendiamo, dove, a chi. Formato leggibile, devo leggerli ad alta voce."

Consegna:
Produci un output esattamente così:

```
[1] Fatturato totale netto: € XX.XXX,XX
[2] Regione top per fatturato: XXXX (€ XX.XXX,XX)
[3] Tipo di cliente top per fatturato: XXXX (€ XX.XXX,XX)
---
Transazioni: XXX | Scontrino medio: € XXX,XX
```

Poi, sotto, stampa anche il fatturato per categoria ordinato dal più alto.

---

## Prova 4 - Il prodotto strano

Competenza testata: analisi incrociata e comunicazione.

Dataset: `vendite_pulito.csv`.

Contesto:
Il capo sospetta: "Secondo me ci sono prodotti che vendono pochi pezzi ma fatturano tanto, e altri che vendono tanto ma fatturano poco. Mi confermi?"

Consegna:

1. Stampa i top 5 prodotti per fatturato netto.
2. Stampa i top 5 prodotti per quantità venduta.
3. Scrivi in un commento una frase di massimo 3 righe che spieghi la differenza come se la dicessi al capo, che non sa cosa sia un `groupby`.

---

## Prova 5 - Le domande cattive

Competenza testata: senso critico e comunicazione.

Dataset: nessuno. Rispondi per iscritto in un file di testo o in commenti nel codice.

Contesto:
Il colloquio è finito. Il selezionatore ti fa 5 domande da lunedì mattina. Non serve codice: serve testa.

Consegna: rispondi a tutte e 5.

5.1
Hai pulito i dati e hai perso il 18% delle righe. Il capo chiede: "Quindi hai buttato il 18% del fatturato?" Cosa rispondi?

5.2
Hai `totale` (lordo) e `totale_scontato` (netto). Il capo dice: "Il fatturato totale è la somma di tutte e due, no?" Cosa rispondi?

5.3
"Elettronica" fattura il 42%. Il capo dice: "Allora investiamo tutto sull'elettronica!" Cosa gli fai notare prima che decida?

5.4
Nel file c'era `sconto = "20%"`. Tu l'hai convertito in `NaN` con `errors="coerce"`. Un collega dice: "Dovevi trasformarlo in 0.20, non buttarlo!" Chi ha ragione? E come avresti fatto?

5.5
Con 500 righe su 12 mesi, il fatturato di marzo è il 20% più basso degli altri mesi. Il capo dice: "A marzo c'è un problema, indaghiamo!" Cosa rispondi?
