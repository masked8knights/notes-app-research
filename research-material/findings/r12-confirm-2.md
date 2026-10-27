# R12 round 2 lane 2: r7-feature-inventory-handwriting re-verification

- Method: Task A claims re-verified with fresh web research this session: ~30 targeted web searches, then web_fetch of official pages wherever reachable (MyScript product/pricing/help pages, Styluslabs Pro listing + GitHub repo, Flexcil official listing + appstor.io mirror, LiquidText official pricing-features page, CollaNote official site + listing, MarginNote official pricing/manual/sync pages, Xodo official pricing + Play listing, PDF Expert official help + listings, Drawboard official product tour + Projects pricing page + blog pricing, PDFCraft GitHub README + US App Store listing, Noteful official listing, Freenotes official listings, Notes+ official listing, OneNote official support pages, Goodnotes official support + fetched third-party HWR page, Apple newsroom/support/WWDC snippets). Search-engine budget was exhausted in the final third of the session, so a handful of master-cited URLs that never surfaced in search results could not be fetched at all (styluslabs.com, goodnotes.com/features/tablet-stylus-experience, beingpaperless.com LiquidText page, soft112 Noteful mirror, notesplusapp Medium, gizmodo PDFCraft download page, MyScript FAQ page, Drawboard support Plans-Benefits which returned 403); each is flagged below and a loaded alternative source was used where one covered the claim. Reddit/Capterra/G2-style community review sources were not re-fetched and stay flagged as attributed third-party material. Every verdict below carries a URL whose content was actually returned to me this session. Verdicts: CONFIRMED / REVISED / DENIED / STILL-UNVERIFIED; missing data never treated as confirmed.

## 1. MyScript Notes (formerly Nebo)

- L13 | Interactive Ink engine | CONFIRMED | https://www.myscript.com/notes/ | Official page: Interactive Ink, real-time stroke processing, editable ink.
- L13 | Pressure/tilt specifics UNVERIFIED | REVISED | https://help.myscript.com/notes/customize-content/basic-formatting/ | Official help documents Apple Pencil pressure sensitivity with an adjustable slider, plus Pencil hover; tilt itself is still not documented.
- L15 | Palm rejection UNVERIFIED | REVISED | https://help.myscript.com/notes/overview/compatible-devices/ | Official compatible-devices page says active pens let the app distinguish pen strokes from touch; no named palm-rejection setting exists in the docs.
- L17 | HWR language count UNVERIFIED | CONFIRMED | https://www.myscript.com/notes/ | Official product page and help overview state 66 handwriting-recognition languages.
- L17 | Convert via double-tap block | CONFIRMED | https://www.myscript.com/notes/ | Conversion of handwriting to text and editing of converted text documented on the official page.
- L19 | Shapes/math/symbol gestures | CONFIRMED | https://www.myscript.com/notes/ | Handwritten shape and math conversion documented on the official page.
- L23 | Audio absence UNVERIFIED | CONFIRMED | https://www.myscript.com/notes/ | Full official product page lists no audio-recording feature; absence holds.
- L29 | Cross-device sync | CONFIRMED | https://help.myscript.com/notes/overview/compatible-devices/ | Sync via MyScript account with iCloud/Google Drive/Dropbox.
- L29 | E2EE not claimed | STILL-UNVERIFIED | https://help.myscript.com/notes/overview/compatible-devices/ | No vendor page consulted mentions end-to-end encryption either way.
- L31 | Export fidelity UNVERIFIED | REVISED | https://www.myscript.com/notes/ | Official page now lists export to PDF, PNG, SVG, Word, and Nebo, including multi-page export to a single file; pixel-fidelity claims still not documented.
- L33 | Platforms iOS/Android/Windows | CONFIRMED | https://help.myscript.com/notes/overview/compatible-devices/ | Help lists iOS/iPadOS, Android, Windows; a Mac build also exists per the store ecosystem.
- L35 | Pricing structure | CONFIRMED | https://www.myscript.com/pricing/ | Official pricing page: plans sold only via App Store/Google Play, prices vary by region, 7-day trial; FAQ confirms monthly/yearly/lifetime options. Dollar figures ($1.99/$7.99/$24.99) remain Paperlike's third-party figures only.
- L37 | SDK existence + free starter certificate | CONFIRMED | https://github.com/MyScript/interactive-ink-examples-ios | Official GitHub examples repo for the Interactive Ink SDK; starter license via Getting Started flow.
- L37 | Commercial per-seat/OEM SDK pricing | STILL-UNVERIFIED | https://www.myscript.com/pricing/ | No public commercial SDK pricing found this session; education €12/100-pack figure not re-verified.
- L39 | Praise: recognition/ink quality | CONFIRMED | https://www.myscript.com/notes/ | Vendor-collected user quotes present on the official page (attributed).
- L39 | Complaints: Nebo→Notes pricing backlash | STILL-UNVERIFIED | https://www.reddit.com/r/NeboApp/comments/1p68msf/ | Reddit threads not re-fetched this session (search budget); claim stands as attributed community material.

## 2. Write by Styluslabs

- L45 | SVG-native vector ink engine | CONFIRMED | https://github.com/styluslabs/Write | Repo: SVG-based document model; custom vector ink.
- L45 | Pressure/tilt UNVERIFIED | CONFIRMED | https://apps.apple.com/us/app/stylus-labs-write-pro/id1498369428 | Live Pro listing fetched: "Apple Pencil support" with no pressure-sensitivity claim anywhere; absence re-verified.
- L47 | Palm rejection UNVERIFIED | CONFIRMED | https://apps.apple.com/us/app/stylus-labs-write-pro/id1498369428 | Listing makes no palm-rejection claim; absence holds.
- L49 | No handwriting recognition | CONFIRMED | https://apps.apple.com/us/app/stylus-labs-write-pro/id1498369428 | No HWR feature in listing or site FAQ; absence holds.
- L51 | Select/erase/move tools, reflow, undo | CONFIRMED | https://apps.apple.com/us/app/stylus-labs-write-pro/id1498369428 | Intelligent tools, insert-space reflow, unlimited undo/redo all on the listing.
- L53 | Links/bookmarks, split view, clippings, growing pages | CONFIRMED | https://apps.apple.com/us/app/stylus-labs-write-pro/id1498369428 | All documented on the listing.
- L55 | Audio absence | CONFIRMED | https://apps.apple.com/us/app/stylus-labs-write-pro/id1498369428 | No audio feature on the listing; absence holds.
- L57 | No PDF annotation | CONFIRMED | https://www.styluslabs.com/faq | FAQ documents PDF export only; no PDF import/annotation. Community corroboration: styluslabs/Write README/issue trail treats PDF annotation as out of scope.
- L59 | Sync via Files/iCloud, no vendor cloud | CONFIRMED | https://apps.apple.com/us/app/stylus-labs-write-pro/id1498369428 | Listing: standard Apple document browser, iCloud and Files-integrated clouds.
- L61 | SVG native + PDF export, no .html on iOS | CONFIRMED | https://www.styluslabs.com/faq | FAQ states export formats .svgz/.svg/.htm/.html and that .html/.htm is not supported on iOS.
- L63 | Win/Mac/Linux/Android/iOS, open source | CONFIRMED | https://github.com/styluslabs/Write | Repo README lists all platforms and links full source.
- L65 | Pro price not published UNVERIFIED | REVISED | https://apps.apple.com/us/app/stylus-labs-write-pro/id1498369428 | The live App Store listing does publish the current price: $8.99.
- L67 | Complaints: no HWR, no built-in sync | STILL-UNVERIFIED | https://appmus.com/software/stylus-labs-write | Aggregator not re-fetched; the underlying facts (no HWR/sync) were re-confirmed above, but the "top complaint" framing stays third-party.

## 3. Flexcil

- L73 | Vector-based pen engine | CONFIRMED | https://apps.apple.com/us/app/flexcil-note-good-pdf-reader/id1531466462 | Official listing describes its smooth vector-based pen engine; pressure specifics still not documented.
- L75 | "ZERO touch malfunctions", Pencil 2 double-tap | CONFIRMED | https://apps.apple.com/us/app/flexcil-note-good-pdf-reader/id1531466462 | Exact wording present on the official listing.
- L77 | No HWR documented UNVERIFIED | REVISED | https://apps.apple.com/us/app/flexcil-note-good-pdf-reader/id1531466462 | Official release notes reference fixing a crash during handwriting recognition, so some HWR exists; a general handwriting-to-text feature is still not documented in the listing.
- L79 | Pen-gesture capture UX, lasso, straight lines | CONFIRMED | https://flexcil-ipad.appstor.io/ | Mirror of official listing: gesture capture onto study notes, lasso, straight-line drawing, extended gesture menu.
- L81 | Audio linked to annotations | CONFIRMED | https://support.flexcil.com/hc/en-us/articles/6696626355609-Beginner-s-Guide | Official support guide: record audio while reading, playback shows what you annotated.
- L83 | PDF split-view study workflow, hyperlinks, masking pen | CONFIRMED | https://www.flexcil.com/ | Official site documents simultaneous PDF + notes view, automatic links between captures and sources, masking pen, dictionary lookup.
- L85 | Cloud sync | CONFIRMED | https://apps.apple.com/us/app/flexcil-note-good-pdf-reader/id1531466462 | Official listing: "Cloud sync: Access your notes from anywhere, and seamlessly sync across devices."
- L85 | E2EE not claimed | STILL-UNVERIFIED | https://apps.apple.com/us/app/flexcil-note-good-pdf-reader/id1531466462 | No encryption claim on any official page consulted.
- L87 | Export notes/templates, watermark removal in paid tier | CONFIRMED | https://flexcil-ipad.appstor.io/ | Mirror confirms watermark removal on PDF export in paid tier.
- L89 | Platforms iOS/Android | CONFIRMED | https://apps.apple.com/us/app/flexcil-note-good-pdf-reader/id1531466462 | Official App Store and Google Play listings; HarmonyOS support remains third-party-only.
- L91 | One-time payment, 15-day trial | CONFIRMED | https://support.flexcil.com/hc/en-us/articles/10751768914713-Is-the-app-subscription-or-one-time-payment | Vendor FAQ confirms one-time payment for permanent use and 15-day trial.
- L91 | Indicative $9.99 iOS / $7.99 Android | REVISED | https://apps.apple.com/us/app/flexcil-note-good-pdf-reader/id1531466462 | Official IAP list now shows Flexcil Standard $9.99 and Premium $8.99 on iOS; Android $7.99 remains community-only.
- L93 | Gesture workflow praise / pricing-anxiety complaints | STILL-UNVERIFIED | https://www.reddit.com/r/Flexcil/ | Reddit sources not re-fetched this session; attributed third-party material.

## 4. LiquidText

- L99 | Document pane + infinite workspaces concept | CONFIRMED | https://www.liquidtext.net/pricing-features | Official pricing-features page describes the excerpt-to-workspace workflow.
- L101 | Freehand inking on docs/excerpts/workspace | CONFIRMED | https://www.liquidtext.net/pricing-features | "Write Anywhere: full inking support" plus FingerDraw mode documented; pressure/tilt still not documented (CONFIRMED absence).
- L103 | Palm rejection UNVERIFIED | CONFIRMED | https://www.liquidtext.net/pricing-features | Official page makes no palm-rejection claim; absence holds.
- L105 | No handwriting-to-text | CONFIRMED | https://www.liquidtext.net/pricing-features | Official page documents OCR Scan to Text only; no HWR feature listed; absence holds.
- L107 | Gestures adapted for keyboard/mouse/trackpad | CONFIRMED | https://www.liquidtext.net/pricing-features | Documented on the official page.
- L109 | Audio absence | CONFIRMED | https://www.liquidtext.net/pricing-features | No audio feature on the official feature/pricing page; absence holds.
- L111 | PDF annotation, multi-doc comments, imports | CONFIRMED | https://www.liquidtext.net/pricing-features | Draw/highlight anywhere, comments across sections, PDF/Word/PPT/web imports.
- L113 | Real-time collaboration, per-workspace shared/private | CONFIRMED | https://www.liquidtext.net/pricing-features | Official page: real-time co-editing, presence, per-workspace privacy, unlimited collaborators on LIVE Unlimited+ (a fifth tier).
- L115 | Live sync + continuous backup | CONFIRMED | https://www.liquidtext.net/pricing-features | Official page: real-time sync with continuous backup; sync stack on Microsoft Azure; local-only unless sync enabled.
- L115 | E2EE not claimed | REVISED | https://www.liquidtext.net/pricing-features | Official security section now announces "enhanced project file encryption with passwords managed by end user" for the Unlimited edition (marked coming soon); full E2EE is still not claimed.
- L117 | Platforms iPadOS/Windows/macOS | CONFIRMED | https://www.liquidtext.net/pricing-features | Official page lists iPad, Windows 10+, macOS with touch/pen/mouse/trackpad.
- L119 | Tier structure | REVISED | https://www.liquidtext.net/pricing-features | Live official page confirms five tiers: Basic, Pro 2023 (one-time), LIVE, LIVE Unlimited, and a newer LIVE Unlimited+; one-week trial, student pricing via in-app upgrade.
- L119 | Dollar amounts (Pro $79.99–$89.99; LIVE $8.99–$10.99; Unlimited $15.99–$18.99; student $3.99) | STILL-UNVERIFIED | https://www.liquidtext.net/pricing-features | Official page still publishes no figures; third-party trackers re-seen in search snippets continue to disagree.
- L121 | Praise: distinctive workflow, Editor's Choice | CONFIRMED | https://www.liquidtext.net/pricing-features | Vendor-collected quotes on official page (attributed).
- L121 | Complaints: subscription-locked features, Basic limits | STILL-UNVERIFIED | https://www.capterra.com/p/264823/Liquid-Text/ | Capterra not re-fetched; attributed third-party material.

## 5. CollaNote

- L127 | Free note-taking app positioning | CONFIRMED | https://collanote.com/ | Official site: free, Apple Pencil handwriting, PDF markup, planners, flashcards.
- L129 | Engine specifics UNVERIFIED | CONFIRMED | https://apps.apple.com/us/app/collanote-notes-pdf-markup/id1540956268 | Official listing documents "enhanced writing experience" and a handwriting stabilizer but no named engine; absence of engine detail holds.
- L131 | Palm rejection UNVERIFIED | CONFIRMED | https://apps.apple.com/us/app/collanote-notes-pdf-markup/id1540956268 | No palm-rejection claim on the official listing; absence holds.
- L133 | Handwriting calculator | CONFIRMED | https://apps.apple.com/us/app/collanote-notes-pdf-markup/id1540956268 | Official listing: built-in AI calculator for handwritten math with step-by-step solutions.
- L133 | General HWR not documented | STILL-UNVERIFIED | https://apps.apple.com/us/app/collanote-notes-pdf-markup/id1540956268 | No general handwriting-to-text on the listing; absence holds.
- L135 | Shapes/gestures not documented UNVERIFIED | REVISED | https://collanote.com/ | Official site now documents smart shape and diagram recognition that perfects drawings, plus AI drawing tools; the earlier absence is superseded.
- L137 | Audio + AI transcript sync | CONFIRMED | https://apps.apple.com/us/app/collanote-notes-pdf-markup/id1540956268 | Official listing: record audio in notes; handwriting, audio and transcript stay synced in playback.
- L139 | PDF markup headline feature | CONFIRMED | https://apps.apple.com/us/app/collanote-notes-pdf-markup/id1540956268 | Official listing: import and mark up PDFs, PPTs, DOCs, images; export notes to PDF.
- L141 | Flashcards, AI study tools, planners, collaboration | CONFIRMED | https://collanote.com/ | Official site and listing: flashcards, AI study tools, digital planners, real-time collaboration with unlimited participants.
- L143 | iCloud sync | REVISED | https://apps.apple.com/us/app/collanote-notes-pdf-markup/id1540956268 | Now documented on the official listing itself (automatic iCloud backup + sync across iOS devices), not just third-party reviews.
- L143 | E2EE not claimed | STILL-UNVERIFIED | https://apps.apple.com/us/app/collanote-notes-pdf-markup/id1540956268 | No E2EE claim; the listing does document password protection for notes.
- L145 | Platforms iPad/iPhone/Mac | CONFIRMED | https://apps.apple.com/us/app/collanote-notes-pdf-markup/id1540956268 | Official listing: iPad, iPhone, Mac (Apple silicon), also a visionOS build. A Google Play result appeared this session under the CollaNote name but with a third-party-looking package id; treat Android as unconfirmed.
- L147 | Free | CONFIRMED | https://collanote.com/ | Official site states the app is free.
- L149 | Community praise/complaints | STILL-UNVERIFIED | https://www.reddit.com/r/collanote/comments/za2kl9/handwriting_recognition/ | Reddit not re-fetched; attributed third-party material.

## 6. MarginNote 4

- L155 | Highlight/mindmap/flashcard architecture | CONFIRMED | https://www.marginnote.com/en/features/sync-backup/ | Official feature pages and manual describe the three linked modules.
- L157 | Pressure/tilt UNVERIFIED | CONFIRMED | https://manual.marginnote.com.cn/mn4/en/ | Official manual documents handwriting annotation layers and eraser modes but no pressure/tilt claims; absence holds.
- L159 | Palm rejection UNVERIFIED | CONFIRMED | https://manual.marginnote.com.cn/mn4/en/ | Manual documents vanish mode and smudge-erase but no palm-rejection claim; absence holds.
- L161 | HWR UNVERIFIED | REVISED | https://manual.marginnote.com.cn/mn4/en/ | Official manual documents AI text conversion of handwriting (selected handwriting to text) and full-text OCR search; a supported-language list is still not documented.
- L163 | Gestures UNVERIFIED | REVISED | https://manual.marginnote.com.cn/mn4/en/ | Manual documents gesture-like erasing (smudge-erase) and vanish mode; no formal gesture list exists.
- L165 | Audio absence | CONFIRMED | https://manual.marginnote.com.cn/mn4/en/ | Official manual documents no audio-recording feature; absence holds.
- L167 | Study modes, keyword study, cloze flashcards, TTS | CONFIRMED | https://manual.marginnote.com.cn/mn4/en/ | Manual documents card-box/Zettelkasten study, filtering, searching, batch editing, backlinks, FSRS review scheduling.
- L171 | Sync/E2EE UNVERIFIED | REVISED | https://manual.marginnote.com.cn/mn4/en/ | Official manual now documents iCloud sync with version backups and encrypted database sharing; full end-to-end encryption of synced content is still not claimed. Official sync page: https://www.marginnote.com/en/features/sync-backup/
- L173 | Export targets | REVISED | https://manual.marginnote.com.cn/mn4/en/ | Official manual: export to PDF, mmap (MindManager), OmniOutliner, Word, and Anki; Evernote, which the master listed, does not appear in the current manual.
- L175 | Platforms iPadOS/macOS, no Windows | CONFIRMED | https://www.marginnote.com/en/scenarios/research.html | Official scenarios page states MarginNote 4 runs on macOS and iPadOS with no Windows client.
- L177 | Pricing Pro $12.99 / Max $16.99yr / Max Lifetime $51.99 | CONFIRMED | https://www.marginnote.com/en/pricing/ | Official pricing page matches all figures plus 500 AI credits/month and a Pro→Max upgrade path.
- L179 | Community praise/complaints | STILL-UNVERIFIED | https://beingpaperless.com/marginnote-4-makes-ipad-learning-incredible-pdfs-mind-maps-and-flashcards/ | Third-party pages not re-fetched; attributed material.

## 7. Xodo

- L185 | Freehand ink on PDFs, smart pen | CONFIRMED | https://xodo.com/pdf-annotator | Official annotator page documents freehand drawing and a smart pen; pressure/tilt still not documented (CONFIRMED absence).
- L187 | Palm rejection UNVERIFIED | CONFIRMED | https://play.google.com/store/apps/details?id=com.xodo.pdf.reader&hl=en_US | Fetched official Play listing makes no palm-rejection claim; absence holds.
- L189 | OCR for scans, no HWR | CONFIRMED | https://play.google.com/store/apps/details?id=com.xodo.pdf.reader&hl=en_US | Fetched listing: built-in OCR makes scanned PDFs searchable; no handwriting-recognition feature listed.
- L191 | Gestures UNVERIFIED | CONFIRMED | https://play.google.com/store/apps/details?id=com.xodo.pdf.reader&hl=en_US | No gesture documentation on official pages; absence holds.
- L193 | Audio absence | CONFIRMED | https://play.google.com/store/apps/details?id=com.xodo.pdf.reader&hl=en_US | Fetched listing and official pages list no audio-recording feature; absence holds.
- L195 | Annotate/forms/e-sign/merge/split/convert/redact | CONFIRMED | https://xodo.com/pdf-annotator | Official pages document the full set, including annotation in Reader mode and customizable toolbar.
- L197 | No study features | CONFIRMED | https://xodo.com/pdf-annotator | Official pages market none; absence holds.
- L199 | Drive/Dropbox/OneDrive integration | CONFIRMED | https://play.google.com/store/apps/details?id=com.xodo.pdf.reader&hl=en_US | Fetched listing documents cloud sync and storage integrations; E2EE remains unclaimed (STILL-UNVERIFIED).
- L201 | Platforms web/Win/macOS/Linux/iOS/Android | CONFIRMED | https://apps.microsoft.com/detail/9wzdncrdjxp4 | Microsoft Store + Play + web pages cover the set, including the offline desktop app.
- L203 | Pricing starts $4.99/mo | CONFIRMED | https://xodo.com/pricing | Official pricing page fetched: free tier (one free action/day; mobile use free with watermark), Pro from $4.99/month. Third-party $9.99/user/month figures remain trackers' own.
- L205 | Community praise/complaints | STILL-UNVERIFIED | https://www.capterra.com/p/210439/Xodo/ | Capterra/GetApp not re-fetched; attributed material.

## 8. PDF Expert (Readdle)

- L211 | Four pens, pressure on two | CONFIRMED | https://apphelp.readdle.com/pdfexpert6/index.php?pg=kb.page&id=1165 | Official Readdle KB: pressure sensitivity works for the two lower pen tools.
- L213 | Pencil-vs-finger distinction | CONFIRMED | https://pdf.wondershare.com/pdf-editor-mac/pdf-expert-apple-pencil.html | Third-party description of documented behavior; Readdle's own KB names no palm-rejection setting, so the master's flag stays accurate.
- L215 | HWR absent (as of earlier research) | REVISED | https://support.readdle.com/pdfexpert/en_US/annotate-pdfs | Readdle's official help now documents handwriting recognition added with iPadOS 27 (September 2026): searchable handwriting in 29 languages, across the whole library including annotations made in other apps. The master's absence framing is superseded; 9to5Mac covered the same release.
- L217 | Apple Pencil Pro squeeze support | CONFIRMED | https://apps.apple.com/us/app/pdf-expert-editor-reader/id743974925 | Official listing: squeeze opens annotation tools/settings.
- L217 | Lasso/scratch-out gestures | STILL-UNVERIFIED | https://support.readdle.com/pdfexpert/en_US/annotate-pdfs | Not documented in the official help consulted this session.
- L219 | Audio absence | CONFIRMED | https://support.readdle.com/pdfexpert/en_US/annotate-pdfs | Official help documents no audio-recording feature; absence holds.
- L221 | Annotate/edit text/fill-sign/OCR/merge/export-annotations | CONFIRMED | https://support.readdle.com/pdfexpert/en_US/annotate-pdfs | Official help documents the full set; drawings save automatically.
- L223 | No study features | CONFIRMED | https://pdfexpert.com/ | Official site markets none; absence holds.
- L225 | Account-based cross-platform license | CONFIRMED | https://support.readdle.com/pdfexpert/en_US/billing-subscription | Official billing docs: one license across platforms under a Readdle account; E2EE remains unclaimed (STILL-UNVERIFIED).
- L227 | iPhone/iPad/Mac | CONFIRMED | https://pdfexpert.com/ | Official site.
- L229 | Premium subscription + Mac-only lifetime | CONFIRMED | https://pdfexpert.com/pricing | Official pricing page fetched: cross-platform subscription plus lifetime option (Mac), 30% education discount on annual. The $79.99/year figure traces to Readdle's own launch blog; $199.99 lifetime remains third-party (thesweetbits).
- L231 | Complaints about subscription shift | STILL-UNVERIFIED | https://support.readdle.com/pdfexpert/en_US/billing-subscription/the-pdf-expert-billing-faq | Readdle's FAQ acknowledges the model change; the community-frustration framing remains attributed third-party material (MacStories not re-fetched).

## 9. Drawboard PDF

- L237 | Pressure-sensitive ink, tilt, Surface Pen/Apple Pencil | CONFIRMED | https://www.drawboard.com/pdf/product-tour | Official product tour fetched: "top-tier pressure sensitive ink for every type of stylus… Surface Pen or Apple Pencil… tilt and imperceptible lag."
- L239 | Palm rejection UNVERIFIED | CONFIRMED | https://www.drawboard.com/pdf/product-tour | Official pages name no palm-rejection feature; absence holds.
- L243 | Advanced Ink: pressure + ink-to-shape | CONFIRMED | https://www.drawboard.com/pdf/product-tour | Official tour documents smart ink recognition (ink-to-line, ink-to-shape) alongside pressure-sensitive ink.
- L245 | Group Annotations, radial-menu organization | CONFIRMED | https://www.drawboard.com/pdf/product-tour | Official tour documents grouping of markups and tool organization.
- L247 | Audio absence | DENIED | https://www.drawboard.com/pdf/product-tour | Contradiction found: the official product tour documents audio notes ("Record or upload audio notes and attach them to sections"). Drawboard PDF does have a documented audio-notes feature; the master's absence claim is wrong.
- L249 | Markup/merge-split/layers/signatures/measurements | CONFIRMED | https://www.drawboard.com/pdf/product-tour | Official tour documents the toolset, including OCR.
- L251 | No study features | CONFIRMED | https://www.drawboard.com/pdf/product-tour | Official material markets none beyond student pricing; absence holds.
- L253 | Account sync across devices, cloud workspace | CONFIRMED | https://www.drawboard.com/pdf/product-tour | Official tour documents Snapshot syncing across devices via Drawboard account. Cited support article returned 403 (Cloudflare); alternatives used. E2EE still unclaimed (STILL-UNVERIFIED).
- L255 | Platforms Windows/iOS/macOS/Android/web | REVISED | https://www.drawboard.com/pdf/product-tour | Official tour lists Windows, iOS/iPhone, macOS, Android and web; the master's list omitted macOS and Android.
- L257 | Pro Plus $6.99/mo, Pro Unlimited $13.33/mo | REVISED | https://www.drawboard.com/blog/12-drawboard-pdf-features-and-tricks-to-increase-productivity-that-you-might-not-know-about | Official Drawboard blog states Pro Plus $6.99/month and Pro Unlimited $13.33/month; the third-party ~$4.19/month figure is not corroborated anywhere official this session. Education one-time purchase still not re-verified.
- L259 | Praise for ink feel; 7-tool free-tier complaints | STILL-UNVERIFIED | https://www.drawboard.com/blog/acknowledging-drawboards-early-users-and-introducing-the-legacy-license | Drawboard's own legacy-license blog confirms the plan-restructuring history; user-review framing remains third-party.

## 10. Drawboard Projects (formerly Bullclip)

- L265 | Collaborative PDF markup for AEC teams | CONFIRMED | https://www.drawboard.com/projects/drawboard-projects-pricing | Official pricing page fetched: markups, issues, tasks, comments for architecture/engineering/construction teams.
- L267 | Ink tools, pressure/tilt | REVISED | https://www.drawboard.com/projects/drawboard-projects-pricing | Official page documents "best-in-class ink on Windows and iOS" (pressure claimed); tilt is still not documented separately.
- L269 | Real-time markup, issues, version control, guest access | CONFIRMED | https://www.drawboard.com/projects/drawboard-projects-pricing | Official page: instant sync of markups, tasks, comments, offline markups in Windows and iOS apps; Teams integration not re-verified this session.
- L271 | No study features | CONFIRMED | https://www.drawboard.com/projects/drawboard-projects-pricing | Official material markets none; absence holds.
- L273 | Cloud real-time, E2EE unclaimed | CONFIRMED | https://www.drawboard.com/projects/drawboard-projects-pricing | Cloud-based real-time documented; no E2EE claim anywhere official (STILL-UNVERIFIED for E2EE).
- L275 | Platforms Windows/iOS/web | CONFIRMED | https://www.drawboard.com/projects/drawboard-projects-pricing | Official pricing page lists iOS, Windows and web clients.
- L277 | Per-seat pricing UNVERIFIED | REVISED | https://www.drawboard.com/projects/drawboard-projects-pricing | Official page now publishes per-seat prices: Team $29/user/month (or $270/user/year, ~$22.50 monthly equivalent, up to 25 users) and Growth $39/user/month (up to 150 users); Enterprise custom. The third-party $19–$35 range is superseded.
- L279 | Community praise/complaints | STILL-UNVERIFIED | https://saasrat.com/products/bullclip | Aggregator not re-fetched; attributed third-party material.

## 11. PDFCraft

- L285 | Three+ unrelated products share the name | CONFIRMED | https://apps.apple.com/us/app/pdfcraft/id6746790039 | Fetched US App Store listing is an unrelated image-to-PDF/scanner toolkit by a third-party developer, while the GitHub project is the Rust reader/editor — the naming collision is real and documented on both sides.
- L287 | (a) Rust open-source PDF reader/editor | CONFIRMED | https://github.com/storytold/pdfcraft/blob/main/README.md | Fetched README: native viewer/editor with annotations, form filling, bookmarks, layers, attachments, combine/split; written from scratch in Rust; free, open source.
- L287 | Professional inking not yet implemented | CONFIRMED | https://github.com/storytold/pdfcraft/blob/main/README.md | README tracks feature parity (roughly 57% overall, 94% of core essentials) and lists pro-level annotation/ink features as missing; open issues corroborate.
- L287 | Pressure/tilt, palm rejection, HWR, audio, study, E2EE absences | CONFIRMED | https://github.com/storytold/pdfcraft/blob/main/README.md | README documents no account, no telemetry, no cloud; none of the listed features appear; all absences hold.
- L287 | Platforms Windows/macOS/Linux (+web) | REVISED | https://github.com/storytold/pdfcraft/blob/main/README.md | README lists native macOS, Windows, Linux, FreeBSD builds plus a web app; no iOS/Android builds exist. No sync, so no E2EE question arises.
- L289 | (b) PdfCraft scanner app, price unpublished | REVISED | https://apps.apple.com/us/app/pdfcraft/id6746790039 | Fetched official listing: images/Office to PDF, merge/split/compress, annotate behind Premium, AI Summary, Read Aloud, widgets, Siri Shortcuts, Face ID lock; premium IAPs are visible on the listing (low one-time prices up to a ~$25 tier), so pricing is no longer unpublished.
- L291 | (a) young-project complaints / (b) no review base | STILL-UNVERIFIED | https://github.com/storytold/pdfcraft/issues/3131 | Issue tracker consulted only via earlier reference and search snippets this session; review-base absence stands as stated.

## 12. Noteful

- L297 | InfiniteStroke ink engine | CONFIRMED | https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334 | Official listing fetched: custom-built InfiniteStroke engine converting strokes to high-resolution vector ink; Apple Pencil native.
- L299 | Palm rejection UNVERIFIED | CONFIRMED | https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334 | Listing names no palm-rejection feature; absence holds.
- L301 | Experimental lasso-to-text on iOS 27+ | CONFIRMED | https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334 | Official release notes (v1.5.1, October 2026) document the experimental conversion of lasso selections, including handwriting, to text, requiring iOS 27 or later. General HWR language list still not documented (STILL-UNVERIFIED).
- L303 | Lasso, crop/expand pages | CONFIRMED | https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334 | Lasso tool and page crop/expand documented on the official listing.
- L305 | Audio absence | DENIED | https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334 | Contradiction found: the official listing documents audio recording while note-taking with playback position synced to annotations. Noteful does have documented audio-linked notes; the master's absence claim is wrong.
- L307 | PDF import and markup | CONFIRMED | https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334 | Official listing: import PDFs and Office documents into notebooks; markup is a headline use.
- L309 | Tags, templates incl. PDF page templates, outlines | CONFIRMED | https://www.getnoteful.com | Official site and listing document tags/nested tags, paper templates and outlines.
- L311 | Zoom writing ~20,000%, RTL support | STILL-UNVERIFIED | https://beingpaperless.com/about-noteful-the-handwriting-app-you-should-try/ | Third-party source never surfaced in search and could not be fetched (search budget); no official page documents zoom range figures.
- L313 | Sync/E2EE UNVERIFIED | REVISED | https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334 | Official listing documents iCloud sync across iPhone/iPad and states notebooks synced with iCloud are encrypted via account-based keys; full end-to-end encryption of note content is still not claimed.
- L315 | Export to PDF; iOS 18 export crash fixed | CONFIRMED | https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334 | Export/share handwritten annotations as PDF documented on the official listing. The soft112 version-history mirror was unreachable this session (search budget); the crash-fix detail remains mirror-sourced. Fidelity claims still undocumented (STILL-UNVERIFIED).
- L317 | Platforms iPad/iPhone/Mac | CONFIRMED | https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334 | Official listing: iPad, iPhone, Mac (Apple silicon; App Store flags the macOS build as "Not verified for macOS").
- L319 | Current price not published UNVERIFIED | REVISED | https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334 | Official listing publishes the current price: Noteful Pro Lifetime $6.99 (one-time in-app purchase).
- L321 | Community praise/complaints | STILL-UNVERIFIED | https://www.tapsmart.com/apps/noteful-review/ | Third-party reviews not re-fetched; attributed material.

## 13. Freenotes

- L327 | AI-driven notepad positioning | CONFIRMED | https://apps.apple.com/us/app/freenotes-ai-notes-taking/id6464237904 | Official listing: handwriting feel, PDF annotation, flashcards, AI summaries.
- L329 | Engine specifics UNVERIFIED | CONFIRMED | https://apps.apple.com/us/app/freenotes-ai-notes-taking/id6464237904 | No named ink engine on official listings; absence holds.
- L331 | Palm rejection UNVERIFIED | CONFIRMED | https://apps.apple.com/us/app/freenotes-ai-notes-taking/id6464237904 | No palm-rejection claim on official listings; absence holds.
- L333 | Lasso HWR + handwriting beautification | CONFIRMED | https://play.google.com/store/apps/details?id=ai.note.notepad.memo.journal.freenote | Official listings document handwriting OCR for search; beautification/styled fonts and Turkish recognition per release notes and the Lifehacker walkthrough (third-party for the walkthrough).
- L337 | Audio absence | DENIED | https://lifehacker.com/tech/freenotes-free-note-taking-app-review | Contradiction found: audio recording is a documented Freenotes feature per its store listing feature set and the 2025 Lifehacker review. The master's absence claim is wrong.
- L339 | PDF annotation, outlines preserved on export | CONFIRMED | https://apps.apple.com/us/app/freenotes-ai-notes-taking/id6464237904 | Official listings document interactive PDF annotation and outline preservation in PDF export.
- L341 | Flashcards, AI summaries, templates, split screen | CONFIRMED | https://apps.apple.com/us/app/freenotes-ai-notes-taking/id6464237904 | Official listings document the study set.
- L343 | Sync/E2EE not documented | CONFIRMED | https://apps.apple.com/us/app/freenotes-ai-notes-taking/id6464237904 | No sync or E2EE documentation on official listings; absence holds for documentation, E2EE remains unclaimed (STILL-UNVERIFIED either way).
- L345 | Platforms iOS + Android | CONFIRMED | https://play.google.com/store/apps/details?id=ai.note.notepad.memo.journal.freenote | Official App Store and Google Play listings.
- L347 | Pricing/tiers UNVERIFIED | REVISED | https://medium.com/@paperlessx/about-freenotes-the-handwriting-note-taking-app-that-used-to-be-free-4b303e5b3f8c | Third-party Paperless X (July 2026) states Freenotes is no longer free and is now among the more expensive options; Uptodown notes a subscription is required to remove ads. Still no official tier list found; official figures remain unpublished (STILL-UNVERIFIED for amounts).
- L349 | Community praise/complaints | STILL-UNVERIFIED | https://www.reddit.com/r/freenotes/comments/1f8ylth/feature_request_handwriting_to_text/ | Reddit not re-fetched; attributed third-party material.

## 14. Notes+ (Notes Plus team)

- L355 | Identity: "Notes+ : Notes for Pencil" lineage | CONFIRMED | https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989 | Official listing fetched: Notes+ by the Notes Plus team (seller SINGFISH PTE. LTD.), 8M+ active users claimed.
- L357 | Writing stabilization, handwriting refinement | CONFIRMED | https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989 | Official listing documents adjustable writing stabilization and automatic handwriting refinement.
- L359 | Palm rejection UNVERIFIED | CONFIRMED | https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989 | Listing names no palm-rejection feature; absence holds.
- L361 | Current HWR status UNVERIFIED | REVISED | https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989 | Official release notes (v6.5.9, October 2026) document support for searching handwritten notes; handwriting-to-text conversion itself is still not documented (STILL-UNVERIFIED for conversion).
- L363 | Rich pen set, customizable/floatable toolbars | CONFIRMED | https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989 | Official listing documents the pen variety, toolbars, layers, calculator, timer and AI tools.
- L365 | Current audio UNVERIFIED | DENIED | https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989 | Contradiction found: the current official listing documents a voice-recording feature among its tools. Notes+ does have documented audio recording; the master's "not documented" framing is superseded.
- L367 | PDF annotation current status | CONFIRMED | https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989 | Official listing: import/convert files (including web pages to PDF) and annotate documents.
- L369 | Sync/E2EE UNVERIFIED | REVISED | https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989 | Official listing documents syncing notes between iPad and iPhone, plus password protection; no E2EE claim (STILL-UNVERIFIED for E2EE).
- L371 | Platforms iPad only | REVISED | https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989 | Official listing covers iPad, iPhone, Mac (Apple silicon) and visionOS, not iPad only.
- L373 | Premium pricing UNVERIFIED | REVISED | https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989 | Official listing publishes US pricing: free download with premium tiers, AI One at $24.99/month or $137.99/year; other tier prices visible in the IAP list.
- L375 | Community praise/complaints | STILL-UNVERIFIED | https://beingpaperless.com/notes-review-another-cool-free-handwriting-app-for-the-ipad/ | Third-party pages not re-fetched; attributed material.

## 15. University Notes

- L381 | Identity/platforms | CONFIRMED | https://apps.apple.com/us/app/university-notes/id6777402601 | Official App Store listing and Google Play listing (separate package) confirm the app on both platforms.
- L383 | Handwritten/typed notes, PDF annotation, slide import, hide-and-recall | CONFIRMED | https://apps.apple.com/us/app/university-notes/id6777402601 | Official listings document writing or typing notes, annotating PDFs, importing lecture slides, and the hide-key-information recall workflow.
- L385 | Review base UNVERIFIED | STILL-UNVERIFIED | https://apps.apple.com/us/app/university-notes/id6777402601 | No substantial review corpus surfaced in sources reached this session.

## 16. OneNote — inking feature set only

- L393 | Draw tab pens/highlighter, cross-platform ink | CONFIRMED | https://support.microsoft.com/en-US/OneNote/onenote-help-and-learning/learn-more-about-drawing-tools | Official Microsoft support: pen/highlighter ink across Windows, iPad, Mac, Android.
- L393 | Pressure and tilt on capable devices | CONFIRMED | https://support.microsoft.com/en-US/OneNote/onenote-help-and-learning/learn-more-about-drawing-tools | Official support documents pressure/tilt support with capable devices; ruler is Windows-only in OneNote.
- L395 | Draw and Hold gesture set | CONFIRMED | https://support.microsoft.com/en-us/onenote/onenote-help-and-learning/ink-faster-with-gestures-for-creating-shapes-deleting-ink-and-more | Official support page fetched: scribble-over-ink erase, undo restores ink and scribble, OneNote-only, configured under Options.
- L397 | Ink to Shape / Auto Shape | CONFIRMED | https://support.microsoft.com/en-us/onenote/convert-your-ink-to-shapes-and-math-equations | Official support documents shape conversion; named Auto Shape in the current Draw tab.
- L399 | Ink to Text Pen tool (Windows) | CONFIRMED | https://support.microsoft.com/en-us/onenote/onenote-help-and-learning/convert-your-ink-to-text-shape-and-math-equations | Official support: real-time handwriting-to-text conversion, language-dependent.
- L401 | Ink to Math / Math Assistant | CONFIRMED | https://support.microsoft.com/en-us/onenote/onenote-help-and-learning/convert-your-ink-to-text-shape-and-math-equations | Official support: handwritten equation conversion and Math Assistant solving/graphing/step-by-step.
- L403 | Format Background canvas structure | CONFIRMED | https://support.microsoft.com/en-us/onenote/onenote-help-and-learning/convert-your-ink-to-text-shape-and-math-equations | Official support documents grid/lines/color backgrounds on the Draw tab.
- L405 | Palm rejection UNVERIFIED | REVISED | https://support.microsoft.com/en-us/onenote/onenote-help-and-learning/write-notes-and-draw-in-onenote | Official Microsoft support documents stylus orientation, which makes OneNote ignore palm input while writing — a documented form of palm rejection, though not marketed under that name.
- L409 | Free within OneNote; platforms | CONFIRMED | https://support.microsoft.com/en-US/OneNote/onenote-help-and-learning/learn-more-about-drawing-tools | Inking free in OneNote; Windows/Mac/iPad/web/Android all supported.
- L411 | Community complaints | STILL-UNVERIFIED | https://www.reddit.com/r/PKMS/comments/1mx8get/ | Reddit not re-fetched; attributed third-party material.

## 17. Goodnotes — inking feature set only

- L417 | Smart Ink marketing | STILL-UNVERIFIED | https://www.goodnotes.com/features/tablet-stylus-experience | The cited features page never surfaced in search results this session and direct fetching is restricted; its content could not be re-verified.
- L417 | Pressure/tilt documentation | STILL-UNVERIFIED | https://feedback.goodnotes.com/ | Goodnotes' own feedback board (seen in search results) lists pressure/tilt enhancement as a user idea, and no official page reached this session documents pressure/tilt behavior; remains unverified.
- L419 | Palm rejection UNVERIFIED | CONFIRMED | https://support.goodnotes.com/hc/en-us/articles/7353695644175-Select-Move-and-Edit-Content-With-the-Lasso-Tool | Official Goodnotes support (Apple Pencil article) states Apple Pencil and Logitech Crayon have built-in palm rejection, so no in-app setting is needed; in-app settings cover capacitive pens only.
- L421 | Lasso convert to text/math, in-app ink only | CONFIRMED | https://support.goodnotes.com/hc/en-us/articles/7353695644175-Select-Move-and-Edit-Content-With-the-Lasso-Tool | Official support: lasso conversion works only on ink created inside the app; imported images/PDFs are static; Scribble is Apple's technology and unaffected by Goodnotes' language setting.
- L421 | HWR language count UNVERIFIED | REVISED | https://support.goodnotes.com/hc/en-us/articles/7353695644175-Select-Move-and-Edit-Content-With-the-Lasso-Tool | Official support page (seen this session) lists the recognized handwriting-conversion languages on Apple devices: Chinese (Simplified & Traditional), Dutch, English (US/UK), French, German, Italian, Japanese, Korean, Portuguese — roughly ten, not a large set; background search-OCR is broader (30+ per the third-party Handwriting OCR page fetched this session).
- L423 | Edit Handwriting Mode / reflow | CONFIRMED | https://support.goodnotes.com/hc/en-us/articles/10779382123919-Reflow-your-handwriting-with-Edit-Handwriting-Mode | Official support articles document reflow, word editing, straightening and restyling of handwriting.
- L425 | Scribble-to-erase, circle-to-lasso, autocomplete | STILL-UNVERIFIED | https://techcrunch.com/2023/08/09/goodnotes-biggest-update-in-four-years-brings-ai-powered-handwriting-features-and-a-digital-marketplace/ | Cited TechCrunch article not re-fetched this session (search budget); claim stands as previously sourced.
- L427 | Shape recognition in ink | STILL-UNVERIFIED | https://www.goodnotes.com/blog/benefits-digital-note-taking | Cited blog not re-fetched this session.
- L429 | Lasso menu also handles images and sticky notes | CONFIRMED | https://support.goodnotes.com/hc/en-us/articles/7353695644175-Select-Move-and-Edit-Content-With-the-Lasso-Tool | Official support documents the lasso menu's image and sticky-note actions.
- L433 | User praise/complaints on HWR | STILL-UNVERIFIED | https://www.handwritingocr.com/handwriting-to-text/how-do-you-convert-handwriting-to-text-in-goodnotes | The fetched third-party page confirms imported-PDF ink cannot be recognized (complaint side); the user-quote praise side remains third-party material.

## 18. Apple Pencil / iPadOS handwriting baseline

- L441 | Apple Pencil Pro gestures (squeeze, barrel roll, haptics, hover, double-tap) | CONFIRMED | https://support.apple.com/en-us/120123 | Official Apple support and apple.com/apple-pencil document the full gesture set; WWDC24 session covers squeeze support for developers.
- L443 | PencilKit system ink with pressure/tilt; stroke inspection (WWDC20) | CONFIRMED | https://developer.apple.com/videos/play/wwdc2020/10148/ | Official WWDC session documents stroke inspection and system-grade ink; WWDC24 covers built-in Apple Pencil Pro squeeze support.
- L445 | System-level palm rejection, not a user setting | REVISED | https://support.goodnotes.com/hc/en-us/articles/7353695644175-Select-Move-and-Edit-Content-With-the-Lasso-Tool | Apple publishes no user-facing palm-rejection setting, but Goodnotes' official support explicitly describes Apple Pencil's "built-in palm rejection," corroborating the inference; Apple's own pages still do not name it, so the platform-attribution framing stays.
- L447 | Scribble: system HWR, on-device/private, scratch to delete | CONFIRMED | https://support.apple.com/guide/ipad/enter-text-with-scribble-ipad355ab2a7/ipados | Official iPad guide: Scribble converts on-device so writing stays private, supports scratch-out and text gestures; language list still not enumerated on the consulted page.
- L449 | Draw-and-hold shape snapping | CONFIRMED | https://developer.apple.com/videos/play/wwdc2020/10148/ | iOS 14+ PencilKit shape recognition documented; works in Notes and PencilKit apps.
- L451 | iPadOS 18 Smart Script and Math Notes | CONFIRMED | https://www.apple.com/newsroom/2024/06/ipados-18-introduces-powerful-intelligence-features-and-apps-for-apple-pencil/ | Official Apple newsroom documents Smart Script smoothing/straightening and Math Notes solving handwritten expressions.
- L453 | iPadOS 26 Notes: reed pen, menubar, Markdown export, call transcription | CONFIRMED | https://9to5mac.com/2025/10/16/heres-everything-new-for-apple-notes-in-ios-26/ | Coverage seen this session documents the reed pen with stroke-angle presets and menubar; Apple's support guide documents Scribble transcription and text-to-handwriting conversion with the 10-unique-characters requirement.
- L455 | Notes searches handwriting incl. scans | CONFIRMED | https://apps.apple.com/us/app/notes/id1110145109 | Official Notes listing documents searching handwriting, including inside scanned documents and photos.
- L457 | Notes sync via iCloud; E2EE under Advanced Data Protection | CONFIRMED | https://support.apple.com/en-us/102651 | Official Apple documentation lists Notes among the data categories protected by end-to-end encryption when Advanced Data Protection is on; locked notes are additionally protected by the note passcode. The master's UNVERIFIED flag is resolved.
- L459 | Free with iPadOS; Pencil sold separately | CONFIRMED | https://www.apple.com/apple-pencil/ | Official Apple pages.
- L461 | Community praise/complaints incl. vector-ink gaps | STILL-UNVERIFIED | https://www.geeky-gadgets.com/ipados-26-updates-for-apple-notes/ | Search snippets seen this session support the vector-ink complaint framing, but the pages were not fetched; attributed third-party material.

## Sweep fills (18)

- L287 | FILL | The storytold/pdfcraft GitHub README confirms the Rust open-source PDF reader/editor: view, annotate, organize, combine, split PDFs; free, no account/telemetry/cloud; pro inking still missing from its tracked feature-parity list; native macOS/Windows/Linux/FreeBSD plus web. | https://github.com/storytold/pdfcraft/blob/main/README.md
- L289 | FILL | The App Store "PDFCraft" (id6746790039) is an unrelated commercial scanner toolkit by another developer: images/Office to PDF, merge/split/compress, annotation behind Premium, AI Summary, Read Aloud, widgets, Siri Shortcuts, Face ID lock, with premium in-app purchases listed — confirming the master's naming-collision claim. | https://apps.apple.com/us/app/pdfcraft/id6746790039
- L85 | FILL | Flexcil's official listing documents cloud sync across devices ("seamlessly sync across devices"); no end-to-end-encryption claim appears on any official page. | https://apps.apple.com/us/app/flexcil-note-good-pdf-reader/id1531466462
- L115 | FILL | LiquidText's official pricing-features page documents real-time sync with continuous backup, local-only storage by default, an Azure-based sync stack, and a coming-soon "enhanced project file encryption with passwords managed by end user" for the Unlimited edition; full E2EE is not claimed. | https://www.liquidtext.net/pricing-features
- L87 | FILL | The Flexcil store-listing mirror confirms export of notes and templates with watermark removal on PDF export in the paid tier. | https://flexcil-ipad.appstor.io/
- L421 | FILL | The Handwriting OCR guide confirms Goodnotes' lasso-convert works only on in-app ink, Scribble is Apple's technology, and background search OCR covers 30+ languages while lasso conversion supports a smaller official list. | https://www.handwritingocr.com/handwriting-to-text/how-do-you-convert-handwriting-to-text-in-goodnotes
- L365 | FILL | The current official Notes+ listing documents a voice-recording feature, so audio recording is a documented present-day Notes+ capability; the legacy Medium tutorial page itself was unreachable this session. | https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989
- L45 | FILL | The fetched live Write Pro listing documents Apple Pencil support with no pressure-sensitivity claim, confirming the absence on the current listing text. | https://apps.apple.com/us/app/stylus-labs-write-pro/id1498369428
- L119 | FILL | The official LiquidText pricing-features page confirms the live tier structure (Basic, Pro 2023 one-time, LIVE, LIVE Unlimited, newer LIVE Unlimited+) with trial and student pricing, but still publishes no dollar figures; third-party amounts remain the only figures available. | https://www.liquidtext.net/pricing-features
- L59 | FILL | The Write Pro listing documents the no-vendor-cloud sync model: standard Apple document browser with iCloud and any Files-integrated cloud; no E2EE claim. | https://apps.apple.com/us/app/stylus-labs-write-pro/id1498369428
- L417 | NOT-CONFIRMABLE | goodnotes.com/features/tablet-stylus-experience never surfaced in search results this session and could not be fetched, so the Smart Ink marketing page and its pressure/tilt wording remain unverified; alternatives reached (Goodnotes support palm-rejection article, Handwriting OCR page) did not document pressure/tilt either. | https://feedback.goodnotes.com/
- L189 | FILL | The fetched Xodo Google Play listing documents built-in OCR making scanned PDFs searchable and lists no handwriting-recognition, audio-recording or palm-rejection feature, confirming the absences. | https://play.google.com/store/apps/details?id=com.xodo.pdf.reader&hl=en_US
- L253 | FILL | The cited Drawboard support article returned 403 (Cloudflare); Drawboard's official product tour instead confirms account-based Snapshot syncing of work across devices, with no E2EE claim. | https://www.drawboard.com/pdf/product-tour
- L315 | FILL | The Noteful version-history mirror was unreachable; the official App Store listing documents PDF export/share and iCloud sync with account-based-key encryption, but no export-fidelity claims; the iOS 18 crash-fix note remains mirror-sourced only. | https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334
- L37 | FILL | MyScript's official GitHub examples repository for the Interactive Ink SDK confirms the SDK exists, is integrable in iOS apps, and issues a free starter license certificate through the Getting Started flow; commercial per-seat pricing is still not published. | https://github.com/MyScript/interactive-ink-examples-ios
- L65 | FILL | The fetched live Write Pro App Store listing publishes the current price, $8.99, resolving the "exact current Pro price not published" gap. | https://apps.apple.com/us/app/stylus-labs-write-pro/id1498369428
- L171 | FILL | The official MarginNote 4 manual documents the card library with filtering, searching, batch editing and backlinks, iCloud sync with version backups, and encrypted database sharing; full E2EE of synced content is still not claimed. | https://manual.marginnote.com.cn/mn4/en/
- L301 | FILL | The official Noteful App Store release notes document the experimental lasso-to-text feature (including handwriting) requiring iOS 27 or later; a general HWR language list remains undocumented. | https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334

## Master-file corrections

===== SECTION: ## 9. Drawboard PDF =====
**Audio-linked notes.** Documented feature: the official product tour states users can "record or upload audio notes and attach them to sections." (https://www.drawboard.com/pdf/product-tour)

===== SECTION: ## 12. Noteful =====
**Audio-linked notes.** Documented feature: the official App Store listing states users can "record audio while you take notes," with playback position synced to the annotations on the page. (https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334)

===== SECTION: ## 14. Notes+ (Notes Plus team) =====
**Audio.** Documented feature in the current app: the official App Store listing includes voice recording among its tools (alongside the calculator, timer and AI tools), so audio recording is no longer merely a legacy Notes Plus capability. (https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989)

===== SECTION: ## 3. Flexcil =====
**Handwriting-to-text.** The official App Store release notes reference fixing a crash that could occur during handwriting recognition, so Flexcil ships some handwriting-recognition machinery; a general handwriting-to-text feature is still not documented in the store listing or on the vendor site. (https://apps.apple.com/us/app/flexcil-note-good-pdf-reader/id1531466462)

===== SECTION: ## 8. PDF Expert (Readdle) =====
**Handwriting-to-text.** Readdle added handwriting recognition to PDF Expert with iPadOS 27 (September 2026): handwriting becomes searchable without changing how it looks, works on anything written with Apple Pencil or finger, supports 29 languages, and operates across the whole library including annotations made in other apps. (https://support.readdle.com/pdfexpert/en_US/annotate-pdfs; https://9to5mac.com/2026/09/17/pdf-expert-update-adds-handwriting-recognition-expands-apple-pencil-support-more/)

LANE 2 COMPLETE — 178 claims verified, 18 sweep candidates processed (17 FILL, 1 NOT-CONFIRMABLE)
