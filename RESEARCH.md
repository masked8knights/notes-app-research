# RESEARCH.md — Notes App Research (Round R2)

Synthesis of Phase 1 research. Raw findings live in `research-material/findings/` (one file per lane, every claim cited there); original sources live in `research-material/`. This file holds the conclusions and the open questions only.

## Sources and lanes

- `research-material/findings/community-digest.md` — feature-request digest of the 1412 Discord messages, grouped by theme, every claim traceable to a message id, no usernames.
- `research-material/findings/github-repos-1.md`, `github-repos-2.md` — 27 GitHub repos investigated (links from the community + the 8 remade.wiki pages' projects).
- `research-material/findings/linked-apps-1.md`, `linked-apps-2.md` — ~58 product/project pages including remade.wiki, monogr.ph spec doc, Obsidian plugins, Ink & Switch essay.
- `research-material/findings/thread-a-sync.md` — Thread A answer (sync/CRDT), includes a measured benchmark (`research-material/benchmarks/thread-a/`).
- `research-material/findings/thread-b-storage.md` — Thread B answer (storage).

Exclusions honored: getbb.app and the whole "bb" plugin ecosystem were dropped from research per user instruction.

## What the community wants (strongest signals)

1. A Rust-native, Electron-free notes app (381 reactions on the opening request).
2. Freeform OneNote-style canvas with freely placed, resizable, layered blocks.
3. Stylus handwriting with pressure, ink-to-shape, palm rejection, stored as plain files.
4. On-device searchable handwriting, stated as the deal-breaker for leaving OneNote.
5. OCR across images/PDFs/voice/video with local ML (ente cited as the model).
6. Markdown-native storage plus Obsidian vault compatibility.
7. Plugin system, graph view, MCP/agent access borrowed from Obsidian's model.
8. Sync via the user's own cloud on plain files; git sync; self-hosting; user-chosen encryption.
9. A Goodnotes-class open-source tablet app (an entire second community channel exists for this).
10. Native Android/iPadOS; skepticism of wrapper ports.
11. Open source is non-negotiable, especially in the handwriting lane.
12. Migration: .one/.onepkg import, 15 years of notes, universal export.
13. Collaboration wanted but feared as the feature "that kills every notes app".
14. Power-user features: inline LaTeX, real tables, shapes/diagrams, RTL/Arabic support.
15. Interface pluralism: user-picked UI (ribbon, file tree, handwriting mode) over one lean shell.

## App landscape patterns

- The stack of the closest siblings is Rust + no webview or Tauri, plain files or block store, Tantivy/SQLite search: CapsuleCraft (.eml capsules + blocks.json, E2EE on roadmap), Meridian-Notes (custom Rust GUI, canvas, ink as SVG), HelixNotes (Tauri, .md, Tantivy, WebDAV), jpzk/opensidian (Tauri v2 vault clone), notecraft (pure Rust OneNote reimplementation with measured feature parity, 61/67).
- AFFiNE is the reference for the canvas↔document duality: blocks carry stable identity with views, so a note can be DocOnly, EdgelessOnly, or both. BlockSuite over Yjs/y-octo.
- E2EE + local-first sells at consumer scale (Anytype, ente, Lockbook). Ente runs on-device CLIP/face models with encrypted synced indexes; the pattern for private universal search inside E2EE.
- Handwriting: MyScript is the commercial moat (66 languages, no RTL); its archived JS SDK and reverse-engineered format repos show lock-in cost. Ink must stay stable-ID vector strokes so HTR can attach later.
- Migration and ink fidelity: ConvertOneNote2MarkDown (766 stars) issues are dominated by lost ink strokes and COM failures; onenote_parser (Rust) exists for .one import.
- Recurring wish across apps: MCP/agent access (three repos added it independently), per-block provenance (Proofeditor), living calculations (obsidian-numerals).
- Remade.wiki wave: open-notebook (40.6k stars, MIT) shows demand scale for revived apps; notecraft (Rust) and CapsuleCraft are early-stage siblings.

## Thread A answer: sync and conflict resolution

Measured (2-core box, scripts in `research-material/benchmarks/thread-a/`): Yjs merged 10,000 concurrently-edited 500-char docs in 0.14 s, 100% converged, ~518 B/update. Automerge 2.0-alpha needed ~1.15 ms/doc and exhausted memory at 10k (Automerge 3, July 2025, targets that). Loro wasm failed to load on Node 22 here (environment problem, flagged). Diamond Types is effectively unmaintained.

Best-evidence answer: hybrid, with CRDTs carrying note content. E2EE CRDT sync is a solved, shipping pattern with client-side merge: relay stores ciphertext plus unencrypted commit hashes/heads so it can plan sync without reading content. Proof: Ink & Switch Keyhive notebook 05 (sedimentree, RIBLT, BeeKEM) and Loro's %ELO protocol (CI-tested Rust↔TS E2EE interop). Ilow Sync ships Loro+AES-GCM for Obsidian vaults. Lockbook proves Rust+E2EE+offline but is file-level, not CRDT. Yjs has no first-party E2EE.

Conflict files don't survive the spec: Obsidian actually defaults to auto-merge, and its forums document silent bad merges and overwritten newer data; conflict frequency scales with offline duration and device count, exactly our scenario. Keep-both remains right only for binary attachments.

Engine pick on current evidence: Loro (first-party E2EE + protocol spec) or Automerge (deepest ecosystem, Beelay pre-1.0). The staffing risk is key agreement and client-side compaction, not the CRDT itself.

## Thread B answer: storage

Every app that needs stable block references converged on a block store with IDs: Trilium (SQLite), Anytype (encrypted blocks), Tana (cloud DB), AFFiNE/BlockSuite (Y.Map block tree), Heptabase, Logseq DB, Ideon (Docker DB). The file-first survivors paid for it: Obsidian pushes all non-content metadata to sidecars; Logseq's blocks-on-lines Markdown was non-portable and produced an unrecoverable data-loss defect, and Logseq's own April 2024 post explains why it abandoned files-as-store (block insert rewrites whole files, no stable IDs) — its promised two-way markdown sync is still unshipped two-plus years later.

The live canvas↔note bridge ships only within one store: Obsidian Canvas (JSON references note files; edits live both ways), Heptabase (card = note), AFFiNE edgeless (same Y.Map). Nobody ships a live two-way bridge across a block-store↔external-folder boundary.

Recommendation: block store as primary; canvas layout as a JSON Canvas-style artifact keyed by block IDs (making the bridge free); guaranteed-lossless export (store JSON + Markdown + .canvas) as the longevity guarantee; a Thymer-style two-way plain-file mirror only if staged (documents first, one-way export first), with Logseq's record as the warning.

## Open questions (next)

1. Threads C–G not yet researched: small local models (C), indexing cost of universal search (D), handwriting/OCR on-device (E), editor/platform guts incl. Tauri vs Electron and embedded-block threat model (F), trust/UX unknowns (G).
2. From Thread A: key-agreement scheme choice (BeeKEM vs alternatives); Lockbook-style conflict behavior documentation.
3. From Thread B: round-trip block-identity encoding for export; mirror conflict policy; whether canvas regions are first-class notes.
4. UNVERIFIED items to re-check later: NicTanghe/BasScript, ThatSheepGuy22/ObbyNotes, an unreachable OfficeIMO fork (handle withheld),gitea sawt, strongcod3r/laplace, Bouquet page, two X posts, one YouTube video, MyScript pricing page (JS shell), OneNote web (JS shell).
5. GitHub push still needs the user's gh auth in WSL or a token in .env (see MILESTONES R1).
