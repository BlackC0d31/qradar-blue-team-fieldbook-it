# Indice delle query

| ID | Query |
|---|---|
| [Q001](../queries/Q001.aql) | Timeline essenziale di un IP |
| [Q002](../queries/Q002.aql) | Account esatto o indirizzo email |
| [Q003](../queries/Q003.aql) | Email nel testo grezzo |
| [Q004](../queries/Q004.aql) | Eventi collegati a una offense |
| [Q005](../queries/Q005.aql) | Offense con finestra ottimizzata |
| [Q006](../queries/Q006.aql) | Quali sorgenti vedono questo IP? |
| [Q007](../queries/Q007.aql) | Eventi dominanti per QID |
| [Q008](../queries/Q008.aql) | Deny verso una singola destinazione |
| [Q009](../queries/Q009.aql) | Esiti misti sullo stesso percorso |
| [Q010](../queries/Q010.aql) | Ricerca testuale indicizzata |
| [Q011](../queries/Q011.aql) | Dominio esatto nei DNS |
| [Q012](../queries/Q012.aql) | URL, Host e User-Agent |
| [Q013](../queries/Q013.aql) | Dettaglio flussi con un IP |
| [Q014](../queries/Q014.aql) | Ultimo evento di una sorgente |
| [Q015](../queries/Q015.aql) | Finestra assoluta riproducibile |
| [Q016](../queries/Q016.aql) | Anteprima del raw della sorgente |
| [Q017](../queries/Q017.aql) | Password spray per sorgente |
| [Q018](../queries/Q018.aql) | Brute force su un account |
| [Q019](../queries/Q019.aql) | Successi ed errori dello stesso utente |
| [Q020](../queries/Q020.aql) | Accessi RDP e credenziali esplicite |
| [Q021](../queries/Q021.aql) | Nuovi account e riabilitazioni |
| [Q022](../queries/Q022.aql) | Reset password e account modificati |
| [Q023](../queries/Q023.aql) | Aggiunta a gruppi sensibili |
| [Q024](../queries/Q024.aql) | Privilegi speciali su nuovi logon |
| [Q025](../queries/Q025.aql) | Ticket Kerberos: volume anomalo |
| [Q026](../queries/Q026.aql) | Preautenticazione Kerberos fallita |
| [Q027](../queries/Q027.aql) | Modifiche alle directory |
| [Q028](../queries/Q028.aql) | Operazioni directory da verificare |
| [Q029](../queries/Q029.aql) | Audit cancellato o policy cambiata |
| [Q030](../queries/Q030.aql) | Account di servizio usato da molte origini |
| [Q031](../queries/Q031.aql) | Autenticazioni IdP da IP e utenti |
| [Q032](../queries/Q032.aql) | Modifiche OAuth, consenso e credenziali |
| [Q033](../queries/Q033.aql) | Scansione verticale di porte |
| [Q034](../queries/Q034.aql) | Scansione orizzontale di host |
| [Q035](../queries/Q035.aql) | Movimento laterale da un server |
| [Q036](../queries/Q036.aql) | LDAPS negato: il caso porta 636 |
| [Q037](../queries/Q037.aql) | Egress escluso dalle reti note |
| [Q038](../queries/Q038.aql) | Trasferimenti prevalentemente in uscita |
| [Q039](../queries/Q039.aql) | Volume piccolo e ripetuto: candidati C2 |
| [Q040](../queries/Q040.aql) | Timeline per verificare un beacon |
| [Q041](../queries/Q041.aql) | DNS con molti nomi distinti |
| [Q042](../queries/Q042.aql) | DNS NXDOMAIN per client |
| [Q043](../queries/Q043.aql) | DNS con etichette molto lunghe |
| [Q044](../queries/Q044.aql) | Connessioni a resolver non approvati |
| [Q045](../queries/Q045.aql) | SMB o amministrazione verso l’esterno |
| [Q046](../queries/Q046.aql) | IP prima e dopo NAT |
| [Q047](../queries/Q047.aql) | Traffico VPN/DTLS da verificare |
| [Q048](../queries/Q048.aql) | BGP flap e reset di sessione |
| [Q049](../queries/Q049.aql) | Shell generata da Office |
| [Q050](../queries/Q050.aql) | Shell figlia di server Java |
| [Q051](../queries/Q051.aql) | PowerShell con argomenti codificati |
| [Q052](../queries/Q052.aql) | LOLBins con destinazioni remote |
| [Q053](../queries/Q053.aql) | msiexec e il falso positivo Citrix PVS |
| [Q054](../queries/Q054.aql) | Accesso a LSASS da processi insoliti |
| [Q055](../queries/Q055.aql) | Nuovi servizi e scheduled task |
| [Q056](../queries/Q056.aql) | Persistenza Unix nei log audit |
| [Q057](../queries/Q057.aql) | Download seguito da shell |
| [Q058](../queries/Q058.aql) | Tunnel e inoltri remoti |
| [Q059](../queries/Q059.aql) | Nuovo JSP scritto nel webroot |
| [Q060](../queries/Q060.aql) | Richieste verso file server-side sospetti |
| [Q061](../queries/Q061.aql) | Errori HTTP per endpoint |
| [Q062](../queries/Q062.aql) | Traversal in URI, anche codificato |
| [Q063](../queries/Q063.aql) | Attività Kubernetes amministrativa |
| [Q064](../queries/Q064.aql) | Rimozione log e disattivazione controlli |
| [Q065](../queries/Q065.aql) | Numero di righe contro numero di eventi |
| [Q066](../queries/Q066.aql) | Volume per bucket di cinque minuti |
| [Q067](../queries/Q067.aql) | Ritardo tra device e storage |
| [Q068](../queries/Q068.aql) | IP in reference set di hunting |
| [Q069](../queries/Q069.aql) | Enrichment dell’asset da mappa |
| [Q070](../queries/Q070.aql) | Tabella utenti: ruolo e reparto |
| [Q071](../queries/Q071.aql) | Host non autorizzati per account di servizio |
| [Q072](../queries/Q072.aql) | Successi per utenti con fallimenti recenti |
| [Q073](../queries/Q073.aql) | Sorgenti rare nella finestra |
| [Q074](../queries/Q074.aql) | Nuove destinazioni rispetto alla baseline |
| [Q075](../queries/Q075.aql) | Rapporto allow/deny con CASE |
| [Q076](../queries/Q076.aql) | Sottoquery FROM su candidati aggregati |
| [Q077](../queries/Q077.aql) | Accesso a dati accumulati GLOBALVIEW |
| [Q078](../queries/Q078.aql) | Identificare QID con parsing insufficiente |
| [Q079](../queries/Q079.aql) | Copertura di una proprietà custom |
| [Q080](../queries/Q080.aql) | Distribuzione dei dati tra domini |
| [Q081](../queries/Q081.aql) | Pivot su un IP indicatore parametrico |
| [Q082](../queries/Q082.aql) | WSO2: accessi a /fileupload |
| [Q083](../queries/Q083.aql) | WSO2: tracce upload e deployment |
| [Q084](../queries/Q084.aql) | IdP: chiamate SCIM e provisioning |
| [Q085](../queries/Q085.aql) | Pattern di comandi negli header SMTP |
| [Q086](../queries/Q086.aql) | Marker generici di comando e staging mail |
| [Q087](../queries/Q087.aql) | Contatti gateway mail verso un IOC fornito |
| [Q088](../queries/Q088.aql) | ESA: management e quarantine esposti |
| [Q089](../queries/Q089.aql) | Exchange: superfici web e PowerShell |
| [Q090](../queries/Q090.aql) | Exchange: worker web che genera shell |
| [Q091](../queries/Q091.aql) | Exchange ibrido: principal e certificati |
| [Q092](../queries/Q092.aql) | Outlook: figli di processo da investigare |
| [Q093](../queries/Q093.aql) | Allegati OneNote e dominio parametrico |
| [Q094](../queries/Q094.aql) | Pivot su User-Agent HTTP fornito |
| [Q095](../queries/Q095.aql) | Pivot DNS su domini forniti |
| [Q096](../queries/Q096.aql) | Endpoint RPC blockchain condivisi |
| [Q097](../queries/Q097.aql) | NetScaler: crash e modifiche sospette |
| [Q098](../queries/Q098.aql) | WSO2 2026: esiti JWT e autenticazione |
| [Q099](../queries/Q099.aql) | WSO2 2026: problemi del throttling |
| [Q100](../queries/Q100.aql) | Email gateway: anomalie oltre le firme |
| [Q101](../queries/Q101.aql) | OpenBMC/IPMI: origini verso UDP 623 |
| [Q102](../queries/Q102.aql) | Wing FTP: NUL codificato e log sessione |
| [Q103](../queries/Q103.aql) | Pivot richieste e sessioni ZoneMinder |
| [Q104](../queries/Q104.aql) | Expressway: accessi al servizio di cluster |
| [Q105](../queries/Q105.aql) | FortiOS: errori del servizio e modifiche |
| [Q106](../queries/Q106.aql) | Webex e porta 9000: verifica del contesto |
| [Q107](../queries/Q107.aql) | SNMP e NetBIOS da un host |
| [Q108](../queries/Q108.aql) | Stessa sessione IdP da IP diversi |
| [Q109](../queries/Q109.aql) | Regola WAF: riscontro con esito e path |
| [Q110](../queries/Q110.aql) | WSO2 VS Code: processi di test inattesi |
| [OPT01](../queries/OPT01.aql) | IP strutturato, output minimo |
| [OPT02](../queries/OPT02.aql) | Classifica prima, raw dopo |
| [OPT03](../queries/OPT03.aql) | Raw sui candidati |
| [OPT04](../queries/OPT04.aql) | Riscrittura diretta di Q076 |
| [OPT05](../queries/OPT05.aql) | Sorgente IP, ramo A |
| [OPT06](../queries/OPT06.aql) | Destinazione IP, ramo B |
| [OPT07](../queries/OPT07.aql) | Testo con filtro selettivo |
