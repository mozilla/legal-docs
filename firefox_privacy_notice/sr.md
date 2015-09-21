# Obaveštenje o privatnosti pretraživača Firefox

15\. april 2014.
{: datetime="2014-04-15" }

Stalo nam je do Vaše privatnosti. Kada Firefox šalje informacije kompaniji Mozilla (to smo mi) u našoj [Polisi privatnosti](https://www.mozilla.org/sr/privacy/) opisuje se način na koji koristimo te informacije.

## Stvari koje bi trebalo da znate

Firefox se automatski povezuje s nama i našim pružaocima usluga radi pružanja ažuriranja, bezbednosti, odlomaka, izveštaja o bezbednosti Firefox-a i ostalih opcija.
{: #essential-features }

* Ažuriranje pregledača i dodataka
  {: #auto-updates }

	Ažuriranje pregledača: Firefox jednom dnevno šalje sledeće podatke Mozilla-i kada proverava da li postoje ažuriranja za pregledač: informacije o verziji Firefox-a kojeg koristite, podešavanja jezika, informacije o operativnom sistemu i verziji. Možete [isključiti ažuriranja tako što ćete pratiti ova uputstva](https://support.mozilla.org/kb/how-stop-firefox-automatically-making-connections#w_auto-update-checking), ali to može ugroziti bezbednost Vašeg sistema.

	Lista blokiranih dodataka: Firefox jednom dnevno kontaktira Mozilla-u radi provere informacija o malicioznim dodacima. To obuhvata, na primer, verziju pregledača, OS i verziju, jezik, ukupni broj zahteva, vreme poslednjeg zahteva, doba dana, IP adresu, kao i listu dodataka koje ste instalirali. Možete [isključiti ažuriranja meta podataka](https://blog.mozilla.org/addons/how-to-opt-out-of-add-on-metadata-updates) u svakom trenutku, ali to može ugroziti bezbednost Vašeg sistema.

* Odlomci
  {: #snippets }

	Na Firefox-ovoj podrazumevanoj početnoj strani (&lt;abouthome&gt;) učitavaju se određene informacije odmah ispod trake za pretragu za koje verujemo da Vam mogu biti od koristi. Zovemo ih „odlomci“. Otprilike jednom dnevno, Firefox se povezuje sa Mozilla-om i pruža Vam nove odlomke, ako postoje. Mozilla prikuplja podatke o tome koliko se na njih često klikne, o nazivu odlomka, jeziku pregledača i koju verziju Firefox-a koristite.

	U cilju prikazivanja relevantnih odlomaka, Firefox šalje Mozilla-i mesečni zahtev da pogleda Vašu lokaciju na nivou zemlje koristeći Vašu IP adresu. Zatim šaljemo date podatke na nivou zemlje nazad Firefox-u, a oni ih skladište lokalno. Firefox će zatim izabrati koje odlomke da prikazuje na osnovu lokalno uskladištenih podataka o zemlji.

* Izveštaji o zdravlju Firefox-a
  {: #health-report .inproduct-link } 

	Izveštaji o zdravlju Firefox-a (Firefox Health Report - FHR) je osmišljen da Vam pruži uvid u stabilnost i performanse Vašeg pregledača, kao i da Vas posavetuje u slučaju da doživite neku neprijatnost, kao što je visoka stopa pada ili dugo čekanje na podizanje pregledača. Mozilla prikuplja i spaja Vaše podatke sa podacima ostalih korisnika Firefox-a i šalje ih Vašem pregledaču kako biste mogli da vidite kako se performanse Vašeg Firefox pregledača vremenom menjaju. Ovi podaci obuhvataju, na primer, hardver uređaja, operativni sistem, verziju Firefox-a, dodatke (broj i vrstu), vremena događaja u pregledaču, vizuelizaciju, vraćanja prethodnih sesija, trajanje sesija, starost profila, broj padova i broj stranica. FHR ne šalje Mozilla-i veze koje posećujete.

	Podatke koji se šalju preko FHR-a koristimo da bismo korisnicima pružili funkcionalnost FHR-a, kao što je pomoć pri analiziranju i rešavanju problema sa performansama Vašeg pregledača. Takođe, koristimo ono što saznamo iz zbirnih FHR podataka da bismo poboljšali Firefox. Možete odabrati da [isključite deljenje podataka](https://support.mozilla.org/kb/firefox-health-report-understand-your-browser-perf#w_how-to-turn-data-sharing-on-or-off).

* Bezbednost
  {: #security }

	Firefox automatski proverava da li je neka stranica maliciozna ili falsifikovana, da li postoje pokvareni dodaci i sertifikati SSL treće strane.

	Sertifikati bezbednih veb sajtova: Kada posetite bezbedni veb sajt (npr. „https“), Firefox vrši proveru sertifikata veb sajta. To može da obuhvati i komunikaciju sa pružaocem statusa treće strane navedenom u sertifikatu. Firefox ovoj trećoj strani šalje informacije kojima se identifikuje [sertifikat](https://support.mozilla.org/kb/secure-website-certificate) sajta. Možete [promeniti svoja željena podešavanja](https://support.mozilla.org/sr-Cyrl/kb/napredna-podesavanja-dodatni-jezicak), ali ako isključite opciju za internet verifikaciju, Firefox ne može da potvrdi identitet veb sajta koji posećujete. Ukoliko isključite ovu opciju, može doći do povećanog rizika od presretanja Vaših privatnih informacija. Ukoliko naiđete na [nepouzdanu konekciju](https://support.mozilla.org/kb/connection-untrusted-error-message), možete se odlučiti da pošaljete Mozilla-i odgovarajuće sertifikate.

	Zaštita od falsifikovanja i napada koju pruža Firefox: Otprilike dva puta na sat, Firefox preuzima od Google liste „SafeBrowsing“ kako bi Vam pomogao da blokirate pristup sajtovima i preuzimanje sadržaja koji su maliciozni ili falsifikovani (Polisa privatnosti kompanije Google nalaze se na adresi <https://www.google.com/policies/privacy>). U slučaju preuzetih izvršnih datoteka koje se ne pojavljuju na ovim listama, Firefox može slati meta podatke, uključujući i veze (URL) povezane sa preuzetim datotekama, servisu SafeBrowsing. Posetite <https://support.mozilla.org/kb/how-does-phishing-and-malware-protection-work> da biste saznali više ili da biste isključili Bezbedno pregledanje (Safe browsing). Ukoliko isključite ove opcije, Firefox Vas ne može upozoriti na potencijalno nelegitimne ili maliciozne veb sajtove ili preuzete datoteke.

* Statistika o korišćenju (koja se još zove „Telemetrija“ u verzijama koje se ne puštaju u opticaj)
  {: #telemetry .inproduct-link}

	Statistika o korišćenju ili „Telemetrija“ predstavlja opciju unutar Firefox-a koja šalje Mozilla-i statistiku o korišćenju, performansama i vremenu reakcije opcija korisničkog interfejsa, memorije i konfiguracije hardvera. Podaci o Vašoj IP adresi se takođe prikupljaju u okviru standardne veb evidencije. Statistika korišćenja se prenosi putem SSL-a i pomaže nam da poboljšamo buduće verzije Firefox-a. Kada se statistika korišćenja pošalje Mozilla-i, podaci se zbirno obrađuju i dostavljaju širokom krugu programera, uključujući i zaposlene u kompaniji Mozilla i njene saradnike.

	Ova opcija je po podrazumevanom uključena u verzijama Nightly, Aurora i Beta pregledača Firefox kako bi pomogao ovim korisnicima da šalju povratne informacije Mozilla-i. U opštim verzijama Firefox-a koje se puštaju u opticaj, ova opcija je po podrazumevanom isključena.

	Više podataka o [Telemetriji možete saznati ovde](https://support.mozilla.org/kb/send-performance-data-improve-firefox), kao i o tome kako da je uključite ili isključite. 

* Pločice

	Pločice predstavljaju opciju u Firefox-u koja se prikazuje na stranicama novih jezičaka. U cilju prikazivanja Pločica, Firefox šalje podatke Mozilla-i u pogledu Pločica, kao što su broj klikova, impresija, Vaša IP adresa, podaci o jeziku i podaci koji se odnose konkretno na pločicu (npr. položaj i veličina mreže). U Beta verziji Firefox-a, određeni kratkoročni telemetrijski eksperimenti (vidite gore) u slučaju Pločica mogu prikupljati informacije o najčešće posećivanim domenima.

---------------------------------------

Kada to zatražite, Firefox se povezuje i sa Mozilla-om kako bi Vam obezbedio mogućnosti kao što su Sync, servisi lociranja, izveštavanje o padovima i dodaci.
{: #optional-features }

* **Sync**: [Firefox Sync](https://www.mozilla.org/sr/firefox/sync/) je servis koji omogućava da sinhronizujete zabeleške, istorijat pregledanja, lozinke i podešavanja Firefox-a na svim Vašim uređajima. Ako koristite servis Sync, možete pročitati [Obaveštenje o privatnosti za Firefox Sync](https://services.mozilla.com/privacy-policy).
{: #sync }

* **Servisi lociranja**: Firefox ima opciju koja omogućava sajtovima da zahtevaju informacije o Vašoj lokaciji (npr. da dozvoli datim sajtovima da prikažu Vašu lokaciju na mapi). Ako neki sajt zahteva Vašu lokaciju, Firefox od Vas traži dozvolu pre nego što pruži tražene informacije. Da bi odredio Vašu lokaciju, Firefox može da iskoristi nekoliko podataka, uključujući opcije geolociranja Vašeg operativnog sistema, Wi-fi mreže, tornjeve mobilne telefonije ili IP adrese. Procena Vaše lokacije uključuje slanje nekih od ovih informacija Google-ovom servisu za geolociranje, koja ima sopstvene [Polise privatnosti](https://www.google.com/privacy/lsf.html).
{: #location-services }

* **Izveštavanje o padovima**: Imate mogućnost da pošaljete Mozilla-i izveštaj o padu nakon što Firefox padne. Ovaj izveštaj sadrži tehničke informacije koje nam pomažu da unapredimo Firefox, uključujući razloge zbog kojih je došlo do pada Firefox-a, aktivni URL-ovi i stanje računarske memorije tokom pada. Izveštaj o padu koji dobijemo može sadržati lične podatke. Delove izveštaja o padu javno objavljujemo na adresi <https://crash-stats.mozilla.com>. Pre nego što javno objavimo izveštaje o padu, preduzimamo mere automatskog brisanja ličnih podatake. Ne brišemo ništa od onoga što eventualno napišete u polju za komentare.
{: #crash-reporter .inproduct-link }

* **Dodaci**: Firefox nudi stranicu „Get Add-ons“ u okviru „Add-ons Manager“ na kojoj su dati popularni dodaci i prikazuje personalizovane preporuke na osnovu dodataka koje ste već instalirali. Radi prikazivanja personalizovanih preporuka, Firefox šalje informacije Mozilla-i, uključujući i listu dodataka koje ste instalirali, podatke o verziji Firefox-a i Vašu IP adresu. Ova komunikacija se dešava samo kada je deo „Get Add-ons“ otvoren, a može se isključiti tako što ćete pratiti [ova uputstva](https://blog.mozilla.org/addons/how-to-opt-out-of-add-on-metadata-updates). „Add-ons Manager“ unutar Firefox-a ima polje za pretragu u koje možete uneti ključne reči za pretraživanje, a Mozilla prikuplja unete ključne reči, kao i informacije o verziji Firefox-a, jeziku i OS kako bi Vam prikazao preporuke.
{: #addons }
