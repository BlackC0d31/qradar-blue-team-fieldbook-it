# GitHub



## Parti da un repository vuoto

Crea su GitHub un repository con nome e visibilità scelti. Per il primo push Git non inizializzare il remoto con README, licenza o .gitignore concorrenti: il pacchetto li include già.

## Estrai l’edizione corretta

Usa questa edizione come radice di un repository. README.md, script e .github devono essere alla radice. Caricare il solo ZIP conserva un archivio, senza estrarre il progetto.

## Verifica prima del commit

Esegui verificatore e test. Mantieni params.json reali, output, raw log e credenziali nelle posizioni locali ignorate. Gli esempi distribuiti usano indirizzi di documentazione e parametri generici.

## Inizializza e crea il commit

Esegui i comandi dalla radice estratta. Se Git richiede un’identità, usa la tua configurazione. Non sono inclusi account o credenziali.

## Collega e invia

Sostituisci OWNER/REPOSITORY nell’URL con il tuo repository vuoto. Autenticati con il metodo GitHub configurato e invia main. Non usare force-push per risolvere un non-fast-forward.

## Controlla il primo avvio

Dopo il push apri Actions e verifica Offline checks. I comandi sono provati localmente; l’esito di un’esecuzione ospitata non può essere affermato prima che avvenga nel tuo repository.

## Crea una release

Usa tag v2.0.0 e RELEASE.md come descrizione iniziale. Sorgenti e PDF sono inclusi. Il manifest verifica coerenza, non autenticità indipendente o firma digitale.

## Alternativa browser

Con questo numero di file e i workflow nascosti, Git o GitHub Desktop sono più affidabili dei caricamenti individuali. Se usi il browser, carica il contenuto estratto in lotti supportati e verifica esplicitamente .github/workflows, tests e docs.

```bash
python3 verify_package.py
python3 -m unittest discover -s tests -v
git init -b main
git add .
git commit -m "Release v2.0.0"
git remote add origin https://github.com/OWNER/REPOSITORY.git
git remote -v
git push -u origin main
```

OWNER/REPOSITORY: sostituisci con il tuo repository vuoto.

[GitHub documentation](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)
