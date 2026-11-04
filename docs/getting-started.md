# Uso del repository

Template confrontati con documentazione e controllati offline. Non sono stati analizzati dal parser né eseguiti sulla tua installazione QRadar. Campi DSM, build, permessi e retention richiedono validazione locale.

## Scegli il percorso

Manuale: apri queries/Q001.aql, sostituisci <IP> e copia la SELECT nell’interfaccia corretta. Preparazione automatizzata: configura il JSON e usa render_query.py. Python è facoltativo per il percorso manuale.

## Estrai e verifica

Estrai l’archivio in una cartella nuova e apri il terminale nella radice del repository. Caricare lo ZIP come singolo file non pubblica un repository sorgente già estratto. Prima delle modifiche esegui verify_package.py.

## Avvio Kali/Linux

Gli strumenti runtime usano solo moduli della libreria standard Python. Per rendering e verifica non servono pip, ambiente virtuale o sudo.

## Avvio Windows

Estrai con Esplora file o Expand-Archive. Usa py -3 -X utf8 se il launcher è presente oppure python -X utf8. --output scrive direttamente UTF-8 ed evita le differenze di encoding della redirezione shell.

## File parametri

Per Q001 usa examples/params.ip.json, per finestre assolute examples/params.window.json. Copia in work/params.json e compila solo i valori richiesti. I null non usati sono ammessi. Formato START/STOP: yyyy-MM-dd HH:mm:ss, con STOP successivo.

## Controlla il risultato

Verifica che non rimangano <...>, che il tempo sia corretto e che esistano i campi Hunt_*. --output non sovrascrive un file esistente senza --force. Se serve, cambia LAST manualmente nella copia di lavoro.

## Proprietà custom

Il renderer non rinomina Hunt_Action, Hunt_URI o altri campi. Rimappa nome e significato della proprietà. deny/drop/blocked sono convenzioni, non valori universali del vendor.

## Esegui e conserva

Copia la SELECT in Log Activity o Network Activity. Prova un evento noto su una finestra breve. Conserva query finale, timezone, source ID, limiti di output, risultati e lacune di copertura.

## Risolvi gli errori

Parametro mancante: compila la chiave. JSON o chiavi duplicate: correggi il file. ID sconosciuto: Q001, non Q1. Output esistente: cambia percorso o usa --force. Zero righe: verifica tempo, NAT, sorgente, dominio e retention.

## Lavoro avanzato

--list elenca gli ID e --show visualizza i metadati. OPT01-OPT07 sono varianti da valutare, non upgrade automatici. Compila docs/benchmark-template.md con scope equivalenti e misure locali.

```bash
python3 verify_package.py
python3 render_query.py --list
python3 render_query.py Q001 --params examples/params.ip.json --output work/Q001.aql
```

```powershell
py -3 -X utf8 verify_package.py
py -3 -X utf8 render_query.py Q001 --params examples/params.ip.json --output work/Q001.aql
```
