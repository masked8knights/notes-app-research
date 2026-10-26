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
