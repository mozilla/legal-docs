# Mozilla Legal Documents

[![Reference Linter](https://github.com/mozilla/legal-docs/actions/workflows/doc_linter_ref.yml/badge.svg)](https://github.com/mozilla/legal-docs/actions/workflows/doc_linter_ref.yml)

[![L10n Linter](https://github.com/mozilla/legal-docs/actions/workflows/doc_linter_l10n.yml/badge.svg)](https://github.com/mozilla/legal-docs/actions/workflows/doc_linter_l10n.yml)

This repository contains legal documents and their applicable translations. Each subdirectory represents a single legal document. Within a document directory is a series of markdown files, each named for the language the document is written in. For instance, `firefox_privacy_notice/de.md` is the German version of the Firefox privacy policy.

## Editing

### Legal Team

If you're a member of the legal team, it's easy to get started. First, make sure you're logged in with your GitHub account. When you have a change which you wish to make, simply find the `en-US.md` version of the document that you wish to change. Open it and press the `Edit` button. If you have never gone through this process before, you will be asked to "fork" the repository (you should).

On the edit page, you'll be presented with a "raw" version of the legal document. Edit the text you wish to change. When you are done editing, there will be a section at the bottom of the page to save your work. Under "Commit summary", enter a brief (tweet-length) description of the change(s) you're making. In the "Extended description" field, explain what the changes are and why they're needed. When you're done, commit your changes.

At this point, you'll be presented with a form to submit a pull request. The bottom section of the page will show all of the change you've made to the document, and all you should need to do is press the "Send Pull Request" button.

Once you've submitted a pull request, your colleagues can review the work under the Pull Requests tab on the right-hand side, and a contributor to the repo can merge your changes.

### Markdown

These files are written in the [Markdown syntax](https://daringfireball.net/projects/markdown/syntax). In some languages, the date format contains dots like `15. travnja 2014.` but this may end up as an ordered list according to the syntax. The workaround is using a backslash to escape a dot after the leading digit(s) like `15\. travnja 2014.`

Some Markdown files use the [Attribute Lists extension](https://python-markdown.github.io/extensions/attr_list/) of the [Python Markdown library](https://pypi.python.org/pypi/Markdown). This is useful when you'd like to set the ID or class of an element, but the extended syntax may cause an error if your parser doesn't support this extension.

### PDF

A [subset of documents](https://github.com/mozilla/legal-docs/blob/main/.github/scripts/pdf_sources.json) is converted to PDF format via [automation](https://github.com/mozilla/legal-docs/blob/main/.github/workflows/pdf_generation.yml). Each localized PDF document is saved in a `pdf` subfolder within the locale folder.

### Localization

Localization of these documents is managed through an external vendor. As a localizer, you're encouraged to find and fix translation issues. All document translations should match the precise meaning in the corresponding `en` version of the document. Additionally, we're always interested in finding errors in markup, broken links, etc.

File a pull request that updates your locale's markdown file to match the `en` version as closely as possible. When you're done, submit a pull request. Someone at Mozilla will review your changes. If there are no problems, your changes will be merged.

Important: we won't be accepting brand new translations for existing documents, only fixes to existing ones.

A summary of the localization status is [available here](http://mozilla.github.io/legal-docs/), with a list of localized and non localized documents.

### Package.json

[Firefox Accounts](https://github.com/mozilla/fxa/tree/main/packages/fxa-content-server) relies on `package.json` to import this repository through `npm` and convert specific documents to HTML.

## Getting changes to production

For www.mozilla.org, the process is as follows:

1. Check the documents to be published on the staging site and make sure they look right:
    * https://www-dev.allizom.org/privacy/
    * https://www-dev.allizom.org/about/legal/
2. [Open this link](https://github.com/mozilla/legal-docs/actions/workflows/prod_push.yml) to access the _Actions_ tab in the repo on the `Publish Documents to Production` workflow. ![Screen Shot 2022-03-25 at 09 35 53](https://user-images.githubusercontent.com/19176817/160134801-1cacc2fa-ba16-4c11-a0fd-1dc9ac6b7240.png)
3. There will be a banner that says "This workflow has a workflow_dispatch event trigger." and, next to it on the right, a button that says `Run Workflow`. Click this button. ![Screen Shot 2022-03-25 at 09 36 14](https://user-images.githubusercontent.com/19176817/160134925-05b56aec-4c0a-4104-bc1e-e57c9cb812d0.png)
4. A form should now open with a field for a list of "files to publish". The default value is `ALL`. If you change nothing and click the `Run workflow` button, all changes to all files will be included in the pull request that is opened. If that is not what you want, you can enter file names in this field. It can be a comma separated list of filenames (e.g. `mdn_plus_terms.md, mdn_plus_privacy.md`), or you can use the `*` character to include all files with a prefix (e.g. `mdn_plus_*`).
5. Click `Run workflow`.
6. It may take a few seconds, but the running workflow will show up on the screen with an animated progress indicator. ![Screen Shot 2022-03-25 at 09 38 40](https://user-images.githubusercontent.com/19176817/160135112-29db7e7c-7589-4055-a56a-577ad3527344.png)
7. Once this is finished, and everything was successful, a new [Pull Request](https://github.com/mozilla/legal-docs/pulls?q=is%3Aopen+is%3Apr+label%3Aprod) should have been opened with all of the requested changes.
8. Review this Pull Request. It will have the title `[prod] Publish document updates`.
9. Once you are satisfied that the correct changes have been included, merge the Pull Request and the changes will be published to the website within a few minutes.

## URL Inventory

Following is a list of directories in this repository and either their URL counterparts on the web or directions to see the document in case it isn't easily linkable.  The URLs below will link to the *English (US)* versions of the document but replacing *en-US* in the URL with an available language code will show alternative languages.

Generally speaking Privacy Notice documents will be at https://www.mozilla.org/privacy/ and Terms documents at
https://www.mozilla.org/about/legal/.

* /firefox_privacy_notice
    * https://www.mozilla.org/en-US/privacy/firefox/
* /mozilla_privacy_policy
    * https://www.mozilla.org/en-US/privacy/
* /websites_privacy_notice
    * https://www.mozilla.org/en-US/privacy/websites/
