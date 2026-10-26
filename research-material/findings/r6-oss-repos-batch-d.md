# R6 Findings — OSS Repos Batch D

Lane: full-depth research on five repo names (six repos, opensidian = two canon repos).
Canon URLs from `notesapp/links-inventory.txt`: DerKezorm/nexlore, cheeterdev/notes, jpzk/opensidian, thiagovasconcelosti/opensidian, realbynl/Meridian-Notes, shardulvs/xnotes-android. All six resolved and are live; none 404.
Context: pull-from assessment is for a Rust/Tauri local-first notes app. Rule: MIT/Apache/BSD = code pullable; GPL/AGPL = concepts only.

---

## 1. nexlore (DerKezorm/nexlore)

**URL:** https://github.com/DerKezorm/nexlore

### 1.1 What it is
A self-hosted, browser-based notes app: notes are plain Markdown files in a folder on the server, edited in the browser, with a WebGL graph view. Explicitly designed to be Obsidian-friendly — the files on disk stay the source of truth and Obsidian, Syncthing or any editor can work on the same vault at the same time. It is "one of the nex apps" (a small family of apps with a shared turquoise visual identity, per the README) (https://github.com/DerKezorm/nexlore). Positioned for "yourself or a small team" — it has multi-user spaces, accounts and permissions, which makes it a server app, not a local-first desktop app (https://github.com/DerKezorm/nexlore).

### 1.2 Author, stack, status
- Author: a single self-taught-style solo maintainer (the whole nex app family appears to be one person's work). No company, no contributor page visible.
- Stack: Python backend (venv + uvicorn + pytest in the dev docs; SQLite database `nexlore.db`), TypeScript/Vite frontend (npm ci, vite, vitest, Playwright e2e), Milkdown visual editor, WebGL graph rendering, Typst for server-side PDF typesetting, pdf.js for PDF viewing, Docker deployment via ghcr.io image (https://github.com/DerKezorm/nexlore).
- Status: extremely active. Releases march from v1.0 to v1.8.1 inside one month of October 2026: 1.0 (early Oct), 1.1.0 canvas (Oct 3), 1.2.0 graph (Oct 4), 1.3.0 backups (Oct 5), 1.4.0 Ask Lore RAG (Oct 5), 1.5.x PDFs (Oct 6–9), 1.6.x cookie hardening (Oct 11), 1.7.x task statuses (Oct 21–22), 1.8.1 (Oct 25) (https://github.com/DerKezorm/nexlore/releases/tag/v1.8.1, https://github.com/DerKezorm/nexlore/releases/tag/v1.1.0, https://github.com/DerKezorm/nexlore/releases/tag/v1.4.0).
- Community size: tiny but real. 5 stars, 0 forks as of the mid-October release pages (https://github.com/DerKezorm/nexlore/releases/tag/v1.5.1). The author filed a TrueNAS community-apps request and a PR to add nexlore to the TrueNAS community train (https://github.com/truenas/apps/issues/5983, https://github.com/truenas/apps/pull/5984) — a signal of ambition beyond the star count.

### 1.3 Full feature list (from README, https://github.com/DerKezorm/nexlore)
- Files-are-truth vault: every note is a Markdown file; file watcher plus full re-scan every 5 minutes; external edits picked up; conflicts become conflict copies (`Note (conflict 2026-09-28 101500).md`), never silent overwrite.
- Editor that keeps what it did not change: Milkdown visual editor with toolbar, `/` insert menu, Markdown shortcuts, block drag grips, front matter as a properties table; only touched blocks are written back, every other byte (including line endings) is preserved.
- Obsidian syntax compatibility: wiki links (`[[Note]]`, `[[Note#Heading|shown]]`), embeds (`![[Note#Heading]]`, `![[Note#^block]]` one level deep), callouts (foldable), highlights, `%%comments%%`, tags, front matter, tasks in Obsidian Tasks-plugin format; Dataview/Templater/Excalidraw plugin syntax left untouched as code; `.obsidian/` untouched.
- Link rewriting on rename/move, across spaces, in the original link style; large renames processed in batches, resumable after restart.
- WebGL graph with semantic zoom (folders are bubbles that open into notes), grouped by folder/tag/auto-derived topics, claimed smooth at 100,000 notes, layout computed server-side and loaded in tiles; local graph per note.
- Canvases in the open JSON Canvas format (`.canvas`), cards snap, note rename rewrites canvas paths, partial writes.
- Everyday: daily notes with calendar, templates (`{{date}}`, `{{title}}`), cross-space task overview (due/scheduled/recurring/done, custom statuses like `[r]`/`[a]` added in 1.7.0), installable as a phone web app (PWA), notes in tabs, split view, favorites, folder symbols/colors.
- Attachments next to notes, pasted images named after the note, GPS/location metadata stripped on upload (on by default), HEIC→WebP, content-hash dedup, PDF full-text indexing; SVG/HTML always downloaded, never rendered.
- Built-in PDF reader (pdf.js sandboxed, per-page links, `![[Manual.pdf#page=3&height=400]]` embeds, side-by-side reading).
- Print/PDF export of a note or whole folder via server-side Typst with page preview, also through the API.
- Spaces (top-level vault folders) with per-space member roles read/write/manage; cross-space links resolve only for people who can read both; unreadable content invisible everywhere including search/graph/backlinks/titles.
- Auth: passwords (Argon2id, 12+ chars), optional TOTP 2FA with recovery codes, multiple simultaneous OpenID Connect providers (authentik one-click card, Microsoft Entra ID incl. `common`/`organizations`), invitation links/mail, strict account linking rules, operator password re-confirmation for destructive admin actions.
- Public share pages with expiry and optional password, off until the operator enables.
- Versioning (bundled per session, thinned over time) and 30-day trash.
- Scheduled full backups (DB + files) with restore-diff check, download/upload for server migration.
- AI in notes (off by default, bring-your-own OpenAI-compatible endpoint): spellcheck, rewrite in 9 tones, translate, summarize, draft-from-note; result shown beside text, never auto-applied; 14-day verbatim log of what was sent. "Ask Lore": RAG over your own readable spaces with numbered per-statement sources, optional embedding model, optional tool-calling, encrypted conversations.
- MCP server exposure (off by default): whole UI surface as tools, OAuth or API keys, three permission levels, per-tool allow/ask/deny with in-app approval.
- Programmatic API (off by default): account tokens, read/write scopes, space limits, expiry; notes/tasks/search/links/dashboards; deliberately no delete/move/share verbs (https://github.com/DerKezorm/nexlore, docs/api.md).
- Sandboxed browser plugins from a curated catalog (contents/reading-time, queries, Kanban, rediscover-old-notes), operator-gated.
- ZIP import of an Obsidian vault or another nexlore space with a report; built-in onboarding guide space in English/German; i18n English + German, operator-uploadable JSON locales.
- Hardening documentation is unusually good: setup code from log on first boot, reverse-proxy/TLS guidance, trusted-proxy handling, per-sender rate braking, sandboxed plugin frames with no network, SSRF-safe outgoing requests (pinned resolution, no redirects, size caps), log never contains note contents or tokens (https://github.com/DerKezorm/nexlore).

### 1.4 What users like
There is essentially no public community yet — 5 stars, 0 forks, no Reddit/HN thread found. What exists is one engaged user team filing issues in October 2026 whose tone is emphatically positive ("Your apps hit our beach target right!" — issue #13), plus repeated feature requests, which is itself the compliment (https://github.com/DerKezorm/nexlore/issues/13). Also a TrueNAS community-app request/PR (https://github.com/truenas/apps/issues/5983). Beyond that: no feedback corpus. That is a real finding: nexlore is a very polished, very new app with effectively zero user base as of Oct 2026.

### 1.5 What is broken / requested
Issues are few but all get same-day/next-day fixes into releases, which is the notable part:
- #13 (Oct 6): no way to add a user's mail address after account creation; also asked about monetization and logo/title customization. Addressed by v1.5.1 ("Every account now has a mail address of its own") (https://github.com/DerKezorm/nexlore/issues/13, https://github.com/DerKezorm/nexlore/releases/tag/v1.5.1).
- #14 (Oct 21): feature request — filters on the Tasks view for custom statuses (`- [r]`, `- [a]`). v1.7.0 shipped custom task statuses and a status filter (https://github.com/DerKezorm/nexlore/issues/14, https://github.com/DerKezorm/nexlore/releases/tag/v1.7.0).
- #15 (Oct 22): bug — query block rejected `path: "Server/"` although the search page accepts it (Obsidian Desktop parity question). Fixed in v1.7.1 ("A query block now also takes a search, as the search page reads it, for example path:\`Server/\`") (https://github.com/DerKezorm/nexlore/issues/15, https://github.com/DerKezorm/nexlore/releases/tag/v1.7.1).
- No open issue backlog of substance; the repo is in a "maintainer ahead of users" state.

### 1.6 License
AGPL-3.0, stated in the README ("License: AGPL-3.0"), with third-party notices in THIRD-PARTY.md and Lucide icons ISC/MIT (https://github.com/DerKezorm/nexlore).

### 1.7 Pull-from assessment
AGPL-3.0 = concepts only; no code pull. But the concept haul is the best in this batch:
- The "editor writes back only what it touched, byte-identical elsewhere" invariant, plus conflict-copy files, is the single most liftable idea here for a Rust/Tauri local-first app that must coexist with Obsidian on one folder. The concept is fully described in the README and is implementable from scratch without touching nexlore code.
- Semantic-zoom WebGL graph (folders as bubbles that open), server-computed layout in tiles — concept portable to Rust/WGPU or a GPU canvas at any scale.
- JSON Canvas support, Obsidian Tasks-plugin task parsing, link rewriting on rename with batch/resume semantics — all concept-liftable specs of behavior.
- The API/MCP permission design (never-offer delete, per-token space scoping) is a good checklist regardless of stack.
- Code itself: Python+TS server architecture does not map to Tauri; nothing worth adapting line-by-line even if the license allowed. Worth noting the release cadence and issue hygiene as a benchmark for how a solo-maintained notes app should ship.

---

## 2. opensidian #1 — jpzk/opensidian

**URL:** https://github.com/jpzk/opensidian (website: https://opensidian.org/)

### 2.1 What it is
A privacy-first, open-source, vault-compatible cross-platform Markdown notes app: an explicit clean-room functional clone of Obsidian ("reimplements Obsidian's behaviour from the outside and contains none of its code"), non-profit, GPLv3. Runs Linux today; the README actively solicits Linux distribution maintainers (https://github.com/jpzk/opensidian). Opensidian (this one) is unaffiliated with Obsidian/Dynalist and says so.

### 2.2 Author, stack, status
- Author: jpzk (solo maintainer; AI-assisted — see 2.6).
- Stack: Rust + Tauri v2, no Electron; WebKitGTK 4.1 on Linux; ships a Nix flake pinning nixpkgs unstable; `cargo build --release --locked` in `src-tauri`; tests via `cargo test --locked` (https://github.com/jpzk/opensidian).
- Status: very active, young, Linux-first. Latest release v0.8.1 (README install table "Tested on fresh install 2026-10-25"); v0.8.0 Oct 23, 2026; v0.4 Oct 7 (https://github.com/jpzk/opensidian/releases/tag/v0.8.0, https://github.com/jpzk/opensidian/releases/tag/v0.4). Packaging is unusually complete for the age: slim and portable AppImage, Flatpak (GNOME 49 runtime), RPM, DEB, Nix; signed SHA256SUMS with a published PGP key (https://github.com/jpzk/opensidian).
- Community: 299 stars, 23 forks (https://github.com/jpzk/opensidian). Listed on AlternativeTo (https://alternativeto.net/software/opensidian/about/) and SaaSHub with Obsidian/Joplin/Logseq as top competitors (https://www.saashub.com/opensidian-alternatives). An unofficial experimental Windows fork exists (v0.8.0-windows.1, plain exe + WebView2) because upstream has no Windows release yet (https://github.com/Morglaf/opensidian/releases/tag/v0.8.0-windows.1).

### 2.3 Full feature list
From the README and site:
- Vault compatibility: opens Obsidian vaults; wikilinks, backlinks, graph view (https://github.com/jpzk/opensidian, https://opensidian.org/).
- Themes: most Obsidian community themes work unmodified; ships AnuPpuccin (default), Material Gruvbox, Minimal, Solarized; themes/snippets hot-reload; broken themes grey out with the reason instead of breaking the app (https://github.com/jpzk/opensidian).
- Community plugins: Obsidian's plugin ecosystem, off by default. Per-vault restricted mode whose flag lives in `~/.opensidian.json` outside the vault, so a vault cannot enable its own plugins; plugin browser with search/sort/README; installs only from GitHub over HTTPS with sha256 recorded; install ≠ enable; per-plugin no permission prompt (documented honestly as "plugins run code with your user's rights"). Top-10 plugins get behavioral e2e coverage (Calendar, Style Settings, Kanban, Advanced Tables, Copilot etc. — PR #5) (https://github.com/jpzk/opensidian, https://github.com/jpzk/opensidian/pull/5).
- Plugin secrets via the system Secret Service (gnome-keyring/KWallet/KeePassXC), never written to files; degrades to "unsupported" without a keyring (https://github.jpzk/opensidian — URL as listed above).
- Cross-platform posture: Linux today with distro packages; Windows only via unofficial fork (see 2.2).
- Build/test maturity: Cargo.lock-pinned builds, Nix dev shell, e2e plugin behavior tests, a cargo-fuzz target (see 2.5), documented known test failures on NixOS (hardcoded `/bin/true`, landlock sandbox limits) (https://github.com/jpzk/opensidian).

### 2.4 What users like
The Show HN thread (Oct 2026) is the main feedback corpus. Positive: a self-described long-time Obsidian user found the UI snappy and exciting and immediately asked about the plugin system (i.e., plugin parity is the make-or-break feature for this audience) (https://news.ycombinator.com/item?id=50070286). Neutral-to-negative but informative: a large part of the thread is a debate about AI-cloned software and whether an Obsidian clone has any right to exist ("I love open source. But Obsidian exists... cloning existing apps to open source is almost push-button in the age of Claude"), the copyright status of heavily AI-generated code, and one commenter noting they filter out projects on domains younger than 30 days (https://news.ycombinator.com/item?id=50070286). Counter-argument in-thread worth recording: markdown files alone are not freedom, because "the lock-in risk is the flow you get used to" — the strongest argument FOR this project's existence (https://news.ycombinator.com/item?id=50070286). No Reddit thread of substance found for this repo.

### 2.5 What is broken / requested
Issue tracker (14 issues, 2 PRs as of v0.8.0) is mostly maintainer-self-filed quality work, which says the community is too new to file bugs:
- #22 (Oct 25): datefmt integer overflow/panic on out-of-range date over IPC, found by the new cargo-fuzz target — panics in debug, silently wraps in release (https://github.com/jpzk/opensidian/issues/22).
- #23 (Oct 25): "pixelated graphs" bug, self-filed with `bug` label (https://github.com/jpzk/opensidian/issues/23).
- #8 (Oct 23): closing all tabs should close the pane (https://github.com/jpzk/opensidian/issues/8).
- #14 (Oct 23): cosmetic, "in the intro dialog, x looks weird" (https://github.com/jpzk/opensidian/issues/14).
- Requested implicitly by users: Windows/macOS builds (third-party fork exists, above), plugin completeness (HN question) (https://github.com/Morglaf/opensidian/releases/tag/v0.8.0-windows.1, https://news.ycombinator.com/item?id=50070286).

### 2.6 AI disclosure (important for quality assessment)
The README has an explicit "AI disclosure" section: "opensidian was built predominantly with AI models. Nearly all of the code, the design docs, and this README were written by Claude ... working from prompts, reviews, and corrections by a single human maintainer"; commit messages record design rationale in the same way. The HN thread litigated exactly this (https://github.com/jpzk/opensidian, https://news.ycombinator.com/item?id=50070286). Unverified: actual code quality/robustness beyond the test/fuzz evidence.

### 2.7 License
GPL-3.0-or-later, per README "Licence: GPL-3.0-or-later (LICENSE). Read THIRD-PARTY.md before redistributing." (https://github.com/jpzk/opensidian).

### 2.8 Pull-from assessment
GPL-3.0 = concepts only. But this is the most architecturally relevant repo in the batch for a Rust/Tauri local-first notes app — it is literally Rust + Tauri v2 + Obsidian vault compatibility, which is close to the target project's own spec:
- Concept-level: restricted-mode plugin design (trust flag outside the vault, sha256-on-install, install≠enable), theme hot-reload with graceful broken-theme fallback, Obsidian link-resolution order (same-folder first, then shortest path — documented in nexlore too), WebKitGTK packaging choices and Nix flake structure.
- Code: not pullable. If the target project ever went GPL it would be the single best starting point in this batch; under a permissive license, only its behavioral specs can be reused.
- Quality: the fuzzing + e2e plugin tests suggest above-average process discipline for an AI-written solo project, but that is inference from process artifacts, not from reading the code — unverified.

---

## 3. opensidian #2 — thiagovasconcelosti/opensidian

**URL:** https://github.com/thiagovasconcelosti/opensidian

### 3.1 What it is (disambiguation)
A completely different project sharing the name: a self-hosted, server-based knowledge-management system in Node.js/TypeScript — REST API + React web frontend, Dockerized, with an MCP server and npm package `opensidian-mcp`. It is a web app you run on a server ("Open: http://localhost:3000"), not a desktop app (https://github.com/thiagovasconcelosti/opensidian/blob/main/README.md).
Disambiguation finding: "opensidian" is a badly polluted name. At least five other projects use it: EpicenterHQ/epicenter's apps/opensidian (local-first browser notes with CRDT-backed virtual filesystem, POSIX shell, Yjs sync, AGPL-3.0, at opensidian.com) (https://github.com/EpicenterHQ/epicenter/tree/main/apps/opensidian, https://news.ycombinator.com/item?id=47676461, https://runany.dev/blog/opensidian-local-first-notes/); markusbegerow/opensidian (Tauri 2 + React + Rust offline desktop notes with local AI chat) (https://github.com/markusbegerow/opensidian); markusbegerow/nextcloud-opensidian (Nextcloud app) (https://github.com/markusbegerow/nextcloud-opensidian); kinghaonan/opensidian (an Obsidian plugin, unrelated) (https://github.com/kinghaopnan/opensidian — URL as found: https://github.com/kinghaonan/opensidian). Only the two canon repos (jpzk, thiagovasconcelosti) were researched in full; the others are recorded here as disambiguation only. opensidian.org belongs to jpzk; opensidian.com belongs to EpicenterHQ.

### 3.2 Author, stack, status
- Author: a solo developer whose other repos (AiShot screenshot tool, deepseek-harness ports) show an AI-heavy, ship-fast pattern; AiShot shows 0 stars, so this author has no audience anywhere (https://github.com/thiagovasconcelosti/AiShot).
- Stack (README table): Node.js 20+, TypeScript, Express backend; React 18 + Vite + React Router frontend; D3.js force graph; marked + front-matter for Markdown; ws WebSocket sync; @modelcontextprotocol/sdk for MCP; Vitest, 79 tests, >80% coverage; GitHub Actions CI on Windows/Mac/Linux; Docker multi-stage (https://github.com/thiagovasconcelosti/opensidian/blob/main/README.md).
- Status: declared v1.0 complete (all 7 phases) and v2.0 full-text search complete (TF-IDF indexer, search API with tag/date/backlink filters and highlighting, advanced search UI) (https://github.com/thiagovasconcelosti/opensidian/blob/main/README.md). Stars, last-commit date, release history: not visible in any fetched/searched page — **unverified**; the repo is live (its README and the inventory's opengraph capture exist) but its community metrics could not be confirmed. No release tags surfaced in search; **unverified whether any exist**.

### 3.3 Full feature list (from README, https://github.com/thiagovasconcelosti/opensidian/blob/main/README.md)
- Vaults: multiple note vaults managed by the server.
- Markdown editor: live preview with `[[wikilink]]` support.
- Knowledge graph: interactive D3.js force-simulation visualization; REST endpoints for full graph and per-note neighborhoods.
- Sync: real-time note sync over WebSocket.
- Auth: JWT login with persistent sessions (register/login/me/logout endpoints).
- Themes: light/dark plus custom themes via a visual theme editor, saved/loaded/deleted over REST.
- Plugins: plugin API with `onLoad(ctx)`, command registration, hooks `note:pre-save` and `note:post-save`, access to vault manager and graph engine; sample plugin included; loaded from `./plugins/` with restart.
- MCP server: stdio server exposing vault_list/vault_open/vault_create, note_create/read/update/delete/search, graph_get/graph_neighbors; runnable via `npx opensidian-mcp` (published npm package) with a documented Claude Desktop config.
- REST API: full notes CRUD, per-vault, full-text search with ranking plus tag/date/hasBacklinks filters, graph endpoints, themes endpoints (full route tables in README).
- Search: TF-IDF full-text with stopwords and persistence (v2.0 milestone).
- Docker: compose file, port 3000 API/web + 3001 (WebSocket), `./vaults` volume.
- Tests: 79 unit tests, coverage >80%.
- No mobile/desktop clients; it is browser-only against a server.

### 3.4 What users like
No community exists: no stars figure found, no issues, no Reddit/HN/AlternativeTo presence for this specific repo. Plainly stated: zero observable user feedback. That is a real finding (https://github.com/thiagovasconcelosti/opensidian/blob/main/README.md and absence of any search results).

### 3.5 What is broken / requested
No issue data found. Unverified either way; nothing public to record. The README's own milestones are all checked complete, but that is the author's self-report.

### 3.6 License
MIT — README badge "License: MIT" and "License: MIT. See LICENSE." (https://github.com/thiagovasconcelosti/opensidian/blob/main/README.md).

### 3.7 Pull-from assessment
MIT = code pullable, and this is the only repo in the batch that is both permissively licensed AND documents an AI-tool integration surface (MCP + plugin hooks + REST). Honest assessment:
- Worth lifting as code: the MCP server module (src/mcp) — a small, isolated stdio server over @modelcontextprotocol/sdk with a clean tool surface (note CRUD + search + graph); porting that tool surface to Rust (e.g. over a Tauri command bridge) is a contained, well-scoped lift. The REST route shape and the two-hook plugin model (`note:pre-save`/`note:post-save`) are simple enough to be specs, not code.
- Not worth lifting as code: the Express server, React web UI, WebSocket sync and D3 graph — they implement a server-centric architecture opposite to a local-first Tauri app; a Tauri app would replace nearly all of it. The 79 tests test that server, not anything reusable.
- Quality caution: single-author AI-generated code with no community review ever applied; treat anything pulled as a starting sketch requiring full re-review. Concepts (MCP tool naming, search-filter parameters, plugin hook points) are freely liftable under MIT and are the main value here.

---

## 4. cheeterdev/notes (Cheeter Notes)

**URL:** https://github.com/cheeterdev/notes

### 4.1 What it is
A Tauri-based Markdown notes desktop app, marketed as "Just Notes, Nothing else" and "the Notes App which does not need a tutorial first." The README is two sentences plus a preview image (https://github.com/cheeterdev/notes). The author announced it on Reddit r/tauri as "Made a Notes App using HTML, CSS and JS in Tauri" linking to the releases page (https://www.reddit.com/r/tauri/best/ — the listing page surfaced the post; the post itself is dated in the listing context).

### 4.2 Author, stack, status
- Stack: Tauri with an HTML/CSS/JS frontend (per the author's own Reddit framing) (https://www.reddit.com/r/tauri/best/).
- Status: essentially a stub repository. The working tree contains only README.md and image.webp; 5 commits total; no visible source code in the repo's file listing (https://github.com/cheeterdev/notes). One release: "1.0 Preview", a pre-release tagged `Preview`, created with GitHub's verified signature, released Oct 6 with 3 assets (asset names did not render on the fetched page; presumably installers) (https://github.com/cheeterdev/notes/releases/tag/Preview).
- Stars/forks/issues: not visible in any fetched page; no issue data found. **Unverified.**

### 4.3 Full feature list
There is none: the README describes only the concept line ("Cheeter Notes is the Notes App which does not need a tutorial first") and an app-preview image. No feature list, no docs, no architecture notes (https://github.com/cheeterdev/notes). Any feature inventory would be guesswork; none recorded.

### 4.4 What users like
No feedback exists. The r/tauri post is the only public trace found; no comment content surfaced in search. Plainly stated: no community, no reviews, no evidence anyone uses it (https://www.reddit.com/r/tauri/best/).

### 4.5 What is broken / requested
No issues found; the repo has no visible issue activity. Nothing to record.

### 4.6 License
No license visible anywhere on the repo page or in search results (other repos in this batch showed a license badge in the About/resources section; this one showed none). **Unverified**: a LICENSE file could exist in git history, but nothing indicates one. As it stands: all-rights-reserved by default; nothing in the repo is legally reusable.

### 4.7 Pull-from assessment
Nothing to pull. No source code in the repo, no license, one signed pre-release binary of unknown contents. The only liftable thing is the positioning concept — "a notes app that needs no tutorial" — which is a marketing idea, not a technical one. Record as: dead end for code, possible competitor-at-large to keep on a watch list if it matures.

---

## 5. Meridian-Notes (realbynl/Meridian-Notes, binary "Meridian")

**URL:** https://github.com/realbynl/Meridian-Notes

### 5.1 What it is
A native (non-web) Markdown note editor written in pure Rust that draws its own window — no web technologies, no Electron/Tauri, no terminal: a custom CPU-painted widget toolkit. Notes are plain Markdown files on disk. Version 0.2, with an enormous feature surface described in the README (https://github.com/realbynl/Meridian-Notes).

### 5.2 Author, stack, status
- Author: solo (realbynl). 16 commits, 3 stars, 1 fork (https://github.com/realbynl/Meridian-Notes via search snapshot).
- Stack: pure Rust workspace, CPU-painted rendering. Layout: `crates/gui` (window binary), `crates/app` (editor app library), `crates/ui` / `crates/term` / `crates/buffer` (widget toolkit, cell-grid editor, text buffer), plus design docs (skins, ui-toolkit, endless, graph, perf) and BACKLOG.md (https://github.com/realbynl/Meridian-Notes).
- Status: pre-alpha test builds. Release v0.2.0-test1, built by CI (github-actions) on Oct 24, 2026, explicitly labeled "early, unsigned, and may crash, lose data, or change without notice. Keep backups"; Windows and macOS builds noted as much less tested than Linux (https://github.com/realbynl/Meridian-Notes/releases/tag/v0.2.0-test1).

### 5.3 Full feature list (from README, https://github.com/realbynl/Meridian-Notes)
- Editing: rope-based buffer, undo/redo, multiple cursors, select next/all occurrences, line move; word wrap, line numbers, minimap, sticky scroll, code folding, permanent+temporary bookmarks; find/replace, find-in-files with an editable results document, regex builder; split views (columns/rows), tabs; macros (record/play/save), pipe-selection-through-command; spell check, lint, git gutter, syntax highlighting, diff vs saved file, time-travel history scrubber; Vim mode, typewriter scrolling, focus mode (paragraph/sentence), pomodoro timer, word statistics/frequency; encodings UTF-8/UTF-16/Latin-1 and LF/CRLF/CR.
- Notes: `[[links]]`, `{{embeds}}` (scrollable, collapsible), backlinks sidebar, hover preview; inline images + image viewer; heading-size rendering; goto-anything (files/lines/symbols), file tree, notebooks/sections/pages; templates and New-file menu; remote folders with sync.
- Views: Endless canvas (notes as free-positioned text boxes via a layout file); graph view of linked notes (`meridian --graph`); table and data-tree side views; pen ink (Wayland stylus) on canvas and in notes, saved as SVG; touch support (tap, drag-scroll, long-press select, pinch zoom).
- Study: Anki-like cloze cards (`{{c1::text}}`), card review, quizzes, recall and Feynman panels, reading queue, exam forecast, Anki import/export (TSV, APKG), study statistics, leech list, speed reader.
- Look: "skins" theming where every color is a role, gradients, PNG tiling/nine-slice, ornaments, custom fonts, hot reload, contrast guard; custom-drawn title bar/ribbon/menus/command palette; editable radial menu; layouts; 50–400% zoom. Every hotkey rebinding in `keys.conf`; `settings.conf`.
- Extensibility: out-of-process plugins on a stable protocol (panels, commands, key bindings).
- Full default hotkey tables are in the README (files/tabs, editing, moving, search, bookmarks/folding, panels/views/modes).

### 5.4 What users like
No community: 3 stars, 1 fork, 16 commits, no issues/threads found anywhere. Plainly stated: zero user feedback; the project is younger than its README. (https://github.com/realbynl/Meridian-Notes via search snapshot.)

### 5.5 What is broken / requested
No issues found; no public bug reports. The release page itself is the only "what's broken" record: everything is flagged as possibly data-losing test builds (https://github.com/realbynl/Meridian-Notes/releases/tag/v0.2.0-test1). The README's BACKLOG.md ("wanted features not yet planned") exists but its contents were not retrievable — unverified.

### 5.6 License
MIT — the repo's resources section shows "MIT license" (https://github.com/realbynl/Meridian-Notes via search snapshot; the README itself just says "See LICENSE").

### 5.7 Pull-from assessment
MIT = code pullable, and this is the batch's most technically interesting pure-Rust codebase for a Tauri/Rust notes app — but also the most overextended:
- Genuinely pullable, plausibly valuable: `crates/buffer` (rope buffer with multi-cursor) and `crates/ui` (a custom CPU-painted widget toolkit with skins) are self-contained Rust crates licensed MIT; they could be vendored or mined directly, which no other repo in this batch offers (everything else is Python/TS/Android).
- Concept-liftable: the skins system (colors as roles, contrast guard), out-of-process plugin protocol, Endless-canvas-as-layout-file, SVG ink storage, time-travel history scrubber, find-in-files-with-editable-results.
- Honest quality assessment: the README advertises a decade of editor features (Vim mode, macros, APKG Anki sync, exam forecast, speed reader, pen ink) on 16 commits with unsigned data-losing builds. That profile usually means the feature list is aspirational and the crates are uneven; treat `crates/buffer`/`crates/ui` as reference code to read and mine, not as dependencies to trust. Verify by reading the actual crate code before any pull decision — unverified beyond repo structure.

---

## 6. xnotes-android (shardulvs/xnotes-android, app "xnotes")

**URL:** https://github.com/shardulvs/xnotes-android (F-Droid: https://f-droid.org/en/packages/com.xnotes/)

### 6.1 What it is
A handwriting-first note-taking, sketching and PDF-annotation app for Android, built for stylus users. Open source, no account, no ads, no tracking, no internet access; notes saved as files in a user-chosen folder (https://github.com/shardulvs/xnotes-android/blob/master/README.md). This is the only repo in the batch with a real user community.

### 6.2 Author, stack, status
- Author: solo (shardulvs). 269 stars, 33 forks (https://github.com/shardulvs/xnotes-android via search snapshot).
- Stack: Kotlin + Jetpack Compose + Material 3, with NDK 27 + CMake (native code, presumably the ink engine); JDK 17; build via Gradle (https://github.com/shardulvs/xnotes-android via search snapshot, https://github.com/ismailGl/xnotes-android mirror README).
- Distribution: GitHub Releases (signed APK), F-Droid (built reproducibly from source), Google Play — GitHub and F-Droid ship the same signed APK (https://github.com/shardulvs/xnotes-android/blob/master/README.md).
- Status: very active. Release stream through late October 2026: v0.8.16→0.8.23 (crash fixes, tables, markdown shortcuts, multi-PDF import), v0.9.0 (PDFium rendering, PDF text selection/copy, markup tool, searchable notes, selectable-text export), v0.9.3 (note covers, AI-designed templates, open `xtemplate` format spun out to its own repo), v0.9.4 (horizontal page mode, Lenovo Tab Pen Plus button, Honor/TCL ink fixes) (https://github.com/shardulvs/xnotes-android/releases/tag/v0.8.23, .../v0.8.20, .../v0.9.0, .../v0.9.3, .../v0.9.4 — URLs as returned by search).

### 6.3 Full feature list (from README, https://github.com/shardulvs/xnotes-android/blob/master/README.md)
- Ink engine: pressure-sensitive low-latency ink (custom stroke engine turning raw stylus samples into a variable-width ribbon that swells/tapers with pressure); pens and highlighters; neon glow on any pen; disappearing ink (fades on its own, for teaching/presenting); shape snapping (draw rough, hold, snaps clean); crisp at any zoom.
- Structure: notebooks and infinite canvas; book layouts (single/double/cover pages, scrolling or page flips); page templates (20+: Cornell, planners, music staves, isometric); note covers (own pictures, or an AI can design a template); always editable — strokes stored as editable vectors in the open `.xnote` format (a zip with JSON; the format is documented in the separate shardulvs/xtemplate repo), never flattened.
- PDF: import and annotate any PDF; PDFium rendering; selectable/copyable PDF text; markup tool (highlight/underline/strike/squiggle with comments); side-note margins on any edge; color filters (invert/sepia/contrast/brightness/multiply/screen) that leave embedded photos untouched; searchable; mixed page sizes; real PDF export (vector, selectable text, links, bookmarks).
- Typed content: Markdown formatted as you type (headings/lists/tasks/quotes/code/emphasis shortcuts, `/` quick menu); tables with insert/restyle/resize; LaTeX equations; code highlighting.
- Audio recording synced to ink playback (lecture capture).
- UI: rearrangeable/floatable/dockable/resizable toolbar; split view (two notes); dark and OLED modes; endless themes (any accent × 8 styles, dual tone, Material You); real file explorer (grid/gallery/list/column/timeline), pinned folders, trash/restore, recent files.
- Platform: Android 8+; S Pen and generic stylus support incl. button events; no network permission; notes as files in a user folder.

### 6.4 What users like
Real, plentiful feedback. On r/fossdroid the author's launch post got engagement and a visible reply "Always been a huge fan of Xournal++ and was waiting for something" (i.e., positioned as the Android Xournal++) (https://www.reddit.com/r/fossdroid/comments/1u0bu53/xnotes_a_handwritingfirst_note_taking_app/). Users recommend it organically: in r/GalaxyTab as "free and open source, very similar to Samsung notes, even better for my taste" (https://www.reddit.com/r/GalaxyTab/comments/1t56cbb/any_good_alternatives_for_samsung_notes_free_or/), in r/NoteTaking alongside StarNote/Flexcil (https://www.reddit.com/r/NoteTaking/comments/1vxxn0b/good_handwriting_app_for_windows_and_android/). MakeUseOf covered it (Sep 2026) as a free Samsung Notes alternative, noting it is clearly built for pen users first (https://www.makeuseof.com/had-no-idea-samsung-notes-had-free-alternative-this-good/). Community forks exist that customize it (e.g. a fork adding handwriting-to-text conversion) — a sign people care enough to maintain their own versions (https://github.com/NeDDy3z/n-notes).

### 6.5 What is broken / requested (103 open issues; selected, https://github.com/shardulvs/xnotes-android/issues)
- Top requests: note encryption (#348), handwriting search (#341), note inside note (#331), sync/ synchronization (#315), grouping elements (#323), pin notes to sidebar (#318), straight-line tool (#324), timer (#328), side-by-side view (#297), save pages as new notes (#308), eraser erase-all-strokes (#298), progressive blur (#304), palm-rejection area tuning, lasso tool inconsistencies (#175), latency on some devices (#171).
- Bugs: stylus hover events unprocessed cause canvas pan (#335, 6 reactions), stylus button function not working on some devices (#316, 8 reactions), selection outline invisible in dark/OLED on light background (#325), split-screen issues (#320, 9 reactions), canvas theme selection bug (#294), closing keyboard closes search dialog (#342).
- Pattern: the community is stylus-hardware-conscious (device-specific ink/button bugs) and privacy-conscious (encryption and sync are the loudest requests, and sync is deliberately absent because the app has no internet). That is directly relevant intel for any local-first notes project: users of a no-network app immediately ask for optional sync and encryption.

### 6.6 License
MIT (https://github.com/shardulvs/xnotes-android via search snapshot: "Resources Readme MIT license"; README build section is compatible).

### 6.7 Pull-from assessment
MIT = code pullable; platform mismatch is the real barrier:
- Not directly pullable into a Rust/Tauri app: it is Android/Kotlin/Compose with an NDK/CMake native layer. A Tauri desktop app cannot run this code.
- Worth mining anyway: the ink-engine design (raw stylus samples → pressure-variable ribbon stroke, low latency, crisp at any zoom) is a set of algorithms that would live in native/Rust code on desktop too; if the native layer is C/C++, individual geometry pieces could port. The open `.xnote` format (zip + JSON, editable vectors, never flattened) and its `xtemplate` sibling are documented, MIT-licensed data-format specs — liftable as-is for interoperability thinking. The disappearing-ink and shape-snap concepts are feature ideas, trivially describable, legally free.
- Honest bottom line: pull concepts, data formats, and possibly stroke-geometry algorithms; do not plan on pulling code wholesale. Also pull the product lesson: file-based storage, no accounts, reproducible F-Droid builds, and same-signed-APK across channels built this project its community.

---

## Cross-batch summary for the Rust/Tauri local-first project

- Code pullable and plausibly useful: Meridian-Notes (MIT, pure Rust: buffer + custom UI toolkit), thiagovasconcelosti/opensidian (MIT, but only the MCP server / plugin-hook surface is worth carrying; the rest is server architecture). Everything else: concepts only (nexlore AGPL, jpzk opensidian GPL) or nothing (cheeterdev: no code, no license).
- Best concept source: nexlore (byte-preserving partial write-back + conflict copies + Obsidian coexistence), jpzk/opensidian (restricted-mode plugin trust model, it is the same Rust+Tauri architecture), xnotes (ink engine + open file format + the no-network/encryption/sync demand pattern).
- Name pollution: any write-up must distinguish jpzk/opensidian (Rust/Tauri, GPLv3, opensidian.org) from thiagovasconcelosti/opensidian (Node server, MIT) from EpicenterHQ's opensidian (CRDT browser app, AGPL, opensidian.com) from markusbegerow/opensidian (Tauri/React/Rust) — four-plus distinct projects share the name.
- Honesty notes: thiagovasconcelosti/opensidian community metrics unverified; cheeterdev/notes stars/license unverified; Meridian-Notes BACKLOG.md contents unverified; all "quality" judgments on jpzk and thiagovasconcelosti code rest on process evidence (tests/fuzz/coverage claims), not on code reading.
