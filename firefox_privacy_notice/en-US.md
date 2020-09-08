## <span class="privacy-header-firefox">Firefox</span> <span class="privacy-header-policy">Privacy Notice</span>

*Effective September 8, 2020*
{: datetime="2020-09-8" }

## At Mozilla, we believe that privacy is fundamental to a healthy internet.

That’s why we build Firefox, and all our products, to give you greater control over the information you share online and the information you share with us. We strive to collect only what we need to improve Firefox for everyone.

In this Privacy Notice, we explain what data Firefox shares and point you to settings to share even less. We also adhere to the practices outlined in the Mozilla [privacy policy](https://www.mozilla.org/privacy/) for how we receive, handle and share information we collect from Firefox.

## Firefox by default shares data to:

### Improve performance and stability for users everywhere {: #health-report }

* __Interaction data__: Firefox sends data about your interactions with Firefox to us (such as number of open tabs and windows; number of webpages visited; number and type of installed Firefox Add-ons; and session length) and Firefox features offered by Mozilla or our partners (such as interaction with Firefox search features and search partner referrals).

* __Technical data__: Firefox sends data about your Firefox version and language; device operating system and hardware configuration; memory, basic information about crashes and errors; outcome of automated processes like updates, safebrowsing, and activation to us.  When Firefox sends data to us, your IP address is temporarily collected as part of our server logs.

Read the telemetry documentation for [Desktop](https://firefox-source-docs.mozilla.org/toolkit/components/telemetry/telemetry/index.html), [Android](https://firefox-source-docs.mozilla.org/mobile/android/index.html), or [iOS](https://github.com/mozilla-mobile/firefox-ios/wiki/Telemetry) or learn how to opt-out of this data collection on [Desktop](https://support.mozilla.org/en-US/kb/share-data-mozilla-help-improve-firefox?redirectlocale=en-US&redirectslug=send-performance-data-improve-firefox) and [Mobile](https://support.mozilla.org/en-US/kb/send-usage-data-firefox-mobile-browsers).
{: #telemetry }

### Set a default search provider {: #defaultsearch }

* __Location data__:  When you first use Firefox, it uses your IP address to set your default search provider based on your country.  [Learn more](https://support.mozilla.org/kb/change-your-default-search-settings-firefox).

### Suggest relevant content

Firefox displays content, such as “Snippets” (messages from Mozilla), Add-on Recommendations, Top Sites (websites suggested by Mozilla for first-time Firefox users), and Pocket Recommendations (which is part of the Mozilla family).

* __Location data__: Firefox uses your IP address to suggest relevant content based on your country and state.

* __Technical & Interaction data__: Firefox sends us data such as the position, size and placement of content we suggest, as well as basic data about your interactions with Firefox’s suggested content. This includes the number of times suggested content is displayed or clicked.

* __Webpage data for Snippets__: When you choose to click on a Snippet link, we may receive data about the link you followed. This information is not associated with any other information about you. [Learn more](https://abouthome-snippets-service.readthedocs.io/en/latest/data_collection.html).
{: #snippets }

* __Webpage, Language, and Location data for Pocket Recommendations__: We recommend content to you based on your browsing history, language, and country location. The process of deciding which stories you should see based on your browsing history happens locally in your copy of Firefox, and neither Mozilla nor Pocket receives a copy of your browsing history. To help you see relevant Pocket Recommendations based on your location, Firefox shares your language and country location with Pocket.

    Mozilla and Pocket receive aggregated data about the recommendations you see and click. We also share aggregated data about the sponsored content you see and click with our third-party ad platform Adzerk so advertisers can see how many people click on their articles. This aggregated data does not identify you personally.

* __Location data and Interaction data for Top Sites__: When you click the Amazon.com Top Site tile on New Tab, we share your country and the time you clicked with Amazon and AdMarketplace (a third-party referral platform) to verify you navigated to Amazon. Firefox does not share your IP address or any other information that could be used to identify you with either Amazon or AdMarketplace.

* __Add-on and Feature Recommendations__: We recommend Add-ons in two places: the Manage Your Extensions Page (about:addons) and the Awesome Bar, where you search or type in URLs. We may also recommend Firefox Features in the Awesome Bar. We base the recommendations in about:addons on a cookie. We base the recommendations in the Awesome Bar on your interaction with Firefox. Mozilla does not receive your browser history. The process happens locally in your own computer’s copy of Firefox. Learn More about [Awesome Bar recommendations](https://support.mozilla.org/kb/extension-recommendations) or [Extensions Page recommendations](https://support.mozilla.org/kb/personalized-extension-recommendations).

### Improve security for users everywhere {: #security }

**Webpage data to DNS Resolver service**: For some Firefox users in the United States, Firefox routes DNS requests to a resolver service that has agreed to Mozilla’s [strict privacy standards for resolvers](https://wiki.mozilla.org/Security/DOH-resolver-policy). This provides added protection from privacy leaks to local networks and also from certain DNS security attacks. System logs of your DNS requests are deleted from the service within 24 hours and are only used for the purpose of DNS resolution.  [Learn more](https://support.mozilla.org/kb/firefox-dns-over-https#w_switching-providers) or see our default DNS resolver service providers below:

* [__Cloudflare__](https://developers.cloudflare.com/1.1.1.1/privacy/firefox/)
* [__NextDNS__](https://nextdns.io/privacy)
* [__Comcast__](https://www.xfinity.com/privacy/policy/dns)

**Technical data for updates**: Desktop versions of Firefox check for browser updates by persistently connecting to Mozilla servers. Your Firefox version, language, and device operating system are used to apply the correct updates. Mobile versions of Firefox may connect to another service if you used one to download and install Firefox. [Learn more](https://support.mozilla.org/kb/how-stop-firefox-automatically-making-connections#w_auto-update-checking).
{: #auto-updates }

**Technical data for add-ons blocklist**: Firefox for Desktop and Android periodically connect to Mozilla to protect you and others from malicious add-ons.  Your Firefox version and language, device operating system, and list of installed add-ons are needed to apply and update the add-ons blocklist. [Learn more](https://support.mozilla.org/kb/how-stop-firefox-making-automatic-connections).

**Webpage and technical data to Google’s SafeBrowsing service**: To help protect you from malicious downloads, Firefox sends basic information about unrecognized downloads to Google's SafeBrowsing Service, including the filename and the URL it was downloaded from.[Learn more](https://support.mozilla.org/kb/how-does-phishing-and-malware-protection-work) or read [Google’s Privacy Policy](https://www.google.com/policies/privacy/). Opting out prevents Firefox from warning you of potentially illegitimate or malicious websites or downloaded files.

**Webpage and technical data to Certificate Authorities**: When you visit a secure website (usually identified with a URL starting with "HTTPS"), Firefox validates the website's [certificate](https://support.mozilla.org/kb/secure-website-certificate). This may involve Firefox sending certain information about the website to the Certificate Authority identified by that website. Opting out increases the risk of your private information being intercepted. [Learn more](https://support.mozilla.org/kb/advanced-settings-browsing-network-updates-encryption#w_certificates-tab).

### Crash reports {: #crash-reporter }
By default on desktop versions of Firefox, we will ask you to share a report with more detailed information about crashes with Mozilla, but you always have the choice to decline.

* __Sensitive data__:  Crash reports include a ‘dump file’ of Firefox’s memory contents at the time of the crash, which may contain data that identifies you or is otherwise sensitive to you.

* __Webpage data__:  Crash reports include the active URL at time of crash.

* __Technical data__:  Crash reports include data on why Firefox crashed and the state of device memory and execution during the crash.

Read the full documentation [here](https://firefox-source-docs.mozilla.org/toolkit/crashreporter/crashreporter/index.html).

### Measure and support our marketing

* __Campaign and Referral Data__: This helps Mozilla understand the effectiveness of our marketing campaigns.
{: #referraltracking }

    _On Desktop_: Firefox by default sends Mozilla HTTP data that may be included with Firefox’s installer.  This enables us to determine the website domain or advertising campaign (if any) that referred you to our download page. Read the [documentation](https://firefox-source-docs.mozilla.org/toolkit/components/telemetry/telemetry/data/environment.html#attribution) or [opt-out](https://support.mozilla.org/kb/desktop-privacy) before installation.

    _On Android_: Firefox by default sends mobile campaign data to Adjust, our analytics vendor, which has its own [privacy policy](https://www.adjust.com/terms/privacy-policy/).  Mobile campaign data includes a Google advertising ID, IP address, timestamp, country, language/locale, operating system, and app version. Read the [documentation](https://firefox-source-docs.mozilla.org/mobile/android/adjust.html).
{: #thirdparty }

* __Technical & Interaction Data__:

    _On iOS and Android_: Firefox by default sends data about what features you use in Firefox to Leanplum, our mobile marketing vendor, which has its own [privacy policy](https://www.leanplum.com/privacy/).  This data allows us to test different features and experiences, as well as provide customized messages and recommendations for improving your experience with Firefox.

    Read the documentation for [iOS](https://github.com/mozilla-mobile/firefox-ios/blob/master/Docs/MMA.md) or [Android](https://firefox-source-docs.mozilla.org/mobile/android/mma.html), or learn how to [disable this feature](https://support.mozilla.org/kb/send-anonymous-usage-data-firefox-mobile-devices).

---

## If you use these features, Firefox will share data to provide you functionality and help us improve our products and services: {: #optional-features }

### Search

You can perform searches directly from several places in Firefox, including the Awesome Bar, Search Bar, or on a New Tab. _Mozilla does not receive your search queries._ We do receive data about how you engage with search in Firefox and the number of searches you request from our search partners. Query data is sent to your search provider, which has its own privacy policy. Links to our default search providers are:

* [__Google__](https://policies.google.com/privacy)
* [__Microsoft (Bing)__](https://privacy.microsoft.com/privacystatement)
* [__Yandex__](https://yandex.ru/legal/confidential/)

__Search Suggestions__: Firefox by default sends search queries to your search provider to help you discover common phrases other people have searched for and improve your search experience. These data will not be sent if your selected search provider does not support search suggestions.
{: #searchsuggestions }

[Learn more](https://support.mozilla.org/kb/use-popular-search-suggestions-firefox-search-bar), including how to disable this feature.

### Firefox Accounts & Join Firefox

* __Registration data__: Mozilla receives your email address and a hash of your password when you create a Firefox Account or sign-up to Join Firefox.  You can choose to include a display name or profile image.  Your email address is sent to our email vendor, SalesForce Marketing Cloud, which has its own [privacy policy](https://www.marketingcloud.com/privacy-policy/website-privacy-statement/).

* __Location data__: For security purposes, we store the IP addresses used to access your Firefox Account in order to approximate your city and country.  We use this data to send you email alerts if we detect suspicious activity, such as account logins from other locations.

* __Interaction data__: We receive data such as your visits to the Firefox Accounts website, dashboards and menu preferences, what products and services you use in connection with your Firefox Account, and your interactions with our emails and SMS messages. We use this to understand your use of our products and services and to send you more useful Firefox Account Tips and in-product messages.

* __Technical data__: To display which devices are synced to your Firefox Account and for security functionality, we store your device operating system, browser and version, timestamp, locale, and the same information for devices connected to your account.  If you use your Firefox Account to log into other websites or services (such as AMO or Pocket), we receive the timestamp of those log-ins.

Read the full documentation or learn more, including how to manage your Firefox Account data or our data practices for [websites and email](https://www.mozilla.org/privacy/websites/).  You can also read the privacy notices for our Firefox Account connected services, which are:

* [Firefox Lockwise](https://support.mozilla.org/kb/firefox-lockwise-and-privacy)
* [Firefox Monitor](https://www.mozilla.org/privacy/firefox-monitor)
* [Firefox Notes](https://addons.mozilla.org/firefox/addon/notes-by-firefox/)
* [Firefox Send](http://send.firefox.com/legal)
* [Firefox Sync](https://www.mozilla.org/privacy/firefox/#sync)

### Sync {: #sync }

* __Synced data__: If you enable Sync, Mozilla receives the information that you sync across devices in encrypted form. This may include Firefox tabs, add-ons, passwords, payment autofill information, bookmarks, history, and preferences.  Deleting your Firefox Account will delete related Firefox Sync content. You can also read the [documentation](https://moz-services-docs.readthedocs.io/en/latest/sync/).

* __Technical and Interaction data__: If you enable sync, Firefox will periodically send basic information using Telemetry about the most recent attempt to sync your data, such as when it took place, whether it succeeded or failed, and what type of device is attempting to sync. You can also read the [documentation](https://firefox-source-docs.mozilla.org/toolkit/components/telemetry/telemetry/data/sync-ping.html).

[Learn more](https://support.mozilla.org/kb/how-do-i-set-sync-my-computer), including how to enable or disable sync.

### Location {: #location-services }

* __Location data to Google's geolocation service__: Firefox always asks before determining and sharing your location with a requesting website (for example, if a map website needs your location to provide directions).  To determine location, Firefox may use your operating system’s geolocation features, Wi-fi networks, cell phone towers, or IP address, and may send this data to Google's geolocation service, which has its own [privacy policy](https://www.google.com/privacy/lsf.html).

[Learn more](https://www.mozilla.org/firefox/geolocation/).

### Website notifications {: #push-notifications }

* __Connection data__: If you allow a website to send you notifications, Firefox connects with Mozilla and uses your IP address to relay the message.  Mozilla cannot access the content of messages.

* __Interaction data__: We receive aggregate data such as the number of Firefox subscriptions and unsubscriptions to website notifications, number of messages sent, timestamps, and senders (which may include specific website providers).

Read the [full documentation](https://mozilla-push-service.readthedocs.io/en/latest/) or [learn more](https://support.mozilla.org/kb/push-notifications-firefox), including how to revoke website notifications.

### Add-ons {: #addons }

You can install Add-ons from addons.mozilla.org (“AMO”) or from the Firefox Add-ons Manager, which is accessible from the Firefox menu button in the toolbar.

* __Search queries__: Search queries in the Add-on Manager are sent to Mozilla to provide you with suggested Add-ons.

* __Interaction data__:  We receive aggregate data about visits to the AMO website and the Add-ons Manager in Firefox, as well as interactions with content on those pages. Read about data practices on [Mozilla websites](https://www.mozilla.org/privacy/websites/).

* __Technical data for updates__: Firefox periodically connects with Mozilla to install updates to Add-ons.  Your installed Add-ons, Firefox version, language, and device operating system are used to apply the correct updates.

---

### Footnote

This privacy notice is for the most recent general release version of Firefox distributed by Mozilla.  If you obtain Firefox elsewhere, or are running an older version, your copy of Firefox may contain different privacy characteristics.
{: #pre-release }

Mozilla’s pre-release versions of Firefox (which are distributed through channels such as Nightly, Beta, Developer Edition and TestFlight) are development platforms frequently updated with experimental features and studies.  In addition to the data collection described in this Privacy Notice, these versions by default may send certain types of web activity and crash data to Mozilla and in some cases to our partners.  Any data collection or sharing adheres to our [Firefox data collection policy](https://wiki.mozilla.org/Firefox/Data_Collection) and we will always be transparent and provide you with controls.
