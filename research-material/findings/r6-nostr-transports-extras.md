# R6 — Nostr, Remaining Sync Transports, and Unclassified Leftovers

Lane: Nostr and the remaining transport/extra items from `links-inventory.txt` not covered by other lanes. Research date: 2026-10-26. Every claim carries its source URL in parentheses. Claims that could not be verified this pass are marked UNVERIFIED; that is a finding, not a gap. Per the hard security rule, no machine names, hostnames, IPs, or personal account identifiers appear anywhere below; third-party public project/repo/developer names that are themselves the research subject are kept as facts.

Context: the project owner asked in the source material whether sync could ride on "cf workers, Tailscale, Iroh, or even nostr?" and pasted the Nostr links below (transcript line ~2460, https://github.com/nostr-protocol/nostr, https://nostr.org/, https://nostrapps.com/obsidian-nostr-writer, https://nostrapps.com/bouquet). The R6 sync lane (findings-r6/r6-sync-crdt-stack.md) explicitly left "Nostr-as-sync-transport: no shipped example found either way" as an open question and flagged iroh as not deep-fetched. This lane closes both.

Cross-cutting context for all pull-from assessments (inherited from the project): a local-first notes app in Rust/Tauri with zero-knowledge/E2EE ambitions, 10k+ documents, offline for days, then merge. GPL/AGPL items are concepts-only.

---

## Part A — Nostr as sync/transport for a private notes app

### A1. What Nostr is, who maintains it, status

Nostr ("Notes and Other Stuff Transmitted by Relays") is an open, decentralized protocol drafted in 2020 by the pseudonymous developer fiatjaf; relays store and forward signed JSON events, and users are identified by secp256k1 keypairs rather than accounts (https://nostr.org/, https://en.wikipedia.org/wiki/Nostr). The canonical repository `nostr-protocol/nostr` is essentially the protocol README and advocacy text, describing itself as "a truly censorship-resistant alternative to Twitter that has a chance of working"; the repo is public-domain licensed (https://github.com/nostr-protocol/nostr). The protocol's normative documents live in the separate `nostr-protocol/nips` repository ("Nostr Implementation Possibilities"), which is actively extended by proposal PRs (https://github.com/nostr-protocol/nips, example: NIP-77 was merged via https://github.com/nostr-protocol/nips/pull/1494). The official site is candid about maturity: Nostr is "still under construction", "an idea with a lot of open-source software around it and a large userbase, but not a finished, polished product" (https://nostr.org/).

**Adoption — conflicting numbers, stated honestly.** A October 2025 review tallied roughly 21,000 total identified users and about 3,675 daily active users, and noted this is "tiny next to Mastodon, Bluesky, or even a mid-sized Discord" (https://www.glukhov.org/post/2025/10/nostr-overview-and-statistics/, https://danmackinlay.name/notebook/nostr.html). A third-party activity dashboard in 2026 showed ~3,028 daily active of ~10,200 monthly active users (https://profilestr.com/reports). At the same time Wikipedia repeats a "over 18 million users across its network" figure from 2023, which almost certainly counts created keypairs/profiles rather than actives (https://en.wikipedia.org/wiki/Nostr). The most rigorous academic survey counts "more than 600 active relays, more than 9 million users (with a profile and contact list), and 100 million posts" (https://arxiv.org/html/2402.05709v2). For a sync-transport decision, the relevant figure is neither: it is relay health.

**Relay health — the finding that matters for sync.** Of roughly 1,005 tracked relays, only about 471 remained public and reachable, ~191 sat behind restrictions, and 343 had simply gone offline (https://hoge.gg/lightning-network-nostr-relay-economy/, https://socialcapitalmarkets.net/crypto-trading/nostr-statistics/). Roughly two-thirds of relays never find a way to cover their own operating costs (https://hoge.gg/lightning-network-nostr-relay-economy/). This churn is the single strongest argument against betting long-term personal data storage on third-party relays without a self-hosted fallback.

**License:** public domain (UNLICENSE-style) for `nostr-protocol/nostr`; the NIPs repo is likewise open. No license constraint at all for concepts or implementations (https://github.com/nostr-protocol/nostr).

### A2. Technical profile: which NIPs actually matter for private E2EE notes sync

The event model (NIP-01) defines kinds, Schnorr signatures over secp256k1, subscription filters, and relay behavior (https://github.com/nostr-protocol/nips, https://nips.nostr.com/). On top of that, the stack relevant to a private notes app is:

**NIP-44 — Encrypted Payloads (Versioned), status: optional, current version 0x02.** ECDH over secp256k1 produces a shared secret; HKDF-extract with salt `nip44-v2` derives a conversation key; a random nonce derives per-message ChaCha key, nonce and HMAC key; content is padded to hide plaintext length, ChaCha20 encrypts, HMAC-SHA256 authenticates, and the whole thing is a versioned base64 payload placed inside a normally signed event. The outer Schnorr signature authenticates the payload and must be validated before decrypting; ChaCha was chosen over AES for speed and multi-key attack resistance, HMAC-SHA256 over Poly1305 because polynomial MACs are easier to forge. Cure53 audited version 2 in December 2023. It replaces the deprecated NIP-04 (AES-256-CBC, no MAC, reused IV patterns) and is used by NIP-37, NIP-46, NIP-59 and private payload flows (https://nips.nostr.com/44). This is the content-encryption primitive a notes sync would use.

**NIP-59 — Gift Wrap, status: optional/relay.** Defines three layers: a rumor (unsigned inner event), a seal (the rumor signed and NIP-44-encrypted to the recipient, kind 13), and a gift wrap (the seal re-encrypted and published from a random one-time key, kind 1059, with routing tags; ephemeral variant kind 21059). The result "is not perfect anonymity, but it separates content, author identity and routing metadata better than a simple encrypted direct message", and timestamps are randomized (https://nips.nostr.com/59). For a single-user notes-sync app the seal layer is what matters (encrypt to yourself); the throwaway-key wrap layer mostly exists to protect social DMs from relay-visible social graphs.

**NIP-17 — Private Direct Messages, updated 2026.** Builds DMs and chat rooms on NIP-44 + NIP-59 instead of the deprecated NIP-04: kind 14 chat messages wrapped in kind 1059, sender and recipient hidden inside the seal, randomized timestamps, self-copy support (https://nips.nostr.com/17). Relevant here mostly as the canonical, maintained example of "private content over Nostr done right".

**NIP-78 — Application-Specific Data.** The generic storage NIP: kind 30078 addressable events with a `d` tag, intended for application-specific data an app syncs across relays; users can self-organize their data, and multiple clients can share a namespace. This is the NIP a notes app would actually store note documents in (https://nips.nostr.com/78). Its documented weakness: it is designed for smallish self-contained JSON blobs, multi-writer semantics are loose, and relays are free to limit content length (relay `limitation.max_content_length` is exposed via NIP-11, commonly 8-16 KB, with some relays larger) (https://learnnostr.org/concepts/relays).

**NIP-77 — Negentropy Syncing, merged 2025.** A Nostr-friendly wrapper around the Negentropy range-based set-reconciliation protocol: client and relay exchange hex-encoded binary filter messages over a `NEG` websocket message type to compute the exact set difference of event IDs cheaply, then fetch only what is missing (https://nips.nostr.com/77). This is the piece that makes "catch up after a week offline" efficient on Nostr. Implementation notes from the merge discussion are a real caution: relays must keep Negentropy filter objects in separate storage, and given Nostr's "delays, reconnections, and clients/relays straight out going away, there will be some memory costs in keeping so many filters in memory" (https://github.com/nostr-protocol/nips/pull/1494). Relay-side support is real: strfry advertises NIP 77 among supported NIPs (https://github.com/hoytech/strfry), and nostr-rs-relay gained it after a long-running issue (https://github.com/scsibug/nostr-rs-relay/issues/234). The underlying protocol is by the same author as strfry and has a standalone Rust crate (https://github.com/nostrdevkit/negentropy).

**NIP-65 — Relay list metadata (adjacent, needed).** Users publish which relays to read/write on their behalf; a notes sync would publish and honor this to find "your" relays (https://github.com/nostr-protocol/nips).

**Blossom — blobs stored simply on media servers.** A separate HTTP protocol using Nostr keys for identity: a set of endpoints (GET/HEAD `/<sha256>`, PUT `/upload`, PUT `/mirror`, DELETE, media optimization endpoints) where blobs are binary data addressed by their sha256 hash; BUD-11 uses kind 24242 authorization events; BUD-03 uses kind 10063 for a user's server list; BUD-07 covers paid uploads; BUD-12 blob management. Spec is public domain and organized as "Blossom Upgrade Documents" (https://github.com/hzrd149/blossom). For a notes app, Blossom is the natural attachment/image transport (note text in kind 30078 events, attachments on Blossom servers referenced by hash). Ecosystem: a curated list exists (https://github.com/hzrd149/awesome-blossom) with Bloom, a Tauri+Rust desktop app bundling a Blossom media server and Nostr relay in one package ("sovereign storage... no server administration required", https://github.com/nostrnative/bloom), Primal's production Blossom server (PostgreSQL-backed, CDN delivery, https://github.com/allenlinli/primal-blossom-server), and a personal PHP/SQLite implementation (https://github.com/johninnis/hubstr-blossom). The earlier Blossom Drive cloud-drive experiment is explicitly deprecated and unmaintained, pointing users to Bouquet instead (https://github.com/hzrd149/blossom-drive).

**What the stack does NOT give you:** group key agreement and rotation (NIP-44 is pairwise ECDH; for multi-device you either derive from your single nsec or build your own), key rotation with data continuity, and any guarantee that a relay retains your events. All of that is app-level work.

### A3. Rust ecosystem (the pull-from question)

The Rust story is unusually good, because the reference SDK is Rust-first with FFI outward:

- `nostr` crate: Rust implementation of the protocol, MIT, v0.45.5 (Sep 2026), ~385K downloads/month, used in 285 crates (https://crates.io/crates/nostr, https://lib.rs/crates/nostr).
- `nostr-sdk`: high-level client library (relay pool, event database, zaps, etc.), MIT, v0.44.x-0.45.x, ~53K downloads/month, used in 79 crates, by Yuki Kishimoto and the Rust Nostr Developers (https://crates.io/crates/nostr-sdk, https://lib.rs/crates/nostr-sdk).
- Supporting crates in the same workspace: `nostr-relay-pool`, `nostr-connect` (NIP-46 remote signer, relevant for keeping nsec out of the app process), `nwc`, storage backends `nostr-sqlite`, `nostr-lmdb`, `nostr-indexeddb`, `nostr-ndb` (nostrdb), `nostr-gossip` traits, and `nostr-blossom` for the Blossom protocol (https://github.com/rust-nostr/nostr).
- `negentropy` crate: standalone Rust implementation of the set-reconciliation protocol, usable without the rest of Nostr (https://github.com/nostrdevkit/negentropy).
- FFI: the workspace builds Python and Kotlin bindings (https://github.com/damus-io/nostr-sdk), so a Tauri app calls it natively as a Rust dependency with no bridge at all.
- Damus (the iOS client) maintains its own fork of nostr-sdk, which is both a robustness signal and a mild fragmentation caution (https://github.com/damus-io/nostr-sdk).
- The workspace's NIP coverage table lists implementations across the stack including the ones relevant here (NIP-44, NIP-59, NIP-77) (https://github.com/rust-nostr/nostr).

Everything is MIT; no GPL/AGPL contamination found in the core crates.

### A4. Who actually syncs notes over Nostr today (this closes the sync lane's open question)

Shipped examples exist, all small:

- **Private Notes (Nostr)**, repo `AlexeyYuPopkov/nostr_notes`: an E2EE notes app on Nostr for iOS, Android, macOS and Web (Flutter monorepo). Notes are encrypted on-device with NIP-44, signed with secp256k1, stored on user-selected relays; "no server, no accounts — only a keypair", with optional PIN-layer encryption; also sells itself for encrypted passwords (https://github.com/AlexeyYuPopkov/nostr_notes, https://apps.apple.com/us/app/private-notes-nostr/id6757975921, https://alexeyyupopkov.github.io/). This is the closest existing product to the target architecture, minus rich text/CRDT.
- **BitOS Notes**, repo `bitoslabs/bitos-notes`: cross-platform local-first notes in Flutter aiming at an "Apple Notes-class" experience, with Nostr as "the decentralized sync and identity layer", offline-capable with optional public sharing and future collaboration (https://github.com/bitoslabs/bitos-notes). Directly on point: local-first + Nostr sync, though Flutter not Rust and pre-1.0.
- **jqw22/notebook**: "a simple encrypted notes app linked to your Nostr identity, uses NIP-44" (https://github.com/jqw22/notebook).
- **Blockcore Notes**: an older web notes app for decentralized infrastructures storing private notes via browser-extension signing (nos2x/Alby), built on early NIPs (https://github.com/block-core/blockcore-notes, https://reactjsexample.com/notes-app-for-decentralized-infrastructure-nostr-and-web5/).
- The grassroots pattern in the community is self-notes via self-messages or a private/localhost relay, confirming there is no standard "notes sync" NIP beyond NIP-78 (https://www.reddit.com/r/nostr/comments/1841z72/any_way_to_store_notes_to_self/).

**Failure modes observed across these and the protocol:** key loss equals data loss (the nsec is simultaneously identity, signing key and the root of the encryption key); NIP-09 deletions are honor-system and relays may ignore them; relay payment walls (BUD-07 for Blossom, paid relays generally) and relay churn (343 of ~1,005 relays offline, https://hoge.gg/lightning-network-nostr-relay-economy/); metadata that survives even NIP-59 (event sizes, edit cadence, your relay set, which pubkeys you talk to); and the two-hop catch-up problem NIP-77 only partially solves (https://nips.nostr.com/77, https://github.com/nostr-protocol/nips/pull/1494).

### A5. Pull-from assessment for the Rust/Tauri E2EE notes app

**Sync-over-Nostr, concretely:** each note document is a kind 30078 event (NIP-78) whose `d` tag is the note ID and whose content is NIP-44-encrypted to your own key (NIP-44 supports self-encryption), optionally NIP-59-sealed; attachments go to Blossom servers referenced by sha256; the relay list is your own (self-hosted plus optionally public); NIP-77 does the offline catch-up; `nostr-sdk` gives all of it in Rust under MIT, embeddable in Tauri directly. A notebook-scale CRDT would ride inside kind 30078 payloads as opaque encrypted bytes, so Nostr needs no understanding of the CRDT, exactly as with the self-hosted-server design.

**Verdict: concepts-only for sync, plus an optional export target.** Reasons: (1) relay churn and payment make third-party relays unacceptable as the primary durability layer for 10k+ documents; a self-hosted relay (strfry, ~50 MB base memory, LMDB; https://www.pistack.xyz/posts/2026-06-06-self-hosted-nostr-relays-strfry-nostream-nostr-rs-relay/; deployment stats: nostr-rs-relay 34.8% and strfry 23.1% of detected relays, https://github.com/rust-nostr/nostr-stats) then becomes just a custom sync server with extra protocol weight; (2) the single-identity-key model conflicts with the project's zero-knowledge goals, where key rotation and per-note keys are first-class; (3) metadata leakage is worse than a plain self-hosted E2EE relay because Nostr relays are public by default and read-access control is only now emerging (an authentication proxy bringing "read-level access control to strfry relays for the first time" was funded in March 2026, https://opensats.org/blog/advancements-in-nostr-relays). What is genuinely worth pulling: the **negentropy range-based set reconciliation protocol** as a portable sync primitive (standalone MIT Rust crate, https://github.com/nostrdevkit/negentropy), the **NIP-44 padding discipline** (length-hiding padding is something most E2EE sync designs forget), and Nostr as an **optional "publish to Nostr" export path** if interop is ever wanted. Bloom (https://github.com/nostrnative/bloom) is also a useful architectural reference for "local server + relay in a Tauri app", MIT/AGPL mix UNVERIFIED at file level.

---

## Part B — Remaining transport items

### B1. iroh (deep dive; completes the sync lane's flagged follow-up)

**What it is / status.** iroh is a Rust library by n0 for embedding direct, encrypted P2P connections into applications: endpoints identified by stable keys ("dial keys, not IPs"), hole-punched QUIC connections between peers, fallback relays for when hole punching fails, and DNS-based discovery via pkarr. iroh 1.0 shipped June 15, 2026 (https://lobste.rs/s/cslljn/iroh_1_0_dial_keys_not_ips, https://pinggy.io/blog/iroh_1_0_dial_keys_not_ips/); crates.io shows active 1.x releases into late 2026. The official framing stresses it is an application-layer library, not a mesh VPN: iroh connects "your app's own devices", while VPNs join "a whole network of unrelated machines" (https://www.iroh.computer/solutions/vpn, https://www.iroh.computer/). License MIT OR Apache-2.0, repo https://github.com/n0-computer/iroh (https://github.com/n0-computer/iroh). Companion crates `iroh-blobs` (BLAKE3-addressed blob transfer) and `iroh-gossip` are the pieces a notes app would actually use.

**Adoption, strongest evidence.** Anytype merged a PR making iroh-based relays and pkarr its global P2P transport layer by default (go-iroh 0.2.1, PKarr relays enabled by default), which is a production-scale notes-adjacent app standardizing on it (https://github.com/anyproto/any/pull/266). Enterprise and AI-infrastructure use cases (distributed LLM training across clouds, agent interconnects replacing VPN tunnels) show up in its marketing and in third-party proposals (https://www.iroh.computer/, https://github.com/NousResearch/hermes-agent/issues/70784).

**Failure modes / limits.** Hole-punching success on hostile networks (CGNAT, national firewalls) was flagged UNVERIFIED by the sync lane and remains so this pass: n0 claims high success rates, but no independent measurement was found; the sync lane's open item "iroh internals (Blindfold, hole-punching success rates on hostile networks)" still stands. Relays are needed as rendezvous fallback and are a trust point for metadata (connection timing) even though not for content (QUIC end-to-end encryption). Community experiments like tunneling WireGuard inside iroh, or SOCKS5/VPN proxies over it, confirm it is a transport toolkit, not a finished network product (https://github.com/n0-computer/wg-iroh, https://github.com/arontsang/iroh-vpn-proxy, https://github.com/mattgeddes/iroh-socks5).

**Pull-from.** Unchanged from the sync lane and now firmer: iroh is the leading Rust-native P2P transport candidate for device-to-device sync (MIT/Apache, first-class Rust, Anytype precedent), with self-hosted relay fallback recommended. It composes with the self-hosted-server design: same encrypted update blobs, iroh as an additional direct path.

### B2. Tailscale (mentioned in source material as a sync transport option)

A WireGuard-based mesh VPN run as a service; the source material floated it as one of "cf workers, Tailscale, Iroh, or even nostr" for sync. For a notes app, sync-over-Tailscale means running your sync server reachable only inside your tailnet, or running Syncthing over it; the app itself needs no SDK. The coordination server is proprietary (headscale, the BSD-licensed self-hosted coordinator, is the open alternative; UNVERIFIED this pass, not re-verified this lane). Verdict: viable for power users as a private transport in front of a self-hosted server, but it is a user-side network choice, not something to build the product around; no license constraint for the app itself.

### B3. Cloud-folder transports referenced in the source material

The source material's actual stated preference for sync was plain cloud folders: "Dropbox/OneDrive is what I'm mainly targeting for now... It'll work regardless as long as you put the .md files in your Cloud and point it to that" (source transcript, quoted in research/extracted_flat.txt line 2409; also "cloud saving (via dropbox, or whatever cloud service is being used)" at extracted_flat.txt line 1904, and the Dillinger editor's GitHub/Dropbox/Google Drive sync as prior art). As a transport class: zero server work for the developer, but sync quality is hostage to the folder-sync engine (partial-write windows, conflict copies, delayed propagation), and E2EE must be layered entirely client-side since these clouds are third-party-read. WebDAV (Nextcloud self-hosted) and S3-compatible buckets are the same pattern with a deterministic API and no folder daemon, and are what most Obsidian-community sync plugins target. Verdict: cloud-folder support is a pragmatic first transport, exactly as the source material says; the E2EE sync engine should treat it as a dumb blob store so the same engine can later ride iroh or a self-hosted relay without redesign.

---

## Part C — The three Nostr links from the inventory, itemized

### C1. https://nostr.org/ — covered fully in A1 above.

### C2. https://github.com/nostr-protocol/nostr — covered fully in A1 above.

### C3. https://nostrapps.com/obsidian-nostr-writer (page now 404; app researched via primary sources)

**Status of the link itself:** the nostrapps.com pages return 404 as of this pass (https://nostrapps.com/obsidian-nostr-writer); nostrapps.com is an auto-generated directory that indexes Nostr apps, so dead links there do not mean the app is dead. The embed in the source material described it as "Obsidian plugin for publishing articles to Nostr".

**The app.** Obsidian Nostr Writer, repo `jamesmagoo/nostr-writer`, an Obsidian plugin (v2.2.0, desktop only, MIT, listed in the official community plugin directory) that publishes notes and short-form posts from Obsidian directly to Nostr: automatic image upload, tags, multiple Nostr profiles and relays, frontmatter extracted into article metadata, and importing Nostr bookmarks as Markdown (https://community.obsidian.md/plugins/nostr-writer, https://github.com/jamesmagoo/nostr-writer). Its stated design is "a quiet place": "completely abstracted from Nostr... the plugin does not read Nostr messages or give you any view into the public space. It just publishes what you've written" (https://github.com/delirehberi/nostr-writer, an active fork of the original). It appears in the awesome-nostr tooling list (https://github.com/dmnyc/awesome-nostr) and was demoed on Stacker News (https://stacker.news/items/237251?commentId=237314).

**Relevance to the project.** It is publish-only, not sync: it takes local Markdown outward to Nostr long-form notes (NIP-23-style articles), it does not store notes on relays or pull them back as source of truth. Pull-from: concept-level reference for a "publish note to Nostr" feature; not a sync architecture.

### C4. https://nostrapps.com/bouquet (page now 404; app researched via primary sources)

**The app.** Bouquet is "a personal manager for Blossom media servers" (description carried in the source material's embed): a web app to upload, browse, delete and sync media blobs across multiple Blossom and NIP-96 storage servers (https://deepwiki.com/flox1an/bouquet, https://github.com/hzrd149/awesome-blossom). It was created alongside the Blossom spec by its author (hzrd149) and is now maintained as a fork (flox1an/bouquet, indexed June 2026). It superseded the deprecated Blossom Drive (https://github.com/hzrd149/blossom-drive).

**Relevance.** Bouquet is to attachments what a notes app's media manager would be: multi-server mirroring, hash-addressed files, Nostr-key auth (BUD-11 kind 24242). Pull-from: the multi-server mirroring UX pattern for a "bring your own blob store" design; the codebase is TypeScript/React so concepts only for a Rust app.

---

## Part D — Unclassified leftovers from the inventory

Items in the inventory that no other lane covers and that fit none of the categories above; one line each, honestly labeled.

- **A Gitea-hosted repository named "workflow-playbook"** on a self-hosted Gitea instance referenced in the source material: appears to be the project's own process playbook rather than third-party research material. Content not fetched (self-hosted instance, not reachable this pass). UNVERIFIED.
- **A Gitea-hosted repository named "sawt"** on the same self-hosted Gitea instance: purpose unclear from the inventory; possibly project tooling. Content not fetched. UNVERIFIED.
- **pandoc.org grid-tables demo page** (chunked pandoc-markdown manual demo for the `grid_tables` extension): documentation of pandoc's grid-table Markdown flavor, relevant only to Markdown round-tripping fidelity, not an app (https://pandoc.org/chunkedhtml-demo/18-pandoc-markdown/grid-tables.html).
- **YouTube video `watch?v=_K-ExOiEv40`**: a review/demo of the NEO writing tool by a book-YouTuber, companion material to the NEO entry covered in the linked-apps lane (https://www.youtube.com/watch?v=_K-ExOiEv40, https://redcircle.com/shows/2toramble/ep/2878ecad-28fc-4fc1-9a98-e47df621c20e).
- **Six klipy.com .mp4/.gif links** in the inventory: animated media assets (GIF/MP4 clips) shared in the source chat; klipy is a GIF/MP4 hosting service. Not apps, not research targets.
- **A share.redd.it preview link for reddit post 1x8dp2r**: the image attachment of the Pele reddit post; Pele itself is covered in the linked-apps lane, so only the asset link was unclassified.
- **t.co short links and x.com status links** (pwnies/sheherenow_ threads): resolvers and social embeds pointing at items already covered in the linked-apps lanes.
- **Social-preview image URLs** (`/api/og`, avatar and og:image endpoints for nextra, ai-counsel, aleph.ai, etc.): generated preview images, not links to software.

---

## Bottom line for the project

The Nostr question the project owner asked ("sync over nostr?") now has a complete answer: the pieces exist (NIP-44 + NIP-59 encryption, NIP-78 storage, NIP-77 catch-up, Blossom blobs, a mature MIT Rust SDK), at least four small shipped apps do exactly this, and the ecosystem is Rust-first, so a sync-over-Nostr module in Tauri is entirely buildable. But relay economics (a third of relays dead, two-thirds unprofitable), public-by-default metadata, and the single-identity-key model make Nostr a poor primary durability layer for a 10k+-document E2EE app. The durable takeaways are the negentropy set-reconciliation primitive (standalone MIT Rust crate), NIP-44's length-hiding padding discipline, Blossom's hash-addressed bring-your-own-blob-store pattern, and iroh (now 1.0, Anytype-validated) as the leading P2P transport to add alongside a self-hosted E2EE sync server.
