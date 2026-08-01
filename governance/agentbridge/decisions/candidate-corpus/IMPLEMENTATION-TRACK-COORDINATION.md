# IMPLEMENTATION TRACK COORDINATION
## Canonical Implementation-Track Map — Hardened AgentBridge v1

STATUS: AWAITING_FOUNDER_DISPOSITION
CLASSIFICATION: COORDINATION_ARTIFACT — not a workflow in the
  WORKFLOW-003–006 sequence; a distinct category, per this authorization's
  own framing.
EXECUTION_AUTHORITY: NONE
MUTATION_AUTHORITY: NONE — no runtime implementation, no governance edit,
  no renaming or renumbering of any existing file performed by this
  document.

DEPENDENCY: Reads `IMPLEMENTATION-READINESS-ASSESSMENT.md`,
  `IMPLEMENTATION-READINESS-WITNESS.md`, `07_LAUNCH_ROADMAP.md`,
  `GATE-3-HYPERBOLIC-CHAMBER-DESIGN-SPECIFICATION-0001.md`, and
  `WORKFLOW-001`/`WORKFLOW-002`'s specifications — all already read in
  full earlier in this continuous session. This document synthesizes and
  cross-references; it does not rediscover.

────────────────────────────────────────
1. CANONICAL IMPLEMENTATION TRACKS
────────────────────────────────────────
Exactly two implementation tracks exist in this corpus. Neither is
invented by this document — both are already self-declared in the
artifacts read:

**Track K (Kernel / Control-Plane).** Governed end-to-end by
`07_LAUNCH_ROADMAP.md`'s own "Current state" and "Open work, ordered"
sections. Milestone sequence: `LIMITED_SELFLAUNCH` → `FULL SELFLaunch`.
Gate identifiers use the `SL-00N` scheme (`SL-001` through `SL-008A`
completed; `SL-008B`, `SL-009L`, `SL-009` anticipated).

**Track C (Hyperbolic Chamber).** Governed by
`GATE-3-HYPERBOLIC-CHAMBER-DESIGN-SPECIFICATION-0001.md` (Design,
un-dispositioned) → `WORKFLOW-001-HYPERBOLIC-CHAMBER-RUNTIME-CONTRACT-
SPECIFICATION.md` (Design, ratified `FOUNDER-DISPOSITION-003`) →
`WORKFLOW-002-HYPERBOLIC-INVOCATION-CONTRACT-SPECIFICATION.md` (Design,
ratified `FOUNDER-DISPOSITION-004`) → an unmade binding decision → an
as-yet-unnamed next gate. Milestone: a bound, invoked chamber protocol
available to AgentBridge gates that opt into it.

A third, non-implementation track exists in this session's own output
(governance-lineage-and-authority-ratification: WORKFLOW-003 through
WORKFLOW-006, `FOUNDER-DISPOSITION-005`) — not itself an implementation
track, but the source of the naming collision analyzed in §5, and
included here only for that reason.

────────────────────────────────────────
2. OWNERSHIP OF EACH TRACK
────────────────────────────────────────
**Track K** is owned procedurally by `07_LAUNCH_ROADMAP.md` itself — the
document that is, by its own text, "the single authoritative, trailing
task list" for this track, regenerated only from sealed-gate records
(`04_GATE_EXECUTION.md`/`06_SEAL_OR_HOLD.md`). Its evidentiary anchor is
`runtime/agentbridge/governance/LIMITED_SELFLAUNCH_OPERATING_BOUNDARY.md`
(Founder-ratified 2026-07-26, predating the workflow stack entirely).

**Track C** is owned by the `GATE-3` → `WORKFLOW-00N` document lineage
in `decisions/candidate-corpus/`, each document individually disposed by
its own Founder Disposition Record in `decisions/ratified/` (or, for
Gate 3, not yet disposed at all — B4 in the readiness assessment).

Both tracks share the same procedural law once either is executed:
`04_GATE_EXECUTION.md`'s seven-stage lifecycle, `05_VERIFICATION.md`'s
cold-process standard, `06_SEAL_OR_HOLD.md`'s verdict set — all now
ratified by attestation (`FOUNDER-DISPOSITION-005`). Neither track owns
that procedural layer; both merely operate under it.

────────────────────────────────────────
3. SHARED DEPENDENCIES
────────────────────────────────────────
- **Procedural law**: both tracks execute under `workflow/00-07`
  (ratified, `FOUNDER-DISPOSITION-005`) — a shared dependency at the
  *how-to-execute-a-gate* level, not at the level of either track's own
  substantive content.
- **The Founder Disposition Record mechanism** as the sole terminal
  authorization act for either track — same format, same authentication
  standard, used identically by both.
- **Git-lineage status**: both tracks' governing documents sit in the
  same untracked `governance/` tree (GOV-LINEAGE-001, still parked) —
  a shared background condition, not a shared blocking dependency (per
  the readiness assessment's B1 finding: GOV-LINEAGE-001 blocks neither
  track's own stated requirements).

No shared *substantive* dependency was found — no document in Track K
cites Track C, or vice versa, for anything beyond the procedural layer
above.

────────────────────────────────────────
4. DIVERGENT DEPENDENCIES
────────────────────────────────────────
**Track K's** own dependency chain is entirely self-contained within
`07_LAUNCH_ROADMAP.md`'s ordered list (items 1–12) and its parallel
track (items 13–20: `SL-008B` test-command design, amendment, Founder
review, implementation, stabilization). None of these fifteen-plus items
reference Gate 3, `WORKFLOW-001`, or `WORKFLOW-002` anywhere.

**Track C's** own dependency chain runs: `FOUNDER-DISPOSITION-001`
(F-01/F-02/F-04) → `FOUNDER-DISPOSITION-002` (SR-EXEC-001) → Gate 3
(both dependencies satisfied, itself undispositioned — B4) →
`FOUNDER-DISPOSITION-003`/`-004` (Design-stage ratifications) → the
binding decision (B5, unmade) → the next gate (blocked additionally on
naming — B6). None of these reference any `SL-00N` item.

**Conclusion**: the two tracks' substantive dependency chains are fully
disjoint. A blocker in one track's chain has no bearing on the other's
readiness.

────────────────────────────────────────
5. NAMESPACE CONFLICTS
────────────────────────────────────────
Two distinct conflicts were found, not one — the readiness assessment's
B6 named the cross-track collision; this analysis additionally finds an
**intra-track** inconsistency that predates and compounds it:

**5a. Intra-Track-C inconsistency (new finding).** `GATE-3-...-0001.md`
§8 ("NEXT GATE (NOT THIS ONE)") names its own anticipated successor
explicitly: **"Gate 4+"** — continuing the `GATE-N` numbering Gate 3
itself established. `WORKFLOW-001-...-SPECIFICATION.md`, written after
Gate 3, does not use that numbering at all — it calls itself
"Workflow 001" and names its own successor "Workflow 002," a different
scheme, with no document anywhere bridging or reconciling the shift from
`GATE-N` to `WORKFLOW-00N`. `WORKFLOW-002-...-SPECIFICATION.md`
continues that second scheme, naming its own successor "WORKFLOW-003."
So: **within Track C alone**, two different, unreconciled naming schemes
already coexist (`GATE-4` per Gate 3's own text; `WORKFLOW-003` per
WORKFLOW-002's own text) for what should be the same next gate.

**5b. Cross-track collision (restated from the readiness assessment,
now precisely scoped).** `WORKFLOW-003` — the specific identifier
Track C's own text points to — is already the filename of this session's
`WORKFLOW-003-GOVERNANCE-LINEAGE-ESTABLISHMENT-SPECIFICATION.md`, an
unrelated, already-produced document. The collision does not stop at
`003`: were Track C's successor ever created and, hypothetically,
followed with a "WORKFLOW-004," "WORKFLOW-005," or "WORKFLOW-006," each
would also collide — those exact identifiers are already used by this
session's own governance-lineage track, and `WORKFLOW-005` specifically
is now the *named subject* of a sealed Founder Disposition
(`FOUNDER-DISPOSITION-005`). The entire `WORKFLOW-003`–`WORKFLOW-006`
range is exhausted by the other track.

────────────────────────────────────────
6. REQUIRED RENUMBERING OR RENAMING
────────────────────────────────────────
**Nothing already produced should be renamed.** Renaming
`WORKFLOW-003` through `WORKFLOW-006` (this session's governance-lineage
documents) would require editing already-ratified content — `FOUNDER-
DISPOSITION-005` names `WORKFLOW-005` by that exact identifier as its
disposition's own subject — and would reproduce exactly the kind of
retroactive rewrite this corpus's own discipline avoids. These files
keep their names.

**Track C's own, not-yet-created next gate should resolve 5a and 5b at
once, by reverting to Gate 3's own original numbering rather than
continuing WORKFLOW-002's.** Concretely: the gate that follows the
binding decision should be named in the **`GATE-N`** scheme Gate 3 itself
established (its own text already names this "Gate 4"), not
`WORKFLOW-003`. This is the smaller, lower-risk fix for three reasons:
nothing existing needs to change; it resolves the cross-track collision
(§5b) automatically, since `GATE-4` is not used anywhere else in this
corpus; and it resolves the intra-track inconsistency (§5a) by choosing
the *earlier, more-anchored* precedent (Gate 3's own explicit statement)
over the *later, less-anchored* one (WORKFLOW-002's own naming choice,
made without ever addressing Gate 3's prior "Gate 4+" statement).

Recommendation, precisely stated: **Track C's next gate should be titled
using the `GATE-N` scheme (e.g. `GATE-4-...`), not `WORKFLOW-00N`.**
This recommendation is itself not a renaming act — no file is touched by
this document — it is guidance for whoever authors that future,
not-yet-existing gate.

────────────────────────────────────────
7. EARLIEST LAWFUL IMPLEMENTATION AUTHORIZATION, PER TRACK
────────────────────────────────────────
**Track K**: per `03_GATE_SELECTION.md`'s own rule ("the next selectable
gate is the first item whose dependencies are all satisfied"), the
earliest lawful next act is `07_LAUNCH_ROADMAP.md`'s own item 1: "Persist
BCP-000001 through a separately authorized narrow mutation gate." This is
available now, independent of anything in Track C.

**Track C**: the earliest lawful *next* act is **not** implementation —
it is the binding decision itself (readiness assessment B5): an explicit,
unhedged, file-anchored Founder statement on whether AgentBridge invokes
the Hyperbolic Chamber, separate from and in addition to WORKFLOW-001/002's
own Design-stage dispositions, per both documents' own text. Only after
that decision, and after Gate 3 itself receives a disposition (B4), does
an actual *implementation-stage* gate become eligible — and per §6, that
gate should be named `GATE-4`, not continue the `WORKFLOW-00N` scheme.

────────────────────────────────────────
8. MAY EITHER TRACK PROCEED INDEPENDENTLY?
────────────────────────────────────────
**Yes — confirmed, not assumed.** §4 found the two tracks' substantive
dependency chains fully disjoint; §3 found their only shared dependency
is the procedural layer, already ratified for both. Track K's earliest
act (persist BCP-000001) does not require Track C's binding decision or
Gate 3's disposition, and vice versa. The namespace conflict in §5 is a
**documentation coordination risk**, not a **causal blocker** — it
constrains what Track C's *next artifact may be called*, not *whether or
when* either track may proceed. Each track may be authorized independently
of the other's current state.

────────────────────────────────────────
EXPLICITLY OUT OF SCOPE FOR THIS DOCUMENT
────────────────────────────────────────
No implementation of either track. No runtime change. No doctrine edit.
No renaming or renumbering of any existing file (§6 is guidance for a
future, not-yet-created document only). No Founder Disposition created.
