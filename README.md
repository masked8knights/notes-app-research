# notes-app-research

Research phase of a project to build a new notes app: Rust-native, local-first,
handwriting-first, zero-knowledge. Nothing is being built yet; this repository
holds the research only, accumulated across repeated full-depth passes (R1-R9).

## What is here

Research output:

- `RESEARCH.md` — the running synthesis: what the research found, thread by
  thread and round by round, with a pointer to the findings file behind every
  claim.
- `FEATURES.md` — the master feature list: everything people said they want,
  grouped into tables, with the source evidence linked per row.
- `APPS-LINKS.md` — the master inventory: every app and repository mentioned in
  the source material, one table row each, with open-source status, repo or
  features-page link, and where functionality can be pulled from.
- `research-material/` — raw inputs and cited evidence. `findings/` holds one
  file per research lane, including the R8 fact-check verdict tables and the R9
  camoufox sweep; the Discord HTML exports themselves stay untracked.

Project management (separate from the research):

- `project/MILESTONES.md` — chronological round log.
- `project/todo.md` — task state.
- `project/REQUIREMENTS.md` — stated requirements and standing rules.
- `project/PLAYBOOK.md` — the workflow rules the project runs under.

`AGENTS.md` at the root is the bootstrap pointer for any assistant opening the
folder. `checks/` holds the pre-push secret scanner, the only script in the
repository. `BACKUPS/` and `ARCHIVE/` are gitignored working folders.

## What the source material is

Feature requests and app discussions from community threads, plus the project
owner's own notes and research brief. Community content is used strictly as
research input: usernames and identifying details were scrubbed before anything
was committed.

## How the rounds went

- R1-R3: source ingestion, first research pass, master files.
- R4: re-run at greater depth after a coverage audit found the first pass too
  shallow: 30+ repositories, per-app deep dives, integration candidates
  (OnlyOffice, Excalidraw, VLC, and similar), MyScript/Nebo reverse-engineering.
- R5: IdeaCraft, Drawboard PDF, and the study/PDF-textbook landscape.
- R6: full-depth sweep of every remaining inventoried item: 12 findings files,
  a verify pass over every unverified claim, and license corrections throughout.
- R7: exhaustive per-app feature inventories for every inventoried app, an
  internet-wide sentiment sweep, and the Evernote/Notion remake landscape.
- R8: full fact-check of the master files in six parallel verification lanes
  (see `research-material/findings/r8-factcheck-corrections.md`); corrections
  applied to the master files.
- R9: link policy enforced in `APPS-LINKS.md` (repo-only for open source,
  vendor features pages for closed source), a camoufox scrape of 334 URLs that
  turned 71 unverified claims into cited evidence, and a markdown-only cleanup.

## Reading order

`RESEARCH.md` is the entry point. `FEATURES.md` answers "what do people want";
`APPS-LINKS.md` answers "what exists and what can we borrow". Findings files in
`research-material/findings/` hold the cited evidence. Project state lives in
`project/`.

## Status

Research only. No build plan has been written and none is planned until the
project owner asks for one.
