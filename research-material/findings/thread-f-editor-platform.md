# Thread F — Editor cores, desktop shell, and embedded app blocks

Lane owner: Thread F of the notes-app research project. Method: web research only (docs, issue trackers, blog/field reports, security writeups). Everything below is sourced; thin or single-anecdote claims are marked UNVERIFIED. No usernames, handles, or machine details are recorded.

---

## 1. Block-editor cores: can they host a canvas-plus-document hybrid?

The brief's demand is specific: **the same block instances live free on an infinite canvas AND inside a linear note, with no format conversion between the two modes.** None of the mainstream editor cores was designed for this. The reference point for what "designed for it" looks like is BlockSuite; everyone else is being bent.

### ProseMirror

The document model is a block tree with positions as paths through the tree, and positions are DOM-relative in the standard view. A 2026 writeup on the ProseMirror forum describes the most serious attempt to bend it: keep ProseMirror's model, transactions, state and plugin architecture intact, and replace the entire DOM view layer with a custom canvas renderer (project "LumenPage", for paginated documents). The authors report the hard parts explicitly: mapping document positions to canvas coordinates and back, rebuilding selection/cursor/hit-testing without the DOM, custom clipboard/drag-drop/input bridges via a hidden textarea (IME composition feedback still incomplete), and screen-reader accessibility named as "probably the hardest unresolved problem" — the ProseMirror author himself confirmed accessibility and touch as the structural risks of any non-DOM view. ([discuss.prosemirror.net thread](https://discuss.prosemirror.net/t/building-a-canvas-based-editor-on-top-of-prosemirror-s-state-and-plugin-system/8982))

- **Bendability: model yes, view no.** ProseMirror's state/plugin layer survives a canvas view; the view layer must be fully rewritten, and freeform positioning (absolutely-positioned draggable node views) has been done at toy scale ([forum, 2019 draggable/absolute-positioning thread](https://discuss.prosemirror.net/t/newbie-question-about-draggable-and-absolute-positioning/2330)) but nobody has shipped the full canvas+doc duality.
- **Verdict for the hybrid:** viable only with a two-renderer architecture (DOM renderer for the linear note, custom canvas renderer over the same model/state), at the cost of duplicating everything the DOM view gave for free: selection, IME, clipboard, a11y, plugins that touch the view.

### TipTap

TipTap is a wrapper over ProseMirror, so it inherits everything above — but it also has the strongest *proven* bridge to a real canvas: **tldraw uses TipTap as its rich-text engine**, storing shape text as TipTap JSON ([tldraw rich-text docs](https://tldraw.dev/sdk-features/rich-text)); tldraw re-exports TipTap's extension surface so custom rich-text extensions don't load a second ProseMirror ([tldraw PR](https://github.com/tldraw/tldraw/pull/10691)); and a community gist demonstrates the inverse embedding — a `tldraw` TipTap node that mounts the full canvas inside a TipTap document ([gist by a tldraw core contributor](https://gist.github.com/steveruizok/0a2466ad3c5adeb998756f5386c3267a)).

- **Bendability: highest demonstrated in both directions** (canvas-inside-doc and doc-inside-canvas). What tldraw does *not* do is make the same blocks simultaneously addressable as canvas shapes and as document children; the embed is a block owning a canvas scene, not a shared block tree.
- **Verdict:** best core if the hybrid is "canvas blocks embedded in notes and note-embedded text editing inside a canvas app" (embedded-canvas model). Weakest if the brief insists on one block tree with two views — that's a ProseMirror-model problem TipTap doesn't solve either.

### Lexical (Meta)

Lexical's model is a DOM-adjacent element tree with a reconciler; there is **no canvas mode and no evidence of anyone building one**. Searches for Lexical canvas/whiteboard work return only adjacent patterns: a Lexical-based editor shipping Excalidraw **whiteboard blocks** as embedded components ([haklex release notes](https://github.com/Innei/haklex/releases/tag/v0.50.1)), and a planning issue for a canvas runtime that lists ProseMirror/Lexical/TipTap vs a minimal contenteditable as candidate engines for inline text on a canvas, i.e. canvas teams choosing an editor, not Lexical hosting a canvas ([BWB-135 issue](https://github.com/blixis-io/wp-blocks/issues/207)). Known weak spot: deeply nested block structures have historically been fragile in Lexical integrations (Payload CMS nested-block issues, e.g. [#3531](https://github.com/payloadcms/payload/issues/3531)).

- **Bendability: UNVERIFIED at depth — no public attempt at a Lexical canvas view was found.** Its headless design (core/renderer split) makes a canvas renderer theoretically possible, but the plugin ecosystem for custom views is far thinner than ProseMirror's, so the bend would be solo work.
- **Verdict: not the pick** for a canvas-first hybrid; fine as a note editor with embedded-canvas blocks.

### BlockSuite (AFFiNE) — the control case

BlockSuite is the one framework built for exactly the pattern in the brief, and its docs state the design directly: **edgeless documents are isomorphic to page documents — both are block trees, with no data conversion during mode switching** ([BlockSuite edgeless data structure](https://blocksuite.io/components/editors/edgeless-data-structure)). The same Y.Doc holds the data; PageEditor and EdgelessEditor are two views that attach and detach from it ([BlockSuite overview](https://github.com/toeverything/blocksuite), [architecture guide](https://docs.affine.pro/blocksuite-wip/architecture)). AFFiNE claims this separation lets it render thousands of vector shapes and text blocks at 60 FPS without DOM-heavy lag ([AFFiNE blog](https://affine.pro/blog/interactive-whiteboard-app)).

- **Evidence it works:** AFFiNE ships doc+whiteboard+databases as views of one underlying store, with edgeless mode as the bridge ([Better Stack guide](https://betterstack.com/community/guides/linux/affine/)).
- **Costs:** much smaller ecosystem than ProseMirror/TipTap/Lexical; the framework is young, API churn is real, and teams adopting it inherit AFFiNE's product opinions. DeepWiki's architecture notes describe a store→model→view data flow that is closer to a game engine than to an editor library.
- **Verdict: the only core where the brief's requirement is the default behavior.** Trade ecosystem breadth for the duality being native.

### Canvas cores (tldraw, Excalidraw) used as the foundation

Both prove the embedding direction into file-based apps: Excalidraw's Obsidian plugin stores drawings as files in the vault, embeds them in markdown, and links notes to and from drawings ([Obsidian plugin page](https://community.obsidian.md/plugins/obsidian-excalidraw-plugin)); a lighter plugin even stores scenes inside fenced code blocks in notes ([CanvasDraw plugin page](https://community.obsidian.md/plugins/canvas-draw)). tldraw ships an embed library and a custom-shape system for embedding generated content and HTML ([tldraw docs](https://tldraw.dev/docs/ai)). But a canvas core adopted as the *whole* app's foundation gives you a drawing tool with text in shapes, not a block-based note system; note→canvas is not a first-class concept in either.

### Comparison summary

| Core | Canvas+doc duality | Evidence of people trying | Distance to goal |
|---|---|---|---|
| ProseMirror | None native | Full canvas-view rewrite (LumenPage) | Large: rewrite view layer + a11y + IME |
| TipTap | None native, but tldraw bridge both ways | tldraw rich text; tldraw-in-TipTap node | Medium: embedded-canvas model is shippable today |
| Lexical | None native | Only canvas-in-editor blocks (haklex) | Large + unexplored |
| BlockSuite | Native (isomorphic page/edgeless trees) | It *is* the attempt (AFFiNE) | Smallest; cost is ecosystem and API stability |
| tldraw / Excalidraw | Inverted (notes-in-canvas only) | Obsidian plugin, embed shapes | Wrong direction as sole core |

**Recommendation to carry forward:** either BlockSuite as core (native duality, smaller ecosystem) or TipTap with an embedded-canvas block type (largest ecosystem, duality by composition rather than by model). The ProseMirror canvas-rewrite path is a multi-quarter project whose hardest cost is accessibility, per the framework author's own assessment.

---

## 2. Shell: Tauri vs Electron vs native

### Numbers (real-world, 2025–2026)

| Metric | Tauri v2 | Electron | Source |
|---|---|---|---|
| Bundle size (benchmark, same app) | 8.6 MiB | 244 MiB | [Hopp benchmark](https://www.gethopp.app/blog/tauri-vs-electron) |
| Memory, 6 windows (benchmark) | ~172 MB | ~409 MB | [Hopp benchmark](https://www.gethopp.app/blog/tauri-vs-electron) |
| Bundle size (typical ranges) | 2–10 MB | 80–250 MB | [buildmvpfast](https://www.buildmvpfast.com/blog/tauri-v2-vs-electron-desktop-apps-2026), [devtoolpicks](https://devtoolpicks.com/blog/tauri-vs-electron-indie-hackers-2026) |
| Idle RAM (typical ranges) | ~30–80 MB | ~120–400 MB | [rustify 2026](https://rustify.rs/articles/rust-tauri-vs-electron-2026), [pkgpulse](https://www.pkgpulse.com/guides/electron-vs-tauri-2026) |
| Cold startup | ~200–500 ms | ~1–2 s | [tech-insider 2026](https://tech-insider.org/tauri-vs-electron-2026/) (vendor-adjacent, treat as approximate) |
| Build time (first build) | ~81 s (Rust compile) | ~16 s | [Hopp benchmark](https://www.gethopp.app/blog/tauri-vs-electron) |

The Hopp benchmark is N=1 on a MacBook but is the cleanest apples-to-apples measurement found; the ranges across sources agree in shape (Tauri roughly 5× smaller and 2–4× lighter at idle, faster to start, slower to build). Startup deltas under ~1.5 s were judged immaterial by the Hopp authors for most apps.

### Can Tauri's webview carry a heavy canvas app?

The honest answer from field reports: **on Windows and macOS, mostly yes; on Linux, it is the known weak platform, and macOS WKWebView has its own jank class.**

- Linux/WebKitGTK: canvas FPS collapses relative to Chromium in the same code ([tauri issue #5761](https://github.com/tauri-apps/tauri/issues/5761)); heavy DOM workloads lag/freeze ([#3988](https://github.com/tauri-apps/tauri/issues/3988)); canvas+CSS filters fall off the GPU path ([#4891](https://github.com/tauri-apps/tauri/issues/4891)). Workarounds documented by Tauri itself include disabling the DMABUF renderer (at the cost of the fast path) or disabling accelerated compositing entirely as a last resort ([Tauri Linux graphics docs](https://v2.tauri.app/develop/debug/linux-graphics/)). Community consensus is that Linux is the poor-performing platform ([linuxquestions thread](https://www.reddit.com/r/linuxquestions/comments/1acbjru/how_improve_gtk_webview_performance_for_tauri_apps/)).
- macOS/WKWebView: WebGL/game-style prototypes run at 60 FPS by the counter but exhibit visual jitter not present in Safari ([Babylon.js forum report](https://forum.babylonjs.com/t/performance-between-safari-and-wkwebview-tauri/60811)); developers building graphics editors report being "stuck with WebKit on Mac" as the core problem ([r/tauri thread](https://www.reddit.com/r/tauri/comments/1n46bum/how_performant_is_tauri_when_it_comes_to/)); stale frames after minimize/restore and webview resize bugs are documented ([tauri issue #14843](https://github.com/tauri-apps/tauri/issues/14843), [ui-kit issue tracking the same class](https://github.com/codeatlasdev/ui/issues/662)).
- Windows/WebView2: closest to Chromium; the Excalidraw-Tauri field reports are mostly positive, with cosmetic issues only (a stray WebView2 shutdown line on stderr, [excalidraw-offline-bin issue](https://github.com/gfaurobert/excalidraw-offline-bin/issues/19)). A subtle canvas-performance gap vs Edge was reported but the reporter was unsure it was real ([r/tauri thread](https://www.reddit.com/r/tauri/comments/1jur0hl/canvas_rendering_performance_in_tauri/)).
- Android webview shows roughly half the FPS of Chrome in the same Tauri app ([r/tauri thread](https://www.reddit.com/r/tauri/comments/1rim086/tauri_webview_performance_versus_chrome_on_android/)) — relevant only if a mobile shell is planned.

**Proof of viability:** multiple shipping Tauri wrappers around Excalidraw exist — a full local-first Excalidraw desktop app on macOS ([excalidraw-desktop](https://github.com/ignacioli/excalidraw-desktop)), a cross-platform Tauri Excalidraw app using the OS webview ([quabyt-tech/excalidraw-desktop](https://github.com/quabyt-tech/excalidraw-desktop)), a community Excalidraw desktop built on Tauri ([excalidraw discussion #11216](https://github.com/excalidraw/excalidraw/discussions/11216)), and an example Tauri app embedding the editor as plain ES modules ([excali-rust PR](https://github.com/HutsonLabs/excali-rust/pull/113)). None of these is an infinite-canvas *editor with thousands of live shapes and rich text* at AFFiNE scale, so "Excalidraw runs fine" is evidence for medium-weight canvases only — mark heavy-canvas Tauri fitness as **partially verified**.

### Native (the third option)

A native shell (Swift/AppKit, or Rust+egui/wgpu with a webview only for notes) removes the webview variable entirely and is what the heaviest canvas apps (Figma) ultimately chose. Costs: no shared codebase with the notes layer, and the block-editor ecosystem above is all web-native. For this project — notes-first with canvas blocks, not a 10,000-shape design tool — the web shell remains the rational default; native is the escape hatch if WKWebView/WebKitGTK jank proves disqualifying on the target platforms.

**Shell recommendation:** Tauri if Linux is a second-tier platform (or ship Electron for Linux only); Electron if first-class Linux and worst-case renderer predictability matter more than 200 MB of disk and ~150 MB of RAM. Tauri v2's build-time capability/ACL system (below) is also a genuine security advantage for the embedded-block design in section 3.

---

## 3. Embedded app blocks: terminal, HTTP endpoint, cron — threat model

### Adversary model

The attacker is a **malicious or compromised note**. A notes app with block types that carry executable configuration (commands to run, ports to bind, schedules to fire) turns every imported note, synced workspace, shared template, or pasted markdown into a delivery vehicle. This is not hypothetical: in April 2026 Elastic Security Labs documented a campaign where a crafted Obsidian vault containing a legitimate shell-execution plugin configuration executed attacker commands on vault open, delivering a RAT — no software vulnerability exploited, purely the app's own plugin capability ([Elastic writeup](https://www.elastic.co/security-labs/phantom-in-the-vault), [corroborating report](https://thehackernews.com/2026/04/obsidian-plugin-abuse-delivers.html)). Obsidian's own security page concedes the structural problem: due to technical limitations it cannot reliably restrict plugins to specific permissions, so it relies on a restricted-mode default and review/scorecards ([Obsidian plugin security](https://obsidian.md/help/plugin-security)). A second Obsidian-ecosystem case — an RCE in a popular plugin where note frontmatter flowed unsanitized into a JavaScript evaluator built on `new Function()` — shows the *note-content-to-code-execution* path specifically ([Tasks plugin ADR-002](https://publish.obsidian.md/tasks-contributing/Architecture+Decisions/ADR-002+-+Security+Response+to+JavaScript+Execution+in+Queries)).

Design principle that follows: **capabilities must be granted per block instance, per note, with an explicit trust prompt — never ambient** (never "plugins can do everything", never "a note's blocks inherit the app's powers").

### Block 1: embedded terminal (xterm.js + node-pty)

Capabilities required: a PTY (node-pty or Rust `portable-pty` sidecar), process spawn, filesystem read/write, full network egress by whatever the shell runs.

What a malicious note could do if terminal blocks were ambient:

- **Arbitrary command execution at app privilege.** node-pty launches processes at the parent's permission level; its own documentation warns to containerize when exposed ([node-pty README security note](https://classic.yarnpkg.com/en/package/node-pty)). A note that can *configure* a terminal block's startup command owns the machine — the Elastic campaign above is exactly this shape.
- **Control-character injection through the PTY channel.** PortSwigger's VS Code research showed the byte-level trust model of PTY forwarding breaking via control characters in dragged/config content, escalating to code execution ([PortSwigger research](https://portswigger.net/research/drag-and-pwnd-leverage-ascii-characters-to-exploit-vs-code)). A note app that lets note text flow toward a PTY without a strict boundary repeats this class.
- **Native-module supply-chain and environment bleed.** node-pty helpers have inherited the host's Node `execArgv` preload flags into child helper processes — the embedding app's own privileged preload can re-run in an unintended context ([node-pty issue #974](https://github.com/microsoft/node-pty/issues/974)).

Mitigations if shipped at all: block instance grants the *specific* binary via allowlist (no shell interpolation; argv arrays, never string commands — the standard command-injection defense ([Auth0 guidance](https://auth0.com/blog/preventing-command-injection-attacks-in-node-js-apps/))), per-block PTY scoped to a project directory, no note text ever concatenated into a command, and an explicit one-time "this terminal block runs: <binary> in <dir>" grant.

**Verdict: plugin-only, explicit per-block grant, never core.** A terminal is a deliberate power tool; it should never exist silently in a note a user merely opened.

### Block 2: HTTP endpoint / webhook receiver block

Capabilities required: port binding (loopback or all interfaces), request routing into app logic, often filesystem or command dispatch on receipt.

What a malicious note could do:

- **Bind to all interfaces instead of loopback** — either through a note-supplied config or a port-config UI the note pre-fills — exposing a command-execution or data-egress surface to the whole LAN. Real finding class: a local app whose config allowed rebinding to all interfaces without auth ([reported issue](https://github.com/Rizzo-AI-Academy/rizzo-pii/issues/112)).
- **Drive-by access via CSRF/DNS rebinding.** Any page the user has open in a browser can POST to a tokenless loopback server; Origin/`Sec-Fetch-Site` checks do not stop DNS rebinding, and a rebound host reaches the server as "same-origin". This exact bypass — leading to drive-by command execution on a localhost dev tool — was reported repeatedly in 2026 audits ([example audit](https://github.com/nithiink/yapcode/issues/70), [DNS-rebinding variants](https://github.com/nithiink/yapcode/issues/96)). Defenses: Host-header allowlist, per-launch random token, and binding loopback only.
- **Port squatting/confusion with other localhost services** (a webhook block on a well-known port hijacking traffic meant for another local tool).
- **Exfiltration channel:** a receiver is bidirectional in practice — responses, error messages, and logs can carry vault data out to whatever page reached it.

Mitigations if shipped: loopback-only bind enforced in core (not configurable by the note), per-launch random bearer token injected into the webhook URL, Host/Origin allowlist, size and rate limits, and the block's allowed handlers restricted to a fixed capability set (append-to-note, run-workflow X) rather than arbitrary dispatch.

**Verdict: core-provided primitive with enforced loopback+token+Host invariants, but the *handlers* a webhook may trigger are plugin/per-note grants.** The network invariant is too easy to get wrong per-plugin; the bind itself is safe enough to core-ify only if core refuses any note-supplied bind address or authless mode.

### Block 3: cron scheduler block

Capabilities required: timers/fire schedules, and whatever action it fires (which is where the real power lies — the schedule itself is benign; the payload is everything).

What a malicious note could do:

- **Persistence.** A schedule in a synced note is auto-persistence: reopen the app, the note loads, the block fires. This is the mechanism that made the Obsidian vault campaign work ("executes on vault open" ≈ a trigger the attacker controls, [Elastic](https://www.elastic.co/security-labs/phantom-in-the-vault)).
- **Payload laundering:** schedule fires a benign-looking action (a workflow, a command, a fetch) configured by the note — the scheduler inherits the worst capability of whatever it can trigger.
- **Resource abuse / timing oracles** (lower severity).

Mitigations: schedules are data, and like all note data they are untrusted; the *action* reference must resolve through the same per-block capability grant as everything else; a background job spawned from a note should run under the same restricted context and surface visibly in a "scheduled by this note" UI so audit is possible.

**Verdict: core scheduler (timers are harmless), plugin-or-granted actions (the payload is not).** The dangerous half must never be granted implicitly by a note being open.

### Core vs plugin-only — the case, stated once

**For core:** consistent capability model and audit surface; Tauri v2 makes this tractable because permissions/scopes/capabilities are declared per window and validated at build time, with fs/shell/network denied by default and scopes narrowed to paths ([Tauri security overview](https://v2.tauri.app/security/), [capabilities](https://v2.tauri.app/security/capabilities/)); a strict CSP enforced by the shell blocks injected remote scripts from reaching IPC in the first place ([Tauri CSP docs](https://v2.tauri.app/security/csp/)).

**For plugin-only:** Obsidian's experience shows the alternative — plugins with unrestricted power and only social controls (review, restricted mode) — ends in weaponized vaults ([Obsidian plugin security](https://obsidian.md/help/plugin-security), [Elastic](https://www.elastic.co/security-labs/phantom-in-the-vault)). Electron's own checklist says the same thing in renderer terms: no Node integration in renderers that show remote content, context isolation everywhere, sandboxing, and untrusted content behind a restricted bridge ([Electron security tutorial](https://www.electronjs.org/docs/latest/tutorial/security), [sandbox docs](https://www.electronjs.org/docs/latest/tutorial/sandbox)); note that enabling Node integration in a renderer disables the sandbox for it. If Electron is the shell, all privileged operations (PTY, bind, schedule-dispatch) must live in the main process behind validated IPC, since contextIsolation alone does not stop a compromised renderer if the preload exposes powerful unfiltered functions ([practitioner analysis](https://safeguard.sh/resources/blog/electron-app-security-best-practices)).

**Synthesis: a hybrid.** Core owns the *invariant enforcement* (loopback-only bind, token generation, argv-only process spawn, CSP, sandbox/IPC boundary) and the *grant ledger* (per-note, per-block, explicit, revocable, persisted outside the note so a synced note cannot grant itself anything). Plugins own the *features* (a terminal UI, webhook handlers, scheduled workflows) and can only exercise capabilities that a human granted to that specific block instance. A malicious note can then at worst: create blocks that *request* capabilities and sit inert until a human reads the grant card — and the app must render that request in a way a human can audit (this is the one UI requirement the threat model imposes: grant prompts must be keyed to block identity and shown at open time, not buried in settings).

### Threat model summary (required writeup)

- **Assets:** user files/vault, OS user account, localhost network surface, credentials reachable by the user's shell, app auto-update integrity.
- **Adversary:** attacker who can deliver a note/workspace/template into the app (shared vault, sync, import, paste). Adversary does not need a vulnerability in the app if block capabilities are ambient.
- **Entry points:** note content (markdown, frontmatter, block attributes, embedded JSON), plugin code, synced workspace config, webhook payloads arriving at a bound port.
- **Highest-risk flows:** (1) note-configured command → PTY (terminal block) — mitigated by argv allowlists + per-block grants; (2) drive-by request to a tokenless loopback receiver — mitigated by core-enforced loopback + token + Host allowlist; (3) note-owned schedule as persistence — mitigated by granted-action indirection + visible scheduling UI; (4) note text reaching a JS evaluator — mitigated by never interpreting note data as code (the Tasks-plugin lesson); (5) XSS in a renderer reaching privileged IPC — mitigated by CSP + context isolation + sandbox + minimal bridge (both shells' documented posture).
- **Residual risk:** grant fatigue (users approving prompts without reading); a malicious plugin that is *trusted once* retains power unless grants are revocable per plugin; supply-chain compromise of the embedded-editor/canvas dependency itself. Residual risks are accepted and surfaced, not eliminated.

---

## Bottom line

The canvas-plus-document hybrid with one shared block tree exists in exactly one editor core: BlockSuite, at the price of a small ecosystem. The pragmatic alternative is TipTap (+tldraw) with duality by composition — canvas blocks embedded in notes and TipTap text inside canvas shapes, both directions already demonstrated publicly. ProseMirror supports the hybrid only via a full non-DOM view rewrite whose unsolved cost is accessibility; Lexical has no canvas pathway in evidence at all. For the shell, Tauri gives ~5× smaller bundles (~8.6 MiB vs ~244 MiB) and roughly half the memory (~172 vs ~409 MB in the best benchmark found), and its build-time capability ACL is the right substrate for the embedded-block permission model; the webview risk is concentrated on Linux/WebKitGTK and, secondarily, WKWebView jank on macOS — both reasons some teams keep Electron for Linux. Embedded terminal/webhook/cron blocks are shippable but only under the hybrid grant model: core enforces invariants (loopback-only, tokens, argv-only spawns, CSP/sandbox/IPC boundary) and holds a revocable per-block grant ledger; plugins implement features. The 2026 Obsidian vault campaign is the standing proof that the ambient-capability alternative is not a theoretical risk.

## Open sub-questions

1. Does BlockSuite's page/edgeless isomorphism hold for *user-authored custom block types* (not just AFFiNE's built-ins), and what is the real learning/API-stability cost in 2026? (Needs a BlockSuite deep-dive or prototype; not verifiable from public docs alone.)
2. Where is the actual FPS/memory ceiling of tldraw or a BlockSuite edgeless editor inside WKWebView/WebKitGTK with thousands of live shapes? All evidence found covers medium-weight canvases; a spike benchmark is the only way to close this.
3. Does any cross-platform app ship *two shells* (Tauri on Win/macOS, Electron on Linux) successfully, and what is the maintenance cost? UNVERIFIED — no public case found.
4. Exact grant-UI design: what does a "this note wants to bind a webhook" prompt look like so users actually read it? (UX research, not web research.)
5. Whether Rust-side PTY (portable-pty sidecar) avoids the node-pty class of issues (execArgv inheritance, native-module surface) or merely relocates them.
6. Cron-block semantics: should schedules pause while a note's trust state is unconfirmed after re-import, and what is the UX cost of that?
