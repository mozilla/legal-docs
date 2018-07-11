# Politica de confidențialitate a browserului Firefox

20 iulie 2017
{: datetime="2017-07-20" }

Ne pasă de confidențialitatea dvs. Atunci când Firefox trimite informații la Mozilla (adică noi), [politica de confidențialitate](https://www.mozilla.org/privacy/) descrie modul în care prelucrăm acele informații.

## Lucruri pe care ar trebui să le știți

Firefox se conectează automat la noi și la furnizorii noștri de servicii pentru a furniza actualizări, securitate, fragmente (snippets), raportul de stare Firefox și alte funcționalități.
{: #essential-features }

* **Actualizări pentru browser și suplimente**
{: #auto-updates }

	Actualizări pentru browser: O dată pe zi, Firefox transmite următoarele informații la Mozilla când caută actualizări pentru browser: informații privind versiunea de Firefox, preferința de limbă, sistemul de operare și versiunea. Puteți [opri actualizările urmărind aceste instrucțiuni](https://support.mozilla.org/kb/how-stop-firefox-automatically-making-connections#w_auto-update-checking), însă poate să vă expună la vulnerabilități de securitate.

	Lista cu suplimente blocate: Firefox contactează Mozilla o dată pe zi pentru a verifica informațiile privind suplimentele pentru a căuta suplimente malițioase. Acest lucru include, spre exemplu: versiunea browserului, sistemul de operare și versiunea, limba, numărul total de cereri, ora ultimei cereri, adresa IP și lista suplimentelor instalate. Puteți [opri actualizările de metadate](https://support.mozilla.org/kb/how-stop-firefox-making-automatic-connections) în orice moment, însă poate să vă expună la vulnerabilități de securitate.

* **Fragmente** (snippets)
{: #snippets }

	Pagina de start implicită a Firefox (&lt;about:home&gt;) încarcă bucăți mici de informații chiar sub bara de căutare care credem că vor fi utile pentru dvs. Pe acestea le numim „snippets”. Aproximativ o dată pe zi, Firefox se conectează la Mozilla și vă furnizează fragmente noi, dacă sunt disponibile. Mozilla poate colecta cât de des sunt apăsate aceste fragmente, numele fragmentului, limba browserului și ce versiune de Firefox folosiți. Noi păstrăm doar aceste informații după 60 de zile într-o formă agregată.

	Pentru a ajuta la afișarea de fragmente relevante, Firefox trimite la Mozilla o cerere lunară pentru a căuta locația dvs. la nivel de țară folosind adresa dvs. IP. Apoi noi trimitem acele informații la nivel de țară înapoi la Firefox, unde sunt stocate local. Firefox va alege apoi fragmente spre afișare în funcție de informațiile stocate local despre țară.

	Unele fragmente sponsorizate ale Mozilla sunt interactive și vă permit să partajați în mod opțional numărul de telefon sau adresa de e-mail. De exemplu, puteți să introduceți numărul dvs. de telefon ca să primiți un SMS pentru a instala Firefox pe Android. Informațiile dvs. sunt primite și prelucrate de furnizorul nostru de e-mail sau de marketingul mobil.

* **Raportul de stare Firefox**
{: #health-report .inproduct-link }

	Raportul de stare Firefox (FHR) este conceput să vă ofere o privire de ansamblu asupra stabilității și perfomanței browser-ului și ponturi dacă întâmpinați probleme, cum ar fi un număr mare de defecte sau întârzieri la pornire. Mozilla colectează și agregă datele dvs. cu cele ale altor utilizatori Firefox și le trimite înapoi la browserul dvs. astfel încât să puteți vedea cum se schimbă performanța browser-ului dvs. Firefox în timp. Aceste date includ, spre exemplu: hardware-ul dispozitivului, sistemul de operare, versiunea Firefox, suplimentele (numărul și tipul), cronologia evenimentelor din browser, randarea, restaurări ale sesiunilor, durata sesiunii, interacțiunea cu punctele de acces prin intermediul căutărilor si utilizarea codurilor de partener Firefox pentru căutare, cât de vechi este un profil, numărul de defecte și pagini. FHR nu trimite către Mozilla URL-urile pe care le vizitați.

	Utilizăm datele trimite prin intermediul FHR pentru a furniza utilizatorilor cu funcționalitate FHR ajutor, spre exemplu, în analizarea și abordarea problemelor de performanță cu browserul dvs. Utilizăm, de asemenea, ceea ce descoperim din datele agregate ale FHR pentru a face Firefox mai bun. Puteți alege să [opriți partajarea de date](https://support.mozilla.org/kb/firefox-health-report-understand-your-browser-perf#w_how-to-turn-data-sharing-on-or-off).

* **Securitate**
{: #security }

	Firefox caută automat pagini web rău-intenționate sau falsificate, suplimente defecte și certificate SSL emise de terți.

	Certificate securizate ale site-urilor web: Când vizitați un site web sigur (de ex., „https”), Firefox va valida certificatul site-ului. Acest lucru poate implica comunicarea cu un terț de încredere specificat de certificat. Firefox trimite acestui site terț informații care identifică [certificatul](https://support.mozilla.org/kb/secure-website-certificate) site-ului. Puteți [schimba preferințele dvs.](https://support.mozilla.org/kb/advanced-settings-browsing-network-updates-encryption#w_certificates-tab), dar dacă dezactivați funcționalitatea de verificare online, Firefox nu poate confirma identitatea site-ului web pe care îl vizitați. Oprirea acestei funcționalități poate crește riscul ca informațiile dvs. private să fie interceptate. Dacă întâlniți o [conexiune nesigură](https://support.mozilla.org/kb/connection-untrusted-error-message), puteți alege, de asemenea, să trimiteți la Mozilla certificatele asociate.

	Protecția Firefox față de falsuri și atacuri: Aproximativ de două ori pe oră, Firefox descarcă listele Google de „Navigare în siguranță” (SafeBrowsing) pentru a ajuta la blocarea accesului la site-uri și descărcări rău-intenționate sau falsificate (Politica de confidențialitate Google se află la <https://www.google.com/policies/privacy/>). Pentru executabile descărcate care nu apar în aceste liste, Firefox poate trimite metadate, inclusiv URL-uri asociate cu fișierul descărcat, către serviciul de „Navigare în siguranță”. Vizitați <https://support.mozilla.org/kb/how-does-phishing-and-malware-protection-work> pentru a afla mai multe despre sau cum să dezactivați „Navigarea în siguranță”. Dacă dezactivați aceste funcționalități, Firefox nu vă poate avertiza cu privire la site-urile web sau descărcările potențial nelegitime sau rău-intenționate.

* **Statistici de utilizare** (numite și „Telemetrie” în versiunile care nu sunt finale)
{: #telemetry .inproduct-link}

	Statisticile de utilizare sau „Telemetria” reprezintă o funcționalitate în Firefox care trimite la Mozilla statistici de utilizare, performantă și viteză de răspuns cu privire la funcționalitățile pentru interfața utilizatorului, memorie sau configurația hardware. Adresa dvs. IP este, de asemenea, colectată ca parte a unui registru web standard. Statisticile de utilizare sunt transmise folosind SSL și ne ajută să îmbunătățim versiunile viitoare de Firefox. Odată trimise la Mozilla, statisticile de utilizare sunt agregate și puse la dispoziția unei game largi de dezvoltatori, inclusiv atât angajați Mozilla, cât și contribuitori publici. Atunci când Telemetria este activată, anumite experimente pe termen scurt ar putea colecta informații despre site-urile vizitate.

	Această funcție este dezactivată implicit în versiunile  Nightly și Beta/Developer Edition ale Firefox pentru a ajuta utilizatorii lor să ofere feedback către Mozilla. În versiunea finală a Firefox această funcție este dezactivită implicit.

	Puteți [afla mai multe despre Telemetrie aici](https://support.mozilla.org/kb/send-performance-data-improve-firefox) și despre cum să o activați sau să o dezactivați.

* **Miniaturi**
{: #tiles }

	Miniaturile sunt o funcționalitate a Firefox afișate pe paginile pentru filă nouă. Pentru a oferi funcționalitatea de miniaturi, Firefox trimite la Mozilla date referitoare la miniaturi, precum numărul de clicuri, impresii, adresa dvs. IP, informații despre limbă și date specifice pentru miniaturi (de ex., poziția și dimensiunea grilei). În Firefox Beta, anumite experimente Telemetrie pe termen scurt (vedeți mai sus) pentru Miniaturi pot colecta informații despre domeniile vizitate de obicei.

* **Căutare implicită**
{: #searchsuggestions }

	Sugestiile de căutare reprezintă o funcție care vă ajută să găsiți sintagme uzuale, pe care le-au mai căutat și alte persoane. Aceste sugestii de căutare sunt oferite de motoarele dvs. de căutare implicite (cum ar fi Google, Yahoo, etc.), și nu de Firefox. Dacă activați această funcție, și motorul dvs. de căutare implicit suportă sugestiile, Firefox poate să trimită termenii pe care îi scrieți în bara inteligentă sau în bara de căutare către motorul dvs. de căutare implicit, pentru a prelua sugestiile, iar această acțiune este supusă Politicii de Confidențialitate aplicabile respectivului motor de căutare implicit. Puteți [afla mai multe despre sugestiile de căutare aici](https://support.mozilla.org/kb/use-popular-search-suggestions-firefox-search-bar), inclusiv cum să le activați sau dezactivați.

* **Referral și urmărirea campaniei**{: #thirdparty } ** **{: #referraltracking }

	Pentru a putea înțelege și îmbunătăți campaniile noastre de marketing, Firefox trimite anumite informații implicit. Acestea include Datele despre referral, cum ar fi domeniul site-ului web sau campania publicitară care v-a indicat să descărcați și să instalați Firefox, ca și Datele despre interacțiuni despre ce funcții Firefox folosiți.

	__Date despre referral__
	Pe Android și iOS, Firefox trimite Datele despre referral către furnizorul nostru de date analitice pentru mobil, și acestea includ ID-ul publicitar al Google, adresa de IP, marcajul de timp, țara, limba, sistemul de operare și versiunea aplicației. Aflați mai multe[aici](https://support.mozilla.org/kb/desktop-attribution-privacy), inclusiv cum puteți dezactiva raportarea.

	Pe desktop, Firefox înregistrează și trimite Datele despre referral ca parte a Firefox Health Report. Aflați mai multe [aici](https://support.mozilla.org/kb/desktop-attribution-privacy), inclusiv cum puteți dezactiva sau opta să nu mai folosiți această raportare.

	__Date despre interacțiuni__
	Pe iOS, Firefox trimite Date despre iteracțiuni către Leanplum, furnizorul nostru de marketing pentru dispozitive mobile, care are propria sa[politică de confidențialitate](https://www.leanplum.com/privacy/). Aceste date ne permit să testăm diferite funcții și experiențe și să oferim mesaje și recomandări personalizate pentru a vă îmbunătăți experiența cu Firefox. Aflați mai multe despre datele pe care le colectăm[aici](https://github.com/mozilla-mobile/firefox-ios/blob/master/MMA.md), și cum puteți[dezactiva acestă funcție](https://support.mozilla.org/kb/send-anonymous-usage-data-firefox-mobile-devices).

---------------------------------------

Când solicitați acest lucru, Firefox se conectează la Mozilla pentru a vă oferi funcționalități cum ar fi Sincronizare, servicii de localizare, raportarea de defecțiuni și suplimente.
{: #optional-features }

* **Sincronizare**
{: #sync }

	[Sincronizare Firefox](https://www.mozilla.org/firefox/sync/) este un serviciu care vă permite să sincronizați semnele de carte, istoricul de navigare, parolele și setările din Firefox pe toate dispozitivele dvs. Dacă utilizați serviciul Sincronizare, puteți citi [Politica de confidențialitate a Sincronizare Firefox](https://accounts.firefox.com/legal/privacy).

* **Servicii de localizare**
{: #location-services }

	Firefox are o funcționalitate care permite site-urilor să solicite locația dvs. (de ex., pentru a permite acelor site-uri să vă arate locația pe o hartă). Dacă un site solicită locația dvs., Firefox vă cere permisiunea înainte de a determina și a împărtăși locația dvs. Pentru a determina locația dvs., Firefox poate utiliza mai multe pachete de date, inclusiv funcționalitățile de geolocalizare ale sistemului dvs. de operare, rețelele WiFi, turnurile de telefonie mobilă sau adresa IP. Estimarea locației dvs. implică trimiterea unor părți din aceste informații la serviciul de geolocalizare Google, care se află sub incidența propriei [politici de confidențialitate](https://www.google.com/privacy/lsf.html).

* **Raportarea de defecțiuni**
{: #crash-reporter .inproduct-link }

	Aveți opțiunea să trimiteți la Mozilla un raport de defecțiuni după ce Firefox s-a închis neașteptat. Acest raport conține informații de ordin tehnic ce ne ajută să îmbunătățim Firefox, inclusiv motivele pentru care Firefox s-a închis neașteptat, URL-ul activ în momentul defecțiunii și starea memoriei calculatorului în timpul defecțiunii. Raportul de defecțiuni poate include informații personale. Noi punem la dispoziția publicului porțiuni din rapoartele de defecțiuni <https://crash-stats.mozilla.com/>). Înainte de a posta în mod public rapoartele de defecțiuni, noi luăm măsuri pentru a separa informațiile cu caracter personal. Nu separăm nimic din ce puteți scrieți în căsuța de comentarii.

* **Erori SSL**
{: #ssl-errors }

	Aveți opțiunea să trimiteți la Mozilla un raport de eroare atunci când este întreruptă o conexiune securizată cu un site web. Acest raport înregistrează certificatul site-ului web, precum și codurile de eroare pentru diagnosticare. Aceste informații ajută Mozilla să monitorizeze eficacitatea certificatelor „fixate” (pinned) ale site-urilor web și detectează posibile atacuri de înșelătorie electronică (phishing) îndreptate împotriva utilizatorilor noștri.

* **Suplimente**
{: #addons }

	Firefox oferă o pagină de descărcare a suplimentelor, parte a Managerului de suplimente, care dispune de suplimente populare și afișează recomandările personalizate pe baza suplimentelor pe care le aveți instalate deja. Pentru a afișa recomandările personalizate, Firefox trimite informații la Mozilla, inclusiv lista de suplimente pe care le-ați instalat, informații despre versiunea Firefox și adresa dvs. IP. Aceste comunicări se produc doar atunci când este deschisă pagina de descărcare a suplimentelor și pot fi oprite urmând [aceste instrucțiuni](https://support.mozilla.org/kb/how-stop-firefox-making-automatic-connections). Managerul de suplimente din Firefox are un câmp de căutare în care puteți tasta cuvinte cheie pentru a realiza căutări și Mozilla colectează aceste căutări cu cuvinte cheie, precum și informații despre versiunea dvs. Firefox, limba și sistemul de operare pentru a vă putea arăta recomandări.

* **Notificări Push**
{: #push-notifications }

	Notificările Push permit site-urilor să vă trimită notificări și actualizări dacă ați optat pentru aceasta. Pentru a primi notificările, Firefox trimite către Mozilla informații despre site-urile de la care ați acceptat să primiți notificări Push. Stocăm aceste informații într-o formă anonimă, împreună cu numărul de notificări pe care le primiți de la fiecare site. Pentru a ajuta dezvoltatorii să-și îmbunătățească modul în care folosesc notificările Push, Mozilla poate să împărtășească date agregate cu diferiți dezvoltatori, inclusiv numărul de vizitatori de pe site-ul lor care s-au abonat sau dezabonat de la serviciul de notificări Push. Puteți gestiona notificările Push în Firefox urmând [aceste instrucțiuni](https://support.mozilla.org/kb/push-notifications-firefox).

* **Capturi de ecran Firefox**
{: #screenshots }

	__Încărcarea capturilor de ecran__
	Capturile de ecran pe care alegeți să le încărcați  sunt trimise către Mozilla și sunt stocate pentru perioada de timp indicată, pe care o puteți modifica.  Putem accesa capturile de ecran pe care le-ați încărcat atunci când acest lucru este necear pentru operarea serviciului nostru. Puteți șterge capturile de ecran pe care le-ați încărcat în orice moment.  

	__Date despre interacțiuni__
	Primim date, cum ar fi vizitele pe site-ul Capturi de ecran Firefox, cât de des au fost accesate capturile de ecran încărcate și cât de des au fost partajate de dvs. și de alții, felul în care ați interacționat cu butoanele și piesele de pe ecran, și mișcările mouse-ului asociate capturilor de ecran.  
Pentru vizitele la site-ul Capturi de ecran Firefox, [politica noastră de confidențialitate pentru site-uri web](https://www.mozilla.org/privacy/websites/) descrie tipurile de date pe care le colectăm. 

	__Date tehnice__
	Primim date cun ar fi dimensiunea medie și numărul de capturi de ecran pe care le-ați încărcat, versiunea browser-ului dvs. Firefox, sistemul de operare al dispozitivului dvs. și erorile înregistrate. Adresele IP care accesează Capturi de ecran Firefox sunt colectate temporar ca parte a jurnalului de server standard. 

	Citiți documentația completă[aici](https://github.com/mozilla-services/screenshots/blob/master/docs/METRICS.md) sau ștergeți toate capturile dvs. de ecran [aici](https://screenshots.firefox.com/leave-screenshots).

Cu excepția cazurilor în care se specifică altceva, prezenta politică de confidențialitate se aplică ultimelor versiuni generale de Firefox. Versiunile care nu au fost lansate oficial (Beta/Developer Edition, Nightly și TestFlight) sunt în continuare parte a ciclului de dezvoltare și pot conține funcționalități noi sau alte opțiuni de confidențialitate. Versiunile care nu au fost lansate oficial trimit automat [date de Telemetrie](https://gecko.readthedocs.io/en/latest/toolkit/components/telemetry/telemetry/index.html) către Mozilla pentru a ne ajuta să îmbunătățim Firefox.
{: #pre-release }

Această traducere nu reprezintă cea mai nouă versiune. Versiunea curentă în limba engleză are prioritate, atunci când există conflicte cu această traducere. Puteți citi versiunea curentă în limba engleză [aici](https://github.com/mozilla/legal-docs/blob/master/acceptable_use_policy/en-US.md).
