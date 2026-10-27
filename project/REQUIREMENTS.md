# REQUIREMENTS

## Requirements (user's words, as closely as recordable)

- Go through and do research on every feature of every app mentioned in the shared Discord chats; produce a full report on everything people want in a notes app, from handwriting to real Evernote-like functionality, cross-platform included.
- Look at all GitHub links and apps people mentioned; do real investigations of everything discussed: projects, features, online reviews, issues, feedback, source code, other projects.
- The chats and the pasted spec/brief are sources of what to research, not sources of truth. Research everything; find evidence.
- Full Rust build is the intended implementation for the product.
- Keep an online copy of everything in a GitHub repo created from the user's WSL setup; the repo tracks all research.
- Do not leak anything from the user's machine, user, IP, keys, or accounts into anything published.
- Follow the workflow-playbook for this project.
- Product direction comes from the pasted spec: canvas-primary block model, local-first, zero-knowledge E2E encryption, self-hosted, cross-platform (desktop + mobile + web), Rust, sandboxed-JS plugins, small local AI model, handwriting everywhere, universal search with no exceptions, editing of office/PDF/video/audio in-app.
- The research brief (research-brief-pasted-2026-10-26.txt) defines research threads A through G and its own rules: primary sources only, name every claim's source, never fill gaps with invention, benchmark where testable, one question at a time, write everything down.
- User instruction: "Don't agree or disagree with anything above" - the spec and brief are the research mandate, not items to debate.
- R12 round directive: the rounds are not just for confirming what we have; their output is enrichment for the build phase: design-relevant evidence, patterns, and details we can act on later. Collect and file accordingly.
- R12 round directive: every claim gets re-proven with real research before this round treats it as true; do not inherit earlier conclusions. Where new evidence contradicts an earlier finding, correct the master files and record what changed and why in the findings file and in the round's milestone entry.
- R12 round directive: no feature area outranks another; do not narrow any pass to what earlier rounds emphasized. Treat every app as if we know nothing about it yet and research it whole.
- R12 round directive: every app also gets a video-evidence pass: official demo and tutorial videos, YouTube walkthroughs, review footage, and the comment threads under them, plus HN and Reddit-style discussion threads, because video shows real workflow behavior that docs, screenshots, and text reviews miss, and comments surface the gripes reviewers leave out.

## Rules

- Secrets and identifying data (usernames, user IDs, guild/server names, machine names, IPs, keys, tokens, personal names tied to accounts) must never appear in anything committed or pushed.
- Raw Discord exports stay in research-material/ and are gitignored; published artifacts reference Discord messages by message ID only, never by author name.
- All images found during research are kept in a tracked repo folder (research-material/images/, one subfolder per round) so other chats and agents can search them later. Screenshots capture public web pages only; nothing from the user's machine appears in them.

## Success criteria

- A RESEARCH.md (plus supporting files) covering every app and linked project mentioned in the chats, with features, reviews, issues, and source-code findings, each with sources.
- The feature-request digest of the Discord communities, referencing message IDs, with no usernames.
- A git repo on the user's machine (WSL) with all research committed, and a GitHub remote.
