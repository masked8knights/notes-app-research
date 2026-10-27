cd /mnt/c/Users/Admin/ThauraTest/notes-app-research/research-material/images/r12
head -3 capture-log.jsonl
grep -o '"status": "[A-Za-z]*' capture-log.jsonl | sort | uniq -c
ls *.jpeg 2>/dev/null | head -3
