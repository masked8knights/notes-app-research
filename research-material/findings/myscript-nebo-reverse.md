# MyScript / Nebo: reverse-engineered & reimplemented technology — deep dive

Lane file for the notes-app research project. Scope: what exists in the wild that
reverse-engineers, reimplements, or openly documents MyScript/Nebo handwriting
tech, and what can legally and practically be pulled from it into a local-first
notes app. Every claim carries its source URL. Date of research: 2026-10-26.

---

## 1. MyScript/MyScriptJS — what MyScript publishes openly

- The repo is now **archived**: MyScript discontinued its ready-to-use Web
  components in favor of iinkJS. https://github.com/MyScript/MyScriptJS
- What it contains: signal capture for all devices, digital ink rendering,
  rich editing gestures, import/export, styling, typeset support, 200+
  math symbols, 65 languages — for text and math recognition.
  https://github.com/MyScript/MyScriptJS
- **The recognition itself is not in the repo.** Every sample is configured
  with an applicationKey + HMAC key pointing at MyScript Cloud; the README
  requires a developer account and the free monthly quota from
  developer.myscript.com. https://github.com/MyScript/MyScriptJS
- The license on MyScriptJS is Apache 2.0 — but that covers only the
  client-side capture/render/editing/transport glue, not the engine.
  https://github.com/MyScript/MyScriptJS
- Key point for us: the open repo is a **client + protocol showcase**. It
  documents (by example) the wire contract: stroke data goes up, JIIX
  (JSON Ink Interchange) + export types (TEXT, HTML, MathML, LaTeX, SVG…)
  come back over REST or WebSocket to hosts like webdemoapi.myscript.com.
  Example: https://github.com/MyScript/MyScriptJS/blob/master/examples/v4/websocket_text_iink.html
- MyScript's own docs describe MyScript Cloud as an HTTP/WebSocket
  recognition PaaS. https://developer.myscript.com/doc/interactive-ink/4.1/web/overview/introduction/
  and the older WebSocket-only API docs:
  https://developer.myscript.com/doc/interactive-ink/3.2/web/websockets/architecture/

## 2. github.com/langergitanu/MyScript — what it actually is

- It is **not a fork and not decompiled code**: it is a written-up
  reverse-engineering *findings document* produced by running apktool + jadx
  on the Nebo Android APK (`com.myscript.nebo`, base + split arm64 +
  xxhdpi), ~31,045 classes. https://github.com/langergitanu/MyScript
- Maintainer: the GitHub account langergitanu, who is building a tablet
  note-taking app ("ThunderNotes") and analyzing competitor apps in a
  series (sibling repo: SamsungNotes analysis).
  https://github.com/langergitanu/MyScript ,
  https://github.com/langergitanu/SamsungNotes ,
  https://github.com/langergitanu/ThunderNotes
- Its verdict, which matters more than any speculation we could do:
  Nebo is a thin Java/SWIG layer over a proprietary native engine. All hard
  algorithms (handwriting, equation, reflow, shape/gesture, prediction) live
  in C++ `.so` libs (libMyScriptEngine, libMyScriptText, libMyScriptMath,
  libMyScriptShape, libMyScriptGesture, libNebo, …) — "best architecture
  donor so far; useless as an algorithm donor." Explicit conclusion: no
  Ghidra work justified. https://github.com/langergitanu/MyScript
- Recognition model files ship in the APK as iink `.res` bundles
  (`math-ak.res`, `math-grm-standard.res`, `gek-standard.res`,
  `shk-diagram.res`, `ank-*.res`) plus `conf/{math,gesture,diagram,
  raw-content}.conf` — proprietary, not reusable.
  https://github.com/langergitanu/MyScript
- No license is displayed on the findings repo, and it contains no Nebo
  source or binary artifacts — just descriptions of the architecture. That
  keeps it on the safer side of reverse-engineering commentary (describing
  an API surface is widely considered lawful; redistributing decompiled
  code would not be). https://github.com/langergitanu/MyScript

## 3. PellelNitram/xournalpp_htr — HTR for Xournal++

- Project by Martin Lellep (solo, University of Edinburgh compute), GPL-2.0,
  building on-device handwriting recognition for Xournal++.
  https://github.com/PellelNitram/xournalpp_htr ,
  https://lellep.xyz/xournalpp_htr/
- **It does not use MyScript at all.** It is its own PyTorch stack, built on
  Harald Scheidl's open work (SimpleHTR, WordDetectorNN, HTRPipeline) plus
  an online (stroke-dynamics) model following Carbune et al. 2020 (Google).
  Companion repo: https://github.com/PellelNitram/OnlineHTR
- Explicitly privacy-focused and local: "no open-source, privacy-focused
  handwriting app does [this] — until now", processing data locally.
  https://lellep.xyz/xournalpp_htr/
- Design was socialized with the Xournal++ community up front (issue #4932,
  2023; earlier thread issue #2152, 2020):
  https://github.com/xournalpp/xournalpp/issues/4932 ,
  https://github.com/xournalpp/xournalpp/issues/2152
- Status: has a HuggingFace online demo and install/usage docs; it is a
  research-grade pipeline (line segmentation + offline CRNN/CTC + a newer
  online model), not a production engine — Hacker News discussion (2024)
  covers the offline-vs-online tradeoff.
  https://github.com/PellelNitram/xournalpp_htr ,
  https://news.ycombinator.com/item?id=41147504

## 4. github.com/orgs/MyScript — open vs proprietary

- 18 public repos, essentially all of them **examples, wrappers or
  discontinued web components**, never an engine:
  https://github.com/orgs/MyScript/repositories
  - MyScriptJS (archived), iinkJS (frozen 2024), web components
    (myscript-text-web / myscript-math-web, frozen 2021), Web Integration
    Samples (Apache-2.0): https://github.com/orgs/MyScript/repositories
  - interactive-ink-examples-{android,ios,windows-uwp,wpf}: reference UI
    implementations around the iink SDK, "Other" license
    https://github.com/MyScript/interactive-ink-examples-ios
  - interactive-ink-packages-ios: Swift Package *pointer* to the SDK
    binaries; geogebra-mirror; panzoom (MIT).
    https://github.com/orgs/MyScript/repositories
- The actual iink SDK (engine, `.res` models) is distributed as licensed
  binaries via developer.myscript.com / NuGet / Maven, quote-priced per OEM;
  the org's GitHub never carries it. NuGet profile:
  https://www.nuget.org/profiles/MyScript ; SDK positioning:
  https://www.myscript.com/sdk/

## 5. The wider field — other reverse-engineering / reimplementation evidence

- **Nebo `.bink` stroke format**: Xournal++ issue #5730 (2024) on Nebo file
  support concludes the interesting strokes live inside binary `.bink`
  files that would need reverse-engineering, or reading via the MyScript
  SDK with a developer account. No public .bink parser found — this is an
  open, unclaimed target. https://github.com/xournalpp/xournalpp/issues/5730
- **Cloud protocol**: not captured/leaked, but *officially documented*.
  The V3/V4 REST + WebSocket APIs were public and used by the Apache-2.0
  open-source JS clients; the current iinkJS/Cloud contract (JIIX export)
  is likewise documented. So an open "protocol client" is legal to write;
  what it talks to (quota'd, keyed cloud) is the practical limit.
  https://developer.myscript.com/doc/interactive-ink/3.2/web/websockets/architecture/ ,
  https://github.com/MyScript/MyScriptJS/blob/master/examples/v4/websocket_text_iink.html
- **Engine reimplementations**: found no open reimplementation of MyScript's
  text/math engine (no decompilation projects, no Ghidra/IDA writeups of
  libMyScript*). The only serious native-binary analysis in the field is the
  langergitanu writeup above, which explicitly stopped at the Java layer.
  https://github.com/langergitanu/MyScript
- **Xournal++ itself**: ships a small built-in recognizer historically
  (originally based on cellwriter's work) but the community effort for real
  HTR is the PellelNitram project. https://github.com/xournalpp/xournalpp/issues/2152
- **RNote** (Rust/GTK4, flxzt): has **no handwriting recognition at all**
  today — no built-in HTR, no plugin path; requests exist but nothing
  shipped. So there is no "RNote approach" to borrow, only an integration
  gap. https://github.com/flxzt/rnote ,
  https://rnote.flxzt.net/
- **Legal takedowns**: searched for MyScript DMCA notices / repo removals
  and found none. MyScript's public posture is licensing-by-quote rather
  than visible enforcement against analysis writeups; absence of takedowns
  is not absence of rights (their engine is patented/proprietary — "20
  years of research" is their own claim). https://www.myscript.com/sdk/

## 6. Pull-from assessment (artifact → what's liftable → legal posture)

| Artifact | Liftable | Legal posture |
| --- | --- | --- |
| MyScriptJS / iinkJS clients (Apache-2.0) | Ink capture, pressure/pointer handling, gesture handling, editor state machine, JIIX export rendering — all client-side code, genuinely reusable | Clean: Apache-2.0 code is redistributable with attribution; but it contains no recognition |
| MyScript Cloud protocol (documented REST/WS + JIIX) | The *interface shape*: incremental stroke up → partial recognition down → JIIX + MathML/LaTeX export; a local engine could expose the same contract | Writing a client is legal; *using* MyScript Cloud needs keys/quota and ToS acceptance. Mimicking the API shape for our own engine is standard clean-room practice |
| langergitanu/MyScript findings | Architecture patterns only: engine facade layering (document/page/reco/display controllers), string-keyed tool/palette properties, ExportOptions + MIME model, reflow rejection callbacks, ContentProvider clipboard ingress | The writeup is descriptive; adopting *patterns* (API layering, callback naming) is not copyright infringement. Do not copy decompiled code, and do not redistribute `.res` models or native libs |
| Nebo APK `.res` models, native `.so` | Nothing — this is the crown-jewel IP | Max legal risk: copyrighted binaries, likely patents on recognition methods. Distribution = infringement; reverse-engineering for interop may be lawful in some jurisdictions but redistribution is not |
| Nebo `.bink` format | Format spec if someone cracks it (import of Nebo notes into our app) | Interop reimplementation of a file format is comparatively defensible; nobody has published one yet |
| xournalpp_htr + OnlineHTR (GPL-2.0) | Actual working on-device HTR: models + pipeline; proof that a solo dev can get useful accuracy | GPL-2.0 is *copyleft*: fine to use if our notes app is GPL-compatible; infectious if we want a permissive-licensed app. Models trained on IAM/own data — check each model's provenance before shipping |
| RNote | Nothing recognition-wise (it has none); useful as ink-model/UI reference only | MPL-2.0-ish per project; clean |

**Bottom line on MyScript itself:** the reverse-engineering evidence is
unanimous — the recognizers are unreachable proprietary native code. What
can legally be pulled is (a) the Apache-2.0 client-side ink/editor/gesture
code, (b) the documented protocol/JIIX interface shape to reimplement
against our own engine, and (c) architectural patterns from the Nebo
analysis. The algorithms and models are off the table.

## 7. Alternatives anchor (comparison, not full re-derivation)

The reverse-engineering route has to be judged against the free on-device
paths that need no MyScript at all:

- **Google ML Kit Digital Ink Recognition**: free, on-device, 300+
  languages via downloadable classifiers, Android/iOS; the practical
  default for an Android-first notes app. https://developers.google.com/ml-kit/vision/digital-ink-recognition
- **Apple PencilKit** (stroke/shape/gesture intelligence + handwriting
  recognition surfaced via VisionKit / Live Text on-device): free on
  Apple platforms, but Apple-ecosystem-locked.
  https://developer.apple.com/documentation/pencilkit
- These cover text recognition well; MyScript's remaining edge is
  interactive ink (typeset/reflow as you write), math, and diagrams — which
  is exactly the part reverse-engineering cannot reach (native, per §2).
  The open-source alternative at parity-of-spirit is xournalpp_htr (§3).
  https://github.com/langergitanu/MyScript

## Verdict for the notes app

1. Pull: MyScriptJS's Apache-2.0 client pieces (capture/gestures/JIIX
   rendering) and its interface contract as a design target.
2. Do not pull: anything from the Nebo APK — no `.so`, no `.res`, no
   decompiled code, no assets.
3. Reimplement against: the documented REST/WS + JIIX shape with our own
   local engine (or ML Kit / xournalpp_htr models as the pluggable backends).
4. Watch: Nebo `.bink` format (open interop target, no published parser yet:
   https://github.com/xournalpp/xournalpp/issues/5730).
