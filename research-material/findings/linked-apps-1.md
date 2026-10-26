# Linked apps research — Part 1 (product/app websites)

Findings from product sites and reviews. Every claim cited with URL. UNVERIFIED where a page was blocked/JS-shell and only search snippets support it. Project lens: Rust local-first canvas/block notes app with E2EE, handwriting, universal search.

## Anytype — E2EE Notion alternative
- What: local-first, P2P-synced knowledge app built on an object model (types + relations) rather than pages; positions itself as the encrypted alternative to Notion.
- Platforms/pricing: desktop (Win/Mac/Linux) + mobile; free tier with 1GB sync, paid plans from about $9/mo (Builder); app is source-available and the sync protocol is MIT; self-hostable sync server.
- Key features: P2P sync with E2EE, object/type/relation graph model, offline-first, self-hosting.
- Complaints: complexity of the object model, sync setup friction for non-technical users.
- Teaches us: E2EE + P2P sync is commercially viable at consumer scale; an object/type model beats folders for interconnected notes; self-hosted sync server is a wanted escape hatch.
- Sources: https://anytype.io/ https://anytype.io/pricing https://blog.anytype.io/

## Craft — beautiful Apple-native docs
- What: polished notes/docs app with tasks, daily notes, calendar integration and whiteboards, aimed at personal and small-team use.
- Platforms/pricing: Mac/iPhone/iPad, Windows app, web/Craft X browser editor; Free plan, Plus at $7.99–10/mo or about $45/yr.
- Key features: block-based editor, strong export (PDF, Markdown, Word, TextBundle) and share-as-site publishing, native Apple performance.
- Complaints: subscription price for what many see as a personal notes tool; weaker cross-platform parity outside Apple.
- Teaches us: export and publishing quality drives word of mouth; native (non-Electron) feel is a differentiator; blocks without good sync still lock users in.
- Sources: https://www.craft.do/ (fetched vca-1), reviews via https://www.craft.do/blog

## Concepts — infinite canvas sketching
- What: vector-based infinite canvas app for sketching, illustration and spatial thinking with a vector-raster hybrid engine.
- Platforms/pricing: iOS, Android, Windows, ChromeOS (iPad-first heritage); Free tier, Pro $4.99/mo or $29.99/yr, one-time Essentials packs $1.99–39.99, Teams $10/mo per license.
- Key features: editable vector strokes that stay resolution-independent, infinite canvas, precision tools (measurement, scale), iOS gets feature parity first.
- Complaints: parity gaps on non-iOS platforms; pricing tiers confusing.
- Teaches us: handwriting/ink layers should be stored as editable vectors, not flattened bitmaps; hybrid vector-raster rendering is the right engine for a canvas app.
- Sources: https://concepts.app/ (fetched qqg-1), pricing at https://concepts.app/pricing

## Dillinger — free online Markdown editor
- What: browser-based Markdown editor with live preview and cloud sync to GitHub, Dropbox, Google Drive, OneDrive and Bitbucket; no signup needed.
- Platforms/pricing: web only; fully free, open source.
- Key features: live preview, export to PDF/HTML/MD, third-party cloud sync, offline-capable once loaded.
- Complaints: development largely dormant; no mobile apps; single-document focus.
- Teaches us: even a bare-bones editor earns loyalty by writing to formats/platforms users already own (file access over lock-in).
- Sources: https://dillinger.io/ (fetched 9kw-1), https://github.com/joemccann/dillinger

## onenote_parser (Rust crate) — OneNote file format parsing
- What: read-only Rust crate parsing OneNote files (`.one`, `.onetoc2`, `.onepkg`) through the FSSHTTPB/OneStore/MS-ONE layers, exposing sections/pages/contents via a stable `Parser` API.
- Platforms/pricing: library, not an app; MSRV 1.85; features `native-fs`, `backtrace`, `onepkg`; custom `FileSystem` trait enables WASM/in-memory backends.
- Key features: lazy positional reads so multi-GB notebooks parse with a working set proportional to active reads, not file size; supports OneDrive downloads and desktop exports; semver-stable API.
- Complaints: read-only, no writing.
- Teaches us: a direct precedent for parsing competitor formats in Rust with streaming IO; the FileSystem abstraction pattern is worth copying for our own storage layer.
- Sources: https://docs.rs/onenote_parser/latest/onenote_parser/ (fetched fkn-1)

## Ente ML — on-device ML for E2EE photos
- What: Ente's machine-learning layer: face recognition and natural-language "magic search" running entirely on-device over E2EE-encrypted photos.
- Platforms/pricing: part of Ente (photos app); free/open code, paid storage plans.
- Key features: CLIP embeddings and face models run locally (ONNX Runtime Mobile via Flutter plugin); indexes themselves are encrypted and synced so all devices benefit; works offline after indexing; desktop recommended for first index pass; no ML on web client.
- Complaints: first index pass is slow on phones; web client has no search-by-content.
- Teaches us: private universal search is achievable: run embeddings/OCR on-device, encrypt the index, sync it like data; design for a slow first pass with a fast client.
- Sources: https://ente.io/blog/machine-learning/ (fetched fkx-1), https://help.ente.io/

## FigCraft (ArtCraft) — Rust Figma alternative
- What: free, open-source interface-design tool rebuilt in pure Rust; early alpha.
- Platforms/pricing: macOS, Windows, Linux, Web; free, no account, no telemetry, no subscription; needs Rust 1.95+ to build.
- Key features: frames, auto layout, components/variants, real vector networks, prototypes; live collaboration where anyone can host the file from the app or a self-hosted server; 400+ CLI commands with a JSON control channel and MCP server so agents can do anything the UI can.
- Complaints: alpha maturity; needs newest Rust toolchain.
- Teaches us: proof a full collaborative Rust canvas app ships; "every UI action is also a command" is an excellent architecture for testing and agents; self-hostable collab host mirrors what our sync should offer.
- Sources: https://getartcraft.com/apps/figcraft (fetched e6o-1), https://github.com/storytold/figcraft

## Ghost — open-source publishing platform
- What: Node.js platform for publishing (blog/newsletter/memberships) with built-in payments, 0% fees, full JSON API; self-host or hosted.
- Platforms/pricing: self-host free (MIT/Core) or Ghost(Pro) hosting; Markdown in the editor flow.
- Key features: Markdown-first authoring, memberships/Stripe, public JSON API.
- Complaints: not a notes app; heavy ops burden when self-hosting.
- Teaches us: a niche adjacent to ours (Markdown-driven publishing) sustains a healthy open-source business; content-as-files plus an API is a durable model.
- Sources: https://ghost.org/ (fetched pq5-1), https://github.com/TryGhost/Ghost

## (dropped entry) — gitea repo that could not be verified
- What: a Gitea-hosted repo the community linked could not be verified: searches returned only generic Gitea results, and the URL is withheld because the repo owner's handle matches a Discord community member name.
- UNVERIFIED: no claims made; the entry is kept only as a marker that one community link was dead, private, or misspelled.
- Teaches us: nothing; flag to the linker that this URL may be dead, private, or misspelled.
- Sources: search results only (https://gitea.com/explore); direct page UNVERIFIED.

## HelixNotes — local Markdown notes in Rust/Tauri
- What: free, open-source (AGPL) local Markdown notes app: rich editor with source mode, saved as ordinary `.md` files; no account.
- Platforms/pricing: Linux (dnf/apt/AUR/Solus), macOS, Windows, Android (F-Droid), iOS/iPadOS; free.
- Key features: Rust+Tauri not Electron; tasks aggregated from every checklist; `[[wiki links]]` graph; Tantivy full-text search, CJK-aware; Mermaid, KaTeX, daily notes; optional WebDAV sync to your own server; optional AI via Ollama or own key; Obsidian import; version history and auto backups.
- Complaints: WebKit/Tauri rendering issues on some Linux setups (documented GBM workaround).
- Teaches us: closest architectural sibling to our project; shows Tantivy is the pragmatic Rust search choice; proves plain-file mirror + rich editor + mobile is reachable with a tiny team; WebDAV-to-own-server is the minimal credible sync story.
- Sources: https://helixnotes.com/ (fetched upx-1), https://gitlab.com/ArkHost/HelixNotes

## Homebrewery — Markdown to styled homebrew
- What: web tool turning Markdown into D&D homebrew styled like the official Player's Handbook; brews stored in Google Drive.
- Platforms/pricing: web only; free.
- Key features: Markdown-with-custom-CSS pipeline, shareable links.
- Complaints: users have reported losing saved brews (Google Drive storage fragility); no offline mode.
- Teaches us: Markdown plus a rendering pipeline can produce gorgeous output; but delegating storage to a third-party drive without export safety nets costs users their work — our local-first files must remain readable even if sync dies.
- Sources: https://homebrewery.naturalcrit.com/ (fetched zsl-1, empty JS shell — page content partially UNVERIFIED), search coverage https://www.reddit.com/r/UnearthedArcana/

## Lockbook — open-source E2EE notes
- What: open-source E2EE notes app with Markdown notes, SVG drawings and plain folders, built around a Rust core library (lb-rs) with C/Java bindings.
- Platforms/pricing: native on Mac, iPhone, Android, Windows, Linux; CLI with fzf/vim integration; free, sync server optional/self-hostable.
- Key features: E2EE by default, drawing as first-class SVG, native clients sharing one Rust core, invitation-based sharing.
- Complaints: small team pace; sharing model (invitations) surprises some users.
- Teaches us: the "Rust core + thin native shells" pattern for cross-platform notes is proven, including an SVG drawing layer our handwriting could target; E2EE can coexist with a plain folder/file mental model.
- Sources: https://lockbook.net/ (fetched 120-1), https://github.com/Lockbook/lockbook

## Milanote — visual boards for creative projects
- What: web/mobile tool for organizing creative projects as visual boards: notes, images, links, files arranged freely; client collaboration.
- Platforms/pricing: web, iOS, Android; free 100 notes, then $9.99/mo (yearly) or $12.50/mo (monthly); teams $49/mo up to 50 users.
- Key features: drag-anywhere boards, templates, web clipper, comments.
- Complaints: free tier very tight (100 items); pricing stings for individuals; no offline/local mode.
- Teaches us: the "moodboard" use case overlaps our canvas; its friction (cloud-only, tight caps) is exactly the local-first gap we can fill.
- Sources: https://milanote.com/ (fetched gyo-1), https://milanote.com/pricing

## Miro — collaborative whiteboard incumbent
- What: the dominant team whiteboard: infinite canvas with sticky notes, diagrams, templates, AI clustering/summarization, Stickies Capture for physical sticky notes; 100M+ users.
- Platforms/pricing: web/desktop/mobile; free Miro Lite (no signup), paid team tiers.
- Key features: real-time multiplayer, huge template library, AI idea generation and clustering, integrations.
- Complaints: heavyweight and pricey; free tier gutted; cloud-only, poor privacy story.
- Teaches us: real-time multiplayer and templates are the expectations a canvas app meets; AI that clusters/summarizes canvas content is now table stakes; but the market hunger for a private/local-first Miro is real.
- Sources: https://miro.com/whiteboard/ (fetched uk1-1), https://miro.com/pricing/

## MyScript Notes — handwriting recognition leader
- What: consumer app (formerly Nebo) from the handwriting-recognition company of the same name; ICR converts handwriting, math and diagrams to text; also sells an SDK to developers/OEMs.
- Platforms/pricing: SDK licensing (OS-agnostic); consumer apps on iOS/Android/Windows; recognition in 66 languages, UI in 11.
- Key features: best-in-class handwriting recognition, math and diagram conversion, real-time ink.
- Complaints: no RTL language recognition (Arabic, Hebrew, Persian, Urdu absent) despite Arabic-speaking markets; SDK cost for indie devs.
- Teaches us: handwriting recognition is a moat built over 20+ years; for our project, treat HWR as pluggable (SDK or local model), and note the RTL gap as an underserved opportunity for offline recognition.
- Sources: https://www.myscript.com/ (pricing page jil-1, JS shell — partially UNVERIFIED), https://www.myscript.com/notes/

## Noteshelf (+ noteshelf3-android) — one-time-purchase handwriting app
- What: handwriting note-taking app by Fluid Touch: ink on PDFs and notebooks, handwriting-to-text, audio recording synced to notes, AI summarize/translate (v3).
- Platforms/pricing: iPad/iPhone/Mac $7.99–9.99 one-time (v2/v3) plus optional Noteshelf 3 premium ~$29.99/yr with AI credits; separate Android/Windows apps (noteshelf3-android); free tier of 3 notebooks; 200+ templates.
- Key features: PDF annotation, rich pen engine, Google Drive sync on Android, OCR handwriting-to-text.
- Complaints: the v3 subscription/credits split confuses and angers long-time one-time buyers; Android parity lags iPad.
- Teaches us: converting a one-time purchase into a subscription over AI features is a reputational risk; our AI should be bring-your-own/local like HelixNotes; handwriting apps live or die by pen latency and PDF import.
- Sources: https://noteshelf.co/ (fetched x9o-1), Android: https://noteshelf.co/noteshelf-3-android/, pricing https://noteshelf.co/pricing/

## Notion — the incumbent being displaced
- What: AI-first all-in-one workspace (blocks + databases + agents); claims 100M+ users; Notion AI, Enterprise Search, MCP connectors, Custom Agents.
- Platforms/pricing: web/desktop/mobile; free tier, AI as paid add-on, per-seat business plans.
- Key features: block editor, relational databases, AI agents writing/acting in pages, MCP for external tools.
- Complaints (well known): cloud-only, no real offline, weak E2EE, slow on big pages, export only as lossy Markdown/CSV.
- Teaches us: blocks + databases define the feature bar; the AI-agent direction shows where the market goes; but its weaknesses (offline, E2EE, file ownership) are precisely our thesis.
- Sources: https://www.notion.com/ (fetched jk9-1), https://www.notion.so/pricing

## OneNote (web) — freeform canvas incumbent
- What: Microsoft's notebook app: notebook > section > page > subpage hierarchy with a freeform canvas per page; co-editing; cloud API since 2014.
- Platforms/pricing: web/desktop/mobile; free with Microsoft account.
- Key features: absolute-positioned content on pages, ink support, section hierarchy, Microsoft Graph/OneNote API.
- Complaints: sync conflicts and multi-platform client fragmentation; local notebooks (`.one`) decoupled from cloud sync.
- Teaches us: the section/page/subpage hierarchy is still the most-cloned structure; OneNote's freeform canvas is the UX our handwriting users will expect; the onenote_parser crate makes importing its files feasible.
- Sources: https://onenote.cloud.microsoft.com/ (fetched zee-1, empty JS shell — structure UNVERIFIED here), https://learn.microsoft.com/en-us/office/client-developer/onenote/onenote-home

## OpenAlternative Notion directory — competitor map
- What: curated directory of Notion alternatives on openalternative.co; fetched in full; a map of the local-first/E2EE notes field.
- Key findings: strong local-first cohort — AppFlowy (block editor + databases, offline, self-host), AFFiNE (local-first, edgeless whiteboard + blocks), Logseq (outliner, plain Markdown, 150+ plugins, encrypted sync), SiYuan (block-level bidirectional links, flashcards, E2EE sync), Anytype, Memos (MIT, self-host), Colanode (CRDT local-first), Beaver Notes (offline-first, bring-your-own sync), SilverBullet (Lua scripting, queries); E2EE cohort — Notesnook (XChaCha20, Argon2, self-hostable sync), Justnote (Web3/Stacks); team wikis — Outline, Docmost (MCP), Huly, XWiki; Macro stands out: Rust backend, CRDT, agent cursors, markdown-native.
- Teaches us: CRDTs and local-first are the category's converging bet; markdown-native + agent-facing (MCP, cursors) is the emerging differentiator; our planned stack sits squarely on the trend.
- Sources: https://openalternative.co/to/notion-alternatives (fetched 3tu-1)

## Poznote — self-hosted file-based notes
- What: self-hosted browser notes app (PHP/SQLite per coverage) with Markdown + rich text, Kanban/tasks/dashboards/graph modes, AI integration, PWA, browser extensions, auto backups.
- Platforms/pricing: self-hosted web; free/open.
- Key features: notes stored as HTML/Markdown files on the filesystem; Obsidian vault import via ZIP; auto-merge for concurrent Markdown edits.
- Complaints: PHP self-hosting audience only; no native apps.
- Teaches us: even a self-hosted web app wins points by keeping notes as plain files on disk and by shipping a Markdown auto-merge — both directly relevant to our sync design.
- Sources: https://poznote.com/ (search coverage hrz-1..; direct fetch not performed — features from search snippets, partially UNVERIFIED), coverage at https://korben.info/poznote.html

## Proofeditor.ai — agents as document collaborators
- What: collaborative document editor designed for humans and AI agents sharing one doc: live presence for agents (X-Agent-Id header), comments, suggestions, and provenance showing who wrote what.
- Platforms/pricing: web; agent-installable via SKILL.md; integrates with Claude Code/Codex/OpenClaw.
- Key features: agent presence/comments/suggestions, provenance tracking, shared live document.
- Complaints: niche, early.
- Teaches us: the next collaboration axis is agent-vs-human provenance; our block model should carry an author/provenance field per block from day one so agents can contribute visibly.
- Sources: https://proofeditor.ai/ (fetched hap-1), https://github.com/proofeditor

## Thymer + Markdown Mirror — two-way plain-file mirror
- What: real-time multiplayer workspace app that mirrors the whole workspace as plain Markdown files on your disk in two-way sync; "the Markdown is for your tools, not your team"; desktop apps Win/Mac/Linux; self-hosting coming soon; MCP/CLI with `--markdown-mirror <path>`; pricing TBD.
- Key features: local .md folder is a live reflection, editable by any local tool or agent even offline; changes flow back to the workspace.
- Complaints: young product, pricing unannounced.
- Teaches us: the single most directly relevant idea in this batch: a two-way live mirror between our block/canvas store and plain Markdown files solves "block app with file access" — design the mirror early, not as an afterthought; note their explicit framing that mirror files serve tools/agents, not the UI.
- Sources: https://thymer.com/markdown-mirror (fetched cw0-1), https://thymer.com/

## Trilium — power-user hierarchical notes
- What: free, AGPL, offline-first hierarchical notes app with cloning, labels/relations, hoisting/workspaces; sync via self-hosted server; single-user.
- Platforms/pricing: desktop (Win/Mac/Linux), web UI, PWA mobile (unofficial TriliumDroid); free, no account.
- Key features: note revisions, protected notes (per-note AES-128-CBC), OCR feeding search, web clipper, REST API, JS scripting, AI opt-in with own keys + MCP; SQLite storage (not plain files); scales to ~100k notes.
- Complaints: single-user, no real-time collaboration; SQLite blob storage means no other tools can read notes directly; PWA mobile feels second-class.
- Teaches us: power users want revisions, scripting, OCR-search and protected notes — cheap to plan as block features; but SQLite-only storage is a recurring regret: keep our format file-accessible like Trilium's users demand; per-note encryption is the pragmatic E2EE granularity.
- Sources: https://trilium.codes/ (fetched ip2-1), https://github.com/zadam/trilium
