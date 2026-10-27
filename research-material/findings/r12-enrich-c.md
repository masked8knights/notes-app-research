# Round R12 — Lane C (evidence enrichment) — notes-app research

Apps assigned: Logseq, Joplin, Notesnook, Trilium Notes, AFFiNE, ente, Heptabase, Kinopio, tldraw, Excalidraw, Saber, Lockbook.

## Logseq

### Visual surface
Desktop (Electron, macOS/Windows/Linux): a left sidebar rail (journals, pages, graph, all pages, all files) plus a right sidebar for pinned pages; the main canvas is a block-based outliner where every bullet is a node and typing `[[` creates page links; a top-right panel toggles "featured" views (graph, contents, linked references, queries); daily journals are the default landing surface [https://github.com/logseq/logseq]. The graph view renders a force-directed node network in a modal overlay; PDFs open in a side/inline pane with annotation highlights. Mobile apps exist for the legacy file version, and a new iOS app for the DB version is in alpha with Android "coming soon" [https://github.com/logseq/logseq]. Web version at app.logseq.com mirrors the desktop shell [https://github.com/logseq/logseq]. Marketing site (logseq.com) is minimal, dark-on-light, and leads with "privacy-first, open-source knowledge base" [https://logseq.com/].

SHOT-LIST (prioritized):
- Home / outliner with journals: https://logseq.com/
- Web app UI (editable demo graph): https://app.logseq.com/
- Repo README (feature summary + roadmap link): https://github.com/logseq/logseq
- Docs hub (feature tour, screenshots of outliner/PDF/queries): https://docs.logseq.com/
- Forum (UI workflows, screenshots in topics): https://discuss.logseq.com/
- DB-version mobile alpha (iOS screenshots surface in Discord/blog, not on README): https://blog.logseq.com/

### Docs analysis
- Two-track product in 2026: legacy file-based version (Markdown/Org-mode, flat EDN/DataScript index over md files) and the DB version (beta) backed by SQLite, with its own sync (RTC, real-time collaboration) in alpha and a new iOS app in alpha; DB version explicitly warns data loss is possible and recommends regular SQLite backups [https://github.com/logseq/logseq].
- Plugin API is first-class: plugins-doc.logseq.com, marketplace repo, sample plugins repo, developer mode toggle in settings [https://github.com/logseq/logseq].
- Git/GitHub sync is an officially documented community pattern (version control of the graph folder) [https://hub.logseq.com/integrations/aV9AgETypcPcf8avYcHXQT/logseq-sync-with-git-and-github/krMyU6jSEN8jG2Yjvifu9i].
- Design decisions worth borrowing: (1) everything is an outliner block, so any note is a queryable atom; (2) journals-as-default-entry lowers blank-page friction; (3) linked references computed automatically per page; (4) `[[wiki links]]` and `#tags` resolve across md and org-mode; (5) paid sync is positioned as a donation tier, not a feature wall [https://github.com/logseq/logseq, https://aiproductivity.ai/pricing/logseq/].
- UNVERIFIED (from third-party pricing pages, not Logseq's own docs): Sync Backer $5/mo, Sync Sponsor $15/mo tiers [https://aiproductivity.ai/pricing/logseq/, https://www.thegeeksclub.com/platforms/logseq/].

### Features
| Area | Detail |
|---|---|
| Editor | Block-based outliner; markdown + org-mode; wikilinks, tags, TODOs, block refs/embeds |
| Structure | Pages, namespaces, journals, graph view, linked/unlinked references, queries (simple + advanced Datalog) |
| Files | Markdown (.md) or Org (.org) files on disk per graph; assets folder; PDF annotation |
| Sync | Legacy: no official sync (git/Dropbox DIY, or paid Sync for md graphs); DB version: RTC real-time sync in alpha |
| Extensibility | Plugin API + marketplace, themes, custom queries, SCI/Clojure scripting |
| Learning | Flashcards (SRS), spaced repetition on blocks |
| Platforms | Windows/macOS/Linux desktop (Electron), web (app.logseq.com), iOS+Android for legacy; DB mobile iOS alpha |
| Pricing | Free/open-source for full local use; paid = sync/backer tiers (see pricing table) |

### Sentiment
| What people say |
|---|
| Longtime users praise the outliner model for ADHD-friendly capture and daily-notes workflows (r/logseq year-long review; Dec 2025 thread) [https://www.reddit.com/r/logseq/comments/1gxc7ra/a_review_of_logseq_after_using_it_for_more_than/, https://www.reddit.com/r/logseq/comments/1pibjd2/coming_back_to_logseq_has_anything_changed_was/] |
| Complaint: slow boot/performance on large graphs in the file version (">10s boot time" reports; "inadequate for large amounts of structured data") [https://www.reddit.com/r/logseq/comments/1pstos9/what_are_you_planning_to_replace_logseq_with/, https://www.reddit.com/r/logseq/comments/1gxc7ra/a_review_of_logseq_after_using_it_for_more_than/] |
| Trust erosion from infrequent updates and poor communication about the DB version timeline [https://www.reddit.com/r/logseq/comments/1kxqouy/i_want_to_hear_your_thoughts_on_logseq_and/, https://www.reddit.com/r/logseq/comments/1p5d07s/request_to_logseq_dev_team_new_update_on_db/] |
| Sync corruption stories drive migration away ("corrupted a bunch of my logseq files") [https://www.reddit.com/r/logseq/comments/1swrx2z/what_is_the_state_of_logseq_should_i_jumpin/] |

### Wants
| What people want changed |
|---|
| DB version progress and a clear migration path; some fear losing plain-file access as the DB version advances [https://www.reddit.com/r/logseq/comments/1swpxht/big_update_logseq_is_splitting_into_two_versions/, https://www.reddit.com/r/logseq/comments/1paij9o/migrating_away_from_logseq_after_years_and_im/] |
| Reliable, non-corrupting sync; faster app startup; continued org-mode support in DB version (reported missing) [https://www.reddit.com/r/logseq/comments/1swrx2z/what_is_the_state_of_logseq_should_i_jumpin/, https://www.reddit.com/r/logseq/comments/1ld0xzm/are_you_going_to_switch_to_logseq_after_db_version/] |

### Pricing and platforms
| Item | Detail |
|---|---|
| Core app | Free, open-source (AGPL), fully functional locally [https://github.com/logseq/logseq, https://productivitystack.io/tools/logseq/] |
| Sync | Donation-based tiers; third-party pages list Sync Backer $5/mo and Sync Sponsor $15/mo (UNVERIFIED against official page) [https://aiproductivity.ai/pricing/logseq/, https://thetechverdict.com/apps/logseq-pricing] |
| Platforms | macOS, Windows, Linux (desktop + Linux installer script in repo); web app; legacy mobile apps; DB-version iOS alpha [https://github.com/logseq/logseq] |
| Self-host | Web app can be self-hosted via Docker per repo docs (docs/ folder Docker Web App Guide) [https://github.com/logseq/logseq] |

### Contradictions
- Common picture "Logseq is a files-first app" now conflicts with 2026 direction: an April 2026 Reddit thread reports Logseq splitting/deprecating the file-based version in favor of the DB version, which users read as losing plain-files-on-disk [https://www.reddit.com/r/logseq/comments/1swpxht/big_update_logseq_is_splitting_into_two_versions/].
- "DB version is the future, everything is fine" is contradicted by README's own beta/data-loss warning and by sync-corruption reports [https://github.com/logseq/logseq, https://www.reddit.com/r/logseq/comments/1swrx2z/what_is_the_state_of_logseq_should_i_jumpin/].

Sources: https://github.com/logseq/logseq · https://logseq.com/ · https://hub.logseq.com/integrations/aV9AgETypcPcf8avYcHXQT/logseq-sync-with-git-and-github/krMyU6jSEN8jG2Yjvifu9i · https://aiproductivity.ai/pricing/logseq/ · plus Reddit threads listed inline.

## Joplin

### Visual surface
Desktop (Electron; Windows/macOS/Linux): a three-pane layout — notebook tree in a left sidebar, note list in the middle, Markdown editor with a live/preview split on the right — with a plugin-panel toggle, tag sidebar, and a search bar up top; there is also a WYSIWYG Markdown editor toggleable with the source mode [https://github.com/laurent22/joplin]. Android/iOS apps are simpler: notebook list, note list, editor, with sync settings deep in config and rich Markdown rendering with checkboxes, code blocks, tables [https://github.com/laurent22/joplin]. The visual language is utilitarian rather than designed: flat panels, default-ish fonts, dense information layout; screenshots on the site show the classic Evernote-like tri-pane [https://joplinapp.org/plans/]. Web Clipper adds a browser extension UI; there is also a CLI terminal client and a headless server app [https://github.com/laurent22/joplin].

SHOT-LIST (prioritized):
- Homepage hero (desktop tri-pane screenshot): https://joplinapp.org/
- Plans page (Joplin Cloud marketing + app screenshots): https://joplinapp.org/plans/
- Repo README (screenshot of desktop app + platform logos): https://github.com/laurent22/joplin
- Docs (feature pages, mobile screenshots): https://joplinapp.org/help/
- Forum screenshots (real user setups, themes): https://discourse.joplinapp.org/
- App Store / Play listing for mobile UI: https://joplinapp.org/

### Docs analysis
- Offline-first: all data local always; notes are Markdown, organized into notebooks, with tags, to-dos with due dates and alarms; full-text search on all platforms [https://github.com/laurent22/joplin].
- Sync targets are BYO-cloud: Nextcloud, Dropbox, OneDrive, WebDAV, local filesystem, and Joplin Cloud (the paid hosted option); E2EE is available on all platforms and on all sync targets, with keys/password-based encryption of notes, notebooks, tags and resources [https://github.com/laurent22/joplin, https://github.com/laurent22/joplin/blob/dev/readme/apps/sync/e2ee.md].
- E2EE design caveat documented in the spec: sync is stateless, clients cannot tell whether other clients use E2EE, and mixed encrypted/unencrypted upload is supported but messy; disabling E2EE must be done manually on every client [https://github.com/laurent22/joplin/blob/master/readme/spec.md].
- Evernote import is first-class: formatted content converted to Markdown, resources and metadata (geolocation, timestamps) preserved [https://github.com/laurent22/joplin].
- Ecosystem breadth: desktop, mobile, CLI, server (Joplin Server for self-hosting), web clipper for Firefox/Chrome, plugins and themes; a warrant canary with published signing key is posted in the repo [https://github.com/laurent22/joplin].
- Joplin Cloud: EU-hosted in Paris, GDPR framing, education discount 50%; feature walls include note publishing, email-to-note, collaboration [https://joplinapp.org/plans/].
- Design decisions worth borrowing: (1) BYO-sync-backend as the base layer with a paid hosted tier only for convenience; (2) E2EE as a per-notebook/folder toggle rather than global-only; (3) stateless sync protocol as a robustness/simplicity tradeoff (documented weakness too); (4) export as an explicit, documented feature path for lock-in avoidance.

### Features
| Area | Detail |
|---|---|
| Editor | Markdown with split preview, WYSIWYG mode, code blocks, tables, math, diagrams via plugins |
| Structure | Notebooks (nested), sub-notebooks, tags, to-dos/alarms, search operators |
| Sync | Nextcloud/Dropbox/OneDrive/WebDAV/local file/Joplin Cloud; Joplin Server self-host; E2EE optional |
| Attachments | Images, PDFs, audio; per-note/attachment size caps apply on Cloud plans (10 MB Basic tier, larger on Pro) [https://www.softwareadvice.com/product/527527-Joplin/, https://www.cloudwards.net/joplin-review/] |
| Extras | Web clipper (Firefox/Chrome), email-to-note (Cloud), note publishing (Cloud), CLI, server app |
| Platforms | Windows, macOS, Linux, Android, iOS, terminal, self-hosted server |
| Pricing | App free; Joplin Cloud paid tiers for hosted sync |

### Sentiment
| What people say |
|---|
| Core block loved: free, open-source, works offline, huge Evernote import success (10k+ notes moved happily) [https://www.reddit.com/r/joplinapp/comments/wgcg9q/why_is_joplin_so_disliked/] |
| Most-cited negatives: sync reliability (conflicts, deletions, initial sync crawling over WebDAV) and a weak iOS app [https://discourse.joplinapp.org/t/very-disappointed-on-joplin-and-its-sync-problems/45026, https://www.reddit.com/r/joplinapp/comments/1mrszbj/initial_sync_taking_forever/, https://www.reddit.com/r/joplinapp/comments/1fhmjat/rip_joplin/] |
| "Not refined or elegant UI" is a recurring aesthetic verdict even from fans [https://www.reddit.com/r/joplinapp/comments/wgcg9q/why_is_joplin_so_disliked/] |
| Offline-first edit-not-yet-synced workflow causes real data-loss stories for some users [https://www.reddit.com/r/joplinapp/comments/1ki3leg/thats_it_i_quit/] |
| Joplin Cloud reported as noticeably faster/more reliable than DIY WebDAV among 2026 users [https://www.reddit.com/r/joplinapp/comments/1rl5d1w/how_reliable_is_joplin_cloud/] |

### Wants
| What people want changed |
|---|
| Better sync conflict handling and clearer sync state UI; faster initial sync; a more polished mobile (especially iOS) experience [https://discourse.joplinapp.org/t/very-disappointed-on-joplin-and-its-sync-problems/45026, https://www.reddit.com/r/joplinapp/comments/1fhmjat/rip_joplin/] |
| Rich-table editing in the non-Markup editor, better WYSIWYG fidelity, less clunky attachments management [https://www.reddit.com/r/Evernote/comments/17mem41/is_joplin_the_best_alternative/] |

### Pricing and platforms
| Item | Detail |
|---|---|
| App | Free, open-source (AGPL-ish), all platforms [https://github.com/laurent22/joplin] |
| Joplin Cloud | Basic ~EUR 28.69/yr (2 GB, 10 MB/note), Pro ~EUR 80.28/yr tier structure with larger storage/note caps; France/GDPR hosting; 50% education discount [https://www.pcmag.com/reviews/joplin, https://joplinapp.org/plans/] |
| Self-host | Joplin Server (Docker) or third-party managed (Elestio) [https://elest.io/open-source/joplin/resources/plans-and-pricing] |
| Platforms | Windows, macOS, Linux, Android, iOS, CLI, web clipper [https://github.com/laurent22/joplin] |

### Contradictions
- "Joplin sync is broken" vs 2026 Joplin Cloud reports saying everything syncs reliably: the pain concentrates on DIY WebDAV/file sync, not the hosted service [https://www.reddit.com/r/joplinapp/comments/1rl5d1w/how_reliable_is_joplin_cloud/, https://www.reddit.com/r/joplinapp/comments/1lafr0z/sync_issues_and_left_over_files/].
- Third-party pricing pages conflict on Joplin Cloud specifics (one SaaS listing wrongly claims no free app tier); official page is the reference [https://joplinapp.org/plans/, https://www.spotsaas.com/product/joplin/pricing].

Sources: https://github.com/laurent22/joplin · https://github.com/laurent22/joplin/blob/master/readme/spec.md · https://joplinapp.org/plans/ · https://discourse.joplinapp.org/t/very-disappointed-on-joplin-and-its-sync-problems/45026 · plus Reddit threads inline.

## Notesnook

### Visual surface
Desktop/web (Electron + React): a sidebar with item groups (notes, notebooks, tags, favorites, archive, trash), a note list column, and a distraction-free rich editor with a slash-command block menu; top bar carries search, sync status and settings; dark/light themes are a stated core of the shared theme package [https://raw.githubusercontent.com/streetwriters/notesnook/master/README.md]. Mobile (React Native, Android/iOS) mirrors the same three surfaces with a bottom tab bar and per-note action sheet; the marketing site emphasizes "clean and slick UI" and features the same panels in screenshots [https://notesnook.com/]. The editor (TipTap/ProseMirror-based per repo packages) supports callouts, code blocks, tables, and a "properties" pane per note [https://github.com/streetwriters/notesnook]. Web clipper exists as a browser extension [https://github.com/streetwriters/notesnook].

SHOT-LIST (prioritized):
- Homepage hero (editor + sidebar screenshots): https://notesnook.com/
- Pricing page (plan comparison UI): https://notesnook.com/pricing
- Downloads page (platform screenshots): https://notesnook.com/downloads
- Repo README (logo, monorepo map): https://github.com/streetwriters/notesnook
- Help center (feature pages with screenshots): https://notesnook.com/help/
- Vericrypt (encryption verification tool UI): https://vericrypt.notesnook.com/

### Docs analysis
- Fully open source (client and server) under GPL-3.0; monorepo contains web, desktop, mobile, web-clipper, shared core, crypto wrapper around libsodium, its own TipTap-based editor package, and theme package [https://github.com/streetwriters/notesnook, https://raw.githubusercontent.com/streetwriters/notesnook/master/README.md].
- Zero-knowledge E2EE: everything encrypted on-device with XChaCha20-Poly1305 and Argon2 key derivation; Vericrypt is an offline tool that lets users verify encryption claims with their own account data [https://github.com/streetwriters/notesnook, https://vericrypt.notesnook.com/].
- Requires an email account (sync identity), with a blog post explaining why — a deliberate design tradeoff vs local-only apps [https://blog.notesnook.com/why-notesnook-requires-an-email-address/].
- Free tier per current pricing page: unlimited encrypted notes on unlimited devices forever; paid plans add attachment storage; on downgrade nothing is deleted or locked (read/edit/export preserved) [https://notesnook.com/pricing]. Third-party detail lists free tier as 50 MB/month attachment storage with 10 MB per-file cap (UNVERIFIED against official page) [https://toolradar.com/tools/notesnook].
- Pricing restructure Oct 2025 into Essential/Pro/Believer plans, with a blog post framing sustainability; free tier strengthened on attachments/vault access per blog [https://blog.notesnook.com/introducing-new-pricing-plans].
- Self-hosting is supported (server code open; co-founder confirmed; docs described as incomplete by third parties) (UNVERIFIED completeness) [https://costbench.com/software/note-taking/notesnook/].
- Dedicated Importer app for migration from Evernote and others is an official sub-project [https://notesnook.com/help/importing-notes].
- Design decisions worth borrowing: (1) verify-your-encryption tooling (Vericrypt) as a trust feature; (2) "nothing locked on downgrade" as an explicit promise; (3) cross-platform editor shipped as a standalone npm package; (4) monorepo with shared core so all clients share one sync engine.

### Features
| Area | Detail |
|---|---|
| Editor | Rich WYSIWYG (TipTap-based) with blocks, callouts, code, tables, math; no first-class Markdown editing (see sentiment) |
| Structure | Notes, notebooks, tags, favorites, pinned, color labels, references/links between notes, reminders |
| Sync | Real-time + automatic sync; E2EE everywhere; requires account |
| Security | XChaCha20-Poly1305 + Argon2, vault (password-locked notes), 2FA, Vericrypt |
| Extras | Web clipper, importer app, export (Markdown/HTML/TXT/PDF), email-to-note (UNVERIFIED current status) |
| Platforms | Windows, macOS, Linux (Electron), Android, iOS, web |
| Pricing | Free tier; Essential/Pro/Believer paid tiers |

### Sentiment
| What people say |
|---|
| Widely praised as the best E2EE notes UX: "clean and slick" UI, feature-rich, best-in-class among encrypted alternatives (site testimonials; r/Evernote megathread recommends it for E2EE) [https://notesnook.com/, https://www.reddit.com/r/Evernote/comments/1tcw1fj/megathread_pricing_repackaging_discussion/] |
| October 2025 price change angered users: roughly 69 EUR/yr perceived as too expensive vs one-time-fee rivals like Upnote; "killed the free plan" perception [https://www.reddit.com/r/Notesnook/comments/1nygdsw/the_new_pricing_is_just_too_expensive/, https://www.reddit.com/r/privacy/comments/1nzb3jp/good_free_alternative_to_notesnook/] |
| Broken promise sentiment: users cite earlier assurances prices would not rise [https://www.reddit.com/r/Notesnook/comments/1ffc86f/how_does_the_new_pricing_implementation_affect_me/] |
| Markdown-first users disappointed by Markdown limitations and clunkiness; bug reports feeling unacknowledged [https://www.reddit.com/r/Notesnook/comments/1nyhlpi/i_am_very_very_disappointed/, https://www.reddit.com/r/Notesnook/comments/1o8v7hb/goodbye_notesnook/] |
| Long-term reliability generally good; new Evernote émigrés weigh company track record and non-EU/US base as a concern [https://www.reddit.com/r/Notesnook/comments/1ppvfxb/notesnook_reliability_over_the_years/] |

### Wants
| What people want changed |
|---|
| Cheaper or grandfathered pricing; one-time or lifetime options; clearer free-tier limits [https://www.reddit.com/r/Notesnook/comments/1nygdsw/the_new_pricing_is_just_too_expensive/] |
| Better Markdown import/export fidelity, fewer bugs, faster fixes, Apple Pencil/handwriting support [https://www.reddit.com/r/Notesnook/comments/1nyhlpi/i_am_very_very_disappointed/, https://www.reddit.com/r/Notesnook/comments/1ag7cpb/worst_notes_app_i_ve_used_so_far/] |

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | Unlimited notes/devices, E2EE, editor features; attachment storage limited [https://notesnook.com/pricing] |
| Paid | Essential/Pro/Believer tiers; ~US$1.67/mo entry per official pricing page; user reports of ~EUR 69/yr for their tier [https://notesnook.com/pricing, https://www.reddit.com/r/Notesnook/comments/1nygdsw/the_new_pricing_is_just_too_expensive/] |
| Self-host | Open-source server; all Pro features free self-hosted (community/co-founder claim, docs incomplete) [https://costbench.com/software/note-taking/notesnook/] |
| Platforms | Windows, macOS, Linux, Android, iOS, web, browser clipper [https://github.com/streetwriters/notesnook] |

### Contradictions
- Earlier "prices will never increase" messaging vs the October 2025 restructure (users quote the promise; blog frames it as a sustainability necessity) [https://www.reddit.com/r/Notesnook/comments/1ffc86f/how_does_the_new_pricing_implementation_affect_me/, https://blog.notesnook.com/introducing-new-pricing-plans].
- Marketing "free forever" vs user perception that the free plan was gutted in 2025; official page still advertises unlimited free notes [https://notesnook.com/pricing, https://www.reddit.com/r/privacy/comments/1nzb3jp/good_free_alternative_to_notesnook/].

Sources: https://github.com/streetwriters/notesnook · https://notesnook.com/pricing · https://blog.notesnook.com/introducing-new-pricing-plans · https://vericrypt.notesnook.com/ · plus Reddit threads inline.

## Trilium Notes

### Visual surface
Desktop (Electron; Windows/macOS/Linux): a dense three-column IDE-like layout — a left launch-bar and note-tree pane, a tabbed main editor, and a right pane for note attributes/backlinks — with a distinctive dark theme by default and hoisting that re-roots the tree at any subtree [https://github.com/TriliumNext/trilium]. Note types switch the editor surface entirely: CKEditor 5 rich text, CodeMirror source/code notes, Excalidraw canvas, Mind Elixir mind maps, Mermaid diagrams, Leaflet geo maps, Tabulator-driven "collections" tables [https://github.com/TriliumNext/trilium]. The server build exposes a web UI described as "almost identical" to desktop (Chrome/Firefox), plus a touch-optimized mobile web frontend [https://github.com/TriliumNext/trilium]. Community native clients exist: TriliumDroid (Android), Pocket Trilium (full local Android instance), Trinote (iOS) [https://github.com/TriliumNext/trilium].

SHOT-LIST (prioritized):
- Repo README (feature list; screenshot assets in repo): https://github.com/TriliumNext/trilium
- Documentation site (UI walkthroughs, screenshots): https://docs.triliumnotes.org
- Wiki screenshots (original zadam wiki, patterns of PKB): https://github.com/zadam/trilium/wiki
- r/selfhosted showcase thread (real desktop screenshots): https://www.reddit.com/r/selfhosted/comments/1ed8h9c/triliumnext_notes_the_last_note_taking_app_you/
- TriliumDroid repo (mobile UI): https://github.com/Flomp/triliumdroid (UNVERIFIED exact URL — referenced from README issue #4962)
- r/selfhosted Aug 2025 update thread (new UI screenshots): https://www.reddit.com/r/selfhosted/comments/1mzeltd/trilium_notes_update/

### Docs analysis
- Governance change: original author zadam transferred the repository to the community project TriliumNext, which regained the "Trilium Notes" name; no migration steps needed from zadam/trilium, but sync versions later than v0.90.4 are incompatible, so desktop/server/TriliumDroid must match sync versions [https://github.com/orgs/TriliumNext/discussions/5867, https://github.com/TriliumNext/trilium].
- Feature surface: arbitrarily deep tree with cloning (one note in multiple places), WYSIWYG with markdown autoformat, source-code editing with syntax highlighting, note versioning, attributes for organization/querying/scripting, per-note encryption, self-hosted sync server, public note sharing, OpenID and TOTP login, REST API, scripting, scales to ~100,000 notes, Evernote/Markdown import-export, web clipper, Grafana metrics dashboard [https://github.com/TriliumNext/trilium].
- Docs live at docs.triliumnotes.org and are also embedded in-app via F1 — the same content served three ways [https://github.com/TriliumNext/trilium].
- AGPL-3.0; funded by donations to the lead maintainer (eliandoran), no paid tier, no feature walls [https://github.com/TriliumNext/trilium].
- Design decisions worth borrowing: (1) attributes (key=value labels) as a general-purpose metadata layer powering queries and scripts; (2) hoisting as a navigation paradigm for big trees; (3) per-note-type editors (canvas/mindmap/geo/table) inside one tree; (4) sync-version pinning discipline documented openly; (5) in-app help = online docs = repo docs, one source of truth.

### Features
| Area | Detail |
|---|---|
| Editor | CKEditor5 WYSIWYG + markdown autoformat; CodeMirror for code; Mermaid; Excalidraw canvas; Mind Elixir mind maps; Leaflet geo maps; Tabulator collections |
| Structure | Deep tree, cloning, hoisting, attributes, backlinks, note maps/relation maps, day notes/journals |
| Sync | Self-hosted sync server (Docker), third-party hosting services; version-pinned protocol |
| Security | Per-note encryption, OpenID, TOTP |
| Automation | REST API, scripting engine, user widgets, Grafana metrics |
| Platforms | Windows, macOS, Linux (binary/Flatpak), web (desktop-identical), mobile web, TriliumDroid/Pocket Trilium/Trinote |
| Pricing | Free, open-source, no paid tier |

### Sentiment
| What people say |
|---|
| Self-hosters love the depth: "no nags, no paywall, no restricted features", called "the last note taking app you should ever need" by fans [https://www.reddit.com/r/selfhosted/comments/1ed8h9c/triliumnext_notes_the_last_note_taking_app_you/] |
| Criticism: UI complexity and perceived slowness scare off newcomers; mobile historically clunky [https://www.reddit.com/r/selfhosted/comments/ygc757/selfhosted_webbased_notetaking_app_and_not_trilium/, https://www.reddit.com/r/selfhosted/comments/erfvyn/best_alternative_to_trilium/] |
| Long-standing gap: no offline-capable official mobile client (web app does not cache notes), driving demand for TriliumDroid/Trinote [https://www.reddit.com/r/Trilium/] |
| Sync-version coupling between server and Android app is an operational pain users must actively manage [https://www.reddit.com/r/selfhosted/comments/1mzeltd/trilium_notes_update/] |
| Homelab/knowledge-base users report very positive outcomes for structured technical notes [https://www.reddit.com/r/homelab/comments/1nyuw1w/trilium/] |

### Wants
| What people want changed |
|---|
| Easier first-party sync story and an official polished mobile app (offline-first); simpler onboarding UI; Mac-specific polish (original author publicly documented weak macOS integration) [https://www.reddit.com/r/PKMS/comments/1edd1dd/triliumnext_notes_the_last_personal_wiki_app_you/, https://github.com/zadam/trilium/wiki/FAQ/047d5f76a52eaaa9c5563ccba9581f6163d309ea] |

### Pricing and platforms
| Item | Detail |
|---|---|
| Cost | Free and open-source (AGPL-3.0); donations to maintainer [https://github.com/TriliumNext/trilium] |
| Platforms | Windows, macOS, Linux, web, mobile web; third-party native apps (TriliumDroid, Pocket Trilium, Trinote) [https://github.com/TriliumNext/trilium] |
| Self-host | First-class: server install, Docker image on Dockerhub [https://github.com/TriliumNext/trilium] |

### Contradictions
- The canonical repo is no longer zadam/trilium: ownership was transferred to the community (TriliumNext) and the project regained the Trilium name — earlier references to "zadam/trilium" URLs now resolve to community-maintained pages [https://github.com/orgs/TriliumNext/discussions/5867, https://github.com/TriliumNext/trilium].
- Old "Trilium is WYSIWYG-only, no source editing" claim (2018 review) is contradicted by the current feature list (CodeMirror source notes, markdown autoformat) [https://www.reddit.com/r/opensource/comments/a1fjr4/trilium_notes_is_an_foss_note_taking_application/, https://github.com/TriliumNext/trilium].

Sources: https://github.com/TriliumNext/trilium · https://github.com/orgs/TriliumNext/discussions/5867 · https://docs.triliumnotes.org · plus Reddit threads inline.

## AFFiNE

### Visual surface
Desktop/web (Electron + web): a sidebar with workspace switcher, favorites and a doc tree; two core view modes — "Page" (linear doc, Notion-like block editing with slash menu) and "Edgeless" (infinite whiteboard canvas where docs, sticky notes, shapes, embedded pages, databases and slides coexist); databases render as table/board (Kanban) views [https://github.com/toeverything/affine]. The visual style is close to Notion in docs mode and Miro/FigJam in Edgeless, with a strong "switch doc to canvas" toggle per page; dark mode and themes supported [https://betterstack.com/community/guides/linux/affine/]. Desktop app packaging ships the same UI offline-first via local storage [https://github.com/toeverything/affine]. Mobile: companion apps exist (iOS/Android readers/editors, historically weaker than desktop — UNVERIFIED current parity) [https://affine.pro/].

SHOT-LIST (prioritized):
- Homepage hero (Page + Edgeless split screenshots): https://affine.pro/
- Pricing page (plan comparison): https://affine.pro/pricing
- Repo README (feature bullets + demo GIFs): https://github.com/toeverything/AFFiNE
- Docs (self-host Docker guide, UI screenshots): https://docs.affine.pro/
- Better Stack guide (self-host screenshots): https://betterstack.com/community/guides/linux/affine/
- Product Hunt reviews page (user screenshots): https://www.producthunt.com/products/affine-2/reviews

### Docs analysis
- Positioning: "There can be more than Notion and Miro" — an all-in-one workspace fusing wiki docs, whiteboards, and databases on one edgeless canvas; blocks include rich text, sticky notes, embedded web pages, multi-view databases, linked pages, shapes, slides [https://github.com/toeverything/AFFiNE, https://raw.githubusercontent.com/toeverything/AFFiNE/canary/README.md].
- Architecture: BlockSuite (open editing toolkit, MIT-licensed editor) + OctoBase (open-source local-first collaborative database); local-first data ownership is an explicit design pillar [https://github.com/toeverything, https://deepwiki.com/toeverything/affine].
- Self-hosting via Docker is documented; the / command menu supports rich embeds (GitHub issues, Figma), and pasting URLs creates inline metadata embeds [https://betterstack.com/community/guides/linux/affine/].
- Pricing: Free, Pro, Team plans starting at $0; Pro primarily adds AI and cloud collaboration [https://affine.pro/pricing, https://www.fahimai.com/affine-pro]. Exact paid figures could not be confirmed from the fetched pricing page (JS-rendered) — UNVERIFIED.
- Design decisions worth borrowing: (1) one block model shared between doc and canvas views (doc-to-canvas is a mode switch, not a copy); (2) local-first sync engine (OctoBase) with CRDT collaboration; (3) databases as first-class blocks with multiple views; (4) plugin surface (BlockSuite) separate from app code.

### Features
| Area | Detail |
|---|---|
| Editor | Block-based docs (Notion-like), slash menu, embeds (GitHub, Figma, URLs), markdown shortcuts |
| Canvas | Edgeless infinite whiteboard; any block usable on canvas; frame/pen/shape tools; slides mode |
| Structure | Docs tree, favorites, tags (journal UNVERIFIED), databases with table/board views |
| Sync | Local-first; AFFiNE Cloud for cross-device + collaboration; self-host via Docker |
| AI | AFFiNE AI (writing/summarization) on paid tiers |
| Platforms | Windows, macOS, Linux, web, iOS/Android companions |
| Pricing | Free / Pro / Team |

### Sentiment
| What people say |
|---|
| Reviewers like the clean, offline-first blend of notes + canvas and doc-to-canvas switching; self-hosting and open-source roots called out positively [https://www.producthunt.com/products/affine-2/reviews] |
| Performance complaints recur: "pretty laggy compared to any other PKM software" on Edgeless canvases [https://www.reddit.com/r/PKMS/comments/1gcm3vj/appflowy_vs_affine/] |
| Data-egress anger: a PSA thread claims bulk import works but bulk export does not, framed as lock-in risk [https://www.reddit.com/r/PKMS/comments/1oaddib/psa_do_not_use_affine_underhanded_nonsense/] |
| Community concern about development pace: claims that several top committers stopped committing mid-2025 circulate in AppFlowy-vs-AFFiNE threads (contest by the project, treat as claim) [https://www.reddit.com/r/selfhosted/comments/1r74quv/appflowy_vs_affine_which_notion_alternative/] |
| Image-sync bugs (endless "loading image" after reinstall) reported in earlier years [https://www.reddit.com/r/Affine/] |

### Wants
| What people want changed |
|---|
| Bulk/"export all" to Markdown, better performance on large canvases, deeper third-party integrations, clearer cloud pricing value [https://www.reddit.com/r/PKMS/comments/1oaddib/psa_do_not_use_affine_underhanded_nonsense/, https://www.fahimai.com/affine-pro] |

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | Full local app + self-host; cloud workspace with limits [https://affine.pro/pricing] |
| Pro/Team | Paid cloud tiers adding AI + collaboration (exact prices UNVERIFIED from fetched page) [https://affine.pro/pricing] |
| Platforms | Windows, macOS, Linux, web, iOS/Android; Docker self-host [https://github.com/toeverything/AFFiNE, https://betterstack.com/community/guides/linux/affine/] |

### Contradictions
- "Privacy-first, local-first, open-source" branding vs user claims of missing bulk export and past image-sync bugs — the tension users cite most when leaving [https://www.reddit.com/r/PKMS/comments/1oaddib/psa_do_not_use_affine_underhanded_nonsense/].
- Dev-activity claims (top-10 devs inactive since Jun 2025) vs continued release activity per repo/third-party reviews; unresolved from search evidence alone [https://www.reddit.com/r/selfhosted/comments/1r74quv/appflowy_vs_affine_which_notion_alternative/, https://github.com/toeverything/affine].

Sources: https://github.com/toeverything/AFFiNE · https://affine.pro/pricing · https://betterstack.com/community/guides/linux/affine/ · plus Reddit/Product Hunt inline.

## ente

### Visual surface
Mobile-first (Flutter, Android/iOS): Ente Photos is a two-column photo grid with albums, a search bar (on-device ML search), and a bottom tab bar; the newer Ente Notes app is a minimal light/dark list editor for notes, tasks, files and a journal, sharing the same account and encryption layer [https://github.com/ente/ente, https://alternativeto.net/software/ente/about/]. Desktop and web (web.ente.com / photos.ente.com) mirror the photo grid; Ente Auth is a standalone 2FA app with a simple token list [https://github.com/ente/ente]. Branding is green-on-dark, minimal, with heavy emphasis on "end-to-end encrypted" badges in marketing screenshots [https://ente.com/#pricing]. Notes' visual surface is deliberately plain: title + body list, checklists, pinning — closer to Google Keep than to a knowledge base (UNVERIFIED beyond app-store descriptions) [https://alternativeto.net/software/ente/about/].

SHOT-LIST (prioritized):
- Ente homepage hero (photos grid + product family): https://ente.com/#pricing
- Repo README (product family overview, screenshots): https://github.com/ente/ente
- Help center (features pages with app screenshots): https://ente.com/help/photos/faq/storage-and-plans
- Notes app listing/screenshots (Play Store / App Store via ente.com): https://ente.com/
- Auth page: https://ente.com/auth (UNVERIFIED exact path — linked from repo README)
- r/enteio threads (real app screenshots): https://www.reddit.com/r/enteio/comments/1r9z2b2/i_love_ente_it_feels_too_good_to_be_true_whats/

### Docs analysis
- ente is an umbrella: E2EE cloud for photos (flagship), 2FA (Ente Auth, free forever), and newer encrypted products covering notes, tasks, files and journal — all on one account and one server ("museum"), a single self-contained Docker image [https://github.com/ente/ente, https://github.com/ente-io/ente/blob/main/server/README.md].
- Everything, including metadata, is encrypted on-device before upload; clients are open source (Dart/Flutter) and self-hosting the server is documented in the repo [https://github.com/ente/ente, https://github.com/ente-io/ente/blob/main/server/README.md, https://privacytools.io/app/ente].
- Pricing model: free 10 GB forever (raised from 5 GB in a 2024 pricing update), paid storage tiers, family plan sharing at no extra cost, referral program, and a legacy-contact feature for account handoff [https://ente.com/faq/subscription/forever-free-plan/, https://ente.com/blog/pricing-update/, https://ente.com/#pricing, https://ente.com/help/photos/features/account/].
- Third-party reviews frame it as "the private Google Photos"; the notes product rides the same subscription/storage pool (UNVERIFIED how notes count against quota) [https://privacytools.io/app/ente].
- Design decisions worth borrowing: (1) one encrypted account spanning multiple small apps (photos, auth, notes) instead of one monolith; (2) legacy contacts (digital inheritance) as a trust feature; (3) on-device AI search keeping metadata local; (4) transparent pricing-update blog posts explaining provider-cost economics; (5) replica storage (data kept in multiple locations) — UNVERIFIED current geography [https://ente.com/faq/subscription/forever-free-plan/].

### Features
| Area | Detail |
|---|---|
| Notes app | Notes, tasks/checklists, files, journal; E2EE, shared account with photos |
| Photos | Backup, albums, sharing, on-device ML search, memories, duplicate detection |
| Auth | Free standalone 2FA app with encrypted backup |
| Sync | Native apps across Android/iOS/web/desktop; background uploads |
| Security | E2EE incl. metadata; open-source clients; self-hostable server (museum Docker image) |
| Platforms | Android, iOS, web, desktop |
| Pricing | 10 GB free; paid storage tiers; family plan |

### Sentiment
| What people say |
|---|
| Overwhelmingly positive on value and privacy: "prices are just amazing", "best alternative to Google Photos" (Trustpilot, AlternativeTo) [https://www.trustpilot.com/review/ente.io, https://alternativeto.net/software/ente/about/] |
| "Feels too good to be true" thread: users probe jurisdictional risk — US entity/CLOUD Act access debates and forced-backdoor scenarios, even among fans [https://www.reddit.com/r/enteio/comments/1r9z2b2/i_love_ente_it_feels_too_good_to_be_true_whats/] |
| Older PrivacyGuides criticism about India incorporation and takedown clauses in terms; company has since shifted structure (UNVERIFIED current jurisdiction) [https://www.reddit.com/r/PrivacyGuides/comments/rjzc9s/compare_cryptee_and_enteio/] |
| Notes specifically: mentioned as part of the appeal ("encrypted home for your notes, tasks, files, and journal") but little dedicated discussion volume vs photos — most sentiment is photo-centric [https://alternativeto.net/software/ente/about/] |

### Wants
| What people want changed |
|---|
| Clearer legal/jurisdictional assurances; more notes-app maturity and feature depth to match dedicated note apps; self-host setup docs described as sparse by a third-party review [https://www.reddit.com/r/enteio/comments/1r9z2b2/i_love_ente_it_feels_too_good_to_be_true_whats/, https://hysenlabs.com/en/projects/ente-ente] |

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | 10 GB forever, E2EE, on-device AI search [https://ente.com/faq/subscription/forever-free-plan/] |
| Paid | Storage tiers; family plan at no extra cost; pricing recalibrated downward in 2024 update [https://ente.com/#pricing, https://ente.com/blog/pricing-update/] |
| Self-host | Server repo + single Docker image; third-party review says instructions are thin [https://github.com/ente-io/ente/blob/main/server/README.md, https://hysenlabs.com/en/projects/ente-ente] |
| Platforms | Android, iOS, web, desktop; Ente Auth on mobile + desktop [https://github.com/ente/ente] |

### Contradictions
- Repo identity: the assigned URL ente-io/ente now coexists with a renamed org at ente/ente (search shows both; GitHub redirects) — references should use the current canonical repo [https://github.com/ente/ente, https://github.com/ente-io/ente].
- "Free forever" marketing vs the earlier 5 GB then 10 GB rebalancing — free tier is real but its size is a business decision the company has changed at least once [https://ente.com/blog/pricing-update/, https://ente.com/faq/subscription/forever-free-plan/].

Sources: https://github.com/ente/ente · https://ente.com/faq/subscription/forever-free-plan/ · https://ente.com/blog/pricing-update/ · https://www.trustpilot.com/review/ente.io · plus Reddit threads inline.

## Heptabase

### Visual surface
Desktop (macOS/Windows/Linux; closed-source): the core surface is infinite-canvas whiteboards populated by draggable cards; cards open into a Notion-like block editor; a right pane hosts "workflows" (queries by tag/property) and a journal view; PDFs open in a reader pane with highlight and margin-note tools, and highlights drag onto the board as cards [https://toolstack.io/tools/heptabase, https://www.reddit.com/r/PKMS/comments/1bt0suo/unleashing_the_mind_heptabase/]. Dark/light themes, minimal chrome, unusually polished visual design; the same card appears on multiple whiteboards via reusability [https://toolguide.io/en/tool/heptabase/]. Mobile apps exist (iOS App Store reviews from 2026 show iPhone/Pad usage; Android historically later), but reviewers describe them as behind desktop [https://apps.apple.com/us/app/heptabase/id6445801508?see-all=reviews&platform=iphone, https://www.reddit.com/r/PKMS/comments/1bt0suo/unleashing_the_mind_heptabase/]. Marketing site leads with a big animated canvas screenshot and study-workflow demos [https://heptabase.com].

SHOT-LIST (prioritized):
- Homepage hero (infinite canvas demo): https://heptabase.com
- Pricing page: https://heptabase.com/pricing
- App Store listing (iOS screenshots): https://apps.apple.com/us/app/heptabase/id6445801508
- Litmus review (AI chat on whiteboard screenshots): https://litmustools.com/review/heptabase/
- MakerStack review (full feature screenshots): https://makerstack.co/reviews/heptabase-review/
- r/heptabase showcase threads: https://www.reddit.com/r/heptabase/comments/1nvysr9/what_are_good_and_bad_things_about_heptabase_in/

### Docs analysis
- Core model: whiteboards of reusable cards; one card can appear on multiple boards and edits propagate everywhere — a deliberate anti-duplication design decision [https://toolguide.io/en/tool/heptabase/, https://aitoolscoop.com/tool/heptabase/].
- PDF-centric research loop: import PDFs, highlight, add margin notes, then convert highlights into cards that connect to concepts — the single most-praised workflow in reviews [https://toolstack.io/tools/heptabase, https://aitoolscoop.com/tool/heptabase/].
- Local-first with real-time sync; offline editing and full-text search without internet; JSON export plus Markdown export (lossy for board context) [https://slashdot.org/software/p/Heptabase/, https://www.reddit.com/r/PKMS/comments/1cdqsu6/heptabase_review_9_months_in/].
- AI: conversational AI Chat over your own cards, annotated PDFs and imported YouTube transcripts, context-bound to a whiteboard; transcription for audio/video; premium tiers gate higher AI allowances and unlimited PDF uploads [https://litmustools.com/review/heptabase/, https://toolchase.com/tool/heptabase/].
- Integrations: Readwise import; Zotero integration on roadmap; MCP protocol support listed (UNVERIFIED maturity) [https://toolguide.io/en/tool/heptabase/, https://chiri.ai/chiri-atlas/heptabase-ai].
- No free tier; 7-day trial; pricing moved to three tiers (Pro/Premium/Premium+) with early-bird grandfathering [https://makerstack.co/reviews/heptabase-review/, https://toolchase.com/tool/heptabase/].
- Design decisions worth borrowing: (1) cards as reusable objects with multi-board presence; (2) PDF highlights as first-class atoms that become notes; (3) whiteboard-context AI (the model sees what you see); (4) workflows pane (structured queries on the right) as a navigation layer over the canvas; (5) single-price simplicity (no feature gating historically) [https://makerstack.co/reviews/heptabase-review/].

### Features
| Area | Detail |
|---|---|
| Editor | Block-based card editor, bi-directional links [https://siteefy.com/tools/heptabase] |
| Canvas | Infinite whiteboards; drag-drop cards/images; frames |
| Research | PDF reader/annotation, highlights-to-cards, audio/video transcription, YouTube import [https://toolstack.io/tools/heptabase, https://chiri.ai/chiri-atlas/heptabase-ai] |
| AI | AI Chat over own knowledge base; premium AI models on higher tiers [https://litmustools.com/review/heptabase/] |
| Sync | Real-time, local-first, offline search [https://slashdot.org/software/p/Heptabase/] |
| Platforms | Windows, macOS, Linux, web, iOS, Android |
| Pricing | 7-day trial; three paid tiers, no free plan [https://toolchase.com/tool/heptabase/] |

### Sentiment
| What people say |
|---|
| Strongest niche: visual learners and researchers; "easy to visualize what I'm trying to learn", workflows pane called the killer feature [https://apps.apple.com/us/app/heptabase/id6445801508?see-all=reviews&platform=iphone, https://www.reddit.com/r/PKMS/comments/1bt0suo/unleashing_the_mind_heptabase/] |
| Feature-poor vs generalists: intentionally narrow; users keep a second system for tasks/wiki [https://www.reddit.com/r/PKMS/comments/16341ft/heptabase_review/] |
| Price plus lock-in: MD export "works OK" but loses context; JSON is proprietary backup — Obsidian users cite this as the main drawback [https://www.reddit.com/r/ObsidianMD/comments/1i6sppl/i_really_like_heptabase/] |
| 2025 sentiment shift: academics left over the AI push ("chase for AI" at the expense of core development) [https://www.reddit.com/r/heptabase/comments/1nvysr9/what_are_good_and_bad_things_about_heptabase_in/] |
| Mobile lags desktop; drag-drop image handling friction [https://www.reddit.com/r/PKMS/comments/1bt0suo/unleashing_the_mind_heptabase/] |

### Wants
| What people want changed |
|---|
| Fidelity-preserving export, smoother image drag-drop, less AI-first roadmap, better mobile parity [https://www.reddit.com/r/ObsidianMD/comments/1i6sppl/i_really_like_heptabase/, https://www.reddit.com/r/heptabase/comments/1nvysr9/what_are_good_and_bad_things_about_heptabase_in/] |

### Pricing and platforms
| Item | Detail |
|---|---|
| Older pricing | $9.99/mo monthly, $7.99/mo annual ($95.88/yr), single tier, 7-day trial, no free plan [https://makerstack.co/reviews/heptabase-review/] |
| Newer pricing | Pro $11.99/mo ($8.99 annual), Premium $23.99/mo ($17.99), Premium+ $71.99/mo ($53.99); early-bird grandfathered at $9.99/mo / $83.88/yr [https://toolchase.com/tool/heptabase/] |
| Platforms | Windows, macOS, Linux, web, iOS, Android [https://slashdot.org/software/p/Heptabase/] |
| Self-host | None (closed-source, cloud sync only) |

### Contradictions
- Pricing: one-tier $9.99/$7.99 (MakerStack, March 2026) vs three-tier Pro/Premium/Premium+ with different prices (ToolChase, Sept 2026) — a 2026 restructuring; official page needed to arbitrate [https://makerstack.co/reviews/heptabase-review/, https://toolchase.com/tool/heptabase/].
- "Lack of mobile apps" (Tool Finder, Sept 2026) contradicted by the App Store listing with active 2026 reviews — mobile exists but is rated weaker than desktop [https://toolfinder.com/alternatives/heptabase, https://apps.apple.com/us/app/heptabase/id6445801508?see-all=reviews&platform=iphone].

Sources: https://heptabase.com · https://toolstack.io/tools/heptabase · https://toolchase.com/tool/heptabase/ · https://makerstack.co/reviews/heptabase-review/ · plus Reddit/App Store inline.

## Kinopio

### Visual surface
Web-first (with iOS app): a hand-drawn, illustrated spatial canvas — painterly backgrounds, a frog mascot, sticker-like cards you tap anywhere to type into; cards hold text, URLs (which play embedded YouTube), images, files/PDFs, and color swatches, connected by draggable connector lines; spaces are pannable/zoomable boards [https://kinopio.club/, https://kinopio.club/help/, https://help.kinopio.club/about/]. The aesthetic is deliberately warm, playful and personal ("embraces individuality and personality. Made for people, not drones" per the homepage) [https://kinopio.club/]. UI details: a bottom toolbar, an inbox/search panel for moving between spaces, user presence indicators for collaboration, and tag groups for [[tags]] [https://github.com/kinopio-club/kinopio-client, https://help.kinopio.club/about/]. iOS app uses a hybrid architecture (documented in a 2023 HN post) [https://news.ycombinator.com/item?id=40810949].

SHOT-LIST (prioritized):
- Homepage hero (spatial canvas demo): https://kinopio.club/
- About page (philosophy + canvas screenshots): https://kinopio.club/about
- Help center (guides with UI screenshots): https://kinopio.club/help/
- Pricing post: https://kinopio.club/help/posts/how-much-does-kinopio-cost/
- GitHub client repo (UI code + screenshots): https://github.com/kinopio-club/kinopio-client
- Product Hunt reviews (user screenshots): https://www.producthunt.com/products/kinopio/reviews

### Docs analysis
- Core interaction: tap anywhere to type; paste URLs into cards; drag connectors between cards; drag in files (PDFs); [[tags]] categorize and group concepts; spaces are canvases you organize spatially [https://kinopio.club/help/, https://help.kinopio.club/about/].
- Pricing is usage-based: all features free up to 100 cards and 5 MB uploads; a subscription lifts the limits; iOS in-app price is higher to cover Apple's fees [https://kinopio.club/help/posts/how-much-does-kinopio-cost/].
- Solo-founder product, solely supported by users; no investors; feature additions gated by fit ("only add features that... truly help its users") [https://kinopio.club/].
- Source code public since June 2024 (kinopio-client repo) — open-source-curious but not advertised as self-hostable; media on a third-party CDN; server URL surfaced in browser logs of the client [https://news.ycombinator.com/item?id=40810949, https://github.com/kinopio-club/kinopio-client].
- Design decisions worth borrowing: (1) zero-signup entry (play before account creation) [https://toolfinder.net/tool/kinopio]; (2) cards as tiny polymorphic objects (text/URL/image/color/file) rather than pages; (3) spatial memory as the retrieval mechanism (the about page argues spatial organization reduces procrastination/anxiety); (4) pricing tied to card count, a simple and legible meter; (5) personality-first UI as differentiation in a sea of gray tools.

### Features
| Area | Detail |
|---|---|
| Editor | Card-based; text, lists, URLs, images, files, colors; inline [[tags]] |
| Canvas | Infinite spatial spaces; connector lines; zoom/pan; groupings |
| Collaboration | Shared spaces with presence indicators; public sharing |
| Mobile | iOS app (hybrid architecture); web app elsewhere |
| Pricing | Free ≤100 cards; paid beyond; Apple-fee uplift on iOS |
| Self-host | Client code public; no documented self-host path |

### Sentiment
| What people say |
|---|
| Aesthetic-driven love: "playful and beautiful design" that makes hard thinking feel creative (Product Hunt) and mindmapping users "kind of obsessed" [https://www.producthunt.com/products/kinopio/reviews, https://www.reddit.com/r/mindmapping/comments/k098vj/kinopioclub_visual_thinking_brainstorming_tool/] |
| Perceived as "too casual, not serious" by some evaluators comparing against Obsidian-class tools [https://www.saashub.com/kinopio] |
| Recommendation pattern: people who outgrow it substitute Obsidian + Excalidraw for work use — a capability ceiling, not a quality complaint [https://news.ycombinator.com/item?id=40666348] |
| Founder responsiveness on HN noted positively; annual solo-dev rhythm visible in HN threads [https://news.ycombinator.com/item?id=31460626, https://www.saashub.com/kinopio] |

### Wants
| What people want changed |
|---|
| Export/backup depth, self-hosting or clearer data ownership, more "serious work" structure features (tables, better linking) — drawn from HN comparisons; specific threads are thin, so treat wants as low-confidence [https://news.ycombinator.com/item?id=40666348] |

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | All features, ≤100 cards, ≤5 MB uploads [https://kinopio.club/help/posts/how-much-does-kinopio-cost/] |
| Paid | Subscription removes limits; slightly higher price in iOS app [https://kinopio.club/help/posts/how-much-does-kinopio-cost/] |
| Platforms | Web (any browser), iOS app [https://kinopio.club/] |
| Self-host | None documented; client source public [https://github.com/kinopio-club/kinopio-client] |

### Contradictions
- "Open source" label (repo public since 2024) vs no self-host offer and cloud-only media — worth pinning as source-available rather than self-hostable FOSS [https://news.ycombinator.com/item?id=40810949, https://github.com/kinopio-club/kinopio-client].
- Commonly compared to whiteboards as a brainstorming toy vs its own positioning as a long-term thinking tool with spatial memory retention [https://kinopio.club/about].

Sources: https://kinopio.club/ · https://kinopio.club/help/posts/how-much-does-kinopio-cost/ · https://help.kinopio.club/about/ · https://github.com/kinopio-club/kinopio-client · plus HN/Reddit inline.

## tldraw

### Visual surface
Web app (tldraw.com) and embeddable React SDK: a crisp, dark-chrome infinite canvas with a floating style panel, shape toolbar (select, draw, eraser, arrow, text, geo, note, line, frame), and a top-left menu; UI is deliberately playful ("Make pollution, make silly shapes", unique cursor animations), buttery zoom/pan, keyboard-shortcut-heavy [https://freealternatives.to/tldraw/review, https://www.reddit.com/r/webdev/comments/qwovzg/tldraw_a_tiny_little_drawing_app_just_released/]. Elements are React components in the SDK, so embedded canvases can hold arbitrary web content [https://sourceforge.net/software/product/tldraw-computer/]. The marketing site is minimal with a full-bleed interactive canvas as the hero [https://tldraw.com]. "Computer" mode adds prompt/sketch-to-app frames that render working HTML/React/SVG output on the canvas [https://aitoolsatlas.ai/tools/tldraw/review]. No native desktop/mobile clients for the public app (PWA-like browser use; UNVERIFIED PWA status) [https://freealternatives.to/tldraw/review].

SHOT-LIST (prioritized):
- Homepage (live canvas as hero): https://tldraw.com
- Docs landing (SDK screenshots): https://tldraw.dev/
- Examples page (example apps): https://tldraw.dev/examples
- License page (watermark policy): https://tldraw.dev/community/license
- License key page (commercial licensing): https://tldraw.dev/sdk-features/license-key
- GitHub README (logo, used-by list, GIFs): https://github.com/tldraw/tldraw

### Docs analysis
- Primary product is a React SDK for infinite-canvas apps; the public whiteboard is the showcase [https://github.com/tldraw/tldraw, https://sourceforge.net/software/product/tldraw-computer/].
- License is the headline design fact: since v3.0 (Sept 2024) the SDK is source-available under the tldraw SDK License (not OSI open source); free with the "Made with tldraw" watermark; hobby license keeps watermark; commercial license (price by quote) removes it and is required for production commercial use; free 100-day trial license for evaluation [https://github.com/tldraw/tldraw/blob/main/LICENSE.md, https://tldraw.dev/community/license, https://tldraw.dev/sdk-features/license-key, https://meetrix.io/blogs/open-source-whiteboard-tools/].
- Includes a multiplayer sync server option; docs cover examples and API thoroughly [https://github.com/api-evangelist/tldraw].
- Design decisions worth borrowing: (1) every canvas element is a React component — extension via normal web tech; (2) watermark-as-monetization for an SDK business; (3) licensing state enforced in-code (env-checked license keys); (4) example-led documentation; (5) instant-no-signup free tool as the top of a commercial funnel [https://freealternatives.to/tldraw/review].
- Limits: public whiteboard has no published board/collaborator limits as of July 2026 [https://freealternatives.to/tldraw/review].

### Features
| Area | Detail |
|---|---|
| Canvas | Infinite, buttery pan/zoom; shapes, notes, arrows, frames, freehand with smoothing |
| SDK | React components per shape, custom shapes, rich API, multiplayer sync server |
| AI | "Computer" prompt/sketch-to-app generation on canvas; Deepmind/Gemini collaboration announced [https://aitoolsatlas.ai/tools/tldraw/review, https://www.reddit.com/r/webdev/comments/qwovzg/tldraw_a_tiny_little_drawing_app_just_released/] |
| Platforms | Web app; SDK for embedding in web apps |
| Pricing | Free whiteboard; SDK free-with-watermark; paid commercial/hobby licenses |
| Files | Board persistence via cloud (no published limits) |

### Sentiment
| What people say |
|---|
| Near-universal praise of feel: "a really nice little drawing app... so hard to make something that feels simple and intuitive" (653 upvotes on r/webdev launch) [https://www.reddit.com/r/webdev/comments/qwovzg/tldraw_a_tiny_little_drawing_app_just_released/] |
| Developers describe it as "one of the best pieces of software ever created" for architecture comms and planning (Product Hunt 2026) [https://www.producthunt.com/products/tldraw/reviews] |
| Developers' first question is licensing: "should I use tldraw, excalidraw or build from scratch" — watermark and quote-based pricing create friction for startups [https://www.reddit.com/r/hackernews/comments/qwnbvq/tldraw_a_tiny_little_drawing_app/, https://tldraw.dev/sdk-features/license-key] |
| vs Excalidraw debates: tldraw wins on polish/SDK, Excalidraw wins on open-source ethos and easy clipboard export [https://www.reddit.com/r/ObsidianMD/comments/1b4k5l7/tldraw_vs_excalidraw_are_they_both_similar/] |

### Wants
| What people want changed |
|---|
| Clearer/cheaper licensing for indie and small commercial use; better export workflows (clipboard export praised in Excalidraw is a tldraw gap per users) [https://www.reddit.com/r/ObsidianMD/comments/1b4k5l7/tldraw_vs_excalidraw_are_they_both_similar/, https://www.reddit.com/r/hackernews/comments/qwnbvq/tldraw_a_tiny_little_drawing_app/] |

### Pricing and platforms
| Item | Detail |
|---|---|
| Whiteboard app | Free, no published limits, no paid tier for the app itself [https://freealternatives.to/tldraw/review] |
| SDK | Free in dev; hobby license (watermark); commercial license by quote; 100-day trial [https://meetrix.io/blogs/open-source-whiteboard-tools/, https://tldraw.dev/sdk-features/license-key] |
| Platforms | Web; embeddable React SDK [https://github.com/tldraw/tldraw] |
| Self-host | Sync server available; SDK license governs; not OSI open source [https://github.com/api-evangelist/tldraw] |

### Contradictions
- Frequently called "open source" in comparisons — the project itself says source-available under a custom license, not OSI open source, and requires paid licenses for commercial production use [https://github.com/api-evangelist/tldraw, https://tldraw.dev/community/license].
- README tagline ("World's best, top-most agent recommended #1 five star SDK") is a joke about AI-recommendation economy that some aggregators list literally — treat vendor marketing claims with that lens [https://github.com/tldraw/tldraw].

Sources: https://github.com/tldraw/tldraw · https://tldraw.dev/community/license · https://tldraw.dev/sdk-features/license-key · https://freealternatives.to/tldraw/review · plus Reddit/HN inline.

## Excalidraw

### Visual surface
Web-first (excalidraw.com): a light, friendly infinite canvas with a hand-drawn sketch aesthetic on every stroke; left vertical toolbar (selection, hand, draw, shapes, text, image, eraser, laser), top-right collaborative buttons, and a floating properties panel; exports to PNG/SVG/clipboard preserve the sketch style [https://github.com/excalidraw/excalidraw, https://www.eli.work/tool/excalidraw-plus]. Excalidraw+ adds a workspace shell: drawing library, folder organization, access controls, voice hangout, presentation mode [https://plus.excalidraw.com/plus]. The Obsidian plugin is a much bigger beast: a full canvas with markdown-to-diagram transclusion, script engine, and Obsidian-vault integration inside the editor pane [https://www.obsidianstats.com/plugins/obsidian-excalidraw-plugin]. No official native desktop/mobile app; embeddable via npm into any app [https://github.com/excalidraw/excalidraw].

SHOT-LIST (prioritized):
- Homepage (canvas live demo): https://excalidraw.com
- GitHub README (badges, screenshots): https://github.com/excalidraw/excalidraw
- Excalidraw+ landing (workspace UI): https://plus.excalidraw.com/plus
- Excalidraw+ pricing page: https://plus.excalidraw.com/pricing
- Obsidian plugin repo (screenshots/GIFs of vault-integrated canvas): https://github.com/zsviczian/obsidian-excalidraw-plugin
- Docs (embed instructions): https://docs.excalidraw.com (UNVERIFIED exact path)

### Docs analysis
- MIT-licensed, truly open-source core; excalidraw.com is described by the project as "a minimal showcase" of the npm package — the package is the real product [https://github.com/excalidraw/excalidraw].
- Real-time collaboration with end-to-end encryption on shareable room links in the free app; no account required to draw [https://github.com/excalidraw/excalidraw, https://doolpa.com/article/excalidraw].
- Excalidraw+ adds: workspace/drawing organization, enhanced sharing and access control, presentation and voice features, 14-day trial, $6/user/mo annual or $7 monthly [https://plus.excalidraw.com/plus, https://plus.excalidraw.com/pricing].
- Monorepo includes exports to PNG/SVG/clipboard, i18n, mermaid-to-excalidraw converter, math, utils packages; Plus-only features will become drop-in plugins for the npm package (stated roadmap) [https://github.com/excalidraw/excalidraw].
- Obsidian plugin (separate project by Zsolt Viczián): scriptable, markdown-embeds, PDF export via Electron IPC, dynamically loads Excalidraw React components; flagged in Obsidian's 2026 security-review changes as non-compliant with newer community-plugin policies (legacy grandfathered plugin) [https://community.obsidian.md/plugins/obsidian-excalidraw-plugin, https://forum.obsidian.md/t/obsidian-excalidraw-extension-is-unsecure-how/114226].
- Design decisions worth borrowing: (1) zero-friction anonymous use before any account; (2) E2EE room links for ephemeral collaboration; (3) hand-drawn style as a deliberate signal that drawings are provisional; (4) showcase-app-plus-SDK split letting integrators own storage; (5) plugin/community porting rather than building native desktop apps.

### Features
| Area | Detail |
|---|---|
| Canvas | Infinite, hand-drawn style shapes, text, images, frames; laser pointer |
| Collaboration | Real-time E2EE rooms via link; live cursors |
| Export | PNG, SVG, clipboard, .excalidraw JSON |
| SDK | npm package, embeddable component, docs [https://github.com/excalidraw/excalidraw] |
| Plus tier | Workspace, folders, access control, presentations, voice [https://plus.excalidraw.com/plus] |
| Platforms | Web (app + SDK); third-party Obsidian plugin; no native apps |

### Sentiment
| What people say |
|---|
| Loved for simplicity and speed of sketching; "frictionless onboarding, real-time collaboration" drives an 85/100 third-party score [https://doolpa.com/article/excalidraw] |
| Chosen over tldraw for open-source ethos and quick clipboard export (Obsidian community debates) [https://www.reddit.com/r/ObsidianMD/comments/1b4k5l7/tldraw_vs_excalidraw_are_they_both_similar/] |
| Obsidian plugin users get near-Heptabase workflows but report bugs (PDF export broken in Obsidian's PDF flow) and security-policy non-compliance concerns [https://github.com/zsviczian/obsidian-excalidraw-plugin/issues/2292, https://forum.obsidian.md/t/obsidian-excalidraw-extension-is-unsecure-how/114226] |
| Mermaid-to-Excalidraw conversion called out as a standout feature by Plus users [https://plus.excalidraw.com/plus] |

### Wants
| What people want changed |
|---|
| Plus features open to the free SDK sooner (roadmap says drop-in plugins); native desktop/offline story; better PDF export in the Obsidian plugin [https://github.com/excalidraw/excalidraw, https://github.com/zsviczian/obsidian-excalidraw-plugin/issues/2292] |

### Pricing and platforms
| Item | Detail |
|---|---|
| Free app | Full editor, collaboration, no account needed [https://github.com/excalidraw/excalidraw] |
| Excalidraw+ | $6/user/mo annual, $7 monthly, 14-day trial [https://plus.excalidraw.com/pricing] |
| SDK | Free npm package, MIT [https://github.com/excalidraw/excalidraw] |
| Self-host | Fully self-hostable (MIT core); no vendor lock-in [https://www.ai-tools-hq.com/tools/excalidraw/] |

### Contradictions
- Excalidraw is frequently used as shorthand for "free open-source whiteboard" — true for the editor, but collaboration features and organizational tools sit in the paid Plus tier, and the free site's rooms are ephemeral; users expecting persistent shared spaces from the free app hit a wall [https://github.com/excalidraw/excalidraw, https://plus.excalidraw.com/plus].
- The huge Obsidian plugin is commonly assumed to be official; it is an independent community project (zsviczian) with its own scope and policy-compliance issues [https://affine.pro/blog/excalidraw-vs-obsidian, https://forum.obsidian.md/t/obsidian-excalidraw-extension-is-unsecure-how/114226].

Sources: https://github.com/excalidraw/excalidraw · https://plus.excalidraw.com/pricing · https://plus.excalidraw.com/plus · https://github.com/zsviczian/obsidian-excalidraw-plugin · plus Reddit/forum inline.

## Saber

### Visual surface
Flutter-based, so UI is identical across Android/iOS/Windows/macOS/Linux/web: a simple file-manager home screen with folders and recent notes, and an editor that is a single white (or darkened) page with a pen/highlighter toolbar (color, size, eraser, lasso) and little else — closer to Xournal++ than to a text editor; notes are handwriting strokes plus imported PDF backgrounds you annotate over [https://saber.adil.hanney.org/, https://github.com/saber-notes/saber]. Night mode darkens the note paper itself, not just the chrome — a documented deliberate choice [https://saber.adil.hanney.org/]. No knowledge-graph, markdown, or database surfaces at all; the entire visual surface is folders → pages → strokes [https://saber.adil.hanney.org/].

SHOT-LIST (prioritized):
- Official site (feature carousel screenshots): https://saber.adil.hanney.org/
- GitHub README (platform badges, screenshots): https://github.com/saber-notes/saber
- Google Play listing (tablet screenshots): https://play.google.com/store/apps/details?id=com.adilhanney.saber
- App Store listing (iPad screenshots): https://apps.apple.com/us/app/saber-handwritten-notes/id1671523739
- GitHub issues (real bug screenshots of UI): https://github.com/saber-notes/saber/issues
- r/GalaxyTab latency comparison thread (Saber among tested apps): https://www.reddit.com/r/GalaxyTab/comments/1swqxa4/i_compared_the_pen_latency_in_eleven_notetaking/

### Docs analysis
- Pitch: "the notes app built for handwriting"; cross-platform (Android, iOS, Windows, macOS, Linux, web) with sync across all of them; free and open-source (GPLv3 per LinuxLinks) [https://github.com/saber-notes/saber, https://www.linuxlinks.com/saber-notes-app-handwriting/].
- Privacy stance: E2EE sync where "not even the server can read them"; sync options include Nextcloud and Saber's own relay infrastructure (Manjaro forum and repo confirm Nextcloud sync; a self-hostable relay/nextcloud app exists) [https://saber.adil.hanney.org/, https://forum.manjaro.org/t/saber-cross-platform-handwritten-notes-app-with-sync/137931].
- Feature set: unlimited nested folders, recent-notes home, non-overlapping highlighter that renders under strokes, PDF import/annotation, night mode that inverts the page, password protection of notes, image insertion (per HelloGitHub review) [https://saber.adil.hanney.org/, https://hellogithub.com/en/repository/saber-notes/saber].
- AlternativeTo's project description still says "work-in-progress... not ready to trust with your notes yet" — the maturity framing is contested below [https://alternativeto.net/software/saber-handwritten-notes/about/].
- Design decisions worth borrowing: (1) highlighter that never darkens on overlap (small but beloved detail); (2) dark mode that darkens the paper; (3) BYO-sync via Nextcloud with E2EE, matching a privacy-first stack; (4) handwriting-first with zero text-editor surface — a focused scope in a category bloated with features.

### Features
| Area | Detail |
|---|---|
| Editor | Pen/highlighter/eraser/lasso; PDF import and annotation; images |
| Structure | Unlimited nested folders; recent notes on home |
| Sync | Cross-device E2EE sync; Nextcloud support; Saber relay (self-hostable) |
| Security | Encrypted storage/sync; password protection per notes |
| Platforms | Android, iOS, Windows, macOS, Linux (AppImage/Flatpak/Snap), web |
| Pricing | Free, open-source (GPLv3); optional hosted sync |

### Sentiment
| What people say |
|---|
| Recurring praise: one of the few genuinely cross-platform handwriting apps for Linux users; distribution packaging (AppImage/Flatpak/Snap) welcomed [https://forum.manjaro.org/t/saber-cross-platform-handwritten-notes-app-with-sync/137931] |
| Bug-driven criticism from 2025: lasso regression and glitches broke a semester of use for one App Store reviewer after a stable 2024 [https://apps.apple.com/us/app/saber-handwritten-notes/id1671523739] |
| Desktop drawing bugs (lines, autosave) annoy early Linux adopters [https://www.reddit.com/r/linux4noobs/comments/1cyakv3/any_good_notetaking_applications_with_handwriting/] |
| Pen latency: in a 2026 eleven-app comparison, Samsung Notes led; Saber's category is performance-sensitive and latency is the decisive metric (Saber tested in the same methodology) [https://www.reddit.com/r/GalaxyTab/comments/1swqxa4/i_compared_the_pen_latency_in_eleven_notetaking/] |
| Positioned against Xournal++, Rnote, Linwood Butterfly as its closest peers [https://alternativeto.net/software/saber-handwritten-notes/] |

### Wants
| What people want changed |
|---|
| Stability and mature text/OCR features; better desktop pen handling; fixes to autosave behavior [https://www.reddit.com/r/linux4noobs/comments/1cyakv3/any_good_notetaking_applications_with_handwriting/, https://apps.apple.com/us/app/saber-handwritten-notes/id1671523739] |

### Pricing and platforms
| Item | Detail |
|---|---|
| Cost | Free, open-source (GPLv3) [https://www.linuxlinks.com/saber-notes-app-handwriting/] |
| Sync service | Nextcloud or Saber relay; E2EE; self-host supported [https://saber.adil.hanney.org/, https://forum.manjaro.org/t/saber-cross-platform-handwritten-notes-app-with-sync/137931] |
| Platforms | Android, iOS, Windows, macOS, Linux, web [https://github.com/saber-notes/saber] |

### Contradictions
- Maturity: AlternativeTo's description calls it a work-in-progress not ready to trust, while the project ships stable releases (Aug 2026) across seven platforms and has real multi-semester classroom users — a stale description vs current reality [https://alternativeto.net/software/saber-handwritten-notes/about/, https://github.com/saber-notes/saber/releases, https://apps.apple.com/us/app/saber-handwritten-notes/id1671523739].

Sources: https://github.com/saber-notes/saber · https://saber.adil.hanney.org/ · https://forum.manjaro.org/t/saber-cross-platform-handwritten-notes-app-with-sync/137931 · https://www.linuxlinks.com/saber-notes-app-handwriting/ · plus App Store/Reddit inline.

## Lockbook

### Visual surface
Native apps on every platform (iOS App Store, Google Play, desktop, web at app.lockbook.net, plus a CLI): a file-tree sidebar with folders, a Markdown editor pane, and an SVG drawing canvas; the design language is quiet and utilitarian — plain folders, plain Markdown, no badges or gamification [https://lockbook.net/, https://github.com/lockbook/lockbook]. The marketing site is text-first, structured around three universality claims (Markdown, SVG, folders) [https://lockbook.net/]. The CLI surfaces no GUI at all: fzf search, $EDITOR editing, and a FUSE-style mount of the whole book as a drive [https://lockbook.net/, https://github.com/lockbook/lockbook]. Mobile screenshots on store listings show the folder tree + editor split with a sync shield icon (UNVERIFIED icon detail) [https://apps.apple.com/us/app/lockbook/id1526775001].

SHOT-LIST (prioritized):
- Official homepage: https://lockbook.net/
- GitHub README (architecture diagram, platform list): https://github.com/lockbook/lockbook
- App Store listing (iOS screenshots): https://apps.apple.com/us/app/lockbook/id1526775001
- Google Play listing (Android screenshots): https://play.google.com/store/apps/details?id=app.lockbook
- Docs (collaboration/sharing page): https://lockbook.net/docs/collaboration.html
- r/macapps launch thread (user-side screenshots): https://www.reddit.com/r/macapps/comments/1qnwtnj/os_lockbook_an_open_source_endtoend_encrypted/

### Docs analysis
- Data model is deliberately universal: Markdown notes, SVG drawings, plain folders — "the universal language" framing means exports are lossless and boring by design; app also previews photos/PDFs and stores arbitrary files [https://lockbook.net/].
- E2EE on-device, sync by invitation-only sharing, no data collection; self-described as "for people with better things to worry about than privacy" — privacy as default rather than a mode [https://alternativeto.net/software/lockbook/about/].
- Developer surface is a differentiator: CLI with Unix-pipe ergonomics, Rust library (lb-rs) with C and Java bindings, a mount-as-drive mode (lockbook fs), cron-able backups [https://github.com/lockbook/lockbook].
- Collaboration: external links in the form app.lockbook.net/uuid currently work only on Apple clients; cross-platform link support is in progress (a hard, honest limit documented in docs) [https://lockbook.net/docs/collaboration.html].
- Rust core with a custom embedded database (org repos include an embedded Rust DB); multi-client sync engineering is the project's visible investment [https://github.com/lockbook, https://github.com/lockbook/lockbook].
- Design decisions worth borrowing: (1) storage formats chosen so a plain file browser can read the export; (2) invitation-based sharing (no public links by default) as a privacy posture; (3) CLI + library + mount giving the same encrypted book three interfaces; (4) flat single premium tier ($2.99/mo, 30 GB) — one price, one feature (space), no feature gating [https://alternativeto.net/software/lockbook/about/, https://apps.apple.com/us/app/lockbook/id1526775001].

### Features
| Area | Detail |
|---|---|
| Editor | Markdown notes; SVG drawing canvas; file previews (photos, PDFs) |
| Structure | Plain folders; exports/backups mirror the folder tree |
| Sync | E2EE cross-device sync, offline-capable; share by invitation |
| Dev tools | CLI (fzf/vim/cron), Rust library with C/Java bindings, filesystem mount |
| Platforms | iOS, Android, macOS, Windows, Linux, web, CLI |
| Pricing | Free tier; Premium $2.99/mo for 30 GB |

### Sentiment
| What people say |
|---|
| 2026 community reaction: praise for quality-vs-awareness gap — "the discrepancy between the product that is built and its general awareness... is way too high" (r/macapps launch) [https://www.reddit.com/r/macapps/comments/1qnwtnj/os_lockbook_an_open_source_endtoend_encrypted/] |
| Positioned in sentiment threads against Standard Notes/Obsidian Sync as the polished-E2EE-underdog; little large-volume discussion exists (small but vocal user base) [https://www.reddit.com/r/macapps/comments/1qnwtnj/os_lockbook_an_open_source_endtoend_encrypted/] |
| Name collisions pollute its reputation search results (a physical "Lockbook" journal product, BookLocker publishing service) — discoverability, not quality, is its weakness [https://www.reddit.com/r/writers/comments/1kccczo/is_booklocker_worth_it/, https://www.sweetyhigh.com/read/lockbook-review-052617] |

### Wants
| What people want changed |
|---|
| Cross-platform external-link collaboration (Apple-only today), more visibility/marketing, richer editing features (the tool bets on boring formats over feature count) [https://lockbook.net/docs/collaboration.html, https://www.reddit.com/r/macapps/comments/1qnwtnj/os_lockbook_an_open_source_endtoend_encrypted/] |

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | Core app and sync; premium is space-only ($2.99/mo, 30 GB) [https://alternativeto.net/software/lockbook/about/, https://apps.apple.com/us/app/lockbook/id1526775001] |
| Open source | Repo lockbook/lockbook; org page shows Rust repos (license shown as Unlicense on org listing — UNVERIFIED which applies to the main repo) [https://github.com/lockbook, https://github.com/lockbook/lockbook] |
| Platforms | iOS, Android, macOS, Windows, Linux, web, CLI [https://github.com/lockbook/lockbook] |
| Self-host | Server is part of the repo; self-host path not prominently marketed (UNVERIFIED) [https://github.com/lockbook/lockbook] |

### Contradictions
- Branding tension: "for people with better things to worry about than privacy" vs competitors' loud privacy marketing — Lockbook deliberately inverts the tone while offering the same E2EE; commonly misread as a lesser privacy posture [https://alternativeto.net/software/lockbook/about/, https://lockbook.net/].
- The assigned URL github.com/Lockbook/lockbook is now github.com/lockbook/lockbook (case/redirect); older third-party pages describe it as "The private, polished note-taking platform" (CoreyCole fork listing) vs today's "Encrypted notebook" — positioning narrowed to notebooks [https://github.com/lockbook/lockbook, https://github.com/CoreyCole/lockbook].

Sources: https://github.com/lockbook/lockbook · https://lockbook.net/ · https://lockbook.net/docs/collaboration.html · https://alternativeto.net/software/lockbook/about/ · plus store listings and Reddit inline.

---

LANE C COMPLETE — 12 apps covered

## Video evidence supplements
*Added after the video-evidence pass became a project requirement. Per app: official/community videos and walkthroughs, review footage, comment threads under them, plus notable HN/Reddit threads — focusing on workflow behavior videos reveal and commenter gripes reviews omit. Video sources found via fresh web search Oct 2026; coverage varies sharply by app and gaps are flagged.*

### Logseq
Official demo videos exist on Logseq's YouTube channel, and third-party comparison footage (Obsidian vs Logseq walkthroughs, embedded by review sites) shows the actual difference reviewers gloss: Logseq's daily-notes-first, journals-then-link flow versus Obsidian's manual structure building [https://awesome.tools/apps/logseq, https://toolchase.com/tool/logseq/]. The most telling thread is community-wide: in r/Logseq's "Best most updated Logseq tutorials" (Jan 2025), commenters explain the tutorial ecosystem itself has frozen — devs are focused on the DB version, the main app hasn't updated for months, and creators won't record because the app is about to change and make their videos irrelevant [https://www.reddit.com/r/logseq/comments/1hud3ko/best_most_updated_logseq_tutorials/]. So what the videos miss by being old is real: block references, queries and mobile behavior shown in even a two-year-old "70 minute basics video" no longer match current app or DB betas. Comment gripes under video coverage (and its review pages) focus on rough UI vs commercial apps and unreliable mobile — things video demos filmed on desktop never surface [https://toolchase.com/tool/logseq/]. No major HN video-related thread surfaced in this pass; the forum threads reference YouTube feature videos rather than carrying substantive gripes themselves [https://discuss.logseq.com/t/how-to-connect-a-comment-to-a-comment-to-a-line-youtube-video-used-for-reference/32115].

### Joplin
The strongest walkthrough is Lawrence Systems' Jan 2026 "Joplin Notes: Open Source Notes Without Lock-In", which shows in sequence what docs describe abstractly: picking a sync backend, self-hosting Joplin Server, E2EE key exchange during sync, plugin installation, and the Markdown/WYSIWYG editor toggle — the toggle-and-see rhythm of editing is exactly what screenshots can't convey [https://forums.lawrencesystems.com/t/joplin-notes-open-source-notes-without-lock-in-youtube-release/26392]. Older but still-watched tutorials (MKs Software House, 23K+ views since 2023) and a "Exploring Joplin" review video show hierarchical notebooks, rich-text/markdown duality and shortcuts in daily use [https://glasp.co/youtube/p/joplin-tutorial-joplin-note-taking-app-tutorial, https://chattube.io/summary/entertainment/F7v7UNam1ck]. Comment threads under reviews and the r/joplinapp thread "Joplin as a main notes taking app?" (Feb 2026) surface the onboarding pain reviewers skip: commenters describe initially hating Joplin because it felt alien, only warming to it after weeks of reorganizing notebooks — plus recurring gripes about rich-text/markdown friction that demo videos (which stay in Markdown) glide over [https://www.reddit.com/r/joplinapp/comments/1r8uzw5/joplin_as_a_main_notes_taking_app/]. Review demo videos pitch it as an Evernote replacement, but commenters gripe about Evernote-import edge cases the demos don't run.

### Notesnook
The main video evidence is Learn Linux TV's (Jay LaCroix) Jan 2026 review, about 11 minutes, notable because he shows a real migration: switching from another app, importing notes, theming/customization across desktop and mobile, sharing a note, and live sync behavior between devices — the sync-speed-while-watching part is what text reviews summarize away [https://www.learnlinux.tv/notesnook-review-a-privacy-focused-app-for-simple-note-taking/, https://daily.dev/posts/notesnook-review-a-privacy-focused-app-for-simple-note-taking-neoknvxo8]. Official product videos are minimal; Notesnook relies on docs and blog posts, so walkthrough footage is thinner than for Joplin or Obsidian-adjacent apps. Comment threads under video coverage are sparse, and the recurring user gripes live mainly in text reviews and forums instead: free-tier limits vs Essential pricing and occasional sync delays — neither prominent in video reviews, which emphasize the generous free tier [https://makerstack.co/reviews/notesnook-review/]. No notable HN thread on Notesnook surfaced in this pass beyond general privacy-app comparisons; say explicitly that its video/comment footprint is the lightest of the majors here.

### Trilium Notes
Video coverage is anchored by one widely linked walkthrough, "Trilium Notes — Open Source, Self Hosted Notes with nth level hierarchy and power!", still distributed via Class Central and mirrors: it shows the full self-host path end to end — Docker Compose setup, desktop vs web UI side by side, and live sync between server and client — plus the tree behaviors that are Trilium's actual selling point: arbitrarily deep nesting, cloning one note into multiple places, and note hoisting [https://www.classcentral.com/course/youtube-trilium-notes-open-source-self-hosted-notes-with-nth-level-hierarchy-and-power-192912, https://eanix.net/2023/02/16/watch-trilium-notes-open-source-self-hosted-notes-with-nth-level-hierarchy-and-power-on-youtube/]. The video dates from early 2023 (creator zadam era), so its workflow footage predates the Trilium/TriliumNext fork transition — a gap the video's comments don't address. The significant thread is the 2019 Show HN (techlash-era discussion of scriptable note-taking): commenters praised the journaling-plus-hierarchy fit and the scripting/attributes depth, i.e. exactly the features the demo video underplays [https://news.ycombinator.com/item?id=18840990]. Commenter gripes (HN and follow-on discussions) center on the learning curve and UI density — visible nowhere in the demo, which shows a curated tree. No substantial review-video comment threads surfaced in this pass; coverage is one strong video plus forum posts [https://05t3.github.io/posts/Trilium_Notes/].

### AFFiNE
AFFiNE's official video footprint is marketing-led: launch and positioning videos ("There can be more than Notion and Miro"), whiteboard use-case reels, and a "Book a Demo" funnel, with the live demo site doing the work videos otherwise would [https://affine.pro/, https://affine.pro/whiteboard]. What official footage does show that docs underplay is the doc↔canvas duality in one click — the same block set rendered as page and as edgeless whiteboard — and database views living on the canvas [https://github.com/toeverything/affine]. Independent YouTube walkthroughs and comparison videos (Notion vs AFFiNE / Miro vs AFFiNE) show the trade-off reviewers omit: feature parity claims vs rougher edge cases, with comment threads gripe-heavy on performance with large canvases, mobile apps, and the self-host vs cloud split — gripes that the official demo videos, filmed on small demo workspaces, never encounter [https://tooliverse.ai/tools/affine]. Thread coverage is dominated by the team's own posts (r/PKMS launch threads, Build-in-Public channel), so genuinely independent comment gripes are sparse and mostly second-hand [https://www.reddit.com/r/PKMS/comments/wgrvoe/affine_is_the_nextgen_knowledge_base_to_replace/, https://community.affine.pro/c/build-in-public]. Explicitly: independent review-video coverage exists but is shallow; the sharpest workflow evidence still comes from the live demo rather than video.

### ente
The standout video is the Hasgeek Rootconf technical review (Jan 2025, ~47 min), unusual because it is a live code-and-architecture teardown rather than a product demo: engineer Mangesh Mane presents the Museum server, the Libsodium E2EE flow, and the Cure53 audit trail, while reviewer Karthik Balakrishnan works through a mindmap of the self-hosting path and concludes live that Dockerfile complexity doesn't matter but Docker Compose does — a self-hosting judgment no doc page states that plainly [https://hasgeek.com/rootconf/ente-self-hosting-images-technical-review/, https://hasgeek.com/rootconf/ente-self-hosting-images-technical-review/videos, https://hasgeek.com/rootconf/ente-self-hosting-images-technical-review/sub/review-of-ente-an-open-source-e2ee-self-hosted-alt-FK8L54TNuHrQBsivJJgDHW]. Lifestyle review videos (MacSources, SammyGuru, The Privacy Dad) show the first-upload experience: overnight encrypted upload of tens of thousands of files, on-device face grouping, natural-language search running locally [https://macsources.com/ente-photos-review/, https://sammyguru.com/ente-photos-review/, https://theprivacydad.com/ente-photos-a-privacy-first-photo-app/]. The HN thread (Mar 2024) and r/selfhosted threads carry the real gripes reviewers omit: the e2ee-vs-features tradeoff (founder vishnumohandas concedes Ente must run ML on-device while Immich runs it server-side, making Immich the smarter pick for pure self-hosters), and a self-hosting wart an Ente engineer confirms in comments — self-hosted instances still ship the hosted app's "refer your friend" banner UI [https://news.ycombinator.com/item?id=39570692, https://www.reddit.com/r/selfhosted/comments/1k8wre0/has_anyone_tried_self_hosting_entephotos/, https://www.reddit.com/r/selfhosted/comments/1bzm1cu/ente_photos_mobile_apps_now_support_selfhosting/]. Video comment gripes also cover album sharing/slideshow problems in the web viewer [https://www.reddit.com/r/enteio/].

### Heptabase
Video coverage is unusually strong from the vendor side: a dedicated Video Tutorials page (and YouTube channel) opens with "Sense-making with whiteboards" and organizing/archiving walkthroughs [https://wiki.heptabase.com/video-tutorials]. Third-party footage shows the workflows that make Heptabase distinctive and that text reviews compress badly: dragging a PDF onto a whiteboard, highlighting, then pulling highlights out as individual cards; pasting a YouTube link and getting a full searchable transcript whose highlighted lines become cards linked to video timestamps — the timestamp-linked-card loop is only really legible on video [https://declom.com/heptabase]. Comparison/review videos also show the AI-chat-grounded-in-your-cards flow (answers cite your own highlights) [https://litmustools.com/review/heptabase/, https://aiindigo.com/blog/heptabase-review-2026-the-visual-brain-for-complex-knowledge]. Comment threads under official tutorials and reviews are thin and mostly positive; the recurring pushback users raise (not the videos) is subscription pricing and the closed-source stance, which appear in review verdicts rather than video comments [https://toolchase.com/tool/heptabase/]. No notable HN gripe thread surfaced in this pass; explicitly, video evidence is rich, thread-based griping is not.

### Kinopio
Video coverage is genuinely sparse and that is itself the finding: no substantial independent YouTube reviews surfaced in this pass. What exists is founder-adjacent media — Pirijan Ketheswaran's localfirst.fm interview episode (May 2024, watchable on YouTube) covering the solo-dev economics and offline-first architecture — plus community-made tutorial videos linked from Kinopio's own Tutorial Club space (e.g. a community YouTube walkthrough on editing cards and connections) [https://www.localfirst.fm/8, https://kinopio.club/tutorial-club-U5rh0oZrhVmSM8D5P19GG]. Kinopio embeds YouTube in cards by design, and demo/help pages show the click-anywhere card workflow, paint-select bulk editing, and [[tag]] connections — the paint-select flow is a genuinely nonstandard interaction that text docs under-describe [https://kinopio.club/, https://kinopio.club/help/]. Thread coverage skews to Product Hunt (6 reviews, 5.0 average) and a 2020 r/mindmapping thread where the founder presents and early users report the "organize my brain for the first time" reaction; gripes are scarce, which reflects a small, devoted userbase rather than absence of problems — recent founder posts tout zoom/scroll performance fixes on Safari/iOS, an admission of where performance gripes lived [https://www.producthunt.com/products/kinopio?launch=kinopio-2-0, https://www.reddit.com/r/mindmapping/comments/k098vj/kinopioclub_visual_thinking_brainstorming_tool/, https://www.linkedin.com/in/pirijan/]. Say explicitly: little video or thread coverage exists; what does exist is positive and founder-centered.

### tldraw
The richest video corpus of the twelve, because the SDK is the product: Steve Ruiz's Latent.Space episode (Jan 2024) ships ~30 minutes of demo-only footage cut from audio and was explicitly meant to be watched, not listened to; it shows live what makes tldraw different — the shape/arrow primitives, canvas performance, and the AI-era pivot that the episode title itself ("The Accidental AI Canvas") marks [https://www.latent.space/p/tldraw]. Further high-profile video: the AI Engineer talk on tldraw.computer showing arrows-plus-LLM visual programming on an infinite canvas, and viral third-party demos the company itself amplified (kotsoft's liquid-simulation canvas collaboration) — evidence of SDK extensibility no screenshot conveys [https://www.classcentral.com/course/youtube-tldraw-computer-steve-ruiz-tldraw-469322, https://x.com/tldraw/status/1808908128765030848?lang=en]. The Jam dev podcast walks through building video annotations on tldraw, showing the React-SVG architecture decisions implementers actually make [https://creators.spotify.com/pod/profile/jamdev/episodes/How-We-Built-Video-Annotations-w-tldraw-e2vqk5p]. Comment gripes cluster around the direction, not the product: the community's recurring complaint is that tldraw drifted from a free drawing app into an AI/commercial platform — visible in how even its champion interviews frame it — plus license/pricing questions for commercial use that demo videos never address. Note explicitly: thread griping is about positioning and licensing, far more than about workflow bugs.

### Excalidraw
Video evidence is concentrated in the ecosystem rather than the core app: the official YouTube channel posted a features-of-the-year walkthrough, and the Obsidian-Excalidraw plugin listing embeds a showcase plus a "Video Walkthrough" explicitly designed to ease the "extremely feature-rich and can feel intimidating at first" overwhelm [https://x.com/excalidraw/status/1889687759939322231, https://www.obsidianstats.com/plugins/obsidian-excalidraw-plugin]. A ~18-minute nf-core bytesize talk shows the real scientific-workflow use: quick diagram authoring, end-to-end-encrypted sharing links, and the VS Code integration — the VS Code editing loop is nearly invisible in the product docs [https://blog.stephenturner.us/p/excalidraw-create-and-share-workflow]. The founding documents of its video gap are candid: a 2020 GitHub issue states plainly that "it's a bit hard to learn how to use Excalidraw" and calls for a 90-second demo video — the reason community tutorials proliferated [https://github.com/excalidraw/excalidraw/issues/1314]. Comment threads carry the sharpest material: in r/ObsidianMD's "Excalidraw plugin: How do you use it?", commenters point newbies to Nicole's video and the creator's YouTube channel, and gripe about the markdown/code-block layer and hiding Excalidraw's embedded code — a confusion mechanics that demo videos of the web app never touch because it is an Obsidian-plugin artifact [https://www.reddit.com/r/ObsidianMD/comments/1h8zvmm/excalidraw_plugin_how_do_you_use_it/]. Core-app gripes in video comments are few; complexity gripe lives in the plugin ecosystem.

### Saber
No meaningful video coverage surfaced in this pass: no official demo or tutorial channel, no notable YouTube walkthroughs or review footage found via fresh searches, and no HN thread of substance. Coverage lives in store listings and GitHub instead, so this subsection's evidence base is store-review comment material by necessity [https://saber.adil.hanney.org/, https://github.com/saber-notes/saber]. What those comments show that no video exists to show: heavy-notes users report real limits — one long-term user on Google Play notes load times that scale with content, with 20+ page notes taking up to a minute to open [https://play.google.com/store/apps/details?id=com.adilhanney.saber&hl=en_IN]; an App Store reviewer reports a 2025 regression that made writing impossible in their notes, with praise for earlier semesters of use [https://apps.apple.com/us/app/saber-handwritten-notes/id1671523739]. Recurring gripes elsewhere in store comments: undo does not reverse erases, finger-drawing quirks when the palm-rejection setting is on, and toolbar-position customization praised as the thing other handwriting apps lock away [https://play.google.com/store/apps/details?id=com.adilhanney.saber]. Say explicitly: video coverage is effectively absent; workflow evidence is store reviews and the repo.

### Lockbook
Video coverage is thin: no notable independent YouTube reviews surfaced in this pass, and Lockbook's own channels lean on its website, Discord and docs rather than video; the repo page links a Discord video thumbnail rather than a product demo [https://github.com/lockbook/lockbook, https://lockbook.net/]. The meaningful thread is the Jan 2026 r/macapps launch post by a developer, where commenters single out the thing no screenshot conveys — the scope of fully native apps across iPhone, iPad (Apple Pencil drawing), macOS, Windows, Linux and Android plus real-time collaborative editing, all E2EE [https://www.reddit.com/r/macapps/comments/1qnwtnj/os_lockbook_an_open_source_endtoend_encrypted/]. Commenter gripes that reviewers omit are small and concrete: a Google Play listing review complains the editor's side margins are so wide that text wrapping differs from Keep or Joplin (one line there, two in Lockbook), calling a small inconvenience a genuine usability drag — exactly the kind of typing-density detail only visible in hands-on footage, of which none exists [https://play.google.com/store/apps/details?id=app.lockbook&amp%3Bhl=en_US&amp%3Bgl=US]. FOSS Force's Mar 2026 write-up notes the roadmap (large-file support, PDF editing, file-system integration) that demos, had they existed, would need to cover [https://fossforce.com/2026/03/keep-your-linux-notes-encrypted-with-lockbook/]. Say explicitly: no meaningful video coverage; thread coverage is a single strong Reddit launch thread plus store comments.

VIDEO SUPPLEMENT COMPLETE — C: 12 of 12 apps covered
