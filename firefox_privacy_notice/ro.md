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

	Firefox automatically checks for malicious or forged web pages, broken add-ons, and third-party issued SSL certificates.

	Secure Website Certificates: When you visit a secure website (i.e. "https"), Firefox will validate the website's certificate. This may involve communicating with a third-party status provider specified by the certificate. Firefox sends to this third-party information identifying the site's [certificate](https://support.mozilla.org/kb/secure-website-certificate). You can [change your preferences](https://support.mozilla.org/kb/advanced-settings-browsing-network-updates-encryption#w_certificates-tab), but if you disable the online verification feature, Firefox cannot confirm the identity of the website you are visiting. Turning off this feature may increase the risk of your private information being intercepted. If you encounter an [untrusted connection](https://support.mozilla.org/kb/connection-untrusted-error-message), you can also choose to send Mozilla the associated certificates.

	Firefox Forgery and Attack Protection: About twice per hour, Firefox downloads Google's SafeBrowsing lists to help block access to sites and downloads that are malicious or forged (Google's privacy policy is at <https://www.google.com/policies/privacy/>). For downloaded executables that do not appear in these lists, Firefox may send metadata, including URLs associated with the downloaded file, to the SafeBrowsing service. Visit <https://support.mozilla.org/kb/how-does-phishing-and-malware-protection-work> to learn more about or disable Safe Browsing. If you disable these features, Firefox cannot warn you of potentially illegitimate or malicious websites or downloaded files.

* Statistici de utilizare (numite şi ca „Telemetrie” în versiunile care nu sunt finale)
  {: #telemetry .inproduct-link}

	Usage statistics or "Telemetry" is a feature in Firefox that sends Mozilla usage, performance, and responsiveness statistics about user interface features, memory and hardware configuration. Your IP address is also collected as a part of a standard web log. Usage statistics are transmitted using SSL and help us improve future versions of Firefox. Once sent to Mozilla, usage statistics are aggregated and made available to a broad range of developers, including both Mozilla employees and public contributors. When Telemetry is enabled, certain short-term experiments may collect information about visited sites.

	This feature is turned on by default in Nightly, Developer Edition, Aurora and Beta builds of Firefox to help those users provide feedback to Mozilla. In the general release version of Firefox, this feature is turned off by default.

	You can [learn more about Telemetry here](https://support.mozilla.org/kb/send-performance-data-improve-firefox) and how to enable or disable it. 

* Tiles 

	Tiles are a feature of Firefox displayed on new tab pages. In order to provide the tiles feature, Firefox sends to Mozilla data relating to the tiles such as number of clicks, impressions, your IP address, locale information and tile specific data (e.g., position and size of grid). In Firefox Beta, certain short-term Telemetry experiments (see above) for Tiles may collect information about commonly visited domains.
	
* Default Search
	To help choose the best default search engine for your location, Firefox sends Mozilla a request once to look up your location at a country level using your IP address. We then send that country level information back to Firefox, where it's stored locally. Firefox will then choose which search engine to use as its default based on the locally stored country information.

* For Firefox for Android only:
In order to understand the performance of certain Mozilla marketing campaigns, Firefox sends data, including a Google advertising ID, IP address, timestamp, country, language/locale, operating system, app version, to our third party vendor. This data allows us to attribute an install to a specific advertising channel and optimize marketing campaign strategies.

---------------------------------------

When you ask it to, Firefox also connects to Mozilla to provide you with features such as Sync, location services, crash reporting, and add-ons.
{: #optional-features }

* **Sincronizare**: [Firefox Sync](https://www.mozilla.org/firefox/sync/) is a service that allows you to sync your Firefox bookmarks, browsing history, passwords, and settings across all of your devices. If you use the Sync service, you can read the [Firefox Sync privacy notice](https://services.mozilla.com/privacy-policy/).
{: #sync }

* **Location services**: Firefox has a feature that allows sites to request your location (e.g., to allow those sites to show your location on a map). If a site requests your location, Firefox seeks your permission before determining and sharing your location. In order to determine your location, Firefox may use several pieces of data to determine your location, including your operating systems geolocation features, WiFi networks, cell phone towers or IP address. Estimating your location involves sending some of this information to Google's geolocation service, which has its own [privacy policy](https://www.google.com/privacy/lsf.html).
{: #location-services }

* **Raportarea de defecţiuni**: You have the option to send Mozilla a crash report after Firefox crashes. This report contains technical information for us to improve Firefox including why Firefox crashed, the active URL at time of crash, and the state of computer memory during the crash. The crash report we receive may include personal information. We make portions of crash reports available publicly at <https://crash-stats.mozilla.com/>). Before publicly posting crash reports, we take steps to automatically redact personal information. We do not redact anything you may write in the comments box.
{: #crash-reporter .inproduct-link }

* **Erori SSL**: You have the option to send Mozilla an error report when a secure website connection is broken. This report records the website certificate as well as diagnostic error codes. This information helps Mozilla monitor the effectiveness of "pinned" website certificates and detect potential phishing attacks against our users.

* **Suplimente**: Firefox offers a Get Add-ons page of the Add-ons Manager that features popular add-ons and displays personalized recommendations based on the add-ons you already have installed. To display the personalized recommendations, Firefox sends information to Mozilla, including the list of add-ons you have installed, Firefox version information, and your IP address. This communication only happens when the Get Add-ons area is open and can be turned off by following [these instructions](https://blog.mozilla.org/addons/how-to-opt-out-of-add-on-metadata-updates/).The add-ons manager in Firefox has a search field where you can enter key words to perform searches and Mozilla collects these key word searches, as well as your Firefox version information, locale, and OS to show you recommendations.
{: #addons }
