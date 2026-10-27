# RESEARCH.md: Notes App Research (through R7 synthesis; see project/MILESTONES.md for R8/R9)

Synthesis of Phase 1 research. Raw findings live in `research-material/findings/` (one file per lane, every claim cited there); original sources live in `research-material/`. This file holds the conclusions and the open questions only.

## Sources and lanes

| Topic / question | What the research found | Evidence |
|---|---|---|
| Community digest | Feature-request digest of the 1412 Discord messages, grouped by theme; every claim traceable to a message id, no usernames. | research-material/findings/community-digest.md |
| GitHub repos | 27 GitHub repos investigated (links from the community plus the 8 remade.wiki pages' projects). | research-material/findings/github-repos-1.md, github-repos-2.md |
| Linked apps | ~58 product/project pages including remade.wiki, monogr.ph spec doc, Obsidian plugins, Ink & Switch essay. | research-material/findings/linked-apps-1.md, linked-apps-2.md |
| Thread A (sync/CRDT) | Answer includes a measured benchmark. | research-material/findings/thread-a-sync.md; research-material/benchmarks/thread-a/ |
| Thread B (storage) | Answer lane. | research-material/findings/thread-b-storage.md |
| Thread C (small local models) | Answer lane. | research-material/findings/thread-c-local-models.md |
| Thread D (indexing cost of universal search) | Answer lane. | research-material/findings/thread-d-indexing.md |
| Thread E (handwriting/OCR on-device) | Answer lane. | research-material/findings/thread-e-handwriting.md |
| Thread F (editor cores, shell, embedded-block threat model) | Answer lane. | research-material/findings/thread-f-editor-platform.md |
| Thread G (trust and UX unknowns) | Answer lane. | research-material/findings/thread-g-trust-ux.md |
| Exclusions honored | getbb.app and the whole "bb" plugin ecosystem were dropped from research per user instruction; the one quality worth carrying over is how malleable getbb.app is as a platform. | (user instruction) |

## What the community wants (strongest signals)

| Topic / question | What the research found | Evidence |
|---|---|---|
| Core ask | A Rust-native, Electron-free notes app (381 reactions on the opening request). | community-digest.md |
| Canvas | Freeform OneNote-style canvas with freely placed, resizable, layered blocks. | community-digest.md |
| Handwriting | Stylus handwriting with pressure, ink-to-shape, palm rejection, stored as plain files. | community-digest.md |
| Handwriting search | On-device searchable handwriting, stated as the deal-breaker for leaving OneNote. | community-digest.md |
| OCR | OCR across images/PDFs/voice/video with local ML (ente cited as the model). | community-digest.md |
| Storage | Markdown-native storage plus Obsidian vault compatibility. | community-digest.md |
| Extensibility | Plugin system, graph view, MCP/agent access borrowed from Obsidian's model. | community-digest.md |
| Sync | Sync via the user's own cloud on plain files; git sync; self-hosting; user-chosen encryption. | community-digest.md |
| Tablet app | A Goodnotes-class open-source tablet app (an entire second community channel exists for this). | community-digest.md |
| Mobile | Native Android/iPadOS; skepticism of wrapper ports. | community-digest.md |
| Open source | Open source is non-negotiable, especially in the handwriting lane. | community-digest.md |
| Migration | .one/.onepkg import, 15 years of notes, universal export. | community-digest.md |
| Collaboration | Wanted but feared as the feature "that kills every notes app". | community-digest.md |
| Power users | Inline LaTeX, real tables, shapes/diagrams, RTL/Arabic support. | community-digest.md |
| Interface pluralism | User-picked UI (ribbon, file tree, handwriting mode) over one lean shell. | community-digest.md |

## App landscape patterns

| Topic / question | What the research found | Evidence |
|---|---|---|
| Closest siblings' stack | Rust + no webview or Tauri, plain files or block store, Tantivy/SQLite search: CapsuleCraft (.eml capsules + blocks.json, E2EE on roadmap), Meridian-Notes (custom Rust GUI, canvas, ink as SVG), HelixNotes (Tauri, .md, Tantivy, WebDAV), jpzk/opensidian (Tauri v2 vault clone), notecraft (pure Rust OneNote reimplementation with measured feature parity, 61/67). | github-repos-1.md, github-repos-2.md, linked-apps-1.md |
| Canvas-document duality | AFFiNE is the reference: blocks carry stable identity with views, so a note can be DocOnly, EdgelessOnly, or both. BlockSuite over Yjs/y-octo. | linked-apps findings |
| E2EE + local-first | Sells at consumer scale (Anytype, ente, Lockbook). Ente runs on-device CLIP/face models with encrypted synced indexes; the pattern for private universal search inside E2EE. | linked-apps findings |
| Handwriting moat | MyScript is the commercial moat (66 languages, no RTL); its archived JS SDK and reverse-engineered format repos show lock-in cost. Ink must stay stable-ID vector strokes so HTR can attach later. | linked-apps findings |
| Migration and ink fidelity | ConvertOneNote2MarkDown (766 stars) issues are dominated by lost ink strokes and COM failures; onenote_parser (Rust) exists for .one import. | linked-apps findings |
| Recurring wish | MCP/agent access (three repos added it independently), per-block provenance (Proofeditor), living calculations (obsidian-numerals). | github-repos findings |
| Remade.wiki wave | open-notebook (40.6k stars, MIT) shows demand scale for revived apps; notecraft (Rust) and CapsuleCraft are early-stage siblings. | github-repos findings |
## Thread A answer: sync and conflict resolution

Measured on a 2-core box, scripts in `research-material/benchmarks/thread-a/`.

| Topic / question | What the research found | Evidence |
|---|---|---|
| Benchmark | Yjs merged 10,000 concurrently-edited 500-char docs in 0.14 s, 100% converged, ~518 B/update. Automerge 2.0-alpha needed ~1.15 ms/doc and exhausted memory at 10k (Automerge 3, July 2025, targets that). Loro wasm failed to load on Node 22 here (environment problem, flagged). Diamond Types is effectively unmaintained. | research-material/benchmarks/thread-a/ |
| Best-evidence answer | Hybrid, with CRDTs carrying note content. E2EE CRDT sync is a solved, shipping pattern with client-side merge: relay stores ciphertext plus unencrypted commit hashes/heads so it can plan sync without reading content. Proof: Ink & Switch Keyhive notebook 05 (sedimentree, RIBLT, BeeKEM) and Loro's %ELO protocol (CI-tested Rust-TS E2EE interop). Ilow Sync ships Loro+AES-GCM for Obsidian vaults. Lockbook proves Rust+E2EE+offline but is file-level, not CRDT. Yjs has no first-party E2EE. | thread-a-sync.md |
| Conflict files | Don't survive the spec: Obsidian actually defaults to auto-merge, and its forums document silent bad merges and overwritten newer data; conflict frequency scales with offline duration and device count, exactly our scenario. Keep-both remains right only for binary attachments. | thread-a-sync.md |
| Engine pick | On current evidence: Loro (first-party E2EE + protocol spec) or Automerge (deepest ecosystem, Beelay pre-1.0). The staffing risk is key agreement and client-side compaction, not the CRDT itself. | thread-a-sync.md |

## Thread B answer: storage

| Topic / question | What the research found | Evidence |
|---|---|---|
| Block store convergence | Every app that needs stable block references converged on a block store with IDs: Trilium (SQLite), Anytype (encrypted blocks), Tana (cloud DB), AFFiNE/BlockSuite (Y.Map block tree), Heptabase, Logseq DB, Ideon (Docker DB). | thread-b-storage.md |
| File-first cost | Obsidian pushes all non-content metadata to sidecars; Logseq's blocks-on-lines Markdown was non-portable and produced an unrecoverable data-loss defect, and Logseq's own April 2024 post explains why it abandoned files-as-store (block insert rewrites whole files, no stable IDs): its promised two-way markdown sync is still unshipped two-plus years later. | thread-b-storage.md |
| Canvas-note bridge | The live bridge ships only within one store: Obsidian Canvas (JSON references note files; edits live both ways), Heptabase (card = note), AFFiNE edgeless (same Y.Map). Nobody ships a live two-way bridge across a block-store/external-folder boundary. | thread-b-storage.md |
| Recommendation | Block store as primary; canvas layout as a JSON Canvas-style artifact keyed by block IDs (making the bridge free); guaranteed-lossless export (store JSON + Markdown + .canvas) as the longevity guarantee; a Thymer-style two-way plain-file mirror only if staged (documents first, one-way export first), with Logseq's record as the warning. | thread-b-storage.md |

## Thread C answer: the small local model

| Topic / question | What the research found | Evidence |
|---|---|---|
| Overall verdict | All four capabilities can be met fully on-device with permissive open weights. | thread-c-local-models.md |
| LLM | Qwen3-4B-Instruct-2507 (Apache 2.0, 2.5 GB at Q4_K_M, 256K context) as the laptop default, SmolLM3-3B as the lighter alternative; avoid Gemma 3n despite its best phone architecture (MatFormer/PLE) because its custom Terms of Use and reported remote-restriction clause are the worst license fit for an open-source-bound app. | thread-c-local-models.md |
| STT | Whisper-class STT on-device is real at tiny/base tiers (whisper.cpp: tiny 31-75 MB, base 57-142 MB, MIT); Whisper-small-class quality is not a comfortable phone base-install. Honest stack: Moonshine tiny/base (MIT, streaming-native, English-first) as default, whisper tiny/base for multilingual, whisper small as an optional download. | thread-c-local-models.md |
| Apple STT | Apple's SpeechAnalyzer matches mid-tier Whisper on iOS 26 but is a closed system asset: disclosure-level accelerator only, never the cross-platform answer. | thread-c-local-models.md |
| TTS | Kokoro-82M (Apache 2.0) for quality; Piper for low-resource, noting the engine's development moved from MIT to GPL, which changes bundling obligations. | thread-c-local-models.md |
| Missing benchmark | Reproducible phone tokens/sec for 3-4B models: nobody has published it (best anchors: about 12 tok/s for 3B Q4 on a Pixel 9 Pro CPU); our own benchmark is mandatory. | thread-c-local-models.md |
| License hygiene | Per-model license hygiene required: some Moonshine legacy non-English models are non-commercial. | thread-c-local-models.md |

## Thread D answer: the indexing cost of the search promise

| Topic / question | What the research found | Evidence |
|---|---|---|
| Text index | The text/code index is cheap and solved (Tantivy-class BM25, minutes at Wikipedia scale); all real cost lives in media understanding. | thread-d-indexing.md |
| "Always" cheats | Every comparable app quietly cheats on "always": Evernote's OCR is server-side, paid-tier, capped at 52 MB and lost on export; Notion's search is cloud-only Elasticsearch with multi-week gap-ridden rebuilds; Obsidian Omnisearch is desktop-only with OCR behind a separate plugin and no video or audio; DEVONthink is macOS-only and advises indexing only "fairly static" locations. | thread-d-indexing.md |
| Video gap | Video search is the hole in everyone's promise. | thread-d-indexing.md |
| Frame OCR | The proposed frame-OCR-of-sampled-frames approach is precedented (fixed-1 FPS frame scouts and per-frame consolidation pipelines), but desktop-class only: per-frame CPU OCR at roughly 383 ms/frame puts video at about 15-30 CPU-hours per GB at 1 FPS, the dominant cost by far. | thread-d-indexing.md |
| Other media costs | Scanned-PDF OCR runs about 1-3 CPU-hours per GB; audio via whisper.cpp base is under an hour per GB. | thread-d-indexing.md |
| On-device reality | Real for images (Apple Vision, milliseconds, no network) and plausible for audio at small tiers; not real for video OCR on phones. Evidence supports a desktop/background-queue design with server fallback for mobile, which is exactly the pattern the market leaders use invisibly. | thread-d-indexing.md |

## Open questions (next)

| Topic / question | What the research found | Evidence |
|---|---|---|
| Status | Threads C-G answered below; remaining sub-questions per thread listed there. | this synthesis |
| From Thread A | Key-agreement scheme choice (BeeKEM vs alternatives); Lockbook-style conflict behavior documentation. | thread-a-sync.md |
## Thread E answer: handwriting and OCR on-device

| Topic / question | What the research found | Evidence |
|---|---|---|
| MyScript | Quote-priced and proprietary (free tiers cap at 2,000 cloud requests / 25 on-device dev licenses; deploy requires a sales contract) and relegates Arabic/Farsi/Hebrew/Urdu to offscreen batch recognition, not live ink. | thread-e-handwriting.md |
| Free competitor | The one free on-device competitor is Google ML Kit Digital Ink Recognition: 300+ languages including Arabic, entirely on-device, but Android/iOS only with closed Google-served models. | thread-e-handwriting.md |
| Other proprietary | Wacom's SDK is signature-only; Microsoft Ink Recognizer is a research project. | thread-e-handwriting.md |
| Open models | Not page-level: TrOCR reaches 2.89-3.42% CER on IAM but only on cropped single text lines; PARSeq is scene-text; Arabic HTR is starved of data (KHATT is 1,000 pages) with only line-level community models, so no open option is production-grade for Arabic handwriting. Tesseract scores 20-40% on handwriting and PaddleOCR about 72.8%, both far below interactive-ink quality; docTR has no handwriting models at all. | thread-e-handwriting.md |
| Recommendation | Ship layered on-device recognition (ML Kit/Apple on mobile, TrOCR-ONNX line-level on desktop/web), make Arabic/RTL a differentiator instead of an afterthought, avoid MyScript's licensing, and do not promise photo-of-paper transcription yet. | thread-e-handwriting.md |

## Thread F answer: editor and platform guts

| Topic / question | What the research found | Evidence |
|---|---|---|
| Editor cores | BlockSuite is the only core with native canvas+doc duality (page and edgeless docs are isomorphic block trees, no conversion on mode switch); TipTap has the strongest demonstrated bridge both ways (tldraw uses TipTap for text, and a tldraw node runs inside TipTap docs); ProseMirror can be bent only via a full non-DOM view rewrite with the framework author flagging accessibility as the hardest unsolved cost; no canvas pathway found for Lexical (UNVERIFIED at depth). | thread-f-editor-platform.md |
| Shell numbers | Best benchmark found: Tauri 8.6 MiB vs Electron 244 MiB bundle, about 172 vs 409 MB RAM across six windows. Tauri's risk concentrates on Linux/WebKitGTK (documented canvas FPS collapse) and macOS WKWebView jank, while WebView2 is near-Chromium, and several shipping Excalidraw-Tauri apps prove medium-weight canvases. | thread-f-editor-platform.md |
| Embedded blocks threat model | Delivered, grounded in the 2026 Obsidian vault RAT campaign and a frontmatter-to-JS-evaluator RCE: terminal = plugin-only with per-block grants (node-pty runs at parent privilege); webhook receiver = core-enforced invariants (loopback-only bind, per-launch token, Host allowlist, against a recurring DNS-rebinding finding class) with plugin-granted handlers; cron = core timers over granted actions only (a schedule is persistence). | thread-f-editor-platform.md |
| Synthesis | A hybrid grant model where core owns invariant enforcement plus a revocable per-note/per-block grant ledger persisted outside the note, and plugins own features. | thread-f-editor-platform.md |

## Thread G answer: trust and UX unknowns

| Topic / question | What the research found | Evidence |
|---|---|---|
| Filing tolerance | No published threshold exists for how much automatic filing people tolerate; the transferable findings are trust-in-automation theory (calibrated trust, overuse/disuse), NN/g's visibility-and-user-control heuristics, and the control-before-activation pattern (paused/shadow/enforce stages with decision history) seen in DEVONthink's suggest-vs-auto-classify split and email-rule UIs. | thread-g-trust-ux.md |
| Face recognition | On-device face recognition has a shipping trust pattern: Apple's "on device, without accessing your photos" framing plus Secure Enclave for biometric templates, and Ente's explicit negatives list (servers never receive unencrypted photos, face data, or indexes; E2EE-synced indexes; local-processing toggle); neither vendor documents the stolen-index/embedding threat model, which stays an open risk. | thread-g-trust-ux.md |
| Video ambition | Video-editing ambition maps to a six-level ladder (trim, captions, silence/filler removal, agentic multi-edit, multi-track, compositing/generative) with scope cost rising sharply after level three. | thread-g-trust-ux.md |
| Trust communication | Patterns that work: specific negative claims, open source plus published audits, and in-product receipts. | thread-g-trust-ux.md |
| User testing | Six questions are explicitly user-testing territory, including the tolerance ceiling, silent-merge vs conflict-file preference, and which ambition level users want. | thread-g-trust-ux.md |

## Open questions (next), continued (items 3-10)

| Topic / question | What the research found | Evidence |
|---|---|---|
| From Thread B | Round-trip block-identity encoding for export; mirror conflict policy; whether canvas regions are first-class notes. | thread-b-storage.md |
| From Thread C | Own benchmark of Qwen3-4B and Moonshine/whisper tiers on target laptop and phone hardware; per-model license check before bundling. | thread-c-local-models.md |
| From Thread D | Frame-rate-vs-recall tuning for video OCR; Android NPU STT feasibility; re-index behavior after media edits. | thread-d-indexing.md |
| From Thread E | Whether ML Kit's closed Google-served models pass the zero-knowledge bar for mobile ink; on-device Arabic HTR watchlist. | thread-e-handwriting.md |
| From Thread F | BlockSuite custom-block maturity; heavy-canvas FPS spikes on WKWebView/WebKitGTK; whether to dual-shell (Tauri + Electron for Linux). | thread-f-editor-platform.md |
| From Thread G | User testing needed on tolerance ceiling, conflict UX preference, and video-ambition level. | thread-g-trust-ux.md |
| UNVERIFIED re-checks | NicTanghe/BasScript, ThatSheepGuy22/ObbyNotes, an unreachable OfficeIMO fork (handle withheld),gitea sawt, strongcod3r/laplace, Bouquet page, two X posts, one YouTube video, MyScript pricing page (JS shell), OneNote web (JS shell). | this synthesis |
| Repo hosting | GitHub online copy established (private at R2b, now public per user request); each future round pushes after a passing secret check. | this synthesis |
## Round R4 additions

| Topic / question | What the research found | Evidence |
|---|---|---|
| New master files | Two new repo-root master files land this round, per user instruction to "leave links to all the apps in a .md file along with all the features in another .md file": APPS-LINKS.md (217 items in 9 categories, one line each: name, URL, description, open-source status with license, findings-file pointers; UNVERIFIED items flagged; similar-named distinct repos listed separately) and FEATURES.md (Part I: 16 apps feature-by-feature with wants/changed and sources; Part II: 13 repos + 11 integration components; Part III: 55-item community wish list plus feature clusters). | APPS-LINKS.md, FEATURES.md |
| No build plan | No build plan was made, per user instruction ("dont make a build plan just yrt"). | user instruction |

## R4: the third Discord thread

| Topic / question | What the research found | Evidence |
|---|---|---|
| Parser lesson | A new export (Notion app-requests thread, 22 messages, 29 links) was parsed with a new parser: this export uses UNQUOTED HTML attributes, so the earlier quoted-attribute parser silently found 0 messages; always inspect raw markup before parsing a new export variant. | thread3-digest.md |
| Core want | A self-hostable, no-paywall Notion-class app with user-chosen cloud backends (Google Drive/Dropbox/OneDrive) and anti-lock-in. | thread3-digest.md |
| AFFiNE gaps cited by users | No Excel-like in-cell functions, no one-database-many-views, ambiguous on-premise storage limits, cloud-only AI. | thread3-digest.md |
| "Gold formula" quote | Anytype on-premise with Notion UX. | thread3-digest.md |
| One member's requirements list | Paragraph-level links surviving moves, encrypted local backup, readable-format auto backup, phone sync, standard-format export, checkboxes/images/color, privacy when synced, code formatting, with AI chat as nice-to-have. | thread3-digest.md |
| Also present | p2panda relay mention, and a Notion-meets-QuickBase vision with online/offline sync. | thread3-digest.md |

Sources: thread3-digest.md, research-material/discord-thread3-transcript.txt

## R4: MyScript / Nebo reverse engineering

| Topic / question | What the research found | Evidence |
|---|---|---|
| Verdict | MyScript's recognition cannot be pulled from anything public. | myscript-nebo-reverse.md |
| MyScriptJS | Archived, Apache-2.0, contains only ink capture/rendering/transport glue; recognition runs behind developer keys. | myscript-nebo-reverse.md |
| Nebo teardown | A published apktool+jadx teardown of Nebo Android (~31,045 classes) shows Nebo is a thin Java/SWIG shell over proprietary native engines (libMyScriptEngine Text/Math/Shape/Gesture) plus proprietary resource bundles: an architecture donor, not an algorithm donor, and nothing binary redistributable. | myscript-nebo-reverse.md |
| Stroke format | Nebo's .bink stroke format has no published parser (Xournal++ issue #5730). | myscript-nebo-reverse.md |
| Open landscape | No open MyScript reimplementation exists; xournalpp_htr (GPL-2.0, CRNN/CTC with stroke dynamics) is research-grade self-built HTR; RNote has no HTR. No DMCA takedowns found. | myscript-nebo-reverse.md |
| Actionable shape | Implement the MyScript interface contract (incremental strokes in, partial recognition out, JIIX/MathML/LaTeX export) against local engines (ML Kit, xournalpp_htr models); never touch APK artifacts. | myscript-nebo-reverse.md |

Sources: myscript-nebo-reverse.md

## R4: integration components verdict (license first)

| Topic / question | What the research found | Evidence |
|---|---|---|
| Excalidraw | MIT; the cleanest true embedded view (React component in webview, weight S). | integrations-1.md |
| Godot | MIT; embeddable via LibGodot/libgodot (M-L). | integrations-1.md |
| libVLC | LGPL-2.1, FFI; workable (M). | integrations-1.md |
| Kdenlive | Via the MLT engine (LGPL-2.1, M) with the editor UI out of scope. | integrations-1.md |
| ONLYOFFICE | AGPL-3.0: a license blocker for native embedding, iframe/WebView embed only (L). | integrations-1.md |
| GPL-family media tools | Audacity GPLv3 has no library/headless mode; OBS libobs GPL-2.0+ infects the host (Streamlabs precedent); GIMP GPL-3.0 headless/ScriptFu only; Krita plugins-only; Blender GPL-2.0+ headless via bpy. GPL-family components are therefore file-level or sidecar integrations only, never in-process. | integrations-1.md |
| Photopea | Closed source despite the free web app: disqualified. | integrations-1.md |
| Stirling PDF | Open-core (MIT essentials + proprietary folders), file-level (S-M). | integrations-1.md |

Sources: integrations-1.md

## R4: OneNote-style pen/keyboard/touch auto-switching

| Topic / question | What the research found | Evidence |
|---|---|---|
| Reference implementations | OneNote Windows ships "Automatically switch between inking, selecting, typing and panning" (File>Options>Advanced>Pen); iPad has "Draw with Touch"; Android has "Ignore touch input when using stylus". | input-mode-switching.md |
| Best architecture reference | tldraw: reject non-pen pointers BEFORE they update input state (a public fix, PR #10346, addressed the exact ordering bug). | input-mode-switching.md |
| Platform hooks | Windows WM_POINTER pointerType + POINTER_PEN_INFO; iOS UITouch.type + UIPencilInteraction + PencilKit drawingPolicy; macOS tabletPoint/Proximity; Android getToolType + ACTION_CANCEL palm cancel + contact-size heuristic; Linux libinput palm detection. | input-mode-switching.md |
| Web pitfalls | Firefox flipped pen to touch mid-stroke historically, and passive capacitive styluses are indistinguishable from fingers (pressure/width fallbacks needed). | input-mode-switching.md |
| Working ruleset | Pen in range means touches become navigation only (pan/zoom/scroll); last-used pen persists across lifts; finger-draw toggle and palm-rejection presets as user overrides. | input-mode-switching.md |
| Licensing | rnote (GPL-3.0, Rust/GTK4) is a study reference; tldraw is source-available with a proprietary license, so no production code reuse, concepts only. | input-mode-switching.md |

Sources: input-mode-switching.md

## R4: tolaria.md

| Topic / question | What the research found | Evidence |
|---|---|---|
| What it is | Tolaria (github.com/refactoringhq/tolaria) is AGPL-3.0-or-later, Tauri v2, roughly 100K LOC of Rust+React (mostly AI-written), plain .md files with YAML frontmatter, no accounts/servers, git-as-sync with opt-in AutoGit, Notion-like block editor plus raw mode, types-as-lenses, YAML custom views, tldraw whiteboards, Mermaid, sandboxed HTML blocks, Cmd+K palette, and AI-first design (OpenAI/Anthropic/Gemini/Ollama/LM Studio, CLI agent targets, bundled MCP server, AGENTS file). | tolaria.md |
| Reception | Praise for UI polish, git-as-AI-transparency, and 10K-note scale; complaints about the Tauri web-wrapper feel, feature creep, and early bugs. | tolaria.md |
| Liftability | Concepts and interactions are freely liftable; reusing its code binds the host project to AGPL. | tolaria.md |

Sources: tolaria.md

## R4: per-app likes/wants (headline signals)

| Topic / question | What the research found | Evidence |
|---|---|---|
| Notability | Its ink is time-locked to audio (tap a stroke to jump the recording): its most irreplaceable feature. | apps-likes-wants.md |
| ConvertOneNote2MarkDown | 766 stars; still exports each OneNote ink stroke as a positionless image although the COM API GetPageContent carries stroke positions plus ISF: ink-preserving OneNote import is a genuine open differentiator. | apps-likes-wants.md |
| Goodnotes 6 | AI ink-smoothing deforms users' handwriting: on-device AI that touches user strokes needs a findable off switch. | apps-likes-wants.md |
| Noteshelf | Charged lifetime v2 buyers again for v3: pricing-trust caution. | apps-likes-wants.md |
| Obsidian security | April 2026 "Phantom in the Vault" campaign: a crafted vault plus a legitimate plugin config executed attacker commands on vault open, meaning vault files themselves are an attack surface. | apps-likes-wants.md |

Sources: apps-likes-wants.md

## R4: repo inventory resolutions

| Topic / question | What the research found | Evidence |
|---|---|---|
| Not-found resolutions | NicTanghe/BasScript does not exist (canonical counterpart: BaseScript.lang, irrelevant to this project). ThatSheepGuy22/ObbyNotes is not findable. A community member's OfficeIMO fork resolves to EvotecIT/OfficeIMO (MIT, .NET). | deep-repos-a.md, deep-repos-b.md, deep-repos-c.md |
| Top liftable Rust-first assets | realbynl/Meridian-Notes (native Rust editor architecture, license to confirm), AlienTechSoftware/notecraft (Rust core/UI split, MIT/Apache-2.0, alpha 0.0.6), EkarinLB/e-journal (egui + encryption-at-rest, MIT), gtg922r/obsidian-numerals (math engine as pure module, MIT, ~600 stars), hughhowey/neo (plain-file data model, MIT, ~1.6k stars), johansan/notebook-navigator (virtualized 100k-note browser; GPL-3.0 so spec-only, 2,782 stars / 1M+ downloads), kostyk348/CapsuleCraft (.eml-per-note storage, MIT). | deep-repos-a.md, deep-repos-b.md, deep-repos-c.md |
| AFFiNE deep dive | BlockSuite duality, OctoBase sync, MIT. | deep-repos-c.md |

Sources: deep-repos-a.md, deep-repos-b.md, deep-repos-c.md
## R5: the study/PDF-textbook angle (BookCraft idea) and IdeaCraft

| Topic / question | What the research found | Evidence |
|---|---|---|
| Trigger | The user supplied one new link (aamirenic/IdeaCraft) plus a full community-submitted app idea (BookCraft: a dedicated stylus study space over notebooks and PDF textbooks, Drawboard-PDF-level inking, organized by subject or course), and asked again whether every app, link and feature truly got in-depth coverage. | user input |
| Coverage audit answer | Stated honestly: every link known at R4 was inventoried and every major app got a deep dive, but depth was tiered (30 repos and 16 apps deep; smaller links inventory-level; a few member-hosted repos unfindable). R5 covers the new material at full depth. | this synthesis |
| IdeaCraft | aamirenic/IdeaCraft, MIT: days-old local-first Tauri 2 + Rust notes app: SQLite, block editor with Markdown shortcuts, page history, search palette, templates, export/backup, sync folder, opt-in local Ollama, minisign auto-updates; Windows-only v1.0.0 (2026-10-23), no handwriting or mobile. | r5-ideacraft.md |
| IdeaCraft pull-from | Under MIT: the SQLite schema (db.rs), the Tauri command layer (commands.rs), the sync-folder design, the smoke-test harness. | r5-ideacraft.md |
| Name confusion | Unrelated namesake repo rickyb82/ideacraft (Rust mind-map canvas) is a likely confusion source. Not part of the ArtCraft family, whose 13-app pure-Rust lineup bans webviews. | r5-ideacraft.md |
| Drawboard PDF | The community's inking reference: pressure ink over Windows Ink, virtual-paper feel, dockable tool favorites, best-in-class palm rejection, calibrated measurement tools; closed source; eroding goodwill from the 2023 subscription switch (pressure ink moved behind Pro) and long-session performance rot. Lesson: pair Drawboard-level ink quality with a different structure and a trustworthy pricing model, not a feature clone. | r5-drawboard-pdf.md |
| Study/PDF landscape | Flexcil, LiquidText, CollaNote, MarginNote 4, Xodo, PDF Expert, plus the Goodnotes/Notability/OneNote textbook angles and newer entrants Write, University Notes, Zotero: the common load-bearing feature set is a course-organized library, pen/highlighter plus text-layer highlighting, excerpt-to-note linking back to source pages, split view, handwriting search, lossless annotated export, annotation-based study aids. | r5-study-apps-landscape.md |
| Loudest wants | Working sync, ink smoothing, pixel eraser and shapes, layers, large-textbook performance, annotation write-back, stable pricing. | r5-study-apps-landscape.md |
| Verdict | The unified dedicated study notebook over textbooks is a real but contested gap; documented traps are subscriptions, buggy updates, large-PDF performance and sync. | r5-study-apps-landscape.md |

Sources: r5-ideacraft.md, r5-drawboard-pdf.md, r5-study-apps-landscape.md

## R6: the full-depth sweep (every remaining inventory item)

Trigger: the user's directive "I dont want varied, I want everything to be reasearched in full and in depth" turned R2-R5's tiered depth into a defect.

| Topic / question | What the research found | Evidence |
|---|---|---|
| Scope | R6 covered every remaining inventory item at full depth in three waves of subagent lanes, producing 12 findings files (~540 KB), then a verify pass dispositioned every UNVERIFIED marker. | r6-*.md |
| Wave 1 (minor apps, editors, sync) | Squid, Concepts, Saber, Workflowy, DEVONthink, ente, Kinopio, then 15 more (Muse/Allume, Thymer, Ideon, OwlLuna, Akasha, Poznote, Tangent, HelixNotes, Lockbook, Pele-not-found, Obsidian Publish pricing backlash, the caption-tool landscape), then editors and publishers (Dillinger, Ghost, Homebrewery, proofeditor, the Amphi disambiguation, the Samsung Notes deep dive), then the sync/CRDT+E2EE stack (BeeKEM, Loro protocol-e2ee, any-sync, secsync, p2panda; Rust-native yrs, Loro, iroh, automerge core, nostr-sdk; 263 URLs cited). | r6-*.md |
| Wave 2 (handwriting and local AI) | HTR/OCR engines measured on real benchmarks (TrOCR best open HTR; Tesseract disqualified for handwriting at 49.58% CER; docTR, PaddleOCR, docling, paperless-ngx, ocrmypdf, OnlineHTR, ArabicOCR_KHATT with the KHATT/LDC licensing checkpoint); Xournal++, RNote (license corrected to GPL-3.0-or-later), the fully reverse-engineered Supernote .note format; palm rejection documented per platform; small local LLMs, STT, TTS and RAG with a pre-ship license checklist. | r6-*.md |
| Wave 3 (Obsidian plugins, OSS batch D, Nostr) | 16 plugins license-verified at each repo (Templater carries a genuine license conflict needing a human check before any pull decision); jpzk/opensidian identified as the closest existing project to ours (Rust+Tauri clean-room Obsidian clone); Nostr judged concepts-only for sync with negentropy set-reconciliation and NIP-44 discipline worth pulling regardless; iroh the stronger Rust-native p2p lane. | r6-*.md |
| Verify pass | 34 entries tracked, 22 resolved, 5 partially, 7 not found. License corrections applied (diamond-types ISC, secsync Apache-2.0 and dormant, snlib and TanaMigrator no-license-unpullable). The "Notion uses Yjs" adoption claim was dropped for lack of a source. Coverage-audit statement updated: the full-depth sweep is complete; every inventoried link now has full-depth research or a documented not-found disposition. | r6-*.md |

Sources: the twelve r6-*.md files (in research-material/findings/)

## R7: per-app feature inventories, internet-wide sentiment, remake landscape, and the user's 11 supplied repos

Trigger: the user's standing demand for the most in-depth research plus 11 newly supplied repos with the instruction "research all of these in depth every feature, etc." Six subagent lanes ran (three had been cancelled by a plan limit in the first attempt and were relaunched successfully).

| Topic / question | What the research found | Evidence |
|---|---|---|
| Feature inventories: majors lane | 20 apps, Obsidian through tldraw, completed with a 4-app top-up (DEVONthink, Kinopio, Concepts, tldraw) after its first run was cancelled. | r7-feature-inventory-majors.md |
| Feature inventories: OSS lane | 19 apps, Logseq through Tangent Notes. | r7-feature-inventory-oss.md |
| Feature inventories: handwriting/study lane | 19 subjects, completed in the earlier run, covering the stored-ink vs live-conversion vs search-only split of HWR, pricing-model transitions as the dominant complaint pattern, and the finding that no app in the batch claims E2EE. Every captured claim carries a URL; gaps are marked UNVERIFIED this session. | r7-feature-inventory-handwriting.md |
| Sentiment sweep sources | Reddit (r/NoteTaking, r/PKMS, r/ObsidianMD, r/Notion, r/Evernote, r/logseq, r/GoodNotes, r/selfhosted), HN evidence from search-indexed threads (hn.algolia.com JSON fetches were blocked), app-store review patterns via community threads (store pages not crawlable this session). | r7-user-sentiment-sweep.md |
| Sentiment sweep result | 8 ranked demands each with 2+ independent sources, 3 single-source items quarantined as unconfirmed, plus praise patterns, pricing-resentment patterns, handwriting-specific sentiment, an honesty check on local-first/E2EE demand, and a migration-pain section. | r7-user-sentiment-sweep.md |
| Remake landscape | 33 projects mapped. 17 verified alive, 13 verified dead/dormant with evidence, 3 unresolvable this session. Four death patterns: vendor adopt-then-drop (Focalboard), single-maintainer exit (Notea, Athens), incumbent-API dependence (NixNote2, Geeknote, Everpad), acqui-deletion (Skiff). | r7-remakes-evernote-notion.md |
| User repos lanes | All 11 supplied repos researched at repo HEAD plus releases, issues, and community reception. Batch A: turtl/desktop, Zettlr, QOwnNotes, blinko, edgeever, notion-re. Batch B: zappynotes, owlistic, NexaNote, memos, siyuan. | r7-user-repos-a.md, r7-user-repos-b.md |
| SiYuan (deepest treatment) | Go kernel + Electron shell, .sy block-JSON files, FTS5, SQLCipher option, dejavu snapshot repo with repo-key E2EE over official cloud/S3/WebDAV/local, attribute views, riff flashcards, MCP server, paid sync gating. Pull-from verdicts recorded per repo in FEATURES.md. | r7-user-repos-b.md |

Sources: r7-feature-inventory-majors.md, r7-feature-inventory-oss.md, r7-feature-inventory-handwriting.md, r7-user-sentiment-sweep.md, r7-remakes-evernote-notion.md, r7-user-repos-a.md, r7-user-repos-b.md

## R12: evidence-enrichment round (2026-10-27)

- R12 was an evidence-enrichment pass over the existing catalog, not new discovery: roughly 99 app and repo entries re-surveyed across seven lane files, each producing per-app Features/Sentiment/Wants/Pricing tables, Contradictions sections, and per-app SHOT-LISTs.: findings/r12-enrich-a.md, findings/r12-enrich-b.md, findings/r12-enrich-c.md, findings/r12-enrich-d.md, findings/r12-enrich-e.md, findings/r12-enrich-f.md, findings/r12-enrich-g.md
- The pass was three-part per app: a visual-surface capture (what the UI actually looks like, platform by platform), an exhaustive docs analysis with anything not confirmed from official sources marked UNVERIFIED rather than filled in, and feature-tied sentiment (likes and wants attached to specific features instead of general verdicts).: findings/r12-enrich-a.md, findings/r12-enrich-e.md
- UNVERIFIED discipline in practice: Dillinger's SourceForge/Slashdot listing (12 AI editing actions, an MCP server, a 13-endpoint REST API) appears nowhere on dillinger.io or the GitHub README and is kept unconfirmed; Dillinger's legacy AngularJS feature set is no longer visible in current docs; sawt is carried entirely UNVERIFIED in lane D.: findings/r12-enrich-e.md, findings/r12-enrich-d.md
- A video-evidence pass accompanied the text pass, because video shows what docs flatten — four concrete examples:
- Samsung Notes: actual S Pen latency, palm rejection and handwriting-conversion speed are only judgeable on hardware footage; text pages never convey them.: findings/r12-enrich-b.md
- Logseq: the most telling video finding is the tutorial ecosystem itself freezing — commenters explain creators will not record because the DB version will make their videos irrelevant, so even two-year-old tutorials no longer match the current app or DB betas.: findings/r12-enrich-c.md
- Obsidian: the r/ObsidianMD subreddit functions as a comment section for YouTube videos, with the CEO (kepano) showing up in a plugin walkthrough's comments and graph-view skeptics gripping under fan videos — sentiment text sources never surface.: findings/r12-enrich-b.md
- Heptabase: the timestamp-linked-card loop and the YouTube-transcript-to-card workflow are only legible on video; Miro's multiplayer facilitation mechanics and CapCut's adjustment-clip behavior are in the same class of video-only evidence.: findings/r12-enrich-c.md, findings/r12-enrich-b.md, findings/r12-enrich-e.md
- Image capture result: the 486-URL shot manifest (shot-manifest.jsonl, one record per URL with lane, app, caption and url fields) was captured into research-material/images/r12/ with headless camoufox in WSL (3 workers; full-page JPEG up to 15000px page height, else viewport-only).
- Capture completeness: 481 of 486 URLs captured; the 5 misses are unreachable URLs, not scraper failures (styluslabs.com TLS certificate errors, one site timeout, one malformed localhost URL recorded in a lane list, one local dev server not running), each documented in research-material/images/r12/capture-notes.md; shot-manifest.jsonl and capture-log.jsonl in the same folder are the provenance records.
- Lane A (findings/r12-enrich-a.md): the 17 study/PDF majors, from Goodnotes through PDFCraft, completed 17 of 17.: findings/r12-enrich-a.md
- Lane B (findings/r12-enrich-b.md): majors batch 1 — Obsidian, Obsidian Publish, OneNote, Evernote, Notion, Craft, Anytype, Tana, Reflect, Milanote, Miro, Samsung Notes, 12 of 12 plus video supplements.: findings/r12-enrich-b.md
- Lane C (findings/r12-enrich-c.md): majors batch 2 — Logseq, Joplin, Notesnook, Trilium Notes, AFFiNE, ente, Heptabase, Kinopio, tldraw, Excalidraw, Saber, Lockbook, 12 of 12 plus video supplements.: findings/r12-enrich-c.md
- Lane D (findings/r12-enrich-d.md): the long tail, 19 entries from Squid through marmalade-tts-android, including a fully UNVERIFIED entry (sawt).: findings/r12-enrich-d.md
- Lane E (findings/r12-enrich-e.md): editors, publishers and video editors — Dillinger, Homebrewery, Ghost, Proofeditor, CapCut, Descript, LumaFusion, 7 apps.: findings/r12-enrich-e.md
- Lane F (findings/r12-enrich-f.md): the OSS repo sweep, 17 of 17 repo entries (notecraft, nexlore, Meridian-Notes, CapsuleCraft, opensidian, e-journal, neo, xnotes-android, verdicts on open-notebook and BasScript, OfficeIMO and more) plus video supplements.: findings/r12-enrich-f.md
- Lane G (findings/r12-enrich-g.md): OSS batch 2, 15 app entries from turtl through the Supernote ecosystem (file header says apps 1-16).: findings/r12-enrich-g.md
- Correction output was collected in a patches file covering 25 sections (notebook-navigator determined unchanged on lane evidence), from which FEATURES.md's R12 corrections are drawn.: findings/r12-int-features-patches.md
- Headline correction: the 2026 pricing re-architectures — Notability's Starter/Lite/Plus/Pro/Business ladder ($79.99/yr Pro) and Goodnotes' Free/Teams additions supersede every cached price row for those two apps.: findings/r12-enrich-a.md
- Headline correction: Samsung Notes' OneNote sync is confirmed gone after July 2026 by Samsung's own support page, killing a still-repeated compatibility fact.: findings/r12-enrich-b.md
- Headline correction: Trilium's canonical repo moved to the community (TriliumNext) and the project regained the Trilium name; Obsidian's plugin count is ~9,521 on the Oct 2026 registry, not the "2,700+" still cited in reviews.: findings/r12-enrich-c.md, findings/r12-enrich-b.md
- Headline correction: velocity signals — CapsuleCraft shipped v1.8.0 one day after the cached v1.7.0 date, and xnotes-android moved to v0.9.0, superseding cached version rows.: findings/r12-int-features-patches.md

Sources: findings/r12-enrich-a.md, findings/r12-enrich-b.md, findings/r12-enrich-c.md, findings/r12-enrich-d.md, findings/r12-enrich-e.md, findings/r12-enrich-f.md, findings/r12-enrich-g.md, findings/r12-int-features-patches.md.

## R12 round 2 (confirmation and gaps)

- Round 2 was a claim-by-claim re-verification of existing findings across nine parallel lanes: no conclusion from an earlier round was inherited; every verdict required a source actually loaded this session, and anything not re-fetched is marked STILL-UNVERIFIED rather than confirmed. Lane files are findings/r12-confirm-1.md through r12-confirm-9.md; each carries per-claim verdict lines in the L<line> | gist | verdict | URL | note format, plus exact-match patch blocks the main session applied to the master files.
- Lane coverage: lane 1 re-verified the majors inventory (74 claims verified; 24 r9-sweep candidates: 11 filled, 13 not confirmable); lane 2 the handwriting inventory (178 claims; 17 filled, 1 not confirmable); lane 3 the OSS inventory (263 claims: 235 confirmed, 26 revised, 2 denied, 73 still-unverified; all 17 candidates filled); lane 4 the user-repos and remakes files (93 claims; 11 filled, 1 not confirmable); lane 5 the deep-repos files (123 claims); lane 6 the thread and sentiment files (66 claims); lane 7 the sync/CRDT, Obsidian-plugins, nostr and integrations files (85 claims: 14 confirmed, 6 revised, 65 still-unverified — the search budget ran out mid-lane and nothing without a loaded source was confirmed); lane 8 the linked-apps, GitHub-repos, sentiment, Tolaria, MyScript-reverse and r8-corrections files (238 claims); lane 9 hunted coverage gaps (24 thin/missing APPS-LINKS rows, 4 feature-area gaps, 12 researched).
- Master-file corrections applied with reasons (the full evidence trail is in the lane files): OneNote's me@onenote.com email capture was removed in March 2025 (Microsoft support page), so the r7 capture row is wrong for current OneNote; Obsidian's audio recorder is a core plugin (help.obsidian.md), correcting "none native"; Goodnotes' audio is core (Note Replay with searchable transcripts, 20 min free/unlimited paid, iOS/macOS only) and the "Special Edition" one-time tier does not appear on the current pricing page, so it is downgraded to unconfirmed; Notability re-verified as iCloud-or-Notability-Cloud sync (max 10 devices), a 2026 tier ladder (Starter free 5 notes / Lite $11.99 / Plus $15.99 / Pro $79.99 / Business $60 per user per year) and a returned NOTABILITY CLASSIC one-time purchase; Tana's real tiers are Free / Pro $20-30 / Business $35 — the third-party "Core $10/Plus $20" listing is wrong; Reflect now headlines "Meet Reflect Open" (open source, local Markdown, free Mac, paid iPhone/iPad, iCloud Drive or Git sync); Craft's free tier is capped at 1,500 blocks, so the master's "unlimited" was wrong.
- Denied and revised by fresh evidence: Outline has no native mobile apps (responsive PWA; official docs), denying the "mobile apps exist" claim; HelixNotes is not archived (live App Store listing, actively developed); e-journal exists (an r8 negative finding was wrong) and uses Tauri v2 with a system WebView, not egui, with releases at v0.12.0/v0.12.1 (2026-10-19/20, so the recorded 2025 date was a typo); ConvertOneNote2MarkDown issue #123 is a how-to thread, not a COM-elevation report — the r8 correction itself needed this further revision, and the canonical COM issue is #102; the TriliumNext repo was renamed to Trilium (same project).
- Version and count refreshes folded into the masters: CapsuleCraft v1.8.1 (2026-10-27); jpzk/opensidian releases up to v0.8.0; notebook-navigator reads 1.5k-1.6k stars in cached snapshots (2,782 not confirmable) with roughly 735,000 installs as of July 2026; Omnisearch has 2,037,395 installs (rank 17, obsidianstats.com most-downloaded); Templater is listed AGPLv3 by the registry, revising the R6 GPLv3 draft; Tailscale's client is BSL 2.0 (not open source) while Netbird carries the row's open-source verdict; Krita and Kdenlive both surfaced headless paths (kritarunner Python runner; kdenlive_render CLI), so "no headless" claims were softened while "no embeddable view" stands; Obsidian Sync re-verified at $4/mo annual ($48/yr) with the plugin registry at ~9,521; the nostr crate sits at 0.45.5 with 2.67M total downloads, the ~446K/month rate kept as estimate only; Piper is dual MIT/GPL-3.0; Meridian-Notes is MIT (license fetched live, dropping the r8 caution); e-journal stores to a single local JSON file plus .bak, and open-note is local-JSON-storage inking, not Firebase-backed.
- The r9-camoufox-sweep candidates: 71 were distributed to lanes 1-4 and 56 were filled with sources, 15 marked not confirmable (absence of current evidence is recorded as such, never treated as confirmation).
- Lane 9's gap additions to the masters: three new FEATURES.md sections (Accessibility: only 7 passing mentions corpus-wide, with the ProServe canvas-accessibility quote; Search quality: no measurement lane exists anywhere in the findings; Data ownership: Capacities has no local mode, Google Keep export gaps, Roam 1.0's local option) and twelve new APPS-LINKS rows researched from scratch (Bear, Apple Notes, Capacities, Roam Research, Dynalist, Google Keep, Notable, Boostnote, Hypothes.is, Agenda, aamirenic/IdeaCraft, jdkruzr/ultrabridge).
- Integration mechanics: nine lane patch-block formats were normalized by the integrating script (SECTION blocks with END SECTION, END ROW, or no end marker), 68 patch operations applied to FEATURES.md and APPS-LINKS.md with zero misses, and hand corrections were anchored to unique master text after the first pass's eight mis-anchors were diagnosed and fixed (e.g. the Godot PR numbers containing "#123" forced section scoping, and the two stats corrections target the findings files, not APPS-LINKS, where no such figures live).

Sources: findings/r12-confirm-1.md, findings/r12-confirm-2.md, findings/r12-confirm-3.md, findings/r12-confirm-4.md, findings/r12-confirm-5.md, findings/r12-confirm-6.md, findings/r12-confirm-7.md, findings/r12-confirm-8.md, findings/r12-confirm-9.md.
