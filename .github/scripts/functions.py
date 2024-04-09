#! /usr/bin/env python3

from collections import defaultdict
from pathlib import Path


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
