# Round R12 — Lane B (evidence enrichment), part 1

## Obsidian
### Visual surface
- Desktop (Windows/macOS/Linux, Electron): a three-pane workspace — left icon ribbon (file explorer, search, starred/bookmarks, tags), a collapsible sidebar file tree, and a central Markdown editor in live-preview or reading mode; tabs and split panes are supported, with a right sidebar for backlinks, outline, tags and local graph. The signature screens are the Graph View (force-directed node web of notes) and Canvas (an infinite spatial board where notes, images, links and text cards can be dragged freely), per the official overview and help docs (https://www.eesel.ai/blog/obsidian-overview, https://obsidian.md/help/plugins/graph).
- Mobile (iOS/Android): the same vault model compressed into a two-pane layout (sidebar drawer + editor), with a toolbar of formatting actions above the keyboard; the "Mobile 2.0" refresh added a redesigned interface, native widgets and Siri integration (https://www.geeky-gadgets.com/obsidian-tips-tricks-2026/).
- Customization is a first-class surface: community themes (thousands) and CSS snippets change nearly everything, so the "default look" is only one of many possible UIs (https://help.obsidian.md/).
SHOT-LIST:
- Desktop editor + graph view — https://obsidian.md (hero screenshots)
- Canvas spatial board — https://obsidian.md
- Graph view controls/help — https://obsidian.md/help/plugins/graph
- Mobile app screens — https://obsidian.md (download/overview section)
- Sync plans page — https://obsidian.md/help/sync/plans
- Pricing page — https://obsidian.md/pricing
- Roadmap (upcoming surfaces) — https://obsidian.md/roadmap/
- Publish site example (the Help site itself) — https://publish.obsidian.md/help

### Docs analysis
- Core app is free for personal use; commercial/revenue-generating use requires a paid commercial license (US$50/user/year) (https://smartremotegigs.com/software/obsidian/).
- Obsidian stores plain Markdown files (plus JSON for Canvas, `.canvas`) in a local folder ("vault"); no account is required to use the core app (https://obsidian.md/help/obsidian).
- Sync limits are hard: Standard = 1 synced vault, 1 GB total, 5 MB max file, 1 month version history; Plus = 10 vaults, 10 GB (expandable to 100 GB), 200 MB max file, 12 months version history; unlimited devices on both (https://obsidian.md/help/sync/plans, https://help.obsidian.md/Obsidian+Sync/Plans+and+storage+limits).
- Sync storage is shared flexibly across vaults (pool model), a design worth borrowing (https://obsidian.md/blog/new-sync-plans/).
- Optional add-ons: Obsidian Sync (~$4–5/mo Standard, $8–10/mo Plus) and Obsidian Publish ($8/site/mo annual, $10 monthly) (https://www.eesel.ai/blog/obsidian-pricing, https://checkthat.ai/brands/obsidian/pricing). 40% student/nonprofit discount on Sync and Publish (https://www.lindy.ai/blog/obsidian-pricing).
- Publish features: hover previews (Wikipedia-style popovers), graph view of published pages, backlinks, full-text search, custom domains, page-level metadata (descriptions, slugs, images), SEO/social cards by default, 100% Lighthouse accessibility score, optional analytics (Plausible/Fathom/Google), and editing + publishing from mobile (https://obsidian.md/publish, https://obsidian.md/help/publish/sites).
- Plugin ecosystem: 2,700+ community plugins plus themes and CSS snippets; developer docs and plugin API are public (https://www.geeky-gadgets.com/obsidian-tips-tricks-2026/, https://docs.obsidian.md/Home).
- Web Clipper browser extension for highlighting and saving pages (https://help.obsidian.md/).
- Bases: a database/table view over notes with typed properties — Obsidian's answer to structured data inside Markdown (https://www.geeky-gadgets.com/obsidian-tips-tricks-2026/).
- Roadmap signals design direction: an open file format for canvas data, saving links to notes/graph views/headings/URLs, RTL/mixed-direction text support, an accessible single-vault Sync plan, local-graph per note (https://obsidian.md/roadmap/).
- Shared vaults for sync exist but lack simultaneous/real-time co-editing (https://checkthat.ai/brands/obsidian/pricing).
- UNVERIFIED (from third-party only): exact monthly (non-annual) Sync prices of $5/$10; the "4.5/5 from 21,799 reviews" aggregate (https://aiproductivity.ai/blog/obsidian-pricing/).

### Features
| Area | Detail |
|---|---|
| Editor | Live-preview Markdown editor; reading mode; Wikilinks + standard MD links; callouts, embeds (notes, images, PDFs) |
| Linking | Backlinks, outgoing links, unresolved links, aliases, block references |
| Graph | Global + local graph views, filters, animation timelapse |
| Canvas | Infinite canvas boards, `.canvas` JSON format; plugins add metadata-cache integration |
| Structured data | Bases (database views), note properties (YAML frontmatter) |
| Sync | Paid add-on, E2E encrypted, version history; or DIY via iCloud/Dropbox/Git/Syncthing |
| Publish | Notes → website with graph, search, hover previews, custom domain |
| Extensibility | 2,700+ plugins, themes, CSS snippets, public API |
| Capture | Web Clipper extension; daily notes; quick switcher (Ctrl/Cmd+O) |
| Platforms | Windows, macOS, Linux, iOS, Android |

### Sentiment
| What people say |
|---|
| Core desktop app is loved: free, local-first, endlessly extensible; ~4.5/5 across review aggregators (https://aiproductivity.ai/blog/obsidian-pricing/) |
| Steep learning curve is the most common deterrent (https://www.reddit.com/r/productivity/comments/1q97b5i/obsidian_cons_or_recommend_other_apps/) |
| Mobile is the weak point: buggy Markdown editing on Android, image-handling confusion (paste path vs find path vs sync path), slow app start (https://www.reddit.com/r/ObsidianMD/comments/1o74hpk/anyone_else_feels_obsidian_mobile_is_really/, https://codeculture.store/blogs/developer-culture/obsidian-mobile-problems-2025) |
| Sync opinion flipped positive by 2026: "works out of the box, has the log and version history"; dissenters still find free alternatives (git, Syncthing, Filen) frustrating on iOS (https://www.reddit.com/r/ObsidianMD/comments/1qiao0h/is_obsidian_sync_worth_it/, https://www.reddit.com/r/ObsidianMD/comments/1s1kwbb/is_obsidian_sync_worth_it_in_2026/) |

### Wants
| What people want changed |
|---|
| Lightweight, faster mobile app and instant quick-capture on Android (https://www.reddit.com/r/ObsidianMD/comments/1pogn6w/whats_one_improvement_youd_like_to_see_in/) |
| Bigger Standard Sync plan (1 GB/1 vault is too small) (https://forum.obsidian.md/t/increase-sync-storage-on-standard-plan/106901) |
| Real-time collaboration in shared vaults (https://checkthat.ai/brands/obsidian/pricing) |
| Regex find-and-replace power and graph view on Publish mobile (https://www.reddit.com/r/ObsidianMD/comments/1pogn6w/whats_one_improvement_youd_like_to_see_in/, https://forum.obsidian.md/t/making-graph-view-accessible-on-mobile-browsers-when-checking-ones-obsidian-publish-website/53844) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Core app | Free for personal use; commercial license $50/user/yr (https://smartremotegigs.com/software/obsidian/) |
| Sync | Standard ~$4–5/mo (1 vault, 1 GB, 5 MB files); Plus ~$8–10/mo (10 vaults, 10–100 GB, 200 MB files) (https://obsidian.md/help/sync/plans) |
| Publish | $8/site/mo annual, $10 monthly (https://checkthat.ai/brands/obsidian/pricing) |
| Catalyst/early-access | One-time license for pre-release builds (https://obsidian.md/help/obsidian) |
| Platforms | Windows, macOS, Linux (deb/AppImage/flatpak), iOS, Android |

### Contradictions
- The folklore "Obsidian has no collaboration" is confirmed for real-time editing, but Sync Plus does offer shared vaults for asynchronous collaboration (https://checkthat.ai/brands/obsidian/pricing).
- Canvas files are JSON (`.canvas`), not Markdown; the roadmap lists an "open file format for infinite canvas data" as future work (https://obsidian.md/roadmap/) — contradicting the common "everything is plain Markdown" shorthand.

Sources: https://obsidian.md/publish • https://obsidian.md/help/sync/plans • https://obsidian.md/roadmap/ • https://obsidian.md/pricing • https://www.reddit.com/r/ObsidianMD/comments/1o74hpk/anyone_else_feels_obsidian_mobile_is_really/ • https://www.geeky-gadgets.com/obsidian-tips-tricks-2026/

## Obsidian Publish
### Visual surface
- Web only: a reader-facing site generated from a vault, published under publish.obsidian.md/<site> (custom domains supported). Default layout: left sidebar with file-explorer navigation and search, center content column, right sidebar with table of contents and an optional local graph; hovering links shows Wikipedia-style page previews (https://obsidian.md/publish, https://obsidian.md/help/publish/sites).
- Fully themable with Publish themes (buildable via the developer docs), so many public sites look custom (https://obsidian.md/help/publish/customize).
- Mobile visitors get a first-class responsive layout; publishers can manage the site from the Obsidian mobile app (https://obsidian.md/publish).
SHOT-LIST:
- Publish product page hero — https://obsidian.md/publish
- Live example site (Obsidian Help) — https://publish.obsidian.md/help
- Site customization options doc — https://obsidian.md/help/publish/customize
- Manage sites (site settings) doc — https://obsidian.md/help/publish/sites

### Docs analysis
- You select which notes to publish and press Publish; the site goes live — no server/hosting management (https://mintlify.wiki/obsidianmd/obsidian-help/publish/introduction).
- Components are toggleable: file-explorer navigation, search bar, table of contents, graph view (local graph in the right sidebar), backlinks (https://obsidian.md/help/publish/sites, https://deepwiki.com/obsidianmd/obsidian-help/3.2-obsidian-publish).
- SEO and social-sharing cards automatic; per-page metadata (descriptions, slugs, images) customizable (https://obsidian.md/publish).
- Privacy stance: private by default, analytics opt-in (https://obsidian.md/publish).
- Performance/accessibility claims: no-configuration speed, 100% Lighthouse accessibility score (https://obsidian.md/publish).
- Limit: published graph on mobile browsers has been a long-standing user complaint; navigation/graph/search placement is fixed per sidebar layout rules (https://forum.obsidian.md/t/making-graph-view-accessible-on-mobile-browsers-when-checking-ones-obsidian-publish-website/53844, https://forum.obsidian.md/t/publish-move-navigation-graph-and-search-to-same-sidebar-when-outline-is-not-used/25767).
- Full refund within 7 days for Sync and Publish purchases (https://obsidian.md/pricing).

### Features
| Area | Detail |
|---|---|
| Publishing | Selective note publishing, one-click publish, custom domains |
| Reader features | Hover previews, graph view, backlinks, search, TOC, file explorer nav |
| Customization | Publish themes, nav ordering, component toggles, per-page metadata |
| Ops | Automatic SEO/social cards, mobile-friendly, optional analytics, accessibility-first |

### Sentiment
| What people say |
|---|
| The interactive graph + hover previews are the differentiator vs static site generators for digital gardens and wikis (https://unmarkdown.com/blog/obsidian-publish-vs-unmarkdown) |
| Users call it pricey for what it is and maintain free alternatives (pubsidian, Quartz) (https://github.com/yoursamlan/pubsidian) |
| Mobile graph view and sidebar layout inflexibility are recurring gripes (https://forum.obsidian.md/t/making-graph-view-accessible-on-mobile-browsers-when-checking-ones-obsidian-publish-website/53844) |

### Wants
| What people want changed |
|---|
| Graph view on mobile published sites (https://forum.obsidian.md/t/making-graph-view-accessible-on-mobile-browsers-when-checking-ones-obsidian-publish-website/53844) |
| Merge navigation/graph/search into one sidebar option (https://forum.obsidian.md/t/publish-move-navigation-graph-and-search-to-same-sidebar-when-outline-is-not-used/25767) |
| Lower price or feature parity with free alternatives (https://unmarkdown.com/blog/obsidian-publish-vs-unmarkdown) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Price | $8/site/mo billed annually; $10 monthly (https://checkthat.ai/brands/obsidian/pricing) |
| Platform | Web (reader); managed from Obsidian desktop/mobile apps |

### Contradictions
- none found

Sources: https://obsidian.md/publish • https://obsidian.md/help/publish/sites • https://obsidian.md/pricing • https://unmarkdown.com/blog/obsidian-publish-vs-unmarkdown

## OneNote
### Visual surface
- Windows desktop: a free-form canvas notebook — each page is an unlimited whiteboard-like surface where text boxes, ink, images, audio, tables and embedded files can be placed anywhere (not a linear document). Left rail lists Notebooks → Sections (colored tabs) → Pages; a top ribbon (Microsoft 365 style) carries Draw/Home/Insert/View tabs. Per the product pages and reviews, the free-form canvas is the defining visual trait (https://www.softwr.com/compare/microsoft-365-vs-microsoft-onenote, https://brandenbodendorfer.com/free-onenote-vs-microsoft-office-onenote/).
- Web: a simplified version of the same hierarchy at onenote.com / OneDrive integration, with the ribbon reduced; desktop and browser can be set as default opening targets for Copilot-app links (https://www.hubsite365.com/en-ww/crm-pages/6-new-microsoft-onenote-features-copilot-notebooks-for-all-fall-2026.htm).
- iPad/Android: touch-first, ribbon collapsed to bottom tab bar, strong pencil/stylus support; the ink experience is called the most mature in the category (https://omnicanvasnotes.com/blog/reviews/onenote-alternatives).
- Fall 2026 additions visible across platforms: Copilot Notebooks (AI-curated notebooks with summaries, drafts, audio overviews saved to OneDrive), MathML support, and touch/keyboard polish (https://www.hubsite365.com/en-ww/crm-pages/6-new-microsoft-onenote-features-copilot-notebooks-for-all-fall-2026.htm, https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/whats-new-in-notebooks--october-2026/4559105).
SHOT-LIST:
- Product page hero (notebook/section/page layout) — https://www.microsoft.com/microsoft-365/onenote
- Copilot in OneNote support hub — https://support.microsoft.com/en-us/onenote/welcome-to-copilot-in-onenote
- Copilot Notebooks explainer — https://support.microsoft.com/en-us/microsoft-365-copilot/what-are-microsoft-365-copilot-notebooks-in-onenote
- Copilot Notebooks vs OneNote Notebooks comparison — https://support.microsoft.com/en-us/microsoft-365-copilot/compare-microsoft-365-copilot-notebooks-and-microsoft-onenote-notebooks
- Store listing for mobile/tablet UI — Microsoft Store / App Store / Play "Microsoft OneNote" pages (not fetched; capture via search)

### Docs analysis
- Hard limit: 2 GB per section file when syncing to OneDrive; error 0xE0000025 "file too large" beyond it; SharePoint limits vary (https://support.microsoft.com/en-us/office/resolve-the-0xe0000025-file-too-large-error-in-onenote-22f8fc8b-92ee-4f8f-b334-0126a3d1f67a).
- Free tier: full OneNote app with 5 GB OneDrive storage shared with other M365 apps; Microsoft 365 Personal/Family adds storage, version history, desktop Office apps; M365 Premium ($19.99/mo) raises Copilot usage limits (https://www.cloudwards.net/onenote-review/, https://costbench.com/software/note-taking/onenote/).
- Handwriting OCR is Windows-only for indexing: ink created on iPad/iPhone is not searchable until opened/processed on a Windows PC (https://learn.microsoft.com/en-us/answers/questions/5748904/one-note-hand-writing-recognization-problem).
- Copilot capabilities documented by Microsoft: summarize pages/sections, generate to-do lists from notes, draft content; Copilot Notebooks draw from docs, decks, Outlook email, Teams chats, Loop and txt files, and produce topic-based "audio overview" episodes saved to OneDrive (https://support.microsoft.com/en-us/onenote/welcome-to-copilot-in-onenote, https://support.microsoft.com/en-us/microsoft-365-copilot/what-are-microsoft-365-copilot-notebooks-in-onenote, https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/whats-new-in-notebooks--october-2026/4559105).
- Copilot Edit Mode (in development, GA target Nov 2026) would let Copilot create/rename/delete pages, sections and whole notebooks — admins flagged as a risk surface (https://windowsforum.com/news/copilot-edit-mode-for-onenote-planned-for-november-2026-direct-notebook-changes-and-admin-risks.447691/).
- Copilot became available to all Microsoft 365 users regardless of subscription level in fall 2026 (https://www.geeky-gadgets.com/new-microsoft-onenote-features/).
- Design decisions worth borrowing: infinite free-form page canvas; notebook→section→page hierarchy with colored sections; page templates; tags with summary pages; local automatic backups on Windows; audio recording embedded on page; "OneNote Notebook" vs new "Copilot Notebook" split shows Microsoft differentiating long-term archive vs AI-curated workspace (https://support.microsoft.com/en-us/microsoft-365-copilot/compare-microsoft-365-copilot-notebooks-and-microsoft-onenote-notebooks).
- Export story is weak: PDF flattens ink to images; .one format is proprietary; no live-ink export path (https://www.plaud.ai/blogs/articles/onenote-alternatives).
- OneNote 2021 perpetual desktop reaches end of support Oct 13, 2026 (third-party; UNVERIFIED against Microsoft lifecycle pages) (https://www.onenotegem.com/a/faq/onenote/2024/0718/onenote-error-0xE0000025.html).

### Features
| Area | Detail |
|---|---|
| Structure | Notebooks → sections → (section groups) → pages → subpages |
| Canvas | Free-form page: place text boxes, ink, media anywhere |
| Ink | Draw/tab/laser pointer, ink-to-text, ink-to-shape, math assistant; OCR indexing Windows-only |
| Search | Full-text incl. OCR of images (Windows), tag search |
| Tags | Checkbox/task/priority tags; tag summary pages |
| Collaboration | Real-time co-editing via cloud notebooks; sharing via OneDrive/SharePoint |
| AI | Copilot summarize/organize/draft; Copilot Notebooks with multi-source references and audio overviews |
| Clipper | Web Clipper extension |
| History | Page versions (M365 tiers), local backups, recycle bin |
| Platforms | Windows, macOS, web, iOS, Android |

### Sentiment
| What people say |
|---|
| Handwriting/stylus workflow on Windows and iPad is considered best-in-class; a fair reason to stay (https://omnicanvasnotes.com/blog/reviews/onenote-alternatives) |
| Recurring complaints: OneDrive sync conflicts ("This page has conflicting changes"), slow deep hierarchy navigation, weak backlinks, data lock-in to OneDrive (https://www.usecarly.com/blog/onenote-alternatives/) |
| Large notebooks make search sluggish; it can miss ink that Evernote catches (https://www.atlasworkspace.ai/blog/evernote-vs-onenote) |
| Organization decays over time — messy pages; reviewers note missing saved searches and advanced filtering (https://geekchamp.com/microsoft-onenote-reviews-2026-pros-cons-and-ratings/) |
| Free version widely valued; M365 integration praised (https://www.capterra.com/p/227211/Microsoft-OneNote/pricing/) |

### Wants
| What people want changed |
|---|
| Better backlinks, saved searches, and structured/filtering power (https://geekchamp.com/microsoft-onenote-reviews-2026-pros-cons-and-ratings/) |
| Reliable sync without conflict pages; larger section limits (https://support.microsoft.com/en-us/office/resolve-the-0xe0000025-file-too-large-error-in-onenote-22f8fc8b-92ee-4f8f-b334-0126a3d1f67a) |
| Real export/interoperability (ink that survives migration) (https://www.plaud.ai/blogs/articles/onenote-alternatives) |
| Cross-platform handwriting OCR parity (iPad/iPhone indexing) (https://learn.microsoft.com/en-us/answers/questions/5748904/one-note-hand-writing-recognization-problem) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | Full app, 5 GB OneDrive storage (https://www.cloudwards.net/onenote-review/) |
| M365 Personal | $9.99/mo annual (Capterra cites $6.99 promo pricing) (https://costbench.com/software/note-taking/onenote/) |
| M365 Premium | $19.99/user/mo, highest Copilot limits (https://costbench.com/software/note-taking/onenote/) |
| Platforms | Windows, macOS, web, iOS, Android; OneNote 2021 perpetual retiring Oct 2026 (UNVERIFIED) |

### Contradictions
- Free tier: one pricing site claims "OneNote does not offer a free plan as of September 2026" (https://costbench.com/software/note-taking/onenote/free-plan/), while the same site's own review and multiple other sources describe a free version with 5 GB storage (https://costbench.com/software/note-taking/onenote/, https://www.cloudwards.net/onenote-review/). Weight of evidence: free tier exists; the "no free plan" page appears to be an error.
- M365 Personal price: $9.99/mo (CostBench) vs $6.99/mo (Capterra) — likely promotional vs list price.

Sources: https://support.microsoft.com/en-us/office/resolve-the-0xe0000025-file-too-large-error-in-onenote-22f8fc8b-92ee-4f8f-b334-0126a3d1f67a • https://support.microsoft.com/en-us/microsoft-365-copilot/what-are-microsoft-365-copilot-notebooks-in-onenote • https://www.cloudwards.net/onenote-review/ • https://www.usecarly.com/blog/onenote-alternatives/ • https://costbench.com/software/note-taking/onenote/

## Evernote
### Visual surface
- Desktop/web/mobile: the classic three-pane layout — left sidebar (note lists, notebooks, tags, Tasks, shortcuts), middle note list with snippets, right editor pane. A "Home" dashboard with draggable widgets (tasks, calendar, notes, pins) is the modern landing surface, per Evernote's own marketing and reviews (https://evernote.com/features/ai-features, https://www.linktly.com/productivity-software/evernote-review/).
- Editor: rich-text (non-Markdown) with checklists, tables, attachments, in-note audio, and a dark mode; v11/v12 redesigns modernized fonts and spacing (https://www.pragma-code.de/en/blog-evernote-guide-features-updates-tips).
- Mobile apps retain the three-pane structure with a bottom tab bar (Home, Search, new note, Tasks) — long-time users describe recent versions as heavier ("slow bloated mess" is a recurring phrase) (https://www.reddit.com/r/Evernote/comments/1oww8h5/megathread_new_pricing_repackaging_discussion/).
SHOT-LIST:
- Product/features hero — https://evernote.com/features/ai-features
- Plan comparison page (UI screenshots per plan) — https://evernote.com/compare-plans
- AI features overview — https://evernote.com/features/ai-features
- Help center (screenshots of Home, Tasks, Search) — https://help.evernote.com/hc/en-us/articles/46594411188371-Evernote-s-AI-Features-Overview

### Docs analysis
- Free plan: max 50 notes, 1 notebook, 1 GB monthly uploads, 200 MB max note size, single device + web — documented by Evernote's own blog and help article (https://evernote.com/blog/evernote-free-note-limits, https://help.evernote.com/hc/en-us/articles/23565231682323-Understanding-Evernote-Free-and-Starter-plans-limits-note-and-notebook-limits-explained).
- Starter ($99/yr) caps at 1,000 notes per Harbor's price-history tracking (https://harbor.my/blog/evernote-price-history/); Advanced ($249.99/yr) is the "real" tier; Enterprise custom (https://www.usecarly.com/blog/evernote-pricing/).
- AI suite (built "in close collaboration with OpenAI"): semantic search over saved content, AI Assistant chat that can search/organize/enrich notes and manage tasks, AI Meeting Notes with transcription and summaries, AI Cleanup/formatting (https://evernote.com/features/ai-features, https://help.evernote.com/hc/en-us/articles/46594411188371-Evernote-s-AI-Features-Overview).
- Natural-language search ("What did I write about X in 2023?") is a flagship 2026 capability (https://toolchase.com/tool/evernote-ai/).
- Tasks with due dates/reminders and Google Calendar integration tie meetings to action items (https://work-management.org/tasks/evernote-review/).
- Spaces remain the team/cross-functional organization layer (https://www.linktly.com/productivity-software/evernote-review/).
- Search spans typed text, PDFs, image OCR and handwriting in one query — still considered among the best (https://www.atlasworkspace.ai/blog/evernote-vs-onenote).
- Design decisions worth borrowing: notebook+tag hybrid organization; web clipper as a capture moat; plan limits that count notes (not storage) as the free-tier squeeze mechanism; calendar↔notes↔tasks triangle.
- UNVERIFIED: whether monthly billing for Starter is exactly $14.99 and Advanced $24.99 (third-party rounding).

### Features
| Area | Detail |
|---|---|
| Capture | Web Clipper, email-in, scanning, audio notes, widgets |
| Organization | Notebooks, tags, stacks, Spaces (teams), shortcuts |
| Search | Full-text + PDF/OCR/handwriting + semantic AI search |
| Tasks | In-note tasks, due dates, recurring, calendar sync |
| AI | Assistant chat, meeting transcription/summaries, cleanup |
| Sync | Cloud (server-side, encrypted in transit); offline on paid tiers |
| Platforms | Windows, macOS, web, iOS, Android |

### Sentiment
| What people say |
|---|
| Price anger dominates: one user's yearly charge went from about $83.80 (2024) to $268.61 (2026); megathreads keep filling (https://www.reddit.com/r/Evernote/comments/1tcw1fj/megathread_pricing_repackaging_discussion/) |
| Free tier squeeze (50 notes/1 notebook) reads as hostility to legacy users (https://www.reddit.com/r/Evernote/comments/17ciai2/is_free_tier_now_limited_to_50_notes/) |
| Product itself still praised: best-in-class search and OCR, useful AI, good calendar/tasks loop (https://work-management.org/tasks/evernote-review/) |
| Performance complaints: heavy client, slow mobile app (https://www.reddit.com/r/Evernote/comments/1oww8h5/megathread_new_pricing_repackaging_discussion/) |
| Distrust of Bending Spoons' strategy: profit-max on a niche, arbitration-only terms changes (https://www.reddit.com/r/Evernote/comments/1mtu8s5/evernote_price_increase/) |

### Wants
| What people want changed |
|---|
| Sane pricing with notice; grandfathering of loyal users (https://www.reddit.com/r/Evernote/comments/1tcw1fj/megathread_pricing_repackaging_discussion/) |
| Restored free tier / higher note caps (https://www.reddit.com/r/Evernote/comments/1mja0y9/evernotes_prices_plans_changing_again_for_the/) |
| Faster, lighter clients (https://www.reddit.com/r/Evernote/comments/1oww8h5/megathread_new_pricing_repackaging_discussion/) |
| Better markdown/interoperability and export (common refrain in alt-app lists; UNVERIFIED as top-request) (https://www.plaud.ai/blogs/articles/onenote-alternatives) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | 50 notes, 1 notebook, 1 GB/mo uploads, 200 MB/note, 1 device (https://evernote.com/blog/evernote-free-note-limits) |
| Starter | $99/yr (~$14.99/mo monthly), 1,000 notes cap (https://harbor.my/blog/evernote-price-history/) |
| Advanced | $249.99/yr (~$24.99/mo monthly) (https://www.usecarly.com/blog/evernote-pricing/) |
| Enterprise | Custom (https://www.eesel.ai/blog/evernote-pricing) |
| Platforms | Windows, macOS, web, iOS, Android |

### Contradictions
- Old plan structure persists in some 2026 reviews: ClickUp still describes Personal $14.99 / Professional $17.99 tiers with 10 GB uploads (https://clickup.com/learn/topic/productivity/tools/evernote/), while Evernote's current structure per pricing trackers is Free/Starter $99/Advanced $249.99 with note-count caps (https://harbor.my/blog/evernote-price-history/). Current structure wins; ClickUp page is stale.
- Free-tier upload allowance: eesel says 1 GB/mo; CostBench says 1-2 devices; Harbor notes the free tier "was" real — the 50-note cap is the consistent, current fact.

Sources: https://evernote.com/blog/evernote-free-note-limits • https://help.evernote.com/hc/en-us/articles/46594411188371-Evernote-s-AI-Features-Overview • https://harbor.my/blog/evernote-price-history/ • https://www.reddit.com/r/Evernote/comments/1tcw1fj/megathread_pricing_repackaging_discussion/ • https://evernote.com/features/ai-features

## Notion
### Visual surface
- Desktop/web: a clean, minimal block-based document editor on white/gray chrome; left sidebar of pages and workspaces; the page is a stack of draggable blocks (text, headings, toggles, callouts, code) that can be turned into databases with multiple views (table, board, calendar, gallery, timeline, list). Slash-command driven; the same surface morphs between note, wiki, and project tracker (https://aiproductivitypicks.com/notion-review-2026/, https://clickup.com/learn/topic/productivity/tools/notion/).
- 2026 surface has grown into a suite: Notion Mail (Gmail-connected inbox that auto-labels/sorts into custom views, composed with the same slash-command editor), Notion Calendar, AI Meeting Notes with speaker labels, and Notion Agents that can read/write Excel and PowerPoint and build interactive HTML blocks like an ROI calculator (https://www.notion.com/releases/2026-07-01, https://www.eesel.ai/blog/notion-ai-review).
- October 2026: Agents got "their own computer and browser," a "Review for me" safety-check mode, and AI usage consolidated under a credit system ($10 per 1,000 credits), with BYOK (bring your own AI) and an improved MCP server (https://releasebot.io/updates/notion, https://www.notion.com/releases).
- Mobile: recognizable but weaker — reviewers consistently call it a second-class citizen vs desktop (https://smartprocessflow.com/notion-review).
SHOT-LIST:
- Product/features hero — https://www.notion.com/product/features
- Pricing page — https://www.notion.com/pricing
- Release notes (screenshots of newest features) — https://www.notion.com/releases
- Notion 3.6 release (agents/HTML blocks) — https://www.notion.com/releases/2026-07-01

### Docs analysis
- Blocks are the unit of content; Free plan: unlimited pages/blocks for a solo user, 5 MB file upload cap, 7-day page history, 10 guests; block cap appears once a second member joins (1,000 blocks per multiple trackers, exact unpublished number per Vyneron) (https://get-alfred.ai/blog/notion-pricing, https://vyneron.com/en/blog/notion-pricing-2026).
- Plans: Free $0; Plus $10/member/mo annual ($12 monthly); Business $20 annual ($24 monthly) — Business now includes the full AI suite, replacing the killed $10/mo AI add-on; Enterprise custom (https://www.rock.so/blog/notion-pricing, https://workmanagementhub.com/notion-pricing-2026/).
- AI credits: $10 per 1,000 monthly credits beyond plan allowances; "Auto" model tier claims frontier results at 90% lower cost (https://www.notion.com/releases).
- Databases: relational links, rollups, subtasks, dependencies, 6+ views, formulas; automation rules exist but are weaker than Asana/ClickUp; no native Gantt dependencies or time tracking (https://crufizo.com/notion-review-2026/, https://smartprocessflow.com/notion-review).
- Offline mode: introduced a real offline mode in 2025 with teams stating a goal to make it "offline by default," avoiding forcing giant workspace downloads; reviewers in 2026 still call it inconsistent (https://www.reddit.com/r/Notion/comments/1mo885b/notion_finally_has_real_offline_mode/, https://ones.com/blog/notion-docs-app-offline-mode-what-actually-works-in-2026/).
- Public API; MCP server for agent access; integrations with Slack, Zapier/Make/n8n (https://smartproductivitytools.com/notion-complete-guide/, https://www.notion.com/releases).
- Design decisions worth borrowing: blocks as universal primitive; databases with typed properties and multiple views; slash commands; a permission/guest model; template marketplace as ecosystem engine; AI priced by credits rather than seats.

### Features
| Area | Detail |
|---|---|
| Editor | Blocks, slash commands, toggles, callouts, HTML blocks |
| Databases | Relations, rollups, formulas, 6+ views, automations |
| AI | Agents (scheduled/triggered), Q&A, meeting notes with speaker labels, credit-based |
| Suite | Notion Mail, Notion Calendar, AI meeting transcription (Zoom/Meet/Teams) |
| Collaboration | Real-time co-editing, comments, guest sharing, workspaces |
| Extensibility | Public API, MCP, integrations, template marketplace |
| Platforms | Web, Windows, macOS, iOS, Android |

### Sentiment
| What people say |
|---|
| G2 strongly positive (4.6/5, 10k+ reviews) but Reddit skews negative on pricing changes and performance (https://hirekai.ai/blog/notion-review) |
| Performance: 3-5s loads on big pages; degradation above ~5,000 database records (https://www.tryorbye.com/products/notion, https://hackceleration.com/notion-review/) |
| Learning curve 2-4 weeks; users report "spending more time organizing than working" (https://www.tryorbye.com/products/notion) |
| Lock-in anxiety: poor full-fidelity export keeps people trapped (https://www.reddit.com/r/Notion/comments/1kyn5wl/this_is_for_people_frustrated_with_notion/) |
| AI paywall resentment: full AI moved behind Business plan; "Plus plan's 20 AI responses is misleading" (https://www.tryorbye.com/products/notion, https://ainotely.com/blog/notion-review/) |

### Wants
| What people want changed |
|---|
| True offline-by-default and reliable mobile app (https://www.reddit.com/r/Notion/comments/1mo885b/notion_finally_has_real_offline_mode/) |
| Task dependencies/Gantt, time tracking, stronger automations (https://smartprocessflow.com/notion-review) |
| Honest, stable AI pricing (https://www.tryorbye.com/products/notion) |
| Better export/data portability (https://www.reddit.com/r/Notion/comments/1kyn5wl/this_is_for_people_frustrated_with_notion/) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | $0, unlimited solo blocks, 5 MB files, 7-day history (https://get-alfred.ai/blog/notion-pricing) |
| Plus | $10/member/mo annual, $12 monthly (https://www.rock.so/blog/notion-pricing) |
| Business | $20/member/mo annual, $24 monthly, AI included (https://workmanagementhub.com/notion-pricing-2026/) |
| AI credits | $10 per 1,000 credits (https://www.notion.com/releases) |
| Enterprise | Custom |
| Platforms | Web, Windows, macOS, iOS, Android |

### Contradictions
- Plan prices conflict across trackers: TinyCommand claims Plus $12 annual / Business $18 annual with a separate $10 AI add-on (https://tinycommand.com/blogs/notion-pricing-2026), while Notion's own pricing page and most trackers agree on Plus $10 / Business $20 annual with AI included on Business (https://www.notion.com/pricing, https://www.rock.so/blog/notion-pricing). Weight of evidence: the latter; TinyCommand appears stale.
- "No real offline" folklore vs Notion's 2025 shipped offline mode (https://www.reddit.com/r/Notion/comments/1mo885b/notion_finally_has_real_offline_mode/): both partly true — mode exists, reliability complaints persist into 2026.

Sources: https://www.notion.com/releases • https://www.notion.com/pricing • https://www.rock.so/blog/notion-pricing • https://www.tryorbye.com/products/notion • https://www.reddit.com/r/Notion/comments/1mo885b/notion_finally_has_real_offline_mode/

## Craft
### Visual surface
- Apple platforms (Mac/iPhone/iPad/Vision Pro) are Craft's home turf: a gorgeous native document app — paper-white canvas, soft typography, block-based docs with inline images, "spaces" as top-level folders, and a distinctive share-as-beautiful-website output. Reviews consistently call it one of the best-looking docs apps available (https://websites2know.com/craft-do-review/, https://www.g2.com/products/craft-docs/reviews).
- Windows and Android (native Android shipped in 2026, fixing the most-cited limitation) plus web app round out platforms; the 2026 releases focused on speed ("Craft now opens faster") and AI editing with three selectable models (https://apps.apple.com/us/app/craft-write-docs-ai-editing/id1487937127, https://websites2know.com/craft-do-review/).
- 2026 feature surface: whiteboards, collections, tags + custom properties with filtering (knowledge-base/reading-list builders), daily notes, tasks with calendar context, MCP support on the free tier (unusual vs competitors) (https://www.anygen.io/showcase/craft-app/index.html, https://reviews.thewindowsclub.com/craft-app-review/, https://digijaws.com/reviews/craft-review/).
SHOT-LIST:
- Product hero — https://www.craft.do
- Pricing page — https://www.craft.do/pricing
- App Store listing (iPad/Mac UI) — https://apps.apple.com/us/app/craft-write-docs-ai-editing/id1487937127
- Help center (sharing/publishing screens) — https://support.craft.do/hc/en-us/articles/4413266374673-Sharing-and-Collaborating-on-Craft-Documents

### Docs analysis
- Sharing model: docs shared individually; no folder sharing; published pages get their own comments setting — public web publishing is first-class (https://support.craft.do/hc/en-us/articles/4413266374673-Sharing-and-Collaborating-on-Craft-Documents).
- Export breadth: PDF, TextBundle, Markdown, Word, plain text — unusually generous, aligned with the solo-writer positioning (https://bizstack.tech/craft-docs-review/).
- Free plan (per DigiJaws, verified 2026-09): 1,500 blocks, 1 GB storage, 25 MB per file, 7-day version history, 15 AI credits (https://digijaws.com/reviews/craft-review/). Paid: Plus $6.40/mo annual or $8 monthly; Family $12/$15 for 2-6 accounts; Team flat $50/mo up to 10 accounts (https://digijaws.com/reviews/craft-review/).
- MCP available even on free tier — rare (https://digijaws.com/reviews/craft-review/).
- AI: assistant with three selectable models, can be avoided entirely (https://wondertools.substack.com/p/craftapp).
- Design decisions worth borrowing: document-as-artifact publishing (docs designed to be shared outward, not just stored); native-platform feel over web-wrapper; spaces + daily notes as the organizing spine; graceful "AI optional" stance.
- Organization depth is shallower than Notion: tags/properties arrived recently; no true database engine (https://reviews.thewindowsclub.com/craft-app-review/).

### Features
| Area | Detail |
|---|---|
| Editor | Block-based docs, inline media, styling, page styles |
| Structure | Spaces, folders, daily notes, tags + custom properties, collections, whiteboards |
| AI | Assistant with model choice, AI editing, 15 credits on free |
| Sharing | Real-time collaboration, public publishing with comments |
| Tasks | Simple task blocks with calendar context |
| Export | PDF, Markdown, Word, TextBundle |
| Platforms | Mac, iPhone, iPad, Vision Pro, Windows, Android, web |

### Sentiment
| What people say |
|---|
| Design/beauty is the core love; "best-looking note app you can buy" (https://websites2know.com/craft-do-review/) |
| Long-time complaint was Apple-only/weak Android and Windows — 2026 Android app addressed it (https://websites2know.com/craft-do-review/) |
| Struggles as a system-of-record at scale vs Notion; better as a writing/presentation tool (https://www.softwares.com/software/craft) |
| Free-tier document limits frustrate professionals (10-doc Starter per Toolguide) (https://toolguide.io/en/tool/craft/) |

### Wants
| What people want changed |
|---|
| Deeper organization (folders/database-like structures) at scale (https://reviews.thewindowsclub.com/craft-app-review/) |
| Richer integrations/ecosystem beyond native share sheets (https://digijaws.com/reviews/craft-review/) |
| More generous free tier (https://toolguide.io/en/tool/craft/) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | Capped (blocks/storage/AI credits per DigiJaws; 10-doc Starter per Toolguide — see contradiction) |
| Plus | $6.40/mo annual, $8 monthly (https://digijaws.com/reviews/craft-review/) |
| Family | $12 annual / $15 monthly, 2-6 accounts |
| Team | $50/mo flat, up to 10 accounts |
| Platforms | Mac, iOS/iPadOS, Vision Pro, Windows, Android, web |

### Contradictions
- Free plan shape: DigiJaws describes a 1,500-block/1 GB free plan (https://digijaws.com/reviews/craft-review/) while Toolguide describes a "Starter" free plan limited to 10 documents with +2/week (https://toolguide.io/en/tool/craft/). Likely a 2026 repackaging; both third-party — official https://www.craft.do/pricing says only "free to start; upgrade for unlimited docs, AI assistant & 30-day version history." UNVERIFIED exact free limits.
- Older reviews (Softwares) cite paid "from $10/mo" (https://www.softwares.com/software/craft) vs DigiJaws' $6.40/$8 Plus — pricing has evidently changed recently.

Sources: https://www.craft.do/pricing • https://support.craft.do/hc/en-us/articles/4413266374673-Sharing-and-Collaborating-on-Craft-Documents • https://digijaws.com/reviews/craft-review/ • https://websites2know.com/craft-do-review/ • https://apps.apple.com/us/app/craft-write-docs-ai-editing/id1487937127

## Anytype
### Visual surface
- Desktop (Windows/macOS/Linux): a Notion-like block editor over a local-first core — left sidebar with spaces and object list, canvas-style pages built from blocks (paragraphs, headings, images, code, embeds), and database-style "sets/collections" with table, board, gallery and calendar views; a graph view visualizes the object network (https://creatoreconomytools.com/tool/anytype, https://www.getapp.com/collaboration-software/a/anytype/).
- Mobile (iOS/Android): native apps with the same object model; reviewers say mobile sync and polish still trail desktop (https://tooliverse.ai/tools/anytype).
- The team has actively simplified the interface; early adopters report the learning curve has flattened in recent versions (https://www.producthunt.com/products/anytype/reviews).
SHOT-LIST:
- Product hero (dashboards/knowledge graph) — https://anytype.io
- GitHub org (open-source repos, architecture) — https://github.com/anyproto
- App Store listing — https://apps.apple.com/us/app/anytype-the-everything-app/id6449487029
- Docs site — https://doc.anytype.io (not fetched; capture via search)

### Docs analysis
- Local-first: primary copy of data on device; create/edit/search/link with no internet; E2E encryption where only the user holds keys; peer-to-peer sync between devices (https://aisotools.com/blog/anytype-review-2026, https://checkthat.ai/brands/anytype).
- Open-source (anyproto org), no-code, local-only or self-hosted backup node options without a membership (https://www.getapp.com/collaboration-software/a/anytype/, https://tooliverse.ai/tools/anytype).
- Free plan: unlimited objects, 1 GB sync storage, E2E encrypted (https://toolradar.com/tools/anytype/pricing).
- Paid: Free / Pro $10/mo / Ultra $20/mo (price increases Aug 2026 from $8/$16), billed monthly; entry "from $9/mo" per Toolradar Oct 2026 check — UNVERIFIED exact tier matrix (https://aiproductivity.ai/tools/anytype/, https://toolradar.com/tools/anytype).
- Object model: every item is an object with a type and relations; flexible custom types; this is the core abstraction (and the learning curve) (https://aisotools.com/blog/anytype-review-2026).
- No web-browser version — desktop/mobile only; no real-time collaborative editing to Notion's level; limited third-party integrations (https://tooliverse.ai/tools/anytype, https://softwarefinder.com/collaboration-productivity-software/anytype).
- Design decisions worth borrowing: local-first + p2p + E2E as the default architecture (not a paid add-on); object/relations instead of files-in-folders; key/recovery-phrase identity; "local-only mode" as an explicit setting.

### Features
| Area | Detail |
|---|---|
| Editor | Blocks (rich text, code, embeds), inline objects |
| Data model | Objects with types + relations; sets/collections; graph view |
| Sync | E2E p2p between devices; 1 GB free sync storage; self-host or local-only modes |
| Privacy | User-held keys, open-source clients, no analytics-first posture |
| Collaboration | Shared spaces exist but weaker than cloud rivals (UNVERIFIED exact co-editing behavior) |
| Platforms | Windows, macOS, Linux, iOS, Android (no web) |

### Sentiment
| What people say |
|---|
| Standout strengths: offline speed, genuine data sovereignty, encryption (https://tooliverse.ai/tools/anytype) |
| The object/relation model "takes real time to learn"; first week slower than the app you left (https://tooliverse.ai/tools/anytype) |
| Recovery phrases and technical onboarding scare non-technical users; template library thin vs Notion (https://www.producthunt.com/products/anytype/reviews) |
| Sync complaints: desktop-mobile sync failures and slow sync reported; mobile polish lags (https://www.reddit.com/r/Anytype/comments/1glbel5/desktop_app_wont_sync_with_mobile_app/) |
| UI/UX gripes in PH review tags: limited search, export issues, no multi-tab support (https://www.producthunt.com/products/anytype/reviews) |

### Wants
| What people want changed |
|---|
| Easier onboarding (recovery phrase, mental model), more templates (https://www.producthunt.com/products/anytype/reviews) |
| Multi-tab support, better search, smoother export (https://www.producthunt.com/products/anytype/reviews) |
| More sync storage on free tier (https://tooliverse.ai/tools/anytype) |
| Real-time collaboration on par with cloud tools (https://aisotools.com/blog/anytype-review-2026) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | Unlimited objects, 1 GB sync (https://toolradar.com/tools/anytype/pricing) |
| Pro | $10/mo (was $8, raised Aug 2026) (https://aiproductivity.ai/tools/anytype/) |
| Ultra | $20/mo (was $16) (https://aiproductivity.ai/tools/anytype/) |
| Platforms | Windows, macOS, Linux, iOS, Android |

### Contradictions
- Free sync storage: Toolradar (Oct 2026, from official pricing page) says 1 GB (https://toolradar.com/tools/anytype/pricing); an embedded user quote in Tooliverse says 100 MB (https://tooliverse.ai/tools/anytype). The 1 GB figure matches the official page; 100 MB appears outdated.
- "Radically easier than before" (recent PH reviews) vs persistent "steep learning curve" verdicts from reviewers in the same year (https://www.producthunt.com/products/anytype/reviews, https://thebusinessdive.com/anytype-review) — onboarding is improving but the abstraction cost is real.

Sources: https://aisotools.com/blog/anytype-review-2026 • https://toolradar.com/tools/anytype/pricing • https://tooliverse.ai/tools/anytype • https://www.producthunt.com/products/anytype/reviews • https://github.com/anyproto

## Tana
### Visual surface
- Web/desktop (cloud): an outliner-first workspace — every note is a bullet tree; any node can carry a supertag that gives it structured fields; nodes flow via live searches/queries into other views (tables, boards, calendars, AI chat panels). The visual signature is dense, keyboard-driven outline nesting with typed fields inline (https://outliner.tana.inc/, https://toolchase.com/tool/tana/).
- Product split in 2026: the original outliner lives at outliner.tana.inc, while tana.inc became the agentic meeting platform (transcription, deliverables, voice agents) announced in April 2026 (https://doolpa.com/article/tana, https://www.aipedia.wiki/tools/tana/).
- Tana Capture mobile app feeds the outliner; no fully native mobile editor — mobile experience is a common weakness (https://aiproductivity.ai/tools/tana/).
SHOT-LIST:
- Outliner product hero — https://outliner.tana.inc/
- Main site (meeting product) — https://tana.inc
- Pricing page — https://tana.inc/pricing (search-verified URL)
- Help/learn hub — https://help.tana.inc (search-verified URL)

### Docs analysis
- Supertags: attach a tag to any outline node; the node inherits structured fields (text, dates, references, dropdowns) — schema-on-write over an outline (https://doolpa.com/article/tana).
- Live searches/queries: dynamic lists that pull nodes matching supertags/properties from anywhere (https://outliner.tana.inc/).
- AI: multi-model AI, AI command bar, in-platform agents, AI Meeting Agent with botless live transcription and automated summaries/action items; meeting agent turns calls into deliverables within minutes (https://aiproductivity.ai/tools/tana/, https://aishortcutlab.com/tools/tana/review).
- Pricing (outliner product): Free up to ~1,000 nodes, basic supertags, limited AI credits, single workspace; Plus/Pro from $10/mo (Pro cited with 5,000 AI credits); Tana for Teams and Enterprise above (https://toolchase.com/tool/tana/, https://www.sollmannkann.com/project-management-and-notes/best-tana-review/).
- Meeting product pricing (June 2026): Pro ~$20/mo early-bird (~$30 standard) unlimited meetings; Max ~$80/mo early-bird (~$120 standard) (https://www.aipedia.wiki/tools/tana/).
- Web + desktop apps; capture app on mobile (https://toolchase.com/tool/tana/).
- Design decisions worth borrowing: schema attaches to notes at any point (tag later, structure emerges); information flows to views via queries rather than being filed; outlines as the universal primitive; "notes become structured data" pipeline.

### Features
| Area | Detail |
|---|---|
| Editor | Infinite outliner, nodes as universal unit, inline fields |
| Structure | Supertags (typed schemas), live queries, graph of nodes |
| AI | Command bar, agents, meeting transcription + summaries + action items |
| Capture | Tana Capture mobile, quick-add inbox |
| Views | Table, board, calendar on tagged nodes |
| Platforms | Web, desktop; mobile capture |

### Sentiment
| What people say |
|---|
| Free plan's 5-supertag cap means you cannot test the core feature without paying (https://aishortcutlab.com/tools/tana/review) |
| Learning curve is the make-or-break: "this is where Tana loses most users" (https://aiproductivity.ai/tools/tana/) |
| The meeting agent is called the clearest ROI in the product (https://aishortcutlab.com/tools/tana/review) |
| Overall scores cluster ~4.3-4.4/5 among tool reviewers (https://toolchase.com/tool/tana/, https://toolpilot.tools/tools/tana) |
| The 2026 pivot to meetings confused existing outliner users (inference from the split; UNVERIFIED as a widespread sentiment) (https://doolpa.com/article/tana) |

### Wants
| What people want changed |
|---|
| Lower learning curve / better onboarding (https://aishortcutlab.com/tools/tana/review) |
| Freer free tier for supertags (https://aishortcutlab.com/tools/tana/review) |
| Better mobile experience (https://aiproductivity.ai/tools/tana/) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | ~1,000 nodes, basic supertags, limited AI, single workspace (https://toolchase.com/tool/tana/) |
| Plus/Pro | from $10/mo (outliner) (https://toolchase.com/tool/tana/) |
| Meeting product | Pro ~$20 early-bird / ~$30 standard; Max ~$80 / ~$120 (https://www.aipedia.wiki/tools/tana/) |
| Platforms | Web, desktop (Mac/Windows), Tana Capture on iOS/Android |

### Contradictions
- Two different "Tana" products now exist (outliner vs meeting platform) with different pricing; older reviews (Dec 2025) describe only the outliner with a single AI stack (https://aiproductivity.ai/tools/tana/), while June 2026 sources describe the meeting-platform plans (https://www.aipedia.wiki/tools/tana/). Reviews must state which product they cover.

Sources: https://outliner.tana.inc/ • https://doolpa.com/article/tana • https://toolchase.com/tool/tana/ • https://aishortcutlab.com/tools/tana/review • https://www.aipedia.wiki/tools/tana/

## Reflect
### Visual surface
- Desktop/web + iOS/Android: a minimalist, fast networked-notes app — dark or light, single sidebar (Daily Notes, Maps of Content), editor with Markdown-style formatting, [[double-bracket]] linking, and a tasteful backlink/graph side panel. Reviewers emphasize speed and restraint: daily notes as the default landing surface (https://aitoolscoop.com/tool/reflect/, https://aitoolbeat.com/tools/reflect).
- Mobile works but is desktop-first in feel (https://toolfinder.com/alternatives/reflect-notes).
SHOT-LIST:
- Product hero — https://reflect.app
- Pricing — https://reflect.app/pricing
- App Store listing (mobile UI) — https://apps.apple.com/us/app/reflect-notes-note-taking/id1558040097 (search-verified URL)
- Academy/docs — https://reflect.app/academy (search-verified URL)

### Docs analysis
- Core model: daily notes as inbox, bidirectional backlinks incl. unlinked references, Maps of Content, graph visualization (https://aitoolscoop.com/tool/reflect/, https://www.producthunt.com/products/reflect-notes/reviews).
- AI built in: GPT-4 assistant with predefined + custom prompts, Whisper voice transcription, web article summarization, calendar integration (Google/Outlook) (https://www.buildfastwithai.com/ai-tools/reflect, https://aitoolscoop.com/tool/reflect/).
- E2E encryption (https://toolguide.io/en/tool/reflect-notes/).
- Kindle/browser snippet capture, real-time cross-device sync (https://sourceforge.net/software/product/Reflect/).
- No free plan: 14-day full-feature trial, then one all-inclusive plan — $10/mo monthly or $8.33/mo billed annually ($100/yr) (https://techvernia.com/pages/reviews/productivity/reflect.html).
- Design decisions worth borrowing: opinionated single-plan pricing; daily-notes-first onboarding (app is useful on day one); E2E encryption for a cloud app; speed as a feature.

### Features
| Area | Detail |
|---|---|
| Editor | Rich text with Markdown support, [[wikilinks]] |
| Network | Backlinks, unlinked references, MOCs, graph view |
| Daily notes | Default daily workspace, recurring templates |
| AI | GPT-4 assistant, custom prompts, Whisper transcription, article summarization |
| Integrations | Readwise, calendars, Chrome/Kindle capture |
| Privacy | End-to-end encryption |
| Platforms | Web, macOS, Windows, iOS, Android |

### Sentiment
| What people say |
|---|
| Praised for speed, design and zero-setup networked thinking; a case study of 3,000+ research notes with faster retrieval after switching from folders (https://aitoolscoop.com/tool/reflect/, https://aiforbusinessautomation.com/tools/reflect-review/) |
| "Perfectly" implemented backlinks/daily notes incl. unlinked references (https://www.producthunt.com/products/reflect-notes/reviews) |
| Limited when you want AI beyond search/summarize; mobile apps unexceptional (https://toolfinder.com/alternatives/reflect-notes) |
| Too expensive and too minimalist for students; built for daily-writing professionals (https://toolguide.io/en/tool/reflect-notes/) |

### Wants
| What people want changed |
|---|
| A free tier (none exists) (https://techvernia.com/pages/reviews/productivity/reflect.html) |
| Stronger mobile experience (https://toolfinder.com/alternatives/reflect-notes) |
| Deeper AI (beyond GPT-4 prompts) and team features (https://toolfinder.com/alternatives/reflect-notes, https://aiforbusinessautomation.com/tools/reflect-review/) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | None; 14-day trial (https://techvernia.com/pages/reviews/productivity/reflect.html) |
| Paid | $10/mo monthly; $8.33/mo annual ($100/yr), single all-inclusive plan (https://techvernia.com/pages/reviews/productivity/reflect.html, https://aitoolbeat.com/tools/reflect) |
| Platforms | Web, macOS, Windows, iOS, Android |

### Contradictions
- CostBench's own pages conflict: its pricing page claims "2 plans from Free–$120/year" (https://costbench.com/software/note-taking/reflect/), its free-plan page says "no free plan" (https://costbench.com/software/note-taking/reflect/free-plan/), and it states "$10/year" and "Free to $120 per year" figures that no other source supports (https://costbench.com/software/note-taking/reflect/free-plan/). Weight of evidence: no free plan, $10/mo or $100/yr.

Sources: https://reflect.app • https://techvernia.com/pages/reviews/productivity/reflect.html • https://aitoolscoop.com/tool/reflect/ • https://toolfinder.com/alternatives/reflect-notes • https://www.producthunt.com/products/reflect-notes/reviews

## Milanote
### Visual surface
- Web + desktop apps + iOS/Android: a calm infinite canvas of "boards" that hold notes, images, links, to-dos and files as cards, with drag-and-drop anywhere, board-within-a-board nesting, and shareable client links. The aesthetic is deliberately editorial — card grid, soft shadows, magazine typography — aimed at creative directors and designers rather than facilitators (https://www.softwares.com/software/milanote, https://moodlyextension.com/blog/milanote-alternative-free.html).
- Boards can be exported/shared as clean web links; no graph/backlink machinery at all — it is a spatial organizing tool, not a knowledge network (https://www.gappsy.com/tools/milanote/).
SHOT-LIST:
- Product hero (moodboard) — https://milanote.com
- Pricing page — https://milanote.com/pricing
- Templates gallery (UI variety) — https://milanote.com/templates (search-verified URL)
- Web clipper listing — Chrome Web Store "Milanote Web Clipper" (search-verified)

### Docs analysis
- Free plan is a permanent trial: 100 notes/images/links combined, 10 file uploads, unlimited shared boards, no time limit (https://bookbird.io/software/milanote/, https://checkthat.ai/brands/milanote/pricing).
- Paid from roughly $9.75–12.50/mo (annual vs monthly) per 2026 trackers; Gappsy cites "from $9.99/mo" (https://storyflow.so/blog/pureref-vs-milanote-vs-morpholio-vs-arena-photographer-moodboard-2026, https://www.gappsy.com/tools/milanote/).
- Strengths per reviewers: wide file-type support, easy client sharing, pleasant interface; weak integrations and no automation for enterprise workflows (https://www.spotsaas.com/product/milanote).
- Web clipper + email-in capture; connectors/arrows between cards (per user reviews) (https://www.softwareadvice.com/idea-management/milanote-profile/).
- Design decisions worth borrowing: boards-within-boards as the single hierarchy; card-based universal content; client-ready share links; restraint (few features, polished).

### Features
| Area | Detail |
|---|---|
| Canvas | Infinite boards, nested boards, cards (notes, images, links, files, to-dos) |
| Collaboration | Real-time editing, comments, shared boards |
| Capture | Web clipper, image/file upload, PDF annotation |
| Sharing | Public share links, export |
| Platforms | Web, macOS, Windows apps, iOS, Android |

### Sentiment
| What people say |
|---|
| Beloved by designers/writers as "the genuinely pleasant" ideation space (https://www.softwares.com/software/milanote) |
| Free tier limits "arrive sooner than expected" — the #1 driver of people seeking alternatives (https://moodlyextension.com/blog/milanote-alternative-free.html) |
| Limited integrations and automation frustrate larger teams (https://www.spotsaas.com/product/milanote) |
| Called the best client-facing moodboard tool for photographers; "the board that wins the job" (https://storyflow.so/blog/pureref-vs-milanote-vs-morpholio-vs-arena-photographer-moodboard-2026) |

### Wants
| What people want changed |
|---|
| Bigger free tier (100-card ceiling too tight) (https://checkthat.ai/brands/milanote/pricing) |
| Integrations/automation (https://www.spotsaas.com/product/milanote) |
| Offline/desktop parity (UNVERIFIED — not prominent in sources) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | 100 cards, 10 file uploads, unlimited shared boards, no time limit (https://bookbird.io/software/milanote/) |
| Paid | from ~$9.75-12.50/mo depending on billing (https://storyflow.so/blog/pureref-vs-milanote-vs-morpholio-vs-arena-photographer-moodboard-2026) |
| Platforms | Web, macOS, Windows, iOS, Android |

### Contradictions
- none found

Sources: https://milanote.com • https://checkthat.ai/brands/milanote/pricing • https://bookbird.io/software/milanote/ • https://moodlyextension.com/blog/milanote-alternative-free.html • https://storyflow.so/blog/pureref-vs-milanote-vs-morpholio-vs-arena-photographer-moodboard-2026

## Miro
### Visual surface
- Web + desktop + mobile: the category-defining infinite whiteboard — zoomable canvas covered in sticky notes, frames, shapes, connectors, templates; cursors and presence for real-time collaboration; a left toolbar of creation tools and a bottom timer/vote/facilitation bar. Over 100M users and 7,000+ templates (https://aiproductivity.ai/tools/miro/, https://hackceleration.com/labs/review/miro).
- 2026 evolution: Miro positions as an "Intelligent Workspace" — AI sidekicks (agents on the canvas), prompt-to-prototyping, Miro MCP, TalkTrack async video, AI note-clustering, stickies-to-diagram conversion (https://www.banani.co/blog/miro-pricing, https://droidcrunch.com/miro-review/).
SHOT-LIST:
- Product hero (canvas) — https://miro.com
- Pricing page — https://miro.com/pricing
- Diagramming page — https://miro.com/diagramming/ (per saascrmreview capture)
- Templates page — https://miro.com/templates/

### Docs analysis
- Free plan: 3 editable boards, unlimited members; AI limited; 100 MCP calls/day on Free (https://figr.design/blog/miro-pricing-a4e11, https://saascrmreview.com/miro-pricing/).
- Starter $8/member/mo billed yearly (~$10 monthly); Business ~$20/member/mo; Enterprise custom (https://saascrmreview.com/miro-pricing/, https://match-vs.com/en/tool/miro).
- AI credits: diagrams cost ~5 credits each; stickies-to-diagram; image generation; sidekicks agents (https://saascrmreview.com/miro-review/).
- Visio/Lucidchart import on Starter matters for migrations (https://saascrmreview.com/miro-review/).
- Design decisions worth borrowing: templates as onboarding (7,000+); board-level permission granularity; facilitation tooling (timer, voting); AI that transforms existing content rather than generating from nothing; MCP access to boards for external agents.

### Features
| Area | Detail |
|---|---|
| Canvas | Infinite whiteboard, frames, connectors, sticky notes, shapes |
| Facilitation | Voting, timer, TalkTrack async recording, breakout frames |
| AI | Note clustering, diagram generation, sidekick agents, prompt-to-prototype |
| Integrations | Huge app marketplace (Slack, Jira, Figma, MS/Google), MCP |
| Templates | 7,000+ |
| Platforms | Web, Windows/macOS desktop, iOS, Android |

### Sentiment
| What people say |
|---|
| Product quality is praised: fast canvas, real-time collab "just works," AI can structure sticky walls (https://hackceleration.com/labs/review/miro) |
| Billing pain is the loudest complaint: guests converted to paid members, mid-cycle prorated charges, editing a board flips you to paid, refunds hard to get (https://aigregator.com/tools/miro-ai) |
| Free plan bites: 3 editable boards / only 3 most recent remain editable (https://droidcrunch.com/miro-review/, https://figr.design/blog/miro-pricing-a4e11) |
| G2 ~4.7/5 (~12k reviews); tool-reviewer aggregate 4.3/5 (https://match-vs.com/en/tool/miro, https://aiproductivity.ai/tools/miro/) |

### Wants
| What people want changed |
|---|
| Transparent billing (member vs guest) (https://aigregator.com/tools/miro-ai) |
| Cheaper team tiers / friendlier free plan (https://saascrmreview.com/miro-pricing/) |
| Better performance on huge boards (UNVERIFIED — not prominent in 2026 sources) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Free | 3 editable boards, unlimited members (https://figr.design/blog/miro-pricing-a4e11) |
| Starter | $8/member/mo annual (https://saascrmreview.com/miro-pricing/) |
| Business | ~$20/member/mo (https://saascrmreview.com/miro-pricing/) |
| Enterprise | Custom |
| Platforms | Web, desktop, iOS, Android |

### Contradictions
- User count: Match VS says 90+ million users (https://match-vs.com/en/tool/miro) vs AI:Productivity's 100 million+ (https://aiproductivity.ai/tools/miro/) — likely marketing rounding vs official; UNVERIFIED.
- Free-plan behavior: "3 editable boards" (https://droidcrunch.com/miro-review/) vs "only the three most recent boards remain editable" (https://figr.design/blog/miro-pricing-a4e11) — the latter matches Miro's documented model (older boards become view-only).

Sources: https://miro.com • https://saascrmreview.com/miro-pricing/ • https://aigregator.com/tools/miro-ai • https://hackceleration.com/labs/review/miro • https://figr.design/blog/miro-pricing-a4e11

## Samsung Notes
### Visual surface
- Android (Galaxy phones/tablets): a notebook metaphor — folders of notes with thumbnail previews, a full-screen editor supporting handwriting with the S Pen (pressure, tilt), typed text, drawings, images and PDF annotation layered over imported documents; toolbar of pen/highlighter/eraser/selection; note-view modes (page, continuous, vertical). Designed touch-first (https://www.techjockey.com/us/detail/samsung-notes, https://valuealltech.com/best-note-taking-app-for-samsung/).
- One UI 9 (2026) added Galaxy AI: note summaries, auto-formatting, transcription, and features that work finger-only without the stylus (https://www.makeuseof.com/ive-used-samsung-notes-now-that-i-have-one-ui-9-and-i-was-surprised-at-how-good-it-is/).
- Windows: a Microsoft Store app for Samsung PCs; community workarounds get it running on other PCs, and Samsung's own support pages confirm the app is locked to Galaxy ecosystems (https://www.reddit.com/r/GalaxyTab/comments/1lhrqyf/samsung_notes_for_windows_needs_fixing/, https://eu.community.samsung.com/t5/mobile-apps-services/samsung-notes-on-other-android-devices/td-p/15181009).
SHOT-LIST:
- Official support/owners page (feature overview, OneNote-sync notice) — https://www.samsung.com/us/support/owners/app/samsung-notes
- Samsung Notes ↔ OneNote sync answer page — https://www.samsung.com/us/support/answer/ANS10003444/
- Google Play listing — https://play.google.com/store/apps/details?id=com.samsung.android.app.notes (search-verified URL)
- Galaxy AI notes features page — samsung.com Galaxy AI section (search-verified)

### Docs analysis
- Free; unlimited notes; no subscription tiers (device purchase is the gate) (https://omnicanvasnotes.com/blog/reviews/samsung-notes-alternatives).
- Sync: Samsung Cloud sync between Galaxy devices; sharing/collaboration on shared notes via Galaxy devices (https://www.samsung.com/us/support/owners/app/samsung-notes).
- The "Sync to Microsoft OneNote" option (2018-2026 partnership) was removed after July 2026; Samsung's support page states it is "no longer available" and points to Samsung Cloud instead (https://www.samsung.com/us/support/owners/app/samsung-notes, https://www.sammobile.com/news/samsung-notes-microsoft-onenote-sync-will-stop-working-soon/).
- Galaxy AI caveat documented by Samsung: PDF-overlay translations do not sync, share, save, or back up/restore (https://www.samsung.com/us/support/answer/ANS10003444/).
- Export: PDF, image, text (Word/Microsoft formats via convert-and-share); PDF annotation imports docs (https://www.techjockey.com/us/detail/samsung-notes).
- Password protection, offline access, locked folders (https://www.techjockey.com/us/detail/samsung-notes).
- Design decisions worth borrowing: zero-config capture (notes open instantly, always installed); handwriting as a first-class citizen; per-note formats; device-ecosystem lock-in as the business model — the counter-example for a new app.

### Features
| Area | Detail |
|---|---|
| Editor | Handwriting (S Pen), text, drawings, images, audio annotations |
| Documents | PDF/image annotation and markup |
| AI | Galaxy AI summaries, formatting, transcription, translation overlays |
| Sync | Samsung Cloud across Galaxy devices; OneNote bridge ended July 2026 |
| Security | Password-protected notes/folders |
| Platforms | Galaxy Android devices; Samsung-PC Windows app; no web/iOS |

### Sentiment
| What people say |
|---|
| On Galaxy hardware it is considered excellent — best free S Pen experience; students and stylus users stay (https://valuealltech.com/best-note-taking-app-for-samsung/, https://mindlifeup.com/samsung-notes-review-for-students/) |
| Even non-stylus owners praise the One UI 9 AI polish (https://www.makeuseof.com/ive-used-samsung-notes-now-that-i-have-one-ui-9-and-i-was-surprised-at-how-good-it-is/) |
| Lock-in anger: OneNote sync shutdown left people asking "is there really no way I can access my old Samsung notes beside Samsung device?" (https://www.reddit.com/r/GalaxyTab/comments/1u3nzzz/galaxy_notes_one_note_sync_will_be_discontinued/) |
| Windows app called "unbelievably bad" — Samsung-PC gating, broken sync (https://www.reddit.com/r/GalaxyTab/comments/1lhrqyf/samsung_notes_for_windows_needs_fixing/) |
| Sync bugs between phone and tablet reported; advice: don't edit simultaneously (https://www.reddit.com/r/samsungnotes/comments/1jujnhw/why_my_notes_arent_properly_synced_between_phone/) |

### Wants
| What people want changed |
|---|
| Cross-platform access (non-Galaxy Android, web, iOS) (https://eu.community.samsung.com/t5/mobile-apps-services/samsung-notes-on-other-android-devices/td-p/15181009, https://www.reddit.com/r/GalaxyTab/comments/1hu2p2e/for_people_who_dont_use_samsung_notes_why_dont/) |
| A replacement for the OneNote bridge / better desktop app (https://r1.community.samsung.com/t5/galaxy-s/notes-sync-with-onenote-going-away-too/td-p/37870600) |
| More reliable sync (https://www.reddit.com/r/samsungnotes/comments/1o5l8wg/samsung_notes_sync_issues/) |

### Pricing and platforms
| Item | Detail |
|---|---|
| Price | Free, no tiers (https://omnicanvasnotes.com/blog/reviews/samsung-notes-alternatives) |
| Platforms | Galaxy Android devices (phone/tablet/Book), Samsung-PC Windows app; no web/iOS (https://www.samsung.com/us/support/owners/app/samsung-notes) |

### Contradictions
- The Gadget Hacks/SamMobile coverage (April 2026) framed OneNote sync as "ending July 2026" (https://samsung.gadgethacks.com/news/samsung-notes-onenote-sync-ending-july-2026-what-galaxy-users-should-do/), and Samsung's support page now confirms it is already gone (https://www.samsung.com/us/support/owners/app/samsung-notes) — a commonly-believed "Samsung Notes syncs with OneNote" fact (still repeated in some older reviews, e.g. Techjockey's collaboration claims) is no longer true as of late 2026.

Sources: https://www.samsung.com/us/support/owners/app/samsung-notes • https://www.samsung.com/us/support/answer/ANS10003444/ • https://www.sammobile.com/news/samsung-notes-microsoft-onenote-sync-will-stop-working-soon/ • https://www.reddit.com/r/GalaxyTab/comments/1lhrqyf/samsung_notes_for_windows_needs_fixing/ • https://www.makeuseof.com/ive-used-samsung-notes-now-that-i-have-one-ui-9-and-i-was-surprised-at-how-good-it-is/

LANE B COMPLETE — 12 apps covered

## Video evidence supplements

Video coverage was researched in a fresh pass (searches per app, October 2026). Note the general pattern first: for every app in this lane, videos show two things text never captures — the actual latency and feel of real-time interaction (multiplayer cursors, stylus strokes, block-dragging) and the messy "how someone actually organizes a vault/board" workflow that official docs sanitize. Comment threads, meanwhile, are systematically harsher about pricing, sync and lock-in than reviewers are.

### Obsidian
Video is Obsidian's biggest community engine: the r/ObsidianMD subreddit functions as a comment section for YouTube videos (e.g., No Boilerplate's "Obsidian: The Good Parts" and a popular 2023 thread asking why Obsidian YouTube videos are so numerous — commenters answer "free + graph view + linking" (https://www.reddit.com/r/ObsidianMD/comments/15hne20/)). Video shows what docs can't: plugins like Dataview, Waypoint and a community 3D graph running in real workflows, and even Obsidian's CEO (kepano) showing up in the comments of a plugin-author's walkthrough (https://www.reddit.com/r/ObsidianMD/comments/17j2lac/). Video-first tutorials such as "Learn Obsidian in One Video" cover Quick Switcher, Canvas and hotkeys as motion, which text docs flatten. What commenters gripe that reviewers omit: the graph view is called "meaningless"/"only good for social media" by skeptics even inside fan threads (echoed on HN: "the local graph has real uses, but the global one is mostly to see structure and look cool"), reviewers' factual slips get corrected in comments (folders DO appear in graphs via plugins), and HN threads on the 2020 Show HN launch and a student-built open-source sync server surface the $8/mo Sync price as the recurring unspoken cost (https://news.ycombinator.com/item?id=37247767).

### Obsidian Publish
No meaningful official demo video exists; Publish's video coverage is entirely community-made digital-garden tutorials, which is itself telling — the workflow people need video for is setup (GitHub/deployment confusion), not daily publishing. The most useful is a complete "Obsidian Digital Garden Tutorial (Publish Alternative) for Non-Technical Users" walkthrough on r/ObsidianMD (https://www.reddit.com/r/ObsidianMD/comments/1l05q4y/), and the Flowershow team's demo video showing Bases-powered dynamic views rendered on a published site — a capability walkthrough more current than most text reviews (https://forum.obsidian.md/t/flowershow-publish-your-obsidian-vault-as-a-website-hosted-edition/105957). What video shows that docs miss: the mobile "Publish changes" slide-up flow and how slow the republish-to-web loop feels in practice. Comment threads under these videos gravitate to the price ($8–10/mo per site) and to free alternatives (the digital garden pipeline, Flowershow), a gripe the official pages never mention.

### OneNote
Official video is Microsoft's Copilot tutorial set — short support videos on summarizing notes into to-do lists and generating outlines, plus third-party Copilot walkthroughs like Learnit Training's 29-minute tutorial (https://support.microsoft.com/en-us/microsoft-365-copilot/copilot-tutorial-summarize-and-identify-to-do-items-with-copilot-in-onenote). The videos demonstrate a workflow docs underplay: Copilot lives in a ribbon pane AND an on-canvas icon, so you summarize a page without leaving it. Beyond Copilot, OneNote has little of the influencer-review video culture its rivals have; reviewers note users discover it bundled rather than by watching a video. Comment threads (HN) carry the real signal: praise as a "loss-leader... impossible to compete with on Windows" alongside gripes that it is bad at linking notes and weak at organizing as notebooks grow, that the UI "never clicked" for iPad/Pencil users, and a recurring dispute over whether "free" secretly requires OneDrive storage (https://news.ycombinator.com/item?id=36611325). Reviewers omit the organizational ceiling; commenters don't.

### Evernote
Evernote's own channel now leads with a video presenting the v11 highlights (115+ improvements since the Bending Spoons takeover) and AI features (AI Transcribe turning audio, video and images into editable text) (https://evernote.com/blog/115-improvements-since-v11); G2 hosts user video reviews and The Business Dive's video-format testing review. What video shows that text misses: how much of the 2026 product is surface polish — faster editor, new capture — layered on the old notebook model, and video testers confirm AI transcription works "as a secondary feature" only. The comment threads are where the real story lives: HN threads on the takeover and a September 2026 "My last six months at Evernote" post from an ex-employee, plus Reddit's r/Evernote Bending Spoons threads, gripe about price hikes, fired US staff, and a free tier reduced to "try before you buy" (https://news.ycombinator.com/item?id=49672342). Notably, even commenters concede "the app has gotten better in the last 2 years" — a nuance almost no polished review includes, and the biggest thing official videos omit is the takeover context itself.

### Notion
Notion has the largest video-tutorial ecosystem in this lane — Capterra reviewers explicitly describe learning it through "many YouTube videos to develop your own unique system," and video reviews like Hack'celeration's 3-year test show relational databases, kanban/calendar views and rollups in motion, quantifying what text can't: databases take 2–3 weeks of daily use to feel natural, complex workflows ~6 weeks (https://hackceleration.com/notion-review/). Video also exposes what docs sanitize: load times on big pages and the actual number of clicks template-heavy work takes. Comment threads invert the review tone: HN's "Notion's mid-life crisis" and Notion 3.0 threads call it "a jack of all trades and master of none" with flexibility as "a cognitive overhead," gripe that a 15-second empty-page load drove one team to cancel, and recall "people not knowing where to place new pages" at a 20-person org (https://news.ycombinator.com/item?id=41683577). Videos (often affiliate-funded) sell the template magic; commenters gripe about performance, feature creep and data lock-in — the trade-offs reviewers bury.

### Craft
Craft's own YouTube channel is the main official video source, supplemented by walkthroughs per use case and a 10-minute "watch me make a document" demo by a Substack reviewer (https://wondertools.substack.com/p/craftapp). What video shows that screenshots can't: the native (non-Electron) speed — instant document open, smooth drag-and-drop styling, full offline behavior, and the iPad pencil workflow that is Craft's best differentiator; Craft's 2026 comparison page itself leans on "loads instantly with thousands of documents" as the video-provable claim. One review critique aimed at Craft's own videos: they lack narration or on-screen direction, so the YouTube channel fills the gap but casual viewers bounce (https://originality.ai/blog/craft-docs-ai-creator-review). Comment threads (Product Hunt, r/NoteTaking) gripe about what reviewers omit: no databases, weaker structure than Notion, and that "best writing experience on Mac" means lock-in to Apple platforms — the simplicity is also the ceiling.

### Anytype
Anytype's video story improved recently: after years of sparse footage (a 2020 alpha demo, a 2023 community demo video), the team "finally stepped up their YouTube game" with a basics video in early 2026 that Reddit praised as "straight to the point and includes some nice demos" (https://www.reddit.com/r/Anytype/comments/1qslqtl/). The Business Dive's video review shows the defining workflow behavior — spaces, object types and P2P sync running locally and offline, snappier than Notion — but also records the churn that text reviews bury: the app "loses 90% of new users, as they become frustrated after a few days" (https://thebusinessdive.com/anytype-review). Comment threads do the critical work reviewers skip: r/Anytype's "most circumvoluted and complicated app" thread, and commenters noting the app "promised local first but it was not local first when released" — a broken-promise grievance that official videos never address.

### Tana
Tana's video coverage is unusually course-shaped: the official "Tana Learn Live" sessions demo supertags and fields interactively, and a whole paid-course economy exists (Unlock Tana, Ev Chapman's Fast Track) because — as the course copy admits — people otherwise spend "hundreds of hours watching YouTube tutorials" and still mess up their workspace (https://tana.inc/articles/tana-learn-live-supertags-and-fields). Videos show what makes Tana different from outliner screenshots: the node IS the tag, so supertags, fields and live search surface structure as you type — mechanics that genuinely require motion to grasp. Comment threads uniformly report what reviews soften: the learning curve is the steepest in the lane ("The learning curve for making any customizations or filters is immense... I feel the learning curve is STEEP"), and even daily users admit an "average daily user trying to log meeting notes or a recipe" will struggle (https://www.reddit.com/r/TanaInc/comments/17yof8u/). On HN, a 2022 thread comparing supertags to Notion's model remains the clearest outside explanation of the concept (https://news.ycombinator.com/item?id=33429692). Commenters also note the pivot risk: the site now leads with AI-meeting positioning, which the tutorial ecosystem hasn't caught up with.

### Reflect
No meaningful video coverage exists: searches surface no official demo/tutorial video library, no major YouTube walkthroughs, and no video reviews of note — Reflect communicates through its Reflect Academy newsletter, blog posts with GIF-level demos (voice memo widget, Whisper transcription), and text reviews (https://reflect.academy/audio-recordings). Its one video-adjacent strength, voice-to-note capture, is documented in writing rather than shown in film, so video's usual job here (showing latency and capture flow) is unfilled. Thread coverage is equally thin: a 2023 r/ProductivityApps thread is explicitly a request for reviews ("I have not found maybe reviews or others using it"), and Product Hunt comments are short praise for speed and AI. The gripes commenters raise that reviewers omit: the passwordless email-link login (one in-depth text review's main complaint), weak single-note export, and a small user base that makes community troubleshooting scarce (https://curtismchale.ca/2023/05/31/in-depth-look-at-reflect-app/).

### Milanote
Milanote's official channel is guides and templates rather than videos; its video footprint is largely indirect — YouTube sponsorships. Multiple user reviews state they discovered the product through YouTube sponsor clips or "a recommendation of a youtuber" (Trustpilot, Software Advice), and Tool Finder's founder (450K YouTube subscribers) tests it on camera; TrustRadius also links a "Milanote for meetings" YouTube demo. What video shows that text misses: the drag-and-drop feel of mixing images, links, swatches and notes on one board, and the web clipper's "Unsorted" holding column that official guides underemphasize. Comment threads fill the gaps: the r/PKMS review thread details the free tier's 100-card / limited-upload wall ("already out of space for file uploads and would need to subscribe"), and HN's 2017 Show HN thread records the original workflow claim users still repeat — replacing "an entire wall of post-its and half a dozen moleskines" (https://news.ycombinator.com/item?id=13587909). Grips reviewers omit: weak mobile apps, no offline, no edit history, and a pricing gap versus alternatives (https://nubiapage.com/milanote-review-2026-download-alternatives-login-free-plan-pricing/).

### Miro
Miro has the most official video of any app here: a YouTube channel of 500+ videos, Miro Academy courses, and a famous community-made 1-hour walkthrough with per-function timestamps (https://community.miro.com/inspiration-and-connection-67/1-hour-miro-walkthrough-tutorial-3106). Video shows the thing Miro sells and screenshots can't: real-time multiplayer (multiple cursors), facilitation mechanics — voting, timers, sticky-note clustering — and Talktrack's async voice/video walkthroughs of boards. Community video also reveals niche-but-real workflows outside docs: TTRPG groups running campaigns on Miro boards as a free VTT. Comment threads converge on two gripes reviewers soft-pedal: the free plan's "3 boards per team, not 3 each," with older boards silently flipping to view-only (https://www.lilachbullock.com/how-to-use-miro/), and price ("still Expensive AF if you want to upgrade"). HN's dominant 2026 thread isn't about workflow at all: the $1.355B Bending Spoons acquisition of Miro, where even critics concede "great whiteboarding tool though" and users immediately discuss exit paths — an acquisition anxiety absent from every official video (https://news.ycombinator.com/item?id=49643848).

### Samsung Notes
There is no polished official video library; the closest is Samsung's developer channel and SamMobile's hands-on screen recordings and video breakdowns (e.g., the One UI 8.5 Samsung Notes redesign, and an MP4 screen-recording demo of the selection-tool lasso change) (https://www.sammobile.com/news/here-is-how-one-ui-8-5-is-reshaping-samsung-notes/). Student TikTok/YouTube content is the de facto tutorial layer. What video shows that no text can: actual S Pen latency, palm rejection, and handwriting-into-text conversion speed on specific hardware — the make-or-break factors for its student audience, which screenshots and spec sheets flatten. Comment threads do the honest work: r/GalaxyTab's handwriting-improvement thread (39 votes, 42 comments) exposes that many users have mediocre hardware variants without palm rejection or pressure sensitivity, and the handwriting-keyboard thread confirms recognition works well only in the right mode (https://www.reddit.com/r/GalaxyTab/comments/1v9hjri/). Reviewers omit the gripes commenters lead with: sync unreliability between phone and tablet, the discontinued OneNote bridge stranding notes in the Galaxy ecosystem, and the "unbelievably bad" Windows app.

VIDEO SUPPLEMENT COMPLETE — B: 12 of 12 apps covered
