# PHILOSELF Boundary Review Annex 002 — Lifecycle and Authority-Class Attack Surfaces

```
ANNEX_TO:            governance/PHILOSELF-BOUNDARY-REVIEW-PACKET-002.md
                     (sha256 a154e670ff108eddac70b14eb6f45336e8dd474b57270bc2f101d37e84c7020f)
CLASS:               ATTACK INSTRUMENT — not canon, not doctrine, not law
AUTHORED_UNDER:      AUTHORIZE_PHILOSELF_BOUNDARY_HOSTILE_REVIEW_002 §2
                     (review issuance authority only)
AUTHOR_SELF:         session 74633bfb (issuer; also authored all subjects —
                     reviewer exclusion per packet-002 §3 applies)
STANDING OF THE TWO CHAINS BELOW: Founder-locked-in-channel doctrine UNDER
                     HOSTILE TEST. Founder authorization of hostile testing is
                     NOT ratification. The reviewer's job is to try to break
                     them, not to defer to them.
RELATION:            APPENDS attack surface. AMENDS NOTHING.
```

## C11 — INSTRUMENT LIFECYCLE SEPARATION

Chain under attack:

```
CONSTITUTED
!= EMITTED
!= PERSISTED
!= TRANSPORTED
!= RECEIVER_RESOLVABLE
!= RECEIVED
!= ACCEPTED
!= ADOPTED
```

Live specimen (disk-bound, no invention required): the emitter of
INSELFACTION-PHILOSELF-MANIFESTATION-001 declared "emitted" while the receiver
resolved a stale pointer. Evidence readable by the reviewer at
`/Users/millysituated/self-communication` (local clone of
situaedmilly/self-communication): defective state at commit `83ac4a5` (pointer
named ISA-20260815-SELFHTML-SEMANTICS-DELTA-HOSTILE-REVIEW-PREP-003, archive
absent), cure at commit `1c02b715` (archive
`inselfactions/INSELFACTION-PHILOSELF-MANIFESTATION-001.json`, whose
`transport_defect_cured` block records the defect from inside the cure).
Receipt was acknowledged receiver-side (CHATGPTSELF) only afterward.

The reviewer must determine:

1. whether all eight are semantically distinct;
2. whether any are events rather than states;
3. whether ordering is total, partial, or invalid;
4. whether transitions can reverse;
5. whether supersession or expiry belongs in this lifecycle;
6. whether receiver-resolvability is instrument-generic or transport-specific;
7. whether ACCEPTED and ADOPTED belong to instrument lifecycle or to receiver
   disposition;
8. which PHILOSELF candidate owns each distinction — and where NO candidate
   owns one, say so plainly (an unowned distinction is a finding, not a gap to
   paper over).

Note the collision surface with PHILOSELF-005 §6, whose instrument lifecycle
(PROPOSED → CONSTITUTED → COMMISSIONED → OPERATING → SUSPENDED | SUPERSEDED |
DECOMMISSIONED) models the INSTRUMENT and not its OUTPUTS. Determine whether
the eight-state chain is a second lifecycle of the same object, a lifecycle of
a different object (the record), or a category error in either direction.

## C12 — AUTHORITY-CLASS SEPARATION

Chain under attack:

```
INITIATION_AUTHORITY
!= EXECUTION_AUTHORITY
!= REVIEW_AUTHORITY
!= ADJUDICATION_AUTHORITY
!= RATIFICATION_AUTHORITY
```

Live specimens: this very cascade (Founder initiated; session 74633bfb
executed repairs; an independent projection reviewed; Founder disposes and
would ratify) and the round-1 refusal chain recorded in R1.

The reviewer must determine:

1. whether these are authority classes, roles, capabilities, or relations;
2. whether one actor may lawfully hold multiple classes, and under what
   declaration discipline;
3. which combinations create prohibited self-adjudication (e.g., EXECUTION +
   REVIEW over the same transition; REVIEW + RATIFICATION);
4. whether delegation is permitted per class, and whether delegated class
   membership narrows (PHILOSELF-002 §4 INV-3 analogue);
5. whether authority can be inherited — and whether chamber-boundary
   inheritance (003 §4 INV-1) reopens 002 §5 AMBIENT_INHERITANCE at the class
   level (round-1 MAT-7 regression check);
6. whether each authority terminates with the SELFPUTE it governs, survives
   it, or requires explicit termination;
7. which distinctions belong to PHILOSELF-002 (authority as such) versus
   PHILOSELF-005 (instrument eligibility) — and whether EXECUTION_DISCRETION
   (autonomous subordinate-operation selection inside an admitted SELFPUTE,
   "SELFauto") is reducible to these five classes or is an orthogonal type
   that some candidate must own.

## Return requirement

C11 and C12 verdicts are returned in the same discipline as packet-002 §4 item
4: each PASS | CHANGES_REQUIRED | BLOCKED, with the strongest constitutional
counterexample found or the reason none was constructible. Wording critique
without a failure scenario is at most minor. Neither chain may be treated as
ratified in the return; both may be refuted by it.
