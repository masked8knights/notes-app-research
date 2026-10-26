# Thread A: Sync and Conflict Resolution (findings)

Question: for a local-first, E2EE (zero-knowledge), Rust-based notes app with 10k+
documents edited offline for days and then merged — CRDTs, conflict files, or a hybrid?

Date: 2026-10-26. Method: primary sources (docs, READMEs, blogs, forums, crates.io/npm),
plus a hands-on merge benchmark on this 2-core/8GB box. Script and raw numbers:
`/home/notesapp/...` → in this workspace: `/home/thaura/notesapp/benchmarks/thread-a/`
(`bench.js`, `results.json`, `bench3.log`).

---

## TL;DR

1. CRDT merging at 10k small docs is not a performance problem. Yjs merged 10,000
   concurrently-edited documents in 0.14 s on a 2-core box. The problem is not merge
   speed; it is key management and the sync protocol.
2. E2EE CRDT sync is solved in production today by one pattern, and it is NOT
   server-side merging: encrypt each document's update stream client-side, let the
   relay store ciphertext plus *unencrypted commit-graph hashes/heads*, and do all
   merging on the client after decryption. Ink & Switch's Beelay and Loro's `%ELO`
   protocol both ship this design. So the answer to "can the server merge ciphertext"
   is: no, and it doesn't need to — heads metadata kept outside the encryption
   envelope is enough for server-side sync *planning* with client-side merge.
3. Conflict files (keep both versions, user merges) are what Obsidian ships, and the
   field evidence says silent merge failures and unnoticed conflict files are a real
   support burden. It is tolerable for one person with a few devices; the failure
   stories get worse with more devices and longer offline windows — which is exactly
   our spec.
4. Best-evidence architecture for the brief: CRDT per document (text), opaque
   ciphertext sync relay that never decrypts, key agreement done client-side (BeeKEM /
   any-sync style), file-level LWW with a "conflicted copy" as the last-resort fallback
   for non-text blobs. I.e. hybrid, with CRDTs doing the heavy lifting on notes.

---

## 1. The benchmark (measured here, not believed)

Setup: Node 22, this 2-core/8 GB sandbox. Scenario: 10,000 notes of ~500 chars. Each
note is created on device A, exported as an update, applied to device B, which then
inserts 50 chars at position 10 concurrently. Then device B's update is merged back
into device A's doc and convergence is verified. Script: `bench.js` in
`/home/thaura/notesapp/benchmarks/thread-a/`; raw output `results.json`.

| library | version | docs | edit+export (s) | merge (s) | per-doc merge | bytes/update | converged |
|---|---|---|---|---|---|---|---|
| yjs | 13.6.33 | 10,000 | 1.77 | **0.141** | 14 µs | ~518 B | 100% |
| @automerge/automerge | 2.0.0-alpha.3 (npm latest) | 1,000 | 1.27 | 1.15 | 1.15 ms | ~608 B | 100% |
| loro-crdt | 1.17.1 | — | failed to run | — | — | — | — |

Caveats, stated plainly:

- Automerge at 10,000 docs did not finish on this box: the process burned 7+ CPU
  minutes and was still running (killed). Reduced to 1,000 docs. Note this is the
  *alpha-era* npm package; Automerge 3 (see below) specifically fixed "high memory
  usage on client devices" and sync-server memory, so 2.x-alpha numbers likely
  understate today's Automerge. https://automerge.org/blog/automerge-3/
- loro-crdt 1.17.1 crashed in Node 22 with a wasm "memory access out of bounds" on a
  2-character insert, reproducible from a bare `LoroDoc`, and not fixed by heap/flags
  (`--max-old-space-size=4096`, `--experimental-wasm-gc`). An environment problem, not
  evidence against Loro (their CI runs Node 18+; cross-language Rust/TS tests ship in
  the protocol repo). But it means our benchmark says nothing about Loro directly.
- One mechanical finding worth recording for implementation: in automerge 2.0.0-alpha,
  `applyChanges` mutates in place AND returns an array; treating the return value as
  the doc silently breaks merge verification. A real integration bug we hit first hand.

Interpretation: 10k documents × 2 offline devices merges in well under a second with
Yjs in JS. Rust-native (yrs, loro, automerge core) is equal or faster. Sync cost at
this scale is dominated by transport and storage, not CRDT math.

## 2. The four candidate engines

### Automerge — automerge.org, Rust core, wasm/JS on top

- Active and shipping: Automerge 3.0 released July 2025, explicitly to cut memory use
  for client devices and "busy sync servers that hold many large documents."
  https://automerge.org/blog/automerge-3/ — v3.3.0–3.3.2 plus `automerge` crate 0.10.0
  on crates.io shipped July 2026. https://automerge.org/blog/2026-july/
- Ecosystem maturity is the strongest of the four: `@automerge/automerge-repo` 2.6.0
  (published Aug 2026), a reference websocket sync server with Docker images
  (https://github.com/automerge/automerge-repo-sync-server), a sync-server guide, an
  access-control guide, Rust + JS + Swift/Python/C/Java bindings.
  https://automerge.org/
- Rust status: the core IS Rust (wasm-bindgen builds); first-class.
- E2EE: the Beelay/Keyhive work below is Automerge's own answer. No E2EE in the base
  sync protocol; that is what Beelay exists for.
- Risk found in our bench: memory footprint on huge multi-doc workloads historically
  (their own 3.0 motivation) — relevant to a 10k-doc vault on a phone.

### Yjs / Yrs — yjs (JS), yrs (Rust port)

- Fastest thing we measured. `yrs` on crates.io is actively maintained (lib.rs page
  updated May 2026; y-crdt org commits Jan 2026; y-octo — a Yjs-compatible CRDT core —
  active). https://lib.rs/crates/yrs , https://github.com/y-crdt
- Rust status: yrs is the mature Rust implementation; pycrdt/yrb bindings exist.
  Yrs release cadence is slower than Loro/Automerge (the GitHub releases page shows
  notable pauses), but the ecosystem (Jupyter, pycrdt) keeps it exercised.
- E2EE: nothing first-party. The classic y-websocket relay holds plaintext. E2EE
  exists only as community add-ons (e.g. y-webrtc signaling still sees document IDs;
  no authoritative yjs E2EE design found). This is a real gap for our brief.
- Note: Yjs's own docs position it for collaborative editors with a live relay; for
  days-offline 10k-doc sync, automerge-repo/loro-protocol-style collection sync (sync
  all documents, not just one room) is a better fit than per-document y-websocket.

### Loro — loro.dev, Rust core

- 1.0 shipped June 2026. https://loro.dev/blog/v1.0 — positioned exactly for our use
  case: local-first, offline editing, multiple locations, and it names E2EE support as
  a 1.0 capability.
- Ships an actual sync protocol with a spec, TS + Rust implementations, websocket
  servers, multiplexed rooms, 256 KiB message fragmentation:
  https://github.com/loro-dev/protocol
- **The only mainstream CRDT library with a first-party, documented E2EE mode** (`%ELO`,
  details in section 3).
- September 2026 blog "CRDTs are not enough: From CRDTs to a local-first sync engine"
  lays out what a sync engine needs beyond the CRDT (timeouts, permissions, backend
  switching, P2P, E2EE at the same time): https://loro.dev/blog/crdt-is-not-enough —
  useful as a requirements checklist for our own design, and a signal the team is
  building exactly the layer our brief asks about.
- Risk: 1.0 is only ~4 months old; API churn possible. Bench env problem noted above.

### Diamond Types — josephg/diamond-types

- Performance is real and documented by the author ("5000x faster", then another 10–80x
  since): https://github.com/josephg/diamond-types ,
  https://josephg.com/blog/crdts-go-brrr/
- But: the README says "WIP… Do not use it for anything serious yet" (text-only, no
  rich types), the crates.io publish is stale (v1.0.0, 2022; repo master is v2.0.0
  needing Rust 1.96), and independent trackers show the repo inactive for years while
  the author works on other things (he maintains crdt-benchmarks and collaborates on
  traces). https://crates.io/crates/diamond-types ,
  https://www.libhunt.com/compare-diamond-types-vs-crdt-benchmarks
- Verdict: great reference implementation and benchmark target; wrong foundation for a
  product today. Single-author bus factor, text-only, no sync protocol, no E2EE story.

Bundle sizes (measured, `du` on installed npm packages in our bench dir): yjs 2.6 MB
installed (JS only, much smaller minified for browser); @automerge/automerge 46 MB
installed, of which the wasm core is 3.6 MB (repeated per target build in the package);
loro-crdt 22 MB installed, wasm core 3.6 MB. All three wasm cores are ~3.5 MB, so
browser/mobile footprint is comparable; Rust-native targets skip wasm entirely.

## 3. THE CRITICAL QUESTION: CRDT ops under E2EE

Rephrased precisely: can the update stream enter a relay as ciphertext, and who merges?

**Yes, it works — and in every real implementation the server does NOT merge. It
routes; clients merge after decrypt.** Two independent, shipping designs prove the
pattern:

**A. Ink & Switch: Beelay / Keyhive (Automerge's E2EE sync), July 2025 lab notebook**
https://www.inkandswitch.com/keyhive/notebook/05/

The notebook states the problem exactly as our brief does: "the sync protocol requires
that both ends are able to read the document whilst one of the objectives of Keyhive is
for the server to only have access to the encrypted data." Their solution:

- The Automerge *content* (commit graph) is encrypted; **the hashes of the commit graph
  and the document heads are kept OUTSIDE the encryption envelope**, so the sync server
  can compare document states and know which documents are out of sync without reading
  them. (Quoted design point, their words: "the document content is encrypted but we
  keep the hashes of the Automerge commit graph outside of the encryption envelope, so
  the sync server knows the heads.")
- The server cannot compact documents (compaction needs plaintext), so they invented
  "sedimentree": the commit graph is periodically compressed into recursively larger
  chunks on the CLIENT, chunk boundaries chosen deterministically by trailing-zero bits
  of commit hashes so peers agree on boundaries without coordination. Sync = exchange
  chunk summaries, then exchange missing chunks. This is the price of a
  zero-knowledge relay: the compaction step the old plaintext sync server did for free
  must move client-side.
- Set reconciliation between peers uses Rateless Invertible Bloom Lookup Tables
  (RIBLT): cost proportional to the *difference* between sets (~1.35–1.7x), not set
  size. A billion-item set differing in 5 items reconciles in ~7.5 symbols / ~240
  bytes. This is how a 10k-document vault finds the handful of stale documents cheaply.
- Key agreement is BeeKEM, a decentralized CGKA (continuous group key agreement) built
  for exactly this setting; its design rationale, security properties (including
  "cross-fork security" against compromised branches), and the concurrency-tolerance
  vs forward-secrecy trade-off are documented in notebook 06:
  https://www.inkandswitch.com/keyhive/notebook/06/ — notable finding: they set the
  security parameter to infinity in the implementation, i.e. they chose "all group
  secrets remain decryptable after arbitrary concurrent membership changes" over
  forward secrecy, because a local-first app's data must stay readable.
- Common case after optimization: a one-document change syncs in **two round trips**
  (membership+collection piggybacked, then content).

**B. Loro `%ELO` (first-party E2EE in loro-protocol)**
https://github.com/loro-dev/protocol

- "%ELO adds end-to-end encryption to Loro sync. The server never decrypts; it indexes
  plaintext headers only to support backfill and routing. Clients encrypt/decrypt using
  AES-GCM with a 12-byte IV and the exact encoded header bytes as AAD."
- There is a TS implementation (`EloAdaptor`) AND a Rust implementation, with
  cross-language E2EE interop tests in CI (`rust/loro-websocket-server/tests/
  elo_cross_lang.rs`). Key agreement is explicitly out of scope ("application-provided"
  `getPrivateKey()` hook) — the library does transport-level E2EE, not identity.
- A real product already ships this pattern: Ilow Sync, an E2EE Obsidian-vault sync
  plugin using Loro CRDTs for conflict-free merge + client-side AES-256-GCM so the
  self-hosted Go/PostgreSQL server can't read content:
  https://github.com/Ilow-Space/IlowObsidianSync

**C. What other E2EE local-first apps do**

- **Lockbook** (lockbook.net): Rust backend, E2EE ("files never leave your device
  without being encrypted with your private key", EC keys, 24-word phrase / QR device
  pairing), offline-first, sync + sharing; `lb-rs` library with C and Java bindings.
  https://lockbook.net/ , https://github.com/lockbook/lockbook . NOT a CRDT app: it
  syncs encrypted file objects in a tree, not op streams. Its precise conflict
  behavior is NOT documented in any page I could reach — the README says nothing about
  conflicts. Finding: lockbook proves E2EE + Rust + multi-device offline sync ships
  fine with whole-file sync; whether it merges or conflicts on concurrent edits is an
  open sub-question (would need reading their sync engine source, `lb-rs`).
- **Anytype / any-sync**: open-source "local-first, peer-to-peer, end-to-end
  encrypted" protocol, CRDT-based, with relays + backup nodes.
  https://github.com/anyproto/any-sync . Notably, in 2026 they added
  **iroh-based relays and pkarr** for their global P2P layer by default:
  https://github.com/anyproto/any/pull/266 — an existing E2EE local-first notes-adjacent
  app that migrated transport to iroh.
- **secsync** (Nik Graf): E2EE document sync design with a hosted relay, combining
  snapshot + updates with signature chains — an independent implementation of the same
  "opaque relay + client merge" pattern (search-verified to exist; not deep-read).

**D. The direct technical answers to the brief's sub-questions**

- Can updates be encrypted BEFORE they enter the CRDT update stream? Yes — that is what
  both Beelay and %ELO do (encrypt the serialized update/commit bytes, headers/AAD
  outside the envelope). The CRDT never sees plaintext at the relay.
- Does that allow merge on the server? No. Server-side CRDT merging requires plaintext
  (it must decode ops to build state). Every real design routes ciphertext and merges
  client-side after decryption. The relay CAN do: routing, storage, set reconciliation
  over hashes/heads, backfill indexing of plaintext headers, access decisions if
  capabilities are also encrypted (Beelay signs envelopes with Ed25519 keys and syncs
  the membership graph as its own structure).
- Cost of zero-knowledge storage: compaction and any server-side indexing beyond heads
  must move to clients (Beelay's sedimentree is exactly this tax). Budget for it.
- What stays genuinely unsolved/publicly undocumented: nothing I found describes a
  server that merges *while blind* (encrypted-domain CRDT merge, Lucretia-style
  research). "Nobody ships that" is a real finding; the industry consensus is client-side
  merge with metadata-aware relays.

## 4. Conflict files: the alternative, and how often conflicts actually happen

- Obsidian's sync is file-level. Its official troubleshooting defines conflicts as
  "you change the same file on two or more devices before they sync" and warns
  conflicts happen more often when working offline — i.e. our exact scenario maximizes
  them. https://obsidian.md/help/sync/troubleshoot
- Important correction to the brief's premise: Obsidian Sync today does NOT default to
  keep-both-and-user-merges. The shipped default is **automatic merge using
  diff-match-patch**, with conflict-copy as an option
  (https://retypeapp.github.io/obsidian/sync/troubleshoot/ mirrors the current options
  list: "Automatically merge (default)"). Obsidian is a conflict-file app only when the
  user turns that on or when sync runs over a dumb file layer (iCloud/Dropbox/Syncthing).
- Field evidence that this is painful:
  - A Jan 2025 PSA thread: months of use "plagued by consistent enough sync conflicts
    that it has been far from a set-it-and-forget-it experience", with Obsidian
    quietly reconciling in ways users miss.
    https://www.reddit.com/r/ObsidianMD/comments/1i2xuvi/
  - Obsidian's own forum on diff-match-patch merges: it "works a majority of the time,
    [but] there have been instances where it overwrote newer data for old, or sometimes
    duplicates both old and new data within the same note."
    https://forum.obsidian.md/t/robust-sync-conflict-resolution/93544
  - A feature request documenting that picking the remote version silently destroys
    the local one, and version history doesn't always save you.
    https://forum.obsidian.md/t/option-to-let-user-manually-resolve-sync-conflicts/94468
  - The keep-both variant's own complaint: conflict duplicates are created *silently*
    and found "weeks or months later."
    https://forum.obsidian.md/t/how-to-deal-with-duplicate-files-created-by-sync/83075
  - Syncthing-under-Obsidian users report conflict files as a recurring nuisance
    correlated with editing while sync is active.
    https://www.reddit.com/r/ObsidianMD/comments/1neuhip/
- Honest reading: conflict files are *tolerable* — people ship them (Obsidian users,
  Dropbox "conflicted copy", Sync.com) — but the complaints cluster on (a) silence
  (user doesn't notice the conflict file), (b) bad auto-merges, and (c) frequency
  scaling with device count and offline duration. For a notes app whose selling point
  is days-offline editing, note-content conflicts would be frequent enough to need
  automatic, correct merging — which is what CRDTs give. Where conflict files DO make
  sense for us: binary attachments and any non-text file, where CRDT semantics are
  meaningless anyway; keep-both + surface-to-user is the right tool there (this is
  also effectively Dropbox's model: last-writer-wins plus preserving the loser as a
  conflicted copy — https://help.dropbox.com/organize/conflicted-copy).

## 5. P2P vs self-hosted relay

- **Beelay's model**: relay-agnostic RPC over any confidential transport (HTTPS, WSS,
  TLS), per-envelope Ed25519 signatures with audience binding (defeats lookalike-server
  MITM) and timestamp + clock-skew negotiation (defeats replay). P2P is possible but
  needs out-of-band public-key exchange. https://www.inkandswitch.com/keyhive/notebook/05/
- **iroh** (www.iroh.computer): not independently deep-fetched in this pass, but its
  adoption is documented from the buyer side: Anytype's production P2P layer now runs
  on iroh relays + pkarr relays (relay-fr-1, relay-de-1, etc.), enabled by default:
  https://github.com/anyproto/any/pull/266 . Anytype's history is the useful precedent:
  they shipped local-P2P + their own relays + self-hostable backup nodes from the start
  (https://news.ycombinator.com/item?id=36799548 , any-sync README), i.e. they did NOT
  do pure P2P — availability came from relay/backup infrastructure all along, and later
  they standardized that infrastructure on iroh.
- WebRTC-based sync (y-webrtc): community-maintained, signaling server needed, no
  E2EE story; fine for live co-editing, weak as a days-offline transport.
- Nostr relays as sync transport: no evidence found in this pass of a notes app
  shipping it; left as an open sub-question rather than claimed either way.
- Pattern the evidence supports: ship an opaque relay for availability (it can't read
  content, so "self-hosted" and "hosted" are the same trust story), keep P2P as an
  optimization path (same LAN / direct connections), which is what both Anytype and
  Beelay effectively do.

## 6. Synthesis: the recommendation the evidence supports

For the brief's spec (local-first, zero-knowledge, Rust, 10k docs, days-offline):

- Use a CRDT for note content. The measured cost of merging 10k concurrently-edited
  docs is trivial; the failure modes it eliminates (silent bad merges, unnoticed
  conflict files, days-long offline divergence) are precisely the documented complaints
  of the conflict-file world.
- Sync architecture: ciphertext-only relay + client-side merge, with unencrypted
  heads/commit-hash metadata for sync planning. Precedents: Beelay (Automerge), %ELO
  (Loro), secsync. This is not research anymore; it is shipping code with CI-tested
  cross-language interop (Loro) and a design notebook (Ink & Switch).
- Engine pick, on current evidence: Loro (first-party E2EE mode + sync protocol spec +
  Rust core, 1.0 in June 2026, actively developed toward exactly this "sync engine"
  vision) or Automerge (deepest ecosystem, mature sync server tooling, Beelay on the
  way but pre-1.0). Yjs/yrs wins raw merge speed and has the fastest Rust port, but no
  first-party E2EE story — you would assemble Beelay-equivalent pieces yourself.
  Diamond Types: out, as a foundation.
- Fallbacks by file type: text → CRDT; binary/attachments → file-level sync with
  last-writer-wins + conflicted-copy preservation (Dropbox/Obsidian-style), surfaced
  in UI, never silent.
- The hard part to staff for is not the CRDT: it is key agreement/rotation across
  devices (BeeKEM solves it; it is a cryptographic subsystem, not a library import —
  Loro explicitly punts on it), and the client-side compaction tax (sedimentree).

## 7. Open sub-questions (honest gaps)

1. Lockbook's actual conflict behavior when two devices edit the same note offline —
   undocumented in reachable pages; would need reading `lb-rs` sync source. Worth doing
   before designing our own fallback layer, since they are the closest Rust+E2EE+notes
   product.
2. Loro `%ELO` in practice at 10k-doc scale: no published benchmark of encrypted sync
   overhead (envelope + IV + header bytes per update) exists. "Nobody has published
   this" — candidate for our own micro-benchmark before committing.
3. iroh internals (Blindfold, iroh-gossip, hole-punching success rates on hostile
   networks): iroh.computer not directly fetched this pass; adoption evidence is
   secondhand via Anytype's PR.
4. Nostr-as-sync-transport: no shipped example found either way.
5. Automerge 3 on 10k docs in constrained memory: our failing 10k run was the old
   2.0.0-alpha npm package; re-run with automerge 3.x (npm `@automerge/automerge@^3`)
   before treating the memory problem as current.
6. Loro-crdt wasm crash on this box's Node 22: unexplained; if we build on loro, first
   task is pinning a Node/rust toolchain where the wasm loads (or going Rust-native,
   where it doesn't apply).
7. Cost of keeping "plaintext headers" indexable at the relay (Loro) vs Beelay's
   stricter "only hashes outside the envelope": a privacy/perf trade-off nobody has
   quantified; we'd choose per our threat model.

## Sources (primary where possible)

- Ink & Switch Keyhive notebook 05, "Syncing Keyhive" (Beelay, sedimentree, RIBLT):
  https://www.inkandswitch.com/keyhive/notebook/05/
- Ink & Switch Keyhive notebook 06, "E2EE in the Local-First Setting" (BeeKEM):
  https://www.inkandswitch.com/keyhive/notebook/06/
- loro-dev/protocol README (%ELO spec, cross-language E2EE tests):
  https://github.com/loro-dev/protocol
- Loro 1.0 announcement: https://loro.dev/blog/v1.0
- Loro, "CRDTs are not enough": https://loro.dev/blog/crdt-is-not-enough
- Loro protocol announcement: https://loro.dev/blog/loro-protocol
- Ilow Sync (Loro + AES-GCM E2EE Obsidian sync): https://github.com/Ilow-Space/IlowObsidianSync
- Automerge 3.0 blog: https://automerge.org/blog/automerge-3/
- This Month in Automerge, July 2026: https://automerge.org/blog/2026-july/
- automerge-repo-sync-server: https://github.com/automerge/automerge-repo-sync-server
- Automerge homepage (bindings, repo/sync server): https://automerge.org/
- y-crdt org / yrs: https://github.com/y-crdt , https://lib.rs/crates/yrs ,
  https://crates.io/crates/yrs
- Diamond Types repo, crates page, author's blog, LibHunt activity:
  https://github.com/josephg/diamond-types , https://crates.io/crates/diamond-types ,
  https://josephg.com/blog/crdts-go-brrr/ ,
  https://www.libhunt.com/compare-diamond-types-vs-crdt-benchmarks
- Lockbook homepage + repo: https://lockbook.net/ , https://github.com/lockbook/lockbook
- any-sync repo: https://github.com/anyproto/any-sync
- Anytype iroh/pkarr PR: https://github.com/anyproto/any/pull/266
- Anytype HN threads (backup-node model): https://news.ycombinator.com/item?id=36799548
- Obsidian Sync troubleshooting: https://obsidian.md/help/sync/troubleshoot
- Obsidian forum threads: 93544 (robust conflict resolution), 94468 (manual resolution
  request), 83075 (silent duplicates); Reddit PSAs 1i2xuvi (sync corruption PSA),
  1neuhip (Syncthing conflicts)
- Dropbox conflicted copy: https://help.dropbox.com/organize/conflicted-copy
- Benchmark artifacts (this box): /home/thaura/notesapp/benchmarks/thread-a/bench.js ,
  results.json , bench3.log
