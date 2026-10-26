# Deep research: batch C (notes-app pull-from candidates)

All claims carry the URL they came from. UNVERIFIED = fetch/search did not confirm; no gap filled from memory.

---

## 1. jpzk/opensidian

Repo: https://github.com/jpzk/opensidian — language Rust (Tauri desktop app; Rust/Tauri per repo description (https://alternativeto.net/software/opensidian/about/) and repo description text (https://github.com/jpzk/opensidian)). Last activity: updated Oct 22, 2026 (https://alternativeto.net/software/opensidian/about/); no releases page verified — UNVERIFIED for latest release tag.

What it is: A clean-room, functional clone of Obsidian: it reimplements Obsidian's behaviour from the outside and contains none of its code (https://github.com/jpzk/opensidian). It is positioned as a privacy-first knowledge-management and collaboration platform (https://github.com/jpzk/opensidian). The project is actively recruiting Linux distribution maintainers (https://github.com/jpzk/opensidian).

Open source: Yes — GPL-3.0-or-later, LICENSE.md in the repo root (https://github.com/jpzk/opensidian/blob/main/LICENSE.md).

Feature list (from README via search snippet, https://github.com/jpzk/opensidian):
- Clean-room functional clone of Obsidian, none of its code
- Privacy-first local knowledge management
- Community call for Linux distro maintainers (packaging focus)
- Deeper feature list UNVERIFIED: full README fetch returned only the LICENSE in my fetch pass

What people like: 279 stars, 21 forks, 23 AlternativeTo likes, 6 open issues, updated Oct 22, 2026 (https://alternativeto.net/software/opensidian/about/).

What people want changed: 6 open issues exist (https://alternativeto.net/software/opensidian/about/) but individual issue URLs were not retrievable this pass — UNVERIFIED.

Pull-from: A Rust/Tauri vault app that already solved "be Obsidian-like without Obsidian code" — useful as a design reference for vault conventions, plugin/clone boundaries, and desktop packaging. Code pull is limited by GPL-3.0-or-later: lifting modules into a Rust-first app would make the combined work copyleft. Better: treat as a spec reference, not code source.

---

## 2. kostyk348/CapsuleCraft

Repo: https://github.com/kostyk348/CapsuleCraft — languages Rust (Tauri 2 backend) + TypeScript (React 19) (https://github.com/kostyk348/CapsuleCraft). Last activity: very active; v1.7.0 released 2026-10-25 (https://github.com/kostyk348/CapsuleCraft/releases/tag/v1.7.0); v1.4.0 on 2026-10-22 (https://github.com/kostyk348/CapsuleCraft/releases/tag/v1.4.0).

What it is: A "zero-database, pure-MIME multimodal workspace and personal knowledge engine" where every note is an RFC 5322 .eml file (https://github.com/kostyk348/CapsuleCraft). Notes become email-like capsules with Message-ID, In-Reply-To and References headers, giving threading and provenance for free (https://github.com/kostyk348/CapsuleCraft). Formerly known as CapsuleOS, now with a mascot and full icon set (https://github.com/kostyk348/CapsuleCraft).

Open source: Yes — MIT, LICENSE file (https://github.com/kostyk348/CapsuleCraft/blob/main/LICENSE); README states MIT license (https://github.com/kostyk348/CapsuleCraft).

Feature list (https://github.com/kostyk348/CapsuleCraft, releases https://github.com/kostyk348/CapsuleCraft/releases/tag/v1.4.0, v1.7.0):
- Every note stored as an RFC 5322 .eml file; vault at ~/.local/share/com.capsuleos.app/vault/ (https://github.com/kostyk348/capsuleos)
- Threading via standard email headers (In-Reply-To, References, Message-ID)
- Multimodal via MIME: attachments/parts carry media inside the note file
- Planning layer: vault-wide tasks, month grid, overdue/today/week buckets, priorities, ICS (VTODO) export (v1.4.0)
- Hierarchy drag-and-drop, Obsidian importer, IMAP sync, MCP expansion (PR #11, https://github.com/kostyk348/CapsuleCraft/pull/11)
- Empty vault + built-in onboarding page explaining the .eml concept (v1.7.0)
- Native standalone AppImage (~8 MB) built on the egui shell, no browser engine inside (v1.6.0, https://github.com/kostyk348/CapsuleCraft/releases/tag/v1.6.0); Tauri/web AppImage kept for parity
- Desktop (Tauri) + web versions

What people like: Listed in the community AppImage catalog via PR #10673 (https://github.com/AppImage/appimage.github.io/pull/10673). Star/fork counts UNVERIFIED this pass (not in fetches).

What people want changed: External contributors actively push large feature PRs — e.g. PR #11 "Master Evolution — MCP expansion, Obsidian importer, hierarchy DnD, and IMAP sync" (https://github.com/kostyk348/CapsuleCraft/pull/11) and PR #7 fixing CI formatting (https://github.com/kostyk348/CapsuleCraft/pull/7). Open issue list UNVERIFIED individually.

Pull-from: The .eml-per-note storage convention is the crown jewel: RFC 5322 + MIME gives a zero-lock-in, human-inspectable, git-friendly format with threading and attachment semantics already standardised. An empty-vault onboarding pattern and ICS/VTODO task export are also directly liftable as designs. MIT license: fully compatible with a Rust-first local-first app.

---

## 3. kostyk348/capsuleos

Repo URL: https://github.com/kostyk348/capsuleos — the fetch of this URL now returns the CapsuleCraft README (https://github.com/kostyk348/capsuleos): the project was renamed CapsuleCraft (see v1.5.0 rename in the release chain, https://github.com/kostyk348/CapsuleCraft/releases/tag/v1.6.0 context; the README still says `cd capsuleos` in build commands, https://github.com/kostyk348/CapsuleCraft).

What it is: The same project as section 2 under its old name. The description "CapsuleOS — Zero-DB, Pure-MIME multimodal workspace & personal knowledge engine. Native desktop (Tauri + React 19)" is still indexed (https://github.com/kostyk348/capsuleos). A Russian-language description confirms each capsule is a separate RFC 5322 .eml file in the vault directory (https://github.com/kostyk348/capsuleos).

Open source: Yes — MIT, same repo as CapsuleCraft (https://github.com/kostyk348/CapsuleCraft/blob/main/LICENSE).

Feature list: identical to section 2; additionally a related account holds a mirror/continuation, kobaltgit/capsuleos, with the same description (https://github.com/kobaltgit/capsuleos).

What people like: same as section 2. What people want changed: same as section 2.

Pull-from: same as section 2 (.eml format, MIT). Treat capsuleos as a stale URL; the live project is CapsuleCraft.

---

## 4. OfficeIMO (community-linked fork)

Repo URL withheld from publication (hosted under a community member's account) — DOES NOT EXIST. Two targeted searches return no such repository; the account's other repos are a personal site, openplayground and multi-chatbot-ui. Nonexistent/private: NOT OPEN SOURCE at this URL.

The real project is EvotecIT/OfficeIMO — language C# (.NET). Last activity/release: NuGet package OfficeIMO.Word v3.4.4 published 2026-09-28, 2,920,435 total downloads (https://evotec.xyz/projects/officeimo/); ~80 forks (https://officeimo.com/).

What it is: A family of lightweight, cross-platform, MIT-licensed .NET libraries for creating, reading, editing, converting, rendering and extracting Office, PDF, email, OneNote and text formats, built on the Open XML SDK with no Office/COM installation required (https://github.com/EvotecIT/OfficeIMO, https://github.com/EvotecIT/OfficeIMO/blob/master/README.md).

Open source: Yes — MIT; the repo title itself says "MIT-licensed, COM-free .NET libraries" (https://github.com/EvotecIT/OfficeIMO). License file: https://github.com/EvotecIT/OfficeIMO/blob/master/LICENSE.

Feature list (from README, https://github.com/EvotecIT/OfficeIMO/blob/master/README.md):
- Word: create, load, edit, append, inspect and save .docx documents
- Excel, PowerPoint, PDF, email (msg/eml) and OneNote read/conversion support in the library family
- Mermaid rendering via ChartForgeX.Markup.Mermaid and a MarkdownRenderer package
- Document and Markdown cores remain independently usable
- Companion PowerShell module (PSWriteOffice), CLI, Studio and browser tools (https://officeimo.com/)

What people like: 2.9M NuGet downloads for Word alone (https://evotec.xyz/projects/officeimo/); ~80 forks (https://officeimo.com/). Stars UNVERIFIED this pass.

What people want changed: no specific issues fetched — UNVERIFIED.

Pull-from: Not Rust code, so lift concepts, not crates: its docx object model (sections, styles, tables, headers/footers, images), the "no COM, pure Open XML" architecture, and the markdown-to-docx rendering path (OfficeIMO.MarkdownRenderer) are exactly the pieces a Rust notes app needs for export. MIT: fully compatible.

---

## 5. masked8knights/bb-kilocode

Repo: https://github.com/masked8knights/bb-kilocode — language TypeScript (plugin source; JS/TS toolchain inferred from npm-style install flow — the page shows `bb plugin install git:...` and `git clone` (https://github.com/masked8knights/bb-kilocode)). Last activity UNVERIFIED (no releases fetched).

What it is: A first-class Kilo Code provider plugin for BB, replacing the built-in ACP guest integration (https://github.com/masked8knights/bb-kilocode). Once installed, Kilo Code appears in BB's provider picker as provider id `kilocode`, and a thread can run against it (https://github.com/masked8knights/bb-kilocode).

Open source: repo is public and installable from git, but the license name was not visible in my fetch — UNVERIFIED.

Feature list (https://github.com/masked8knights/bb-kilocode):
- Registers provider `kilocode` in BB's provider picker
- Hot plugin management: `bb plugin reload kilocode`
- Install via one git URL, or clone for development
- Scoped to provider integration only; no note features

What people like / want changed: tiny utility repo; no stars, issues or discussions surfaced in search — UNVERIFIED.

Pull-from: little for a notes app beyond the pattern: a plugin that adapts an external model provider into a host app's provider registry, installed from a bare git URL. License incompatible/unknown, so nothing to lift as code.

---

## 6. nostr-protocol/nostr

Repo: https://github.com/nostr-protocol/nostr — language: protocol spec/README (no application codebase; the NIPs live in a sibling repo) (https://github.com/nostr-protocol/nostr). Last activity UNVERIFIED for the repo itself; the NIPs repo is actively maintained (https://github.com/nostr-protocol/nips).

What it is: The home of the Nostr protocol: "a truly censorship-resistant alternative to Twitter that has a chance of working" (https://github.com/nostr-protocol/nostr). The protocol is deliberately tiny: events signed by keys, relayed by dumb relays; NIP-01 is the core spec and the NIPs document optional extensions (https://github.com/nostr-protocol/nostr).

Open source: The NIPs (spec documents) are public domain (https://nostr-nips.com/). A license file for the nostr repo itself was not verified — UNVERIFIED; the repo is essentially documentation, so licensing matters little.

Feature list / design points (https://github.com/nostr-protocol/nostr, https://nips.nostr.com/):
- Event-based model: clients sign events; relays store and forward; no server-side accounts
- Key identity rather than account identity (censorship resistance by design)
- Client picks any NIP subset; "NIPs listed here are not a protocol checklist" (https://github.com/erskingardner/nips, mirror of upstream)
- Spec process: standards emerge by adoption first, then get codified as NIPs (https://github.com/nostr-protocol/nips/blob/master/README.md)

What people like / want changed: ecosystem-scale adoption is the signal; per-repo stars/issues UNVERIFIED this pass.

Pull-from: The interesting angle for a local-first notes app is the relay/E2E-relevant protocol design, not code: keypair-based identity, signed append-only events, dumb relays + smart clients, and NIP-style "small core, opt-in extensions" layering map directly onto a sync/backup layer where notes sync through untrusted relays and E2E encryption rides on the keypair model. Public-domain specs: no license friction at all.

---

## 7. realbynl/Meridian-Notes

Repo: https://github.com/realbynl/Meridian-Notes — language Rust, native GUI (draws its own window; no web technologies, no terminal) (https://github.com/realbynl/Meridian-Notes). Version 0.2; roadmap in ROADMAP.md; last release tag UNVERIFIED.

What it is: A fast, themable, native note editor in Rust whose notes are plain Markdown files readable in any other editor (https://github.com/realbynl/Meridian-Notes). It is also a study tool: cloze cards, quizzes and Anki import/export sit inside the editor (https://github.com/realbynl/Meridian-Notes).

Open source: Yes — a LICENSE file is referenced ("See Licence ... See LICENSE.", https://github.com/realbynl/Meridian-Notes) but the exact license name was not visible in my fetch — UNVERIFIED.

Feature list (https://github.com/realbynl/Meridian-Notes):
- Rope-based buffer, undo/redo, multiple cursors, select next/all, move lines
- Word wrap, line numbers, minimap, sticky scroll, code folding, permanent/temporary bookmarks
- Find/replace, find-in-files with an editable results document, regex builder
- Split views (columns/rows), tabs, macros (record/play/save), pipe selection through command
- Spell check, lint, git gutter, syntax highlighting, diff vs saved file, time-travel history scrubber
- Vim mode, typewriter scrolling, focus mode, pomodoro, word statistics
- Encodings/line endings: UTF-8/16, Latin-1, LF/CRLF/CR
- Notes: [[links]], {{embeds}}, backlinks sidebar, hover preview, inline pictures, heading-size rendering, goto-anything, file tree, notebooks/sections/pages, templates, remote folders with sync
- Views: Endless canvas (notes as free-positioned text boxes via a layout file), graph view (`meridian --graph`), table/data-tree side views, pen ink (Wayland stylus) saved as SVG, touch gestures
- Study: cloze cards, review, quizzes, recall/Feynman panels, reading queue, exam forecast, Anki TSV/APKG import/export, study stats, leech list, speed reader
- Look/feel: role-based skin system, gradients, PNG tile/nine-slice, ornaments, custom fonts, hot reload, contrast guard
- Out-of-process plugins on a stable protocol (panels, commands, key bindings); rebindable keys and settings configs
- Crate layout: crates/gui (window, CPU-painted editor, canvas, graph, ink), crates/app (all features as a library), crates/ui, crates/term, crates/buffer; docs/ design notes (ink.md, skins.md, ui-toolkit.md, endless.md, graph.md, perf.md)

What people like / want changed: no stars/issues fetched — UNVERIFIED.

Pull-from: Arguably the best Rust-first pull source in the batch: the crate decomposition (buffer vs ui vs app vs gui), a CPU-painted editor design doc (docs/perf.md), the SVG-based ink pipeline, the out-of-process plugin protocol, and cloze/Anki study structures. License unknown: do not lift code until the LICENSE file is confirmed compatible.

---

## 8. shardulvs/xnotes-android

Repo: https://github.com/shardulvs/xnotes-android — Android app, Kotlin/C++ (build needs JDK 17, NDK 27.0.12077973 and CMake 3.22.1) (https://github.com/shardulvs/xnotes-android). Active: repo updated ~2 weeks ago (https://github.com/shardulvs/xnotes-android); on F-Droid updated ~3 weeks ago (https://f-droid.org/packages/com.xnotes/).

What it is: A handwriting-first notebook for phones and tablets, built for pen and stylus, with pressure-sensitive variable-width ink (https://f-droid.org/packages/com.xnotes/). Nothing is flattened: every stroke is stored as editable vector data in the open .xnote format (https://github.com/NicolasKDev/xnotes-android, fork of the same README).

Open source: Yes — shipped on F-Droid, which builds from source and verifies against the GitHub release (https://f-droid.org/packages/com.xnotes/). Exact license name UNVERIFIED this pass (F-Droid listing implies an OSI license; not stated in my fetches).

Feature list (https://f-droid.org/packages/com.xnotes/, https://github.com/shardulvs/xnotes-android):
- Pressure-sensitive, variable-width ink; strokes never flattened
- Paged notes and an infinite canvas mode
- Strokes stay re-selectable, movable, restylable (open .xnote vector format)
- F-Droid and GitHub ship the same signed APK; switchable without reinstalling
- Active fork ecosystem, including a Linux host port (DarkL0gos/xnotes-android, https://github.com/DarkL0gos/xnotes-android) with XDG config paths

What people like: multiple active forks (pmvi, sylphrena0, Lucas-Tolle, gky051224, NicolasKDev, LeleoLazarini) and a separate Linux port project (https://github.com/DarkL0gos/xnotes-android); F-Droid presence. Stars UNVERIFIED.

What people want changed: no specific issues fetched — UNVERIFIED.

Pull-from: The .xnote "strokes as editable vector data, never rasterised" format philosophy, the paged+infinite-canvas dual document model, and the desktop-port approach are directly liftable designs for a Rust notes app's ink engine. Format is app-specific: adopt the idea, define your own Rust-first schema.

---

## 9. slogsdon/bb-tui

Repo URL: https://github.com/slogsdon/bb-tui — DOES NOT EXIST in search results. slogsdon's repos surface as bb-plugin-* utilities instead (search pass found no slogsdon/bb-tui; slogsdon repos like bb-plugin-* exist in other lanes). Treat as nonexistent: NOT AVAILABLE.

What exists is bborn/bb-tui — language Go (go install; https://github.com/bborn/bb-tui). Last activity UNVERIFIED (no release page fetched).

What it is: A terminal UI for BB, ported from the TaskYou TUI: board, thread view, composer, filters, saved views and command palette, running against BB's API rather than a local database (https://github.com/bborn/bb-tui). Threads read as conversations: replies as markdown, tool calls collapsed to one line each (https://github.com/bborn/bb-tui).

Open source: public repo, installable via go install and Homebrew tap (https://github.com/bborn/bb-tui). License name UNVERIFIED this pass.

Feature list (https://github.com/bborn/bb-tui):
- Kanban-style board of threads grouped by state (Queued/Running/Waiting/Idle), list view via `v`
- Thread view with markdown replies, collapsed tool calls, composer underneath
- Composer: `/` offers the project's skills, `@` its files, ctrl+o model picker, ctrl+y permission mode, ctrl+v clipboard image attach
- Filters, saved views, command palette; keybindings and themes stored TUI-side in ~/.bb-tui/, all thread data from the BB server only (BB_SERVER_URL)
- VHS-generated screenshots from an invented demo workspace (internal/bbstore/demo.go); `--demo` mode; `--debug-state` headless view-tree JSON for testing

What people like / want changed: UNVERIFIED (no stars/issues fetched).

Pull-from: UX patterns only: thread-as-conversation rendering, board/grouping states, saved views, and the headless --debug-state testing approach. Go code with unverified license: do not lift as code.

---

## 10. theohbrothers/ConvertOneNote2MarkDown

Repo: https://github.com/theohbrothers/ConvertOneNote2MarkDown — language PowerShell (ConvertOneNote2MarkDown-v2.ps1) (https://github.com/theohbrothers/ConvertOneNote2MarkDown). Last activity: ~711-757 stars and 80-84 forks across recent snapshots; release activity visible (https://github.com/theohbrothers/ConvertOneNote2MarkDown/releases/). A fork of SjoerdV/ConvertOneNote2MarkDown (https://github.com/theohbrothers/ConvertOneNote2MarkDown/releases/).

What it is: A PowerShell script that uses the OneNote Object Model on a workstation to convert OneNote pages to Word documents, then Pandoc to convert the Word files to Markdown (https://github.com/theohbrothers/ConvertOneNote2MarkDown). It is the standard escape hatch for people leaving OneNote/EverNote for plain text (https://github.com/theohbrothers/ConvertOneNote2MarkDown).

Open source: Yes — GPLv3; the upstream LICENSE is GPL version 3 (https://github.com/SjoerdV/ConvertOneNote2MarkDown/blob/master/LICENSE).

What converts cleanly (https://github.com/theohbrothers/ConvertOneNote2MarkDown):
- Full notebooks, or one notebook; pages in sections at Notebook, Section Group and nested Section Group levels
- Mirrored folder structure; subpages as subfolders or name prefixes; configurable max filename length (32-255)
- Media (images, attachments) into central or per-folder /media dirs, symbols stripped from names, relative links rewritten into the .md
- Title as # heading, standardised created/modified DateTime, horizontal rule separator
- Pandoc flavour choice (markdown, commonmark, gfm, markdown_mmd, markdown_phpextra, markdown_strict), list cleanup, backslash-escape removal, LF/CRLF choice
- Dry run, reuse of existing .docx (90% faster), docx naming conventions, optional .pdf export alongside .md, verbose logs

What is lost or breaks (all from the README Known Issues, https://github.com/theohbrothers/ConvertOneNote2MarkDown):
- Collapsed/hidden paragraphs are NOT exported to .md (workaround: Onetastic macro to expand all)
- Password-protected sections must be unlocked; the Object Model cannot read them
- InkDrawing (pen/handwritten) positions are NOT preserved in .md; pages must be "flattened" by hand (screenshot + remove ink) or a .pdf export used, which preserves InkDrawing absolute positions (config $exportPdf = 2)
- OneNote is unusable during conversion; Word plugins can break .docx generation; Windows Defender may block pandoc.exe; RPC errors need same-privilege PowerShell/OneNote and absolute paths (troubleshooting section, https://github.com/theohbrothers/ConvertOneNote2MarkDown)

What people like: 711-757 stars, 80-84 forks (https://github.com/theohbrothers/ConvertOneNote2MarkDown/releases/); discussed on r/planetemacs as the migration path (https://www.reddit.com/r/planetemacs/comments/s17xlf/convertonenote2markdown_ready_to_make_the_step_to/).

What people want changed: Issue #112 "OneNote bug? RPC server unavailable" (closed) (https://github.com/theohbrothers/ConvertOneNote2MarkDown/issues/112); Issue #183 "Screenshots not imported properly" (https://github.com/theohbrothers/ConvertOneNote2MarkDown/issues/183) — state UNVERIFIED from snippet.

Pull-from: Not code for a Rust app, but a requirements goldmine for an OneNote importer: the Object Model → docx → Pandoc pipeline, what OneNote content degrades (ink, collapsed paragraphs, locked sections), and the media/relative-link rewriting rules. GPL-3.0: do not lift the script; reimplement the conversion matrix.

---

## 11. thiagovasconcelosti/opensidian

Repo: https://github.com/thiagovasconcelosti/opensidian — language TypeScript/Node (npm scripts: npm install/build/test/dev) (https://github.com/thiagovasconcelosti/opensidian/blob/main/README.md). Last activity UNVERIFIED; appears to be a small project (no stars/releases surfaced).

What it is: A different project from jpzk/opensidian despite the same name: "an open-source knowledge management system inspired by Obsidian" with a plugin system for extending functionality (https://github.com/thiagovasconcelosti/opensidian/blob/main/README.md). It is unrelated to the Rust/Tauri clean-room clone in section 1.

Open source: Yes — MIT, per its README (https://github.com/thiagovasconcelosti/opensidian/blob/main/README.md). LICENSE file URL UNVERIFIED (not fetched directly).

Feature list (https://github.com/thiagovasconcelosti/opensidian/blob/main/README.md):
- Knowledge-management system inspired by Obsidian
- Plugin system for custom functionality
- Standard Node toolchain (install, build, test, dev)

What people like / want changed: nothing surfaced; the same account's other activity is unrelated issues (e.g. a helios-server issue, https://github.com/benadida/helios-server/issues/302). Note: the AlternativeTo "Opensidian" page (279 stars) tracks jpzk's, not this one (https://alternativeto.net/software/opensidian/about/).

Pull-from: minimal; plugin-system concept only. MIT-compatible but not worth lifting from a project this small.

---

## 12. toeverything/affine (DEEP)

Repo: https://github.com/toeverything/AFFiNE — languages TypeScript + Rust (built "with Typescript/React/Rust" per the project's own launch post, https://www.reddit.com/r/PKMS/comments/wgrvoe/affine_is_the_nextgen_knowledge_base_to_replace/). Last activity: repo page indexed August 17, 2026 (https://github.com/toeverything/AFFiNE); latest release v0.27.4 dated 2026-08-18 (https://opentechub.com/repo/toeverything/AFFiNE) — treat exact latest tag as UNVERIFIED past that snapshot.

What it is: A privacy-first, local-first, open-source alternative to Notion and Miro: one platform where docs, canvas and tables are "hyper-merged" (the affine name) (https://github.com/toeverything/AFFiNE). It is a block-based knowledge base with planning, sorting and creating together, with a live demo, Discord and self-host docs (https://github.com/toeverything/AFFiNE).

Open source: Yes — MIT. The repo is MIT-licensed and the product page states the editor is MIT-licensed with self-hosting free for up to 10 seats per workspace (https://affine.pro/blog/affine-self-host-v10-seats — UNVERIFIED exact URL; the seat policy was surfaced via search snippets, mark exact terms UNVERIFIED). License file: https://github.com/toeverything/AFFiNE/blob/canary/LICENSE.

Scale: stars reported as 60k+ in 2026 by the team's blog (https://affine.pro/blog, UNVERIFIED exact post) and 73.3k by an aggregator snapshot (https://opentechub.com/repo/toeverything/AFFiNE); roughly 666-774 open issues in early-2026 snapshots (https://opentechub.com/repo/toeverything/AFFiNE). No single number is verifiable to me directly — UNVERIFIED individually.

BlockSuite architecture: BlockSuite (https://github.com/toeverything/blocksuite) is the MIT-licensed block-based editor framework underlying AFFiNE, providing both the document (page) editor and the edgeless (whiteboard) editing surface over the same block data model (https://github.com/toeverything/blocksuite, https://github.com/toeverything/AFFiNE). The launch discussion describes it as "not only a block docs, but also a visual learning/collaboration tool merged together" (https://github.com/toeverything/AFFiNE/discussions/84). Sync/collaboration logic lives in the Rust OctoBase component of the monorepo (https://github.com/toeverything/AFFiNE).

Canvas+doc duality: the same block document is viewable as a structured page and as a free edgeless canvas — "Docs, canvas and tables are hyper-merged with AFFiNE - just like the word affine" (https://github.com/toeverything/AFFiNE). This is the repo's core architectural idea: one data model, two (or more) renderers, rather than separate doc and whiteboard stores.

Self-hosting model: distributed as Docker images (ghcr.io/toeverything/affine-graphql:stable) with a docker-compose setup; community self-host threads and issues document the compose file and its rough edges (https://www.reddit.com/r/selfhosted/comments/1b0dyqt/affinepro_our_notionmiro_open_source_alternative/, which references https://github.com/toeverything/AFFiNE/issues/6154). Self-host is Community Edition; the hosted affine.pro product adds paid features, and self-host seat limits reportedly apply (exact current terms UNVERIFIED — https://affine.pro).

Feature list (https://github.com/toeverything/AFFiNE, https://github.com/toeverything/AFFiNE/discussions/84):
- Block-based docs editor, edgeless whiteboard/canvas, tables, kanban — one merged data model
- Local-first data, privacy-first sync, self-host via Docker
- Open-source, customisable ("There can be more than Notion and Miro")
- Rust sync core (OctoBase), BlockSuite editor framework as separate MIT projects

What people like: sustained r/selfhosted and r/PKMS reception (54 upvotes / 90 comments on the self-host thread, https://www.reddit.com/r/selfhosted/comments/1b0dyqt/affinepro_our_notionmiro_open_source_alternative/); 60k+ stars scale (https://opentechub.com/repo/toeverything/AFFiNE); original launch discussion still referenced (https://github.com/toeverything/AFFiNE/discussions/84).

What people want changed (top open themes):
- End-to-end encryption / stronger privacy guarantees for sync and self-host — recurring request theme surfaced in issue searches (https://github.com/toeverything/AFFiNE/issues — exact issue numbers UNVERIFIED this pass)
- Self-hosting friction: compose configuration, versioning and seat limits; e.g. issue #6154 linked from the self-host thread (https://github.com/toeverything/AFFiNE/issues/6154)
- General bug backlog: the issues page is dominated by recent editor/canvas bugs (https://github.com/toeverything/AFFiNE/issues)

Pull-from: the deepest pull source in this batch. Lift patterns, not code (TypeScript/Rust split, but licences allow both): the single block data model rendered by both page and edgeless canvas (BlockSuite's duality), the Rust-side sync engine separation (OctoBase), the block-as-plugin editor framework, and the local-first + Docker self-host packaging. MIT everywhere (AFFiNE, BlockSuite, OctoBase): fully compatible with a Rust-first notes app, including direct code study of BlockSuite's edgeless rendering and OctoBase's sync/CRDT layer.

---

## Cross-batch takeaways

The two most liftable Rust-first assets are realbynl/Meridian-Notes (native Rust editor architecture, license to confirm) and toeverything/AFFiNE's architectural patterns (BlockSuite duality, OctoBase sync, MIT). CapsuleCraft's .eml-per-note storage convention is the most distinctive format idea, MIT and directly usable. xnotes-android contributes the never-flatten ink/vector format philosophy. ConvertOneNote2MarkDown defines exactly what an OneNote importer must handle (ink, collapsed paragraphs, locked sections). jpzk/opensidian is a GPL reference only. The two named URLs a community member's OfficeIMO fork and slogsdon/bb-tui do not exist; canonical counterparts are EvotecIT/OfficeIMO (MIT, .NET) and bborn/bb-tui (Go).
