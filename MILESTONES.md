# MILESTONES.md

### Round R1: Project setup and source ingestion
Date: 2026-10-27
Did: Created project folder with playbook layout on user's PC. Copied playbook as PLAYBOOK.md. Saved all starting materials into research-material/ (2 Discord HTML exports, product spec, research brief, parsed transcript + JSON). Parsed 1412 Discord messages (1359 in OneNote/Obsidian/Evernote/Notion thread, 53 in Goodnotes/Amphi/NoteShelf thread); extracted 281 unique links, 48 GitHub repos.
Result: Setup complete; parsing complete. Toolchain probed: git 2.53.0 on Windows and in WSL Ubuntu; gh CLI 2.46.0 in WSL; no gh on Windows.
Learned: Discord exports use chatlog__message-container markup; parseable by regex split on data-message-id. GitHub links include a get-bb.app plugin ecosystem and a OneNote-format research repo (AlienTechSoftware/notecraft) that mirrors this project's research intent.
Fixed: Skill base file outside workspace; routed through workspace copy for transfer.
Next: Subagent research sweeps (Discord digest, repo research, app landscape); then Threads A-B; RESEARCH.md; git repo + GitHub remote.
Blocked: GitHub push needs the user's gh auth in WSL or a token added to .env by the user.
Status: done

### Round R2: Research sweep complete (community, repos, apps, Threads A-B)
Date: 2026-10-27
Did: Ran 7 parallel research lanes, all URLs passed inline after the earlier fetch-gate aborts. Community digest of all 1412 Discord messages (themes + message ids, no usernames). 27 GitHub repos and ~58 product pages investigated, including the 8 remade.wiki pages and the monogr.ph spec. Thread A answered with a measured benchmark (Yjs merged 10k concurrently-edited docs in 0.14 s; Automerge 2.0-alpha exhausted memory at 10k). Thread B answered: block store primary + JSON Canvas-style layout artifact + guaranteed-lossless export; two-way file mirror only staged. getbb.app and the "bb" ecosystem dropped per user instruction.
Result: 7 findings files + benchmark artifacts committed under research-material/; RESEARCH.md written with conclusions and open questions.
Learned: fetch-gate rule for subagents: URLs must appear in the task prompt text itself, never only inside files read via bash. Subagents that hit step limits resumed cleanly by task id when told to stop re-searching and write the file from what they had.
Next: Threads C-G research; then Phase 2 plan and user confirmation; git commit + push (blocked on user gh auth or token in .env).
Blocked: GitHub push (same as R1).
Status: done

### Round R2b: GitHub online copy established
Date: 2026-10-27
Did: Ran checks/commit-r2.sh (commit d03e89d, 13 files, 2275 insertions). Secret checker passed over worktree and full history at the publish boundary. Created private GitHub repo notes-app-research via gh in WSL and pushed main (gh was already authenticated in the user's WSL, so no token in .env was needed).
Result: Online copy live and private; future rounds push after each secret check.
Learned: The repo lives on /mnt/c but WSL gh handles it fine; repo made private by default because findings quote community material, user can flip it public.
Next: Threads C-G research lanes; then Phase 2 plan and user confirmation.
Blocked: none
Status: done

### Round R3: Threads C-G answered; Phase 1 research complete
Date: 2026-10-27
Did: Ran 5 parallel lanes (C local models, D indexing cost, E handwriting/OCR, F editor/platform + embedded-block threat model, G trust/UX), each with inline URLs and its own findings file. Wrote the C-G conclusions into RESEARCH.md and expanded the open-questions list to per-thread items. Committed as R3 and pushed after a passing secret check.
Result: All seven research threads from the brief now answered with cited findings; 12 findings files, 1 benchmark. Research phase of Phase 1 is complete.
Learned: Lane isolation held (each subagent touched only its file); the 2026 Obsidian vault RAT campaign grounds the embedded-block threat model; "nobody has published this" turned out to be a recurring honest finding (phone tokens/sec, auto-filing tolerance ceiling, stolen-index threat models). Near-miss fixed: piping the secret checker into tail masked its nonzero exit, so a commit with an all-interfaces bind literal (the IP-pattern hit in thread-f, since reworded to plain wording) got committed locally; caught before push, commit rewritten out of history, checker now always run as a hard gate with no pipes (checks/push-*.sh). Also: .gitignore now covers research-material/authors-local-only.txt (community member names) and checks/commit-*.sh helpers; PowerShell-quoting mangling of long one-liners is fully avoided by writing scripts with device_write and running them with bash.
Next: Phase 2: decompose research into a build plan (MVP / v1 / PLUGIN / LATER per brief deliverables), confirm the todo order with the user before any build work.
Blocked: none
Status: done

### Round R4: Deep re-run of every app and repo; master files; repo public
Date: 2026-10-27
Did: User judged R2/R3 not deep enough and directed a proper re-run: every app and repo with all features, what people like, what they want changed, open-source status, and where functionality can be pulled from, including reverse-engineered MyScript/Nebo. Parsed the third Discord thread (Notion app-requests; 22 messages, 29 links; parser rewritten for this export's unquoted HTML attributes). Researched user-added sources: diktafon (+v1.1.1), marmalade-tts-android, tolaria.md. Ran 10 research lanes (3 deep repo batches covering the full inventory, thread3 digest, integration components, MyScript/Nebo reverse-engineering, per-app likes/wants, tolaria, OneNote-style pen/keyboard/touch auto-switching) plus 2 compiler lanes that built APPS-LINKS.md (217 items in 9 categories) and FEATURES.md (16 apps + 13 repos + 11 integration components + community wish-list synthesis) at repo root, per user request. Made the GitHub repo public on user request.
Result: Findings set grew from 12 to 21 files; two master files at repo root. Repo pushed after a passing secret check.
Learned: A lane that hits the usage limit may still have finished writing its file (deep-repos-c): verify file completeness before relaunching a failed lane. This Discord export uses unquoted HTML attributes, so the earlier quoted-attribute parser silently found 0 messages; always inspect raw markup before parsing a new export format variant.
Next: Keep RESEARCH.md integrated with R4 conclusions. Phase 2 build plan remains deferred on user instruction ("dont make a build plan just yet").
Blocked: none
Status: done

### Round R4b: publish-gate fixes and R4 push
Date: 2026-10-27
Did: Resolved the three problems the push gate raised, then pushed R4. First, the raw thread-3 Discord exports (parsed JSON + transcript) were committed this round and carry community member names; both were untracked and gitignored, matching the R1 policy that research-material/discord* raw files stay local. Second, the history scan's -i flag made DESKTOP-[A-Z0-9]{6} case-insensitive, so the ordinary phrase "desktop-mobile" matched the machine-name pattern; removed -i so history mirrors the case-sensitive worktree scan. Third, thread-3 author names were missing from local-rules.txt; added 12 new author-name rules (names live only in the gitignored rules file), joining the three rules already present from earlier rounds. Scrubbed published files (thread3-digest.md, deep-repos-c.md, APPS-LINKS.md, RESEARCH.md): member names replaced with generic member labels, member-hosted URLs withheld from publication. One-shot helper scripts that embedded member names in their sed patterns were overwritten with clean stubs so the worktree scan passes.
Result: Rules proven to fire: every new rule flagged the raw transcript scan before scrubbing; all tracked files scan clean after. The fixed history rule fires on a scratch file containing the machine-name pattern and passes benign prose. Gate passes; R4 pushed to the public repo with member names absent from worktree and history.
Push evidence: the first amended-push attempt caught four more worktree hits (this milestone entry itself carried the 12 member names until reworded; three helper scripts still held them until stubbed). After those fixes the gate passed and commit 90a003e reached main, followed by fe5edf4 (todo close-out marking R4 lanes 11-18 passed). Remote verified: no machine/user-path patterns in the pushed tree.

### Round R5: new material at full depth (IdeaCraft, Drawboard PDF, the BookCraft study idea)
Date: 2026-10-27
Did: Coverage-audit question answered honestly (inventory complete at R4; depth was tiered: 30 repos and 16 apps deep, smaller links inventory-level, a few member-hosted repos unfindable). Three parallel research lanes on the new material: aamirenic/IdeaCraft, Drawboard PDF, the study/PDF-textbook app landscape behind the BookCraft idea. Findings written to research-material/findings/r5-ideacraft.md, r5-drawboard-pdf.md, r5-study-apps-landscape.md and integrated into APPS-LINKS.md (16 new items), FEATURES.md (R5 section), RESEARCH.md (R5 section), todo.md (items 19-21).
Result: IdeaCraft is a young MIT Rust/Tauri reference (pullable schema, command layer, sync-folder design; no handwriting or mobile). Drawboard is the closed-source inking benchmark, with its own subscription-backlash history as the cautionary lesson. The unified dedicated study notebook over textbooks is a real but contested gap with documented traps (subscriptions, buggy updates, large-PDF performance, sync).
Learned: Namesake repos (rickyb82/ideacraft vs aamirenic/IdeaCraft) need explicit disambiguation in the inventory. A praise quote can name a benchmark whose maker's pricing history is itself a research finding.
Fixed: none needed.
Next: Phase 2 plan still deferred per user instruction; R4/R5 findings feed it when unblocked.
Blocked: none.
Status: done
Learned: A new Discord export's raw outputs (transcript, parsed JSON, links) must be gitignored from the first commit; only the parser script and scrubbed digests belong in the repo. A case-insensitive flag on a pattern anchored to an uppercase identifier turns ordinary prose into hits; history and worktree scans must use the same case rules. Member names added mid-project require re-scanning everything already committed, including tool scripts in checks/.
Fixed: run-secret-check.sh history scan case sensitivity; local-rules.txt (12 new rules); four published files; .gitignore raw-export entries.
Next: Phase 2 plan awaits user go-ahead; no build plan per user instruction.
Blocked: none.
Status: done

### Round R6: full-depth sweep of every remaining inventory item
Date: 2026-10-26
Did: Three waves of parallel subagent lanes (12 total) researched every remaining inventory item at full depth: minor note apps batch 1 (Squid, Concepts, Saber, Workflowy, DEVONthink, ente, Kinopio) and batch 2 (Muse/Allume, Thymer, Ideon, OwlLuna, Akasha, Poznote, Tangent, HelixNotes, Lockbook, Pele, Obsidian Publish, caption tools), editors and publishers (Dillinger, Ghost, Homebrewery, proofeditor, Amphi, Samsung Notes deep dive), the sync/CRDT+E2EE stack (BeeKEM, Loro protocol-e2ee, any-sync, secsync, p2panda; Rust-native yrs, Loro, iroh, automerge core, nostr-sdk), HTR/OCR engines in two files (TrOCR best open HTR; Tesseract disqualified for handwriting; docling, paperless-ngx, OnlineHTR, ArabicOCR_KHATT), the Xournal++/RNote/Supernote ecosystem (Supernote .note format fully reverse-engineered), local AI models (LLM/STT/TTS/RAG plus a pre-ship license checklist), 16 Obsidian plugins license-verified, OSS batch D (jpzk/opensidian identified as the closest existing project to ours), Nostr/transports, and a verify pass over all 34 UNVERIFIED entries. 12 findings files (~540 KB, 3,603 lines) written and transferred into the repo.
Result: Coverage-audit statement closed: every inventoried link now has full-depth research or a documented not-found disposition. APPS-LINKS.md and FEATURES.md carry the R6 sections; RESEARCH.md carries the R6 summary. Licenses corrected: diamond-types ISC, secsync Apache-2.0 (dormant), RNote GPL-3.0-or-later, Xournal++ bare GPL-2.0, snlib and TanaMigrator no-license.
Learned: The pull-from map now has its strongest entries: jpzk/opensidian (Rust+Tauri Obsidian clone), TrOCR (best open HTR), Kinopio's localStorage-first queued-ops pattern, Lockbook's Rust E2EE core, and the reverse-engineered Supernote format. Relay economics and single-identity keys keep Nostr a concepts-only transport.
Fixed: Identifier and Windows-path scan of all 12 findings files run before transfer; clean.
Next: Phase 2 plan remains deferred per user instruction ("dont make a build plan just yet").
Blocked: none.
Status: done
