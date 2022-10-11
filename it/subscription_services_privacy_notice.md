# Servizi Mozilla in abbonamento | Informativa sulla privacy

Versione 1.0, in vigore dal martedì 11 ottobre 2022
{: datetime="2022-10-11" }

## Mozilla progetta i suoi prodotti dando priorità alla tua privacy.

__Mozilla VPN__ protegge le connessioni a Internet del tuo dispositivo. Mozilla collabora con Mullvad per crittografare in modo sicuro e anonimo il tuo traffico su Internet.

__Firefox Relay__ consente di mantenere il proprio indirizzo e-mail e numero di telefono principale privato al sicuro dai servizi online, creando un numero di telefono e un indirizzo email unici e casuali (maschera).

Questa informativa sulla privacy spiega quali dati vengono raccolti da Firefox Relay e Mozilla VPN, come vengono condivisi e perché. Per quanto riguarda il modo in cui riceviamo, gestiamo e condividiamo le informazioni, puoi anche fare riferimento all'[Informativa sulla privacy di Mozilla](https://www.mozilla.org/privacy/).

## Cose da sapere

__Informazioni sull'account Firefox.__ Questi Servizi richiedono un account Firefox, che invia a Mozilla il tuo indirizzo email, le impostazioni locali e l'indirizzo IP. Ulteriori informazioni sulle [procedure riguardanti i dati dell'account Firefox](https://www.mozilla.org/privacy/firefox/#firefox-accounts-join-firefox).

__Informazioni sul pagamento.__ Quando ti iscrivi ai Servizi, il tuo addebito sarà gestito tramite uno dei nostri fornitori terzi di servizi di pagamento: Stripe, Apple, PayPal o Google Pay. Mozilla riceve un record del tuo account (che include l'indirizzo di fatturazione e le ultime quattro cifre del tuo metodo di pagamento) e lo stato del tuo abbonamento. Mozilla non memorizza i dettagli completi del pagamento.

__Dati relativi alle interazioni.__ Mozilla riceve dati sulle tue interazioni con i Servizi (ad esempio, quando accedi ed esci, le preferenze impostate, ecc.). Scopri i dettagli sui [dati relativi alle interazioni con la VPN](https://github.com/mozilla-mobile/mozilla-vpn-client/blob/main/glean/metrics.yaml) e sui [dati relativi alle interazioni con Relay](https://github.com/mozilla/fx-private-relay/blob/main/METRICS.md).

__Dati tecnici.__ Mozilla riceve informazioni di base sulla versione software installata per la VPN o il componente aggiuntivo Relay e sui dispositivi su cui è installata, incluso il sistema operativo e la configurazione hardware. Il tuo indirizzo IP viene temporaneamente memorizzato nei registri del nostro server per 90 giorni. Quando usi il servizio Mozilla VPN, né Mozilla né il nostro partner Mullvad conservano alcun registro sul server con le tue attività sulla rete.
Usiamo i dati per migliorare le prestazioni e la stabilità per i nostri utenti e per misurare la performance dei Servizi.

### Mozilla VPN {: #vpn }

__Dati sulla posizione.__ Mozilla VPN riceve il tuo indirizzo IP quando ti registri al servizio e lo utilizzi. Ci serviamo dell'indirizzo IP per approssimare la tua posizione e impostare il server VPN a cui ti connetti e perché la disponibilità, i prezzi e le offerte di Mozilla VPN possono dipendere dal Paese in cui risiedi.

__Dati sulle campagne e di riferimento.__ Queste informazioni aiutano Mozilla VPN a comprendere l'efficacia delle campagne marketing. Al momento dell'installazione dell'app, Mozilla può ricevere il tuo indirizzo IP, oltre a dati sulla campagna e di riferimento, come le campagne pubblicitarie su cui hai fatto clic e il sistema operativo utilizzato, il tipo e l'identificativo del dispositivo e la versione del sistema operativo. Mozilla condivide queste informazioni con Adjust, ma il tuo indirizzo IP non viene né condiviso né memorizzato. Per saperne di più, consulta la [documentazione di Adjust](https://github.com/mozilla-mobile/mozilla-vpn-client/blob/main/src/adjust/adjust.md).

__Dati di rete.__ Mullvad riceve il tuo traffico Internet per fornire il servizio. All'attivazione, Mozilla VPN provvede alla crittografia del tuo traffico Internet e lo invia a Mullvad. Mullvad si impegna a non tenere in registri nessuno dei dati che riceve. Ulteriori informazioni nell'[Informativa sulla privacy di Mullvad](https://mullvad.net/help/no-logging-data-policy/).

### Firefox Relay {: #relay }

__Messaggi email.__ Firefox Relay elabora i tuoi messaggi email per inviarli e inoltrarli dai tuoi indirizzi email mascherati al tuo indirizzo email principale. Il contenuto dei messaggi non viene né letto né memorizzato. Nel caso un'email non possa essere consegnata, verrà temporaneamente memorizzata nei nostri server ed eliminata dopo la consegna (in nessun caso verrà conservata per più di tre giorni). Se usi la funzione di blocco delle email promozionali, il Servizio verificherà le intestazioni delle email per determinare se devono essere bloccate.

__Maschere e loro utilizzo.__ Mozilla conserva una copia dei dati del tuo account per fornire il servizio, in particolare per associare il tuo indirizzo email principale agli indirizzi email mascherati. Se crei una maschera personalizzata, Mozilla la memorizza per potervi inoltrare le email. Mozilla memorizza il sito in cui hai creato la maschera, i siti in cui l'hai successivamente utilizzata e tutte le etichette ad essa associate, per garantire che la maschera sia facilmente reperibile quando vuoi utilizzarla. Scopri come [attivare e disattivare queste funzioni](https://relay.firefox.com/faq).

__Telefonate e SMS.__ Per inviare e inoltrare le chiamate e gli SMS, Firefox Relay elabora il numero di telefono e i messaggi. Memorizziamo un registro dei numeri di telefono che hai contattato tramite Relay per poter esibire i registri delle tue chiamate e degli SMS, inviare SMS di risposta e bloccare i numeri di telefono. Non monitoriamo né memorizziamo il contenuto delle telefonate effettuate tramite Firefox Relay.

Ti invitiamo a leggere la documentazione sulla telemetria di [Firefox Relay](https://github.com/mozilla/fx-private-relay/blob/main/METRICS.md). Puoi disattivare la raccolta di dati telemetrici attivando la funzione di [antitracciamento](https://support.mozilla.org/kb/how-do-i-turn-do-not-track-feature) nel tuo browser.

__Informazioni che condividiamo.__ Firefox Relay condivide informazioni con terzi per fornirti il servizio. Mozilla ha stipulato con l'azienda indicata di seguito un accordo che prevede la protezione dei tuoi dati. Ecco chi utilizziamo per supportare Firefox Relay:

* __[Amazon Web Services.](https://aws.amazon.com/privacy/)__ Amazon Web Services (AWS) è una piattaforma di cloud computing. Firefox Relay si avvale di AWS per ricevere le email inviate agli indirizzi email mascherati e per inoltrarle all'indirizzo email principale associato all'account Firefox. Solo Mozilla conosce l'associazione tra l'indirizzo email principale e gli indirizzi email mascherati.

* __[Twilio.](https://www.twilio.com)__ Twilio riceve il tuo numero di telefono, la tua maschera telefonica e i numeri di telefono con cui scambi chiamate e SMS. Twilio riceve anche il contenuto degli SMS inviati e ricevuti tramite Firefox Relay. Mozilla ha impostato il servizio Twilio in modo da eliminare dopo 7 giorni i registri degli SMS inviati e ricevuti tramite Firefox Relay.

## Altre cose da sapere

Molte delle informazioni che memorizziamo in merito ai nostri utenti con account Firefox sono facilmente accessibili accedendo all'account. [Qui](https://support.mozilla.org/products/privacy-and-security/user-control) puoi trovare ulteriori informazioni sulla gestione dei tuoi dati. Per inoltrare richieste, contattaci sul nostro [Portale per la richiesta di accesso ai dati personali](https://privacyportal.onetrust.com/webform/1350748f-7139-405c-8188-22740b3b5587/4ba08202-2ede-4934-a89e-f0b0870f95f0).

Per qualsiasi altra domanda in merito alle nostre pratiche di privacy puoi contattarci all'indirizzo compliance@mozilla.com.

Rispondiamo a tutte le richieste che riceviamo da individui che desiderano esercitare i propri diritti di protezione dei dati, indipendentemente dal luogo in cui risiedono. La tua richiesta verrà accolta, a meno che un requisito legale non ci impedisca di farlo o si applichi un'eccezione legale.

Per supporto generale, puoi visitare i nostri [forum](https://support.mozilla.org/) .
