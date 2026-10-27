# Round 12 — Lane E (evidence enrichment)

Apps: Dillinger, Homebrewery, Ghost, Proofeditor, CapCut, Descript, LumaFusion

## Dillinger

### Visual surface

Web (dillinger.io): a two-pane writing surface — Monaco-based editor (the VS Code engine) on the left with syntax-highlighted markdown, and a live rendered preview on the right with scroll sync between panes. The marketing site stresses a chrome-light shell: top nav (Features / AI / Integrations / Guide / Compare / Open Editor), dark mode toggle, zen mode that strips everything but the writing area, and Vim/Emacs keybinding modes in settings <cite index="p5w-1"></cite>. No signup screen sits in front of the editor; the app opens straight into an untitled document with local autosave and no account required <cite index="vi4-1"></cite>. Positioning has shifted visibly: the site's hero copy now sells Dillinger as "AI-ready," framing markdown as the interchange format for LLM prompts <cite index="p5w-1"></cite>.

Desktop: no native desktop app; it is a browser tool (an old Electron wrapper of the AngularJS era existed, not evidenced on the current site). Mobile: browser-based, "mobile-ready" is legacy positioning; current site makes no responsive-layout claims. UNVERIFIED whether the current Next.js build ships a PWA/offline install — the FAQ says "after the initial load, the editor continues to work without an internet connection" <cite index="vi4-1"></cite>, but I could not confirm an installable PWA manifest.

Shot-list (screens visible for capture):
- Editor with live preview (hero screen): https://dillinger.io/ (click "Open Editor" → the editor surface itself; also visible in screenshots embedded on the features page)
- Features grid page: https://dillinger.io/features
- AI positioning page: https://dillinger.io/ai
- Integrations page: https://dillinger.io/integrations
- Comparison/StackEdit page: https://dillinger.io/compare
- Guide page (best-online-markdown-editor): https://dillinger.io/guide/best-online-markdown-editor
- GitHub repo README (code-level view): https://github.com/joemccann/dillinger

### Docs analysis

- Docs live as the site's marketing/features pages plus the GitHub README; there is no separate docs center. Capabilities per README: Monaco editor with markdown syntax highlighting and image paste support; real-time preview with scroll sync; zen mode via Cmd/Ctrl+Shift+Z; drag & drop for .md/.txt/.markdown; autosave to local persistence; export to Markdown/HTML/PDF; OAuth cloud integrations for GitHub, Google Drive, Dropbox, OneDrive, Bitbucket (each needs OAuth callback config at /api/{provider}/callback for self-hosting) <cite index="16x-1"></cite>.
- Editor architecture worth borrowing: the app is built as Next.js 14 + Monaco + Tailwind + Zustand state + Lucide icons, i.e. editor-core (Monaco) decoupled from a thin Zustand store; "writing tools should disappear" is the stated philosophy <cite index="16x-1"></cite>. For a notes app this is the pattern of a single-mode editor (no plugin system at all) that leans entirely on the host editor's ergonomics — no extensions, no transcript model, no rendering pipeline beyond markdown-to-HTML with preview sync.
- Hard limits: 5 cloud providers only, export limited to three formats (no custom export templates); no user accounts on the product itself (accounts only exist at the third-party cloud providers) <cite index="vi4-1"></cite>. Cloud sync is file save/load per provider, not continuous document sync.
- Test/quality infra is unusually formal for a small OSS editor: 294 Vitest unit/integration tests + 39 Playwright E2E tests, 98% coverage, organized by lib/store/hooks/components/routes/e2e — a borrowable practice for a notes app that edits user text <cite index="16x-1"></cite>.
- UNVERIFIED: SourceForge/Slashdot 2026 listing claims 12 AI editing actions, publishing with custom URLs, document sharing, a Chrome extension for in-page conversion, an MCP server, and a 13-endpoint REST API with a 5-document free tier and Pro at $8/month <cite index="w6d-1"></cite>. None of this appears on dillinger.io or the GitHub README as of my fetch; treat as unconfirmed (possibly a separate commercial relaunch or stale/marketing copy).
- UNVERIFIED: the legacy AngularJS feature set (Tablet/mobile layout, gist import, Google Docs→markdown conversion) is no longer visible in current docs <cite index="gz3-3"></cite>.

### Features

| Area | Detail |
|---|---|
| Editor core | Monaco (VS Code engine): syntax highlighting, multiple cursors, find/replace, autocomplete (https://dillinger.io/features) |
| Preview | Live side-by-side rendered markdown, scroll-synced (https://dillinger.io/features) |
| Documents | Single-document focus; autosave to browser local storage, no accounts (https://dillinger.io/) |
| Import | Drag & drop .md, .txt, .markdown, HTML, images; auto-conversion (https://dillinger.io/features) |
| Export | Markdown, styled HTML, PDF (https://dillinger.io/features) |
| Cloud sync | GitHub, Dropbox, Google Drive, OneDrive, Bitbucket via OAuth; per-file save/load (https://dillinger.io/features) |
| Focus modes | Zen mode fullscreen (Cmd/Ctrl+Shift+Z); dark/night mode (https://github.com/joemccann/dillinger) |
| Keybindings | Vim and Emacs modes in settings (https://dillinger.io/features) |
| AI | "AI-ready" positioning for LLM prompt authoring; UNVERIFIED 12 AI actions + MCP server per SourceForge (https://dillinger.io/ai; https://sourceforge.net/software/product/Dillinger/) |
| Extensibility | None on the product itself; OSS repo MIT, self-hostable Next.js app (https://github.com/joemccann/dillinger) |
| Platforms | Web only (https://dillinger.io/) |

### Sentiment

| What people say |
|---|
| Longtime users found the original site effectively dead/suspicious in March 2025: an r/Markdown thread claims dillinger.io "is phishing user data, a shame because it was a great markdown notetaking interface" and asks for alternatives (https://www.reddit.com/r/Markdown/comments/1jj3hcn/dillingerio_alternative/) |
| r/webdev thread "Dillinger.io suspected of Phishing?" (March 2025): users noted the live homepage no longer matched the Wayback archive of the classic app, so many browser-warning-wary users abandoned it (https://www.reddit.com/r/webdev/comments/1jfwy14/dillingerio_suspected_of_phising/) |
| A 2025 r/Markdown "best markdown editor" thread skips Dillinger because the poster "had many problems with it," though liking the browser-window concept (https://www.reddit.com/r/Markdown/comments/1jz8r60/best_markdown_editor_app/) |
| Markdown Guide's tool review praises the split-pane markdown support but says export options are not customizable and file saving is "a bit flaky" (https://www.markdownguide.org/tools/dillinger/) |
| A Dec 2025 It's FOSS community thread shows users still discovering and self-hosting it from GitHub (Node.js 10 era code) (https://itsfoss.community/t/has-anyone-used-the-dillinger-markdown-editor/15238/25) |

### Wants

| What people want changed |
|---|
| Trust back: users wanted clarity on who runs dillinger.io after the 2025 phishing suspicion and site relaunch (https://www.reddit.com/r/webdev/comments/1jfwy14/dillingerio_suspected_of_phising/) |
| Reliable multi-file saving; the flaky file save and non-customizable export are the recurring complaints (https://www.markdownguide.org/tools/dillinger/) |
| A saved workspace across sessions rather than one untitled document; competitor MDflow markets exactly this gap (workspace with sync, sharing, comments, API, remote MCP) (https://mdflow.cz/compare-markdown-editors/dillinger-alternative) |

### Pricing and platforms

| Item | Detail |
|---|---|
| Price | Free, no paid tiers, no signup per official site FAQ; UNVERIFIED counter-claim of Pro $8/month with 5-doc free tier per SourceForge/Slashdot (https://dillinger.io/; https://sourceforge.net/software/product/Dillinger/) |
| OSS | MIT license, self-hostable Next.js 14 app (https://github.com/joemccann/dillinger) |
| Platforms | Web browser; works offline after first load; no native app (https://dillinger.io/) |

### Contradictions

- The official site says "completely free… no paid tiers" and open source (https://dillinger.io/), while 2026 SourceForge/Slashdot listings describe a Pro tier at $8/month, 5-document free cap, AI actions, MCP server, Chrome extension and REST API (https://sourceforge.net/software/product/Dillinger/). Either a commercial relaunch exists that the site FAQ doesn't reflect, or the aggregator copy is wrong.
- The GitHub repo README now describes Next.js 14 + Monaco (https://github.com/joemccann/dillinger), while Slashdot/SourceForge and legacy memory describe Dillinger as AngularJS (https://slashdot.org/software/p/Dillinger/). The codebase was visibly rewritten.
- Reddit March 2025 users suspected the relaunched site of phishing vs. the archived original (https://www.reddit.com/r/webdev/comments/1jfwy14/dillingerio_suspected_of_phising/), while current site docs present a free, offline-capable, privacy-framing product (https://dillinger.io/). The trust history contradicts the current marketing.

Sources: https://dillinger.io/ · https://dillinger.io/features · https://dillinger.io/ai · https://github.com/joemccann/dillinger · https://www.markdownguide.org/tools/dillinger/ · https://sourceforge.net/software/product/Dillinger/ · https://www.reddit.com/r/webdev/comments/1jfwy14/dillingerio_suspected_of_phising/ · https://www.reddit.com/r/Markdown/comments/1jj3hcn/dillingerio_alternative/ · https://mdflow.cz/compare-markdown-editors/dillinger-alternative · https://itsfoss.community/t/has-anyone-used-the-dillinger-markdown-editor/15238/25

---
## Homebrewery (The Homebrewery, NaturalCrit)

### Visual surface

Web (the only platform): the core screen is a split-pane editor — markdown source on the left with syntax highlighting, a live paginated "brew renderer" on the right that displays the document as D&D-book-style pages (two-column, ornate headings, stat blocks) <cite index="m8h-1"></cite>. The editor surface carries a snippet bar (PHB, tables, images, fonts, licenses snippets), tabs for TEXT EDITOR / STYLE (CSS) / SNIPPETS (custom) / SETTINGS, a Properties menu (title, description, tags, theme, thumbnail, language, co-authors), a HISTORY button for local backups, and a draggable divider with jump/sync-scroll buttons <cite index="wmk-1"></cite>. Around the editor sits the site shell: home page with recent/community brews, a per-user BREWS page, and the VAULT — a searchable catalog of all published brews, recently re-skinned with dark mode and alternate views <cite index="wmk-1"></cite>. There is no native app; mobile viewing is supported but mobile editing is explicitly not recommended (cover pages are excluded from ToC "editing on mobile is still not recommended") <cite index="wmk-1"></cite>.

Shot-list:
- Home page (marketing/community surface): https://homebrewery.naturalcrit.com/
- New brew editor (the split-pane + snippet bar + Properties): https://homebrewery.naturalcrit.com/new/
- Vault search/browse: https://homebrewery.naturalcrit.com/vault
- Example user page (published brews grid): https://homebrewery.naturalcrit.com/user/ezekieljd
- FAQ page (in-app help): https://homebrewery.naturalcrit.com/faq
- Migrate (Legacy→V3 guide): https://homebrewery.naturalcrit.com/migrate
- Changelog as rendered document (shows the app's own typography): https://github.com/naturalcrit/homebrewery/blob/master/changelog.md

### Docs analysis

- Document model: a brew is a single markdown text plus a separate CSS "style" block plus metadata (title, description, tags, renderer, theme, thumbnail, language, authors). Input is Markdown + HTML + CSS; the parser emits HTML+CSS with a theme applied, so the "distinctive D&D flavor" is a stylesheet layer over a markdown pipeline <cite index="m8h-1"></cite>. Two renderers coexist: Legacy and V3 (default since v3.2.0), selectable per document in Properties — a borrowable migration pattern where a rendering engine change is opt-in per document and old documents keep rendering <cite index="wmk-1"></cite>.
- "Markdown+" extension syntax is a design decision worth borrowing: divs/spans via `{{class,#id,color:red ...}}` curly blocks, inline style injection `{myClass}`, definition lists via `::`, super/subscripts, extended tables (colspan/rowspan, multiple header rows), `\page`/`\column` pagination control, and page-level CSS via `\page{myStyles}` — a small, learnable syntax that removes the need for raw HTML <cite index="wmk-1"></cite>.
- Variables system: `$[var]` template variables with hoisting (values defined later in the document can be resolved earlier) and a math handler (`$[varA + var2 * 2]`, abs/sign functions) — variables defined as `[var]:content` blocks, output as markdown <cite index="wmk-1"></cite>.
- Theme system: brews tagged `meta:theme` can be selected as a Theme by other brews (style layering supported); a Blank theme exists as a base; shareable published themes are planned <cite index="wmk-1"></cite>.
- Snippet system: the editor exposes a large hierarchical snippet library that inserts templated markdown; users can define their own snippets in a SNIPPETS tab, and custom snippets travel with custom themes <cite index="wmk-1"></cite>. This is a plugin-lite architecture: extension = markdown snippets + CSS theme, no JS.
- Security decision: scripts in brews are now blocked/neutralized on both editor and share paths (two independent fixes in v3.23.0) — user HTML/CSS is allowed, JS is not <cite index="wmk-1"></cite>.
- Persistence: dual storage — Homebrewery's MongoDB or the author's own Google Drive; transfer between them keeps share/edit links and metadata; saves now send diffs instead of full files to cut timeout errors; brew payloads are compressed on save <cite index="wmk-1"></cite>. Local automatic backups: up to 5 snapshots per brew kept in the browser, restorable from a HISTORY button <cite index="wmk-1"></cite>.
- Rendering pipeline details: partial page rendering (only the edited page re-renders), lazy image loading, an iframe-based brew renderer (title added for a11y), and print-to-PDF via the browser with dedicated print styles and page sizes (A3/A4/A5/Card, ink-friendly mode) <cite index="wmk-1"></cite>.
- Sharing/publishing: share links, deep links to page anchors (`#p4`), a metadata API endpoint `/metadata/:shareId`, a `/css/:shareId` route for extracting styles, view counts (owner views excluded), and the Vault as a search index of published brews <cite index="wmk-1"></cite>.
- Self-hosting is a first-class path: MIT license, Node 16+, MongoDB required, Docker and FreeBSD install docs, offline use at localhost:8000, and the standalone PHB stylesheet extractable via `npm run phb` <cite index="799-1"></cite>. Markdown+ extensions are being extracted into separate NPM packages for reuse by other projects <cite index="wmk-1"></cite>.
- Editor is CodeMirror 6 (multiple v3.22 fixes "with Codemirror 6") <cite index="wmk-1"></cite>.
- UNVERIFIED: exact current document size limits (some old reports of long-line server crashes; changelog shows compress + diff saves addressing save limits) <cite index="wmk-1"></cite>.

### Features

| Area | Detail |
|---|---|
| Editor | Split-pane source + live paginated preview; CodeMirror 6; syntax highlighting; code folding; multiple editor themes (Darkvision, Darkbrewery) (https://github.com/naturalcrit/homebrewery/blob/master/changelog.md) |
| Document model | Markdown text + CSS style tab + metadata (tags, theme, thumbnail, language, renderer, co-authors) (https://github.com/naturalcrit/homebrewery) |
| Renderers | Legacy and V3 per-document; V3 "Markdown+" syntax (curly divs/spans, def lists, tables, `\page`/`\column`) (https://github.com/naturalcrit/homebrewery/blob/master/changelog.md) |
| Themes | Brew-as-theme, `meta:theme` tag, Blank base theme, layering (https://github.com/naturalcrit/homebrewery/blob/master/changelog.md) |
| Snippets | Hierarchical built-in snippet bar; user-defined snippets in SNIPPETS tab (https://github.com/naturalcrit/homebrewery/blob/master/changelog.md) |
| Variables | `$[var]` with hoisting and math; auto page-number variable `$[HB_pageNumber]` (https://github.com/naturalcrit/homebrewery/blob/master/changelog.md) |
| Pagination | Page/column breaks, cover pages, page sizes A3/A4/A5/Card, print/PDF pipeline, view modes single/two-page/grid (https://github.com/naturalcrit/homebrewery/blob/master/changelog.md) |
| Sharing | Share links, page anchors, view counts, publish to Vault, metadata API `/metadata/:shareId` (https://github.com/naturalcrit/homebrewery/blob/master/changelog.md) |
| Storage | Homebrewery Mongo or author's Google Drive; transfers preserve links; diff-based saves; compressed payloads; 5 local browser backups per brew (https://github.com/naturalcrit/homebrewery/blob/master/changelog.md) |
| Security | Script execution blocked in brews; CSS sanitization in style editor (https://github.com/naturalcrit/homebrewery/blob/master/changelog.md) |
| Collaboration | Co-authors (invite by username), owner-only editing, co-author removal (https://github.com/naturalcrit/homebrewery/blob/master/changelog.md) |
| Platforms | Web only; self-hostable MIT app (https://github.com/naturalcrit/homebrewery) |

### Sentiment

| What people say |
|---|
| Editor lockups are a recurring theme: a user whose brew "just stopped working" and froze for 20+ minutes after pasting content (https://www.reddit.com/r/homebrewery/comments/1ctts2p/brew_no_longer_working_cant_make_new_brew/) |
| Steep learning curve: "I'm struggling with homebrewery and grasping it's concepts… when I go to the style editor I find I can't switch back which makes it frustrating" (https://www.reddit.com/r/homebrewery/comments/1ldieda/help/) |
| Access-control scares: a user lost editor access to their own brews overnight ("The current logged in user does not have editor access to this brew") (https://www.reddit.com/r/homebrewery/comments/1064o2q/the_current_logged_in_user_does_not_have_editor/) |
| Print/PDF fidelity gaps: pages duplicating on PDF/share output while the editor preview looked fine (https://www.reddit.com/r/homebrewery/comments/b1vwbp/for_some_reason_on_the_editing_page_my_brew_looks/); other PDF tools failing to read parts of exported PDFs (https://www.reddit.com/r/homebrewery/comments/ov2m5s/master_pdf_editor_doesnt_read_some_parts_of_a_pdf/) |
| Style-injection bugs: a bug in the style injector broke brews around v3.13 and a second bug was confirmed by a developer afterwards (https://www.reddit.com/r/homebrewery/comments/1dr1sx9/v3130/) |
| Active, responsive maintainers: in a Jan 2026 thread the team reported a fix for accented-character save errors shipped about a week after report (https://www.reddit.com/r/homebrewery/comments/1q1p1gw/homebrewery_in_2025/) |

### Wants

| What people want changed |
|---|
| Faster, more forgiving editor on large brews and paste (https://www.reddit.com/r/homebrewery/comments/1ctts2p/brew_no_longer_working_cant_make_new_brew/) |
| Lower learning curve and reversible style-editing UX (https://www.reddit.com/r/homebrewery/comments/1ldieda/help/) |
| WYSIWYG parity between editor preview and print/PDF/share output (https://www.reddit.com/r/homebrewery/comments/b1vwbp/for_some_reason_on_the_editing_page_my_brew_looks/) |
| Robust access recovery for self-locked brews (https://www.reddit.com/r/homebrewery/comments/1064o2q/the_current_logged_in_user_does_not_have_editor/) |
| True .md export (an open issue asks for an .md export option; current .txt download is brew markdown preceded by two code-fenced blocks for metadata/style) (https://github.com/naturalcrit/homebrewery/issues/4845) |

### Pricing and platforms

| Item | Detail |
|---|---|
| Price | Free; no paid tier for the tool itself (NaturalCrit sells unrelated D&D content) (https://www.naturalcrit.com/) |
| OSS | MIT-licensed, self-hostable with Node 16+ and MongoDB, Docker/FreeBSD docs (https://github.com/naturalcrit/homebrewery) |
| Platforms | Web; mobile viewing supported, editing discouraged (https://github.com/naturalcrit/homebrewery/blob/master/changelog.md) |

### Contradictions

- Common picture says "Homebrewery is just a pretty markdown editor." The changelog shows a far deeper system: template variables with math and hoisting, brew-as-theme layering, user-defined snippets, a published-brews search engine (Vault), and a metadata API (https://github.com/naturalcrit/homebrewery/blob/master/changelog.md).
- Common belief is "editing on mobile works." The maintainers explicitly recommend against mobile editing (https://github.com/naturalcrit/homebrewery/blob/master/changelog.md).
- UNVERIFIED counter-claim: the r/homebrewery wiki describes the parser as Markdown+HTML+CSS in → HTML+CSS out (https://www.reddit.com/r/homebrewery/wiki/index/); I could not load the wiki directly (403) to confirm its current wording.

Sources: https://github.com/naturalcrit/homebrewery · https://github.com/naturalcrit/homebrewery/blob/master/changelog.md · https://homebrewery.naturalcrit.com/vault · https://www.reddit.com/r/homebrewery/wiki/index/ · https://www.reddit.com/r/homebrewery/comments/1ctts2p/brew_no_longer_working_cant_make_new_brew/ · https://www.reddit.com/r/homebrewery/comments/1ldieda/help/ · https://www.reddit.com/r/homebrewery/comments/1064o2q/the_current_logged_in_user_does_not_have_editor/ · https://www.reddit.com/r/homebrewery/comments/b1vwbp/for_some_reason_on_the_editing_page_my_brew_looks/ · https://www.reddit.com/r/homebrewery/comments/ov2m5s/master_pdf_editor_doesnt_read_some_parts_of_a_pdf/ · https://www.reddit.com/r/homebrewery/comments/1dr1sx9/v3130/ · https://www.reddit.com/r/homebrewery/comments/1q1p1gw/homebrewery_in_2025/ · https://github.com/naturalcrit/homebrewery/issues/4845 · https://www.naturalcrit.com/

---
## Ghost

### Visual surface

Web admin (the product's main surface): a writing-first admin — post list sidebar left, and an editor that is a clean single-column canvas with a contextual formatting toolbar, a slash/card menu (`/` or `+` to insert), emoji via `:`, and cards for images, galleries, embeds, bookmarks, callouts, toggles, buttons and more <cite index="o53-1"></cite><cite index="3sb-1"></cite>. The editor was rebuilt (Koenig v3) on React + Lexical with a publicly playable demo at koenig.ghost.org — the best place to capture the editor UI without an account <cite index="zu5-1"></cite>. Marketing site (ghost.org) shows publication themes, pricing tables and the "launch your creative business" funnel; the developer docs (docs.ghost.org) are a Mintlify-style docs site <cite index="ng8-1"></cite>. Self-hosted and Ghost(Pro) share the same admin; there is a mobile editing experience in-browser ("much improved mobile editing" per the editor rewrite), but no native mobile or desktop app. UNVERIFIED whether Ghost still ships an official Android/iOS app — none is evident on current pages <cite index="zu5-1"></cite>.

Shot-list:
- Editor demo (Koenig playground, no login): https://koenig.ghost.org
- Editor cards overview (lists every card with visuals): https://ghost.org/help/cards/
- Intro to the editor (toolbar, card menu, internal linking, image editor): https://ghost.org/help/using-the-editor/
- New-editor changelog post (before/after, feature list): https://ghost.org/changelog/new-editor/
- Pricing page with plan comparison tables: https://ghost.org/pricing/
- Architecture docs (system diagram context): https://docs.ghost.org/architecture
- Homepage (theme showcase, product surface): https://ghost.org

### Docs analysis

- Architecture worth borrowing: three decoupled parts — a RESTful JSON core API (Content API read-only, cacheable, key-authenticated; Admin API read/write with role-based auth), an independent admin client, and an optional theme front-end (Handlebars). "Ghost-Admin is extremely powerful but entirely optional" — any client can drive the API <cite index="ng8-1"></cite>. For a notes app: separate the document API from the editor UI and make the editor replaceable.
- Editor architecture: Koenig was Ember.js over MobileDoc (an open JSON doc format that "never became widely adopted"), then rebuilt on React + Lexical (Meta's editor framework); the team worked directly with the Lexical core team and claims to be the first independent company to build a full-scale dynamic editor on Lexical <cite index="zu5-1"></cite>. Storage format is Lexical JSON in the database; API docs cover reading/writing it <cite index="zu5-1"></cite>. Lesson: choosing a doc format nobody else uses froze the editor for years.
- Card system: content is composed of typed cards (image, markdown, HTML, gallery, divider, bookmark, email content, call to action, public preview, button, callout, GIF, toggle, audio, video, file, product, header, embed, signup) inserted via `/` search; themes target each card by class, and themes can exclude default card asset implementations <cite index="3sb-1"></cite><cite index="3sb-2"></cite>. This is Ghost's plugin system: no JS plugins, but typed content blocks with theme-level styling hooks.
- Editor capabilities per help center: contextual toolbar, emoji-by-colon, internal linking three ways (cmd+k search over posts/pages/tags/authors, `@` inline as you type, bookmark cards), native image editing with annotations via Pintura (crop/adjust/annotate without leaving the editor) <cite index="o53-1"></cite>.
- Editor rewrite fixes worth noting as hard limits of the old one: nested lists were previously impossible; very large posts were "painful"; undo/redo chaining was broken; mobile editing was poor <cite index="zu5-1"></cite>.
- Workflow: post history with per-editor diffs and restore, scheduling, custom social/SEO metadata per post, email-only content (newsletter blocks inside posts), member-only content gating, newsletter sending with custom templates and edit links after sending <cite index="ng8-1"></cite><cite index="4xv-1"></cite>.
- Extensibility: webhooks (trigger on content changes), Admin/Content APIs, JS SDK, Zapier/n8n automation, custom storage adapters (external filesystems), and a Handlebars theme layer with a broad third-party marketplace <cite index="ng8-1"></cite>. Self-hosting via Ghost-CLI; SQLite default in dev, MySQL recommended in production <cite index="ng8-1"></cite>.
- Hard limits in the hosted product: file upload caps scale with plan (5 MB → 1 GB), staff users 1/3/15/unlimited, member caps by plan, custom themes only from Publisher up <cite index="4xv-1"></cite>.

### Features

| Area | Detail |
|---|---|
| Editor | Block/card visual editor (Koenig, React+Lexical), contextual toolbar, slash menu, nested lists, undo/redo chains (https://ghost.org/changelog/new-editor/) |
| Cards | ~20 typed cards incl. image, gallery, bookmark, callout, toggle, button, signup, email content, HTML, markdown (https://ghost.org/help/cards/) |
| Image editing | Built-in Pintura editor: adjust, crop, annotate with arrows/borders (https://ghost.org/help/using-the-editor/) |
| Internal linking | cmd+k search across posts/pages/tags/authors; `@` inline mention; bookmark cards (https://ghost.org/help/using-the-editor/) |
| Document model | Lexical JSON stored server-side; readable/writable via Admin API (https://ghost.org/changelog/new-editor/) |
| Publishing workflow | Draft→scheduled→published; post history w/ restore; custom SEO/social metadata (https://docs.ghost.org/architecture) |
| Membership/newsletters | Members, tiers, paid subscriptions 0% platform fee, newsletters, email-only content, comments (https://ghost.org/pricing/) |
| API | Content API (read-only, cacheable), Admin API (role-based), webhooks, JS SDK (https://docs.ghost.org/architecture) |
| Theming | Handlebars themes, card CSS classes, card-asset exclusion, marketplace (https://docs.ghost.org/themes/content) |
| Self-hosting | MIT open source, Ghost-CLI, SQLite/MySQL, custom storage adapters (https://docs.ghost.org/architecture) |
| Platforms | Web admin (mobile web improved); hosted Ghost(Pro) or self-host (https://ghost.org/pricing/) |

### Sentiment

| What people say |
|---|
| The writing experience is the standout: editor called "perfect and super lightweight"; descriptions like "sublime" and "distraction-free" recur in reviews (https://www.reddit.com/r/Ghost/comments/1e7cg1q/convince_me_to_not_use_ghost_for_a_personal_blog/; https://www.emailsoftwareinsights.com/reviews/ghost/) |
| Missing media library: "Editor it's simple and very fast, but doesn't even have a media library" — a self-hosting user adapted to it (https://www.reddit.com/r/juststart/comments/15i1ktg/is_anyone_a_ghost_user_what_are_your_thoughts/) |
| Users coming from WordPress expect a plugin ecosystem and are disappointed; "Where are all the plugins?" is a common complaint (https://www.emailsoftwareinsights.com/reviews/ghost/) |
| Newsletter format friction: exporting Lexical posts/HTML into other newsletter senders requires conversion and subscriber syncing (https://www.reddit.com/r/Ghost/comments/1e7cg1q/convince_me_to_not_use_ghost_for_a_personal_blog/) |
| G2/Capterra/Product Hunt reviewers praise speed, memberships, comments and support; several say it feels less fragile than WordPress (https://www.g2.com/products/ghost/reviews; https://www.producthunt.com/products/ghost/reviews) |
| Self-hosting demands more powerful hosting than WordPress (https://www.reddit.com/r/juststart/comments/15i1ktg/is_anyone_a_ghost_user_what_are_your_thoughts/) |

### Wants

| What people want changed |
|---|
| A media/asset library in the admin (https://www.reddit.com/r/juststart/comments/15i1ktg/is_anyone_a_ghost_user_what_are_your_thoughts/) |
| A real plugin/extension ecosystem beyond cards and themes (https://www.emailsoftwareinsights.com/reviews/ghost/) |
| Cheaper team seats and high-volume newsletter tiers instead of jumping plans (https://www.usebetterproducts.com/ghost-cms-review/) |
| Easier content export/conversion out of Lexical for third-party newsletter tools (https://www.reddit.com/r/Ghost/comments/1e7cg1q/convince_me_to_not_use_ghost_for_a_personal_blog/) |

### Pricing and platforms

| Item | Detail |
|---|---|
| Self-host | Free, MIT open source (https://docs.ghost.org/architecture) |
| Ghost(Pro) Starter | $18/mo billed yearly; 1 staff user, 1,000 members, 5 MB uploads, 1 newsletter (https://ghost.org/pricing/) |
| Publisher | $29/mo billed yearly; 3 staff, custom themes, paid subscriptions, advanced analytics, 1,000 members (https://ghost.org/pricing/) |
| Business | $199/mo billed yearly; 15 staff, 10,000 members, priority support, 250 MB uploads (https://ghost.org/pricing/) |
| Custom | Unlimited staff/members, SSO, dedicated IP, 99.9% SLA (https://ghost.org/pricing/) |
| Platforms | Web admin (any browser, mobile web), hosted or self-hosted; no native desktop/mobile apps advertised (https://ghost.org/pricing/) |

### Contradictions

- Third-party pricing roundups (e.g. "Starter $15, Standard $79") disagree with the official page, which currently shows Starter $18, Publisher $29, Business $199 — the "Standard" plan name appears stale in secondary sources (https://ghost.org/pricing/; https://niusleters.com/en/platforms/ghost; https://www.g2.com/products/ghost/pricing).
- Older material describes Ghost's editor as built on MobileDoc; the current, commonly repeated claim that Ghost is "an Ember admin" is outdated — the editor is React+Lexical since the Oct 2023 rewrite (https://ghost.org/changelog/new-editor/).
- None found on editor capabilities themselves.

Sources: https://ghost.org/changelog/new-editor/ · https://docs.ghost.org/architecture · https://ghost.org/help/using-the-editor/ · https://ghost.org/help/cards/ · https://ghost.org/pricing/ · https://koenig.ghost.org · https://www.reddit.com/r/Ghost/comments/1e7cg1q/convince_me_to_not_use_ghost_for_a_personal_blog/ · https://www.reddit.com/r/juststart/comments/15i1ktg/is_anyone_a_ghost_user_what_are_your_thoughts/ · https://www.emailsoftwareinsights.com/reviews/ghost/ · https://www.producthunt.com/products/ghost/reviews · https://docs.ghost.org/themes/content

---
## Proofeditor (Proof, proofeditor.ai)

### Visual surface

Web (the only platform): a document-first, centered single-column editor with a warm cream canvas and near-black warm text; the design deliberately avoids card shadows and heavy chrome, achieving depth by tonal surface shifts instead, per a design-system extraction of the live site <cite index="huc-1"></cite>. The signature element is a colored authorship gutter running down the left edge of the document — green for human-written text, purple for AI-written — so every paragraph visibly knows its author; track-changes suggestions render as inline color washes (green for insertions, muted red for deletions), and threaded comments are violet-blue pill badges; presence shows as green dots <cite index="a70-3"></cite><cite index="huc-1"></cite>. Type is a single family (Switzer), 18px body, weight-400 headings at 58/40/24px — literary rather than SaaS-bold <cite index="huc-1"></cite>. Homepage is a terminal-style pitch with copy-paste "Install Proof for me" commands for OpenClaw, Claude Code and Codex, ending in exactly one onboarding question about when the agent should open new docs in Proof <cite index="xvg-1"></cite>. No native desktop or mobile app is evident; the team has publicly noted they "need a mobile-friendly comment flow" for reviewers on phones — mobile UX is known-weak <cite index="hjm-1"></cite>.

Shot-list:
- Editor showcase with macOS window dots (homepage hero): https://www.proofeditor.ai/
- "Welcome to Proof" live doc (provenance gutter, green/purple, suggestions explained in situ): https://www.proofeditor.ai/d/bmqsxdl4
- Get-started onboarding page: https://www.proofeditor.ai/get-started
- Agent setup fallback reference: https://www.proofeditor.ai/agent-setup
- Agent docs (API reference): https://www.proofeditor.ai/agent-docs
- Open-source SDK repo (editor/server code and workspace layout): https://github.com/EveryInc/proof-sdk

### Docs analysis

- Document model: the unit is a markdown document with a per-character provenance layer, comments anchored to visible text quotes, and typed suggestions (track-changes marks) — revision is a single integer that increments on every change; reads return `{ revision, title, markdown, comments[], suggestions[] }` in one call <cite index="bl5-1"></cite>.
- Agent-first editing protocol worth borrowing wholesale: exactly two endpoints do everything — one read (`GET v3/document`) and one write (`POST v3/edit` with an operations array of replace/insert/delete/set_document plus review ops comment/reply/resolve/suggest/accept/reject, max 100 ops per request) <cite index="bl5-1"></cite>. Targets are visible text, never opaque refs or base tokens; ambiguity is disambiguated by `occurrence` or `before/after` context quotes, and conflicts return the fresh document inline (`error.current`) so a failed batch can be re-resolved and retried in one shot <cite index="bl5-1"></cite>.
- Failure design: a single closed-set error envelope (`AUTH, NOT_FOUND, INVALID_REQUEST, TARGET_NOT_FOUND, TARGET_AMBIGUOUS, CONFLICT, TOO_LARGE, BUSY, PENDING, INTERNAL`) with a `retryable` flag, `opIndex`, and candidate list with «guillemets»-marked snippets; partial commits are honest (`partial: true`, applied count, committed results), and `Idempotency-Key` retries safely replay <cite index="bl5-1"></cite>.
- Suggestion system is deeply typed: text suggestions, plus structured ones for table rows/columns, atoms (image/hr/hardbreak/footnote_reference), formatting marks (bold/italic/strikethrough/code/link), and node updates (headings, paragraphs, list items, code blocks, images, table cells) — structural suggestions "fail closed" until every connected editor supports the new reader, a capability-negotiation pattern worth borrowing <cite index="bl5-1"></cite>.
- Opaque-block rule: frontmatter, raw HTML and unknown extensions cannot be partially edited; the API refuses rather than approximates — a good data-integrity stance for a notes app <cite index="bl5-1"></cite>.
- Provenance/permissions: `by` records authorship on every write; presence identity (`X-Agent-Id: ai:<id>`) is separate from access tokens; creation returns an `accessToken` plus an `ownerSecret` that is the only key that can delete, and is permanently revoked when a human claims the document in the browser <cite index="bl5-1"></cite>.
- Event model: `/events/pending` and `/events/stream` (SSE with cursor frames and heartbeats), lifecycle events for comments and suggestions including deletion events that carry `markId`; `text.settled` is a deliberate sparse wake signal that carries no text and forces a re-read — cheap-notification, authoritative-read design <cite index="bl5-1"></cite>.
- Self-diagnosing product: agents report bugs via `POST /api/bridge/report_bug`; the server enriches reports with server traces and document events and files a Linear triage issue with a `fixerBrief` — UNVERIFIED beyond the docs' own claim <cite index="bl5-1"></cite>.
- Open-source core: proof-sdk is MIT and contains the collaborative markdown editor, realtime server, provenance model, agent HTTP bridge and a SQLite store, packaged as `doc-core`, `doc-editor`, `doc-server`, `doc-store-sqlite`, `agent-bridge` <cite index="htg-1"></cite>. It is a point-in-time snapshot that lags the hosted product <cite index="bl5-1"></cite>.
- Limits: `set_document` accepts at most 2 MiB of markdown; structural suggestions own one contiguous subtree; a pending table suggestion owns the whole table; typed suggestions cannot be modified in place, only rejected and recreated <cite index="bl5-1"></cite>.

### Features

| Area | Detail |
|---|---|
| Editor | Collaborative markdown editor, live presence, centered document column (https://github.com/EveryInc/proof-sdk) |
| Provenance | Per-character authorship gutter: green = human, purple = AI (https://www.proofeditor.ai/d/bmqsxdl4) |
| Suggestions | Track-changes-style typed proposals with accept/reject, including table/format/atom/node suggestions (https://www.proofeditor.ai/agent-docs) |
| Comments | Text-anchored threads, replies, resolve/unresolve; no comment deletion via review ops (https://www.proofeditor.ai/agent-docs) |
| Agent access | Two-endpoint HTTP bridge, content negotiation on share URLs (Accept: json or markdown), SSE events, presence (https://www.proofeditor.ai/agent-docs) |
| Sharing | Tokenized share links; role tiers viewer/commenter/editor/owner; ownerless docs claimable in browser (https://www.proofeditor.ai/agent-docs) |
| Library | Personal library of documents; managed "Your Library" doc with rename forbidden (https://www.proofeditor.ai/agent-docs) |
| Extensibility | Installed as an agent skill (SKILL.md), works with Claude Code, Codex, OpenClaw; open-source SDK (https://www.proofeditor.ai/) |
| Reliability tooling | In-product agent bug reporting that files Linear issues; retry/backoff guidance in docs (https://www.proofeditor.ai/agent-docs) |
| Platforms | Web only; mobile comment flow acknowledged as needed (https://www.proofeditor.ai/) |

### Sentiment

| What people say |
|---|
| Launch reception was hype-framed: Every's editor calls it "the Google Docs moment for AI," launched March 11, 2026 as fast, free and open source (https://x.com/ajjuliani/status/2031881580155666926; https://x.com/danshipper/status/2031794701221736529) |
| The founder says he "vibe coded" the product in his spare time while running Every, having previously said such an editor would have taken three to four engineers six months (https://x.com/every/status/2022356105276666069) |
| No independent reviews, app-store ratings or user complaint threads are visible yet — the product is ~7 months old and its documentation is written for agents rather than humans |
| The product's own docs list observed failure classes (stale reads, paused docs, comment/mark disagreement across devices, 5xx on slugs), which is an unusually candid self-audit of current reliability (https://www.proofeditor.ai/agent-docs) |

### Wants

| What people want changed |
|---|
| Mobile-friendly comment flow for reviewers arriving from shared links on phones — stated on the product's own site (https://www.proofeditor.ai/) |
| Nothing else independently documented; no feature-request threads found (UNVERIFIED absence — search coverage is thin for a brand-new product) |

### Pricing and platforms

| Item | Detail |
|---|---|
| Price | Free at launch ("fast, free, and open source") (https://x.com/danshipper/status/2031794701221736529) |
| OSS | MIT (EveryInc/proof-sdk: editor, server, provenance model, agent bridge, SQLite store); hosted product made by Every (https://github.com/EveryInc/proof-sdk) |
| Platforms | Web; agent skills for Claude Code/Codex/OpenClaw (https://www.proofeditor.ai/) |

### Contradictions

- The task's given link `github.com/proofeditor` could not be confirmed to exist as a GitHub org or to host Proof; the actual open-source repo found is `EveryInc/proof-sdk` (https://github.com/EveryInc/proof-sdk). UNVERIFIED that any `proofeditor` org exists.
- Common framing of Proof as a "product launch" underplays it: the founder describes it as a spare-time vibe-coded build rather than a team product (https://x.com/every/status/2022356105276666069), while the SDK docs describe a full workspace (editor, server, store, bridge) with an ADR for open-sourcing the core (https://github.com/EveryInc/proof-sdk).

Sources: https://www.proofeditor.ai/ · https://www.proofeditor.ai/agent-setup · https://www.proofeditor.ai/agent-docs · https://www.proofeditor.ai/d/bmqsxdl4 · https://www.proofeditor.ai/get-started · https://github.com/EveryInc/proof-sdk · https://github.com/educlopez/design-bites/blob/main/design-mds/proofeditor.ai/DESIGN.md · https://x.com/danshipper/status/2031794701221736529 · https://x.com/ajjuliani/status/2031881580155666926 · https://x.com/every/status/2022356105276666069

---
## CapCut

### Visual surface

Mobile (iOS/Android, the flagship): dark-mode capture-and-edit app; the editor is a vertical video preview with a horizontal multi-track timeline below (video, audio, text, overlay tracks), a scrubbing playhead, and a bottom toolbar of icon-driven clip tools (split, speed, animation, filters, volume) that swaps contextually as you select a clip or a track <cite index="e4h-3"></cite>. A large share of the first-run surface is template-driven: the Template tab shows reusable creator designs (not finished videos), browsable by trend and by platform (TikTok, Reels) <cite index="j6a-1"></cite>. Desktop (Windows/macOS): a dark, three-region layout — media/material panel left, preview center, timeline bottom with layer stacking, keyframes and overlays — closer to a pro NLE, with AI features (auto-cut, captions, background removal, retouch) in the same toolbars <cite index="e4h-8"></cite><cite index="e4h-3"></cite>. Web: the same dark editor in the browser plus a growing SEO/AI-tool surface (Seedance 2.0 Mini text/image-to-video, AI image generators by vertical) <cite index="2g3-1"></cite>. A dedicated iPad app is in beta and positioned as the advanced/complex-editing variant, distinct from the phone app <cite index="j6a-1"></cite>. Official help confirms UI churn is a fact of life: features move between screens in updates, and there is no version rollback <cite index="j6a-1"></cite>.

Shot-list:
- Homepage (dark hero, download CTAs, AI-tool carousel): https://www.capcut.com
- Help Center (FAQ card grid): https://www.capcut.com/help
- AI features hub: https://www.capcut.com/features
- Desktop "how to use" tutorial page (full desktop UI screenshots): https://www.capcut.com/resource/how-to-use-capcut-on-pc
- Beginner tutorial page (mobile UI screenshots): https://www.capcut.com/resource/capcut-tutorial-for-beginners
- Feature-availability comparison table (mobile vs desktop vs web, Free vs Pro): https://capcutguide.com/capcut-video-editor-features-guide/

### Docs analysis

- Platform segmentation is a deliberate architecture: mobile, desktop, web and iPad are separate editors with different feature sets; official help states the iPad app is designed "for more advanced and complex editing workflows" while the phone app stays simple, and neither replaces the other <cite index="j6a-1"></cite>. Third-party feature matrices document that many tools (4K export, keyframes, chroma key, AI features, cloud projects) differ by platform, plan, region and app version <cite index="e4h-1"></cite>.
- Subscription gating is enforced at the asset level: any template, effect, filter, font, sticker or music track tagged Pro must be removed before a free export, and CapCut's own help center documents how to strip Pro items from a project to make it exportable on the free plan <cite index="93l-1"></cite>. For a notes app this is a borrowable (and cautionary) model: per-item entitlement tags checked at output time rather than at input.
- Credit system: 2026 plans bundle AI credits (Pro ~1,200/month, Ultra more) consumed by AI generations; credit rules are documented separately per platform, with mobile buy/check routes described differently from web <cite index="93l-2"></cite><cite index="e4h-1"></cite>.
- Template ecosystem: templates are first-class documents — reusable designs that render user media into a finished edit; trending-template discovery is a product surface with its own SEO pages <cite index="j6a-1"></cite>. Lesson for a notes app: sharable, remixable "templates of content" as a growth surface.
- Hard limits and quirks from official help: no private-account option on any platform (as of January 2026), no profile-picture change on web/desktop (mobile only), forced updates on PC (no rollback supported), watermark removal and 4K export behind Pro, and pricing that varies by region/device/promo with per-account A/B pricing tests <cite index="j6a-1"></cite><cite index="93l-5"></cite>.
- Rendering pipeline: export supports up to 4K on desktop; slow-motion template playback is attributed to playback/rendering settings mismatch or device real-time processing limits — the renderer is device-bound on mobile <cite index="j6a-1"></cite><cite index="e4h-3"></cite>.
- Official "docs" are FAQ-first (troubleshooting, safety, parents' guides) rather than a reference manual; even advanced users on r/CapCut ask "is there a documentation for special desktop features" — none exists <cite index="e4h-5"></cite>.
- There is a third-party MCP/API ecosystem (VectCutAPI) exposing CapCut-style draft-file editing, indicating the local project format (drafts JSON) is readable — UNVERIFIED for the official product; CapCut itself publishes no public API <cite index="e4h-4"></cite>.

### Features

| Area | Detail |
|---|---|
| Editor | Multi-track timeline, split/speed/reverse, keyframes, transitions synced to music, overlays (https://www.capcut.com/resource/how-to-use-capcut-on-pc) |
| AI editing | Auto Cut (trim/sync to beats, speech, prompts), auto captions, background removal, retouch, AI voiceover, AI design/image generation, Seedance 2.0 Mini text/image-to-video (https://www.capcut.com/features) |
| Templates | Reusable creator-designed edits; trending-template marketplace; template watermark rules (https://www.capcut.com/help) |
| Asset library | Stickers, fonts, filters, effects, music; Pro-tagged items gated (https://www.capcut.com/features) |
| Platform sync | Cloud projects (Pro/Standard); Standard plan no longer valid across mobile and PC per 2026 membership restructure (https://www.capcut.com/help) |
| Export | Up to 4K desktop; 1080p cap on Standard; watermarks on free/Pro-tagged content (https://fluxnote.io/guides/capcut-pro-pricing-2026) |
| Collaboration | CapCut Teams plan for shared workspaces (https://www.capcut.com/help) |
| Platforms | iOS, Android, Windows, macOS, Web, iPad (beta) (https://www.capcut.com/help) |

### Sentiment

| What people say |
|---|
| Paywall creep is the dominant complaint: users document formerly free tools (transitions, speed curves, animations, effects, audio extraction, cloud storage) migrating to Pro over successive updates (https://checkthat.ai/brands/capcut/reviews) |
| r/CapCut "everything that was great about capcut is now locked behind a paywall in this recent update": motion blur, 99% of stickers/transitions/fonts went Pro (https://www.reddit.com/r/CapCut/comments/1bggkwt/everything_that_was_great_about_capcut_is_now/) |
| January 2026 Pro price increase triggered "the DEATH of CapCut" threads; users compare it to Filmora's paywall behavior (https://www.reddit.com/r/CapCut/comments/1qmowww/pro_price_increase_is_the_DEATH_of_capcut/) |
| Export-blocking trust break: "I spent an hour adjusting audio tracks and transitions, only to find the export button blocked by a premium paywall" (Trustpilot, via checkthat) (https://checkthat.ai/brands/capcut/reviews) |
| r/VideoEditing has effectively blacklisted it: progressive paywalling of captioning, licensing issues, buggy software (https://www.reddit.com/r/VideoEditing/comments/1w0sst2/lets_talk_a_moment_about_capcut_and_the_shift_in/) |
| UI/layout lock-in cuts both ways: hobbyists stay because "I'm used to the UI in layout of capcut and now it's harder" on other apps (https://www.reddit.com/r/CapCut/comments/1htbzyu/people_who_are_upset_that_capcut_is_not_free/) |
| r/VideoEditing also credits its ease of use: it remains the tool beginners reach for first (https://www.reddit.com/r/VideoEditing/comments/1w0sst2/lets_talk_a_moment_about_capcut_and_the_shift_in/) |

### Wants

| What people want changed |
|---|
| Stable free tier: clear up-front labeling of what may become paid later, instead of retroactive paywalling of features users already rely on (https://www.reddit.com/r/CapCut/comments/1eapjkl/for_all_those_saying_get_used_to_pay/) |
| Fewer intrusive AI features that "barely even work," more core editing stability (https://www.reddit.com/r/CapCut/comments/1qmowww/pro_price_increase_is_the_death_of_capcut/) |
| Real documentation for desktop features and their reliability behavior (https://www.reddit.com/r/CapCut/comments/13v63gh/is_there_a_documentation_for_special_desktop/) |
| Less glitchiness on mobile; several users are actively hunting alternatives (https://www.reddit.com/r/CapCut/comments/1n1nyy5/free_editing_software_capcut_is_slowly_paywalling/) |
| Reversal of the 2026 price increase / better value tiers (https://www.reddit.com/r/CapCut/comments/1qmowww/pro_price_increase_is_the_death_of_capcut/) |

### Pricing and platforms

| Item | Detail |
|---|---|
| Free | Core editor, watermarked Pro-tagged exports blocked; free plan limits documented by third parties (https://fluxnote.io/guides/capcut-pro-pricing-2026) |
| Standard | ~$9.99/mo; 1080p export cap; cross-platform support reduced in 2026 restructure (https://pixflow.net/blog/capcut-pro-price-worth-it/; https://www.capcut.com/help) |
| Pro | ~$19.99/mo or $179.99/yr on web; ~1,200 AI credits/mo, 1 TB cloud storage, 4K export; app-store checkouts run a few dollars more (https://pixflow.net/blog/capcut-pro-price-worth-it/; https://www.nemovideo.com/blog/capcut-pro-pricing-2026) |
| Ultra | ~$79/mo, heavy AI generation (https://pixflow.net/blog/capcut-pro-price-worth-it/) |
| Teams | Team plan for collaboration (https://www.capcut.com/help) |
| Pricing authority | Official help says pricing varies by region/device/promotions and points to in-app checkout; no fixed global price published (https://www.capcut.com/help/how-much-does-capcut-pro-cost) |
| Platforms | iOS, Android, iPad (beta), Windows, macOS, Web (https://www.capcut.com/help) |

### Contradictions

- Third-party pricing guides disagree with each other and with official messaging: some list Pro $9.99/mo and $89.99/yr, others $19.99/mo and $179.99/yr, and official help says there is no fixed global price and points to in-app checkout (https://www.capcut.com/help/how-much-does-capcut-pro-cost; https://dpremi.com/blog/capcut-pro-price-guide-2026; https://pixflow.net/blog/capcut-pro-price-worth-it/).
- "Free video editor" reputation vs. reality: the free editor remains functional, but a documented pattern of moving formerly free features to Pro contradicts CapCut's historical free positioning (https://checkthat.ai/brands/capcut/reviews; https://www.reddit.com/r/CapCut/comments/1eapjkl/for_all_those_saying_get_used_to_pay/).

Sources: https://www.capcut.com/help · https://www.capcut.com/features · https://www.capcut.com/resource/how-to-use-capcut-on-pc · https://capcutguide.com/capcut-video-editor-features-guide/ · https://fluxnote.io/guides/capcut-pro-pricing-2026 · https://pixflow.net/blog/capcut-pro-price-worth-it/ · https://www.reddit.com/r/CapCut/comments/1bggkwt/everything_that_was_great_about_capcut_is_now/ · https://www.reddit.com/r/CapCut/comments/1qmowww/pro_price_increase_is_the_death_of_capcut/ · https://www.reddit.com/r/VideoEditing/comments/1w0sst2/lets_talk_a_moment_about_capcut_and_the_shift_in/ · https://www.reddit.com/r/CapCut/comments/1eapjkl/for_all_those_saying_get_used_to_pay/ · https://checkthat.ai/brands/capcut/reviews · https://www.reddit.com/r/CapCut/comments/13v63gh/is_there_a_documentation_for_special_desktop/ · https://e4h-4 source: https://github.com/sun-guannan/VectCutAPI/blob/main/MCP_Documentation_English.md

---
## Descript

### Visual surface

Desktop and web (macOS/Windows apps plus browser): the signature layout is a two-panel editor — the script panel (the transcript as a word-processor document, the primary editing surface) on top, with scene/canvas and timeline below for fine visual control; Descript explicitly says the timeline is optional and "you can make a whole video without touching it" <cite index="t9b-6"></cite>. The script supports word-processor actions (delete/cut/paste text removes or moves the underlying media), a wordbar at the bottom for fine word timing, strikethrough "ignore" marks, inline parenthetical notes like [cough], and speaker labels <cite index="02w-1"></cite>. Around the editor: an AI-actions layer (Underlord assistant), scenes that work like slide decks, layout/template library, clips publishing, and an in-app Learning Center <cite index="t9b-9"></cite><cite index="t9b-10"></cite>. No mobile editor; mobile exists only for capture/permissions. UNVERIFIED: current app-store listing details for the desktop app minimum OS requirements.

Shot-list:
- Homepage hero (script panel + canvas + timeline visual): https://www.descript.com/
- Features page (record/edit/refine/share/multiply sections with product screenshots): https://www.descript.com/features
- Pricing page with plan comparison: https://www.descript.com/pricing
- "Edit like a doc" help article (annotated editor screenshots): https://help.descript.com/hc/en-us/articles/15726742913933-Edit-like-a-doc
- Audio-to-text tool page (transcript UI screenshots): https://www.descript.com/tools/audio-text
- Beginner tutorial (start-to-finish UI walkthrough): https://www.descript.com/blog/article/descript-tutorial-for-beginners-6-steps-to-get-started

### Docs analysis

- Transcript-as-document model worth borrowing in full: the transcript "isn't just a reference — it's directly linked to your media"; deleting a word deletes it from the audio/video; cut/paste moves media; a separate `Remove from transcript` op hides text without touching media; `Ignore` strikes through without deleting — i.e., the text is an index into the media, and there are three distinct delete-like semantics <cite index="02w-1"></cite>.
- Inline notes: parenthetical annotations ([cough], [laughter]) that ride in exported transcripts but don't affect word/media alignment — a non-destructive metadata channel inside the text <cite index="02w-1"></cite>.
- Wordbar: word-level timing adjustment at the bottom of the script for caption sync — word-level time data is stored per word, not just per clip <cite index="02w-1"></cite>.
- Bulk operations: Remove Filler Words finds and deletes ums/uhs/likes/long pauses project-wide with per-cut review before applying; Remove Retakes detects repeated takes and keeps the last good one; Shorten word gaps compresses pauses across the whole script — reviewable batch edits are a pattern a notes app could borrow for AI edits <cite index="t9b-8"></cite><cite index="02w-1"></cite>.
- Regeneration: editing a line of script can trigger AI "regenerate" that recreates the speaker's voice for the new words; translation of transcript/captions/audio into 30+ languages <cite index="t9b-7"></cite>.
- Scenes model: content is organized as scenes (like slides) whose layouts swap visuals while the script stays the source of truth — a layout layer decoupled from the content layer <cite index="t9b-9"></cite>.
- AI assistant surface: Descript connects to external assistants (Claude, ChatGPT) via MCP so agents run edits; help center ships an `/llms.txt` docs index for AI consumption — agent-first documentation packaging <cite index="t9b-1"></cite>.
- Hard limits: accuracy up to ~95% claimed; media is metered per month by hours (Free 1 hour; paid tiers more), not by seats alone; export quality (4K) and transcription volume tier-gated; heavy users get pushed up-tier by the media-hours cap <cite index="t9b-5"></cite><cite index="71v-3"></cite>.
- Feature breadth per official pages: screen recording, multi-track editing, Green Screen, Studio Sound (noise removal/voice quality), auto subtitles, eye contact correction, generative image/video, clips repurposing, publishing/hosting <cite index="t9b-2"></cite><cite index="t9b-8"></cite>.

### Features

| Area | Detail |
|---|---|
| Editor | Text-first script editor linked 1:1 to media; optional timeline for fine control; wordbar for word timing (https://help.descript.com/hc/en-us/articles/15726742913933-Edit-like-a-doc) |
| Transcription | Auto transcription on import/record; ~95% accuracy claim; speaker labels; transcript correction flow (https://www.descript.com/tools/audio-text) |
| AI editing | Remove Filler Words (reviewable batch), Remove Retakes, Shorten word gaps, Studio Sound, Green Screen, eye contact (https://www.descript.com/features) |
| Voice | Regenerate uses AI to recreate the speaker's voice for script edits; Overdub-style voice cloning (https://www.descript.com/transcription) |
| Structure | Scenes (slide-like), layouts, templates (https://gotranscript.com/public/descript-101-edit-videos-like-a-doc-with-ai-help) |
| AI assistant | Underlord in-app assistant; MCP connection for external agents (Claude/ChatGPT) (https://help.descript.com/; https://gotranscript.com/public/descript-101-edit-videos-like-a-doc-with-ai-help) |
| Repurposing | AI Actions to blog posts, social clips, summaries; clips/publishing/hosting (https://www.descript.com/blog/article/new-learning-center-useful-videos-that-show-you-how-to-use-descript) |
| Collaboration | Comments, team workspaces, per-editor seats (https://www.descript.com/pricing) |
| Platforms | Desktop apps (macOS, Windows) + web; mobile capture only (https://www.descript.com/blog/article/how-to-use-descript) |

### Sentiment

| What people say |
|---|
| The core idea is loved, the execution is criticized: "I think Descript is a brilliant idea for editing via transcript… but the performance is awful" (https://www.reddit.com/r/Descript/comments/17rrqwl/descript_is_by_far_the_most_unresponsive_slow_and/) |
| Slowness and bugs recur: browser-based, "slow and somewhat buggy"; corrections often need two or more attempts (https://www.reddit.com/r/podcasting/comments/1ktotjo/descript_is_horrible/) |
| Transcription quality complaints on real recordings: co-hosts with high-quality mics still get "abysmal" transcription, and filler-word removal inherits those errors (https://www.reddit.com/r/Descript/comments/1b0q11d/descript_poor_quality_transcription/; https://www.reddit.com/r/podcasting/comments/u669i9/problems_with_descript/) |
| Export quality loss: a 500 MB source compressed to 23 MB on export with little control over settings (https://www.eesel.ai/blog/descript-reviews) |
| Destructive rendering artifacts: flattening edited tracks could add "nasty spike sounds" (https://www.reddit.com/r/podcasting/comments/u669i9/problems_with_descript/) |
| UI churn drives power users away: "Descript changed the way it works, and now I find it really difficult to use" (https://www.reddit.com/r/podcasting/comments/1rqimqy/what_is_your_experience_using_descript_and_other/) |
| Pro users cancel over polish: an honest-review thread titled "why I cancelled my pro subscription" (https://www.reddit.com/r/Descript/comments/17z5bkh/an_honest_review_of_descript_and_why_i_cancelled/) |

### Wants

| What people want changed |
|---|
| Performance: faster project load, responsive editing, fewer "preparing" states (https://www.reddit.com/r/Descript/comments/17rrqwl/descript_is_by_far_the_most_unresponsive_slow_and/) |
| Reliable transcription on real-world audio, not just clean inputs (https://www.reddit.com/r/Descript/comments/1b0q11d/descript_poor_quality_transcription/) |
| Export settings control (bitrate/quality) instead of aggressive default compression (https://www.eesel.ai/blog/descript-reviews) |
| UI stability — power users want workflows to stop being reworked (https://www.reddit.com/r/podcasting/comments/1rqimqy/what_is_your_experience_using_descript_and_other/) |
| Standalone NLE-independent transcript editing for team logins (https://www.reddit.com/r/editors/comments/1r2yi48/alternative_to_descript_for_text_based/) |

### Pricing and platforms

| Item | Detail |
|---|---|
| Free | $0, 1 media hour/mo, core editor (https://www.descript.com/pricing) |
| Hobbyist | $16/mo billed annually ($24 monthly) (https://www.layer3labs.io/guides/descript-pricing) |
| Creator | $24/mo annually ($35 monthly), 4K, more hours (https://www.layer3labs.io/guides/descript-pricing) |
| Business | $50/mo annually ($65 monthly), team features (https://www.layer3labs.io/guides/descript-pricing) |
| Enterprise | Custom, quoted (https://www.layer3labs.io/guides/descript-pricing) |
| Metering | Media hours/month + AI credits per plan; the cap (not seats) is what pushes upgrades (https://www.layer3labs.io/guides/descript-pricing) |
| Platforms | macOS, Windows, Web (https://www.descript.com/blog/article/how-to-use-descript) |

### Contradictions

- Official claim of "up to 95% accuracy" vs. repeated user reports of abysmal transcription on high-quality recordings — accuracy is clearly input-dependent and plan-marketing numbers don't transfer (https://www.descript.com/tools/audio-text; https://www.reddit.com/r/Descript/comments/1b0q11d/descript_poor_quality_transcription/).
- Official positioning "edit like a doc, no timeline required" vs. pro reviewers finding the whole pipeline slow and buggy enough that the time saving never materializes (https://www.descript.com/; https://www.reddit.com/r/editors/comments/1r2yi48/alternative_to_descript_for_text_based/).
- Some 2026 third-party pricing pages mention a "Pro" tier; the official page's current tiers are Free/Hobbyist/Creator/Business (+Enterprise) — the Pro name appears stale (https://fluxnote.io/guides/descript-pricing-2026; https://www.descript.com/pricing).

Sources: https://www.descript.com/features · https://help.descript.com/hc/en-us/articles/15726742913933-Edit-like-a-doc · https://help.descript.com/ · https://www.descript.com/ · https://www.descript.com/tools/audio-text · https://www.descript.com/pricing · https://www.layer3labs.io/guides/descript-pricing · https://www.reddit.com/r/Descript/comments/17rrqwl/descript_is_by_far_the_most_unresponsive_slow_and/ · https://www.reddit.com/r/podcasting/comments/1ktotjo/descript_is_horrible/ · https://www.reddit.com/r/Descript/comments/1b0q11d/descript_poor_quality_transcription/ · https://www.eesel.ai/blog/descript-reviews · https://www.reddit.com/r/podcasting/comments/1rqimqy/what_is_your_experience_using_descript_and_other/

---
## LumaFusion

### Visual surface

iPad/iPhone (flagship): a dark professional NLE built touch-first — a media library, a source/preview player, and the signature timeline that is simultaneously track-based and magnetic ("the world's most flexible track-based AND magnetic timeline" is LumaTouch's own framing), with layered video/graphic tracks plus separate audio tracks below <cite index="8v2-1"></cite>. The timeline UI is icon-dense: LumaTouch's own tutorial series opens by touring "the icons and features available to editors" before any editing, which tells you how much surface the timeline carries <cite index="k1y-1"></cite>. Clip editors expose color correction with waveform/vector/histogram scopes, keyframes, LUT import, EQ and audio ducking <cite index="8v2-1"></cite>. Mac (M1+) and Vision Pro run the same app; Android/ChromeOS ship a ground-up rebuild of the same experience with a minimum of 3 GB RAM <cite index="8v2-1"></cite><cite index="gz7-7"></cite>. The official site (lumafusion.com and luma-touch.com product pages) presents dark product screenshots and feature grids rather than a marketing funnel; LumaFusion was Apple's "App of the Year" 2021 and an Editors' Choice recipient, claims it wears on the store listing <cite index="8v2-1"></cite>.

Shot-list:
- App Store listing (feature grid, screenshots, version notes): https://apps.apple.com/us/app/lumafusion/id1062022008
- Timeline product page (multicam/timeline screenshots): https://luma-touch.com/timeline/
- Tutorials index (official video tutorials, incl. the timeline tour): https://luma-touch.com/tutorials/
- Reference Guide (full manual): https://luma-touch.com/lumafusion-reference-guide
- Creator Pass page (paid-tier feature pack): https://luma-touch.com/creator-pass-2/
- Android/ChromeOS product page: https://luma-touch.com/lumafusion-for-android/
- 9to5Mac walkthrough article (project features, screenshots): https://9to5mac.com/2017/07/19/lumafusion-ipad-video-editing-guide-part-1-getting-familiar-with-projects/

### Docs analysis

- The Reference Guide is a genuine manual (PDF, hundreds of pages, publication 3.0 era), unusual thoroughness for a mobile app; the App Store description functions as the concise feature reference <cite index="8v2-1"></cite>. Core architecture: projects with 12 video/audio or graphic tracks and 12 additional audio tracks since v5.2 (previously 6+6), 4K ProRes and HDR handling, frame rates 18–240 fps, markers/tags/notes, and voiceover recording while playing <cite index="8v2-1"></cite><cite index="l0g-3"></cite>.
- The dual magnetic/track-based timeline is the key design decision: magnetic behavior for fast assembly, track discipline for layering — LumaTouch deliberately refuses to choose, unlike Final Cut or Premiere <cite index="8v2-1"></cite>. Adjustment Clips (v5.2) apply effects/position/scale/crop to all layers below them, layered and keyframable — a non-destructive global-edit layer worth borrowing for any document/canvas app <cite index="l0g-1"></cite><cite index="l0g-3"></cite>.
- Enhanced features are sold separately: Speed Ramping & Enhanced Keyframing ($19.99 one-time), Multicam Studio (sync 6 cameras/audio, $19.99), FCPXML export to Final Cut Pro ($19.99), CoreMelt PaintX plug-in — all bundled in the Creator Pass subscription which also unlocks Storyblocks stock media <cite index="8v2-1"></cite><cite index="15i-1"></cite>. XML/FCPXML export is the professional interop escape hatch; LumaFusion positions itself inside a desktop workflow rather than replacing it <cite index="8v2-1"></cite>.
- Media handling: edit directly from Photos, Frame.io, and USB-C drives; import from cloud storage; background downloading of library clips with progress shown as blue/green stripes on timeline clips (from the Reference Guide) <cite index="8v2-1"></cite><cite index="k1y-6"></cite>. Audio: stereo and dual-mono per clip, third-party audio plugins, keyframable levels/panning/EQ, audio ducking <cite index="8v2-1"></cite>.
- Hard limits observed in docs and store listing: no Windows version; Android build requires Android 10+ / 3 GB RAM minimum; desktop features (e.g. some keyframe tiers) vary by platform; the App Store marketing text still describes the old 6-track layout in places while What's New lists 12 — version drift inside official copy <cite index="gz7-7"></cite><cite index="8v2-1"></cite>. UNVERIFIED: exact current per-format export codec options beyond the store's "control resolution, quality, and format" claim.
- Container limitation: multi-audio-track video files are a documented-in-forums weakness — a 3-track OBS .mkv remuxed to .mp4 shows one merged track in LumaFusion where DaVinci Resolve shows all three (user report, consistent across several r/LumaFusion threads; not addressed in official docs I could see) <cite index="srb-1"></cite><cite index="srb-4"></cite>.

### Features

| Area | Detail |
|---|---|
| Timeline | Hybrid track-based + magnetic timeline; 12 video + 12 audio tracks (v5.2); markers, tags, notes (https://apps.apple.com/us/app/lumafusion/id1062022008) |
| Effects | Adjustment Clips affect all layers below; green screen/luma/chroma keys; unlimited keyframes; custom text/effect presets shareable (https://apps.apple.com/us/app/lumafusion/id1062022008) |
| Color | Scopes (waveform/vector/histogram), LUT import (.cube/.3dl), powerful color correction (https://apps.apple.com/us/app/lumafusion/id1062022008) |
| Audio | EQ (graphic/parametric), Voice Isolation, ducking, stereo/dual-mono, third-party audio plugins, keyframed mixing, voiceover record (https://apps.apple.com/us/app/lumafusion/id1062022008) |
| Media | Edit from Photos, Frame.io, USB-C drives, cloud import; external monitor preview; background media download with progress on clips (https://apps.apple.com/us/app/lumafusion/id1062022008) |
| Interop | FCPXML export to Final Cut Pro (paid); aspect ratios and frame rates for social through cinema (https://apps.apple.com/us/app/lumafusion/id1062022008) |
| Paid add-ons | Speed Ramping & Enhanced Keyframing, Multicam Studio (6 angles), PaintX plug-in; all in Creator Pass with Storyblocks (https://luma-touch.com/creator-pass-2/) |
| Platforms | iOS 27+, iPadOS, macOS (M1+), visionOS, Android 10+/ChromeOS (3 GB+ RAM); no Windows (https://apps.apple.com/us/app/lumafusion/id1062022008; https://luma-touch.com/lumafusion-for-android/) |

### Sentiment

| What people say |
|---|
| Long-standing respect on Apple platforms: 4.7/5 across 25K App Store ratings, App of the Year 2021 (https://apps.apple.com/us/app/lumafusion/id1062022008) |
| Android build is the pain point: on an S10+ with 8 GB RAM a user still needs to clear every app from memory before editing and juggle gallery/file managers — "Lumafusion is the worst app in America" is the hyperbolic title (https://www.reddit.com/r/LumaFusion/comments/1ir8jjg/lumafusion_is_the_worst_app_in_america/) |
| Multi-audio-track files frustrate technical users: OBS-recorded mkv/mp4 shows one merged audio track vs Resolve showing all three (https://www.reddit.com/r/LumaFusion/comments/wyg4ps/can_lumafusion_edit_video_files_with_multiple/) |
| Audio export distortion when levels ride in the orange/red despite clean in-app playback (https://www.reddit.com/r/LumaFusion/comments/ltl477/bad_quality_audio_after_exporting/) |
| Imported mp4s can show black video with audio only in the media pool (https://www.reddit.com/r/LumaFusion/comments/18q1qvo/imported_mp4s_only_have_their_audio_playing_but/) |
| Reviewers praise the track count, layering, 4K support and "intuitive" multi-track interface as its core strength (https://www.techjockey.com/reviews/lumafusion-video-editing-software) |

### Wants

| What people want changed |
|---|
| A more robust Android build (memory management, fewer crashes on mid-range devices) (https://www.reddit.com/r/LumaFusion/comments/1ir8jjg/lumafusion_is_the_worst_app_in_america/) |
| Proper multi-audio-track container support on import (https://www.reddit.com/r/LumaFusion/comments/wyg4ps/can_lumafusion_edit_video_files_with_multiple/) |
| Unbundled pricing complaints surface around the Creator Pass gating of formerly pro features like speed ramping and FCPXML export (https://www.redsharknews.com/lumafusion-version-5.2-expands-to-12-video-and-audio-tracks) |
| UNVERIFIED: no aggregate feature-request list found in official channels beyond support email; LumaTouch directs requests to lumatouch.co/support (https://apps.apple.com/us/app/lumafusion/id1062022008) |

### Pricing and platforms

| Item | Detail |
|---|---|
| Base app | $29.99 one-time on App Store (Apple) and $29.99 on Android/ChromeOS per LumaTouch's own announcement (https://apps.apple.com/us/app/lumafusion/id1062022008; https://luma-touch.com/lumatouch-releases-lumafusion-for-chromeos-and-android/) |
| Creator Pass | $9.99/month or $69.99/year: all Enhanced Features + Storyblocks stock library (https://luma-touch.com/creator-pass-2/) |
| A la carte | Speed Ramping & Keyframing $19.99, Multicam Studio $19.99, FCPXML Export $19.99, CoreMelt PaintX $19.99 (https://apps.apple.com/us/app/lumafusion/id1062022008) |
| Platforms | iPhone, iPad (iOS 27+/iPadOS 27+), Mac (M1+, macOS 26+), Apple Vision (visionOS 27+), Android 10+/ChromeOS (3 GB+ RAM); no Windows (https://apps.apple.com/us/app/lumafusion/id1062022008; https://luma-touch.com/lumafusion-for-android/) |

### Video evidence

- Official tutorial channel and index: LumaTouch hosts its tutorial library at https://luma-touch.com/tutorials/, including the "main features of the timeline" tour by Caroline that the docs themselves recommend watching before editing — the clearest official footage of real timeline workflow (https://luma-touch.com/tutorials/).
- Official multicam footage: LumaTouch's timeline page embeds a chef/production-crew case video showing Multicam Studio used to cut cooking-show segments, demonstrating angle switching synced to primary audio on the timeline (https://luma-touch.com/timeline/).
- Third-party walkthroughs: 9to5Mac's multi-part video guide (2017) walks through project creation, preferences, renaming/duplicating/deleting projects — still the reference walkthrough for the project layer (https://9to5mac.com/2017/07/19/lumafusion-ipad-video-editing-guide-part-1-getting-familiar-with-projects/). Primal Video's 2025 beginner tutorial shows the cross-platform interface "similar across iOS and Android," import, and new-project flow, and notes editing via touchscreen, keyboard/trackpad, or Apple Pencil (https://primalvideo.com/video-creation/editing/lumafusion-tutorial-how-to-edit-video-on-iphone-ipad/).
- What video shows about real workflow: media import is a separate library step (down-arrow source picker with Dropbox/Drive options) before timeline work; trimming/splitting/reordering are the taught core moves; adjustment clips and keyframing are positioned as the "advanced" layer after mastering the timeline icons (https://luma-touch.com/tutorials/; https://vidpromom.com/lumafusion-tutorial/).
- Comment threads and gripe-gap: UNVERIFIED — I could not load YouTube comment threads directly in this pass. From Reddit-side discussion, users gripe about Android memory pressure, multi-audio-track imports and export distortion, topics the polished official tutorials do not mention (https://www.reddit.com/r/LumaFusion/comments/1ir8jjg/lumafusion_is_the_worst_app_in_america/; https://www.reddit.com/r/LumaFusion/comments/wyg4ps/can_lumafusion_edit_video_files_with_multiple/). No notable Hacker News threads surfaced in searches this pass; absence is UNVERIFIED, not confirmed.
- Caution: several GitHub/SEO pages about LumaFusion surfaced in earlier searches and were judged spam; none are cited here.

### Contradictions

- Track-count drift inside official copy: the App Store description still advertises "Six video/audio or graphic tracks + six additional audio tracks" while the same page's What's New for 5.x confirms 12 video and 12 audio tracks since v5.2 — official marketing text lags official release notes (https://apps.apple.com/us/app/lumafusion/id1062022008).
- Base price printed as $29 by press vs $29.99 on the store page (https://www.redsharknews.com/lumafusion-version-5.2-expands-to-12-video-and-audio-tracks; https://apps.apple.com/us/app/lumafusion/id1062022008).
- Press describe v5.2's 12 tracks as "included"/free expansion, but RedShark's own pricing note shows the tracks arrive inside paid feature packs (Speed Ramping/Keyframing or Creator Pass), i.e. the capability expansion was tied to the paid tier, with only SVG import, Quick Zoom transitions and preset shapes free (https://www.redsharknews.com/lumafusion-version-5.2-expands-to-12-video-and-audio-tracks).

Sources: https://apps.apple.com/us/app/lumafusion/id1062022008 · https://www.redsharknews.com/lumafusion-version-5.2-expands-to-12-video-and-audio-tracks · https://9to5mac.com/2025/02/25/this-new-lumafusion-feature-unlocks-even-more-creativity/ · https://luma-touch.com/creator-pass-2/ · https://luma-touch.com/lumafusion-for-android/ · https://luma-touch.com/lumatouch-releases-lumafusion-for-chromeos-and-android/ · https://luma-touch.com/tutorials/ · https://luma-touch.com/timeline/ · https://luma-touch.com/lumafusion-reference-guide · https://www.reddit.com/r/LumaFusion/comments/wyg4ps/can_lumafusion_edit_video_files_with_multiple/ · https://www.reddit.com/r/LumaFusion/comments/1ir8jjg/lumafusion_is_the_worst_app_in_america/ · https://www.reddit.com/r/LumaFusion/comments/ltl477/bad_quality_audio_after_exporting/ · https://primalvideo.com/video-creation/editing/lumafusion-tutorial-how-to-edit-video-on-iphone-ipad/ · https://9to5mac.com/2017/07/19/lumafusion-ipad-video-editing-guide-part-1-getting-familiar-with-projects/

LANE E COMPLETE — 7 apps covered
