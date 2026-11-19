SELECT min(importo) as minimo,
max(importo) as massimo,
min(data) as primo_giorno,
max(data) as ultimo_giorno
FROM vendite;