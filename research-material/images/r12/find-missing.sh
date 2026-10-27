#!/bin/bash
cd /mnt/c/Users/Admin/ThauraTest/notes-app-research/research-material/images/r12
python3 - <<'EOF'
import json
done = set()
fails = {}
for line in open("capture-log.jsonl", encoding="utf-8"):
    e = json.loads(line)
    if e["status"].startswith("OK"):
        done.add(e["idx"])
    else:
        fails[e["idx"]] = e
missing = [fails[i] for i in sorted(fails) if i not in done]
print("missing:", len(missing))
for e in missing:
    print(e["idx"], e["url"], "|", e["status"][:120])
EOF
