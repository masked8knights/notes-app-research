# Round 12 — Lane A (evidence enrichment) — Group A apps
App order: Goodnotes, Notability, Noteshelf, CollaNote, MarginNote 4, Flexcil, LiquidText, Xodo, PDF Expert, University Notes, Write (Styluslabs), Zotero, Hypothesis, Noteful/Freenotes/Notes+, Drawboard PDF, Drawboard Projects, PDFCraft.

## Goodnotes
### Visual surface
- iOS/iPadOS (primary): notebook-grid library ("Landing page") with cover thumbnails, then a paper-editor with toolbar: pen/highlighter/eraser/lasso/shape/text/image tools, tool-color tray, and a dropdown of paper templates; a left sidebar (thumbnails/outline/bookmarks) and split-view support. The marketing site shows the editor with the new AI sidebar and dynamic templates. Visual evidence: https://www.goodnotes.com/features and https://www.goodnotes.com/pricing (product shots of editor + library).
- macOS: same document model (notebooks, text documents, whiteboards) in a windowed app; users report page-switch lag on Mac (https://www.reddit.com/r/GoodNotes/comments/17j3tld/is_goodnotes_6_really_that_bad/).
- Android/Windows/web: cross-platform app with core note-taking and PDF markup, sync via Goodnotes Cloud on Pro (https://www.goodnotes.com/pricing).
- SHOT-LIST (screens to capture):
  - Goodnotes iPad editor with toolbar + AI sidebar — https://www.goodnotes.com/features
  - Library/notebook grid view — https://www.goodnotes.com/features
  - Pricing page plan-comparison visuals — https://www.goodnotes.com/pricing
  - Math Assist in action — https://support.goodnotes.com/hc/en-us/articles/7459211888143-How-to-use-Math-Assist-Interactive-Exam-Practice
  - Goodnotes AI guide screens (Ask Mode, spellcheck) — https://support.goodnotes.com/hc/en-us/articles/10779112528399-A-guide-to-Goodnotes-AI
  - Goodnotes 6 launch visuals — https://www.goodnotes.com/blog/introducing-goodnotes-6

### Docs analysis
- Free plan: up to 3 files total across notebooks/text docs/whiteboards, 5 MB import size, 20 min audio recording per notebook, watermarked exports, up to 3 folders; notebooks above 3 become read-only (editable ones user-chosen) — https://www.goodnotes.com/pricing and https://support.goodnotes.com/hc/en-us/articles/13808767840015-Compare-Goodnotes-Plans-and-Features (snippet via search; page itself blocked 403)
- Plans: Free $0; Essential $11.99/yr (unlimited files/audio, no watermark, basic AI); Pro $35.99/yr (private link sharing, hosting real-time collaboration, cross-platform cloud sync, advanced AI incl. Meetings and Create Mode); AI Pass +$9.99/mo (~12x more AI credits); Special Edition one-time purchase on Apple only (no Goodnotes Cloud, limited AI); Teams $120/seat/yr (SAML SSO, domain control, admin console); Enterprise custom — https://www.goodnotes.com/pricing
- AI split: on-device no-credit features (Math conversion, Circle to Lasso, Spell check, Handwriting reflow, Convert to text, Scribble-to-erase) vs credit-based cloud AI (Ask Mode, quiz generator, Meeting AI, image generation) — https://support.goodnotes.com/hc/en-us/articles/10779112528399-A-guide-to-Goodnotes-AI
- Math AI is powered by Wolfram|Alpha LLM API with Solve/Teach Me modes — https://support.goodnotes.com/hc/en-us/articles/13683534670223-Goodnotes-AI-for-Math
- Study Sets with spaced-repetition "Smart Learn"; AI does not auto-generate flashcards from notes (third-party claim analysis) — https://studycardsai.com/blog/can-goodnotes-convert-notes-into-flashcards (UNVERIFIED against official docs; support.403)
- Layers is an experimental feature, iPad/Mac only, disabled during Pro trial — https://www.goodnotes.com/pricing (feature table)
- Education tier (Schools): teaching-only presentation layer, class folders, feedback mode, AI safety controls — https://www.goodnotes.com/pricing
- Security posture: SOC 2 Type 2, ISO 27001, GDPR/CCPA, AWS infra, Trust Center — https://www.goodnotes.com/pricing
- Design decisions worth borrowing: editable-vs-readonly graceful degradation above the free quota; split of on-device vs credit AI; "elements tool" (reusable sticker/clips); presentation mode with pointer; collaborative link sharing gated by host tier.

### Features
| Area | Detail |
|---|---|
| Handwriting | Pen styles, pressure sensitivity (iOS), shape recognition, handwriting reflow, scribble-to-erase, spellcheck for handwriting |
| PDF | Import/annotate PDFs, photos, JPG; 5 MB import cap on free |
| Structure | Notebooks, folders (3 free), text documents, whiteboards, bookmarks/outline, elements tool |
| Study | Study Sets flashcards, spaced repetition, quiz generator, math assist/conversion |
| Audio | Recording 20 min free / unlimited paid; transcription on iOS |
| Collaboration | Link sharing, comments, real-time collab (hosting = Pro) |
| Sync/backup | iCloud (iOS), Google Drive/OneDrive/Dropbox backup; Goodnotes Cloud cross-platform sync on Pro |
| Platform | iOS, macOS, Android, Windows, web |

### Sentiment
| What people say |
|---|
| Handwriting search praised as the killer feature vs competitors (https://www.reddit.com/r/GoodNotes/comments/1bhrpnz/is_goodnotes_6_worth_it_for_new_users/) |
| Massive anger at the GoodNotes 5→6 forced upgrade to subscription; "the last solid one-time purchase notes app" betrayal narrative (https://www.reddit.com/r/GoodNotes/comments/15mnzfk/dont_upgrade_to_goodnotes_6/) |
| Family Sharing not supported by subscription — parents of multiple kids refuse to upgrade (https://www.reddit.com/r/GoodNotes/comments/15n3yv2/raise_your_voice_impact_goodnotes_6_with_app/) |
| Stability/performance complaints: freezing, crashes on older iPads, Mac page-switch lag; some reverted to GN5 (https://www.reddit.com/r/GoodNotes/comments/17j3tld/is_goodnotes_6_really_that_bad/, https://www.sikayetvar.com/en/goodnotes-us) |
| Distrust of future pricing after the 5→6 pattern (https://www.reddit.com/r/GoodNotes/comments/1cv93w7/imo_goodnotes_6_is_untrustworthy_and_you_should/) |
| Subscription-family argument seen as hypocritical because Goodnotes had publicly mocked Notability's subscription switch (https://www.reddit.com/r/GoodNotes/comments/1cv93w7/imo_goodnotes_6_is_untrustworthy_and_you_should/) |

### Wants
| What people want changed |
|---|
| A genuine lifetime one-time purchase across platforms, not Apple-only Special Edition (https://www.reddit.com/r/GoodNotes/comments/15nfw1o/goodnotes_6_pricing_and_subscription_model/) |
| Family-shareable license (https://www.reddit.com/r/GoodNotes/comments/15n3yv2/raise_your_voice_impact_goodnotes_6_with_app/) |
| Performance fixes on Mac and older iPads (https://www.reddit.com/r/GoodNotes/comments/17j3tld/is_goodnotes_6_really_that_bad/) |
| Fewer AI features nobody asked for, more core writing reliability (https://www.reddit.com/r/GoodNotes/comments/15oklbw/goodnotes_6_is_fundamentally_wrong_its_simply_an/) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | 3 files, 5MB imports, 20-min audio, watermark, 3 folders |
| Essential | $11.99/yr, 7-day trial |
| Pro | $35.99/yr (cross-platform sync, collab hosting) |
| AI Pass | +$9.99/mo, ~12x AI credits |
| Special Edition | Apple one-time purchase (varies by region) |
| Teams | $120/seat/yr; Enterprise custom |
| Platforms | iOS, macOS, Android, Windows, web |

### Contradictions
- Goodnotes publicly criticized Notability's 2019 subscription switch, then moved to subscription itself with GN6 (https://www.reddit.com/r/GoodNotes/comments/1cv93w7/imo_goodnotes_6_is_untrustworthy_and_you_should/). Also note the "current Goodnotes is free for GN5 users" claim in one 2026 review (https://paperlike.com/blogs/paperlikers-insights/app-review-goodnotes-vs-notability) sits awkwardly against the paid Essential/Pro tiers now on the pricing page — the 2026 pricing is a re-architected model, not the 2023 launch one.

Sources: https://www.goodnotes.com/pricing ; https://www.goodnotes.com/features ; https://support.goodnotes.com/hc/en-us/articles/10779112528399-A-guide-to-Goodnotes-AI ; https://support.goodnotes.com/hc/en-us/articles/13683534670223-Goodnotes-AI-for-Math ; reddit threads above ; paperlike.com/blogs/paperlikers-insights/app-review-goodnotes-vs-notability

---
## Notability
### Visual surface
- iPad/iPhone: a Home tab (recent notes, records, imports), a horizontal-scrolling note editor where each "note" is one tall page you scroll sideways, right-side toolbox bar (pen/highlighter/eraser/text/photo/record/lasso), and the signature audio timeline strip under the note that shows synced playback with handwriting animation. App Store copy confirms PDF/doc import, form fill, real-time transcription (https://apps.apple.com/us/app/notability-smarter-ai-notes/id360593530).
- Mac: same document model; users report copy-paste being finicky (https://www.softwareadvice.com/productivity/notability-profile/).
- Web: a web version in beta, still weak — sync and subscription recognition failed in testing (https://beingpaperless.com/notability-15-review-is-it-worth-it/).
- SHOT-LIST:
  - Notability iPad editor with audio timeline — https://apps.apple.com/us/app/notability-smarter-ai-notes/id360593530 (App Store screenshots)
  - Home tab / Learn Home Screen with AI quizzes — https://blog.notability.com/post/notabilitys-back-to-school-2026-guide-every-new-feature-explained
  - Pricing page visuals — https://notability.com/pricing
  - Smart Notes / summaries screens — https://blog.notability.com/post/whats-new-in-notability
  - Page Manager bulk-actions view — https://blog.notability.com/post/welcome-to-the-next-generation-of-notability-11-0

### Docs analysis
- Free Starter: 5 free notes, all editing tools, PDF/doc import, 20,000+ templates, 7-day version history (https://notability.com/pricing)
- Individual tiers: Lite $11.99/yr (unlimited notes, iOS-only third-party backups); Plus $15.99/yr (limited AI: YouTube link-to-note, quizzes/flashcards, transcription; 30-day history); Pro $79.99/yr (unlimited transcription/summaries, chat with notes, 90-day history) (https://notability.com/pricing)
- Business: $60/user/yr and Business Pro $180/user/yr with shared libraries, live collaboration, Intune MAM, audit log (https://notability.com/pricing)
- Audio is the anchor: recording synced to handwriting; playback re-draws strokes per pixel; text syncs per second (https://beingpaperless.com/notability-2/)
- Live collaboration and cross-device sync run on "Notability Cloud"; handwriting recognition and math-to-LaTeX are iOS/Android only per the plan matrix (https://notability.com/pricing/compare)
- Version history is a paid differentiator: 7 days free, 90 days Pro (https://notability.com/pricing/compare)
- Fall 2026 additions: Calligraphy Pen, flashcard import from Anki/CSV, updated academic planner, AI quizzes on the Learn Home Screen (https://blog.notability.com/post/notabilitys-back-to-school-2026-guide-every-new-feature-explained)
- Study chapters from a specific PDF chapter rather than whole docs; edits sync instantly for collaborators (https://blog.notability.com/post/whats-coming-to-notability-this-semester) (UNVERIFIED detail of "instant" sync claim is marketing)
- Design decisions worth borrowing: per-pixel handwriting playback against audio; version history as a tier ladder; chapter-scoped AI; Home tab that mixes notes/recordings/imports.

### Features
| Area | Detail |
|---|---|
| Handwriting | Pencil/pen/highlighter, calligraphy pen (2026), multi-note split view, math→LaTeX (iOS/Android) |
| Audio | Synced recording+playback, live transcription, per-plan limits |
| AI | Smart Notes summaries, quizzes/flashcards, YouTube-to-note, chat with notes |
| PDF | Import/annotate PDFs, docs, slides; scan paper; form fill |
| Organization | Folders, handwriting search, shared libraries |
| Collaboration | Link sharing, live collaboration (Cloud) |
| History | 7/30/90-day version history by tier |

### Sentiment
| What people say |
|---|
| Audio-synced note playback still the most-praised feature, especially for lectures (https://paperlike.com/blogs/paperlikers-insights/app-review-goodnotes-vs-notability, https://www.reddit.com/r/ipad/comments/1d8e9of/a_quick_reminder_that_you_shouldnt_use_or/) |
| Data loss reports during device migration; iCloud sync unreliable, multi-day transfers (https://www.reddit.com/r/notabilityapp/ — migration thread) |
| A student reports losing a week of notes before an exam with no recovery (https://www.reddit.com/r/notabilityapp/comments/1o357au/whats_the_upsides_and_downsides_of_notability/) |
| "Worst pricing setup" criticism for a handwriting app in 2025/26; web version not ready (https://beingpaperless.com/notability-15-review-is-it-worth-it/) |
| Copy/paste finicky in reviews of the desktop experience (https://www.softwareadvice.com/productivity/notability-profile/) |

### Wants
| What people want changed |
|---|
| A trustworthy lifetime/one-time option that doesn't break on device migration (https://www.reddit.com/r/notabilityapp/ — migration thread) |
| Restored playback-speed toggle on the timeline (regression in v14) (https://medium.com/@paperlessx/notability-15-review-is-it-worth-it-b7d2c0a39e7b) |
| Reliable sync and recovery for lost notes (https://www.reddit.com/r/notabilityapp/comments/1o357au/whats_the_upsides_and_downsides_of_notability/) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Starter | Free, 5 notes |
| Lite | $11.99/yr |
| Plus | $15.99/yr |
| Pro | $79.99/yr |
| Business | $60/user/yr; Business Pro $180/user/yr |
| Platforms | iOS, macOS, web (beta); handwriting recognition iOS/Android only |

### Contradictions
- The 2019 pivot made Notability a "free app with optional subscription" (https://blog.notability.com/post/pricing-updates), but the current compare page shows a freemium Starter limit of 5 notes (https://notability.com/pricing/compare) — the "free" promise eroded. Earlier recorded prices ($14.99 Pro annual, one-time $9.99 era) no longer match the 2026 ladder ($79.99/yr Pro); treat all cached pricing as stale.

Sources: https://notability.com/pricing ; https://notability.com/pricing/compare ; https://apps.apple.com/us/app/notability-smarter-ai-notes/id360593530 ; https://beingpaperless.com/notability-2/ ; https://beingpaperless.com/notability-15-review-is-it-worth-it/ ; blog.notability.com posts above

---
## Noteshelf
### Visual surface
- iPad/iPhone: shelf-style library with notebook covers, groups/cATEGORIES; editor with bottom tool tray, zoom box for writing, customizable covers and vivid templates (Noteshelf 3 redesign per its Medium launch post, https://medium.com/noteshelf/introducing-all-new-noteshelf-3-3a89f78fd240). Paperless X praises the zoom tool with auto-advance and reachable tool tray (https://beingpaperless.com/noteshelf-3-for-the-ipad-complete-review/).
- Windows: "humble venture into windows" copy, built for stylus devices, preloaded on Samsung Galaxy Book2/Book3 series, tuned for Surface Pro; typing, audio recording, PDF markup, zoom box, Pixabay image access (https://www.noteshelf.net/noteshelf-windows.html).
- Android: Google Play listing highlights Noteshelf AI (study notes, page summarization, translate, explain), lined/dotted/grid papers with customizable line spacing, cover packs (https://play.google.com/store/apps/details?id=com.fluidtouch.noteshelf2&hl=en).
- macOS: template library and iCloud sync across Apple devices (https://www.noteshelf.net/).
- SHOT-LIST:
  - Noteshelf 3 iPad editor with zoom box — https://apps.apple.com/us/app/noteshelf-3-ai-digital-notes/id6458735203 (App Store screenshots)
  - Windows app on Surface Pro — https://www.noteshelf.net/noteshelf-windows.html
  - Android screens with AI panel — https://play.google.com/store/apps/details?id=com.fluidtouch.noteshelf2&hl=en
  - Noteshelf 3 launch visuals — https://medium.com/noteshelf/introducing-all-new-noteshelf-3-3a89f78fd240

### Docs analysis
- Support portal (Fluid Touch): covers Windows, Android, Mac; "Sync notes across Android and Windows devices with Google Drive"; "Introduction to Noteshelf AI on Windows"; OCR handwriting-to-text how-to; cross-platform sync FAQ; groups; printing (https://noteshelf-support.fluidtouch.biz/hc/en-us/categories/360003570274-Noteshelf-on-Windows, https://noteshelf-support.fluidtouch.biz/hc/en-us/sections/12409008745113-FAQ-s)
- Handwriting→text via lasso tool (https://noteshelf-support.fluidtouch.biz/hc/en-us/articles/14273189697817-How-to-use-Handwriting-to-Text-OCR-Feature)
- Android model: "free to use with limited functionality, along with a small one-time fee to go fully premium" (https://www.noteshelf.net/noteshelf3-android.html)
- Apple pricing: Noteshelf 3 is $7.99 universal one-time purchase across iPad/iPhone/Mac (https://beingpaperless.com/noteshelf-3-for-the-ipad-complete-review/); Noteshelf 3 is a separate app from Noteshelf 2 — repurchase required (https://paperlike.com/blogs/paperlikers-insights/noteshelf-review)
- Sync silos: Google Drive for Android↔Windows, iCloud for Apple devices; no cross-ecosystem sync (https://paperlike.com/blogs/paperlikers-insights/noteshelf-review)
- Audio recording exists on all platforms but has NO synced playback to notes (https://paperlike.com/blogs/paperlikers-insights/noteshelf-review); playback speed 0.7x/1.5x/2x in v2 (https://beingpaperless.com/noteshelf/)
- Design decisions worth borrowing: zoom box with auto-advance as a first-class writing aid; device-ecosystem sync silos vs one account; a Watch companion for recordings (v2); pre-load partnerships (Samsung) as distribution.

### Features
| Area | Detail |
|---|---|
| Handwriting | Smooth ink, palm rejection, zoom box, OCR convert/search |
| PDF | Annotation, form fill, signing |
| Audio | Recording on all platforms, no synced playback |
| AI | Study notes, page summarization, translate, explain (Android/Windows incl.) |
| Templates | Large template packs, covers, planners (Day & Night Journal) |
| Media | Image crop/erase/resize, Pixabay stock images |
| Sync | Google Drive (Android/Windows), iCloud (Apple), Dropbox backup |

### Sentiment
| What people say |
|---|
| Best-in-class writing feel with S Pen on Galaxy Tab: responsiveness and palm rejection (https://www.reddit.com/r/DigitalNotebooks/comments/1iur5vd/noteshelf_3_opinion/) |
| Sync errors and lost information on Mac/iPad in Noteshelf 3 (https://www.reddit.com/r/ipad/comments/15x7boj/noteshelf_vs_noteshelf_3/) |
| Backlash risk over premium "for life" users seeing subscription prompts; "premium was meant to be for life" (https://www.reddit.com/r/Noteshelf/comments/1ezyzg3/anyone_else_get_this/) |
| Noteshelf 3 removed simple conveniences from v2 (multi-page view, page-corner handles) while adding AI (https://apps.apple.com/us/app/noteshelf-3-ai-digital-notes/id6458735203) |
| Migration from v2 to v3 smooth for some, messy for others (https://apps.apple.com/us/app/noteshelf-3-ai-digital-notes/id6458735203) |

### Wants
| What people want changed |
|---|
| Synced audio playback tied to notes (top missing feature) (https://paperlike.com/blogs/paperlikers-insights/noteshelf-review) |
| Restored v2 page-navigation conveniences (https://apps.apple.com/us/app/noteshelf-3-ai-digital-notes/id6458735203) |
| Cross-ecosystem sync without paying twice (https://www.reddit.com/r/GalaxyTab/comments/1ewrnzj/did_anyone_try_noteshelf_3_yet/) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Apple | $7.99 one-time, universal (iPad/iPhone/Mac) |
| Android | Freemium, small one-time premium fee |
| Windows | One-time purchase; preloaded on Galaxy Books |
| Platforms | iPadOS, iOS, macOS, Android, Windows |

### Contradictions
- "Premium for life" marketing vs subscription prompts observed by a premium user (https://www.reddit.com/r/Noteshelf/comments/1ezyzg3/anyone_else_get_this/). Earlier claim (2022 Paperlike) that Windows "can't sync or even import notes from iOS" (https://paperlike.com/blogs/paperlikers-insights/noteshelf-review) — now partially superseded: Google Drive sync Android↔Windows exists, but Apple↔Windows sync still does not.

Sources: https://www.noteshelf.net/noteshelf-windows.html ; https://noteshelf-support.fluidtouch.biz/hc/en-us/categories/360003570274-Noteshelf-on-Windows ; https://paperlike.com/blogs/paperlikers-insights/noteshelf-review ; https://beingpaperless.com/noteshelf-3-for-the-ipad-complete-review/ ; reddit threads above

---
## CollaNote
### Visual surface
- iPad/iPhone: colorful, student-centric UI; folder shelf, note editor with 50+ pens/brushes, sticker drawer, paper/template picker; built-in flashcards and AI study tools on the same canvas. Official site presents an "interactive wall of actual study materials" shared by users (https://collanote.com/). App Store shows lock-screen integration for recording/timer/Pomodoro, iPhone Duo optimization with a Mini Map for canvas navigation and a physics-based Book Reading Mode with side-by-side pages (https://apps.apple.com/us/app/collanote-notes-pdf-markup/id1540956268).
- Mac (Apple Silicon): same app via Apple silicon Macs (https://beingpaperless.com/collanote-new-kid-on-the-block/).
- SHOT-LIST:
  - CollaNote iPad editor with pen/sticker drawer — https://apps.apple.com/us/app/collanote-notes-pdf-markup/id1540956268 (App Store screenshots)
  - Official site feature wall — https://collanote.com/ and https://www.collanote.com/features/
  - Book Reading Mode two-page view — https://apps.apple.com/us/app/collanote-notes-pdf-markup/id1540956268
  - Whiteboard/collaboration session — https://www.producthunt.com/products/collanote

### Docs analysis
- Entirely free; "no in-app purchases as of now" per early coverage (https://medium.com/macoclock/collanote-a-truly-free-note-taking-app-39752b47dbe5) — CHANGED by 3.0: some previously free items (premium pens, ASMR sounds) moved to premium (https://www.reddit.com/r/collanote/comments/1fo7hcf/review_of_collanote_30_after_more_than_1_month_of/) (UNVERIFIED exact price of premium)
- Feature set per official site: 180+ papers & templates, 50+ pens & brushes, stickers/stamps drawer, flashcards, AI study tools, PDF markup, digital planners (https://collanote.com/)
- Collaboration is peer-to-peer with no server storage for private rooms; offline edits require manual merge; only public rooms are stored server-side, a cost decision by the solo dev (https://www.reddit.com/r/collanote/comments/npigt6/bugs/)
- Unique features: audio recording, whiteboard, memos, planner in one app; pencil tool mimicking physical pencil; smart shape/diagram recognition; exam Calculator Emulator mode (https://collanote-notes-pdf-markup-ios.soft112.com/); timer/Pomodoro/stopwatch on Lock Screen (https://apps.apple.com/us/app/collanote-notes-pdf-markup/id1540956268)
- Known gap: no auto-backup; cannot import PDFs into existing notes (2022 review; UNVERIFIED if still true in 2026) (https://medium.com/jmspaceblog/collanote-free-note-taking-app-2152b32ce65c, https://beingpaperless.com/collanote-for-ipad-2024-full-review-pt-3-should-you-be-using-it/)
- Design decisions worth borrowing: exam-emulator mode (device becomes allowed calculator); lock-screen capture controls; public/private collaboration rooms as a cost lever; physics-based page-turn reading mode; mini-map navigation for large canvases.

### Features
| Area | Detail |
|---|---|
| Handwriting | 50+ pens/brushes, low-latency ink, pencil simulation, shape recognition |
| Collaboration | Real-time collaborative notes/whiteboard, P2P for private rooms |
| PDF | Markup and annotation |
| Templates | 180+ papers/templates, stickers, planners |
| Study | Flashcards, AI study tools, quiz-style tools |
| Utilities | Audio recording, Pomodoro/timer/stopwatch, Lock Screen controls, calculator emulator |

### Sentiment
| What people say |
|---|
| Loved for being genuinely free with a full feature set; App Store editorial awards (App of the Day, Big App From Small Team) (https://medium.com/macoclock/collanote-a-truly-free-note-taking-app-39752b47dbe5) |
| Frequent freezing/crashing mid-work; audio sync frustrations (https://updf.com/annotate-pdf/collanote/) |
| 3.0 moved formerly free features (premium pens, ASMR sounds) behind payment — trust hit (https://www.reddit.com/r/collanote/comments/1fo7hcf/review_of_collanote_30_after_more_than_1_month_of/) |
| Collaborative notes have trouble joining/syncing for some users (https://apps.apple.com/us/app/collanote-notes-pdf-markup/id1540956268?see-all=reviews&platform=iphone) |
| "Busy app, too much going on"; no auto-backup makes it risky for serious notes (https://beingpaperless.com/collanote-for-ipad-2024-full-review-pt-3-should-you-be-using-it/) |
| Undo button placement on the side criticized (https://www.reddit.com/r/collanote/comments/1fo7hcf/review_of_collanote_30_after_more_than_1_month_of/) |
| Folder drag-to-reorder not supported; folders lose custom color order (https://apps.apple.com/gb/app/1540956268?see-all=reviews&platform=iphone) |

### Wants
| What people want changed |
|---|
| Auto-backup and reliable sync (https://beingpaperless.com/collanote-for-ipad-2024-full-review-pt-3-should-you-be-using-it/) |
| Server-backed private collaboration so offline edits merge automatically (https://www.reddit.com/r/collanote/comments/npigt6/bugs/) |
| Stability fixes; fewer bugs despite rapid updates (https://beingpaperless.com/whats-new-in-collanote-3-months-later/) |
| Folder reordering and organizational freedom (https://apps.apple.com/gb/app/1540956268?see-all=reviews&platform=iphone) |
| Infinite whiteboard mode request (https://www.reddit.com/r/collanote/comments/v5eyow/whiteboard_mode/) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Price | Free; some premium items added in 3.0 (UNVERIFIED pricing) |
| Platforms | iPadOS, iOS, Apple-silicon Macs |
| Business model | Solo developer; P2P collab to avoid server costs |

### Contradictions
- "Completely free, no in-app purchases" (https://medium.com/macoclock/collanote-a-truly-free-note-taking-app-39752b47dbe5) vs premium items in 3.0 (https://www.reddit.com/r/collanote/comments/1fo7hcf/review_of_collanote_30_after_more_than_1_month_of/). Also: praised as "most updated app on the App Store" while being the buggiest of the big iPad notes apps (https://beingpaperless.com/whats-new-in-collanote-3-months-later/).

Sources: https://collanote.com/ ; https://apps.apple.com/us/app/collanote-notes-pdf-markup/id1540956268 ; https://beingpaperless.com/collanote-for-ipad-2024-full-review-pt-3-should-you-be-using-it/ ; reddit threads above

---
## MarginNote 4
### Visual surface
- iPad/iPhone: a three-pane deep-reading workspace — document on the left, margin/study notebook on the right, and a mind-map canvas that grows from your highlights; switching to Study/Review mode swaps in flashcard decks and the card-box board. Marketing imagery is built around the document-mindmap split ("Cards as the Axis": one highlight is simultaneously a PDF highlight, a mind-map node, and a flashcard) (https://apps.apple.com/us/app/marginnote-4-ai-notes-mindmap/id1531657269).
- Mac: same core; users report slowness/glitches on M1 MacBook Air with 16GB and huge study sets, while iPad Pro 11" runs fine (https://apps.apple.com/us/app/marginnote-4-ai-notes-mindmap/id1531657269 — review quote).
- New brand site ("Where deep reading leaves a trace") foregrounds four wired modules: PDF/EPUB/web/video reader, highlight→card pipeline, mind map, review (https://www.marginnote.com/en/index.html).
- SHOT-LIST:
  - iPad document+mindmap split view — https://apps.apple.com/us/app/marginnote-4-ai-notes-mindmap/id1531657269 (App Store screenshots)
  - Review mode with flashcards and card box — https://manual.marginnote.com.cn/mn4/en/
  - Video note-taking screen — https://www.marginnote.com/features (Chinese feature page with visuals)
  - Site hero/visual wall — https://www.marginnote.com/en/index.html

### Docs analysis
- Features (official features page, Chinese; translated): chapter-level re-folding/re-assembly of books (merge multiple books, reorder chapters, fold sections); built-in web browser for lookup and clipping online video courses; dual-document synced-scroll comparison where every note links back to the source page; infinite-canvas handwriting notebook with multiple papers; multi-layer study scratchpads so one book supports repeated study passes; card-box kanban with multi-level grouping/filtering; hand-drawn mind maps with ink auto-following layout; multiple canvases and layers; text-outline view of mind maps; "document recall" (hide highlights/handwriting to self-test); mind-map recall (progressive folding of the knowledge frame); recording of note moments with back-links to page, notebook and map citations; video notes for local/YouTube/Bilibili with speed control, keyframe clipping, subtitle-synced annotation; cross-book chapter splicing into a custom "exam book"; mind-map layers (https://www.marginnote.com/features)
- Manual: four mindmap↔document linking modes; cards locatable via outline/card box/board; flashcards with front/back scheduled by the FSRS spaced-repetition algorithm (https://manual.marginnote.com.cn/mn4/en/)
- Pricing (official): Pro Lifetime $12.99 (iPhone/iPad only, no Mac, no advanced OCR, 500 one-time AI credits); Max Annual $16.99/yr (all platforms, advanced OCR + AI OCR templates/translation, AI summary/Q&A/card generation/Book Breakdown, 500 AI credits/mo, 1-month trial); Max Lifetime $51.99 (same features, AI credits only first 3 years); DMG Mac channel via Paddle: Standard $35, Premium +$10 upgrade, license paths not interchangeable with App Store; AI add-on packs 500cr/$1.39, 3000cr/$7.49, 20000cr/$44.99; no BYOK for AI; OCR in MarginNote is Max-gated per third-party comparison (https://www.marginnote.com/en/pricing/, https://paperlike.com/blogs/paperlikers-insights/liquidtext-vs-marginnote)
- Upgrade matrix is unusually complex: MN3 iOS→Pro only, Pro→Max second step; MN3 Mac App Store→Max direct; MN3 DMG lifetime code free-activates MN4 Standard (https://www.marginnote.com/en/pricing/)
- Design decisions worth borrowing: "one excerpt, three surfaces" (highlight = map node = flashcard) as a core data model; progressive folding recall (hide layers/cards for self-testing); multi-layer handwriting over the same book for repeat passes; chapter-level book reassembly; FSRS scheduling.

### Features
| Area | Detail |
|---|---|
| Reading | PDF, EPUB, web pages, video (local/YouTube/Bilibili), subtitle-synced video notes |
| Study | Excerpt→card pipeline, FSRS flashcards, card-box kanban, StudySets |
| Mind map | Infinite canvas, hand-drawn, layers, multiple canvases, text outline view |
| OCR/AI | Advanced OCR gated to Max; AI summary/Q&A/card gen/Book Breakdown; Agent AI organizes docs into structured mind maps (https://apps.apple.com/za/app/marginnote-4/id1531657269) |
| Recall | Document recall (blank-out), mind-map progressive folding |
| Sync | iPad↔Mac notes sync via (UNVERIFIED mechanism — iCloud) |

### Sentiment
| What people say |
|---|
| Devotees call it the most important app in their toolbox; textbook-centered workflows (https://apps.apple.com/us/app/marginnote-4-ai-notes-mindmap/id1531657269) |
| Chronic crashes and slowness on Mac and with large study sets; a reviewer's app closed while writing the review itself (https://apps.apple.com/us/app/1531657269?l=zh-Hans-CN&see-all=reviews&platform=mac) |
| "Years of delays and promises" before MN4 shipped; pricing called "a mess" (https://www.outlinersoftware.com/topics/viewt/10732) |
| Setapp MN3 users can't upgrade or transfer the database to MN4 (https://setapp.com/apps/marginnote/customer-reviews) |
| Years-long unfixed major issues drive one-star reviews despite loving the concept (https://apps.apple.com/us/app/marginnote-4-ai-notes-mindmap/id1531657269?see-all=reviews&platform=ipad) |
| Appreciation that the core is NOT subscription (https://apps.apple.com/us/app/1531657269?l=zh-Hans-CN&see-all=reviews&platform=mac) |

### Wants
| What people want changed |
|---|
| Performance/stability on Mac and large libraries (https://apps.apple.com/us/app/marginnote-4-ai-notes-mindmap/id1531657269) |
| Simpler, unified licensing across channels (https://www.outlinersoftware.com/topics/viewt/10732) |
| Database migration path between store versions (https://setapp.com/apps/marginnote/customer-reviews) |
| BYOK for AI (explicitly declined by dev) (https://www.marginnote.com/en/pricing/) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Pro Lifetime | $12.99, iPhone/iPad only |
| Max Annual | $16.99/yr, all Apple platforms |
| Max Lifetime | $51.99, AI credits 3 years |
| DMG Mac | $35 Standard, +$10 Premium |
| AI packs | $1.39/$7.49/$44.99 |
| Platforms | iOS, iPadOS, macOS (DMG channel for Mac direct) |

### Contradictions
- The site itself reframes what users believed: a "lifetime" Max purchase actually stops including AI credits after 3 years (https://www.marginnote.com/en/pricing/), and OCR is commonly believed free but is Max-gated (https://paperlike.com/blogs/paperlikers-insights/liquidtext-vs-marginnote). Earlier picture of "MarginNote 3 one-time purchase for everything" no longer holds in MN4's tiered model.

Sources: https://www.marginnote.com/en/pricing/ ; https://www.marginnote.com/features ; https://manual.marginnote.com.cn/mn4/en/ ; https://apps.apple.com/us/app/marginnote-4-ai-notes-mindmap/id1531657269 ; https://paperlike.com/blogs/paperlikers-insights/liquidtext-vs-marginnote

---
## Flexcil
### Visual surface
- iPad/iPhone: a PDF-first two-column study workspace — document on one side, "study note" beside it; gestures (pen-drag = highlight, box gesture = capture) do most of the work; top bar switches Reading/Pen gesture modes with undo/redo, search, share, and a sidebar holding bookmarks, an annotation list, and cross-document reference links (https://www.productived.net/reviews/flexcil). Users single out the floating toolbar and formatting gestures (https://apps.apple.com/us/app/flexcil-note-good-pdf-reader/id1531466462?see-all=reviews).
- Android: same gesture UX per Play listing; drag-and-paste of text into PDFs or notebooks (https://play.google.com/store/apps/details?id=com.flexcil.flexcilnote&hl=en_US).
- SHOT-LIST:
  - iPad PDF+study-note split with gesture highlight — https://apps.apple.com/us/app/flexcil-note-good-pdf-reader/id1531466462 (App Store screenshots)
  - Sidebar with annotation list/references — https://www.productived.net/reviews/flexcil
  - Box-gesture document capture — https://www.flexcil.com/support/category/flexcil-user-guide/
  - Play Store screens — https://play.google.com/store/apps/details?id=com.flexcil.flexcilnote&hl=en_US

### Docs analysis
- Core (free): gesture highlight/underline, summarize into study notes, instant PDF open, zoom, folder/file/category management, 2-page spread view, cloud support (Dropbox/Drive/OneDrive/iCloud/Box), backup (https://flexcil-ipad.appstor.io/)
- Flexcil Standard one-time add-on unlocks: PDF page editing, text boxes/images, annotation/reference navigation, unlimited folders/categories/pages, straight-line + lasso, extended gesture menu, bookmarks, more pens, colorful covers/templates, watermark removal (https://flexcil-ipad.appstor.io/)
- Business model: one-time payment for permanent use, 15-day free trial, no auto-charge (https://support.flexcil.com/hc/en-us/articles/10751768914713-Is-the-app-subscription-or-one-time-payment)
- Free vs paid split per official story post: free tier keeps one note cover/blank template, 10 pen colors and 4 pen slots (https://www.flexcil.com/stories/free-vs-standard-flexcil-2/)
- Purchases do not carry across app stores (Google vs Apple) (https://www.reddit.com/r/Flexcil/comments/1fdso3m/question_about_premium_version/)
- User guide categories: PDF annotation, textbox/image editing, outline editing, eraser, box-gesture capture (https://www.flexcil.com/support/category/flexcil-user-guide/)
- Design decisions worth borrowing: gestures as primary annotation input (2-step highlight), annotation-list sidebar with jump-to-source, "capture by box gesture" from any document into a note, planner IAP packs as a revenue line.

### Features
| Area | Detail |
|---|---|
| Gesture UX | Pen-gesture highlight/underline, box capture, drag-paste, mode toggle |
| PDF | Reader, annotate, page edit, outline editing, spread view |
| Notes | Study notes beside PDF, folders/categories, bookmarks |
| Navigation | Annotation list, references/jump links across documents |
| Sync/backup | iCloud, Dropbox, Google Drive, OneDrive, Box |
| Missing (vs peers) | No handwriting→text conversion (complaint thread) |

### Sentiment
| What people say |
|---|
| Praised as more streamlined than GoodNotes for annotation; floating toolbar loved (https://apps.apple.com/us/app/flexcil-note-good-pdf-reader/id1531466462?see-all=reviews) |
| Apple editorial recognition: Editor's Choice, App of the Day, demo app in Apple stores; ~2.4M users claimed (https://edtechimpact.com/products/flexcil/) |
| "Stopped upgrading" feeling; missing basic features like handwriting-to-text (https://www.reddit.com/r/Flexcil/comments/1qbjo1m/is_premium_worth_it_for_long_term_use_when_can_i/) |
| Trust wobble: "Purchased Premium lifetime for offline use, and now I need to be online" (https://www.reddit.com/r/Flexcil/comments/16fqdxc/loving_the_premium_version_so_far/) |
| Long-term support worry: when will updates/sync stop for lifetime buyers (https://www.reddit.com/r/Flexcil/comments/1qbjo1m/is_premium_worth_it_for_long_term_use_when_can_i/) |

### Wants
| What people want changed |
|---|
| Handwriting-to-text conversion (https://www.reddit.com/r/Flexcil/comments/1qbjo1m/is_premium_worth_it_for_long_term_use_when_can_i/) |
| Faster, resumed update cadence (https://www.reddit.com/r/Flexcil/comments/1qbjo1m/is_premium_worth_it_for_long_term_use_when_can_i/) |
| Offline license validation instead of online checks (https://www.reddit.com/r/Flexcil/comments/16fqdxc/loving_the_premium_version_so_far/) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | Core gesture reading/annotating, basic note tools |
| Flexcil Standard | ~$9.99 one-time IAP (App Store in-app list; prices vary by region/planner bundles $11.99–$14.99) |
| Premium | ~$8.99 one-time IAP (App Store in-app list) |
| Platforms | iOS/iPadOS, Android; no desktop app found |

### Contradictions
- The task list's "Flexcil 4" matches no product: the App Store title's "4+" is an age rating, not a version (https://apps.apple.com/us/app/flexcil-note-good-pdf-reader/id1531466462). Also, official help says one-time payment/no auto-charge (https://support.flexcil.com/hc/en-us/articles/10751768914713-Is-the-app-subscription-or-one-time-payment) while a user reports needing to be online to validate a lifetime purchase (https://www.reddit.com/r/Flexcil/comments/16fqdxc/loving_the_premium_version_so_far/).

Sources: https://flexcil-ipad.appstor.io/ ; https://apps.apple.com/us/app/flexcil-note-good-pdf-reader/id1531466462 ; https://support.flexcil.com/hc/en-us/articles/10751768914713-Is-the-app-subscription-or-one-time-payment ; https://www.productived.net/reviews/flexcil ; reddit threads above

---
## LiquidText
### Visual surface
- iPad (flagship): a two-zone workspace — a document pane on the left and an infinite workspace on the right where excerpts and ink live; pinch-to-gather compresses surrounding pages around a highlight so distant text can be read together; ink lines drawn between excerpts/notes/documents act as visual hyperlinks that call out on touch. The document pane holds several PDFs/Word/PowerPoint/web pages at once (https://www.liquidtext.net/liquidtextadeeperdive).
- Mac/Windows: same workspace model in a window; Android not available as of mid-2026 (https://beingpaperless.com/liquidtext/).
- SHOT-LIST:
  - iPad workspace with excerpts, mind-map connections — https://www.liquidtext.net/liquidtextadeeperdive
  - Pinch-to-gather variable context view — https://www.liquidtext.net/liquidtextadeeperdive
  - Pricing/feature table visuals — https://www.liquidtext.net/pricing-features
  - Legal use case (trial notebook) — https://law.liquidtext.net/
  - Live collaboration shared workspace — https://www.lawnext.com/2025/04/liquidtext-innovative-annotation-tool-for-complex-documents-adds-real-time-collaboration.html

### Docs analysis
- Core model: every project = document pane + multiple infinite workspaces; excerpts are live (they stay connected to source, so re-reading a source updates the excerpt) (https://www.liquidtext.net/liquidtextadeeperdive)
- Feature summary (official): unified workspace; write anywhere; excerpt anything; connect notes↔notes, notes↔docs, excerpts↔excerpts, doc↔doc; connection maps; pinch search and pinch highlight with variable context; view/link distant parts of documents simultaneously; standard-format export; real-time collaboration with shared workspace and documents (https://www.liquidtext.net/liquidtextadeeperdive)
- Real-time collaboration added April 2025: collaborators comment by typing or writing on a shared workspace (https://www.lawnext.com/2025/04/liquidtext-innovative-annotation-tool-for-complex-documents-adds-real-time-collaboration.html)
- Formats: PDF, Word, PowerPoint, web pages; Dropbox/iCloud/Box/SharePoint; exports projects to popular formats (https://www.liquidtext.net/liquidtextadeeperdive)
- Pricing is famously convoluted: free tier with 3 workspaces; Pro one-time purchase from $19.99 to $49.99 depending on tier, PLUS live subscription options: LIVE $8.99/mo billed yearly, LIVE Unlimited $15.99/mo, and Pro 2023 one-time $89.99 (MentalClone 2026 figures; official page itself is JS-heavy) (https://mentalclone.com/blog/liquidtext-pricing, https://beingpaperless.com/liquidtext/)
- Positioning now leans enterprise/legal: trial notebooks, data-room review, redline comparison (https://law.liquidtext.net/)
- "Second brain" pitch: notes stay connected to sources so current work compounds (https://www.liquidtext.net/2ndbrain)
- Design decisions worth borrowing: excerpts-as-live-objects (bi-directional link to source); pinch-to-gather variable context; connections as a first-class visible graph; document-pane + workspace split; enterprise/legal as a high-ARPU vertical.

### Features
| Area | Detail |
|---|---|
| Workspace | Infinite canvases per project, document pane, layout freedom |
| Excerpts | Pull anything from PDFs/Word/PPT/web into live excerpts |
| Connections | Ink lines = visual hyperlinks across docs and notes |
| Context | Pinch-to-gather/search with variable context; simultaneous distant-page viewing |
| Collaboration | Real-time shared workspaces (2025+) |
| Formats | PDF, Word, PPT, web; cloud storage integrations; export |

### Sentiment
| What people say |
|---|
| Reviewers call it the best deep-reading tool available: "no better app… possibly no better workflow" (https://www.liquidtext.net/liquidtextadeeperdive) |
| Users complain workspace items drift/scroll away from where they were placed instead of staying put (https://apps.apple.com/gb/app/liquidtext/id922765270?see-all=reviews) |
| Cost criticized as steep for occasional users; value skewed to heavy legal/research users (https://softwarefinder.com/legal/liquidtext) |
| Desktop experience lags the iPad original (https://beingpaperless.com/liquidtext/) |
| Learning curve acknowledged; real-time collaboration initially clunky (https://www.techzone101.com/2023/08/liquidtext-reviews.html) (UNVERIFIED single source) |

### Wants
| What people want changed |
|---|
| Anchored placement of workspace items (stop auto-scrolling drift) (https://apps.apple.com/gb/app/liquidtext/id922765270?see-all=reviews) |
| Android version (https://beingpaperless.com/liquidtext/) |
| Simpler pricing (https://softwarefinder.com/legal/liquidtext) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | Limited workspaces (3) |
| Pro | One-time, $19.99–$89.99 depending on tier/version |
| LIVE | $8.99/mo (billed yearly) |
| LIVE Unlimited | $15.99/mo |
| Enterprise | Custom |
| Platforms | iPadOS, macOS, Windows |

### Contradictions
- LiquidText is commonly grouped as a "student note-taking app" (as in our earlier rounds), but the company now markets primarily to lawyers and enterprises (https://law.liquidtext.net/), and pricing reporting is inconsistent across trackers (Capterra "$3.99/user/mo", MentalClone "$89.99 one-time + $8.99/mo", Paperless X "$19.99–$49.99") (https://www.capterra.com/p/264823/Liquid-Text/pricing/, https://mentalclone.com/blog/liquidtext-pricing, https://beingpaperless.com/liquidtext/) — flag: no single canonical price sheet is publicly stable.

Sources: https://www.liquidtext.net/liquidtextadeeperdive ; https://law.liquidtext.net/ ; https://www.lawnext.com/2025/04/liquidtext-innovative-annotation-tool-for-complex-documents-adds-real-time-collaboration.html ; https://mentalclone.com/blog/liquidtext-pricing ; https://beingpaperless.com/liquidtext/ ; https://apps.apple.com/gb/app/liquidtext/id922765270?see-all=reviews

---
## Xodo
### Visual surface
- Web: a tool-grid homepage ("40+ online tools") — every function (convert, merge, split, OCR, sign, AI summarize) is a card opening a single-purpose viewer with a left tool rail; Xodo Drive sidebar for storage (https://xodo.com/pricing, https://xodo.com/blog/xodo-plans-explained).
- Mobile (iOS/Android): PDF viewer/annotator with Smart Pen and Smart Highlighter tools, built-in scanner, form filling, translation on Android; stylus support incl. Apple Pencil and S Pen (https://xodo.com/blog/xodo-plans-explained).
- Desktop: Xodo PDF Studio (full editor) and free Xodo PDF Reader on Windows/macOS/Linux (https://xodo.com/blog/xodo-plans-explained).
- SHOT-LIST:
  - Xodo Web tool grid — https://xodo.com/pricing
  - Pricing page plan cards — https://xodo.com/pricing
  - PDF Studio desktop editor — https://xodo.com/blog/xodo-plans-explained
  - Mobile annotator with Smart Pen — App Store/Play listing of "Xodo PDF"

### Docs analysis
- Product family per official 2026 guide: Xodo Web ($7.99/mo yearly, $10.99 monthly; free = 1 action/day, 1GB Xodo Drive), PDF Studio ($9.99/mo yearly, $19.99 monthly, $240 perpetual with 12 months upgrades, 2 devices), free PDF Reader (view/annotate/fill/sign only), Xodo Mobile (iOS $39.99/yr, Android $109.99/yr, $11.99/mo; watermarks on free), Document Suite ($14.99/mo yearly, $24.99 monthly; Web+Studio+Mobile), Teams custom, Xodo Sign separate ($10/$16/mo, free 3 docs/mo, API from $50/mo) (https://xodo.com/blog/xodo-plans-explained)
- Privacy design claim: most tools process files locally in-browser; files needing upload are permanently deleted after 1h (https://xodo.com/pricing)
- Web free limit: 1 action/download per day; some features (PDF/A conversion, split/merge refinement) are premium-only (https://xodo.com/blog/xodo-plans-explained)
- Built on Apryse technology (Apryse acquired Xodo); enterprise SDK underlies consumer apps (https://xodo.com/pricing)
- Design decisions worth borrowing: per-product pricing by platform instead of one sync-service fee; local-first processing as a privacy selling point; "1 free action/day" as a razor-thin free tier; separate e-sign product with audit trails.

### Features
| Area | Detail |
|---|---|
| PDF tools | 40+ web tools, 60+ desktop tools: convert (Word/Excel/PPT/PDF-A/HEIC), merge, split, OCR, compress, redact, compare, preflight |
| Annotation | Mobile annotator, Smart Pen, Smart Highlighter, forms, signing |
| AI | AskPDF, PDF Summarizer |
| Storage | Xodo Drive 1GB free |
| Signature | Xodo Sign: templates, audit trails, API |
| Platforms | Web, Windows, macOS, Linux, iOS, Android |

### Sentiment
| What people say |
|---|
| G2/G2-style reviewers: "everything just works smoothly"; free version genuinely usable (https://www.g2.com/products/xodo/reviews) |
| Complaint: subscription credits expire monthly — "you end up paying too much for stuff you never get to use" (https://aidetectplus.com/blog/xodo-review) |
| Small nonprofits priced out over time ("the price point… was not working any longer") (https://www.capterra.com/p/210439/Xodo/pricing/) |
| Widely used by digital-planner crowd: clickable planner links load quickly (https://www.capterra.com/p/210439/Xodo/pricing/) |
| Confusion across many similarly-named Xodo products and pricing variants (https://xodo.com/blog/xodo-plans-explained) |

### Wants
| What people want changed |
|---|
| Non-expiring credits or simpler one-price-all-tools model (https://aidetectplus.com/blog/xodo-review) |
| More generous free tier than 1 action/day (https://xodo.com/blog/xodo-plans-explained) |
| Fewer separate products/simpler lineup (https://xodo.com/blog/xodo-plans-explained) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Web | $7.99/mo (yearly) / $10.99 (monthly) |
| PDF Studio | $9.99/mo (yearly) / $19.99 (monthly) / $240 perpetual |
| Mobile | iOS $39.99/yr, Android $109.99/yr, $11.99/mo |
| Document Suite | $14.99/mo (yearly) / $24.99 (monthly) |
| Sign | $10–$16/mo, API from $50/mo |
| Platforms | Web, Windows, macOS, Linux, iOS, Android |

### Contradictions
- Reviewer claim of $9/month Pro (https://app.softwarehope.com/software/xodo) vs official $7.99/$9.99/$14.99 product-split pricing (https://xodo.com/blog/xodo-plans-explained); the widely repeated idea that "Xodo is one app" is now false — it is a product family (Web/Studio/Reader/Mobile/Sign) with separate subscriptions.

Sources: https://xodo.com/blog/xodo-plans-explained ; https://xodo.com/pricing ; https://www.g2.com/products/xodo/reviews ; https://aidetectplus.com/blog/xodo-review ; https://www.capterra.com/p/210439/Xodo/pricing/

---
## PDF Expert (Readdle)
### Visual surface
- iPad/iPhone: a document-centric PDF app — file manager grid (works with Readdle Documents and Files), then an editor with a top toolbar (pen, highlighter, note, text, image, link, signature) and a sidebar for bookmarks/outline/thumbnails; tabbed multi-document editing. App Store screenshots show a clean, near-Acrobat look (https://apps.apple.com/us/app/pdf-expert-pdf-editor-reader/id323023808).
- Mac: same editor in a window; this is the only tier you can still buy outright. Windows version exists as a separate product (UNVERIFIED: current availability/feature parity — pricing trackers still call it Apple-only).
- SHOT-LIST:
  - iPad editor with annotation toolbar — https://apps.apple.com/us/app/pdf-expert-pdf-editor-reader/id323023808 (App Store screenshots)
  - Pricing page plan cards — https://pdfexpert.com/pricing
  - Readdle billing/subscription help (shows plan structure) — https://support.readdle.com/pdfexpert/en_US/billing-subscription

### Docs analysis
- Model: one-time purchase exists only for PDF Expert for Mac; the iOS Premium pack and cross-platform app are subscription (https://support.readdle.com/pdfexpert/en_US/billing-subscription)
- Cross-platform yearly plan ~$79.99/yr (about $6.67/mo) (https://thebusinessdive.com/pdf-expert-review); Mac lifetime $139.99 one-time, Mac-only (https://www.fahimai.com/pdf-expert)
- Education discount: 30% off the annual plan with a verified educational email (https://pdfexpert.com/pricing)
- Sync across Apple devices via supported cloud services (not a proprietary sync engine) (https://thebusinessdive.com/pdf-expert-review)
- Aggregated rating 4.7/5 on G2 (33 reviews) (https://toolradar.com/tools/pdf-expert)
- Known weaknesses per 2026 roundups: OCR struggles on low-quality scans; not available outside Apple's ecosystem (https://www.pdnob.com/alternative/pdf-expert-alternative.html)
- Design decisions worth borrowing: lifetime price for the desktop-only tier as a compromise between one-time and subscription; education pricing as a loyalty lever; cloud-service-based sync instead of building a sync engine.

### Features
| Area | Detail |
|---|---|
| PDF editing | Text editing in place, images, links, page manipulation |
| Annotation | Pen, highlighter, notes, shapes, signatures |
| Forms | Fill-and-sign, form creation |
| OCR | Present but weak on low-quality scans (complaint-driven) |
| Sync | Via cloud services across Apple devices |
| Platform | iOS, iPadOS, macOS; Windows separate |

### Sentiment
| What people say |
|---|
| "Love the app, quite frankly excellent" — even in a price rant (https://www.reddit.com/r/ipad/comments/niw4u2/pdf_expert_50_a_year_rant/) |
| Subscription-price anger from $50/yr era, continuing as prices rise (https://www.reddit.com/r/ipad/comments/niw4u2/pdf_expert_50_a_year_rant/, https://www.pdnob.com/alternative/pdf-expert-alternative.html) |
| Longtime users drift away after needs change but still "revert on occasion" (https://www.g2.com/products/pdf-expert/pricing) |
| OCR quality complaints on scanned docs (https://www.pdnob.com/alternative/pdf-expert-alternative.html) |

### Wants
| What people want changed |
|---|
| Lifetime option covering iPhone/iPad, not just Mac (https://www.fahimai.com/pdf-expert) |
| Windows/Android availability (https://www.pdnob.com/alternative/pdf-expert-alternative.html) |
| Better OCR on low-quality scans (https://www.pdnob.com/alternative/pdf-expert-alternative.html) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Subscription | ~$79.99/yr cross-platform (iOS+Mac) |
| Mac lifetime | $139.99 one-time |
| Education | 30% off annual |
| Platforms | iOS, iPadOS, macOS (Windows separate product) |

### Contradictions
- Older picture "PDF Expert is Apple-only" (https://www.pdnob.com/alternative/pdf-expert-alternative.html) vs the existence of a Windows version (UNVERIFIED here); and "one-time purchase available" claims (https://www.mac-forums.com/threads/im-looking-at-pdf-expert-app-opinions-recommendations.376402/) are true only for Mac, not the cross-platform product (https://support.readdle.com/pdfexpert/en_US/billing-subscription).

Sources: https://support.readdle.com/pdfexpert/en_US/billing-subscription ; https://pdfexpert.com/pricing ; https://thebusinessdive.com/pdf-expert-review ; https://www.fahimai.com/pdf-expert ; https://www.pdnob.com/alternative/pdf-expert-alternative.html ; https://www.reddit.com/r/ipad/comments/niw4u2/pdf_expert_50_a_year_rant/

---
## University Notes: Study Notes (2026)
### Visual surface
- iPad/iPhone/Mac (primary): a digital-notebook app built around "active recall from your own notes": notebook pages with tabs for switching notebooks, a floating Memorisation Sheet you drag over the page to hide only what's beneath it, a Tape tool (digital sticky strips over answers, tap to reveal), and per-colour highlight hiding (yellow = emphasis, red = test yourself). PDF pages can be extended on the right side to create annotation margin space (https://apps.apple.com/au/app/university-notes-study-notes/id6777402601?platform=ipad).
- Also on Android (Play listing: FOODMENU.WORLD K.K.) (https://play.google.com/store/apps/details?id=world.foodmenu.studynotes).
- SHOT-LIST:
  - iPad note editor with Memorisation Sheet over a table — https://apps.apple.com/au/app/university-notes-study-notes/id6777402601?platform=ipad (App Store screenshots)
  - Tape tool over a past paper — same App Store screenshots
  - Android screens — https://play.google.com/store/apps/details?id=world.foodmenu.studynotes

### Docs analysis
- Four documented revision mechanics (all from the official listing): (1) colour-keyed memorisation with a cover sheet; (2) hiding highlighted sections by colour for active recall; (3) questions/answers/explanations on separate layers, hide the answer layer, rewrite on top; (4) digital tape over keywords/diagrams without changing original note colours (https://apps.apple.com/au/app/university-notes-study-notes/id6777402601?platform=ipad)
- Structure: categories, folders/subfolders, chapters per lesson/subject; tabs between notebooks; ruler, compass, geometric shapes (https://apps.apple.com/au/app/university-notes-study-notes/id6777402601?platform=ipad)
- Privacy label: "Data Not Collected" — developer does not collect any data; contains advertising and unrestricted web access (https://apps.apple.com/au/app/university-notes-study-notes/id6777402601?platform=ipad)
- Targets Year 11/12 (ATAR/HSC/VCE/QCE/WACE/SACE), TAFE and uni; 43 languages; requires iOS 15.6+ (https://apps.apple.com/au/app/university-notes-study-notes/id6777402601?platform=ipad)
- Free at listing time; pricing/subscription not visible in listing (UNVERIFIED whether monetisation is ads-only)
- Design decisions worth borrowing: study-mechanics as native tools (cover sheet, per-colour hiding, layer-hiding Q&A, tape) rather than bolted-on flashcards; right-side page extension for annotation margin; "revise from your own notes" as a positioning wedge vs Goodnotes-style storage.

### Features
| Area | Detail |
|---|---|
| Handwriting | Pencil input, improved handwriting + keyboard input (v1.6.x) |
| Recall tools | Memorisation Sheet (floating cover), colour-based hiding, Tape tool, hidden answer layers |
| PDF | Import slides/past papers, annotate, extend page margin |
| Structure | Folders/subfolders, chapters, notebook tabs, shapes/ruler/compass |
| Platform | iOS, iPadOS, macOS, visionOS, Android |

### Sentiment
| What people say |
|---|
| No ratings yet: "hasn't received enough ratings or reviews to display an overview" (https://apps.apple.com/au/app/university-notes-study-notes/id6777402601?platform=ipad) — sentiment vacuum; treat all coverage as marketing |

### Wants
| What people want changed |
|---|
| none found (no user reviews yet) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Price | Free at listing (monetisation UNVERIFIED; ad-supported per age classification) |
| Platforms | iOS/iPadOS/macOS/visionOS, Android |
| Privacy | Data not collected |

### Contradictions
- none found (too new for conflicting claims)

Sources: https://apps.apple.com/au/app/university-notes-study-notes/id6777402601?platform=ipad ; https://play.google.com/store/apps/details?id=world.foodmenu.studynotes

---
## Write by Styluslabs
### Visual surface
- Cross-platform (Windows/Mac/Linux/iOS/Android): an austere, canvas-first handwriting app that looks like a vector drawing tool with paper; a small floating tool strip (pen width/colors, insert-space tool, select, erase), margin ruler, and a document browser (Apple Files integration on iOS). The UI is deliberately spartan; Linux users call it ugly but the best handwriting engine on the platform (https://www.reddit.com/r/linuxquestions/comments/11m0bag/best_note_taking_app_with_handwriting_support/).
- SHOT-LIST:
  - Main writing canvas with tool strip — https://www.styluslabs.com/write/ (product page visuals)
  - Help/manual pages with annotated screenshots — https://www.styluslabs.com/write/Help.html
  - GitHub releases page (binary screenshots per release) — https://github.com/styluslabs/Write/releases

### Docs analysis
- Core concept: "a word processor for handwriting" — strokes are grouped into lines so paragraph-level operations work on ink (https://alternativeto.net/software/stylus-labs-write/about/)
- Unique tools per official site/FAQ: Ruled Insert Space (insert blank lines or space between words; the whole paragraph reflows), ruled erase, ruled select; bookmarks labeled with handwriting; handwritten links between documents; margin content usable as bookmark; online whiteboarding collaboration at styluslabs.com/share (https://www.styluslabs.com/, https://play.google.com/store/apps/details?id=com.styluslabs.writeqt&hl=en_IN&gl=US)
- File format: non-proprietary SVG, openable in other vector apps and browsers; documents in /sdcard/styluslabs/write/ on Android; iCloud/Files-app integration on iOS (https://apps.apple.com/us/app/stylus-labs-write/id1580794413, https://play.google.com/store/apps/details?id=com.styluslabs.write&hl=en_IN)
- Limits: text can be displayed in SVG but not edited in Write; no PDF annotation, no text/shape insertion, no LaTeX vs Xournal++ (https://styluslabs.com/faq, https://github.com/xournalpp/xournalpp/issues/2358)
- Write 3 changelog highlights: 3x smaller documents, image cropping, pen width varying by speed/direction, dashed lines, list view browser, single-touch erase/select/insert-space option (https://write-beta.soft112.com/)
- Free app with Pro IAP on iOS (UNVERIFIED price of Pro); desktop builds free (https://stylus-labs-write-pro-ios.soft112.com/)
- Design decisions worth borrowing: line-of-strokes as an editable unit (reflow for ink is the standout mechanic competitors still lack); open SVG storage; handwritten bookmarks/links as navigation; margin-as-bookmark.

### Features
| Area | Detail |
|---|---|
| Handwriting engine | Stroke-into-line grouping, ruled insert space (reflow), ruled erase/select |
| Navigation | Handwritten bookmarks, handwritten links, margin bookmarks |
| Files | SVG format, Files-app/iCloud integration, SD-card storage |
| Collaboration | Online whiteboarding (styluslabs.com/share) |
| Pen | Width by speed/direction, dashed lines, pressure sensitivity |
| Not included | PDF annotation, text editing, shape/LaTeX insertion |

### Sentiment
| What people say |
|---|
| "Best handwriting app I've found on Linux" despite ugly UI and proprietary status (https://www.reddit.com/r/linuxquestions/comments/11m0bag/best_note_taking_app_with_handwriting_support/) |
| Preferred over Xournal++/Rnote by some for pure handwriting flow (https://www.reddit.com/r/opensource/comments/1f5fnmr/finding_for_handwriting_notetaking_program/) |
| Dev is unusually responsive in threads, taking feature requests directly (https://www.reddit.com/r/stylus/comments/wkztj5/pen_settings_for_stylus_labs_write/) |
| Other projects file issues asking to copy its features: bookmarks to text, reflow, ruled erase/select (https://github.com/Joost-8/FineNotes/issues/20) |
| Slow update cadence noted ("updated for the first time in years" in 2020) (https://www.reddit.com/r/stylus/comments/gnxymz/stylus_labs_write_handwritten_text_word_processor/) |

### Wants
| What people want changed |
|---|
| Better UI/theme polish (https://www.reddit.com/r/linuxquestions/comments/11m0bag/best_note_taking_app_with_handwriting_support/) |
| Editable text in documents (https://styluslabs.com/faq) |
| PDF annotation and more note-taking features (https://github.com/xournalpp/xournalpp/issues/2358) |

### Video evidence
- Official demo video linked from the Play listing ("Watch the demo video to get started") — hosted via styluslabs.com (https://play.google.com/store/apps/details?id=com.styluslabs.write&hl=en_IN); specific YouTube URL UNVERIFIED in this pass.
- The Play listing describes what the demo shows: insert-space reflow in action, link/bookmark creation (https://play.google.com/store/apps/details?id=com.styluslabs.write&hl=en_IN).
- No significant YouTube walkthrough ecosystem or comment threads found for Write (search returned none) — community discussion lives in the Google Groups support forum (http://groups.google.com/forum/#!forum/write-support) and Reddit r/stylus.

### Pricing and platforms
| Item | Detail |
|---|---|
| Price | Free (desktop and Android); iOS has a Pro IAP (UNVERIFIED price) |
| Platforms | Windows, macOS, Linux, iOS/iPadOS, Android |
| License | Proprietary freeware; GitHub repo hosts releases/issues, not source (https://github.com/styluslabs/Write) |

### Contradictions
- The brief's "open source" label is wrong: the GitHub repo distributes releases and tracks issues but the source is not open; a Reddit thread explicitly calls Write proprietary (https://github.com/styluslabs/Write, https://www.reddit.com/r/linuxquestions/comments/11m0bag/best_note_taking_app_with_handwriting_support/).

Sources: https://www.styluslabs.com/ ; https://styluslabs.com/faq ; https://github.com/styluslabs/Write ; https://alternativeto.net/software/stylus-labs-write/about/ ; reddit threads above

---
## Zotero
### Visual surface
- Desktop (Windows/macOS/Linux): three-pane library — left sidebar (collections, tags, feeds), center item list, right item pane (metadata, abstract, notes, tags, related); double-click opens the built-in reader with a left PDF pane, right annotations sidebar, and tabs across the top for multiple open papers. Zotero 8 added an Appearance panel and reader themes, per-document view settings (https://www.zotero.org/blog/zotero-8/).
- Web: library.zotero.org mirrors the library and reader in the browser (https://www.zotero.org/storage).
- iOS: library + reader with PDF/EPUB/snapshot reading and Read Aloud added Aug 2026 (https://www.zotero.org/blog/).
- SHOT-LIST:
  - Desktop library three-pane — https://www.zotero.org/support/quick_start_guide
  - Built-in PDF reader with annotations sidebar — https://www.zotero.org/support/pdf_reader
  - Zotero 8 Appearance panel / reader themes — https://www.zotero.org/blog/zotero-8/
  - iOS reader with Read Aloud — https://www.zotero.org/blog/
  - Storage plans page — https://www.zotero.org/storage

### Docs analysis
- Reader (official): highlight/underline/notes in Reading Mode; annotations carried into notes automatically include links back to the PDF page and citations usable in Word/LibreOffice/Google Docs via plugins (https://www.zotero.org/support/pdf_reader)
- Reader supports EPUB and webpage snapshots, resizable highlights after creation, hover previews of intra-PDF link targets (https://forums.zotero.org/discussion/106716/available-for-beta-testing-updated-reader-with-epub-snapshot-support-and-new-annotation-types)
- Zotero 8 (Jan 2026): selected annotations grouped by top-level item in the item pane; Appearance panel; reader themes; per-document view settings (https://www.zotero.org/blog/zotero-8/)
- iOS Read Aloud (Aug 2026): reads PDFs, EPUBs and snapshots in natural voices, auto-skips citations/headers/footers/tables, sentence/paragraph skip, start from any spot (https://www.zotero.org/blog/)
- Storage: free 300MB; 2GB $20/yr, 6GB $60/yr, Unlimited $120/yr; Lab/Institution = unlimited for members; local library always unlimited; files in groups you own draw on your quota; group members access freely (https://www.zotero.org/support/individual_storage, https://www.zotero.org/support/storage_faq)
- Plan switching is prorated into a shifted expiration date, not an immediate charge; paid accounts non-refundable (https://www.zotero.org/support/storage_faq)
- Sync workaround documented: metadata syncs free regardless; linked-file attachments and WebDAV (own server) avoid storage fees (https://www.zotero.org/support/individual_storage)
- Plugin ecosystem is enormous: 11.3M downloads for one reader-sidebar plugin; plugins add reference sidebars, AI chat, Better BibTeX etc. (https://www.zoteroplugins.org/c/reading)
- Design decisions worth borrowing: annotation objects that carry source-links and citation hooks into writing tools; group libraries with owner-paid storage; prorated plan switching; open plugin architecture as the real product surface.

### Features
| Area | Detail |
|---|---|
| Reference management | Metadata capture via browser connector, collection/tag organization, feeds |
| Reader | Built-in PDF/EPUB/snapshot reader, annotations, Reading Mode, themes (Z8) |
| Notes | Standalone + annotation-derived notes with back-links and citations |
| Writing | Word/LibreOffice/Docs plugins for one-click citations |
| Sync | Free metadata sync; file sync via Zotero Storage or WebDAV |
| Collaboration | Group libraries (public/private), owner-pays storage |
| Platform | Windows/macOS/Linux/iOS/Web; Android UNVERIFIED (no official app) |

### Sentiment
| What people say |
|---|
| Loved as free, open-source, community-governed; rated ~4.5/5 in aggregator (https://aitoolpick.org/pricing/zotero/) |
| Storage-tier anger: $120 unlimited is the only sensible option once past 6GB; tiers called "20 years out of date" (https://forums.zotero.org/discussion/87656/is-storage-pricing-helping-zotero-project, https://forums.zotero.org/discussion/124075/zotero-storage-pricing-policies) |
| Long-requested reader/EPUB features arrived only after years of forum pressure (https://forums.zotero.org/discussion/90368/feature-request-zotero-beta-windows-ios-beta-ipad-epub-reading) |
| University licensing (e.g. Penn) quietly solves storage for members; awareness of it is low (https://guides.library.upenn.edu/citationmgmt/zotero-storage) |
| Community fills gaps: third-party AI readers like ZotReader appear because Zotero avoids native AI (https://www.reddit.com/r/zotero/comments/1kvzn16/introducing_zotreader_read_annotate_talk_with/) |

### Wants
| What people want changed |
|---|
| Mid-size storage tiers (~$50-80/yr) between 6GB and unlimited (https://forums.zotero.org/discussion/124075/zotero-storage-pricing-policies) |
| Native AI/chat with PDFs (community builds it instead) (https://www.reddit.com/r/zotero/comments/1kvzn16/introducing_zotreader_read_annotate_talk_with/) |
| More responsive plugin-dependent feature gaps (https://www.zoteroplugins.org/c/reading) |

### Video evidence
- Official screencast tutorials page on zotero.org covers quick start, Word plugin, groups (https://www.zotero.org/support/screencast_tutorials) (URL from docs tree; UNVERIFIED individual video content in this pass).
- YouTube walkthrough ecosystem is large but unindexed here; the community discussion of demo behavior appears mainly on Zotero Forums, where users narrate workflows (beta reader threads) rather than gripe about video content (https://forums.zotero.org/discussion/88688/in-built-pdf-reader-beta-pdf-annotation-coherence).
- Comment-thread behavior worth noting: Zotero devs reply directly and substantively in forum threads, and feature requests are tracked to delivery (EPUB reader shipped after being requested in the beta thread) (https://forums.zotero.org/discussion/90368/feature-request-zotero-beta-windows-ios-beta-ipad-epub-reading).

### Pricing and platforms
| Item | Detail |
|---|---|
| Software | Free, open source |
| Storage | 300MB free; 2GB $20/yr; 6GB $60/yr; Unlimited $120/yr |
| Lab/Institution | Unlimited, org pricing |
| Platforms | Windows, macOS, Linux, iOS, Web |

### Contradictions
- Aggregators misreport Zotero's pricing as monthly ("$20/month" for 2GB) (https://aitoolpick.org/pricing/zotero/) vs official yearly (https://www.zotero.org/support/individual_storage) — treat aggregator price rows as noise. Also "Zotero is citation-only" is stale: since Zotero 6-8 it is a full PDF/EPUB reader-annotator (https://www.zotero.org/blog/zotero-8/).

Sources: https://www.zotero.org/support/pdf_reader ; https://www.zotero.org/blog/zotero-8/ ; https://www.zotero.org/support/storage_faq ; https://www.zotero.org/support/individual_storage ; https://www.zoteroplugins.org/c/reading ; forums.zotero.org threads above

---
## Hypothesis (Hypothes.is)
### Visual surface
- Browser (Chrome/Chromium extension + bookmarklet): activating Hypothesis opens a right sidebar over any webpage/PDF/EPUB; selecting text raises a small toolbar (annotate, highlight, page note); annotations are threaded cards with tags, LaTeX support, markdown-ish formatting (bold/italics/links/lists); a filter bar and group switcher sit atop the sidebar (https://web.hypothes.is/help/annotation-basics/, https://libguides.trinity.edu/digital-annotation/hypothesis).
- LMS (Canvas etc.): the annotation layer appears inside course content; instructors see a dashboard of engagement (https://ascode.osu.edu/hypothesis-social-annotation-tool-your-carmen-course).
- SHOT-LIST:
  - Chrome extension sidebar with threaded annotations — https://chromewebstore.google.com/detail/hypothesis-web-pdf-annota/bjfhmglciegochdpefhhlphglcehbmek (store screenshots)
  - Annotation basics screens — https://web.hypothes.is/help/annotation-basics/
  - LMS app in Canvas module view — https://kb.wisconsin.edu/dle/page.php?id=104254
  - Pricing/packages page visuals — https://web.hypothes.is/pricing-page/

### Docs analysis
- Four annotation primitives: highlights, margin notes anchored to text, page notes, and replies (https://acrlog.org/2017/01/25/hyopthes-is-and-the-dream-of-universal-web-annotation/)
- Visibility model: public (whole stream), private "Only Me", or group-scoped; highlights toggleable per page (https://hypothes.is/docs/help)
- Standards-based: the `h` web app exposes an open Web Annotations API; the client is a browser annotator against that API; code is open source on GitHub (https://github.com/hypothesis/h)
- Individual tier: free with unlimited public/private annotations and private groups (https://makerstack.co/reviews/hypothesis-review/)
- Institutional tiers: Bronze (LMS integration, 1,000 seats), Silver (2,000 seats, advanced analytics, auto-grading), Gold (3,000 seats, unlimited training, dedicated CSM, quarterly check-ins, Hypothesis Academy); pricing itself is quote-only (https://web.hypothes.is/pricing-page/)
- Annotations support LaTeX, links, lists (https://libguides.trinity.edu/digital-annotation/hypothesis)
- Design decisions worth borrowing: annotations as an open-data layer (W3C Web Annotation model) over documents the app doesn't own; group-scoped visibility as the privacy unit; auto-grading and dashboards as the monetizable educator surface.

### Features
| Area | Detail |
|---|---|
| Annotation | Highlights, margin notes, page notes, replies, tags |
| Scope | Public/private/group; LMS course groups |
| Formats | Web pages, PDFs, EPUBs, images, videos (via LMS app) |
| Social | Threaded discussion on text, permalinked annotations |
| Educator | Auto-grading, analytics dashboard, SpeedGrader support |
| Openness | Open source, open API, interoperable annotation data |

### Sentiment
| What people say |
|---|
| Educators overwhelmingly positive: students arrive to class prepared, quieter students participate (testimonials on official pricing page) (https://web.hypothes.is/pricing-page/) |
| Chrome store rating 3.9/5 — moderate for an extension (https://chromewebstore.google.com/detail/hypothesis-web-pdf-annota/bjfhmglciegochdpefhhlphglcehbmek) |
| Limitations noted: enterprise features paywalled, learning curve, occasional sync issues on some browsers, complex sites can misbehave (https://bugsmash.io/blog/website-annotation-tool/) |
| Annotator-score 7.4/10 in 2026 independent review (https://makerstack.co/reviews/hypothesis-review/) |

### Wants
| What people want changed |
|---|
| Better PDF rendering/robustness on complex documents (https://bugsmash.io/blog/website-annotation-tool/) |
| AI features — competitors ship AI sidebar reading helpers, Hypothesis stays AI-light (https://chromewebstore.google.com/detail/annotator-web-pdf-annotat/odednchjeljhdcfkplhoikkoniijdobc) (UNVERIFIED as stated demand; inferred from market gap) |
| Public tier pricing for small institutions without LMS deals (https://web.hypothes.is/pricing-page/) (UNVERIFIED) |

### Video evidence
- Official YouTube channel exists with LMS demo videos (hypothes.is YouTube; UNVERIFIED — no direct video URL captured this pass); help docs embed demos of the extension workflow (https://web.hypothes.is/help/annotation-basics/).
- University teaching centers produce the main walkthrough footage (e.g. OSU ASC distance-ed pages with embedded guides) (https://ascode.osu.edu/hypothesis-social-annotation-tool-your-carmen-course).
- No HN thread captured this pass (UNVERIFIED); historical HN coverage of Hypothes.is is extensive but not re-verified here.

### Pricing and platforms
| Item | Detail |
|---|---|
| Individual | Free, unlimited annotations, private groups |
| Bronze/Silver/Gold | Institutional, quote-based, seat-capped (1k/2k/3k) |
| Platforms | Chrome/Chromium extension, bookmarklet, LMS app (Canvas/Blackboard/Moodle/D2L), API |

### Contradictions
- Hypothesis is commonly described in our earlier notes as a general web-annotation layer for individuals, but the company's own page now sells it almost purely as an LMS/social-reading product for institutions (https://web.hypothes.is/pricing-page/). The "free" product remains, but the strategic center has moved.

Sources: https://web.hypothes.is/pricing-page/ ; https://web.hypothes.is/help/annotation-basics/ ; https://github.com/hypothesis/h ; https://makerstack.co/reviews/hypothesis-review/ ; https://libguides.trinity.edu/digital-annotation/hypothesis

---
## Noteful
### Visual surface
- iPad/iPhone: minimalist, content-maximizing UI — a document browser with notebooks and #tag navigation, a clean editor with a slim toolbar (3 brushes: ballpoint, fountain pen, highlighter), tags typed inline, and a Layers panel that can be opened alongside tags; App Store screenshots show an annotated note with the Layers and Tags panels open (https://www.atlasworkspace.ai/blog/best-note-taking-apps-for-ipad, https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334).
- SHOT-LIST:
  - iPad note with Layers panel open — https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334 (App Store screenshots)
  - Tag browse view (#nested/tag) — https://www.getnoteful.com/
  - Official site feature wall — https://www.getnoteful.com/

### Docs analysis
- Layers (official): annotate on separate layers without changing original content; hide/show independently; rearrange; composite complex layouts — Pro-gated (https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334)
- Ink: custom-built "InfiniteStroke" engine converting strokes to high-res vector ink; 3 brushes only; shape recognition (https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334)
- Organization: #tag and #nested/tag inline tagging anywhere in notebooks; browse notebooks or pages by tags; rename/re-assign tags; "more flexible than folders" (https://www.getnoteful.com/)
- Sync: iCloud sync to iPhone+iPad, account-based key encryption; Mac via M1 (https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334)
- Audio: record while writing, playback synced to notes (https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334)
- Pricing: free app, Noteful Pro Lifetime $6.99 one-time (App Store IAP list; earlier reporting said $9.99 once — price appears to have dropped) (https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334, https://www.alphonsolabs.com/best-note-taking-apps-ipad-2026/)
- v1.5.1: experimental lasso-selection-to-text conversion; Add Page button in Overview; iOS 18 export crash fix (https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334)
- Weak spot documented by reviewers: search only covers notebook titles and tags, not note content (https://beingpaperless.com/noteful-complete-review-2022/)
- Design decisions worth borrowing: layers as a $6.99-lifetime differentiator; inline hashtag tagging instead of folders; three-brush restraint; audio synced to ink on a one-time-purchase app.

### Features
| Area | Detail |
|---|---|
| Handwriting | InfiniteStroke vector ink, 3 brushes, shape recognition, lasso, experimental selection→text |
| Layers | Separate annotation layers, hide/show/rearrange (Pro) |
| PDF | Import PDFs/Office, annotate, export as PDF |
| Organization | #tags/#nested tags, notebooks, Quick Create |
| Audio | Recording synced to notes |
| Sync | iCloud, iPhone+iPad, Mac M1+ |

### Sentiment
| What people say |
|---|
| Enthusiasts call it "10 times better than Goodnotes" precisely because of layering (used for quizzes, signing documents) (https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334) |
| Users describe the 3-layer workflow (original page / handwriting / annotations-corrections) as the killer feature for study notes (https://www.lemon8-app.com/@schiann_/7343412417865269765?region=us) |
| Paperless X: search tool is the worst feature — titles and tags only (https://beingpaperless.com/noteful-complete-review-2022/) |
| Reddit: "I want to like Noteful… the pens just feel so weird to me" — ink feel split opinion vs Freenotes' pencil feel (https://www.reddit.com/r/ipad/comments/1rirmmo/best_handwritten_notetaking_app_for_ipad/) |
| 4.8/5 from 24K ratings — the best-rated of the three-layer apps (https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334) |

### Wants
| What people want changed |
|---|
| Content search inside notes (https://beingpaperless.com/noteful-complete-review-2022/) |
| Better pen/ink feel (https://www.reddit.com/r/ipad/comments/1rirmmo/best_handwritten_notetaking_app_for_ipad/) |
| More brushes/tools beyond the minimal set (https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334) (UNVERIFIED as aggregated request) |

### Video evidence
- Paperless X has written reviews plus a user-guide site (howto.beingpaperless.com) with step-by-step footage for the app family (https://howto.beingpaperless.com/freenotes-user-guide-for-beginners-ipad/ — Freenotes; Noteful guide exists in the same series, UNVERIFIED exact URL).
- No official YouTube channel found for Noteful; walkthroughs are third-party only (UNVERIFIED specific video URLs).

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | Core writing, 3 basic templates |
| Pro Lifetime | $6.99 one-time (layers, unlimited notebooks, tags, iCloud sync, auto-backup, premium templates) |
| Platforms | iPadOS, iOS, macOS (M1+), visionOS |

### Contradictions
- Pricing drift: $3 IAP at launch (2021) (https://www.tapsmart.com/apps/noteful-review/) → $9.99 one-time (June 2026 reporting) (https://www.alphonsolabs.com/best-note-taking-apps-ipad-2026/) → $6.99 lifetime in the current App Store IAP list (https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334). Use the live store figure.

Sources: https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334 ; https://www.getnoteful.com/ ; https://beingpaperless.com/noteful-complete-review-2022/ ; https://www.atlasworkspace.ai/blog/best-note-taking-apps-for-ipad

---
## Freenotes
### Visual surface
- iPad/iPhone: a modern, minimalist handwriting app — floating toolbar that docks on any side and blends into the page, a second and third toolbars, in-app split screen, and PiP video while writing; big template/AI marketplaces (https://beingpaperless.com/freenotes-for-ipad-2025-review-handwriting-app/, https://zapier.com/blog/best-note-taking-app-for-ipad-iphone/).
- SHOT-LIST:
  - iPad editor with floating toolbar + layers — https://apps.apple.com/us/app/freenotes-ai-notes-taking/id6464237904 (App Store screenshots)
  - Active Recall Tape tool demo — same App Store screenshots
  - Infinite-canvas whiteboard — same screenshots
  - User-guide screenshots — https://howto.beingpaperless.com/freenotes-user-guide-for-beginners-ipad/

### Docs analysis
- Feature set (official listing): AI Summary, AI Chat with PDF, AI Homework Helper, AI Study Companion, auto-organizing, OCR search, PDF annotation, infinite canvas, shape recognition, hyperlinks (planner-style clickable links), Active Recall Tape, templates (grid/Cornell/dotted), flashcards from pages, PiP video learning with screenshot capture, iCloud & Google Drive sync (https://apps.apple.com/us/app/freenotes-ai-notes-taking/id6464237904)
- Free today, monetizing in progress: ads plus Plus/Pro membership ladders ($1.99/week, $9.99/yr Plus, $6.99/wk or $19.99/mo or $39.99/yr Pro, $29.99 Plus lifetime, $29.99 remove-ads) (https://apps.apple.com/us/app/freenotes-ai-notes-taking/id6464237904)
- Company: Chinese origin (Hangzhou Free Note Technology), now FREENOTES AI PTE. LTD. (SG); iPad/iPhone only, runs unverified on Apple-silicon Macs (https://beingpaperless.com/freenotes-for-the-ipad-complete-review/)
- Data label: identifiers used to track across apps/websites — a privacy outlier among notes apps (https://apps.apple.com/us/app/freenotes-ai-notes-taking/id6464237904)
- v3.49: iPhone Duo foldable support with split transcript/playback, Quark Cloud Drive import, seasonal icon packs (https://apps.apple.com/us/app/freenotes-ai-notes-taking/id6464237904)
- Design decisions worth borrowing: floating dockable toolbar; Active Recall Tape as a named study tool; PiP video+notes; monetization via ads→subscription ladder (a path to watch, not necessarily to copy).

### Features
| Area | Detail |
|---|---|
| Handwriting | Low-latency ink, custom brushes, shape recognition, handwriting beautification with font import |
| AI | Summary, chat-with-PDF, homework helper, study companion, auto-organization |
| Study | Active Recall Tape, flashcards from pages, OCR search |
| Media | PiP video notes with screenshot capture, audio recording + transcripts |
| Sync | iCloud, Google Drive, Quark Cloud Drive |
| Layers | Layers within notes for quizzes/organization (https://zapier.com/blog/best-note-taking-app-for-ipad-iphone/) |

### Sentiment
| What people say |
|---|
| Hailed as "the best value there is" for iPad note-taking (free with layers, AI, split screen) (https://zapier.com/blog/best-note-taking-app-for-ipad-iphone/) |
| Pencil-feel praised as the best among the new-generation apps (https://www.reddit.com/r/ipad/comments/1rirmmo/best_handwritten_notetaking_app_for_ipad/) |
| Ink smoothness complaints vs native Notes/Notability (https://www.reddit.com/r/freenotes/comments/1dgyzsw/better_handwriting_support/) |
| Users leaving over "ads and subscription push" (https://www.reddit.com/r/ipad/comments/1rirmmo/best_handwritten_notetaking_app_for_ipad/) |
| 4.7/5 from 64K ratings — largest review base of the trio (https://apps.apple.com/us/app/freenotes-ai-notes-taking/id6464237904) |

### Wants
| What people want changed |
|---|
| Smoother handwriting engine (https://www.reddit.com/r/freenotes/comments/1dgyzsw/better_handwriting_support/) |
| No ads / fairer monetization (https://www.reddit.com/r/ipad/comments/1rirmmo/best_handwritten_notetaking_app_for_ipad/) |
| Desktop app (only unverified Mac support) (https://beingpaperless.com/freenotes-for-the-ipad-complete-review/) |

### Video evidence
- Paperless X maintains an official-style user guide with video walkthroughs for Freenotes (https://howto.beingpaperless.com/freenotes-user-guide-for-beginners-ipad/).
- No first-party demo channel verified; App Store "Events" posts (e.g. the iPhone Duo event) substitute for demo videos (https://apps.apple.com/us/app/freenotes-ai-notes-taking/id6464237904).
- Comment threads under third-party walkthroughs were not captured this pass (UNVERIFIED).

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | Full app with ads |
| Plus | $9.99/yr or $29.99 lifetime |
| Pro | $6.99/wk, $19.99/mo, or $39.99/yr |
| Remove ads | $29.99 one-time |
| Platforms | iOS/iPadOS (visionOS, unverified Mac) |

### Contradictions
- "Currently a free app… not sure when the developers will start charging" (2024 review, https://beingpaperless.com/freenotes-for-the-ipad-complete-review/) vs the fully built subscription ladder now live (https://apps.apple.com/us/app/freenotes-ai-notes-taking/id6464237904) — the monetization prediction landed. Also the name: App Store shows both "Freenotes: AI Notes Taking" and "Freenotes®:AI Notes, Docs, PDF" — same app id.

Sources: https://apps.apple.com/us/app/freenotes-ai-notes-taking/id6464237904 ; https://beingpaperless.com/freenotes-for-the-ipad-complete-review/ ; https://zapier.com/blog/best-note-taking-app-for-ipad-iphone/ ; reddit threads above

---
## Notes+ (SINGFISH)
### Visual surface
- iPad-first ("Notes+ : Notes for Pencil", 8M+ claimed active users): a feature-dense editor — 32 pen types including screenshot pen, vanish (temporary) pen, laser pen, dotted/wavy line pens; margin extension; oversized notes; grid view page jumping; dual-page split view of the same document; in-app browser; built-in calculator and timer (https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989).
- SHOT-LIST:
  - iPad editor with pen carousel and margin extension — https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989 (App Store screenshots)
  - Dual Pages split view — same screenshots
  - Layers UI (3-layer system) — same screenshots
  - Official site — https://www.notesplus.com (Terms/Privacy confirm domain; site not fetched this pass — UNVERIFIED layout)

### Docs analysis
- Layers: "solve a problem multiple times using the layering function with up to three layers" — built-in, not Pro-gated (https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989)
- AI monetization is extreme: AI One bundle $24.99/mo or $137.99/yr covers 6 AI tools (summary, quiz, flashcards, audio transcription+summary, YouTube subtitle+summary, NoteSnap pen); individual AI tools $7.99-15.99 (monthly subs); fonts $9.99; four-AI-features unlock $12.99/$71.99 (https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989)
- Requires iOS 17+; runs on iPhone, iPad, M1+ Mac, visionOS; age rating 16+ (unrestricted web access) (https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989)
- Data collection: diagnostics only, not linked to identity (https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989)
- v6.5.9 (Oct 2026): handwriting + text-box search added; colors/templates on extended pages (https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989)
- Design decisions worth borrowing: vanish pen (temporary ink) and screenshot pen as novel capture tools; up-to-3-layers for repeat problem solving; margin extension; dual-view of the same document; per-tool AI micro-subscriptions (an aggressive — and likely alienating — monetization pattern).

### Features
| Area | Detail |
|---|---|
| Handwriting | 32 pens (screenshot/vanish/laser/dotted/wavy), shapes, cover tool |
| Layers | Up to 3 layers, toggleable |
| PDF | Import/convert files from Windows/Mac, web-page-to-PDF import, margin extension |
| Media | Audio recording, PiP, in-app browser, calculator, timer |
| AI | 6-tool bundle + per-tool subscriptions |
| Sync | iPad↔iPhone sync |

### Sentiment
| What people say |
|---|
| 4.7/5 from 3.2K ratings; users thank the dev team effusively (https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989) |
| Layers confusion: Reddit users find the layer system unintuitive vs Noteful, redirected to a user guide (https://www.reddit.com/r/ipad/comments/1rpajxq/can_anymore_explain_how_to_use_layers_in_notes_app/) |
| Widely recommended in "best app" threads alongside Noteful/Freenotes as the budget layer-trio (https://www.atlasworkspace.ai/blog/best-note-taking-apps-for-ipad) |

### Wants
| What people want changed |
|---|
| Simpler, more discoverable layers UX (https://www.reddit.com/r/ipad/comments/1rpajxq/can_anymore_explain_how_to_use_layers_in_notes_app/) |
| Less aggressive AI subscription pricing (https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989) (inferred from IAP structure; UNVERIFIED as direct complaints) |

### Video evidence
- No official demo channel verified this pass (UNVERIFIED); the developer links a user guide from support (referenced by Reddit helpers, https://www.reddit.com/r/ipad/comments/1rpajxq/can_anymore_explain_how_to_use_layers_in_notes_app/).
- Third-party iPad-notes YouTubers cover it in roundups; specific URLs not captured (UNVERIFIED).

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | Core note-taking with ads (age 16+ listing implies ad content) |
| AI One | $24.99/mo or $137.99/yr |
| Per-tool AI | $7.99-15.99/mo each |
| Fonts/pen unlocks | $9.99, $12.99, $71.99 one-offs |
| Platforms | iOS/iPadOS 17+, macOS M1+, visionOS |

### Contradictions
- "Free" listing with 8M users (https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989) vs per-tool AI subscriptions costing up to $24.99/mo — the AI bundle alone costs more yearly than Goodnotes Pro. Also contact email bella@notesplus.com and notesplus.com domain suggest a rebrand from the older "Notes Plus" app; relationship UNVERIFIED.

Sources: https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989 ; https://www.reddit.com/r/ipad/comments/1rpajxq/can_anymore_explain_how_to_use_layers_in_notes_app/ ; https://zapier.com/blog/best-note-taking-app-for-ipad-iphone/

---
## Drawboard PDF
### Visual surface
- Windows (flagship): a radial/favorites markup UX — a customizable favorites bar of markup tools, radial-menu option, pressure-sensitive ink, canvas-first document view; dark mode; grid paper backgrounds (notebook, Gregg/Pitman ruled, graph, engineering, isometric) (https://www.drawboard.com/pdf, https://sourceforge.net/software/product/Drawboard-PDF/).
- iOS/Android/web: same markup toolkit; Drawboard Cloud as the new home for shared docs (https://slashdot.org/software/p/Drawboard-PDF/).
- SHOT-LIST:
  - Windows favorites-bar markup on a plan drawing — https://www.drawboard.com/pdf (product page visuals)
  - Drawboard Cloud sharing screen — https://slashdot.org/software/p/Drawboard-PDF/ (copy) and App Store screenshots https://apps.apple.com/us/app/drawboard-pdf-paperless-tools/id1086503728
  - Pricing page (PDF vs Projects split) — https://www.drawboard.com/pricing

### Docs analysis
- Free "Pro Basic/Essentials" plan since May 2020 (previously a $10 once-off); paid plans: Pro Lite $5.99/mo, Pro Plus $9.99/mo, Pro Unlimited $18.99/mo, 30% annual discount; some lifetime IAPs exist on iOS (Pro Lite $49.99, Pro Unlimited $159.99 per App Store IAP list) (https://sourceforge.net/software/product/Drawboard-PDF/, https://apps.apple.com/us/app/drawboard-pdf-paperless-tools/id1086503728, https://support.drawboard.com/hc/en-us/articles/4409163761423-Understanding-our-Subscription-Model)
- Students/teachers: one-off payment for Pro, no subscription, no renewals (https://www.drawboard.com/pricing)
- Legacy License program (2025): acknowledging early users, restores premium features for legacy $10 buyers (https://www.drawboard.com/blog/acknowledging-drawboards-early-users-and-introducing-the-legacy-license)
- Feature moves: some Essentials tools were moved into Pro tiers (https://www.drawboard.com/pdf/new-pro-plans); 256-bit encryption, passwords, digital signatures, full offline mode (https://sourceforge.net/software/product/Drawboard-PDF/)
- License must be linked to a cloud account on sign-in (https://support.drawboard.com/hc/en-us/articles/4406251856527-Plans-Benefits)
- No built-in OCR (community workaround: use other tools) (https://www.reddit.com/r/Surface/comments/12yhyv2/drawboard_pdf_app/)
- Design decisions worth borrowing: favorites bar + radial menu as the markup UX; education one-time Pro; Legacy License as a real repair mechanism for the 2023 user anger; engineering-grid paper backgrounds.

### Features
| Area | Detail |
|---|---|
| Markup | Pens/shapes/stamps/cloud, favorites bar, radial menu, pressure ink |
| Documents | Merge/split, bookmarks, password/signatures, encryption |
| Grids | Engineering/isometric/graph/ruled papers |
| Sharing | Drawboard Cloud |
| Gaps | No OCR, no tags comparable to Noteful/LiquidText (https://www.reddit.com/r/Surface/comments/15pg478/drawboard_pdf_removed_paid_functionality_and/) |

### Sentiment
| What people say |
|---|
| Best-ink-on-Surface reputation persists; "smells like roses in comparative reviews" (https://www.reddit.com/r/Surface/comments/15pg478/drawboard_pdf_removed_paid_functionality_and/) |
| 2023: paid functionality removed from lifetime purchases — "stole my license", censure demanded (https://www.reddit.com/r/Surface/comments/15pg478/drawboard_pdf_removed_paid_functionality_and/, https://www.reddit.com/r/Surface/comments/11kqjgh/drawboard_pdf_stole_my_license_is_there_lawsuit/) |
| 2025: Legacy License restores features for old buyers; anger persists in newer threads (https://www.reddit.com/r/Surface/comments/1jlaroj/drawboard_restores_access_to_premium_features_for/) |
| Subscription-fatigue: users compare with Xodo, Adobe; "subscription is crazy, not even on par with Adobe" (https://www.reddit.com/r/Surface/comments/1ormu94/drawboard_pdf_users_how_in_the_world_do_you/) |
| Authentication hoops: repeated logins between app and web interfaces (https://www.reddit.com/r/Surface/comments/1o89bw5/how_does_the_sub_feel_about_drawboard_pdf/) |
| G2: UI praised, easier than Adobe, free tier genuinely usable (https://www.g2.com/products/drawboard-pdf/reviews) |

### Wants
| What people want changed |
|---|
| Honored one-time licenses (partially answered by Legacy License) (https://www.drawboard.com/blog/acknowledging-drawboards-early-users-and-introducing-the-legacy-license) |
| Tagging/organization to catch up with Noteful/LiquidText (https://www.reddit.com/r/Surface/comments/15pg478/drawboard_pdf_removed_paid_functionality_and/) |
| Fewer pop-ups to subscribe (https://www.reddit.com/r/Surface/comments/18jo9mt/any_good_drawboard_alternative/) |

### Video evidence
- Windows Central's 2018 review remains the canonical press coverage (https://www.windowscentral.com/drawboard-pdf-windows-10-absolute-powerhouse); the author later noted Drawboard addressed pricing concerns directly (https://www.windowscentral.com/drawboard-pdf-windows-10-absolute-powerhouse).
- No first-party demo channel verified this pass (UNVERIFIED); community walkthroughs exist on YouTube but URLs were not captured.

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | Pro Basic/Essentials |
| Pro Lite | $5.99/mo (30% off annually) |
| Pro Plus | $9.99/mo |
| Pro Unlimited | $18.99/mo |
| iOS IAPs | Pro Lite $49.99, Pro Unlimited $159.99 lifetime |
| Education | One-time Pro payment |
| Platforms | Windows, iOS, macOS, Android, web |

### Contradictions
- The 2016-era plan ("Pro tier will replace the need for once-off payments") became the 2023 removal of paid features from paid licenses (https://www.drawboard.com/blog/acknowledging-drawboards-early-users-and-introducing-the-legacy-license, https://www.reddit.com/r/Surface/comments/15pg478/drawboard_pdf_removed_paid_functionality_and/), then the 2025 Legacy License reversal — a full round-trip recorded on their own blog.

Sources: https://www.drawboard.com/pricing ; https://sourceforge.net/software/product/Drawboard-PDF/ ; https://www.drawboard.com/blog/acknowledging-drawboards-early-users-and-introducing-the-legacy-license ; https://apps.apple.com/us/app/drawboard-pdf-paperless-tools/id1086503728 ; reddit threads above

---
## Drawboard Projects (formerly Bullclip)
### Visual surface
- Web/desktop/iOS: a project-tree workspace (Projects → documents → drawings with version stacks); the canvas shows the drawing with a right-side panel for issues, comment threads and reviewer assignments; revisions auto-publish to all members; overlay mode visually diffs two revisions. The design-review canvas is built for AEC drawings, not essays (https://www.drawboard.com/pricing, https://www.drawboard.com/projects).
- SHOT-LIST:
  - Project document tree with version stacks — https://www.drawboard.com/projects (hero visuals)
  - Drawing canvas with pinned issues and comment threads — https://www.drawboard.com/pricing (feature visuals)
  - Overlay/revision-compare screen — https://www.drawboard.com/pricing
  - Microsoft Marketplace listing screenshots — https://marketplace.microsoft.com/en-us/product/web-apps/drawboardptyltd.bullclip?exp=ubp8&tab=Overview

### Docs analysis
- Core (official pricing page): unlimited projects and workspaces; auto versioning (new revisions push to all members); revision switching; title block scan with OCR templates; overlay mode; shared public AND shared private layers; personal and shared project markup libraries; calibrated measurement toolset; guest invitations with time-limited access; offline markup on Windows/iOS; custom exports with/without annotations, issues, threads (https://www.drawboard.com/pricing)
- Issues/tasks: assign to contributors with deadlines, pin to drawing regions, threaded discussions, review statuses (Needs Review → Approved), custom task lists/statuses/tags, CSV export, public API with API keys and webhooks (Growth tier) (https://www.drawboard.com/pricing)
- Integrations: Procore, Aconex, Microsoft Teams, OneDrive/Drive/Dropbox, Revit add-in, Autodesk Forma, Archicad (Growth tier adds API/webhooks) (https://www.drawboard.com/pricing)
- Pricing: Team $29/user/mo or $270/user/yr (annual ~22% off), up to 25 users; Growth $39/user/mo or $370/user/yr, up to 150 users; Enterprise custom from 20 users; per-seat caps by tier (https://www.drawboard.com/pricing)
- Platforms: Windows, iOS, web; browser + iOS/Windows apps for Bullclip (https://crozdesk.com/software/drawboard-projects)
- Design decisions worth borrowing: markup layers with per-team visibility (public/private) as a collaboration unit; auto-versioning with revision switching; OCR title-block templates for automated drawing intake; guest time-limited seats; status workflow tied to review approvals.

### Features
| Area | Detail |
|---|---|
| Real-time markup | Live multi-user annotation on drawings |
| Versioning | Auto versioning, revision switching, overlay compare |
| Issues | Pinned issues, threads, statuses, assignments, CSV export |
| Layers | Shared public/private layers, personal markup libraries |
| Integrations | Procore, Aconex, Revit, Archicad, Autodesk Forma, Teams, cloud drives, API/webhooks |
| Security | SSO, domain restrictions, guest access |

### Sentiment
| What people say |
|---|
| Architects (Hassell, 70 seats) rely on it for multi-site drawing reviews (https://www.drawboard.com/projects) |
| G2 users: exceptional at real-time coordination meetings where speed matters (https://www.g2.com/products/drawboard-projects/reviews) |
| Capterra: switching from Adobe/Word workflow takes adjustment; real-time create/share/download called innovative (https://www.capterra.com/p/162608/Bullclip/) |
| Crozdesk 79/100 with rising trend (https://crozdesk.com/software/drawboard-projects) |
| Positioned as PDF-markup specialist vs Procore's full PM suite (https://saasrat.com/products/bullclip) |
| Consumer-grade anger at Drawboard PDF's subscription spills over onto the Projects brand (https://www.reddit.com/r/Surface/comments/15pg478/drawboard_pdf_removed_paid_functionality_and/) |

### Wants
| What people want changed |
|---|
| Cheaper per-seat pricing for small firms (Team tier caps at 25 users; enterprise from 20) (https://www.drawboard.com/pricing) (inferred from tier structure; no direct quote captured — UNVERIFIED) |
| Deeper PM-suite breadth vs Procore (https://saasrat.com/products/bullclip) |

### Video evidence
- No first-party demo channel captured this pass (UNVERIFIED); the Microsoft Marketplace listing is the primary visual reference (https://marketplace.microsoft.com/en-us/product/web-apps/drawboardptyltd.bullclip?exp=ubp8&tab=Overview).
- The 2021 rebrand blog post narrates product evolution with screenshots (https://www.drawboard.com/blog/drawboard-projects-the-next-evolution-of-bullclip).

### Pricing and platforms
| Item | Detail |
|---|---|
| Team | $29/user/mo or $270/user/yr, ≤25 users |
| Growth | $39/user/mo or $370/user/yr, ≤150 users |
| Enterprise | Custom, from 20 users |
| Platforms | Windows, iOS, web |

### Contradictions
- none found (niche product with consistent reporting)

Sources: https://www.drawboard.com/pricing ; https://www.drawboard.com/projects ; https://www.g2.com/products/drawboard-projects/reviews ; https://crozdesk.com/software/drawboard-projects ; https://saasrat.com/products/bullclip

---
## PDFCraft (ArtCraft)
### Visual surface
- Desktop (macOS/Windows/Linux/FreeBSD, plus a WebAssembly build): a workbench-style PDF editor — tabbed documents, left Tools panel (F4 toggles, widths remembered), right side panel for bookmarks/thumbnails/comments, an Organize-pages grid where pages sit like cards on a table, and a ⌘K command palette over every tool; light and dark themes (https://github.com/storytold/pdfcraft).
- Its own README screenshot pipeline (`cargo xtask screenshots`) is the visual documentation: the showcase 13-page specimen PDF open with the All tools panel and threaded comments (https://github.com/storytold/pdfcraft).
- SHOT-LIST:
  - Viewer with Tools panel and threaded comments — https://github.com/storytold/pdfcraft (README screenshots)
  - Organize-pages grid with multi-selection — https://github.com/storytold/pdfcraft
  - Document Properties security tab — https://github.com/storytold/pdfcraft
  - Product page hero — https://getartcraft.com/apps/pdfcraft

### Docs analysis
- Scope (official): read/search/organize/combine/split/secure; incremental atomic saves that keep original bytes intact (verified with qpdf on CI); 40-bit RC4→AES-256 security handler incl. Unicode passwords and permission honoring; comments with replies; form fill/authoring with sandboxed JS; redaction/sanitizing; basic digital signatures; accessibility checker; printing (https://github.com/storytold/pdfcraft)
- Honest alpha disclosure: 57% of tracked feature parity, 94% of core essentials; weak at office-doc→PDF, .docx export loses layout; editing existing text (esp. CJK/RTL), OCR beyond Latin, Preflight/PDF/X/UA all "thin or missing" (https://github.com/storytold/pdfcraft)
- Agent-first design: `pdfcraft-cli` tool table with JSON schemas, an opt-in MCP server over stdin/stdout (never self-started, no network port), and a loopback UI-control channel for driving the real interface; `--root` confines file access (https://github.com/storytold/pdfcraft)
- Clean-room claim: behavior from ISO 32000 and black-box observation; 983-file pdf.js corpus: 0 crashes, 963 render clean; engine/UI crate split with UI swappable (https://github.com/storytold/pdfcraft)
- No account, no telemetry, no cloud; dual MIT/Apache-2.0; ArtCraft branding excluded from the license (https://github.com/storytold/pdfcraft)
- Design decisions worth borrowing: incremental atomic saves as a data-integrity guarantee (rare in the notes-app space); "pages as cards" organize grid with deep named undo; honest quantified parity disclosure; agent/CLI surface as a first-class product axis; clean-room renderer discipline.

### Features
| Area | Detail |
|---|---|
| Reading | Continuous/single/two-up/rotation/Read mode, deep zoom tiling, bookmarks search, page labels |
| Editing | Page rotate/delete/insert/reorder, combine/extract/split preserving links/forms/layers |
| Comments | Threaded comments incl. highlights by find-text, replies, status |
| Forms/Security | Fill/author forms, RC4→AES-256, permissions, redaction, signatures (basic) |
| Automation | CLI, JSON scripts, opt-in MCP server, UI-control loopback channel |
| Not yet | Text-content editing, office import/export, Latin-only OCR, Preflight |

### Sentiment
| What people say |
|---|
| "Uninstalled Acrobat DC thanks to PdfCraft" — 800+ upvotes; users treat it as a real Acrobat replacement (https://www.reddit.com/r/ArtCraftAI/comments/1x4h8gd/i_uninstalled_acrobat_dc_thanks_to_pdfcraft_thank/) |
| Rated 9.5/10 in performance tests vs Adobe with better privacy and fewer resources (https://www.reddit.com/r/BestGitHubRepos/comments/1x48dxc/pdfcraft_the_pdf_workbench_an_opensource/) |
| Trust anxieties: virus scanners (NordVPN/AVG) flag the ArtCraft launcher; community runs its own security checks (https://www.reddit.com/r/ClaudeCode/comments/1x3aue7/ran_a_security_check_of_artcrafts_pdfcraft_and/, https://www.reddit.com/r/ArtCraftAI/comments/1x9xyyt/pdfcraft_not_printing/) |
| "Is PDFCraft really safe?" threads get ~30-upvote reassurance answers (https://www.reddit.com/r/ArtCraftAI/comments/1xberer/is_pdfcraft_really_safe/) |
| Users keep Sumatra for viewing due to bookmark quirks but call PdfCraft "really amazing" (https://www.reddit.com/r/ArtCraftAI/comments/1x5ocfx/thank_you_and_please_keep_working_on_pdf_craft/) |
| Al Jazeera covers ArtCraft as AI-built challenger to Adobe's economic model (https://www.aljazeera.com/news/2026/10/14/how-ai-apps-are-offering-free-substitutes-for-big-tech-software) |
| HN: "settles whether one can build large, working software with AI" (https://news.ycombinator.com/item?id=49958850) |

### Wants
| What people want changed |
|---|
| Paper printing working reliably (printing bugs reported) (https://www.reddit.com/r/ArtCraftAI/comments/1x9xyyt/pdfcraft_not_printing/) |
| Image export (PDF→JPEG/PNG) (https://www.reddit.com/r/ArtCraftAI/comments/1x4h8gd/i_uninstalled_acrobat_dc_thanks_to_pdfcraft_thank/) |
| Bookmark/viewing polish (https://www.reddit.com/r/ArtCraftAI/comments/1x5ocfx/thank_you_and_please_keep_working_on_pdf_craft/) |

### Video evidence
- No official demo videos found (UNVERIFIED); the README's generated screenshot set serves as visual docs (https://github.com/storytold/pdfcraft).
- HN thread 49958850 is the key discussion: commenters note Mac touchpad bugs in PhotoCraft, question the AI-built origin, and report no suspicious behavior (https://news.ycombinator.com/item?id=49958850).
- Reddit comment threads center on safety and migration from Acrobat; what reviews omit: the antivirus false-positive friction on the launcher is the biggest onboarding complaint (https://www.reddit.com/r/ClaudeCode/comments/1x3aue7/ran_a_security_check_of_artcrafts_pdfcraft_and/).

### Pricing and platforms
| Item | Detail |
|---|---|
| Price | Free, open source (MIT/Apache-2.0) |
| Platforms | macOS, Windows (x64/x86/ARM64), Linux, FreeBSD, Web/WASM |
| Distribution | ArtCraft Launcher, standalone installers, MSIs signed (Learning Machines) |

### Contradictions
- The brief's "PDFCraft (ArtCraft)" links to a desktop PDF workbench, not an iPad/handwriting app — if earlier rounds recorded it as a mobile notes app, that picture is wrong (https://getartcraft.com/apps/pdfcraft). Also, "ArtCraft" doubles as the name of the team's AI image/video studio (https://getartcraft.com/apps/pdfcraft), and press frames the whole suite as AI-generated software built to undercut Adobe (https://www.aljazeera.com/news/2026/10/14/how-ai-apps-are-offering-free-substitutes-for-big-tech-software) while the README itself claims clean-room engineering discipline — both can be true, but the AI-construction narrative dominates outside the repo (https://news.ycombinator.com/item?id=49958850).

Sources: https://github.com/storytold/pdfcraft ; https://getartcraft.com/apps/pdfcraft ; https://news.ycombinator.com/item?id=49958850 ; reddit threads above ; https://www.aljazeera.com/news/2026/10/14/how-ai-apps-are-offering-free-substitutes-for-big-tech-software

---
LANE A COMPLETE — 17 of 17 apps covered
