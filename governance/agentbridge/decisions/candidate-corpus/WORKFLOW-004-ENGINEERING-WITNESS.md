# WORKFLOW-004 — ENGINEERING WITNESS

STATUS: READY_FOR_FOUNDER_RATIFICATION_REVIEW — not yet dispositioned.
CLASS: Engineering Evidence — this witness does not itself become law and
  does not ratify `workflow/00-07`; it supports a future Founder decision
  on whether/how to do so.
EXECUTION_AUTHORITY: NONE.
MUTATION_AUTHORITY: NONE. No file in `workflow/00-07` was edited. No
  Founder Disposition was created.
STAGING/COMMIT/PUSH/PUBLICATION: NONE.

────────────────────────────────────────
A. UTC WINDOW
────────────────────────────────────────
2026-07-30 (date only — same disclosed clock-time limitation as every
prior witness this session).

────────────────────────────────────────
B. REPOSITORY, BRANCH, AND HEAD
────────────────────────────────────────
Repository: /Users/millysituated/RUORA
Branch: main
HEAD: 1a7475a533cb14560f307fa6d199cfeca997323e (unchanged throughout this
  gate).

────────────────────────────────────────
C. READ (per WORKFLOW-004's own token-alchemy constraint: workflow/00-07,
   referenced Founder dispositions, lineage records required — no
   rediscovery, no redesign)
────────────────────────────────────────
Full read, this session, of all 8 `governance/agentbridge/workflow/*.md`
files (headers had been read under WORKFLOW-003; full bodies of
`01_SESSION_BOOTSTRAP.md` through `07_LAUNCH_ROADMAP.md` were read fresh
under this gate specifically to check for internal authority citations —
`00_MANIFEST.md` was already read in full under WORKFLOW-003 and is
re-cited, not re-read, here).

Re-cited, not re-read fresh (already read in full under WORKFLOW-003,
still valid per this session's continuous context): all four
`decisions/ratified/FOUNDER-DISPOSITION-00{1,2,3,4}-*.md` records;
`GOV-LINEAGE-001-...md`; `LINEAGE-DEFECT-PATTERN-DEFINITION.md`;
`runtime/agentbridge/governance/LIMITED_SELFLAUNCH_OPERATING_BOUNDARY.md`.

Additional verification performed this gate (confirming, not
rediscovering): `grep -n "SL-008\|LIMITED_SELFLAUNCH\|Founder\|ratif"`
across all 8 workflow files, to confirm the SL-008A/LIMITED_SELFLAUNCH
citations found in `04_GATE_EXECUTION.md` and `07_LAUNCH_ROADMAP.md` are
the only such citations in the stack (confirmed — no other file in
`01-06` contains either term); `shasum -a 256` of all 8 files (recorded in
E, and provided as the evidence basis a future ratifying gate would need,
per the specification's §G); `stat -f mtime` of all 8 files (confirmed
unchanged from every prior recording this session: 2026-07-27
19:33:57–19:36:57); `git status --porcelain`.

No AgentBridge kernel/control-plane runtime was inspected or invoked. No
document outside the set named above was read under this gate — in
particular, `agent-selfrealization/*`, `GATE-3`, `SR-EXEC-001-*`,
`WORKFLOW-001/002 spec+witness`, and `doctrine/runtime-doctrine-stack.md`
were **not** re-read this gate; where cited below, they are cited from
facts already established and recorded in
`WORKFLOW-003-...-SPECIFICATION.md`, not from a fresh read, consistent
with this gate's "no rediscovery" constraint.

────────────────────────────────────────
D. PRODUCED
────────────────────────────────────────
Exactly two files, both new:
  1. `WORKFLOW-004-FOUNDATIONAL-WORKFLOW-AUTHORITY-SPECIFICATION.md` —
     findings for Objectives A–F: no existing ratified chain covers
     `workflow/00-07` as a document set (A); the smallest lawful
     mechanism is the stack's own Decision-only gate template plus the
     existing Founder Disposition Record format (B); retrospective
     ratification is lawful under this corpus's own established practice
     (C); replacement is not indicated (D); the four existing Founder
     Dispositions remain independently valid regardless of this finding
     (E); one canonical recommendation — ratify by attestation, via a
     future bounded Decision-only gate (F).
  2. This file.

No workflow file edited. No doctrine edited. No schema touched. No
Founder Disposition created — one path is recommended, not issued, per
WORKFLOW-004's own explicit prohibition on "Ratifying documents" and
"Creating Founder dispositions."

────────────────────────────────────────
E. SCOPE COMPLIANCE
────────────────────────────────────────
Confirmed fresh, not assumed:
  - `find governance -type f -newermt <turn-start-timestamp>` returns
    exactly the three files expected: the two WORKFLOW-003 outputs
    (already existing from the prior gate) and this gate's own
    specification (checked before this witness file itself was written).
  - `git status --porcelain`: identical to every prior recording this
    session — same five untracked top-level paths, none newly modified.
  - All 8 `governance/agentbridge/workflow/*.md` files: mtimes unchanged
    (2026-07-27 19:33:57–19:36:57) and content hashes recorded fresh this
    session:

```
00_MANIFEST.md            88c55b89748ca0e68d0bd89095e10bc095801a0162dcfb71172b8379d54762d2
01_SESSION_BOOTSTRAP.md    b7264d592216990c0b57df4d959ad333045f3ae1d36058ca6de7759d88fbdd9e
02_SYNCHRONIZATION.md      87275a44d3c8f5f28935c852e38c47477f5b92adb05a9c75cc490eb56f78eac3
03_GATE_SELECTION.md       7fe194c2d40f361a0a3b54d7b332e653c341730fd6e1ac80a755efcaa1e6acae
04_GATE_EXECUTION.md       f9bb54619a1ac14d20efd196d75bff12ee5f13a8f6d48a429b72fdc6cc6d1b34
05_VERIFICATION.md         7856e9269d6be80479b203f3a8f6080f051907c1107d0f484851c76a089f7a37
06_SEAL_OR_HOLD.md         244787e163831a214f6644253f39be0318ed6cf215187449c2f0d72daede1f9c
07_LAUNCH_ROADMAP.md       d23726f8606a21afcd7b5f2e50fd7c2fb57c0ac47f987ad5d5dd98b786fc6f91
```

  These are recorded here as a durable anchor: no prior witness in this
  corpus had hashed these 8 files before (they were previously referenced
  only by mtime). A future ratifying gate, or any future amendment gate,
  now has a concrete baseline to diff against — the same kind of gap
  GOV-LINEAGE-001 named for the corpus generally, closed here specifically
  for this one subtree, to the extent a content hash (not a Git commit)
  can close it.
  - No staging, commit, push, or publication performed at any point.

────────────────────────────────────────
F. WHAT THIS DOES NOT ESTABLISH
────────────────────────────────────────
This witness does not ratify `workflow/00-07`. It does not establish that
the stack is unauthorized or improperly relied upon — to the contrary, it
finds real, ratified grounding upstream (`LIMITED_SELFLAUNCH`/SL-008A) and
no content defect. It narrowly establishes that the ratification covering
that upstream decision does not, by its own stated scope, extend to these
8 documents as governance artifacts, and that no separate ratification
event does either. It does not resolve GOV-LINEAGE-001. It does not touch
the three stale-status-header findings from WORKFLOW-003 (schema,
WORKFLOW-001 spec, WORKFLOW-002 spec) — excluded per this workflow's own
calling instruction. Per this corpus's signal non-equivalence law:
analysis is not authorization; this gate performed analysis only.

────────────────────────────────────────
G. RECOMMENDED FOUNDER DISPOSITION (recommendation only — not self-issued)
────────────────────────────────────────
The specification is internally consistent, every claim is grounded in a
direct citation (a line number, a hash, a chronology, or a named prior
Founder Disposition) rather than inference, and it stays within the
AUTHORITY_LINEAGE_ONLY scope WORKFLOW-004 itself defines. On those narrow
engineering grounds, **APPROVE** is supportable for the specification as
an authority-lineage record.

What the Founder is actually being asked to weigh, separately from the
engineering assessment above:

1. **Whether to open the ratification gate this document recommends.**
   The specification's §F recommendation — a bounded Decision-only gate
   producing a `FOUNDER-DISPOSITION-00N-WORKFLOW-STACK-WITNESS.md` — is
   not itself authorized by this witness. It is the next available lawful
   step, not a step already taken.
2. **Whether "ratify by attestation" is the right remedy**, versus, e.g.,
   deferring ratification until Git lineage is also resolved (folding this
   into GOV-LINEAGE-001's own eventual Genesis Commit sequence rather than
   running it as a separate, earlier gate). This document recommends the
   former (a smaller, independent, immediately-actionable gate) but the
   Founder may reasonably prefer to sequence it after GOV-LINEAGE-001
   instead, since both ultimately touch the same untracked tree.
3. Nothing about this finding requires urgent remedy — per E, all four
   existing Founder Dispositions remain valid on their own terms regardless
   of when or whether `workflow/00-07` itself is formally ratified.

Allowed dispositions, per this corpus's existing vocabulary:
  APPROVE — this authority-lineage record becomes canonical; the
    recommended ratification-gate path (§F) is accepted as the next lawful
    step, without yet authorizing that gate to run.
  APPROVE WITH AMENDMENTS — specify which finding needs correction.
  RETURN FOR REVISION — specify what's missing.
  HOLD — if the Founder prefers to sequence this behind GOV-LINEAGE-001.

────────────────────────────────────────
H. VERDICT
────────────────────────────────────────
READY_FOR_FOUNDER_RATIFICATION_REVIEW.

Both required outputs are complete, every load-bearing claim is grounded
in a direct citation freshly re-verified this session (line numbers,
hashes, mtimes, chronology), scope containment is confirmed (exactly two
new files, all 8 workflow files confirmed byte-identical via hash, no
staging/commit/push), and the gate stops here, per WORKFLOW-004's own
closing instruction: "Stop immediately after witness generation."
WORKFLOW-005 cannot begin until this document receives Founder
disposition.
