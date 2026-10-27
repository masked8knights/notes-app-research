# Features Master: every note app, every feature, in depth

One table per app; each row is one claim with its source.

Compiled from all findings files in `research-material/findings/`. One section per app, then per open-source repo, then integration components, then two synthesis sections. Every claim carries its source findings file(s). Nothing here is invented; where a finding was marked UNVERIFIED in the source, that is carried through.

Conventions: every app and repo section uses the same groups in the same order: **Features** (Area | Detail), **Sentiment** (What people say), **Wants** (What people want changed), and **Pricing and platforms** (Item | Detail); empty groups are omitted. One row is one claim. A findings-file Sources line sits under each section; URLs, UNVERIFIED markers and fact-check notes are appended in parentheses at the end of the row they belong to.

---

# PART I: APPS

## Goodnotes

### Visual surface
- iOS/iPadOS (primary): notebook-grid library ("Landing page") with cover thumbnails, then a paper-editor with toolbar: pen/highlighter/eraser/lasso/shape/text/image tools, tool-color tray, and a dropdown of paper templates; a left sidebar (thumbnails/outline/bookmarks) and split-view support. The marketing site shows the editor with the new AI sidebar and dynamic templates (https://www.goodnotes.com/features, https://www.goodnotes.com/pricing).
- macOS: same document model (notebooks, text documents, whiteboards) in a windowed app; users report page-switch lag on Mac (https://www.reddit.com/r/GoodNotes/comments/17j3tld/is_goodnotes_6_really_that_bad/).
- Android/Windows/web: cross-platform app with core note-taking and PDF markup, sync via Goodnotes Cloud on Pro (https://www.goodnotes.com/pricing).

### Docs analysis
- Free plan: up to 3 files total across notebooks/text docs/whiteboards, 5 MB import size, 20 min audio recording per notebook, watermarked exports, up to 3 folders; notebooks above 3 become read-only (editable ones user-chosen) — https://www.goodnotes.com/pricing and https://support.goodnotes.com/hc/en-us/articles/13808767840015-Compare-Goodnotes-Plans-and-Features (snippet via search; page itself blocked 403)
- Plans: Free $0; Essential $11.99/yr (unlimited files/audio, no watermark, basic AI); Pro $35.99/yr (private link sharing, hosting real-time collaboration, cross-platform cloud sync, advanced AI incl. Meetings and Create Mode); AI Pass +$9.99/mo (~12x more AI credits); Special Edition one-time purchase on Apple only (no Goodnotes Cloud, limited AI); Teams $120/seat/yr (SAML SSO, domain control, admin console); Enterprise custom — https://www.goodnotes.com/pricing
- AI split: on-device no-credit features (Math conversion, Circle to Lasso, Spell check, Handwriting reflow, Convert to text, Scribble-to-erase) vs credit-based cloud AI (Ask Mode, quiz generator, Meeting AI, image generation) — https://support.goodnotes.com/hc/en-us/articles/10779112528399-A-guide-to-Goodnotes-AI
- Math AI is powered by Wolfram|Alpha LLM API with Solve/Teach Me modes — https://support.goodnotes.com/hc/en-us/articles/13683534670223-Goodnotes-AI-for-Math
- Study Sets with spaced-repetition "Smart Learn"; AI does not auto-generate flashcards from notes (third-party claim analysis) — https://studycardsai.com/blog/can-goodnotes-convert-notes-into-flashcards (UNVERIFIED against official docs; support.403)
- Layers is an experimental feature, iPad/Mac only, disabled during Pro trial; Education tier (Schools): teaching-only presentation layer, class folders, feedback mode, AI safety controls; security posture SOC 2 Type 2, ISO 27001, GDPR/CCPA — https://www.goodnotes.com/pricing
- R12 correction: pricing re-architected vs the R8-cached model — a Free tier now exists, Essential/Pro annual pricing is confirmed, a Teams tier ($120/seat/yr) was added, and the Special Edition is a region-variable Apple one-time purchase rather than the R8-recorded flat $29.99 FAQ-only listing.
- Design decisions worth borrowing: editable-vs-readonly graceful degradation above the free quota; split of on-device vs credit AI; "elements tool" (reusable sticker/clips); presentation mode with pointer; collaborative link sharing gated by host tier.

**Features**
| Area | Detail |
|---|---|
| Capture/ink | Pen and highlighter with ink smoothing; ink rendering tuned per device; pressure sensitivity (iOS); shape recognition |
| Canvas/ink | PDF and image annotation; "infinite-ish" paper templates; lasso; links between notes; handwriting reflow; scribble-to-erase |
| Editing | Handwriting OCR search and conversion; handwriting spellcheck/completion (AI-driven in Goodnotes 6, on-device, no credits) |
| Study | Study Sets flashcards, spaced repetition "Smart Learn", quiz generator, Math Assist/conversion (Wolfram|Alpha LLM) |
| Audio | Audio recording alongside notes (20 min free / unlimited paid); transcription on iOS |
| Organization | Notebooks, folders (3 free), text documents, whiteboards, bookmarks/outline; Marketplace content (stickers, planners) |
| Collaboration | Link sharing, comments, real-time collab (hosting = Pro) |
| Sync | iCloud sync; Google Drive/OneDrive/Dropbox backup; Goodnotes Cloud cross-platform sync on Pro |
| Export | PDF export (watermarked on free) |
| Platform | iOS, macOS, Android, Windows, web |

**Sentiment**
| What people say |
|---|
| Handwriting search across notes plus audio recording "coupled with writing notes" was used by a user through years of law school; handwriting search praised as the killer feature vs competitors (https://www.reddit.com/r/GoodNotes/comments/1bhrpnz/is_goodnotes_6_worth_it_for_new_users/) |
| Links, lasso, and the broad feature set were called the best among iPad notebooks; rated the most user-friendly iPad notebook with the best handwriting-box search for students. |
| G2 reviewers praise quick capture that can be developed later and a laser pointer for presentations. |
| The AI ink-smoothing actually deforms handwriting for some users, tied to Apple Pencil hover behavior; AI outputs arrive in a generic typed font instead of handwriting, a recurring irritation. |
| Massive anger at the GoodNotes 5→6 forced upgrade to subscription; "the last solid one-time purchase notes app" betrayal narrative (https://www.reddit.com/r/GoodNotes/comments/15mnzfk/dont_upgrade_to_goodnotes_6/) |
| Family Sharing not supported by subscription — parents of multiple kids refuse to upgrade (https://www.reddit.com/r/GoodNotes/comments/15n3yv2/raise_your_voice_impact_goodnotes_6_with_app/) |
| Stability/performance complaints: freezing, crashes on older iPads, Mac page-switch lag; some reverted to GN5; sync complaints exist even for iCloud users (https://www.reddit.com/r/GoodNotes/comments/17j3tld/is_goodnotes_6_really_that_bad/, https://www.sikayetvar.com/en/goodnotes-us) |
| Distrust of future pricing after the 5→6 pattern; the subscription-family argument seen as hypocritical because Goodnotes had publicly mocked Notability's subscription switch (https://www.reddit.com/r/GoodNotes/comments/1cv93w7/imo_goodnotes_6_is_untrustworthy_and_you_should/) |

**Wants**
| What people want changed |
|---|
| Ink that never rewrites what you wrote (auto-correcting smoothing off); forced handwriting completion/spellcheck should be optional. |
| A genuine lifetime one-time purchase across platforms, not Apple-only Special Edition (https://www.reddit.com/r/GoodNotes/comments/15nfw1o/goodnotes_6_pricing_and_subscription_model/) |
| Family-shareable license (https://www.reddit.com/r/GoodNotes/comments/15n3yv2/raise_your_voice_impact_goodnotes_6_with_app/) |
| Performance fixes on Mac and older iPads (https://www.reddit.com/r/GoodNotes/comments/17j3tld/is_goodnotes_6_really_that_bad/) |
| Fewer AI features nobody asked for, more core writing reliability; AI output rendered in handwriting rather than typed font (https://www.reddit.com/r/GoodNotes/comments/15oklbw/goodnotes_6_is_fundamentally_wrong_its_simply_an/) |
| Subscription/price creep ("too expensive for how buggy it is"); Windows tiers feel pricey; an end to UI/UX churn ("we don't need new features"). |

**Pricing and platforms**
| Item | Detail |
|---|---|
| Free | 3 files, 5MB imports, 20-min audio, watermark, 3 folders |
| Essential | $11.99/yr, 7-day trial |
| Pro | $35.99/yr (cross-platform sync, collab hosting) |
| AI Pass | +$9.99/mo, ~12x AI credits |
| Special Edition | Apple one-time purchase, varies by region (previously recorded as a flat $29.99, FAQ-only listing) |
| Teams | $120/seat/yr; Enterprise custom |
| Platforms | iOS, macOS, Android, Windows, web (previously iPad/macOS/Windows/web; Android now included) |
| Closed source | |

R12 correction: the R8/R11-cached pricing (Essential/Pro only, $29.99 Special Edition, no Free tier, no Android) is superseded by the 2026 ladder above — a Free tier and Teams tier now exist and Android is a supported platform.

### Contradictions
- Goodnotes publicly criticized Notability's 2019 subscription switch, then moved to subscription itself with GN6 (https://www.reddit.com/r/GoodNotes/comments/1cv93w7/imo_goodnotes_6_is_untrustworthy_and_you_should/). The "current Goodnotes is free for GN5 users" claim in one 2026 review (https://paperlike.com/blogs/paperlikers-insights/app-review-goodnotes-vs-notability) sits awkwardly against the paid Essential/Pro tiers now on the pricing page — the 2026 pricing is a re-architected model, not the 2023 launch one.

Sources: apps-likes-wants.md ; findings/r12-enrich-a.md

## Notability

### Visual surface
- iPad/iPhone: a Home tab (recent notes, records, imports), a horizontal-scrolling note editor where each "note" is one tall page you scroll sideways, right-side toolbox bar (pen/highlighter/eraser/text/photo/record/lasso), and the signature audio timeline strip under the note that shows synced playback with handwriting animation. App Store copy confirms PDF/doc import, form fill, real-time transcription (https://apps.apple.com/us/app/notability-smarter-ai-notes/id360593530).
- Mac: same document model; users report copy-paste being finicky (https://www.softwareadvice.com/productivity/notability-profile/).
- Web: a web version in beta, still weak — sync and subscription recognition failed in testing (https://beingpaperless.com/notability-15-review-is-it-worth-it/).

### Docs analysis
- Free Starter: 5 free notes, all editing tools, PDF/doc import, 20,000+ templates, 7-day version history (https://notability.com/pricing)
- Individual tiers: Lite $11.99/yr (unlimited notes, iOS-only third-party backups); Plus $15.99/yr (limited AI: YouTube link-to-note, quizzes/flashcards, transcription; 30-day history); Pro $79.99/yr (unlimited transcription/summaries, chat with notes, 90-day history) (https://notability.com/pricing)
- Business: $60/user/yr and Business Pro $180/user/yr with shared libraries, live collaboration, Intune MAM, audit log (https://notability.com/pricing)
- Audio is the anchor: recording synced to handwriting; playback re-draws strokes per pixel; text syncs per second (https://beingpaperless.com/notability-2/)
- Live collaboration and cross-device sync run on "Notability Cloud"; handwriting recognition and math-to-LaTeX are iOS/Android only per the plan matrix; version history is a paid differentiator: 7 days free, 90 days Pro (https://notability.com/pricing/compare)
- Fall 2026 additions: Calligraphy Pen, flashcard import from Anki/CSV, updated academic planner, AI quizzes on the Learn Home Screen (https://blog.notability.com/post/notabilitys-back-to-school-2026-guide-every-new-feature-explained)
- Study chapters from a specific PDF chapter rather than whole docs; edits sync instantly for collaborators (UNVERIFIED: "instant" sync claim is marketing) (https://blog.notability.com/post/whats-coming-to-notability-this-semester)
- Design decisions worth borrowing: per-pixel handwriting playback against audio; version history as a tier ladder; chapter-scoped AI; Home tab that mixes notes/recordings/imports.

**Features**
| Area | Detail |
|---|---|
| Capture/ink | Handwriting: pencil/pen/highlighter, Calligraphy Pen (Fall 2026), multi-note split view, math→LaTeX (iOS/Android) |
| Canvas/ink | PDF and image annotation, doc/slide import, scan paper, form fill |
| Audio | Recording time-linked to ink: tap a stroke to jump to that moment; playback re-draws strokes per pixel; annotations made during playback sync back into the timeline; live transcription with per-plan limits |
| AI | Smart Notes summaries, quizzes/flashcards (Anki/CSV import), YouTube link-to-note, chat with notes |
| Organization | Folders, handwriting search, shared libraries |
| Collaboration | Link sharing, live collaboration (Notability Cloud) |
| History | 7/30/90-day version history by tier |
| Sync | iCloud sync |
| Export | PDF export; export as PDF+audio zip |

**Sentiment**
| What people say |
|---|
| Time-synced audio is the signature: audio synced to notes called "LIFE CHANGING" for lectures; audio-synced playback remains the most-praised feature (https://paperlike.com/blogs/paperlikers-insights/app-review-goodnotes-vs-notability, https://www.reddit.com/r/ipad/comments/1d8e9of/a_quick_reminder_that_you_shouldnt_use_or/) |
| Tapping written text jumps the audio to that moment. |
| Minimalist interface people explicitly say they love; several ex-Goodnotes users call it the best handwriting experience. |
| The 2021 switch from one-time purchase to subscription is the defining grievance of the app's community, with users demanding refunds; the Plus relaunch in 2024 ("era of bought-for-life Notability is over") and repeated "remove required paid subscription" threads continue the pattern. |
| "Worst pricing setup" criticism for a handwriting app in 2025/26; the web version is not ready (https://beingpaperless.com/notability-15-review-is-it-worth-it/) |
| Data loss reports during device migration; iCloud sync unreliable with multi-day transfers; a student reports losing a week of notes before an exam with no recovery (https://www.reddit.com/r/notabilityapp/comments/1o357au/whats_the_upsides_and_downsides_of_notability/) |
| Notes failing to load reported; copy/paste finicky in reviews of the desktop experience (https://www.softwareadvice.com/productivity/notability-profile/) |
| Heavy moderation/censorship of complaints on their subreddit; the "Classic Plan" restore path was reported broken. |

**Wants**
| What people want changed |
|---|
| Pay once and keep everything — a trustworthy lifetime/one-time option that doesn't break on device migration (https://www.reddit.com/r/notabilityapp/ — migration thread) |
| Never hold sync hostage behind a subscription; reliable sync and recovery for lost notes (https://www.reddit.com/r/notabilityapp/comments/1o357au/whats_the_upsides_and_downsides_of_notability/) |
| Restored playback-speed toggle on the timeline (regression in v14) (https://medium.com/@paperlessx/notability-15-review-is-it-worth-it-b7d2c0a39e7b) |
| Honor the Classic plan; stop repeated re-subscription pushes. |

**Pricing and platforms**
| Item | Detail |
|---|---|
| Starter | Free, 5 notes |
| Lite | $11.99/yr |
| Plus | $15.99/yr |
| Pro | $79.99/yr |
| Business | $60/user/yr; Business Pro $180/user/yr |
| Platforms | iOS, macOS, web (beta); handwriting recognition iOS/Android only |

R12 correction: the cached plan ladder (Free/Classic/Plus, iPad/Mac only) is superseded — the 2026 lineup is Starter/Lite/Plus/Pro/Business with a $79.99/yr Pro tier, a web beta, and Android handwriting recognition; earlier recorded prices (one-time $9.99 era, $14.99 Pro annual) no longer match.

### Contradictions
- The 2019 pivot made Notability a "free app with optional subscription" (https://blog.notability.com/post/pricing-updates), but the current compare page shows a freemium Starter limit of 5 notes (https://notability.com/pricing/compare) — the "free" promise eroded. Earlier recorded prices no longer match the 2026 ladder; treat all cached pricing as stale.

Sources: apps-likes-wants.md ; findings/r12-enrich-a.md

## Noteshelf

### Visual surface
- iPad/iPhone: shelf-style library with notebook covers and groups; editor with a bottom tool tray and the zoom box for writing, customizable covers and templates (Noteshelf 3 redesign). Windows build is tuned for stylus devices and preloaded on Samsung Galaxy Book2/Book3; Android listing highlights the AI panel; macOS carries the template library and iCloud sync.

### Docs analysis
- Support portal covers Windows/Android/Mac: Google Drive sync across Android and Windows devices, Noteshelf AI on Windows, lasso-based handwriting-to-text OCR, groups and printing.
- Apple pricing: Noteshelf 3 is a $7.99 universal one-time purchase across iPad/iPhone/Mac; Noteshelf 3 is a separate app from Noteshelf 2 (repurchase required). Android model: free with limited functionality plus a small one-time premium fee. Sync silos: Google Drive for Android↔Windows, iCloud for Apple devices; no cross-ecosystem sync. Audio records on all platforms but has no synced playback to notes.
- Design decisions worth borrowing: zoom box with auto-advance as a first-class writing aid; device-ecosystem sync silos vs one account; Samsung preload partnerships as distribution.

**Features**

| Area | Detail |
|---|---|
| Capture/ink | Handwriting with tuned pen pressure and ink rendering; zoom box with auto-advance; palm rejection. |
| Editing/canvas | Templates (large packs, covers, planners). |
| Audio | Audio recording on all platforms; no synced playback to notes. |
| Export | Vector PDF export. |
| Integration | Evernote push. |
| Editing | Handwriting OCR search and conversion. |
| AI | Noteshelf AI: study notes, page summarization, translate, explain (Android/Windows included). |
| Media | Image crop/erase/resize, Pixabay stock images. |
| Sync | Google Drive (Android/Windows), iCloud (Apple), Dropbox backup. |

**Sentiment**

| What people say |
|---|
| Fountain-pen ink rendering is the standout: "only app to produce a decent fountain pen and my handwriting looks the best". |
| Fountain-pen rendering rated on par with Samsung Notes. |
| Vector PDF export is the deciding feature over Samsung Notes for some users. |
| Best-in-class writing feel with S Pen on Galaxy Tab: responsiveness and palm rejection. (R12) |
| Paid Noteshelf 2 "lifetime" buyers had to pay again for Noteshelf 3, a lifetime-promise breach pattern the findings flag as a caution for the new app. |
| Sync errors and lost information on Mac/iPad reported in Noteshelf 3. (R12) |
| Premium "for life" users report subscription prompts: "premium was meant to be for life". (R12) |
| Noteshelf 3 removed v2 conveniences (multi-page view, page-corner handles) while adding AI. (R12) |
| Migration from v2 to v3 smooth for some, messy for others. (R12) |

**Wants**

| What people want changed |
|---|
| True lifetime ownership (no paid v3). |
| Catch up on feature lag versus rivals. |
| Stronger cloud backup. |
| Fix bugs (annotations disappearing, tour restarting every launch, scrolling lag, no web preview). |
| Bring the Android version to parity with iPad. |
| Synced audio playback tied to notes — the top missing feature. (R12) |
| Restored v2 page-navigation conveniences. (R12) |
| Cross-ecosystem sync without paying twice. (R12) |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | iPad/iPhone/macOS/Android/Windows. |
| Business | Apple: $7.99 universal one-time purchase for Noteshelf 3 (2026). Previously a paid Noteshelf 2 with a second repurchase at v3. |
| Business | Android: freemium, free with limited functionality plus a small one-time premium fee (2026). |
| Business | Windows: one-time purchase; preloaded on Samsung Galaxy Books. |

### Contradictions
- "Premium for life" marketing vs subscription prompts observed by a premium user. Also, an older claim that Windows "can't sync or even import notes from iOS" is now partially superseded: Google Drive sync Android↔Windows exists, but Apple↔Windows sync still does not. R12 correction: pricing and platform coverage re-verified in 2026 — the cached "iPad/Android/Windows" row now reads $7.99 universal one-time on Apple plus freemium Android, and AI features exist on Android/Windows.

Sources: apps-likes-wants.md ; findings/r12-enrich-a.md

## Amphi

### Visual surface
- (b) Amphi canvas app: iPad-only study workspace on a single canvas — widgets (Calculator, Browser, PDF Viewer at the Dec 2025 review) placed, resized and snapped anywhere; a Binder for viewing documents side by side without iPad Split View; circle-content gesture raising four AI-tutor actions. The current site/store surface is much broader: kanban, mind map, flowchart, gallery, music, timer, mindfulness, 3D, website-embed, YouTube and web-search widgets, plus canvases, notebooks and PDFs.

### Docs analysis
- Store privacy label is heavy for a study app: data linked to identity includes Contact Info, User Content, Search History, Browsing History, Identifiers and Diagnostics; cloud AI features require internet, and the listing carries an assistive-use disclaimer to verify AI output before relying on it for graded or safety-critical work.
- Positioning is deliberately workflow-shaped: built by four Imperial College London graduates from their own "messy reality of student workflows" — the pitch is replacing the GoodNotes-plus-Split-View-plus-YouTube-plus-LLM juggling, not improving any single tool.

**Features**

| Area | Detail |
|---|---|
| Naming | Note that two products share the name. |
| Identity | (a) Amphi Notes: free open-source cross-platform plain-text notebook. |
| Identity | Amphi Notes has folders like a file system, image/video insertion, markdown-ish text. |
| Identity | (b) Amphi (useamphi.com): closed-source iPad student canvas app. |
| Organization | File-system-like folders. |
| Organization | The canvas app combines notes, documents, flashcards, timers, calculators. |
| Canvas | Single study canvas; widgets resizable and snapped into place; Binder view for side-by-side documents. (R12) |
| Widgets | At launch Calculator, Browser, PDF Viewer; now also kanban, mind map, flowchart, gallery, music, timer, mindfulness, 3D, website embed, YouTube, web search. (R12) |
| AI | Embedded AI tutors: circle content and choose Next (step-by-step walkthrough), Find (locate extra resources), Explain, Check; canvas context shapes answers; custom tutors in development. (R12) |
| Sync | Self-hosted sync server or Amphi Cloud (Amphi Notes); iCloud sync (canvas app). (R12) |

**Sentiment**

| What people say |
|---|
| XDA reviewers liked one canvas replacing several student apps; the reviewer stopped using iPad Split View within days. |
| Community lives on Discord. |
| The self-hosted, own-your-data sync model draws open-source users. |
| The app is very small (about 2 downloads/30 days per AppBrain), so there is little recurring praise or complaint data; the findings state this explicitly rather than inventing a consensus. |
| App Store reception is thin and lukewarm where it exists: 3.7/5 from 7 ratings (GB storefront). (R12) |
| Known friction: cannot take notes while a study widget is open on the canvas (a frequent complaint on Amphi's Discord, reported via XDA). (UNVERIFIED beyond that single writeup) |

**Wants**

| What people want changed |
|---|
| Allow note-taking while a study widget is open on the canvas. |
| Custom AI tutor creation and sharing (on the roadmap). (R12) |
| Desktop and Android versions (developers say in the works; nothing shipped). (R12) |
| New-app signal: open local files plus easy self-hosted sync. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Cross-platform (Amphi Notes). |
| Platform | iPad only for the canvas app; requires iPadOS 26.0+ (Vision via visionOS 26.0+); English only. (R12) |
| Price | Free download with IAPs: Student £0.99 and Pro £9.99 on the store; site plans are Note-taker Free (unlimited canvases/notebooks/PDFs, iCloud sync) and Student £0.99/month with flashcards; a third tier appears without a published price — UNVERIFIED. (R12; previously no pricing was recorded) |
| Developer | Amphi Labs LTD; store version 1.1.4 dated 17 Oct 2026; TestFlight beta preceded the store release. (R12) |
| License | Amphi Notes GPL-3.0+. |
| License | The iPad Amphi AI app is closed source. |

### Video evidence
- The team uploaded a YouTube video explaining the fragmented student-workflow problem — that video is how the XDA reviewer found the app, and the XDA review embeds hands-on footage of the canvas, widgets and tutor actions in real use. No independent walkthroughs surfaced; comment-side gripes live in the app's private Discord rather than public threads.

### Contradictions
- Widget set: the December 2025 review describes three widgets; the current site/store describe many more — a beta-to-1.1.4 progression rather than a true conflict, but sources disagree if read side by side. R12 correction: the canvas app now ships a much larger widget catalog and published pricing, superseding the cached "notes/flashcards/timers/calculators" summary.

Sources: apps-likes-wants.md ; findings/r12-enrich-d.md

## Evernote

### Visual surface
- Desktop/web/mobile: the classic three-pane layout (sidebar, note list with snippets, editor pane); a "Home" dashboard with draggable widgets is the modern landing surface; editor is rich-text (non-Markdown) with checklists, tables, attachments, in-note audio; mobile keeps the three-pane structure with a bottom tab bar, described by long-time users as heavier than before.

### Docs analysis
- Free plan: max 50 notes, 1 notebook, 1 GB monthly uploads, 200 MB max note size, single device + web (Evernote's own help pages).
- AI suite (built "in close collaboration with OpenAI"): semantic search over saved content, AI Assistant chat that can search/organize/enrich notes and manage tasks, AI Meeting Notes with transcription and summaries, AI Cleanup/formatting; natural-language search ("What did I write about X in 2023?") is a flagship 2026 capability. Tasks with due dates/reminders and Google Calendar integration tie meetings to action items; Spaces remain the team layer. Search spans typed text, PDFs, image OCR and handwriting in one query — still considered among the best.
- Plan limits that count notes (not storage) are the free-tier squeeze mechanism; the web clipper remains the capture moat.

**Features**

| Area | Detail |
|---|---|
| Capture | Web clipper (its most famous feature). |
| Capture | Email-in, scanning, audio notes, widgets. (R12) |
| Capture | Notebooks/tags. |
| Organization | Notebooks/tags. |
| Organization | Reminders. |
| Organization | Tasks. |
| Organization | Stacks, Spaces (teams), shortcuts. (R12) |
| Search | Powerful search including text in images. |
| Search | Full-text + PDF/OCR/handwriting + semantic AI search and natural-language search. (R12) |
| Tasks | In-note tasks, due dates, recurring, calendar sync. (R12) |
| AI | AI features recently added. |
| AI | Assistant chat, meeting transcription/summaries, AI Cleanup. (R12) |
| Sync | Full sync across platforms. |

**Sentiment**

| What people say |
|---|
| The web clipper is repeatedly called the best on the market, the thing people still miss after leaving. |
| Deep search/archive value: decades of notes retained. |
| Users stay for the archive. |
| Price anger dominates: one user's yearly charge went from about $83.80 (2024) to $268.61 (2026); megathreads keep filling. (R12) |
| The free tier squeeze (50 notes/1 notebook) reads as hostility to legacy users. (R12) |
| Product itself still praised: best-in-class search and OCR, useful AI, good calendar/tasks loop. (R12) |
| Performance complaints: heavy client, slow mobile app ("slow bloated mess"). (R12) |
| Distrust of Bending Spoons' strategy: profit-max on a niche, arbitration-only terms changes. (R12) |
| An app-store-review analysis cited 57% of negative reviews on price/upsell/AI versus 4% technical faults. (UNVERIFIED in the R8 fact-check (the source could not be re-located); treat only the community complaints below as sourced) |
| Layoffs of the entire US team and months of silence followed the acquisition. |
| Community mood: WSJ "Evernote is dying" discussion; a September 2026 "My last six months at Evernote" post from an ex-employee. (R12) |
| Export/alternatives threads are the most upvoted content. |

**Wants**

| What people want changed |
|---|
| Saner pricing after the 2022 acquisition ("over priced for a note taking app"). |
| Pricing with notice and grandfathering of loyal users. (R12) |
| A 32% increase reported by leavers. |
| Less upsell pressure. |
| A free tier big enough for casual use ($242/yr to stay at the "casual user limit" was called too small). |
| A trustworthy archive you own forever. |
| Faster, lighter clients. (R12) |
| Better markdown/interoperability and export. (common refrain in alt-app lists; UNVERIFIED as top-request) (R12) |
| New-app signal: a trustworthy archive priced sanely, with a clipper as good as Evernote's. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Veteran cloud archive. |
| Platform | Now owned by Bending Spoons. |
| Business | 50-note / one-notebook free cap under Bending Spoons. (R8 fact-check against Evernote's help pages) |
| Business | Starter $99/yr (~$14.99/mo), 1,000 notes cap; Advanced $249.99/yr (~$24.99/mo); Enterprise custom. Previously the plan ladder was Personal/Professional tiers with upload caps — superseded (2026). |
| Platforms | Windows, macOS, web, iOS, Android. (R12) |

### Video evidence
- Evernote's own channel leads with the v11 highlights video (115+ improvements since the takeover) and AI Transcribe; G2 hosts user video reviews. Video shows how much of the 2026 product is surface polish layered on the old notebook model, and testers confirm AI transcription works only "as a secondary feature". The real story lives in comments: HN threads on the takeover and an ex-employee's "last six months" post, plus Reddit Bending Spoons threads, gripe about price hikes, fired US staff, and a free tier reduced to "try before you buy" — though even commenters concede the app has gotten better in the last two years, a nuance no polished review includes.

### Contradictions
- Old plan structure persists in some 2026 reviews (Personal $14.99/Professional $17.99 with 10 GB uploads) against the current Free/Starter $99/Advanced $249.99 structure with note-count caps; current structure wins, the older page is stale. R12 correction: pricing ladder and platform list re-verified in 2026; the cached "50-note free cap" row is confirmed and now sits inside a Free/Starter/Advanced ladder.

Sources: apps-likes-wants.md ; findings/r12-enrich-b.md

## OneNote

### Visual surface
- Windows desktop: a free-form canvas notebook — each page is an unlimited whiteboard-like surface where text boxes, ink, images, audio, tables and embedded files can be placed anywhere (not a linear document); left rail lists Notebooks → Sections (colored tabs) → Pages; a Microsoft 365-style ribbon carries Draw/Home/Insert/View. Web is a simplified version of the same hierarchy; iPad/Android are touch-first with the ribbon collapsed to a bottom tab bar and strong pencil support. Fall 2026 additions: Copilot Notebooks, MathML support, touch/keyboard polish.

### Docs analysis
- Hard limit: 2 GB per section file when syncing to OneDrive ("file too large" error beyond it); SharePoint limits vary.
- Free tier: full OneNote app with 5 GB OneDrive storage shared with other M365 apps; M365 Personal/Family adds storage and version history; M365 Premium raises Copilot usage limits.
- Handwriting OCR indexing is Windows-only: ink created on iPad/iPhone is not searchable until opened/processed on a Windows PC.
- Copilot: summarize pages/sections, generate to-do lists, draft content; Copilot Notebooks draw from docs, decks, Outlook email, Teams chats, Loop and txt files and produce topic-based "audio overview" episodes saved to OneDrive; Copilot Edit Mode (GA target Nov 2026) would let Copilot create/rename/delete pages, sections and notebooks — admins flagged as a risk surface. Copilot became available to all M365 users regardless of subscription level in fall 2026.
- Export story is weak: PDF flattens ink to images; .one format is proprietary; no live-ink export path.
- Design decisions worth borrowing: infinite free-form page canvas; colored sections; tag summary pages; local automatic backups on Windows; the "OneNote Notebook" vs "Copilot Notebook" split shows Microsoft differentiating long-term archive vs AI-curated workspace.

**Features**

| Area | Detail |
|---|---|
| Canvas/ink | Freeform infinite canvas: place ink, text, and images anywhere. |
| Canvas/ink | Dump a picture or PDF and scribble over it (free-form overlay). |
| Organization | Notebook/section/page hierarchy. |
| Editing | Typing/drawing anywhere to think non-linearly. |
| Editing | Gathering research material on one page. |
| Editing | Ink-to-text, ink-to-shape, math assistant, laser pointer. (R12) |
| Search | OCR. |
| Tags | Checkbox/task/priority tags; tag summary pages. (R12) |
| Collaboration | Sharing and collaboration; real-time co-editing via cloud notebooks. (R12) |
| AI | Copilot summarize/organize/draft; Copilot Notebooks with multi-source references and audio overviews. (R12) |
| Clipper | Web Clipper extension. (R12) |
| History | Page versions (M365 tiers), local backups, recycle bin. (R12) |
| Sync | OneDrive storage requirement. |
| Sync | Sync via Microsoft cloud. |

**Sentiment**

| What people say |
|---|
| The infinite canvas itself is the beloved core: "love Onenote just because of infinite canvas." |
| For many users sync is rock solid, one reason they stay. |
| For others (especially teams) sync is the dominant complaint; the findings hold both. |
| Handwriting/stylus workflow on Windows and iPad is considered best-in-class — a fair reason to stay. (R12) |
| Recurring complaints: OneDrive sync conflicts ("This page has conflicting changes"), slow deep hierarchy navigation, weak backlinks, data lock-in to OneDrive. (R12) |
| Large notebooks make search sluggish; it can miss ink that Evernote catches. (R12) |
| Organization decays over time — messy pages; missing saved searches and advanced filtering. (R12) |
| OneNote lets users set pen/touch auto-switching (automatic mode switching setting), which the community cites as the reference behavior other apps lack. (See the dedicated synthesis in Part III and the wish list) |
| Weak mobile apps and no nested folders in sections. |
| Users feel trapped by the format. |
| Stagnation: a user left to try everything else and came back "sick of lack of improvements." |

**Wants**

| What people want changed |
|---|
| Fast, reliable sync (conflict spikes for teams). |
| No data loss or stale versions across cached notebooks. |
| Speed on complex pages. |
| Better mobile apps and nested folders in sections. |
| Better backlinks, saved searches, and structured/filtering power. (R12) |
| Real export/interoperability — ink that survives migration. (R12) |
| Cross-platform handwriting OCR parity (iPad/iPhone indexing). (R12) |
| Resumed development. |
| New-app signal: infinite canvas plus sync you never have to think about. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Windows/web/mobile; also macOS and iPad/Android apps. (R12) |
| Business | Free with a Microsoft account: full app, 5 GB OneDrive storage. Previously cached as just "free with a Microsoft account"; the 2026 check confirms the free tier despite one pricing site claiming otherwise. |
| Business | M365 Personal $9.99/mo annual (a $6.99/mo promotional price also cited); M365 Premium $19.99/user/mo with the highest Copilot limits. (R12) |
| Business | OneNote 2021 perpetual desktop reaches end of support Oct 13, 2026. (third-party; UNVERIFIED against Microsoft lifecycle pages) (R12) |

### Video evidence
- Official video is Microsoft's Copilot tutorial set (summarizing notes into to-do lists, generating outlines) plus third-party Copilot walkthroughs; the videos show Copilot living in both a ribbon pane and an on-canvas icon so you summarize a page without leaving it. Beyond Copilot, OneNote has little of the influencer-review video culture its rivals have — users discover it bundled. HN comment threads carry the real signal: praise as a "loss-leader" impossible to compete with on Windows, gripes that it is bad at linking notes and weak at organizing as notebooks grow, that the UI "never clicked" for iPad/Pencil users, and a recurring dispute over whether "free" secretly requires OneDrive storage.

### Contradictions
- Free tier: one pricing site claims "OneNote does not offer a free plan as of September 2026" while the same site's own review and multiple other sources describe a free version with 5 GB storage; weight of evidence says the free tier exists. M365 Personal price differs across sources ($9.99 vs $6.99 — likely list vs promotional). R12 correction: pricing rows expanded from the cached "free with Microsoft account" to the 2026 ladder, and Copilot Notebooks added as the headline 2026 change.

Sources: apps-likes-wants.md, input-mode-switching.md ; findings/r12-enrich-b.md

## Notion

### Visual surface
- Desktop/web: a clean, minimal block-based document editor; left sidebar of pages and workspaces; the page is a stack of draggable blocks (text, headings, toggles, callouts, code) that can be turned into databases with multiple views (table, board, calendar, gallery, timeline, list); slash-command driven; the same surface morphs between note, wiki and project tracker. The 2026 surface has grown into a suite: Notion Mail, Notion Calendar, AI Meeting Notes with speaker labels, and Notion Agents that can read/write Excel and PowerPoint and build interactive HTML blocks. October 2026: Agents got "their own computer and browser," a "Review for me" safety-check mode, and AI usage consolidated under a credit system. Mobile is consistently called second-class vs desktop.

### Docs analysis
- Blocks are the unit of content; Free plan: unlimited pages/blocks solo, 5 MB file upload cap, 7-day page history, 10 guests; block cap appears once a second member joins (exact unpublished number).
- Plans: Free $0; Plus $10/member/mo annual ($12 monthly); Business $20 annual ($24 monthly) — Business now includes the full AI suite, replacing the killed $10/mo AI add-on; Enterprise custom. AI credits: $10 per 1,000 monthly credits beyond plan allowances; "Auto" model tier claims frontier results at 90% lower cost.
- Databases: relational links, rollups, subtasks, dependencies, 6+ views, formulas; automation rules are weaker than Asana/ClickUp; no native Gantt dependencies or time tracking. Offline: a real offline mode shipped in 2025 with a stated goal of "offline by default," but reviewers in 2026 still call it inconsistent. Public API; MCP server for agent access; Slack/Zapier/Make/n8n integrations.
- Design decisions worth borrowing: blocks as universal primitive; typed properties with multiple views; slash commands; template marketplace as ecosystem engine; AI priced by credits rather than seats.

**Features**

| Area | Detail |
|---|---|
| Editing | Block editor. |
| Editing | Pages in pages. |
| Editing | Slash commands, toggles, callouts; Agents can build interactive HTML blocks. (R12) |
| Organization | Relational databases with multiple views. |
| Organization | Templates. |
| Collaboration | Sharing/permissions. |
| Collaboration | API/integrations; MCP server for agent access. (R12) |
| AI | Notion AI. |
| AI | Notion Agents (scheduled/triggered, with their own computer and browser), Q&A, meeting notes with speaker labels, credit-based usage. (R12) |
| Suite | Notion Mail, Notion Calendar, AI meeting transcription (Zoom/Meet/Teams). (R12) |
| Sync | Cloud-first. |
| Sync | Recent per-page offline mode. |
| Sync | Real offline mode shipped 2025 with "offline by default" as a stated goal; 2026 reviewers still call it inconsistent. (R12) |

**Sentiment**

| What people say |
|---|
| The all-in-one value: "I don't have to open one app to take a small note and then transfer it into another system". |
| Block structure plus linked databases and filters gives one source of truth with different views. |
| Databases non-technical people can use. |
| G2 strongly positive (4.6/5, 10k+ reviews) but Reddit skews negative on pricing changes and performance. (R12) |
| Performance quantified: 3-5s loads on big pages; degradation above ~5,000 database records. (R12) |
| Learning curve 2-4 weeks; users report "spending more time organizing than working". (R12) |
| Speed complaints are specific and tracked as a worsening trend: large databases and workspaces take seconds to minutes. |
| Offline mode is per-page and manual; the community calls it too little too late. |
| Memory usage is extreme: 2 pages = 1.5GB reported. |
| Lock-in anxiety: poor full-fidelity export keeps people trapped. (R12) |
| AI paywall resentment: full AI moved behind the Business plan; "Plus plan's 20 AI responses is misleading". (R12) |
| Workspace chaos: "the tool should not be the work"; hours spent re-organizing. |
| Database-view complaint specifics (from the digests): users want faster view switching and better handling of large databases. |
| Slow database views are the single most-cited technical failure. |

**Wants**

| What people want changed |
|---|
| Speed for large databases and workspaces. |
| A real full offline mode. |
| True offline-by-default and a reliable mobile app. (R12) |
| Task dependencies/Gantt, time tracking, stronger automations. (R12) |
| Honest, stable AI pricing. (R12) |
| Data portability (notes are not stored locally; people migrate to Airtable/Obsidian for limits and speed). |
| Less memory usage. |
| Less re-organization overhead. |
| New-app signal: Notion's flexibility with local speed: instant, offline, and yours. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Web/desktop/mobile. |
| Platform | Proprietary. |
| Business | Free $0 (unlimited solo blocks, 5 MB files, 7-day history); Plus $10/member/mo annual ($12 monthly); Business $20/member/mo annual ($24 monthly) with the full AI suite included — previously AI was a separate $10/mo add-on, now killed (2026); Enterprise custom; AI credits $10 per 1,000 beyond plan allowances. |
| Business | Free plan block cap kicks in once a second member joins (exact number unpublished). (R12) |

### Video evidence
- Notion has the largest video-tutorial ecosystem in its lane — reviewers describe learning it through "many YouTube videos," and video reviews quantify what text can't: databases take 2-3 weeks of daily use to feel natural, complex workflows about 6 weeks. Video also exposes what docs sanitize: load times on big pages and the number of clicks template-heavy work takes. Comment threads invert the review tone: HN threads call it "a jack of all trades and master of none" with flexibility as cognitive overhead, gripe that a 15-second empty-page load drove a team to cancel, and recall people not knowing where to place new pages at a 20-person org.

### Contradictions
- Plan prices conflict across trackers (Plus $12/Business $18 with a separate AI add-on on one stale page) against Notion's own pricing page and most trackers (Plus $10/Business $20 annual, AI included on Business); the latter wins. "No real offline" folklore vs the 2025 shipped offline mode: both partly true — the mode exists, reliability complaints persist. R12 correction: pricing re-verified in 2026 and the AI add-on marked superseded by AI-included Business.

Sources: apps-likes-wants.md, community-digest.md, thread3-digest.md ; findings/r12-enrich-b.md

## Obsidian

### Visual surface
- Desktop (Windows/macOS/Linux, Electron): a three-pane workspace — left icon ribbon, collapsible sidebar file tree, central Markdown editor in live-preview or reading mode; tabs and split panes, right sidebar for backlinks, outline, tags and local graph. The signature screens are the Graph View (force-directed node web) and Canvas (an infinite spatial board). Mobile compresses the vault model into a two-pane layout; the "Mobile 2.0" refresh added a redesigned interface, native widgets and Siri integration. Community themes and CSS snippets change nearly everything.

### Docs analysis
- Core app free for personal use; commercial/revenue-generating use requires a paid commercial license (US$50/user/year). Vault = plain Markdown files (plus JSON Canvas `.canvas`) in a local folder; no account required for the core app.
- Sync limits are hard: Standard = 1 synced vault, 1 GB total, 5 MB max file, 1 month version history; Plus = 10 vaults, 10 GB (expandable to 100 GB), 200 MB max file, 12 months history; unlimited devices on both; storage pools flexibly across vaults.
- Optional add-ons: Sync (~$4-5/mo Standard, $8-10/mo Plus) and Publish ($8/site/mo annual, $10 monthly); 40% student/nonprofit discount. Publish features: hover previews, graph view of published pages, backlinks, full-text search, custom domains, SEO/social cards by default, optional analytics, editing + publishing from mobile.
- Bases: a database/table view over notes with typed properties — Obsidian's answer to structured data inside Markdown. Web Clipper browser extension. Roadmap signals: an open file format for canvas data, saving links to notes/graph views/headings/URLs, RTL text, an accessible single-vault Sync plan. Shared vaults for sync exist but lack real-time co-editing.

**Features**

| Area | Detail |
|---|---|
| Editing | Markdown vault on disk (plain local .md files). |
| Editing | MathJax. |
| Editing | Canvas (as .canvas files in the open JSON Canvas format). |
| Editing | Callouts, embeds (notes, images, PDFs), aliases, block references. (R12) |
| Organization | Bidirectional links/graph. |
| Organization | ~9,500 community plugins (registry ~9,521 entries, Oct 2026). |
| Organization | Per-vault config that syncs everywhere. |
| Organization | Bases: database/table views over notes with typed properties. (R12) |
| Search | Fast local search. |
| Capture | Web Clipper extension; daily notes; quick switcher. (R12) |
| Publishing | Obsidian Publish: notes → website with graph, search, hover previews, custom domains. (R12) |
| Sync | Optional paid Sync (E2E-encrypted). |
| Sync | Fully offline otherwise. |
| Sync | Sync plans: Standard 1 vault/1 GB, Plus 10 vaults/10-100 GB, unlimited devices, pooled storage. (R12) |
| Export | Notes are plain local files, no lock-in. |

**Sentiment**

| What people say |
|---|
| Plain local Markdown files are the loyalty anchor: your data is never locked in, change tools without rebuilding. |
| A Reddit straw poll on "if Obsidian went database tomorrow" shows how users reason about it ("Right now there's basically zero chance of the app going south like changing note storage formats"). |
| Fast, offline, great for code+math. |
| Core desktop app loved: free, local-first, endlessly extensible; ~4.5/5 across review aggregators. (R12) |
| Steep learning curve is the most common deterrent. (R12) |
| Mobile is the weak point: buggy Markdown editing on Android, image-handling confusion, slow app start. (R12) |
| Sync opinion flipped positive by 2026: "works out of the box, has the log and version history"; dissenters still find free alternatives frustrating on iOS. (R12) |
| File-first costs (from thread-b-storage): metadata beyond note content leaks into JSON sidecar files (.obsidian folder: hotkeys, themes, plugins, workspace.json). |
| Also a hidden metadata cache (IndexedDB). |
| Renaming a note rewrites every file containing a wikilink ("rename fanout"). |
| The canvas is a sibling .canvas file (JSON Canvas, MIT-licensed, spun out March 2024). |
| Canvas positions and edges live in the .canvas file, note content stays in .md files, which is why the canvas-note bridge works live in both directions for free. |
| Community hunger to go beyond .md ("does the use of .md format also doom Obsidian to miss some advanced features? Like a database?"). |
| Security incident: an April 2026 Elastic Security Labs campaign in which malicious community plugins shared inside shared vaults delivered the PhantomPulse RAT, aimed at finance and crypto people via LinkedIn/Telegram. |
| The vector was plugins in shared vaults, not fake app downloads. |
| Security incident: an RCE in a popular plugin (Tasks) where note frontmatter flowed unsanitized into a `new Function()` evaluator (CVSS 8.6, patched May 8, 2026). |
| Running JS in queries is off by default. |

**Wants**

| What people want changed |
|---|
| Sync price (Standard $4/mo billed annually = $48/yr; the $96/yr figure is the Plus tier) feels bad next to free workarounds. |
| No regional pricing or one-time option. (obsidian.md's main pricing page now shows a single $4/mo plan while obsidian.md/sync still lists both tiers) |
| Mobile sync friction with free workarounds. |
| A lightweight, faster mobile app and instant quick-capture on Android. (R12) |
| A bigger Standard Sync plan (1 GB/1 vault is too small). (R12) |
| Real-time collaboration in shared vaults. (R12) |
| Regex find-and-replace power and graph view on Publish mobile. (R12) |
| Plugin dependence on volunteer maintainers. |
| New-app signal: local Markdown plus effortless, affordable sync built in. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | App proprietary but free for personal use. |
| Platform | Desktop/mobile; Linux via deb/AppImage/flatpak. (R12) |
| Business | Commercial license $50/user/yr for revenue-generating use. (R12) |
| Business | Publish $8/site/mo annual, $10 monthly; Catalyst one-time license for pre-release builds; 40% student/nonprofit discount on Sync and Publish. (R12) |

### Video evidence
- Video is Obsidian's biggest community engine: the r/ObsidianMD subreddit functions as a comment section for YouTube videos, and tutorials cover Quick Switcher, Canvas and hotkeys as motion, which text docs flatten. Commenters gripe what reviewers omit: skeptics call the graph view "meaningless"/"only good for social media" even inside fan threads, reviewers' factual slips get corrected in comments, and HN threads surface the $8/mo Sync price as the recurring unspoken cost.

### Contradictions
- The folklore "Obsidian has no collaboration" is confirmed for real-time editing, but Sync Plus does offer shared vaults for asynchronous collaboration. Canvas files are JSON (`.canvas`), not Markdown, and the roadmap lists an "open file format for infinite canvas data" as future work — contradicting the "everything is plain Markdown" shorthand. One 2026 review's "2,700+ community plugins" is stale against the Oct 2026 registry count of ~9,521 kept in this section. R12 correction: pricing/platform rows re-verified in 2026; commercial license, Publish and Bases added as 2026-documented facts.

Sources: apps-likes-wants.md, thread-b-storage.md, thread-f-editor-platform.md ; findings/r12-enrich-b.md

## Miro

### Visual surface
- Web + desktop + mobile: the category-defining infinite whiteboard — zoomable canvas of sticky notes, frames, shapes, connectors and templates, with live cursors/presence, a left creation toolbar and a bottom facilitation bar (timer, voting). 2026 positioning is an "Intelligent Workspace": AI sidekick agents on the canvas, prompt-to-prototyping, AI note-clustering, stickies-to-diagram conversion, TalkTrack async video, and an MCP server exposing boards to external agents.

### Docs analysis
- Free plan: 3 editable boards (older boards flip to view-only), unlimited members, limited AI, 100 MCP calls/day. Starter $8/member/mo billed yearly (~$10 monthly); Business ~$20/member/mo; Enterprise custom. AI is credit-metered (a generated diagram costs about 5 credits); Visio/Lucidchart import on Starter matters for migrations. Design decisions worth borrowing: templates as onboarding (7,000+), board-level permission granularity, facilitation tooling, AI that transforms existing content rather than generating from nothing, and MCP access to boards.

**Features**

| Area | Detail |
|---|---|
| Canvas | Infinite boards. |
| Canvas | Sticky notes. |
| Canvas | Diagrams. |
| Capture | Document/PDF embedding. |
| Capture | Templates. |
| Collaboration | Real-time multiplayer. |
| Collaboration | Integrations (Azure DevOps etc.). |
| Facilitation | Voting, timer, TalkTrack async recording, breakout frames. (R12) |
| AI | Note clustering, diagram generation, sidekick agents, prompt-to-prototype. (R12) |
| Integration | Large app marketplace plus an MCP server for external agents. (R12) |

**Sentiment**

| What people say |
|---|
| Templates plus real-time collaboration for brainstorming and planning. |
| Beloved by agile teams for story mapping, retros, technical mapping. |
| Template breadth (whiteboarding, mockups, roadmaps, process flows). |
| Performance/lag on large or even modest boards, worsening over years ("boards are way laggier and take far longer to load"). |
| Lag specifically after inserting documents/PDFs. |
| Paid limits and unexpected deletions noted on Trustpilot. |
| Product quality still praised in 2026: fast canvas, real-time collab "just works", AI can structure sticky walls. (R12) |
| Billing pain is the loudest 2026 complaint: guests converted to paid members, mid-cycle prorated charges, editing a board flips you to paid, refunds hard to get. (R12) |
| G2 ~4.7/5 (~12k reviews) against harsher tool-reviewer aggregates (4.3/5). (R12) |
| The $1.355B Bending Spoons acquisition dominates the 2026 HN discussion; even critics concede "great whiteboarding tool though" while users discuss exit paths — acquisition anxiety no official material addresses. (R12) |

**Wants**

| What people want changed |
|---|
| A whiteboard that stays fast as the board grows. |
| Fix lag after inserting documents/PDFs. |
| Stop UI regressions and unresponsive controls. |
| Saner paid limits. |
| Transparent billing around members vs guests. (R12) |
| Cheaper team tiers and a friendlier free plan. (R12) |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Business | Paid tiers with board caps. |
| Business | Free: 3 editable boards, unlimited members; older boards become view-only. Previously the free-tier detail was cached only as "board caps" — now confirmed (2026). |
| Business | Starter $8/member/mo annual; Business ~$20/member/mo; Enterprise custom. (R12) |
| Platform | Web, Windows/macOS desktop, iOS, Android. (R12) |

### Video evidence
- Miro has the most official video in the lane: a 500+ video YouTube channel, Miro Academy courses and a famous community-made 1-hour walkthrough with per-function timestamps. Video shows what screenshots cannot: real-time multiplayer cursors, facilitation mechanics (voting, timers, sticky clustering), TalkTrack async board walkthroughs, and niche workflows outside the docs such as TTRPG groups running campaigns on boards. Comment threads soft-pedal two gripes reviewers bury: the free plan is "3 boards per team, not 3 each," with older boards silently flipping to view-only, and price ("still Expensive AF if you want to upgrade").

### Contradictions
- User counts differ across 2026 trackers (90M+ vs 100M+); likely marketing rounding, UNVERIFIED. Free-plan behavior: "3 editable boards" vs "only the three most recent boards remain editable" — the latter matches Miro's documented model. Large-board performance: still a complaint in the R11 findings, but barely present in 2026 sources (UNVERIFIED whether it improved). R12 correction: pricing/platform rows filled in from 2026 evidence and the Bending Spoons acquisition added as the dominant 2026 community story.

Sources: apps-likes-wants.md ; findings/r12-enrich-b.md

## Milanote

### Visual surface
- Web + desktop apps + iOS/Android: a calm infinite canvas of "boards" holding notes, images, links, to-dos and files as cards, with drag-and-drop anywhere, board-within-a-board nesting and shareable client links. The aesthetic is deliberately editorial (card grid, soft shadows, magazine typography), aimed at creative directors and designers rather than facilitators; connectors/arrows run between cards, and there is no graph/backlink machinery at all — it is a spatial organizing tool, not a knowledge network.

### Docs analysis
- Free plan is a permanent trial: 100 notes/images/links combined, 10 file uploads, unlimited shared boards, no time limit. Web clipper and email-in capture. Strengths per reviewers: wide file-type support, easy client sharing, pleasant interface; weak integrations and no automation for enterprise workflows. Design decisions worth borrowing: boards-within-boards as the single hierarchy, card-based universal content, client-ready share links, restraint (few features, polished).

**Features**

| Area | Detail |
|---|---|
| Canvas | Drag-and-drop cards on boards. |
| Canvas | Columns. |
| Canvas | Templates. |
| Capture | Image/file support. |
| Capture | Web clipper and email-in; PDF annotation. (R12) |
| Collaboration | Sharing/collaboration. |
| Sharing | Public share links and export. (R12) |

**Sentiment**

| What people say |
|---|
| Visual clarity for brainstorming and organizing: "by far my favorite tool for taking notes and saving ideas". |
| The freeform canvas feels like a wall of sticky notes. |
| Desktop boards described as amazing even by critics. |
| Mobile app nearly unusable: can't even add boards. |
| Boards degrade with many cards. |
| No edit history. |
| Export is per-board PDF/PNG/doc only. |
| A formal request exists on their own roadmap poll to "Export your data in a proprietary Milanote format" (i.e., even a full proprietary dump is wanted and not shipped). |
| Users complain "No Easy Export / Backup?". |
| The 100-note limit drove users to build alternatives. |
| Called the best client-facing moodboard tool for photographers; "the board that wins the job". (R12) |
| Free-tier limits "arrive sooner than expected" and are the #1 driver of people seeking alternatives. (R12) |
| Weak integrations and no automation frustrate larger teams. (R12) |

**Wants**

| What people want changed |
|---|
| Usable mobile app. |
| Fair pricing/bigger free tier. |
| Edit history. |
| Full export/backup. |
| Boards that scale. |
| Offline and desktop parity. (UNVERIFIED — not prominent in 2026 sources) |
| Integrations and automation for team workflows. (R12) |
| New-app signal: visual boards that work on every device at a fair price. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Business | 100-note free cap; ~$100/yr. Previously the cached price was ~$100/yr; 2026 trackers put paid from ~$9.75-12.50/mo depending on annual vs monthly billing — consistent with the yearly figure, now shown monthly. |
| Free | 100 cards, 10 file uploads, unlimited shared boards, no time limit. (R12) |
| Platform | Web, macOS, Windows apps, iOS, Android. (R12) |

### Video evidence
- Milanote's official channel is guides and templates rather than videos; its video footprint is largely indirect, via YouTube sponsorships — multiple user reviews say they discovered it through sponsor clips or "a recommendation of a youtuber", and Tool Finder's founder tests it on camera. Video shows the drag-and-drop feel of mixing images, links, swatches and notes on one board, plus the web clipper's "Unsorted" holding column that official guides underemphasize. Comment threads fill the gaps: the r/PKMS review thread details the 100-card/upload wall, and the 2017 Show HN thread records the original claim users still repeat — replacing "an entire wall of post-its and half a dozen moleskines". Grips reviewers omit: weak mobile apps, no offline, no edit history, pricing gap versus alternatives.

### Contradictions
- none found in 2026 sources beyond the cached annual price now restated monthly. R12 correction: free-tier mechanics (100 combined cards, 10 file uploads) and platform coverage added from 2026 evidence; the cached ~$100/yr price is confirmed and restated per month.

Sources: apps-likes-wants.md, thread-b-storage.md ; findings/r12-enrich-b.md

## Anytype

### Visual surface
- Desktop (Windows/macOS/Linux): a Notion-like block editor over a local-first core — left sidebar with spaces and object list, canvas-style pages built from blocks, database-style "sets/collections" with table, board, gallery and calendar views, and a graph view of the object network. Mobile (iOS/Android) carries the same object model but reviewers say sync and polish still trail desktop. No web version. The team has actively simplified the interface; early adopters report the learning curve has flattened in recent versions.

### Docs analysis
- Local-first: the primary copy of data lives on device; create/edit/search/link with no internet; E2E encryption with only the user holding keys; P2P sync between devices; self-hosted backup node or "local-only mode" as explicit settings; open-source clients (anyproto org) with key/recovery-phrase identity. Free plan: unlimited objects, 1 GB sync storage, E2E encrypted. Object model: every item is an object with a type and relations — the core abstraction and the learning curve. Limited third-party integrations; shared spaces exist but co-editing is weaker than cloud rivals (UNVERIFIED exact behavior).

**Features**

| Area | Detail |
|---|---|
| Editing/organization | Objects/sets/collections instead of pages. |
| Editing/organization | Graph + relations. |
| Editing | Blocks (rich text, code, embeds), inline objects. (R12) |
| Sync | Local storage with P2P/local network sync. |
| Sync | Self-hostable backup nodes. |
| Sync | Offline-first. |
| Security | E2E encryption with user-held keys. |
| Security | Keys generated locally; server never decrypts data. |
| Security | No account required. |
| Export | Markdown export (improved in 0.47.4, July 2025, to support properties and types). |
| Platform | No web version; Windows, macOS, Linux, iOS, Android clients. (R12) |

**Sentiment**

| What people say |
|---|
| Privacy model is the draw: "I love that it's local first... encrypted... powerful. Never had an issue with data loss". |
| Fast pages even with hundreds of items. |
| Storage reality (thread-b-storage): the vault is opaque encrypted blobs + index folders; "Files are stored inside flatfs dir in encrypted fragments, so they can't be accessed outside of Anytype". |
| Media streamed on demand and deduplicated. |
| Local-first does not mean plain files. |
| Export is the pressure valve and has repeatedly disappointed: a 2024 thread "Export is not great" reports Markdown export dropping everything but names. |
| A 2025 thread says property-rich data makes "the markdown export useless" and "your data will be encrypted and usable only with proprietary Anytype." |
| Release 0.47.4 improved this. |
| A co-founder pushed back on the lock-in charge on the community forum. |
| Takeaway recorded in the findings: an object/block store with strong encryption makes a faithful plain-file projection genuinely hard. |
| Anytype's answer has been improving one-way export, not a mirror. |
| Standout strengths per 2026 reviewers: offline speed, genuine data sovereignty, encryption; the object/relation model "takes real time to learn". (R12) |
| Recovery phrases and technical onboarding scare non-technical users; template library thin vs Notion. (R12) |
| Sync complaints: desktop-mobile sync failures and slow sync; mobile polish lags. (R12) |
| Product Hunt review tags add gripes: limited search, export issues, no multi-tab support. (R12) |
| A Business Dive video-review claim records heavy churn: the app "loses 90% of new users, as they become frustrated after a few days". (R12) |

**Wants**

| What people want changed |
|---|
| Reliable desktop-mobile sync (desktop-mobile sync barely happening, slow sync, synced-flagged items actually unsynced). |
| Mobile app quality catching up to desktop. |
| Transparent file storage on disk (no plain-file layout like Obsidian's). |
| Notion-grade database features (formulas). |
| A third-party security audit. |
| Analytics concerns addressed. |
| Easier onboarding (recovery phrase, mental model) and more templates. (R12) |
| Multi-tab support, better search, smoother export. (R12) |
| More sync storage on the free tier. (R12) |
| Real-time collaboration on par with cloud tools. (R12) |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Source-available (custom "Any Source Available" license; repos at github.com/anyproto; client code public, not OSI-approved). |
| Platform | Desktop/mobile. |
| Business | Free: unlimited objects, 1 GB sync storage. Pro $10/mo; Ultra $20/mo — both raised Aug 2026 (previously $8/$16). (R12) |

### Video evidence
- Anytype's video story improved recently: after years of sparse footage (a 2020 alpha demo, a 2023 community demo), the team released a basics video in early 2026 that Reddit praised as "straight to the point and includes some nice demos". The Business Dive's video review shows the defining workflow — spaces, object types and P2P sync running locally and offline, snappier than Notion — but also records the churn text reviews bury. Comment threads do the critical work reviewers skip: an r/Anytype "most circumvoluted and complicated app" thread, and commenters noting the app "promised local first but it was not local first when released", a broken-promise grievance official videos never address.

### Contradictions
- Free sync storage: 1 GB (matches the official pricing page, Oct 2026) vs an embedded user quote of 100 MB (likely outdated). Onboarding: "radically easier than before" per recent Product Hunt reviews vs persistent "steep learning curve" verdicts from other 2026 reviewers — improving, but the abstraction cost is real. R12 correction: pricing rows added (Free/Pro $10/Ultra $20, Aug 2026 raises) and the no-web-client limit recorded; nothing in the R11 rows proved wrong.

Sources: apps-likes-wants.md, thread-b-storage.md ; findings/r12-enrich-b.md

## Tana

### Visual surface
- Web/desktop (cloud): an outliner-first workspace — every note is a bullet tree; any node can carry a supertag that gives it structured fields; nodes flow via live searches/queries into other views (tables, boards, calendars, AI chat panels). The visual signature is dense, keyboard-driven outline nesting with typed fields inline. Tana Capture mobile feeds the outliner; there is no fully native mobile editor.

### Docs analysis
- Supertags: attach a tag to any outline node; the node inherits structured fields (text, dates, references, dropdowns) — schema-on-write over an outline. Live searches/queries pull nodes matching supertags/properties from anywhere into dynamic lists. AI: multi-model AI, AI command bar, in-platform agents, and an AI Meeting Agent with botless live transcription and automated summaries/action items. Product split in 2026: the original outliner lives at outliner.tana.inc while tana.inc became the agentic meeting platform (transcription, deliverables, voice agents) announced April 2026. Outliner pricing: Free up to ~1,000 nodes, basic supertags, limited AI credits, single workspace; Plus/Pro from $10/mo (Pro cited with 5,000 AI credits). Design decisions worth borrowing: schema attaches to notes at any point (tag later, structure emerges); information flows to views via queries rather than being filed; outlines as the universal primitive.

**Features**

| Area | Detail |
|---|---|
| Editing | Nested outline built around a daily "dashboards" note. |
| Organization | Supertags with field/inheritance schema (schema-driven tags). |
| Organization | Queryable graph. |
| AI | AI command bar/agents. |
| AI | Meeting Agent: botless live transcription, summaries and action items turned into deliverables within minutes. (R12) |
| Capture | Web clipper. |
| Capture | Tana Capture mobile app feeding the outliner. (R12) |
| Views | Tables, boards and calendars on tagged nodes. (R12) |
| Sync | Proprietary cloud database. |
| Export | JSON export (full, with Tana-specific structures). |
| Export | Markdown export (first version arrived 2025, subset-by-supertag, with/without fields). |

**Sentiment**

| What people say |
|---|
| Supertags "genuinely different from every other tagging or database system". |
| Users miss them in other apps. |
| The outliner model lets you capture everything, tag it, resurface on the day page. |
| "there really isn't anything to replace Tana" for bullet notes. |
| Learning curve: "as hard as learning a programming language". |
| Hours to learn; a survivors-only bias noted in reviews. |
| Storage (thread-b-storage): vendor lock-in is explicit, "Your data lives in Tana's proprietary format". |
| A 2023 user: JSON export "is a bit limited" unless you know what to do with it. |
| Community tooling (TanaMigrator) converts the JSON workspace export into a vault of markdown files. |
| TanaMigrator's author warns "VERY good chance edge cases exist." |
| Performance degrades as the workspace grows. |
| The free plan's 5-supertag cap means you cannot test the core feature without paying. (R12) |
| The meeting agent is called the clearest ROI in the product. (R12) |
| The 2026 pivot to meetings confused existing outliner users. (UNVERIFIED as a widespread sentiment) (R12) |
| Tool-reviewer scores cluster ~4.3-4.4/5. (R12) |

**Wants**

| What people want changed |
|---|
| Learnable-in-minutes structure instead of days. |
| A mobile app not too limited for real workspace use. |
| Performance at scale. |
| A free tier thick enough to evaluate. |
| Less perceived AI push. |
| Freer free tier for supertags specifically. (R12) |
| New-app signal: supertag-like structure learnable in minutes. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Business | Free / Pro $20/mo early-bird ($30 regular) / Business from $35/mo. (tana.inc, R8 fact-check) |
| Business | The older $10-18 tiers are gone. (R8 fact-check (tana.inc)) |
| Business | The separate Tana Outliner product lists Plus $8/mo. |
| Business | 2026 split: the outliner product (outliner.tana.inc) prices Free ~1,000 nodes / Plus-Pro from $10/mo, while the meeting platform prices Pro ~$20/mo early-bird (~$30 standard) and Max ~$80/mo early-bird (~$120 standard) — two products, two ladders; reviews must state which they cover. (R12) |
| Platform | Web, desktop (Mac/Windows); Tana Capture on iOS/Android. (R12) |

### Video evidence
- Tana's video coverage is unusually course-shaped: official "Tana Learn Live" sessions demo supertags and fields interactively, and a paid-course economy exists (Unlock Tana, Ev Chapman's Fast Track) because, as course copy admits, people otherwise spend "hundreds of hours watching YouTube tutorials" and still mess up their workspace. Videos show what outliner screenshots cannot: the node IS the tag, so supertags, fields and live search surface structure as you type. Comment threads uniformly report what reviews soften: the steepest learning curve in the lane, and even daily users admit an average user logging meeting notes or a recipe will struggle. Commenters also note the pivot risk: the site now leads with AI-meeting positioning, which the tutorial ecosystem hasn't caught up with.

### Contradictions
- Two different "Tana" products now exist (outliner vs meeting platform) with different pricing; December 2025 reviews describe only the outliner with a single AI stack, while June 2026 sources describe the meeting-platform plans. R12 correction: the pricing row now records the 2026 product split rather than one ladder, and the Meeting Agent/Capture rows were added.

Sources: apps-likes-wants.md, thread-b-storage.md ; findings/r12-enrich-b.md

## Reflect

### Visual surface
- Desktop/web + iOS/Android: a minimalist, fast networked-notes app — single sidebar (Daily Notes, Maps of Content), Markdown-style editor with [[double-bracket]] linking, and a tasteful backlink/graph side panel. Daily notes are the default landing surface; reviewers emphasize speed and restraint. Mobile works but feels desktop-first.

### Docs analysis
- Core model: daily notes as inbox, bidirectional backlinks including unlinked references, Maps of Content, graph visualization. AI built in: GPT-4 assistant with predefined + custom prompts, Whisper voice transcription, web article summarization, calendar integration (Google/Outlook). E2E encryption; Kindle/browser snippet capture; real-time cross-device sync; Readwise integration. Pricing: no free plan — 14-day full-feature trial, then one all-inclusive plan ($10/mo monthly or $8.33/mo billed annually, $100/yr). Design decisions worth borrowing: opinionated single-plan pricing; daily-notes-first onboarding (useful on day one); E2E encryption for a cloud app; speed as a feature.

**Features**

| Area | Detail |
|---|---|
| Editing | Daily notes flow. |
| Editing | Backlinks/graph. |
| AI | GPT-based AI assistants. |
| AI | Voice transcription. |
| Capture | Web clipper. |
| Capture | Calendar integration. |
| Capture | Kindle/browser snippet capture and Readwise integration. (R12) |
| Sync | E2E-encrypted cloud sync. |
| Export | Reflect JSON, CSV, markdown zip, HTML zip. |
| Export | Daily backups to the hard drive. |
| Platform | Web, macOS, Windows, iOS, Android clients. (R12) |

**Sentiment**

| What people say |
|---|
| The daily-note workflow "gets a lot of love... calming; you don't have to think about where something belongs". |
| Polish praised ("easy to use and the performance is phenomenal"). |
| Does fewer things very well. |
| Seamless for journaling. |
| Backlinks/daily notes incl. unlinked references called "perfectly" implemented; a 3,000+-note case study reports faster retrieval after switching from folders. (R12) |
| Limited when you want AI beyond search/summarize; mobile apps unexceptional. (R12) |
| Too expensive and too minimalist for students; built for daily-writing professionals. (R12) |
| Storage story (thread-b-storage): Classic exports are a copy, not a mirror; one user complained you "can only export all your notes in one go". |
| The notable 2026 move is a cloud block-ish app adding a plain-file sibling product (Reflect Open: "Your choice of sync: iCloud Drive or Git") rather than a mirror of the existing one. |

**Wants**

| What people want changed |
|---|
| Lower price ("$10/month is steep"; alternatives undercut it). |
| Fix occasional sync delays. |
| Better attachment management ("sucks"). |
| A real Android experience. |
| Database/table features Notion users expect. |
| A free tier (none exists). (R12) |
| Deeper AI beyond GPT-4 prompts, and team features. (R12) |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Business | ~$10/mo, no real free tier. Confirmed 2026: $10/mo monthly or $8.33/mo billed annually ($100/yr), single all-inclusive plan with a 14-day trial. |
| Platform | 2026 split: Reflect Open (open-source, local Markdown files, choice of iCloud Drive or Git sync) added alongside maintained Reflect Classic. |

### Contradictions
- CostBench's own pages conflict (its pricing page claims "2 plans from Free–$120/year" while its free-plan page says "no free plan", plus unsupported "$10/year" figures); weight of evidence: no free plan, $10/mo or $100/yr. R12 correction: pricing detail (trial, annual price, single plan) and platform list added from 2026 sources; the cached "~$10/mo, no real free tier" row stands confirmed.

Sources: apps-likes-wants.md, thread-b-storage.md ; findings/r12-enrich-b.md

## Logseq

### Visual surface
- Desktop (Electron): a left sidebar rail (journals, pages, graph, all pages/files) plus a right sidebar for pinned pages; the main canvas is a block-based outliner where every bullet is a node and typing `[[` creates page links; a top-right panel toggles graph, contents, linked references and queries; daily journals are the default landing surface. Graph view renders a force-directed network in a modal overlay; PDFs open in a side/inline pane with annotation highlights. Web mirrors the desktop shell; DB-version iOS app is in alpha.

### Docs analysis
- Two-track product in 2026: the legacy file-based version (Markdown/Org-mode, flat EDN/DataScript index over md files) and the DB version (beta) backed by SQLite, with RTC real-time sync in alpha and a new iOS app in alpha; the DB version explicitly warns data loss is possible and recommends regular SQLite backups. DB-version goals include Datalog queries, offline-first RTC with E2EE, and a long-term "seamless two-way sync between the database and markdown files" that remains aspirational. The OG/DB split took effect April 24, 2026, with OG maintenance-only.
- Plugin API is first-class (plugins docs, marketplace repo, developer mode); Git/GitHub sync is an officially documented community pattern. Self-hosting the web app via Docker is documented in the repo. Design decisions worth borrowing: everything is an outliner block, so any note is a queryable atom; journals-as-default lowers blank-page friction; linked references computed automatically; paid sync positioned as a donation tier rather than a feature wall.

**Features**

| Area | Detail |
|---|---|
| Editing | Block-level outliner (every line is a block: bullet, indentable, referenceable, embeddable). |
| Editing | Block references and embeds. |
| Editing | Drag-anywhere blocks. |
| Editing | Markdown + Org-mode; `[[wikilinks]]`, `#tags`, TODOs. (R12) |
| Organization | Tasks. |
| Organization | Queries (Datalog). |
| Organization | Graph links. |
| Organization | Whiteboards. |
| Organization | Namespaces, linked/unlinked references. (R12) |
| Learning | Flashcards (SRS spaced repetition on blocks). (R12) |
| Extensibility | Plugins. |
| Extensibility | Plugin API + marketplace, themes, custom queries, SCI/Clojure scripting. (R12) |
| Sync | Optional paid sync. |
| Sync | Local Markdown/org files as the store. |
| Sync | DB version: RTC real-time collaboration in alpha. (R12) |
| New DB version | A database (SQLite) version to fix performance. (Announced April 2024, DB beta shipped July 13, 2026) |
| New DB version | April 24, 2026: the OG/DB split took effect; OG is maintenance-only. (R12) |

**Sentiment**

| What people say |
|---|
| The block outliner is the loved model: everything has hierarchy, so retrieval pulls whole trees ("far more powerful and intuitive than Obsidian"). |
| Users love the Logseq way even while criticising the app. |
| Praise for ADHD-friendly capture and daily-notes workflows from longtime users. (R12) |
| Performance collapses on large graphs (1000+ pages), the app's defining complaint; boot times over 10s reported. (R12) |
| Sync data loss/duplication; fragile two-way sync. |
| Sync corruption stories drive migration away. (R12) |
| A file-writing defect produced unrecoverable data loss (in-app edits never written to ./pages/*.md). |
| The encoding cost (thread-b-storage): "Logseq uses Markdown syntax but not every Markdown file is a valid Logseq page, basically because of dashes". |
| Logseq began inserting hyphens on every line, "breaking MD functionality" (issue #3457, a 2020 Markdown hyphen bug). |
| Users want "normal markdown files that I can take with me anywhere." |
| Logseq's own April 2024 post explains the pivot to a database version: "Creating a new block requires rewriting the entire Markdown file"; "Renaming a page updates all files that reference it"; "structure data support is limited... lacking features like persistent IDs, timestamps". |
| The DB version's goals include Datalog queries, offline-first RTC with E2EE, and a long-term goal of "seamless two-way sync between the database and markdown files", still aspirational two years later. |
| OG is maintenance-only without reaching 1.0 (the OG/DB split took effect April 24, 2026). |
| "enable hourly backups to the filesystem" is community advice for DB users rather than official documentation. (UNVERIFIED as official guidance in the R8 fact-check) |
| The file plane is a backup/export surface, not the store. |
| The findings call Logseq the strongest evidence that the file mirror is a goal even the team that wants it has not shipped. |
| Trust erosion from infrequent updates and poor communication about the DB timeline. (R12) |

**Wants**

| What people want changed |
|---|
| Performance that survives 1000+ pages. |
| Sync without data loss or duplication. |
| Faster development and a finished mobile/sync. |
| Clarity on the DB version's trade-offs (SQLite portability, markdown export losing properties worry users). |
| A clear DB migration path; some fear losing plain-file access as the DB version advances. (R12) |
| Continued org-mode support in the DB version (reported missing). (R12) |
| Faster app startup. (R12) |
| New-app signal: Logseq's outliner power without the performance ceiling, on plain files. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Open-source, AGPL-3.0. |
| Platform | Desktop/mobile. |
| Platforms | Windows/macOS/Linux desktop (Electron), web (app.logseq.com, self-hostable via Docker), legacy iOS/Android; DB-version iOS alpha. (R12) |
| Sync tiers | Donation-based; third-party pages list Sync Backer $5/mo and Sync Sponsor $15/mo (UNVERIFIED against Logseq's own pages). (R12) |

### Video evidence
- Official demo videos exist on Logseq's YouTube channel, and third-party comparison footage (Obsidian vs Logseq walkthroughs) shows the actual difference reviewers gloss: Logseq's daily-notes-first, journals-then-link flow versus Obsidian's manual structure building. The most telling thread is community-wide: in r/Logseq's January 2025 tutorials thread, commenters explain the tutorial ecosystem itself has frozen — devs are focused on the DB version, the main app has not updated for months, and creators will not record because the app is about to change and make their videos irrelevant. What the videos miss by being old is real: block references, queries and mobile behavior shown in even a two-year-old basics video no longer match the current app or DB betas. Comment gripes under video coverage focus on rough UI versus commercial apps and unreliable mobile, things desktop-filmed demos never surface.

### Contradictions
- The common picture "Logseq is a files-first app" now conflicts with 2026 direction: the April 2026 OG/DB split has users reading the DB version as losing plain-files-on-disk, while the README's own beta/data-loss warning contradicts "the DB version is the future, everything is fine". R12 correction: the section now records the two-track OG/DB split, the alpha RTC sync and DB mobile apps, and donation-based sync tiers, none of which the cached rows captured.

Sources: apps-likes-wants.md, thread-b-storage.md ; findings/r12-enrich-c.md

## Tolaria

### Visual surface
- Desktop (Tauri/React/TypeScript) with a four-pane layout: sidebar (Inbox, Vault, Types, Pinned, custom views, folders), note list with sortable/property columns, editor (WYSIWYG plus raw mode via Cmd+/), and a status bar for vault, git and AI status. Three official Loom walkthroughs embedded in the launch essay show real daily workflow (inbox review cadence, web clipping into typed notes). A getting-started vault clones on first launch.

### Docs analysis
- Origin and scale: built by Luca Rossi (author of the Refactoring newsletter) to manage his 10,000+ note vault migrated from Notion; released free and open source in May 2026; ~100K lines of Rust + React at launch; 19.9k stars / 1.4k forks by late September 2026, with dated releases through the sweep (latest v2026-09-24).
- Principles (README): files-first plain Markdown with YAML frontmatter; git-first (every vault is a git repo, any remote, no Tolaria servers); offline-first, no accounts or subscriptions; AGPL-3.0-or-later with a trademark policy on the name/logo; types as lenses not schemas; AI-first but not AI-only (setup paths for Claude Code, Codex, Gemini CLI plus an AGENTS file); keyboard-first.
- Feature velocity in 2026: whiteboards, RTL and local AI models (May); AI agents creating notes directly plus a built-in MCP note-creation tool (Jun 6); Swedish/Ukrainian localization and copy-note-Git-URLs (Jun 10); native markdown spreadsheets with CSV syntax in cells (Jun 23); Authenticode-signed Windows installers, Homebrew cask, getting-started vault.
- Design decisions worth borrowing: types-as-lenses with no validation; views-as-YAML with natural-language dates AI can author; Inbox lifecycle; AutoGit idle/focus heuristics; wikilinks auto-updating on rename; AGENTS-file convention; bundled MCP vault tools; no-trash, git-as-safety-net deletion model. Code lifting is binding (AGPL-3.0).

**Features**

| Area | Detail |
|---|---|
| Editing | Notion-like WYSIWYG block editor (BlockNote/Tiptap) + raw Markdown mode (Cmd+/); filename always visible at top. (R12) |
| Editing | Slash commands. |
| Editing | [[wikilinks]] with autocomplete and auto-update on rename. |
| Editing | Mermaid diagrams. |
| Editing | KaTeX math with editable source panel. |
| Editing | Code blocks with syntax highlighting. |
| Editing | Editable callouts. |
| Editing | Sandboxed HTML blocks. |
| Editing | Colored highlights. |
| Editing | Todo block shortcut. |
| Editing | Collapsible headings. |
| Editing | Table navigation. |
| Capture | Inbox section (unorganized notes, Forte-style capture-vs-organize, disableable). |
| Capture | Note list sortable by any property or file metadata with customizable property columns. |
| Capture | cmd+click to open URL/note links. |
| Capture | Web-clipping into typed notes shown in the developer's Loom walkthroughs. (R12) |
| Canvas | tldraw whiteboards stored as markdown files. (Shipped in 2026 velocity: whiteboards, RTL, local AI models) |
| Rich content | Media/PDF previews (PDF.js), lightbox. |
| Rich content | Spreadsheet notes (plain-text sheets with formulas via IronCalc WASM). (Lane d: CSV syntax in cells plus frontmatter formatting, Jun 23 release) |
| Attachments | Drag-and-drop from Finder. |
| Attachments | Clipboard paste. |
| Attachments | Remote image paste. |
| Attachments | Vault-root or note-relative paths. |
| Organization | Types as lenses, not schemas: every note has a type (default Note). |
| Organization | Types are themselves markdown files with icon/color, no required fields or validation. |
| Organization | Sidebar sections (Inbox, All notes, Archive, types, Pinned/favorites, custom views, folder tree at the bottom). |
| Organization | Custom views are YAML files in a views/ folder with nested filter criteria, regexes and natural-language dates, and AI can author them. |
| Search | Command palette (Cmd+K) with semantic matching. |
| Search | Keyboard-first design. |
| Search | Quick open with create-note-from-search. |
| Search | Note body full-text search. |
| AI | Direct model providers (OpenAI, Anthropic, Gemini, OpenRouter, Ollama, LM Studio, custom OpenAI-compatible endpoints) for chat over note context. |
| AI | CLI agent targets (Claude Code, Codex, OpenCode, Pi, Gemini, Copilot CLI, Kiro, Antigravity, Hermes). |
| AI | Dedicated AI side workspace. |
| AI | AI commit-message drafting. |
| AI | AI can create notes. (Lane d: shipped Jun 6, OpenAI-backed, plus bundled MCP note-creation tool) |
| Integration | Bundled MCP server (Node or Bun) exposing vault tools (create/update/append notes, vault lifecycle). |
| Integration | AGENTS file ships for external agents to self-orient. |
| Integration | Claude Code skills usable from the AI panel. |
| Integration | Per-agent model picker. |
| Integration | Local API keys. |
| Sync | Git is the sync layer: in-app commit, push, browse history, per-note version history. |
| Sync | AutoGit opt-in mode auto-commits/pushes when idle or on focus shift. |
| Sync | Mobile syncs via iCloud or Files app sharing the same git repository, auto-commit on save with merge support. |
| Multi-vault | Multiple vaults, separate app windows per vault, mounted vault workspaces, custom vault order, parent Git repository support, vault deep links. |
| Export | PDF export. |
| Export | Standalone HTML previews. |
| Localization | Swedish and Ukrainian shipped (Jun 10); RTL support (May). (R12) |

**Sentiment**

| What people say |
|---|
| Files-first vault: notes are plain .md with YAML frontmatter, no database, no proprietary format. |
| Folders are secondary; flat-vault friendly. |
| Origin: the author migrated 10,000+ notes from Notion to plain Markdown and built the app he wanted. |
| Mostly AI-written code (~zero lines written by the author himself); 1900+ commits, 3000+ tests, 70 ADRs. |
| Git-first as AI transparency is a loved feature: seeing exactly what the AI changed vs what you wrote, with AI as a git contributor. |
| No trash bin; git history is the safety net (a deliberate deletion model). |
| AI chats are not persisted in vault files by default. |
| Loved: UI polish with real files underneath; the inbox concept; clipboard image paste praised as rare and essential. |
| Open source vs Obsidian ("I had no idea Obsidian wasn't open source"; lock-in freedom is the differentiator). |
| Show HN (May 2026) thread was large: strong praise for git-first AI-auditable edits, repeated Bear-influence observations (the dev confirmed Bear as a design influence), admiration that it is open source where Obsidian is not. (R12) |
| Reddit reach beyond HN: an r/DigitalEscapeTools "open-source alternative to Obsidian" thread drew 1,048 votes and 65 comments; r/macapps commenters noted it "moved really fast" with Windows demand answered after launch. (R12) |
| Skeptics in the thread: a webwrapper-versus-native bloc refused Tauri on principle; a feature-creep warning invoking Bear's restraint; one dismissive single-maintainer-lifespan comment pushed back on by others. (R12) |
| Emerging (alpha, Oct 2026): what shipped in October 2026 was the iPhone/iPad client. |
| A web client is announced as an in-development beta with alpha CI only. (R8 fact-check correction: the earlier note said the web client had shipped) |
| The remote-client direction (sharing notes/vaults with view-only/revoke, signed access tickets) is still worth watching, though desktop remains git/no-server. |
| The findings' pull-from assessment: liftable concepts include types-as-lenses, views-as-YAML with natural-language dates, Inbox lifecycle, AutoGit idle/focus heuristics, wikilinks auto-updating on rename, AGENTS-file convention, bundled MCP vault tools, no-trash git-as-safety-net model. |
| Code lifting is binding: AGPL-3.0. |
| Not worth copying: the React/BlockNote editor layer (the project's own weak point per HN bug reports). |
| Known bugs to avoid repeating: "last modified" sorting breaks after first git commit (sorts by commit date). |
| Known bugs to avoid repeating: code fence requires a space; ctrl-e end-of-line missing; cursor jumps below block after fence creation. |

**Wants**

| What people want changed |
|---|
| A truly native (AppKit/SwiftUI) app rather than a Tauri/React web-wrapper. |
| Feature-creep worry ("stay focused like Bear"). |
| Early-bug fixes (blank frozen app; three bugs in five minutes; sort-by-modified issue). |
| Editor friction fixes. |
| "AI-first" wording read as humans second-class. |
| Large-file editor performance. |
| npm-dependency-in-adjacent-to-home trust concern. |
| Mobile demand (largely since addressed). |
| A way to donate/pay at launch. |
| Answers to single-maintainer longevity skepticism. |
| Dark mode (requested in the Show HN thread). (R12) |
| Live visibility of agent edits in the vault (Google-Docs-style); the dev pointed to git authorship as the answer, commenters still want live awareness. (R12) |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | macOS, Windows, Linux desktop (Homebrew cask + signed installers). |
| Platform | iOS/iPadOS beta via TestFlight. |
| Platform | An iPhone/iPad client shipped October 2026. |
| Platform | ~52.6K lines of Rust plus ~53K lines of TypeScript/TSX (repo count, Oct 2026), Tauri v2. |
| Platform | AGPL-3.0-or-later; free and open source forever, no accounts or subscriptions. |
| Price | Free and open source; README carries a sponsor panel; monetization is indirect (the paid Refactoring newsletter is a separate product); the dev's stated pledge: free forever, 2+ hours/day on it. (R12) |

### Video evidence
- The only official video is three Loom walkthroughs by the developer — how he organizes his workspace, his inbox workflow, and saving web resources into typed notes — linked from both the README and the launch essay; they show real daily workflow rather than feature tours. No independent YouTube reviews surfaced; the deepest discussion is textual: the Show HN thread, where the developer answered bug reports in real time, and Reddit crossposts whose comments (webwrapper architecture, feature creep, early sorting bugs) are exactly what the official walkthroughs omit.

### Contradictions
- Platform parity at launch: an HN commenter noted the site mentioned Mac and Linux but offered only a Mac download; Linux builds existed in GitHub releases — since resolved (Authenticode-signed Windows installers and Homebrew cask are now documented), but the early install experience was uneven. Star counts vary across sources (16.8k in June listings, 19.9k by late September) — growth velocity, not a conflict. R12 correction: launch scale, author identity, 2026 feature velocity and the October iPhone/iPad ship are now recorded; the cached rows did not carry them.

Sources: tolaria.md ; findings/r12-enrich-d.md

## AFFiNE

### Visual surface
- Desktop/web (Electron + web): a sidebar with workspace switcher, favorites and a doc tree; two core view modes — "Page" (linear doc, Notion-like block editing with slash menu) and "Edgeless" (infinite whiteboard canvas where docs, sticky notes, shapes, embedded pages, databases and slides coexist); databases render as table/board views. Doc-to-canvas is a per-page mode switch, not a copy. Mobile companion apps exist (iOS/Android editors, historically weaker than desktop — UNVERIFIED current parity).

### Docs analysis
- Positioning: "There can be more than Notion and Miro" — an all-in-one workspace fusing wiki docs, whiteboards and databases on one edgeless canvas; blocks include rich text, sticky notes, embedded web pages, multi-view databases, linked pages, shapes, slides.
- Architecture: BlockSuite (open MIT-licensed editing toolkit) + OctoBase (open-source local-first collaborative database); local-first data ownership is an explicit design pillar. Self-hosting via Docker is documented; the / command menu supports rich embeds (GitHub issues, Figma) and pasting URLs creates inline metadata embeds.
- Pricing: Free, Pro, Team plans starting at $0; Pro primarily adds AI and cloud collaboration. Exact paid figures could not be confirmed from the JS-rendered pricing page — UNVERIFIED.
- Design decisions worth borrowing: one block model shared between doc and canvas views; local-first sync engine (OctoBase) with CRDT collaboration; databases as first-class blocks with multiple views; plugin surface (BlockSuite) separate from app code.

**Features**

| Area | Detail |
|---|---|
| Editing/organization | "everything is a block, something that could be edited and transformed freely". |
| Editing/organization | Doc + whiteboard + databases as views of one underlying store. |
| Editing/organization | Edgeless (canvas) mode. |
| Editing | Block-based docs (Notion-like), slash menu, embeds (GitHub, Figma, URLs), markdown shortcuts. (R12) |
| Editing | Frame/pen/shape tools and a slides mode on the canvas. (R12) |
| Organization | Docs tree, favorites, tags, databases with table/board views. (R12) |
| Storage | BlockSuite documents are a block tree "structured as a tree and stored within a Y.Map" (CRDT), with `sys:id`, `sys:flavour`, `sys:children`. |
| Storage | Persistent block IDs and parent/child structure with no file concept anywhere. |
| Canvas | Edgeless documents are isomorphic to page documents: both are block trees, with no data conversion during mode switching. |
| Canvas | A `surface` block holds all whiteboard elements. |
| Canvas | "a Page is a type of Database, as is Edgeless." |
| Sync | Local IndexedDB/SQLite per platform plus sync servers. |
| Sync | Local-first; AFFiNE Cloud for cross-device + collaboration; self-host via Docker. (R12) |
| AI | AFFiNE AI (writing/summarization) on paid tiers. (R12) |
| Performance | Claims to render thousands of vector shapes and text blocks at 60 FPS without DOM-heavy lag. |

**Sentiment**

| What people say |
|---|
| BlockSuite is the one editor core built for the canvas-plus-document hybrid: PageEditor and EdgelessEditor are two views that attach and detach from the same Y.Doc. |
| Costs recorded: much smaller ecosystem than ProseMirror/TipTap/Lexical. |
| The framework is young, API churn is real. |
| Teams adopting it inherit AFFiNE's product opinions. |
| DeepWiki's architecture notes describe a store-to-model-to-view data flow closer to a game engine than an editor library. |
| No plain-file story of the Thymer kind exists in BlockSuite. (Docs do not mention one; UNVERIFIED beyond docs read) |
| Edgeless + page as two views of one store is also the control case in the editor-core comparison: "the only core where the brief's requirement is the default behavior." |
| Product-level 2026 sentiment: reviewers like the clean, offline-first blend of notes + canvas and the doc-to-canvas switch; self-hosting and open-source roots called out positively. (R12) |
| Performance complaints recur: "pretty laggy compared to any other PKM software" on Edgeless canvases. (R12) |
| Data-egress anger: a PSA thread claims bulk import works but bulk export does not, framed as lock-in risk. (R12) |
| Community concern about development pace: claims that several top committers stopped committing mid-2025 circulate in AppFlowy-vs-AFFiNE threads (contested by the project; treat as claim). (R12) |
| Image-sync bugs (endless "loading image" after reinstall) reported in earlier years. (R12) |

**Wants**

| What people want changed |
|---|
| Not recorded in the findings beyond the ecosystem/API-stability cost framing; the findings treat AFFiNE primarily as architecture evidence. |
| Product-level 2026 wants: bulk "export all" to Markdown, better performance on large canvases, deeper third-party integrations, clearer cloud pricing value. (R12) |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Windows, macOS, Linux, web, iOS/Android companions; Docker self-host. (R12) |
| Business | Free (full local app + self-host; cloud workspace with limits), Pro and Team paid cloud tiers adding AI + collaboration; exact figures UNVERIFIED from the pricing page. (R12) |

### Video evidence
- Video coverage is thin and mostly official: Bizful.net's walkthroughs (AFFiNE vs Notion-style doc work; AFFiNE as a Miro replacement) and an official deep-dive with a BlockSuite engineer on the Block Developer Podcast that shows the edgeless/doc architecture from the builder's side. No strong independent review video surfaced in this sweep; the community signal lives in Reddit threads and Product Hunt reviews, where the export PSA and lag complaints dominate over anything shown on screen.

### Contradictions
- "Privacy-first, local-first, open-source" branding vs user claims of missing bulk export and past image-sync bugs — the tension users cite most when leaving. Dev-activity claims (top-10 devs inactive since Jun 2025) vs continued release activity per repo/third-party reviews — unresolved from the evidence. R12 correction: the section previously recorded only BlockSuite architecture evidence; 2026 product-level rows (positioning, pricing tiers, self-hosting, sentiment) are now added alongside it.

Sources: thread-b-storage.md, thread-f-editor-platform.md ; findings/r12-enrich-c.md

# PART II: OPEN-SOURCE REPOS

(Repo sections merge the deep-repos, github-repos and linked-apps findings. Where the findings recorded only repo-level feature lists without user sentiment, the Wants row reflects that.)

## CapsuleCraft (kostyk348/CapsuleCraft, a.k.a. capsuleos)

**Features**

| Area | Detail |
|---|---|
| Capture/editing | Block editor (headings, paragraphs, task lists, callouts, code blocks, CSV datagrids, audio-attachment notes) with autosave, undo/redo and `.eml` round-trip. |
| Capture/editing | `[[wiki links]]` with a live backlink index. |
| Capture/editing | Renaming rewrites all links. |
| Capture/editing | Zen focus mode, wide canvas and a two-tier header redesign landed in v1.8.0. (R12) |
| Organization/search | Okapi BM25 full-vault search with Cyrillic-aware folding. |
| Organization/search | Plus a "related by meaning" tf-idf cosine ranking. |
| Organization/search | Tags stored in message headers. |
| Planning | Tasks aggregated to Agenda / Kanban / Gantt views with dependency arrows and cycle protection. |
| Planning | RFC 5545 ICS export. |
| Threading | Real email threading, replies are child .eml files via In-Reply-To/References. |
| Threading | Datasets travel as MIME parts addressed by Content-ID. |
| Import/integration | Drag-drop .eml import, IMAP, Obsidian vault migration (`--import-obsidian`). |
| Import/integration | An external email parser ingests real Gmail/Outlook/Thunderbird .eml files with dual preview modes (PR #8). (R12) |
| Import/integration | Bundled MCP server exposing the vault to AI agents. |
| Import/integration | Offline deterministic "Co-Thinker" critique engine with no API keys. |
| i18n | Russian and English UI. (R12) |

**Sentiment**

| What people say |
|---|
| The "capsule" is a multipart MIME message: headers carry tags (X-Capsule-Tags), a `blocks.json` JSON part is the structured block canvas, extra MIME parts are datasets/attachments addressed by Content-ID, and threading rides standard mail headers. |
| A proof that a plain open-standard format can still host a block model. |
| Renamed from capsuleos at v1.5.0. |
| v1.0.0 shipped 2026-08-16 and v1.7.0 on 2026-10-25 (monthly-plus iteration). |
| An honest LIMITATIONS.md lists gaps: no code execution or audio in the native shell yet, best-effort folder watching, capsules not GPG-encrypted. |
| The roadmap already names GPG-encrypted capsules and optional end-to-end-encrypted vault sync ("tamper/censor-proof, still zero-cloud"). |
| Independent evidence that E2EE sync is the next expected feature in this category. |
| The project's own comparison table concedes where it loses: Obsidian's plugin ecosystem, OneNote's inking depth, Notion's collaborative editing. (R12) |
| A `--snapshot` CLI generates the README's own screenshots, doubling as the documentation pipeline. (R12) |

**Wants**

| What people want changed |
|---|
| No user sentiment recorded; visible direction comes from the roadmap (encryption, E2EE sync, audio in the native shell). |
| The vault starts empty by design rather than shipping demo content. (R12) |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Native Rust + egui shell with no webview (~11 MB AppImage, glibc-only). |
| Platform | macOS arm64 native builds shipped since v1.4.0; the legacy web shell needs WebKitGTK. (R12) |
| Platform | Legacy Tauri/web builds also published. |
| Platform | MIT license. |
| Platform | 98 Rust unit tests in the native shell plus 151 Vitest tests in the legacy web engine. |
| Repo layout | Implementation and build-from-source at kostyk348/CapsuleCraft; README and releases hosted on kobaltgit/capsuleos. (R12) |

### Contradictions
- R12 correction: the release-cadence row is superseded: v1.8.0 shipped 2026-10-26, one day after the cached v1.7.0 date, so the monthly-plus iteration is still accelerating.

Sources: deep-repos-c.md, github-repos-2.md ; findings/r12-enrich-f.md

## Meridian-Notes (realbyln/Meridian-Notes)

### Visual surface
- README is text-only on the fetched page (no screenshot URLs found; UNVERIFIED whether screenshots exist). Described visuals: a CPU-painted editor with minimap and git gutter, an "Endless canvas" of free-positioned text boxes with pen ink, graph view, radial menu, custom title bar/ribbon/menus/command palette, skins with gradients and PNG tiles with hot reload, zoom 50-400%.

### Docs analysis
- Native Rust, "No web technologies and no terminal: it draws its own window" — a CPU-painted custom widget toolkit (crates/ui, crates/term, crates/buffer) rather than egui/Tauri/Electron.
- Storage: plain Markdown files; the canvas layout lives in a separate layout file; pen ink saved as SVG; config in ~/.config/meridian (keys.conf, settings.conf); project settings in <project>/.meridian.
- Study suite is unusually deep: cloze cards, card review, quizzes, recall and Feynman panels, exam forecast, Anki import/export (TSV + APKG), leech list, speed reader.
- Activity: v0.2.0-test1 with unsigned Windows x86_64 test builds ("may crash, lose data"). License file not inspected in the 2026 pass — UNVERIFIED.

**Features**

| Area | Detail |
|---|---|
| Editor | Rope-based buffer, multiple cursors, macros (record/play/save), split views, vim mode, spell check, lint, git gutter, syntax highlighting, focus mode, typewriter scrolling, time-travel history scrubber. |
| Editor | Minimap and sticky scroll; find-in-files with an "editable results document". (R12) |
| Notes | `[[links]]`. |
| Notes | Scrollable/collapsible `{{embeds}}`. |
| Notes | Backlinks sidebar. |
| Notes | Hover preview. |
| Notes | Goto-anything. |
| Notes | Templates. |
| Notes | Plain Markdown files readable in any other editor. |
| Notes | "Remote folders with sync" listed among notes features — mechanism undocumented, UNVERIFIED. (R12) |
| Canvas/views | An "Endless canvas" where notes with a layout file open as free-positioned text boxes. |
| Canvas/views | Graph view. |
| Canvas/views | Pen ink on the canvas and inside Markdown notes, saved as SVG. |
| Canvas/views | Touch gestures. |
| Canvas/views | Radial menu. (R12) |
| Study | Cloze cards (`{{c1::text}}`). |
| Study | Card review. |
| Study | Quizzes. |
| Study | Anki import/export (TSV, APKG). |
| Study | Exam forecast. |
| Study | Recall/Feynman panels, leech list, speed reader. (R12) |
| Extensibility | Out-of-process plugins on a stable protocol (panels, commands, key bindings). |
| Extensibility | Rebindable keys via keys.conf. |
| Extensibility | Skins with hot reload where every color is a role. |

**Sentiment**

| What people say |
|---|
| Ink saved as SVG inside a Markdown note is a clean file-format answer for pen input. |
| The "layout file turns a note into free-positioned canvas boxes" pattern is a lightweight alternative to full canvas documents. |
| Out-of-process plugins avoid embedding a scripting runtime. |
| CPU painting instead of a GPU framework is a stated differentiator, with documented perf.md and gui-parity.md design notes. (R12) |
| Early and tiny (v0.2, 3 stars, test releases described as "early, unsigned, may crash, lose data"), which its own findings read as the cost of building a custom GUI toolkit. |

**Wants**

| What people want changed |
|---|
| Nothing recorded beyond the project's own early-stage warnings (BACKLOG.md exists but was not fetched in the 2026 pass). |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Rust with its own GUI toolkit (self-drawn title bar, ribbon, menus, command palette, dialogs: no webview, no terminal). |
| Platform | Wayland stylus support. |
| Platform | MIT license. |
| Platform | Windows x86_64 builds; Linux via cargo build; macOS breadth UNVERIFIED. (R12) |

### Contradictions
- none found; the 2026 pass adds docs-level detail but contradicts nothing cached. R12 correction: the editor/canvas/study rows are now backed by the 2026 repo sweep (minimap, editable find results, radial menu, recall/Feynman panels, leech list, speed reader), and the Windows-build scope is recorded.

Sources: deep-repos-c.md, github-repos-2.md ; findings/r12-enrich-f.md

## notecraft (AlienTechSoftware/notecraft)

### Visual surface
- README is screenshot-heavy and states every picture is drawn by the app's own test harness (`cargo xtask screenshots`), not mock-ups. Pictured: a Home screen with an Office-style ribbon, a Tags view rendering OneNote-style marks (To Do, Important, Question, Idea), an Equations view with a native TeX subset (fractions, roots, sums, integrals), a 14-theme gallery (light/dark, seven accents each), a File screen showing notebooks and their disk locations, a "Both formats" view with HTML and CommonMark pages side by side, a page-source ("look inside a page") view, and Mermaid diagrams rendered in place.

### Docs analysis
- Pure Rust, no Electron, no browser engine, no database; one binary rendered with egui on the GPU. Layered Cargo workspace (notecraft-model → formats/math/onenote → store → engine → ui-egui → apps) enforced by `cargo xtask layers`.
- Storage: notebooks/section-groups/sections/pages are plain nested folders; a page is index.html or index.md with pictures in assets/; per-node `_node.toml` metadata; format rules documented in docs/folder-format.md.
- Page format selectable per page/section/notebook/globally: HTML (default) or CommonMark+GFM.
- Sync: none built; notebooks are folders, so any OneDrive/Dropbox/Syncthing/iCloud-watched folder is a synced notebook; "no server, no account".
- OneNote import: `notecraft-onenote` crate reads `.one` section files from Microsoft's published [MS-ONESTORE]/[MS-ONE] specs (clean-room); ink and password-protected sections not read yet; CLI-only.
- Agent surface: every action is a command with an id, dispatched identically by window, CLI, loopback JSON-lines channel and a stdio-only MCP server; `--connect` lets an agent see the running window.
- Testing: 292 tests including paired pixel tests, headless real-window UI tests, contrast tests for all 14 themes, command fuzzing, HTML/MD round-trip, MCP-over-pipe integration.
- Honest-gaps discipline: "everything unfinished is written down in docs/gaps.md and ROADMAP.md; the app says 'not built' where it means it."

**Features**

| Area | Detail |
|---|---|
| Storage | Privacy-first, local-first storage on device. |
| Storage | Notebooks/sections/pages as plain nested folders; pages are index.html or index.md plus `_node.toml` metadata. (R12) |
| Account | No cloud account required. |
| Editing | Markdown-centric notes. |
| Editing | Direct-on-page WYSIWYG; containers as movable/resizable boxes; no selection across blocks yet (documented limitation). (R12) |
| Formats | HTML default, CommonMark+GFM optional, selectable per page/section/notebook/globally. (R12) |
| Ink/drawing | Drawing SVG stored as text in the page folder. (R12) |
| Equations | Native TeX subset rendering (RaTeX crate). (R12) |
| Diagrams | Mermaid rendered in-page with click-to-edit source. (R12) |
| Tags | 12 OneNote-style tags stored as plain text. (R12) |
| Search | Cross-notebook search with snippets. (R12) |
| Import | .one sections via Microsoft's published specs (clean-room); no ink or password-protected sections yet. (R12) |
| Agents | MCP stdio server + JSON-lines control channel + CLI; every action a command. (R12) |
| Themes | 14 themes (light/dark × 7 accents), contrast-tested. (R12) |
| RTL | Partial: per page/line/run direction; mixed lines not reordered. (R12) |

**Sentiment**

| What people say |
|---|
| Dual-licensed MIT OR Apache-2.0, so the architecture (Rust core + separate UI layer, storage layout, local-first sync decisions) is copy-paste friendly. |
| At this maturity it is a design comparison point rather than a usable product. |
| Very few users yet ("has had little use", own README), but issue traffic (file pickers, Linux release, stylus input, pen-mode switching) shows early adopters already treat it as a serious OneNote alternative. (R12) |
| No video coverage of any kind exists (no demo, walkthrough, review or comment thread); the README's programmatically rendered screenshots substitute for motion evidence. (R12) |

**Wants**

| What people want changed |
|---|
| One visible request: open issue #8 on stylus/palm-rejection input behavior on Linux, opened 2026-10-25. |
| File-picker dialogs instead of drag-only attachments (issue #4). (R12) |
| A Linux release (issue #3). (R12) |
| OneNote-style automatic pen/type switching with remembered pen color/thickness (issue #9). (R12) |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Cross-platform desktop targets. |
| Platform | A Rust core with the UI layer split on top. |
| Platform | Alpha scope is narrow (0.0.6, no published release). |
| Platform | Windows x64 binaries only (unsigned, SmartScreen warning documented); macOS/Linux build-from-source, untested; no web build. (R12) |
| Price | Free, open source. (R12) |

### Contradictions
- none found. R12 correction: the cached section carried only three feature rows (local storage, no account, markdown notes); the 2026 sweep shows a far broader OneNote-alternative build-out (HTML/Markdown dual format, TeX, Mermaid, tags, .one import, MCP agent surface, 14 themes) and records the wants rows from open issues.

Sources: deep-repos-a.md, github-repos-1.md ; findings/r12-enrich-f.md

## e-journal (EkarinLB/e-journal)

### Visual surface
- README text-heavy with feature cards; no visible screenshot URLs on the fetched page. Described screens: home shelf of notebooks with title search; a continuous-scroll page with ruled/margin paper, page dock and zoom; hideable UI ("one keystroke for nothing but the page"); light/dark themes.

### Docs analysis
- Stack: Rust backend with Tauri v2; the ink canvas renders on the system WebView (WebView2 on Windows, WebKitGTK 4.1 on Linux); "no Electron runtime in the shipped app"; Windows installers 2.5-3.5 MB, AppImage 84 MB.
- Storage: the entire library is ONE readable JSON file plus a rolling .bak; atomic writes via temp-file rename; single-instance enforcement; refusal to save an empty library ("if a save would wipe real notebooks, E-Journal declines it").
- Sync: none; single-file library means backup-by-copy, with `.ejournal` whole-library export/re-import for machine moves.
- Ink engine: pressure-sensitive ballpoint/fountain/brush nibs, Chaikin-subdivision smoothing, translucent highlighter, eraser, scribble-to-delete gesture that distinguishes scribbles from loops/underlines/writing, palm rejection, and drag-to-scroll deliberately off so a pen stroke never moves the page.
- Import: read-only import of Microsoft Journal `.ink` files decoded locally as SQLite (3 of 25 sample files import blank; stroke-blob decoding unfinished).
- Honest-gaps list: no version history (single .bak only), no typed text/sticky notes/shapes/lasso, title-only search, no tags/favourites, unsigned Windows binaries, no macOS build. Roadmap ranks version history, full .ink decoding, a local handwriting-search index, typed text/shapes, Flathub + signing.
- Clean-room statement: written from public documentation and observed behavior; Microsoft Journal is a behavioral reference, no proprietary assets.

**Features**

| Area | Detail |
|---|---|
| Storage | Encrypted local journal storage. |
| Storage | Single-JSON-file library with rolling .bak, atomic writes and empty-save refusal. (R12) |
| Journaling | Daily entries with calendar/date navigation. |
| Journaling | Mood tracking. |
| Journaling | Handwriting-first pages: continuous scroll creating pages, ruled/plain/blank paper. (R12) |
| Ink | Pressure-sensitive nibs (ballpoint/fountain/brush), Chaikin smoothing, highlighter, eraser, scribble-to-delete gesture, palm rejection. (R12) |
| Images | Insert/move/resize; drag-and-drop from the file manager. (R12) |
| Organization | Tagging. |
| AI | AI-generated summaries of entries using a local model. |
| Import | Read-only Microsoft Journal `.ink` import (partial stroke decoding). (R12) |
| Export | Markdown export. |
| Export | `.ejournal` whole-library export/re-import. (R12) |

**Sentiment**

| What people say |
|---|
| MIT-licensed and in the same product family as a Rust-first notes app, so the entry-storage schema, calendar navigation, encryption-at-rest approach and export path are directly liftable. |
| Twelve beta point-versions shipped by 0.12.0. |
| No user sentiment captured in the 2026 pass (issues not fetched); the README credits early users with finding rough edges. (R12) |

**Wants**

| What people want changed |
|---|
| Nothing recorded beyond the maintainer's own iteration. |
| Maintainer roadmap (2026 pass): version history, full .ink decoding, handwriting search, typed text/shapes, Flathub + signed builds. (R12) |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Local-first, AI-powered journaling desktop app in Rust with the egui/eframe toolkit. |
| Platform | Rust + Tauri v2 with an ink canvas on the system WebView; Windows 10 1809+ (NSIS/MSI, unsigned) and Linux (deb/AppImage; Flatpak in prep); no macOS, no mobile. (R12) |
| Platform | Dark/light theming. |
| Platform | Ships as a single binary. |
| License | MIT. (R12) |

### Contradictions
- The cached stack (egui/eframe, encrypted journal entries, mood tracking, AI summaries) and the 2026 sweep's stack (Tauri v2 with an ink canvas on the system WebView, single-JSON library, .ink import) describe substantially different apps; the cached rows are kept but UNVERIFIED in the 2026 sources, and may reflect an earlier development stage of the same project. R12 correction: the ink-first architecture, storage model and platform matrix are now recorded from the 2026 repo sweep.

Sources: deep-repos-a.md, github-repos-1.md ; findings/r12-enrich-f.md

## neo (hughhowey/neo)

### Visual surface
- README paints the UI precisely: a bookshelf library with labeled shelves, drag-and-drop books, cover art with progress bars from word goals; a writing page styled like a printed book (drop caps on chapter openings, auto-numbered chapters, dark mode, controls fading until hover); an Outline tab of index cards set like a page; script pages "on white card stock with two brass brads" in Courier Prime; a Darlings tab; NEO Pocket on a phone. The product page carries platform screenshots.

### Docs analysis
- Stack: Electron, deliberately simple (main.js shell, preload.js bridge, renderer); "If you know JavaScript, you can change NEO"; electron-builder installers.
- Storage: library in ~/Documents/NEO Library (movable via File → Library Folder…): one folder per book, chapters as readable HTML, metadata as JSON; continuous autosave; daily zip backups kept two weeks; email yourself a WIP with ⌘E.
- Sync: none built; the author suggests putting the library folder on iCloud; OneDrive-Documents interaction is explicitly detected and warned about.
- Screenplays: Fountain/Final Draft interop (.fdx/.fountain import-export), Final Draft's ⌘1-⌘7 element keys, INT./EXT. detection, (CONT'D) automation, scene lengths in eighths of a page, industry-format PDF export.
- Exports/imports: EPUB3 built to KDP guidelines, docx, PDF with page numbers/bookmarks, HTML, markdown, plain text; timestamped PDF snapshot email with a SHA-256 fingerprint of the text; .docx/.txt/.md import with automatic chapter/scene-break detection (acknowledged rough).
- i18n: 10 languages, one-file translation. License: MIT; maintainer is Hugh Howey (Silo).

**Features**

| Area | Detail |
|---|---|
| Library | Rendered as a bookshelf with labeled shelves, drag-and-drop, cover art and progress bars tied to word goals. |
| Writing | Manuscript pages look like books: automatic chapter renumbering, drop caps, curly-quote/em-dash/ellipsis auto-correction, spellcheck only on demand. |
| Writing | Keyboard-driven flow (one Enter = paragraph, two = `***` section break, three = new chapter). |
| Revision | A "Darlings" tab that parks cut passages and restores them to the exact original spot. |
| Revision | A placeholder hotkey drops a mark + sticky note mid-flow, collected into a to-do panel. |
| Outline | The book shown as index cards. |
| Outline | A card's note appears in the manuscript as a gray ghost paragraph that follows the writing until dismissed. |
| Outline | Dragging a card moves the text. |
| Cover art | Seeded abstract covers (six art styles × six type templates) with optional OpenAI-key text-derived covers (~1 cent/picture, key stored encrypted, lettering always real type). (R12) |
| Omnibus | Bind a shelf into one book (EPUB/docx/PDF with front/back matter, Parts via `+`, straight-through chapter numbering). (R12) |
| Screenplays | Fountain/Final Draft interop, element keys, (CONT'D) automation, industry-format PDF. (R12) |
| Export/backup | EPUB3 (KDP), docx, PDF, HTML, md, txt; daily zip backups; ⌘E timestamped snapshot email with SHA-256 text fingerprint. (R12) |
| Mobile | NEO Pocket: an Android side-load APK reading the NEO Library folder. (R12) |

**Sentiment**

| What people say |
|---|
| The index-card outline to document two-way binding is a small canvas-adjacent pattern worth studying. |
| Metadata (progress, goals, outline cards) is layered over plain text without a database. |
| Opinionated vertical UX (built by a novelist for novelists) sustains loyal local-first users. |
| The novelist-author launch drew open-source community attention on Tildes in August 2026, where one recurring complaint is LLM-flavored writing in software READMEs generally. (R12) |

**Wants**

| What people want changed |
|---|
| Nothing recorded in the findings. |
| The author's stated roadmap: chapter version history, a manuscript format for agent submissions, global end matter updating across books. (R12) |
| The screenplays feature was added because "a lot of you have asked for this feature" — evidence of feature-by-demand dynamics. (R12) |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Free and open source (MIT per the README), no accounts or subscriptions. (R8 fact-check corrected an earlier claim that neo was not open source) |
| Platform | Plain files on disk. |
| Platform | Installers for macOS (Intel + arm64), Windows (self-updating) and Linux (AppImage; a --no-sandbox note applies on Ubuntu 24.04+). (R12) |
| Platform | NEO Pocket: Android side-load APK. (R12) |

### Contradictions
- none found. R12 correction: the section is expanded with the 2026 sweep's docs evidence (screenplays interop, export/import matrix, seeded cover art, omnibus bind, daily zip backups, Android Pocket client), none of which contradicts the cached rows.

Sources: deep-repos-b.md, github-repos-2.md ; findings/r12-enrich-f.md

## notebook-navigator (johansan/notebook-navigator)

**Features**

| Area | Detail |
|---|---|
| Scope | Obsidian community plugin replacing the file browser and calendar. |
| Explorer | A virtualized two-pane explorer (folder tree + file list) with visual previews, built for very large vaults (100k+ notes target) using TanStack Virtual. |
| Organization | Smart folders. |
| Organization | Recent-notes view. |
| Organization | AI-style filter search with a filter-search grammar. |
| Organization | Frontmatter keyword (tag) discovery with included/excluded lists. |
| Organization | Tag and marker discovery with per-tag/folder icons and colors. |
| Organization | Calendar navigation. |
| Organization | Per-folder icons and colors. |
| Organization | Folder notes. |
| Organization | Manual sort mode with keyboard reordering. |
| Keyboard | Full keyboard navigation (all shortcuts remappable, VIM-style keys). |
| Docs | A documented settings surface (14 sections). |
| Storage | Storage across IndexedDB, Local Storage and an in-memory cache. |
| Storage | Per-setting "sync" toggles deciding whether a setting is stored locally or shared across devices. |
| Privacy | A documented network/diagnostics disclosure listing every HTTP request the plugin makes. |

**Sentiment**

| What people say |
|---|
| 2,782 stars / 104 forks / 1,072,639 downloads per obsidianstats (5.0 rating). |
| Reddit/forum word of mouth calling it a real replacement for the default file browser. |
| A case study reports 180 releases and ~zero hand-written LOC (AI-assisted development). |
| The docs are a blueprint in themselves: a startup/boot process doc (cold vs warm boot, metadata cache), a metadata pipeline doc (cache rebuild, provider stages) and a storage architecture doc (which store holds what). |
| Its switching guides for Evernote, Apple Notes, Bear, OneNote and Day One map where users actually migrate from. |

**Wants**

| What people want changed |
|---|
| No open issues surfaced; the author explicitly does not accept PRs ("no PRs will be accepted") and funnels feature direction into the 1.5 roadmap issue #274. |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Mobile-optimized. |

Sources: deep-repos-b.md, github-repos-2.md

## opensidian

Two unrelated projects share the name; the findings cover both.

**Features**

| Area | Detail |
|---|---|
| Positioning | (jpzk/opensidian, the primary subject) "Open-source and non-profit under GPLv3, vault-compatible cross-platform markdown notes app"; privacy-first knowledge management positioning. |
| Positioning | Explicitly a clean-room functional clone of Obsidian (reimplemented from the outside, contains none of its code, not affiliated with Obsidian/Dynalist). |
| Editing | Obsidian-vault-compatible Markdown notes. |
| Themes | (jpzk) Bundled AnuPpuccin (default), Material Gruvbox, Minimal and Solarized; most Obsidian community themes work as-is and broken themes grey out with a reason. (R12) |
| Security | (jpzk) Restricted-mode flag stored in `~/.opensidian.json` outside the vault so a vault you open cannot turn its own plugins on; plugins install only from GitHub over HTTPS with recorded sha256, and installing never enables. (R12) |
| Security | (jpzk) Plugin secrets go through the Secret Service keyring (gnome-keyring/KWallet/KeePassXC), never to a file. (R12) |
| Second project | (thiagovasconcelosti/opensidian, MIT, separate codebase) Node.js/Express + React 18/Vite. |
| Second project | D3 force-simulation knowledge graph. |
| Second project | WebSocket real-time sync. |
| Second project | JWT auth. |
| Second project | Multiple vaults. |
| Second project | Markdown editor with live preview and `[[wikilinks]]`. |
| Second project | Themes with a visual editor. |
| Second project | A hook-based plugin API (`note:pre-save`, `note:post-save`, command registration). |
| Second project | A full REST API (vaults, notes CRUD, graph neighbors, ranked full-text search with tag/date/backlink filters). |
| Second project | An MCP server published as the npm package opensidian-mcp so AI tools can read the vault. (R12) |
| Second project | Docker deployment. |
| Second project | Vitest (79 tests, >80% coverage). |

**Sentiment**

| What people say |
|---|
| jpzk/opensidian is the closest live reference implementation of an "Obsidian clone in Rust + Tauri" and doubles as a distribution checklist (AppImage variants, flatpak, rpm/deb, nix, GPG-signed checksums). |
| Its WebKitGTK dependency pain is an argument for a native GUI shell. |
| Two more independent projects adding MCP servers to notes vaults (this one and Tolaria) mark AI-agent vault access as a standard expectation. |
| Clean-room cloning is a legal pattern worth remembering; the name collision is a naming risk. |
| A rare AI disclosure: the jpzk README states nearly all the code, design docs and README were written by Claude (via Claude Code) with one human maintainer. (R12) |
| Early users are enthusiastic and asking for parity: an Android request (issue #4), Windows and plugin-support questions plus a missing roadmap (issue #2), and a naming nit that it should be branded "Opensidian" (issue #12). (R12) |

**Wants**

| What people want changed |
|---|
| Nothing recorded beyond maintainer roadmap items (jpzk) and the projects' own docs. |
| Android version (issue #4), Windows version plus a public roadmap (issue #2), proper "Opensidian" casing (issue #12); the maintainer is recruiting Linux distribution maintainers. (R12) |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Rust + Tauri v2 (WebKitGTK 4.1 webview on Linux). |
| Platform | v0.8.1 with fresh-install tests on Fedora 44, Ubuntu 26.04 LTS and Debian 13 dated 2026-10-25; no built-in sync evidenced (vault-folder based, so external sync tools apply). (2026) |
| Linux packaging | Slim AppImage. |
| Linux packaging | Portable AppImage (WebKit bundled). |
| Linux packaging | Flatpak (GNOME runtime). |
| Linux packaging | RPM. |
| Linux packaging | DEB. |
| Linux packaging | Nix (flake pins toolchain and crates). (R12) |
| Linux packaging | Reproducibility hygiene: SHA256SUMS signed with a published GPG key, locked cargo builds (`--locked`). |
| Linux packaging | Recruiting Linux distribution maintainers. |
| Site | opensidian.org. (R12) |

### Contradictions
- R12 correction: the thiagovasconcelosti repo is not a fork of jpzk/opensidian; R12 evidence shows an independent Node.js/TypeScript project that only shares the OpenSidian name, with a different stack, license and architecture. The cached install-matrix line (Fedora 44 and Ubuntu 26.04) also understates the matrix, which includes Debian 13.

Sources: deep-repos-c.md, github-repos-2.md ; findings/r12-enrich-f.md

## xnotes-android (shardulvs/xnotes-android)

**Features**

| Area | Detail |
|---|---|
| Ink | A custom native stroke engine (Kotlin + Jetpack Compose UI, NDK 27 + CMake core) turning raw stylus samples into a variable-width ribbon that swells and tapers with pressure. |
| Ink | Pens and highlighters, neon glow, disappearing ink. |
| Ink | Shape snapping (draw rough, hold, it snaps clean). |
| Ink | Crisp at any zoom. |
| Ink | Ink never flattened ("every stroke can be moved, restyled or erased later"). |
| Structure | Notebooks AND an infinite canvas ("pages when you want structure, endless space when you don't"). |
| Structure | Book layouts (single/double/cover, scroll or page-flip). |
| Structure | 20+ page templates (Cornell, planners, music staves, isometric). |
| Structure | 20+ themes; dark/OLED modes. |
| PDF | Import with margin widening for side notes. |
| PDF | Text markups. |
| PDF | Per-PDF color filters that keep photos true-color. |
| PDF | Real PDF export (vector, selectable text, links, bookmarks). |
| Text/media | Markdown with live formatting. |
| Text/media | Typed notes with tables, LaTeX, code highlighting. |
| Text/media | Audio recording that replays ink in sync with the lecture. |
| Shell | Customizable/floating/dockable toolbar. |
| Shell | Split view. |
| Shell | A real file explorer with grid/gallery/list/column/timeline views. |
| Sync | No built-in sync; the maintainer points users to a chosen folder plus Syncthing (issue #267). (R12) |
| Ecosystem | Forks carry it off Android: a Linux Swing host and a Qt 6 + Kotlin/Native port (libxnotes.so) that keeps notes compatible with the Android app, plus a Simplified-Chinese localization fork and two passive forks. (R12) |

**Sentiment**

| What people say |
|---|
| The storage stance is the positioning itself: "notes are saved as files in a folder you choose, not locked away in an app's database". |
| "open source, no account, no ads, no tracking, no internet access." |
| Distribution: GitHub Releases and F-Droid ship the same signed APK, so users can switch channels without reinstalling. |
| The Google Play build is a separate channel with a signing conflict (issue #166). (R8 fact-check corrected an earlier same-APK-on-all-three reading) |
| 269 stars, 33 forks, v0.8.23, README updated 2026-10-11. |
| The "notebooks or infinite canvas" duality is the same docs-vs-canvas tension AFFiNE solves with one block model. |
| The maintainer's r/fossdroid launch post (June 2026) frames the itch: other apps had laggy ink, clunky PDF markup, or flattened notes on export. (R12) |
| Added to a community Material You app list as a FOSS app; issue culture is active, with the maintainer closing issues with workarounds the same week. (R12) |

**Wants**

| What people want changed |
|---|
| Nothing recorded beyond the project's own roadmap; the feature set itself is the community demand signal (file-based storage, PDF interop both ways, editable ink, ink synced to audio, templates). |
| Layers with opacity, image export (jpg/png) and fill-area color (issue #288). (R12) |
| Auto handwriting correction and a shape/diagram library (issue #229). (R12) |
| Note-inside-note nesting (issue #331). (R12) |
| Ports beyond Android, with sponsorship friction noted (issue #234). (R12) |
| Folder-structure confusion, answered by pointing at New Note → New Folder (issue #310). (R12) |

**Pricing and platforms**

| Item | Detail |
|---|---|
| License | MIT. |
| Platforms | Android via GitHub Releases (signed APK), F-Droid (reproducible builds) and Google Play; Linux via the DarkL0gos forks. (R12) |
| Status | previously v0.8.23 with 269 stars, now v0.9.0 with roughly 240-247 stars and issues active within days. (2026) |

### Contradictions
- R12 correction: the version/status cached in the Sentiment table (v0.8.23, 269 stars) is superseded by the v0.9.0 release; the Google Play signing-conflict note (issue #166) stands unchanged.

Sources: deep-repos-c.md, github-repos-2.md ; findings/r12-enrich-f.md

## diktafon (Lukas-Novak/diktafon)

**Features**

| Area | Detail |
|---|---|
| Fork | A fork of jaromiru/diktafon: an open-source voice-memo app organized like cassette tapes, transcribing and summarizing entirely on-device. |
| Fork | The fork adds opt-in cloud backup and opt-in cloud transcription to your own server, both off by default. |
| Capture | One-tap recording on topic-based cassettes, no naming or setup; capture needs no network. (R12) |
| Tape metaphor | Cassettes as continuous gapless recordings. |
| Tape metaphor | Colour-coded segment bar, optional chime at memo boundaries, scrub/seek/skip. (R12) |
| Tape metaphor | Tap-to-seek transcripts. |
| AI | On-device Whisper transcription and Qwen summaries (vendored whisper.cpp + llama.cpp). |
| AI | Silero VAD noise-aware transcription with a rumble filter. |
| AI | Auto language detection per memo. |
| AI | Whisper and Qwen models download once on first run, switchable in Settings. (R12) |
| AI | Per-memo and per-cassette summaries/titles. |
| Data | Export/import archives (cassette or whole library, audio + text, additive import). (R12) |
| Data | Opt-in self-hosted sync with durable retry. |
| Extras | Around 19 UI/summary languages, cassette colour labels, retranscribe-cassette, per-memo copy/delete, light/dark themes. (R12) |

**Sentiment**

| What people say |
|---|
| A case study in consent-first cloud: everything local by default, cloud strictly opt-in, per-consent fallback after failed local attempts. |
| The fork exists as an answer to a privacy tension: upstream users who want on-device privacy plus their own backup target, with the consent language kept carefully. (R12) |
| No notable HN, Reddit or third-party review coverage found for either upstream or fork this pass; the README's privacy-first framing is the loudest public voice. (R12) |
| The "your own server + durable retry" ingest model maps well onto optional E2EE sync. |
| Upstream credit reads "designed by Jaromír Janisch, implemented by Claude Code." |

**Wants**

| What people want changed |
|---|
| Nothing recorded beyond the fork's own additions (cloud backup/transcription were built as the answer to that gap); no wants documented in public issue threads this pass, UNVERIFIED beyond README scope. (R12) |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Platform | Flutter (Android, iOS, Linux). |
| License | MIT, both upstream and fork. |
| Platform (upstream) | previously "released on F-Droid, Google Play and the App Store" without a fork distinction, now split: upstream jaromiru/diktafon ships Android (F-Droid, Google Play, sideload APKs interchangeable), iOS (App Store, iOS 13.0+), Linux tarball (libmpv/parecord/ffmpeg deps; Android 7.0+ with 4 GB RAM recommended). (2026) |
| Platform (fork) | Fork APKs on the fork's GitHub Releases only; cloud features require the self-hosted diktafon-ingest receiver. (R12) |
| Verification | SHA256SUMS files and GitHub build-provenance attestations on every release; integration tests cover record-play-transcribe-summarize end to end. (R12) |
| Models | Whisper and Qwen downloaded on first run. |

### Contradictions
- R12 correction: the cached store row described upstream, not the fork: store listings point at jaromiru/diktafon builds, so store installs do not include the fork's opt-in cloud features, and the fork's README reframes "nothing ever leaves the device" as "nothing leaves without consent."

Sources: github-repos-1.md ; findings/r12-enrich-d.md

## marmalade-tts-android (maxwhipw/marmalade-tts-android)

**Features**

| Area | Detail |
|---|---|
| Core | A native Android text-to-speech app with on-device neural voices and emotion-aware prosody. |
| Integration | Implementing Android's standard TTS engine interface so it is a system-wide drop-in replacement for Google/Samsung TTS. |
| Engines | Kokoro engine. |
| Engines | A fast English "Kitten Nano" voice bundled in the APK. |
| Engines | Bigger engines download on demand from pinned hostnames into app-private storage. |
| Cloud | Cloud voices strictly opt-in with the user's own API key (Venice.ai, OpenAI), documented in PRIVACY.md. |
| Personalization | Per-app voice routing via aliases (each app gets its own voice/speed/effects). |
| Personalization | 8 languages with auto-detection. |
| Personalization | 22 voice-effect presets plus an editor. |
| Accessibility | TalkBack/WCAG 2.1 AA support. |
| Playback | Foreground playback service with lock-screen/Bluetooth controls. |
| Integration | Share-sheet and "read selection" integration. |
| Family | Sibling apps: marmalade-stt-android (speech-to-text, also on F-Droid), the marmalade-tts Linux CLI ancestor, and marmalade-android (an OpenClaw AI assistant client). (R12) |

**Sentiment**

| What people say |
|---|
| Its value to a notes project is the privacy-engineering pattern: on-device AI/audio as a headline feature with opt-in cloud as a clearly fenced exception, and download-on-demand models from pinned hosts. |
| The right pattern if the app ever ships local speech features (voice notes, reading notes aloud). |
| Traction is distribution-led: a live F-Droid listing, an r/FDroidUpdates mention and a pending privacyguides/verified-apps verification; no critical reviews or Reddit threads of the TTS app itself surfaced this pass. (R12) |
| Users confuse the STT and TTS sibling apps, and the dev redirects between them in the issue threads. (R12) |

**Wants**

| What people want changed |
|---|
| Nothing recorded in the earlier findings. |
| More voices: issue #23 requests VCTK/more voices; the maintainer declines voices without explicit consent for TTS usage and is considering selling one-time premium voice-actor voices on a Play release. (R12) |
| Speed consistency: some downloadable engines speak slower than locally built ones (issue #19). (R12) |
| Pronunciation replacement/user dictionary support: issue #15 records a user migrating nearly 5,000 text-pair entries. (R12) |

**Pricing and platforms**

| Item | Detail |
|---|---|
| Licensing | Source is MIT but the released APK compiles in espeak-ng (GPL-3.0-or-later), making the APK a GPL-3.0 combined work. |
| Licensing | A deliberate licensing structure to satisfy Google Play's no-runtime-code-download rule. |
| Platform | Distributed via F-Droid (reproducible builds; v1.1.0 live since September 2026), GitHub Releases (fdroid-flavor APK) and Obtainium. |
| Store status | previously "Play in progress", now Google Play listing not found this pass; Play presence UNVERIFIED, and the dev has floated paid premium voices there. (2026) |
| Verification | The privacyguides/verified-apps submission (October 2026) includes APK signing-certificate verification. (R12) |

### Contradictions
- R12 correction: the cached "Play and F-Droid in progress" store status is superseded: F-Droid is live (v1.1.0) and Play presence is UNVERIFIED. A GitHub mirror (elmojunior/marmalade-tts-android) duplicates the README; only maxwhipw's repo is referenced by F-Droid and privacyguides.

Sources: github-repos-2.md ; findings/r12-enrich-d.md

## ConvertOneNote2MarkDown (theohbrothers/ConvertOneNote2MarkDown)

**Features**

| Area | Detail |
|---|---|
| Core | Converts OneNote notebooks to Markdown (via pandoc) with media extracted. |
| Fork | A hardened fork of SjoerdV/ConvertOneNote2MarkDown. |
| Implementation | PowerShell main script (~1,474 lines) driving the OneNote COM API and pandoc. |
| Implementation | docx files as the intermediate representation (naming by page ID or hierarchy). |
| Config | config.example.ps1 for saved configurations including a dry-run mode. |
| Release | CI releases (v2.23.1 latest). |
| Adoption | 766 stars, 84 forks, issues still active through 2026-10. |

**Sentiment**

| What people say |
|---|
| The known failure modes are the migration map: COM automation requires matching admin elevation (OneNote and the terminal both as admin or conversion fails, issue #123). |
| COM class factory errors (#102). |
| Trailing periods in page titles break PowerShell 5 conversions (#197). |
| Hand-written ink is the hard part: OneNote exports each ink stroke as a separate image without position. |
| An October 2026 issue (#200) requests merging strokes into a single image, noting that GetPageContent does carry each stroke's position and Ink Serialized Format renderable by WPF: the data exists but the docx path loses it. |

**Wants**

| What people want changed |
|---|
| Exactly those issues, above all ink fidelity. |
| OneNote users are still actively escaping to Markdown in 2026, and a converter with 766 stars is a real adoption funnel for any Markdown-first app. |
| A notes app that preserves ink semantics (position + strokes) on import would be genuinely differentiated. |

Sources: deep-repos-c.md, github-repos-2.md

## OfficeIMO (EvotecIT/OfficeIMO)

**Features**

| Area | Detail |
|---|---|
| Core | A family of MIT-licensed, COM-free .NET libraries for creating, reading, editing, converting, rendering and extracting Office, PDF, email, OneNote and text formats, with no Microsoft Office or LibreOffice installation required. |
| Packaging | Dozens of packages, many zero-third-party-dependency by design (OfficeIMO.Core, OfficeIMO.Pdf, OfficeIMO.OneNote). |
| Formats | Word (.docx plus first-party .doc), Excel (.xlsx/.xls), PowerPoint (.pptx/.ppt/.pot/.pps), Visio (.vsdx family), OneNote (.one/.onetoc2/.onepkg). |
| Formats | PDF (create/parse/render/edit/sign, PDF/A-2b, PDF/A-3b, PDF/UA-1, Factur-X, ZUGFeRD validation), OpenDocument (ODT/ODS/ODP/ODG), Markdown (typed AST, HTML/PDF rendering). |
| Formats | RTF, AsciiDoc, LaTeX, OPML, DocBook, CSV, EPUB, XPS, DjVu, CHM, iWork (.pages/.numbers/.key reading), Publisher recovery. |
| Formats | Email formats (EML/MIME, MSG/OFT, TNEF, mbox, PST/OST, OLM, EMLX, Outlook OAB, iCalendar, vCard), Google Workspace and Confluence bridges, invoicing (EN 16931/UBL/Polish FA(3), KSeF submission). |
| Tooling | A shared drawing/raster engine with PNG/JPEG/TIFF/WebP/SVG export. |
| Tooling | OCR hooks. |
| Tooling | An optional security provider (CMS/S/MIME/RFC 3161/X.509). |
| Tooling | The OfficeIMO Studio desktop app (Windows/Linux, Apple apps in development) with PDF markup/redaction/forms. |
| Tooling | A CLI. |
| Tooling | An MCP server plus Agent Skills so AI agents can inspect and convert local documents. |

**Sentiment**

| What people say |
|---|
| Very active (current v3.5.2 among dozens of rapid point releases; a one-issue open backlog at time of fetch). |
| The pull-from pieces for a Rust project (code is C#, but MIT): OfficeIMO.Markdown's typed Markdown AST with source spans, stable block identities and transforms (a model for lossless round-trip markdown editing). |
| The OfficeIMO.OneNote .one/.onetoc2 reader/writer design, the only mature open implementation of that format family. |
| The "fidelity report / loss preflight" pattern applied to every conversion, worth copying as an import/export UX principle. |
| The zero-dependency packaging discipline. |

**Wants**

| What people want changed |
|---|
| One visible open issue (#3171, opened 2026-10-23) about the GitHub experience having an "above the fold" problem. |
| No feature-level sentiment recorded. |

Sources: deep-repos-a.md, deep-repos-c.md, github-repos-1.md, github-repos-2.md

## Integration components

(All assessments are about embedding inside a local-first, Rust-target notes app; license is the recurring deciding factor.)

**Features**

| Area | Detail |
|---|---|
| OnlyOffice (documents) | An office suite: text document, spreadsheet, presentation and PDF editors. |
| OnlyOffice (documents) | The editing core is sdkjs (a JavaScript editor engine). |
| OnlyOffice (documents) | Document Server is a self-hosted server rendering it in a browser and Desktop Editors is a local shell around the same web core. |
| OnlyOffice (documents) | Embedding path is network embedding: iframe + JavaScript API + postMessage (the Nextcloud, Moodle, Odoo and WordPress connectors are all built on it). |
| OnlyOffice (documents) | AGPL-3.0 across Document Server Community Edition and sdkjs, with additional Section 7 terms (original logo retained, trademarks not usable). |
| OnlyOffice (documents) | Verdict: best-in-class office editing is realistic only if the host accepts AGPL or buys the commercial Developer edition. Weight L; license is the blocker. |
| Stirling PDF | Self-hosted PDF manipulation platform: merge, split, OCR, sign, redact, convert, compress, watermark, plus a desktop client and browser UI. |
| Stirling PDF | Java, ~94-95k stars (Oct 2026). |
| Stirling PDF | Open-core: most of the tree is MIT, but named directories (e.g. `frontend/src/editor/proprietary/`) sit under a proprietary "Stirling PDF User License". |
| Stirling PDF | The essentials (conversion, editing, watermarking, redaction, password protection) remain free for self-hosting. |
| Stirling PDF | No component library or SDK: run it (Docker or desktop) and point a webview/iframe at it, or integrate file-level against its API. |
| Stirling PDF | Verdict: file-level only; a heavy Java server, and the prettiest editing UI lives in proprietary folders. Weight S-M (API) / L (UI embed). |
| Excalidraw (canvas/diagram) | Ships as an npm package exporting the whole editor as a React component (`@excalidraw/excalidraw`), MIT, with `EXCALIDRAW_ASSET_PATH` for self-hosted assets and a documented elements/JSON data model for persistence. |
| Excalidraw (canvas/diagram) | Runs in any webview (Electron, Tauri). |
| Excalidraw (canvas/diagram) | Prior art: the official VS Code extension and Obsidian's popular Excalidraw plugin, which embeds the component inside Obsidian and stores drawings as files in the vault, embeddable in Markdown with notes linked to and from drawings. |
| Excalidraw (canvas/diagram) | Verdict: "the unambiguous win of this whole list." Weight S. |
| VLC / libVLC (media playback) | The VLC player is GPLv2+ but libVLC is deliberately LGPL-2.1+ so third-party (including closed-source) apps can embed the engine. |
| VLC / libVLC (media playback) | C API with official bindings (C++, Python, Java, Objective-C, C#) and render callbacks to output video into a host-provided surface. |
| VLC / libVLC (media playback) | Codec patents may require royalties for some bundled codecs. |
| VLC / libVLC (media playback) | Verdict: the mainstream way to embed playback (FFI + window interop; binaries ~100MB+). Weight M. |
| VLC / libVLC (media playback) | (mpv/libmpv, also LGPL, exists outside this list.) |
| Audacity (audio editing) | GPLv3 project mid-way through a large 4.x rewrite. |
| Audacity (audio editing) | No library, no SDK, no WASM build, no headless mode. |
| Audacity (audio editing) | The only automation surface is `mod-script-pipe`, which lets an external Python/Perl script drive a running Audacity instance over named pipes. |
| Audacity (audio editing) | Verdict: file-level only (launch externally, optionally drive via script pipes). Embedding its DSP would mean a hard fork. |
| Audacity (audio editing) | If waveform editing is needed, purpose-built DSP crates are the honest answer. Weight M (poor value). |
| OBS Studio (recording/streaming) | GPL-2.0-or-later. |
| OBS Studio (recording/streaming) | libobs is the embeddable rendering/compositing/encoding core, but embedding it in-process makes the host a GPL-2.0+ derivative. |
| OBS Studio (recording/streaming) | Streamlabs' obs-studio-node was released under GPLv2 for exactly this reason. |
| OBS Studio (recording/streaming) | Commercial embedding without source disclosure produced a license dispute (lowkey.gg). |
| OBS Studio (recording/streaming) | Verdict: either a GPL-licensed separate helper process, or OS-level capture APIs (ScreenCaptureKit/AVFoundation) instead. Weight L-XL (libobs) / S (OS APIs). |
| Image editors (GIMP / Krita / Photopea) | GIMP is GPL-3.0 (GPLv3+ well before 3.0; 3.0 itself shipped 16 March 2025), with Script-Fu/Python-Fu plugins, a libgimp 3.0 API and terminal batch runs, but no embeddable widget. |
| Image editors (GIMP / Krita / Photopea) | Krita is GPL with C++/Python plugins (a plugin "can do everything that Krita can do", inside Krita, not inside your app); no embeddable view or headless library. |
| Image editors (GIMP / Krita / Photopea) | Photopea is proprietary (repo is issues-only) with a real iframe + postMessage scripting API, which would make a "local-first" app call a remote closed service with user files. |
| Image editors (GIMP / Krita / Photopea) | Verdict: none is a good embedded component; use a small purpose-built canvas (or Excalidraw) for inline annotation, and GIMP/Krita as external "Edit in..." hand-offs. Photopea is disqualified on license/privacy grounds. |
| Godot (2D/3D engine) | MIT, no royalties. |
| Godot (2D/3D engine) | Headless server builds are officially documented. |
| Godot (2D/3D engine) | LibGodot (engine-as-a-library) was mainlined in a sponsored PR (#110863, merged, with follow-ups #123552/#123717 citing it as merged). |
| Godot (2D/3D engine) | migueldeicaza/libgodot is a maintained embeddable fork powering SwiftGodotKit and react-native-godot as an embedding precedent; GDExtension is the standard native-plugin mechanism. |
| Godot (2D/3D engine) | Verdict: the runtime embedded is realistic and precedented; the Godot editor embedded is fantasy. Makes sense only for interactive 2D/3D widgets (e.g. a 3D-scene note). Weight M-L. |
| Blender (3D) | GPL-2.0-or-later (Cycles is Apache-2.0); API-calling add-ons are treated as GPL. |
| Blender (3D) | No embeddable UI; the real mechanism is `bpy`, an official pip-installable Python module for pipelines and web services, plus headless `blender -b` and the `blenderless` wrapper. |
| Blender (3D) | Verdict: a sidecar Python process/Blender binary for thumbnailing, converting or rendering 3D assets referenced by notes; the GPL boundary is cleanest as a separate process. Weight M. |
| Kdenlive (video editing) | GPL-3.0-or-later as an application, with no embeddable view or headless library. |
| Kdenlive (video editing) | The layer beneath it, the MLT Multimedia Framework (also behind Shotcut), is LGPL-2.1 for the framework and client libraries, with a C API of playlists/producers/consumers. |
| Kdenlive (video editing) | Verdict: use MLT via FFI as the engine for a "video note" playback/trim/convert feature rather than Kdenlive itself. Weight M (MLT) / XL (UI). |
| Synthesis | Clean wins: Excalidraw (S, MIT, embeds directly), libVLC (M, LGPL) and MLT (M, LGPL) as engine-level FFI for media, bpy/Blender (M, headless sidecar) and GIMP headless (M) for file-level processing. |
| Synthesis | Possible but licensing-dependent: OnlyOffice (only with AGPL compatibility or a commercial license) and libobs (only as a GPL-licensed separate helper). |
| Synthesis | Non-starters as embedded components: Audacity, Kdenlive UI, Krita/GIMP UI, Photopea (non-free + remote service). |

**Wants**

| What people want changed |
|---|
| The findings record no user sentiment for these components; the analysis is capability and license fit, not demand. |

Sources: integrations-1.md

---

# PART III: SYNTHESIS

## 1. Feature wish list from the community

Every distinct feature request found across the Discord threads and digests, each tagged with the app/context it came from:

1. Web clipper as good as Evernote's (Evernote; also requested in Tana, Reflect contexts): apps-likes-wants.md, community-digest.md
2. OCR search (search text inside images/PDFs/handwriting) (Evernote praise; Goodnotes; requested in digests): apps-likes-wants.md, community-digest.md
3. Voice suite: voice transcription and voice-note capture (Reflect has it; requested more broadly): apps-likes-wants.md, community-digest.md
4. Canvas + PDF annotation in one app (OneNote overlay model; Goodnotes/Notability strengths; requested in digests): apps-likes-wants.md, community-digest.md
5. Unified task calendar (tasks with dates surfacing on a daily page) (Notion/Tana/Reflect contexts; digests): community-digest.md, thread3-digest.md
6. RAG chat over your own notes (local-first AI; Tolaria model-provider chat; digests): thread-c-local-models.md, tolaria.md, community-digest.md
7. AI stylistic mimicry: AI output in your own handwriting/style rather than generic typed font (Goodnotes complaint generalized): apps-likes-wants.md
8. Flashcards/study mode built in (Amphi canvas app; digests): apps-likes-wants.md, community-digest.md
9. Publishing (turn notes into a site/blog) (Obsidian Publish context; digests): community-digest.md
10. Web companion (access notes from a browser) (Tolaria alpha "remote client"; digests): tolaria.md, community-digest.md
11. Real-time collaboration (multiplayer editing) (Miro/Milanote/OneNote contexts; Logseq DB offline-first RTC goal; digests): apps-likes-wants.md, thread-b-storage.md, thread3-digest.md
12. Tiered roles for collaboration (viewer/editor/admin) (Notion permissions context; digests): community-digest.md, thread3-digest.md
13. Pen/keyboard/touch auto-switching like OneNote (input-mode findings): input-mode-switching.md
14. Cloud-backend choice (self-host or pick your provider instead of vendor cloud) (Amphi Notes self-host; Anytype backup nodes; Reflect Open iCloud/Git): apps-likes-wants.md, thread-b-storage.md
15. Paragraph-level links that survive moves/edits (block-reference durability; Logseq block refs; digests): thread3-digest.md
16. Encrypted backup (E2E-encrypted backups user can verify) (Anytype/Reflect contexts; digests): thread-b-storage.md, community-digest.md
17. Standard-format export that keeps properties/types (Anytype 0.47.4 story; Logseq DB export worries; Tana subset export): thread-b-storage.md
18. A live two-way file mirror of a structured workspace (Thymer model; Logseq's unshipped goal): thread-b-storage.md
19. Ink that never rewrites what you wrote (Goodnotes): apps-likes-wants.md
20. Optional (not forced) handwriting completion/spellcheck (Goodnotes 6): apps-likes-wants.md
21. AI output rendered in handwriting (Goodnotes): apps-likes-wants.md
22. Pay once, keep everything (Notability/Noteshelf lifetime pattern; Evernote/Obsidian pricing): apps-likes-wants.md
23. Sync never held hostage to a subscription (Notability iCloud lock): apps-likes-wants.md
24. Honor lifetime purchases across major versions (Noteshelf 2 to 3): apps-likes-wants.md
25. Fair/regional sync pricing (Obsidian): apps-likes-wants.md
26. Built-in effortless sync without plugin dependence (Obsidian): apps-likes-wants.md
27. Full offline mode (whole workspace, not per-page) (Notion): apps-likes-wants.md
28. Local data portability; no storage-format lock-in (Notion, Evernote, Anytype, Tana): apps-likes-wants.md, thread-b-storage.md
29. Guaranteed-lossless export (JSON dump of the whole store + Markdown projection + JSON Canvas for canvases) (synthesis in thread-b): thread-b-storage.md
30. Full export/backup for canvas apps (Milanote roadmap poll; "No Easy Export / Backup?"): thread-b-storage.md
31. Edit history on canvas boards (Milanote): apps-likes-wants.md
32. Usable mobile apps at parity with desktop (Milanote, Anytype, Tana, Noteshelf, Reflect, OneNote): apps-likes-wants.md
33. Nested folders/sections (OneNote): apps-likes-wants.md
34. Performance that survives a large corpus (Notion, Miro, Logseq, Obsidian, Tana, Milanote): apps-likes-wants.md
35. Notion-grade database features (formulas, linked views) in private/local apps (Anytype, Reflect): apps-likes-wants.md
36. Supertag-like structure learnable in minutes (Tana): apps-likes-wants.md
37. Daily-notes calm at a local-first price point (Reflect): apps-likes-wants.md
38. Better attachment management (Reflect): apps-likes-wants.md
39. Vector PDF export (Noteshelf deciding feature): apps-likes-wants.md
40. Time-synced audio: tap ink/text to jump in the recording (Notability signature): apps-likes-wants.md
41. Note-taking possible while a study widget/overlay is open (Amphi): apps-likes-wants.md
42. A marketplace for stickers/planners/templates (Goodnotes has it; wanted elsewhere): apps-likes-wants.md
43. A whiteboard that stays fast as the board grows (Miro): apps-likes-wants.md
44. Trustworthy archive you own forever (Evernote): apps-likes-wants.md
45. A third-party security audit for private/encrypted apps (Anytype): apps-likes-wants.md
46. AI over note context with direct model-provider choice (Tolaria): tolaria.md
47. Bundled MCP server / agent tool surface for the vault (Tolaria): tolaria.md
48. Custom views authored by AI (views-as-YAML with natural-language dates) (Tolaria): tolaria.md
49. Git-as-sync with AutoGit idle/focus auto-commit (Tolaria): tolaria.md
50. Wikilinks that auto-update on rename (Tolaria; the inverse of Obsidian's rename-fanout cost): tolaria.md, thread-b-storage.md
51. Truly native (non-web-wrapper) desktop shells (Tolaria HN demand): tolaria.md
52. Feature focus, no churn/creep ("stay focused like Bear"; "we don't need new features") (Tolaria, Goodnotes): tolaria.md, apps-likes-wants.md
53. Per-block capability grants with auditable prompts for embedded terminal/webhook/cron blocks (thread-f security model; the Obsidian vault RAT as the anti-pattern): thread-f-editor-platform.md
54. Beyond-.md structure (a database) without abandoning files (Obsidian forum hunger): thread-b-storage.md
55. Support notes that are not dashes-per-line Markdown (Logseq portability complaint): thread-b-storage.md

## 2. Feature clusters

The recurring themes across apps, grouped:

- Capture versatility: web clipper (Evernote, Tana, Reflect), voice transcription (Reflect), audio-with-ink (Notability, Goodnotes, Noteshelf), quick capture that can be developed later (Goodnotes), inbox capture-vs-organize lifecycle (Tolaria), widget capture (xnotes-android). The wish list adds flashcards/study capture (Amphi) and PDF/image overlay capture (OneNote).: apps-likes-wants.md, tolaria.md, deep-repos-a.md
- Search-everything: OCR inside images and handwriting (Evernote, Goodnotes, OneNote), handwriting-box search (Goodnotes best-in-class), semantic command palette (Tolaria), deep archive search (Evernote), indexing (thread-d). Users consistently name search as the retention feature.: apps-likes-wants.md, thread-d-indexing.md, tolaria.md
- Local-first AI: direct model-provider choice including local (Ollama, LM Studio) versus cloud (Tolaria), GPT assistants (Reflect, Notion, Evernote), AI command bar (Tana), AI commit messages and AI-authored views (Tolaria), RAG chat over notes (digests). The community wants AI on their own terms, over their own notes.: tolaria.md, thread-c-local-models.md, apps-likes-wants.md
- Handwriting: ink rendering quality as a deciding feature (Noteshelf fountain pen; Notability best-in-class), ink fidelity versus AI smoothing (Goodnotes complaint), handwriting OCR search/conversion (Goodnotes), pen/touch/keyboard auto-switching (OneNote reference behavior), reverse-engineering Nebo's handwriting engine (myscript-nebo-reverse).: apps-likes-wants.md, input-mode-switching.md, myscript-nebo-reverse.md
- Canvas: infinite freeform canvas as thinking space (OneNote loved core), real-time collaborative boards (Miro, Milanote), canvas-as-database-view (AFFiNE/BlockSuite edgeless), whiteboards stored as files (Tolaria/tldraw), the live canvas-note bridge (Obsidian Canvas sibling-file design; Heptabase and AFFiNE one-store designs), and canvas-app mortality risk (Muse's wind-down: handed to Adam Wulf as Muse 3.0 and rebranded Allume in June 2026).: apps-likes-wants.md, thread-b-storage.md, thread-f-editor-platform.md
- Databases/structure: relational databases with views (Notion loved and complained about), supertags (Tana), objects/sets/collections (Anytype), blocks with persistent IDs (Logseq DB, BlockSuite Y.Map, Trilium's why-database argument), types-as-lenses without schemas (Tolaria). The cluster's tension: structure wants a database, portability wants files, and no surveyed app has shipped both at high fidelity (Thymer mirror, Logseq two-way sync, both unproven).: apps-likes-wants.md, thread-b-storage.md, thread-f-editor-platform.md, tolaria.md
- Sync/trust: the single most-named pain across every community (OneNote, Anytype, Logseq, Obsidian, Notion, Reflect, Notability). Sub-themes: sync that is fast and never lost data, sync not held hostage to subscriptions, E2E encryption people can verify (Anytype, Reflect), Git-as-sync (Tolaria), P2P/local sync (Anytype), self-hosted sync servers (Amphi), and the warning that generic cloud sync corrupts database stores (Trilium's document.db).: apps-likes-wants.md, thread-b-storage.md, tolaria.md
- Export/anti-lock-in: plain local files as the loyalty anchor (Obsidian), export fidelity as the pressure valve and its repeated failures (Anytype pre-0.47.4, Tana subsets, Logseq properties lost, Milanote per-board only), conversion tooling as a category (ConvertOneNote2MarkDown, TanaMigrator), guaranteed-lossless export as the synthesis (JSON dump + Markdown projection + JSON Canvas), and JSON Canvas as the proven open canvas format.: thread-b-storage.md, apps-likes-wants.md, deep-repos-c.md
- Extensibility: plugin ecosystems as gravity (~9,500 Obsidian plugins, registry ~9,521 entries Oct 2026), plugins as the security surface (the 2026 Obsidian vault RAT campaign; the Tasks-plugin RCE; the per-block grant model as the proposed fix), MCP servers and AGENTS files as the new agent-facing extensibility (Tolaria), embedded app blocks (OnlyOffice, Excalidraw, VLC, Audacity, and the rest of the integrations findings), and embedded terminal/webhook/cron blocks only under core-enforced invariants (thread-f).: thread-f-editor-platform.md, integrations-1.md, tolaria.md, apps-likes-wants.md

Cross-cutting conclusion carried from the findings: the three recurring gaps across all fourteen mainstream apps are (1) sync that is fast, reliable and either free or fairly priced; (2) local files/ownership with easy export; (3) performance that survives a large real corpus. An app that nails all three while keeping any signature modeling idea learnable in minutes addresses the most-named pain in every community studied.: apps-likes-wants.md

## R5 additions: the study/PDF-textbook angle (BookCraft idea research)

- The BookCraft idea as submitted (community suggestion, R5): a dedicated everyday study space for stylus students, explicitly not a PDF editor: its own library with notebooks, imported PDF textbooks and study materials organized by subject or course; notebook feel with natural handwriting, customizable pens and highlighters, easy movement between pages and materials; Drawboard PDF named as the inking-quality reference.: R5-user-link
- Drawboard PDF, what people like: pressure ink feel, dockable favorites-bar tool configs, palm rejection called better than Acrobat's, calibrated measurement/protractor toolset unique in the category.: findings/r5-drawboard-pdf.md
- Drawboard PDF, what people want changed: performance rot in long sessions and on large PDFs, no tabs or pinnable folders, missing in-place paste and hotkeys, free-tier upsell nags, lasting anger at the 2023 move of pressure ink behind Pro. Nothing open source.: findings/r5-drawboard-pdf.md
- The load-bearing study feature set, consistent across every app surveyed: import arbitrary PDFs into a course-organized library; freehand pen/highlighter plus text-layer highlighting; excerpt-to-note linking back to the source page (Flexcil gestures, LiquidText canvas, MarginNote mindmap, Zotero extraction); split view of textbook and notebook; search across handwriting and annotations; lossless export of the annotated PDF; study aids built on annotations (flashcards, quizzes, hide-to-memorize, tape tools).: findings/r5-study-apps-landscape.md
- Most-wanted across study communities: trustworthy sync (Flexcil's number-one request), ink smoothing, pixel eraser and shape tools, layers separating annotations from content (requested even of Notability), true PDF support (OneNote printout is the anti-pattern: image pages, misalignment, memory blowups), large-textbook performance (Goodnotes praised for exactly this), annotation write-back into the source PDF, stable non-subscription pricing (the loudest theme in every community), an end to the two-app pairing problem (Flexcil + Noteful named combos).: findings/r5-study-apps-landscape.md
- Loved differentiators worth stealing: Write's ink-manipulation primitives (select, move, erase, reflow handwritten text); University Notes' memorization layer mechanics on PDFs; Xournal++'s independently movable annotation objects; ZotFile's click-through links from notes back to PDF locations.: findings/r5-study-apps-landscape.md
- Verdict: no app is the unified dedicated study notebook over textbooks; the gap is real but contested (Flexcil closest on workflow but engine-limited, MarginNote deepest system but rigid and buggy, mainstream annotators treat the textbook as one content type). Documented traps for a new entrant: subscriptions, buggy updates, large-PDF performance, sync.: findings/r5-study-apps-landscape.md
- IdeaCraft (aamirenic, MIT): young but directly relevant Rust/Tauri reference: SQLite schema (db.rs), Tauri command layer (commands.rs), sync-folder design and smoke-test harness are pullable under MIT. No handwriting, no mobile. Not part of the ArtCraft family despite the name; rickyb82/ideacraft is the unrelated namesake.: findings/r5-ideacraft.md

## R6 additions: synthesis from the full-depth sweep (12 findings files)

- Obsidian plugin demand signal (16 plugins, registry cross-checked, licenses verified at each repo): self-hostable E2E sync, a Dataview-style query layer, note-embedding canvases, code-running templates, and the file browser as product surface.: findings/r6-obsidian-plugins.md, findings/r6-oss-repos-batch-d.md
- Obsidian plugin cautionary evidence: Kanban orphaned with a version over a year old, Dataview's loudest complaint is table loading speed, Templater has a genuine license conflict (AGPL package.json vs GPL badge, no LICENSE file) needing a human check before any pull decision.: findings/r6-obsidian-plugins.md, findings/r6-oss-repos-batch-d.md
- jpzk/opensidian is the closest existing project to ours: a GPL-3.0 Rust+Tauri v2 clean-room Obsidian clone claiming to run real community plugins; concepts only under GPL, but its restricted-mode plugin trust design is worth copying.: findings/r6-obsidian-plugins.md, findings/r6-oss-repos-batch-d.md
- Sync/CRDT verdict: the CRDT + E2EE intersection is no longer under-documented. Automerge/Keyhive's BeeKEM, Loro's experimental protocol-e2ee, any-sync's encrypted DAGs, secsync's snapshot/AEAD model, and p2panda's post-compromise security all attack it directly.: findings/r6-sync-crdt-stack.md, findings/r6-unverified-resolutions.md
- Sync/CRDT verdict: Rust-native options (yrs, Loro, iroh, automerge's Rust core, nostr-sdk) are real and shippable.: findings/r6-sync-crdt-stack.md, findings/r6-unverified-resolutions.md
- Sync/CRDT license corrections: diamond-types is ISC not MIT, secsync is Apache-2.0 not AGPL-3.0 (last npm publish mid-2024, effectively dormant), TanaMigrator and snlib carry no license (code unpullable).: findings/r6-sync-crdt-stack.md, findings/r6-unverified-resolutions.md
- Sync/CRDT correction: The "Notion uses Yjs" claim was dropped; Notion's own engineering blog describes its own CRDT approach without confirming Yjs.: findings/r6-sync-crdt-stack.md, findings/r6-unverified-resolutions.md
- Handwriting verdict: TrOCR (MIT) is the best open handwriting-to-text engine (IAM CER 2.89 large / 3.42 base / 4.22 small; okraPDF independent testing put TrOCR-large at 3.68 CER, best non-VLM result).: findings/r6-htr-ocr-engines-a.md, findings/r6-htr-ocr-engines-b.md
- Handwriting verdict: Tesseract is disqualified for handwriting (49.58% CER, zero lines exact); ML Kit Digital Ink is stroke-input only and proprietary; PARSeq is scene-text only.: findings/r6-htr-ocr-engines-a.md, findings/r6-htr-ocr-engines-b.md
- Handwriting gaps that remain: temporal line segmentation for online (stroke-based) HTR is unsolved, and general OCR engines stay poor at real handwriting.: findings/r6-htr-ocr-engines-a.md, findings/r6-htr-ocr-engines-b.md
- Handwriting verdict: The Supernote .note format is fully reverse-engineered (philips/supernote-typescript, Aug 2026: TOTALPATH per-stroke trails with pressures and tilts, RATTA_RLE bitmaps, partial-erase fragments, embedded MyScript iink files), giving a real path to pull stylus-vault functionality; snlib (Rust) exists but carries no license.: findings/r6-xournal-rnote-supernote.md
- Local AI verdict: small open-weights models are viable per task with license discipline. Qwen3-Embedding-0.6B (Apache) as default RAG embedder, sqlite-vec brute-force sufficing at notes-app corpus sizes.: findings/r6-local-ai-models.md
- Local AI verdict: batch Whisper feasible on phones while streaming STT needs Moonshine (MIT) or platform APIs (whisper.cpp Android streaming runs slower than realtime; the exact ratio UNVERIFIED in the R8 fact-check).: findings/r6-local-ai-models.md
- Local AI verdict: Kokoro-82M the desktop TTS pick, KittenTTS and Supertonic phone-size but with license warnings, Piper GPL (concepts only).: findings/r6-local-ai-models.md
- Local AI runtimes: MLC, ExecuTorch, Core ML, ONNX Runtime, MediaPipe/LiteRT, plus Rust-native candle, mistral.rs, burn.: findings/r6-local-ai-models.md
- Local AI verdict: Ollama is a desktop distribution layer, never the mobile mechanism.: findings/r6-local-ai-models.md
- Local AI license traps: Llama Community and Gemma Terms are not OSI licenses; a pre-ship license-verification checklist is in the findings file.: findings/r6-local-ai-models.md
- Minor-apps verdict: across Squid, Concepts, Saber, Workflowy, DEVONthink, ente, Kinopio, Poznote, Tangent, Lockbook and the rest, the demand pattern is consistent.: findings/r6-batch1-minor-note-apps.md, findings/r6-batch2-minor-note-apps.md
- Minor-apps verdict: Sync trust is the category's weakest point (Squid's sync unshipped ~2 years, Samsung Notes duplicating conflicts instead of merging, OneNote sync partnership ending July 2026).: findings/r6-batch1-minor-note-apps.md, findings/r6-batch2-minor-note-apps.md
- Minor-apps verdict: Subscription-and-pack paywalls breed resentment (Concepts, Squid Premium, Obsidian Publish at 8 dollars per site per month).: findings/r6-batch1-minor-note-apps.md, findings/r6-batch2-minor-note-apps.md
- Minor-apps verdict, most liftable local-first patterns: Kinopio's localStorage-first with queued ops and websockets, Lockbook's Rust core with E2EE, Saber's dual-password E2EE Nextcloud sync.: findings/r6-batch1-minor-note-apps.md, findings/r6-batch2-minor-note-apps.md
- Minor-apps verdict: File-format anxiety recurs wherever a closed format is the only container (.sbe, .note, Squid's Premium-walled backups).: findings/r6-batch1-minor-note-apps.md, findings/r6-batch2-minor-note-apps.md
- Editors/publishers verdict: Dillinger's client-side-only rendering and the Homebrewery's markdown-in themed-PDF-out pipeline are both directly liftable patterns; Ghost's Koenig editor and Ghost 6.0's split-services architecture matter if publishing becomes a surface; proofeditor's notes-to-AI contract is a live experiment to watch rather than copy.: findings/r6-editors-publishers.md
- Editors/publishers verdict: The Samsung Notes deep dive exposed the trust pattern of the whole category: PDF export rasterizes handwriting, no bulk export, sync conflicts duplicate instead of merge.: findings/r6-editors-publishers.md
- Nostr/transports verdict: concepts-only for sync plus an optional export path. At least four shipped apps sync notes over Nostr, but relay economics (471 public relays, 343 offline) and the single-identity-key conflict with per-note keys argue against Nostr as primary transport.: findings/r6-nostr-transports-extras.md
- Nostr/transports verdict: Pull regardless: negentropy set-reconciliation (NIP-77) and NIP-44 padding discipline; NIP-44 v2 is Cure53-audited.: findings/r6-nostr-transports-extras.md
- Nostr/transports verdict: nostr crate 0.45.5 runs ~446K downloads/month (crate 0.45.5, Oct 2026).: findings/r6-nostr-transports-extras.md
- Nostr/transports verdict: iroh (MIT/Apache, 1.0 June 2026, default transport in Anytype) is the stronger Rust-native p2p lane.: findings/r6-nostr-transports-extras.md
- Verify-pass closure: 34 unverified entries tracked, 22 resolved, 5 partially, 7 not found.: findings/r6-unverified-resolutions.md
- Verify-pass license corrections applied: diamond-types ISC, secsync Apache-2.0, snlib and TanaMigrator no-license-unpullable, Xournal++ bare GPL-2.0, RNote GPL-3.0-or-later (not Apache/EUPL as first assumed).: findings/r6-unverified-resolutions.md
- Verify-pass closure: fbalobaf/supernote-viewer is gone. "Notion uses Yjs" dropped. One independent Loro-vs-Y.rs-vs-Automerge benchmark exists (giosuel/imaginarium PR 16). Still open: KHATT derivative-weights licensing, Dillinger phishing accusation unverified by design.: findings/r6-unverified-resolutions.md

Sources: the twelve findings/r6-*.md files (r6-batch1-minor-note-apps, r6-batch2-minor-note-apps, r6-editors-publishers, r6-sync-crdt-stack, r6-htr-ocr-engines-a, r6-htr-ocr-engines-b, r6-xournal-rnote-supernote, r6-local-ai-models, r6-obsidian-plugins, r6-oss-repos-batch-d, r6-nostr-transports-extras, r6-unverified-resolutions).

## R7 additions: per-app feature inventories, internet-wide sentiment, remake landscape, and the 11 user-supplied repos

- Feature-inventory closure: 20 majors, 19 OSS apps, and 19 handwriting/study subjects now carry per-feature inventories with a URL on every captured claim; where a page could not be captured the claim is marked UNVERIFIED this session, not filled.: findings/r7-feature-inventory-majors.md, findings/r7-feature-inventory-oss.md, findings/r7-feature-inventory-handwriting.md
- Feature-inventory closure, new verified facts: Kinopio's full localStorage + idb-keyval + queued-API-ops architecture from the author's own writeup with exact pricing ($8/mo, $80/yr, $250 lifetime, 100-card free cap).: findings/r7-feature-inventory-majors.md, findings/r7-feature-inventory-oss.md, findings/r7-feature-inventory-handwriting.md
- Feature-inventory closure, new verified facts: DEVONthink's OCR engine chain (ABBYY per vendor FAQ, Vision-based recognition in DT4, Pro/Server gating) and AES-256 sync locations.: findings/r7-feature-inventory-majors.md, findings/r7-feature-inventory-oss.md, findings/r7-feature-inventory-handwriting.md
- Feature-inventory closure, new verified facts: tldraw's open-SDK/closed-app split with its Durable-Objects/SQLite/R2 sync stack, Make Real, and an official MCP App (March 2026).: findings/r7-feature-inventory-majors.md, findings/r7-feature-inventory-oss.md, findings/r7-feature-inventory-handwriting.md
- Sentiment verdict (internet-wide, beyond the Discord threads): 8 ranked demands, each backed by at least two independent sources.: findings/r7-user-sentiment-sweep.md
- Sentiment verdict, top three: offline/local-first with plain-file ownership as the dominant switch motive, anger at subscription rug-pulls of lifetime buyers (Evernote under Bending Spoons, Notability 2021, GoodNotes' buried one-time tier), sync that never loses data including mobile.: findings/r7-user-sentiment-sweep.md
- Sentiment verdict: Handwriting demand stands as a combined gap: ink feel plus search-without-conversion plus formula handling plus cross-platform sync plus open export has no combined answer (Nebo best at recognition but bare).: findings/r7-user-sentiment-sweep.md
- Sentiment honesty check: local-first/E2EE is loud as the grammar of PKM switchers but niche as a standalone purchase driver outside those bubbles.: findings/r7-user-sentiment-sweep.md
- Remake-landscape verdict: 33 projects mapped, 17 verified alive, 13 dead with evidence, 3 unresolvable this session.: findings/r7-remakes-evernote-notion.md
- Remake-landscape verdict, four death patterns named with evidence: vendor adopt-then-drop (Focalboard), single-maintainer exit (Notea, Athens), incumbent-API dependence (NixNote2, Geeknote, Everpad), acqui-deletion (Skiff).: findings/r7-remakes-evernote-notion.md
- Remake-landscape verdict: Migration pain documented from first-person sources: Evernote ENEX fragility and OCR-index loss, Notion export silently degrading relations/rollups.: findings/r7-remakes-evernote-notion.md
- User-repos verdicts: the strongest new pull-from candidates are SiYuan's dejavu snapshot/provider abstraction with repo-key E2EE (top candidate; WebDAV ETag fragility flagged as an anti-pattern), Memos' single-binary + AI-provider-abstraction story (no sync engine, no E2EE), NexaNote's per-point-pressure ink canvas with tested WebDAV conflict resolution (MPL-2.0), and edgeever's triple-write storage (JSON+Markdown+text) with an offline sync queue.: findings/r7-user-repos-a.md, findings/r7-user-repos-b.md
- User-repos verdicts: Turtl's Rust core carries a real per-space-key E2EE design but the project is effectively stalled.: findings/r7-user-repos-a.md, findings/r7-user-repos-b.md
- User-repos verdicts: notion-re (showcase-only), zappynotes (hiatus), and owlistic (event-bus pattern only) contribute little.: findings/r7-user-repos-a.md, findings/r7-user-repos-b.md

Sources: the seven findings/r7-*.md files.

## R12 additions: evidence-enrichment round (2026-10-27)

- Annotation layers are becoming their own market segment: Hypothesis has pivoted to selling an annotation layer into LMS integrations (social annotation inside Canvas and Blackboard courseware), while layer panels are now the headline differentiator across iPad note/PDF apps (Noteful, Drawboard Pro, Notes+, FreeNotes), and community confusion about which apps actually have layers shows demand running ahead of the vocabulary.: findings/r12-enrich-a.md
- Write's line-of-strokes reflow is the borrowable ink mechanic: strokes selected as words and lines that reflow when text is inserted, with other projects' issues explicitly requesting it be copied, and third-party analysis (partly UNVERIFIED) reading it as strokes-as-words with join/split geometry.: findings/r12-enrich-a.md
- Study-recall mechanics are going native rather than living in hackwork: University Notes ships a memorization layer purpose-built for the workflow (cover sheet, per-colour hiding, layer-hiding Q&A, tape over the answer), FreeNotes adds an Active Recall Tape, Meridian-Notes wraps its canvas in a full study suite (Anki import, leech list, exam forecast, recall and Feynman panels, speed reader), and SiYuan adds an FSRS scheduler.: findings/r12-enrich-a.md, findings/r12-enrich-f.md, findings/r12-enrich-g.md
- Trust repair after subscription conversions has a working template: Drawboard's Legacy License restores the pre-conversion entitlement to long-time users at no cost, the most durable goodwill signal recorded in the study/PDF category.: findings/r12-enrich-a.md
- Agent surfaces are becoming a product axis, not a bolt-on: PDFCraft treats CLI, JSON output, an MCP server and a headless loopback as first-class surfaces; QOwnNotes and notecraft ship MCP servers; CapsuleCraft and opensidian-mcp are independent MCP servers aimed at agents.: findings/r12-enrich-a.md, findings/r12-enrich-f.md, findings/r12-enrich-g.md
- Proofeditor's agent editing protocol is a reference design for safe AI edit-in-place: two endpoints (prepare, provide), edits targeting visible text, structural suggestions failing closed rather than firing blind.: findings/r12-enrich-e.md
- LumaFusion's magnetic-and-track hybrid timeline is the no-mode-switch answer: classic tracks stay available for precision editing while magnetic clips are opt-in per section, so neither workflow forces a mode change or excludes the other.: findings/r12-enrich-e.md
- Adjustment Clips are the borrowable non-destructive cascade: in CapCut, a filter or grade applied to an adjustment clip cascades to every clip below it without touching their parameters.: findings/r12-enrich-e.md
- Format openness decides who builds the tooling: Supernote's closed .note format bred a reverse-engineering ecosystem (the R6 format work plus an active eReadersForum reverse-engineering thread), while Write's SVG storage and plain-file-folder stores (notecraft's "sync with the folder", xnotes-android's files-in-a-folder) invite integrations for free.: findings/r12-enrich-a.md, findings/r12-enrich-f.md, findings/r12-enrich-g.md
- Quantified parity disclosure and honest self-comparison are working as trust marketing: notecraft's PARITY.md (61 of 67 checklist items), PDFCraft's own 57%-parity disclosure with UX-mode differentiation, memos' compare page conceding losses to Obsidian, and CapsuleCraft's comparison table.: findings/r12-enrich-a.md, findings/r12-enrich-f.md, findings/r12-enrich-g.md
- EdgeEver's triple-format storage (markdown plus SQLite plus media files) is the concrete proof of the "plain files but indexed" architecture.: findings/r12-enrich-g.md
- Sync diagnostics are a shippable feature, not a debug page: NexaNote surfaces sync state as an explicit diagnostics panel with a dry-run command before changes apply.: findings/r12-enrich-g.md
- Session-based revision history with agent-safety labels: Poznote snapshots at 10-minute sessions with thinning, and "Before AI/MCP" labels make agent-era changes distinguishable in history.: findings/r12-enrich-d.md
- Privacy fencing has converged on one shape across small apps: diktafon's consent-first cloud (nothing leaves without consent), marmalade's opt-in cloud with the user's own key, opensidian's restricted mode outside the vault for untrusted plugins, and CapsuleCraft's on-device critique engine.: findings/r12-enrich-d.md, findings/r12-enrich-f.md

Corrections to earlier findings:
- Goodnotes: R8/R11-cached pricing superseded — the 2026 ladder adds Free and Teams tiers, Special Edition is a region-variable Apple one-time rather than flat $29.99, and Android is a supported platform; pricing was re-architected in 2026, not the 2023 launch model.: findings/r12-enrich-a.md
- Notability: cached plan ladder (Free/Classic/Plus, iPad/Mac only) superseded by Starter/Lite/Plus/Pro/Business with a $79.99/yr Pro tier, a web beta, and Android handwriting recognition; earlier one-time $9.99 and $14.99 Pro annual no longer match.: findings/r12-enrich-a.md
- Noteshelf: pricing and platform coverage re-verified in 2026 — $7.99 universal one-time on Apple plus freemium Android, AI features exist on Android/Windows, and Google Drive sync Android↔Windows now exists (Apple↔Windows still does not).: findings/r12-enrich-a.md
- MarginNote 4: the "MN3 one-time purchase for everything" picture no longer holds in MN4's tiered model — a "lifetime" Max purchase stops including AI credits after 3 years and OCR is Max-gated.: findings/r12-enrich-a.md
- Zotero: aggregator monthly pricing wrong ($20/month vs official yearly); "citation-only" is stale — since Zotero 6-8 it is a full PDF/EPUB reader-annotator.: findings/r12-enrich-a.md
- Amphi: widget row superseded — the canvas app now ships a much larger widget catalog with published pricing (a beta-to-1.1.4 progression that reads as a conflict when sources are compared side by side).: findings/r12-enrich-a.md
- Evernote: pricing ladder and platform list re-verified — current Free/Starter $99/Advanced $249.99 with note-count caps; old Personal $14.99/Professional $17.99 pages stale; the "50-note free cap" row is confirmed and sits inside the new ladder.: findings/r12-enrich-b.md
- OneNote: free tier confirmed against a "no free plan as of September 2026" claim; pricing rows expanded from the cached "free with 5GB"; M365 Personal $9.99 vs $6.99 is likely list vs promotional.: findings/r12-enrich-b.md
- Notion: pricing re-verified — Plus $10/Business $20 annual with AI included on Business (a stale tracker said Plus $12/Business $18 plus a $10 AI add-on); "no real offline" folklore split: the 2025 offline mode shipped, reliability complaints persist.: findings/r12-enrich-b.md
- Obsidian: pricing/platform rows re-verified; commercial license, Publish and Bases added as documented facts; a 2026 review's "2,700+ community plugins" is stale against the Oct 2026 registry count of ~9,521.: findings/r12-enrich-b.md
- Miro: pricing/platform rows filled from 2026 evidence and the Bending Spoons acquisition added as the dominant community story; free-plan behavior documented as "only the three most recent boards remain editable".: findings/r12-enrich-b.md
- Milanote: free-tier mechanics (100 combined cards, 10 file uploads) and platform coverage added; the cached ~$100/yr price is confirmed and restated per month.: findings/r12-enrich-b.md
- Anytype: pricing rows added (Free/Pro $10/Ultra $20 after Aug 2026 raises) and the no-web-client limit recorded; nothing in the R11 rows proved wrong.: findings/r12-enrich-b.md
- Tana: two different "Tana" products now exist (outliner vs meeting platform) with different pricing; the pricing row now records the 2026 product split rather than one ladder, and Meeting Agent/Capture rows were added.: findings/r12-enrich-b.md
- Reflect: pricing detail (trial, annual price, single plan) and platform list added; CostBench's own pages conflict and the cached "~$10/mo, no real free tier" row stands confirmed.: findings/r12-enrich-b.md
- Samsung Notes: the 2018-2026 OneNote sync option was removed after July 2026 and Samsung's support page confirms it is "no longer available"; the widely repeated "Samsung Notes syncs with OneNote" fact is no longer true as of late 2026.: findings/r12-enrich-b.md
- Logseq: the section now records the 2026 OG/DB two-track split, the alpha RTC sync and DB mobile apps, and donation-based sync tiers, none of which the cached rows captured.: findings/r12-enrich-b.md
- Trilium: the canonical repo is no longer zadam/trilium — ownership transferred to the community (TriliumNext) and the project regained the Trilium name; earlier zadam/trilium URLs now resolve to community-maintained pages.: findings/r12-enrich-c.md
- Saber: AlternativeTo's "work-in-progress, not ready to trust" description is stale against current reality — stable releases (Aug 2026) across seven platforms and real multi-semester classroom users.: findings/r12-enrich-c.md
- Squid: a third-party listing's "premium features require a one-time purchase" is wrong or outdated — the official help center says premium is a subscription (with two features also available as one-off IAPs).: findings/r12-enrich-d.md
- Poznote (lane d corrections context): revision system recorded as shipped — 10-minute session snapshots with thinning and Before AI/MCP labels.: findings/r12-enrich-d.md
- Ghost: third-party roundups' "Starter $15, Standard $79" disagree with the official page (Starter $18, Publisher $29, Business $199 — the "Standard" name is stale); older "Ember admin" descriptions are outdated — the editor is React+Lexical since the Oct 2023 rewrite.: findings/r12-enrich-e.md
- Descript: some 2026 third-party pages mention a "Pro" tier; the official page's current tiers are Free/Hobbyist/Creator/Business (+Enterprise) — the Pro name is stale.: findings/r12-enrich-e.md
- open-notebook: the earlier "no repo" finding is outdated — a public repo exists.: findings/r12-enrich-f.md
- CapsuleCraft: the release-cadence row is superseded — v1.8.0 shipped 2026-10-26, one day after the cached v1.7.0 date, so the monthly-plus iteration is still accelerating.: findings/r12-int-features-patches.md
- opensidian: the thiagovasconcelosti repo is not a fork of jpzk/opensidian — R12 evidence shows an independent Node.js/TypeScript project that only shares the OpenSidian name, with a different stack, license and architecture; the cached install matrix also understated it (Debian 13 missing).: findings/r12-int-features-patches.md
- xnotes-android: cached version/status (v0.8.23, 269 stars) superseded by the v0.9.0 release; the Google Play signing-conflict note (issue #166) stands unchanged.: findings/r12-int-features-patches.md
- diktafon: cached store row described upstream, not the fork — store listings point at jaromiru/diktafon builds, so store installs do not include the fork's opt-in cloud features, and the fork's README reframes "nothing ever leaves the device" as "nothing leaves without consent".: findings/r12-int-features-patches.md
- marmalade-tts-android: the cached "Play and F-Droid in progress" store status is superseded — F-Droid is live (v1.1.0) and Play presence is UNVERIFIED; a GitHub mirror duplicates the README, and only maxwhipw's repo is referenced by F-Droid and privacyguides.: findings/r12-int-features-patches.md
- Tolaria: launch scale, author identity, 2026 feature velocity and the October iPhone/iPad ship are now recorded; the cached rows did not carry them (the at-launch Mac-only-download gap has since been resolved with signed Windows installers and a Homebrew cask).: findings/r12-int-features-patches.md
- AFFiNE: the section previously recorded only BlockSuite architecture evidence; 2026 product-level rows (positioning, pricing tiers, self-hosting, sentiment) are now added alongside it.: findings/r12-int-features-patches.md
- notecraft: the cached section carried only three feature rows; the 2026 sweep shows a far broader OneNote-alternative build-out (HTML/Markdown dual format, TeX, Mermaid, tags, .one import, MCP agent surface, 14 themes) and records the wants rows from open issues.: findings/r12-int-features-patches.md
- e-journal: the cached stack (egui/eframe, encrypted journal entries, mood tracking, AI summaries) and the 2026 sweep's stack (Tauri v2 with an ink canvas on the system WebView, single-JSON library, .ink import) describe substantially different apps; cached rows are kept but UNVERIFIED in 2026 sources and may reflect an earlier development stage.: findings/r12-int-features-patches.md
- neo: the section is expanded with the 2026 sweep's docs evidence (screenplays interop, export/import matrix, seeded cover art, omnibus bind, daily zip backups, Android Pocket client), none of which contradicts the cached rows.: findings/r12-int-features-patches.md

Coverage index:
- Lane A (r12-enrich-a.md): study/PDF majors, 17 apps — Goodnotes, Notability, Noteshelf, CollaNote, MarginNote 4, Flexcil, LiquidText, Xodo, PDF Expert, University Notes, Write (Styluslabs), Zotero, Hypothesis, Noteful/Freenotes/Notes+, Drawboard PDF, Drawboard Projects, PDFCraft (completion: 17 of 17).: findings/r12-enrich-a.md
- Lane B (r12-enrich-b.md): majors batch 1, 12 apps plus video supplements — Obsidian, Obsidian Publish, OneNote, Evernote, Notion, Craft, Anytype, Tana, Reflect, Milanote, Miro, Samsung Notes (completion: 12 of 12).: findings/r12-enrich-b.md
- Lane C (r12-enrich-c.md): majors batch 2, 12 apps plus video supplements — Logseq, Joplin, Notesnook, Trilium Notes, AFFiNE, ente, Heptabase, Kinopio, tldraw, Excalidraw, Saber, Lockbook (completion: 12 of 12).: findings/r12-enrich-c.md
- Lane D (r12-enrich-d.md): long-tail OSS and small apps, 19 entries — Squid, Concepts, Workflowy, DEVONthink, Muse, Thymer, Ideon, OwlLuna, Akasha, Pele, Poznote, Amphi, Amphi Notes, Tangent Notes, HelixNotes, Tolaria, sawt (UNVERIFIED), diktafon fork, marmalade-tts-android (completion: 19 apps).: findings/r12-enrich-d.md
- Lane E (r12-enrich-e.md): editors, publishers and video editors, 7 apps — Dillinger, Homebrewery, Ghost, Proofeditor, CapCut, Descript, LumaFusion (completion: 7 apps).: findings/r12-enrich-e.md
- Lane F (r12-enrich-f.md): OSS repo sweep, 17 repo entries plus video supplements — notecraft (multiple sections), nexlore, Meridian-Notes, capsuleos/CapsuleCraft, opensidian (two entries), e-journal, cheeterdev/notes, neo, xnotes-android, open-note, open-notebook verdict, BasScript verdict, OfficeIMO (completion: 17 of 17 repos).: findings/r12-enrich-f.md
- Lane G (r12-enrich-g.md): OSS batch 2, 15 app entries — turtl, Zettlr, QOwnNotes, blinko, edgeever, notion-re, zappynotes, owlistic, NexaNote, memos, SiYuan, Xournal++, RNote, MyScript/Nebo, Supernote ecosystem (completion: 15 apps; file header says apps 1-16).: findings/r12-enrich-g.md
- Total: about 99 app and repo entries across the seven lanes (17+12+12+19+7+17+15); the round was framed as ~104, with the delta from shared-name entries and verdict rows.

Sources: findings/r12-enrich-a.md, findings/r12-enrich-b.md, findings/r12-enrich-c.md, findings/r12-enrich-d.md, findings/r12-enrich-e.md, findings/r12-enrich-f.md, findings/r12-enrich-g.md, findings/r12-int-features-patches.md.
