# HBCSELF-ROOT-v0.2 Activation Contract — Ratification 001

SUBJECT: `governance/HBCSELF-ROOT-v0.2-ACTIVATION-CONTRACT-CANDIDATE-01.md`,
commit `597c38a`.
ACT: Founder ratification of the activation contract, plus resolution of
one of its four open questions.
FOUNDER: Milasophahr (session identity `vsafetyalliance@gmail.com`),
acting directly — two direct answers to two direct questions, same
evidentiary bar as `HBCSELF-ROOT-v0.2-RATIFICATION-001.md`.
DATE: 2026-08-19.
CAUSAL PARENT: `f7c2aa9` (HBCSELF-ROOT-v0.2 ratification) →
`597c38a` (activation contract candidate 01).

## What this ratifies

The semantic content of `HBCSELF-ROOT-v0.2-ACTIVATION-CONTRACT-CANDIDATE-01.md`
as of commit `597c38a`, unmodified: the three-object ontology
(ROOT/ACTIVATION/SESSION_PROJECTION), the 7-field fail-closed activation
schema, the 3-state activation state machine, the additive authority
ceiling (`HBCSELF_CANNOT_SELF_RATIFY`, `HBCSELF_CANNOT_SELF_ACTIVATE`), and
the termination-condition definitions.

## Open Question 2 — RESOLVED

Candidate document §7.2 asked whether root supersession should
auto-terminate all activations, or use a finer invalidation classifier.

**Resolution:** YES — fail-closed. Any new ratified version of
`HBCSELF-ROOT` automatically terminates every activation bound to the
prior `EXACT_ROOT_REF`, unconditionally. No dependency-sensitive
classification of which changes are "invalidating." Re-activation under a
new root always requires a fresh activation object.

This is now binding on the contract, not merely a proposed default.

## Open Questions 1, 3, 4 — explicitly NOT resolved by this ratification

- Reality-capable-seat identity mechanism (§7.1)
- Concurrent-activation coordination (§7.3)
- Activation-object custody location (§7.4)

These were triaged as implementation Matter, not semantic-soundness
blockers, and that triage is accepted here: ratifying the contract's
structure does not require settling them first. They remain open and
should be resolved before any real `ACT-0001` is created, not before this
ratification.

## What this does NOT do

`RATIFICATION ≠ ACTIVATION`, holding one more time:

- **No activation object is created by this record.**
  `HBCSELF_ACTIVE_SESSIONS = 0` after this ratification, exactly as before it.
- No `ACT-0001` exists. No session is projecting HBCSELF's semantics.
- Open Questions 1, 3, 4 remain open — creating a real activation later
  will need at least Open Question 1 (reality-capable-seat identity)
  settled first, since the contract's own R4-derived requirement depends
  on it being answerable.
- No merge to main. No change to `HBCSELF-ROOT-v0.2` itself.

## Standing

| Object | Standing |
|---|---|
| `HBCSELF-ROOT-v0.2` (`f7c2aa9`) | RATIFIED (unchanged) |
| `HBCSELF-ROOT-v0.2-ACTIVATION-CONTRACT-CANDIDATE-01` (`597c38a`) | **RATIFIED** |
| Root-supersession termination policy | SETTLED — fail-closed, terminate all |
| Reality-capable-seat identity mechanism | OPEN |
| Concurrent-activation coordination | OPEN |
| Activation-ledger custody location | OPEN |
| Any `HBCSELF_ACTIVATION` object | NONE EXIST |
| `HBCSELF_SESSION_PROJECTION` | NONE — no session is running under HBCSELF |

STOP.
