# PHILOSELF Admission Instrument — Worked Constituting Record (Candidate)

```
STATUS:              CANDIDATE CONSTITUTING RECORD — the instrument is
                     UNCONSTITUTED: lifecycle PROPOSED, fail-closed per
                     PHILOSELF-005 §4 INV-1 (no grant yet cited)
PURPOSE:             Sequence step C (ADMISSION REALIZATION) — demonstrate that
                     an ADMISSION instrument is now SPECIFIABLE from the
                     repaired corpus alone, which round-2's end question found
                     impossible pre-repair ("three concepts must be invented:
                     a chamber lifecycle, a projection lifecycle, and an
                     expiry-event vocabulary" — all three now exist)
AUTHORED_UNDER:      Founder-hardened A-I repair authority, step C
IMPLEMENTATION:      NOT_AUTHORIZED — this is a paper constitution of an
                     instrument, not code, not a running mechanism
RATIFICATION:        NOT_GRANTED
```

## Constituting record (PHILOSELF-005 §3, all twelve fields)

```
INSTRUMENT
├── identity/type                ADMISSION-INSTRUMENT-001, v0.1 (class: ADMISSION)
├── constituting_grant_ref       NONE_YET — requires a Founder-issued
│                                PHILOSELF-002 §3 grant id. Until cited:
│                                lifecycle PROPOSED, no operation lawful,
│                                outputs carry record class only (INV-1).
│                                Required grant shape:
│                                  MAY CAUSE: chamber_boundary
│                                    UNDECLARED -> DECLARED (Standing established)
│                                  MAY CAUSE: chamber
│                                    PROPOSED -> ADMISSION_PENDING -> ADMITTED
│                                  MAY CAUSE: projection
│                                    DRAFT -> CONSTITUTED -> ADMITTED
│                                  MAY NOT CAUSE: any transition of a chamber
│                                    of which this instrument is an occupant
├── chamber                      declared per instantiation; DISJOINT from any
│                                chamber it adjudicates — as an occupant
│                                (003 §3 definition) it is barred by
│                                INV-ADMISSION-SEPARATION-001 (003 §4 INV-7)
│                                from establishing standing for boundaries it
│                                is AffectedByBoundary of
├── capability                   substrate-indexed: read paths, compute sha256,
│                                read process/session records, write its own
│                                admission records to its declared record path
├── authorized_operation_class   chamber-boundary declaration; chamber
│                                admission (PROPOSED->ADMITTED); projection
│                                admission (DRAFT->ADMITTED); duplicate-child
│                                classification and disposition (005 §6)
├── forbidden_operation_class    any EXECUTION/REVIEW/ADJUDICATION/RATIFICATION
│                                -class operation; any operation on its own
│                                constitution; any boundary standing for its
│                                own chamber
├── witness_eligibility          chamber-boundary transitions and projection
│                                admissions of chambers it does NOT occupy
├── proof_eligibility            NONE (admissible default, 005 §3) — its
│                                records enter EvaluateProof only under a
│                                Founder-authorized rule named in the
│                                evaluating act (005 §10 OQ-4 registry open)
├── source_binding_requirements  before operating: bind by sha256 the chamber's
│                                instantiating record, the projection record,
│                                and every subject artifact the admission
│                                depends on (003 §4 INV-5)
├── lifecycle                    PROPOSED (current) -> CONSTITUTED -> ACTIVE ->
│                                SUSPENDED -> EXPIRED|REVOKED|SUPERSEDED ->
│                                RETIRED; maintained by the constituting
│                                authority, never by this instrument
├── expiration/supersession      expires by named event: closure of the mission
│                                chamber it serves, or supersession by a
│                                successor constituting record; REVOKED
│                                propagates automatically from grant revocation
└── accountability/provenance    answers to the constituting grant's holder;
                                 every record carries constituting_grant_ref,
                                 instrument identity, and chamber binding
```

## What this record establishes and does not establish

Establishes: SPECIFIABILITY. Every field is filled from PHILOSELF-001..005
v0.3 alone — chamber states from 003 §6, projection states from 005 §6,
expiry events from 002 INV-6 + 003 chamber closure, proof default from 005
§3/INV-8, occupancy bar from 003 §3+INV-7. Nothing was invented.

Does not establish: an instrument. `constituting_grant_ref: NONE_YET` fails
closed. Constitution awaits a Founder grant; activation awaits commencement
(004 §4 INV-6); nothing here implements, runs, or admits anything.
