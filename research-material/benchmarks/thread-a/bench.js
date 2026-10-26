// Thread A benchmark: 10k small notes, two offline devices, merge.
// Measures: per-doc edit+export, bulk merge time, merged doc integrity.
const fs = require('fs');

const N = 10000;           // documents
const TEXT_LEN = 500;      // chars per note (~ a short note)
const CHARS_PER_EDIT = 50; // device B edits within existing text

function randText(len) {
  let s = '';
  for (let i = 0; i < len; i++) s += String.fromCharCode(97 + ((Math.random() * 26) | 0));
  return s;
}

async function benchYjs() {
  const Y = require('yjs');
  const docsA = [], docsB = [];
  const t0 = performance.now();
  for (let i = 0; i < N; i++) {
    const d = new Y.Doc();
    d.getText('body').insert(0, randText(TEXT_LEN));
    const u = Y.encodeStateAsUpdate(d);
    // device B: its own doc with concurrent insert at position 10
    const d2 = new Y.Doc();
    Y.applyUpdate(d2, u);
    d2.getText('body').insert(10, randText(CHARS_PER_EDIT));
    docsA.push({ d, u });
    docsB.push({ d: d2, u2: Y.encodeStateAsUpdate(d2) });
  }
  const tEdit = performance.now() - t0;
  const t0m = performance.now();
  let ok = 0;
  for (let i = 0; i < N; i++) {
    Y.applyUpdate(docsA[i].d, docsB[i].u2);
    if (docsA[i].d.getText('body').length === TEXT_LEN + CHARS_PER_EDIT) ok++;
  }
  const tMerge = performance.now() - t0m;
  const bytes = docsA.reduce((s, x) => s + x.u.length, 0);
  return { lib: 'yjs@' + require('yjs/package.json').version, editMs: tEdit, mergeMs: tMerge, ok, updateBytes: bytes };
}

async function benchAutomerge() {
  const A = require('@automerge/automerge');
  const N = 1000; // reduced: 10k docs exhausted RAM/2GB wasm on this box (see notes)
  const docsA = [], docsB = [];
  const t0 = performance.now();
  for (let i = 0; i < N; i++) {
    let d = A.from({ body: randText(TEXT_LEN) });
    const u = A.getAllChanges(d);
    // device B clones and edits concurrently
    let d2 = A.clone(d);
    d2 = A.change(d2, (s) => { s.body = s.body.slice(0, 10) + randText(CHARS_PER_EDIT) + s.body.slice(10); });
    docsA.push({ d, u });
    docsB.push({ d: d2, u2: A.getAllChanges(d2) });
  }
  const tEdit = performance.now() - t0;
  const t0m = performance.now();
  let ok = 0;
  for (let i = 0; i < N; i++) {
    let d = A.clone(docsA[i].d);
    const applied = A.applyChanges(d, docsB[i].u2);
    d = Array.isArray(applied) ? applied[0] : applied;
    if (d.body.length === TEXT_LEN + CHARS_PER_EDIT) ok++;
  }
  const tMerge = performance.now() - t0m;
  const bytes = docsA.reduce((s, x) => s + x.u.reduce((a, c) => a + c.length, 0), 0);
  return { lib: 'automerge', editMs: tEdit, mergeMs: tMerge, ok, updateBytes: bytes };
}

async function benchLoro() {
  const L = require('loro-crdt');
  const docsA = [], docsB = [];
  const t0 = performance.now();
  for (let i = 0; i < N; i++) {
    const d = new L.LoroDoc();
    d.getText('body').insert(0, 0, randText(TEXT_LEN));
    d.commit();
    const u = d.export({ mode: 'update' });
    // device B receives A's update and edits concurrently
    const d2 = new L.LoroDoc();
    d2.import(u);
    d2.getText('body').insert(0, 10, randText(CHARS_PER_EDIT));
    d2.commit();
    docsA.push({ d, u });
    docsB.push({ d: d2, u2: d2.export({ mode: 'update', from: d.version() }) });
  }
  const tEdit = performance.now() - t0;
  const t0m = performance.now();
  let ok = 0;
  for (let i = 0; i < N; i++) {
    const r = docsA[i].d.import(docsB[i].u2);
    if (r.ok && docsA[i].d.getText('body').toString().length === TEXT_LEN + CHARS_PER_EDIT) ok++;
  }
  const tMerge = performance.now() - t0m;
  const bytes = docsA.reduce((s, x) => s + x.u.length, 0);
  return { lib: 'loro-crdt@' + require('loro-crdt/package.json').version, editMs: tEdit, mergeMs: tMerge, ok, updateBytes: bytes };
}

(async () => {
  const results = [];
  for (const fn of [benchYjs, benchAutomerge]) {
    try { results.push(await fn()); }
    catch (e) { results.push({ lib: fn.name, error: String(e && e.message || e), stack: e && e.stack ? e.stack.split('\n').slice(1,4).join(' | ') : '' }); }
  }
  const out = { n: N, charsPerNote: TEXT_LEN, concurrentEditChars: CHARS_PER_EDIT, results };
  fs.writeFileSync('/home/thaura/notesapp/benchmarks/thread-a/results.json', JSON.stringify(out, null, 2));
  console.log(JSON.stringify(out, null, 2));
})();
