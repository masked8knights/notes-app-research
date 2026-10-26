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
