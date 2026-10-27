import json, os, re, threading, queue, time, random

BASE = "/mnt/c/Users/Admin/ThauraTest/notes-app-research/research-material/images/r12"
MANIFEST = os.path.join(BASE, "shot-manifest.jsonl")
LOG = os.path.join(BASE, "capture-log.jsonl")
WORKERS = 3
MAX_ATTEMPTS = 6

def slugify(s):
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return s[:40] or "app"

rows = []
with open(MANIFEST, encoding="utf-8") as f:
    for i, line in enumerate(f):
        r = json.loads(line)
        r["idx"] = i
        r["name"] = f"r12-{r['lane']}-{slugify(r['app'])}-{i:03d}.jpeg"
        rows.append(r)

def done_set():
    done = set()
    if os.path.exists(LOG):
        with open(LOG, encoding="utf-8") as f:
            for line in f:
                try:
                    e = json.loads(line)
                    if e.get("status", "").startswith("OK"):
                        done.add(e["idx"])
                except Exception:
                    pass
    return done

log_lock = threading.Lock()
logf = open(LOG, "a", encoding="utf-8")

def log(e):
    with log_lock:
        logf.write(json.dumps(e, ensure_ascii=False) + "\n")
        logf.flush()

def run_attempt(todo):
    """One browser pass. Returns True if the browser survived the attempt."""
    from camoufox.sync_api import Camoufox
    alive = {"ok": True}

    def worker(q):
        try:
            with Camoufox(headless=True) as b:
                p = b.new_page(viewport={"width": 1440, "height": 1000})
                p.set_default_timeout(35000)
                while True:
                    try:
                        r = q.get_nowait()
                    except queue.Empty:
                        return
                    try:
                        p.goto(r["url"], timeout=35000, wait_until="domcontentloaded")
                        p.wait_for_timeout(2500)
                        h = p.evaluate("document.documentElement.scrollHeight")
                        if h and h <= 15000:
                            p.screenshot(path=os.path.join(BASE, r["name"]), full_page=True, type="jpeg", quality=75)
                            mode = "full"
                        else:
                            p.screenshot(path=os.path.join(BASE, r["name"]), type="jpeg", quality=80)
                            mode = "viewport"
                        log({"idx": r["idx"], "name": r["name"], "url": r["url"], "status": f"OK {mode} h={h}"})
                    except Exception as ex:
                        err = f"{type(ex).__name__}: {ex}"[:200]
                        log({"idx": r["idx"], "name": r["name"], "url": r["url"], "status": f"FAIL {err}"})
                        if "TargetClosedError" in err or "browser has been closed" in err.lower():
                            alive["ok"] = False
                            return
                    q.task_done()
                    time.sleep(random.uniform(0.4, 1.2))
        except Exception:
            alive["ok"] = False

    q = queue.Queue()
    for r in todo:
        q.put(r)
    threads = [threading.Thread(target=worker, args=(q,), daemon=True) for _ in range(min(WORKERS, len(todo)))]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return alive["ok"]

for attempt in range(1, MAX_ATTEMPTS + 1):
    done = done_set()
    todo = [r for r in rows if r["idx"] not in done]
    print(f"attempt {attempt}: {len(todo)} remaining of {len(rows)}", flush=True)
    if not todo:
        break
    ok = run_attempt(todo)
    print(f"attempt {attempt} finished, browser alive: {ok}", flush=True)
    if not ok:
        time.sleep(5)

done = done_set()
print(f"DONE: {len(done)} of {len(rows)} captured", flush=True)
logf.close()
