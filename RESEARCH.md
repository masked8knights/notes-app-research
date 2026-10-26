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
10. GitHub online copy established (private repo, see MILESTONES R2b); each future round pushes after a passing secret check.
