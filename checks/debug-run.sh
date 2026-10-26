#!/usr/bin/env bash
# debug-run.sh: show which local rules match the findings files (gitignored helper)
cd "$(dirname "$0")/.." || exit 1
for f in research-material/findings/community-digest.md \
         research-material/findings/github-repos-1.md \
         research-material/findings/github-repos-2.md \
         research-material/findings/linked-apps-1.md \
         research-material/findings/linked-apps-2.md \
         research-material/findings/thread-a-sync.md \
         research-material/findings/thread-b-storage.md; do
  echo "== $f"
  bash checks/debug-rules.sh "$f" | head -12
done
