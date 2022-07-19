#! /usr/bin/env python3

import os
import json


def main():
    script_path = os.path.dirname(__file__)
    root_path = os.path.abspath(os.path.join(script_path, os.pardir, os.pardir))

    with open(os.path.join(script_path, "sources.json")) as f:
        source_folders = json.load(f)["source_folders"]

    # Get the list of files in the source folders
    source_files = []
    for folder in source_folders:
        for doc in os.listdir(os.path.join(root_path, folder)):
            if not doc.startswith(".") and not os.path.isdir(
                os.path.join(root_path, folder, doc)
            ):
                source_files.append(os.path.join(folder, doc))
    source_files.sort()

    # Get the list of files in all locale folders
    translated_files = []
    for root, dirs, files in os.walk(root_path, followlinks=True):
        # Ignore source folders
        if root == root_path:
            dirs[:] = [d for d in dirs if d not in source_folders]
        # Ignore hidden folders
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for filename in files:
            # Search for .md files, but not in the root
            if os.path.splitext(filename)[1] == ".md" and root != root_path:
                filename = os.path.relpath(os.path.join(root, filename), root_path)
                translated_files.append(filename)

    stats = {}
    for translation in translated_files:
        locale, filename = translation.split(os.path.sep)
        if filename not in stats:
            stats[filename] = {"count": 1, "locales": [locale]}
        else:
            stats[filename]["count"] += 1
            stats[filename]["locales"].append(locale)

    for f, data in stats.items():
        data["locales"].sort()

    source_filenames = [f.split(os.path.sep)[1] for f in source_files]

    translated_files = [f for f in list(stats.keys()) if f in source_filenames]
    translated_files.sort()

    output = []
    output.append("# Current Status\n")

    if translated_files:
        output.append(
            "List of translated files (number of locales between parentheses):"
        )
        for f in translated_files:
            count = len(stats[f]["locales"])
            output.append(f"* {f} ({count})")

    only_en_files = list(set(source_filenames) - set(stats.keys()))
    only_en_files.sort()
    if only_en_files:
        output.append("\nList of files not translated:")
        for f in only_en_files:
            output.append(f"* {f}")

    missing_en_files = list(set(stats.keys()) - set(source_filenames))
    missing_en_files.sort()
    if missing_en_files:
        output.append(
            "\n List of translated files not available in source folders (locale between parentheses):"
        )
        for f in missing_en_files:
            locales = ", ".join(stats[f]["locales"])
            output.append(f"* {f} ({locales})")

    with open(os.path.join(root_path, ".github", "README.md"), "w") as f:
        f.write("\n".join(output))
    with open(os.path.join(root_path, ".github", "stats.json"), "w") as f:
        json.dump(stats, f, indent=2, sort_keys=True)

    # Update sources.json with the list of translated files.
    # This is needed when a brand new file is translated.
    source_translated_files = [
        f for f in source_files if f.split(os.path.sep)[1] in translated_files
    ]
    source_translated_files.sort()

    with open(os.path.join(script_path, "sources.json"), "w") as f:
        data = {
            "source_folders": source_folders,
            "translated_docs": source_translated_files,
        }
        json.dump(data, f, indent=4, sort_keys=True)


if __name__ == "__main__":
    main()
