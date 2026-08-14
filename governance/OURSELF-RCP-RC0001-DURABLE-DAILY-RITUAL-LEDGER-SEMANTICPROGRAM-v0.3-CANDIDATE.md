# RC-0001 DURABLE DAILY RITUAL LEDGER SEMANTICPROGRAM v0.3
## Bounded revision candidate · SP-R03 · repairs Cold Review 002

**STATUS** CANDIDATE_READY_FOR_REVIEW · FOUNDER_DECISION_REQUIRED
**RATIFICATION** NOT RATIFIED · NOT SEALED · NOT COLD-REVIEWED
**PROOF SUBJECT** Durable Daily Ritual Ledger
**AUTHORIZED PATH** `governance/OURSELF-RCP-RC0001-DURABLE-DAILY-RITUAL-LEDGER-SEMANTICPROGRAM-v0.3-CANDIDATE.md`
**REVISION SUBJECT** v0.2 `611a782e7abdf323de6567497d4da372ff011142d44de16c6f53c2a9d1feb007` — preserved unmodified as the exact subject of Cold Review 002
**REPAIR MANDATE** Cold Review 002 `bdd8c218ade5e37f0b23605ec2f789ae6f72b74855aa036eb9905039fc46167e` · six surfaces
**AUTHORITY LIMIT** Bounded semantic revision only. No founder adjudication, seal, extraction, representation selection, RealityIR, implementation, RC-0001 execution, protocol mutation, commission amendment, source-custody mutation, HBC mutation, staging, or commit.

**GOVERNING REPAIR CRITERION** — unchanged

> A repair counts only if the normative representation either makes the defect **impossible** or makes it **explicitly detectable**.

**SURGICAL CONSTRAINT.** Cold Review 002 confirmed five mechanisms survived attack. They are carried forward **unchanged**: the L-fact / T-fact partition, the ordered admission model, `view(n)` outside trace semantics, FT-03's A-03 neutrality, and the absence of the Assertion / Adjudication / Establishment gate. No repair below alters any of them.

**THE ARCHITECTURAL CONSTRAINT ON REPAIR 1.** Capability resolution must become **visible to proof without becoming permission to reinterpret semantic law**. The Operator gate is not restored. `begin`, `record`, and `complete` retain state-and-content-only preconditions.

---

## 0. Authority, scope, and provenance

### 0.1 FD-01 governing order — unchanged

1. **L1** · the 2026-08-12 founder seal controls the RC-0001 proof-subject scope;
2. **L3** · later founder acts are valid founder-directed input but do not supersede L1;
3. **L2** · the authoring commission controls this movement's procedure and exact output path;
4. **L4** · reconciliation and review records are derived evidence, not sources of founder meaning.

### 0.2 Source pins

| Pin | Layer | Source | Exact identity |
|---|---|---|---|
| P-L1-A | L1 | Founder-sealed RC-0001 scope | Codex session `019ff7ee-9e35-7101-915e-74a0aae7d677` · ordinal 59 · text SHA-256 `4cfd687b2ea9cdbcf366c29a60b124e76cf0f9cce9fb4de897d812b69b3f4bb5` |
| P-L1-B | L1 | Founder constitutional laws and worked trace | same session · ordinal 72 · text SHA-256 `796a3588fbd8fbc611b62f6bba2267d462dd42f92f865a876f82e3387190e221` |
| P-L1-C | L1 | Founder proof topology, pass/fail predicates, stage contract, prohibitions, non-goals | same session · ordinal 85 · text SHA-256 `e951c1bc4f3fdb0fdfe4f133624acfd521dfedb7240bbdb80a0fe4147d82b8e3` |
| P-L1-CONTAINER | L1 custody | Raw founder-session container | SHA-256 `cee97abe168b011e8cc2bf1d69009d755f8c744998302c76743ac432a7d81ebe` |
| P-L2 | L2 | SemanticProgram authoring commission | SHA-256 `9a04124a25ec3dc9c281d73a4f6bce7ecb7a0619a0d9890f9a51fd5ce5dcc04e` |
| P-L3-A | L3 | Later founder SemanticProgram direction | Claude session `fcf1e66c-294f-4669-82e7-f83271b22970` · message `c563940d-dccb-4b24-88f3-ae3ef4b55537` · text SHA-256 `f0029a9ad5d362e9e8b5a35410da15babc0008b8d82299c2bb95dfde386f4802` |
| P-L3-FD01 | L3 | FD-01 source-authority act | Codex session `019ffad0-ee9c-74f1-85f9-a9efb60db01c` · message `msg_019ffbc7-7932-7b70-bfee-dbc65ba3aa43` · text SHA-256 `72a96c051531f1b7cbefd7a1061d8f6f68222594d4f7426d865e03da0bdaa771` |
| P-L4-R1 | L4 | Corrected source-lineage reconciliation | SHA-256 `a506352ae82bd889034b5972dc2b090185aac3c6ac58f6bbc083f7d4614e68c6` |
| P-L4-CR1 | L4 | Cold Review 001 | SHA-256 `54de4a52ffa4f63086cbc19d30e7d7beb49b5c61cc1b37a2605da187e626276f` |
| P-L4-CR2 | L4 | Cold Review 002 | SHA-256 `bdd8c218ade5e37f0b23605ec2f789ae6f72b74855aa036eb9905039fc46167e` |
| P-V02 | Revision subject | v0.2 candidate | SHA-256 `611a782e7abdf323de6567497d4da372ff011142d44de16c6f53c2a9d1feb007` |
| P-V01 | Evidence only | v0.1 candidate | SHA-256 `3e675d9ebd1e8bbb25193625ef9ca784146d8d639e57d5f5fe9dfaee46551537` |

### 0.3 Provenance model — unchanged

CP (commission, binding): `FOUNDER-DIRECTED` · `RCP-CONSTRAINED` · `AUTHOR-PROPOSED` · `UNRESOLVED`.
LP (FD-01 lineage, additive): `FOUNDER_SEALED_L1` · `FOUNDER_DIRECTED_L3` · `COMMISSION_REQUIRED` · `AUTHOR_PROPOSED` · `DERIVED`.
L1 relation (substantive entailment judgment): `EXACT` · `ELABORATES` · `ORTHOGONAL` · `CONFLICTS`. See §17.

### 0.4 Normative envelope — unchanged

Only **SP** rows are normative. **FT** rows are derived witnesses adding no law. **A** rows are docket questions.

---

## 0.5 Repair register — the six mandated surfaces

| # | Surface | Repair mode | Governing clauses |
|---|---|---|---|
| 1 | Capability leak (SP-132) | **IMPOSSIBLE** — total disposition accounting over the presented sequence makes silent loss nonconforming | SP-150–SP-154, SP-091 |
| 2 | Refusal nondeterminacy | **IMPOSSIBLE** — fixed refusal precedence yields exactly one outcome per admitted input | SP-160, SP-031, SP-033, SP-035, SP-043 |
| 3 | Docket misclassification | **DETECTABLE** — sharpened T(A) test rerun over all items, admissibility criterion made explicit | §13.0, §13.1 |
| 4 | EXACT overclaims | **DETECTABLE** — all claims re-audited against raw source by nine attacks; three demoted, one split | §17 |
| 5 | SP-R02-GAP-01 | **CLOSED** — trace coverage added for the existing confirmation boundary | FT-11, §12.2 |
| 6 | Evidence miscounts | **IMPOSSIBLE** — evidence generated by an embedded reproducible auditor | §16.4 |

---

## 1. Identity, purpose, and non-goals

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-001 | RC-0001's proof subject is one substrate-neutral Durable Daily Ritual Ledger whose preserved meaning includes Ritual, Entry, the progression idle → active → complete, begin, record, complete, invalid transition law, durability, canonical ordering, restart preservation, and equivalent state traces. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-A | — |
| SP-002 | The program governs logical state and observable semantic consequence; no user interface, runtime, language, serialization, storage engine, network, or device mechanism is part of its meaning. | L2 | RCP-CONSTRAINED | COMMISSION_REQUIRED | ELABORATES | P-L1-B, P-L1-C, P-L2 §2.1 | — |
| SP-003 | A successful ledger transition establishes what the ledger records and no more. Entry status complete means the program's complete transition succeeded for that Entry-bearing cycle; it is not independent proof that an external-world act occurred. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L3-A, P-L4-R1 | A-05 |
| SP-004 | **REVISED (CR-002 B.4).** The founder-stated exclusions are, literally and in full: from P-L1-A, "No auth, no cloud, no camera, no AI, no networking"; from P-L1-B, "No cloud. No authentication. No generative AI. No camera. No networking. No seductive product surface hiding compiler defects"; from P-L1-C, the first proof is not beautiful UI, production architecture, App Store readiness, sophisticated Swift, sophisticated React, generalized storage abstraction, or a reusable design system. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-A, P-L1-B, P-L1-C | A-08 |
| SP-100 | Any generalization of SP-004's literal register — "distribution readiness" for App Store readiness, "target-code sophistication" for sophisticated Swift and React — is authored elaboration carrying no founder seal. Where a generalization and the literal register differ in extent, the literal register governs. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-C | — |
| SP-005 | A conforming embodiment preserves the acceptance predicates of this SemanticProgram through normalized semantic observation; visual similarity, matching component structure, or matching binaries cannot substitute for semantic equality. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-B, P-L1-C | — |

### 1.1 Intended participant outcome

The ledger supplies one durable, ordered account of the content recorded while a Ritual is active and the completion state reached through lawful operations. It remains usable after a bounded restart and across daily recurrence, without importing an observer-adjudication ontology into the core state machine.

---

## 2. Semantic actors, capability, and the program boundary

### 2.0 Capability resolution — REPAIR SURFACE 1

**The v0.2 defect.** SP-132 placed capability filtering outside the SemanticProgram boundary and called it `ORTHOGONAL`. Cold Review 002 B.1-F1 showed the relocation was not a removal: for presented sequence `begin; record("A"); record("B"); complete`, an embodiment whose pre-boundary filter drops `record("B")` yields Entries `[A]` while an unfiltered embodiment yields `[A, B]`, and **neither violates any SP clause**, because SP-091 compared "the same SemanticProgram input" and the two inputs were no longer the same after filtering. This defeats executable semantic preservation and contradicts P-L1-B constitutional law 3:

> **"Capability loss is typed and explicit. No emitter silently 'figures something out.'"**

**The v0.3 repair — total disposition accounting.** Capability resolution remains outside transition law. What changes is that it can no longer be invisible: every presented element must be accounted for, and the accounting is a proof-visible T-fact.

```
PRESENTED SEQUENCE  (the required vector — what conformance compares)
        │
        ▼
CAPABILITY RESOLUTION           may not delete; must dispose
        │
        ├── ADMITTED ────────────────► SemanticProgram transition law
        │
        └── CAPABILITY_UNSUPPORTED ──► typed T-fact, proof-visible
            CAPABILITY_DEGRADED        (never reaches transition law)
```

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-150 | **NEW · REPAIR 1.** RC-0001's conformance input is a **presented sequence** of invocations and discontinuity boundaries. Every element of the presented sequence receives exactly one disposition in the program's record: `ADMITTED`, `CAPABILITY_UNSUPPORTED`, or `CAPABILITY_DEGRADED`. The disposition function is total: no presented element may be absent from the record. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B, P-L4-CR2 B.1-F1 | A-07 |
| SP-151 | **NEW · REPAIR 1.** A non-`ADMITTED` disposition is a typed T-fact naming the presented element and its loss class. It occupies a position in the trace, is observable by the conformance witness, and is never silent. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B, P-L1-C | — |
| SP-152 | **NEW · REPAIR 1 (barrier).** Conformance is compared over the **presented sequence**, not over the post-resolution admitted sequence. Two embodiments conform only if every presented element receives the same disposition and every `ADMITTED` element produces the same outcome. An embodiment that admits an element another disposes as unsupported has already diverged. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-C, P-L4-CR2 B.1-F1 | — |
| SP-153 | **NEW · REPAIR 1 (the architectural distinction).** Capability resolution decides only whether a presented element reaches the SemanticProgram. It never decides whether an admitted element's transition is legal, never alters an L-fact, and never supplies or withholds permission to any Participant. **Capability decision ≠ transition permission.** | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L2 §6.2 | A-07 |
| SP-154 | **NEW · REPAIR 1 (L1 law 3).** Removal of a presented element without a typed disposition is nonconforming, not an implementation freedom. An embodiment that silently narrows the presented sequence fails RC-0001 regardless of the ledger state it reaches. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B law 3 | — |

**Withdrawn:** SP-132. Its `ORTHOGONAL` justification in v0.2 §17.3 was false, as Cold Review 002 B.1-F2 established.

**Why the counterexample is now impossible.** Presented `begin; record("A"); record("B"); complete`. Embodiment I must emit `CAPABILITY_UNSUPPORTED(record("B"))` as a typed T-fact; embodiment W emits `ADMITTED(record("B"))`. SP-152 compares dispositions over the presented sequence, so the divergence is visible at the element that caused it, before any Entry-count difference arises. The Operator gate is not restored: `record` still has no invoker precondition.

### 2.1 Actors

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-010 | A Participant is a logical principal presented to the SemanticProgram. Participant identity proof and authentication mechanics are outside RC-0001. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L3-A | — |
| SP-011 | Invocation capability and observation capability are conceptually independent: possessing either does not imply possessing the other. This models the commission's required separation. It does not make either a precondition of any RC-0001 operation. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L2 §6.2, P-L3-A | A-07 |
| SP-130 | RC-0001 admits **no invocation-capability precondition** on begin, record, or complete. An admitted invocation's acceptance or refusal is determined solely by state legality and content presence. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L4-CR1 CR-01 | A-07 |
| SP-131 | No capability, permission, role, authority, or admission model may cause any presented sequence to produce a disposition or outcome other than the one this SemanticProgram assigns it. A model that can do so is nonconforming, not an alternative reading. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B, P-L3-FD01 | — |
| SP-013 | The designated RC-0001 conformance witness must be able to observe every L-fact in SP-019 at an identified operation position through the SP-110 projection, and the complete T-fact stream including dispositions. Witness observation is not an operation. | L2 | AUTHOR-PROPOSED | COMMISSION_REQUIRED | ELABORATES | P-L1-B, P-L1-C, P-L2 §6.7 | — |
| SP-014 | No ledger fact is required by this SemanticProgram to be hidden from any Participant. Confidentiality and access-control policy are not semantic guarantees of RC-0001. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L2 §6.7 | — |
| SP-016 | No RC-0001 operation grants, transfers, revokes, or establishes a Participant's authority. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L2 §6.8 | A-05 |
| SP-028 | Refusal is produced by the SemanticProgram's state and content law; no Participant has discretionary power to convert a refused attempt into an accepted one, or an accepted attempt into a refused one. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-C, P-L2 §6.2 | — |
| SP-029 | No confirmer, amender, invalidator, Reporter, Assertion, Adjudicator, Adjudication, or Establishment construct exists, because no confirmation, amendment, invalidation, or world-fact adjudication operation is admitted. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L2 §6.2, P-L3-FD01 | A-05, A-06 |

---

## 3. Semantic facts and identity

### 3.0 The L-fact / T-fact partition — CARRIED FORWARD UNCHANGED

Cold Review 002 B.2 evaluated the six-step trace `begin; record("Reflect"); restart; restart; complete; restart` and found the partition does not leak. It is preserved verbatim.

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-103 | The SemanticProgram's observable facts are partitioned into two disjoint classes. **L-facts** are the state the program preserves. **T-facts** are the monotonic witness record of what was presented and what the program answered. No fact belongs to both classes. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-B, P-L1-C | — |
| SP-019 | The complete **L-fact** set is: Ledger identity; Ritual identity; current-state value; current DaySlot ordinal; ordered pending contributions while present; durable ordered Entries with content and status; and canonical history order. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-A, P-L1-B | A-01, A-03, A-04 |
| SP-102 | **REVISED.** The complete **T-fact** set is: the operation position ordinal; the ordered disposition record required by SP-150; the ordered operation-outcome stream; restart-boundary markers; and the derived illegal-transition count. T-facts are append-only and strictly monotonic. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-B, P-L1-C | — |
| SP-104 | A witness about preservation may not count as mutation of the thing whose preservation it witnesses. Emission of a T-fact never constitutes a change to any L-fact, and no preservation obligation ranges over T-facts. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-B | — |
| SP-105 | **NEW.** No transition evaluation may read a T-fact. Operation outcomes are determined by current L-facts, the operation, and its content alone. This makes the partition's one-way direction mechanically checkable rather than asserted. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-B, P-L4-CR2 B.2 | — |

### 3.1 Facts and identity clauses

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-017 | One SemanticProgram instance governs one logical Ledger identity and one Ritual-under-test identity. Daily recurrence continues that Ritual identity rather than silently creating a new Ritual definition. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L3-A | — |
| SP-018 | The founder worked trace exposes a top-level `state` value and a per-Entry `status` value as two separately named observation fields, both of which take the value complete in that trace. This clause states that literal observation and nothing further. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-B | — |
| SP-101 | Whether the two fields of SP-018 denote one predicate under two projections or two causally coupled predicates is not determined by their separate appearance. Both readings are admitted. Any clause that would exclude either reading is nonconforming until A-02 is adjudicated. | L4 DERIVATION | UNRESOLVED | DERIVED | ELABORATES | P-L1-B, P-L4-CR1 CR-02 | A-02 |
| SP-020 | After a successful complete, each successful record in that active interval corresponds to exactly one durable Entry whose content equals the recorded content and whose status is complete. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B | A-03 |
| SP-021 | An Entry's semantic identity is its Ritual identity plus its canonical history position. Two successful record acts with equal content remain two distinct Entries because their canonical positions differ. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B, P-L1-C | A-03 |
| SP-022 | A successful record creates an observable ordered pending contribution immediately. Whether that contribution already bears Entry identity is left open by SP-026. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B | A-03 |
| SP-023 | A DaySlot is a monotonically ordered logical recurrence partition whose ordinal is semantic. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L3-A, P-L2 §6.9 | A-04 |
| SP-024 | Canonical history order is ascending DaySlot ordinal, then ascending successful-record order within the active interval associated with that DaySlot. Equal content never collapses distinct positions. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L1-C | A-04 |
| SP-025 | A completed Entry is immutable: no admitted operation deletes it, rewrites its content, changes its status, or replaces its canonical position. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-C | A-06 |
| SP-026 | The candidate does not decide whether the pending contribution created by record already has Entry identity or acquires Entry identity only through complete. Both models are normatively admitted; see SP-140. | L4 DERIVATION | UNRESOLVED | DERIVED | ELABORATES | P-L1-A, P-L1-B, P-L4-CR1 CR-03 | A-03 |
| SP-027 | The candidate does not decide whether or how a logical DaySlot maps to a civil calendar, locale, or timezone. | L4 DERIVATION | UNRESOLVED | DERIVED | ELABORATES | P-L1-A, P-L2 §6.9 | A-04 |

### 3.2 Identity distinctions that must remain observable

current `state` versus Entry `status` (as fields — SP-101 governs their relationship) · pending contribution versus durable Entry · two equal-content records versus one · same L-facts at different positions · accepted operation versus refused attempt · **admitted element versus capability-disposed element** · ledger completion versus independently verified world event.

---

## 4. Operations

### 4.0 Refusal precedence — REPAIR SURFACE 2

**The v0.2 defect.** At `state = idle`, `pending = empty`, operation `complete`, both failure conditions hold. SP-035 said "`INVALID_TRANSITION` or `NO_RECORDED_CONTENT`" without disambiguating, and SP-043 then produced `illegal_transition_count` of 1 or 0 for identical input. Cold Review 002 B-F3 confirmed identical input with two legal outputs, and FT-08 was asserting one branch — the CR-03 pattern surviving in a second row.

**The v0.3 repair — fix the mechanism, then let the trace derive from it.**

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-160 | **NEW · REPAIR 2.** Every admitted invocation yields exactly one normative result, determined in fixed precedence: **(1) state legality is evaluated first** — if the operation is not lawful from the current state, the result is refusal `INVALID_TRANSITION` and evaluation stops; **(2) content conditions are evaluated only if the operation is state-legal** — yielding `MISSING_CONTENT` for record without content, or `NO_RECORDED_CONTENT` for complete with no pending contribution; **(3) otherwise the operation is accepted.** No admitted input state and operation may yield more than one result. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L4-CR2 B-F3 | — |
| SP-161 | **NEW · REPAIR 2 (precedence justification).** State legality precedes content evaluation because the invalid-transition law is founder-sealed at P-L1-A while the content-presence refusals are authored. A founder-sealed law is evaluated before an authored refusal class. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L4-CR1 §4 | — |
| SP-043 | **REVISED.** The derived illegal-transition count increments by exactly one when and only when the SP-160 result is `INVALID_TRANSITION`. Because SP-160 yields exactly one result per admitted input, the count is deterministic. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-B, P-L1-C | — |

### 4.1 State-changing operations

Preconditions are state-and-content only. No invoker qualification appears.

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-030 | begin expresses intent to enter an active Ritual interval. It succeeds when and only when current state is idle; success changes current state to active, preserves all durable Entries, creates no Entry, and emits an accepted begin outcome. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B | A-01 |
| SP-031 | **REVISED.** A refused begin leaves every L-fact unchanged and emits a rejected begin outcome whose single reason is determined by SP-160. begin has no content condition, so its only refusal reason is `INVALID_TRANSITION`. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-A, P-L1-B, P-L2 §6.4 | — |
| SP-032 | record(content) expresses intent to add one content-bearing contribution to the active interval. It succeeds when and only when current state is active and content is present as a semantic value; success appends one pending contribution in admission order, leaves state active and durable Entries unchanged, and emits an accepted record outcome. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B | A-03 |
| SP-033 | **REVISED.** A refused record leaves every L-fact unchanged and emits a rejected record outcome whose single reason is determined by SP-160: `INVALID_TRANSITION` when state is not active, otherwise `MISSING_CONTENT`. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-A, P-L1-B, P-L2 §6.4 | — |
| SP-034 | complete expresses intent to close the active interval. It succeeds when and only when current state is active and at least one pending contribution exists; success changes current state to complete, causes one complete Entry per pending contribution to exist in canonical order, clears the pending projection, preserves all earlier Entries, and emits an accepted complete outcome. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B | A-01, A-02, A-03 |
| SP-035 | **REVISED.** A refused complete leaves every L-fact unchanged and emits a rejected complete outcome whose single reason is determined by SP-160: `INVALID_TRANSITION` when state is not active, otherwise `NO_RECORDED_CONTENT`. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-A, P-L1-B, P-L2 §6.4 | — |

### 4.2 Observation — CARRIED FORWARD UNCHANGED

Cold Review 002 confirmed `view(n)` purity holds. `inspect` remains withdrawn as an operation.

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-110 | Observation is a total function `view(n)` from any operation position `n` to the complete L-fact set as of `n`. It is a projection of program state, not an operation, not an attempt, and not an event. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L2 §6.7, P-L3-A | — |
| SP-111 | `view` is defined at every operation position, emits no T-fact, occupies no position, never contributes to the illegal-transition count, and can never alter the acceptance, refusal, ordering, disposition, or outcome of any invocation. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L4-CR1 §7.2 | — |
| SP-112 | `view` is total and deterministic: `view(n)` has exactly one value for a given presented sequence and position. Two observations at the same position are the same value. Observations at different positions are different observations, not disagreement. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-C, P-L2 §6.7 | — |
| SP-113 | Staleness is not a semantic property of the program. A substrate delivering `view(n)` when the greatest admitted position is `m > n` has delivered a correct observation of position `n`. No currentness obligation is required, and none is imposed. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L2 §6.7 | — |
| SP-114 | The RC-0001 conformance witness compares `view(n)` and the T-fact stream across substrates. Because observation emits nothing, no read can influence pass or fail except through the values it reports. | L2 | AUTHOR-PROPOSED | COMMISSION_REQUIRED | ELABORATES | P-L1-B, P-L1-C | — |

### 4.3 Operation-wide law

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-037 | Each operation is semantically atomic. No conforming observation may return a partially applied begin, record, or complete. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-C, P-L2 §6.4 | — |
| SP-038 | Every accepted operation is distinguishable from a no-op by a changed L-fact set or an accepted outcome. Every rejected attempt is distinguishable from absence of an attempt by its rejected T-fact outcome. Every capability-disposed element is distinguishable from an absent element by its disposition T-fact. | L2 | AUTHOR-PROPOSED | COMMISSION_REQUIRED | ELABORATES | P-L1-C, P-L2 §7 | — |
| SP-039 | begin, record, and complete require no Assertion, Reporter, Adjudicator, Adjudication, Establishment, contest status, capability, or authoritative-world-answer precondition. The founder trace must succeed without any such construct. | L3 | FOUNDER-DIRECTED | FOUNDER_DIRECTED_L3 | ELABORATES | P-L3-FD01 | — |

---

## 5. State model and invariants

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-040 | Initial current state is idle, pending count is zero, and durable Entry history may be empty or may contain Entries preserved from earlier DaySlots. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B | A-01 |
| SP-041 | **REVISED (CR-002 B.4).** The founder-sealed transitions of the three sealed operations are idle —begin→ active, active —record→ active, and active —complete→ complete. No other transition of begin, record, or complete is lawful. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-A, P-L1-B | — |
| SP-042 | Within one DaySlot, complete is terminal for state-changing operations. A later DaySlot boundary may make a new daily cycle idle under SP-053 without deleting prior Entries. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L3-A | A-01, A-04 |
| SP-044 | Pending-contribution order equals accepted record admission order. complete preserves that relative order when the corresponding Entries join history. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L1-C | A-03 |
| SP-045 | Canonical history order is total, stable across every contemplated discontinuity, and independent of wall-clock timestamps. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L1-C | A-04 |
| SP-046 | Once complete, an Entry and its content, status, and relative order survive a contemplated restart. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-A, P-L1-B | A-06 |
| SP-047 | The candidate does not decide which entity owns current state. SP-101 governs the operation/state completion relationship; A-01 governs ownership. | L4 DERIVATION | UNRESOLVED | DERIVED | ELABORATES | P-L1-B, P-L4-R1 | A-01, A-02 |
| SP-048 | **REVISED.** No correction, amendment, deletion, supersession, invalidation, scheduling, or world-fact adjudication transition exists, and no fourth state-changing operation is admitted. The closure over operations beyond the sealed three is an authored minimality choice, not a founder-sealed prohibition. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L1-A, P-L1-C, P-L3-FD01 | A-05, A-06 |
| SP-049 | Once complete, an Entry and its content, status, identity, and relative order survive later DaySlot transitions. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L3-A | A-04, A-06 |

---

## 6. Discontinuities — CARRIED FORWARD UNCHANGED

Cold Review 002 confirmed the restart witness separation is coherent under the six-step trace. Preserved verbatim.

| Clause | Discontinuity and boundary | L-facts that survive | L-facts that must not survive | Ordering | Permitted degradation | T-fact effect | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SP-050 | restart means a page/runtime reload, process restart, or device restart followed by re-entry to the same logical Ledger identity with its durable semantic state available. | Ledger and Ritual identity; current state; DaySlot; pending contributions; completed Entries; canonical order. | None. Volatile presentation state is not an L-fact. | Pending and history order identical. | None. An L-fact survives exactly or the restart law is violated. | Exactly one restart-boundary T-fact; position advances by one. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L1-C | — |
| SP-051 | A restart invokes no operation and changes no L-fact. Its entire semantic footprint is the single T-fact required by SP-050. | All L-facts existing immediately before interruption. | None. | Identical before and after. | None. | Exactly one boundary marker. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B | — |
| SP-052 | Total destruction of the logical Ledger identity or loss of all durable semantic state is not a restart under SP-050. RC-0001 makes no survival claim across that different event. | Not specified; outside the contemplated class. | Not specified. | Not specified. | The event may not be relabeled as a conforming restart. | Not specified. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L4-CR1 §4 | — |
| SP-053 | DaySlot boundary increments the DaySlot ordinal. idle remains idle; complete becomes idle for a new cycle; active remains active and keeps its originating DaySlot until complete. | Ledger and Ritual identity; pending contributions; completed Entries; origin DaySlots; canonical order. | No completed Entry or pending contribution is destroyed. The prior current-state value need not survive when complete becomes idle. | History order preserved; later Entries sort after earlier DaySlots. | None. | One boundary marker; position advances by one. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L3-A | A-01, A-04 |
| SP-054 | A change in who is observing is not a discontinuity of this program. Because observation is the total projection SP-110, there is no observer state to lose. | Every L-fact. | None. | Unchanged. | None. | None. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L2 §6.7 | — |
| SP-055 | **REVISED.** Temporary disconnection means a Participant cannot present an invocation for an interval. An invocation never presented is not part of the presented sequence and has no program presence. An invocation presented but capability-disposed is accounted for under SP-150 and is not "absent." | All L-facts. | None. | Preserved. | Unpresented intent is never promoted into any fact; presented intent is never silently removed. | Dispositions per SP-150. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L3-A, P-L2 §6.6 | — |

### 6.1 Restart preservation witness

At operation position `n`, a restart yields position `n+1`:

```
view(n+1) = view(n)                       every L-fact identical
T-facts(n+1) = T-facts(n) + one restart-boundary marker
```

Disjoint fact classes (SP-103), so both hold. SP-105 additionally forbids any transition evaluation from reading a T-fact, so the partition's one-way direction is a normative clause rather than a prose claim.

---

## 7. Observer, confidentiality, authority, and confirmation

### 7.1 Observation matrix

| L-fact class | Who must observe | Who must not | Agreement law | Position law |
|---|---|---|---|---|
| current state and DaySlot | designated conformance witness | nobody semantically prohibited | `view(n)` single-valued | different `n` may differ; each position-identified |
| ordered pending contributions | designated conformance witness while present | nobody semantically prohibited | `view(n)` single-valued | as above |
| completed Entries, content, status, identity, order | designated conformance witness | nobody semantically prohibited | `view(n)` single-valued | later positions may add Entries, never rewrite earlier ones |

| T-fact class | Observation law |
|---|---|
| dispositions, operation outcomes, restart markers, illegal-transition count | witnessed as an append-only stream; the same presented sequence yields the same stream |

### 7.2 Authority and confirmation — the boundary Pass C identified

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-060 | A state counts as achieved when its lawful state transition succeeds. No separate confirmation, acceptance, Adjudication, Establishment, capability, or authoritative-world-answer act is required. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L3-FD01 | A-05 |
| SP-061 | record preserves supplied content as ledger content. It does not convert that content into an externally verified claim, a completion observation, or an authority decision. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L3-A, P-L4-R1 | A-05 |
| SP-064 | No unconfirmed-intent state can masquerade as accepted world fact: pending content is visibly pending, and completed Entry status denotes ledger completion only under SP-003. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L2 §6.8 | A-03, A-05 |

**The commission's authority boundary lives here.** Commission §6.2 speaks of "power to confirm it" and §6.8 asks "which states count without confirmation… who can confer it." Cold Review 002 Pass C established that this is **confirmation authority**, not invocation capability. SP-060 answers it: nothing confers; lawful transition suffices. SP-003 draws the boundary: ledger completion is not world truth. FT-11 now falsifies it.

---

## 8. Time, ordering, admission, and recurrence — CARRIED FORWARD UNCHANGED

Cold Review 002 found the concurrency repair airtight. Preserved verbatim.

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-071 | The SemanticProgram's admitted input is a totally ordered sequence. Every admitted invocation receives exactly one position ordinal at admission, before any transition evaluation. Transition legality is evaluated strictly in that order. The order is part of the input, never a result of interpretation. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B, P-L1-C | — |
| SP-120 | A presentation that does not yield a total admission order is not RC-0001 SemanticProgram input. Substrate simultaneity must be resolved into an admission order before the boundary; that resolution is input construction, not a semantic choice. A conformance vector that fails to determine the admission order of two attempts is malformed and may not be run. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-C | — |
| SP-121 | Two embodiments given the same presented sequence necessarily receive the same admission order, because the order is a component of that input. Divergent Entry sets arising from different serializations are impossible for one input; observed divergence is a conformance failure, not a permitted reading. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-B, P-L1-C | — |
| SP-070 | Wall-clock time and timestamps are not semantic order sources. Admission position ordinal, DaySlot ordinal, and accepted record order are the only ordering facts. Admission order is supplied as input and never derived from a clock. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-C, P-L2 §6.9 | A-04 |
| SP-083 | Conflicting state-changing attempts are resolved solely by their admission order under SP-071. Each is evaluated against the state produced by its predecessors. No last-writer, recency, or wall-clock rule may replace transition legality. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-C | — |
| SP-072 | A late invocation is judged against the state at its admission position, not against the state that existed when Participant intent was formed. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L3-A, P-L2 §6.9 | — |
| SP-073 | Repeated successful record invocations are distinct accepted acts even when content is equal. A repeated begin or complete after the first state change is refused by the invalid-transition law. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L2 §6.10 | — |
| SP-074 | Daily recurrence creates a new DaySlot while preserving the same Ledger and Ritual identities and all earlier Entries. A missed idle DaySlot creates no Entry. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L3-A | A-04 |
| SP-075 | An active interval crossing a DaySlot boundary retains its originating DaySlot for the Entries produced when it later completes. No second active interval begins while current state remains active. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L3-A | A-01, A-04 |

---

## 9. Failure, duplication, conflict, and recovery

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-080 | **REVISED.** Every admitted invocation yields exactly one accepted or rejected outcome under SP-160. Refusal never silently becomes success and never partially mutates any L-fact. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B, P-L1-C, P-L2 §6.10 | — |
| SP-081 | Retrying a rejected operation is a new presented element at a later position. A prior refusal neither reserves a future success nor suppresses the retry's outcome. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L2 §6.10 | — |
| SP-082 | **REVISED.** Re-delivery has no hidden deduplication semantics. Two admitted record invocations produce two pending contributions and, after complete, two Entries. Transport-duplicate suppression is a construction of the presented sequence and must be reflected in it, not performed silently at the boundary. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L2 §6.10, P-L1-B law 3 | — |
| SP-084 | Recovery from a contemplated restart is exact L-fact continuation under SP-050 and SP-051. Recovery may not synthesize missing Entries, discard pending contributions, reorder history, or reset complete to idle. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L1-C | — |

---

## 10. L3-under-L1 reconciliation

Carried forward from v0.2 with two disposition updates. L3 remains valid founder-directed input, never promoted into L1 law.

| L3 construct or area | Disposition in v0.3 | L1 relation | Governing clause |
|---|---|---|---|
| Ledger · Ritual | program container and Ritual-under-test | EXACT | SP-001, SP-017 |
| RitualOccurrence / PlannedOccurrence | not adopted as core entities | ELABORATES if adopted | A-01 |
| CompletionObservation | not required for the founder trace | ORTHOGONAL if non-gating | A-05 |
| Correction | not adopted | ORTHOGONAL if it preserves L1 history | SP-025, A-06 |
| Day | logical DaySlot; civil mapping open | ELABORATES | SP-023, A-04 |
| Participant / Observer | **capability gates no operation; capability loss is typed and proof-visible** | ELABORATES | SP-010, SP-011, SP-130, SP-150–SP-154, A-07 |
| AuthorityDecision | not required to achieve L1 state | ORTHOGONAL if non-gating | A-05 |
| define / schedule ritual | outside the sealed three-operation core | ORTHOGONAL | SP-048 |
| observe / inspect | the SP-110 projection; withdrawn as an operation | ELABORATES | SP-110–SP-114 |
| record completion / noncompletion | record accepts opaque content; asserts no world fact | ELABORATES | SP-032, SP-061 |
| observation / authority separation | independent concepts; neither gates an operation | ELABORATES | SP-011, SP-130, SP-153 |
| recorded intent versus accepted fact | pending content distinct from completed Entry; neither is verified world fact | ELABORATES | SP-022, SP-064 |
| observer septuple | answered by projection, position, and agreement clauses | ELABORATES | SP-110–SP-114 |
| PENDING / CORROBORATED / CONTESTED / REJECTED / SUPERSEDED / STANDING | not adopted; core state remains idle / active / complete | ORTHOGONAL | SP-018, SP-041 |
| cross-day-boundary | a contemplated DaySlot discontinuity, not a fourth operation | ELABORATES | SP-053, SP-074, SP-075 |
| reconcile observations | not adopted; observation is a projection | ORTHOGONAL | SP-110, SP-111, A-05 |
| Assertion / Adjudication / Establishment ontology | **remains rejected as a precondition of RC-0001** | CONFLICTS when it gates the founder trace | SP-029, SP-039, SP-060 |

**Closed and not reopened.** Cold Review 001 §4 and Cold Review 002 both confirm the adjudication gate is correctly absent. No repair in SP-R03 required or reintroduced it.

---

## 11. Founder-sealed trace and acceptance predicates

**REPAIR SURFACE 4 applied here.** v0.2's SP-090 combined the founder's worked example with a normative requirement and strengthened the founder's modality from "might require" to "yields," and added a precondition the founder never wrote. Cold Review 002 B.4 and B.4-F6 confirmed both. v0.3 splits the clause so the reproduction and the requirement carry different relations.

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-090 | **REVISED · reproduction only.** The founder's worked example is: for event trace `begin`, `record("Reflect")`, `complete`, `restart`, the oracle **might require** `state = complete`, `entries.count = 1`, `entries[0].content = "Reflect"`, `entries[0].status = complete`, `history_order = canonical`, `illegal_transition_count = 0`; and if both substrates satisfy that normalized semantic trace, they conform. This clause reproduces that example and its stated modality, adding nothing. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-B | — |
| SP-094 | **NEW · the normative requirement.** RC-0001 adopts the SP-090 example as a required vector: from initial state idle with **empty durable Entry history** and empty pending, the presented sequence `begin; record("Reflect"); complete; restart` must produce exactly those six values, with every element disposed `ADMITTED`. The initial-condition qualification and the promotion from "might require" to "must produce" are authored, not founder-sealed. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B, P-L4-CR2 B.4-F6 | A-01, A-02, A-03 |
| SP-091 | **REVISED (CR-002 B.4).** For every required vector, the reference semantic trace and each normalized target trace must be equal. Comparison is over the presented sequence per SP-152. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-C | — |
| SP-092 | Semantic preservation fails if any of these diverges: legal transition behavior; illegal transition behavior; durable state; restart semantics; ordering; failure semantics; normalization; acceptance predicates. Divergence fails the proof even if both embodiments look immaculate. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-C | — |
| SP-093 | **REVISED · demoted.** Normalization may erase structural, visual, binary, runtime, and presentation differences, but may not erase any distinction needed to evaluate SP-090 through SP-092. The generalization from the founder's specific examples — differing SwiftUI/React lifecycles, differing persistence engines, differing internal object graphs — to "runtime and presentation differences" is authored. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B, P-L1-C | — |

### 11.1 Founder-trace satisfiability derivation

| Step | Governing clause and precondition | Required result |
|---|---|---|
| presentation | SP-150 | four elements presented; all disposed `ADMITTED` |
| initial | SP-040, SP-094 | state idle; pending zero; durable history empty |
| `begin` | current state is idle — SP-030, SP-160 step 3 | accepted; state active |
| `record("Reflect")` | state active; content present — SP-032, SP-160 step 3 | accepted; one pending contribution; state active |
| `complete` | state active; ≥1 pending — SP-034, SP-160 step 3 | accepted; state complete; one complete Entry "Reflect"; pending cleared |
| `restart` | same Ledger identity — SP-050, SP-051 | every L-fact preserved; one boundary T-fact |
| observation | SP-110 `view` at final position | the six SP-090 values; all three attempts state-legal, so `illegal_transition_count = 0` |

**No step supplies a Participant, role, capability, Operator, Observer, Assertion, Adjudication, or Establishment.** Every precondition is discharged by the state, the content string, and the presented sequence itself.

---

## 12. Falsifying traces

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-140 | A falsifying trace may test admitted semantics. It may not manufacture semantics. Where a docket item admits more than one normative model, no FT row may treat either model's observable consequence as falsifying. Such a row must restrict itself to consequences shared by all admitted models, or state its branch condition and remain inert until adjudication. An FT row that discriminates an admitted alternative is void, not authoritative. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L2 §6.11, P-L4-CR1 CR-03 | — |

### 12.1 Trace suite

| Trace | Input | Expected normalized observation | Falsifying observation | Basis |
|---|---|---|---|---|
| FT-01 · founder success and restart | `begin → record("Reflect") → complete → restart` | all four elements `ADMITTED`; state complete; one Entry "Reflect" status complete; canonical history; zero illegal transitions; one restart boundary | any missing/extra Entry; changed content, status, or order; state other than complete; nonzero illegal count; any need for a capability, role, or adjudication input | SP-039, SP-090, SP-094, SP-130 |
| FT-02 · invalid transition refusal | idle → `record("Reflect")` | rejected `INVALID_TRANSITION` per SP-160 step 1; state idle; no pending; no Entry; illegal count 1 | record accepted; any Entry or pending appears; refusal absent; any L-fact changes; reason other than `INVALID_TRANSITION` | SP-041, SP-033, SP-043, SP-160 |
| FT-03 · active restart — branch-parameterized | `begin → record("Reflect") → restart → complete` | **Shared by every admitted A-03 model, and the only falsifiable content of this row:** after restart, state active and one pending contribution "Reflect" in unchanged order; after complete, exactly one complete Entry "Reflect". | restart resets to idle; pending dropped or altered; pending order changed; lawful complete prevented; more or fewer than one Entry after complete | SP-050, SP-051, SP-084, SP-140 |
| | **A-03 branch note — inert until adjudicated.** Under A-03(A) the pending contribution already bears Entry identity across the restart; under A-03(B) it does not. Neither observation falsifies preservation. | | | |
| FT-04 · observation position | one record succeeds between positions `n` and `n+1`; observe at both | `view(n)` and `view(n+1)` each single-valued, differing by the new contribution; observing appends no T-fact and changes no L-fact | two different values at one position; an observation appending an outcome, advancing position, or altering the illegal count | SP-110–SP-113 |
| FT-05 · concurrency exclusion | active with pending `["A"]`; a vector presenting `record("B")` and `complete` without a determined admission order | the vector is **malformed** and must not be run | the vector is run and yields a result; or two embodiments run it and report different Entry sets as both conforming | SP-071, SP-120, SP-121 |
| FT-06 · ordered concurrency | the same two invocations, admitted in the stated order `record("B") < complete` | both accepted; Entries `[A, B]`; illegal count unchanged | any embodiment producing `[A]` with a rejected record for this input, i.e. silently re-serializing a supplied order | SP-071, SP-083, SP-121 |
| FT-07 · duplicate content and order | `begin → record("Reflect") → record("Reflect") → complete` | two distinct complete Entries, equal content, record order, distinct canonical positions | one Entry due to content deduplication; reversed or unstable order; ambiguous identity | SP-021, SP-073, SP-082 |
| FT-08 · **REVISED · derives from SP-160** | trace A: active with one pending → `complete`; trace B: state complete, pending empty → `complete` | A accepted, changes state and history. B: SP-160 step 1 applies first because state is not active, so the single reason is `INVALID_TRANSITION`, no L-fact changes, illegal count +1. | both normalize as "complete"; refusal loses T-fact presence; B creates or changes an Entry; **B emits `NO_RECORDED_CONTENT`, or emits either reason nondeterministically** | SP-034, SP-035, SP-038, SP-160 |
| FT-09 · day recurrence and active carry | trace A: complete → DaySlot boundary; trace B: active with one pending → DaySlot boundary | A becomes idle with history intact; B remains active, retains pending and origin DaySlot; both increment DaySlot | history deletion; active reset; pending loss; identical outcome for A and B; changed canonical order | SP-053, SP-074, SP-075 |
| FT-10 · restart fact partition | any state at position `n` → restart | `view(n+1) = view(n)` exactly; T-facts gain exactly one boundary marker; position advances by exactly one | any L-fact differs across the boundary; or no boundary marker emitted; or more than one emitted | SP-050, SP-051, SP-103, SP-104 |
| FT-11 · **NEW · confirmation-authority boundary** | `begin → record("X") → complete`, presented with **no confirming actor, authority, or external attestation anywhere in the sequence** | all elements `ADMITTED`; state complete; one Entry "X" status complete; the ledger asserts nothing about whether the practice occurred in the world | **any** of: completion withheld pending a confirmation act; a distinct confirmed/unconfirmed surface exposed on state or Entry; Entry status complete presented as evidence the external act occurred; a confirming role required to exist for the trace to succeed | SP-003, SP-060, SP-064, P-L2 §6.2, §6.8 |
| FT-12 · **NEW · capability disposition visibility** | presented `begin → record("A") → record("B") → complete`, where one embodiment's substrate cannot support `record("B")` | that embodiment disposes `CAPABILITY_UNSUPPORTED(record("B"))` as a typed T-fact and diverges visibly from an embodiment disposing it `ADMITTED` | `record("B")` absent from the disposition record; Entries `[A]` and `[A, B]` both reported conforming; capability loss inferable only from the Entry count | SP-150–SP-154, SP-091, SP-152 |

**Commission §6.11 coverage:** successful operation FT-01 · refused operation FT-02, FT-08 · contemplated discontinuity FT-03, FT-09, FT-10 · visibility boundary FT-04 · **authority boundary FT-11** · temporal/duplicate/conflict edge FT-06, FT-07 · operationally similar but semantically different FT-08.

### 12.2 SP-R02-GAP-01 — closed, with its cause corrected

**v0.2 misstated the cause.** §12.2 of v0.2 asserted that removing the Operator gate destroyed the authority-boundary trace and that the commission requirement and the CR-01 repair were in genuine tension. Cold Review 002 Pass C answered **D**: commission §6.11's "authority boundary" means **confirmation** authority, never invocation capability. v0.1's FT-05 was a capability trace wearing an authority label, so withdrawing it removed nothing §6.11 required. There was no tension — there was a coverage gap over a boundary that already existed at SP-003 and SP-060, and a misdiagnosis of it.

```
GAP CLASS        trace-coverage defect, not an authority-ontology defect
BOUNDARY         confirmation authority — SP-003, SP-060, SP-064
COVERAGE         FT-11
NEW SEMANTICS    none invented
A-07 RELATION    none; A-07 governs invocation capability, a different question
STATUS           CLOSED
```

No authority ontology was invented to make commission test 8 green.

---

## 13. Founder decision docket

### 13.0 Closure classification — REPAIR SURFACE 3

**The v0.2 defect.** Cold Review 002 B.3-F5 found A-01 labeled `OPERATIVELY_DECIDED` while its own note said its alternatives were "not excluded in principle" — the OPEN branch by the document's own rule — with structurally identical A-04 also labeled `OPERATIVELY_DECIDED`. The test was sound; its application was not, because the test never said what makes an alternative *admissible*.

**Sharpened test.** An alternative is **admissible** only if it is realizable as observable semantics under the current L-fact set. An alternative that asserts a semantic fact the program does not carry is not a conforming implementation choice — it is a request to change SP-019.

> **T(A):** Considering only admissible alternatives, can two embodiments adopting different ones both satisfy every normative SP clause?
> `YES for all` → OPEN · `YES for some` → PARTIALLY_DECIDED · `NO for all but one` → OPERATIVELY_DECIDED

This resolves the v0.2 inconsistency without altering any normative semantics: A-01's alternatives A/B/C each assert an ownership relation as semantic fact, and SP-019 carries no owner coordinate, so they are inadmissible on the same ground as A-04's B/C. **The label was right; the note was wrong.** Corrected below.

### 13.1 Classification result — rerun over all items

| Item | Question | Admissible alternatives | Closure class | Installed branch |
|---|---|---|---|---|
| A-01 | Which entity owns the observable state? | **D only.** A, B, C each require an owner coordinate as semantic fact; SP-019 carries none. | **OPERATIVELY_DECIDED** | D — state exposed without owner attribution |
| A-02 | Relation between invoking complete and observing state complete? | **A, B, C all admissible.** SP-018 states only the literal field observation; SP-101 expressly admits both readings. | **OPEN** | none |
| A-03 | Does record create an Entry, mutate one, or create a non-Entry contribution? | **A and B admissible; C inadmissible** — SP-022 requires the contribution be *created*, excluding a pre-existing Entry mutated by record. | **PARTIALLY_DECIDED** | none between A and B |
| A-04 | What maps a logical DaySlot to a civil day? | **A only.** B and C require timezone or participant-relative day as semantic facts; SP-019 carries none. | **OPERATIVELY_DECIDED** | A — DaySlot only |
| A-05 | Does RC-0001 need a world-fact observation and authority layer? | **A only.** B requires world-fact and authority-decision facts absent from SP-019, and SP-029/SP-048 admit no such operation. | **OPERATIVELY_DECIDED** | A — no additional layer |
| A-06 | Can completed Entry meaning later be corrected? | **A only.** B and C require a correction operation; SP-048 admits none. | **OPERATIVELY_DECIDED** | A — no correction |
| A-07 | **REFRAMED.** Does RC-0001 admit an invocation-capability precondition, and how is capability loss accounted for? | **(a) only.** (b) and (c) require an invoker-qualification fact the founder vector does not supply; SP-131 forbids any model that changes a disposition or outcome. | **OPERATIVELY_DECIDED** | (a) — no invocation gate; **capability loss typed, visible, and totally accounted under SP-150** |
| A-08 | **NEW.** P-L1-A excludes "no AI"; P-L1-B excludes "No generative AI." These differ in extent. Which governs RC-0001's exclusion boundary? | **Both admissible** — SP-004 reproduces both literally and resolves neither; no normative clause depends on the difference. | **OPEN** | none |

**Summary: OPEN 2 · PARTIALLY_DECIDED 1 · OPERATIVELY_DECIDED 5 · all eight FOUNDER_DECISION_REQUIRED.**

No normative semantics were changed to make a docket label true. The only change in this section is the admissibility criterion, which makes the existing labels derivable rather than asserted — and A-08, which exists because SP-004's re-audit surfaced a genuine source-internal difference.

### 13.2 Decision detail — changes from v0.2 only

**A-01** · Corrected note: alternatives A, B, and C are **inadmissible**, not "not excluded in principle." Selecting one requires adding an owner coordinate to SP-019, which is a founder act, not an implementation choice.

**A-07** · Reframed by Repair 1. The question is no longer only "is there a gate" but "how is capability loss accounted for." Installed answer: no gate, and total typed accounting. Consequence of (b) or (c): the sealed trace ceases to be self-sufficient and requires an input the founder never wrote.

**A-08** · New. Alternatives: (a) the narrower "no generative AI" governs, leaving non-generative AI unexcluded; (b) the broader "no AI" governs; (c) both stand and the intersection governs. Consequence: none for v0.3's semantics — no clause depends on it — but it bounds what a later RC-0001 target may contain. Recommendation: **none offered.** SP-004 reproduces both phrasings verbatim rather than resolving a founder difference by authorship.

All other items retain their v0.2 alternatives and consequences.

---

## 14. Extraction-readiness crosswalk

| Instrument question | Clauses or witnesses | Readiness |
|---|---|---|
| Q1 · truth after operation success | SP-030, SP-032, SP-034, SP-160; FT-01 | ANSWERABLE |
| Q2 · truth after refusal | SP-028, SP-031, SP-033, SP-035, SP-043, SP-160; FT-02, FT-08 | ANSWERABLE |
| Q3 · intermediate state | SP-037, SP-080 | ANSWERABLE — partial state forbidden and unobservable |
| Q4 · effect distinguishable from no-op | SP-038, SP-043; FT-02, FT-08, FT-12 | ANSWERABLE |
| Q5 · facts surviving each discontinuity | SP-050–SP-055; FT-03, FT-09, FT-10 | ANSWERABLE |
| Q6 · facts that must not survive | SP-050–SP-055 | ANSWERABLE |
| Q7 · surviving relative order | SP-044–SP-046, SP-050–SP-055 | ANSWERABLE |
| Q8 · permitted degradation | SP-050–SP-055, SP-113, SP-150 | ANSWERABLE — no L-fact degradation; capability degradation is typed |
| Q9 · required observer | SP-013, SP-110, SP-114, §7.1 | ANSWERABLE |
| Q10 · multi-party observability | SP-014, SP-112, §7.1 | ANSWERABLE |
| Q11 · observer agreement | SP-112; FT-04 | ANSWERABLE |
| Q12 · required unobservability | SP-014, §7.1 | ANSWERABLE — none required |
| Q13 · authority confirmation | SP-029, SP-060, SP-130, SP-153; FT-11 | ANSWERABLE |
| Q14 · required unconfirmed intent | SP-022, SP-026, SP-061, SP-064; FT-11 | ANSWERABLE |
| Q15 · authority transfer or establishment | SP-016, SP-039, SP-060 | ANSWERABLE — no operation transfers authority |
| Q16 · erasure versus falsification | SP-090–SP-094; FT-01–FT-12; §3.2 | EVALUABLE by a later extraction movement |

---

## 15. Representation firewall and namespace check

The author has seen representation-lineage material and makes no coldness claim. No semantic choice is justified by the vocabulary or capability of any representation under later test.

Subject-local meanings: `canonical` means only the SP-024 comparator; `durable` means only the SP-050–SP-052 survival obligations; `position` means only the SP-071 admission ordinal; `pending` means only the SP-022 pre-complete effect; `view` means only the SP-110 projection; `disposition` means only the SP-150 accounting.

The candidate contains no database schema, storage-engine choice, serialization shape, interface flow, target-language construct, RealityIR, RequiredVectors, tolerance class, emitter design, resolver, oracle, representation option, F-05 tier selection, HBC accommodation, or implementation backlog.

---

## 16. Author-side conformance

### 16.1 Sealed-scope coverage

| Gate | Required L1 surface | Evidence | Result |
|---|---|---|---|
| S-01 | Ritual and Entry | SP-001, SP-017, SP-020–SP-022, SP-026 | PASS |
| S-02 | idle → active → complete; begin, record, complete | SP-018, SP-030–SP-035, SP-041 | PASS |
| S-03 | invalid-transition and failure law | SP-031, SP-033, SP-035, SP-043, SP-160, SP-080–SP-083 | PASS |
| S-04 | durable Entry and restart preservation | SP-046, SP-050–SP-052, SP-084; FT-03, FT-10 | PASS |
| S-05 | canonical ordering, equivalent traces, acceptance predicates | SP-024, SP-044, SP-045, SP-090–SP-094 | PASS |
| S-06 | founder exclusions, non-goals, concrete founder trace | SP-004, SP-005, SP-090 | PASS |
| S-07 | **NEW** — constitutional law 3: capability loss typed and explicit | SP-150–SP-154; FT-12 | PASS |

**SEALED-SCOPE COVERAGE 7/7.**

### 16.2 Cold Review 002 finding disposition

| Finding | Disposition | Where |
|---|---|---|
| CR-08 (PARTIALLY_CLOSED from CR-001) | **CLOSED** — SP-004 now reproduces all three pins in full including "No seductive product surface hiding compiler defects"; the `no AI` / `no generative AI` extent difference is docketed as A-08 rather than resolved by authorship | SP-004, A-08, §17.1 |
| B.1-F1 capability leak | **REPAIRED** — total disposition accounting; comparison over presented sequence | SP-150–SP-154, SP-152, SP-091 |
| B.1-F2 false ORTHOGONAL on SP-132 | **REPAIRED** — SP-132 withdrawn entirely | §2.0 |
| B-F3 refusal nondeterminacy | **REPAIRED** — SP-160 precedence; SP-043 derives; FT-08 derives | SP-160, SP-161, SP-043, FT-08 |
| B.3-F5 A-01 misclassification | **REPAIRED** — admissibility criterion added; label derivable; note corrected | §13.0, §13.1, §13.2 |
| B.4 SP-004 EXACT overclaim | **REPAIRED** — full literal register | SP-004 |
| B.4 SP-090 EXACT overclaim | **REPAIRED** — split into SP-090 (reproduction, founder modality preserved) and SP-094 (requirement, ELABORATES) | SP-090, SP-094 |
| B.4 SP-091 EXACT overclaim | **REPAIRED** — restated as "for every required vector"; this is also the capability-leak closure | SP-091, SP-152 |
| B.4-F6 undeclared founder input | **REPAIRED** — "empty current cycle" replaced by explicit "empty durable Entry history", declared authored | SP-094 |
| B-F8 ontology miscount | **REPAIRED** — evidence regenerated by embedded auditor, not hand-corrected | §16.4 |
| B-F9 ORTHOGONAL miscount | **REPAIRED** — same | §16.4, §17.3 |
| Pass C · SP-R02-GAP-01 | **CLOSED** — trace coverage added; cause corrected; no new semantics | FT-11, §12.2 |

**12/12 dispositioned.** Additionally, SP-093 was demoted to `ELABORATES` on the author's own re-audit — not a review finding, but the same defect class.

### 16.3 What was deliberately not touched

L-fact / T-fact partition · ordered admission model (SP-071, SP-120, SP-121) · `view(n)` semantics (SP-110–SP-114) · FT-03 neutrality and SP-140 · Assertion/Adjudication/Establishment prohibition · restart witness separation. Each survived Cold Review 002 attack. SP-102 and SP-105 are additive: SP-102 registers the new disposition record as a T-fact, SP-105 makes the partition's one-way direction normative rather than assumed. Neither weakens the partition.

### 16.4 Mechanical evidence — regenerated, not synchronized

**The law applied:** a mechanical evidence claim must be generated by the measurement it describes, not manually synchronized with it. The two v0.2 miscounts arose from a hand-written count and a case-sensitive scan. Both are replaced by the auditor below, which any reviewer can run.

**Reproduction:** save as `sp-evidence-audit.py`, run `python3 sp-evidence-audit.py <this file>`.

```python
#!/usr/bin/env python3
# SP-EVIDENCE-AUDIT v1 — regenerates every mechanical claim in this section.
# Scope: NORMATIVE ENVELOPE = everything before the "## 17. Provenance entailment" heading.
import sys, re, pathlib
from collections import Counter
txt = pathlib.Path(sys.argv[1]).read_text()
norm = re.split(r'^## 17\. Provenance entailment', txt, flags=re.M)[0]
L = norm.split('\n')
SPROW = r'^\| (SP-\d{3}) '
sp = [l for l in L if re.match(SPROW, l)]
ids = [re.match(SPROW, l).group(1) for l in sp]
FIELDS = {
 'LAYER': r'\| (L1|L2|L3|L4 DERIVATION|AUTHORSHIP UNDER L2) \|',
 'CP':    r'\| (FOUNDER-DIRECTED|RCP-CONSTRAINED|AUTHOR-PROPOSED|UNRESOLVED) \|',
 'LP':    r'\| (FOUNDER_SEALED_L1|FOUNDER_DIRECTED_L3|COMMISSION_REQUIRED|AUTHOR_PROPOSED|DERIVED) \|',
 'REL':   r'\| (EXACT|ELABORATES|ORTHOGONAL|CONFLICTS) \|'}
viol = []
for l, i in zip(sp, ids):
    for k, rx in FIELDS.items():
        if len(re.findall(rx, l)) != 1: viol.append((i, k, len(re.findall(rx, l))))
    if re.search(r'\| CONFLICTS \|', l): viol.append((i, 'ADOPTED_CONFLICTS', 1))
    if re.search(r'\| UNRESOLVED \|', l) and not re.search(r'A-0[1-9]', l):
        viol.append((i, 'UNRESOLVED_NO_DOCKET', 1))
dup = sorted({i for i in ids if ids.count(i) > 1})
def dist(k): return dict(Counter(re.search(FIELDS[k], l).group(1) for l in sp if re.search(FIELDS[k], l)))
ONTOLOGY = r'assertion|adjudicat|establishment|reporter|contested'
onto = [(re.match(SPROW, l).group(1), 'PROHIBITS' if re.search(r'\bno\b|\bnot\b|require no|remains? absent|prohibit', l, re.I) else 'REVIEW')
        for l in sp if re.search(ONTOLOGY, l, re.I)]
REPTERMS = r'\b(SQLite|IndexedDB|SwiftData|Core Data|localStorage|sessionStorage|cookie|SQL|database|filesystem|HTTP|WebSocket|DURABLE_LOCAL|tier|scalar|Option [ABC])\b'
rep = [(re.match(SPROW, l).group(1), m) for l in sp for m in re.findall(REPTERMS, l, re.I)]
ortho = [re.match(SPROW, l).group(1) for l in sp if re.search(r'\| ORTHOGONAL \|', l)]
exact = [re.match(SPROW, l).group(1) for l in sp if re.search(r'\| EXACT \|', l)]
out = [
 f"NORMATIVE_SP_ROWS      {len(sp)}",
 f"UNIQUE_IDS             {len(set(ids))}",
 f"DUPLICATE_IDS          {dup or 'NONE'}",
 f"SHAPE_VIOLATIONS       {viol or 'NONE'}",
 f"LAYER_DIST             {dist('LAYER')}",
 f"CP_DIST                {dist('CP')}",
 f"LP_DIST                {dist('LP')}",
 f"REL_DIST               {dist('REL')}",
 f"EXACT_ROWS             {len(exact)} -> {exact}",
 f"ORTHOGONAL_ROWS        {len(ortho)} -> {ortho}",
 f"ONTOLOGY_ROWS          {len(onto)} -> {onto}",
 f"REPRESENTATION_HITS    {len(rep)} -> {rep or 'NONE'}",
 f"FT_ROWS                {len([l for l in L if re.match(r'^\| FT-\d{2} ', l)])}",
 f"Q_ROWS                 {len([l for l in L if re.match(r'^\| Q\d{1,2} ·', l)])}",
 f"DOCKET_ITEMS           {len([l for l in L if re.match(r'^\| A-0[1-9] \|', l)])}",
 f"TRAILING_WHITESPACE    {len([l for l in txt.split(chr(10)) if l != l.rstrip()])}",
 f"AUDIT_RESULT           {'FAIL' if (viol or dup or rep) else 'PASS'}"]
print('\n'.join(out))
```

**Validation of the auditor itself.** Run against v0.2 (`611a782e…feb007`), it independently reproduces Cold Review 002's *corrected* counts — `ONTOLOGY_ROWS 6` and `ORTHOGONAL_ROWS 10` — against v0.2's own prose claims of 3 and 9. The auditor detects the defect it was built to prevent, on the document that had it.

**Generated output for this file:** §16.5. Any figure in this document that the script contradicts is wrong, and the script governs.

### 16.5 Generated evidence

Produced by running the §16.4 script against this file. Not hand-entered, not reconciled against prose.

```
NORMATIVE_SP_ROWS      90
UNIQUE_IDS             90
DUPLICATE_IDS          NONE
SHAPE_VIOLATIONS       NONE
LAYER_DIST             {'L1': 9, 'L2': 4, 'AUTHORSHIP UNDER L2': 61, 'L4 DERIVATION': 15, 'L3': 1}
CP_DIST                {'FOUNDER-DIRECTED': 10, 'RCP-CONSTRAINED': 1, 'AUTHOR-PROPOSED': 75, 'UNRESOLVED': 4}
LP_DIST                {'FOUNDER_SEALED_L1': 9, 'COMMISSION_REQUIRED': 4, 'AUTHOR_PROPOSED': 61,
                        'DERIVED': 15, 'FOUNDER_DIRECTED_L3': 1}
REL_DIST               {'EXACT': 9, 'ELABORATES': 72, 'ORTHOGONAL': 9}
EXACT_ROWS             9 -> ['SP-001', 'SP-004', 'SP-005', 'SP-018', 'SP-041',
                             'SP-046', 'SP-090', 'SP-091', 'SP-092']
ORTHOGONAL_ROWS        9 -> ['SP-010', 'SP-014', 'SP-016', 'SP-029', 'SP-048',
                             'SP-054', 'SP-055', 'SP-072', 'SP-081']
ONTOLOGY_ROWS          6 -> [('SP-029', 'PROHIBITS'), ('SP-101', 'PROHIBITS'),
                             ('SP-039', 'PROHIBITS'), ('SP-048', 'PROHIBITS'),
                             ('SP-060', 'PROHIBITS'), ('SP-140', 'PROHIBITS')]
REPRESENTATION_HITS    0 -> NONE
FT_ROWS                12
Q_ROWS                 16
DOCKET_ITEMS           8
TRAILING_WHITESPACE    0
AUDIT_RESULT           PASS
```

**Cross-checks a reviewer should run against this output:**

```
EXACT_ROWS            must equal the 9 clauses justified in §17.1        ✓ 9 = 9
ORTHOGONAL_ROWS       is the authoritative enumeration; §17.3 defers to it
ONTOLOGY_ROWS         6 rows, every one classified PROHIBITS
                      (v0.2 prose claimed 3 — the miscount CR-002 B-F8 caught)
FT_ROWS               12 (10 carried forward + FT-11 confirmation boundary
                      + FT-12 capability disposition)
DOCKET_ITEMS          8 (A-01…A-07 + A-08 from SP-004's re-audit)
REPRESENTATION_HITS   0
```

The v0.2 → v0.3 deltas visible in this output are exactly the intended repairs: `ORTHOGONAL` 10 → 9 (SP-132 withdrawn), `EXACT` 10 → 9 (SP-093 demoted), SP rows 82 → 90 (SP-094, SP-105, SP-150–SP-154, SP-160, SP-161 added), FT 10 → 12, docket 7 → 8.

---

## 17. Provenance entailment review — REPAIR SURFACE 4

`EXACT` is a substantive judgment, falsifiable by a reviewer. A mechanical script may audit completeness; it may never award `EXACT`.

**Nine attacks applied to every claim:** missing source member · extra candidate member · narrower proposition · wider proposition · added precondition · removed consequence · changed subject · changed temporal boundary · changed quantifier or modality.

### 17.1 Re-audit of every EXACT claim

| Clause | Source proposition | Attacks applied | Result |
|---|---|---|---|
| SP-001 | P-L1-A: "Durable Daily Ritual Ledger / Ritual / Entry / idle → active → complete / begin / record / complete / + invalid transition law / + durability / + canonical ordering / + restart preservation / + equivalent state traces"; "A substrate-neutral semantic reality" | member-for-member both directions; "substrate-neutral" replaces v0.2's "substrate-independent" to match the source word; v0.2's added "observable" before "progression" **removed** as an unsourced qualifier | **EXACT** · falsify by naming a member in one list and not the other |
| SP-004 | P-L1-A five exclusions; P-L1-B six exclusions; P-L1-C seven non-goals | missing member — **this attack succeeded against v0.2** and is now closed by reproducing all three registers verbatim; extent difference between "no AI" and "No generative AI" is preserved, not resolved, and docketed as A-08 | **EXACT** · falsify by naming a source exclusion absent from SP-004 |
| SP-005 | P-L1-B: "semantic equivalence ≠ structural equivalence ≠ visual identity ≠ binary identity"; P-L1-C: "Even if both apps look immaculate" | no widening: the clause forbids substitution of exactly the three named identity kinds | **EXACT** |
| SP-018 | P-L1-B worked trace: `state = complete` and `entries[0].status = complete` as separately named fields | changed subject — the clause now says "the founder worked trace exposes", not "the founder vector requires"; asserts nothing about the fields' relationship | **EXACT** |
| SP-041 | P-L1-A progression and three operations; P-L1-B repeats both | **widening attack succeeded against v0.2**: "No other state-changing operation transition is lawful" read as forbidding a fourth operation, which L1 does not state. Now scoped to "no other transition **of begin, record, or complete**"; the fourth-operation closure moved to SP-048 as `AUTHOR-PROPOSED` | **EXACT** |
| SP-046 | P-L1-A "+ durability", "+ restart preservation"; P-L1-B vector's post-restart Entry fields | temporal boundary checked: the clause speaks only of a *contemplated* restart per SP-050, matching the vector's single restart | **EXACT** |
| SP-090 | P-L1-B: "the oracle **might require**: …"; "If both substrates satisfy that normalized semantic trace, they conform." | **modality attack succeeded against v0.2** ("might require" → "yields") and **added-precondition attack succeeded** ("From an idle state with an empty current cycle"). Now a pure reproduction preserving "might require"; both the requirement and the initial condition moved to SP-094 as `AUTHOR-PROPOSED` | **EXACT** |
| SP-091 | P-L1-C: "Reference trace = Normalized Web trace = Normalized iOS trace, **for every required vector**" | **changed-subject attack succeeded against v0.2** ("for every required vector" → "the same SemanticProgram input"), which was the capability loophole. Now restated with the founder's subject | **EXACT** |
| SP-092 | P-L1-C Fail list, all eight items, plus "Even if both apps look immaculate" | member-for-member on all eight | **EXACT** |

**Demoted on this re-audit:** SP-093 → `ELABORATES`. The founder named specific implementation freedoms (differing SwiftUI/React lifecycles, differing persistence engines, differing internal object graphs); "runtime and presentation differences" generalizes them. Widening attack succeeds; `EXACT` is withdrawn.

**EXACT claims: 9.** Four of v0.2's ten survived unchanged; three were repaired after a successful attack; one was split; one was demoted; one (SP-001) was tightened by removing an unsourced qualifier.

### 17.2 Attacks attempted and failed

Against SP-005, SP-018, SP-046, and SP-092 all nine attacks were attempted and none succeeded. Reported as failed attacks rather than omitted, so a reviewer can see which claims were tested and held.

### 17.3 Non-EXACT relations

`ELABORATES` rows add precision within regions the source leaves undefined; the load-bearing cases are SP-024 (the source says "canonical ordering" and `history_order = canonical` but supplies no comparator), SP-071 (the source requires equivalent traces but supplies no admission rule), SP-050 (the source names restart but not its boundary), SP-093 (demoted above), SP-094 (the requirement the founder stated as "might require"), and SP-150–SP-154 (the source states capability loss must be typed and explicit but supplies no accounting mechanism).

`ORTHOGONAL` rows are each satisfiable-or-not without affecting any L1 proposition. **The enumeration in this subsection is deliberately not hand-listed** — v0.2's hand-list omitted SP-029 and produced Cold Review 002 B-F9. The auditor's `ORTHOGONAL_ROWS` output in §16.5 is the authoritative enumeration.

**Adopted `CONFLICTS` rows: 0.**

---

## 18. Repair readiness gate

| Requirement | Result |
|---|---|
| CR-001 findings 9/9 CLOSED claimed | **9/9** — CR-08 closed by SP-004's full register |
| CR-002 findings 100% dispositioned | **12/12** — §16.2 |
| capability loss cannot silently remove semantic input | **YES** — SP-150 total accounting; SP-154 nonconformance; FT-12 |
| L1 law 3 contradiction | **0** — SP-154 enforces it directly |
| transition result deterministic for every admitted input | **YES** — SP-160 |
| FT-08 derives from SP law | **YES** — derives from SP-160 step 1 |
| A-01–A-07 classification test rerun | **YES** — all eight, with admissibility criterion; A-08 added |
| EXACT claims all substantively re-audited | **YES** — §17.1; 9 claims, 3 repaired, 1 split, 1 demoted |
| SP-R02-GAP-01 closed by trace coverage | **YES** — FT-11; no new semantics |
| mechanical evidence regenerated reproducibly | **YES** — §16.4 auditor, validated against v0.2 |
| L/T partition unchanged | **YES** — plus SP-105 strengthening the one-way direction |
| concurrency unchanged | **YES** |
| `view(n)` unchanged | **YES** |
| FT-03 neutrality unchanged | **YES** |
| old authority/adjudication gate remains absent | **YES** — SP-029, SP-039, SP-060 |

**Every line above is an author-side claim.** Cold Review 001 found nine defects in a document self-reporting 14/14 PASS; Cold Review 002 found six more in its successor. No conclusion here is established before Cold Review 003.

---

## 19. Terminal boundary

```
CANDIDATE                     v0.3 · READY FOR COLD REVIEW 003
COLD REVIEW 001 SUBJECT       3e675d9e…551537   PRESERVED · UNMODIFIED
COLD REVIEW 002 SUBJECT       611a782e…feb007   PRESERVED · UNMODIFIED
FOUNDER DECISIONS A-01–A-08   NOT RESOLVED
SEMANTICPROGRAM SEAL          NOT GRANTED
FOUNDER ADJUDICATION          NOT PERFORMED
REQUIREMENT EXTRACTION        NOT AUTHORIZED
REPRESENTATION SELECTION      NOT AUTHORIZED
IMPLEMENTATION                NOT AUTHORIZED
PROTOCOL MUTATION             NOT AUTHORIZED
COMMISSION AMENDMENT          NOT AUTHORIZED
HBC MUTATION                  NOT AUTHORIZED
GIT STAGING / COMMIT / PUSH   NOT AUTHORIZED
NEXT LAWFUL GATE              lineage-independent Cold Review 003
```

**Independence limitation.** Authored by the session that authored v0.2, SLR-01, and SLR-01-R1. Not cold, not blind, not lineage-independent.

Rollback before any staging is removal of this one untracked file. No predecessor is modified by this movement.

---

*Capability may be refused. It may not be forgotten. The difference between those two is the whole compiler.*
