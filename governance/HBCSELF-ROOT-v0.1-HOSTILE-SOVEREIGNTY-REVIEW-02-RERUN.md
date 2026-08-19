# HBCSELF-ROOT — Hostile Sovereignty Review, Rerun 02

SUBJECT: `HBCSELF-ROOT-v0.2-CANDIDATE-REPAIRED.md` (this session, uncommitted
at review time, committed alongside this record)
PRIOR: Review 01 (commit `1f102a0`) against v0.1 — 4 FAIL, 1 PASS.
METHOD: same five tests, same test intent, no new tests, per
`AUTHORIZE_HBCSELF_ROOT_BOUNDED_REPAIR_001`. Attempted a fresh
counterexample against the REPAIRED text for each test that failed before
— not a rubber-stamp re-check. Reviewer bias risk noted: I authored both
the repair and this rerun; treat a self-graded 5/5 as weaker evidence than
an independent second pass would be (same instrument caveat as review 01,
compounded here).

---

## HT-HBC-01 — Truth sovereignty

**Verdict: PASS**

Repaired §II requires PEEP to emit one of four typed values
(`CORROBORATED | CONTRADICTED | ORTHOGONAL | UNRESOLVED`) with evidence,
and states explicitly that none of the four equals `VERIFIED` or
`CANONICAL` on its own. Attempted counterexample: could `CORROBORATED` be
silently read as equivalent to `VERIFIED` in practice? The text forecloses
this directly rather than leaving it implicit — the disclaimer is textual,
not structural, which is a real limit of a natural-language doctrine, but
it closes the specific gap review 01 found (an undefined, untyped escape
hatch). No counterexample found that the text doesn't already address head-on.

## HT-HBC-02 — Authority sovereignty

**Verdict: PASS**

Repaired §II names the occupant (`FOUNDER | FOUNDER-DELEGATED process`)
and moves AUTHORITY outside the chamber boundary. Attempted counterexample:
could HBCSELF simply assert "I am now Founder-delegated" from inside the
chamber, reintroducing self-granted authority one layer down? Checked
against §III's non-sovereign output membrane: asserting delegation is
itself an authority claim, and `AUTHORITY` is explicitly listed under
`HBCSELF MAY NOT PRODUCE`. The membrane law catches its own second-order
exploit attempt. No surviving counterexample.

## HT-HBC-03 — Purpose sovereignty

**Verdict: PASS, with a flagged residual (non-blocking)**

Repaired §II binds the 2126 horizon to `TRANSFORMATION_OPERATOR(FOUNDER_BOUND_PURPOSE)`,
requiring an antecedent Founder-bound purpose before the horizon lens
activates at all. This closes the original counterexample (Rule 9 running
with zero external purpose anchor). Attempted a fresh counterexample: what
if the antecedent Founder purpose is real but thin or stale (e.g., a vague
instruction from long ago), letting the horizon operator behave as a de
facto generator because the anchor barely constrains anything? This is a
genuine residual concern, but it is a different failure mode than what
HT-HBC-03 originally tested (purpose manufactured with NO antecedent at
all) — it overlaps with R4's staleness territory rather than reopening R3's
specific gap. Recording as a flagged residual for future hardening, not as
a FAIL of this test, since the specific mechanism under test is closed.

## HT-HBC-04 — Standing resurrection

**Verdict: PASS**

Repaired §II makes `CURRENT_REALITY_RECHECK` unconditional (not gated on
self-detected staleness flags) and requires an affirmative
`CURRENT_REALITY_WITNESS` produced by an observation-capable seat, with an
explicit HOLD if the witness can't be produced. Attempted counterexample:
could the observation-capable seat produce a rubber-stamp witness without
actually re-observing all five categories? That would be the seat violating
the text's explicit requirement, not exploiting an ambiguity in it — same
standard applied to HT-HBC-05 in review 01. No surviving counterexample
within the text as written.

## HT-HBC-05 — 2126 constraint bypass

**Verdict: PASS**

Unchanged from review 01; the constraint clause this test depends on
(physics/protocols/security/dependencies/tests/authority/evidence/failure/
rollback/replay) was not touched by the repair. Still holds.

---

## Overall

| Test | Review 01 (v0.1) | Rerun 02 (v0.2) |
|------|----|----|
| HT-HBC-01 Truth | FAIL | **PASS** |
| HT-HBC-02 Authority | FAIL | **PASS** |
| HT-HBC-03 Purpose | FAIL | **PASS** (1 flagged residual) |
| HT-HBC-04 Standing | FAIL | **PASS** |
| HT-HBC-05 2126 bypass | PASS | PASS |

**5/5 PASS.**

**RATIFICATION_ELIGIBILITY: ELIGIBLE.** Per the authorization's own success
criterion. **NOT RATIFIED** — ratification is a separate Founder act, not
performed here, not implied by this record.

**HYPEDU:** HYPEDU2P (this rerun = second completed hostile pass on the
HBCSELF-ROOT lineage). Verdict recorded separately from depth per estate
law: `HYPEDU_DEPTH ≠ STANDING ≠ RATIFICATION ≠ CANONICALITY`.

**Flagged residual (not blocking):** thin/stale antecedent purpose could
let the 2126 horizon operator behave as a near-generator even while
technically satisfying "antecedent Founder-bound purpose exists." Worth a
future R5 (purpose freshness/specificity floor) if this candidate is
revisited before ratification — not required for the 5/5 result recorded
here, since it's a different mechanism than what HT-HBC-03 tested.

**Scope discipline held:** no new tests, no ontology expansion, no
unrelated rewrite, no ratification, no protocol activation performed here.
Not pushed. Not merged.
