# 00_MANIFEST — OURSELF Agent Initiation Architecture

**Suite:** `governance/agent-selfrealization/`
**Protocol version:** `ourself.agent-selfrealization.v1`

## Status (read this before anything else)

```
Universal initiation architecture:  CANDIDATE
AgentBridge integration:             UNDECIDED
Ratified doctrine:                   NO
Runtime enforcement:                 NOT IMPLEMENTED
```

This suite is a **candidate constitutional protocol**. It is not ratified
doctrine, it does not govern any live agent by default, and it is not the
governing prefix of AgentBridge or of
`governance/agentbridge/workflow/`. Nothing in this suite may be cited as
binding until a Founder review explicitly ratifies it (see the trailing
disposition questions at the end of this document).

## Purpose

Answer, before any other document in this suite is read:

- What is this protocol suite?
- Which documents are normative candidates, which are generated at
  session time, and which are still exploration?
- What is the current protocol schema version?
- What is this suite's relationship to the pre-existing
  `governance/agentbridge/workflow/` stack?

## File inventory

```
governance/agent-selfrealization/
├── 00_MANIFEST.md                    this document — routing only
├── 01_UNIVERSAL_DOCTRINE.md           the durable law + universal cycle
├── 02_SELFREALIZATION_PROMPT.md       Chamber I canonical prompt
├── 03_SELFREALIZATION_SCHEMA.yaml     Chamber I machine-readable contract
├── 04_ROLE_CONSTITUTIONS/             11 role-specific constitutions
│   ├── observer.md
│   ├── researcher.md
│   ├── architect.md
│   ├── planner.md
│   ├── executor.md
│   ├── verifier.md
│   ├── governor.md
│   ├── memory-keeper.md
│   ├── dispatcher.md
│   ├── recovery.md
│   └── orchestrator.md
├── 05_RUNTIME_AUTHORIZATION_PACKET.md the bridge from REALIZED to Chamber II
├── 06_RUNTIME_FLOW.md                 Chamber II canonical prompt
├── 07_EXECUTION_WITNESS_SCHEMA.yaml    machine-readable execution witness
├── 08_HANDOFF_SCHEMA.yaml              machine-readable session handoff
└── 09_FALSIFICATION_TESTS.md           adversarial test bank for the suite
```

All 19 files above are candidate documents. None are generated at session
time in the sense `governance/agentbridge/workflow/07_LAUNCH_ROADMAP.md` is
regenerated — a `selfrealization_record` and an execution witness are
generated *instances* that conform to the schemas here, but the schemas and
prompts themselves change only through an explicit amendment gate.

## Reading / execution order

```
01_UNIVERSAL_DOCTRINE
  → 02_SELFREALIZATION_PROMPT  (Chamber I)
  → [selfrealization_record, per 03_SELFREALIZATION_SCHEMA.yaml]
  → 05_RUNTIME_AUTHORIZATION_PACKET
  → 06_RUNTIME_FLOW              (Chamber II)
  → [execution witness, per 07_EXECUTION_WITNESS_SCHEMA.yaml]
  → [handoff, per 08_HANDOFF_SCHEMA.yaml]
```

`04_ROLE_CONSTITUTIONS/` is consulted during Chamber I, Section III/IV, to
bound whichever role the agent has been assigned. `09_FALSIFICATION_TESTS.md`
is not part of the live execution path — it is the adversarial bank used to
review the suite itself.

## Two-chamber principle

```
SELFREALIZATION            RUNTIME
"what am I, where am I,    "given lawful identity and
what governs me, what      authority, what state
may I perceive, what may   transition do I execute
I change, how must I       now?"
prove it?"
```

Chamber II (`06_RUNTIME_FLOW.md`) is inaccessible to any agent until Chamber
I (`02_SELFREALIZATION_PROMPT.md`) has produced a `selfrealization_record`
whose `verdict.status` is `REALIZED`, per `01_UNIVERSAL_DOCTRINE.md`.

## Relationship to `governance/agentbridge/workflow/` (unresolved — do not assume)

This suite is drafted **implementation-neutral**: it does not reference,
depend on, or presuppose the AgentBridge-specific workflow numbering
(`01_SESSION_BOOTSTRAP.md` … `07_LAUNCH_ROADMAP.md`). The two stacks
currently stand as independent, sibling constitutional layers. Specifically
left undecided by this scaffold, and reserved for Founder disposition:

1. Whether `agent-selfrealization` becomes a mandatory Chamber-I prefix
   that every AgentBridge session must clear before
   `01_SESSION_BOOTSTRAP.md` runs.
2. Whether the two stacks instead remain permanently independent —
   AgentBridge-specific session bootstrap for AgentBridge work, this suite
   for the wider OURSELF agent population.
3. Whether a separate binding-adapter design gate is required to reconcile
   any overlapping responsibility (both stacks currently define their own
   gate-selection logic and their own verdict vocabularies, and those
   vocabularies are not identical).

No document in this suite claims to supersede
`governance/agentbridge/workflow/`, and no document there has been modified
to reference this suite.

## Required output of this document

Any session loading this manifest states, before proceeding to
`01_UNIVERSAL_DOCTRINE.md`, that it has read the Status block above and
will not treat this suite as ratified, runtime-enforced, or binding on
AgentBridge.

## Refusal / HOLD conditions

- Any attempt to treat this suite as already ratified, or as already
  governing AgentBridge, is itself a violation of this manifest and must be
  refused pending Founder disposition.
- Schema version mismatch between this manifest and any other document in
  the suite → `HOLD`.

## Trailing disposition (for Founder review, not for this session to decide)

- [ ] Ratify `01_UNIVERSAL_DOCTRINE.md` as durable doctrine.
- [ ] Approve `03_SELFREALIZATION_SCHEMA.yaml` / `07_...` / `08_...` as
      candidate machine-readable contracts.
- [ ] Ratify the 11 role constitutions.
- [ ] Decide whether SELFREALIZATION becomes a mandatory prefix to
      AgentBridge.
- [ ] Decide whether a binding-adapter design gate is required.

Ratification of any item above does not, by itself, authorize
implementation of a runtime validator. That is a separate gate.
