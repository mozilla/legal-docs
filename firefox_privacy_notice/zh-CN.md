# Firefox 浏览器隐私权保护事宜通知

2017 年 6 月 5 日
{: datetime="2017-06-05" }

我们关心您的隐私。当 Firefox 向 Mozilla（即本公司）发送信息时，我们的[隐私权政策](https://www.mozilla.org/privacy/) 会就我们如何处理相关信息加以说明。

## 用户须知

Firefox 可自动与我们和我们的服务提供商连线，以提供更新、安全、片段 (Snippet)、Firefox 系统状况报告和其它功能。
{: #essential-features }

* **浏览器和附加组件更新**
{: #auto-updates }

	浏览器更新：每日一次；在检查浏览器是否有更新时，Firefox 会向 Mozilla 发送以下信息：您使用的 Firefox 版本信息、语言偏好、操作系统和版本。您可以[按照以下说明关闭更新功能](https://support.mozilla.org/kb/how-stop-firefox-automatically-making-connections#w_auto-update-checking)，但这可能会使您无法防范某些安全隐患。

	附加组件黑名单：Firefox 每天例行与 Mozilla 联系一次，以检查附加组件信息，检查是否有恶意附加组件。这些信息包括但不限于：浏览器版本、操作系统和版本、系统语言环境、请求使用相关组件的总次数、上次请求时间、当日时间、IP 地址和您已安装的附加组件列表。您可以随时[关闭元数据更新功能](https://blog.mozilla.org/addons/how-to-opt-out-of-add-on-metadata-updates/)，但这可能会使您无法防范某些安全隐患。

* **片段**
{: #snippets }

	Firefox 的默认主页 (&lt;about:home&gt;) 会在搜索栏下方加载少量我们认为对您有用的信息。我们将其称为“片段”。Firefox 大约每天会与 Mozilla 连线一次，为您提供最新的片段（若有）。Mozilla 可收集片段的点击频率、片段名称、浏览器语言环境和您使用的 Firefox 的版本等信息。我们仅以汇总形式将这些信息保留 60 天。

	为了显示相关的片段，Firefox 每月会向 Mozilla 发送请求，通过您的 IP 地址查看您所在的国家或地区。我们随后会将这一信息发回给 Firefox，由其在当地储存。Firefox 然后将基于这一当地储存的国家或地区信息选择向您显示的片段。

	一些 Mozilla 赞助的片段是互动性的，您可以选择是否与其分享您的电话号码或电子邮件地址。例如，您可以输入您的电话号码来接收短信，以在所用 Android 手机上安装 Firefox。您的信息由我们的电子邮件和手机营销供应商负责接收和处理。

* **Firefox 系统状况报告**
{: #health-report .inproduct-link }

	Firefox 系统状况报告 (FHR) 旨在为您提供有关所用浏览器的稳定性和使用性能方面的信息，以及您在遇到故障率高或者启动时间长等问题时所需的支持提示。Mozilla 收集并汇总您和其他 Firefox 用户的数据，并将其发回给浏览器，以便您查看所用 Firefox 浏览器的性能随时间推移的变化情况。这些数据包括但不限于：设备硬件、操作系统、Firefox 版本、附加组件（数目和类型）、浏览事件的发生时间、处理情况、会话恢复、会话时长、与搜索访问点的互动和使用 Firefox 搜索伙伴代码、设置文件的新旧程度、故障次数和页面数等。FHR 不会向 Mozilla 发送您访问的网址 (URL)。

	我们使用通过 FHR 发送的数据为用户提供 FHR 功能方面的信息，用以帮助您分析和解决浏览器在使用性能方面的问题。我们还可用汇集的 FHR 数据改进 Firefox 的总体性能。您可以选择[关闭数据分享功能](https://support.mozilla.org/kb/firefox-health-report-understand-your-browser-perf#w_how-to-turn-data-sharing-on-or-off)。

* **安全**
{: #security }

	Firefox 会自动检查恶意或伪造网页、损坏的附加组件和第三方颁发的 SSL 证书。

	安全网站证书：当您访问一个安全网站（即 https）时，Firefox 将验证该网站的证书。此项验证可能需与证书指定的第三方状态提供商通信。Firefox 将向所及第三方发送信息，以鉴定该网站的[证书](https://support.mozilla.org/kb/secure-website-certificate)。您可以[修改您的偏好](https://support.mozilla.org/kb/advanced-settings-browsing-network-updates-encryption#w_certificates-tab)，但如果您禁用在线验证功能，Firefox 则无法识别您所到网站。关闭此功能可能会增加您的私人信息被截获的风险。若遇到[不受信任的连接](https://support.mozilla.org/kb/connection-untrusted-error-message)，您也可以选择将相关证书发送给 Mozilla。

	Firefox 对伪造和攻击的防护：Firefox 每小时大约两次下载 Google 的安全浏览列表，以助用户封锁这些恶意或伪造网站及其下载内容（Google 的隐私权政策请见 <https://www.google.com/policies/privacy/>）。对于不在此列表中的已下载的可执行文件，Firefox 可向安全浏览服务发送包括与下载文件相关 URL 在内的元数据。有关安全浏览功能或如何关闭这一功能方面的详细信息，请访问 <https://support.mozilla.org/kb/how-does-phishing-and-malware-protection-work>。如果您禁用这些功能，Firefox 将无法就潜在非法或恶意网站及下载文件对您发出警报。

* **使用情况统计**（在非发布版本中亦称“遥测”功能）
{: #telemetry .inproduct-link}

	使用情况统计或“遥测”是 Firefox 的一项功能，用于向 Mozilla 传送有关用户界面功能、内存和硬件配置的使用、性能和响应方面的统计数据。您的 IP 地址也作为标准网络日志的一部分加以收集。使用情况统计通过 SSL 输送，用以帮助我们在将来的版本中对 Firefox 进行改进。发送给 Mozilla 后，使用情况统计将被汇总提供给各方开发者，其中包括 Mozilla 的员工和公益开发者。启用遥测功能时，某些短期实验项目可能会用之收集所访问网站的信息。

	这一功能在 Nightly、Developer Edition、Aurora 和 Beta 版本的 Firefox 中为默认开启，以帮助这些用户向 Mozilla 提供反馈。在 Firefox 的一般发行版本中，此功能为默认关闭。

	您可[在此了解更多关于遥测功能的信息](https://support.mozilla.org/kb/send-performance-data-improve-firefox) 以及如何启用和关闭方面的说明。

* **磁贴**
{: #tiles }

	磁贴是 Firefox 在新标签页上显示的一项功能。为了提供磁贴功能，Firefox 会向 Mozilla 发送与磁贴相关的数据，如点击数、印记、您的 IP 地址、语言环境信息和磁贴的相关信息（如位置和方格尺寸）。在 Beta 版的 Firefox 中，磁贴功能的一些短期遥测实验项目（见上），可能会用来收集用户经常访问的域名。

* **默认搜索**
{: #searchsuggestions }

	搜索建议功能可以帮助您找到其他人搜索过的常见短语。这些搜索建议是由您的默认搜索引擎（如 Google、Yahoo 等）提供的，并非来自 Firefox。如果您启用了这一功能，且您的默认搜索引擎支持搜索建议，则 Firefox 可能将您在智能地址栏或搜索栏中输入的词语发送给您的默认搜索引擎以获取建议。这一操作受到您默认搜索引擎适用的隐私政策的约束。您可以[在这里了解更多关于搜索建议的信息](https://support.mozilla.org/kb/use-popular-search-suggestions-firefox-search-bar)以及如何启用或禁用这一功能。

* **引荐和广告活动追踪**
{: #referraltracking }
{: #thirdparty }

	为帮助了解和改进我们的市场推广活动，Firefox 可能会发送“引荐数据”，如引荐您下载并安装 Firefox 的网站域名或广告宣传。
 
	在 Android 和 iOS 设备上，Firefox 会将引荐数据发送给我们的移动分析供应商，包括 Google 广告 ID、IP 地址、时间戳、国家或地区、区域设置、操作系统和应用程序版本。您可以点击 [此处](https://support.mozilla.org/kb/send-anonymous-usage-data-firefox-mobile-devices) 了解详情，包括如何禁用此报告。

	在桌面设备上，Firefox 会记录引荐数据并将其作为 Firefox 系统状况报告的一部分发送给 Mozilla。您可以点击 [此处](https://support.mozilla.org/kb/desktop-attribution-privacy) 了解详情，包括如何选择退出或禁用此报告。

---------------------------------------

当您提出要求时，Firefox 还能与 Mozilla 连线为您提供诸如同步、定位服务、故障报告和附加组件等功能。
{: #optional-features }

* **同步**
{: #sync }

	[Firefox 同步](https://www.mozilla.org/firefox/sync/) 是一项服务，允许您在所用各种设备上同步您的 Firefox 书签、浏览历史、密码和设置。如果您使用同步服务，请阅读[Firefox 同步服务隐私权政策通知](https://accounts.firefox.com/legal/privacy)。

* **定位服务**
{: #location-services }

	Firefox 的定位功能允许网站请求获得您所在地信息（例如，允许相关网站在地图上显示您所在位置）。若某网站请求您的位置信息，Firefox 会在向其提供该信息之前征求您的许可。为了确定您所在位置，Firefox 可能使用一些数据进行判断，包括您所用操作系统的地理定位功能、WiFi 网络、手机信号塔或 IP 地址。估测您所在位置时，系统需将其中一些信息发送给 Google 的地理定位服务，该项服务有其自己的[隐私权政策](https://www.google.com/privacy/lsf.html)。

* **故障报告**
{: #crash-reporter .inproduct-link }

	当 Firefox 出现故障时，您可通过相关选项，向 Mozilla 发送故障报告。此报告含能使我们改进 Firefox 的技术信息，其中包括 Firefox 出现故障的原因、出现故障时使用的 URL 以及出现故障时计算机内存的状态等资讯。我们所收到的故障报告中可能包含个人信息。我们会在 <https://crash-stats.mozilla.com/> 向公众提供部分故障报告。在向公众发布故障报告之前，我们会按操作步骤自动移除个人信息。我们不会移除您在评论栏中填写的任何内容。

* **SSL 错误**
{: #ssl-errors }

	当某一加密网站连接出现问题时，您可通过相关选项，向 Mozilla 发送错误报告。此报告将记录网站证书以及诊断用的错误代码。此信息有助于 Mozilla 监控“固定式”网站证书的效果并检测对用户的潜在钓鱼式攻击。

* **附加组件**
{: #addons }

	Firefox 在附加组件管理器中提供有“获取附加组件”页面，其中列有热门附加组件，并可根据您已经安装的附加组件显示相关的个性化推荐。为了显示个性化推荐，Firefox 会将相关信息发送给 Mozilla，其中包括您已经安装的附加组件列表、Firefox 版本信息以及您的 IP 地址。此通信只在“获取附加组件”页面打开时才会发生，而且您可在需要时按照[这里的说明](https://blog.mozilla.org/addons/how-to-opt-out-of-add-on-metadata-updates/)将其关闭。Firefox 的附加组件管理器里有一个搜索栏，您可以在此输入关键词进行搜索，Mozilla 会收集这些关键词搜索以及您所用的 Firefox 版本信息、语言环境和操作系统，用以为您显示相关推荐。

* **推送通知**
{: #push-notifications }

	如果您启用了推送通知，网站就可以向您发送通知和更新。为了获取通知，Firefox 会将您同意接受推送通知的网站信息发送给 Mozilla。 我们会在匿名表格中存储这一信息，以及每个网站向您发送的通知数量。 为了帮助开发者改进他们对于推送通知的使用，Mozilla 可能会与某些开发者分享汇总信息，包括有多少网站访问者订阅了或者取消订阅了他们的推送通知。您可以遵照[这些说明](https://support.mozilla.org/kb/push-notifications-firefox)在 Firefox 中管理推送通知。
	
##

除非另有说明，否则本隐私权政策通知旨在用于最近全面发行的几个 Firefox 版本。我们推出的几个预发行版本 (Beta、Aurora/Developer Edition、Nightly 以及 TestFlight) 目前仍处于开发阶段，可能会有一些新功能，或在隐私保护方面各有不同的特点。这些预发行版本会自动将[遥测数据](https://gecko.readthedocs.io/en/latest/toolkit/components/telemetry/telemetry/index.html) 传给 Mozilla，用以帮助我们改进 Firefox。
{: #pre-release }
