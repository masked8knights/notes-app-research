# Thread D — Indexing cost of "everything visible is searchable"

Research lane for the notes-app research project. Scope: what the app's total search
promise (PDF incl. scanned OCR, images OCR, video frame-OCR + timestamped transcription,
audio transcription, handwriting, code) costs to index, per media type; on-device state
of the art; how comparable apps structure indexes and where they quietly cheat; a cost
estimate table; bottom line; open sub-questions.

Rules followed: primary sources preferred; every number carries its source URL; anything
not verified from a source is marked **UNVERIFIED** or **ESTIMATE (derived)** with the
derivation shown. No product redesign included.

---

## 1. Per-media-type pipeline notes

### 1a. Text and code (the cheap case)
The index layer itself is a solved problem. Tantivy, a Rust full-text engine inspired by
Lucene, provides BM25 scoring, natural query language, phrase queries, incremental and
multithreaded indexing, configurable tokenizers (stemming for 17 Latin languages, plus
third-party Chinese/Japanese/Korean tokenizers), and reports indexing English Wikipedia
in under 3 minutes on one desktop; documents become searchable only after a `commit()`
and reader reload, which is the latency floor for "instant" search
(https://github.com/quickwit-oss/tantivy). Notion's lexical search is Elasticsearch with
an online per-block indexing pipeline plus periodic full rebuilds; their 2026 rebuild
post describes full reindex as a quarterly event that took several weeks and finished
with gaps before they moved to a Spark-native snapshot pipeline (now under 24 hours,
100% consistency) (https://www.notion.com/blog/rebuilding-notions-lexical-search-reindexer).
Code search adds tokenization concerns (symbols, camelCase, punctuation), for which
tantivy has no built-in answer; nothing in the sources examined covers code-specific
tokenization, so the pipeline design there is an **open sub-question** (section 8).

### 1b. Scanned PDFs and documents
The most mature open-source reference pipeline is paperless-ngx: a consumer watches an
inbox, routes by MIME type, and for PDFs runs OCRmyPDF (which wraps Tesseract) on pages
without a text layer, while Office docs go through Apache Tika/Gotenberg; extracted text
lands in a full-text index (Whoosh per one write-up of the stack)
(https://github.com/paperless-ngx/paperless-ngx; pipeline write-ups:
https://deepwiki.com/paperless-ngx/paperless-ngx/4.2-ocr-and-text-extraction,
https://dev.to/pickuma/paperless-ngx-self-hosted-document-management-for-developers-who-want-the-api-dgm).
Key design lesson: skip pages that already have a text layer ("skip-text" behavior;
paperless users have to pass `--force-ocr` to re-OCR
https://github.com/paperless-ngx/paperless-ngx/discussions/9078). Docling generalizes
this to layout-aware parsing: a linear per-page pipeline of PDF backend → layout model →
table structure model → pluggable OCR engine (Tesseract, EasyOCR, RapidOCR, macOS Vision,
SuryaOCR), producing a unified document representation
(https://github.com/docling-project/docling, technical report
https://arxiv.org/html/2408.09869v5, engine catalog
https://docling-project.github.io/docling/usage/model_catalog/). Layout+table models are
a quality/cost dial: Docling's own guidance says to prefer OCR-pipeline mode when speed
matters and GPU is unavailable (https://github.com/docling-project/docling-graph/blob/main/docs/fundamentals/pipeline-configuration/docling-settings.md).
OCRmyPDF defaults to a 180-second-per-page Tesseract timeout as its backstop
(https://ocrmypdf.readthedocs.io/en/latest/advanced.html).

### 1c. Images (photos, screenshots, handwriting)
Same OCR engine, single image per unit of work. On Apple platforms the OS ships the
engine: Vision's VNRecognizeTextRequest finds and recognizes text in images with a fast
path and an accurate path (WWDC session
https://developer.apple.com/videos/play/wwdc2019/234/), runs on Neural Engine / GPU /
CPU, "in a few milliseconds for most operations," at zero per-call cost, fully on-device
(https://blakecrosley.com/blog/vision-framework-built-in). Live Text extends this to
handwriting in images and to text in video on-device
(https://zengo.eu/en/blog/apple-ocr-revolutionizing-text-recognition,
https://www.reddit.com/r/macapps/comments/1rgzllm/ocr_options_for_macos_on_screen_in_images_on_the/).
It can even be plugged in as an OCRmyPDF engine
(https://github.com/mkyt/ocrmypdf-AppleOCR). Cross-platform, PaddleOCR's PP-OCRv6 family
ships mobile-tier models of 4–8 MB for CPU/edge and server tiers for GPU, ONNX-exportable
(https://www.forasoft.com/learn/ai-for-video-engineering/articles-ai/paddleocr-text-detection-video,
https://github.com/PaddlePaddle/PaddleOCR). Accuracy caveat for the handwriting promise:
PaddleOCR's own recognition scores for handwritten Chinese/English are far below printed
text (0.58 vs 0.90 weighted accuracy for v5 server rec
https://github.com/PaddlePaddle/PaddleOCR/blob/main/docs/version3.x/algorithm/PP-OCRv5/PP-OCRv5.en.md),
so "handwriting searchable" is a much weaker guarantee than "printed text searchable."

### 1d. Video (frame OCR + timestamped transcription)
The proposed approach — reuse the image-OCR pipeline on sampled frames — is exactly what
existing open-source pipelines do:
- FrameScout, an offline desktop search engine for local images/videos, extracts video
  frames at a fixed 1 FPS and OCRs them, and lists scene-detection-based extraction as a
  future improvement (https://github.com/bobgsning/FrameScout).
- VideoIndex (open-source, Rust core) indexes long video once into speech, on-screen
  text, frames and scenes on a shared timebase so agents can search and cite moments
  (https://www.videoindex.org/).
- A video-text pipeline repo does frame detection → perspective correction → OCR →
  consolidation of per-frame results into phrase-level records
  (https://github.com/sgrischenko8/OCR).
- CaptiOCR continuously OCRs a screen region with Tesseract and de-duplicates repeated
  text with ROVER + TF-IDF novelty scoring (https://github.com/carlosacchi/captiocr).
- Academic prior art (CMU, Video OCR): analyze frames to find text regions, binarize,
  run OCR, feed text into search indexes; deep frame analysis improved retrieval
  (http://www.cs.cmu.edu/~dipanjan/pubs/VOCR_draft.pdf).
- As a managed-service background point only: Twelve Labs offers API-level on-screen
  text extraction and text-in-video search without owning OCR infrastructure
  (https://www.twelvelabs.io/blog/how-to-perform-video-ocr-using-twelve-labs-api).
- A 2026 ecosystem gap confirms this is not commodity: a video-search tool's open issue
  asks for exactly this feature because slides/dashboards in screen recordings are
  unsearchable today (https://github.com/gabe-santana/saccade/issues/5).

Performance anchors: PaddleOCR's detection model costs ~383 ms per image on CPU
(standard mode, server tier) (https://github.com/Felix-lxd/PaddlePaddle-PaddleOCR/blob/main/docs/version3.x/pipeline_usage/OCR.en.md);
PaddleOCR v3.7 reports 5.2x CPU speedup (OpenVINO) over the previous server tier and
6.1x on Apple M4 for the tiny tier (https://github.com/PaddlePaddle/PaddleOCR/releases).
At 1 FPS sampling, 1 hour of video = 3,600 frames; per-frame OCR cost therefore
dominates video indexing cost by orders of magnitude over transcription (see table).
Frame sampling rate is the single biggest cost dial and none of the open-source
pipelines publishes quality-vs-FPS curves: **UNVERIFIED** how low FPS can go before
on-screen text search degrades badly.

### 1e. Audio
Transcription via Whisper-family models. whisper.cpp runs fully offline on CPU/Apple
Silicon: on an M2 Pro, 60 s of audio transcribes in 2.8 s with the base model (9% WER)
and 21 s with the medium model (https://tokrepo.com/en/workflows/whisper-cpp-local-speech-text-pure-c-c-e1fd7c46);
benchmark compilations put Apple-Silicon real-time factors at roughly 20–30x real-time
for tiny/base and 2.5–5x for medium/large
(https://justvoice.ai/blog/whisper-benchmark-apple-silicon-m3-m4,
https://getspeakup.app/blog/whisper-cpp-benchmark-mac/). On NVIDIA GPUs faster-whisper
reaches ~12x real-time for large-v3 (https://www.promptquorum.com/power-local-llm/local-whisper-stt-comparison-2026).
Model-size/quality tradeoff table with WER per tier is in
(https://vexascribe.com/whisper-cpp) — tiny ~10% WER vs large baseline, base ~7%, medium ~3%.
Timestamps (needed for the "jump to the moment" promise) are a native Whisper output;
no source examined quantifies timestamp precision: **UNVERIFIED**.

### 1f. Handwriting
Covered by the OCR engines above (Apple Live Text handles handwriting in images;
PaddleOCR publishes separate handwriting accuracy, markedly lower than printed).
No source examined covers handwriting in PDFs from stylus apps beyond Evernote's
behavior (see 2c). Dedicated on-device handwriting-recognition state of the art beyond
these engines was not researched: **UNVERIFIED / gap**.

---

## 2. On-device state of the art, and what realistically falls back

- Images/PDF pages: on-device is genuinely viable on Apple platforms (Vision framework,
  Neural Engine, milliseconds per image, no network
  https://blakecrosley.com/blog/vision-framework-built-in) and workable cross-platform
  with mobile-tier PaddleOCR models of 4–8 MB
  (https://www.forasoft.com/learn/ai-for-video-engineering/articles-ai/paddleocr-text-detection-video).
- Audio: on-device viable with whisper.cpp/tiny/base; quality tier (medium/large) pushes
  toward GPU or server fallback (https://tokrepo.com/en/workflows/whisper-cpp-local-speech-text-pure-c-c-e1fd7c46,
  https://www.promptquorum.com/power-local-llm/local-whisper-stt-comparison-2026).
  Low-end phones and long recordings realistically fall back to first-sync or queued
  processing. No source examined measures on-device STT on Android/mobile NPUs: **UNVERIFIED**.
- Video: frame-OCR at 1 FPS on CPU is hours of compute per hour of video (table below);
  every open-source implementation that does it is desktop-class, offline-first, and
  none does it on phones. Realistic design: phone falls back to server or defers video
  indexing to desktop/sync; no source documents a mobile video-OCR product: **UNVERIFIED**.
- Scanned PDFs: Tesseract-class OCR on CPU is minutes per hundred pages (table); on
  device it must be a background queue. Paperless-ngx and Docling are both
  server/desktop pipelines; neither is a mobile OCR reference: **gap**.
- Desktop-only OS OCR (Apple Vision) is unavailable on Windows/Linux, so a
  cross-platform app needs its own engine there (Tesseract/ONNX PaddleOCR). No source
  compares on-device OCR quality across Windows/Linux options: **UNVERIFIED**.

---

## 3. How comparable apps structure indexes, and where they cheat on "always"

- **Evernote.** Documents the promise: search inside PDFs, Office files, images,
  presentations and scanned documents, with handwriting search in images, plus semantic
  search — but a hard limit of 52 MB per PDF processed for search, and OCR for PDF
  search is a paid-tier feature (Personal and up; Plus is not eligible)
  (https://help.evernote.com/hc/en-us/articles/360040282613-Search-overview,
  https://evernote.com/features/search,
  https://discussion.evernote.com/forums/topic/141482-existing-pdf-and-jpg-documents-get-ocr-and-hence-become-searchable-when-i-upgrade-to-personal-is-this-correct/).
  The OCR is described as running on Evernote's servers in the background, writing
  results into a hidden section of the note rather than into the file, so the OCR index
  is lost on export and exists only inside Evernote
  (https://pdf.wondershare.com/ocr/evernote-alternatives.html,
  https://www.reddit.com/r/Evernote/comments/1afc4z7/evernote_ocr_to_the_rescue/,
  https://univik.com/blog/evernote-pdf-to-text.html). Community documentation also says
  images inside PDFs are not OCRed, only standalone image attachments
  (https://discussion.evernote.com/forums/topic/146672-challenges-with-evernotes-ocr-functionality-and-document-searchability/).
  Cheats: server-side only OCR; 52 MB cap; paid tier; no video and no audio
  transcription promise at all in the sources examined.
- **Notion.** Lexical search is server-side Elasticsearch, rebuilt fully on a schedule;
  the 2026 post describes full reindex as historically multi-week with ~90% consistency
  before the Spark rebuild (now under 24 h, 100%) — i.e., freshness was maintained by an
  online pipeline with periodic heavy reconciliation, and attachments/media are not part
  of the promise (https://www.notion.com/blog/rebuilding-notions-lexical-search-reindexer).
  Third-party writeups note search scope degrades for deep/old pages and that
  block-level content search is unreliable in practice
  (https://www.askoro.dev/blog/notion-search-not-working-fix). Vector (AI Q&A) search is
  a separate dual-path architecture: Spark batch embedding plus a Kafka real-time path
  (https://www.zenml.io/llmops-database/scaling-vector-search-infrastructure-for-ai-powered-workspace-search-352f8dff).
  Cheats: no attachment indexing in lexical search; freshness guaranteed only for the
  server-side, cloud-only product.
- **Obsidian + Omnisearch plugin.** The closest on-device analogue: a BM25 engine
  (MiniSearch) inside the app, indexing notes, PDFs, Office docs and images via a
  companion "Text Extractor" plugin, with typo tolerance; it won Obsidian's 2023 Gems of
  the Year (https://github.com/scambier/obsidian-omnisearch,
  https://community.obsidian.md/plugins/omnisearch). Cheats: OCR depends on a separate
  plugin and the platform's text extraction; Chinese support needs yet another plugin;
  index serialization is opt-in for load speed; no video or audio support at all; it is
  desktop-only (Electron), so "on-device" means "on a laptop," not on a phone
  (https://github.com/scambier/obsidian-omnisearch,
  https://github.com/scambier/obsidian-omnisearch/releases/tag/1.4.0).
- **DEVONthink.** Imports or *indexes* files in place, maintains a concordance of all
  words in a database, and layers See Also/Classify similarity features on top; indexing
  is explicitly recommended only for "fairly static locations," i.e., freshness is a
  known compromise (manual: https://download.devontechnologies.com/download/devonthink/3.5.1/DEVONthink%20Manual.pdf,
  https://download.devontechnologies.com/download/devonthink/3.0.4/DEVONthink%20Manual.pdf;
  concordance docs: https://download.devontechnologies.com/download/devonthink/3.8.2/DEVONthink.help/Contents/Resources/pgs/inspectors-concordance.html,
  https://download.devontechnologies.com/download/devonthink/3.8.2/DEVONthink.help/Contents/Resources/pgs/tasks-analyzing.html).
  Cheats: macOS-only; no cloud, no mobile-first promise; media transcription is not part
  of the documented search feature set examined.
- **Paperless-ngx** (documents only, but the honest pipeline): everything is queued
  through a consumer; OCR runs server-side on your own hardware; nothing is
  instant. That it does not even try to be instant is the instructive part
  (https://github.com/paperless-ngx/paperless-ngx,
  https://deepwiki.com/paperless-ngx/paperless-ngx/4-document-processing-pipeline).

Pattern across all of them: nobody keeps the "always" promise everywhere. The universal
compromises are (a) server-side OCR hidden behind a client search box (Evernote, Notion),
(b) heavy media simply excluded (Obsidian, DEVONthink, Notion lexical), (c) deferred
background queues with no freshness guarantee (paperless-ngx, Evernote's OCR lag,
DEVONthink's static-location advice), and (d) size caps (Evernote's 52 MB).

---

## 4. Cost estimate table (CPU time per GB of media)

All per-GB figures are **ESTIMATE (derived)** from the cited per-unit numbers; derivations
shown so they can be checked. Assumptions per row are stated. No invented measured
numbers.

| Media type | Unit cost (sourced) | Assumption for 1 GB | Est. CPU time per GB |
|---|---|---|---|
| Plain text / code | Tantivy indexes English Wikipedia (<3 min on one desktop) — https://github.com/quickwit-oss/tantivy | Wikipedia ≈ tens of GB of text | **Minutes per GB** (sub-minute in practice) |
| Scanned PDF page, Tesseract CPU | 0.5–2 s/page (user report) — https://www.reddit.com/r/commandline/comments/h9lj6w/; 24 pages/45 s — https://aiundecided.com/tools/ocr-comparison/; 60 pages/10–64 s public benchmark — https://openbenchmarking.org/test/system/ocrmypdf; ~3–5 s/page sequential — https://fastocr.org/blog/ocr-accuracy-comparison-benchmarks; 180 s/page timeout backstop — https://ocrmypdf.readthedocs.io/en/latest/advanced.html | 300-dpi grayscale page ≈ 0.5–1 MB → ~1,000–2,000 pages/GB | **~1–3 CPU-hours per GB** central case; up to ~10 h at the slow end |
| Image, Apple Vision on-device | "a few milliseconds for most operations" — https://blakecrosley.com/blog/vision-framework-built-in | 1 GB ≈ ~300 photos of 3 MB | **≈ minutes per GB** on Apple Neural Engine (order-of-magnitude; no published per-image ms figure found — **UNVERIFIED**) |
| Image, PaddleOCR CPU | ~383 ms/image detection (server tier, standard mode) — https://github.com/Felix-lxd/PaddlePaddle-PaddleOCR/blob/main/docs/version3.x/pipeline_usage/OCR.en.md; 5.2x CPU speedup in v3.7 — https://github.com/PaddlePaddle/PaddleOCR/releases | 1 GB ≈ ~300 photos, or ~2,000 screenshots of 0.5 MB | ~2 min/photo-equivalent → **~10 CPU-hours per 1,000 images**; tiny tier cuts this several-fold |
| Audio, whisper.cpp base on Apple Silicon | 60 s audio in 2.8 s (M2 Pro) — https://tokrepo.com/en/workflows/whisper-cpp-local-speech-text-pure-c-c-e1fd7c46; medium: 21 s/60 s | 128-kbps MP3 ≈ 57.6 MB/h → ~17.4 h/GB | base: ~48 min/GB; medium: ~6 CPU-hours/GB |
| Audio, whisper.cpp large on Apple Silicon GPU | RTF ~1.0–2.6x (M1–M4) — https://justvoice.ai/blog/whisper-benchmark-apple-silicon-m3-m4 | same | **~7–17 GPU-hours per GB** (borderline non-viable on-device) |
| Video, frame OCR at 1 FPS, PaddleOCR CPU | ~383 ms/frame — same source as above | 1 GB ≈ 1–2 h of video → 3,600–7,200 frames | **~15–30 CPU-hours per GB** before transcription; tiny tier and OpenVINO/M4 speedups reduce it, GPU removes the bottleneck |
| Video, transcription only (audio track) | as audio row | audio track ≈ 1–2 h/GB | ~1–12 h depending on model tier |

Reading of the table: the index itself (Tantivy) is noise; OCR of static documents is
background-queue-sized; audio is manageable at small model tiers; video frame-OCR is the
cost center, growing linearly with sampling rate, and is what no comparable app has
shipped.

---

## 5. Bottom line

1. The full-text index is trivially cheap and well-served by Tantivy-class engines; all
   real cost sits in media understanding, and it is CPU/GPU time, not index size.
2. Every comparable app that advertises deep search quietly limits it: server-side OCR
   behind paid tiers and size caps (Evernote), cloud-only lexical search with periodic
   multi-week rebuilds (Notion), desktop-only OCR via optional plugins and no media
   search (Obsidian Omnisearch), macOS-only with freshness caveats (DEVONthink). None
   offers video; none offers audio transcription in the sources examined. The "always"
   promise has no precedent at parity.
3. The proposed video approach (reuse image-OCR on sampled frames) is exactly what
   open-source pipelines do (FrameScout at fixed 1 FPS, VideoIndex, per-frame
   consolidation pipelines), so it is precedented — but only on desktop-class hardware,
   and frame-sampling rate is the dominant cost dial with no published quality curves.
4. On-device is real for images (Apple Vision, milliseconds/image) and plausible for
   audio at small Whisper tiers; it is not real for video OCR on phones today, and
   handwriting accuracy is categorically weaker than printed-text accuracy in the
   engines' own benchmarks.
5. First-sync/network fallback is not a cheat in this landscape; it is what the market
   leaders already do, invisibly (Evernote's server OCR, Notion's cloud index). A
   desktop/background-queue model with server fallback for mobile is the pattern the
   evidence supports.

---

## 6. Open sub-questions

- Code tokenization for the index (symbols, camelCase) — no source examined covers it.
- Frame-sampling rate vs on-screen-text recall: is 1 FPS enough, is 0.2 FPS usable? No
  published curves found (**UNVERIFIED**).
- On-device STT quality on Android NPUs; cross-platform OCR (Windows/Linux) quality vs
  Tesseract baseline (**UNVERIFIED**).
- Whisper timestamp precision for "jump to the moment" UX (**UNVERIFIED**).
- Incremental re-indexing cost after edits to large media files (do you re-OCR the
  whole video/PDF?): none of the pipelines examined answers this.
- Memory footprint of OCR engines on mobile (Docling workers hold ~2 GB RAM per parser
  process per one third-party writeup — https://github.com/dhananjayve/doc-ocr-pipeline —
  which would rule out phone deployment for layout models).
- Handwriting-specific engines beyond Vision/PaddleOCR were not researched.
