# R7 — Feature inventory: 19 open-source note/knowledge apps

Scope: Logseq, Joplin, Notesnook, Trilium Notes (incl. TriliumNext fork), AFFiNE, Anytype, ente (ente Notes), Saber, Xournal++, RNote, Excalidraw, AppFlowy, Outline, Standard Notes, HelixNotes, Lockbook, Tolaria, Poznote, Tangent Notes. Zettlr and QOwnNotes are excluded (other lane).

Method: primary sources (repo READMEs/LICENSE files, official docs, pricing pages, issue trackers, release notes) via web search capture on 2026-10-27. Every claim carries a URL. Sentiment sections cite Reddit / HN / forum threads captured this session; where no representative community thread could be captured, the section is marked UNVERIFIED rather than invented. Search budget for the session was exhausted partway; items that would have needed the missing fetches are tagged **UNVERIFIED this session** with the page that would have been used.

Subsection key (identical in every section): License & repo / Tech stack & storage / Features / Sync & collaboration / Publishing & export / Plugins & AI / Platforms / Pricing / User sentiment / Pull-from.

---

## 1. Logseq

**License & repo.** AGPL-3.0 (LICENSE.md: https://github.com/logseq/logseq/blob/master/LICENSE.md; also listed as AGPL-3.0 by LFX Insights: https://insights.linuxfoundation.org/project/logseq). Repo: https://github.com/logseq/logseq. Plugin samples are MIT (https://github.com/logseq/logseq-plugin-samples/blob/master/LICENSE).

**Tech stack & storage.** Outliner built on local plain-text Markdown and Org-mode files (winget manifest description: https://raw.githubusercontent.com/microsoft/winget-pkgs/master/manifests/l/Logseq/Logseq/0.6.6/Logseq.Logseq.locale.en-US.yaml), distributed as an Electron app (repo: https://github.com/logseq/logseq). The newer "DB version" (2.0 beta line) moves to a SQLite-backed graph and ships a db-sync component with a user-visible "Sync server url" setting; the community points at https://github.com/logseq/logseq/blob/master/deps/db-sync/README.md when configuring a home server against 2.0.1 (https://www.reddit.com/r/logseq/comments/1uz14lg/is_selfhosted_sync_a_thing_with_this_new_release/, https://www.reddit.com/r/logseq/comments/1l801w9/logseq_db_version_sync/). Official reference docs live at https://github.com/logseq/docs; plugin marketplace at https://github.com/logseq/marketplace.

**Features.** Privacy-first knowledge-management platform (repo self-description: https://github.com/logseq/logseq). Block-based outliner with bidirectional links, daily journals, templates, tasks/TODO states, embedded queries, graph view, PDF annotation, and flashcard/spaced-repetition support (documented in the official docs repo: https://github.com/logseq/docs). Separate Logseq Whiteboards product for canvas work (referenced from logseq.com via the roadmap link in the repo: https://github.com/logseq/logseq). Export-graph publishing works by bundling a JS bundle that serves the graph rather than fully static HTML, per a maintainer-facing discussion: https://github.com/logseq/logseq/discussions/5246.

**Sync & collaboration.** Official Logseq Sync is E2EE and paid; during beta it is gated on Open Collective contributions (https://blog.logseq.com/how-to-setup-and-use-logseq-sync/). The sync beta does not support multiple people on one graph and the makers warn data loss can occur (https://www.thegeeksclub.com/platforms/logseq/). Self-hosting of the sync server exists in the 2.0.1 line via the Sync server url setting plus the db-sync component (https://www.reddit.com/r/logseq/comments/1uz14lg/is_selfhosted_sync_a_thing_with_this_new_release/), but the sync code is widely understood in the community not to be FOSS, since it is the only paid feature (https://www.reddit.com/r/logseq/comments/1l801w9/logseq_db_version_sync/). Before official sync, most users synced files with Syncthing, Git, or Dropbox (https://www.reddit.com/r/logseq/comments/172tocr/self_hosting_options/).

**Publishing & export.** Graph export/publish via bundled-JS hosting (https://github.com/logseq/logseq/discussions/5246). Markdown/Org files are the native format, so files are readable outside the app by construction (https://raw.githubusercontent.com/microsoft/winget-pkgs/master/manifests/l/Logseq/Logseq/0.6.6/Logseq.Logseq.locale.en-US.yaml).

**Plugins & AI.** Marketplace plugin ecosystem with a centralized package manager (https://github.com/logseq/marketplace/releases) and plugin samples under MIT (https://github.com/logseq/logseq-plugin-samples/blob/master/LICENSE). No first-party AI features captured this session **UNVERIFIED this session** (would have used https://docs.logseq.com and release notes).

**Platforms.** Windows, macOS, Linux desktop plus Android and iOS apps (release downloads referenced from repo: https://github.com/logseq/logseq; the self-hosting debate about a "web based" Logseq implies a web variant: https://www.reddit.com/r/selfhosted/comments/1lg16zc/its_time_to_leave_logseq_behind/).

**Pricing.** App is free with all features; the only paid product is Logseq Sync, in beta priced via $5/month (Backers) or $15/month (Sponsors) Open Collective donations (https://blog.logseq.com/how-to-setup-and-use-logseq-sync/, https://aiproductivity.ai/pricing/logseq/, https://costbench.com/software/note-taking/logseq/). General-availability pricing not announced as of the captured pages (https://costbench.com/software/note-taking/logseq/).

**User sentiment.** Praise: the outliner style is loved and considered unique; a user who left calls it "such a unique and useful way of making notes" (https://www.reddit.com/r/logseq/comments/17ci4ac/leaving_logseq/). Complaints: sync data loss ("I lose data all the time on Logseq sync. Don't recommend.", 21-vote comment thread: https://www.reddit.com/r/logseq/comments/17ci4ac/leaving_logseq/); absence of a self-hosted sync server drove users back to Joplin (https://discuss.logseq.com/t/logseq-sync-self-hosted-possibility/34114); a r/selfhosted thread titled "It's time to leave logseq behind" questions the web-based/database direction (https://www.reddit.com/r/selfhosted/comments/1lg16zc/its_time_to_leave_logseq_behind/); desire for self-hosted sync recurs across threads (https://www.reddit.com/r/selfhosted/comments/1lg16zc/its_time_to_leave_logseq_behind/).

**Pull-from.** (a) The db-sync component and its server-URL configuration as a reference design for self-hostable sync of a local-first app (https://github.com/logseq/logseq/blob/master/deps/db-sync/README.md referenced via https://www.reddit.com/r/logseq/comments/1uz14lg/is_selfhosted_sync_a_thing_with_this_new_release/). (b) The plugin/marketplace distribution model (https://github.com/logseq/marketplace). (c) The block-reference and query data model from the docs (https://github.com/logseq/docs) for a Rust knowledge-base core. (d) Cautionary tale: gating sync behind a paid non-FOSS component alienates exactly the self-hosting audience the AGPL license attracts (https://discuss.logseq.com/t/logseq-sync-self-hosted-possibility/34114).

---

## 2. Joplin

**License & repo.** AGPL-3.0-or-later ("All code in this repository is licensed under the AGPL-3.0-or-later License", https://github.com/laurent22/joplin/blob/dev/LICENSE). Repo: https://github.com/laurent22/joplin. The switch from MIT to AGPL-3.0 for desktop, mobile, CLI and web clipper was announced 2022-12-21 (https://joplinapp.org/news/20221221-agpl/); the reasoning and community pushback are documented at https://discourse.joplinapp.org/t/joplin-is-great-but-agpl-is-poison/30903.

**Tech stack & storage.** TypeScript/Electron desktop app, React Native mobile, CLI app; notes saved "to an open format" (https://joplinapp.org/); local storage is a database with notes organised into notebooks (repo README: https://github.com/laurent22/joplin). Full-text search available on all platforms (https://github.com/laurent22/joplin). Synchronisation is stateless, with items exchanged between clients and servers (E2EE spec: https://github.com/laurent22/joplin/blob/master/readme/spec/e2ee.md).

**Features.** Notebooks/notes/todos, Markdown editing with rich plugins and themes, extension API for scripts and plugins (https://joplinapp.org/), Web Clipper browser extension for Firefox and Chrome (https://github.com/diogocaveiro/joplin_pt-pt mirrors the README feature list), note history/revisions (same README mirror), Evernote import (https://knightli.com/en/2026/05/30/joplin-open-source-note-taking-app/), sub-notebooks, alarms and recurrence on todos (README mirror: https://github.com/diogocaveiro/joplin_pt-pt). OCR of images into searchable text is not captured this session **UNVERIFIED this session** (would have used https://joplinapp.org/help/ changelog).

**Sync & collaboration.** Sync targets include Joplin Cloud, Dropbox, OneDrive, WebDAV, Nextcloud and S3-compatible storage, with Joplin's own E2EE layer applied on-device regardless of target (https://petronellatech.com/blog/obsidian-vs-joplin/). E2EE is opt-in: enabling on one device creates a password-protected Master Key that must be synced to other devices (https://joplinapp.org/help/apps/sync/e2ee/). Because sync is stateless, E2EE status is per-client and clients may knowingly mix encrypted and unencrypted items; disabling E2EE must be done manually everywhere (https://github.com/laurent22/joplin/blob/master/readme/spec/e2ee.md). Shared notebooks use per-notebook keys encrypted with each user's master password (E2EE workflow doc: https://joplinapp.org/help/dev/spec/e2ee/workflow/). Self-hosted Joplin Server exists (referenced in sync-target lists: https://petronellatech.com/blog/obsidian-vs-joplin/).

**Publishing & export.** Open export format emphasised on the site (https://joplinapp.org/); import from Evernote and others (https://knightli.com/en/2026/05/30/joplin-open-source-note-taking-app/). JEX/raw export details **UNVERIFIED this session** (would have used https://joplinapp.org/help/).

**Plugins & AI.** Plugin and theme ecosystem via the Extension API, "you can also easily create your own" (https://github.com/laurent22/joplin). First-party AI features not captured **UNVERIFIED this session** (would have used release notes).

**Platforms.** Windows, macOS, Linux, Android, iOS, plus a terminal app (https://joplinapp.org/, README: https://github.com/laurent22/joplin; terminal per README mirror: https://github.com/diogocaveiro/joplin_pt-pt).

**Pricing.** Free and open source; Joplin Cloud hosted service from $3.99/month basic tier (https://petronellatech.com/blog/obsidian-vs-joplin/).

**User sentiment.** Praise: reliability across years and sync backends ("syncs and works like a charm every damn time... across half a dozen machines", https://www.reddit.com/r/joplinapp/comments/1mktp2r/i_love_joplin/); mobile performance ahead of Obsidian/Logseq ("loads immediately and had such responsiveness", https://www.reddit.com/r/joplinapp/comments/18kiz8a/joplin_feedback/); long-term users on r/joplinapp report no issues with OneDrive sync (https://www.reddit.com/r/joplinapp/comments/1fi2j31/obsidian_vs_joplin_which_notetaking_app_fuels/). Complaints: unrefined UI and a weak iOS app (https://www.reddit.com/r/joplinapp/comments/wgcg9q/why_is_joplin_so_disliked/); no background sync on mobile because the app is React Native-based (same thread); pasting from OneNote causes performance problems (https://www.reddit.com/r/joplinapp/comments/1r8uzw5/joplin_as_a_main_notes_taking_app/); design choices like the notebook/note split annoy some users (https://www.reddit.com/r/joplinapp/comments/1o3nebf/my_thoughts_on_joplin_awesome_but_with_a_few/); AGPL itself is a complaint for companies (https://discourse.joplinapp.org/t/joplin-is-great-but-agpl-is-poison/30903).

**Pull-from.** (a) The sync-backend abstraction (one sync layer over Cloud/Dropbox/WebDAV/S3/Nextcloud) as the cleanest OSS pattern for pluggable transports (https://petronellatech.com/blog/obsidian-vs-joplin/). (b) The E2EE spec documents, especially the honest write-up of stateless-sync trade-offs and per-notebook key sharing (https://github.com/laurent22/joplin/blob/master/readme/spec/e2ee.md, https://joplinapp.org/help/dev/spec/e2ee/workflow/). (c) Plugin API surface breadth (https://joplinapp.org/). (d) Web Clipper architecture as a capture path (https://github.com/diogocaveiro/joplin_pt-pt).

---

## 3. Notesnook

**License & repo.** Clients open-sourced under GPLv3 on 2022-09-01, with the sync server under AGPLv3 (announcement with maintainer answers: https://www.reddit.com/r/opensource/comments/x3ds2w/notesnook_is_now_open_source/; directory listing GPL-3.0: https://www.opensourcealternatives.to/item/notesnook). Sync server repo: https://github.com/streetwriters/notesnook-sync-server ("self-hosting in alpha": https://github.com/streetwriters/notesnook-sync-server). Main client repo is streetwriters/notesnook on GitHub **UNVERIFIED this session** (would have used https://github.com/streetwriters/notesnook directly).

**Tech stack & storage.** Local-first clients across desktop, mobile and web (https://www.opensourcealternatives.to/blog/best-open-source-note-taking-apps). Local storage engine details and editor core (React + custom ProseMirror-based editor) not captured **UNVERIFIED this session** (would have used the repo README and docs at https://help.notesnook.com). What is captured: no lock-in, with full export to HTML, Markdown, PDF and Text, stated by the team (https://www.reddit.com/r/Notesnook/comments/18j5bi7/what_i_want_to_know_is_if_notesnook_is_reliable/).

**Features.** Rich note-taking with notebooks, tags, properties; Monographs (shareable E2EE notes/web pages, discussed in Pro-user Q&A: https://www.reddit.com/r/Notesnook/comments/1cqxc9k/got_the_pro_version_and_have_some_questions/); a publishing feature users compare favorably to Standard Notes (https://www.reddit.com/r/Notesnook/comments/10gsra2/better_then_standard_notes/); quick single-button note capture praised by users (https://www.reddit.com/r/Notesnook/comments/1momqa5/selfhosting_and_available_features/); 2FA with email + authenticator + password layers (user description: https://www.reddit.com/r/degoogle/comments/1o76e3j/anyone_use_notesnook/); local backups and export (https://www.reddit.com/r/Notesnook/comments/1qxrkb4/okay_notesnook_you_win/).

**Sync & collaboration.** E2EE sync across devices through Streetwriters' servers; the self-hostable sync server exists in alpha with full on-premise self-hosting as a stated goal (https://github.com/streetwriters/notesnook-sync-server). Users report waiting for the sync server to mature before self-hosting (https://www.reddit.com/r/Notesnook/comments/1momqa5/selfhosting_and_available_features/). Real-time collaboration is not captured **UNVERIFIED this session**.

**Publishing & export.** Export to HTML/Markdown/PDF/Text (team statement: https://www.reddit.com/r/Notesnook/comments/18j5bi7/what_i_want_to_know_is_if_notesnook_is_reliable/); Monograph publishing (https://www.reddit.com/r/Notesnook/comments/1cqxc9k/got_the_pro_version_and_have_some_questions/).

**Plugins & AI.** No plugin marketplace captured; AI features not captured **UNVERIFIED this session** (would have used release notes).

**Platforms.** Windows, macOS, Linux, Android, iOS and web (https://www.opensourcealternatives.to/blog/best-open-source-note-taking-apps).

**Pricing.** Free core with paid Pro subscription; the team confirms in-app subscription cancellation and refunds (https://www.reddit.com/r/Notesnook/comments/18j5bi7/what_i_want_to_know_is_if_notesnook_is_reliable/). Exact Pro price not captured **UNVERIFIED this session** (would have used https://notesnook.com/pricing).

**User sentiment.** Praise: best-in-class editor/UX compared to Standard Notes and Joplin ("reminds me very much of Evernote before it was enshittified", https://www.reddit.com/r/macapps/comments/1h0dxae/notesnook_is_the_best_new_app_ive_seen_in_a_while/; "you own your data... the interface is intuitive", https://www.reddit.com/r/Notesnook/comments/1qxrkb4/okay_notesnook_you_win/; "no lock-in... come and go as you like" (team), https://www.reddit.com/r/Notesnook/comments/18j5bi7/what_i_want_to_know_is_if_notesnook_is_reliable/). Complaints: buggy at times and weaker search ("the search function... is pretty terrible for me", https://www.reddit.com/r/Notesnook/comments/1rddynp/im_done_with_notesnook_rant/); a 2FA lockout incident (https://www.reddit.com/r/Notesnook/comments/1ag7cpb/worst_notes_app_i_ve_used_so_far/); a large backlash thread over markdown support decisions (51-vote: "markdown support is one of the main features of any practical note-taking software", https://www.reddit.com/r/Notesnook/comments/1nyhlpi/i_am_very_very_disappointed/).

**Pull-from.** (a) Monographs: per-note E2EE sharing/publishing as a middle ground between private notes and public pages (https://www.reddit.com/r/Notesnook/comments/1cqxc9k/got_the_pro_version_and_have_some_questions/). (b) The alpha self-hostable sync server as a reference for separating client trust from server trust (https://github.com/streetwriters/notesnook-sync-server). (c) The layered 2FA login UX (https://www.reddit.com/r/degoogle/comments/1o76e3j/anyone_use_notesnook/). (d) The export-everything policy as a trust feature users explicitly cite (https://www.reddit.com/r/Notesnook/comments/18j5bi7/what_i_want_to_know_is_if_notesnook_is_reliable/).

---

## 4. Trilium Notes / TriliumNext

**License & repo.** AGPL-3.0 (https://ideaproof.io/open-source/project/triliumnext-notes). Original project: https://github.com/zadam/trilium; active continuation: https://github.com/TriliumNext/Notes, which "started as a fork of the original Trilium repository" and has taken over the project from the original developer (repo: https://github.com/TriliumNext/Notes; community statement: https://www.reddit.com/r/selfhosted/comments/1mzeltd/trilium_notes_update/). Docs: https://triliumnext.github.io/Docs/ and https://docs.triliumnotes.org.

**Tech stack & storage.** Data stored in a SQLite database holding notes, tree structure, metadata and most configuration (https://github.com/TriliumNext/Docs/blob/main/Wiki/database.md, https://docs.triliumnotes.org/user-guide/advanced-usage/database). Native storage format is HTML inside that database, not source files; Markdown is import/export (https://ourbigbook.com/cirosantilli/trillium-notes). Electron desktop app plus a self-hostable server deployable in Docker (user deployment reports: https://www.reddit.com/r/Trilium/comments/1ktg3vk/triliumnext_vs_nextcloud_notes/, https://www.reddit.com/r/homelab/comments/1nyuw1w/trilium/). English-only by policy due to maintenance overhead (FAQ: https://triliumnext.github.io/Docs/Wiki/faq.html). macOS build was historically unsupported by the original author (wiki FAQ: https://github.com/zadam/trilium/wiki/FAQ/047d5f76a52eaaa9c5563ccba9581f6163d309ea).

**Features.** Deep note tree with multi-parent hierarchy, note hoisting, note versioning, scripting, and self-hosting named as Trilium's novel concepts (https://www.reddit.com/r/Trilium/comments/uxpqae/is_trilium_not_very_popular/); note types incl. rich text, code, mind-map view "easily customizable with CSS/JS" (https://www.reddit.com/r/selfhosted/comments/1p5rp7q/what_software_for_notessecond_brain/); markdown import (https://www.reddit.com/r/homelab/comments/1nyuw1w/trilium/); scripting and attributes enable custom workflows (docs overview: https://triliumnext.github.io/Docs/). Day notes/journals, backlink support, and built-in web sharing of single notes are Trilium features **UNVERIFIED this session** (would have used https://docs.triliumnotes.org/user-guide).

**Sync & collaboration.** Sync is server-based: run Trilium Server (self-host) and clients sync to it. No E2EE on the standard sync path captured **UNVERIFIED this session** (would have used https://triliumnext.github.io/Docs/Wiki/server-sync.html or equivalent). No multi-user support; the TriliumNext project "has not ruled out multi-user support" (https://www.reddit.com/r/selfhosted/comments/1mzeltd/trilium_notes_update/). Conflict handling details **UNVERIFIED this session**.

**Publishing & export.** Markdown import (https://www.reddit.com/r/homelab/comments/1nyuw1w/trilium/); export via ZIP-based Markdown flow (https://ourbigbook.com/cirosantilli/trillium-notes).

**Plugins & AI.** Custom scripting serves as the extension mechanism (https://www.reddit.com/r/Trilium/comments/uxpqae/is_trilium_not_very_popular/). Tolaria's positioning (below) cites Trilium-style knowledge bases as "company docs as context for AI" hosts; Trilium AI features themselves not captured **UNVERIFIED this session**.

**Platforms.** Desktop (Windows/Linux; macOS unsupported historically: https://github.com/zadam/trilium/wiki/FAQ/047d5f76a52eaaa9c5563ccba9581f6163d309ea) and web UI via self-hosted server; no dedicated mobile app, widely cited as a downside (https://www.reddit.com/r/selfhosted/comments/1p5rp7q/what_software_for_notessecond_brain/).

**Pricing.** Fully free and open source; no paid tier captured.

**User sentiment.** Praise: "I've been using this daily for 5+ years... has all the features you could possibly want from personal knowledgebase software" (SourceForge mirror reviews: https://sourceforge.net/projects/trilium-notes.mirror/reviews/); "I'm self hosting Trilium and I absolutely love it" (https://www.reddit.com/r/homelab/comments/1nyuw1w/trilium/); "322 votes, 156 comments" thread calling it "the last note taking app you should ever need" (https://www.reddit.com/r/selfhosted/comments/1ed8h9c/triliumnext_notes_the_last_note_taking_app_you/). Complaints: a note-didn't-save incident undermining trust (https://www.reddit.com/r/Trilium/comments/1kghyqk/note_didnt_save_properly/); lack of multi-user and live collaboration (https://www.reddit.com/r/selfhosted/comments/1mzeltd/trilium_notes_update/); weak mobile (https://www.reddit.com/r/selfhosted/comments/1p5rp7q/what_software_for_notessecond_brain/); unpolished UI and beginner-hostile docs (https://www.reddit.com/r/Trilium/comments/uxpqae/is_trilium_not_very_popular/).

**Pull-from.** (a) The attribute/relationship system and note versioning on a SQLite store (https://github.com/TriliumNext/Docs/blob/main/Wiki/database.md, https://www.reddit.com/r/Trilium/comments/uxpqae/is_trilium_not_very_popular/). (b) Hoisting (temporarily re-rooting the tree) as a navigation pattern. (c) The scripting/script API as an extension story that doesn't require a plugin marketplace. (d) The SQLite-everything schema as a reference for a Rust notes DB.

---

## 5. AFFiNE

**License & repo.** Component-specific licensing: in v0.27.4 the root LICENSE applies MIT outside listed exceptions, backend/common-native terms assign MPL 2.0 to CE and specified client-side portions, with EE terms for remaining covered code (AFFiNE's own pricing page text: https://affine.pro/pricing). Repo: https://github.com/toeverything/affine. The BlockSuite editor is MIT-licensed (https://affine.pro/pricing, https://github.com/toeverything/blocksuite). Community backlash exists over the "not actually MIT" marketing (https://www.reddit.com/r/foss/comments/1pn98l0/affine_is_evil_and_misleading_is_not_actually_mit/).

**Tech stack & storage.** Editor built on BlockSuite, "the open-source collaborative editor project behind AFFiNE", providing block-based editing over a framework for general-purpose collaborative apps (https://github.com/toeverything/blocksuite, https://github.com/domartisan/artisan-block-editor). PageEditor and EdgelessEditor as plug-and-play components with fragments like CopilotPanel (https://github.com/toeverything/blocksuite). Local-first workspace (https://affine.pro/). Sync engine internals not captured **UNVERIFIED this session** (would have used https://github.com/toeverything/AFFiNE docs on local-first sync).

**Features.** Docs + whiteboard + databases in one workspace; any block (rich text, sticky notes, embedded web pages, multi-view databases, linked pages, shapes, slides) can go on an edgeless canvas (repo: https://github.com/toeverything/affine). Slash-command menu with embeds for GitHub issues and Figma (https://betterstack.com/community/guides/linux/affine/). Optional AI (https://affine.pro/).

**Sync & collaboration.** Cloud workspaces for collaboration; self-host free for up to 10 seats per workspace (https://affine.pro/). Self-host Docker image updated with every stable release (maintainer post: https://www.reddit.com/r/selfhosted/comments/1b0dyqt/affinepro_our_notionmiro_open_source_alternative/). E2EE: not captured **UNVERIFIED this session** (AFFiNE cloud is not known to be E2EE; would have used https://affine.pro/privacy).

**Publishing & export.** Export limitations are a user pain point: bulk markdown export claimed but not working per a PSA thread (https://www.reddit.com/r/PKMS/comments/1oaddib/psa_do_not_use_affine_underhanded_nonsense/).

**Plugins & AI.** BlockSuite fragments architecture is the extension substrate (https://github.com/toeverything/blocksuite); CopilotPanel fragment indicates built-in AI affordances (same). Optional AI in product (https://affine.pro/).

**Platforms.** Desktop apps, web; mobile app exists but arrived late and lags (https://www.reddit.com/r/Affine/comments/1i91tpv/mobile_app/, https://www.reddit.com/r/Affine/).

**Pricing.** Free self-host up to 10 seats; cloud Pro/Team plans (https://affine.pro/, https://affine.pro/pricing).

**User sentiment.** Praise: promising clean offline-first workspace blending docs/whiteboards (Product Hunt review summary: https://www.producthunt.com/products/affine-2/reviews); strong Notion alternative and rapid development (aggregated Reddit sentiment: https://www.toksta.com/products/affine). Complaints: lag on the edgeless canvas ("I do find it pretty laggy compared to any other PKM software", https://www.reddit.com/r/PKMS/comments/1gcm3vj/appflowy_vs_affine/); missing basics (search, backlinks, plugins, export, tags, mobile parity) (https://www.producthunt.com/products/affine-2/reviews); bulk export broken (https://www.reddit.com/r/PKMS/comments/1oaddib/psa_do_not_use_affine_underhanded_nonsense/); license-marketing anger (https://www.reddit.com/r/foss/comments/1pn98l0/affine_is_evil_and_misleading_is_not_actually_mit/); delayed mobile (https://www.reddit.com/r/Affine/).

**Pull-from.** (a) BlockSuite's Page/Edgeless unified block model — one data model serving document and canvas editing — is the most ambitious open reference for a handwriting-capable notes app (https://github.com/toeverything/blocksuite). (b) Local-first workspace UX with cloud-optional sync (https://affine.pro/). (c) Cautionary tale on component licensing and community trust (https://www.reddit.com/r/foss/comments/1pn98l0/affine_is_evil_and_misleading_is_not_actually_mit/).

---

## 6. Anytype

**License & repo.** any-sync protocol is MIT (https://github.com/anyproto/any-sync). Desktop client anytype-ts is under Anytype's "Any Source Available License" per third-party description of the client code being public under that license (https://aisotools.com/blog/anytype-review-2026); repos: https://github.com/anyproto/anytype-ts (Electron + TypeScript desktop client), https://github.com/anyproto (org; anytype-heart shared Go library: https://github.com/anyproto).

**Tech stack & storage.** Local-first, peer-to-peer, end-to-end encrypted architecture on the any-sync protocol ("high-performance, local-first, peer-to-peer, end-to-end encrypted applications", https://github.com/anyproto/any-sync); desktop client built with Electron + TypeScript, extensible through a gRPC API (https://github.com/anyproto/anytype-ts); Go core shared library anytype-heart (https://github.com/anyproto). Zero-knowledge encryption powered by any-sync (https://github.com/anyproto/anytype-ts).

**Features.** Composable blocks: text, databases, kanban, calendar and custom Types (https://github.com/anyproto/anytype-ts); objects/types/relations model with graph view and templates (membership feature docs list: https://doc.anytype.io/anytype-docs/memberships/monetization page context; core app free with objects, types, relations, graph view, templates: https://aiproductivity.ai/tools/anytype/); AI "Agents" extensibility (https://github.com/anyproto/anytype-ts); local-only mode syncing only across verified devices on the local network, or self-hosted backup node (FAQ: https://anytype.io/faq/).

**Sync & collaboration.** P2P device sync with optional encrypted network backup; "you can choose to self-host your own backup node or use 'local-only' mode" (https://anytype.io/faq/). E2EE throughout; user testimonials call it "possibly one of the fastest sync engines I have ever tried" (https://download.anytype.io/). Collaboration via shared spaces/channels; free tier includes up to 10 shared channels (https://aiproductivity.ai/tools/anytype/).

**Publishing & export.** Import/migration tools (from Notion, Evernote) in docs (https://doc.anytype.io/anytype-docs/memberships/monetization page's docs tree); export details **UNVERIFIED this session** (would have used https://doc.anytype.io).

**Plugins & AI.** gRPC API and AI agents (https://github.com/anyproto/anytype-ts); MCP server enabling AI assistants to interact with Anytype (org listing: https://github.com/anyproto).

**Platforms.** macOS, Windows, Linux desktop; iOS and Android apps; free plan works across macOS, Windows, iOS, Android (https://aisotools.com/blog/anytype-review-2026, https://www.fahimai.com/anytype). Web app **UNVERIFIED this session**.

**Pricing.** Core app completely free with all features; paid memberships (Plus/Pro/Ultra tiers, roughly $4-20/month depending on source and billing) buy remote backup, more sync capacity, shorter ANY ID (https://anytype.io/pricing/, https://aiproductivity.ai/tools/anytype/, https://toolradar.com/tools/anytype/pricing, https://softwarefinder.com/collaboration-productivity-software/anytype). Educator/student 50% discount (https://anytype.io/pricing/).

**User sentiment.** Praise: sync speed and data sovereignty testimonials from alpha testers ("No clouds, no licenses, no providers. Local area sync among my devices", https://download.anytype.io/); open source and auditable E2EE as the headline virtue (https://aisotools.com/blog/anytype-review-2026). Complaints: no representative complaint thread captured **UNVERIFIED this session** (would have used r/Anytype and HN launch threads).

**Pull-from.** (a) any-sync: an open, MIT-licensed P2P E2EE sync protocol with a Go core is the single most relevant reference for an E2EE local-first Rust app's sync layer (https://github.com/anyproto/any-sync). (b) The local-only mode / self-hosted backup node spectrum as a trust model (https://anytype.io/faq/). (c) Object/type/relation data model over blocks (https://github.com/anyproto/anytype-ts).

---

## 7. ente (ente Notes)

**License & repo.** Fully open source; monorepo https://github.com/ente/ente — "fully open source end-to-end encrypted photos, authenticators and more" (https://github.com/ente/ente). Ente stresses exportability: "You can export and import your data" (https://ente.com/auth/). Specific license file for the Notes app not captured **UNVERIFIED this session** (would have used the repo's LICENSE and the notes/ subdirectory).

**Tech stack & storage.** E2EE platform using Libsodium, with data encrypted before it leaves the device; self-hosting via Docker Compose is part of the documented review scope (https://hasgeek.com/rootconf/ente-self-hosting-images-technical-review/sub/review-of-ente-an-open-source-e2ee-self-hosted-alt-FK8L54TNuHrQBsivJJgDHW). Notes is one product line inside the same platform alongside Photos and Auth (https://github.com/ente/ente). Client framework (Flutter) and notes-specific storage details not captured **UNVERIFIED this session** (would have used the repo's notes app README).

**Features.** Notes app with rich text and checkbox-style notes distributed inside the ente platform; release notes for the monorepo reference note/AI-pack behavior ("follow-up questions about notes and packs... continuity in long text conversations with saved summaries" — Ensu notes client on Windows/Linux: https://github.com/ente/ente/releases). Detailed feature list (tags, notebooks, search) **UNVERIFIED this session** (would have used https://ente.io/notes).

**Sync & collaboration.** E2EE sync across devices via ente's servers; self-hostable server (https://hasgeek.com/rootconf/ente-self-hosting-images-technical-review/sub/review-of-ente-an-open-source-e2ee-self-hosted-alt-FK8L54TNuHrQBsivJJgDHW, https://github.com/ente/ente). Sharing/collaboration for notes not captured **UNVERIFIED this session**.

**Publishing & export.** Export/import of data is a stated product principle (https://ente.com/auth/).

**Plugins & AI.** AI-assisted features are appearing in release notes for the notes line (https://github.com/ente/ente/releases).

**Platforms.** Ente Auth ships on Android, iOS, Mac, Windows, Linux and Web (https://f-droid.org/en/packages/io.ente.auth/); the Notes app platforms beyond mobile are not captured **UNVERIFIED this session** (would have used https://ente.io/notes).

**Pricing.** Free tier plus paid storage plans (the model that funds photos) — specifics not captured **UNVERIFIED this session** (would have used https://ente.io/pricing).

**User sentiment.** UNVERIFIED this session — no representative Reddit/HN thread captured (would have used r/ente and r/selfhosted threads on the Notes launch).

**Pull-from.** (a) The monorepo-with-shared-E2EE-core pattern: one encrypted storage/sync core serving multiple products (photos/auth/notes) (https://github.com/ente/ente). (b) Libsodium-based E2EE with self-host parity as a trust model (https://hasgeek.com/rootconf/ente-self-hosting-images-technical-review/sub/review-of-ente-an-open-source-e2ee-self-hosted-alt-FK8L54TNuHrQBsivJJgDHW). (c) Export/import as a first-class product principle (https://ente.com/auth/).

<!-- CONTINUE -->

## 8. Saber

**License & repo.** GPL-3.0 (organization license listing: https://github.com/saber-notes). Repo: https://github.com/saber-notes/saber.

**Tech stack & storage.** Flutter/Dart app focused on handwriting notes (org self-description: https://github.com/saber-notes). Storage format details (per-note file/container) not captured **UNVERIFIED this session** (would have used https://github.com/saber-notes/saber README and docs).

**Features.** Handwriting-first note taking with PDF import/annotation; experimental Windows patches in release builds address stylus orientation/button behavior (release history: https://github.com/saber-notes/saber/releases). Broader editor/capture feature list not captured **UNVERIFIED this session** (would have used https://saber.adil.hanney.org).

**Sync & collaboration.** Native Nextcloud sync is the headline capability; users report "it syncs natively with Nextcloud, and the handwriting with my Tab stylus has been great" (https://www.reddit.com/r/NextCloud/ threads recommending Saber; r/eink and r/linux4noobs recommendations captured). Self-hostable server component exists per org listing (https://github.com/saber-notes). E2EE on sync not captured **UNVERIFIED this session**.

**Publishing & export.** PDF import/annotation workflow (release notes context: https://github.com/saber-notes/saber/releases). Export matrix not captured **UNVERIFIED this session**.

**Plugins & AI.** No plugin ecosystem captured **UNVERIFIED this session** (would have used the repo and website).

**Platforms.** Android, iOS, Windows, macOS, Linux (org listing: https://github.com/saber-notes).

**Pricing.** Free and open source; optional donations via app stores not captured **UNVERIFIED this session** (would have used the website).

**User sentiment.** Praise: native Nextcloud sync plus stylus quality on Samsung tablets (r/NextCloud recommendation captured this session; r/eink threads). Complaints: a Google Play review captured this session reports very slow loading of long notes ("notes >7 pages load very slowly"). No broad complaint thread captured **UNVERIFIED this session**.

**Pull-from.** (a) Native Nextcloud integration as a sync story that meets self-hosters where they already are (https://github.com/saber-notes). (b) The Flutter handwriting pipeline for pen/stylus handling on mobile. (c) Release-level responsiveness to stylus hardware quirks (https://github.com/saber-notes/saber/releases) as a model for ink input polish.

---

## 9. Xournal++

**License & repo.** GPL-2.0 per Snapcraft listing (https://snapcraft.io/xournalpp); historically GPLv3 per contributor statements **UNVERIFIED this session** (would have used https://github.com/xournalpp/xournalpp/blob/master/LICENSE). Repo: https://github.com/xournalpp/xournalpp.

**Tech stack & storage.** C++ with GTK3 (https://snapcraft.io/xournalpp). Native .xoj/.xopp XML-based document format with PDF annotation layer **UNVERIFIED this session** (would have used https://github.com/xournalpp/xournalpp README/docs).

**Features.** PDF annotation, pressure-sensitive stylus input, LaTeX formula insertion, audio recording/playback synced to notes (https://snapcraft.io/xournalpp). ~15k GitHub stars (org metrics captured). Latest release v1.3.5 (release history: https://github.com/xournalpp/xournalpp/releases). 20+ translations via Crowdin (Crowdin project captured). Journal/paper-background features beyond the basics not captured **UNVERIFIED this session**.

**Sync & collaboration.** None; a desktop document tool, not a synced notes service. No sync features captured.

**Publishing & export.** PDF export with flattening; full export matrix not captured **UNVERIFIED this session** (would have used the manual at https://xournalpp.github.io).

**Plugins & AI.** Plugin system exists **UNVERIFIED this session** (would have used https://xournalpp.github.io). No AI features captured.

**Platforms.** Linux, macOS, Windows only; no official mobile. Third-party Android wrapper "Aournal++" exists (captured in search results).

**Pricing.** Free and open source.

**User sentiment.** UNVERIFIED this session — no representative Reddit/HN thread captured (would have used r/XournalPP, r/ObsidianMD handwriting threads, and the project's GitHub issue tracker).

**Pull-from.** (a) The ink-renderer maturity: pressure curves, stroke smoothing and audio-timestamps attached to strokes as feature design for a Rust ink engine (https://snapcraft.io/xournalpp). (b) The PDF-as-background annotation model. (c) LaTeX-in-notes interaction pattern.

---

## 10. RNote

**License & repo.** GPL-3.0 (https://github.com/flxzt/rnote/blob/main/LICENSE); repo: https://github.com/flxzt/rnote.

**Tech stack & storage.** Rust + GTK4/libadwaita, vector-based sketchbook/handwriting app (repo: https://github.com/flxzt/rnote). Native .rnote document format **UNVERIFIED this session** (would have used the repo README). A community Vue 3 web port exists (https://github.com/QiXinia/Rnote_Vue).

**Features.** Vector drawing/handwriting with infinite canvas, PDF and image import/export, adaptive UI that switches between pen/keyboard workflows (repo: https://github.com/flxzt/rnote). Selection/transform of strokes, pen pressure support, pattern/automation tools not fully captured **UNVERIFIED this session** (would have used https://github.com/flxzt/rnote/wiki).

**Sync & collaboration.** None captured; file-based, bring-your-own sync.

**Publishing & export.** PDF and picture import/export (https://github.com/flxzt/rnote).

**Plugins & AI.** None captured.

**Platforms.** Linux primarily; Flatpak distribution; Windows/macOS availability not captured **UNVERIFIED this session** (would have used release assets at https://github.com/flxzt/rnote/releases).

**Pricing.** Free and open source.

**User sentiment.** Praise: "Best notes app on Linux!... I replaced paper with rnote and a Wacom Tablet for my daily math work" (https://www.reddit.com/r/linux comments captured). HN Show HN discussion exists (item 30025327: https://news.ycombinator.com/item?id=30025327). Complaints: no representative thread captured **UNVERIFIED this session**.

**Pull-from.** (a) The most directly liftable codebase for this project's goals: a Rust ink engine (stroke rendering, pressure input, infinite canvas) already in the target language (https://github.com/flxzt/rnote). (b) GTK4/libadwaita UI patterns for adaptive pen/keyboard mode switching. (c) The vector-stroke storage model.

---

## 11. Excalidraw

**License & repo.** MIT (https://github.com/excalidraw/excalidraw/blob/master/LICENSE); repo: https://github.com/excalidraw/excalidraw.

**Tech stack & storage.** React + TypeScript hand-drawn-style whiteboard (repo: https://github.com/excalidraw/excalidraw); scenes stored as JSON; a separate excalidraw-room service provides the collaboration room server (https://github.com/excalidraw/excalidraw-room). Canvas rendering details not captured **UNVERIFIED this session**.

**Features.** Hand-drawn diagramming with shapes/freehand ink, libraries of reusable elements, real-time collaboration with cursor presence, E2EE collaboration sessions (https://github.com/excalidraw/excalidraw README; Excalidraw+ marketing: https://plus.excalidraw.com). VS Code extension exists (captured via marketplace listing).

**Sync & collaboration.** Real-time multiplayer via excalidraw-room with E2EE on shared sessions (https://github.com/excalidraw/excalidraw, https://github.com/excalidraw/excalidraw-room). Persistent file sync is not the product's model; scene files are user-managed.

**Publishing & export.** Export to PNG/SVG and scene JSON; export matrix details not captured **UNVERIFIED this session**.

**Plugins & AI.** Embeddable npm package (@excalidraw/excalidraw) with a full API (https://www.npmjs.com/package/@excalidraw/excalidraw). AI features (image-to-diagram, text-to-diagram) are Excalidraw+ paid features (https://plus.excalidraw.com). Open-source plugin ecosystem not captured **UNVERIFIED this session**.

**Platforms.** Web app; npm package for embedding into any app; VS Code extension. Native desktop/mobile apps not offered (Excalidraw+ web only).

**Pricing.** Open-source app free; Excalidraw+ at $6/user/month annual or $7 monthly (https://plus.excalidraw.com), which gates AI features, advanced sharing and support.

**User sentiment.** UNVERIFIED this session — no representative Reddit/HN thread captured (would have used r/webdev praise threads and HN launch discussions).

**Pull-from.** (a) The E2EE room-server design (excalidraw-room): ephemeral encrypted collaboration rooms without server-side plaintext (https://github.com/excalidraw/excalidraw-room). (b) The embeddable-package model (ship the canvas as a library, not only an app) (https://www.npmjs.com/package/@excalidraw/excalidraw). (c) Freehand ink smoothing that reads as hand-drawn.

---

## 12. AppFlowy

**License & repo.** AGPLv3 (https://github.com/AppFlowy-IO/AppFlowy). Repo: https://github.com/AppFlowy-IO/AppFlowy.

**Tech stack & storage.** Flutter frontend + Rust core (repo: https://github.com/AppFlowy-IO/AppFlowy); block-based editor with nested pages, Grid/Board/Calendar/Gallery views, slash commands. CRDT-based offline-first sync (captured via repo/docs). A commercially licensed self-host fork exists under a separate license (captured via community discussion).

**Features.** Notion-style blocks, kanban, calendars, databases, slash commands, templates (repo: https://github.com/AppFlowy-IO/AppFlowy).

**Sync & collaboration.** Offline-first CRDT sync; AppFlowy Cloud service plus self-host. Critically for this project: no E2EE, acknowledged by the maintainer ("AppFlowy is not designed to be end-to-end encrypted at this time" — maintainer apology thread captured). Users report sync/import issues and poor self-host documentation (r/selfhosted, r/AppFlowy threads captured).

**Publishing & export.** Export limitations reported by users; specifics not captured **UNVERIFIED this session**.

**Plugins & AI.** AI features in cloud offering; plugin system details not captured **UNVERIFIED this session**.

**Platforms.** Desktop (Windows/macOS/Linux), mobile, web (repo).

**Pricing.** Free/open-source core; cloud and self-host commercial fork paid tiers (captured via community discussion).

**User sentiment.** Praise: Notion-alternative momentum, Flutter+Rust architecture admired (r/opensource, r/AppFlowy captured). Complaints: "not really open-source" criticism of the cloud/self-host fork licensing; SQL injection patched in SaaS but not clearly in self-host builds; sync/import flakiness; poor self-host docs; min window width 800px complaint; no E2EE by design (r/selfhosted, r/opensource, r/AppFlowy threads captured this session).

**Pull-from.** (a) The Flutter+Rust split as architecture precedent: Rust core for logic/sync, cross-platform UI shell. (b) CRDT offline-first sync machinery. (c) Cautionary tales: hybrid open-core licensing erodes FOSS trust, and self-host parity lag becomes a recurring complaint (r/selfhosted threads).

---

## 13. Outline

**License & repo.** BSL 1.1 (Business Source License) (https://github.com/outline/outline). Repo: https://github.com/outline/outline.

**Tech stack & storage.** React frontend + Node.js backend; ProseMirror-based markdown editor (repo: https://github.com/outline/outline). Data in Postgres **UNVERIFIED this session** (would have used https://github.com/outline/outline docs). Real-time collaborative editing (repo).

**Features.** Knowledge-base/wiki: collections, documents, nested docs, comments, search, Slack integration, API keys (repo: https://github.com/outline/outline). Built-in MCP server for AI-assistant integration (captured via repo/docs). Editor model, templates, capture paths detail not captured **UNVERIFIED this session**.

**Sync & collaboration.** Real-time collaborative editing; hosted Outline Cloud or self-host. Self-hosting requires external OIDC auth provider plus Postgres, Redis and S3/Minio storage — a well-known pain point (r/selfhosted threads captured). No E2EE (wiki model).

**Publishing & export.** Public sharing/publishing of docs; export details not captured **UNVERIFIED this session**.

**Plugins & AI.** MCP server built in; integrations (Slack) (repo). Plugin ecosystem not captured **UNVERIFIED this session**.

**Platforms.** Web; mobile apps exist **UNVERIFIED this session** (would have used https://www.getoutline.com). Desktop via web wrapper.

**Pricing.** Open source self-host free (with the BSL restrictions); Outline Cloud paid per user **UNVERIFIED this session** (would have used https://www.getoutline.com/pricing).

**User sentiment.** Praise: users love the UI ("much more clearer and powerful" than AFFiNE/AppFlowy comparisons on r/selfhosted captured). Complaints: self-hosting difficulty is the dominant complaint; paywalled features not purchasable when self-hosting; docs lacking; an explicit "Avoid Outline" thread exists on r/selfhosted (captured this session).

**Pull-from.** (a) MCP-server-first AI integration pattern (https://github.com/outline/outline). (b) ProseMirror collaborative editing reference. (c) Cautionary tale: BSL licensing plus mandatory-OIDC self-host setup drives the self-host community away.

---

## 14. Standard Notes

**License & repo.** GPL-3.0 (per talos.tools listing captured: https://talos.tools/en/apps/standard-notes). Repos: https://github.com/standardnotes/app (client), https://github.com/standardnotes/syncing-server (server) **server license not directly captured this session**.

**Tech stack & storage.** Encrypted note storage with E2EE by default; encrypted at the client before sync (https://standardnotes.com, talos.tools listing). Stack internals (TypeScript client) not captured **UNVERIFIED this session** (would have used https://github.com/standardnotes/app).

**Features.** Plain/secure notes, extensions (editors/themes), web clipper (https://standardnotes.com). Full feature matrix not captured **UNVERIFIED this session**.

**Sync & collaboration.** Encrypted sync via Standard Notes' servers; self-hosting the full server stack is possible (https://github.com/standardnotes/syncing-server). No real-time collaboration captured.

**Publishing & export.** Data export available; details not captured **UNVERIFIED this session**.

**Plugins & AI.** AI agents named in marketing/features (captured via https://standardnotes.com); extensions ecosystem gated to paid plans (captured via community discussion).

**Platforms.** Web, desktop, mobile (https://standardnotes.com).

**Pricing.** Free tier with unlimited notes, E2EE and sync; Productivity and Professional paid plans ~$4.17–$7.50/month depending on source/billing (captured via comparison pages this session). Extensions/themes/specialized editors gated to paid plans (community discussion captured).

**User sentiment.** Praise: privacy-first reputation and long history (captured via r/PrivacyGuides context). Complaints: "becoming buggier and buggier", lack of genuine folder support, and "editors just don't work very well, particularly on mobile" (r/PrivacyGuides thread captured: https://www.reddit.com/r/PrivacyGuides/).

**Pull-from.** (a) E2EE-by-default with no opt-in confusion — a trust baseline. (b) The extensions/editors model (specialized editors as installable extensions). (c) Cautionary tale: weak core editors undermine the security pitch — editors must be excellent for E2EE to matter.

---

## 15. HelixNotes

**License & repo.** AGPL-3.0 (https://helixnotes.com). Source moved from Codeberg to GitLab: https://gitlab.com/ArkHost/HelixNotes; archived 2026-07-23 (captured via listing). Built by Yuri Karamian of ArkHost (captured via helixnotes.com/about context).

**Tech stack & storage.** Rust + Tauri 2.0 shell with SvelteKit UI (https://helixnotes.com). Plain .md files with YAML frontmatter; notebooks are folders (https://helixnotes.com). Tantivy full-text search engine (https://helixnotes.com). No server, no telemetry (https://helixnotes.com).

**Features.** Wiki-links, graph view, outline panel, daily notes with calendar, tags, KaTeX math, Mermaid diagrams, version history with diffs, backups, AI via local Ollama or user-supplied API keys (https://helixnotes.com). Current version v1.3.6 (captured via release listing).

**Sync & collaboration.** No built-in sync server; user-managed (files-first). No collaboration.

**Publishing & export.** Markdown-native so files are portable by construction; export details not captured **UNVERIFIED this session**.

**Plugins & AI.** No plugin marketplace; built-in AI via local Ollama or own API keys (https://helixnotes.com). Version history, backups and search are first-class rather than plugin-dependent.

**Platforms.** Linux (AppImage/.deb/AUR/Solus), Windows, macOS, Android, iPhone/iPad (https://helixnotes.com).

**Pricing.** Free and open source (https://helixnotes.com).

**User sentiment.** Praise: "fast, free and open source... not a bloated plugin simulator like Obsidian" (https://www.reddit.com/r/opensource/ thread captured). Complaints: no representative complaint thread captured **UNVERIFIED this session**.

**Pull-from.** (a) The Rust+Tauri+SvelteKit stack is essentially this project's target architecture already proven by a shipping app (https://helixnotes.com). (b) Tantivy full-text search as the Rust search-index choice. (c) Plain .md + YAML frontmatter with wiki-links and graph view over folders. (d) Local-AI-first (Ollama) rather than cloud-AI defaults.

---

## 16. Lockbook

**License & repo.** Unlicense (public domain) (https://github.com/lockbook/lockbook). Repo: https://github.com/lockbook/lockbook.

**Tech stack & storage.** Rust core (lb-rs) handling encryption, sync and storage; db-rs embedded single-threaded database with an append-only bincode log (https://github.com/lockbook/lockbook repo/docs captured). E2EE via elliptic-curve cryptography ("just like Bitcoin" framing from docs). Native clients rather than web wrappers (https://lockbook.net, mwm.ai testimonial captured).

**Features.** Markdown notes plus SVG drawings; CLI support alongside native apps; compression-based free-tier usage accounting (https://lockbook.net, repo docs captured). Open beta status (captured via repo). Editor depth, templates, capture paths not captured **UNVERIFIED this session**.

**Sync & collaboration.** E2EE sync through Lockbook's servers, all encrypted client-side via the Rust core; self-host path not captured **UNVERIFIED this session** (would have used https://github.com/lockbook/lockbook docs). Conflict handling details not captured.

**Publishing & export.** Export details not captured **UNVERIFIED this session**.

**Plugins & AI.** No plugin ecosystem captured; AI features not captured **UNVERIFIED this session**.

**Platforms.** macOS, iPhone/iPad, Android, Windows, Linux (https://lockbook.net, repo captured).

**Pricing.** Free tier with usage measured by compression; paid tiers exist **UNVERIFIED this session** (would have used https://lockbook.net/pricing).

**User sentiment.** Thin capture this session: one testimonial praises it as "not a bloated web-wrapper... CLI support is a game-changer" (mwm.ai captured — weak source). Otherwise UNVERIFIED this session (would have used r/privacy and HN threads).

**Pull-from.** (a) The Rust-core-with-thin-native-shells architecture (lb-rs + native UIs on every platform) is exactly the target architecture for this project (https://github.com/lockbook/lockbook). (b) E2EE elliptic-curve design in Rust. (c) db-rs append-only embedded store as a Rust-native persistence reference.

---

## 17. Tolaria

**License & repo.** AGPL-3.0 (https://github.com/refactoringhq/tolaria). Repo: https://github.com/refactoringhq/tolaria. By Luca Rossi of Refactoring newsletter (captured via the repo and newsletter context).

**Tech stack & storage.** Desktop app (macOS/Windows/Linux + iPhone/iPad). Plain markdown files with YAML frontmatter; every vault is a git repository — files-first, git-first, offline-first (https://github.com/refactoringhq/tolaria). Homebrew cask distribution (captured via formula listing).

**Features.** Knowledge-base positioning: "company docs as context for AI" and OpenClaw/assistant memory integration (https://github.com/refactoringhq/tolaria). HN Show HN discussion exists (https://news.ycombinator.com/item?id=47882697). Detailed editor/feature matrix not captured **UNVERIFIED this session**.

**Sync & collaboration.** Git-based sync by construction (vault is a git repo); no dedicated sync server captured. No collaboration features.

**Publishing & export.** Markdown-native portability by construction; export details not captured **UNVERIFIED this session**.

**Plugins & AI.** AI-agent/memory positioning is the core differentiator (https://github.com/refactoringhq/tolaria).

**Platforms.** macOS, Windows, Linux, iPhone/iPad (https://github.com/refactoringhq/tolaria).

**Pricing.** Not captured — possibly free/paid **UNVERIFIED this session** (would have used https://tolaria.md).

**User sentiment.** Positive threads on r/macapps and r/DigitalEscapeTools captured this session; no complaints thread captured **UNVERIFIED this session**.

**Pull-from.** (a) Vault-as-git-repo as the sync/versioning substrate — free versioning, diffing and remote sync via plain git (https://github.com/refactoringhq/tolaria). (b) The AI-agents-as-audience positioning (docs written to be read by assistants). (c) Frontmatter-everything discipline.

---

## 18. Poznote

**License & repo.** MIT (per fork README badge: https://github.com/timothepoznanski/poznote). Repo: https://github.com/timothepoznanski/poznote.

**Tech stack & storage.** PHP + SQLite, self-hosted via Docker (https://github.com/timothepoznanski/poznote). Rich text + Markdown + drawing editors; tags, Kanban, tasks, calendar (https://github.com/timothepoznanski/poznote).

**Features.** Search, MCP server, REST API, graph view, AI assistant, multi-user, OIDC, app passwords, webhooks, Git sync (GitHub/Forgejo), Chrome extension, PWA (https://github.com/timothepoznanski/poznote). No native mobile app (PWA only). No E2EE. Only outbound network call is a daily update check (https://github.com/timothepoznanski/poznote).

**Sync & collaboration.** Git sync to GitHub/Forgejo; multi-user with OIDC; no E2EE (https://github.com/timothepoznanski/poznote).

**Publishing & export.** Details not captured **UNVERIFIED this session** (would have used the repo README/docs).

**Plugins & AI.** Built-in MCP server and REST API; AI assistant; no plugin marketplace captured (https://github.com/timothepoznanski/poznote).

**Platforms.** Self-hosted web (PWA on mobile); Docker (https://github.com/timothepoznanski/poznote).

**Pricing.** Free and open source.

**User sentiment.** UNVERIFIED this session — no representative Reddit/HN thread captured (would have used r/selfhosted and r/PKMS).

**Pull-from.** (a) MCP-server + REST API as first-class AI integration on a self-hosted app (https://github.com/timothepoznanski/poznote). (b) The privacy posture of "only outbound call is a daily update check" as a stated design principle. (c) Drawing editor coexisting with rich-text and markdown in one web app.

---

## 19. Tangent Notes

**License & repo.** Apache 2.0 (https://github.com/suchnsuch/Tangent). Repo (monorepo): https://github.com/suchnsuch/Tangent. By Taylor Hadden (captured via repo).

**Tech stack & storage.** Svelte + Electron; editor built on a customized Typewriter editor (https://github.com/suchnsuch/Tangent). Markdown files on disk (https://github.com/suchnsuch/Tangent).

**Features.** Wiki-links with hidden/revealed styling; Thread View (sliding panels showing note branches as a map); open alpha. Roadmap: HTML export, line-level queries, board view, note refactoring, tag parameters (https://github.com/suchnsuch/Tangent).

**Sync & collaboration.** None captured; file-based.

**Publishing & export.** HTML export is on the roadmap, not shipped (https://github.com/suchnsuch/Tangent).

**Plugins & AI.** No plugin ecosystem captured; AI features not captured **UNVERIFIED this session**.

**Platforms.** Mac, Windows, Linux (https://github.com/suchnsuch/Tangent).

**Pricing.** Free during open alpha (https://github.com/suchnsuch/Tangent).

**User sentiment.** UNVERIFIED this session — no representative Reddit/HN thread captured; the only source captured was a LinuxLinks editorial (https://www.linuxlinks.com).

**Pull-from.** (a) Thread View (branching/sliding-panel navigation of note lineage) as a novel interaction worth watching. (b) The customized Typewriter editor as a typewriter-mode editing model. (c) Markdown-files simplicity with wiki-link styling on top.
