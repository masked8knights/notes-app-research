# IdeaCraft (aamirenic/IdeaCraft) — Research Findings

Researched: 2026-10-26, via web search and direct fetches of the GitHub repo, its release page, its issue tracker, and related repos/sites.

## 1. What IdeaCraft is

IdeaCraft is a free, open-source, local-first desktop workspace app for notetaking, knowledge management, data organization, and project and task tracking, described by its repo title as "a 7mb desktop app, completely reimagined in Rust" (https://github.com/aamirenic/IdeaCraft). The README positions it as a fast, offline-friendly desktop app for Windows, with the same source tree compiling on Linux and macOS via build-from-source (https://github.com/aamirenic/IdeaCraft). Target users are people who want notes/docs/projects/knowledge kept locally: the repo's tagline stresses that pages live in a local SQLite database and "your words never leave your machine unless you turn on sync" (https://github.com/aamirenic/IdeaCraft).

Platforms: Windows 10 (1809+) and Windows 11 get prebuilt installers; Linux and macOS builds work from source but have no prebuilt installers or auto-update feed yet (https://github.com/aamirenic/IdeaCraft).

Tech stack: a Tauri 2 app — a compact Rust binary wrapping a plain HTML/CSS/JS frontend in `ui/` (embedded at build time, no separate frontend build step), rendered through the system webview (WebView2 on Windows, WebKitGTK/WebKit on Linux/macOS), with SQLite via bundled rusqlite for storage (https://github.com/aamirenic/IdeaCraft). The Rust core is organized as `src-tauri/src/commands.rs` (all Tauri IPC commands: pages, blocks, search, sync, AI, updater) and `src-tauri/src/db.rs` (SQLite schema + seed logic) (https://github.com/aamirenic/IdeaCraft). Build prerequisites are Rust 1.80+ and Node.js 18+; data lives in `%APPDATA%\com.ideacraft.app.desktop` as `ideacraft.db` plus attachments (https://github.com/aamirenic/IdeaCraft). The repo title and "completely reimagined in Rust" wording suggest a Rust rewrite of an earlier app, though no predecessor is named in the materials found (https://github.com/aamirenic/IdeaCraft).

The repo includes an npm distribution path: `npm install -g ideacraft` runs a postinstall step that downloads the latest signed installer from GitHub Releases and installs silently per-user, and the `ideacraft` launcher command supports `install`, `uninstall` and `where` subcommands (https://github.com/aamirenic/IdeaCraft).

## 2. Full feature list

From the README feature list (https://github.com/aamirenic/IdeaCraft) and the v1.0.0 release notes (https://github.com/aamirenic/IdeaCraft/releases/tag/v1.0.0):

- ~7 MB install, starts in under a second, no background services (https://github.com/aamirenic/IdeaCraft)
- Block editor with Markdown shortcuts — headings, lists, to-dos, quotes, code, dividers (https://github.com/aamirenic/IdeaCraft; https://github.com/aamirenic/IdeaCraft/releases/tag/v1.0.0)
- Favorites, trash, page history, page icons and covers (https://github.com/aamirenic/IdeaCraft)
- Search (including a Ctrl K search palette), full-text search, templates, comments (https://github.com/aamirenic/IdeaCraft; https://github.com/aamirenic/IdeaCraft/releases/tag/v1.0.0)
- Data export/backup, and device-to-device sync via a sync folder (https://github.com/aamirenic/IdeaCraft)
- Optional AI assistant via a local Ollama endpoint, off by default (https://github.com/aamirenic/IdeaCraft)
- Dark/light/follow-system themes (https://github.com/aamirenic/IdeaCraft)
- Auto-updates: a Rust-side updater plugin checks a `latest.json` release feed, downloads the signed installer on confirm from Settings → About → Check for updates, and restarts the app; artifacts are minisign-signed (https://github.com/aamirenic/IdeaCraft)
- A smoke-test harness (`npm run smoke`) drives the real app over the WebView2 DevTools protocol, verifying boot, seeded content, page creation, typing, trash + delete-forever, and uncaught JS errors (https://github.com/aamirenic/IdeaCraft)

Screenshots are referenced on the README (editor in both themes plus the Ctrl K palette) but the fetched text does not include the images themselves (https://github.com/aamirenic/IdeaCraft).

Notably absent (based on everything fetched): no handwriting/stylus support, no mobile platform, no end-to-end-encrypted cloud sync (sync is a local folder mechanism), and no mention of drawing/canvas features (https://github.com/aamirenic/IdeaCraft).

## 3. Repo facts

- The repo exists and is public: https://github.com/aamirenic/IdeaCraft (https://github.com/aamirenic/IdeaCraft)
- License: MIT (https://github.com/aamirenic/IdeaCraft)
- Languages: Rust core plus a plain JavaScript/HTML/CSS frontend; Node.js tooling for the npm package and smoke tests (https://github.com/aamirenic/IdeaCraft)
- Stars/forks: exact counts were not visible in any fetched page or search result; a fork exists at https://github.com/Velcent/IdeaCraft carrying the identical description (https://github.com/Velcent/IdeaCraft)
- Releases: one release found, v1.0.0 ("first release"), published by aamirenic on 23 Oct 2026 (00:48 UTC), tagged 86e1e92, with 4 commits to main since the release as of the search date (2026-10-26) (https://github.com/aamirenic/IdeaCraft/releases/tag/v1.0.0)
- Release assets: `IdeaCraft_1.0.0_x64-setup.exe` (NSIS installer, per-user) and `latest.json` for the auto-updater (https://github.com/aamirenic/IdeaCraft/releases/tag/v1.0.0)
- Release cadence is very young: this is the project's first release, days old at research time (https://github.com/aamirenic/IdeaCraft/releases/tag/v1.0.0)
- Maintainer activity: aamirenic is active on GitHub, e.g. four pull requests to AnkarIIT/OpenJarvis (README fixes, textual version fix, Piper voice download redirect fix, Windows VC++ prerequisites note) (https://github.com/AnkarIIT/OpenJarvis/pull/1; https://github.com/AnkarIIT/OpenJarvis/pull/2; https://github.com/AnkarIIT/OpenJarvis/pull/3; https://github.com/AnkarIIT/OpenJarvis/pull/4); aamirenic also has an OpenJarvis repo at https://github.com/aamirenic/OpenJarvis
- Distribution/deployment state: prebuilt installers ship for Windows only; the app is not code-signed with a paid certificate (SmartScreen warning on first manual launch; the updater verifies via minisign instead); Linux/macOS bundler tooling is explicitly requested as PRs (https://github.com/aamirenic/IdeaCraft)

## 4. Open-source status and pull-from assessment

IdeaCraft is fully open source under the MIT license (https://github.com/aamirenic/IdeaCraft). MIT is highly permissive, so for a separate Rust notes app it permits copying, modifying and redistributing code with attribution — no copyleft obligations (https://github.com/aamirenic/IdeaCraft).

Which pieces look pullable, given the architecture (https://github.com/aamirenic/IdeaCraft):

- The SQLite data layer (`src-tauri/src/db.rs`: schema + seed logic) — a small, self-contained rusqlite schema for pages/blocks/favorites/trash/history that could be adapted directly into a Rust app's storage layer.
- The Tauri IPC command surface (`src-tauri/src/commands.rs`: pages, blocks, search, sync, AI, updater) — reusable as a reference for command design if the Rust notes app also uses Tauri; less directly reusable if it uses another framework, since the commands are Tauri-shaped.
- The sync-folder mechanism (device-to-device sync via a folder) — a simple design worth studying, though the code's coupling to Tauri commands limits direct reuse.
- The whole app is itself Tauri 2 + Rust, so if the planned Rust notes app uses Tauri, this is essentially a working template for: block editor backend, SQLite persistence, search, templates, export/backup, auto-update feed, and NSIS/DEB/AppImage/DMG packaging.
- Less pullable: the frontend is plain HTML/CSS/JS rendered in a webview; it is MIT too, but it is not a Rust component, so a "Rust notes app" would likely reuse ideas rather than code there. Also note the "no Electron" purist stance attributed to the ArtCraft family (see section 6) conflicts with using a webview at all (https://getartcraft.com/apps).

Caveat for reuse: the project is days old (v1.0.0 on 2026-10-23), so the codebase is young and lightly reviewed; issue #1 already flags a dependency advisory (see below), and there is a RustSec-relevant Tokio pin to check before building on it (https://github.com/aamirenic/IdeaCraft/issues/1).

## 5. Known issues, complaints, feature requests

The issue tracker is nearly empty, consistent with the project's age. Findings:

- Issue #1, "A dependency has a published memory-safety issue" (opened ~4 days before 2026-10-26, i.e. around 2026-10-22): the reporter, after a GPT-based code inspection, states the Rust lockfile pins Tokio 1.54.0, affected by a race/use-after-free advisory fixed in 1.54.1; the reporter did not establish whether IdeaCraft reaches the affected timer functionality, notes other dependency advisories of platform-specific and maintenance character, and says the JavaScript build-tool lockfile passed npm audit. No assignees, labels, projects or milestones; no linked branches or PRs (https://github.com/aamirenic/IdeaCraft/issues/1)
- No other issues, and no feature requests from users, were found in search (https://github.com/aamirenic/IdeaCraft/issues/1 was the only issue surfaced across searches)
- Self-declared known limitations from the README: Windows-only prebuilt installers; no paid code-signing certificate; the update feed reports a connection error until the first real GitHub release publishes `latest.json`; window focus/restore from minimized state via tray is not guaranteed on all Windows configurations (https://github.com/aamirenic/IdeaCraft)

## 6. Relation to ArtCraft apps (PhotoCraft, PDFCraft)

No relation found between aamirenic/IdeaCraft and the ArtCraft app family. The ArtCraft "Crafting Apps" lineup at getartcraft.com lists thirteen pure-Rust apps — PhotoCraft (image editor), VectorCraft, FilmCraft, LightCraft, PdfCraft (PDF workbench), EffectCraft, DesignCraft, FigCraft, WordCraft, SoundCraft, DeckCraft, CADCraft, GridCraft — published by the storytold GitHub org, and IdeaCraft is not among them (https://getartcraft.com/apps; https://github.com/storytold/pdfcraft; https://github.com/storytold/photocraft). aamirenic/IdeaCraft also differs technically from the ArtCraft principles: ArtCraft's rules say "Pure Rust compiled to real desktop apps... No Electron, no web views", while IdeaCraft is a Tauri webview app (https://getartcraft.com/apps; https://github.com/aamirenic/IdeaCraft).

However, a second, unrelated repo also named "ideacraft" does claim kinship with the craft family: rickyb82/ideacraft is a Rust-native concept-map/mind-map canvas (v0.1 early preview, dual MIT/Apache-2.0) that describes itself as belonging "to the craft family of open creative tools (GridCraft, PdfCraft, …)", with draw.io interchange, an MCP server for AI agents, a headless CLI, and a web/WASM build; rickyb82/mailcraft likewise names "(gridcraft, ideacraft, pdfcraft…)" as its craft family (https://github.com/rickyb82/ideacraft; https://github.com/rickyb82/mailcraft). This rickyb82 project is not on the official getartcraft.com lineup (https://getartcraft.com/apps), so it appears to be a community/sibling project adopting the "craft" conventions rather than an official ArtCraft app. For the notes-app research, it is worth distinguishing the two namesakes: the Discord reference is almost certainly aamirenic/IdeaCraft (a notes app), not rickyb82/ideacraft (a mind-mapping canvas) (https://github.com/aamirenic/IdeaCraft; https://github.com/rickyb82/ideacraft).

Useful to this research regardless: ArtCraft's stated principles (open source, permissive licenses, native Rust, familiar shortcuts, fully local files, agent-ready CLI/JSON/MCP, WebAssembly builds) are a documented signal of what this Rust-native community values in creative/notes tooling (https://getartcraft.com/apps), and ArtCraft's own notes-adjacent entries are WordCraft (word processing) and GridCraft (spreadsheets), with IdeaCraft absent (https://getartcraft.com/apps).

## Summary of confidence

Everything above about aamirenic/IdeaCraft comes from the repo's own README, its v1.0.0 release notes, its single issue, and search-result metadata fetched on 2026-10-26; star/fork counts and commit-level activity beyond the release tag were not visible in any fetched page. The ArtCraft non-relation conclusion rests on the full official app lineup (thirteen apps, no IdeaCraft) plus the architecture mismatch (webview vs "no web views"). The namesake-disambiguation finding (rickyb82/ideacraft) is solid and directly relevant to avoiding confusion in later research rounds.
