# Contribuire

Mantieni stabili gli ID e modifica prima i cataloghi JSON canonici. Spiega domanda, telemetria, tipi dei campi, esempi positivi/negativi, limiti e riferimenti.

Usa record sintetici e indirizzi di documentazione. Non inviare log di lavoro, identità, token o indicatori di casi privati.

Gli strumenti runtime richiedono solo Python 3.10+. Per ricostruire i documenti installa `requirements-docs.txt`, poi esegui:

```bash
python tools/build_docs.py
python tools/release.py --refresh-manifest
python verify_package.py
python -m unittest discover -s tests -v
```

Revisiona le modifiche prima di aggiornare il manifest. Non rigenerare gli hash per nascondere differenze non spiegate.
Indica separatamente la validazione Ariel: i test offline non certificano sintassi o copertura sulla console.
