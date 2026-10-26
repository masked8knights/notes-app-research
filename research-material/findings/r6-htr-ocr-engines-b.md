# R6 Batch B: Document Processing, OCR, Handwriting Stack & Palm Rejection

Research lane: document-processing and handwriting stack, batch B. Date of research: 2026-10-26.
Project context: local-first Rust/Tauri notes app promising on-device handwriting recognition and OCR everywhere, plus document indexing (PDFs including scanned ones, images, handwriting).
Convention: every claim carries its source URL in parentheses. Items that could not be verified are marked unverified. GPL/AGPL/MPL items are treated as concepts-only for this project (no code pull); MIT/Apache/BSD items are pullable.

---

## 1. OCRmyPDF (ocrmypdf, originally jbarlow83)

### 1.1 What it is, maintainer, version/status
- OCRmyPDF adds an OCR text layer to scanned PDF files so they become searchable and copy-pasteable. Started and led by James Barlow (jbarlow83), now maintained under the org ocrmypdf/OCRmyPDF on GitHub (https://github.com/ocrmypdf/ocrmypdf).
- Current version v17.13.0 released 28 Sep 2026, with 17.13.1 docs current; actively maintained (https://github.com/ocrmypdf/OCRmyPDF/releases, https://ocrmypdf.readthedocs.io/en/latest/installation.html).
- Requires Python >= 3.11 (https://pypi.org/project/ocrmypdf/). 17.13.0 dropped veraPDF for speculative PDF/A checking and now requires pikepdf[pdfa] 10.15+ (which pulls jsonschema, referencing, fonttools) (https://ocrmypdf.readthedocs.io/en/latest/installation.html).
- Status: very healthy. Regular releases, large user base, packaged on Homebrew, PyPI, conda-forge, Docker (https://anaconda.org/conda-forge/ocrmypdf, https://hub.docker.com/r/jbarlow83/ocrmypdf).

### 1.2 Capability picture
- Generates a searchable PDF/A from a regular PDF; places OCR text accurately under the image; keeps original image resolution; inserts text "losslessly" when possible; optimizes PDF images (often shrinking output); optional deskew and image cleaning before OCR; validates input/output; parallelizes across all CPU cores; uses Tesseract, 100+ languages (https://github.com/ocrmypdf/ocrmypdf).
- Modes that matter for a notes app: default (OCR pages without text), --skip-text, --redo-ocr (add text layer to PDFs that already have some OCR), --force-ocr (rasterize everything and re-OCR) (https://github.com/ocrmypdf/OCRmyPDF/discussions/1562).
- Scriptable CLI plus a Python API (ocrmypdf.ocr(...)) (https://github.com/ocrmypdf/OCRmyPDF/issues/1029).
- Note: OCRmyPDF itself is a PDF orchestration layer, not a recognizer. Recognition quality is entirely Tesseract's; it is not a handwriting recognizer. (Inference from architecture; consistent with https://www.reddit.com/r/selfhosted/comments/1nmbuos/.)
- Language packs and Tesseract are external system dependencies; JBIG2 encoder (jbig2enc) is optional and not packaged on Fedora (larger outputs without it) (https://ocrmypdf.readthedocs.io/en/latest/installation.html).

### 1.3 On-device feasibility / resource profile
- Not a model-based system; it is a Python pipeline around Tesseract + pikepdf/pikepdf PDF libraries. Footprint is dominated by Tesseract traineddata per language and PDF rendering intermediates.
- Memory is the known pain point: a 100 MB PDF can produce > 2 GB of intermediates for high page counts (https://github.com/jbarlow83/OCRmyPDF/issues/115); users report filling 32 GB RAM on some files and MemoryError failures (https://github.com/ocrmypdf/OCRmyPDF/issues/1029, https://github.com/ocrmypdf/OCRmyPDF/issues/1290).
- Maintainer guidance for constrained memory: limit parallel jobs, on an N-core system run about sqrt(N) parallel processes each with --jobs set to sqrt(N), and provide generous /tmp space for large files (https://github.com/ocrmypdf/OCRmyPDF/discussions/1386).

### 1.4 License and repo
- Core code: Mozilla Public License 2.0 (MPL-2.0). Non-core code generally MIT; documentation and tests CC-BY-SA 4.0 (https://github.com/jbarlow83/OCRmyPDF/blob/master/LICENSE, https://github.com/jbarlow83/OCRmyPDF/blob/master/README.md, https://pypi.org/project/ocrmypdf/).
- Repo: https://github.com/ocrmypdf/ocrmypdf
- For this project: MPL-2.0 is file-level copyleft. Per the project's rule, treat as concepts-only: study its architecture (page decomposition, redo-ocr diffing, PDF/A handling, parallelism) but do not copy code.

### 1.5 Real-world experience, complaints, failure modes (GitHub issues)
- Hang at end of processing on medium-large scanned PDFs (finish writing output, then long stall cleaning temp dir; ~72 MB / 85 pages reported) (https://github.com/ocrmypdf/OCRmyPDF/issues/1570).
- Output file inflation: --force-ocr re-renders pages as images in the widest colorspace/highest resolution used on the page, typically enlarging files (5.44x in one report); maintainer recommends --redo-ocr instead (https://github.com/ocrmypdf/OCRmyPDF/issues/1366, https://github.com/ocrmypdf/OCRmyPDF/discussions/1562).
- Extreme pathological case: highly compressed text-heavy PDF (~6500 pages, 180 MB) grew to > 3 GB after forced OCR because each page became an image layer + text layer (https://github.com/ocrmypdf/OCRmyPDF/issues/1579).
- PDF/A conversion can be pathological: a 2 MB PDF grew ~50x (~100 MB) with --skip-text --optimize 3 --jbig2-lossy and took over half an hour; disabling PDF/A output fixed it (https://github.com/ocrmypdf/OCRmyPDF/issues/1079). Older similar report of ~4x growth with default PDF/A on black/white scans (https://github.com/jbarlow83/OCRmyPDF/issues/293).
- General memory pressure failures on large inputs (issues #115, #1029, #1290 above).
- Lesson for the notes app: the redo-ocr/skip-text distinction and per-page image handling are the hard engineering; file-size inflation and temp-space use are the top recurring complaints.

### 1.6 Pull-from assessment for Rust/Tauri
- Not usable directly from Rust: it is a Python CLI/library with subprocess-level parallelism. Integration path would be shelling out to the CLI, which drags Python + Tesseract + pikepdf into every install. Not attractive for a Tauri app.
- Pullable concepts (given MPL-2.0 constraints, concepts only): the "add invisible text under image" PDF pattern, redo-ocr diffing logic, page-level parallel OCR, PDF/A optimization trade-offs.
- Practical path for the project: use Tesseract (Apache-2.0) directly via bindings or an ONNX-equivalent engine for OCR, and implement PDF text-layer insertion in Rust (e.g., with lopdf/pdf-writer style crates, or a Rust PDF library), borrowing OCRmyPDF's design rather than its code.

---

## 2. Docling (IBM)

### 2.1 What it is, maintainer, version/status
- Docling is IBM's open-source document-conversion toolkit: it parses many formats (PDF, DOCX, PPTX, XLSX, HTML, EPUB, images, audio, email formats, and more) into a unified structured DoclingDocument representation (https://docling-project.github.io/docling/, https://github.com/docling-project/docling).
- Created by IBM Research (AI4K group, Rüschlikon), announced Nov 2024; hosted in the LF AI & Data Foundation; in early 2026 IBM donated it to the Linux Foundation's Agentic AI Foundation (AAIF) alongside BeeAI and Data Prep Kit, and launched a Docling OpenShift Operator with Red Hat (https://research.ibm.com/blog/docling-generative-AI, https://idp-software.com/vendors/docling/).
- Very active: CHANGELOG shows continuous 2026 activity (e.g., OCR engine work #4418, PPTX/LibreOffice fixes #4425) (https://github.com/docling-project/docling/blob/main/CHANGELOG.md). 10k+ stars already by early 2025 (https://arxiv.org/pdf/2501.17887).
- Python package + CLI; companion repos: docling-ibm-models (the AI models), docling-serve (serving), docling-graph (knowledge graphs).

### 2.2 Capability picture
- Advanced PDF understanding: page layout, reading order, table structure, code, formulas, image classification (https://docling-project.github.io/docling/).
- Powered by specialized models: layout analysis (DocLayNet lineage; current catalog has RT-DETR-based layout models docling-layout-heron, heron-101, egret-medium/large/xlarge) and TableFormer for table cell recognition (accurate and fast modes) (https://docling-project.github.io/docling/usage/model_catalog/).
- Pluggable OCR engines: EasyOCR, RapidOCR (PP-OCR), Tesseract; per-user reports RapidOCR generally handles tables better than EasyOCR (https://github.com/docling-project/docling/issues/2727).
- New for 2026: Granite-Docling-258M, an ultra-compact end-to-end vision-language model (258M params) that converts documents while preserving layout, tables, equations and lists, replacing the traditional OCR + layout pipeline; Apache 2.0 (https://www.ibm.com/new/announcements/granite-docling-end-to-end-document-conversion, https://www.ibm.com/granite/docs/models/docling).
- Five-line Python setup; integrates with LlamaIndex/LangChain for RAG (https://research.ibm.com/blog/docling-generative-AI).

### 2.3 On-device feasibility / resource profile (concrete numbers, published)
- From the Docling technical report (225-page TTS benchmark): M3 Max 4 threads native: 177 s total, 1.27 pages/sec, 6.20 GB peak memory; M3 Max 16 threads: 167 s, 1.34 pages/sec, 6.20 GB; x86 Xeon 4 threads: 375 s, 0.60 pages/sec, 6.16 GB; M3 Max with pypdfium backend: 103 s, 2.18 pages/sec, 2.56 GB peak (lower table quality) (https://en.papernotes.org/ECCV2024/others/docling_pdf_document_conversion/, https://lacuna.tiptreesystems.com/work/docling-technical-report/wrk_50f15bdf4b8e7b7ab2ba63c010899877).
- Per-page per-model latencies: layout model 44 ms on L4 GPU, 633 ms on x86 CPU, 271 ms on M3 Max SoC; TableFormer fast: 400 ms GPU, 1.74 s x86 CPU, 704 ms M3 Max (https://arxiv.org/html/2501.17887v1).
- Model weights on disk: layout + TableFormer land at ~506 MiB (342 MiB TableFormer + 164 MiB layout, du-verified); RapidOCR adds ~40 MB (PP-OCRv4); the Python venv is ~1.3 GB because the ML stack ships as hard dependencies (https://thunderbit.com/blog/docling-review). TableFormer artifacts ~358 MB on the docling-models Hugging Face repo (https://huggingface.co/docling-project/docling-models/tree/v2.2.0/model_artifacts/tableformer).
- GPU deployment figures (server-class, for scale reference): layout ~1 GB VRAM, TableFormer ~600 MB, EasyOCR 500 MB–1.5 GB; single Docling worker 4–6 GB VRAM total (https://www.spheron.network/blog/self-host-document-intelligence-docling-marker-mineru-rag-guide/).
- Verdict for a notes app: the classic pipeline is heavy (multi-GB Python stack, GBs of RAM on big PDFs) but the models themselves are laptop-feasible; Granite-Docling-258M is the interesting on-device-shaped artifact (a 258M-param VLM is roughly 0.5 GB at 8-bit quantization, though no on-device latency numbers are published — unverified).

### 2.4 License and repos
- Docling codebase: MIT. Models: docling-ibm-models is MIT; individual models may carry their own licenses (check per artifact) (https://github.com/docling-project/docling, https://github.com/docling-project/docling-ibm-models). Granite-Docling-258M: Apache 2.0 (https://www.ibm.com/new/announcements/granite-docling-end-to-end-document-conversion).
- Repos: https://github.com/docling-project/docling, https://github.com/docling-project/docling-ibm-models
- Pull assessment: MIT/Apache means code and model concepts are pullable. But the code is Python; for Rust/Tauri the realistic pull is the models: layout and TableFormer are standard PyTorch/ONNX-convertible vision models, and Granite-Docling-258M is a HF model that could run via a local inference runtime (candle/ort), though its VLM decode path makes it much heavier than a plain OCR pass. Unverified: whether official ONNX exports exist for the layout/TableFormer models.

### 2.5 Real-world experience, complaints, failure modes
- Table extraction from scanned/photographed documents is the top accuracy complaint: most errors are OCR-engine limitations plus TableFormer sometimes dropping or merging cell texts (https://github.com/docling-project/docling/issues/2081).
- OCR accuracy complaints for non-Latin content (Japanese/English tests unsatisfactory even after tuning; users seeking better engines) (https://github.com/docling-project/docling-serve/issues/552).
- Surprise on first run: 1.3 GB venv and heavy dependency pull even for trivial conversions (https://thunderbit.com/blog/docling-review).
- do_ocr=False confusion: some users report OCR still running because of "Lazy OCR" behavior when a PDF lacks a text layer (https://github.com/docling-project/docling/issues/2312).
- import errors if the user's script is named docling.py (common footgun, documented in discussion) (https://github.com/docling-project/docling/discussions/2156).
- Benchmarking effort exists specifically to pin down Docling orchestration variance (layout model choice, reading order, OCR presets) (https://github.com/michal-hradis/ocr_benchmarking/issues/80).

### 2.6 Pull-from assessment summary for the notes app
- Best-value pulls: (a) the DoclingDocument schema as inspiration for a structured document representation; (b) the model catalog concepts (layout detection + table structure as separate small models); (c) Granite-Docling-258M as an optional heavy "full document understanding" mode if a VLM runtime is available. The pipeline itself stays out (Python, GPL-free but heavy).
- Do not plan on running the standard pipeline inside a Tauri app; plan on exporting/quantizing individual models to ONNX and running via ort/candle, or calling docling-serve as a sidecar for desktop power users.

---

## 3. Paperless-ngx

### 3.1 What it is, maintainer, version/status
- Paperless-ngx is a community-maintained, self-hosted document management system: scan, index and archive documents; the official successor to Paperless and Paperless-ng, deliberately run by a maintainer team rather than one person (https://github.com/paperless-ngx/paperless-ngx/tree/main).
- About 46,000 GitHub stars; GPL-3.0 license; Python/Django backend, PostgreSQL/SQLite/Redis data layer, Docker deployment; no legal entity, global community (https://www.mrtechking.com/paperless-ngx-github/, https://www.opentechhub.io/paperless-ngx/, https://github.com/paperless-ngx/paperless-ngx/blob/dev/LICENSE).
- Status: very active in 2026 (new features still landing, e.g., OCR Templates / zone-OCR PR #13043 merged) (https://github.com/paperless-ngx/paperless-ngx/pull/13043).

### 3.2 Capability picture
- Ingestion from scans, watch folders, email consumption; OCR via Tesseract + OCRmyPDF so image-only scans become searchable; archival PDF stored alongside original; automatic classification of correspondent, document type, tags, storage paths using a trainable ML classifier that learns from your filing history; optional LLM/AI add-ons (paperless-gpt, paperless-ai) for OCR/tags/summaries; full-text search with highlighting; saved views; configurable workflows (https://openapps.pro/apps/paperless-ngx, https://www.pistack.xyz/posts/paperless-ngx-self-hosted-document-management-guide/, https://www.reddit.com/r/selfhosted/comments/1nmbuos/).
- Zone-OCR templates: rectangular regions per document type, pdftoppm rendering, coordinate scaling, custom-field targets — merged feature in 2026 (https://github.com/paperless-ngx/paperless-ngx/pull/13043).
- Data stays on the user's server; nothing transmitted (https://sourceforge.net/projects/paperless-ngx.mirror/).

### 3.3 On-device feasibility
- Not designed for on-device or embedded use: server software with Python, Redis, a task queue, and Docker orchestration. Resource profile is server-class; heavy OCR ingestion is the bottleneck (30 MB/600-page files took dramatically longer than 100 MB/3-page files on one deployment) (https://www.reddit.com/r/selfhosted/comments/17qhzhh/).
- Relevance to the notes app is as a reference architecture (ingestion pipeline, classifier, full-text indexing, archival copy), not as a component.

### 3.4 License and repo
- GPL-3.0 (https://github.com/paperless-ngx/paperless-ngx/blob/dev/LICENSE, https://sourceforge.net/projects/paperless-ngx.mirror/).
- Repo: https://github.com/paperless-ngx/paperless-ngx
- Pull assessment: GPL-3.0 = strictly concepts-only for this project. Study the UX and pipeline concepts (auto-classification from user corrections, archive vs original dual-file model, workflow engine); copy no code.

### 3.5 Real-world experience, complaints, failure modes
- Handwriting: essentially unsupported. Users asking about handwriting report Tesseract-based OCR is hit-and-miss at best for cursive/handwritten text; this is a consistent community answer (https://www.reddit.com/r/selfhosted/comments/1doy32j/).
- OCR quality ceiling: because Paperless uses OCRmyPDF which uses Tesseract, accuracy is capped by Tesseract; dirty scans and forms do poorly; many users bolt on external OCR (Google Document AI) or local LLM/vision models via paperless-gpt/paperless-ai to compensate (https://www.reddit.com/r/selfhosted/comments/1nmbuos/, https://www.reddit.com/r/selfhosted/comments/17lbzgx/, https://www.reddit.com/r/selfhosted/comments/1rug8bj/).
- Auto-classification (tags/correspondents) frequently wrong for personal-scale libraries until trained on many corrections (https://www.reddit.com/r/Paperlessngx/comments/1q45jnx/, https://www.reddit.com/r/Paperlessngx/comments/1vkfhtd/).
- Export/sync clunkiness: original vs archive file size differences, duplicate-on-rename fears without delete options (https://www.reddit.com/r/Paperlessngx/comments/1q45jnx/).
- UI feels dated/retro to some users (https://www.reddit.com/r/Paperlessngx/comments/1q45jnx/).
- Ingestion throughput on large PDFs (see 3.3).
- Insight the project should steal: "OCR is king" — every downstream feature (classification, AI, search) degrades with bad OCR text; users learned to treat OCR quality as the single most important pipeline property (https://www.reddit.com/r/Paperlessngx/comments/1vaaecd/).

### 3.6 Pull-from assessment for Rust/Tauri
- No code pull (GPL). Concept pulls: dual-file archival model, user-correction-driven classification, consumption directories, zone-OCR templates, and the community-validated lesson that an LLM pass on top of bad OCR text is worthless — get the text layer right first.

---

## 4. Apple Vision framework (text recognition)

### 4.1 What it is, maintainer, status
- Apple's first-party on-device computer-vision framework, shipping with the OS. Text recognition is exposed as VNRecognizeTextRequest ("An image-analysis request that finds and recognizes text in an image") plus a modernized Swift async API from iOS 18, and RecognizeDocumentsRequest (WWDC25) which returns structured paragraphs rather than raw lines (https://developer.apple.com/documentation/vision/vnrecognizetextrequest, https://daily.dev/posts/detecting-text-in-images-with-the-vision-framework-hckvlzdp7).
- Maintained by Apple; models ship inside the OS and are free to use, closed weights, closed source.

### 4.2 Capability picture
- VNRecognizeTextRequest: recognitionLevel .fast (live camera streams) vs .accurate (documents); language hints; automaticallyDetectsLanguage; usesLanguageCorrection; customWords (app-specific vocabulary); per-observation bounding boxes and confidence via topCandidates(_:); support for 18+ languages including Cyrillic and Arabic scripts per one 2026 survey (Apple's own supportedRecognitionLanguages() is the authoritative runtime list) (https://blakecrosley.com/blog/vision-framework-built-in, https://www.it-jim.com/blog/apple-vision-framework/, https://developer.apple.com/documentation/vision/vnrecognizetextrequest/supportedrecognitionlanguages(), https://developer.apple.com/documentation/vision/vnrequesttextrecognitionlevel?language=objc).
- Handwriting: supported in the .accurate path for a subset of languages; the accurate level is effectively required for handwriting (users found .fast fails on handwritten text and .accurate with revision pinning + custom words is the fix) (https://blakecrosley.com/blog/vision-framework-built-in, https://stackoverflow.com/questions/79582666/).
- Two API generations coexist: classic VN-prefixed classes with completion handlers, and a Swift-only async/await API (RecognizeTextRequest with @Observable, iOS 18/26) (https://www.bitcot.com/vision-framework-in-swift-for-ios-development/, https://developer.apple.com/forums/tags/vision).
- VisionKit's ImageAnalyzer wraps text recognition for DataScanner-style live use (https://developer.apple.com/forums/tags/visionkit).

### 4.3 On-device feasibility / resource profile
- Entirely on-device, no per-scan cost, works offline (https://www.bitcot.com/vision-framework-in-swift-for-ios-development/).
- No published model size or latency figures from Apple (models are opaque OS components). Community datum: one developer ran ~26,500 frame grabs through VNRecognizeTextRequest on iPadOS 18/26/27 for a regression study, confirming it is fast enough for batch use on iPad hardware, but no ms/page numbers published (https://developer.apple.com/forums/tags/visionkit). Unverified: any specific ms/page figure.

### 4.4 License
- Proprietary Apple SDK, free with the platform. Not pullable, not portable. Usage on-device is unrestricted within Apple platforms.

### 4.5 Real-world experience, complaints, failure modes
- Single handwritten letters often produce zero observations (drawn-letter recognition fails where multi-letter text works) (https://developer.apple.com/forums/tags/vision).
- Whole-line duplicates: the same text recognized twice (once as a combined line, once as individual strings), seen on real iPads on iPadOS 18/26/27 but not in the Simulator — a trap for testing (https://developer.apple.com/forums/tags/visionkit).
- Handwriting language coverage is a subset; non-supported-language handwriting degrades badly (https://blakecrosley.com/blog/vision-framework-built-in).
- General consensus among developers: excellent printed-text OCR for receipts/signage/documents on iOS 18+; handwriting is serviceable but not in the class of dedicated HTR systems (https://blakecrosley.com/blog/vision-framework-built-in).

### 4.6 Pull-from assessment for Rust/Tauri
- Not usable from Rust/Tauri except by shipping an Apple-platform native layer: a small Swift helper (via Tauri's sidecar or a Swift/Objective-C plugin bridge) exposing OCR over FFI. This is the only free on-device OCR option on macOS/iOS, so the practical architecture is: on Apple platforms use Vision via a native bridge; elsewhere use a portable engine (Tesseract/ONNX-based).
- License constraints: none beyond platform terms; no privacy concerns (on-device).

---

## 5. PencilKit (Apple) — ink + handwriting

### 5.1 What it is, status
- Apple's framework for capturing and rendering pen/touch strokes in an app: PKCanvasView captures Apple Pencil input and displays rendered results (https://developer.apple.com/documentation/pencilkit/pkcanvasview).
- Big 2026 change: WWDC26 session "Read between the strokes with PencilKit" introduces PKStrokeRecognizer, on-device handwriting recognition for PencilKit on iOS, iPadOS, macOS and visionOS 27; usage: create recognizer, updateDrawing(drawing), then recognizedText() or indexableContent; supports device languages or explicit preferredLanguages, recognition over subsets of strokes by stroke ID, and exposes supportedLanguages and recognizerVersion for language handling and re-indexing; Apple says it powers handwriting search in Freeform and Notes (https://developer.apple.com/videos/play/wwdc2026/203/, https://wwdc.ai/2026/203).
- PKStrokePath can convert to and from Bézier paths, so handwriting recognition is usable with custom canvases that do not use PKCanvasView (https://wwdc.ai/2026/203).
- Community wrappers track the new surface: PKStroke.id stable stroke ids, selection get/set, erasePath, per-point lateralJitter (https://github.com/munimtechnologies/munim-pencilkit/pull/16).

### 5.2 Capability picture
- Ink rendering with PKInkingTool (pen/marker/corrector), tilt sensitivity, pressure-driven width, undo, and system tool picker; drawingPolicy (.default/.anyInput/.pencilOnly) controls whether finger and/or pencil draw (https://getstream.io/blog/pencilkit-swiftui/, https://medium.com/@wesleymatlock/customizing-pencilkit-going-past-apples-tool-picker-b82eca7bfbe2, https://www.sagarunagar.com/blog/create-signature-canvas-in-ios/).
- Palm rejection: "comes free" — PKCanvasView's drawing gesture recognizer plus Apple Pencil digitizer input give system-level palm rejection and low latency without app work (https://github.com/caiopieri/flint/issues/13, https://getstream.io/blog/pencilkit-swiftui/). Setting drawingPolicy to .pencilOnly is the strongest palm-rejection posture (https://www.sagarunagar.com/blog/create-signature-canvas-in-ios/).
- Interaction extras: UIPencilInteraction reports double-tap and squeeze; respects the user's preferredTapAction; prefersPencilOnlyDrawing reflects the user's system-wide pencil-only preference — apps should honor it (https://developer.apple.com/documentation/uikit/uipencilinteraction, https://developer.apple.com/documentation/uikit/uipencilinteraction/preferredtapaction, https://developer.apple.com/documentation/uikit/uipencilinteraction/preferspencilonlydrawing).

### 5.3 On-device feasibility
- All on-device, OS-supplied. The recognizer's model size and latency are not published (Apple does not disclose). Unverified: any figures.

### 5.4 License
- Proprietary Apple framework, free with the platform. Not portable.

### 5.5 Real-world experience, complaints
- Drawing + finger gesture conflicts: enabling cancelsTouchesInView = false on the drawing gesture recognizer lets SwiftUI gestures and PencilKit coexist but complicates simultaneous recognition; common Stack Overflow pain point (https://stackoverflow.com/questions/76129038/).
- Custom tool pickers require bypassing PKToolPicker, which is doable but undocumented territory (https://medium.com/@wesleymatlock/customizing-pencilkit-going-past-apples-tool-picker-b82eca7bfbe2).
- The most-requested missing capability for years was handwriting recognition; PKStrokeRecognizer answers it, but only on OS 27 (https://developer.apple.com/videos/play/wwdc2026/203/).
- Comparison note from an independent project: Apple's Smart Script (iPadOS 18+) has no public API; PKStrokeRecognizer is the sanctioned path (https://github.com/Rybib/Handwriting-Fixing-System).

### 5.6 Pull-from assessment for Rust/Tauri
- Tauri on macOS/iPadOS would render via webviews, so PencilKit is not directly available; a native Swift canvas component (PKCanvasView wrapped in a native view via Tauri's macOS plugin system) is the only way to get its ink quality, latency and palm rejection. Otherwise the notes app must build its own ink stack in the webview (pointer events, pressure via PointerEvent.pressure) and lose Apple-grade latency/palm rejection.
- Concept pull: the PKStrokePath <-> Bézier conversion idea is directly relevant — store strokes as parametric curves, not rasters; that is what makes stroke-ID-addressable recognition and re-indexing possible (https://wwdc.ai/2026/203).

---

## 6. OnlineHTR (PellelNitram) — online handwriting recognition

### 6.1 What it is, maintainer, version/status
- The real project is https://github.com/PellelNitram/OnlineHTR (not AABashar). It is a clean PyTorch implementation of "Fast multi-language LSTM-based online handwriting recognition" by Carbune et al. (2020, Google), the paper at https://doi.org/10.1007/s10032-020-00350-4 (https://github.com/PellelNitram/OnlineHTR).
- Author: PellelNitram (Martin, a physics PhD researcher at Edinburgh), building it as part of xournalpp_htr to bring handwriting recognition to Xournal++ (https://github.com/PellelNitram/OnlineHTR, https://github.com/PellelNitram/xournalpp_htr, https://github.com/xournalpp/xournalpp/issues/4932).
- Status: research-grade, solo project; README "Open tasks" include CTC beam decoding with a language model, Bézier preprocessing, and publishing weights to Hugging Face (not yet done at research time) (https://github.com/PellelNitram/OnlineHTR). ~29 stars, 6 forks — small but influential within the note-taking community (https://www.libhunt.com/topic/handwritten-text-recognition).

### 6.2 Capability picture / how it works
- Online HTR: recognizes text from pen stroke time series (points with dx, dy, dt and new-stroke flag n), not from images. The reference model interpolates raw strokes to 20 points per unit length and feeds features (dx, dy, dt, n) through an LSTM network with CTC greedy decoding (https://github.com/PellelNitram/OnlineHTR).
- The source paper's system supports 102 languages with one deep architecture and reduced error rates 20–40% relative over the previous segment-and-decode system; curve-difference features cut input sequence length ~4x, which is the key to low RNN latency (https://link.springer.com/article/10.1007/s10032-020-00350-4, https://lacuna.tiptreesystems.com/work/fast-multi-language-lstm-based-online-handwriting, https://scispace.com/papers/fast-multi-language-lstm-based-online-handwriting-416h7dav06).
- Trained on IAM-OnDB (IAM On-Line Handwriting Database); pretrained weights provided for download (dataIAMOnDB_featuresLinInterpol20DxDyDtN_decoderGreedy) (https://github.com/PellelNitram/OnlineHTR).
- Companion repo xournalpp_htr holds the broader system (offline SimpleHTR word model, TrOCR experiments, PP-OCRv5 via rapidocr/ONNX, YOLO text-line detector) (https://github.com/PellelNitram/xournalpp_htr, https://github.com/PellelNitram/xournalpp_htr/pull/163).

### 6.3 On-device feasibility / resource profile
- No published parameter count or memory figures for OnlineHTR. The Carbune architecture is an LSTM over point sequences, historically designed to run in real time on device (the Google system powered Gboard handwriting); the paper reports average per-item latencies in the low hundreds of ms for the older segment-and-decode system, with the LSTM system faster — but the exact LSTM latency figure per device class is not restated here. Unverified: exact model size and ms/stroke figures.
- Offline comparators from the xournalpp_htr benchmark (Oct 2026): PP-OCRv5 recognizer-only reaches CER 28.4% (SimpleHTR 31.7%), word accuracy 42.0% (SimpleHTR 46.7%, TrOCR large 48.5%) on their handwriting eval — i.e., their handwriting task is genuinely hard and even large models land around 50% word accuracy (https://github.com/PellelNitram/xournalpp_htr/pull/163).

### 6.4 License and repos
- OnlineHTR: MIT (https://github.com/PellelNitram/OnlineHTR). xournalpp_htr: repo published openly; license of xournalpp_htr itself not confirmed at research time (unverified — check LICENSE file before pulling).
- Repos: https://github.com/PellelNitram/OnlineHTR, https://github.com/PellelNitram/xournalpp_htr
- Model weights: downloaded from the project (HF publishing listed as an open task) (https://github.com/PellelNitram/OnlineHTR).

### 6.5 Real-world experience, complaints, failure modes
- The Xournal++ integration issue (#4932) is the main public record: the author announced OnlineHTR completion in June 2024 and restarted work on shipping HTR in Xournal++ (https://github.com/xournalpp/xournalpp/issues/4932).
- Hacker News discussion crystallized the key limitation: this is stroke-order-aware "online" recognition, fundamentally different from offline OCR on scans; the open hard problem is locating text on a page in the temporal domain (segmenting continuous pen input into text lines) (https://news.ycombinator.com/item?id=41152874, https://news.ycombinator.com/item?id=41147504).
- Training data scarcity for online HTR is a community-recognized bottleneck (IAM-OnDB is the main public dataset; it requires registration and its license restricts redistribution) (https://news.ycombinator.com/item?id=41152874, https://github.com/PellelNitram/OnlineHTR).
- Greedy decoding only at present; no language model, so accuracy on unconstrained text is below commercial systems (https://github.com/PellelNitram/OnlineHTR).

### 6.6 Pull-from assessment for Rust/Tauri
- License is MIT: code and model concepts fully pullable. The architecture (point-feature LSTM + CTC) converts well: an LSTM/CTC model of this class exports to ONNX and runs on ort or candle; the preprocessing (linear interpolation to fixed points-per-length, dx/dy/dt/n features) is trivially reimplementable in Rust.
- This is the closest open-source match to the notes app's promise of on-device handwriting recognition from stylus strokes. Integration path: retrain or fine-tune on IAM-OnDB (or vendor a larger dataset), export ONNX, run via ort, implement CTC greedy decode in Rust. The missing engineering piece is temporal line segmentation/word grouping, which neither repo fully solves (https://news.ycombinator.com/item?id=41152874).

---

## 7. ArabicOCR_KHATT (Arabic handwriting OCR on KHATT)

### 7.1 What it is, repo/paper identification
- The matching repo is https://github.com/FixFips/ArabicOCR_KHATT: "Arabic handwritten text recognition using a CRNN (CNN + BiLSTM) with CTC loss, trained on the KHATT dataset", with a Gradio web demo and weights on Hugging Face (repo FixFips/arabicocr-khatt) (https://github.com/FixFips/ArabicOCR_KHATT).
- The KHATT dataset itself: KFUPM Handwritten Arabic TexT database, unconstrained handwritten Arabic from 1,000 writers, 2,000 similar-text + 2,000 unique-text paragraph images plus extracted line images with ground truth; developed by a group at KFUPM (Saudi Arabia) with TU-Dortmund and TU-Braunschweig; published as Mahmoud et al., "KHATT: An open Arabic offline handwritten text database", Pattern Recognition 47.3 (2014) (https://www.kaggle.com/datasets/nizarcharrada/khattarabic, https://huggingface.co/datasets/benhachem/KHATT, https://github.com/FixFips/ArabicOCR_KHATT).
- Access requires a request at khatt.ideas2serve.net — a gated dataset, which constrains retraining (https://github.com/rr250/Arabic-Handwritten-Text-Detection-and-Recognization, https://github.com/FixFips/ArabicOCR_KHATT).

### 7.2 Maintainer and status
- Solo project (FixFips), packaged on PyPI as arabicocr-khatt, MIT license; recent activity with an HF Space demo (https://github.com/FixFips/ArabicOCR_KHATT). Version number on PyPI not captured at research time (unverified; check PyPI).
- Related KHATT-based work for context: MUZAMMILPERVAIZ/Arabic-Handwritten-OCR (DCNN + BiLSTM + CTC, notebook-grade) (https://github.com/MUZAMMILPERVAIZ/Arabic-Handwritten-OCR); AHR-OCR2024/Arabic-Handwriting-Recognition (ResNet50V2 pretrained on Arabic Alphabet Character dataset then KHATT, 108,619 combined samples, E2E app for exam grading) (https://github.com/AHR-OCR2024/Arabic-Handwriting-Recognition); KhattTech (mobile AHR app) (https://github.com/KhattTech).

### 7.3 Capability picture / how it works (this is what makes it Arabic-specific)
- Line-level OCR (line or paragraph image to Arabic text) with automatic page line-segmentation via classical morphology (https://github.com/FixFips/ArabicOCR_KHATT).
- Architecture: input [B, 1, 96, 1536] grayscale → CNN (7 conv layers, BatchNorm, Dropout2d) → adaptive pooling into 3 vertical zones (preserving where dots sit above vs below the baseline — the only difference between ب/ت/ث and ن/ي) → 2-layer BiLSTM (1536 → 384) → FC → CTC → greedy or beam-search decoding with an Arabic character bigram language model, reversed back to RTL. 75-class charset (https://github.com/FixFips/ArabicOCR_KHATT).
- Input height 96 chosen to keep diacritic dots (3–5 px) large enough for 3×3 convolutions; dot-safe augmentation only (shear, kashida stretch, mild rotation) — erosion/dilation/elastic are banned because they destroy 2–4 px dots (https://github.com/FixFips/ArabicOCR_KHATT).
- Preprocessing: grayscale → CLAHE → dual-polarity Otsu binarization → LANCZOS resize to H=96 → pad to W=1536 (https://github.com/FixFips/ArabicOCR_KHATT).
- Evaluation includes a dot-group CER metric tracking errors on dot-differentiated letter groups, called the #1 Arabic OCR error source (https://github.com/FixFips/ArabicOCR_KHATT).
- Published CER/WER numbers were not visible on the README at research time (metrics are in the model card on HF per the upload script description); unverified: exact KHATT CER/WER figures.

### 7.4 On-device feasibility / resource profile
- A 7-layer CNN + 2-layer BiLSTM(384) CRNN is small by modern standards — this class of model is typically well under 10M parameters and runs comfortably on-device via ONNX. Unverified: exact parameter count and inference latency (not published in README).
- The bigram LM and beam search add negligible compute; the classical morphology line-segmentation step is CPU-only.

### 7.5 License
- MIT (https://github.com/FixFips/ArabicOCR_KHATT). KHATT dataset: research-access agreement required — redistribution of trained weights trained on it should be checked against the KHATT license terms before shipping in the app (unverified: whether KHATT's agreement permits derivative model weights; treat as a legal checkpoint).

### 7.6 Real-world experience, complaints, failure modes
- Documented limitations in README: performance is best on handwriting similar to KHATT; printed fonts, noisy backgrounds, or strongly curved text may fail; complex page layouts segment poorly; labels historically Windows-1256 encoded (reader falls back to UTF-8) (https://github.com/FixFips/ArabicOCR_KHATT).
- Broader Arabic-OCR ecosystem pain points from the sibling projects: generic CRNNs miss dot-position semantics entirely, which is why the 3-zone pooling and dot-group metrics exist; Arabic script's cursive connectivity, context-dependent letter shapes and diacritics are the recurring failure drivers (https://github.com/Dalia-Manel/Arabic_OCR, https://github.com/FixFips/ArabicOCR_KHATT).
- Low community traction (small star counts); Arabic OCR is described by the author as underserved (https://github.com/FixFips/ArabicOCR_KHATT).

### 7.7 Pull-from assessment for Rust/Tauri
- MIT: fully pullable. The architecture ports cleanly to ONNX (conv front-end + BiLSTM + CTC) and runs via ort in Rust; the preprocessing pipeline (CLAHE, Otsu, resize/pad) is straightforward in Rust image crates. The three-zone vertical pooling is a custom tensor reshape — easy in ONNX.
- For the notes app: this is the reference design if Arabic handwriting support is in scope, but note it is offline (image-based) OCR of rendered handwriting, not online stroke recognition; it would apply to photos/scans and to rasterized note pages. The KHATT access agreement and its derivative-weights question must be cleared with legal before bundling any weights retrained on KHATT.

---

## 8. Palm rejection technology (techniques for stylus apps to detect and reject palm touch)

This section is written for direct implementation by the notes app, so it documents concrete techniques per platform with sources.

### 8.1 The physical/sensing basis
- Palm rejection exploits the difference between fingertip and palm contact: smaller contact area, higher signal concentration. One survey describes fingertip signals peaking in under 10 ms vs palm drags of 20–50 ms, with sensors using rise/fall-time measurement; treat the specific numbers as secondary-source claims, not vendor documentation (https://roosholleman.com/article/how-does-palm-rejection-work-the-science-behind-touchscreen-precision).
- Research-level sensing goes further: grip and hold detection, distinguishing the hand holding the pen from the resting hand, using IMU signals in the stylus itself to separate intentional gestures from incidental contact (https://www.hbenko.com/publications/2014/Sensing%20Techniques%20for%20Stylus%20Tablet%20Interaction_UIST2014.pdf).
- Practical technique set used by real apps: (a) pen-priority — if any stylus is in range or down, suppress/suspend all touch; (b) contact-size heuristics — large touch major/minor axis = palm; (c) pressure-based discrimination where touch pressure differs from pen pressure; (d) cancellation handling — the OS may retroactively cancel a palm touch after recognizing it, so strokes must be undoable; (e) user-facing pen-only mode. (Synthesis of the platform docs below; this list is analysis, not a single source.)

### 8.2 iPadOS / UIKit / PencilKit
- Apple Pencil hardware reports its own touches separately from finger touches; the system-level drawingPolicy controls what PKCanvasView accepts: .pencilOnly rejects all finger/palm input, .anyInput accepts both (https://www.sagarunagar.com/blog/create-signature-canvas-in-ios/, https://medium.com/@wesleymatlock/customizing-pencilkit-going-past-apples-tool-picker-b82eca7bfbe2).
- UIPencilInteraction exposes Apple Pencil double-tap and squeeze, the user's preferredTapAction, and prefersPencilOnlyDrawing — the user's system-wide preference for pencil-only drawing, which apps are expected to honor (https://developer.apple.com/documentation/uikit/uipencilinteraction, https://developer.apple.com/documentation/uikit/uipencilinteraction/preferredtapaction, https://developer.apple.com/documentation/uikit/uipencilinteraction/preferspencilonlydrawing).
- Predicted touches: UIKit's predictedTouches(for:) on UIEvent supplies predicted future touch locations so drawing stays smooth while the real events arrive; the app draws predictions immediately and replaces them with coalesced actual touches — this is latency work that complements palm rejection (https://developer.apple.com/documentation/uikit/uievent/1613814-predictedtouches, https://developer.apple.com/documentation/uikit/touches_presses_and_gestures/handling_touches_in_your_view/minimizing_latency_with_predicted_touches, https://developer.apple.com/documentation/uikit/incorporating-predicted-touches-into-an-app).
- PencilKit's canvas handles palm rejection and Apple Pencil handling internally; native apps get it "for free" by using PKCanvasView (https://github.com/caiopieri/flint/issues/13, https://getstream.io/blog/pencilkit-swiftui/).
- For a custom canvas (webview-based, as in a Tauri app): detect pointerType === 'pen' from PointerEvents and suspend finger handling while a pen is active, honor touch cancel events, and consider a setting mirroring prefersPencilOnlyDrawing. (Implementation inference; PointerEvent.pointerType is web-standard.)

### 8.3 Android (MotionEvent / Compose)
- MotionEvent exposes everything needed: getToolType() returns TOOL_TYPE_FINGER, TOOL_TYPE_STYLUS, or TOOL_TYPE_ERASER; getPressure() reports stylus pressure; getAxisValue() with AXIS_TILT and AXIS_ORIENTATION gives stylus tilt/orientation; the stylus API surface includes hover and palm detection (https://developer.android.com/develop/ui/compose/touch-input/stylus-input/advanced-stylus-features, https://developer.android.com/develop/ui/compose/touch-input/input-compatibility-on-large-screens).
- System palm rejection sends cancellations: the Views doc documents checking event.getFlags() & FLAG_CANCELED; when set, the app must undo the last MotionEvent set back to that pointer's ACTION_DOWN, re-rendering as if the palm stroke never happened (https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/advanced-stylus-features).
- In Jetpack Compose, access the underlying MotionEvent from the PointerEvent and check ACTION_CANCEL to stop and roll back a gesture (https://developer.android.com/develop/ui/compose/touch-input/stylus-input/advanced-stylus-features).
- Android 13+ reports palm touches differently from all other API levels, so rejection logic must branch by API level; because the touch may reach the app before the system recognizes it as a palm, the app must itself identify extraneous events and ignore them (https://developer.android.com/develop/ui/compose/quick-guides/content/reject-stylus-palm-touches — URL returned 404 on direct fetch at research time; the indexed snippet is authoritative as of 2026-01).
- The official stylus codelab walks through pressure, tilt, orientation and palm rejection implementation via MotionEvent (https://developer.android.com/codelabs/large-screens/advanced-stylus-support).
- Wacom's Android docs add that getPressure() is normalized 0.0–1.0 but may exceed those bounds depending on the input driver, and historical pressure is available per historical event (https://developer-docs.wacom.com/docs/icbt/android/overview/android-basics/).
- Ecosystem reality check: palm rejection on Android is app-dependent and works reliably mainly in apps that implement it (Samsung Notes, Squid, Nebo); system-wide pressure/tilt is not exposed to most apps without custom HID/Bluetooth parsing for non-standard styluses — so a notes app cannot rely on the OS alone (https://electronics.alibaba.com/question/android-stylus-pen-guide-what-works-what-doesn%E2%80%99t-t).
  (Note: the Alibaba page URL as indexed ends -doesn%E2%80%99t; the trailing -t in the citation above is the indexed form.)

### 8.4 Windows (Windows Ink)
- The system-level palm rejection control is "Ignore touch input when I'm using my pen" in Settings → (Bluetooth &) devices → Pen & Windows Ink; when enabled, Windows suppresses touch while the pen is in use (https://www.addictivetips.com/windows-tips/enable-palm-rejection-on-windows-10-touch-screen/, https://umatechnology.org/how-to-enable-palm-rejection-on-windows-11/, https://techilife.com/how-to-turn-on-palm-rejection-windows-10/).
- Behavioral detail: with pen-then-touch ordering and the ignore setting off, touch input during pen use is aggressively ignored (suppressed) — some app developers report they cannot disable this aggressive rejection, so a notes app on Windows must design around both orders (pen-first and touch-first) (https://learn.microsoft.com/en-gb/answers/questions/2116584/).
- The digitizer reports hover distance before contact; Windows Ink uses pen approach to predict intent, engage palm rejection, and prepare pressure curves before the tip touches the display (https://macmyths.com/configure-pen-and-windows-ink-settings-in-windows-11-10/).
- Hardware-level: Microsoft's "Simultaneous pen and touch validation" guidance exists for OEM validation of palm rejection behavior, and its troubleshooting notes tie touch suppression failures partly to the system handedness setting (left/right hand) (https://learn.microsoft.com/en-us/windows-hardware/design/component-guidelines/simultaneous-pen-and-touch-validation).
- OneNote palm rejection is described as relying on this OS-level setting rather than an app-internal feature toggle (https://learn.microsoft.com/en-us/answers/questions/5285708/).
- For a Tauri (webview) app on Windows: PointerEvent.pointerType also distinguishes pen; the app should implement pen-priority suppression plus honor touch cancellations, and surface the OS setting in onboarding since inking failures are frequently traced to it being off (https://learn.microsoft.com/en-us/answers/questions/5656926/).

### 8.5 Cross-cutting implementation recommendations for the notes app (analysis, from the sources above)
- Treat palm rejection as three layers: (1) input classification (pointerType/toolType, contact geometry via touch major/minor where exposed, pressure signature), (2) policy (pen-priority suppression, user pencil-only preference, handedness-aware palm zones on the writing edge), (3) retroactive undo (ACTION_CANCEL / FLAG_CANCELED / iOS touch cancellation must revert strokes cleanly — this requires the stroke model to keep per-stroke provisional state until a grace period passes).
- Because the app is Rust/Tauri with a webview canvas, per-platform native palm rejection is NOT free (unlike PKCanvasView): the canvas must implement layer 1 and 2 itself from PointerEvents, and each OS's cancellation semantics must be mapped to web events (pointercancel). This is a first-class engineering work item, not an OS freebie, except if a native canvas component is embedded per platform.

---

## 9. Cross-cutting conclusions for the Rust/Tauri notes app

- Pullable code/models (MIT/Apache/BSD): OnlineHTR (MIT, closest match to on-device stroke HTR), ArabicOCR_KHATT (MIT, reference design for Arabic handwriting OCR with the dot-safety techniques), Docling models and schema (MIT; Granite-Docling-258M Apache 2.0), Tesseract-traineddata-based engines, PP-OCR/rapidocr ONNX models (as used in xournalpp_htr).
- Concepts-only (copyleft): OCRmyPDF (MPL-2.0), Paperless-ngx (GPL-3.0).
- Closed but free on-platform: Apple Vision (OCR incl. handwriting in a subset of languages) and PencilKit/PKStrokeRecognizer (ink + on-device handwriting recognition, OS 27) — reachable from Rust only through a native Swift/ObjC bridge per platform, never through the webview.
- Gap the ecosystem confirms: nobody has solved temporal (online) line segmentation well in open source; every open HTR effort is strong on the model and weak on "find the text lines in the pen stream" (https://news.ycombinator.com/item?id=41152874). This is where the notes app can differentiate.
- Second confirmed gap: handwriting OCR quality of general OCR stacks is poor (Paperless/Tesseract hit-and-miss; even xournalpp_htr's best large models reach ~48.5% word accuracy on their eval) (https://www.reddit.com/r/selfhosted/comments/1doy32j/, https://github.com/PellelNitram/xournalpp_htr/pull/163). On-device HTR for notes is a hard-won feature, matching the project's premise that it must be built, not bought.
- Palm rejection must be implemented in-app for a webview canvas on all three desktop platforms; the platform APIs (pointerType/toolType, tilt/orientation, cancellation flags, pencil-only preferences) are documented above and are the concrete building blocks.
