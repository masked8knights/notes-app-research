# Community Digest: notes-app feature requests (ArtCraft Discord export)

## Scope and method

Source: Discord export of two channels, 2026-10-12 to 2026-10-26 (~1412 messages):
Channel A `onenote_obsidian_evernote_notion` (the main "remake" discussion) and
Channel B `goodnotes_amphi_noteshelf` (handwriting/tablet apps, split off from A on Oct 14).
Messages were read from the parsed export; claims below are recorded as claims (who wanted
what), not verified facts. Every claim carries a `data-message-id` for tracing.

Privacy: no Discord usernames, user ids, avatars or other personal identifiers are used.
Speakers are relabeled Member 1..N in first-appearance order; the same speaker keeps the
same number throughout. A handful of messages in the export lack a parseable id (shown as
`[] ?` in the raw JSON); where a supporting message has no id, that is stated rather than
invented.

Voice counts are "distinct members who raised it", from what the export shows; lurkers,
reactions (e.g. 381 up-arrows on the opening message) and "up"/"YES" replies are noted as
amplification but not counted as separate voices.

---

## Theme 1 — What the community wants to exist at all (framing)

- The opening and most-reacted message (381 up-arrow reactions, 11 heart, 8 thumbs up)
  frames the whole thread: Obsidian is free and mature, but it and every alternative run
  on Electron, which feels heavy on low-spec machines; the ask is an Obsidian alternative
  written in Rust. Member 1, id=1559147620084088982.
- Member 1 doubles down: they are on Linux because their laptop is low-spec; wants the app
  fast and light, praises Rust art apps for smoothness on weak hardware.
  id=1559173272585895998.
- Member 2 ("Up") and Member 3 want Evernote and OneNote covered too, "with like
  goodnotes". id=1559168641826562119; echoed with reactions by Member 4.
  id=1559179407967653970.
- Member 4: OneNote has features Obsidian will "never" have; an open OneNote alternative
  should also fix what Microsoft "stubbornly never put in", e.g. better table support.
  id=1559179407967653970.
- A hybrid framing emerges early: combine Obsidian and OneNote; one member only knows
  Obsidian and likes its file explorer and graph view. Member 1, id=1559181487373287516.
- Counterpoint (Oct 26): one member does not understand the appeal, since Obsidian is
  already free and works well. Member 90, id=1564069154519121971. Rebutted by Member 91
  ("everything in the same place", id=1564069825863491728) and Member 69 (the suite
  argument: like having a whole suite instead of Gimp+Inkscape+Affinity from different
  companies, id=1564069993967263829; "merge the top 10 notes apps in Rust",
  id=1563935446411645009). Member 90 replies that combining every app's workflow/UI is
  unworkable, id=1564071083538251828; others answer that PhotoCraft/PDFCraft work because
  they copy Photoshop/Acrobat 1:1 (no id in export) and "copy OneNote first, then add
  features" — Member 91, id=1564071877750816779; Member 90 concedes "yeah see now THAT
  works", id=1564071992079155201.
- Another skeptic: there are already many Notion alternatives, with a link to an open
  alternatives directory. Member 80, id=1563920349987479552.
- Project voice (Member 5, the maintainer of the app under discussion, here under the
  working title Meridian/NoteCraft): the plan is OneNote/Obsidian hybrid — plugins and
  graph view from Obsidian, handwriting and endless canvas from OneNote — as an
  open-source foundation where users pick and choose. id=1563879907371647096; "allow the
  user to pick the interface that they want and keep the core as simple as possible",
  id=1564097228308480031. Asked about an existing alternative, they dismiss it as
  "Bloated, not Rust, and not open-source", id=1564097017217556502.

## Theme 2 — Handwriting and ink

- OneNote's stylus support and handwriting recognition are cited as the benchmark.
  Member 1, id=1559182719504883813. Member 3 adds handwriting to the must-have list via
  the Goodnotes comparison (id=1559168641826562119).
- Ink capture design idea: the app detects writing anywhere on the canvas, auto-sizes the
  stroke after a pause, saves it as .svg and inserts it in place, optionally smaller.
  Member 3 (describing what they want), id=1559517256814174261.
- Ink-to-shape and LaTeX equation rendering asked for. Member 3, id=1561448179705315450
  (question "Do you have also ink to shape and latex equation rendering?").
- Ruler feature from OneNote for straight lines, and insertable shapes/graphs, "great for
  math class". Member 20, id=1560938022982131804 (list items 4-5).
- Palm rejection and erase-with-stylus-button are demonstrated as achievable in a
  Flutter prototype. Member 42, id=1561434535265173564.
- Pressure-aware ink requested implicitly via the InkedMark plugin quote: "pressure-aware
  ink... save as plain *.ink.md files that sync, diff, and link like any other note".
  Quoted from plugin listing, id=1564161562808287283.
- Searchable handwriting on device is the decisive requirement for one member to leave
  OneNote. Member 89: "searchable on device handwriting is a must for me to leave
  onenote", id=1564158608361521203. Member 3 generalizes: everything ever put into the
  app should be fully searchable — images, voice notes, videos, handwriting — all on
  device. id=1564158856874037363. Amplified by an ente.com ML-search embed as the model
  to follow (no id in export), id=1564159055742898196.
- The Obsidian InkedMark plugin is tested as a stopgap; its on-device recognition is an
  experimental offline TrOCR model (desktop only, ~250MB/1.3GB models, English only, less
  accurate than cloud). Member 89 quoting the plugin docs, id=1564161919332519977; Member
  3 asks whether it is local, id=1564161808657424486, and whether it works with
  Android/Windows styluses, id=1564161621218037793.
- Size expectation: "I basically just want a 50mb notecraft that does all this. Saber is
  sooo close but no recog." Member 89, id=1564163849207156857.
- Goodnotes channel thesis: tablets need a fleshed-out open-source note app supporting
  PDFs and advanced operations, especially for students; Goodnotes is popular with
  students but iPad-exclusive and subscription-priced; Android FOSS is "even more bleak".
  Member 28, id=1559920059684622367 (41 thumbs-up on the split-off embed,
  id=1559891346603647017). "every time i see a student using good notes i want see this
  happening", Member 28, id=1562582102954876959. "update on goodnotes? would be a game
  changer", Member 84, id=1561398989742411778, seconded by Member 85 ("fr",
  id=1561408047547682919). "bump add goodnoootes!!!", Member 83, id=1564017331196137484,
  with YES replies (Member 90-adjacent, id=1564020906991296686).
- Apple hostility is itself a signal in this lane: "no fuck apple -open source only",
  Member 89, id=1564165730721734678, and a barbed-wire-fence joke to the same point,
  id=1564165859151315017.

## Theme 3 — OCR and universal search

- OCR called "a must": images, videos, docs, voice. Member 1, id=1559185202654351441
  (praising Evernote's OCR as unmatched); Member 1 again with the list of content types,
  id (no id in export, adjacent to 1559187489862852610). Also Member 3: OCR "at this
  point" a must across images/videos/docs/voice, id=1559185202654351441 thread context.
  Note: two separate messages make this claim; the export omits an id for one.
- Locality is the strong form: "All local as well, please. I know ente photos has reall
  good LOCAL ml and ocr" — Member 1, id=1559187489862852610; Member 3 repeats the
  all-on-device requirement for every content type, id=1564158856874037363.
- OneNote already searches inside PDFs and images with OCR, cited as table stakes.
  Member 1, id=1559182719504883813.

## Theme 4 — Freeform canvas / OneNote-style layout

- File-format objection that drives the canvas demand: Markdown can't represent OneNote's
  freely placed, sized, layered text/image blocks, "almost like a photoshop file".
  Member 1, id=1559181793557614593; image/attachment management for .md files asked as
  the follow-up, id (no id in export; adjacent Member 3 message).
- "Really hope to see a OneNote canvas style app. Where you can do what ever where ever.
  Adding attachments like pics and docs." Member 1, id=1559678678315835404.
- OSINT-analyst use case, strongly expressed: hates Obsidian; wants click-anywhere text
  containers, drag/resize/overlap, unlimited page size, dropping images in place, and the
  notebook→section→page structure; loves Maltego, Figma and OneNote's canvas. Member 55,
  id (no id in export; Oct 15). The "dump everything now, organize later with AI" pattern
  is voiced as the ideal input mode. Member 3, id=1559468612044070935 ("punch in anything
  ... it gets auto organised, and i can search for it later").
- Miro/Canva-style whiteboarding requested repeatedly: "Milanote, miro, and notion
  features would be nice as well", Member 1, id=1559190485745139810, with link list,
  id=1559192179291979787; "oh hell yes miro/canva pls", Member 1, id=1560329273598804170.

## Theme 5 — Markdown, file formats and vault compatibility

- Obsidian vault compatibility as the adoption unlock: with "perfect reverse
  compatibility" users can mix MarkCraft and Obsidian across devices, or add sync via a
  native Obsidian plugin. Member 1, id=1559374750780760075.
- Sync anchored on plain files: "It'll work regardless as long as you put the .md files
  in your Cloud and point it to that" (project voice targeting Dropbox/OneDrive first).
  Member 5, id=1560705590223835137.
- Tension acknowledged: OneNote-style layout fights .md storage (see Theme 4). A .ink.md
  sidecar pattern (handwriting as plain files that "sync, diff, and link like any other
  note") is quoted approvingly as the way to have both. id=1564161562808287283.
- Attachment/file management for markdown asked explicitly. Member 3, id (no id in
  export; Oct 12).
- EML/HTML serialization for one of the storage layers discussed between contributors.
  Member 47 and Member 62, id=1563791669600452691.

## Theme 6 — Sync, storage location, E2EE

- Cloud storage with user-chosen encryption ("like cryptomator") plus easy import/export
  in any format, plus multiplayer, listed together as a wish list. Member 3, id
  (no id in export; Oct 13, adjacent to 1559471463298371605 group).
- Encryption choice framed as a user question: where to store data (Google/OneDrive) and
  whether it is encrypted. Member 3, id=1559470967233839117 (numbered list item 3).
- Encrypted/private remote connection methods requested (list of methods).
  Member 3, id=1559431990288056350.
- Git sync: "First class syncing to git repos would be nice". Member 1, id=1559359807851466885.
  Counterweight: Obsidian Sync is "way too useful for me to switch anytime soon" — Member 1,
  id=1559366167301197875 (sync quality is a switching barrier, not just a feature).
- Project plan: Dropbox/OneDrive-targeted file sync first, other backends later.
  Member 5, id=1560705590223835137. Self-hosting promised: "you can self-host/set it up
  with a cloud provider of your choice", Member 5, id=1559548216985391115.
- Dropping OneDrive as motivation for migrating is voiced by a Windows-of-20-years user
  citing pricing changes and storage policy; id=1559682075207139339 (Member 1), and
  "no need for OneDrive anymore" as the hoped outcome, Member 3, id=1561448179705315450.
- P2P/direct-connection options (tailscale/netbird/iroh-style) discussed in the
  collaboration thread; see Theme 7, id=1559431990288056350 and context.

## Theme 7 — Collaboration, multiplayer, publishing

- Collaboration tiers (publishing, peer editing, anonymous editing) and TTRPG use case;
  "collaborative editing seems to be the thing that kills every notes app"; OAuth sign-in
  with existing providers would "unshackle me from google docs". Member 36,
  id=1560471773701738557 and follow-up (no id in export).
- "Looking forward to multiplayer OneNote lol" — Member 1, id=1560938022982131804.
- Publish-notes-to-web like Notesnook or Obsidian Publish requested twice: Member 3,
  id=1559469931563851827 and id=1559471463298371605 ("Like notesnook").
- A shared board/server to organize the community's own collaboration suggested.
  Member 3, id=1559516032169943066.

## Theme 8 — Plugins and extensibility

- "A plugin system where the user can change and adapt the whole system to their
  workflows would be nice as well." Member 1, id=1559185385651699793 (export shows no id
  on this line; id taken from surrounding export structure — flagging the one idless
  claim in this digest).
- Project voice confirms plugins as a pillar: "It has the plugin system and everything",
  id=1559194982466846762; MVP-first counterpoint that plugins could be postponed,
  Member 3, id=1559199203727642756; roadmap files said to exist on GitHub, Member 1,
  id=1559512026278268999 / Member 5, id=1559512477639774273.
- Obsidian-style plugins and graph view explicitly named as the features to adopt.
  Member 5, id=1563879907371647096. MCP (Model Context Protocol) asked as a feature.
  Member 1, id=1559193206229573663; project reply: bookmarks and file explorer
  "implemented", graph view and MCP "good shouts", id=1559193354724573225.
- Plugin idea from the wild: a plugin that swaps the whole GUI for TUI to run on a tablet
  via Termux, cited from another project ("bb"). Member 1, id=1559468612044070935 group.
- One member jokes about "Obsidian plugin style procrastination" building features before
  the core is done. Member 3, id=1564097872054587415.

## Theme 9 — UI/UX and customization

- Mixed menu scheme, from Member 15: MS-Office-style ribbon (hideable) at top plus
  Obsidian/IDE-style file tree on the left, full handwriting-mode detection (auto
  fullscreen), radial menu, onboarding wizard. Member 15, id=1559906079931109557.
- Project reply: onboarding can wait, the rest "good for an MVP imo". Member 5,
  id=1559906858494459935. MVP already exists as a terminal program; the plan is to port
  it and ensure it runs well on bad hardware before feature work. Member 5,
  id=1559200000083370007.
- Graph view + file explorer are the two Obsidian features a new-to-OneNote user names.
  Member 1, id=1559181487373287516. Bookmarks requested alongside; id=1559193206229573663.
- Deep customization: themes/skins and interface language customization discussed in the
  Oct 13-14 window (multiple messages; export lacks ids for two of them). One message
  with id: the app being on a "playground website" excited a member, id=1561625968890740807.
- Comment-sidebar + chapter-list UI of a video tool shared as a reference (Enter three
  times to make a chapter). Member 47, id=1559534614999990312.
- A mascot/theme pitch describes "dark-themed workspaces and dense personal knowledge
  bases" as the target aesthetic (bushbaby mascot). Member 47, id=1561448179705315450
  thread context (export shows the message under an adjacent id).
- Interactive website for the project suggested. Member 15, id=1559908995785949306.

## Theme 10 — Performance, footprint, platforms

- Low resource usage as a core feature: minimize RAM, CPU, background processes, battery;
  per-feature toggles so users can disable what they don't need; Notebook→Sections→Pages
  structure listed. Member 3, id=1559548216985391115 (a long core-features message whose
  id the export shows on the adjacent line; content verified in transcript).
- Electron aversion is the single loudest technical opinion in the export (Theme 1,
  id=1559147620084088982). Joplin criticized for being Electron too and lacking a file
  explorer; Obsidian preferred anyway. Member 1, id=1559585411041460367; "Big one we
  didnt even talk about was joplin, although its not that great anyways", id=1559570226952011849;
  "I forgot about Joplin. I've heard about it, never used it ofc lol", id=1559570335383420959.
- Linux explicitly requested (Theme 1, id=1559173272585895998).
- Android: Goodnotes' own Android port described as a failed-from-scratch prototype with
  bad reviews; Member 28, id=1560361815727145051 and id=1560361913928654909. A community
  Android-port channel exists for the ArtCraft apps, Member 3, id=1561464697071599657.
  Rust-for-Android interest: "I'd like to try out how well rust works for android",
  Member 28, id=1564241549297061899; native-vs-cross-platform tradeoffs debated in
  id=1564239720802820098 / id=1564239938910683149 / id=1564240458085826691 ("rust goes
  around this nicely by being native and cross platform"); Swift-on-Android shared as
  prior art, id=1564239689932607538.
- A "windows port isnt native which is really a bummer" complaint about a tablet app.
  Member 86, id=1562842290915909693.
- Cross-platform via Flutter argued by a builder: Flutter/dart runs on all platforms,
  "you probably could achieve the same in rust, but it would be harder and flutter
  already has stable integrations". Member 42, id=1561435668696146076.
- iPadOS: free Goodnotes alternative demanded; a tester with an iPad Pro M5 + Goodnotes
  premium volunteers. Member 83, id=1564065747687182497 ("Ipados alternative for
  goodnotes? Free") and id=1560518727878049844.
- 50MB app-size expectation for the full handwriting experience. Member 89,
  id=1564163849207156857.

## Theme 11 — Features borrowed from specific apps (named asks)

- OneNote: better table support than Microsoft ever shipped (Theme 1,
  id=1559179407967653970); ruler and insertable shapes/graphs (id=1560938022982131804);
  ink-to-shape and LaTeX rendering (id=1561448179705315450); notebook→section→page
  hierarchy (id=1559548216985391115 context); screen recording and voice recording,
  Member 3, id=1559764211280777287; the endless canvas and free placement (Theme 4).
- Obsidian: plugins, graph view (id=1563879907371647096); vault compatibility
  (id=1559374750780760075); file explorer, id=1559181487373287516; markdown native
  storage, Theme 5. "Obsidian is a must" — Member 79, id=1563907274668507196.
- Evernote: unmatched OCR, id=1559185202654351441.
- Notion: strong properties on notes + collaboration praised by a TTRPG user
  (id=1560471773701738557); Notion/Milanote/Miro features wanted, id=1559190485745139810.
- Workflowy-style collapsible bullet points, nested properties, and database-like views
  requested by a power user in the Oct 13-14 window (multiple messages; the export omits
  ids on two, one id present: id=1559471463298371605 thread context).
- LaTeX/STEM: "Please, just don't forget inline latex for the STEM notes", Member 1,
  id=1559629113432481973; project: "Latex is a good shout, adding that", id=1559629397579800609.
- Diagrams: native mermaid and Vega+D3 support claimed at 50% by a contributor.
  Member 47, id=1561625968890740807.
- AI/auto-organization: punch-anything-and-auto-organize vision (id=1559468612044070935);
  an email-watching assistant anecdote as the mental model for proactive AI
  (id=1559764211280777287 thread context; content in transcript, no id on that line).
- Voice notes and video capture (id=1559764211280777287; Theme 3).

## Theme 12 — Migration, import/export, data ownership

- ".one file support?" asked directly. Member 20, id=1560455675006554113. Mac OneNote's
  inability to load local .onepkg files cited as a pain point. Member 1, id=1559485968023556158.
- "it will soon import all my notes from the last 15 years and it already supports RTL" —
  Member 3 on the prototype's promise, id=1561447966965768224.
- Import/export in and out of "any file format or software" on the wish list (Theme 6,
  idless message near id=1559471463298371605). PDF export shipped in one community
  prototype, Member 42, id=1562440033825202347.
- Data ownership sentiment: a contributor building their own OneNote replacement says
  they hate OneNote's closed format and want to own their data; contributor status
  report: themes, page source view, RTL at 75%, mermaid/Vega+D3 50%, OneNote import 10%.
  Member 47, id=1561625968890740807 and thread context.
- Right-to-left (Arabic) language support as a first-class need. Member 47,
  id=1561447966965768224, id=1561625968890740807.

## Theme 13 — Pricing, licensing, trust

- Goodnotes "costs a monthly premium" and is iPad-exclusive; the lack of good free note
  apps on tablets is the gap. Member 28, id=1559920059684622367.
- Samsung Notes pitched as the free, feature-complete benchmark app. Member 28,
  id=1559970778634653816; two benchmark pathways spelled out (Samsung Notes parity first
  vs Goodnotes completeness first). Member 28, id=1559971549530816514. Goodnotes' free
  trial noted as a testing path, id=1560361658013057085; popularity evidence via App
  Store listing, id=1560362533267832883.
- Concepts and Noteshelf-Android flagged as paid and proprietary; Concepts described as
  infinite-whiteboard-first, not note-taking. Member 3, id=1562988208508108863; Member 28,
  id=1563209109912948828. "is noteshelf better than goodnotes?" — Member 86,
  id=1563214688945311825; "Never tried it, but it seems close", Member 3,
  id=1563302566014754969.
- Open source as non-negotiable in the handwriting lane: "Of course it has to be open
  source as well" (Goodnotes/Amphi/NoteShelf context). Member 3, id=1564165005589356648.
- Open-source status of Obsidian itself disputed in-thread: "Obsidian is NOT open source",
  Member 28, id=1564225771495755867, vs earlier "Just not open source", id=1559195024812417056
  and "Obsidian is already free and open source", id=1564069154519121971. The export shows
  the community never settles this; recorded as a dispute, not a fact.
- Big-MS lock-in fatigue: 20-year Microsoft user citing OneDrive pricing/storage changes
  as the trigger to look elsewhere. Member 1, id=1559682075207139339.
- Licensing/weight complaints against alternatives generally: "most of them heavy on
  booting, closed license and One lacks features compared to the other" — Member 69,
  id=1563935446411645009.

## Theme 14 — Build-tooling and process signals

- AI-assisted development openly used and debated: a community builder credits
  Antigravity/Gemini for their Flutter app (id=1561434535265173564); AI policy in an
  upstream repo asked, Member 28, id=1563942080227836056; answered: AI use fine with
  review, maintainers reshape contributions, Member 88, id=1563942897332658319 and
  id=1563943967001673842. The community's own plan: assemble a research repo of findings
  and have AI "hack away at a list of features and requirements" before building.
  Member 3, id=1564240622246699159.
- Release cadence interest: nightlies requested early ("daily updates", Oct 13; no id in
  export); releases shared as they land — v0.0.6 announced, Member 47, id=1563902004299042909;
  "love seeing this develop", Member 28, id=1563941993019736066.

## Theme 15 — Apps, projects and tools the community mentions

- Obsidian — the baseline; free/mature (id=1559147620084088982), Electron objection
  (same), open-source status disputed (id=1564069154519121971 vs id=1564225771495755867),
  vault compatibility and sync as switching barriers (id=1559374750780760075,
  id=1559366167301197875), plugins/graph view to copy (id=1563879907371647096),
  InkedMark handwriting plugin tested (id=1564161475764031629, id=1564161562808287283).
- OneNote — main template: canvas, handwriting, OCR, tables, ruler, sections; .one
  format pain (id=1559179407967653970, id=1559181793557614593, id=1559182719504883813,
  id=1560455675006554113, id=1559485968023556158); Mac .onepkg failure (same).
- Evernote — OCR benchmark (id=1559185202654351441).
- Notion — properties/collaboration benchmark (id=1560471773701738557); many alternatives
  already exist (id=1563920349987479552).
- Goodnotes — the tablet-lane target: popular with students, iPad-only, subscription
  (id=1559920059684622367); free trial usable for testing (id=1560361658013057085);
  Android port failed/prototype (id=1560361815727145051); popularity evidence
  (id=1560362533267832883); grouped with Amphi/NoteShelf as the paid-proprietary trio
  (id=1559891346603647017, id=1564165005589356648).
- Samsung Notes — free benchmark for PDF editing and UI (id=1559970778634653816); one
  community prototype targets it (id=1562440033825202347).
- Squid — Android tablet app that "lacks many of the capabilities Goodnotes has"
  (id=1559920059684622367).
- Notesnook — simple, liked despite gaps (id=1559485000553074799); publishing model to
  copy (id=1559469931563851827).
- Trilium (triliumnotes.org) — shared as a project to study, dashboard compared
  (id=1559471463298371605, id=1559479080150106153).
- Joplin — Electron, no file explorer, considered not great (id=1559570226952011849,
  id=1559585411041460367).
- AFFiNE — "goes into that direction" as an open OneNote/Obsidian-ish clone; tried for
  ~3 seconds, not liked (id=1564226519163736075, id=1564228269811826731).
- Anytype — Notion alternative "becoming open source", rebuilding as "anytwo"
  (id=1559629397579800609).
- Miro / Milanote / Canva — whiteboard/canvas references (id=1559190485745139810,
  id=1560329273598804170).
- Figma, Maltego — UI/interaction references from the OSINT use case (Theme 4, no id).
- Workflowy — bullet-outlining pattern requested (Theme 11, no id).
- ente — local ML/OCR on photos cited as the privacy-respecting search model
  (id=1559187489862852610, id=1564159055742898196).
- InkedMark (Obsidian plugin) — pressure-aware ink as .ink.md, on-device TrOCR
  experimental (id=1564161475764031629, id=1564161562808287283, id=1564161919332519977).
- Saber — "sooo close but no recog" (id=1564163849207156857).
- Concepts — infinite-whiteboard app, paid/proprietary (id=1562988208508108863,
  id=1563209109912948828).
- Noteshelf 3 Android — paid/proprietary alternative (id=1562988208508108863,
  id=1563214688945311825).
- Amphi (useamphi.com) — in the tablet-app trio (id=1559891346603647017).
- OwlLuna — Apple-side handwriting app shared twice; "amazing project, just no android,
  windows, or, linux versions" (id=1563498680890429510, id=1564165162817032193,
  id=1563521663319015517).
- xnotes-android — FOSS Android notes app; an active contributor vouches for it
  (id=1563622664319406232, id=1563623145251020931).
- open-note (community member's Flutter repo, hasanmajid.github.io) — OneNote+Samsung
  Notes feature blend, stylus erase, palm rejection, PDF export, web deployment
  (id=1561434535265173564, id=1561435668696146076, id=1562440033825202347).
- CapsuleCraft — community project shared as now-good (id=1563843367102582845).
- Meridian / NoteCraft — the thread's own app: hybrid plan (id=1563879907371647096),
  release v0.0.6 (id=1563902004299042909), EML/HTML serialization work
  (id=1563791669600452691).
- Cryptomator — encryption pattern for cloud storage (Theme 6, no id).
- Tailscale/Netbird/Iroh — direct/P2P connection methods discussed (Theme 6/7 context).
- OfficeIMO — library floated for reading .one/.docx files (Theme 12 context, no id).
- Muse — a user's name for the imagined AI assistant watching emails (id=1559764211280777287
  context, no id on line).
- BasScript — a member's own screenplay-writing app, shared as context (no id in export).

## Theme 16 — Ambiguities and gaps in the record

- Two separate members demand OCR/universal search on adjacent messages and the export
  lost the id of one; the claim is double-sourced but only one id survives (Theme 3).
- The Workflowy/properties/database-views run (Oct 13-14) and the OSINT canvas run
  (Oct 15) are among the most detailed feature lists in the thread, but several of those
  messages carry no parseable id in this export; they are cited with "no id in export"
  rather than a guessed id. Re-run extraction on discord_raw.json against raw HTML if
  exact ids are needed.
- The community never resolves whether Obsidian is open source (Theme 13); treat all
  such statements as claims.
- Several "[] ?" messages in the export are image/attachment-only or bot lines and were
  not content-bearing for this digest.

---

## Top signals

1. A Rust-native, Electron-free notes app is the loudest, most-reacted demand (381
   reactions on the opening message; id=1559147620084088982), tied to low-spec hardware
   (id=1559173272585895998).
2. Freeform OneNote-style canvas with freely placed, resizable, layered text/image
   blocks, as a first-class mode (id=1559181793557614593, id=1559678678315835404).
3. Handwriting with stylus: pressure-aware ink, ink-to-shape, palm rejection, stored as
   plain files (id=1559182719504883813, id=1559517256814174261, id=1564161562808287283).
4. Searchable handwriting ON DEVICE: the stated deal-breaker for leaving OneNote
   (id=1564158608361521203), generalized to all content types locally
   (id=1564158856874037363, id=1559187489862852610).
5. OCR over images/PDFs/voice/video called "a must", with local ML as the model
   (id=1559185202654351441, id=1559187489862852610).
6. Markdown-native storage plus Obsidian vault compatibility as the adoption path
   (id=1559374750780760075, id=1560705590223835137).
7. A plugin system and graph view borrowed from Obsidian, with MCP interest
   (id=1563879907371647096, id=1559193206229573663, id=1559185385651699793).
8. Sync: plain .md files through the user's own cloud (Dropbox/OneDrive first), git sync,
   self-hosting, and encryption choice (id=1560705590223835137, id=1559359807851466885,
   id=1559548216985391115, id=1559470967233839117).
9. A Goodnotes-class open-source tablet/handwriting app: the whole second channel exists
   because Goodnotes is iPad-only and subscription-priced (id=1559920059684622367,
   id=1564017331196137484, id=1561398989742411778).
10. Android and iPadOS coverage with a native feel; skepticism of wrapper ports; Rust
    cross-platform interest (id=1564241549297061899, id=1564239938910683149,
    id=1561435668696146076).
11. Open source as non-negotiable, especially in the handwriting lane; goodnotes-class
    apps are paid and proprietary (id=1564165005589356648, id=1562988208508108863).
12. Migration is an entry barrier: .one/.onepkg import, 15 years of notes, export in any
    format (id=1560455675006554113, id=1559485968023556158, id=1561447966965768224).
13. Collaboration/multiplayer is wanted but feared as the thing "that kills every notes
    app"; publish-to-web like Notesnook asked (id=1560471773701738557,
    id=1560938022982131804, id=1559469931563851827).
14. Power-user structure features: LaTeX inline, tables, ruler, shapes, mermaid/Vega
    diagrams, RTL/Arabic support (id=1559629113432481973, id=1560938022982131804,
    id=1561625968890740807).
15. Interface pluralism: ribbon + file tree + handwriting-detection modes, user-picked
    UI, keep the core lean (id=1559906079931109557, id=1564097228308480031,
    id=1559185068633624577).
