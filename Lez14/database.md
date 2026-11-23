# === FOREGN KEY ===

##### **Una Foregn Key (FK) è un vincolo che collega due tabelle**

Server a garantire l'integrità **referenziale,** non puoi inserire in una tabella figlia un valore

che non esiste nella tabella 'madre"

**ESEMPIO**

ordini e utenti

CREATE TABLE immagini (

	id INT AUTO_INCREMENT PRIMARY KEY,

	utente_id INT NOT NULL,

	prodotto VARCHAR(100)

	totale DECIMAL(10, 2),

	FOREIGN KEY (utente_id) REFERENCES utenti(id) ON DELETE CASCADE)
