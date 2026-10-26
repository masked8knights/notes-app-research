# Thread 3 digest — "Notion — a productivity and note-taking application" (Discord, 22 msgs, 12–27 Oct 2026)

Source: research-material/discord-thread3-transcript.txt (raw transcript, untracked; parsed JSON and links file alongside it).
All message ids are Discord snowflakes in [brackets]. Links from the thread: AFFiNE repo https://github.com/toeverything/affine, NoteCraft repo https://github.com/AlienTechSoftware/notecraft (discord-thread3-links.txt).

## A. Distinct wants, complaints, recommendations

### Wants: cloud storage backends
- member A wants Notion-like apps whose data lives on user-chosen consumer cloud drives (Google Drive / Dropbox / OneDrive) [1559185243280244787] (member A).

### Wants: no paywall / size limits
- member B wants Notion without the paywall and size limits [1559327100555497577] (member B).
- member C says Notion is far too expensive for his company, a reason he stays on Anytype [1564282566322946259] (member C).

### Want: self-hosted Notion (member D's full list)
- member D has looked for a self-hosted Notion for years; feature list he wants: notes, flowcharts ("flowchats" sic), mindmaps, planning tools, kanban boards, databases, wikis, charts, tables, web-clipper, markdown, block-based editing, collaboration, relations, "and much more" — the ideal tool for planning and documentation [1559566626729365628] (member D).

### Recommendation + experiences: AFFiNE (vs Notion)
- member E recommends AFFiNE (https://github.com/toeverything/affine) as an open-source cross of Notion and Milanote [1559637092391198803] (member E); a follow-up message says the author tried it, finds it very good, unsure if it fits the ask [1559637197148266627] (unnamed).
- member B has used AFFiNE but finds it missing many small Notion things she enjoys, which is why she wants Notion itself [1560002501154054237] (member B).
- member F asks what those small things are, weighing whether to try AFFiNE [1560245299811721247] (member F).
- member G notes AFFiNE's last release was two months old; a reply asks whether there was any announcement about it [1560336205793460315], [1560336242573447190] (member G, unnamed).
- member H tried both: AFFiNE still lacks some Notion functionality, specifically Excel-like in-cell functions [1561142319250669699] (member H).
- member C's detailed AFFiNE test (on-premise deploy) [1564282566322946259] (member C):
  - Missing: cannot create a database and show it in multiple views — the core Notion feature he needs (database/views separation).
  - Ambiguity on storage limit even when self-hosted on premise.
  - Cannot connect a local AI; only the main cloud AI providers.
  - What he loves in Notion: database and views separation, customizable changes, collaboration, page publication on the web.
  - His use case: project management — a projects-and-tasks database with many tags, viewed per project or per person.
- member J asks "Affine?" when member C describes the Anytype-UX wish [1564247051296837686], admits never having tried it, just keeps seeing it recommended [1564249806543528127] (member J); member C says he will try it and later reports back [1564249683218661500], [1564282566322946259]; member J says he will look into it himself [1564282737173467308].

### Architecture suggestion: local-first + relay (p2panda)
- member I suggests the app could be local-first with a relay; he uses p2panda with great success for his Discord-like app [1559923956251631708] (member I).

### Broader mashup thread pointer
- member J points to a separate thread mashing up Obsidian/Notion/Miro/Evernote/OneNote, canvas and handwriting features, inviting people to add requests there [1559549980551942232] (member J).

### Want: Notion meets QuickBase, integrated
- member K wants something like Notion meets QuickBase in a single shell, with a cloud backend and online/offline API syncing, integrating with other tools; he is researching that [1561232352557011065] (member K).

### member L's full requirements list for a note app ("NoteCraft")
Posted as what he needs before he can call any app his note app [1561320411231162410] (member L):
- Paragraph-level links: link a paragraph in one note to another note, not just page-to-page; links must survive moving the note.
- Local backup, with an encryption option.
- Automatic backup in a readable format so he knows he will never lose his notes.
- Sync to other devices; he needs to capture notes on the phone when ideas come.
- Export to a standard format: anti-lock-in; some apps deliberately hinder export, and standard-format export makes import into other apps easy.
- Basic functionality: checkboxes, images, changing text color.
- Notes completely private, even when synced between devices.
- Code formatting that renders neatly and readably.
- Nice to have: chat with your notes via AI.

### Repo shared in reply to member L
- member M posts https://github.com/AlienTechSoftware/notecraft ("NoteCraft" referenced by member L) [1561439372471959712] (member M).

### Want: Anytype + Notion UX
- member C: "A Notion on premise like Anytype but with Notion UX would be gold" [1564246090033668229] (member C).

### Signals of stalled / substitute-tool market
- member B returned to wanting Notion itself despite AFFiNE [1560002501154054237]; member C stays on Anytype because AFFiNE lacks view separation and Notion is too costly [1564282566322946259] — an unmet-product gap for a self-hostable Notion-class app.

## B. Repo research: voice notes / TTS resources

### 1. Lukas-Novak/diktafon (fork of jaromiru/diktafon)
- What it is: an open-source voice-memo app organized like cassette tapes; each topic is a cassette that plays as one continuous chronological tape. Transcription and summarization run entirely on device; this fork adds opt-in cloud backup and opt-in cloud transcription to a self-hosted receiver (diktafon-ingest), off by default https://github.com/Lukas-Novak/diktafon <cite index="ye6-1"></cite>
- Platform/language: Flutter app (Flutter 3.44.5 pinned) shipping Android (7.0+, arm64/x86_64 APKs), iOS (13.0+), and Linux desktop (x64 tarball); transcription by vendored whisper.cpp, summaries by vendored llama.cpp (Qwen), Silero VAD for voice-activity detection; distributed via F-Droid, Google Play, App Store and GitHub releases https://github.com/Lukas-Novak/diktafon <cite index="ye6-1"></cite>
- License: MIT (repo README, incl. vendored engines' licences documented in LICENCE.md) https://github.com/Lukas-Novak/diktafon <cite index="ye6-1"></cite>
- Feature list from README: one-tap capture with no setup or network; tap-to-seek transcripts (tap a word, tape jumps there); per-memo one-sentence gist, per-cassette summary and suggested titles; noise-aware transcription via VAD plus rumble filter, original audio untouched; gapless "tape illusion" playback with color-coded segment bar and optional chime at memo boundaries; per-memo spoken-language auto-detection (cassettes may mix languages); export/import of cassettes as a single archive with audio plus readable text, additive import; light/dark themes, cassette color labels, retranscribe-cassette, per-memo copy/delete; on-device models downloaded once at first run and switchable in Settings https://github.com/Lukas-Novak/diktafon <cite index="ye6-1"></cite>
- Release v1.1.1 (https://github.com/Lukas-Novak/diktafon/releases/tag/v1.1.1): fixes three compounding bugs where cloud transcripts never returned to the tape (duplicated /diktafon/v1 URL prefix causing 404; queue re-POSTing full audio with fresh request_id instead of resuming, causing duplicate server transcriptions every ~30 min; foreground drain gating cloud jobs on a local model being provisioned); adds transcription-location setting (phone or cloud via diktafon-ingest); explicit per-memo cloud fallback after failed local transcription with a consent dialog naming destination, duration and size; durable request-id uploads resumable across app kill and reboot; server-side diktafon-ingest v1 protocol with SQLite-backed jobs, retention policy (keep_audio_on_server default false), lease claims across containers, atomic result publication, Idempotency-Key-notified webhook; renames the upload feature "Cloud backup" across 20 locales; privacy copy now makes the "never leaves this device" promise conditional on consent https://github.com/Lukas-Novak/diktafon/releases/tag/v1.1.1 <cite index="5mc-1"></cite>
- What people like: the upstream on-device-only privacy design is why one contributor uses it (stated in the feature-request issue https://github.com/jaromiru/diktafon/issues/27 <cite index="kvr-5"></cite>); the fork's upload feature originated as a feature request with a working implementation proposed to upstream https://github.com/jaromiru/diktafon/issues/27 <cite index="kvr-5"></cite>
- What people want changed (issues, with URLs):
  - Fork issue #1: v1.1.2 should make Cloud backup truly back up everything (summaries, cassette artifacts, retention) per a 2026-10-01 design decision https://github.com/Lukas-Novak/diktafon/issues/1 <cite index="kvr-1"></cite>
  - Upstream issue #27: opt-in upload of finished memos to a user-configured server (implemented in this fork's v1.0.9...v1.1.0-server-upload range) https://github.com/jaromiru/diktafon/issues/27 <cite index="kvr-5"></cite>
  - Play Store user feedback: wants a widget, tap-and-hold to copy the summary, and reports slow/unpredictable transcription times for 15-minute audio https://play.google.com/store/apps/details?id=cz.mod42.diktafon&hl=en_US <cite index="kvr-10"></cite>
  - diktafon-ingest repo issues include a README section request for webhook-out configuration (consumer wiring for outgoing notifications, e.g. an Alfred pipeline subscriber) https://github.com/Lukas-Novak/diktafon-ingest/issues/1 <cite index="kvr-3"></cite>
- Pull-from assessment for a local-first Rust notes app: license MIT, so code and concepts are fully compatible with a Rust app. The Flutter/Dart UI cannot be lifted directly, but the product patterns are directly reusable: cassette-style chronological capture, tap-to-seek word-level transcripts, VAD-gated transcription (no phantom words), mixed-language auto-detection, additive export archives pairing audio with readable text, and the cloud-optional design (everything local by default; opt-in sync to YOUR server with durable resumable request-id uploads, consent dialogs, and a SQLite job/retention/idempotency ingest protocol) https://github.com/Lukas-Novak/diktafon <cite index="ye6-1"></cite> https://github.com/Lukas-Novak/diktafon/releases/tag/v1.1.1 <cite index="5mc-1"></cite> For Rust, whisper.cpp and llama.cpp are reachable through existing bindings (whisper-rs etc.), and the v1.1.1 release notes show the exact failure modes (URL duplication, re-upload on retry, model-gating cloud jobs) a Rust implementation must design around https://github.com/Lukas-Novak/diktafon/releases/tag/v1.1.1 <cite index="5mc-1"></cite> The diktafon-ingest receiver spec (jobs, leases, retention default false, notify events with Idempotency-Key) is a ready-made blueprint for the notes app's optional self-hosted sync receiver https://github.com/Lukas-Novak/diktafon/releases/tag/v1.1.1 <cite index="5mc-1"></cite>

### 2. maxwhipw/marmalade-tts-android
- What it is: a native Android system text-to-speech engine with on-device neural voices and emotion-aware prosody; sister project to the Linux CLI marmalade-tts; positions itself as the middle ground between Google's data-hungry default and robotic FOSS engines https://github.com/maxwhipw/marmalade-tts-android <cite index="du3-1"></cite>
- Platform/language: Android; implements the standard Android TTS interface as a drop-in replacement for Google/Samsung TTS. Rust is evidenced in crash logs from a consuming app ("RustStdoutStderr" unwind, issue #5) https://github.com/maxwhipw/marmalade-tts-android/issues/5 <cite index="gop-5"></cite>; exact language split (Kotlin vs Rust) is not stated in the README — UNVERIFIED beyond the Rust log evidence. Repo shows 21 stars, 2 forks (from issue page header) https://github.com/maxwhipw/marmalade-tts-android/issues/5 <cite index="gop-5"></cite>
- License: source files MIT with no GPL code in the repository; however the released APK compiles in espeak-ng (GPL-3.0-or-later) so the distributed APK is a GPL-3.0-or-later combined work (a Google Play requirement); third-party licenses browsable in-app and in NOTICE.md/LICENSES/ https://github.com/maxwhipw/marmalade-tts-android <cite index="du3-1"></cite>
- Feature list from README: natural ready-to-speak neural voices; fast on modest phones; private by default (all on device); optional cloud voices strictly opt-in via your own API key (Venice.ai and OpenAI in the list); per-app voice routing with aliases tying a voice to speed and effect settings; 8 languages with auto language detection on the Kokoro engine; TalkBack accessibility support targeting WCAG 2.1 AA; 22 voice-effect presets plus an editor; foreground playback service for long text with lock-screen and Bluetooth controls; share-to-speak and system "read selection"; install via F-Droid (recommended, reproducible builds), GitHub Releases, or Obtainium https://github.com/maxwhipw/marmalade-tts-android <cite index="du3-1"></cite>
- Engines: a fast English voice (Kitten Nano) is built into the APK so it speaks offline from first launch; bigger engines download on demand from hostnames pinned in a catalog into app-private storage; details in PRIVACY.md https://github.com/maxwhipw/marmalade-tts-android <cite index="du3-1"></cite>
- What people like: a user calls it "great app, one of the better TTS apps out there so far" (issue #21) https://github.com/maxwhipw/marmalade-tts-android/issues/21 <cite index="gop-2"></cite>; active issue traffic with rapid owner responses and quick follow-up releases (issues #24 owner reply noting fixes shipped in 1.2/1.3) https://github.com/maxwhipw/marmalade-tts-android/issues/24 <cite index="gop-6"></cite>
- What people want changed (issues, with URLs):
  - Speech rate other than 100% sounds vibratey/robotic (#21) https://github.com/maxwhipw/marmalade-tts-android/issues/21 <cite index="gop-2"></cite>
  - Voices distorted at playback speeds other than 1.0 after the 1.1.0 update; reported fixed in 1.2/1.3 (#24) https://github.com/maxwhipw/marmalade-tts-android/issues/24 <cite index="gop-6"></cite>
  - Crash with German Thorsten voice, no speech (Android 12, LG V60) (#20) https://github.com/maxwhipw/marmalade-tts-android/issues/20 <cite index="gop-3"></cite>; Thorsten still failing in-app on Android 16 (#25) https://github.com/maxwhipw/marmalade-tts-android/issues/25 <cite index="gop-8"></cite>; German synthesis fails with a "y1.j" message on any Kokoro model (#29) https://github.com/maxwhipw/marmalade-tts-android/issues/29 <cite index="gop-10"></cite>
  - Feature request: on-device German Pocket TTS engine (checkpoint and embeddings exist upstream), motivated by German users having only one native engine (#30) https://github.com/maxwhipw/marmalade-tts-android/issues/30 <cite index="gop-9"></cite>
  - Routing broken after deleting an alias: re-routing a different alias to that app impossible without clearing app storage (#32, Marmalade 1.3.3, Android 16) https://github.com/maxwhipw/marmalade-tts-android/issues/32 <cite index="gop-4"></cite>
  - OneUI: users cannot find how to set Marmalade as default voice input for other apps (#26) https://github.com/maxwhipw/marmalade-tts-android/issues/26 <cite index="gop-1"></cite>
  - A consuming app (read_later) crashed calling TTS, Rust unwind in log (#5, closed) https://github.com/maxwhipw/marmalade-tts-android/issues/5 <cite index="gop-5"></cite>
- Pull-from assessment for a local-first Rust notes app: this is a system-wide TTS engine, not voice-note capture, so its role is the playback/read-back side. The liftable ideas: on-device neural TTS with a small built-in voice plus larger downloadable engines from pinned hostnames into private storage; per-app/alias voice routing; privacy.md-grade disclosure separating on-device, downloadable-models-only, and opt-in cloud (API-key) paths https://github.com/maxwhipw/marmalade-tts-android <cite index="du3-1"></cite> License-wise the source is MIT, compatible, but any lift that includes espeak-ng (phonemizer) drags in GPL-3.0-or-later for the combined work; an MIT-pure Rust TTS path should avoid espeak-ng and either use a permissively-licensed phonemizer or ship model+phonemizer-data-only downloads the way Marmalade's engine catalog does https://github.com/maxwhipw/marmalade-tts-android <cite index="du3-1"></cite> Rust appears in its runtime logs https://github.com/maxwhipw/marmalade-tts-android/issues/5 <cite index="gop-5"></cite>, so engine-side Rust precedent likely exists, but which components are Rust is UNVERIFIED from the README. Its German-voice quality issues (#20, #25, #29) also show the testing burden of multi-engine on-device TTS https://github.com/maxwhipw/marmalade-tts-android/issues/29 <cite index="gop-10"></cite>

### Cross-cutting takeaway for the notes app
- Thread demand converges on: self-hostable/local-first Notion-class app, no paywall or size limits, user-chosen storage (consumer clouds or own server/relay), database-views separation, paragraph-level durable links, readable+encrypted backups, standard-format export, phone sync with privacy preserved in transit, and optional AI (local AI preferred over cloud-only). Diktafon shows how voice capture + on-device transcription + optional self-hosted sync can be packaged MIT-licensed; Marmalade shows how private on-device TTS playback can ride a standard platform interface.
