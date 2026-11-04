# Sicurezza e gestione dei dati

Gli strumenti generano testo localmente: non contengono connettori QRadar, credenziali o raccolte pianificate.
Per possibili vulnerabilità degli strumenti usa la segnalazione privata se abilitata dal proprietario. Non pubblicare segreti o dati operativi nelle issue.

Il renderer rifiuta volutamente letterali ambigui con apici, backslash o caratteri di controllo. Identità complesse e ricerche IPv6 richiedono adattamento manuale revisionato allo schema locale. Wildcard LIKE/ILIKE e tokenizzazione TEXT SEARCH restano semantica della query, non indicatori validati.

Gli hash di integrità non sono firme digitali. Esiti GitHub Actions e risultati Ariel reali vanno distinti dai controlli locali.
