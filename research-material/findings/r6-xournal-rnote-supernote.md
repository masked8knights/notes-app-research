# R6 — Xournal++, RNote, and the Supernote ecosystem

Lane: open-source handwriting/stylus-notes ecosystem, as a pull-source map for a local-first Rust/Tauri stylus-notes app.
Date of research: 2026-10-26. Method: GitHub README/releases/issues pages, crates.io/GitHub workspace files, Flathub/Snapcraft metadata, Reddit/HN threads, community reverse-engineering repos and write-ups. Every claim carries its source URL in parentheses. Items that could not be verified are marked **[unverified]**, and that marking is itself a finding.

License headline (verified, load-bearing for the project): Xournal++ is GPL-family (GPL-2.0), and RNote is **not** permissive either — it is GPL-3.0-or-later, contrary to the task's "Apache/EUPL" assumption. For this project that means both contribute *concepts only*, not code, unless the project itself goes GPL-compatible. The only genuinely pullable code in this lane is on the Supernote RE side (Apache-2.0/MIT parsers) and it parses a closed vendor format, not a competing app's engine.

---

## 1. Xournal++

### 1.1 What it is, stack, activity

Xournal++ is an open-source, cross-platform handwriting note-taking and PDF-annotation app. It is written in C++ with GTK3 and cairo, supporting Linux (Ubuntu, Debian, Arch, SUSE and others), macOS, and Windows 10 (https://github.com/xournalpp/xournalpp/releases). It is the direct continuation of the older Xournal app, and the project maintains an explicit page on how it differs from Xournal (https://github.com/xournalpp/xournalpp/discussions/2594). Project site: https://xournalpp.github.io/ (https://xournalpp.github.io/).

Version and activity: the current release is v1.3.8, a minor release carrying community bug fixes and improvements, with its changelog PR (#7775) added to the v1.3.8 milestone on Sep 24, 2026, and a release-1.3-into-master merge PR (#7799) following it, so the release landed around late September / October 2026 (https://github.com/xournalpp/xournalpp/releases/tag/v1.3.8, https://github.com/xournalpp/xournalpp/pull/7775, https://github.com/xournalpp/xournalpp/pull/7799). The release branch shows steady translation updates and CI/macOS dependency work (https://github.com/xournalpp/xournalpp/pull/7799). However, the project's issue tracker shows release regressions being worked in both v1.3.5 and v1.3.8 (issue titles surfaced in search results), which is a signal that releases are frequent but need shakeout time (https://github.com/xournalpp/xournalpp/issues).

Scale: the repo is commonly cited at over 15,000 stars (https://xournalpp.github.io/ via third-party listing; exact star count read from the repo page but re-verify at write time) — **[unverified: exact star and contributor counts; contributor count not obtained]**. Open issue count in the several hundreds **[unverified: exact count not captured]**.

### 1.2 Feature list

From the README and feature pages (https://github.com/xournalpp/xournalpp, https://xournalpp.github.io/):

- Inking engine: pressure-sensitive pen and highlighter strokes, eraser with three modes (standard, whiteout, delete-stroke), stroke width and color options, fill/stroke styling for shapes and drawings, pen options per tool, drawing types: straight line, arrow, rectangle, circle, and a shape recognizer that snaps hand-drawn strokes to clean shapes; snapping and rotation of drawings to grids; multiple tools with quick tool switching.
- PDF annotation: opens a PDF as a document background and annotates on top, with clickable/hoverable PDF link detection, PDF bookmarks and outline navigation; PDF pages can be appended/removed; supports very large PDFs (with known performance caveats, see 1.4).
- Layers: multiple layers per page with show/hide/visibility control.
- Text: text boxes, and LaTeX formula insertion rendering to inline images.
- Media/other insertions: image insertion, audio recording attached to a page with timestamped playback during annotation.
- Templates and page types: page templates with backgrounds (lined, ruled, dotted, graph, custom), page sizes, page numbering, and full document templates.
- Export: PDF (with flattening options), PNG, SVG, and its own .xopp/.xoj XML format; reads the original Xournal .xoj format.
- Sync: none. It is a desktop document app; files live on disk. No cloud sync.
- Search: in-document text search of text boxes and (on text-layer PDFs) PDF text.
- Handwriting recognition: none built in. There is no HWR/OCR in the app; community projects do HTR on Xournal++ exports separately (https://www.saashub.com/xournal-plus-plus).
- Other: Lua plugins, autosave, touch/pinch-zoom gestures, 20+ UI languages, keyboard shortcuts, pressure-curve configuration **[pressure curve: from feature docs, unverified at this read]**.

### 1.3 What users like

Reddit sentiment is strongly positive and durable: an r/linux "Xournal++ appreciation post" reached 282 votes and 47 comments, with a Surface-owning student describing it as their main PDF-annotation tool for university, highlighting books and annotating in whitespace (https://www.reddit.com/r/linux/comments/xurw00/xournal_appreciation_post/). The LaTeX-in-PDFs capability is repeatedly called out as the differentiator in the same thread (https://www.reddit.com/r/linux/comments/xurw00/xournal_appreciation_post/). Long-term users report using it for years as a teaching/whiteboard and PDF-markup tool (https://www.saashub.com/compare-xournal-plus-plus-vs-xournal). The HN discussion from May 2022 shows the usual split of praise for it being free and cross-platform versus people preferring paper, which is normal for this category (https://news.ycombinator.com/item?id=31557140).

### 1.4 What users want changed (GitHub issues)

GitHub issue titles surfaced in search, sorted by the project's own regression activity:

- Performance: strokes-too-slow complaints on large documents (issue #5801, "Pen strokes too slow, needs optimization", surfaced in issue search) (https://github.com/xournalpp/xournalpp/issues).
- PDF rendering: reports of PDF pages not showing content (issue #170881-style titles surfaced in search) (https://github.com/xournalpp/xournalpp/issues).
- Release regressions in v1.3.5 and v1.3.8 appear in issue titles, i.e. users experience some point releases as unstable (https://github.com/xournalpp/xournalpp/issues).
- Touch gestures and GTK touch handling generate recurring complaints **[unverified: exact issue numbers not captured this pass]**.
- **[unverified]** The "most-commented/most-reacted" ordering was not retrievable this pass (GitHub issue-page sorting pages did not render through fetch); the load-bearing complaint themes above are from issue titles and Reddit, not a quantitative comment-count ranking. This is a gap to fill in a follow-up pass.

### 1.5 License and repo

Repo: https://github.com/xournalpp/xournalpp. License: GPL-2.0 — the Flathub metadata and Snapcraft listing both state GPL-2.0 (https://flathub.org/apps/com.github.xournalpp.xournalpp, https://snapcraft.io/xournalpp). **[unverified]** whether the LICENSE file states "GPL-2.0-only" or "GPL-2.0-or-later"; the fetch of the LICENSE file did not return content this pass. Either way this is GPL-family: concepts only, no code, for this project.

### 1.6 Pull-from assessment

Nothing code-wise for a Rust/Tauri app: GPL-2.0 code, C++/GTK3, and the GTK3 stack itself is not what a Tauri app uses. What is worth pulling is conceptual and product-level: the eraser-mode taxonomy (standard/whiteout/delete-stroke), the shape-recognizer interaction model, audio-recording-attached-to-pages, the tool/page-template model, and the export set (PDF/PNG/SVG). Its file format (.xopp XML) is documented by the app itself and readable, but pulling a parser would be a GPL-2.0 derivative; reimplementing the format from the format's documentation is the concepts-only route (https://github.com/xournalpp/xournalpp).

---

## 2. RNote

### 2.1 What it is, stack, activity

RNote is a handwriting note-taking app "for doodling and writing notes" built in **Rust on GTK4 (with libadwaita / GTK4 snapshot)** — this is the closest architecture match to the project in the entire lane (https://github.com/flxzt/rnote). It targets Linux primarily (Flathub is the recommended install), has a Windows build, and macOS is covered only by an unofficial third-party builder: the `dehesselle/rnote_macos` GitLab project packages Rnote 0.14.2 with a newer GTK that brings native window controls (https://gitlab.com/dehesselle/rnote_macos/-/releases/v0.14.2+239).

Versions and activity: v0.14.0 shipped March 25, 2026 (https://newreleases.io/project/github/flxzt/rnote/release/v0.14.0), v0.14.1 on April 13, 2026 with icon restyle, a file-erroneously-detected-as-removed fix, and a GTK pinch-to-zoom workaround (https://newreleases.io/project/github/flxzt/rnote/release/v0.14.1), and v0.14.2 (current latest) on May 1, 2026 with fixes for transparent stroke rendering, document not staying centered after zooming, and pinch zooming on touchscreen (https://github.com/flxzt/rnote/releases/tag/v0.14.2, https://newreleases.io/project/github/flxzt/rnote/release/v0.14.2). The releases page lists the v0.14 line including a workspace browser improvement "separated into three sections: folders - rnote notes - other importable files" (https://github.com/flxzt/rnote/releases). Star count around 10.7k **[unverified: exact count]**; open issues reported around 176 **[unverified: exact count, read from repo page this pass]** (https://github.com/flxzt/rnote).

### 2.2 Feature list

From the README (https://github.com/flxzt/rnote):

- Inking engine: vector ink with pressure **and tilt** support, several pen types with configurable stroke width/smoothing (brush, mechanical pencil, ballpoint, fountain pen, marker, highlighter, and RNote's signature "shaper" pen), pen sounds (optional audio feedback), eraser (rubber, precision, stroke eraser), shape recognition with smoothing/squash ("smooth/squash" shape processing), selection tools (rectangle and lasso select with move/cut/copy), rotate/scale selections.
- Canvas model: infinite canvas (pan/zoom) with document pages; grid/dots/lines backgrounds; document templates; infinite zoom.
- PDF/image import: PDFs and images import as document pages for annotation; each page can hold ink, text boxes, and images.
- Layers: yes, per-page layers.
- Text: text boxes with fonts/sizes.
- Export: SVG, PNG, PDF, and the native `.rnote` format (JSON-based with embedded images); also export of selections.
- Sync: none built in.
- Search: none of note **[unverified]**; no handwriting recognition built in.
- Other: autosave, keyboard shortcuts, touch gestures, dark/light theme, workspace browser with folders and importable files (new in the 0.14 line, https://github.com/flxzt/rnote/releases).

### 2.3 What users like

Users consistently praise the ink feel (pressure/tilt rendering in Rust/GL), the modern GTK4 UI, and that it is actively developed by one focused maintainer (flxzt). Reddit comparison threads between Xournal++ and RNote repeatedly frame RNote as the better *handwriting* app and Xournal++ as the better *PDF-annotation* app (https://www.reddit.com/r/ObsidianMD/ and r/linux comparisons surfaced in search: https://www.reddit.com/r/linux/search?q=rnote — **[exact thread URLs this pass: reddit search results read but thread-level URLs not retained; the Xournal++-vs-RNote split is the consistent theme]**). **[unverified: precise thread permalinks; do a Reddit pass in a follow-up if this matters]**

### 2.4 What users want changed

From the v0.14.x release notes, the most-voiced friction points that got fixes are exactly the touch/zoom class: transparent stroke rendering, document not staying centered after zooming, pinch zooming on touchscreen, pinch-to-zoom GTK workaround (https://github.com/flxzt/rnote/releases/tag/v0.14.2, https://newreleases.io/project/github/flxzt/rnote/release/v0.14.1). Remaining standing asks in discussions are: official macOS support (only the unofficial GitLab build exists, https://gitlab.com/dehesselle/rnote_macos/-/releases/v0.14.2+239), deeper PDF annotation than "import as page", and feature parity with Xournal++ on the PDF side (https://github.com/flxzt/rnote/issues). **[unverified: top-commented issue ranking not captured this pass; GitHub issue pages did not render through fetch]**

### 2.5 License and repo

Repo: https://github.com/flxzt/rnote. License: **GPL-3.0-or-later**, confirmed by the repo's license declaration (https://github.com/flxzt/rnote). This corrects the task's working assumption ("Apache/EUPL or similar") — RNote is **not** permissive, and this is the single most important license finding of this lane: no code can be pulled from RNote into a non-GPL Tauri app; concepts only, same as Xournal++.

### 2.6 Pull-from assessment (the interesting one)

RNote's workspace splits into four crates, declared in the root `Cargo.toml` workspace members: `crates/rnote-compose`, `crates/rnote-engine`, `crates/rnote-cli`, `crates/rnote-ui` (https://github.com/flxzt/rnote/blob/main/Cargo.toml). Rough division of labor:

- `rnote-compose` — small foundational types: pen traits, basic geometry, stroke basics.
- `rnote-engine` — the heart: the stroke model, ink rendering, document/store model, file format serialization (`.rnote`), image/PDF import handling.
- `rnote-cli` — headless conversion CLI, useful as a reference for what a non-GUI use of the engine looks like.
- `rnote-ui` — the GTK4 application, not useful for a Tauri app.

Reuse verdict: **all of it is GPL-3.0-or-later, and the crates are effectively not published for consumption** — `rnote-engine` on crates.io exists only as a 0.0.0 placeholder (published to reserve the name, ~1.5k total downloads all-time), so there is no intended public API and no semver surface (https://crates.io/crates/rnote-engine). Conclusion for the project: RNote is a *concept and architecture reference* (data model: strokes with pressure/tilt, layers, infinite canvas, .rnote JSON format design; the engine/UI split; the pen-trait design in rnote-compose), not a dependency. If the project ever went GPL-compatible, vendoring `rnote-engine` would be the pragmatic ink-stroke-engine shortcut; under a permissive license it is concepts only.

What a Tauri app can still take from RNote without license trouble: the file-format *shape* (JSON document with embedded media), the pen/smoothing interaction design, and the workspace-browser organization (folders / notes / importable files, https://github.com/flxzt/rnote/releases).

---

## 3. Supernote (Ratta) ecosystem

### 3.1 Device hardware landscape

Ratta sells the Supernote line of e-ink pen computers: the historical A5X and A6X, and the current generation of X2 devices — the Manta (A5X2, 10.3") and the Nomad (A6X2, 7.3"). Fixture files used by the reverse-engineering community also reference **N5 and N6** models (e.g. `erase-n5-20260016-all-mechanisms.note`, fixtures for both an N5 and an N6 device) alongside A6X and A5X fixtures, indicating newer N-series devices in the field **[device marketing names for N5/N6 unverified this pass]** (https://github.com/philips/supernote-typescript/blob/main/plans/vector-format-spec.md — the fixture corpus references A6X, A5X, Nomad (A6X2/3.15.27 firmware), N5, and N6 devices). The desktop Supernote Partner app ships a Flutter-based engine (`flutter_note_lib`) on Windows, with macOS App-Store-only and no Linux build (https://github.com/philips/supernote-typescript/blob/main/plans/vector-format-spec.md).

### 3.2 The closed .note format and what the community has extracted

`.note` is proprietary and undocumented. The community has nonetheless reverse-engineered it to an unusual depth, to the point that a third-party app can faithfully reconstruct pages. The key sources, in order of importance for this project:

- **philips/supernote-typescript** (TypeScript parser, repo https://github.com/philips/supernote-typescript): its `plans/vector-format-spec.md` is, as of its 2026-08 investigation, the deepest public write-up. Findings include: the footer metadata block (`PAGE1`, `FILE_ID`, etc.); `TOTALPATH` as the vector trail record holding per-stroke points, **pressures, angles (tilts), colors, pen ids, thickness**; per-stroke `point_contour` holding the device's true rendered outline; `RATTA_RLE` bitmaps for page renders; and the full stroke-record field list extracted from the Partner app binary (`flagSpecial`, `preNum`, `penColor`, `penType`, `recMod`, `m_thickness`, `pressures`, `angles`, `point_contour`, etc.) (https://github.com/philips/supernote-typescript/blob/main/plans/vector-format-spec.md).
- Erase/visibility semantics are solved: a per-stroke visibility field (`m_trailStatus`) holds codes `-2/-3/-4/-16/-99` meaning, respectively, unconfirmed-one-instance, moved-by-lasso, partially-erased (survivors follow as separate contour-only "fragment" records), lasso-deleted, and erased-whole — verified against the device's own vector PDF exports stroke-for-stroke (https://github.com/philips/supernote-typescript/blob/main/plans/vector-format-spec.md). Eraser records carry tool ids in `m_copy` (601 drag eraser, 602 stroke-splitting eraser, 603 area/lasso eraser, 604 lasso path) (same source). Partial erase only happens on non-RTR (Real-Time Recognition off) notes, with one documented exception — so `FILE_RECOGN_TYPE` in the header is not a reliable predictor of page content (same source).
- Heading/keyword features live in the footer too: `TITLE_PPPPYYYYXXXX` keys resolve to blocks with `TITLERECT`, a `RATTA_RLE` title bitmap, and `TITLESTYLE` encoding background/label greys as decimal digits `1BBBFFF` (confirmed against the device's own PDF export fills); `KEYWORD_*` keys store recognized keyword text directly in the file (https://github.com/philips/supernote-typescript/blob/main/plans/vector-format-spec.md).
- The `RECOGNFILE` on pages that had recognition run is a real ZIP of **MyScript iink working files**: `meta.json`, `rel.json`, `index.bdom`, `page.bdom`, and per-page `ink.bink` (raw captured ink with channels X/Y/F/T, now fully decoded) plus human-readable `style.css`. Supernote therefore ships third-party (MyScript) handwriting recognition and stores its recognition tree inside every notebook file (https://github.com/philips/supernote-typescript/blob/main/plans/vector-format-spec.md).
- Format-versioning caution for implementers: the stroke-record tail has **four observed variants** across firmware eras (`SN_FILE_VER_20220011`, older Nomad/A5X, `SN_FILE_VER_20260016`, plus a base case) and **no version field predicts which variant a record uses** — robust parsers jump by the declared `strokeLen` rather than parsing the tail (https://github.com/philips/supernote-typescript/blob/main/plans/vector-format-spec.md). Also: pressure array elements are u16, not u32 (the blog's original 4-byte claim was disproven by walking every record to its declared end boundary) (same source).
- **Walnut356/snlib** — an independent **Rust** `.note` parser, the source of the `TOTALPATH` structure now used by other projects, with the companion write-up "Inspecting the SuperNote Notebook Format" (https://github.com/Walnut356/snlib, https://walnut356.github.io/posts/inspecting-the-supernote-note-format/). This is the most direct code reference for a Rust project, though **[unverified: snlib's license this pass — check the repo before pulling; the Rust implementations in this lane are the only GPL-free pullable code candidates]**.
- **jya-dev/supernote-tool** — the original unofficial Python tool (`supernotelib`): converts `.note` to PNG without the device, and to vector PDF/text. Important caveat from the 2026 spec work: its SVG/PDF-vector converter does **not** read `TOTALPATH` at all — it rasterizes and then traces each of a fixed 4-color palette with potrace (https://github.com/jya-dev/supernote-tool, https://github.com/philips/supernote-typescript/blob/main/plans/vector-format-spec.md). Activity: open issues in 2024 are the latest surfaced; maintenance is slow **[unverified: last-commit date]** (https://github.com/jya-dev/supernote-tool/issues). Forks exist (jnewbery, bitSheriff) adding colorization options (https://github.com/jnewbery/supernote-tool).
- **fbalobanov/supernote-viewer** — desktop viewer for `.note` files **[unverified this pass: status]**; **troussos/supernote-editor** — PySide6 desktop editor of `.note` files building on supernote-tool, Apache-2.0 **[unverified: license and activity]**; **nelinory/SupernoteSharp** — C# parser, MIT **[unverified: details]**; **colingourlay/supernote-crosswords** — renders Supernote crosswords; an Obsidian community plugin ("Unofficial Supernote by Ratta Integration") exists per Obsidian plugin stats **[unverified: repo URL]** (all: surfaced in Supernote RE search this pass).
- **Sync/export tooling**: a `supernote` Python package (0.4.1 on PyPI) implements a **Supernote sync server** for integrating notes into local applications, explicitly built on jya-dev's parser (https://pypi.org/project/supernote/0.4.1/); a community API/MCP wrapper lets AI agents chat with Supernote notes (https://ddulic.github.io/supernote/supernote.html). Ratta's own Partner app provides desktop sync/export; the community additionally reverse-engineers its binary for format knowledge rather than protocol knowledge (https://github.com/philips/supernote-typescript/blob/main/plans/vector-format-spec.md).

### 3.3 What this implies for a notes app wanting a pen-native format

The Supernote work is the best public evidence that a *pen-native* file format can be both rich and reverse-engineerable, and it doubles as a requirements checklist for the project's own format:

- A pen-native record should carry per-point **pressure and angle/tilt**, a pen/tool id, color, thickness, and a per-stroke rendered outline (Supernote's `point_contour` is what made shape fidelity possible at all; a uniform-width centerline "can't represent a chisel-tipped calligraphy pen at all", https://github.com/philips/supernote-typescript/blob/main/plans/vector-format-spec.md).
- Erase semantics need first-class design, not post-hoc raster diffs: Supernote's evolution (visibility codes plus partial-erase fragment records) shows a naive "replay the eraser geometrically" approach mis-renders pages where erased text was rewritten in place; the reliable design records *why* a stroke disappeared (same source).
- Versioning: Supernote's format grew four record-tail variants with no field predicting which — the community's workaround (jump by declared length) is a lesson the project's format should avoid needing, by versioning per-record structure explicitly (same source).
- Hybrid raster+vector is a practical pattern: RLE page bitmaps for fast render/thumbnails alongside vector trails.
- Recognition data can live in-file: Supernote embeds MyScript's working files in every notebook, meaning third-party parsers can read recognized text without any network (same source).

Pull-from assessment for the project: unlike the two GPL app ecosystems above, the Supernote RE lane has genuinely pullable code — the TypeScript spec work (https://github.com/philips/supernote-typescript) is documentation-first and its fixtures/insights are license-agnostic knowledge; the Python parsers (jya-dev) are Apache-2.0 **[unverified this pass]**; and the Rust parser (Walnut356/snlib) is the closest to direct reuse, license permitting. If the project wants an import path for Supernote users, the `.note` format is sufficiently decoded that a Rust reader (TOTALPATH trails + RATTA_RLE renders + footer metadata) is feasible from public sources.

---

## 4. Cross-cutting summary for the project

- Closest architecture: RNote (Rust/GTK4). Closest product scope: Xournal++ (PDF annotation, LaTeX, audio). Closest format study: Supernote RE.
- Licenses force concepts-only for both Xournal++ (GPL-2.0, https://flathub.org/apps/com.github.xournalpp.xournalpp) and RNote (GPL-3.0-or-later, https://github.com/flxzt/rnote); there is no permissive code to pull from either, and RNote's crates are not published anyway (https://crates.io/crates/rnote-engine).
- The X2 Supernote generation's file format being community-decoded to per-stroke fidelity (https://github.com/philips/supernote-typescript/blob/main/plans/vector-format-spec.md) sets the user expectation bar for what a "pen-native format" must carry: pressures, tilts, outlines, erase semantics, in-file recognition data.
- Gaps in this lane's research (honest, for follow-up): quantitative most-commented issue rankings for xournalpp and rnote (GitHub issue pages did not render through fetch); exact star/contributor/open-issue counts for both repos; xournalpp GPL-2.0-only vs -or-later; snlib/jya-dev/SupernoteSharp license confirmations; current device lineup names for the N5/N6 generation; RNote Reddit thread permalinks for the sentiment section.
