# Mozilla Privacy Policy

March 6, 2026
{: datetime="2026-03-06" }

## Smart Window allows you to use AI to enhance your browsing experience

Safety, transparency, privacy, and user choice have always been core to Firefox, and those values also guide the design of its AI-enhanced version, Smart Window.
Smart Window is completely optional and opt-in. If activated, it builds on the classic Firefox experience (classic window) by using AI to enhance your browsing experience. It allows you to interact with a digital Assistant that learns how you use the web, adapts to your preferences, and helps you complete tasks more efficiently. To do so, it collects and processes certain information about your browsing, including real-time Smart Window activity.

When using Smart Window, Mozilla processes certain data specifically to provide these AI-enhanced features. That processing is governed by this Smart Window Privacy Notice, in addition to the [Firefox Privacy Notice](https://www.mozilla.org/en-US/privacy/firefox/), which continues to apply to your use of classic Firefox. To the extent there is any inconsistency between them with respect to Smart Window-related processing, this notice will govern.

You need a Mozilla account to use Smart Window. Creating and using that account involves processing additional data —such as account activity and contact information—as described in the [Mozilla Accounts Privacy Notice](https://www.mozilla.org/en-US/privacy/mozilla-accounts/).

You can open a Firefox classic window at any time in the File menu of your browser, or toggle between Smart and classic windows using the icon in the top right corner. Your use of classic Windows will be governed by the [Firefox Privacy Notice](https://www.mozilla.org/en-US/privacy/firefox/), unless and until you choose to open a new Smart Window.

You can choose to use Smart Window with a model or server other than those provided by Mozilla by customizing the settings in your Smart Window preferences.  Note that if you select a third-party model or server not offered in the Smart Window interface, your information will not be routed through a Mozilla server and will instead be processed directly by that provider, subject to its terms of service and privacy notice.

## How is your data used?

### To create Memories about your activity

Smart Window infers information about you based on your interactions with the Assistant and your recent Firefox browsing activity, including websites you have visited. This may include activity outside of Smart Window (such as in classic Windows), but does not include activity in Private Windows. By default, this information is processed on a Mozilla server to infer your interests, which we call Memories. For example, if you search for “vegan restaurants,” chat about vegan recipe substitutions, and submit queries like “are Oreos vegan?,” the Assistant may infer an interest in veganism.  We delete this information from our servers after it's been processed. Memories are stored locally on your device and automatically expire after a limited period unless your subsequent activity indicates continued relevance. You can review or delete a specific Memory in your settings, block all Memories from being used in a particular chat, or remove a specific Memory from a chat and re-run the associated query without it. More information about how to manage your Memories can be found here [Add relevant SUMO article].

### To provide the Smart Window Assistant

The assistant feature lives in your Smart Bar, and can help improve your searches, answer questions, retrieve pages that you have visited in classic or Smart Windows, or make information on the web easier to consume.

#### To help find what you’re looking for

When you submit a query in the Smart Bar and do not specifically indicate your intent, the assistant uses a local intent classification model to determine whether it can be best addressed by a **chat** or a **search**.

If a query is classified as a **chat**, the assistant may leverage  stored Memories that appear relevant to your query or incorporate additional information from your browsing history to tailor the prompt; for example:
    - If your query appears related to ***your open tabs*** (for example “help me come up with an itinerary for Paris based on the five travel blog posts I have open”), the assistant will include the titles and URLs of your open tabs in the prompt.
    - If your query appears related to ***your past browsing activity*** (for example, “what were the ingredients of that chicken pasta recipe I saw yesterday?” or “compare the five different black sneakers I looked at last week”), the assistant may review page titles and URLs to determine potentially relevant content, access those pages in the background, and incorporate relevant information into the prompt. You can exclude specific pages by deleting them from your history or bookmarks or, when the assistant’s search is limited to open tabs, by closing the relevant tab.
    - Where your query appears to contain location-related information, the assistant may infer your location to further personalize prompts.

The Assistant sends the full prompt (including your query, any relevant Memories, and any additional relevant browsing context) to a Mozilla server.

Upon receipt, Mozilla assigns a unique identifier to support aggregate usage tracking for the Smart Window feature and forwards the request to a third-party large language model (LLM) on your behalf. The LLM receives the request from Mozilla, not directly from you, and sees a Mozilla IP address rather than your own. The request includes only the information needed to generate a response. Additional information about our LLM partners, and how you can select which LLM you use, is available here.

The LLM provides a response based on information in its knowledge base and information included in the prompt. We share that response with you in the chat, along with the specific Memories included in the prompt. You can then choose to disable Memories and re-run the prompt without them, continue or close the chat, or initiate a broader web search.

If the assistant cannot provide a satisfactory response or classifies your query as a search, it may tailor your query using relevant Memories, browser context, or chat history to help find the information you seek. Once submitted, your search provider will process that query in accordance with its own Privacy Notice.

### To maintain improve features, performance and stability

We also process data to keep Smart Window operational, improve features and performance, and identify, troubleshoot, and diagnose issues, including feedback you may choose to provide us with about the assistant. Mozilla never retains chat logs without your permission.
We designed Smart Window to give users access to new, innovative features as soon as they become available and we may offer experimental Smart Window features on a temporary basis. Some experiments may involve additional processing of technical, system performance, location, settings, interaction and browsing data to assess usage, functionality, stability, and other concerns. Where an experiment would involve material changes to how we process your information, we will provide notice of those changes as described below.

## Changes

Mozilla aims to remain at the forefront of AI browser technology and may update Smart Window and this notice by posting those changes online and updating the effective date of this notice. If the changes are substantive, we will also announce the updates more prominently through Mozilla's usual channels for such announcements, such as through an in-product notification.
