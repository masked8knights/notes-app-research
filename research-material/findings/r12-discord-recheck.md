# R12 round 4 — Discord re-check (2026-10-28)

Task (todo 48): re-read all Discord exports in research-material/ against current findings; list every app, repo, feature request, or complaint with no findings coverage; research the gaps.

Sources re-read in full:
- discord-transcript-all-threads.txt (4,749 lines; thread onenote_obsidian_evernote_notion, 2026-10-12 through 2026-10-25)
- discord-thread3-transcript.txt (81 messages, Notion thread, through 2026-10-27)
- discord-thread3-links.txt (23 links)
- discord-parsed-messages.json / discord-thread3-parsed.json (raw parsed copies; member-name files stay gitignored per R1 policy)
- discord-export-goodnotes-amphi-noteshelf.html / discord-export-onenote-obsidian-evernote-notion.html (raw HTML)

Method: every app, repo, link, feature request and complaint extracted during the full re-read was cross-checked against research-material/findings/ by name (grep over all findings files) before being declared a gap. Coverage was far better than the raw link count suggested; most Discord items were digested in rounds 1-2 and re-verified in rounds 2-3. The genuine gaps are below.

## 1. Coverage verdicts (already covered, no action)

- HelixNotes, Amphi, Ideon, Poznote, Tangent Notes, Thymer (incl. markdown mirror), Proofeditor, Dillinger, Homebrewery, Ghost, Craft, Trilium, Anytype (incl. the "opensourcing/anytwo" claim, filed UNVERIFIED in community-digest), AFFiNE, Obsidian plugin cluster, notebook-navigator, obsidian-numerals, InkedMark, badges/list-callouts/sheets-extended plugin names, syncthing+tailscale vault sync, diktafon, marmalade-tts-android, e-journal, opensidian (jpzk and thiagovasconcelosti fork), open-note, ObbyNotes, AlienTechSoftware/notecraft, joshmaster2165/Notecraft, NoteCraft (base44, a member), Pele-as-app, OwlLuna, CapsuleCraft, cheeterdev/notes, nexlore, Meridian-Notes, BasScript, MyScriptJS, xnotes-android, sawt, onenote_parser crate, OfficeIMO OneNote.Markdown/Html, malleable-software essay, monogr.ph spec, openalternative.co, Canva (as whiteboard reference), the community essays on Samsung Notes, Squid and FOSS on iPad, Goodnotes Android-port failure, p2panda, bb plugin ecosystem (excluded R13).
- monogr.ph v5 spec: linked-apps-2.md already carries the pasted spec text; the export's pasted copy matches it. r12-confirm-8 line 44 flags the live URL as STILL-UNVERIFIED; content-level verification from the pasted copy stands.

## 2. Gaps found — apps/repos with no findings coverage, researched this round

### 2.1 zennotes (new row, UNVERIFIED-which-project)
Discord (a member of the main thread, one line: "zennotes", no URL). Same-named projects found: ZenNotes (github.com/adibhanna/zennotes), keyboard-first local Markdown notes with Vim motions, MCP server for note search, Go-based self-host option, MIT; also a React-Native zennotes by chixdollar (Monorepo SaaS, ~3 stars); also Zen Notes Android (com.zennotesapp, offline, ~500 downloads). Which one a member meant cannot be verified. Row added to APPS-LINKS.md for the adibhanna project with the caveat; others noted UNVERIFIED in the row's findings pointer.

### 2.2 Macro Docs (new row)
Surfaced via openalternative.co/alternatives/notion embed in the main thread (one member); the embed's other names (AppFlowy, AFFiNE) were already covered, Macro Docs was not. Researched: Macro Docs is macro.com/documents, AGPL-3.0, an open-source "Notion and Google Docs and Obsidian" hybrid; Rust backend, SolidJS frontend, docs isolated in Durable Objects, local-first edits. New row in APPS-LINKS.md under Open-source notes apps and engines.

## 3. Gaps found — still-unverified items resolved by this round

### 3.1 Pele the Mermaid renderer (resolves r12-confirm-8 "Pele Mermaid STILL-UNVERIFIED")
Confirmed: Pele is a new Mermaid diagram renderer for Obsidian written by kepano (MIT). Release notes claim 100-500x faster rendering than mermaid.js and a 230 kB gzipped bundle vs mermaid.js's ~1.6 MB, no dependencies, compatibility with Mermaid 12.1.0 syntax. Shipped in Obsidian 1.15.0 desktop early access (announced Oct 22, 2026). Obsidian's own renderer, not a third-party app; filed as an Obsidian-capability line in the round-4 findings and a supplement to the Obsidian rows' findings pointers (no new row: part of Obsidian).

### 3.2 capsuleos / CapsuleCraft identity (resolves r12-confirm-5 "capsuleos repo/renamed status STILL-UNVERIFIED")
Discord re-read adds the missing context: a Discord member posted github.com/kostyk348/CapsuleCraft on 2026-10-23 ("Remade my project to Egui") and again 2026-10-25, plus rationale for .eml storage ("I find .eml more powerful and easy to use than .md" [paraphrase of the in-thread rationale, 2026-10-25]). This matches r12-enrich-f's v1.8.0 finding (Egui shell, pure-MIME .eml, implementation repo kostyk348/CapsuleCraft, releases also visible via kobaltgit/capsuleos). Conclusion: capsuleos is the earlier name/repo, renamed CapsuleCraft around v1.5; kobaltgit is the collaborator account behind the release-hosting repo. Both still-unverified flags now carry this resolution pointer.

### 3.3 NoteCraft (AlienTechSoftware/notecraft) update beyond earlier v0.0.3-era claims
Discord (a member, 2026-10-26) pointed at the releases page: v0.0.6 alpha shipped the .one OneNote importer (PR #6), implemented with the OfficeIMO library (MIT) for OneNote parsing, revision-store read via the project's own notecraft-onenote crate. Right-to-left text half-done; storage in dual HTML and Markdown; MCP server for AI-assisted editing; builds unsigned, dual MIT/Apache-2.0 license. Supplements github-repos-1 and r12-enrich-f (which stop at v0.0.3). No new row; existing notecraft rows' findings pointers gain this file.

### 3.4 joshmaster2165/Notecraft re-checked
Discord re-read did not surface new claims beyond r12-enrich-f's coverage (61/67 OneNote parity table, .one import with ink/password sections/page versions/AI). Confirmed covered.

## 4. Gaps found — feature requests / complaints with no findings coverage (wants-evidence)

### 4.1 a third member's NoteCraft suggestions (2026-10-25, main thread)
Against a desktop OneNote-reimplementation prototype: two-finger trackpad panning needed (mouse-only navigation blocks him), pen/stylus support, tab spacing between notes ("like OneNote sections"), zoom anchored at pointer. Directional evidence: a OneNote-parity clone without trackpad two-finger panning or pen input fails the tablet/stylus users it exists for.

### 4.2 a student member's student workflow list (2026-10-25, main thread)
Student using OneNote for university: wants PDF printouts (scanned lecture notes) as page background for handwriting over them; automatic shape recognition when drawing over the scan; lasso selection; OneNote-style section tabs for per-course notebooks; stylus-eraser-end switching (pen end writes, eraser end erases, no tool toggle); and argues a file format should follow usage, with infinite-canvas for handwriting and markdown files for plain notes. Directional evidence for: background-PDF handwriting over scans, shape recognition, lasso, section tabs, eraser-end input switching, and the canvas-vs-file split by content type.

### 4.3 OneNote infinity page + Linux clone demand (main thread)
a third member: the OneNote infinity page ("desperately need [it]"). User ".": wants a version of Windows OneNote that works on Linux. Both already implicit in earlier rounds' OneNote complaints; the infinity-page demand and an explicit Linux-clone want were not filed anywhere and are now.

### 4.4 another member's Obsidian-gap wants list (main thread, 2026-10-16/18/23)
Long-time Obsidian power user listing plugin-papering gaps: Workflowy-like performance at scale for the core editor; nested-yaml properties/queries and Bases-style views done properly; vaults-as-contexts with partition and joining (work one vault, merge later); folder notes and folder aliases; virtual notes/views; JSON micro-snippets with the meta_bind plugin as the nearest existing thing; emoji color highlights; the badges and list-callouts plugins; the excalidraw integration rated better than Excalidraw itself in feel; the obsidian-bases virtual-notes gap called out by name; grid/merged-cell tables (pandoc grid_tables, sheets-extended plugin); inline SVG; URL embedding. Directional evidence: an Obsidian successor must treat nesting, queries, folder-notes, embedded-objects and performance-at-scale as core, not plugins.

### 4.5 Meridian-Notes (the Meridian-Notes author's app) community-update details (main thread, 2026-10-13/16/21)
Newer than r12-enrich-f's snapshot: inline calculator in notes, split views, context menu via Ctrl+K, Lua scripts for extensibility (distinct from Rust plugins), layout state kept in a per-vault folder, performance target 600 MHz-class hardware, and a community vote on naming the app ONYX Notes. Supplements the Meridian-Notes rows' findings pointers.

### 4.6 one member's demand (main thread, 2026-10-14)
Notes should be fully searchable incl. images, voice, video, handwriting, on device; linked ente as the reference implementation. community-digest covers the demand; the ente-as-reference pointer added here.

## 5. Out-of-scope observations (R13 scope, recorded not researched)

- ollama vs llama.cpp and Qwen 3.6:35b local-model debate (one member et al., 2026-10-24): local-model runtime tooling, excluded per R13 (standalone llama.cpp rows removed); the app's own vendored whisper.cpp/llama.cpp feature remains filed per R13's exception.
- Swift-for-Android tooling feasibility claims (the goodnotes-thread member): dev-tooling context for Android strategy, not a notetaking app; recorded here as a pointer only.
- gitea.com/one member/workflow-playbook: a playbook document link, not an app.

## 6. Bottom line

Coverage check over all exports: 55 distinct apps/repos named across the Discord material; 53 already had findings coverage from rounds 1-3; 2 new rows this round (zennotes, Macro Docs); 3 still-unverified flags resolved (Pele renderer, capsuleos identity, NoteCraft v0.0.6); 6 wants/complaint clusters newly filed (4.1-4.6). Findings pointers updated in APPS-LINKS.md for rows whose findings gained supplements (notecraft, CapsuleCraft, Meridian-Notes, Pele/Obsidian, monogr.ph-adjacent).
