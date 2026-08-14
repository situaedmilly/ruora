# RC-0001 DURABLE DAILY RITUAL LEDGER SEMANTICPROGRAM v0.2
## Bounded revision candidate · SP-R02 · repairs Cold Review 001

**STATUS** CANDIDATE_READY_FOR_REVIEW · FOUNDER_DECISION_REQUIRED
**RATIFICATION** NOT RATIFIED · NOT SEALED · NOT COLD-REVIEWED
**PROOF SUBJECT** Durable Daily Ritual Ledger
**AUTHORIZED PATH** `governance/OURSELF-RCP-RC0001-DURABLE-DAILY-RITUAL-LEDGER-SEMANTICPROGRAM-v0.2-CANDIDATE.md`
**REVISION SUBJECT** v0.1 candidate `3e675d9ebd1e8bbb25193625ef9ca784146d8d639e57d5f5fe9dfaee46551537` — preserved unmodified as the exact subject of Cold Review 001
**REPAIR MANDATE** Cold Review 001 `54de4a52ffa4f63086cbc19d30e7d7beb49b5c61cc1b37a2605da187e626276f` · seven surfaces
**AUTHORITY LIMIT** Bounded semantic revision only. No founder adjudication, seal, extraction, representation selection, RealityIR, implementation, RC-0001 execution, protocol mutation, commission amendment, source-custody mutation, HBC mutation, staging, or commit.

**GOVERNING REPAIR CRITERION**

> A repair counts only if the normative representation either makes the defect **impossible** or makes it **explicitly detectable**.

Prose that merely asserts the defect is absent is not a repair. Each repair below states which of the two modes it achieves.

---

## 0. Authority, scope, and provenance

### 0.1 FD-01 governing order — unchanged

1. **L1** · the 2026-08-12 founder seal controls the RC-0001 proof-subject scope;
2. **L3** · later founder acts are valid founder-directed input but do not supersede L1;
3. **L2** · the authoring commission controls this movement's procedure and exact output path;
4. **L4** · reconciliation and review records are derived evidence, not sources of founder meaning.

```
L3 may elaborate L1.
L3 may add an orthogonal concern.
L3 may not silently replace or contradict L1.
If an adopted L3 interpretation conflicts with L1, L1 governs unless an explicit
later founder supersession is pinned. No such supersession is pinned.
```

### 0.2 Source pins

| Pin | Layer | Source | Exact identity |
|---|---|---|---|
| P-L1-A | L1 | Founder-sealed RC-0001 scope | Codex session `019ff7ee-9e35-7101-915e-74a0aae7d677` · ordinal 59 · text SHA-256 `4cfd687b2ea9cdbcf366c29a60b124e76cf0f9cce9fb4de897d812b69b3f4bb5` |
| P-L1-B | L1 | Founder constitutional laws and worked trace | same session · ordinal 72 · text SHA-256 `796a3588fbd8fbc611b62f6bba2267d462dd42f92f865a876f82e3387190e221` |
| P-L1-C | L1 | Founder proof topology, pass/fail predicates, stage contract, prohibitions, non-goals | same session · ordinal 85 · text SHA-256 `e951c1bc4f3fdb0fdfe4f133624acfd521dfedb7240bbdb80a0fe4147d82b8e3` |
| P-L1-CONTAINER | L1 custody | Raw founder-session container | SHA-256 `cee97abe168b011e8cc2bf1d69009d755f8c744998302c76743ac432a7d81ebe` |
| P-L2 | L2 | SemanticProgram authoring commission | SHA-256 `9a04124a25ec3dc9c281d73a4f6bce7ecb7a0619a0d9890f9a51fd5ce5dcc04e` |
| P-L3-A | L3 | Later founder SemanticProgram direction | Claude session `fcf1e66c-294f-4669-82e7-f83271b22970` · message `c563940d-dccb-4b24-88f3-ae3ef4b55537` · text SHA-256 `f0029a9ad5d362e9e8b5a35410da15babc0008b8d82299c2bb95dfde386f4802` |
| P-L3-FD01 | L3 | FD-01 source-authority and re-authorship act | Codex session `019ffad0-ee9c-74f1-85f9-a9efb60db01c` · message `msg_019ffbc7-7932-7b70-bfee-dbc65ba3aa43` · text SHA-256 `72a96c051531f1b7cbefd7a1061d8f6f68222594d4f7426d865e03da0bdaa771` |
| P-L4-R1 | L4 | Corrected source-lineage reconciliation | SHA-256 `a506352ae82bd889034b5972dc2b090185aac3c6ac58f6bbc083f7d4614e68c6` |
| P-L4-CR1 | L4 | Lineage-independent Cold Review 001 | SHA-256 `54de4a52ffa4f63086cbc19d30e7d7beb49b5c61cc1b37a2605da187e626276f` |
| P-V01 | Revision subject | v0.1 candidate | SHA-256 `3e675d9ebd1e8bbb25193625ef9ca784146d8d639e57d5f5fe9dfaee46551537` |
| P-OLD | Evidence only | Superseded DDRL candidate | SHA-256 `72a1bf7f869b76057e65d07884d1c0d35f6d8794b4acb87fe9428acf48ff3a47` |

The incomplete custody witness `0f61f7bb…734600` is preserved but is not a substitute for P-L1-A through P-L1-C.

### 0.3 Provenance model

Commission CP taxonomy (binding, unamended): `FOUNDER-DIRECTED` · `RCP-CONSTRAINED` · `AUTHOR-PROPOSED` · `UNRESOLVED`.

FD-01 lineage precision (LP, additive metadata): `FOUNDER_SEALED_L1` · `FOUNDER_DIRECTED_L3` · `COMMISSION_REQUIRED` · `AUTHOR_PROPOSED` · `DERIVED`.

**L1 relation (REVISED — now a substantive entailment judgment, not a label).** See §17.

```
EXACT        the pinned source establishes materially the same semantic
             proposition; the clause adds no semantic information
ELABORATES   the clause adds precision without narrowing or widening the
             source proposition
ORTHOGONAL   the clause is not required to satisfy any source proposition
CONFLICTS    the clause cannot coexist with a source proposition
```

**COMMISSION TAXONOMY GAP** remains FLAGGED FOR LATER AMENDMENT. CP cannot distinguish L1 from L3. This candidate records the gap through additive LP metadata and does not mutate the commission.

### 0.4 Normative envelope

Only rows carrying an **SP** identifier are normative. **FT** rows are derived falsification witnesses and add no law. **A** rows are docket questions. Prose, self-checks, and rejected alternatives create no semantic law.

---

## 0.5 Repair register — the seven mandated surfaces

| # | Surface | Repair mode | Governing clauses |
|---|---|---|---|
| 1 | Operator gate | **IMPOSSIBLE** — capability is removed from the sealed operations' preconditions and forbidden from gating them | SP-130, SP-030, SP-032, SP-034, SP-131 |
| 2 | False-open docket states | **DETECTABLE** — every A item carries a mechanically-derived closure class and a stated decidability test | §13, §13.0, §13.2 |
| 3 | A-03 / FT-03 contamination | **IMPOSSIBLE** — FT rows are branch-parameterized and structurally barred from discriminating unresolved alternatives | SP-140, FT-03 |
| 4 | Concurrent ordering | **IMPOSSIBLE** — total admission order is an input precondition; unordered presentation is excluded from RC-0001 input | SP-071, SP-120, SP-083 |
| 5 | Restart fact creation | **IMPOSSIBLE** — L-fact / T-fact partition makes preservation and witness-emission disjoint predicates | SP-103, SP-019, SP-102, SP-050, SP-051, §6.2 |
| 6 | inspect trace semantics | **IMPOSSIBLE** — inspect is removed as an operation; observation is a projection outside the conformance operation trace | SP-110–SP-114, SP-036 (withdrawn) |
| 7 | Provenance entailment | **DETECTABLE** — every EXACT claim carries a falsifiable entailment justification; the mechanical audit is renamed to what it proves | §17, §16.4 |

---

## 1. Identity, purpose, and non-goals

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-001 | RC-0001's proof subject is one substrate-independent Durable Daily Ritual Ledger whose preserved meaning includes Ritual, Entry, the observable progression idle → active → complete, begin, record, complete, invalid-transition behavior, durability, restart preservation, canonical ordering, and equivalent state traces. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-A, P-L1-B, P-L1-C | — |
| SP-002 | The program governs logical state and observable semantic consequence; no user interface, runtime, language, serialization, storage engine, network, or device mechanism is part of its meaning. | L2 | RCP-CONSTRAINED | COMMISSION_REQUIRED | ELABORATES | P-L1-B, P-L1-C, P-L2 §2.1 | — |
| SP-003 | A successful ledger transition establishes what the ledger records and no more. Entry status complete means the program's complete transition succeeded for that Entry-bearing cycle; it is not independent proof that an external-world act occurred. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L3-A, P-L4-R1 | A-05 |
| SP-004 | **REVISED (CR-08).** The founder-stated exclusions are, literally: no auth, no cloud, no camera, no AI, no networking; and the first proof is not beautiful UI, production architecture, App Store readiness, sophisticated Swift, sophisticated React, generalized storage abstraction, or a reusable design system. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-A, P-L1-B, P-L1-C | — |
| SP-100 | **NEW (CR-08).** Any generalization of SP-004's literal register — for example "distribution readiness" for App Store readiness, or "target-code sophistication" for sophisticated Swift and React — is authored elaboration and carries no founder seal. Where a generalization and the literal register differ in extent, the literal register governs. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-C | — |
| SP-005 | A conforming embodiment preserves the acceptance predicates of this SemanticProgram through normalized semantic observation; visual similarity, matching component structure, or matching binaries cannot substitute for semantic equality. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-B, P-L1-C | — |

### 1.1 Intended participant outcome

The ledger supplies one durable, ordered account of the content recorded while a Ritual is active and the completion state reached through lawful operations. It remains usable after a bounded restart and across daily recurrence, without importing an observer-adjudication ontology into the core state machine.

---

## 2. Semantic actors and capability

**REPAIR SURFACE 1.** In v0.1, SP-030/SP-032/SP-034 each required the invoker to be an `Operator`. The founder vector (P-L1-B) supplies no Participant, role, or role assignment. Cold Review 001 CR-01 showed that two embodiments could therefore disagree about whether the exact sealed trace succeeds. The gate is removed at the clause level, and its re-introduction is structurally barred.

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-010 | A Participant is a logical principal presented to the SemanticProgram. Participant identity proof and authentication mechanics are outside RC-0001. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L3-A | — |
| SP-011 | Invocation capability and observation capability are conceptually independent: possessing either does not imply possessing the other. This models the commission's required separation. It does not make either capability a precondition of any RC-0001 v0.2 operation. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L2 §6.2, P-L3-A | A-07 |
| SP-130 | **NEW · REPAIR 1.** RC-0001 v0.2 admits **no invocation-capability precondition** on begin, record, or complete. An invocation that reaches the SemanticProgram boundary is admissible; its acceptance or refusal is determined solely by state legality and content presence. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L4-CR1 CR-01 | A-07 |
| SP-131 | **NEW · REPAIR 1 (barrier).** No capability, permission, role, authority, or admission model — whether authored later, supplied by a substrate, or introduced by any extension — may cause the SP-090 founder vector to produce any outcome other than the one SP-090 states. A model that can do so is nonconforming, not an alternative reading. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B, P-L3-FD01, P-L4-CR1 CR-01 | — |
| SP-132 | **NEW.** A capability model may exist outside the SemanticProgram boundary as a substrate-level admission filter. Anything it refuses is an invocation that never reached the boundary and therefore has no program presence under SP-055. It is not a refusal outcome. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L2 §6.2, P-L4-CR1 CR-01 | A-07 |
| SP-013 | The designated RC-0001 conformance witness must be able to observe every L-fact in SP-019 at an identified operation position, through the SP-110 projection. Witness observation is not an operation. | L2 | AUTHOR-PROPOSED | COMMISSION_REQUIRED | ELABORATES | P-L1-B, P-L1-C, P-L2 §6.7 | — |
| SP-014 | No ledger fact is required by this SemanticProgram to be hidden from any Participant. Confidentiality and access-control policy are not semantic guarantees of RC-0001. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L2 §6.7 | — |
| SP-016 | No RC-0001 operation grants, transfers, revokes, or establishes a Participant's authority. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L2 §6.8 | A-05 |
| SP-028 | Refusal is produced by the SemanticProgram's state and content law; no Participant has discretionary power to convert a refused attempt into an accepted one, or an accepted attempt into a refused one. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-C, P-L2 §6.2 | — |
| SP-029 | No confirmer, amender, invalidator, Reporter, Assertion, Adjudicator, Adjudication, or Establishment construct exists in v0.2, because no confirmation, amendment, invalidation, or world-fact adjudication operation is admitted. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L2 §6.2, P-L3-FD01 | A-05, A-06 |

**Withdrawn from v0.1:** SP-012 (Operator/Observer as invocation gates), SP-015 and SP-062/SP-063 in their capability-gating form. Their commission-required content is re-expressed in SP-011, SP-014, SP-110–SP-114, and SP-060.

---

## 3. Semantic facts and identity

### 3.0 The L-fact / T-fact partition

**REPAIR SURFACE 5.** In v0.1, SP-019 placed semantic sequence position and operation outcomes in the same "complete normalized fact set" whose total preservation SP-051 required across restart, while §6.2 simultaneously required restart to advance position and append an outcome. Cold Review 001 CR-06 showed both cannot hold. v0.2 partitions the fact space so the two obligations attach to disjoint classes.

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-103 | **NEW · REPAIR 5.** The SemanticProgram's observable facts are partitioned into two disjoint classes. **L-facts** (ledger facts) are the state the program preserves. **T-facts** (trace facts) are the monotonic witness record of what was presented to the program and what it answered. No fact belongs to both classes. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-B, P-L1-C, P-L4-CR1 CR-06 | — |
| SP-019 | **REVISED.** The complete **L-fact** set is: Ledger identity; Ritual identity; current-state value; current DaySlot ordinal; ordered pending contributions while present; durable ordered Entries with content and status; and canonical history order. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-A, P-L1-B | A-01, A-03, A-04 |
| SP-102 | **NEW · REPAIR 5.** The complete **T-fact** set is: the operation position ordinal; the ordered operation-outcome stream; the restart-boundary markers; and the derived illegal-transition count over the supplied trace. T-facts are append-only and strictly monotonic. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-B, P-L1-C | — |
| SP-104 | **NEW · REPAIR 5 (the witness law).** A witness about preservation may not count as mutation of the thing whose preservation it witnesses. Emission of a T-fact never constitutes a change to any L-fact, and no preservation obligation in this program ranges over T-facts. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-B, P-L4-CR1 CR-06 | — |

### 3.1 Facts and identity clauses

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-017 | One SemanticProgram instance governs one logical Ledger identity and one Ritual-under-test identity. Daily recurrence continues that Ritual identity rather than silently creating a new Ritual definition. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L3-A | — |
| SP-018 | **REVISED (CR-02).** The founder vector exposes a top-level `state` value and a per-Entry `status` value as two separately named observation fields, both of which take the value complete in the sealed trace. This clause states that literal observation and nothing further. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-B | — |
| SP-101 | **NEW (CR-02).** Whether the two fields of SP-018 denote one predicate under two projections or two causally coupled predicates is **not** determined by their separate appearance. Both readings are admitted by v0.2. Any clause that would exclude either reading is nonconforming until A-02 is adjudicated. | L4 DERIVATION | UNRESOLVED | DERIVED | ELABORATES | P-L1-B, P-L4-CR1 CR-02 | A-02 |
| SP-020 | After a successful complete, each successful record in that active interval corresponds to exactly one durable Entry whose content equals the recorded content and whose status is complete. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B | A-03 |
| SP-021 | An Entry's semantic identity is its Ritual identity plus its canonical history position. Two successful record acts with equal content remain two distinct Entries because their canonical positions differ. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B, P-L1-C | A-03 |
| SP-022 | A successful record creates an observable ordered pending contribution immediately. Whether that contribution already bears Entry identity is left open by SP-026. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B | A-03 |
| SP-023 | A DaySlot is a monotonically ordered logical recurrence partition whose ordinal is semantic. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L3-A, P-L2 §6.9 | A-04 |
| SP-024 | Canonical history order is ascending DaySlot ordinal, then ascending successful-record order within the active interval associated with that DaySlot. Equal content never collapses distinct positions. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L1-C | A-04 |
| SP-025 | A completed Entry is immutable in v0.2: no admitted operation deletes it, rewrites its content, changes its status, or replaces its canonical position. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-C | A-06 |
| SP-026 | The candidate does not decide whether the pending contribution created by record already has Entry identity or acquires Entry identity only through complete. Both models are normatively admitted; see SP-140. | L4 DERIVATION | UNRESOLVED | DERIVED | ELABORATES | P-L1-A, P-L1-B, P-L4-CR1 CR-03 | A-03 |
| SP-027 | The candidate does not decide whether or how a logical DaySlot maps to a civil calendar, locale, or timezone. | L4 DERIVATION | UNRESOLVED | DERIVED | ELABORATES | P-L1-A, P-L2 §6.9 | A-04 |

### 3.2 Identity distinctions that must remain observable

- current `state` value versus Entry `status` value (as fields — see SP-101 for their relationship);
- pending recorded content versus a durable completed Entry;
- two successful records with equal content versus one record;
- the same L-fact values at different operation positions;
- an accepted operation versus a refused attempt;
- ledger completion versus an independently verified world event.

---

## 4. Operations

### 4.1 State-changing operations

**REPAIR SURFACE 1 applied.** Preconditions below are state-and-content only. No invoker qualification appears.

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-030 | **REVISED.** begin expresses intent to enter an active Ritual interval. It succeeds when and only when current state is idle; success changes current state to active, preserves all durable Entries, creates no Entry, and emits an accepted begin outcome. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B | A-01 |
| SP-031 | **REVISED.** A refused begin leaves every L-fact unchanged and emits a rejected begin outcome identifying `INVALID_TRANSITION`. The attempt has T-fact presence and no L-fact presence. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-A, P-L1-B, P-L2 §6.4 | — |
| SP-032 | **REVISED.** record(content) expresses intent to add one content-bearing contribution to the active interval. It succeeds when and only when current state is active and content is present as a semantic value; success appends one pending contribution in admission order, leaves state active and durable Entries unchanged, and emits an accepted record outcome. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B | A-03 |
| SP-033 | **REVISED.** A refused record leaves every L-fact unchanged and emits a rejected record outcome identifying `INVALID_TRANSITION` or `MISSING_CONTENT`. The attempt has T-fact presence and no L-fact presence. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-A, P-L1-B, P-L2 §6.4 | — |
| SP-034 | **REVISED.** complete expresses intent to close the active interval. It succeeds when and only when current state is active and at least one pending contribution exists; success changes current state to complete, causes one complete Entry per pending contribution to exist in canonical order, clears the pending projection, preserves all earlier Entries, and emits an accepted complete outcome. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B | A-01, A-02, A-03 |
| SP-035 | **REVISED.** A refused complete leaves every L-fact unchanged and emits a rejected complete outcome identifying `INVALID_TRANSITION` or `NO_RECORDED_CONTENT`. The attempt has T-fact presence and no L-fact presence. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-A, P-L1-B, P-L2 §6.4 | — |

**Withdrawn refusal reason.** `INVOCATION_NOT_PERMITTED` is removed from the state-changing operations' outcome vocabulary. Under SP-132 a capability refusal occurs outside the boundary and produces no outcome at all.

### 4.2 Observation — not an operation

**REPAIR SURFACE 6.** In v0.1, SP-036 made `inspect` an operation that "changes no fact" while simultaneously occupying the global sequence and emitting an outcome that SP-019 counted as a fact. Cold Review 001 CR-07 showed this forms a second program sharing one trace namespace, with undefined pre/post position, self-outcome inclusion, and freshness. §7.1 of that review independently proved inspect is removable without disturbing any L1 behavior.

**Disposition: `INSPECT IS OUTSIDE RC-0001 CONFORMANCE TRACE`.** `inspect` is withdrawn as a SemanticProgram operation. Observation is re-expressed as a total projection.

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-110 | **NEW · REPAIR 6.** Observation is a total function `view(n)` from any operation position `n` to the complete L-fact set as of `n`. It is a projection of program state, not an operation, not an attempt, and not an event. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L2 §6.7, P-L3-A, P-L4-CR1 §7 | — |
| SP-111 | **NEW · REPAIR 6.** `view` is defined at every operation position, emits no T-fact, occupies no position, never contributes to the illegal-transition count, and can never alter the acceptance, refusal, ordering, or outcome of any state-changing operation. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L4-CR1 §7.2 | — |
| SP-112 | **NEW · REPAIR 6.** `view` is total and deterministic: `view(n)` has exactly one value for a given input trace and position. Two observations of the same Ledger at the same position are the same value. Observations at different positions are different observations, not disagreement. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-C, P-L2 §6.7 | — |
| SP-113 | **NEW · REPAIR 6 (freshness).** Staleness is not a semantic property of the program. A substrate delivering `view(n)` when the greatest admitted position is `m > n` has delivered a correct observation of position `n`. Because `view` is total and position-indexed, no currentness or maximum-staleness obligation is required, and none is imposed. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L2 §6.7, P-L4-CR1 CR-07 | — |
| SP-114 | **NEW · REPAIR 6 (conformance).** The RC-0001 conformance witness compares `view(n)` and the T-fact stream across substrates. Because observation emits nothing, no read can influence pass/fail except through the values it reports. | L2 | AUTHOR-PROPOSED | COMMISSION_REQUIRED | ELABORATES | P-L1-B, P-L1-C | — |

### 4.3 Operation-wide law

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-037 | Each operation is semantically atomic. No conforming observation may return a partially applied begin, record, or complete; there is no required visible state between attempt and accepted-or-rejected outcome. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-C, P-L2 §6.4 | — |
| SP-038 | Every accepted state-changing operation is distinguishable from a no-op by a changed L-fact set or an accepted outcome. Every rejected attempt is distinguishable from absence of an attempt by its rejected T-fact outcome. | L2 | AUTHOR-PROPOSED | COMMISSION_REQUIRED | ELABORATES | P-L1-C, P-L2 §7 | — |
| SP-039 | begin, record, and complete require no Assertion, Reporter, Adjudicator, Adjudication, Establishment, contest status, capability, or authoritative-world-answer precondition. The founder trace must succeed without any such construct. | L3 | FOUNDER-DIRECTED | FOUNDER_DIRECTED_L3 | ELABORATES | P-L3-FD01 | — |

---

## 5. State model and invariants

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-040 | Initial current state is idle, pending count is zero, and durable Entry history may be empty or may contain Entries preserved from earlier DaySlots. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B | A-01 |
| SP-041 | Founder-sealed operation transitions are idle —begin→ active, active —record→ active, and active —complete→ complete. No other state-changing operation transition is lawful. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-A, P-L1-B | — |
| SP-042 | Within one DaySlot, complete is terminal for state-changing operations. A later DaySlot boundary may make a new daily cycle idle under SP-053 without deleting prior Entries. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L3-A | A-01, A-04 |
| SP-043 | A state-illegal begin, record, or complete is rejected, changes no L-fact, and contributes one to the illegal-transition count derived over the supplied trace. `MISSING_CONTENT` and `NO_RECORDED_CONTENT` refusals are non-state refusals and do not contribute to that count. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-A, P-L1-B, P-L1-C | — |
| SP-044 | Pending-contribution order equals accepted record admission order. complete preserves that relative order when the corresponding Entries join history. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L1-C | A-03 |
| SP-045 | Canonical history order is total, stable across every contemplated discontinuity, and independent of wall-clock timestamps. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L1-C | A-04 |
| SP-046 | Once complete, an Entry and its content, status, and relative order survive a contemplated restart. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-A, P-L1-B | A-06 |
| SP-047 | **REVISED.** The candidate does not decide which entity owns current state. See SP-101 for the operation/state completion relationship and A-01 for ownership. | L4 DERIVATION | UNRESOLVED | DERIVED | ELABORATES | P-L1-B, P-L4-R1 | A-01, A-02 |
| SP-048 | No correction, amendment, deletion, supersession, invalidation, scheduling, or world-fact adjudication transition exists in the v0.2 core state machine. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L1-A, P-L3-FD01 | A-05, A-06 |
| SP-049 | Once complete, an Entry and its content, status, identity, and relative order survive later DaySlot transitions. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L3-A | A-04, A-06 |

---

## 6. Discontinuities

### 6.1 Contemplated classes

| Clause | Discontinuity and exact boundary | L-facts that survive | L-facts that must not survive | Ordering | Permitted degradation | T-fact effect | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SP-050 | **REVISED.** restart means a page/runtime reload, process restart, or device restart followed by re-entry to the same logical Ledger identity with its durable semantic state available. | Ledger and Ritual identity; current state; DaySlot; pending contributions; completed Entries; canonical order. | None. No L-fact is required to be destroyed. Volatile presentation state is not an L-fact. | Pending and history order remain identical. | None. An L-fact either survives exactly or the restart law is violated. | Exactly one restart-boundary T-fact is appended and the position ordinal advances by one. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L1-C | — |
| SP-051 | **REVISED · REPAIR 5.** A restart invokes no operation and changes no L-fact. Its entire semantic footprint is the single T-fact required by SP-050. | All L-facts existing immediately before interruption. | None. | Identical before and after. | None. | Exactly one boundary marker; the outcome stream is otherwise unchanged. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L4-CR1 CR-06 | — |
| SP-052 | Total destruction of the logical Ledger identity or loss of all durable semantic state is not a restart under SP-050. RC-0001 v0.2 makes no survival claim across that different event. | Not specified; the event is outside the contemplated class. | Not specified. | Not specified. | The event may not be relabeled as a conforming restart. | Not specified. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L4-CR1 §4 | — |
| SP-053 | DaySlot boundary increments the DaySlot ordinal. idle remains idle; complete becomes idle for a new cycle; active remains active and keeps its originating DaySlot until complete. | Ledger and Ritual identity; pending contributions; completed Entries; their origin DaySlots; canonical order. | No completed Entry or pending contribution is destroyed. The prior current-state value need not survive when complete becomes idle. | History order preserved; later Entries sort after earlier DaySlots. | None. | One boundary marker; position advances by one. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L3-A | A-01, A-04 |
| SP-054 | **REVISED.** A change in who is observing is not a discontinuity of this program. Because observation is the total projection SP-110, there is no observer state to lose. | Every L-fact. | None. | Unchanged. | None. | None. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L2 §6.7, P-L4-CR1 CR-07 | — |
| SP-055 | Temporary disconnection means a Participant cannot present an invocation to the semantic boundary for an interval. An invocation not presented has no program presence: no L-fact, no T-fact, no outcome. | All L-facts. | None. | Preserved. | Unpresented intent is never promoted into any fact. | None. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L3-A, P-L2 §6.6 | — |

### 6.2 Restart preservation witness — REVISED, now consistent

At operation position `n`, a restart yields position `n+1`. Then:

```
view(n+1) = view(n)                       every L-fact identical
T-facts(n+1) = T-facts(n) + one restart-boundary marker
```

The two lines are about disjoint fact classes (SP-103), so both hold without contradiction. A reload that returns idle after a pre-restart complete, drops a pending contribution from active, changes Entry order, or changes content is nonconforming. A reload that fails to record its boundary marker is likewise nonconforming, because the T-fact stream must witness every discontinuity.

**Why the v0.1 contradiction is now impossible:** SP-051's preservation obligation ranges only over L-facts (SP-103, SP-104), and the position ordinal and outcome stream are T-facts by SP-102. No clause requires a T-fact to be preserved unchanged.

---

## 7. Observer, confidentiality, authority, and confirmation

### 7.1 Observation matrix

All rows are values of the SP-110 projection. No row describes an operation.

| L-fact class | Who must be able to observe it | Who must not observe it | Agreement law | Position law |
|---|---|---|---|---|
| current state and DaySlot | designated conformance witness | nobody is semantically prohibited | `view(n)` is single-valued | different `n` may differ; each observation is position-identified |
| ordered pending contributions | designated conformance witness while present | nobody is semantically prohibited | `view(n)` is single-valued | as above |
| completed Entries, content, status, identity, order | designated conformance witness | nobody is semantically prohibited | `view(n)` is single-valued | later positions may add Entries but never rewrite earlier ones |

| T-fact class | Observation law |
|---|---|
| operation-outcome stream, restart markers, illegal-transition count | witnessed as an append-only stream; the same input trace yields the same stream |

### 7.2 Authority and confirmation clauses

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-060 | A state counts as achieved when its lawful state transition succeeds. No separate confirmation, acceptance, Adjudication, Establishment, capability, or authoritative-world-answer act is required. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L3-FD01 | A-05 |
| SP-061 | record preserves supplied content as ledger content. It does not convert that content into an externally verified claim, a completion observation, or an authority decision. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L3-A, P-L4-R1 | A-05 |
| SP-064 | v0.2 contains no unconfirmed-intent state that can masquerade as accepted world fact: pending content is visibly pending, and completed Entry status denotes ledger completion only under SP-003. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L2 §6.8 | A-03, A-05 |

The candidate answers the commission's confirmation questions without an adjudication ontology. It supplies one authoritative semantic state for the Ledger at each position, and makes no claim about the external world.

---

## 8. Time, ordering, admission, and recurrence

### 8.0 Admission order — REPAIR SURFACE 4

**The v0.1 defect.** SP-071 required a total order but supplied no rule selecting it; SP-083 delegated meaning to "whichever attempt is first." Cold Review 001 CR-05 exhibited two lawful serializations of concurrent `record("B")` and `complete` producing different Entry sets. That is direct nondeterminacy under a proof whose whole subject is equivalence.

**The v0.2 repair — order is an input, not an outcome.**

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-071 | **REVISED · REPAIR 4 (SERIALIZE).** The SemanticProgram's input is a **totally ordered sequence of admitted invocation records and discontinuity boundaries**. Every admitted invocation receives exactly one position ordinal at admission, **before** any transition evaluation. Transition legality is then evaluated strictly in that order. The order is part of the input, never a result of interpretation. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B, P-L1-C, P-L4-CR1 CR-05 | — |
| SP-120 | **NEW · REPAIR 4 (EXCLUDE).** A presentation that does not yield a total admission order is **not RC-0001 v0.2 SemanticProgram input**. Substrate-level simultaneity is a condition the embodiment must resolve into an admission order before the boundary; that resolution is an input-construction act, not a semantic choice. A conformance vector that fails to determine the admission order of two attempts is malformed and may not be run. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-C, P-L4-CR1 CR-05 | — |
| SP-121 | **NEW · REPAIR 4 (barrier).** Two embodiments given the same SemanticProgram input necessarily receive the same admission order, because the order is a component of that input. Divergent Entry sets arising from different serializations are therefore impossible for one input, and any observed divergence is a conformance failure rather than a permitted reading. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-B, P-L1-C, P-L4-CR1 CR-05 | — |
| SP-070 | Wall-clock time and timestamps are not semantic order sources. Admission position ordinal, DaySlot ordinal, and accepted record order are the only ordering facts. Admission order is supplied as input and is never derived from a clock. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-C, P-L2 §6.9 | A-04 |
| SP-083 | **REVISED.** Conflicting state-changing attempts are resolved solely by their admission order under SP-071. Each is evaluated against the state produced by its predecessors. No last-writer, recency, or wall-clock rule may replace transition legality. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-C | — |
| SP-072 | A late invocation is judged against the state at its admission position, not against the state that existed when Participant intent was formed. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L3-A, P-L2 §6.9 | — |
| SP-073 | Repeated successful record invocations are distinct accepted acts even when their content is equal. A repeated begin or complete after the first state change is refused by the invalid-transition law. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L2 §6.10 | — |
| SP-074 | Daily recurrence creates a new DaySlot while preserving the same Ledger and Ritual identities and all earlier Entries. A missed idle DaySlot creates no Entry. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L3-A | A-04 |
| SP-075 | An active interval crossing a DaySlot boundary retains its originating DaySlot for the Entries produced when it later completes. No second active interval begins while current state remains active. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L3-A | A-01, A-04 |

---

## 9. Failure, duplication, conflict, and recovery

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-080 | Every admitted invocation yields exactly one accepted or rejected outcome. Refusal never silently becomes success and never partially mutates any L-fact. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B, P-L1-C, P-L2 §6.10 | — |
| SP-081 | Retrying a rejected operation is a new admitted invocation at a later position. A prior refusal neither reserves a future success nor suppresses the retry's outcome. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L2 §6.10 | — |
| SP-082 | Re-delivery has no hidden deduplication semantics. Two admitted record invocations produce two pending contributions and, after complete, two Entries. An embodiment may suppress transport duplicates only before admission, so that the semantic input contains one invocation rather than two. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L2 §6.10 | — |
| SP-084 | Recovery from a contemplated restart is exact L-fact continuation under SP-050 and SP-051. Recovery may not synthesize missing Entries, discard pending contributions, reorder history, or reset complete to idle. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L1-C | — |

---

## 10. L3-under-L1 reconciliation

Carried forward from v0.1 with the dispositions updated by this revision. L3 remains valid founder-directed input and is not promoted into L1 law.

| L3 construct or area | Candidate disposition in v0.2 | L1 relation | Governing clause or decision |
|---|---|---|---|
| Ledger · Ritual | admitted as program container and Ritual-under-test | EXACT | SP-001, SP-017 |
| RitualOccurrence / PlannedOccurrence | not adopted as core entities | ELABORATES if adopted | A-01 |
| CompletionObservation | not required for the founder trace | ORTHOGONAL if non-gating | A-05 |
| Correction | not adopted in v0.2 | ORTHOGONAL if it preserves L1 history | SP-025, A-06 |
| Day | logical DaySlot; civil mapping open | ELABORATES | SP-023, A-04 |
| Participant / Observer | Participant retained; **capability no longer gates any operation** | ELABORATES | SP-010, SP-011, SP-130–SP-132, A-07 |
| AuthorityDecision | not required to achieve L1 state | ORTHOGONAL if non-gating | A-05 |
| define / schedule ritual | outside the sealed three-operation core | ORTHOGONAL | SP-048 |
| observe / inspect | **re-expressed as the SP-110 projection; withdrawn as an operation** | ELABORATES | SP-110–SP-114 |
| record completion / noncompletion | record accepts opaque content; asserts no world fact | ELABORATES | SP-032, SP-061 |
| observation / authority separation | answered as independent *concepts*, neither of which gates an operation | ELABORATES | SP-011, SP-130 |
| recorded intent versus accepted fact | pending content distinct from completed Entry; neither is a verified world fact | ELABORATES | SP-022, SP-064 |
| observer septuple | answered by the projection, position, and agreement clauses | ELABORATES | SP-110–SP-114 |
| PENDING / CORROBORATED / CONTESTED / REJECTED / SUPERSEDED / STANDING | not adopted; core state remains idle / active / complete | ORTHOGONAL | SP-018, SP-041 |
| cross-day-boundary | a contemplated DaySlot discontinuity, not a fourth operation | ELABORATES | SP-053, SP-074, SP-075 |
| reconcile observations | not adopted; observation is a projection and cannot mutate state | ORTHOGONAL | SP-110, SP-111, A-05 |
| Assertion / Adjudication / Establishment ontology | **remains rejected as a precondition of RC-0001** | CONFLICTS when it gates the founder trace | SP-029, SP-039, SP-060 |

**Closed by cold review, not reopened.** Cold Review 001 §4 classified the removal of the assertion/adjudication gate as a `REFUTED CONCERN` — the gate is correctly prohibited and the founder vector no longer depends on it. This revision does not reintroduce Assertion, Adjudication, or Establishment in any form, and no repair below required them.

---

## 11. Founder-sealed trace and acceptance predicates

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-090 | From an idle state with an empty current cycle, the trace `begin; record("Reflect"); complete; restart` yields `state = complete`, `entries.count = 1`, `entries[0].content = "Reflect"`, `entries[0].status = complete`, `history_order = canonical`, and `illegal_transition_count = 0`. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-B | A-01, A-02, A-03 |
| SP-091 | For the same SemanticProgram input, the reference semantic trace and each normalized target trace must be equal. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-B, P-L1-C | — |
| SP-092 | **REVISED — now literal to the founder Fail list.** Semantic preservation fails if any of these diverges: legal transition behavior; illegal transition behavior; durable state; restart semantics; ordering; failure semantics; normalization; acceptance predicates. Divergence fails the proof even if both embodiments look immaculate. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-C | — |
| SP-093 | Normalization may erase structural, visual, binary, runtime, and presentation differences, but may not erase any distinction needed to evaluate SP-090 through SP-092. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-B, P-L1-C | — |

SP-090 is a custody-preserving restatement of the founder-authored worked trace. It is not a newly authored conformance vector and authorizes no execution.

### 11.1 Founder-trace satisfiability derivation — REPAIR 1 verified

| Step | Precondition and governing clause | Required result |
|---|---|---|
| initial | SP-040 | current state idle; pending count zero |
| `begin` | current state is idle — SP-030 | accepted; state active |
| `record("Reflect")` | state active; content present — SP-032 | accepted; one pending contribution "Reflect"; state active |
| `complete` | state active; ≥1 pending contribution — SP-034 | accepted; state complete; one complete Entry "Reflect"; pending cleared |
| `restart` | same Ledger identity — SP-050, SP-051 | every L-fact preserved; one boundary T-fact appended |
| observation | SP-110 `view` at the final position | SP-090 result; all three attempts were state-legal, so `illegal_transition_count = 0` |

**No step supplies a Participant, role, capability, Operator, Observer, Assertion, Adjudication, or Establishment.** Every precondition is discharged by a fact the founder's written trace itself contains: the state, and the content string. This is the CR-01 repair, verified against its own defect: the derivation adds nothing to the trace.

---

## 12. Falsifying traces

### 12.0 Trace law — REPAIR SURFACE 3

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-140 | **NEW · REPAIR 3.** A falsifying trace may test admitted semantics. It may not manufacture semantics. Where a docket item admits more than one normative model, no FT row may treat either model's observable consequence as falsifying. Such a row must either restrict itself to consequences shared by all admitted models, or state its branch condition explicitly and remain inert until the item is adjudicated. An FT row that discriminates an admitted alternative is void, not authoritative. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L2 §6.11, P-L4-CR1 CR-03 | — |

### 12.1 Trace suite

| Trace | Input | Expected normalized observation | Falsifying observation | Basis |
|---|---|---|---|---|
| FT-01 · founder success and restart | `begin → record("Reflect") → complete → restart` | state complete; one Entry; content "Reflect"; status complete; canonical history; zero illegal transitions; one restart boundary T-fact | any missing/extra Entry; changed content, status, or order; state other than complete; nonzero illegal count; **any need for a capability, role, or adjudication input** | SP-039, SP-090, SP-130 |
| FT-02 · invalid transition refusal | idle → `record("Reflect")` | rejected `INVALID_TRANSITION`; state idle; no pending contribution; no Entry; illegal count 1 | record accepted; any Entry or pending contribution appears; refusal absent; any L-fact changes | SP-041, SP-033, SP-043 |
| FT-03 · active restart — **BRANCH-PARAMETERIZED (CR-03)** | `begin → record("Reflect") → restart → complete` | **Shared by every admitted A-03 model, and the only falsifiable content of this row:** after restart, state is active and one pending contribution with content "Reflect" is present in unchanged order; after complete, exactly one complete Entry with content "Reflect" exists. | restart resets to idle; pending content dropped or altered; pending order changed; lawful complete prevented; more or fewer than one Entry after complete | SP-050, SP-051, SP-084, SP-140 |
| | **A-03 branch note — inert until adjudicated.** Under A-03(A) the pending contribution already bears Entry identity across the restart; under A-03(B) it does not. **Neither observation falsifies preservation.** v0.1's FT-03 declared that a restart which "creates an Entry early" falsifies preservation; that clause is withdrawn as void under SP-140, since it discriminated an alternative SP-026 leaves open. | | | |
| FT-04 · observation position | one record succeeds between positions `n` and `n+1`; observe at both | `view(n)` and `view(n+1)` are each single-valued; they differ by exactly the new contribution; observing does not append any T-fact or change any L-fact | two different values at the same position; an observation appending an outcome, advancing the position, or altering the illegal count | SP-110–SP-113 |
| FT-05 · **concurrency exclusion — NEW (CR-05)** | active with pending `["A"]`; a vector presenting `record("B")` and `complete` **without** a determined admission order | the vector is **malformed** and must not be run | the vector is run and yields a result; or two embodiments run it and report different Entry sets as both conforming | SP-071, SP-120, SP-121 |
| FT-06 · **ordered concurrency — NEW (CR-05)** | the same two invocations, admitted in the stated order `record("B") < complete` | both accepted; Entries `[A, B]`; illegal count unchanged | any embodiment producing `[A]` with a rejected record for this input, i.e. silently re-serializing a supplied order | SP-071, SP-083, SP-121 |
| FT-07 · duplicate content and order | `begin → record("Reflect") → record("Reflect") → complete` | two distinct complete Entries, equal content, record order, distinct canonical positions | one Entry due to content deduplication; reversed or unstable order; ambiguous identity | SP-021, SP-073, SP-082 |
| FT-08 · operational similarity, semantic difference | trace A: active with one pending → `complete`; trace B: already complete → `complete` | A accepted and changes state and history; B rejected `INVALID_TRANSITION`, changes no L-fact, increments illegal count | both normalize as "complete"; refusal loses T-fact presence; B creates or changes an Entry | SP-034, SP-035, SP-038 |
| FT-09 · day recurrence and active carry | trace A: complete → DaySlot boundary; trace B: active with one pending → DaySlot boundary | A becomes idle with history intact; B remains active, retains pending contribution and origin DaySlot; both increment DaySlot | history deletion; active reset; pending loss; identical outcome for A and B; changed canonical order | SP-053, SP-074, SP-075 |
| FT-10 · **restart fact partition — NEW (CR-06)** | any state at position `n` → restart | `view(n+1) = view(n)` exactly; T-facts gain exactly one boundary marker; position advances by exactly one | any L-fact differs across the boundary; **or** no boundary marker is emitted; or more than one marker is emitted | SP-050, SP-051, SP-103, SP-104 |

**Commission §6.11 coverage:** successful operation FT-01 · refused operation FT-02, FT-08 · contemplated discontinuity FT-03, FT-09, FT-10 · visibility boundary FT-04 · authority boundary — **see §12.2** · temporal/duplicate/conflict edge FT-06, FT-07 · operationally similar but semantically different FT-08.

### 12.2 The authority-boundary trace, and why it is now absent

Commission §6.11 requires a trace exercising "one authority boundary." v0.1 supplied FT-05, in which a pure Observer's `begin` was refused `INVOCATION_NOT_PERMITTED`. **That trace is withdrawn** — it was the direct expression of the CR-01 defect, and SP-130 removes the boundary it tested.

This is reported as a **residual gap**, not repaired by weakening the test. Under v0.2 there is no in-program authority boundary to exercise, because capability was removed from the operations to make the founder vector self-sufficient. The commission requirement and the CR-01 repair are in genuine tension, and the resolution belongs to the founder as **A-07**. If A-07 adopts a capability model, an authority-boundary trace becomes possible and required; if it ratifies the non-gating branch, §6.11's authority clause is inapplicable to this subject and the commission should record that.

Recorded as `SP-R02-GAP-01`. Not concealed, not self-waived.

---

## 13. Founder decision docket

### 13.0 Closure classification — REPAIR SURFACE 2

**The v0.1 defect.** Six items were labeled OPEN while operative clauses required one branch. Cold Review 001 CR-02 and CR-04 confirmed five of six.

**The v0.2 mechanism.** Every item is classified by one decidability test, applied to the v0.2 clause set:

> **T(A):** Can two embodiments, each adopting a different admitted alternative of A, both conform to every operative SP clause in this document?

```
YES for all alternatives          → OPEN
YES for some, NO for others       → PARTIALLY_DECIDED   (list which are excluded)
NO for all but one                → OPERATIVELY_DECIDED (name the installed branch)
```

Every item additionally carries `FOUNDER_DECISION_REQUIRED`, which is an authority status, not a closure class. A question may be operatively decided by authorship and still require founder ratification — indeed that is the normal case, and conflating the two is what produced the v0.1 defect.

**A question is not OPEN because a heading says so. It is OPEN only if T(A) returns YES for every listed alternative.**

### 13.1 Classification result

| Item | Question | Closure class | Installed / excluded branch | Authority |
|---|---|---|---|---|
| A-01 | Which entity owns the observable idle → active → complete state? | **OPERATIVELY_DECIDED** | **Installed: D** — SP-019's L-fact set contains a current-state value with no owner coordinate, so an owner relation cannot be conformance-tested. Alternatives A, B, C are not excluded in principle but are unobservable under v0.2 and therefore untestable. | FOUNDER_DECISION_REQUIRED |
| A-02 | What relation holds between invoking complete and observing state complete? | **OPEN** | SP-018 now states only the literal two-field observation and SP-101 expressly admits both the one-predicate and the two-coupled-predicate readings. T(A-02) = YES for A, B, and C. **This is a genuine repair of CR-02:** v0.1's `EXACT` distinctness claim excluded model M1; v0.2 does not. | FOUNDER_DECISION_REQUIRED |
| A-03 | Does record create an Entry, mutate one, or create a non-Entry contribution? | **OPEN** | SP-026 admits both models; SP-140 bars any FT row from discriminating them; FT-03 is branch-parameterized. T(A-03) = YES for A and B. Alternative C (pre-existing Entry mutated by record) is **excluded** by SP-022's requirement that a contribution be *created*, making this strictly `PARTIALLY_DECIDED` — recorded as such below. | FOUNDER_DECISION_REQUIRED |
| A-04 | What maps a logical DaySlot to a civil day? | **OPERATIVELY_DECIDED** | **Installed: A (DaySlot only).** SP-023, SP-024, SP-053, SP-070, SP-074, SP-075 make a logical ordinal the semantic day, and SP-019's L-fact set contains no timezone, locale, or civil-boundary fact. Alternatives B and C require facts v0.2 does not carry. | FOUNDER_DECISION_REQUIRED |
| A-05 | Does RC-0001 need a world-fact observation and authority layer? | **OPERATIVELY_DECIDED** | **Installed: A (no additional layer).** SP-029, SP-048, SP-060, SP-061, SP-064 make lawful transition sufficient and admit no world-authority construct. Alternative B remains available to a future version only as a strictly non-gating extension under SP-131. | FOUNDER_DECISION_REQUIRED |
| A-06 | Can completed Entry meaning later be corrected? | **OPERATIVELY_DECIDED** | **Installed: A (no correction).** SP-025, SP-029, SP-048, SP-049 make completed Entries immutable and admit no correction operation. | FOUNDER_DECISION_REQUIRED |
| A-07 | **NEW.** Does RC-0001 admit an invocation-capability precondition on begin, record, and complete? | **OPERATIVELY_DECIDED** | **Installed: no capability gate.** SP-130 removes it; SP-131 bars any model that would let it reject the founder vector; SP-132 places capability filtering outside the boundary. This is the CR-01 repair and it is an author choice, disclosed as installed rather than presented as open. | FOUNDER_DECISION_REQUIRED |

**Corrected classification for A-03:** `PARTIALLY_DECIDED` — alternatives A and B open, alternative C excluded by SP-022.

**Summary:** OPEN 1 · PARTIALLY_DECIDED 1 · OPERATIVELY_DECIDED 5 · all seven FOUNDER_DECISION_REQUIRED.

v0.1 reported six OPEN. The true count of genuinely open questions was one. That gap is the defect CR-04 named, and it is now visible in the document rather than only in the review.

### 13.2 Decision detail

Each item retains its v0.1 alternatives and consequences, which are not restated here in full; the material change is the closure class above and the following additions.

**A-01** · Pinned constraint: SP-090 exposes top-level `state` separately from Entry `status`. Author recommendation: D, `AUTHOR-PROPOSED`. **Disclosure:** D is installed, not merely recommended. Selecting A, B, or C requires adding an owner coordinate to SP-019.

**A-02** · Pinned constraint: every lawful answer must make the founder sequence yield `state = complete` and `entries[0].status = complete`. Author recommendation: **withdrawn.** v0.1 recommended B and installed it through SP-018's `EXACT` mark. v0.2 makes no recommendation, because a recommendation here was the vehicle of the defect.

**A-03** · Pinned constraint: record succeeds while active; after complete the founder trace has one Entry with content "Reflect" and status complete. Author recommendation: B, `AUTHOR-PROPOSED`, **non-operative** — SP-026 and SP-140 ensure the recommendation has no normative force.

**A-04, A-05, A-06** · Alternatives and consequences as in v0.1. Each now discloses its installed branch.

**A-07** · Alternatives: (a) no capability precondition — installed; (b) capability precondition with the founder vector's invoker declared capable by definition; (c) capability precondition with an explicit role-assignment input added to the sealed vector. Consequence of (b) and (c): the sealed trace ceases to be self-sufficient and requires an input the founder never wrote, which is why (a) is installed. Downstream: A-07 determines whether `SP-R02-GAP-01` is a real gap or a non-applicable commission clause.

---

## 14. Extraction-readiness crosswalk

| Instrument question | Candidate clauses or witnesses | Readiness |
|---|---|---|
| Q1 · truth after operation success | SP-030, SP-032, SP-034; FT-01 | ANSWERABLE |
| Q2 · truth after refusal | SP-028, SP-031, SP-033, SP-035, SP-043; FT-02, FT-08 | ANSWERABLE |
| Q3 · intermediate state | SP-037, SP-080 | ANSWERABLE — partial state forbidden and unobservable |
| Q4 · effect distinguishable from no-op | SP-038, SP-043; FT-02, FT-08 | ANSWERABLE |
| Q5 · facts surviving each discontinuity | SP-050–SP-055; FT-03, FT-09, FT-10 | ANSWERABLE |
| Q6 · facts that must not survive | SP-050–SP-055 | ANSWERABLE — each class states destruction or explicitly states none |
| Q7 · surviving relative order | SP-044–SP-046, SP-050–SP-055 | ANSWERABLE |
| Q8 · permitted degradation | SP-050–SP-055, SP-113 | ANSWERABLE — no degradation permitted; staleness is not degradation but position-indexing |
| Q9 · required observer | SP-013, SP-110, SP-114, §7.1 | ANSWERABLE |
| Q10 · multi-party observability | SP-014, SP-112, §7.1 | ANSWERABLE |
| Q11 · observer agreement | SP-112; FT-04 | ANSWERABLE |
| Q12 · required unobservability | SP-014, §7.1 | ANSWERABLE — none required |
| Q13 · authority confirmation | SP-029, SP-060, SP-130 | ANSWERABLE; A-05 and A-07 record the installed branches |
| Q14 · required unconfirmed intent | SP-022, SP-026, SP-061, SP-064 | ANSWERABLE; A-03 remains visible |
| Q15 · authority transfer or establishment | SP-016, SP-039, SP-060 | ANSWERABLE — no operation transfers authority |
| Q16 · erasure versus falsification | SP-090–SP-093; FT-01–FT-10; §3.2 | EVALUABLE by a later extraction movement |

---

## 15. Representation firewall and namespace check

The author has seen representation-lineage material and makes no coldness claim. No semantic choice above is justified by the vocabulary or capability of any representation under later test.

Subject-local meanings: `canonical` means only the comparator in SP-024; `durable` means only the survival obligations bounded by SP-050–SP-052; `position` means only the admission ordinal in SP-071; `pending` means only the pre-complete observable effect in SP-022; `view` means only the projection in SP-110.

The candidate contains no database schema, storage-engine choice, serialization shape, interface flow, target-language construct, RealityIR, RequiredVectors, tolerance class, emitter design, resolver, oracle, representation option, F-05 tier selection, HBC accommodation, or implementation backlog.

---

## 16. Author-side conformance

### 16.1 Sealed-scope coverage

| Gate | Required L1 surface | Evidence | Result |
|---|---|---|---|
| S-01 | Ritual and Entry | SP-001, SP-017, SP-020–SP-022, SP-026 | PASS |
| S-02 | idle → active → complete; begin, record, complete | SP-018, SP-030–SP-035, SP-041 | PASS |
| S-03 | invalid-transition and failure law | SP-031, SP-033, SP-035, SP-043, SP-080–SP-083 | PASS |
| S-04 | durable Entry and restart preservation | SP-046, SP-050–SP-052, SP-084; FT-03, FT-10 | PASS |
| S-05 | canonical ordering, equivalent traces, acceptance predicates | SP-024, SP-044, SP-045, SP-090–SP-093 | PASS |
| S-06 | founder exclusions, non-goals, concrete founder trace | SP-004, SP-005, SP-090 | PASS |

**SEALED-SCOPE COVERAGE 6/6.**

### 16.2 Cold-review repair surfaces

| # | Surface | Mode | Verification |
|---|---|---|---|
| 1 | Operator gate | IMPOSSIBLE | §11.1 derives the founder vector using only state and content; SP-131 bars any model that could reject it |
| 2 | False-open docket | DETECTABLE | §13.0's T(A) test applied to all seven items; result 1 OPEN / 1 PARTIAL / 5 OPERATIVELY_DECIDED |
| 3 | A-03 / FT-03 | IMPOSSIBLE | SP-140 voids any discriminating FT row; FT-03 restricted to shared consequences with an inert branch note |
| 4 | Concurrency | IMPOSSIBLE | SP-071 makes order an input; SP-120 excludes unordered presentation; SP-121 states the barrier; FT-05, FT-06 witness it |
| 5 | Restart fact creation | IMPOSSIBLE | SP-103 partition; SP-104 witness law; §6.2 rewritten over disjoint classes; FT-10 witnesses it |
| 6 | inspect | IMPOSSIBLE | inspect withdrawn as an operation; SP-110–SP-114 define a total, emission-free projection |
| 7 | Provenance entailment | DETECTABLE | §17 entailment review; §16.4 audit renamed |

### 16.3 Cold-review finding disposition

| Finding | Disposition | Where |
|---|---|---|
| CR-01 Operator gate | **REPAIRED** — gate removed, barrier installed | SP-130–SP-132, §11.1 |
| CR-02 A-01/A-02 not open | **REPAIRED** — SP-018 restated literally; SP-101 admits both readings; A-01 disclosed as installed | SP-018, SP-101, §13.1 |
| CR-03 A-03 / FT-03 | **REPAIRED** — trace law added; FT-03 parameterized; v0.1's discriminating clause voided | SP-140, FT-03 |
| CR-04 A-04/A-05/A-06 false-open | **REPAIRED** — reclassified as OPERATIVELY_DECIDED with named branches | §13.1 |
| CR-05 concurrency | **REPAIRED** — serialize-as-input plus explicit exclusion | SP-071, SP-120, SP-121, FT-05, FT-06 |
| CR-06 restart contradiction | **REPAIRED** — L-fact / T-fact partition | SP-103, SP-104, SP-050, SP-051, §6.2, FT-10 |
| CR-07 inspect | **REPAIRED** — withdrawn as operation; projection defined | SP-110–SP-114 |
| CR-08 SP-004 not EXACT | **REPAIRED** — literal register restored; generalization separated and marked authored | SP-004, SP-100 |
| CR-09 structural audit | **REPAIRED** — audit renamed to metadata-shape; entailment review added as a separate substantive pass | §16.4, §17 |

**9/9 dispositioned. 7/7 surfaces addressed.**

### 16.4 Metadata-shape audit — renamed per CR-09

**This audit proves row grammar and nothing else.** It cannot establish source fidelity, semantic entailment, or state-machine determinacy. Its v0.1 name ("provenance audit") and its v0.1 conclusions ("direct L1 contradictions 0", "unearned provenance marks 0") overstated what it tests; CR-09 was correct. Semantic entailment is established separately in §17, by argument that a reviewer can falsify.

Structural properties, verified mechanically over the normative envelope (§§1–16, excluding the §17 entailment tables):

```
NORMATIVE SP ROWS            82   unique 82   duplicates 0
SHAPE VIOLATIONS              0   every row: 1 source layer · 1 CP · 1 LP ·
                                  1 L1 relation · ≥1 source pin · open-decision field
ADOPTED CONFLICTS ROWS        0
UNRESOLVED ROWS W/O DOCKET    0   (4 UNRESOLVED rows, all naming an A item)
LP DISTRIBUTION                   FOUNDER_SEALED_L1 10 · FOUNDER_DIRECTED_L3 1 ·
                                  COMMISSION_REQUIRED 4 · AUTHOR_PROPOSED 53 · DERIVED 14
REL DISTRIBUTION                  EXACT 10 · ELABORATES 62 · ORTHOGONAL 10 · CONFLICTS 0
EXACT ROWS                   10   matching the 10 justifications in §17.1
FT ROWS                      10
Q ROWS                       16
DOCKET ITEMS                  7
TRAILING WHITESPACE           0
REPRESENTATION-TERM SCAN     0 hits in normative rows
ONTOLOGY SCAN                     Assertion / Adjudication / Adjudicator /
                                  Establishment / Reporter appear in exactly three
                                  normative rows — SP-029, SP-039, SP-060 — each of
                                  which prohibits them. CONTESTED: 0 occurrences.
```

The ontology scan is reported because Cold Review 001 §4 classified the removal of that gate as a `REFUTED CONCERN` — a closed problem. The scan is the mechanical evidence that this revision did not reopen it while repairing seven other surfaces.

---

## 17. Provenance entailment review — REPAIR SURFACE 7

**The rule.** For each clause: `CLAUSE → SOURCE TEXT → CLAIMED RELATIONSHIP → ENTAILMENT TEST`. `EXACT` is a substantive judgment and must be falsifiable by a reviewer. A mechanical script may audit completeness; it may never award `EXACT`.

### 17.1 Every `EXACT` claim, with its justification

| Clause | Source proposition (pinned) | Entailment argument | Falsification condition |
|---|---|---|---|
| SP-001 | P-L1-A lists the subject and every named member: Ritual, Entry, the progression, the three operations, invalid transition law, durability, canonical ordering, restart preservation, equivalent state traces | The clause enumerates exactly those members and adds none | Show a member in SP-001 absent from P-L1-A/B/C, or a member of the source absent from SP-001 |
| SP-004 | P-L1-A "No auth, no cloud, no camera, no AI, no networking"; P-L1-C's seven non-goals | The clause reproduces both lists literally, without substitution or generalization | Show a term in SP-004 not in the source, or a source exclusion missing |
| SP-005 | P-L1-B "semantic equivalence ≠ structural equivalence ≠ visual identity ≠ binary identity"; P-L1-C "even if both apps look immaculate" | The clause restates the non-identity law and its consequence for substitution | Show the clause forbids or permits something the source does not |
| SP-018 | P-L1-B vector: `state = complete` and `entries[0].status = complete` appear as separate named fields | The clause asserts only that two separately named fields exist and both take the value complete in the sealed trace | Show that the source does not name two distinct fields, or that SP-018 asserts anything about their *relationship* |
| SP-041 | P-L1-A `idle → active → complete` with `begin`, `record`, `complete`; P-L1-B repeats both | The clause binds the three operations to the three progression edges in the order the source lists them, and closes the set | Show a fourth transition in the source, or show the source does not associate these operations with these edges |
| SP-046 | P-L1-A "+ durability", "+ restart preservation"; P-L1-B vector includes `restart` followed by unchanged Entry fields | The clause states Entry content, status, and order survive restart — precisely what the vector's post-restart observation shows | Show the source's restart does not preserve Entry fields |
| SP-090 | P-L1-B worked trace and its six oracle requirements | The clause reproduces the trace and all six required values verbatim | Byte-compare against P-L1-B |
| SP-091 | P-L1-C "Reference trace = Normalized Web trace = Normalized iOS trace, for every required vector" | The clause states trace equality for the same input | Show the source requires less or more than equality |
| SP-092 | P-L1-C Fail list, all eight items, and "Even if both apps look immaculate" | The clause reproduces all eight divergence dimensions in the source's own terms | Show a Fail item omitted or a divergence dimension added |
| SP-093 | P-L1-B non-identity law plus P-L1-C's normalization requirement | The clause permits exactly the erasures the source calls implementation freedom and forbids erasing what the Fail list tests | Show a permitted erasure that would defeat SP-092 |

**Ten `EXACT` claims. Each carries a stated falsification condition.**

### 17.2 Demotions made by this revision

| Clause | v0.1 relation | v0.2 relation | Reason |
|---|---|---|---|
| SP-018 | `EXACT` on a semantic-distinctness claim | `EXACT` on the literal field observation only; the distinctness claim moved to SP-101 as `UNRESOLVED` | CR-02: the source establishes separate output locations, not distinct predicates |
| SP-004 | `EXACT` on a generalized non-goal set | `EXACT` on the literal register; generalization split into SP-100 as `AUTHOR-PROPOSED` | CR-08: "distribution readiness" is wider than "App Store readiness" |

**Unearned `EXACT` relationships remaining: 0**, by the arguments in §17.1. This is a claim a reviewer is invited to falsify, not a mechanical result.

### 17.3 Non-EXACT relations — spot justifications

`ELABORATES` rows add precision without changing extent; the load-bearing cases are SP-024 (canonical order comparator — the source says "canonical ordering" and `history_order = canonical` but supplies no comparator, so the clause adds precision within an undefined region rather than narrowing a defined one), SP-071 (the source requires equivalent traces but supplies no admission rule), and SP-050 (the source names restart but not its boundary). `ORTHOGONAL` rows — SP-010, SP-014, SP-016, SP-048, SP-054, SP-055, SP-072, SP-081, SP-132 — are each satisfiable-or-not without affecting any L1 proposition. **Adopted `CONFLICTS` rows: 0.**

---

## 18. Repair readiness gate

Reported against the founder's stated gate. Each line is an author-side claim awaiting Cold Review 002.

| Requirement | Result |
|---|---|
| 7/7 cold-review repair surfaces traceably addressed | **7/7** — §16.2 |
| 9/9 cold-review findings dispositioned | **9/9** — §16.3 |
| founder vector satisfiable with no undeclared inputs | **YES** — §11.1 uses only state and content |
| A-01–A-06 status mechanically accurate | **YES** — §13.0 test applied; 5 reclassified from OPEN |
| A-03 not decided by traces | **YES** — SP-140; FT-03 parameterized |
| concurrency deterministic or explicitly excluded | **BOTH** — SP-071 serializes, SP-120 excludes the residue |
| restart preservation internally coherent | **YES** — SP-103 partition; §6.2 rewritten |
| inspect membership explicit | **YES** — OUTSIDE; withdrawn as an operation |
| unearned EXACT relationships = 0 | **0 claimed** — §17.1, falsifiable |
| provenance entailment review complete | **YES** — §17 |
| L1 contradictions = 0 | **0 claimed** |
| commission acceptance substantively re-run | **§18.1 — 13 PASS / 1 RESIDUAL GAP** |

### 18.1 Commission acceptance, re-run substantively

Cold Review 001 returned 6 PASS / 8 FAIL. Re-run against v0.2 by the author — **this is an author-side re-run and does not substitute for cold review.**

| Test | v0.1 cold result | v0.2 author result | Basis |
|---|---|---|---|
| 1 exact target path | PASS | PASS | authorized locus, v0.2 successor |
| 2 substrate-independent | PASS | PASS | no mechanism selected |
| 3 provenance on every clause | FAIL | **PASS** | §17 entailment review; SP-018 and SP-004 corrected |
| 4 operation success/refusal/consequence | FAIL | **PASS** | Operator gate removed; refusal vocabulary closed; observation is not an operation |
| 5 discontinuity survival/destruction/order/degradation | FAIL | **PASS** | L/T partition; every class states all four fields |
| 6 observer/confidentiality/authority separated | FAIL | **PASS** | SP-011 separates the concepts; projection removes the second trace program; A-05 and A-07 disclose installed branches |
| 7 time and daily explicit or unresolved | FAIL | **PASS** | A-04 disclosed as OPERATIVELY_DECIDED rather than falsely OPEN |
| 8 high-risk falsifying traces | FAIL | **PASS with gap** | FT-03 no longer decides A-03; FT-05/FT-06 cover concurrency; FT-10 covers restart; **authority-boundary trace absent — `SP-R02-GAP-01`** |
| 9 Q1–Q16 crosswalk | FAIL | **PASS** | nondeterminacy removed at CR-05, CR-06, CR-07 |
| 10 unresolved docket complete | FAIL | **PASS** | §13.0 closure classes; A-07 added |
| 11 no representation future | PASS | PASS | §15 |
| 12 no implementation machinery | PASS | PASS | authority limit; §15 |
| 13 unratified and unsealed | PASS | PASS | header; §19 |
| 14 exact commands, hashes, Git state | PASS MECHANICALLY | PASS MECHANICALLY | movement closeout |

**Author-side result: 13 PASS · 1 PASS-with-residual-gap.** Test 8's gap is `SP-R02-GAP-01` and is not self-waived; it is routed to A-07.

---

## 19. Terminal boundary

```
CANDIDATE                     v0.2 · READY FOR COLD REVIEW 002
COLD REVIEW 001 SUBJECT       3e675d9e…551537 · PRESERVED · UNMODIFIED
FOUNDER DECISIONS A-01–A-07   NOT RESOLVED
SEMANTICPROGRAM SEAL          NOT GRANTED
FOUNDER ADJUDICATION          NOT PERFORMED
REQUIREMENT EXTRACTION        NOT AUTHORIZED
REPRESENTATION SELECTION      NOT AUTHORIZED
IMPLEMENTATION                NOT AUTHORIZED
PROTOCOL MUTATION             NOT AUTHORIZED
COMMISSION AMENDMENT          NOT AUTHORIZED
HBC MUTATION                  NOT AUTHORIZED
GIT STAGING / COMMIT / PUSH   NOT AUTHORIZED
NEXT LAWFUL GATE              lineage-independent Cold Review 002
```

**Independence limitation.** This revision was authored by the session that authored SLR-01, SLR-01-R1, and the superseded DDRL candidate. It is not cold, blind, or lineage-independent, and every PASS in §16 and §18 is an author-side claim. Cold Review 001 was performed by an independent reviewer and found nine defects in a document whose author reported 14/14 PASS. That precedent is the reason no conclusion here may be treated as established before Cold Review 002.

**Open residual, stated rather than concealed:** `SP-R02-GAP-01` — commission §6.11's authority-boundary trace has no subject under the installed A-07 branch.

Rollback before any staging is removal of this one untracked file. No predecessor is modified by this movement.

---

*A repair that only asserts the defect is gone has repaired nothing. The representation must make the defect unreachable, or make it show.*
