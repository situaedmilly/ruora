# ADMISSION_INSTRUMENT_CONSTITUTING_GRANT_001 — DRAFT

```
STANDING: DRAFT_AWAITING_FOUNDER_ISSUANCE — this record has NO force. It is a
sovereign-record draft prepared under R6 (DRAFT_ONLY). Issuance is a Founder
act; nothing in this wave issues it. Until issued, the admission instrument's
constituting record (governance/PHILOSELF-ADMISSION-INSTRUMENT-CONSTITUTING-
RECORD-v0.1-CANDIDATE.md) remains grant_ref NONE_YET, lifecycle PROPOSED,
fail-closed per PHILOSELF-005 §4 INV-1.
```

## Grant (PHILOSELF-002 §3 shape)

```
grant_id:              ADMISSION_INSTRUMENT_CONSTITUTING_GRANT_001
source:                MILASOPHAHR (constituting authority — sovereign)
domain:                PHILOSELF chamber admission, RUORA estate
holder_effect:         constitutes ADMISSION-INSTRUMENT-001 (class ADMISSION);
                       the instrument holds NO authority — it operates under
                       THIS grant via constituting_grant_ref (002 §9 / M-3)
object_scope:          chambers and projections it does NOT occupy
permitted_transition:  chamber_boundary  UNDECLARED -> DECLARED (standing est.)
                       chamber           PROPOSED -> ADMISSION_PENDING -> ADMITTED
                       chamber           ACTIVE -> COMPROMISED (breach re-adjudication)
                       projection        DRAFT -> CONSTITUTED -> ADMITTED
                       child_context     classification + duplicate disposition
forbidden_transition:  ANY transition of a chamber/boundary the instrument is
                       AffectedByBoundary of (003 §4 INV-7 — prohibited
                       self-adjudication, disjointness required);
                       ANY REVIEW / REPAIR / ADJUDICATION / RATIFICATION-class
                       transition (explicitly: no review authority, no repair
                       authority, no ratification authority);
                       ANY standing elevation except through EvaluateProof
                       under an ACTIVE rule (005 §4 INV-8)
preconditions:         boundary claims classed per 003 INV-3; source bindings
                       by digest per 003 INV-5; every admission decision
                       evaluated under ACTIVE ProofRules covering the claim
                       types (proof-rule requirements — no ACTIVE rule for a
                       required claim type => ADMISSION: BLOCKED, never
                       narrated through)
expiration:            by named event: Founder revocation, or supersession by
                       a successor constituting grant
delegation:            NONE — non-delegable
accountability:        MILASOPHAHR as source; the instrument's records carry
                       grant_id + instrument identity + chamber binding
witness_requirement:   every admission act produces admission records
                       (invocation/result class where instrumented); lifecycle
                       states maintained by the constituting authority
```

Issuance form (for the Founder, when chosen): a signed issuance line naming
this grant_id, this draft's sha256, and the constituting record's sha256 —
recorded to governance and transported. Until then: NO FORCE.
