#!/usr/bin/env bash

set -euo pipefail

# Move to the root
cd "$(dirname "$0")/../.."

for f in $(find . -type f -name "*.md"); do
    # Remove BOM if present
    if [ "$(head -c3 "$f" | xxd -p)" = "efbbbf" ]; then
        tail -c +4 "$f" > "$f.tmp" && mv "$f.tmp" "$f"
        echo "Removed BOM from $f"
    fi
    
    # Normalize line endings to LF
    # Remove CR from CRLF line endings
    sed -i '' 's/\r$//' "$f"

    # Convert legacy CR-only files
    tr '\r' '\n' < "$f" > "$f.tmp" && mv "$f.tmp" "$f"
    
    # Normalize trailing newlines
    # Step 1: remove all trailing blank lines
    sed -i '' -e :a -e '/^\n*$/{$d;N;ba' -e '}' "$f"
    # Step 2: add exactly one ending newline
    printf '\n' >> "$f"
done
