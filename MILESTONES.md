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

### Round R7: per-app inventories, internet-wide sentiment, remake landscape, and the user's 11 repos
Date: 2026-10-27
Did: Six subagent lanes ran after a first attempt lost three of five lanes to a plan limit (relaunched successfully once the window reset): feature-inventory majors (20 apps, 4-app top-up after a cancelled first run), feature-inventory OSS (19 apps), feature-inventory handwriting (19 subjects, completed in the earlier run), internet-wide sentiment sweep (8 ranked demands with 2+ independent sources each), Evernote/Notion remake landscape (33 projects, 17 alive / 13 dead with evidence), and two lanes covering the 11 user-supplied repos (turtl/desktop, Zettlr, QOwnNotes, blinko, edgeever, notion-re, zappynotes, owlistic, NexaNote, memos, siyuan). Seven findings files (~334 KB, ~1,900 lines) written and transferred into research-material/findings/. Master files integrated: APPS-LINKS.md (R7 section: 11 new repo entries plus inventory/remake/sentiment summary lines), FEATURES.md (R7 synthesis), RESEARCH.md (R7 section), todo.md (items 26-28).
Result: The pull-from map gained its two strongest sync/E2EE candidates: SiYuan's dejavu snapshot/provider abstraction with repo-key E2EE (with WebDAV ETag fragility flagged as an anti-pattern) and edgeever's triple-write storage with an offline sync queue. NexaNote contributes the per-point-pressure ink canvas reference. The sentiment sweep independently confirmed the Discord threads' top demands with wider evidence.
Learned: Plan limits can cancel subagent lanes mid-run; a lane file's existence does not prove its content is complete, so every surviving file must be verified against its brief before integration. Small projects researched honestly (notion-re, zappynotes) yield "nothing to lift" verdicts, which are findings, not padding.
Fixed: The cancelled majors lane's incomplete file (sections 1-16 of 20) was completed rather than rewritten, preserving the earlier work.
Next: Phase 2 plan remains deferred per user instruction; no build plan.
Blocked: none.
Status: done

### Round R8: full fact-check of the master files and repo cleanup
Date: 2026-10-27
Did: The user flagged that FEATURES.md's Amphi claims were not true. Six parallel subagent lanes re-verified FEATURES.md against primary sources (official pricing pages, app-store listings, vendor docs, GitHub/package registries), lane by lane: iPad/study apps, PKM majors, canvas/minor apps, OSS repos, integration components, and HTR/sync/AI/Nostr. Root cause of the Amphi error: the Discord thread linked useamphi.com (Amphi Labs LTD, closed-source iPad AI canvas) but findings glued the unrelated open-source repo amphi2024/notes (GPL-3.0-or-later, self-hosted sync) onto it; the two-product split itself was correct. All six lane verdict tables copied into research-material/findings/ as r8-factcheck-lane-1..6, with a summary in r8-factcheck-corrections.md. 25 corrections applied to FEATURES.md, plus APPS-LINKS.md (Amphi pairing fixed, Meridian MIT marked UNVERIFIED) and apps-likes-wants.md (self-hosted-sync praise attributed to Amphi Notes).
Result: Wrong claims corrected in place and marked as fact-check corrections: Goodnotes pricing ($11.99/$35.99 tiers, not $29.99/yr), Evernote 50-note cap (not 51), the 57% negative-review stat marked UNVERIFIED, Obsidian Sync Standard $4/mo vs Plus $96/yr (checkout-default claim dropped), Obsidian plugins ~9,500 (not ~5,000; registry doubled in 2026), the Elastic April 2026 incident (malicious community plugins in shared vaults, not fake app downloads), Tana's current pricing, Tolaria's code size and its Oct 2026 iPhone/iPad client (web client is announced beta only), neo is MIT open source, xnotes' Play signing conflict, Stirling ~94-95k stars, GIMP's GPLv3+ history, Godot LibGodot merged, Muse's wind-down to Allume, nostr crate ~446K downloads/month, and whisper.cpp Android marked UNVERIFIED for the 5x ratio. Items the lanes could not verify were marked UNVERIFIED, never silently filled.
Learned: An honest fact-check pass produces as many "master file was already right" verdicts as corrections; recording those (CapsuleCraft zero-database, notebook-navigator #274, diktafon speech-to-text) is what lets the next session trust the files. Claims resting on package-registry listings rather than the LICENSE file itself must say so.
Fixed: Repo cleanup: the 15 one-off helper scripts in checks/ moved to ARCHIVE/ (checks/ now holds only run-secret-check.sh and its config); FEATURES.md's stale findings path fixed to research-material/findings/; README refreshed with R7/R8 and the findings/ description.
Next: R8 close (secret gate, commit, push). Phase 2 plan remains deferred per user instruction; no build plan. Camoufox UNVERIFIED-filling task remains deferred and resumes only if the user wants it.
Blocked: none.
Status: done

### Round R9: APPS-LINKS.md link policy, camoufox UNVERIFIED sweep, and markdown-only repo
Date: 2026-10-27
Did: Three work items from the user's directive. (1) APPS-LINKS.md reworked to a strict link policy: every open-source project now points at its forge repo only (github.com or equivalent), with remade.wiki project lines collapsed to one-line "Covered by" pointers that keep the original request records (Prosecraft and ScriptCraft kept as explicit no-repo-found records), and closed-source apps point at the vendor's own features or pricing page (Evernote, Notion, Goodnotes, Descript, Heptabase, Kinopio, LiquidText, MarginNote 4, Squid, Thymer). Backup taken before the edits (BACKUPS/APPS-LINKS.md.bak-preR9). (2) A camoufox sweep from WSL scraped 334 URLs (415 UNVERIFIED target lines deduplicated) in a background run: 323 pages ok, 11 documented errors (styluslabs.com and lumafusion SSL, cafebazaar/play.google/sourceforge fetch aborts, three dead blog hosts, lockbook/pricing and smartspark timeouts). The corpus (scraper/r9-corpus.jsonl, not committed) was keyword-matched against the 415 UNVERIFIED lines: 71 high-confidence fill candidates written into research-material/findings/r9-camoufox-sweep.md without rewriting finding lines in place; the three strongest fills were merged by hand into the r7 feature inventories: Notability's third-party pricing page live-confirmed ($99.99/yr Pro tier, 400 AI quizzes/flashcards per month on a lower tier, still third party, not Notability's own page), Stylus Labs' live App Store listing confirmed to make no pressure-sensitivity claim (matching the UNVERIFIED verdict), and LiquidText's official pricing page confirmed the tier structure (Basic / Pro 2023 one-time / LIVE / LIVE Unlimited, one-week LIVE trial, student pricing via in-app upgrade) while dollar figures stay UNVERIFIED because the page publishes amounts only in images. (3) Repo cleanup: the remaining tracked one-off code files (bench.js, discord-thread3-parser.py) moved to ARCHIVE/ and untracked; checks/ holds only the secret gate.
Result: The repo's tracked content is markdown plus raw research data (transcripts, JSON/JSONL outputs of the parsing runs), with run-secret-check.sh the only script. An earlier scripted fill attempt damaged three finding lines (stale line numbers replaced lines wholesale); git diff exposed it and all three lines were restored verbatim with the scraped evidence appended, verified by line read.
Learned: Never apply line-number edits from a targets file generated before later edits to the same file; re-derive line numbers from fresh content at apply time. WSL background jobs need the assistant's own background runner (nohup dies with the launching console); script files beat inline wsl bash -c quoting every time.
Next: Phase 2 plan remains deferred per user instruction ("dont make a build plan just yet"). Remaining UNVERIFIED fills (68 candidates in r9-camoufox-sweep.md) can be merged on request.
Blocked: none.
Status: done
