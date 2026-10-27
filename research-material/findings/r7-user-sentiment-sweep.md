# R7 — Internet-wide user sentiment sweep: note-taking apps, 2025–2026

Scope: what note-taking app users across the public internet say they want, love, and hate in 2025–2026. Sources: Reddit (r/ObsidianMD, r/Notion, r/Evernote, r/PKMS, r/NoteTaking, r/selfhosted, r/logseq, r/GoodNotes, r/notabilityapp, r/GalaxyTab, r/samsungnotes, r/Anytype, r/heptabase), Hacker News (via search-indexed threads; direct hn.algolia.com JSON fetch was blocked from this environment, so HN coverage relies on search-indexed thread excerpts), app-community complaint threads in lieu of crawlable store pages (store pages marked UNVERIFIED where noted), and 2025–2026 roundup articles as weak secondary corroboration only.

Method note: every claim carries a URL. Quotes are under 15 words and at most one per source; everything else is paraphrase. Demands with only one independent source are listed separately and ranked low. "Independent" = different site/community, not two posts in one thread.

---

## 1. Ranked unmet demands (most-voiced first)

### D1. True offline/local-first operation and real data ownership (plain, open files) — VERY HIGH volume
What people want: notes that open and work with no connection, stored in plain markdown/open formats on their own disk, so no company can lock, price-gate, or lose their notes. How often: this is the single most recurring motive in every "switched from X" thread found in this sweep.
- r/ObsidianMD, "For those who recently switched from Notion to Obsidian" (2025-10): switchers cite cloud-storage distrust and raw speed — https://www.reddit.com/r/ObsidianMD/comments/1o18nse/for_those_who_recently_switched_from_notion_to/
- r/ObsidianMD, "Should I switch from Notion to Obsidian?" (2026-01): the clincher was moving notes out of Notion's remote servers and proprietary format into local markdown — https://www.reddit.com/r/ObsidianMD/comments/1qhborl/should_i_switch_from_notion_to_obsidian/
- r/ProductivityApps (2026-05): 3-year Notion user describes feeling like they were "renting" their own brain; notes as plain .md files survived if the vendor vanished — https://www.reddit.com/r/ProductivityApps/comments/1t2zv2n/i_spent_3_years_using_notion_for_everything/
- r/ObsidianMD, "Anyone leave Notion for Obsidian?" (2025-02): lack of offline mode and server-side data fear as departure reasons — https://www.reddit.com/r/ObsidianMD/comments/1j0jzj2/anyone_leave_notion_for_obsidian_what_do_you_like/
- r/PKMS, "Local-first opensource PKM with mobile app and full sync" (2025-07): user frustration that no app combines local-first, open-source, mobile, and full sync — https://www.reddit.com/r/PKMS/comments/1m255s8/localfirst_opensource_pkm_with_mobile_app_and/
- Hacker News, "Ask HN: What note taking app do you guys using as a developer?" (2025-03): top reply recommends Obsidian because markdown files stay readable forever — https://news.ycombinator.com/item?id=43299636
- Hacker News, "Ask HN: If I build another note taking app…" (2025): requirements list includes open source, cross-platform, sub-2-second open, and conflict-free sync — https://news.ycombinator.com/item?id=43217003
Apps failing at it and how: Notion (cloud-only, no real offline mode, proprietary database); Evernote (cloud-locked proprietary store, painful export — see Migration, M1); GoodNotes/Notability (proprietary binary formats); Logseq's move away from markdown in its DB version actively erodes its own local-file appeal (see D6). Roundup corroboration (weak source): Zapier and PCMAG 2026 roundups both position Obsidian as the local-files/power-user pick — https://zapier.com/blog/best-note-taking-apps/ , https://www.pcmag.com/picks/the-best-note-taking-apps

### D2. Honest one-time pricing; anger at subscription conversions and rug-pulls of paid "lifetime" buyers — VERY HIGH volume
What people want: buy-once options that stay valid, no features held hostage behind subscriptions, and no retroactive changes to what they already paid for.
- r/Evernote megathreads on pricing/repackaging (2025-11 and 2026-05): decade-long paying users say the latest pricing finally forces them out — https://www.reddit.com/r/Evernote/comments/1oww8h5/megathread_new_pricing_repackaging_discussion/ , https://www.reddit.com/r/Evernote/comments/1tcw1fj/megathread_pricing_repackaging_discussion/
- r/PKMS, "After 12 years canceled evernote" (2026-09): renewal jumped from under £50 to £150, cancellation followed — https://www.reddit.com/r/PKMS/comments/1wsmohv/after_12_years_canceled_evernote/
- r/Evernote, "The trigger that's moving me from Evernote" (2025-08): price path $69.99 → $129 → $242/yr; also notes exporting all notes was a pain — https://www.reddit.com/r/Evernote/comments/1n33kcl/the_trigger_thats_moving_me_from_evernote_anyone/
- r/notabilityapp, "As of 12AM Today, the Era of Bought-For-Life Notability is Over" (2025-02): long-paid users suddenly blocked from creating or editing notes without a yearly plan — https://www.reddit.com/r/notabilityapp/comments/1ive5aq/as_of_12am_today_the_era_of_boughtforlife/
- r/ipad, "Notability is quietly breaking the 'Classic Plan' and censoring complaints" (2025-09): legacy purchasers hitting editing limits, difficult restore, moderation of complaints — https://www.reddit.com/r/ipad/comments/1nm9bg5/notability_is_quietly_breaking_the_classic_plan/
- r/GoodNotes, "What happened to the one-time purchase option?" (2025-08): one-time purchase hidden or removed from upgrade screens — https://www.reddit.com/r/GoodNotes/comments/1n4yyhw/what_happened_to_the_onetime_purchase_option_for/
- r/GoodNotes, "Anyone using GoodNotes lifetime plan long-term?" (2025-10): "lifetime" means lifetime of the current version only — https://www.reddit.com/r/GoodNotes/comments/1o4g7hh/anyone_using_goodnotes_lifetime_plan_longterm/
- Hacker News thread on App Store guidelines (2025-05): GoodNotes 5 buyer complains the pricing page hides actual prices behind plan tiles — https://news.ycombinator.com/item?id=43869187
Apps failing: Evernote (repeated large increases under Bending Spoons), Notability (2021 subscription conversion with 1-year grace, free-tier monthly edit limits, 2025 classic-plan erosion), GoodNotes (subscription-first upgrade path, version-lifetime "lifetime" plan), Craft (free-tier block limit criticized in https://www.reddit.com/r/PKMS/comments/1k9iuer/anyone_know_of_an_offlinefirst_blockbased_app/ ). See also section 3.

### D3. Sync that never loses data, and works across all their devices including mobile — HIGH volume
What people want: dependable sync of notes and attachments across desktop/mobile/web, without conflicts, data loss, or "finicky" setup.
- r/PKMS (2025-06): user juggling Obsidian + Bear because no trustworthy offline-first macOS+iOS app exists, and Obsidian mobile is inadequate for them — https://www.reddit.com/r/PKMS/comments/1lb3owm/looking_for_an_offlinefirst_app_with_synced/
- r/GalaxyTab, "Notetaking apps" (2024-08): catalog of sync failures across Android handwriting apps — Notewise no sync on lifetime, Noteshelf sync "very finicky," Notein no phone app — https://www.reddit.com/r/GalaxyTab/comments/1euj4u6/notetaking_apps/
- r/NoteTaking (2023-01): Noteshelf's Google Drive sync described as useless outside Android, data in a custom binary format — https://www.reddit.com/r/NoteTaking/comments/10np1tw/android_note_taking_apps/
- r/selfhosted, "Note App that's really good" (2026-06): exhaustive wish list (Notion-like UI, web, native iOS, self-hosted, lightweight) with every candidate failing on sync or weight — https://www.reddit.com/r/selfhosted/comments/1tyt63h/note_app_thats_really_good/
- Hacker News, "Ask HN: If I build another note taking app" (2025): sync must never lose data due to conflicts — https://news.ycombinator.com/item?id=43217003
- r/samsungnotes (2026-01): sideloaded Samsung Notes on phone requires manual weekly backup because OCR/sync don't follow — https://www.reddit.com/r/samsungnotes/comments/1qfp76f/some_of_the_big_issues_of_samsung_notes/ (also https://www.reddit.com/r/GalaxyTab/comments/1d1q949/which_note_taking_apps_do_yall_use_especially_for/ )
Apps failing: Android handwriting apps generally (Squid long lacked cloud sync/backup — https://www.reddit.com/r/chromeos/comments/b7o7kp/shame_on_the_note_taking_app_squid/ ; https://www.reddit.com/r/chromeos/comments/bkghzs/alternatives_to_squid_other_than_onenote/ ), Obsidian mobile (recurring complaint, above), self-hosted stacks needing many containers or heavy RAM (Notesnook MongoDB+MinIO+8 containers, AppFlowy 2-4GB RAM — https://www.reddit.com/r/selfhosted/comments/1tyt63h/note_app_thats_really_good/ ).

### D4. Handwriting search/OCR that actually works, without disrupting the writing flow — HIGH volume (stylus users; very high within that segment)
What people want: searchable handwriting (ideally without a manual conversion step), good recognition of formulas and mixed content, and export that keeps handwriting usable.
- r/NeboApp (2025-06): wants to search handwritten notes without converting to text; notes ReMarkable forces conversion — https://www.reddit.com/r/NeboApp/comments/1l9t2xh/search_handwritten_notes_without_converting_to/
- r/samsungnotes (2026-01): pay-once version can search typed text but not handwriting — https://www.reddit.com/r/samsungnotes/comments/1qfp76f/some_of_the_big_issues_of_samsung_notes/
- r/NoteTaking (2026-08): recognition quality comparison — Nebo best at conversion to editable text, GoodNotes decent but below Nebo — https://www.reddit.com/r/NoteTaking/comments/1voucay/which_ipad_apps_have_handwriting_recognition/
- r/GalaxyTab (2024-07): "f*** samsung notes and noteshelf" over OCR gaps; Nebo OCRs handwriting in PDF export where Samsung never did — https://www.reddit.com/r/GalaxyTab/comments/1e0cqng/what_are_the_best_note_taking_apps/
- r/GalaxyTab (2020-07): physics formulas break Nebo recognition; conversion workflow described as distracting — https://www.reddit.com/r/GalaxyTab/comments/hsvaz9/apps_for_searchable_hand_writing_notes/
- r/NoteTaking wishlist post: wants Canva-like freedom plus handwriting search, which no app has — https://www.reddit.com/r/NoteTaking/ (r/NoteTaking index, "i wish there was an app…" post)
Apps failing: Samsung Notes (no handwriting search on one-time tier), Noteshelf ("bad OCR," custom binary format — https://www.reddit.com/r/GalaxyTab/comments/1euj4u6/notetaking_apps/ , https://www.reddit.com/r/NoteTaking/comments/10np1tw/android_note_taking_apps/ ), ReMarkable (forced conversion), Nebo (best recognition but bare feature set — https://www.reddit.com/r/GalaxyTab/comments/1kpv9tx/which_notes_app_do_you_recommend/ ).

### D5. Speed and responsiveness (instant open, instant search, no lag) — HIGH volume
- r/ProductivityApps (2026-05): Notion loading times were the final push; Obsidian "opens instantly, search is instant" — https://www.reddit.com/r/ProductivityApps/comments/1t2zv2n/i_spent_3_years_using_notion_for_everything/
- r/ObsidianMD (2025-10): Obsidian "just so much faster" than a huge Notion database — https://www.reddit.com/r/ObsidianMD/comments/1o18nse/for_those_who_recently_switched_from_notion_to/
- r/ObsidianMD (2025-04): offline-by-default vs Notion's "promised offline mode for 5 years," plus lag — https://www.reddit.com/r/ObsidianMD/comments/1jq53ww/why_does_obsidian_work_better_for_you_than_notion/
- r/GalaxyTab (2022-08): Squid stroke-selection and eraser friction described in detail — https://www.reddit.com/r/chromeos/comments/wx0vk3/squid_pro_vs_noteshelf_vs_nebo_vs/
- r/capacitiesapp switch story (2024-09): left Logseq "too damn slow and buggy" — https://www.reddit.com/r/capacitiesapp/comments/1fhdhd7/why_i_switched_from_heptabase_tana_logseq_to/
- Hacker News (2019 classic but still cited): wanted lightweight, always-open, keyboard-invoked notes — https://news.ycombinator.com/item?id=18845892
Apps failing: Notion (loading spinners on large databases), Logseq (performance), OneNote (search at scale per HN dev thread — https://news.ycombinator.com/item?id=43299636 ).

### D6. Vendor stability and honest communication (Logseq's stall as the cautionary tale) — MEDIUM-HIGH volume
- r/logseq, "Logseq is dead? No updates since Apr 23, 2024" (2025-04): community alarm at a year without releases — https://www.reddit.com/r/logseq/comments/1jtzhiy/logseq_is_dead_no_updates_since_apr_23_2024/
- r/logseq, "Why do you still stick with Logseq?" (2025-05): migration to Obsidian after a year of stalled development and "abysmal" communication — https://www.reddit.com/r/logseq/comments/1kwju84/why_do_you_still_stick_with_logseq/
- r/logseq, "Big update: Logseq is splitting into two versions" (2026-04): markdown version's security-only future read as a deprecation notice — https://www.reddit.com/r/logseq/comments/1swpxht/big_update_logseq_is_splitting_into_two_versions/
- r/logseq, "What are you planning to replace logseq with?" (2025-12): years of complaints about staleness, no roadmap — https://www.reddit.com/r/logseq/comments/1pstos9/what_are_you_planning_to_replace_logseq_with/
- Secondary corroboration (weak source): Medium piece on users migrating to Affine/Obsidian over delays — https://medium.com/@theo-james/logseq-development-delays-are-users-migrating-to-affine-or-obsidian-e22bb42b8741
Apps failing: Logseq (DB rewrite absorbed 2+ years with no release; 2026 split relegates the markdown version to maintenance). Broader pattern: Evernote users repeatedly report silence on pricing changes and support going missing (https://www.reddit.com/r/Evernote/comments/1mtu8s5/evernote_price_increase/ , https://www.reddit.com/r/Evernote/comments/1ms3ds0/whats_going_on_at_the_moment_with_evernote/ ).

### D7. No forced/intrusive AI; fix the basics before shipping AI — MEDIUM-HIGH volume and rising
- r/ObsidianMD (2025-05): Notion "trying to lean heavily into AI" pushed the user to Obsidian; intrusive-AI aversion cited as a common reason — https://www.reddit.com/r/ObsidianMD/comments/1kwjbz9/why_people_are_making_obsidian_more_and_more_like/
- r/ObsidianMD (2025-10): absence of incorporated AI made switching easy — https://www.reddit.com/r/ObsidianMD/comments/1o18nse/for_those_who_recently_switched_from_notion_to/
- r/ProductivityApps (2026-05): anger at AI paywalled at +$10/month on top of an existing subscription — https://www.reddit.com/r/ProductivityApps/comments/1t2zv2n/i_spent_3_years_using_notion_for_everything/
- r/heptabase, 9-month-later review (2025-10): PhD student left because AI features were prioritized over must-have basics (citations, inline tags, backlinks filtering) — https://www.reddit.com/r/heptabase/comments/1nvysr9/what_are_good_and_bad_things_about_heptabase_in/
- r/GoodNotes pricing thread (2023): "$30 for one-off" anger framed around students being squeezed — https://www.reddit.com/r/GoodNotes/comments/16gnfds/goodnotes_6_rip_off/
- Counter-signal for balance: 2026 roundups show the market's centerpiece shifting to AI meeting notes (Granola, Fathom), so demand for AI exists elsewhere — https://learn.g2.com/best-note-taking-apps , https://toolradar.com/best/note-taking
Apps failing: Notion (AI paywall), Heptabase (AI roadmap over basics), Evernote (price hikes justified "because ai" per user commentary — https://www.reddit.com/r/Evernote/comments/1n33kcl/the_trigger_thats_moving_me_from_evernote_anyone/ ).

### D8. Simple, reliable organization: folders + tags + a real export, without over-engineering — MEDIUM volume
- Hacker News, "Why are there no good note taking apps" (2022, still the canonical ask-HN framing): wants markdown/plaintext, folders, tags, no auto-rendering — https://news.ycombinator.com/item?id=31645045
- r/ProductivityApps, "Features that you expect a note taking app to have" (2026-01): organization, visible todos with due dates, PDF export of selections, attachments, E2EE — https://www.reddit.com/r/ProductivityApps/comments/1qbggfh/features_that_you_expect_a_note_taking_app_to_have/
- r/NoteTaking, "best note taking apps in 2026" (2026-07): flagged gap is that apps make you assemble tasks/calendar yourself via plugins — https://www.reddit.com/r/NoteTaking/comments/1uwxg44/best_note_taking_apps_in_2026/
- r/NoteTaking 2026 roundup thread: no app helps you memorize/study — https://www.reddit.com/r/NoteTaking/comments/1uwxg44/best_note_taking_apps_in_2026/ (same thread, different commenter)
- r/samsungnotes wishlist (2026-01): page-size choices, infinite canvas, ruler with angles — https://www.reddit.com/r/samsungnotes/comments/1qg4zal/samsung_notes_is_almost_perfect_but_here_is_whats/
- r/selfhosted, "We need a 'simple' web based MD notes app" (2025-08): the unmet ask is exactly a simple web markdown app — https://www.reddit.com/r/selfhosted/comments/1mzod84/we_need_a_simple_web_based_md_notes_app/

### Single-source, unconfirmed (ranked low on purpose)
- Handwriting search on reMarkable-style e-ink tied to cloud conversion (r/NeboApp thread above is the only direct first-person account found in this sweep): https://www.reddit.com/r/NeboApp/comments/1l9t2xh/search_handwritten_notes_without_converting_to/
- "One button full migration" as a desired feature (only the r/Evernote migration threads articulate it as a demand, others describe the pain): https://www.reddit.com/r/Evernote/comments/1s60t71/how_do_you_migrate_all_your_notes_out_of_evernote/
- Local auto-export of handwriting to a folder on-device (r/ipad single thread, 2023): https://www.reddit.com/r/ipad/comments/1166rez/goodnotes_alternative_handwriting_app_with_local/
- App store review-trend articles for Goodnotes/Notability/Noteshelf/Samsung Notes/Squid/Nebo store pages: UNVERIFIED — individual store pages were not crawlable in this sweep; sentiment was sourced from community threads instead. One third-party review article corroborates Goodnotes pricing confusion: https://eathealthy365.com/the-top-7-limitations-of-the-goodnotes-app-in-2026/

---

## 2. Recurring praise patterns (why people stay)

Obsidian: speed, plain markdown ownership, offline-first, and a huge plugin ecosystem. Switchers repeatedly cite instant open/search and files that outlive the vendor (https://www.reddit.com/r/ProductivityApps/comments/1t2zv2n/i_spent_3_years_using_notion_for_everything/ , https://www.reddit.com/r/ObsidianMD/comments/1qhborl/should_i_switch_from_notion_to_obsidian/ , https://www.reddit.com/r/ObsidianMD/comments/1o3xo6g/officially_moved_from_notion_to_obsidian/ ). HN users praise hackability (custom plugin pushing markdown to a static site) while flagging weak mobile (https://news.ycombinator.com/item?id=41228758 ). The 2026 arrival of the Bases core plugin narrowed the "Notion has databases" objection (https://www.reddit.com/r/ObsidianMD/comments/1wbkuff/deciding_between_obsidian_and_notion_some_help/ ).

Evernote (legacy loyalty): users who stayed a decade praise search, web clipping, and reliability; one HN commenter returned to Evernote after trying everything because it "just works" (https://news.ycombinator.com/item?id=33194051 ); a 2026 defector says they loved it since the beginning and credit Bending Spoons with real product improvements, leaving only over price (https://www.reddit.com/r/enshittification/comments/1rhosd0/i_have_loved_evernote_since_the_beginning_but_it/ , https://www.reddit.com/r/Evernote/comments/1tcw1fj/megathread_pricing_repackaging_discussion/ ).

Anytype: staying users love local-first + E2EE + encryption even on device, and "it's a central hub for my digital life" sentiment (https://www.reddit.com/r/Anytype/comments/1j3bude/active_users_what_is_your_experience_using_at_so/ , https://www.reddit.com/r/Anytype/comments/1vjoevx/considering_anytype_and_looking_for_honest/ , https://www.reddit.com/r/PKMS/comments/1pws1p2/a_review_of_all_pkms_apps_in_2025_which_is_your/ ). Honest caveats: no true WYSIWYG/markdown-native feel (https://www.reddit.com/r/PKMS/comments/1k9iuer/anyone_know_of_an_offlinefirst_blockbased_app/ ) and a "closed in a dark room" data-isolation feeling for some (https://www.reddit.com/r/PKMS/comments/1py2s9p/why_i_ended_up_with_anytype_even_though_its_far/ ).

Heptabase: praised as uniquely good at synthesizing knowledge by arranging cards on a canvas, better than Obsidian canvas which users call a scratchpad (https://www.reddit.com/r/ObsidianMD/comments/1tcd1ws/need_someone_sharing_experience_about_heptabase/ , https://www.reddit.com/r/ObsidianMD/comments/1i6sppl/i_really_like_heptabase/ ). Long-term reviewers who never regretted it still list price and export lock-in as the negatives (https://www.reddit.com/r/PKMS/comments/1cdqsu6/heptabase_review_9_months_in/ ).

Samsung Notes: praised as free with a good writing feel, the default Android stylus pick (https://www.reddit.com/r/GalaxyTab/comments/18gvwtk/the_best_handwritingnotetaking_apps/ ); its wishlists exist precisely because users like it and want to stay (https://www.reddit.com/r/samsungnotes/comments/1qg4zal/samsung_notes_is_almost_perfect_but_here_is_whats/ ).

Apple Notes: praised for zero-friction sync and collaboration with anyone in the Apple ecosystem (https://news.ycombinator.com/item?id=41228758 ).

Joplin, Capacities, Noteful: Joplin is the default open-source Evernote replacement in roundups and r/selfhosted threads (https://zapier.com/blog/best-note-taking-apps/ , https://www.reddit.com/r/selfhosted/comments/1se0c99/looking_for_a_self_hosted_note_taking_app/ ); Capacities wins switchers from Logseq/Heptabase/Tana for being straightforward (https://www.reddit.com/r/capacitiesapp/comments/1fhdhd7/why_i_switched_from_heptabase_tana_logseq_to/ ); Noteful's $8 lifetime price is named as the reason for leaving Notability (https://www.reddit.com/r/notabilityapp/comments/1i0cipr/from_1199_to_1999_in_one_year/ ).

---

## 3. Pricing / business-model resentment patterns

Pattern A — Acquire, raise, repeat (Bending Spoons / Evernote). Documented price path in user reports: $69.99 → $129 → $242/yr offered, cancellations answered with 40% retention discounts (https://www.reddit.com/r/Evernote/comments/1n33kcl/the_trigger_thats_moving_me_from_evernote_anyone/ ); 30%+ increases for consecutive years (https://www.reddit.com/r/Evernote/comments/1evblg2/another_30_price_increase_in_2025/ ); $250/yr top tier called crazy for basic needs, with users kept "constantly looking to exit" (https://www.reddit.com/r/Evernote/comments/1oww8h5/megathread_new_pricing_repackaging_discussion/ ); 2026 megathread where even decade-long satisfied users are forced out (https://www.reddit.com/r/Evernote/comments/1tcw1fj/megathread_pricing_repackaging_discussion/ ). HN threads connect the price rises to the 2026 IPO: WSJ-reported revenue up 30% since 2022 while users fell 48%, i.e., revenue extracted through price rises from a shrinking base (https://news.ycombinator.com/item?id=49672342 ); a user reports their top tier up $70 in one year (https://www.reddit.com/r/Evernote/comments/1ukirdu/bending_spoons_ceo_on_cnbc/ ).

Pattern B — The subscription rug-pull on legacy buyers (Notability). 2021: paid users given one year of premium then downgraded to a free tier with monthly edit limits, widely called the worst subscription transition seen and argued to violate App Store guidelines (https://www.reddit.com/r/notabilityapp/comments/qkseo3/notability_has_the_worst_transition_to_a/ , https://www.reddit.com/r/notabilityapp/comments/qkhos4/notability_is_now_freemium_and_i_hate_it/ , https://www.reddit.com/r/apple/comments/qkgt7g/notability_goes_free_with_subscription_model/ ). 2025: era-of-bought-for-life-is-over thread as the paywall closes on old purchasers (https://www.reddit.com/r/notabilityapp/comments/1ive5aq/as_of_12am_today_the_era_of_boughtforlife/ ); classic-plan breakage and complaint moderation (https://www.reddit.com/r/ipad/comments/1nm9bg5/notability_is_quietly_breaking_the_classic_plan/ ); tier inflation from 2 to 3 plans with AI quotas (https://www.reddit.com/r/notabilityapp/comments/1lng39r/thoughts_on_notability_pro/ ). Churn goes to one-time-price rivals (Noteful — https://www.reddit.com/r/notabilityapp/comments/1i0cipr/from_1199_to_1999_in_one_year/ ).

Pattern C — Version-extortion and hidden one-time tiers (GoodNotes). GN6's 2023 subscription shift produced lasting anger, with the v5-discount fiasco later partially defused (https://www.reddit.com/r/GoodNotes/comments/16gnfds/goodnotes_6_rip_off/ , https://www.reddit.com/r/GoodNotes/comments/1o3oi9v/is_this_the_end_of_goodnotes/ ); the one-time "Special Edition" purchase is buried behind a "Show all plans" disclosure (https://www.reddit.com/r/GoodNotes/comments/1o4g7hh/anyone_using_goodnotes_lifetime_plan_longterm/ ); lifetime excludes cross-platform sync that subscribers get (https://www.reddit.com/r/ipad/comments/18wxqhf/goodnotes_6_worth_one_time_purchase/ ); HN notes the pricing page lists plans without prices (https://news.ycombinator.com/item?id=43869187 ).

Pattern D — Quiet degradation of the paid promise. Notability classic-plan editing limits (Pattern B); Evernote users reporting missing files and account lockouts amid price changes (https://www.reddit.com/r/Evernote/comments/1ms3ds0/whats_going_on_at_the_moment_with_evernote/ ); Standard Notes self-hosters finding premium editors paywalled even on their own servers (https://www.reddit.com/r/selfhosted/comments/1tyt63h/note_app_thats_really_good/ ); Craft's free block limit (https://www.reddit.com/r/PKMS/comments/1k9iuer/anyone_know_of_an_offlinefirst_blockbased_app/ ).

Cross-cutting: the strongest single sentiment sentence found is the refusal to ever buy from the acquirer again: "I will never, ever sign up to any product that is owned by Bending Spoons" (r/PKMS, https://www.reddit.com/r/PKMS/comments/1wsmohv/after_12_years_canceled_evernote/ — quote under 15 words, one per source rule respected).

---

## 4. Handwriting-specific sentiment (stylus note-takers)

The core unmet ask: no app combines (a) a great ink feel, (b) reliable handwriting search/OCR without a disruptive conversion step, (c) real formula/math handling, (d) cross-platform sync, and (e) an open export format at a fair price. Users triangulate between apps that each fail one leg.

- Search without conversion: users want their notebook searchable as-is; forced conversion to text is the complaint against ReMarkable and the friction in Nebo's flow (https://www.reddit.com/r/NeboApp/comments/1l9t2xh/search_handwritten_notes_without_converting_to/ ).
- Recognition ceiling: complicated physics formulae break Nebo; users want math handled (https://www.reddit.com/r/GalaxyTab/comments/hsvaz9/apps_for_searchable_hand_writing_notes/ ).
- Paywall placement: Samsung Notes' one-time tier searches typed but not handwritten text (https://www.reddit.com/r/samsungnotes/comments/1qfp76f/some_of_the_big_issues_of_samsung_notes/ ); GoodNotes gates handwriting AI (spellcheck/math assist) behind the subscription (https://eathealthy365.com/the-top-7-limitations-of-the-goodnotes-app-in-2026/ ).
- Missing features requested for years in Notability: layers for physics/maths/chemistry sketches, tables of contents, internal hyperlinks (https://www.reddit.com/r/notabilityapp/comments/1hwiob4/disappointed_about_the_updates/ ).
- Android fragmentation: per-app feature matrices users maintain show no Android app with good ink + search + sync + export (https://www.reddit.com/r/GalaxyTab/comments/1euj4u6/notetaking_apps/ , https://www.reddit.com/r/GalaxyTab/comments/1kpv9tx/which_notes_app_do_you_recommend/ ).
- Export fidelity: handwriting exported to PDF showing spikes/artifacts (https://www.reddit.com/r/GoodNotes/comments/q5djbq/export_handwriting_spikes/ ); Samsung Notes lacking vector export making files huge (https://www.reddit.com/r/squidnotes/ index).
- Nebo is repeatedly named best-in-class at recognition but "very bare" otherwise (https://www.reddit.com/r/NoteTaking/comments/1voucay/which_ipad_apps_have_handwriting_recognition/ , https://www.reddit.com/r/GalaxyTab/comments/1kpv9tx/which_notes_app_do_you_recommend/ ).

---

## 5. Local-first / privacy / E2EE sentiment — honest assessment

Loud and structurally important inside PKM/dev communities; niche or absent in mainstream consumer sentiment.

Evidence it is a mainstream-of-PKM force: data ownership/server fear is the most-cited reason for leaving Notion and Evernote in this sweep (see D1: https://www.reddit.com/r/ObsidianMD/comments/1qhborl/should_i_switch_from_notion_to_obsidian/ , https://www.reddit.com/r/ProductivityApps/comments/1t2zv2n/i_spent_3_years_using_notion_for_everything/ ). Encryption is a top-6 "expected feature" in a general r/ProductivityApps expectations thread, with users naming Joplin, Notesnook, Bear as E2EE options (https://www.reddit.com/r/ProductivityApps/comments/1qbggfh/features_that_you_expect_a_note_taking_app_to_have/ ). Anytype's committed users cite on-device encryption as the deciding factor (https://www.reddit.com/r/PKMS/comments/1pws1p2/a_review_of_all_pkms_apps_in_2025_which_is_your/ ). GoodNotes users actively audit whether handwriting trains AI features (https://www.reddit.com/r/GoodNotes/comments/1gfifsq/good_notes_and_privacy_concerns/ ).

Evidence it is niche outside those bubbles: HN debates whether local-first has any viable business model and whether demand has been proven at all ("Someone has to prove that there's a demand for paid local first subscriptions" — https://news.ycombinator.com/item?id=45333021 ; a 2026 piece argues "local-first" is being used as a buzzword and that backups of cloud services achieve the same safety — https://news.ycombinator.com/item?id=46506957 ). E2EE skeptics on HN argue client-side E2EE with auto-updating apps is effectively broken and first-party E2EE is "snake oil" (https://news.ycombinator.com/item?id=32562143 ). Roundups' consumer picks (OneNote, Apple Notes, Google Keep) compete on convenience, not encryption (https://www.pcmag.com/picks/the-best-note-taking-apps , https://zapier.com/blog/best-note-taking-apps/ ). Verdict: privacy/ownership language is now the standard grammar of PKM switchers (very loud), but as a standalone purchase driver for the average note app user it remains secondary to price, speed, and sync.

---

## 6. Migration pain (what makes switching hard)

M1 — Evernote export is deliberately hostile: notebook-by-notebook or 100-note-max export, no one-button full migration; a 13-year migration took hours mostly because of export limits (https://www.reddit.com/r/Evernote/comments/1s60t71/how_do_you_migrate_all_your_notes_out_of_evernote/ , https://www.reddit.com/r/Evernote/comments/185y5ll/migrated_to_obsidian/ ). Defectors call exporting all notes "a pain in the ASS" (https://www.reddit.com/r/Evernote/comments/1n33kcl/the_trigger_thats_moving_me_from_evernote_anyone/ ).

M2 — Metadata and fidelity loss in transit: creation dates lost via ENEX→Joplin→markdown routes; table and web-clip formatting degraded; third-party tools (Yarle, evernote2obsidian, Obsidian Importer) exist precisely because official paths lose data (https://www.reddit.com/r/ObsidianMD/comments/18okbxk/migrating_14_years_of_evernote_content_to_obsidian/ , https://www.reddit.com/r/ObsidianMD/comments/1j9zvlc/from_evernote_to_obsidian/ , https://www.reddit.com/r/Evernote/comments/18sz8ru/switching_from_evernote_to_obsidian_here_is_what/ ).

M3 — Bulk-import breakage: importing hundreds of notebooks at once into Obsidian ground a mid-level PC to a halt; wrong-folder misplacements forced a restart and notebook-by-notebook import (https://www.reddit.com/r/enshittification/comments/1rhosd0/i_have_loved_evernote_since_the_beginning_but_it/ , https://www.reddit.com/r/Evernote/comments/18sz8ru/switching_from_evernote_to_obsidian_here_is_what/ ).

M4 — Handwriting lock-in is the hardest wall: .note (Notability) and .goodnotes files are mutually incompatible; PDF export is the only bridge and it is flattened (not editable, handwriting becomes pixels) (https://www.reddit.com/r/GoodNotes/comments/1l9wicx/done_with_notability_whats_the_best_way_to_import/ , https://www.reddit.com/r/GoodNotes/comments/1oe8l4s/is_there_a_way_to_transfer_notes_from_goodnotes/ ). A GoodNotes feedback-forum request for an open data format notes the .notes files are encrypted binary, unreadable to other tools (https://feedback.goodnotes.com/forums/191274-customer-suggestions-for-goodnotes-apple/suggestions/40953457-open-data-format-for-goodnotes ). Noteshelf data sits in a custom binary format with no non-Android client (https://www.reddit.com/r/NoteTaking/comments/10np1tw/android_note_taking_apps/ ).

M5 — Attachment logistics: Obsidian dumps attachments in the vault root by default, requiring plugins like Custom Attachment Location to keep things sane (https://jc.kiwi/evernote-to-obsidian/ ). Syncing attachments (images, PDFs) alongside notes is the recurring failure point of self-hosted stacks (https://www.reddit.com/r/selfhosted/comments/1tyt63h/note_app_thats_really_good/ ).

M6 — Guide-industrial complex as a signal: the volume of third-party Evernote→Obsidian guides (AIToolPick 2026, Jordan Crawford 2025) exists because vendors ship no adequate path (https://aitoolpick.org/blog/how-to-switch-from-evernote-to-obsidian/ , https://jc.kiwi/evernote-to-obsidian/ ).

---

## Coverage and confidence notes

- HN: direct algolia.com JSON fetches were blocked from this environment; HN evidence comes from search-indexed thread excerpts, which still yielded 2024–2026 threads. 
- App store pages: UNVERIFIED (not crawlable); replaced by community threads plus one corroborating review article.
- Reddit r/Anytype and r/heptabase contributed 2025–2026 threads; r/Notion contributed one 2026 thread (users returning to Notion over Obsidian's learning curve: https://www.reddit.com/r/Notion/comments/1u4jfvx/thinking_of_going_back_to_notion_from_obsidian/ — a reminder that the Obsidian wave has a counter-current).
- Roundups used only as secondary corroboration (Zapier, PCMAG, G2, ClickUp, Toolradar).

## Tally

- Ranked demands: 8 (D1–D8), plus 3 single-source items listed separately.
- Demands with ≥2 independent sources: 8 of 8 (each ranked demand cites sources from at least two distinct communities/sites; D8 includes HN + Reddit).
- Praise patterns: 9 apps/communities; pricing patterns: 4; handwriting asks: 7 sub-points; local-first verdict: loud-in-PKM, niche-mainstream; migration pains: 6.
