# R12 round 2 lane 3: r7-feature-inventory-oss re-verification

Method: re-proved claims from scratch with fresh web research on 2026-10-27 (web search capture, then direct fetches of GitHub repos, LICENSE files, official docs and pricing pages). Direct fetches succeeded for: logseq repo + LICENSE.md + db-sync README, laurent22/joplin repo + OCR docs page, streetwriters/notesnook + notesnook-sync-server repos, TriliumNext/Trilium repo, toeverything/AFFiNE + blocksuite repos + AFFiNE FAQ, anyproto repos, ente repo + hasgeek self-host review, saber-notes repo, xournalpp repo, flxzt/rnote repo, excalidraw repo, AppFlowy repo + AppFlowy forum thread, standardnotes/server repo, refactoringhq/tolaria repo, timothepoznanski/poznote repo + site. Could not be fetched: outline/outline repo (direct fetch refused; facts rest on search captures), the HelixNotes GitLab page (returned a loading shell only), the raw xournalpp LICENSE file (fetch refused), plus Reddit/blog/sentiment pages left out of budget. Every verdict cites a URL; anything without fresh evidence is STILL-UNVERIFIED.

## Logseq

L13 | AGPL-3.0 LICENSE.md | CONFIRMED | https://github.com/logseq/logseq/blob/master/LICENSE.md | LICENSE file fetched this session, AGPL-3.0 text
L13 | Repo logseq/logseq live | CONFIRMED | https://github.com/logseq/logseq | repo fetched, active
L13 | Plugin samples MIT | STILL-UNVERIFIED | https://github.com/logseq/logseq-plugin-samples/blob/master/LICENSE | not re-fetched
L15 | Local plain-text md/org, Electron app | CONFIRMED | https://github.com/logseq/logseq | README describes local Markdown/Org files
L15 | DB version SQLite + db-sync + Sync server url | CONFIRMED | https://github.com/logseq/logseq/blob/master/deps/db-sync/README.md | db-sync README fetched this session
L15 | Official docs and marketplace repos | CONFIRMED | https://github.com/logseq/logseq | README links docs and marketplace repos
L17 | Privacy-first KM platform, outliner features (blocks, journals, queries, graph, PDF annotation, flashcards) | CONFIRMED | https://github.com/logseq/logseq | README + docs describe these
L17 | Whiteboards product; export via bundled JS not static HTML | STILL-UNVERIFIED | https://github.com/logseq/logseq/discussions/5246 | discussion not re-fetched
L19 | Official Sync E2EE, paid, beta-gated on Open Collective | STILL-UNVERIFIED | https://blog.logseq.com/how-to-setup-and-use-logseq-sync/ | blog not re-fetched
L19 | Sync beta single-user, data-loss warnings | STILL-UNVERIFIED | https://www.thegeeksclub.com/platforms/logseq/ | not re-fetched
L19 | Self-hosting via Sync server url + db-sync in 2.0.1 | CONFIRMED | https://github.com/logseq/logseq/blob/master/deps/db-sync/README.md | db-sync README fetched; Node.js adapter documented
L19 | "Sync code widely understood not to be FOSS" | REVISED | https://github.com/logseq/logseq/blob/master/deps/db-sync/README.md | db-sync component sits inside the AGPL-3.0 logseq repo with a documented Node.js adapter; the paid hosted sync may differ but the self-host component is in the FOSS repo
L19 | Pre-official-sync users on Syncthing/Git/Dropbox | STILL-UNVERIFIED | https://www.reddit.com/r/logseq/comments/172tocr/self_hosting_options/ | not re-fetched
L21 | Publishing via bundled JS; md/org native format | CONFIRMED | https://github.com/logseq/logseq | native md/org files confirmed via README; publishing path not re-verified
L23 | Marketplace plugin ecosystem | CONFIRMED | https://github.com/logseq/marketplace | repo exists and is referenced from main repo
L23 | No first-party AI features | CONFIRMED | https://toolchase.com/tool/logseq/ | third-party listing states no first-party AI; weak secondary source, treat as best-available
L25 | Windows/macOS/Linux desktop + Android/iOS apps | STILL-UNVERIFIED | https://github.com/logseq/logseq | README confirms desktop; mobile app stores not re-fetched
L27 | App free; Sync beta priced $5/$15 via Open Collective | STILL-UNVERIFIED | https://blog.logseq.com/how-to-setup-and-use-logseq-sync/ | pricing pages not re-fetched
L29 | Sentiment: outliner praise, sync data-loss complaints | STILL-UNVERIFIED | https://www.reddit.com/r/logseq/comments/17ci4ac/leaving_logseq/ | sentiment threads not re-fetched
L31 | Pull-from framing on db-sync and marketplace | CONFIRMED | https://github.com/logseq/logseq/blob/master/deps/db-sync/README.md | db-sync and marketplace both verified live

## Joplin

L37 | AGPL-3.0-or-later license | CONFIRMED | https://github.com/laurent22/joplin/blob/dev/LICENSE | LICENSE fetched, AGPL-3.0
L37 | Repo laurent22/joplin active | CONFIRMED | https://github.com/laurent22/joplin | repo fetched
L37 | MIT-to-AGPL switch announced 2022-12-21 | CONFIRMED | https://joplinapp.org/news/20221221-agpl/ | news page verified
L39 | TypeScript/Electron desktop, React Native mobile, CLI | CONFIRMED | https://github.com/laurent22/joplin | README describes stack
L39 | Open-format storage; full-text search all platforms | CONFIRMED | https://joplinapp.org/ | site states open format
L39 | Stateless sync, E2EE spec | CONFIRMED | https://github.com/laurent22/joplin/blob/master/readme/spec/e2ee.md | spec referenced from repo
L41 | Notebooks/notes/todos, Markdown + plugins/themes, extension API | CONFIRMED | https://joplinapp.org/ | site feature list
L41 | Web Clipper for Firefox/Chrome | CONFIRMED | https://github.com/laurent22/joplin | README documents clipper
L41 | Note history/revisions, Evernote import, sub-notebooks, alarms | CONFIRMED | https://github.com/laurent22/joplin | README feature list
L41 | OCR of images not captured | REVISED | https://joplinapp.org/help/apps/ocr/ | OCR docs page live; official OCR shipped in v2.14 (https://joplinapp.org/news/20240301-release-2-14/), March 2024
L43 | Sync targets: Joplin Cloud, Dropbox, OneDrive, WebDAV, Nextcloud, S3 | CONFIRMED | https://joplinapp.org/help/apps/sync/ | official sync docs list targets
L43 | E2EE opt-in with password-protected Master Key | CONFIRMED | https://joplinapp.org/help/apps/sync/e2ee/ | docs fetched
L43 | Stateful caveats: per-client E2EE, mixed items, manual disable everywhere | CONFIRMED | https://github.com/laurent22/joplin/blob/master/readme/spec/e2ee.md | spec describes stateless-sync trade-offs
L43 | Shared notebooks use per-notebook keys | CONFIRMED | https://joplinapp.org/help/dev/spec/e2ee/workflow/ | workflow doc live
L43 | Self-hosted Joplin Server exists | CONFIRMED | https://github.com/laurent22/joplin | README documents Joplin Server
L45 | Open export format; Evernote import | CONFIRMED | https://joplinapp.org/ | site emphasizes export
L45 | JEX/raw export details | STILL-UNVERIFIED | https://joplinapp.org/help/ | help pages not re-fetched
L47 | Plugin/theme ecosystem via Extension API | CONFIRMED | https://joplinapp.org/ | plugin directory and API documented
L47 | First-party AI features not captured | REVISED | https://joplinapp.org/news/20260831-release-3-7/ | Joplin 3.7 (Aug 2026) added first-party AI chat and an MCP server, so this claim is now outdated
L49 | Platforms: Win/macOS/Linux/Android/iOS + terminal | CONFIRMED | https://joplinapp.org/ | site download list
L51 | Free; Joplin Cloud from $3.99/month | STILL-UNVERIFIED | https://joplinapp.org/pricing/ | pricing page not re-fetched
L53 | Sentiment praise and complaints | STILL-UNVERIFIED | https://www.reddit.com/r/joplinapp/comments/1mktp2r/i_love_joplin/ | threads not re-fetched
L55 | Pull-from: sync abstraction, E2EE spec, plugin API, clipper | CONFIRMED | https://github.com/laurent22/joplin/blob/master/readme/spec/e2ee.md | underlying artifacts all verified

## Notesnook

L61 | Clients GPLv3 since 2022-09-01 | CONFIRMED | https://notesnook.com/pricing | official pricing page fetched states "Client and server, GPLv3"
L61 | Sync server AGPLv3 | REVISED | https://github.com/streetwriters/notesnook-sync-server | sync server repo README still says AGPLv3, but the official pricing page now states "Client and server, GPLv3"; official page wins, conflict noted
L61 | Sync server repo streetwriters/notesnook-sync-server | CONFIRMED | https://github.com/streetwriters/notesnook-sync-server | repo fetched
L61 | Main client repo streetwriters/notesnook | CONFIRMED | https://github.com/streetwriters/notesnook | repo exists, fetched via search-surfaced URL
L63 | Local-first clients desktop/mobile/web | CONFIRMED | https://notesnook.com/ | site describes local-first
L63 | React + ProseMirror-based editor | STILL-UNVERIFIED | https://github.com/streetwriters/notesnook | editor internals not re-verified from repo
L63 | Full export to HTML/Markdown/PDF/Text | CONFIRMED | https://notesnook.com/ | export stated as product principle on official site
L65 | Monographs shareable E2EE notes | CONFIRMED | https://notesnook.com/monographs | product page live
L65 | 2FA with email + authenticator + password layers | CONFIRMED | https://notesnook.com/ | security features documented on site
L65 | Local backups | CONFIRMED | https://notesnook.com/ | backups documented on site
L67 | E2EE sync across devices through Streetwriters servers | CONFIRMED | https://notesnook.com/pricing | official page describes E2EE sync
L67 | Self-hostable sync server in alpha | REVISED | https://github.com/streetwriters/notesnook-sync-server | repo now says self-hosting is possible but without support; no longer described as alpha
L67 | Real-time collaboration not captured | STILL-UNVERIFIED | https://github.com/streetwriters/notesnook-sync-server | no fresh evidence either way
L69 | Export HTML/MD/PDF/Text; Monograph publishing | CONFIRMED | https://notesnook.com/ | both documented on official site
L71 | No plugin marketplace; AI not captured | STILL-UNVERIFIED | https://notesnook.com/ | site shows no plugin marketplace; AI status not re-verified
L73 | Platforms Win/macOS/Linux/Android/iOS/web | CONFIRMED | https://notesnook.com/ | download list on site
L75 | Free core + paid Pro; in-app cancellation and refunds | CONFIRMED | https://notesnook.com/pricing | pricing page fetched
L75 | Exact Pro price | STILL-UNVERIFIED | https://notesnook.com/pricing | numeric tier price not captured in fetch
L77 | Sentiment: editor praise, search complaints, markdown backlash | STILL-UNVERIFIED | https://www.reddit.com/r/Notesnook/comments/1rddynp/im_done_with_notesnook_rant/ | threads not re-fetched
L79 | Pull-from: Monographs, sync-server separation, 2FA UX, export policy | CONFIRMED | https://notesnook.com/monographs | underlying features verified on official site

## Trilium Notes / TriliumNext

L85 | AGPL-3.0 | CONFIRMED | https://github.com/TriliumNext/Trilium | repo fetched, AGPL-3.0 LICENSE
L85 | Original zadam/trilium; continuation took over | CONFIRMED | https://github.com/TriliumNext/Trilium | continuation repo fetched and active
L85 | Continuation named TriliumNext/Notes | REVISED | https://github.com/TriliumNext/Trilium | the repo has been renamed to TriliumNext/Trilium; master should use the new path
L85 | Docs at triliumnext.github.io and docs.triliumnotes.org | CONFIRMED | https://docs.triliumnotes.org/ | docs site live
L87 | SQLite database holds notes/tree/metadata | CONFIRMED | https://docs.triliumnotes.org/user-guide/advanced-usage/database | official docs
L87 | HTML in DB, not source files; Markdown import/export | CONFIRMED | https://docs.triliumnotes.org/ | docs describe storage model
L87 | Electron desktop + self-hostable Docker server | CONFIRMED | https://github.com/TriliumNext/Trilium | README documents both
L87 | English-only policy; historical macOS gap | STILL-UNVERIFIED | https://triliumnext.github.io/Docs/Wiki/faq.html | FAQ not re-fetched
L89 | Multi-parent hierarchy, hoisting, versioning, scripting | CONFIRMED | https://docs.triliumnotes.org/ | docs describe tree, hoisting, versioning, scripting
L89 | Note types incl. mind-map view | CONFIRMED | https://docs.triliumnotes.org/ | note-type docs list mind map
L89 | Day notes, backlinks, web sharing UNVERIFIED | REVISED | https://docs.triliumnotes.org/user-guide/note-types/text/links | backlinks documented on official docs page; day notes and sharing remain unverified here
L91 | Server-based sync, clients to Trilium Server | CONFIRMED | https://docs.triliumnotes.org/developer-guide/concepts/sync | sync docs page live
L91 | No E2EE on standard sync path | REVISED | https://docs.triliumnotes.org/developer-guide/architecture/security | security docs describe per-note encryption; sync-path E2EE scope still not fully pinned down
L91 | No multi-user support | CONFIRMED | https://github.com/TriliumNext/Trilium | README states single-user
L93 | Markdown import; ZIP-based export | CONFIRMED | https://docs.triliumnotes.org/ | import/export documented
L95 | Scripting as extension mechanism | CONFIRMED | https://docs.triliumnotes.org/ | scripting docs live
L95 | Trilium AI features not captured | STILL-UNVERIFIED | https://github.com/TriliumNext/Trilium | no fresh evidence
L97 | Windows/Linux desktop; no dedicated mobile app | CONFIRMED | https://github.com/TriliumNext/Trilium | README lists desktop; mobile absent
L97 | macOS unsupported historically | STILL-UNVERIFIED | https://github.com/zadam/trilium/wiki/FAQ/047d5f76a52eaaa9c5563ccba9581f6163d309ea | wiki not re-fetched
L99 | Fully free, no paid tier | CONFIRMED | https://github.com/TriliumNext/Trilium | no paid offering found
L101 | Sentiment praise and complaints | STILL-UNVERIFIED | https://www.reddit.com/r/selfhosted/comments/1ed8h9c/triliumnext_notes_the_last_note_taking_app_you/ | threads not re-fetched
L103 | Pull-from: attributes/versioning, hoisting, scripting, SQLite schema | CONFIRMED | https://docs.triliumnotes.org/ | underlying features verified

## AFFiNE

L109 | Root LICENSE MIT with listed exceptions | CONFIRMED | https://github.com/toeverything/affine | root LICENSE fetched, MIT
L109 | Backend/common-native MPL 2.0 for CE, EE terms for rest | REVISED | https://github.com/toeverything/affine | the CE repo is now simply MIT at the root; the pricing-page component-licensing language is no longer the license mechanism in the fetched repo
L109 | BlockSuite editor MIT-licensed | REVISED | https://github.com/toeverything/blocksuite | blocksuite repo LICENSE fetched: MPL 2.0, not MIT
L109 | Backlash over "not actually MIT" marketing | STILL-UNVERIFIED | https://www.reddit.com/r/foss/comments/1pn98l0/affine_is_evil_and_misleading_is_not_actually_mit/ | thread not re-fetched
L111 | Editor built on BlockSuite | CONFIRMED | https://github.com/toeverything/blocksuite | repo fetched, self-describes as behind AFFiNE
L111 | PageEditor/EdgelessEditor + CopilotPanel fragments | CONFIRMED | https://github.com/toeverything/blocksuite | README describes components
L111 | Local-first workspace | CONFIRMED | https://affine.pro/ | site describes local-first
L111 | Sync engine internals | STILL-UNVERIFIED | https://github.com/toeverything/AFFiNE | not re-verified
L113 | Docs + whiteboard + databases; edgeless canvas blocks | CONFIRMED | https://github.com/toeverything/affine | README describes
L113 | Slash menu with GitHub/Figma embeds | STILL-UNVERIFIED | https://betterstack.com/community/guides/linux/affine/ | guide not re-fetched
L113 | Optional AI | CONFIRMED | https://affine.pro/ | AI positioned on site
L115 | Cloud workspaces; self-host free up to 10 seats | CONFIRMED | https://affine.pro/pricing | pricing page live
L115 | Docker image per stable release | STILL-UNVERIFIED | https://www.reddit.com/r/selfhosted/comments/1b0dyqt/affinepro_our_notionmiro_open_source_alternative/ | post not re-fetched
L115 | E2EE not captured | REVISED | https://affine.pro/blog/faq | official FAQ says to expect E2EE support "in the near future"; not fully live on AFFiNE Cloud today
L117 | Bulk markdown export broken per PSA thread | STILL-UNVERIFIED | https://www.reddit.com/r/PKMS/comments/1oaddib/psa_do_not_use_affine_underhanded_nonsense/ | thread not re-fetched
L119 | BlockSuite fragments as extension substrate | CONFIRMED | https://github.com/toeverything/blocksuite | README describes fragment architecture
L121 | Desktop + web; mobile app late and lagging | CONFIRMED | https://affine.pro/ | official site lists desktop/web/mobile apps; lagging claim from Reddit remains unverified
L123 | Free self-host 10 seats; cloud Pro/Team | CONFIRMED | https://affine.pro/pricing | pricing page fetched
L125 | Sentiment: praise and complaints incl. lag, export, license anger | STILL-UNVERIFIED | https://www.reddit.com/r/PKMS/comments/1gcm3vj/appflowy_vs_affine/ | threads not re-fetched
L127 | Pull-from: BlockSuite block model, local-first UX, licensing cautionary tale | CONFIRMED | https://github.com/toeverything/blocksuite | BlockSuite verified with corrected license

## Anytype

L133 | any-sync protocol MIT | CONFIRMED | https://github.com/anyproto/any-sync | repo LICENSE fetched, MIT
L133 | Desktop client under Any Source Available License | CONFIRMED | https://github.com/anyproto/anytype-ts | repo fetched; states "Licensed under the Any Source Available License 1.0"
L133 | anytype-ts Electron + TypeScript | CONFIRMED | https://github.com/anyproto/anytype-ts | repo README
L133 | Org anyproto; anytype-heart Go library | CONFIRMED | https://github.com/anyproto | org page fetched
L135 | Local-first P2P E2EE on any-sync | CONFIRMED | https://github.com/anyproto/any-sync | repo README
L135 | gRPC API extensibility | CONFIRMED | https://github.com/anyproto/anytype-ts | README documents gRPC
L135 | Zero-knowledge encryption | CONFIRMED | https://github.com/anyproto/anytype-ts | README describes zero-knowledge encryption
L137 | Composable blocks: text, databases, kanban, calendar, custom Types | CONFIRMED | https://github.com/anyproto/anytype-ts | README features
L137 | Objects/types/relations, graph view, templates | CONFIRMED | https://anytype.io/ | site describes object model
L137 | AI "Agents" extensibility | STILL-UNVERIFIED | https://github.com/anyproto/anytype-ts | not re-verified from repo
L137 | Local-only mode or self-hosted backup node | CONFIRMED | https://anytype.io/faq/ | FAQ fetched, both options stated
L139 | P2P device sync with optional encrypted backup | CONFIRMED | https://anytype.io/faq/ | FAQ describes sync model
L139 | Free tier up to 10 shared channels | STILL-UNVERIFIED | https://aiproductivity.ai/tools/anytype/ | secondary source not re-fetched
L141 | Import/migration from Notion, Evernote | CONFIRMED | https://anytype.io/ | importers documented on site
L141 | Export details | STILL-UNVERIFIED | https://doc.anytype.io | docs not re-fetched
L143 | gRPC API and AI agents; MCP server | CONFIRMED | https://github.com/anyproto | org lists MCP server repo
L145 | macOS/Windows/Linux desktop; iOS and Android apps | CONFIRMED | https://github.com/anyproto | org lists native iOS (Swift) and Android (Kotlin) client repos
L145 | Web app UNVERIFIED | STILL-UNVERIFIED | https://anytype.io | no web app evidence found this session
L147 | Core app free; paid memberships for backup/sync capacity | CONFIRMED | https://anytype.io/pricing/ | pricing page live
L147 | Educator/student 50% discount | STILL-UNVERIFIED | https://anytype.io/pricing/ | discount line not re-captured
L149 | Sentiment: sync praise, no complaint thread | STILL-UNVERIFIED | https://download.anytype.io/ | testimonials not re-fetched
L151 | Pull-from: any-sync protocol, local-only/backup-node spectrum, object model | CONFIRMED | https://github.com/anyproto/any-sync | all three verified

## ente (ente Notes)

L157 | Fully open source monorepo github.com/ente/ente | CONFIRMED | https://github.com/ente/ente | repo fetched
L157 | "End-to-end encrypted photos, authenticators and more" | CONFIRMED | https://github.com/ente/ente | README states E2EE photos/auth/more
L157 | Specific Notes app license | STILL-UNVERIFIED | https://github.com/ente/ente | LICENSE file not directly captured
L157 | Ente stresses exportability | CONFIRMED | https://ente.com/auth/ | export principle stated
L159 | E2EE via Libsodium, encrypted before leaving device | CONFIRMED | https://hasgeek.com/rootconf/ente-self-hosting-images-technical-review/sub/review-of-ente-an-open-source-e2ee-self-hosted-alt-FK8L54TNuHrQBsivJJgDHW | technical review fetched
L159 | Self-hosting via Docker Compose documented | CONFIRMED | https://github.com/ente/ente | self-host docs in repo
L159 | Notes one product line alongside Photos and Auth | REVISED | https://github.com/ente/ente | repo fetched: there is no standalone ente Notes product; notes functionality lives inside the platform (Ente Locker) and Ensu is a separate AI-chat app, not the notes client
L161 | Rich text + checkbox notes inside ente platform | REVISED | https://github.com/ente/ente/releases | release notes reference note behavior, but the framing "Ensu notes client" in the master conflates Ensu (AI chat app) with notes; notes are not a standalone product line
L161 | Detailed feature list | STILL-UNVERIFIED | https://ente.io/notes | no fresh capture
L163 | E2EE sync via ente servers; self-hostable server | CONFIRMED | https://github.com/ente/ente | sync and self-host architecture in repo
L165 | Export/import as product principle | CONFIRMED | https://ente.com/auth/ | stated on site
L167 | AI-assisted features in notes-line release notes | REVISED | https://github.com/ente/ente/releases | AI features appear in Ensu/monorepo releases; they are not attributable to a standalone Notes product
L169 | Ente Auth on Android/iOS/Mac/Windows/Linux/Web | CONFIRMED | https://f-droid.org/en/packages/io.ente.auth/ | F-Droid listing live
L169 | Notes app platforms beyond mobile | STILL-UNVERIFIED | https://ente.io/notes | no fresh capture
L171 | Free tier + paid storage plans | CONFIRMED | https://ente.io/pricing | pricing page live
L173 | Sentiment | STILL-UNVERIFIED | https://www.reddit.com/r/ente/ | threads not re-fetched
L175 | Pull-from: monorepo shared E2EE core, Libsodium trust model, export principle | CONFIRMED | https://github.com/ente/ente | all three verified

## Saber

L181 | GPL-3.0 | CONFIRMED | https://github.com/saber-notes | org license listing fetched
L181 | Repo saber-notes/saber | CONFIRMED | https://github.com/saber-notes/saber | repo fetched
L183 | Flutter/Dart handwriting app | CONFIRMED | https://github.com/saber-notes/saber | repo README
L183 | Storage format details | STILL-UNVERIFIED | https://github.com/saber-notes/saber | per-note container format not re-captured
L185 | Handwriting-first, PDF import/annotation | CONFIRMED | https://github.com/saber-notes/saber | README describes
L185 | Experimental Windows stylus patches | STILL-UNVERIFIED | https://github.com/saber-notes/saber/releases | releases not re-fetched
L187 | Native Nextcloud sync headline capability | CONFIRMED | https://github.com/saber-notes/saber | README documents Nextcloud sync
L187 | Self-hostable server component | CONFIRMED | https://github.com/saber-notes | org lists sync server repo
L187 | E2EE on sync not captured | REVISED | https://github.com/saber-notes/saber | README states notes are end-to-end encrypted, with a second password option for additional protection; dual-password E2EE confirmed
L189 | PDF import/annotation workflow | CONFIRMED | https://github.com/saber-notes/saber | README
L189 | Export matrix | STILL-UNVERIFIED | https://saber.adil.hanney.org | site not re-fetched
L191 | No plugin ecosystem | STILL-UNVERIFIED | https://github.com/saber-notes/saber | no fresh evidence
L193 | Android, iOS, Windows, macOS, Linux | CONFIRMED | https://github.com/saber-notes/saber | README platform list
L195 | Free and open source | CONFIRMED | https://github.com/saber-notes/saber | README
L197 | Sentiment: Nextcloud praise, slow long-note complaint | STILL-UNVERIFIED | https://www.reddit.com/r/NextCloud/ | threads not re-fetched
L199 | Pull-from: Nextcloud sync story, Flutter ink pipeline, stylus polish | CONFIRMED | https://github.com/saber-notes/saber | underlying facts verified

## Xournal++

L205 | GPL-2.0 per Snapcraft; GPLv3 per contributors unresolved | STILL-UNVERIFIED | https://github.com/xournalpp/xournalpp/blob/master/LICENSE | raw LICENSE fetch refused again this session; repo page fetched but license line not captured; GPL-2.0 vs GPL-3.0 remains unresolved
L205 | Repo xournalpp/xournalpp | CONFIRMED | https://github.com/xournalpp/xournalpp | repo fetched
L207 | C++ with GTK3 | CONFIRMED | https://github.com/xournalpp/xournalpp | repo README
L207 | .xoj/.xopp XML format with PDF annotation layer | REVISED | https://github.com/xournalpp/xournalpp | repo fetched: .xopp files are gzipped XML documents; the format claim itself is confirmed with that refinement
L209 | PDF annotation, pressure input, LaTeX, audio recording synced | CONFIRMED | https://github.com/xournalpp/xournalpp | README features
L209 | ~15k GitHub stars; latest v1.3.5 | STILL-UNVERIFIED | https://github.com/xournalpp/xournalpp/releases | releases page not re-fetched for exact version
L209 | 20+ translations via Crowdin | CONFIRMED | https://github.com/xournalpp/xournalpp | README notes Crowdin translations
L211 | No sync; desktop document tool | CONFIRMED | https://github.com/xournalpp/xournalpp | no sync features in README
L213 | PDF export with flattening | CONFIRMED | https://github.com/xournalpp/xournalpp | export documented in README
L215 | Plugin system exists | REVISED | https://github.com/xournalpp/xournalpp | repo fetched: plugin system confirmed, Lua-based plugins documented
L215 | No AI features | CONFIRMED | https://github.com/xournalpp/xournalpp | no AI features in README
L217 | Linux, macOS, Windows only; third-party Android wrapper | CONFIRMED | https://github.com/xournalpp/xournalpp | README lists three desktop platforms
L219 | Free and open source | CONFIRMED | https://github.com/xournalpp/xournalpp | README
L221 | Sentiment | STILL-UNVERIFIED | https://www.reddit.com/r/XournalPP/ | threads not re-fetched
L223 | Pull-from: ink renderer, PDF-background annotation, LaTeX pattern | CONFIRMED | https://github.com/xournalpp/xournalpp | underlying facts verified

## RNote

L229 | GPL-3.0 | CONFIRMED | https://github.com/flxzt/rnote | repo LICENSE fetched, GPL-3.0-or-later
L229 | Repo flxzt/rnote | CONFIRMED | https://github.com/flxzt/rnote | repo fetched
L231 | Rust + GTK4/libadwaita vector sketchbook | CONFIRMED | https://github.com/flxzt/rnote | repo README
L231 | Native .rnote document format | REVISED | https://github.com/flxzt/rnote | repo fetched: .rnote is gzipped JSON and the README warns the format is still unstable across versions
L231 | Community Vue 3 web port exists | STILL-UNVERIFIED | https://github.com/QiXinia/Rnote_Vue | not re-fetched
L233 | Infinite canvas, PDF/image import-export, adaptive pen/keyboard UI | CONFIRMED | https://github.com/flxzt/rnote | README features
L233 | Selection/transform, pen pressure, pattern tools | CONFIRMED | https://github.com/flxzt/rnote | README describes pressure and tools
L235 | No sync; file-based bring-your-own | CONFIRMED | https://github.com/flxzt/rnote | no sync feature in README
L237 | PDF and picture import/export | CONFIRMED | https://github.com/flxzt/rnote | README
L239 | No plugins, no AI | CONFIRMED | https://github.com/flxzt/rnote | neither in README
L241 | Linux primarily, Flatpak; Windows/macOS availability UNVERIFIED | REVISED | https://github.com/flxzt/rnote | README fetched: Linux, macOS and Windows are all listed as available; not Linux-primary-only
L243 | Free and open source | CONFIRMED | https://github.com/flxzt/rnote | README
L245 | Sentiment: r/linux praise, HN Show HN | STILL-UNVERIFIED | https://news.ycombinator.com/item?id=30025327 | threads not re-fetched
L247 | Pull-from: Rust ink engine, GTK4 UI patterns, vector-stroke storage | CONFIRMED | https://github.com/flxzt/rnote | underlying facts verified

## Excalidraw

L253 | MIT license | CONFIRMED | https://github.com/excalidraw/excalidraw | repo LICENSE fetched, MIT
L253 | Repo excalidraw/excalidraw | CONFIRMED | https://github.com/excalidraw/excalidraw | repo fetched
L255 | React + TypeScript whiteboard; scenes as JSON | CONFIRMED | https://github.com/excalidraw/excalidraw | repo README
L255 | excalidraw-room collaboration server | CONFIRMED | https://github.com/excalidraw/excalidraw-room | repo exists
L257 | Hand-drawn diagramming, libraries, real-time collab, E2EE sessions | CONFIRMED | https://github.com/excalidraw/excalidraw | README describes E2EE collaboration and shared elements
L257 | VS Code extension | STILL-UNVERIFIED | https://marketplace.visualstudio.com/items?itemName=excalidraw.excalidraw | marketplace not re-fetched
L259 | Multiplayer via excalidraw-room with E2EE | CONFIRMED | https://github.com/excalidraw/excalidraw-room | room README describes end-to-end encryption
L259 | Persistent file sync not the model | CONFIRMED | https://github.com/excalidraw/excalidraw | scene files user-managed
L261 | Export PNG/SVG and scene JSON | CONFIRMED | https://github.com/excalidraw/excalidraw | README lists exports
L263 | Embeddable npm package @excalidraw/excalidraw | CONFIRMED | https://github.com/excalidraw/excalidraw | README documents @excalidraw/excalidraw package
L263 | AI features (image-to-diagram, text-to-diagram) Excalidraw+ paid | STILL-UNVERIFIED | https://plus.excalidraw.com | Excalidraw+ pages not re-fetched
L263 | Open-source plugin ecosystem | REVISED | https://github.com/excalidraw/excalidraw | repo fetched: README notes drop-in plugin support is planned, not a shipped ecosystem today
L265 | Web app + npm package; no native desktop/mobile apps | CONFIRMED | https://github.com/excalidraw/excalidraw | README: web-first, embedding via package
L267 | Excalidraw+ at $6/user/month annual or $7 monthly | STILL-UNVERIFIED | https://plus.excalidraw.com | pricing page not re-fetched
L269 | Sentiment | STILL-UNVERIFIED | https://www.reddit.com/r/webdev/ | threads not re-fetched
L271 | Pull-from: E2EE room-server design, embeddable-package model, ink smoothing | CONFIRMED | https://github.com/excalidraw/excalidraw-room | room design verified

## AppFlowy

L277 | AGPLv3 | CONFIRMED | https://github.com/AppFlowy-IO/AppFlowy | repo LICENSE fetched, AGPL-3.0
L277 | Repo AppFlowy-IO/AppFlowy | CONFIRMED | https://github.com/AppFlowy-IO/AppFlowy | repo fetched
L279 | Flutter frontend + Rust core | CONFIRMED | https://github.com/AppFlowy-IO/AppFlowy | repo README
L279 | Block editor, Grid/Board/Calendar/Gallery views, slash commands | CONFIRMED | https://github.com/AppFlowy-IO/AppFlowy | README features
L279 | CRDT-based offline-first sync | CONFIRMED | https://github.com/AppFlowy-IO/AppFlowy | README describes offline-first sync
L279 | Commercially licensed self-host fork | STILL-UNVERIFIED | https://forum.appflowy.com/ | forum not re-fetched for this specific claim
L281 | Notion-style blocks, kanban, databases, templates | CONFIRMED | https://github.com/AppFlowy-IO/AppFlowy | README
L283 | No E2EE acknowledged by maintainer | CONFIRMED | https://forum.appflowy.com/t/791 | maintainer forum answer states AppFlowy is not designed to be end-to-end encrypted at this time; corroborated at https://forum.appflowy.com/t/4679
L283 | AppFlowy Cloud plus self-host | CONFIRMED | https://github.com/AppFlowy-IO/AppFlowy | cloud and self-host documented
L285 | Export limitations reported | STILL-UNVERIFIED | https://www.reddit.com/r/AppFlowy/ | threads not re-fetched
L287 | AI features in cloud offering | CONFIRMED | https://github.com/AppFlowy-IO/AppFlowy | AI integration documented in README
L287 | Plugin system details | STILL-UNVERIFIED | https://github.com/AppFlowy-IO/AppFlowy | not re-verified
L289 | Desktop Win/macOS/Linux, mobile, web | CONFIRMED | https://github.com/AppFlowy-IO/AppFlowy | README platform list
L291 | Free core; cloud and commercial fork paid tiers | CONFIRMED | https://appflowy.io/pricing | pricing page live
L293 | Sentiment: momentum praise, licensing and sync complaints | STILL-UNVERIFIED | https://www.reddit.com/r/selfhosted/ | threads not re-fetched
L295 | Pull-from: Flutter+Rust split, CRDT machinery, open-core cautionary tale | CONFIRMED | https://github.com/AppFlowy-IO/AppFlowy | underlying facts verified

## Outline

L301 | BSL 1.1 license | CONFIRMED | https://www.bitdoze.com/outline-install/ | self-host guides state BSL 1.1; corroborated by https://contabo.com/blog/best-self-hosted-wiki-tools/ — direct outline/outline repo fetch refused again this session
L301 | Repo outline/outline | STILL-UNVERIFIED | https://github.com/outline/outline | direct repo fetch refused; existence corroborated by search captures
L303 | React frontend + Node.js backend | CONFIRMED | https://docs.getoutline.com/s/guide/ | official docs describe the stack
L303 | ProseMirror-based markdown editor | CONFIRMED | https://docs.getoutline.com/s/guide/ | docs describe the editor
L303 | Data in Postgres | CONFIRMED | https://docs.getoutline.com/s/hosting/ | self-hosting docs require Postgres
L305 | Collections, docs, nested docs, comments, search, Slack, API keys | CONFIRMED | https://docs.getoutline.com/s/guide/ | official docs
L305 | Built-in MCP server | CONFIRMED | https://docs.getoutline.com/s/guide/ | MCP integration documented in official docs
L307 | Real-time collaborative editing | CONFIRMED | https://docs.getoutline.com/s/guide/ | documented
L307 | Self-host requires external OIDC + Postgres + Redis + S3/Minio | CONFIRMED | https://docs.getoutline.com/s/hosting/ | hosting docs list these requirements
L307 | No E2EE | CONFIRMED | https://docs.getoutline.com/s/guide/ | wiki model, no E2EE documented
L309 | Public sharing/publishing of docs | CONFIRMED | https://docs.getoutline.com/s/guide/ | share links documented
L311 | MCP server built in; Slack integrations | CONFIRMED | https://docs.getoutline.com/s/guide/ | documented
L313 | Mobile apps exist | DENIED | https://docs.getoutline.com/s/guide/doc/the-app-Ez4bmY6VDD | official docs: there are no native mobile apps; mobile is a responsive PWA. Desktop apps for macOS/Windows exist, which revises "desktop via web wrapper" toward native shells
L315 | Self-host free with BSL restrictions; Cloud paid per user | CONFIRMED | https://www.getoutline.com/pricing | pricing page captured via search
L317 | Sentiment: UI praise, self-hosting difficulty dominant complaint | STILL-UNVERIFIED | https://www.reddit.com/r/selfhosted/ | threads not re-fetched
L319 | Pull-from: MCP pattern, ProseMirror reference, BSL cautionary tale | CONFIRMED | https://docs.getoutline.com/s/guide/ | underlying facts verified

## Standard Notes

L325 | GPL-3.0 | CONFIRMED | https://github.com/standardnotes/server | server repo fetched, GPL-3.0; client app repo also GPL-3.0 per directory listings
L325 | Repos standardnotes/app (client), syncing-server (server) | REVISED | https://github.com/standardnotes/self-hosted | the syncing-server path is legacy; the server now lives at standardnotes/server (fetched, GPL-3.0)
L325 | Server license not captured | REVISED | https://github.com/standardnotes/server | server repo fetched this session: GPL-3.0
L327 | E2EE by default, encrypted at client before sync | CONFIRMED | https://standardnotes.com | site describes E2EE by default
L327 | Stack internals (TypeScript client) | STILL-UNVERIFIED | https://github.com/standardnotes/app | client repo not re-fetched
L329 | Plain/secure notes, extensions, web clipper | CONFIRMED | https://standardnotes.com | site features
L331 | Encrypted sync via SN servers; self-hosting possible | CONFIRMED | https://github.com/standardnotes/server | server repo fetched, self-host documented
L331 | No real-time collaboration | CONFIRMED | https://standardnotes.com | no collab feature documented
L333 | Data export available | CONFIRMED | https://standardnotes.com | export documented
L335 | AI agents in marketing | STILL-UNVERIFIED | https://standardnotes.com | AI claims not re-captured
L335 | Extensions gated to paid plans | CONFIRMED | https://standardnotes.com/plans | plans page fetched
L337 | Web, desktop, mobile | CONFIRMED | https://standardnotes.com | platform list
L339 | Free tier unlimited notes/E2EE/sync; paid ~$4.17-7.50/month | REVISED | https://standardnotes.com/plans | official plans page fetched: free core with paid Productivity and Professional tiers; comparison-page price range is plausible but the official page is the authority
L341 | Sentiment: privacy praise, buggier editors complaints | STILL-UNVERIFIED | https://www.reddit.com/r/PrivacyGuides/ | threads not re-fetched
L343 | Pull-from: E2EE default, extensions/editors model, editor-quality cautionary tale | CONFIRMED | https://standardnotes.com | underlying facts verified

## HelixNotes

L349 | AGPL-3.0 | CONFIRMED | https://alternativeto.net/software/helixnotes/about/ | listing states AGPL-3.0; helixnotes.com states open source
L349 | Source moved Codeberg to GitLab | CONFIRMED | https://gitlab.com/ArkHost/HelixNotes | GitLab project exists; page returned a loading shell only, so repo contents not inspected
L349 | Archived 2026-07-23 | DENIED | https://apps.apple.com/us/app/helixnotes/id6788490726 | App Store listing live and current; project actively developed, so the archived flag from a listing is wrong
L349 | Built by Yuri Karamian of ArkHost | STILL-UNVERIFIED | https://helixnotes.com | about-page attribution not re-captured
L351 | Rust + Tauri 2.0 + SvelteKit UI | CONFIRMED | https://helixnotes.com | site describes the stack
L351 | Plain .md files with YAML frontmatter, notebooks are folders | CONFIRMED | https://helixnotes.com | site describes storage
L351 | Tantivy full-text search | CONFIRMED | https://helixnotes.com | site names Tantivy
L351 | No server, no telemetry | CONFIRMED | https://helixnotes.com | site states local-only posture
L353 | Wiki-links, graph view, outline panel, daily notes, tags, KaTeX, Mermaid, version history, backups | CONFIRMED | https://helixnotes.com | feature list on site
L353 | AI via local Ollama or user API keys | CONFIRMED | https://helixnotes.com | site describes local-AI options
L353 | Current version v1.3.6 | CONFIRMED | https://helixnotes.com | release/version listing
L355 | No built-in sync server; user-managed files | CONFIRMED | https://helixnotes.com | no sync server advertised
L357 | Markdown-native portability | CONFIRMED | https://helixnotes.com | plain files
L359 | No plugin marketplace; version history/backups/search first-class | CONFIRMED | https://helixnotes.com | site positions these as built-in
L361 | Linux (AppImage/.deb/AUR/Solus), Windows, macOS, Android, iPhone/iPad | CONFIRMED | https://helixnotes.com | platform list; corroborated by https://apps.apple.com/us/app/helixnotes/id6788490726
L363 | Free and open source | CONFIRMED | https://helixnotes.com | site states
L365 | Sentiment: r/opensource praise | STILL-UNVERIFIED | https://www.reddit.com/r/opensource/ | thread not re-fetched
L367 | Pull-from: Rust+Tauri+SvelteKit stack, Tantivy, files-first, local-AI-first | CONFIRMED | https://helixnotes.com | all four verified

## Lockbook

L373 | Unlicense (public domain) | CONFIRMED | https://github.com/lockbook/lockbook | repo LICENSE fetched, Unlicense
L373 | Repo lockbook/lockbook | CONFIRMED | https://github.com/lockbook/lockbook | repo fetched
L375 | Rust core lb-rs handles encryption/sync/storage | CONFIRMED | https://github.com/lockbook/lockbook | repo README
L375 | db-rs embedded append-only store | CONFIRMED | https://github.com/lockbook/lockbook | repo docs describe db-rs
L375 | E2EE via elliptic-curve cryptography | CONFIRMED | https://github.com/lockbook/lockbook | docs describe E2EE design
L375 | Native clients, not web wrappers | CONFIRMED | https://lockbook.net | site describes native apps
L377 | Markdown notes plus SVG drawings; CLI support | CONFIRMED | https://github.com/lockbook/lockbook | README describes notes, drawings, CLI
L377 | Compression-based free-tier accounting | CONFIRMED | https://lockbook.net | usage accounting described
L377 | Open beta status | STILL-UNVERIFIED | https://github.com/lockbook/lockbook | not re-captured
L379 | E2EE sync through Lockbook servers, client-side encryption | CONFIRMED | https://github.com/lockbook/lockbook | architecture documented
L379 | Self-host path not captured | REVISED | https://lockbook.net/docs/self-hosting.html | official self-hosting docs page exists
L381 | Export details | STILL-UNVERIFIED | https://lockbook.net | not re-captured
L383 | No plugin ecosystem; no AI | CONFIRMED | https://github.com/lockbook/lockbook | neither documented
L385 | macOS, iPhone/iPad, Android, Windows, Linux | CONFIRMED | https://github.com/lockbook/lockbook | README platform list
L387 | Free tier + paid tiers exist | CONFIRMED | https://apps.apple.com/us/app/lockbook/id1526775001 | App Store listing fetched: premium at $2.99/month for 30 GB
L387 | Paid tier price | CONFIRMED | https://apps.apple.com/us/app/lockbook/id1526775001 | premium $2.99/month, 30 GB
L389 | Sentiment: thin capture, one weak-source testimonial | STILL-UNVERIFIED | https://www.reddit.com/r/privacy/ | threads not re-fetched
L391 | Pull-from: Rust-core + native shells, E2EE elliptic-curve design, db-rs | CONFIRMED | https://github.com/lockbook/lockbook | all three verified

## Tolaria

L397 | AGPL-3.0 | CONFIRMED | https://github.com/refactoringhq/tolaria | repo LICENSE fetched, AGPL-3.0-or-later
L397 | Repo refactoringhq/tolaria | CONFIRMED | https://github.com/refactoringhq/tolaria | repo fetched
L397 | By Luca Rossi of Refactoring newsletter | STILL-UNVERIFIED | https://refactoringhq.github.io/tolaria/ | attribution not re-captured
L399 | Desktop app macOS/Windows/Linux + iPhone/iPad | CONFIRMED | https://github.com/refactoringhq/tolaria | README lists desktop platforms; iPhone/iPad is a TestFlight beta per repo, so mobile is beta not general availability
L399 | Plain markdown with YAML frontmatter; vault is a git repo | CONFIRMED | https://github.com/refactoringhq/tolaria | README describes files-first git-first model
L399 | Tauri-based desktop app | CONFIRMED | https://github.com/refactoringhq/tolaria | README: Tauri + React + TypeScript
L399 | Homebrew cask distribution | STILL-UNVERIFIED | https://github.com/Homebrew/homebrew-cask | formula not re-fetched
L401 | Knowledge-base positioning "company docs as context for AI"; MCP server | CONFIRMED | https://github.com/refactoringhq/tolaria | README fetched: AI-agent positioning and an MCP server are documented
L401 | HN Show HN discussion exists | STILL-UNVERIFIED | https://news.ycombinator.com/item?id=47882697 | not re-fetched
L403 | Git-based sync by construction; no dedicated sync server | CONFIRMED | https://github.com/refactoringhq/tolaria | README
L403 | No collaboration features | CONFIRMED | https://github.com/refactoringhq/tolaria | none documented
L405 | Markdown-native portability; export details | STILL-UNVERIFIED | https://refactoringhq.github.io/tolaria/ | docs not re-fetched
L407 | AI-agent/memory positioning core differentiator | CONFIRMED | https://github.com/refactoringhq/tolaria | README
L409 | Platforms macOS/Windows/Linux/iPhone-iPad | CONFIRMED | https://github.com/refactoringhq/tolaria | README; mobile in TestFlight beta
L411 | Pricing not captured | REVISED | https://github.com/refactoringhq/tolaria | repo fetched: Tolaria is free and open source; the old "possibly paid" framing is resolved
L413 | Sentiment: positive r/macapps threads | STILL-UNVERIFIED | https://www.reddit.com/r/macapps/ | threads not re-fetched
L415 | Pull-from: vault-as-git-repo, AI-agents-as-audience, frontmatter discipline | CONFIRMED | https://github.com/refactoringhq/tolaria | all three verified

## Poznote

L421 | MIT license | CONFIRMED | https://github.com/timothepoznanski/poznote | repo fetched, MIT LICENSE
L421 | Repo timothepoznanski/poznote | CONFIRMED | https://github.com/timothepoznanski/poznote | repo fetched
L423 | PHP + SQLite, self-hosted via Docker | CONFIRMED | https://github.com/timothepoznanski/poznote | repo README
L423 | Rich text + Markdown + drawing editors; tags, Kanban, tasks, calendar | CONFIRMED | https://github.com/timothepoznanski/poznote | README features
L425 | Search, MCP server, REST API, graph view, AI assistant, multi-user, OIDC | CONFIRMED | https://github.com/timothepoznanski/poznote | README feature list
L425 | App passwords, webhooks, Git sync (GitHub/Forgejo), Chrome extension, PWA | CONFIRMED | https://github.com/timothepoznanski/poznote | README features
L425 | No native mobile app (PWA only) | CONFIRMED | https://github.com/timothepoznanski/poznote | README states PWA
L425 | No E2EE | CONFIRMED | https://github.com/timothepoznanski/poznote | no E2EE documented
L425 | Only outbound call is daily update check | CONFIRMED | https://github.com/timothepoznanski/poznote | README privacy note
L427 | Git sync to GitHub/Forgejo; multi-user with OIDC; no E2EE | CONFIRMED | https://github.com/timothepoznanski/poznote | README
L429 | Publishing/export details UNVERIFIED | REVISED | https://github.com/timothepoznanski/poznote | repo fetched: backup/export to file is documented; full export matrix still not captured
L431 | Built-in MCP server and REST API; AI assistant | CONFIRMED | https://github.com/timothepoznanski/poznote | README
L433 | Self-hosted web, PWA on mobile, Docker | CONFIRMED | https://github.com/timothepoznanski/poznote | README
L435 | Free and open source | CONFIRMED | https://poznote.com | site and repo
L437 | Sentiment | STILL-UNVERIFIED | https://www.reddit.com/r/selfhosted/ | threads not re-fetched
L439 | Pull-from: MCP+REST as first-class AI integration, privacy posture, drawing editor | CONFIRMED | https://github.com/timothepoznanski/poznote | all three verified

## Tangent Notes

L445 | Apache 2.0 | CONFIRMED | https://github.com/suchnsuch/Tangent | repo LICENSE fetched, Apache 2.0
L445 | Repo monorepo suchnsuch/Tangent | CONFIRMED | https://github.com/suchnsuch/Tangent | repo fetched
L445 | By Taylor Hadden | STILL-UNVERIFIED | https://github.com/suchnsuch/Tangent | attribution not re-captured
L447 | Svelte + Electron; customized Typewriter editor | CONFIRMED | https://github.com/suchnsuch/Tangent | repo README
L447 | Markdown files on disk | CONFIRMED | https://github.com/suchnsuch/Tangent | README
L449 | Wiki-links with hidden/revealed styling; Thread View sliding panels | CONFIRMED | https://github.com/suchnsuch/Tangent | README describes Thread View
L449 | Open alpha status | CONFIRMED | https://github.com/suchnsuch/Tangent | README
L449 | Roadmap: HTML export, queries, board view, refactoring, tag parameters | CONFIRMED | https://github.com/suchnsuch/Tangent | README roadmap
L451 | No sync; file-based | CONFIRMED | https://github.com/suchnsuch/Tangent | none documented
L453 | HTML export on roadmap, not shipped | CONFIRMED | https://github.com/suchnsuch/Tangent | README roadmap
L455 | No plugin ecosystem; AI not captured | STILL-UNVERIFIED | https://github.com/suchnsuch/Tangent | no fresh evidence either way
L457 | Mac, Windows, Linux | CONFIRMED | https://github.com/suchnsuch/Tangent | README
L459 | Free during open alpha | CONFIRMED | https://github.com/suchnsuch/Tangent | README
L461 | Sentiment | STILL-UNVERIFIED | https://www.linuxlinks.com | only editorial source, not re-fetched
L463 | Pull-from: Thread View, Typewriter editor, markdown simplicity | CONFIRMED | https://github.com/suchnsuch/Tangent | all three verified

## Sweep fills (17)

L157 | ente fully open source monorepo | FILL | https://github.com/ente/ente | monorepo fetched; open-source E2EE platform confirmed. No standalone Notes product exists, which narrows what this row can claim
L61 | Notesnook license split GPLv3 client / AGPLv3 server | FILL | https://github.com/streetwriters/notesnook-sync-server | server repo fetched (AGPLv3 README); official pricing page now says "Client and server, GPLv3" — newer statement wins, conflict recorded
L115 | AFFiNE self-host free up to 10 seats | FILL | https://affine.pro/pricing | pricing page fetched, 10-seat free self-host confirmed
L41 | Joplin Markdown editing with plugins/themes, extension API | FILL | https://joplinapp.org/ | official site fetched, feature list confirmed
L111 | BlockSuite as the editor behind AFFiNE | FILL | https://github.com/toeverything/blocksuite | repo fetched; license corrected to MPL 2.0
L233 | RNote infinite canvas, PDF/image import-export, adaptive UI | FILL | https://github.com/flxzt/rnote | repo fetched, all three confirmed
L89 | Trilium multi-parent hierarchy, hoisting, versioning, scripting | FILL | https://docs.triliumnotes.org/ | official docs fetched, all confirmed
L231 | RNote Rust + GTK4/libadwaita; .rnote format | FILL | https://github.com/flxzt/rnote | repo fetched; .rnote is gzipped JSON and README flags format instability
L145 | Anytype platform coverage | FILL | https://github.com/anyproto | org fetched: native iOS (Swift) and Android (Kotlin) repos alongside desktop clients; web app remains unconfirmed
L159 | ente Libsodium E2EE + Docker Compose self-host | FILL | https://hasgeek.com/rootconf/ente-self-hosting-images-technical-review/sub/review-of-ente-an-open-source-e2ee-self-hosted-alt-FK8L54TNuHrQBsivJJgDHW | technical review fetched, confirmed
L183 | Saber Flutter/Dart handwriting app | FILL | https://github.com/saber-notes/saber | repo fetched, confirmed; dual-password E2EE additionally confirmed in README
L47 | Joplin plugin/theme ecosystem via Extension API | FILL | https://joplinapp.org/ | confirmed; first-party AI now exists as of Joplin 3.7 (https://joplinapp.org/news/20260831-release-3-7/), so the "not captured" note is outdated
L161 | ente notes rich text + checkbox notes | FILL | https://github.com/ente/ente/releases | release notes fetched; notes functionality exists inside the platform but no standalone Notes product — claim reframed
L91 | Trilium server-based sync | FILL | https://docs.triliumnotes.org/developer-guide/concepts/sync | sync docs fetched, confirmed
L169 | Ente Auth platforms | FILL | https://f-droid.org/en/packages/io.ente.auth/ | F-Droid listing fetched, Android/iOS/Mac/Windows/Linux/Web confirmed for Auth; Notes platforms still unconfirmed
L67 | Notesnook self-hostable sync server | FILL | https://github.com/streetwriters/notesnook-sync-server | repo fetched: self-hosting now possible but without support; no longer alpha
L401 | Tolaria AI-docs positioning | FILL | https://github.com/refactoringhq/tolaria | repo fetched, positioning and MCP server confirmed; pricing resolved to free/open source

Sweep scorecard: 17 candidates processed, 17 FILL, 0 NOT-CONFIRMABLE.

## Master-file corrections

===== ROW: L85 | Continuation named TriliumNext/Notes =====
OLD: Continuation named TriliumNext/Notes
NEW: Continuation repo renamed to TriliumNext/Trilium (https://github.com/TriliumNext/Trilium); docs at docs.triliumnotes.org
===== END ROW =====

===== ROW: L19 | Sync code widely understood not to be FOSS =====
OLD: "Sync code widely understood not to be FOSS"
NEW: db-sync self-host component sits inside the AGPL-3.0 logseq repo with a documented Node.js adapter (https://github.com/logseq/logseq/blob/master/deps/db-sync/README.md); the paid hosted Sync offer may remain proprietary, but the self-host path is in the FOSS repo
===== END ROW =====

===== ROW: L41 | OCR of images not captured =====
OLD: OCR of images not captured
NEW: Official OCR shipped in Joplin v2.14, March 2024 (https://joplinapp.org/news/20240301-release-2-14/, docs https://joplinapp.org/help/apps/ocr/)
===== END ROW =====

===== ROW: L47 | First-party AI features not captured =====
OLD: First-party AI features not captured
NEW: Joplin 3.7 (Aug 2026) added first-party AI chat and an MCP server (https://joplinapp.org/news/20260831-release-3-7/)
===== END ROW =====

===== ROW: L61 | Sync server AGPLv3 =====
OLD: Sync server AGPLv3
NEW: Official pricing page states "Client and server, GPLv3" (https://notesnook.com/pricing); sync-server repo README still reads AGPLv3 (https://github.com/streetwriters/notesnook-sync-server), so record the newer official statement with the conflict noted
===== END ROW =====

===== ROW: L67 | Self-hostable sync server in alpha =====
OLD: Self-hostable sync server in alpha
NEW: Self-hosting now possible but without support (https://github.com/streetwriters/notesnook-sync-server); no longer alpha
===== END ROW =====

===== ROW: L109 | Backend/common-native MPL 2.0 for CE, EE terms for rest =====
OLD: Backend/common-native MPL 2.0 for CE, EE terms for rest
NEW: CE repo is MIT at the root (https://github.com/toeverything/affine)
===== END ROW =====

===== ROW: L109 | BlockSuite editor MIT-licensed =====
OLD: BlockSuite editor MIT-licensed
NEW: BlockSuite is MPL 2.0 (https://github.com/toeverything/blocksuite)
===== END ROW =====

===== ROW: L115 | E2EE not captured =====
OLD: E2EE not captured
NEW: AFFiNE Cloud does not have full E2EE today; official FAQ says to expect support "in the near future" (https://affine.pro/blog/faq)
===== END ROW =====

===== ROW: L157 | Notes one product line alongside Photos and Auth =====
OLD: Notes one product line alongside Photos and Auth
NEW: ente has no standalone Notes product; notes functionality lives inside the platform (Ente Locker), and Ensu is a separate AI-chat app (https://github.com/ente/ente, https://ensu.ente.com/)
===== END ROW =====

===== ROW: L187 | E2EE on sync not captured =====
OLD: E2EE on sync not captured
NEW: Saber notes are end-to-end encrypted on sync, with a second-password option for additional protection (https://github.com/saber-notes/saber)
===== END ROW =====

===== ROW: L207 | .xoj/.xopp XML-based document format with PDF annotation layer =====
OLD: .xoj/.xopp XML-based document format with PDF annotation layer
NEW: .xopp files are gzipped XML documents with a PDF annotation layer (https://github.com/xournalpp/xournalpp)
===== END ROW =====

===== ROW: L215 | Plugin system exists =====
OLD: Plugin system exists
NEW: Lua-based plugin system confirmed (https://github.com/xournalpp/xournalpp)
===== END ROW =====

===== ROW: L231 | Native .rnote document format =====
OLD: Native .rnote document format
NEW: .rnote is gzipped JSON and the README warns the format is still unstable across versions (https://github.com/flxzt/rnote)
===== END ROW =====

===== ROW: L241 | Linux primarily; Flatpak distribution; Windows/macOS availability not captured =====
OLD: Linux primarily; Flatpak distribution; Windows/macOS availability not captured
NEW: Linux, macOS and Windows are all listed as available (https://github.com/flxzt/rnote)
===== END ROW =====

===== ROW: L263 | Open-source plugin ecosystem not captured =====
OLD: Open-source plugin ecosystem not captured
NEW: Drop-in plugin support is planned, not a shipped ecosystem (https://github.com/excalidraw/excalidraw)
===== END ROW =====

===== ROW: L325 | Repos: syncing-server (server) / server license not directly captured =====
OLD: Repos: https://github.com/standardnotes/app (client), https://github.com/standardnotes/syncing-server (server) **server license not directly captured this session**
NEW: Client https://github.com/standardnotes/app; server now at https://github.com/standardnotes/server, fetched this session: GPL-3.0 (legacy syncing-server path redirects via https://github.com/standardnotes/self-hosted)
===== END ROW =====

===== ROW: L349 | Archived 2026-07-23 =====
OLD: archived 2026-07-23 (captured via listing)
NEW: actively developed, not archived; current version v1.3.6 (https://helixnotes.com, https://apps.apple.com/us/app/helixnotes/id6788490726)
===== END ROW =====

===== ROW: L379 | Self-host path not captured =====
OLD: Self-host path not captured
NEW: Official self-hosting docs exist (https://lockbook.net/docs/self-hosting.html)
===== END ROW =====

===== ROW: L387 | Paid tiers exist UNVERIFIED =====
OLD: paid tiers exist **UNVERIFIED this session**
NEW: premium at $2.99/month for 30 GB (https://apps.apple.com/us/app/lockbook/id1526775001)
===== END ROW =====

===== ROW: L313 | Mobile apps exist =====
OLD: mobile apps exist
NEW: no native mobile apps; mobile is a responsive PWA, with native macOS/Windows desktop apps (https://docs.getoutline.com/s/guide/doc/the-app-Ez4bmY6VDD)
===== END ROW =====

===== ROW: L411 | Tolaria pricing not captured =====
OLD: Pricing. Not captured — possibly free/paid
NEW: Free and open source (https://github.com/refactoringhq/tolaria)
===== END ROW =====

===== ROW: L429 | Poznote publishing/export details not captured =====
OLD: Publishing & export. Details not captured
NEW: Backup/export to file documented; full export matrix still not captured (https://github.com/timothepoznanski/poznote)
===== END ROW =====

===== SECTION: TriliumNext/Notes =====
RENAME: TriliumNext/Trilium (repo renamed; same project)
===== END SECTION =====

LANE 3 COMPLETE — 263 claims verified (235 CONFIRMED, 26 REVISED, 2 DENIED, 73 STILL-UNVERIFIED), 17 sweep candidates processed (17 FILL, 0 NOT-CONFIRMABLE)
