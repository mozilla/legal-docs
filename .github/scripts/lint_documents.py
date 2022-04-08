#! /usr/bin/env python3

from collections import defaultdict
from bs4 import BeautifulSoup
from pathlib import Path
import argparse
import markdown
import json
import os
import re
import sys


def extractLinks(content):
    """Convert Markdown to HTML, extract all links"""

    links = []
    html_content = markdown.markdown(content)
    doc = BeautifulSoup(html_content, "html.parser")
    for link in doc.findAll("a"):
        links.append(link.get("href"))

    return links


def extractAnchors(content):
    """Extract anchors, including the surrounding text"""

    anchors = []
    anchor_pattern = re.compile("(?P<pre>.*)?(?P<anchor>{:\s?#[a-z]+\s?})(?P<post>.*)?")
    for line in content:
        # Strip line carriage
        line = line.strip()
        matches = anchor_pattern.match(line)
        if matches:
            line_anchors = matches.groupdict()
            if line_anchors:
                anchors.append(line_anchors)

    return anchors


def checkAnchors(anchors):
    """Check for issues in anchors"""

    errors = []
    for anchor in anchors:
        if len(anchor["pre"]) > 0 and anchor["pre"] == anchor["pre"].strip():
            errors.append(
                f"Anchors should be preceded by a space. Anchor: |{anchor['anchor']}|"
            )
        if "{:" in anchor["pre"]:
            errors.append(
                f"Anchors should not be followed by other text. Anchor: |{anchor['pre']} {anchor['anchor']}|"
            )
        if "{: " not in anchor["anchor"]:
            errors.append(
                f"Anchor name should be preceded by a space. Anchor: |{anchor['anchor']}|"
            )
        if anchor["post"]:
            errors.append(
                f"Anchors should not be followed by other text ({anchor['post']}). Anchor: {anchor['anchor']} {anchor['anchor']}"
            )

    return errors


def findAllFiles(path):
    """Create a list of all markdown files in path"""

    files = defaultdict(list)
    search_path = Path(path)
    file_paths = search_path.glob(f"*/*.md")

    for fp in file_paths:
        # Threat the first folder as locale code
        locale = str(fp).split(os.sep)[0]
        filename = os.path.relpath(fp, os.path.join(path, locale))
        files[locale].append(filename)

    return files


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
        "--exceptions",
        nargs="?",
        dest="exceptions_file",
        help="Path to JSON exceptions file",
    )
    args = parser.parse_args()

    files_list = findAllFiles(args.files_path)

    data = defaultdict(dict)
    for locale, filenames in files_list.items():
        locale_data = defaultdict(dict)
        for f in filenames:
            # Extract links
            filename = os.path.join(args.files_path, locale, f)
            content = Path(filename).read_text()
            links = extractLinks(content)

            # Extract anchors
            with open(filename, "r") as fp:
                content = fp.readlines()
                anchors = extractAnchors(content)

            locale_data[f] = {
                "anchors": anchors,
                "links": links,
            }
        data[locale] = locale_data

    # Load exceptions
    exceptions = defaultdict(list)
    if args.exceptions_file:
        filename = args.exceptions_file
        if os.path.exists(filename):
            with open(filename, "r") as f:
                exceptions = json.load(f)

    ref_locale = args.ref_locale
    locales = list(data.keys())
    locales.sort()
    for locale in locales:
        locale_errors = []
        for f, f_data in data[locale].items():
            exception_id = f"{locale}::{f}"

            # Check anchors
            if exception_id not in exceptions["anchors"]:
                errors = checkAnchors(f_data["anchors"])

            # Check links
            if exception_id not in exceptions["links"]:
                for l in f_data["links"]:
                    if "en-US/" in l:
                        errors.append(f"en-US should not be used in links: {l}")
                    if "http://" in l:
                        errors.append(f"https should be used in links: {l}")

                # Compare links with reference locale
                if locale != ref_locale:
                    if f in data[ref_locale]:
                        if f_data["links"] != data[ref_locale][f]["links"]:
                            missing = list(
                                set(data[ref_locale][f]["links"]) - set(f_data["links"])
                            )
                            if missing:
                                errors.append("  Missing links:")
                                for m in missing:
                                    errors.append(f"  - {m}")
                            additional = list(
                                set(f_data["links"]) - set(data[ref_locale][f]["links"])
                            )
                            if additional:
                                errors.append("  Additional links:")
                                for m in additional:
                                    errors.append(f"  - {m}")

            if errors:
                locale_errors.append(f"  File: {f}")
                for e in errors:
                    locale_errors.append(f"    {e}")

        if locale_errors:
            print(f"\nLocale: {locale}")
            print("\n".join(locale_errors))


if __name__ == "__main__":
    main()
