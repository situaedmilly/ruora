# ADMISSION_INSTRUMENT_CONSTITUTING_GRANT_001 — ISSUED

```
grant_id:                     ADMISSION_INSTRUMENT_CONSTITUTING_GRANT_001
grant_type:                   ADMISSION_INSTRUMENT_CONSTITUTING_GRANT
issuer:                       MILASOPHAHR (sovereign act, executed by CLAUDESELF
                              session 74633bfb under
                              FOUNDER_ISSUE_PHILOSELF_SOVEREIGN_RECORDS_001 §1)
authority_class:              ADMISSION_AUTHORITY
issued_at:                    2026-08-15T20:51:05Z
standing:                     ISSUED — the instrument is thereby
                              CONSTITUTED_NOT_EXECUTED
draft_path:                   governance/ADMISSION-INSTRUMENT-CONSTITUTING-GRANT-001-DRAFT.md
draft_sha256:                 489891743bfd528c541fb9e1a4488e6728ae97a21a811f8d70be8cdc0d494140
constituting_record_path:     governance/PHILOSELF-ADMISSION-INSTRUMENT-CONSTITUTING-RECORD-v0.1-CANDIDATE.md
constituting_record_sha256:   307dbb4e1ae60cef981fae99f111732d25c78ff440e8a07f8cb7ba90b479b57f
pre_issuance_resolution:      commit-pinned 68481acbf0d2b264597ba585dbc0c3f4b52d2b72,
                              GitHub-byte verified, ZERO DRIFT
instrument_identity:          ADMISSION-INSTRUMENT-001, v0.1
instrument_type:              ADMISSION (PHILOSELF-005 §6 class)
record_identity:              this record carries NO self-digest (Founder patch
                              1: SELF_DIGEST_PARADOX law — a record never
                              contains its own whole-file hash; identity =
                              external custody binding, digest computed after
                              serialization, held by custody commit +
                              INSELFACTION)
```

## Authorized chamber scope / boundary classes

Chambers and projections the instrument does NOT occupy. Boundary classes it
may evaluate: all ten PHILOSELF-003 §3 dimensions — for chambers where, per
`AffectedByBoundary(x, B)`, it is not itself boundary-affected.

**AffectedByBoundary separation rule (binding):**
`AffectedByBoundary(x, B) ⇒ x cannot be sole adjudicator of Standing(B)`. The
instrument must not establish any boundary for which it is itself the sole
boundary-affected adjudicator (PHILOSELF-003 §4 INV-7).

## Allowed operations

- evaluate declared chamber-entry claims;
- consume ACTIVE ProofRules within their activation scope;
- produce ADMISSION EVALUATION RECORDS;
- return ADMITTED, BLOCKED, or INDETERMINATE as constitutionally specified.

## Forbidden operations

No hostile review. No corpus repair. No expansion of this grant. No ProofRule
activation. No adjudication of its own constitution. No ratification. No seal.
No PHILOSELF commencement. No X1 mutation. No AgentBridge or SELFQUEUE
implementation.

## Proof-rule requirements

Every admission decision is evaluated under ACTIVE ProofRules covering the
claim types; a required claim type with no ACTIVE rule ⇒ ADMISSION: BLOCKED,
never narrated through (PHILOSELF-005 §4 INV-8 fail-closed).

## Non-collapse (binding)

```
ADMISSION_AUTHORITY          != REVIEW_AUTHORITY
ADMISSION_AUTHORITY          != ADJUDICATION_AUTHORITY
ADMISSION_INSTRUMENT         != REVIEWER
ADMISSION_INSTRUMENT         != RATIFIER
ADMISSION_RESULT             != REVIEW_VERDICT
ADMISSION_PASS               != CONSTITUTIONAL_VALIDITY
ADMISSION_INSTRUMENT_OUTPUT  != ADMISSION_STANDING   (Founder patch 2)
```

**Elevation chain (Founder patch 2, binding):** the instrument's output is an
ADMISSION EVALUATION RECORD, never standing itself. Standing arises only
through the full chain:

```
ADMISSION INSTRUMENT -> ADMISSION EVALUATION RECORD
  -> EvaluateProof(w, c, r, χ) under an ACTIVE rule -> BOUNDED STANDING
```

The instrument cannot self-elevate its own output; "the instrument produced
it" is never a standing shortcut.

## Expiry / revocation / accountability

Expiry by named event: Founder revocation or supersession by successor grant.
Revocation: MILASOPHAHR at will; propagates to the instrument's lifecycle
(REVOKED) with no gap (PHILOSELF-005 §6). Delegation: NONE. Accountability:
MILASOPHAHR as source; every instrument record carries grant_id + instrument
identity + chamber binding.

## Post-issuance state

```
R6_ADMISSION_GRANT:   ISSUED
ADMISSION_INSTRUMENT: CONSTITUTED_NOT_EXECUTED
CHAMBER_REALIZATION:  NOT_RUN (frozen — outside this authority)
```
