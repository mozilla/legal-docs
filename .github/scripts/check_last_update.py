#! /usr/bin/env python3

from collections import defaultdict
from pathlib import Path
import argparse
import json
import os
import re
import sys


def extractUpdateDate(filename):
    """Extract update date from file"""

    date_pattern = re.compile(
        '.*{:\s?datetime="(?P<update>[0-9]{4}-[0-9]{2}-[0-9]{2})"\s?}.*'
    )

    with open(filename, "r") as fp:
        for line in fp:
            matches = date_pattern.match(line)
            if matches:
                dates = matches.groupdict()
                return dates["update"]


def findAllFiles(path):
    """Create a list of all markdown files in path"""

    files = defaultdict(list)
    search_path = Path(path)
    file_paths = search_path.glob(f"*/*.md")

    for fp in file_paths:
        # Threat the first folder as locale code
        locale = str(fp.parent.relative_to(path))
        filename = str(fp.name)
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
    args = parser.parse_args()

    files_list = findAllFiles(args.files_path)

    data = defaultdict(dict)
    for locale, filenames in files_list.items():
        for f in filenames:
            data[f][locale] = extractUpdateDate(
                os.path.join(args.files_path, locale, f)
            )

    ref_locale = args.ref_locale
    locales = list(data.keys())
    locales.sort()
    for filename, locale_dates in data.items():
        ref_date = data[filename][ref_locale] if ref_locale in data[filename] else None
        if ref_date == None:
            print(f"{filename}: missing update date in reference file")
        else:
            errors = []
            for locale, locale_date in locale_dates.items():
                if locale == ref_locale:
                    continue
                if locale_date != ref_date:
                    if locale_date == None:
                        errors.append(f"  - {locale}: Missing date")
                    else:
                        errors.append(f"  - {locale}: Outdated ({locale_date})")
            if errors:
                print(f"{filename} (reference: {ref_date})")
                errors.sort()
                print("\n".join(errors))


if __name__ == "__main__":
    main()
