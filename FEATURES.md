# Features Master — every note app, every feature, in depth

Compiled from all findings files in `/home/thaura/notesapp/findings/`. One section per app, then per open-source repo, then integration components, then two synthesis sections. Every claim carries its source findings file(s). Nothing here is invented; where a finding was marked UNVERIFIED in the source, that is carried through.

Conventions: (a) Core features merged and deduplicated, grouped by theme (capture, editing, canvas/ink, organization, search, AI, sync, export, collaboration, platform). (b) Standout details are the non-obvious specifics the findings recorded. (c) Wants changed is condensed from the findings.

---

# PART I — APPS

## Goodnotes

(a) Core features:
- Capture/ink: pen and highlighter with ink smoothing; handwriting with ink rendering tuned per device.
- Canvas/ink: PDF and image annotation; "infinite-ish" paper templates; lasso tool; links between notes.
- Editing: handwriting OCR search and conversion; handwriting spellcheck/completion (AI-driven in Goodnotes 6).
- Audio: audio recording alongside notes.
- Organization: notebooks; marketplace content (stickers, planners).
- AI: assist features (summarize, define); handwriting spellcheck/completion.
- Sync: iCloud sync.
- Export: PDF export.
- Platform: iPad/macOS/Windows/web apps (cross-platform).
- Business: subscription tiers (Goodnotes 6).

(b) Standout details:
- Handwriting search across notes plus audio recording "coupled with writing notes" was used by a user through years of law school.
- Links, lasso, and the broad feature set were called the best among iPad notebooks; also rated the most user-friendly iPad notebook with the best handwriting-box search for students.
- G2 reviewers praise quick capture that can be developed later, and a laser pointer for presentations.
- The AI ink-smoothing actually deforms handwriting for some users, tied to Apple Pencil hover behavior; reviewers note Notability and Apple Notes do not do this.
- AI outputs arrive in a generic typed font instead of handwriting, a recurring irritation.
- Sync complaints exist even for iCloud users.

(c) What users want changed: ink that never rewrites what you wrote (auto-correcting smoothing off); forced handwriting completion/spellcheck should be optional; subscription/price creep ("too expensive for how buggy it is"; Windows tiers feel pricey); an end to UI/UX churn ("we don't need new features"); AI output rendered in handwriting rather than typed font. New-app signal from the findings: ink fidelity without a subscription.

Sources: apps-likes-wants.md

## Notability

(a) Core features:
- Capture/ink: handwriting; PDF annotation.
- Audio: audio recording time-linked to ink — tap a stroke to jump to that moment in the recording; annotations made during playback sync back into the timeline.
- Sync: iCloud sync.
- Export: PDF export; export as PDF+audio zip.
- Platform: iPad/Mac.
- Business: Free/Classic/Plus subscription tiers (history of plan changes).

(b) Standout details:
- Time-synced audio is the signature: audio synced to notes called "LIFE CHANGING" for lectures; tapping written text jumps the audio to that moment.
- Minimalist interface people explicitly say they love; several ex-Goodnotes users call it the best handwriting experience.
- The 2021 switch from one-time purchase to subscription is the defining grievance of the app's community, with users demanding refunds.
- Pattern of repeated re-subscription pushes: Plus relaunch in 2024 ("era of bought-for-life Notability is over"), then "remove required paid subscription" threads.
- iCloud sync is locked behind the subscription; notes failing to load reported.
- Heavy moderation/censorship of complaints on their subreddit; the "Classic Plan" restore path was reported broken.

(c) What users want changed: pay once and keep everything; never hold sync hostage behind a subscription; honor the Classic plan; stop repeated re-subscription pushes.

Sources: apps-likes-wants.md

## Noteshelf

(a) Core features:
- Capture/ink: handwriting with tuned pen pressure and ink rendering.
- Editing/canvas: templates.
- Audio: audio recording.
- Export: vector PDF export.
- Platform: iPad/Android/Windows.
- Integration: Evernote push.

(b) Standout details:
- Fountain-pen ink rendering is the standout: "only app to produce a decent fountain pen and my handwriting looks the best"; on par with Samsung Notes.
- Vector PDF export is the deciding feature over Samsung Notes for some users.
- Paid Noteshelf 2 "lifetime" buyers had to pay again for Noteshelf 3 — a lifetime-promise breach pattern the findings flag as a caution for the new app.

(c) What users want changed: true lifetime ownership (no paid v3); catch up on feature lag versus rivals; stronger cloud backup; fix bugs (annotations disappearing, tour restarting every launch, scrolling lag, no web preview); bring the Android version to parity with iPad.

Sources: apps-likes-wants.md

## Amphi

(a) Core features:
- Note that two products share the name. (a) Amphi Notes: free open-source cross-platform plain-text notebook; folders like a file system; image/video insertion; markdown-ish text. (b) Amphi (useamphi.com): closed-source iPad student canvas app.
- Organization: file-system-like folders; the canvas app combines notes, documents, flashcards, timers, calculators.
- AI: embedded AI tutors and study widgets (canvas app).
- Sync: self-hosted sync server or Amphi Cloud (Amphi Notes).
- Platform: cross-platform (Amphi Notes); iPad (canvas app).
- License: Amphi Notes GPL-3.0+; the iPad Amphi AI app is closed source.

(b) Standout details:
- XDA reviewers liked one canvas replacing several student apps; community lives on Discord.
- The self-hosted, own-your-data sync model draws open-source users.
- The app is very small (about 2 downloads/30 days per AppBrain), so there is little recurring praise or complaint data — the findings state this explicitly rather than inventing a consensus.
- Known friction: cannot take notes while a study widget is open on the canvas (a frequent complaint on Amphi's Discord, reported via XDA; marked UNVERIFIED beyond that single writeup).

(c) What users want changed: allow note-taking while a study widget is open on the canvas. New-app signal: open local files plus easy self-hosted sync.

Sources: apps-likes-wants.md

## Evernote

(a) Core features:
- Capture: web clipper (its most famous feature); notebooks/tags.
- Organization: notebooks/tags; reminders; tasks.
- Search: powerful search including text in images.
- AI: AI features recently added.
- Sync: full sync across platforms.
- Platform: veteran cloud archive; now owned by Bending Spoons.
- Business: 51-note free cap under Bending Spoons.

(b) Standout details:
- The web clipper is repeatedly called the best on the market — the thing people still miss after leaving.
- Deep search/archive value: decades of notes retained; users stay for the archive.
- An analysis of app-store reviews found 57% of negative reviews concern price/upsell/AI versus 4% technical faults.
- Layoffs of the entire US team and months of silence followed the acquisition.
- Community mood: WSJ "Evernote is dying" discussion; export/alternatives threads are the most upvoted content.

(c) What users want changed: saner pricing after the 2022 acquisition ("over priced for a note taking app"; a 32% increase reported by leavers); less upsell pressure; a free tier big enough for casual use ($242/yr to stay at the "casual user limit" was called too small); a trustworthy archive you own forever. New-app signal: a trustworthy archive priced sanely, with a clipper as good as Evernote's.

Sources: apps-likes-wants.md

## OneNote

(a) Core features:
- Canvas/ink: freeform infinite canvas — place ink, text, and images anywhere; dump a picture or PDF and scribble over it (free-form overlay).
- Organization: notebook/section/page hierarchy.
- Editing: typing/drawing anywhere to think non-linearly; gathering research material on one page.
- Search: OCR.
- Collaboration: sharing and collaboration.
- Sync: OneDrive storage requirement; sync via Microsoft cloud.
- Platform: Windows/web/mobile; free with a Microsoft account.

(b) Standout details:
- The infinite canvas itself is the beloved core: "love Onenote just because of infinite canvas."
- For many users sync is rock solid, one reason they stay — while for others (especially teams) it is the dominant complaint; the findings hold both.
- Pen/touch/keyboard behavior: the input-mode-switching findings record OneNote's automatic mode switching setting (see the dedicated synthesis in Part III and the wish list) — OneNote lets users set pen/touch auto-switching, which the community cites as the reference behavior other apps lack.
- Weak mobile apps and no nested folders in sections; users feel trapped by the format.
- Stagnation: a user left to try everything else and came back "sick of lack of improvements."

(c) What users want changed: fast, reliable sync (conflict spikes for teams); no data loss or stale versions across cached notebooks; speed on complex pages; better mobile apps and nested folders in sections; resumed development. New-app signal: infinite canvas plus sync you never have to think about.

Sources: apps-likes-wants.md, input-mode-switching.md

## Notion

(a) Core features:
- Editing: block editor; pages in pages.
- Organization: relational databases with multiple views; templates.
- Collaboration: sharing/permissions; API/integrations.
- AI: Notion AI.
- Sync: cloud-first; recent per-page offline mode.
- Platform: web/desktop/mobile; proprietary.

(b) Standout details:
- The all-in-one value: "I don't have to open one app to take a small note and then transfer it into another system"; block structure plus linked databases and filters gives one source of truth with different views; databases non-technical people can use.
- Speed complaints are specific and tracked as a worsening trend: large databases and workspaces take seconds to minutes.
- Offline mode is per-page and manual — the community calls it too little too late.
- Memory usage is extreme: 2 pages = 1.5GB reported.
- Workspace chaos: "the tool should not be the work" — hours spent re-organizing.
- Database-view complaints specifics (from the digests): users want faster view switching and better handling of large databases; slow database views are the single most-cited technical failure.

(c) What users want changed: speed for large databases and workspaces; a real full offline mode; data portability (notes are not stored locally — people migrate to Airtable/Obsidian for limits and speed); less memory usage; less re-organization overhead. New-app signal: Notion's flexibility with local speed: instant, offline, and yours.

Sources: apps-likes-wants.md, community-digest.md, thread3-digest.md

## Obsidian

(a) Core features:
- Editing: Markdown vault on disk (plain local .md files); MathJax; canvas (as .canvas files in the open JSON Canvas format).
- Organization: bidirectional links/graph; ~5,000 community plugins; per-vault config that syncs everywhere.
- Search: fast local search.
- Sync: optional paid Sync (E2E-encrypted); fully offline otherwise.
- Export: notes are plain local files — no lock-in.
- Platform: app proprietary but free for personal use; desktop/mobile.

(b) Standout details:
- Plain local Markdown files are the loyalty anchor: your data is never locked in, change tools without rebuilding. A Reddit straw poll on "if Obsidian went database tomorrow" shows how users reason about it ("Right now there's basically zero chance of the app going south like changing note storage formats").
- Fast, offline, great for code+math.
- File-first costs (from thread-b-storage): metadata beyond note content leaks into JSON sidecar files (.obsidian folder: hotkeys, themes, plugins, workspace.json) and a hidden metadata cache (IndexedDB); renaming a note rewrites every file containing a wikilink ("rename fanout"); the canvas is a sibling .canvas file (JSON Canvas, MIT-licensed, spun out March 2024) — positions and edges live there, note content stays in .md files, which is why the canvas↔note bridge works live in both directions for free.
- Community hunger to go beyond .md ("does the use of .md format also doom Obsidian to miss some advanced features? Like a database?").
- Security incidents in the ecosystem: an April 2026 Elastic Security Labs campaign where a crafted vault with a legitimate shell-execution plugin configuration delivered a RAT on vault open; and an RCE in a popular plugin (Tasks) where note frontmatter flowed unsanitized into a `new Function()` evaluator.

(c) What users want changed: Sync price (~$96/yr) feels bad next to free workarounds; no regional pricing or one-time option; checkout defaults to the pricier Sync Plus tier, called misleading; mobile sync friction with free workarounds; plugin dependence on volunteer maintainers. New-app signal: local Markdown plus effortless, affordable sync built in.

Sources: apps-likes-wants.md, thread-b-storage.md, thread-f-editor-platform.md

## Miro

(a) Core features:
- Canvas: infinite boards; sticky notes; diagrams.
- Capture: document/PDF embedding; templates.
- Collaboration: real-time multiplayer; integrations (Azure DevOps etc.).
- Business: paid tiers with board caps.

(b) Standout details:
- Templates plus real-time collaboration for brainstorming and planning; beloved by agile teams for story mapping, retros, technical mapping; template breadth (whiteboarding, mockups, roadmaps, process flows).
- Performance/lag on large or even modest boards, worsening over years — "boards are way laggier and take far longer to load"; lag specifically after inserting documents/PDFs.
- Paid limits and unexpected deletions noted on Trustpilot.

(c) What users want changed: a whiteboard that stays fast as the board grows; fix lag after inserting documents/PDFs; stop UI regressions and unresponsive controls; saner paid limits.

Sources: apps-likes-wants.md

## Milanote

(a) Core features:
- Canvas: drag-and-drop cards on boards; columns; templates.
- Capture: image/file support.
- Collaboration: sharing/collaboration.
- Business: 100-note free cap; ~$100/yr.

(b) Standout details:
- Visual clarity for brainstorming and organizing: "by far my favorite tool for taking notes and saving ideas"; the freeform canvas feels like a wall of sticky notes; desktop boards described as amazing even by critics.
- Mobile app nearly unusable — can't even add boards.
- Boards degrade with many cards; no edit history.
- Export is per-board PDF/PNG/doc only; a formal request exists on their own roadmap poll to "Export your data in a proprietary Milanote format" (i.e., even a full proprietary dump is wanted and not shipped); users complain "No Easy Export / Backup?"
- The 100-note limit drove users to build alternatives.

(c) What users want changed: usable mobile app; fair pricing/bigger free tier; edit history; full export/backup; boards that scale. New-app signal: visual boards that work on every device at a fair price.

Sources: apps-likes-wants.md, thread-b-storage.md

## Anytype

(a) Core features:
- Editing/organization: objects/sets/collections instead of pages; graph + relations.
- Sync: local storage with P2P/local network sync; self-hostable backup nodes; offline-first.
- Security: E2E encryption with user-held keys; keys generated locally; server never decrypts data; no account required.
- Export: Markdown export (improved in 0.47.4, July 2025, to support properties and types).
- Platform: source-available (custom "Any Source Available" license; repos at github.com/anyproto; client code public, not OSI-approved); desktop/mobile.

(b) Standout details:
- Privacy model is the draw: "I love that it's local first... encrypted... powerful. Never had an issue with data loss"; fast pages even with hundreds of items.
- Storage reality (thread-b-storage): the vault is opaque encrypted blobs + index folders — "Files are stored inside flatfs dir in encrypted fragments, so they can't be accessed outside of Anytype"; media streamed on demand and deduplicated. Local-first does not mean plain files.
- Export is the pressure valve and has repeatedly disappointed: a 2024 thread "Export is not great" reports Markdown export dropping everything but names; a 2025 thread says property-rich data makes "the markdown export useless" and "your data will be encrypted and usable only with proprietary Anytype." Release 0.47.4 improved this; a co-founder pushed back on the lock-in charge on the community forum.
- Takeaway recorded in the findings: an object/block store with strong encryption makes a faithful plain-file projection genuinely hard; Anytype's answer has been improving one-way export, not a mirror.

(c) What users want changed: reliable desktop-mobile sync (desktop-mobile sync barely happening, slow sync, synced-flagged items actually unsynced); mobile app quality catching up to desktop; transparent file storage on disk (no plain-file layout like Obsidian's); Notion-grade database features (formulas); a third-party security audit; analytics concerns addressed.

Sources: apps-likes-wants.md, thread-b-storage.md

## Tana

(a) Core features:
- Editing: nested outline built around a daily "dashboards" note.
- Organization: supertags with field/inheritance schema (schema-driven tags); queryable graph.
- AI: AI command bar/agents.
- Capture: web clipper.
- Sync: proprietary cloud database.
- Export: JSON export (full, with Tana-specific structures) and Markdown export (first version arrived 2025, subset-by-supertag, with/without fields).
- Business: paid tiers ~$10–18/mo.

(b) Standout details:
- Supertags "genuinely different from every other tagging or database system"; users miss them in other apps; the outliner model lets you capture everything, tag it, resurface on the day page; "there really isn't anything to replace Tana" for bullet notes.
- Learning curve: "as hard as learning a programming language"; hours to learn; a survivors-only bias noted in reviews.
- Storage (thread-b-storage): vendor lock-in is explicit — "Your data lives in Tana's proprietary format"; a 2023 user: JSON export "is a bit limited" unless you know what to do with it; community tooling (TanaMigrator) converts the JSON workspace export into a vault of markdown files, with the author warning "VERY good chance edge cases exist."
- Performance degrades as the workspace grows.

(c) What users want changed: learnable-in-minutes structure instead of days; a mobile app not too limited for real workspace use; performance at scale; a free tier thick enough to evaluate; less perceived AI push. New-app signal: supertag-like structure learnable in minutes.

Sources: apps-likes-wants.md, thread-b-storage.md

## Reflect

(a) Core features:
- Editing: daily notes flow; backlinks/graph.
- AI: GPT-based AI assistants; voice transcription.
- Capture: web clipper; calendar integration.
- Sync: E2E-encrypted cloud sync.
- Export: reflect JSON, CSV, markdown zip, HTML zip; daily backups to the hard drive.
- Business: ~$10/mo, no real free tier.
- 2026 split: Reflect Open (open-source, local Markdown files, choice of iCloud Drive or Git sync) added alongside maintained Reflect Classic.

(b) Standout details:
- The daily-note workflow "gets a lot of love... calming; you don't have to think about where something belongs"; polish praised ("easy to use and the performance is phenomenal"; does fewer things very well); seamless for journaling.
- Storage story (thread-b-storage): Classic exports are a copy, not a mirror — one user complained you "can only export all your notes in one go"; the notable 2026 move is a cloud block-ish app adding a plain-file sibling product (Reflect Open: "Your choice of sync: iCloud Drive or Git") rather than a mirror of the existing one.

(c) What users want changed: lower price ("$10/month is steep"; alternatives undercut it); fix occasional sync delays; better attachment management ("sucks"); a real Android experience; database/table features Notion users expect.

Sources: apps-likes-wants.md, thread-b-storage.md

## Logseq

(a) Core features:
- Editing: block-level outliner (every line is a block — bullet, indentable, referenceable, embeddable); block references and embeds; drag-anywhere blocks.
- Organization: tasks; queries (Datalog); graph links; whiteboards.
- Extensibility: plugins.
- Sync: optional paid sync; local Markdown/org files as the store.
- Platform: open-source, AGPL-3.0; desktop/mobile.
- New DB version: a database (SQLite) version to fix performance, in public testing through late 2025/2026.

(b) Standout details:
- The block outliner is the loved model: everything has hierarchy, so retrieval pulls whole trees — "far more powerful and intuitive than Obsidian"; users love the Logseq way even while criticising the app.
- Performance collapses on large graphs (1000+ pages) — the app's defining complaint.
- Sync data loss/duplication; fragile two-way sync; a file-writing defect produced unrecoverable data loss (in-app edits never written to ./pages/*.md).
- The encoding cost (thread-b-storage): "Logseq uses Markdown syntax but not every Markdown file is a valid Logseq page, basically because of dashes"; Logseq began inserting hyphens on every line, "breaking MD functionality" (issue #3457); users want "normal markdown files that I can take with me anywhere."
- Logseq's own April 2024 post explains the pivot to a database version: "Creating a new block requires rewriting the entire Markdown file"; "Renaming a page updates all files that reference it"; "structure data support is limited... lacking features like persistent IDs, timestamps"; goals include Datalog queries, offline-first RTC with E2EE, and a long-term goal of "seamless two-way sync between the database and markdown files" — still aspirational two years later. OG is maintenance-only without reaching 1.0; DB users are advised to "enable hourly backups to the filesystem" (the file plane is a backup/export surface, not the store).
- The findings call Logseq the strongest evidence that the file mirror is a goal even the team that wants it has not shipped.

(c) What users want changed: performance that survives 1000+ pages; sync without data loss or duplication; faster development and a finished mobile/sync; clarity on the DB version's trade-offs (SQLite portability, markdown export losing properties worry users). New-app signal: Logseq's outliner power without the performance ceiling, on plain files.

Sources: apps-likes-wants.md, thread-b-storage.md

## Tolaria

(a) Core features:
- Editing: Notion-like WYSIWYG block editor (BlockNote/Tiptap) + raw Markdown mode (Cmd+/); slash commands; [[wikilinks]] with autocomplete and auto-update on rename; Mermaid diagrams; KaTeX math with editable source panel; code blocks with syntax highlighting; editable callouts; sandboxed HTML blocks; colored highlights; todo block shortcut; collapsible headings; table navigation.
- Capture: Inbox section (unorganized notes, Forte-style capture-vs-organize, disableable); note list sortable by any property or file metadata with customizable property columns; cmd+click to open URL/note links.
- Canvas: tldraw whiteboards stored as markdown files.
- Rich content: media/PDF previews (PDF.js), lightbox, spreadsheet notes (plain-text sheets with formulas via IronCalc WASM).
- Attachments: drag-and-drop from Finder, clipboard paste, remote image paste, vault-root or note-relative paths.
- Organization: types as lenses, not schemas — every note has a type (default Note); types are themselves markdown files with icon/color, no required fields or validation; sidebar sections (Inbox, All notes, Archive, types, Pinned/favorites, custom views, folder tree at the bottom); custom views are YAML files in a views/ folder with nested filter criteria, regexes and natural-language dates, and AI can author them.
- Search: command palette (Cmd+K) with semantic matching; keyboard-first design; quick open with create-note-from-search; note body full-text search.
- AI: direct model providers (OpenAI, Anthropic, Gemini, OpenRouter, Ollama, LM Studio, custom OpenAI-compatible endpoints) for chat over note context; CLI agent targets (Claude Code, Codex, OpenCode, Pi, Gemini, Copilot CLI, Kiro, Antigravity, Hermes); dedicated AI side workspace; AI commit-message drafting; AI can create notes.
- Integration: bundled MCP server (Node or Bun) exposing vault tools (create/update/append notes, vault lifecycle); AGENTS file ships for external agents to self-orient; Claude Code skills usable from the AI panel; per-agent model picker; local API keys.
- Sync: Git is the sync layer — in-app commit, push, browse history, per-note version history; AutoGit opt-in mode auto-commits/pushes when idle or on focus shift; mobile syncs via iCloud or Files app sharing the same git repository, auto-commit on save with merge support.
- Multi-vault: multiple vaults, separate app windows per vault, mounted vault workspaces, custom vault order, parent Git repository support, vault deep links.
- Export: PDF export; standalone HTML previews.
- Platform: macOS, Windows, Linux desktop (Homebrew cask + signed installers), iOS/iPadOS beta via TestFlight; ~100K lines of Rust + React, Tauri v2; AGPL-3.0-or-later; free and open source forever, no accounts or subscriptions.

(b) Standout details:
- Files-first vault: notes are plain .md with YAML frontmatter, no database, no proprietary format; folders are secondary; flat-vault friendly.
- Origin: the author migrated 10,000+ notes from Notion to plain Markdown and built the app he wanted; mostly AI-written code (~zero lines written by the author himself); 1900+ commits, 3000+ tests, 70 ADRs.
- Git-first as AI transparency is a loved feature: seeing exactly what the AI changed vs what you wrote, with AI as a git contributor.
- No trash bin — git history is the safety net (a deliberate deletion model).
- AI chats are not persisted in vault files by default.
- Loved: UI polish with real files underneath; the inbox concept; clipboard image paste praised as rare and essential; open source vs Obsidian ("I had no idea Obsidian wasn't open source"; lock-in freedom is the differentiator).
- Emerging (alpha, Oct 2026): a web client ("remote client") with note create/rename/delete, sharing notes/vaults with view-only/revoke, signed access tickets, collaborator Co-authored-by trailers, mobile background sync — a shift worth watching, though desktop remains git/no-server.
- The findings' pull-from assessment: liftable concepts include types-as-lenses, views-as-YAML with natural-language dates, Inbox lifecycle, AutoGit idle/focus heuristics, wikilinks auto-updating on rename, AGENTS-file convention, bundled MCP vault tools, no-trash git-as-safety-net model. Code lifting is binding: AGPL-3.0. Not worth copying: the React/BlockNote editor layer (the project's own weak point per HN bug reports).
- Known bugs to avoid repeating: "last modified" sorting breaks after first git commit (sorts by commit date); code fence requires a space; ctrl-e end-of-line missing; cursor jumps below block after fence creation.

(c) What users want changed: a truly native (AppKit/SwiftUI) app rather than a Tauri/React web-wrapper; feature-creep worry ("stay focused like Bear"); early-bug fixes (blank frozen app; three bugs in five minutes; sort-by-modified issue); editor friction fixes; "AI-first" wording read as humans second-class; large-file editor performance; npm-dependency-in-adjacent-to-home trust concern; mobile demand (largely since addressed); a way to donate/pay at launch; answers to single-maintainer longevity skepticism.

Sources: tolaria.md

## AFFiNE

(a) Core features:
- Editing/organization: "everything is a block — something that could be edited and transformed freely"; doc + whiteboard + databases as views of one underlying store; Edgeless (canvas) mode.
- Storage: BlockSuite documents are a block tree "structured as a tree and stored within a Y.Map" (CRDT), with `sys:id`, `sys:flavour`, `sys:children` — persistent block IDs and parent/child structure with no file concept anywhere.
- Canvas: edgeless documents are isomorphic to page documents — both are block trees, with no data conversion during mode switching; a `surface` block holds all whiteboard elements; "a Page is a type of Database, as is Edgeless."
- Sync: local IndexedDB/SQLite per platform plus sync servers.
- Performance: claims to render thousands of vector shapes and text blocks at 60 FPS without DOM-heavy lag.

(b) Standout details:
- BlockSuite is the one editor core built for the canvas-plus-document hybrid: PageEditor and EdgelessEditor are two views that attach and detach from the same Y.Doc.
- Costs recorded: much smaller ecosystem than ProseMirror/TipTap/Lexical; the framework is young, API churn is real; teams adopting it inherit AFFiNE's product opinions; DeepWiki's architecture notes describe a store→model→view data flow closer to a game engine than an editor library.
- No plain-file story of the Thymer kind exists in BlockSuite (docs do not mention one; UNVERIFIED beyond docs read).
- Edgeless + page as two views of one store is also the control case in the editor-core comparison: "the only core where the brief's requirement is the default behavior."

(c) What users want changed: not recorded in the findings beyond the ecosystem/API-stability cost framing; the findings treat AFFiNE primarily as architecture evidence.

Sources: thread-b-storage.md, thread-f-editor-platform.md

---

# PART II — OPEN-SOURCE REPOS

(Repo sections merge the deep-repos, github-repos and linked-apps findings. Where the findings recorded only repo-level feature lists without user sentiment, (c) reflects that.)

## CapsuleCraft (kostyk348/CapsuleCraft, a.k.a. capsuleos)

(a) Core features:
- Capture/editing: block editor (headings, paragraphs, task lists, callouts, code blocks, CSV datagrids, audio-attachment notes) with autosave, undo/redo and `.eml` round-trip; `[[wiki links]]` with a live backlink index; renaming rewrites all links.
- Organization/search: Okapi BM25 full-vault search with Cyrillic-aware folding, plus a "related by meaning" tf-idf cosine ranking; tags stored in message headers.
- Planning: tasks aggregated to Agenda / Kanban / Gantt views with dependency arrows and cycle protection; RFC 5545 ICS export.
- Threading: real email threading, replies are child .eml files via In-Reply-To/References; datasets travel as MIME parts addressed by Content-ID.
- Import/integration: drag-drop .eml import, IMAP, Obsidian vault migration (`--import-obsidian`); bundled MCP server exposing the vault to AI agents; offline deterministic "Co-Thinker" critique engine with no API keys.
- Platform: native Rust + egui shell with no webview (~11 MB AppImage, glibc-only); legacy Tauri/web builds also published; MIT license; 98 Rust unit tests in the native shell plus 151 Vitest tests in the legacy web engine.
(b) Standout details: the "capsule" is a multipart MIME message: headers carry tags (X-Capsule-Tags), a `blocks.json` JSON part is the structured block canvas, extra MIME parts are datasets/attachments addressed by Content-ID, and threading rides standard mail headers — a proof that a plain open-standard format can still host a block model. Renamed from capsuleos at v1.5.0; v1.0.0 shipped 2026-08-16 and v1.7.0 on 2026-10-25 (monthly-plus iteration). An honest LIMITATIONS.md lists gaps: no code execution or audio in the native shell yet, best-effort folder watching, capsules not GPG-encrypted. The roadmap already names GPG-encrypted capsules and optional end-to-end-encrypted vault sync ("tamper/censor-proof, still zero-cloud") — independent evidence that E2EE sync is the next expected feature in this category.
(c) What users want changed: no user sentiment recorded; visible direction comes from the roadmap (encryption, E2EE sync, audio in the native shell).
Sources: deep-repos-c.md, github-repos-2.md

## Meridian-Notes (realbyln/Meridian-Notes)

(a) Core features:
- Editor: rope-based buffer, multiple cursors, macros (record/play/save), split views, vim mode, spell check, lint, git gutter, syntax highlighting, focus mode, typewriter scrolling, time-travel history scrubber.
- Notes: `[[links]]`, scrollable/collapsible `{{embeds}}`, backlinks sidebar, hover preview, goto-anything, templates; plain Markdown files readable in any other editor.
- Canvas/views: an "Endless canvas" where notes with a layout file open as free-positioned text boxes; graph view; pen ink on the canvas and inside Markdown notes, saved as SVG; touch gestures.
- Study: cloze cards (`{{c1::text}}`), card review, quizzes, Anki import/export (TSV, APKG), exam forecast.
- Extensibility: out-of-process plugins on a stable protocol (panels, commands, key bindings); rebindable keys via keys.conf; skins with hot reload where every color is a role.
- Platform: Rust with its own GUI toolkit (self-drawn title bar, ribbon, menus, command palette, dialogs — no webview, no terminal); Wayland stylus support; MIT license.
(b) Standout details: ink saved as SVG inside a Markdown note is a clean file-format answer for pen input; the "layout file turns a note into free-positioned canvas boxes" pattern is a lightweight alternative to full canvas documents; out-of-process plugins avoid embedding a scripting runtime. Early and tiny (v0.2, 3 stars, test releases described as "early, unsigned, may crash, lose data"), which its own findings read as the cost of building a custom GUI toolkit.
(c) What users want changed: nothing recorded beyond the project's own early-stage warnings.
Sources: deep-repos-c.md, github-repos-2.md

## notecraft (AlienTechSoftware/notecraft)

(a) Core features: privacy-first, local-first storage on device; no cloud account required; cross-platform desktop targets; Markdown-centric notes; a Rust core with the UI layer split on top. Alpha scope is narrow (0.0.6, no published release).
(b) Standout details: dual-licensed MIT OR Apache-2.0, so the architecture (Rust core + separate UI layer, storage layout, local-first sync decisions) is copy-paste friendly; at this maturity it is a design comparison point rather than a usable product.
(c) What users want changed: one visible request, open issue #8 on stylus/palm-rejection input behavior on Linux, opened 2026-10-25.
Sources: deep-repos-a.md, github-repos-1.md

## e-journal (EkarinLB/e-journal)

(a) Core features: local-first, AI-powered journaling desktop app in Rust with the egui/eframe toolkit; encrypted local journal storage; daily entries with calendar/date navigation; mood tracking; tagging; AI-generated summaries of entries using a local model; Markdown export; dark/light theming; ships as a single binary.
(b) Standout details: MIT-licensed and in the same product family as a Rust-first notes app, so the entry-storage schema, calendar navigation, encryption-at-rest approach and export path are directly liftable; twelve beta point-versions shipped by 0.12.0.
(c) What users want changed: nothing recorded beyond the maintainer's own iteration.
Sources: deep-repos-a.md, github-repos-1.md

## neo (hughhowey/neo)

(a) Core features:
- Library: rendered as a bookshelf with labeled shelves, drag-and-drop, cover art and progress bars tied to word goals.
- Writing: manuscript pages look like books — automatic chapter renumbering, drop caps, curly-quote/em-dash/ellipsis auto-correction, spellcheck only on demand; keyboard-driven flow (one Enter = paragraph, two = `***` section break, three = new chapter).
- Revision: a "Darlings" tab that parks cut passages and restores them to the exact original spot; a placeholder hotkey drops a mark + sticky note mid-flow, collected into a to-do panel.
- Outline: the book shown as index cards; a card's note appears in the manuscript as a gray ghost paragraph that follows the writing until dismissed; dragging a card moves the text.
- Platform: free, no accounts or subscriptions; plain files on disk; installers for macOS (Intel + arm64), Windows (self-updating) and Linux (AppImage).
(b) Standout details: the index-card outline ↔ document two-way binding is a small canvas-adjacent pattern worth studying; metadata (progress, goals, outline cards) is layered over plain text without a database; opinionated vertical UX (built by a novelist for novelists) sustains loyal local-first users.
(c) What users want changed: nothing recorded in the findings.
Sources: deep-repos-b.md, github-repos-2.md

## notebook-navigator (johansan/notebook-navigator)

(a) Core features (Obsidian community plugin replacing the file browser and calendar):
- A virtualized two-pane explorer (folder tree + file list) with visual previews, built for very large vaults (100k+ notes target) using TanStack Virtual.
- Smart folders, recent-notes view, AI-style filter search with a filter-search grammar, frontmatter keyword (tag) discovery with included/excluded lists, tag and marker discovery with per-tag/folder icons and colors, calendar navigation, per-folder icons and colors, folder notes, manual sort mode with keyboard reordering.
- Full keyboard navigation (all shortcuts remappable, VIM-style keys); mobile-optimized; a documented settings surface (14 sections).
- Storage across IndexedDB, Local Storage and an in-memory cache; per-setting "sync" toggles deciding whether a setting is stored locally or shared across devices; a documented network/diagnostics disclosure listing every HTTP request the plugin makes.
(b) Standout details: 2,782 stars / 104 forks / 1,072,639 downloads per obsidianstats (5.0 rating), with Reddit/forum word of mouth calling it a real replacement for the default file browser; a case study reports 180 releases and ~zero hand-written LOC (AI-assisted development). The docs are a blueprint in themselves: a startup/boot process doc (cold vs warm boot, metadata cache), a metadata pipeline doc (cache rebuild, provider stages) and a storage architecture doc (which store holds what). Its switching guides for Evernote, Apple Notes, Bear, OneNote and Day One map where users actually migrate from.
(c) What users want changed: no open issues surfaced; the author explicitly does not accept PRs ("no PRs will be accepted") and funnels feature direction into the 1.5 roadmap issue #274.
Sources: deep-repos-b.md, github-repos-2.md

## opensidian

Two unrelated projects share the name; the findings cover both.
(a) Core features (jpzk/opensidian — the primary subject):
- "Open-source and non-profit under GPLv3, vault-compatible cross-platform markdown notes app"; privacy-first knowledge management positioning; explicitly a clean-room functional clone of Obsidian (reimplemented from the outside, contains none of its code, not affiliated with Obsidian/Dynalist).
- Obsidian-vault-compatible Markdown notes; Rust + Tauri v2 (WebKitGTK 4.1 webview on Linux); v0.8.1 with fresh-install tests on Fedora 44 and Ubuntu 26.04 LTS dated 2026-10-25.
- Linux packaging breadth: slim AppImage, portable AppImage (WebKit bundled), Flatpak (GNOME runtime), RPM, DEB, Nix; reproducibility hygiene: SHA256SUMS signed with a published GPG key, locked cargo builds (`--locked`); recruiting Linux distribution maintainers.
- Second project (thiagovasconcelosti/opensidian, MIT, separate codebase): Node.js/Express + React 18/Vite; D3 force-simulation knowledge graph; WebSocket real-time sync; JWT auth; multiple vaults; Markdown editor with live preview and `[[wikilinks]]`; themes with a visual editor; a hook-based plugin API (`note:pre-save`, `note:post-save`, command registration); a full REST API (vaults, notes CRUD, graph neighbors, ranked full-text search with tag/date/backlink filters); an MCP server so AI tools can read the vault; Docker deployment; Vitest (79 tests, >80% coverage).
(b) Standout details: jpzk/opensidian is the closest live reference implementation of an "Obsidian clone in Rust + Tauri" and doubles as a distribution checklist (AppImage variants, flatpak, rpm/deb, nix, GPG-signed checksums); its WebKitGTK dependency pain is an argument for a native GUI shell. Two more independent projects adding MCP servers to notes vaults (this one and Tolaria) mark AI-agent vault access as a standard expectation. Clean-room cloning is a legal pattern worth remembering; the name collision is a naming risk.
(c) What users want changed: nothing recorded beyond maintainer roadmap items (jpzk) and the projects' own docs.
Sources: deep-repos-c.md, github-repos-2.md

## Strata (Niko1221/Strata)

(a) Core features: a local LLM inference engine that runs models on the user's own machine; one-click installer; desktop app plus terminal client; automatic engine/model selection for the user's hardware; GPU offload with CPU fallback; OpenAI-compatible and Anthropic-compatible localhost API endpoints so existing agents and tools can point at local models; a `strata connect` flow that configures those agents; built-in benchmark suite; image generation via a Stable Diffusion CLI companion (`sd-cli`); MIT license.
(b) Standout details: the localhost server speaking OpenAI/Anthropic wire formats is the pragmatic route for private AI features in a notes app (works against any local or remote model); the "auto-pick engine for this hardware" UX and the benchmark-harness discipline (reproducible local benchmarks shipped with the app) both transfer. The issue tracker is the busy part: 439 open issues across labels [TUI], [GUI], [Engine], [Benchmark], [Other], active as recently as 2026-10-26, with community members posting their own benchmark runs on consumer RTX hardware.
(c) What users want changed: nothing recorded at feature level beyond the labeled issue surface above.
Sources: deep-repos-a.md, github-repos-1.md

## xnotes-android (shardulvs/xnotes-android)

(a) Core features:
- Ink: a custom native stroke engine (Kotlin + Jetpack Compose UI, NDK 27 + CMake core) turning raw stylus samples into a variable-width ribbon that swells and tapers with pressure; pens and highlighters, neon glow, disappearing ink; shape snapping (draw rough, hold — it snaps clean); crisp at any zoom; ink never flattened ("every stroke can be moved, restyled or erased later").
- Structure: notebooks AND an infinite canvas ("pages when you want structure, endless space when you don't"); book layouts (single/double/cover, scroll or page-flip); 20+ page templates (Cornell, planners, music staves, isometric); 20+ themes; dark/OLED modes.
- PDF: import with margin widening for side notes, text markups, per-PDF color filters that keep photos true-color; real PDF export (vector, selectable text, links, bookmarks).
- Text/media: Markdown with live formatting; typed notes with tables, LaTeX, code highlighting; audio recording that replays ink in sync with the lecture.
- Shell: customizable/floating/dockable toolbar; split view; a real file explorer with grid/gallery/list/column/timeline views; MIT license.
(b) Standout details: the storage stance is the positioning itself: "notes are saved as files in a folder you choose, not locked away in an app's database"; "open source, no account, no ads, no tracking, no internet access." Distribution: F-Droid, GitHub Releases and Google Play shipping the same signed APK so users can switch channels without reinstalling. 269 stars, 33 forks, v0.8.23, README updated 2026-10-11. The "notebooks or infinite canvas" duality is the same docs-vs-canvas tension AFFiNE solves with one block model.
(c) What users want changed: nothing recorded beyond the project's own roadmap; the feature set itself is the community demand signal (file-based storage, PDF interop both ways, editable ink, ink synced to audio, templates).
Sources: deep-repos-c.md, github-repos-2.md

## diktafon (Lukas-Novak/diktafon)

(a) Core features:
- A fork of jaromiru/diktafon: an open-source voice-memo app organized like cassette tapes, transcribing and summarizing entirely on-device; the fork adds opt-in cloud backup and opt-in cloud transcription to your own server, both off by default.
- Tape metaphor: cassettes as continuous gapless recordings; tap-to-seek transcripts.
- AI: on-device Whisper transcription and Qwen summaries (vendored whisper.cpp + llama.cpp); Silero VAD noise-aware transcription with a rumble filter; auto language detection per memo; per-memo and per-cassette summaries/titles.
- Data: export/import archives; opt-in self-hosted sync with durable retry.
- Platform: Flutter (Android, iOS, Linux); MIT; released on F-Droid, Google Play and the App Store with SHA256SUMS and GitHub build-provenance attestations.
(b) Standout details: a case study in consent-first cloud — everything local by default, cloud strictly opt-in, per-consent fallback after failed local attempts; the "your own server + durable retry" ingest model maps well onto optional E2EE sync; upstream credit reads "designed by Jaromír Janisch, implemented by Claude Code."
(c) What users want changed: nothing recorded beyond the fork's own additions (cloud backup/transcription were built as the answer to that gap).
Sources: github-repos-1.md

## marmalade-tts-android (maxwhipw/marmalade-tts-android)

(a) Core features:
- A native Android text-to-speech app with on-device neural voices and emotion-aware prosody, implementing Android's standard TTS engine interface so it is a system-wide drop-in replacement for Google/Samsung TTS.
- On-device engines: Kokoro engine; a fast English "Kitten Nano" voice bundled in the APK; bigger engines download on demand from pinned hostnames into app-private storage; cloud voices strictly opt-in with the user's own API key (Venice.ai, OpenAI), documented in PRIVACY.md.
- Personalization: per-app voice routing via aliases (each app gets its own voice/speed/effects); 8 languages with auto-detection; 22 voice-effect presets plus an editor.
- Accessibility/integration: TalkBack/WCAG 2.1 AA support; foreground playback service with lock-screen/Bluetooth controls; share-sheet and "read selection" integration.
(b) Standout details: source is MIT but the released APK compiles in espeak-ng (GPL-3.0-or-later), making the APK a GPL-3.0 combined work — a deliberate licensing structure to satisfy Google Play's no-runtime-code-download rule. Distributed via F-Droid (reproducible builds), GitHub Releases (fdroid-flavor APK) and Obtainium. Its value to a notes project is the privacy-engineering pattern: on-device AI/audio as a headline feature with opt-in cloud as a clearly fenced exception, and download-on-demand models from pinned hosts — the right pattern if the app ever ships local speech features (voice notes, reading notes aloud).
(c) What users want changed: nothing recorded in the findings.
Sources: github-repos-2.md

## ConvertOneNote2MarkDown (theohbrothers/ConvertOneNote2MarkDown)

(a) Core features: converts OneNote notebooks to Markdown (via pandoc) with media extracted; a hardened fork of SjoerdV/ConvertOneNote2MarkDown; PowerShell main script (~1,474 lines) driving the OneNote COM API and pandoc; docx files as the intermediate representation (naming by page ID or hierarchy); config.example.ps1 for saved configurations including a dry-run mode; CI releases (v2.23.1 latest); 766 stars, 84 forks, issues still active through 2026-10.
(b) Standout details: the known failure modes are the migration map: COM automation requires matching admin elevation (OneNote and the terminal both as admin or conversion fails, issue #123); COM class factory errors (#102); trailing periods in page titles break PowerShell 5 conversions (#197). Hand-written ink is the hard part: OneNote exports each ink stroke as a separate image without position, and an October 2026 issue (#200) requests merging strokes into a single image, noting that GetPageContent does carry each stroke's position and Ink Serialized Format renderable by WPF — the data exists but the docx path loses it.
(c) What users want changed: exactly those issues — above all ink fidelity; OneNote users are still actively escaping to Markdown in 2026, and a converter with 766 stars is a real adoption funnel for any Markdown-first app. A notes app that preserves ink semantics (position + strokes) on import would be genuinely differentiated.
Sources: deep-repos-c.md, github-repos-2.md

## OfficeIMO (EvotecIT/OfficeIMO)

(a) Core features:
- A family of MIT-licensed, COM-free .NET libraries for creating, reading, editing, converting, rendering and extracting Office, PDF, email, OneNote and text formats, with no Microsoft Office or LibreOffice installation required; dozens of packages, many zero-third-party-dependency by design (OfficeIMO.Core, OfficeIMO.Pdf, OfficeIMO.OneNote).
- Format breadth: Word (.docx plus first-party .doc), Excel (.xlsx/.xls), PowerPoint (.pptx/.ppt/.pot/.pps), Visio (.vsdx family), OneNote (.one/.onetoc2/.onepkg), PDF (create/parse/render/edit/sign, PDF/A-2b, PDF/A-3b, PDF/UA-1, Factur-X, ZUGFeRD validation), OpenDocument (ODT/ODS/ODP/ODG), Markdown (typed AST, HTML/PDF rendering), RTF, AsciiDoc, LaTeX, OPML, DocBook, CSV, EPUB, XPS, DjVu, CHM, iWork (.pages/.numbers/.key reading), Publisher recovery, email formats (EML/MIME, MSG/OFT, TNEF, mbox, PST/OST, OLM, EMLX, Outlook OAB, iCalendar, vCard), Google Workspace and Confluence bridges, invoicing (EN 16931/UBL/Polish FA(3), KSeF submission).
- Tooling: a shared drawing/raster engine with PNG/JPEG/TIFF/WebP/SVG export; OCR hooks; an optional security provider (CMS/S/MIME/RFC 3161/X.509); the OfficeIMO Studio desktop app (Windows/Linux, Apple apps in development) with PDF markup/redaction/forms; a CLI; and an MCP server plus Agent Skills so AI agents can inspect and convert local documents.
(b) Standout details: very active (current v3.5.2 among dozens of rapid point releases; a one-issue open backlog at time of fetch). The pull-from pieces for a Rust project (code is C#, but MIT): OfficeIMO.Markdown's typed Markdown AST with source spans, stable block identities and transforms (a model for lossless round-trip markdown editing); the OfficeIMO.OneNote .one/.onetoc2 reader/writer design, the only mature open implementation of that format family; the "fidelity report / loss preflight" pattern applied to every conversion, worth copying as an import/export UX principle; and the zero-dependency packaging discipline.
(c) What users want changed: one visible open issue (#3171, opened 2026-10-23) about the GitHub experience having an "above the fold" problem; no feature-level sentiment recorded.
Sources: deep-repos-a.md, deep-repos-c.md, github-repos-1.md, github-repos-2.md

## Integration components

(a) Core features and embeddability (all assessments are about embedding inside a local-first, Rust-target notes app; license is the recurring deciding factor):
- OnlyOffice (documents): an office suite — text document, spreadsheet, presentation and PDF editors. The editing core is sdkjs (a JavaScript editor engine); Document Server is a self-hosted server rendering it in a browser and Desktop Editors is a local shell around the same web core. Embedding path is network embedding: iframe + JavaScript API + postMessage (the Nextcloud, Moodle, Odoo and WordPress connectors are all built on it). AGPL-3.0 across Document Server Community Edition and sdkjs, with additional Section 7 terms (original logo retained, trademarks not usable). Verdict: best-in-class office editing is realistic only if the host accepts AGPL or buys the commercial Developer edition. Weight L; license is the blocker.
- Stirling PDF: self-hosted PDF manipulation platform — merge, split, OCR, sign, redact, convert, compress, watermark — plus a desktop client and browser UI; Java, ~93k stars. Open-core: most of the tree is MIT, but named directories (e.g. `frontend/src/editor/proprietary/`) sit under a proprietary "Stirling PDF User License"; the essentials (conversion, editing, watermarking, redaction, password protection) remain free for self-hosting. No component library or SDK: run it (Docker or desktop) and point a webview/iframe at it, or integrate file-level against its API. Verdict: file-level only; a heavy Java server, and the prettiest editing UI lives in proprietary folders. Weight S–M (API) / L (UI embed).
- Excalidraw (canvas/diagram): ships as an npm package exporting the whole editor as a React component (`@excalidraw/excalidraw`), MIT, with `EXCALIDRAW_ASSET_PATH` for self-hosted assets and a documented elements/JSON data model for persistence. Runs in any webview (Electron, Tauri). Prior art: the official VS Code extension and Obsidian's popular Excalidraw plugin, which embeds the component inside Obsidian and stores drawings as files in the vault, embeddable in Markdown with notes linked to and from drawings. Verdict: "the unambiguous win of this whole list." Weight S.
- VLC / libVLC (media playback): the VLC player is GPLv2+ but libVLC is deliberately LGPL-2.1+ so third-party (including closed-source) apps can embed the engine; C API with official bindings (C++, Python, Java, Objective-C, C#) and render callbacks to output video into a host-provided surface. Codec patents may require royalties for some bundled codecs. Verdict: the mainstream way to embed playback (FFI + window interop; binaries ~100MB+). Weight M. (mpv/libmpv, also LGPL, exists outside this list.)
- Audacity (audio editing): GPLv3 project mid-way through a large 4.x rewrite. No library, no SDK, no WASM build, no headless mode; the only automation surface is `mod-script-pipe`, which lets an external Python/Perl script drive a running Audacity instance over named pipes. Verdict: file-level only (launch externally, optionally drive via script pipes). Embedding its DSP would mean a hard fork. If waveform editing is needed, purpose-built DSP crates are the honest answer. Weight M (poor value).
- OBS Studio (recording/streaming): GPL-2.0-or-later. libobs is the embeddable rendering/compositing/encoding core, but embedding it in-process makes the host a GPL-2.0+ derivative: Streamlabs' obs-studio-node was released under GPLv2 for exactly this reason, and commercial embedding without source disclosure produced a license dispute (lowkey.gg). Verdict: either a GPL-licensed separate helper process, or OS-level capture APIs (ScreenCaptureKit/AVFoundation) instead. Weight L–XL (libobs) / S (OS APIs).
- Image editors (GIMP / Krita / Photopea): GIMP is GPL-3.0 since 3.0, with Script-Fu/Python-Fu plugins, a libgimp 3.0 API and terminal batch runs, but no embeddable widget. Krita is GPL with C++/Python plugins (a plugin "can do everything that Krita can do" — inside Krita, not inside your app); no embeddable view or headless library. Photopea is proprietary (repo is issues-only) with a real iframe + postMessage scripting API — which would make a "local-first" app call a remote closed service with user files. Verdict: none is a good embedded component; use a small purpose-built canvas (or Excalidraw) for inline annotation, and GIMP/Krita as external "Edit in..." hand-offs. Photopea is disqualified on license/privacy grounds.
- Godot (2D/3D engine): MIT, no royalties. Headless server builds are officially documented; LibGodot (engine-as-a-library) is being mainlined in a sponsored PR (#110863), with migueldeicaza/libgodot as a maintained embeddable fork powering SwiftGodotKit and react-native-godot as an embedding precedent; GDExtension is the standard native-plugin mechanism. Verdict: the runtime embedded is realistic and precedented; the Godot editor embedded is fantasy. Makes sense only for interactive 2D/3D widgets (e.g. a 3D-scene note). Weight M–L.
- Blender (3D): GPL-2.0-or-later (Cycles is Apache-2.0); API-calling add-ons are treated as GPL. No embeddable UI; the real mechanism is `bpy`, an official pip-installable Python module for pipelines and web services, plus headless `blender -b` and the `blenderless` wrapper. Verdict: a sidecar Python process/Blender binary for thumbnailing, converting or rendering 3D assets referenced by notes; the GPL boundary is cleanest as a separate process. Weight M.
- Kdenlive (video editing): GPL-3.0-or-later as an application, with no embeddable view or headless library. The layer beneath it, the MLT Multimedia Framework (also behind Shotcut), is LGPL-2.1 for the framework and client libraries, with a C API of playlists/producers/consumers. Verdict: use MLT via FFI as the engine for a "video note" playback/trim/convert feature rather than Kdenlive itself. Weight M (MLT) / XL (UI).
(b) Standout details: the comparison table's bottom line — clean wins: Excalidraw (S, MIT, embeds directly), libVLC (M, LGPL) and MLT (M, LGPL) as engine-level FFI for media, bpy/Blender (M, headless sidecar) and GIMP headless (M) for file-level processing. Possible but licensing-dependent: OnlyOffice (only with AGPL compatibility or a commercial license) and libobs (only as a GPL-licensed separate helper). Non-starters as embedded components: Audacity, Kdenlive UI, Krita/GIMP UI, Photopea (non-free + remote service).
(c) What users want changed: the findings record no user sentiment for these components; the analysis is capability and license fit, not demand.
Sources: integrations-1.md

---

# PART III — SYNTHESIS

## 1. Feature wish list from the community

Every distinct feature request found across the Discord threads and digests, each tagged with the app/context it came from:

1. Web clipper as good as Evernote's (Evernote; also requested in Tana, Reflect contexts) — apps-likes-wants.md, community-digest.md
2. OCR search (search text inside images/PDFs/handwriting) (Evernote praise; Goodnotes; requested in digests) — apps-likes-wants.md, community-digest.md
3. Voice suite: voice transcription and voice-note capture (Reflect has it; requested more broadly) — apps-likes-wants.md, community-digest.md
4. Canvas + PDF annotation in one app (OneNote overlay model; Goodnotes/Notability strengths; requested in digests) — apps-likes-wants.md, community-digest.md
5. Unified task calendar (tasks with dates surfacing on a daily page) (Notion/Tana/Reflect contexts; digests) — community-digest.md, thread3-digest.md
6. RAG chat over your own notes (local-first AI; Tolaria model-provider chat; digests) — thread-c-local-models.md, tolaria.md, community-digest.md
7. AI stylistic mimicry — AI output in your own handwriting/style rather than generic typed font (Goodnotes complaint generalized) — apps-likes-wants.md
8. Flashcards/study mode built in (Amphi canvas app; digests) — apps-likes-wants.md, community-digest.md
9. Publishing (turn notes into a site/blog) (Obsidian Publish context; digests) — community-digest.md
10. Web companion (access notes from a browser) (Tolaria alpha "remote client"; digests) — tolaria.md, community-digest.md
11. Real-time collaboration (multiplayer editing) (Miro/Milanote/OneNote contexts; Logseq DB offline-first RTC goal; digests) — apps-likes-wants.md, thread-b-storage.md, thread3-digest.md
12. Tiered roles for collaboration (viewer/editor/admin) (Notion permissions context; digests) — community-digest.md, thread3-digest.md
13. Pen/keyboard/touch auto-switching like OneNote (input-mode findings) — input-mode-switching.md
14. Cloud-backend choice (self-host or pick your provider instead of vendor cloud) (Amphi Notes self-host; Anytype backup nodes; Reflect Open iCloud/Git) — apps-likes-wants.md, thread-b-storage.md
15. Paragraph-level links that survive moves/edits (block-reference durability; Logseq block refs; digests) — thread3-digest.md
16. Encrypted backup (E2E-encrypted backups user can verify) (Anytype/Reflect contexts; digests) — thread-b-storage.md, community-digest.md
17. Standard-format export that keeps properties/types (Anytype 0.47.4 story; Logseq DB export worries; Tana subset export) — thread-b-storage.md
18. A live two-way file mirror of a structured workspace (Thymer model; Logseq's unshipped goal) — thread-b-storage.md
19. Ink that never rewrites what you wrote (Goodnotes) — apps-likes-wants.md
20. Optional (not forced) handwriting completion/spellcheck (Goodnotes 6) — apps-likes-wants.md
21. AI output rendered in handwriting (Goodnotes) — apps-likes-wants.md
22. Pay once, keep everything (Notability/Noteshelf lifetime pattern; Evernote/Obsidian pricing) — apps-likes-wants.md
23. Sync never held hostage to a subscription (Notability iCloud lock) — apps-likes-wants.md
24. Honor lifetime purchases across major versions (Noteshelf 2→3) — apps-likes-wants.md
25. Fair/regional sync pricing and honest checkout defaults (Obsidian) — apps-likes-wants.md
26. Built-in effortless sync without plugin dependence (Obsidian) — apps-likes-wants.md
27. Full offline mode (whole workspace, not per-page) (Notion) — apps-likes-wants.md
28. Local data portability; no storage-format lock-in (Notion, Evernote, Anytype, Tana) — apps-likes-wants.md, thread-b-storage.md
29. Guaranteed-lossless export (JSON dump of the whole store + Markdown projection + JSON Canvas for canvases) (synthesis in thread-b) — thread-b-storage.md
30. Full export/backup for canvas apps (Milanote roadmap poll; "No Easy Export / Backup?") — thread-b-storage.md
31. Edit history on canvas boards (Milanote) — apps-likes-wants.md
32. Usable mobile apps at parity with desktop (Milanote, Anytype, Tana, Noteshelf, Reflect, OneNote) — apps-likes-wants.md
33. Nested folders/sections (OneNote) — apps-likes-wants.md
34. Performance that survives a large corpus (Notion, Miro, Logseq, Obsidian, Tana, Milanote) — apps-likes-wants.md
35. Notion-grade database features (formulas, linked views) in private/local apps (Anytype, Reflect) — apps-likes-wants.md
36. Supertag-like structure learnable in minutes (Tana) — apps-likes-wants.md
37. Daily-notes calm at a local-first price point (Reflect) — apps-likes-wants.md
38. Better attachment management (Reflect) — apps-likes-wants.md
39. Vector PDF export (Noteshelf deciding feature) — apps-likes-wants.md
40. Time-synced audio: tap ink/text to jump in the recording (Notability signature) — apps-likes-wants.md
41. Note-taking possible while a study widget/overlay is open (Amphi) — apps-likes-wants.md
42. A marketplace for stickers/planners/templates (Goodnotes has it; wanted elsewhere) — apps-likes-wants.md
43. A whiteboard that stays fast as the board grows (Miro) — apps-likes-wants.md
44. Trustworthy archive you own forever (Evernote) — apps-likes-wants.md
45. A third-party security audit for private/encrypted apps (Anytype) — apps-likes-wants.md
46. AI over note context with direct model-provider choice (Tolaria) — tolaria.md
47. Bundled MCP server / agent tool surface for the vault (Tolaria) — tolaria.md
48. Custom views authored by AI (views-as-YAML with natural-language dates) (Tolaria) — tolaria.md
49. Git-as-sync with AutoGit idle/focus auto-commit (Tolaria) — tolaria.md
50. Wikilinks that auto-update on rename (Tolaria; the inverse of Obsidian's rename-fanout cost) — tolaria.md, thread-b-storage.md
51. Truly native (non-web-wrapper) desktop shells (Tolaria HN demand) — tolaria.md
52. Feature focus — no churn/creep ("stay focused like Bear"; "we don't need new features") (Tolaria, Goodnotes) — tolaria.md, apps-likes-wants.md
53. Per-block capability grants with auditable prompts for embedded terminal/webhook/cron blocks (thread-f security model; the Obsidian vault RAT as the anti-pattern) — thread-f-editor-platform.md
54. Beyond-.md structure (a database) without abandoning files (Obsidian forum hunger) — thread-b-storage.md
55. Support notes that are not dashes-per-line Markdown (Logseq portability complaint) — thread-b-storage.md

## 2. Feature clusters

The recurring themes across apps, grouped:

- Capture versatility: web clipper (Evernote, Tana, Reflect), voice transcription (Reflect), audio-with-ink (Notability, Goodnotes, Noteshelf), quick capture that can be developed later (Goodnotes), inbox capture-vs-organize lifecycle (Tolaria), widget capture (xnotes-android). The wish list adds flashcards/study capture (Amphi) and PDF/image overlay capture (OneNote). — apps-likes-wants.md, tolaria.md, deep-repos-a.md
- Search-everything: OCR inside images and handwriting (Evernote, Goodnotes, OneNote), handwriting-box search (Goodnotes best-in-class), semantic command palette (Tolaria), deep archive search (Evernote), indexing (thread-d). Users consistently name search as the retention feature. — apps-likes-wants.md, thread-d-indexing.md, tolaria.md
- Local-first AI: direct model-provider choice including local (Ollama, LM Studio) versus cloud (Tolaria), GPT assistants (Reflect, Notion, Evernote), AI command bar (Tana), AI commit messages and AI-authored views (Tolaria), RAG chat over notes (digests). The community wants AI on their own terms, over their own notes. — tolaria.md, thread-c-local-models.md, apps-likes-wants.md
- Handwriting: ink rendering quality as a deciding feature (Noteshelf fountain pen; Notability best-in-class), ink fidelity versus AI smoothing (Goodnotes complaint), handwriting OCR search/conversion (Goodnotes), pen/touch/keyboard auto-switching (OneNote reference behavior), reverse-engineering Nebo's handwriting engine (myscript-nebo-reverse). — apps-likes-wants.md, input-mode-switching.md, myscript-nebo-reverse.md
- Canvas: infinite freeform canvas as thinking space (OneNote loved core), real-time collaborative boards (Miro, Milanote), canvas-as-database-view (AFFiNE/BlockSuite edgeless), whiteboards stored as files (Tolaria/tldraw), the live canvas↔note bridge (Obsidian Canvas sibling-file design; Heptabase and AFFiNE one-store designs), and canvas-app mortality risk (Muse's death). — apps-likes-wants.md, thread-b-storage.md, thread-f-editor-platform.md
- Databases/structure: relational databases with views (Notion loved and complained about), supertags (Tana), objects/sets/collections (Anytype), blocks with persistent IDs (Logseq DB, BlockSuite Y.Map, Trilium's why-database argument), types-as-lenses without schemas (Tolaria). The cluster's tension: structure wants a database, portability wants files, and no surveyed app has shipped both at high fidelity (Thymer mirror, Logseq two-way sync, both unproven). — apps-likes-wants.md, thread-b-storage.md, thread-f-editor-platform.md, tolaria.md
- Sync/trust: the single most-named pain across every community (OneNote, Anytype, Logseq, Obsidian, Notion, Reflect, Notability). Sub-themes: sync that is fast and never lost data, sync not held hostage to subscriptions, E2E encryption people can verify (Anytype, Reflect), Git-as-sync (Tolaria), P2P/local sync (Anytype), self-hosted sync servers (Amphi), and the warning that generic cloud sync corrupts database stores (Trilium's document.db). — apps-likes-wants.md, thread-b-storage.md, tolaria.md
- Export/anti-lock-in: plain local files as the loyalty anchor (Obsidian), export fidelity as the pressure valve and its repeated failures (Anytype pre-0.47.4, Tana subsets, Logseq properties lost, Milanote per-board only), conversion tooling as a category (ConvertOneNote2MarkDown, TanaMigrator), guaranteed-lossless export as the synthesis (JSON dump + Markdown projection + JSON Canvas), and JSON Canvas as the proven open canvas format. — thread-b-storage.md, apps-likes-wants.md, deep-repos-c.md
- Extensibility: plugin ecosystems as gravity (~5,000 Obsidian plugins), plugins as the security surface (the 2026 Obsidian vault RAT campaign; the Tasks-plugin RCE; the per-block grant model as the proposed fix), MCP servers and AGENTS files as the new agent-facing extensibility (Tolaria), embedded app blocks (OnlyOffice, Excalidraw, VLC, Audacity, and the rest of the integrations findings), and embedded terminal/webhook/cron blocks only under core-enforced invariants (thread-f). — thread-f-editor-platform.md, integrations-1.md, tolaria.md, apps-likes-wants.md

Cross-cutting conclusion carried from the findings: the three recurring gaps across all fourteen mainstream apps are (1) sync that is fast, reliable and either free or fairly priced; (2) local files/ownership with easy export; (3) performance that survives a large real corpus. An app that nails all three while keeping any signature modeling idea learnable in minutes addresses the most-named pain in every community studied. — apps-likes-wants.md

## R5 additions: the study/PDF-textbook angle (BookCraft idea research)

- The BookCraft idea as submitted (community suggestion, R5): a dedicated everyday study space for stylus students, explicitly not a PDF editor: its own library with notebooks, imported PDF textbooks and study materials organized by subject or course; notebook feel with natural handwriting, customizable pens and highlighters, easy movement between pages and materials; Drawboard PDF named as the inking-quality reference. — R5-user-link
- Drawboard PDF, what people like: pressure ink feel, dockable favorites-bar tool configs, palm rejection called better than Acrobat's, calibrated measurement/protractor toolset unique in the category. What people want changed: performance rot in long sessions and on large PDFs, no tabs or pinnable folders, missing in-place paste and hotkeys, free-tier upsell nags, lasting anger at the 2023 move of pressure ink behind Pro. Nothing open source. — findings/r5-drawboard-pdf.md
- The load-bearing study feature set, consistent across every app surveyed: import arbitrary PDFs into a course-organized library; freehand pen/highlighter plus text-layer highlighting; excerpt-to-note linking back to the source page (Flexcil gestures, LiquidText canvas, MarginNote mindmap, Zotero extraction); split view of textbook and notebook; search across handwriting and annotations; lossless export of the annotated PDF; study aids built on annotations (flashcards, quizzes, hide-to-memorize, tape tools). — findings/r5-study-apps-landscape.md
- Most-wanted across study communities: trustworthy sync (Flexcil's number-one request), ink smoothing, pixel eraser and shape tools, layers separating annotations from content (requested even of Notability), true PDF support (OneNote printout is the anti-pattern: image pages, misalignment, memory blowups), large-textbook performance (Goodnotes praised for exactly this), annotation write-back into the source PDF, stable non-subscription pricing (the loudest theme in every community), an end to the two-app pairing problem (Flexcil + Noteful named combos). — findings/r5-study-apps-landscape.md
- Loved differentiators worth stealing: Write's ink-manipulation primitives (select, move, erase, reflow handwritten text); University Notes' memorization layer mechanics on PDFs; Xournal++'s independently movable annotation objects; ZotFile's click-through links from notes back to PDF locations. — findings/r5-study-apps-landscape.md
- Verdict: no app is the unified dedicated study notebook over textbooks; the gap is real but contested (Flexcil closest on workflow but engine-limited, MarginNote deepest system but rigid and buggy, mainstream annotators treat the textbook as one content type). Documented traps for a new entrant: subscriptions, buggy updates, large-PDF performance, sync. — findings/r5-study-apps-landscape.md
- IdeaCraft (aamirenic, MIT): young but directly relevant Rust/Tauri reference: SQLite schema (db.rs), Tauri command layer (commands.rs), sync-folder design and smoke-test harness are pullable under MIT. No handwriting, no mobile. Not part of the ArtCraft family despite the name; rickyb82/ideacraft is the unrelated namesake. — findings/r5-ideacraft.md

## R6 additions: synthesis from the full-depth sweep (12 findings files)

- Obsidian plugin demand signal (16 plugins, registry cross-checked, licenses verified at each repo): self-hostable E2E sync, a Dataview-style query layer, note-embedding canvases, code-running templates, and the file browser as product surface. Cautionary evidence: Kanban orphaned with a version over a year old, Dataview's loudest complaint is table loading speed, Templater has a genuine license conflict (AGPL package.json vs GPL badge, no LICENSE file) needing a human check before any pull decision. jpzk/opensidian is the closest existing project to ours: a GPL-3.0 Rust+Tauri v2 clean-room Obsidian clone claiming to run real community plugins; concepts only under GPL, but its restricted-mode plugin trust design is worth copying. — findings/r6-obsidian-plugins.md, findings/r6-oss-repos-batch-d.md

- Sync/CRDT verdict: the CRDT + E2EE intersection is no longer under-documented. Automerge/Keyhive's BeeKEM, Loro's experimental protocol-e2ee, any-sync's encrypted DAGs, secsync's snapshot/AEAD model, and p2panda's post-compromise security all attack it directly; Rust-native options (yrs, Loro, iroh, automerge's Rust core, nostr-sdk) are real and shippable. License corrections: diamond-types is ISC not MIT, secsync is Apache-2.0 not AGPL-3.0 (last npm publish mid-2024, effectively dormant), TanaMigrator and snlib carry no license (code unpullable). The "Notion uses Yjs" claim was dropped: Notion's own engineering blog describes its own CRDT approach without confirming Yjs. — findings/r6-sync-crdt-stack.md, findings/r6-unverified-resolutions.md

- Handwriting verdict: TrOCR (MIT) is the best open handwriting-to-text engine (IAM CER 2.89 large / 3.42 base / 4.22 small; okraPDF independent testing put TrOCR-large at 3.68 CER, best non-VLM result). Tesseract is disqualified for handwriting (49.58% CER, zero lines exact); ML Kit Digital Ink is stroke-input only and proprietary; PARSeq is scene-text only. Open-source gaps that remain: temporal line segmentation for online (stroke-based) HTR is unsolved, and general OCR engines stay poor at real handwriting. The Supernote .note format is fully reverse-engineered (philips/supernote-typescript, Aug 2026: TOTALPATH per-stroke trails with pressures and tilts, RATTA_RLE bitmaps, partial-erase fragments, embedded MyScript iink files), giving a real path to pull stylus-vault functionality; snlib (Rust) exists but carries no license. — findings/r6-htr-ocr-engines-a.md, findings/r6-htr-ocr-engines-b.md, findings/r6-xournal-rnote-supernote.md

- Local AI verdict: small open-weights models are viable per task with license discipline. Qwen3-Embedding-0.6B (Apache) as default RAG embedder, sqlite-vec brute-force sufficing at notes-app corpus sizes; batch Whisper feasible on phones while streaming STT needs Moonshine (MIT) or platform APIs (whisper.cpp Android streaming runs ~5x slower than realtime); Kokoro-82M the desktop TTS pick, KittenTTS and Supertonic phone-size but with license warnings, Piper GPL (concepts only). Runtimes: llama.cpp, MLC, ExecuTorch, Core ML, ONNX Runtime, MediaPipe/LiteRT, plus Rust-native candle, mistral.rs, burn. Ollama is a desktop distribution layer, never the mobile mechanism. License traps: Llama Community and Gemma Terms are not OSI licenses; a pre-ship license-verification checklist is in the findings file. — findings/r6-local-ai-models.md

- Minor-apps verdict: across Squid, Concepts, Saber, Workflowy, DEVONthink, ente, Kinopio, Poznote, Tangent, Lockbook and the rest, the demand pattern is consistent. Sync trust is the category's weakest point (Squid's sync unshipped ~2 years, Samsung Notes duplicating conflicts instead of merging, OneNote sync partnership ending July 2026). Subscription-and-pack paywalls breed resentment (Concepts, Squid Premium, Obsidian Publish at 8 dollars per site per month). Most liftable local-first patterns: Kinopio's localStorage-first with queued ops and websockets, Lockbook's Rust core with E2EE, Saber's dual-password E2EE Nextcloud sync. File-format anxiety recurs wherever a closed format is the only container (.sbe, .note, Squid's Premium-walled backups). — findings/r6-batch1-minor-note-apps.md, findings/r6-batch2-minor-note-apps.md

- Editors/publishers verdict: Dillinger's client-side-only rendering and the Homebrewery's markdown-in themed-PDF-out pipeline are both directly liftable patterns; Ghost's Koenig editor and Ghost 6.0's split-services architecture matter if publishing becomes a surface; proofeditor's notes-to-AI contract is a live experiment to watch rather than copy. The Samsung Notes deep dive exposed the trust pattern of the whole category: PDF export rasterizes handwriting, no bulk export, sync conflicts duplicate instead of merge. — findings/r6-editors-publishers.md

- Nostr/transports verdict: concepts-only for sync plus an optional export path. At least four shipped apps sync notes over Nostr, but relay economics (471 public relays, 343 offline) and the single-identity-key conflict with per-note keys argue against Nostr as primary transport. Pull regardless: negentropy set-reconciliation (NIP-77) and NIP-44 padding discipline; NIP-44 v2 is Cure53-audited. nostr crate 0.45.5 runs ~385K downloads/month. iroh (MIT/Apache, 1.0 June 2026, default transport in Anytype) is the stronger Rust-native p2p lane. — findings/r6-nostr-transports-extras.md

- Verify-pass closure: 34 unverified entries tracked, 22 resolved, 5 partially, 7 not found. License corrections applied: diamond-types ISC, secsync Apache-2.0, snlib and TanaMigrator no-license-unpullable, Xournal++ bare GPL-2.0, RNote GPL-3.0-or-later (not Apache/EUPL as first assumed). fbalobaf/supernote-viewer is gone. "Notion uses Yjs" dropped. One independent Loro-vs-Y.rs-vs-Automerge benchmark exists (giosuel/imaginarium PR 16). Still open: KHATT derivative-weights licensing, Dillinger phishing accusation unverified by design. — findings/r6-unverified-resolutions.md

Sources: the twelve findings/r6-*.md files (r6-batch1-minor-note-apps, r6-batch2-minor-note-apps, r6-editors-publishers, r6-sync-crdt-stack, r6-htr-ocr-engines-a, r6-htr-ocr-engines-b, r6-xournal-rnote-supernote, r6-local-ai-models, r6-obsidian-plugins, r6-oss-repos-batch-d, r6-nostr-transports-extras, r6-unverified-resolutions).
