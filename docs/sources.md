# Fonti

## S01 - IBM · Struttura ed esempi AQL

https://www.ibm.com/docs/en/qsip/7.5.0?topic=structure-sample-aql-queries
Indice web ufficiale; fetch diretto parzialmente 403.

## S02 - IBM · Esempi eventi e flussi

https://www.ibm.com/docs/en/qsip/7.4.0?topic=language-events-flows-query-examples
Esempi ufficiali; adattamento originale delle ricerche.

## S03 - IBM · Calcolo e formattazione

https://www.ibm.com/docs/en/qsip/7.5.0?topic=language-aql-data-calculation-formatting-functions
UTF8, DATEFORMAT, LONG; testo indicizzato ufficiale.

## S04 - IBM · Funzioni di recupero dati

https://www.ibm.com/docs/en/qsip/7.5.0?topic=language-aql-data-retrieval-functions
INOFFENSE, OFFENSE_TIME e reference data; indicizzazione ufficiale.

## S05 - IBM · Aggregazioni AQL

https://www.ibm.com/docs/en/qradar-on-cloud?topic=language-aql-data-aggregation-functions
COUNT, SUM, UNIQUECOUNT, STDEV e HAVING.

## S06 - IBM · Operatori AQL

https://www.ibm.com/docs/en/qradar-on-cloud?topic=language-aql-logical-comparison-operators
TEXT SEARCH, ILIKE, MATCHES; documentazione ufficiale.

## S07 - IBM · Campi events e flows

https://www.ibm.com/docs/en/qsip/7.5.0?topic=language-event-flow-simarc-fields-aql-queries
Schema standard; verificare supporto del collector.

## S08 - IBM · Criteri temporali

https://www.ibm.com/docs/en/qsip/7.4.0?topic=language-time-criteria-in-aql-queries
LAST, START/STOP e millisecondi.

## S09 - IBM · Proprietà custom

https://www.ibm.com/docs/en/qradar-on-cloud?topic=properties-creating-custom-property
Le proprietà Hunt_* di questo libro sono convenzioni locali da creare o rimappare.

## S10 - IBM · Monitoraggio utenti e rete

https://www.ibm.com/docs/en/qradar-on-cloud?topic=language-user-network-monitoring-query-examples
Esempi di aggregazioni per rete e identità.

## S11 - IBM · Sottoquery AQL

https://www.ibm.com/docs/en/qradar-on-cloud?topic=language-aql-subquery
FROM e IN; una colonna IN e massimo 10.000 risultati interni.

## S12 - IBM · Prestazioni filtri testuali

https://www.ibm.com/support/pages/ariel-contains-filter-performs-case-insensitive-match-and-less-efficient-matches-filter-qradar
Case sensitivity e costo relativo; evitare equivalenze universali.

## S13 - IBM · Release 7.5 UP11

https://www.ibm.com/support/pages/release-qradar-750-update-package-11-sfs-202161120250122185136
Esempio di fix su reference map ed eventi offense: conta la build.

## S14 - IBM · Events FAQ / coalescing

https://www.ibm.com/docs/en/qradar-on-cloud?topic=problems-events-faq
Coalescenza, conteggi e raw rappresentativi.

## S15 - Microsoft · Windows Security events

https://learn.microsoft.com/azure/sentinel/windows-security-event-id-reference
Catalogo dei tipi di evento; query AQL originali, non query Sentinel copiate.

## S16 - Microsoft · Exchange hybrid security

https://techcommunity.microsoft.com/blog/exchange/exchange-server-security-changes-for-hybrid-deployments/4396833
Articolo Exchange Team aggiornato il 7 maggio 2026.

## S17 - Microsoft · Sysmon

https://learn.microsoft.com/sysinternals/downloads/sysmon
Telemetria processi, file e ProcessAccess; policy e configurazione determinano copertura.

## S18 - IBM · Esempi reference data

https://www.ibm.com/docs/en/qsip/7.6.0?topic=language-reference-data-query-examples
Consultato come riferimento aggiuntivo; verificare disponibilità in 7.5.

## S19 - IBM · Logica condizionale

https://www.ibm.com/docs/fr/qsip/7.5.0?topic=language-conditional-logic-in-aql-queries
IF/CASE nel motore AQL; comportamento dei report da validare separatamente.

## S20 - IBM · GLOBALVIEW

https://www.ibm.com/docs/it/qsip/7.5.0?topic=tasks-accessing-globalview-database
Accesso a saved search accumulate; dipendenza dallo schema della vista.

## S21 - IBM · API POST Ariel searches

https://ibmsecuritydocs.github.io/qradar_api_28.0/28.0--ariel-searches-POST.html
Ricerca asincrona; versione API da adattare alla console.

## S22 - IBM · API stato e risultati

https://ibmsecuritydocs.github.io/qradar_api_15.0/15.0--ariel-searches-search_id-GET.html
Reference endpoint; non è una prescrizione della versione API 15.

## S23 - IBM · Event processing performance

https://www.ibm.com/docs/en/qradar-on-cloud?topic=problems-event-processing-performance
Ottimizzazione delle proprietà e pipeline.

## S24 - IBM · Ricerche offense lente

https://www.ibm.com/support/pages/slow-offense-linked-eventflow-searches-qradar-due-missing-domain-or-offense-source-indexes
Indici dominio/offense e limiti delle ricerche correlate.

## V01 - WSO2 · CVE-2022-29464

https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2022/WSO2-2021-1738/
Advisory originale WSO2; Identity Server 5.8.0 elencato.

## V02 - NIST NVD · CVE-2022-29464

https://nvd.nist.gov/vuln/detail/cve-2022-29464
Dettagli fileupload e traversal; rimandi a exploit e KEV.

## V03 - WSO2 · SCIM authorization

https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2019/WSO2-2019-0656/
Advisory che indica 5.8.0 o superiore come non affetto da quel problema specifico.

## V04 - Cisco · CVE-2025-20393

https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sma-attack-N9bf4
Advisory letto; HTTP Spam Quarantine, RCE root e release corrette.

## V05 - Citrix · CTX697096

https://support.citrix.com/external/article?articleNumber=CTX697096
CVE-2026-88771/88772 e altre; testo vendor letto, sfruttamento osservato dichiarato.

## V06 - CERT-EU · Exchange CVE-2025-53786

https://cert.europa.eu/publications/security-advisories/2025-030/
Advisory istituzionale e collegamenti Microsoft; richiede admin on-prem.

## V07 - WSO2 · CVE-2026-5430

https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2026-5328/
Pubblicato 3 maggio 2026; bypass JWT su prodotti/versioni esplicitamente elencati.

## V08 - WSO2 · CVE-2026-4249

https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2026-5236/
Pubblicato 3 maggio 2026; DoS persistente nel throttling.

## V09 - WSO2 · CVE-2026-19515

https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2026-5854/
Pubblicato 15 settembre 2026; estensione MI VS Code, non Identity Server.

## V10 - Google Security Research · OpenBMC

https://github.com/google/security-research/security/advisories/GHSA-gg9x-v835-m48q
Ricerca originale CVE-2021-39296 con PoC pubblico; non eseguito.

## V11 - RCE Security · Wing FTP

https://www.rcesecurity.com/2025/06/what-the-null-wing-ftp-server-rce-cve-2025-47812/
Ricerca originale CVE-2025-47812 con dettagli e PoC; non eseguito.

## V12 - Cisco · CVE-2026-76466

https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vcs-static-cred-hr7EWZ8t
21 ottobre 2026; Expressway cluster, RPC/cookie e comandi root.

## V13 - NHS England · Fortinet CC-4736

https://digital.nhs.uk/cyber-alerts/2026/cc-4736
Advisory istituzionale con aggiornamento 9 settembre 2026; PSIRT FG-IR-25-084 non leggibile direttamente.

## V14 - NIST NVD · Outlook CVE-2026-78509

https://nvd.nist.gov/vuln/detail/cve-2026-78509
Solo record indicizzato leggibile: heap overflow Outlook. Fetch diretto senza testo; MSRC richiede JavaScript.

## V15 - Microsoft MSRC · CVE-2026-78509

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-78509
Pagina individuata ma dettagli non leggibili: non usata per affermare PoC, zero-click o sfruttamento.

## P01 - IBM - Index Management 7.5

https://www.ibm.com/docs/en/qsip/7.5.0?topic=tasks-index-management
Indici come filtro dei dati e costo di spazio; testo ufficiale indicizzato.

## P02 - IBM - Indexing best practices

https://www.ibm.com/docs/en/qradar-common?topic=app-indexing-best-practices
Indici delle proprietà e dati storici; contesto documentale Advisor.

## P03 - IBM - Event processing performance

https://www.ibm.com/docs/en/qradar-on-cloud?topic=problems-event-processing-performance
Parsing, proprietà e cardinalità delle global view.

## P04 - IBM - AQL subquery

https://www.ibm.com/docs/en/qradar-on-cloud?topic=language-aql-subquery
Dipendenze tra subquery e query esterna; limite dei risultati IN.

## P05 - IBM - Search status API

https://ibmsecuritydocs.github.io/qradar_api_15.0/15.0--ariel-searches-search_id-GET.html
Stati, processed_record_count, record_count e query_execution_time; verificare unità e campi nella API locale.

## P06 - IBM - AQL retrieval functions

https://www.ibm.com/docs/en/qsip/7.5.0?topic=language-aql-data-retrieval-functions
OFFENSE_TIME, reference data, GLOBALVIEW e scope dei processor.

## P07 - IBM - Resource restrictions

https://www.ibm.com/docs/en/qsip/7.5.0?topic=searches-resource-restrictions-in-distributed-environments
I nodi distribuiti e il trasferimento dei risultati possono influire sulla ricerca; testo indicizzato.

## P08 - IBM - AQL logical/comparison operators

https://www.ibm.com/docs/en/qradar-on-cloud?topic=language-aql-logical-comparison-operators
LIMIT e vincoli TEXT SEARCH; riferimento della sintassi.

## P09 - IBM - Indexed properties and Quick Filters

https://www.ibm.com/support/pages/how-use-indexed-properties-and-quick-filters-faster-searches-ibm-qradar-siem
Supporto IBM per indicizzazione e ricerca testuale.

## P10 - IBM - Globalview database

https://www.ibm.com/docs/it/qsip/7.5.0?topic=tasks-accessing-globalview-database
Accesso alle viste accumulate tramite API e schema della saved search.

## G01 - Scenario didattico generico


Esempio ipotetico con parametri e indirizzi di documentazione; nessun incidente reale o indicatore verificato.
