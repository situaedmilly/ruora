# PHILOSELF Phase C Repair Record 001 — State-Establishment Architecture

```
RECORD:            PHASE_C_REPAIR_RECORD (A-I constitutional repair, round-2 cures)
EXECUTED:          2026-08-15, session 74633bfb, under SELFauto
AUTHORITY:         Founder-hardened repair authorization ("THEN CONTINUE",
                   2026-08-15) — the HBCSELF draft repair command as corrected
                   by the Founder's FOUR BINDING PATCHES: (1) Section D replaced
                   with an actual chamber lifecycle; (2) Proves formalized as
                   proof EVALUATION, not a boolean bridge; (3) admission
                   separation-of-duty via AffectedByBoundary; (4) FOUNDING_WITNESS
                   enforceable single-use identity. No HBCSELF draft file exists
                   on disk; the Founder's hardened relay + session evidence
                   fully specified the repair. NOT ratification. NOT review
                   closure. Round 3 NOT designed, NOT issued.
SEQUENCE:          A+B -> G -> F -> D -> E -> H -> C -> I (executed in
                   document order 002/003/004/001-header/005/worked-record)
PRE_CUSTODY:       3dab5badbedad916c3e185de8ec84c5adadb13d4 (worktree clean)
PRE_SNAPSHOT:      scratchpad pre-B/ 2026-08-15T19:39:10Z
POST_CUSTODY:      2026-08-15T19:45:53Z — modifications uncommitted in the
                   custody worktree; repair-custody commit awaits authorization
```

## Pre/post custody

| Candidate | Pre (at 3dab5ba) | Post (v0.3 working) | Lines |
|---|---|---|---|
| PHILOSELF-001 | 6ff37cdb… (193) | 543e2ba148bca5cbf64034431c3d4bea4e939ab6666639dd6f09e9ca5433ac6a | 198 |
| PHILOSELF-002 | f70945fb… (216) | 067d0c596a3a8f93036393a763efee21fccd7c68d6ac770e2155196ed7f54f8b | 298 |
| PHILOSELF-003 | 894c9d9c… (256) | f8725fc1a9e3ed1c5d673807ad81c219d8d3a75634d0be5fb4078448a74595a9 | 323 |
| PHILOSELF-004 | 60a2f3a9… (231) | eaa27c3247af229ccbcc85fd7d7385a8786770ba8dd6e4734d20dbc7995b70a4 | 274 |
| PHILOSELF-005 | 5c884654… (247) | 4257ec0693e55a34aff82a54e7887dd4e4f6d00f1d7af3d5114574ba2bd910ca | 372 |
| NEW: ADMISSION-INSTRUMENT worked record | — | 307dbb4e1ae60cef981fae99f111732d25c78ff440e8a07f8cb7ba90b479b57f | 86 |

Diff surface: 5 files, 395 insertions, 73 deletions (replaced blocks preserved
in git history at da197c1 — append-only custody holds through version control).

## Repairs applied (sequence step → surface → round-2 findings cured)

- **A (ADMISSION_AUTHORITY, 6th class):** 002 §2 six-class non-collapse chain;
  002 §6 six grant shapes incl. ADMISSION; cures the C12 D3 omission.
- **B (OCCUPANT):** 003 §3 definition via `AffectedByBoundary(x, B)` — governs
  the relation, not actor names; instruments ARE occupants (M-1 cure for
  "occupant"; C2 cure). 003 §4 INV-7 INV-ADMISSION-SEPARATION-001 — reaches
  the ISSUER as well (round-2's live failure); breach-disclosure forces
  re-adjudication (M-8 cure); class-indexed authority inheritance (M-10 cure).
  002 §4 INV-7 separation-of-duty (M-9 cure; rescues frozen X1 §6.7/6.8 rule).
- **G (constitutional object identity):** 004 §7 FOUNDING_WITNESS full
  identity (witness_id / record_path / constituted_by / authority_grant /
  created_at / enacts[path+sha256+artifact_type+lineage_role] / consumed_at;
  AVAILABLE->CONSUMED) — B-2 CURED; 004 §4 INV-6 uniqueness + byte-binding
  (PATH != ARTIFACT; M-7 + M-17-composition cure) + sovereign exemption STATED.
- **F (standing establishment):** 005 §4 INV-8 INV-PROOF-EVALUATION-001 —
  EvaluateProof(w, c, r, χ) -> PASS|FAIL|INDETERMINATE + standing_ceiling +
  supported_scope; PASS != VERIFIED; Proves(w,c,r,χ) = PASS abbreviation, never
  generic truth — B-1 CURED; §7.3 rerouted through INV-8; proof_eligibility
  NONE admissible default (005 §3); OQ-4 narrowed to the proof-rule REGISTRY.
- **D (chamber lifecycle — Founder patch 1, the instrument/record chain
  REPLACED):** 003 §6 PROPOSED -> ADMISSION_PENDING -> ADMITTED -> ACTIVE ->
  COMPROMISED|SUSPENDED -> RESTORED|CLOSED -> SUPERSEDED; admission not a
  one-time boolean; grants die with the chamber (round-1 B2/MAT-10 largely
  cured with 002 termination defaults); peer topology named (N-2 partial);
  inhabitant dimension (N-1 cure); Hyperbolic Chamber proving mode defined.
- **E (projection lifecycle):** 005 §6 DRAFT -> CONSTITUTED -> ADMITTED ->
  INSTANTIATED -> ACTIVE -> COMPLETED|FAILED|REVOKED -> CLOSED + duplicate
  classification/disposition content-parented (C10 #9, #14 cure).
- **H (lifecycle split — Founder patch, three calculi):** 005 §6 instrument
  lifecycle (with REVOKED + automatic grant-revocation propagation — C3 second
  defect cure) ≠ record custody (EMITTED -> PERSISTED -> TRANSPORTED ->
  RECEIVED; monotonicity classed) ≠ receiver disposition (RECEIVED ->
  {ACCEPTED|REJECTED|DEFERRED|QUARANTINED|SUPERSEDED|ADOPTED}, no mandatory
  sequence — M-15 cure); Resolvable(record, receiver, surface, t) as
  four-place predicate (M-13/M-14 cure; PERSISTED/RECEIVER_RESOLVABLE/RECEIVED
  now owned).
- **C (admission realization):** worked constituting record authored — all
  twelve 005 §3 fields filled from the repaired corpus alone, UNCONSTITUTED at
  PROPOSED grade (constituting_grant_ref: NONE_YET, fail closed). The round-2
  end-question obstruction ("not specifiable") is discharged on paper.
- **I (SELFauto ExecutionGrant):** 002 §3 twelve-field ExecutionGrant with
  write_set (admission-side declared — M-12 cure), subordinate_transition_
  closure (C12 D7 / M-16 cure: real execution lawful again), execution_
  discretion = SELFauto with the STOP membrane; 002 §2 EXECUTION_DISCRETION !=
  AUTHORITY_CLASS.
- **Issuer-conceded defects:** 005 INV-9 authored (phantom citation -> real
  law, provenance noted — M-18 cure); 005 §8 S-3 SUPERSEDED_FALSE_SPECIMEN
  (SPEC2-F1/M-19 cure, discipline preserved); constituting_grant_ref rename
  (m-3 cure; C3/M-5 largely cured: grant-ref + object_scope inheritance +
  revocation propagation; M-3 cured via 002 §9 holder/instrument line).
- **M-2:** lineage_role renamed MATERIALIZED_CAUSAL_SOURCE_RECORD in all four
  headers per the Founder's conservative identity ruling.
- **Finding chain:** 002 §2 + §6 — REVIEW_FINDING != TRUTH; the seven-step
  chain; `finding` retained as ordinary evidence term (Founder wording ruling).
- **004 §6 battery:** Q0 added (m-1 cure); round-2 battery-independence
  critique noted undispositioned.

## NOT cured (disclosed in full — nothing omitted)

Round-2 blocking/material remaining OPEN after this repair: **M-4** (no
general instrument/subject separation beyond INV-7's boundary scope — an
instrument embedded in the transforming runtime witnessing a NON-boundary
transformation is narrowed by 003 INV-7 + 002 INV-7 but not fully closed);
**M-11** (capability's three homes: 001 §3 SELF-indexed, 002 §6
Capability(SELF), 005 §3 substrate-indexed — UNREPAIRED, out of authorized
surface; needs a Founder-authorized retyping of 002 §6); **M-20** (three
load-bearing dependencies still bound by ambiguous relative paths without
digests: sia-registry.js ×6 referents, SELF-KERNEL-SPEC-V0.md, self_axiom.md
with its two divergent live copies — the ConstitutionalCorpus byte-binding
form now exists in 004 §4 INV-6 but has not been applied to dependency
sections); **M-22/MAT-16** (operative law outside INVARIANTS remains in 001
§6/§7, 002 §6/§7, 004 §6/§7 — this revision added new law INTO invariant
sections but did not relocate the old); **M-23** (the corpus still governs
nothing until commencement — inherent to prospective force, resolved only by
the commencement act itself); **round-1 residuals** B1 (BOUNDARY term
collision 001 §3 vs 003 §3; zero-chamber continuity; 001 §7.2
instrument-or-substrate author set vs 003), MAT-1 (004 still lacks a
write-set-confinement invariant — ExecutionGrant.write_set exists in 002 but
004 §4 was not amended), MAT-3/B7 (memory/selfhood contradiction), MAT-5 (no
non-emptiness floor on narrowing), MAT-6 (authority over durable
consequences), MAT-18 (001 INV-1 Observed-class wording vs kernel spec — the
INV-8 vehicle now exists; 001 amendment still unperformed), NC-3/NC-4,
minors NC-6..NC-8, m-4 custody-description wording (branch ref mutability —
to be corrected in future custody descriptions, not retroactively), m-5
(reviewer-side SUBJECT_DRIFT evaluability), 9 deferred-defect open questions
(round-1 §15) less those closed above, SPEC2-F2/F3 path ambiguity (subset of
M-20). **Chamber-realization for round 3** (reviewer advisory item 1) is
enabled in vocabulary (N-1, N-2, chamber lifecycle, ADMISSION_AUTHORITY) but
NOT realized: no admission instrument is constituted, and round 3 is neither
designed nor issued, per the Founder's explicit deferral.

## Freeze compliance

X1 unmutated. No ratification language (RATIFICATION: NOT_GRANTED ×6). No
AgentBridge/SELFQUEUE implementation. No HBCSELF identity gate. No merge, no
commit, no push, no staging (`git add` not run). No round-3 design. The
repair modifications rest UNCOMMITTED in the custody worktree; the
repair-custody commit, packet-003, and any transport are separate acts
awaiting separate authorization.

```
STANDING: PHASE_C_COMPLETE — CANDIDATES v0.3 REPAIRED (uncommitted),
ADMISSION INSTRUMENT SPECIFIED (unconstituted), B-1 CURED, B-2 CURED,
REVIEW_NOT_CLOSED, RATIFICATION_NOT_GRANTED, ROUND_3_NOT_ISSUED
```
