# Firefox-Browser – Datenschutz-Hinweis

15.04.14
{: datetime="2014-04-15" }

Den Schutz Ihrer Daten nehmen wir sehr ernst. Wenn Firefox Daten an Mozilla (an uns) sendet, verarbeiten wir diese Daten wie in der [Datenschutzerklärung](https://www.mozilla.org/privacy/) beschrieben.

## Folgendes sollten Sie wissen

Firefox stellt automatisch eine Verbindung mit uns und unseren Dienstanbietern her, um Updates, Sicherheit, Snippets, den Firefox-Statusbericht und andere Features bereitzustellen. 
{: #essential-features }

* Browser- und Add-on-Updates
  {: #auto-updates }

	Browser-Updates: Einmal am Tag sendet Firefox folgende Informationen an Mozilla, wenn auf Browser-Updates geprüft wird: Ihre Firefox-Versionsinformationen, Spracheinstellung, Ihr Betriebssystem und dessen Version. Sie können [Updates mithilfe dieser Anweisungen abstellen](https://support.mozilla.org/de/kb/Firefox-baut-unaufgeforderte-Verbindungen-auf#w_automatische-updateprakfung), allerdings werden Sie dadurch eventuell Sicherheitslücken gegenüber anfällig.

	Add-on-Blockierliste: Firefox kontaktiert Mozilla einmal am Tag, um nach Add-on-Informationen und schädlichen Add-ons zu suchen. Dies umfasst zum Beispiel: Browser-Version, Betriebssystem und Version, verwendete Sprache, Gesamtzahl der Anfragen, Zeit der letzten Anfrage, Tageszeit, IP-Adresse sowie die Liste der installierten Add-ons. Sie können jederzeit [Metadaten-Updates abstellen](https://blog.mozilla.org/addons/how-to-opt-out-of-add-on-metadata-updates/), allerdings werden Sie dadurch eventuell Sicherheitslücken gegenüber anfällig.

* Snippets
  {: #snippets }

	Die Standard-Homepage von Firefox (&lt;about:home&gt;) lädt direkt unterhalb der Suchleiste kleine Informationseinheiten, die unserer Meinung nach für Sie nützlich sein können. Diese nennen wir „Snippets“. Ungefähr einmal am Tag stellt Firefox eine Verbindung mit Mozilla her und liefert Ihnen ggf. neue Snippets (falls vorhanden). Mozilla erfasst, wie oft auf Snippets geklickt wird, den Snippet-Namen, die Sprache der Oberfläche und welche Version von Firefox Sie verwenden.

	Damit nur relevante Snippets angezeigt werden, sendet Firefox eine monatliche Anfrage an Mozilla, um Ihren Ort auf Landesebene mithilfe Ihrer IP-Adresse zu ermitteln. Dann senden wir die Information über Ihre Landesebene zurück an Firefox, wo sie lokal gespeichert wird. Firefox wählt dann anhand der lokal gespeicherten Landesinformation Snippets zur Anzeige aus.

* Firefox-Statusbericht
  {: #health-report .inproduct-link } 

	Der Firefox-Statusbericht hat den Zweck, Ihnen Einblicke in die Stabilität und Performanz Ihres Browsers zu gewähren und Ihnen Support-Tipps zu liefern, falls Probleme wie hohe Absturzraten oder langsame Starts auftreten. Mozilla erfasst Ihre Daten gemeinsam mit denen anderer Firefox-Benutzer, fasst diese zusammen und sendet sie zurück an Ihren Browser, damit Sie sehen können, wie sich Ihre Firefox-Performanz im Lauf der Zeit entwickelt. Diese Daten umfassen zum Beispiel: Gerätehardware, Betriebssystem, Firefox-Version, Add-ons (Anzahl und Typ), Verzögerung und Dauer von Browser-Ereignissen, Darstellung, Sitzungswiederherstellungen, Länge einer Sitzung, Alter eines Profils, Anzahl der Abstürze und Anzahl der Seiten. Der Statusbericht sendet Mozilla keine von Ihnen besuchten Internetadressen.

	Wir verwenden die über den Statusbericht gesendeten Daten dazu, Benutzern die mit dem Statusbericht verbundenen Funktionen bereitzustellen und Ihnen z. B. bei der Analyse und Behebung von Performanzproblemen mit Ihrem Browser zu helfen. Die Ergebnisse des Statusberichts benutzen wir in aggregierter Form auch zur Verbesserung von Firefox. Sie können die [Datenfreigabe deaktivieren](https://support.mozilla.org/de/kb/firefox-statusbericht-beurteilen-sie-effizienz#w_datenweitergabe-aktivieren-oder-deaktivieren).

* Sicherheit
  {: #security }

	Firefox prüft automatisch auf schädliche oder gefälschte Webseiten, defekte Add-ons und von Dritten ausgestellte SSL-Zertifikate.

	Website-Sicherheitszertifikate: Wenn Sie eine sichere Website (d. h. „https“) besuchen, überprüft Firefox das Zertifikat der Website. Dabei kann eine Kommunikation mit dem vom Zertifikat angegebenen Status-Drittanbieter erfolgen. Firefox sendet an diesen Dritten Informationen, die das [Zertifikat](https://support.mozilla.org/kb/secure-website-certificate) der Website identifizieren. Sie können [Ihre Einstellungen ändern](https://support.mozilla.org/de/kb/Einstellungen-Fenster--Erweitert-Abschnitt#w_zertifikate_2). Wenn Sie die Online-Prüffunktion deaktivieren, kann Firefox jedoch die Identität der von Ihnen besuchten Website nicht bestätigen. Wenn Sie diese Funktion deaktivieren, wird das Risiko erhöht, dass Ihre privaten Daten abgefangen werden können. Wenn Sie auf eine [nicht vertrauenswürdige Verbindung](https://support.mozilla.org/kb/connection-untrusted-error-message) stoßen, können Sie auch wählen, ob die zugeordneten Zertifikate an Mozilla geschickt werden sollen.

	Firefox-Betrugsversuchs- und Angriffsschutz: Ungefähr zweimal in der Stunde lädt Firefox die SafeBrowsing-Listen von Google herunter, um den Zugang zu Websites und Downloads zu blockieren, die schädlich oder gefälscht sind (die Datenschutzerklärung von Google finden Sie unter <https://www.google.com/policies/privacy/>). Wenn heruntergeladene ausführbare Dateien nicht auf diesen Listen erscheinen, kann Firefox Metadaten einschließlich der mit der heruntergeladenen Datei verbundenen Internetadressen an den SafeBrowsing-Dienst senden. Unter <https://support.mozilla.org/kb/how-does-phishing-and-malware-protection-work> finden Sie weitere Informationen über SafeBrowsing und das Deaktivieren dieses Dienstes. Wenn Sie diese Funktionen deaktivieren, kann Firefox Sie nicht vor potentiell illegitimen oder schädlichen Websites bzw. heruntergeladenen Dateien warnen.

* Nutzungsstatistiken (werden in Nicht-Release-Builds auch als „Telemetrie“ bezeichnet)
  {: #telemetry .inproduct-link}

	Nutzungsstatistiken oder „Telemetrie“ sind eine Funktion in Firefox, die Mozilla Nutzungs-, Performanz- und Reaktionsfähigkeits-Statistiken über Benutzeroberflächen-Funktionen sowie Speicher- und Hardwarekonfigurationen sendet. Ihre IP-Adresse wird als Teil eines Standard-Webprotokolls ebenfalls erfasst. Nutzungsstatistiken werden mithilfe von SSL übertragen und helfen uns, zukünftige Firefox-Versionen zu verbessern. Wenn sie an Mozilla gesendet werden, werden Nutzungsstatistiken aggregiert und verschiedenen Entwicklern zur Verfügung gestellt, darunter sowohl Mozilla-Mitarbeiter als auch externe Mitwirkende. Bei aktivierter Telemetrie können in bestimmten kurzfristigen Experimenten Informationen über besuchte Websites erfasst werden.

	Diese Funktion ist in den Nightly-, Aurora- und Beta-Builds von Firefox standardmäßig aktiviert, sodass diese Benutzer leichter Feedback an Mozilla weiterleiten. In der allgemeinen Release-Version von Firefox ist diese Funktion standardmäßig deaktiviert.

	Sie können [hier mehr über Telemetrie erfahren](https://support.mozilla.org/kb/send-performance-data-improve-firefox) und nachlesen, wie diese Funktion aktiviert bzw. deaktiviert wird. 

* Kacheln

	Kacheln sind eine Firefox-Funktion, das auf neuen Tab-Seiten angezeigt wird. Um die Kachelfunktion bereitzustellen, sendet Firefox Daten über die Kacheln an Mozilla, wie z. B. die Anzahl der Klicks, Anzeigehäufigkeit, Ihre IP-Adresse, Informationen zur Sprache der Benutzeroberfläche und kachelspezifische Daten (z. B. Position und Größe des Rasters). In Firefox Beta können bestimmte kurzzeitige Telemetrie-Versuche (siehe oben) für Kacheln Informationen zu häufig besuchten Domains erfassen.

---------------------------------------

Wenn Sie Firefox dazu auffordern, wird auch eine Verbindung mit Mozilla hergestellt, um Ihnen Funktionen wie Sync, Standortdienste, Absturzberichte und Add-ons bereitzustellen.
{: #optional-features }

* **Sync**: [Firefox Sync](https://www.mozilla.org/firefox/sync/) ist ein Dienst, mit dem Sie Ihre Firefox-Lesezeichen, Browserchronik, Passwörter und Einstellungen auf allen Ihren Geräten synchronisieren können. Wenn Sie den Sync-Dienst verwenden, lesen Sie bei Bedarf den [Firefox-Sync-Datenschutzhinweis](https://services.mozilla.com/privacy-policy/).
{: #sync }

* **Standortdienste**: Firefox weist eine Funktion auf, mit der Websites Ihren Standort anfordern können (z. B. damit diese Websites Ihren Standort auf einer Karte anzeigen können). Fordert eine Website Ihren Standort an, verlangt Firefox Ihre Genehmigung, bevor Ihr Standort bestimmt und weitergegeben wird. Um Ihren Standort zu bestimmen, kann Firefox mehrere Datenelemente nutzen, darunter die Standortortungsfunktionen Ihres Betriebssystems, WLAN-Netzwerke, Mobilfunktürme oder die IP-Adresse. Um Ihre Position zu schätzen, werden einige dieser Informationen an den Standortbestimmungsdienst von Google gesendet, für den eine eigene [Datenschutzerklärung](https://www.google.com/privacy/lsf.html) gilt.
{: #location-services }

* **Absturzberichte**: Sie haben die Option, Mozilla einen Absturzbericht zu senden, wenn Firefox abgestürzt ist. Dieser Bericht enthält technische Informationen, mit denen wir Firefox verbessern können, zum Beispiel den Grund für den Absturz, die zum Absturzzeitpunkt aktive Adresse (URL) und den Zustand des Computerspeichers während des Absturzes. Der Absturzbericht, den wir erhalten, kann persönliche Informationen enthalten. Wir stellen Teile der Absturzberichte unter <https://crash-stats.mozilla.com/> der Öffentlichkeit zur Verfügung. Bevor Absturzberichte veröffentlicht werden, unternehmen wir Schritte, um persönliche Informationen automatisch zu entfernen. Wir entfernen nichts, was Sie eventuell in das Kommentarfeld geschrieben haben.
{: #crash-reporter .inproduct-link }

* **Add-ons**: Firefox bietet im Add-ons-Manager die Seite „Add-ons suchen“. Hier können Sie beliebte Add-ons abrufen und es werden personalisierte Empfehlungen angezeigt, die auf den bereits von Ihnen installierten Add-ons basieren. Um die personalisierten Empfehlungen anzuzeigen, sendet Firefox Informationen an Mozilla, darunter die Liste der von Ihnen installierten Add-ons, Firefox-Versionsinformationen und Ihre IP-Adresse. Diese Kommunikation erfolgt nur, wenn der Bereich zum Abrufen von Add-ons geöffnet ist, und kann mithilfe [dieser Anweisungen](https://blog.mozilla.org/addons/how-to-opt-out-of-add-on-metadata-updates/) deaktiviert werden. Der Add-ons-Manager in Firefox weist ein Suchfeld auf, in das Sie Schlüsselbegriffe für die Suche eingeben können. Mozilla erfasst diese Schlüsselwortsuche sowie Ihre Firefox-Versionsinformationen, die Sprache Ihrer Oberfläche und Betriebssystem, um speziell auf Sie zugeschnittene Empfehlungen anzuzeigen.
{: #addons }
