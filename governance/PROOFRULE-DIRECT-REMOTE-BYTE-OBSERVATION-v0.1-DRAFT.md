# ProofRule — direct_remote_byte_observation (DRAFT)

```
STATUS: DRAFT — NOT REGISTERED, NOT ACTIVE. Drafted under
FOUNDER_AUTHORIZE_PHILOSELF_R1_R5_REPAIR_WAVE_001 §R2 (draft-only).
EvaluateProof MUST reject this rule (PHILOSELF-005 §4 INV-8 fail-closed:
status != ACTIVE). Activation requires the Founder adjudication act drafted
at PROOFRULE_ACTIVATION_DIRECT_REMOTE_BYTE_OBSERVATION_001 — NOT ISSUED.
```

## ProofRule record (PHILOSELF-005 §6 schema)

```
rule_id:                    direct_remote_byte_observation
claim_type:                 REMOTE_SURFACE_RETURNED_BYTES
supported_proposition:      "Receiver R observed surface S return byte
                            sequence B with digest D at time t."
admissible_witness_types:   tool invocation record + corresponding tool result
                            record (producer-typed, PHILOSELF-005 §2/INV-3) +
                            digest recomputation over the returned bytes
admissible_source_types:    remote content surface addressed by immutable
                            reference (commit-pinned path preferred; a branch
                            ref is a mutable address and weakens the claim's
                            time-indexing, never its byte content)
chamber_requirements:       evaluating chamber must bind R, S, t and the
                            invocation records inside its own EVIDENCE
                            BOUNDARY; the receiver R is the chamber's occupant
                            for the observation and may DISCLOSE it — standing
                            is established only by evaluation under this rule
                            once ACTIVE (INV-RC-ADMISSION-001 preserved)
supported_scope:            the returned-bytes proposition ONLY, indexed by
                            (record, receiver, surface, t) —
                            Resolvable(record, receiver, surface, t)
standing_ceiling:           STRONG for the returned-bytes proposition
failure_conditions:         digest mismatch; missing invocation or result
                            record; surface unaddressed; time unstamped;
                            witness records declaration-class only
author:                     session 74633bfb (CLAUDESELF) — author is NOT
                            activator (RULE_AUTHOR != RULE_ACTIVATOR_BY_DEFAULT)
registration_record:        NONE — not yet registered
activation_authority:       domain-scoped ADJUDICATION_AUTHORITY (PHILOSELF-002
                            §6), holder MILASOPHAHR
activation_grant_ref:       NONE — see draft activation record, NOT ISSUED
status:                     DRAFT
activated_at:               —
expires_at:                 by named event, per activation grant when issued
supersedes:                 nothing
provenance:                 distilled from this estate's live practice
                            (GitHub-byte digest recomputation, receiver-side
                            verification discipline, transport receipts)
```

## Explicitly unsupported propositions

This rule establishes NOTHING about: canonicity; ratification; semantic
correctness; authorship; originality; authority; absence on other surfaces;
persistence across time. Each of those is a different claim type under a
different rule that does not yet exist.

## Bound specimen — the API race (surface-indexing is load-bearing)

Live specimen, 2026-08-15: after channel push `798af1c`, the GitHub contents
surface served the new pointer while the commits surface served the prior
head — same record, same receiver, same instant, two surfaces, two truth
values. Therefore:

```
REMOTE_COMMIT_EXISTS
  != Resolvable(record, receiver, contents_surface, t)
  != Resolvable(record, receiver, commits_surface, t)
```

A claim evaluated under this rule is indexed to the SURFACE that returned the
bytes, never to "the remote" as an undifferentiated object.
