# R12 round 2 lane 9: gap hunt

Method note: 208 unique names were extracted from the first column of APPS-LINKS.md (compound cells split into components) and each was grep'd (case-insensitive, fixed-string) against all 34 findings files under research-material/findings/. An entry is a gap when its best match count across the full cell, its base name, and its components is 0-2. Sixteen of the 40 low-coverage rows are meta-rows (file formats such as Evernote HTML/XML ENEX, Pandoc grid tables, .ink.md sidecars, X posts by pwnies and sheherenow_, a YouTube video ID, arXiv papers, Notesnook monograph example, Ratta Supernote docs, AGENTS files, Nostr NIPs, the Obsidian-plugins list row, malleable-software essay, batch labels); those are excluded below. Several of the R5/R7-addition rows have since been enriched in their Key-facts cells by earlier R12 lanes, but per the lane brief the test here is the findings corpus, so they are still listed.

## Coverage gaps
- aamirenic/IdeaCraft | matches: 0 | Tauri/Rust local-first desktop workspace notes app, added via R5-user-link; detail exists in its Key-facts cell but nothing in the findings corpus backs it
- rickyb82/ideacraft | matches: 0 | separate GitHub repo carrying the same IdeaCraft description; relationship to aamirenic's repo UNVERIFIED
- MyScript interactive-ink-examples-ios | matches: 0 | Apple iOS example apps for the MyScript interactive ink SDK (R7 additions)
- University Notes: Study Notes (2026) | matches: 1 | app-store study/PDF notes app with annotation and note templates (R5 additions)
- MarlenaMakosza/LiveQuill issue 4 | matches: 1 | GitHub issue in LiveQuill, a handwriting notes project (R7 additions)
- Drawboard Projects (formerly Bullclip) | matches: 1 | rebranded Bullclip, project review/annotation app (R5 additions; an R12 lane note exists in its cell)
- Hypothesis | matches: 1 | Hypothes.is web-annotation tool (R5 additions); the single corpus match is the word "hypothesis" in prose, so real coverage is effectively 0
- Write by Styluslabs | matches: 1 | Android-first handwriting notes app, free, adds vector ink (R5 additions; R12 note in cell)
- everyai-com/snapbench | matches: 1 | mobile OCR benchmarking project (R7 additions; not a note app)
- google_mlkit_digital_ink_recognition | matches: 1 | Flutter package wrapping ML Kit digital-ink recognition (R7 additions; a component, not an app)
- mkyt/ocrmypdf-AppleOCR | matches: 1 | ocrmypdf plugin adding macOS Vision OCR (R7 additions; a tool, not an app)
- notecraft-core-studio.base44.app | matches: 1 | Base44-built web notes builder app (R7 additions)
- supernote-annotations | matches: 1 | Obsidian plugin ingesting Supernote annotations (R7 additions; out of R13 notetaking-app scope)
- Gemma3-1B-IT (litert-community) | matches: 2 | on-device Gemma model variant used in app evidence (R7 additions; a model, not an app)
- swiftsaneai (sanenotes) issues 295 and 819 | matches: 2 | Swift notes app repository referenced only as evidence source (R7 additions)
- jdkruzr/ultrabridge | matches: 2 | self-hosted bridge adding search/HTR/AI to e-ink tablets (R7 additions; researched below)
- David-Magdy/TR_OCR_LARGE | matches: 2 | handwriting/OCR training project (R7 additions; not a note app)
- Gemma 3n E4B-it | matches: 2 | on-device Gemma model variant (R7 additions; a model, not an app)
- Gemma3-1B-IT | matches: 2 | on-device Gemma model variant (R7 additions; a model, not an app)
- Homebrewery | matches: 2 | GitHub repo for a D&D 5e notes/monsters tool (R5-user-link; R12 note in cell)
- MarginNote 4 | matches: 2 | study/annotation app combining mind-map, flashcards and PDF notes (R5 additions; R12 note in cell)
- ScriptCraft | matches: 2 | Evernote-remake project with no repository found (R7 additions)
- Zotero | matches: 2 | reference manager treated as a notes-adjacent competitor (R5 additions; R12 note in cell)
- sync-embeds | matches: 2 | Obsidian plugin for syncing embedded content (R7 additions; out of R13 notetaking-app scope)
- Apps mentioned in the findings corpus as alternatives/competitors but absent from APPS-LINKS entirely: Bear | matches: 23 | NOT IN APPS-LINKS; the single biggest unnamed competitor in the corpus, named in switching guides and alternatives lists
- Apple Notes | matches: 15 | NOT IN APPS-LINKS; the default app every competitor is compared against
- Boostnote | matches: 12 | NOT IN APPS-LINKS (one passing cell mention); open-source developer notes app whose rewrite was archived
- Notable | matches: 9 | NOT IN APPS-LINKS; nearly all matches are the word "notable", so the app itself has 0 real coverage
- Roam Research | matches: 7 | NOT IN APPS-LINKS; outliner/PKM competitor named in linked-apps and sentiment files
- Capacities | matches: 6 | NOT IN APPS-LINKS; object-based notes app named as an alternative
- Dynalist | matches: 3 | NOT IN APPS-LINKS; outliner by the Obsidian team, in maintenance mode
- JabRef | matches: 2 | NOT IN APPS-LINKS; open-source reference manager named beside Zotero in linked-apps-1.md
- Google Keep | matches: 2 | NOT IN APPS-LINKS; mainstream quick-capture competitor
- Agenda | matches: 0 real (2 word matches for "agenda") | NOT IN APPS-LINKS; calendar-driven notes app

## Feature-area gaps
- Accessibility | no dedicated findings anywhere; corpus has only 7 passing mentions across 5 files, no screen-reader-per-app data, and a single WCAG claim that belongs to a TTS utility, not a notes app
- Search quality (user-facing) | no dedicated findings; index internals are covered (thread-d-indexing, thread-f-editor-platform) but ranking quality, fuzzy matching and OCR-search accuracy are never measured
- Data ownership | no dedicated findings; a single corpus line (r7-user-sentiment-sweep.md, "data ownership/server fear is the most-cited reason") plus partial overlap with thread-g-trust-ux
- Pricing transparency | no dedicated findings; prices appear scattered in per-app rows and digests but no file audits pricing practices, hidden fees, or free-tier degradation

## Researched gaps

### Bear
- What it is: Markdown-style note app built around nested tags rather than folders, with themes and attachable files (https://bear.app; https://bearnotes.org/)
- Platforms: macOS (10.15+, Apple Silicon), iOS and iPadOS only; no Windows, Android or web app (https://bearnotes.org/; https://apps.apple.com/us/app/bear-private-flexible-notes/id1091189122)
- Pricing: free; Bear Pro $2.99/month or $29.99/year with 7-day free trial, sync and themes gated behind Pro (https://www.toolguide.io/reviews/bear; https://aehq0jvh41gy9rp96jajgg-on.drv.tw/OneNote/Bear.html)
- Distinctive features: nested-tag hierarchy that mimics folder structure without folders, PDF/image OCR search in Pro, iCloud sync (https://www.toolguide.io/reviews/bear)
- Gripes: no Windows/Android/web versions, so it strands users in Apple's ecosystem (https://www.toolguide.io/reviews/bear); reviewers call it paying for functionality that is standard elsewhere, and sync behind the paywall draws repeated criticism (https://www.toolguide.io/reviews/bear; https://bundl.run/blog/bear-app-download-mac)

### Apple Notes
- What it is: Apple's free system notes app, the comparison baseline every competitor names (findings corpus, apps-likes-wants.md and r6-additions rows)
- Platforms: iPhone, iPad, Mac, Apple Watch plus iCloud web on any browser (https://toolfinder.co/compare/things-vs-apple-notes)
- Pricing: free, bundled with Apple hardware; no subscription (https://daringfireball.net/linked/2026/09/16/marks-ios-26-apple-notes-import-markdown)
- Distinctive features: deep system integration (Apple Pencil, locked notes, collaboration), and Apple-Intelligence features such as Math Notes and Image Wand that competitors lack (https://paperlike.com/blogs/illustration/why-i-abandoned-apple-notes-as-a-digital-note-taker)
- Distinctive feature: Markdown import/export arrived in iOS 26/macOS Tahoe 26, closing its biggest interop gap (https://daringfireball.net/linked/2026/09/16/marks-ios-26-apple-notes-import-markdown)
- Gripes: no way to type Markdown before iOS 26 and still no plain-text workflows (https://paperlike.com/blogs/illustration/why-i-abandoned-apple-notes-as-a-digital-note-taker); export remains one note at a time with blurry handwriting PDFs and no native Windows/Android access (https://paperlike.com/blogs/illustration/why-i-abandoned-apple-notes-as-a-digital-note-taker); sync failures that erase recent notes push users to dedicated apps (https://paperlike.com/blogs/illustration/why-i-abandoned-apple-notes-as-a-digital-note-taker); missing search filters, templates and version history for note-taking veterans (https://smallcubes.ai/articles/the-ultimate-notes-app-for-veterans-from-apple-notes)
- Gripe: organization degrades past a few hundred notes, users report (https://paperlike.com/blogs/illustration/why-i-abandoned-apple-notes-as-a-digital-note-taker)

### Capacities
- What it is: object-based notes app where notes are instances of reusable types (books, people, projects) with properties and graph linking, plus daily notes and an AI assistant (https://www.saasradar.app/en/capacities-review; https://www.aitoolscoop.com/ai-tools/capacities)
- Platforms: Windows, macOS, Linux, iOS, Android and web (https://www.aitoolscoop.com/ai-tools/capacities)
- Pricing: free tier plus Pro; third-party trackers put Pro at $9.99/month and a Believer tier at $12.49/month, official pricing-page figure UNVERIFIED in this lane (https://costbench.io/tools/capacities)
- Distinctive features: object/type model with properties instead of flat pages; blocks-based editor; European hosting and privacy-first claims (https://www.saasradar.app/en/capacities-review)
- Gripes: stores no markdown files on disk, per its own docs answering whether it works like Obsidian (https://docs.capacities.io/faq/general-questions); startup takes 5-10 seconds and users worry the hosted model could make their data inaccessible if the company folds (https://www.reddit.com/r/PKMS/comments/1r7qa4r/obsidian_notes_v_capacities_why_this_has_been/); users request a local-only no-sync mode and report images missing from full exports (https://feedback.capacities.io/feature-ideas/p/idea-local-mode-use-capacities-without-server-sync; https://www.reddit.com/r/CapacitiesApp/comments/1t9bfed/missing_images_in_the_export/)

### Roam Research
- What it is: hosted outliner PKM app built on bidirectional links, block references and daily notes (https://agilehubs.com/guides/best-roam-research-alternatives)
- Platforms: web app; mobile via web wrappers, no native apps (https://www.notely.app/blog/roam-research-pricing)
- Pricing: Pro $15/month monthly or $8.33/month billed annually ($99/year), no free tier (https://agilehubs.com/guides/best-roam-research-alternatives; https://roamresearch.com/#/v8/help/articles/827827)
- Distinctive features: Roam 1.0 update provided offline mode and an option to store all data locally, its largest overhaul in years (https://roamresearch.com)
- Distinctive features: bidirectional backlinks and block-level references that set the pattern competitors copied (https://agilehubs.com/guides/best-roam-research-alternatives)
- Gripes: long-running user complaint that development stagnated after 2020 (https://forum.dynalist.io/t/what-happened-to-roam-research-and-are-they-still-in-business/20176); price criticized against modern rivals (https://www.notely.app/blog/roam-research-pricing)

### Dynalist
- What it is: web, desktop and mobile outliner from the team that later built Obsidian (https://www.taskade.com/blog/dynalist-alternatives)
- Platforms: web, Windows/macOS/Linux desktop, iOS/Android (https://www.taskade.com/blog/dynalist-alternatives)
- Pricing: free tier; Pro $7.99/month billed annually or $9.99 monthly, with a $3.33/month annual unlock figure also circulating; official pricing page not fetched in this lane, UNVERIFIED against dynalist.io (https://www.taskade.com/blog/dynalist-alternatives; https://www.outliner.com/market)
- Distinctive features: keyboard-first infinite outlining with zoom-to-branch; same team's future was redirected to Obsidian (https://www.outliner.com/market)
- Gripes: explicitly in maintenance mode with its roadmap frozen in favor of Obsidian (https://www.outliner.com/market); reviewers position it as an alternative because of that stagnation rather than active development (https://www.taskade.com/blog/dynalist-alternatives)

### Google Keep
- What it is: free quick-capture notes with labels, reminders, voice memos and image text extraction (https://ainotely.com/blog/google-keep-review)
- Platforms: Android, iOS, web (https://ainotely.com/blog/google-keep-review)
- Pricing: completely free; notes do not count against Drive storage (https://www.cloudwards.net/google-keep-review/)
- Distinctive features: sticky-note simplicity with color/label organization, reminders and image-text extraction, described by PCMag as almost aggressively simple (https://www.pcmag.com/reviews/google-keep-web)
- Gripes: no Export button for portable formats such as PDF, so archiving means manual copying or Takeout HTML/JSON without link structure (https://www.sheetifycrm.com/blogs/updates/what-are-the-disadvantages-of-google-keep; https://www.marqly.com/blog/export-google-keep); no manual note ordering, even archived notes cannot be moved (https://www.reddit.com/r/GoogleKeep/comments/1vizte3/general_consensus_on_keep_in_2026/); sharing drops titles and images-only, and the flat sticky-pile structure breaks down as projects grow (https://www.androidpolice.com/google-keep-missing-features-annoy-me/; https://www.saner.ai/blogs/best-google-keep-alternatives)
- Gripe: search lags noticeably on large accounts (https://www.reddit.com/r/GoogleKeep/comments/1k8kab0/does_gkeep_have_limit_when_it_comes_to_the_number/)

### Notable
- What it is: cross-platform markdown notes app with frontmatter metadata per note, built on CodeMirror, exporting MD/HTML/PDF (https://notable.app; https://wiredcraft.com/blog/notable-1-8/)
- Platforms: Windows, macOS, Linux desktop (https://notable.app)
- Pricing: free, proprietary; was open source through v1.8.1 and closed after that (https://news.ycombinator.com/item?id=21415575)
- Distinctive features: multi-note editor with inline attachments and math; plain-file storage users can sync themselves via Git or a cloud folder (https://wiredcraft.com/blog/notable-1-8/)
- Gripes: closed-source move drew a maintainer suggestion to fork the last open version, and fork versions of the last open-source release circulate (https://news.ycombinator.com/item?id=21415575); no built-in sync means users juggle their own transport; current release cadence UNVERIFIED in this lane (https://notable.app)

### Boostnote (BoostIO / BoostNote-App)
- What it is: open-source markdown notes app aimed at developers, with a cloud rewrite (BoostNote.next) and a local-space version (https://github.com/BoostIO/BoostNote-App/releases)
- Platforms: Windows, macOS, Linux desktop plus web (https://github.com/BoostIO/BoostNote-App)
- Pricing: free; open source (https://github.com/BoostIO/BoostNote-App)
- Distinctive features: snippet/code-block-centric markdown editor and local-storage space; community local fork BoostNote.next-local keeps the offline version alive (https://github.com/BoostNote-App/local)
- Gripes: the rewrite repository was archived on May 12, 2026 with last release 0.23.0, and the legacy repo was archived as well, so the project has no active maintenance (https://github.com/BoostIO/BoostNote-App/releases; https://github.com/Boostnote/boostnote)
- Gripe: the split between cloud and local-space versions left communities on divergent codebases (https://github.com/BoostNote-App/local)

### aamirenic/IdeaCraft
- What it is: local-first workspace desktop notes app built with Tauri/Rust, ~7 MB app (https://github.com/aamirenic/IdeaCraft)
- Platforms: Windows, macOS, Linux via Tauri (https://tauri.app)
- Pricing/license: UNVERIFIED; no license stated in search results this lane
- Distinctive features: first release v1.0.0; Tauri framing keeps the binary far smaller than Electron peers, the trade-off corpus files discuss for webview risks (https://github.com/aamirenic/IdeaCraft)
- Gripes: repository issue #1 tracks dependency advisories, normal for a young project but a real security-surface signal (https://github.com/aamirenic/IdeaCraft/issues/1); a second repo (Velcent/IdeaCraft) carries an identical description, so users cannot tell which project is canonical (https://github.com/Velcent/IdeaCraft)

### Hypothes.is
- What it is: open annotation layer for web pages, PDFs and ePubs, with public, private and group annotations (https://web.hypothes.is/blog/annotate-web-pdfs-epubs-online/)
- Platforms: web via browser extension and proxy, plus LMS integrations (https://web.hypothes.is/lms/)
- Pricing: free for individuals; institutional plans in Bronze/Silver/Gold tiers tied to LMS integrations (https://web.hypothes.is/lms/); a third-party estimate of roughly $4/user/year for institutions is UNVERIFIED (https://fabric.so/posts/hypothesis)
- License: open source; client and extension repos under BSD-2-Clause (https://github.com/hypothesis/client; https://github.com/hypothesis/chrome-extension)
- Distinctive features: threaded replies between annotators and public annotation layers over any URL or PDF (https://web.hypothes.is/blog/annotate-web-pdfs-epubs-online/)
- Gripes: annotations live only inside Hypothesis with no connection to a knowledge base and no AI features, per a user comparison (https://web.hypothes.is/blog/annotate-web-pdfs-epubs-online/); institutional pricing is not published, forcing sales contact (https://web.hypothes.is/lms/)

### Agenda
- What it is: calendar-driven notes app where notes are organized on a timeline and tied to calendar events and projects (https://agenda.com; https://setapp.com/apps/agenda)
- Platforms: macOS, iOS, iPadOS (https://agenda.com)
- Pricing: free core with optional one-time premium unlocks rather than a subscription, a model users praise in reviews (https://www.producthunt.com/products/agenda/reviews)
- Distinctive features: date-first notes that attach meetings and projects to a timeline, making it a hybrid planner-notes app (https://setapp.com/apps/agenda)
- Gripes: the editor supports only one font, limiting formatting for study use (https://www.agenda.community/t/editing-agenda-documents-edit-copied-older-notes/210); reminder scheduling is limited to on-the-hour times for workday settings (https://www.agenda.community/t/how-to-set-reminder-schedule-for-work-day-times/5304)

### jdkruzr/ultrabridge
- What it is: self-hosted Go bridge for e-ink tablets (Supernote Private Cloud, Onyx Boox, reMarkable) adding integrated search, a TODO index, handwriting recognition through any VLM (ChatGPT, Claude) and an MCP server (https://github.com/jdkruzr/ultrabridge)
- Platforms: self-hosted server (Go) bridging the tablets' cloud endpoints; documented at v1.6.0 (https://github.com/jdkruzr/ultrabridge)
- Pricing: free to self-host; license not stated in the repository search results this lane, UNVERIFIED; its successor project AragoniteAlexandriaServer is Apache-2.0 (https://github.com/jdkruzr/AragoniteAlexandriaServer)
- Distinctive features: CalDAV/WebDAV task sync, render-to-OCR pipeline for search/RAG text, and a native device HWR proxy that returns MyScript JIIX to the tablet (https://github.com/jdkruzr/ultrabridge)
- Gripes: requires running your own server with Supernote Private Cloud as a prerequisite, a real deployment burden (https://github.com/jdkruzr/ultrabridge); some legacy design/test documents describe earlier MariaDB-backed SPC integration, so setup docs have moved over versions (https://github.com/jdkruzr/ultrabridge)

## Master-file additions

===== SECTION: ## Accessibility =====
## Accessibility

No findings file covers accessibility systematically; the corpus's total accessibility signal is seven passing mentions across five files, none of them a per-app survey. The strongest evidence found is structural: a 2026 writeup on building a canvas editor over ProseMirror names screen-reader accessibility "probably the hardest unresolved problem", with the ProseMirror author himself confirming accessibility and touch as the structural risks of any non-DOM view (findings: thread-f-editor-platform.md; https://discuss.prosemirror.net/t/building-a-canvas-based-editor-on-top-of-prosemirror-s-state-and-plugin-system/8982). The same carries into master-file advice: the canvas-plus-document hybrid's hardest cost is accessibility (findings: thread-f-editor-platform.md). In ink apps, hit-target sizes are a documented accessibility finding (findings: linked-apps-2.md). The only WCAG conformance claim anywhere in the corpus belongs to a TTS utility rather than a notes app (TalkBack support targeting WCAG 2.1 AA in marmalade-tts-android, findings: github-repos-2.md). No APPS-LINKS row records screen-reader support, keyboard-only navigation, or contrast behavior for any note app: per-app accessibility (VoiceOver/NVDA/TalkBack) is UNVERIFIED across the board and is the cheapest remaining survey lane for R13.
===== END =====

===== SECTION: ## Search quality =====
## Search quality

User-facing search quality (ranking, fuzzy matching, OCR-search accuracy, search latency) has no dedicated findings file; the corpus covers indexing internals (thread-d-indexing) and editor platforms (thread-f-editor-platform) but never measures quality. Corpus evidence that it matters: Trilium-class users want revisions, scripting, OCR-search and protected notes (findings: linked-apps-1.md), and GoodNotes advertises handwriting OCR search as a core feature (findings: apps-likes-wants.md). Outside the corpus, measured search-quality complaints exist for mainstream apps: Google Keep search lags noticeably on large accounts (https://www.reddit.com/r/GoogleKeep/comments/1k8kab0/does_gkeep_have_limit_when_it_comes_to_the_number/), and Google Keep's search is described as slow when notes pile up (https://www.saner.ai/blogs/best-google-keep-alternatives). A quality comparison lane (search latency, ranking sanity checks, handwriting-search accuracy on the same sample set) would fill the gap; no such measurement exists anywhere in the corpus as of R12.
===== END =====

===== SECTION: ## Data ownership =====
## Data ownership

No dedicated findings file; the corpus's only direct treatment is one line: data-ownership/server fear is the most-cited reason for PKM decisions (findings: r7-user-sentiment-sweep.md), with partial overlap in thread-g-trust-ux. Fresh gaps researched in R12-confirm-9 sharpen the pattern for mainstream apps: Capacities stores no markdown files on disk and has no local-only mode (https://docs.capacities.io/faq/general-questions; https://feedback.capacities.io/feature-ideas/p/idea-local-mode-use-capacities-without-server-sync), and users explicitly worry the hosted model could make data inaccessible if the company folds (https://www.reddit.com/r/PKMS/comments/1r7qa4r/obsidian_notes_v_capacities_why_this_has_been/); Google Keep has no portable export format short of Takeout HTML/JSON without link structure (https://www.sheetifycrm.com/blogs/updates/what-are-the-disadvantages-of-google-keep; https://www.marqly.com/blog/export-google-keep); Roam added a local-storage option only with its Roam 1.0 update (https://roamresearch.com). A dedicated data-ownership audit per app (file access, export fidelity, cloud-only status) is the missing R13 artifact.
===== END =====

===== ROW: Bear =====
| Bear | n | https://bear.app | Apple-only Markdown-style note app organized by nested tags rather than folders; macOS 10.15+ (Apple Silicon), iOS/iPadOS, no Windows/Android/web; free with Bear Pro $2.99/mo or $29.99/yr (7-day trial, grandfathered plans), sync and themes gated behind Pro; PDF/image OCR search in Pro; long-standing Apple-lock-in makes it a recurring switching destination; findings: r12-confirm-9 |
===== END =====

===== ROW: Apple Notes =====
| Apple Notes | n (bundled with Apple OSes) | https://support.apple.com/apple-notes | Apple's free system notes app, the default every competitor is compared against; iPhone/iPad/Mac/Watch plus iCloud web; locked notes, collaboration, Apple Pencil, Math Notes and Image Wand AI features; iOS 26/macOS Tahoe 26 added Markdown import/export; gripes: no Markdown typing before iOS 26, one-note-at-a-time export with blurry handwriting PDFs, sync-erasure complaints, organization degrades past a few hundred notes, no Windows/Android; findings: r12-confirm-9 |
===== END =====

===== ROW: Capacities =====
| Capacities | n | https://capacities.io | Object-based notes app: notes as instances of reusable types (books, people, projects) with properties, graph linking, daily notes, AI assistant; Windows/macOS/Linux/iOS/Android/web; free tier plus Pro (third-party figures $9.99/mo Pro, $12.49/mo Believer; official page UNVERIFIED this lane); gripes: no markdown files on disk (own docs), 5-10s startup, hosted-only storage with no local-only mode yet, images missing from full export; findings: r12-confirm-9 |
===== END =====

===== ROW: Roam Research =====
| Roam Research | n | https://roamresearch.com | Hosted outliner PKM app built on bidirectional links, block references and daily notes; web plus web-wrapped mobile, no native apps; Pro $15/mo or $8.33/mo billed annually, no free tier; Roam 1.0 added offline mode and local data storage; gripes: development stagnation since 2020, price against modern rivals; findings: r12-confirm-9 |
===== END =====

===== ROW: Dynalist =====
| Dynalist | n | https://dynalist.io | Web/desktop/mobile outliner from the team that later built Obsidian; keyboard-first infinite outlining with zoom-to-branch; free tier, Pro $7.99/mo annual or $9.99 monthly (third-party figure, official page UNVERIFIED this lane); explicitly in maintenance mode with roadmap frozen in favor of Obsidian; findings: r12-confirm-9 |
===== END =====

===== ROW: Google Keep =====
| Google Keep | n | https://keep.google.com | Free quick-capture sticky-style notes with labels, reminders, voice memos and image text extraction; Android/iOS/web; completely free, notes do not count against Drive storage; gripes: no PDF/portable export (Takeout gives HTML/JSON without link structure), no manual note ordering even for archived notes, flat structure that breaks down as projects grow, search lag on large accounts; findings: r12-confirm-9 |
===== END =====

===== ROW: Notable =====
| Notable | n (open source through v1.8.1, closed after) | https://notable.app | Cross-platform markdown notes app with per-note frontmatter metadata, CodeMirror editor, inline attachments and math, MD/HTML/PDF export; Windows/macOS/Linux; plain-file storage synced by the user via Git or cloud folder; went closed source at v1.8.1; current release cadence UNVERIFIED this lane; findings: r12-confirm-9 |
===== END =====

===== ROW: Boostnote =====
| Boostnote | y | https://github.com/BoostIO/BoostNote-App | Open-source developer-focused markdown notes app (BoostIO), cloud rewrite plus local-space version; Windows/macOS/Linux/web; rewrite archived May 12, 2026 (last release 0.23.0) and legacy repo archived too, so no active maintenance; community local fork BoostNote.next-local keeps offline use alive; findings: r12-confirm-9 |
===== END =====

===== ROW: Hypothes.is =====
| Hypothes.is | y (hypothesis/h and extension repos, BSD-2-Clause) | https://web.hypothes.is | Open annotation layer for web pages, PDFs and ePubs with public/private/group annotations and threaded replies; browser extension and proxy plus LMS integrations; free for individuals, institutional Bronze/Silver/Gold LMS plans (pricing not published, ~$4/user/year third-party estimate UNVERIFIED); gripes: annotations live only inside Hypothesis, no knowledge-base or AI connection; findings: r12-confirm-9 |
===== END =====

===== ROW: Agenda =====
| Agenda | n | https://agenda.com | Calendar-driven notes app: notes tied to calendar events and projects on a timeline; macOS/iOS/iPadOS; free core with one-time premium unlocks instead of subscription (praised in user reviews); gripes: single font in editor, reminder scheduling limited to on-the-hour workday times; findings: r12-confirm-9 |
===== END =====

===== ROW: aamirenic/IdeaCraft =====
| aamirenic/IdeaCraft | UNVERIFIED (license not stated in this lane's sources) | https://github.com/aamirenic/IdeaCraft | ~7 MB Tauri/Rust local-first workspace desktop notes app (Windows/macOS/Linux via Tauri); first release v1.0.0; issue #1 tracks dependency advisories; Velcent/IdeaCraft carries an identical description, canonical relationship UNVERIFIED; findings: r12-confirm-9 |
===== END =====

===== ROW: jdkruzr/ultrabridge =====
| jdkruzr/ultrabridge | UNVERIFIED (repo license not stated this lane; successor AragoniteAlexandriaServer is Apache-2.0) | https://github.com/jdkruzr/ultrabridge | Self-hosted Go bridge for e-ink tablets (Supernote Private Cloud, Onyx Boox, reMarkable): CalDAV/WebDAV sync, integrated search and TODO index, handwriting recognition via any VLM (ChatGPT/Claude), MCP server; native device HWR proxy returns MyScript JIIX; documented at v1.6.0; requires running your own server with Supernote Private Cloud; findings: r12-confirm-9 |
===== END =====

LANE 9 COMPLETE — 24 coverage gaps, 4 feature-area gaps, 12 gaps researched
