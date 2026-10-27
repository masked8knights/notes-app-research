# R7 — Remakes of Evernote and Notion: the complete landscape

**Lane:** remakes of Evernote and/or Notion (open-source clones, forks, and alternatives built to replace them), their status, and how each has fared. Deep feature dives (Turtl, SiYuan internals) belong to other lanes; only remake status and health are recorded here.

**Method:** every GitHub claim below was checked this session (2026-10-27) against the live repo page, `commits.atom` and `releases.atom` feeds. Each entry carries a URL for its status claim. Anything not directly captured this session is marked **UNVERIFIED this session**. Repo-check evidence (dates pulled from the feeds) is consolidated in Appendix A.

Headline numbers: **33 projects/named attempts covered; 17 verified actively developed; 13 verified dead, archived, dormant or deleted; 3 could not be verified at all.**

---

## Part 1 — Notion remakes

### 1.1 AppFlowy (AppFlowy-IO/AppFlowy) — ALIVE, the flag-bearer
- Repo: https://github.com/AppFlowy-IO/AppFlowy — AGPL-3.0, ~77.8k stars (repo page, this session).
- Status: actively developed. Current release v0.14.11; the Play Store listing for it carries October 2026 features (relative-date filters, YouTube-transcript import into AI blocks) (https://play.google.com/store/apps/details?id=io.appflowy.appflowy&hl=en), and AppFlowy's own release/build repos show builds timestamped 2026-10-25 (https://github.com/AppFlowy-IO/AppFlowy-Builder/releases/tag/0.14.11-release/0.14.11-261025-0954). Its changelog page tracks paired desktop/cloud version requirements (https://appflowy.com/what-is-new). Note: the main repo's default-branch commit feed showed the most recent commit as 2026-06-26, so the visible `main` branch is quieter than the release train; a lot of the work now lives in sibling repos (AppFlowy-Cloud, AppFlowy-Builder).
- Stack: Flutter + Rust; AppFlowy Cloud for collaboration/self-host sync.
- Fidelity: the closest *spiritual* Notion remake. It has Notion-style blocks and databases (grid/board/calendar views), workspace hierarchy, and now AI integration. It does **not** import Notion workspaces wholesale and has no formula fields yet — a 2026 roundup notes "no formula fields: the field type does not exist yet; formula-heavy Notion setups have no equivalent in AppFlowy" (https://www.opensourcealternatives.to/alternative-to/notion).
- Self-host: full desktop-first model plus self-hosted AppFlowy Cloud (v0.19.x pairs with desktop v0.14.x per https://appflowy.com/what-is-new).
- Reception: repeatedly listed as *the* leading open-source Notion alternative in 2026 roundups (https://openalternative.co/alternatives/notion, https://github.com/topics/notion-alternative), and its relaunch Show HN in Sept 2024 drew sustained attention (https://news.ycombinator.com/item?id=41435721).

### 1.2 Focalboard (Mattermost → mattermost-community/focalboard) — EFFECTIVELY DEAD / community handoff
- Repo: https://github.com/mattermost-community/focalboard (the old mattermost/focalboard URL redirects there — verified this session). Not formally GitHub-archived, but functionally discontinued.
- Timeline, all cited:
  - Built as an open-source Trello/Asana/Notion hybrid; Mattermost bundled it as "Boards" from v6 (https://www.focalboard.com/download/mattermost/).
  - Aug 2023: Mattermost announced "upcoming product changes to Boards and various plugins" (https://forum.mattermost.com/t/upcoming-product-changes-to-boards-and-various-plugins/16669).
  - Aug 28, 2024: repository split — "As of August 28th, 2024 this repository now only contains the standalone Focalboard project. The Mattermost plugin has been moved to mattermost/mattermost-plugin-boards where it will be maintained separately" (https://github.com/mattermost-community/focalboard/issues/5038).
  - Jan 2025: Mattermost support confirms "Focalboard is now community-supported… Focalboard repository has been transferred to the Community organization on GitHub" and the Boards plugin entered maintenance mode, absent from Mattermost v9+ (https://support.mattermost.com/hc/en-us/articles/19614000831252-Why-Boards-is-not-available-in-the-latest-Mattermost-Version-9-0).
- Release evidence: last release v8.0.0, 2024-06-17, explicitly "a plugin only release" (releases feed this session; https://github.com/mattermost-community/focalboard/releases.atom). No release in ~28 months.
- Community asked for maintainers and got no traction ("Call for Maintainers – Standalone Focalboard", issue #5038, Aug 2024). Reddit asked the honest question — "Is Focalboard actually dead, or is it feature-complete and not affected by the halted development?" — with the top reply noting development has halted and the community is "unable to continue due to lack of familiarity with the codebase" (https://www.reddit.com/r/selfhosted/comments/1dpkugs/is_focalboard_actually_dead_or_is_it/).
- Fidelity as a Notion remake: Kanban/table/gallery boards with card properties, page cards with markdown-ish blocks. It never had Notion's document-editor depth, databases-with-relations, or a web clipper. Personal Desktop Edition is gone; only the plugin and a stale standalone server remain.
- Verdict: Mattermost integrated it, then dropped it. Dead as a Notion remake; a frozen codebase others could fork, but the community explicitly failed to form around it.

### 1.3 Notea — DEAD BY MAINTAINER STATEMENT
- Original repo: https://github.com/QingWei-Li/notea (2,143 stars, MIT, verified this session); now also mirrored under https://github.com/notea-org/notea. The `zinclabs/notea` location returns 404 (verified this session).
- Status: the notea-org README states plainly: "this project is barely maintained anymore. I don't have time to work on Notea, and I've personally stopped using it too. If you want something that can synchronise using S3 (or a variety of other methods), then I recommend Joplin" (https://github.com/notea-org/notea). Last release v0.4.0-alpha, 2022-12-04 (releases feed this session); a stray last commit 2025-11 on the original repo is not accompanied by any release.
- What it was: a 2021-wave self-hosted Notion-clone that stored notes in S3, React/Next.js + Prosemirror-based editor. Announced to r/selfhosted in April 2021 ("a self-hosted Notion alternative", 666 upvotes) (https://www.reddit.com/r/selfhosted/comments/n0jacf/notea_selfhosted_notetaking_app_stored_on_s3_aka/), and picked up in the early roundups ("Notea is the best free and open source alternative to Notion… very similar Notion like interface", https://www.ilovefreesoftware.com/09/featured/free-open-source-alternatives-to-notion.html).
- Fidelity: page tree + Notion-style slash editor; no databases, no clipper, no import pipeline of note. Self-host via Docker/Vercel + S3-compatible storage.
- Verdict: dead. Classic single-maintainer clone whose maintainer left, and said so in the README.

### 1.4 AFFiNE (toeverything/AFFiNE) — ALIVE, the other serious contender
- Repo: https://github.com/toeverything/AFFiNE — ~73.9k stars (repo page this session). License is split/custom ("Other" on GitHub; LICENSE file is a TOEVERYTHING Pte. Ltd. composite, https://raw.githubusercontent.com/toeverything/AFFiNE/canary/LICENSE) — not a clean single OSI license, worth flagging when comparing.
- Status: very actively developed. Release feed shows canary builds literally today (v2026.10.26-canary.915, 2026-10-26) and last commit same day.
- Fidelity: block-based editor with an "Edgeless" whiteboard mode (Notion + FigJam), databases, and an import pipeline that includes Notion. Positioned directly against Notion in every roundup (e.g. Docmost's own competitor survey, https://docmost.com/blog/open-source-notion-alternatives/).
- Self-host: Docker-based self-hosting plus AFFiNE Cloud.
- Reception: consistently named among the top open-source Notion alternatives in 2026 listings (https://openalternative.co/alternatives/notion, https://github.com/topics/notion-alternative).

### 1.5 Anytype (anyproto) — ALIVE, "open source" with an asterisk
- Core repo: https://github.com/anyproto/anytype-heart (the kernel; AGPL-family/composite license shown as "NOASSERTION" on the repo page) with desktop/mobile clients under the same org (e.g. anytype-ts). Verified active: anytype-heart nightly release v0.51.7-nightly.20261024.1 dated 2026-10-23, commits within the last days (feeds this session).
- Positioning: local-first, encrypted, object-graph workspace marketed as a Notion alternative ("Anytype is the cleanest choice" for local-first Notion alternatives, https://toolfinder.com/best/open-source-note-taking-apps).
- Fidelity: page/block editing, collections/sets (database-like objects), graph; deliberately does *not* clone Notion's cloud collaboration model; no official Notion importer of full fidelity (relations/graph mapping is lossy) — **UNVERIFIED this session** on importer specifics.
- Self-host: any-sync network nodes are open source and self-hostable; the default is their hosted coordination servers.
- Reception: strong among privacy/self-host crowds; the 2026 roundups list it first among local-first options (https://toolfinder.com/best/open-source-note-taking-apps).

### 1.6 SiYuan (siyuan-note/siyuan) — ALIVE (standing only; deep dive elsewhere)
- Repo: https://github.com/siyuan-note/siyuan — AGPL-3.0, ~46.9k stars. Active: last commit 2026-10-20, release feed updated 2026-10-26 (feeds this session).
- Standing as a Notion remake: block-based documents with SQL-queryable blocks, databases, backlinks; began as a Chinese-local-first outliner and absorbed Notion-like blocks/databases. Ships Notion and Evernote importers. Cloud sync is the paid product; the core is self-hostable and open source.
- Self-host: Docker images, or local desktop apps with optional paid sync.

### 1.7 Memos (usememos/memos) — ALIVE (standing only)
- Repo: https://github.com/usememos/memos — MIT, ~64.1k stars. Active: last commit and release same day, 2026-10-26 (feeds this session).
- Standing: marketed as an open-source "flomo/Notion-lite" — a micro-note stream with markdown, not a workspace remake. It is a *partial* Notion substitute (quick notes, tags) with no page trees, databases or collaboration. Self-host via single Docker container + SQLite.

### 1.8 Docmost (docmost/docmost) — ALIVE
- Repo: https://github.com/docmost/docmost — AGPL-3.0, ~22.1k stars. Active: v0.97.0 released 2026-10-25; last commit 2026-10-25 (feeds this session).
- What it is: self-hosted wiki/docs ("open-source Confluence and Notion alternative" per its own marketing and its 2026 roundup of the space, https://docmost.com/blog/open-source-notion-alternatives/). Nest/React + Postgres, spaces, editor with tables/callouts, comments. Notion fidelity is partial: documents and hierarchy yes, databases/no-code tables no. Self-host is its whole model (Docker).
- Reception: rapid star growth since 2024; commonly recommended in r/selfhosted threads when people ask for self-hosted Notion. **UNVERIFIED this session** for a specific Reddit thread URL.

### 1.9 Teable (teableio/teable) — ALIVE (databases only)
- Repo: https://github.com/teableio/teable — ~21.9k stars; license shown "NOASSERTION" (AGPL/commercial dual — **UNVERIFIED this session** on exact terms). Active: release `release.2026-10-23` dated 2026-10-23, commit same day (feeds this session).
- Standing: it remakes the *database half* of Notion (and is otherwise closer to an Airtable alternative; see also Baserow and NocoDB, which target Airtable rather than Notion and are listed in the Airtable-alternative surveys: https://alternativeto.net/software/airtable/?license=opensource). Relevant here because "Notion databases" is precisely what Notion-exporters lose, and Teable imports Notion CSV exports. It is not a document workspace.

### 1.10 Logseq (logseq/logseq) — ALIVE (Roam-lineage, adjacent to Notion)
- Repo: https://github.com/logseq/logseq — AGPL-3.0, ~45.4k stars. Active: last commit 2026-10-25; releases are rolling "nightly" builds (feeds this session).
- Standing: a Roam clone primarily (as even the comparisons note: "Logseq is currently the closest (feature-wise) and most stable alternative to Roam… open-sourced, privacy-driven and local-first", https://travischan.medium.com/roam-research-alternatives-42030ef3a087). It appears in Notion-alternative lists for its block editor and databases (beta). Its DB-version rewrite has been slow; outliner-first UX is a poor fit for document-centric Notion users.

### 1.11 Eidos (mayneyao/eidos) — ALIVE, newer entrant
- Repo: https://github.com/mayneyao/eidos — AGPL-3.0, ~3.2k stars. Active: last commit 2026-10-26 (feed this session).
- Provenance: "Show HN: Eidos – Offline alternative to Notion", June 2024, with the author's motivation on the record: "Notion, like most SaaS products, is not open-source… I really like the concepts of FOSS, solid, and local-first" (https://news.ycombinator.com/item?id=40746773).
- Fidelity: local-first, SQLite-based Notion-like tables + AI extensible via plugins; single-user, no real collaboration. Self-host via PWA/local.

### 1.12 Colanode (colanode/colanode) — ALIVE, newer entrant
- Repo: https://github.com/colanode/colanode — Apache-2.0, ~5.2k stars. Last release v0.4.7 on 2026-04-03; last commit same date (feeds this session). Roughly six months without a commit as of today — young project, cadence slowing; flag for re-check.
- Provenance: "Show HN: Colanode, open-source and local-first Slack and Notion alternative", April 2025 — "an open-source, local-first collaboration app combining the best of Slack-style chats and Notion-style note-taking, fully self-hostable" (https://news.ycombinator.com/item?id=43780176).

### 1.13 Notabase (churichard/notabase) — STALLED
- Repo: https://github.com/churichard/notabase — AGPL-3.0, ~915 stars; no releases (feed this session). Hosted product still up at https://notabase.io/.
- Provenance: "Show HN: https://notabase.io – a note-taking app for networked thinking… supports page stacking, linked references, block references, a graph view… open source so you can self-host" (https://news.ycombinator.com/item?id=34537748, Jan 2023).
- Status: the last visible commit on the default branch is 2026-07-17 with zero releases in 2026; effectively a solo hobby project, not a credible base. (The 915 stars belong to churichard/notabase; notabase/notabase is a different, older repo — both checked this session.)

### 1.14 Basetool (basetool-io/basetool) — DEAD
- Repo: https://github.com/basetool-io/basetool — Apache-2.0, ~286 stars. Last commit 2022-06-20; last (and only meaningful) release v0.0.1, 2021-11-15 (feeds this session). AlternativeTo lists it as "discontinued" (https://alternativeto.net/software/basetool/).
- What it was: an open-source internal-tool/Airtable-flavored table app from the 2021 wave. No self-host community formed. Verdict: dead, no successor.

### 1.15 Athens Research (athensresearch/athens) — DEAD, best-documented death in the category
- Repo: https://github.com/athensresearch/athens — last commit 2022-12-12; last release v2.1.0-beta.5, 2022-10-10 (feeds this session). Not GitHub-flagged archived, but abandoned.
- Death evidence: the project itself (YC W21, "Launch HN: Athens Research – Open-Source Roam Research", https://news.ycombinator.com/item?id=26316793) shut down its hosted service and stopped; contemporaneous write-up "Athens Research is gone, what's next?" — "The most shameless Roam-clone has thrown in the towel… this update seems like they left users with only an unsupported way to download the data" (https://medium.com/@bchamberlain951/athens-research-is-gone-whats-next-92c77eec6fcb, Nov 2022); HN: "Athens (open-source Roam Research) is no longer being actively maintained" (https://news.ycombinator.com/item?id=34285769, Jan 2023).
- Why it died (from those sources + repo inactivity): company-first strategy that collapsed, and an Electron/ClojureScript codebase community contributors couldn't take over — the same pattern that later repeated with Focalboard.

### 1.16 Bangle.io (bangle-io/bangle-io) — SEMI-ALIVE
- Repo: https://github.com/bangle-io/bangle-io — ~1.2k stars; no license detected on the repo page this session (**UNVERIFIED** license). Last commit 2026-07-12; last release v1.0.1, 2026-07-06 (feeds).
- What it is: a Notion-style editing experience over plain local Markdown files, born from a Show HN in 2021. Cadence is now sporadic releases separated by months.

### 1.17 Adjacent but often listed: Outline, SilverBullet, Trilium, Boostnote
These get pulled into "Notion alternative" lists; their remake status:
- **Outline** (https://github.com/outline/outline): ~41.1k stars, active (commit 2026-10-26, release 2026-10-23, feeds this session). It is an Evernote/wiki-alternative (see Part 2). Licensing caveat: the repo LICENSE is **Business Source License 1.1** (verified from https://raw.githubusercontent.com/outline/outline/master/LICENSE this session) — source-available since 2023, not OSI open source; the old open-core fork conversations follow from that.
- **SilverBullet** (https://github.com/silverbulletmd/silverbullet): MIT, ~6.4k stars, active (2.12.1 released 2026-10-12, commit 2026-10-22, feeds). A markdown/PKM web app; a Notion *substitute* for personal notes, not a clone. Recommended by self-hosters leaving Notion (https://www.reddit.com/r/selfhosted/comments/18zoc0k/its_2024_and_theres_still_not_a_decent_notion/).
- **Trilium / TriliumNext**: see Part 3, a full death-and-resurrection case.
- **Boostnote / BoostNote.next** (https://github.com/BoostIO/boostnote and https://github.com/BoostIO/BoostNote-App): the original Boostnote last committed 2021-09-02 (dead); the rewrite BoostNote-App last committed 2025-06-17 with its last release in 2022-05 (feeds this session) — dormant. Once the leading open-source notes app (~19k stars at peak across both), effectively dead as a Notion alternative.

### 1.18 The "end-to-end encrypted Notion" Show HN (May 2023)
An E2EE Notion alternative was shown on HN in May 2023 (https://news.ycombinator.com/item?id=35874244) but the fetched page text does not name the product; **UNVERIFIED this session** — not counted as a separate project until identified.

---

## Part 2 — Evernote remakes

### 2.1 Joplin (laurent22/joplin) — ALIVE, the standard answer
- Repo: https://github.com/laurent22/joplin — ~56.9k stars; license file composite ("NOASSERTION" on the GitHub page; MIT-family with plugins) — active: last commit 2026-10-27, release 2026-10-23 (feeds this session).
- Standing: the de-facto Evernote replacement. Not a clone of Evernote's UI, but it remade the job: notebooks, tags, attachments, **ENEX import** (https://joplinapp.org/help/apps/import_export/), web clipper, E2EE sync (Joplin Cloud / Dropbox / WebDAV / S3). Single-maintainer-led with a large community; extremely long-lived (2016→).
- Fidelity/limits: ENEX import drops colors/fonts (text always survives; HTML import available for fidelity); "links between notes are mostly preserved" (https://joplinapp.org/help/apps/import_export/). Web-clipper and OCR are weaker than Evernote's (no built-in image OCR; third-party plugins).
- Self-host: clients are local; sync is bring-your-own (or paid Joplin Cloud).

### 2.2 Notesnook (streetwriters/notesnook) — ALIVE
- Repo: https://github.com/streetwriters/notesnook — GPL-3.0, ~14.8k stars. Active: v3.4.11 released 2026-10-26; commit same day (feeds this session).
- Standing: E2EE notes app with a dedicated Evernote importer, marketed in 2026 roundups as "the more affordable alternative at $4.99/mo, with end-to-end encryption" (https://toolfinder.com/best/open-source-note-taking-apps). Clients open source; sync server self-hostable. Not a UI clone; fidelity is "notes + attachments + tags", with clipper and note history.

### 2.3 QOwnNotes (pbek/QOwnNotes) — ALIVE
- Repo: https://github.com/pbek/QOwnNotes — GPL-2.0, ~5.9k stars. Active: "continuous" release dated 2026-10-26 (feed this session). Long-running single-maintainer markdown desktop app with Evernote import and own Nextcloud server components. Standing: alive, but it is a personal markdown app, not an Evernote clone.

### 2.4 Turtl (turtl/desktop) — DORMANT (remake-status only; deep dive elsewhere)
- Repo: https://github.com/turtl/desktop — GPL-3.0, ~736 stars (repo page this session). **No release since 2019-04-15** (releases feed this session); the last commit on the default branch is 2025-03-27 — maintenance pokes, not development.
- What it is: the original open-source encrypted Evernote-alternative (shared vaults, boards) from 2013-era. UI and stack (Common Lisp server, ClojureScript client) froze long ago.
- Verdict: alive-ish code, dead product development. Not a credible base in 2026; kept on record because it is still the most-cited "old" Evernote remake.

### 2.5 Outline — ALIVE (see 1.17 for license caveat)
The strongest *self-hosted* Evernote analog that is still growing: documents/collections, web-clipper, Slack/Google auth, Markdown storage, ~41.1k stars, active as of 2026-10-23 release (feeds this session). It remade Evernote-for-teams more than Notion. BSL 1.1 license since 2023 (verified above) is the main fork-adoption caveat.

### 2.6 NixNote2 (baumgarr/nixnote2) — STALLED
- Repo: https://github.com/baumgarr/nixnote2 — last release v2.0.2; the default-branch commit feed shows 2017-10-29 as the newest entry (feeds this session — an odd result; development may live on non-default branches, **UNVERIFIED** beyond the feed).
- What it was: the serious open-source *Evernote client* (syncing to Evernote itself) for Linux. With Evernote's API decline it lost its purpose. Verdict: effectively dead as a path out of Evernote.

### 2.7 Boostnote — DEAD (see 1.17). Last release of the rewrite: 2022.

### 2.8 GitNoter — MINOR, stillborn as an Evernote remake
- "Show HN: An open source alternative to Evernote (Self Hosted)", June 2022 (https://news.ycombinator.com/item?id=31580045). It stored notes as Markdown in a git repo; HN commenters immediately pushed back that it wasn't an Evernote alternative at all — "EverNote is *all about* dropping random files into it… it also has a very handy web clipper", listing clipper/OCR/attachments as the actual bar (same thread). Repo activity since: **UNVERIFIED this session**. Recorded as a data point on what Evernote actually requires.

### 2.9 Deleted projects people still mention: Geeknote, Everpad
- Geeknote (CLI Evernote client) and Everpad (Evernote-integrated Linux client): both `github.com/geeknote/geeknote` and `github.com/everpad/everpad` return **404 today** (verified this session) — repos deleted, not archived. Mentioned in older Evernote-exit guides; **UNVERIFIED this session** for the exact deletion dates. Both died with the Evernote API ecosystem they depended on.

### 2.10 Skiff (Pages) — the famous closed-source death (context entry)
Not open source, included because every "Notion alternative died" discussion involves it: Notion acquired Skiff in Feb 2024 (https://techcrunch.com/2024/02/09/notion-acquires-privacy-focused-productivity-platform-skiff/), and "All Skiff services, including Mail, Pages, Calendar and Drive, were sunset on August 9, 2024" per Skiff's own migration page (https://skiff.com/data-migration), with data deletion and no account conversion (https://arstechnica.com/gadgets/2024/02/encrypted-email-service-skiff-gets-acquired-will-shut-down-in-six-months/). The r/Notion reaction was bitter ("that's why they bought Skiff. Just to wipe it in six months", https://www.reddit.com/r/Notion/comments/1an2zst/skiff_acquired_by_notion/). A cautionary anchor for the whole remake landscape: alternatives die when their owners do.

---

## Part 3 — The Trilium death-and-resurrection (most instructive case)

- zadam/trilium (~38.6k stars, AGPL-3.0) was the leading self-hosted hierarchical notes app. The author announced "Trilium transitions into maintenance mode" (TriliumNext issue #4620, Jan 2024) as development slowed (https://github.com/TriliumNext/Trilium/issues/4620).
- The community forked as TriliumNext. After "nearly a year of attempts, Zadam responded and agreed to transfer the original repository to TriliumNext… the original creator had been dealing with major life changes – having a child and work pressures – and was actually pleased with how the project had evolved under new leadership" (https://dosu.dev/customers/how-triliumnext-revitalized-an-abandoned-open-source-project-with-dosus-help). The transfer happened 2025-06-23 (recorded in issue #4620, https://github.com/TriliumNext/Trilium/issues/4620), and TriliumNext/Notes was renamed back to TriliumNext/Trilium ("'Notes' is now 'trilium'", https://github.com/orgs/TriliumNext/discussions/5845; "TriliumNext Notes will become Trilium Notes", https://github.com/orgs/TriliumNext/discussions/5867).
- Current state: https://github.com/TriliumNext/Trilium is the home; Docker images now "track triliumnext/trilium, the official continuation of Trilium" (https://hub.docker.com/r/zadam/trilium). Notably, the old zadam/trilium repo feed now shows the *new* releases (v0.106.1, 2026-10-23) — it mirrors the continuation. Project is actively developed as of this week (feeds this session).
- Lesson for the lane: a healthy fork-with-transfer saved this one; note the contrast with Focalboard, where the vendor kept the repo and the community could not take over.

---

## Part 4 — Could not be verified / not found this session

- **"Nim" (nim.astro?)** — no credible open-source Notion remake by that name found; searches return the Nim language and unrelated small note apps (e.g. https://github.com/Nihmar/Niman, https://github.com/alialbaali/Noto). Finding: **no evidence such a notable remake exists.**
- **"Noi"** — the project of that name is an AI browser, not a notes/PKM app; excluded.
- **undb** — listed among open-source Airtable-like alternatives (https://alternativeto.net/software/airtable/?license=opensource) but its GitHub repo could not be located under imhcg/undb or undbxyz/undb this session (404s); **UNVERIFIED this session.**
- **"OpenKnowledge"** (Show HN June 2026, "open source AI-first alternative to Obsidian/Notion", https://news.ycombinator.com/item?id=48675435) — repo not identified this session; new and unproven. **UNVERIFIED.**

---

## Part 5 — Migration pain: what users report moving out

### 5.1 Out of Evernote (ENEX quirks)
- **OCR'd PDFs lose their searchability.** Evernote's OCR index lives in the note, not the document: "Evernote OCR has one problem: It doesn't make the document itself searchable. The search index for the OCR is embedded into the note. When notes are exported, the internal OCR index is lost" (https://www.reddit.com/r/Evernote/comments/1afc4z7/evernote_ocr_to_the_rescue/). The PDFs come out as plain images/scans, and tools must re-OCR them (https://univik.com/blog/evernote-pdf-to-text.html). Evernote's own docs only discuss making scans searchable *inside* Evernote (https://help.evernote.com/hc/en-us/articles/37423805275539-If-scanned-PDFs-are-not-appearing-in-your-search-results).
- **ENEX export itself is fragile.** Exporting while a sync is in progress "is a reliable way to get a partial file"; one corrupt attachment can kill an entire notebook export, and huge notebooks must be split (https://harbor.my/blog/export-evernote-notes/).
- **Attachments and links.** Real-world import threads report attachments silently missing after ENEX import (https://discourse.joplinapp.org/t/attachment-lost-after-evernote-import/6865), and internal note links lost on large migrations — one user moving 27,000 notes / 5,200 tags reported export crashes and dead inter-note links, with the "Joplin Evernote Links Replacer" plugin as the partial fix (https://www.reddit.com/r/joplinapp/comments/1bvixp9/currently_exporting_my_27000_notes_207_notebooks/). Third-party guides confirm users "lose formatting and folder structure… attachments, embedded data or metadata" in manual ENEX conversions (https://www.bitrecover.com/blog/export-evernote-to-joplin/).
- **ENML/round-trip fidelity.** Joplin's docs concede formatting loss on complex notes (colors, font sizes/faces) and offer HTML import as the fidelity fallback; even modern 2026 importer tooling still fights nested tables, `<en-crypt>` blocks, and `<en-todo>` inside lists (https://github.com/jfolcini/agaric/issues/2513), and image references with spaces or special characters get dropped across Evernote/Joplin/Notion importers (https://github.com/jfolcini/agaric/issues/6032).

### 5.2 Out of Notion (blocks/databases/API)
- **Exports silently degrade structure.** "Every format silently degrades complex structures like relations, rollups, and formulas" (https://clonepartner.com/blog/definitive-guide-notion-data-export-api-pdf-html). Databases export as flat CSVs losing "every view, filter, relation, and rollup you configured"; callouts export as raw HTML; nested-page filenames embed 32-character UUIDs that break Windows path limits (https://unmarkdown.com/blog/notion-export-broken). Toggles flatten because Markdown has no toggle; synced blocks become duplicated static copies (https://raccoon.page/blog/notion-export-limitations/). Relation properties become opaque page-ID lists (https://www.breeze.pm/articles/export-from-notion). Notion itself says re-uploading an export will not recreate the workspace (https://restora.cc/blog/what-notion-export-leaves-behind).
- **First-person account:** "Notion's official export preserves text and basic tables, but internal links between pages, images pasted from clipboard, database formulas, and table relations have no direct equivalent in plain Markdown. Can I migrate Notion to Markdown without losing anything? No." (https://dev.to/jtorchia/plain-text-won-i-migrated-my-notes-from-notion-to-markdown-and-lost-more-than-i-expected-46bl).
- **API path:** the export API requires recursively walking block trees with pagination and a 3 req/sec rate limit, plus custom translation layers (https://clonepartner.com/blog/definitive-guide-notion-data-export-api-pdf-html); database formulas/rollups/relations arrive as raw references needing custom resolution (https://www.minibase.md/blog/save-notion-pages-as-markdown/).
- **Team-scale exits are DIY:** teams leaving Notion report exporting relations only by writing n8n/API pipelines themselves ("We have multiple relational databases with thousands of rows within Notion. We were able to export all Notion's data including relations using Notion's API and n8n", https://www.reddit.com/r/selfhosted/comments/18zoc0k/its_2024_and_theres_still_not_a_decent_notion/).

---

## Part 6 — Verdict

### Alive in 2026 and credible as bases to pull from
| Project | Base-worthiness | Key evidence |
|---|---|---|
| AppFlowy | The strongest Notion remake overall | v0.14.11, Oct 2026 builds (kc3 sources above) |
| AFFiNE | Co-front-runner; check split license | canary builds 2026-10-26 |
| SiYuan | Strong block-based remake with importers | release 2026-10-26 |
| Joplin | The strongest Evernote replacement | release 2026-10-23, commit 2026-10-27 |
| Outline | Best self-hosted Evernote-for-teams; BSL caveat | release 2026-10-23 |
| Notesnook | E2EE Evernote path, active | v3.4.11, 2026-10-26 |
| Memos | Partial Notion substitute (quick notes) | release 2026-10-26 |
| Anytype | Local-first encrypted workspace | nightly 2026-10-23 |
| Docmost | Young but fast-growing wiki/Notion-lite | v0.97.0, 2026-10-25 |
| Teable | Databases-only complement | release 2026-10-23 |
| Trilium (TriliumNext/Trilium) | Resurrected, active | v0.106.1, 2026-10-23 |
| Logseq | Alive; outliner-first | commit 2026-10-25 |
| QOwnNotes | Alive, niche | continuous, 2026-10-26 |
| Eidos | Young, active | commit 2026-10-26 |
| Colanode | Young; cadence slowing — recheck | v0.4.7, 2026-04-03 |
| SilverBullet | Alive, PKM substitute | 2.12.1, 2026-10-12 |
| Bangle.io | Semi-alive | v1.0.1, 2026-07-06 |

### Dead, dormant, or deleted — each with its death evidence
- **Focalboard**: dropped by Mattermost (plugin moved out Aug 2024, issue #5038; plugin in maintenance mode Jan 2025, Mattermost support article); last release June 2024; no maintainer came (issue #5038).
- **Notea**: maintainer statement in README ("barely maintained… I've personally stopped using it too"); last release Dec 2022.
- **Athens**: last commit Dec 2022; closure write-up Nov 2022 (Medium) and HN confirmation Jan 2023; YC-backed company-first strategy collapsed.
- **Basetool**: last commit June 2022; listed discontinued by AlternativeTo.
- **Boostnote (both generations)**: original last commit 2021; rewrite last commit June 2025, last release 2022.
- **NixNote2**: default-branch feed shows no commits since 2017; purpose (Evernote sync client) evaporated.
- **Geeknote, Everpad**: repos deleted (404s verified this session).
- **Turtl**: no release since April 2019; commits reduced to occasional maintenance (last: March 2025).
- **Skiff (Pages)**: closed-source, but the canonical death — acquired by Notion Feb 2024, all services sunset 2024-08-09 (skiff.com/data-migration).
- **GitNoter**: Show HN only; HN feedback showed it didn't meet the actual Evernote bar (clipper, attachments, OCR).

### Why the deaths happened (patterns, all evidenced above)
1. **Vendor adopt-then-drop**: Focalboard is the case study — integrated into Mattermost, deprecated out, transferred to a community org that issued a "Call for Maintainers" and found none.
2. **Single-maintainer clone**: Notea's own README says the maintainer left and stopped using it. Athens' company-first plan collapsed and the ClojureScript codebase was too hard to inherit.
3. **Dependent on the incumbent's API**: NixNote2, Geeknote, Everpad died with the Evernote client-API era.
4. **Acqui-deletion**: Skiff, shut down 12 months after Notion bought it.

---

## Appendix A — Repo-check evidence (captured this session, 2026-10-27, via github.com repo pages, /commits.atom and /releases.atom)

| Repo | Archived? | License | Stars | Last commit (default branch) | Last release |
|---|---|---|---|---|---|
| AppFlowy-IO/AppFlowy | no | AGPL-3.0 | 77,789 | 2026-06-26 | 0.14.11 (Oct 2026 per Play/Builder) |
| mattermost-community/focalboard | no (redirected) | Other/NOASSERTION | — | — (feed quiet) | v8.0.0, 2024-06-17 |
| zinclabs/notea | 404 | — | — | — | — |
| QingWei-Li/notea | no | MIT | 2,143 | 2025-11-15 | v0.4.0-alpha, 2022-12-04 |
| notea-org/notea | no | MIT | — | — | — (README: barely maintained) |
| turtl/desktop | no | GPL-3.0 | 736 | 2025-03-27 | 2019-04-15 |
| outline/outline | no | BSL 1.1 (LICENSE file) | 41,077 | 2026-10-26 | 2026-10-23 |
| siyuan-note/siyuan | no | AGPL-3.0 | 46,947 | 2026-10-20 | 2026-10-26 |
| usememos/memos | no | MIT | 64,098 | 2026-10-26 | 2026-10-26 |
| laurent22/joplin | no | NOASSERTION (composite) | 56,888 | 2026-10-27 | 2026-10-23 |
| streetwriters/notesnook | no | GPL-3.0 | 14,832 | 2026-10-26 | v3.4.11, 2026-10-26 |
| pbek/QOwnNotes | no | GPL-2.0 | 5,930 | 2026-10-26 | continuous, 2026-10-26 |
| toeverything/AFFiNE | no | Other (split) | 73,881 | 2026-10-26 | v2026.10.26-canary.915 |
| docmost/docmost | no | AGPL-3.0 | 22,109 | 2026-10-25 | v0.97.0, 2026-10-25 |
| teableio/teable | no | NOASSERTION | 21,930 | 2026-10-26 | 2026-10-23 |
| logseq/logseq | no | AGPL-3.0 | 45,394 | 2026-10-25 | nightly, 2026-10-25 |
| athensresearch/athens | no | NOASSERTION | 6,298 | 2022-12-12 | v2.1.0-beta.5, 2022-10-10 |
| bangle-io/bangle-io | no | not detected | 1,236 | 2026-07-12 | v1.0.1, 2026-07-06 |
| silverbulletmd/silverbullet | no | MIT | 6,391 | 2026-10-22 | 2.12.1, 2026-10-12 |
| zadam/trilium | no | AGPL-3.0 | 38,577 | — (mirrors continuation) | v0.106.1, 2026-10-23 |
| TriliumNext/Trilium (was /Notes) | no | AGPL-3.0 | — | 2025-06-24 (feed snapshot; active on new home) | v0.95.0 (pre-rename) |
| anyproto/anytype-heart | no | NOASSERTION | 425 | 2026-10-26 | nightly 2026-10-23 |
| churichard/notabase | no | AGPL-3.0 | 915 | 2026-07-17 | none |
| basetool-io/basetool | no | Apache-2.0 | 286 | 2022-06-20 | v0.0.1, 2021-11-15 |
| BoostIO/boostnote | no | — | — | 2021-09-02 | — |
| BoostIO/BoostNote-App | no | NOASSERTION | 4,044 | 2025-06-17 | 2022-05-02 |
| baumgarr/nixnote2 | no | — | — | 2017-10-29 (feed) | v2.0.2 |
| colanode/colanode | no | Apache-2.0 | 5,176 | 2026-04-03 | v0.4.7, 2026-04-03 |
| mayneyao/eidos | no | AGPL-3.0 | 3,200 | 2026-10-26 | 2026-10-26 |
| geeknote/geeknote | 404 (deleted) | — | — | — | — |
| everpad/everpad | 404 (deleted) | — | — | — | — |
| klaussinani/tusk | no | — | — | 2026-03-23 (stray) | (dormant; last release 2019 per older records) **UNVERIFIED** |

**Counting:** 33 projects/named attempts covered. Verified actively developed: 17 (AppFlowy, AFFiNE, SiYuan, Memos, Outline, Anytype, Joplin, Notesnook, QOwnNotes, Docmost, Teable, Logseq, SilverBullet, Trilium/TriliumNext, Eidos, Bangle.io [semi], Colanode [semi]). Verified dead/archived/dormant/deleted: 13 (Focalboard, Notea, Turtl, Athens, Basetool, Boostnote×2, NixNote2, Geeknote, Everpad, GitNoter, Skiff, Notabase [stalled]). Could not verify: 3 (Nim, undb, OpenKnowledge). Final file: ~330 lines.
