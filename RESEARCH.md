# RESEARCH.md — Notes App Research (Round R2)

Synthesis of Phase 1 research. Raw findings live in `research-material/findings/` (one file per lane, every claim cited there); original sources live in `research-material/`. This file holds the conclusions and the open questions only.

## Sources and lanes

- `research-material/findings/community-digest.md` — feature-request digest of the 1412 Discord messages, grouped by theme, every claim traceable to a message id, no usernames.
- `research-material/findings/github-repos-1.md`, `github-repos-2.md` — 27 GitHub repos investigated (links from the community + the 8 remade.wiki pages' projects).
- `research-material/findings/linked-apps-1.md`, `linked-apps-2.md` — ~58 product/project pages including remade.wiki, monogr.ph spec doc, Obsidian plugins, Ink & Switch essay.
- `research-material/findings/thread-a-sync.md` — Thread A answer (sync/CRDT), includes a measured benchmark (`research-material/benchmarks/thread-a/`).
- `research-material/findings/thread-b-storage.md` — Thread B answer (storage).
- `research-material/findings/thread-c-local-models.md` — Thread C answer (small local models).
- `research-material/findings/thread-d-indexing.md` — Thread D answer (indexing cost of universal search).
- `research-material/findings/thread-e-handwriting.md` — Thread E answer (handwriting/OCR on-device).
- `research-material/findings/thread-f-editor-platform.md` — Thread F answer (editor cores, shell, embedded-block threat model).
- `research-material/findings/thread-g-trust-ux.md` — Thread G answer (trust and UX unknowns).

Exclusions honored: getbb.app and the whole "bb" plugin ecosystem were dropped from research per user instruction.

## What the community wants (strongest signals)

1. A Rust-native, Electron-free notes app (381 reactions on the opening request).
2. Freeform OneNote-style canvas with freely placed, resizable, layered blocks.
3. Stylus handwriting with pressure, ink-to-shape, palm rejection, stored as plain files.
4. On-device searchable handwriting, stated as the deal-breaker for leaving OneNote.
5. OCR across images/PDFs/voice/video with local ML (ente cited as the model).
6. Markdown-native storage plus Obsidian vault compatibility.
7. Plugin system, graph view, MCP/agent access borrowed from Obsidian's model.
8. Sync via the user's own cloud on plain files; git sync; self-hosting; user-chosen encryption.
9. A Goodnotes-class open-source tablet app (an entire second community channel exists for this).
10. Native Android/iPadOS; skepticism of wrapper ports.
11. Open source is non-negotiable, especially in the handwriting lane.
12. Migration: .one/.onepkg import, 15 years of notes, universal export.
13. Collaboration wanted but feared as the feature "that kills every notes app".
14. Power-user features: inline LaTeX, real tables, shapes/diagrams, RTL/Arabic support.
15. Interface pluralism: user-picked UI (ribbon, file tree, handwriting mode) over one lean shell.

## App landscape patterns

- The stack of the closest siblings is Rust + no webview or Tauri, plain files or block store, Tantivy/SQLite search: CapsuleCraft (.eml capsules + blocks.json, E2EE on roadmap), Meridian-Notes (custom Rust GUI, canvas, ink as SVG), HelixNotes (Tauri, .md, Tantivy, WebDAV), jpzk/opensidian (Tauri v2 vault clone), notecraft (pure Rust OneNote reimplementation with measured feature parity, 61/67).
- AFFiNE is the reference for the canvas↔document duality: blocks carry stable identity with views, so a note can be DocOnly, EdgelessOnly, or both. BlockSuite over Yjs/y-octo.
- E2EE + local-first sells at consumer scale (Anytype, ente, Lockbook). Ente runs on-device CLIP/face models with encrypted synced indexes; the pattern for private universal search inside E2EE.
- Handwriting: MyScript is the commercial moat (66 languages, no RTL); its archived JS SDK and reverse-engineered format repos show lock-in cost. Ink must stay stable-ID vector strokes so HTR can attach later.
- Migration and ink fidelity: ConvertOneNote2MarkDown (766 stars) issues are dominated by lost ink strokes and COM failures; onenote_parser (Rust) exists for .one import.
- Recurring wish across apps: MCP/agent access (three repos added it independently), per-block provenance (Proofeditor), living calculations (obsidian-numerals).
- Remade.wiki wave: open-notebook (40.6k stars, MIT) shows demand scale for revived apps; notecraft (Rust) and CapsuleCraft are early-stage siblings.

## Thread A answer: sync and conflict resolution

Measured (2-core box, scripts in `research-material/benchmarks/thread-a/`): Yjs merged 10,000 concurrently-edited 500-char docs in 0.14 s, 100% converged, ~518 B/update. Automerge 2.0-alpha needed ~1.15 ms/doc and exhausted memory at 10k (Automerge 3, July 2025, targets that). Loro wasm failed to load on Node 22 here (environment problem, flagged). Diamond Types is effectively unmaintained.

Best-evidence answer: hybrid, with CRDTs carrying note content. E2EE CRDT sync is a solved, shipping pattern with client-side merge: relay stores ciphertext plus unencrypted commit hashes/heads so it can plan sync without reading content. Proof: Ink & Switch Keyhive notebook 05 (sedimentree, RIBLT, BeeKEM) and Loro's %ELO protocol (CI-tested Rust↔TS E2EE interop). Ilow Sync ships Loro+AES-GCM for Obsidian vaults. Lockbook proves Rust+E2EE+offline but is file-level, not CRDT. Yjs has no first-party E2EE.

Conflict files don't survive the spec: Obsidian actually defaults to auto-merge, and its forums document silent bad merges and overwritten newer data; conflict frequency scales with offline duration and device count, exactly our scenario. Keep-both remains right only for binary attachments.

Engine pick on current evidence: Loro (first-party E2EE + protocol spec) or Automerge (deepest ecosystem, Beelay pre-1.0). The staffing risk is key agreement and client-side compaction, not the CRDT itself.

## Thread B answer: storage

Every app that needs stable block references converged on a block store with IDs: Trilium (SQLite), Anytype (encrypted blocks), Tana (cloud DB), AFFiNE/BlockSuite (Y.Map block tree), Heptabase, Logseq DB, Ideon (Docker DB). The file-first survivors paid for it: Obsidian pushes all non-content metadata to sidecars; Logseq's blocks-on-lines Markdown was non-portable and produced an unrecoverable data-loss defect, and Logseq's own April 2024 post explains why it abandoned files-as-store (block insert rewrites whole files, no stable IDs) — its promised two-way markdown sync is still unshipped two-plus years later.

The live canvas↔note bridge ships only within one store: Obsidian Canvas (JSON references note files; edits live both ways), Heptabase (card = note), AFFiNE edgeless (same Y.Map). Nobody ships a live two-way bridge across a block-store↔external-folder boundary.

Recommendation: block store as primary; canvas layout as a JSON Canvas-style artifact keyed by block IDs (making the bridge free); guaranteed-lossless export (store JSON + Markdown + .canvas) as the longevity guarantee; a Thymer-style two-way plain-file mirror only if staged (documents first, one-way export first), with Logseq's record as the warning.

## Thread C answer: the small local model

All four capabilities can be met fully on-device with permissive open weights. LLM: Qwen3-4B-Instruct-2507 (Apache 2.0, 2.5 GB at Q4_K_M, 256K context) as the laptop default, SmolLM3-3B as the lighter alternative; avoid Gemma 3n despite its best phone architecture (MatFormer/PLE) because its custom Terms of Use and reported remote-restriction clause are the worst license fit for an open-source-bound app. STT tension resolved: Whisper-class STT on-device is real at tiny/base tiers (whisper.cpp: tiny 31-75 MB, base 57-142 MB, MIT); Whisper-small-class quality is not a comfortable phone base-install, so the honest stack is Moonshine tiny/base (MIT, streaming-native, English-first) as default, whisper tiny/base for multilingual, whisper small as an optional download. Apple's SpeechAnalyzer matches mid-tier Whisper on iOS 26 but is a closed system asset: disclosure-level accelerator only, never the cross-platform answer. TTS: Kokoro-82M (Apache 2.0) for quality; Piper for low-resource, noting the engine's development moved from MIT to GPL, which changes bundling obligations. Reproducible phone tokens/sec for 3-4B models: nobody has published it (best anchors: about 12 tok/s for 3B Q4 on a Pixel 9 Pro CPU); our own benchmark is mandatory. Per-model license hygiene required: some Moonshine legacy non-English models are non-commercial.

## Thread D answer: the indexing cost of the search promise

The text/code index is cheap and solved (Tantivy-class BM25, minutes at Wikipedia scale); all real cost lives in media understanding. Every comparable app quietly cheats on "always": Evernote's OCR is server-side, paid-tier, capped at 52 MB and lost on export; Notion's search is cloud-only Elasticsearch with multi-week gap-ridden rebuilds; Obsidian Omnisearch is desktop-only with OCR behind a separate plugin and no video or audio; DEVONthink is macOS-only and advises indexing only "fairly static" locations. Video search is the hole in everyone's promise. The proposed frame-OCR-of-sampled-frames approach is precedented (fixed-1 FPS frame scouts and per-frame consolidation pipelines), but desktop-class only: per-frame CPU OCR at roughly 383 ms/frame puts video at about 15-30 CPU-hours per GB at 1 FPS, the dominant cost by far. Scanned-PDF OCR runs about 1-3 CPU-hours per GB; audio via whisper.cpp base is under an hour per GB. On-device is real for images (Apple Vision, milliseconds, no network) and plausible for audio at small tiers; it is not real for video OCR on phones. Evidence supports a desktop/background-queue design with server fallback for mobile, which is exactly the pattern the market leaders use invisibly.

## Open questions (next)

1. Threads C-G answered below; remaining sub-questions per thread listed there.
2. From Thread A: key-agreement scheme choice (BeeKEM vs alternatives); Lockbook-style conflict behavior documentation.

## Thread E answer: handwriting and OCR on-device

MyScript is quote-priced and proprietary (free tiers cap at 2,000 cloud requests / 25 on-device dev licenses; deploy requires a sales contract) and relegates Arabic/Farsi/Hebrew/Urdu to offscreen batch recognition, not live ink. The one free on-device competitor is Google ML Kit Digital Ink Recognition: 300+ languages including Arabic, entirely on-device, but Android/iOS only with closed Google-served models. Wacom's SDK is signature-only; Microsoft Ink Recognizer is a research project. Open models are not page-level: TrOCR reaches 2.89-3.42% CER on IAM but only on cropped single text lines; PARSeq is scene-text; Arabic HTR is starved of data (KHATT is 1,000 pages) with only line-level community models, so no open option is production-grade for Arabic handwriting. Tesseract scores 20-40% on handwriting and PaddleOCR about 72.8%, both far below interactive-ink quality; docTR has no handwriting models at all. Recommendation: ship layered on-device recognition (ML Kit/Apple on mobile, TrOCR-ONNX line-level on desktop/web), make Arabic/RTL a differentiator instead of an afterthought, avoid MyScript's licensing, and do not promise photo-of-paper transcription yet.

## Thread F answer: editor and platform guts

BlockSuite is the only core with native canvas+doc duality (page and edgeless docs are isomorphic block trees, no conversion on mode switch); TipTap has the strongest demonstrated bridge both ways (tldraw uses TipTap for text, and a tldraw node runs inside TipTap docs); ProseMirror can be bent only via a full non-DOM view rewrite with the framework author flagging accessibility as the hardest unsolved cost; no canvas pathway found for Lexical (UNVERIFIED at depth). Shell numbers (best benchmark found): Tauri 8.6 MiB vs Electron 244 MiB bundle, about 172 vs 409 MB RAM across six windows; Tauri's risk concentrates on Linux/WebKitGTK (documented canvas FPS collapse) and macOS WKWebView jank, while WebView2 is near-Chromium, and several shipping Excalidraw-Tauri apps prove medium-weight canvases. Embedded blocks threat model delivered (grounded in the 2026 Obsidian vault RAT campaign and a frontmatter-to-JS-evaluator RCE): terminal = plugin-only with per-block grants (node-pty runs at parent privilege); webhook receiver = core-enforced invariants (loopback-only bind, per-launch token, Host allowlist, against a recurring DNS-rebinding finding class) with plugin-granted handlers; cron = core timers over granted actions only (a schedule is persistence). Synthesis: a hybrid grant model where core owns invariant enforcement plus a revocable per-note/per-block grant ledger persisted outside the note, and plugins own features.

## Thread G answer: trust and UX unknowns

No published threshold exists for how much automatic filing people tolerate; the transferable findings are trust-in-automation theory (calibrated trust, overuse/disuse), NN/g's visibility-and-user-control heuristics, and the control-before-activation pattern (paused/shadow/enforce stages with decision history) seen in DEVONthink's suggest-vs-auto-classify split and email-rule UIs. On-device face recognition has a shipping trust pattern: Apple's "on device, without accessing your photos" framing plus Secure Enclave for biometric templates, and Ente's explicit negatives list (servers never receive unencrypted photos, face data, or indexes; E2EE-synced indexes; local-processing toggle); neither vendor documents the stolen-index/embedding threat model, which stays an open risk. Video-editing ambition maps to a six-level ladder (trim, captions, silence/filler removal, agentic multi-edit, multi-track, compositing/generative) with scope cost rising sharply after level three. Trust communication patterns that work: specific negative claims, open source plus published audits, and in-product receipts. Six questions are explicitly user-testing territory, including the tolerance ceiling, silent-merge vs conflict-file preference, and which ambition level users want.
3. From Thread B: round-trip block-identity encoding for export; mirror conflict policy; whether canvas regions are first-class notes.
4. From Thread C: own benchmark of Qwen3-4B and Moonshine/whisper tiers on target laptop and phone hardware; per-model license check before bundling.
5. From Thread D: frame-rate-vs-recall tuning for video OCR; Android NPU STT feasibility; re-index behavior after media edits.
6. From Thread E: whether ML Kit's closed Google-served models pass the zero-knowledge bar for mobile ink; on-device Arabic HTR watchlist.
7. From Thread F: BlockSuite custom-block maturity; heavy-canvas FPS spikes on WKWebView/WebKitGTK; whether to dual-shell (Tauri + Electron for Linux).
8. From Thread G: user testing needed on tolerance ceiling, conflict UX preference, and video-ambition level.
9. UNVERIFIED items to re-check later: NicTanghe/BasScript, ThatSheepGuy22/ObbyNotes, an unreachable OfficeIMO fork (handle withheld),gitea sawt, strongcod3r/laplace, Bouquet page, two X posts, one YouTube video, MyScript pricing page (JS shell), OneNote web (JS shell).
10. GitHub online copy established (private at R2b, now public per user request); each future round pushes after a passing secret check.

## Round R4 additions

Two new repo-root master files land this round, per user instruction to "leave links to all the apps in a .md file along with all the features in another .md file": APPS-LINKS.md (217 items in 9 categories, one line each: name, URL, description, open-source status with license, findings-file pointers; UNVERIFIED items flagged; similar-named distinct repos listed separately) and FEATURES.md (Part I: 16 apps feature-by-feature with wants/changed and sources; Part II: 13 repos + 11 integration components; Part III: 55-item community wish list plus feature clusters). No build plan was made, per user instruction ("dont make a build plan just yrt").

## R4: the third Discord thread

A new export (Notion app-requests thread, 22 messages, 29 links) was parsed with a new parser: this export uses UNQUOTED HTML attributes, so the earlier quoted-attribute parser silently found 0 messages; always inspect raw markup before parsing a new export variant. Core want: a self-hostable, no-paywall Notion-class app with user-chosen cloud backends (Google Drive/Dropbox/OneDrive) and anti-lock-in. AFFiNE gaps cited by users: no Excel-like in-cell functions, no one-database-many-views, ambiguous on-premise storage limits, cloud-only AI. The community's "gold formula" quote: Anytype on-premise with Notion UX. A detailed requirements list (one member) wants paragraph-level links surviving moves, encrypted local backup, readable-format auto backup, phone sync, standard-format export, checkboxes/images/color, privacy when synced, code formatting, with AI chat as nice-to-have. Also present: p2panda relay mention, and a Notion-meets-QuickBase vision with online/offline sync.
Sources: findings/thread3-digest.md, research-material/discord-thread3-transcript.txt

## R4: MyScript / Nebo reverse engineering

Verdict: MyScript's recognition cannot be pulled from anything public. MyScriptJS (archived, Apache-2.0) contains only ink capture/rendering/transport glue; recognition runs behind developer keys. A published apktool+jadx teardown of Nebo Android (~31,045 classes) shows Nebo is a thin Java/SWIG shell over proprietary native engines (libMyScriptEngine Text/Math/Shape/Gesture) plus proprietary resource bundles: an architecture donor, not an algorithm donor, and nothing binary redistributable. Nebo's .bink stroke format has no published parser (Xournal++ issue #5730). No open MyScript reimplementation exists; xournalpp_htr (GPL-2.0, CRNN/CTC with stroke dynamics) is research-grade self-built HTR; RNote has no HTR. No DMCA takedowns found. Actionable shape: implement the MyScript interface contract (incremental strokes in, partial recognition out, JIIX/MathML/LaTeX export) against local engines (ML Kit, xournalpp_htr models); never touch APK artifacts.
Sources: findings/myscript-nebo-reverse.md

## R4: integration components verdict (license first)

Excalidraw (MIT) is the cleanest true embedded view (React component in webview, weight S). Godot (MIT) is embeddable via LibGodot/libgodot (M-L). libVLC (LGPL-2.1, FFI) workable (M); Kdenlive via the MLT engine (LGPL-2.1, M) with the editor UI out of scope. ONLYOFFICE is AGPL-3.0: a license blocker for native embedding, iframe/WebView embed only (L). Audacity GPLv3 has no library/headless mode; OBS libobs GPL-2.0+ infects the host (Streamlabs precedent); GIMP GPL-3.0 headless/ScriptFu only; Krita plugins-only; Blender GPL-2.0+ headless via bpy. GPL-family components are therefore file-level or sidecar integrations only, never in-process. Photopea is closed source despite the free web app: disqualified. Stirling PDF is open-core (MIT essentials + proprietary folders), file-level (S-M).
Sources: findings/integrations-1.md

## R4: OneNote-style pen/keyboard/touch auto-switching

User-requested feature, researched to architecture level. OneNote Windows ships "Automatically switch between inking, selecting, typing and panning" (File>Options>Advanced>Pen); iPad has "Draw with Touch"; Android has "Ignore touch input when using stylus". Best architecture reference is tldraw: reject non-pen pointers BEFORE they update input state (a public fix, PR #10346, addressed the exact ordering bug). Platform hooks: Windows WM_POINTER pointerType + POINTER_PEN_INFO; iOS UITouch.type + UIPencilInteraction + PencilKit drawingPolicy; macOS tabletPoint/Proximity; Android getToolType + ACTION_CANCEL palm cancel + contact-size heuristic; Linux libinput palm detection. Web pitfalls found: Firefox flipped pen to touch mid-stroke historically, and passive capacitive styluses are indistinguishable from fingers (pressure/width fallbacks needed). Working ruleset: pen in range means touches become navigation only (pan/zoom/scroll); last-used pen persists across lifts; finger-draw toggle and palm-rejection presets as user overrides. rnote (GPL-3.0, Rust/GTK4) is a study reference; tldraw is source-available with a proprietary license, so no production code reuse, concepts only.
Sources: findings/input-mode-switching.md

## R4: tolaria.md

Tolaria (github.com/refactoringhq/tolaria) is AGPL-3.0-or-later, Tauri v2, roughly 100K LOC of Rust+React (mostly AI-written), plain .md files with YAML frontmatter, no accounts/servers, git-as-sync with opt-in AutoGit, Notion-like block editor plus raw mode, types-as-lenses, YAML custom views, tldraw whiteboards, Mermaid, sandboxed HTML blocks, Cmd+K palette, and AI-first design (OpenAI/Anthropic/Gemini/Ollama/LM Studio, CLI agent targets, bundled MCP server, AGENTS file). Reception: praise for UI polish, git-as-AI-transparency, and 10K-note scale; complaints about the Tauri web-wrapper feel, feature creep, and early bugs. Concepts and interactions are freely liftable; reusing its code binds the host project to AGPL.
Sources: findings/tolaria.md

## R4: per-app likes/wants (headline signals)

Notability's ink is time-locked to audio (tap a stroke to jump the recording): its most irreplaceable feature. ConvertOneNote2MarkDown (766 stars) still exports each OneNote ink stroke as a positionless image although the COM API GetPageContent carries stroke positions plus ISF: ink-preserving OneNote import is a genuine open differentiator. Goodnotes 6 AI ink-smoothing deforms users' handwriting: on-device AI that touches user strokes needs a findable off switch. Noteshelf charged lifetime v2 buyers again for v3: pricing-trust caution. April 2026 Obsidian "Phantom in the Vault" campaign: a crafted vault plus a legitimate plugin config executed attacker commands on vault open, meaning vault files themselves are an attack surface.
Sources: findings/apps-likes-wants.md

## R4: repo inventory resolutions

NicTanghe/BasScript does not exist (canonical counterpart: BaseScript.lang, irrelevant to this project). ThatSheepGuy22/ObbyNotes is not findable. slogsdon/bb-tui resolves to bborn/bb-tui (Go); a community member's OfficeIMO fork resolves to EvotecIT/OfficeIMO (MIT, .NET). Top liftable Rust-first assets: realbynl/Meridian-Notes (native Rust editor architecture, license to confirm), AlienTechSoftware/notecraft (Rust core/UI split, MIT/Apache-2.0, alpha 0.0.6), EkarinLB/e-journal (egui + encryption-at-rest, MIT), Niko1221/Strata (localhost LLM API pattern, MIT), gtg922r/obsidian-numerals (math engine as pure module, MIT, ~600 stars), hughhowey/neo (plain-file data model, MIT, ~1.6k stars), johansan/notebook-navigator (virtualized 100k-note browser; GPL-3.0 so spec-only, 2,782 stars / 1M+ downloads), kostyk348/CapsuleCraft (.eml-per-note storage, MIT). AFFiNE deep dive: BlockSuite duality, OctoBase sync, MIT.
Sources: findings/deep-repos-a.md, findings/deep-repos-b.md, findings/deep-repos-c.md

## R5: the study/PDF-textbook angle (BookCraft idea) and IdeaCraft

Trigger: the user supplied one new link (aamirenic/IdeaCraft) plus a full community-submitted app idea (BookCraft: a dedicated stylus study space over notebooks and PDF textbooks, Drawboard-PDF-level inking, organized by subject or course), and asked again whether every app, link and feature truly got in-depth coverage. Coverage audit answer, stated honestly: every link known at R4 was inventoried and every major app got a deep dive, but depth was tiered (30 repos and 16 apps deep; smaller links inventory-level; a few member-hosted repos unfindable). R5 covers the new material at full depth.
IdeaCraft (aamirenic/IdeaCraft, MIT): days-old local-first Tauri 2 + Rust notes app: SQLite, block editor with Markdown shortcuts, page history, search palette, templates, export/backup, sync folder, opt-in local Ollama, minisign auto-updates; Windows-only v1.0.0 (2026-10-23), no handwriting or mobile. Pull-from under MIT: the SQLite schema (db.rs), the Tauri command layer (commands.rs), the sync-folder design, the smoke-test harness. Unrelated namesake repo rickyb82/ideacraft (Rust mind-map canvas) is a likely confusion source. Not part of the ArtCraft family, whose 13-app pure-Rust lineup bans webviews.
Drawboard PDF: the community's inking reference: pressure ink over Windows Ink, virtual-paper feel, dockable tool favorites, best-in-class palm rejection, calibrated measurement tools; closed source; eroding goodwill from the 2023 subscription switch (pressure ink moved behind Pro) and long-session performance rot. Lesson: pair Drawboard-level ink quality with a different structure and a trustworthy pricing model, not a feature clone.
Study/PDF-textbook landscape (Flexcil, LiquidText, CollaNote, MarginNote 4, Xodo, PDF Expert, plus the Goodnotes/Notability/OneNote textbook angles and newer entrants Write, University Notes, Zotero): the common load-bearing feature set is a course-organized library, pen/highlighter plus text-layer highlighting, excerpt-to-note linking back to source pages, split view, handwriting search, lossless annotated export, annotation-based study aids. Loudest wants: working sync, ink smoothing, pixel eraser and shapes, layers, large-textbook performance, annotation write-back, stable pricing. Verdict: the unified dedicated study notebook over textbooks is a real but contested gap; documented traps are subscriptions, buggy updates, large-PDF performance and sync.
Sources: findings/r5-ideacraft.md, findings/r5-drawboard-pdf.md, findings/r5-study-apps-landscape.md

## R6: the full-depth sweep (every remaining inventory item)

Trigger: the user's directive "I dont want varied, I want everything to be reasearched in full and in depth" turned R2-R5's tiered depth into a defect. R6 covered every remaining inventory item at full depth in three waves of subagent lanes, producing 12 findings files (~540 KB), then a verify pass dispositioned every UNVERIFIED marker.

Wave 1 (minor apps, editors, sync): Squid, Concepts, Saber, Workflowy, DEVONthink, ente, Kinopio, then 15 more (Muse/Allume, Thymer, Ideon, OwlLuna, Akasha, Poznote, Tangent, HelixNotes, Lockbook, Pele-not-found, Obsidian Publish pricing backlash, the caption-tool landscape), then editors and publishers (Dillinger, Ghost, Homebrewery, proofeditor, the Amphi disambiguation, the Samsung Notes deep dive), then the sync/CRDT+E2EE stack (BeeKEM, Loro protocol-e2ee, any-sync, secsync, p2panda; Rust-native yrs, Loro, iroh, automerge core, nostr-sdk; 263 URLs cited).

Wave 2 (handwriting and local AI): HTR/OCR engines measured on real benchmarks (TrOCR best open HTR; Tesseract disqualified for handwriting at 49.58% CER; docTR, PaddleOCR, docling, paperless-ngx, ocrmypdf, OnlineHTR, ArabicOCR_KHATT with the KHATT/LDC licensing checkpoint); Xournal++, RNote (license corrected to GPL-3.0-or-later), the fully reverse-engineered Supernote .note format; palm rejection documented per platform; small local LLMs, STT, TTS and RAG with a pre-ship license checklist.

Wave 3 (Obsidian plugins, OSS batch D, Nostr): 16 plugins license-verified at each repo (Templater carries a genuine license conflict needing a human check before any pull decision); jpzk/opensidian identified as the closest existing project to ours (Rust+Tauri clean-room Obsidian clone); Nostr judged concepts-only for sync with negentropy set-reconciliation and NIP-44 discipline worth pulling regardless; iroh the stronger Rust-native p2p lane.

Verify pass: 34 entries tracked, 22 resolved, 5 partially, 7 not found. License corrections applied (diamond-types ISC, secsync Apache-2.0 and dormant, snlib and TanaMigrator no-license-unpullable). The "Notion uses Yjs" adoption claim was dropped for lack of a source. Coverage-audit statement updated: the full-depth sweep is complete; every inventoried link now has full-depth research or a documented not-found disposition.

Sources: the twelve findings/r6-*.md files.

## R7: per-app feature inventories, internet-wide sentiment, remake landscape, and the user's 11 supplied repos

Trigger: the user's standing demand for the most in-depth research plus 11 newly supplied repos with the instruction "research all of these in depth every feature, etc." Six subagent lanes ran (three had been cancelled by a plan limit in the first attempt and were relaunched successfully).

Feature inventories: the majors lane (20 apps, Obsidian through tldraw) completed with a 4-app top-up (DEVONthink, Kinopio, Concepts, tldraw) after its first run was cancelled; the OSS lane (19 apps, Logseq through Tangent Notes); the handwriting/study lane (19 subjects, completed in the earlier run) covering the stored-ink vs live-conversion vs search-only split of HWR, pricing-model transitions as the dominant complaint pattern, and the finding that no app in the batch claims E2EE. Every captured claim carries a URL; gaps are marked UNVERIFIED this session.

Internet-wide sentiment sweep: Reddit (r/NoteTaking, r/PKMS, r/ObsidianMD, r/Notion, r/Evernote, r/logseq, r/GoodNotes, r/selfhosted), HN evidence from search-indexed threads (hn.algolia.com JSON fetches were blocked), app-store review patterns via community threads (store pages not crawlable this session). Result: 8 ranked demands each with 2+ independent sources, 3 single-source items quarantined as unconfirmed, plus praise patterns, pricing-resentment patterns, handwriting-specific sentiment, an honesty check on local-first/E2EE demand, and a migration-pain section.

Remake landscape: 33 projects mapped. 17 verified alive, 13 verified dead/dormant with evidence, 3 unresolvable this session. Four death patterns: vendor adopt-then-drop (Focalboard), single-maintainer exit (Notea, Athens), incumbent-API dependence (NixNote2, Geeknote, Everpad), acqui-deletion (Skiff).

User repos lanes: all 11 supplied repos researched at repo HEAD plus releases, issues, and community reception. Batch A: turtl/desktop, Zettlr, QOwnNotes, blinko, edgeever, notion-re. Batch B: zappynotes, owlistic, NexaNote, memos, siyuan. SiYuan received the deepest treatment: Go kernel + Electron shell, .sy block-JSON files, FTS5, SQLCipher option, dejavu snapshot repo with repo-key E2EE over official cloud/S3/WebDAV/local, attribute views, riff flashcards, MCP server, paid sync gating. Pull-from verdicts recorded per repo in FEATURES.md.

Sources: findings/r7-feature-inventory-majors.md, findings/r7-feature-inventory-oss.md, findings/r7-feature-inventory-handwriting.md, findings/r7-user-sentiment-sweep.md, findings/r7-remakes-evernote-notion.md, findings/r7-user-repos-a.md, findings/r7-user-repos-b.md
