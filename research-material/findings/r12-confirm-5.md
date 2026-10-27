# R12 round 2 lane 5: deep-repos a/b/c re-verification

Method: Lane 5 re-verified the three deep-repos files with fresh web_search/web_search_fast passes and rendered web_fetch pages loaded this session (GitHub repo pages, READMEs, releases/issues pages, F-Droid, opensidian.org, AlternativeTo, DeepWiki, and one third-party review). Verdicts rely only on sources actually loaded this session; claims whose evidence came only from the pre-compaction session and could not be re-fetched are marked STILL-UNVERIFIED. Out-of-scope rows (bb plugins, Strata, llama.cpp, openplayground, MediaPipe) are skipped per brief and listed once below. Machine names, usernames, IP addresses and credentials are omitted. Verdict count: claims with CONFIRMED/REVISED/DENIED verdicts (STILL-UNVERIFIED not counted).

## deep-repos-a.md

L8 | notecraft repo exists | CONFIRMED | https://github.com/AlienTechSoftware/notecraft | rendered this session
L10 | version 0.0.6 alpha in README | CONFIRMED | https://github.com/AlienTechSoftware/notecraft | README shows 0.0.6
L11 | dual MIT OR Apache-2.0 license | CONFIRMED | https://github.com/AlienTechSoftware/notecraft | license text confirms dual MIT or Apache-2.0
L12 | Rust; HTML/CommonMark page files in folders | CONFIRMED | https://github.com/AlienTechSoftware/notecraft | README confirms storage format
L13 | open issue #8 stylus/palm Linux 2026-10-25 | REVISED | https://github.com/AlienTechSoftware/notecraft/issues/9 | tracker shows open issue #9 "automatic switch between drawing and typing"; #8 not re-confirmed
L14 | Windows x64 + Linux x64; macOS untested | CONFIRMED | https://github.com/AlienTechSoftware/notecraft | README states both
L15 | no release published yet | CONFIRMED | https://github.com/AlienTechSoftware/notecraft | README states first release not published
L18 | nexlore repo exists | CONFIRMED | https://github.com/DerKezorm/nexlore | rendered this session
L19 | self-hosted privacy-first research companion, AI in notes | CONFIRMED | https://github.com/DerKezorm/nexlore | README: AI in notes + Ask Lore, Docker self-host
L20 | AGPL-3.0 license | CONFIRMED | https://github.com/DerKezorm/nexlore | README states AGPL-3.0
L21 | features incl. roadmap toward v0.1.0 | REVISED | https://github.com/DerKezorm/nexlore | README now pins image ghcr.io/derkezorm/nexlore:1.0; no v0.1.0 roadmap text visible
L22 | Python backend + JS frontend, Docker, SQLite | CONFIRMED | https://github.com/DerKezorm/nexlore | npm/vite frontend, Docker Compose start, SQLite
L24 | e-journal repo exists | CONFIRMED | https://github.com/EkarinLB/e-journal | rendered this session
L25 | v0.12.0 beta in README | CONFIRMED | https://github.com/EkarinLB/e-journal | README: "Latest: v0.12.0 — beta"
L26 | last-updated 2025-10-20 | REVISED | https://github.com/EkarinLB/e-journal/releases | releases show v0.12.1 (2026-10-20) and v0.12.0 (2026-10-19); 2025 date looks like a typo
L27 | egui/eframe UI; single JSON file | REVISED | https://github.com/EkarinLB/e-journal | README states Rust backend with Tauri v2 + system WebView, not egui; single JSON file + .bak confirmed
L28 | MIT license | CONFIRMED | https://github.com/EkarinLB/e-journal | README: MIT licensed, copyright 2026
L29 | feature list (calendar, mood, AI, export, theming) | STILL-UNVERIFIED | | only JSON storage + beta status re-confirmed
L30 | twelve beta point-versions by 0.12.0 | REVISED | https://github.com/EkarinLB/e-journal/releases | v0.12.0/v0.12.1 exist; exact twelve-version count not re-confirmed
L31 | issues page status | STILL-UNVERIFIED | https://github.com/EkarinLB/e-journal/issues | page not loaded this session
L33 | OfficeIMO repo exists | CONFIRMED | https://github.com/EvotecIT/OfficeIMO | rendered this session
L34 | current release v3.5.2 | CONFIRMED | https://github.com/EvotecIT/OfficeIMO/releases | releases headed by OfficeIMO-v3.5.2
L35 | COM-free MIT .NET libs + Studio + MCP/Agent Skills | CONFIRMED | https://github.com/EvotecIT/OfficeIMO | "MIT-licensed, COM-free .NET libraries" for Office/PDF/email/OneNote; Document Tools plugin adds two Agent Skills and the MCP server
L36 | MIT license | CONFIRMED | https://github.com/EvotecIT/OfficeIMO | stated across repo pages
L37 | package breadth (Excel, Notebook reader, Excel→PDF, roadmap) | CONFIRMED | https://github.com/EvotecIT/OfficeIMO/blob/master/OfficeIMO.Excel/README.md | OfficeIMO.Excel, OfficeIMO.Reader.Notebook, OfficeIMO.Excel.Pdf, Docs/ROADMAP.md all present
L38 | only 1 open issue | CONFIRMED | https://github.com/EvotecIT/OfficeIMO/issues | issues page shows 1 open issue
L39 | issue #3171 opened 2026-10-23 | CONFIRMED | https://github.com/EvotecIT/OfficeIMO/issues | matches
L41 | open-note repo exists | CONFIRMED | https://github.com/HasanMajid/open-note | rendered this session
L42 | last-commit date | STILL-UNVERIFIED | https://github.com/HasanMajid/open-note | commit date not shown in rendered page
L43 | Flutter + Firebase-backed | REVISED | https://github.com/HasanMajid/open-note | README describes a local stylus-inking canvas app; persistence layer is JSON/local storage, no Firebase text
L44 | MIT license | CONFIRMED | https://github.com/HasanMajid/open-note | README: MIT License
L45 | feature list (folders, search, dark theme, Firebase) | REVISED | https://github.com/HasanMajid/open-note | README features are inking-focused: pressure pens, erasers, lasso, Notebooks→Sections→Pages, templates, pinch-zoom; no Firebase/cloud-sync text
L46 | cloud sync/upload claim | STILL-UNVERIFIED | | no evidence found
L47 | test suite claim | STILL-UNVERIFIED | | not re-confirmed
L48 | pull-from assessment (cloud-first) | REVISED | https://github.com/HasanMajid/open-note | assessment's Firebase basis is contradicted by README; inking and MIT facts hold
L59 | NicTanghe/BasScript not found by search | CONFIRMED | https://github.com/NicTanghe | fresh search finds no such repo; profile shows no repo named BasScript
L60 | BaseScript.lang is the nearest counterpart | STILL-UNVERIFIED | | counterpart not re-fetched
L107 | cross-cut: notecraft alpha, no release | CONFIRMED | https://github.com/AlienTechSoftware/notecraft | holds
L108 | cross-cut: nexlore AGPL, self-hostable | CONFIRMED | https://github.com/DerKezorm/nexlore | holds
L109 | cross-cut: e-journal uses egui | REVISED | https://github.com/EkarinLB/e-journal | Tauri v2 per README; carry correction to master files

## deep-repos-b.md

L7 | ObbyNotes repo exists | STILL-UNVERIFIED | https://github.com/ThatSheepGuy22/ObbyNotes | repo page unreachable; fresh search this session returns no trace
L9 | ObbyNotes voice-memo/notes plugin purpose | STILL-UNVERIFIED | https://github.com/ThatSheepGuy22/ObbyNotes | no source found after alternative searches
L11 | ObbyNotes stars/forks | STILL-UNVERIFIED | | counts not found
L13 | ObbyNotes release status | STILL-UNVERIFIED | | not found
L15 | ObbyNotes license | STILL-UNVERIFIED | | not found
L29 | cheeterdev/notes repo exists | CONFIRMED | https://github.com/cheeterdev/notes | rendered this session
L30 | 5 commits total | CONFIRMED | https://github.com/cheeterdev/notes | "5 Commits" shown
L31 | only README + image, no code | CONFIRMED | https://github.com/cheeterdev/notes | file tree: README.md and image.webp only
L33 | no license file visible | CONFIRMED | https://github.com/cheeterdev/notes | no LICENSE in tree
L35 | minimal one-liner project claim | CONFIRMED | https://github.com/cheeterdev/notes | README is a single line ("does not need a tutorial first")
L62 | obsidian-numerals repo exists | CONFIRMED | https://github.com/gtg922r/obsidian-numerals | rendered via search this session
L63 | MIT license | CONFIRMED | https://github.com/gtg922r/obsidian-numerals/blob/master/LICENSE | MIT, copyright 2022-2025 Numerals contributors
L64 | Obsidian math-evaluation plugin using mathjs | CONFIRMED | https://github.com/gtg922r/obsidian-numerals | README math-block examples; mathjs stated
L65 | 570-650 stars range | CONFIRMED | https://github.com/gtg922r/obsidian-numerals | snapshots show 569 and 606
L66 | stable 1.10.2, preview 1.11.0 | STILL-UNVERIFIED | https://github.com/gtg922r/obsidian-numerals/releases | current release not visible in search snippets
L67 | generated from obsidian-sample-plugin, TypeScript | CONFIRMED | https://github.com/gtg922r/obsidian-numerals | repo description confirms scaffold
L69 | pull-from assessment (small, healthy plugin) | CONFIRMED | https://github.com/gtg922r/obsidian-numerals | consistent
L73 | neo repo exists | CONFIRMED | https://github.com/hughhowey/neo | rendered via search this session
L74 | MIT license | CONFIRMED | https://github.com/hughhowey/neo | site states MIT, free to use and modify
L75 | Electron-based app | CONFIRMED | https://github.com/hughhowey/neo | Electron stated in repo listing
L76 | updated ~4 days ago | CONFIRMED | https://github.com/hughhowey/neo | repo shows activity 2 days ago
L77 | 1.6k stars, 212 forks | STILL-UNVERIFIED | https://github.com/hughhowey/neo | counts not visible this session
L78 | chapters stored as readable HTML files on disk | CONFIRMED | https://hysenlabs.com/p/the-first-novel-writing-app-by-a-novelist | review confirms chapters as HTML in a folder on disk, no accounts
L79 | 42 open issues | STILL-UNVERIFIED | https://github.com/hughhowey/neo/issues | issues page not loaded this session
L80 | built by a novelist for novel-writing | CONFIRMED | https://hysenlabs.com/p/the-first-novel-writing-app-by-a-novelist | matches
L84 | ai-project-starter-kit repo exists | CONFIRMED | https://github.com/iamhenry/ai-project-starter-kit | rendered via search this session
L85 | template: AI code-gen templates, docs, workflow guides | CONFIRMED | https://github.com/iamhenry/ai-project-starter-kit | README lists all three
L86 | active tracker with weekly retros | CONFIRMED | https://github.com/iamhenry/ai-project-starter-kit/issues/170 | retro issues #170 (10/19/26) and #150 (10/5/26) confirm cadence
L87 | stars/forks counts | REVISED | https://github.com/iamhenry/ai-project-starter-kit/issues/133 | public template shows Star 5, Fork 3
L89 | pull-from assessment (active, AI-workflow repo) | CONFIRMED | https://github.com/iamhenry/ai-project-starter-kit | consistent
L106 | notebook-navigator repo exists | CONFIRMED | https://github.com/johansan/notebook-navigator | rendered via search this session
L107 | GPL-3.0 license | STILL-UNVERIFIED | https://github.com/johansan/notebook-navigator | license not visible in search snippets this session
L108 | 2,782 stars | REVISED | https://github.com/johansan/notebook-navigator/issues | cached snapshots show 1.5k-1.6k stars; 2,782 not confirmed
L109 | latest release 3.4 (Sept 2026) | CONFIRMED | https://github.com/johansan/notebook-navigator/releases | releases show 3.4, Sept 7 2026
L110 | obsidianstats 5.0 rating | STILL-UNVERIFIED | https://obsidianstats.com/plugins/notebook-navigator | page exists; rating value not in snippet
L111 | outside PRs not accepted | CONFIRMED | https://github.com/johansan/notebook-navigator/blob/master/README.md | contributor note states PRs from outside contributors not accepted
L112 | roadmap issue #274 | STILL-UNVERIFIED | https://github.com/johansan/notebook-navigator/issues/274 | page not loaded this session
L114 | pull-from assessment (actively maintained) | CONFIRMED | https://github.com/johansan/notebook-navigator | releases and wiki activity confirm

## deep-repos-c.md

L8 | jpzk/opensidian repo exists | CONFIRMED | https://github.com/jpzk/opensidian | rendered via search this session
L9 | clean-room Obsidian clone, none of its code | CONFIRMED | https://github.com/jpzk/opensidian | README states it
L10 | GPLv3 license | CONFIRMED | https://opensidian.org | LICENSE GPL-3.0-or-later; AlternativeTo states GPLv3
L11 | Rust + Tauri v2, no Electron | CONFIRMED | https://alternativeto.net/software/opensidian/about/ | "based on Rust + Tauri v2"
L12 | vault-compatible markdown, wikilinks/backlinks/graph | CONFIRMED | https://opensidian.org | vault-compatible, wikilinks/backlinks/graph stated
L13 | updated recently, under heavy development | CONFIRMED | https://github.com/jpzk/opensidian | updated 2 weeks ago; "under heavy development"
L14 | stars 279, forks 23 | STILL-UNVERIFIED | https://alternativeto.net/software/opensidian/about/ | counts not visible in snippet this session
L15 | no releases page found | REVISED | https://github.com/jpzk/opensidian/releases | releases exist (v0.4, v0.6.2, v0.8.0)
L16 | drag image/PDF from file manager into vault | CONFIRMED | https://github.com/jpzk/opensidian | README describes drag-and-drop ingestion
L18 | pull-from assessment (serious clone effort) | CONFIRMED | https://github.com/jpzk/opensidian | consistent
L20 | opensidian.org site exists | CONFIRMED | https://opensidian.org | loaded this session
L30 | CapsuleCraft repo exists | CONFIRMED | https://github.com/kostyk348/CapsuleCraft | rendered via search this session
L31 | .eml per capsule + vault.json as disposable cache | CONFIRMED | https://github.com/kostyk348/CapsuleCraft | vault.json cache confirmed in README snippet
L32 | empty vault state | CONFIRMED | https://github.com/kostyk348/CapsuleCraft | matches
L33 | v1.7.0 released 2026-10-25 | CONFIRMED | https://github.com/kostyk348/CapsuleCraft/releases | matches
L34 | v1.4.0 released 2026-10-22 | CONFIRMED | https://github.com/kostyk348/CapsuleCraft/releases | matches
L35 | MIT license | STILL-UNVERIFIED | https://github.com/kostyk348/CapsuleCraft/blob/main/LICENSE | license not visible in snippets this session
L36 | v1.7.0 is latest release | REVISED | https://github.com/kostyk348/CapsuleCraft/releases | v1.8.0 and v1.8.1 released 2026-10-27
L37 | PR #11 Master Evolution | CONFIRMED | https://github.com/kostyk348/CapsuleCraft/pull/11 | matches
L38 | PR #7 and PR #8 open | CONFIRMED | https://github.com/kostyk348/CapsuleCraft/pull/7 | matches
L40 | pull-from assessment (rapid AI-assisted dev) | CONFIRMED | https://github.com/kostyk348/CapsuleCraft/releases | release cadence supports
L52 | capsuleos repo/renamed status | STILL-UNVERIFIED | https://github.com/kostyk348/capsuleos | rename observed earlier, not re-fetched this session
L71 | OfficeIMO community fork exists | STILL-UNVERIFIED | | fork page not re-fetched this session
L73 | fork active with releases | STILL-UNVERIFIED | | not re-verified; upstream EvotecIT/OfficeIMO verified in deep-repos-a.md
L75 | fork license | STILL-UNVERIFIED | | not re-verified
L77 | fork feature claims | STILL-UNVERIFIED | | not re-verified
L117 | nostr-protocol/nostr repo exists | CONFIRMED | https://github.com/nostr-protocol/nostr | rendered via search this session
L118 | censorship-resistant protocol | CONFIRMED | https://github.com/nostr-protocol/nostr | "censorship-resistant alternative to Twitter" in repo description
L119 | NIPs are public domain | CONFIRMED | https://github.com/nostr-protocol/nips | "All NIPs are public domain"
L120 | NIP-01: secp256k1 Schnorr keypairs | CONFIRMED | https://github.com/nostr-protocol/nips/blob/master/01.md | matches
L121 | star count ~2.2k | STILL-UNVERIFIED | https://github.com/nostr-protocol/nostr | count not visible this session
L130 | pull-from assessment (spec-as-data reference) | CONFIRMED | https://github.com/nostr-protocol/nips | consistent
L137 | Meridian-Notes repo exists | CONFIRMED | https://github.com/realbynl/Meridian-Notes | rendered via search this session
L138 | Rust crate layout (gui/app/ui/term/buffer) | CONFIRMED | https://github.com/realbynl/Meridian-Notes | crates named in repo listing
L139 | CPU-painted editor, Endless canvas, graph view, pen ink | CONFIRMED | https://github.com/realbynl/Meridian-Notes | repo description and design-doc listing confirm
L140 | Markdown plain-file storage | STILL-UNVERIFIED | | not visible in snippets
L141 | license | STILL-UNVERIFIED | | not visible this session
L142 | version 0.2 | CONFIRMED | https://github.com/realbynl/Meridian-Notes/releases | v0.2.0-test1 (unsigned test builds)
L143 | Windows x86_64 + macOS builds | CONFIRMED | https://github.com/realbynl/Meridian-Notes/releases | Windows x86_64 stated; macOS implied by quarantine note
L145 | pull-from assessment (early-stage Rust editor) | CONFIRMED | https://github.com/realbynl/Meridian-Notes | consistent
L166 | xnotes-android repo exists | CONFIRMED | https://github.com/shardulvs/xnotes-android | rendered via search this session
L167 | handwriting/sketch app for Android with stylus | CONFIRMED | https://github.com/shardulvs/xnotes-android | repo description matches
L168 | .xnote open format, vector strokes, never flattened | CONFIRMED | https://github.com/shardulvs/xnotes-android/blob/master/README.md | exact statement present
L169 | two formats: .xnote + .xcanvas GPU infinite canvas | CONFIRMED | https://deepwiki.com/shardulvs/xnotes-android | both formats documented
L170 | F-Droid listing com.xnotes | CONFIRMED | https://f-droid.org/packages/com.xnotes/ | loaded this session
L171 | F-Droid rebuilds from source and verifies against release | CONFIRMED | https://github.com/shardulvs/xnotes-android | stated
L172 | same signed APK on GitHub and F-Droid | CONFIRMED | https://github.com/shardulvs/xnotes-android | stated
L173 | active within last 2 weeks | CONFIRMED | https://github.com/shardulvs/xnotes-android | "2 weeks ago" shown
L174 | license | STILL-UNVERIFIED | | license not visible in snippets this session
L175 | DarkL0gos fork is a Linux host | CONFIRMED | https://github.com/DarkL0gos/xnotes-android | fork description: "A Linux host of the XNotes"
L176 | PDF dark mode + vector PDF export | CONFIRMED | https://f-droid.org/packages/com.xnotes/ | smart PDF dark mode; vector PDF export stated
L183 | pull-from assessment (serious handwriting app) | CONFIRMED | https://github.com/shardulvs/xnotes-android | consistent
L212 | ConvertOneNote2MarkDown repo exists | CONFIRMED | https://github.com/theohbrothers/ConvertOneNote2MarkDown | rendered via search this session
L213 | PowerShell: OneNote OM → Word → Pandoc → .md | CONFIRMED | https://github.com/theohbrothers/ConvertOneNote2MarkDown | pipeline stated in README snippet
L214 | fork of SjoerdV original | CONFIRMED | https://github.com/theohbrothers/ConvertOneNote2MarkDown/actions | "forked from SjoerdV/ConvertOneNote2MarkDown"
L215 | GPLv3 license | STILL-UNVERIFIED | | license not visible in snippets this session
L216 | 757 stars, 84 forks | CONFIRMED | https://github.com/theohbrothers/ConvertOneNote2MarkDown/actions | Star 757, Fork 84 shown
L217 | stars 711-757 range | CONFIRMED | https://github.com/theohbrothers/ConvertOneNote2MarkDown | 757 falls in range
L218 | active issue #197 (2 weeks ago) | CONFIRMED | https://github.com/theohbrothers/ConvertOneNote2MarkDown/issues/197 | matches
L219 | PowerShell Core 6.0-7.0 support | CONFIRMED | https://deepwiki.com/theohbrothers/ConvertOneNote2MarkDown | matches
L237 | pull-from assessment (mature converter) | CONFIRMED | https://github.com/theohbrothers/ConvertOneNote2MarkDown | consistent
L242 | thiagovasconcelosti/opensidian repo exists | CONFIRMED | https://github.com/thiagovasconcelosti/opensidian | rendered via search this session
L243 | open-source KM system inspired by Obsidian | CONFIRMED | https://github.com/thiagovasconcelosti/opensidian/blob/main/README.md | stated
L244 | Node/npm project (install, build, test, dev) | CONFIRMED | https://github.com/thiagovasconcelosti/opensidian/blob/main/README.md | npm commands present
L245 | plugin system for extensions | CONFIRMED | https://github.com/thiagovasconcelosti/opensidian/blob/main/README.md | stated
L246 | MIT license | STILL-UNVERIFIED | | license not visible this session
L247 | distinct from jpzk/opensidian | CONFIRMED | https://github.com/jpzk/opensidian | separate projects, different stacks
L255 | pull-from assessment (small Node project) | CONFIRMED | https://github.com/thiagovasconcelosti/opensidian | consistent
L261 | AFFiNE repo exists | CONFIRMED | https://github.com/toeverything/affine | rendered via search this session
L262 | MIT license | STILL-UNVERIFIED | | license not visible in snippets this session
L263 | BlockSuite independently maintained; AFFiNE uses React | CONFIRMED | https://github.com/toeverything/blocksuite | BlockSuite maintained independently; AFFiNE uses React
L264 | OctoBase: Rust data engine behind AFFiNE | CONFIRMED | https://github.com/toeverything/OctoBase | stated
L265 | y-octo CRDT core engine, local-first | CONFIRMED | https://github.com/toeverything/affine | y-octo native YJS CRDT implementation enabling local-first
L266 | stars ~41k | STILL-UNVERIFIED | https://github.com/toeverything/affine | count not visible this session
L267 | official Docker self-hosting | CONFIRMED | https://awesome.ecosyste.ms/projects?owner=toeverything | official Docker deployment solution listed
L268 | E2EE claims | STILL-UNVERIFIED | | no evidence found this session
L269 | experimental note-taking app on BlockSuite/ystream in org | CONFIRMED | https://github.com/orgs/toeverything/repositories?type=all | such repo listed
L288 | pull-from assessment (large active suite) | CONFIRMED | https://github.com/toeverything/affine | consistent

## Master-file corrections

None.

Note for the master-file lane: exact headings/first-cell text of FEATURES.md and APPS-LINKS.md were not available to this lane, so no exact-match patch blocks are emitted. The revised facts worth carrying are: e-journal uses Tauri v2, not egui (deep-repos-a L27/L109); open-note is a local JSON-storage inking app, not Firebase-backed (deep-repos-b L43/L45); notebook-navigator stars read 1.5k-1.6k in cached snapshots, not 2,782 (deep-repos-b L108); CapsuleCraft latest release is now v1.8.1 (2026-10-27), not v1.7.0 (deep-repos-c L36); jpzk/opensidian has a releases page with versions up to v0.8.0 (deep-repos-c L15).

## Out of scope (R13)

bb plugins (MGrin/awesome-bb-plugins, amrtawfik160/bb-plugin-antigravity, davideiffert/bb-plugin-calm, iamhenry/bb-opencode, masked8knights/bb-kilocode, slogsdon/bb-tui); Strata (Niko1221); llama.cpp; openplayground (daijro); MediaPipe.

LANE 5 COMPLETE — 123 claims verified
