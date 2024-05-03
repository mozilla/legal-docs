#! /usr/bin/env python3

from collections import defaultdict
from pathlib import Path
import re


def extractUpdateDate(filename):
    """Extract update date from file"""

    date_pattern = re.compile(
        r'.*{:\s?datetime="(?P<update>[0-9]{4}-[0-9]{2}-[0-9]{2})"\s?}.*'
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
    file_paths = search_path.glob("*/*.md")

    for fp in file_paths:
        # Threat the first folder as locale code
        locale = str(fp.parent.relative_to(path))
        filename = str(fp.name)
        files[locale].append(filename)

    return files
