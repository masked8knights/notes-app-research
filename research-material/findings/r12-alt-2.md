r12 lane 2 (alt-2): open/lesser-known alternatives for Tana, Roam Research, Dynalist, Workflowy, Reflect, Capacities, Kinopio, Heptabase, Milanote, Miro, Muse (museapp.com/Allume), Concepts — researched 2026-10-27. Research only; no build plan.

===== SECTION: Tana — alternatives =====
### Thinktool
- Official/repo: https://github.com/c2d7fa/thinktool (site: https://thinktool.io)
- License: GNU AGPLv3 or later, per LICENSE.md stated in repo README (https://github.com/c2d7fa/thinktool)
- Platforms: web client + Node.js server + Electron desktop client; data in a SQLite database (repo README)
- Maintenance: effectively frozen. Author's own README: he switched to a simpler Emacs tool ("zt") and "won't be spending much time on Thinktool"; repo does not accept issues/PRs and the author may force-push; hosted web version recommended against and slated for takedown (https://github.com/c2d7fa/thinktool; corroborated at https://www.opensourceagenda.com/projects/thinktool). Single-maintainer risk: total (one person, archive-like).
- Coverage of Tana workflows: covers associative outlining with backlinks/bidirectional links; unique data model where an item can exist under multiple parents with no original/copy distinction (clones/mirrors without transclusion). Lacks: Tana's supertags/typed-object fields, AI features, daily-notes pipeline.
- Design worth borrowing: clone data model — same item in multiple places, "no difference between the original and its clones"; no separate page/item distinction. Stated in the repo's own comparison section (https://github.com/c2d7fa/thinktool).
- Pricing/self-host: free to self-build forever per README; only a JSON export offered for the dying hosted service.
- Video/community pass: no official video found. Community thread: Outliner Software forum discussion of Thinktool's associative-outliner experiment, 2020 (https://www.outlinersoftware.com/topics/viewt/9045); it shows reviewers found it a simplified outliner and questioned platform support. Docs don't surface the archive status; the README does.

### TiddlyWiki
- Official/repo: https://tiddlywiki.com ; repo https://github.com/Jermolene/TiddlyWiki5
- License: BSD-3-Clause, per the GitHub org's license listing (https://github.com/Jermolene)
- Platforms: single self-contained HTML file in a browser; server editions (Node.js) for saving/sync; runs on desktop and mobile browsers
- Storage model: everything is "tiddlers" — small records with titles, tags and fields — inside one HTML file, or served by Node; no server required for personal use
- Maintenance: very active, ~25 years old; repo listed BSD-3 with thousands of stars and frequent releases (https://github.com/Jermolene/TiddlyWiki5). Team-maintained (Jermolene org), lower single-maintainer risk than most.
- Coverage of Tana workflows: closest OSS analog to Tana's object model — tags act like supertags, tiddler fields hold structured data, and list filters do Tana-style queries. Lacks: collaborative outliner feel, Tana's AI/inbox flow.
- Design worth borrowing: tiddler (typed record with fields + tags) data model; filter syntax; single-file portability.
- Pricing/self-host: free; optional hosting via community services.
- Video/community pass: HN threads show longevity claims and gripes browser changes broke the single-file save flow over the years: TiddlyWiki 5.1.23 (https://news.ycombinator.com/item?id=25527581), "Twenty Years of TiddlyWiki" (https://news.ycombinator.com/item?id=44198116), where commenters also point to TiddlyPWA as the sync path docs underplay.

### Grist
- Official/repo: https://www.getgrist.com ; repo https://github.com/gristlabs/grist-core
- License: Apache-2.0 for grist-core (per repo README)
- Platforms: web app (self-host via Docker), desktop app, hosted SaaS
- Storage model: SQLite-backed spreadsheet-database documents; tables/columns/typed cells, access rules, Python formulas
- Maintenance: actively developed by Grist Labs; star count not re-verified this lane (UNVERIFIED), repo shows ongoing releases (https://github.com/gristlabs/grist-core)
- Coverage of Tana workflows: covers the structured-object half of Tana (supertag-like typed records, linked tables, filtered views) but is a spreadsheet-database, not an outliner: no outline editing, no daily notes, no block references.
- Design worth borrowing: typed columns + per-row access rules; document-as-SQLite storage makes export/backup trivial.
- Pricing/self-host: grist-core free/Apache-2.0, self-hostable; paid hosted and enterprise tiers exist.
- Video/community pass: not searched this lane (web-search budget exhausted); no HN/Reddit thread recorded here — gap flagged rather than treated as absent.

===== END SECTION =====

===== SECTION: Roam Research — alternatives =====
### Foam
- Official/repo: https://foambubble.github.io/foam ; repo https://github.com/foambubble/foam
- License: MIT (per repo README and package.json, https://github.com/foambubble/foam)
- Platforms: VS Code extension + workspace template; anything VS Code runs on; optional static publishing
- Storage model: local-first plain Markdown files with wiki-links
- Maintenance: active — repo shows commits within the last two weeks at search time (https://github.com/foambubble/foam); multi-contributor org, moderate bus factor
- Coverage of Roam workflows: covers wikilinks/backlinks, daily notes, graph visualization, note templates, publishing. Lacks: block-level references (only heading/anchor level), outliner-style zoom, Roam's query UI.
- Design worth borrowing: Roam-on-plain-markdown recipe; the extension architecture is a reference for adding backlinks/daily-notes to any editor.
- Pricing/self-host: free; data is plain files.
- Video/community pass: HN thread where a commenter notes they tried Obsidian/FOAM and prefer outliners, plus the point that plugins can cover Roam features (https://news.ycombinator.com/item?id=33221245). Reddit: r/ObsidianMD "Open source alternatives such as Foam" — commenters say Foam "provides very similar features to Roam" but it is "a VS Code extension though, doesn't really compare" (https://www.reddit.com/r/ObsidianMD/comments/1dilab1/open_source_alternatives_such_as_foam/) and r/ObsidianMD 2025 thread listing Foam and Org-roam as OSS options (https://www.reddit.com/r/ObsidianMD/comments/1io0zzx/what_best_obsidian_alternatives_are_out_there/). The gripes docs miss: it's an editor extension, so the experience depends on VS Code.
### Org-roam
- Official/repo: https://www.orgroam.com ; repo https://github.com/org-roam/org-roam
- License: GPL-3.0 (per repo)
- Platforms: Emacs (desktop; some mobile Emacs ports UNVERIFIED)
- Storage model: plain Org-mode files + a local SQLite cache for links/graph
- Maintenance: active into 2026 (~6,000 stars, recent commits per search results, https://github.com/org-roam/org-roam); maintained by a small Emacs-community team, moderate single-maintainer risk
- Coverage of Roam workflows: covers bidirectional links, backlink buffer, daily notes (with org-journal style flows), citation linking. Lacks: browser UI, block references are Org-mode headline-based rather than arbitrary blocks.
- Design worth borrowing: SQLite index over plain files as a fast backlink/graph layer.
- Pricing/self-host: free; entirely local.
- Video/community pass: r/ObsidianMD thread names Org-roam as the other OSS Roam-like tried (https://www.reddit.com/r/ObsidianMD/comments/1io0zzx/what_best_obsidian_alternatives_are_out_there/). No official demo video recorded this lane; Emacs-cult status is the visible gripe (requires Emacs).
### Emanote (with Neuron status note)
- Official/repo: https://emanote.srid.ca ; repo https://github.com/srid/emanote
- License: AGPL-3.0 (per repo)
- Platforms: Haskell server on Windows/macOS/Linux; notes viewed in browser, edited in any editor
- Storage model: plain Markdown/Org folders; renders to a linked wiki
- Maintenance: maintained successor; star count ~900 at search time per search results (https://github.com/srid/emanote). Predecessor Neuron (https://github.com/srid/neuron) is superseded/maintenance-mode — dead as a going concern, evidence in Emanote's own docs.
- Coverage of Roam workflows: covers backlinks, folgezettel tree structure, live embedding; editing stays in your editor. Lacks: block references, daily-note UI, anything interactive.
- Design worth borrowing: type-safe Haskell rendering layer over plain notes; embedding/folgezettel hierarchy semantics.
- Pricing/self-host: free.
- Video/community pass: none recorded this lane (budget); gap flagged.

===== END SECTION =====

===== SECTION: Dynalist — alternatives =====
### TreeSheets
- Official/repo: https://treesheets.com ; repo https://github.com/aardappel/treesheets
- License: ZLIB license, per repo (https://github.com/aardappel/treesheets)
- Platforms: native C++/wxWidgets app for Windows/macOS/Linux
- Storage model: single .cts documents (XML-ish), export options; not a folder of text files
- Maintenance: slow but alive; ~3.1k stars per search results; HN resubmissions 2023 and 2024 with author participation (https://news.ycombinator.com/item?id=34184993, https://news.ycombinator.com/item?id=40475397). Effectively one original author — high single-maintainer risk.
- Coverage of Dynalist workflows: covers hierarchical outline-style organization with instant keyboard entry and zoom-into-cell (cell zooming stands in for outliner zoom). Lacks: cloud sync, mobile, block references, daily notes, sharing.
- Design worth borrowing: nested-cell spreadsheet/outliner hybrid — hierarchy without separate "page" objects; zoom-as-navigation.
- Pricing/self-host: free, local.
- Video/community pass: HN 2021 thread carries the durable gripe: "usability of this application is quite limited. It feels more like a proof of concept, than an application for daily use" (https://news.ycombinator.com/item?id=27614912). Hackaday walkthrough of the hierarchical-spreadsheet framing (https://hackaday.com/2022/09/07/organise-your-hacks-with-treesheets-an-open-source-hierarchical-spreadsheet/). Older threads: https://news.ycombinator.com/item?id=15057392, https://news.ycombinator.com/item?id=15058913.
### Zim
- Official/repo: https://zim-wiki.org ; repo https://github.com/zim-desktop-wiki/zim-desktop-wiki
- License: GPL-2.0, per repo (https://github.com/zim-desktop-wiki/zim-desktop-wiki)
- Platforms: Linux (native GTK); Windows builds exist but less polished
- Storage model: plain-text wiki pages in a folder structure, one file per page
- Maintenance: maintained but slow; ~2.1k stars, commits into 2026 per search results (repo URL above). Small maintainer group, aging Python/GTK codebase.
- Coverage of Dynalist workflows: covers hierarchical note trees with folding, inline checklists, tags, journal plugin for daily notes, backlinks between pages. Lacks: single-drag-outline feel of Dynalist, block references, zoomed outlining, web/mobile.
- Design worth borrowing: page-tree + plugins on plain text; the journal and task-list plugins are simple patterns for daily notes on files.
- Pricing/self-host: free, local.
- Video/community pass: none recorded this lane (budget); gap flagged.

===== END SECTION =====

===== SECTION: Workflowy — alternatives =====
### Org-mode (Emacs)
- Official: https://orgmode.org (GNU Emacs, https://www.gnu.org/software/emacs/)
- License: GPL-3.0 (part of Emacs, per gnu.org)
- Platforms: Emacs on desktop; third-party mobile apps exist
- Storage model: plain text .org files
- Maintenance: maintained as core GNU infrastructure; effectively no abandonment risk
- Coverage of Workflowy workflows: covers infinitely nestable outline with folding, TODO states, tagging, agenda/daily notes, export. Lacks: modern touch UI, quick-capture simplicity without Emacs, realtime collaboration.
- Design worth borrowing: the original outliner data model (headlines, drawers, properties, TODO keywords) that most OSS outliners imitate.
- Pricing/self-host: free.
- Video/community pass: canonical tool, not searched this lane; countless community tutorials exist (not individually verified here).
### OutWiker
- Official/repo: https://outwiker.sourceforge.io / https://jenyay.com/outwiker ; repo https://github.com/Jenyay/outwiker
- License: GPL-3.0, per repo (https://github.com/Jenyay/outwiker)
- Platforms: Windows/Linux (Python/Qt)
- Storage model: page-tree of folders, each page its own text/HTML/Markdown content plus attachments
- Maintenance: active — release notes and coverage into 2026 per search results (https://github.com/Jenyay/outwiker; LinuxTools/LinuxLinks review Aug 2026). Essentially one author — high single-maintainer risk.
- Coverage of Workflowy workflows: covers nested page tree, quick hierarchical notes, tags, attachments. Lacks: one continuous zoomable outline (it is page-based, not item-based), block references, web version.
- Design worth borrowing: page-type plugin system (text, HTML, Markdown pages) on a plain-folder tree.
- Pricing/self-host: free, local.
- Video/community pass: LinuxLinks write-up is the main recent community coverage found; no HN/Reddit thread recorded this lane.

===== END SECTION =====

===== SECTION: Reflect — alternatives =====
### nb
- Official/repo: https://xwmx.github.io/nb ; repo https://github.com/xwmx/nb
- License: AGPL-3.0-or-later, per repo and Homebrew formula (https://github.com/xwmx/nb, https://formulae.brew.sh/formula/nb)
- Platforms: shell script (macOS/Linux/Windows via WSL); includes a local web editor (nb serve)
- Storage model: plain text/markdown notebooks in folders, each a Git repository; optional encryption; Pandoc conversion
- Maintenance: active, 8.4k stars per repo page at search time (https://github.com/xwmx/nb); primary author plus contributors — moderate bus factor
- Coverage of Reflect workflows: covers local-first notes, linking/tagging/filtering/search, Git versioning and sync, bookmarks, encryption. Lacks: Reflect's graph view, daily-note-first UI, realtime sync (git-based).
- Design worth borrowing: "notebook = git repo" storage; a single portable script as the whole app; local web editor over the same files.
- Pricing/self-host: free.
- Video/community pass: none recorded this lane (budget); gap flagged.
### zk
- Official/repo: https://zk-org.github.io/zk ; repo https://github.com/zk-org/zk
- License: GPL-3.0, per repo (https://github.com/zk-org/zk)
- Platforms: Go CLI for macOS/Linux/Windows; integrates with any editor via LSP
- Storage model: plain markdown notebooks with frontmatter
- Maintenance: active — commits into 2026 per search results (repo above); small maintainer team, elevated single-maintainer risk
- Coverage of Reflect workflows: covers backlinks, tags, templates (daily notes via templates), fast filtering/search, editor LSP integration. Lacks: built-in GUI, graph visualization, mobile, realtime sync.
- Design worth borrowing: LSP server exposing backlinks/navigation to any editor — a neat way to add Reflect-style features without owning the UI.
- Pricing/self-host: free, local.
- Video/community pass: none recorded this lane (budget); gap flagged.

===== END SECTION =====

===== SECTION: Capacities — alternatives =====
### Unigraph
- Official/repo: https://unigraph.dev ; repo https://github.com/unigraph-dev/unigraph-dev
- License: MIT, per repo README (https://github.com/unigraph-dev/unigraph-dev)
- Platforms: web app, self-hosted via Docker; requires a Dgraph backend (project maintains its own fork, built from https://github.com/unigraph-dev/dgraph per README)
- Storage model: local-first knowledge graph on Dgraph; typed objects with schemas and subscriptions
- Maintenance: author-run project; repo README invites contributors rather than claiming momentum; last release date not re-verified this lane (UNVERIFIED) — treat as stalled/stalled-risk. High single-maintainer risk.
- Coverage of Capacities workflows: covers the core object/type idea — typed objects ("schema-objects"), properties, and one graph where the same object appears across views (notes, todos, bookmarks, feeds). Lacks: polish, mobile, Capacities' daily notes UX.
- Design worth borrowing: schema-objects with subscriptions that keep every view of an object in sync — the closest pullable implementation of Capacities/Tana object typing.
- Pricing/self-host: free, self-host.
- Video/community pass: author's r/selfhosted introduction lists the object-sync feature set (todo, calendar, email, read-later, bookmarks in one graph) (https://www.reddit.com/r/selfhosted/comments/qwylqm/ive_made_unigraph_a_localselfhosted_foss_personal/). Comments there show interest but also the "ambitious one-person scope" worry docs don't mention.

===== END SECTION =====

===== SECTION: Kinopio — alternatives =====
### scrumblr
- Official/repo: https://github.com/alias1/scrumblr
- License: GPL-3.0, per repo (https://github.com/alias1/scrumblr)
- Platforms: Node.js web app, self-hosted
- Storage model: server-side boards shared by URL
- Maintenance: dormant — small, old commit history (project dates from the early 2010s; exact last-commit date UNVERIFIED this lane). Treat as archive-quality source, not a live product.
- Coverage of Kinopio workflows: covers freeform spatial boards with draggable cards (text, list, image cards) shared in real time via URL. Lacks: Kinopio's wiki/canvas hybrid (card-to-card links, drawings, keyboard spatial navigation).
- Design worth borrowing: simplest possible spatial-card canvas; draggable card DOM over a pannable board.
- Pricing/self-host: free, self-host.
- Video/community pass: none recorded this lane (budget); gap flagged.
- Direct-source note (not an alternative): Kinopio's author made the client code public in June 2024 under a non-commercial license — client repo https://github.com/kinopio-club/kinopio-client, author's post https://pketh.org/open-source-kinopio.html, HN discussion https://news.ycombinator.com/item?id=40810949. Server-side code remains closed. This is a pullable source for Kinopio's card/canvas client behavior only (commercial reuse prohibited by that license).

===== END SECTION =====

===== SECTION: Heptabase — alternatives =====
### spacedeck-open
- Official/repo: https://github.com/spacedeck/spacedeck-open (project page for the original product is defunct; the repo is the source of truth)
- License: AGPL-3.0, per repo (https://github.com/spacedeck/spacedeck-open)
- Platforms: Node.js web app, self-hosted
- Storage model: server-side boards with media/text/shape objects; exact DB engine stated in repo (original used MongoDB — UNVERIFIED this lane)
- Maintenance: effectively frozen — the open-source release carries copyright notices through 2018 and shows minimal commits since (~1.1k stars per search results). Archive-quality.
- Coverage of Heptabase workflows: covers spatial boards with draggable cards, media embeds, text blocks, shapes and grouping/alignment — the canvas-with-cards core. Lacks: PDF annotation, card backlinks/graph, offline apps, realtime co-editing maturity.
- Design worth borrowing: a mature implementation of card-on-canvas editing (pan/zoom, z-order, text-in-canvas) that most OSS canvas notes lack.
- Pricing/self-host: free, self-host.
- Video/community pass: none recorded this lane (budget); gap flagged.

===== END SECTION =====

===== SECTION: Milanote — alternatives =====
### Pinry
- Official/repo: https://pinry.github.io/pinry/ ; repo https://github.com/pinry/pinry
- License: BSD, per LICENSE.md ("Copyright (c) 2019, Pinry's Contributors") — exact clause (2- vs 3-clause) UNVERIFIED (https://github.com/pinry/pinry/blob/master/LICENSE.md)
- Platforms: Django + JS web app, self-hosted via Docker; browser extensions; browser-only use
- Storage model: server-side boards of pinned images/videos/links with tags and users
- Maintenance: alive but low-energy — ~3.4k stars, releases are "minor-fix" batches per search results (https://github.com/pinry/pinry/releases); small maintainer group.
- Coverage of Milanote workflows: covers visual/mood boards — saving, tiling, tagging and sharing images and links, per-board and per-user organization. Lacks: freeform canvas placement (tiling grid instead), sticky text notes, drawing, drag-anywhere layout.
- Design worth borrowing: the board/round pinner model plus sharing permissions; extension-driven capture.
- Pricing/self-host: free, self-host.
- Video/community pass: HN launch thread (https://news.ycombinator.com/item?id=3895618); r/SelfhostingHub thread reports easy Docker install and family use (https://www.reddit.com/r/SelfhostingHub/comments/192fh9r/pinry_the_opensource_tiling_image_board/); Cloudron forum thread calls it the longstanding self-hosted pin board (https://forum.cloudron.io/topic/1065/pinry). Gripes there are about hosting setup, which docs underplay.

===== END SECTION =====

===== SECTION: Miro — alternatives =====
### WBO (whitebophir)
- Official/repo: https://wbo.ophir.dev ; repo https://github.com/lovasoa/whitebophir
- License: AGPL-3.0, per repo (https://github.com/lovasoa/whitebophir)
- Platforms: Node.js web app, self-hosted (Docker)
- Storage model: shared boards by URL, server-side vector board state
- Maintenance: active — ~2.7k stars, commits in October 2026 per search results (repo above). Single primary author plus occasional contributors — moderate single-maintainer risk.
- Coverage of Miro workflows: covers real-time collaborative freehand whiteboarding with text, shapes, boards shared by link, no login. Lacks: Miro's frames/boards-in-boards, presentation mode, plugin ecosystem, integrations, templates.
- Design worth borrowing: minimal real-time collaborative vector board (simple protocol, no accounts) — a clean reference for multi-user whiteboard sync.
- Pricing/self-host: free, self-host.
- Video/community pass: none recorded this lane (budget); gap flagged.
### diagrams.net (drawio)
- Official: https://www.drawio.com ; repo https://github.com/jgraph/drawio (desktop: https://github.com/jgraph/drawio-desktop)
- License: Apache-2.0 for the web editor; the Electron desktop app is GPLv3 (per the two repos)
- Platforms: web, desktop (Electron), plus integrations; fully offline-capable desktop build
- Storage model: XML files (diagrams), local or cloud storage of the user's choosing
- Maintenance: very active, tens of thousands of stars across the two repos (per search results); company-backed (JGraph), low single-maintainer risk.
- Coverage of Miro workflows: covers diagramming, shapes, custom shape libraries, embedded editing, export. Lacks: Miro-style sticky-note brainstorms and video/facilitation features (though sticky-note shapes exist), realtime multi-user editing in the plain OSS builds (collab ships via integrations rather than the standalone app).
- Design worth borrowing: battle-tested XML graph model and shape registry; offline-first desktop packaging.
- Pricing/self-host: free.
- Video/community pass: none recorded this lane (budget); gap flagged.
### Whiteboard (cracker0dks)
- Official/repo: https://github.com/cracker0dks/whiteboard
- License: stated MIT in repo metadata per community research lists — LICENSE file not opened this lane, mark UNVERIFIED (https://github.com/cracker0dks/whiteboard)
- Platforms: Node.js web app, self-hosted; Docker available
- Storage model: server-side boards, saved images; REST API for control
- Maintenance: alive — 833 stars, v1.9.1 released with drag-and-drop shapes, touchscreen support and zoom-to-area per the releases page (https://github.com/cracker0dks/whiteboard/releases); essentially one author — high single-maintainer risk.
- Coverage of Miro workflows: covers lightweight collaborative sketchboard: freehand, shapes, sticky notes, image upload, multi-user in real time. Lacks: Miro's scale (frames, templates, integrations, permissions).
- Design worth borrowing: minimal WebSocket whiteboard protocol; REST API for driving a whiteboard programmatically.
- Pricing/self-host: free, self-host.
- Video/community pass: none recorded this lane (budget); gap flagged.

===== END SECTION =====

===== SECTION: Muse (museapp.com, rebranded Allume) — alternatives =====
Note on the closed app itself: this lane's searches returned that museapp.com has been rebranded to Allume and the product has moved direction; current product status could not be confirmed with a stable page this lane (UNVERIFIED).
### OpenBoard
- Official/repo: https://openboard.sourceforge.io ; repo https://github.com/OpenBoard-org/OpenBoard
- License: GPL-3.0, per repo (https://github.com/OpenBoard-org/OpenBoard)
- Platforms: desktop C++/Qt app for Windows/macOS/Linux (education-oriented interactive whiteboard)
- Storage model: local documents/pages (UBZ documents), import of PDFs, images, presentations
- Maintenance: maintained releases per repo/search results; modest contributor count — moderate single-maintainer risk. Star count not re-verified (UNVERIFIED).
- Coverage of Muse workflows: covers spatial annotation over imported documents on a zoomable canvas, page hierarchy, infinite drawing surface, local-first. Lacks: Muse's nested-canvas-for-thinking UX polish, realtime collaboration, web/mobile.
- Design worth borrowing: annotation-over-document canvas (import PDF/webpage/image and write on top at any zoom) — the same mechanic Muse used for reading-and-thinking surfaces.
- Pricing/self-host: free, local.
- Video/community pass: none recorded this lane (budget); gap flagged.

===== END SECTION =====

===== SECTION: Concepts (concepts.app) — alternatives =====
### Graphite
- Official: https://graphite.rs ; repo https://github.com/GraphiteEditor/graphite
- License: dual MIT/Apache-2.0, per repo (https://github.com/GraphiteEditor/graphite)
- Platforms: browser editor (WebAssembly/Rust) with local file handling; desktop packaging in progress
- Storage model: its own .graphite document format; SVG import/export (raster and vector pipeline)
- Maintenance: very active — steady progress reports, Show HN 2024, node-based editor shipped 2025 per search results (https://github.com/GraphiteEditor/graphite; https://news.ycombinator.com/item?id=41853810; https://news.ycombinator.com/item?id=42747192). Foundation-backed team, lower single-maintainer risk.
- Coverage of Concepts workflows: covers vector drawing on an infinite canvas with a node-based, non-destructive editing graph; still in alpha, so Concepts' pen-first sketching, stylus pressure UI and mobile apps are not matched yet.
- Design worth borrowing: node-based procedural vector pipeline — vector editing as a dataflow graph rather than fixed tools; Rust/WASM editor core.
- Pricing/self-host: free.
- Video/community pass: HN threads (2022 launch https://news.ycombinator.com/item?id=30675530; 2023 https://news.ycombinator.com/item?id=36901401 listed as 36901406 in results; Show HN 2024 https://news.ycombinator.com/item?id=41853810; 2025 preview https://news.ycombinator.com/item?id=43279939). Aggregator reviews record a durable gripe: editor lag that users say was later fixed (https://www.saashub.com/graphite-editor). Official demo videos exist on graphite.rs per search results (not individually watched this lane).
### GodSVG
- Official/repo: https://github.com/MewPurPur/GodSVG (site: https://mewpurpur.github.io/godsvg.github.io/)
- License: MIT, per repo (https://github.com/MewPurPur/GodSVG)
- Platforms: Godot-based desktop app (Windows/macOS/Linux), portable builds
- Storage model: edits SVG directly (code-as-source editing alongside the canvas)
- Maintenance: active per search results but explicitly late-alpha; effectively one author — high single-maintainer risk
- Coverage of Concepts workflows: covers precise vector/SVG object editing with direct manipulation; lacks stylus-first freehand sketching, infinite-canvas document metaphor, mobile.
- Design worth borrowing: tight coupling of live SVG source and canvas edits — a small, clean reference for vector editors.
- Pricing/self-host: free.
- Video/community pass: none recorded this lane (budget); gap flagged.
### SVG-Edit
- Official/repo: https://github.com/SVG-Edit/svgedit (hosted editor https://svgedit.netlify.app/editor/)
- License: GPL-2.0-family per repo/history — older docs state the original code is GPL while the embeddable widget is MIT; exact current LICENSE not opened this lane (UNVERIFIED)
- Platforms: browser; embeddable widget (iframe/JS) in any app
- Storage model: SVG documents in browser or file
- Maintenance: long-dormant project taken over by new maintainers; revived with resumed releases per search results (repo above) — check commit cadence before relying on it
- Coverage of Concepts workflows: covers basic vector shape/pen/path editing in the browser, embeddable anywhere. Lacks: stylus-first UX, pressure input, modern infinite-canvas feel.
- Design worth borrowing: the original embeddable-browser-vector-editor widget — useful as a starting point or reference rather than a finished product.
- Pricing/self-host: free.
- Video/community pass: none recorded this lane (budget); gap flagged.

===== END SECTION =====

===== ROWS =====
| Thinktool | y (AGPL-3.0) | https://github.com/c2d7fa/thinktool | Associative outliner, item-level clones with multiple parents, backlinks; SQLite, Electron/web/server; author moved on, hosted version closing, archive-quality. findings: r12-alt-2 |
| TiddlyWiki | y (BSD-3-Clause) | https://github.com/Jermolene/TiddlyWiki5 | Single-HTML-file wiki; tiddlers with tags/fields = Tana-like object model; ~25 years old, team-maintained, very active. findings: r12-alt-2 |
| Grist | y (Apache-2.0) | https://github.com/gristlabs/grist-core | Spreadsheet-database with typed columns and access rules; SQLite-backed docs; covers Tana's structured-object half, not the outliner; active. findings: r12-alt-2 |
| Foam | y (MIT) | https://github.com/foambubble/foam | Roam-style PKM as a VS Code extension on plain markdown; wikilinks, backlinks, daily notes, graph; active. findings: r12-alt-2 |
| Org-roam | y (GPL-3.0) | https://github.com/org-roam/org-roam | Emacs Roam-like: backlinks + SQLite index over Org files, daily notes; active into 2026. findings: r12-alt-2 |
| Emanote | y (AGPL-3.0) | https://github.com/srid/emanote | Haskell note server over markdown/Org; backlinks, folgezettel; successor to dead Neuron; maintained. findings: r12-alt-2 |
| TreeSheets | y (ZLIB) | https://github.com/aardappel/treesheets | Hierarchical spreadsheet/outliner with zoom-into-cell; native cross-platform; slow but alive; single author. findings: r12-alt-2 |
| Zim | y (GPL-2.0) | https://github.com/zim-desktop-wiki/zim-desktop-wiki | Plain-text desktop wiki, page tree + folding + journal plugin; Linux/GTK; slow maintenance. findings: r12-alt-2 |
| Org-mode | y (GPL-3.0) | https://orgmode.org | Original plain-text outliner: nesting, folding, TODO/agenda, daily notes; part of Emacs, no abandonment risk. findings: r12-alt-2 |
| OutWiker | y (GPL-3.0) | https://github.com/Jenyay/outwiker | Page-tree notes with page-type plugins and attachments; Windows/Linux Qt; active, single author. findings: r12-alt-2 |
| nb | y (AGPL-3.0-or-later) | https://github.com/xwmx/nb | Single-script CLI + local web notes; git versioning, encryption, bookmarks; 8.4k stars, active. findings: r12-alt-2 |
| zk | y (GPL-3.0) | https://github.com/zk-org/zk | Go CLI zettelkasten: backlinks, tags, templates, LSP for any editor; active, small team. findings: r12-alt-2 |
| Unigraph | y (MIT) | https://github.com/unigraph-dev/unigraph-dev | Local-first typed-object knowledge graph on Dgraph; closest pullable Capacities/Tana object model; author-run, stalled-risk. findings: r12-alt-2 |
| scrumblr | y (GPL-3.0) | https://github.com/alias1/scrumblr | Minimal shared spatial card board by URL; dormant archive-quality source. findings: r12-alt-2 |
| Kinopio client (open-sourced) | y (non-commercial license) | https://github.com/kinopio-club/kinopio-client | Kinopio's own client made public June 2024, server closed; non-commercial license blocks commercial reuse; design reference only. findings: r12-alt-2 |
| spacedeck-open | y (AGPL-3.0) | https://github.com/spacedeck/spacedeck-open | Cards/media/text/shapes on spatial boards; frozen since its 2018 open-source release; archive-quality. findings: r12-alt-2 |
| Pinry | y (BSD) | https://github.com/pinry/pinry | Self-hosted tiling image/link boards with tags and sharing; Milanote moodboard analog without freeform canvas; alive, low-energy. findings: r12-alt-2 |
| WBO (whitebophir) | y (AGPL-3.0) | https://github.com/lovasoa/whitebophir | Realtime collaborative web whiteboard, no accounts; active Oct 2026, single primary author. findings: r12-alt-2 |
| diagrams.net (drawio) | y (Apache-2.0 web; GPLv3 desktop) | https://github.com/jgraph/drawio | Full diagramming editor, offline desktop, XML files; company-backed, very active; no standalone realtime collab. findings: r12-alt-2 |
| Whiteboard (cracker0dks) | y (MIT, UNVERIFIED license file) | https://github.com/cracker0dks/whiteboard | Lightweight collaborative sketchboard with REST API; 833 stars, v1.9.1 in 2024; single author. findings: r12-alt-2 |
| OpenBoard | y (GPL-3.0) | https://github.com/OpenBoard-org/OpenBoard | Desktop interactive whiteboard: annotation over imported PDFs/images on zoomable canvas pages; Muse-like document-annotation surface; maintained. findings: r12-alt-2 |
| Graphite | y (MIT/Apache-2.0 dual) | https://github.com/GraphiteEditor/graphite | Rust/WASM node-based non-destructive vector editor on infinite canvas; very active; alpha vs Concepts' pen UX. findings: r12-alt-2 |
| GodSVG | y (MIT) | https://github.com/MewPurPur/GodSVG | Godot-based direct-manipulation SVG editor with live source; late alpha, single maintainer. findings: r12-alt-2 |
| SVG-Edit | y (GPL-2.0-family, UNVERIFIED variant) | https://github.com/SVG-Edit/svgedit | Embeddable browser vector editor; long dormant, now under new maintainers with resumed releases; verify cadence. findings: r12-alt-2 |

LANE 2 COMPLETE — 12 closed apps processed, 24 new alternatives documented (23 general alternatives + the Kinopio client-source note counted as its own row)
