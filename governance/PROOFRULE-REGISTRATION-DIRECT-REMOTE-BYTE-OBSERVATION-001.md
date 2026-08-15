# ProofRule Registration — direct_remote_byte_observation (REGISTERED)

```
registration_record:      PROOFRULE_REGISTRATION_DIRECT_REMOTE_BYTE_OBSERVATION_001
registered_at:            2026-08-15T20:51:05Z
act_class:                REGISTRY CUSTODY ONLY — registration confers NO
                          standing-producing authority (REGISTERED_RULE !=
                          ACTIVE_RULE; REGISTRY_CUSTODY != RULE_AUTHORITY)
rule_id:                  direct_remote_byte_observation
rule_version:             v0.1
rule_sha256:              b02f91e6ab3a768f2c5a5f7c43786dee41e9f0126da23fc3229719717cde81d0
                          (governance/PROOFRULE-DIRECT-REMOTE-BYTE-OBSERVATION-v0.1-DRAFT.md,
                          commit-pinned 68481ac, GitHub-byte verified)
claim_type:               REMOTE_SURFACE_RETURNED_BYTES
admissible_witness_types: tool invocation record + corresponding tool result
                          record + digest recomputation over returned bytes
admissible_source_types:  remote content surface addressed by immutable
                          (commit-pinned) reference
chamber_requirements:     evaluating chamber binds R, S, t and invocation
                          records inside its EVIDENCE BOUNDARY; occupant may
                          disclose, never establish
supported_scope:          the returned-bytes proposition only —
                          Resolvable(record, receiver, surface, t)
standing_ceiling:         STRONG for the returned-bytes proposition
failure_conditions:       digest mismatch; missing invocation/result record;
                          surface unaddressed; time unstamped;
                          declaration-class-only witnesses
author:                   session 74633bfb (author != activator by default)
provenance:               distilled from live estate practice (GitHub-byte
                          recomputation, receiver-side verification discipline)
status:                   REGISTERED
record_identity:          NO self-digest (SELF_DIGEST_PARADOX law); identity =
                          external custody binding
```

## Explicitly unsupported (the rule establishes NONE of these)

Canonicity; ratification; constitutional correctness; semantic correctness;
authorship; originality; general authority; persistence across time; absence
on another receiver surface; **equivalence between repository existence and
receiver resolution**.

## Bound relation and specimen

`Resolvable(record, receiver, surface, t)` — four-place, surface-indexed.
API-race specimen preserved:

```
REMOTE_COMMIT_EXISTS
  != Resolvable(record, receiver, contents_surface, t)
  != Resolvable(record, receiver, commits_surface, t)
```

## Post-registration state

```
PROOFRULE: REGISTERED_NOT_ACTIVE
```
