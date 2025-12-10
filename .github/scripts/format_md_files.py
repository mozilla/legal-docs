#!/usr/bin/env python3
import sys
from pathlib import Path
import re


def normalize_file(path: Path) -> None:
    """
    Normalize a single Markdown file:
    - Remove UTF-8 BOM if present
    - Convert CRLF / CR to LF
    - Remove trailing blank lines and ensure exactly one final newline,
      while PRESERVING trailing spaces on non-blank lines.
    """
    original_text = None
    try:
        # Read with automatic BOM removal and Universal Newline conversion (CRLF/CR -> LF)
        with path.open("r", encoding="utf-8-sig", newline=None) as f:
            text = f.read()

        original_text = text
    except FileNotFoundError:
        print(f"Error: File not found {path}", file=sys.stderr)
        return
    except UnicodeDecodeError as e:
        print(f"Error decoding {path} (Skipping): {e}", file=sys.stderr)
        return
    except Exception as e:
        print(f"Error reading {path}: {e}", file=sys.stderr)
        return

    # Normalize trailing newline
    if not text:
        normalized_text = ""
    else:
        # Step A: Remove trailing blank lines and reduce to one final newline
        normalized_text = re.sub(r"(\s*\n)+$", "\n", text)

    # Check if any change occurred
    changed = normalized_text != original_text
    if changed:
        print(f"Normalized file ending: {path}")

    try:
        # Writing in text mode ensures UTF-8 encoding.
        # newline="" ensures Python doesn't convert LF back to CRLF.
        with path.open("w", encoding="utf-8", newline="") as f:
            f.write(normalized_text)
    except Exception as e:
        print(f"Error writing {path}: {e}", file=sys.stderr)


def main() -> None:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent.parent

    print(f"Scanning for .md files in: {repo_root}")

    for md_file in repo_root.rglob("*.md"):
        normalize_file(md_file)


if __name__ == "__main__":
    main()
