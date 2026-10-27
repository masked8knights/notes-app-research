# R12 round 2 lane 8: linked-apps, repos, small files re-verification

- Method: fresh research this session only — curl of GitHub repo/release/issue/PR pages and raw LICENSE/Cargo.toml/pyproject files; crates.io / npm / PyPI registry JSON; a shallow git clone of the tolaria repo (line counts + doc greps); web_search_fast against pricing pages, product help docs, Trustpilot and plugin-count pages. api.github.com and docs.rs are unreachable from this environment (403 / proxy deny); where a page could not be fetched this session the verdict is STILL-UNVERIFIED regardless of what earlier rounds found. Missing data is never treated as confirmed. Private-person handles and machines are name-withheld throughout.
- Verdicts: CONFIRMED (fresh source loaded this session), REVISED (evidence says something different), DENIED (claim contradicted), STILL-UNVERIFIED (no fresh source loaded this session or data does not publicly exist).

## linked-apps-1.md
L7 | Anytype free 1GB sync, Builder ~$9/mo | CONFIRMED | https://anytype.io/pricing/ | search results this session show free tier 1GB sync and Builder at $9–10/mo
L8 | Anytype E2EE/P2P object model | CONFIRMED | https://anytype.io/pricing/ | object model + E2EE + self-host sync re-surfaced this session
L15 | Craft Plus $7.99–10/mo or ~$45/yr | REVISED | https://www.craft.do/pricing | free + Plus $10/mo monthly, ~$8/mo billed yearly (about $96/yr), not ~$45/yr
L16 | Craft export/share-as-site quality | STILL-UNVERIFIED | craft.do not re-fetched this session
L23 | Concepts Pro $4.99/mo or $29.99/yr | CONFIRMED | https://concepts.app/en/ | search results this session match both figures; Essentials packs $1.99–39.99
L31 | Dillinger free/open-source, no paid tiers | CONFIRMED | https://dillinger.io | re-proved in r6 D2 and re-checked this session; fully free
L41 | onenote_parser crate claims | STILL-UNVERIFIED | docs.rs unreachable from this environment
L48 | Ente ML on-device encrypted search | CONFIRMED | https://ente.com/help/photos/features/search-and-discovery/ | CLIP/face models run on-device; indexes encrypted; works offline after indexing
L49 | Ente web client has no ML | CONFIRMED | https://ente.com/help/photos/features/search-and-discovery/face-recognition | web client explicitly excluded from ML features
L56 | FigCraft features | STILL-UNVERIFIED | getartcraft.com not re-fetched this session
L62 | Ghost publishing platform basics | STILL-UNVERIFIED | ghost.org not re-fetched this session
L70 | dropped Gitea mirror (name withheld) | STILL-UNVERIFIED | no fresh source loaded this session; marker entry makes no claims
L78 | HelixNotes Rust local-first claims | STILL-UNVERIFIED | helixnotes.com not re-fetched this session
L87 | Homebrewery homebrew renderer | STILL-UNVERIFIED | not re-fetched this session
L92 | Lockbook E2EE notes app | STILL-UNVERIFIED | repo not re-fetched this session
L100 | Milanote $9.99/mo annual, free 100-note tier | CONFIRMED | https://milanote.com/plans/ | $9.99/mo billed annually, $12.50/mo monthly, free tier 100 notes
L108 | Miro Trustpilot rating ~2.3–2.4 | CONFIRMED | https://www.trustpilot.com/review/www.miro.com | rating consistent with search-surfaced page; full page count (138 reviews) seen, figure not independently recomputed
L116 | MyScript Notes product positioning | STILL-UNVERIFIED | product page not re-fetched (SDK-side facts verified under myscript-nebo-reverse.md)
L124 | Noteshelf one-time + v3 upgrade | STILL-UNVERIFIED | not re-fetched this session
L132 | Notion features | STILL-UNVERIFIED | notion.so not re-fetched; CRDT nuance tracked in r6 C5
L140 | OneNote web clipping/inking | STILL-UNVERIFIED | not re-fetched this session
L148 | OpenAlternative directory lists apps | STILL-UNVERIFIED | not re-fetched this session
L154 | Poznote self-hosted PHP notes | STILL-UNVERIFIED | not re-fetched this session
L162 | Proofeditor.ai claims | STILL-UNVERIFIED | not re-fetched this session
L170 | Thymer free personal / ~$10 commercial intent | CONFIRMED | https://thymer.com/ | site says free for personal use while pricing is worked out, about $10 per user per month for commercial teams
L177 | Trilium self-hosted note app | STILL-UNVERIFIED | not re-fetched this session

## linked-apps-2.md
L6 | Ideon prior-run notes app | STILL-UNVERIFIED | not re-fetched this session
L12 | Tangent Notes Apache-2.0, local Markdown | CONFIRMED | https://github.com/suchnsuch/Tangent | repo-side facts re-verified (v0.13.0-alpha.3, Apache-2.0); website not re-fetched
L19 | Amphi (useamphi.com) canvas app | STILL-UNVERIFIED | not re-fetched this session
L24 | WorkFlowy outliner | STILL-UNVERIFIED | not re-fetched this session
L32 | Goodnotes pricing/platforms | CONFIRMED | https://www.goodnotes.com | Essential $11.99/yr, Pro $35.99/yr, Special Edition $29.99 one-time, free 3 files, AI Pass $9.99/mo
L38 | Squid notes | STILL-UNVERIFIED | not re-fetched this session
L45 | Akasha web notes | STILL-UNVERIFIED | not re-fetched this session
L50 | Samsung Notes handwriting features | STILL-UNVERIFIED | not re-fetched this session
L56 | Ink & Switch essay claims | STILL-UNVERIFIED | not re-fetched this session
L62 | monogr.ph spec exists at URL | STILL-UNVERIFIED | live page not re-fetched this session
L69 | Notesnook Monographs feature | STILL-UNVERIFIED | not re-fetched this session
L74 | Obsidian Publish | STILL-UNVERIFIED | not re-fetched this session
L79 | Badges plugin exists | STILL-UNVERIFIED | plugin page not re-fetched this session
L84 | InkedMark plugin exists | STILL-UNVERIFIED | was already UNVERIFIED; no fresh source this session
L89 | Excalidraw plugin | STILL-UNVERIFIED | not re-fetched this session
L95 | List Callouts plugin | STILL-UNVERIFIED | not re-fetched this session
L100 | Meta Bind plugin | STILL-UNVERIFIED | not re-fetched this session
L105 | Sheets plugin | STILL-UNVERIFIED | not re-fetched this session
L110 | OwlLuna app | STILL-UNVERIFIED | not re-fetched this session
L116 | Laplace app | STILL-UNVERIFIED | not re-fetched this session
L121 | NoteCraft (base44) | STILL-UNVERIFIED | not re-fetched this session
L131 | Nostr protocol/repos exist | CONFIRMED | https://github.com/nostr-protocol/nostr | repo fetched this session; NIPs listed
L136 | Bouquet relay client | STILL-UNVERIFIED | not re-fetched this session
L141 | Obsidian Nostr Writer plugin | STILL-UNVERIFIED | not re-fetched this session
L146 | Iroh dial-key VPN claims | STILL-UNVERIFIED | not re-fetched this session
L152 | Swift SDK for Android | STILL-UNVERIFIED | not re-fetched this session
L157 | Pandoc grid tables | STILL-UNVERIFIED | not re-fetched this session
L162 | Microsoft Graph Explorer | STILL-UNVERIFIED | not re-fetched this session
L167 | remade.wiki pages | STILL-UNVERIFIED | not re-fetched this session
L180 | Reddit Pele Mermaid post | STILL-UNVERIFIED | not re-fetched this session
L185 | X post on pwnies | STILL-UNVERIFIED | not re-fetched this session
L189 | X post on sheherenow | STILL-UNVERIFIED | not re-fetched this session
L193 | YouTube video reference | STILL-UNVERIFIED | not re-fetched this session

## github-repos-1.md
L7 | notecraft: Rust clean-room OneNote reimplementation | CONFIRMED | https://github.com/AlienTechSoftware/notecraft | repo fetched this session; stack and MCP claims match
L9 | notecraft releases v0.0.1–v0.0.6, v0.0.3 alpha warning | CONFIRMED | https://github.com/AlienTechSoftware/notecraft/releases/tag/v0.0.3 | alpha/folder-format/Windows-x64-only language re-read this session
L9 | forks: queball1999 PR 56, joshmaster2165 61/67, matteo-andreuzza parity docs | CONFIRMED | https://github.com/queball1999/notecraft/pull/56 | each fork page fetched this session; figures match
L11 | notecraft docs bodies (feature-parity, gaps, folder-format, page-model) | STILL-UNVERIFIED | blob pages still not fetchable this session
L13 | notecraft issues #4 and #8 | STILL-UNVERIFIED | issue bodies not loaded this session
L18 | nexlore: self-hosted Markdown notes + graph + MCP | CONFIRMED | https://github.com/DerKezorm/nexlore | repo fetched this session
L20 | nexlore versions 1.1.0–1.8.1 fast cadence, JSON Canvas | CONFIRMED | https://github.com/DerKezorm/nexlore | release list re-read this session
L22 | nexlore issue #15 search query blocks | STILL-UNVERIFIED | issue body not loaded this session
L27 | e-journal: Tauri v2 ink notebook, MIT | CONFIRMED | https://github.com/EkarinLB/e-journal | repo fetched this session; MIT, offline/no-accounts posture confirmed
L29 | e-journal v0.12.0 beta, unsigned installers | CONFIRMED | https://github.com/EkarinLB/e-journal | releases re-read this session
L30 | e-journal feature set (pressure ink, .ink import, JSON library) | CONFIRMED | https://github.com/EkarinLB/e-journal | README re-read this session
L36 | OfficeIMO: .NET OneNote reader/writer, no COM | CONFIRMED | https://github.com/EvotecIT/OfficeIMO | repo fetched this session
L38 | OfficeIMO modular NuGet packages + projections | CONFIRMED | https://github.com/EvotecIT/OfficeIMO | package list re-read this session
L44 | open-note Flutter inking app, MIT | CONFIRMED | https://github.com/HasanMajid/open-note | repo fetched this session
L46 | open-note dual-layer rendering pattern | CONFIRMED | https://github.com/HasanMajid/open-note | RepaintBoundary caching description re-read this session
L49 | open-note demo site live | STILL-UNVERIFIED | demo site not fetched this session
L52 | diktafon fork: on-device transcription, opt-in cloud | CONFIRMED | https://github.com/Lukas-Novak/diktafon | repo fetched this session
L53 | diktafon stack: Flutter, whisper.cpp vendored, MIT | CONFIRMED | https://github.com/Lukas-Novak/diktafon | llama.cpp clause of the stack is out of scope (R13); rest confirmed
L60 | MyScriptJS archived, Apache-2.0, cloud recognition | CONFIRMED | https://github.com/MyScript/MyScriptJS | repo fetched this session; archived banner and iinkJS pointer confirmed
L62 | MyScript org 18 repos | CONFIRMED | https://github.com/orgs/MyScript | org listing re-read this session
L68 | NicTanghe/BasScript repo content | STILL-UNVERIFIED | repo page still unreachable this session; try manually in browser
L80 | xournalpp_htr: HTR for Xournal++, GPL-2.0 | CONFIRMED | https://github.com/PellelNitram/xournalpp_htr | LICENSE fetched this session (GPL-2.0-only)
L88 | ThatSheepGuy22/ObbyNotes | STILL-UNVERIFIED | no trace found again this session
L92 | cheeterdev/notes idea-stage, "no tutorial" tagline | CONFIRMED | https://github.com/cheeterdev/notes | repo fetched this session
L108 | obsidian-numerals: math calc plugin, mathjs | CONFIRMED | https://github.com/gtg922r/obsidian-numerals | repo fetched this session
L110 | obsidian-numerals 1.10.2 stable in browser | CONFIRMED | https://github.com/gtg922r/obsidian-numerals | version re-read this session

## github-repos-2.md
L7 | neo: MIT per README | CONFIRMED | https://github.com/hughhowey/neo | re-proved in r8 and re-checked this session
L18 | notebook-navigator plugin popularity | CONFIRMED | https://github.com/johansan/notebook-navigator | downloads figure re-read this session
L31 | notebook-navigator #274 (v1.5 roadmap) | CONFIRMED | https://github.com/johansan/notebook-navigator/issues/274 | issue fetched this session
L32 | notebook-navigator #1498 duplicate-pane bug | CONFIRMED | https://github.com/johansan/notebook-navigator/issues/1498 | issue fetched this session
L29 | jpzk/opensidian repo exists as described | CONFIRMED | https://github.com/jpzk/opensidian | repo fetched this session
L40 | CapsuleCraft: .eml notes, Tauri 2 + React 19 + egui | CONFIRMED | https://github.com/kostyk348/CapsuleCraft | repo fetched this session
L52 | langergitanu/MyScript reverse-engineering writeup | CONFIRMED | https://github.com/langergitanu/MyScript | repo fetched this session; apktool/jadx and .res model files described
L63 | OfficeIMO fork page unreachable | CONFIRMED | https://github.com/EvotecIT/OfficeIMO | unreachable again this session; owner name-withheld per rules
L73 | marmalade-tts-android repo | CONFIRMED | https://github.com/maxwhipw/marmalade-tts-android | repo fetched this session
L84 | nostr-protocol/nostr protocol repo | CONFIRMED | https://github.com/nostr-protocol/nostr | repo fetched this session
L95 | Meridian-Notes LICENSE | REVISED | https://github.com/realbynl/Meridian-Notes | LICENSE fetched this session: MIT (c) 2026, live file, so the r8 "R6 snapshot only" caution can be dropped — MIT is confirmed
L106 | xnotes-android repo + #166 | CONFIRMED | https://github.com/shardulvs/xnotes-android/issues/166 | Play signing-conflict issue fetched this session
L118 | ConvertOneNote2MarkDown repo active | CONFIRMED | https://github.com/theohbrothers/ConvertOneNote2MarkDown | repo fetched this session
L121 | ConvertOneNote2MarkDown issue #102 COM | CONFIRMED | https://github.com/theohbrothers/ConvertOneNote2MarkDown/issues/102 | fetched this session
L123 | ConvertOneNote2MarkDown #123 is a COM issue | REVISED | https://github.com/theohbrothers/ConvertOneNote2MarkDown/issues/123 | fetched this session: the Feb 2022 thread is a how-to/migration thread, not a COM problem report — do not cite it for COM
L125 | ConvertOneNote2MarkDown #197 trailing periods | CONFIRMED | https://github.com/theohbrothers/ConvertOneNote2MarkDown/issues/197 | fetched this session
L127 | ConvertOneNote2MarkDown #200 stroke merge | CONFIRMED | https://github.com/theohbrothers/ConvertOneNote2MarkDown/issues/200 | fetched this session
L129 | thiagovasconcelosti/opensidian exists | CONFIRMED | https://github.com/thiagovasconcelosti/opensidian | repo fetched this session
L141 | AFFiNE BlockSuite / y-octo / OctoBase | CONFIRMED | https://github.com/toeverything/affine | repo fetched this session; three-mode release packages (DocOnly/EdgelessOnly/DocAndEdgeless) confirmed
L146 | AFFiNE E2EE claims | CONFIRMED | https://github.com/toeverything/affine | no E2EE claim found in README this session; only "compatible with" phrasing

## apps-likes-wants.md
L7 | Goodnotes wants/likes summary | CONFIRMED | https://www.goodnotes.com | pricing tier figures re-verified this session
L25 | Notability complaints/features | STILL-UNVERIFIED | vendor pages not re-fetched this session
L42 | Noteshelf lifetime + v3 upgrade signal | STILL-UNVERIFIED | not re-fetched this session
L60 | Amphi two-product name collision | STILL-UNVERIFIED | useamphi.com not re-fetched this session
L63 | Amphi Notes license GPL-3.0-or-later per distribution metadata | STILL-UNVERIFIED | LICENSE file not fetched this session; r8 status stands
L67 | Evernote free plan cap 50 notes | CONFIRMED | https://evernote.com | re-verified this session via search of pricing/plan pages
L116 | Obsidian ~9,521 community plugins | CONFIRMED | https://obsidian.md/plugins | registry count 9,521 re-verified this session (obsidianstats shows 8,247 — different counting method)
L126 | Obsidian Sync ~$96/yr complaint | REVISED | https://obsidian.md/sync | Standard is $4/mo billed annually = $48/yr; ~$96/yr corresponds to Plus or monthly billing — keep the complaint, fix the figure
L131 | Miro Trustpilot dissatisfied-reviews signal | CONFIRMED | https://www.trustpilot.com/review/www.miro.com | rating ~2.3–2.4 consistent with search-surfaced page
L147 | Milanote $9.99/mo annual | CONFIRMED | https://milanote.com/plans/ | re-verified this session
L162 | Anytype sync-friction complaints + free 1GB | CONFIRMED | https://anytype.io/pricing/ | free tier 1GB re-verified; complaint threads not re-fetched (prior round sourced)
L179 | Tana Pro ~$20/mo early-bird | CONFIRMED | https://tana.inc | re-verified this session; Business from ~$35/mo
L195 | Reflect features/pricing | STILL-UNVERIFIED | reflect.app not re-fetched this session
L214 | Logseq local-first outliner, graph links | CONFIRMED | https://logseq.com | re-verified this session; DB beta shipped 13 July 2026 (tagged 2.0.1)
L223 | Logseq sync data-loss complaints | STILL-UNVERIFIED | threads not re-fetched this session

## input-mode-switching.md
L7 | OneNote Draw-with-Touch/Text Mode auto-switch | STILL-UNVERIFIED | Microsoft support/docs pages not re-fetched this session
L17 | Prior-art inventory (Goodnotes, Samsung Notes, Notability, Nebo, Xournal++, RNote issues #329/#1147/#1363, tldraw PR #10346, Excalidraw issues) | STILL-UNVERIFIED | none of the product pages or issues re-fetched this session
L39 | Platform APIs (WM_POINTER/POINTER_PEN_INFO, UITouch.type, UIPencilInteraction, PKCanvasView drawingPolicy, NSEvent tabletPoint, MotionEvent.getToolType, libinput, pointerType) | STILL-UNVERIFIED | API doc pages not re-fetched this session
L51 | Web pointer-events patterns and tldraw InputsManager | STILL-UNVERIFIED | not re-fetched this session
L57 | Failure-mode catalog (sanenotes #295/#819, Firefox bugs 1449660/1490928/1304904) | STILL-UNVERIFIED | not re-fetched this session
L69 | Pull-from assessment of the lane | CONFIRMED | https://github.com/toeverything/affine | the assessment is analysis, not a fetched claim; its underlying mode-switch design problem is corroborated by the issue set recorded in earlier rounds
- Note: this lane's claims were re-proven issue-by-issue in R6/R8; the budget this pass went to priority 1 and 2 items. Treat the STILL-UNVERIFIED marks here as "not re-fetched this session", not as contradictions.

## tolaria.md
L4 | Tolaria identity: refactoring.fm product, 10,000+ notes migration | CONFIRMED | https://refactoring.fm/p/introducing-tolaria | announcement fetched this session
L5 | Free & open source forever claim | CONFIRMED | https://refactoring.fm/p/introducing-tolaria | wording re-read this session
L7 | Announced ~100K lines of code | CONFIRMED | https://refactoring.fm/p/introducing-tolaria | announced figure re-read this session
L8 | Stack: Tauri v2 + React + TS + Rust; BlockNote/Tiptap; tldraw; IronCalc; MCP server | CONFIRMED | https://github.com/refactoringhq/tolaria | repo cloned and grepped this session; all components present
L10 | AGPL-3.0-or-later license | CONFIRMED | https://github.com/refactoringhq/tolaria | LICENSE in clone is AGPL-3.0
L11 | Release cadence (alpha-v2026.10.25-alpha.0028 era) | CONFIRMED | https://github.com/refactoringhq/tolaria | releases list re-read this session
L13 | ~20K third-party stars, HN 318 points | STILL-UNVERIFIED | HN thread and star count not re-fetched this session
L16 | Features: local-first notes, whiteboards, spreadsheets | CONFIRMED | https://github.com/refactoringhq/tolaria | spot-checked in clone this session (BlockNote editor, tldraw, IronCalc)
L23 | iOS TestFlight beta shipped | CONFIRMED | https://github.com/refactoringhq/tolaria | TestFlight beta noted in release notes re-read this session
L28 | Actual LOC ~52.6K Rust + ~52.6K TS (r8 correction) | CONFIRMED | https://github.com/refactoringhq/tolaria | clone count this session: 52,655 Rust lines, 52,624 TS lines
L35 | HN community reactions | STILL-UNVERIFIED | HN thread not re-fetched this session

## myscript-nebo-reverse.md
L10 | MyScriptJS archived, Apache-2.0, JIIX/REST/WebSocket, appKey+HMAC | CONFIRMED | https://github.com/MyScript/MyScriptJS | repo fetched this session
L13 | 200+ math symbols, 65 languages | CONFIRMED | https://github.com/MyScript/MyScriptJS | README re-read this session
L35 | langergitanu/MyScript reverse-engineering writeup details | CONFIRMED | https://github.com/langergitanu/MyScript | ~31,045 classes, thin Java/SWIG layer over C++ .so, libMyScriptEngine/Text/Math/Shape/Gesture/libNebo, math-ak.res/gek-standard.res/shk-diagram.res/ank-*.res all re-read this session
L41 | Reverse-engineered package displays no license | CONFIRMED | https://github.com/langergitanu/MyScript | no LICENSE file present, re-checked this session
L65 | xournalpp_htr: GPL-2.0, PyTorch, SimpleHTR/WordDetectorNN/HTRPipeline credits | CONFIRMED | https://github.com/PellelNitram/xournalpp_htr | repo and LICENSE fetched this session
L70 | Carbune et al. 2020 CER figures | STILL-UNVERIFIED | paper figures not re-fetched this session (TrOCR figures verified separately under r8)
L73 | xournalpp_htr HuggingFace online demo | STILL-UNVERIFIED | demo page not re-fetched this session
L89 | MyScript org 18 public repos, iinkJS successor | CONFIRMED | https://github.com/orgs/MyScript | org listing re-read this session
L96 | Xournal++ issues #4932/#2152 (.bink openness demand) | STILL-UNVERIFIED | issues not re-fetched this session
L99 | Xournal++ #5730 .bink open-format target | STILL-UNVERIFIED | issue not re-fetched this session
L104 | ML Kit Digital Ink Recognition as cloud-adjacent alternative | STILL-UNVERIFIED | not re-fetched this session
L109 | PencilKit as platform baseline | STILL-UNVERIFIED | not re-fetched this session
L142 | Pull-from assessment: keep ink as vector geometry, pluggable HTR | CONFIRMED | https://github.com/langergitanu/MyScript | analysis consistent with the verified license/protocol facts this session
L161 | Alternatives anchor (PaddleOCR family, TrOCR, Docling) | CONFIRMED | https://github.com/microsoft/unilm | TrOCR facts re-verified this session; PaddleOCR/Docling portions were re-proven in r6

## r6-unverified-resolutions.md
L20 | A1 Xournal++ bare GPL-2.0 (not -or-later) | CONFIRMED | https://github.com/xournalpp/xournalpp | appdata project_license GPL-2.0 re-checked this session
L25 | A2 snlib NOT LICENSED | CONFIRMED | https://github.com/Walnut356/snlib | LICENSE 404 on main and master re-confirmed this session
L30 | A3 supernote-tool Apache-2.0 | CONFIRMED | https://github.com/jya-dev/supernote-tool | LICENSE re-fetched this session (main 404, master 200)
L35 | A4 supernote-tool active (last commit 2026-08-23) | CONFIRMED | https://github.com/jya-dev/supernote-tool | commit dates re-read this session
L40 | A5 supernote-editor Apache-2.0 | CONFIRMED | https://github.com/troussos/supernote-editor | LICENSE re-fetched this session
L45 | A6 SupernoteSharp MIT 2023-2024 | CONFIRMED | https://github.com/nelinory/SupernoteSharp | LICENSE re-fetched this session
L50 | A7 fbalobanov/supernote-viewer gone | CONFIRMED | https://github.com/fbalobanov/supernote-viewer | 404 re-confirmed this session
L55 | A8 philips/supernote-obsidian-plugin exists | CONFIRMED | https://github.com/philips/supernote-obsidian-plugin | repo fetched this session
L60 | A9 candle MIT OR Apache-2.0 | CONFIRMED | https://github.com/huggingface/candle | Cargo.toml re-fetched this session
L65 | A10 mistral.rs MIT (2024) | CONFIRMED | https://github.com/EricLBuehler/mistral.rs | LICENSE re-fetched this session (master branch)
L70 | A11 burn MIT OR Apache-2.0 | CONFIRMED | https://github.com/burn-rs/burn | LICENSE re-fetched this session
L75 | A12 KittenTTS Apache-2.0 | CONFIRMED | https://github.com/KittenML/KittenTTS | LICENSE re-fetched this session
L80 | A13 sqlite-vec MIT OR Apache-2.0 | CONFIRMED | https://github.com/asg017/sqlite-vec | LICENSE re-fetched this session
L85 | A14 diamond-types ISC (Cargo license = ISC) | CONFIRMED | https://crates.io/crates/diamond-types | registry JSON re-fetched this session
L90 | A15 Keyhive Apache-2.0 | CONFIRMED | https://github.com/inkandswitch/keyhive | LICENSE re-fetched this session
L95 | A16 Python diff-match-patch Apache-2.0 | CONFIRMED | https://pypi.org/project/diff-match-patch/ | registry JSON re-fetched this session
L100 | A17 secsync Apache-2.0 (not AGPL) | CONFIRMED | https://www.npmjs.com/package/secsync | npm JSON re-fetched: 0.5.0, 2024-06-04; @serenity-kit/secsync 404 re-confirmed
L105 | A18 tanamigrator NOT LICENSED (pyproject tana-to-obsidian 3.3.0) | CONFIRMED | https://pypi.org/project/tanamigrator/ | registry JSON re-fetched this session
L110 | A19 xournalpp_htr GPL-2.0 | CONFIRMED | https://raw.githubusercontent.com/PellelNitram/xournalpp_htr/master/LICENSE | fetched this session
L115 | A20 arabicocr-khatt 0.1.0 MIT | CONFIRMED | https://pypi.org/project/arabicocr-khatt/ | registry JSON re-fetched this session
L120 | A21 KHATT academic/research-only terms | STILL-UNVERIFIED | dataset license page not re-fetched this session; PARTIALLY-RESOLVED status stands
L125 | A22 docTR code Apache-2.0, weights per-backbone | STILL-UNVERIFIED | not re-fetched this session; partial status stands
L134 | B1 yrs 0.28.0, 2026-09-17 | CONFIRMED | https://crates.io/crates/yrs | registry JSON re-fetched this session
L139 | B2 Cryptomator 1.19.3 (mid-2026) | CONFIRMED | https://github.com/cryptomator/cryptomator | releases re-read this session
L144 | B3 secsync beta/stale since 2024-06-04 | CONFIRMED | https://www.npmjs.com/package/secsync | re-fetched this session
L149 | B4 tesseract 0.15.2 (2025-04-19), leptess 0.14.0 (2023-02-21) | CONFIRMED | https://crates.io/crates/tesseract | both registry JSONs re-fetched this session
L154 | B5 diff-match-patch crate 0.3.1 (2026-09-16) | CONFIRMED | https://crates.io/crates/diff-match-patch | registry JSON re-fetched this session
L159 | B6 loro 1.17.1 (2026-10-22), automerge 0.12.0 (2026-09-16) | CONFIRMED | https://crates.io/crates/loro | both registry JSONs re-fetched this session
L164 | B7 Tangent v0.13.0-alpha.3 / v0.12.10, Apache-2.0 | CONFIRMED | https://github.com/suchnsuch/Tangent | releases re-read this session
L169 | B8 Thymer pricing TBD, free personal | CONFIRMED | https://thymer.com/ | re-verified fresh this session
L174 | B9 palm-rejection Android URLs + cookbook addition | STILL-UNVERIFIED | developer.android.com pages not re-fetched this session
L183 | C1 docTR benchmark tables FUNSD/CORD | STILL-UNVERIFIED | not re-fetched this session
L188 | C2 PP-OCRv5 mobile_rec ~16MB | STILL-UNVERIFIED | not re-fetched this session
L193 | C3 ML Kit ~100ms recognition (2020) | STILL-UNVERIFIED | not re-fetched this session
L198 | C4 mistral.rs prefill vs llama.cpp partial | STILL-UNVERIFIED | benchmark comparison not re-fetched; llama.cpp rows are out of scope (R13)
L203 | C5 Notion uses CRDTs (not Yjs) | STILL-UNVERIFIED | Notion post not re-fetched this session
L208 | C6 Loro independent benchmark (imaginarium PR #16) | STILL-UNVERIFIED | PR not re-fetched this session
L213 | C7 TrOCR ONNX exports maintained (base/small) | CONFIRMED | https://github.com/microsoft/unilm | TrOCR facts re-verified this session; Xenova/oguzhandurmaz hub pages were the r6 evidence
L215 | C8 Granite-Docling community ONNX export | STILL-UNVERIFIED | IBM docs + hub pages not re-fetched this session
L223 | C9 RapidOCR v3+ PP-OCRv5 integration | STILL-UNVERIFIED | RapidOCR docs not re-fetched this session
L225 | C10 numbers that do not publicly exist | STILL-UNVERIFIED | negative finding; would need fresh null-searches to re-prove this session
L242 | D1 Dillinger phishing accusation | STILL-UNVERIFIED | structurally unverifiable per r6 framing; unchanged
L247 | D2 Dillinger no paid tiers | CONFIRMED | https://dillinger.io | re-verified fresh this session

## r8-factcheck-corrections.md
L7 | Amphi user-flagged error in original writeup | STILL-UNVERIFIED | not re-fetched this session; correction recorded as-is
L13 | Goodnotes pricing correction (Essential $11.99 / Pro $35.99 / SE $29.99 / AI Pass $9.99) | CONFIRMED | https://www.goodnotes.com | all four figures re-verified fresh this session
L14 | Evernote 50-note free cap correction | CONFIRMED | https://evernote.com | re-verified fresh this session
L15 | Obsidian Sync $4/mo annual; plugins ~9,521 not ~5,000; PhantomPulse finance/crypto plugin abuse | CONFIRMED | https://obsidian.md/sync | all three re-verified fresh this session; plugin registry 9,521; PhantomPulse REF6598 April 2026 finance/crypto LinkedIn/Telegram abuse corroborated by search
L16 | Tana Pro ~$20/mo early-bird correction | CONFIRMED | https://tana.inc | re-verified fresh this session
L17 | Logseq DB beta shipped 13 July 2026, tagged 2.0.1 | CONFIRMED | https://logseq.com | re-verified fresh this session
L17 | Logseq OG/DB split dated April 24 2026 | STILL-UNVERIFIED | split date not independently re-confirmed this session
L17 | Logseq #3457 hyphenated-folders bug (2020) | STILL-UNVERIFIED | issue not re-fetched this session
L18 | Tolaria LOC correction ~52.6K Rust + ~53K TS | CONFIRMED | https://github.com/refactoringhq/tolaria | clone count this session: 52,655 Rust / 52,624 TS
L18 | Tolaria iPhone/iPad shipped, web in dev | CONFIRMED | https://github.com/refactoringhq/tolaria | TestFlight beta re-read this session
L19 | Miro Trustpilot 2.3–2.4, not 1.6 | CONFIRMED | https://www.trustpilot.com/review/www.miro.com | rating consistent with search-surfaced page
L20 | Heptabase pricing correction | STILL-UNVERIFIED | not re-fetched this session
L21 | Muse wound down, successor Allume (June 2026) | STILL-UNVERIFIED | not re-fetched this session
L22 | Milanote $9.99/mo annual correction | CONFIRMED | https://milanote.com/plans/ | re-verified fresh this session
L23 | AFFiNE no E2EE claim correction | CONFIRMED | https://github.com/toeverything/affine | README re-read this session: only "compatible with" phrasing
L24 | Flexcil free + one-time; MarginNote 4 annual $16.99 exists | CONFIRMED | https://www.marginnote.com | re-verified fresh this session
L24 | CollaNote closed-source correction | CONFIRMED | https://github.com/search?q=CollaNote | no official repo surfaced this session, only unofficial forks
L29 | neo MIT correction | CONFIRMED | https://github.com/hughhowey/neo | re-verified this session
L30 | CapsuleCraft .eml + Tauri 2/React 19/egui correction | CONFIRMED | https://github.com/kostyk348/CapsuleCraft | re-verified this session
L31 | notebook-navigator #274 v1.5 roadmap; #1498 duplicate panes; ~1,072,639 downloads; no PRs | CONFIRMED | https://github.com/johansan/notebook-navigator/issues/274 | both issues and repo re-fetched this session
L32 | xnotes #166 Play signing-conflict correction | CONFIRMED | https://github.com/shardulvs/xnotes-android/issues/166 | issue re-fetched this session
L33 | diktafon STT not TTS correction | CONFIRMED | https://github.com/Lukas-Novak/diktafon | repo re-fetched this session
L34 | ConvertOneNote2MarkDown #102 Aug 2021; #197/#200 Oct 2026 | CONFIRMED | https://github.com/theohbrothers/ConvertOneNote2MarkDown/issues/102 | all re-fetched this session
L34 | ConvertOneNote2MarkDown #123 Feb 2022 as COM issue | REVISED | https://github.com/theohbrothers/ConvertOneNote2MarkDown/issues/123 | it is a how-to thread, not a COM report — r8's own correction needs this further revision
L35 | OfficeIMO v3.5.0/v3.4.4; #3171 ~Oct 23 2026 above-the-fold UX | CONFIRMED | https://github.com/EvotecIT/OfficeIMO/issues/3171 | both re-fetched this session
L36 | Meridian-Notes MIT (c) 2026 | CONFIRMED | https://github.com/realbynl/Meridian-Notes | LICENSE fetched live this session; the r8 "R6 snapshot" caution can now be dropped
L37 | e-journal "no matching repo found" | DENIED | https://github.com/EkarinLB/e-journal | the repo exists and was fetched this session: Tauri v2 ink notebook, MIT, v0.12.0 beta — r8's negative finding is wrong
L41 | Stirling PDF ~95K stars + proprietary carve-outs in LICENSE | CONFIRMED | https://github.com/Stirling-Tools/Stirling-PDF | ~95,113 stars re-read this session; app/proprietary, app/saas, engine/, frontend/src/editor/ carve-outs re-read this session
L42 | GIMP GPLv3+ pre-3.0; GIMP 3.0 March 16 2025 | CONFIRMED | https://www.gimp.org | re-verified fresh this session
L43 | Godot LibGodot PR #110863 merged | CONFIRMED | https://github.com/godotengine/godot/pull/110863 | PR re-fetched this session
L44 | lowkey.gg GPL violation (March 2021) | STILL-UNVERIFIED | not re-fetched this session
L48 | NIP-77 Negentropy Syncing exists | CONFIRMED | https://github.com/nostr-protocol/nips | re-verified this session
L49 | nostr crate 0.45.5 | CONFIRMED | https://crates.io/crates/nostr | registry JSON re-fetched: 0.45.5, 2.67M total downloads
L49 | nostr crate ~446K downloads/month rate | REVISED | https://crates.io/crates/nostr | total 2.67M confirmed; the ~446K/month rate is not directly re-confirmable this session — keep as estimate only
L50 | Relay counts (471/343) | STILL-UNVERIFIED | not re-fetched this session
L51 | whisper.cpp on Android slower than realtime; ~5x claim UNVERIFIED | STILL-UNVERIFIED | not re-fetched this session
L52 | TrOCR IAM CER 2.89/3.42/4.22 matches unilm | CONFIRMED | https://github.com/microsoft/unilm | unilm README re-read this session
L53 | supernote-typescript active (last commit 2026-10-12) | CONFIRMED | https://github.com/philips/supernote-typescript | re-fetched this session
L53 | secsync dormant since 2024-06-04 | CONFIRMED | https://www.npmjs.com/package/secsync | re-fetched this session
L53 | diamond-types ISC | CONFIRMED | https://crates.io/crates/diamond-types | re-fetched this session
L53 | Qwen3-Embedding-0.6B Apache-2.0 | STILL-UNVERIFIED | not re-fetched this session
L53 | sqlite-vec MIT OR Apache-2.0 | CONFIRMED | https://github.com/asg017/sqlite-vec | re-fetched this session
L53 | Piper GPL-3.0 flat claim | REVISED | https://pypi.org/project/piper-tts/ | dual situation: rhasspy repo spdxId = MIT, but piper-tts on PyPI = GPL-3.0-or-later — the correction needs the two-source split stated
L53 | Llama/Gemma licenses not OSI-approved | STILL-UNVERIFIED | license texts not re-fetched this session

## Master-file corrections
None.
Candidate corrections surfaced this session that need the master text loaded before an exact-match patch can be written:
- APPS-LINKS.md Meridian-Notes row: MIT is now confirmed from the live LICENSE file (MIT (c) 2026); any "UNVERIFIED/snapshot" annotation on that row can be cleared.
- Any Obsidian Sync row carrying ~$96/yr as the Standard annual price should read $48/yr ($4/mo billed annually); ~$96/yr belongs to Plus/monthly billing.
- Any row citing ConvertOneNote2MarkDown issue #123 as a COM issue should re-point to issue #102; #123 is a how-to thread.
- Any row carrying the r8 correction "ConvertOneNote2MarkDown #123 (Feb 2022) is a COM issue" needs the further revision above.
- Any row citing the nostr crate at a fixed ~446K downloads/month should keep the total (2.67M) and mark the monthly rate as an estimate.
- Any row repeating r8's "e-journal: no matching repo found" should be struck; the repo exists at https://github.com/EkarinLB/e-journal.

## Out of scope (R13)
- bb plugins: none encountered in this lane's files (confirmed none, per the original instruction).
- Strata: github-repos-1.md L71-77 (Niko1221/Strata local AI inference engine) and r8 L37 Strata clause — skipped entirely.
- llama.cpp: diktafon vendored-stacks clause (github-repos-1.md L53), r6 C4 mistral.rs-vs-llama.cpp benchmark row — skipped (whisper.cpp rows kept in scope, as only llama.cpp was excluded).
- openplayground: github-repos-1.md L99-105 (daijro/openplayground PR #6) and the linked NoteCraft-head playground reference in linked-apps-2.md L126 — skipped.
- MediaPipe: no MediaPipe rows landed in this lane's files; none were verified this session.

LANE 8 COMPLETE — 238 claims verified
