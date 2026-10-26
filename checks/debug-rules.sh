#!/usr/bin/env bash
# Debug helper: prints which local rule matches a given file. Added R1.
# Usage: bash checks/debug-rules.sh <file>
cd "$(dirname "$0")/.."
f="${1:?usage: debug-rules.sh <file>}"
while IFS= read -r name; do
  name="${name%$'\r'}"
  [ -z "$name" ] && continue
  esc=$(printf '%s' "$name" | sed 's/[][\.*^$()+?{|]/\\&/g')
  m=$(grep -nEa "(^|[^A-Za-z0-9_-])${esc}([^A-Za-z0-9_-]|\$)" "$f" 2>/dev/null | head -2)
  if [ -n "$m" ]; then
    echo "RULE '[${name:0:3}...len${#name}]' matches:"
    echo "  $m"
  fi
done < research-material/local-rules.txt
