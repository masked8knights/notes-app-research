# r6 — Obsidian Plugin Cluster (Lane: r6-obsidian-plugins)

Research date: 2026-10-26. Sources: web search, official Obsidian community plugin registry
(raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugins.json — 9,518 plugins
at retrieval), GitHub repos via raw.githubusercontent.com, obsidianstats.com, Reddit, Obsidian forums.

Scope: every Obsidian PLUGIN link in `links-inventory.txt`, plus the "usual suspects" the project
owner flagged (Dataview, Templater, Omnisearch, Kanban, Daily Notes/core plugins, Sync alternatives).
Excalidraw appears in the inventory itself. Per directive, NOTHING in this file covers gettbb.app /
get-bb.app or any `bb-*` entry; those inventory links were excluded from this lane's scope.

Registry cross-check (official community-plugins.json, retrieved 2026-10-26) confirms these IDs and
authors, which anchor every section below:

- `obsidian-excalidraw-plugin` — zsviczian
- `dataview` — blacksmithgu
- `templater-obsidian` — silentvoid13
- `omnisearch` — Simon Cambier
- `obsidian-kanban` — Obsidian Community Archive
- `obsidian-list-callouts` — mgmeyers
- `obsidian-meta-bind-plugin` — Moritz Jung (mProjectsCode)
- `sheets` — niconekoru, name "Sheets Extended"
- `spreadsheets` — divamgupta (adjacent, context for Sheets)
- `numerals` — ryanc
- `badges` — gapmiss
- `inkedmark` — liqpil, repo pcrausaz/obsidian-inkedmark ("This plugin has not been manually reviewed
  by Obsidian staff" — registry description)
- `notebook-navigator` — Johan Sanneblad
- `nostr-writer` — jamesmagoo
- `obsidian-livesync` — vrtmrz
- `remotely-save` — remotely-save

Licenses were verified by reading LICENSE/LICENSE.txt/LICENSE.md/COPYING at each repo via
raw.githubusercontent.com on 2026-10-26; conflicts are stated explicitly where found.

---

## 1. Excalidraw plugin (`obsidian-excalidraw-plugin`)

**What it does.** A full-featured whiteboard/sketching plugin that embeds Excalidraw drawing canvases
into Obsidian: draw in markdown-linked `.excalidraw` files, embed drawings in notes, turn drawings into
concept maps with links to notes, import/export, image and PDF import for annotation, and a scripting
API ("Excalidraw Automate") for other plugins. (https://github.com/zsviczian/obsidian-excalidraw-plugin;
https://community.obsidian.md/plugins/obsidian-excalidraw-plugin)

**Author:** Zsolt Viczián (zsviczian), a single very active maintainer. **Install base:** listed among
Obsidian's most-downloaded plugins of all time, top-5 cluster alongside Templater, Dataview, Tasks and
Git (https://www.obsidianstats.com/most-downloaded). Exact all-time count unverified this pass
(obsidianstats.com renders its numbers via JavaScript; the page text I could pull did not contain the
figure). The repo shows ~7.2k stars (https://community.obsidian.md/plugins/obsidian-excalidraw-plugin,
user-facing page text). Marked "unverified number" honestly rather than guessing.

**Status.** Very actively maintained; heavy release cadence (releases page is dense with 2.x point
releases) (https://github.com/zsviczian/obsidian-excalidraw-plugin/releases). In May 2026 the developer
opened a debate about monetizing an add-on ("Excalidraw Plugin Developer: The Future of Obsidian
Plugins" — https://www.reddit.com/r/ObsidianMD/comments/1tg4e3c/excalidraw_plugin_developer_the_future_of/),
which is worth tracking: a maintainer-visible signal that even big community plugins strain to fund
themselves. Community reaction pushed back on any subscription ("we already have too many
subscriptions" — same thread).

**Features (full list, from repo README and plugin page).**
- Freehand drawing canvas embedded in markdown; every drawing is an `.excalidraw` (JSON) file
  (https://github.com/zsviczian/obsidian-excalidraw-plugin)
- Markdown-flavored drawing files that stay plain-text and sync-able (same source)
- Concept-map mode: draw arrows between "frame" nodes that embed live Obsidian notes; clicking
  navigates the vault (same source)
- Embed notes, images (local and public URLs), PDFs, websites (Iframelely resolves page titles when
  dragging links in) (same source)
- Flip/PDF/annotate workflow, image import and export, PNG/SVG export (same source)
- "Excalidraw Automate" scripting API + companion scripts; separate "Excalidraw Extras" plugin was
  split out in 2026 to house heavy dependencies and high-privilege operations so the core plugin stays
  lightweight and works with Obsidian Sync Basic and community security policies
  (https://www.obsidianstats.com/plugins/excalidraw-extras)
- AI integrations and optional Taskbone OCR, both opt-in; fonts for those are downloaded from GitHub
  on first use to keep startup fast (https://github.com/zsviczian/obsidian-excalidraw-plugin)
- Theme integration (colors picked up from Obsidian themes), dark/light mode drawing themes (same source)
- Scripts library, templated shapes, stickies, markdown tables in drawings, mindmapping shortcuts (same source; full
  wiki: https://github.com/zsviczian/obsidian-excalidraw-plugin/wiki — "Excalidraw Automate How To" page)

**What users LIKE.** Users describe it as far better than any other drawing plugin they've found, and
many say Excalidraw is the one thing that keeps them on Obsidian ("I use Excalidraw - it is important to
me to use with Obsidian, and works far better than any other drawing plugins I've found" —
https://www.reddit.com/r/ObsidianMD/comments/1tg4e3c/). The concept-map/frame-embed workflow (drawings
that link into the vault) is the repeatedly-praised differentiator vs plain Excalidraw.

**What users WANT CHANGED (GitHub issues, load-bearing for us).**
- Performance decay as boards grow: typing lag with the plugin enabled even in normal notes
  (https://github.com/zsviczian/obsidian-excalidraw-plugin/issues/1456); input lag on large boards on
  tablets (https://www.reddit.com/r/ObsidianMD/comments/1hfkjhf/how_to_fix_input_lag_in_excalidraw_on_obsidian/);
  extreme slowness affecting Obsidian itself after opening older drawings
  (https://github.com/zsviczian/obsidian-excalidraw-plugin/issues/1738); general lag reports
  (https://www.reddit.com/r/ObsidianMD/comments/t0c9s5/obsidian_lag_with_excalidraw/)
- Regression pain between versions: 2.15.1 broke embedded notes and caused note corruption for some
  users, fixed by rolling back to 2.15.0
  (https://www.reddit.com/r/Excalidraw/comments/1n48mcq/plugin_issues_with_obsidian_excalidraw_2151/) —
  fast-moving single-maintainer plugin = occasional breakage, users keep old versions
- Startup-time anxiety is acknowledged by the author himself (the Extras split exists specifically to
  keep the core fast) (https://www.obsidianstats.com/plugins/excalidraw-extras)
- Monetization tension (see above) — users do not want subscriptions

**Open-source status.** License: GNU Affero GPL v3 — verified by reading
https://raw.githubusercontent.com/zsviczian/obsidian-excalidraw-plugin/master/LICENSE. Repo:
https://github.com/zsviczian/obsidian-excalidraw-plugin. **AGPL = CONCEPTS ONLY** for pull-from.

**Pull-from assessment.** Code: not pullable (AGPL-3.0). Concepts with strong demand evidence:
(1) drawings as plain-text JSON files that live in the vault and sync/diff like notes;
(2) note-embedding canvases (arrows connecting live note embeds) — the killer feature users cite;
(3) annotation/import of PDFs and images; (4) a scripting/automation surface for drawing files;
(5) the architecture lesson: keep heavy dependencies out of the core file-viewer so startup stays fast.
A Rust/Tauri app should treat "infinite canvas that embeds live notes" as a first-class feature concept.

---

## 2. Dataview (`dataview`) + successor Datacore + native competitor Bases

**What it does.** Query engine over vault metadata: DQL query language plus JS API, renders tables,
lists, task lists and calendar views from frontmatter/inline fields; the de-facto database layer of
Obsidian (https://github.com/blacksmithgu/obsidian-dataview).

**Author:** Michael Brenan (blacksmithgu). **Install base:** among the most-downloaded plugins of all
time, in the top-5 cluster (https://www.obsidianstats.com/most-downloaded). Exact count unverified this
pass (JS-rendered stats page). GitHub ~6.6k stars (unverified this pass).

**Status.** Maintenance is effectively stalled: the author is working on a successor, **Datacore**
("Work-in-progress successor to Dataview with a focus on UX and speed"
https://github.com/blacksmithgu/datacore), and the community asks for Dataview to at least mention it
(https://github.com/blacksmithgu/obsidian-dataview/issues/1825). Ecosystem plugins are already
planning the switch (https://github.com/ivan-lednev/obsidian-day-planner/issues/693). Meanwhile
**Obsidian Bases** (a native core feature, file-as-database views) shipped and is eating this space
(https://obsidian.rocks/dataview-vs-datacore-vs-obsidian-bases/). Timeline context: the vault-database
concept is central to every notes-app roadmap (https://github.com/blacksmithgu/obsidian-dataview).

**Features (full list, from repo/docs).**
- DQL query language: TABLE, LIST, TASK, CALENDAR views; WHERE/SORT/GROUP BY/FLATTEN; queries
  persist as live blocks inside notes that re-execute on open
  (https://github.com/blacksmithgu/obsidian-dataview)
- DataviewJS: full JS API for programmatic queries and rendering (same source)
- Metadata model: frontmatter YAML + inline fields (`key:: value`), computed via expressions; page
  objects with automatic typing (same source; docs https://blacksmithgu.github.io/obsidian-dataview/)
- Embedded task views with query filtering across the vault (same source)
- Calendar view by date field (same source)
- Inline field rendering in Live Preview and Reading mode (same source)
- Incremental caching of vault metadata for query speed (same source; see complaints below)

**What users LIKE.** It is the single most load-bearing power-user plugin: "turns Obsidian into a
database"; the reason many workflows (project trackers, reading lists, recipe indexes, task boards)
live inside markdown files at all. Community showcase threads document huge query-driven workflows
(https://forum.obsidian.md/t/datacore-plugin-showcase-thread/91545).

**What users WANT CHANGED (GitHub issues, load-bearing for us).**
- Table loading speed degrades with vault size; queries can take seconds on big vaults
  (https://github.com/blacksmithgu/obsidian-dataview/issues/1226)
- Maintainer responsiveness: long issue backlogs, successor not production-ready, users feel stranded
  between an aging plugin and an unfinished Datacore
  (https://github.com/blacksmithgu/obsidian-dataview/issues/1825; https://github.com/blacksmithgu/datacore/issues)
- Conceptual complaint set: DQL is a second language to learn; error messages are cryptic; JS queries
  are powerful but fragile (community-wide recurring theme; e.g.
  https://forum.obsidian.md/t/datacore-plugin-showcase-thread/91545)

**Open-source status.** License: MIT (verified from
https://raw.githubusercontent.com/blacksmithgu/obsidian-dataview/master/LICENSE.txt — "MIT License,
Copyright (c) 2021 Michael Brenan"). Datacore is also MIT (verified from
https://raw.githubusercontent.com/blacksmithgu/datacore/master/LICENSE.txt — "MIT License, Copyright
(c) 2025 Michael Brenan"). Repo: https://github.com/blacksmithgu/obsidian-dataview.

**Pull-from assessment.** **Code IS pullable (MIT)** — but it is TypeScript targeted at Obsidian's
API; realistic pull is the query-planning/caching ideas and the expression evaluator design. Concepts
with demand evidence: (1) queries that persist in the note as live blocks; (2) frontmatter as a typed,
queryable database over plain markdown; (3) task rollups across files; (4) the performance lesson:
incremental indexing is a requirement, not an optimization, and the #1 complaint is speed. A native
Rust implementation of a DQL-like query layer over a local index is one of the strongest demand signals
in this whole research cluster.

---

## 3. Templater (`templater-obsidian`)

**What it does.** A scripting template engine: templates with variables, functions, user-defined
JavaScript, cursor placement, folder/file templates, startup templates, and system-command execution
(https://www.obsidianstats.com/plugins/templater-obsidian).

**Author:** SilentVoid13; per the project page, day-to-day maintenance has moved to Zachatoo (community
maintainer) — UNVERIFIED this pass (https://github.com/SilentVoid13/Templater). **Install base:**
6,017,669 all-time downloads, 5,369 stars, five-star average reviews
(https://www.obsidianstats.com/plugins/templater-obsidian). Note an older figure of 3.7M circulates on
the Obsidian Hub page (https://publish.obsidian.md/hub/02+-+Community+Explainers/Plugins/Templater) —
the 6.0M obsidianstats figure is the current one.

**Status.** Actively maintained; most recent data point on the stats page dated September 19, 2026
(https://www.obsidianstats.com/plugins/templater-obsidian). Releases page active
(https://github.com/SilentVoid13/Templater/releases).

**Features (full list, from README/docs).**
- Template variables and dynamic content: dates, titles, frontmatter access
  (https://github.com/SilentVoid13/Templater)
- `<% tp.* >` internal function family (file, date, frontmatter, system, web, cursor) (same source)
- User-defined JavaScript functions (user scripts) callable inside templates (same source)
- Interactive prompts and suggesters inside templates (same source)
- Folder templates (auto-apply on new file creation), file templates, startup templates
  (https://docs.templater.obsidiangranary.com/overview/templater-syntax — Templater docs, mirrored at
  https://github.com/SilentVoid13/Templater#documentation)
- Cursor navigation and insertion point control (same source)
- System command execution from templates (https://www.obsidianstats.com/plugins/templater-obsidian)

**What users LIKE.** "Simple and powerful" is the recurring five-star summary; the scripting ceiling
(emails of workflow automation built in templates) keeps power users loyal
(https://www.obsidianstats.com/plugins/templater-obsidian). Universally referenced in setup guides —
it is one of the plugins a new Obsidian user installs first.

**What users WANT CHANGED.** Learning curve (the `tp` syntax is intimidating to non-programmers);
error surfacing in templates is poor; docs scattered across the site and repo. These recur in forum
threads and issue titles — UNVERIFIED as specific issue links this pass (search budget exhausted);
the general friction is documented by the docs site existing as a separate fan-maintained mirror
(https://docs.templater.obsidiangranary.com/).

**Open-source status.** **License conflict, stated honestly:** package.json declares
`"license": "AGPL-3.0-only"` (verified from
https://raw.githubusercontent.com/SilentVoid13/Templater/master/package.json), while GitHub's license
detection shows "GPLv3 license" (https://github.com/SilentVoid13/Templater), and no LICENSE/COPYING
file exists at the repo root (404 from raw.githubusercontent.com for LICENSE, LICENSE.md, COPYING on
master). Treat as copyleft (GPL/AGPL family) — **concepts only** until the project verifies which
license actually applies.

**Pull-from assessment.** Code: not pullable as far as verifiable (AGPL-3.0 declared in package.json;
GPL-3.0 shown by GitHub — either way copyleft). Concepts with demand evidence: (1) templates that run
code (user scripts) rather than only fill variables; (2) folder/file/startup template triggers
(automation on lifecycle events); (3) interactive prompts/suggesters inside note creation; (4) cursor
placement as part of template semantics. All four are direct feature specs for a Rust notes app.

---

## 4. Omnisearch (`omnisearch`)

**What it does.** A search engine for the vault that "just works": fuzzy, weighted full-text search
with a modal UI, respecting frontmatter, supporting Chinese/Cyrillic/other scripts via extra
"text-extractor" companion plugins for PDFs/images (https://github.com/scambier/obsidian-omnisearch).

**Author:** Simon Cambier (scambier). **Install base:** listed among Obsidian's most-downloaded
plugins (top-25 cluster) (https://www.obsidianstats.com/most-downloaded); figure ~2M cited on the
community page — UNVERIFIED precise count this pass. **Status:** maintained; has a companion
"Omnisearch Companion" plugin for extra features
(https://github.com/scambier/obsidian-omnisearch — Discussion #353).

**Features (full list, from README).**
- Vault-wide fuzzy search with weighted results (title matches, headings, recency-weighted)
  (https://raw.githubusercontent.com/scambier/obsidian-omnisearch/master/README.md)
- Indexing of PDFs, images (OCR), and office files via the Omnisearch Text Extractor companion
  (same source)
- CJK and multilingual support (same source)
- Vault-history weighting: recently-visited notes rank higher (same source)
- Query cache; opens results in default or custom search actions (same source)
- Vim-style shortcuts, obsidian-embedded search page, Obsidian URI deep links into results (same source)

**What users LIKE.** Core search is the #1 most-complained-about limitation of stock Obsidian
(match-only, no fuzzy ranking), and Omnisearch is the community's standard fix; users describe it as
the search Obsidian should ship. Recurring praise: finds notes by partial words, respects frontmatter
exclusions. (Community page and README; https://community.obsidian.md/plugins/omnisearch)

**What users WANT CHANGED.** Index rebuild time on very large vaults and memory usage are the recurring
complaints; some want richer query syntax (boolean operators). UNVERIFIED as specific issue links this
pass; performance theme is consistent across community threads.

**Open-source status.** License: GPL-3.0 (verified from
https://raw.githubusercontent.com/scambier/obsidian-omnisearch/master/LICENSE). Repo:
https://github.com/scambier/obsidian-omnisearch. **GPL = CONCEPTS ONLY.**

**Pull-from assessment.** Code: not pullable (GPL-3.0). Concepts with demand evidence: (1) fuzzy
weighted full-text ranking as a first-class core feature (the stock app's weakness is the plugin's
raison d'être); (2) OCR/PDF text extraction feeding the same index (text-extractor pattern);
(3) recency weighting from visit history. For a Rust/Tauri app: ship search that beats stock Obsidian
on day one, e.g. via Tantivy-style indexing; this plugin is the demand evidence.

---

## 5. Kanban (`obsidian-kanban`)

**What it does.** Markdown-backed Kanban boards: a board view over a plain markdown file, one list per
heading, one card per list item; drag-and-drop, date metadata, links inside cards
(https://github.com/mgmeyers/obsidian-kanban).

**Author:** mgmeyers (original); now under the **Obsidian Community Archive** as it searches for new
maintainers (https://github.com/obsidian-community/obsidian-kanban; the community plugin page itself
bears "The Kanban plugin is looking for new maintainers" —
https://community.obsidian.md/plugins/obsidian-kanban).

**Install base.** 2.7M downloads reported on the community plugin page
(https://community.obsidian.md/plugins/obsidian-kanban); kepano's Aug 2024 blog put it at 1.9M
(https://kepano.dev/obsidian-plugin-report-2024/ — figure as cited there). Among the most-downloaded
plugins all-time (https://www.obsidianstats.com/most-downloaded).

**Status.** Maintenance paused: "Is this project still maintained?" — latest release over a year old,
bug reports from incompatibility with newer Obsidian versions piling up
(https://github.com/mgmeyers/obsidian-kanban/issues/1157). Community Archive holds it for safekeeping
and recruiting (https://github.com/obsidian-community/obsidian-kanban).

**Features (full list, from README).**
- Kanban boards rendered from markdown lists; two-way sync (edit in board or in text) (README, same URL as above)
- Drag-and-drop cards between lists and within lists (same source)
- Card metadata: dates with hover previews, checkbox marking, links and embeds inside cards (same source)
- Board settings per-file (list width, column colors) stored in file frontmatter (same source)
- Plugins-inside-boards: integrates with Tasks-style metadata (same source)
- Markdown-only storage: board is a normal note, sync-safe (same source)

**What users LIKE.** The markdown-underneath design: boards are plain files, so they sync everywhere
and diff cleanly; users keep boards inside their normal vault backups. Load-bearing for the project:
"markdown-backed kanban" is a proven, wanted format. (MAINTAINERS.md records the user-base scale
argument: https://github.com/obsidian-community/obsidian-kanban/blob/main/MAINTAINERS.md)

**What users WANT CHANGED (GitHub issues, load-bearing for us).**
- Card creation breaking entirely after updates: boards render but new cards throw errors
  (https://github.com/mgmeyers/obsidian-kanban/issues/967)
- General "still maintained?" anxiety; incompatibilities with newer Obsidian builds
  (https://github.com/mgmeyers/obsidian-kanban/issues/1157)
- The maintainer's own note in MAINTAINERS.md about community-vision tension — the plugin is big
  enough that every design decision becomes political (same source)

**Open-source status.** License: GPL-3.0 (verified from
https://raw.githubusercontent.com/mgmeyers/obsidian-kanban/master/LICENSE.md and the community-archive
copy at https://raw.githubusercontent.com/community-archive/obsidian-kanban/main/LICENSE.md). Repo:
https://github.com/mgmeyers/obsidian-kanban. **GPL = CONCEPTS ONLY.**

**Pull-from assessment.** Code: not pullable (GPL-3.0). Concepts with demand evidence: (1) Kanban as a
VIEW over plain markdown, never a special file format; (2) per-board config in frontmatter;
(3) two-way text/board editing. Also a cautionary tale: a beloved plugin orphaned by burnout — an
argument for making such views core features rather than community add-ons.

---

## 6. List Callouts (`obsidian-list-callouts`)

**What it does.** Adds colored callout "badges" to list items: a custom string in the list item text
(e.g. `> [!INFO]`) becomes an inline icon + colored bar per item, with custom icons and colors
(https://github.com/mgmeyers/obsidian-list-callouts).

**Author:** mgmeyers. **Install base:** 141k downloads (community page —
https://community.obsidian.md/plugins/obsidian-list-callouts). **Status:** UNMAINTAINED — the plugin
page itself says it is not maintained (2 years no updates) and lists a fork
(`list-callouts-improved`) that continues it
(https://community.obsidian.md/plugins/obsidian-list-callouts; fork search: "obsidian list callouts
fork" — the improved fork name appears in the registry's related-plugin listings on the same page).

**Features (full list, from repo README).**
- Per-list-item callouts with icon + color bar (README, same URL as above)
- Custom callout types defined per-vault (icon, color, title) (same source)
- Works in editing and reading modes (same source)
- Pure CSS-decorative transform — text stays standard markdown (same source)

**What users LIKE.** Cheap visual grammar for lists (status labels, moods, priorities) without
inventing a new format. (community page user reviews and forum mentions —
https://community.obsidian.md/plugins/obsidian-list-callouts)

**What users WANT CHANGED.** Maintenance abandonment is the complaint: the page recommends the fork;
users grumble about no updates under recent Obsidian versions (same page).

**Open-source status.** License: GPL-3.0 (verified from
https://raw.githubusercontent.com/mgmeyers/obsidian-list-callouts/master/LICENSE.md). Repo:
https://github.com/mgmeyers/obsidian-list-callouts. **GPL = CONCEPTS ONLY.**

**Pull-from assessment.** Code: not pullable (GPL-3.0). Concept with demand evidence: inline,
per-item visual callouts in lists, defined by a tiny convention rather than a format. Small but a
repeated request in notes-app UX. A similar effect is achievable with CSS/attribute markers natively.

---

## 7. Meta Bind (`obsidian-meta-bind-plugin`)

**What it does.** Turns notes into interactive UIs: embeds input fields (toggles, dropdowns, sliders,
text/number/date/progress), metadata displays, and buttons bound to frontmatter properties, updating
live (https://www.obsidianstats.com/plugins/obsidian-meta-bind-plugin).

**Author:** Moritz Jung (mProjectsCode). **Install base:** significant — listed in the top-25
most-downloaded cluster (https://www.obsidianstats.com/most-downloaded); precise count unverified this
pass (JS-rendered page). **Status:** actively maintained (mProjectsCode is one of the most consistent
community maintainers; stats page current — https://www.obsidianstats.com/plugins/obsidian-meta-bind-plugin).

**Features (full list, from docs/README).**
- Input fields: toggle, dropdown, select, slider, progress bar, text, number, date, time (docs at
  https://mprojectscode.github.io/obsidian-meta-bind-plugin-docs/)
- Bindings to frontmatter properties with live two-way sync (same source)
- Buttons with configurable actions (commands, templater runs, file open) (same source)
- Math.js expressions computed inside notes (same source)
- Frontmatter "note config" blocks for field styling defaults (same source)
- Toggle styles, input validation, JSDoc-style error surfacing inline (same source)

**What users LIKE.** The "Obsidian as app-builder" use case: habit trackers, dashboards, RPG character
sheets, chore charts — all without leaving markdown. Community dashboards lean on it heavily
(https://www.obsidianstats.com/plugins/obsidian-meta-bind-plugin).

**What users WANT CHANGED.** Binding edge cases (select-metadata and file-specific field configs have
long open issue threads) and mobile parity. UNVERIFIED as specific issue links this pass; the docs'
own issue tracker at https://github.com/mProjectsCode/obsidian-meta-bind-plugin/issues is the canon.

**Open-source status.** License: GPL-3.0 (verified from
https://raw.githubusercontent.com/mProjectsCode/obsidian-meta-bind-plugin/master/LICENSE.txt). Repo:
https://github.com/mProjectsCode/obsidian-meta-bind-plugin. **GPL = CONCEPTS ONLY.**

**Pull-from assessment.** Code: not pullable (GPL-3.0). Concepts with demand evidence: (1) notes as
interactive forms bound to frontmatter — strong and growing demand; (2) declarative inline syntax for
inputs; (3) button actions triggering app commands. For a local-first Rust app this is a natural
"widgets in markdown" feature family, and the demand evidence is direct.

---

## 8. Sheets Extended (`sheets`, repo `niconekoru/obsidan-advanced-table-xt`)

**What it does.** Advanced table features on markdown tables: vertical (rotated) headers, merged
cells (rowspan/colspan via `| |` conventions), and custom CSS classes per table, staying compatible
with the Advanced Tables plugin's syntax (registry description, official community-plugins.json:
id `sheets`, name "Sheets Extended", description "Vertical headers, merged cells, and custom CSS
tables with Advanced Tables compatability" — https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugins.json).

**Author:** niconekoru (NicoNekoru). **Install base:** small — UNVERIFIED precise count this pass.
**Status:** maintained as of the registry data pull (2026-10-26); repo active on master
(https://github.com/niconekoru/obsidan-advanced-table-xt).

**Features (full list, from repo README).**
- Vertical header rows (rotated text) in markdown tables (README, same URL as above)
- Merged cells via conventions on the cell text (same source)
- Per-table custom CSS class assignment (same source)
- Compatibility mode with Advanced Tables editor commands (same source)
- Reading-mode and Live-Preview rendering of extended tables (same source)

**What users LIKE.** Markdown tables that stop being grid-locked: sub-column grouping via merged
headers, dense property sheets. Niche but passionate. (community page —
https://community.obsidian.md/plugins/sheets)

**What users WANT CHANGED.** Fragility of the merge syntax when other plugins rewrite tables; limited
editor support for merged cells in Live Preview. UNVERIFIED as issue links this pass.

**Open-source status.** License: **Apache-2.0** (verified from
https://raw.githubusercontent.com/niconekoru/obsidan-advanced-table-xt/master/LICENSE). Repo:
https://github.com/niconekoru/obsidan-advanced-table-xt. **APACHE = CODE PULLABLE.**

**Pull-from assessment.** Code: pullable with attribution (Apache-2.0), though the implementation is
TypeScript/CodeMirror — realistic pull is the syntax conventions (merge markers, vertical-header
marker), which are the valuable part, plus test cases. Concepts with demand evidence: markdown tables
need to grow merged cells and vertical headers to cover real property sheets; users prefer extending
markdown syntax over switching to a spreadsheet file format (see also the wider spreadsheet-plugin
ecosystem: Sheet Plus — full Excel-like grids on Univer
(https://community.obsidian.md/plugins/sheet-plus); Spreadsheets by Divam Gupta with formulas in
markdown tables (https://community.obsidian.md/plugins/spreadsheets); Markdown Spreadsheets writing
strict GFM with CSV/Excel export (https://community.obsidian.md/plugins/markdown-spreadsheets) —
the demand spans "keep it markdown" to "give me Excel", and the middle lane (formulas in markdown
tables) is the most cited by users wanting both worlds).

---

## 9. Numerals (`numerals`)

**What it does.** Renders enhanced markdown lists as live math: each list line becomes a calculation
step with results shown inline; variables, unit conversions, LaTeX output, comments
(https://github.com/gtg922r/obsidian-numerals).

**Author:** ryanc (Ryan C. Gordon is NOT this author — handle is `ryanc` per the official registry;
repo owner gtg922r — verified from community-plugins.json: id `numerals`, author `ryanc`; repo URL
https://github.com/gtg922r/obsidian-numerals).

**Install base.** UNVERIFIED precise count this pass (not in the top-25 list I pulled). **Status:**
actively maintained; releases in 2025-2026 include a license change to MIT
(https://github.com/gtg922r/obsidian-numerals/releases).

**Features (full list, from repo README).**
- Live evaluation of markdown list lines as math expressions (README, same URL as above)
- Variables (`x = 5` then reuse), function evaluation (same source)
- Unit conversions and currency-ish arithmetic via a units engine (same source)
- LaTeX rendering of results (same source)
- Comments and result annotations; sum/skip conventions (same source)
- Support for evaluation via math.js under the hood (same source)

**What users LIKE.** "Evaluated scratchpad" feel: taking notes that are half math without leaving
markdown. Cited as the calculator everyone keeps open next to real work. (repo README community
praise section and Reddit mentions — https://www.reddit.com/r/ObsidianMD/ search "numerals" —
UNVERIFIED this pass, search budget exhausted)

**What users WANT CHANGED.** Variable scoping across blocks; performance on long sheets. UNVERIFIED
as issue links this pass.

**Open-source status.** License: MIT (verified from
https://raw.githubusercontent.com/gtg922r/obsidian-numerals/master/LICENSE — "MIT License, Copyright
(c) 2022-2025 The Numerals contributors"). Repo: https://github.com/gtg922r/obsidian-numerals.
**MIT = CODE PULLABLE.**

**Pull-from assessment.** Code: pullable (MIT), TypeScript. The evaluation engine (math.js wrapper +
unit handling) is the reusable concept; in Rust the equivalent would be a small expression evaluator
with units (e.g. a KDL of `furs`-style crates) — the plugin is the demand evidence, not the codebase
to port. Concepts: inline evaluated scratchpads inside normal notes, unit-aware math in lists.

---

## 10. Badges (`badges`)

**What it does.** Inline badges/callouts in notes: small pill-shaped labels with icon + text rendered
from a simple syntax, useful for status markers and metadata chips (registry description "Add inline
badges/callouts to notes" — https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugins.json;
plugin page https://community.obsidian.md/plugins/badges).

**Author:** gapmiss. **Install base:** UNVERIFIED precise count this pass (small plugin). **Status:**
present in the registry (2026-10-26 pull); repo
https://github.com/gapmiss/badges active on master.

**Features (full list, from repo README).**
- Badge syntax for inline icons + labels (README, https://github.com/gapmiss/badges)
- Predefined badge styles; custom colors (same source)
- Works in reading mode and live preview (same source)

**What users LIKE.** Lightweight status decoration that survives sync (it is only text). (plugin page
community reviews — https://community.obsidian.md/plugins/badges)

**What users WANT CHANGED.** UNVERIFIED this pass; the plugin is small and stable, most issues relate
to icon set coverage (https://github.com/gapmiss/badges/issues).

**Open-source status.** License: MIT (verified from
https://raw.githubusercontent.com/gapmiss/badges/master/LICENSE). **MIT = CODE PULLABLE.**

**Pull-from assessment.** Code: pullable (MIT) but trivial scope; the concept (inline status chips in
markdown) overlaps with List Callouts and is a CSS-level feature for us. Demand evidence: mild, mostly
overlapping with #6.

---

## 11. InkedMark (`inkedmark`, repo `pcrausaz/obsidian-inkedmark`)

**What it does.** Handwriting inside markdown notes: pressure-aware ink stored as a first-class block
in `*.ink.md` files (which remain plain markdown), with a searchable typed "text layer" (transcription,
key points, wikilinks, tags) that core Obsidian search, graph, backlinks and Quick Switcher index
(README — https://raw.githubusercontent.com/pcrausaz/obsidian-inkedmark/master/README.md).

**Author:** liqpil (registry author) / repo pcrausaz. **Install base:** new plugin — UNVERIFIED count;
**registry status line is load-bearing**: "This plugin has not been manually reviewed by Obsidian
staff" (community-plugins.json) — i.e. auto-approved/not yet fully reviewed, so treat with care.
**Status:** new and actively developed (demo at https://inkedmark.com).

**Features (full list, from README).**
- Pen-first canvas view over `*.ink.md` files that stay plain markdown (README)
- Searchable text layer: recognition produces transcription, key points, `[[links]]`, `#tags` indexed
  by core search/graph/backlinks/Quick Switcher (same source)
- Inline sketches: embed handwriting notes via `![[Sketch.ink.md]]`, or draw into a ```inkedmark`
  block inside any note (same source)
- Apple Pencil support: pressure-variable ink (perfect-freehand), coalesced event capture, palm
  rejection, wet/dry canvas split for low latency (same source)
- Works on desktop, iPad, and mobile (same source)

**What users LIKE.** The pitch itself — handwriting that stays markdown and becomes searchable — is
the liked part; demo thread reaction on r/ObsidianMD (UNVERIFIED links this pass).

**What users WANT CHANGED.** Too new for a mature complaint set; UNVERIFIED.

**Open-source status.** License: MIT (verified from
https://raw.githubusercontent.com/pcrausaz/obsidian-inkedmark/master/LICENSE). Repo:
https://github.com/pcrausaz/obsidian-inkedmark. **MIT = CODE PULLABLE.**

**Pull-from assessment.** Code: pullable (MIT). Demand evidence is important beyond the plugin's size:
handwriting-in-notes with OCR text layers is exactly the Apple-notes-escape use case, and the plugin's
architecture (ink as markdown, text layer indexed by the same engine as typed notes) is a directly
transferable design for a Tauri app with pen input. The perfect-freehand choice (MIT) is also the
de-facto standard ink-stroke renderer.

---

## 12. Notebook Navigator (`notebook-navigator`)

**What it does.** A replacement file browser: folders, tags, properties and shortcuts in one pane,
with note previews, full keyboard navigation, dual-pane layout, mobile optimization; advertised as
working with 100,000+ notes (https://www.obsidianstats.com/plugins/notebook-navigator).

**Author:** Johan Sanneblad. **Install base:** large (top-25 cluster per
https://www.obsidianstats.com/most-downloaded); precise count unverified this pass. **Status:** very
actively maintained with an unusually disciplined engineering process (TypeScript, ESLint, Prettier,
Vitest, zero-warning build gate, CodeQL scanning, documented network-disclosure section)
(https://www.obsidianstats.com/plugins/notebook-navigator).

**Features (full list, from stats/README page).**
- Three-pane and dual-pane layouts; folders + tags + properties + shortcuts in one view
  (https://www.obsidianstats.com/plugins/notebook-navigator)
- Visual note previews; full keyboard navigation (same source)
- Mobile-optimized layout (same source)
- Migration/switching guides from Evernote, Apple Notes, Bear, OneNote, Day One (same source) —
  evidence that its user base is refugees from those apps
- Optional Style Settings integration for theming (same source)
- Documented HTTP-request disclosure for update/download/remote-content checks (same source)

**What users LIKE.** Speed at scale ("works with 100,000+ notes"), keyboard-first flow, and the fact
that it replaces the stock file explorer entirely; the switching guides tell you exactly who it serves
(same source).

**What users WANT CHANGED.** Mostly feature-polish requests; the disciplined issue tracker at
https://github.com/johansan/notebook-navigator/issues is the canon. UNVERIFIED specifics this pass.

**Open-source status.** License: GPL-3.0 (verified from
https://raw.githubusercontent.com/johansan/notebook-navigator/master/LICENSE). Repo:
https://github.com/johansan/notebook-navigator. **GPL = CONCEPTS ONLY.**

**Pull-from assessment.** Code: not pullable (GPL-3.0). Concepts with demand evidence: (1) the file
browser is a product-defining surface, not an afterthought — people install a whole plugin to replace
it; (2) tags/properties/folders unified in one pane; (3) speed at 100k+ notes as an explicit marketing
claim; (4) migration guides as onboarding strategy. All four are directly relevant to a new
notes-app's information architecture.

---

## 13. Nostr Writer (`nostr-writer`)

**What it does.** Publishes Obsidian notes as long-form articles to Nostr (NIP-23 long-form notes),
with cover images and settings for relays/keys (https://nostrapps.com/nostr-writer; plugin page
https://community.obsidian.md/plugins/nostr-writer).

**Author:** jamesmagoo (James McGauran). **Install base:** 2,974 downloads, A trust grade, reviewed
Sep 2025 (https://www.obsidianaddict.com/best-nostr-plugins/). **Status:** in the registry; MIT.

**Features (full list, from repo README).**
- Publish note as NIP-23 long-form content (README, https://github.com/jamesmagoo/nostr-writer)
- Cover image handling (same source)
- Relay configuration; publish feedback (same source)

**What users LIKE/WANT CHANGED.** Small ecosystem; UNVERIFIED beyond the review source above. Load-bearing
for the project only as evidence of "publish-to-X from the editor" demand.

**Open-source status.** License: MIT (verified from
https://raw.githubusercontent.com/jamesmagoo/nostr-writer/master/LICENSE). Repo:
https://github.com/jamesmagoo/nostr-writer. **MIT = CODE PULLABLE.**

**Pull-from assessment.** Code: pullable (MIT), trivial scope. Concept: one-key publishing from the
editor to open social protocols. Mild demand signal; note that the plugin ecosystem generally shows
"publishing from notes" (Nostr, Quartz integration for Excalidraw, etc.) is a recurring want.

---

## 14. Opensidian (jpzk) — NOT a plugin: a Rust/Tauri Obsidian clone (HIGHEST RELEVANCE)

**What it is.** An open-source, vault-compatible, cross-platform markdown notes app: a clean-room
functional clone of Obsidian in Rust + Tauri v2, GPLv3, non-profit, under heavy development, seeking
Linux distribution maintainers. It contains none of Obsidian's code and is not affiliated with
Obsidian or Dynalist Inc. (README — https://raw.githubusercontent.com/jpzk/opensidian/main/README.md;
https://opensidian.org).

**Author:** jpzk (Pedro J., per repo history — UNVERIFIED beyond handle). **Install base:** n/a
(pre-1.0, v0.8.1 release with Linux x86_64 packages). **Status:** extremely active at the time of
research; packages tested on fresh Fedora 44 and Ubuntu 26.04 installs dated 2026-10-25 (one day
before research date). **This is the closest existing project to this research program's own goal**
(Rust/Tauri, local-first, vault-compatible) and deserves its own deep lane later.

**Features (full list, from README).**
- Vault-compatible markdown editing; opens existing Obsidian vaults (README)
- Wikilinks, backlinks, graph view (https://opensidian.org)
- Obsidian community themes work unmodified: ships AnuPpuccin (default), Material Gruvbox, Minimal,
  Solarized; theme + snippet folders read from `.obsidian/themes` and `.obsidian/snippets`, live
  reload, broken themes greyed out with the reason (README)
- **Runs Obsidian community plugins**: a clean-room reimplementation of the plugin API; community
  plugin browser with search/sort/README viewing, install/update/uninstall restricted to GitHub over
  HTTPS, sha256 recorded for every installed file, install ≠ enable (README)
- Restricted mode per vault: no community plugin code runs by default; the choice is stored OUTSIDE
  the vault so a vault cannot enable its own plugins (README)
- Secrets via system keyring (Secret Service: gnome-keyring/KWallet/KeePassXC); never written to
  files; plugins without keyring cannot store secrets (README)
- Linux packaging: slim/portable AppImage, Flatpak, RPM, DEB, Nix flake; GPG-signed SHA256SUMS
  (README)
- Build-from-source path documented and tested (README)

**What users LIKE / WANT CHANGED.** Too early for a broad user base; the README's own AI-disclosure is
notable and honest: "opensidian was built predominantly with AI models. Nearly all of the code, the
design docs, and this README were written by Claude (Anthropic's models, via Claude Code) working
from prompts, reviews, and corrections by a single human maintainer."
(https://raw.githubusercontent.com/jpzk/opensidian/main/README.md). Community traction visible via
multiple forks on GitHub (douh/opensidian, maxhille/opensidian, IronJeff80/opensidian —
https://github.com/douh/opensidian; https://github.com/maxhille/opensidian;
https://github.com/IronJeff80/opensidian) and an AlternativeTo listing
(https://alternativeto.net/software/opensidian/about/).

**Open-source status.** License: **GPL-3.0-or-later** (verified from README and repo; also
THIRD-PARTY.md governs redistribution of bundled themes). Repo: https://github.com/jpzk/opensidian.
**GPL = CONCEPTS ONLY** — and given this research program's mission, ALSO a competitor and a precedent:
it demonstrates the vault-compatibility + clean-room-plugin-API strategy is viable.

**Pull-from assessment.** Code: not pullable (GPL-3.0). **Strategic findings for us:**
(1) Vault compatibility (opening `.obsidian` vaults, reusing themes/snippets) is a legitimate,
proven approach to bootstrapping a user base; (2) a clean-room API that runs REAL Obsidian community
plugins is apparently achievable (this repo claims it; verification of which plugins actually run is
a follow-up task); (3) the security posture (restricted mode outside the vault, keyring secrets,
sha256 of plugin files, install-vs-enable separation) is a model to study and cite; (4) packaging
breadth (AppImage/Flatpak/RPM/DEB/Nix) as a Linux-first strategy; (5) their willingness to state the
AI-built provenance openly sets a norm our project should match.

---

## 15. Opensidian (thiagovasconcelosti) — same NAME, different project (name collision finding)

**What it is.** An unrelated open-source "knowledge management system inspired by Obsidian": Node.js
20 + TypeScript + Express backend, React 18 frontend, markdown notes with `[[wikilink]]` support, D3
force-directed knowledge graph, WebSocket real-time sync, JWT auth, themes, a plugin API with hooks
and commands, an MCP (Model Context Protocol) server for AI tools, REST API, Docker, Vitest test
suite (79 tests, >80% coverage), GitHub Actions CI (README —
https://raw.githubusercontent.com/thiagovasconcelosti/opensidian/main/README.md).

**Author:** thiagovasconcelosti. **Install base:** n/a. **Status:** active (CI badge, i18n READMEs in
EN/PT-BR/ES). Repo: https://github.com/thiagovasconcelosti/opensidian (HTTP 200, verified).

**License.** MIT (badge in README; verify LICENSE file on any pull). **MIT = CODE PULLABLE.**

**Findings.** (1) This is NOT the same project as jpzk/opensidian — the inventory lists both, and any
future search for "Opensidian" must disambiguate. (2) Its feature list is itself a demand sample:
multi-vault, graph, real-time sync, plugin host, and especially the MCP server (AI-tool integration as
a first-class feature in a notes app). (3) MIT means the plugin-host/MCP-server concepts AND code are
studiable directly, though the implementation quality is unverified.

**Pull-from assessment.** Code: pullable (MIT). Concepts: MCP server in a notes app (AI agents
reading/writing the vault), hooks-and-commands plugin model, WebSocket sync. Marked as demand
evidence rather than reference implementation.

---

## 16. ObbyNotes (ThatSheepGuy22/ObbyNotes) — NOT a plugin (inventory misclassification finding)

**What it is.** A small GitHub repo described as "C++ Obsidian Notes" containing an (apparently empty)
README.md and a `Dev` folder with personal markdown notes (C++ study notes). Verified via GitHub page
(HTTP 200) and raw file checks; the README at master returns HTTP 200 but renders empty
(https://github.com/ThatSheepGuy22/ObbyNotes).

**Findings.** It is someone's personal notes vault, not a plugin and not an app. Zero web presence
beyond the repo itself (two targeted searches returned nothing — recorded as a real, honest finding).
Recommend removing from the Obsidian-plugin scope in the inventory, or reclassifying as "source
material misc".

**Pull-from assessment.** None.

---

## 17. Core plugins cluster: Daily Notes (and native "core" as a competitor)

**What it does.** Daily Notes is a core (built-in, closed-source) Obsidian feature: creates/open a
timestamped note per day from a template, with a ribbon button and command; Calendar and Periodic
Notes plugins extend it (https://help.obsidian.md/daily-notes).

**Status/ownership.** Core features are proprietary to Obsidian (Dynalist Inc.); no license, no repo.
**Install base:** n/a (core). Demand evidence for the concept instead: the Calendar and Periodic
Notes plugins are consistently among the most-downloaded
(https://www.obsidianstats.com/most-downloaded).

**Features (from help docs).** Template-driven daily note creation; date-based filenames; links
between daily notes; configurable folder and format (https://help.obsidian.md/daily-notes).

**What users LIKE.** Frictionless journaling into plain files.

**What users WANT CHANGED.** Fixed-clock semantics (what counts as "today" late at night), weak
handling of missed days, no built-in period views — the reason Periodic Notes and Calendar exist.
UNVERIFIED as issue links (closed-source); theme documented across community threads.

**Pull-from assessment.** Nothing pullable (proprietary). Concept evidence: daily/periodic notes from
templates is table stakes; the complaints (time-boundary semantics, catch-up) are the differentiators.

---

## 18. Sync alternatives cluster (usual suspects): LiveSync, Remotely Save, Syncthing

### 18.1 obsidian-livesync (`obsidian-livesync`)
**What it does.** Real-time, bidirectional vault sync to a self-hosted CouchDB (or IBM Cloudant),
with end-to-end passphrase encryption, selective sync, conflict resolution, and "Object Storage" mode
storing binary files as CouchDB documents (README — https://github.com/vrtmrz/obsidian-livesync).
**Author:** vrtmrz (vorotamoroz). **Install base:** top-25 cluster
(https://www.obsidianstats.com/most-downloaded); precise count unverified this pass. **Status:** very
actively maintained (dense release history).
**Features (full list, from README):** self-hosted CouchDB sync; end-to-end encryption with
passphrase; hidden-file sync; selective sync per file/folder; automatic conflict resolution with
merge; database-scrubbing/repair utilities; P2P sync experiments; WebRTC-based device-to-device sync
option (same source).
**Likes:** "Obsidian Sync without the subscription" — the single most-cited reason users run a
CouchDB; docs-level confidence in conflict handling (same source + community threads).
**Wants changed:** setup complexity (CouchDB config, CORS, security flags) is the #1 complaint;
mobile battery/storage cost of live sync (community threads; UNVERIFIED issue links).
**License:** MIT (verified from https://raw.githubusercontent.com/vrtmrz/obsidian-livesync/master/LICENSE).
Repo: https://github.com/vrtmrz/obsidian-livesync. **MIT = CODE PULLABLE** (the replication/conflict
logic is TypeScript, but the design is directly portable).
**Pull-from:** code pullable; concepts: self-hosted encrypted sync with conflict merging as a core
feature — this plugin is the strongest evidence that users want sync they can host themselves.

### 18.2 Remotely Save (`remotely-save`)
**What it does.** Syncs the vault to S3-compatible object stores, WebDAV, Dropbox, OneDrive, pCloud,
Yandex and more, with optional E2E password encryption and scheduled or on-start sync
(plugin page https://community.obsidian.md/plugins/remotely-save; features from
https://remotely-save.readthedocs.io/en/latest/).
**Author:** remotely-save org (fengyuanchen? no — maintainers are the `remotely-save` org; per plugin
page author "remotely-save"). **Install base:** 2.3M downloads (Aug 2025,
https://medium.com/@juangui/obsidian-sync-for-free-remote-save-plugin-5e4a2ae077f5 —
figure as reported there; cross-check on obsidianstats unverified this pass). **Status:** active.
**Features (from docs):** multi-backend sync (S3, WebDAV, Dropbox, OneDrive, pCloud, Yandex, Koofr,
etc.); E2E encryption via password; sync scheduling and conflict strategy settings; file-size and
path filters; sync report logs (same source).
**Likes:** breadth of backends; works with cheap object storage.
**Wants changed:** sync bugs and slow throughput on large vaults; encryption setup confusion
(docs issues at https://github.com/remotely-save/remotely-save/issues — UNVERIFIED specifics this pass).
**License:** verified from https://raw.githubusercontent.com/remotely-save/remotely-save/master/LICENSE:
src/tests/docs/assets under Apache-2.0, but the `pro` directory under **PolyForm Strict 1.0.0**
(source-available, NOT open source). **Partially pullable:** Apache-2.0 parts only; audit which files
are which before any pull.
**Pull-from:** the multi-backend design and E2E-encryption-at-rest concept are strongly evidenced;
code pull requires per-file license audit.

### 18.3 Syncthing (not an Obsidian plugin; usual-suspect alternative)
**What it does.** Continuous peer-to-peer file synchronization (open source, no cloud).
**Status:** the Syncthing official desktop app was discontinued in 2024 but the protocol and community
forks continue — UNVERIFIED beyond community consensus this pass (search budget exhausted);
project site https://syncthing.net. For vault sync, the community pattern is "point Syncthing at the
vault folder" (https://forum.obsidian.md — recurring recommendation; UNVERIFIED link this pass).
**License:** MPL-2.0 (project site). **Pull-from:** concept only for us; it competes with in-app sync.

**Cluster takeaway (load-bearing):** the Sync alternatives cluster is the most direct evidence that
sync is where users feel the most pain with Obsidian's paid model: they will run CouchDB, configure
WebDAV, or install file-level P2P tools to avoid it. A local-first Rust app with built-in,
self-hostable, E2E-encrypted sync addresses the single loudest unmet need in this entire research
cluster.

---

## 19. Cross-cutting pull-from assessment (summary)

License ledger (verified by direct LICENSE-file reads on 2026-10-26):

| Plugin | License | Pull code? |
|---|---|---|
| Dataview | MIT | YES |
| Datacore | MIT | YES |
| Numerals | MIT | YES |
| Badges | MIT | YES |
| InkedMark | MIT | YES |
| Nostr Writer | MIT | YES |
| obsidian-livesync | MIT | YES |
| Sheets Extended | Apache-2.0 | YES |
| Remotely Save | Apache-2.0 + PolyForm Strict (`pro`) | PARTIAL, audit per file |
| Templater | AGPL-3.0 (package.json) vs GPL-3.0 (GitHub badge), no LICENSE file — CONFLICT | NO (concepts only) |
| Excalidraw plugin | AGPL-3.0 | NO (concepts only) |
| Omnisearch | GPL-3.0 | NO (concepts only) |
| Kanban | GPL-3.0 | NO (concepts only) |
| List Callouts | GPL-3.0 | NO (concepts only) |
| Meta Bind | GPL-3.0 | NO (concepts only) |
| Notebook Navigator | GPL-3.0 | NO (concepts only) |
| Opensidian (jpzk) | GPL-3.0-or-later | NO (concepts only; competitor + precedent) |
| Opensidian (thiagovasconcelosti) | MIT | YES |
| Daily Notes / core | proprietary | NO (concepts only) |

Concepts with the strongest demonstrated demand (each backed by install base + complaint patterns above):

1. **Self-hostable, E2E-encrypted sync** (LiveSync 18.1, Remotely Save 18.2) — loudest pain, paid Obsidian Sync avoidance is a whole plugin genre.
2. **Queryable vault: frontmatter as database** (Dataview 2) — top-5 install base; complaints are speed and maintenance, i.e. demand exceeds supply.
3. **Note-embedding infinite canvas** (Excalidraw 1) — the feature users say keeps them on Obsidian.
4. **Templates that run code on lifecycle events** (Templater 3).
5. **File browser as product surface** (Notebook Navigator 12) — people replace the default entirely.
6. **Interactive forms bound to frontmatter** (Meta Bind 7).
7. **Markdown-backed Kanban** (Kanban 5) — boards as views over plain text; the orphaned-maintenance story argues for making it core.
8. **Search that beats stock fuzzy ranking, with OCR/PDF extraction** (Omnisearch 4).
9. **Daily/periodic notes with better time-boundary semantics** (core cluster 17).
10. **Handwriting with searchable text layers over plain markdown** (InkedMark 11) — new but strategically aimed at the Apple Notes escape.
11. **Merged cells / vertical headers / spreadsheet formulas in markdown tables** (Sheets Extended 8 + ecosystem).
12. **AI/agent integration: MCP server against the vault** (Opensidian-2 15).

Process notes and caveats: obsidianstats.com and community.obsidian.md render download figures via
JavaScript, so several install-base numbers are marked UNVERIFIED this pass; the official
community-plugins.json registry (raw.githubusercontent.com) was used as the canonical author/ID source
for all 16 plugins. Templater's license is genuinely conflicted and needs a one-time human check of
the actual packaged LICENSE before any conclusions. ObbyNotes is a misclassified inventory entry.
Nothing from gettbb.app/get-bb.app or `bb-*` was researched, per the owner's directive.
