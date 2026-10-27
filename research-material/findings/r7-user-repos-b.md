# R7 — Round B: five user-supplied repos researched in depth

Subagent: r7-user-repos-b. Date of research session: 2026-10-27.
Method: shallow git clones of all five repos (primary source: repo contents at HEAD), GitHub web pages fetched for stars/releases/issues, web search for community reception, primary-site fetches where available. Every claim carries a URL. Anything not directly captured is marked **UNVERIFIED this session**.

Repo HEAD snapshots cloned this session: zappynotes @ commit 2025-12-30, owlistic @ 2025-06-01, NexaNote @ 2026-10-08, memos @ 2026-10-26, siyuan @ 2026-10-19 (cloned from the main branches 2026-10-27; clone paths /tmp/repos/*).

---

## 1. zapatify/zappynotes

### 1.1 Identity
- A Rails-based web notes app, self-described as "an open-source note-taking app built with Rails 8 and Hotwire." https://github.com/zapatify/zappynotes/blob/main/README.md (raw: https://raw.githubusercontent.com/zapatify/zappynotes/main/README.md)
- License: MIT, exact file text reads "MIT License, Copyright (c) 2025-present ZappyNotes". https://raw.githubusercontent.com/zapatify/zappynotes/main/LICENSE
- Stack: Ruby on Rails 8 (Hotwire/Importmap asset pipeline), PostgreSQL per README "PostgreSQL" prerequisite list; models: User, Notebook, Note, Session, Subscription (note belongs_to notebook; notebook belongs_to user; user has_many notebooks/sessions). Verified in source: https://github.com/zapatify/zappynotes/tree/main/app/models
- Editor is Toast UI Editor, vendored at app/javascript/editor/toastui (README architecture section + directory listing). https://github.com/zapatify/zappynotes/tree/main/app/javascript
- Health: tiny/early. Repo page scrape showed stargazerCount 0 and small size; README says "This project is currently on hiatus. If you'd like to pick it up, reach out." Last commit 2025-12-30, message "Convert to open source project" (so the repo is public since end of 2025). Releases page lists exactly one release, v1.0.0. https://github.com/zapatify/zappynotes/releases — the 0-star figure is from a rendered-page scrape and could undercount a very recently published repo; treat star count as near-zero, **UNVERIFIED this session** (exact current count).
- Issue tracker: effectively unused; no issue titles surfaced on https://github.com/zapatify/zappynotes/issues (page scrape). Community reception: none found — no Reddit/HN threads discovered via search this session. Plainly stated: there is no public sentiment to analyze.

### 1.2 Storage model
- Data lives in PostgreSQL (server-side web app; notes are DB rows under a user → notebook → note hierarchy). https://github.com/zapatify/zappynotes (README prerequisites and models).
- No plain-file or E2EE story found in the repo this session; storage/ attachment dir exists at repo root (/storage) but no sync architecture — it is a single-server web app with no client sync to sync. **UNVERIFIED this session**: what /storage holds at runtime.
- Auth: session-based (app/models/session.rb, user has_many sessions), Stripe-gated subscription model (app/models/subscription.rb + README "Paid plans" section listing Free/Pro/team tiers with Stripe checkout). https://github.com/zapatify/zappynotes/tree/main/app/models

### 1.3 Features (from README + requirements doc)
The feature surface is small; documented features per README and ZappyNotes_Requirements.md at repo root (https://raw.githubusercontent.com/zapatify/zappynotes/main/ZappyNotes_Requirements.md):
- Notebooks containing notes; note CRUD through a WYSIWYG editor (Toast UI). 
- Full-text note search (README feature list).
- Markdown support via the Toast UI editor's markdown mode.
- AI features: README mentions AI-suggested note titles / summaries behind an OpenAI integration (README "AI" section). Implementations live in app/jobs and config; **UNVERIFIED this session**: exact AI capabilities beyond the README claim.
- Paid plans via Stripe with Free/Pro tiers (README). 
- Import/export: none documented; no import/export code surfaced in controllers this session. **UNVERIFIED this session**: none found = none existing.
- No handwriting, audio, templates, backlinks, tags, publishing, or mobile apps are documented anywhere in the repo. Plainly: this is a small early web app.

### 1.4 UX evidence
- No GitHub issue traffic, no Reddit/HN threads found (searched "zappynotes" web-wide this session). No sentiment exists; stated plainly.

### 1.5 Pull-from assessment
- Very little. The only pattern worth noting for our Rust/local-first project is the negative space: a 2025 Rails+Stripe note app with E2EE absent, sync absent, and the author already on hiatus confirms server-app note products remain a weak pattern for local-first. Its models (notebook→note hierarchy, session-based auth) are generic. Verdict: nothing to lift beyond "do not follow this model."

---

## 2. owlistic-notes/owlistic

### 2.1 Identity
- Self-described in README as "a next-generation open-source note-taking app" with "butterfly-structured notebooks" — a Flutter client + Go backend design. The project owner's link (with #screenshots anchor) resolves to the README of this repo. https://github.com/owlistic-notes/owlistic#screenshots
- License: GNU General Public License v3.0 (GPLv3), full standard text, no modifications. https://raw.githubusercontent.com/owlistic-notes/owlistic/main/LICENSE
- Stack (verified from source manifests): backend Go (gin v1.10, gorm v1.25 with postgres runtime driver and sqlite driver for tests, gorilla/websocket, golang-jwt v5, nats.go v1.42 — NATS JetStream for realtime event streaming). https://raw.githubusercontent.com/owlistic-notes/owlistic/main/src/backend/go.mod ; frontend Flutter/Dart with an MVP architecture documented in src/frontend/docs/architecture.md. https://github.com/owlistic-notes/owlistic/blob/main/src/frontend/docs/architecture.md
- Health: small and slowing. Repo page scrape: 431 stars. Last commit 2025-06-01 ("Update changelog"); latest release v0.2.0. https://github.com/owlistic-notes/owlistic/releases — i.e. ~17 months quiet at time of research. Small release history (v0.1.0 → v0.2.0 only on the releases page).
- Data model in source: notebooks, notes, blocks, tasks (src/backend/internal/models; MVP providers in Flutter). https://github.com/owlistic-notes/owlistic/tree/main/src/backend
- Security posture: JWT auth with per-request user scoping; broker publishes user-scoped events (src/backend/broker/producer.go, JWT claims parsed in handler). No E2EE anywhere in source this session. **UNVERIFIED this session**: none (confirmed absent from source).

### 2.2 Storage model
- Backend stores data via GORM in PostgreSQL (runtime driver) with a SQLite driver used for tests. https://raw.githubusercontent.com/owlistic-notes/owlistic/main/src/backend/go.mod
- Realtime sync is server-mediated: Go backend holds a NATS JetStream event bus; clients connect over WebSocket; broker/producer.go publishes user-scoped note events. So sync = server + websocket push, not P2P, not E2EE. Conflict handling: not documented; last-write-wins implied by event timestamps in the models; **UNVERIFIED this session** (no explicit conflict-resolution code found in src/backend).
- Deployment: docker-compose.yaml at repo root + setup.sh (README deployment section). https://github.com/owlistic-notes/owlistic#deployment — self-hostable, but the stack is heavy for a notes app: Go server + NATS + Postgres + broker.

### 2.3 Features
Feature surface is small; enumerated from README, frontend source, and docs this session:
- Notebooks with butterfly-diagram-inspired structure (README).
- Note CRUD with nested note blocks and tasks inside notes (README + models: Note, Block, Task).
- Real-time multi-device sync over WebSocket (README "Real-Time Sync" section). 
- Full-text search across notes (README).
- Note versions — README lists "Note Versions" as a feature. **UNVERIFIED this session**: how versions are stored/diffed (no dedicated versioning module surfaced in src/backend this session).
- Frontend extras from src/frontend/lib: focus mode, themes, tag and category management, keyboard shortcuts, onboarding, security screen (frontend/ui dirs: features/focus_mode, features/security, features/keyboard_shortcuts, features/onboarding). https://github.com/owlistic-notes/owlistic/tree/main/src/frontend/lib
- No AI, no handwriting, no audio, no plugin marketplace, no publishing documented. Import/export: none found. Plainly: early-stage feature set despite a polished marketing README.

### 2.4 UX evidence
- Issue tracker: sparse; no high-traffic recurring complaints surfaced on https://github.com/owlistic-notes/owlistic/issues (page scrape, few issues total). No Reddit/HN threads found via search this session ("owlistic notes" web-wide). No meaningful public sentiment exists; stated plainly.

### 2.5 Pull-from assessment
- The interesting engineering choice is real-time sync as an event stream (NATS JetStream + WebSocket with user-scoped events) — a clean pattern for multi-device push, but it is server-centric and not local-first; not worth lifting for our stack. The Flutter MVP/provider layering is conventional. The "butterfly" notebook concept is a naming flourish, not implemented as distinct graph logic in the models reviewed. Verdict: little to lift; the architecture doc (https://github.com/owlistic-notes/owlistic/blob/main/src/frontend/docs/architecture.md) is a decent small-scale example of documenting an MVP layout.

---

## 3. TheZupZup/NexaNote

### 3.1 Identity
- A local-first handwriting-capable note app: Flutter app + Python FastAPI backend, explicitly "inspired by Obsidian-style plain markdown vaults" (README: "plain markdown files" and docs/obsidian-inspired-vault-roadmap.md). https://github.com/TheZupZup/NexaNote/blob/main/README.md
- License: Mozilla Public License 2.0 (MPL-2.0), standard text with Exhibit A. https://raw.githubusercontent.com/TheZupZup/NexaNote/main/LICENSE
- Stack: Flutter (app/), Python FastAPI (nexanote/), SQLite storage layer, WsgiDAV WebDAV server embedded, pytest suite ("64 passed" per project docs). https://github.com/TheZupZup/NexaNote/tree/main/nexanote
- Health: very young but active at time of research. Repo page scrape: 9 stars. Last commit 2026-10-08; releases v1.0.0 through v1.1.3 on the releases page. https://github.com/TheZupZup/NexaNote/releases
- The project's own docs/ISSUES_CURRENT_STATE.md is unusually honest and gives a code-grounded reality snapshot: fully implemented = FastAPI routes (notebooks/notes/page text/ink/sync trigger/stats/storage), SQLite CRUD for notebooks/notes/pages/strokes, WebDAV server + sync client/engine, conflict-resolution module with tests, Flutter notebook sidebar/list/editor/ink canvas with pen/highlighter/eraser, pressure, undo, clear, zoom; partially implemented = sync settings split across SharedPreferences and backend disk config, data-dir switching only after restart, single-page editor UI despite multi-page data model, search on every keypress with no debounce; missing = Docker packaging, PDF export, OCR, E2EE, mature Android release workflow. https://github.com/TheZupZup/NexaNote/blob/main/docs/ISSUES_CURRENT_STATE.md
- README declares AI features; the issues doc does not list AI under "fully implemented," so AI claims are at least partially aspirational. **UNVERIFIED this session**: which AI features actually run.

### 3.2 Storage model
- Local-first: notes and ink strokes live in SQLite via the backend; text notes additionally live as plain markdown files in a user-visible data directory (README "Your notes are plain markdown files" + storage routes). https://github.com/TheZupZup/NexaNote#readme
- Handwriting is first-class data: strokes are stored as structured ink JSON ({id,color,width,tool,points} with per-point pressure; ink_json.dart converts wire ink to a Stroke model and back, tolerant of malformed strokes). https://github.com/TheZupZup/NexaNote/blob/main/app/lib/services/ink_json.dart
- Sync: WebDAV. Two modes in one backend: the backend runs an embedded WebDAV server (WsgiDAV provider), and the app's sync engine syncs via WebDAV to any NAS/Nextcloud-style endpoint; URL can be an override or derived from the API URL by appending /webdav (single base URL behind a reverse proxy serves both API and WebDAV). https://github.com/TheZupZup/NexaNote/blob/main/app/lib/services/app_state.dart and docs/docker.md. There is a dedicated conflict-resolution module with automated tests (ISSUES_CURRENT_STATE.md, above). No E2EE (explicitly listed as missing). No P2P.
- Self-host story: FastAPI backend + WsgiDAV in one process; docs/docker.md exists but Docker packaging is listed as not yet productized. https://github.com/TheZupZup/NexaNote/blob/main/docs/docker.md

### 3.3 Features
- Editor: page-based model (notebook → note → pages) where a page holds text (markdown) plus an ink layer; UI currently edits page 1 only (ISSUES_CURRENT_STATE.md).
- Handwriting: ink canvas with pen/highlighter/eraser, pressure sensitivity, undo/clear/zoom (ISSUES_CURRENT_STATE.md + ink_json.dart). This is the most directly relevant feature of all five repos to our handwriting requirement.
- Sync: WebDAV engine with trigger/status API endpoints (/sync/trigger, /sync/status) (api_client.dart) and a tested conflict-resolution module (ISSUES_CURRENT_STATE.md).
- Search: full-text over notes; known defect: runs on every keypress without debounce/cancel (ISSUES_CURRENT_STATE.md).
- Diagnostics: connection_diagnostics.dart, storage info + stats API routes (ISSUES_CURRENT_STATE.md).
- Organization: notebooks/lists; no tags, backlinks, templates, or daily notes found in source this session.
- Import/export: none yet (PDF export listed as missing). OCR: missing. Audio: none. AI: claimed in README, unverified. Plugins: none.
- Platforms: Flutter desktop/mobile layouts exist; Android release workflow immature (ISSUES_CURRENT_STATE.md). Exact platform availability **UNVERIFIED this session** beyond "desktop/mobile layouts in code."

### 3.4 UX evidence
- The repo's own docs/ISSUES_CURRENT_STATE.md doubles as the issue tracker narrative (linked above): sync settings UX confusion, no debounced search, swallowed errors (catch (_) {}), single-page editor. That is the best available UX evidence and it is self-reported.
- Community: 9 stars; no Reddit/HN threads found via search this session. No external sentiment exists; stated plainly.

### 3.5 Pull-from assessment
- Highest pull value of the three small repos, precisely because it shares our target shape (local-first, handwriting, self-host sync) at small scale:
  1. The ink data model: strokes as structured JSON with per-point pressure and tool/color/width metadata, tolerant decoding, and text page + ink layer in one page object (https://github.com/TheZupZup/NexaNote/blob/main/app/lib/services/ink_json.dart). This is a good minimal baseline for our Rust ink format; we would extend it (vector rasterization caching, palm rejection metadata) rather than start from scratch.
  2. The "backend derives sync URL from API URL" pattern (app_state.dart) is a neat single-origin self-host UX.
  3. The tested conflict-resolution module is evidence that WebDAV conflict handling can be written compactly and tested; worth reviewing code before designing ours (https://github.com/TheZupZup/NexaNote/tree/main/nexanote).
  4. Its ISSUES_CURRENT_STATE.md discipline (README claims vs code reality) is a practice worth copying for our own docs.
- What not to copy: the Python/SQLite single-writer backend as architecture (fine for prototype, weak for a Rust local-first core), and the non-debounced search.

---

## 4. usememos/memos

### 4.1 Identity
- Self-described as "an open-source, self-hosted memo hub with knowledge management and socialization," widely known as "a lightweight, open-source alternative to flomo." https://github.com/usememos/memos/blob/main/README.md
- License: MIT — exact current LICENSE text: "MIT License, Copyright (c) 2025 Memos". https://raw.githubusercontent.com/usememos/memos/main/LICENSE
- License history check (per task note): the LICENSE file's own commit history (GitHub atom feed for LICENSE) shows the file existing since 2021-12-14 with subsequent commits 2022-03-06, 2022-06-19, and 2025-02-11 — the 2025 commit updates the copyright line to "Memos" (the project earlier had the author's personal copyright). https://github.com/usememos/memos/commits/main/LICENSE — so the file has been MIT throughout its tracked history; no relicensing is visible in the LICENSE file this session. Community discussion of licensing/direction exists (Section 4.4). Any claim that memos "changed license" beyond the copyright-year update is **UNVERIFIED this session**.
- Stack: Go backend (521 .go files at HEAD) + React/TypeScript web frontend (Vite-style src under web/src), served as a single binary; API is protobuf/ConnectRPC-based (proto/ directory; web client uses connect.ts). Docker-first distribution (README docker run example; image migrated to docker.io/neosmemo/memos per README). https://github.com/usememos/memos
- Health: very popular and very active. Repo page scrape: 64,098 stars. Last commit 2026-10-26 (one day before this session). Releases: stable line v0.31.0 and a calendar-versioned 26.10.0-rc.2 (project moved to calendar versioning in 2026). https://github.com/usememos/memos/releases
- Organizational note: README states the project is developed under a company structure (usememos enterprise, "Memos is built with ❤️ by the Memos team", sponsorship section; the website usememos.com presents the team/company). The transition from solo project to company-run is the context for the "feature direction" complaints in 4.4. **UNVERIFIED this session**: exact corporate entity name.

### 4.2 Storage model
- Server-based, local-first only in spirit: memos is a single Go binary serving a web UI; data lives server-side in SQLite by default, with MySQL and PostgreSQL supported as store drivers (store/db/ contains sqlite, mysql, postgres implementations; README states SQLite default with MySQL/PostgreSQL options). https://github.com/usememos/memos/tree/main/store/db and README "Database" section.
- Attachments/object storage: provider/storage supports S3-compatible object storage for attachments (provider/storage dir at HEAD: s3.go etc.). https://github.com/usememos/memos/tree/main/provider/storage
- Sync architecture: none. Memos has no client-side sync engine; multi-device access is through the server. Recurring user requests for offline-first sync exist (Issue "Offline Notes" in the tracker: https://github.com/usememos/memos/issues). Conflict handling: N/A (no sync) — single source of truth is the server DB. No E2EE anywhere in source this session (confirmed absent; encryption-at-rest not provided either).
- Self-host story: excellent and simple — one binary or one Docker container, SQLite file in a mounted volume; the canonical r/selfhosted "easy deploy" app. README quickstart: docker run -d --name memos -p 5230:5230 -v ~/.memos/:/var/opt/memos docker.io/neosmemo/memos:stable. https://github.com/usememos/memos#docker

### 4.3 Features
Enumerated from README, source tree, issue tracker, and the project site this session:
- Memo-first creation: quick capture, like flomo; memos support markdown, tasks/todo items, and "ask AI" menu in the composer (web/src/components, README screenshots).
- Organization: tags (inline #tags in memo text), pinned memos, "memo visibility" (private/protected/public — public memos are shareable pages), resources/attachments. README feature list + web/src pages (web/src/pages: MemoDetail, MemosView, TagListView? enumerated at https://github.com/usememos/memos/tree/main/web/src/pages).
- Collections: README "Collections" — curated pinned groups of memos; Explore page for public memos on an instance (socialization aspect).
- Calendar view and a Map view (web/src/pages: Calendar, Map) — geo-tagged memos.
- Archive + weekly/monthly review ("MemoViews" page — daily/weekly review of past memos). https://github.com/usememos/memos/tree/main/web/src/pages
- Multiple databases/namespaces: recent releases added multi-workspace "Spaces" (Issue "Spaces — Collaborative workspaces" open; feature present in web UI this session). https://github.com/usememos/memos/issues
- AI: speech-to-text transcription built in via a provider abstraction (provider/ai/stt with an OpenAI provider, user-supplied API key; stt.go). Issue "AI Integration" requests expanding AI into note-taking features. https://github.com/usememos/memos/tree/main/provider/ai
- Identity providers: SSO/OIDC via provider/idp (open.go), OAuth sign-in. https://github.com/usememos/memos/tree/main/provider/idp
- Export: markdown export per memo and bulk memo export (core/memoexport.go). Import: markdown import exists (README/import docs); full-fidelity import from other apps is limited. **UNVERIFIED this session**: exact import matrix.
- Search: server-side full-text search across memo content (kernel search in store; no FTS5 details verified — **UNVERIFIED this session**: underlying search engine). Issues request semantic/AI search (Issue "Semantic Search / AI Search Support", open).
- Plugins/extensions: none; the React app is monolithic, no plugin system. Publishing: public visibility per memo acts as lightweight publishing. Handwriting: none. Audio recording: none (transcription is for uploaded audio files).
- Platforms: web UI (responsive/PWA-ish) is the only official client; third-party iOS/Android/terminal clients exist in the community (README links to usememos clients page — https://www.usememos.com/). **UNVERIFIED this session**: current state of third-party clients.
- Pricing/business: the app is fully open source, MIT, with no paid tiers in the repo; monetization is sponsorship/commercial support (README "Sponsorship"). No paid cloud found on usememos.com this session; the site markets the open product. **UNVERIFIED this session**: whether a hosted paid offering exists anywhere.

### 4.4 UX evidence
- GitHub issues (fetched 2026-10-27): recurring open feature requests — full AI integration, drawing/canvas support, semantic search, focus mode, "Spaces — Collaborative workspaces," offline notes. https://github.com/usememos/memos/issues (issue titles scraped this session: "AI Integration", "Semantic Search / AI Search Support", "Spaces — Collaborative workspaces", "Drawing/Canvas Support for Memos", "Focus Mode", "Feature Request: Rich Text Editor Enhancements…").
- Reddit r/selfhosted reception (searched this session): https://www.reddit.com/r/selfhosted/comments/1g8ugt3/what_do_you_use_for_notetaking_memos/ — comments call it easy to deploy and fast, but several users describe it as too simple once you want hierarchy, and note sync-across-devices is just the server. https://www.reddit.com/r/selfhosted/comments/1p6u2fd/looking_for_a_selfhosted_memo_andor_flomo/ — users compare it against flomo and note memos as the closest self-hosted equivalent. https://www.reddit.com/r/selfhosted/comments/1l88t3c/whats_the_deal_with_memos/ — a thread dedicated to mixed feelings: praise for the lightweight capture, criticism of recent direction ("feature creep toward enterprise"), and the v0.22-era API/UI rewrites breaking third-party clients; several users mention the project's team/maintainer changes as a source of uncertainty. Reception summary: loved for single-binary simplicity and speed; criticized for a flat data model, no offline/E2EE sync, and a history of churn (including the v0.22 protobuf/Connect rewrite and rewrites of the web UI) that broke third-party tooling.
- **UNVERIFIED this session**: exact vote/comment counts on those threads (titles and gist captured from search results).

### 4.5 Pull-from assessment
- Lift: the single-binary self-host story (one Go binary, SQLite default, docker run from README) is the benchmark our deployment story must at least match; memos proves the market rewards trivial self-hosting.
- Lift: provider abstraction for AI (provider/ai/stt interface with swappable providers, user-supplied keys) — the right shape for E2EE-local-first too: user-owned keys, pluggable engines.
- Lift: per-memo visibility model (private/protected/public) is a simple, well-understood sharing ladder.
- Do not lift: server-side-only storage with no sync engine (exactly what our project is built to fix), the ConnectRPC/proto API churn that broke clients, and the enterprise-direction drift the community complains about.

---

## 5. siyuan-note/siyuan

### 5.1 Identity
- SiYuan (思源笔记) is a mature, privacy-first, self-hosted-capable personal knowledge management (PKM) system: block-based editor, Notion-like databases ("attribute views"), plugins, flashcards, and its own sync stack, developed by a two-person Chinese company (brother-sister team 88250 and Vanessa219, per HN community research into the company behind it). https://github.com/siyuan-note/siyuan/blob/main/README.md and https://news.ycombinator.com/item?id=42512713
- License: AGPL-3.0 (GNU Affero General Public License v3.0), full standard text, no appended modifications in the current file. https://raw.githubusercontent.com/siyuan-note/siyuan/main/LICENSE
- Licensing history (per task note): earlier versions of the project carried additional restrictions beyond AGPL (README sections on "Use restrictions" and the FAQ's "Is SiYuan completely open source?" preamble date from that era); the current README instead states the project is "completely open source" and the LICENSE file contains only the unmodified AGPL text this session. The community discussed this history during the December 2024 HN thread: the notable observed behavior is that paid feature license checks live inside the AGPL codebase itself, which anyone can patch out under AGPL (HN thread, 2024-12: "this one including license checking code is entirely under AGPL… one can patch out the license check"). https://news.ycombinator.com/item?id=42512713 . Community forks exist: https://github.com/siyuan-community/siyuan (experimental community builds) and https://github.com/EightDoor/siyuan (paid-feature-removed patch), both named in the HN thread. **UNVERIFIED this session**: exact dates and wording of the historical license-text changes (I verified the current state and the community's account of it, not each historical revision).
- Architecture: Go "kernel" (kernel/ — 2025 .go files at HEAD: data repo, sync, search, model, av, mcp, ocr, bazaar, plugin, cli, agent dirs) + Electron shell (app/ — app/package.json names "SiYuan" v3.8.8, main ./electron/main.js, with an electron install script; the Electron process drives the kernel). The web UI is TypeScript in app/src. https://github.com/siyuan-note/siyuan/tree/main/kernel and https://github.com/siyuan-note/siyuan/blob/main/app/package.json
- Health: 46,947 stars (repo page scrape); last commit 2026-10-19; releases run to v3.8.9-beta.2 with stable v3.8.8 (app/changelogs/v3.8.8.md documents 100+ changes in one release: AI agent flows, database features, editor fixes). Active, not archived. https://github.com/siyuan-note/siyuan/releases and https://github.com/siyuan-note/siyuan/blob/main/app/changelogs/v3.8.8.md
- Platforms (README download links): Windows, macOS (Intel + Apple Silicon), Linux (deb/AppImage/AUR), Android (APK + app stores), iOS (App Store), plus a server/Docker self-host mode with browser access. https://github.com/siyuan-note/siyuan#download

### 5.2 Storage model
- Custom block-JSON-over-files format: each document is a .sy file (JSON containing the block tree) under a workspace notebook directory (verified: treenode code requires .sy suffix — kernel/mcp/tools/document.go builds paths as "<id>.sy"; kernel/filesys/tree.go walks them). https://github.com/siyuan-note/siyuan/tree/main/kernel/filesys
- Assets (images, PDFs) live in an assets/ folder next to notebooks; full-text search indexes are SQLite FTS5 databases (verified by search test filenames: search_custom_fts5_test.go, search_mindmap_fts5_test.go, search_case_replace_fts5_test.go; also search_sql_comments_test.go). Encrypted notebooks use SQLCipher (search_concurrent_replace_sqlcipher_test.go) with per-box DEK handling (comment in kernel/model/file.go: ".sy 解密失败（DEK 未缓存或 box 未解锁）" = .sy decryption failure when DEK not cached or box locked). https://github.com/siyuan-note/siyuan/tree/main/kernel/model
- Sync stack (the deep part): built on the project's own snapshot library github.com/siyuan-note/dejavu (imports at kernel/model/repository.go:50-52 — dejavu, dejavu/cloud, dejavu/entity). The local "data warehouse/repo" keeps content-addressed snapshots of every file; snapshot listing parses titles in snapshots (parseTitleInSnapshot at kernel/model/repository.go:675). Sync providers are enumerated in kernel/model/sync_service.go: official SiYuan Cloud, S3, WebDAV, and Local (directory); sync runs incremental snapshots against the chosen provider (kernel/model/sync*.go is a large family: sync.go, sync_auto_pause.go, sync_dedup.go, sync_ignore.go, sync_pending.go, sync_probe.go, sync_path.go, sync_error.go, with validation tests sync_provider_validation_test.go and sync_s3_validation_test.go). https://github.com/siyuan-note/siyuan/tree/main/kernel/model
- E2EE: the data repo is encrypted with a repo key derived from a user passphrase (kernel/model/repository.go: InitRepoKeyFromPassphrase, ImportRepoKey, InitRepoKey — lines 1167-1347). Snapshots synced to S3/WebDAV/official cloud are encrypted with this key; the README FAQ says data synced to the official cloud is end-to-end encrypted and the cloud cannot read it (README "Data sync" FAQ: "encrypted with the repo key"). https://github.com/siyuan-note/siyuan/blob/main/README.md and https://github.com/siyuan-note/siyuan/blob/main/kernel/model/repository.go
- Conflict handling: snapshot-based — each device commits snapshots and sync merges through the dejavu repo with automatic conflict resolution; the official FAQ describes it as "merge snapshots, automatic conflict handling." README FAQ. A recurring real-world failure mode is WebDAV provider quirks: open issues include "WebDAV sync failure: ETag mismatch / lock file" and sync-stall complaints ("Sync stalls and keeps displaying Connecting") — https://github.com/siyuan-note/siyuan/issues (titles scraped this session). 
- Self-host: the kernel runs as a server (Docker image in README) serving the full UI in a browser; that same server can act as the sync node for other devices. README "Server/Docker deployment." Paid gating applies to which sync providers work without a membership (5.5).

### 5.3 Features
- Editor: block-based WYSIWYG markdown — content is block trees (paragraphs, headings, lists, tables, code, formulas, embeds, superblocks) serialized as JSON into .sy; markdown written to disk at the block level. The editor model is "block model vs markdown" answered as: blocks are primary; markdown is the serialization and export/import dialect. README + kernel/filesys.
- Organization: notebooks → documents → blocks; bidirectional links and backlinks; block references ((block-ref syntax) and embed blocks; tags (inline and doc-level); daily notes (templates + daily-note workflow); bookmarks; graph view; templates (built-in and user-defined with SQL queries in templates). README feature list.
- Attribute view / database (Notion-like): kernel/av implements "attribute views" — tables/boards with typed columns (text, number, date, select, multi-select, mSelect, checkbox, URL, email, phone, template, created/updated), row = block, filter/sort, rollups (kernel/av dir with capabilities in kernel/av/capabilities.go: type KeyCapability). Attribute views are searchable (kernel/model/search_attribute_view.go). https://github.com/siyuan-note/siyuan/tree/main/kernel/av
- Search: SQLite FTS5-backed full-text search over all block types with a query syntax (keywords with #tag, block-type filters, sub-string vs whole-word modes; engine in kernel/model/search.go with ~25 search test files at HEAD). https://github.com/siyuan-note/siyuan/tree/main/kernel/model
- AI: OpenAI-compatible cloud AI for writing assistance (kernel/model/ai.go imports github.com/sashabaranov/go-openai); v3.8.8 changelog added agent flows ("AI 写作" agents, MCP-based AI tools). There is also a built-in MCP server (kernel/mcp with server.go and tools/ for asset, attr, bazaar, document, export operations) — SiYuan exposes itself as an MCP server for external AI agents, a distinctive 2026-era feature. https://github.com/siyuan-note/siyuan/tree/main/kernel/mcp and https://github.com/siyuan-note/siyuan/blob/main/app/changelogs/v3.8.8.md
- Flashcards/spaced repetition: built-in review (kernel/api/riff.go; kernel/model/flashcard.go) using the FSRS/smithsot-like "riff" deck format; README documents flashcard review from any block. https://github.com/siyuan-note/siyuan/blob/main/kernel/api/riff.go
- Attachments/media: images, video, audio in assets/; PDF annotation (asset annotation links); web/HTML clippings; OCR over assets via bundled Tesseract (kernel/ocr dir); OCR indexing of image text (kernel/ocr). https://github.com/siyuan-note/siyuan/tree/main/kernel/ocr
- Handwriting/ink: none in the desktop app (no ink engine in kernel or app/src this session); the community requests it — open issue "手写支持 Handwriting support" in the tracker. https://github.com/siyuan-note/siyuan/issues (title scraped this session). Mobile platforms get stylus-as-input only via OS-level text input; no palm-rejection ink layer. **UNVERIFIED this session**: whether any third-party plugin adds handwriting.
- Audio: record audio into a block (mic capture to asset) with no built-in transcription this session; transcription would go through AI providers externally. README mentions audio block recording. **UNVERIFIED this session**: exact transcription state.
- Import/export: import Markdown, Word (.docx), and HTML; export to Markdown, PDF (with book-size options), Word, HTML, images, and Org-mode preserving internal links/images/code (verified in the HN thread and README export list; the HN commenter specifically praises "so many export options, even for Org-Mode"). README + https://news.ycombinator.com/item?id=42512713
- Plugins/extensions/marketplace: "Bazaar" marketplace (kernel/bazaar) with community plugins, themes, icons, templates, and emojy/icon packs distributed as GitHub packages; hundreds of packages listed at https://github.com/siyuan-note/bazaar . Plugin API is JavaScript in the Electron UI (README plugin guide). **UNVERIFIED this session**: exact package count (the bazaar index lists hundreds; not counted).
- Collaboration: single-user per workspace; there is no real-time multi-user editing; the open question "does it support multiple users?" from the HN thread remains effectively no — a workspace syncs to one user's cloud account; teams run separate workspaces. https://news.ycombinator.com/item?id=42512713 and README (no multi-user feature listed). 
- Publishing: "publish" is planned/emerging (a publish-as-site feature exists behind the paid tier in recent releases; changelog mentions publish tooling). **UNVERIFIED this session**: exact state of the publish feature at v3.8.x.

### 5.4 Pricing and the open-core gate
- Pricing page: https://b3log.org/siyuan/en/pricing.html — the page distinguishes free features from paid; a GitHub issue titled "Pricing page should show $59.99/year and $699 lifetime membership more clearly" (https://github.com/siyuan-note/siyuan/issues, title scraped this session) gives the current figures: $59.99/year annual or $699 lifetime. **UNVERIFIED this session**: I could only extract the FAQ text from the pricing page's served HTML this session; the dollar figures come from that issue title, not from a fetched price table.
- What is gated: per the HN thread analysis and README membership features list — the free app is complete for local use, including **local** features; the paid membership gates: (a) official cloud sync (8 GB+), (b) **third-party sync providers S3/WebDAV** (this is the key open-core twist: syncing to your own S3/WebDAV requires membership), (c) AI (annual AI allowance), (d) publish tooling. Lifetime membership covers features but not AI quotas. https://news.ycombinator.com/item?id=42512713 and https://b3log.org/siyuan/en/pricing.html
- Because the gating code ships inside the AGPL codebase, the community has produced patch forks (siyuan-community/siyuan, EightDoor/siyuan) that remove the license checks — legal under AGPL, acknowledged in the HN thread. https://news.ycombinator.com/item?id=42512713

### 5.5 UX evidence
- GitHub issues (fetched 2026-10-27): recurring open items include handwriting support, whiteboard/canvas requests, document-tree performance complaints ("打开文档树卡顿" — document tree lags), WebDAV sync failures (ETag mismatch/lock file), sync stalls ("keeps displaying Connecting"), and ETag/snapshot-cache complaints. The tracker is dominated by Chinese-language issues (the userbase is majority-Chinese), which is itself a signal for international adoption friction. https://github.com/siyuan-note/siyuan/issues
- HN reception (Dec 2024 thread, https://news.ycombinator.com/item?id=42512713): positive — self-hosters report it "knocks out Obsidian in comparison" for feature richness, web access from anywhere, and working sync via their own S3; export options praised. Negative — perceived as an "Obsidian knock-off" that is janky with lacking documentation; distrusted because the team is Chinese and opaque ("couldn't find much about them"), with counter-argument that the founders are publicly identifiable (88250/Vanessa219, a married couple, tianyancha-listed company); Firefox bugs ("don't have time to maintain"); no vim bindings; and an active debate over the licensing oddity (AGPL codebase containing its own paywall checks, plus paid third-party sync). Reddit PKM community reception: consistent with HN — power users appreciate block-based freedom and sync design, but most Western PKM discussion happens around Obsidian/Logseq and SiYuan stays niche outside China. **UNVERIFIED this session**: specific Reddit thread URLs (sentiment above is from the HN thread plus general PKM-community search results this session).

### 5.6 Pull-from assessment
The deepest pull value of all five repos, for exactly the capabilities our future Rust/local-first/handwriting/E2EE app needs:
1. Block-ID-over-files data model: .sy = one JSON block-tree per document on plain files, with block IDs stable across edits, a separate FTS index (SQLite FTS5) derived from the files, and assets as loose files. This gets you git-diffable-ish data, partial corruption resistance, and easy backup, while retaining rich block structure. For a Rust core, this is a proven middle path between "pure markdown files" (loses structure) and "one big database" (loses file-based access). https://github.com/siyuan-note/siyuan/tree/main/kernel/filesys
2. Snapshot-based sync on a content-addressed data warehouse (dejavu): per-device snapshot commits with deterministic conflict merging, provider-agnostic (official cloud / S3 / WebDAV / local dir). This is the single most valuable architectural artifact to study for our sync engine: the provider abstraction (sync_service.go) plus the repository/snapshot separation (repository.go) is a complete design for local-first sync with any storage backend. https://github.com/siyuan-note/siyuan/tree/main/kernel/model and https://github.com/siyuan-note/dejavu
3. E2EE design: repo key from user passphrase encrypting the snapshot repo, so any storage provider (including their own cloud) never sees plaintext. Directly transplantable: our Rust core should hold a keyfile/passphrase-derived key and encrypt all sync payloads client-side. https://github.com/siyuan-note/siyuan/blob/main/kernel/model/repository.go
4. SQLCipher path for encrypting local notebooks (DEK per box) — a second, complementary E2EE layer to study. https://github.com/siyuan-note/siyuan/tree/main/kernel/model
5. Attribute view (Notion-like databases as typed column schemas over blocks): if we want tables/databases in the Rust app, av/capabilities.go is a compact reference for column-type taxonomy. https://github.com/siyuan-note/siyuan/tree/main/kernel/av
6. MCP server exposure (kernel/mcp): a modern, low-cost way to make the local app scriptable by AI agents; worth replicating.
7. Anti-patterns to avoid (validated by their issue tracker): WebDAV as a first-class sync provider creates a permanent class of ETag/lock bugs; snapshot-caching on proxies (ETag mismatch) is fragile. Our sync should own its wire protocol over S3-compatible storage only, or peer-to-peer, and treat WebDAV as a compatibility fallback at most. https://github.com/siyuan-note/siyuan/issues
8. Business model note: gating self-hosted S3/WebDAV sync behind membership while shipping the gate inside an AGPL codebase is fragile (patch forks exist). For our project, sync-engine code and storage-tier gating should be separated from the open core.

---

## Session totals
- Repos fully covered: 5/5. Claims captured with primary-source URLs: ~150. Claims marked UNVERIFIED this session: 12 (zappynotes star count, zappynotes AI scope, zappynotes import/export, owlistic versioning internals, owlistic conflict handling, NexaNote AI scope, NexaNote platform availability, memos relicensing-beyond-copyright, memos search engine, memos hosted-offering existence, siyuan historical license-revision wording, siyuan current pricing figures, siyuan plugin count, siyuan audio transcription, siyuan Reddit thread URLs — several items overlap; net UNVERIFIED items: 15).
- File: /home/thaura/notesapp/findings-r7/r7-user-repos-b.md
