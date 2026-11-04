# Query avanzate e prestazioni



## Separa i costi

Selezione, valutazione filtri, parsing, aggregazione/ordinamento, trasferimento e rendering UI possono contribuire diversamente. Il diagramma è concettuale, non un execution plan fisico.

## Definisci l’equivalenza

Il set completo di source ID numerici può sostituire una ricerca per nome mantenendo scope. Una finestra più corta o meno host/processor cambia la copertura: va dichiarato.

## Controlla gli indici reali

Verifica Index Management secondo ruolo/build: proprietà corretta e periodo storico coperto. Abilitare un indice non crea automaticamente lo storico; valuta spazio e impatto sull’acquisizione.

## Parsing e indici

L’ottimizzazione del parsing prepara valori; l’indice aiuta a localizzarli. Sono controlli differenti. Verifica copertura dell’estrazione prima di sostituire un filtro raw con una proprietà.

## Testo e campi strutturati

sourceip = valore cerca un campo; una sottostringa raw può comparire ovunque. Non sono intercambiabili. TEXT SEARCH ha tokenizzazione propria e nei template va per primo, combinato con AND.

## Indagine in due passaggi

OPT02 seleziona QID, conteggi e tempi; OPT03 recupera raw mirati. Copri tutti i gruppi pertinenti, anche eventi rari decisivi, e verifica eventuale troncamento a LIMIT.

## Cardinalità

Raggruppare per sourceip è diverso da aggiungere URI completa e User-Agent. Togli dimensioni soltanto se la domanda rimane valida. Anche le viste accumulate hanno un costo di cardinalità.

## Sottoquery e baseline

Controlla query interna e cardinalità: un LIMIT più basso può eliminare candidati. I reference data sono stato corrente salvo snapshot precedente conservato; non apprendere contatti sospetti prima di cercare novità.

## Confronti A/B assoluti

Fissa START/STOP, sorgenti, domini, colonne e dati. Alterna A-B/B-A quando il costo operativo lo consente. Registra stato, conteggi, tempo motore, trasferimento/UI e note su cache e carico separatamente.

## Interpreta le misure

Per tre prove comparabili completate usa la mediana. Speedup = mediana A / mediana B con la stessa unità. Nessuna accelerazione del pacchetto rappresenta una misura sulla tua console.

## Periodi storici estesi

Segmenta con semantica dei confini documentata. SUM/COUNT sono ricomponibili con pesi corretti; UNIQUECOUNT non si somma se le identità si ripetono. Mantieni il contesto tra confini per le sequenze.

## OPT01 - IP strutturato, output minimo

```sql
SELECT starttime, sourceip, destinationip, qid
FROM events
WHERE logsourceid = <LS_ID>
  AND sourceip = '<IP>'
LIMIT 200
START '<START>' STOP '<STOP>'
```

Sostituire a raw ILIKE soltanto se la domanda è il sourceip normalizzato, non un IP in qualsiasi punto del payload.

## OPT02 - Classifica prima, raw dopo

```sql
SELECT qid, SUM(eventcount) AS N,
       MIN(starttime) AS Primo, MAX(starttime) AS Ultimo
FROM events
WHERE logsourceid = <LS_ID> AND sourceip = '<IP>'
GROUP BY qid
ORDER BY N DESC
START '<START>' STOP '<STOP>'
```

Primo passaggio per scegliere QID e intervallo; non fornisce prova testuale del payload.

## OPT03 - Raw sui candidati

```sql
SELECT starttime, sourceip, destinationip, qid,
       UTF8(payload) AS Raw
FROM events
WHERE logsourceid = <LS_ID> AND sourceip = '<IP>'
  AND qid = <QID>
ORDER BY starttime ASC
LIMIT 200
START '<START>' STOP '<STOP>'
```

Secondo passaggio; recuperare ogni candidato necessario e controllare troncamento al limite.

## OPT04 - Riscrittura diretta di Q076

```sql
SELECT sourceip, UNIQUECOUNT(destinationip) AS N
FROM events
WHERE logsourceid = <LS_FW>
GROUP BY sourceip
HAVING N >= 30
ORDER BY N DESC
LAST 15 MINUTES
```

Candidata equivalente a Q076 sullo stesso perimetro. Non è un benchmark eseguito.

## OPT05 - Sorgente IP, ramo A

```sql
SELECT starttime, logsourceid, sourceip, destinationip, qid
FROM events
WHERE sourceip = '<IP>'
START '<START>' STOP '<STOP>'
```

Primo ramo di un OR: unire al ramo B e deduplicare la sovrapposizione prima dei conteggi.

## OPT06 - Destinazione IP, ramo B

```sql
SELECT starttime, logsourceid, sourceip, destinationip, qid
FROM events
WHERE destinationip = '<IP>'
START '<START>' STOP '<STOP>'
```

Secondo ramo. Un indice in ciascun ramo non garantisce che due ricerche siano più rapide di una.

## OPT07 - Testo con filtro selettivo

```sql
SELECT starttime, sourceip, qid, UTF8(payload) AS Raw
FROM events
WHERE TEXT SEARCH '<TERM>'
  AND logsourceid = <LS_ID>
LIMIT 200
START '<START>' STOP '<STOP>'
```

Tokenizzazione e copertura dell’indice testuale possono differire da ILIKE: verificare campioni, punteggiatura e periodo indicizzato.
