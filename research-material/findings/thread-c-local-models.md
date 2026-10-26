# Thread C: Small local models survey

Research lane: Thread C. Scope: one small local model family for (1) summarize/rewrite/draft, (2) RAG Q&A over the user's notes, (3) on-device STT, (4) on-device TTS. Surveyed October 2026.

Method note: claims are tagged by provenance. `[primary]` = the vendor's own model card, repository, docs, or license text, at the URL given. `[3rd-party]` = a measurement or report by someone else; treat as indicative, not authoritative. `[UNVERIFIED]` = not confirmed from any fetched source in this run; no number below is invented, anything without a source is marked this way. "Nobody has published this" is recorded as a finding where it applies. Runtime assumed: llama.cpp/GGUF on CPU and whatever GPU backends phones/laptops expose (Metal, Vulkan/OpenCL Adreno); the app is open-source-bound, so license terms are first-class.

---

## 1. Language model (summarizing / rewriting / drafting, and RAG generation over notes)

### Candidates

**Qwen3-4B-Instruct-2507** (Qwen, Alibaba)
- Parameters: 4B (safetensors, BF16) [primary: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507]
- License: Apache 2.0 [primary: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/LICENSE]
- Quantized size on disk: Q4_K_M GGUF = 2.5 GB; Q4_K_S = 2.38 GB; Q3_K_S = 1.89 GB [primary repo file listing: https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF/tree/main]
- Context: 256K tokens, non-thinking instruct variant [primary model description, mirrored at https://huggingface.co/NexaAI/Qwen3-4B-Instruct-2507-npu]
- Real memory use: [UNVERIFIED] not published by the vendor; rule of thumb for GGUF is roughly model-file size plus KV cache, but we did not find a vendor figure.
- Speed: on a desktop CPU, a community benchmark reports ~13 tok/s for the Q8_K_XL GGUF variant [3rd-party: https://www.reddit.com/r/LocalLLaMA/comments/1p90zzi/cpuonly_llm_performance_ts_with_llamacpp/]. On-phone figures for this exact model: nobody has published reproducible numbers we could find; see Speed discussion below.
- Vendor trust: weights from Alibaba (Qwen team). Apache 2.0 is clean for redistribution. No remote-restriction or use-policy clause in the license. Consideration for the project: training-data provenance and the vendor's jurisdiction are a values question, not a legal one; the license imposes nothing.

**Gemma 3n E4B-it** (Google)
- Parameters: raw 8B, effective 4B; Per-Layer Embeddings let it run with a memory footprint "comparable to a traditional 4B model" by offloading low-utilization matrices [primary: https://huggingface.co/google/gemma-3n-E4B-it]
- Architecture: MatFormer nested sub-models (E2B is a nested sub-model of E4B), PLE offload to CPU, 32K context, multimodal text/image/video/audio input [primary: same model card; https://huggingface.co/docs/transformers/en/model_doc/gemma3n]
- Quantized size on disk: [UNVERIFIED] the launch HF repo ships BF16 for transformers; LiteRT/MediaPipe-format quantized builds exist (see litert-community repos, e.g. Gemma3-1B-IT for the 1B sibling at https://huggingface.co/litert-community/Gemma3-1B-IT) but we did not confirm an E4B file size in this run.
- Real memory use: E2B ~2 GB RAM and E4B ~3 GB per a third-party primer [3rd-party: https://aman.ai/primers/ai/gemma-3n/]; Google's own blog claims ~1.5x faster first response on mobile vs Gemma 3 4B and a reduced memory footprint via PLE, KV sharing and activation quantization [primary: https://developers.googleblog.com/en/introducing-gemma-3n/]
- Speed on phones: no verified on-device tokens/sec figure for Gemma 3n has been published [3rd-party observation: https://www.promptquorum.com/power-local-llm/mobile-llm-models-phi4-gemma-smollm]. This is a genuine gap in the literature.
- License: custom Gemma Terms of Use, not an OSI license. Redistribution requires passing Google's use restrictions downstream as an enforceable provision; use is bound to the Gemma Prohibited Use Policy; reporting indicates Google reserves the right to restrict usage remotely for violations [primary: https://ai.google.dev/gemma/terms ; 3rd-party: https://techcrunch.com/2025/03/14/open-ai-model-licenses-often-carry-concerning-restrictions/]. Third-party posts in 2026 claim later Gemma generations moved to Apache 2.0 [3rd-party, UNVERIFIED against a primary Google page: https://www.mindstudio.ai/blog/gemma-4-apache-2-license-commercial-use] — verify before relying on it.
- Trust concern: the license itself. For an open-source-bound, zero-knowledge app, a custom license with a use-policy incorporated by reference and a remote-restriction clause is materially worse than Apache/MIT, independent of model quality.

**Phi-4-mini-instruct** (Microsoft)
- Parameters: 3.8B, dense decoder-only [primary: https://huggingface.co/microsoft/Phi-4-mini-instruct]
- License: MIT [primary: license metadata and README, https://huggingface.co/microsoft/Phi-4-mini-instruct/blob/main/README.md]
- Quantized size on disk: [UNVERIFIED] GGUF conversions exist (bartowski, unsloth) but no file size was confirmed in this run.
- Speed: [UNVERIFIED] no on-device figure found.
- Trust: Microsoft corporate provenance, but MIT terms are the cleanest class.

**SmolLM3-3B** (Hugging Face)
- Parameters: 3B; repo is 6.17 GB (BF16) [primary file listing: https://huggingface.co/HuggingFaceTB/SmolLM3-3B/tree/main]
- License: Apache 2.0 [primary: https://huggingface.co/HuggingFaceTB/SmolLM3-3B]
- Quantized size on disk: Q4_K_M GGUF exists from the standard converters [primary repo: https://huggingface.co/bartowski/HuggingFaceTB_SmolLM3-3B-GGUF]; exact byte size [UNVERIFIED in this run]. The full-precision repo is ~6.17 GB, so a Q4 file plausibly lands near 2 GB, but that is inference, not a sourced number.
- Speed: community CPU benchmark reports ~27 tok/s at Q4_K_XL and ~16 tok/s at Q8_K_XL on a desktop CPU [3rd-party: https://www.reddit.com/r/LocalLLaMA/comments/1p90zzi/cpuonly_llm_performance_ts_with_llamacpp/]
- Also notable: the team publishes fully open training data and intermediate checkpoints, an unusually strong trust posture [primary: https://huggingface.co/HuggingFaceTB/SmolLM3-3B-Base]

### Runtime reality (shared by all GGUF candidates)

- llama.cpp is the de facto runtime; the whole model lives in one GGUF file [primary: https://github.com/ggml-org/llama.cpp]
- A community measurement on a Pixel 9 Pro reports ~12 tok/s for Llama-3.2-3B-Instruct Q4_K_M on CPU via llama.cpp [3rd-party: https://www.reddit.com/r/LocalLLaMA/comments/1glx6a5/phone_llms_benchmarks/]. This is the best phone-CPU anchor we found: expect roughly 10-15 tok/s for a 3-4B Q4 model on a recent flagship CPU, and clearly not-interactive speeds on mid-range phones.
- A peer-reviewed-style benchmark study of llama.cpp (CPU) vs MLC LLM (GPU) on commodity mobile devices exists and is the right primary literature to consult for methodology [primary paper: https://arxiv.org/html/2410.03613v3]
- Reproducible Snapdragon phone/laptop numbers across CPU/OpenCL/Vulkan/NPU backends are, per one benchmarking project's own words, not answerable today: "nobody can answer that reproducibly" [3rd-party but self-aware about the gap: https://github.com/everyai-com/snapbench]. Treat any specific phone tok/s claim with caution.
- Google's sanctioned on-device path: MediaPipe LLM Inference API runs LLMs fully on-device from .task files; on Android it is positioned for experimental use, with production Android LLMs going through Gemini Nano via Android AICore; MediaPipe now recommends migrating to LiteRT-LM [primary: https://developers.googleblog.com/large-language-models-on-device-with-mediapipe-and-tensorflow-lite/ ; https://ai.google.dev/edge/mediapipe/solutions/genai/llm_inference/android]. AICore/Gemini Nano is a system-managed, closed model: it does not fit a zero-knowledge, ship-the-weights app.

### RAG fit

No candidate publishes RAG-specific numbers; RAG quality over a user's notes is a function of (a) the retriever (embedding model + chunking, not surveyed here) and (b) the generator's context handling. The differentiators found: Qwen3-4B-Instruct-2507's 256K context [primary: https://huggingface.co/NexaAI/Qwen3-4B-Instruct-2507-npu] allows dumping many retrieved chunks without aggressive re-ranking; SmolLM3 and Phi-4-mini have long-context variants (SmolLM3 128K is reported by third parties [3rd-party: https://tinyweights.dev/posts/smollm3-3b-the-fully-ope/], UNVERIFIED against the primary card). Grounding faithfulness of these specific models on private-note RAG: nobody has published this. It is a test-we-must-run finding, not a research-able one.

---

## 2. On-device speech-to-text

### Candidates

**Whisper family via whisper.cpp** (OpenAI weights, MIT)
- Sizes and disk: tiny 39M params / 75 MB, base 74M / 142 MB, small 244M / 466 MB; Q5_1 quantized: tiny 31 MB, base 57 MB, small 182 MB [primary (ggml's own WASM demo page): https://ggml.ai/whisper.cpp/ ; model docs: https://github.com/ggml-org/whisper.cpp/blob/master/models/README.md]
- Params cross-check: tiny 38-39M, base 74M, small 244M [primary: https://huggingface.co/openai/whisper-tiny ; https://huggingface.co/openai/whisper-small]
- License: MIT [primary: https://huggingface.co/openai/whisper-small and OpenAI repo https://github.com/openai/whisper]
- Real memory use: small GGML reported ~852 MB runtime RAM [3rd-party: https://openwhispr.com/blog/whisper-model-sizes-explained]
- Speed: whisper.cpp is a C/C++ CPU/edge port with mobile examples [primary: https://github.com/ggml-org/whisper.cpp]. Batch transcription on phones is fast; the pain point is streaming: a developer discussion documents naive live transcription at ~5x slower than real time on Android until the 30-second window is reworked [primary issue: https://github.com/ggml-org/whisper.cpp/discussions/3567]. Whisper's fixed 30-second window is architecturally hostile to streaming [3rd-party writeup of the same: https://www.reddit.com/r/androiddev/comments/1po663c/whispercpp_on_android_streaming_live/]
- Quality: Whisper small.en ~3.43% WER on LibriSpeech test-clean [3rd-party citing the published eval: https://www.aimodels.fyi/models/huggingFace/whisper-small-openai]; WER degrades sharply at tiny for non-English audio, as users report with the ~75 MB tiny model [primary issue: https://github.com/ggml-org/whisper.cpp/issues/1103]. An Apple Neural Engine encoder path (ANEForge) claims ~2x faster encoder from tiny to medium [primary README: https://github.com/ggml-org/whisper.cpp]

**Moonshine** (Moonshine AI, formerly Useful Sensors)
- Sizes: tiny 27M, base 61M params; sequence-to-sequence ASR, English in the first generation; trained on 200,000 hours [primary model card: https://huggingface.co/UsefulSensors/moonshine]
- Current repo: moonshine-ai/moonshine, now covering "speech to text, intent recognition, and text to speech," everything on-device, streaming-first, with models "from higher accuracy than Whisper Large V3 down to tiny 1MB models" [primary: https://github.com/moonshine-ai/moonshine]
- License: MIT for the code and for the English-language models; the exceptions are legacy non-streaming non-English models under the non-commercial Moonshine Community License [primary: https://github.com/moonshine-ai/moonshine/blob/main/LICENSE ; https://github.com/moonshine-ai/moonshine]
- Vendor claim on quality: "greater accuracy on standard datasets over existing ASR systems of similar sizes" [primary: https://huggingface.co/UsefulSensors/moonshine]; a third-party writeup calls it a slight WER edge over Whisper plus large speed increases [3rd-party: https://www.hackster.io/news/asr-gets-a-shot-of-moonshine-2b80a6a514e0]
- Trust: MIT, small vendor, transparent model card including explicit dual-use/surveillance caveats [primary: https://huggingface.co/UsefulSensors/moonshine]. The newer v2 generation and non-English sizes need a license check per-model before bundling [primary README: https://github.com/moonshine-ai/moonshine]

**Platform STT: Apple SpeechAnalyzer (iOS 26 / macOS Tahoe 26)**
- A new on-device transcription model exposed via SpeechAnalyzer/SpeechTranscriber; Apple states the model "operates entirely on-device, ensuring privacy and efficiency" [primary: https://developer.apple.com/videos/play/wwdc2025/277/ ; docs: https://developer.apple.com/documentation/speech/speechanalyzer]
- Third-party benchmarking places its accuracy between Whisper base and small on long-form conversational speech [3rd-party: https://www.argmaxinc.com/blog/apple-and-argmax]; a 2026 third-party test reports 2.12% WER on LibriSpeech clean vs Whisper Small's 3.74% [3rd-party: https://gigazine.net/gsc_news/en/20260714-apple-speech-analyzer-benchmark/]
- The model is a system asset, not in your bundle [3rd-party: https://www.forasoft.com/blog/article/speech-recognition-with-neural-networks-on-ios-1621]. That is the crux: it is on-device, but it is closed and not shippable inside a zero-knowledge app; it is also Apple-only, so it cannot be the cross-platform answer.

### The transcription tension, resolved

Can a zero-knowledge app ship Whisper-class STT fully on-device on a phone today?

- Yes at tiny/base: whisper.cpp tiny (75 MB, 31 MB at Q5_1) and base (142 MB, 57 MB at Q5_1) run on phones; these are MIT and bundle-able. But "Whisper-class" at tiny/base means clearly lower accuracy than the Whisper people compare against (small and up), and worse again off-English [primary issue evidence: https://github.com/ggml-org/whisper.cpp/issues/1103]
- Not comfortably at small: 466 MB on disk (182 MB quantized) and ~850 MB RAM [3rd-party: https://openwhispr.com/blog/whisper-model-sizes-explained] plus batch-only ergonomics make small a "download on first use" model for long-form dictation, not a shippable default.
- The honest fallback, in order: (1) bundle Moonshine tiny/base (27M/61M, MIT, streaming-native, designed exactly for this) as the default English STT; (2) ship whisper.cpp tiny/base Q5_1 where multilingual coverage is needed and accept the accuracy hit; (3) offer the platform STT (Apple SpeechAnalyzer / whatever Android ships) as an opt-in "faster and no download" path with a plain-language note that it uses OS-provided, closed models; (4) offer whisper small (or Moonshine's larger v2 sizes) as an optional download for users who want maximum accuracy offline. Full Whisper-small-class quality inside the base install on a phone is not available today; saying so in the product is the honest position.

---

## 3. On-device text-to-speech

**Kokoro-82M** (hexgrad)
- Parameters: 82M, open-weight; "delivers comparable quality to larger models while being significantly faster" [primary: https://huggingface.co/hexgrad/Kokoro-82M]
- License: Apache 2.0 [primary: https://huggingface.co/hexgrad/Kokoro-82M/tree/main]
- Size on disk: repo total 363 MB [primary file listing: https://huggingface.co/hexgrad/Kokoro-82M/tree/main]; model-only and ONNX sizes [UNVERIFIED in this run]; community ONNX ports exist, including multilingual community builds [primary: https://huggingface.co/onnx-community/Kokoro-82M-v1.1-zh-ONNX]
- On-phone runtime: no published tok/s on phones found in this run [UNVERIFIED]. The inference library is pip-installable and CPU-friendly [primary: https://github.com/hexgrad/kokoro]
- Trust: solo/small-team author, Apache weights, pretrained lineage disclosed (StyleTTS2-LJSpeech base) [primary: https://huggingface.co/hexgrad/Kokoro-82M]

**Piper** (rhasspy / Open Home Foundation)
- "A fast, local neural text to speech system," optimized for Raspberry Pi-class hardware [primary: https://github.com/rhasspy/piper]
- License split, important: the original rhasspy/piper is MIT and was archived (made read-only) in October 2025; active development moved to OHF-Voice/piper1-gpl, which is GPL-licensed, and most voices phonemize via espeak-ng under GPL [primary repo pointers: https://github.com/rhasspy/piper ; license discussion: https://github.com/rhasspy/piper/discussions/271 ; 3rd-party summary of the move: https://www.cekura.ai/discover/piper-tts]
- For an open-source-bound app this is workable (GPL is open source) but it changes the obligation: ship Piper-derived code as GPL-compatible, or use the archived MIT release at the cost of future maintenance.

Voice quality tradeoff: Kokoro is the quality pick and permissively licensed; Piper is the low-resource pick with proven Raspberry-Pi-class speed, but engine maintenance moved under GPL. A per-model voice download store (either engine) keeps the base app small.

---

## 4. Comparison table

### Language model (GGUF, Q4-class unless noted)

| Model | Params | Disk (quant) | RAM | CPU tok/s | Phone GPU tok/s | License | Trust notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Qwen3-4B-Instruct-2507 | 4B | 2.5 GB (Q4_K_M) [src] | UNVERIFIED | ~13 (Q8, desktop CPU) [3rd-party] | nobody has published reproducible numbers [src] | Apache 2.0 | Alibaba origin; clean license |
| Gemma 3n E4B-it | 8B raw / 4B effective | UNVERIFIED | ~3 GB (3rd-party claim) | UNVERIFIED | Google claims 1.5x faster first response vs Gemma 3 4B; no absolute figure published | Custom Gemma ToU + Prohibited Use Policy | Remote-restriction clause; worst fit for open-source-bound |
| Phi-4-mini-instruct | 3.8B | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | MIT | Clean terms |
| SmolLM3-3B | 3B | ~6.17 GB BF16; Q4 size UNVERIFIED | UNVERIFIED | ~27 (Q4) / ~16 (Q8), desktop CPU [3rd-party] | UNVERIFIED | Apache 2.0 | Fully open training data; strong trust posture |

Sources per row are in sections 1 and "Runtime reality" above.

### STT / TTS

| Model | Params | Disk | License | Notes |
| --- | --- | --- | --- | --- |
| Whisper tiny | 39M | 75 MB (31 MB Q5_1) | MIT | Low accuracy off-English |
| Whisper base | 74M | 142 MB (57 MB Q5_1) | MIT | Best bundle compromise |
| Whisper small | 244M | 466 MB (182 MB Q5_1) | MIT | ~850 MB RAM; download-on-demand tier |
| Moonshine tiny/base | 27M / 61M | UNVERIFIED (v2 claims down to 1MB-class models) | MIT (English models; check per-model) | Streaming-native; English-first |
| Apple SpeechAnalyzer | closed | system asset | proprietary | On-device but not bundle-able; iOS-only |
| Kokoro-82M | 82M | 363 MB repo | Apache 2.0 | Quality pick; phone tok/s unpublished |
| Piper voices | per-voice | UNVERIFIED | engine: MIT (archived) / GPL (current) | Low-resource pick |

---

## 5. Bottom-line recommendation

Ship a layered stack, all permissively licensed, none of it Google-licensed. For the LLM: Qwen3-4B-Instruct-2507 (Apache 2.0, 2.5 GB Q4_K_M, 256K context) as the default bundling target for laptop-class devices, with SmolLM3-3B (Apache 2.0, fully open training data) as the lighter alternative where 2.5 GB is too much; treat the 4B choice as provisional until we run our own grounding tests on our own notes corpus, since no vendor publishes RAG faithfulness numbers. Avoid Gemma 3n despite its genuinely superior phone architecture (MatFormer/PLE, audio input): its custom license with the Prohibited Use Policy and reported remote-restriction clause is the single worst fit among the candidates for an open-source-bound, zero-knowledge app. For STT: bundle Moonshine (MIT) as the default with whisper.cpp tiny/base Q5_1 for multilingual, whisper small as an optional download, and platform STT as an opt-in accelerator with honest disclosure that it is a closed system model. For TTS: Kokoro-82M (Apache 2.0) where quality matters, Piper voices where resources are minimal, with a license check on which Piper codebase we link. The honest claim the app can make: fully on-device, offline, open-weights for all four capabilities, with Whisper-small-class transcription available but not in the base download on phones.

The biggest open measurement gap the field leaves us: reproducible tokens/sec for 3-4B models on phone CPUs and GPUs. Our own benchmark on target devices is a required project task, not something the literature supplies.

## Open sub-questions

- Exact RAM use at runtime for each Q4 GGUF on Android/iOS: nobody publishes vendor figures; measure with our harness. [UNVERIFIED by nature]
- SmolLM3-3B and Phi-4-mini-instruct Q4_K_M file sizes: confirm from the bartowski/unsloth repo file listings before bundling. [UNVERIFIED in this run]
- Kokoro-82M model-only size and latency on phone CPUs (and whether the ONNX path fits a mobile app): measure. [UNVERIFIED]
- Moonshine v2 model list, sizes, and per-model licenses for non-English: read the current moonshine-ai model zoo before any bundle. [not fetched in this run]
- Whether later Gemma generations really moved to Apache 2.0 (third-party claims exist): verify against Google's primary license page before revisiting Gemma at all. [UNVERIFIED]
- RAG grounding quality of Qwen3-4B vs SmolLM3 on a private-notes corpus with our chosen embedding model: our own eval; nobody has published this.
- Phone-GPU backends (Metal/Adreno Vulkan/NPU) for llama.cpp and whisper.cpp on our specific target devices: reproducible public numbers do not exist; benchmark ourselves. [finding]
- Android platform STT (what AICore/Gemini Nano or default speech service actually provides per OEM): confirm what is on-device vs cloud per device, since Google's own docs route production LLM use through closed AICore. [needs device-specific verification]
