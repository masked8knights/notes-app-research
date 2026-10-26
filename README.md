# notes-app-research

Research phase of a project to build a new notes app: Rust-native, local-first,
handwriting-first, zero-knowledge. Nothing is being built yet; this repository
holds the research only, accumulated across repeated full-depth passes (R1-R6).

## What is here

- `RESEARCH.md` — the running synthesis: what the research found, thread by
  thread and round by round, with a pointer to the findings file behind every
  claim.
- `APPS-LINKS.md` — the master inventory: every app and repository mentioned in
  the source material, one entry each, with open-source status and where
  functionality can be pulled from.
- `FEATURES.md` — the master feature list: everything people said they want,
  grouped, with per-round synthesis at the end.
- `research-material/` — raw inputs and findings. `findings/` holds one file per
  research lane (~70 files); the original source exports and parsed transcripts
  are gitignored.
- `MILESTONES.md` — chronological round log. `todo.md` — task state.
  `REQUIREMENTS.md` — stated requirements. `LEARNINGS.md` — durable lessons.

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

## Reading order

`RESEARCH.md` is the entry point. `FEATURES.md` answers "what do people want";
`APPS-LINKS.md` answers "what exists and what can we borrow". Findings files in
`research-material/findings/` hold the cited evidence.

## Status

Research only. No build plan has been written and none is planned until the
project owner asks for one.
