# Registro di validazione

Preparazione: 2026-11-04. Ambiente locale: Python 3.12.14, Linux.

- Superati 11 test offline, compreso il rendering dei 117 template con parametri sintetici dello schema.
- Verificati UTF-8/BOM, chiavi JSON duplicate, parametri non validi, ordine date, protezione dalla sovrascrittura e output in caso di errore CLI.
- Superati i controlli di coerenza file/cataloghi, link Markdown locali e bilanciamento strutturale di apici/parentesi.
- Renderizzati i tre PDF per la revisione; controllati limiti del testo e pagine campione.
- La verifica della release pubblica non ha rilevato identificatori dei casi privati o riferimenti all’organizzazione operativa nei testi/PDF.

Sono controlli locali di software e documentazione. Non sono stati eseguiti parser Ariel, connessioni QRadar o job GitHub Actions ospitati. La matrice fornita prevede Python 3.10/3.13 su Linux/Windows: gli esiti reali vanno verificati dopo il caricamento.

Il manifest verifica coerenza, non costituisce firma digitale o autenticità indipendente.
