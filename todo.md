# todo.md

## Active

1. [passed] Phase 0: create project folder ThauraTest with playbook layout; probe toolchain (git 2.53 Windows + WSL Ubuntu, gh 2.46 in WSL).
2. [passed] Phase 1 (start): parse Discord exports into transcripts; save all research material.
3. [passed] Phase 1: digest Discord communities - extract every app, link, and feature request, referencing message IDs.
4. [passed] Phase 1: research every linked GitHub repo and app (subagent sweep) — R2 first pass.
5. [passed] Phase 1: research brief Thread A (sync) and Thread B (storage).
6. [passed] Phase 1: research Threads C-G (local models, indexing cost, handwriting/OCR, editor internals, UX trust).
7. [passed] Phase 1: write RESEARCH.md consolidating all findings with sources.
8. [deferred] Phase 2: decompose into plan — USER SAID NO BUILD PLAN YET. Do not start until asked.
9. [passed] Git repo, secret checker gate, GitHub remote. Repo made PUBLIC on user request.
10. [backlog] Rust build kickoff (blocked behind item 8).
11. [passed] R4 deep re-run lane 1: repos batch A (8 repos) - full features, likes, wants-changed, open-source status, pull-from assessment, linked evidence.
12. [passed] R4 lane 2: repos batch B (10 repos) - same depth.
13. [passed] R4 lane 3: repos batch C (12 repos) - same depth.
14. [passed] R4 lane 4: new Notion thread (thread 3) digest + voice notes/TTS repos (diktafon + v1.1.1, marmalade-tts-android).
15. [passed] R4 lane 5: integration candidates (OnlyOffice, Sterling PDF, Excalidraw, VLC, Audacity, OBS, image editor, Godot, Blender, Kdenlive): license, embedding model, pull-from.
16. [passed] R4 lane 6: MyScript/Nebo reverse-engineering deep dive (MyScriptJS, langergitanu/MyScript, xournalpp_htr, MyScript org, Nebo RE work).
17. [passed] R4 lane 7: per-app deep run on the major apps named in threads (Goodnotes, Notability, NoteShelf, Amphi, Evernote, OneNote, Notion, Obsidian, Miro, Milanote, Anytype, Tana, Reflect, Logseq): features, likes, wants-changed.
18. [passed] R4: integrate lanes into RESEARCH.md, update MILESTONES.md, secret-check gate, commit and push. Pushed as commit 90a003e after gate passed; remote verified clean.

## Status notes

- R4 launched because the user judged R2/R3 not deep enough: "do a proper research run of every app and repo for all of their features and all of the stuff that people like or want changed", track open-source status and where functionality can be pulled from, including reverse-engineered MyScript/Nebo.
- Item 8 explicitly deferred on user instruction: "dont make a build plan just yet".
- Subagent lanes write only to their own findings file in findings/; main session is the only writer of RESEARCH.md, todo.md, MILESTONES.md.
- R4 gate fixes: raw thread-3 exports untracked and gitignored; history scan case fix proven on a scratch file; 15 author-name rules now in the gitignored local rules file; secret-bearing one-shot helper scripts stubbed in checks/.
