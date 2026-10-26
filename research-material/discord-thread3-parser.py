import re, json, html

SRC = "/mnt/user-data/uploads/ArtCraft - ✨・app-requests - Notion -  a productivity and note-taking application [1559185243280244787].html"
OUT_JSON = "/home/thaura/notesapp/discord-thread3-parsed.json"
OUT_TXT = "/home/thaura/notesapp/discord-thread3-transcript.txt"
OUT_LINKS = "/home/thaura/notesapp/discord-thread3-links.txt"

with open(SRC, encoding="utf-8") as f:
    src = f.read()

# Container attributes are unquoted in this export: class=chatlog__message-container data-message-id=<digits>
parts = re.split(r'class=chatlog__message-container\s+data-message-id=', src)[1:]

def strip_tags(s):
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s)
    s = re.sub(r'[ \t]+', ' ', s)
    s = re.sub(r'\n{2,}', '\n', s)
    return s.strip()

def grab(chunk, attr):
    # href=... or title=..., quoted or unquoted
    m = re.search(attr + r'="([^"]*)"', chunk) or re.search(attr + r'=([^ >]+)', chunk)
    return m.group(1) if m else ""

messages = []
links = set()
for p in parts:
    mid = re.match(r'(\d+)', p).group(1)
    # message body: div class=chatlog__content chatlog__markdown (older exports used chatlog__message-content)
    m = (re.search(r'class="?chatlog__content chatlog__markdown"?(.*?)(?=class="?chatlog__reactions|class="?chatlog__divider|class="?chatlog__embeds|$)', p, re.S)
         or re.search(r'class="?chatlog__message-content"?(.*?)(?=class="?chatlog__message-reactions|class="?chatlog__divider|class="?chatlog__reference-symbol|$)', p, re.S))
    body = m.group(1) if m else ""
    body = re.split(r'<div[\s>]', body)[0]  # drop trailing container-remnant markup
    body = strip_tags(body).lstrip("> \n").strip()
    author = ""
    m = re.search(r'class="?chatlog__author"?(.*?)</', p, re.S)
    if m:
        author = strip_tags(m.group(1))
    ts = grab(p, "title")
    if not ts:
        m = re.search(r'class="?chatlog__timestamp"?(.*?)</', p, re.S)
        ts = strip_tags(m.group(1)) if m else ""
    for href in re.findall(r'href="(.*?)"', p) + re.findall(r'href=([^ >]+)', p):
        links.add(href)
    messages.append({"id": mid, "author": author, "timestamp": ts, "content": body})

with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(messages, f, ensure_ascii=False, indent=1)

with open(OUT_TXT, "w", encoding="utf-8") as f:
    for msg in messages:
        f.write(f"[{msg['id']}] {msg['author']} ({msg['timestamp']}):\n{msg['content']}\n\n")

with open(OUT_LINKS, "w", encoding="utf-8") as f:
    for l in sorted(links):
        f.write(l + "\n")

print(f"messages: {len(messages)}")
print(f"unique links: {len(links)}")
nonempty = sum(1 for m in messages if m["content"])
print(f"nonempty bodies: {nonempty}")
