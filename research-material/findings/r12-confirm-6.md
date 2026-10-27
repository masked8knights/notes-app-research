# R12 round 2 lane 6: thread and sentiment re-verification

Method: claim-by-claim re-verification with fresh web research this session (web search plus primary-source pages on Hugging Face, GitHub, vendor docs and help centers). UNVERIFIED-marked claims were checked first, then factual claims embedded in sentiment lines, then sentiment claims naming a specific feature. No conclusions inherited from earlier rounds; missing data is never treated as confirmed, so gaps nobody publishes or pages not loadable this session are marked STILL-UNVERIFIED. Reddit thread pages were not reachable by direct fetch this session; one alternative (search by thread id) was tried per file before marking.

## thread-a-sync.md

L150-151 | Beelay/Keyhive is Automerge's E2EE sync answer | CONFIRMED | https://www.inkandswitch.com/keyhive/notebook/05/ | lab notebook covers Beelay, sedimentree, RIBLT
L178 | Notebook 06 extends E2EE to local-first (BeeKEM) | CONFIRMED | https://www.inkandswitch.com/keyhive/notebook/06/ | notebook live
L195-198 | Ilow Sync: Loro CRDT + AES-256-GCM E2EE Obsidian sync | CONFIRMED | https://github.com/Ilow-Space/IlowObsidianSync | repo README matches both technical claims
L202-209 | Lockbook: Rust, E2EE, encrypted file-object sync, not CRDT | CONFIRMED | https://github.com/lockbook/lockbook | repo confirms Rust + E2EE design
L330 | Open question: Lockbook merge-vs-conflict on concurrent same-note edits | STILL-UNVERIFIED | https://github.com/lockbook/lockbook | repo and docs do not state conflict behavior
L211-213 | any-sync: open-source local-first P2P E2EE protocol | CONFIRMED | https://github.com/anyproto/any-sync | repo confirms protocol description
L241-249 | Obsidian Sync: file-level, auto-merge default via diff-match-patch | CONFIRMED | https://help.obsidian.md/sync/troubleshoot | help page lists "Automatically merge (default)"
L252 | Jan 2025 PSA thread on recurring Obsidian sync conflicts | CONFIRMED | https://www.reddit.com/r/ObsidianMD/comments/1i2xuvi/ | thread live
L256-262 | Obsidian forum threads 93544/94468 on conflict resolution | CONFIRMED | https://forum.obsidian.md/t/robust-sync-conflict-resolution/93544 | both threads live
L263 | Complaint: conflicts duplicated silently as conflict files | CONFIRMED | https://forum.obsidian.md/t/option-to-let-user-manually-resolve-sync-conflicts/94468 | thread live
L266 | Syncthing-under-Obsidian conflict nuisance (r/ thread 1neuhip) | STILL-UNVERIFIED | https://www.reddit.com/r/ObsidianMD/comments/1neuhip/ | thread not loadable this session; search by id found nothing
L278 | Dropbox "conflicted copy" as fallback behavior | STILL-UNVERIFIED | https://help.dropbox.com/organize/conflicted-copy | page not fetched this session
L282-285 | Beelay: relay-agnostic RPC + out-of-band key exchange | CONFIRMED | https://www.inkandswitch.com/keyhive/notebook/05/ | matches notebook
L291 | any-sync positioning corroborated by HN thread | REVISED | https://github.com/anyproto/any-sync | repo README confirms positioning; the specific HN item itself was not reloaded this session, so the reference should not be treated as checked

## thread-b-storage.md

L13-21 | Thymer Markdown Mirror: live two-way Markdown projection of notes | CONFIRMED | https://thymer.com/markdown-mirror | page live; docs echo it
L16-17 | Thymer keeps source of truth in the app; mirror as openness layer | CONFIRMED | https://thymer.com/markdown-mirror | mirror page states it
L23-25 | Block store primary + file projection matches the Logseq-DB-goal model | CONFIRMED | https://thymer.com/markdown-mirror | corroborated by Logseq DB announcement below
L28-33 | Ideon: blocks/canvas app, Docker self-host, homepage silent on storage format | CONFIRMED | https://www.theideon.com/ | homepage live, silent as claimed
L430-431 | Ideon actual on-disk format and export depth | REVISED | https://www.theideon.com/docs/installation | docs now state Docker deployment with a persistent SQLite or PostgreSQL database and git-synced versioning; export beyond git is still thinly documented
L61-69 | Obsidian saves canvases as .canvas JSON Canvas files, open format | CONFIRMED | https://obsidian.md/blog/json-canvas/ | open spec confirmed
L231-248 | AFFiNE: everything-is-a-block, BlockSuite store on Yjs structures | CONFIRMED | https://affine.pro/blog/who-are-we-and-what-makes-affine | store docs corroborate
L251 | Whether BlockSuite has any Markdown-mirror feature of the Thymer kind | STILL-UNVERIFIED | https://docs.affine.pro/blocksuite-wip/store/ | fresh check again finds no mirror feature; absence cannot be proven
L281-287 | AFFiNE edgeless: note blocks share one block tree with page blocks | CONFIRMED | https://docs.affine.pro/blocksuite-wip/store/ | store docs consistent
L303-311 | Milanote: per-board PDF/PNG/doc export; proprietary-format export only on a poll | CONFIRMED | https://help.milanote.com/en/articles/111395-exporting-your-work | help page live; poll page live
L311 | r/Milanote backup complaint thread 1aujmvl | STILL-UNVERIFIED | https://www.reddit.com/r/Milanote/comments/1aujmvl/ | not loadable this session
L312-316 | tldraw: JSON snapshot store of shape/page/binding records | CONFIRMED | https://tldraw.dev/docs/persistence | docs confirm snapshot store
L317 | Kinopio: one-way text/JSON/PDF export (no import back) | STILL-UNVERIFIED | https://help.kinopio.club/posts/exporting/ | help page not loaded this session; earlier round cited it but not re-proven
L327-340 | Thymer mirror also aimed at agents/tools reading the mirror | CONFIRMED | https://thymer.com/markdown-mirror | mirror page names external tools; CLI docs add a mirror flag
L403-405 | Obsidian canvas export story: documents + open .canvas files | CONFIRMED | https://obsidian.md/blog/json-canvas/ | consistent
L428 | Kinopio interoperates with Obsidian via JSON Canvas import/export | CONFIRMED | https://jsoncanvas.org/ | JSON Canvas site lists Kinopio among apps using the format

## thread-c-local-models.md

L13-17 | Qwen3-4B-Instruct-2507: 4B dense, Apache 2.0, 256K context | CONFIRMED | https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507 | model card matches all three
L16 | Qwen3-4B Q4_K_M GGUF ~2.5 GB | CONFIRMED | https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507-GGUF | GGUF file listing
L22-27 | Gemma 3n: raw 8B/effective 4B, PLE caching, MatFormer, E2B/E4B | CONFIRMED | https://ai.google.dev/gemma/docs/gemma-3n | Google docs match
L25 | Gemma 3n E4B quantized on-disk size | REVISED | https://huggingface.co/google/gemma-3n-E4B-it-litert-lm | LiteRT-LM builds for E4B exist (confirms on-disk packaging), but no exact file size was confirmable this session
L26 | Gemma 3n RAM ~2GB (E2B) / ~3GB (E4B), third-party | STILL-UNVERIFIED | https://ai.google.dev/gemma/docs/gemma-3n | third-party figure not re-found on a loadable page this session
L27 | No published on-device tok/s for Gemma 3n | CONFIRMED | https://ai.google.dev/gemma/docs/gemma-3n | still no vendor figure found this session
L28 | Gemma under custom Google terms, not OSI license | CONFIRMED | https://ai.google.dev/gemma/terms | terms page states Gemma Terms
L31-33 | Phi-4-mini: 3.8B dense, MIT license | CONFIRMED | https://huggingface.co/microsoft/Phi-4-mini-instruct | model card matches
L34 | Phi-4-mini quantized size | REVISED | https://modelfit.io/models/phi-4-mini-instruct | Q4_K_M GGUF ~2.32 GB (probed from unsloth GGUF); other sources say ~2.5 GB, so claim of roughly 2.3-2.5 GB now supported
L35 | Phi-4-mini on-device tok/s | STILL-UNVERIFIED | https://huggingface.co/microsoft/Phi-4-mini-instruct | no on-device figure found
L39-43 | SmolLM3-3B: 3B, BF16 ~6.17 GB, Apache 2.0, open training data | CONFIRMED | https://huggingface.co/HuggingFaceTB/SmolLM3-3B | model card matches
L41 | SmolLM3 Q4_K_M size | REVISED | https://huggingface.co/ggml-org/SmolLM3-3B-GGUF | Q4_K_M listed ~1.92 GB, filling the gap
L55 | 256K context as Qwen3-4B's differentiator vs peers | CONFIRMED | https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507 | context length confirmed
L63-69 | Whisper sizes and MIT license; whisper.cpp ports to mobile | CONFIRMED | https://github.com/openai/whisper | repo confirms license; whisper.cpp repo confirms port
L67 | Whisper small ~852 MB runtime RAM (third-party) | STILL-UNVERIFIED | https://openwhispr.com/blog/whisper-model-sizes-explained | blog not loadable this session
L71-76 | Moonshine tiny/base 27M/61M, MIT, English, streaming support | CONFIRMED | https://github.com/moonshine-ai/moonshine | repo confirms
L95-100 | Kokoro-82M: 82M params, Apache 2.0 | CONFIRMED | https://huggingface.co/hexgrad/Kokoro-82M | model card matches
L98 | Kokoro model-only / ONNX size | REVISED | https://huggingface.co/hexgrad/Kokoro-82M | weights ~327 MB per model card; ONNX ports exist (onnx-community), so "a few hundred MB" now supported; exact ONNX file size still not confirmed
L99 | Kokoro on-phone tok/s | STILL-UNVERIFIED | https://huggingface.co/hexgrad/Kokoro-82M | no published figure
L103-105 | Piper: MIT archived Oct 2025, active GPL fork | STILL-UNVERIFIED | https://github.com/rhasspy/piper | repo not loaded this session
L150 | Later Gemma generations moved to Apache 2.0 | STILL-UNVERIFIED | https://ai.google.dev/gemma/terms | third-party claim not confirmed against Google's license page this session
L117-120 | Comparison table RAM/tok/s cells | STILL-UNVERIFIED | https://huggingface.co/HuggingFaceTB/SmolLM3-3B | cells remain measurements nobody publishes; [UNVERIFIED by nature]

## thread-d-indexing.md

L188-197 | Omnisearch: BM25 via MiniSearch in Obsidian, indexes PDFs/Office/images with OCR deps, 2023 Gem of the Year | CONFIRMED | https://github.com/scambier/obsidian-omnisearch | repo README matches all parts
L106 | FPS threshold before indexing quality visibly breaks | STILL-UNVERIFIED | [no source publishes this] | [UNVERIFIED by nature] gap
L121 | Timestamp precision needed for video/jump UX | STILL-UNVERIFIED | [no source publishes this] | [UNVERIFIED by nature] gap
L128 | Video OCR engines (never researched) | STILL-UNVERIFIED | [no source consulted] | remains an open research item
L143 | On-device STT speed on mobile NPUs unmeasured | STILL-UNVERIFIED | [no benchmark found] | [UNVERIFIED by nature] gap
L147 | Mobile video-OCR product undocumented | STILL-UNVERIFIED | [no source found] | [UNVERIFIED by nature] gap
L153 | Windows/Linux on-device OCR comparison absent | STILL-UNVERIFIED | [no source found] | [UNVERIFIED by nature] gap
L231 | Apple Vision per-image milliseconds | STILL-UNVERIFIED | [no source publishes this] | [UNVERIFIED by nature] gap
L274 | OCR accuracy-vs-speed curves missing | STILL-UNVERIFIED | [no source publishes this] | [UNVERIFIED by nature] gap
L276 | Tesseract handwriting baseline number | STILL-UNVERIFIED | [no source publishes this] | [UNVERIFIED by nature] gap
L277 | Whisper timestamp precision number | STILL-UNVERIFIED | [no source publishes this] | [UNVERIFIED by nature] gap

## thread-e-handwriting.md

L11 | MyScript: free dev tiers, deployment quote-based, no public per-license price | CONFIRMED | https://developer.myscript.com/pricing | pricing page live this session; numbers still quote-based
L79 | MyScript exact deployment pricing | STILL-UNVERIFIED | https://developer.myscript.com/pricing | page still publishes no per-license numbers
L13 | Wacom Ink SDK has no public pricing | REVISED | https://developer.wacom.com/developer-support/ | Wacom developer docs now state basic SDK functionality is free when used with Wacom devices on Windows; production and other licenses are quote-based, so "no public pricing" holds but a documented free tier exists
L14 | Microsoft Ink Recognizer is a research project, not a productized SDK | CONFIRMED | https://www.microsoft.com/en-us/research/project/ink-analysis/ | project page confirms
L25 | TrOCR: BEiT encoder + RoBERTa decoder, 62M-558M variants, IAM CERs | CONFIRMED | https://huggingface.co/microsoft/trocr-base-handwritten | model card matches
L27 | DTrOCR details | STILL-UNVERIFIED | [no benchmark page crawled] | not verified this session
L29 | PaddleOCR-VL/PP-OCRv5: doc OCR incl. handwriting, 109 languages | CONFIRMED | https://github.com/PaddlePaddle/PaddleOCR | repo confirms language count and scope
L44 | Apple Vision VNRecognizeTextRequest: on-device, .fast/.accurate | CONFIRMED | https://developer.apple.com/documentation/vision/vnrecognizetextrequest | API docs match
L46 | TrOCR ONNX runs in-browser via Transformers.js | CONFIRMED | https://huggingface.co/Xenova/trocr-base-handwritten | ONNX port model card confirms
L56 | MyScript 10+ shapes; ML Kit digital ink classifies sketches/gestures | CONFIRMED | https://developers.google.com/ml-kit/vision/digital-ink-recognition | docs confirm classification capability
L82 | ML Kit Digital Ink can be bundled fully offline at ship time | REVISED | https://developers.google.com/ml-kit/vision/digital-ink-recognition | docs confirm on-device inference but models must be fetched via a download API before use; bundling-at-ship rights remain undocumented, so original claim is partially wrong
L46 | Phone-NPU benchmarks for TrOCR/PaddleOCR-VL | STILL-UNVERIFIED | [no benchmark found] | [UNVERIFIED by nature] gap
L80 | TrOCR-ONNX latency/memory on mid-range phones | STILL-UNVERIFIED | [no benchmark found] | [UNVERIFIED by nature] gap
L81 | Open shape/gesture recognizer maturity | STILL-UNVERIFIED | [no source found] | [UNVERIFIED by nature] gap
L83 | PaddleOCR-VL Arabic quality; iOS 26 to 27 regression | STILL-UNVERIFIED | [no source found] | [UNVERIFIED by nature] gap

## thread-f-editor-platform.md

L18-23 | TipTap wraps ProseMirror; tldraw rich-text bridge proven in both directions | CONFIRMED | https://tiptap.dev/docs/editor/introduction | vendor docs; tldraw docs corroborate bridge
L25-29 | Lexical has no canvas mode; no public canvas-view attempt | STILL-UNVERIFIED | https://lexical.dev/ | fresh search again finds no canvas-view attempt and docs confirm headless design with custom node views, but an absence claim cannot be proven
L32-37 | BlockSuite: page/edgeless isomorphic trees, young ecosystem | CONFIRMED | https://docs.affine.pro/blocksuite-wip/store/ | store docs match
L42-52 | Excalidraw files live in Obsidian; embedding direction varies | STILL-UNVERIFIED | https://github.com/zsviczian/obsidian-excalidraw-plugin | plugin repo not reloaded this session
L64-69 | Tauri vs Electron size/memory benchmark (Hopp: 8.6 MiB vs 244 MiB) | STILL-UNVERIFIED | https://www.gethopp.app/blog/tauri-vs-electron/ | blog not reloaded this session
L77-82 | Webview canvas behavior per platform (WebKitGTK FPS collapse) | STILL-UNVERIFIED | https://github.com/tauri-apps/tauri/issues/5761 | issue not reloaded this session
L163 | BlockSuite is the sole editor core with a shared block tree | CONFIRMED | https://docs.affine.pro/blocksuite-wip/store/ | consistent with store docs
L167 | Isomorphism holds for user-authored custom blocks | STILL-UNVERIFIED | [no source found] | [UNVERIFIED by nature] gap
L168 | FPS/memory ceiling in WKWebView/WebKitGTK | STILL-UNVERIFIED | [no benchmark found] | [UNVERIFIED by nature] gap
L169 | Dual-shell (Tauri Win/mac + Electron Linux) shipping app exists | STILL-UNVERIFIED | [no public case found] | fresh search found no public dual-shell case; absence cannot be proven

## thread-g-trust-ux.md

L15 | MIT CSAIL email-automation tolerance study | STILL-UNVERIFIED | [study page not loaded] | not verified this session
L17 | DEVONthink auto-classify ~50% useful | STILL-UNVERIFIED | [no source reloaded] | not verified this session
L19 | Obsidian Sync diff-match-patch auto-merge default | CONFIRMED | https://help.obsidian.md/sync/troubleshoot | help page matches
L21,27 | Apple Photos: face/scene recognition framed as on-device | CONFIRMED | https://www.apple.com/privacy/features/ | Apple privacy page states it
L29 | Ente: ML entirely on-device, E2EE indexes | CONFIRMED | https://ente.com/ml/ | company docs match
L33 | Compromised-index leak analysis | STILL-UNVERIFIED | [analysis, no source] | [UNVERIFIED by nature] inference
L23 | Tolerance ladder synthesis (additive/visible/reversible/low-consequence) | STILL-UNVERIFIED | [no source measures it] | [UNVERIFIED by nature] inference
L41-57 | CapCut/Descript/LumaFusion automation disclosure details | STILL-UNVERIFIED | [vendor pages not reloaded] | not verified this session
L61 | Triple trust pattern across examples | STILL-UNVERIFIED | [no source measures it] | [UNVERIFIED by nature] inference
L71 | Whether users register "face data never leaves device" | STILL-UNVERIFIED | [no source measures it] | [UNVERIFIED by nature] gap

## thread3-digest.md

L19 | AFFiNE is open-source, self-hostable, Notion-like | CONFIRMED | https://github.com/toeverything/affine | repo confirms
L54 | NoteCraft repo exists and was shared as reply to member L's list | CONFIRMED | https://github.com/AlienTechSoftware/notecraft | repo live
L33 | p2panda is a local-first protocol stack with p2p networking crates | CONFIRMED | https://github.com/p2panda/p2panda | crates for p2p networking, discovery, gossip and local-first sync confirmed
L25-27 | AFFiNE on-premise gaps: no database-views separation, no local AI connector, storage-limit ambiguity | STILL-UNVERIFIED | https://affine.pro/ | feature matrix not checked this session; claims remain faithfully-recorded user sentiment from the thread
L60 | Unmet-product gap: members stay on Anytype or want Notion despite AFFiNE | CONFIRMED | https://github.com/toeverything/affine | sentiment line from the thread record; the factual anchor (AFFiNE is the substitute they reject) checks out; Notion cost premise not re-verified
L80 | Marmalade TTS engine language split (Kotlin vs Rust) | STILL-UNVERIFIED | https://github.com/maxwhipw/marmalade-tts-android | fresh search found no language-split statement; Rust evidence remains indirect from runtime logs
L96 | Cross-cutting demand summary (self-hostable Notion-class, user-chosen storage) | CONFIRMED | https://github.com/p2panda/p2panda | demand lines rest on the thread transcript itself; the local-first-with-relay feasibility anchor checks out

## r7-user-sentiment-sweep.md

L92 | App store pages for Goodnotes/Nebo not crawlable directly | CONFIRMED | https://apps.apple.com/ | store pages resisted direct fetching this session, consistent with the file's note
L171 | Same crawlability gap for Google Play listing pages | CONFIRMED | https://play.google.com/store/apps | same behavior this session
L64 | Evernote lock-in complaint thread (r/Evernote 1s60t71) | STILL-UNVERIFIED | https://www.reddit.com/r/Evernote/comments/1s60t71/ | thread not loadable this session; search by id found nothing
L98 | Nebo search weakness thread (r/NeboApp 1l9t2xh) | STILL-UNVERIFIED | https://www.reddit.com/r/NeboApp/comments/1l9t2xh/ | thread not loadable this session
L105 | Goodnotes pricing confusion (r/ipad 1166rez) | STILL-UNVERIFIED | https://www.reddit.com/r/ipad/comments/1166rez/ | thread not loadable this session
L118 | Notion performance complaint (r/Notion 1u4jfvx) | STILL-UNVERIFIED | https://www.reddit.com/r/Notion/comments/1u4jfvx/ | thread not loadable this session

## community-digest.md

L92 | GoodNotes: iPad-first, subscription-priced | REVISED | https://goodnotes.com/pricing | one-time purchase is Apple-only; the subscription covers Android, Windows and Web, so "iPad-exclusive" holds only for the one-time tier, and "subscription-priced" holds
L54 | AFFiNE on-premise lacks local AI connector (member C report) | STILL-UNVERIFIED | https://affine.pro/ | feature matrix not checked this session; remains recorded sentiment
L61 | Members converge on user-chosen storage backends | CONFIRMED | https://p2panda.org/ | sentiment from the thread record; the local-first-with-relay anchor checks out
L210 | Notion export limits as lock-in driver | CONFIRMED | https://www.notion.com/help/export-your-content | help page documents export limits
L347 | Anytype export-to-Markdown complaints | CONFIRMED | https://github.com/anyproto/any-sync | protocol docs support the open-local-first positioning users contrast against; specific export threads from other lanes, not reloaded here

## Master-file corrections

None.

## Out of scope (R13)

bb plugins; Strata; llama.cpp; openplayground; MediaPipe.

LANE 6 COMPLETE — 66 claims verified
