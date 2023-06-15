# Mozilla Abonnementdienste | Datenschutzhinweis

Version 1.0, gültig ab Dienstag, 11. Oktober 2022
{: datetime="2022-10-11" }

## Wir bei Mozilla entwickeln Produkte, bei denen Ihre Privatsphäre an oberster Stelle steht.

__Mozilla VPN__ schützt die Internetverbindungen Ihres Geräts. Mozilla arbeitet mit Mullvad zusammen, um Ihren Internet-Traffic privat und sicher zu verschlüsseln.

__Firefox Relay__ ermöglicht Ihnen, Ihre primäre E-Mail-Adresse und Telefonnummer zu schützen und vor Online-Diensten geheimzuhalten, indem Sie eine spezielle, beliebige (Masken-) Telefonnummer und E-Mail-Adresse(n) erstellen.

In diesem Datenschutzhinweis wird erläutert, welche Daten Firefox Relay und Mozilla VPN erfassen, teilen und warum das so ist. Wir halten uns auch an die in der [Mozilla-Datenschutzerklärung](https://www.mozilla.org/privacy/) umrissenen Praktiken in Bezug auf den Empfang, den Umgang mit und das Teilen von Informationen.

## Sie sollten Folgendes wissen

__Firefox-Kontoinformationen.__ Für diese Dienste ist ein Firefox-Konto erforderlich, das Mozilla Ihre E-Mail-Adresse, Ihr Gebietsschema und Ihre IP-Adresse sendet. Weitere Informationen über [Firefox-Konto-Datenpraktiken](https://www.mozilla.org/privacy/firefox/#firefox-accounts-join-firefox).

__Informationen zur Zahlung.__ Wenn Sie die Dienste abonnieren, bezahlen Sie über einen der folgenden externen Zahlungsanbieter: Stripe, Apple, PayPal oder Google Pay. Mozilla erhält bestimmte Informationen zu Ihrem Konto, darunter die Rechnungsadresse und die letzten vier Ziffern der von Ihnen gewählten Zahlungsweise, und zum Status des Abonnements Ihres Kontos. Die vollständigen Zahlungsdaten werden von Mozilla nicht gespeichert.

__Interaktionsdaten.__ Mozilla erhält Daten über Ihre Interaktionen mit den Diensten, darunter wann Sie sich anmelden und welche Einstellungen Sie vorgenommen haben. Erfahren Sie mehr über [VPN-Interaktionsdaten](https://dictionary.telemetry.mozilla.org/apps/mozilla_vpn) und [Relay-Interaktionsdaten](https://github.com/mozilla/fx-private-relay/blob/main/METRICS.md).

__Technische Daten.__ Mozilla erhält grundlegende Informationen über die installierte Ihrer VPN- oder Relay Add-On-Software und Geräte, auf der diese installiert ist, einschließlich Betriebssystem und Hardwarekonfiguration. Ihre IP-Adresse wird als Teil unserer Server-Logs kurzzeitig für 90 Tage erfasst. Weder Mozilla noch unser Partner Mullvad führt Server-Logs Ihrer Netzwerkaktivität, wenn Sie den Mozilla VPN-Dienst verwenden.
Wir verwenden die Daten, um die Leistung und Stabilität für unsere Benutzer zu verbessern und die Leistung der Dienste zu messen.

### Mozilla VPN {: #vpn }

__Standortdaten.__ Mozilla VPN erhält Ihre IP-Adresse, wenn Sie sich für den Dienst registrieren und ihn nutzen. Wir verwenden die IP-Adresse, um Ihren Standort zu schätzen, um festzulegen, mit welchem VPN-Server Sie verbunden werden, und weil die Mozilla VPN-Verfügbarkeit, Preise und Angebote von Ihrem Land abhängen.

__Kampagnen- und Empfehlungsdaten__. Hiermit kann Mozilla VPN die Effektivität unserer Marketingkampagnen messen. Bei der Installation der App kann Mozilla Ihre IP-Adresse, Kampagnen- und Empfehlungsdaten (z. B. auf welche Werbekampagnen Sie reagiert haben), Ihr Betriebssystem, Ihren Gerätetyp, Geräteidentifikatoren und Ihre Betriebssystemversion erhalten. Mozilla teilt diese Angaben (mit Ausnahme Ihrer IP-Adresse; die von uns weder geteilt noch gespeichert wird) mit Adjust. Lesen Sie die [Adjust-Dokumentation](https://github.com/mozilla-mobile/mozilla-vpn-client/blob/main/src/apps/vpn/adjust/adjust.md).

__Netzwerkdaten.__ Mullvad empfängt Ihren Internet-Traffic, um den Dienst bereitzustellen. Wenn Sie Mozilla VPN aktivieren, wird Ihr Internet-Traffic verschlüsselt und an Mullvad gesendet. Mullvad hat sich dazu verpflichtet, keine der erhaltenen Daten zu protokollieren oder aufzuzeichnen. Weitere Informationen finden Sie in der [Datenschutzerklärung von Mullvad](https://mullvad.net/help/no-logging-data-policy/).

### Firefox Relay {: #relay }

__E-Mail-Nachrichten.__ Zum Senden und Weiterleiten Ihrer E-Mail-Nachrichten über Ihre maskierte(n) E-Mail-Adresse(n) an Ihre Haupt-E-Mail-Adresse verarbeitet Firefox Relay Ihre E-Mail-Nachrichten. Wir lesen und speichern den Inhalt Ihrer Nachrichten nicht. Sollte eine E-Mail nicht zugestellt werden können, bewahren wir sie auf unseren Servern auf und löschen sie nach der Zustellung. (Keinesfalls jedoch wird eine E-Mail länger als drei Tage von uns aufbewahrt.) Wenn Sie die Funktion zum Blockieren von Werbemails nutzen, überprüft der Dienst den Header der E-Mails, um festzustellen, ob eine E-Mail blockiert werden muss.

__Masken und wo sie von Ihnen verwendet werden.__ Mozilla führt eine Kopie Ihrer Kontoinformationen, um Ihnen den Dienst bereitzustellen, insbesondere, um Ihre primäre E-Mail-Adresse Ihrer/Ihren maskierten E-Mail-Adresse(n) zuzuordnen. Wenn Sie eine spezifische Maske erstellen, speichert Mozilla diese, um E-Mails dorthin weiterleiten zu können. Mozilla speichert die Orte, an denen Sie die Maske erstellt haben, Orte, an denen Sie die Maske danach verwendet haben und alle mit der Maske verbundenen Kennzeichnungen, um sicherzustellen, dass Ihre Masken leicht auffindbar sind, wenn Sie bereit sind, sie zu nutzen. Erfahren Sie, wie Sie [diese Funktionen aktivieren oder deaktivieren](https://relay.firefox.com/faq).

__Telefongespräche und SMS-Nachrichten.__ Um Ihre Telefongespräche und SMS-Nachrichten zu senden und weiterzuleiten, verarbeitet Firefox Relay Ihre Telefonnummer und SMS-Nachrichten. Wir speichern ein Log der Telefonnummern, die Sie über Relay kontaktiert haben, um Ihre Anruf- und SMS-Logs anzuzeigen, SMS-Antworten zu senden und Telefonnummern zu sperren. Wir überwachen und speichern den Inhalt von über Firefox Relay getätigten Telefongesprächen nicht.

Lesen Sie die Telemetrie-Dokumentation für [Firefox Relay](https://github.com/mozilla/fx-private-relay/blob/main/METRICS.md). Sie können die Telemetrie-Erfassung per Opt-out abstellen, indem Sie die Funktion [Do Not Track (DNT)](https://support.mozilla.org/kb/how-do-i-turn-do-not-track-feature) in Ihrem Browser aktivieren.

__Von uns geteilte Informationen.__ Firefox Relay teilt Daten mit bestimmten Dritten, um Ihnen den Dienst bereitzustellen. Mozilla hat mit diesem Unternehmen Vereinbarungen getroffen, durch die dieses vertraglich zum Schutz Ihrer Daten verpflichtet ist. Wir arbeiten mit folgenden Anbietern zusammen, um Firefox Relay zu unterstützen:

* __[Amazon Web Services.](https://aws.amazon.com/privacy/)__ Amazon Web Services (AWS) ist eine Cloud-Computing-Plattform. Firefox Relay nutzt AWS, um an Ihre maskierte(n) E-Mail-Adresse(n) gesendete E-Mail-Nachrichten zu empfangen und an Ihre primäre E-Mail-Adresse weiterzuleiten, die Ihrem Firefox-Konto zugeordnet ist. Nur Mozilla kennt die Zuordnung zwischen Ihrer primären E-Mail-Adresse und Ihrer/Ihren maskierten E-Mail-Adresse(n).

* __[Twilio.](https://www.twilio.com)__ Twilio erhält Ihre Telefonnummer, Ihre Telefonnummer-Maske sowie die Telefonnummern, mit denen Sie Telefongespräche und SMS-Nachrichten austauschen. Twilio erhält auch den Inhalt von SMS-Nachrichten, die Sie über Firefox Relay senden und empfangen, und Mozilla hat den Twilio Dienst so eingerichtet, dass die von Ihnen über Firefox Relay gesendeten und empfangenen SMS-Nachrichten nach 7 Tagen gelöscht werden.

## Weitere Informationen, mit denen Sie vertraut sein sollten

Viele der Informationen, die wir über unsere Benutzer von Firefox-Konten speichern, sind durch Anmeldung bei Ihrem Konto leicht zugänglich. Hier finden Sie [weitere Informationen zur Verwaltung Ihrer Daten](https://support.mozilla.org/products/privacy-and-security/user-control). Für Anfragen kontaktieren Sie uns bitte über unser [Portal für Zugangsanfragen von betroffenen Personen](https://privacyportal.onetrust.com/webform/1350748f-7139-405c-8188-22740b3b5587/4ba08202-2ede-4934-a89e-f0b0870f95f0).

Bei anderen Fragen zu unseren Datenschutzpraktiken können Sie sich jederzeit unter compliance@mozilla.com an uns wenden.

Wir beantworten alle Anfragen, die wir von Einzelpersonen erhalten, die ihre Datenschutzrechte ausüben möchten, ungeachtet des Wohnorts der Person. Wir werden Ihrer Anfrage nachkommen, es sei denn, eine gesetzliche Vorschrift hindert uns daran oder es gilt eine gesetzliche Ausnahme.

In unseren [Foren](https://support.mozilla.org/) finden Sie allgemeine Support- und Hilfeinformationen.
