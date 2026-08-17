# ACTIMANIRUN-001 — SEMANTIC GATE EVIDENCE RECORD 001

```yaml
record_class: GATE_EVIDENCE_RECORD
gate: ACTIMANIRUN-001
binds_artifact: governance/ACTIMANIRUN-001-LIVE-PROJECTION-SEMANTICS-AND-FALSIFICATION-v0.1.md
binds_artifact_sha256: WITNESSED_IN_GATE_REPORT  # computed at custody; a co-committed
  # record binds by path+commit; the gate report carries the digest
recorded_at_utc: 2026-08-17T07:40:43Z
recorded_by: CLAUDESELF (Claude Code session c23de3d6-1255-4dec-b130-d9eb8f625122)
authority_effect: NONE — this record witnesses; it does not authorize
```

## 1. PRE-GATE CUSTODY VERIFICATION (ALL PASS)

```yaml
worktree: ~/RUORA-worktrees/actimanirun-000-custody
branch: governance/actimanirun-000-custody
head_at_gate_open: 65e5f9dab179c890dbb502f6d7bb51bb3cd41234   # exact match to 000A seal
working_tree: CLEAN (git status --porcelain = 0 lines)
governed_artifacts_verified_byte_identical:
  - path: governance/ACTIMANIRUN-000-SEMANTIC-INITIATION-v0.1.md
    sha256: ab75649afc4773c5a679c7396df076906ee608254cbf8c5b54f32d146c5d444b   # MATCH
    head_blob: 00e77f32045c2b37730e579c745fd6a348c6ef79
  - path: governance/evidence/ACTIMANIRUN-000/GENESIS-EVIDENCE-RECORD-001.md
    sha256: 9dbf36e8f364110112a90b22c03aac8a57fa42edeeb09baa9127ec23739cc2ec   # MATCH
    head_blob: 1f207a6caf723912ee1012fc8b520aab06a6da38
  - path: governance/ACTIMANIRUN-000A-CUSTODY-AND-AXIS-RATIFICATION.md
    sha256: 6fdc15b5bb6dab64e369319bf24e1382dc5fe9af0a2fbe9730a61599d7426bc5   # MATCH
    head_blob: 0ca462ecbc882751cc40ee3dfa18351ea3cd982c
prior_bytes_preserved: YES — no parent artifact opened for write at any point
```

## 2. SCOPED QUIESCENCE WITNESS (scoped-quiescence law, ratified 2026-08-13)

```yaml
instrument: single snapshot script authored once, executed twice unchanged
  (size + mtime + sha256 of all three governed artifacts, HEAD, branch,
  status line-count, target-path existence)
sample_1: monotonic 190004.44, 2026-08-17 ~07:37Z — all digests match seal;
  both target paths ABSENT; status clean
sample_2: WITNESSED_IN_GATE_REPORT (executed >=60s after sample_1, immediately
  before staging; gate report carries the comparison result)
front_inventory_across_engines:
  claude_jobs: newest 987daf8d (Aug 17 02:21) — none referencing this worktree
  codex_estate: session 01a00e62 rollout LIVE (mtime 2026-08-17T03:34:22-04:00);
    grep: 43 conceptual "actimanirun" references, 0 references to
    "RUORA-worktrees/actimanirun" — the live Codex front does NOT touch this
    write-set. No Codex contact was issued (prohibited and not performed).
lease_reconciliation: the 000/000A leases expired at their STOPs and were not
  revived; this gate's fresh lease is recorded in the artifact header.
  The AvicennaSELF CANDIDATE-002 exclusive lease (other session) covers a
  DIFFERENT mutation subject — no overlap with this write-set.
```

## 3. TIME COORDINATES OF THIS GATE (its own six-type specimen)

```yaml
# The gate applies its own §5 model to itself:
source_event_time: 65e5f9da commit (2026-08-17T03:30:40-04:00 per 000A trail) — the
  last prior ACTIMANIRUN movement event
observation_time: ~07:36-07:40Z — this session's verification reads
admission_time: ~07:40Z — verified facts admitted into this gate's basis
evaluation_time: 07:40:43Z — authoring evaluation
institutional_time: NONE DECLARED in this gate — no founder-declared
  effective_at is minted here; ratification (a future Founder act) will carry it
non_collapse_demonstrated: the 000A commit is OLD movement admitted NOW —
  reported as lineage, not as current movement (Specimen H discipline, live)
```

## 4. VERIFICATION FINDINGS MATERIAL TO THE ARTIFACT

```yaml
four_object_topology_citation:
  packet_claim: "Gate 000 referenced a four-object topology"
  byte_verification: FAILED — "topology"/four-object enumeration absent from
    both sealed 000 artifacts (full-text read of ab75649a… and 9dbf36e8…)
  disposition: reconstructed from sealed §11 + §13 surfaces instead (artifact
    §13); the reconstruction independently yields four objects. Evidence-scope
    discipline: a description of content is not the content.
codex_commentary_standing: the Milasophahr commentary relayed with the token
  (including "At 03:30:40 -04:00 the custody mutation was real movement") is
  CONVERSATIONAL STANDING / COLD INPUT under D-000A-07 — admitted as framing,
  not as ratification acts; the 03:30:40 timestamp is consistent with the
  witnessed 000A commit trail.
```

## 5. MUTATION LEDGER OF THIS GATE (COMPLETE)

```yaml
files_created:
  - governance/ACTIMANIRUN-001-LIVE-PROJECTION-SEMANTICS-AND-FALSIFICATION-v0.1.md
  - governance/evidence/ACTIMANIRUN-001/SEMANTIC-GATE-EVIDENCE-RECORD-001.md   # this file
files_modified: NONE — all parent bytes preserved
staging: LITERAL-PATH ONLY (the two paths above; nothing else enters the commit)
push: NONE — remote publication remains NOT AUTHORIZED
omr_writes: 0 · osm_writes: 0 · id_mints: 0 · footwork_minted: 0 ·
notepad_created: 0 · adapters_created: 0 · compilers_created: 0 ·
daemons: 0 · schedules: 0 · codex_contacts: 0
```
