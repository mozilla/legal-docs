import shutil
import sys
from pathlib import Path


def split_files(files):
    """Convert a CSV string to a list of strings"""
    return [f.strip() for f in files.split(",")]


def copy_files(filename, dest):
    """Copy all language versions of `filename` to `dest`

    Copy includes language folder.
    """
    dest_path = Path(dest)
    src_path = Path(".")
    num_files = 0
    if filename == "ALL":
        extensions = [".md", ".pdf"]
        file_paths = [p for p in src_path.rglob("*/*") if p.suffix in extensions]
    else:
        file_paths = src_path.glob(f"*/{filename}")

    for fp in file_paths:
        dest_locale_dir = dest_path.joinpath(fp.parent)
        dest_locale_dir.mkdir(exist_ok=True)
        shutil.copy(fp, dest_locale_dir)
        print(fp)
        num_files += 1

    return num_files


def main(files, dest):
    num_files = 0
    files_list = split_files(files)
    if "ALL" in files_list and len(files_list) > 1:
        # No need for any other action
        files_list = ["ALL"]

    for fn in files_list:
        num_copied = copy_files(fn, dest)
        num_files += num_copied
        if num_copied == 0:
            # If any of the search terms returns nothing throw an error
            return f"No files found matching {fn}"

    print(f"Successfully copied {num_files} files")
    return 0  # Success


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
