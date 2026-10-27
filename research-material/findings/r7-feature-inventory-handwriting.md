# R7 Feature Inventory — Handwriting / Study / PDF apps

Lane: handwriting & study batch (r7). Rules followed: primary sources cited per claim group; anything not confirmable from a primary source is marked **UNVERIFIED**. No machine names, IPs or credentials. Compiled 2026-10-27.

A recurring evidence note: most vendors document feature lists on marketing/store pages rather than spec sheets, and almost none document ink-engine internals or E2EE. Where a claim rests only on a store listing or a third-party review, that is flagged.

---

## 1. MyScript Notes (formerly Nebo)

Renamed from Nebo to MyScript Notes on iOS and Android; Windows keeps the name Nebo. Lifetime purchases remain valid with no extra charge for existing features; notes stay compatible and synced across platforms. (https://www.myscript.com/notes/; https://help.myscript.com/notes/frequently-asked-questions/)

**Ink engine / pressure & tilt.** Built on MyScript "Interactive Ink" technology; active-pen support, real-time stroke processing, editable interactive ink. (https://help.myscript.com/notes/) Pressure/tilt specifics are not published in the docs consulted — **UNVERIFIED**.

**Palm rejection.** Documented as stylus-precision input with finger/palm not disturbing the page (stated generally on the getting-started help page, which says the app "supports active pens for precise input"); explicit palm-rejection settings are not documented — **UNVERIFIED**. (https://help.myscript.com/notes/)

**Handwriting-to-text.** Core capability: convert handwriting to typed text, then edit/format; double-tap a block to convert (classic Nebo interaction, documented in the user guide). Pen gestures, lasso selection, instant conversion are listed on the getting-started page. (https://help.myscript.com/notes/; https://help.myscript.com/nebo/edit-content/convert/) Language count is not stated on the pages consulted — **UNVERIFIED** (MyScript historically claims a large language set on its site).

**Shape / ink gestures.** Lasso selection, pen gestures, and conversion of handwritten shapes and math are documented (conversion page covers "handwritten text and shapes"). Recognizes handwritten superscripts and 17 added symbols (◦ ☆ ↑ ↓ ↗ ↘ ↔ ⇔ ≠ ≈ ≥ ≤ ♀ ♂ ⊕ ⊖ ∅) per the Android release notes. (https://help.myscript.com/nebo/edit-content/convert/; https://help.myscript.com/notes/versions/android/)

**Structure features.** Notebooks with fixed pages, freeform Boards ("the world's most advanced endless canvas" per the store listing), PDF import for annotation, math calculations and diagrams inline. (https://apps.apple.com/us/app/myscript-notes-ai-handwriting/id1119601770; https://www.myscript.com/notes/)

**Audio-linked notes.** Not a documented Nebo/Notes feature — **UNVERIFIED** (no audio-recording feature appears in the official help or store listing consulted).

**PDF annotation.** Import existing files as PDFs, ready to annotate. (https://apps.apple.com/us/app/myscript-notes-ai-handwriting/id1119601770)

**Study features.** AI summarization and quiz creation from notes are promoted on the product page ("create quiz from your notes"). (https://www.myscript.com/notes/)

**Sync / storage / E2EE.** Notes sync across devices (compatibility FAQ). E2EE is not claimed in the consulted docs — **UNVERIFIED**. (https://help.myscript.com/notes/frequently-asked-questions/)

**Export fidelity.** Export to "basic formats" and share converted text (per product page); specific fidelity claims not documented — **UNVERIFIED**. (https://www.myscript.com/notes/)

**Platforms.** iOS, Android, Windows (Nebo). (https://help.myscript.com/notes/)

**Pricing (iOS/Android, 2026).** Free 7-day trial with limited pages; $1.99/month or $7.99/year subscription for full access; $24.99 lifetime one-time for full access (per Paperlike's January 2026 review — third party; the vendor's own pricing page says plans are sold only via App Store/Google Play and prices vary by region). (https://paperlike.com/blogs/paperlikers-insights/myscript-notes-app-review; https://www.myscript.com/pricing/)

**Nebo / iink SDK licensing as currently published.** MyScript publishes a handwriting-recognition & interactive-ink SDK for developers/OEMs ("flexible, easy to integrate and OS-agnostic"). (https://www.myscript.com/sdk/; https://www.myscript.com/) Development starts with a free license certificate claimed through the SDK's Getting Started flow (illustrated in MyScript's own GitHub example repos). (https://github.com/MyScript/interactive-ink-examples-ios) Commercial licensing terms are set out in MyScript's SDK native-libraries licensing document (PDF, v1, 2017). (https://cdn.myscript.com/legal/licensing-for-the-use-of-interactive-ink-sdk-native-libraries-v1.pdf) For education, licenses are sold in packs starting at 100 licenses at €12 each. (https://www.myscript.com/education/) Current per-seat/per-OEM commercial pricing is not published on the public pages consulted — **UNVERIFIED**.

**UX note.** Top praise: best-in-class handwriting recognition and realistic ink ("Excellent handwriting recognition… The app is perfect" — user quotes on the official page; https://www.myscript.com/notes/). Top complaints: the Nebo→MyScript Notes transition introduced subscription/new-purchase plans with what users describe as roughly a 3x price increase for one-time purchase, and confusion about what lifetime covers; see r/NeboApp threads "Nebo has transitioned to MyScript Notes for students" (https://www.reddit.com/r/NeboApp/comments/1n9razt/) and "Anyone regret getting the Nebo lifetime subscription?" (https://www.reddit.com/r/NeboApp/comments/1p68msf/).

---

## 2. Write by Styluslabs

**Ink engine / pressure & tilt.** Custom vector ink on an SVG native document format; Apple Pencil support in Write Pro ("STANDARD NOTE-TAKING AND DRAWING TOOLS — Apple Pencil support"). Explicit pressure-sensitivity claims are not made in the official material consulted — **UNVERIFIED**. R9 camoufox re-scrape of the live App Store listing confirms the listing itself makes no pressure-sensitivity claim either. (https://www.styluslabs.com/; https://spark.mwm.ai/en/apps/stylus-labs-write-pro/1498369428 — store-listing mirror; original listing: https://apps.apple.com/us/app/stylus-labs-write-pro/id1498369428)

**Palm rejection.** Not documented in official material — **UNVERIFIED**.

**Handwriting-to-text.** No handwriting recognition feature is documented in official material — effectively none. **UNVERIFIED** (absence documented only by omission from the official feature lists). (https://www.styluslabs.com/)

**Shape / ink gestures.** Intelligent tools to select, erase, and move writing; reflow handwritten text with the insert-space tool; move strokes and insert space in multiples of the page ruling; cut/copy/paste selection; unlimited undo/redo. (https://play.google.com/store/apps/details?id=com.styluslabs.write; https://www.styluslabs.com/)

**Distinctive editing.** Handwritten links to bookmarks and websites; bookmarks labeled with handwriting; work on two documents with split view; save frequently used content as clippings; column detection protects sketches when editing text; pages can grow automatically near the edge. (https://www.styluslabs.com/; https://play.google.com/store/apps/details?id=com.styluslabs.write)

**Audio-linked notes.** Not documented — none. **UNVERIFIED** (absence).

**PDF annotation.** Export to PDF is documented; annotating PDFs is not documented as a feature — **UNVERIFIED**. (https://styluslabs.com/faq)

**Sync / storage / E2EE.** No vendor cloud: standard Apple document browser, iCloud and any Files-integrated cloud, Files app integration on iOS. E2EE not claimed — **UNVERIFIED**. (https://apps.apple.com/us/app/stylus-labs-write/id1580794413)

**Export fidelity.** Open standard SVG native format, openable in other vector apps and web browsers; export to PDF (add extension in Save As; .html/.htm not supported on iOS). (https://apps.apple.com/us/app/stylus-labs-write/id1580794413; https://styluslabs.com/faq)

**Platforms & openness.** Windows, macOS, Linux, Android, iOS; source published on GitHub. (https://github.com/styluslabs/Write; https://www.styluslabs.com/download/)

**Pricing.** Free "Write" plus paid "Write Pro" one-time purchase (Pro listing: https://apps.apple.com/us/app/stylus-labs-write-pro/id1498369428). Exact current Pro price not published on official pages consulted — **UNVERIFIED**.

**UX note.** Praise (third-party, flagged): unusual editing tools for handwritten documents, reflow and selection are standout. Complaints: no handwriting-to-text/OCR, and no built-in sync. (https://appmus.com/software/stylus-labs-write — third party; **UNVERIFIED** as "top complaint")

---

## 3. Flexcil

**Ink engine / pressure & tilt.** "Beautiful handwriting with vector-based pen engine" (EdTech Impact profile). Pressure specifics not documented — **UNVERIFIED**. (https://edtechimpact.com/products/flexcil/ — third-party profile)

**Palm rejection.** Store listing claims "Guaranteed ZERO touch malfunctions" with Apple Pencil, support for Apple Pencil 2nd gen double-tap. (https://apps.apple.com/us/app/flexcil-note-good-pdf-reader/id1531466462)

**Handwriting-to-text.** Not documented as a core feature in the consulted official material — **UNVERIFIED**.

**Shape / ink gestures.** Signature gesture UX: highlight by pen gestures and capture text/images onto study notes by pen gestures; lasso and straight-line drawing; extended gesture menu for search/bookmark. (https://play.google.com/store/apps/details?id=com.flexcil.flexcilnote; https://flexcil-ipad.appstor.io/ — store-listing mirror)

**Audio-linked notes.** Record audio while reading; recorded audio syncs with annotations and shows what you annotated during playback. (https://support.flexcil.com/hc/en-us/articles/6696626355609-Beginner-s-Guide)

**PDF annotation + study workflow.** View PDFs and take notes simultaneously on the same screen; automatic hyperlinks between captured text/images and the original source; masking pen; dictionary lookup and keyword search; share notes across PDFs; unlimited folders/categories/pages, notes covers and templates (add-ons). (https://support.flexcil.com/hc/en-us/articles/6696626355609-Beginner-s-Guide; https://www.flexcil.com/; https://flexcil-ipad.appstor.io/)

**Sync / storage.** Cloud sync across devices (store listing, 2025 update). E2EE not claimed — **UNVERIFIED**. (https://apps.apple.com/us/app/flexcil-note-good-pdf-reader/id1531466462)

**Export.** Exporting notes and templates; watermark removal in paid tier. **UNVERIFIED** fidelity detail. (https://flexcil-ipad.appstor.io/)

**Platforms.** iOS/iPadOS, Android, HarmonyOS. (https://updf.com/edit-pdf/flexcil/ — third party; consistent with vendor profiles)

**Pricing.** Free tier (limited to 5 folders, etc.) plus one-time "Standard/Premium" purchase; vendor FAQ: "You only need a one-time payment for permanent use," 15-day free trial, no auto-charge. Indicative prices: $9.99 iOS / $7.99 Android (r/Flexcil announcements — community, not official). (https://support.flexcil.com/hc/en-us/articles/10751768914713-Is-the-app-subscription-or-one-time-payment; https://www.flexcil.com/stories/free-vs-standard-flexcil-2/; https://www.reddit.com/r/Flexcil/)

**UX note.** Praise: the gesture capture/linking workflow between PDF and notes is repeatedly called the feature users waited for. (https://www.flexcil.com/ — vendor-selected quotes) Complaints: anxiety around the 2023 free-vs-premium split and fear of a subscription switch; restore-purchase issues on iOS. (https://www.reddit.com/r/Flexcil/comments/1639879/; https://support.flexcil.com/hc/en-us/articles/10751768914713)

---

**Handwriting-to-text.** The official App Store release notes reference fixing a crash that could occur during handwriting recognition, so Flexcil ships some handwriting-recognition machinery; a general handwriting-to-text feature is still not documented in the store listing or on the vendor site. (https://apps.apple.com/us/app/flexcil-note-good-pdf-reader/id1531466462)


## 4. LiquidText

**Concept.** Every project creates a document pane plus multiple infinite workspaces; you pull excerpts from documents onto workspaces and connect notes to source text. Patented multi-touch document manipulation gestures. (https://www.liquidtext.net/liquidtextadeeperdive; https://www.liquidtext.net/pricing-features)

**Ink engine / pressure & tilt.** Freehand writing on documents, excerpts, comments and workspace; pen/ink supported. Pressure/tilt specifics not documented — **UNVERIFIED**. (https://www.liquidtext.net/pricing-features)

**Palm rejection.** Not documented — **UNVERIFIED**.

**Handwriting-to-text.** Not documented — **UNVERIFIED** (absence from feature pages).

**Shape / gestures.** Gestural functions translated for keyboard/mouse/touchpad devices; multi-touch manipulation. (https://www.liquidtext.net/pricing-features)

**Audio-linked notes.** Not documented — **UNVERIFIED** (absence).

**PDF annotation.** Draw/highlight anywhere on document, notes, or workspace; comment on two or more sections at once; link comments to multiple documents. Imports PDF, Word, PowerPoint, web pages. Not a full PDF editor (third-party LawSites note). (https://www.liquidtext.net/features; https://www.lawnext.com/2025/04/liquidtext-innovative-annotation-tool-for-complex-documents-adds-real-time-collaboration.html)

**Study/research features.** Document analysis workflow: link notes to source text, compare across documents; marketed heavily for legal analysis. Collaboration: real-time, near-realtime co-editing (multiple users in same textbox without conflict, presence indicators, per-workspace shared/private, comments/notifications). (https://www.liquidtext.net/legal; https://apps.apple.com/us/app/liquidtext/id922765270)

**Sync / storage.** LiquidText Live cloud subscription: real-time project synchronization across devices with continuous backup. E2EE not claimed — **UNVERIFIED**. (https://www.liquidtext.net/)

**Platforms.** iPadOS, Windows 10+, macOS; touch, pen, mouse, trackpad, multi-monitor. (https://www.liquidtext.net/)

**Pricing.** Free Basic edition; one-time Pro purchase (third-party sources say $79.99–$89.99); LIVE subscription ~$8.99–$10.99/month; LIVE Unlimited ~$15.99–$18.99/month; student discount ~$3.99/month annual (third-party pricing trackers; official pricing page publishes amounts only in images — figures marked **UNVERIFIED** where they rest on third parties only). R9 camoufox scrape of the live official pricing page confirms the tier structure: Basic / Pro 2023 one-time / LIVE / LIVE Unlimited, one-week free trial on LIVE, real-time sync and backup, real-time collaboration with one colleague (LIVE), unlimited storage with upgradable collaborators and priority support (LIVE Unlimited), and student pricing offered via upgrade from inside the app. (https://www.liquidtext.net/pricing-features; https://mentalclone.com/blog/liquidtext-pricing; https://paperlike.com/blogs/paperlikers-insights/liquidtext-vs-marginnote; https://beingpaperless.com/liquidtext-5-0-syncing-backup/)

**UX note.** Praise: "wholly unlike any other PDF app" workflow; Editor's Choice from Apple and Microsoft (vendor-collected quotes). (https://www.liquidtext.net/liquidtextadeeperdive) Complaints: subscription-locked features and pricing seen as restrictive for students; Basic tier limited to a single document and no inking. (https://www.capterra.com/p/264823/Liquid-Text/ — third-party reviews, **UNVERIFIED** as vendor claims)

---

## 5. CollaNote

**Positioning.** Free note-taking app for iPad, iPhone and Mac: Apple Pencil handwriting, PDF markup, digital planners, flashcards and AI study tools on one canvas. (https://www.collanote.com/home)

**Ink engine / pressure & tilt.** Apple Pencil handwriting; engine specifics not documented — **UNVERIFIED**. (https://www.collanote.com/home)

**Palm rejection.** Not documented — **UNVERIFIED**.

**Handwriting-to-text.** Handwriting calculator: write a math problem and get step-by-step solutions. General HWR not documented — **UNVERIFIED**. (https://apps.apple.com/us/app/collanote-notes-pdf-markup/id1540956268; https://www.collanote.com/home)

**Shape / ink gestures.** Not documented in consulted material — **UNVERIFIED**.

**Audio-linked notes.** Record lectures/meetings with AI transcript; handwriting, audio and transcript sync together during playback. (https://apps.apple.com/xk/app/collanote-notes-pdf-markup/id1540956268)

**PDF annotation.** PDF markup is a headline feature. (https://www.collanote.com/home)

**Study features.** Flashcards; AI study tools; community notes curated by the CollaNote team; digital planners/templates; collaboration on shared notes. (https://www.collanote.com/home; https://apps.apple.com/us/app/collanote-notes-pdf-markup/id1540956268)

**Sync / storage.** iCloud sync and cloud backups are described by third-party reviews; E2EE not claimed — **UNVERIFIED**. (https://updf.com/annotate-pdf/collanote/ — third party)

**Platforms.** iPad, iPhone, Mac. (https://www.collanote.com/home)

**Pricing.** Free (vendor: "CollaNote is a free note-taking app"). (https://www.collanote.com/home)

**UX note.** Praise (third-party): feature depth for a free app, templates, collaboration. Complaints (third-party): users on r/collanote ask about handwriting recognition gaps. (https://www.reddit.com/r/collanote/comments/za2kl9/handwriting_recognition/)

---

## 6. MarginNote 4

**Architecture.** "One excerpt is a PDF highlight, a mind map node, and a flashcard — one capture, three places" (Card Axis). Four modules wired together (document/reader, study notebook, mind map, flashcards). (https://apps.apple.com/us/app/marginnote-4-ai-notes-mindmap/id1531657269; https://www.marginnote.com/en/index.html)

**Ink engine / pressure & tilt.** Handwriting annotation supported; engine/pressure specifics not documented — **UNVERIFIED**.

**Palm rejection.** Not documented — **UNVERIFIED**.

**Handwriting-to-text.** OCR features exist (AI OCR templates per third-party profile); classic MN3 had handwriting recognition; current HWR language support not documented — **UNVERIFIED**. (https://mwm.ai/apps/marginnote-4-ai-notes-mindmap/1531657269 — third party)

**Gestures.** Not documented in consulted material — **UNVERIFIED**.

**Audio.** Not documented in consulted material — **UNVERIFIED**.

**PDF annotation + study.** Three major modes: reading, studying, reviewing (third-party review; consistent with vendor's module structure). Study keywords, drag-and-drop notes, Wikipedia/Google/Translator lookups, clipping content from multiple documents into one mind map, focus mode with layered outline, cloze flashcards and quick review, text-to-speech support. (https://www.marginnote.com/features; https://beingpaperless.com/marginnote-4-makes-ipad-learning-incredible-pdfs-mind-maps-and-flashcards/; http://www.marblejar.net/2020/10/tutorial-of-marginnote-app-for-mind.html)

**AI features.** AI book breakdown, AI Q&A, AI flashcard generation, AI translation (third-party profile; vendor site markets "AI Notes" in the app title). (https://mwm.ai/apps/marginnote-4-ai-notes-mindmap/1531657269; https://apps.apple.com/us/app/marginnote-4-ai-notes-mindmap/id1531657269)

**Sync / storage / E2EE.** Card library with filtering/search/batch edit and backlinks across mind maps and documents (user manual). Cross-device sync and E2EE not documented — **UNVERIFIED**. (https://manual.marginnote.com.cn/mn4/en/)

**Export.** Export to OmniOutliner, MindManager, Evernote. (https://www.marginnote.com/features)

**Platforms.** iOS/iPadOS (Pro tier), macOS (Standard/Max). (https://forum.marginnote.com/t/q-a-frequently-asked-questions-about-mn4-payment-plans/9702)

**Pricing (official).** Free Basic version; Pro Lifetime $12.99 (iPhone/iPad); Max Annual $16.99/year with 1-month trial and 500 AI credits/month; Max Lifetime $51.99 (AI credits for first 3 years). (https://www.marginnote.com/en/pricing/)

**UX note.** Praise (third-party): the highlight→mindmap→flashcard pipeline for deep reading. Complaints (third-party): pricing structure called "a mess" at the MN4 launch; steep learning curve. (https://www.outlinersoftware.com/topics/viewt/10732; https://beingpaperless.com/marginnote-4-makes-ipad-learning-incredible-pdfs-mind-maps-and-flashcards/)

---

## 7. Xodo

**Ink engine / pressure & tilt.** Freehand drawing/writing on PDFs (web annotator page); "Smart pen" support on mobile store listing. Pressure specifics not documented — **UNVERIFIED**. (https://xodo.com/pdf-annotator; https://apps.apple.com/us/app/pdf-reader-editor-xodo/id805075929)

**Palm rejection.** Not documented — **UNVERIFIED**.

**Handwriting-to-text.** OCR exists for scanned documents (image-to-PDF with OCR per Google Play listing); handwriting recognition not documented — **UNVERIFIED**. (https://play.google.com/store/apps/details/Xodo_PDF_Reader_Editor?id=com.xodo.pdf.reader)

**Gestures.** Not documented — **UNVERIFIED**.

**Audio.** Not a documented feature — **UNVERIFIED** (absence).

**PDF features.** Annotate: notes, highlights, underline, freehand draw, shapes, comments; fillable form creation and signing; merge/split; convert PDF to Word/Excel/PowerPoint; redaction; compression; scanner; annotation in Reader mode; customizable toolbar. Direct-save to files. (https://xodo.com/pdf-annotator; https://apps.apple.com/us/app/pdf-reader-editor-xodo/id805075929; https://www.drawboard.com/blog/top-pdf-annotation-apps — Drawboard's own comparison of Xodo)

**Study features.** None marketed — general document tool. **UNVERIFIED** (absence).

**Sync / storage.** Integrates with Google Drive, Dropbox, OneDrive. E2EE not claimed — **UNVERIFIED**. (https://www.capterra.com/p/210439/Xodo/)

**Platforms.** Web, Windows, macOS, Linux (desktop offline app), iOS, Android. (https://xodo.com/; https://xodo.com/pricing; https://apps.microsoft.com/detail/9wzdncrdjxp4)

**Pricing.** Official pricing page: plans "start at $4.99 per month" with free trial; third-party trackers list Pro from $9.99/month and a Document Suite around $14.99/month billed yearly. (https://xodo.com/pricing; https://www.g2.com/products/xodo/pricing; https://pdfeditify.com/blog/xodo-pricing-explained)

**UX note.** Praise: works with digital planners including clickable links; fast loading (Capterra reviewer quotes). Complaints: subscription price for small non-profits; limited advanced text editing. (https://www.capterra.com/p/210439/Xodo/pricing/; https://www.getapp.com/collaboration-software/a/xodo/)

---

## 8. PDF Expert (Readdle)

**Ink engine / pressure & tilt.** Four pen tools: the two upper pens are minimum-width 1 pt, the two lower 0.5 pt; pressure sensitivity works for the two lower pens; you can pick upper pens to use Apple Pencil without pressure. (https://apphelp.readdle.com/pdfexpert6/?pg=kb.page&id=1105; https://apphelp.readdle.com/pdfexpert6/index.php?pg=kb.page&id=1165)

**Palm rejection.** The app distinguishes Apple Pencil from finger (finger for page navigation, pencil for annotation, per Wondershare's description of documented behavior); explicit palm-rejection docs not consulted — **UNVERIFIED**. (https://pdf.wondershare.com/pdf-editor-mac/pdf-expert-apple-pencil.html — third party)

**Handwriting-to-text.** With iPadOS 27, PDF Expert recognizes handwriting and makes it searchable without changing how it looks; works on anything written with Apple Pencil or finger; supports 29 languages; works within PDFs and across the whole library, including annotations made in other apps. (https://support.readdle.com/pdfexpert/en_US/annotate-pdfs; https://9to5mac.com/2026/09/17/pdf-expert-update-adds-handwriting-recognition-expands-apple-pencil-support-more/)

**Gestures.** Apple Pencil Pro squeeze opens annotation tools/settings instantly (store listing July 2026). Lasso/scratch-out gestures not documented — **UNVERIFIED**. (https://apps.apple.com/us/app/pdf-expert-editor-reader/id743974925)

**Audio.** Not a documented feature — **UNVERIFIED** (absence).

**PDF features.** Annotate (highlights, notes, pens, markup), edit text/images/links, fill and sign, OCR, merge/split, export annotations only, flatten, drawings saved automatically. (https://support.readdle.com/pdfexpert/en_US/annotate-pdfs/getting-started-with-pdf-expert; https://pdfexpert.com/how-to-draw-on-pdf)

**Study features.** None marketed — **UNVERIFIED** (absence).

**Sync / storage.** Readdle ecosystem (Documents/Spark/Scanner Pro); cross-platform license under one account; Mac OCR. E2EE not claimed — **UNVERIFIED**. (https://pdfexpert.com/; https://support.readdle.com/pdfexpert/en_US/billing-subscription)

**Platforms.** iPhone, iPad, Mac. (https://pdfexpert.com/)

**Pricing.** Free download with annotation/reading; Premium subscription $79.99/year (2022 launch price for cross-platform), lifetime license $199.99, 30% education discount on annual. (https://pdfexpert.com/blog/pdf-expert3; https://thesweetbits.com/tools/readdle-pdf-expert/ — third party; https://pdfexpert.com/pricing)

**UX note.** Praise: annotation polish with Apple Pencil, "puts Adobe Acrobat to shame" (vendor's own tagline). (https://pdfexpert.com/pricing) Complaints: shift from perpetual license to subscription upset PDF Expert 2 owners despite 50%-off-first-year bridge; general subscription fatigue. (https://support.readdle.com/pdfexpert/en_US/billing-subscription/the-pdf-expert-billing-faq; https://www.macstories.net/news/pdf-expert-moves-to-annual-subscription-business-model/)

---

**Handwriting-to-text.** Readdle added handwriting recognition to PDF Expert with iPadOS 27 (September 2026): handwriting becomes searchable without changing how it looks, works on anything written with Apple Pencil or finger, supports 29 languages, and operates across the whole library including annotations made in other apps. (https://support.readdle.com/pdfexpert/en_US/annotate-pdfs; https://9to5mac.com/2026/09/17/pdf-expert-update-adds-handwriting-recognition-expands-apple-pencil-support-more/)


## 9. Drawboard PDF

**Ink engine / pressure & tilt.** "Write and draw with top-tier pressure sensitive ink for every type of stylus… Surface Pen or Apple Pencil, pixel-perfect precision, tilt and imperceptible lag" (product tour). Pen settings include a pressure-sensitivity toggle for active pens; pressure curves adjustable (firm pressure = thicker stroke). (https://www.drawboard.com/pdf/product-tour; https://support.drawboard.com/hc/en-us/articles/360001578856-Drawboard-PDF-Pen-and-ink-settings; https://www.drawboard.com/blog/12-drawboard-pdf-features-and-tricks-to-increase-productivity-that-you-might-not-know-about)

**Palm rejection.** Not explicitly documented in consulted pages — **UNVERIFIED**.

**Handwriting-to-text.** Not documented — **UNVERIFIED** (absence).

**Shapes / smart ink.** Advanced Ink kit (Pro): pressure-sensitive ink plus ink-to-shape smart recognition. (https://support.drawboard.com/hc/en-us/articles/6678832900751-Advanced-ink)

**Gestures.** Group Annotations for selecting/grouping markups; radial-menu tool organization. (https://www.drawboard.com/pdf/product-tour; https://braincanvas.blog/what-does-drawboard-pdf-do — third party)

**Audio.** Not documented — **UNVERIFIED** (absence).

**PDF features.** Markup with pen/highlighter/shapes; document manipulation (merge/split); layers; signatures (2 on Basic); calibration/measurements are part of the engineering positioning. (https://www.drawboard.com/pdf/pro; https://www.drawboard.com/pdf/)

**Study features.** Student pricing exists; no study-specific features marketed — **UNVERIFIED** (absence).

**Sync / storage.** Drawboard account carries subscription across devices; cloud workspace on higher tiers. E2EE not claimed — **UNVERIFIED**. (https://support.drawboard.com/hc/en-us/articles/4406251856527-Plans-Benefits)

**Platforms.** Windows (origin), iOS/iPhone, web. (https://www.drawboard.com/pdf/ios; https://marketplace.microsoft.com/en-us/product/drawboardptyltd.drawboardpdf)

**Pricing.** Free "Essentials" plan (Basic limited to 7 tools, 2 signatures); Pro via monthly/yearly subscription (third-party cites ~$4.19/month billed annually); education: one-time payment Pro, or one-time 3-year Pro Plus for eligible students. (https://www.drawboard.com/pdf/pro; https://support.drawboard.com/hc/en-us/articles/4409163761423-Understanding-our-Subscription-Model; https://www.drawboard.com/solutions/for-students; https://www.tenorshare.com/knowledge/drawboard-pdf-review.html — third party)

**UX note.** Praise: natural ink feel for engineering/construction markup. Complaints: 7-tool limit on the free tier and plan restructuring frustrated long-time users (Legacy License program acknowledges early $10 buyers). (https://www.drawboard.com/blog/acknowledging-drawboards-early-users-and-introducing-the-legacy-license)

---

**Audio-linked notes.** Documented feature: the official product tour states users can "record or upload audio notes and attach them to sections." (https://www.drawboard.com/pdf/product-tour)


## 10. Drawboard Projects (formerly Bullclip)

**Purpose.** Real-time collaborative PDF markup platform for architecture/engineering/construction: mark up, discuss and track issues on the PDF canvas. (https://www.drawboard.com/projects; https://www.drawboard.com/blog/drawboard-projects-the-next-evolution-of-bullclip)

**Ink / pressure.** Inherits Drawboard ink tools ("best-in-class ink tools" per transition announcement). Pressure/tilt specifics not published separately — **UNVERIFIED**. (https://www.drawboard.com/blog/drawboard-projects-the-next-evolution-of-bullclip)

**Collaboration features.** Real-time markup across a team; assignable issues pinned to drawings; version control; layer management; Guest Access for external reviewers; Activity Feeds; Microsoft Teams integration; browser + Windows + iOS clients; cloud document management. (https://www.drawboard.com/projects/tour; https://alternativeto.net/software/bullclip/about/; https://www.capterra.com/p/162608/Bullclip/)

**Study features.** None — team design-review tool. **UNVERIFIED** (absence).

**Sync / storage.** Cloud-based, real-time. E2EE not claimed — **UNVERIFIED**.

**Platforms.** Windows, iOS, web. (https://alternativeto.net/software/bullclip/about/; https://www.drawboard.com/projects)

**Pricing.** Per-team/seat subscription; public per-seat prices not published on consulted pages — **UNVERIFIED**. (https://www.drawboard.com/projects)

**UX note.** Praise: intuitive markup + real-time collaboration + version control for construction document review. (https://saasrat.com/products/bullclip — third party) Complaints: not documented in consulted material — **UNVERIFIED**.

---

## 11. PDFCraft

**Disambiguation (important).** At least three unrelated products share this name: (a) an open-source PDF reader/editor written in Rust by storytold (GitHub), Apache-2.0 per AlternativeTo; (b) "PdfCraft: PDF Scanner" on the iOS App Store (converter/merger/annotator with premium tier); (c) various Android "PDF Craft" utility apps. This lane documents (a) as the notable open-source project and flags (b)/(c) as separate commercial apps.

**(a) PdfCraft (storytold, Rust, open source).** Native reader/editor: view, annotate, organize, combine, split, secure PDFs; annotations, form filling, bookmarks, layers, attachments; written from scratch in Rust; Apache-2.0, free. (https://github.com/storytold/pdfcraft; https://alternativeto.net/software/pdfcraft/about/) Handwriting/ink features: users have filed feature requests for professional pen/brush/highlight annotation tools and OCR — i.e., professional inking is not yet implemented (open issue #3131). (https://github.com/storytold/pdfcraft/issues/3131) Pressure/tilt, palm rejection, HWR, audio, study features, E2EE: not documented — **UNVERIFIED**. Platforms: Windows, macOS, Linux (+ web per Gizmodo download page). (https://gizmodo.com/download/pdfcraft)

**(b) PdfCraft: PDF Scanner (App Store, commercial).** Convert images/Office files to PDF and back, merge/split/compress/reorder, annotate & form filling (pencil icon, Premium), AI Summary, Read Aloud, widgets, Siri Shortcuts, Face ID lock. (https://apps.apple.com/in/app/pdfcraft/id6746790039) Pricing: freemium with Premium — exact price not published on consulted pages — **UNVERIFIED**.

**UX note.** (a) Praise: speed and native performance; complaints: young project, missing pro annotation features (issue tracker is the evidence). (b)/(c): no reliable review base found in consulted sources — **UNVERIFIED**.

---

## 12. Noteful

**Ink engine.** Custom-built "InfiniteStroke" engine that captures and converts strokes into high-resolution vector ink; Apple Pencil native support; "natural, fluid and precise handwriting." (https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334)

**Palm rejection.** Not documented — **UNVERIFIED**.

**Handwriting-to-text.** Experimental feature converting lasso selections (including handwriting) to text, requires iOS 27 or later (version history). General HWR languages not documented — **UNVERIFIED**. (https://noteful-note-taking-on-pdf-ios.soft112.com/ — version-history mirror of official release notes)

**Gestures.** Lasso selection; pages can be cropped and expanded (third-party review). (https://beingpaperless.com/about-noteful-the-handwriting-app-you-should-try/ — third party)

**Audio-linked notes.** Not documented in consulted material — **UNVERIFIED**.

**PDF annotation.** Import PDFs and MS Office documents into a notebook; PDF markup is a headline use. (https://noteful-note-taking-on-pdf.en.softonic.com/iphone — listing mirror; https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334)

**Study features.** Layers; multiple paper templates, including whole-PDF documents saved as page templates (rare); #tag and #nested/tag organization; document outlines; "more flexible than folders" positioning; tags anywhere in notebooks. (https://beingpaperless.com/noteful-complete-review-2022/ — third party; https://noteful-note-taking-on-pdf.en.softonic.com/iphone; https://www.getnoteful.com/)

**Zoom writing.** Zoom range up to ~20,000% with zoom lock; right-to-left handwriting supported. (https://beingpaperless.com/about-noteful-the-handwriting-app-you-should-try/ — third party)

**Sync / storage / E2EE.** Not documented in consulted material — **UNVERIFIED**.

**Export fidelity.** Export to PDF; an iOS 18 export crash was fixed per version history — fidelity claims not documented — **UNVERIFIED**. (https://noteful-note-taking-on-pdf-ios.soft112.com/)

**Platforms.** iPad, iPhone, Mac (App Store + Mac listing). (https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334?platform=mac)

**Pricing.** One-time purchase, ~$5 circa 2024 per a user/developer review (Paul Wintz, August 2026) — current official price not published on consulted pages — **UNVERIFIED**. (https://paulwintz.com/useful-software/noteful)

**UX note.** Praise (third-party): writing feel, whole-PDF page templates, cropping/expanding pages. Complaints (third-party, older): no handwriting search and no folders at the time of the 2021 review; tagging has since been added. (https://www.tapsmart.com/apps/noteful-review/)

---

**Audio-linked notes.** Documented feature: the official App Store listing states users can "record audio while you take notes," with playback position synced to the annotations on the page. (https://apps.apple.com/us/app/noteful-notes-pdf-markup/id1587904334)


## 13. Freenotes

**Positioning.** AI-driven digital notepad: realistic handwriting feel, PDF annotation, infinite canvas, flashcards, AI summaries. (https://freenotes-note-taking.updatestar.com/ — listing aggregator; store listing: https://apps.apple.com/us/app/freenotes-ai-notes-taking/id6464237904)

**Ink engine.** "Realistic handwriting" claimed; engine specifics not documented — **UNVERIFIED**.

**Palm rejection.** Not documented — **UNVERIFIED**.

**Handwriting-to-text.** Lasso circle → tap → "Handwriting to Text" (Lifehacker walkthrough). Plus a signature feature: "handwriting beautification" that converts handwriting into styled fonts (cute/elegant/playful), with Turkish recognition added and local font import; Font Hub fonts sync to language lists. (https://lifehacker.com/tech/freenotes-free-note-taking-app-review — third party; https://apps.apple.com/us/app/freenotes-ai-notes-taking/id6464237904 — release notes)

**Gestures.** Lasso-based selection/conversion as above.

**Audio.** Not documented in consulted material — **UNVERIFIED**.

**PDF annotation.** Interactive PDF annotation for large files; outlines preserved when exporting to PDF so exported outlines jump to pages. (https://play.google.com/store/apps/details?id=ai.note.notepad.memo.journal.freenote; https://apps.apple.com/us/app/freenotes-ai-notes-taking/id6464237904)

**Study features.** Educational templates; notebooks with varied page sizes, portrait/landscape; flashcards; AI summaries; split screen and picture-in-picture. (https://beingpaperless.com/freenotes-for-the-ipad-complete-review/ — third party; https://www.scribd.com/document/859273238/Welcome-to-Freenotes — official feature PDF mirrored on Scribd)

**Sync / storage / E2EE.** Not documented in consulted material — **UNVERIFIED**.

**Platforms.** iOS/iPadOS, Android (Google Play). (https://apps.apple.com/us/app/freenotes-ai-notes-taking/id6464237904; https://play.google.com/store/apps/details?id=ai.note.notepad.memo.journal.freenote)

**Pricing.** "Used to be free": free core with premium features now (third-party). Current tiers not published on consulted pages — **UNVERIFIED**. (https://medium.com/@paperlessx/about-freenotes-the-handwriting-note-taking-app-that-used-to-be-free-4b303e5b3f8c — third party)

**UX note.** Praise (third-party): great free/cheap option for students; handwriting beautification. Complaints (third-party): HWR at launch was limited (users requested plain handwriting-to-text; September 2024 thread). (https://www.reddit.com/r/freenotes/comments/1f8ylth/feature_request_handwriting_to_text/)

---

## 14. Notes+ (Notes Plus team)

**Identity.** Newer "Notes+ : Notes for Pencil" app (App Store id1609361989) from the Notes Plus lineage (older "Notes Plus" iPad app: handwriting, typing, audio recording, document annotation, HWR). (https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989; https://medium.com/notesplusapp/notes-plus-tutorials-9e674dfdee19; https://new.notesplusapp.com/)

**Ink engine.** Adjustable writing stabilization; automatic handwriting refinement (release notes). (https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989)

**Palm rejection.** Not documented — **UNVERIFIED**.

**Handwriting-to-text.** Legacy Notes Plus offered handwriting recognition as an add-on historically; current Notes+ HWR status not documented in consulted pages — **UNVERIFIED**. (https://www.iphonejd.com/iphone_jd/2012/01/review-notes-plus-take-advanced-notes-convert-handwriting-to-text.html — historical review)

**Pens/gestures.** Rich annotation pens: single line, wavy, dashed, double line, double wavy, triple lines; reed pen; customizable toolbar; floatable handwriting toolbar; crayons; alignment guides for images; sticker categories reorder. (https://beingpaperless.com/notes-review-another-cool-free-handwriting-app-for-the-ipad/ — third party; https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989 — release notes)

**Audio.** Legacy Notes Plus: audio recording during note-taking. Current Notes+ audio not documented — **UNVERIFIED**. (https://medium.com/notesplusapp/notes-plus-tutorials-9e674dfdee19)

**PDF annotation.** Document annotation in legacy; current status not documented — **UNVERIFIED**.

**Sync / storage / E2EE.** Not documented — **UNVERIFIED**.

**Platforms.** iPad (iOS). (https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989)

**Pricing.** Notes+ is free with premium elements (third-party review headline: "cool, free handwriting app"); AI-pen terms exist at notesplus.com. Exact premium pricing not published on consulted pages — **UNVERIFIED**. (https://beingpaperless.com/notes-review-another-cool-free-handwriting-app-for-the-ipad/)

**UX note.** Praise (third-party): free, generous pen set, stabilization/refinement controls. Complaints: not documented in consulted material — **UNVERIFIED**.

---

**Audio.** Documented feature in the current app: the official App Store listing includes voice recording among its tools (alongside the calculator, timer and AI tools), so audio recording is no longer merely a legacy Notes Plus capability. (https://apps.apple.com/us/app/notes-notes-for-pencil/id1609361989)


## 15. University Notes

Sparse primary data. App Store listing (id6777402601, "University Notes: Study Notes App"): handwritten study notes, keyboard notes & writing, study with PDFs plus handwritten notes, review & memorize your notes; August 2026 release notes mention improved handwriting and keyboard input. (https://apps.apple.com/us/app/university-notes/id6777402601)

Everything else this lane would normally document — ink engine, pressure/tilt, palm rejection, HWR languages, gestures, audio, sync, export, pricing — is not documented in the consulted primary sources: **UNVERIFIED / not documented**. Developer identity and platform coverage beyond iOS also **UNVERIFIED**.

**UX note.** Insufficient review base found in consulted sources — **UNVERIFIED**.

---

## 16. OneNote — inking feature set only

(Another lane covers OneNote overall; this section covers ink only.)

**Ink engine / pens.** Draw tab with pen, highlighter, and other ink tools; works with pen, finger, or mouse across Windows, iPad, Mac, Android; pressure sensitivity and tilt supported on capable devices; ruler for straight lines (Windows only in OneNote/Word/PowerPoint). (https://svsu.teamdynamix.com/TDClient/1949/Portal/KB/ArticleDet?ID=101204 — institutional summary of Microsoft features; https://support.microsoft.com/en-US/OneNote/onenote-help-and-learning/learn-more-about-drawing-tools)

**Ink gestures (Draw and Hold).** OneNote-only "Draw and Hold" gesture set: draw a scribble (loopy or zigzag stroke) over ink to erase; undo restores both ink and scribble. Configured under File > Options > Advanced > Pen. (https://support.microsoft.com/en-us/onenote/onenote-help-and-learning/ink-faster-with-gestures-for-creating-shapes-deleting-ink-and-more)

**Ink to Shape / Auto Shape.** Draw shapes with pen or finger and convert to perfect shapes; available in Word, PowerPoint, Excel and OneNote for Windows; in current OneNote the feature is named Auto Shape and lives in a consolidated shapes dropdown on the Draw tab. (https://support.microsoft.com/en-us/onenote/convert-your-ink-to-shapes-and-math-equations; https://learn.microsoft.com/en-us/answers/questions/5378199/unable-to-view-ink-to-shape-option-in-draw-section; https://techcommunity.microsoft.com/blog/microsoft365insiderblog/new-draw-tab-and-ink-tools-in-onenote-on-windows/4215558)

**Ink to Text.** Ink to Text Pen tool (Windows; Word, OneNote, PowerPoint) converts handwriting to text as you write; unavailable if the input language is not supported. Classic "convert ink to text" selection-based conversion also exists. (https://techcommunity.microsoft.com/blog/microsoft365insiderblog/introducing-the-ink-to-text-pen-tool-in-word-onenote-and-powerpoint-for-windows/4222008; https://support.microsoft.com/en-us/onenote/onenote-help-and-learning/convert-your-ink-to-text-shape-and-math-equations)

**Ink to Math / Math Assistant.** Convert handwritten equations; Math Assistant solves equations, plots graphs, and gives step-by-step solutions — a study-specific inking feature. (https://support.microsoft.com/en-us/onenote/onenote-help-and-learning/convert-your-ink-to-text-shape-and-math-equations; https://svsu.teamdynamix.com/TDClient/1949/Portal/KB/ArticleDet?ID=101204)

**Canvas.** Format Background on the Draw tab gives structure to the blank canvas (grid/lines/color); infinite-ish canvas placement of ink anywhere on the page. (https://techcommunity.microsoft.com/blog/microsoft365insiderblog/new-draw-tab-and-ink-tools-in-onenote-on-windows/4215558)

**Palm rejection.** Not documented as a named feature in consulted pages — **UNVERIFIED**.

**Audio-linked notes.** Covered by the OneNote-overall lane; not documented here.

**Pricing/platform.** Free within OneNote (Microsoft 365/free OneNote). Platforms: Windows, Mac, iPad, web, Android. (https://support.microsoft.com/en-US/OneNote/onenote-help-and-learning/learn-more-about-drawing-tools)

**UX note.** Out of scope detail; inking complaints commonly raised elsewhere (no text highlight via pen — you draw over text) are third-party observations, **UNVERIFIED** here. (https://www.reddit.com/r/PKMS/comments/1mx8get/)

---

## 17. Goodnotes — inking feature set only

**Ink engine / pressure & tilt.** "Smart Ink" marketing: straighten and align handwriting, adjust spacing, reshape paragraphs without losing your style. Pressure/tilt documentation not in consulted pages — **UNVERIFIED**. (https://www.goodnotes.com/features/tablet-stylus-experience)

**Palm rejection.** Not documented in consulted pages — **UNVERIFIED**.

**Handwriting-to-text.** Lasso-select handwriting → Convert to Text (or math). Works only on ink created inside the app; imported images/PDFs are static and neither lasso nor Scribble extracts text from them. Scribble uses Apple's handwriting technology, not Goodnotes' own; changing Goodnotes' recognition language does not change Scribble; Goodnotes maintains separate lists of HWR/search languages (list not fetched — language count **UNVERIFIED**). (https://support.goodnotes.com/hc/en-us/articles/7353695644175-Select-Move-and-Edit-Content-With-the-Lasso-Tool; https://www.handwritingocr.com/handwriting-to-text/how-do-you-convert-handwriting-to-text-in-goodnotes — third party; https://support.goodnotes.com/hc/en-us/articles/7353717663887-How-does-Scribble-work-with-Goodnotes)

**Edit Handwriting Mode.** Reflow handwritten notes, edit individual words, straighten lines, change alignment or color — treat handwriting like typed text. (https://support.goodnotes.com/hc/en-us/articles/10779441732111-Edit-your-handwriting-with-Lasso-Edit-Mode; https://support.goodnotes.com/hc/en-us/articles/10779382123919-Reflow-your-handwriting-with-Edit-Handwriting-Mode)

**Gestures.** GoodNotes 6 added "scribble to erase" and "circle to lasso" gestures; experimental word autocomplete for English handwriting after 3 characters. (https://techcrunch.com/2023/08/09/goodnotes-biggest-update-in-four-years-brings-ai-powered-handwriting-features-and-a-digital-marketplace/)

**Shapes.** Shape recognition in ink (perfect shapes; benefit-blog description). (https://www.goodnotes.com/blog/benefits-digital-note-taking)

**Audio / PDF / study.** Out of this lane's ink scope except: lasso menu also handles images (share/save/crop) and sticky notes (edit text, author, resolve thread). (https://support.goodnotes.com/hc/en-us/articles/7353695644175-Select-Move-and-Edit-Content-With-the-Lasso-Tool)

**Pricing.** Covered by the Goodnotes-overall lane.

**UX note.** Praise: HWR accuracy in lasso conversion ("does an amazing job even with my sloppy penmanship" — user post, third party). (https://www.lemon8-app.com/@sheishaute/7520756520137638455) Complaints: can't recognize handwriting inside imported PDFs/images. (https://www.handwritingocr.com/handwriting-to-text/how-do-you-convert-handwriting-to-text-in-goodnotes)

---

## 18. Apple Pencil / iPadOS handwriting baseline

(Every handwriting app is measured against this, so it is inventoried in full.)

**Hardware gestures & sensors (Apple Pencil Pro).** Squeeze (sensor in barrel; opens tool palettes/context menus, app-configurable), barrel roll (gyroscope rotation for shaped pen/brush tools), haptic feedback (light pulse on squeeze/double-tap), hover preview (display-side feature on M2+ iPad Pro: virtual shadow/tool preview), double-tap to switch tools, Find My. (https://support.apple.com/en-us/120123; https://www.apple.com/apple-pencil/; https://www.cnet.com/tech/computing/apple-releases-pencil-pro-with-haptic-feedback-and-new-gestures/)

**PencilKit (developer framework).** System-grade ink capture with pressure/tilt; opaque drawing model; WWDC20 added stroke inspection so apps can read strokes, inks, paths and points; PencilKit-based custom tools inherit iOS 14+ shape recognition; WWDC24 documented deep built-in support for Apple Pencil Pro squeeze with no additional code. (https://developer.apple.com/videos/play/wwdc2020/10148/; https://ios.gadgethacks.com/how-to/make-perfect-shapes-notes-drawings-annotations-with-ios-14s-new-shape-recognition-tool-0337673/; https://developer.apple.com/videos/play/wwdc2024/10214/)

**Palm rejection.** Handled at system level for Apple Pencil input; not documented as a user setting — **UNVERIFIED** (inference from platform architecture, flagged as such).

**Scribble.** System-wide handwriting-to-text in any text field without opening the keyboard; converts on-device, so writing stays private; delete by scratching out; cut/paste/insert-text gestures; available in several languages (list not enumerated on the consulted page). (https://support.apple.com/guide/ipad/enter-text-with-scribble-ipad355ab2a7/ipados; https://support.apple.com/guide/ipad/do-more-with-apple-pencil-ipad89415cd5/ipados)

**Shape recognition.** Draw a shape and hold: snaps to perfect shape; works in Notes and in PencilKit-based third-party tools. (https://www.creativebloq.com/how-to/handwriting-on-the-iPad — how-to consistent with Apple docs; https://ios.gadgethacks.com/how-to/make-perfect-shapes-notes-drawings-annotations-with-ios-14s-new-shape-recognition-tool-0337673/)

**Apple Notes handwriting features, iPadOS 18 (2024).** Smart Script: smooths and straightens handwriting in real time while keeping the user's personal style; lets you paste typed text as handwriting; edit and organize handwritten notes with the pencil. Math Notes: type or write expressions and see them solved instantly in your own handwriting; variables; graphs from equations; part of Calculator and Notes. (https://www.apple.com/newsroom/2024/06/ipados-18-introduces-powerful-intelligence-features-and-apps-for-apple-pencil/; https://9to5mac.com/2024/07/17/ipados-18-smart-script-math-notes-interview/; https://www.macstories.net/stories/ipados-18s-smart-script-a-promising-start-but-dont-toss-your-keyboard-out-yet/)

**Apple Notes handwriting features, iPadOS 26 (2025).** Notes adds a reed pen (calligraphy) tool with stroke-angle presets in the markup palette; menubar; Markdown export; call transcription. Support guide documents Scribble transcription as you write, and converting a typed text object to handwriting (requires previously saved notes with at least 10 unique lowercase characters in your handwriting). (https://9to5mac.com/2025/10/16/heres-everything-new-for-apple-notes-in-ios-26/; https://appleinsider.com/articles/25/06/11/markdown-and-menu-bars-how-apple-notes-on-ipados-26-has-matured; https://support.apple.com/guide/ipad/add-drawings-and-handwriting-ipada87a6078/ipados)

**Search.** Notes searches handwriting, including inside scanned documents/photos. (https://apps.apple.com/us/app/notes/id1110145109 — official listing)

**Sync / E2EE.** Notes syncs via iCloud; end-to-end encryption of Notes is available under Apple's Advanced Data Protection — not verified in this lane's sources: **UNVERIFIED** (point to Apple Platform Security documentation for confirmation).

**Pricing.** Included free with iPadOS; Apple Pencil hardware sold separately. (https://www.apple.com/apple-pencil/)

**UX note.** Praise (community): iPadOS 26 Notes updates led users to argue paid note apps are no longer needed. (https://www.reddit.com/r/AppleNotesGang/comments/1l7qim9/) Complaints: critical gaps persist such as vector ink support and flexible table editing; handwriting spellcheck underlines annoy users. (https://www.geeky-gadgets.com/ipados-26-updates-for-apple-notes/; https://www.reddit.com/r/AppleNotesGang/comments/1l7qim9/)

---

## Cross-cutting observations for the master features doc

1. Vendors systematically under-document palm rejection and pressure/tilt; the best-documented ink engines in this batch are Drawboard PDF (explicit pressure settings + Advanced Ink), PDF Expert (four-pen pressure scheme), Noteful (named engine: InfiniteStroke), and Apple (PencilKit, Smart Script).
2. Handwriting-to-text splits into three models: SDK-based conversion of stored ink (MyScript, Goodnotes, Freenotes, legacy Notes Plus), system-level live conversion (Scribble, OneNote Ink to Text Pen), and post-hoc search-only recognition without conversion (PDF Expert's iOS 27 feature, Apple Notes search).
3. Only Apple and OneNote document math-specific inking (Math Notes; Ink to Math/Math Assistant); CollaNote's step-by-step handwritten math is the closest third-party equivalent found.
4. E2EE is claimed by none of the third-party apps in this batch's consulted docs; Apple Notes E2EE rests on Advanced Data Protection (unverified here).
5. Pricing pressure is the dominant complaint pattern: Nebo/MyScript Notes (subscription transition), PDF Expert (perpetual→subscription), Drawboard (plan restructure), Flexcil (free→premium split). Free or one-time outliers: CollaNote, Write, Noteful (one-time), MarginNote Pro tier.
