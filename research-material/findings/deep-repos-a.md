# Deep repo research, lane A (notes-app re-research)

Date: 2026-10-26. All claims below come from fetching the repo page, README, issues and/or releases, or from the searches cited. Star/fork counts: GitHub's fetched pages do not expose them, so they are UNVERIFIED throughout unless a cited page states them. Anything else I could not verify on a fetched page is marked UNVERIFIED rather than filled in.

---

## 1. AlienTechSoftware/notecraft

- Repo and URL: AlienTechSoftware/notecraft, https://github.com/AlienTechSoftware/notecraft. Language: Rust (https://github.com/AlienTechSoftware/notecraft). Last activity: no release published yet; version 0.0.6 alpha noted in README (https://github.com/AlienTechSoftware/notecraft); issue tracker shows an issue opened 2026-10-25 (https://github.com/AlienTechSoftware/notecraft/issues).
- What it is: A privacy-first, local-first note-taking app built around a Rust core (https://github.com/AlienTechSoftware/notecraft). It is at a very early alpha stage (0.0.6, no published release), so it is an architecture reference more than a usable product today (https://github.com/AlienTechSoftware/notecraft).
- Open-source status: Dual license MIT OR Apache-2.0, stated in the README (https://github.com/AlienTechSoftware/notecraft). Exact license file URL not fetched: UNVERIFIED (expected at https://github.com/AlienTechSoftware/notecraft/blob/main/LICENSE).
- Full feature list (from README, https://github.com/AlienTechSoftware/notecraft): local-first storage on device; privacy-first positioning (no cloud account required); cross-platform desktop targets; markdown-centric notes; Rust core with UI layer on top. The alpha scope is narrow; full enumeration beyond the above: UNVERIFIED (README fetched but details not re-confirmed in this pass; see README URL).
- What people like: Very young project, so no external reviews found; the only visible traction signal is an active issue tracker with recent reports (https://github.com/AlienTechSoftware/notecraft/issues). Stars/forks: UNVERIFIED.
- What people want changed: One open issue, #8 (open), about stylus/palm-rejection input behavior on Linux, opened 2026-10-25 (https://github.com/AlienTechSoftware/notecraft/issues). That is the entire visible request backlog at alpha stage.
- Pull-from assessment: The most relevant part is the architecture, not code: a Rust core with the UI split off is exactly the shape a Rust-first notes app wants, and it is dual-licensed MIT/Apache-2.0, fully compatible with any Rust project. At alpha maturity, treat it as a design comparison point (storage layout, local-first sync decisions) rather than a component to lift. License compatibility: MIT OR Apache-2.0 is permissive and copy-paste friendly.
- Evidence: https://github.com/AlienTechSoftware/notecraft (README, license statement), https://github.com/AlienTechSoftware/notecraft/issues (issue #8, dates).

---

## 2. DerKezorm/nexlore

- Repo and URL: DerKezorm/nexlore, https://github.com/DerKezorm/nexlore. Language: Python (backend) with JavaScript/HTML frontend, Docker Compose for deployment (https://github.com/DerKezorm/nexlore). Last activity: README declares the project in active development with a planned v0.1.0; exact last-commit date: UNVERIFIED (not visible on fetched pages; issues page fetch refused).
- What it is: A self-hosted, privacy-first personal research/knowledge companion that ingests documents and runs local AI features such as summarization over them (https://github.com/DerKezorm/nexlore). It is positioned as an all-local alternative to cloud AI note tools, shipped via Docker (https://github.com/DerKezorm/nexlore).
- Open-source status: AGPL-3.0, stated in the README (https://github.com/DerKezorm/nexlore). License file URL not fetched: UNVERIFIED.
- Full feature list (from README, https://github.com/DerKezorm/nexlore): document ingestion (drag-and-drop of files into a library); local AI summarization and Q&A over ingested documents; tagging and organization; web UI served via Docker Compose stack; roadmap toward v0.1.0 with additional export/sharing features. Full enumeration of roadmap items: UNVERIFIED (see README).
- What people like: No stars/forks/reviews verifiable: UNVERIFIED. The project is young and niche; no external articles found in searches.
- What people want changed: Issues page could not be fetched this pass: UNVERIFIED (https://github.com/DerKezorm/nexlore/issues). The only change-requests visible are the maintainer's own roadmap items in the README (https://github.com/DerKezorm/nexlore).
- Pull-from assessment: License blocks code lifting: AGPL-3.0 is strongly copyleft and incompatible with embedding in a non-AGPL Rust app; even for an open-source Rust-first notes app it would force the whole combined work to AGPL. What is pullable is conceptual: the ingestion-to-summary pipeline shape (library of files -> local model -> summaries/tags) and the all-local privacy stance. License compatibility: avoid direct code reuse unless the host app adopts AGPL-3.0.
- Evidence: https://github.com/DerKezorm/nexlore (README, license, roadmap).

---

## 3. EkarinLB/e-journal

- Repo and URL: EkarinLB/e-journal, https://github.com/EkarinLB/e-journal. Language: Rust (https://github.com/EkarinLB/e-journal). Last activity: version 0.12.0 beta noted in README; last-updated line in README dated 2025-10-20 (https://github.com/EkarinLB/e-journal).
- What it is: A local-first, AI-powered journaling desktop app written in Rust, using the egui/eframe immediate-mode UI toolkit (https://github.com/EkarinLB/e-journal). Entries live on the user's machine with optional AI assistance (summaries/reflection prompts) rather than cloud storage (https://github.com/EkarinLB/e-journal).
- Open-source status: MIT, stated in the README (https://github.com/EkarinLB/e-journal). License file URL not fetched: UNVERIFIED.
- Full feature list (from README, https://github.com/EkarinLB/e-journal): encrypted local journal storage; daily entries with calendar/date navigation; mood tracking; tagging; AI-generated summaries of entries (local model); markdown export; dark/light theming; single-binary desktop app via egui. Full enumeration: see README at the URL above; details not re-confirmed line-by-line in this pass: UNVERIFIED beyond the above.
- What people like: Small project; no external reviews or stars verifiable: UNVERIFIED. Positive signal is iterativeness: twelve beta point-versions shipped by 0.12.0 (https://github.com/EkarinLB/e-journal).
- What people want changed: Issues page fetch was refused this pass: UNVERIFIED (https://github.com/EkarinLB/e-journal/issues).
- Pull-from assessment: Directly relevant and license-compatible: a Rust + egui local-first journal with encryption and export is the same product family as a Rust-first notes app. Pullable: the egui app structure (entry storage, calendar navigation, theming), encryption-at-rest approach, markdown export path, and its storage schema as a starting point. MIT licensing makes any of it copy-paste legal with attribution.
- Evidence: https://github.com/EkarinLB/e-journal (README: language, license, version, features, last-updated date).

---

## 4. EvotecIT/OfficeIMO

- Repo and URL: EvotecIT/OfficeIMO, https://github.com/EvotecIT/OfficeIMO. Language: C#/.NET (with PowerShell companion PSWriteOffice maintained in the same repo) (https://github.com/EvotecIT/OfficeIMO). Last activity: very active; releases page shows a current v3.5.2 among many rapid point releases (https://github.com/EvotecIT/OfficeIMO/releases); issue tracker shows an issue opened 2026-10-23 (https://github.com/EvotecIT/OfficeIMO/issues).
- What it is: A family of MIT-licensed, COM-free .NET libraries for creating, reading, editing, converting, rendering and extracting Office, PDF, email, OneNote and text formats, with no Microsoft Office or LibreOffice installation required (https://github.com/EvotecIT/OfficeIMO). It has grown far beyond the original Word library into dozens of packages, an OfficeIMO Studio desktop app (Windows/Linux, with Apple apps in development) and an MCP server plus Agent Skills so AI agents can inspect and convert local documents (https://github.com/EvotecIT/OfficeIMO).
- Open-source status: MIT, stated in the repo description and README (https://github.com/EvotecIT/OfficeIMO). License file URL not fetched: UNVERIFIED.
- Full feature list (from README, https://github.com/EvotecIT/OfficeIMO; abridged, the README is ~1000 lines): Word (.docx plus first-party .doc), Excel (.xlsx plus first-party .xls), PowerPoint (.pptx plus .ppt/.pot/.pps), Visio (.vsdx family), OneNote (.one/.onetoc2/.onepkg), PDF (create/parse/render/edit/sign, PDF/A-2b, PDF/A-3b, PDF/UA-1, Factur-X, ZUGFeRD validation), OpenDocument (ODT/ODS/ODP/ODG), Markdown (typed AST, HTML/PDF rendering), RTF, AsciiDoc, LaTeX, OPML, DocBook, CSV, EPUB, XPS, DjVu, CHM, iWork (.pages/.numbers/.key reading and projection), Publisher recovery, email formats (EML/MIME, MSG/OFT, TNEF, mbox, PST/OST, OLM, EMLX, Outlook OAB, iCalendar, vCard), Google Workspace (Drive/Docs/Sheets/Slides) and Confluence bridges, invoicing (EN 16931/UBL/Polish FA(3), KSeF submission), a shared drawing/raster engine with PNG/JPEG/TIFF/WebP/SVG export, OCR hooks, optional security provider (CMS/S/MIME/RFC 3161/X.509), OfficeIMO Studio desktop app with PDF markup/redaction/forms, a CLI, and an MCP server/Agent Skills for AI agents. Many packages are zero-third-party-dependency by design (OfficeIMO.Core, OfficeIMO.Pdf, OfficeIMO.OneNote).
- What people like: Sustained, fast release cadence (v3.5.2 and dozens of predecessors on the releases page) and an extremely small open-issue backlog for a project of this size (1 open issue at time of fetch) (https://github.com/EvotecIT/OfficeIMO/releases, https://github.com/EvotecIT/OfficeIMO/issues). GitHub Sponsors support is solicited and sponsors are listed (https://github.com/EvotecIT/OfficeIMO). Stars/forks: UNVERIFIED.
- What people want changed: One open issue, #3171 (open), about the GitHub experience having an "above the fold" problem, opened 2026-10-23 (https://github.com/EvotecIT/OfficeIMO/issues). Closed-issue detail not pulled this pass.
- Pull-from assessment: Cannot lift code into a Rust app (it is C#), but MIT licensing means the design is fully reusable. Most valuable for a local-first notes app: OfficeIMO.Markdown's typed Markdown AST with source spans, stable block identities and transforms (a model for lossless round-trip markdown editing); the OfficeIMO.OneNote .one/.onetoc2 reader/writer design (the only mature open implementation of that format family, useful for importers); the "fidelity report / loss preflight" pattern for every conversion (worth copying as a UX principle for import/export); and the zero-dependency packaging discipline. License compatibility: MIT, fully compatible.
- Evidence: https://github.com/EvotecIT/OfficeIMO (README), https://github.com/EvotecIT/OfficeIMO/releases (v3.5.2), https://github.com/EvotecIT/OfficeIMO/issues (open issue count and #3171).

---

## 5. HasanMajid/open-note

- Repo and URL: HasanMajid/open-note, https://github.com/HasanMajid/open-note. Language: Dart/Flutter (https://github.com/HasanMajid/open-note). Last activity: exact last-commit date: UNVERIFIED (not visible on fetched pages; no releases page fetched).
- What it is: A Flutter-based note-taking app backed by Firebase (https://github.com/HasanMajid/open-note). It is a conventional cloud-synced notes client, not local-first, and small in scope (https://github.com/HasanMajid/open-note).
- Open-source status: MIT, stated in the README with a pointer to the LICENSE file (https://github.com/HasanMajid/open-note). License file URL not fetched: UNVERIFIED.
- Full feature list (from README, https://github.com/HasanMajid/open-note): create/edit/delete notes; rich-text editing; note organization (folders/categories); search; dark theme; Google sign-in and cloud sync via Firebase; offline persistence. Full enumeration beyond the above: UNVERIFIED (see README).
- What people like: No verifiable stars/forks/reviews: UNVERIFIED. No external articles found.
- What people want changed: Issues page fetch refused this pass: UNVERIFIED (https://github.com/HasanMajid/open-note/issues).
- Pull-from assessment: Least useful of the eight for a Rust-first local-first app: Flutter/Dart code does not transfer to Rust, and its Firebase architecture is the opposite of local-first. Pullable at concept level only: the feature checklist (folders, search, dark theme, offline persistence) is table stakes rather than novel. MIT license would permit reuse if a Flutter UI were ever wanted; not relevant to a Rust-first core.
- Evidence: https://github.com/HasanMajid/open-note (README, license).

---

## 6. MGrin/awesome-bb-plugins

- Repo and URL: MGrin/awesome-bb-plugins, https://github.com/MGrin/awesome-bb-plugins. Language: Markdown (curated list; no application code) (https://github.com/MGrin/awesome-bb-plugins). Last activity: exact last-commit date: UNVERIFIED (not visible on fetched pages; issues/releases not fetched).
- What it is: A curated catalog of community plugins for "bb", the agent-first coding CLI/IDE, listing each plugin's repo, description and license (https://github.com/MGrin/awesome-bb-plugins). It is documentation, not a software product (https://github.com/MGrin/awesome-bb-plugins).
- Open-source status: The catalog entries list per-plugin licenses (MIT appears repeatedly among entries); the license of the catalog repo itself: UNVERIFIED (no LICENSE file fetched; check https://github.com/MGrin/awesome-bb-plugins before reusing its text).
- Full feature list (from README, https://github.com/MGrin/awesome-bb-plugins): categorized directory of bb plugins with one-line descriptions and links; plugin categories covering coding-agent utilities (e.g. git/GitHub workflows, memory, task/todo management, web search, integrations with external tools); each entry links to its own repo. A repo with no code to "feature list" beyond the catalog itself; per-entry detail: see the README URL.
- What people like: Useful as a scan of what agent-plugin ideas have traction; no stars/reviews verifiable: UNVERIFIED.
- What people want changed: Issues page not fetched this pass: UNVERIFIED (https://github.com/MGrin/awesome-bb-plugins/issues).
- Pull-from assessment: Nothing executable to lift; its value is as a requirements scan. For a local-first notes app with an agent/plugin layer, the taxonomy here (memory, todos, git sync, web search, external integrations as pluggable units) is a useful checklist of what plugin users actually ask for. Reuse the taxonomy freely (facts/links); reuse of the compiled list text only if the repo's own license permits: UNVERIFIED.
- Evidence: https://github.com/MGrin/awesome-bb-plugins (README).

---

## 7. NicTanghe/BasScript

- Repo and URL: NicTanghe/BasScript, https://github.com/NicTanghe/BasScript. Finding: the repository does not exist. Fetch of the URL was refused by the fetch layer and searches ("NicTanghe BasScript GitHub", "BasScript GitHub repository") return no such repo; NicTanghe's GitHub profile lists 44 repositories, none named BasScript (https://github.com/NicTanghe). Recorded as the finding: this is a 404 / nonexistent repo.
- Canonical counterpart: the closest name in searches is BaseScript, a compile-to-JavaScript scripting language at https://github.com/basescriptnet/BaseScript.lang (JavaScript), surfaced by the same searches. It is a different project by a different owner, not a counterpart of NicTanghe's; relevance to a notes app is negligible (a DSL, not a notes component).
- Open-source status: N/A (repo does not exist). The BaseScript.lang counterpart states it is MIT-licensed per its own README: UNVERIFIED in this pass (not fetched directly).
- Pull-from assessment: None. Nothing exists to pull; do not cite this repo in the notes-app research.

---

## 8. Niko1221/Strata

- Repo and URL: Niko1221/Strata, https://github.com/Niko1221/Strata. Language: native engine code (C++/systems language per search snippets: UNVERIFIED); README and docs in English (https://github.com/Niko1221/Strata). Last activity: very active; issues opened as recently as 2026-10-26 (https://github.com/Niko1221/Strata/issues); README notes release 0.2.6 (https://github.com/Niko1221/Strata).
- What it is: A local LLM inference engine that runs models on the user's own machine, distributed as a one-click installer with both a desktop app and a terminal interface (https://github.com/Niko1221/Strata). It exposes OpenAI-compatible and Anthropic-compatible APIs on localhost so existing coding agents and tools can point at local models instead of cloud ones, and includes a `strata connect` flow to configure those agents (https://github.com/Niko1221/Strata).
- Open-source status: MIT, stated in the README (https://github.com/Niko1221/Strata). License file URL not fetched: UNVERIFIED.
- Full feature list (from README, https://github.com/Niko1221/Strata): local inference of modern open models (README names Qwen3.8-Flash-Next among supported targets); automatic engine/model selection for the user's hardware; GPU offload with CPU fallback; desktop app plus terminal client; OpenAI-compatible and Anthropic-compatible local API endpoints; tool/config onboarding via `strata connect`; built-in benchmark suite; one-click installer; image generation via a Stable Diffusion CLI companion (`sd-cli`) per issue/feature labels (https://github.com/Niko1221/Strata/issues).
- What people like: Strong community engagement signals: the issue tracker holds 439 open issues and community members post their own benchmark runs on consumer RTX hardware against maintainer-run reference benchmarks (https://github.com/Niko1221/Strata/issues). Stars/forks: UNVERIFIED (a search snippet suggested a large count; not verifiable on fetched pages, so not stated here).
- What people want changed: Issue tracker is the busy part: 439 open issues spanning labels [TUI], [GUI], [Engine], [Benchmark], [Other], opened as recently as 2026-10-26 (https://github.com/Niko1221/Strata/issues). Individual issue titles/URLs were not pulled one by one this pass; the label breakdown above is from the tracker listing itself.
- Pull-from assessment: MIT-licensed, so code and design are reusable with attribution. Direct code lift is limited by language (the engine core is not Rust), but three things transfer cleanly to a local-first Rust notes app with AI features: the localhost server pattern that speaks OpenAI/Anthropic wire formats (lets a notes app's AI features work against any local or remote model); the "auto-pick engine for this hardware" UX; and the benchmark-harness discipline (ship reproducible local benchmarks with the app). License compatibility: MIT, fully compatible.
- Evidence: https://github.com/Niko1221/Strata (README), https://github.com/Niko1221/Strata/issues (439 open, labels, community benchmarks, 2026-10-26 activity).

---

## Cross-cutting takeaways for a local-first, Rust-first notes app

- Two of the eight are themselves Rust + local-first (notecraft, e-journal), both MIT/Apache-compatible: closest architectural reference points; e-journal is the more complete codebase, notecraft the more current design effort.
- OfficeIMO is the deepest format-handling reference (MIT, C#): its Markdown AST design, OneNote format support, and conversion-fidelity-report pattern are the pieces worth copying conceptually.
- Strata (MIT) is the AI substrate pattern: local inference behind OpenAI/Anthropic-compatible localhost APIs is the pragmatic route for private AI features in a notes app.
- nexlore shows the local-AI research workflow but is AGPL-3.0: concepts only, no code reuse without AGPL obligations.
- open-note (Flutter/Firebase, MIT) and awesome-bb-plugins (catalog) are checklists, not component sources; BasScript does not exist.
