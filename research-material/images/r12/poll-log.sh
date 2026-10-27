#!/bin/bash
cd /mnt/c/Users/Admin/ThauraTest/notes-app-research/research-material/images/r12
for i in 1 2 3 4 5 6 7 8 9; do
  n=$(wc -l capture-log.jsonl | awk '{print $1}')
  o=$(grep -c 'status.: .OK' capture-log.jsonl)
  echo "poll$i entries=$n ok=$o"
  sleep 60
done
echo final
wc -l capture-log.jsonl
grep -c 'status.: .OK' capture-log.jsonl
