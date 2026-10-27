# R12 round 2 lane 7: sync/CRDT, plugins, nostr, integrations re-verification

Method: claim-by-claim re-verification of the four staged R6 files. Evidence was loaded fresh this session: the obsidianstats.com most-downloaded list and individual plugin pages (Templater, Omnisearch, Meta Bind, Notebook Navigator, Numerals, obsidian-livesync, Remotely Save, Kanban), Stirling-PDF / Kdenlive / Krita repo pages, crates.io pages for automerge, yrs, diamond-types, loro-protocol, the negentropy repo, strfry relay self-hosting coverage, rust-nostr/nostr-stats deployment counts, and Tailscale licensing searches. The search budget ran out before full re-coverage of the remaining targets, so every claim without a source loaded this session is marked STILL-UNVERIFIED (missing data is never treated as confirmed). Header/method lines of the input files are verified against the file content itself. Gists are at most 10 words; URLs in the URL column are either sources loaded this session or, for STILL-UNVERIFIED verdicts, the primary source that should settle the claim next pass.

## r6-sync-crdt-stack.md

L3 | header: every claim carries source URL | CONFIRMED | (input file itself) | header statement matches file content; verdicts below carry URLs
L33 | Automerge WASM ~4.7 MB inside plugin bundle | STILL-UNVERIFIED | https://github.com/SystemSculpt/obsidian-systemsculpt-ai/issues/345 | cited issue not reloaded within this pass's budget
L33 | automerge crate 400 KiB source, binary size unknown | STILL-UNVERIFIED | https://crates.io/crates/automerge | binary size claim never re-verified this pass
L29 | stated: automerge crate 0.12.0, MIT, on crates.io | CONFIRMED | https://crates.io/crates/automerge | surfaced in this session's crates.io searches
L49 | Yjs repo active, updates into 2026 | STILL-UNVERIFIED | https://github.com/yjs/yjs | repo page not loaded this session
L49 | yrs actively maintained on crates.io | CONFIRMED | https://crates.io/crates/yrs | crate confirmed live this session; exact latest version still not captured
L53 | Yjs note-app-scale benchmark specifics | STILL-UNVERIFIED | https://github.com/yjs/yjs | no public benchmark re-found this session
L57 | Notion uses Yjs (widely reported) | STILL-UNVERIFIED | https://y-crdt.github.io/pycrdt/ | adopter list not independently re-verified this session
L71 | Loro benchmark page lacks independent numbers | STILL-UNVERIFIED | https://www.loro.dev/docs/performance | vendor benchmark page not reloaded; no third-party benchmark found
L73 | loro-crdt npm bundle size | STILL-UNVERIFIED | https://www.npmjs.com/package/loro-crdt | WASM build exists (confirmed via search) but size not captured
L69 | stated: loro-protocol published on crates.io | CONFIRMED | https://crates.io/crates/loro-protocol | crate surfaced in this session's searches
L77 | Loro adoption beyond Ilow and loro-extended | STILL-UNVERIFIED | https://github.com/Ilow-Space/IlowObsidianSync | no additional production adopters surfaced this session
L93 | diamond-types license is MIT | STILL-UNVERIFIED | https://crates.io/crates/diamond-types | license field not read this session
L89 | stated: diamond-types published as v1.0.0 crate | CONFIRMED | https://crates.io/crates/diamond-types | crate surfaced this session; WIP status unchanged
L95 | diamond-types adoption in shipped apps | STILL-UNVERIFIED | https://github.com/josephg/diamond-types | no shipping-app adopter found this session
L109 | Keyhive performance/binary size at note scale | STILL-UNVERIFIED | https://github.com/inkandswitch/keyhive | no benchmarks surfaced this session
L111 | Keyhive workspace license | STILL-UNVERIFIED | https://github.com/inkandswitch/keyhive | license file not read this session
L113 | adoption beyond Roomy and the iroh PoC | STILL-UNVERIFIED | https://www.context-awesome.com/list/n0-computer/awesome-iroh | index not reloaded this session
L131 | any-sync third-party adoption | STILL-UNVERIFIED | https://github.com/anyproto/any-sync | no third-party app surfaced this session
L149 | iroh production scale | STILL-UNVERIFIED | https://github.com/n0-computer/iroh | no outage postmortems or scale data this session
L163 | diff-match-patch archived, Apache-2.0 | STILL-UNVERIFIED | https://github.com/google/diff-match-patch | repo not reloaded this session
L169 | diff-match-patch Rust crate exists, maintained | STILL-UNVERIFIED | https://crates.io/crates/diff-match-patch | crate not confirmed on crates.io this session
L193 | p2panda published benchmarks | STILL-UNVERIFIED | https://github.com/p2panda/p2panda | no benchmark data this session
L197 | p2panda shipping third-party app | STILL-UNVERIFIED | https://github.com/p2panda/p2panda | none identified this session
L211 | y-octo claims (future BaseBlockSuite store) | STILL-UNVERIFIED | https://github.com/toeverything/blocksuite | DeepWiki-only source, not independently confirmed
L215 | BlockSuite third-party adoption beyond AFFiNE | STILL-UNVERIFIED | https://github.com/toeverything/blocksuite | none surfaced this session
L217 | AFFiNE has no first-party editor-state E2EE | STILL-UNVERIFIED | https://community.affine.pro/c/build-in-public/blocksuite-github-and-technical-preview | absence claim not re-verified this session
L219 | y-octo maturity (not production-deployed) | STILL-UNVERIFIED | https://github.com/toeverything/blocksuite | status not re-verified this session
L227 | secsync current release status after grant | STILL-UNVERIFIED | https://github.com/nikgraf/secsync | release cadence not re-verified this session
L237 | secsync benchmark numbers | STILL-UNVERIFIED | https://github.com/nikgraf/secsync | none published, still true per available evidence
L239 | secsync license (historically AGPL-3.0) | STILL-UNVERIFIED | https://github.com/nikgraf/secsync | license file not read this session
L241 | secsync adoption beyond Serenity Notes | STILL-UNVERIFIED | https://github.com/serenity-kit/secsync | none surfaced this session
L251 | Tana ships no official export tooling | STILL-UNVERIFIED | https://github.com/glibalien/tanamigrator | absence claim not re-verified this session
L257 | TanaMigrator license | STILL-UNVERIFIED | https://github.com/glibalien/tanamigrator | license file not read this session
L259 | TanaMigrator quantified user counts | STILL-UNVERIFIED | https://github.com/glibalien/tanamigrator | no download/user data this session
L271 | Cryptomator latest version number | STILL-UNVERIFIED | https://github.com/cryptomator/cryptomator | releases page not loaded this session
L273 | Cryptomator iOS/Android app details | STILL-UNVERIFIED | https://cryptomator.org/ | mobile apps not re-verified this session
L277 | Cryptomator incident history | STILL-UNVERIFIED | https://cryptomator.org/for-individuals/ | no postmortems found; absence claim stands unverified
L289 | Tailscale per-component licenses | REVISED | https://github.com/tailscale/tailscale | client BSL 2.0 confirmed this session; coordination plane proprietary stands; other component licenses still unverified
L309 | IlowObsidianSync team size / bus factor | STILL-UNVERIFIED | https://github.com/Ilow-Space/IlowObsidianSync | small-team inference from release authorship not re-verified
L321 | IlowObsidianSync user numbers | STILL-UNVERIFIED | https://www.obsidianstats.com/plugins/ilow-sync | install count not captured this session
L323 | IlowObsidianSync key-rotation story | STILL-UNVERIFIED | https://github.com/Ilow-Space/IlowObsidianSync | rotation semantics still undocumented in reviewed material

## r6-obsidian-plugins.md

L183 | Templater maintenance moved to Zachatoo | CONFIRMED | https://www.obsidianstats.com/plugins/templater-obsidian | maintainer Zachatoo confirmed on plugin page this session
L184 | stated: Templater 6,017,669 all-time downloads | CONFIRMED | https://www.obsidianstats.com/most-downloaded | rank 2 with same figure on most-downloaded list
L184 | stated: Templater 5,369 GitHub stars | STILL-UNVERIFIED | https://github.com/SilentVoid13/Templater | star count not reloaded this session
L218 | stated: Templater licensed GPLv3 | REVISED | https://www.obsidianstats.com/plugins/templater-obsidian | registry page lists AGPLv3, not GPLv3; raw package.json check of R6 conflicts with registry entry
L212 | Templater complaint thread specifics | STILL-UNVERIFIED | https://github.com/SilentVoid13/Templater/issues | issue links never captured; none surfaced this session
L240 | Omnisearch precise install count | REVISED | https://www.obsidianstats.com/most-downloaded | 2,037,395 installs, rank 17, author Simon Cambier, loaded this session
L260 | Omnisearch complaint issue links | STILL-UNVERIFIED | https://github.com/scambier/obsidian-omnisearch/issues | issue links never captured; none surfaced this session
L371 | stated: Meta Bind in top-25 by installs | CONFIRMED | https://www.obsidianstats.com/plugins/obsidian-meta-bind-plugin | top-25 presence and author mProjectsCode confirmed this session
L390 | Meta Bind issue-thread specifics | STILL-UNVERIFIED | https://github.com/mProjectsCode/obsidian-meta-bind-plugin/issues | issue links never captured; none surfaced this session
L412 | Sheets (niconekoru) install count | STILL-UNVERIFIED | https://www.obsidianstats.com/plugins/obsidian-sheets | page not loaded this session
L428 | Sheets merged-cell Live Preview issue links | STILL-UNVERIFIED | https://github.com/NicoNekoru/obsidian-extend/issues | issue links never captured; none surfaced this session
L458 | Numerals install count | STILL-UNVERIFIED | https://www.obsidianstats.com/plugins/numerals | plugin page confirmed stable 1.10.2, math.js, author ryanc; download count not captured
L473 | Numerals open issue specifics | STILL-UNVERIFIED | https://github.com/gtg922r/obsidian-numerals/issues | issue links never captured; none surfaced this session
L475 | Numerals want-changed (variable scoping, long-sheet perf) | STILL-UNVERIFIED | https://github.com/gtg922r/obsidian-numerals/issues | complaint set not re-sourced this session
L497 | Badges (gapmiss) install count | STILL-UNVERIFIED | https://www.obsidianstats.com/plugins/obsidian-badges | page not loaded this session
L509 | Badges want-changed specifics | STILL-UNVERIFIED | https://github.com/gapmiss/obsidian-badges/issues | issue links never captured; none surfaced this session
L528 | InkedMark install count (new plugin) | STILL-UNVERIFIED | https://www.obsidianstats.com/plugins/inkedmark | page not loaded this session
L544 | InkedMark demo-thread reaction links | STILL-UNVERIFIED | https://www.reddit.com/r/ObsidianMD/ | thread links never captured; none surfaced this session
L546 | InkedMark want-changed set | STILL-UNVERIFIED | https://github.com/pcrausaz/obsidian-inkedmark/issues | too-new plugin; nothing surfaced this session
L564 | stated: Notebook Navigator download figure | REVISED | https://www.obsidianstats.com/plugins/notebook-navigator | ~735k installs by July 2026 and most-downloaded new plugin of 2025 (200,000+); figures loaded this session
L587 | Notebook Navigator issue-tracker specifics | STILL-UNVERIFIED | https://github.com/johansan/notebook-navigator/issues | tracker confirmed as canon; specific threads not re-verified; author Johan Sanneblad and PRs-not-accepted confirmed this session
L615 | Nostr Writer like/want-changed specifics | STILL-UNVERIFIED | https://github.com/ndem69/nostr-writer | small ecosystem; nothing surfaced this session
L636 | Opensidian author beyond the handle | STILL-UNVERIFIED | https://github.com/jpzk | author identity not re-verified this session
L745 | closed-source theme issue links | STILL-UNVERIFIED | https://forum.obsidian.md | community-thread links never captured; none surfaced this session
L760 | stated: obsidian-livesync stores binaries as CouchDB docs | CONFIRMED | https://www.obsidianstats.com/plugins/obsidian-livesync | plugin page confirms CouchDB/object-storage backends (MinIO, S3, R2), WebRTC P2P, MIT, vrtmrz, Obsidian 1.7.2+ requirement
L768 | Remotely Save mobile battery/storage cost links | STILL-UNVERIFIED | https://github.com/remotely-save/remotely-save/issues | community-thread links never captured; none surfaced this session
L789 | Remotely Save issue specifics | STILL-UNVERIFIED | https://github.com/remotely-save/remotely-save/issues | issue links never captured; none surfaced this session; 2,333,618 installs (rank 13) and mixed license confirmed on registry page this session
L800 | Remotely Save forks beyond community consensus | STILL-UNVERIFIED | https://github.com/remotely-save/remotely-save | fork landscape not re-verified this session
L802 | recurring forum recommendation link | STILL-UNVERIFIED | https://forum.obsidian.md | forum link never captured; none surfaced this session
L855 | summary: several install-base numbers unverified | CONFIRMED | https://www.obsidianstats.com/most-downloaded | remaining gaps are exactly the ones still marked above after this pass

## r6-nostr-transports-extras.md

L3 | header: claims carry URLs, UNVERIFIED is a finding | CONFIRMED | (input file itself) | header statement matches file content
L73 | Bloom repo MIT/AGPL license mix at file level | STILL-UNVERIFIED | https://github.com/nostrnative/bloom | repo not loaded this session
L73 | stated: strfry ~50 MB base, LMDB; nostr-rs-relay 34.8% / strfry 23.1% share | CONFIRMED | https://github.com/rust-nostr/nostr-stats | deployment-share figures and self-hosting coverage surfaced this session (also https://www.pistack.xyz/posts/2026-06-06-self-hosted-nostr-relays-strfry-nostream-nostr-rs-relay/); negentropy standalone MIT crate re-confirmed at https://github.com/nostrdevkit/negentropy
L85 | iroh hole-punching success on hostile networks | STILL-UNVERIFIED | https://github.com/n0-computer/iroh | no independent measurement surfaced this session
L91 | headscale as BSD-licensed self-hosted coordinator | STILL-UNVERIFIED | https://github.com/juanfont/headscale | license not re-verified this session; Tailscale coordination-plane-proprietary side re-confirmed this session via https://github.com/tailscale/tailscale
L125 | Gitea repo "workflow-playbook" content | STILL-UNVERIFIED | (self-hosted instance, unreachable) | source instance unreachable; unreachable means unverified, not absent
L126 | Gitea repo "sawt" purpose | STILL-UNVERIFIED | (self-hosted instance, unreachable) | same unreachable instance; purpose remains unclear

## integrations-1.md

L3 | header: inline URLs on every claim, UNVERIFIED marked | CONFIRMED | (input file itself) | header statement matches file content
L27 | Stirling PDF: no SDK, webview/API integration only | CONFIRMED | https://github.com/Stirling-Tools/stirling-pdf | repo loaded this session: ~93k stars, run by Stirling PDF Inc, open-core MIT outside app/proprietary, desktop frontend, engine/; no WASM/headless library surfaced
L57 | libVLC legal embedding: named commercial embedders | STILL-UNVERIFIED | https://wiki.videolan.org/LibVLC | named-embedder list not re-verified this session
L59 | vlc-rs bindings maintained | STILL-UNVERIFIED | https://github.com/1bsyl/vlc-rs | binding maintenance status not re-verified this session
L95 | Krita: no embeddable view, no headless library | REVISED | https://github.com/KDE/krita | this session surfaced CLI --export export path and kritarunner headless Python runner; "no headless" is too strong, though no embeddable view stands; GPL verdict unchanged
L137 | Kdenlive: no embeddable view, no headless library | REVISED | https://github.com/KDE/kdenlive | this session surfaced CLI rendering via kdenlive_render (headless with xvfb workaround); "no headless" is too strong; MLT layer distinction confirmed at https://github.com/mltframework/mlt, LGPL-2.1-for-framework claim not re-verified this session

## Master-file corrections

None. The master files (FEATURES.md, APPS-LINKS.md) were not staged in this lane's inputs, so exact-match patch blocks cannot be drafted against their headings and row cells. The three evidence revisions that should be carried into R13 against the master file are: Templater's license is listed as AGPLv3 on the registry (the R6 draft said GPLv3); Notebook Navigator's install base is roughly 735,000 as of July 2026 (most-downloaded new plugin of 2025 with over 200,000 downloads), well above any figure in the R6 drafts; Omnisearch's install base is 2,037,395 (rank 17). The Remotely Save license situation (registry lists OTHER, a mixed Apache-2.0 plus PolyForm Strict repository) was re-confirmed rather than contradicted.

## Out of scope (R13)

bb plugins, Strata, llama.cpp, openplayground, MediaPipe.

LANE 7 COMPLETE — 85 claims verified (14 CONFIRMED, 6 REVISED, 0 DENIED, 65 STILL-UNVERIFIED)
