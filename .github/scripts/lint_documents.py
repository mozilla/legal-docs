#! /usr/bin/env python3

from collections import Counter, defaultdict
from bs4 import BeautifulSoup
from pathlib import Path
import argparse
import markdown
import json
import os
import re
import string
import sys
from functions import findAllFiles


class DocumentCheck:
    def __init__(self, files_path, ref_locale, exceptions_path):
        self.files_path = files_path
        self.ref_locale = ref_locale
        self.errors = []

        self.allowed_characters = set(string.ascii_lowercase + string.digits + "_")

        self.files_list = findAllFiles(self.files_path)
        self.extractData()
        self.loadExceptions(exceptions_path)

    def showResults(self):
        print("\n".join(self.errors))

    def extractData(self):
        data = defaultdict(dict)
        for locale, filenames in self.files_list.items():
            locale_data = defaultdict(dict)
            for f in filenames:
                # Extract links
                filename = os.path.join(self.files_path, locale, f)
                content = Path(filename).read_text()
                links = self.extractLinks(content)

                # Extract anchors
                with open(filename, "r") as fp:
                    content = fp.readlines()
                    anchors = self.extractAnchors(content)

                locale_data[f] = {
                    "anchors": anchors,
                    "links": links,
                }
            data[locale] = locale_data

        self.md_data = data

    def extractLinks(self, content):
        """Convert Markdown to HTML, extract all links"""

        links = []
        html_content = markdown.markdown(content)
        doc = BeautifulSoup(html_content, "html.parser")
        for link in doc.findAll("a"):
            # For anchors without an href attribute, store the id
            href = link.get("href", link.get("id", None))
            if href:
                links.append(href)

        return links

    def extractAnchors(self, content):
        """Extract anchors, including the surrounding text"""

        anchors = []
        anchor_pattern = re.compile(r"(?P<anchor>{:\s*#[a-z0-9-]+\s*})", re.IGNORECASE)
        for line in content:
            # Strip line carriage
            line = line.strip()
            matches = anchor_pattern.findall(line)
            if matches:
                line_anchors = []
                for m in matches:
                    line_anchors.append(
                        {
                            "pre": line[0 : line.find(m)],
                            "anchor": m,
                            "post": line[line.find(m) + len(m) :],
                        }
                    )
                anchors.append(line_anchors)

        return anchors

    def loadExceptions(self, exceptions_path):
        exceptions = defaultdict(list)
        if exceptions_path and os.path.exists(exceptions_path):
            with open(exceptions_path, "r") as f:
                exceptions = json.load(f)

        self.exceptions = exceptions

    def checkDocuments(self, check_type):
        if check_type == "ref":
            # Check only the reference locale
            locales = [self.ref_locale]
        else:
            # Check all locales but the reference
            locales = list(self.md_data.keys())
            locales.remove(self.ref_locale)
            locales.sort()

        ref_data = self.md_data[self.ref_locale]
        for locale in locales:
            locale_errors = []
            for f, f_data in self.md_data[locale].items():
                file_errors = []
                exception_id = f"{locale}/{f}"

                # For the reference locale, check the filename. Only lowercase
                # characters, digits, and underscores are allowed.
                if locale == self.ref_locale:
                    if set(f.removesuffix(".md")) - self.allowed_characters:
                        file_errors.append(
                            f"The filename should only user lowercase letters, digits, and underscores ({f})"
                        )

                # Check anchors
                if exception_id not in self.exceptions["anchors"]:
                    file_errors.extend(self.checkAnchors(f_data["anchors"]))

                # Check links
                for link in f_data["links"]:
                    if "en-US/" in link:
                        file_errors.append(f"en-US should not be used in links: {link}")
                    if "http://" in link:
                        file_errors.append(f"https should be used in links: {link}")

                # Compare links and anchors with reference locale
                if locale != self.ref_locale and f in ref_data:
                    for type in ["links", "anchors"]:
                        file_errors.extend(
                            self.compareData(type, f_data, ref_data[f], exception_id)
                        )

                if file_errors:
                    locale_errors.append(f"  File: {f}")
                    for e in file_errors:
                        locale_errors.append(f"    {e}")

            if locale_errors:
                self.errors.append(f"\nLocale: {locale}")
                self.errors.extend(locale_errors)

        return self.errors

    def checkAnchors(self, anchors):
        """Check for issues in anchors"""

        errors = []
        for line_anchors in anchors:
            if len(line_anchors) > 1:
                errors.append(
                    f"Documents should not have multiple anchors on the same line.\n"
                    f"      Line: {line_anchors[0]['pre']}{line_anchors[0]['anchor']}{line_anchors[0]['post']}"
                )
            for a in line_anchors:
                if len(a["pre"]) > 0 and a["pre"] == a["pre"].strip():
                    errors.append(
                        f"Anchors should be preceded by a space.\n"
                        f"      Line: {a['pre']}{a['anchor']}{a['post']}"
                    )
                if "{: " not in a["anchor"]:
                    errors.append(
                        f"Anchor name should be preceded by a space.\n"
                        f"      Anchor: {a['anchor']}"
                    )
                if a["post"]:
                    errors.append(
                        f"Anchors should not be followed by other text.\n"
                        f"      Line: {a['pre']}{a['anchor']}{a['post']}"
                    )

        return errors

    def list_difference(self, l1, l2):
        # Create list of elements that differ between the two lists,
        # preserving duplicates and order.
        count = Counter(l1)
        count.subtract(l2)
        diff = []
        for e in l1:
            if count[e] > 0:
                count[e] -= 1
                diff.append(e)

        return diff

    def compareData(self, type, locale_data, reference_data, exception_id):
        errors = []
        if type == "links":
            l10n_list = locale_data[type]
            ref_list = reference_data[type]
        else:
            l10n_list = [e[0]["anchor"] for e in locale_data[type]]
            ref_list = [e[0]["anchor"] for e in reference_data[type]]

        if l10n_list != ref_list:
            # Cannot convert lists into set to find the differences,  because
            # it will remove duplicates.
            missing = self.list_difference(ref_list, l10n_list)
            additional = self.list_difference(l10n_list, ref_list)

            differences = [f"-{e}" for e in missing] + [f"+{e}" for e in additional]

            # Don't print links listed in exceptions
            if type == "links" and exception_id in self.exceptions[type]:
                differences = [
                    d
                    for d in differences
                    if d not in self.exceptions[type][exception_id]
                ]

            differences.sort()

            if len(differences) == 0:
                return []

            if (
                exception_id in self.exceptions[type]
                and differences == self.exceptions[type][exception_id]
            ):
                return []

            errors.append(f"There are differences in {type}")
            for e in differences:
                if e.startswith("-"):
                    errors.append(f"- (missing) {e[1:]}")
                else:
                    errors.append(f"- (added) {e[1:]}")

        return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path",
        required=True,
        dest="files_path",
        help="Path to folder including subfolders for all locales",
    )
    parser.add_argument(
        "--ref",
        required=False,
        dest="ref_locale",
        default="en",
        help="Reference locale code (default 'en')",
    )
    parser.add_argument(
        "--type",
        required=False,
        default="l10n",
        choices=["l10n", "ref"],
        help="Analyze the reference locale (type='ref') or other locales (type='l10n')",
    )
    parser.add_argument(
        "--exceptions",
        nargs="?",
        dest="exceptions_file",
        help="Path to JSON exceptions file",
    )
    args = parser.parse_args()

    checks = DocumentCheck(args.files_path, args.ref_locale, args.exceptions_file)
    repo_errors = checks.checkDocuments(args.type)

    if repo_errors:
        checks.showResults()
        sys.exit(1)
    else:
        print("No issues found.")


if __name__ == "__main__":
    main()
