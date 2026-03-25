# Smart Window Privacy Policy

March 6, 2026
{: datetime="2026-03-06" }

## Smart Window allows you to use AI to enhance your browsing experience

Safety, transparency, privacy, and user choice have always been core to Firefox, and those values also guide the design of its AI-enhanced version, Smart Window.

Smart Window is completely optional and opt-in. If activated, it builds on the classic Firefox experience (classic window) by using AI to enhance your browsing experience. It allows you to interact with a digital assistant that learns how you use the web, adapts to your preferences, and helps you complete tasks more efficiently. To do so, it collects and processes certain information about your browsing, including real-time Smart Window activity.

When using Smart Window, Mozilla processes certain data specifically to provide these AI-enhanced features. That processing is governed by this Smart Window Privacy Notice, in addition to the [Firefox Privacy Notice](https://www.mozilla.org/privacy/firefox/), which continues to apply to your use of classic Firefox. To the extent there is any inconsistency between them with respect to Smart Window-related processing, this notice will govern.  Your use of Smart Window is also subject to the [Smart Window Terms of Use](https://www.mozilla.org/about/legal/terms/smart-window/) and the [Firefox Terms of Use](https://www.mozilla.org/about/legal/terms/firefox/).

You need a Mozilla account to use Smart Window. Creating and using that account involves processing additional data — such as account activity and contact information — as described in the [Mozilla Accounts Privacy Notice](https://www.mozilla.org/privacy/mozilla-accounts/).

You can open a Firefox classic window at any time in the File menu of your browser, or toggle between Smart and classic windows using the icon in the top right corner. Your use of classic windows will be governed by the [Firefox Privacy Notice](https://www.mozilla.org/privacy/firefox/), unless and until you choose to open a new Smart Window.

You can choose to use Smart Window with a model endpoint other than those provided by Mozilla by customizing the settings in your Smart Window preferences. Note that if you select a model endpoint not offered in the Smart Window interface, your information will be processed by that endpoint and will not be routed through a Mozilla server. If that endpoint is operated by a third party, its terms of service and privacy notice will apply.

## How is your data used?

### To create Memories about your activity

Smart Window infers information about you based on your interactions with the assistant and your [recent Firefox browsing activity](#missing-link), including websites you have visited. This may include activity outside of Smart Window (such as in classic windows), but it does not include activity in Private Windows. By default, this information is processed on a Mozilla server to infer your interests, which we call Memories. For example, if you search for “vegan restaurants,” chat about vegan recipe substitutions, and submit queries like “are Oreos vegan?,” the assistant may infer an interest in veganism. We do not retain this information on our servers after processing. Instead, Memories are stored locally on your device and automatically expire after a limited period unless your subsequent activity indicates continued relevance.

You can review or delete a specific Memory in your settings, block all Memories from being used in a particular chat, or remove a specific Memory from a chat and re-run the associated query without it. More information about how to manage your Memories can be found [here](#missing-link).

### To provide the Smart Window Assistant

The assistant feature lives in your Smart Bar, and can help improve your searches, answer questions, retrieve pages you have visited in classic or Smart Windows, and make information on the web easier to consume. To provide these features, the Assistant processes your query and, where relevant to your request, limited browsing context and stored Memories. When you submit a query in the Smart Bar, the assistant uses a local (on device) intent classification model to determine whether the query is best addressed by a **chat** or a **search**.

If your query is classified as a chat, the assistant will leverage any potentially relevant stored Memories or browsing context to tailor the prompt. For example, if your query relates to your past browsing activity (such as “what were the ingredients of that chicken pasta recipe I saw yesterday?” or “compare the five different black sneakers I looked at last week”), the assistant may review limited browsing data from your history—namely page titles and URLs—to identify potentially relevant content, access those pages in the background, and incorporate relevant content from those pages into the proposed prompt. You can exclude specific pages by deleting them from your history or bookmarks or, when the assistant’s search is limited to open tabs, by closing the relevant tab.

Where your query appears to contain location-related information, the assistant may infer your location to further personalize prompts.

The assistant sends the full prompt (including your query, any relevant Memories, and any additional relevant browsing context) to a Mozilla server.

Upon receipt, Mozilla forwards the request to a third-party large language model (LLM) on your behalf. The LLM receives the request from Mozilla, not directly from you, and sees a Mozilla IP address rather than your own. The request includes only the information needed to generate a response. Additional information about our LLM partners, and how you can select which LLM you use, is available [here](#missing-link).

The LLM provides a response based on information in its knowledge base and information included in the prompt. We share that response with you in the chat, along with the specific Memories included in the prompt. You can then choose to disable Memories and re-run the prompt without them, continue or close the chat, or initiate a broader web search.

If the assistant cannot provide a satisfactory response or classifies your query as a **search**, it may tailor your query using relevant Memories, browser context, or chat history to help find the information you seek. Once submitted, your search provider will process that query in accordance with its own Privacy Notice.

### To maintain improve features, performance and stability

We also process data to keep Smart Window operational, improve features and performance, and identify, troubleshoot, and diagnose issues, including feedback you choose to provide us with about the assistant. Mozilla never retains chat logs without your permission.

We designed Smart Window to give users access to new, innovative features as soon as they become available and we may offer experimental Smart Window features on a temporary basis. Some experiments may involve additional processing of technical, system performance, location, settings, interaction and browsing data to assess usage, functionality, stability, and other concerns. Where an experiment would involve material changes to how we process your information, we will provide notice of those changes as described below.

## Changes

Mozilla aims to remain at the forefront of AI browser technology and may update Smart Window and this notice by posting those changes online and updating the effective date of this notice. If the changes are substantive, we will also announce the updates more prominently through Mozilla's usual channels for such announcements, such as through an in-product notification.
