# ML recognition links: handwriting, OCR, image ML

Compiled 2026-11-06 as a link reference. Sources: this project's verified findings (r12-alt-4.md, r12-alt-6.md, myscript-nebo-reverse.md, linked-apps-1.md, community-digest.md) plus a fresh web sweep of the 2026 OCR-model landscape (roundup sources listed at the end). Research only, no build plan. Licenses are as verified in findings; anything not verified there is marked UNVERIFIED.

## 1. Digital ink: handwriting from strokes (the MyScript/Nebo lane)

| Name | License / cost | Link | What it covers |
|---|---|---|---|
| Google ML Kit Digital Ink Recognition | Free, closed SDK, on-device | https://developers.google.com/ml-kit/vision/digital-ink-recognition | 300+ languages via downloadable classifiers, Android + iOS. The practical default and the easiest Nebo substitute |
| Apple PencilKit + Scribble | Free, Apple platforms only | https://developer.apple.com/documentation/pencilkit | On-device stroke, shape and gesture intelligence; handwriting surfaced via VisionKit / Live Text |
| MyScriptJS / iinkJS | Apache-2.0 (client only, no recognition) | https://github.com/MyScript/MyScriptJS | Ink capture, pressure handling, gestures, JIIX rendering. Recognition runs in MyScript Cloud and needs developer keys |
| MyScript Interactive Ink SDK examples | Free starter certificate; commercial pricing unpublished | https://github.com/MyScript/interactive-ink-examples-ios | Official SDK examples. MyScript's real edge is interactive ink (typeset and reflow as you write) plus math and diagrams, all closed |
| langergitanu/MyScript | Documentation project, no usable code | https://github.com/langergitanu/MyScript | Reverse-engineering notes on the Nebo APK and MyScript file format. Architecture patterns only; do not copy decompiled code |
| xournalpp_htr | See repo | https://github.com/PellelNitram/xournalpp_htr | Open handwriting-to-text for Xournal++; the parity-of-spirit open engine |

**Documented gap:** no open project covers general online stroke-to-text handwriting recognition as an embeddable SDK. Offline line-image HTR, gesture recognizers, and handwritten math all exist open; MyScript's interactive-ink engine does not. (findings: r12-alt-6.md, myscript-nebo-reverse.md)

## 2. Handwritten page-image HTR (offline, multilingual)

| Name | License | Link | Notes |
|---|---|---|---|
| Kraken | Apache-2.0 | https://github.com/mittagessen/kraken | Turn-key OCR/HTR for historical and non-Latin scripts including Arabic; DOI-pinned model zoo; active |
| Calamari | GPL-3 (since 2.0) | https://github.com/Calamari-OCR/calamari | Line-based ATR engine, OCRopy lineage; default engine of OCR4all; TensorFlow 2; research-paced |
| PyLaia | Models MIT; repo LICENSE UNVERIFIED | https://github.com/jpuigcerver/PyLaia | PyTorch HTR toolkit by Teklia; pretrained models on Hugging Face; language-model-boosted accuracy |
| eScriptorium | UNVERIFIED | https://gitlab.com/scripta/escriptorium | Self-hosted web platform to annotate, transcribe, and train kraken models; institutional production use |
| TrOCR (Microsoft) | MIT | https://huggingface.co/microsoft/trocr-base-handwritten | Lightest offline option for modern handwriting; runs on-device (the InkedMark Obsidian plugin does exactly this, findings: community-digest.md) |

## 3. Printed-text OCR, multilingual, on-device

| Name | License | Link | Notes |
|---|---|---|---|
| PaddleOCR | Apache-2.0 | https://github.com/PaddlePaddle/PaddleOCR | Current benchmark leader: PP-OCRv6 recognition, PP-StructureV3 layout parsing, 0.9B PaddleOCR-VL document model, 100+ languages |
| RapidOCR | Apache-2.0 (bundled model weights retain Baidu/PaddleOCR rights, per repo notice) | https://github.com/RapidAI/RapidOCR | PaddleOCR models packaged as ONNX for mobile and edge; Python/C++/Java/C#; active, v3.9.x 2026 |
| EasyOCR | Apache-2.0 | https://github.com/JaidedAI/EasyOCR | 80+ languages and scripts; lowest setup friction; slow-moving, EasyOCR2 fork announced Dec 2025 |
| docTR | UNVERIFIED this pass | https://github.com/mindee/doctr | PyTorch pipeline; the pick when you want to tune the accuracy-latency trade-off yourself |
| Tesseract 5.5.3 | Apache-2.0 | https://github.com/tesseract-ocr/tesseract | CPU-only baseline for printed text; 5.5.3 released 24 Jul 2026 |
| Surya | UNVERIFIED this pass | https://github.com/datalab-to/surya | 90+ languages; the quality/speed balance pick |
| Pix2Text | MIT | https://github.com/breezedeus/Pix2Text | Open Mathpix alternative: layout, tables, formulas and text to Markdown; 80+ languages; local Mac app |

**Benchmark snapshot (2026 roundups, sources below):** PaddleOCR leads classic engines on handwriting at about 73% accuracy versus Tesseract 45% and EasyOCR 62%, and the VLM-based tools (Surya, olmOCR, Qwen2.5-VL) beat classic engines on handwriting in practice. Comparisons point to PaddleOCR for multilingual and CPU work, DeepSeek-OCR or olmOCR where a GPU is available, and Surya as the quality/speed middle ground.

## 4. Document-VLM models (GPU, whole pages to structured Markdown)

| Name | Link | Notes |
|---|---|---|
| PaddleOCR-VL-1.6 | https://github.com/PaddlePaddle/PaddleOCR | Top of OmniDocBench v1.6 at 96.34 |
| MinerU2.5-Pro | https://github.com/opendatalab/MinerU | Second at 95.75 |
| GLM-OCR | Repo link UNVERIFIED this pass | Third at 95.22; 0.9 to 1.2B-parameter models beat Qwen3-VL-235B (89.78) at a fraction of the compute |
| olmOCR | https://github.com/allenai/olmocr | AllenAI; its benchmark (olmOCR-Bench) is the community standard |
| DeepSeek-OCR | Repo link UNVERIFIED this pass | The GPU pick named in the 2026 roundups for scans with tables, formulas or handwriting |
| LightOnOCR-3 | Repo link UNVERIFIED this pass | Released Oct 2026, Apache-2.0, three sizes (0.8/1/4B); reported 86.3 on olmOCR-Bench for the 4B model |

## 5. On-device image ML for private search (the ente lane)

Ente ML is the reference design for private content search: https://ente.io/blog/machine-learning/

- CLIP embeddings plus face models run locally via ONNX Runtime Mobile, over E2EE-encrypted photos.
- The index itself is encrypted and synced like data, so every device benefits; search works offline after indexing.
- First indexing pass is slow on phones; desktop is recommended for the first pass. No ML on the web client.
- Design lessons filed from it: run embeddings/OCR on-device, encrypt the index, sync it like data, and plan for a slow first pass with a fast client. (findings: linked-apps-1.md, community-digest.md)

## 6. Adjacent recognizers

| Name | License | Link | Notes |
|---|---|---|---|
| Seshat | GPLv3 | https://github.com/falvaro/seshat | Handwritten math strokes to LaTeX/MathML/InkML; C++; frozen research code, single author |
| LaTeX-OCR (pix2tex) | MIT | https://github.com/lukas-blecher/LaTeX-OCR | Handwritten math image to LaTeX (ViT); ~16k stars; dormant; accuracy gripes on hard snippets |
| $P recognizer | New BSD | https://depts.washington.edu/acelab/proj/dollar/pdollar.html | Point-cloud gesture and shape recognizer, roughly 70-line core; JS/C# references, Python/Unity/ObjC ports |
| WritePad engine | Engine GPL-3 | https://github.com/phatware/WritePad-Handwriting-Recognition-Engine | Self-contained multilingual cursive/print/mixed HWR engine; iOS/Android/Windows/Linux/macOS; open-sourced 2016, legacy |
| OpenScan | UNVERIFIED | https://github.com/ethereal-developers/OpenScan | Privacy-first Android document scanner to PDF; the VisionKit document-scan analog; offline, no network |

## 7. Quick picks

| Need | Use |
|---|---|
| Online handwriting-to-text on Android/iOS | ML Kit Digital Ink Recognition |
| Offline handwriting from page scans, many scripts | Kraken (train via eScriptorium) |
| Offline handwriting, modern text, lightest | TrOCR |
| Printed OCR, multilingual, CPU | PaddleOCR, or RapidOCR/Tesseract for deployment simplicity |
| Printed OCR, best quality, GPU | PaddleOCR-VL, or olmOCR/MinerU |
| Handwritten math | Seshat (strokes) or LaTeX-OCR (image) |
| Private photo/note search | Ente ML pattern: CLIP on-device plus encrypted index |
| Gesture and shape recognition | $P recognizer |

## 8. What stays closed

- MyScript's interactive-ink engine (typeset and reflow while writing, math, diagrams): native binaries, no open reimplementation exists. Pull only the Apache-2.0 client pieces and mimic the documented protocol shape. (myscript-nebo-reverse.md)
- General online stroke HWR as an embeddable SDK: closed everywhere. (r12-alt-6.md)
- RapidOCR's bundled model weights remain Baidu/PaddleOCR property; only its source is Apache-2.0. (r12-alt-6.md)
- Nebo's `.bink` ink format has no published parser (tracked at https://github.com/xournalpp/xournalpp/issues/5730). (myscript-nebo-reverse.md)

## Web sweep sources (2026-11-06)

- https://imagetotable.ai/blog/best-open-source-ocr-tools-2026 (Sep 2026; handwriting accuracy figures)
- https://roboflow.com/blog/best-open-source-ocr-models (Oct 2026; OmniDocBench v1.6 ranking)
- https://www.koncile.ai/en/ressources/10-open-source-ocr-tools-you-should-know-about (Nov 2026; LightOnOCR-3)
- https://www.llamaindex.ai/insights/7-best-open-source-ocr-tools (Aug 2026; CPU vs GPU picks)
- https://vdf.ai/blog/best-local-ocr-models/ (Oct 2026; Tesseract 5.5.3 release)
- https://www.aimadetools.com/blog/best-open-source-ocr-models-2026/ (Aug 2026; language-count comparisons)
