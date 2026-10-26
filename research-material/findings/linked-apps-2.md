# Linked apps research — Part 2 (linked product pages)

Findings from linked product pages, essays, plugins and community links. Every claim cited with URL; pages not fetched this pass are marked so, with content from general knowledge or the project's own Discord/pasted documents (flagged per line). Project lens: Rust local-first canvas/block notes app with E2EE, handwriting, universal search.

## Ideon — self-hosted spatial canvas, everything is a block
- What: a self-hosted spatial workspace where every item on the canvas is a block with x/y coordinates; blocks connect with optional text labels, group and move together (from a previous run's verified notes; site not re-fetched this pass).
- Key features: infinite 2D canvas with zoom/pan and multi-user live cursors; projects as containers (metadata, block/link graph, access control, undo/redo plus manual snapshots with intent, asset folder); folders, sharing, trash. Published block taxonomy of nineteen types — Core, Note (Markdown), Snippet (code), plus Shell, Webhook, Cron, Kanban with custom fields among them.
- Relevance: the closest existence proof of the block-as-canvas-unit data model — position is data, connections carry meaning, CRDTs handle sync. The nineteen-type taxonomy is a direct blueprint for our block-type design; Shell/Webhook/Cron show how far "everything is a block" can be pushed.
- Sources: https://www.theideon.com/ (content from prior-run notes; page not re-fetched this pass)

## Tangent Notes — open-source tangential Markdown writing
- What: clean, powerful open-source notes app for Mac, Windows and Linux, Apache 2.0.
- Key features: tangential writing — link to existing notes or create new ones without losing your train of thought; a branching map of your notes builds itself as you write, visualized with sliding panels so you always know where you are; notes are local Markdown files readable by any text editor; free forever.
- Relevance: proof that a non-canvas spatial model (branching panels) can express thought paths; local-plain-files with zero hidden state is exactly our storage thesis.
- Sources: https://www.tangentnotes.com/ (fetched mkh-1)

## Amphi — iPad study canvas with widgets and AI tutors
- What: iPad study workspace putting notes, documents, flashcards, timers, calculators and AI tutors on one canvas, built by students to fix app fragmentation (prior-run verified notes; not re-fetched).
- Key features: widget model — Research, Document Viewer, Scientific Calculator, YouTube, Desmos, Wolfram Alpha, To-Do List, Pomodoro widgets sit on the canvas next to the work; AI chat, AI lasso tools (Next, Find, Explain, Check), build-your-own tutors, AI-generated flashcards using on-canvas context. Tiers: free (unlimited canvases, PDFs, iCloud sync), Student £0.99/mo, Pro £9.99/mo (AI credits). Recent handwriting release improved stroke saving, navigation and undo/redo.
- Relevance: source of the widget-on-canvas model — tools live where the work is instead of split panes; AI that reads the visible canvas context is a pattern our lasso/selection AI should copy.
- Sources: https://www.useamphi.com/ (content from prior-run notes; not re-fetched this pass)

## WorkFlowy — the outliner
- What: web/desktop/mobile infinite outliner: zoomable bullet-list hierarchy, one of the oldest structured-thinking tools (page not fetched this pass; description from general knowledge — verify).
- Key features: infinite nesting with zoom-to-branch, mirroring/duplication of bullets, tags, search, sharing of subtrees.
- Complaints: cloud-only, no local files or E2EE; free tier item caps.
- Relevance: the zoomable-outline is the 1-D ancestor of our 2-D canvas; its zoom semantics (a block becomes the whole view) map directly onto canvas focus mode; mirroring shows why block references matter.
- Sources: https://workflowy.com/

## Goodnotes — tablet handwriting incumbent (+ store listings)
- What: the most popular tablet note-taking app for students, with PDF annotation, handwriting search and handwriting-to-text.
- Platforms: iPad-first (historically effectively iPad-exclusive), plus store listings for Android (https://play.google.com/store/apps/details?id=com.goodnotes.android.app) and iOS (https://apps.apple.com/us/app/goodnotes-ai-notes-docs-pdf/id1444383602, "AI Notes, Docs, PDF"); subscription pricing.
- Community verdict (Discord thread, 14 Oct 2026): "exclusive to iPads, and costs a monthly premium"; "the lack of good free note taking Apps on iPadOS and Android Tablets has been an issue for a while… FOSS Apps are even more bleak"; the community wants a fleshed-out open-source tablet notes app supporting PDF files "like Goodnotes"; Goodnotes named the likely benchmark for parity because a free trial showcases most features. Known user asks: per-document handwriting-recognition language and searchable PDFs (raised in the sibling OneNote/Obsidian thread).
- Relevance: our project is the FOSS answer to exactly this gap: tablet handwriting + PDF annotation + handwriting search, cross-platform and offline.
- Sources: https://www.goodnotes.com/ ; https://play.google.com/store/apps/details?id=com.goodnotes.android.app ; https://apps.apple.com/us/app/goodnotes-ai-notes-docs-pdf/id1444383602 ; community thread in project Discord export (Goodnotes_Amphi_NoteShelf channel)

## Squid (formerly Papyrus) — Android ink notes
- What: the Play listing com.steadfastinnovation.android.projectpapyrus is Squid (Steadfast Innovation's "Papyrus" project), a vector-ink note-taking app for Android (page not fetched this pass; identification from package name and community context — verify).
- Key features: pressure-sensitive vector ink on paper/PDF, no handprint flattening, cloud sync via Google Drive on paid tier.
- Community verdict: "There is Squid on Android… but it lacks many of the capabilities Goodnotes has."
- Relevance: the Android ink baseline to beat; its vector-ink storage is the model for our handwriting layer.
- Sources: https://play.google.com/store/apps/details?id=com.steadfastinnovation.android.projectpapyrus

## Akasha — local-only encrypted notes (Microsoft Store 9n3xffmbl7kx)
- What: the mystery app at apps.microsoft.com/detail/9n3xffmbl7kx is Akasha, a local-only encrypted desktop notes application built with Flutter, free on the Microsoft Store (listing dated August 2026).
- Relevance: a small-scale precedent for local-only encrypted notes on Windows; Flutter (not Rust) and no sync, which leaves the local-first + sync + Rust lane open for us.
- Sources: https://apps.microsoft.com/detail/9n3xffmbl7kx (identified via search, fhb-1)

## Samsung Notes — free Android benchmark
- What: Samsung's pre-installed notes app; the support page covers sync via Samsung Cloud/OneDrive, PDF import, annotation and handwriting (page not fetched this pass; description from general knowledge — verify).
- Community verdict: "popular contender… surprisingly feature complete in terms of PDF editing, which is good UI. It might also be easier to benchmark against than Goodnotes because it is available for free on Google Play and Android."
- Relevance: the recommended zero-cost benchmark for our tablet feature parity: free, Android, PDF + ink.
- Sources: https://www.samsung.com/us/support/owners/app/samsung-notes ; community thread (Goodnotes_Amphi_NoteShelf)

## Ink & Switch — "Malleable Software" essay
- What: the Ink & Switch research essay arguing software should be malleable: users should be able to change, extend and remake their tools rather than consume fixed apps (page not fetched this pass; thesis from general knowledge of the essay — verify).
- Key content: tool-makers not tool-users; end-user programming and tool ecosystems; the observation that AI may finally make malleable software practical; builds on their local-first computing research line.
- Relevance: the intellectual foundation for our plugin language (sandboxed JS per the spec) and for user-authored blocks; cite it in our design doc when justifying programmability.
- Sources: https://www.inkandswitch.com/essay/malleable-software/

## monogr.ph/s/OHwf5C9o8E — our own spec ("Features I Would Like in A Notes App", v5)
- What: the project's single document: the decisions, the full spec, the per-app inventory with links, the data model, the build sequence, and what is still unverified. A private, open-source, local-first notebook where you write on one infinite canvas and everything else — sorting, OCR, transcription, search — derives from that canvas (its own OG description, from the project's pasted copy of the document).
- Feature list and decisions locked in Part I: canvas is primary, notes are derived objects; sync follows Ente's model — fully local, self-hosted, zero-knowledge, no hosted tier required; handwriting scope is anything (stylus, finger, scanned paper, photographed-page OCR); self-hosted Docker deploy, no vendor cloud; plugin language is sandboxed JavaScript; AI ships with a small local model, offline, day one; speed is a first-class architectural constraint targeting Thymer's feel; editing files and video is core; tabs and an internal browser are core; everything is searchable always, indexed on arrival with nothing to opt into; plain-file storage (Markdown on disk) tagged [v1], citing Thymer's Markdown Mirror as prior art; open formats, export everything.
- Tag scheme: [MVP] first usable version, [v1] first real release, [PLUGIN] not in core, [LATER] wanted not scheduled; guiding rule: core stays small and boring, plugins make it yours.
- Relevance: this is the document our research feeds; every finding above should be read against its Part II sections (canvas, blocks, sync, search, handwriting).
- Sources: https://monogr.ph/s/OHwf5C9o8E (content confirmed from the project's pasted copy of the document; live page not re-fetched this pass)

## Notesnook Monographs — publish notes as web pages
- What: Notesnook's publishing feature that turns a note into a shareable public web page (a "monograph") (page not fetched this pass; description from general knowledge — verify).
- Relevance: the E2EE-notes-app answer to publishing; pairs with Obsidian Publish below — publishing must not compromise the encrypted-at-rest model (Monographs publishes only what you explicitly push).
- Sources: https://notesnook.com/help/publish-notes-with-monographs

## Obsidian Publish — hosted note publishing
- What: Obsidian's paid add-on publishing a vault (or a selected folder) to a hosted, themeable wiki-style site with graph navigation and backlinks (page not fetched this pass; description from general knowledge — verify).
- Relevance: the incumbent publishing story our local-first app competes with; a static-site export from Markdown files would be our free version.
- Sources: https://obsidian.md/publish

## Obsidian plugin: Badges
- What: community plugin rendering inline GitHub-style badges in notes (page not fetched this pass; description from general knowledge — verify).
- Relevance: example of the small-renderer plugin genre our sandboxed-JS plugin system must accommodate; also a hint that status/metadata chips belong in the block model.
- Sources: https://community.obsidian.md/plugins/badges

## Obsidian plugin: InkedMark
- What: community plugin adding ink/handwriting marks into Markdown notes (page not fetched this pass; content unverified — the plugin's exact behavior was not confirmed this pass).
- Relevance: directly relevant as prior art for handwriting embedded in Markdown files — precisely the tension between our ink blocks and the plain-file mirror; needs a proper look in the storage thread.
- Sources: https://community.obsidian.md/plugins/inkedmark — UNVERIFIED content

## Obsidian plugin: Excalidraw
- What: the flagship Obsidian drawing plugin: full Excalidraw canvas embedded in the vault, drawings stored as JSON-in-Markdown or SVG, with links from shapes to notes and embedded mini-views (page not fetched this pass; description from general knowledge — verify).
- Complaints: heavy, slow on big drawings; JSON-in-Markdown is awkward for external tools.
- Relevance: the main precedent for canvas-inside-Markdown-vault; its shape-as-link and embed-back features are the canvas↔note bridge prior art our spec's Thread B asks for.
- Sources: https://community.obsidian.md/plugins/obsidian-excalidraw-plugin

## Obsidian plugin: List Callouts
- What: community plugin adding styled callouts to individual list items rather than whole blocks (page not fetched this pass; description from general knowledge — verify).
- Relevance: shows user demand for per-line styling inside text blocks; our block model gets this for free via block attributes.
- Sources: https://community.obsidian.md/plugins/obsidian-list-callouts

## Obsidian plugin: Meta Bind
- What: community plugin embedding interactive input fields (buttons, toggles, selects, progress) bound to note frontmatter (page not fetched this pass; description from general knowledge — verify).
- Relevance: precedent for bidirectional UI↔data binding inside notes — a light version of what our block properties with schema would do natively.
- Sources: https://community.obsidian.md/plugins/obsidian-meta-bind-plugin

## Obsidian plugin: Sheets
- What: community plugin embedding Excel-like spreadsheet cells inside Markdown notes (page not fetched this pass; description from general knowledge — verify).
- Relevance: tables-with-formulas as a block type; supports the spec's position that editing office-like content is core.
- Sources: https://community.obsidian.md/plugins/sheets

## OwlLuna — Swift iPad handwriting canvas
- What: an open-source iPad handwriting/canvas app by owaisazmal, with story docs at the site; its GitHub repo shows Swift canvas code (PageStack, ZoomWindow, EditorScreen) and active issues/PRs (site not fetched this pass; details from cached repo references — verify).
- Key features observed in references: pens and an eraser with two modes, text selection, snapping highlighter, zoom windows; privacy-by-design — "nothing is recorded behind another app or behind a notebook's lock"; small-target findings (36pt swatch buttons, 28pt sidebar chevrons) recorded as issues.
- Relevance: open-source Swift reference for the pen/eraser/highlighter interaction vocabulary and for privacy decisions in a recording-capable ink app; also a reminder that hit-target sizes are a real accessibility finding.
- Sources: https://owaisazmal.github.io/OwlLuna/ (and repo https://github.com/owaisazmal/OwlLuna)

## Laplace — strongcod3r notes project
- What: a GitHub Pages project site under strongcod3r (page not fetched this pass and not covered by searches this pass — content UNVERIFIED; generic "Laplace" web results were unrelated apps).
- Relevance: unresolved; needs the repo link or a direct look before any claim is made.
- Sources: https://strongcod3r.github.io/laplace/ — UNVERIFIED

## NoteCraft (base44) — AI-built notes app attempt
- What: a notes app built on Base44, the no-code AI app-builder platform (site not fetched this pass). Community-sourced Base44 verdicts: "fantastic for rapid prototyping… works well for prototypes, but not for running apps in production."
- Relevance: a cautionary datapoint for AI-generated app scaffolds: fine for mockups, not for the production local-first core; our Rust core remains the right approach.
- Sources: https://notecraft-core-studio.base44.app — page not fetched; Base44 verdicts from cached community reviews

## NoteCraft head — playground.daijro.dev/head/notecraft
- What: a headless "notecraft" playground under daijro.dev (fetch refused this pass; content UNVERIFIED).
- Relevance: unknown until fetched; the path suggests a headless/programmatic notes engine worth checking when links allow.
- Sources: https://playground.daijro.dev/head/notecraft/ — UNVERIFIED

## Nostr — the protocol
- What: Notes and Other Stuff Transmitted by Relays: a simple, stateless relay-based protocol for distributed social/event publishing using keypairs (site not fetched this pass; description from general knowledge — verify).
- Relevance: candidate transport layer for P2P/decentralized sync and publishing of notes (relays as optional sync endpoints, keys as identity); pairs with iroh for direct transport.
- Sources: https://nostr.org/

## Bouquet — nostrapps.com/bouquet
- What: dead link — the page returned HTTP 404 this pass; no content to summarize.
- Relevance: Bouquet is known elsewhere as a Nostr web client, but nothing verifiable here; mark for re-check or drop from the inventory.
- Sources: https://nostrapps.com/bouquet — 404 / UNVERIFIED

## Obsidian Nostr Writer — nostrapps.com listing
- What: a Nostr-related writer/Obsidian integration listed on nostrapps.com (page not fetched this pass; content UNVERIFIED).
- Relevance: if real, prior art for publishing Markdown notes to Nostr relays; verify the repo before citing further.
- Sources: https://nostrapps.com/obsidian-nostr-writer — UNVERIFIED

## Iroh (VPN use case) — dial keys, not IPs
- What: iroh is a Rust P2P networking library; the VPN page pitches it as replacing Tailscale/WireGuard/reverse-SSH for app-to-device connectivity.
- Key features: every node addressed by public key; NAT/firewall punching for direct connections; end-to-end encrypted by default so the platform cannot see traffic; ships as a library inside your app — no separate client, no coordination server, no ports; explicitly not a whole-device network overlay.
- Relevance: the strongest candidate for our device-to-device sync transport: a self-hosted server becomes optional because peers can dial each other directly, and E2EE is inherent; iroh is Rust, fitting our stack.
- Sources: https://www.iroh.computer/solutions/vpn (fetched t5a-1)

## Swift SDK for Android — getting started (swift.org)
- What: Swift's official article on building an Android toolchain and running Swift code on Android via SPM/gradle plugin (page not fetched this pass; description from general knowledge of the article — verify).
- Relevance: competitive intel only: it lowers the cost of shipping Swift handwriting/canvas components cross-platform, which weakens the "Rust core + native shells" uniqueness argument; our response is Rust's single-language core covering desktop, mobile and (via WASM) web.
- Sources: https://www.swift.org/documentation/articles/swift-sdk-for-android-getting-started.html

## Pandoc grid tables — extension demo
- What: Pandoc's documentation demo page for the grid_tables Markdown extension: tables with block elements (lists, code, even tables) inside cells, arbitrary column widths, multi-line content (page not fetched this pass; the URL anchors the extension docs — verify).
- Relevance: prior art for the plain-file mirror problem: if our block canvas mirrors to Markdown, grid tables (or a similar block-carrying Markdown dialect) are the known vocabulary for rich blocks in .md files.
- Sources: https://pandoc.org/demo/example33/8.9-tables.html#extension-grid_tables

## Microsoft Graph Explorer — API console
- What: Microsoft's in-browser console for composing and running Graph API calls, including the OneNote API surface (page not fetched this pass; description from general knowledge — verify).
- Relevance: the quickest way to probe OneNote's cloud data model (sections/pages/freeform content) when designing our import path alongside the onenote_parser crate (see linked-apps-1).
- Sources: https://developer.microsoft.com/en-us/graph/graph-explorer

## remade.wiki — the community's app-remake tracker (8 pages)
- What: remade.wiki tracks community app-remake projects with maintainer-reported status, compatibility, languages, platforms, licenses, known limitations and refreshed GitHub stats. The eight listed pages:
- **prosecraft** (https://remade.wiki/projects/prosecraft) — remake page for ProseCraft; not fetched this pass, details UNVERIFIED.
- **capsulecraft** (https://remade.wiki/projects/capsulecraft) — matches the Discord-shared repo: CapsuleCraft, "zero-database, pure-MIME multimodal workspace and personal knowledge engine. Every note is an RFC 5322 .eml file" (from the community-shared GitHub embed); page itself not fetched.
- **open-notebook** (https://remade.wiki/projects/open-notebook) — fetched: experimental, partial (claimed) parity, Python + TypeScript, web, MIT; limitations: own storage/interfaces/provider config, no established Google-notebook import or account sync; needs hosting and configured models; 40.6k stars, 4,663 forks, active (push 5 days ago).
- **notecraft-onenote** (https://remade.wiki/projects/notecraft-onenote) — OneNote-parity project page; not fetched this pass, details UNVERIFIED.
- **open-note** (https://remade.wiki/projects/open-note) — matches the community-shared repo https://github.com/HasanMajid/open-note; page not fetched this pass.
- **e-journal** (https://remade.wiki/projects/e-journal) — not fetched this pass, details UNVERIFIED.
- **notecraft** (https://remade.wiki/projects/notecraft) — fetched: experimental Rust Notepad-remake targeting Windows, MIT; limitations: repo created 11 Oct 2026, spec and foundation in progress, listed workflows are goals not features, reference Notepad unpinned, parity report has no measurements; 5 stars, 1 fork.
- **scriptcraft** (https://remade.wiki/projects/scriptcraft) — not fetched this pass, details UNVERIFIED.
- Relevance: this wiki is the public scoreboard of the remake wave our project belongs to; open-notebook shows what a successful remake looks like (MIT, 40k stars, honest limitation reporting), and notecraft shows the early-stage end of the curve.
- Sources: the eight URLs above (open-notebook ugh-1, notecraft q5r-1; others not fetched this pass)

## Reddit — Pele, new Mermaid renderer for Obsidian
- What: an r/ObsidianMD thread announcing Pele, a new renderer for Mermaid diagrams coming to Obsidian (title from the URL; thread body not fetched this pass — content UNVERIFIED).
- Relevance: diagram rendering is again a core-expectation feature (HelixNotes ships Mermaid too); Pele suggests the field is moving to faster Mermaid pipelines — worth tracking for our canvas text blocks.
- Sources: https://www.reddit.com/r/ObsidianMD/comments/1x8dp2r/pele_new_renderer_for_mermaid_diagrams_coming_in/

## X post — pwnies/status/2098138440097493382
- What: an X (Twitter) post linked by the community; content not fetched and not captured in any cached search this pass — UNVERIFIED, nothing to summarize without inventing.
- Sources: https://x.com/pwnies/status/2098138440097493382 — UNVERIFIED

## X post — sheherenow_/status/2104637183793807643
- What: an X (Twitter) post linked by the community; content not fetched this pass — UNVERIFIED.
- Sources: https://x.com/sheherenow_/status/2104637183793807643 — UNVERIFIED

## YouTube video — watch?v=_K-ExOiEv40
- What: a YouTube video linked by the community; not fetched this pass and no transcript or title captured in cached results — UNVERIFIED, no claims made.
- Sources: https://www.youtube.com/watch?v=_K-ExOiEv40 — UNVERIFIED
