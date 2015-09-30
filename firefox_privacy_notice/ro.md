# Politica de confidențialitate a browserului Firefox

15 aprilie 2014
{: datetime="2014-04-15" }

Ne pasă de confidențialitatea dvs. Atunci când Firefox trimite informații la Mozilla (adică noi), [politica de confidențialitate](https://www.mozilla.org/privacy/) descrie modul în care prelucrăm acele informații.

## Lucruri pe care ar trebui să le știți

Firefox se conectează automat la noi și la furnizorii noștri de servicii pentru a furniza actualizări, securitate, fragmente (snippets), raportul de stare Firefox și alte funcționalități.
{: #essential-features }

* Actualizări pentru browser și suplimente
  {: #auto-updates }

	Actualizări pentru browser: O dată pe zi, Firefox transmite următoarele informații la Mozilla când caută actualizări pentru browser: informații privind versiunea de Firefox, preferința de limbă, sistemul de operare și versiunea. Puteți [opri actualizările urmărind aceste instrucțiuni](https://support.mozilla.org/kb/how-stop-firefox-automatically-making-connections#w_auto-update-checking), însă poate să vă expună la vulnerabilități de securitate.

	Lista cu suplimente blocate: Firefox contactează Mozilla o dată pe zi pentru a verifica informațiile privind suplimentele pentru a căuta suplimente malițioase. Acest lucru include, spre exemplu: versiunea browserului, sistemul de operare și versiunea, limba, numărul total de cereri, ora ultimei cereri, adresa IP și lista suplimentelor instalate. Puteți [opri actualizările de metadate](https://blog.mozilla.org/addons/how-to-opt-out-of-add-on-metadata-updates/) în orice moment, însă poate să vă expună la vulnerabilități de securitate.

* Fragmente (snippets)
  {: #snippets }

	Pagina de start implicită a Firefox (&lt;about:home&gt;) încarcă bucăți mici de informații chiar sub bara de căutare care credem că vor fi utile pentru dvs. Pe acestea le numim „snippets”. Aproximativ o dată pe zi, Firefox se conectează la Mozilla și vă furnizează fragmente noi, dacă sunt disponibile. Mozilla poate colecta cât de des sunt apăsate aceste fragmente, numele fragmentului, limba browserului și ce versiune de Firefox folosiți. Noi păstrăm doar aceste informații după 60 de zile într-o formă agregată.

	Pentru a ajuta la afișarea de fragmente relevante, Firefox trimite la Mozilla o cerere lunară pentru a căuta locația dvs. la nivel de țară folosind adresa dvs. IP. Apoi noi trimitem acele informații la nivel de țară înapoi la Firefox, unde sunt stocate local.  Firefox va alege apoi fragmente spre afișare în funcție de informațiile stocate local despre țară.
	
	Unele fragmente sponsorizate ale Mozilla sunt interactive și vă permit să partajați în mod opțional numărul de telefon sau adresa de e-mail. De exemplu, puteți să introduceți numărul dvs. de telefon ca să primiți un SMS pentru a instala Firefox pe Android. Informațiile dvs. sunt primite și prelucrate de furnizorul nostru de e-mail sau de marketingul mobil.

* Raportul de stare Firefox
  {: #health-report .inproduct-link } 

	Raportul de stare Firefox (FHR) este conceput să vă ofere o privire de ansamblu asupra stabilității și perfomanței și ponturi dacă întâmpinați probleme, precum rată crescută de de defecțiuni sau timpi lenți de pornire. Mozilla colectează și agregă datele dvs. cu cele ale altor utilizatori Firefox și le trimite înapoi la browserul dvs. astfel încât să puteți vedea cum se schimbă performanța lui Firefox în timp. Aceste date includ, spre exemplu: hardware-ul dispozitivului, sistemul de operare, versiunea Firefox, suplimentele (numărul și tipul), cronologia evenimentelor din browser, randarea, restaurări ale sesiunilor, durata sesiunii, cât de vechi este un profil, numărul de defecțiuni și pagini. FHR nu trimite la Mozilla URL-uri pe care le vizitați.

	Utilizăm datele trimite prin intermediul FHR pentru a furniza utilizatorilor cu funcționalitate FHR ajutor, spre exemplu, în analizarea și abordarea problemelor de performanță cu browserul dvs. Utilizăm, de asemenea, ceea ce descoperim din datele agregate ale FHR pentru a face Firefox mai bun. Puteți alege să [opriți partajarea de date](https://support.mozilla.org/kb/firefox-health-report-understand-your-browser-perf#w_how-to-turn-data-sharing-on-or-off).

* Securitate
  {: #security }

	Firefox caută automat pagini web rău-intenționate sau falsificate, suplimente defecte și certificate SSL emise de terți.

	Certificate securizate ale site-urilor web: Când vizitați un site web sigur (de ex., „https”), Firefox va valida certificatul site-ului. Acest lucru poate implica comunicarea cu un terț de încredere specificat de certificat. Firefox trimite acestui site terț informații care identifică [certificatul](https://support.mozilla.org/kb/secure-website-certificate) site-ului. Puteți [schimba preferințele dvs.](https://support.mozilla.org/kb/advanced-settings-browsing-network-updates-encryption#w_certificates-tab), dar dacă dezactivați funcționalitatea de verificare online, Firefox nu poate confirma identitatea site-ului web pe care îl vizitați. Oprirea acestei funcționalități poate crește riscul ca informațiile dvs. private să fie interceptate. Dacă întâlniți o [conexiune nesigură](https://support.mozilla.org/kb/connection-untrusted-error-message), puteți alege, de asemenea, să trimiteți la Mozilla certificatele asociate.

	Protecția Firefox față de falsuri și atacuri: Aproximativ de două ori pe oră, Firefox descarcă listele Google de „Navigare în siguranță” (SafeBrowsing) pentru a ajuta la blocarea accesului la site-uri și descărcări rău-intenționate sau falsificate (Politica de confidențialitate Google se află la <https://www.google.com/policies/privacy/>). Pentru executabile descărcate care nu apar în aceste liste, Firefox poate trimite metadate, inclusiv URL-uri asociate cu fișierul descărcat, către serviciul de „Navigare în siguranță”. Vizitați <https://support.mozilla.org/kb/how-does-phishing-and-malware-protection-work> pentru a afla mai multe despre sau cum să dezactivați „Navigarea în siguranță”. Dacă dezactivați aceste funcționalități, Firefox nu vă poate avertiza cu privire la site-urile web sau descărcările potențial nelegitime sau rău-intenționate.

* Statistici de utilizare (numite și „Telemetrie” în versiunile care nu sunt finale)
  {: #telemetry .inproduct-link}

	Statisticile de utilizare sau „Telemetria” reprezintă o funcționalitate în Firefox care trimite la Mozilla statistici de utilizare, performantă și viteză de răspuns cu privire la funcționalitățile pentru interfața utilizatorului, memorie sau configurația hardware. Adresa dvs. IP este, de asemenea, colectată ca parte a unui registru web standard. Statisticile de utilizare sunt transmise folosind SSL și ne ajută să îmbunătățim versiunile viitoare de Firefox. Odată trimise la Mozilla, statisticile de utilizare sunt agregate și puse la dispoziția unei game largi de dezvoltatori, inclusiv atât angajați Mozilla, cât și contribuitori publici. Atunci când Telemetria este activată, anumite experimente pe termen scurt ar putea colecta informații despre site-urile vizitate.

	Această funcționalitate este pornită în mod implicit în versiunile Nightly, Developer Edition, Aurora și Beta ale Firefox pentru a ajuta acei utilizatori să furnizeze feedback la Mozilla. În versiunea lansată pentru uz general a Firefox, această funcționalitate este oprită în mod implicit.

	Puteți [afla mai multe despre Telemetrie aici](https://support.mozilla.org/kb/send-performance-data-improve-firefox) și despre cum să o activați sau să o dezactivați.

* Miniaturi 

	Miniaturile sunt o funcționalitate a Firefox afișate pe paginile pentru filă nouă. Pentru a oferi funcționalitatea de miniaturi, Firefox trimite la Mozilla date referitoare la miniaturi, precum numărul de clicuri, impresii, adresa dvs. IP, informații despre limbă și date specifice pentru miniaturi (de ex., poziția și dimensiunea grilei). În Firefox Beta, anumite experimente Telemetrie pe termen scurt (vedeți mai sus) pentru Miniaturi pot colecta informații despre domeniile vizitate de obicei.
	
* Căutare implicită
	Pentru a vă ajuta să alegeți cel mai bun motor de căutare implicit pentru locația dvs., Firefox trimite la Mozilla o cerere pentru a vă căuta locația la nivel de țară, folosind adresa dvs. IP. Noi trimitem aceste informații despre țară înapoi la Firefox, de unde sunt stocate local. Firefox va alege apoi ce motor de căutare să folosească ca opțiune implicită în funcție de informațiile stocate local despre țară.

* Doar în cazul lui Firefox pentru Android:
Pentru a putea înțelege performanța anumitor campanii de marketing ale Mozilla, Firefox trimite date, inclusiv un identificator (ID) publicitar Google, adresă IP, marcaj de timp (timestamp), țara, limba/localizarea, sistemul de operare, versiunea aplicației către vânzătorul nostru terț. Aceste date ne permit să atribuim o instalare unui canal specific de publicitate și pentru a optimiza strategiile ce privesc campaniile de marketing.

---------------------------------------

Când solicitați acest lucru, Firefox se conectează la Mozilla pentru a vă oferi funcționalități cum ar fi Sincronizare, servicii de localizare, raportarea de defecțiuni și suplimente.
{: #optional-features }

* **Sincronizare**: [Sincronizare Firefox](https://www.mozilla.org/firefox/sync/) este un serviciu care vă permite să sincronizați semnele de carte, istoricul de navigare, parolele și setările din Firefox pe toate dispozitivele dvs. Dacă utilizați serviciul Sincronizare, puteți citi [Politica de confidențialitate a Sincronizare Firefox](https://services.mozilla.com/privacy-policy/).
{: #sync }

* **Servicii de localizare**: Firefox are o funcționalitate care permite site-urilor să solicite locația dvs. (de ex., pentru a permite acelor site-uri să vă arate locația pe o hartă). Dacă un site solicită locația dvs., Firefox vă cere permisiunea înainte de a determina și a împărtăși locația dvs. Pentru a determina locația dvs., Firefox poate utiliza mai multe pachete de date, inclusiv funcționalitățile de geolocalizare ale sistemului dvs. de operare, rețelele WiFi, turnurile de telefonie mobilă sau adresa IP. Estimarea locației dvs. implică trimiterea unor părți din aceste informații la serviciul de geolocalizare Google, care se află sub incidența propriei [politici de confidențialitate](https://www.google.com/privacy/lsf.html).
{: #location-services }

* **Raportarea de defecțiuni**: Aveți opțiunea să trimiteți la Mozilla un raport de defecțiuni după ce Firefox s-a închis neașteptat. Acest raport conține informații de ordin tehnic ce ne ajută să îmbunătățim Firefox, inclusiv motivele pentru care Firefox s-a închis neașteptat, URL-ul activ în momentul defecțiunii și starea memoriei calculatorului în timpul defecțiunii. Raportul de defecțiuni poate include informații personale. Noi punem la dispoziția publicului porțiuni din rapoartele de defecțiuni <https://crash-stats.mozilla.com/>). Înainte de a posta în mod public rapoartele de defecțiuni, noi luăm măsuri pentru a separa informațiile cu caracter personal. Nu separăm nimic din ce puteți scrieți în căsuța de comentarii.
{: #crash-reporter .inproduct-link }

* **Erori SSL**: Aveți opțiunea să trimiteți la Mozilla un raport de eroare atunci când este întreruptă o conexiune securizată cu un site web. Acest raport înregistrează certificatul site-ului web, precum și codurile de eroare pentru diagnosticare. Aceste informații ajută Mozilla să monitorizeze eficacitatea certificatelor „fixate” (pinned) ale site-urilor web și detectează posibile atacuri de înșelătorie electronică (phishing) îndreptate împotriva utilizatorilor noștri.

* **Suplimente**: Firefox oferă o pagină de descărcare a suplimentelor, parte a Managerului de suplimente, care dispune de suplimente populare și afișează recomandările personalizate pe baza suplimentelor pe care le aveți instalate deja. Pentru a afișa recomandările personalizate, Firefox trimite informații la Mozilla, inclusiv lista de suplimente pe care le-ați instalat, informații despre versiunea Firefox și adresa dvs. IP. Aceste comunicări se produc doar atunci când este deschisă pagina de descărcare a suplimentelor și pot fi oprite urmând [aceste instrucțiuni](https://blog.mozilla.org/addons/how-to-opt-out-of-add-on-metadata-updates/). Managerul de suplimente din Firefox are un câmp de căutare în care puteți tasta cuvinte cheie pentru a realiza căutări și Mozilla colectează aceste căutări cu cuvinte cheie, precum și informații despre versiunea dvs. Firefox, limba și sistemul de operare pentru a vă putea arăta recomandări.
{: #addons }


