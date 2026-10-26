# Embedded components research, lane 1: documents, PDF, canvas, media, engines

Scope: open-source applications evaluated as EMBEDDED components inside a local-first notes app (Rust desktop target assumed). Sources: official sites, GitHub repos, license files. Every claim carries an inline URL; anything not confirmed from a primary source is marked UNVERIFIED.

---

## 1. ONLYOFFICE (documents)

**What it is.** An office suite: text document, spreadsheet, presentation and PDF editors. Two relevant distributions: ONLYOFFICE Document Server (a self-hosted server rendering the editors in a browser, https://github.com/ONLYOFFICE/DocumentServer) and ONLYOFFICE Desktop Editors (a desktop client, https://github.com/ONLYOFFICE/DesktopEditors). The actual editing core is sdkjs, a JavaScript editor engine (https://github.com/ONLYOFFICE/sdkjs), and the desktop app is essentially a shell that hosts that web core locally.

**License.** AGPL-3.0 across Document Server Community Edition and sdkjs (https://www.onlyoffice.com/license-faq). Notably it carries additional terms under Section 7: the original product logo must be retained and ONLYOFFICE trademarks may not be used (https://github.com/ONLYOFFICE). Commercial "Developer" editions exist for those the AGPL does not suit (https://guides.onlyoffice.com/faq/docs-enterprise.aspx).

**Embedding architecture.** The supported path is network embedding: Document Server runs (typically in Docker) and is embedded into a host web page via an iframe with a JavaScript/JavaScript API and postMessage-based configuration and events (https://www.api.onlyoffice.com/). The official connector ecosystem (Nextcloud, Moodle, Odoo, WordPress etc.) is all built on this same iframe/API architecture (https://www.onlyoffice.com/blog/2026/07/integration-ecosystem). The desktop path exists inside the project itself: Desktop Editors packages the sdkjs web core into a local app (https://github.com/ONLYOFFICE/DesktopEditors), which proves the "editor core in a local webview" model works, but the project does not publish that as a reusable component API; a third-party integration example doing iframe + postMessage bridging is https://github.com/milio48/bedoffice.

**Prior art.** Nextcloud, Moodle, Odoo, WordPress connectors (https://www.onlyoffice.com/blog/2026/07/integration-ecosystem); the Desktop Editors app itself.

**Assessment (Rust/local-first).** Two realistic shapes: (a) sidecar Document Server embedded via WebView/iframe; the AGPL then applies to the combination exposed to users, so the notes app would need to be AGPL-compatible or buy a commercial license (https://www.onlyoffice.com/license-faq); (b) bundling the sdkjs web core in a webview, mirroring Desktop Editors. Technical weight L; license weight is the real blocker for a non-AGPL app. "Best-in-class office editing for free" is realistic only if the host accepts AGPL; otherwise fantasy.

---

## 2. Sterling PDF

**What it is.** "Stirling PDF" (Stirling-Tools/Stirling-PDF) is a self-hosted PDF manipulation platform: merge, split, OCR, sign, redact, convert, compress, watermark, plus a desktop client for Windows/macOS/Linux and a browser UI (https://github.com/Stirling-Tools/stirling-pdf, https://docs.stirlingpdf.com/). Written mainly in Java, ~93k stars. So: a PDF toolbox/editor web service, not a lightweight PDF component.

**License.** Open-core. The LICENSE file licenses most of the tree as MIT but assigns named directories (e.g. `frontend/src/editor/proprietary/`) to a proprietary "Stirling PDF User License" (https://github.com/Stirling-Tools/Stirling-PDF/blob/main/LICENSE). The project describes itself as dual-licensed, "AGPL-3.0 for public source" in its own README marketing terms (https://github.com/Opensource-PDF-Editor/Stirling-PDF), and a maintainer-side discussion states the essentials (conversion, editing, watermarking, redaction, password protection) remain free/MIT for self-hosting and business use, while paid "Team/Enterprise" features moved to proprietary terms in v1.0.0 (https://github.com/Stirling-Tools/Stirling-PDF/discussions/4332). One secondary audit describes the repo as MIT with proprietary folders including engine/ and the desktop frontend, and notes GitHub flags the license as unrecognised (https://www.mrtechking.com/stirling-pdf-github/).

**Embedding architecture.** There is no component library or SDK. Embedding options are: (a) run it (Docker or desktop client) and point a webview/iframe at its UI; (b) file-level integration against its private/local API (https://github.com/Stirling-Tools/stirling-pdf). No WASM build, no headless library documented (UNVERIFIED beyond the above).

**Prior art.** None found as an embedded component; it is deployed standalone (https://docs.stirlingpdf.com/).

**Assessment (Rust/local-first).** Realistic as a sidecar service or file-level API integration (weight S–M) rather than an embedded view. For a truly local-first app, beware: the platform is a Java server (heavy) and the prettiest editing UI lives in proprietary folders. File-level only verdict; embedding the UI is possible but drags the proprietary-terms folders or the whole open-core arrangement in.

---

## 3. Excalidraw (canvas/diagram)

**What it is.** A hand-drawn-style whiteboard/diagramming canvas (https://github.com/excalidraw/excalidraw), distributed as an npm package for direct embedding (https://www.npmjs.com/package/@excalidraw/excalidraw).

**License.** MIT (https://www.npmjs.com/package/@excalidraw/excalidraw).

**Embedding architecture.** Best-in-class: `@excalidraw/excalidraw` exports the whole editor as a React component; you install it and render it in any React app, with an `EXCALIDRAW_ASSET_PATH` for self-hosted assets (https://docs.excalidraw.com/docs/@excalidraw/excalidraw/integration, https://www.npmjs.com/package/@excalidraw/excalidraw). Data model (elements/JSON) is documented, so persistence into a notes app's storage is straightforward. Runs inside any webview (Electron, Tauri) since it is plain React + canvas.

**Prior art.** Official VS Code extension embeds the component in a webview (vscode-excalidraw, https://marketplace.visualstudio.com/items?itemName=excalidraw.excalidraw); Obsidian's popular Excalidraw plugin embeds the same component inside the Obsidian app (https://github.com/zsviczian/obsidian-excalidraw-plugin).

**Assessment (Rust/local-first).** The unambiguous win of this whole list. In a Tauri/Electron-based notes app with a webview, it is a drop-in MIT-licensed embedded canvas. Weight S–M. No realistic downside; permissive license imposes only MIT attribution.

---

## 4. VLC (media playback) / libVLC

**What it is.** VLC media player and, more importantly for embedding, libVLC: the engine extracted as an embeddable multimedia framework (https://github.com/videolan/vlc).

**License.** The VLC player is GPLv2+; libVLC is deliberately licensed LGPLv2.1+ so third-party applications (including closed-source ones) can embed the engine without adopting the GPL (https://github.com/videolan/vlc, https://videolan.videolan.me/vlc/master/libvlc.html, https://www.videolan.org/press/lgpl-libvlc.html).

**Embedding architecture.** libVLC exposes a C API (https://videolan.videolan.me/vlc/master/libvlc.html) designed for embedding playback into applications; official bindings exist for C++, Python, Java, Objective-C and C# (https://videolan.videolan.me/vlc/master/libvlc.html). It supports render callbacks for outputting video into a host-provided surface/window, which is exactly what an embedded player widget needs (https://wiki.videolan.org/LibVLC). License practicality: distributing libVLC is allowed under LGPL terms (https://vlc-user-documentation.readthedocs.io/en/latest/support/faq/legalconcerns.html); note codec patents: some codecs bundled with VLC are patented and may require royalties (https://vlc-user-documentation.readthedocs.io/en/latest/support/faq/legalconcerns.html).

**Prior art.** libVLC's own positioning is as the media engine of third-party apps, and the VideoLAN docs/FAQ state non-GPL and closed-source apps legally embed it under LGPL (https://wiki.videolan.org/LibVLC, https://vlc-user-documentation.readthedocs.io/en/latest/support/faq/legalconcerns.html). (Named commercial embedders not individually verified here: UNVERIFIED.)

**Assessment (Rust/local-first).** Realistic and proven model: link/dlopen libVLC from Rust via FFI (community bindings exist; e.g. `vlc-rs`, UNVERIFIED as maintained), render into a child window or texture. Weight M (FFI + window interop + binary distribution size ~100MB+ UNVERIFIED). This is the mainstream way to embed playback; alternatives (mpv/libmpv, LGPL too) exist outside this list's scope.

---

## 5. Audacity (audio editing)

**What it is.** The best-known open-source multi-track audio editor, in the middle of a large 4.x rewrite (https://github.com/audacity/audacity).

**License.** GPLv3 for the project as a whole today; most code files are GPLv2-or-laster with exceptions in /au3/lib-src and VST3 code (https://github.com/audacity/audacity, https://en.wikipedia.org/wiki/Audacity_(audio_editor)). Historically distributed as GPLv2 (https://manual.audacityteam.org/man/license.html).

**Embedding architecture.** Effectively none. There is no library, no SDK, no WASM build, no headless mode. The only automation surface is `mod-script-pipe`, an optional plugin that lets an external Python/Perl script drive a running Audacity instance over named pipes (https://manual.audacityteam.org/man/scripting.html); wrappers like PyAudacity explicitly require Audacity to be open, "there is no headless mode" (https://pypi.org/project/PyAudacity/).

**Prior art.** Scripting integrations only (https://github.com/unfor19/audacity-scripting, https://manual.audacityteam.org/man/scripting.html). No known app embeds it as a component.

**Assessment (Rust/local-first).** Verdict: file-level only (launch externally, optionally drive via script pipes). Embedding its UI is fantasy; embedding its DSP would mean a hard fork into a library the project does not maintain as one, at XL effort and with GPL obligations. If a notes app needs waveform editing, the honest answer is purpose-built DSP crates, not Audacity.

---

## 6. OBS Studio (recording/streaming)

**What it is.** OBS Studio: screen recording and live-streaming studio, plus `libobs`, the C core library underneath it (https://github.com/obsproject/obs-studio).

**License.** GPL-2.0-or-later, confirmed in the COPYING file and libobs headers ("either version 2 ... or (at your option) any later version") (https://github.com/obsproject/obs-studio/blob/master/COPYING, https://obsproject.com/forum/threads/obs-license-inquiry.58557/).

**Embedding architecture.** libobs IS the embeddable architecture: it is a full rendering/compositing/encoding core that hosts plugins, and a plugin that links with OBS Studio falls under GPL-2.0+ (https://obsproject.com/forum/threads/forum-resource-and-ip-policy.178569/). Embedding libobs in your own app is possible but makes your app a GPL-2.0+ derivative; Streamlabs did exactly this with obs-studio-node, a Node/Electron binding to libobs released under GPLv2 (https://github.com/stream-labs/obs-studio-node/blob/staging/LICENSE), and commercial embedding without source disclosure has produced license-infringement disputes (https://obsproject.com/forum/threads/obs-license-infringement.141405/).

**Prior art.** Streamlabs Desktop via obs-studio-node (https://github.com/stream-labs/obs-studio-node); the lowkey.gg dispute above.

**Assessment (Rust/local-first).** For a notes app's "record a screencast note" feature, libobs is a very heavy hammer (compositing engine, scenes, streaming). Realistic paths: (a) embed libobs as a separate GPL-licensed helper process and keep the notes app's own code out of the GPL boundary, (b) use OS-level capture APIs (ScreenCaptureKit/AVFoundation on macOS, etc.) instead. Embedding libobs in-process into a non-GPL Rust app is a license violation, not an option (https://obsproject.com/forum/threads/obs-license-infringement.141405/). Weight L–XL for path (a), S for using OS APIs. Verdict: headless/helper only; embedded-view = fantasy for a non-GPL host.

---

## 7. Image editor: GIMP vs Krita vs Photopea

**GIMP.** GNU Image Manipulation Program; GPL-3.0 since 3.0 (https://www.cgchannel.com/2025/03/gimp-3-0-is-out/). Extension model: Script-Fu and Python-Fu plugins against the Procedure Database; Script-Fu is an embedded interpreter in each plugin, and ScriptFu has an eval hook other languages can call (https://developer.gimp.org/resource/script-fu/programmers-reference/, https://developer.gimp.org/resource/script-fu/scriptfu-tools/). GIMP 3 exposes a library API (libgimp 3.0 API reference exists, https://developer.gimp.org/api/3.0/libgimp/), and it supports non-interactive/batch runs from the terminal (https://exifinjector.com/blog/gimp-batch-processing). But there is no embeddable widget/UID-surface for another app's window; no known prior art embedding the editor UI. Verdict: headless/file-level only (batch conversions, thumbnails, scripted effects) as an external process; GPL-3 obligations attach to any distributed linking. Weight M for headless, XL for anything more.

**Krita.** Painting app under KDE; GPL (project states the extension API is an integral part of Krita licensed under the GNU GPL) (https://krita.org/en/about/license/); repo https://github.com/KDE/krita. Extension model: C++ and Python plugins; distributing a Krita Python plugin requires GPL (https://scripting.krita.org/lessons/plugin-submission, https://docs.krita.org/en/user_manual/python_scripting/krita_python_plugin_howto.html). Plugin docs explicitly note a Python plugin "can do everything that Krita can do" (https://docs.krita.org/en/user_manual/python_scripting/install_custom_python_plugin.html) — inside Krita, not inside your app. No embeddable view, no headless library documented (UNVERIFIED beyond this). Prior art: none as embedded component. Verdict: file-level/external process only. Weight M–L.

**Photopea.** NOT open source. It is a free, ad-supported browser-based Photoshop-like editor whose source is proprietary; the GitHub repo is for issues only (https://github.com/photopea/photopea, https://en.wikipedia.org/wiki/Photopea, https://www.reddit.com/r/photopea/comments/1mulkwk/open_and_friendly_software/). It does have a real embedding surface: an iframe + postMessage scripting API used to drive it from a host page (https://github.com/yikuansun/PhotopeaAPI, https://github.com/yankooliveira/sd-webui-photopea-embed/blob/main/README.md, and live scripting docs referenced as https://www.photopea.com/api/live in community discussion, https://www.reddit.com/r/photopea/comments/t4wx7p/scripting_and_json_configuration_file_instant/). There is also a corporate self-hostable version (https://en.wikipedia.org/wiki/Photopea). Verdict: not embeddable as open source; the iframe embed means your "local-first" app calls a remote closed service with user files, which contradicts the product premise unless the corporate self-host option is purchased. Weight S technically, but disqualifying on principles for a privacy-first app.

**Overall recommendation among the three:** none is a good embedded component. If the notes app needs inline image annotation, build a small purpose-built canvas (or reuse Excalidraw); if it needs pro-grade raster editing, integrate GIMP or Krita as external "Edit in..." hand-off. Photopea drops out on license/privacy grounds.

---

## 8. Godot (2D/3D engine)

**What it is.** The Godot game engine (https://github.com/godotengine/godot).

**License.** MIT, explicitly permissive with no royalties (https://godotengine.org/license/, https://docs.godotengine.org/en/stable/about/faq.html).

**Embedding architecture.** Historically the engine runs games, not "engine as a library", but the situation is now concrete: headless server builds are officially documented for dedicated-server export (https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_dedicated_servers.html); LibGodot, an API to embed Godot as a library, is being mainlined in a sponsored PR (https://github.com/godotengine/godot/pull/110863); meanwhile migueldeicaza/libgodot is a maintained fork "modified to be embeddable as a library" powering SwiftGodotKit (https://github.com/migueldeicaza/libgodot), and react-native-godot embeds the engine into React Native apps under MIT (https://github.com/borndotcom/react-native-godot). GDExtension is the standard native-plugin mechanism for engine-side code.

**Prior art.** SwiftGodotKit (macOS/iOS embedding, https://github.com/migueldeicaza/libgodot), react-native-godot (https://github.com/borndotcom/react-native-godot), the LibGodot mainline effort (https://github.com/godotengine/godot/pull/110863).

**Assessment (Rust/local-first).** For a notes app, Godot only makes sense if there are interactive 2D/3D widgets (e.g. a 3D scene note). Because the license is MIT there is no license friction at all; the friction is engineering: embedding the runtime (via the libgodot fork or the mainline PR once merged) and rendering its surface into the app's window. Weight M–L. The Godot *editor* embedded as a component is fantasy; the *runtime* embedded is realistic and precedented.

---

## 9. Blender (3D)

**What it is.** The 3D creation suite (https://www.blender.org/about/license/).

**License.** GPL-2.0-or-later for Blender's own code; some modules more permissive (Cycles renderer is Apache-2.0) (https://www.blender.org/about/license/). Add-ons that call the Blender API are treated as GPL (https://blenderartists.org/t/addons-licence-and-python-modules/1169606).

**Embedding architecture.** No embeddable UI. The real mechanism is `bpy`: an official pip-installable Python module exposing Blender as a library for pipelines, web services and research (https://pypi.org/project/bpy/, https://developer.blender.org/docs/handbook/building_blender/python_module/). Headless rendering via `bpy` or `blender -b` is a solved pattern; `blenderless` wraps it for headless servers (https://github.com/oqton/blenderless, https://pypi.org/project/blenderless/). Cycles rendering is fully scriptable headlessly.

**Prior art.** Studio pipelines and web services built on bpy (https://pypi.org/project/bpy/); blenderless (https://github.com/oqton/blenderless).

**Assessment (Rust/local-first).** Realistic: a sidecar Python process (or Blender binary) using bpy for thumbnailing, converting, or rendering 3D assets referenced by notes; the GPL boundary is cleanest as a separate process (https://www.blender.org/about/license/). Embedding Blender's viewport/editing UI into a notes app is fantasy. Weight M for headless rendering, L–XL if you build real 3D features on bpy.

---

## 10. Kdenlive (video editing)

**What it is.** KDE's non-linear video editor, built on the MLT framework and KDE/Qt (https://github.com/KDE/kdenlive).

**License.** GPL-3.0-or-later as a whole (some parts GPL-2.0-or-later; source files carry `GPL-3.0-only OR LicenseRef-KDE-Accepted-GPL` headers) (https://www.opensourcefeed.org/software/kdenlive/, https://github.com/KDE/kdenlive/blob/master/src/mltconnection.cpp).

**Embedding architecture.** Kdenlive the application: no embeddable view, no headless library (UNVERIFIED beyond repo docs). The important distinction is the layer beneath it: **MLT Multimedia Framework** (https://github.com/mltframework/mlt) is the video editing/playback engine Kdenlive and Shotcut are built on, and MLT is licensed **LGPL-2.1** for the framework and client libraries (GPLv2 only for the standalone melt/melted applications) (https://www.mltframework.org/docs/copyrightpolicy/, https://github.com/mltframework/mlt). So the embeddable piece is MLT (C API, playlists/producers/consumers), not Kdenlive's editor UI.

**Prior art.** Shotcut, a full editor built directly on MLT (https://github.com/mltframework/mlt); Kdenlive itself.

**Assessment (Rust/local-first).** Embedding Kdenlive's UI: fantasy (XL). Using MLT via FFI as the engine for a "video note" playback/trim/convert feature: realistic, LGPL-friendly, weight M (plus binary size and codec patent considerations, as with libVLC). If video features are needed, target MLT (or ffmpeg-based crates) rather than Kdenlive.

---

## Comparison table

| Component | License | Embeddability | Realistic integration weight |
|---|---|---|---|
| ONLYOFFICE (documents) | AGPL-3.0 + s7 terms (https://www.onlyoffice.com/license-faq) | Embedded-view (iframe/WebView of Document Server or sdkjs core) | L (license is the blocker unless AGPL-compatible or commercial) |
| Sterling PDF | Open-core: MIT essentials + proprietary folders (https://github.com/Stirling-Tools/Stirling-PDF/blob/main/LICENSE) | File-level only (sidecar service/API); webview embed possible | S–M (API) / L (UI embed) |
| Excalidraw | MIT (https://www.npmjs.com/package/@excalidraw/excalidraw) | Embedded-view (React component in webview) | S |
| VLC / libVLC | libVLC LGPL-2.1+ (player GPL-2.0+) (https://videolan.videolan.me/vlc/master/libvlc.html) | Embedded-view via libVLC render callbacks / FFI | M |
| Audacity | GPLv3 (https://github.com/audacity/audacity) | File-level only (mod-script-pipe drives running GUI) | M (poor value) |
| OBS Studio | GPL-2.0+ (https://github.com/obsproject/obs-studio/blob/master/COPYING) | Headless/helper only (libobs; GPL infects in-process embedding) | L–XL (libobs) / S (OS capture APIs instead) |
| GIMP | GPL-3.0 (https://www.cgchannel.com/2025/03/gimp-3-0-is-out/) | File-level/headless only (batch, Script-Fu eval) | M (headless) / XL (anything UI) |
| Krita | GPL (https://krita.org/en/about/license/) | File-level/external process only | M–L |
| Photopea | Proprietary/closed source (https://github.com/photopea/photopea) | Embedded-view only via remote iframe API (privacy-hostile) | S technically; disqualified for local-first |
| Godot | MIT (https://godotengine.org/license/) | Embedded-view of runtime (libgodot) or headless | M–L (editor embed = fantasy) |
| Blender | GPL-2.0+ (Cycles Apache-2.0) (https://www.blender.org/about/license/) | Headless only (bpy module / `blender -b`) | M (render pipeline) |
| Kdenlive | GPL-3.0-or-later (https://www.opensourcefeed.org/software/kdenlive/) | File-level for Kdenlive; embedded engine via MLT (LGPL-2.1) | M (MLT) / XL (UI) |

## Bottom line for a Rust/local-first notes app

Clean wins: Excalidraw (S, MIT, embeds directly), libVLC (M, LGPL) and MLT (M, LGPL) as engine-level FFI for media, bpy/Blender (M, headless sidecar) and GIMP headless (M) for file-level processing. Possible but licensing-dependent: ONLYOFFICE (only with AGPL-compat or commercial license) and libobs (only as a GPL-licensed separate helper). Non-starters as embedded components: Audacity, Kdenlive UI, Krita/GIMP UI, Photopea (non-free + remote service).
