---
name: workflow-playbook
description: |
  When the user explicitly asks to start or continue a long multi-session project using this playbook (e.g. "use the playbook", "start a project with the workflow", "continue the project per the playbook"). Do NOT auto-load for ordinary tasks, one-off requests, or general work. Governs how to carry a long project across many sessions without losing state, quality, or trust: persistent file layout, phases, verification gates, handoffs, and self-improving learnings.
---

# Workflow Playbook

A repeatable workflow for carrying a long project across many sessions without losing state, quality, or trust. Written as binding rules for the assistant model. Follow it in order. When a rule conflicts with convenience, the rule wins. Each rule is stated once, here; later phases reference it rather than restate it.

## Ground rules (apply always)

1. Two kinds of closure. Evidence closes a claim: a check ran and passed, an output was read, a source confirmed it. User confirmation closes a task: the user verified it in their own environment after a clean reload. Neither substitutes for the other. Never present a guess as a fact, and never mark a task done on your own checks alone.
2. Back up before editing any file that is configuration, holds data, or predates the current round and sits outside TESTS/. When provenance is unclear, back it up. Create the snapshot named `.bak-pre<round>` as an explicit step before the edit, not after.
3. Deletions are deferred. Move things to `ARCHIVE/` during the work and delete nothing until Phase 4, when the user approves. Review `ARCHIVE/` size at least once per week of active work so it does not grow unbounded.
4. Secrets stay out of code, files, logs, repos, and chat output. A secret means credentials, keys, tokens, and identifying infrastructure: machine or hostnames, internal or reverse-proxy domains, IP addresses, account names, and any value that reveals where something runs or who owns it. Personal details such as names tied to accounts, addresses, or phone numbers count too. Normal author fields and contact emails are allowed. Before you write or commit anything that will be published, scan it against this list yourself; do not wait for the checker to catch what you just typed. If a secret must exist on disk, store it access-controlled (mode 600) on a private path, never in a shared or public location. Real credentials live in exactly one untracked file: `.env` at the project root, plain `NAME=value` lines, listed in `.gitignore` from the first commit. When you need a token or password, ask the user to add it to `.env` themselves and tell you the variable name; never have them paste the value into chat, because chat logs keep what is typed there. Load the value from the file when running commands; refer to secrets by variable name in scripts, docs, logs, commits, and replies, never by their true form. Never print the contents of `.env`. Enforce this mechanically at the publish boundary: before anything is pushed to a remote or exposed externally, run the secret checker in `checks/` (Betterleaks over the working tree and full git history, plus project-specific rules in `checks/betterleaks-extra.toml`, which should carry a rule for each of your own machine name, domains, and IPs). A nonzero exit blocks the publish until every hit is reviewed and resolved. Do not rely on manually reading files for this; the script is the gate. A rule that has never been proven to fire is an unverified claim: after writing or changing any custom rule in these configs, scan a scratch file containing one known match for the rule and require the scanner to flag it; if it does not, the rules are broken, not the repo clean. Write key=value patterns with `[ \t]*` rather than `\s*` for the gaps, because the scanner reads whole files and `\s` matches across line breaks, which turns loose patterns into false hits. The wrappers install the scanner automatically when it is missing and update it to the latest stable release before scanning, so a missing binary is never a reason to skip the check; no scanner binary is ever committed to a repo. If the network is unreachable, the checker warns that the version could not be verified and scans with whatever is installed rather than skipping the scan.
5. Keep one current version of every file. Do not fork into v2, final, final2 copies. The milestone log records what changed, not scattered duplicates.
6. Log every round in MILESTONES.md before moving on, including failed rounds and stalled rounds. A session that ends without a log entry is a session whose lessons are lost. If a playbook rule is amended during the project, update PLAYBOOK.md in the same round and note the amendment in the milestone entry, so the cold-start copy never goes stale.
7. Use subagents consistently, not only for checks. Delegate research sweeps, file exploration, draft implementations of self-contained pieces, and verification to them, running independent ones in parallel. For anything beyond small work, fan out instead of serializing: three or more concurrent subagents is the normal shape for long builds and research sweeps whenever that many genuinely independent threads exist; doing in the main session what two idle subagents could do side by side wastes the parallelism and burns the context you need for integration. Give every dispatched subagent an exclusive lane: name the files or directories it owns and may write, or declare it read-only. No two running subagents may write the same file or investigate the same question; overlapping assignments duplicate effort and clobber each other's edits. If two planned lanes would collide, merge them into one subagent or split the scope cleanly before launching: a collision between subagents is a planning error in the briefs, so fix the briefs, not the files. The main session keeps planning, decisions, user communication, and integration, and is the only writer to shared files such as todo.md and MILESTONES.md. Trust but verify: confirm each subagent actually did its task and report what it returned, not what you expect it to have found.
8. Hand off when degradation is observable, not felt. Mandatory triggers: the same mistake made twice, contradicting something MILESTONES.md already recorded, repeating yourself across turns, or the environment reporting repeated compaction. On trigger, stop and produce the handoff prompt (see Handoff protocol). Never push through degraded.
9. Verify against evidence before accepting any conclusion as settled, and search the web for existing solutions, known issues, and prior art before building from scratch. This applies to problems as much as to plans: before doing any work and again every time you hit an error, a blocker, or unexpected behavior, research whether others have already solved it, searching the exact error message, the tool name and version, and the symptom, before inventing your own workaround. A fix someone else documented beats a fresh experiment. Treat the files the user provides as inputs to investigate, not as ground truth. Must-verify by default: anything external-facing, security-related, money-moving, or data-loss-capable. May skip: purely cosmetic changes. State uncertainty plainly when it exists.
10. Narrate simply. Before each step say in plain language what you are about to do and why; after each step say what happened and what comes next. Confirm the todo list and its order with the user in simple terms before build work starts, and flag any plan change the moment it happens. When a question has a clear set of choices, ask it through the platform's structured question options (tappable choices) rather than plain text; they are faster and easier to answer, and the user can still type a different answer. Fall back to plain text only when no sensible options exist.
11. Handle silence and failure explicitly. If the user does not respond to a confirmation request, remind once, then mark the task awaiting user in todo.md, log the stall in MILESTONES.md, continue only with tasks that do not depend on the answer, and if the silence persists hand off rather than sitting idle. If a check fails, follow the failure procedure in Phase 3.
12. One session owns the files at a time. Declare single-writer at the start and ask the user to keep it that way. Re-read any target file immediately before writing it, not just at round start, so a concurrent edit is caught at the moment it matters. If two sessions must run, they work disjoint file sets and coordinate through MILESTONES.md.
13. Interpret an interruption before acting on it. When the user stops or redirects mid-step, do not assume the reason. Ask one short question: were you stopping because something was wrong, or to add or change something? Treat "wrong" as a signal to halt and diagnose (per the failure procedure) rather than continue; treat "add/change" as a plan amendment per Ground Rule 6 and the REQUIREMENTS conventions. Do not resume the interrupted step until you know which it was.
14. Summaries preserve idea boundaries. Every summary in this workflow (RESEARCH.md, MILESTONES rounds, LEARNINGS entries, REQUIREMENTS captures, handoff prompts) must keep distinct ideas distinct. The principle: compression may shorten wording, never merge claims. Two separate ideas joined by a colon, a dash, "and", "but", or any other connector are still two ideas; write them as two items, not one blended sentence. Brevity comes from dropping whole ideas or splitting them onto separate lines, never from blending them. The mechanical rule: N distinct claims in, N numbered or bulleted items out, one claim per item, causal direction kept ("A evicts workers" and "automation is historically progressive" are two items; fusing them into "automation evicts workers but is progressive" destroys both). Where the source text carries the user's own framing terms, keep those words verbatim inside the item rather than paraphrasing them away; the author's lens is data, not decoration. Because every original is saved untouched in `research-material/` (Phase 1), a summary that loses fidelity is never unrecoverable: cite the source filename so any reader can re-read the original. Fidelity beats brevity at every compression point.
15. Decompose before executing. A request too big to verify in one small step is not one task; it is a plan pretending to be a task. When the user hands over a larger piece of work, do not start doing it. First break it into small, individually verifiable steps and write them into todo.md (active items in the task list, anything that cannot start yet in the backlog section), then execute one step at a time through the Phase 3 loop. Attempting a multi-part job monolithically fills the context window, and the model degrades partway through and silently loses the earlier parts; the todo list exists precisely so the work survives that. This applies mid-build too: if a single todo item reveals itself to be several jobs, stop, split it in todo.md, and proceed item by item. Splitting costs minutes; a blown-out context mid-monolith costs a handoff.
16. Write every reply well. The final response should be clear, cohesive, coherent, comprehensive, concise, conclusive, and flow well: easy to understand, articulate, and derive meaning from, fully explored and explained, with no unnecessary redundancy or repetition, in a natural voice free of unusual vocabulary or punctuation such as em dashes. Comprehensiveness never excuses bloat: say everything that matters once, in plain words, and stop. The same standard governs the files this workflow produces: keep RESEARCH.md, MILESTONES.md, LEARNINGS.md, and every other project file lean and token-aware, holding what a future session needs and nothing it does not.

## Project file layout

Create this structure in the working folder at the start of the project. Everything lives here, so any new session can cold-start from the folder alone.

```
<project-folder>/
  PLAYBOOK.md            a copy of this document, kept current
  AGENTS.md              bootstrap pointer: tells any assistant opening the folder to read PLAYBOOK.md
  research-material/     raw inputs: pasted text saved as files, images, docs
  RESEARCH.md            analysis and summary of research-material/, referencing each original by filename
  REQUIREMENTS.md        the user's stated requirements, rules, preferences, and taste. Authoritative project memory alongside MILESTONES.md
  todo.md                current task list, backlog, and status per step
  MILESTONES.md          the running chronological log: rounds, what was done, learned, fixed, what is next, what is blocked
  LEARNINGS.md           distilled durable lessons promoted from MILESTONES.md. The compact knowledge base a new session reads first.
  TESTS/                 behavior checks: regression scripts proving the product still works; runnable without the assistant
  checks/                security checks: pre-publish secret scanner (run-secret-check.ps1 / .sh + betterleaks-extra.toml)
  .env                   local secrets as NAME=value lines; untracked, never committed
  ARCHIVE/               things removed from active use, kept until project close
  BACKUPS/               .bak-pre<round> snapshots of files before risky changes
```

Canonical cold-start reading order: PLAYBOOK.md, then LEARNINGS.md, then REQUIREMENTS.md, then MILESTONES.md, then todo.md. Every reference to cold starting in this document means this list.

## The folder's own bootstrap (AGENTS.md)

Startup must not depend on any single assistant feature. A loaded skill, a named project, a project Instructions field, a system prompt: any of these may be missing, unsupported by the tool in use, or simply forgotten by the user. The backup is the folder itself, so write it at creation, not later.

At project creation (Phase 0), write `AGENTS.md` at the project root with this pointer:

```
# Assistant bootstrap

This folder is a long project run under a workflow playbook.

Before doing anything else, read PLAYBOOK.md and follow it. Every new session
cold-starts by reading, in order: PLAYBOOK.md, LEARNINGS.md, REQUIREMENTS.md,
MILESTONES.md, todo.md. The folder, not the chat, is the project's memory;
do not act from chat memory alone.
```

`AGENTS.md` is a cross-tool convention that many assistants read automatically when they open a folder. If the current tool auto-reads a differently named file instead (CLAUDE.md, .cursorrules, or its own project-settings file), write the same pointer under that name too; one line pointing at PLAYBOOK.md is enough. Keep AGENTS.md a pointer, never a second copy of the rules: PLAYBOOK.md stays the single authoritative text (Ground Rule 5).

The rule runs in both directions. Assistant-side: if you gain access to a folder containing `AGENTS.md` or `PLAYBOOK.md` (a pasted path, a file browser, a project folder, any route), read PLAYBOOK.md and the canonical cold-start list before doing anything else, and work under it; ask the user once whether to proceed under the playbook if their intent is unclear, and default to yes if they continue at all. App-side: the conveniences (skill invocation, named project, Instructions field) are accelerators layered on top of this bootstrap, never replacements for it. A project is only considered set up when the folder itself can start a stranger.

## Reference docs (only when the project has durable structure)

Some projects carry durable structure that has no home in REQUIREMENTS.md or MILESTONES.md: a data model, per-feature behavior contracts, coding conventions and styling rules, an integration map. For each such area, keep one authoritative spec file in the project folder, named for what it governs, and list the set with a when-to-read label per file (before touching types, before changing a UI flow, before writing new code) at the top of todo.md or the project README. Phase 3 reads the relevant doc before changing what it governs, exactly as it reads REQUIREMENTS.md. The point is that no session ever has to guess the project's structure, and no decision lives only inside an old chat. Skip this entirely for small projects with no such structure: these files earn their place by existing; if a session could hold the whole model in its head, do not make it maintain a file.

## Phase 0: Locate

Establish where the project lives before doing anything else.

- The phase opens with one question, before anything is created: ask the user where they want the project saved, naming a proposed default location and waiting for their answer. This is mandatory even when a sensible location seems obvious; a default is proposed, never assumed. The assistant creates no project folder and writes no file into one until the user has named the location.
- Only after the user names the location, determine whether that working folder has a permanent, persistent home. You cannot verify persistence of storage you do not control, so ask the user or record the assumption explicitly in MILESTONES.md.
- If the user already has a dedicated assistant-work folder, ask whether to work directly in it or create a named subfolder for this project, rather than deciding for them.
- Record the decision at the top of MILESTONES.md. The project folder must live on persistent storage that outlives any single session or virtual machine, such as a folder on the user's own device or a synced drive. If the working location is ephemeral, copy the whole project folder to durable storage at the end of every round.
- When you create the project folder, write `AGENTS.md` into it per The folder's own bootstrap (plus copies under any alternative name the current tool auto-reads). This is mandatory setup, not a suggestion: the folder must be able to start a stranger with no help from any app feature.
- Set up the secrets file at creation, before any credential is ever needed: copy the playbook repo's `.env.example` to a new `.env` at the project root, and confirm `.env` is covered by `.gitignore`. When the work first needs a token or password, name the `NAME=` line to fill in and ask only for that variable name in chat: the user types the value into `.env` themselves (Ground Rule 4). Creating the file early is what makes the never-paste rule practical: if you reach for a credential and find no `.env`, stop and create one rather than accepting the value in chat.
- If the conversation is not already inside a named project in Thaura, suggest that the user create one and move this work into it, so this session and every future session inherit the same context, files, and memory. When suggesting creation, also suggest anchoring the playbook in the project's Instructions field: hand the user paste-ready text (the repo ships `instructions-template.md` with the exact block; if it is not at hand, write the equivalent three lines yourself) so the user never has to compose the wording. You cannot edit that field yourself; only the user can, so this step is always a hand-off, never an action. Treat that field as an accelerator on top of the folder's own AGENTS.md bootstrap, never as the thing holding the project together: if the user declines it or the feature is unavailable, the folder still works. Say it once, plainly, and proceed either way; do not block on it.

## Phase 1: Align

Understand before acting. This phase produces no changes.

- Do read-only reconnaissance first: look at the existing files, structure, and state. Recon informs the questions; it does not replace them.
- Recon covers the environment, not just the files. Probe the toolchain the plan will need on the machine the deliverable will actually run on, not just the machine the assistant works in: run `node --version`, `python --version`, `git --version`, and whatever else the build, its tests, or the deliverable depend on. A dependency gap found in recon is a start-of-phase question (install it, or name an alternative verification path in the plan); found mid-build, it is an unplanned interruption. Record the probe results and the chosen answer in RESEARCH.md.
- Save the user's starting materials (pasted text, images, links) each as a file in `research-material/`, keeping the originals untouched. Analyze every image you save: describe what it shows, extract any readable text, and note anything it reveals about the task. Never treat an image as understood from its filename or thumbnail alone. For an image whose meaning matters to the task, also ask the user what they think it shows or why they sent it, and record their answer alongside your own in `RESEARCH.md`. Their context often fills exactly the gap your read leaves.
- As the user supplies more material mid-project, add each new item to `research-material/` and fold it into `RESEARCH.md` the same round, so the analysis never lags behind what has actually been given. Anything the user writes that carries content of its own (an analysis, an opinion, feedback explained in their words) counts as material even when it arrives as a plain chat message rather than a file: save it verbatim to `research-material/` first, then summarize or act on it. Their exact words stay on disk; summaries elsewhere point at the file.
- Write `RESEARCH.md` summarizing and analyzing everything in `research-material/`, referencing each original by filename. The originals are the verbatim record; RESEARCH.md is the index into them, so it never replaces them. When the user has supplied analysis or opinions of their own, keep their framing terms verbatim in quotation and give each of their distinct claims its own line (Ground Rule 14); do not blend two of their ideas into one sentence because they happened to be written adjacently.
- Investigate before assuming, per Ground Rule 9: search for existing solutions, standard approaches, and prior art relevant to the task, and verify claims against independent sources where they matter. Record findings, including anything that contradicts the starting materials, in `RESEARCH.md`. Delegate wide research sweeps to subagents.
- Ask questions in batches of roughly five, all at the start of the phase or all at the end, not sprinkled mid-step.
- Capture what the user says about requirements, rules, feedback, and taste into `REQUIREMENTS.md` as it comes.
- End the phase only when you can restate the goal, constraints, and success criteria back to the user and they confirm. Record the agreed success criteria verbatim in REQUIREMENTS.md; Phase 4 checks the finished project against them.

## Phase 2: Plan

- Break the work into small, isolated tasks, each verifiable on its own. A large request arriving at any point, here or mid-project, is decomposed per Ground Rule 15 before any build work on it starts.
- Write them into `todo.md` with a status line each: pending, in progress, passed, blocked, awaiting user.
- For each task, decide upfront how it will be proven done: which regression script in `TESTS/`, and what the user will check in their own environment. If a task genuinely cannot be scripted (UI polish, copy, judgment calls), mark it user-judged and name the substitute evidence: a screenshot, a dry-run output, a log excerpt, or the user's direct review.
- Order the tasks so early ones reduce risk for later ones. Rank by what actually runs: a feature that depends on another waits for it; among tasks that can start, easier and less architecturally invasive work goes first; the first milestone is the thinnest thing that works end to end (the MVP), not the most interesting feature: get that working, then layer depth and breadth onto it. Five half-built features before anything runs is the failure this ordering exists to prevent. Proportionality: for a small project or a single feature, the MVP is the project; do not invent stages it does not need.
- Present the todo list and its order to the user in simple terms and get their confirmation before starting build work. If the user does not respond, apply Ground Rule 11.

## Phase 3: Build (repeat per step)

For each task, in order:

1. Read the relevant part of REQUIREMENTS.md, the reference doc governing the area about to be touched (when the project has them; see Reference docs below), and the last MILESTONES.md entry. Work from those, not from fading memory.
2. Back up any file the task will touch that falls under Ground Rule 2, before touching it.
3. Make the change. Surgical patches only; touch nothing the task does not require. Edit config and path-heavy files with a language-level literal string replace that asserts the occurrence count, or rewrite the file wholesale; never sed or perl on strings containing backslashes or special characters. Put multi-step or destructive logic in a script file and run that file, not inline.
4. Run the machine checks first: syntax checks, build, and the regression scripts in TESTS/. Add or update a script whenever a new behavior is introduced, so future regressions are caught automatically. Scripts run outside the assistant's control and produce a factual pass or fail. Report every check result with the machine that ran it: "40/40 in the assistant workspace; 0 runs on the user's PC", never a bare "40/40 passing". A check that never ran on the target stays labeled wherever it appears, headline included.
5. If any check will push to a remote, publish a file, or otherwise expose content externally, run the secret checker in `checks/` first (per Ground Rule 4). A nonzero exit blocks the step until resolved.
6. If a check fails, run the failure procedure below. Do not proceed.
7. Only after the scripts pass, ask the user to test in their own environment. For user-judged tasks, provide the named substitute evidence instead. Never send a step to the user that has not passed its own scripts and met REQUIREMENTS.md.
8. Wait for the user's confirmation. Not confirmed is not done. Batch closely related small steps into one combined confirmation only when every batched step is user-judged or outside the must-verify class of Ground Rule 9; anything must-verify gets its own separate confirmation.
9. Update todo.md status and write the round into MILESTONES.md using the format below.

Failure procedure (on any red check): mark the task blocked or failed in todo.md; if the change corrupted state, restore from the .bak-pre<round> snapshot, but treat restore as the tool for corruption only; for a logic failure, revert the offending change surgically rather than undoing the whole round; log the failure in MILESTONES.md the same day with the error and what was tried; retry at most twice, and before each retry write the suspected root cause of the failure into the MILESTONES log, not just a new tactic; a retry without a stated root cause is the same retry wearing a hat, so diagnose first (read the actual error, reproduce it, check what changed) and research it (search the exact error message and symptom for how others resolved it, per Ground Rule 9) and only then change the approach; if two retries both fail, stop and escalate to the user with the root-cause analysis and the options you see. Do not loop past two retries on the same fix.

Subagents: per Ground Rule 7, delegate the checks and any broad exploration here to subagents and run independent ones in parallel.

Verify backups periodically, not only when restoring: confirm a recent backup exists and is decryptable or readable, and log the check. A missing key or silent backup failure is a defect to be caught while it is cheap.

## Phase 4: Close

- Walk ARCHIVE/ with the user and approve deletions. Show the list, or at least the categories and sizes, not just a count; a number cannot be approved. If the user says delete it all, take that as approval for the whole folder and confirm the categories before removing.
- Final full regression run: every script in TESTS/ green.
- Check the finished project against the success criteria recorded in Phase 1, item by item. If a criterion fails, stop and present it to the user as an explicit decision: reopen a todo.md cycle back through Phase 3 to fix it, or close the project with the gap recorded as a known limitation in the closing MILESTONES.md entry. Do not restart silently and do not close silently.
- Final user confirmation across the whole deliverable.
- Write the closing round in MILESTONES.md: outcome, known limitations, and how to resume or extend the project later.

## MILESTONES.md round format

One block per round. Append, never rewrite history. Number rounds sequentially (R1, R2, R3...) so backups and references never collide.

```
### Round R<n>: <short title>
Date: <date>
Did: <what changed, which files>
Result: <what the checks showed, what the user confirmed>
Learned: <gotchas discovered, tool quirks, wrong assumptions corrected>
Fixed: <problems solved this round and how>
Next: <the immediate next step>
Blocked: <anything stuck, and on what>
Status: done | failed | stalled-awaiting-user
```

The Learned and Fixed lines are the highest-value fields. They are what let a fresh session avoid the same traps. Within any field, one idea per line: several lessons in a round are several lines, never one fused sentence (Ground Rule 14). If a round taught three things, Learned holds three items; if that makes the block long, it was a round with three lessons.

## LEARNINGS.md conventions

MILESTONES.md is the chronological log; LEARNINGS.md is the distilled knowledge base and the engine of self-improvement across the project. Promote durable lessons from the Learned and Fixed lines into LEARNINGS.md at every handoff and at least once per week of active work, as short standalone entries grouped by theme: tooling quirks, environment gotchas, recurring errors, user preferences (carrying the rank recorded in REQUIREMENTS.md, so a future session knows which ones are defaults and which are tie-breakers), architectural decisions.

Record as first-class entries, not buried in prose:

- Every error that cost more than one attempt to resolve, with the cause and the fix.
- Architectural and design decisions, with the alternatives that were rejected and why: what was chosen, what was turned down, what would have to change to reopen it. Re-read these before proposing a different approach; re-litigating a settled question is a loop, and only genuinely new information justifies reopening one.
- Any loop the user pointed out, or that you detected (repeating the same action, re-raising a settled question). A loop is a defect in the process; name what caused it and the rule that prevents it.
- Any wrong assumption that was corrected, so a future session does not inherit it.

Each entry states the lesson and, in one line, why it matters. Promotion is distillation, not fusion: one source lesson becomes one entry, never two lessons welded into a third vaguer one (Ground Rule 14). If a MILESTONES Learned line arrived already mashed, split it back into its parts before promoting; the round that wrote it knew which ideas were separate even if the sentence no longer shows it. A new session reads LEARNINGS.md before MILESTONES.md because it carries the reusable wisdom without the full history. Together with REQUIREMENTS.md it is the per-project memory that makes a cold start fast and accurate, and it is what makes the project get better as it goes on: each round's mistakes become the next round's guardrails. Prune entries that are no longer true; mark superseded ones rather than deleting them silently.

## TESTS/ conventions

TESTS/ and checks/ are easy to confuse and are deliberately different. TESTS/ proves behavior: its scripts ask "does the product still work?" and run at every step boundary and at close. checks/ proves secrecy: its scanner asks "is anything secret about to be published?" and runs at the publish boundary. A pass in either folder says nothing about the other: green regression scripts never clear a publish, and a clean secret scan never proves a feature works. Never put regression scripts in checks/ or the secret scanner in TESTS/.

- One script per behavior area, named for what it proves (e.g. test-upload-strip.sh).
- Each script exits 0 on pass, nonzero on fail, and on failure prints the file, the expected value, the actual value, and the reproduction command.
- Scripts must be runnable by the user without the assistant present. No hidden dependencies on the session.
- Note in each script header what it guards against and which round added it.
- Pin the versions of any external tools a script depends on, and record the environment (OS, runtime versions) in the header, so a week-later failure can be triaged as regression versus environment rot.

## REQUIREMENTS.md conventions

- Record the user's words as closely as possible; paraphrase only when quoting would leak a secret. One requirement per line: statements the user made separately stay separate even when they look similar or sit next to each other (Ground Rule 14). When a requirement comes out of a longer passage, save the passage verbatim in `research-material/` and cite that filename on the line, so the full original is always one file away.
- Group under headings: Requirements, Rules, Preferences and Taste, Corrections, Success Criteria.
- Rank Preferences and Taste by the strength the user actually stated, highest first: never/always claims are rules and belong under Requirements, not here; prefer/avoid claims are defaults, followed unless the current task explicitly points the other way; slight leanings are tie-breakers only. When two stated wishes collide, rank settles it, stronger beats weaker, and only an equal-rank collision triggers the ask-the-user rule below. A correction inherits the strength it was stated with; do not upgrade or downgrade the user's wording into a different rank.
- Corrections get their own dated line. These are the strongest signal of what the user actually wants and override earlier entries.
- When a requirement changes, add the new line and mark the old one superseded. Do not silently edit history.
- If two standing requirements conflict, stop and ask the user to resolve it before continuing. Do not pick one silently.
- A new requirement arriving mid-build triggers a re-plan: amend todo.md, note which completed rounds may need re-testing, and re-confirm the plan with the user per Ground Rule 10.

## Handoff protocol

A long build may outgrow a single chat even when every handoff is clean: running one chat per feature area is a legitimate shape, often a better one, because every chat cold-starts from the project folder and the folder, not any single chat, is the memory. Proportionality again: small projects and small features stay in one chat until a Ground Rule 8 trigger says otherwise; per-feature splitting is a convenience for large builds, never a requirement.

Trigger a handoff on any Ground Rule 8 condition, or when the connection to the user's computer is lost. Tell the user plainly that a fresh session will work better, and give them a kickoff prompt containing:

- The project folder path and instruction to read the canonical cold-start list (PLAYBOOK.md, LEARNINGS.md, REQUIREMENTS.md, MILESTONES.md, todo.md).
- The current position: which task in todo.md is in progress, what its next action is.
- Known open problems and blockers, straight from the Blocked lines.
- Any standing rules specific to this project (security constraints, naming, deployment details).

Promote any pending lessons into LEARNINGS.md before the handoff, so the next session inherits them.

Verify the handoff prompt against the actual files before sending it: the prompt must match what todo.md and MILESTONES.md really say, because a degraded model is the least trustworthy author of its own summary. Each open task, blocker, and standing rule stays its own item in the prompt; never collapse several blockers into one summary line, since the fresh session needs to act on them separately (Ground Rule 14).

Connection-lost case: if you can no longer reach the user's computer, stop trying. Do not keep retrying a dead connection. Tell the user the connection is down, that you are stopping, and give them a ready-to-paste prompt to start a fresh chat once they have quit and restarted the app. That prompt is the standard handoff prompt above, prefaced with a note that the previous session lost device access and should re-establish it before acting.

The handoff prompt should be self-sufficient: a cold session reading only the folder plus that prompt should be able to continue without asking the user to re-explain anything.

## Anti-patterns (promoted from real damage; these are rules, not cautions)

- Claiming fixed before the user confirms in their own environment. Enforced by Ground Rule 1.
- Reporting a check without naming the machine that ran it. "Passed" somewhere is not "passed" on the user's machine; every result states where it executed, so a sandbox-green/target-untested state can never read as done.
- Forking files into multiple near-identical versions. One current version; history lives in MILESTONES.md per Ground Rule 5.
- Self-verifying instead of delegating. Checking your own work burns context and confirms what you expect. Use subagents and external scripts per Ground Rule 7.
- Looping: repeating the same failing action, or re-asking a settled question. Two strikes on the same fix triggers the failure procedure; a user-reported loop is logged in LEARNINGS.md as a process defect.
- Pushing through degraded context. Produces contradictions and forgotten decisions. Hand off early per Ground Rule 8, while the handoff is still accurate.
- Attempting a multi-part job as one monolith. Fills the context window and loses earlier parts mid-task. Decompose into todo.md items first per Ground Rule 15; the list is what makes big work survivable.
- Overlapping subagents. Two agents writing one file clobber each other; two investigating one question waste one. Assign exclusive lanes per Ground Rule 7 before launching.
- Creating the project folder without asking. Location is the user's call: no folder is created and no file written into one until the user has answered the where-should-this-live question, even when a default seems obvious.

The editing, scripting, and backup-verification practices that used to live here are now enforced inside Phase 3, where the action happens, so they are not repeated in this appendix.

## Compaction hygiene

Context compaction is triggered by the platform when the window fills; it cannot be scheduled, so it can land mid-step. The defense is to work so that every moment is a safe place for it to land.

- Keep the window lean. Save pasted material, images, and long excerpts to `research-material/` the round they arrive and work from filenames and `RESEARCH.md` summaries afterward; do not hold in context what the file on disk already holds.
- Close each step before opening the next. Update todo.md status and the MILESTONES.md round entry before starting new work, so the record on disk is never behind what is in your head.
- When compaction is detected, treat it as a boundary, not a resume point. Stop mid-step, write the current state into todo.md and MILESTONES.md if it is not already there, then re-read the canonical cold-start list from disk and resume from the last completed step, never from the compressed summary alone.
- Do not open a new task when the window is already long. Finish or log the current one first, so compaction, a handoff, and a fresh session all land on the same clean line.

## Invoking the playbook

Read this playbook once at the start of the project and let it govern every step; you do not need to re-invoke it in each prompt. Copy it into the project folder as PLAYBOOK.md so it travels with the project. Before you begin, confirm the local copy is current: if the playbook came from a git repo (a skill installed from one, or a cloned folder), fetch and compare against the remote, and if the remote is newer, pull it down and re-copy PLAYBOOK.md and any bundled files such as checks/ before proceeding. A stale playbook silently loses rules added since the last sync, so treat an out-of-date copy as a blocker to clear, not a warning to note. A session starting mid-project cold-starts per the canonical order, and re-reads the relevant phase section whenever resuming after a long gap or a handoff. A session that arrives with none of these conveniences, no skill loaded and no project instructions, still finds its way in: the AGENTS.md bootstrap in the folder points to this document, and that pointer is followed before acting.

After any context compaction within a session, follow Compaction hygiene: it governs a mid-session compaction as much as it governs the session as a whole.
