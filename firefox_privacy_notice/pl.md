# Zasady prywatności przeglądarki Firefox

15.04.2014
{: datetime="2014-04-15" }

Przywiązujemy dużą wagę do ochrony prywatności użytkowników. Gdy przeglądarka Firefox przesyła informacje do firmy Mozilla (to my), sposób ich wykorzystania przez nas reguluje [Polityka prywatności firmy Mozilla](https://www.mozilla.org/privacy/).

## Co warto wiedzieć

Firefox automatycznie nawiązuje połączenia z nami i naszymi dostawcami usług, by udostępniać aktualizacje, funkcje zabezpieczeń, wycinki, raport o kondycji przeglądarki Firefox i inne funkcje. 
{: #essential-features }

* Aktualizacje przeglądarki i dodatków
  {: #auto-updates }

	Aktualizacje przeglądarki: Firefox raz dziennie wysyła do firmy Mozilla następujące informacje, by sprawdzić dostępność aktualizacji przeglądarki: informacje o wersji przeglądarki Firefox, preferencje językowe, system operacyjny i jego wersja. Można [wyłączyć aktualizacje, wykonując te instrukcje](https://support.mozilla.org/kb/how-stop-firefox-automatically-making-connections#w_auto-update-checking), ale zwiększa to zagrożenia związane z lukami w zabezpieczeniach.

	Lista blokowanych dodatków: Firefox raz dziennie kontaktuje się z firmą Mozilla, by sprawdzić informacje o niebezpiecznych dodatkach. Obejmują one na przykład: wersję przeglądarki, system operacyjny i jego wersję, ustawienia regionalne, całkowitą liczbę żądań, czas ostatniego żądania, porę dnia, adres IP i listę zainstalowanych dodatków. Można [wyłączyć aktualizacje metadanych](https://blog.mozilla.org/addons/how-to-opt-out-of-add-on-metadata-updates/), ale zwiększa to zagrożenia związane z lukami w zabezpieczeniach.

* Wycinki
  {: #snippets }

	Domyślna strona główna przeglądarki Firefox (&lt;about:home&gt;) wczytuje tuż pod paskiem wyszukiwania niewielkie porcje informacji, które naszym zdaniem mogą być przydatne dla użytkownika. Nazywamy je „wycinkami”. Około raz dziennie Firefox łączy się z firmą Mozilla i pobiera informacje o nowych wycinkach, jeśli są dostępne. Mozilla agreguje dane dotyczące częstotliwości kliknięć wycinków, ich nazw, ustawień regionalnych przeglądarki oraz używanej wersji Firefoksa.

	Aby umożliwić wyświetlanie właściwych wycinków, Firefox co miesiąc wysyła do firmy Mozilla żądanie wyszukiwania lokalizacji użytkownika na poziomie kraju na podstawie adresu IP. Wysyłamy te informacje z powrotem do przeglądarki, gdzie są przechowywane lokalnie. Następnie na podstawie lokalnie przechowywanych informacji o kraju Firefox dobiera wyświetlane użytkownikowi wycinki.

* Raport o kondycji przeglądarki Firefox
  {: #health-report .inproduct-link } 

	Raport o kondycji przeglądarki Firefox ma na celu udostępnienie użytkownikowi informacji o sprawności i stabilności przeglądarki oraz wskazówek dotyczących pomocy technicznej w przypadku problemów, takich jak duża liczba awarii lub długi czas uruchamiania. Mozilla gromadzi i agreguje dane użytkownika przeglądarki Firefox i wysyła je z powrotem do przeglądarki, aby pokazać użytkownikowi, jak sprawność przeglądarki zmienia się wraz z upływem czasu. Dane te obejmują na przykład: sprzęt, system operacyjny, wersję przeglądarki Firefox, dodatki (liczba i typ), czas zdarzeń przeglądarki, renderowanie, liczbę przywróconych sesji, długość sesji, wiek profilu, liczbę awarii oraz liczbę stron. W raporcie nie są wysyłane do firmy Mozilla odwiedzane przez użytkownika adresy URL.

	Dane wysyłane za pośrednictwem raportu wykorzystujemy, by udostępniać użytkownikom jego funkcje, takie jak możliwość analizowania i rozwiązywania problemów z działaniem przeglądarki. Informacji uzyskanych z danych raportu używamy także do ulepszania przeglądarki Firefox. Możesz [wyłączyć udostępnianie danych](https://support.mozilla.org/kb/firefox-health-report-understand-your-browser-perf#w_how-to-turn-data-sharing-on-or-off).

* Bezpieczeństwo
  {: #security }

	Firefox automatycznie sprawdza niebezpieczne lub sfałszowane witryny internetowe, uszkodzone dodatki i wystawiane przez inne firmy certyfikaty SSL.

	Certyfikaty bezpiecznych witryn internetowych: gdy użytkownik odwiedza bezpieczną witrynę internetową (tj. „https”), Firefox weryfikuje jej certyfikat. Może się to wiązać z nawiązaniem komunikacji ze wskazanym przez certyfikat zewnętrznym dostawcą stanu. Firefox wysyła do niego informacje identyfikujące [certyfikat](https://support.mozilla.org/kb/secure-website-certificate) witryny. Możesz [zmienić ustawienia](https://support.mozilla.org/kb/advanced-settings-browsing-network-updates-encryption#w_certificates-tab), ale jeśli wyłączysz funkcję weryfikacji online, przeglądarka Firefox nie będzie mogła potwierdzać tożsamości odwiedzanych witryn. Wyłączenie tej funkcji może zwiększyć ryzyko przechwycenia prywatnych informacji użytkownika. Jeśli użytkownik natrafi na[niezaufane połączenie](https://support.mozilla.org/kb/connection-untrusted-error-message), może wysłać do firmy Mozilla skojarzone z nim certyfikaty.

	Ochrona przeglądarki Firefox przed atakami i fałszerstwami: około dwa razy na godzinę Firefox pobiera listę bezpiecznego przeglądania Google, by blokować dostęp do witryn i plików, które są niebezpieczne lub sfałszowane (polityka prywatności Google jest dostępna na stronie <https://www.google.com/policies/privacy/>). W przypadku pobranych plików wykonywalnych, które nie znajdują się na tej liście, Firefox może wysyłać metadane, w tym powiązane z nimi adresy URL, do usługi bezpiecznego przeglądania. Więcej informacji na temat funkcji bezpiecznego przeglądania i możliwości jej wyłączenia można znaleźć na stronie <https://support.mozilla.org/kb/how-does-phishing-and-malware-protection-work>. Jeśli te funkcje zostaną wyłączone, Firefox nie będzie w stanie ostrzegać o potencjalnie nielegalnych albo niebezpiecznych witrynach lub plikach do pobrania.

* Statystyki użytkowania (określane w wersjach niefinalnych jako „Telemetria”)
  {: #telemetry .inproduct-link}

	Statystyki użytkowania (czy też „Telemetria”) to funkcja przeglądarki Firefox, która wysyła do firmy Mozilla statystyki użytkowania, wydajności i reaktywności dotyczące funkcji interfejsu, pamięci i konfiguracji sprzętowej. W ramach standardowego dziennika internetowego pobierany jest także adres IP użytkownika. Statystyki użytkowania są transmitowane przy użyciu protokołu SSL i pomagają nam udoskonalać przyszłe wersje przeglądarki Firefox. Po wysłaniu statystyk użytkowania do firmy Mozilla są one agregowane i udostępnianie szerokiemu gronu programistów, wśród których są zarówno pracownicy firmy Mozilla, jak i zewnętrzni twórcy.

	Funkcja ta jest włączona domyślnie w wersjach Nightly, Aurora i Beta przeglądarki Firefox, by ułatwić ich użytkownikom przesyłanie informacji do firmy Mozilla. W ogólnodostępnej finalnej wersji przeglądarki Firefox ta funkcja jest domyślnie wyłączona.

	[Tutaj można dowiedzieć się więcej o Telemetrii](https://support.mozilla.org/kb/send-performance-data-improve-firefox) oraz sposobach jej włączania i wyłączania. 

* Miniatury

	Miniatury to funkcja przeglądarki Firefox wyświetlana na stronach nowych kart. Aby udostępniać funkcję miniatur, Firefox przesyła do firmy Mozilla powiązane z nimi dane, takie jak liczba kliknięć i wyświetleń, adres IP użytkownika, informacje o ustawieniach regionalnych i dane miniatur (np. położenie i rozmiar siatki). W przeglądarce Firefox Beta pewne krótkoterminowe eksperymenty związane z Telemetrią (patrz wyżej) dla funkcji Miniatury mogą zbierać informacje o często odwiedzanych domenach.

---------------------------------------

Jeśli użytkownik o to poprosi, Firefox łączy się także z firmą Mozilla, by udostępnić funkcje takie jak Sync, usługi lokalizacji, zgłaszanie awarii i dodatki.
{: #optional-features }

* **Sync**: [Firefox Sync](https://www.mozilla.org/firefox/sync/) to usługa, która umożliwia synchronizowanie zakładek, historii przeglądania, haseł i ustawień przeglądarki Firefox na wszystkich urządzeniach użytkownika. Jeśli usługa Sync jest używana, warto zapoznać się z [Polityką prywatności usługi Firefox Sync](https://services.mozilla.com/privacy-policy/).
{: #sync }

* **Usługi lokalizacji**: w Firefox dostępna jest funkcja, która umożliwia witrynom wysłanie żądania ustalenia lokalizacji użytkownika (np. by umożliwić wyświetlenie jej na mapie). Jeśli witryna zażąda lokalizacji użytkownika, przed jej ustaleniem i udostępnieniem Firefox pyta użytkownika o pozwolenie. Aby określić lokalizację użytkownika, Firefox może wykorzystać kilka rodzajów danych, w tym funkcje lokalizacji geograficznej systemu operacyjnego, sieci Wi-Fi, stacje bazowe telefonii komórkowej i adres IP. Oszacowanie lokalizacji użytkownika wymaga wysłania części z tych informacji do usługi lokalizacji geograficznej firmy Google, która ma własną [politykę prywatności](https://www.google.com/privacy/lsf.html).
{: #location-services }

* **Zgłaszanie awarii**: po awarii przeglądarki Firefox użytkownik ma możliwość wysłania do firmy Mozilla raportu o awarii. Zawiera on informacje techniczne pozwalające nam udoskonalić przeglądarkę, w tym przyczynę awarii, aktywny adres URL oraz stan pamięci komputera w momencie awarii. Otrzymany przez nas raport o awarii może zawierać dane osobowe. Fragmenty raportów o awariach udostępniamy publicznie na stronie <https://crash-stats.mozilla.com/>. Przed ich opublikowaniem automatycznie usuwamy dane osobowe. Nie redagujemy treści, które użytkownicy wpisują w polu komentarzy.
{: #crash-reporter .inproduct-link }

* **Dodatki**: Firefox udostępnia stronę Pobierz dodatki w Menedżerze dodatków. Zawiera ona popularne dodatki i wyświetla spersonalizowane rekomendacje na podstawie zainstalowanych już przez użytkownika dodatków. Aby wyświetlać spersonalizowane rekomendacje, Firefox wysyła do firmy Mozilla informacje, w tym listę zainstalowanych dodatków, informacje o wersji przeglądarki Firefox i adres IP użytkownika. Komunikacja ma miejsce tylko wtedy, gdy otwarty jest obszar Pobierz dodatki. Można ją wyłączyć, wykonując [te instrukcje](https://blog.mozilla.org/addons/how-to-opt-out-of-add-on-metadata-updates/). W Menedżerze dodatków w przeglądarce Firefox dostępne jest pole wyszukiwania, w którym można wprowadzać hasła do wyszukania. Mozilla zbiera informacje o wyszukiwanych hasłach, a także o wersji przeglądarki Firefox, ustawieniach regionalnych oraz systemie operacyjnym, by wyświetlać rekomendacje dla użytkownika.
{: #addons }
