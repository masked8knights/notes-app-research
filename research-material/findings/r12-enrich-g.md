# Round R12 — Lane G (evidence enrichment) — apps 1-16

## turtl
### Visual surface
Desktop is a thin Electron/NWJS wrapper around a Rust core (core-rs) with the interface rendered from the turtl/js web app; the repo is build instructions only, so the UI is a three-pane web layout (sidebar of boards/spaces, note stream, note editor) per the official site's framing of spaces, notes and sharing (https://github.com/turtl/desktop, https://turtlapp.com). The official site markets it as "the secure, collaborative notebook" with sync, spaces, tag/text search and Markdown writing (https://turtlapp.com). There is an Android app (com.lyonbros.turtl on Google Play) and a browser extension for desktop bookmarking; reviews on Play mention being unable to reach notes offline, implying a login-gated flow (https://play.google.com/store/apps/details?id=com.lyonbros.turtl&hl=en_US, https://turtlapp.com/features/). No iOS client exists per user commentary (https://www.saashub.com/turtl-reviews). Visual design evidence is thin because the site shows almost no real screenshots — shot-list below relies on the app itself.

SHOT-LIST:
- Marketing homepage hero (spaces/sync/search tiles): https://turtlapp.com/
- Full feature list page: https://turtlapp.com/features/
- Premium/subscription page (shows account/plan UI): https://turtlapp.com/premium/
- GitHub org page (app screenshots referenced as "Turtl's main app interface"): https://github.com/turtl
- Android Play listing screenshots: https://play.google.com/store/apps/details?id=com.lyonbros.turtl&hl=en_US

### Docs analysis
- Note types: text, bookmark, password, image, file/document — a multi-artifact "everything bucket" model rather than one note type (https://turtlapp.com/features/).
- Client-side crypto on all data; sharing with per-person permission levels from read-only to full ownership; sharing is the core differentiator (https://turtlapp.com/features/).
- Search: full-text, filter by tag or lack of tag, sort by create/edit date (https://turtlapp.com/features/).
- Markdown writing plus TeX math inside `$$` delimiters (https://turtlapp.com/features/).
- Import/export of the whole profile for backup or moving between servers — an explicit migration path (https://turtlapp.com/features/).
- "Semi-offline mode": you must be online to log in; review comments confirm offline-unreachable notes as a pain point (https://turtlapp.com/features/, https://play.google.com/store/apps/details?id=com.lyonbros.turtl&hl=en_US).
- Open-source server for self-hosting; config-driven (TURTL_APP_API_URL env mapping) (https://turtlapp.com/features/, https://libreselfhosted.com/project/turtl/).
- Keyboard-shortcut-first navigation (`?` shows shortcuts) (https://turtlapp.com/features/).
- Architecture worth borrowing: logic core in Rust designed to be embedded across desktop, mobile and possibly browser via Emscripten, with thin UI shells per platform (https://github.com/turtl, https://github.com/turtl/desktop).
- Core library was audited (link on homepage, 2021 era); audit commentary flagged affected dependencies and that TLS between client and server is optional, making communication security dependent on it (https://turtlapp.com/, https://www.reddit.com/r/linux/comments/ois6zu/turtlapp_was_recently_audited/).
- Hard limits: none documented publicly; storage/sync caps not stated on official pages — UNVERIFIED, appears to be none enforced for premium vs free besides storage on hosted service.

### Features
| Area | Detail |
|---|---|
| Note types | text, bookmark, password, image, file/document (https://turtlapp.com/features/) |
| Editing | Markdown; TeX math in $$ (https://turtlapp.com/features/) |
| Org | Spaces/boards, tags, text search, sort by date (https://turtlapp.com/features/) |
| Sharing | Per-user permissions read-only → ownership; E2E encrypted shares (https://turtlapp.com/features/) |
| Capture | Browser extension; Android share-to-Turtl (https://turtlapp.com/features/) |
| Backup | Full profile import/export (https://turtlapp.com/features/) |
| Sync | Hosted sync server or self-hosted (https://turtlapp.com/) |
| i18n | Multiple translations, RTL support (https://turtlapp.com/features/) |
| Offline | Semi-offline only; login requires connection (https://turtlapp.com/features/) |
| Platforms | Windows/Linux/macOS desktop, Android, browser extension; no iOS (https://github.com/turtl/desktop, https://play.google.com/store/apps/details?id=com.lyonbros.turtl&hl=en_US) |

### Sentiment
| What people say |
|---|
| Praised as an open-source, E2E-encrypted Evernote alternative with AES-256 and sync (https://alternativeto.net/software/turtl/about/) |
| Criticized as poorly maintained with infrequent updates (https://alternativeto.net/software/turtl/about/) |
| Play reviewers love concept/layout/features but call reliability wanting and complain notes are unreachable without internet (https://play.google.com/store/apps/details?id=com.lyonbros.turtl&hl=en_US) |
| No iOS app is a recurring blocker (https://www.saashub.com/turtl-reviews) |
| Encryption-on-view, re-encrypt-on-save design noted as making E2E social notes feasible (https://www.saashub.com/compare-standard-notes-vs-turtl) |

### Wants
| What people want changed |
|---|
| Real offline access without login/online check (https://play.google.com/store/apps/details?id=com.lyonbros.turtl&hl=en_US) |
| iOS client (https://www.saashub.com/turtl-reviews) |
| Faster, more consistent maintenance cadence (https://alternativeto.net/software/turtl/about/) |
| More reliable sync (https://play.google.com/store/apps/details?id=com.lyonbros.turtl&hl=en_US) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Free hosted service | Yes, with a premium paid service offered via turtlapp.com/premium; donations encouraged (https://turtlapp.com/, https://turtlapp.com/premium/) |
| Self-host | Free, open-source server (https://turtlapp.com/, https://libreselfhosted.com/project/turtl/) |
| Platforms | Windows, macOS, Linux (Electron), Android, browser extension; no iOS (https://github.com/turtl/desktop) |

### Contradictions
- Name collision: search results for "Turtl pricing" are dominated by turtl.co, an unrelated B2B "Revenue Content Platform" with enterprise pricing — do not confuse with the note app turtlapp.com, which is free/self-host (https://turtl.co/pricing/, https://turtlapp.com/).
- Widely described as an Evernote alternative; the hosted service being free with a premium tier contradicts some aggregator pages listing custom enterprise pricing for the note app itself (aggregators are indexing the wrong Turtl) (https://www.saasworthy.com/product/turtl-co/pricing vs https://turtlapp.com/).

Sources: https://turtlapp.com/ ; https://turtlapp.com/features/ ; https://turtlapp.com/premium/ ; https://github.com/turtl/desktop ; https://github.com/turtl ; https://alternativeto.net/software/turtl/about/ ; https://play.google.com/store/apps/details?id=com.lyonbros.turtl&hl=en_US ; https://www.reddit.com/r/linux/comments/ois6zu/turtlapp_was_recently_audited/ ; https://libreselfhosted.com/project/turtl/ ; https://www.saashub.com/turtl-reviews ; https://turtl.co/pricing/

## Zettlr
### Visual surface
Desktop (macOS/Windows/Linux, Electron + Vue 3 + CodeMirror 6): a "publication workbench" layout — a file manager sidebar over a local folder tree (workspace-based, like an IDE rather than a database), a central distraction-light Markdown editor with WYSIWYG-ish rendering of elements, and a right sidebar with tabs for citations/bibliography, tags, related files and writing stats; separate windows exist for preferences, tag manager, statistics with graph view, projects, print preview and onboarding/tutorial (evidenced by the win-* windows enumerated in the repo: win-main, win-preferences, win-stats "Statistics window with graph view", win-tag-manager, win-project-properties, win-print, win-onboarding) (https://github.com/Zettlr/Zettlr). The site positions it as covering the whole writing pipeline "from initial notes to journal submission or book manuscript" with citations in over 9,000 CSL styles (https://www.zettlr.com/, https://www.zettlr.com/features). Themes, dark modes and custom CSS are first-class (https://github.com/Zettlr/Zettlr). The repo's resources/screenshots directory plus 102 screenshots catalogued on noteapps.info are the visual evidence base (https://noteapps.info/apps/zettlr). No mobile app exists; desktop only (https://bundl.run/compare/zettlr-vs-obsidian).

SHOT-LIST:
- Homepage hero (workbench positioning, screenshots strip): https://www.zettlr.com/
- Features page: https://www.zettlr.com/features
- Documentation landing (sidebar tour, editor, spell/grammar/style checkers): https://docs.zettlr.com/en/
- Citations doc (bibliography sidebar rendering): https://docs.zettlr.com/en/editor/citations
- PKMS/Zettelkasten doc page (graph/linking concepts): https://docs.zettlr.com/en/pkms/
- GitHub README screenshots: https://github.com/Zettlr/Zettlr
- Screenshot catalog (102 shots): https://noteapps.info/apps/zettlr
- Press/reviews hub: https://www.zettlr.com/press

### Docs analysis
- Privacy-first by design: no forced cloud sync, no telemetry, plain Markdown files on disk in user-controlled workspaces; third-party sync (Git, Syncthing, Nextcloud) is the intended path (https://www.zettlr.com/, https://github.com/Zettlr/Zettlr).
- Citations are a first-class subsystem: integrated with Zotero/JabRef, citation autocomplete, rendered bibliography in a sidebar, CSL styles shipped and refreshed automatically via a csl:refresh build step (https://docs.zettlr.com/en/editor/citations, https://github.com/Zettlr/Zettlr).
- Export via bundled Pandoc (with LaTeX/Word templates), Textbundle; a build flag exists for repackagers to substitute system Pandoc, showing export integrity is considered a contract (https://github.com/Zettlr/Zettlr).
- Markdown dialect is Pandoc Markdown: CommonMark + GFM + Pandoc extensions, Zettelkasten links/IDs/tags, footnotes, LaTeX math, Mermaid diagrams (https://www.markdownguide.org/tools/zettlr/).
- Zettelkasten support: note IDs, internal wiki links, related files, graph view; docs candidly state a PKMS slows some people down — an unusual honesty in docs worth borrowing (https://www.zettlr.com/, https://docs.zettlr.com/en/pkms/).
- Snippets system with variables and tabstops as text blueprints (https://www.zettlr.com/).
- File-System Abstraction Layer (FSAL) with an internal cache; `--clear-cache` CLI flag and auto-clear when version mismatches — a design pattern for caching index state (https://github.com/Zettlr/Zettlr).
- CLI switches as user features: `--launch-minimized` (autostart to tray), `--data-dir`, `--disable-hardware-acceleration` (https://github.com/Zettlr/Zettlr).
- Ship-with-a-tutorial onboarding: app includes tutorial files per language (https://github.com/Zettlr/Zettlr).
- Architecture: main-process service-provider singletons behind IPC, renderers as independent Vue/Pinia SPAs per window; CodeMirror 6 editor (https://github.com/Zettlr/Zettlr).
- Limits: 32-bit not supported; Pandoc required for import/export (bundled otherwise); no mobile client, no first-party sync — these are hard boundaries, not limitations buried in docs (https://github.com/Zettlr/Zettlr, https://bundl.run/compare/zettlr-vs-obsidian).
- Free/open-source GPL v3; funding purely via donations; brand (name/icons) excluded from the license — forking must rename (https://github.com/Zettlr/Zettlr).
- Build-flag governance is remarkable: redistributors who disable update checks or unbundle Pandoc must provide working alternatives or lose implicit consent to distribute — UNVERIFIED as to enforceability, but written into the README (https://github.com/Zettlr/Zettlr).

### Features
| Area | Detail |
|---|---|
| Editor | Pandoc Markdown, CodeMirror 6, spell/grammar/style checkers, math, Mermaid (https://www.markdownguide.org/tools/zettlr/, https://docs.zettlr.com/en/) |
| Citations | Zotero/JabRef integration, 9,000+ CSL styles, bibliography sidebar (https://www.zettlr.com/, https://docs.zettlr.com/en/editor/citations) |
| PKM | Zettelkasten IDs, wiki links, related files, graph view, tags (https://www.zettlr.com/) |
| Export | Pandoc, LaTeX/Word templates, Textbundle (https://github.com/Zettlr/Zettlr) |
| Search | Powerful full-text search across workspaces (https://github.com/Zettlr/Zettlr) |
| Writing aids | Snippets with variables/tabstops, writing targets, writing statistics (https://www.zettlr.com/, https://github.com/Zettlr/Zettlr) |
| Files | Local workspace folders, FSAL cache, projects (https://github.com/Zettlr/Zettlr) |
| Customization | Themes, dark modes, custom CSS (https://github.com/Zettlr/Zettlr) |
| Sync | None first-party; bring-your-own file sync (https://www.zettlr.com/) |
| Platforms | macOS Intel/ARM, Windows x64, Linux x64/ARM (deb, rpm, AppImage) + package managers; desktop only (https://github.com/Zettlr/Zettlr) |

### Sentiment
| What people say |
|---|
| Framed as calm, long-form scholarly alternative to Obsidian; "feels calmer for long-form scholarly prose" (https://bundl.run/compare/zettlr-vs-obsidian) |
| XDA writer switched from Notion for fast offline plain-text with no subscriptions or sync delays (https://www.xda-developers.com/zettlr-notion-alternative/) |
| Some find it rough at the edges; the Augmented Scholar review credits Zotero autocomplete + Pandoc export but flags polish issues (https://augmentedscholars.com/tools/zettlr/) |
| Zettelkasten users complain folders concept conflicts with Zettelkasten thinking, and want raw-text/note-export flexibility (https://www.reddit.com/r/Zettlr/comments/rxjpqx/how_to_transform_zettels_to_raw_text_zettlr_not/) |
| One user-review blog called it "awful" for their workflow, showing a love/hate split (https://kwikgaret.weebly.com/blog/zettlr-review) |
| Active development: multiple bugs filed Sept–Oct 2026 (https://github.com/Zettlr/Zettlr/issues) |

### Wants
| What people want changed |
|---|
| Mobile/iOS app repeatedly requested; users jury-rig with Markor/Zettel Notes + file sync (https://github.com/Zettlr/Zettlr/discussions/3535, https://github.com/Zettlr/Zettlr/issues/3739, https://blog.babak.no/2023/02/04/how-to-almost-use-zettlr-on-android-devices/) |
| Better Zettelkasten workflow support without folders; easier zettel-to-raw-text (https://www.reddit.com/r/Zettlr/comments/rxjpqx/how_to_transform_zettels_to_raw_text_zettlr_not/) |
| Fewer rough edges in the citation/export pipeline (https://augmentedscholars.com/tools/zettlr/) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Price | Free and open source, donation-funded (https://www.zettlr.com/) |
| Platforms | macOS (Intel/Apple Silicon), Windows x64, Linux x64/ARM (deb/rpm/AppImage; Homebrew, Flathub, WinGet, Chocolatey, Arch); no mobile (https://github.com/Zettlr/Zettlr) |
| Limits | No 32-bit; Pandoc bundled or required (https://github.com/Zettlr/Zettlr) |

### Contradictions
- Aggregator/marketing pages sometimes describe Zettlr as a "note-taking application" (Wikipedia) while the project itself positions it strictly as a publication workbench for long-form writing with citations; the difference matters for feature comparisons (https://en.wikipedia.org/wiki/Zettlr vs https://github.com/Zettlr/Zettlr).
- Commonly believed to sync: it deliberately does not (privacy-first, files stay local), contra the "notes app with sync" default expectation (https://www.zettlr.com/).

Sources: https://github.com/Zettlr/Zettlr ; https://www.zettlr.com/ ; https://www.zettlr.com/features ; https://docs.zettlr.com/en/ ; https://docs.zettlr.com/en/editor/citations ; https://docs.zettlr.com/en/pkms/ ; https://www.markdownguide.org/tools/zettlr/ ; https://bundl.run/compare/zettlr-vs-obsidian ; https://noteapps.info/apps/zettlr ; https://www.xda-developers.com/zettlr-notion-alternative/ ; https://github.com/Zettlr/Zettlr/discussions/3535 ; https://github.com/Zettlr/Zettlr/issues/3739 ; https://www.reddit.com/r/Zettlr/comments/rxjpqx/how_to_transform_zettels_to_raw_text_zettlr_not/

## QOwnNotes
### Visual surface
Native Qt (C++) desktop app for Linux/macOS/Windows, deliberately not Electron; the defining visual trait is total layout freedom — the first-run dialog asks which layout you want (Minimal, Full, Preview Only, Vertical, Single Column) and every panel is dockable, floatable and stackable, with fully customizable toolbars (https://www.xda-developers.com/ditched-onenote-for-open-source-tool/, https://github.com/pbek/QOwnNotes). The working surface is a three-panel classic: navigation/note list, editor with Markdown highlighting (inline image previews, heading folding, optional hiding of Markdown syntax), and preview; themes, dark mode with live switching, custom color modes with their own accent colors, and freedesktop native icon themes are supported (https://www.qownnotes.org/getting-started/overview.html). Distraction-free, full-screen and typewriter modes exist for writing (https://www.qownnotes.org/getting-started/overview.html). Mobile is not an app of its own: Android users run QOwnNotes Android or Nextcloud Notes against the same synced plain-text folder (https://github.com/pbek/QOwnNotes).

SHOT-LIST:
- Official screenshots page (linked from README "Screenshots"): https://www.qownnotes.org/
- Overview/concept page: https://www.qownnotes.org/getting-started/overview.html
- GitHub README (screenshot + extension/store links): https://github.com/pbek/QOwnNotes
- Project page with screenshots (linked as "QOwnNotes project page" in README): https://www.qownnotes.org/
- Installation page (platform packaging breadth): https://www.qownnotes.org/installation.html

### Docs analysis
- Files-first philosophy: notes are existing plain-text Markdown files, no import needed, multiple note folders freely chosen; names come from the first line of the note (Nextcloud Notes convention) with optional override (https://www.qownnotes.org/getting-started/overview.html, https://github.com/pbek/QOwnNotes).
- Sync is delegated entirely to the file layer: Nextcloud/ownCloud file sync, Syncthing, Dropbox etc.; the app watches external changes and shows a diff dialog (https://github.com/pbek/QOwnNotes).
- Server-side companion app (QOwnNotesAPI / Nextcloud app) unlocks note versioning and trash restore from the server; local trash and system trash modes also exist (https://github.com/pbek/QOwnNotes).
- Todo/tasks: manages Nextcloud/ownCloud task lists (Tasks Plus / Calendar Plus) or any CalDAV server; can create Nextcloud Deck cards and link them in notes (https://www.qownnotes.org/getting-started/overview.html).
- Wiki-links `[[Note]]` with autocomplete, heading anchors, aliases, backlinks and refactoring support (https://www.qownnotes.org/getting-started/overview.html).
- Encryption: built-in AES-256 per note, pluggable schemes via scripts (Keybase, PGP) (https://www.qownnotes.org/getting-started/overview.html).
- AI posture notable for a notes app: built-in AI script integration (OpenAI, Groq) plus a built-in MCP server so external AI agents can search/fetch notes securely — design decision worth borrowing (bring-your-own-model + local MCP gateway) (https://www.qownnotes.org/getting-started/overview.html).
- Editor ecosystem: spellcheck, optional LanguageTool and Harper grammar checking, optional Markdown LSP (Marksman completions/diagnostics, Rumdl linting), Vim mode, block selection, tabbed editing (https://www.qownnotes.org/getting-started/overview.html).
- Scripting in QML with an online script repository installable in-app (https://www.qownnotes.org/getting-started/overview.html).
- Capture: Web Companion browser extensions (Chrome/Firefox) for selected-text notes, screenshots, bookmark management; a web app can insert photos from a phone into the current desktop note (https://github.com/pbek/QOwnNotes, https://www.qownnotes.org/getting-started/overview.html).
- Import: Evernote (large files, optional YAML front matter) and Joplin import (https://github.com/pbek/QOwnNotes).
- Portable mode for USB sticks; 60+ languages via Crowdin (https://www.qownnotes.org/getting-started/overview.html).
- Limits: requires Qt 5.5+/Qt 6 desktop OS; no first-party mobile client (relies on ecosystem apps); versioning/trash need the Nextcloud server app — UNVERIFIED whether any hard file-size or note-count limits exist beyond the filesystem (https://github.com/pbek/QOwnNotes).

### Features
| Area | Detail |
|---|---|
| Storage | Plain-text Markdown, existing files, multiple folders, first-line naming (https://www.qownnotes.org/getting-started/overview.html) |
| Editor | MD highlighting, inline images, heading folding, syntax hiding, tabs, Vim mode, block selection (https://github.com/pbek/QOwnNotes) |
| Grammar | Spellcheck, LanguageTool, Harper, Markdown LSP (Marksman, Rumdl) (https://www.qownnotes.org/getting-started/overview.html) |
| Links | [[Note]] wiki links, backlinks, aliases, anchors, refactoring (https://www.qownnotes.org/getting-started/overview.html) |
| Tasks | Nextcloud/ownCloud tasks, CalDAV, Deck cards (https://github.com/pbek/QOwnNotes) |
| Versioning | Server-side restore (Nextcloud app), local/system trash (https://github.com/pbek/QOwnNotes) |
| Encryption | AES-256 built-in, Keybase/PGP via scripts (https://www.qownnotes.org/getting-started/overview.html) |
| AI | Script AI (OpenAI/Groq), built-in MCP server for external agents (https://www.qownnotes.org/getting-started/overview.html) |
| Extensibility | QML scripts, online script repo, customizable toolbars/shortcuts (https://github.com/pbek/QOwnNotes) |
| Capture | Browser companions, phone-photo web app (https://github.com/pbek/QOwnNotes) |
| Layout | Fully dockable panels, 5 preset layouts, portable mode (https://www.xda-developers.com/ditched-onenote-for-open-source-tool/) |
| Platforms | Linux, macOS, Windows (Qt); mobile via ecosystem apps (https://github.com/pbek/QOwnNotes) |

### Sentiment
| What people say |
|---|
| Loved by plain-text/self-hosted crowd: "exactly what I want", GUI alternative to emacs/neovim (https://www.reddit.com/r/degoogle/comments/1lrpjnq/what_do_yall_think_of_qownnotes/) |
| Qt interface called "a bit jank at times" — visual polish is the recurring gripe (https://www.reddit.com/r/degoogle/comments/1lrpjnq/what_do_yall_think_of_qownnotes/) |
| XDA praised tweakability, layout chooser, scripts (https://www.xda-developers.com/ditched-onenote-for-open-source-tool/) |
| Compared favorably to Joplin for Markdown highlighting depth and CSS-customizable editor+preview (https://www.reddit.com/r/linux/comments/gc26f2/qownnotes_best_open_source_cross_platform_note/) |
| Historical complaint: updates shipped too fast for comfort (https://www.reddit.com/r/LinuxActionShow/comments/519huq/qownnotes_is_a_note_taking_and_todo_list_app_that/) |
| Older grievance: WebDAV connections broken and developer reportedly declined to fix; server-side app requirement puzzled users (https://www.reddit.com/r/NextCloud/comments/6zq82s/could_someone_please_explain_to_me_why_qownnotes/) |
| Many users stay in raw Markdown and never open preview — highlighting-in-editor is what matters (https://www.reddit.com/r/NoteTaking/comments/1la3ik4/do_people_actually_use_the_rendered_markdown/) |

### Wants
| What people want changed |
|---|
| Smoother, less janky UI polish (https://www.reddit.com/r/degoogle/comments/1lrpjnq/what_do_yall_think_of_qownnotes/) |
| First-class mobile story rather than relying on Nextcloud Notes/Markor etc. (https://github.com/pbek/QOwnNotes) |
| Better WebDAV / arbitrary-server support without the server-side app (https://www.reddit.com/r/NextCloud/comments/6zq82s/could_someone_please_explain_to_me_why_qownnotes/) |
| Gentler release cadence (historic) (https://www.reddit.com/r/LinuxActionShow/comments/519huq/qownnotes_is_a_note_taking_and_todo_list_app_that/) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Price | Free, open source GPL, no paid tier (https://www.qownnotes.org/getting-started/overview.html) |
| Platforms | GNU/Linux, macOS, Windows (Qt 5.5+/Qt 6); Android via QOwnNotes Android/Markor, iOS via CloudNotes (third-party); browser companions Chrome/Firefox (https://github.com/pbek/QOwnNotes) |
| Limits | Qt desktop requirement; versioning/trash require Nextcloud app (https://github.com/pbek/QOwnNotes) |

### Contradictions
- The app is marketed as working "together with" Nextcloud/ownCloud, but the sync itself is plain file sync and the server-side app is only needed for versioning/trash — a nuance users repeatedly miss (https://www.reddit.com/r/NextCloud/comments/6zq82s/could_someone_please_explain_to_me_why_qownnotes/ vs https://github.com/pbek/QOwnNotes).
- Positioned as "not Electron" for low resource use, yet a 2025 review still frames it against Electron apps' look; its Qt theming (freedesktop icons) partially closes the gap (https://www.qownnotes.org/getting-started/overview.html vs https://www.reddit.com/r/linux/comments/alura7/im_seeing_a_lot_of_note_taking_apps_around_here/).

Sources: https://www.qownnotes.org/getting-started/overview.html ; https://github.com/pbek/QOwnNotes ; https://www.xda-developers.com/ditched-onenote-for-open-source-tool/ ; https://www.reddit.com/r/degoogle/comments/1lrpjnq/what_do_yall_think_of_qownnotes/ ; https://www.reddit.com/r/NextCloud/comments/6zq82s/could_someone_please_explain_to_me_why_qownnotes/ ; https://www.reddit.com/r/linux/comments/gc26f2/qownnotes_best_open_source_cross_platform_note/ ; https://www.reddit.com/r/NoteTaking/comments/1la3ik4/do_people_actually_use_the_rendered_markdown/ ; https://www.reddit.com/r/LinuxActionShow/comments/519huq/qownnotes_is_a_note_taking_and_todo_list_app_that/

## blinko
### Visual surface
Web-first card UI (TypeScript/Next.js) with self-host via Docker or a Tauri desktop shell for macOS/Windows/Linux/Android (https://github.com/blinkospace/blinko). The product model is a two-tier capture flow made visible in the interface: a quick "Blink" (fleeting thought, few words, messy is fine) that can be promoted into a durable "Note" — the marketing site walks Capture → Grow (select rough text, ask AI to expand/polish) → Make it yours (turn Blink into Note) → Share (publish to a personal blog) (https://blinko.space/en). The hosted Cloud page shows a plugin marketplace, an AI conversation view over your notes, a random-walk resurfacing view, a file hub, and a "companion" playful presence character (https://blinko.space/en). Themes: light/dark with system-follow, custom theme colors, multi-language UI (https://dev.to/blinkospace/blinko-selfhosted-note-taking-ai-tool-1f19). Positioned as combining microblogging, task management, pastebin and notes in one self-hosted app (https://addrom.com/blinko-self-hosted-notes-with-ai-rag-baked-in-2/). An iOS client is not listed — README names macOS, Windows, Android, Linux only (https://github.com/blinkospace/blinko).

SHOT-LIST:
- GitHub README (demo credentials, feature bullets): https://github.com/blinkospace/blinko
- Docs intro + install (Docker compose): https://docs.blinko.space/
- Cloud landing (capture/grow/share flow, companion, plugin market): https://blinko.space/en
- Noted.lol walkthrough with compose file (shows web UI in screenshots): https://noted.lol/blinko/
- Make Tech Easier review (in-article screenshots): https://maketecheasier.com/blinko-notes-app/

### Docs analysis
- Core model: card notes with a deliberate Blink-vs-Note lifecycle — capture imperfect first, AI-polish later, promote to durable note, optionally publish to blog; this staging of thought maturity is a borrowable design decision (https://blinko.space/en).
- AI RAG retrieval over your own notes via natural-language queries, running within the self-hosted environment; AI expand/polish of selected text; "conversation with your notes" chat (https://docs.blinko.space/, https://blinko.space/en).
- Storage: plain text/Markdown, self-hosted (Postgres+Next.js stack per Docker install) — no third-party cloud unless using Blinko Cloud (https://github.com/blinkospace/blinko, https://noted.lol/blinko/).
- Install: one-command curl install script; PikaPods one-click deploy with 20% revenue share back to the project — a hosted-partnership model worth noting (https://github.com/blinkospace/blinko).
- RSS reader built in: subscribe and read feeds inside the app, integrating external info into the knowledge base (https://dev.to/blinkospace/blinko-selfhosted-note-taking-ai-tool-1f19).
- Plugin marketplace (hosted Cloud page lists focus timer, background music as examples) (https://blinko.space/en).
- Companion character ("a playful presence to make coming back feel personal") — gamification/retention design decision (https://blinko.space/en).
- Limits: macOS builds are not notarized; users must run `sudo xattr -rd com.apple.quarantine /Applications/blinko.app` — a real friction point documented in the README FAQ (https://github.com/blinkospace/blinko).
- No documented hard limits on storage/sync in docs — UNVERIFIED; Docker volume layout is the main deployment pitfall (https://www.reddit.com/r/selfhosted/comments/1gop6xf/blinko_a_nice_aienhanced_notes_app/).
- Sync story: self-hosted server is the hub; multi-device via the account on your own server — UNVERIFIED how offline-first the Tauri clients are, docs do not specify conflict handling (https://docs.blinko.space/).

### Features
| Area | Detail |
|---|---|
| Capture | Blink quick-capture, plain text/Markdown cards (https://blinko.space/en) |
| AI | RAG natural-language retrieval, expand/polish selection, chat with notes (https://docs.blinko.space/, https://blinko.space/en) |
| Lifecycle | Blink → Note promotion; publish to personal blog (https://blinko.space/en) |
| Extras | RSS reader, plugin marketplace, file hub, random-walk resurfacing, companion character (https://dev.to/blinkospace/blinko-selfhosted-note-taking-ai-tool-1f19, https://blinko.space/en) |
| Deployment | Docker one-liner, PikaPods, self-host; hosted Blinko Cloud (https://github.com/blinkospace/blinko) |
| Theming | Light/dark/system, custom accent colors, multi-language (https://dev.to/blinkospace/blinko-selfhosted-note-taking-ai-tool-1f19) |
| Platforms | Web, Tauri desktop macOS/Windows/Linux, Android; iOS absent (https://github.com/blinkospace/blinko) |

### Sentiment
| What people say |
|---|
| Make Tech Easier called it the one note app covering privacy, usability, accessibility; Notion-like flexibility with AI (https://maketecheasier.com/blinko-notes-app/) |
| XDA: notes never leave your machine unless you choose to back them up — privacy as the headline (https://www.xda-developers.com/private-ai-notes/) |
| Reviewers: "what Obsidian would be if it prioritized AI search over plugin complexity"; one-command Docker install praised (https://reviewnexa.com/blinko-review/) |
| r/selfhosted comparisons favor Memos for single-purpose reliability: Blinko "with OIDC is super buggy in general and random things break all over" (https://www.reddit.com/r/selfhosted/comments/1l53nee/memos_vs_blinko/) |
| Users confused by the Blink vs Note distinction and hub concept on first try (https://www.reddit.com/r/selfhosted/comments/1gop6xf/blinko_a_nice_aienhanced_notes_app/) |
| Telegram-bot integration sought but hard to set up (https://www.reddit.com/r/selfhosted/comments/1hy1vtk/blinko_notes_anyone_managed_to_make_it_work_with/) |

### Wants
| What people want changed |
|---|
| Reliable OIDC/SSO (https://www.reddit.com/r/selfhosted/comments/1l53nee/memos_vs_blinko/) |
| iOS app / better mobile parity (https://www.reddit.com/r/selfhosted/comments/1hy1vtk/blinko_notes_anyone_managed_to_make_it_work_with/) |
| Fewer breakages across updates; clearer docs for volumes/config (https://www.reddit.com/r/selfhosted/comments/1gop6xf/blinko_a_nice_aienhanced_notes_app/) |
| Working integrations (Telegram bot) with less setup pain (https://www.reddit.com/r/selfhosted/comments/1hy1vtk/blinko_notes_anyone_managed_to_make_it_work_with/) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Self-host | Free, open source (AGPL-family repo); donation-funded via Ko-fi/afdian; PikaPods rev-share (https://github.com/blinkospace/blinko) |
| Cloud | Blinko Cloud hosted plan; free users keep full core features, Cloud revenue funds development (https://blinko.space/en) |
| Platforms | Web, macOS, Windows, Linux, Android (Tauri); no iOS listed (https://github.com/blinkospace/blinko) |

### Contradictions
- README markets Tauri as "lightweight" and the app as "efficient and fast", yet selfhosted-community reports describe random breakages and buggy SSO after updates — the lightweight claim does not extend to operational robustness (https://github.com/blinkospace/blinko vs https://www.reddit.com/r/selfhosted/comments/1l53nee/memos_vs_blinko/).
- Docs emphasize "complete control over your information" while the same project sells Blinko Cloud, a hosted service — both true, but the marketing nuance matters (https://docs.blinko.space/ vs https://blinko.space/en).

Sources: https://github.com/blinkospace/blinko ; https://docs.blinko.space/ ; https://blinko.space/en ; https://noted.lol/blinko/ ; https://dev.to/blinkospace/blinko-selfhosted-note-taking-ai-tool-1f19 ; https://maketecheasier.com/blinko-notes-app/ ; https://www.xda-developers.com/private-ai-notes/ ; https://www.reddit.com/r/selfhosted/comments/1l53nee/memos_vs_blinko/ ; https://www.reddit.com/r/selfhosted/comments/1gop6xf/blinko_a_nice_aienhanced_notes_app/ ; https://reviewnexa.com/blinko-review/ ; https://addrom.com/blinko-self-hosted-notes-with-ai-rag-baked-in-2/

## edgeever (EdgeEver)
### Visual surface
A deliberately Evernote-shaped, modern-stack rebuild: the classic three-pane productivity layout (notebook tree view · note list · editor) with resizable panels, executed in Vite + React + Tailwind + shadcn/ui + Radix with a TipTap/ProseMirror editor that toggles between rich-text WYSIWYG and raw Markdown (https://github.com/tianma-if/edgeever). Beyond the classic surface it layers visual note types: native poster notes (canvas-based structured cards, double-click to edit), AI-generated diagrams/infographics (timelines, comparison charts, quadrant matrices, mind maps), Mermaid, and native tables (https://github.com/tianma-if/edgeever). Clients: web PWA (Workbox/Dexie offline drafts), Electron desktop with a Rust sidecar, Expo/React Native Android, native SwiftUI iOS, and a Manifest V3 web clipper (https://github.com/tianma-if/edgeever). The repo advertises "17 step-by-step showcases with screenshots" as its visual evidence; demo at demo.edgeever.org resets daily (https://github.com/tianma-if/edgeever). Release notes show tablet layouts, reader typography and Android share-sheet capture being actively refined (https://github.com/tianma-if/edgeever/issues/498, https://github.com/tianma-if/edgeever/issues/504).

SHOT-LIST:
- GitHub README (feature matrix, architecture): https://github.com/tianma-if/edgeever
- Live demo workspace (three-pane UI): https://demo.edgeever.org
- Release-note showcase links ("Explore 17 step-by-step showcases with screenshots" in README): https://github.com/tianma-if/edgeever
- HelloGitHub listing page: https://hellogithub.com/en/repository/tianma-if/edgeever
- v2.8.0 release notes (screen capture feature): https://github.com/tianma-if/edgeever/issues/681

### Docs analysis
- Positioning is explicit and unusually detailed: a gap-analysis against Evernote (ads/add-ons, tightened quotas), Obsidian (closed core, paid sync, vault bloat from attachments, cold-start lag at thousands of notes), Joplin (dated UI, paid fast sync, no web workspace), Memos (timeline ≠ productivity), SiYuan (block overhead) — claiming silky-smooth operation at 10,000+ notes (https://github.com/tianma-if/edgeever).
- Zero-cost serverless: full stack runs on Cloudflare Workers + D1 (SQLite) + R2 within free quotas, quoted capacity ~150k short notes and ~50k images; Docker alternative for VPS/NAS supports "millions of notes" (https://github.com/tianma-if/edgeever).
- Novel deployment path: a copy-paste prompt that an AI agent (Codex/Claude/Cursor/etc.) executes to fork, provision D1/R2 and deploy — deployment-as-agent-task is a borrowable idea (https://github.com/tianma-if/edgeever).
- Triple-format storage model: every note persisted simultaneously as content_json (TipTap source of truth), content_markdown (interoperability/API/agents) and content_text (full-text search/indexing) — a strong design decision worth borrowing (https://github.com/tianma-if/edgeever).
- Offline-first sync: edits upload after 30s of typing inactivity, remote-change polling every 5 min while visible, immediate on refocus; constants configurable (DEFERRED_MEMO_SYNC_DELAY_MS, BACKGROUND_WORKSPACE_REFRESH_INTERVAL_MS); auto-sync queue resumes when reconnected (https://github.com/tianma-if/edgeever).
- Client-side silent image compression before upload (to WebP when beneficial, max edge 2560px, original kept if no gain) to save serverless compute; chunked streaming supports up to 1 GiB files; 50–90% size reduction claimed (https://github.com/tianma-if/edgeever).
- AI: BYOK (OpenAI/Claude/Gemini/custom endpoints), sidebar assistant for summary/proofread/translate, AI RSS daily digest with noise filtering, AI diagram generation, prompt-to-database tables with auto field typing (https://github.com/tianma-if/edgeever).
- Agent-native: built-in Remote MCP (one-click config in Profile → API/MCP) with full CRUD over notes, diagrams, tables, poster notes, notebooks, tags, attachments, revisions, templates; ACP in desktop to drive local coding agents (https://github.com/tianma-if/edgeever).
- Publishing: one-click static documentation-site publishing of notebooks with tree navigation and password protection; public collection forms without login, syncing into tables; share management with QR codes (https://github.com/tianma-if/edgeever, https://github.com/tianma-if/edgeever/issues/504, https://github.com/tianma-if/edgeever/issues/613).
- Deep structured clipping for 20+ platforms (X, Xiaohongshu, WeChat, Zhihu, Reddit, GitHub, YouTube, Bilibili, Medium, Substack...); WeChat chat-history archiving on macOS; video notes saving YouTube/Bilibili pages with captions, and transcription via configured speech service (https://github.com/tianma-if/edgeever, https://github.com/tianma-if/edgeever/issues/489).
- Migration guides: Evernote ENEX import script, flomo, Memos, Notion; native ZIP backup whose extracted notes/ directory is clean Markdown + attachments with metadata enabling lossless restore (https://github.com/tianma-if/edgeever).
- Multi-user: instance admin creates member accounts, each with fully isolated workspace (notes, trash, MCP tokens); storage dashboard per account; brute-force protection (https://github.com/tianma-if/edgeever).
- Desktop extras: global show/hide shortcut, screen-region capture to note (v2.8.0), PicGo/PicList image-host integration (https://github.com/tianma-if/edgeever/issues/681, https://github.com/tianma-if/edgeever).
- License AGPL-3.0; trademark clause: forks may say "based on EdgeEver" but not imply official status (https://hellogithub.com/en/repository/tianma-if/edgeever, https://github.com/tianma-if/edgeever).
- UNVERIFIED: real-world performance at 10k+ notes and sync reliability claims are vendor-stated, no independent benchmark found.

### Features
| Area | Detail |
|---|---|
| Layout | Classic three-pane, resizable; Evernote workflow (https://github.com/tianma-if/edgeever) |
| Editor | TipTap WYSIWYG ↔ raw Markdown toggle, math, task lists, focus mode, second-level autosave (https://github.com/tianma-if/edgeever) |
| Visual notes | Poster notes (canvas cards), AI diagrams, Mermaid, tables, image-card export (MD/HTML/PDF) (https://github.com/tianma-if/edgeever) |
| Org | Infinite-depth notebook tree, tags, drag-sort, batch merge/move, ms full-text search (https://github.com/tianma-if/edgeever) |
| Capture | Web clipper (20+ platforms deep-structured), mobile share sheet, screen capture, video notes + transcription (https://github.com/tianma-if/edgeever) |
| AI | BYOK sidebar assistant, RSS digest, AI tables/diagrams, MCP + ACP agent protocols (https://github.com/tianma-if/edgeever) |
| Publishing | Notebook → static doc site w/ password, share links/QR, loginless collection forms (https://github.com/tianma-if/edgeever) |
| Sync | Instant multi-device, offline-first queue, zero device limits (https://github.com/tianma-if/edgeever) |
| Multi-user | Member accounts, tenant isolation, storage dashboard (https://github.com/tianma-if/edgeever) |
| Migration | ENEX/flomo/Memos/Notion guides; ZIP backup = Markdown + attachments (https://github.com/tianma-if/edgeever) |
| Platforms | Web/PWA, macOS/Windows/Linux (Electron+Rust), Android (Expo), iOS 17+ (SwiftUI), Chrome/Edge/Firefox clipper (https://github.com/tianma-if/edgeever) |

### Sentiment
| What people say |
|---|
| Very new but fast-growing: ~2.9k stars, 511 stars in the past 7 days at review time (https://hellogithub.com/en/repository/tianma-if/edgeever) |
| Extremely rapid release cadence: at least 10 releases in October 2026 alone (v1.100.0 → v2.8.0) — breadth over polish is implied by the volume of fixes per release (https://github.com/tianma-if/edgeever/issues/478, https://github.com/tianma-if/edgeever/issues/681) |
| Rough edges visible in release notes: Android AI crash ("undefined is not a function"), empty notes when iOS share-sheet posts, iOS App Store submission failing on process issues, Android device-level verification incomplete (https://github.com/tianma-if/edgeever/issues/632, https://github.com/tianma-if/edgeever/issues/613) |
| No substantial independent review corpus yet — UNVERIFIED beyond repo activity; community lives in a Telegram group tied to LINUX DO (https://github.com/tianma-if/edgeever) |

### Wants
| What people want changed |
|---|
| (Inferred from changelogs, UNVERIFIED as explicit requests) more stable mobile AI features, reliable iOS share-sheet capture, working App Store distribution (https://github.com/tianma-if/edgeever/issues/632, https://github.com/tianma-if/edgeever/issues/613) |
| China-market friction: iOS app requires an Apple ID from outside mainland China (https://github.com/tianma-if/edgeever) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Price | Free and open source, AGPL-3.0; donation-funded (WeChat Pay/Alipay) (https://hellogithub.com/en/repository/tianma-if/edgeever, https://github.com/tianma-if/edgeever) |
| Hosting | Cloudflare free tier (no VPS) or Docker on VPS/NAS; note: R2 must be activated with a payment method even on free allowance (https://github.com/tianma-if/edgeever) |
| Limits | Cloudflare free tier ~150k short notes / ~50k images; Docker unbounded claim (https://github.com/tianma-if/edgeever) |
| Platforms | Web/PWA, macOS, Windows, Linux, Android, iOS (17+), Chrome/Edge/Firefox (https://github.com/tianma-if/edgeever) |

### Contradictions
- Headline says "Serverless & 100% Free Forever", but the Cloudflare path requires activating an R2 subscription with a payment method before the free storage allowance works — free, but not card-free (https://github.com/tianma-if/edgeever).
- README claims "seamless, low-latency, instant multi-device sync", yet the same README's core-mechanisms section describes deferred 30s upload and 5-minute background polling — instant marketing vs eventual-consistency reality (https://github.com/tianma-if/edgeever).
- Trademark/disclaimer insists EdgeEver is not affiliated with Evernote and independently designed, while the name, three-pane pitch, and Evernote migration guide lean hard on the Evernote identity (https://github.com/tianma-if/edgeever).

Sources: https://github.com/tianma-if/edgeever ; https://hellogithub.com/en/repository/tianma-if/edgeever ; https://github.com/tianma-if/edgeever/issues/489 ; https://github.com/tianma-if/edgeever/issues/498 ; https://github.com/tianma-if/edgeever/issues/504 ; https://github.com/tianma-if/edgeever/issues/613 ; https://github.com/tianma-if/edgeever/issues/632 ; https://github.com/tianma-if/edgeever/issues/681 ; https://demo.edgeever.org

## notion-re (lochana-dahanayake/notion-re)
### Visual surface
UNVERIFIED — not researchable. The repository https://github.com/lochana-dahanayake/notion-re is not indexed by any web search I could run (GitHub search results, portfolio sites, and blog coverage all miss it), and direct fetch of the URL is refused in this environment, so no screenshot, README, or UI description could be verified. What is verifiable about the author: a personal developer account that was renamed from loch214 to lochana-dahanayake on 2026-10-23 (four days before this research), with public work consisting of a Next.js/React/Tailwind/Framer-Motion portfolio site (lochana-dahanayake.me) and an "architecture-advisor" web app that pairs a deterministic rule engine with bounded AI explanations (https://github.com/lochana-dahanayake/architecture-advisor, https://github.com/lochana-dahanayake/my-portfolio, https://github.com/lochana-dahanayake/architecture-advisor/pull/14). A "notion-re" name implies a Notion re-implementation, but that is inference, not evidence — treat as UNVERIFIED.

SHOT-LIST:
- (None capturable — no publicly indexed visual evidence found; if the main session can open https://github.com/lochana-dahanayake/notion-re directly in its browser, capture the README and any screenshots there.)

### Docs analysis
- No documentation accessible through search; the repo returns no indexed description, README excerpt, or fork/activity traces (searched: github search results, "notion-re" web, account page results). UNVERIFIED: whether the repo is public, empty, renamed, or private (https://github.com/lochana-dahanayake/lochana-dahanayake).
- Adjacent verifiable context from the same author: architecture-advisor uses "deterministic rule engine + bounded AI explanations" — an AI-constraint design philosophy that may carry over, UNVERIFIED (https://github.com/lochana-dahanayake/architecture-advisor).
- The account rename means any previously recorded link from an earlier round (e.g. loch214/notion-re) may now 404 or redirect; the task-supplied URL uses the new name (https://github.com/lochana-dahanayake/architecture-advisor/pull/14).

### Features
| Area | Detail |
|---|---|
| Capabilities | UNVERIFIED — nothing confirmable found in this research pass |

### Sentiment
| What people say |
|---|
| None found — no reviews, forum posts, issues, or social mentions surfaced (searches on "notion-re", "lochana-dahanayake notion", GitHub topic searches) |

### Wants
| What people want changed |
|---|
| None found |

### Pricing and platforms
| Item | Detail |
|---|---|
| Price | Unknown — UNVERIFIED |
| Platforms | Unknown — UNVERIFIED (name suggests a web/desktop Notion-style app, inference only) |

### Contradictions
- If an earlier round recorded notion-re as an established product with features/pricing, that picture cannot be reproduced from public evidence now: the repo is invisible to search and only the author's other projects surface. Any prior claims about it should be treated as unverifiable (https://github.com/lochana-dahanayake/architecture-advisor/pull/14 for account context).

Sources: https://github.com/lochana-dahanayake/architecture-advisor ; https://github.com/lochana-dahanayake/my-portfolio ; https://github.com/lochana-dahanayake/lochana-dahanayake ; https://github.com/lochana-dahanayake/architecture-advisor/pull/14 ; (target repo not indexed: https://github.com/lochana-dahanayake/notion-re)

## zappynotes (zapatify/zappynotes)
### Visual surface
UNVERIFIED — the repository itself is not reachable through the search/fetch tooling in this pass (its exact URL never surfaces as a standalone indexed page, only the author's profile listing), so no UI description, screenshots, or README rendering could be confirmed. What is verifiable: the repo sits on the GitHub profile of user zapatify ("Zapata") with the on-repo description "Modern self-hosted note-taking app built with Rails 8 - Open source Evernote alternative" and the language marked Ruby; the same profile also holds zapatify.github.io (HTML site repo), ZappyTime (TypeScript), and a Ruby loan-amortization gem, so this is a personal side project profile rather than a product organization (https://github.com/zapatify, https://github.com/zapatify/amortizy). Being Rails 8 implies a server-rendered web UI, but that is inference — UNVERIFIED.

SHOT-LIST:
- (None capturable — repo page not indexed; main session should try the README and any screenshots directly at the repo if its browser can reach it.)

### Docs analysis
- Verified claims: self-hosted; built on Rails 8; Ruby stack; positioned as an open-source Evernote alternative (https://github.com/zapatify).
- UNVERIFIED: everything else — sync architecture, storage format, editor type, export/import, mobile clients, multi-user support, limits. No documentation site, blog post, deployment guide, or Docker instructions surfaced in any search pass (https://github.com/zapatify).
- The author's GitHub Pages repo (zapatify.github.io) may hold project docs but also does not surface with zappynotes content in search results (https://github.com/zapatify).

### Features
| Area | Detail |
|---|---|
| Known | Self-hosted; Rails 8/Ruby; Evernote-alternative positioning (https://github.com/zapatify) |
| Everything else | UNVERIFIED — no doc, demo, or third-party coverage found |

### Sentiment
| What people say |
|---|
| None found — zero reviews, issues coverage, forum posts, or social mentions surfaced |

### Wants
| What people want changed |
|---|
| None found |

### Pricing and platforms
| Item | Detail |
|---|---|
| Price | Open source per its own description; no pricing info found (https://github.com/zapatify) |
| Platforms | Web (self-hosted, Rails) implied; desktop/mobile UNVERIFIED (https://github.com/zapatify) |

### Contradictions
- None found (nothing substantial recorded at all — flagging the name-collision risk instead: search results for "zappy notes"/"zap notes" are dominated by unrelated projects — ZapNotesApp by ZigaoWang (GPLv3, zap-notes.com), ZapNotesApp org (iOS), ZapNotes org — none of which is this Rails 8 app; any earlier-round data conflating them should be discarded) (https://zap-notes.com/, https://github.com/ZigaoWang/ZapNotesApp vs https://github.com/zapatify).

Sources: https://github.com/zapatify ; https://github.com/zapatify/amortizy ; https://zap-notes.com/ ; https://github.com/ZigaoWang/ZapNotesApp

## owlistic
### Visual surface
A web SPA (React/Vite) with a classic structure: sidebar with an infinite notebooks → notes → sub-notes tree, a note editor with a floating toolbar, and dedicated screens for Home, Notes, Tasks, Profile and Trash, in dark/light modes that auto-detect the OS preference (https://github.com/owlistic-notes/owlistic, http://blog.brightcoding.dev/2025/08/14/owlistic-a-developer-friendly-open-source-notes-todo-app-with-real-time-sync). The editor is TipTap-based WYSIWYG with slash-commands, markdown↔rich-text conversion shortcuts, and inline todo items that sync globally when checked (third-party writeup; repo README confirms the editor + inline todos) (https://github.com/owlistic-notes/owlistic). The README carries a screenshots section (General: real-time updates; Editor: editor/scrolling/toolbar; Screens: home, sidebar, profile, trash, notebooks, notes, tasks) but the fetched page renders only placeholders — screenshots exist in-repo and are the main visual evidence (https://github.com/owlistic-notes/owlistic). The project's own docs site is JS-rendered and nearly empty to non-browser fetches (https://owlistic-notes.github.io/owlistic/). The creator admitted the UI was unfinished at launch and screenshots "make decent" only later — expect an unpolished, functional look (https://www.reddit.com/r/selfhosted/comments/1kqy8y4/open_source_notetakingtodo_app/).

SHOT-LIST:
- README screenshots block (General/Editor/Screens tables): https://github.com/owlistic-notes/owlistic
- Docs site (Get Started/Roadmap): https://owlistic-notes.github.io/owlistic/
- Repo file tree: docs/features referenced by README: https://github.com/owlistic-notes/owlistic/blob/main/README.md
- Releases page (activity check): https://github.com/owlistic-notes/owlistic/releases

### Docs analysis
- Feature set from README: notebooks/notes tree, WYSIWYG editor, inline todos, real-time sync, JWT auth, role-based access control, trash, dark/light mode, Markdown import (https://github.com/owlistic-notes/owlistic).
- Deployment: Docker via GHCR image, plus community Helm charts for Kubernetes; local dev Node 18+/pnpm (repo README structure; Helm: https://github.com/owlistic-notes/owlistic via https://github.com/orgs/owlistic-notes/repositories).
- Third-party writeup claims (treat as UNVERIFIED against the repo, some may be aspirational): WebSocket real-time sync with CRDT under the hood and multi-cursor presence, Cmd+K global search, bulk Markdown import and subtree .zip export, soft-delete trash with 30-day retention, SQLite/PostgreSQL with encryption at rest, plugin API loaded from ~/.owlistic/plugins or npm tag owlistic-plugin, CSS-variable theming, roadmap to E2E encryption + offline-first sync at 1.0 (Q1 2026) (http://blog.brightcoding.dev/2025/08/14/owlistic-a-developer-friendly-open-source-notes-todo-app-with-real-time-sync).
- Governance: consensus-based core team, decisions in public GitHub Discussions; code GPLv3, branding CC-BY-4.0; README follows the standard-readme spec — an unusual docs discipline worth borrowing (https://github.com/owlistic-notes/owlistic, http://blog.brightcoding.dev/2025/08/14/owlistic-a-developer-friendly-open-source-notes-todo-app-with-real-time-sync).
- No mobile app; roadmap mentions Mobile PWA — UNVERIFIED whether shipped (http://blog.brightcoding.dev/2025/08/14/owlistic-a-developer-friendly-open-source-notes-todo-app-with-real-time-sync).
- Hard limits: none documented — UNVERIFIED (https://github.com/owlistic-notes/owlistic).

### Features
| Area | Detail |
|---|---|
| Structure | Notebooks → notes → sub-notes tree (https://github.com/owlistic-notes/owlistic) |
| Editor | WYSIWYG (TipTap-class), slash commands, inline todos, Markdown import (https://github.com/owlistic-notes/owlistic) |
| Collaboration | Real-time multi-device/tab sync; RBAC; JWT auth (https://github.com/owlistic-notes/owlistic) |
| Data | PostgreSQL/SQLite backend, Docker, Helm charts (https://github.com/orgs/owlistic-notes/repositories) |
| Lifecycle | Trash/soft delete; dark/light theming (https://github.com/owlistic-notes/owlistic) |
| Extensibility | Plugin system + theming (third-party claim, UNVERIFIED) (http://blog.brightcoding.dev/2025/08/14/owlistic-a-developer-friendly-open-source-notes-todo-app-with-real-time-sync) |
| Platforms | Self-hosted web; no desktop/mobile native clients (https://github.com/owlistic-notes/owlistic) |

### Sentiment
| What people say |
|---|
| Creator's April 2025 launch on r/selfhosted: honest about "issues with text styling and some sync issues" at that stage (https://www.reddit.com/r/selfhosted/comments/1k3tkrt/open_source_notetaking_app/) |
| May 2025 follow-up post drew 18 votes and discussion; creator promising screenshots/video after UI bug fixes (https://www.reddit.com/r/selfhosted/comments/1kqy8y4/open_source_notetakingtodo_app/) |
| Project under active development with a warning banner about bugs and breaking changes (https://github.com/owlistic-notes/owlistic) |
| Minimal independent coverage beyond the creator's own posts and one blog writeup (https://github.com/owlistic-notes/owlistic) |

### Wants
| What people want changed |
|---|
| Polish: text styling and sync reliability (creator's own admission at launch) (https://www.reddit.com/r/selfhosted/comments/1k3tkrt/open_source_notetaking_app/) |
| Documentation depth beyond the skeleton docs site (https://owlistic-notes.github.io/owlistic/) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Price | Free, GPLv3, no paid tier (https://github.com/owlistic-notes/owlistic) |
| Platforms | Self-hosted web (Docker/K8s); no native clients (https://github.com/orgs/owlistic-notes/repositories) |

### Contradictions
- The third-party blog describes a mature architecture (CRDT, presence, plugin marketplace, E2E roadmap with dates); the repo's own README lists a much smaller shipped feature set and a warning that breaking changes are expected — the blog reads partly as promotion and should not be cited as shipped reality (http://blog.brightcoding.dev/2025/08/14/owlistic-a-developer-friendly-open-source-notes-todo-app-with-real-time-sync vs https://github.com/owlistic-notes/owlistic).

Sources: https://github.com/owlistic-notes/owlistic ; https://github.com/orgs/owlistic-notes/repositories ; https://owlistic-notes.github.io/owlistic/ ; http://blog.brightcoding.dev/2025/08/14/owlistic-a-developer-friendly-open-source-notes-todo-app-with-real-time-sync ; https://www.reddit.com/r/selfhosted/comments/1k3tkrt/open_source_notetaking_app/ ; https://www.reddit.com/r/selfhosted/comments/1kqy8y4/open_source_notetakingtodo_app/

## NexaNote (TheZupZup/NexaNote)
### Visual surface
A Flutter client (Linux desktop + Android) with an honest, utility-first look: first launch offers a prominent "Use NexaNote offline" path, the working surface has a Text vs Draw mode switch for typed vs stylus notes, a Settings screen holding Backend API connection fields, and a Settings → About card showing the installed version; the creator's own README concedes the Android build is "functional but still being polished" (https://github.com/TheZupZup/NexaNote). Drawing mode provides pen, highlighter, eraser with pressure sensitivity (mouse works too); the backend exposes an interactive Swagger UI at the API's /docs endpoint for the technically minded (https://github.com/TheZupZup/NexaNote). No screenshots are visible in the fetched README, and there is no marketing site — the app's visual evidence is essentially the app itself (https://github.com/TheZupZup/NexaNote).

SHOT-LIST:
- README (compose file, storage layout, roadmap): https://github.com/TheZupZup/NexaNote
- Releases page with attached APK: https://github.com/TheZupZup/NexaNote/releases
- Swagger UI at a deployed instance: http://127.0.0.1:8766/docs (local only; capture from a demo deployment if the main session runs the Docker image)
- Issue #82 (Linux desktop storage gap): https://github.com/TheZupZup/NexaNote/issues/82

### Docs analysis
- Core pitch: self-hosted handwriting/stylus notes on your own NAS, privacy-first; Flutter client + Python FastAPI backend, everything stored as plain files on your server (https://github.com/TheZupZup/NexaNote).
- Storage layout is plain files on disk: notes/ as Markdown + YAML frontmatter, notebooks/ as YAML metadata, drawings/ as per-note JSON stroke files, sync_logs/ as JSON diagnostics — openable in Obsidian or any editor, backup-able with ordinary file tools; strokes-as-JSON (not raster images) is a notable design decision (https://github.com/TheZupZup/NexaNote).
- Local-first with truly optional backend: device SQLite for offline, "no backend, NAS, or Docker required"; WebDAV sync via your own server when wanted (https://github.com/TheZupZup/NexaNote).
- Deployment: single multi-arch Docker image (amd64+arm64) exposing REST on 8766 and WebDAV on 8765; NAS volume examples for Synology/Ugreen; reverse-proxy recipes (Nginx, Caddy, Cloudflare Tunnel) for single-hostname TLS (https://github.com/TheZupZup/NexaNote).
- Sync diagnostics as a product feature: latest sync report JSON, dry-run sync with ?dry_run=true, and a copy-diagnostics button that redacts credentials — a design pattern worth borrowing for trust and bug reports (https://github.com/TheZupZup/NexaNote).
- Release engineering as a feature: one vX.Y.Z tag drives Android versionName/code, pubspec, Docker tags, F-Droid metadata and CHANGELOG via an idempotent web-UI workflow with a release-bump guard script — unusually disciplined for a solo project (https://github.com/TheZupZup/NexaNote).
- Distribution posture: no Play Store; GitHub Releases APK with stable asset name NexaNote-Android.apk, tracked by Obtainium; F-Droid metadata draft aligned (MPL-2.0, no proprietary deps, INTERNET permission used only for your own server) (https://github.com/TheZupZup/NexaNote).
- Status honesty: "Sync reliability is improving but is not yet bulletproof", "Not yet recommended for critical notes without your own backups" — rare candor (https://github.com/TheZupZup/NexaNote).
- Hard limits / gaps: desktop Linux local store is broken because sqflite ships Android/iOS implementations only and nothing sets databaseFactory for Linux/Windows — local persistence on desktop is effectively absent (https://github.com/TheZupZup/NexaNote/issues/82). Roadmap: sync reliability, Android polish, conflict-resolution UI, F-Droid, desktop packaging (https://github.com/TheZupZup/NexaNote).

### Features
| Area | Detail |
|---|---|
| Notes | Typed notes as .md + YAML frontmatter; notebooks (https://github.com/TheZupZup/NexaNote) |
| Handwriting | Stylus pen/highlighter/eraser, pressure sensitivity, strokes stored as JSON (https://github.com/TheZupZup/NexaNote) |
| Storage | Local SQLite offline + plain-file server layout; no third-party cloud (https://github.com/TheZupZup/NexaNote) |
| Sync | WebDAV through your own server; sync logs + dry-run + redacted diagnostics (https://github.com/TheZupZup/NexaNote) |
| Backend | FastAPI, Docker multi-arch, REST 8766 + WebDAV 8765 (https://github.com/TheZupZup/NexaNote) |
| Distribution | GitHub Releases APK + Obtainium, F-Droid metadata in progress, no Play Store (https://github.com/TheZupZup/NexaNote) |
| Platforms | Android APK, Linux desktop (local store currently broken there); no iOS, no web app (https://github.com/TheZupZup/NexaNote, https://github.com/TheZupZup/NexaNote/issues/82) |

### Sentiment
| What people say |
|---|
| Creator's April 2026 r/selfhosted launch post was removed by moderators — limited organic visibility (https://www.reddit.com/r/selfhosted/comments/1si5j4s/removed_by_moderator/) |
| A QA pass found "mostly bugs that lose or revert notes" in the Flutter client and backend, fixed with regression tests that failed before each fix — data-loss risk was real and recent (https://github.com/TheZupZup/NexaNote/pull/81) |
| Offline editor safety fix: text typed in the debounce window was skipped when switching to Draw mode (https://github.com/TheZupZup/NexaNote/pull/80) |
| Issue reporter expected notes to "save locally on Linux... the same as on Android" — user trust in local-first claim currently unmet on desktop (https://github.com/TheZupZup/NexaNote/issues/82) |
| Very small user base; no substantive review corpus — UNVERIFIED sentiment beyond repo activity |

### Wants
| What people want changed |
|---|
| Working local persistence on Linux/Windows desktop (https://github.com/TheZupZup/NexaNote/issues/82) |
| Bulletproof sync + a clear conflict-resolution UI (creator's own roadmap; issue threads concur) (https://github.com/TheZupZup/NexaNote) |
| F-Droid availability (roadmap) (https://github.com/TheZupZup/NexaNote) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Price | Free, MPL-2.0 (modifications stay open, commercial use allowed) (https://github.com/TheZupZup/NexaNote) |
| Platforms | Android (GitHub Releases APK), Linux desktop (limited); self-hosted FastAPI backend; no iOS/web (https://github.com/TheZupZup/NexaNote) |
| Limits | Desktop local store broken (issue #82); sync not bulletproof per README (https://github.com/TheZupZup/NexaNote/issues/82) |

### Contradictions
- "Local-first" claim vs reality on desktop: the README promises notes saved on-device with no backend, but issue #82 shows the Linux desktop client cannot open its local SQLite store at all — local-first currently holds only on Android (https://github.com/TheZupZup/NexaNote vs https://github.com/TheZupZup/NexaNote/issues/82).
- Privacy-first positioning ("Your notes never touch a third-party cloud") while the entire app is distributed via GitHub Releases and Docker Hub, both third-party platforms — the note data, not the software, is the privacy boundary; worth stating precisely (https://github.com/TheZupZup/NexaNote).

Sources: https://github.com/TheZupZup/NexaNote ; https://github.com/TheZupZup/NexaNote/issues/82 ; https://github.com/TheZupZup/NexaNote/pull/80 ; https://github.com/TheZupZup/NexaNote/pull/81 ; https://www.reddit.com/r/selfhosted/comments/1si5j4s/removed_by_moderator/

## memos
### Visual surface
The defining visual is the timeline, not a folder tree: you open the app, type into a single composer, save, and the memo lands on a date-grouped feed, like a self-hosted Twitter/journal rather than a document app (https://github.com/usememos/memos, https://pickuma.com/for-dev/memos-self-hosted-markdown-note-taking/). Organization is inline `#tags` plus full-text search; memos render Markdown with syntax-highlighted code fences, tables, LaTeX, inline audio attachments, image previews with arrow-key navigation, drag-and-drop files, and a Focus Mode for distraction-free writing (https://pickuma.com/for-dev/memos-self-hosted-markdown-note-taking/). It ships as a web/PWA app (installable on phones from the browser); there is no native desktop or mobile client — third-party mobile apps exist in the ecosystem (https://pickuma.com/for-dev/memos-self-hosted-markdown-note-taking/, https://noted.lol/memos/). Marketing and comparison pages (usememos.com/compare/*) present honest side-by-side tables, including rows where Memos answers "no" — an unusually candid marketing style (https://usememos.com/compare/notesnook, https://usememos.com/compare/standard-notes).

SHOT-LIST:
- GitHub README hero: https://github.com/usememos/memos
- Official site homepage: https://usememos.com/
- Features page: https://usememos.com/features
- Compare pages (visual of honest comparison tables): https://usememos.com/compare/evernote
- Noted.lol review (in-article UI screenshots): https://noted.lol/memos/
- Live demo (official, linked from README "Demo"): https://demo.usememos.com/

### Docs analysis
- Architecture: single Go binary server (~20 MB Docker image), web front end; SQLite default, PostgreSQL/MySQL via driver flag — the only note app in this lane with a production-grade Go/Rust-class single-binary story (https://pickuma.com/for-dev/memos-self-hosted-markdown-note-taking/).
- Everything lives in one mounted folder (`~/.memos` → /var/opt/memos): "back up that one folder" — the simplest possible backup contract (https://github.com/usememos/memos).
- Versioning changed to calendar scheme `YY.MM.N` (no `v` prefix), Docker tags: `stable`, monthly (`26.10`), `canary`; upgrade requirement: coming from before v0.31.0, run v0.31.0 once first (https://github.com/usememos/memos).
- Capture ecosystem: Chrome/Firefox web clipper (saves pages/selections/images as Markdown with source link), Memogram Telegram bot, REST + gRPC APIs, official MCP server for AI tools (https://github.com/usememos/memos).
- Privacy posture: MIT license, zero telemetry; hosting cost is the user's (https://usememos.com/, https://usememos.com/features).
- Export: Markdown/JSON/CSV; import tooling is a work in progress — migrating from other apps often requires writing your own API script (https://pickuma.com/for-dev/memos-self-hosted-markdown-note-taking/).
- Sync/cloud: none built in; remote access = expose server, VPN, or tunnel (Tailscale/Cloudflare Tunnel) — a genuine barrier for non-technical users (https://pickuma.com/for-dev/memos-self-hosted-markdown-note-taking/).
- Collaboration: thin — public links per memo, microblog publishing mode; no real-time co-editing or comment threads (https://pickuma.com/for-dev/memos-self-hosted-markdown-note-taking/).
- Hard limits: no note limits or subscription tiers in the software itself (https://usememos.com/compare/evernote). No E2E encryption — the compare page states plainly "Not end to end" (https://usememos.com/compare/notesnook).
- Design decisions worth borrowing: the single-folder backup contract, honest self-comparisons as marketing, date-timeline as the only organizing metaphor, calendar versioning with canary channel (https://github.com/usememos/memos, https://usememos.com/compare/notesnook).

### Features
| Area | Detail |
|---|---|
| Model | Timeline of short Markdown memos; date-grouped; no folders/hierarchies (https://pickuma.com/for-dev/memos-self-hosted-markdown-note-taking/) |
| Editor | Markdown composer: code fences, tables, LaTeX, media, drag-drop, Focus Mode (https://pickuma.com/for-dev/memos-self-hosted-markdown-note-taking/) |
| Org | Inline #tags, full-text search (https://github.com/usememos/memos) |
| Sharing | Public memo links, microblog feed mode; shared spaces where each person keeps own memos (https://github.com/usememos/memos) |
| Capture | Web clipper, Telegram bot (Memogram), REST/gRPC API, MCP server (https://github.com/usememos/memos) |
| Data | SQLite default, Postgres/MySQL optional; single-folder backup; MD/JSON/CSV export (https://github.com/usememos/memos, https://pickuma.com/for-dev/memos-self-hosted-markdown-note-taking/) |
| Deployment | Docker/Compose/K8s/binary; port 5230 (https://github.com/usememos/memos) |
| Encryption | None E2E, stated honestly (https://usememos.com/compare/notesnook) |
| Platforms | Web/PWA only (official); third-party mobile clients in ecosystem (https://pickuma.com/for-dev/memos-self-hosted-markdown-note-taking/) |

### Sentiment
| What people say |
|---|
| Beloved as the lightweight "Twitter-like" capture tool; ~63k stars, 4.8k forks by late 2026 (https://github.com/usememos/memos/issues/6245) |
| Pickuma's May 2026 review: ideal for scratchpad-style developers; honest about no hierarchy, no collaboration, no cloud sync (https://pickuma.com/for-dev/memos-self-hosted-markdown-note-taking/) |
| Recurring pain: database migration is manual and error-prone — users hit KABOOM errors with pgloader SQLite→Postgres, removed copydb flag broke MySQL paths (https://github.com/orgs/usememos/discussions/3108, https://github.com/usememos/memos/issues/4550) |
| Upgrade-time schema migration failures have burned users (issue #3348 after updating to 0.22.0) (https://github.com/usememos/memos/issues/3348) |
| Fleet-ops notes "schema-migration hiccups on upgrade" as a known trap category (https://github.com/heyvaldemar/fleet-ops/issues/40) |
| Some users simply can't find the export feature and look for alternatives (https://www.reddit.com/r/selfhosted/comments/1r0tkqk/memos_app_or_alternative/) |
| Users confused about where data physically lands (SQLite vs mounted volume mismatch, issue #2526) (https://github.com/usememos/memos/issues/2526) |

### Wants
| What people want changed |
|---|
| One-click SQLite→Postgres migration tool (open feature request, Aug 2026) (https://github.com/usememos/memos/issues/6245) |
| Native single-memo and bulk export/import for non-technical instance migration (open, Sept 2026) (https://github.com/usememos/memos/issues/6309) |
| Easier discovery of export; better migration ergonomics overall (https://www.reddit.com/r/selfhosted/comments/1r0tkqk/memos_app_or_alternative/) |
| Some want hierarchy: it is deliberately absent — a philosophical boundary, not an omission (https://pickuma.com/for-dev/memos-self-hosted-markdown-note-taking/) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Price | Free, MIT, no tiers; hosting is your cost (https://usememos.com/) |
| Platforms | Self-hosted web/PWA (Docker, K8s, binary); ecosystem: web clipper, Telegram bot, third-party mobile apps (https://github.com/usememos/memos) |
| Limits | No note limits in software; no E2E encryption; single-user-instance-first with shared spaces (https://usememos.com/compare/evernote) |

### Contradictions
- Version numbering: earlier common knowledge describes Memos as v0.x releases (many articles still cite v0.28.0, April 2026), but current releases are calendar-tagged `YY.MM.N` (26.x) with an explicit "run v0.31.0 once first" upgrade gate — the project left the 0.x era (https://pickuma.com/for-dev/memos-self-hosted-markdown-note-taking/ vs https://github.com/usememos/memos).
- The project's own compare page claims "Memos includes every feature on any server" with no plan tiers, while Pickuma documents import tooling as "work in progress" and users report manual database gymnastics for migrations — "every feature" overstates operational completeness (https://usememos.com/compare/standard-notes vs https://github.com/usememos/memos/issues/6245).
- Widely described as "privacy-first, your data stays yours" while E2E encryption is absent (their own compare page says "Not end to end"); data stays yours but is readable by the server (https://usememos.com/compare/notesnook).

Sources: https://github.com/usememos/memos ; https://usememos.com/ ; https://usememos.com/features ; https://usememos.com/compare/notesnook ; https://usememos.com/compare/standard-notes ; https://usememos.com/compare/evernote ; https://pickuma.com/for-dev/memos-self-hosted-markdown-note-taking/ ; https://noted.lol/memos/ ; https://github.com/usememos/memos/issues/6245 ; https://github.com/usememos/memos/issues/6309 ; https://github.com/usememos/memos/issues/3348 ; https://github.com/usememos/memos/issues/2526 ; https://github.com/orgs/usememos/discussions/3108 ; https://www.reddit.com/r/selfhosted/comments/1r0tkqk/memos_app_or_alternative/

## siyuan (SiYuan)
### Visual surface
A block-based WYSIWYG knowledge workspace (TypeScript front, Go back) for desktop, mobile and self-hosted server, with a niche but distinctive feature surface: zoom-in block focus with breadcrumb navigation ("go into a block like zooming into a canvas"), a global and block-focused relationship graph, document and list outlines that complement each other, flashcards powered by the FSRS spaced-repetition algorithm, a Notion-style database layer with relation/rollup/template, and AI assist hooks to OpenAI for continue-writing, translation, abstracting, brainstorming and grammar fixes (https://b3log.org/siyuan/en/). Marketing panels show block editing, flashcards/database/AI, bidirectional links, list outline and privacy/sync as the five pillars; the app pitches itself as a place "where humans and AI agents work together" (https://b3log.org/siyuan/en/, https://apps.apple.com/us/app/siyuan/id1583226508). Data lives in a workspace folder (notebooks/assets/config) on device; sync is incremental and end-to-end encrypted (https://b3log.org/siyuan/en/, https://publish.obsidian.md/xybre/permalink/9aeaf4c2-9cfc-4d06-9e99-7a5e4b786f2d).

SHOT-LIST:
- Official English homepage (five feature panels with UI panels): https://b3log.org/siyuan/en/
- GitHub README: https://github.com/siyuan-note/siyuan
- iOS App Store screenshots: https://apps.apple.com/us/app/siyuan/id1583226508
- Google Play listing: https://play.google.com/store/apps/details?id=org.b3log.siyuan
- HomelabAddiction self-host guide (UI walkthrough screenshots): https://homelabaddiction.com/self-hosted/siyuan/

### Docs analysis
- Storage model: blocks-first with WYSIWYG; content stored as .sy JSON files with an asset pipeline; Markdown import/export supported (https://b3log.org/siyuan/en/, https://publish.obsidian.md/xybre/permalink/9aeaf4c2-9cfc-4d06-9e99-7a5e4b786f2d).
- Blocks as the only core concept: docs pages are themselves blocks; blocks convert, split, reorganize and move without breaking links — link stability under restructuring is the flagship design decision (https://b3log.org/siyuan/en/).
- 20+ block-level and 10+ span-level element types; widget blocks for extension (https://b3log.org/siyuan/en/).
- Million-word documents claimed editable via dynamic loading on ordinary computers — UNVERIFIED independently, vendor claim (https://b3log.org/siyuan/en/).
- Sync: E2E AES-GCM encrypted, incremental, key stored locally; sync targets: official paid cloud, AWS S3 direct, WebDAV, or self-hosted Docker server; mobile device doubles as a LAN server so a PC browser can use the phone's copy (https://b3log.org/siyuan/en/, https://publish.obsidian.md/xybre/permalink/9aeaf4c2-9cfc-4d06-9e99-7a5e4b786f2d).
- Offline-first: fully usable without network, "even if the cloud service is down" (https://b3log.org/siyuan/en/).
- Flashcards via FSRS algorithm built in — spaced repetition as a first-class PKM feature, rare in this space (https://b3log.org/siyuan/en/).
- Mobile server + Docker server with lock-screen password for multi-person collaboration (https://b3log.org/siyuan/en/).
- Monetization split: core app free/open-source AGPL-3.0, most features free even commercially; paid optional cloud services (sync/storage subscription) — the standard "free app + paid sync" asymmetry (https://www.promptquorum.com/power-local-llm/siyuan-review, https://openclawhub.tools/tool/siyuan/).
- AI: connect to OpenAI (BYO key pattern); local-LLM option highlighted by reviewers — UNVERIFIED whether a local-LLM provider is built-in or user-configured (https://www.promptquorum.com/power-local-llm/siyuan-review).

### Features
| Area | Detail |
|---|---|
| Editor | Block-level WYSIWYG, 20+ block elements, zoom-in focus, million-word docs claim (https://b3log.org/siyuan/en/) |
| Linking | Block references, bidirectional links, backlink panel w/ filter+search, global + focused graphs (https://b3log.org/siyuan/en/) |
| Outlines | Document + list outlines, folding incl. heading blocks (https://b3log.org/siyuan/en/) |
| Database | Relation, rollup, template; two DBs linkable (https://b3log.org/siyuan/en/) |
| Memory | FSRS flashcards built in (https://b3log.org/siyuan/en/) |
| AI | OpenAI hooks: continue, translate, abstract, brainstorm, grammar (https://b3log.org/siyuan/en/) |
| Sync | E2E AES-GCM incremental; official cloud, S3, WebDAV, Docker self-host; phone-as-LAN-server (https://b3log.org/siyuan/en/) |
| Platforms | Windows/macOS/Linux desktop, Android/iOS apps, browser access to self-hosted server (https://b3log.org/siyuan/en/) |

### Sentiment
| What people say |
|---|
| "Siyuan compared to Obsidian feels like switching to JetBrains IDEs from VS Code... a sleeper" — powerful but heavier (https://www.reddit.com/r/PKMS/comments/1jwk9sw/siyuan_notes_a_hidden_pkms_gem/) |
| Repeated complaint of clunkiness: "felt clunky and a bit rough" (https://www.reddit.com/r/PKMS/comments/1kaojm7/why_siyuan_is_not_popular/) |
| Complexity + documentation quality are the top reasons it's niche; "documentation sucked" per one PKMS thread (https://www.reddit.com/r/PKMS/comments/1l3flyz/logseq_x_siyuan_chinese_developers/) |
| Self-hosted server doesn't pair with the official mobile clients' sync the way users expect; one user dropped it over mobile+SWA (https://www.reddit.com/r/ObsidianMD/comments/1nzh6fx/have_you_guys_tried_siyuan/) |
| Onboarding/registering/paying called painful (https://www.reddit.com/r/SiyuanPKM/comments/17zolsm/how_has_siyuan_helped_you_so_far/) |
| Yunnan-based developer ownership (App Store metadata) spooks some Western privacy-focused users (https://www.reddit.com/r/PKMS/comments/1928euo/i_tested_some_apps_to_build_a_second_brainpkms/) |
| Fans praise local-first by default, true block identity, cleaner WYSIWYG (https://www.reddit.com/r/PKMS/comments/1jwk9sw/siyuan_notes_a_hidden_pkms_gem/) |

### Wants
| What people want changed |
|---|
| Better English documentation and onboarding (https://www.reddit.com/r/PKMS/comments/1l3flyz/logseq_x_siyuan_chinese_developers/) |
| Smoother self-host-sync-to-official-mobile path (https://www.reddit.com/r/ObsidianMD/comments/1nzh6fx/have_you_guys_tried_siyuan/) |
| Less clunky UI; gentler learning curve (https://www.reddit.com/r/PKMS/comments/1kaojm7/why_siyuan_is_not_popular/) |
| Cleaner export to standard Markdown for exit (https://www.reddit.com/r/ObsidianMD/comments/1izr85c/how_good_is_siyuan_as_an_alternative_to_notion/) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | Full core app, AGPL-3.0, commercial use allowed (https://www.promptquorum.com/power-local-llm/siyuan-review) |
| Paid | Optional official cloud services (sync/storage) via subscription; pricing figures not verified this pass — UNVERIFIED (https://b3log.org/siyuan/en/) |
| Platforms | Windows, macOS, Linux, Android, iOS, Docker self-host, browser (https://apps.apple.com/us/app/siyuan/id1583226508, https://b3log.org/siyuan/en/) |

### Contradictions
- Community describes self-hosting as awkward with mobile clients, while official marketing sells the Docker server as "build your own cloud notes" for multi-person collaboration — both true, but the official mobile apps' sync against self-hosted servers is the friction point (https://b3log.org/siyuan/en/ vs https://www.reddit.com/r/ObsidianMD/comments/1nzh6fx/have_you_guys_tried_siyuan/).
- Marketed as "privacy-first" while being built by a Yunnan-based company; users' trust calculus conflicts with the technical privacy design (E2EE keys stored locally) (https://b3log.org/siyuan/en/ vs https://www.reddit.com/r/PKMS/comments/1928euo/i_tested_some_apps_to_build_a_second_brainpkms/).
- Some aggregators (openclawhub) list a competitor comparison calling SiYuan "outline-first editing paradigm" while the official pitch is block-first with outlines as a secondary pillar (https://openclawhub.tools/tool/siyuan/ vs https://b3log.org/siyuan/en/).

Sources: https://b3log.org/siyuan/en/ ; https://github.com/siyuan-note/siyuan ; https://apps.apple.com/us/app/siyuan/id1583226508 ; https://www.promptquorum.com/power-local-llm/siyuan-review ; https://homelabaddiction.com/self-hosted/siyuan/ ; https://publish.obsidian.md/xybre/permalink/9aeaf4c2-9cfc-4d06-9e99-7a5e4b786f2d ; https://www.reddit.com/r/PKMS/comments/1jwk9sw/siyuan_notes_a_hidden_pkms_gem/ ; https://www.reddit.com/r/PKMS/comments/1kaojm7/why_siyuan_is_not_popular/ ; https://www.reddit.com/r/ObsidianMD/comments/1nzh6fx/have_you_guys_tried_siyuan/ ; https://www.reddit.com/r/PKMS/comments/1928euo/i_tested_some_apps_to_build_a_second_brainpkms/

## Xournal++
### Visual surface
A native GTK3 C++ app that looks like a classic Linux utility: a toolbar area at top (multiple predefined and fully customizable toolbars, optimizable for portrait or landscape), a main canvas where you write with pressure-sensitive stylus input on paper backgrounds (note-taking, scratch paper, whiteboarding) or on top of a loaded PDF, and a sidebar with page previews, advanced page sorting, PDF bookmarks and a layer panel where layers can be individually hidden or edited (https://github.com/xournalpp/xournalpp). Multiple page backgrounds (ruled, lined, graph) selectable straight from the toolbar; over 20 interface languages (https://github.com/xournalpp/xournalpp). Desktop only in official form: Windows 10/11 (winget/Scoop/MS Store), Linux (deb, Flatpak, AppImage, distro repos), macOS (with signing workarounds); a Flutter mobile/web app exists for Android via F-Droid but the project is stalled (https://github.com/xournalpp/xournalpp).

SHOT-LIST:
- GitHub README screenshots table (GNU/Linux, Windows 10, macOS Catalina, ChromeOS mobile, toolbars, layer sidebar): https://github.com/xournalpp/xournalpp
- Official website user guide: https://xournalpp.github.io/
- User Manual wiki: https://github.com/xournalpp/xournalpp/wiki/User-Manual
- Releases page (per-platform binaries): https://github.com/xournalpp/xournalpp/releases
- OMG! Ubuntu walkthrough article with screenshots: https://www.omgubuntu.co.uk/2019/06/xournalpp-handwritten-notes-app-linux

### Docs analysis
- PDF annotation is the anchor: annotate on top of PDFs, select/copy/highlight/underline/strikethrough text from the background PDF, follow links from it (https://github.com/xournalpp/xournalpp).
- Drawing toolset: pen/highlighter/eraser with multiple configs, stroke styles (solid/dotted), shapes (line, arrow, circle, rectangle, spline), fill, resize/rotate, rotation and grid snapping, input stabilization, set-square and compass tools for measurement/guided arcs — an unusual physical-instrument metaphor (https://github.com/xournalpp/xournalpp).
- LaTeX support with customizable template and resizable syntax-highlighted editor (requires LaTeX install; Flatpak needs the TeX Live extension) (https://github.com/xournalpp/xournalpp).
- Audio recording/playback alongside notes — note+audio sync for lectures (https://github.com/xournalpp/xournalpp).
- Extensibility: Lua-scripted plugins (ColorCycle, Export, HighlightPosition ship as examples); .gpl color palettes; page templates; button mapping per stylus/mouse button (https://github.com/xournalpp/xournalpp).
- File format, the critical design lesson: .xopp is gzipped XML and PDFs are NOT embedded — delete the PDF and the background is lost; a new format that stores PDFs/attachments internally is being introduced (#937). Legacy .xoj compatible with Xournal, with Xournal++-only features lost on export (https://github.com/xournalpp/xournalpp).
- Export: SVG/PNG/PDF from GUI and command line (CLI export is a nice automation surface) (https://github.com/xournalpp/xournalpp).
- Mobile story officially stalled: 2020-2021 Flutter app (Android/iOS/web) "development has stalled and we have lost contact to the (single) developer"; web app withdrawn; iOS never published — bus-factor risk made explicit (https://github.com/xournalpp/xournalpp).
- Hard limits: macOS release refuses to run until users manually `xattr -c` + re-codesign (Apple policy) (https://github.com/xournalpp/xournalpp); official Debian/Ubuntu binaries are distro-version-locked (https://github.com/xournalpp/xournalpp); no cloud, no sync, single-file local model — by design (https://github.com/xournalpp/xournalpp).

### Features
| Area | Detail |
|---|---|
| Handwriting | Pressure-sensitive stylus (Wacom/Huion/XP Pen), input stabilization, eraser configs (https://github.com/xournalpp/xournalpp) |
| PDF | Annotate, text select/highlight/strike, bookmark sidebar, link following (https://github.com/xournalpp/xournalpp) |
| Drawing | Shapes, fill, snap/rotate, set-square+compass, layers (https://github.com/xournalpp/xournalpp) |
| Text/LaTeX | Text tool with fonts; LaTeX with templates (https://github.com/xournalpp/xournalpp) |
| Audio | Record+playback alongside notes (https://github.com/xournalpp/xournalpp) |
| Extensibility | Lua plugins, customizable toolbars, button mapping, .gpl palettes, templates (https://github.com/xournalpp/xournalpp) |
| Export | SVG/PNG/PDF via GUI + CLI; import .xoj; .xopp gzipped XML (https://github.com/xournalpp/xournalpp) |
| Collaboration/sync | None — local single-file app (https://github.com/xournalpp/xournalpp) |
| Platforms | Linux (deb/Flatpak/AppImage/distro repos), Windows 10+ (exe/MS Store/winget/Scoop), macOS (manual signing fix), Android via stalled Xournal++ Mobile (F-Droid); iOS unpublished (https://github.com/xournalpp/xournalpp) |

### Sentiment
| What people say |
|---|
| Appreciation posts on r/linux: many love it as the PDF-annotation workhorse (https://www.reddit.com/r/linux/comments/xurw00/xournal_appreciation_post/) |
| Teachers/students rely on it for student-submitted PDF markup (SourceForge reviews) (https://sourceforge.net/projects/xournal.mirror/reviews/) |
| Harsh counterpart: "most unoptimized writing app I have ever come across", crashes on Ubuntu, stylus button press not recognized (https://github.com/xournalpp/xournalpp/discussions/5865) |
| Crashes persist into 2026 (issue #7857, one week old; fresh bug issues opened Oct 2026) (https://github.com/xournalpp/xournalpp/issues/7857, https://github.com/xournalpp/xournalpp/issues) |
| ChromeOS: "app randomly closes when I try to zoom" (https://www.reddit.com/r/chromeos/comments/14xp8o0/xournal_is_now_fully_supported_with_chromeos_115/) |
| AppImage printing broken on MX-Linux; 1.2.10 AppImage "does not open at all" (https://sourceforge.net/projects/xournal.mirror/reviews/) |
| Older verdict echoing: "too buggy, unstable and a UX mess" (https://www.reddit.com/r/Ubuntu/comments/c8a5o1/software_recommendation_lighter_version_of_xournal/) |
| Privacy-minded users value it because no data goes to AI/cloud, but find formatting and spell/grammar support lacking (https://www.reddit.com/r/privacy/comments/1lfyttt/alternative_to_xournal/) |

### Wants
| What people want changed |
|---|
| Stability (crashes during zoom, on save, platform-specific) (https://github.com/xournalpp/xournalpp/issues/7857) |
| An iOS app (buildable preview exists, no store release) (https://github.com/xournalpp/xournalpp) |
| Text/formatting polish, spell/grammar tools for typists (https://www.reddit.com/r/privacy/comments/1lfyttt/alternative_to_xournal/) |
| PDF-embedding file format (in progress, #937) (https://github.com/xournalpp/xournalpp) |
| Revival of the mobile app (https://github.com/xournalpp/xournalpp) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Price | Free, GPL, no paid tier (https://github.com/xournalpp/xournalpp) |
| Platforms | Linux, Windows 10+, macOS (signing workaround), ChromeOS via Debian container, Android (stalled mobile app); iOS unpublished (https://github.com/xournalpp/xournalpp) |
| Limits | No sync/cloud; PDF backgrounds external; distro-version-locked official binaries (https://github.com/xournalpp/xournalpp) |

### Contradictions
- A 2020 community post announced "Mobile is on the way!" for Android/iOS/web; the current README states the mobile app stalled, the web app is withdrawn, and the single developer was lost — the mobile promise quietly died (https://www.reddit.com/r/opensource/comments/ie1mum/xournal_is_an_open_source_handwriting_note_taking/ vs https://github.com/xournalpp/xournalpp).
- Positioned as fast/lean vs Electron apps, yet a sizable user group reports crashes and unresponsiveness — "fast" is true of the C++ core, not consistently of the experience (https://github.com/xournalpp/xournalpp vs https://github.com/xournalpp/xournalpp/discussions/5865).

Sources: https://github.com/xournalpp/xournalpp ; https://github.com/xournalpp/xournalpp/wiki/User-Manual ; https://xournalpp.github.io/ ; https://www.omgubuntu.co.uk/2019/06/xournalpp-handwritten-notes-app-linux ; https://github.com/xournalpp/xournalpp/discussions/5865 ; https://github.com/xournalpp/xournalpp/issues/7857 ; https://sourceforge.net/projects/xournal.mirror/reviews/ ; https://www.reddit.com/r/chromeos/comments/14xp8o0/xournal_is_now_fully_supported_with_chromeos_115/ ; https://www.reddit.com/r/privacy/comments/1lfyttt/alternative_to_xournal/ ; https://www.reddit.com/r/linux/comments/xurw00/xournal_appreciation_post/

## RNote
### Visual surface
A GTK4/Rust vector drawing app for stylus work with an adaptive UI that reshapes itself for big and small screens: toolbar with pen styles (pressure-sensitive, configurable stroke styles), a shape tool, a selection tool that moves/rotates/resizes/modifies existing strokes, and a workspace browser sidebar for quick access to related files (https://github.com/flxzt/rnote, https://rnote.flxzt.net/). Documents live on expansion layouts of the user's choice: fixed pages, continuous vertical, infinite in every direction, with customizable page formats, background colors/patterns/sizes; tabs let you keep several documents open; there are optional pen sounds and reconfigurable stylus-button shortcuts (https://github.com/flxzt/rnote). Bundled fonts are characterful (handwritten Grape Nuts, the dyslexia-designed OpenDyslexic, the typewriter TT2020, Excalidraw's Virgil) — a deliberate sketchbook aesthetic (https://rnote.flxzt.net/). Rough.js algorithms power the rough-shape look, and Pizarra is credited as the architectural inspiration — the design language is "digital paper", not a productivity suite (https://github.com/flxzt/rnote).

SHOT-LIST:
- Project website (hero + screenshots strip): https://rnote.flxzt.net/
- GitHub README "Screenshots" section: https://github.com/flxzt/rnote
- Flathub listing (screens + metadata): https://flathub.org/apps/com.github.flxzt.rnote
- Releases page (Windows/macOS installers): https://github.com/flxzt/rnote/releases
- It's FOSS review article (in-article screenshots): https://itsfoss.com/news/rnote-0-9-released/

### Docs analysis
- Vector-based drawing core, targeted at students/teachers/drawing-tablet owners — the "digital sketchbook" niche, not text notes (https://github.com/flxzt/rnote).
- Import: PDF, bitmap, SVG; export: documents to SVG/PDF/Xopp (Xournal++ interop!), pages and selections to SVG/PNG/JPEG; native .rnote = gzipped JSON; autosave; printing; tabs; drag & drop (https://github.com/flxzt/rnote).
- .rnote format is explicitly unstable with breaking changes at v0.2/0.3/0.4/0.5 — docs provide flatpak downgrade-by-commit instructions, an honest compatibility stance worth borrowing (tell users exactly how to roll back) (https://github.com/flxzt/rnote).
- CLI companion (rnote-cli, run via flatpak command) for automating .rnote file handling (https://github.com/flxzt/rnote).
- Platform notes are candid: X11 unsupported (GTK4 Wayland story), Windows build ships but suffers a GTK4 black-border bug; flatpak permission issues (Flatseal fixes) documented as "Pitfalls" — rare docs honesty (https://github.com/flxzt/rnote).
- Funding model: GitHub Sponsors/Liberapay to the single original author; sponsor goals tied to buying a PineNote/linux phone to port Rnote — mobile is a funding-dependent roadmap item, not a plan (https://rnote.flxzt.net/).
- GPL-3.0-or-later; community via Matrix rooms (#rnote, #rnote-dev) and GitHub Discussions (https://github.com/flxzt/rnote).
- No sync, no cloud, no collaboration, no text-heavy note management (files managed by the OS workspace) — single-document model like a real notebook app (https://github.com/flxzt/rnote).
- Hard limits: none on documents documented; the format instability IS the operational limit — UNVERIFIED beyond the stated breaking changes (https://github.com/flxzt/rnote).

### Features
| Area | Detail |
|---|---|
| Input | Stylus-first, pressure-sensitive, stroke styles, shape tool, palm-rejection caveats (https://github.com/flxzt/rnote) |
| Canvas | Infinite/continuous/fixed-page layouts, custom page formats, backgrounds, tabs (https://rnote.flxzt.net/) |
| Annotation | PDF/bitmap/SVG import for markup (https://github.com/flxzt/rnote) |
| Export | SVG/PDF/Xopp, pages/selections to SVG/PNG/JPEG (https://github.com/flxzt/rnote) |
| Files | .rnote = gzipped JSON; unstable, versioned breaks; autosave; CLI (https://github.com/flxzt/rnote) |
| Extras | Pen sounds, stylus-button shortcuts, workspace browser, printing (https://github.com/flxzt/rnote) |
| Platforms | Linux (Flatpak official), Windows (installer/winget), macOS (app bundle); no mobile yet (https://github.com/flxzt/rnote, https://rnote.flxzt.net/) |

### Sentiment
| What people say |
|---|
| Linux-community favorite: OMG! Ubuntu and It's FOSS covered v0.9 positively; FOSS decrees it "a top handwriting app for Linux" (https://itsfoss.com/news/rnote-0-9-released/, https://www.fosslinux.com/47057/rnote-handwriting-app-linux.htm) |
| GreatNotes-style praise: "interface is incredibly streamlined, smoothest writing experience of all the apps I've tried", dark theme done right (https://github.com/flxzt/rnote/issues/52) |
| Consensus: better than Xournal++ for looks and flow, but users want shape filling, PDF import as pages, resizing existing strokes, bookmarks/insert blank page between pages (https://www.reddit.com/r/linux/comments/x62290/rnote_v0550_has_been_released_notesketch_app_for/) |
| Known rough spots in threads: pressure sensitivity glitches, occasional slowness, crashes, incompatibility blocks between file format versions (https://www.reddit.com/r/kde/comments/13hbujz/rnote_is_a_perfect_example_of_why_linux_cannot/) |
| Windows users report usability issues (touch/touchpad pinch zooming, light-theme adaptation problems) (https://www.reddit.com/r/windows8/comments/1dypvfn/rnote_is_a_great_application_for_writing_notes/) |
| Flatpak sandbox friction (drag & drop permissions) is a recurring support topic (https://github.com/flxzt/rnote/issues/329) |
| One cynical take: "a perfect example of why Linux cannot attract developers... immature UI" — the maturity gap is real but contested (https://www.reddit.com/r/kde/comments/13hbujz/rnote_is_a_perfect_example_of_why_linux_cannot/) |

### Wants
| What people want changed |
|---|
| Fill shapes (raised many times) (https://www.reddit.com/r/linux/comments/x62290/rnote_v0550_has_been_released_notesketch_app_for/) |
| Import PDFs as pages, not just background (https://www.reddit.com/r/linux/comments/x62290/rnote_v0550_has_been_released_notesketch_app_for/) |
| Stable file format without version breakage (https://github.com/flxzt/rnote) |
| Mobile/tablet ports (Linux phone, PineNote) — explicitly gated on sponsorship (https://rnote.flxzt.net/) |
| Better Windows experience (https://www.reddit.com/r/windows8/comments/1dypvfn/rnote_is_a_great_application_for_writing_notes/) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Price | Free, GPL-3.0+; donation-funded (GitHub Sponsors/Liberapay) (https://rnote.flxzt.net/) |
| Platforms | Linux Flatpak (official), Windows installer/winget, macOS app bundle; no mobile (https://github.com/flxzt/rnote) |
| Limits | X11 unsupported; format instability; flatpak sandbox permissions (https://github.com/flxzt/rnote) |

### Contradictions
- Website pitch targets "students, teachers and those who own a drawing tablet", yet much of the friction (X11 rejection, Flatseal permissions, pen-button remapping hacks) falls hardest on exactly that audience on mainstream hardware; the polished screenshot story vs. documented pitfalls is the app's central tension (https://rnote.flxzt.net/ vs https://github.com/flxzt/rnote).
- Xournal++ export/import interop (Xopp) exists, but the two apps' communities describe them as competitors rather than complements (https://github.com/flxzt/rnote vs https://www.reddit.com/r/kde/comments/13hbujz/rnote_is_a_perfect_example_of_why_linux_cannot/).

Sources: https://github.com/flxzt/rnote ; https://rnote.flxzt.net/ ; https://itsfoss.com/news/rnote-0-9-released/ ; https://github.com/flxzt/rnote/issues/52 ; https://github.com/flxzt/rnote/issues/329 ; https://www.reddit.com/r/linux/comments/x62290/rnote_v0550_has_been_released_notesketch_app_for/ ; https://www.reddit.com/r/kde/comments/13hbujz/rnote_is_a_perfect_example_of_why_linux_cannot/ ; https://www.reddit.com/r/windows8/comments/1dypvfn/rnote_is_a_great_application_for_writing_notes/ ; https://flathub.org/apps/com.github.flxzt.rnote

## MyScript / Nebo (now "MyScript Notes")
### Visual surface
The handwriting-recognition company behind the Interactive Ink engine sells the Nebo app, rebranded "MyScript Notes"; the note surface is page types rather than one editor: Notebooks (Goodnotes-like, cover/title, page size/orientation/color, blank/dotted/lined/grid templates, images only), Documents (lined pages where handwriting is actively recognized and converted, where text and handwriting mix even mid-sentence, and where dedicated section types add sketches, images, diagrams, math and boards), Boards (freeform infinite-canvas brainstorming, nothing auto-converts, lasso+Convert on demand), and imported PDFs (word-processor-style editing, type, boxes, colored backgrounds, thumbnail sidebar, page rearranging, export with annotations flattened) (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review). Signature live UI elements: a real-time conversion preview in the upper-left showing the recognized text as you write, a pen-customization test window where you try nib/brush/fountain pens and thicknesses before committing, and gesture formatting (underline twice for title, underline once for bold, box to highlight, draw bullets for lists, scratch-out to erase, vertical line to break letters, upward line to join) that works on typed text too (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review). Platforms: iOS, iPadOS, Mac, Android, Windows; one purchase covers up to 10 devices across ecosystems (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review).
SHOT-LIST:
- Paperlike review (annotated UI screenshots of Notebooks/Documents/Boards/PDFs, tools, gestures, org): https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review
- r/NeboApp subreddit (user screenshots, UI-revamp previews — an Android UI revamp was announced there): https://www.reddit.com/r/NeboApp/
- CNET review page (historic screenshots of equation/diagram conversion): https://www.cnet.com/reviews/myscript-nebo-review/
- Official pages https://www.myscript.com and https://www.myscript.com/nebo (not reachable by the fetch tooling in this pass — UNVERIFIED current marketing copy; SDK repos https://github.com/MyScript/MyScriptJS and https://github.com/MyScript/interactive-ink-examples-ios likewise unverified this pass)

### Docs analysis
- The engine, not the app, is the asset: Interactive Ink converts handwriting live, reflows handwriting like typed text when the display area changes (no shrinking), recognizes and solves math equations, converts drawn shapes (basic shapes + arrows; Venn overlaps OK; triangles failed in testing) into editable vector diagram objects that stay interactive when pasted into PowerPoint/Keynote (https://www.cnet.com/reviews/myscript-nebo-review/, https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review).
- Block model: you create blocks for non-text content (images, camera shots, drawings, diagrams, equations) — content-type-aware capture is the trade for solving/recognizing it; costs speed, gains structure (https://www.cnet.com/reviews/myscript-nebo-review/).
- Math: handwritten equations convert to text and calculate; export as LaTeX or image — chem equations also supported per Paperlike (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review).
- Dictionary: onboard custom-word dictionary for recognition, one word at a time — a UX weakness worth learning from (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review).
- AI (2026): summarize/explain, create quizzes, answer questions from your notes; AI Study Sets iOS-first, Android "coming soon" (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review).
- Org model: Collections → Folders → Notes, three levels only; every page type (notebook/doc/board/PDF) is a note; unlimited-scrolling pages make long lessons awkward — a structural ceiling reviewers call insufficient for serious PKM (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review).
- Search spans handwriting, PDF annotations, and diagram text (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review).
- Sync/backup: MyScript account sync plus iCloud/Google Drive/Dropbox manual sync; whole-library backup as a proprietary .MyScriptNotesbackup file; export PDF/Word/PNG/SVG + proprietary format; web publishing via create-link with contact-list or open access (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review).
- Pricing: free 7-day trial (most features, limited pages), $1.99/mo or $7.99/yr, $24.99 lifetime; legacy Nebo lifetime holders keep lifetime access (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review).
- Hard limits: requires active-stylus hardware for the core experience (passive pens/fingers lose precision); passive stylus still works; recognition needs writing within lines — oversized handwriting auto-disappears unless line size is adjusted (https://www.cnet.com/reviews/myscript-nebo-review/, https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review).
- UNVERIFIED this pass: official marketing pages and the MyScriptJS/iOS SDK repos (fetch tooling refused them); SDK claims about Interactive Ink web/iOS integrations could not be confirmed.

### Features
| Area | Detail |
|---|---|
| Surfaces | Notebooks, Documents (recognized), Boards (freeform), PDF import (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review) |
| Recognition | Live conversion preview, best-in-class cursive/sloppy accuracy, reflow, gestures on typed text (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review) |
| Math | Handwritten equations → text + solver, LaTeX/image export, chemical equations (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review) |
| Diagrams | Hand-drawn → editable vectors; survives into PowerPoint/Keynote (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review) |
| Tools | Felt/brush/fountain pens w/ test window, smart highlighter (snaps to line), stroke eraser picking single letters, precise eraser, lasso (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review) |
| AI | Summarize/explain/quizzes/AI Study Sets from your notes (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review) |
| Org | 3-level collections/folders/notes, full-library search over handwriting (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review) |
| Platforms | iOS/iPadOS/Mac/Android/Windows, 1 purchase ≤10 devices (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review) |

### Sentiment
| What people say |
|---|
| Paperlike (updated Jan 2026): recognition "insanely good"; single cross-platform purchase is unique in the category; verdict: great compromise between Apple Notes and Goodnotes/Notability (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review) |
| Same review's caveats: three-level org too shallow, no template customization, hex-code colors missing, dictionary slow (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review) |
| CNET (2017, historic): best handwriting recognition tested, but finicky; palm rejection on Windows pulled up taskbar/launched apps; persistent un-dismissable sign-in banner; recognition inconsistent (https://www.cnet.com/reviews/myscript-nebo-review/) |
| CNET: converting to text discards the handwritten visual, forcing verification against memory — a data-fidelity complaint (https://www.cnet.com/reviews/myscript-nebo-review/) |
| UNVERIFIED this pass: current Reddit sentiment (r/NeboApp fetch refused); historic complaints about sync and file-format lock-in are known from general discourse but not re-verified here |

### Wants
| What people want changed |
|---|
| Deeper organization than three levels (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review) |
| Keep the handwriting visible/verifiable after conversion (historic, CNET) (https://www.cnet.com/reviews/myscript-nebo-review/) |
| Templates/customization parity with Goodnotes-class apps (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review) |
| Android parity for AI Study Sets (announced "coming soon") (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Trial | Free 7 days, most features, limited pages (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review) |
| Subscription | $1.99/month or $7.99/year, full features (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review) |
| Lifetime | $24.99 one-time, all current features + future updates (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review) |
| Platforms | iOS, iPadOS, macOS, Android, Windows; one purchase across ≤10 devices (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review) |
| Hardware | Active stylus strongly required for core experience (https://www.cnet.com/reviews/myscript-nebo-review/) |

### Contradictions
- Naming: virtually all older coverage (and common knowledge) calls the app Nebo; since the 2025/2026 rebrand it is "MyScript Notes" and the company confirms the app is "still mostly the same" — searches for "Nebo" and "MyScript Notes" return the same product (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review).
- Pricing model flipped: 2017 CNET describes a $9 one-time purchase; 2026 reality is subscription-with-lifetime-option — earlier rounds recording "one-time purchase" should be updated (https://www.cnet.com/reviews/myscript-nebo-review/ vs https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review).
- 2017: Android "forthcoming" and conversion destroys the original handwriting; 2026: Android shipped, and conversion is previewable non-destructively in the flow — the product changed materially (https://www.cnet.com/reviews/myscript-nebo-review/ vs https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review).

Sources: https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review ; https://www.cnet.com/reviews/myscript-nebo-review/ ; https://www.reddit.com/r/NeboApp/ (not fetched)

## Supernote ecosystem (Ratta Supernote + third-party tooling)
### Visual surface
Supernote is an e-ink hardware line, not an app: currently the A5X2 Manta (10.3", 300 PPI) and A6X2 Nomad (7.8"), successors to the A5X/A6X generation, deliberately shipped with no backlight to keep the paper look, and using EMR styluses (the review unit paired a LAMY Safari Vista EMR pen) whose nib rides close to the display so handwriting lands with minimal parallax (https://www.itpro.com/hardware/tablets/supernote-a5-x2-manta-review-a-premium-e-ink-tablet-thats-still-somewhat-spartan, https://supernote.com/pages/what-upgrades-does-supernote-a5-x2-have). The on-device UI is spartan by design: reviews describe a menu-light writing-first interface built around headings, keywords, digests and layers, with a lasso that stays fluid for moving drawn elements, and reviewers' one-line verdict is "arguably the most uncompromising E-Ink note-taking tablet available today" (https://www.itpro.com/hardware/tablets/supernote-a5-x2-manta-review-a-premium-e-ink-tablet-thats-still-somewhat-spartan, https://www.ereadersforum.com/threads/great-but-too-expensive-supernote-a5x2-manta-review.3829/). Ratta advertises a modular hardware design (A6X2 units upgradable toward A5X2 internals), gyroscope-driven rotation, and pen-nib options tuned for different feels (https://supernote.com/pages/what-upgrades-does-supernote-a5-x2-have). Official documentation lives at ratta.helpjuice.com with a downloadable user-manual PDF (https://ratta.helpjuice.com/?kb_language=en_US, https://ib.supernote.com/V2.6_EN.pdf), but the help-center pages are JS-rendered and returned no readable content to non-browser fetching — breadth of official docs is UNVERIFIED this pass.

SHOT-LIST:
- Official A5X2 upgrades page (hardware design shots): https://supernote.com/pages/what-upgrades-does-supernote-a5-x2-have
- Official help center home: https://ratta.helpjuice.com/?kb_language=en_US
- Official user manual PDF V2.6: https://ib.supernote.com/V2.6_EN.pdf
- YouTube review footage (see Video evidence below): https://www.youtube.com/watch?v=GwrF5Ibevf8 and https://www.youtube.com/watch?v=oQBZKqL_23o
- eReadersForum review threads (in-thread screenshots): https://www.ereadersforum.com/threads/great-but-too-expensive-supernote-a5x2-manta-review.3829/ ; https://www.ereadersforum.com/threads/supernote-manta-a5x2-in-depth-review-of-the-10-7-300ppi-enote-tablet-truly-is-for-those-who-write.4266/
- ITPro Manta review (in-article photos): https://www.itpro.com/hardware/tablets/supernote-a5-x2-manta-review-a-premium-e-ink-tablet-thats-still-somewhat-spartan

### Docs analysis
- File format is the central design fact: notes are a proprietary `.note` binary. In January 2021 Ratta told the community it planned to open the format "in April, when the data structure is stable"; a May 2024 thread titled "Release the spec of the .note file" shows the spec still unopened three years later, with users reverse-engineering the container (e.g. muting a pen stroke by setting the 5th byte to FF across all sub-containers) (https://www.reddit.com/r/Supernote/comments/kv7ccz/the_spec_for_the_note_file_format/, https://www.reddit.com/r/Supernote/comments/1cyopn7/release_the_spec_of_the_note_file/).
- Because the spec is closed, the third-party ecosystem reconstructs it: jya-dev/supernote-tool is an unofficial Python tool (pip package `supernotelib`) that converts `*.note` files to PNG/SVG/PDF entirely off-device, with colorization via four replacement hex codes in order black, darkgray, gray, white (#fefefe for white since #ffffff means transparent), vector-PDF handwriting via `--pdf-type vector`, text extraction of the device's real-time recognition results (firmware Chauvet 2.7.21+), a metadata-JSON dump via `supernote-tool analyze`, and multi-threaded conversion (https://github.com/jya-dev/supernote-tool/blob/master/README.md).
- supernote-tool documents exact per-generation compatibility: .note from A5 (SN100.B000.432), A6X and A5X (Chauvet 2.25.39), A6X2 and A5X2 (Chauvet 3.28.42) — reverse-engineers must track firmware evolution per hardware generation, a maintenance burden that follows directly from the closed format (https://github.com/jya-dev/supernote-tool/blob/master/README.md).
- The tool is Apache-2.0, explicitly "under development and may change", and community-maintained even for its packaging (Nix support is community) (https://github.com/jya-dev/supernote-tool/blob/master/README.md).
- Companion unofficial desktop tooling exists: qiaodenghui/Supernote is an unofficial cross-platform QML/C++ desktop app that opens and operates .note files by drag-and-drop or double-click (https://github.com/qiaodenghui/Supernote).
- Official documentation exists as a versioned user-manual PDF ("Supernote X User Manual V2.6") covering standard-note tools and notebook creation, but per-page docs breadth could not be verified (help center unfetchable) — UNVERIFIED (https://ib.supernote.com/V2.6_EN.pdf, https://ratta.helpjuice.com/?kb_language=en_US).
- Design decisions worth borrowing: per-generation firmware-tagged format compatibility tracking, and an `analyze` mode that dumps internal metadata as JSON for developers (https://github.com/jya-dev/supernote-tool/blob/master/README.md).
- Official marketing sells hardware-level virtues (modularity, rotation, nib feel) rather than software lock-in — the ecosystem story lives entirely in the community, not the vendor's docs (https://supernote.com/pages/what-upgrades-does-supernote-a5-x2-have).
- Cloud/sync story: not confirmed this pass (help center unfetchable) — UNVERIFIED.

### Features
| Area | Detail |
|---|---|
| Hardware | A5X2 Manta (10.3", 300 PPI), A6X2 Nomad (7.8"); no backlight; EMR pens (LAMY Safari Vista EMR) (https://www.itpro.com/hardware/tablets/supernote-a5-x2-manta-review-a-premium-e-ink-tablet-thats-still-somewhat-spartan) |
| Writing UI | Headings, keywords, digests, layers; fluid lasso; menu-light (https://www.itpro.com/hardware/tablets/supernote-a5-x2-manta-review-a-premium-e-ink-tablet-thats-still-somewhat-spartan) |
| File format | Proprietary .note binary; spec promised open in 2021, never published; firmware-tagged per generation (https://www.reddit.com/r/Supernote/comments/kv7ccz/the_spec_for_the_note_file_format/, https://github.com/jya-dev/supernote-tool/blob/master/README.md) |
| Export (official) | User-manual PDF documents standard-note tools; PDF export exists but breadth UNVERIFIED (https://ib.supernote.com/V2.6_EN.pdf) |
| Export (community) | supernote-tool: .note → PNG/SVG/PDF/vector PDF, colorize, RRT text extraction, metadata JSON dump (https://github.com/jya-dev/supernote-tool/blob/master/README.md) |
| Desktop (community) | qiaodenghui/Supernote: QML/C++ unofficial desktop editor for .note (https://github.com/qiaodenghui/Supernote) |
| Platforms | Dedicated e-ink devices only; no phone/desktop app verified this pass — UNVERIFIED (https://supernote.com/pages/what-upgrades-does-supernote-a5-x2-have) |

### Sentiment
| What people say |
|---|
| ITPro: "a real joy to use", glides "with just enough friction to feel reasonably like using a rollerball pen on a crisp sheet of paper"; one of the most seamless e-ink experiences on the market (https://www.itpro.com/hardware/tablets/supernote-a5-x2-manta-review-a-premium-e-ink-tablet-thats-still-somewhat-spartan) |
| Same review: no backlight is a real downside in the dark (plane cabin, taxi); "That look and feel doesn't come cheap" — $607 with pen and cover, "a hard sell" (https://www.itpro.com/hardware/tablets/supernote-a5-x2-manta-review-a-premium-e-ink-tablet-thats-still-somewhat-spartan) |
| eReadersForum verdict: "Great, but (too?) expensive"; in-depth review calls it "a complete redesign... a lot of excellence... but at quite a price" (https://www.ereadersforum.com/threads/great-but-too-expensive-supernote-a5x2-manta-review.3829/, https://www.ereadersforum.com/threads/supernote-manta-a5x2-in-depth-review-of-the-10-7-300ppi-enote-tablet-truly-is-for-those-who-write.4266/) |
| Reddit community's standing gripe is format lock-in: three-plus years of threads asking Ratta to release the .note spec; users byte-hack files to work around it (https://www.reddit.com/r/Supernote/comments/1cyopn7/release_the_spec_of_the_note_file/) |
| An A5X2 Manta reviewer on the official page: there "wasn't a lot of good introductory material on the primary features — headings, keywords, digests, layers" and "would have appreciated a video on each feature" (https://supernote.com/pages/what-upgrades-does-supernote-a5-x2-have) |

### Wants
| What people want changed |
|---|
| Publish the .note file specification (still open demand after 2021 promise) (https://www.reddit.com/r/Supernote/comments/1cyopn7/release_the_spec_of_the_note_file/) |
| Per-feature tutorial videos for headings, keywords, digests, layers (https://supernote.com/pages/what-upgrades-does-supernote-a5-x2-have) |
| Cheaper configurations / value for the price (https://www.ereadersforum.com/threads/great-but-too-expensive-supernote-a5x2-manta-review.3829/) |
| (Optional backlight debated) — community splits over the no-backlight philosophy (https://www.itpro.com/hardware/tablets/supernote-a5-x2-manta-review-a-premium-e-ink-tablet-thats-still-somewhat-spartan) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Hardware | Manta A5X2 review bundle (LAMY Safari Vista EMR + half folio) $607 / £497-equiv; device-only price not verified this pass — UNVERIFIED (https://www.itpro.com/hardware/tablets/supernote-a5-x2-manta-review-a-premium-e-ink-tablet-thats-still-somewhat-spartan) |
| Software | No subscription observed in any source this pass; tooling is free/open — UNVERIFIED as an exhaustive claim (https://supernote.com/pages/what-upgrades-does-supernote-a5-x2-have) |
| Platforms | Dedicated e-ink tablets (A5X2, A6X2, legacy A5X/A6X/A5/A6); community desktop converters (https://github.com/jya-dev/supernote-tool/blob/master/README.md) |
| Sync/cloud | Official cloud/Dropbox story not verifiable this pass — UNVERIFIED (https://ratta.helpjuice.com/?kb_language=en_US) |

### Video evidence
- Two substantive YouTube reviews are embedded in eReadersForum threads: the A5X2 review ("This is the Supernote A5X2, arguably the most uncompromising E-Ink note-taking tablet available today") at https://www.youtube.com/watch?v=GwrF5Ibevf8, and the Manta in-depth review ("It's a complete redesign... a lot of excellence... but at quite a price") at https://www.youtube.com/watch?v=oQBZKqL_23o (https://www.ereadersforum.com/threads/great-but-too-expensive-supernote-a5x2-manta-review.3829/, https://www.ereadersforum.com/threads/supernote-manta-a5x2-in-depth-review-of-the-10-7-300ppi-enote-tablet-truly-is-for-those-who-write.4266/).
- What footage is said to show (via review text surrounding the embeds; the videos themselves were not watchable in this pass — UNVERIFIED for in-frame specifics): real handwriting latency behavior, the lasso moving drawn elements fluidly, and the paper-like rendering (https://www.itpro.com/hardware/tablets/supernote-a5-x2-manta-review-a-premium-e-ink-tablet-thats-still-somewhat-spartan).
- Comment-thread gripes captured in prose around video embeds and official-page reviews: price, missing per-feature tutorial videos, no backlight in the dark (https://supernote.com/pages/what-upgrades-does-supernote-a5-x2-have, https://www.ereadersforum.com/threads/great-but-too-expensive-supernote-a5x2-manta-review.3829/).
- Official demo/tutorial channel and r/Supernote video threads: not surfaced by the searches run — UNVERIFIED.

### Contradictions
- Ratta promised to open the .note format "in April" (2021) once the data structure stabilized; by May 2024 the community was still formally petitioning for the spec and reverse-engineering bytes — the promise and the lock-in conflict, and the closed spec is what makes supernote-tool's whole reverse-engineering ecosystem necessary (https://www.reddit.com/r/Supernote/comments/kv7ccz/the_spec_for_the_note_file_format/ vs https://www.reddit.com/r/Supernote/comments/1cyopn7/release_the_spec_of_the_note_file/).
- Marketing emphasizes modularity/upgradability (A6X2 → A5X2) while reviews emphasize the flip side: premium price for a device that stays "somewhat spartan" in software and lacks a backlight (https://supernote.com/pages/what-upgrades-does-supernote-a5-x2-have vs https://www.itpro.com/hardware/tablets/supernote-a5-x2-manta-review-a-premium-e-ink-tablet-thats-still-somewhat-spartan).
- Cross-check vs thread-e (r12-enrich-e.md): no Supernote, e-ink, or handwriting-recognition claims exist in that file, so there is nothing recorded there to re-prove or contradict; all findings above are freshly evidenced this pass (checked locally, no URL).

Sources: https://www.itpro.com/hardware/tablets/supernote-a5-x2-manta-review-a-premium-e-ink-tablet-thats-still-somewhat-spartan ; https://supernote.com/pages/what-upgrades-does-supernote-a5-x2-have ; https://github.com/jya-dev/supernote-tool/blob/master/README.md ; https://www.reddit.com/r/Supernote/comments/kv7ccz/the_spec_for_the_note_file_format/ ; https://www.reddit.com/r/Supernote/comments/1cyopn7/release_the_spec_of_the_note_file/ ; https://github.com/qiaodenghui/Supernote ; https://ib.supernote.com/V2.6_EN.pdf ; https://ratta.helpjuice.com/?kb_language=en_US ; https://www.ereadersforum.com/threads/great-but-too-expensive-supernote-a5x2-manta-review.3829/ ; https://www.ereadersforum.com/threads/supernote-manta-a5x2-in-depth-review-of-the-10-7-300ppi-enote-tablet-truly-is-for-those-who-write.4266/ ; https://www.youtube.com/watch?v=GwrF5Ibevf8 ; https://www.youtube.com/watch?v=oQBZKqL_23o

LANE G COMPLETE — 15 apps covered
