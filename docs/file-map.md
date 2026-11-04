# Mappa dei file

| File | Uso |
|---|---|
| queries/*.aql | 117 template testuali separati, non un formato di importazione massiva QRadar. |
| queries.json / variants.json | Cataloghi canonici usati dal renderer e dalla documentazione generata. |
| parameter_schema.json | Tipi dei parametri ed esempi sintetici, non configurazione QRadar. |
| params.example.json / examples/ | Modello vuoto e piccoli input dimostrativi con indirizzi di documentazione. |
| fieldbook.py / render_query.py | Validazione e preparazione locali; nessuna connessione o esecuzione AQL. |
| verify_package.py / MANIFEST.sha256.json | Coerenza cataloghi/file e integrità della release. |
| docs/*.md / docs/pdf/ | Manuale, atlante, guide uso/prestazioni modificabili e tre PDF pronti. |
| docs/assets/ | Identità grafica vettoriale e diagrammi concettuali originali. |
| tests/ / .github/workflows/ | Test offline e workflow CI fornito. |
| tools/build_docs.py / tools/release.py | Ricostruzione AQL/Markdown/PDF e aggiornamento esplicito del manifest. |
| requirements-docs.txt | Dipendenza opzionale bloccata per i PDF; non serve agli strumenti runtime. |
| LICENSE / NOTICE / CONTRIBUTING.md | Licenza MIT, attribuzioni, limiti di validazione e politica dei contributi. |
