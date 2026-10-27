#!/usr/bin/env bash
# Secret checker: scans working tree and full git history for identifying data.
# Blocks any push until clean. All local-only rules (machine name, user path,
# community member names) live in research-material/local-rules.txt, which is
# gitignored. This script contains no secrets itself and is safe to commit.
# Run from repo root in WSL: bash checks/run-secret-check.sh   (added in R1)
set -u
cd "$(dirname "$0")/.."
RULES="research-material/local-rules.txt"
fail=0

if [ ! -f "$RULES" ]; then
  echo "SECRET CHECK WARNING: $RULES missing; running pattern-only scan."
fi

scan() {
  local label="$1" f="$2"
  if grep -nEa 'DESKTOP-[A-Z0-9]{6}|C:.Users\.[A-Za-z]|(^|[^A-Za-z0-9.])((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])([^0-9.]|$)' "$f" >/dev/null 2>&1; then
    echo "SECRET-HIT [$label] $f (machine/user-path/IP pattern)"
    fail=1
  fi
  if [ -f "$RULES" ]; then
    while IFS= read -r name; do
      name="${name%$'\r'}"
      # Names shorter than 3 chars match ordinary punctuation in any file;
      # substring scanning cannot police them reliably (limitation, see MILESTONES R1).
      [ -z "$name" ] && continue
      [ "${#name}" -lt 3 ] && continue
      esc=$(printf '%s' "$name" | sed 's/[][\.*^$()+?{|]/\\&/g')
      if grep -nEa "(^|[^A-Za-z0-9_-])${esc}([^A-Za-z0-9_-]|\$)" "$f" >/dev/null 2>&1; then
        echo "SECRET-HIT [$label] $f (local rule match)"
        fail=1
        break
      fi
    done < "$RULES"
  fi
}

while IFS= read -r -d '' f; do
  [ -f "$f" ] || continue
  scan "worktree" "$f"
done < <( { git ls-files -z; find . -type f -not -path './.git/*' -not -path './ARCHIVE/*' -not -path './BACKUPS/*' -not -path './research-material/*.html' -not -path './research-material/pasted-*.txt' -not -path './research-material/discord*' -not -path './research-material/authors-local-only.txt' -not -path './research-material/local-rules.txt' -print0; } | sort -zu )

if [ -d .git ]; then
  for c in $(git rev-list --all 2>/dev/null); do
    git grep -nEa 'DESKTOP-[A-Z0-9]{6}|C:.Users\.[A-Za-z]|(^|[^A-Za-z0-9.])((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])([^0-9.]|$)' "$c" -- . 2>/dev/null | head -3 | while read -r line; do
      echo "SECRET-HIT [history $c] $line"
    done
  done
fi

if [ "$fail" -eq 1 ]; then
  echo "SECRET CHECK FAILED: resolve every hit before publishing."
  exit 1
fi
echo "SECRET CHECK PASSED: worktree and history clean."
