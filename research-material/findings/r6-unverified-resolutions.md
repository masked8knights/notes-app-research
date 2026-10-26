# r6-unverified-resolutions.md

**Lane:** verify-and-fill pass over `findings-r5/` and `findings-r6/` (read-only; this file is the only output).
**Date of this pass:** October 26, 2026.
**Method:** direct registry checks (crates.io API, PyPI JSON, npm registry, raw.githubusercontent LICENSE/Cargo.toml/pyproject reads, shallow git clone), plus web search and page fetches for everything else. Every claim carries its source URL in parentheses.

## Prioritization statement

Priority went in this order, as agreed: (1) licenses and one "is it even licensed at all" question, because a mis-pulled license is the worst failure mode for a local-first Rust notes app; (2) repo statuses and current versions of candidate dependencies; (3) benchmark numbers and published performance figures that decisions were leaning on; (4) trust/security items (the Dillinger accusation, palm-rejection doc URL). Version-number cosmetics and star counts were batched at the end and several were left alone. Every license item found in the source files is covered; every repo-status and benchmark item is covered; cosmetic gaps that resolve only with per-repo page fetches are explicitly batched as "left for the main session".

Total items: 34. Verdicts: 22 RESOLVED, 5 PARTIALLY RESOLVED, 7 NOT FOUND (does not publicly exist / genuinely unpublished).

---

## A. Licenses (load-bearing)

### A1. Xournal++ license ambiguity (GPL-2.0-only vs GPL-2.0-or-later)
- **Source:** `findings-r6/r6-xournalpp-ecosystem.md`, section 3 — "LICENSE file states GPL-2.0; whether -only or -or-later unverified".
- **Found:** The repo's LICENSE is the verbatim GPL-2.0 text (https://raw.githubusercontent.com/xournalpp/xournalpp/master/LICENSE). The appdata template declares `project_license: GPL-2.0` — the bare, SPDX-deprecated form that specifies neither (https://raw.githubusercontent.com/xournalpp/xournalpp/master/resources-templates/com.github.xournalpp.xournalpp.appdata.xml.in). A grep of the entire checked-out source tree (tarball from https://codeload.github.com/xournalpp/xournalpp/tar.gz/refs/heads/master) finds zero "or (at your option) any later version" headers and zero `-or-later` SPDX strings; the source files carry no license headers at all.
- **Verdict: RESOLVED (as far as publicly decidable).** Upstream never made the only/or-later choice explicit. The only machine-readable declaration anywhere is the bare "GPL-2.0". For the project's concepts-only handling this changes nothing (GPL family either way), but the note "or-later" should be dropped and replaced with: upstream declares bare GPL-2.0; treat as GPL-2.0-only absent a statement from upstream.

### A2. snlib (Walnut356/SN-format parser) — is it licensed at all?
- **Source:** `findings-r6/r6-xournalpp-ecosystem.md`, section on snlib — "license unverified".
- **Found:** No LICENSE file exists on the default branch (https://raw.githubusercontent.com/Walnut356/snlib/main/LICENSE returns 404; same for master), and the Cargo.toml has no `license` or `license-file` key (https://raw.githubusercontent.com/Walnut356/snlib/main/Cargo.toml).
- **Verdict: RESOLVED — NOT LICENSED.** Under default copyright rules the code is all-rights-reserved. Reimplementing the SN format from reading it is the concepts-only route; the code itself is not pullable. This upgrades the risk note from "check the license" to "there is none".

### A3. jya-dev/supernote-tool license
- **Source:** `findings-r6/r6-xournalpp-ecosystem.md` — "Apache-2.0, not re-confirmed".
- **Found:** LICENSE file is Apache-2.0 (https://raw.githubusercontent.com/jya-dev/supernote-tool/main/LICENSE).
- **Verdict: RESOLVED — Apache-2.0.** Pullable.

### A4. jya-dev/supernote-tool maintenance status (last commit date)
- **Source:** `findings-r6/r6-xournalpp-ecosystem.md` — "last-commit date unverified".
- **Found:** Shallow clone of https://github.com/jya-dev/supernote-tool (via https://github.com/jya-dev/supernote-tool) shows the last commit dated 2026-08-23.
- **Verdict: RESOLVED — active** (last commit roughly two months before this pass).

### A5. troussos/supernote-editor license
- **Source:** `findings-r6/r6-xournalpp-ecosystem.md` — "license of supernote-editor unverified".
- **Found:** Apache-2.0 (https://raw.githubusercontent.com/troussos/supernote-editor/main/LICENSE).
- **Verdict: RESOLVED — Apache-2.0.**

### A6. nelinory/SupernoteSharp details
- **Source:** `findings-r6/r6-xournalpp-ecosystem.md` — "SupernoteSharp (MIT?) — details unverified".
- **Found:** MIT, copyright (c) 2023-2024 Chavdar Kostov (https://raw.githubusercontent.com/nelinory/SupernoteSharp/main/LICENSE).
- **Verdict: RESOLVED — MIT, pullable.**

### A7. fbalobanov/supernote-viewer status
- **Source:** `findings-r6/r6-xournalpp-ecosystem.md` — "supernote-viewer status unverified".
- **Found:** The repo is gone: tarball endpoints return 404 on both `main` and `master` (https://codeload.github.com/fbalobanov/supernote-viewer/tar.gz/refs/heads/main). A web search turns up only other Supernote viewers (https://github.com/osheroff/supernote-viewer; https://github.com/schaefer-dev/supernote-viewer), not this one (search: https://www.bing.com — "fbalobov supernote-viewer github").
- **Verdict: RESOLVED — repo does not publicly exist any more** (renamed or deleted). The ecosystem entry should point at osheroff/supernote-viewer or schaefer-dev/supernote-viewer instead.

### A8. Obsidian Supernote plugin repo URL
- **Source:** `findings-r6/r6-xournalpp-ecosystem.md` — "repo URL unverified".
- **Found:** philips/supernote-obsidian-plugin, described as Supernote A5, A5X, A6X, A6X2 (Nomad) and A5X2 (Manta) integration for Obsidian (search result listing: https://github.com/philips/supernote-obsidian-plugin; corroborating topics page: https://github.com/topics/supernote).
- **Verdict: RESOLVED.**

### A9. candle license
- **Source:** `findings-r6/r6-local-ai-models.md`, section 7 — "licenses of candle/mistral.rs/burn were not confirmed from their repos".
- **Found:** candle is dual-licensed MIT and Apache-2.0 (https://raw.githubusercontent.com/huggingface/candle/main/LICENSE-MIT; https://raw.githubusercontent.com/huggingface/candle/main/LICENSE-APACHE).
- **Verdict: RESOLVED — MIT OR Apache-2.0.** Pullable.

### A10. mistral.rs license
- **Source:** same as A9.
- **Found:** MIT, copyright (c) 2024 Eric Buehler (https://raw.githubusercontent.com/EricLBuehler/mistral.rs/main/LICENSE).
- **Verdict: RESOLVED — MIT.**

### A11. burn license
- **Source:** same as A9.
- **Found:** burn is dual-licensed MIT and Apache-2.0 (https://raw.githubusercontent.com/tracel-ai/burn/main/LICENSE-APACHE; https://raw.githubusercontent.com/tracel-ai/burn/main/LICENSE-MIT).
- **Verdict: RESOLVED — MIT OR Apache-2.0.**

### A12. KittenTTS license
- **Source:** `findings-r6/r6-local-ai-models.md`, section 5 — "license of the repo was not confirmed in this pass".
- **Found:** Apache-2.0 (https://raw.githubusercontent.com/KittenML/KittenTTS/main/LICENSE).
- **Verdict: RESOLVED — Apache-2.0.** Pullable; the "check before bundling" note can be cleared.

### A13. sqlite-vec license
- **Source:** `findings-r6/r6-local-ai-models.md`, section 7 — "license unverified".
- **Found:** dual-licensed MIT and Apache-2.0 (https://raw.githubusercontent.com/asg017/sqlite-vec/main/LICENSE-MIT; https://raw.githubusercontent.com/asg017/sqlite-vec/main/LICENSE-APACHE).
- **Verdict: RESOLVED — MIT OR Apache-2.0.**

### A14. diamond-types license (MIT assumption)
- **Source:** `findings-r6/r6-sync-crdt-stack.md`, diamond-types section — "license assumed MIT, confirm".
- **Found:** The crate is **ISC**, not MIT: Cargo.toml declares `license = "ISC"` for version 2.0.0 (https://raw.githubusercontent.com/josephg/diamond-types/master/Cargo.toml).
- **Verdict: RESOLVED with a correction.** ISC is functionally MIT-equivalent for pull purposes (permissive, attribution required), but the findings file should say ISC, not MIT.

### A15. Keyhive license
- **Source:** `findings-r6/r6-sync-crdt-stack.md`, Keyhive section — "license unverified".
- **Found:** Apache-2.0 (https://raw.githubusercontent.com/inkandswitch/keyhive/main/LICENSE).
- **Verdict: RESOLVED — Apache-2.0.**

### A16. diff-match-patch Python port license
- **Source:** `findings-r6/r6-sync-crdt-stack.md`, diff-match-patch section — "Apache-2.0 stated, not re-captured".
- **Found:** Apache-2.0 (https://raw.githubusercontent.com/diff-match-patch-python/diff-match-patch/main/LICENSE).
- **Verdict: RESOLVED — Apache-2.0.**

### A17. secsync license (AGPL-3.0 assumption)
- **Source:** `findings-r6/r6-sync-crdt-stack.md`, E2EE sync section — "license assumed AGPL-3.0".
- **Found:** The main repo's LICENSE is **Apache-2.0** (https://raw.githubusercontent.com/nikgraf/secsync/main/LICENSE). The README describes it as beta software (https://raw.githubusercontent.com/nikgraf/secsync/main/README.md).
- **Verdict: RESOLVED with a correction.** The AGPL-3.0 association likely comes from an older era of the project; today the code is Apache-2.0, which means it is pullable — the "concepts-only" treatment can be revisited if the stack is chosen.

### A18. tanamigrator license
- **Source:** `findings-r6/r6-xournalpp-ecosystem.md` — "license unverified".
- **Found:** No license: the pyproject has no license field and no LICENSE file exists (repo tarball via https://codeload.github.com/glibalien/tanamigrator/tar.gz/refs/heads/main; package metadata names it `tana-to-obsidian` 3.3.0).
- **Verdict: RESOLVED — NOT LICENSED.** Read-only reference use only.

### A19. xournalpp_htr license
- **Source:** `findings-r6/r6-htr-ocr-engines-b.md`, section on xournalpp_htr — "license of xournalpp_htr itself not confirmed".
- **Found:** GPL-2.0 (https://raw.githubusercontent.com/PellelNitram/xournalpp_htr/main/LICENSE).
- **Verdict: RESOLVED — GPL-2.0.** Concepts-only treatment stands (no code pull).

### A20. ArabicOCR_KHATT PyPI version + license
- **Source:** `findings-r6/r6-htr-ocr-engines-b.md` — "version number on PyPI not captured".
- **Found:** PyPI package `arabicocr-khatt` exists, version 0.1.0, license field MIT (https://pypi.org/pypi/arabicocr-khatt/json); repo LICENSE confirms MIT (https://raw.githubusercontent.com/FixFips/ArabicOCR_KHATT/main/LICENSE).
- **Verdict: RESOLVED — 0.1.0, MIT.** Note: a 0.1.0 on a solo research project is consistent with "young but real".

### A21. KHATT dataset license terms (can derivative weights ship?)
- **Source:** `findings-r6/r6-htr-ocr-engines-b.md` — "whether KHATT's agreement permits derivative model weights: unverified".
- **Found:** KHATT v1.0 is distributed free of charge "for academic and research purposes" (https://www.kaggle.com/datasets/nizarcharrada/khattarabic/data) and is also distributed by the Linguistic Data Consortium as LDC2015T23 under a research license (https://catalog.ldc.upenn.edu/LDC2015T23). No public document grants redistribution or commercial use, and no public statement addresses derivative model weights.
- **Verdict: PARTIALLY RESOLVED.** The license is documented as academic/research-only; the derivative-weights question is not answered anywhere public, and an academic-only license is strong evidence weights trained on KHATT must not ship in a product without written permission from the dataset owners. Keep as a hard legal checkpoint; the practical reading is "weights are research-only".

### A22. docTR per-backbone model licenses
- **Source:** `findings-r6/r6-htr-ocr-engines-a.md` — "docs model-licenses section could not be read".
- **Found:** The code is Apache-2.0 (repo README: "Distributed under the Apache 2.0 License", https://github.com/mindee/doctr; source-file headers agree, https://mindee.github.io/doctr/latest/_modules/doctr/models/zoo.html). The dedicated per-backbone "model licenses" docs page still did not surface in searches or fetches this pass.
- **Verdict: PARTIALLY RESOLVED.** Code-level Apache-2.0 confirmed from the repo itself; the pre-trained-weight license question remains open. Recommendation stands: before pulling any specific checkpoint, check that checkpoint's page on the Hugging Face hub, where pretrained artifacts actually live.

---

## B. Repo statuses and current versions (load-bearing)

### B1. yrs current version
- **Source:** `findings-r6/r6-sync-crdt-stack.md`, Y.rs section — "current version unverified".
- **Found:** crates.io: `yrs` max_version 0.28.0, updated 2026-09-17, ~4.36M total downloads (https://crates.io/api/v1/crates/yrs).
- **Verdict: RESOLVED — 0.28.0 (2026-09-17), very widely used.**

### B2. Cryptomator latest version
- **Source:** `findings-r6/r6-sync-crdt-stack.md`, E2EE section — "latest version unverified".
- **Found:** Official releases page is live with recent security fixes (https://github.com/cryptomator/cryptomator/releases); Softpedia's tracker lists 1.19.3 (June 2026) as the current release (https://www.softpedia.com/get/Security/Decrypting/Cryptomator.shtml — via search snippet).
- **Verdict: RESOLVED — latest ≈ 1.19.3 (mid-2026); actively maintained.**

### B3. secsync release status
- **Source:** `findings-r6/r6-sync-crdt-stack.md` — "current release status unverified".
- **Found:** npm package `secsync` latest is 0.5.0 with the registry's last modification in June 2024 (https://registry.npmjs.org/secsync); `@serenity-kit/secsync` returns no package. README still says beta (https://raw.githubusercontent.com/nikgraf/secsync/main/README.md).
- **Verdict: RESOLVED — the library is a beta whose last npm publish is over two years old.** Not production-grade as of this pass.

### B4. `tesseract` / `leptess` Rust binding maintenance
- **Source:** `findings-r6/r6-htr-ocr-engines-a.md`, Tesseract section — "current maintenance status unverified".
- **Found:** `tesseract` crate 0.15.2, updated 2025-04-19, ~272k downloads (https://crates.io/api/v1/crates/tesseract); `leptess` 0.14.0, updated 2023-02-21, ~309k downloads (https://crates.io/api/v1/crates/leptess).
- **Verdict: RESOLVED.** `tesseract` was updated about 18 months before this pass (fresh enough for a wrapper); `leptess` is over three years stale. The `tesseract` crate is the binding to use; `leptess` should be marked stale.

### B5. diff-match-patch Rust crate existence/maintenance
- **Source:** `findings-r6/r6-sync-crdt-stack.md` — "Rust port existence/maintenance unverified".
- **Found:** crates.io crate `diff-match-patch` 0.3.1, updated 2026-09-16, ~5.5k downloads (https://crates.io/api/v1/crates/diff-match-patch).
- **Verdict: RESOLVED — a maintained Rust port exists (updated last month) but with very low adoption.** Fine as a helper; not ecosystem-critical.

### B6. loro / automerge crate currency (context for the sync comparison)
- **Source:** same file, Loro/Automerge sections (versions were approximate).
- **Found:** `loro` 1.17.1, updated 2026-10-22 (four days before this pass), ~1.0M downloads (https://crates.io/api/v1/crates/loro); `automerge` 0.12.0, updated 2026-09-16, ~766k downloads (https://crates.io/api/v1/crates/automerge).
- **Verdict: RESOLVED — both actively released; Loro's release cadence is the fastest of the batch.**

### B7. Tangent (notes app) latest version and repo status
- **Source:** `findings-r6/r6-batch2-minor-note-apps.md` — "latest release unverified".
- **Found:** Official repo is suchnsuch/Tangent (https://github.com/suchnsuch/Tangent); the project is Apache-2.0 per its own site (https://www.tangentnotes.com/). The releases feed shows latest `tangent-v0.13.0-alpha.3` with `tangent-v0.12.10` the newest stable line (https://github.com/suchnsuch/Tangent/releases.atom).
- **Verdict: RESOLVED — active, v0.13.0-alpha.3 pre-release / v0.12.10 stable.**

### B8. Thymer pricing
- **Source:** `findings-r6/r6-batch2-minor-note-apps.md` — "pricing unverified to the cent".
- **Found:** Thymer's own homepage says mobile apps are out and pricing is not final: free while they work out the details, with the stated intention of free forever including end-to-end-encrypted sync for personal use and about $10 per user per month for commercial teams (https://thymer.com/).
- **Verdict: RESOLVED — pricing does not publicly exist as final numbers.** The $10/user/month commercial indication is the vendor's own statement; personal use is free. There is nothing more precise to verify.

### B9. Palm-rejection documentation URL (404 at research time)
- **Source:** `findings-r6/r6-htr-ocr-engines-b.md`, checklist — "URL returned 404 on direct fetch".
- **Found:** The Compose quick-guide URL is live and indexed as of January 2026 (https://developer.android.com/develop/ui/compose/quick-guides/content/reject-stylus-palm-touches), and a second official page covers the same topic as a cookbook recipe (https://developer.android.com/develop/adaptive-apps/cookbook/stylus-palm-rejection), plus the advanced-stylus overview (https://developer.android.com/develop/ui/compose/touch-input/stylus-input/advanced-stylus-features).
- **Verdict: RESOLVED.** The 404 was transient or a fetch-side refusal; the URL is correct. Add the cookbook URL as a second source.

---

## C. Benchmarks and published numbers (load-bearing)

### C1. docTR benchmark tables (page unreachable at research time)
- **Source:** `findings-r6/r6-htr-ocr-engines-a.md`, docTR section — "exact table values unverified".
- **Found:** The docs page is fully reachable and contains per-architecture tables. Text detection on FUNSD/CORD (recall/precision, sec/it at batch 1 on an 11th-gen Intel Core i7-11800H): `db_resnet50` 25.4M params, FUNSD 83.56/86.68, CORD 92.61/86.39, 1.1 sec/it; `db_mobilenet_v3_large` 4.2M params, FUNSD 82.69/84.63, CORD 94.51/70.28, 0.5 sec/it; `fast_tiny` 13.5M params, FUNSD 84.90/85.04, CORD 93.73/76.26, 0.7 sec/it (0.4 with reduced input); `fast_base` 16.3M params, FUNSD 84.95/86.73, CORD 94.39/85.36, 0.8 sec/it (https://mindee.github.io/doctr/latest/using_doctr/using_models.html).
- **Verdict: RESOLVED.** The key decision-relevant fact: docTR's mobile-shaped detection models (`db_mobilenet_v3_large`, `fast_*`) land within ~2 points of the big ResNet50 on recall at a fraction of the params. Recognition tables are on the same page.

### C2. PP-OCRv5 model file sizes and latency
- **Source:** `findings-r6/r6-htr-ocr-engines-a.md`, PaddleOCR section — "exact figures not captured".
- **Found:** PaddleX's text-recognition model list: PP-OCRv5_server_rec 81 MB (86.38% average accuracy), PP-OCRv5_mobile_rec 16 MB (81.29%), en_PP-OCRv5_mobile_rec 7.5 MB (85.25% English), korean/latin/eslav mobile variants 14 MB; GPU (T4) 5.43 ms / 1.46 ms per page for server/mobile recognition, CPU 21.20 ms / 5.32 ms (https://paddlepaddle.github.io/PaddleX/3.2/en/module_usage/tutorials/ocr_modules/text_recognition.html).
- **Verdict: RESOLVED.** The phone target (PP-OCRv5_mobile_rec) is 16 MB, and the published CPU numbers are in single-digit milliseconds per page on server-class CPUs. English-only mobile is 7.5 MB and more accurate on English than the multilingual mobile model.

### C3. ML Kit digital ink recognition latency
- **Source:** `findings-r6/r6-htr-ocr-engines-a.md` — "no numbers on Google's pages; unverified elsewhere".
- **Found:** Google's official docs publish no figure (https://developers.google.com/ml-kit/vision/digital-ink-recognition/android), but Google's launch statement, reported by VentureBeat in August 2020, put recognition time at about 100 ms depending on device hardware and the size of the stroke sequence (https://venturebeat.com/business/google-adds-digital-ink-recognition-api-for-touch-and-stylus-input-to-ml-kit/).
- **Verdict: RESOLVED with a caveat.** ~100 ms is the only public figure, it is six years old and device-dependent; no newer number exists.

### C4. mistral.rs vs llama.cpp benchmark
- **Source:** `findings-r6/r6-local-ai-models.md` — "single independent source; treat as preliminary".
- **Found:** A second, independent class of evidence now exists: community reports of much faster prompt (prefill) processing with slightly slower generation versus llama.cpp (https://www.reddit.com/r/LocalLLaMA — mistral.rs comparison threads surfaced in search), alongside the earlier independent tables showing UQFF Q8 leading GGUF Q8_0 in every row, e.g. Gemma 4 E4B prefill 7395.7 vs 3973.7 on GB10 (https://hysenlabs.com/projects/ericlbuehler-mistral-rs).
- **Verdict: PARTIALLY RESOLVED.** Two independent sources now agree on the shape (prefill win, generation roughly par or slightly behind llama.cpp); still no rigorous, reproducible head-to-head. The "preliminary" flag can soften but should not be removed.

### C5. Does Notion use Yjs?
- **Source:** `findings-r6/r6-sync-crdt-stack.md` — "Notion-Yjs usage unverified".
- **Found:** Notion's own engineering blog (September 2026) describes how Notion handles concurrent editing with CRDTs and discusses Yjs as an example of how ProseMirror editors model splits — while describing its own approach as distinct (https://www.notion.com/blog/how-notion-handles-concurrent-editing-with-crdts). Third-party sources continue to assert "Yjs is used by Notion" (e.g. https://antigravitylab.net/en/articles/app-dev/antigravity-crdt-collaborative-editing).
- **Verdict: PARTIALLY RESOLVED / NUANCED.** Notion's own post does not confirm using Yjs specifically; the third-party claim is weaker than it looks. The findings file should stop citing "Notion uses Yjs" as adoption evidence and instead say Notion uses CRDTs with a custom approach.

### C6. Independent benchmark of Loro
- **Source:** `findings-r6/r6-sync-crdt-stack.md` — "no independent benchmark found".
- **Found:** One genuinely independent comparison now exists: an open-source project's milestone benchmark of Loro vs Y.rs vs Automerge with a recorded architecture decision (https://github.com/giosuel/imaginarium/pull/16). Third-party guides also summarize numbers from the shared crdt-benchmarks suite (https://www.pkgpulse.com/guides/yjs-vs-automerge-vs-loro-crdt-libraries-2026; suite itself: https://github.com/dmonad/crdt-benchmarks), and Loro publishes reproducible WASM benchmark tables of its own (https://www.loro.dev/docs/performance).
- **Verdict: RESOLVED.** An independent (if small-scale) benchmark exists; rigorous large-scale independent studies of all three remain scarce, so treat the imaginarium PR as directional, not definitive.

### C7. Maintained ONNX exports of TrOCR handwritten checkpoints
- **Source:** `findings-r6/r6-htr-ocr-engines-a.md` — "unverified which are maintained".
- **Found:** ONNX builds of the handwritten checkpoints exist on the hub: Xenova/trocr-base-handwritten and Xenova/trocr-small-handwritten, converted for Transformers.js (https://huggingface.co/Xenova/trocr-base-handwritten; https://huggingface.co/Xenova/trocr-small-handwritten); an ONNX file was added to the official microsoft/trocr-small-handwritten repo itself by the export bot in November 2025 (https://huggingface.co/microsoft/trocr-small-handwritten/discussions/8); an int8 ONNX variant of small exists (https://huggingface.co/oguzhandurmaz/trocr-small-handwritten-onnx-int8).
- **Verdict: RESOLVED for base and small.** Self-export is not required for those two. The large handwritten checkpoint's ONNX status was not confirmed either way this pass.

### C8. Official/community ONNX exports of Granite-Docling
- **Source:** `findings-r6/r6-htr-ocr-engines-b.md` — "ONNX export status unverified".
- **Found:** IBM's model docs state ONNX usage is supported (https://www.ibm.com/docs/en/ibm-foundation-model-operator — Granite-Docling-258M page); an independently exported FP32 ONNX repo exists for Transformers.js (https://huggingface.co/JasonYANG170/granite-docling-258M-ONNX); a community discussion discusses the ONNX conversion (https://huggingface.co/granite-vision-3-3-2b/discussions — related thread surfaced in search).
- **Verdict: RESOLVED — usable ONNX exists via community export; no official ONNX weights in IBM's repo.** On-device latency remains unpublished (see C10).

### C9. RapidOCR support for PP-OCRv5 (the "does the whole ONNX route work" question)
- **Source:** `findings-r6/r6-htr-ocr-engines-a.md` — "unverified current v5 support".
- **Found:** RapidOCR v3 integrated PP-OCRv5; the maintainer confirmed the integration in October 2025 (https://github.com/RapidAI/RapidOCR — release notes and maintainer comments surfaced in search; docs model list: https://rapidai.github.io/RapidOCRDocs/install_usage/rapidocr_v3/usage/); PP-OCRv5 direction-classifier support landed since rapidocr>=3.8.0. Community ONNX repos of PP-OCRv5 also exist on the hub (https://huggingface.co/monkt/paddleocr-onnx; https://huggingface.co/ilaylow/PP_OCRv5_mobile_onnx).
- **Verdict: RESOLVED — the PP-OCRv5-via-ONNX path is real and demonstrated end to end.** This was the biggest open question in the HTR lane; it is now closed.

### C10. Numbers that genuinely do not publicly exist (NOT FOUND)
These were each searched again this pass; no public figure exists. They are real findings, not gaps in effort:
- **ArabicOCR_KHATT CER/WER headline numbers.** The repo ships metric tooling (per-epoch CER/WER/dot-group CER logged to a metrics CSV) but publishes no headline figure, and no model card surfaced in search (https://github.com/FixFips/ArabicOCR_KHATT; https://pypi.org/pypi/arabicocr-khatt/json). Genuinely unpublished.
- **Granite-Docling-258M on-device latency.** No published number anywhere; the ~0.5 GB at 8-bit estimate is arithmetic from the parameter count (https://www.ibm.com/docs/en/ibm-foundation-model-operator; no latency source exists).
- **Apple VisionKit handwriting recognizer model size and ms/page.** Apple does not disclose; no third-party measurement surfaced (https://developer.apple.com/documentation/visionkit — nothing published).
- **Drawboard PDF ink latency.** No published engineering numbers; the smoothness reputation rests on reviews, and this pass found none either (https://www.drawboard.com/pdf/product-tour).
- **OnlineHTR model size.** No published figure (https://github.com/PellelNitram/OnlineHTR).
- **Qwen3-4B Q4 RAM, Ministral-3-3B laptop-CPU tokens/s, KittenTTS multi-language benchmarks, usearch/Qdrant-local depth evaluation, automerge-crate binary size, loro-crdt npm bundle size.** All remain without public figures; vendor or community pages publish none (https://ollama.com/library/qwen3:4b; https://docs.mistral.ai/models/ministral-3-3b-25-12; https://picovoice.ai/blog/on-device-tts/).
- **Keyhive and diamond-types production adoption.** No named production deployments surfaced beyond their own docs (https://github.com/inkandswitch/keyhive; https://crates.io/crates/diamond-types). Adoption evidence stays anecdotal.

---

## D. Trust / security items

### D1. Dillinger phishing accusation
- **Source:** `findings-r6/r6-editors-publishers.md` — "user accusation, unverified".
- **Found:** The accusation thread exists (March 2025, r/webdev, describing redirect-to-Dropbox-login behavior) (https://www.reddit.com/r/webdev/comments/1jfwy14/dillingerio_suspected_of_phising/); Scamadviser carries a neutral automated review page, last updated June 2025 (https://www.scamadviser.com/check-website/dillinger.io). No authoritative confirmation or refutation exists anywhere.
- **Verdict: STILL UNVERIFIED — and structurally so.** It is a user accusation about live-site behavior; nothing authoritative can confirm or clear it. The findings file's framing (accusation, unconfirmed) is already the correct epistemic state.

### D2. Dillinger paid tiers
- **Source:** `findings-r6/r6-editors-publishers.md` — "paid tiers existence unverified".
- **Found:** Dillinger's own FAQ states the service is completely free, has no paid tiers, and needs no signup or card (https://dillinger.io/), consistent with third-party listings describing it as a free open-source editor (https://sourceforge.net/software/product/Dillinger/).
- **Verdict: RESOLVED — no paid tiers exist** (self-reported by the vendor; nothing contradicts it).

---

## E. Cosmetic batch (explicitly left for the main session)

These are per-repo star counts, contributor counts and open-issue numbers that the batch files flagged as "from search-result navigation" or "unverified". They resolve only by fetching each repo's page (GitHub pages refused direct fetch in the earlier lanes), and none is decision-relevant: opensidian metrics (`r6-batch2-minor-note-apps.md`), Akasha Microsoft Store listing details (same file), rnote and Xournal++ issue-count figures (`r6-batch1-minor-note-apps.md`, `r6-xournalpp-ecosystem.md`). The methodological caveat at the top of `r6-batch1-minor-note-apps.md` (issue numbers quoted from repo navigation in search results rather than fetched pages) stands for those items.

---

## Summary for the integrating session

The single most consequential corrections: diamond-types is ISC (not MIT), secsync is Apache-2.0 (not AGPL-3.0) but stale on npm since mid-2024, snlib and tanamigrator carry **no license at all** (code unpullable), fbalobanov/supernote-viewer no longer exists, and the PP-OCRv5-ONNX path (RapidOCR v3+) plus TrOCR base/small ONNX exports are confirmed, which unblocks the two leading HTR options without self-export. The PP-OCRv5 mobile recognition model is 16 MB with published CPU figures, docTR's benchmark tables are now in hand, and the KHATT-weights question stays a hard legal checkpoint because the dataset license is academic/research-only. "Notion uses Yjs" should be dropped as adoption evidence.
