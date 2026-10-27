# R12 image capture notes (2026-10-27)

Captured with headless camoufox (Firefox-based anti-detection browser) in WSL, 3 workers, 1440x1000 viewport, full-page screenshot when page height is 15000px or less, otherwise viewport-only. JPEG quality 75 (full page) or 80 (viewport).

- shot-manifest.jsonl: 486 records parsed from the seven lane files' SHOT-LIST blocks and visual-surface sections (lane, app, caption, url).
- r12-capture.py: first capture run; r12-capture2.py: resilient rerun that restarts the browser when it dies and retries failures (needed: the first run lost the browser partway and lost 260 shots).
- capture-log.jsonl: full history including retries (keep: it is the provenance record; early FAIL entries are superseded by later OK entries for the same idx).
- Files: r12-{lane}-{app-slug}-{idx}.jpeg, idx matches the manifest line number.

Result: 481 of 486 captured. The 5 misses are unreachable URLs, not scraper failures:

| idx | url | reason |
|-----|-----|--------|
| 46 | https://www.styluslabs.com/write/ | SEC_ERROR_UNKNOWN_ISSUER (site TLS cert not trusted) |
| 47 | https://www.styluslabs.com/write/Help.html | SEC_ERROR_UNKNOWN_ISSUER (same cert) |
| 102 | https://www.linktly.com/productivity-software/evernote-review/ | Timeout 35s exceeded (site unresponsive) |
| 381 | http://localhost:3000: | Malformed URL recorded in a lane shot-list (localhost reference, not reachable from this machine) |
| 444 | http://127.0.0.1:8766/docs | Connection refused (local dev server, not running) |

Helper scripts poll-log.sh and find-missing.sh are scratch tooling from the capture session and can be removed at any time.
