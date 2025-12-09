#!/usr/bin/env bash

set -euo pipefail

# Move to the root
cd "$(dirname "$0")/../.."

for f in $(find . -type f -name "*.md"); do
    # Remove BOM if present
    if [ "$(head -c3 "$f" | xxd -p)" = "efbbbf" ]; then
        tail -c +4 "$f" > "$f.tmp" && mv "$f.tmp" "$f"
        echo "Removed BOM: $f"
    fi
    
    # Normalize line endings to LF if necessary
    lineinfo=$(file "$f")

    if [[ "$lineinfo" == *"CRLF"* ]]; then
        # Convert CRLF -> LF
        sed -i '' 's/\r$//' "$f"
        echo "Converted CRLF to LF: $f"
    elif [[ "$lineinfo" == *"CR line terminators"* ]]; then
        # Convert CR -> LF
        tr '\r' '\n' < "$f" > "$f.tmp" && mv "$f.tmp" "$f"
        echo "Converted CR to LF: $f"
    fi    
    
    # Ensure single trailing newline. Using awf since sed behaves 
    # differently on macOS and Linux.
    awk 'NF { last = NR } { lines[NR] = $0 } END {
        for (i = 1; i <= last; i++) print lines[i]
    }' "$f" > "$f.tmp" && mv "$f.tmp" "$f"
    echo "Normalized trailing newline: $f"
done
