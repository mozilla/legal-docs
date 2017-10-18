## <span class="privacy-header-firefox">Firefox</span> <span class="privacy-header-policy">— Politique de confidentialité</span>

*Date d’effet : 28 septembre 2017*
{: datetime="2017-09-28" }

## Chez Mozilla, nous considérons que la confidentialité est essentielle pour l’intégrité d’Internet.

C’est pourquoi nous développons Firefox et tous nos autres produits avec le souci de vous donner le contrôle sur les informations que vous partagez en ligne et celles que vous partagez avec nous. Nous veillons à ne recueillir que les informations dont nous avons besoin pour améliorer Firefox pour tous.

Dans cette Politique de confidentialité, nous expliquons quelles données Firefox partage et vous expliquons comment partager encore moins de données. Nous adhérons en outre aux pratiques décrites dans la [Politique de confidentialité](https://www.mozilla.org/privacy/) de Mozilla sur la réception, le traitement et le partage des informations que nous recueillons à partir de Firefox.

## Par défaut, Firefox partage les données aux fins suivantes :

### Améliorer les performances et la stabilité pour les utilisateurs, où qu’ils se trouvent {: #health-report }

* __Données d’interaction__ : Firefox nous envoie des données relatives à vos interactions avec Firefox (comme le nombre d’onglets et fenêtres ouverts, le nombre de pages web visitées, le nombre et type de modules complémentaires Firefox installés et la durée des sessions) et les fonctionnalités proposées par Mozilla ou nos partenaires (comme l’interaction avec les fonctionnalités de recherche Firefox et les recommandations des partenaires de recherche).

* __Données techniques__ : Firefox nous envoie des données à propos de la version et de la langue de votre Firefox, du système d’exploitation de votre appareil et sa configuration matérielle, de la mémoire, des informations de base sur les plantages et les erreurs, le résultat de processus automatiques comme les mises à jour, le blocage de sites malveillants et l’activation. Lorsque Firefox nous envoie des données, votre adresse IP est temporairement collectée dans les fichiers journaux de nos serveurs.

Lisez la documentation de télémétrie pour [ordinateur](https://firefox-source-docs.mozilla.org/toolkit/components/telemetry/telemetry/index.html), [Android](https://firefox-source-docs.mozilla.org/mobile/android/fennec/index.html) ou [iOS](https://github.com/mozilla-mobile/firefox-ios/wiki/Telemetry) ou apprenez à [vous retirer](https://support.mozilla.org/kb/send-performance-data-improve-firefox) de cette collecte de données.
{: #telemetry }

### Définir un prestataire de recherche par défaut {: #defaultsearch }

* __Données de géolocalisation__ : lors de votre première utilisation de Firefox, celui-ci se base sur votre adresse IP pour définir votre moteur de recherche par défaut en fonction de votre pays. [En savoir plus](https://support.mozilla.org/kb/change-your-default-search-settings-firefox).

### Suggérer du contenu pertinent

Firefox affiche du contenu, tels les « snippets » (messages de Mozilla) et les Sites les plus visités (sites suggérés par Mozilla pour les nouveaux utilisateurs de Firefox).

* __Données de géolocalisation__ : Firefox se sert de votre adresse IP pour vous suggérer du contenu pertinent en fonction de votre pays.

* __Données techniques et d’interaction__ : Firefox nous envoie des données telles la position, la taille et l’emplacement de contenus que nous suggérons, ainsi que des données de base à propos de vos interactions avec le contenu suggéré par Firefox. Cela comprend le nombre de fois où le contenu suggéré est affiché ou le nombre de fois où vous avez cliqué dessus.

* __Données de pages web pour les snippets__ : lorsque vous décidez de cliquer sur un lien de snippet, nous pouvons recevoir des données sur le lien que vous avez suivi. Ces données ne sont aucunement associées à des informations vous concernant personnellement. [En savoir plus](https://abouthome-snippets-service.readthedocs.io/en/latest/data_collection.html).
{: #snippets }

### Améliorer la sécurité des utilisateurs où qu’ils se trouvent {: #security }

* __Données techniques des mises à jour__ : les versions de Firefox sur ordinateurs de bureau vérifient régulièrement la disponibilité de mises à jour en se connectant aux serveurs de Mozilla. Votre version de Firefox, langue et système d’exploitation sont utilisés pour trouver les mises à jour appropriées. Les versions mobiles de Firefox peuvent se connecter à un autre service si vous en avez utilisé un pour télécharger et installer Firefox. [En savoir plus](https://support.mozilla.org/kb/how-stop-firefox-automatically-making-connections#w_auto-update-checking).
{: #auto-updates }

* __Données techniques pour la liste de blocage des modules complémentaires__ : Firefox pour les ordinateurs de bureau et appareils Android se connecte régulièrement à Mozilla pour protéger les utilisateurs contre les modules complémentaires dangereux. Votre version de Firefox, langue, système d’exploitation et liste des modules complémentaires installés sont nécessaires pour appliquer et mettre à jour la liste de blocage des modules complémentaires. [En savoir plus](https://support.mozilla.org/kb/how-stop-firefox-making-automatic-connections).

* __Données techniques et de pages web envoyées au service Safe Browsing de Google__ : pour vous aider à vous protéger contre les téléchargements dangereux, Firefox envoie des informations de base concernant les téléchargements non reconnus au service Safe Browsing de Google, notamment le nom du fichier et l’URL à partir de laquelle il a été téléchargé.

    [En savoir plus](https://support.mozilla.org/kb/how-does-phishing-and-malware-protection-work) (ou lisez les [Règles de confidentialité de Google](https://www.google.com/policies/privacy/)). Si vous renoncez à ce service, Firefox ne pourra pas vous signaler les sites web et les téléchargements dangereux.

* __Données techniques et de pages web envoyées aux organismes de certificats__ : lorsque vous visitez un site sécurisé (en général identifié par « HTTPS », Firefox valide le [certificat](https://support.mozilla.org/kb/secure-website-certificate) du site web. Cela peut impliquer de la part de Firefox l’envoi de certaines informations concernant le site web à l’organisme de certificats identifié par ce site web.

    Si vous renoncez à ce service, vous augmentez le risque d’interception de vos informations personnelles. [En savoir plus](https://support.mozilla.org/kb/advanced-settings-browsing-network-updates-encryption#w_certificates-tab).

### Rapports de plantage {: #crash-reporter }
Par défaut, avec les versions pour ordinateurs de bureau de Firefox, nous vous demanderons de partager un rapport contenant plus d’informations détaillées sur les plantages de Mozilla, mais vous pouvez refuser de le faire à tout moment.

* __Données sensibles__ : les rapports de plantage comprennent un fichier de « vidage » du contenu de la mémoire de Firefox au moment du plantage, pouvant contenir des données qui vous identifient ou que vous pouvez considérer comme sensibles.

* __Données de pages web__ : les rapports de plantage incluent l’URL active au moment du plantage.

* __Données techniques__ : un rapport de plantage comprend des données sur les raisons du plantage de Firefox et l’état de la mémoire de l’appareil et de son exécution au moment du plantage.

Vous pouvez [lire la documentation complète](https://firefox-source-docs.mozilla.org/toolkit/crashreporter/crashreporter/index.html).

### Mesurer et soutenir notre

* __campagne marketing et nos données de référence__ : cela aide Mozilla à comprendre l’efficacité de nos campagnes marketing.
{: #referraltracking }

    _Sur ordinateur_ : par défaut, Firefox envoie des données HTTP à Mozilla, qui peuvent être incluses dans le programme d’installation de Firefox. Cela nous permet de déterminer le domaine du site web ou la campagne publicitaire (le cas échéant) qui vous a dirigé vers notre page de téléchargement. Lisez la [documentation](https://firefox-source-docs.mozilla.org/toolkit/components/telemetry/telemetry/data/environment.html#attribution) ou [retirez-vous](https://support.mozilla.org/kb/desktop-privacy) avant l’installation.

    _Sur iOS et Android_ : par défaut, Firefox envoie des données de campagnes mobiles à Adjust, notre prestataire d’analyses, qui dispose de sa propre [politique de confidentialité](https://www.adjust.com/privacy_policy/). Les données de campagnes mobiles incluent ce qui suit : ID de publicité Google, adresse IP, horodatage, pays/langue, système d’exploitation et version de l’application. Vous pouvez consulter la [documentation](https://firefox-source-docs.mozilla.org/mobile/android/fennec/adjust.html).
{: #thirdparty }

* __Données techniques et d’interaction__ :

    _Sur iOS et Android_ : par défaut, Firefox envoie des données relatives aux fonctionnalités que vous utilisez dans Firefox à Leanplum, notre prestataire de marketing mobile, qui dispose de sa propre [politique de confidentialité](https://www.leanplum.com/privacy/).  Ces données nous permettent de tester différentes fonctionnalités et expériences, et de proposer des messages et des recommandations personnalisés pour améliorer la façon dont vous utilisez Firefox.

    Lisez la documentation sur [iOS](https://github.com/mozilla-mobile/firefox-ios/blob/master/MMA.md) ou [Android](https://firefox-source-docs.mozilla.org/mobile/android/fennec/mma.html), ou apprenez à [désactiver cette fonctionnalité](https://support.mozilla.org/kb/send-anonymous-usage-data-firefox-mobile-devices).

---

## Si vous utilisez ces fonctionnalités, Firefox partagera des données pour les fonctions suivantes : {: #optional-features }

### Recherche

Vous pouvez effectuer des recherches directement de plusieurs endroits dans Firefox, notamment depuis la barre d’adresse intelligente, la barre de recherche ou un nouvel onglet. _Mozilla ne reçoit pas vos requêtes de recherche._ Les données de requête sont envoyées à votre moteur de recherche, qui dispose de sa propre politique de confidentialité.

* __Suggestions de recherche__ : par défaut, Firefox envoie les requêtes de recherche à votre moteur de recherche pour les comparer aux expressions courantes recherchées par d’autres utilisateurs afin d’améliorer votre expérience de recherche. Ces données ne seront pas envoyées si votre moteur de recherche ne prend pas en charge les suggestions.
{: #searchsuggestions }

    [En savoir plus](https://support.mozilla.org/kb/use-popular-search-suggestions-firefox-search-bar), notamment sur la désactivation de cette fonctionnalité.

### Comptes Firefox

* __Données des comptes Firefox__ : Mozilla reçoit votre adresse de courriel et votre mot de passe chiffré lorsque vous créez un compte Firefox. Vous pouvez décider d’inclure un nom d’affichage ou une image de profil. Votre adresse de courriel est envoyée à notre prestataire de messagerie, SalesForce Marketing Cloud, qui dispose de sa propre [politique de confidentialité](https://www.marketingcloud.com/privacy-policy/website-privacy-statement/). Si vous utilisez votre compte Firefox pour vous connecter à d’autres services ou sites web (comme AMO ou Pocket), ces services nous envoient l’horodatage de votre connexion.

* __Données de géolocalisation__ : pour des raisons de sécurité, nous stockons les adresses IP que vous utilisez pour accéder à votre compte Firefox, afin de vous localiser au plus près (ville et pays). Nous utilisons ces données pour vous envoyer des courriels d’alerte si nous détectons des activités suspectes, comme des connexions à votre compte depuis d’autres lieux.

* __Données d’interaction__ : nous recevons des données telles que les visites et les interactions avec le site web des comptes Firefox et les préférences des menus, ainsi que les interactions d’accueil, de messagerie et de SMS. [En savoir plus](https://www.mozilla.org/privacy/websites/) sur les pratiques de données de Mozilla concernant les sites web et la messagerie.

* __Données techniques__ : pour afficher les services qui sont synchronisés avec votre compte Firefox et pour des raisons fonctionnelles, nous stockons votre système d’exploitation, navigateur et version, horodatage, langue (ainsi que les mêmes informations pour les appareils connectés à votre compte).

Lisez [la documentation complète](https://github.com/mozilla/fxa-auth-server/blob/master/docs/metrics-events.md) ou [apprenez-en plus](https://support.mozilla.org/kb/access-mozilla-services-firefox-accounts), notamment comment [supprimer votre compte](https://support.mozilla.org/kb/how-do-i-delete-my-firefox-account).

### Sync {: #sync }

* __Données synchronisées__ : si vous activez Sync, Mozilla reçoit les informations que vous synchronisez sur vos appareils sous forme chiffrée. Cela peut inclure : onglets, modules complémentaires, mots de passe, données préremplies de paiement, marque-pages, historique et préférences. Le fait de supprimer votre compte Firefox supprimera le contenu de Firefox Sync associé. Vous pouvez également lire la [documentation](https://moz-services-docs.readthedocs.io/en/latest/sync/).

* __Données techniques et d’interaction__ : si vous activez Sync, Firefox enverra régulièrement des données de base à l’aide de la télémétrie, concernant la tentative la plus récente de synchroniser vos données, par exemple le moment où cela s’est produit, si la tentative a échoué ou réussi et le type d’appareil qui tente la synchronisation. Vous pouvez également lire la [documentation](https://firefox-source-docs.mozilla.org/toolkit/components/telemetry/telemetry/data/sync-ping.html).

[En savoir plus](https://support.mozilla.org/kb/how-do-i-set-sync-my-computer), notamment comment activer et désactiver la synchronisation.

### Géolocalisation {: #location-services }

* __Données de localisation pour le service de géolocalisation de Google__ : Firefox vous demandera toujours la permission avant de déterminer et partager votre localisation avec un site web qui la demande (par exemple, si un site de cartes routières a besoin de votre localisation pour vous proposer un itinéraire). Pour déterminer votre localisation, Firefox peut utiliser les fonctionnalités de géolocalisation de votre système d’exploitation, les réseaux Wi-Fi, les relais de réseaux mobiles ou les adresses IP, puis envoyer ces données au service de géolocalisation Google, qui dispose de sa propre [politique de confidentialité](https://www.google.com/privacy/lsf.html).

[En savoir plus](https://www.mozilla.org/firefox/geolocation/).

### Firefox Screenshots {: #screenshots }

* __Envoi de captures d’écran__ : les captures d’écran que vous décidez d’envoyer sont envoyées à Mozilla et stockées pendant la période indiquée, que vous pouvez modifier. Nous nous réservons le droit d’accéder à vos captures d’écran lorsque cela est raisonnablement nécessaire pour le bon fonctionnement du service. Vous pouvez supprimer vos captures d’écran envoyées à tout moment.

* __Données d’interaction__ : nous recevons des données telles les visites au site web Firefox Screenshots, le nombre de fois où les captures d’écran envoyées ont été consultées et partagées par vous ou d’autres utilisateurs, ainsi que vos interactions avec les boutons, vignettes et déplacements de souris relatifs à la capture des écrans.

    Pour les visites au site web Firefox Screenshots, consultez notre [Avis de confidentialité relatif aux sites web](https://www.mozilla.org/privacy/websites/), qui décrit les types de données que nous collectons.

* __Données techniques__ : nous recevons des données, comme la taille moyenne et le nombre de vos captures d’écran envoyées, la version de votre navigateur Firefox, le système d’exploitation de votre appareil et des erreurs. L’adresse IP servant à accéder au site web Firefox Screenshots est momentanément collectée par le fichier journal de serveur standard.

Lisez la [documentation complète](https://github.com/mozilla-services/screenshots/blob/master/docs/METRICS.md) ou [apprenez-en plus](https://wiki.mozilla.org/Firefox/Screenshots/FAQs).

### Notifications des sites web {: #push-notifications }

* __Données de connexion__ : si vous autorisez un site web à vous envoyer des notifications, Firefox se connecte à Mozilla et utilise votre adresse IP pour relayer le message. Mozilla ne peut pas accéder au contenu des messages.

* __Données d’interaction__ : nous recevons des données agrégées tels que le nombre d’abonnements et de désabonnements Firefox aux notifications des sites web, le nombre de messages envoyés, les horodatages et les envoyeurs (qui peuvent inclure des prestataires de sites web spécifiques).

Lisez la [documentation complète](https://mozilla-push-service.readthedocs.io/en/latest/) ou [apprenez-en plus](https://support.mozilla.org/kb/push-notifications-firefox), notamment comment désactiver les notifications des sites web.

### Modules complémentaires {: #addons }

Vous pouvez installer des modules complémentaires à partir du site addons.mozilla.org (« AMO ») ou du Gestionnaire de modules complémentaires, accessible en cliquant sur le bouton Modules dans le menu Firefox (trois barres superposées) de la barre d’outils.

* __Requêtes de recherche__ : les requêtes de recherche du Gestionnaire de modules complémentaires sont envoyées à Mozilla pour nous permettre de vous suggérer des modules complémentaires.

* __Données d’interaction__ : nous recevons des données agrégées sur vos visites au site AMO et l’utilisation du Gestionnaire de modules complémentaires dans Firefox, ainsi que sur les interactions avec le contenu sur ces pages. En savoir plus sur les pratiques de données sur les [sites web Mozilla](https://www.mozilla.org/privacy/websites/).

* __Données techniques des mises à jour__ : Firefox se connecte régulièrement à Mozilla pour installer les mises à jour des modules complémentaires. Vos modules complémentaires installés, votre version de Firefox, votre langue et votre système d’exploitation sont utilisés pour trouver les mises à jour appropriées.

---

### Note

Cette politique de confidentialité concerne la version générale la plus récente de Firefox distribuée par Mozilla. Si vous installez Firefox autrement que par le biais de Mozilla ou que vous utilisez une version plus ancienne, certaines caractéristiques de confidentialité peuvent être différentes.
{: #pre-release }

Les versions de développement de Firefox (distribuées via des canaux comme Nightly, Beta, TestFlight et BuddyBuild) sont en cours de développement actif et peuvent inclure des caractéristiques de confidentialité différentes.
