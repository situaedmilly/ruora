# OURSELF Reality Capability Grant — Q2/Q3 Disposition, Candidate 01

STATUS: CANDIDATE. Closes only the two blocking sub-questions from
`OURSELF-REALITY-CAPABLE-SEAT-IDENTITY-MECHANISM-CANDIDATE-01.md`
(commit `aeaec9e`) that prevent a first real `REALITY_CAPABILITY_GRANT`
from being issued for `ACT-0001`. No grant issued here. No HBCSELF
activation. No `ACT-0001`. Q4/Q5 remain deferred, untouched.

---

## Q2 — Evidentiary bar

**Proposal:** any claim used to satisfy `HBCSELF-ROOT-v0.2` §II's R4
(`CURRENT_REALITY_RECHECK` / `CURRENT_REALITY_WITNESS`) — i.e. anything
that gates executable `MORPHTATION` — carries a minimum assurance floor of
**TIER 2**, uniformly across R4's five categories. Not solving the general
N-tier system here; this is a narrow rule scoped to R4-gating claims only.

**TIER 2 requires:**

- **Primary measurement:** semantically valid for the proposition it
  claims to establish, observability scope established (per §3 below — an
  inline contract, not a claim of general capability), contamination
  risks checked.
- **Independent corroboration, when genuinely available:** a second
  observation that does not share the same failure mode as the first.
- **When no genuinely independent corroboration exists:** record
  `NO_INDEPENDENT_CORROBORATION_AVAILABLE` explicitly — do not treat
  primary-only evidence as sufficient by default — and require a Founder
  gate before the claim is used to satisfy R4.

**Independence test (added here — the proposal as commanded didn't define
"genuinely independent," and an undefined independence judgment is the
same shape of gap R4 already found once before in the self-diagnosed
staleness check):** two observations corroborate independently only if
they share **none** of the following:

1. the same underlying data source / state (e.g. the same on-disk index
   file, the same cached value);
2. the same instrument binary/library/code path;
3. the same unverified precondition (e.g. both trust the same clock, the
   same network path, the same unverified assumption).

If they share any of the three, treat the second observation as the first
one restated, not corroboration — file it as
`NO_INDEPENDENT_CORROBORATION_AVAILABLE`, not as a passed Tier 2 check.
Two shell commands both walking the same git object database do not
corroborate each other on "what does the repo contain"; `ps` cross-checked
against `lsof` (different kernel interfaces, different code paths) does —
this is not theoretical: a real instrument error (a `ps | grep gemini`
match on this estate's own shell) was caught exactly this way earlier in
this session's own work, and is the concrete precedent this bar is built on.

**Practical consequence, stated plainly rather than left implicit:** for a
single-session `ACT-0001`, true corroboration will often mean
different-instrument-same-seat (e.g. `git status` cross-checked by
`shasum` on the actual files, not two invocations of `git`), not
different-seat. Where even that isn't available,
`NO_INDEPENDENT_CORROBORATION_AVAILABLE` + Founder gate should be expected
as the common path for a first activation, not the exception.

**Preserved:**
```
CORROBORATION        ≠ REPETITION
CLAIM_CORRECTNESS     ≠ METHOD_VALIDITY
NO_COVERAGE             ≠ NO_CHANGE
```

## Q3 — Grant issuance ceremony

**Proposal:** a `REALITY_CAPABILITY_GRANT` is valid only when **all three**
hold:

1. `HARNESS_OR_TOOL_CONFIGURATION_FACT` — the seat's tool access for the
   surface is a fact about the runtime, not a claim.
2. `DEMONSTRATED_OBSERVATION_CAPABILITY` — at least one successful, logged
   invocation against a real observable target.
3. `EXPLICIT_FOUNDER_ISSUANCE` — a direct Founder act, same evidentiary bar
   as every other Founder act in this lineage (a direct answer to a direct
   question, identity-bound — not inferred from narrative, not
   assumed-accepted from a relayed recommendation).

**Preserved:**
```
CAPABILITY_CLAIM        ≠ CAPABILITY_GRANT
TOOL_CONFIGURED           ≠ CAPABILITY_DEMONSTRATED
CAPABILITY_DEMONSTRATED     ≠ CAPABILITY_GRANTED
SEAT_CANNOT_SELF_ISSUE_GRANT
HBCSELF_CANNOT_ISSUE_GRANT
```

**Batch issuance (added here — not in the original command, but needed to
avoid recreating the exact "blunt bureaucracy machine" Q2 was written to
avoid, applied now to Q3's ceremony overhead):** a single Founder issuance
act MAY cover multiple named surfaces for one named seat within one named
activation scope, in one act — e.g. "for ACT-0001's seat, I grant
FILESYSTEM + PROCESS + LOG" as one Founder decision — rather than requiring
a separate direct question per surface. This does not weaken condition 3;
it just avoids multiplying Founder interactions for what is, per-surface,
the same act performed once. Per-surface granularity is preserved in the
*grant record* (§2 of `aeaec9e` still requires each surface independently
justified); it is not required in the *ceremony*.

## Q1 — Minimal observability contract convention (for ACT-0001 only)

No registry. An inline contract carried directly in the grant record:

```
observability_contract_ref:
  type: INLINE_CONTRACT
  id: OBS-CONTRACT-ACT0001-01
  surface:                    <one of the typed surfaces>
  proposition_class:          <what kind of claim this instrument can support>
  instrument:                 <exact tool/command>
  instrument_semantics:       <what it actually reads and how>
  known_contamination_risks:  <e.g. "matches own process", "cached state">
  coverage_ceiling:           <what this instrument cannot see, explicitly>
```

Six fields, no more. This does not generalize past `ACT-0001` — a future
activation gets its own inline contract, or the estate can build a real
registry later if the pattern repeats enough to warrant one (Q4-adjacent,
still deferred).

## Q4, Q5 — unchanged, still deferred

Ledger/custody and surface-granularity-for-composites remain open,
untouched by this document, per the prior triage.

## Exact Founder decisions required (not made by this document)

1. Adopt (or amend) the Tier-2-minimum rule for R4-gating claims.
2. Adopt the independence test as stated, or replace it.
3. Adopt batch issuance for Q3 (one Founder act, multiple surfaces/one
   seat/one activation scope) versus requiring strictly per-grant,
   per-surface issuance.
4. Accept the 6-field inline observability contract as sufficient for
   `ACT-0001`, or require more.

## ACT-0001 blocking state after this document

Still **BLOCKED**. This document proposes dispositions for Q1-Q3; it does
not adopt them. No `REALITY_CAPABILITY_GRANT` becomes valid until the four
decisions above are made by explicit Founder act, and even then, `ACT-0001`
still separately needs `EXACT_SESSION_REF` and
`FOUNDER_PURPOSE_OR_MATTER_REF` resolved before it can exist as a valid
activation object per the activation contract's own 7-field schema.

---

TERMINAL_SUCCESS = Q2/Q3 proposals ready for Founder disposition.
NO_REAL_GRANT_ISSUED. No `ACT-0001`. No HBCSELF activation. No global
ledger built. No universal surface taxonomy built. Candidate not ratified.
Not pushed. Not merged.
