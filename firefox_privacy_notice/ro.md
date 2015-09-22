# Politica de confidențialitate a browserului Firefox

15 aprilie 2014
{: datetime="2014-04-15" }

Ne pasă de confidențialitatea dvs. Atunci când Firefox transmite informații la Mozilla (adică noi), [politica de confidențialitate](https://www.mozilla.org/privacy/) descrie modul în care prelucrăm acele informații.

## Câteva lucruri pe care ar trebui să le știți

Firefox se conectează automat la noi și la furnizorii noștri de servicii pentru a furniza actualizări, securitate, fragmente (snippets), raportul de stare Firefox și alte funcționalități.
{: #essential-features }

* Actualizări pentru browser și suplimente
  {: #auto-updates }

	Actualizări pentru browser: O dată pe zi, Firefox transmite următoarele informații la Mozilla când caută actualizări pentru browser: informații privind versiunea de Firefox, preferința de limbă, sistemul de operare și versiunea. Puteți [opri actualizările urmărind aceste instrucțiuni](https://support.mozilla.org/kb/how-stop-firefox-automatically-making-connections#w_auto-update-checking), însă poate să vă expună la vulnerabilități de securitate.

	Lista cu suplimente blocate: Firefox contactează Mozilla o dată pe zi pentru a verifica informațiile privind suplimentele pentru a căuta suplimente malițioase. Acest lucru include, spre exemplu: versiunea browserului, sistemul de operare și versiunea, limba, numărul total de cereri, ora ultimei cereri, adresa IP și lista suplimentelor instalate. Puteți [opri actualizările de metadate](https://blog.mozilla.org/addons/how-to-opt-out-of-add-on-metadata-updates/) în orice moment, însă poate să vă expună la vulnerabilități de securitate.

* Snippets
  {: #snippets }

	Pagina de start implicită a (&lt;about:home&gt;) încarcă fragmente mici de informații chiar sub bara de căutare care credem că vor fi utile pentru dvs. Pe acestea le numim „snippets”. Aproximativ o dată pe zi, Firefox se conectează la Mozilla și vă furnizează snippets noi, dacă sunt disponibile. Mozilla poate colecta cât de des sunt apăsate aceste snippets, numele snippetului, limba browserului și ce versiune de Firefox folosiți. Noi păstrăm doar aceste informații după 60 de zile într-o formă agregată.

	Pentru a ajuta la afișarea de snippets relevante, Firefox trimite la Mozilla o cerere lunară pentru a căuta locația dvs. la nivel de țară folosindu-vă adresa IP. Apoi noi trimitem acele informații la nivel de țară înapoi în Firefox, unde este stocată local.  Firefox va alege apoi snippets spre afișare în funcție de informațiile locale stocate privind țara.
	
	Unele snippets sponsorizate ale Mozilla sunt interactive și vă permit să partajați în mod opțional numărul de telefon sau adresa de e-mail. De exemplu, puteți să introduceți numărul dvs. de telefon ca să primiți un SMS pentru a instala Firefox pe Android. Informațiile dvs. sunt primite și prelucrate de producător mobil pentru marketing sau de furnizorul de e-mail.

* Raportul de stare Firefox
  {: #health-report .inproduct-link } 

	Raportul de stare Firefox (FHR) este conceput să vă ofere is designed to provide you with insights about your browser's stability and performance and with support tips should you experience issues, such as high crash rates or slow startup times. Mozilla collects and aggregates your data with that of other Firefox users and sends it back to your browser so you can see how your Firefox performance changes over time. This data includes, for example: device hardware, operating system, Firefox version, add-ons (count and type), timing of browser events, rendering, session restores, length of session, how old a profile is, count of crashes, and count of pages. FHR does not send Mozilla URLs that you visit.

	We use the data sent through FHR to provide users with FHR's functionality, such as helping you analyze and address performance issues with your browser. We also use what we learn from the FHR data in the aggregate to make Firefox better. You can choose to [turn data sharing off](https://support.mozilla.org/kb/firefox-health-report-understand-your-browser-perf#w_how-to-turn-data-sharing-on-or-off).

* Securitate
  {: #security }

	Firefox verifică automat paginile web rău intenționate sau falsificate, suplimente sau certificate SSL emise de terți nesigure.

	Certificate sigure ale site-urilor web: atunci când vizitați un site sigur (adică "https"), Firefox va valida certificatul site-ului. Aceasta poate implica comunicarea cu un terț de încredere specificat de certificat. Firefox trimite acestui site terț informații care identifică [certificatul](https://support.mozilla.org/kb/secure-website-certificate) site-ului. Puteți [schimba preferințele dvs.](https://support.mozilla.org/kb/advanced-settings-browsing-network-updates-encryption#w_certificates-tab), dar dacă dezactivați funcția de verificare online, Firefox nu poate identifica identitatea site-ului pe care-l vizitați. Dezactivarea acestei funcționalități poate crește riscul ca informațiile dvs. private să fie interceptate. Dacă întâlniți o [conexiune nesigură](https://support.mozilla.org/kb/connection-untrusted-error-message), puteți alege să trimiteți la Mozilla certificatele asociate.

	Protecția Firefox față de falsuri și atac: aproximativ de două ori pe oră, Firefox descarcă listele Google de „Navigare în siguranță„ (SafeBrowsing) pentru a ajuta la blocarea accesului la site-uri și descărcări rele intenționate sau falsificate (Politica de confidențialitate Google se găsește la <https://www.google.com/policies/privacy/>). Pentru executabile descărcate care nu apar în aceste liste, Firefox poate trimite metadate, inclusiv URL-uri asociate către serviciul de „Navigare în siguranță”. Vizitați <https://support.mozilla.org/kb/how-does-phishing-and-malware-protection-work> pentru a afla mai multe despre cum să dezactivați „Navigarea în siguranță”. Dacă dezactivați aceste funcționalități, Firefox nu vă poate avertiza asupra site-urilor web sau descărcări potențial nelegitime sau rău intenționate.

* Statistici de utilizare (numite și ca „Telemetrie” în versiunile care nu sunt finale)
  {: #telemetry .inproduct-link}

	Statistici de utilizare sau „Telemetrie” este o nouă funcție Firefox care trimite la Mozilla statistici de utilizare, performantă și de receptivitate despre funcții ce țin de interfețele utilizator, memorie sau configurația hardware. Adresa dvs. de IP este, de asemenea, colectată ca parte a unui registru web standard. Statistici de utilizare sunt transmise folosind SSL și ne ajută să îmbunătățim versiunile viitoare de Firefox. Odată trimise la Mozilla, statisticile de utilizare sunt agregate și puse la dispoziția unui număr mare de dezvoltatori, inclusiv angajați Mozilla și contribuitori publici. Atunci când este activată Telemetria, animite experimente pe termen lung ar putea colecta informații despre site-urile vizitate.

	Această funcție este activate în mod implicit în edițiile Nightly Developer Edition, Aurora și Beta de Firefox pentru a ajuta acei utilizatori să trimită feedback la Mozilla. În versiunea stabilă pentru uz general de Firefox, această funcție este dezactivată în mod implicit.

	Puteți [afla mai multe despre Telemetrie aici](https://support.mozilla.org/kb/send-performance-data-improve-firefox) și despre cum să activați sau să dezactivați funcția.

* Miniaturi 

	Miniaturile sunt o funcție a Firefox afișate pe paginile de filă nouă. Pentru a oferi funcționalitatea de miniaturi, Firefox trimite la Mozilla date asociate miniaturilor, precum numărul de clicuri, impresii, adresa de IP a dvs., informații despre limbă (locale) și date specifice pentru miniaturi (de ex. poziția și dimensiunea grilei). În Firefox Beta, anumite experimente Telemetry pe termen scurt (vedeți mai sus) pentru Miniaturi pot colecta informații despre domeniile vizitate în mod frecvent.
	
* Căutare implicită
	Pentru a vă ajuta să alegeți cel mai bun motor de căutare pentru locația dvs., Firefox trimite la Mozilla o cerere pentru a vă identifica locația la nivel de țară, folosind adresa de IP a dvs. Noi trimitem aceste informații despre țară înapoi la Firefox, de unde sunt stocate local. Firefox va alege apoi ce motor de căutare să folosească pe baza informațiilor despre țară stocată local.

* Doar pentru Firefox pentru Android:
Pentru a putea înțelege performanța anumitor campanii de marketing Mozilla, Firefox trimite date, inclusiv un identificator (ID) publicitar Google, adresa de IP, un marcaj de timp (timestamp), țara, limba/localizarea, sistemul de operare, versiunea aplicației către un vânzător terț. Aceste date ne permit să atribuim o instalare unui canal specific de publicitate și pentru a optimiza strategiile ce privesc campaniile de marketing.

---------------------------------------

Când solicitați acest lucru, Firefox se conectează la Mozilla pentru a vă oferi funcționalități cum ar fi Sincronizare, servicii de localizare, raportarea defectelor și suplimente.
{: #optional-features }

* **Sincronizare**: [Firefox Sync](https://www.mozilla.org/firefox/sync/) este un serviciu care vă permite să sincronizați semnele de carte, istoricul de navigare, parolele și setările pentru toate dispozitivele dvs. Dacă utilizați serviciul Sincronizare, puteți citi [Politica de confidențialitate Firefox Sincronizare](https://services.mozilla.com/privacy-policy/).
{: #sync }

* **Servicii de localizare**: Firefox are o funcționalitate care permite site-urilor să vă solicite locația (de ex. pentru a permite acelor site-uri să vă identifice locația pe o hartă). Dacă un site vă solicită locația, Firefox vă cere permisiunea înainte de a decide să vă împărtășească locația. Pentru a vă determina locația, Firefox poate trimite mai multe pachete de date care includ funcționalitățile de geolocație a sistemului dvs. de operare, rețele WiFi, turnuri de telefonie mobilă sau adrese de IP. Estimarea locației dvs. implică trimiterea unor părți din aceste informații la serviciul de geolocalizare Google, care se află sub incidența propriei [politici de confidențialitate](https://www.google.com/privacy/lsf.html).
{: #location-services }

* **Raportarea de defecţiuni**: Aveți opțiunea să trimiteți la Mozilla un raport de defecte după ce Firefox s-a închis în mod neașteptat. Acest raport conține informații de ordin tehnic ce ne ajută să îmbunătățim Firefox, inclusiv motivele pentru care Firefox s-a închis, URL-ul activ în acel moment și starea memoriei calculatorului în timpul închiderii. Raportul de defecțiuni poate include informații personale. Noi facem porțiuni din acest raport public la <https://crash-stats.mozilla.com/>). Înainte de a posta în mod public rapoartele de defecțiuni, noi luăm măsuri să anonimizăm informația personală. Nu anonimizăm nimic din ce scrieți în căsuța de comentarii.
{: #crash-reporter .inproduct-link }

* **Erori SSL**: Aveți opțiunea de a trimite la Mozilla un raport de eroare atunci când este întreruptă o conexiune sigură la un site. Acest raport înregistrează certificatul site-ului web și codurile de eroare pentru diagnoză asociate. Aceste informații ajută Mozilla să monitorizeze acuratețea certificatelor „fixate” (pinned) și detectează posibile atacuri de phishing îndreptate împotriva utilizatorilor noștri.

* **Suplimente**: Firefox oferă o pagină de obținere de suplimente, parte a Gestionarului de suplimente, care evidențiază suplimente populare și afișează recomandările personalizate pe baza suplimentelor pe care le aveți instalate deja, informații despre versiunea Firefox a dvs. și adresa de IP a dvs. Aceste comunicări se produc doar atunci când este deschisă pagina de obținere de suplimente și pot fi dezactivate urmând [aceste instrucțiuni](https://blog.mozilla.org/addons/how-to-opt-out-of-add-on-metadata-updates/). Gestionarul de suplimente din Firefox are o căsuța de căutare în care puteți introduce cuvinte cheie pentru a realiza căutări și Mozilla colectează aceste căutări de cuvinte cheie, precum și informații despre versiunea de Firefox a dvs, limba și sistemul de operare pentru a vă putea arăta recomandări.
{: #addons }
