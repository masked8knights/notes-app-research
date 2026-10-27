# Features Master: every note app, every feature, in depth

One table per app; each row is one claim with its source.

Compiled from all findings files in `research-material/findings/`. One section per app, then per open-source repo, then integration components, then two synthesis sections. Every claim carries its source findings file(s). Nothing here is invented; where a finding was marked UNVERIFIED in the source, that is carried through.

Conventions: every app and repo section uses the same groups in the same order: **Features** (Area | Detail), **Sentiment** (What people say), **Wants** (What people want changed), and **Pricing and platforms** (Item | Detail); empty groups are omitted. One row is one claim. A findings-file Sources line sits under each section; URLs, UNVERIFIED markers and fact-check notes are appended in parentheses at the end of the row they belong to.

---

# PART I: APPS

## Goodnotes

**Features**

| Area | Detail |
|---|---|
| Capture/ink | Pen and highlighter with ink smoothing. |
| Capture/ink | Handwriting with ink rendering tuned per device. |
| Canvas/ink | PDF and image annotation. |
| Canvas/ink | "infinite-ish" paper templates. |
| Canvas/ink | Lasso tool. |
| Canvas/ink | Links between notes. |
| Editing | Handwriting OCR search and conversion. |
| Editing | Handwriting spellcheck/completion (AI-driven in Goodnotes 6). |
| Audio | Audio recording alongside notes. |
| Organization | Notebooks. |
| Organization | Marketplace content (stickers, planners). |
| AI | Assist features (summarize, define). |
| AI | Handwriting spellcheck/completion. |
| Sync | iCloud sync. |
| Export | PDF export. |

**Sentiment**

| What people say |
|---|
| Handwriting search across notes plus audio recording "coupled with writing notes" was used by a user through years of law school. |
| Links, lasso, and the broad feature set were called the best among iPad notebooks. |
| Rated the most user-friendly iPad notebook with the best handwriting-box search for students. |
| G2 reviewers praise quick capture that can be developed later. |
| G2 reviewers praise a laser pointer for presentations. |
| The AI ink-smoothing actually deforms handwriting for some users, tied to Apple Pencil hover behavior. |
| Reviewers note Notability and Apple Notes do not do this. |
| AI outputs arrive in a generic typed font instead of handwriting, a recurring irritation. |
| Sync complaints exist even for iCloud users. |

**Wants**

| What people want changed |
|---|
| Ink that never rewrites what you wrote (auto-correcting smoothing off). |
| Forced handwriting completion/spellcheck should be optional. |
| Subscription/price creep ("too expensive for how buggy it is"). |
| Windows tiers feel pricey. |
| An end to UI/UX churn ("we don't need new features"). |
| AI output rendered in handwriting rather than typed font. |
| New-app signal from the findings: ink fidelity without a subscription. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | iPad/macOS/Windows/web apps (cross-platform). |
| Business | Goodnotes 6 pricing: Essential $11.99/yr and Pro $35.99/yr. (goodnotes.com/pricing, R8 fact-check) |
| Business | The one-time $29.99 "Special Edition" purchase exists on Apple only and is listed only in the FAQ rather than as a plan card, so "buried" is fair. (R8 fact-check) |
| Business | AI Pass add-on $9.99/mo. |
| Business | Closed source. |

Sources: apps-likes-wants.md

## Notability

**Features**

| Area | Detail |
|---|---|
| Capture/ink | Handwriting. |
| Capture/ink | PDF annotation. |
| Audio | Audio recording time-linked to ink: tap a stroke to jump to that moment in the recording. |
| Audio | Annotations made during playback sync back into the timeline. |
| Sync | iCloud sync. |
| Export | PDF export. |
| Export | Export as PDF+audio zip. |

**Sentiment**

| What people say |
|---|
| Time-synced audio is the signature: audio synced to notes called "LIFE CHANGING" for lectures. |
| Tapping written text jumps the audio to that moment. |
| Minimalist interface people explicitly say they love. |
| Several ex-Goodnotes users call it the best handwriting experience. |
| The 2021 switch from one-time purchase to subscription is the defining grievance of the app's community, with users demanding refunds. |
| Pattern of repeated re-subscription pushes: Plus relaunch in 2024 ("era of bought-for-life Notability is over"). |
| Then "remove required paid subscription" threads. |
| iCloud sync is locked behind the subscription. |
| Notes failing to load reported. |
| Heavy moderation/censorship of complaints on their subreddit. |
| The "Classic Plan" restore path was reported broken. |

**Wants**

| What people want changed |
|---|
| Pay once and keep everything. |
| Never hold sync hostage behind a subscription. |
| Honor the Classic plan. |
| Stop repeated re-subscription pushes. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | iPad/Mac. |
| Business | Free/Classic/Plus subscription tiers (history of plan changes). |

Sources: apps-likes-wants.md

## Noteshelf

**Features**

| Area | Detail |
|---|---|
| Capture/ink | Handwriting with tuned pen pressure and ink rendering. |
| Editing/canvas | Templates. |
| Audio | Audio recording. |
| Export | Vector PDF export. |
| Integration | Evernote push. |

**Sentiment**

| What people say |
|---|
| Fountain-pen ink rendering is the standout: "only app to produce a decent fountain pen and my handwriting looks the best". |
| Fountain-pen rendering rated on par with Samsung Notes. |
| Vector PDF export is the deciding feature over Samsung Notes for some users. |
| Paid Noteshelf 2 "lifetime" buyers had to pay again for Noteshelf 3, a lifetime-promise breach pattern the findings flag as a caution for the new app. |

**Wants**

| What people want changed |
|---|
| True lifetime ownership (no paid v3). |
| Catch up on feature lag versus rivals. |
| Stronger cloud backup. |
| Fix bugs (annotations disappearing, tour restarting every launch, scrolling lag, no web preview). |
| Bring the Android version to parity with iPad. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | iPad/Android/Windows. |

Sources: apps-likes-wants.md

## Amphi

**Features**

| Area | Detail |
|---|---|
| Naming | Note that two products share the name. |
| Identity | (a) Amphi Notes: free open-source cross-platform plain-text notebook. |
| Identity | Amphi Notes has folders like a file system, image/video insertion, markdown-ish text. |
| Identity | (b) Amphi (useamphi.com): closed-source iPad student canvas app. |
| Organization | File-system-like folders. |
| Organization | The canvas app combines notes, documents, flashcards, timers, calculators. |
| AI | Embedded AI tutors and study widgets (canvas app). |
| Sync | Self-hosted sync server or Amphi Cloud (Amphi Notes). |

**Sentiment**

| What people say |
|---|
| XDA reviewers liked one canvas replacing several student apps. |
| Community lives on Discord. |
| The self-hosted, own-your-data sync model draws open-source users. |
| The app is very small (about 2 downloads/30 days per AppBrain), so there is little recurring praise or complaint data; the findings state this explicitly rather than inventing a consensus. |
| Known friction: cannot take notes while a study widget is open on the canvas (a frequent complaint on Amphi's Discord, reported via XDA). (UNVERIFIED beyond that single writeup) |

**Wants**

| What people want changed |
|---|
| Allow note-taking while a study widget is open on the canvas. |
| New-app signal: open local files plus easy self-hosted sync. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Cross-platform (Amphi Notes). |
| Platform | iPad (canvas app). |
| License | Amphi Notes GPL-3.0+. |
| License | The iPad Amphi AI app is closed source. |

Sources: apps-likes-wants.md

## Evernote

**Features**

| Area | Detail |
|---|---|
| Capture | Web clipper (its most famous feature). |
| Capture | Notebooks/tags. |
| Organization | Notebooks/tags. |
| Organization | Reminders. |
| Organization | Tasks. |
| Search | Powerful search including text in images. |
| AI | AI features recently added. |
| Sync | Full sync across platforms. |

**Sentiment**

| What people say |
|---|
| The web clipper is repeatedly called the best on the market, the thing people still miss after leaving. |
| Deep search/archive value: decades of notes retained. |
| Users stay for the archive. |
| An app-store-review analysis cited 57% of negative reviews on price/upsell/AI versus 4% technical faults. (UNVERIFIED in the R8 fact-check (the source could not be re-located); treat only the community complaints below as sourced) |
| Layoffs of the entire US team and months of silence followed the acquisition. |
| Community mood: WSJ "Evernote is dying" discussion. |
| Export/alternatives threads are the most upvoted content. |

**Wants**

| What people want changed |
|---|
| Saner pricing after the 2022 acquisition ("over priced for a note taking app"). |
| A 32% increase reported by leavers. |
| Less upsell pressure. |
| A free tier big enough for casual use ($242/yr to stay at the "casual user limit" was called too small). |
| A trustworthy archive you own forever. |
| New-app signal: a trustworthy archive priced sanely, with a clipper as good as Evernote's. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Veteran cloud archive. |
| Platform | Now owned by Bending Spoons. |
| Business | 50-note / one-notebook free cap under Bending Spoons. (R8 fact-check against Evernote's help pages) |

Sources: apps-likes-wants.md

## OneNote

**Features**

| Area | Detail |
|---|---|
| Canvas/ink | Freeform infinite canvas: place ink, text, and images anywhere. |
| Canvas/ink | Dump a picture or PDF and scribble over it (free-form overlay). |
| Organization | Notebook/section/page hierarchy. |
| Editing | Typing/drawing anywhere to think non-linearly. |
| Editing | Gathering research material on one page. |
| Search | OCR. |
| Collaboration | Sharing and collaboration. |
| Sync | OneDrive storage requirement. |
| Sync | Sync via Microsoft cloud. |

**Sentiment**

| What people say |
|---|
| The infinite canvas itself is the beloved core: "love Onenote just because of infinite canvas." |
| For many users sync is rock solid, one reason they stay. |
| For others (especially teams) sync is the dominant complaint; the findings hold both. |
| OneNote lets users set pen/touch auto-switching (automatic mode switching setting), which the community cites as the reference behavior other apps lack. (See the dedicated synthesis in Part III and the wish list) |
| Weak mobile apps and no nested folders in sections. |
| Users feel trapped by the format. |
| Stagnation: a user left to try everything else and came back "sick of lack of improvements." |

**Wants**

| What people want changed |
|---|
| Fast, reliable sync (conflict spikes for teams). |
| No data loss or stale versions across cached notebooks. |
| Speed on complex pages. |
| Better mobile apps and nested folders in sections. |
| Resumed development. |
| New-app signal: infinite canvas plus sync you never have to think about. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Windows/web/mobile. |
| Platform | Free with a Microsoft account. |

Sources: apps-likes-wants.md, input-mode-switching.md

## Notion

**Features**

| Area | Detail |
|---|---|
| Editing | Block editor. |
| Editing | Pages in pages. |
| Organization | Relational databases with multiple views. |
| Organization | Templates. |
| Collaboration | Sharing/permissions. |
| Collaboration | API/integrations. |
| AI | Notion AI. |
| Sync | Cloud-first. |
| Sync | Recent per-page offline mode. |

**Sentiment**

| What people say |
|---|
| The all-in-one value: "I don't have to open one app to take a small note and then transfer it into another system". |
| Block structure plus linked databases and filters gives one source of truth with different views. |
| Databases non-technical people can use. |
| Speed complaints are specific and tracked as a worsening trend: large databases and workspaces take seconds to minutes. |
| Offline mode is per-page and manual; the community calls it too little too late. |
| Memory usage is extreme: 2 pages = 1.5GB reported. |
| Workspace chaos: "the tool should not be the work"; hours spent re-organizing. |
| Database-view complaint specifics (from the digests): users want faster view switching and better handling of large databases. |
| Slow database views are the single most-cited technical failure. |

**Wants**

| What people want changed |
|---|
| Speed for large databases and workspaces. |
| A real full offline mode. |
| Data portability (notes are not stored locally; people migrate to Airtable/Obsidian for limits and speed). |
| Less memory usage. |
| Less re-organization overhead. |
| New-app signal: Notion's flexibility with local speed: instant, offline, and yours. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Web/desktop/mobile. |
| Platform | Proprietary. |

Sources: apps-likes-wants.md, community-digest.md, thread3-digest.md

## Obsidian

**Features**

| Area | Detail |
|---|---|
| Editing | Markdown vault on disk (plain local .md files). |
| Editing | MathJax. |
| Editing | Canvas (as .canvas files in the open JSON Canvas format). |
| Organization | Bidirectional links/graph. |
| Organization | ~9,500 community plugins (registry ~9,521 entries, Oct 2026). |
| Organization | Per-vault config that syncs everywhere. |
| Search | Fast local search. |
| Sync | Optional paid Sync (E2E-encrypted). |
| Sync | Fully offline otherwise. |
| Export | Notes are plain local files, no lock-in. |

**Sentiment**

| What people say |
|---|
| Plain local Markdown files are the loyalty anchor: your data is never locked in, change tools without rebuilding. |
| A Reddit straw poll on "if Obsidian went database tomorrow" shows how users reason about it ("Right now there's basically zero chance of the app going south like changing note storage formats"). |
| Fast, offline, great for code+math. |
| File-first costs (from thread-b-storage): metadata beyond note content leaks into JSON sidecar files (.obsidian folder: hotkeys, themes, plugins, workspace.json). |
| Also a hidden metadata cache (IndexedDB). |
| Renaming a note rewrites every file containing a wikilink ("rename fanout"). |
| The canvas is a sibling .canvas file (JSON Canvas, MIT-licensed, spun out March 2024). |
| Canvas positions and edges live in the .canvas file, note content stays in .md files, which is why the canvas-note bridge works live in both directions for free. |
| Community hunger to go beyond .md ("does the use of .md format also doom Obsidian to miss some advanced features? Like a database?"). |
| Security incident: an April 2026 Elastic Security Labs campaign in which malicious community plugins shared inside shared vaults delivered the PhantomPulse RAT, aimed at finance and crypto people via LinkedIn/Telegram. |
| The vector was plugins in shared vaults, not fake app downloads. |
| Security incident: an RCE in a popular plugin (Tasks) where note frontmatter flowed unsanitized into a `new Function()` evaluator (CVSS 8.6, patched May 8, 2026). |
| Running JS in queries is off by default. |

**Wants**

| What people want changed |
|---|
| Sync price (Standard $4/mo billed annually = $48/yr; the $96/yr figure is the Plus tier) feels bad next to free workarounds. |
| No regional pricing or one-time option. (obsidian.md's main pricing page now shows a single $4/mo plan while obsidian.md/sync still lists both tiers) |
| Mobile sync friction with free workarounds. |
| Plugin dependence on volunteer maintainers. |
| New-app signal: local Markdown plus effortless, affordable sync built in. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | App proprietary but free for personal use. |
| Platform | Desktop/mobile. |

Sources: apps-likes-wants.md, thread-b-storage.md, thread-f-editor-platform.md

## Miro

**Features**

| Area | Detail |
|---|---|
| Canvas | Infinite boards. |
| Canvas | Sticky notes. |
| Canvas | Diagrams. |
| Capture | Document/PDF embedding. |
| Capture | Templates. |
| Collaboration | Real-time multiplayer. |
| Collaboration | Integrations (Azure DevOps etc.). |

**Sentiment**

| What people say |
|---|
| Templates plus real-time collaboration for brainstorming and planning. |
| Beloved by agile teams for story mapping, retros, technical mapping. |
| Template breadth (whiteboarding, mockups, roadmaps, process flows). |
| Performance/lag on large or even modest boards, worsening over years ("boards are way laggier and take far longer to load"). |
| Lag specifically after inserting documents/PDFs. |
| Paid limits and unexpected deletions noted on Trustpilot. |

**Wants**

| What people want changed |
|---|
| A whiteboard that stays fast as the board grows. |
| Fix lag after inserting documents/PDFs. |
| Stop UI regressions and unresponsive controls. |
| Saner paid limits. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Business | Paid tiers with board caps. |

Sources: apps-likes-wants.md

## Milanote

**Features**

| Area | Detail |
|---|---|
| Canvas | Drag-and-drop cards on boards. |
| Canvas | Columns. |
| Canvas | Templates. |
| Capture | Image/file support. |
| Collaboration | Sharing/collaboration. |

**Sentiment**

| What people say |
|---|
| Visual clarity for brainstorming and organizing: "by far my favorite tool for taking notes and saving ideas". |
| The freeform canvas feels like a wall of sticky notes. |
| Desktop boards described as amazing even by critics. |
| Mobile app nearly unusable: can't even add boards. |
| Boards degrade with many cards. |
| No edit history. |
| Export is per-board PDF/PNG/doc only. |
| A formal request exists on their own roadmap poll to "Export your data in a proprietary Milanote format" (i.e., even a full proprietary dump is wanted and not shipped). |
| Users complain "No Easy Export / Backup?". |
| The 100-note limit drove users to build alternatives. |

**Wants**

| What people want changed |
|---|
| Usable mobile app. |
| Fair pricing/bigger free tier. |
| Edit history. |
| Full export/backup. |
| Boards that scale. |
| New-app signal: visual boards that work on every device at a fair price. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Business | 100-note free cap; ~$100/yr. |

Sources: apps-likes-wants.md, thread-b-storage.md

## Anytype

**Features**

| Area | Detail |
|---|---|
| Editing/organization | Objects/sets/collections instead of pages. |
| Editing/organization | Graph + relations. |
| Sync | Local storage with P2P/local network sync. |
| Sync | Self-hostable backup nodes. |
| Sync | Offline-first. |
| Security | E2E encryption with user-held keys. |
| Security | Keys generated locally; server never decrypts data. |
| Security | No account required. |
| Export | Markdown export (improved in 0.47.4, July 2025, to support properties and types). |

**Sentiment**

| What people say |
|---|
| Privacy model is the draw: "I love that it's local first... encrypted... powerful. Never had an issue with data loss". |
| Fast pages even with hundreds of items. |
| Storage reality (thread-b-storage): the vault is opaque encrypted blobs + index folders; "Files are stored inside flatfs dir in encrypted fragments, so they can't be accessed outside of Anytype". |
| Media streamed on demand and deduplicated. |
| Local-first does not mean plain files. |
| Export is the pressure valve and has repeatedly disappointed: a 2024 thread "Export is not great" reports Markdown export dropping everything but names. |
| A 2025 thread says property-rich data makes "the markdown export useless" and "your data will be encrypted and usable only with proprietary Anytype." |
| Release 0.47.4 improved this. |
| A co-founder pushed back on the lock-in charge on the community forum. |
| Takeaway recorded in the findings: an object/block store with strong encryption makes a faithful plain-file projection genuinely hard. |
| Anytype's answer has been improving one-way export, not a mirror. |

**Wants**

| What people want changed |
|---|
| Reliable desktop-mobile sync (desktop-mobile sync barely happening, slow sync, synced-flagged items actually unsynced). |
| Mobile app quality catching up to desktop. |
| Transparent file storage on disk (no plain-file layout like Obsidian's). |
| Notion-grade database features (formulas). |
| A third-party security audit. |
| Analytics concerns addressed. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Source-available (custom "Any Source Available" license; repos at github.com/anyproto; client code public, not OSI-approved). |
| Platform | Desktop/mobile. |

Sources: apps-likes-wants.md, thread-b-storage.md

## Tana

**Features**

| Area | Detail |
|---|---|
| Editing | Nested outline built around a daily "dashboards" note. |
| Organization | Supertags with field/inheritance schema (schema-driven tags). |
| Organization | Queryable graph. |
| AI | AI command bar/agents. |
| Capture | Web clipper. |
| Sync | Proprietary cloud database. |
| Export | JSON export (full, with Tana-specific structures). |
| Export | Markdown export (first version arrived 2025, subset-by-supertag, with/without fields). |

**Sentiment**

| What people say |
|---|
| Supertags "genuinely different from every other tagging or database system". |
| Users miss them in other apps. |
| The outliner model lets you capture everything, tag it, resurface on the day page. |
| "there really isn't anything to replace Tana" for bullet notes. |
| Learning curve: "as hard as learning a programming language". |
| Hours to learn; a survivors-only bias noted in reviews. |
| Storage (thread-b-storage): vendor lock-in is explicit, "Your data lives in Tana's proprietary format". |
| A 2023 user: JSON export "is a bit limited" unless you know what to do with it. |
| Community tooling (TanaMigrator) converts the JSON workspace export into a vault of markdown files. |
| TanaMigrator's author warns "VERY good chance edge cases exist." |
| Performance degrades as the workspace grows. |

**Wants**

| What people want changed |
|---|
| Learnable-in-minutes structure instead of days. |
| A mobile app not too limited for real workspace use. |
| Performance at scale. |
| A free tier thick enough to evaluate. |
| Less perceived AI push. |
| New-app signal: supertag-like structure learnable in minutes. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Business | Free / Pro $20/mo early-bird ($30 regular) / Business from $35/mo. (tana.inc, R8 fact-check) |
| Business | The older $10-18 tiers are gone. (R8 fact-check (tana.inc)) |
| Business | The separate Tana Outliner product lists Plus $8/mo. |

Sources: apps-likes-wants.md, thread-b-storage.md

## Reflect

**Features**

| Area | Detail |
|---|---|
| Editing | Daily notes flow. |
| Editing | Backlinks/graph. |
| AI | GPT-based AI assistants. |
| AI | Voice transcription. |
| Capture | Web clipper. |
| Capture | Calendar integration. |
| Sync | E2E-encrypted cloud sync. |
| Export | Reflect JSON, CSV, markdown zip, HTML zip. |
| Export | Daily backups to the hard drive. |

**Sentiment**

| What people say |
|---|
| The daily-note workflow "gets a lot of love... calming; you don't have to think about where something belongs". |
| Polish praised ("easy to use and the performance is phenomenal"). |
| Does fewer things very well. |
| Seamless for journaling. |
| Storage story (thread-b-storage): Classic exports are a copy, not a mirror; one user complained you "can only export all your notes in one go". |
| The notable 2026 move is a cloud block-ish app adding a plain-file sibling product (Reflect Open: "Your choice of sync: iCloud Drive or Git") rather than a mirror of the existing one. |

**Wants**

| What people want changed |
|---|
| Lower price ("$10/month is steep"; alternatives undercut it). |
| Fix occasional sync delays. |
| Better attachment management ("sucks"). |
| A real Android experience. |
| Database/table features Notion users expect. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Business | ~$10/mo, no real free tier. |
| Platform | 2026 split: Reflect Open (open-source, local Markdown files, choice of iCloud Drive or Git sync) added alongside maintained Reflect Classic. |

Sources: apps-likes-wants.md, thread-b-storage.md

## Logseq

**Features**

| Area | Detail |
|---|---|
| Editing | Block-level outliner (every line is a block: bullet, indentable, referenceable, embeddable). |
| Editing | Block references and embeds. |
| Editing | Drag-anywhere blocks. |
| Organization | Tasks. |
| Organization | Queries (Datalog). |
| Organization | Graph links. |
| Organization | Whiteboards. |
| Extensibility | Plugins. |
| Sync | Optional paid sync. |
| Sync | Local Markdown/org files as the store. |
| New DB version | A database (SQLite) version to fix performance. (Announced April 2024, DB beta shipped July 13, 2026) |

**Sentiment**

| What people say |
|---|
| The block outliner is the loved model: everything has hierarchy, so retrieval pulls whole trees ("far more powerful and intuitive than Obsidian"). |
| Users love the Logseq way even while criticising the app. |
| Performance collapses on large graphs (1000+ pages), the app's defining complaint. |
| Sync data loss/duplication; fragile two-way sync. |
| A file-writing defect produced unrecoverable data loss (in-app edits never written to ./pages/*.md). |
| The encoding cost (thread-b-storage): "Logseq uses Markdown syntax but not every Markdown file is a valid Logseq page, basically because of dashes". |
| Logseq began inserting hyphens on every line, "breaking MD functionality" (issue #3457, a 2020 Markdown hyphen bug). |
| Users want "normal markdown files that I can take with me anywhere." |
| Logseq's own April 2024 post explains the pivot to a database version: "Creating a new block requires rewriting the entire Markdown file"; "Renaming a page updates all files that reference it"; "structure data support is limited... lacking features like persistent IDs, timestamps". |
| The DB version's goals include Datalog queries, offline-first RTC with E2EE, and a long-term goal of "seamless two-way sync between the database and markdown files", still aspirational two years later. |
| OG is maintenance-only without reaching 1.0 (the OG/DB split took effect April 24, 2026). |
| "enable hourly backups to the filesystem" is community advice for DB users rather than official documentation. (UNVERIFIED as official guidance in the R8 fact-check) |
| The file plane is a backup/export surface, not the store. |
| The findings call Logseq the strongest evidence that the file mirror is a goal even the team that wants it has not shipped. |

**Wants**

| What people want changed |
|---|
| Performance that survives 1000+ pages. |
| Sync without data loss or duplication. |
| Faster development and a finished mobile/sync. |
| Clarity on the DB version's trade-offs (SQLite portability, markdown export losing properties worry users). |
| New-app signal: Logseq's outliner power without the performance ceiling, on plain files. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Open-source, AGPL-3.0. |
| Platform | Desktop/mobile. |

Sources: apps-likes-wants.md, thread-b-storage.md

## Tolaria

**Features**

| Area | Detail |
|---|---|
| Editing | Notion-like WYSIWYG block editor (BlockNote/Tiptap) + raw Markdown mode (Cmd+/). |
| Editing | Slash commands. |
| Editing | [[wikilinks]] with autocomplete and auto-update on rename. |
| Editing | Mermaid diagrams. |
| Editing | KaTeX math with editable source panel. |
| Editing | Code blocks with syntax highlighting. |
| Editing | Editable callouts. |
| Editing | Sandboxed HTML blocks. |
| Editing | Colored highlights. |
| Editing | Todo block shortcut. |
| Editing | Collapsible headings. |
| Editing | Table navigation. |
| Capture | Inbox section (unorganized notes, Forte-style capture-vs-organize, disableable). |
| Capture | Note list sortable by any property or file metadata with customizable property columns. |
| Capture | cmd+click to open URL/note links. |
| Canvas | tldraw whiteboards stored as markdown files. |
| Rich content | Media/PDF previews (PDF.js), lightbox. |
| Rich content | Spreadsheet notes (plain-text sheets with formulas via IronCalc WASM). |
| Attachments | Drag-and-drop from Finder. |
| Attachments | Clipboard paste. |
| Attachments | Remote image paste. |
| Attachments | Vault-root or note-relative paths. |
| Organization | Types as lenses, not schemas: every note has a type (default Note). |
| Organization | Types are themselves markdown files with icon/color, no required fields or validation. |
| Organization | Sidebar sections (Inbox, All notes, Archive, types, Pinned/favorites, custom views, folder tree at the bottom). |
| Organization | Custom views are YAML files in a views/ folder with nested filter criteria, regexes and natural-language dates, and AI can author them. |
| Search | Command palette (Cmd+K) with semantic matching. |
| Search | Keyboard-first design. |
| Search | Quick open with create-note-from-search. |
| Search | Note body full-text search. |
| AI | Direct model providers (OpenAI, Anthropic, Gemini, OpenRouter, Ollama, LM Studio, custom OpenAI-compatible endpoints) for chat over note context. |
| AI | CLI agent targets (Claude Code, Codex, OpenCode, Pi, Gemini, Copilot CLI, Kiro, Antigravity, Hermes). |
| AI | Dedicated AI side workspace. |
| AI | AI commit-message drafting. |
| AI | AI can create notes. |
| Integration | Bundled MCP server (Node or Bun) exposing vault tools (create/update/append notes, vault lifecycle). |
| Integration | AGENTS file ships for external agents to self-orient. |
| Integration | Claude Code skills usable from the AI panel. |
| Integration | Per-agent model picker. |
| Integration | Local API keys. |
| Sync | Git is the sync layer: in-app commit, push, browse history, per-note version history. |
| Sync | AutoGit opt-in mode auto-commits/pushes when idle or on focus shift. |
| Sync | Mobile syncs via iCloud or Files app sharing the same git repository, auto-commit on save with merge support. |
| Multi-vault | Multiple vaults, separate app windows per vault, mounted vault workspaces, custom vault order, parent Git repository support, vault deep links. |
| Export | PDF export. |
| Export | Standalone HTML previews. |

**Sentiment**

| What people say |
|---|
| Files-first vault: notes are plain .md with YAML frontmatter, no database, no proprietary format. |
| Folders are secondary; flat-vault friendly. |
| Origin: the author migrated 10,000+ notes from Notion to plain Markdown and built the app he wanted. |
| Mostly AI-written code (~zero lines written by the author himself); 1900+ commits, 3000+ tests, 70 ADRs. |
| Git-first as AI transparency is a loved feature: seeing exactly what the AI changed vs what you wrote, with AI as a git contributor. |
| No trash bin; git history is the safety net (a deliberate deletion model). |
| AI chats are not persisted in vault files by default. |
| Loved: UI polish with real files underneath; the inbox concept; clipboard image paste praised as rare and essential. |
| Open source vs Obsidian ("I had no idea Obsidian wasn't open source"; lock-in freedom is the differentiator). |
| Emerging (alpha, Oct 2026): what shipped in October 2026 was the iPhone/iPad client. |
| A web client is announced as an in-development beta with alpha CI only. (R8 fact-check correction: the earlier note said the web client had shipped) |
| The remote-client direction (sharing notes/vaults with view-only/revoke, signed access tickets) is still worth watching, though desktop remains git/no-server. |
| The findings' pull-from assessment: liftable concepts include types-as-lenses, views-as-YAML with natural-language dates, Inbox lifecycle, AutoGit idle/focus heuristics, wikilinks auto-updating on rename, AGENTS-file convention, bundled MCP vault tools, no-trash git-as-safety-net model. |
| Code lifting is binding: AGPL-3.0. |
| Not worth copying: the React/BlockNote editor layer (the project's own weak point per HN bug reports). |
| Known bugs to avoid repeating: "last modified" sorting breaks after first git commit (sorts by commit date). |
| Known bugs to avoid repeating: code fence requires a space; ctrl-e end-of-line missing; cursor jumps below block after fence creation. |

**Wants**

| What people want changed |
|---|
| A truly native (AppKit/SwiftUI) app rather than a Tauri/React web-wrapper. |
| Feature-creep worry ("stay focused like Bear"). |
| Early-bug fixes (blank frozen app; three bugs in five minutes; sort-by-modified issue). |
| Editor friction fixes. |
| "AI-first" wording read as humans second-class. |
| Large-file editor performance. |
| npm-dependency-in-adjacent-to-home trust concern. |
| Mobile demand (largely since addressed). |
| A way to donate/pay at launch. |
| Answers to single-maintainer longevity skepticism. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | macOS, Windows, Linux desktop (Homebrew cask + signed installers). |
| Platform | iOS/iPadOS beta via TestFlight. |
| Platform | An iPhone/iPad client shipped October 2026. |
| Platform | ~52.6K lines of Rust plus ~53K lines of TypeScript/TSX (repo count, Oct 2026), Tauri v2. |
| Platform | AGPL-3.0-or-later; free and open source forever, no accounts or subscriptions. |

Sources: tolaria.md

## AFFiNE

**Features**

| Area | Detail |
|---|---|
| Editing/organization | "everything is a block, something that could be edited and transformed freely". |
| Editing/organization | Doc + whiteboard + databases as views of one underlying store. |
| Editing/organization | Edgeless (canvas) mode. |
| Storage | BlockSuite documents are a block tree "structured as a tree and stored within a Y.Map" (CRDT), with `sys:id`, `sys:flavour`, `sys:children`. |
| Storage | Persistent block IDs and parent/child structure with no file concept anywhere. |
| Canvas | Edgeless documents are isomorphic to page documents: both are block trees, with no data conversion during mode switching. |
| Canvas | A `surface` block holds all whiteboard elements. |
| Canvas | "a Page is a type of Database, as is Edgeless." |
| Sync | Local IndexedDB/SQLite per platform plus sync servers. |
| Performance | Claims to render thousands of vector shapes and text blocks at 60 FPS without DOM-heavy lag. |

**Sentiment**

| What people say |
|---|
| BlockSuite is the one editor core built for the canvas-plus-document hybrid: PageEditor and EdgelessEditor are two views that attach and detach from the same Y.Doc. |
| Costs recorded: much smaller ecosystem than ProseMirror/TipTap/Lexical. |
| The framework is young, API churn is real. |
| Teams adopting it inherit AFFiNE's product opinions. |
| DeepWiki's architecture notes describe a store-to-model-to-view data flow closer to a game engine than an editor library. |
| No plain-file story of the Thymer kind exists in BlockSuite. (Docs do not mention one; UNVERIFIED beyond docs read) |
| Edgeless + page as two views of one store is also the control case in the editor-core comparison: "the only core where the brief's requirement is the default behavior." |

**Wants**

| What people want changed |
|---|
| Not recorded in the findings beyond the ecosystem/API-stability cost framing; the findings treat AFFiNE primarily as architecture evidence. |

Sources: thread-b-storage.md, thread-f-editor-platform.md

---

# PART II: OPEN-SOURCE REPOS

(Repo sections merge the deep-repos, github-repos and linked-apps findings. Where the findings recorded only repo-level feature lists without user sentiment, the Wants row reflects that.)

## CapsuleCraft (kostyk348/CapsuleCraft, a.k.a. capsuleos)

**Features**

| Area | Detail |
|---|---|
| Capture/editing | Block editor (headings, paragraphs, task lists, callouts, code blocks, CSV datagrids, audio-attachment notes) with autosave, undo/redo and `.eml` round-trip. |
| Capture/editing | `[[wiki links]]` with a live backlink index. |
| Capture/editing | Renaming rewrites all links. |
| Organization/search | Okapi BM25 full-vault search with Cyrillic-aware folding. |
| Organization/search | Plus a "related by meaning" tf-idf cosine ranking. |
| Organization/search | Tags stored in message headers. |
| Planning | Tasks aggregated to Agenda / Kanban / Gantt views with dependency arrows and cycle protection. |
| Planning | RFC 5545 ICS export. |
| Threading | Real email threading, replies are child .eml files via In-Reply-To/References. |
| Threading | Datasets travel as MIME parts addressed by Content-ID. |
| Import/integration | Drag-drop .eml import, IMAP, Obsidian vault migration (`--import-obsidian`). |
| Import/integration | Bundled MCP server exposing the vault to AI agents. |
| Import/integration | Offline deterministic "Co-Thinker" critique engine with no API keys. |

**Sentiment**

| What people say |
|---|
| The "capsule" is a multipart MIME message: headers carry tags (X-Capsule-Tags), a `blocks.json` JSON part is the structured block canvas, extra MIME parts are datasets/attachments addressed by Content-ID, and threading rides standard mail headers. |
| A proof that a plain open-standard format can still host a block model. |
| Renamed from capsuleos at v1.5.0. |
| v1.0.0 shipped 2026-08-16 and v1.7.0 on 2026-10-25 (monthly-plus iteration). |
| An honest LIMITATIONS.md lists gaps: no code execution or audio in the native shell yet, best-effort folder watching, capsules not GPG-encrypted. |
| The roadmap already names GPG-encrypted capsules and optional end-to-end-encrypted vault sync ("tamper/censor-proof, still zero-cloud"). |
| Independent evidence that E2EE sync is the next expected feature in this category. |

**Wants**

| What people want changed |
|---|
| No user sentiment recorded; visible direction comes from the roadmap (encryption, E2EE sync, audio in the native shell). |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Native Rust + egui shell with no webview (~11 MB AppImage, glibc-only). |
| Platform | Legacy Tauri/web builds also published. |
| Platform | MIT license. |
| Platform | 98 Rust unit tests in the native shell plus 151 Vitest tests in the legacy web engine. |

Sources: deep-repos-c.md, github-repos-2.md

## Meridian-Notes (realbyln/Meridian-Notes)

**Features**

| Area | Detail |
|---|---|
| Editor | Rope-based buffer, multiple cursors, macros (record/play/save), split views, vim mode, spell check, lint, git gutter, syntax highlighting, focus mode, typewriter scrolling, time-travel history scrubber. |
| Notes | `[[links]]`. |
| Notes | Scrollable/collapsible `{{embeds}}`. |
| Notes | Backlinks sidebar. |
| Notes | Hover preview. |
| Notes | Goto-anything. |
| Notes | Templates. |
| Notes | Plain Markdown files readable in any other editor. |
| Canvas/views | An "Endless canvas" where notes with a layout file open as free-positioned text boxes. |
| Canvas/views | Graph view. |
| Canvas/views | Pen ink on the canvas and inside Markdown notes, saved as SVG. |
| Canvas/views | Touch gestures. |
| Study | Cloze cards (`{{c1::text}}`). |
| Study | Card review. |
| Study | Quizzes. |
| Study | Anki import/export (TSV, APKG). |
| Study | Exam forecast. |
| Extensibility | Out-of-process plugins on a stable protocol (panels, commands, key bindings). |
| Extensibility | Rebindable keys via keys.conf. |
| Extensibility | Skins with hot reload where every color is a role. |

**Sentiment**

| What people say |
|---|
| Ink saved as SVG inside a Markdown note is a clean file-format answer for pen input. |
| The "layout file turns a note into free-positioned canvas boxes" pattern is a lightweight alternative to full canvas documents. |
| Out-of-process plugins avoid embedding a scripting runtime. |
| Early and tiny (v0.2, 3 stars, test releases described as "early, unsigned, may crash, lose data"), which its own findings read as the cost of building a custom GUI toolkit. |

**Wants**

| What people want changed |
|---|
| Nothing recorded beyond the project's own early-stage warnings. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Rust with its own GUI toolkit (self-drawn title bar, ribbon, menus, command palette, dialogs: no webview, no terminal). |
| Platform | Wayland stylus support. |
| Platform | MIT license. |

Sources: deep-repos-c.md, github-repos-2.md

## notecraft (AlienTechSoftware/notecraft)

**Features**

| Area | Detail |
|---|---|
| Storage | Privacy-first, local-first storage on device. |
| Account | No cloud account required. |
| Editing | Markdown-centric notes. |

**Sentiment**

| What people say |
|---|
| Dual-licensed MIT OR Apache-2.0, so the architecture (Rust core + separate UI layer, storage layout, local-first sync decisions) is copy-paste friendly. |
| At this maturity it is a design comparison point rather than a usable product. |

**Wants**

| What people want changed |
|---|
| One visible request: open issue #8 on stylus/palm-rejection input behavior on Linux, opened 2026-10-25. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Cross-platform desktop targets. |
| Platform | A Rust core with the UI layer split on top. |
| Platform | Alpha scope is narrow (0.0.6, no published release). |

Sources: deep-repos-a.md, github-repos-1.md

## e-journal (EkarinLB/e-journal)

**Features**

| Area | Detail |
|---|---|
| Storage | Encrypted local journal storage. |
| Journaling | Daily entries with calendar/date navigation. |
| Journaling | Mood tracking. |
| Organization | Tagging. |
| AI | AI-generated summaries of entries using a local model. |
| Export | Markdown export. |

**Sentiment**

| What people say |
|---|
| MIT-licensed and in the same product family as a Rust-first notes app, so the entry-storage schema, calendar navigation, encryption-at-rest approach and export path are directly liftable. |
| Twelve beta point-versions shipped by 0.12.0. |

**Wants**

| What people want changed |
|---|
| Nothing recorded beyond the maintainer's own iteration. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Local-first, AI-powered journaling desktop app in Rust with the egui/eframe toolkit. |
| Platform | Dark/light theming. |
| Platform | Ships as a single binary. |

Sources: deep-repos-a.md, github-repos-1.md

## neo (hughhowey/neo)

**Features**

| Area | Detail |
|---|---|
| Library | Rendered as a bookshelf with labeled shelves, drag-and-drop, cover art and progress bars tied to word goals. |
| Writing | Manuscript pages look like books: automatic chapter renumbering, drop caps, curly-quote/em-dash/ellipsis auto-correction, spellcheck only on demand. |
| Writing | Keyboard-driven flow (one Enter = paragraph, two = `***` section break, three = new chapter). |
| Revision | A "Darlings" tab that parks cut passages and restores them to the exact original spot. |
| Revision | A placeholder hotkey drops a mark + sticky note mid-flow, collected into a to-do panel. |
| Outline | The book shown as index cards. |
| Outline | A card's note appears in the manuscript as a gray ghost paragraph that follows the writing until dismissed. |
| Outline | Dragging a card moves the text. |

**Sentiment**

| What people say |
|---|
| The index-card outline to document two-way binding is a small canvas-adjacent pattern worth studying. |
| Metadata (progress, goals, outline cards) is layered over plain text without a database. |
| Opinionated vertical UX (built by a novelist for novelists) sustains loyal local-first users. |

**Wants**

| What people want changed |
|---|
| Nothing recorded in the findings. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Free and open source (MIT per the README), no accounts or subscriptions. (R8 fact-check corrected an earlier claim that neo was not open source) |
| Platform | Plain files on disk. |
| Platform | Installers for macOS (Intel + arm64), Windows (self-updating) and Linux (AppImage). |

Sources: deep-repos-b.md, github-repos-2.md

## notebook-navigator (johansan/notebook-navigator)

**Features**

| Area | Detail |
|---|---|
| Scope | Obsidian community plugin replacing the file browser and calendar. |
| Explorer | A virtualized two-pane explorer (folder tree + file list) with visual previews, built for very large vaults (100k+ notes target) using TanStack Virtual. |
| Organization | Smart folders. |
| Organization | Recent-notes view. |
| Organization | AI-style filter search with a filter-search grammar. |
| Organization | Frontmatter keyword (tag) discovery with included/excluded lists. |
| Organization | Tag and marker discovery with per-tag/folder icons and colors. |
| Organization | Calendar navigation. |
| Organization | Per-folder icons and colors. |
| Organization | Folder notes. |
| Organization | Manual sort mode with keyboard reordering. |
| Keyboard | Full keyboard navigation (all shortcuts remappable, VIM-style keys). |
| Docs | A documented settings surface (14 sections). |
| Storage | Storage across IndexedDB, Local Storage and an in-memory cache. |
| Storage | Per-setting "sync" toggles deciding whether a setting is stored locally or shared across devices. |
| Privacy | A documented network/diagnostics disclosure listing every HTTP request the plugin makes. |

**Sentiment**

| What people say |
|---|
| 2,782 stars / 104 forks / 1,072,639 downloads per obsidianstats (5.0 rating). |
| Reddit/forum word of mouth calling it a real replacement for the default file browser. |
| A case study reports 180 releases and ~zero hand-written LOC (AI-assisted development). |
| The docs are a blueprint in themselves: a startup/boot process doc (cold vs warm boot, metadata cache), a metadata pipeline doc (cache rebuild, provider stages) and a storage architecture doc (which store holds what). |
| Its switching guides for Evernote, Apple Notes, Bear, OneNote and Day One map where users actually migrate from. |

**Wants**

| What people want changed |
|---|
| No open issues surfaced; the author explicitly does not accept PRs ("no PRs will be accepted") and funnels feature direction into the 1.5 roadmap issue #274. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Mobile-optimized. |

Sources: deep-repos-b.md, github-repos-2.md

## opensidian

Two unrelated projects share the name; the findings cover both.

**Features**

| Area | Detail |
|---|---|
| Positioning | (jpzk/opensidian, the primary subject) "Open-source and non-profit under GPLv3, vault-compatible cross-platform markdown notes app"; privacy-first knowledge management positioning. |
| Positioning | Explicitly a clean-room functional clone of Obsidian (reimplemented from the outside, contains none of its code, not affiliated with Obsidian/Dynalist). |
| Editing | Obsidian-vault-compatible Markdown notes. |
| Second project | (thiagovasconcelosti/opensidian, MIT, separate codebase) Node.js/Express + React 18/Vite. |
| Second project | D3 force-simulation knowledge graph. |
| Second project | WebSocket real-time sync. |
| Second project | JWT auth. |
| Second project | Multiple vaults. |
| Second project | Markdown editor with live preview and `[[wikilinks]]`. |
| Second project | Themes with a visual editor. |
| Second project | A hook-based plugin API (`note:pre-save`, `note:post-save`, command registration). |
| Second project | A full REST API (vaults, notes CRUD, graph neighbors, ranked full-text search with tag/date/backlink filters). |
| Second project | An MCP server so AI tools can read the vault. |
| Second project | Docker deployment. |
| Second project | Vitest (79 tests, >80% coverage). |

**Sentiment**

| What people say |
|---|
| jpzk/opensidian is the closest live reference implementation of an "Obsidian clone in Rust + Tauri" and doubles as a distribution checklist (AppImage variants, flatpak, rpm/deb, nix, GPG-signed checksums). |
| Its WebKitGTK dependency pain is an argument for a native GUI shell. |
| Two more independent projects adding MCP servers to notes vaults (this one and Tolaria) mark AI-agent vault access as a standard expectation. |
| Clean-room cloning is a legal pattern worth remembering; the name collision is a naming risk. |

**Wants**

| What people want changed |
|---|
| Nothing recorded beyond maintainer roadmap items (jpzk) and the projects' own docs. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Rust + Tauri v2 (WebKitGTK 4.1 webview on Linux). |
| Platform | v0.8.1 with fresh-install tests on Fedora 44 and Ubuntu 26.04 LTS dated 2026-10-25. |
| Linux packaging | Slim AppImage. |
| Linux packaging | Portable AppImage (WebKit bundled). |
| Linux packaging | Flatpak (GNOME runtime). |
| Linux packaging | RPM. |
| Linux packaging | DEB. |
| Linux packaging | Nix. |
| Linux packaging | Reproducibility hygiene: SHA256SUMS signed with a published GPG key, locked cargo builds (`--locked`). |
| Linux packaging | Recruiting Linux distribution maintainers. |

Sources: deep-repos-c.md, github-repos-2.md

## Strata (Niko1221/Strata)

**Features**

| Area | Detail |
|---|---|
| Core | A local LLM inference engine that runs models on the user's own machine. |
| Install | One-click installer. |
| Models | Automatic engine/model selection for the user's hardware. |
| Models | GPU offload with CPU fallback. |
| API | OpenAI-compatible and Anthropic-compatible localhost API endpoints so existing agents and tools can point at local models. |
| API | A `strata connect` flow that configures those agents. |
| Benchmark | Built-in benchmark suite. |
| Image generation | Via a Stable Diffusion CLI companion (`sd-cli`). |

**Sentiment**

| What people say |
|---|
| The localhost server speaking OpenAI/Anthropic wire formats is the pragmatic route for private AI features in a notes app (works against any local or remote model). |
| The "auto-pick engine for this hardware" UX and the benchmark-harness discipline (reproducible local benchmarks shipped with the app) both transfer. |
| The issue tracker is the busy part: 439 open issues across labels [TUI], [GUI], [Engine], [Benchmark], [Other], active as recently as 2026-10-26. |
| Community members posting their own benchmark runs on consumer RTX hardware. |

**Wants**

| What people want changed |
|---|
| Nothing recorded at feature level beyond the labeled issue surface above. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Desktop app plus terminal client. |
| License | MIT. |

Sources: deep-repos-a.md, github-repos-1.md

## xnotes-android (shardulvs/xnotes-android)

**Features**

| Area | Detail |
|---|---|
| Ink | A custom native stroke engine (Kotlin + Jetpack Compose UI, NDK 27 + CMake core) turning raw stylus samples into a variable-width ribbon that swells and tapers with pressure. |
| Ink | Pens and highlighters, neon glow, disappearing ink. |
| Ink | Shape snapping (draw rough, hold, it snaps clean). |
| Ink | Crisp at any zoom. |
| Ink | Ink never flattened ("every stroke can be moved, restyled or erased later"). |
| Structure | Notebooks AND an infinite canvas ("pages when you want structure, endless space when you don't"). |
| Structure | Book layouts (single/double/cover, scroll or page-flip). |
| Structure | 20+ page templates (Cornell, planners, music staves, isometric). |
| Structure | 20+ themes; dark/OLED modes. |
| PDF | Import with margin widening for side notes. |
| PDF | Text markups. |
| PDF | Per-PDF color filters that keep photos true-color. |
| PDF | Real PDF export (vector, selectable text, links, bookmarks). |
| Text/media | Markdown with live formatting. |
| Text/media | Typed notes with tables, LaTeX, code highlighting. |
| Text/media | Audio recording that replays ink in sync with the lecture. |
| Shell | Customizable/floating/dockable toolbar. |
| Shell | Split view. |
| Shell | A real file explorer with grid/gallery/list/column/timeline views. |

**Sentiment**

| What people say |
|---|
| The storage stance is the positioning itself: "notes are saved as files in a folder you choose, not locked away in an app's database". |
| "open source, no account, no ads, no tracking, no internet access." |
| Distribution: GitHub Releases and F-Droid ship the same signed APK, so users can switch channels without reinstalling. |
| The Google Play build is a separate channel with a signing conflict (issue #166). (R8 fact-check corrected an earlier same-APK-on-all-three reading) |
| 269 stars, 33 forks, v0.8.23, README updated 2026-10-11. |
| The "notebooks or infinite canvas" duality is the same docs-vs-canvas tension AFFiNE solves with one block model. |

**Wants**

| What people want changed |
|---|
| Nothing recorded beyond the project's own roadmap; the feature set itself is the community demand signal (file-based storage, PDF interop both ways, editable ink, ink synced to audio, templates). |

**Pricing and platforms**

| Item | Detail |
|---|---|
| License | MIT. |

Sources: deep-repos-c.md, github-repos-2.md

## diktafon (Lukas-Novak/diktafon)

**Features**

| Area | Detail |
|---|---|
| Fork | A fork of jaromiru/diktafon: an open-source voice-memo app organized like cassette tapes, transcribing and summarizing entirely on-device. |
| Fork | The fork adds opt-in cloud backup and opt-in cloud transcription to your own server, both off by default. |
| Tape metaphor | Cassettes as continuous gapless recordings. |
| Tape metaphor | Tap-to-seek transcripts. |
| AI | On-device Whisper transcription and Qwen summaries (vendored whisper.cpp + llama.cpp). |
| AI | Silero VAD noise-aware transcription with a rumble filter. |
| AI | Auto language detection per memo. |
| AI | Per-memo and per-cassette summaries/titles. |
| Data | Export/import archives. |
| Data | Opt-in self-hosted sync with durable retry. |

**Sentiment**

| What people say |
|---|
| A case study in consent-first cloud: everything local by default, cloud strictly opt-in, per-consent fallback after failed local attempts. |
| The "your own server + durable retry" ingest model maps well onto optional E2EE sync. |
| Upstream credit reads "designed by Jaromír Janisch, implemented by Claude Code." |

**Wants**

| What people want changed |
|---|
| Nothing recorded beyond the fork's own additions (cloud backup/transcription were built as the answer to that gap). |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Flutter (Android, iOS, Linux). |
| License | MIT. |
| Platform | Released on F-Droid, Google Play and the App Store with SHA256SUMS and GitHub build-provenance attestations. |

Sources: github-repos-1.md

## marmalade-tts-android (maxwhipw/marmalade-tts-android)

**Features**

| Area | Detail |
|---|---|
| Core | A native Android text-to-speech app with on-device neural voices and emotion-aware prosody. |
| Integration | Implementing Android's standard TTS engine interface so it is a system-wide drop-in replacement for Google/Samsung TTS. |
| Engines | Kokoro engine. |
| Engines | A fast English "Kitten Nano" voice bundled in the APK. |
| Engines | Bigger engines download on demand from pinned hostnames into app-private storage. |
| Cloud | Cloud voices strictly opt-in with the user's own API key (Venice.ai, OpenAI), documented in PRIVACY.md. |
| Personalization | Per-app voice routing via aliases (each app gets its own voice/speed/effects). |
| Personalization | 8 languages with auto-detection. |
| Personalization | 22 voice-effect presets plus an editor. |
| Accessibility | TalkBack/WCAG 2.1 AA support. |
| Playback | Foreground playback service with lock-screen/Bluetooth controls. |
| Integration | Share-sheet and "read selection" integration. |

**Sentiment**

| What people say |
|---|
| Its value to a notes project is the privacy-engineering pattern: on-device AI/audio as a headline feature with opt-in cloud as a clearly fenced exception, and download-on-demand models from pinned hosts. |
| The right pattern if the app ever ships local speech features (voice notes, reading notes aloud). |

**Wants**

| What people want changed |
|---|
| Nothing recorded in the findings. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Licensing | Source is MIT but the released APK compiles in espeak-ng (GPL-3.0-or-later), making the APK a GPL-3.0 combined work. |
| Licensing | A deliberate licensing structure to satisfy Google Play's no-runtime-code-download rule. |
| Platform | Distributed via F-Droid (reproducible builds), GitHub Releases (fdroid-flavor APK) and Obtainium. |

Sources: github-repos-2.md

## ConvertOneNote2MarkDown (theohbrothers/ConvertOneNote2MarkDown)

**Features**

| Area | Detail |
|---|---|
| Core | Converts OneNote notebooks to Markdown (via pandoc) with media extracted. |
| Fork | A hardened fork of SjoerdV/ConvertOneNote2MarkDown. |
| Implementation | PowerShell main script (~1,474 lines) driving the OneNote COM API and pandoc. |
| Implementation | docx files as the intermediate representation (naming by page ID or hierarchy). |
| Config | config.example.ps1 for saved configurations including a dry-run mode. |
| Release | CI releases (v2.23.1 latest). |
| Adoption | 766 stars, 84 forks, issues still active through 2026-10. |

**Sentiment**

| What people say |
|---|
| The known failure modes are the migration map: COM automation requires matching admin elevation (OneNote and the terminal both as admin or conversion fails, issue #123). |
| COM class factory errors (#102). |
| Trailing periods in page titles break PowerShell 5 conversions (#197). |
| Hand-written ink is the hard part: OneNote exports each ink stroke as a separate image without position. |
| An October 2026 issue (#200) requests merging strokes into a single image, noting that GetPageContent does carry each stroke's position and Ink Serialized Format renderable by WPF: the data exists but the docx path loses it. |

**Wants**

| What people want changed |
|---|
| Exactly those issues, above all ink fidelity. |
| OneNote users are still actively escaping to Markdown in 2026, and a converter with 766 stars is a real adoption funnel for any Markdown-first app. |
| A notes app that preserves ink semantics (position + strokes) on import would be genuinely differentiated. |

Sources: deep-repos-c.md, github-repos-2.md

## OfficeIMO (EvotecIT/OfficeIMO)

**Features**

| Area | Detail |
|---|---|
| Core | A family of MIT-licensed, COM-free .NET libraries for creating, reading, editing, converting, rendering and extracting Office, PDF, email, OneNote and text formats, with no Microsoft Office or LibreOffice installation required. |
| Packaging | Dozens of packages, many zero-third-party-dependency by design (OfficeIMO.Core, OfficeIMO.Pdf, OfficeIMO.OneNote). |
| Formats | Word (.docx plus first-party .doc), Excel (.xlsx/.xls), PowerPoint (.pptx/.ppt/.pot/.pps), Visio (.vsdx family), OneNote (.one/.onetoc2/.onepkg). |
| Formats | PDF (create/parse/render/edit/sign, PDF/A-2b, PDF/A-3b, PDF/UA-1, Factur-X, ZUGFeRD validation), OpenDocument (ODT/ODS/ODP/ODG), Markdown (typed AST, HTML/PDF rendering). |
| Formats | RTF, AsciiDoc, LaTeX, OPML, DocBook, CSV, EPUB, XPS, DjVu, CHM, iWork (.pages/.numbers/.key reading), Publisher recovery. |
| Formats | Email formats (EML/MIME, MSG/OFT, TNEF, mbox, PST/OST, OLM, EMLX, Outlook OAB, iCalendar, vCard), Google Workspace and Confluence bridges, invoicing (EN 16931/UBL/Polish FA(3), KSeF submission). |
| Tooling | A shared drawing/raster engine with PNG/JPEG/TIFF/WebP/SVG export. |
| Tooling | OCR hooks. |
| Tooling | An optional security provider (CMS/S/MIME/RFC 3161/X.509). |
| Tooling | The OfficeIMO Studio desktop app (Windows/Linux, Apple apps in development) with PDF markup/redaction/forms. |
| Tooling | A CLI. |
| Tooling | An MCP server plus Agent Skills so AI agents can inspect and convert local documents. |

**Sentiment**

| What people say |
|---|
| Very active (current v3.5.2 among dozens of rapid point releases; a one-issue open backlog at time of fetch). |
| The pull-from pieces for a Rust project (code is C#, but MIT): OfficeIMO.Markdown's typed Markdown AST with source spans, stable block identities and transforms (a model for lossless round-trip markdown editing). |
| The OfficeIMO.OneNote .one/.onetoc2 reader/writer design, the only mature open implementation of that format family. |
| The "fidelity report / loss preflight" pattern applied to every conversion, worth copying as an import/export UX principle. |
| The zero-dependency packaging discipline. |

**Wants**

| What people want changed |
|---|
| One visible open issue (#3171, opened 2026-10-23) about the GitHub experience having an "above the fold" problem. |
| No feature-level sentiment recorded. |

Sources: deep-repos-a.md, deep-repos-c.md, github-repos-1.md, github-repos-2.md

## Integration components

(All assessments are about embedding inside a local-first, Rust-target notes app; license is the recurring deciding factor.)

**Features**

| Area | Detail |
|---|---|
| OnlyOffice (documents) | An office suite: text document, spreadsheet, presentation and PDF editors. |
| OnlyOffice (documents) | The editing core is sdkjs (a JavaScript editor engine). |
| OnlyOffice (documents) | Document Server is a self-hosted server rendering it in a browser and Desktop Editors is a local shell around the same web core. |
| OnlyOffice (documents) | Embedding path is network embedding: iframe + JavaScript API + postMessage (the Nextcloud, Moodle, Odoo and WordPress connectors are all built on it). |
| OnlyOffice (documents) | AGPL-3.0 across Document Server Community Edition and sdkjs, with additional Section 7 terms (original logo retained, trademarks not usable). |
| OnlyOffice (documents) | Verdict: best-in-class office editing is realistic only if the host accepts AGPL or buys the commercial Developer edition. Weight L; license is the blocker. |
| Stirling PDF | Self-hosted PDF manipulation platform: merge, split, OCR, sign, redact, convert, compress, watermark, plus a desktop client and browser UI. |
| Stirling PDF | Java, ~94-95k stars (Oct 2026). |
| Stirling PDF | Open-core: most of the tree is MIT, but named directories (e.g. `frontend/src/editor/proprietary/`) sit under a proprietary "Stirling PDF User License". |
| Stirling PDF | The essentials (conversion, editing, watermarking, redaction, password protection) remain free for self-hosting. |
| Stirling PDF | No component library or SDK: run it (Docker or desktop) and point a webview/iframe at it, or integrate file-level against its API. |
| Stirling PDF | Verdict: file-level only; a heavy Java server, and the prettiest editing UI lives in proprietary folders. Weight S-M (API) / L (UI embed). |
| Excalidraw (canvas/diagram) | Ships as an npm package exporting the whole editor as a React component (`@excalidraw/excalidraw`), MIT, with `EXCALIDRAW_ASSET_PATH` for self-hosted assets and a documented elements/JSON data model for persistence. |
| Excalidraw (canvas/diagram) | Runs in any webview (Electron, Tauri). |
| Excalidraw (canvas/diagram) | Prior art: the official VS Code extension and Obsidian's popular Excalidraw plugin, which embeds the component inside Obsidian and stores drawings as files in the vault, embeddable in Markdown with notes linked to and from drawings. |
| Excalidraw (canvas/diagram) | Verdict: "the unambiguous win of this whole list." Weight S. |
| VLC / libVLC (media playback) | The VLC player is GPLv2+ but libVLC is deliberately LGPL-2.1+ so third-party (including closed-source) apps can embed the engine. |
| VLC / libVLC (media playback) | C API with official bindings (C++, Python, Java, Objective-C, C#) and render callbacks to output video into a host-provided surface. |
| VLC / libVLC (media playback) | Codec patents may require royalties for some bundled codecs. |
| VLC / libVLC (media playback) | Verdict: the mainstream way to embed playback (FFI + window interop; binaries ~100MB+). Weight M. |
| VLC / libVLC (media playback) | (mpv/libmpv, also LGPL, exists outside this list.) |
| Audacity (audio editing) | GPLv3 project mid-way through a large 4.x rewrite. |
| Audacity (audio editing) | No library, no SDK, no WASM build, no headless mode. |
| Audacity (audio editing) | The only automation surface is `mod-script-pipe`, which lets an external Python/Perl script drive a running Audacity instance over named pipes. |
| Audacity (audio editing) | Verdict: file-level only (launch externally, optionally drive via script pipes). Embedding its DSP would mean a hard fork. |
| Audacity (audio editing) | If waveform editing is needed, purpose-built DSP crates are the honest answer. Weight M (poor value). |
| OBS Studio (recording/streaming) | GPL-2.0-or-later. |
| OBS Studio (recording/streaming) | libobs is the embeddable rendering/compositing/encoding core, but embedding it in-process makes the host a GPL-2.0+ derivative. |
| OBS Studio (recording/streaming) | Streamlabs' obs-studio-node was released under GPLv2 for exactly this reason. |
| OBS Studio (recording/streaming) | Commercial embedding without source disclosure produced a license dispute (lowkey.gg). |
| OBS Studio (recording/streaming) | Verdict: either a GPL-licensed separate helper process, or OS-level capture APIs (ScreenCaptureKit/AVFoundation) instead. Weight L-XL (libobs) / S (OS APIs). |
| Image editors (GIMP / Krita / Photopea) | GIMP is GPL-3.0 (GPLv3+ well before 3.0; 3.0 itself shipped 16 March 2025), with Script-Fu/Python-Fu plugins, a libgimp 3.0 API and terminal batch runs, but no embeddable widget. |
| Image editors (GIMP / Krita / Photopea) | Krita is GPL with C++/Python plugins (a plugin "can do everything that Krita can do", inside Krita, not inside your app); no embeddable view or headless library. |
| Image editors (GIMP / Krita / Photopea) | Photopea is proprietary (repo is issues-only) with a real iframe + postMessage scripting API, which would make a "local-first" app call a remote closed service with user files. |
| Image editors (GIMP / Krita / Photopea) | Verdict: none is a good embedded component; use a small purpose-built canvas (or Excalidraw) for inline annotation, and GIMP/Krita as external "Edit in..." hand-offs. Photopea is disqualified on license/privacy grounds. |
| Godot (2D/3D engine) | MIT, no royalties. |
| Godot (2D/3D engine) | Headless server builds are officially documented. |
| Godot (2D/3D engine) | LibGodot (engine-as-a-library) was mainlined in a sponsored PR (#110863, merged, with follow-ups #123552/#123717 citing it as merged). |
| Godot (2D/3D engine) | migueldeicaza/libgodot is a maintained embeddable fork powering SwiftGodotKit and react-native-godot as an embedding precedent; GDExtension is the standard native-plugin mechanism. |
| Godot (2D/3D engine) | Verdict: the runtime embedded is realistic and precedented; the Godot editor embedded is fantasy. Makes sense only for interactive 2D/3D widgets (e.g. a 3D-scene note). Weight M-L. |
| Blender (3D) | GPL-2.0-or-later (Cycles is Apache-2.0); API-calling add-ons are treated as GPL. |
| Blender (3D) | No embeddable UI; the real mechanism is `bpy`, an official pip-installable Python module for pipelines and web services, plus headless `blender -b` and the `blenderless` wrapper. |
| Blender (3D) | Verdict: a sidecar Python process/Blender binary for thumbnailing, converting or rendering 3D assets referenced by notes; the GPL boundary is cleanest as a separate process. Weight M. |
| Kdenlive (video editing) | GPL-3.0-or-later as an application, with no embeddable view or headless library. |
| Kdenlive (video editing) | The layer beneath it, the MLT Multimedia Framework (also behind Shotcut), is LGPL-2.1 for the framework and client libraries, with a C API of playlists/producers/consumers. |
| Kdenlive (video editing) | Verdict: use MLT via FFI as the engine for a "video note" playback/trim/convert feature rather than Kdenlive itself. Weight M (MLT) / XL (UI). |
| Synthesis | Clean wins: Excalidraw (S, MIT, embeds directly), libVLC (M, LGPL) and MLT (M, LGPL) as engine-level FFI for media, bpy/Blender (M, headless sidecar) and GIMP headless (M) for file-level processing. |
| Synthesis | Possible but licensing-dependent: OnlyOffice (only with AGPL compatibility or a commercial license) and libobs (only as a GPL-licensed separate helper). |
| Synthesis | Non-starters as embedded components: Audacity, Kdenlive UI, Krita/GIMP UI, Photopea (non-free + remote service). |

**Wants**

| What people want changed |
|---|
| The findings record no user sentiment for these components; the analysis is capability and license fit, not demand. |

Sources: integrations-1.md

---

# PART III: SYNTHESIS

## 1. Feature wish list from the community

Every distinct feature request found across the Discord threads and digests, each tagged with the app/context it came from:

1. Web clipper as good as Evernote's (Evernote; also requested in Tana, Reflect contexts): apps-likes-wants.md, community-digest.md
2. OCR search (search text inside images/PDFs/handwriting) (Evernote praise; Goodnotes; requested in digests): apps-likes-wants.md, community-digest.md
3. Voice suite: voice transcription and voice-note capture (Reflect has it; requested more broadly): apps-likes-wants.md, community-digest.md
4. Canvas + PDF annotation in one app (OneNote overlay model; Goodnotes/Notability strengths; requested in digests): apps-likes-wants.md, community-digest.md
5. Unified task calendar (tasks with dates surfacing on a daily page) (Notion/Tana/Reflect contexts; digests): community-digest.md, thread3-digest.md
6. RAG chat over your own notes (local-first AI; Tolaria model-provider chat; digests): thread-c-local-models.md, tolaria.md, community-digest.md
7. AI stylistic mimicry: AI output in your own handwriting/style rather than generic typed font (Goodnotes complaint generalized): apps-likes-wants.md
8. Flashcards/study mode built in (Amphi canvas app; digests): apps-likes-wants.md, community-digest.md
9. Publishing (turn notes into a site/blog) (Obsidian Publish context; digests): community-digest.md
10. Web companion (access notes from a browser) (Tolaria alpha "remote client"; digests): tolaria.md, community-digest.md
11. Real-time collaboration (multiplayer editing) (Miro/Milanote/OneNote contexts; Logseq DB offline-first RTC goal; digests): apps-likes-wants.md, thread-b-storage.md, thread3-digest.md
12. Tiered roles for collaboration (viewer/editor/admin) (Notion permissions context; digests): community-digest.md, thread3-digest.md
13. Pen/keyboard/touch auto-switching like OneNote (input-mode findings): input-mode-switching.md
14. Cloud-backend choice (self-host or pick your provider instead of vendor cloud) (Amphi Notes self-host; Anytype backup nodes; Reflect Open iCloud/Git): apps-likes-wants.md, thread-b-storage.md
15. Paragraph-level links that survive moves/edits (block-reference durability; Logseq block refs; digests): thread3-digest.md
16. Encrypted backup (E2E-encrypted backups user can verify) (Anytype/Reflect contexts; digests): thread-b-storage.md, community-digest.md
17. Standard-format export that keeps properties/types (Anytype 0.47.4 story; Logseq DB export worries; Tana subset export): thread-b-storage.md
18. A live two-way file mirror of a structured workspace (Thymer model; Logseq's unshipped goal): thread-b-storage.md
19. Ink that never rewrites what you wrote (Goodnotes): apps-likes-wants.md
20. Optional (not forced) handwriting completion/spellcheck (Goodnotes 6): apps-likes-wants.md
21. AI output rendered in handwriting (Goodnotes): apps-likes-wants.md
22. Pay once, keep everything (Notability/Noteshelf lifetime pattern; Evernote/Obsidian pricing): apps-likes-wants.md
23. Sync never held hostage to a subscription (Notability iCloud lock): apps-likes-wants.md
24. Honor lifetime purchases across major versions (Noteshelf 2 to 3): apps-likes-wants.md
25. Fair/regional sync pricing (Obsidian): apps-likes-wants.md
26. Built-in effortless sync without plugin dependence (Obsidian): apps-likes-wants.md
27. Full offline mode (whole workspace, not per-page) (Notion): apps-likes-wants.md
28. Local data portability; no storage-format lock-in (Notion, Evernote, Anytype, Tana): apps-likes-wants.md, thread-b-storage.md
29. Guaranteed-lossless export (JSON dump of the whole store + Markdown projection + JSON Canvas for canvases) (synthesis in thread-b): thread-b-storage.md
30. Full export/backup for canvas apps (Milanote roadmap poll; "No Easy Export / Backup?"): thread-b-storage.md
31. Edit history on canvas boards (Milanote): apps-likes-wants.md
32. Usable mobile apps at parity with desktop (Milanote, Anytype, Tana, Noteshelf, Reflect, OneNote): apps-likes-wants.md
33. Nested folders/sections (OneNote): apps-likes-wants.md
34. Performance that survives a large corpus (Notion, Miro, Logseq, Obsidian, Tana, Milanote): apps-likes-wants.md
35. Notion-grade database features (formulas, linked views) in private/local apps (Anytype, Reflect): apps-likes-wants.md
36. Supertag-like structure learnable in minutes (Tana): apps-likes-wants.md
37. Daily-notes calm at a local-first price point (Reflect): apps-likes-wants.md
38. Better attachment management (Reflect): apps-likes-wants.md
39. Vector PDF export (Noteshelf deciding feature): apps-likes-wants.md
40. Time-synced audio: tap ink/text to jump in the recording (Notability signature): apps-likes-wants.md
41. Note-taking possible while a study widget/overlay is open (Amphi): apps-likes-wants.md
42. A marketplace for stickers/planners/templates (Goodnotes has it; wanted elsewhere): apps-likes-wants.md
43. A whiteboard that stays fast as the board grows (Miro): apps-likes-wants.md
44. Trustworthy archive you own forever (Evernote): apps-likes-wants.md
45. A third-party security audit for private/encrypted apps (Anytype): apps-likes-wants.md
46. AI over note context with direct model-provider choice (Tolaria): tolaria.md
47. Bundled MCP server / agent tool surface for the vault (Tolaria): tolaria.md
48. Custom views authored by AI (views-as-YAML with natural-language dates) (Tolaria): tolaria.md
49. Git-as-sync with AutoGit idle/focus auto-commit (Tolaria): tolaria.md
50. Wikilinks that auto-update on rename (Tolaria; the inverse of Obsidian's rename-fanout cost): tolaria.md, thread-b-storage.md
51. Truly native (non-web-wrapper) desktop shells (Tolaria HN demand): tolaria.md
52. Feature focus, no churn/creep ("stay focused like Bear"; "we don't need new features") (Tolaria, Goodnotes): tolaria.md, apps-likes-wants.md
53. Per-block capability grants with auditable prompts for embedded terminal/webhook/cron blocks (thread-f security model; the Obsidian vault RAT as the anti-pattern): thread-f-editor-platform.md
54. Beyond-.md structure (a database) without abandoning files (Obsidian forum hunger): thread-b-storage.md
55. Support notes that are not dashes-per-line Markdown (Logseq portability complaint): thread-b-storage.md

## 2. Feature clusters

The recurring themes across apps, grouped:

- Capture versatility: web clipper (Evernote, Tana, Reflect), voice transcription (Reflect), audio-with-ink (Notability, Goodnotes, Noteshelf), quick capture that can be developed later (Goodnotes), inbox capture-vs-organize lifecycle (Tolaria), widget capture (xnotes-android). The wish list adds flashcards/study capture (Amphi) and PDF/image overlay capture (OneNote).: apps-likes-wants.md, tolaria.md, deep-repos-a.md
- Search-everything: OCR inside images and handwriting (Evernote, Goodnotes, OneNote), handwriting-box search (Goodnotes best-in-class), semantic command palette (Tolaria), deep archive search (Evernote), indexing (thread-d). Users consistently name search as the retention feature.: apps-likes-wants.md, thread-d-indexing.md, tolaria.md
- Local-first AI: direct model-provider choice including local (Ollama, LM Studio) versus cloud (Tolaria), GPT assistants (Reflect, Notion, Evernote), AI command bar (Tana), AI commit messages and AI-authored views (Tolaria), RAG chat over notes (digests). The community wants AI on their own terms, over their own notes.: tolaria.md, thread-c-local-models.md, apps-likes-wants.md
- Handwriting: ink rendering quality as a deciding feature (Noteshelf fountain pen; Notability best-in-class), ink fidelity versus AI smoothing (Goodnotes complaint), handwriting OCR search/conversion (Goodnotes), pen/touch/keyboard auto-switching (OneNote reference behavior), reverse-engineering Nebo's handwriting engine (myscript-nebo-reverse).: apps-likes-wants.md, input-mode-switching.md, myscript-nebo-reverse.md
- Canvas: infinite freeform canvas as thinking space (OneNote loved core), real-time collaborative boards (Miro, Milanote), canvas-as-database-view (AFFiNE/BlockSuite edgeless), whiteboards stored as files (Tolaria/tldraw), the live canvas-note bridge (Obsidian Canvas sibling-file design; Heptabase and AFFiNE one-store designs), and canvas-app mortality risk (Muse's wind-down: handed to Adam Wulf as Muse 3.0 and rebranded Allume in June 2026).: apps-likes-wants.md, thread-b-storage.md, thread-f-editor-platform.md
- Databases/structure: relational databases with views (Notion loved and complained about), supertags (Tana), objects/sets/collections (Anytype), blocks with persistent IDs (Logseq DB, BlockSuite Y.Map, Trilium's why-database argument), types-as-lenses without schemas (Tolaria). The cluster's tension: structure wants a database, portability wants files, and no surveyed app has shipped both at high fidelity (Thymer mirror, Logseq two-way sync, both unproven).: apps-likes-wants.md, thread-b-storage.md, thread-f-editor-platform.md, tolaria.md
- Sync/trust: the single most-named pain across every community (OneNote, Anytype, Logseq, Obsidian, Notion, Reflect, Notability). Sub-themes: sync that is fast and never lost data, sync not held hostage to subscriptions, E2E encryption people can verify (Anytype, Reflect), Git-as-sync (Tolaria), P2P/local sync (Anytype), self-hosted sync servers (Amphi), and the warning that generic cloud sync corrupts database stores (Trilium's document.db).: apps-likes-wants.md, thread-b-storage.md, tolaria.md
- Export/anti-lock-in: plain local files as the loyalty anchor (Obsidian), export fidelity as the pressure valve and its repeated failures (Anytype pre-0.47.4, Tana subsets, Logseq properties lost, Milanote per-board only), conversion tooling as a category (ConvertOneNote2MarkDown, TanaMigrator), guaranteed-lossless export as the synthesis (JSON dump + Markdown projection + JSON Canvas), and JSON Canvas as the proven open canvas format.: thread-b-storage.md, apps-likes-wants.md, deep-repos-c.md
- Extensibility: plugin ecosystems as gravity (~9,500 Obsidian plugins, registry ~9,521 entries Oct 2026), plugins as the security surface (the 2026 Obsidian vault RAT campaign; the Tasks-plugin RCE; the per-block grant model as the proposed fix), MCP servers and AGENTS files as the new agent-facing extensibility (Tolaria), embedded app blocks (OnlyOffice, Excalidraw, VLC, Audacity, and the rest of the integrations findings), and embedded terminal/webhook/cron blocks only under core-enforced invariants (thread-f).: thread-f-editor-platform.md, integrations-1.md, tolaria.md, apps-likes-wants.md

Cross-cutting conclusion carried from the findings: the three recurring gaps across all fourteen mainstream apps are (1) sync that is fast, reliable and either free or fairly priced; (2) local files/ownership with easy export; (3) performance that survives a large real corpus. An app that nails all three while keeping any signature modeling idea learnable in minutes addresses the most-named pain in every community studied.: apps-likes-wants.md

## R5 additions: the study/PDF-textbook angle (BookCraft idea research)

- The BookCraft idea as submitted (community suggestion, R5): a dedicated everyday study space for stylus students, explicitly not a PDF editor: its own library with notebooks, imported PDF textbooks and study materials organized by subject or course; notebook feel with natural handwriting, customizable pens and highlighters, easy movement between pages and materials; Drawboard PDF named as the inking-quality reference.: R5-user-link
- Drawboard PDF, what people like: pressure ink feel, dockable favorites-bar tool configs, palm rejection called better than Acrobat's, calibrated measurement/protractor toolset unique in the category.: findings/r5-drawboard-pdf.md
- Drawboard PDF, what people want changed: performance rot in long sessions and on large PDFs, no tabs or pinnable folders, missing in-place paste and hotkeys, free-tier upsell nags, lasting anger at the 2023 move of pressure ink behind Pro. Nothing open source.: findings/r5-drawboard-pdf.md
- The load-bearing study feature set, consistent across every app surveyed: import arbitrary PDFs into a course-organized library; freehand pen/highlighter plus text-layer highlighting; excerpt-to-note linking back to the source page (Flexcil gestures, LiquidText canvas, MarginNote mindmap, Zotero extraction); split view of textbook and notebook; search across handwriting and annotations; lossless export of the annotated PDF; study aids built on annotations (flashcards, quizzes, hide-to-memorize, tape tools).: findings/r5-study-apps-landscape.md
- Most-wanted across study communities: trustworthy sync (Flexcil's number-one request), ink smoothing, pixel eraser and shape tools, layers separating annotations from content (requested even of Notability), true PDF support (OneNote printout is the anti-pattern: image pages, misalignment, memory blowups), large-textbook performance (Goodnotes praised for exactly this), annotation write-back into the source PDF, stable non-subscription pricing (the loudest theme in every community), an end to the two-app pairing problem (Flexcil + Noteful named combos).: findings/r5-study-apps-landscape.md
- Loved differentiators worth stealing: Write's ink-manipulation primitives (select, move, erase, reflow handwritten text); University Notes' memorization layer mechanics on PDFs; Xournal++'s independently movable annotation objects; ZotFile's click-through links from notes back to PDF locations.: findings/r5-study-apps-landscape.md
- Verdict: no app is the unified dedicated study notebook over textbooks; the gap is real but contested (Flexcil closest on workflow but engine-limited, MarginNote deepest system but rigid and buggy, mainstream annotators treat the textbook as one content type). Documented traps for a new entrant: subscriptions, buggy updates, large-PDF performance, sync.: findings/r5-study-apps-landscape.md
- IdeaCraft (aamirenic, MIT): young but directly relevant Rust/Tauri reference: SQLite schema (db.rs), Tauri command layer (commands.rs), sync-folder design and smoke-test harness are pullable under MIT. No handwriting, no mobile. Not part of the ArtCraft family despite the name; rickyb82/ideacraft is the unrelated namesake.: findings/r5-ideacraft.md

## R6 additions: synthesis from the full-depth sweep (12 findings files)

- Obsidian plugin demand signal (16 plugins, registry cross-checked, licenses verified at each repo): self-hostable E2E sync, a Dataview-style query layer, note-embedding canvases, code-running templates, and the file browser as product surface.: findings/r6-obsidian-plugins.md, findings/r6-oss-repos-batch-d.md
- Obsidian plugin cautionary evidence: Kanban orphaned with a version over a year old, Dataview's loudest complaint is table loading speed, Templater has a genuine license conflict (AGPL package.json vs GPL badge, no LICENSE file) needing a human check before any pull decision.: findings/r6-obsidian-plugins.md, findings/r6-oss-repos-batch-d.md
- jpzk/opensidian is the closest existing project to ours: a GPL-3.0 Rust+Tauri v2 clean-room Obsidian clone claiming to run real community plugins; concepts only under GPL, but its restricted-mode plugin trust design is worth copying.: findings/r6-obsidian-plugins.md, findings/r6-oss-repos-batch-d.md
- Sync/CRDT verdict: the CRDT + E2EE intersection is no longer under-documented. Automerge/Keyhive's BeeKEM, Loro's experimental protocol-e2ee, any-sync's encrypted DAGs, secsync's snapshot/AEAD model, and p2panda's post-compromise security all attack it directly.: findings/r6-sync-crdt-stack.md, findings/r6-unverified-resolutions.md
- Sync/CRDT verdict: Rust-native options (yrs, Loro, iroh, automerge's Rust core, nostr-sdk) are real and shippable.: findings/r6-sync-crdt-stack.md, findings/r6-unverified-resolutions.md
- Sync/CRDT license corrections: diamond-types is ISC not MIT, secsync is Apache-2.0 not AGPL-3.0 (last npm publish mid-2024, effectively dormant), TanaMigrator and snlib carry no license (code unpullable).: findings/r6-sync-crdt-stack.md, findings/r6-unverified-resolutions.md
- Sync/CRDT correction: The "Notion uses Yjs" claim was dropped; Notion's own engineering blog describes its own CRDT approach without confirming Yjs.: findings/r6-sync-crdt-stack.md, findings/r6-unverified-resolutions.md
- Handwriting verdict: TrOCR (MIT) is the best open handwriting-to-text engine (IAM CER 2.89 large / 3.42 base / 4.22 small; okraPDF independent testing put TrOCR-large at 3.68 CER, best non-VLM result).: findings/r6-htr-ocr-engines-a.md, findings/r6-htr-ocr-engines-b.md
- Handwriting verdict: Tesseract is disqualified for handwriting (49.58% CER, zero lines exact); ML Kit Digital Ink is stroke-input only and proprietary; PARSeq is scene-text only.: findings/r6-htr-ocr-engines-a.md, findings/r6-htr-ocr-engines-b.md
- Handwriting gaps that remain: temporal line segmentation for online (stroke-based) HTR is unsolved, and general OCR engines stay poor at real handwriting.: findings/r6-htr-ocr-engines-a.md, findings/r6-htr-ocr-engines-b.md
- Handwriting verdict: The Supernote .note format is fully reverse-engineered (philips/supernote-typescript, Aug 2026: TOTALPATH per-stroke trails with pressures and tilts, RATTA_RLE bitmaps, partial-erase fragments, embedded MyScript iink files), giving a real path to pull stylus-vault functionality; snlib (Rust) exists but carries no license.: findings/r6-xournal-rnote-supernote.md
- Local AI verdict: small open-weights models are viable per task with license discipline. Qwen3-Embedding-0.6B (Apache) as default RAG embedder, sqlite-vec brute-force sufficing at notes-app corpus sizes.: findings/r6-local-ai-models.md
- Local AI verdict: batch Whisper feasible on phones while streaming STT needs Moonshine (MIT) or platform APIs (whisper.cpp Android streaming runs slower than realtime; the exact ratio UNVERIFIED in the R8 fact-check).: findings/r6-local-ai-models.md
- Local AI verdict: Kokoro-82M the desktop TTS pick, KittenTTS and Supertonic phone-size but with license warnings, Piper GPL (concepts only).: findings/r6-local-ai-models.md
- Local AI runtimes: llama.cpp, MLC, ExecuTorch, Core ML, ONNX Runtime, MediaPipe/LiteRT, plus Rust-native candle, mistral.rs, burn.: findings/r6-local-ai-models.md
- Local AI verdict: Ollama is a desktop distribution layer, never the mobile mechanism.: findings/r6-local-ai-models.md
- Local AI license traps: Llama Community and Gemma Terms are not OSI licenses; a pre-ship license-verification checklist is in the findings file.: findings/r6-local-ai-models.md
- Minor-apps verdict: across Squid, Concepts, Saber, Workflowy, DEVONthink, ente, Kinopio, Poznote, Tangent, Lockbook and the rest, the demand pattern is consistent.: findings/r6-batch1-minor-note-apps.md, findings/r6-batch2-minor-note-apps.md
- Minor-apps verdict: Sync trust is the category's weakest point (Squid's sync unshipped ~2 years, Samsung Notes duplicating conflicts instead of merging, OneNote sync partnership ending July 2026).: findings/r6-batch1-minor-note-apps.md, findings/r6-batch2-minor-note-apps.md
- Minor-apps verdict: Subscription-and-pack paywalls breed resentment (Concepts, Squid Premium, Obsidian Publish at 8 dollars per site per month).: findings/r6-batch1-minor-note-apps.md, findings/r6-batch2-minor-note-apps.md
- Minor-apps verdict, most liftable local-first patterns: Kinopio's localStorage-first with queued ops and websockets, Lockbook's Rust core with E2EE, Saber's dual-password E2EE Nextcloud sync.: findings/r6-batch1-minor-note-apps.md, findings/r6-batch2-minor-note-apps.md
- Minor-apps verdict: File-format anxiety recurs wherever a closed format is the only container (.sbe, .note, Squid's Premium-walled backups).: findings/r6-batch1-minor-note-apps.md, findings/r6-batch2-minor-note-apps.md
- Editors/publishers verdict: Dillinger's client-side-only rendering and the Homebrewery's markdown-in themed-PDF-out pipeline are both directly liftable patterns; Ghost's Koenig editor and Ghost 6.0's split-services architecture matter if publishing becomes a surface; proofeditor's notes-to-AI contract is a live experiment to watch rather than copy.: findings/r6-editors-publishers.md
- Editors/publishers verdict: The Samsung Notes deep dive exposed the trust pattern of the whole category: PDF export rasterizes handwriting, no bulk export, sync conflicts duplicate instead of merge.: findings/r6-editors-publishers.md
- Nostr/transports verdict: concepts-only for sync plus an optional export path. At least four shipped apps sync notes over Nostr, but relay economics (471 public relays, 343 offline) and the single-identity-key conflict with per-note keys argue against Nostr as primary transport.: findings/r6-nostr-transports-extras.md
- Nostr/transports verdict: Pull regardless: negentropy set-reconciliation (NIP-77) and NIP-44 padding discipline; NIP-44 v2 is Cure53-audited.: findings/r6-nostr-transports-extras.md
- Nostr/transports verdict: nostr crate 0.45.5 runs ~446K downloads/month (crate 0.45.5, Oct 2026).: findings/r6-nostr-transports-extras.md
- Nostr/transports verdict: iroh (MIT/Apache, 1.0 June 2026, default transport in Anytype) is the stronger Rust-native p2p lane.: findings/r6-nostr-transports-extras.md
- Verify-pass closure: 34 unverified entries tracked, 22 resolved, 5 partially, 7 not found.: findings/r6-unverified-resolutions.md
- Verify-pass license corrections applied: diamond-types ISC, secsync Apache-2.0, snlib and TanaMigrator no-license-unpullable, Xournal++ bare GPL-2.0, RNote GPL-3.0-or-later (not Apache/EUPL as first assumed).: findings/r6-unverified-resolutions.md
- Verify-pass closure: fbalobaf/supernote-viewer is gone. "Notion uses Yjs" dropped. One independent Loro-vs-Y.rs-vs-Automerge benchmark exists (giosuel/imaginarium PR 16). Still open: KHATT derivative-weights licensing, Dillinger phishing accusation unverified by design.: findings/r6-unverified-resolutions.md

Sources: the twelve findings/r6-*.md files (r6-batch1-minor-note-apps, r6-batch2-minor-note-apps, r6-editors-publishers, r6-sync-crdt-stack, r6-htr-ocr-engines-a, r6-htr-ocr-engines-b, r6-xournal-rnote-supernote, r6-local-ai-models, r6-obsidian-plugins, r6-oss-repos-batch-d, r6-nostr-transports-extras, r6-unverified-resolutions).

## R7 additions: per-app feature inventories, internet-wide sentiment, remake landscape, and the 11 user-supplied repos

- Feature-inventory closure: 20 majors, 19 OSS apps, and 19 handwriting/study subjects now carry per-feature inventories with a URL on every captured claim; where a page could not be captured the claim is marked UNVERIFIED this session, not filled.: findings/r7-feature-inventory-majors.md, findings/r7-feature-inventory-oss.md, findings/r7-feature-inventory-handwriting.md
- Feature-inventory closure, new verified facts: Kinopio's full localStorage + idb-keyval + queued-API-ops architecture from the author's own writeup with exact pricing ($8/mo, $80/yr, $250 lifetime, 100-card free cap).: findings/r7-feature-inventory-majors.md, findings/r7-feature-inventory-oss.md, findings/r7-feature-inventory-handwriting.md
- Feature-inventory closure, new verified facts: DEVONthink's OCR engine chain (ABBYY per vendor FAQ, Vision-based recognition in DT4, Pro/Server gating) and AES-256 sync locations.: findings/r7-feature-inventory-majors.md, findings/r7-feature-inventory-oss.md, findings/r7-feature-inventory-handwriting.md
- Feature-inventory closure, new verified facts: tldraw's open-SDK/closed-app split with its Durable-Objects/SQLite/R2 sync stack, Make Real, and an official MCP App (March 2026).: findings/r7-feature-inventory-majors.md, findings/r7-feature-inventory-oss.md, findings/r7-feature-inventory-handwriting.md
- Sentiment verdict (internet-wide, beyond the Discord threads): 8 ranked demands, each backed by at least two independent sources.: findings/r7-user-sentiment-sweep.md
- Sentiment verdict, top three: offline/local-first with plain-file ownership as the dominant switch motive, anger at subscription rug-pulls of lifetime buyers (Evernote under Bending Spoons, Notability 2021, GoodNotes' buried one-time tier), sync that never loses data including mobile.: findings/r7-user-sentiment-sweep.md
- Sentiment verdict: Handwriting demand stands as a combined gap: ink feel plus search-without-conversion plus formula handling plus cross-platform sync plus open export has no combined answer (Nebo best at recognition but bare).: findings/r7-user-sentiment-sweep.md
- Sentiment honesty check: local-first/E2EE is loud as the grammar of PKM switchers but niche as a standalone purchase driver outside those bubbles.: findings/r7-user-sentiment-sweep.md
- Remake-landscape verdict: 33 projects mapped, 17 verified alive, 13 dead with evidence, 3 unresolvable this session.: findings/r7-remakes-evernote-notion.md
- Remake-landscape verdict, four death patterns named with evidence: vendor adopt-then-drop (Focalboard), single-maintainer exit (Notea, Athens), incumbent-API dependence (NixNote2, Geeknote, Everpad), acqui-deletion (Skiff).: findings/r7-remakes-evernote-notion.md
- Remake-landscape verdict: Migration pain documented from first-person sources: Evernote ENEX fragility and OCR-index loss, Notion export silently degrading relations/rollups.: findings/r7-remakes-evernote-notion.md
- User-repos verdicts: the strongest new pull-from candidates are SiYuan's dejavu snapshot/provider abstraction with repo-key E2EE (top candidate; WebDAV ETag fragility flagged as an anti-pattern), Memos' single-binary + AI-provider-abstraction story (no sync engine, no E2EE), NexaNote's per-point-pressure ink canvas with tested WebDAV conflict resolution (MPL-2.0), and edgeever's triple-write storage (JSON+Markdown+text) with an offline sync queue.: findings/r7-user-repos-a.md, findings/r7-user-repos-b.md
- User-repos verdicts: Turtl's Rust core carries a real per-space-key E2EE design but the project is effectively stalled.: findings/r7-user-repos-a.md, findings/r7-user-repos-b.md
- User-repos verdicts: notion-re (showcase-only), zappynotes (hiatus), and owlistic (event-bus pattern only) contribute little.: findings/r7-user-repos-a.md, findings/r7-user-repos-b.md

Sources: the seven findings/r7-*.md files.
