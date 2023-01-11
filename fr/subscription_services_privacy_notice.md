# Services d’abonnement Mozilla | Politique de confidentialité

Version 1.0 - Date d’effet : mardi 11 octobre 2022
{: datetime="2022-10-11" }

## Chez Mozilla, nous concevons des produits respectant votre confidentialité.

__Mozilla VPN__ protège les connexions Internet de votre appareil. Mozilla s’est associé à la société Mullvad pour le chiffrement privé et sécurisé de votre trafic Internet.

__Firefox Relay__ vous permet de protéger votre adresse e-mail principale et vos numéros de téléphone sur les services en ligne en les rendant uniques et aléatoires (par le biais d’alias).

Cette politique de confidentialité explique quelles données Mozilla VPN collecte et partage, et dans quels buts. Nous adhérons en outre à la [Politique de confidentialité de Mozilla](https://www.mozilla.org/privacy/), qui explique comment nous recevons, traitons et partageons les informations.

## Ce que vous devez savoir

__Informations de compte Firefox.__ Ces services nécessitent un compte Firefox, qui envoie à Mozilla VPN votre adresse e-mail, vos paramètres régionaux (langue, etc.) et votre adresse IP. En savoir plus sur les [pratiques en matière de données de compte Firefox](https://www.mozilla.org/privacy/firefox/#firefox-accounts-join-firefox).

__Informations de paiement.__ Lorsque vous vous abonnerez aux Services, vous enverrez un paiement par le biais de l’un de nos fournisseurs de paiement tiers : Stripe, Apple, PayPal ou Google Pay. Mozilla reçoit un enregistrement de votre compte (comprenant votre adresse de facturation et les quatre derniers chiffres de votre mode de paiement) et le statut de l’abonnement de votre compte. Mozilla ne stocke pas tous les détails de vos paiements.

__Données d’interaction.__ Mozilla reçoit des données relatives à vos interactions avec les Services. Par exemple, quand vous vous connectez et déconnectez, les préférences que vous paramétrez. En savoir plus sur les [données d’interaction VPN](https://github.com/mozilla-mobile/mozilla-vpn-client/blob/main/glean/metrics.yaml) et les [données d’interaction Relay](https://github.com/mozilla/fx-private-relay/blob/main/METRICS.md).

__Données techniques.__ Mozilla reçoit des informations de base concernant la version installée de votre extension VPN ou Relay, l’appareil sur lequel elle est installée, y compris le système d’exploitation et la configuration matérielle. Votre adresse IP est temporairement collectée dans le cadre de notre journalisation des serveurs, pendant 90 jours. Ni Mozilla, ni notre partenaire Mullvad ne conserve les journaux de serveurs enregistrant votre activité réseau lorsque vous utilisez le service Mozilla VPN.
Nous utilisons les données pour améliorer les performances et la stabilité pour nos utilisateurs, et mesurer les performances des Services.

### Mozilla VPN {: #vpn }

__Données de localisation.__ Mozilla VPN reçoit votre adresse IP lorsque vous vous inscrivez au service et l’utilisez. Nous utilisons l’adresse IP pour vous localiser approximativement afin de déterminer le serveur VPN auquel vous vous connectez et parce que la disponibilité, les tarifs et les offres de Mozilla VPN varient selon les pays.

__Données de campagne et données de renvoi.__ Ces données aident Mozilla VPN à évaluer l’efficacité de nos campagnes marketing. Lors de l’installation de l’application, Mozilla peut recevoir votre adresse IP en plus des données de campagne et de renvoi, par exemple les campagnes publicitaires avec lesquelles vous avez interagi et votre système d’exploitation, type d’appareil, identificateurs d’appareil et version du système d’exploitation. Mozilla partage ces informations avec Adjust, mais nous ne partageons ni ne stockons votre adresse IP. Voir la [documentation Adjust](https://github.com/mozilla-mobile/mozilla-vpn-client/blob/main/src/apps/vpn/adjust/adjust.md).

__Données réseau.__ Mullvad reçoit votre trafic Internet pour fournir le service. Une fois Mozilla VPN activé, celui-ci chiffre votre trafic Internet et l’envoie à Mullvad. Mullvad s’est engagé à ne pas consigner les données qu’elle reçoit. En savoir plus : [Politique de confidentialité de Mullvad](https://mullvad.net/help/no-logging-data-policy/).

### Firefox Relay {: #relay }

__Messages e-mail.__ Pour envoyer et transférer vos messages e-mail depuis votre ou vos adresses e-mail masquées par des alias vers votre adresse e-mail principale, Firefox Relay doit traiter vos messages e-mail. Nous ne lisons ni ne stockons le contenu de vos messages. Si un e-mail ne peut pas vous être acheminé, nous le conservons sur nos serveurs et le supprimons après avoir été acheminé (dans tous les cas, nous ne le conservons pas plus de trois jours). Si vous utilisez la fonction de blocage des e-mails promotionnels, le Service vérifiera les en-têtes des e-mails pour déterminer si ces derniers doivent être bloqués.

__Alias, et où les utiliser.__ Mozilla conserve une copie des informations de votre compte pour fournir le service, en particulier pour associer votre adresse e-mail principale à votre ou vos adresses masquées par des alias. Si vous créez un alias personnalisé, Mozilla le stockera pour pouvoir y transférer des e-mails. Mozilla stocke le site qui vous a servi à créer le alias, les sites où vous avez ensuite utilisé le alias et toutes les étiquettes associées au alias afin que celui-ci soit facile à retrouver quand vous en avez besoin. En savoir plus sur [l’activation et la désactivation de cette fonctionnalité](https://relay.firefox.com/faq).

__Appels téléphoniques et SMS.__ Pour envoyer et transférer vos appels téléphoniques et SMS, Firefox Relay traite votre numéro de téléphone et SMS. Nous créons des journaux avec les numéros de téléphone que vous avez contactés via Relay afin de consigner vos appels et SMS, envoyer des réponses par SMS et bloquer des numéros de téléphone. Nous ne surveillons pas ni ne stockons le contenu des appels téléphoniques que vous passez via Firefox Relay.

Lisez la documentation relative à la télémétrie pour [Firefox Relay](https://github.com/mozilla/fx-private-relay/blob/main/METRICS.md). Vous pouvez annuler la collecte de données de télémétrie en activant l’option [Ne pas me pister](https://support.mozilla.org/kb/how-do-i-turn-do-not-track-feature) dans votre navigateur.

__Informations que nous partageons.__ Firefox Relay partage des informations avec certaines sociétés tierces afin de vous fournir le service. Mozilla a conclu des accords avec cette société, obligeant cette dernière à protéger vos informations. Voici la liste de nos partenaires qui contribuent au bon fonctionnement de Firefox Relay :

* __[Amazon Web Services.](https://aws.amazon.com/privacy/)__ Amazon Web Services (AWS) est une plateforme informatique basée sur le cloud. Firefox Relay se sert d’AWS pour recevoir les e-mails envoyés à votre ou vos adresses e-mail masquées par des alias et les transférer à l’adresse e-mail principale associée à votre compte Firefox. Seul Mozilla connaît l’association entre votre adresse e-mail principale et votre ou vos adresses e-mail masquées par des alias.

* __[Twilio.](https://www.twilio.com)__ Twilio reçoit votre numéro de téléphone, votre alias de téléphone et les numéros de téléphone qui vous servent à échanger des appels téléphoniques et SMS. Twilio reçoit d’autre part le contenu des SMS que vous envoyez et recevez via Firefox Relay et Mozilla a configuré le service Twilio pour qu’il supprime les enregistrements des SMS que vous envoyez et recevez via Firefox Relay après 7 jours.

## Autres informations importantes

La plupart des informations que nous stockons sur nos utilisateurs de comptes Firefox sont facilement accessibles en se connectant à ces comptes. Découvrez [comment gérer vos données](https://support.mozilla.org/products/privacy-and-security/user-control). Pour toute demande, veuillez nous contacter via notre [Portail de demande d’accès aux données](https://privacyportal.onetrust.com/webform/1350748f-7139-405c-8188-22740b3b5587/4ba08202-2ede-4934-a89e-f0b0870f95f0).

Si vous avez d’autres questions concernant nos pratiques de confidentialité, veuillez nous contacter à l’adresse compliance@mozilla.com.

Nous répondons à toutes les demandes des personnes désireuses d’exercer leurs droits de protection des données, quelle que soit leur localisation (pays/région). Nous répondrons à votre demande, à moins qu’une disposition ou exclusion légale nous en empêche.

Visitez nos [forums](https://support.mozilla.org/) pour obtenir de l’assistance.
