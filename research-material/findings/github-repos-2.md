# GitHub repos — Part 2 of 2 (findings)

Project: Rust local-first canvas/block notes app with E2EE. This file covers repos H–Z of the scan list (Part 1 is in github-repos-1.md). EXCLUSION applied: no getbb.app / "bb" ecosystems covered. All claims are cited to the URL they came from; anything not confirmable is marked UNVERIFIED.

---

## 1. hughhowey/neo (NEO)

What it is: A distraction-free novel-writing tool "created by a novelist" — a word processor that understands it is writing books and nothing else. Free, no accounts or subscriptions.
Stack: Ships as macOS .dmg (Intel + arm64), Windows installer/portable .exe (self-updating), Linux AppImage. Source language not stated on the README page fetched (binaries distributed via Releases), so language UNVERIFIED.
Maturity: Actively distributed with installers for three platforms and a user base of writers; exact star/commit counts not visible on the fetched page. Free with a "buy me a coffee" style funding model not confirmed on page — UNVERIFIED for funding.
Key features: Library rendered as a bookshelf with labeled shelves, drag-and-drop, cover art and progress bars tied to word goals. Manuscript pages look like books: automatic chapter renumbering, drop caps, curly quotes/em-dash/ellipsis auto-correction, spellcheck only on demand. Keyboard-driven writing flow (one Enter = paragraph, two = `***` section break, three = new chapter). A "Darlings" tab that parks cut passages and restores them to the exact original spot. Placeholders: a hotkey drops a mark + sticky note mid-flow, collected into a to-do panel. Outline tab shows the book as index cards; a card's note appears in the manuscript as a gray ghost paragraph that follows the writing until dismissed; dragging a card moves the text.
Relevance to our project: A model of opinionated local-first UX — plain files on disk, zero accounts, everything editable, and metadata (progress, goals, outline cards) layered over plain text without a database. The index-card outline ↔ document two-way binding is a small canvas-adjacent pattern worth noting. Also a reminder that niche vertical apps (novelists) sustain loyal local-first users.
Sources: https://github.com/hughhowey/neo

---

## 2. johansan/notebook-navigator (Obsidian plugin)

What it is: An Obsidian community plugin that replaces the file explorer with a fast notes browser "inspired by Apple Notes, Bear, Evernote and Day One" — folders, tags, properties and shortcuts in one view, with a dual-pane layout.
Stack: TypeScript, React; virtual scrolling with TanStack Virtual; storage across IndexedDB, Local Storage and an in-memory cache; quality tooling: ESLint (official Obsidian plugin), Prettier, Vitest, CodeQL scans; a production build with zero errors/warnings required before merges.
Maturity: Very actively maintained and documented (public API reference, theming guide, startup process, metadata pipeline, storage architecture, rendering architecture docs with Mermaid diagrams); multi-lingual README (21+ languages). Star count not visible on fetched page — UNVERIFIED, but the docs depth implies a mature project.
Key features: Scales to 100,000+ notes; visual previews; full keyboard navigation (all shortcuts remappable, VIM-style keys); mobile-optimized; folder notes; manual sort mode with keyboard reordering; per-setting "sync" toggles that decide whether a setting is stored locally or shared across devices; a documented network/diagnostics disclosure listing every HTTP request the plugin makes.
Relevance to our project: The docs themselves are a blueprint: a startup/boot process doc (cold vs warm boot, metadata cache), a metadata pipeline (cache rebuild, provider stages), and a storage architecture doc (which store holds what) are exactly the operational docs a local-first app needs. Performance approach (virtualization + cache tiers) matters if our app targets large vaults. The "switching guides" for Evernote, Apple Notes, Bear, OneNote and Day One tell us where users actually migrate from — the same list we should target with importers.
Sources: https://github.com/johansan/notebook-navigator

---

## 3. jpzk/opensidian

What it is: "Open-source and non-profit under GPLv3, vault-compatible cross-platform markdown notes app"; a privacy-first platform for knowledge management and collaboration. Explicitly a clean-room functional clone of Obsidian: reimplements Obsidian's behavior from the outside, contains none of its code, and is not affiliated with Obsidian/Dynalist.
Stack: Rust + Tauri v2 (WebKitGTK 4.1 webview on Linux); Rust 1.98 build; Nix flake in-repo.
Maturity: v0.8.1 release; README documents fresh-install tests on Fedora 44 and Ubuntu 26.04 LTS dated 2026-10-25 and build tests dated 2026-10-03 — under heavy development and very fresh; explicitly recruiting Linux distribution maintainers.
Key features: Obsidian-vault-compatible markdown notes; Linux packaging breadth: slim AppImage, portable AppImage (WebKit bundled), Flatpak (GNOME runtime), RPM, DEB, Nix; reproducibility/security hygiene: SHA256SUMS signed with a published GPG key, per-distrowebkit dependency instructions, locked cargo build (`--locked`).
Relevance to our project: This is the closest live reference implementation of "Obsidian clone in Rust + Tauri" and a checklist for our own distribution story (AppImage variants, flatpak, rpm/deb, nix, GPG-signed checksums, `cargo build --locked` docs). Note the WebKitGTK dependency pain it documents — an argument for our own GUI shell (like Meridian/CapsuleCraft below) or for accepting the webview cost consciously. Clean-room cloning is also a legal pattern worth remembering.
Sources: https://github.com/jpzk/opensidian

---

## 4. kostyk348/CapsuleCraft (a.k.a. capsuleos)

What it is: A "zero-database, pure-MIME multimodal workspace and personal knowledge engine. Every note is an RFC 5322 .eml file." A local-first note editor and planner with no database, no cloud, no accounts. https://github.com/kostyk348/capsuleos redirects to this repo (it is the same project; renamed to CapsuleCraft at v1.5.0 — the /tree/main URL is the same repo root).
Stack: Native shell is Rust + egui (no webview, glibc-only, ~11 MB AppImage); legacy web/Tauri builds still published (Windows MSI/NSIS, Linux deb needing libwebkit2gtk-4.1); MIT license; 98 Rust unit tests in the native shell plus 151 Vitest tests in the legacy web engine.
Maturity: Extremely fast iteration: v1.0.0 2026-08-16 (first Tauri release) → v1.5.0 rename + native egui shell 2026-10-23 → v1.6.0 native standalone AppImage 2026-10-25 → v1.7.0 built-in FAQ 2026-10-25. Pre-1.0 in spirit but shipping monthly+.
Key features: Block editor (headings, paragraphs, task lists, callouts, code blocks, CSV datagrids, audio-attachment notes) with autosave, undo/redo and `.eml` round-trip; `[[wiki links]]` with live backlink index and rename rewrites all links; Okapi BM25 full-vault search with Cyrillic-aware folding plus "related by meaning" tf-idf cosine ranking; planning (tasks aggregated to Agenda/Kanban/Gantt with dependency arrows and cycle protection, RFC 5545 ICS export); real email threading — replies are child .eml files with In-Reply-To/References; datasets as MIME parts addressed by Content-ID; import via drag-drop .eml, IMAP, or Obsidian vault migration (`--import-obsidian`); MCP server exposing the vault to AI agents; offline deterministic "Co-Thinker" critique engine, no API keys.
Format: the "capsule" is a multipart MIME message: headers carry tags (X-Capsule-Tags), a `blocks.json` JSON part is the structured block canvas, extra MIME parts are datasets/attachments addressed by Content-ID, threading rides standard mail headers. Comparison table positions it against Obsidian/OneNote/Notion on lock-in, git/grep/r-sync-ability and offline; an honest LIMITATIONS.md lists gaps (no code execution/audio in native shell yet, best-effort folder watching, capsules not GPG-encrypted).
Relevance to our project: Highly relevant. It is a young Rust local-first block notes app proving three things we care about: (1) plain open-standard storage (like our Markdown) can still host a block model — the JSON block canvas travels as one MIME part while attachments travel as others; (2) a Rust+egui native shell with no webview is viable at ~11 MB; (3) its roadmap literally includes "GPG-encrypted capsules" and "optional end-to-end-encrypted vault sync (tamper/censor-proof, still zero-cloud)" — direct evidence that E2EE sync is the next feature users expect in this category. The BM25 + tf-idf local search stack and Obsidian importer are also directly reusable ideas.
Sources: https://github.com/kostyk348/CapsuleCraft (also reached via https://github.com/kostyk348/CapsuleCraft/tree/main and https://github.com/kostyk348/capsuleos — same repo/redirect)

---

## 5. langergitanu/MyScript

What it is: Not a code fork of MyScript the company. It is a reverse-engineering documentation project: notes and specs decompiling MyScript's pen-input protocol and the MyScript .notes file format, with the stated goal of building a free, independent note-taking app that supports the format. The README mirrors http://web.mit.edu/kathawala/notes.html and links the author's own ThunderNotes project and a `thunder-format-proposal.md` format proposal. So: documentation/reverse-engineering repo, not an application.
Stack: Documentation (Markdown). No application code observed on the fetched page.
Maturity: Small personal research repo; no stars/releases visible on the fetched page — maturity effectively UNVERIFIED beyond content.
Key features (as documentation): analysis of MyScript's ink data structures and sync/protocol behavior, plus a proposed open format ("thunder-format-proposal") for storing handwriting independently of MyScript.
Relevance to our project: Two lessons. (1) Proprietary ink/handwriting formats are a lock-in pain point serious enough that users reverse-engineer them — if our canvas supports pen ink, an open, documented ink format and an import path from proprietary ones is a differentiator. (2) The same author community that builds notes apps also builds format proposals — there is appetite for an open handwriting/canvas format standard.
Sources: https://github.com/langergitanu/MyScript

---

## 6. OfficeIMO fork (unreachable, handle withheld)

What it is: UNVERIFIED — a repository under a community member GitHub handle could not be found via two searches; the handle matches a Discord community member name so it is withheld here, and no OfficeIMO repo surfaced for it. Per the coordinator's hypothesis it is presumably a fork of EvotecIT/OfficeIMO (the upstream that all searches surface), which is an MIT-licensed, COM-free .NET library family for creating, reading, editing, converting, rendering and extracting Office, PDF, email, OneNote and text formats (works without MS Office automation; 79+ forks; releases as recent as 2026-07-27 including an OfficeIMO Studio desktop tool). Other visible forks: SaintPistachio/OfficeIMO, SimonCropp/OfficeIMO, GerHobbelt, Zacgoose.
Stack (upstream): .NET / C#, MIT.
Maturity (upstream): actively released through 2026.
Relevance to our project: skipped deep analysis per instructions (likely fork). Tangential relevance only: the upstream handles OneNote formats, which matters to OneNote-migration tooling in general.
Sources: search results for the OfficeIMO fork (no repo found); https://github.com/EvotecIT/OfficeIMO

---

## 7. maxwhipw/marmalade-tts-android

What it is: A native Android text-to-speech app with on-device neural voices and emotion-aware prosody — sister project to a Linux CLI (marmalade-tts). Positions itself as "the missing middle" between Google's data-hungry default and robotic FOSS engines.
Stack: Android (Kotlin implied); implements Android's standard TTS engine interface so it is a system-wide drop-in replacement for Google/Samsung TTS; source MIT, but the released APK compiles in espeak-ng (GPL-3.0-or-later), making the APK a GPL-3.0 combined work — a deliberate licensing structure to satisfy Google Play's no-runtime-code-download rule.
Maturity: Small personal OSS project; distributed via F-Droid (reproducible builds), GitHub Releases (fdroid-flavor APK) and Obtainium. Star count not visible on fetched page — UNVERIFIED.
Key features: On-device neural voices (Kokoro engine; a fast English "Kitten Nano" voice bundled in the APK, bigger engines download on demand from pinned hostnames into app-private storage); cloud voices strictly opt-in with the user's own API key (Venice.ai, OpenAI) and documented in PRIVACY.md; per-app voice routing via aliases (each app gets its own voice/speed/effects); 8 languages with auto-detection; TalkBack/WCAG 2.1 AA accessibility; 22 voice-effect presets plus editor; foreground playback service with lock-screen/Bluetooth controls; share-sheet and "read selection" integration.
Relevance to our project: Mostly a privacy-engineering pattern source rather than a notes competitor. Teaches: (1) on-device AI/audio as a headline privacy feature with opt-in cloud as a clearly fenced exception; (2) download-on-demand models from pinned hosts into app-private storage — the right pattern if we ever ship local whisper-ish features; (3) reproducible F-Droid builds as a trust channel; (4) if our notes app gains audio (voice notes, reading notes aloud), an on-device TTS integration path exists in the ecosystem.
Sources: https://github.com/maxwhipw/marmalade-tts-android

---

## 8. nostr-protocol/nostr (Nostr protocol)

What it is: The protocol spec repo for Nostr — "Notes and Other Stuff Transmitted by Relays": "the simplest open protocol that is able to create a censorship-resistant global 'social' network". It is not a social app but a message protocol: each person publishes notes to multiple relays (simple servers, anyone can run one, any policy), followers fetch from relays, and every note is signed with the author's keypair so relays cannot forge content. Discovery of which relays hold which person's notes ("outbox model") is the acknowledged hard part, with heuristics and NIP-65 relay lists addressing it.
Stack/spec: Protocol definition + NIPs (Nostr Implementation Possibilities) documents; repository is public domain. The NIP list is large (100+) and explicitly a menu, not a checklist — apps pick the subset they need.
Key NIPs relevant to notes/E2EE: NIP-01 (basic protocol flow), NIP-04 Encrypted Direct Message (marked unrecommended/deprecated in favor of NIP-17), NIP-17 Private Direct Messages, NIP-40 Expiration Timestamp, NIP-42 Authentication of clients to relays, NIP-44 Encrypted Payloads (versioned), NIP-49 Private Key Encryption (ncryptsec), NIP-50 Search Capability, NIP-51 Lists, NIP-59 Gift Wrap, NIP-65 Relay List Metadata, plus content-ish ones (NIP-23 Long-form Content, NIP-54 Wiki, NIP-37 Draft Events).
Maturity: The protocol and NIP process are mature and actively maintained (deprecations are marked inline with reasons).
Relevance to our project: Nostr is a credible sync/backup transport for a local-first notes app that wants to avoid building and trusting its own server: notes (or E2EE blobs) can be published to any relay the user picks, signatures give integrity, NIP-65 gives relay discovery, NIP-40 gives TTLs. E2EE primitives exist at the protocol level (NIP-44 versioned encryption + NIP-59 gift wrap sealing + NIP-49 key encryption), though they are oriented to messaging, so encrypting a whole note vault would be our own layer on top (e.g. kind-generic encrypted payloads addressed to self). Cost: no query/CRDT story — Nostr gives at-least-once delivery and signed events, not multi-device merge; we would still need CRDTs locally and would use Nostr as transport only.
Sources: https://github.com/nostr-protocol/nostr and https://github.com/nostr-protocol/nips/blob/master/README.md

---

## 9. realbynl/Meridian-Notes

What it is: "A fast, themable, native note editor written in Rust. No web technologies and no terminal: it draws its own window." Notes are plain Markdown files readable in any other editor. Version 0.2, with a ROADMAP.md and BACKLOG.md.
Stack: Rust (crates/ workspace in repo), own GUI toolkit (docs/ui-toolkit.md describes self-drawn title bar, ribbon, menus, command palette, dialogs), Wayland stylus support, MIT license.
Maturity: Early: 3 stars, 0 watchers, test releases (v0.2.0-test1, "early, unsigned, may crash, lose data"). Solo project.
Key features: Editor: rope-based buffer, multiple cursors, macros (record/play/save), split views, vim mode, spell check, lint, git gutter, syntax highlighting, time-travel history scrubber, focus mode, typewriter scrolling. Notes: `[[links]]`, scrollable/collapsible `{{embeds}}`, backlinks sidebar, hover preview, goto-anything, templates. Views: an "Endless canvas" where notes with a layout file open as free-positioned text boxes; graph view (`--graph`); pen ink on the canvas and inside Markdown notes, saved as SVG; touch gestures. Study: cloze cards `{{c1::text}}`, card review, quizzes, Anki import/export (TSV, APKG), exam forecast. Extensibility: out-of-process plugins on a stable protocol (panels, commands, key bindings); rebindable keys via keys.conf; skins with hot reload where every color is a role.
Relevance to our project: The most architecturally similar project found in this batch: Rust, own GUI (no webview), Markdown files, canvas + ink + links + plugins. Takeaways: (1) ink saved as SVG inside a Markdown note is a clean file-format answer for pen input; (2) out-of-process plugins over a stable protocol avoids embedding a scripting runtime; (3) the "layout file turns a note into free-positioned canvas boxes" is a lightweight alternative to full canvas documents; (4) study/flashcard tooling is an unexpected but plausible differentiator for note apps; (5) building your own GUI toolkit is a very large time sink — Meridian's breadth vs its 3 stars shows the cost.
Sources: https://github.com/realbynl/Meridian-Notes (and its v0.2.0-test1 release page)

---

## 10. shardulvs/xnotes-android

What it is: A handwriting notes and sketching app for Android with stylus support — pressure-sensitive ink, PDF annotation, notebooks and an infinite canvas.
Stack: Kotlin + Jetpack Compose, Material 3; NDK 27 + CMake for the native stroke engine; needs JDK 17 to build. MIT license. Listed on F-Droid (com.xnotes), GitHub Releases (signed APK) and Google Play; GitHub and F-Droid ship the same signed APK so users can switch without reinstalling.
Maturity: Active: 269 stars, 33 forks; releases up to v0.8.23; README updated 2026-10-11.
Key features: Custom stroke engine turning raw stylus samples into a variable-width ribbon that swells/tapers with pressure; pens and highlighters, neon glow, disappearing ink, shape snapping (draw rough, hold, snaps clean); crisp at any zoom; notebooks AND an infinite canvas ("pages when you want structure, endless space when you don't"); book layouts (single/double/cover, scroll or page-flip); PDF import with margin widening for side notes, text markups, per-PDF color filters that keep photos true-color; dark/OLED modes; real PDF export (vector, selectable text, links, bookmarks); Markdown with live formatting; typed notes with tables, LaTeX, code highlighting; audio recording that replays ink in sync with the lecture; 20+ page templates (Cornell, planners, music staves, isometric); 20+ themes; customizable/floating/dockable toolbar; split view; a real file explorer with grid/gallery/list/column/timeline views.
Storage stance (quoted nearly verbatim because it is the positioning itself): "notes are saved as files in a folder you choose, not locked away in an app's database, so you stay in full control of them"; "open source, no account, no ads, no tracking, no internet access"; "nothing gets flattened, so every stroke can be moved, restyled or erased later."
Relevance to our project: Direct evidence for the mobile/canvas side: users of handwriting apps demand (1) file-based storage in a user-chosen folder as a privacy guarantee, (2) PDF interop both ways, (3) ink that stays editable forever (no flattening), (4) ink synced to audio, (5) templates. The "notebooks or infinite canvas" duality is the same docs-vs-canvas tension AFFiNE solves with one block model. Its three-store distribution with identical APKs is a good publishing pattern.
Sources: https://github.com/shardulvs/xnotes-android (and https://github.com/shardulvs/xnotes-android/blob/master/README.md)

---

## 11. theohbrothers/ConvertOneNote2MarkDown

What it is: A OneNote migration tool: converts OneNote notebooks to Markdown (via pandoc) with media extracted, maintained as a hardened fork of SjoerdV/ConvertOneNote2MarkDown ("Ready to make the step to Markdown and saying farewell to your OneNote, EverNote or whatever proprietary note taking tool...").
Stack: PowerShell (main script ~1,474 lines) driving the OneNote COM API and pandoc; config.example.ps1 for saved configurations including a dry-run mode; docx files as the intermediate representation (naming by page ID or hierarchy); CI releases (v2.23.1 latest).
Maturity: Mature and popular: 766 stars, 84 forks (upstream stats on the fork page); releases through 2024-03 and issues still active through 2026-10.
Key features/issues visible: COM automation requires matching admin elevation (OneNote and the terminal must both run as admin or conversion fails — issue #123); COM class factory errors (issue #102); Windows path quirks (trailing periods in page titles break PowerShell 5 conversions — issue #197); hand-written ink is the hard part: OneNote exports each ink stroke as a separate image without position, and an October 2026 issue (#200) requests merging strokes into a single image, noting that GetPageContent does carry each stroke's position and Ink Serialized Format renderable by WPF — i.e., the data exists but the docx path loses it.
Relevance to our project: Two things. (1) Demand signal: OneNote users are still actively escaping to Markdown in 2026, and a converter with 766 stars is a real adoption funnel for any Markdown-first app — we should plan OneNote import (possibly via this tool or OfficeIMO-style parsing). (2) Ink fidelity is the known gap: handwriting survives migration poorly today; a notes app that preserves ink semantics (position + strokes) on import would be genuinely differentiated.
Sources: https://github.com/theohbrothers/ConvertOneNote2MarkDown (repo page, releases, and issues #102, #123, #197, #200, #204)

---

## 12. thiagovasconcelosti/opensidian

What it is: A separate project, NOT a fork of jpzk/opensidian — same name, entirely different code, stack and license. Its README describes an "open-source knowledge management system inspired by Obsidian" with graph indexing, real-time sync and plugin support; MIT license.
Stack: Node.js 20+ / TypeScript / Express backend; React 18 + Vite + React Router frontend; D3.js force-simulation knowledge graph; marked + front-matter for Markdown; WebSocket (ws) for real-time sync; @modelcontextprotocol/sdk for an MCP server; Vitest (79 tests, >80% coverage); GitHub Actions CI (Windows/Mac/Linux); Docker multi-stage.
Maturity: Young solo project (searches show no community); well-engineered for its size (tests, CI, docs/architecture folder).
Key features: Multiple vaults; markdown editor with live preview and `[[wikilink]]` support; interactive D3 graph; JWT auth with persistent sessions; themes with a visual editor; plugin API with hooks (`note:pre-save`, `note:post-save`) and command registration; a full REST API (auth, vaults, notes CRUD, graph neighbors, ranked full-text search with tag/date/backlinks filters, themes); MCP server so AI tools can read the vault; Docker deployment.
Comparison with jpzk/opensidian: jpzk = GPLv3, Rust + Tauri v2, desktop, clean-room Obsidian clone, vault-compatible, packaging-heavy, no server. thiagovasconcelosti = MIT, TypeScript server+web, cloud-ish architecture (server, JWT, WebSocket), no Obsidian vault compatibility claim. They are unrelated projects sharing a name; a third, EpicenterHQ/epicenter, also appears under the opensidian name in search results, plus Morglaf/opensidian (a genuine fork of jpzk's, publishing experimental Windows builds).
Relevance to our project: (1) Name collision risk is real when naming a notes app. (2) Two more independent projects are adding MCP servers to notes vaults — AI-agent access to local knowledge bases is becoming a standard expectation, worth a design slot in our architecture. (3) Its hook-based plugin API (`note:pre-save`) is a minimal, sane plugin surface.
Sources: https://github.com/thiagovasconcelosti/opensidian/blob/main/README.md (and search results contrasting it with https://github.com/jpzk/opensidian)

---

## 13. toeverything/affine (AFFiNE) — KEY REFERENCE

What it is: "There can be more than Notion and Miro." An open-source, privacy-focused, local-first alternative to Notion & Miro where docs, canvas and tables are hyper-merged. The flagship open-source example of exactly our product category: block notes + edgeless canvas in one app.
Stack: TypeScript frontend (React, Electron, Vite, Jotai state); editor stack is BlockSuite (toeverything/blocksuite), a standalone toolkit of web components with two first-party editors — PageEditor (block-based document editor) and EdgelessEditor (graphics editor with opt-in canvas rendering that shares the same rich-text capabilities as PageEditor); CRDT layer is Yjs on web plus y-octo, a native, high-performance, thread-safe Yjs CRDT implementation in Rust, and OctoBase, the Rust local-first collaborative data engine behind the client/server (napi-rs bridges Rust to Node). License MIT for Community Edition (self-host via Docker); an Enterprise Edition (SSO, rebranding, admin/audit) is planned, and contributors sign a CLA.
Maturity: Very large and active: ~72,985 stars (+1,034 in a recent window), repository age 4 years, latest version v0.27.4, last commit 1 day ago (per openalternative.co listing of the repo); docs at docs.affine.pro; self-hostable.
Block model — the core lesson: everything is a block; a block is "rather an abstract idea in terms of its data rather than a concrete thing — what we are dealing with is normally the 'views' of blocks." The same block can be referenced, embedded and linked into different places and views and "it is always the same block." Basic blocks (text, headings, code, quote, divider, lists) are rich-text-derived ("virgo" in BlockSuite) with markdown shortcuts; converting blocks preserves content and meta — e.g. select to-dos and "convert into database" turns them into a kanban. Notes carry a display mode of DocOnly / EdgelessOnly / DocAndEdgeless ("both") — i.e., the data model explicitly supports a block living in a document, on the canvas, or both. The edgeless canvas accepts any block type: rich text, sticky notes, embedded web pages, multi-view databases, linked pages, shapes, even slides — "Docs and whiteboard are now fully merged."
Interop: BlockSuite provides persistence via block snapshots and transformers to/from third-party formats such as Markdown and HTML, plus incremental updates, real-time collaboration and decentralized sync via its document streaming mechanism, and cross-document state scheduling with one document reusable in multiple editors. BlockSuite is framework-agnostic (native web components on a minimized vanilla runtime) and still marked early-stage.
Design lineage the project itself cites: Quip & Notion ("everything is a block"), Trello (kanban), Airtable & Miro (programmable datasheets), Miro & whimsical (edgeless whiteboard), Remote & Capacities (object-based tags). Ecosystem also includes AFFiNE AI and prebuilt templates (vision board, Cornell notes, planners — note how many of the top templates are study/planning formats).
Relevance to our project: This is the architecture to study and adapt for Rust:
1) One canonical block graph, many views: implement blocks as pure data with a stable identity, then render doc view, canvas (edgeless) view, kanban/table views from the same data. The NoteDisplayMode Doc/Edgeless/both flag is the minimal mechanism that lets blocks live in both worlds — adopt this idea.
2) Rust CRDT core under a TS/other editor: AFFiNE's y-octo/OctoBase proves a Rust local-first data engine with a JS bridge (napi-rs) is a sound and battle-tested shape; for a Rust-native app we can skip the bridge entirely and use a Yjs-compatible or custom CRDT in-process.
3) Snapshot/transformer layer: keep a formal, tested mapping block-graph ↔ Markdown (and HTML) so files stay plain and import/export is lossless-ish — this is what keeps local-first honest.
4) Block snapshots also give us E2EE-friendly opaque payloads: sync only needs the CRDT update stream, which we can encrypt as a whole (unlike structural formats).
5) Their weak spots to beat: CLA + open-core enterprise split, and the early-stage feel of BlockSuite extension APIs — an opportunity for a fully-permissive, plugin-friendly Rust project.
Sources: https://github.com/toeverything/affine ; https://github.com/toeverything/blocksuite ; https://docs.affine.pro/core-concepts/elements-of-affine/blocks ; https://openalternative.co/affine ; search results for "AFFiNE BlockSuite block model canvas edgeless" (incl. https://betterstack.com/community/guides/linux/affine/ and https://blocksuite.io/api/@blocksuite/affine-model)

---

## Cross-cutting takeaways for the project

- Local-first storage as a stated promise is now table stakes: CapsuleCraft (.eml files), Meridian (Markdown files), xnotes ("files in a folder you choose"), NEO (plain files), AFFiNE ("you always own your data on your disk"). Users phrase it as control, not engineering.
- E2EE sync appears on independent roadmaps (CapsuleCraft: GPG capsules + zero-cloud E2EE vault sync) before it exists in most small apps — building it first is a real differentiator. Nostr (NIP-44/59/49) offers ready E2EE primitives and a relay transport; combine with a local CRDT for merge.
- The docs-vs-canvas problem has a proven answer: one block graph, multiple views, with a per-block display mode (AFFiNE/BlockSuite). A Rust version of this (block model + CRDT + doc/canvas/table renderers, Markdown snapshots for interop) is the architectural core to aim at.
- Rust without a webview is viable and loved (CapsuleCraft ~11 MB egui shell, Meridian's own toolkit) but Meridian shows the toolkit cost; Tauri (jpzk/opensidian) trades that for WebKitGTK pain. Decision point, not a detail.
- Migration funnels matter: OneNote escapees (766-star converter, still active issues in Oct 2026), Obsidian vault import (CapsuleCraft, jpzk), Apple Notes/Bear/Evernote/Day One switchers (notebook-navigator). Ink fidelity is the known failure mode of migration.
- Users expect: AI-agent access to the vault via MCP (two independent projects added it), local search (BM25), templates, plugins over stable protocols, and reproducible/multi-channel distribution with signed checksums.
ution with signed checksums.
cksums.
