# R8 fact-check: corrections applied

Round R8 (2026-10-27), launched by the user: "some of the things that you have listed in the features.md like amphi being self-hosted and opensource are not true. I need you to go through and fact check everything."

Method: six parallel subagent lanes re-verified claims in FEATURES.md against primary sources (official pricing pages, app-store listings, vendor docs/blogs, GitHub/package registries). Full verdict tables with source URLs: r8-factcheck-lane-1-ipad-study.md through r8-factcheck-lane-6-htr-sync-ai-nostr.md. This file lists what was WRONG and what changed in the master files. CONFIRMED claims are not repeated here; see the lane files.

## Amphi (the user-flagged error)

The Discord thread linked https://www.useamphi.com/. That is Amphi Labs LTD's closed-source iPad study canvas (notes, documents, flashcards, AI tutors, in-app purchases). A different product shares the name: Amphi Notes (github.com/amphi2024/notes), a free open-source plain-text notebook (GPL-3.0-or-later per Snapcraft/AUR distribution listings; the LICENSE file itself was not fetched) with self-hosted sync via amphi2024/server. Earlier findings glued the open-source repo's properties onto the useamphi.com subject. Fixes: APPS-LINKS.md line 47 now separates the two products and marks useamphi.com closed-source; apps-likes-wants.md attributes the self-hosted-sync praise to Amphi Notes explicitly. The two-product split in FEATURES.md's Amphi section was judged correct by the lane; license evidence note added.

## Features / majors (lanes 1-3)

- Goodnotes 6: there is no ~$29.99/yr subscription. Essential is $11.99/yr, Pro $35.99/yr; $29.99 was the one-time "Special Edition" purchase (Apple only, listed only in the FAQ). Free tier is "up to 3 files"; AI Pass is $9.99/mo.
- Evernote: free cap is 50 notes / one notebook, not 51. The "57% of negative reviews" stat is UNVERIFIED (source not re-locatable) and is now marked as such.
- Obsidian: Sync Standard is $4/mo billed annually ($48/yr); the $96/yr figure is Sync Plus. The claim that checkout defaults to the pricier tier was dropped (unverifiable); obsidian.md's main pricing page now shows a single $4/mo plan while obsidian.md/sync still lists both. Plugin registry has roughly 9,500 entries (~9,521 as of 2026-10-27), not ~5,000; the library doubled within 2026. The April 2026 Elastic Security Labs campaign delivered the PhantomPulse RAT via malicious community plugins in shared vaults targeting finance/crypto people on LinkedIn/Telegram; it was not fake app downloads aimed at Ukraine's government/military.
- Tana: pricing is Free / Pro $20/mo early-bird ($30 regular) / Business from $35/mo on tana.inc; the older $10-18 tiers are gone.
- Logseq: issue #3457 is a 2020 Markdown hyphen bug (the FEATURES text already described it correctly; dated now). "Enable hourly backups" is community advice, not official documentation, and is marked UNVERIFIED as official guidance. DB version: announced April 2024, DB beta shipped July 13, 2026; the OG/DB split took effect April 24, 2026.
- Tolaria: ~52.6K lines of Rust plus ~53K lines of TypeScript/TSX (repo count, Oct 2026), not ~100K lines of Rust. What shipped in October 2026 was the iPhone/iPad client; the web client is an announced in-development beta with alpha CI only.
- Miro: Trustpilot ~2.3-2.4/5, not ~1.6 (no wrong figure was found in the current master files, so no edit was needed there).
- Heptabase: Pro $8.99 / Premium $17.99 / Premium+ $53.99 per month billed annually (no wrong figure found in master files).
- Muse: wound down gracefully and handed to Adam Wulf (Muse 3.0, rebranded Allume in June 2026); "death" wording corrected.
- Milanote: $9.99/mo billed annually (about $120/yr). The roadmap-poll and "no edit history" claims remain UNVERIFIED.
- AFFiNE: no E2EE claim exists in the current master files; AFFiNE itself only says CRDT sync is "naturally compatible with" E2EE and never claims AFFiNE Cloud is E2EE.
- Flexcil: free tier plus a one-time purchase, not a subscription (findings already correct). MarginNote 4: alongside the one-time tiers, Max Annual $16.99/yr and MAX monthly IAPs exist, so "no subscription" is not strictly true.
- CollaNote: no official open-source repo found anywhere (publisher Zauberberg Lab); treat as closed. No open-source claim was found in the current master files.

## OSS repos (lane 4)

- neo (hughhowey/neo): MIT per its README ("free to use, free to modify, free to share"); an earlier "free but NOT open source" reading was wrong and is corrected in FEATURES.md.
- CapsuleCraft (kostyk348/CapsuleCraft): zero-database, every note an RFC 5322 .eml file; the findings files already said this correctly. Stack is Tauri 2 + React 19 web and Rust + egui native.
- notebook-navigator: issue #274 IS the September 2025 v1.5 roadmap tracking issue (the findings files already cited it correctly); the duplicate-panes issue is #1498. The plugin has 1,072,639 downloads and the author accepts no PRs.
- xnotes-android: GitHub Releases and F-Droid ship the same signed APK; the Google Play build is a separate channel with a signing conflict (issue #166). Corrected in FEATURES.md.
- diktafon: speech-to-text (Whisper transcription + Qwen summarization), not TTS; master files already described it correctly.
- ConvertOneNote2MarkDown: issues #102 (Aug 2021) and #123 (Feb 2022) are old; only #197 and #200 are from October 2026. The master files do not date them, so no edit was needed.
- OfficeIMO: only v3.5.0 (Tool) and v3.4.4 (Word) were verifiable; the "current v3.5.2" claim was not confirmed and issue #3171 (~Oct 23, 2026) was.
- Meridian-Notes: MIT rests on an R6 search snapshot of the repo's resources section; marked UNVERIFIED in R8 (APPS-LINKS.md line 303 annotated).
- e-journal: no matching repo found (only an unrelated academic platform). Strata: MIT/439-issues not re-verifiable in R8; stands as originally recorded with source citations.

## Integrations (lane 5)

- Stirling PDF: ~94-95k stars (not 93k). Its LICENSE file's proprietary carve-outs (app/proprietary, app/saas, engine/, several frontend/src/editor/ subdirs) verified.
- GIMP: GPLv3+ well before 3.0; 3.0 itself shipped 16 March 2025. Corrected in FEATURES.md.
- Godot: LibGodot was mainlined via PR #110863 (merged; follow-ups #123552/#123717 cite it as merged). Corrected in FEATURES.md.
- lowkey.gg: the dispute was the March 2021 GPL-violation accusation (shipping OBS code without source), not a forking controversy.

## HTR / sync / AI / Nostr (lane 6)

- NIP-77 is "Negentropy Syncing"; the master files already described it as negentropy set-reconciliation, which is accurate. Negative query filters (neg: prefix) are a NIP-50 extension.
- nostr crate: 0.45.5, about 446K downloads/month (not 385K). Corrected in FEATURES.md.
- Relay counts (471 public / 343 offline): UNVERIFIED, left as sourced-but-unchecked.
- whisper.cpp Android: documented as slower than realtime; the "~5x" ratio is UNVERIFIED and the wording now says so.
- TrOCR IAM CER figures (2.89/3.42/4.22) match Microsoft's unilm README; okraPDF's 3.68% TrOCR / 49.58% Tesseract figures are okraPDF's own August 2026 vendor benchmark (source note retained).
- philips/supernote-typescript active as of Aug 2026; secsync (Apache-2.0) dormant since 2024-06-04; diamond-types ISC; Qwen3-Embedding-0.6B Apache-2.0; sqlite-vec MIT+Apache-2.0; Piper GPL-3.0; Llama/Gemma licenses are not OSI-approved.
