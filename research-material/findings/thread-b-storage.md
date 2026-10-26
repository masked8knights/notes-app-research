# Thread B — The Storage Question: block store vs plain-file mirror

Research brief lane B. Finds what gates the data model: should the primary store be a
block/object store with IDs and positions (files as derived artifacts), or a plain-file
mirror on disk (the files ARE the API, accepting Markdown's limits)?
Date of research: 2026-10-26. All claims carry a source URL; UNVERIFIED marks pages that
blocked or were not confirmed.

---

## 0. The two poles named in the brief

**Thymer — the mirror.** Thymer's "Markdown Mirror" page states the full position: a
multiplayer structured workspace ("pages, dashboards, galleries, databases, and tasks") on
one side, and "a live reflection of the workspace as plain Markdown, kept in two-way sync"
on the other. Thymer explicitly says the app is the source of truth and the mirror is the
openness layer: "Keep Thymer as your source of truth while using the tools that work best
on plain files", agents and scripts "read and write files, working on the same live
workspace", and the Markdown exists because "The Markdown is for your tools, not your
team."
Source: https://thymer.com/markdown-mirror

Note what Thymer is claiming structurally: a block/structured store as primary, with a
continuous two-way file projection of it. That is not the Obsidian model (files ARE the
store); it is the Logseq-DB-goal model (see §2.3) and the Anytype-export-goal model, but
run continuously instead of on demand.

**Ideon — no plain files attempted.** Ideon's homepage presents "everything is a block"
(structured blocks: repos, palettes, stakeholders, links, files, text), spatial canvas
organization, workspace versioning/snapshots, and realtime multiplayer, installed via a
single Docker command that provisions "database, server, everything." Nothing on the page
mentions Markdown, files on disk, or export.
Source: https://www.theideon.com/
(Their FAQ/blog sections were not fetched in detail; UNVERIFIED whether deeper export
features exist beyond what the homepage shows.)

---

## 1. How existing apps actually solved it

### 1.1 Obsidian — file-first, with a second file format for canvas

Obsidian stores a vault as "folders of Markdown files, so there's absolutely no lock-in"
(sales framing, but it matches the storage doc): the note content is ordinary .md files
editable in any editor. Source: https://www.sitepoint.com/obsidian-beginner-guide/

What `.obsidian` covers: Obsidian creates a `.obsidian` config folder in the vault root
holding vault-specific preferences — hotkeys, themes, community plugins, core-plugins.json,
app.json, appearance.json, and workspace files. `workspace.json` (and `workspaces.json`)
store current workspace layout and "update whenever you open a new file" — Obsidian itself
advises gitignoring them for noisy commits. Global settings (account, global appearance)
live in a separate system folder. Sources:
https://help.obsidian.md/data-storage
https://simplememofast.com/en/obsidian/what-is-vault/

So in Obsidian's file-first world, *metadata beyond note content* still leaks out of
Markdown into JSON sidecar files and a hidden metadata cache (IndexedDB). File-first does
not mean "everything is Markdown"; it means content is Markdown and everything else is
app-private JSON around it.

Canvas: Obsidian saves canvases as `.canvas` files "using the open JSON Canvas format" —
a root JSON object with `nodes` and `edges` arrays; node types include `text`, `file`
(referencing vault notes by path), links, and groups. In March 2024 Obsidian spun the
format out as JSON Canvas (jsoncanvas.org) "in hopes of providing longevity, readability,
interoperability, and extensibility" — MIT-licensed, free for any app to implement.
Sources:
https://help.obsidian.md/plugins/canvas
https://obsidian.md/blog/json-canvas/
https://github.com/kepano/obsidian-skills/blob/main/skills/json-canvas/SKILL.md

Key structural observation: in Obsidian, the canvas is a *sibling file* to the notes it
positions. Positions and edges live in the .canvas JSON; note content stays in the .md
files the nodes point at. That split is exactly why the canvas↔note bridge (§3.1) works
live in both directions without any sync machinery.

Known cost of file-first: renaming a note rewrites every file containing a wikilink; a
Reddit rant on "the cardinal flaw of file over app" makes the block-store argument that
"you could easily have file objects where the id is just linked to whatever name you
choose." Source: https://www.reddit.com/r/ObsidianMD/comments/1epg7ie/

### 1.2 Anytype — encrypted object store, files unreadable by design

Anytype is offline-first: "all data you create will be stored locally first", synced via a
private IPFS-style P2P network. The storage doc states the vault folder contains "every
Object, every encrypted block, every file you've uploaded, plus the indexes", and that
"Files are stored inside flatfs dir in encrypted fragments, so they can't be accessed
outside of Anytype." Media is streamed on demand and deduplicated. Community threads
confirm the vault is opaque blobs + index folders, not readable documents.
Sources:
https://doc.anytype.io/anytype/data/storage
https://community.anytype.io/t/local-storage-location-folder-sharing/10504

Export story is the pressure valve and it has repeatedly disappointed: a 2024 thread
"Export is not great" reports Markdown export dropping everything but names ("I worry
about data preservation. Let's suppose I need to move away from Anytype"); a 2025 thread
("Migrating away") says property-rich data makes "the markdown export useless" and "your
data will be encrypted and usable only with proprietary Anytype." Anytype improved this in
release 0.47.4 (July 2025), where "Markdown import and export now support properties and
types", and a co-founder pushed back on the lock-in charge on the community forum.
Sources:
https://www.reddit.com/r/Anytype/comments/1bfzyp7/export_is_not_great/
https://www.reddit.com/r/Anytype/comments/1jx14l3/migrating_away_from_anytype/
https://www.reddit.com/r/Anytype/comments/1m25sw6/markdown_export_and_import_now_support_properties/
https://www.reddit.com/r/Anytype/comments/1gnz6rn/goodbye_roundup/
https://www.reddit.com/r/Anytype/comments/1k4w1pw/why_not_use_markdown/ (the framing "Anytype
isn't just a note-taking app — it's a local-first, end-to-end encrypted object database…
Markdown is great for linear text, but it can't handle the complex data Anytype treats as
first-class citizens")

Takeaway: an object/block store with strong encryption makes a *faithful* plain-file
projection genuinely hard; Anytype's answer has been improving one-way export, not a
mirror.

### 1.3 Logseq — blocks written onto file lines, and the pivot away from it

Classic Logseq (now "Logseq OG") stores "every note as a plain Markdown or Org-mode file
on your local disk", but the block is the atom: "an outliner where every line is a block"
— each block is a bullet (`-` line), indentable, referenceable, embeddable.
Sources:
https://makerstack.co/reviews/logseq-review/
https://kolavistudio.com/markdown-tools/logseq

The known pain points of that encoding, all from users and the project's own tracker:

- "Logseq uses Markdown syntax but not every Markdown file is a valid Logseq page,
  basically because of dashes: Logseq expects them to define blocks."
  https://discuss.logseq.com/t/were-dashes-really-needed-for-outlining/7203
- Logseq began inserting hyphens on every line, "breaking MD functionality":
  https://github.com/logseq/logseq/issues/3457
- Users on portability: "I want normal markdown files that I can take with me anywhere";
  others note the encoding is "risky in regard that if you want to switch to another app…
  you might lose knowledge."
  https://www.reddit.com/r/logseq/comments/1329eww/
  https://www.reddit.com/r/logseq/comments/189sv4e/
- Worst case: "Edits in Logseq not being written to local files: UNRECOVERABLE DATA LOSS"
  — a sync/writing defect where in-app edits never hit ./pages/*.md.
  https://discuss.logseq.com/t/edits-in-logseq-not-being-written-to-local-files-unrecoverable-data-loss/23031

The decisive primary source is Logseq's own April 2024 post "Why the database version and
how it's going?" The team's stated reasons to leave files as the primary store:
- "Creating a new block requires rewriting the entire Markdown file."
- "Renaming a page updates all files that reference it."
- "The structure data support is limited compared to a database, lacking features like
  persistent IDs, timestamps, and more."
- Their goals: stability, reliable undo/redo, performance, "effortlessly supporting up to
  50,000 pages", Datalog queries, custom classes/properties, offline-first RTC with E2EE.
- FAQ in the same post: "Are you going to deprecate Markdown files support? No… with a
  long-term goal of achieving seamless two-way sync between the database and markdown
  files." Founder tienson: "We plan to experiment with two-way sync (either real-time or
  periodically) between the db and markdown files once the db is more stable."
Source: https://discuss.logseq.com/t/why-the-database-version-and-how-its-going/26744

Status in 2026: Logseq split into Logseq OG (file-based) and the database version; OG is
in maintenance-only mode without reaching 1.0, and the DB version was still in public
testing through late 2025/2026 with mobile and RTC in earlier testing.
Sources:
https://www.outlinersoftware.com/topics/viewt/12614/0/logseq-db-update
https://discuss.logseq.com/t/whats-new-with-logseq-db-may-16th-2026/35020
https://dessence.ai/blog/logseq-alternatives-after-stalled-development-2026
A community FAQ notes DB users should "enable hourly backups to the filesystem" — i.e. the
file plane in the DB version is a *backup/export* surface, not the store.
Source: https://www.outlinersoftware.com/topics/viewt/12472

Logseq is the strongest evidence in this lane that the mirror is a *goal that even the
team that wants it has not shipped*: the two-way db↔markdown sync they promised in 2024
was still aspirational two years later, while the two-way file mirror (OG) came with
data-loss and portability complaints of its own.

### 1.4 Tana — proprietary cloud DB, export as pressure valve

Tana's supertags turn any node into typed structured data. Storage is a proprietary cloud
database; the migration-focused write-ups are blunt: "Vendor lock-in: Your data lives in
Tana's proprietary format."
Source: https://justmarkdown.com/blog/tana-to-markdown-migration
Users: "Currently, you can export… JSON… but unless you know what to do with the JSON it
is a bit limited… However, you can also export your data in plain markdown" (2023); a
2025 release thread celebrates "First version of Export as Markdown is finally here"
(subset-by-supertag, with/without fields), with JSON as "the full export with all metadata
(incl. Tana-specific structures)."
Sources:
https://www.reddit.com/r/TanaInc/comments/13uoh7e/
https://www.reddit.com/r/TanaInc/comments/1kocdr8/
Community tooling fills the gap: TanaMigrator converts the JSON workspace export into "a
vault of markdown files," with the author warning of edge cases.
Source: https://www.reddit.com/r/TanaInc/comments/1qo42xs/
The canonical stay-away argument: "it is proprietary and cloud-based… Tana supports
exports to formats like Markdown or JSON, so you can typically recover most of your raw
content" — most, not all. Source:
https://www.dsebastien.net/the-reasons-ill-never-switch-from-obsidian-to-tana/

### 1.5 Reflect — cloud app learned to become file-first

Reflect Classic: E2E-encrypted cloud notes; export to "reflect json, csv, markdown zip
file, and html zip file", and daily backups to the hard drive (a copy, not a mirror —
one user complained you "can only export all your notes in one go").
Sources:
https://reflect.academy/import-export-backups
https://www.reddit.com/r/PKMS/comments/1k7unys/
https://stephenjzeoli.medium.com/reflect-my-perfect-notes-application-af0978de3373

Notable 2026 move: Reflect's homepage now leads with "Reflect Open — An open-source
note-taking app with daily notes, backlinks, and local Markdown files… Local files: Keep
your notes in a folder you choose… Your choice of sync: iCloud Drive or Git", with
Classic ("Paid Reflect Classic subscribers…") still maintained. A cloud block-ish app
added a plain-file sibling product rather than a mirror of the existing one.
Source: https://reflect.app/

### 1.6 TriliumNotes — SQLite store, and the clearest written defense of it

Trilium stores everything (notes, tree, metadata, config) in one SQLite `document.db`;
content is HTML, not Markdown. Sources:
https://docs.triliumnotes.org/user-guide/advanced-usage/database
https://ourbigbook.com/cirosantilli/trillium-notes

The FAQ answers "Why database instead of flat files?" head-on: "file systems are simply
not powerful enough for what we want to achieve." Their enumerated reasons: clones ("hard
directory links") don't exist in filesystems; filesystems separate directory vs file
while Trilium deliberately doesn't; no user-controlled ordering; attributes would need
extended attributes that differ per OS; links between notes would become "side-car files
(mini-databases)"; and "Filesystems are generally not transactional… having transactions
make it way easier to keep notes and their metadata in predictable and consistent state."
Source: https://docs.triliumnotes.org/user-guide/faq

They also warn the other direction: never sync document.db with Dropbox/GDrive/OneDrive —
"they will corrupt the database file" (`database disk image is malformed`); only the
built-in sync server is supported. Source: same FAQ page.

Trilium's export story ("take them back out in open formats") is one-way per request.
Source: https://triliumnotes.org/

### 1.7 AFFiNE / BlockSuite — pure block store, canvas and page are views

AFFiNE's stated goal: "everything was a block — something that could be edited and
transformed freely." BlockSuite documents are a block tree "structured as a tree and
stored within a Y.Map" (CRDT), with `sys:id`, `sys:flavour`, `sys:children` — persistent
block IDs and parent/child structure with no file concept anywhere.
Sources:
https://affine.pro/blog/who-are-we-and-what-makes-affine
https://docs.affine.pro/blocksuite-wip/store/

Edgeless (canvas) mode adds a `surface` block holding all whiteboard elements: "Root
Block → Surface Block → (Embed/Shape/Brush elements, Note blocks…)"; "blocks can have two
potential storage locations" — inside a note's block tree, or as elements of the surface.
A page and an edgeless canvas are both just database views: "a Page is a type of Database,
as is Edgeless."
Sources:
https://blocksuite.io/components/editors/edgeless-data-structure
https://docs.affine.pro/core-concepts/elements-of-affine/blocks-with-databases

Storage is local IndexedDB/SQLite per platform plus sync servers; no plain-file story of
the Thymer kind exists in BlockSuite. (Docs do not mention one; UNVERIFIED beyond docs
read here.)

---

## 2. Canvas ↔ note bridge prior art: does anything ship "live both ways"?

"Live in both directions" at the storage layer means: the canvas region and the note are
not two copies that sync, but one object (or two files with a strict reference) such that
editing either surface edits the same underlying data. Survey:

**Ships it — Obsidian Canvas.** A canvas node of type `file` references a real .md file in
the vault. Editing the note inside the canvas edits the note file; the file is the single
source of truth and the canvas holds only position/size/edges. Editing the same note in
the editor is instantly "live" on the canvas because there is no second copy. This is the
most widely shipped version of the bridge, and it works *because* storage is files plus
one sibling JSON file.
Source: https://help.obsidian.md/plugins/canvas (plus format detail:
https://github.com/kepano/obsidian-skills/blob/main/skills/json-canvas/SKILL.md)

**Ships it — Heptabase.** A card on a whiteboard *is* the note: same object, opened
in-place on the canvas or as a document. Bi-directional links between cards/dates/
whiteboards; content exportable as Markdown "at any time". Cards live in a local database
(offline-first), optionally synced to AWS; card files on disk are GUID-named internals,
and export produces human-named Markdown — i.e., one-way projection of a block store.
Sources:
https://wiki.heptabase.com/version-one
https://www.reddit.com/r/PKMS/comments/16341ft/ (GUID vs export-name observation)
https://support.heptabase.com/en/articles/10448141-is-my-data-safe-in-heptabase

**Ships it — AFFiNE edgeless.** Note blocks live inside the same Y.Map document as the
surface; edgeless and page mode are two views of one store. A "region becoming a normal
linked note" is native because notes ARE blocks on the canvas. Again: block store, no
plain-file bridge.
Sources:
https://blocksuite.io/components/editors/edgeless-data-structure
https://docs.affine.pro/core-concepts/elements-of-affine/blocks-with-databases

**Partial — Excalidraw plugin (Obsidian).** Drawings are files in the vault
(.excalidraw.md) that "link to them [notes], and can be embedded directly into your
markdown"; the plugin can convert an existing Markdown note into an Excalidraw drawing to
use "both sides of the card", with known rough edges (Markdown reading-mode rendering bugs
in hybrid notes; JSON-embedded-in-markdown rather than a clean block store). "Live"
embedding exists in the ecosystem (e.g., Sync Embeds plugin turns transclusions into
"live, editable, two-way synced blocks"), but each is a plugin-level overlay, not a
storage-layer guarantee.
Sources:
https://danholloran.me/posts/excalidraw-in-obsidian-visual-thinking-that-lives-in-your-vault
https://github.com/zsviczian/obsidian-excalidraw-plugin/issues/1706
https://github.com/zsviczian/obsidian-excalidraw-plugin/issues/1705
https://community.obsidian.md/plugins/sync-embeds

**Does not ship it — Milanote, tldraw, Kinopio, Muse.** These are canvas-first with
shape/card objects, not notes:
- Milanote: boards of elements; export is per-board PDF/PNG/doc; a formal request exists
  on their roadmap poll to "Export your data in a proprietary Milanote format" (i.e., even
  a full proprietary dump is wanted and not shipped); users complain "No Easy Export /
  Backup?"
  https://help.milanote.com/en/articles/111395-exporting-your-work
  https://poll.milanote.com/c/49-export-your-data-in-a-proprietary-milanote-format
  https://www.reddit.com/r/Milanote/comments/1aujmvl/
- tldraw: the store is a JSON snapshot of shape/page/binding records; "document (shapes,
  pages, bindings)… and session (camera, selection, UI state)" are separated. Shapes are
  not notes; there is no note bridge to bridge.
  https://tldraw.dev/docs/persistence
  https://tldraw.dev/reference/tlschema/TLSerializedStore
- Kinopio: spaces export "in a plain text, JSON and PDF formats" — one-way.
  https://kinopio.club/help/exporting/
- Muse (canvas thinking tool, 2019–2023) raised $2M, never found a viable business model,
  and pivoted (now Allume) — a reminder that the canvas-app category has a mortality
  rate; whatever storage is chosen, users depended on the company surviving.
  https://adamwiggins.com/muse-retrospective/
  https://x.com/MuseAppHQ

**Finding:** the live canvas↔note bridge ships, but only inside (a) file-first apps where
the note file is the shared truth (Obsidian Canvas, Excalidraw embeds), or (b) block-store
apps where the canvas and page are two views over the same blocks (Heptabase, AFFiNE). No
app ships it across a *boundary* between a block store and an external plain-file mirror;
in every shipped case the two surfaces share one store. Thymer's mirror and Logseq's
unshipped db↔md two-way sync are the only serious attempts to put the boundary itself
under continuous sync.

---

## 3. Export vs mirror: the arguments and the real-world record

**The mirror promises (Thymer):** portability, agent/tool access ("Run terminal tools
like ripgrep… Hand work to tools like Claude Code"), import/backup/export from a plain
folder, no lock-in — while the structured editor keeps the team-facing UX.
Source: https://thymer.com/markdown-mirror

**What two-way file sync has actually cost (Logseq OG record):**
- Hyphen-every-line encoding makes files non-portable Markdown despite being files
  (§1.3 sources).
- A file-writing defect produced unrecoverable data loss (edit never written to disk):
  https://discuss.logseq.com/t/edits-in-logseq-not-being-written-to-local-files-unrecoverable-data-loss/23031
- Wikilink-based identity means renames fan out across files (Obsidian case):
  https://www.reddit.com/r/ObsidianMD/comments/1epg7ie/
- General Obsidian-forum hunger for going beyond .md ("does the use of .md format also
  doomed Obsidian to miss some advanced features? Like a database?"):
  https://forum.obsidian.md/t/it-is-hoped-that-obsidian-will-not-be-bound-by-the-framework-of-md/10480

**What block-store-first has actually cost (Anytype/Tana/Trilium/Logseq-DB record):**
- Export fidelity gaps that users experience as hostage-taking (Anytype, Tana — §1.2, §1.4).
- The store is unusable outside the app: Anytype's encrypted fragments "can't be accessed
  outside of Anytype" (https://doc.anytype.io/anytype/data/storage); Trilium's
  document.db corrupts under generic sync services (https://docs.triliumnotes.org/user-guide/faq).
- On abandonment, users are left with whatever export existed at the last release — and
  where properties/fields were involved, the exports lost them (Anytype, Tana threads
  above; TanaMigrator's "VERY good chance edge cases exist" warning:
  https://www.reddit.com/r/TanaInc/comments/1qo42xs/).
- A Reddit straw poll on "if Obsidian went database tomorrow" shows the loyalty file-first
  buys and how users reason about it ("Right now there's basically zero chance of the app
  going south like changing note storage formats"):
  https://www.reddit.com/r/ObsidianMD/comments/1aeetyz/

**The strongest pro-database argument on record (Trilium FAQ, §1.6):** filesystems cannot
do clones, arbitrary ordering, per-note attributes, fast cross-note links, or
transactions. Note that Thymer's answer to every one of those is the same as Trilium's
*architecture* (a structured store) — Thymer just also commits to a live file projection,
which Trilium and Anytype do not attempt.

**The honest synthesis:** the industry converged on block stores with IDs (Trilium,
Anytype, Tana, BlockSuite, Logseq DB, Heptabase, Ideon) for exactly the feature reasons
Trilium and Logseq enumerate; file-first survivors (Obsidian) concede metadata to sidecar
JSON and accept rename-fanout; and every serious "files as first-class citizens" attempt
that also needs structure ends up promising a two-way sync it finds very hard to ship
(Logseq 2024→2026). Two-way file mirror at high fidelity is the road Logseq has been
walking for two-plus years without arriving.

---

## 4. Conclusion for the Rust app: what the evidence supports

1. **The evidence supports block store as primary, with export and/or a bounded mirror as
   a projection — not files-as-primary.** Every app in this survey that supports canvas
   positions, stable block references, properties, or realtime collab ended up with IDs
   in a store (SQLite/Yjs/proprietary); the two that kept files primary (Obsidian,
   Logseq OG) paid in rename fanout, sidecar JSON, and non-portable "Markdown".
2. **Obsidian-style canvas design is the proven cheap version of the bridge:** notes are
   files/blocks with stable identity; a canvas is one JSON document of
   (position, size, edges, note-references). The bridge is live both ways *for free*
   because the canvas never duplicates note content. For a Rust app: store canvas layout
   as a JSON (or bincode) artifact keyed by note IDs; never copy note text into the
   canvas record. This gives Heptabase-style "region becomes a note" and "note is placed
   on canvas" without any sync engine.
3. **If a plain-file story is wanted, Thymer's mirror is a heavier commitment than it
   looks** — it is effectively the Logseq DB two-way sync goal plus one-way export, with
   all the hard cases Logseq has not finished after 2+ years: delete/create/rename
   reconciliation, preserving block IDs across round-trips (Markdown has none), and
   conflict rules. A staged version is defensible: one-way faithful export first
   (properties in frontmatter/Anytype-0.47.4-style), two-way sync later for
   documents-only (excluding canvases, which get a JSON Canvas .canvas artifact — an
   open, MIT format built exactly for interoperability:
   https://obsidian.md/blog/json-canvas/).
4. **Nobody ships a live two-way bridge between a block store and an external file
   folder today.** Anything we build there is novel; treat that as risk, and the
   file-mirror as a feature with a documented failure surface (Logseq OG data-loss
   thread), not an obvious default.
5. **Data longevity argument cuts both ways and mostly favors "export you can trust":**
   files-first apps die slower (Obsidian loyalty, §3), but the actual losses reported in
   block-store apps are export-fidelity losses, not storage-format losses — and Muse's
   death shows canvas apps as a category carry mortality risk that pure storage choices
   don't fix. A guaranteed-lossless export (JSON dump of the whole store + Markdown
   projection of documents + JSON Canvas for canvases) covers the longevity need at a
   fraction of the mirror's cost.

### Open sub-questions remaining

- Mirror scope: if a mirror is built, which projections round-trip losslessly? (Block IDs
  in HTML comments/frontmatter vs re-deriving identity from headings; Logseq's hyphen
  history suggests "not all".)
- Conflict policy: how do concurrent app-side and disk-side edits resolve in a mirror?
  (No surveyed app documents one for this case; Logseq DB has not shipped theirs.)
- Do canvas regions need to be *first-class notes* (Heptabase/AFFiNE) or only *hold
  notes* (Obsidian)? This decides whether the block store needs a "region → note"
  promotion operation.
- Whether the exported canvas should be JSON Canvas (interoperable with Obsidian today)
  or a richer internal JSON (Heptabase-style full export).
- UNVERIFIED areas: Ideon's actual on-disk format (Docker DB; homepage silent on
  export); Reflect Open's storage details beyond homepage claims; AFFiNE's exact local
  persistence per platform.

---

## Source index

Primary (docs/official):
- https://thymer.com/markdown-mirror — Thymer's two-way mirror claim
- https://www.theideon.com/ — Ideon blocks/canvas/Docker positioning
- https://help.obsidian.md/plugins/canvas — .canvas files, JSON Canvas
- https://obsidian.md/blog/json-canvas/ — JSON Canvas open format announcement
- https://help.obsidian.md/data-storage — .obsidian folder contents
- https://doc.anytype.io/anytype/data/storage — Anytype local-first encrypted blocks
- https://discuss.logseq.com/t/why-the-database-version-and-how-its-going/26744 — Logseq's
  reasons for the database version and two-way sync goal
- https://docs.triliumnotes.org/user-guide/faq — Trilium's why-database argument
- https://docs.triliumnotes.org/user-guide/advanced-usage/database — document.db
- https://triliumnotes.org/ — "take them back out in open formats"
- https://blocksuite.io/components/editors/edgeless-data-structure — surface block model
- https://docs.affine.pro/blocksuite-wip/store/ — Y.Map block tree with IDs
- https://affine.pro/blog/who-are-we-and-what-makes-affine — everything-is-a-block
- https://wiki.heptabase.com/version-one — cards as notes, Markdown export anytime
- https://support.heptabase.com/en/articles/10448141-is-my-data-safe-in-heptabase — local
  DB + AWS
- https://tldraw.dev/docs/persistence — snapshot model (document vs session)
- https://kinopio.club/help/exporting/ — text/JSON/PDF export
- https://help.milanote.com/en/articles/111395-exporting-your-work — Milanote export limits
- https://poll.milanote.com/c/49-export-your-data-in-a-proprietary-milanote-format —
  user request for full export
- https://reflect.app/ — Reflect Open, local Markdown files
- https://reflect.academy/import-export-backups — Classic exports/backups
- https://outliner.tana.inc/help/import-and-export — Tana export formats
- https://justmarkdown.com/blog/tana-to-markdown-migration — Tana lock-in assessment
- https://adamwiggins.com/muse-retrospective/ — Muse lifecycle

Community/secondary:
- https://www.reddit.com/r/logseq/comments/15s1ul2/ , /1329eww/ , /189sv4e/ — Logseq
  portability pain
- https://discuss.logseq.com/t/were-dashes-really-needed-for-outlining/7203
- https://github.com/logseq/logseq/issues/3457 — hyphen regression
- https://discuss.logseq.com/t/edits-in-logseq-not-being-written-to-local-files-unrecoverable-data-loss/23031
- https://www.outlinersoftware.com/topics/viewt/12614/0/logseq-db-update , /12472 — OG
  maintenance mode; DB backups
- https://discuss.logseq.com/t/whats-new-with-logseq-db-may-16th-2026/35020
- https://www.reddit.com/r/Anytype/comments/1bfzyp7/ , /1jx14l3/ , /1m25sw6/ , /1gnz6rn/ ,
  /1k4w1pw/ — Anytype export record
- https://www.reddit.com/r/TanaInc/comments/13uoh7e/ , /1kocdr8/ , /1qo42xs/ — Tana export
- https://www.reddit.com/r/PKMS/comments/1k7unys/ , /16341ft/ , /1cdqsu6/ — Reflect,
  Heptabase internals
- https://www.reddit.com/r/Milanote/comments/1aujmvl/ — Milanote backup complaint
- https://www.reddit.com/r/ObsidianMD/comments/1epg7ie/ , /1aeetyz/ — file-over-app debate
- https://forum.obsidian.md/t/it-is-hoped-that-obsidian-will-not-be-bound-by-the-framework-of-md/10480
- https://www.sitepoint.com/obsidian-beginner-guide/ — vault = folders of .md
- https://simplememofast.com/en/obsidian/what-is-vault/ — .obsidian inventory
- https://github.com/zsviczian/obsidian-excalidraw-plugin/issues/1706 , /1705 — note↔
  drawing conversion and its bugs
- https://danholloran.me/posts/excalidraw-in-obsidian-visual-thinking-that-lives-in-your-vault
- https://community.obsidian.md/plugins/sync-embeds — live two-way transclusions plugin
- https://www.reddit.com/r/logseq/... kolavistudio.com, makerstack.co — block-per-line
  framing
