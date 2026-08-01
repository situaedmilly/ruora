# WORKFLOW-004 — FOUNDATIONAL WORKFLOW AUTHORITY ESTABLISHMENT
## Canonical Specification

STATUS: PARKED
CLASSIFICATION: GOVERNANCE_EVIDENCE_ITEM — authority lineage only
EXECUTION_AUTHORITY: NONE
MUTATION_AUTHORITY: NONE (no doctrine edit, no workflow/00-07 edit, no
  Founder disposition, no ratification act authorized by this document)
SCOPE: AUTHORITY_LINEAGE_ONLY — determines whether `workflow/00-07` already
  has constitutional authority; does not grant, withhold, or manufacture it.

DEPENDENCY: Produced under
  `WORKFLOW-003-GOVERNANCE-LINEAGE-ESTABLISHMENT-SPECIFICATION.md`'s own
  Gap C.2 finding ("`workflow/00-07`'s constitutional authority is
  DECLARED, not repository-evidenced"). This document does not restate
  C.2 — it investigates it to the depth WORKFLOW-003's bounded scope did
  not attempt.

────────────────────────────────────────
0. WHAT THIS DOCUMENT DOES AND DOES NOT DO
────────────────────────────────────────
Does: determine, by direct textual and evidentiary inspection of
`workflow/00-07` themselves plus the Founder Disposition records and
lineage records those files reference or that reference them, whether an
existing ratified chain already covers this stack; if not, name the
smallest lawful ratification mechanism; determine whether retrospective
ratification is lawful under this corpus's own established practice;
determine whether replacement (vs. ratification) is indicated; determine
whether FOUNDER-DISPOSITION-001 through -004 remain valid regardless of
the answer; produce one canonical recommendation.

Does not: ratify `workflow/00-07`. Does not create a Founder Disposition
Record. Does not edit any of the 8 workflow files, any doctrine file, or
any schema. Does not address the three stale-status-header findings
(schema, WORKFLOW-001 spec, WORKFLOW-002 spec) named in
`WORKFLOW-003-...-SPECIFICATION.md` C.3/C.4 — the calling instruction for
this workflow explicitly excludes them, on the grounds that they are a
separate maintenance concern from the authority-chain question this
document addresses. Does not perform runtime inspection or AgentBridge
routing.

Method, stated per this corpus's own evidence-classification vocabulary
(VERIFIED / DECLARED / UNKNOWN, established in
`FOUNDER-RATIFICATION-001-...-PACKET.md` §Evidence Classification): every
claim below is VERIFIED by direct read of the cited file this session,
unless marked otherwise.

────────────────────────────────────────
A. DOES `workflow/00-07` ALREADY POSSESS CONSTITUTIONAL AUTHORITY THROUGH AN EXISTING RATIFIED CHAIN?
────────────────────────────────────────
**Finding: NO — not as a document set. A real, ratified precedent exists,
but its own stated scope does not name `workflow/00-07` as its subject.**

Evidence, read in full this session:

1. **`04_GATE_EXECUTION.md` line 10** cites its own grounding directly:
   "Execute exactly the one gate named by `03_GATE_SELECTION.md`, using
   the lifecycle proven by **SL-008A**." This is not a vague appeal to
   authority — it names a specific, checkable prior proof chain.

2. **`07_LAUNCH_ROADMAP.md`'s own "Current state (as of this scaffold's
   creation)" section**, under "Completed," lists — as facts already true
   at the moment this roadmap document was written — "SL-008A bounded
   git-add implementation," "SL-008A operational stabilization,"
   "**LIMITED_SELFLAUNCH Founder ratification**," and "**LIMITED_SELFLAUNCH
   operating-boundary publication**."

3. Cross-referencing item 2 against `runtime/agentbridge/governance/
   LIMITED_SELFLAUNCH_OPERATING_BOUNDARY.md` (read in full this session):
   that document **is** a genuine, ratified constitutional artifact —
   "Published at (UTC): 2026-07-26T17:52:32Z," "Ratified by: Founder
   decision — `OURSELF_SYNCHRONIZED_FOUNDER_DECISION`
   (`DECISION_SIGNAL`/`DESIGN_SIGNAL`/`SYNTHESIS_SIGNAL`), decided_by
   MYSELF, attribution Philosopher Milly (Human_TURN)," with a named
   evidence-basis table (5 proof chains, PC-000001–PC-000005) and a
   verified kernel HEAD/regression-suite state at ratification. This is
   the single document anywhere in the governance corpus (per
   WORKFLOW-003's own inventory) carrying an actual named decision-signal
   and Founder attribution, rather than a bare self-declared status
   string.

4. **Chronology matters here.** The boundary document was published
   2026-07-26T17:52:32Z. `workflow/00_MANIFEST.md` (the earliest file in
   the 8-file stack) was authored 2026-07-27 19:33:57 — **the next day**.
   The workflow stack was therefore authored *after*, and in explicit
   reference to, an already-ratified decision — not concurrently with an
   independent ratification act of its own.

5. **The boundary document's own stated scope excludes the workflow
   stack.** Its "Governs:" line states explicitly: "OURSELF AgentBridge
   kernel (`/Users/millysituated/RUORA/projects/agent-bridge`) and
   control-plane (`/Users/millysituated/RUORA/systems/ourself-agent-
   bridge`)." It does not name `governance/agentbridge/workflow/`. Its
   "Required execution path" references `tools/proof-path-driver.js` — a
   kernel-side artifact, not a governance-markdown artifact. The
   ratification is real; its scope, by its own words, is the kernel and
   control-plane, not the 8 workflow documents that later describe and
   build on it.

6. **`07_LAUNCH_ROADMAP.md` line 25–27 states, of itself, exactly the
   distinction this finding turns on**: "This document does not ratify
   constitutions. Ratification status shown here reflects decisions made
   elsewhere (Founder ratification, sealed gates) — it is a record, not
   the mechanism of ratification." The roadmap is explicit that it is
   reporting a ratification, not performing one. For `SL-008A`/
   `LIMITED_SELFLAUNCH`, a real "elsewhere" exists (item 3). For the
   8-file scaffold itself, no equivalent "elsewhere" record exists
   anywhere in `decisions/ratified/` — confirmed by WORKFLOW-003's own
   inventory (A.2): the ratified directory's first-ever occupant,
   `FOUNDER-DISPOSITION-001`, was created 2026-07-29, two days later, on
   an unrelated subject (SELFREALIZATION F-01/F-02/F-04), and none of the
   four existing Founder Dispositions name or ratify `workflow/00-07`
   itself — each treats `04_GATE_EXECUTION.md`/`05_VERIFICATION.md`/
   `06_SEAL_OR_HOLD.md` as pre-existing read-only reference material
   (confirmed by direct re-citation: FOUNDER-DISPOSITION-003's evidence
   basis records "`04_GATE_EXECUTION.md` mtime unchanged (read-only
   reference)").

7. **The stack's own trailing roadmap does not describe itself as
   finished, let alone ratified, at time of creation.**
   `07_LAUNCH_ROADMAP.md`'s "Trailing tasks until launch" list's first,
   unchecked item is literally: "`- [ ] Complete the eight-file workflow
   scaffold`," immediately followed by "`- [ ] Verify scope and full RUORA
   working-tree state`" and "`- [ ] Run a fresh-session workflow recovery
   test`" — also unchecked. This is the stack's own internal accounting,
   at the moment of its own authorship, treating its own completion and
   verification as open work — which sits uneasily beside every one of
   the 8 files' header line unconditionally declaring `Status:
   FOUNDER_AUTHORIZED_OPERATIONAL_WORKFLOW`.

**Conclusion for A**: A real, ratified Founder decision exists upstream
(`LIMITED_SELFLAUNCH`/SL-008A) and the workflow stack's content is a
faithful, well-grounded formalization of the process that decision
proved out — this is not a fabricated or ungrounded claim of authority.
But the ratification's own stated scope does not extend to the 8 workflow
documents as governance artifacts, no separate ratification event covers
them, and the stack's own roadmap output lists its own completion as
pending at time of writing. The self-declared `FOUNDER_AUTHORIZED_
OPERATIONAL_WORKFLOW` status is best classified, in this corpus's own
vocabulary, as **DECLARED** (asserted, well-grounded in real prior events,
consistently relied upon since) but **not VERIFIED** against a
repository-resident ratification record naming these files as its
subject.

────────────────────────────────────────
B. SMALLEST LAWFUL RATIFICATION MECHANISM
────────────────────────────────────────
The corpus already contains the exact mechanism needed; it has simply never
been pointed at itself:

1. **Gate class**: `04_GATE_EXECUTION.md`'s own **Decision-only gate**
   template — "Input: a question requiring a Founder/human decision.
   Allowed: present options, tradeoffs, and a recommendation. Forbidden:
   implementing any option before the decision is made." This finding
   *is* such a question.

2. **Record format**: a `FOUNDER-DISPOSITION-00N-WORKFLOW-STACK-WITNESS.md`
   in `decisions/ratified/`, in the exact structural format
   FOUNDER-DISPOSITION-001 through -004 already established (Identity /
   Exact Scope / Ratified Behavior / Evidence Basis / Exclusions /
   Authentication Disclosure) — reusing the existing template rather than
   inventing a new one, consistent with this corpus's own repeated
   practice of reuse over invention (WORKFLOW-001 §A, WORKFLOW-002 §0).

3. **Content required for that future gate to produce a sound record**:
   cite this document's A.1–A.7 findings as its evidence basis; name the
   8 files exactly; record their current hashes (below, F) as the content
   being ratified; state explicitly (per GOV-LINEAGE-001's own established
   pattern) that this ratifies file content, not a Git-anchored revision,
   since no Git history exists for this tree either.

No new organ, template, or process needs to be invented. The smallest
lawful mechanism is: run the Decision-only gate this stack already
defines, using the record format this stack's own Founder Dispositions
already use, targeted at the stack itself.

────────────────────────────────────────
C. IS RETROSPECTIVE RATIFICATION LAWFUL?
────────────────────────────────────────
**Finding: YES, under this corpus's own already-established practice —
with one disclosed caveat.**

`LINEAGE-DEFECT-PATTERN-DEFINITION.md` (read in full under WORKFLOW-003,
re-cited here as a lineage record directly on point, not re-read fresh) 
names exactly this shape of correction: "Correction: Create a
repository-resident Lineage Record without changing constitutional
meaning — no redesign, no added requirements, no scope expansion, no
implementation. The correction is transcription, not engineering." A
Founder ratification of already-operating, already-relied-upon content is
the same shape: it does not change what the 8 files say, only whether a
ratification record exists attesting to it.

Direct precedent already exists in this corpus for ratifying content that
predates the disposition act itself: **FOUNDER-DISPOSITION-001** ratified
the F-01/F-02/F-04 repair inside `03_SELFREALIZATION_SCHEMA.yaml`, and that
repair's file mtime (2026-07-28) predates the disposition (2026-07-29) —
the Founder disposition record itself states this plainly: "the ratifying
packet's own evidentiary content was not in question... F-01 and F-02 were
VERIFIED with no residual gap." Retrospective ratification of pre-existing,
verified content is not a novel or irregular act in this corpus; it is
already how this corpus's most load-bearing ratification was performed.

Caveat, disclosed rather than hidden: as with GOV-LINEAGE-001's own
finding, `workflow/00-07` has no Git history, so any future ratification
of it — like FOUNDER-DISPOSITION-001 through -004 before it — certifies
file content and hash at time of ratification, not a Git-anchored
revision. This is not a defect specific to retrospective ratification; it
is the same evidentiary ceiling every ratification in this corpus
operates under, restated here rather than treated as a new problem.

────────────────────────────────────────
D. IS REPLACEMENT REQUIRED?
────────────────────────────────────────
**Finding: NO.**

No content defect was found in `workflow/00-07` during this session's full
read of all 8 files. To the contrary:
- Every one of FOUNDER-DISPOSITION-001 through -004 relies on and reuses
  this stack's vocabulary (the eight-verdict set, cold-process
  verification, the epistemic pipeline, `PROPOSITION_INFLATION`) without
  ever finding fault with it or proposing an alternative.
- `WORKFLOW-001`/`WORKFLOW-002`'s own specifications explicitly build on
  `04_GATE_EXECUTION.md`'s lifecycle rule ("No stage implies the next")
  as settled, sound doctrine.
- The internal cross-references within the 8 files themselves are
  consistent (each document's "Required inputs" matches the prior
  document's "Required output"; the launch-state footer convention is
  applied uniformly across all 8).
- Per C above and the Lineage Defect pattern, the correction indicated is
  transcription/ratification, not redesign. Replacement would be a strictly
  larger, riskier act than the defect (a missing ratification record)
  actually calls for.

────────────────────────────────────────
E. DO CURRENT DOWNSTREAM DISPOSITIONS REMAIN VALID?
────────────────────────────────────────
**Finding: YES — FOUNDER-DISPOSITION-001 through -004 remain valid Founder
decisions, and this finding does not retroactively ratify `workflow/00-07`
by association.**

Each of the four existing Founder Dispositions' own "Authentication
Disclosure"/"Authentication basis" section grounds its validity in a
direct, first-person, unhedged statement by the Founder in the
controlling conversation transcript — not in the ratification status of
the vocabulary or process framework the statement was expressed through.
FOUNDER-DISPOSITION-001: "an explicit, first-person, unambiguous statement
of disposition, made by the human party in this session." 
FOUNDER-DISPOSITION-002 through -004: the same standard, explicitly
disclosed as "not claimed to be stronger" each time. A Founder decision is
valid because the Founder decided it; the terms it was decided in
(`SEALED`, `READY_FOR_FOUNDER_RATIFICATION_REVIEW`, the epistemic pipeline)
are descriptive vocabulary the decision was expressed through, not a
precondition of the decision's own validity.

The caveat stated deliberately, to avoid the exact scope-inflation this
corpus's evidence discipline exists to prevent (per FOUNDER-DISPOSITION-
001's own precedent language): this finding does not mean `workflow/00-07`
is therefore also ratified merely because decisions expressed in its
vocabulary are valid. That would be reasoning backward from effect to
cause and is exactly the kind of inference this document's Objective A
was tasked with checking directly, not assuming. The four dispositions'
validity and `workflow/00-07`'s own ratification status are independent
facts; this document finds the first true and the second not yet
established, without either implying the other.

────────────────────────────────────────
F. CANONICAL AUTHORITY RECOMMENDATION
────────────────────────────────────────
Run one bounded Decision-only gate (per B) that presents the Founder with
exactly the finding in A: `workflow/00-07` is a faithful, well-grounded
formalization of an already-ratified prior decision (`LIMITED_SELFLAUNCH`/
SL-008A), consistently relied upon by four subsequent, independently valid
Founder Dispositions (E), containing no identified content defect (D), and
lawfully eligible for retrospective ratification under this corpus's own
established practice (C) — but not, as of this inventory, itself the
subject of any ratification record.

The recommended disposition path for that future gate: **ratify by
attestation**, not rewrite — produce a `FOUNDER-DISPOSITION-00N-
WORKFLOW-STACK-WITNESS.md` recording the Founder's direct decision on the
8 files as currently written (hashes below), using the existing
Decision-only gate template and Founder Disposition Record format, with
the same disclosed Git-lineage caveat every prior disposition already
carries.

This document does not run that gate. Per WORKFLOW-004's own scope, it
stops at the recommendation.

────────────────────────────────────────
G. CURRENT FILE HASHES (for the future ratifying gate's own evidence basis)
────────────────────────────────────────
Recorded fresh this session, `shasum -a 256`:
```
00_MANIFEST.md            <recorded in accompanying Engineering Witness>
01_SESSION_BOOTSTRAP.md   <recorded in accompanying Engineering Witness>
02_SYNCHRONIZATION.md     <recorded in accompanying Engineering Witness>
03_GATE_SELECTION.md      <recorded in accompanying Engineering Witness>
04_GATE_EXECUTION.md      <recorded in accompanying Engineering Witness>
05_VERIFICATION.md        <recorded in accompanying Engineering Witness>
06_SEAL_OR_HOLD.md        <recorded in accompanying Engineering Witness>
07_LAUNCH_ROADMAP.md      <recorded in accompanying Engineering Witness>
```
Full hash values are recorded once, in
`WORKFLOW-004-ENGINEERING-WITNESS.md`, to avoid duplicating an evidence
table across two documents.

────────────────────────────────────────
EXPLICITLY OUT OF SCOPE FOR THIS DOCUMENT
────────────────────────────────────────
No ratification performed. No Founder Disposition created. No edit to any
of the 8 workflow files. No doctrine edit. No runtime implementation. No
AgentBridge routing. No schema change. No treatment of the three
stale-status-header findings from `WORKFLOW-003-...-SPECIFICATION.md`
C.3/C.4 — excluded per this workflow's own calling instruction, to keep
the authority question and the header-maintenance question in separate,
single-purpose gates.
