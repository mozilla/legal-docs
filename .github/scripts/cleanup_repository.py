#! /usr/bin/env python3

import os
import json
import shutil


def main():
    script_path = os.path.dirname(__file__)
    root_path = os.path.abspath(os.path.join(script_path, os.pardir, os.pardir))

    with open(os.path.join(script_path, "sources.json")) as f:
        config_data = json.load(f)
        source_folders = config_data["source_folders"]
        translated_docs = config_data["translated_docs"]

    # Get folders in the root, ignore hidden folders
    root_folders = [
        f
        for f in next(os.walk(root_path))[1]
        if not f.startswith(".") and f not in source_folders
    ]
    root_folders.sort()

    # Get files in the root, ignore hidden files
    (_, _, root_files) = next(os.walk(root_path))
    root_files = [f for f in root_files if not f.startswith(".")]

    # Remove all folders and files, except the ones in source folders
    for d in root_folders:
        shutil.rmtree(os.path.join(root_path, d))
    for f in root_files:
        os.remove(os.path.join(root_path, f))

    # Get the list of files in the source folders
    source_files = []
    for folder in source_folders:
        for doc in os.listdir(os.path.join(root_path, folder)):
            if not doc.startswith("."):
                source_files.append(os.path.join(folder, doc))
    source_files.sort()

    # Remove source files that are not translated
    for f in source_files:
        if f not in translated_docs:
            os.remove(os.path.join(root_path, f))


if __name__ == "__main__":
    main()
