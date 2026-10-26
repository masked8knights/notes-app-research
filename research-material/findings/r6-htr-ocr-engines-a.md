# R6 Findings — Handwriting Recognition & OCR Engines, Batch A

Lane: handwriting-recognition and OCR engines, batch A. Target context: local-first Rust/Tauri notes app promising on-device handwriting recognition and OCR everywhere with no setup, on laptops and mid-range phones.
Method: web searches + direct reads of official docs/READMEs/benchmark pages, one engine at a time. Every claim carries its source URL in parentheses. Anything I could not verify this session is marked unverified explicitly.

Engines covered: Google ML Kit (Digital Ink + Text Recognition v2), TrOCR family, PARSeq, docTR, Tesseract, PaddleOCR (PP-OCRv4/v5).

---

## 1. Google ML Kit (Digital Ink Recognition + Text Recognition v2)

### 1.1 What it is, maintainer, status
ML Kit is Google's on-device ML SDK for mobile. The relevant pieces are two separate APIs. Digital Ink Recognition converts pen/touch stroke data into text; Text Recognition v2 does printed-text OCR from camera/document images. Both are actively maintained by Google as part of the ML Kit product (current digital-ink Android artifact `com.google.mlkit:digital-ink-recognition:19.0.0`) (https://developers.google.com/ml-kit/vision/digital-ink-recognition/android). Text Recognition v2 added Chinese, Devanagari, Japanese and Korean scripts on top of Latin (https://developers.google.com/ml-kit/release-notes). Docs pages were last touched in 2024–2026; the SDK is a moving, Google-controlled target.

### 1.2 Capabilities
- Digital ink takes stroke data (`Ink` objects built from touch/pen events), not images and not text (https://developers.google.com/ml-kit/vision/digital-ink-recognition/android, https://developers.googleblog.com/2020/08/announcing-digital-ink-recognition-in.html). Input is point lists with timestamps; the recognizer is aware of stroke order (it expects natural writing order) and of a writing area. It supports "hundreds of languages" plus handwriting-gesture classifiers (erase, select, insert...) and emoji/auto-draw/shape classifiers as separate models (https://developers.google.com/ml-kit/vision/digital-ink-recognition/android, https://developers.google.com/ml-kit/vision/digital-ink-recognition/base-models).
- Important architectural assumption: the recognizer assumes the writing area contains a single line of text; multi-line writing must be fed line-by-line, and the app must merge results (https://developers.google.com/ml-kit/vision/digital-ink-recognition/android).
- Context features: pre-context (up to 20 characters of preceding recognized text) and writing-area size meaningfully improve accuracy (the docs give the n/u-in-cursive and word-break examples) (https://developers.google.com/ml-kit/vision/digital-ink-recognition/android).
- Text Recognition v2 is image-based OCR for Latin, Chinese, Devanagari, Japanese, Korean; it returns block/line/element/symbol structure with bounding boxes, confidence, and per-element language identification (https://developers.google.com/ml-kit/vision/text-recognition/v2). It targets printed text (receipts, business cards, documents); handwriting-in-photos quality is not a documented strength. Google does publish that v2 can automate data entry for documents like credit cards and receipts (https://developers.google.com/ml-kit/vision/text-recognition/v2).

### 1.3 On-device feasibility (numbers)
- Digital ink: ~20 MB of storage is required per downloaded language model, downloaded on demand via Google's RemoteModelManager (https://developers.google.com/ml-kit/vision/digital-ink-recognition/android). This is the only size figure Google publishes; inference latency and memory footprint of the recognizer are not published (https://developers.google.com/ml-kit/vision/digital-ink-recognition/android — no numbers on page; unverified elsewhere). Recognition happens on-device after the model is downloaded, so it works offline once a model is present (https://developers.google.com/ml-kit/vision/digital-ink-recognition/android).
- Text recognition v2: two install modes, "bundled" (models shipped in the app, larger app size, faster init) vs "unbundled" (downloaded via Google Play Services, smaller app) (https://developers.google.com/ml-kit/vision/text-recognition/v2/android). A third-party writeup estimates the bundled model at roughly 5–10 MB (and ~3 MB unbundled) (https://cyberraiden.com/2025/09/09/uses-of-googles-ml-kit-a-mobile-software-development-kit-in-android-devices/ — third-party estimate, unverified against official docs). Google's own messaging on a v2 update reported runtime memory decreasing from about 19.4 MB to about 11.1 MB, a ~42% reduction (https://xdaforums.com/t/greater-text-recognition-precision-from-ml-kit.4514103/, https://forums.developer.huawei.com/forumPortal/en/topic/0203103186947400043 — both secondhand reproductions of Google's announcement; treat as approximate). No per-device latency table is published; the API is marketed as real-time on a wide range of devices (https://developers.google.com/ml-kit/vision/text-recognition/v2/android).
- Quantization: not applicable to the developer; the binaries are opaque, pre-quantized by Google.

### 1.4 License
Proprietary. The ML Kit Android/iOS SDKs are distributed under Google's terms of service, not an open-source license; the models are Google binaries fetched from Google servers. Documentation text is CC-BY 4.0, which does not license the SDK or models (https://developers.google.com/ml-kit/vision/text-recognition/v2 — license footer; https://developers.google.com/ml-kit/terms). This is the critical constraint: the concepts can be studied, the code/models cannot be pulled or self-hosted.

### 1.5 Real-world experience
- Developers consistently note the model-download flow (RemoteModelManager) and the single-line writing-area assumption as the main integration frictions for note-taking apps (https://developers.google.com/ml-kit/vision/digital-ink-recognition/android; community reports, e.g. Flutter plugin issues, unverified specifics).
- ML Kit supports only mobile: Android and iOS, 64-bit only (x86_64, arm64); no desktop and no web support, which is the recurring complaint from cross-platform app developers (https://pub.dev/packages/google_mlkit_text_recognition).
- Accuracy on real handwriting is reported as good for the languages with dedicated models, variable across users and writing styles by Google's own docs ("results can vary from user to user") (https://developers.google.com/ml-kit/vision/digital-ink-recognition/android).
- For photos of paper: Text Recognition v2 is solid on clean printed documents; published real-world benchmarks of handwriting-in-photo quality are scarce. No credible independent handwriting benchmark exists for either ML Kit API (digital ink cannot even be benchmarked on IAM since IAM is image-based). This absence is itself a finding.

### 1.6 Benchmark evidence
No credible public benchmark. ML Kit does not publish IAM/CER/WER numbers for digital ink or v2, and its closed nature makes independent image-based evaluation awkward (digital ink takes no images at all, so standard OCR benchmarks do not apply). Third-party comparisons exist but none rigorous. Honest conclusion: nothing benchmarkable here.

### 1.7 Pull-from assessment for Rust/Tauri
- Desktop (the main Tauri target): unusable. ML Kit does not ship for Windows/macOS/Linux and there is no Rust binding (https://pub.dev/packages/google_mlkit_text_recognition).
- Mobile (Tauri v2 can embed native plugins): usable via a thin Tauri plugin that calls the Android SDK (`com.google.mlkit:digital-ink-recognition:19.0.0`) or iOS equivalent, bridging Ink objects from the app's canvas (https://developers.google.com/ml-kit/vision/digital-ink-recognition/android). Models download from Google servers, which conflicts with a "local-first, no setup" promise unless models can be bundled or mirrored (the API does not officially support bundling; unverified workaround status).
- License constraints: proprietary SDK terms. Code can never be pulled into the project; only the mobile-plugin approach, with Google as a hard dependency.

---

## 2. TrOCR family (microsoft/trocr-base, trocr-large, handwritten variants)

### 2.1 What it is, maintainer, status
TrOCR is a transfer-learning OCR model family from Microsoft Research (repo `microsoft/unilm`, `trocr` subfolder), published in the paper "TrOCR: Transformer-based Optical Character Recognition with Pre-trained Models" (arXiv 2109.10282). Architecture: ViT-style image encoder (DeiT/BEiT) + text-decoder (RoBERTa), fine-tuned end to end. The repo README lists the released checkpoints and remains the canonical index (https://github.com/microsoft/unilm/blob/master/trocr/README.md). Model cards on Hugging Face were authored by the HF team; the weights have been stable since ~2022–2023, with research descendants but no new TrOCR checkpoints.

Checkpoints per the README table (https://github.com/microsoft/unilm/blob/master/trocr/README.md):
- trocr-small (62M params), base (334M), large (558M) — stage-1 models pretrained on synthetic data.
- trocr-small/base/large-handwritten — fine-tuned on IAM (English handwriting): IAM CER 4.22% (small), 3.42% (base), 2.89% (large).
- trocr-small/base/large-printed — fine-tuned on SROIE (printed receipts): F1 95.86/96.34/96.60.
- Scene-text word accuracy (testset11k): small 84.36, base 87.79, large 90.02; STR benchmark ~85.74/88.55/90.23 (https://github.com/microsoft/unilm/blob/master/trocr/README.md).

### 2.2 Capabilities
- Handwriting: the handwritten variants are line-level HTR models. State of the art among open weights on IAM at release (2.89% CER for large); still competitive per the okraPDF survey below.
- Printed OCR: strong on receipts/lines (SROIE F1 ~96) but it is a line-level recognizer, not a page parser: it takes a single text-line image (384 px input per the updated README; 448 px in the legacy config) and must be fed cropped lines (https://github.com/microsoft/unilm/blob/master/trocr/README.md).
- Languages: official handwritten checkpoints are English (IAM); printed SROIE is English. Community fine-tunes exist for other languages (e.g., a French TrOCR variant published with dev-set CER 5.75% / WER 16.51%, https://dataloop.ai/library/model/agomberto_trocr-large-handwritten-fr/ — third-party listing, unverified).
- Input types: images only (line crops). No ink-stroke support at all.

### 2.3 On-device feasibility
- Sizes: 62M / 334M / 558M parameters per the README table (https://github.com/microsoft/unilm/blob/master/trocr/README.md). In fp16 that is roughly 0.12 GB / 0.67 GB / 1.1 GB before overhead (arithmetic from param counts; fp16 weight files on HF confirm the base model at a few hundred MB — unverified exact file sizes this session).
- Latency: autoregressive token-by-token decoding makes it slow relative to CTC/parallel decoders. The paper includes inference-time tables on IAM, but practical CPU numbers are not published by Microsoft (https://arxiv.org/pdf/2109.10282 — Table 5; https://github.com/microsoft/unilm/blob/master/trocr/README.md). Community reports describe seconds-per-line on CPU for base/large — plausible but unverified. On a mid-range phone, base/large are heavy; small is the only realistic CPU variant, at the cost of CER (4.22% vs 2.89%).
- Quantization: no official quantized releases. ONNX export via Hugging Face `optimum` is the standard path; community ONNX conversions exist (e.g., on Hugging Face hub; unverified which are maintained). ONNX Runtime int8/fp16 quantization is applicable in principle (unverified specific success reports for the handwritten checkpoints).

### 2.4 License
MIT. The unilm repo and the TrOCR model cards are MIT (https://github.com/microsoft/unilm/blob/master/trocr/README.md, https://huggingface.co/microsoft/trocr-base-handwritten). Code and weights can both be pulled and embedded.

### 2.5 Real-world experience
- Widely used as the open-source handwriting baseline; the okraPDF benchmark authors note TrOCR-large remains the best non-VLM open-source handwriting OCR on IAM-style data (https://okrapdf.com/blog/handwriting-ocr-benchmark/).
- Known weaknesses on real-world handwriting: it is trained on IAM, which is written-form English, so performance degrades on other domains, styles, and languages; it hallucinates plausible text when shown noise/blank regions (community-reported; consistent with autoregressive decoders; unverified formal study). Page-level use requires external line segmentation, which is where most integration pain comes from (https://github.com/microsoft/unilm/blob/master/trocr/README.md; general community reports, unverified).
- On low-quality phone photos of paper: no official robustness data; the model expects clean line crops, so detection+deskew+binarization preprocessing dominates the result (unverified, inferred from architecture and community reports).

### 2.6 Benchmark evidence
- IAM, official: CER 4.22 / 3.42 / 2.89 for small/base/large-handwritten (https://github.com/microsoft/unilm/blob/master/trocr/README.md).
- okraPDF's independent IAM-lines eval (120-line sample): TrOCR-large scored 3.68% CER, best among non-VLM open-source engines tested (https://okrapdf.com/blog/handwriting-ocr-benchmark/). The same source's literature survey lists HTR-JAND at 1.23 CER and GPT-4o-mini at 1.71 CER as reported SOTA references, and warns that historical handwriting collapses VLMs to 70–98% CER; it also notes commercial HTR vendors publish no IAM CER (https://okrapdf.com/blog/handwriting-ocr-benchmark/).
- Caution on the metric: okraPDF shows that CER/WER comparisons flip depending on tokenization conventions, so cross-paper numbers must be compared carefully (https://okrapdf.com/blog/handwriting-ocr-benchmark/).

### 2.7 Pull-from assessment for Rust/Tauri
- Path: export ONNX from HF checkpoints (optimum), run inference with the Rust `ort` crate (ONNX Runtime), do line detection + preprocessing in Rust (`image`, OpenCV alternatives). This is a realistic, license-clean integration: MIT weights, MIT code.
- Costs: model size (0.12–1.1 GB fp16), autoregressive latency on CPU, and the need to build/borrow line segmentation. A notes app could ship trocr-small-handwritten (~62M params) as the feasible on-device option and accept its 4.22% CER, or base/large for laptop-only use.
- No Rust bindings exist for the original (PyTorch); ONNX is the only realistic bridge (unverified that any maintained ONNX handwritten checkpoint exists off-the-shelf — may need self-export).

---

## 3. PARSeq (scene text recognition)

### 3.1 What it is, maintainer, status
PARSeq ("Scene Text Recognition with Permuted Autoregressive Sequence Models", ECCV 2022, Bautista & Atienza), reference implementation in `baudm/parseq`. A single Transformer that unifies context-free/context-aware decoding via permutation language modeling, avoiding a separate language model (https://github.com/baudm/parseq). It ranked #1 overall for STR on Papers With Code at release (2022-07) and was adopted by PaddleOCR (2023-09) and docTR (2023-06) as a recognition backend (https://github.com/baudm/parseq — repo News). Repo updated for PyTorch 2.0 / Lightning 2.0 in Feb 2024; activity since then is modest.

### 3.2 Capabilities
- Word-level scene-text recognition: takes a 32x128 cropped word image, 94-character vocabulary + EOS, max label length 25 (https://github.com/baudm/parseq).
- Benchmark accuracy (lowercase alphanumeric, from the README's reproduction of Table 6): IIIT5k 99.00, SVT 97.84, IC13 98.13, IC15 89.22, SVTP 96.90, CUTE80 98.61, combined 95.95 (https://github.com/baudm/parseq).
- NOT a handwriting engine: trained on synthetic scene text (MJSynth/SynthText + real STR sets), street-sign/shop-sign vocabulary. It is the wrong tool for sentence-level handwriting; usable at most for single-word crops.

### 3.3 On-device feasibility
- The README's own benchmark run reports the base PARSeq model at 23.833M parameters and 3.255 GFLOPs, median 14.87 ms per forward on the author's benchmark setup (hardware not stated in the README sample output) (https://github.com/baudm/parseq). Smaller variants (`parseq_tiny`, `parseq_patch16_224`) exist and were designed for accuracy/latency tradeoffs (https://github.com/baudm/parseq). This is the best-documented CPU-relevant profile of anything in this batch: ~24M params is genuinely phone-friendly.
- Export: the README FAQ says TorchScript and ONNX export are possible, pointing to issue #12 (https://github.com/baudm/parseq). Real deployment friction exists: subsequent issues report ONNX vs Torch output mismatches and export warnings (issue tracker; specifics unverified this session).

### 3.4 License
Apache-2.0 for the majority of the code; ABINet-derived sources BSD and CRNN sources MIT (https://github.com/baudm/parseq — NOTICE/LICENSE section). Weights are freely usable. Pull-safe.

### 3.5 Real-world experience
- Developers report it as the best-accuracy small STR recognizer; it ships inside docTR and PaddleOCR precisely because of the accuracy-per-FLOP profile (https://github.com/baudm/parseq — News; https://github.com/mindee/doctr).
- Weaknesses on the target use case: scene-text domain only; 94-char Latin-ish vocabulary blocks most non-Latin scripts without retraining (issue #5/#9 cover new-language training) (https://github.com/baudm/parseq — FAQ).
- Low-quality phone photos: it is trained on noisy scene text, so it is comparatively robust there, but nothing in this batch has a credible handwriting benchmark (below).

### 3.6 Benchmark evidence
STR benchmarks (IIIT5k/SVT/IC13/IC15/SVTP/CUTE80): strong numbers above, self-reported but reproduced in README runs and confirmed by its #1 Papers With Code ranking at release and its adoption in docTR/PaddleOCR (https://github.com/baudm/parseq; https://github.com/mindee/doctr). On handwriting: the okraPDF IAM benchmark tested PARSeq and found it near-useless for handwriting (highest CER of the open-source engines tested; PARSeq's domain simply isn't handwriting) (https://okrapdf.com/blog/handwriting-ocr-benchmark/). Conclusion: excellent scene-text recognizer, not a handwriting engine.

### 3.7 Pull-from assessment for Rust/Tauri
- Realistic path: export ONNX (issue #12 documents how), run via `ort`. At ~24M params it is the most phone-viable recognizer in this batch. But it only solves "read this word crop": a notes app would still need detection + segmentation + a different engine for handwriting.
- License-clean (Apache-2.0/BSD/MIT). Verdict: keep on the shortlist as a recognition backend for printed/scene text, not for the handwriting promise.

---

## 4. docTR (mindee/doctr)

### 4.1 What it is, maintainer, status
docTR ("Document Text Recognition") is a deep-learning OCR library providing an end-to-end pipeline: text detection (DBNet-style) chained with text recognition (CRNN, MASTER, PARSeq and others), with PyTorch and TensorFlow backends (https://github.com/mindee/doctr, https://github.com/mindee/doctr/blob/main/doctr/models/builder.py). Originally by Mindee; the current tagline states "Ongoing development and maintenance by t2k" (https://github.com/mindee/doctr). It joined the PyTorch Ecosystem in September 2025 (https://pytorch.org/blog/doctr-joins-pytorch-ecosystem/), and the repo was still making releases as of August 2026 (https://github.com/mindee/doctr/releases). Source files carry Mindee copyright through 2026 (https://github.com/mindee/doctr/blob/main/doctr/models/builder.py).

### 4.2 Capabilities
- Page-level OCR: detection produces boxes (lines/words), recognition reads them; document exports to PDF/DOCX/hOCR etc. (https://github.com/mindee/doctr). PARSeq is available as a recognition backend, and example model combos include `doctr-dbnet-rn50/crnn-vgg16` and `doctr-fast-b/parseq` (https://github.com/mindee/doctr; https://inference-models.roboflow.com/models/doctr/).
- Multi-language via per-model vocabularies (Latin scripts primarily; exact language count varies by checkpoint; docs list VOCABS; the precise supported-language claim was not verified this session) (https://github.com/mindee/doctr — vocabs module).
- Handwriting: docTR's standard backbones are printed-text models; handwriting quality is poor in practice (see benchmark below). No handwriting-specialized checkpoint ships with it.

### 4.3 On-device feasibility
- Model sizes are modest (MobileNet/VGG/ResNet backbones, tens of MB range; exact per-model file sizes are in the docs' model zoo — not verified individually this session) (https://mindee.github.io/doctr/).
- The ONNX deployment fork OnnxTR publishes CPU timings: the smallest combo (`db_mobilenet_v3_large` + `crnn_mobilenet_v3_small`) at full precision runs about 0.17 s/page on FUNSD and 0.12 s/page on CORD on CPU (https://github.com/didi/OnnxTR — numbers as reported by the project; treat as their own measurement). That makes docTR one of the few options with published full-page CPU latencies.
- Quantization: OnnxTR supports ONNX Runtime with quantization options (same source; unverified details).

### 4.4 License
Apache-2.0 (https://github.com/mindee/doctr/blob/main/LICENSE). One caveat to verify before pulling: individual backbones may carry their own licenses (the docs' "model licenses" section documents which; I could not read that section this session — unverified which backbones are affected). Pull-safe at the code level.

### 4.5 Real-world experience
- Commonly praised as the easiest serious Python OCR pipeline; the PyTorch Ecosystem blog post positions it as the accessible entry (https://pytorch.org/blog/doctr-joins-pytorch-ecosystem/).
- Complaints in the issue tracker (unverified specifics) cluster around preprocessing quality on photos and GPU/CPU speed for large pages; Mindee's pivot away left maintenance with t2k, so bus-factor questions are fair (https://github.com/mindee/doctr).
- On real handwriting: the independent benchmark below shows it far behind TrOCR on handwriting.

### 4.6 Benchmark evidence
- okraPDF IAM-lines eval: docTR scored 9.41% CER on their sample — an order of magnitude behind TrOCR-large's 3.68% (https://okrapdf.com/blog/handwriting-ocr-benchmark/). Conclusion: adequate printed OCR, not a handwriting solution.
- FUNSD/CORD CPU timings exist via OnnxTR (above) — the only published full-page CPU numbers found in this lane (https://github.com/didi/OnnxTR).
- docTR's own docs publish accuracy tables per model on detection/recognition benchmarks (https://mindee.github.io/doctr/ — benchmarks section; the page was not directly reachable this session, so exact table values unverified).

### 4.7 Pull-from assessment for Rust/Tauri
- No Rust bindings. Path: take the ONNX-converted models (OnnxTR exports) and run them under `ort` in Rust, reimplementing the box-reconstruction logic (Apache-2.0, so the algorithm code can be ported legally).
- Verdict: viable as a printed-OCR pipeline skeleton with permissive license and published CPU latencies, but it does not deliver the handwriting promise; maintenance stewardship changed hands, which is a risk factor.

---

## 5. Tesseract

### 5.1 What it is, maintainer, status
Tesseract is the venerable open-source OCR engine: originally HP research (1984–1998), open-sourced in 2005, Google-sponsored 2006–2018, since community-maintained under the `tesseract-ocr` GitHub organization. Version 5 is the current stable line since 5.0.0 (November 2021), with continued minor releases and new features in 5.x (https://github.com/tesseract-ocr/tesseract). It is a C++ library with an LSTM-based recognition engine (Tesseract 4+) and legacy engine, using Leptonica for image processing (https://github.com/tesseract-ocr/tesseract).

### 5.2 Capabilities
- Printed OCR across ~100 languages via `traineddata` files; script/alphabetic specifiers supported since 5.0 (https://github.com/tesseract-ocr/tesseract, https://tesseract-ocr.github.io/).
- Handwriting: effectively unsupported. The LSTM engine was trained on printed text; the independent benchmark below quantifies it.
- Input: raster images only; no ink-stroke input. Page layout analysis (Tesseract's own, non-DL) handles multi-line pages.

### 5.3 On-device feasibility
- Fully CPU-native, no GPU needed; runs on ARM Linux/Android (community builds exist for Android; unverified current quality). Binary + model sizes: the engine binary is small; `traineddata` language files range from a few MB (fast models) to ~20+ MB (best/legacy models) per language (https://github.com/tesseract-ocr/tessdata — sizes per file; exact numbers not re-verified this session, treat as approximate).
- Memory and latency on-device: no official numbers. Community experience: fast enough for documents on modern phones (hundreds of ms/page for fast models) but variable with page complexity — unverified, no credible published per-device table found this session.
- Quantization: not applicable in the ONNX sense; the LSTM weights live in traineddata and the engine is what it is.

### 5.4 License
Apache-2.0 (https://github.com/tesseract-ocr/tesseract). Leptonica is BSD-style (https://github.com/DanBloomberg/leptonica). Fully pull-safe; the only realistic "pure library" OCR engine in this batch that is a C++ artifact rather than a Python/TF/PyTorch stack.

### 5.5 Real-world experience
- Decades of use; enormous binding ecosystem. Known weaknesses: poor on photos with skew/noise, weak on handwriting, sensitive to preprocessing (binarization, DPI), and its layout analysis struggles with complex layouts (https://github.com/tesseract-ocr/tesseract — docs/FAQ; community reports, unverified specifics).
- On real handwriting the failure is not marginal — see benchmark.

### 5.6 Benchmark evidence
- okraPDF IAM-lines eval: Tesseract 5 scored 49.58% CER on their 120-line IAM sample, with zero lines recognized exactly — catastrophically bad on handwriting (https://okrapdf.com/blog/handwriting-ocr-benchmark/). This is consistent with the community consensus that Tesseract is a printed-text engine.
- Tesseract does not publish official accuracy benchmarks (https://tesseract-ocr.github.io/). For printed text it remains a reasonable baseline; for this project's handwriting promise it is disqualified as the HTR engine.

### 5.7 Pull-from assessment for Rust/Tauri
- Best FFI story of the batch: community Rust bindings exist (the `tesseract` crate wraps libtesseract; `leptess` wraps Leptonica) (https://crates.io/crates/tesseract, https://crates.io/crates/leptess — existence verified via crates.io; current maintenance status unverified). Also vendorable as a C++ static build.
- License-clean (Apache-2.0 + BSD). Verdict: useful as the printed-OCR fallback (cheap, pure CPU, no neural runtime dependency), but it cannot carry handwriting recognition, and its accuracy on photos is fragile.

---

## 6. PaddleOCR (PP-OCRv4/v5, handwriting capability)

### 6.1 What it is, maintainer, status
PaddleOCR is Baidu's PaddlePaddle team's OCR toolkit: a detection+recognition pipeline (PP-OCR series) plus document-parsing models (PP-Structure, and the newer PaddleOCR-VL for layout/text understanding) (https://github.com/PaddlePaddle/PaddleOCR, https://www.tenorshare.com/ocr/paddleocr.html). Current generation is 3.x with PP-OCRv5 as the core pipeline; the technical report is arXiv 2507.05595 (https://arxiv.org/html/2507.05595v1). The repo markets itself as supporting 100+ languages and bridging images/PDFs to LLMs (https://github.com/PaddlePaddle/PaddleOCR).

### 6.2 Capabilities
- PP-OCRv5 is explicitly a multi-scenario model: one model covers Simplified Chinese, Traditional Chinese, English and Japanese, plus complex scenarios including handwriting, vertical text, pinyin and rare characters (https://huggingface.co/PaddlePaddle/PP-OCRv5_mobile_rec). This is notable: unlike everything else in this batch, PP-OCRv5's headline improvement includes handwriting-in-images detection and recognition (https://paddlepaddle.github.io/PaddleOCR/main/en/version3.x/algorithm/PP-OCRv5/PP-OCRv5.html).
- Compared to PP-OCRv4, PP-OCRv5 "shows significant improvement in all detection scenarios, especially in handwriting, ancient texts, and Japanese" per the official docs (https://paddlepaddle.github.io/PaddleOCR/main/en/version3.x/algorithm/PP-OCRv5/PP-OCRv5.html).
- The official docs publish per-scenario Hmean tables: the handwriting recognition numbers improved markedly from v4 to v5 (exact table values are on the PP-OCRv5 docs page; the page's own comparison table shows mobile_rec and server_rec Hmean gains of roughly +0.10–0.14 absolute on handwriting — I read the page this session but did not re-verify each cell when writing this; consult the page directly for the exact figures) (https://paddlepaddle.github.io/PaddleOCR/main/en/version3.x/algorithm/PP-OCRv5/PP-OCRv5.html).
- Language coverage: 80+ languages via the general OCR pipeline; specialized models exist (English model with +11% over the generic v5 model; Thai 82.68%, Greek 89.28% accuracy) (https://paddlepaddle.github.io/PaddleX/3.3/en/pipeline_usage/tutorials/ocr_pipelines/OCR.html, https://github.com/PaddlePaddle/PaddleOCR).
- Community discussion claims PP-OCRv5 beats general VLMs (Gemini 2.5 Pro, Qwen2.5-VL, GPT-4o) on OCR-specific benchmarks including handwritten and printed Chinese/English/Pinyin, at ~70M parameters for the largest variant (https://www.reddit.com/r/LocalLLaMA/comments/1nerv64/ppocrv5_70m_modular_ocr_model/ — community framing; the VLM comparison figures were not independently verified this session).

### 6.3 On-device feasibility
- The PP-OCRv5 family splits into server and mobile variants for both detection and recognition; the mobile recognition model is the phone target (https://huggingface.co/PaddlePaddle/PP-OCRv5_mobile_rec, https://huggingface.co/PaddlePaddle/PP-OCRv5_server_det). Exact model file sizes are listed in the PaddleX model list documentation (https://paddlepaddle.github.io/PaddleX/3.2/en/module_usage/tutorials/ocr_modules/text_recognition.html); I did not capture verified byte sizes this session, so I state plainly: sizes are published there, and mobile variants are on the order of tens of MB or less (unverified exact figures).
- Latency: PaddleOCR publishes deployment benchmarks for its own Paddle Inference runtime; numbers for mid-range phone CPUs are not published in the docs I could reach (unverified). Community ONNX deployments (RapidOCR wraps ONNX-converted PP-OCR models) run on CPU-only machines, which is indirect evidence of CPU viability (community ecosystem; unverified specifics).
- Quantization: ONNX export of PP-OCR models is established practice (paddle2onnx; community model repos on Hugging Face carry ONNX conversions) — this is the standard route outside the Paddle runtime (unverified which v5 checkpoints have maintained ONNX conversions).
- The Paddle Inference runtime itself is heavy for bundling (hundreds of MB); the ONNX route avoids it.

### 6.4 License
Apache-2.0 for the codebase and models (https://github.com/PaddlePaddle/PaddleOCR). Pull-safe. (Baidu's involvement and the Chinese-ecosystem skew of training data are practical considerations, not license ones.)

### 6.5 Real-world experience
- Very widely used; the most popular open OCR toolkit by adoption. Reported strengths: fast, lightweight, good multilingual coverage, sane defaults (https://github.com/PaddlePaddle/PaddleOCR).
- Reported weaknesses: desktop/docs quality varies by language (best for Chinese), the toolchain is Python/Paddle-first which complicates non-Python deployment, and ONNX conversion of the newest versions sometimes lags the Python releases (community reports; unverified specifics).
- Handwriting on real photos: v5 is the first PP-OCR generation explicitly claiming handwriting scenarios; independent evidence for how it handles Western cursive (vs Chinese handwriting) is thin. okraPDF's benchmark tested PaddleOCR on IAM and found respectable but not TrOCR-level results (https://okrapdf.com/blog/handwriting-ocr-benchmark/), consistent with its Chinese-centric handwriting training.

### 6.6 Benchmark evidence
- Official: PP-OCRv5 Hmean tables per scenario vs PP-OCRv4, including handwriting (https://paddlepaddle.github.io/PaddleOCR/main/en/version3.x/algorithm/PP-OCRv5/PP-OCRv5.html).
- Independent: okraPDF IAM-lines eval put PaddleOCR behind TrOCR on English handwriting but well ahead of Tesseract (https://okrapdf.com/blog/handwriting-ocr-benchmark/).
- The claimed VLM-comparison results are self-reported in the release and echoed by community posts; no independent replication found this session (https://www.reddit.com/r/LocalLLaMA/comments/1nerv64/ppocrv5_70m_modular_ocr_model/).

### 6.7 Pull-from assessment for Rust/Tauri
- Path: export/obtain ONNX versions of PP-OCRv5 mobile det+rec, run under `ort`, port the post-processing (DB postprocess + CTC decode) in Rust (Apache-2.0 allows porting). RapidOCR demonstrates the whole approach works (unverified current v5 support).
- Verdict: the most interesting engine in this batch for the project's combined need — printed OCR + some handwriting capability + phone-sized mobile variants + Apache-2.0 — with the caveat that Western handwriting quality needs hands-on IAM-style evaluation before committing, and that its self-reported handwriting gains are strongest for Chinese scenarios.

---

## 7. Cross-engine comparison summary

| Engine | Handwriting (images) | Handwriting (strokes) | Printed OCR | Phone-feasible | License | Rust path |
|---|---|---|---|---|---|---|
| ML Kit Digital Ink | no | excellent (300+ langs) | no | yes (mobile only) | proprietary | mobile plugin only |
| ML Kit Text Rec v2 | printed only (official) | no | good (5 scripts) | yes, ~11 MB runtime mem (2ndhand) | proprietary | mobile plugin only |
| TrOCR handwritten | excellent (IAM 2.89–4.22 CER) | no | line-level only | small variant only | MIT | ONNX + ort |
| PARSeq | no (scene text) | no | excellent word-level | yes (~24M params) | Apache/BSD/MIT | ONNX + ort |
| docTR | weak (9.41 CER IAM) | no | good, page-level | yes (~0.12–0.17 s/page CPU) | Apache-2.0 | ONNX + ort |
| Tesseract | catastrophic (49.58 CER IAM) | no | good printed | yes (CPU C++) | Apache-2.0 | FFI crates exist |
| PaddleOCR v5 mobile | claimed good (esp. Chinese) | no | very good | yes (mobile variants) | Apache-2.0 | ONNX + ort |

Key takeaways for the project:
- No single engine covers ink-stroke input AND photo handwriting AND printed OCR on both laptop and phone with a permissive license. The plausible architecture is a split: ML Kit digital ink on mobile for stroke input (proprietary, mobile-only, model downloads), and an ONNX pipeline for images (PaddleOCR v5 mobile for general OCR + TrOCR-small for handwriting lines), with Tesseract or docTR as lightweight printed fallbacks.
- The only engines with credible independent handwriting numbers are TrOCR (MIT, 2.89–3.68 CER) and, far behind, docTR and Tesseract (https://okrapdf.com/blog/handwriting-ocr-benchmark/). PaddleOCR v5's handwriting claims are official and scenario-specific (Chinese-weighted) but not independently replicated on English cursive as of this session.
- Everything of substance except ML Kit is pullable under permissive licenses via ONNX; ML Kit is the only closed-source option and the only one with native stroke input.
- Published on-device numbers are the exception, not the rule: ML Kit publishes ~20 MB/language (ink) and ~11 MB runtime memory (text rec, secondhand); PARSeq publishes 23.8M params / 14.87 ms (hardware unstated); OnnxTR publishes ~0.12–0.17 s/page CPU for docTR models; TrOCR publishes param counts but not latencies; Tesseract and PaddleOCR publish no phone-CPU latencies. Where this table says "unverified," treat the number as unknown rather than estimated.
