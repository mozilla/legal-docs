# Firefox böngésző Adatvédelmi tájékoztató

2014\. április 15.
{: datetime="2014-04-15" }

Fontos számunkra az Ön adatainak védelme. Ha a Firefox adatokat küld a Mozilla (ez minket jelent) számára, akkor [adatvédelmi irányelveink](https://www.mozilla.org/privacy/) írják le ezek kezelésének módját.

## Tudnivalók

A Firefox automatikusan csatlakozik hozzánk és szolgáltatóinkhoz frissítések, biztonsági elemek, kódrészletek, Firefox állapotjelentés és egyéb funkciók biztosítása érdekében. 
{: #essential-features }

* Böngésző és kiegészítők frissítése
  {: #auto-updates }

	Böngészőfrissítések: Naponta egyszer a Firefox a következő adatokat küldi el a Mozillának, amikor az böngészőfrissítéseket keres: az Ön Firefox verziójának adatai, a nyelvi beállítás, az operációs rendszer és annak verziója. Megteheti, hogy [kikapcsolja a frissítéseket a következő utasítások szerint](https://support.mozilla.org/kb/how-stop-firefox-automatically-making-connections#w_auto-update-checking), de ez biztonsági szempontból sérülékenységet jelenthet az Ön számára.

	Letiltott kiegészítők listája: A Firefox naponta egyszer kapcsolatba lép a Mozillával, és egyezteti a kiegészítők adatait, hogy a rosszindulatú kiegészítőket ellenőrizhesse. Ez magában foglalja például a következőket: böngészőverzió, operációs rendszer és verzió, területi beállítás, összes kérés száma, a legutóbbi kérés dátuma, a napon belül az időpont, IP-cím és az Ön által telepített kiegészítők listája. Bármikor megteheti, hogy [kikapcsolja a metaadatok frissítését](https://blog.mozilla.org/addons/how-to-opt-out-of-add-on-metadata-updates/), de ez biztonsági szempontból sérülékenységet jelenthet az Ön számára.

* Kódrészletek
  {: #snippets }

	A Firefox alapértelmezett kezdőlapja (&lt;about:home&gt;) közvetlenül a keresősáv alatt olyan rövid tájékoztatásokat jelenít meg, amelyeket az Ön számára hasznosnak ítélünk. Ezeket „kódrészleteknek” nevezzük. Körülbelül naponta egy alkalommal a Firefox csatlakozik a Mozillához és új kódrészleteket nyújt Önnek, ha vannak ilyenek. A Mozilla összesíti, hogy milyen gyakran kattintanak rá a kódrészletekre, a kódrészlet nevét, a böngésző területi beállításait és hogy a Firefox melyik verzióját használja.

	Annak érdekében, hogy megfelelő kódrészleteket jelenítsen meg, a Firefox IP-címe segítségével havonta lekérdezi a Mozillától az Ön országszintű tartózkodási helyét. Utána az országszintű adatokat visszaküldjük a Firefox-nak, amely helyileg tárolja ezeket. A Firefox az Önnek megjelenő kódrészleteket a helyileg tárolt országszintű adat alapján fogja kiválasztani.

* Firefox állapotjelentés
  {: #health-report .inproduct-link } 

	A Firefox állapotjelentés (FHR) célja, hogy az Ön számára rálátást nyújtson saját böngészője stabilitására és teljesítményére, és hogy tippek formájában támogassa Önt, amikor problémát észlel, például gyakori összeomlást vagy lassú indítást. A Mozilla más Firefox felhasználókéval együtt és összesítve gyűjti az Ön adatait, és visszaküldi az Ön saját böngészőjére, hogy Ön láthassa, hogyan változik a Firefox teljesítménye az idő múlásával. Ezek az adatok magukban foglalják például a következőket: hardver eszköz, operációs rendszer, Firefox verzió, kiegészítők (száma és típusa), a böngészési események időzítése, feldolgozás, munkamenet helyreállítása, munkamenet hossza, profil kora, összeomlások száma és az oldalak száma. Az FHR nem tartalmazza az Ön által látogatott oldalak URL címeit.

	Az FHR-en keresztül küldött adatokat arra használjuk, hogy biztosítsuk a felhasználók számára a működőképességet, és hogy megoldjuk böngészője teljesítménnyel kapcsolatos problémáit. Arra is felhasználjuk az FHR adatok alapján leszűrteket, hogy fejlesszük a Firefox-ot. Dönthet úgy, hogy [kikapcsolja az adatmegosztást](https://support.mozilla.org/kb/firefox-health-report-understand-your-browser-perf#w_how-to-turn-data-sharing-on-or-off).

* Biztonság
  {: #security }

	A Firefox automatikusan ellenőrzi a rosszindulatú vagy hamisított webhelyeket, a sérült kiegészítőket és a harmadik fél által kibocsátott SSL tanúsítványokat.

	Biztonságos webhely tanúsítványok: Ha Ön felkeres egy biztonságos webhelyet (pl. „https”), akkor a Firefox ellenőrzi a webhely tanúsítványát. Ennek része lehet a tanúsítvány által megjelölt állapotszolgáltatóval folytatott kommunikáció. A Firefox elküldi ezeket a harmadik féltől kapott adatokat, amelyek igazolják a webhely [tanúsítványát](https://support.mozilla.org/kb/secure-website-certificate). Lehetősége van [megváltoztatni a beállításait](https://support.mozilla.org/kb/advanced-settings-browsing-network-updates-encryption#w_certificates-tab), de ha kikapcsolja az online hitelesítés funkciót, akkor a Firefox nem képes megerősíteni az Ön által felkeresett webhely azonosítóját. Ennek a funkciónak a kikapcsolása növelheti annak kockázatát, hogy megszerzik a személyes adatait. Ha [nem megbízható kapcsolatot](https://support.mozilla.org/kb/connection-untrusted-error-message)észlel, akkor elküldheti a Mozillának az ahhoz rendelt tanúsítványokat.

	Firefox hamisítás és támadás elleni védelem: Körülbelül óránként kétszer a Firefox letölti a Google SafeBrowsing listáját, ezzel járul hozzá a rosszindulatú vagy hamisított webhelyekhez és letöltésekhez való hozzáférés megakadályozásához (a Google adatvédelmi irányelvei itt érhetők el: <https://www.google.com/policies/privacy/>). Az ezeken a listákon nem szereplő letöltött végrehajtható elemek esetén a Firefox a letöltött fájlhoz kapcsolódó metaadatokat – beleértve az URL-t – elküldheti a SafeBrowsing szolgáltatás részére. Keresse fel a(z) <https://support.mozilla.org/kb/how-does-phishing-and-malware-protection-work> webhelyet, hogy további információkat kapjon a SafeBrowsing szolgáltatásról, vagy hogy kikapcsolja azt. Ha kikapcsolja ezeket a funkciókat, a Firefox nem tudja figyelmeztetni Önt a potenciálisan illegitim vagy rosszindulatú webhelyekre vagy letöltött fájlokra.

* Használati statisztikák (más néven „Telemetria” ki nem adott build esetén)
  {: #telemetry .inproduct-link}

	A használati statisztikák vagy „Telemetria” a Firefox azon funkciója, amely elküldi a Mozilla használati, teljesítményre és reakcióidőre vonatkozó statisztikáit a felhasználói felület funkcióival, memóriájával és hardverkonfigurációjával összefüggésben. A szokásos webes naplózás részként az Ön IP-címét is gyűjti a rendszer. A használati statisztikákat SSL alkalmazásával továbbítják, és ezek segítenek bennünket a Firefox jövőbeli verzióinak tökéletesítésében. A Mozillához küldést követően a használati statisztikákat összesítik, és fejlesztők széles köre számára teszik hozzáférhetővé, beleértve a Mozilla alkalmazottait és közreműködőit.

	Ez a funkció alapértelmezés szerint engedélyezett a Firefox Nightly, Aurora és Beta build változatainál, hogy segítse azokat a felhasználókat, akik visszajelzést adnak a Mozillának. A Firefox általános kiadott változatai esetében alapértelmezett beállításként ez a funkció ki van kapcsolva.

	Itt [tudhat meg többet a telemetriáról](https://support.mozilla.org/kb/send-performance-data-improve-firefox) és annak be- vagy kikapcsolásáról. 

* Csempék

	A csempe a Firefox által az új oldalakon megjelenített funkciót jelenti. A csempe funkció biztosítása érdekében a Firefox elküldi a Mozillának a csempékkel kapcsolatos adatokat, például a kattintások és megjelenítések számát, az Ön IP-címét, a területi beállításokra vonatkozó adatokat és a csempe specifikus adatokat (pl. a rács helyzete és mérete). A Firefox Beta változatánál bizonyos rövid távú Telemetriás kísérletek (lásd fenn) adatokat gyűjthetnek a gyakran látogatott domainekről a csempe funkcióhoz.

---------------------------------------

Az Ön kérésére is csatlakozik a Firefox a Mozillához, hogy Önnek funkciókat biztosítson, például a Sync funkciót, helymeghatározási szolgáltatásokat, összeomlás jelentést és kiegészítőket.
{: #optional-features }

* **Sync**: [A Firefox Sync](https://www.mozilla.org/firefox/sync/) olyan szolgáltatás, amelynek révén szinkronizálhatja Firefox könyvjelzőit, böngészési előzményeit, jelszavait és beállításait minden eszközén. Amennyiben használja a Sync szolgáltatást, akkor olvassa el a [Firefox Sync Adatvédelmi tájékoztatót](https://services.mozilla.com/privacy-policy/)
{: #sync }

* **Helymeghatározási szolgáltatások**: A Firefox rendelkezik olyan funkcióval, amelynek révén a webhelyek lekérhetik az Ön tartózkodási helyét (pl. azért, hogy ezek a webhelyek feltüntethessék az Ön helyét térképen). Ha egy webhely kéri az Ön tartózkodási helyének adatait, akkor a Firefox az Ön engedélyét kéri, mielőtt meghatározná vagy megosztaná az Ön tartózkodási helyét. Az Ön helyének meghatározása során a Firefox számos adatot felhasználhat, beleértve az Ön operációs rendszerének földrajzi helyének jellemzőit, a WiFi hálózatokat, mobiltornyokat vagy IP-címet. Az Ön tartózkodási helyének megállapítása során előfordulhat, hogy ezen adatok egy részét elküldjük a Google földrajzihely-szolgáltatásához, amely rendelkezik saját [adatvédelmi irányelvvel](https://www.google.com/privacy/lsf.html).
{: #location-services }

* **Összeomlási jelentés**: Önnek lehetősége van rá, hogy a Firefox összeomlása után összeomlási jelentést küldjön a Mozillának. Ebben a jelentésben műszaki adatok szerepelnek, amelyek segítségével fejleszthetjük a Firefox-ot, beleértve a Firefox összeomlásának okát, az összeomlás idején aktív URL-t, és a számítógép memóriájának állapotát az összeomlás idején. Az összeomlási jelentés részeként személyes adatok is eljuthatnak hozzánk. Az összeomlási jelentések egyes részeit nyilvánosságra hozzuk itt: <https://crash-stats.mozilla.com/>. Az összeomlási jelentések közzétételét megelőzően lépéseket teszünk a személyes adatok automatikus kivonása érdekében. Nem távolítunk el semmit, amit Ön írt a megjegyzés mezőbe.
{: #crash-reporter .inproduct-link }

* **Kiegészítők**: A Firefox a kiegészítőkezelő a népszerű kiegészítőket tartalmazó kiegészítők letöltése oldalát ajánlja, és személyes ajánlásokat jelenít meg az Ön által már telepített kiegészítőkre vonatkozóan. A személyes ajánlások megjelenítéséhez a Firefox adatokat küld a Mozillának, beleértve az Ön által telepített kiegészítők listáját, a Firefox verzióadatait és az Ön IP-címét. Erre a közlésre csak akkor kerül sor, ha a Kiegészítők letöltése terület meg van nyitva, és ki lehet kapcsolni a következő [utasításokat követve](https://blog.mozilla.org/addons/how-to-opt-out-of-add-on-metadata-updates/). A Firefox kiegészítőkezelője olyan keresési mezővel rendelkezik, amelyben megadhatja a keresés kulcsszavait, és a Mozilla összegyűjti ezeket a keresési kulcsszavakat, valamint az Ön Firefox verziójának adatait, területi beállításait, és operációs rendszerét, hogy ajánlásokat mutathasson Önnek.
{: #addons }
