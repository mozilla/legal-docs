import shutil
import sys
from pathlib import Path


def split_files(files):
    """Convert a CSV string to a list of strings"""
    return [f.strip() for f in files.split(",")]


def copy_files(filename, dest):
    dest_path = Path(dest)
    src_path = Path(".")
    if filename == "ALL":
        file_paths = src_path.glob(f"*/*.md")
    else:
        file_paths = src_path.glob(f"*/{filename}")

    for fp in file_paths:
        dest_locale_dir = dest_path.joinpath(fp.parent)
        dest_locale_dir.mkdir(exist_ok=True)
        shutil.copy(fp, dest_locale_dir)
        print(fp)


def main(files, dest):
    files_list = split_files(files)
    for fn in files_list:
        copy_files(fn, dest)


if __name__ == "__main__":
    main(*sys.argv[1:])