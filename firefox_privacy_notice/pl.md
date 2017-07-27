# Zasady prywatności przeglądarki Firefox

20 lipca 2017 r\.
{: datetime="2017-07-20" }

Przywiązujemy dużą wagę do ochrony prywatności użytkowników. Gdy przeglądarka Firefox przesyła informacje do firmy Mozilla (to my), sposób ich wykorzystania przez nas reguluje [Polityka prywatności firmy Mozilla](https://www.mozilla.org/privacy/).

## Co warto wiedzieć

Firefox automatycznie nawiązuje połączenia z nami i naszymi dostawcami usług, by udostępniać aktualizacje, funkcje zabezpieczeń, wycinki, raport o kondycji przeglądarki Firefox i inne funkcje.
{: #essential-features }

* **Aktualizacje przeglądarki i dodatków**
{: #auto-updates }

	Aktualizacje przeglądarki: Firefox raz dziennie wysyła do firmy Mozilla następujące informacje, by sprawdzić dostępność aktualizacji przeglądarki: informacje o wersji przeglądarki Firefox, preferencje językowe, system operacyjny i jego wersja. Można [wyłączyć aktualizacje, wykonując te instrukcje](https://support.mozilla.org/kb/how-stop-firefox-automatically-making-connections#w_auto-update-checking), ale zwiększa to zagrożenia związane z lukami w zabezpieczeniach.

	Lista blokowanych dodatków: Firefox raz dziennie kontaktuje się z firmą Mozilla, by sprawdzić informacje o niebezpiecznych dodatkach. Obejmują one na przykład: wersję przeglądarki, system operacyjny i jego wersję, ustawienia regionalne, całkowitą liczbę żądań, czas ostatniego żądania, porę dnia, adres IP i listę zainstalowanych dodatków. Można [wyłączyć aktualizacje metadanych](https://blog.mozilla.org/addons/how-to-opt-out-of-add-on-metadata-updates/), ale zwiększa to zagrożenia związane z lukami w zabezpieczeniach.

* **Wycinki**
{: #snippets }

	Domyślna strona główna przeglądarki Firefox (&lt;about:home&gt;) wczytuje tuż pod paskiem wyszukiwania niewielkie porcje informacji, które naszym zdaniem mogą być przydatne dla użytkownika. Nazywamy je „wycinkami”. Około raz dziennie Firefox łączy się z firmą Mozilla i pobiera informacje o nowych wycinkach, jeśli są dostępne. Mozilla może gromadzić dane dotyczące częstotliwości kliknięć wycinków, ich nazw, ustawień regionalnych przeglądarki oraz używanej wersji Firefoksa. Dane te są przechowywane po 60 dniach jedynie w formie zagregowanej.

	Aby umożliwić wyświetlanie właściwych wycinków, Firefox co miesiąc wysyła do firmy Mozilla żądanie wyszukiwania lokalizacji użytkownika na poziomie kraju na podstawie adresu IP. Wysyłamy te informacje z powrotem do przeglądarki, gdzie są przechowywane lokalnie. Następnie na podstawie lokalnie przechowywanych informacji o kraju Firefox dobiera wyświetlane użytkownikowi wycinki.

	Niektóre sponsorowane przez firmę Mozilla wycinki są interaktywne i umożliwiają opcjonalne udostępnienie numeru telefonu bądź adresu e-mail. Można na przykład podać numer telefonu, by otrzymać SMS-a w celu zainstalowania przeglądarki Firefox w systemie Android. Informacje użytkownika są odbierane i przetwarzane przez naszego dostawcę usług marketingowych dla urządzeń mobilnych i poczty e-mail.

* **Raport o kondycji przeglądarki Firefox**
{: #health-report .inproduct-link }

	Raport o kondycji przeglądarki Firefox ma na celu udostępnienie użytkownikowi informacji o sprawności i stabilności przeglądarki oraz wskazówek dotyczących pomocy technicznej w przypadku problemów, takich jak duża liczba awarii lub długi czas uruchamiania. Mozilla gromadzi i agreguje dane użytkownika przeglądarki Firefox i wysyła je z powrotem do przeglądarki, aby pokazać użytkownikowi, jak sprawność przeglądarki zmienia się wraz z upływem czasu. Dane te obejmują między innymi sprzęt, system operacyjny, wersję przeglądarki Firefox, dodatki (liczba i typ), czas zdarzeń przeglądarki, renderowanie, liczbę przywróconych sesji, długość sesji, interakcję z punktami dostępu do wyszukiwania i wykorzystanie kodów partnerów wyszukiwania przeglądarki Firefox, wiek profilu, liczbę awarii oraz liczbę stron. W raporcie nie są wysyłane do firmy Mozilla odwiedzane przez użytkownika adresy URL.

	Dane wysyłane za pośrednictwem raportu wykorzystujemy, by udostępniać użytkownikom jego funkcje, takie jak możliwość analizowania i rozwiązywania problemów z działaniem przeglądarki. Informacji uzyskanych z danych raportu używamy także do ulepszania przeglądarki Firefox. Możesz [wyłączyć udostępnianie danych](https://support.mozilla.org/kb/firefox-health-report-understand-your-browser-perf#w_how-to-turn-data-sharing-on-or-off).

* **Bezpieczeństwo**
{: #security }

	Firefox automatycznie sprawdza niebezpieczne lub sfałszowane witryny internetowe, uszkodzone dodatki i wystawiane przez inne firmy certyfikaty SSL.

	Certyfikaty bezpiecznych witryn internetowych: gdy użytkownik odwiedza bezpieczną witrynę internetową (tj. „https”), Firefox weryfikuje jej certyfikat. Może się to wiązać z nawiązaniem komunikacji ze wskazanym przez certyfikat zewnętrznym dostawcą stanu. Firefox wysyła do niego informacje identyfikujące [certyfikat](https://support.mozilla.org/kb/secure-website-certificate) witryny. Możesz [zmienić ustawienia](https://support.mozilla.org/kb/advanced-settings-browsing-network-updates-encryption#w_certificates-tab), ale jeśli wyłączysz funkcję weryfikacji online, przeglądarka Firefox nie będzie mogła potwierdzać tożsamości odwiedzanych witryn. Wyłączenie tej funkcji może zwiększyć ryzyko przechwycenia prywatnych informacji użytkownika. Jeśli użytkownik natrafi na[niezaufane połączenie](https://support.mozilla.org/kb/connection-untrusted-error-message), może wysłać do firmy Mozilla skojarzone z nim certyfikaty.

	Ochrona przeglądarki Firefox przed atakami i fałszerstwami: około dwa razy na godzinę Firefox pobiera listę bezpiecznego przeglądania Google, by blokować dostęp do witryn i plików, które są niebezpieczne lub sfałszowane (polityka prywatności Google jest dostępna na stronie <https://www.google.com/policies/privacy/>). W przypadku pobranych plików wykonywalnych, które nie znajdują się na tej liście, Firefox może wysyłać metadane, w tym powiązane z nimi adresy URL, do usługi bezpiecznego przeglądania. Więcej informacji na temat funkcji bezpiecznego przeglądania i możliwości jej wyłączenia można znaleźć na stronie <https://support.mozilla.org/kb/how-does-phishing-and-malware-protection-work>. Jeśli te funkcje zostaną wyłączone, Firefox nie będzie w stanie ostrzegać o potencjalnie nielegalnych albo niebezpiecznych witrynach lub plikach do pobrania.

* **Statystyki użytkowania** (określane w wersjach niefinalnych jako „Telemetria”)
{: #telemetry .inproduct-link}

	Statystyki użytkowania (czy też „Telemetria”) to funkcja przeglądarki Firefox, która wysyła do firmy Mozilla statystyki użytkowania, wydajności i reaktywności dotyczące funkcji interfejsu, pamięci i konfiguracji sprzętowej. W ramach standardowego dziennika internetowego pobierany jest także adres IP użytkownika. Statystyki użytkowania są transmitowane przy użyciu protokołu SSL i pomagają nam udoskonalać przyszłe wersje przeglądarki Firefox. Po wysłaniu statystyk użytkowania do firmy Mozilla są one agregowane i udostępnianie szerokiemu gronu programistów, wśród których są zarówno pracownicy firmy Mozilla, jak i zewnętrzni twórcy. Gdy Telemetria jest włączona, niektóre krótkoterminowe eksperymenty mogą zbierać informacje na temat odwiedzanych witryn.

	Funkcja ta jest włączona domyślnie w wersjach Nightly i Beta/Developer przeglądarki Firefox, by ułatwić ich użytkownikom przesyłanie informacji do firmy Mozilla. W ogólnodostępnej finalnej wersji przeglądarki Firefox ta funkcja jest domyślnie wyłączona.

	[Tutaj można dowiedzieć się więcej o Telemetrii](https://support.mozilla.org/kb/send-performance-data-improve-firefox) oraz sposobach jej włączania i wyłączania.

* **Miniatury**
{: #searchsuggestions }

	Podpowiedzi wyszukiwania to funkcja, która pomaga znaleźć hasła, których często szukali inni użytkownicy. Podpowiedzi są dostarczane przez domyślną wyszukiwarkę (np. Google, Yahoo itp.), a nie przez Firefoksa. Jeśli używana domyślna wyszukiwarka obsługuje podpowiedzi, po włączeniu tej funkcji Firefox może wysyłać hasła wpisywane w pasku Awesome Bar lub w pasku wyszukiwania do domyślnej wyszukiwarki, by pobrać podpowiedzi. Podlega to Polityce prywatności domyślnej wyszukiwarki. [Więcej informacji o podpowiedziach wyszukiwania można znaleźć tutaj](https://support.mozilla.org/kb/use-popular-search-suggestions-firefox-search-bar), razem z informacjami, jak włączyć i wyłączyć tę funkcję.

* **Polecenia i śledzenie kampanii**{: #thirdparty } ** **{: #referraltracking }

	Aby pomóc nam zrozumieć i ulepszyć kampanie marketingowe, Firefox domyślnie wysyła pewne informacje. Obejmuje to „dane poleceń”, takie jak informacje o domenie witryny lub kampanii reklamowej, która poleciła pobranie i zainstalowanie przeglądarki Firefox, a także „dane interakcji” dotyczące wykorzystywanych funkcji przeglądarki.

	__Dane poleceń__
	W systemach Android i iOS przeglądarka Firefox wysyła dane poleceń do naszego dostawcy analityki mobilnej i obejmują one także identyfikator reklamowy Google, adres IP, sygnaturę czasową, kraj, ustawienia lokalne oraz wersję systemu operacyjnego i aplikacji. Więcej informacji, w tym sposób wyłączania tych raportów, znajdziesz[tutaj](https://support.mozilla.org/kb/desktop-attribution-privacy).

	Na komputerach przeglądarka Firefox rejestruje i wysyła dane poleceń do firmy Mozilla w ramach raportu o kondycji przeglądarki. Więcej informacji, w tym sposób rezygnacji z tych raportów lub ich wyłączenia, znajdziesz[tutaj](https://support.mozilla.org/kb/desktop-attribution-privacy).

	__Dane interakcji__
	W systemie iOS przeglądarka Firefox wysyła dane interakcji do naszego dostawcy usług marketingu mobilnego, firmy Leanplum, która ma własną [politykę prywatności](https://www.leanplum.com/privacy/). Dane te pozwalają nam testować różne funkcje i interfejsy, a także dostarczać personalizowane wiadomości i rekomendacje pozwalające użytkownikom lepiej korzystać z przeglądarki Firefox. Więcej informacji na temat zbierania tych danych znajdziesz [tutaj](https://github.com/mozilla-mobile/firefox-ios/blob/master/MMA.md), możesz też [wyłączyć tę funkcję](https://support.mozilla.org/kb/send-anonymous-usage-data-firefox-mobile-devices).

---------------------------------------

Jeśli użytkownik o to poprosi, Firefox łączy się także z firmą Mozilla, by udostępnić funkcje takie jak Sync, usługi lokalizacji, zgłaszanie awarii i dodatki.
{: #optional-features }

* **Sync**
{: #sync }

	[Firefox Sync](https://www.mozilla.org/firefox/sync/) to usługa, która umożliwia synchronizowanie zakładek, historii przeglądania, haseł i ustawień przeglądarki Firefox na wszystkich urządzeniach użytkownika. Jeśli usługa Sync jest używana, warto zapoznać się z [Polityką prywatności usługi Firefox Sync](https://accounts.firefox.com/legal/privacy).

* **Usługi lokalizacji**
{: #location-services }

	w Firefox dostępna jest funkcja, która umożliwia witrynom wysłanie żądania ustalenia lokalizacji użytkownika (np. by umożliwić wyświetlenie jej na mapie). Jeśli witryna zażąda lokalizacji użytkownika, przed jej ustaleniem i udostępnieniem Firefox pyta użytkownika o pozwolenie. Aby określić lokalizację użytkownika, Firefox może wykorzystać kilka rodzajów danych, w tym funkcje lokalizacji geograficznej systemu operacyjnego, sieci Wi-Fi, stacje bazowe telefonii komórkowej i adres IP. Oszacowanie lokalizacji użytkownika wymaga wysłania części z tych informacji do usługi lokalizacji geograficznej firmy Google, która ma własną [politykę prywatności](https://www.google.com/privacy/lsf.html).

* **Zgłaszanie awarii**
{: #crash-reporter .inproduct-link }

	po awarii przeglądarki Firefox użytkownik ma możliwość wysłania do firmy Mozilla raportu o awarii. Zawiera on informacje techniczne pozwalające nam udoskonalić przeglądarkę, w tym przyczynę awarii, aktywny adres URL oraz stan pamięci komputera w momencie awarii. Otrzymany przez nas raport o awarii może zawierać dane osobowe. Fragmenty raportów o awariach udostępniamy publicznie na stronie <https://crash-stats.mozilla.com/>. Przed ich opublikowaniem automatycznie usuwamy dane osobowe. Nie redagujemy treści, które użytkownicy wpisują w polu komentarzy.

* **Błędy SSL**
{: #ssl-errors }

	Po przerwaniu bezpiecznego połączenia z witryną użytkownik ma możliwość wysłania do firmy Mozilla raportu o błędzie. Raport zawiera certyfikat witryny oraz diagnostyczne kody błędów. Informacje te pomagają firmie Mozilla monitorować skuteczność „przypiętych” certyfikatów witryn i wykrywać potencjalne ataki mające na celu wyłudzenie danych osobowych naszych użytkowników.

* **Dodatki**
{: #addons }

	Firefox udostępnia stronę Pobierz dodatki w Menedżerze dodatków. Zawiera ona popularne dodatki i wyświetla spersonalizowane rekomendacje na podstawie zainstalowanych już przez użytkownika dodatków. Aby wyświetlać spersonalizowane rekomendacje, Firefox wysyła do firmy Mozilla informacje, w tym listę zainstalowanych dodatków, informacje o wersji przeglądarki Firefox i adres IP użytkownika. Komunikacja ma miejsce tylko wtedy, gdy otwarty jest obszar Pobierz dodatki. Można ją wyłączyć, wykonując [te instrukcje](https://blog.mozilla.org/addons/how-to-opt-out-of-add-on-metadata-updates/). W Menedżerze dodatków w przeglądarce Firefox dostępne jest pole wyszukiwania, w którym można wprowadzać hasła do wyszukania. Mozilla zbiera informacje o wyszukiwanych hasłach, a także o wersji przeglądarki Firefox, ustawieniach regionalnych oraz systemie operacyjnym, by wyświetlać rekomendacje dla użytkownika.

* **Powiadomienia wypychane**
{: #push-notifications }

	Powiadomienia wypychane umożliwiają witrynom wysyłanie powiadomień i aktualizacji, jeśli użytkownik wyrazi na to zgodę. Aby otrzymywać powiadomienia, Firefox wysyła do firmy Mozilla informacje o witrynach, z których użytkownik zgodził się je otrzymywać. Informacje te przechowujemy w formie zanonimizowanej wraz z liczbą powiadomień, które wysyła użytkownikowi każda z witryn. Aby pomóc programistom lepiej wykorzystywać powiadomienia wypychane, Mozilla może udostępniać niektórym programistom zagregowane dane, w tym liczbę użytkowników odwiedzających witrynę, którzy zasubskrybowali jej powiadomienia wypychane lub anulowali ich subskrypcję. Powiadomieniami wypychanymi w Firefoksie można zarządzać, wykonując [te instrukcje](https://support.mozilla.org/kb/push-notifications-firefox).

* **Firefox Screenshots**
{: #screenshots }

	__Przesłane zrzuty ekranu__
	Przesłane zrzuty ekranu są wysyłane do firmy Mozilla i przechowywane przez wskazany ograniczony czas, który można zmienić.  Przesłane zrzuty ekranu możemy wykorzystać, gdy będzie to niezbędne do świadczenia usługi. Przesłane zrzuty ekranu można w każdej chwili usunąć.  

	__Dane interakcji__
	Otrzymujemy dane, takie jak informacje o odwiedzeniu witryny Firefox Screenshots, jak często przesłane zrzuty ekranu są otwierane i udostępniane (przez użytkownika i inne osoby) oraz informacje o interakcji z przyciskami, kafelkami i ruchach myszy powiązanych z wykonywaniem zrzutów ekranu. 
Dane zbierane podczas odwiedzin witryny Firefox Screenshots opisują nasze [zasady prywatności dotyczące witryn](https://www.mozilla.org/privacy/websites/). 

	__Dane techniczne__
	Otrzymujemy dane dotyczące przeciętnego rozmiaru i liczby przesłanych zrzutów ekranu, wersji przeglądarki Firefox, systemu operacyjnego urządzenia oraz błędów. Adres IP, z którego otwierana jest witryna Firefox Screenshots, jest przechowywany chwilowo jako element standardowego dziennika serwera. 

	Pełną dokumentację znajdziesz [tutaj](https://github.com/mozilla-services/screenshots/blob/master/docs/METRICS.md), możesz też usunąć swoje zrzuty ekranu [tutaj](https://screenshots.firefox.com/leave-screenshots).

Z wyjątkiem przypadków, w których stwierdzono inaczej, niniejsze zasady prywatności dotyczą najnowszych wersji publicznie dostępnego wydania przeglądarki Firefox. Wersje rozwojowe (Beta/Developer Edition, Nightly i TestFlight) są nadal aktywnie rozwijane i mogą zawierać nowe funkcje, a na prywatność związaną z ich używaniem wpływają inne kwestie. Wersje rozwojowe automatycznie wysyłają [dane telemetrii](https://gecko.readthedocs.io/en/latest/toolkit/components/telemetry/telemetry/index.html) do firmy Mozilla. Dane te pomagają nam w usprawnianiu przeglądarki Firefox.
{: #pre-release }
