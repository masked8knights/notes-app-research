# R6 Findings: Small Local AI Models for a Local-First, E2EE Notes App

Scope: the app ships small models on-device for (a) summarizing long documents, (b) rewriting/drafting, (c) answering questions over the user's notes (RAG), (d) speech-to-text, and (e) text-to-speech. Zero-knowledge app: nothing may call out to a server for inference. Target hardware: laptops and mid-range phones. Research date: October 2026.

Method note: every claim carries its source URL in parentheses. Where a number comes from vendor marketing rather than an independent benchmark, that is stated. Where sources conflict or no published number exists, the item is marked **unverified** or **no published number** rather than guessed. Nothing in this file names machines, hosts, network addresses, or accounts; all references are to public projects and published research.

---

## 1. Small LLMs for summarize / rewrite / RAG

### 1.1 The field as of October 2026

The 3B–4B class became genuinely usable in 2025–2026. Retrospective comparisons note that two years ago anything below 7B struggled with basic instruction following, while the 2026 edge models (Gemma 4 edge variants called out specifically) are described as the most-improved category of open-weight models in 2025–2026 (https://www.ertas.ai/best/best-small-llm-for-local-deployment). A current roundup picks as best small local LLMs: Qwen3.5 4B for 8 GB-RAM machines, Gemma 4 E4B for a multimodal 4B-class model, Phi-4 Mini 3.8B for the lightest footprint at 2.5 GB, and Qwen3.5 2B or 0.8B when RAM is the binding limit (https://www.promptquorum.com/local-llms/small-local-llm-models). General guidance elsewhere in the same space: run the largest model that fits in RAM with room to spare; for 8 GB machines that means 3B–4B (https://locul.ai/blog/best-local-llm).

### 1.2 Model-by-model

**Qwen3-4B (Alibaba).** 4.0B parameters (3.6B non-embedding), 36 layers, GQA with 32 query / 8 KV heads, 32,768-token context natively extendable to 131,072 with YaRN, dual-mode (reasoning / non-reasoning) native, Apache 2.0 license, released April 29, 2025 (https://huggingface.co/Qwen/Qwen3-4B-GGUF; https://apxml.com/models/qwen3-4b). The official GGUF family exists; Ollama's Q4_K_M build is 2.5 GB on disk (https://ollama.com/library/qwen3:4b). Real memory use at Q4 is roughly the file size plus KV cache; no vendor-published RAM figure for the quantized build was found — **no published number**.

**Qwen3.5 (February 2026).** Dense models at 0.8B, 2B, 4B, 9B, 27B and MoE models at 35B-A3B, 122B-A10B, 397B-A17B (https://vdf.ai/blog/qwen-on-premises-enterprise-deployment/). Notable for a notes app: one permissive-license family covering the whole size ladder with official quantized builds (same source). An Ollama `qwen3.5:4b` listing exists (https://ollama.com/library/qwen3.5:4b). Per-size benchmark scores for Qwen3.5 small variants were not extracted in this research pass — **unverified quality claims** beyond "best small LLM 2026" roundup positioning (https://www.promptquorum.com/local-llms/small-local-llm-models).

**Gemma 3 4B (Google).** Q4 download ~2.6 GB, recommended RAM ~6 GB (https://whatsmy.fyi/what-llm-can-i-run/gemma-3-4b); Q4_K_M loads in ~3.5 GB (https://modelfit.io/models/gemma3-4b/); another source says ~3.5 GB VRAM at Q4 with 6 GB RAM minimum for CPU fallback (https://bestllmfor.com/modele/gemma3-4b/). License: Gemma Terms — open-weight, **not** open-source, carries Google's own usage policy, which the source itself flags as something to read before shipping in a product (https://whatsmy.fyi/what-llm-can-i-run/gemma-3-4b). Inference on edge devices in 4-bit: 20–30 tokens/sec, useful for summarization/Q&A locally (https://deploybase.ai/articles/best-small-llm).

**Gemma 4 (Google, released April 2, 2026).** Multiple independent sources report the whole Gemma 4 family moved to **Apache 2.0 with no user caps or revenue terms** (https://www.yottalabs.ai/post/gemma-4-hardware-requirements-gpu-memory-2026; https://codersera.com/blog/gemma-4-vs-gemma-3-what-changed-and-should-you-switch/; https://www.mindstudio.ai/blog/gemma-4-apache-2-license-commercial-use). This is the single most important license development for shipping small models: it would make a Google-quality edge model bundlable without the Gemma Terms encumbrance. Caveat: this research relied on secondary reporting; before shipping, verify Apache 2.0 in Google's actual license text and repo — flagged **verify-before-ship**.

Gemma 4 edge models E2B/E4B: multimodal (text + vision + audio), MediaPipe-compatible, under 1.5 GB at 2-bit quantization for E2B (https://codersera.com/blog/gemma-4n-vs-gemma-4/). GGUF Q4_K_M: E2B ~1.3 GB, E4B ~2.5 GB (https://www.mindstudio.ai/blog/gemma-4-e2b-e4b-edge-models-phone-local). E2B INT4 runs on mid-range Android hardware from 2023 onward (6 GB RAM, Snapdragon 8-class) via MediaPipe and LiteRT (https://www.mindstudio.ai/blog/gemma-4-edge-deployment-e2b-e4b-models). Phone RAM estimates vary by source: ~3.1 GB of memory for E2B per one source (https://cloudinsight.cc/en/blog/gemma-4-hardware-requirements) vs ~6 GB RAM "comfortable" per another (https://gemma4all.com/blog/gemma-4-on-phone) — **conflicting sources; treat 3–6 GB as the working range, test on real devices**. The E4B at 4-bit needs roughly 5.5–6 GB (https://codersera.com/blog/gemma-4-vs-gemma-3-what-changed-and-should-you-switch/). Note: Gemma 3n (the 2025 predecessor) already demonstrated the key trick — raw 5B/8B parameters running with a 2B/4B-class memory footprint via Per-Layer Embeddings (PLE) caching and selective parameter activation, operating in as little as 2 GB / 3 GB (https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/; https://annjose.com/blog/mobile-on-device-ai-hands-on-gemma/).

**Phi-4-mini (Microsoft).** 3.8B parameters, dense decoder-only, MIT license, 128K context, 200K vocabulary across 23 languages (https://huggingface.co/unsloth/Phi-4-mini-instruct-GGUF; https://dev.co/ai/llms/phi-4-mini-instruct-gguf). Q4_K_M GGUF is 2.49 GB (https://tinyweights.dev/posts/run-phi-4-mini-locally/); Ollama lists it at 2.5 GB with vendor-published MMLU 67.3 and MATH 64.0 (https://localaimaster.com/models/phi-4-mini) — benchmark numbers are Microsoft's own, not independent. MIT makes it the most license-friendly of the "brand-name" small models.

**Llama 3.2 1B / 3B (Meta).** Explicitly designed and positioned for "highly constrained environments, such as mobile devices" (https://huggingface.co/meta-llama/Llama-3.2-1B; https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct). License is the Llama 3.2 Community License, a custom agreement (https://ollama.com/library/llama3.2:1b/blobs/fcc5a6bec9da). Restriction set (see section 1.4): 700M MAU threshold, "Built with Llama" branding, prohibition on using outputs to improve other models, not OSI-approved (https://blog.promise.legal/open-weight-ai-license-trap-startups/; https://techcrunch.com/2025/03/14/open-ai-model-licenses-often-carry-concerning-restrictions/; https://centreforaileadership.org/resources/opinion_is_llama_really_open_source_10_2024/). GGUF disk sizes were not extracted from primary sources in this pass; community Q4_K_M files are commonly cited around ~0.8 GB (1B) and ~2 GB (3B) — **approximate, unverified here**.

**Ministral 3 3B (Mistral, December 2025, part of the Mistral 3 family).** Apache 2.0, described as running on a laptop CPU or a 6–8 GB GPU at Q4_K_M, ~385 tokens/sec on an RTX 5090 (https://codersera.com/blog/run-and-install-mistral-3-3b-locally-the-complete-guide/). Ministral 3 8B is "built for edge deployment" per Mistral's docs (https://docs.mistral.ai/models/ministral-3-8b-25-12; https://docs.mistral.ai/models/ministral-3-3b-25-12). Laptop-CPU tokens/sec for the 3B: **no published number found**; the RTX 5090 figure is not representative of the target hardware.

**SmolLM3-3B (Hugging Face).** Apache 2.0, dual-mode reasoning, 6 languages, 128K context, GQA + NoPE architecture (3:1 ratio), pretrained on 11.2T tokens with a staged curriculum — and **fully open**: base model, instruct/reasoning checkpoint, data mixture, and training configs all published (https://huggingface.co/HuggingFaceTB/SmolLM3-3B; https://tinyweights.dev/posts/smollm3-3b-the-fully-ope/; https://apxml.com/models/smollm3-3b; https://atomic.chat/models/smollm3-3b). Released July 8, 2025. This is the highest-trust provenance profile in the whole survey: no vendor policy to read, no terms that can change.

### 1.3 Real-world speeds (what the numbers actually say)

Measured and community-reported anchors, none of them ours to verify:

- Apple M1, 7B model at Q4_0 via llama.cpp: ~7.9 tokens/sec generation (https://github.com/ggml-org/llama.cpp/discussions/4167).
- Qwen3 14B on M4 Max: 38 tokens/sec with MLX vs 18 tokens/sec with llama.cpp — the runtime can double the speed on the same chip (https://www.kunalganglani.com/llm-benchmarks; title also in https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html).
- Snapdragon 8 Elite phone, 14B at Q4_K_M: ~5.5 tokens/sec (community report, https://www.reddit.com/r/LocalLLaMA/ — thread surfaced in this research via aggregate listings; treat as one anecdotal data point).
- Gemma 3 4B 4-bit on edge devices: 20–30 tokens/sec (https://deploybase.ai/articles/best-small-llm).
- Aggregated Apple Silicon decode-speed databases now exist covering 109 local LLMs across M1–M6 chips and six runtimes, mixing published, community-run, and estimated rows — useful, but each row is only as good as its label (https://llmcheck.net/benchmarks; https://modelpiper.com/blog/local-llm-benchmarks-apple-silicon).
- snapbench: an open, fixed-matrix benchmark project for Snapdragon phones running llama.cpp (build b11700) across CPU, OpenCL-Adreno, Vulkan, and Hexagon NPU backends on Llama 3.2 1B/3B and Qwen3 4B — the most reproducible phone-side data located, though per-model results were not extracted in this pass (https://github.com/ggml-org/llama.cpp ecosystem references; snapbench repo surfaced via search results). **Verify directly at the repo before quoting numbers.**

Translation for the notes app: a 4B-class Q4 model on a modern laptop CPU does short summaries and rewrites at readable speed (roughly 10–30 tokens/sec depending on chip and runtime); the same model on a mid-range phone is near the edge of patience (~5–15 tokens/sec) and wants a 1–3B model or a 2-bit/4-bit edge variant instead. No source publishes a clean matrix of "mid-range phone, 2B model, Q4, tokens/sec" — that measurement is ours to make. **Gap.**

### 1.4 Licenses and vendor trust, stated plainly

Four license families dominate the small-model field (https://ai-tldr.dev/learn/local-open-models/open-model-ecosystem/open-model-licenses/; https://bestllmfor.com/ — license-family framing surfaced in this research):

1. **Apache 2.0 / MIT** — Qwen, Mistral Ministral, SmolLM3, Phi-4-mini. Redistribute, modify, ship commercially, no branding obligations, no user caps. Highest trust.
2. **Llama Community License** — free only under 700M monthly active users, with a separate license Meta may grant or deny "in its sole discretion" above that (https://blog.promise.legal/open-weight-ai-license-trap-startups/); prohibits using model outputs to improve any other model (https://techcrunch.com/2025/03/14/open-ai-model-licenses-often-carry-concerning-restrictions/); not OSI-approved open source (https://ai-tldr.dev/learn/local-open-models/open-model-ecosystem/open-model-licenses/); the multimodal variant additionally withholds grants to EU-domiciled individuals and companies (https://ollama.com/library/llama3.2:latest/blobs/a70ff7e570d9).
3. **Gemma Terms** — no MAU threshold, but a prohibited-use policy applies, and the license is open-weight rather than open-source (https://whatsmy.fyi/what-llm-can-i-run/gemma-3-4b; https://techcrunch.com/2025/03/14/open-ai-model-licenses-often-carry-concerning-restrictions/). Applies to Gemma 3.x and 3n. Gemma 4 reportedly Apache 2.0 (see 1.2, verify-before-ship).
4. **Custom non-commercial / research-only** — exists in the field but none of the models recommended below carry one (https://ai-tldr.dev/learn/local-open-models/open-model-ecosystem/open-model-licenses/).

Trust signal ranking for an E2EE product that bundles weights: SmolLM3 (fully open, Apache) > Qwen / Ministral / Phi-4-mini (Apache/MIT, reputable labs) > Gemma 4 if Apache confirmed > Llama 3.2 / Gemma 3 (usable, but with strings worth a legal read).

---

## 2. On-device inference runtimes

**llama.cpp (MIT, C/C++).** The default answer for a Rust/Tauri app. Plain C/C++ with no dependencies; Apple Silicon is a first-class citizen (ARM NEON, Accelerate, Metal); CPU paths cover AVX2/AVX512/AMX/NEON; GPU backends cover CUDA, ROCm, Vulkan, SYCL (https://github.com/ggml-org/llama.cpp; https://www.sandgarden.com/learn/llama-cpp). Compiles for iOS (simulator and device) and Android via NDK, with example apps for on-device transcription and inference (https://vexascribe.com/whisper-cpp for the mobile compile claim; the llama.cpp repo carries iOS/Android examples). On iOS, CoreML conversion can delegate matrix operations to the Apple Neural Engine and push throughput significantly higher on A17/M-class silicon (https://mvpfactory.io/blog/on-device-llm-inference-via-kmp-and-llama-cpp-memory-mapped-model-loading-ane). Memory-mapped model loading is the standard mobile pattern (same source). GGUF is the de facto quantization format across the ecosystem.

**MLC LLM (Apache 2.0).** Machine-learning compilation on Apache TVM: one model compiled to optimized native code for iOS, Android, WebGPU browsers, and GPUs from a single codebase; no other major engine covers WebGPU + iOS + Android + NVIDIA + AMD + Intel Arc from one codebase (https://www.local-llm.net/tools/mlc-llm/; https://localaimaster.com/blog/mlc-llm-setup-guide; https://freeapihub.com/ai-models/mlc-llm). WebLLM is the browser-side package (https://llm.mlc.ai/docs/get_started/quick_start). Trade-off: models must be compiled per-target (TVMLib), so the model library is platform-specific; more moving parts than GGUF for a shipping app.

**Ollama (MIT).** macOS 14+, Windows, Linux, plus Docker; also via Homebrew/Pacman/Nix (https://www.promptquorum.com/power-local-llm/ollama-review). It is a llama.cpp-based distribution layer, not its own runtime; Ollama 0.30 imports GGUF directly and the Hugging Face Hub is integrated (https://ollama.com/blog/improved-performance-and-model-support-with-gguf; https://huggingface.co/docs/hub/en/ollama). **No mobile platform support** (same sources; consistent with its CLI/desktop-server design). For the notes app this makes Ollama a developer convenience and a desktop-side model manager at most — never the shipping mechanism on phones.

**ExecuTorch (PyTorch's on-device stack, BSD-style license).** Runs LLMs, vision, and speech on-device with 12+ hardware backends; in production across Instagram, Facebook, WhatsApp serving billions of users, including Instagram's Cutouts feature migrated to ExecuTorch with speed gains on both Android and iOS (https://executorch.ai/; https://github.com/pytorch/executorch; https://engineering.fb.com/2025/07/28/android/executorch-on-device-ml-meta-family-of-apps/; https://unsloth.ai/docs/basics/inference-and-deployment/deploy-llms-phone). The strongest "proven at consumer scale" signal of any runtime, but it requires a PyTorch export path per model — heavier tooling than GGUF drop-in.

**Core ML / Apple Neural Engine.** Not a standalone LLM runtime but the iOS acceleration layer: reachable from llama.cpp via CoreML ANE delegation (see above), from WhisperKit for STT (section 3), and via Core ML Tools conversions generally. Apple introduced SpeechAnalyzer at WWDC 2025 for on-device speech recognition, which independent tests found outperforming Whisper for speed on-device (https://www.argmaxinc.com/blog/apple-and-argmax; https://www.reddit.com/r/apple/comments/1lef13s/apples_new_transcription_apis_blow_past_whisper/).

**ONNX Runtime Mobile.** Officially supports iOS and Android inference (https://onnxruntime.ai/docs/get-started/with-mobile.html; https://onnxruntime.ai/docs/tutorials/mobile/). For LLMs in production Android apps, the documented path is INT8 QDQ graphs with Qualcomm QNN delegates executing on the Hexagon NPU; on iOS, Core ML Tools conversion targets the Neural Engine; full on-device LLM fine-tuning has been demonstrated on a Pixel 6 (https://dev.to/shashank_ms_6a35baa4be138/deploying-llm-models-on-mobile-devices-with-low-power-consumption-6mn). An NPU-execution community demo of full on-device LLM training/inference/RAG on Android (MobileTransformers) also surfaced (same source thread). This is the main route to battery-friendly NPU inference for ONNX-style models (embeddings, Whisper exports, Parakeet ONNX).

**MediaPipe LLM Inference / Google AI Edge (permissive Apache 2.0 license).** Google's on-device wrapper API for small LLMs on Web, Android, and iOS; initially supported Gemma, Phi-2, Falcon, StableLM (https://developers.googleblog.com/large-language-models-on-device-with-mediapipe-and-tensorflow-lite/; https://www.reddit.com/r/LocalLLaMA/comments/1ba5jeh/). Now the recommended deployment path for Gemma on mobile, with multimodal prompting (text + image + audio inputs) on Android (https://developers.google.com/edge/mediapipe/solutions/genai/llm_inference/android; https://ai.google.dev/gemma/docs/integrations/mobile). Browser package: `@mediapipe/tasks-genai` (https://faun.dev/toolbox/mediapipe-llm-inference-api/). If the phone-side LLM is a Gemma 4 E2B, this is the paved road.

**Rust-native runtimes.** mistral.rs: Rust-native, full-stack (quantization, multimodality, tool calling, structured output), with day-0 Gemma 4 support (https://www.reddit.com/r/rust/comments/1salwsk/mistralrs_rustnative_inference_engine_withday0/; https://github.com/EricLBuehler/mistral.rs). Independent benchmarks claim its UQFF Q8 format leads llama.cpp GGUF Q8_0 in every measured row (e.g., Gemma 4 E4B prefill 7395.7 vs 3973.7 on GB10), while results against vLLM at BF16 are mixed and it trails badly on the 26B-A4B MoE (https://hysenlabs.com/projects/ericlbuehler-mistral-rs) — a single independent source; **treat the benchmark comparison as preliminary**. candle (Hugging Face's Rust tensor library) supports Llama v3, Mistral, Phi-3, Gemma with quantization (https://dasroot.net/posts/2026/01/building-llm-applications-rust-candle-llm-crates/; https://medium.com/@soumyajit.swain/rust-the-performance-edge-for-large-language-model-inference-59528a66ec68). burn: Rust ML framework, compared frequently against candle (https://www.reddit.com/r/rust/ — comparison threads surfaced in search). Licenses of candle/mistral.rs/burn were not confirmed from their repos in this pass — **unverified; check before adopting**. For a Rust/Tauri app the pragmatic pattern is: call llama.cpp through its C API (or a binding crate) rather than betting the core on a young Rust-native engine.

**LiteRT (formerly TensorFlow Lite).** Google's mobile ML runtime, named as the deployment support path for Gemma 4 edge models alongside MediaPipe (https://www.mindstudio.ai/blog/gemma-4-edge-deployment-e2b-e4b-models).

---

## 3. Speech-to-text on-device

### 3.1 Whisper size ladder and accuracy

Published parameter counts and on-disk sizes, with representative WER ranges from aggregated sources (sizes and WERs from https://openwhispr.com/blog/whisper-model-sizes-explained, https://metawhisp.com, https://theneuralbase.com, https://vexascribe.com/how-accurate-is-whisper):

- tiny: 39M params, ~39–75 MB; ~10–15% WER on clean English (OpenAI's own clean-English figure ~13%), degrading to 25–40% on noisy audio.
- base: 74M, ~74 MB; ~7–10% WER clean.
- small: 244M, ~141 MB; ~5–7% clean.
- medium: 769M, ~312 MB; ~4–5% clean.
- large-v3: 1.5B, ~2.9 GB; ~3–5% clean.

A 2026 field test (2,475 samples) measured 3.6% WER on clean read English and 12.4% WER on crowd-sourced recordings from ordinary microphones for the best Whisper variant (https://vexascribe.com/how-accurate-is-whisper). The gap between benchmark audio and real voice-note audio is the design-relevant fact.

### 3.2 Implementations (same weights, different runtimes)

Same Whisper weights produce the same WER; implementations differ in speed and platform (https://suprflow.app/guides/whisper-vs-faster-whisper-vs-whisperx; https://whipscribe.com/whisper-implementations-compared; https://modal.com/blog/choosing-whisper-variants).

- **whisper.cpp** — the CPU/Apple-Silicon winner and the portable choice: C/C++, compiles for iOS and Android via NDK, example apps demonstrate real-time on-device transcription on iPhone 12+ and modern Snapdragon 8-class Android devices (https://vexascribe.com/whisper-cpp).
- **faster-whisper** — CTranslate2-based, up to 4x faster with int8, described in an August 2026 comparison as the best default for self-hosted/server use (https://diyai.io; https://modal.com/blog/choosing-whisper-variants). Python-centric; not the mobile path.
- **WhisperX** — faster-whisper plus wav2vec2 forced alignment and pyannote diarization; the ~70x-realtime large-v2 claim is server-class (https://suprflow.app/guides/whisper-vs-faster-whisper-vs-whisperx). Diarization and word alignment matter for meeting transcripts, not for voice notes.
- **WhisperKit (Argmax)** — MIT-licensed Swift SDK running Whisper natively on Apple Neural Engine (https://whipscribe.com/tools/whisperkit; https://www.argmaxinc.com/blog/apple-and-argmax). The iOS-specific answer.
- A current landscape summary: whisper.cpp strongest for CPU/Apple portability, faster-whisper for servers, NVIDIA Parakeet TDT unusually attractive for fast local inference, Qwen3-ASR a multilingual challenger (https://diyai.io).

### 3.3 whisper.cpp on Android: the honest numbers

This is where the design tension lives, and the findings are concrete:

- Streaming/live transcription with whisper.cpp on Android runs ~5x slower than real-time even though batch transcription is fast; making it work for "live" transcription required heavily modifying the library's core logic (https://www.reddit.com/r/androiddev/comments/1po663c/whispercpp_on_android_streaming_live/ — developer report, December 2025).
- Power/accuracy sweet spot: tiny.en uses ~25% less power than base.en on flagship hardware but WER jumps from ~4.2% to ~8.7% in reverberant settings; balanced picks are tiny.en Q4_K_M on flagships and tiny.en Q3_K_M on mid-tier devices; going below Q3_K risks accuracy collapse with minimal extra savings (https://commercialtoolry.com/electronics/gemini-nano-vs-whisper-cpp-which-consumes-less-battery-on-android-for-live-transcription).
- q8_0 whisper-tiny.en on mid-range Android reaches sub-200ms latency for short chunks (aggregate finding from the same search set).

**Resolution of the design tension:** yes, Whisper-class transcription is feasible on a mid-range phone in 2026 — at tiny/base size, quantized to Q3–Q5, in **batch mode** (record, then transcribe), at usable quality for voice notes. It is **not** a good live-streaming experience on mid-range hardware with stock whisper.cpp. The honest fallback ladder for streaming/dictation: Moonshine (below) or platform native speech APIs (Apple SpeechAnalyzer on iOS 26/macOS 26, which independent tests found faster than Whisper on-device — https://www.argmaxinc.com/blog/apple-and-argmax), with Whisper small as the laptop-grade quality tier.

### 3.4 The challengers

**Moonshine (Useful Sensors, MIT license).** 27M (tiny) and 61M (base) parameters, on-device, streaming, processes audio proportional to its actual length rather than fixed 30-second windows, up to 5x faster than Whisper at comparable accuracy (https://github.com/moonshine-ai/moonshine; https://huggingface.co/UsefulSensors/moonshine-tiny; https://the-decoder.com — Nov 2024 coverage). Moonshine v2's Ergodic Streaming Encoder is designed specifically for latency-critical edge streaming (https://www.gladia.io/blog/best-open-source-speech-to-text-models). For a notes app's dictation feature this is the best fit found: MIT, tiny, streaming-native, on-device.

**NVIDIA Parakeet TDT (CC-BY-4.0).** Parakeet TDT 0.6B v3 covers 25 European languages with word timestamps and long-audio support (24 minutes full attention on A100; up to 3 hours with local attention) (https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3; https://builderai.tools/blog/speech-recognition-beyond-whisper-parakeet-sensevoice). The 1.1B variant posts the highest throughput of open models, RTFx above 2,000 (https://www.gladia.io/blog/best-open-source-speech-to-text-models). Community ONNX/LiteRT exports exist and make phone deployment real: an INT8 ONNX conversion is optimized for ONNX Runtime Web (https://huggingface.co/nasedkinpv/parakeet-tdt-0.6b-onnx-int8 — see also https://huggingface.co/fcreait/parakeet-tdt-0.6b-v3-int8-onnx for weights-only int8 quantization), and a LiteRT conversion was tested on a 2020-era Samsung flagship (Exynos 2100) with 4 CPU threads at background priority achieving roughly one-third of real time, with word-level agreement vs Whisper large-v3 of 16.1% difference at FP16-ish and 20.9% at full int8 (https://huggingface.co/supyoshi/parakeet-tdt-0.6b-v3-litert). Reading: Parakeet 0.6B runs on phones at batch speed on older mid-range silicon but its accuracy on real-world audio is a tier below Whisper medium, and quantization costs a few points. License is permissive for shipping (attribution required).

**Vosk (Apache 2.0, Kaldi-based).** ~50 MB per-language models (the small French model is 41 MB), 20+ languages, true streaming, zero-latency partial results, speaker identification (https://alphacephei.com/vosk/models; https://github.com/alphacep/vosk-api; https://sourceforge.net/projects/vosk-speech-recognition.mirror/). Current assessment: still the smallest thing that reliably works offline in embedded contexts, but a fallback rather than a first pick in 2026 — its accuracy predates the neural-transformer era (https://builderai.tools/blog/speech-recognition-beyond-whisper-parakeet-sensevoice; https://whipscribe.com/tools/vosk).

**Whisper Large V3 Turbo** provides 216x real-time speed with broad language coverage — server-class figure, listed for completeness (https://www.gladia.io/blog/best-open-source-speech-to-text-models).

### 3.5 Verdict for the notes app

Laptops: whisper.cpp with small (or medium for quality-critical use), Metal/Accelerate acceleration — batch, few seconds of latency per minute of audio. Phones: batch mode with tiny/base quantized (Q3_K_M–Q4_K_M) via whisper.cpp NDK; streaming dictation via Moonshine (MIT) as primary, Vosk as the extreme-low-resource fallback, or the platform's native speech recognizer where its privacy properties are acceptable to an E2EE promise (on-device Apple SpeechAnalyzer qualifies on device-locality; its internals are not open). All recommended model weights are permissively licensed: Whisper MIT (code/weights as released by OpenAI for openai-whisper — weights under MIT per the OpenAI repo; note some distillation variants carry different terms), Moonshine MIT, Vosk Apache 2.0, Parakeet CC-BY-4.0 (attribution), so bundling is clean for every one of them.

---

## 4. Text-to-speech on-device

**Piper (Open Home Foundation).** Fast, local, CPU-only neural TTS optimized to run real-time on a Raspberry Pi 4; on a Pi with medium-quality models it generates 1.6 seconds of speech per second (https://github.com/rhasspy/piper; https://www.home-assistant.io/voice_control/voice_remote_local_assistant/; https://www.promptquorum.com/power-local-llm/piper-tts-review). Voices are small per-voice ONNX files trained with VITS. Licensing changed: the original rhasspy/piper repo went read-only in October 2025 and active development moved to OHF-Voice/piper1-gpl, with the license changed from MIT to **GPL-3.0-or-later** (https://localaimaster.com/blog/piper-tts-setup-guide; https://aivideosensei.com/guides/piper-tts-offline-voice-guide; https://github.com/rhasspy/piper). Quality: good but audibly synthetic compared with Kokoro (https://www.promptquorum.com/power-local-llm/piper-vs-kokoro-tts).

**Kokoro-82M.** 82M-parameter model, Apache/MIT ecosystem, judged the most natural-sounding of the small English models (https://www.promptquorum.com/power-local-llm/piper-vs-kokoro-tts; https://localaimaster.com/blog/kokoro-tts-local-setup). Picovoice's on-device TTS benchmark table lists Kokoro at ~2.0 GB runtime footprint and classifies it (with Piper at ~2.6 GB) as limited to desktop or server deployments where memory is not a constraint (https://picovoice.ai/blog/on-device-tts/) — note this conflicts with the model's raw parameter count implying a much smaller file; the 2 GB figure likely includes runtime/voice-pack overhead as that source measures it. **Conflicting sources on real footprint; measure before designing the phone bundle.**

**KittenTTS (KittenML, February 2026).** The phone-feasible newcomer: 15M–80M parameter models, the 14–15M Nano under 25 MB INT8, runs on CPU without a GPU; developer preview v0.8 with known issues in the Nano INT8 variant; March 2026 releases added 80M/40M/14M tiers, the 80M being highest quality and the 14M claiming state-of-the-art expressivity at its size (https://github.com/KittenML/KittenTTS; https://rits.shanghai.nyu.edu/ai/kittentts-state-of-the-art-voice-synthesis-in-under-25-mb/; https://news.ycombinator.com/item?id=47441546). Picovoice's benchmark lists Kitten TTS Nano at a 320 MB runtime footprint, "fit mid-range devices" (https://picovoice.ai/blog/on-device-tts/). English 8 voices in v0.8; language coverage thin. License of the repo was not confirmed in this pass — **unverified; check before bundling** (the project is presented as open-source).

**Other 2025–2026 on-device entries** (sizes from Picovoice's August 2026 benchmark unless noted): Supertonic TTS 2 at 450 MB (mid-range feasible), Pocket TTS (Kyutai) at 610 MB with the best core-hour ratio in the mid-range tier at 0.37x (https://picovoice.ai/blog/on-device-tts/), Neu-TTS-Nano at 2.1 GB, Chatterbox-TTS-Turbo at 7.5 GB (https://picovoice.ai/blog/on-device-tts/).

**License is the real decision-maker in TTS**: Kokoro, Chatterbox, Bark, Orpheus 3B are Apache/MIT (commercial-safe); Piper's active fork is GPL-3.0 (commercially usable but copyleft); XTTS v2 is CPML; F5-TTS weights are CC-BY-NC; Fish Speech open is CC-BY-NC-SA-4.0 (https://localaimaster.com/blog/best-local-tts-models). The non-commercial ones are disqualified for a shipping product regardless of quality.

**Verdict:** Desktop/laptop TTS: Kokoro-82M (Apache/MIT, most natural small model). Phone TTS: KittenTTS or Supertonic TTS 2 as the only found options with a mid-range footprint; both young (KittenTTS is a developer preview) — budget for voice-quality iteration, and **verify KittenTTS's license text directly before shipping**. Piper is the reference architecture for tiny per-voice ONNX TTS, but under this project's GPL/AGPL concepts-only rule for code, GPL-3.0 Piper is adopted as a concept/design reference rather than a linked dependency in the proprietary app; the same VITS-on-ONNX pattern is implementable or reachable through permissive alternatives.

---

## 5. RAG and embeddings on-device

### 5.1 Embedding models

- **Qwen3-Embedding (0.6B / 4B / 8B, Alibaba, Apache 2.0).** 32K context; the 8B scores 70.58 on MTEB multilingual (highest open score at the time of release), and the 0.6B scores 70.47 on MTEB English v2 — i.e., the smallest sibling nearly matches the flagship (sources aggregated in this research: https://supermemory.ai, https://maximem.ai — Sept 2026, https://futureagi.com, https://bentoml.com — roundup context). Apache 2.0 across all sizes.
- **EmbeddingGemma-300M (Google, September 2025).** 308M parameters, 2K context, trained for 100+ languages, highest-ranking text-only multilingual embedding model under 500M on MTEB at release, built from Gemma 3 with T5Gemma initialization (https://developers.googleblog.com/en/introducing-embeddinggemma/; https://huggingface.co/blog/embeddinggemma; https://huggingface.co/google/embeddinggemma-300m; https://ai.google.dev/gemma/docs/embeddinggemma). Ships QAT (quantization-aware trained) q4_0 and q8_0 builds designed for on-device use, listed on Ollama as `embeddinggemma:300m-qat-q4_0` / `-q8_0` (https://www.reddit.com/r/LocalLLaMA/comments/1n8egxb/). 768 output dimensions, ~69.67 MTEB English v2 (aggregated in research). License: Gemma Terms — usable but not permissively licensed; flagged against this app's preference for clean-license components. Community reports note uneven non-English quality despite the multilingual training claim (same Reddit thread — anecdotal).
- **Jasper-Token-Compression-600M (Snowflake, MIT).** 74.75 on MTEB English v2, rank 2 among open models at the time measured — the strongest MIT-licensed scorer found (aggregated in research: https://maximem.ai — Sept 2026).
- **harrier-oss-v1-0.6b (MIT):** 69.01 multilingual (aggregated: https://maximem.ai).
- **BGE-M3:** dense + sparse + multivector in one model, 63.0 multilingual score, the most-downloaded open embedding model; the multi-vector output is useful for hybrid retrieval (aggregated: https://futureagi.com, https://bentoml.com).
- **all-MiniLM-L6-v2 (Apache 2.0):** still the universal baseline; a 2026 study measured 83 ms latency and 492 MB memory footprint for it in a small-model deployment (aggregated: https://bentoml.com / study surfaced in this research). Good enough for single-language note search; weaker multilingual.

For a notes-app corpus (typically hundreds to tens of thousands of notes), what matters is: per-note embedding cost on CPU, memory footprint, and license — not top-of-MTEB scores, since retrieval over a private corpus with a known domain is an easier task than the benchmark. A 100–600M parameter model at int8 (roughly 60–600 MB on disk) is the right size class; 32K context (Qwen3-Embedding) comfortably embeds whole long notes in one pass.

### 5.2 Vector stores for an embedded, local-first app

- **sqlite-vec (Alex Garcia).** Portable C extension, zero dependencies, runs anywhere SQLite runs (including phones); the successor to sqlite-vss; repeatedly characterized as "surprisingly solid" for smaller/local-scale workloads (https://llms.blog — Aug 2026; https://kanopylabs.com — Sept 2026; https://firecrawl.dev; https://mongreldb.com). Ideal fit for a notes app already using SQLite: vectors live beside the notes in the same database file, which matters for an E2EE app that syncs one encrypted blob store.
- **LanceDB.** Embedded, columnar, zero-copy memory-mapped reads, handles larger-than-memory datasets, has a well-regarded Rust API (community feedback: https://www.reddit.com/r/rust threads surfaced in research; https://kanopylabs.com). It is the default vector store of AnythingLLM (https://www.aitooldiscovery.com/how-to/anythingllm-setup-guide). Better choice if the corpus or metadata outgrows SQLite or columnar scans/versions are wanted; heavier dependency than sqlite-vec.
- **usearch** (single-file, SIMD, many-language bindings) and **Qdrant-local** (embedded mode of the Qdrant engine) are the remaining credible candidates; both surfaced as embedded options in the same comparisons (https://kanopylabs.com; https://github.com/hirnlabs/hirn/issues/84). Not deeply evaluated in this pass — **unverified beyond listing**.

What a notes-sized corpus actually needs: brute-force (exact) cosine search over a few thousand 384–768-dimension vectors is sub-millisecond to low-millisecond on CPU and needs no index at all; approximate indexes (IVF/HNSW) earn their complexity only in the tens-of-thousands to millions range. Consequence: sqlite-vec with brute-force + optional sqlite-vec indexes covers the design space; the exotic-ANN complexity can be deferred indefinitely.

### 5.3 Verdict

Embeddings: Qwen3-Embedding-0.6B (Apache 2.0) as default, with EmbeddingGemma-300M QAT q4_0 as the size-optimized alternative if its Gemma Terms are acceptable for bundling in a given jurisdiction/product decision, and Jasper-Token-Compression (MIT) where English-only is enough and top accuracy is wanted. Store: sqlite-vec inside the existing encrypted SQLite store. Chunking and re-embedding policy (what triggers re-embedding on note edit) is app logic, not research; no external dependency needed.

---

## 6. Integration verdict for a Rust/Tauri, zero-knowledge app

The app's rule: GPL/AGPL-licensed code is adopted concepts-only (design reference, not linked dependency); model weights follow their own licenses, stated per model above.

**LLM (summarize / rewrite / RAG answer generation).**
- Laptop (8+ GB): Qwen3-4B or Phi-4-mini (both Apache/MIT) at Q4_K_M (~2.5 GB) via llama.cpp compiled into the Tauri app (MIT, C API callable from Rust directly or via a binding crate). SmolLM3-3B as the fully-open provenance alternative. Gemma 4 E4B if the Apache 2.0 relicense is confirmed in the license text — it is the strongest 4B-class multimodal candidate.
- Phone (Android): llama.cpp via NDK with a 1–3B model (Qwen3.5 0.8B/2B, Llama 3.2 1B/3B noting its community-license strings, or SmolLM3's smaller siblings if quality holds); OR Gemma 4 E2B (~1.3 GB Q4_K_M, Apache 2.0 per reporting) through MediaPipe/LiteRT on the officially supported path for mid-range 2023+ devices. The MediaPipe path trades GGUF uniformity for the paved road (NPU-friendly, maintained). **Decision to test on real devices, not in documents.**
- Phone (iOS): llama.cpp with Metal + optional CoreML ANE delegation is the unified answer; WhisperKit-style Core ML packaging is the pattern to imitate for any Core ML models. No Ollama on mobile, ever — it is a desktop tool.
- Memory-mapped GGUF loading is the required pattern for mobile (load-from-disk without full RAM residency) (https://mvpfactory.io/blog/on-device-llm-inference-via-kmp-and-llama-cpp-memory-mapped-model-loading-ane).

**STT.** whisper.cpp (MIT) everywhere for batch transcription of voice notes: small on laptops, tiny/base Q3_K_M–Q4_K_M on phones. Moonshine (MIT) for streaming/dictation on phones. Platform-native recognizers (Apple SpeechAnalyzer) as an optional quality/speed path on iOS 26+, keeping in mind that for an E2EE promise an on-device native engine is acceptable where its terms allow, while open-source weights (Whisper/Moonshine) are the auditable default. Parakeet ONNX (CC-BY-4.0) is the quality-per-watt challenger worth benchmarking on Hexagon NPU via ONNX Runtime QNN delegates.

**TTS.** Kokoro-82M (Apache/MIT) on desktop; KittenTTS or Supertonic TTS 2 on phones pending license verification and quality testing. Piper: concepts-only under the GPL rule (its VITS-ONNX-per-voice-file architecture is the design blueprint either way).

**RAG.** Qwen3-Embedding-0.6B (Apache 2.0) + sqlite-vec (check its license file before linking: widely presented as MIT/permissive — **verify in repo**) inside the app's existing encrypted SQLite. Brute-force search until the corpus proves otherwise.

**Distribution of weights.** Ship weights as downloadable content, not embedded in the binary (keeps the app store packages small and lets users choose model quality tiers). All recommended weights (Apache/MIT/CC-BY-4.0-weights) permit redistribution; record attribution files for CC-BY-4.0 (Parakeet). License-verification checklist before ship: Gemma 4 license text (Apache 2.0 confirmation), KittenTTS license, sqlite-vec license, candle/mistral.rs licenses if adopted, Whisper weight-license terms for the exact checkpoint used.

---

## 7. Honest gaps and unverified items (consolidated)

- **No clean published matrix** of tokens/sec for 1B–4B Q4 models on mid-range phone CPUs/GPUs; community anecdotes (e.g., ~5.5 tok/s for a 14B on a flagship Snapdragon) and the snapbench project are the closest anchors. First-party benchmarking on real target devices is mandatory.
- **Gemma 4 Apache 2.0** rests on secondary reporting (multiple, consistent, April–July 2026); confirm in Google's official license text.
- **KittenTTS license** and **candle / mistral.rs / burn licenses**: not confirmed in this pass.
- **sqlite-vec license**: presented as permissive in all sources read; confirm the exact license in the repository.
- **Llama 3.2 GGUF exact disk sizes**: approximate community figures, not extracted from a primary source.
- **Kokoro phone footprint**: sources conflict (raw 82M params vs a 2.0 GB runtime figure in one benchmark table); measure.
- **Parakeet on-phone accuracy**: one community LiteRT test (Italian voice notes vs Whisper large-v3 transcripts) — directionally useful, not a benchmark-grade result.
- **Vendor-published benchmark numbers** for Phi-4-mini (MMLU 67.3, MATH 64.0) are Microsoft's own table, not independent.
- **mistral.rs vs llama.cpp performance claims** come from one independent benchmark source; preliminary.
- Whisper tiny/base WER figures vary across aggregator sources by a few points; treat the ladder's ordering as solid and the exact percentages as ranges.

All URLs are public documentation, model cards, published benchmarks, or dated reporting; nothing in this file identifies machines, hosts, network addresses, or accounts.
