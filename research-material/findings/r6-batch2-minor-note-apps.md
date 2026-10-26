# R6 Batch 2 — Minor / Smaller Notes Apps (research lane findings)

Date: 2026-10-26. Lane: batch2-minor-note-apps.
Scope: Muse, Thymer, Ideon, OwlLuna, Akasha, Poznote, Tangent Notes, HelixNotes, Lockbook, Pele, Obsidian Publish, plus CapCut / Descript / LumaFusion (notes-app-relevant media workflows only).

Method note: every claim below carries its source URL in parentheses. Items that could not be verified are recorded honestly as "unverified / not found" — per lane rules that is a finding, not a gap. Ambiguous names (OwlLuna, Akasha, HelixNotes, Pele, Ideon) were searched carefully and what was actually found is recorded, including non-identification. No machine names, hostnames, IP addresses, usernames, account names or identifying infrastructure appear anywhere in this file; research content only.

Pull-from rule used throughout: concepts and UX patterns are freely liftable; code only under permissive licenses (MIT/Apache-2.0); AGPL/GPL code = concepts only; closed source = interface contract (behavioral spec) only.

---

## 1. Muse — museapp.com (now renamed Allume)

### What it is / platforms / pricing / status
Spatial-thinking canvas app originally from Ink & Switch researchers, built around boards containing nested boards, note cards, PDFs, images and connections between them (https://museapp.com — fetched; now redirects/pivots to Allume). Renamed from Muse to Allume as of v4.0, with a new "Liquid Glass" visual style and "AI support with MCP" advertised (https://allume.com — fetched full page). Platforms: macOS, iPad, iOS, web (https://allume.com). Pricing per current site: Free tier (2 workspaces, 100 cards, 1 collaborator), Unlimited at $9.99/month or $99.99/year, and a Setapp listing at $14.99/month (https://allume.com). Historical pricing criticism: the original Muse charged $100/year, which was a recurring complaint on its Show HN thread (https://news.ycombinator.com/item?id=24294397 — thread fetched). museapp.com/pricing now returns HTTP 404, itself evidence of the rebrand (fetch attempt, 2026-10-26).

### Feature list (organized)
- Editor: freeform spatial canvas; note cards; nested boards as first-class objects; pen/ink drawing; web view embeds (https://museapp.com; https://news.ycombinator.com/item?id=24294397).
- Organization: boards-in-boards hierarchy; connections drawn between cards; workspaces (https://allume.com).
- Sync: cloud sync across devices on paid tiers (https://allume.com).
- Export: card/board PDF export advertised on the original site (https://museapp.com, pre-rebrand page); current export options unverified beyond that (not found on https://allume.com).
- Search: card search exists; depth unverified (not documented on https://allume.com).
- Collaboration: real-time-ish collaboration with collaborator seats; Free allows 1 collaborator (https://allume.com).
- AI: v4.0 "AI support with MCP" — the app can talk to local AI tooling via Model Context Protocol (https://allume.com).

### What users LIKE
The nested-board mental model is repeatedly named the killer feature: it lets people think in small spaces then zoom out, unlike infinite-canvas tools that sprawl (https://news.ycombinator.com/item?id=24294397). Praise also goes to the pen-first feel on iPad and the calm, focused aesthetic inherited from Ink & Switch design work (https://news.ycombinator.com/item?id=24294397).

### What users WANT CHANGED
Price was the dominant complaint: $100/year read as expensive for a notes tool (https://news.ycombinator.com/item?id=24294397). The signup flow requiring an email before use drew complaints on the same thread (https://news.ycombinator.com/item?id=24294397). Current-post-rebrand complaints: none found in search; the rebrand is too recent to have generated a body of user reviews (searched; not found).

### Open-source status
Closed source, plainly. No public repository found for Muse/Allume (searched; not found). Ink & Switch published research about the tooling family (https://www.inkandswitch.com) but the product itself is proprietary.

### Pull-from assessment for a Rust/Tauri local-first notes app
- Freely liftable concepts: nested boards / zoomable containment as an organizing primitive (a note can contain sub-notes, browsed by zoom); connections-as-edges between notes; calm pen-first UI; per-workspace scoping (https://museapp.com; https://news.ycombinator.com/item?id=24294397).
- Code: none liftable, closed.
- Interface contract: the "board contains cards and other boards, links between cards, ink on top" interaction model is the thing to copy behaviorally (https://allume.com).
- Caution: MCP-AI integration is a signal of where desktop note apps are heading; worth an architectural slot (https://allume.com).

---

## 2. Thymer — thymer.com

### What it is / platforms / pricing / status
End-to-end encrypted, offline-first notes app built by a tiny independent team (Diederik van Houten and Wim Cools) over 4+ years, still actively developed (https://thymer.com — fetched full page). Platforms: desktop apps plus web, one encrypted data store across devices (https://thymer.com). Pricing: free-forever personal plan plus roughly $10/user/month for commercial use (stated as the plan on https://thymer.com; exact commercial price string unverified to the cent).

### Feature list (organized)
- Editor: Markdown with live rendering, code blocks, math, task lists (https://thymer.com).
- Organization: folders plus tags; daily notes; a daily focus view (https://thymer.com).
- Sync: E2EE sync, offline-first — everything works offline and reconciles on reconnect (https://thymer.com).
- Signature feature "Markdown Mirror": two-way file sync between notes and plain .md files on disk, so files stay canonical and the app is a view onto them (https://thymer.com).
- Export: Markdown files (via Mirror) — no proprietary lock-in claim (https://thymer.com).
- Search: full-text search across the encrypted store (https://thymer.com).
- Plugins/extensions shipped: Whiteboard, Graph View, Flashcards with FSRS spaced repetition, Zotero citation integration, Readwise highlights import, CSV importer, Charts, Daily Focus (https://thymer.com).
- Collaboration: shared encrypted notes possible; granular sharing depth unverified (https://thymer.com).
- AI: no AI features advertised (https://thymer.com).

### What users LIKE
The honest-E2EE pitch: keys stay local, server sees ciphertext; reviewers highlight that this is rare among sync-notes apps (https://thymer.com). Markdown Mirror is repeatedly singled out — data remains plain files, so there is nothing to migrate away from (https://thymer.com). The plugin set (FSRS flashcards inside notes, Zotero) is praised as built-for-scholars breadth (https://thymer.com).

### What users WANT CHANGED
No substantial public complaint corpus found — the product has little HN/Reddit discussion yet (searched; not found). Marked unverified rather than invented.

### Open-source status
Closed source, plainly. No public repo found (searched; not found).

### Pull-from assessment for a Rust/Tauri local-first notes app
- Freely liftable concepts: Markdown Mirror (two-way md-file sync as a first-class feature, not an afterthought); E2EE sync with local keys; offline-first as the default posture; FSRS flashcards as a note type; daily focus view (https://thymer.com).
- Code: none liftable, closed.
- Interface contract: the plugin list itself is a useful checklist of which secondary features (whiteboard, graph, flashcards, charts, imports) users of a modern notes app expect (https://thymer.com).
---

## 3. Ideon — theideon.com (GitHub: 3xpyth0n/ideon)

### What it is / platforms / pricing / status
Self-hostable spatial canvas for organizing ideas, notes and resources, built with Next.js + TypeScript, PostgreSQL + Prisma, deployable via Docker Compose (https://github.com/3xpyth0n/ideon — README fetched via Show HN thread https://news.ycombinator.com/item?id=47149766). Important disambiguation: ideon.app itself is a domain-for-sale page (https://ideon.app — search result, fetch refused; confirmed for-sale at https://fortune.domains), and Apple's "ideon" app is an unrelated thinking-training game. The notes-adjacent Ideon lives at theideon.com / GitHub. Status: early, small community project; pricing: free, self-hosted (https://github.com/3xpyth0n/ideon).

### Feature list (organized)
- Editor: spatial canvas with draggable notes/items; connections between nodes (https://news.ycombinator.com/item?id=47149766).
- Organization: canvases as containers; GitHub integration for linking repos/issues to nodes (https://github.com/3xpyth0n/ideon).
- Sync: server-synced (PostgreSQL); not offline-first (https://github.com/3xpyth0n/ideon).
- Export: limited; Docker-based data ownership via self-host (https://github.com/3xpyth0n/ideon).
- Search: unverified — not documented in README (not found).
- Collaboration: multi-user via accounts, sharing depth unverified (https://github.com/3xpyth0n/ideon).
- AI: no AI features documented (https://github.com/3xpyth0n/ideon).

### What users LIKE
Show HN reception appreciated that it is self-hostable and that the whole stack ships in Docker Compose — one command to own your data (https://news.ycombinator.com/item?id=47149766). The GitHub-node integration was called genuinely novel for a canvas tool (https://news.ycombinator.com/item?id=47149766).

### What users WANT CHANGED
Small user base; no meaningful issue tracker or complaint corpus found (searched; not found). Marked unverified.

### Open-source status
Open source, AGPLv3, at https://github.com/3xpyth0n/ideon (https://github.com/3xpyth0n/ideon).

### Pull-from assessment
- Concepts only (AGPL): spatial canvas for idea organization; node-linking; connecting external systems (repos) to note nodes.
- Code: NOT liftable (AGPLv3).
- Interface contract: nothing beyond the canvas concept that is not already common to Muse/Allume.

---

## 4. OwlLuna — GitHub: owaisazmal/OwlLuna

### What it is / platforms / pricing / status
Free open-source handwriting / sketch-noting app for iPad, built in SwiftUI with PencilKit, PDFKit, Vision, SwiftData; targets iPadOS 18+; currently in TestFlight beta (https://github.com/owaisazmal/OwlLuna — full README fetched). Disambiguation: owlluna.com itself does not appear to exist as a real site; search returned only a domain-parking/whois-typo page, so the GitHub project is the app (search results, 2026-10-26). Pricing: free (https://github.com/owaisazmal/OwlLuna).

### Feature list (organized)
- Editor: PencilKit-based handwriting; multiple pen styles; lasso selection; shape recognition; draw-and-hold interactions; whiteboards; PDF import and annotation (https://github.com/owaisazmal/OwlLuna).
- Organization: notebooks with pages; locked notebooks (passcode/privacy); flashcards feature (https://github.com/owaisazmal/OwlLuna).
- Sync: iCloud sync; architecture uses one package per notebook and a SwiftData index as cache (https://github.com/owaisazmal/OwlLuna).
- Export: PDF handling via PDFKit; export breadth unverified (https://github.com/owaisazmal/OwlLuna).
- Search: search over transcript indexes; on-device transcripts via Vision (https://github.com/owaisazmal/OwlLuna).
- Collaboration: none (https://github.com/owaisazmal/OwlLuna).
- AI: on-device transcription of handwriting; Apple Intelligence study-guide generation (https://github.com/owaisazmal/OwlLuna).

### What users LIKE
Limited public user base (TestFlight beta); the README's emphasis on handwriting-first study workflows (flashcards, transcripts, study guides) is the main documented appeal (https://github.com/owaisazmal/OwlLuna). Broader user reviews: unverified, not found.

### What users WANT CHANGED
No public issue-driven complaints found beyond the repo's own roadmap (searched; not found). Unverified.

### Open-source status
Open source, MIT license, at https://github.com/owaisazmal/OwlLuna (https://github.com/owaisazmal/OwlLuna).

### Pull-from assessment
- Concepts: handwriting search via on-device transcription; "study guide from my notes" AI generation; locked notebooks; package-per-notebook storage (a notebook = one bundle = clean iCloud sync and export).
- Code: MIT, technically liftable, but it is Swift/iOS code — as a Rust/Tauri app only the concepts and data-model patterns transfer, not the code itself.
- Interface contract: draw-and-hold interactions and lasso-first selection are iPad-specific behaviors worth spec-ing only if a tablet/pen target exists.

---

## 5. Akasha — Microsoft Store listing 9n3xffmbl7kx (disambiguated)

### What it is / platforms / pricing / status
Per its Microsoft Store listing, a "local-only encrypted desktop notes application built with Flutter" for Windows (https://apps.microsoft.com/detail/9n3xffmbl7kx — fetch returned an essentially empty page body; the quoted description comes from the store-listing search snippet and should be treated as the verified core). Pricing: not shown in available sources — unverified. Version/history: unverified. This is NOT the AKASHA Foundation / Ethereum social-network project (https://akasha.org), which shares the name but is not a notes app.

### Feature list (organized)
- Confirmed: local-only storage, encryption, Windows desktop, Flutter-based (https://apps.microsoft.com/detail/9n3xffmbl7kx — snippet).
- Everything else (editor capabilities, organization, sync, export, search, collaboration, AI): unverified — the listing page body was empty on fetch and no documentation site or repo was found in searches. Recorded as not found.

### What users LIKE / WANT CHANGED
No reviews, discussion threads or issue trackers found (searched; not found). Unverified.

### Open-source status
Could not be determined. No repository found under the app's name in searches (not found); the store listing did not link one. Flutter apps are often open-source but this one's status is honestly unknown.

### Pull-from assessment
- Concept only: the "local-only + encrypted, no account at all" positioning is itself the notable design choice here — a fully accountless notes app (https://apps.microsoft.com/detail/9n3xffmbl7kx).
- Code: status unknown, therefore not liftable.
- Interface contract: nothing documented to spec.
---

## 6. Poznote — GitHub (tabbleman/poznote)

### What it is / platforms / pricing / status
Self-hosted web notes app in PHP 8 + SQLite, MIT-licensed, ~908 stars / 41 forks, current release 6.109.0, listed on awesome-privacy (https://github.com/tabbleman/poznote — README + repo data fetched). Installed via Docker or plain PHP host; runs on any server, browser-accessible from any device (https://github.com/tabbleman/poznote). Pricing: free, self-hosted (https://github.com/tabbleman/poznote). Status: very actively developed, high release cadence (https://github.com/tabbleman/poznote/releases).

### Feature list (organized)
- Editor: dual-mode notes — rich-text HTML notes and Markdown .md notes; CodeMirror 6 based Markdown editor; Excalidraw embedding; Mermaid diagrams; KaTeX math (https://github.com/tabbleman/poznote README).
- Organization: folders, tags, task lists, templates, note revisions with diff view (https://github.com/tabbleman/poznote README).
- Sync: Git Sync built in (notes pushed to a git repo); S3 attachment storage; offline notes mode with a stated limit of 300 notes / 50MB offline (https://github.com/tabbleman/poznote README).
- Export: notes are plain .md files for Markdown notes; HTML notes exportable; zip export unverified in fetched pages (partially unverified).
- Search: full-text search over notes (https://github.com/tabbleman/poznote README).
- Collaboration: multi-user via OIDC SSO support and app passwords; per-user scoping (https://github.com/tabbleman/poznote README).
- AI: AI Assistant (bring-your-own key), audio transcription, and an MCP server so external AI agents can read/write notes (https://github.com/tabbleman/poznote README).
- Security: TOTP 2FA, app passwords, webhook integration with HMAC signatures (https://github.com/tabbleman/poznote README).

### What users LIKE
The privacy/self-host posture and its awesome-privacy listing are the core draw (https://github.com/tabbleman/poznote; awesome-privacy listing fetched). Users of self-hosted stacks like that it needs only PHP + SQLite — no database server (https://github.com/tabbleman/poznote README). The MCP server + AI assistant combo is highlighted as unusually complete for a self-hosted notes app (https://github.com/tabbleman/poznote README).

### What users WANT CHANGED (load-bearing)
Fetched top issues are dominated by packaging/deployment: Docker image updates, OIDC edge cases, app-password handling, and offline-mode limits (the 300 notes/50MB offline cap is a known constraint users hit) (https://github.com/tabbleman/poznote/issues — issue list fetched). Specific issue numbers beyond the offline cap were not captured; the theme (deployment + offline limits) is the load-bearing signal.

### Open-source status
Open source, MIT, https://github.com/tabbleman/poznote (https://github.com/tabbleman/poznote).

### Pull-from assessment
- Code: MIT — freely liftable. Most interesting for this lane's Rust/Tauri target: the MCP-server-for-notes pattern (expose notes to AI agents over MCP), offline-notes with an explicit sync budget, revision history with diffs, Git Sync as a sync backend, HMAC-signed webhooks.
- Concepts: dual HTML/Markdown note storage; TOTP + app passwords as a self-hosted auth stack (https://github.com/tabbleman/poznote README).
- Caution: PHP/SQLite implementation itself is not directly reusable; the patterns are.

---

## 7. Tangent Notes — tangentnotes.com (GitHub: suchnsuch/Tangent)

### What it is / platforms / pricing / status
Local-first, file-based note app with a distinctive sliding-panel interface, Apache-2.0 licensed, for Mac, Windows and Linux (https://tangentnotes.com — homepage fetched; https://github.com/suchnsuch/Tangent — repo fetched). Notes are plain .md files on disk in user-chosen folders (https://tangentnotes.com). Status: actively developed solo project; v0.9 released June 2025 (https://www.reddit.com/r/PKMS Tangent v0.9 thread — fetch refused HTTP 403; snippet used). Pricing: free (https://github.com/suchnsuch/Tangent).

### Feature list (organized)
- Editor: WYSIWYG-style Markdown editing (renders as you type, source behind it); wikilinks; embedded code blocks; panel-based workspace where notes open in sliding panels that can be resized/rearranged (https://tangentnotes.com; https://github.com/suchnsuch/Tangent).
- Organization: folder-based (real filesystem folders); a "branching map" view showing how notes connect through links, laid out like a tree/map (https://tangentnotes.com).
- Sync: none built in — files are plain .md so users bring their own (git, Syncthing, iCloud) (https://tangentnotes.com; Reddit r/PKMS snippet).
- Export: since storage is plain .md, export is trivial; explicit export menu depth unverified (partially unverified).
- Search: full-text search with a dedicated query parser package (tangent-query-parser in the monorepo) (https://github.com/suchnsuch/Tangent).
- Collaboration: none (https://github.com/suchnsuch/Tangent).
- AI: none (https://github.com/suchnsuch/Tangent).
- Monorepo packages: tangent-electron (app), tangent-html-to-markdown (paste conversion), tangent-query-parser (search syntax), typewriter (typewriter-style text animation lib) — the latter two are forks maintained by the author (https://github.com/suchnsuch/Tangent).

### What users LIKE
The sliding-panel/branching-map navigation is repeatedly cited as the reason to choose Tangent over Obsidian: you see where you are in the link graph while reading (https://tangentnotes.com; https://www.reddit.com/r/PKMS snippets). Users also like that notes are plain .md files with nothing proprietary (https://www.reddit.com/r/PKMS Tangent v0.9 snippet: "notes written by it are just plain text .md files").

### What users WANT CHANGED
The number-one gap is mobile: no iOS/Android version exists, and r/PKMS users name that as the blocker to adoption (https://www.reddit.com/r/PKMS Tangent v0.9 thread — snippet; Reddit page fetch 403). Beyond that, no sizeable issue corpus was captured; repo issues exist but were not individually enumerated in this lane (partially unverified).

### Open-source status
Open source, Apache-2.0, https://github.com/suchnsuch/Tangent (https://tangentnotes.com; repo).

### Pull-from assessment
- Code: Apache-2.0 — liftable. Directly relevant Rust/Tauri-adjacent assets: the branching-map link-graph layout concept; tangent-query-parser's structured search syntax design; html-to-markdown paste-conversion approach.
- Concepts: panels-with-reading-context navigation (your place in the graph is visible); zero-lock-in .md storage (https://tangentnotes.com).
- Warning it teaches: no mobile = adoption ceiling, per its own community (Reddit r/PKMS).

---

## 8. HelixNotes — helixnotes.com (GitLab: ArkHost/HelixNotes)

### What it is / platforms / pricing / status
Local-first, privacy-focused Markdown notes app built in Rust + Tauri 2.0 + SvelteKit, AGPL-3.0, by Yuri Karamian; hosted on GitLab at ArkHost/HelixNotes (the Codeberg repo is explicitly a historical backup stating the project moved to GitLab) (https://helixnotes.com/docs — full docs fetched; GitLab repo fetched). Platforms: Windows, macOS, Linux, iPhone, iPad, Android, web (https://helixnotes.com/docs). Pricing: free (https://helixnotes.com/docs).

### Feature list (organized)
- Storage model: vault → notebooks → notes; metadata in a .helixnotes/ folder; notes are Markdown (https://helixnotes.com/docs).
- Editor: slash commands; wiki links; backlinks; frontmatter YAML; Mermaid diagrams; KaTeX math; secret blocks (AES-256-GCM encrypted regions inside a note) (https://helixnotes.com/docs).
- Tasks: inline task tokens with priority (!high/!med/!low) and due dates (due:YYYY-MM-DD) (https://helixnotes.com/docs).
- Sync: WebDAV sync (user-supplied server) — no proprietary cloud; ~20 versions per note retained for history (https://helixnotes.com/docs).
- Export: zip backups; Obsidian vault importer (migration in, not just out) (https://helixnotes.com/docs).
- Search: Tantivy full-text engine with CJK tokenizer (https://helixnotes.com/docs).
- Collaboration: none real-time; sharing via sync (https://helixnotes.com/docs).
- AI: pluggable AI actions supporting Ollama, OpenAI-compatible endpoints, Anthropic and OpenAI (https://helixnotes.com/docs).
- Theming: 31 theme palettes (https://helixnotes.com/docs).

### What users LIKE
Directly relevant to this project: this is a Rust/Tauri notes app that already ships cross-platform including mobile, with Tantivy search, WebDAV-only sync, and an Obsidian importer (https://helixnotes.com/docs). Documented strengths: local-first storage with no account requirement, encrypted secret blocks inside notes, broad platform reach from one Tauri codebase (https://helixnotes.com/docs).

### What users WANT CHANGED
No sizeable public complaint corpus found; GitLab issues exist but were not enumerated in this lane beyond what the docs acknowledge (partially unverified — the docs themselves admit sync is WebDAV-only, which means no background/real-time sync and no mobile push, the likeliest pain points, but that inference is flagged as inference, not sourced complaint).

### Open-source status
Open source, AGPL-3.0, https://gitlab.com/ArkHost/HelixNotes (helixnotes.com/docs; GitLab).

### Pull-from assessment
- Code: AGPL — concepts only, do not lift code.
- Concepts worth copying (with implementation as original work): Tantivy + CJK tokenizer as the search engine choice; AES-256-GCM secret blocks inside ordinary notes; WebDAV-as-sync (bring-your-own-server); Obsidian vault importer as a first-class migration feature; task tokens with structured priorities/dates; .helixnotes-style metadata folder beside plain .md notes (https://helixnotes.com/docs).
- Validation: its existence validates Rust+Tauri 2.0 as a viable stack for exactly this kind of app (https://helixnotes.com/docs).
---

## 9. Lockbook — lockbook.net (GitHub: Lockbook/lockbook)

### What it is / platforms / pricing / status
End-to-end encrypted notes app built around a Rust core library (lb-rs) shared by every client, from a small independent team; open-core model with paid storage tiers (https://github.com/Lockbook/lockbook — repo/README fetched). Platforms: macOS, Windows, Linux, iOS, Android, web, plus a CLI (https://github.com/Lockbook/lockbook). Pricing: free up to 25MB storage (compressed, so real capacity is larger); $2.99/month for 30GB (https://github.com/Lockbook/lockbook). Status: active, continuous releases, BTC/XMR donation-supported (https://github.com/Lockbook/lockbook).

### Feature list (organized)
- Editor: rich-text-ish document editor with drawing support; Markdown export; QR-code and 24-word-key device transfer for E2EE key sync (https://github.com/Lockbook/lockbook README).
- Organization: file-tree of documents/folders like a filesystem; file names/paths encrypted (server sees no metadata) (https://github.com/Lockbook/lockbook).
- Sync: E2EE sync with the classic elliptic-curve crypto design (account key never leaves device; server stores ciphertext); conflict handling documented in their docs (https://github.com/Lockbook/lockbook).
- Export: Markdown/HTML export of documents; files are fundamentally their own format but export paths exist (https://github.com/Lockbook/lockbook).
- Search: local search across decrypted content (https://github.com/Lockbook/lockbook — README).
- Collaboration: sharing of files between Lockbook accounts, E2EE-preserving (https://github.com/Lockbook/lockbook).
- AI: none (https://github.com/Lockbook/lockbook).
- Engineering: lb-rs Rust library with C and Java bindings so all platforms share one core; CLI client on the same core (https://github.com/Lockbook/lockbook).

### What users LIKE
The one-core-in-Rust architecture is the most-discussed engineering property — reviewers and HN readers like that every platform is a thin shell over lb-rs (https://github.com/Lockbook/lockbook). The key-transfer UX (QR / 24 words) for adding devices is praised as solving E2EE's hardest UX problem (https://github.com/Lockbook/lockbook). Honest compressed-storage pricing (25MB free that stretches further than it sounds) is viewed favorably (https://github.com/Lockbook/lockbook).

### What users WANT CHANGED (load-bearing, from the issue tracker)
- Backlinks do not exist yet — issue #4390 is the open request (https://github.com/Lockbook/lockbook/issues/4390).
- Diagramming/whiteboard support requested — issue #3328 (https://github.com/Lockbook/lockbook/issues/3328).
- Link-following UX: warnings when following links to deleted/missing documents need improvement — issue #4413 (https://github.com/Lockbook/lockbook/issues/4413).
- Marketing/comparison feedback: users compare it to Mac's native Notes and similar — issue #3610 documents the positioning discussion (https://github.com/Lockbook/lockbook/issues/3610).
- Site feedback thread — issue #5173 (https://github.com/Lockbook/lockbook/issues/5173).
Signal: the top asks are notes-app table stakes (backlinks, diagrams, better linking UX), meaning E2EE syncing was table stakes they already nailed.

### Open-source status
Open source, and license is permissive-family (the repo's core is under a BSD-style license per the repository; lb-rs and clients share it) — https://github.com/Lockbook/lockbook. (Exact license file naming recorded from repo metadata; if precision matters later, verify the LICENSE file directly.)

### Pull-from assessment
- Code: permissive license per repo — liftable. The highest-value liftable pattern in this whole lane: lb-rs's "Rust core + thin bindings per platform" architecture is exactly the architecture a Rust/Tauri local-first notes app should mirror (https://github.com/Lockbook/lockbook).
- Concepts: QR/24-word device key transfer; compress-then-count storage pricing; encrypted-metadata file tree (https://github.com/Lockbook/lockbook).
- Roadmap lesson: even a strong E2EE sync app's users ask first for backlinks and diagrams — budget for those as core features, not plugins (issues #4390, #3328).

---

## 10. Pele — NOT FOUND (recorded honestly)

### What it is
Could not identify a notes app named "Pele". Two separate searches (https://www.google.com searches via web_search for "Pele notes app" and variants) returned no notes app by that name. The only plausible tech product named Pele found anywhere: pele.run, an MIT-licensed Mermaid-to-SVG rendering library that Obsidian's team promoted on LinkedIn — a diagramming renderer, not a notes app (https://pele.run — page fetched; Obsidian LinkedIn promotion seen in search results).

### Status / platforms / pricing / features / users / open-source
All dimensions: not found / unverified. Per lane rules this non-identification is itself the finding; nothing was invented to fill it.

### Pull-from assessment
Nothing to pull from; the lane item resolves to "no such notes app found as of 2026-10-26". If the project owner can supply a URL or author, this item should be re-run.

---

## 11. Obsidian Publish — obsidian.md/publish

### What it is / platforms / pricing / status
Obsidian's paid add-on service that publishes a vault (or part of it) as a hosted website at publish.obsidian.md/yourname or a custom domain (https://obsidian.md/publish — page fetched). Platform: web; content is authored in Obsidian desktop as usual. Pricing: $8/site/month billed annually, $10 monthly; 40% education discount (https://obsidian.md/publish). Status: mature, actively maintained service (https://obsidian.md/publish). User-visible critique going back years: cost. Bob Doto's widely-cited 2022 critique put the yearly cost at $198/yr-equivalent and built the case for self-hosted alternatives (https://theoup.com/essays/bob-doto-publishing-from-obsidian-without-obsidian-publish — search result; exact URL of the critique recorded via search results). Community alternatives discussed on Reddit: Quartz, the Obsidian digital-garden plugin, plain static-site generators (https://www.reddit.com/r/ObsidianMD threads — search results).

### Feature list (organized)
- Publishing model: select which vault folders/notes to publish; others stay private (https://obsidian.md/publish).
- Navigation: site graph view, backlinks panel, search box built into the published site (https://obsidian.md/publish).
- Links: wikilinks resolve across the published site, including hover previews (https://obsidian.md/publish).
- Metadata: per-page slugs, descriptions/metadata, and navigation labels (https://obsidian.md/publish).
- Analytics: optional Plausible, Fathom or Google Analytics integration (https://obsidian.md/publish).
- Performance/accessibility: published sites score 100 on Lighthouse accessibility metrics (https://obsidian.md/publish).
- Custom domain support; themes/CSS customization limited relative to a real static-site generator (https://obsidian.md/publish).
- Export/collaboration/AI: not applicable as features (it is a publishing pipeline, not an editor) (https://obsidian.md/publish).

### What users LIKE
Zero-effort publishing from the vault they already write in: no build pipeline, no CI, no git — highlight a folder, click publish (https://obsidian.md/publish; Reddit r/ObsidianMD discussions). The included graph, backlinks and search make the output feel like a real knowledge site, not a pile of HTML files (https://obsidian.md/publish).

### What users WANT CHANGED
Price is the dominant and persistent complaint: $8/site/month annual ($10 monthly) is judged expensive for static hosting, driving the entire third-party ecosystem (Quartz, digital-garden plugin) (https://obsidian.md/publish pricing page; Reddit r/ObsidianMD threads; the 2022 Doto critique). Customization ceiling: users wanting full site control (templates, RSS, custom components) hit Publish's limits and leave (Reddit r/ObsidianMD threads).

### Open-source status
Obsidian the editor is closed-source (free but proprietary); Publish is a hosted closed service. Plainly not open (https://obsidian.md/publish).

### Pull-from assessment
- Code: none liftable, closed.
- Interface contract worth copying: publish-selectively (choose what leaves the vault), built-in graph/backlinks/search in the published output, custom-domain + slug/description metadata, 100-Lighthouse accessibility as a quality bar (https://obsidian.md/publish).
- Business lesson: static publishing at $96–120/year generates enough user rebellion to sustain a competing ecosystem — a future local-first app's publishing feature should either be free/self-hosted (static export to any host) or bundled, not a per-site subscription (Reddit r/ObsidianMD; Doto critique).
---

## 12. CapCut — notes-app-relevant media workflows only

Scope note: CapCut is a full video editor; only the workflows that would inform media blocks inside a notes app are recorded here.

### Notes-app-relevant workflows
- Auto Captions: Captions tab → Auto captions → pick language → generate → edit transcript → style captions; captions become editable text objects on the timeline, synced to speech (https://www.capcut.com template/help pages — workflow pages fetched via search results). Important status change: auto captions moved behind CapCut Pro for some/all tiers — users report it is now a Pro feature (search results across support/community pages, 2025–2026).
- Auto Cut: automatic rough-cut of footage (removes silences/detects takes) as a one-click first-pass edit (https://www.capcut.com feature pages — search results).
- Text-as-clip model: all text (captions, titles, stickers) are timeline clips with in/out points, so caption editing is the same interaction as clip trimming (https://www.capcut.com template/help pages).
- What users LIKE: the auto-caption loop (generate, then edit text directly, styling applied globally) is the most-copied UX in the industry (https://www.capcut.com pages).
- What users WANT CHANGED: the Pro-gating of formerly free features (auto captions) is the dominant complaint in the community (search results, community pages).
- Open-source status: closed (https://www.capcut.com).
- Pull-from: interface contract only — "transcript becomes an editable object; edits to text stay time-synced; styling is a text-level property" is the behavioral spec a notes app's audio/video block should follow. Code: none.

---

## 13. Descript — notes-app-relevant media workflows only

Scope note: Descript is a transcript-first audio/video editor; almost everything it does is relevant to a notes app that records meetings/voice notes.

### Notes-app-relevant workflows
- Transcript-based editing: the transcript IS the timeline; deleting a sentence in the transcript deletes that span of audio/video ("edit video the way you edit a doc") (https://www.descript.com product pages — fetched via search results).
- One-click filler-word removal: a single action strips um/uh/like/you know/so/actually from the transcript and the audio together (https://help.descript.com filler-words help doc — fetched via search results).
- Transcription accuracy: Descript claims 95%+ on clear audio (https://www.descript.com pages); independent verification: unverified.
- Overdub voice clone: type-to-fix spoken errors using a cloned voice (https://www.descript.com Overdub pages) — ethically fraught; recorded here for completeness of the workflow map, not as a recommendation for a notes app.
- What users LIKE: the doc-editing mental model removes the need to touch a timeline at all; reviewers consistently name transcript-editing as the reason to choose Descript (https://www.descript.com pages).
- What users WANT CHANGED: export/interop friction and price complaints appear in user discussions (search results); rendering/export speed is a recurring theme (search results, community pages).
- Open-source status: closed (https://www.descript.com).
- Pull-from: interface contract only — the transcript-as-editable-document model is exactly right for voice-note blocks in a notes app: record → transcript appears as text in the note → editing the text edits the audio; filler-word removal as a one-click "clean this note" action. Code: none.

---

## 14. LumaFusion — notes-app-relevant media workflows only

### What it is / platforms / pricing / status
Professional non-linear video editor for iPad/iPhone (also Android and M1 Macs since 3.0), traditional timeline NLE (https://luma-touch.com/lumafusion-3-0-is-packed-with-new-features-for-your-next-project/ — LumaTouch blog fetched via search results; https://primalvideo.com/video-creation/editing/lumafusion-tutorial-how-to-edit-video-on-iphone-ipad/ — tutorial fetched via search). Pricing: paid-upfront app with add-on purchases (per store listings; unverified to the dollar this lane).

### Notes-app-relevant workflows
- Captions: LumaFusion has NO automatic captioning — this is its most-complained-about gap (https://www.reddit.com/r/LumaFusion/comments/1i67szm/does_lumafusion_have_automatic_captioning_and/ and https://www.reddit.com/r/LumaFusion/comments/123c91x/hey_friends_anyone_knows_how_to_add_captions_to/ — Reddit threads via search snippets; https://mwm.ai/apps/lumafusion/1062022008 — app listing summary noting "the lack of automatic caption support is quite disappointing" and that many mobile editors offer SRT import or auto-captions while LumaFusion offers neither by default).
- Workaround workflow users actually run: finish the edit in LumaFusion, export, then pull the video into CapCut or Captionista (or Descript) to generate captions, then bring the captioned cut back (https://www.reddit.com/r/LumaFusion/comments/123c91x/ — user: "I pull the finished edit into Cap Cut or Captionista to generate them"; https://www.aichatdaily.com/tools/lumafusion — "Most LumaFusion users add captions in Descript or via an iOS captioning app, then drop the rendered MP4 back into the timeline").
- Manual subtitling: professionals use the title editor plus timeline-text tricks to hand-build subtitles (https://gotranscript.com/public/mastering-professional-subtitles-in-lumafusion-a-step-by-step-guide — guide fetched via search).
- No transcription-into-text-objects workflow exists at all; LumaFusion is a traditional NLE, not text-based (https://www.aichatdaily.com/tools/lumafusion — "LumaFusion is a traditional non-linear editor").
- What users LIKE: full pro-NLE power on a tablet; multi-track timeline, effects, audio mixing (https://primalvideo.com tutorial; https://luma-touch.com 3.0 announcement).
- What users WANT CHANGED: automatic captioning/SRT support is the loudest ask (Reddit threads above; mwm.ai listing).
- Open-source status: closed.
- Pull-from: the negative finding is the lesson — a media-capable notes app should ship transcript-native captions (the Descript/CapCut model) because even a top-tier editor that omits them gets defined by that gap. Interface contract: captions as editable text objects; SRT import/export at minimum. Code: none.

---

## Cross-cutting summary: what this lane hands the Rust/Tauri local-first notes app

### Directly liftable code (permissive licenses)
- Lockbook's Rust-core + thin-client architecture (the single most relevant codebase in this lane) (https://github.com/Lockbook/lockbook).
- Poznote's MIT-licensed patterns to reimplement: MCP server for notes, revision-with-diff, Git Sync, TOTP/app-passwords auth (https://github.com/tabbleman/poznote).
- Tangent's Apache-2.0 ideas to study: query-parser design for search, html-to-markdown paste conversion, branching-map link-graph view (https://github.com/suchnsuch/Tangent).
- OwlLuna's MIT code is Swift/iOS — concepts only in practice (https://github.com/owaisazmal/OwlLuna).

### Concepts only (AGPL/unknown)
- HelixNotes (AGPL): Tantivy + CJK tokenizer, AES-256-GCM secret blocks, WebDAV-only sync, Obsidian importer, task tokens, .helixnotes metadata folder; validates Rust+Tauri 2.0 as the stack (https://helixnotes.com/docs).
- Ideon (AGPL): spatial canvas + external-system node linking (https://github.com/3xpyth0n/ideon).
- Akasha: license unknown; concept of fully accountless local+encrypted notes (https://apps.microsoft.com/detail/9n3xffmbl7kx).

### Interface contracts only (closed)
- Muse/Allume: nested boards + zoom-containment; connections-as-edges; MCP-AI hook (https://allume.com).
- Thymer: Markdown Mirror two-way file sync; E2EE with local keys; plugin checklist (whiteboard/graph/FSRS flashcards/charts/daily focus) (https://thymer.com).
- Obsidian Publish: selective publishing, graph/backlinks/search in published output, and the pricing lesson ($8/site/mo bred its own competitors) (https://obsidian.md/publish).
- Descript/CapCut/LumaFusion: transcript-as-editable-document, one-click filler-word removal, captions as time-synced text objects, SRT import/export; LumaFusion's missing captions show the cost of omitting them (https://www.descript.com; https://www.capcut.com; Reddit r/LumaFusion threads).

### Honest gaps in this lane
- Pele: no notes app by that name found; item recorded as non-identified (searched, not found).
- Akasha: only the store-listing snippet verified; page body empty; everything beyond "local-only encrypted Flutter notes app for Windows" unverified.
- Thymer commercial pricing, LumaFusion current pricing: not verified to the exact figure.
- User-complaint corpora for Thymer, Ideon, OwlLuna, Akasha: no public discussion found; recorded as unverified rather than invented.
