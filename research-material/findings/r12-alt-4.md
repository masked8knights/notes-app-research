LANE 4 — closed-source handwriting/stylus apps: Goodnotes, Notability, Noteshelf, Samsung Notes, Squid, Concepts, CollaNote, Noteful/Freenotes/Notes+, Amphi. Research-only evidence file, 2026-10-27. Already-covered tools named only as "covered elsewhere".

===== SECTION: Goodnotes — alternatives =====
### Write (Stylus Labs)
- Repo: https://github.com/styluslabs/Write — "cross-platform app with unique features for editing and organizing handwritten notes", C++, Windows/Mac/Linux/iOS/Android builds (per repo README snippet: https://github.com/styluslabs/Write). iOS "Write Pro" App Store listing confirms the open-source move in its release notes: https://apps.apple.com/us/app/stylus-labs-write-pro/id1498369428
- License: AGPL-3.0 — declared in the Debian ITP (package styluslabs-write, version jan-2025): https://www.mail-archive.com/debian-devel@lists.debian.org/msg386717.html ; confirmed by AlternativeTo ("Open Source (AGPL-3.0) and Free"): https://alternativeto.net/software/stylus-labs-write/about/ and a Lemmy announcement "Write is now AGPLv3": https://lemmy.ml/post/21154326 . NixOS packaging PR exists: https://github.com/NixOS/nixpkgs/pull/346463
- Ink stack: custom C++ vector ink engine (repo language C++), pen-first design; pressure/variable-width behavior UNVERIFIED from this lane's sources. Cross-platform desktop + mobile is the differentiator.
- Maintenance: releases page active with 2025-2026 dates visible on https://github.com/styluslabs/Write/releases (dates June 2025 and March 2026 appear in the page listing); exact latest version number UNVERIFIED. Small org, low star count on repo page; single-small-team risk.
- Covers vs Goodnotes: handwriting notebooks, cross-platform; lacks out of the box: HWR search (none found in sources), cloud sync (community/self-host instead), PDF annotation workflow UNVERIFIED for current version.
- Borrowable design: self-hostable collaboration server stylusboard, open source, "online whiteboard server for real-time collaboration in Write": https://github.com/styluslabs/stylusboard
- Pricing/self-host: free, open source; no hosted service to pay for.
- Community pass: Xournal++ maintainers/users discussing complementarity ("Write: smooth, reliable, low power handwriting app") in xournalpp issue: https://github.com/xournalpp/xournalpp/issues/2358 ; LinuxLinks review: https://www.linuxlinks.com/write-application-handwritten-notes/ ; AUR user reports of a Wayland/GL segfault with pointer to upstream issue #27: https://aur.archlinux.org/packages/write_stylus (gripe documentation-style reviews omit: Wayland rendering fragility).
### Saber (covered elsewhere)
- Covered elsewhere in the round (f-droid listing https://f-droid.org/packages/com.adilhanney.saber/ surfaced again in this lane's searches: https://www.reddit.com/r/opensource/comments/y1wxcl/any_open_source_note_taking_app_for_android_that/ ).
### LaTeX-OCR (pix2tex)
- Repo: https://github.com/lukas-blecher/LaTeX-OCR ; site: https://lukas-blecher.github.io/LaTeX-OCR/ ("convert an image containing a formula to corresponding LaTeX code", needs PyTorch).
- License: MIT (Context7 metadata: https://context7.com/lukas-blecher/latex-ocr shows License: MIT; star-history page also shows "Python/MIT": https://www.star-history.com/lukas-blecher/latex-ocr/ ). LICENSE file exists at https://github.com/lukas-blecher/LaTeX-OCR/blob/main/LICENSE
- Ink stack: ViT image-to-LaTeX model; trained with handwritten data mixed in per the training notebook: https://github.com/lukas-blecher/LaTeX-OCR/blob/main/notebooks/LaTeX_OCR_training.ipynb
- Maintenance: ~16.3k stars (https://www.star-history.com/lukas-blecher/latex-ocr/ shows 16.3k, global rank #2707; activity tab shows 16.6k: https://github.com/lukas-blecher/LaTeX-OCR/activity ); star-history shows 0 pushes recently → dormant. Single-author risk (project creator is the main contributor per https://github.com/lukas-blecher/LaTeX-OCR ).
- Covers vs Goodnotes: Goodnotes converts handwriting including math to text; this pulls the handwritten-math-to-LaTeX piece. Lacks: full HWR of prose, PDF annotation, sync.
- Pricing: free/open source; Docker image exists (https://hub.docker.com/r/lukasblecher/pix2tex but "last updated over 4 years ago").
- Community pass: r/LaTeX thread recommending it with the gripe that "the accuracy is still lacking" on hard snippets: https://www.reddit.com/r/LaTeX/comments/1aci7tk/any_good_ocr_software_for_latex/ ; demo video UNVERIFIED.
### Pix2Text
- Repo: https://github.com/breezedeus/Pix2Text — "open-source alternative to Mathpix": layouts, tables, math formulas (LaTeX) and text to Markdown; 80+ languages.
- License: MIT (Context7 metadata: https://context7.com/breezedeus/pix2text shows License: MIT; LICENSE at https://github.com/breezedeus/Pix2Text/blob/main/LICENSE ).
- Ink stack: small model suite (text line rec, layout, formula recognition) producing Markdown; handles handwritten formulas per repo description.
- Maintenance: repo updated within the last month per Context7 (https://context7.com/breezedeus/pix2text ); releases page live: https://github.com/breezedeus/Pix2Text/releases ; star count UNVERIFIED from this lane. A companion Mac desktop app exists: https://github.com/breezedeus/Pix2Text-Mac ("local OCR application based on Pix2Text, no internet connection required").
- Covers vs Goodnotes: handwriting/formula OCR for converting ink to searchable text; lacks ink rendering, note UI, sync.
- Pricing/self-host: free, runs locally; website with docs exists via the repo.
- Community pass: Mac app README documents clipboard-formula workflow: https://github.com/breezedeus/Pix2Text-Mac ; video UNVERIFIED.
### EasyOCR
- Repo: https://github.com/JaidedAI/EasyOCR — ready-to-use OCR, 80+ languages and scripts (Latin, Chinese, Arabic, Devanagari, Cyrillic): https://github.com/JaidedAI/EasyOCR/releases
- License: Apache-2.0 (org page shows "Apache-2.0" next to the repo: https://github.com/jaidedai ).
- Maintenance: 30k stars, 3.6k forks, repo updated Dec 5, 2025 (org page: https://github.com/jaidedai ); latest release v1.7.2 (releases page above). Commit activity appears slowed in 2026; a separate "EasyOCR2" Rust-flavored fork by a different org was announced Dec 28, 2025 in issue #1447: https://github.com/JaidedAI/EasyOCR/issues/1447 (maintenance-consolidation signal).
- Covers vs Goodnotes: printed-text OCR on note images/pages; handwriting accuracy is weaker than dedicated HWR engines (no claim made otherwise). Lacks: stylus input, notebooks, sync.
- Pricing: free, self-hosted Python library; vendor page: https://www.jaided.ai/easyocr/
- Community pass: the EasyOCR2 announcement issue doubles as a community pulse: https://github.com/JaidedAI/EasyOCR/issues/1447 ; video UNVERIFIED.
### WritePad engine + SDK
- Engine repo: https://github.com/phatware/WritePad-Handwriting-Recognition-Engine — "multilingual handwriting recognition engine for iOS, Android, Windows, Linux, MAC OS X" (README: https://github.com/phatware/WritePad-Handwriting-Recognition-Engine/blob/master/README.md )
- License: GPL v3.0 for the engine source ("This source code is distributed under the GPL v 3.0 license", same README); the SDK repo (samples + compiled libs) is at https://github.com/phatware/WritePadSDK and notes open-source projects can use the GPL engine (README: https://github.com/phatware/WritePadSDK ). Commercial license offered for closed use: https://www.prnewswire.com/news-releases/phatware-releases-writepad-handwriting-recognition-engine-as-open-source-300342467.html
- Ink stack: stroke-based HWR recognizing cursive/print/mixed styles (press release above); self-contained engine, no cloud.
- Maintenance: SDK shows 183 stars / 67 forks on its GitHub page (https://github.com/phatware/WritePadSDK ); engine originally open-sourced October 2016 (press release above; mirrored: https://preserve.mactech.com/2016/10/11/phatware-writepad-handwriting-recognition-engine-released-open-source ). Very low recent activity; treat as legacy — last release date UNVERIFIED.
- Covers vs Goodnotes: on-device handwriting recognition to text (the piece Goodnotes does with its own engine); lacks modern accuracy on many languages, no note UI.
- Community pass: Swift sample project documented in the SDK README (link above); video UNVERIFIED.
===== END SECTION =====

===== SECTION: Notability — alternatives =====
(Noteability's signature workflow is audio recording time-linked to handwritten notes; this lane found no uncovered open-source app doing ink+audio sync together; audio-only OSS below plus Saber and Xournal++ which do ink+audio and are covered elsewhere.)
### Shiyin
- Repo: https://github.com/juinwei7/Shiyin — free open-source macOS meeting-notes app: records system audio (Zoom/Meet/Teams) without a bot, transcribes on-device (whisper.cpp + Breeze ASR 25), speaker diarization, timestamped notes.
- License: MIT — stated in the awesome-mac submission PR: https://github.com/jaywcjlove/awesome-mac/pull/3711
- Maintenance: macOS only (Swift, Xcode 26 / Swift 6.2 required per repo README: https://github.com/juinwei7/Shiyin ); releases run through v4.1.2 (release list: https://github.com/juinwei7/Shiyin/releases/tag/v4.1.2 ); auto-update from GitHub Releases since 3.1.1 ( https://github.com/juinwei7/Shiyin/releases/tag/v3.1.1 ). Single-author risk.
- Covers vs Notability: the audio+timestamp side (recording, transcript, time-linked notes) but on transcripts, not handwritten ink; lacks: ink canvas, PDF annotation, mobile.
- Borrowable design: on-device transcription + timestamped note entries keyed to audio positions.
- Pricing: free, brings your own LLM key.
- Community pass: the awesome-mac PR text is the best community-facing description: https://github.com/jaywcjlove/awesome-mac/pull/3711 ; video UNVERIFIED.
### opennotes
- Repo: https://github.com/alexkroman/opennotes — open-source AI meeting notetaker; recordings saved under a recordings/ directory, Whisper.cpp-based transcription, "drift correction" mic setting to keep audio in sync (README: https://github.com/alexkroman/opennotes ).
- License: UNVERIFIED (not visible in this lane's captures; check repo LICENSE before relying).
- Maintenance: small project; stars/last commit UNVERIFIED.
- Covers vs Notability: audio capture + transcription pipeline only; no ink.
- Community pass: README workflow notes above; video UNVERIFIED.
### transcribee
- Org/product page: https://about.transcribee.net/ ; repo: https://github.com/bugbakery/transcribee — collaborative audio/video transcription platform: automatic draft transcripts, confidence-highlighted corrections, speaker naming, real-time collaboration, export to text/WebVTT/SRT (about page).
- License: AGPL-3.0 — stated on the about page ( https://about.transcribee.net/ ) and visible on the org page ( https://github.com/bugbakery ).
- Maintenance: org shows the repo updated Sep 30, 2026 with roughly 517 stars ( https://github.com/bugbakery/transcribee via org listing: https://github.com/orgs/bugbakery/repositories ); hosted version exists (about page). Collective maintainers (software collective per https://github.com/bugbakery ) — bus-factor better than single author.
- Covers vs Notability: structured, time-aligned transcripts with collaboration; not handwriting. Complements an ink layer.
- Pricing/self-host: open source, intended for organizational self-hosting (docs: https://github.com/bugbakery/transcribee/blob/main/doc/development_setup.md ).
- Community pass: audapolis sibling project (word processor for spoken-word editing, AGPL): https://github.com/bugbakery/audapolis/releases/tag/v0.3.0 ; video UNVERIFIED.
### Gap note
- Ink+audio time-sync in open source exists in Saber and Xournal++ (both covered elsewhere); no additional uncovered project found by this lane. UNVERIFIED negative finding — worth a second pass by another lane.
===== END SECTION =====

===== SECTION: Noteshelf — alternatives =====
### Write (Stylus Labs)
- Same entry as under Goodnotes; the relevant fit for Noteshelf is the Android/iOS handwriting-notebook workflow with an open file approach; AGPL-3.0 (Debian ITP: https://www.mail-archive.com/debian-devel@lists.debian.org/msg386717.html ), repo: https://github.com/styluslabs/Write
### EasyOCR / Pix2Text
- Same entries as under Goodnotes: handwriting/page OCR pieces: https://github.com/JaidedAI/EasyOCR and https://github.com/breezedeus/Pix2Text
### Android-handwriting ecosystem evidence (community pass for this and Samsung Notes)
- F-Droid writing category (catalog of FOSS Android writing/inking apps): https://f-droid.org/categories/writing/
- F-Droid listing for xnotes — "handwriting-first notebook for phones and tablets, built for pen and stylus… pressure-sensitive, variable-width ink, nothing you draw is ever flattened" (covered elsewhere, listed here as ecosystem evidence): https://f-droid.org/packages/com.xnotes/
- GrapheneOS community thread on FOSS handwritten note apps + stylus recommendations (Pixel Tablet context): https://discuss.grapheneos.org/d/6355-foss-handwritten-note-taking-apps-and-stylus-reccomendations
- Reddit r/opensource: "Any open source note taking app for Android that use a pen?" — 16 votes/16 comments; recurring conclusion: pen-first FOSS Android apps are scarce and most rely on keyboards: https://www.reddit.com/r/opensource/comments/y1wxcl/any_open_source_note_taking_app_for_android_that/
- Reddit r/fossdroid: "Note taking Apps with hand writing?": https://www.reddit.com/r/fossdroid/comments/1n0dij9/note_taking_apps_with_hand_writing/
- What threads show that docs miss: users' main gripes are sync story and palm rejection on cheap styli, not ink rendering quality.
===== END SECTION =====

===== SECTION: Samsung Notes — alternatives =====
### Write (Stylus Labs)
- Android build exists (cross-platform repo README: https://github.com/styluslabs/Write ); AGPL-3.0 (sources as above). Samsung Notes' pull (free, S-Pen-optimized, Samsung-only) is covered by Write on the openness axis but not on S-Pen Air-command integration UNVERIFIED.
### android-quill (dead, recorded with evidence)
- Repo: https://github.com/ryanamaral/android-quill — "handwriting note-taking app for Android tablets", open source (GPL), explicit note-format claim: "your notes are not stuck in an opaque file format"; tested n-trig pens on ThinkPad Tablet/HTC Flyer and Samsung S-pen on Galaxy Note (ICS) — i.e., Android 3.x/4.x era (README: https://github.com/ryanamaral/android-quill ).
- Status: effectively dead (era of Honeycomb/ICS hardware, no releases visible in captures; last activity date UNVERIFIED). Useful only as a file-format/ink-rendering reference, not a base.
### papyrus (dead stub, recorded with evidence)
- Repo: https://github.com/lambdaforge/papyrus — "Android note app" with ~10 commits and only project skeleton files (repo page shows only .iml/roadmap files: https://github.com/lambdaforge/papyrus ). Never released; do not treat as an alternative. (Distinct from the e-book reader PapyrusReader org: https://github.com/PapyrusReader and from a 2023 FOSS note-manager article whose product's site is dead: https://itsfoss.com/papyrus-open-source-note-manager/ .)
### EasyOCR / WritePad engine
- As under Goodnotes: https://github.com/JaidedAI/EasyOCR and https://github.com/phatware/WritePad-Handwriting-Recognition-Engine (engine GPL v3, Android among supported OSes).
### Saber, xnotes-android, marmalade (covered elsewhere)
- Covered elsewhere; re-surfaced in this lane's F-Droid/Reddit captures ( https://f-droid.org/packages/com.adilhanney.saber/ , https://f-droid.org/packages/com.xnotes/ , https://www.reddit.com/r/fossdroid/comments/1n0dij9/note_taking_apps_with_hand_writing/ ).
===== END SECTION =====

===== SECTION: Squid — alternatives =====
### Write (Stylus Labs)
- Closest uncovered open analog to Squid (pen-driven notes on Android/desktop); AGPL-3.0 (sources as above), repo: https://github.com/styluslabs/Write . PDF annotation in Write UNVERIFIED in this lane's captures.
### Okular (KDE)
- Official page: https://okular.kde.org/ — document viewer with an Annotation mode: "inline and popup notes, highlight and underline text", plus graphic annotations including Freehand Line (ink): https://okular.kde.org/ and docs: https://docs.kde.org/?application=okular (annotations overview captured: https://okular.kde.org/ )
- License: GPL family (KDE project); exact license text UNVERIFIED in this lane's captures — verify against the repo LICENSE before relying (repo: https://invent.kde.org/graphics/okular ).
- Ink stack: dedicated InkAnnotation freehand engine storing point-series paths (DeepWiki analysis of core/annotations: https://deepwiki.com/KDE/okular ; annotation engines incl. InkEngine: same source). Desktop (Linux/Windows/macOS).
- Maintenance: maintained under KDE Gear with regular releases; version 25.12 noted on the official site vs an older Flatpak build 23.08.5 — packaging lag is a real gripe ( https://www.reddit.com/r/linux on annotating PDFs with Okular: https://www.reddit.com/r/linux/ ).
- Covers vs Squid: PDF annotation with ink, highlighters, stamps; lacks: notebook metaphor, cloud sync, mobile-first UX.
- Community pass: r/kde thread "How often do you use the freehand line annotation in Okular?" — reviewer gripes that freehand lines "don't render properly while writing" (live-stroke rendering lag): https://www.reddit.com/r/kde/ ; r/kde thread on whether Okular annotations meet the PDF annotation spec, noting the poppler backend: https://www.reddit.com/r/kde/ (both threads surfaced in this lane's captures; full permalinks in saved results).
### MuPDF / PyMuPDF (pullable PDF-ink engine)
- Official: https://mupdf.com/ ; PyMuPDF: https://github.com/pymupdf/pymupdf — "high performance Python library" wrapping the MuPDF C engine, maintained by Artifex (README).
- License: AGPL v3 with commercial licensing from Artifex — stated explicitly: https://pymupdf.readthedocs.io/en/latest/faq/index.html ("PyMuPDF and MuPDF: either GNU AGPL or a commercial license"; AGPL applies even in a RAG data pipeline) and PyPI: https://pypi.org/project/pymupdf/
- Ink stack: first-class ink-annotation API (set ink lists, stroke points) in the C headers: https://github.com/ArtifexSoftware/mupdf/blob/master/include/mupdf/pdf/annot.h (pdf_set_annot_ink_list) ; annotation recipes: https://pymupdf.readthedocs.io/en/latest/recipes-annotations.html ; release history shows markup/ink annotation accessor improvements: https://mupdf.com/releases/history
- Maintenance: actively maintained by Artifex; docs release 1.26.1 dated May 26, 2025: https://mupdf.readthedocs.io/_/downloads/en/1.26.1/pdf/
- Covers vs Squid: the write-ink-onto-PDF-and-save machinery (what Squid's PDF workflow needs) as a library, not an app. Lacks UI, palm rejection, sync.
- Design worth borrowing: a small project already uses vendored MuPDF specifically to get Okular-like ink annotation write-back into a viewer (issue: https://github.com/theodoreOnzGit/kopitiam/issues/80 ) — evidence the AGPL path is viable for a notes app.
### OpenBoard
- Official: https://openboard.ch/en — GPLv3, "maintained by the community on GitHub" (official site). Repo: https://github.com/OpenBoard-org/OpenBoard (build docs on the wiki; Qt 6).
- License: GPL-3.0-only with an OpenSSL linking exception (Wikipedia infobox + refs: https://en.wikipedia.org/wiki/OpenBoard ; Snap store metadata: https://snapcraft.io/openboard shows GPL-3.0-only).
- Ink stack: Qt-based whiteboard for classrooms: import a PDF and annotate/highlight/correct it live, write over any desktop content, screencast recording (overview article: https://www.blog.brightcoding.dev/2026/09/29/openboard-orgopenboard-open-source-interactive-whiteboard-for-classrooms and https://openboard.ch/en ). Pressure specifics UNVERIFIED.
- Maintenance: release 1.7.7 on 30 March 2026 (Wikipedia ref and Snap "latest/stable 30 March 2026"), last commit April 23, 2026 with 1.8.0 work on the dev branch (Bright Coding article). Community-maintained after GIP ENA took over the IP (Wikipedia). Stars UNVERIFIED from this lane's captures.
- Covers vs Squid: ink over PDFs and lesson recording on desktop; lacks: Android, per-page notebooks, sync.
- Community pass: educational review (annotating on stylus, exporting to PDF for students): https://www.blog.brightcoding.dev/2026/09/29/openboard-orgopenboard-open-source-interactive-whiteboard-for-classrooms ; video UNVERIFIED.
### Saber (covered elsewhere)
- Covered elsewhere; the closest FOSS Android ink-on-PDF app overall.
===== END SECTION =====

===== SECTION: Concepts — alternatives =====
(Concepts' core: infinite-canvas vector ink with pressure. Open analogs below are whiteboards/painters, not notebook apps.)
### Excalidraw
- Official: https://excalidraw.com ; repo: https://github.com/excalidraw/excalidraw — infinite canvas whiteboard, hand-drawn style, images, shape libraries, i18n; "the app hosted at excalidraw.com is a minimal showcase" (README).
- License: MIT (LICENSE file: https://github.com/excalidraw/excalidraw/blob/master/LICENSE ).
- Ink stack: vector elements on an infinite canvas; pen input works via pointer events, but stylus pressure is not a core modeled attribute UNVERIFIED — treat pressure support as absent until tested. E2E-encrypted collab sessions in hosted mode (comparison article: https://www.opensourcealternatives.to/item/excalidraw ).
- Maintenance: 90k+ stars (best-of-2026 roundup: https://www.opensourcealternatives.to/blog/best-open-source-whiteboard-tools ); large maintainer team + community ( https://plus.excalidraw.com/community ); actively developed (fresh third-party coverage within the last weeks: https://openappscout.com/apps/excalidraw/ ).
- Covers vs Concepts: freeform sketching, infinite canvas, collaboration; lacks: pressure-sensitive precision ink, notebooks/pages, PDF-ink workflows, HWR.
- Design worth borrowing: scene serialization that round-trips via a plain JSON file (drag a .excalidraw file onto the canvas; Hack Design guide: https://www.hackdesign.org/toolkit/excalidraw/ ).
- Pricing/self-host: fully free/self-hostable (MIT); Excalidraw+ is the paid hosted tier, not required.
- Community pass: comparison of Excalidraw/tldraw/WBO for collaboration incl. licensing caveats: https://windowsforum.com/windows-news.4/open-source-browser-whiteboards-excalidraw-tldraw-and-wbo-for-instant-collaboration.399992/ ; official HN thread UNVERIFIED in this lane's captures.
### Drawpile
- Official: https://drawpile.net/ ; repo: https://github.com/drawpile/Drawpile — "a collaborative drawing program: draw, paint and animate together with others on the same canvas"; Windows builds code-signed via SignPath (README).
- License: GNU GPL v3.0 (LICENSE file: https://github.com/drawpile/Drawpile/blob/main/LICENSE.txt ; org page shows GPL v3.0: https://github.com/drawpile ).
- Ink stack: raster canvas with pressure-sensitive tablet input designed for graphics tablets; animation and layers; hosted/self-hosted session servers (drawpile.net). Pressure handling via Qt tablet events is standard for the stack UNVERIFIED in this lane's captures.
- Maintenance: ~1.2k stars, org updated Nov 8, 2025 ( https://github.com/drawpile ); small team — single-maintainer risk moderate.
- Covers vs Concepts: pressure drawing and real-time collaboration; lacks: vector ink, notes/notebook structure, PDF import annotation UNVERIFIED.
- Pricing/self-host: free; self-hostable server (drawpile.net docs).
- Community pass: official site + GitHub are the community hubs; dedicated HN/Reddit thread UNVERIFIED in this lane's captures — flagged for a later pass.
### MyPaint
- Official site: https://mypaint.info/ (referenced from the org: https://github.com/mypaint ); repo: https://github.com/mypaint/mypaint — "simple drawing and painting program that works well with Wacom-style graphics tablets", with the libmypaint brushstroke engine and mypaint-brushes library (README).
- License: GNU GPL v2.0 or later (Licenses.md: https://github.com/mypaint/mypaint/blob/master/Licenses.md ; LinuxLinks also lists GPL v2: https://www.linuxlinks.com/mypaint/ ).
- Ink stack: raster; dynamic brush engine reacting to stylus pressure, tilt and speed (fork description and LinuxLinks: https://www.linuxlinks.com/mypaint/ ); unlimited canvas; layer support.
- Maintenance: slow-moving/legacy project — LinuxLinks profile 2023; third-party 2026 mirrors and installers exist (e.g. https://github.com/alexreeves-maker38/Mypaint ) while upstream activity appears low; last release date UNVERIFIED (2.0.1 is the commonly cited last stable — verify before relying). Legacy single-maintainer risk.
- Covers vs Concepts: pressure-expressive freehand ink; lacks: vector output, collaboration, note structure.
- Community pass: DIGImend (cheap non-Wacom tablet drivers) uses MyPaint as its reference pressure app — community tablet-setup docs: https://digimend.github.io/support/howto/apps/mypaint/
### tldraw (source-available, not OSI open source — recorded with caveat)
- Official: https://tldraw.com ; repo: https://github.com/tldraw/tldraw ; SDK license: https://tldraw.dev/community/license and LICENSE.md: https://github.com/tldraw/tldraw/blob/main/LICENSE.md
- License: custom "tldraw license" adapted from the Scratch license (announcement: https://tldraw.substack.com/p/license-updates-for-the-tldraw-sdk ); since v3.0.0 commercial use is permitted with the "Made with tldraw" watermark visible ( https://newreleases.io/project/github/tldraw/tldraw/release/v3.0.0 ); production requires a license key, watermark removal costs money; hobby (non-commercial) licenses keep the watermark ( https://tldraw.dev/sdk-features/license-key ). Third-party summary of the watermark rules: https://windowsforum.com/windows-news.4/open-source-browser-whiteboards-excalidraw-tldraw-and-wbo-for-instant-collaboration.399992/
- Ink stack: React infinite-canvas SDK, polished freehand; pressure handling UNVERIFIED.
- Covers vs Concepts: canvas UX reference; the licensing makes it a borrowing reference, not a fork base, for anything copyleft or watermark-averse.
- Maintenance: company-backed, very active (v3.0.0 released; FAQ: https://tldraw.dev/faq ).
### WBO / whitebophir
- Repo: https://github.com/lovasoa/whitebophir — "online collaborative whiteboard that is simple, free, easy to use and to deploy"; live instance https://wbo.ophir.dev ; official Docker image (README).
- License: AGPL-3.0 (shown on repo metadata: https://github.com/lovasoa/whitebophir ).
- Ink stack: simple vector strokes on shared boards; mobile-friendly; integrates into Jitsi conferences (wiki: https://github.com/lovasoa/whitebophir/wiki/WBO-Jitsi-integration ).
- Maintenance: ~2.5k stars, 476 forks (issues page header: https://github.com/lovasoa/whitebophir/issues ); Docker image actively updated with OpenTelemetry support ( https://hub.docker.com/r/lovasoa/wbo ); last commit date UNVERIFIED; primarily one core maintainer.
- Covers vs Concepts: lightweight shared sketching, trivially self-hosted; lacks: pressure, layers, notebooks.
- Pricing: free/self-host via Docker.
===== END SECTION =====

===== SECTION: CollaNote — alternatives =====
(CollaNote's core: free iPad handwriting with real-time collaboration and audio. Open analogs are whiteboards with collab; ink+audio collab remains a gap.)
### Excalidraw
- As above: MIT, E2E-encrypted collaboration, self-hostable — repo: https://github.com/excalidraw/excalidraw ; collaboration caveat article: https://windowsforum.com/windows-news.4/open-source-browser-whiteboards-excalidraw-tldraw-and-wbo-for-instant-collaboration.399992/
### Drawpile
- As above: GPL-3.0 shared canvas built for real-time co-drawing with layers — https://github.com/drawpile/Drawpile ; https://drawpile.net/
### WBO (whitebophir)
- As above: AGPL-3.0, Jitsi integration for in-call whiteboarding — https://github.com/lovasoa/whitebophir
### stylusboard (Write's collab server)
- Repo: https://github.com/styluslabs/stylusboard — "online whiteboard server for real-time collaboration in Write": shared handwritten documents, self-hostable; the only uncovered open option where the shared object is a handwriting document rather than a whiteboard. License UNVERIFIED (check repo LICENSE). Maintenance status tied to the Write project.
### Gap note
- Real-time collaborative handwriting with palm rejection and pressure (CollaNote's actual magic) has no uncovered open-source equivalent this lane could verify; Excalidraw/Drawpile/WBO cover whiteboard-style collab only. UNVERIFIED negative finding.
===== END SECTION =====

===== SECTION: Noteful / Freenotes / Notes+ — alternatives =====
(iPad handwriting+PDF annotators. iPad-native OSS is thin; cross-platform picks below.)
### Write (Stylus Labs)
- iOS "Write Pro" on the App Store with the open-source repo noted in its App Store release notes — https://apps.apple.com/us/app/stylus-labs-write-pro/id1498369428 ; repo https://github.com/styluslabs/Write ; AGPL-3.0 (Debian ITP: https://www.mail-archive.com/debian-devel@lists.debian.org/msg386717.html ). The iOS Pro app is the closest uncovered open-core analog to Noteful's workflow; current iOS build maintenance pace UNVERIFIED.
### Okular
- Desktop PDF ink annotation (covered in detail under Squid) — the PDF-annotation-with-ink piece on desktop: https://okular.kde.org/
### MuPDF / PyMuPDF
- The library path for building PDF ink annotation into a notes app (covered in detail under Squid): https://github.com/pymupdf/pymupdf ; AGPL v3 / commercial from Artifex: https://pymupdf.readthedocs.io/en/latest/faq/index.html
### Saber (covered elsewhere)
- Covered elsewhere; Flutter-based, cross-platform including iOS.
===== END SECTION =====

===== SECTION: Amphi (useamphi.com, closed iPad AI study canvas) — alternatives =====
(Closed app identified from its App Store listing — "iPad study workspace that brings your notes, documents, flashcards, timers, calculators, and AI tutors into one canvas": https://apps.apple.com/gb/app/amphi-ai-notes-flashcards/id6760332638 — and its site: https://www.useamphi.com/ and https://www.useamphi.com/about . Note: amphi.ai is a different product, a visual data-preparation tool — do not conflate: https://amphi.ai/ . Open-source Amphi Notes is covered elsewhere.)
### Khoj
- Official: https://khoj.dev/ ; repo: https://github.com/khoj-ai/khoj — self-hostable AI "second brain": semantic search over notes/docs, chat with local or cloud LLMs, custom agents, automations (README).
- License: AGPL-3.0 with 36,048 stars (profile page: https://everylocalai.com/tool/khoj ); org: https://github.com/khoj-ai
- Ink stack: none (text-based RAG over notes); for Amphi's AI-tutor angle it pulls the search/agents/automations layer that could sit on top of an ink-canvas app's exports.
- Maintenance: active, company-backed tiny team ("We build in the open", https://khoj.dev/ ); GPU acceleration via CUDA/Metal/Vulkan documented ( https://everylocalai.com/tool/khoj ).
- Covers vs Amphi: AI Q&A over your own material, agents, automations; lacks: ink canvas, flashcards UI, PDF ink markup.
- Pricing/self-host: free self-host; Khoj's managed cloud is being deprecated and self-hosting is now the primary path (deployment page: https://railway.com/deploy/khoj ).
- Community pass: the "2026 review, self-hosted only" write-up is the community pulse incl. the cloud-deprecation angle: https://www.promptquorum.com/power-local-llm/khoj-ai-second-brain-review ; video UNVERIFIED.
### Reor (dead — recorded with evidence)
- Repo: https://github.com/reorproject/reor — AI desktop note-taking running LLMs/embeddings locally (Ollama, Transformers.js, LanceDB), auto-linking, semantic search, RAG (README).
- License: AGPL-3.0 (repo badge/README: https://github.com/reorproject/reor ).
- Maintenance: ARCHIVED — "This repository was archived by the owner on Mar 7, 2026. It is now read-only." (releases page banner: https://github.com/reorproject/reor/releases ); ~8.6k stars ( https://www.star-history.com/reorproject/reor/ ). Dead as a base; potentially forkable code only.
- Community pass: r/opensource announcement thread: https://www.reddit.com/r/opensource/ (surfaced in captures as r/opensource: "Reor: A private & self-organizing note-taking app powered by local AI models").
### Pix2Text
- As under Goodnotes: local math-formula + text OCR to LaTeX/Markdown — a plausible pull for an AI study-canvas that needs handwritten equations digitized: https://github.com/breezedeus/Pix2Text (MIT).
### Gap note
- The open-source Amphi Notes repo (covered elsewhere) is the direct analog; for the closed app's canvas+AI-tutors combination, no other uncovered open project combines ink canvas and embedded tutors this lane could verify. UNVERIFIED negative finding.
===== END SECTION =====

===== ROWS =====
| Write (Stylus Labs) | y (AGPL-3.0) | https://github.com/styluslabs/Write | Cross-platform vector-ink handwriting app (Win/Mac/Linux/iOS/Android), open since ~2020, releases into 2026; self-hostable collab server stylusboard; gripe: Wayland segfaults reported. findings: r12-alt-4 |
| Excalidraw | y (MIT) | https://github.com/excalidraw/excalidraw | 90k+ star infinite-canvas whiteboard, vector elements, E2E collab, very active; no pressure-sensitive precision ink. findings: r12-alt-4 |
| Drawpile | y (GPL-3.0) | https://github.com/drawpile/Drawpile | Collaborative raster drawing with tablet pressure + animation, ~1.2k stars, updated Nov 2025, small team. findings: r12-alt-4 |
| Okular | y (GPL, verify exact text) | https://okular.kde.org/ | KDE document viewer with dedicated InkAnnotation freehand engine over PDFs; gripes: live-stroke render lag, poppler backend, flatpak lag. findings: r12-alt-4 |
| OpenBoard | y (GPL-3.0-only) | https://openboard.ch/en | Classroom whiteboard: PDF import + ink annotation, write over desktop, screencast; 1.7.7 Mar 2026, 1.8.0 in dev. findings: r12-alt-4 |
| MuPDF / PyMuPDF | y (AGPL-3.0, commercial from Artifex) | https://github.com/pymupdf/pymupdf | Pullable PDF engine with first-class ink-annotation write API (pdf_set_annot_ink_list); docs 1.26.1 May 2025. findings: r12-alt-4 |
| MyPaint | y (GPL-2.0-or-later) | https://github.com/mypaint/mypaint | Pressure/tilt/speed dynamic brush engine (libmypaint), infinite canvas, raster; legacy-slow maintenance, single-maintainer risk. findings: r12-alt-4 |
| WBO (whitebophir) | y (AGPL-3.0) | https://github.com/lovasoa/whitebophir | Lightweight self-host collaborative whiteboard, ~2.5k stars, Docker, Jitsi integration; no pressure. findings: r12-alt-4 |
| tldraw | n (source-available, custom license) | https://github.com/tldraw/tldraw | Infinite-canvas React SDK; commercial use OK with watermark since v3.0.0, license key for production; borrowing reference only. findings: r12-alt-4 |
| LaTeX-OCR (pix2tex) | y (MIT) | https://github.com/lukas-blecher/LaTeX-OCR | Handwritten math image to LaTeX (ViT), ~16k stars, dormant, single author; community gripe: accuracy on hard snippets. findings: r12-alt-4 |
| Pix2Text | y (MIT) | https://github.com/breezedeus/Pix2Text | Open Mathpix alternative: layout/table/formula/text to Markdown, 80+ languages, local Mac app, updated recently. findings: r12-alt-4 |
| EasyOCR | y (Apache-2.0) | https://github.com/JaidedAI/EasyOCR | 30k-star OCR, 80+ languages, last release v1.7.2, repo updated Dec 2025; EasyOCR2 fork announced Dec 2025. findings: r12-alt-4 |
| Kraken | y (Apache-2.0) | https://github.com/mittagessen/kraken | Turn-key OCR/HTR for historical and non-Latin scripts, model repo ecosystem, docs 4.3.0; stars UNVERIFIED. findings: r12-alt-4 |
| WritePad engine/SDK | y (engine GPL v3.0; SDK samples) | https://github.com/phatware/WritePad-Handwriting-Recognition-Engine | Self-contained multilingual cursive/print/mixed HWR engine for iOS/Android/Win/Linux/macOS, open-sourced 2016, legacy/low activity. findings: r12-alt-4 |
| Khoj | y (AGPL-3.0) | https://github.com/khoj-ai/khoj | Self-hostable AI second brain: semantic search, agents, automations over notes; 36k stars, cloud deprecated, self-host primary. findings: r12-alt-4 |
| Reor | y (AGPL-3.0, ARCHIVED) | https://github.com/reorproject/reor | Local-LLM AI notes app, 8.6k stars, archived Mar 7 2026 — forkable code only. findings: r12-alt-4 |
| Shiyin | y (MIT) | https://github.com/juinwei7/Shiyin | macOS meeting notes: botless recording, on-device whisper.cpp transcription, speaker ID, timestamped notes; active releases (v4.1.2), single author. findings: r12-alt-4 |
| opennotes | y (license UNVERIFIED) | https://github.com/alexkroman/opennotes | Open-source AI meeting notetaker with whisper.cpp and audio drift-correction; small project. findings: r12-alt-4 |
| transcribee | y (AGPL-3.0) | https://github.com/bugbakery/transcribee | Collaborative audio/video transcription with confidence highlighting, speaker naming, exports; ~517 stars, updated Sep 2026. findings: r12-alt-4 |
| android-quill | y (GPL, dead) | https://github.com/ryanamaral/android-quill | Ancient Android-tablet handwriting app (Android 3.x/4.x, S-pen/n-trig tested), open file format claim; effectively dead, reference only. findings: r12-alt-4 |

LANE 4 COMPLETE — 9 closed apps processed, 20 new alternatives documented
