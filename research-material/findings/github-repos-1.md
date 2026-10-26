# GitHub repos, part 1 of 2 (A–O / batch 1)

Research lane: GitHub repositories for the notes-app project (Rust, local-first, canvas/block notes, E2EE).
Fetched 2026-10-26. Excludes anything bb/get-bb related (per instruction; none encountered).

## AlienTechSoftware/notecraft
- What it is: open-source, clean-room reimplementation of Microsoft OneNote, rebuilt in pure Rust. Note taking and organization with OneNote's freeform canvas and ink, markdown-first folder-based file format editable in any text editor. Desktop + web; automation through MCP.
- Stack: pure Rust; UI with egui and wgpu; web build via WebAssembly (Trunk). Crates layered by architecture levels (L0 notecraft-model: node kinds, page formats, tags, name rules, ids, time).
- Maturity: very early alpha. Releases v0.0.1 through v0.0.6; v0.0.3 release page (Oct 21, 2026) states plainly: "Alpha... little use, and the folder format can still change. Keep a backup... Windows x64 only." Active forks/renames in the same project family: queball1999/notecraft (parity checklist at 49% after Phase 1, PR 56), joshmaster2165/Notecraft ("OneNote parity: 61 of 67 features", OneNote import, AI & agents, Rust + Tauri), matteo-andreuzza/notecraft (docs/parity.md, parity-catalog.md), a notecraft fork by a community member (name withheld).
- Key features: freeform canvas + ink, notebook > section-group > section > page hierarchy, rich text, tags, links, versions, recycle bin, conflict copies, markdown/plain-file storage, OneNote import, MCP for agents, bundled "Welcome" HTML demo notebook.
- Docs worth reading: docs/feature-parity.md, docs/gaps.md, docs/folder-format.md, docs/page-model.md, docs/research/onenote-file-format, docs/post-parity.md. NOTE: I could not fetch the blob pages directly (tool refused); UNVERIFIED for the doc bodies. What is verified: the README excerpt from search confirming feature-parity.md exists and is the "honest picture" of gaps, and the folder-format rules "down to name length and conflict copies."
- Page model (from search snippet, dr3-1): a page carries its own metadata (title, id, order, created, updated) in front matter or tags, so a page survives copy/move/sync as itself. This is a strong local-first design pattern.
- Issues/discussions: search surfaced issues #4 and #8 on notecraft (bodies UNVERIFIED). PR context: the "full HTML Welcome demo" PR (#6) actually lives on daijro/openplayground, where a contributor wired NoteCraft's WASM build into openplayground's live-app gallery; verified in headless Chrome, owner thanked the contributor.
- Relevance: closest architectural sibling to our project (Rust, local-first, canvas, E2EE-adjacent privacy posture). Teaches: measured parity discipline (checklists with wiring vs behaviour), self-describing page metadata for sync safety, clean-room legal hygiene, honest "what works today" docs, and exposing the app to agents via MCP.
- Sources: https://github.com/AlienTechSoftware/notecraft , https://github.com/AlienTechSoftware/notecraft/releases/tag/v0.0.3 , https://github.com/queball1999/notecraft/pull/56 , https://github.com/joshmaster2165/Notecraft , https://github.com/daijro/openplayground/pull/6 , https://github.com/matteo-andreuzza/notecraft

## DerKezorm/nexlore
- What it is: self-hosted, web-based notes app: notes as plain Markdown files on disk, browsed/edited in a browser, with an Obsidian-friendly folder structure and a zoomable graph view.
- Stack: Markdown-file storage; browser UI; MCP support for AI agents. Canvas interop via JSON Canvas v1.1.0 format.
- Maturity: moving very fast — published versions 1.1.0 through 1.8.1 (mid/late Oct 2026), plus open-source releases after 1.7.
- Key features: Markdown notes in plain folders, zoomable infinite graph, search with OR query blocks, canvas in JSON Canvas format, MCP tool access, RAG Q&A over your notes ("Ask Lore"), e-mail confirmation, Microsoft Entra ID sign-in, manual/automatic backups, versioned updates. Self-hosted but cloud-ready sync direction.
- Issues: issue #15 (unretrieved, UNVERIFIED) discusses search query blocks, per search snippet.
- Relevance: proves demand for local-files-first notes with a canvas/graph layer; JSON Canvas adoption is the pragmatic interop choice for a block/canvas app. The local-markdown-file base plus optional self-hosted server is exactly the trust gradient our E2EE app should copy. Fast release cadence shows one-maintainer velocity is possible.
- Sources: https://github.com/DerKezorm/nexlore (search result qte-1)

## EkarinLB/e-journal
- What it is: local-first ink notebook for Windows and Linux for pen users; open source, offline, no accounts/telemetry ("nothing leaves your computer — because there is nothing to send it to").
- Stack: Tauri v2, Rust backend owning storage/files/window, ink canvas on the system WebView (no bundled Chromium, no Electron). MIT.
- Maturity: v0.12.0 beta; CI-built installers (exe, MSI, deb, AppImage) with SHA-256 checksums; unsigned Windows binaries (SmartScreen warning).
- Key features: pressure-sensitive ink (ballpoint/fountain/brush nibs, Chaikin smoothing, translucent highlighter, eraser, scribble-to-delete), notebooks/pages with ruled/plain/blank paper, continuous scroll creating pages, images with drag-drop, undo/redo, palm rejection, single JSON library file + rolling .bak, atomic writes, single-instance lock, read-only import of Microsoft Journal .ink (SQLite) files, whole-library export.
- Honest gap list in README: no version history, no typed text/shapes/lasso, title-only search (no HTR), partial .ink import, no tags, no macOS.
- Relevance: a small, disciplined template for our project: one readable JSON library with atomic writes + .bak + refuse-empty-save is a directly reusable local-first storage pattern; the "tracked rather than hidden" gaps doc is good user trust practice; roadmap ranks version history #1, then HTR-based handwriting search.
- Sources: https://github.com/EkarinLB/e-journal

## EvotecIT/OfficeIMO
- What it is: a .NET library suite for reading/writing Microsoft Office documents natively; includes OfficeIMO.OneNote, described as the first C# OneNote reader/writer, clean-room, no COM, first-party, no external dependencies.
- Stack: C#/.NET. Modular NuGet packages: OfficeIMO.Word, Excel, PowerPoint, OneNote, plus projections OneNote.Markdown and OneNote.Html (semantic projections owned by the project), and OneNote versions/revisions support.
- Maturity: long-running, actively maintained; large README; multiple OneNote packages (reader/writer, ink, conflicts, versions).
- Key features: .one notebook reading/writing, HTML and Markdown projections of OneNote content, versions and revisions, ink support, conflict handling. Not an app; a library others build on.
- Relevance: shows what a full OneNote-format implementation must cover (projections to HTML/Markdown as separate "owners" of serialization, revisions, ink, conflicts). For our project: treat format projections (canvas->markdown, canvas->html) as separate modules with clear ownership; OneNote import is a real user demand (several ecosystem tools exist for it).
- Sources: https://github.com/EvotecIt/OfficeIMO (sub-pages OfficeIMO.OneNote.Html and OneNote.Markdown tree pages not separately fetched; package descriptions verified from the main README)

## HasanMajid/open-note
- What it is: OpenNote, a modern cross-platform note-taking app combining "the fluid, low-latency inking experience of Samsung Notes with the hierarchical organization of Microsoft OneNote"; stylus, touch and desktop workflows on one canvas.
- Stack: Flutter/Dart; feature-first architecture (core/, features/canvas, features/notebook, features/storage). MIT.
- Maturity: personal project; no releases or stars visible on the fetched page; demo site hasanmajid.github.io/open-note/ UNVERIFIED (could not fetch).
- Key features: dual-layer rendering (GPU-cached finished strokes via RepaintBoundary vs in-progress stroke), pressure-sensitive pens, stroke + area/precision erasers, stylus/palm rejection, lasso selection with move/scale/rotate (15° snapping), rich text boxes with non-destructive formatting, OneNote-style Notebooks > Sections > Pages hierarchy, pinch-zoom/pan canvas, page templates (blank/ruled/grid), JSON storage.
- Relevance: the rendering architecture note (cache finished strokes, separate layer for the live stroke) is exactly the canvas performance pattern our Rust app needs; feature list is a compact spec of what stylus users expect (precision eraser, lasso transforms, palm rejection).
- Sources: https://github.com/HasanMajid/open-note , https://hasanmajid.github.io/open-note/ (UNVERIFIED)

## Lukas-Novak/diktafon
- What it is: a fork of jaromiru/diktafon: open-source voice-memo app organized like cassette tapes, transcribing and summarizing entirely on-device. The fork adds opt-in cloud backup and opt-in cloud transcription to your own server, off by default.
- Stack: Flutter (Android, iOS, Linux); vendored whisper.cpp + llama.cpp; Silero VAD; on-device models (Whisper transcription, Qwen summaries). MIT.
- Maturity: released on F-Droid, Google Play, App Store; SHA256SUMS + GitHub build-provenance attestations; upstream "designed by Jaromír Janisch, implemented by Claude Code."
- Key features: tape metaphor (cassettes as continuous gapless recordings), tap-to-seek transcripts, per-memo and per-cassette summaries/titles, noise-aware transcription (VAD + rumble filter), auto language detection per memo, export/import archives, opt-in self-hosted sync with durable retry.
- Relevance: the fork's design is a case study in consent-first cloud: everything local by default, cloud strictly opt-in, per-consent fallback after failed local attempts. The "your own server + durable retry" ingest model maps well onto optional E2EE sync. Also shows AI transcription/summary as an expected notes-app feature in 2026.
- Sources: https://github.com/Lukas-Novak/diktafon

## MyScript/MyScriptJS (and MyScript org)
- What it is: archived JS SDK for handwriting recognition in web apps (signal capture, digital ink rendering, recognition via MyScript Cloud). Succeeded by iinkJS ("Interactive Ink"); org instructs users to move to iinkJS and discontinue ready-made web components.
- Stack: JavaScript, Apache 2.0; React/Angular/Vue example integrations; requires MyScript developer account/API keys; recognition happens in MyScript Cloud (not local).
- Maturity: archived (last update Jan 2021 per org listing); iinkJS last touched Jan 2024; org has 18 repos including Interactive Ink SDK examples for iOS/Android/Windows UWP/WPF, a GeoGebra mirror, and a pdf.js fork (11k stars).
- Key features: text and math recognition (200+ math symbols, 65 languages), editing gestures, import/export, styling, typeset.
- Relevance: confirms handwriting recognition in notes apps is dominated by a cloud-vendor SDK, which conflicts with local-first/E2EE. For us: keep ink as vector geometry in the file format so HTR can be added later (local or pluggable), and note MyScript's own UI reference implementations as interaction-design reference for interactive ink.
- Sources: https://github.com/MyScript/MyScriptJS , https://github.com/orgs/MyScript/repositories

## NicTanghe/BasScript
- UNVERIFIED: the repo URL could not be fetched and searches for "NicTanghe BasScript" returned nothing on point (only LibreOffice's unrelated "BasicScript"). The org exists (44 repos, Rust developer per another search result) but this specific repo's content is unknown. Recommend checking manually in the browser.
- Sources: https://github.com/NicTanghe/BasScript (UNVERIFIED), https://github.com/NicTanghe (profile snippet via search)

## Niko1221/Strata
- What it is: not a notes app: a local AI inference engine, "Qwen3.8-Flash-Next on any consumer hardware," one-click install for Windows/Linux (also Mac), OpenAI/Anthropic-compatible APIs on localhost, optional image input. Desktop + terminal apps.
- Stack: Rust; GGUF-quantized models from ISTA-DASLab/Unsloth; disk-streaming for models larger than RAM; supports NVIDIA RTX, AMD Radeon, Intel Arc, Apple Silicon.
- Maturity: v0.2.6 installers published; versioned benchmarks against named hardware; MIT.
- Key features: `strata launch` per-model engine download, `strata connect` for coding tools (Claude Code, Codex CLI, etc.), desktop app with chat/files/live preview, benchmark tables per GPU.
- Relevance: the obvious local-AI companion for a local-first notes app: if our app wants AI features (summarize, HTR, semantic search) without cloud, an OpenAI-compatible localhost server like Strata is the integration path (same pattern nexlore/diktafon use). Also a UX benchmark for one-click local AI installs.
- Sources: https://github.com/niko1221/strata

## PellelNitram/xournalpp_htr
- What it is: Xournal++ HTR: handwritten text recognition for Xournal++, turning handwritten pages into searchable text; solo research project by Martin Lellep (Univ. of Edinburgh), GPL-2.0.
- Stack: Python ML stack; acknowledges building on public HTR repos (SimpleHTR, WordDetectorNN, HTRPipeline); no-install online demo on HuggingFace; demo video; docs site for install/usage/contribution.
- Maturity: research-grade solo project, actively cited (software citation block); funding via donations; README is thin (points to docs site).
- Key features: HTR for Xournal++ handwritten notes, online demo, structured docs for users and developers.
- Relevance: evidence that "search what you wrote by hand" is a wanted feature in inking apps (e-journal ranks it #3 in its roadmap too). Teaches that HTR can ship as a separate add-on process against existing ink files rather than core; our file format should keep strokes with stable IDs so an HTR layer can attach recognized text.
- Sources: https://github.com/PellelNitram/xournalpp_htr

## ThatSheepGuy22/ObbyNotes
- UNVERIFIED: direct fetch refused and web search found no trace of this repo (possibly new, renamed, private or deleted). Nothing could be established about it. Recommend manual browser check.
- Sources: https://github.com/ThatSheepGuy22/ObbyNotes (UNVERIFIED)

## cheeterdev/notes
- What it is: "Cheeter Notes is the Notes App which does not need a tutorial first" ("Just Notes, Nothing else."). Essentially an idea-stage repo: README plus one screenshot image.
- Stack: none visible yet; 5 commits total.
- Maturity: skeleton/pre-launch; no code, no releases visible.
- Key features: positioning only: zero-learning-curve notes. No implementation to evaluate.
- Relevance: the tagline is itself the finding: the pitch people reach for is "a notes app you don't need a tutorial for." Onboarding-free simplicity is the differentiation claim of choice in this space.
- Sources: https://github.com/cheeterdev/notes

## daijro/openplayground, PR #6
- What it is: openplayground is daijro's live gallery of web apps; PR #6 (by a community member, name withheld, Oct 2026) replaces the generic sample notebook with NoteCraft's bundled full HTML "Welcome to NoteCraft" demo, and updates the live-app test.
- Stack: connects to NoteCraft's Rust/WASM (Trunk) build; verified in headless Chrome at 1440x1000 with zero browser errors.
- Maturity: small PR; owner (daijro) responded "Thanks for the PR!" (unmerged as of fetch).
- Key features: proves a Rust canvas notes app compiles to WASM and runs its full HTML demo in a plain browser tab.
- Relevance: a Rust+egui/wgpu (or similar) notes app can have a first-class web deployment; a "Welcome notebook" bundled demo is a good onboarding pattern worth copying.
- Sources: https://github.com/daijro/openplayground/pull/6

## gtg922r/obsidian-numerals
- What it is: Obsidian plugin "Numerals" that turns math code blocks (and inline expressions) into a full calculator: units, currencies, variables, functions, frontmatter/Dataview metadata, cross-note references. Inspired by Numi, Numbr, Soulver.
- Stack: TypeScript, esbuild-bundled Obsidian community plugin; mathjs engine; strict reproducible-build and release-governance policies.
- Maturity: stable 1.10.2 in the Community Plugins browser; 1.11.0 "recovery preview" in development (unpublished).
- Key features: inline `#:` calculations, show-your-work `#=:` mode, math blocks with `=>` result highlighting, unit/currency math, note-wide `$variables`, `@prev`/`@total`, frontmatter and cross-note `[[note]].property` references, result write-back into notes, autocomplete, click-to-edit rendered blocks, multiple layouts/formats.
- Relevance: demonstrates "living calculations inside notes" as a feature users want; the lessons for a block/canvas app are: results stay coupled to source lines (click-to-edit), calculations can reference document metadata and other documents, and versioned release governance matters once users depend on you.
- Sources: https://github.com/gtg922r/obsidian-numerals
