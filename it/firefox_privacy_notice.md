## Informativa sulla privacy di <span class="privacy-header-firefox">Firefox</span> <span class="privacy-header-policy"></span>

*In vigore dal 30 settembre 2021*
{: datetime="2021-09-30" }

## Noi di Mozilla riteniamo che la salvaguardia della privacy sia fondamentale per un buon funzionamento di Internet.

Per questo Firefox, così come tutti i nostri prodotti, sono stati creati in modo da offrire agli utenti maggiore controllo sulle informazioni condivise online e con noi. Facciamo il possibile per raccogliere solo i dati strettamente necessari per migliorare Firefox per tutti.

In questa Informativa sulla privacy, spieghiamo quali sono i dati che Firefox condivide e aiutiamo gli utenti a configurare impostazioni per condividerne ancora meno. Per quanto riguarda il modo in cui riceviamo, gestiamo e condividiamo le informazioni raccolte tramite Firefox, rispettiamo inoltre le prassi indicate nell'[Informativa sulla privacy di Mozilla](https://www.mozilla.org/privacy/).

## Per impostazione predefinita, Firefox condivide dati per le seguenti finalità:

### Miglioramento di prestazioni e stabilità per gli utenti, ovunque {: #health-report }

* __Dati relativi alle interazioni__: Firefox ci invia dati sulle interazioni degli utenti con Firefox (come numero di schede e finestre aperte, numero di pagine Web visitate, numero e tipo di componenti aggiuntivi di Firefox installati e durata delle sessioni) e con le funzioni di Firefox offerte da Mozilla o dai nostri partner (come interazioni con le funzionalità di ricerca di Firefox e riferimenti dei partner di ricerca).

* __Dati tecnici__: Firefox ci invia dati sulla versione di Firefox installata e sulle preferenze linguistiche, sul sistema operativo del dispositivo utilizzato, sulla sua configurazione hardware e sulla memoria, informazioni di base su arresti anomali ed errori e sul risultato di processi automatizzati come aggiornamenti, Safe Browsing e attivazione dei nostri servizi. Quando Firefox ci invia dei dati, l'indirizzo IP dell'utente viene temporaneamente acquisito dai nostri registri del server.

Leggere la documentazione relativa alla telemetria per dispositivi [desktop](https://firefox-source-docs.mozilla.org/toolkit/components/telemetry/telemetry/index.html), [Android](https://dictionary.telemetry.mozilla.org/apps/fenix) o [iOS](https://github.com/mozilla-mobile/firefox-ios/wiki/Telemetry), oppure vedere come rifiutare questa raccolta di dati su dispositivi [desktop](https://support.mozilla.org/en-US/kb/share-data-mozilla-help-improve-firefox?redirectlocale=en-US&redirectslug=send-performance-data-improve-firefox) e [mobili](https://support.mozilla.org/en-US/kb/send-usage-data-firefox-mobile-browsers).
{: #telemetry }

### Ricerca {: #defaultsearch }

Le ricerche in Firefox possono essere eseguite da diversi punti, come la barra degli indirizzi, la barra di ricerca e la pagina Nuova scheda. Riceviamo dati sulle interazioni dell'utente con la funzione di ricerca in Firefox e sul numero di ricerche effettuate tramite i nostri partner di ricerca. 

* __Dati sulla posizione__: al primo utilizzo di Firefox, l'indirizzo IP dell'utente viene usato per configurare il provider di servizi di ricerca predefinito in base al Paese. [Per saperne di più](https://support.mozilla.org/kb/change-your-default-search-settings-firefox).

* __Query di ricerca__: se viene selezionato un provider che supporta i suggerimenti di ricerca, per impostazione predefinita, Firefox invia le richieste al provider di servizi di ricerca per aiutare l'utente a scoprire frasi comuni usate nelle ricerche da altri e migliorare l'esperienza di ricerca. [Ulteriori informazioni](https://support.mozilla.org/kb/search-suggestions-firefox) che includono come disattivare questa funzione. Se viene abilitato Firefox Suggest, noi e i nostri partner potremmo anche ricevere le query di ricerca dell'utente. [Ulteriori informazioni di seguito](#searches). 

### Suggerimento di contenuti rilevanti

Firefox visualizza contenuti, come componenti aggiuntivi consigliati, siti principali (siti Web proposti da Mozilla ai nuovi utenti di Firefox) e contenuti consigliati di Pocket (parte della famiglia Mozilla).

* __Dati sulla posizione__: Firefox usa l'indirizzo IP dell'utente per suggerire contenuti rilevanti in base al Paese.

* __Dati tecnici e sulle interazioni__: Firefox ci invia dati come posizione, dimensione e collocazione dei contenuti che suggeriamo, così come dati di base sulle interazioni dell'utente con tali contenuti. Ciò include il numero di volte che i contenuti vengono visualizzati o selezionati mediante clic.

* __Contenuti consigliati di Pocket__: suggeriamo contenuti sulla base di cronologia di navigazione, lingua e posizione geografica. L'elaborazione della scelta delle storie da visualizzare avviene a livello locale nella copia di Firefox in uso e né Mozilla né Pocket ricevono una copia della cronologia di navigazione. Per favorire la visualizzazione di contenuti consigliati di Pocket pertinenti sulla base della posizione geografica, Firefox condivide i dati sulla lingua e sul Paese con Pocket.

    Mozilla e Pocket ricevono unicamente dati in forma aggregata sui suggerimenti visualizzati e su cui si fa clic. Condividiamo inoltre dati in forma aggregata sui contenuti sponsorizzati visualizzati e su cui si fa clic con la nostra piattaforma di terze parti Adzerk, affinché gli inserzionisti possano vedere quante persone hanno fatto clic sui loro articoli. Questi dati aggregati non ci permettono di identificare gli utenti.

* __Siti principali__: quando si fa clic sulla tile di un sito principale sponsorizzato nella scheda Novità, condividiamo i dati su Paese, area geografica, contea (per gli Stati Uniti) e ora in cui è stato fatto clic con AdMarketplace (una piattaforma di riferimento di terze parti) per confermare l'avvenuta navigazione al sito. Firefox non condivide l'indirizzo IP dell'utente o qualsiasi altra informazione identificabile.

* __Funzioni e componenti aggiuntivi consigliati__: i componenti aggiuntivi consigliati possono essere visualizzati nella pagina Gestione estensioni (about:addons) e nella barra degli indirizzi, dove è possibile effettuare ricerche o digitare URL. Nella barra degli indirizzi possiamo anche consigliare funzioni Firefox. I consigli visualizzati nella pagina about:addons si basano su un cookie. Mentre i consigli visualizzati nella barra degli indirizzi si basano sulle interazioni dell'utente con Firefox. Mozilla non riceve la cronologia di navigazione. La scelta dei contenuti da visualizzare avviene a livello locale nella copia in uso di Firefox. Ulteriori informazioni sui [contenuti consigliati nella barra degli indirizzi](https://support.mozilla.org/kb/extension-recommendations) o nella [pagina Gestione estensioni](https://support.mozilla.org/kb/personalized-extension-recommendations).

### Miglioramento della sicurezza degli utenti ovunque {: #security }

**Dati delle pagine Web al servizio DNS ricorsivo**: per alcuni utenti di Firefox negli Stati Uniti, Firefox indirizza le richieste DNS a un servizio ricorsivo che ha accettato di aderire ai [rigidi standard di riservatezza di Mozilla per i servizi DNS ricorsivi](https://wiki.mozilla.org/Security/DOH-resolver-policy). Questo servizio garantisce una protezione aggiuntiva dalle violazioni della privacy alle reti locali, oltre che da alcuni attacchi alla sicurezza DNS. I registri di sistema delle richieste DNS vengono cancellati dal servizio entro 24 ore e sono utilizzati esclusivamente per finalità di risoluzione DNS. Maggiori informazioni sono disponibili [qui](https://support.mozilla.org/kb/firefox-dns-over-https#w_switching-providers) oppure nei siti dei nostri provider di servizi DNS ricorsivi elencati di seguito:

* [__Cloudflare__](https://developers.cloudflare.com/1.1.1.1/privacy/firefox/)
* [__NextDNS__](https://nextdns.io/privacy)
* [__Comcast__](https://www.xfinity.com/privacy/policy/dns)

**Dati tecnici per gli aggiornamenti**: le versioni desktop di Firefox verificano la disponibilità di aggiornamenti del browser connettendosi continuamente ai server Mozilla. La versione di Firefox in uso, la lingua selezionata e il sistema operativo del dispositivo sono utilizzati per applicare gli aggiornamenti corretti. Le versioni di Firefox per dispositivi mobili possono connettersi a un altro servizio, se ne è stato utilizzato uno per scaricare e installare Firefox. [Per saperne di più](https://support.mozilla.org/kb/how-stop-firefox-automatically-making-connections#w_auto-update-checking).
{: #auto-updates }

**Dati tecnici per l'elenco di blocco dei componenti aggiuntivi**: Firefox per desktop e Android si connettono periodicamente a Mozilla per proteggere gli utenti da componenti aggiuntivi dannosi. La versione e la lingua di Firefox, il sistema operativo del dispositivo e l'elenco dei componenti aggiuntivi installati sono necessari per applicare e aggiornare l'elenco di blocco dei componenti aggiuntivi. [Per saperne di più](https://support.mozilla.org/kb/how-stop-firefox-making-automatic-connections).

**Dati tecnici e delle pagine Web per il servizio Google Safe Browsing**: per proteggere gli utenti da download dannosi, Firefox invia informazioni di base su download sconosciuti al servizio Google Safe Browsing, includendo il nome del file e l'URL da cui è stato scaricato. Per saperne di più [leggere qui](https://support.mozilla.org/kb/how-does-phishing-and-malware-protection-work) o consultare l'[Informativa sulla privacy di Google](https://www.google.com/policies/privacy/). La disattivazione di queste opzioni impedisce a Firefox di inviare segnalazioni sul pericolo di siti Web o file scaricati potenzialmente illegali o dannosi.

**Dati tecnici e delle pagine Web per le Autorità di certificazione**: quando viene visitato un sito Web sicuro (generalmente identificato da un URL che inizia con "HTTPS"), Firefox convalida il [certificato](https://support.mozilla.org/kb/secure-website-certificate) del sito Web. Questa procedura può comportare l'invio, da parte di Firefox, di determinate informazioni sul sito Web all'Autorità di certificazione identificata dal sito Web. La disattivazione di questa funzione, può aumentare il rischio di intercettazione di informazioni private. [Per saperne di più](https://support.mozilla.org/kb/advanced-settings-browsing-network-updates-encryption#w_certificates-tab).

### Segnalazioni di arresti anomali {: #crash-reporter }
Per impostazione predefinita, nelle versioni desktop di Firefox viene chiesto di inviare a Mozilla una segnalazione con maggiori dettagli in caso di arresto anomalo, ma è sempre possibile scegliere di non farlo.

* __Dati sensibili__:  le segnalazioni di arresti anomali includono un "file di dump" dei contenuti della memoria di Firefox al momento dell'arresto che può contenere dati personali sensibili dell'utente.

* __Dati delle pagine Web__:  le segnalazioni di arresti anomali includono l'URL attivo al momento dell'arresto.

* __Dati tecnici__:  le segnalazioni di arresti anomali includono dati sul motivo dell'arresto anomalo di Firefox e sullo stato della memoria del dispositivo e sulla sua esecuzione al momento dell'arresto.

Leggere la documentazione completa [qui](https://firefox-source-docs.mozilla.org/toolkit/crashreporter/crashreporter/index.html).

### Misurazione e supporto delle nostre campagne marketing

* __Dati sulle campagne e di riferimento__: questi dati aiutano Mozilla a comprendere l'efficacia delle campagne marketing.
{: #referraltracking }

    _Su desktop_: Per impostazione predefinita, Firefox invia a Mozilla dati HTTP che possono essere inclusi nel programma di installazione di Firefox. Questi dati ci consentono di determinare il dominio del sito Web o la campagna marketing (se pertinente) che ha portato l'utente alla nostra pagina di download. Leggere la [documentazione](https://firefox-source-docs.mozilla.org/toolkit/components/telemetry/telemetry/data/environment.html#attribution) al riguardo oppure [disattivare l'opzione](https://support.mozilla.org/kb/desktop-privacy) before installation.

    _Su Android_: Firefox invia per impostazione predefinita dati sulle campagne pubblicitarie mobili ad Adjust, il nostro fornitore di analytics, che ha una sua [informativa sulla privacy](https://www.adjust.com/terms/privacy-policy/). I dati sulle campagne pubblicitarie mobili includono: ID pubblicitario Google, indirizzo IP, indicatore temporale, Paese, lingua/impostazioni locali, sistema operativo e versione dell'app. Per saperne di più, leggere la [documentazione](https://dictionary.telemetry.mozilla.org/apps/fenix?itemType=metrics&page=1&search=adjust).
{: #thirdparty }

---

## Se si usano queste funzioni, Firefox condividerà alcuni dati per fornire le funzionalità e per aiutarci migliorare i nostri prodotti e servizi: {: #optional-features }

### Firefox Suggest {: #searches }

Mozilla sta sviluppando una nuova funzione che ci aiuta a fornire agli utenti informazioni migliori più facilmente. La funzione è chiamata Firefox Suggest e una sua prima versione è al momento disponibile per gli utenti negli Stati Uniti. Firefox Suggest mostra contenuti consigliati e sponsorizzati. Nell'ambito di questa funzione, ci impegniamo a limitare la possibilità di identificare gli utenti da parte nostra e dei nostri partner. [Ulteriori informazioni](https://support.mozilla.org/en-US/kb/navigate-web-faster-firefox-suggest?as=u&utm_source=inproduc) che includono come attivare e disattivare questa funzione.

Per migliorare l'esperienza di navigazione degli utenti, così come il prodotto stesso, Firefox condivide le seguenti informazioni:

* __Ricerche__: Firefox invia a Mozilla il contenuto che viene digitato nella barra di ricerca e Mozilla può condividere tali dati con i propri [partner](https://support.mozilla.org/en-US/kb/navigate-web-faster-firefox-suggest?as=u&utm_source=inproduc#w_who-are-mozillas-partners).. 

* __Siti visitati__: per i suggerimenti su cui si fa clic, Firefox invia a Mozilla l'URL del sito Web e Mozilla può condividere tali dati con i propri [partner](https://support.mozilla.org/en-US/kb/navigate-web-faster-firefox-suggest?as=u&utm_source=inproduc#w_who-are-mozillas-partners).

* __Dati sulla posizione__: Firefox invia a Mozilla l'indirizzo IP dell'utente che utilizziamo per suggerire contenuti in base a Paese, stato e città. Mozilla può condividere informazioni relative alla posizione dell'utente con i nostri partner, che però non riceveranno l'indirizzo IP dell'utente. 

* __Dati tecnici e sulle interazioni__: Firefox invia a Mozilla dati come il numero di volte in cui Firefox suggerisce o visualizza contenuti su cui poi viene fatto clic, così come informazioni di base sulle interazioni con Firefox Suggest. Mozilla condivide con i nostri [partner](https://support.mozilla.org/en-US/kb/navigate-web-faster-firefox-suggest?as=u&utm_source=inproduc#w_who-are-mozillas-partners) informazioni quali il numero di volte in cui i suggerimenti vengono visualizzati e selezionati per finalità di verifica e miglioramento della funzione. 


### Account Firefox

* __Dati di registrazione__: quando si crea un account Firefox o ci si registra a Firefox, Mozilla riceve l'indirizzo email e un hash della password. È possibile scegliere se includere un nome da visualizzare o un'immagine del profilo. L'indirizzo email viene inviato al nostro fornitore di servizi email, Acoustic, che ha una sua [informativa sulla privacy](https://acoustic.com/privacy-notice/).

* __Dati sulla posizione__: per finalità di sicurezza, memorizziamo gli indirizzi IP utilizzati per accedere all'account Firefox, allo scopo di individuare la città e il Paese dell'utente. Utilizziamo tali dati per inviare avvisi email in caso vengano rilevate attività sospette, come accessi all'account da altre località.

* __Dati relativi alle interazioni__: riceviamo dati come informazioni sulle visite al sito Web degli account Firefox, dashboard e preferenze di menu, sui prodotti e servizi che vengono utilizzati in relazione all'account Firefox e sulle interazioni con i nostri messaggi email e SMS. Tali dati ci servono per comprendere come gli utenti utilizzano i nostri prodotti e servizi e per inviare loro suggerimenti e messaggi più pertinenti in relazione all'account Firefox.

* __Dati tecnici__: per visualizzare i dispositivi che sono sincronizzati con l'account Firefox e per finalità di sicurezza, memorizziamo informazioni su sistema operativo del dispositivo, tipo e versione del browser, indicatore temporale e impostazioni locali e le stesse informazioni vengono memorizzate per tutti i dispositivi connessi all'account. Se l'account Firefox viene utilizzato per accedere ad altri siti Web o servizi (come AMO o Pocket), riceviamo l'indicatore temporale di tali accessi.

È possibile leggere la documentazione completa oppure trovare ulteriori informazioni su come gestire i dati dell'account Firefox o le nostre prassi in merito ai dati di [siti Web e email](https://www.mozilla.org/privacy/websites/). È inoltre possibile consultare le informative sulla privacy dei nostri servizi connessi all'account Firefox, che sono:

* [Firefox Lockwise](https://support.mozilla.org/kb/firefox-lockwise-and-privacy)
* [Firefox Monitor](https://www.mozilla.org/privacy/firefox-monitor)
* [Firefox Notes](https://addons.mozilla.org/firefox/addon/notes-by-firefox/)
* [Firefox Send](http://send.firefox.com/legal)
* [Firefox Sync](https://www.mozilla.org/privacy/firefox/#sync)

### Sync {: #sync }

* __Dati sincronizzati__: se si abilita Sync, Mozilla riceverà le informazioni che vengono sincronizzate sui vari dispositivi in formato crittografato. Tali informazioni possono includere schede Firefox, componenti aggiuntivi, password, informazioni di pagamento compilate automaticamente, segnalibri, cronologia e preferenze. Eliminando l'account Firefox, verranno eliminati tutti i contenuti Firefox Sync correlati. È anche possibile consultare la [documentazione](https://moz-services-docs.readthedocs.io/en/latest/sync/).

* __Dati tecnici e sulle interazioni__: se si abilita Sync, Firefox invierà periodicamente tramite telemetria informazioni di base sull'ultimo tentativo di sincronizzazione dei dati, come data e ora della sincronizzazione, esito e tipo di dispositivo che si è tentato di sincronizzare. È anche possibile consultare la [documentazione](https://firefox-source-docs.mozilla.org/toolkit/components/telemetry/telemetry/data/sync-ping.html).

[Ulteriori informazioni](https://support.mozilla.org/kb/how-do-i-set-sync-my-computer) che includono come attivare e disattivare la sincronizzazione.

### Localizzazione {: #location-services }

* __Dati relativi alla posizione al servizio di geolocalizzazione di Google__: Firefox chiede sempre il consenso prima di determinare e condividere la posizione dell'utente con un sito Web che la richiede (ad esempio, se un sito di mappe necessita della posizione di partenza per fornire delle indicazioni stradali). Per determinare la posizione, Firefox può usare le funzioni di geolocalizzazione del sistema operativo, le reti Wi-Fi, i ripetitori dei cellulari o l'indirizzo IP e può inviare tali dati al servizio di geolocalizzazione di Google, che ha una sua [informativa sulla privacy](https://www.google.com/privacy/lsf.html).

[Per saperne di più](https://www.mozilla.org/firefox/geolocation/).

### Notifiche di siti Web {: #push-notifications }

* __Dati sulla connessione__: se si autorizza un sito Web a inviare notifiche, Firefox si connette a Mozilla e utilizza l'indirizzo IP dell'utente per recapitare i messaggi. Mozilla non può accedere al contenuto dei messaggi.

* __Dati relativi alle interazioni__: riceviamo dati in forma aggregata come il numero di iscrizioni e disiscrizioni alle notifiche di siti Web da Firefox, numero di messaggi inviati, indicatori temporali e mittenti (che possono includere specifici provider di siti Web).

È possibile leggere la [documentazione completa](https://mozilla-push-service.readthedocs.io/en/latest/) oppure [trovare ulteriori informazioni](https://support.mozilla.org/kb/push-notifications-firefox), che includono come revocare le notifiche di siti Web.

### Componenti aggiuntivi {: #addons }

è possibile installare componenti aggiuntivi dal sito addons.mozilla.org ("AMO") o da Gestione estensioni di Firefox, accessibile tramite il pulsante di menu Firefox nella barra degli strumenti.

* __Query di ricerca__: le query di ricerca in Gestione estensioni vengono inviate a Mozilla per fornire all'utente componenti aggiuntivi consigliati.

* __Dati relativi alle interazioni__: riceviamo dati in forma aggregata sulle visite al sito Web AMO e alla sezione Gestione estensioni di Firefox, così come sulle interazioni con i contenuti di tali pagine. È possibile leggere ulteriori informazioni sulle prassi in materia di dati per i [siti Web di Mozilla](https://www.mozilla.org/privacy/websites/).

* __Dati tecnici per gli aggiornamenti__: Firefox si connette periodicamente a Mozilla per installare aggiornamenti dei componenti aggiuntivi. I componenti aggiuntivi installati, la versione di Firefox in uso, la lingua selezionata e il sistema operativo del dispositivo sono utilizzati per applicare gli aggiornamenti corretti.

---

### Nota

Questa informativa sulla privacy si riferisce alla più recente versione per uso generale di Firefox distribuita da Mozilla. Se Firefox è stato ottenuto diversamente o se si esegue una versione meno recente, la copia di Firefox in uso può contenere aspetti relativi alla privacy differenti.
{: #pre-release }

Le versioni preliminari di Mozilla Firefox (distribuite attraverso canali quali Nightly, Beta, Developer Edition e TestFlight) sono piattaforme di sviluppo frequentemente aggiornate con funzioni e studi sperimentali. Oltre alla raccolta dati descritta nella presente informativa sulla privacy, queste versioni possono inviare per impostazione predefinita alcuni tipi di dati relativi all'attività sul Web e agli arresti anomali a Mozilla e in alcuni casi ai nostri partner. Qualsiasi raccolta o condivisione di dati aderisce alla nostra [Informativa sulla raccolta dei dati di Firefox](https://wiki.mozilla.org/Firefox/Data_Collection) e noi saremo sempre trasparenti e forniremo i controlli.
