# RC-0001 DURABLE DAILY RITUAL LEDGER SEMANTICPROGRAM v0.5
## Bounded blocker-resolution candidate · SP-R05 · repairs Cold Review 004

**STATUS** CANDIDATE_READY_FOR_COLD_REVIEW_005 · FOUNDER_DECISION_REQUIRED
**RATIFICATION** NOT RATIFIED · NOT SEALED · NOT COLD-REVIEWED
**PROOF SUBJECT** Durable Daily Ritual Ledger
**AUTHORIZED PATH** `governance/OURSELF-RCP-RC0001-DURABLE-DAILY-RITUAL-LEDGER-SEMANTICPROGRAM-v0.5-CANDIDATE.md`
**REVISION SUBJECT** v0.4 `7c680b0286d79f8c6af162223bdfe62789f0123a5e28e28dcf855873df2cf48f` — preserved unmodified as the exact subject of Cold Review 004
**REPAIR MANDATE** Cold Review 004 `7ce5feac4bc20c7dd7987e368e397912db0627203e85a5705d5144fff96d1a50` · `CHANGES_REQUIRED` · **CR3-B01 CLOSED** · 1 BLOCKING · 11 MATERIAL · 5 MINOR · 8/15 threshold lines met
**OPERATIVE STATE** INSELFACTION `ISA-20260814-RC0001-CR004-004`
**AUTHORITY LIMIT** Bounded blocker resolution against Cold Review 004 only. **This is not authority for a broad SemanticProgram redesign, and specifically not authority to invent a capability vocabulary.** No founder adjudication, seal, extraction, representation selection, RealityIR, capability-resolver implementation, RC-0001 execution, protocol or RCP/F-05 mutation, commission amendment, source-custody mutation, HBC mutation, staging, or commit. No founder decision is resolved by authorship.

**THE PRIMARY QUESTION, ANSWERED BEFORE ANY REPAIR WAS MADE**

> Can capability loss be made mechanically typed **without inventing semantic vocabulary that neither L1 nor the admitted source lineage authorizes?**

**`CR4-01 REPAIRABILITY: B · SOURCE_SUFFICIENT_WITH_DERIVATION`** — see §0.6. Repair was therefore performed in this movement. Had the answer been C, D or E, this document would carry `BLOCKED_BY_FOUNDER_OR_SOURCE_DECISION` and no semantic installation.

**CR3-B01 IS PRESERVED CLOSED.** Cold Review 004 closed it independently — the first blocker closure in this cascade established by a reviewer rather than claimed by an author. **No clause bearing on it was reopened.** SP-043, SP-102 and SP-094's sequence-scoping are carried forward unchanged except for CR4-02's DaySlot pin, which adds an initial-condition coordinate and touches no part of the count's derivation.

**GOVERNING REPAIR CRITERION** — unchanged

> A repair counts only if the normative representation either makes the defect **impossible** or makes it **explicitly detectable**.

**AND THE RULE EARNED ACROSS THREE REVIEWS**

> Changing the description of a defect is not repairing the mechanism that permits it.

**BLOCKER PRECEDENCE.** CR3-B01 controls this gate and was repaired first, in the mandated order: root cause → affected normative mechanism → minimum structural repair → the counterexample that broke v0.3 → re-run. Only then were the remaining findings addressed. The root cause was a **derived count with an increment rule but no scope**; the minimum structural repair is to scope the T-fact set to one presented sequence and make the required vector a presented sequence in its own right. No founder-sealed meaning, commission law, or unresolved founder decision had to be changed to do it — so this movement does **not** return `BLOCKED_BY_FOUNDER_OR_SOURCE_DECISION`.

**SURGICAL CONSTRAINT.** Cold Review 003 confirmed these mechanisms survived attack. They are carried forward **unchanged**: the L-fact / T-fact partition and T→L non-interference, ordered admission, `view(n)` purity, restart witness separation, FT-03's A-03 neutrality, deterministic refusal precedence (18/18 `EXACTLY_ONE`), the Assertion / Adjudication / Establishment prohibition, and the L1-governs-L3 lineage. **A fourth revision must not become an excuse to churn previously proven surfaces**; where such a clause is touched at all, it is to restore text v0.3 deleted or to repair a clause v0.3's own edit falsified, and §16.3 records the CR-003 verdict that protects each one.

**THE ARCHITECTURAL CONSTRAINT.** Capability resolution must become **visible to proof without becoming permission to reinterpret semantic law**. The Operator gate is not restored. `begin`, `record`, and `complete` retain state-and-content-only preconditions, SP-153 keeps capability decision outside transition permission, and SP-105 forbids any transition evaluation from reading a T-fact.

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
| P-L4-CR3 | L4 | **Cold Review 003 — this movement's repair mandate** | SHA-256 `d9afbcb47f9813430ea763126f80aa25e617012ef80aa6996e0c03d33dc848b1` |
| P-V03 | Revision subject | v0.3 candidate | SHA-256 `55c590ead44e38248a7f97405c8cb23740018df4bd9b154a8a0fd3df99dd7f8e` |
| P-V02 | Evidence only | v0.2 candidate | SHA-256 `611a782e7abdf323de6567497d4da372ff011142d44de16c6f53c2a9d1feb007` |
| P-V01 | Evidence only | v0.1 candidate | SHA-256 `3e675d9ebd1e8bbb25193625ef9ca784146d8d639e57d5f5fe9dfaee46551537` |

### 0.3 Provenance model — unchanged

CP (commission, binding): `FOUNDER-DIRECTED` · `RCP-CONSTRAINED` · `AUTHOR-PROPOSED` · `UNRESOLVED`.
LP (FD-01 lineage, additive): `FOUNDER_SEALED_L1` · `FOUNDER_DIRECTED_L3` · `COMMISSION_REQUIRED` · `AUTHOR_PROPOSED` · `DERIVED`.
L1 relation (substantive entailment judgment): `EXACT` · `ELABORATES` · `ORTHOGONAL` · `CONFLICTS`. See §17.

### 0.4 Normative envelope — unchanged

Only **SP** rows are normative. **FT** rows are derived witnesses adding no law. **A** rows are docket questions.

---

## 0.6 CR4-01 repairability adjudication — the first output of SP-R05

**Question put:** is capability loss individuable from already-admitted semantics, or does typing it require authoring the vocabulary that makes the types meaningful?

**Answer: `B · SOURCE_SUFFICIENT_WITH_DERIVATION`.** The individuating basis exists in admitted, digest-verified source and required no invention. What is *derived* is the identification of RC-0001's requirement set with this document's own clause set — necessary because the source names "semantic requirement" as an entity of RealityIR, which does not exist and which this movement may not create.

| Grounding | Where it already exists |
|---|---|
| Loss is indexed **per semantic requirement** | RCP v0.1 §5.2 `OUTPUT` — *"a CapabilityDecision per semantic requirement"*; `SEMANTIC SOURCE MAP` — *"every decision references the RealityIR requirement it answers"* |
| A **closed** decision vocabulary already exists | RCP §5.3 — `SUPPORTED` `SUBSTITUTED` `DEGRADED` `ABSENT` `REFUSED` |
| Totality | RCP `INV-RC-CAP-1` — *"Every semantic requirement receives exactly one decision. A requirement with no decision is a compilation error, not a default."* |
| **Injective distinction** — the missing calibration | RCP `INV-RC-KERNEL-4` — *"No admitted construct may encode a distinction already encoded by another admitted construct."* |
| Loss resolves backward **to a SemanticProgram rule** | P-L1-C's sealed Semantic Source Map — `CapabilityDecision → RealityIR transition → SemanticProgram rule`; sealed as `TRACEABILITY REQUIREMENT` |
| The same pattern already adjudicated one layer over | F-05 v0.2 `INV-OBS-PER-2` — *"A substrate that cannot SHALL say so **at the named tier**"* |

**Provenance of the grounding record.** RCP v0.1 draft, SHA-256 `1aa3698c29ca9d471390d8943ab64afd7e5a5d943645062fe64451ba0938c776`, **recomputed** and matching the digest the authoring commission names as a `GOVERNING RECORD`. It is admitted lineage, not a document reached for because it was convenient.

**Why not A.** "Semantic requirement" is named by RCP as a RealityIR entity. Identifying it with this document's clause identities is a derivation, disclosed at SP-167 rather than presented as source.

**Why not C.** No founder decision must be made for the repair to be lawful. The repair *removes* an authored vocabulary and replaces it with references into a set the document already publishes; it is a narrowing, and it creates no new semantic terms.

**Why not D.** The genuinely protocol-level objects — RCP §5.3's decision vocabulary and the CapabilityDecision record schema reserved to R-04 — are **not** installed, extended or pre-empted. SP-171 declines them explicitly and docket item **A-10** records the reconciliation as reserved. This document supplies only the requirement identities a decision is taken *per*, which is a precondition of R-04 rather than an encroachment on it.

**Why not E.** No source contradiction was found. RCP §5, P-L1-C's source map and F-05's precedent all point the same way.

**The line that was not crossed.** No capability ontology was authored. No enum of substrate limitations — `STORAGE_LIMITATION`, `UI_DEGRADATION`, `NETWORK_RESTRICTION` or any sibling — appears anywhere in this document. Had individuation required inventing such a set, the correct return was `BLOCKED_BY_FOUNDER_OR_SOURCE_DECISION`, and it would have been returned.

---

## 0.5 Repair register — Cold Review 004, in blocker-first order

Full per-finding detail is at **§16.2**. Cold Review 004's own headline and §10 verdict block report "NEW MATERIAL 7"; its §4 carries twelve numbered findings — `CR4-01` BLOCKING plus `CR4-02`…`CR4-12`, eleven MATERIAL — plus five MINOR. **This register dispositions the actual finding set, not the erroneous total**, and the reviewer's arithmetic defect is recorded at §16.2 as reviewer-record evidence rather than silently absorbed.

| # | Surface | Sev | Repair mode | Governing clauses |
|---|---|---|---|---|
| 1 | **CR4-01** — the loss class was drawn from the embodiment's own declaration; nothing closed the vocabulary or individuated "capability", so CR-003 §3.5's pair reconstructs comparing equal | **BLOCKING** | **IMPOSSIBLE** — the embodiment is removed from the naming role. Loss is named by the identity of the clause whose obligation it cannot honor, drawn from a closed published set, exact in both directions, and injective by `INV-RC-KERNEL-4` | SP-151, SP-152, SP-155, SP-167–SP-171 |
| 2 | CR4-03 — the published auditor did not execute; its body was duplicated with a divergent copy, and true numbers carried a false provenance | MATERIAL | **IMPOSSIBLE + DETECTABLE** — every `python` fence is `compile()`d, every fence scanned for duplicated payload, the program re-extracts its own shipped bytes and compares, and compares its output to the published block | §16.4 auditor |
| 3 | CR4-02 — the required vector left the DaySlot ordinal unpinned while SP-023 makes it semantic | MATERIAL | **IMPOSSIBLE** — the vector pins a single fixed DaySlot ordinal | SP-094 |
| 4 | CR4-04 — SP-005 carried authored normative law inside a `FOUNDER_SEALED_L1 / EXACT` row | MATERIAL | **IMPOSSIBLE** — split on the SP-090/SP-094 pattern, now applied class-wide rather than row-locally | SP-005, SP-172 |
| 5 | CR4-05 — SP-091 replaced two named traces with an unbounded quantifier, weakening the sealed Pass condition | MATERIAL | **IMPOSSIBLE** — the founder's three-way equality is restored verbatim; the cardinality is carried by an authored clause | SP-091, SP-173 |
| 6 | CR4-06 — SP-046 promoted a modalized worked example to unhedged universal law under an `EXACT` seal | MATERIAL | **IMPOSSIBLE** — the enumeration and the modality promotion are split out and declared authored, as SP-094 already declares for the identical promotion | SP-046, SP-174 |
| 7 | CR4-07 — the count's scoping was a founder decision given operative force without docketing | MATERIAL | **DETECTABLE** — docketed as **A-09** and flagged as decided-by-installation; the underlying choice is *not* resolved by authorship | A-09, §13.1 |
| 8 | CR4-08 — §13.0's branch mapping was not a partition; the third branch fired vacuously on every singleton | MATERIAL | **IMPOSSIBLE** — the rule is restated over `\|Y\|` rather than quantifier prose, and an `INCONSISTENT` branch prevents a no-answer item collapsing into `OPERATIVELY_DECIDED` | §13.0 |
| 9 | CR4-09 — SP-019's "complete" L-fact set was falsified by SP-053 and SP-075 | MATERIAL | **IMPOSSIBLE** — the originating DaySlot ordinal is added; four docket justifications that presupposed exhaustiveness are re-grounded | SP-019, §13.1 |
| 10 | CR4-10 — `view`'s domain specified three ways; acceptance values evaluated *before* the restart, so the sole required vector never witnessed post-restart state | MATERIAL | **IMPOSSIBLE + DISCLOSED** — observation is evaluated at the final presented index; §15's false claim is corrected and the unreconciled coordinate terms are recorded as a residual | SP-175, §11.1, §15 |
| 11 | CR4-11 — SP-121's stated reason was false under the disposition regime | MATERIAL | **IMPOSSIBLE** — sameness of admission order is a consequence of SP-152 conformance, not a property of the input | SP-121 |
| 12 | CR4-12 — §17.3's `ORTHOGONAL` justification for SP-029 rested on a premise L1 falsifies | MATERIAL | **IMPOSSIBLE** — SP-029 gains the scope limiter its neighbours carry, and §17.3 argues scope instead of denying L1 speaks | SP-029, §17.3 |
| 13 | CR4-M1…M5 — §17.1 tally, SP-158 quotation drift, Semantic Source Map absent, §16.1 rationale, §15 acceptance vocabulary | MINOR | all **CORRECTED** | §15, §16.1, §17.1, SP-158 |

**No finding Cold Review 004 confirmed closed was reopened.** CR3-B01 and the thirteen CLOSED CR-003 findings are carried forward untouched.

---

## 1. Identity, purpose, and non-goals

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-001 | RC-0001's proof subject is one substrate-neutral Durable Daily Ritual Ledger whose preserved meaning includes Ritual, Entry, the progression idle → active → complete, begin, record, complete, invalid transition law, durability, canonical ordering, restart preservation, and equivalent state traces. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-A | — |
| SP-002 | The program governs logical state and observable semantic consequence; no user interface, runtime, language, serialization, storage engine, network, or device mechanism is part of its meaning. | L2 | RCP-CONSTRAINED | COMMISSION_REQUIRED | ELABORATES | P-L1-B, P-L1-C, P-L2 §2.1 | — |
| SP-003 | A successful ledger transition establishes what the ledger records and no more. Entry status complete means the program's complete transition succeeded for that Entry-bearing cycle; it is not independent proof that an external-world act occurred. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L3-A, P-L4-R1 | A-05 |
| SP-004 | **REVISED (CR3-15).** The founder-stated exclusions are reproduced here member-for-member. From P-L1-A: "No auth, no cloud, no camera, no AI, no networking". From P-L1-B: "No cloud. No authentication. No generative AI. No camera. No networking. No seductive product surface hiding compiler defects." From P-L1-C: "The first proof is not:" — "beautiful UI;" "production architecture;" "App Store readiness;" "sophisticated Swift;" "sophisticated React;" "generalized storage abstraction;" "reusable design system." (P-L1-C is a semicolon-terminated bullet list; v0.3 re-rendered it as a comma list and added the article "a" before "reusable design system". Both are corrected here, and the v0.3 lead-in "literally and in full" is withdrawn as a claim about rendering.) This clause is **reportorial**: it reproduces the register and enforces nothing — see SP-166. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-A, P-L1-B, P-L1-C | A-08 |
| SP-166 | **NEW (CR3-19) · the register's operative status, stated rather than left implicit.** No clause of this SemanticProgram has the form "an embodiment containing X is nonconforming" for any member of SP-004's register. SP-004 reproduces; SP-002 places mechanisms outside the program's *meaning* rather than prohibiting their presence. Enforcement of the founder exclusions is therefore **not performed at the SemanticProgram layer**, by design — §15 forbids implementation content, and an exclusion is a property of a built artefact. This is disclosed because A-08's openness follows from it: no clause depends on the "no AI" / "No generative AI" difference because no clause depends on the register at all. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L1-C, P-L4-CR3 CR3-19 | A-08 |
| SP-100 | Any generalization of SP-004's literal register — "distribution readiness" for App Store readiness, "target-code sophistication" for sophisticated Swift and React — is authored elaboration carrying no founder seal. Where a generalization and the literal register differ in extent, the literal register governs. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-C | — |
| SP-005 | **REVISED (CR3-15).** The founder distinguishes four terms, in his words: "semantic equivalence ≠ structural equivalence ≠ visual identity ≠ binary identity". **REVISED AGAIN (CR4-04):** the authored conformance sentence that followed the chain is removed to SP-172. L1 states the four-term distinction and that *"What must remain equal are the declared observable semantics"*; it says nothing about the acceptance predicates of a SemanticProgram it never saw. This row is now the founder's distinction alone. (v0.3 renamed three of the four comparanda — "matching component structure", "visual similarity", "matching binaries" — and §17.1 then described a four-term chain as "the three named identity kinds". The founder's terms are restored.) | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-B, P-L1-C | — |
| SP-172 | **NEW (CR4-04) · the authored consequence of SP-005.** A conforming embodiment preserves the acceptance predicates of this SemanticProgram through **semantic equivalence**; structural equivalence, visual identity, and binary identity are each distinct from it and none substitutes for it. This sentence is authored: it is a normative conformance condition referencing *this SemanticProgram*, an artifact L1 never saw, and "acceptance predicates" appears in L1 only at constitutional law 4 and in P-L1-C's emitter and fail lists — never joined to the four-term chain. It is stated here rather than inside SP-005 so that a founder-sealed row is never parameterized by an authored clause, which is the SP-090/SP-094 technique CR3-01 established and v0.4 failed to apply class-wide. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B, P-L4-CR4 CR4-04 | — |

### 1.1 Intended participant outcome

The ledger supplies one durable, ordered account of the content recorded while a Ritual is active and the completion state reached through lawful operations. It remains usable after a bounded restart and across daily recurrence, without importing an observer-adjudication ontology into the core state machine.

---

## 2. Semantic actors, capability, and the program boundary

### 2.0 Capability resolution — SP-R03 surface 1 · SP-R04 surfaces 1 and 2

**The v0.2 defect.** SP-132 placed capability filtering outside the SemanticProgram boundary and called it `ORTHOGONAL`. Cold Review 002 B.1-F1 showed the relocation was not a removal: for presented sequence `begin; record("A"); record("B"); complete`, an embodiment whose pre-boundary filter drops `record("B")` yields Entries `[A]` while an unfiltered embodiment yields `[A, B]`, and **neither violates any SP clause**, because SP-091 compared "the same SemanticProgram input" and the two inputs were no longer the same after filtering. This defeats executable semantic preservation and contradicts P-L1-B constitutional law 3:

> **"Capability loss is typed and explicit. No emitter silently 'figures something out.'"**

**The v0.3 repair, carried forward — total disposition accounting.** Capability resolution remains outside transition law. What changes is that it can no longer be invisible: every presented element must be accounted for, and the accounting is a proof-visible T-fact.

```
PRESENTED SEQUENCE  (what conformance compares)
        │
        ▼
CAPABILITY RESOLUTION           may not delete; must dispose
        │
        ├── ADMITTED ──────────────────────────► SemanticProgram transition law
        │
        └── CAPABILITY_UNSUPPORTED ────────────► typed T-fact, proof-visible
            + FAILED-REQUIREMENT SET             (never reaches transition law)
              (SP clause identities, closed set)
                        │
                        └── compared across embodiments (SP-152)
```

**The v0.3 defect, per Cold Review 003.** v0.3 offered two non-`ADMITTED` tokens. `CAPABILITY_DEGRADED` occurred twice in the whole document, had no definition, no assignment rule and no trace coverage; and SP-153's binary ("decides only whether a presented element **reaches** the SemanticProgram") left it operationally identical to `CAPABILITY_UNSUPPORTED`. Worse, the **loss class never entered the comparison**: CR-003 §3.5 constructed embodiments G′ and H′ losing *capacity* and *canonical ordering* respectively — the second a member of P-L1-A's sealed scope list — and they compared **equal**, violating no clause. P-L1-B law 3 requires capability loss to be *typed* and explicit; v0.3 achieved explicit and stopped short of typed.

**The v0.4 repair.** One non-`ADMITTED` disposition, carrying a **declared loss class** that is itself compared. The type moved inside the compared surface, which is where law 3 requires it.

**The v0.4 defect, per Cold Review 004 — `CR4-01`, BLOCKING.** The loss class was drawn from *the embodiment's own* published capability declaration. Nothing in v0.4 closed that vocabulary and nothing individuated "capability." SP-151's sentence — *"Two embodiments lacking different capabilities therefore carry different loss classes"* — asserted a fact about the world instead of imposing a constraint the program enforces. So CR-003 §3.5's pair reconstructs: G′ and H′ may each **truthfully** publish one coarse class such as `SECOND_RECORD_UNSUPPORTED`, satisfy SP-155's veridicality (it is true of both), and compare **equal** under SP-152. The loss of canonical ordering — a member of P-L1-A's sealed scope list — is invisible again. v0.4 §16.2 rated that repair `IMPOSSIBLE`; it was merely *unenforced*. Under the governing criterion, the hole moved from an undefined token to an uncalibrated vocabulary; it did not close.

**The v0.5 repair — individuate by the obligation lost, not by a name the loser chooses.** The failure mode is structural: any scheme in which the party being measured supplies the vocabulary that individuates its own loss is uncalibrated by construction. The repair removes the embodiment from the naming role entirely. A `CAPABILITY_UNSUPPORTED` disposition no longer carries a declared *class*; it names the **failed-requirement set** — the identities of the clauses of this document whose obligation the embodiment cannot honor for that element.

This introduces **no vocabulary**. It is a reference into a closed, enumerated set the document already publishes, and it is what the admitted source lineage already requires:

- **RCP §5.2** (governing record `1aa3698c…38c776`, named by the commission) states the Capability Resolver's `OUTPUT` as *"a CapabilityDecision **per semantic requirement**"*, and its `SEMANTIC SOURCE MAP` obligation as *"every decision references the RealityIR requirement it answers."* Loss is indexed by requirement in the protocol's own contract.
- **`INV-RC-CAP-1` (Totality)** — *"Every semantic requirement receives exactly one decision. A requirement with no decision is a compilation error, not a default."*
- **`INV-RC-KERNEL-4` (Injective distinction)** — *"No admitted construct may encode a distinction already encoded by another admitted construct. Two constructs that collapse to one meaning encode neither."* This is precisely the calibration `CR4-01` found missing, and it was already admitted.
- **P-L1-C's sealed Semantic Source Map** traces `CapabilityDecision → RealityIR transition → SemanticProgram rule`. The founder sealed that a capability decision resolves backward *to a SemanticProgram rule*. Requirement identity is not an author's convenience; it is a founder-sealed traceability requirement.
- **F-05 v0.2 `INV-OBS-PER-2`** already adjudicated the same pattern one layer over: *"A substrate that cannot SHALL say so **at the named tier** rather than satisfying the requirement at a lower tier silently."*

**What this repair does not do.** It installs no capability decision vocabulary. RCP §5.3 already publishes a closed five-member one (`SUPPORTED`, `SUBSTITUTED`, `DEGRADED`, `ABSENT`, `REFUSED`), and the CapabilityDecision *record schema* is expressly reserved to R-04. Neither is authored, extended, or pre-empted here; see SP-171 and docket item **A-10**. This document supplies only the requirement identities that such a decision is later taken *per* — which is the SemanticProgram's own layer, and the one layer that must exist before R-04 can do its work.

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-150 | **REVISED (CR3-04).** RC-0001's conformance input is a **presented sequence** of invocations and discontinuity boundaries. Every element receives exactly one disposition in the program's record: `ADMITTED` or `CAPABILITY_UNSUPPORTED`. The disposition function is total: no presented element may be absent from the record. `CAPABILITY_DEGRADED` is **withdrawn** — it denoted nothing SP-153's binary could distinguish from `CAPABILITY_UNSUPPORTED`, and a token with no assignment rule is not a type. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B, P-L4-CR2 B.1-F1, P-L4-CR3 CR3-04 | A-07 |
| SP-151 | **REVISED (CR4-01).** A `CAPABILITY_UNSUPPORTED` disposition is a typed T-fact naming the presented element and its **failed-requirement set** under SP-169. The former "loss class" is **withdrawn**: it was drawn from the embodiment's own published declaration, which made the party being measured the author of the vocabulary individuating its loss, and no clause closed that vocabulary or individuated "capability" (CR4-01). The failed-requirement set names members of the closed requirement set fixed by SP-167. An embodiment never invents a member and never supplies a coarser name of its own. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B, P-L1-C, P-L4-CR4 CR4-01 | — |
| SP-152 | **REVISED (CR4-01, the barrier).** Conformance is compared over the **presented sequence**, not over the post-resolution admitted sequence. Two embodiments conform only if, for every presented element, they assign **the same disposition and — where that disposition is `CAPABILITY_UNSUPPORTED` — the same failed-requirement set**, and every `ADMITTED` element produces the same outcome. Set equality is by clause identity, not by description. An embodiment that admits an element another disposes as unsupported has already diverged; so has one that fails SP-024 where another fails SP-022. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-C, P-L4-CR2 B.1-F1, P-L4-CR4 CR4-01 | — |
| SP-155 | **REVISED (CR3-08, CR4-01) · veridicality.** A disposition must be true of the embodiment that emits it. An embodiment may not dispose `CAPABILITY_UNSUPPORTED` an element its substrate can in fact admit, and **every member of its failed-requirement set must name an obligation it genuinely cannot honor for that element**. A disposition record that misdescribes the substrate is nonconforming, not a permitted reading. Because SP-169 also requires exactness in the other direction, veridicality here is a two-sided test: a named requirement it *can* honor falsifies the record, and so does an unnamed requirement it *cannot*. Without this clause SP-152 compares two records to each other and never to reality. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B law 3, P-L4-CR3 CR3-08, P-L4-CR4 CR4-01 | — |
| SP-156 | **NEW (CR3-13) · boundary elements.** A discontinuity boundary is a presented element under SP-150, but its **only lawful disposition is `ADMITTED`**. SP-050 and SP-053 permit no degradation of a discontinuity, and SP-046 and SP-084 are unconditional. A boundary disposed `CAPABILITY_UNSUPPORTED` is nonconforming. This resolves the SP-150/SP-050 conflict on its face rather than leaving two clauses that cannot both be satisfied. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L4-CR3 CR3-13 | — |
| SP-157 | **NEW (CR3-06) · two distinct position coordinates.** Every presented element receives a **presented index** — its ordinal in the presented sequence, assigned to admitted and unsupported elements alike. Only `ADMITTED` invocations additionally receive an **SP-071 admission ordinal**. SP-152 compares by presented index; SP-013 and SP-110 range over admission ordinals. A `CAPABILITY_UNSUPPORTED` element consumes a presented index and **does not** consume an admission ordinal, so two embodiments disposing differently never misalign the position-indexed witness surface. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-C, P-L4-CR3 CR3-06 | — |
| SP-175 | **NEW (CR4-10) · observation past a discontinuity.** A discontinuity boundary consumes a presented index and **no** admission ordinal (SP-051, SP-157), so no observation addressed by admission ordinal can reach past it. Acceptance values of a required vector are therefore evaluated at the **final presented index**, after every element including a terminal boundary. Where SP-110, SP-112 and SP-013 range over an operation position or admission ordinal, they range over admitted invocations only and do **not** supply the post-boundary observation the founder's vector requires; this clause supplies it. Without it the sole required vector (SP-096) terminates its observation at `complete` and RC-0001 never witnesses anything after a restart — while *"+ restart preservation"* is a P-L1-A sealed scope member and *"restart semantics"* is on P-L1-C's fail list. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-C, P-L4-CR4 CR4-10 | — |
| SP-153 | **REVISED (CR3 §5.1.1) · the architectural distinction.** Capability resolution decides only whether a presented element reaches the SemanticProgram. It never decides whether an admitted element's transition is legal, **never writes an L-fact**, and never supplies or withholds permission to any Participant. **Capability decision ≠ transition permission.** It is **not** claimed that a disposition is L-fact-neutral in consequence: withholding an element changes which later transitions are reachable, and SP-152 exists precisely because that consequence is real and must be compared. The prohibition is on *writing*, not on *mattering*. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L2 §6.2, P-L4-CR3 §5.1.1 | A-07 |
| SP-154 | **NEW · REPAIR 1 (L1 law 3).** Removal of a presented element without a typed disposition is nonconforming, not an implementation freedom. An embodiment that silently narrows the presented sequence fails RC-0001 regardless of the ledger state it reaches. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B law 3 | — |
| SP-158 | **REVISED (CR4-M2) · NEW in v0.4 (CR3-12) · P-L1-B constitutional law 5, reproduced.** *"Adaptation is a governed act. A substrate-specific workaround requires explicit authorization."* P-L1-C's Emitter FORBIDDEN AUTHORITY entry reads *"invent capability adaptations"* — reproduced without a terminal period, which the pin does not carry (**CORRECTED, CR4-M2**: v0.4 placed a period inside the quotation marks and added the connective "correspondingly", while §17.1 audited the row as reproducing "nothing further"; the connective is removed and the two renderings now agree). | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-B, P-L1-C | — |
| SP-159 | **REVISED (CR3-12, CR4-01) · the authored consequence of SP-158.** RC-0001 authorizes no substrate-specific workaround. An embodiment that cannot admit a presented element disposes it `CAPABILITY_UNSUPPORTED` with its failed-requirement set; it may **not** substitute alternative semantics, approximate the element, reorder to accommodate it, or invent an adaptation. There is no unilateral adaptation route, because there is no authorization mechanism in RC-0001 that could grant one. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B law 5, P-L1-C, P-L4-CR3 CR3-12 | — |
| SP-167 | **NEW (CR4-01) · semantic requirement identity.** A **semantic requirement** of RC-0001 is an obligation this document normatively imposes, and its identity is the identity of the clause imposing it. The requirement set is therefore the set of normative SP clauses inside this document's SP-006 envelope: **closed, enumerated, and fixed at this candidate's digest**. No requirement exists that this document does not state, and no embodiment may name one it does not state. This is the set a later RealityIR carries forward under RCP §5.2's *"a CapabilityDecision per semantic requirement"*; identity is fixed at this layer because RealityIR does not exist and this movement may not create it. | L2 | RCP-CONSTRAINED | COMMISSION_REQUIRED | ELABORATES | P-L1-C, RCP §5.2, P-L4-CR4 CR4-01 | A-10 |
| SP-168 | **NEW (CR4-01) · invocation is computed, not declared.** Each presented element **invokes** a determinate set of semantic requirements: exactly those whose obligation is engaged by that element at that presented index. The invoked set is a function of the element and the presented-sequence prefix — both already compared by SP-152 — and of nothing else. It is computed from this document by any reader, and is **never declared by the embodiment**. §2.0.1 publishes the invocation table for `begin`, `record`, `complete`, and discontinuity boundaries. Two embodiments given the same presented sequence therefore compute identical invoked sets, and may differ only in what they can honor. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B law 3, P-L4-CR4 CR4-01 | — |
| SP-169 | **NEW (CR4-01) · the failed-requirement set, and its exactness.** A `CAPABILITY_UNSUPPORTED` disposition names the **failed-requirement set**: those requirements invoked at that element which the embodiment cannot honor. The set must be **exact** — every invoked requirement it cannot honor is named (maximality), and no requirement it can honor is named (minimality) — and **non-empty**, since an element with no failed requirement is `ADMITTED` by SP-150. Exactness is what makes the record falsifiable: because the requirement set is closed and published and SP-155 binds the declaration to the substrate, a reviewer can refute any named member or any omission against the substrate itself. A coarse self-description is not available, because the only admissible names are clause identities. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B law 3, P-L1-C, P-L4-CR4 CR4-01 | — |
| SP-170 | **NEW (CR4-01) · injective distinction, applied.** RCP `INV-RC-KERNEL-4`: *"No admitted construct may encode a distinction already encoded by another admitted construct. Two constructs that collapse to one meaning encode neither."* Applied to capability loss: two embodiments failing different semantic requirements necessarily carry different failed-requirement sets, **because the requirements are the distinctions**. There is no coarser admissible name under which two distinct failures could collapse, since every admissible name is a clause identity and clause identities do not merge. This is the calibration the v0.4 loss class lacked, and it is not authored here — it is an already-admitted kernel invariant applied to a surface that had escaped it. | L2 | RCP-CONSTRAINED | COMMISSION_REQUIRED | ELABORATES | RCP INV-RC-KERNEL-4, P-L4-CR4 CR4-01 | — |
| SP-171 | **NEW (CR4-01) · the protocol boundary this repair does not cross.** This document installs **no** capability decision vocabulary. RCP §5.3 publishes a closed five-member decision vocabulary (`SUPPORTED`, `SUBSTITUTED`, `DEGRADED`, `ABSENT`, `REFUSED`) and the CapabilityDecision **record schema is reserved to R-04**. Neither is authored, extended, ratified, or pre-empted here, and RC-0001's two dispositions are **not** claimed to be that vocabulary or to be reconcilable with it by authorship. The reconciliation is a protocol-level act and is docketed as **A-10**. What this document supplies is only the requirement identities such a decision is taken *per* — the SemanticProgram's own layer, and a precondition of R-04 rather than an encroachment on it. | L2 | RCP-CONSTRAINED | COMMISSION_REQUIRED | ORTHOGONAL | RCP §5.3, F-05 v0.2 §11, P-L4-CR4 CR4-01 | A-10 |

**Withdrawn:** SP-132 (v0.2; its `ORTHOGONAL` justification was false, per Cold Review 002 B.1-F2). **Withdrawn in v0.4:** the `CAPABILITY_DEGRADED` token, per CR3-04.

**Why the v0.2 counterexample remains impossible.** Presented `begin; record("A"); record("B"); complete`. Embodiment I must emit `CAPABILITY_UNSUPPORTED(record("B"))` as a typed T-fact with a declared loss class; embodiment W emits `ADMITTED(record("B"))`. SP-152 compares dispositions over the presented sequence, so divergence is visible at the element that caused it, before any Entry-count difference arises. Cold Review 003 §3 re-ran this construction against v0.3 and confirmed detection at element 3; v0.4 preserves that mechanism and does not alter it.

**Why the CR-003 / CR-004 degraded-capability counterexample is now impossible.** G′ cannot hold a second pending contribution; H′ can hold two but cannot preserve their canonical order. Both dispose `CAPABILITY_UNSUPPORTED(record("B"))`. Under v0.3 they compared equal because the loss class sat outside the comparison. Under v0.4 they *could* compare equal again, because each could truthfully publish one coarse class of its own choosing — that is `CR4-01`. Under SP-167–SP-170 the naming role is removed from them entirely: `record` at an active state invokes a fixed set of requirements computed from §2.0.1, and

```
G′  failed-requirement set = { SP-022 }          cannot create the ordered pending contribution
H′  failed-requirement set = { SP-024 }          creates it, cannot preserve canonical order
{ SP-022 } ≠ { SP-024 }  ⟹  SP-152 divergence at presented index 3
```

Neither embodiment can collapse these, because neither chooses the names. The distinction P-L1-A sealed — canonical ordering — is now the identity of a published clause, and an embodiment that failed ordering while naming `{ SP-022 }` is refuted by SP-155 against its own substrate. **A type whose extension is chosen by the party being measured is not a type; a clause identity is not chooseable.**

### 2.0.1 Requirement invocation table — SP-168

Computed from this document's own clauses. A reader derives it; an embodiment does not declare it. `n/a` marks a row whose disposition is constrained elsewhere.

| Presented element | Invoked requirements | Notes |
|---|---|---|
| `begin` | SP-030, SP-031, SP-037, SP-038 | success condition, refusal law, atomicity, no-op distinguishability |
| `record(content)` | SP-032, SP-162, SP-022, SP-021, SP-024, SP-033, SP-037, SP-038 | success and content predicate; ordered pending contribution; Entry identity; canonical order; refusal; atomicity; distinguishability |
| `complete` | SP-034, SP-020, SP-021, SP-024, SP-035, SP-037, SP-038 | success condition; one Entry per pending contribution; identity; canonical order; refusal; atomicity; distinguishability |
| discontinuity boundary | SP-046, SP-050, SP-051, SP-052, SP-053, SP-084 | **n/a for failure** — SP-156 makes `ADMITTED` the only lawful disposition, so a boundary's failed-requirement set is necessarily empty. An embodiment that cannot honor these does not dispose the boundary; it **fails RC-0001**. |

**Bounded claim, stated rather than hidden.** This table individuates loss across every requirement RC-0001 declares. It does **not** individuate loss of anything RC-0001 does not declare — such a loss is outside this proof's semantic surface by SP-002 and SP-003, not silently absorbed by it. That boundary is a property of the gate's scope, and is disclosed here rather than left for a reviewer to discover. Whether the RC-0001 requirement set is itself complete is `CR4-09`'s question, dispositioned in §16.2.

**The architectural line is unmoved.** The Operator gate is not restored. `begin`, `record`, and `complete` retain state-and-content-only preconditions; SP-153 keeps capability decision outside transition permission; SP-105 forbids any transition evaluation from reading a T-fact. Nothing in this repair gives capability resolution authority over semantic law — it gives proof authority over capability resolution.

### 2.1 Actors

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-010 | **RECLASSIFIED (CR3-03).** A Participant is a logical principal presented to the SemanticProgram. Participant identity proof and authentication mechanics are outside RC-0001. Relation corrected from `ORTHOGONAL` to `ELABORATES`: this clause restates a founder exclusion — P-L1-A "no auth" and P-L1-B "No authentication" — and a clause restating an L1 proposition elaborates it rather than standing orthogonal to it. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L3-A | — |
| SP-011 | Invocation capability and observation capability are conceptually independent: possessing either does not imply possessing the other. This models the commission's required separation. It does not make either a precondition of any RC-0001 operation. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L2 §6.2, P-L3-A | A-07 |
| SP-130 | RC-0001 admits **no invocation-capability precondition** on begin, record, or complete. An admitted invocation's acceptance or refusal is determined solely by state legality and content presence. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L4-CR1 CR-01 | A-07 |
| SP-131 | No capability, permission, role, authority, or admission model may cause any presented sequence to produce a disposition or outcome other than the one this SemanticProgram assigns it. A model that can do so is nonconforming, not an alternative reading. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B, P-L3-FD01 | — |
| SP-013 | The designated RC-0001 conformance witness must be able to observe every L-fact in SP-019 at an identified operation position through the SP-110 projection, and the complete T-fact stream including dispositions. Witness observation is not an operation. | L2 | AUTHOR-PROPOSED | COMMISSION_REQUIRED | ELABORATES | P-L1-B, P-L1-C, P-L2 §6.7 | — |
| SP-014 | No ledger fact is required by this SemanticProgram to be hidden from any Participant. Confidentiality and access-control policy are not semantic guarantees of RC-0001. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L2 §6.7 | — |
| SP-016 | No RC-0001 operation grants, transfers, revokes, or establishes a Participant's authority. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L2 §6.8 | A-05 |
| SP-028 | Refusal is produced by the SemanticProgram's state and content law; no Participant has discretionary power to convert a refused attempt into an accepted one, or an accepted attempt into a refused one. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-C, P-L2 §6.2 | — |
| SP-029 | **REVISED (CR4-12).** No confirmer, amender, invalidator, Reporter, Assertion, Adjudicator, Adjudication, or Establishment construct exists **in this SemanticProgram's ontology**, because no confirmation, amendment, invalidation, or world-fact adjudication operation is admitted here. The scope limiter is added because the unscoped form was false as written: L1 names `Adjudication` as a stage of the canonical stack (P-L1-A:25, P-L1-B:21), a required protocol layer (P-L1-C:26) and the subject of constitutional law 6. RC-0001's SemanticProgram is stage 2; adjudication is a later stage, and its absence *here* is not a denial of it *there*. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L2 §6.2, P-L3-FD01 | A-05, A-06 |

---

## 3. Semantic facts and identity

### 3.0 The L-fact / T-fact partition — MECHANISM PRESERVED · TWO ROWS EDITED

Cold Review 002 B.2 evaluated the six-step trace `begin; record("Reflect"); restart; restart; complete; restart` and found the partition does not leak; Cold Review 003 re-confirmed it and returned `L/T non-interference — holds`. **The mechanism is unchanged. The section text is not**, and v0.3's "preserved verbatim" header was false: SP-102 and SP-105 were marked changed inside it. In v0.4, SP-102 is revised again for CR3-B01. Every changed row in this document is marked and enumerated in §16.6.

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-103 | The SemanticProgram's observable facts are partitioned into two disjoint classes. **L-facts** are the state the program preserves. **T-facts** are the monotonic witness record of what was presented and what the program answered. No fact belongs to both classes. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-B, P-L1-C | — |
| SP-019 | **REVISED (CR4-09).** The complete **L-fact** set is: Ledger identity; Ritual identity; current-state value; current DaySlot ordinal; **the originating DaySlot ordinal of the open active interval, while one is open**; ordered pending contributions while present; durable ordered Entries with content and status; and canonical history order. The originating DaySlot was omitted from v0.2 through v0.4 while SP-075 obliged an interval to *retain* it and SP-053 listed *"origin DaySlots"* among surviving L-facts — so the enumeration claiming completeness contradicted two clauses that depended on a member it did not carry. Present `⟨begin, record("A"), boundary, complete⟩` from DaySlot 1: immediately after the boundary the origin is not recoverable from any other member, because the contribution is not yet in canonical history. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-A, P-L1-B | A-01, A-03, A-04 |
| SP-102 | **REVISED (CR3-B01).** T-facts are **scoped to one presented sequence.** For a presented sequence `P`, the complete **T-fact** set of `P` is: the presented index; the admission ordinal of each admitted element; the ordered disposition record required by SP-150; the ordered operation-outcome stream; restart-boundary markers; and the illegal-transition count derived over `P`. Within `P` the T-fact set is append-only and strictly monotonic. It does not carry across presented sequences: each presented sequence begins with an empty T-fact set. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-B, P-L1-C | — |
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

### 4.0 Refusal precedence — SP-R03 surface 2 · SP-R04 surface 5 (content predicate)

**The v0.2 defect.** At `state = idle`, `pending = empty`, operation `complete`, both failure conditions hold. SP-035 said "`INVALID_TRANSITION` or `NO_RECORDED_CONTENT`" without disambiguating, and SP-043 then produced `illegal_transition_count` of 1 or 0 for identical input. Cold Review 002 B-F3 confirmed identical input with two legal outputs, and FT-08 was asserting one branch — the CR-03 pattern surviving in a second row.

**The v0.3 repair, carried forward unchanged — fix the mechanism, then let the trace derive from it.** Cold Review 003 enumerated the full 18-cell Cartesian twice and returned 18/18 `EXACTLY_ONE`; SP-160's precedence text is therefore untouched. SP-R04 changes only SP-161's justification (CR3-09) and supplies step 2's missing antecedent predicate (SP-162, CR3-07).

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-160 | **NEW · REPAIR 2.** Every admitted invocation yields exactly one normative result, determined in fixed precedence: **(1) state legality is evaluated first** — if the operation is not lawful from the current state, the result is refusal `INVALID_TRANSITION` and evaluation stops; **(2) content conditions are evaluated only if the operation is state-legal** — yielding `MISSING_CONTENT` for record without content, or `NO_RECORDED_CONTENT` for complete with no pending contribution; **(3) otherwise the operation is accepted.** No admitted input state and operation may yield more than one result. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L4-CR2 B-F3 | — |
| SP-161 | **REVISED (CR3-09) · precedence justification.** State legality precedes content evaluation because the **existence** of an invalid-transition law is founder-sealed at P-L1-A ("+ invalid transition law") while the content-presence refusal classes are wholly authored. A founder-sealed law is evaluated before an authored refusal class. **What is sealed is the law's existence, not its edge content** — the operation-to-edge mapping is authored at SP-163. The precedence rule stands on that narrower ground. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L4-CR1 §4, P-L4-CR3 CR3-09 | — |
| SP-162 | **NEW (CR3-07) · the content-presence predicate.** Content is **present** when a content value is supplied with the invocation. Presence is a property of *supply*, not of the value's length, shape, or whitespace: a supplied empty value **is present**, and `record("")` is therefore state-legal-and-content-satisfied at `state = active`, appending one pending contribution whose content is the empty value. Content is **absent** only when no content value is supplied. This predicate is authored — P-L1-A, P-L1-B and P-L1-C fix no presence criterion — and it is stated because without it SP-160 step 2's antecedent is undefined and two embodiments diverge lawfully on the same element. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B, P-L4-CR3 CR3-07 | — |
| SP-043 | **REVISED (CR3-B01).** The illegal-transition count is **derived over one presented sequence and has no existence outside it.** For a presented sequence `P`, `illegal_transition_count(P)` is the number of elements of `P` whose SP-160 result is `INVALID_TRANSITION`. Its value at the first element of `P` is zero; it increments by exactly one when and only when an element of `P` yields `INVALID_TRANSITION`; and no earlier presented sequence contributes to it. Because SP-160 yields exactly one result per admitted element, the count is deterministic. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-B, P-L1-C | — |

### 4.1 State-changing operations

Preconditions are state-and-content only. No invoker qualification appears.

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-030 | begin expresses intent to enter an active Ritual interval. It succeeds when and only when current state is idle; success changes current state to active, preserves all durable Entries, creates no Entry, and emits an accepted begin outcome. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B | A-01 |
| SP-031 | **REVISED.** A refused begin leaves every L-fact unchanged and emits a rejected begin outcome whose single reason is determined by SP-160. begin has no content condition, so its only refusal reason is `INVALID_TRANSITION`. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-A, P-L1-B, P-L2 §6.4 | — |
| SP-032 | **REVISED (CR3-07).** record(content) expresses intent to add one contribution to the active interval. It succeeds when and only when current state is active and content is **present in the sense fixed by SP-162**; success appends one pending contribution in admission order, leaves state active and durable Entries unchanged, and emits an accepted record outcome. The v0.3 phrase "content-bearing contribution" is withdrawn: it implied a non-emptiness criterion that SP-162 does not impose, and the two readings pulled against each other. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L4-CR3 CR3-07 | A-03 |
| SP-033 | **REVISED.** A refused record leaves every L-fact unchanged and emits a rejected record outcome whose single reason is determined by SP-160: `INVALID_TRANSITION` when state is not active, otherwise `MISSING_CONTENT`. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-A, P-L1-B, P-L2 §6.4 | — |
| SP-034 | complete expresses intent to close the active interval. It succeeds when and only when current state is active and at least one pending contribution exists; success changes current state to complete, causes one complete Entry per pending contribution to exist in canonical order, clears the pending projection, preserves all earlier Entries, and emits an accepted complete outcome. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B | A-01, A-02, A-03 |
| SP-035 | **REVISED.** A refused complete leaves every L-fact unchanged and emits a rejected complete outcome whose single reason is determined by SP-160: `INVALID_TRANSITION` when state is not active, otherwise `NO_RECORDED_CONTENT`. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-A, P-L1-B, P-L2 §6.4 | — |

### 4.2 Observation — MECHANISM PRESERVED · ROWS EDITED

Cold Review 002 confirmed `view(n)` purity holds and Cold Review 003 did not disturb it. `inspect` remains withdrawn as an operation. **v0.3's "CARRIED FORWARD UNCHANGED" header was false** — SP-110–SP-114 had all been edited beneath it, and one of those edits (SP-112) made a clause false. SP-112 and SP-113 are repaired here; see §16.6.

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-110 | Observation is a total function `view(n)` from any operation position `n` to the complete L-fact set as of `n`. It is a projection of program state, not an operation, not an attempt, and not an event. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L2 §6.7, P-L3-A | — |
| SP-111 | `view` is defined at every operation position, emits no T-fact, occupies no position, never contributes to the illegal-transition count, and can never alter the acceptance, refusal, ordering, disposition, or outcome of any invocation. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L4-CR1 §7.2 | — |
| SP-112 | **REVISED (CR3-05) — v0.3's edit falsified this clause.** `view` is total and deterministic: `view(n)` has exactly one value for a given **presented sequence together with its disposition record** and a given admission ordinal `n`. Two observations at the same ordinal are the same value. Observations at different ordinals are different observations, not disagreement. (v0.2 said "input trace", which was post-admission and true. v0.3 substituted "presented sequence" inside a section labelled *deliberately not touched* — and thereby made the clause **false**, because under SP-150 two embodiments sharing a presented sequence may differ in disposition and therefore in L-facts. The determinant is restored to include the disposition record.) | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-C, P-L2 §6.7, P-L4-CR3 CR3-05 | — |
| SP-113 | **REVISED (CR3-05) — deleted text restored.** Staleness is not a semantic property of the program. A substrate delivering `view(n)` when the greatest admitted ordinal is `m > n` has delivered a correct observation of ordinal `n`. No currentness **or maximum-staleness** obligation is required, and none is imposed. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L2 §6.7, P-L4-CR1 CR-07 | — |
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
| SP-041 | **REVISED (CR3-09) · reproduction only.** P-L1-A and P-L1-B each state, as two separate unlabelled registers, the progression `idle → active → complete` and the operation list `begin`, `record`, `complete`. This clause reproduces both registers and asserts nothing about which operation drives which edge. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-A, P-L1-B | — |
| SP-163 | **NEW (CR3-09) · the authored operation-to-edge mapping.** RC-0001 maps the sealed operations onto the sealed progression as idle —begin→ active, active —record→ active, and active —complete→ complete; no other transition of begin, record, or complete is lawful. **This mapping is authored.** L1 supplies the chain and the operation list as separate registers and never joins them, and the `active —record→ active` self-loop appears in no pin: L1's chain has two arrows. The mapping is derivable from P-L1-B's worked trace reaching `state = complete` with `illegal_transition_count = 0` only if the chain is read as exhaustive — a reading of an example the founder himself modalized as "might require". It is therefore stated as authored elaboration, on the same footing as SP-048's fourth-operation closure. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L4-CR3 CR3-09 | — |
| SP-042 | Within one DaySlot, complete is terminal for state-changing operations. A later DaySlot boundary may make a new daily cycle idle under SP-053 without deleting prior Entries. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L3-A | A-01, A-04 |
| SP-044 | Pending-contribution order equals accepted record admission order. complete preserves that relative order when the corresponding Entries join history. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L1-C | A-03 |
| SP-045 | Canonical history order is total, stable across every contemplated discontinuity, and independent of wall-clock timestamps. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L1-C | A-04 |
| SP-046 | **REVISED AGAIN (CR4-06).** Entries survive a restart — P-L1-A seals *"+ durability"* and *"+ restart preservation"* unhedged. **What is preserved is no longer enumerated inside this sealed row:** the field list (content, status, relative order) is drawn solely from P-L1-B's worked trace, which the founder modalized as *"the oracle **might require**"*, and composing three register items into one binding law is the same promotion SP-094 already declares authored. That enumeration moves to SP-174. (v0.3 scoped this to a "**contemplated** restart" — a qualifier set by the `AUTHOR-PROPOSED` clauses SP-050 and SP-052, which made an `EXACT` row's extent depend on authored text. The qualifier is removed: "restart" here is the founder's own word, and the boundary between a restart and total destruction is drawn where it belongs, in SP-050 and SP-052, not inside a sealed row.) | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-A, P-L1-B | A-06 |
| SP-174 | **NEW (CR4-06) · the authored enumeration split from SP-046.** What survives a restart is each completed Entry's **content**, **status**, and **relative order**. This enumeration and its promotion from the founder's *"might require"* to an unhedged universal law are **authored**, exactly as SP-094 declares for the same promotion in the required vector, and they bind three separately-sealed register items — durability, restart preservation, canonical ordering — into one composite obligation L1 never composes. The obligation is retained because RC-0001 is unprovable without it; only its provenance is corrected. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L4-CR4 CR4-06 | A-06 |
| SP-047 | The candidate does not decide which entity owns current state. SP-101 governs the operation/state completion relationship; A-01 governs ownership. | L4 DERIVATION | UNRESOLVED | DERIVED | ELABORATES | P-L1-B, P-L4-R1 | A-01, A-02 |
| SP-048 | **REVISED.** No correction, amendment, deletion, supersession, invalidation, scheduling, or world-fact adjudication transition exists, and no fourth state-changing operation is admitted. The closure over operations beyond the sealed three is an authored minimality choice, not a founder-sealed prohibition. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L1-A, P-L1-C, P-L3-FD01 | A-05, A-06 |
| SP-049 | Once complete, an Entry and its content, status, identity, and relative order survive later DaySlot transitions. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L3-A | A-04, A-06 |

---

## 6. Discontinuities — MECHANISM PRESERVED · ROWS EDITED

Cold Review 002 confirmed the restart witness separation is coherent under the six-step trace, and Cold Review 003 did not disturb it. **v0.3's "preserved verbatim" header was false** — SP-050 through SP-055 had all been edited beneath it, with normative text deleted from SP-050 and SP-051. SP-050 is restored and SP-055 reclassified here; SP-051's v0.2 sentence remains deliberately absent, and that absence is now declared rather than implied. See §16.6.

| Clause | Discontinuity and boundary | L-facts that survive | L-facts that must not survive | Ordering | Permitted degradation | T-fact effect | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SP-050 | **REVISED (CR3-05) — deleted text restored.** restart means a page/runtime reload, process restart, or device restart followed by re-entry to the same logical Ledger identity with its durable semantic state available. | Ledger and Ritual identity; current state; DaySlot; pending contributions; completed Entries; canonical order. | None. **No L-fact is required to be destroyed.** Volatile presentation state is not an L-fact. | Pending and history order identical. | None. An L-fact survives exactly or the restart law is violated. | Exactly one restart-boundary T-fact; presented index advances by one. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L1-C, P-L4-CR1 CR-06 | — |
| SP-051 | A restart invokes no operation and changes no L-fact. Its entire semantic footprint is the single T-fact required by SP-050. | All L-facts existing immediately before interruption. | None. | Identical before and after. | None. | Exactly one boundary marker. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B | — |
| SP-052 | Total destruction of the logical Ledger identity or loss of all durable semantic state is not a restart under SP-050. RC-0001 makes no survival claim across that different event. | Not specified; outside the contemplated class. | Not specified. | Not specified. | The event may not be relabeled as a conforming restart. | Not specified. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L4-CR1 §4 | — |
| SP-053 | DaySlot boundary increments the DaySlot ordinal. idle remains idle; complete becomes idle for a new cycle; active remains active and keeps its originating DaySlot until complete. | Ledger and Ritual identity; pending contributions; completed Entries; origin DaySlots; canonical order. | No completed Entry or pending contribution is destroyed. The prior current-state value need not survive when complete becomes idle. | History order preserved; later Entries sort after earlier DaySlots. | None. | One boundary marker; position advances by one. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L3-A | A-01, A-04 |
| SP-054 | A change in who is observing is not a discontinuity of this program. Because observation is the total projection SP-110, there is no observer state to lose. | Every L-fact. | None. | Unchanged. | None. | None. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ORTHOGONAL | P-L2 §6.7 | — |
| SP-055 | **RECLASSIFIED (CR3-03).** Temporary disconnection means a Participant cannot present an invocation for an interval. An invocation never presented is not part of the presented sequence and has no program presence. An invocation presented but capability-disposed is accounted for under SP-150 and is not "absent." | All L-facts. | None. | Preserved. | Unpresented intent is never promoted into any fact; presented intent is never silently removed. | Dispositions per SP-150. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B law 3, P-L3-A, P-L2 §6.6 | — |

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
| dispositions and failed-requirement sets, operation outcomes, restart markers, illegal-transition count | witnessed as an append-only stream, scoped to one presented sequence (SP-102). **REVISED (CR3-02):** the stream is a function of the presented sequence **and the embodiment's capability resolution** — not of the presented sequence alone. v0.3's law here read "the same presented sequence yields the same stream", which Repair 1 makes false by construction: SP-152 exists precisely because two embodiments given the same presented sequence may produce different dispositions, and that difference is how divergence is detected. Sameness of stream is a **conformance requirement compared under SP-152**, not a property guaranteed by the input. |

### 7.2 Authority and confirmation — the boundary Pass C identified

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-060 | A state counts as achieved when its lawful state transition succeeds. No separate confirmation, acceptance, Adjudication, Establishment, capability, or authoritative-world-answer act is required. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L3-FD01 | A-05 |
| SP-061 | record preserves supplied content as ledger content. It does not convert that content into an externally verified claim, a completion observation, or an authority decision. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L3-A, P-L4-R1 | A-05 |
| SP-064 | No unconfirmed-intent state can masquerade as accepted world fact: pending content is visibly pending, and completed Entry status denotes ledger completion only under SP-003. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L2 §6.8 | A-03, A-05 |

**The commission's authority boundary lives here.** Commission §6.2 speaks of "power to confirm it" and §6.8 asks "which states count without confirmation… who can confer it." Cold Review 002 Pass C established that this is **confirmation authority**, not invocation capability. SP-060 answers it: nothing confers; lawful transition suffices. SP-003 draws the boundary: ledger completion is not world truth. FT-11 now falsifies it.

---

## 8. Time, ordering, admission, and recurrence — MECHANISM PRESERVED · ROWS EDITED

Cold Review 002 found the concurrency repair airtight and Cold Review 003 did not reopen it. **v0.3's "preserved verbatim" header was false** — SP-071, SP-120, SP-121, SP-070, SP-073 and SP-083 had all been edited beneath it, and SP-071 had lost the definition of its own element domain. That definition is restored here. See §16.6.

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-071 | **REVISED (CR3-05, CR3-06) — element domain restored.** The SemanticProgram's admitted input is a totally ordered sequence **of admitted invocation records and discontinuity boundaries**. Every admitted invocation receives exactly one admission ordinal at admission, before any transition evaluation. Transition legality is evaluated strictly in that order. The order is part of the input, never a result of interpretation. Elements disposed `CAPABILITY_UNSUPPORTED` receive a presented index but no admission ordinal, per SP-157. (v0.3 deleted this clause's definition of its own element domain under a header asserting verbatim preservation.) | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B, P-L1-C, P-L4-CR1 §7, P-L4-CR3 CR3-05 | — |
| SP-120 | A presentation that does not yield a total admission order is not RC-0001 SemanticProgram input. Substrate simultaneity must be resolved into an admission order before the boundary; that resolution is input construction, not a semantic choice. A conformance vector that fails to determine the admission order of two attempts is malformed and may not be run. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-C | — |
| SP-121 | **REVISED (CR4-11).** Two embodiments given the same presented sequence **and assigning the same dispositions** necessarily receive the same admission order. v0.4's justification — *"because the order is a component of that input"* — is **false under the disposition regime**: the admitted sequence is the image of the presented sequence under the embodiment's disposition function, not a component of the input. E1 admitting all of `⟨begin, record("A"), record("B"), complete⟩` gives `complete` admission ordinal 4; E2 disposing `record("B")` unsupported gives it 3, from the same presented sequence. Sameness of admission order is therefore a **consequence of SP-152 conformance**, not a property guaranteed by the input — the correction §7.1 already made for the T-fact stream and did not propagate here. Divergent Entry sets arising from different serializations are impossible for one input; observed divergence is a conformance failure, not a permitted reading. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L1-B, P-L1-C | — |
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
| Ledger · Ritual | program container and Ritual-under-test | **ELABORATES (RECLASSIFIED, CR3-16)** | SP-001, SP-017 |
| RitualOccurrence / PlannedOccurrence | not adopted as core entities | ELABORATES if adopted | A-01 |
| CompletionObservation | not required for the founder trace | ORTHOGONAL if non-gating | A-05 |
| Correction | not adopted | ORTHOGONAL if it preserves L1 history | SP-025, A-06 |
| Day | logical DaySlot; civil mapping open | ELABORATES | SP-023, A-04 |
| Participant / Observer | **capability gates no operation; capability loss is typed, classed, and proof-visible** | ELABORATES | SP-010, SP-011, SP-130, SP-150–SP-159, A-07 |
| AuthorityDecision | not required to achieve L1 state | ORTHOGONAL if non-gating | A-05 |
| define / schedule ritual | outside the sealed three-operation core | ORTHOGONAL | SP-048 |
| observe / inspect | the SP-110 projection; withdrawn as an operation | ELABORATES | SP-110–SP-114 |
| record completion / noncompletion | record accepts opaque content; asserts no world fact | ELABORATES | SP-032, SP-061 |
| observation / authority separation | independent concepts; neither gates an operation | ELABORATES | SP-011, SP-130, SP-153 |
| recorded intent versus accepted fact | pending content distinct from completed Entry; neither is verified world fact | ELABORATES | SP-022, SP-064 |
| observer septuple | answered by projection, position, and agreement clauses | ELABORATES | SP-110–SP-114 |
| PENDING / CORROBORATED / CONTESTED / REJECTED / SUPERSEDED / STANDING | not adopted; core state remains idle / active / complete | ORTHOGONAL | SP-041, SP-163 **(CR3-14: SP-018 removed as a citation — it states a literal two-field observation "and nothing further" and says nothing about the progression)** |
| cross-day-boundary | a contemplated DaySlot discontinuity, not a fourth operation | ELABORATES | SP-053, SP-074, SP-075 |
| reconcile observations | not adopted; observation is a projection | ORTHOGONAL | SP-110, SP-111, A-05 |
| Assertion / Adjudication / Establishment ontology | **remains rejected as a precondition of RC-0001** | CONFLICTS when it gates the founder trace | SP-029, SP-039, SP-060 |

**Closed and not reopened.** Cold Review 001 §4 and Cold Review 002 both confirm the adjudication gate is correctly absent. No repair in SP-R03 required or reintroduced it.

---

## 11. Founder-sealed trace and acceptance predicates

**SP-R03 surface 4 was applied here; SP-R04 surfaces 1 and 3 revise it further.** v0.2's SP-090 combined the founder's worked example with a normative requirement and strengthened the founder's modality from "might require" to "yields," and added a precondition the founder never wrote. Cold Review 002 B.4 and B.4-F6 confirmed both. v0.3 splits the clause so the reproduction and the requirement carry different relations.

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-090 | **REVISED · reproduction only.** The founder's worked example is: for event trace `begin`, `record("Reflect")`, `complete`, `restart`, the oracle **might require** `state = complete`, `entries.count = 1`, `entries[0].content = "Reflect"`, `entries[0].status = complete`, `history_order = canonical`, `illegal_transition_count = 0`; and if both substrates satisfy that normalized semantic trace, they conform. This clause reproduces that example and its stated modality, adding nothing. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-B | — |
| SP-094 | **REVISED (CR3-B01).** RC-0001 adopts the SP-090 example as a required vector. The required vector **is a complete presented sequence in its own right** — `⟨ begin, record("Reflect"), complete, restart ⟩` — evaluated from initial state idle with empty durable Entry history, empty pending, **and a single fixed DaySlot ordinal for the whole vector** (CR4-02: v0.4 pinned three of SP-019's members and left the DaySlot ordinal free, while SP-023 makes that ordinal semantic — so two conforming runs at different DaySlots failed SP-091 equality with no clause violated), and **all six acceptance values are evaluated over that presented sequence and no other**. Every element must be disposed `ADMITTED`. Because SP-102 scopes T-facts to one presented sequence and SP-043 derives the count over it, `illegal_transition_count = 0` follows from the vector containing no state-illegal element, and **cannot be satisfied or defeated by any element outside the vector.** A proper suffix of a longer presented sequence is not this required vector, however closely its L-facts resemble the stated initial condition. The initial-condition qualification and the promotion from "might require" to "must produce" are authored, not founder-sealed. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B, P-L4-CR2 B.4-F6, P-L4-CR3 CR3-B01 | A-01, A-02, A-03 |
| SP-091 | **REVISED AGAIN (CR4-05).** *"Reference trace = Normalized Web trace = Normalized iOS trace, for every required vector."* Reproduced as the founder wrote it. v0.4 rendered this as "the reference **semantic** trace and **each** normalized target trace", which inserted a word into a claimed-exact reproduction and replaced two named traces with an unbounded quantifier satisfiable by an empty or singleton target set — strictly weaker than the sealed proposition, on attacks #3 and #9. The target-set cardinality is carried by SP-173. | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-C | — |
| SP-095 | **REVISED (CR4-01) · NEW in v0.4 (CR3-01) · the authored comparison rule, split out of SP-091.** The comparison SP-091 requires is performed over the **presented sequence** per SP-152, element by element, including each element's disposition and failed-requirement set. This sentence is authored: the phrase "presented sequence" appears nowhere in P-L1-A, P-L1-B, or P-L1-C, and SP-152 is `AUTHOR-PROPOSED`. It is stated here rather than inside SP-091 so that a founder-sealed row is never parameterized by an authored clause. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-C, P-L4-CR3 CR3-01 | — |
| SP-173 | **NEW (CR4-05) · the target-set cardinality SP-091 requires.** SP-091's equality is a **three-way** equality over a reference trace and **two** independently lowered target traces. It is not satisfied by an empty or singleton target set. The founder fixes this topology directly — *"TWO independently lowered targets → TWO observed trace sets → ONE conformance judgment"* — and titles the gate *Dual-Substrate Semantic Preservation*. **Naming the two substrates is not a representation choice:** SP-002 excludes runtime, language and storage mechanism from this program's *meaning*, and the identity of the two targets the proof compares is a property of the proof's topology, not of the ledger's semantics. An embodiment count below two makes the sealed Pass condition vacuous rather than satisfied. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-A, P-L1-B, P-L1-C, P-L4-CR4 CR4-05 | — |
| SP-096 | **NEW (CR3-08) · declared bound on the quantifier domain.** At the SemanticProgram layer the required-vector set is **the singleton containing SP-094's vector**. SP-091's quantifier therefore ranges over one member, and the SP-152 barrier is never exercised against the reference trace, because SP-094 mandates every element `ADMITTED`. Enlarging the required-vector set is a later movement and is not performed here. This clause states the bound rather than concealing it. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-C, P-L4-CR3 CR3-08 | — |
| SP-092 | **REVISED (CR3-15).** Semantic preservation fails if any of these diverges: legal transition behavior; illegal transition behavior; durable state; restart semantics; ordering; failure semantics; normalization; acceptance predicates. Divergence fails the proof "even if both **apps** look immaculate". (v0.3 substituted "embodiments" for the founder's "apps" without reporting the substitution; the founder's word is restored, and §15 records "embodiment" as this document's term for it.) | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-C | — |
| SP-093 | **REVISED · demoted.** Normalization may erase structural, visual, binary, runtime, and presentation differences, but may not erase any distinction needed to evaluate SP-090 through SP-092. The generalization from the founder's specific examples — differing SwiftUI/React lifecycles, differing persistence engines, differing internal object graphs — to "runtime and presentation differences" is authored. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B, P-L1-C | — |

### 11.1 Founder-trace satisfiability derivation

| Step | Governing clause and precondition | Required result |
|---|---|---|
| presentation | SP-150 | four elements presented; all disposed `ADMITTED` |
| initial | SP-040, SP-094 | state idle; pending zero; durable history empty |
| `begin` | current state is idle — SP-030, SP-160 step 3 | accepted; state active |
| `record("Reflect")` | state active; content present — SP-032, SP-160 step 3 | accepted; one pending contribution; state active |
| `complete` | state active; ≥1 pending — SP-034, SP-160 step 3 | accepted; state complete; one complete Entry "Reflect"; pending cleared |
| `restart` | same Ledger identity — SP-050, SP-051, SP-156 | every L-fact preserved; one boundary T-fact; boundary disposed `ADMITTED` |
| observation · five L-facts | observation at the **final presented index**, after every element including the terminal `restart` (**CORRECTED, CR4-10** — v0.4 read "the final admission ordinal", which is 3 and falls *before* the restart, so the sole required vector never observed anything post-restart even though "+ restart preservation" is a sealed scope member) | `state = complete`, `entries.count = 1`, `entries[0].content = "Reflect"`, `entries[0].status = complete`, `history_order = canonical` |
| observation · sixth value | **SP-013 witness T-fact stream** — *not* `view` | `illegal_transition_count = 0` over this presented sequence (SP-043, SP-102). **REVISED (CR3-10):** v0.3 derived all six from SP-110, but SP-110's codomain is the L-fact set and SP-102 places the count in the T-fact set, so `view` structurally cannot return it. The witness reaches it under SP-013. |

**No step supplies a Participant, role, capability, Operator, Observer, Assertion, Adjudication, or Establishment.** Every precondition is discharged by the state, the content string, and the presented sequence itself.

---

## 12. Falsifying traces

| Clause | Normative semantic clause | Source layer | CP | LP | L1 relation | Source pin | Open decision |
|---|---|---|---|---|---|---|---|
| SP-140 | A falsifying trace may test admitted semantics. It may not manufacture semantics. Where a docket item admits more than one normative model, no FT row may treat either model's observable consequence as falsifying. Such a row must restrict itself to consequences shared by all admitted models, or state its branch condition and remain inert until adjudication. An FT row that discriminates an admitted alternative is void, not authoritative. | L4 DERIVATION | AUTHOR-PROPOSED | DERIVED | ELABORATES | P-L2 §6.11, P-L4-CR1 CR-03 | — |
| SP-164 | **NEW (CR3-11) · P-L1-B constitutional law 2, reproduced.** *"Conformance vectors originate from canonical semantics, never from Web or iOS implementations."* | L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-B | — |
| SP-165 | **NEW (CR3-11) · the authored consequence of SP-164.** A conformance vector's input sequence and expected values must be derived from this SemanticProgram's clauses. A vector whose expected values are read off an embodiment's observed behaviour is **not a conformance vector** and may not be run — it would make the target its own oracle and prove only that an implementation agrees with itself. This applies to every required vector under SP-094 and SP-096 and to every FT row input. v0.3 legislated about vectors — declaring them malformed (SP-120), adopting one (SP-094), quantifying over them (SP-091) — while carrying no origination constraint at all; the word "originate" occurred nowhere in it. | AUTHORSHIP UNDER L2 | AUTHOR-PROPOSED | AUTHOR_PROPOSED | ELABORATES | P-L1-B law 2, P-L4-CR3 CR3-11 | — |

### 12.1 Trace suite

| Trace | Input | Expected normalized observation | Falsifying observation | Basis |
|---|---|---|---|---|
| FT-01 · founder success and restart | `begin → record("Reflect") → complete → restart` | all four elements `ADMITTED`; state complete; one Entry "Reflect" status complete; canonical history; zero illegal transitions; one restart boundary | any missing/extra Entry; changed content, status, or order; state other than complete; nonzero illegal count; any need for a capability, role, or adjudication input | SP-039, SP-090, SP-094, SP-130 |
| FT-02 · invalid transition refusal | presented sequence `⟨ record("Reflect") ⟩` from state idle | rejected `INVALID_TRANSITION` per SP-160 step 1; state idle; no pending; no Entry; `illegal_transition_count = 1` **over this presented sequence** | record accepted; any Entry or pending appears; refusal absent; any L-fact changes; reason other than `INVALID_TRANSITION`; **or a count that reflects any element outside this presented sequence** | SP-043, SP-102, SP-160, SP-163 |
| FT-03 · active restart — branch-parameterized | `begin → record("Reflect") → restart → complete` | **Shared by every admitted A-03 model, and the only falsifiable content of this row:** after restart, state active and one pending contribution "Reflect" in unchanged order; after complete, exactly one complete Entry "Reflect". | restart resets to idle; pending dropped or altered; pending order changed; lawful complete prevented; more or fewer than one Entry after complete | SP-050, SP-051, SP-084, SP-140 |
| | **A-03 branch note — inert until adjudicated.** Under A-03(A) the pending contribution already bears Entry identity across the restart; under A-03(B) it does not. Neither observation falsifies preservation. | | | |
| FT-04 · observation position | one record succeeds between positions `n` and `n+1`; observe at both | `view(n)` and `view(n+1)` each single-valued, differing by the new contribution; observing appends no T-fact and changes no L-fact | two different values at one position; an observation appending an outcome, advancing position, or altering the illegal count | SP-110–SP-113 |
| FT-05 · concurrency exclusion | active with pending `["A"]`; a vector presenting `record("B")` and `complete` without a determined admission order | the vector is **malformed** and must not be run | the vector is run and yields a result; or two embodiments run it and report different Entry sets as both conforming | SP-071, SP-120, SP-121 |
| FT-06 · ordered concurrency | the same two invocations, admitted in the stated order `record("B") < complete` | both accepted; Entries `[A, B]`; illegal count unchanged | any embodiment producing `[A]` with a rejected record for this input, i.e. silently re-serializing a supplied order | SP-071, SP-083, SP-121 |
| FT-07 · duplicate content and order | `begin → record("Reflect") → record("Reflect") → complete` | two distinct complete Entries, equal content, record order, distinct canonical positions | one Entry due to content deduplication; reversed or unstable order; ambiguous identity | SP-021, SP-073, SP-082 |
| FT-08 · **REVISED · derives from SP-160** | trace A: active with one pending → `complete`; trace B: state complete, pending empty → `complete` | A accepted, changes state and history. B: SP-160 step 1 applies first because state is not active, so the single reason is `INVALID_TRANSITION`, no L-fact changes, illegal count +1. | both normalize as "complete"; refusal loses T-fact presence; B creates or changes an Entry; **B emits `NO_RECORDED_CONTENT`, or emits either reason nondeterministically** | SP-034, SP-035, SP-038, SP-160 |
| FT-09 · day recurrence and active carry | trace A: complete → DaySlot boundary; trace B: active with one pending → DaySlot boundary | A becomes idle with history intact; B remains active, retains pending and origin DaySlot; both increment DaySlot | history deletion; active reset; pending loss; identical outcome for A and B; changed canonical order | SP-053, SP-074, SP-075 |
| FT-10 · restart fact partition | any state at position `n` → restart | `view(n+1) = view(n)` exactly; T-facts gain exactly one boundary marker; position advances by exactly one | any L-fact differs across the boundary; or no boundary marker emitted; or more than one emitted | SP-050, SP-051, SP-103, SP-104 |
| FT-11 · **REVISED (CR3-18) · confirmation-authority boundary, with its one discriminating falsifier and its declared limit** | `begin → record("X") → complete`, presented with no confirming actor, authority, or external attestation anywhere in the sequence; observed at every admission ordinal | all elements `ADMITTED`; state complete; one Entry "X" status complete; **and `view(n)` at every ordinal exposes no field beyond SP-019's L-fact set** | **the discriminating falsifier:** a distinct confirmed/unconfirmed surface exposed on state or Entry — an extra field outside SP-019's complete L-fact set, detectable by comparing `view(n)`'s domain against SP-019 at each ordinal | SP-003, SP-019, SP-060, SP-064, SP-110, P-L2 §6.2, §6.8 |
| | **Declared limit — CR3-18 accepted, not papered over.** v0.3 gave this row four falsifiers. Three had no discriminating power: "completion withheld pending confirmation" is already impossible under SP-034's biconditional and already falsified by FT-01; "a confirming role required to exist" is a verbatim duplicate of FT-01's falsifying column and is forbidden normatively by SP-039; and "Entry status presented as evidence the act occurred" is **not evaluable by the conformance witness at all** — SP-114 bounds the witness to `view(n)` and the T-fact stream, and presentation is excluded from the program's meaning by SP-002. Those three are withdrawn. **SP-003's external-claim prohibition is therefore not witness-falsifiable at the SemanticProgram layer**, and Cold Review 003's embodiment X — which implements these semantics exactly while publishing that `status = complete` certifies world occurrence — remains undetectable here. That is a real gap in falsification coverage, recorded rather than concealed; it is not repairable without importing presentation semantics, which §15 forbids. | | | |
| FT-12 · **REVISED (CR4-01) · capability disposition and failed-requirement visibility** | presented `begin → record("A") → record("B") → complete`, where one embodiment's substrate cannot support `record("B")` | that embodiment disposes `CAPABILITY_UNSUPPORTED(record("B"))` as a typed T-fact **naming its exact failed-requirement set**, and diverges visibly at presented index 3 from an embodiment disposing it `ADMITTED` | `record("B")` absent from the disposition record; Entries `[A]` and `[A, B]` both reported conforming; capability loss inferable only from the Entry count; the failed-requirement set absent from the compared record; **or a named member the substrate can in fact honor, or an unnamed member it cannot** | SP-150–SP-157, SP-167–SP-171, SP-091, SP-095, SP-152 |
| FT-13 · **REVISED (CR3-04 §3.5, CR4-01) · two different losses must not compare equal** | presented `begin → record("A") → record("B") → complete` to embodiment G′, which cannot hold a second pending contribution, and to H′, which can hold two but cannot preserve their canonical order and therefore declines | both dispose `record("B")` `CAPABILITY_UNSUPPORTED`; G′ names `{ SP-022 }` and H′ names `{ SP-024 }` by SP-168's computed invocation, **so SP-152 reports divergence at presented index 3** | G′ and H′ compared as conforming to each other; the failed-requirement set erased by normalization; a loss of canonical ordering — a member of P-L1-A's sealed scope list — reported as the same fact as a loss of capacity; **or both embodiments admitted to name one coarser common label, which SP-167 makes inexpressible and SP-170 forbids** | SP-151, SP-152, SP-155, SP-093, SP-167–SP-170 |
| FT-16 · **NEW (CR4-01) · the failed-requirement set must not be self-serving** | embodiment H′, which cannot preserve canonical order, declares `CAPABILITY_UNSUPPORTED(record("B"))` naming `{ SP-022 }` — a requirement it can in fact honor — in order to match G′'s record and compare equal | the record is **nonconforming under SP-155**, because SP-022's obligation is one H′ genuinely meets, and nonconforming under SP-169's maximality, because SP-024 is unnamed and unmet. Agreement obtained by misnaming is refuted against the substrate, not accepted as equality | H′ and G′ compared conforming on identical declared sets; the two-sided exactness test applied in only one direction; a reviewer unable to refute a named member because no closed requirement set exists to check it against | SP-155, SP-167, SP-168, SP-169, SP-152 |
| FT-14 · **NEW (CR3-B01) · the count has no existence outside its presented sequence** | DaySlot 1: presented sequence `⟨ complete ⟩` from idle, yielding `INVALID_TRANSITION` and count 1. DaySlot boundary. DaySlot 2: the SP-094 required vector presented as **its own** presented sequence `⟨ begin, record("Reflect"), complete, restart ⟩` | DaySlot 2's presented sequence begins with an empty T-fact set (SP-102), so `illegal_transition_count = 0` and the founder predicate holds; DaySlot 1's count is not carried | the DaySlot 2 observation reports a nonzero count; **or** an embodiment satisfies SP-094 by pointing at a proper suffix of a longer presented sequence whose count is nonzero; **or** any clause permits the count to accumulate across presented sequences | SP-043, SP-094, SP-102, SP-090 |
| FT-15 · **NEW (CR3-07) · the content-presence predicate is fixed, not embodiment-chosen** | presented `begin → record("") → complete → complete` | `record("")` is **present** under SP-162 and is accepted, appending one pending contribution with empty content; `complete` succeeds; the fourth element is state-illegal, so `illegal_transition_count = 1` over this presented sequence | an embodiment treats `record("")` as `MISSING_CONTENT`, reaching `NO_RECORDED_CONTENT` at element 3 and count 0 at element 4 — the divergence CR3-07 constructed, in which two embodiments differed on a **founder acceptance predicate** with no clause violated | SP-032, SP-162, SP-160, SP-043 |
| FT-16 · **NEW (CR3-13) · a boundary may not be capability-disposed** | presented `begin → record("A") → ⟨DaySlot boundary⟩ → complete` where an embodiment's substrate cannot represent the boundary | the boundary is disposed `ADMITTED` or the embodiment is nonconforming under SP-156 | the boundary disposed `CAPABILITY_UNSUPPORTED` and the run still reported conforming; or a DaySlot boundary silently omitted from the disposition record | SP-050, SP-053, SP-150, SP-156 |

**Commission §6.11 coverage:** successful operation FT-01 · refused operation FT-02, FT-08, FT-15 · contemplated discontinuity FT-03, FT-09, FT-10, FT-16 · visibility boundary FT-04 · **authority boundary FT-11, with its declared limit** · temporal/duplicate/conflict edge FT-06, FT-07 · operationally similar but semantically different FT-08 · capability accounting FT-12, FT-13 · scope of derived counts FT-14.

### 12.2 SP-R02-GAP-01 — closed, with its cause corrected

**v0.2 misstated the cause.** §12.2 of v0.2 asserted that removing the Operator gate destroyed the authority-boundary trace and that the commission requirement and the CR-01 repair were in genuine tension. Cold Review 002 Pass C answered **D**: commission §6.11's "authority boundary" means **confirmation** authority, never invocation capability. v0.1's FT-05 was a capability trace wearing an authority label, so withdrawing it removed nothing §6.11 required. There was no tension — there was a coverage gap over a boundary that already existed at SP-003 and SP-060, and a misdiagnosis of it.

**v0.3 overstated the closure.** Cold Review 003 tested FT-11's four falsifiers for discriminating power and found three duplicative or unevaluable, and constructed an embodiment that passes FT-11 while violating SP-003 — the clause FT-11 names as its basis. v0.4 does not repeat the overstatement.

```
GAP CLASS        trace-coverage defect, not an authority-ontology defect
BOUNDARY         confirmation authority — SP-003, SP-060, SP-064
COVERAGE         FT-11, reduced to its one discriminating falsifier
NEW SEMANTICS    none invented
A-07 RELATION    none; A-07 governs invocation capability, a different question
STATUS           PARTIALLY_CLOSED
RESIDUAL         SP-003's prohibition on presenting ledger completion as world
                 evidence is NOT witness-falsifiable: SP-114 bounds the witness
                 to view(n) and the T-fact stream, and SP-002 excludes
                 presentation from the program's meaning. No SemanticProgram-layer
                 trace can fail on it.
```

No authority ontology was invented to make commission test 8 green — and none is invented now to make this row look closed. The cause correction stands; the symptom is partially covered, and the uncovered part is named.

---

## 13. Founder decision docket

### 13.0 Closure classification — SP-R03 surface 3 · SP-R04 docket corrections

**The v0.2 defect.** Cold Review 002 B.3-F5 found A-01 labeled `OPERATIVELY_DECIDED` while its own note said its alternatives were "not excluded in principle" — the OPEN branch by the document's own rule — with structurally identical A-04 also labeled `OPERATIVELY_DECIDED`. The test was sound; its application was not, because the test never said what makes an alternative *admissible*.

**Sharpened test.** An alternative is **admissible** only if it is realizable as observable semantics under the current L-fact set. An alternative that asserts a semantic fact the program does not carry is not a conforming implementation choice — it is a request to change SP-019.

**REVISED (CR4-08) — the branch mapping is now genuinely a partition, because the v0.4 form was not one.** v0.4 restored an exclusivity conjunct and asserted the branches were "mutually exclusive and jointly exhaustive." Cold Review 004 falsified that: v0.4's third branch read *"NO for all but one member of `Adm(A)`"*, and for a **singleton** `Adm(A)` the set "all but one" is empty, so that branch is **vacuously true** and fires no matter what `T` returns. Its first branch, "YES for all members", also fires. OPEN and OPERATIVELY_DECIDED therefore both fired on **all five singleton items** — A-01, A-04, A-05, A-06, A-07 — which is every item the document classifies as decided. The claim of partition was the defect, not the labels.

The rule is restated over a set rather than over quantifier prose, which is what removes the vacuity:

> Let `Adm(A)` be the admissible alternatives, and let
> **`Y(A) = { x ∈ Adm(A) : an embodiment adopting x satisfies every normative SP clause }`**.
>
> `|Y| = 0` → **INCONSISTENT** — no conforming answer exists; the item is a defect, not a decision, and must be reported rather than classified
> `|Y| = 1` → **OPERATIVELY_DECIDED**
> `|Y| ≥ 2` and `Y = Adm(A)` → **OPEN**
> `|Y| ≥ 2` and `Y ⊊ Adm(A)` → **PARTIALLY_DECIDED** (list the excluded members)

**Why this is a partition.** The four branches are selected by `|Y| = 0`, `|Y| = 1`, and — for `|Y| ≥ 2` — the decidable predicate `Y = Adm`. These conditions are pairwise disjoint and cover every case, including the singleton case that defeated v0.4, where `|Y| ≤ 1` makes the `|Y| ≥ 2` branches unreachable by construction rather than by reading. **`INCONSISTENT` is new and is not a classification of convenience**: it exists so that an item with no conforming answer cannot be silently absorbed into `OPERATIVELY_DECIDED`, which v0.4's vacuous branch would have done. No current item is `INCONSISTENT`.

**Every label below is unchanged under the corrected rule**, verified item by item in §13.1: the five singletons have `|Y| = 1` → `OPERATIVELY_DECIDED`; A-02, A-03 and A-08 have `|Y| = |Adm| = 2` → `OPEN`. The repair corrects the mechanism that assigned the labels, not the labels — which is the distinction the governing criterion demands, and the one v0.4 failed here.

**Criterion reading fixed (CR3 §4.1b).** v0.3's criterion had two readings — an *observability* test ("realizable as observable semantics") and an *assertion* test ("asserts a semantic fact the program does not carry"). They diverge for any alternative positing an internal fact it never exposes in `view(n)`. **The assertion reading governs**, and it is the one applied below: an alternative is inadmissible when it requires a semantic fact absent from SP-019, whether or not that fact is exposed.

This resolves the v0.2 inconsistency without altering any normative semantics: A-01's alternatives A/B/C each assert an ownership relation as semantic fact, and SP-019 carries no owner coordinate, so they are inadmissible on the same ground as A-04's B/C. **The label was right; the note was wrong.** Corrected below.

### 13.1 Classification result — rerun over all items

| Item | Question | Admissible alternatives | Closure class | Installed branch |
|---|---|---|---|---|
| A-01 | Which entity owns the observable state? | **D only.** A, B, C each require an owner coordinate as semantic fact; SP-019 carries none. | **OPERATIVELY_DECIDED** | D — state exposed without owner attribution |
| A-02 | Relation between invoking complete and observing state complete? | **A and B admissible; C inadmissible (CORRECTED, CR3 §4.4).** SP-018 states only the literal field observation and SP-101 expressly admits both readings, so A and B stand. v0.3 recorded C admissible; under the assertion reading C posits distinct completion scopes as a scope-identity fact SP-019 does not carry, so C is inadmissible. `Adm = {A, B}`, T is YES for both. | **OPEN** *(label unchanged; justification corrected)* | none |
| A-03 | Does record create an Entry, mutate one, or create a non-Entry contribution? | **A and B admissible; C inadmissible** — SP-022 requires the contribution be *created*, excluding a pre-existing Entry mutated by record. | **OPEN — RECLASSIFIED (CR3 §4.3)** | none between A and B |
| A-04 | What maps a logical DaySlot to a civil day? | **A only.** B and C require timezone or participant-relative day as semantic facts; SP-019 carries none. | **OPERATIVELY_DECIDED** | A — DaySlot only |
| A-05 | Does RC-0001 need a world-fact observation and authority layer? | **A only.** B requires world-fact and authority-decision facts absent from SP-019, and SP-029/SP-048 admit no such operation. | **OPERATIVELY_DECIDED** | A — no additional layer |
| A-06 | Can completed Entry meaning later be corrected? | **A only.** B and C require a correction operation; SP-048 admits none. | **OPERATIVELY_DECIDED** | A — no correction |
| A-07 | **REFRAMED.** Does RC-0001 admit an invocation-capability precondition, and how is capability loss accounted for? | **(a) only.** (b) and (c) require an invoker-qualification fact the founder vector does not supply; SP-131 forbids any model that changes a disposition or outcome. | **OPERATIVELY_DECIDED** | (a) — no invocation gate; **capability loss typed, visible, and totally accounted under SP-150** |
| A-08 | **NEW.** P-L1-A excludes "no AI"; P-L1-B excludes "No generative AI." These differ in extent. Which governs RC-0001's exclusion boundary? | **Both admissible** — SP-004 reproduces both literally and resolves neither; no normative clause depends on the difference. | **OPEN** | none |
| A-09 | **NEW (CR4-07).** Over what is the illegal-transition count derived — one presented sequence, or cumulatively across sequences in a *durable daily* ledger? | **Both admissible against source.** L1 mentions the count exactly once (P-L1-B:120, `illegal_transition_count = 0`), inside a worked trace, **modalized** (*"the oracle might require"*), and scopes it nowhere. Verified: zero occurrences of reset / per-run / cumulative / across-runs in any pin. v0.3 read it cumulatively; v0.4 and v0.5 read it per presented sequence. | **OPERATIVELY_DECIDED — by this document's own installation, and flagged accordingly** | per-presented-sequence (SP-043, SP-102) |
| A-10 | **NEW (CR4-01).** How do RC-0001's two dispositions relate to RCP §5.3's closed five-member capability decision vocabulary, and to the CapabilityDecision record schema reserved to R-04? | **Not enumerable at this layer.** The alternatives live in the Protocol and in R-04, neither of which this movement may author. SP-171 declines the question rather than installing an answer. | **OPEN** | none — expressly reserved |
| A-11 | **NEW (CR4 §6, split from A-07).** By what scheme is capability loss accounted for? | **Unenumerated.** No alternative accounting scheme is enumerated anywhere in this corpus, so no `Adm` set exists to test. `Y` is therefore not computable and no closure class is earned. | **OPEN** | requirement-indexed accounting (SP-167–SP-171) — installed, not decided |

**Summary: OPEN 5 · PARTIALLY_DECIDED 0 · OPERATIVELY_DECIDED 6 · INCONSISTENT 0 · all eleven FOUNDER_DECISION_REQUIRED.**

**A-07 and Cold Review 004's divergence, recorded rather than overruled.** CR004 independently derived `PARTIALLY_DECIDED` for A-07 via constructions α/β, against this document's `OPERATIVELY_DECIDED`. The cause is that v0.4's A-07 asked **two** questions — is there an invocation gate, and how is loss accounted for — whose admissible sets differ, and no single closure class can be true of both. v0.5 splits them: A-07 keeps the gate question and is `OPERATIVELY_DECIDED` on it; the accounting question becomes **A-11** and is `OPEN` with an unenumerated `Adm`. **This is not a rejection of CR004's finding.** If a reviewer holds that the split is illegitimate and A-07 must remain compound, then CR004's `PARTIALLY_DECIDED` stands for the compound item and this document is wrong on that row. The split is offered as a more precise reading, not as an author's verdict over a reviewer's.

**A-09's classification is flagged, and the reason is a limitation of T(A) itself.** `T` quantifies over "every normative SP clause" — so **any** question this document's clauses already answer collapses to `|Y| = 1` and reads `OPERATIVELY_DECIDED`, including questions the author installed by choice against founder silence. A-09 is exactly such a case: the clauses that narrow `Y` (SP-043, SP-102) *are* the authored installation under review. The label is therefore reported as **decided-by-installation**, and is not evidence that the founder's question is closed. This limitation applies to A-09 alone among the eleven; the other ten are narrowed by SP-019's fact set or by source, not by a clause authored to settle the item. **Recorded as a residual in §18.2 rather than repaired, because repairing it means changing what `T` ranges over, which is beyond CR004's mandate.**

**Three items added, none created.** A-09, A-10 and A-11 disclose founder decisions that already existed — A-09 was operative in v0.3 and v0.4 without being docketed (CR4-07), A-10 is the protocol boundary SP-171 declines to cross, and A-11 was the undisclosed half of A-07 that v0.4 §13.2 already admitted was "an authored installation awaiting adjudication." **No new founder decision is required for this revision to be lawful**; these are pre-existing decisions made visible.

**A-03's reclassification, shown.** `Adm(A-03) = {A, B}` — §13.1 itself filters C, and Cold Review 003 verified SP-022 and agreed. SP-026 is a normative clause and states that *"Both models are normatively admitted; see SP-140"*, and SP-140 voids any FT row that discriminates them. So two embodiments adopting A and B respectively both satisfy every normative SP clause: T is **YES for every member of `Adm`**, which is the first branch — **OPEN**. `PARTIALLY_DECIDED` was reachable only under v0.2's superseded rule, in which C remained inside T's domain and returned NO. **The label survived the repair; the rule that generated it did not.** §13.1's own installed-branch cell already read "none between A and B", which is what OPEN describes.

**No normative semantics were changed to make a docket label true.** The changes in this section are: the restored exclusivity conjunct, the fixed criterion reading, A-03's reclassification, and corrected justifications for A-02, A-07 and A-08. SP-026, SP-140, SP-019 and SP-022 are untouched — the semantic freedom is exactly what it was; only its description is now accurate. **The docket describes semantic freedom. It does not create it.**

### 13.2 Decision detail — changes from v0.2 only

**A-01** · Corrected note: alternatives A, B, and C are **inadmissible**, not "not excluded in principle." Selecting one requires adding an owner coordinate to SP-019, which is a founder act, not an implementation choice.

**A-07** · Reframed by Repair 1. The question is no longer only "is there a gate" but "how is capability loss accounted for." Installed answer: no gate, and total typed accounting with a compared loss class. Consequence of (b) or (c): the sealed trace ceases to be self-sufficient and requires an input the founder never wrote. **Disclosure (CR3 §4.4):** the admissible-alternatives cell enumerates only the *gate* alternatives (a)/(b)/(c). **No alternative accounting scheme is enumerated anywhere in this corpus**, so the `OPERATIVELY_DECIDED` verdict is earned on the gate question alone. A founder cannot decide against unenumerated alternatives, and the accounting half of A-07 is therefore an authored installation awaiting adjudication, not a closed question.

**A-08** · Alternatives, **corrected (CR3 §4.4)**: (a) the narrower "No generative AI" governs, leaving non-generative AI unexcluded; (b) the broader "no AI" governs. v0.3 listed a third alternative — "both stand and the intersection governs" — which is **extensionally identical to (a)**, since the intersection of {all AI} and {generative AI} is {generative AI}. Three labels, two extents; the redundant label is withdrawn. Consequence: none for this candidate's semantics, but it bounds what a later RC-0001 target may contain. Recommendation: **none offered.** SP-004 reproduces both phrasings verbatim rather than resolving a founder difference by authorship.

**Why A-08 is open — disclosed (CR3-19).** Not merely because both strings are preserved. A-08 is open **by inertness**: per SP-166 there is no clause of the form "an embodiment containing X is nonconforming" for *any* member of the exclusion register, so §13.1's "no normative clause depends on the difference" is true because **no clause depends on the register at all**. A-08 would read as open no matter how carelessly it were handled, and the first clause that attempted to enforce an exclusion would force the question immediately. That is stated here so the founder adjudicates against the real situation.

**One observation, expressly not a resolution.** SP-004's register ranges over all three pins conjunctively, which leans extensionally toward (b). No clause reads the set, so no operative consequence follows, and the `OPEN` label stands.

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
| Q8 · permitted degradation | SP-050–SP-055, SP-113, SP-150, SP-151, SP-156, SP-159 | ANSWERABLE — **no L-fact degradation and no permitted adaptation**; an element the substrate cannot admit is disposed `CAPABILITY_UNSUPPORTED` with an exact failed-requirement set (SP-169), and no substitute semantics may be supplied |
| Q9 · required observer | SP-013, SP-110, SP-114 | ANSWERABLE — cited to normative clauses; §7.1 is a non-normative summary under §0.4 and is no longer the answering instrument (CR3-02) |
| Q10 · multi-party observability | SP-014, SP-112 | ANSWERABLE |
| Q11 · observer agreement | SP-112; FT-04 | ANSWERABLE |
| Q12 · required unobservability | SP-014 | ANSWERABLE — none required |
| Q13 · authority confirmation | SP-029, SP-060, SP-130, SP-153; FT-11 | ANSWERABLE |
| Q14 · required unconfirmed intent | SP-022, SP-026, SP-061, SP-064 | ANSWERABLE by clause. **FT-11 withdrawn as a citation (CR3-18):** FT-11 never observes the pending state between `record` and `complete`, so it does not exercise SP-064 and cannot witness this question. **No FT row currently witnesses recorded-intent-versus-accepted-fact**; commission §6.8's question remains clause-answered and trace-untested. |
| Q15 · authority transfer or establishment | SP-016, SP-039, SP-060 | ANSWERABLE — no operation transfers authority |
| Q16 · erasure versus falsification | SP-090–SP-094; FT-01–FT-12; §3.2 | EVALUABLE by a later extraction movement |

---

## 15. Representation firewall and namespace check

The author has seen representation-lineage material and makes no coldness claim. No semantic choice is justified by the vocabulary or capability of any representation under later test.

Founder acceptance vocabulary, bound here for the first time (**CR4-M5**): `entries` means the durable ordered Entry sequence of SP-019 under SP-024 canonical order; `entries.count` is its cardinality; **`entries[0]` is its first element under that order, indexing being zero-based**; `state` means the current-state value of SP-019; `status` means the completion status of SP-020. v0.4 pinned ten terms and none of these five, although all five appear in the founder's own acceptance trace and `[0]` fixes zero-basing only by the founder's notation rather than by any clause. Subject-local meanings: `canonical` means only the SP-024 comparator; `durable` means only the SP-050–SP-052 survival obligations; `pending` means only the SP-022 pre-complete effect; `view` means only the SP-110 projection; `disposition` means only the SP-150 accounting; `failed-requirement set` means only the SP-169 accounting; `semantic requirement` means only the SP-167 clause-identity set.

**Position vocabulary — REVISED (CR3-06).** v0.3 pinned `position` to a single meaning, the SP-071 admission ordinal, while SP-151 said a non-`ADMITTED` disposition "occupies a position". **CORRECTED (CR4-10):** v0.4 claimed "neither is called 'position' unqualified", which is false — SP-013, SP-021, SP-025, SP-053, SP-070, SP-072, SP-081, SP-110 and SP-111 all use *position* or *ordinal* in further senses, and §15 pinned only two of at least six coordinate terms. The two coordinates below are named separately and are the only two SP-152 and SP-157 compare; the remaining uses are **not** hereby pinned, and reconciling them is recorded as a residual in §18.2: **presented index** means the SP-157 ordinal over the presented sequence, assigned to every element; **admission ordinal** means the SP-071 ordinal, assigned only to admitted invocations.

**Content vocabulary — NEW (CR3-07).** `present`, of content, means only the SP-162 supply criterion. `absent` means only that no content value was supplied.

**Term mapping to the founder's vocabulary (CR3-15).** `embodiment` is this document's term for what P-L1-C calls an **app**. Where a founder-sealed row quotes the source, the founder's word is used and this mapping supplies the correspondence; the substitution is never made silently inside an `EXACT` row.

The candidate contains no database schema, storage-engine choice, serialization shape, interface flow, target-language construct, RealityIR, tolerance class, emitter design, resolver, oracle, representation option, F-05 tier selection, HBC accommodation, or implementation backlog. **It does declare a required-vector set** — the SP-094 singleton bounded by SP-096. v0.3's blanket "no RequiredVectors" was inaccurate as to the SemanticProgram layer and is corrected: what the candidate contains no representation-layer vector *artifacts* for is target execution, which remains a later movement.

---

## 16. Author-side conformance

### 16.1 Sealed-scope coverage

| Gate | Required L1 surface | Evidence | Result |
|---|---|---|---|
| S-01 | Ritual and Entry | SP-001, SP-017, SP-020–SP-022, SP-026 | PASS |
| S-02 | idle → active → complete; begin, record, complete | SP-030–SP-035, SP-041, SP-163 **(CR3-14: SP-018 withdrawn as evidence — it states a literal two-field observation "and nothing further" and asserts nothing about the progression)** | PASS |
| S-03 | invalid-transition and failure law | SP-031, SP-033, SP-035, SP-043, SP-160, SP-080–SP-083 | PASS |
| S-04 | durable Entry and restart preservation | SP-046, SP-050–SP-052, SP-084; FT-03, FT-10 | PASS |
| S-05 | canonical ordering, equivalent traces, acceptance predicates | SP-024, SP-044, SP-045, SP-090–SP-094 | PASS |
| S-06 | founder exclusions, non-goals, concrete founder trace | SP-004, SP-005, SP-090, SP-166 | **PASS as REPRODUCED, not as ENFORCED** — CR3-19 showed this gate did not say which it meant. SP-166 now states plainly that no clause enforces the register at the SemanticProgram layer. |
| S-07 | constitutional law 3: capability loss typed and explicit | SP-150–SP-157; FT-12, FT-13 | PASS — and **now genuinely typed and calibrated**: SP-152 compares the failed-requirement set, whose members are clause identities the embodiment cannot choose (CR4-01). v0.4 compared a type the loser named; v0.5 compares a type the program fixes |
| S-08 | **NEW** — constitutional law 2: vectors originate from canonical semantics | SP-164, SP-165 | PASS — v0.3 had no origination constraint at all (CR3-11) |
| S-09 | **NEW** — constitutional law 5: adaptation is a governed act | SP-158, SP-159 | PASS — v0.3 supplied no authorization concept (CR3-12) |

**SEALED-SCOPE COVERAGE 9/9. CORRECTED (CR4-M4).** v0.4 justified the gate by asserting that "laws 1, 4, 6 and 7 concern emitters, adaptation mechanics and promotion." That is false for two of the four. **Law 1** — *"Reference semantics are normative"* — has reference semantics, this artifact's own layer, as its subject, and is honoured rather than scoped out: SP-001 and SP-090 carry it. **Law 6** — *"Witness ≠ judgment"* — has witness and adjudication as its subject, and this candidate **does** carry a witness surface (SP-013, SP-051, §6.1, §11.1); no substantive contradiction of it was found, and SP-029 as revised under CR4-12 now states the scope explicitly. Laws 4 and 7 alone are emitter- and promotion-scoped. The gate result is unchanged; the rationale it rested on was wrong for half its members, which is the defect.

### 16.2 Finding disposition — Cold Review 004 first, then the Cold Review 003 record

**Cold Review 004 · the actual §4 finding set.** CR004's headline and §10 verdict block both report "NEW MATERIAL 7"; §4 carries `CR4-01` (BLOCKING) plus `CR4-02`…`CR4-12` — **eleven** MATERIAL — plus `CR4-M1`…`CR4-M5`. **The review is not edited**; its arithmetic defect is recorded here as reviewer-record evidence, and this document dispositions the twelve numbered findings and five minors that actually exist. Per-finding repair modes are at §0.5. The `CR4-01` repair mode is `IMPOSSIBLE`, and that word is used advisedly: v0.4 applied it to `CR3-04` and was wrong, which is the whole reason this revision exists — so the claim is stated with its counterexample (FT-13, FT-16) rather than asserted.

**Cold Review 004's independent verdicts that this document does not disturb:** `CR3-B01 CLOSED`; the thirteen CR-003 findings closed; `A-01`, `A-04`, `A-05` and `A-06` re-confirmed `OPERATIVELY_DECIDED` on grounds independent of SP-019's falsified exhaustiveness; §16.5's v0.4 tallies accurate. None is re-litigated below.

---

### 16.2.1 Cold Review 003 finding disposition — all 19 findings plus the regression items

Cold Review 003 returned `CHANGES_REQUIRED`: 1 BLOCKING, 13 MATERIAL, 5 MINOR, 3 of 16 threshold lines met. Every finding is dispositioned below. **Repair mode is stated per the governing criterion: a repair counts only if the normative representation either makes the defect IMPOSSIBLE or makes it EXPLICITLY DETECTABLE.**

| Finding | Sev | Root cause | Repair mode | Normative change | Post-repair expected result |
|---|---|---|---|---|---|
| **CR3-B01** | **BLOCKING** | The illegal-transition count had an increment rule, monotonicity and append-only-ness, but **no scope, no initial value and no reset point**; SP-094's initial condition could not name it because SP-103 makes L and T disjoint | **IMPOSSIBLE** | SP-043 and SP-102 scope the count and the whole T-fact set to one presented sequence; SP-094 makes the required vector a complete presented sequence whose six values are evaluated over it and no other, and denies satisfaction by a proper suffix | The CR-003 day-2 trace no longer satisfies SP-094 while failing the founder predicate: DaySlot 2's vector, presented as its own sequence, starts from an empty T-fact set and yields count 0. FT-14 falsifies any accumulation |
| CR3-01 | MATERIAL | An authored operative sentence sat inside a `FOUNDER_SEALED_L1 / EXACT` row, parameterizing a sealed row by an `AUTHOR-PROPOSED` clause | **IMPOSSIBLE** | SP-091 reduced to the founder's sentence alone; the comparison rule split out as SP-095, `AUTHOR-PROPOSED` — the SP-090/SP-094 technique applied one row down | No sealed row's content varies with an authored clause. §17.1 audits SP-091's single sentence |
| CR3-02 | MATERIAL | §7.1 asserted "the same presented sequence yields the same stream" of a class containing dispositions — false by construction of Repair 1 | **EXPLICITLY_DETECTABLE** | §7.1's T-fact law restated: the stream is a function of presented sequence **and** capability resolution; sameness is a conformance requirement compared under SP-152, not a property of the input. §14 Q9–Q12 re-cited to normative clauses | The false law is gone; the true relation is stated where §0.4 allows it no normative force |
| CR3-03 | MATERIAL | §17.3 named a regex "the authoritative enumeration" of `ORTHOGONAL` — a substantive entailment judgment delegated to a label-reader | **IMPOSSIBLE** | §17.3 hand-justifies every `ORTHOGONAL` row; the auditor supplies the count only and says so. SP-010 and SP-055 reclassified to `ELABORATES` on that re-audit | `ORTHOGONAL` 9 → 7, each with a stated argument. No relation judgment is delegated to the script |
| CR3-04 | MATERIAL | `CAPABILITY_DEGRADED` had two occurrences, no definition, no assignment rule, no coverage; and the loss class never entered the compared surface | **IMPOSSIBLE** | Token withdrawn (SP-150). SP-151 requires a declared loss class; **SP-152 compares it**; FT-13 exercises it | CR-003's G′/H′ pair, which compared equal under v0.3, now diverges at presented index 3 |
| CR3-05 | MATERIAL | 39 unmarked clause edits; sections labelled "preserved verbatim" had deleted normative text; SP-112's edit made it false | **IMPOSSIBLE** | Deleted text restored to SP-050, SP-071, SP-113; SP-112 repaired; four false headers corrected; §16.6 change register added; **the auditor gained a diff mode that FAILs on any changed row lacking a marker** | `UNMARKED_CHANGED_ROWS NONE`, mechanically checked against v0.3 |
| CR3-06 | MATERIAL | SP-151 said a non-`ADMITTED` disposition "occupies a position" while §15 pinned `position` to the admission ordinal only | **IMPOSSIBLE** | SP-157 separates **presented index** from **admission ordinal**; SP-071's element domain restored; §15 pins both | Neither reading survives; the position-indexed witness surface cannot misalign |
| CR3-07 | MATERIAL | No clause defined content presence, so SP-160 step 2's antecedent was undefined and two embodiments diverged lawfully on `record("")` | **IMPOSSIBLE** | SP-162 fixes presence as supply, not non-emptiness; SP-032 re-pointed; §15 pins the terms; FT-15 exercises it | CR-003's E1/E2 divergence is no longer available: one reading is normative |
| CR3-08 | MATERIAL | Nothing required a disposition to be **veridical**; SP-091's quantifier ranged over a singleton on which all elements are `ADMITTED` | **EXPLICITLY_DETECTABLE** | SP-155 makes a misdescribing disposition record nonconforming; SP-096 declares the singleton bound rather than concealing it | Two embodiments can no longer conform by both misreporting; the quantifier bound is disclosed, not hidden |
| CR3-09 | MATERIAL | SP-041's `EXACT` covered an operation→edge mapping and a `record` self-loop that appear in no L1 pin | **IMPOSSIBLE** | SP-041 reduced to reproduction of L1's two registers; the mapping moved to SP-163 as `AUTHOR-PROPOSED`; SP-161's justification narrowed to the law's **existence** | No authored inference wears a founder seal. The precedence rule stands on the narrower ground |
| CR3-10 | MATERIAL | §11.1 derived all six acceptance values from `view`, whose codomain is the L-fact set, while the sixth is a T-fact | **IMPOSSIBLE** | §11.1 split: five L-facts from SP-110, the count from the SP-013 witness stream | The vector's derivation cites an instrument that can actually return each value |
| CR3-11 | MATERIAL | L1 constitutional law 2 had **no operative surface**; "originate" occurred zero times while the document legislated about vectors | **IMPOSSIBLE** | SP-164 reproduces law 2; SP-165 states the authored consequence — a vector whose expectations are read off an implementation is not a conformance vector | Gate S-08 added; the anti-circularity law now binds every required vector and FT input |
| CR3-12 | MATERIAL | L1 constitutional law 5 was never engaged; degradation was unauthorized adaptation with no authorization concept anywhere | **IMPOSSIBLE** | SP-158 reproduces law 5; SP-159 forbids invented adaptation, substitution, approximation and accommodating reorder | Gate S-09 added. With `CAPABILITY_DEGRADED` withdrawn there is no adaptation route left to authorize |
| CR3-13 | MATERIAL | SP-150 made boundaries disposable while SP-050 permitted them no degradation — two clauses unsatisfiable together for a degraded boundary | **IMPOSSIBLE** | SP-156: a discontinuity boundary's only lawful disposition is `ADMITTED`; FT-16 witnesses it | The conflict is resolved on its face, and the previously uncovered DaySlot mis-disposition is now caught |
| CR3-14 | MINOR | SP-018 cited in §16.1 S-02 and §10 for propositions it expressly disclaims | **IMPOSSIBLE** | Both citations withdrawn and re-pointed to SP-041/SP-163 | The row was always faithful; the misuse is removed |
| CR3-15 | MINOR | Residual `EXACT` paraphrase: SP-005 renamed three of four comparanda, SP-046's scope was set by authored clauses, SP-092 substituted "embodiments" for "apps", SP-004 mis-rendered P-L1-C; §17.2 was false | **IMPOSSIBLE** | All four rows restored to the founder's words; §17.2 rewritten to state what was actually attempted | Each `EXACT` row now reproduces source wording; the term mapping lives in §15 |
| CR3-16 | MINOR | A tenth `EXACT` judgment sat in §10's relation column, outside both audits and structurally invisible to the auditor | **EXPLICITLY_DETECTABLE** | §10's Ledger·Ritual row reclassified to `ELABORATES`; §17.1 states its coverage boundary | No `EXACT` claim exists outside §17.1's audit |
| CR3-17 | MINOR | §16.5 claimed "not hand-entered" while being hand-rewrapped, 22 lines to the program's 17 | **IMPOSSIBLE** | §16.5 pasted verbatim and unwrapped; regenerated to a fixpoint | A `diff` of a fresh run against the block now matches, which is what the section invites |
| CR3-18 | MATERIAL | FT-11's four falsifiers: three duplicative or unevaluable; embodiment X passes it while violating SP-003 | **EXPLICITLY_DETECTABLE — with a declared limit** | Three falsifiers withdrawn; the discriminating one kept; §12.2 downgraded to `PARTIALLY_CLOSED`; the uncoverable residual named; §14 Q14's FT-11 citation withdrawn | The row no longer claims coverage it does not have. **SP-003's external-claim prohibition remains not witness-falsifiable, and that is stated, not concealed** |
| CR3-19 | MINOR | The founder exclusion register is entirely inert, and the docket did not disclose that this is *why* A-08 is open | **EXPLICITLY_DETECTABLE** | SP-166 states the register's operative status; §13.2 discloses that A-08 is open by inertness; S-06 marked REPRODUCED not ENFORCED | The founder adjudicates A-08 against the real situation |
| CR-001 CR-09 (REGRESSED) | MATERIAL | v0.3 deleted the CR-09 rename and the "proves row grammar and nothing else" disclaimer while adding a global verdict token | **IMPOSSIBLE** | Rename and disclaimer restored, and the disclaimer moved **inside the program** so output and bound cannot be separated; `AUDIT_RESULT` renamed `SHAPE_AUDIT_RESULT`; §6.6's overreaching claims withdrawn | The apparatus states what it cannot prove, in its own bytes |
| CR-002 residue (B.2-F7, B.4·SP-041, B.4·SP-001, A-03) | MATERIAL | v0.3's §16.2 dispositioned twelve findings and omitted four | **EXPLICITLY_DETECTABLE** | B.2-F7 addressed at CR3-02; SP-041 at CR3-09; A-03 at §13.1; SP-001's residual quantifier softening left standing and named in §17.1 | No CR-002 finding is now undispositioned |

**Regression surfaces touched by these repairs**, listed so a reviewer knows where to attack: the T-fact scope change (SP-043, SP-102) reaches FT-02, FT-08, FT-14 and §11.1; the disposition-alphabet change (SP-150–SP-157) reaches §2.0, §7.1, SP-038, SP-055, SP-093, FT-12, FT-13, FT-16 and A-07; the `EXACT` restorations reach §16.1 and §17; the docket changes reach §13 only.

### 16.3 What was deliberately not touched

**Preserved because Cold Review 003 confirmed them, and this revision is bounded to CR-003's findings:**

| Mechanism | CR-003 verdict |
|---|---|
| L-fact / T-fact partition and T→L non-interference (SP-103, SP-104, SP-105) | `L/T non-interference — holds`. CR-003 §2.20 records that a proposed BLOCKING breach was **killed** by the reviewer: capability resolution is a common cause, not a T-fact read |
| Ordered admission (SP-071, SP-120, SP-121) | CR-05 CLOSED; the ordering mechanism survives. Only SP-071's deleted element domain is restored |
| `view(n)` purity (SP-110, SP-111, SP-114) | CR-07 CLOSED. SP-112 and SP-113 are repaired for CR3-05, not redesigned |
| FT-03 neutrality and SP-140 | CR-03 CLOSED; re-ran under both A-03 models with identical falsifiers |
| Assertion / Adjudication / Establishment prohibition (SP-029, SP-039, SP-048, SP-060) | CR-01 CLOSED; "no Operator is reachable". **Not reintroduced by any repair here** |
| Deterministic refusal precedence (SP-160) | **TOTAL** — 18/18 `EXACTLY_ONE`, enumerated twice independently. SP-160's precedence text is unchanged; only SP-161's *justification* is narrowed and SP-162 supplies step 2's missing antecedent |
| L1-governs-L3 lineage (§0.1) | Unchanged |
| The capability barrier's core mechanism (SP-152 comparison over the presented sequence) | B.1-F1 **CLOSED**; CR-003 could not reconstruct the escape by any route. v0.4 extends the compared tuple with the loss class and does not alter the comparison's basis |

### 16.6 Change register — every SP row changed from v0.4, mechanically generated

CR3-05's defect was that v0.3 asserted verbatim preservation over text it had edited. The remedy is not a better assurance; it is a check that fails. §16.4's auditor accepts the prior version as a second argument and reports `ROWS_ADDED`, `ROWS_REMOVED`, `ROWS_CHANGED` and — the one that matters — `UNMARKED_CHANGED_ROWS`, any row whose bytes differ from the prior version without carrying a change marker. The diff block in §16.5 is that output, run against v0.4.

**9 added · 0 removed · 13 changed · 0 unmarked.** The nine added rows are SP-167–SP-171 (the `CR4-01` repair), SP-172 (`CR4-04` split), SP-173 (`CR4-05` cardinality), SP-174 (`CR4-06` split) and SP-175 (`CR4-10` post-boundary observation). **Nothing was removed**, and in particular nothing bearing on `CR3-B01`.

**Non-row changes, declared by hand** because the diff covers SP rows only: the header and §0.6 (new); §0.5 register (rewritten for CR-004); §2.0 preamble, diagram and the new §2.0.1 invocation table; §11.1's observation row; §13.0's branch rule and §13.1's three new docket items; §15's corrected coordinate claim and new acceptance-vocabulary bindings; §16.1's corrected rationale; §16.2's new CR-004 preamble; §16.4 and §16.5 (rewritten); §17.1's corrected tally and SP-158 audit row; §17.3's SP-029 justification; §18 and §19 (rewritten).

**One deliberate non-restoration, carried forward.** SP-051's v0.2 sentence *"the outcome stream is otherwise unchanged"* remains deleted, for the reason v0.3 gave and CR-002 B.2-F7 accepted.

**What this register cannot tell you.** That the changes are *correct*. It reports which bytes moved and whether the author admitted moving them. Cold Review 004 found `CR4-11` in a row that was **byte-identical across v0.3 and v0.4** and carried no marker at all — a defect no diff can surface, because nothing changed. A clean change register is evidence about honesty, not about soundness.

### 16.4 Mechanical evidence — regenerated, and bounded to what it measures

**The law applied, unchanged:** a mechanical evidence claim must be generated by the measurement it describes, not manually synchronized with it.

**The bound restored — CR-001 CR-09, which v0.3 regressed.** v0.2 headed this section *"Metadata-shape audit — renamed per CR-09"* and opened *"This audit proves row grammar and nothing else. It cannot establish source fidelity, semantic entailment, or state-machine determinacy."* v0.3 deleted the rename and the disclaimer, substituted *"the script governs"*, and simultaneously introduced a global `AUDIT_RESULT` verdict token that v0.2's block never contained. **The evidence apparatus grew a pass/fail verdict at the same moment it lost the sentence saying what it cannot prove.** Both the rename and the disclaimer are restored, and the disclaimer is now carried inside the program itself so it cannot be separated from its output.

**What Cold Review 003 proved about the v0.3 auditor, and what v0.4 does about each finding.**

| CR-003 probe | v0.3 result | v0.4 result | Mechanism |
|---|---|---|---|
| PROBE-A2 · empty file | PASS | **FAIL** | positive structure checks: an envelope heading, SP rows, FT rows, Q rows and docket items must all be present |
| PROBE-A5 · second `## 17.` heading truncating the envelope | PASS, 3 metrics silently zeroed | **FAIL** | `ENVELOPE_HEADINGS` must be exactly 1 |
| PROBE-5 · clause row smuggled after the boundary | PASS, row invisible | **FAIL** | `ROWS_OUTSIDE_ENVELOPE` flags any row carrying all four metadata fields outside the envelope; §17's own SP-shaped tables carry none and do not trip it |
| fence injection · row-shaped line inside the code fence | ingested as a founder-sealed clause | **not ingested** | fenced blocks are stripped before scanning |
| PROBE-A3 · honest `CONFLICTS` relabel | **FAIL — the gate punished candour** | **PASS, with `DISCLOSED_CONFLICTS`** | an adopted `CONFLICTS` is a disclosure to be reported, not a shape violation; concealment no longer scores better than honesty |
| PROBE-A9 · ontology `PROHIBITS` verdict from the word "no"/"not" | asserted a verdict | **verdict withdrawn** | `ONTOLOGY_ROWS` now lists row IDs only; classification was never a measurement |
| adjacent duplicate field tokens | evaded arity check | **caught** | lookahead so a match cannot consume the delimiter the next match needs |
| non-UTF-8 locale | crash | **fixed** | explicit `encoding='utf-8'`; argv guard added |
| CR3-05 · unmarked clause edits | invisible | **detected** | optional second argument diffs against the prior version and fails on any changed row lacking a `NEW`/`REVISED`/`RECLASSIFIED`/`WITHDRAWN` marker |

**What remains true and is NOT claimed away.** `SHAPE_AUDIT_RESULT PASS` on **v0.2 is still PASS**. The auditor cannot detect the six defects Cold Review 002 confirmed in that document, and no amount of structural checking will make it able to. It reads the labels the author typed. **A passing shape audit is evidence for row grammar and envelope shape, and for nothing else** — not for source fidelity, not for entailment, not for candidate health. Every claim in §16.5 is bounded accordingly, and §17 never delegates a relation judgment to it.

**What Cold Review 004 proved about the v0.4 auditor — `CR4-03`, and the rule it forces.** The block v0.4 published **did not execute**: a `SyntaxError` at document line 781, because the fence contained the script **twice** and the second copy lost its opening line prefix at a splice seam. The two copies differed at exactly the FT-row regex, so they disagreed on `FT_ROWS` (16 versus 17). §16.5's numbers were nonetheless correct, because they came from a *working copy in a scratch directory* — the numbers were true and their stated provenance was false. This is worse than a wrong number: it is a true number with a fabricated origin, published under a sentence claiming it was *"produced by running the §16.4 script against this file."*

**The rule that replaces manual seam-fixing.** Excising this one duplicate would repair the instance and leave the mechanism. v0.5 installs the chain as a machine check the program performs on itself:

```
embedded executable  →  extract exact shipped bytes  →  execute extracted bytes
                     →  capture output  →  compare with published evidence
```

| Check | What it makes impossible |
|---|---|
| `FENCE_PARSE_FAILURES` | every `python`-tagged fence in the artifact is `compile()`d. A truncated or spliced payload cannot be published, because it cannot parse. This alone catches the v0.4 defect. |
| `FENCE_DUPLICATE_PAYLOADS` | every fence is scanned for a contiguous run of ≥5 substantial lines occurring twice. A duplicated body is caught **even when the duplicate happens to parse** — the case the parse check would miss. |
| `SHIPPED_BYTES_EXECUTED` | the running program re-extracts its own fence from the artifact and compares those bytes to the bytes it is executing. `IDENTICAL` is the only passing value. **A nearby working copy cannot masquerade as the shipped program.** |
| `PUBLISHED_EVIDENCE_MATCH` | the program compares its own measurement block against the block published in §16.5, located by *section heading*, not by a prose anchor that would match the script's own copy of that prose. |

Two hazards that produced this defect class are removed at the source rather than guarded against. The script never writes a literal triple-backtick — it builds one as `chr(96) * 3` — so its own body can no longer terminate the fence that carries it. And every document anchor is a **line-anchored regex** rather than a bare string, so the script cannot match its own source and count itself; this is why `ENVELOPE_HEADINGS` is 1 rather than 2.

**The self-check's own limit, stated rather than implied.** `PUBLICATION_INTEGRITY PASS` proves the published bytes are the executed bytes and that the published output is this program's output. It proves **nothing** about whether the measurements are the right measurements. A program that measured the wrong things perfectly would still report `PASS` here. The diff-mode block is deliberately printed *outside* the compared region, so running with a prior-version argument cannot falsify publication integrity — and correspondingly, the diff block carries no publication-integrity guarantee of its own.

**Reproduction — and this is now the only supported procedure.** Extract the fenced block below **from this file** and run the extracted bytes: `python3 <extracted> <this file> [prior version]`. Do not run a copy kept elsewhere; if you do, `SHIPPED_BYTES_EXECUTED` will report `DIVERGENT` with both digests, which is the check working, not a defect.

```python
#!/usr/bin/env python3
# RC-0001 SemanticProgram shape auditor v0.5 (CR4-03).
# Measures row grammar and envelope shape; verifies its own publication integrity.
# It cannot judge a relation label, reach L1, or detect a semantic defect.
# Usage:  python3 <this-file> <artifact.md> [prior-version.md]
# The documented procedure is to EXTRACT this block from the artifact and run the
# extracted bytes. The script then proves that is what happened.
import sys, re, pathlib, hashlib
from collections import Counter
if len(sys.argv) < 2:
    print("USAGE: audit.py <artifact.md> [prior.md]"); raise SystemExit(2)
BT = chr(96) * 3                      # never write a literal fence inside this script
art = pathlib.Path(sys.argv[1])
txt = art.read_text(encoding='utf-8')

# ---- envelope -------------------------------------------------------------
# Anchored patterns, never bare strings: a bare literal would match this script's
# own source and count itself as a heading. Indented source lines cannot match `^##`.
ENV_RX = r'^## 0\. Authority, scope, and provenance'
TRM_RX = r'^## 17\. Provenance entailment review'
env_n = len(re.findall(ENV_RX, txt, re.M))
me_, mt_ = re.search(ENV_RX, txt, re.M), re.search(TRM_RX, txt, re.M)
i = me_.start() if me_ else -1
j = mt_.start() if mt_ else -1
norm = txt[i:j] if (i >= 0 and j > i) else ''
fence_rx = re.compile('^' + BT + '.*?^' + BT, re.M | re.S)
norm_nofence = fence_rx.sub('', norm)
L = norm_nofence.split('\n')
SPROW = r'^\| (SP-\d{3}) '
sp = [l for l in L if re.match(SPROW, l)]
ids = [re.match(SPROW, l).group(1) for l in sp]
FIELDS = {
 'LAYER': r'\| (L1|L2|L3|L4 DERIVATION|AUTHORSHIP UNDER L2) (?=\|)',
 'CP':    r'\| (FOUNDER-DIRECTED|RCP-CONSTRAINED|AUTHOR-PROPOSED|UNRESOLVED) (?=\|)',
 'LP':    r'\| (FOUNDER_SEALED_L1|FOUNDER_DIRECTED_L3|COMMISSION_REQUIRED|AUTHOR_PROPOSED|DERIVED) (?=\|)',
 'REL':   r'\| (EXACT|ELABORATES|ORTHOGONAL|CONFLICTS) (?=\|)'}
viol, conflicts = [], []
for l, k_id in zip(sp, ids):
    for k, rx in FIELDS.items():
        if len(re.findall(rx, l)) != 1: viol.append((k_id, k, len(re.findall(rx, l))))
    if re.search(r'\| CONFLICTS (?=\|)', l): conflicts.append(k_id)
    if re.search(r'\| UNRESOLVED (?=\|)', l) and not re.search(r'A-\d{2}', l):
        viol.append((k_id, 'UNRESOLVED_NO_DOCKET', 1))
dup = sorted({x for x in ids if ids.count(x) > 1})
tail = fence_rx.sub('', txt[len(norm) + i:])
smuggled = [re.match(SPROW, l).group(1) for l in tail.split('\n') if re.match(SPROW, l)
            and all(re.search(rx, l) for rx in FIELDS.values())]
def dist(k): return dict(Counter(re.search(FIELDS[k], l).group(1) for l in sp if re.search(FIELDS[k], l)))
onto = [re.match(SPROW, l).group(1) for l in sp
        if re.search(r'assertion|adjudicat|establishment|reporter|contested', l, re.I)]
REPTERMS = (r'\b(SQLite|IndexedDB|SwiftData|Core Data|localStorage|sessionStorage|cookie|SQL|'
            r'database|filesystem|HTTP|WebSocket|DURABLE_LOCAL|tier|scalar|Option [ABC]|'
            r'Postgres|MySQL|Redis|MongoDB|JSON|YAML|ORM|on disk|REST|gRPC|S3)\b')
rep = [(re.match(SPROW, l).group(1), m) for l in sp for m in re.findall(REPTERMS, l, re.I)]
ortho = [re.match(SPROW, l).group(1) for l in sp if re.search(r'\| ORTHOGONAL (?=\|)', l)]
exact = [re.match(SPROW, l).group(1) for l in sp if re.search(r'\| EXACT (?=\|)', l)]
ft = len([l for l in L if re.match(r'^\| FT-\d{2} · ', l)])
q  = len([l for l in L if re.match(r'^\| Q\d+ · ', l)])
dk = len([l for l in L if re.match(r'^\| A-\d{2} \| ', l)])

# ---- publication integrity: every fenced block in the artifact (CR4-03) ---
fences, k = [], 0
lines = txt.split('\n')
while k < len(lines):
    if lines[k].startswith(BT):
        tag = lines[k][len(BT):].strip(); start = k
        k += 1
        while k < len(lines) and lines[k].rstrip() != BT: k += 1
        fences.append((tag, start + 1, k, lines[start + 1:k]))
    k += 1
def longest_repeat(body):
    """Longest contiguous run of >=5 substantial lines occurring more than once."""
    sub = [x for x in body if len(x.strip()) > 12]
    best = 0
    for a in range(len(sub)):
        for b in range(a + 5, len(sub) + 1):
            blk = '\n'.join(sub[a:b])
            if '\n'.join(sub[b:]).find(blk) >= 0: best = max(best, b - a)
            else: break
    return best
parse_fail, dup_payload = [], []
for tag, ln, _end, body in fences:
    src = '\n'.join(body)
    if tag == 'python':
        try: compile(src, f'<fence@{ln}>', 'exec')
        except SyntaxError as e: parse_fail.append((ln, f'line {e.lineno}: {e.msg}'))
    r = longest_repeat(body)
    if r >= 5: dup_payload.append((ln, f'{r} duplicated lines'))

# ---- shipped-bytes identity: did we run what the artifact publishes? ------
me = pathlib.Path(sys.argv[0]).read_text(encoding='utf-8') if pathlib.Path(sys.argv[0]).exists() else ''
shipped = next(('\n'.join(b) for tg, _l, _e, b in fences if tg == 'python'), None)
if shipped is None:                      shipped_state = 'NO_PYTHON_FENCE_IN_ARTIFACT'
elif me.rstrip('\n') == shipped.rstrip('\n'): shipped_state = 'IDENTICAL'
else:                                    shipped_state = ('DIVERGENT executed=' +
    hashlib.sha256(me.encode()).hexdigest()[:12] + ' shipped=' + hashlib.sha256(shipped.encode()).hexdigest()[:12])

# ---- diff mode ------------------------------------------------------------
diff_out = []
if len(sys.argv) > 2:
    pt = pathlib.Path(sys.argv[2]).read_text(encoding='utf-8')
    pe_, pt_ = re.search(ENV_RX, pt, re.M), re.search(TRM_RX, pt, re.M)
    pl = fence_rx.sub('', pt[pe_.start():pt_.start()]).split('\n')
    prev = {re.match(SPROW, l).group(1): l for l in pl if re.match(SPROW, l)}
    cur = {k2: v for k2, v in zip(ids, sp)}
    added = sorted(set(cur) - set(prev)); removed = sorted(set(prev) - set(cur))
    changed = sorted(k2 for k2 in set(cur) & set(prev) if cur[k2] != prev[k2])
    unmarked = [k2 for k2 in changed if not re.search(r'\*\*(REVISED|NEW)', cur[k2])]
    diff_out = [f"DIFF_BASE              {pathlib.Path(sys.argv[2]).name}",
                f"ROWS_ADDED             {len(added)} -> {added}",
                f"ROWS_REMOVED           {len(removed)} -> {removed}",
                f"ROWS_CHANGED           {len(changed)} -> {changed}",
                f"UNMARKED_CHANGED_ROWS  {len(unmarked)} -> {unmarked or 'NONE'}"]

# ---- positive structure checks: an empty or gutted file must FAIL ---------
positive = []
if env_n != 1:       positive.append(('ENVELOPE_HEADINGS', env_n))
if not norm:         positive.append(('NO_ENVELOPE', 0))
if len(sp) < 50:     positive.append(('TOO_FEW_SP_ROWS', len(sp)))
if ft == 0:          positive.append(('NO_FT_ROWS', 0))
if q == 0:           positive.append(('NO_Q_ROWS', 0))
if dk == 0:          positive.append(('NO_DOCKET_ITEMS', 0))
if not exact:        positive.append(('NO_EXACT_ROWS', 0))
if smuggled:         positive.append(('ROWS_OUTSIDE_ENVELOPE', len(smuggled)))
if parse_fail:       positive.append(('FENCE_PARSE_FAILURES', len(parse_fail)))
if dup_payload:      positive.append(('FENCE_DUPLICATE_PAYLOADS', len(dup_payload)))
if shipped_state not in ('IDENTICAL',): positive.append(('SHIPPED_BYTES', shipped_state))

core = [
 f"ENVELOPE_HEADINGS      {env_n} (must be exactly 1)",
 f"NORMATIVE_SP_ROWS      {len(sp)}",
 f"UNIQUE_IDS             {len(set(ids))}",
 f"DUPLICATE_IDS          {dup or 'NONE'}",
 f"SHAPE_VIOLATIONS       {viol or 'NONE'}",
 f"DISCLOSED_CONFLICTS    {conflicts or 'NONE'}",
 f"ROWS_OUTSIDE_ENVELOPE  {smuggled or 'NONE'}",
 f"LAYER_DIST             {dist('LAYER')}",
 f"CP_DIST                {dist('CP')}",
 f"LP_DIST                {dist('LP')}",
 f"REL_DIST               {dist('REL')}",
 f"EXACT_ROWS             {len(exact)} -> {exact}",
 f"ORTHOGONAL_ROWS        {len(ortho)} -> {ortho}",
 f"ONTOLOGY_ROWS          {len(onto)} -> {onto}",
 f"REPRESENTATION_HITS    {len(rep)} -> {rep or 'NONE'}",
 f"FT_ROWS                {ft}",
 f"Q_ROWS                 {q}",
 f"DOCKET_ITEMS           {dk}",
 f"TRAILING_WHITESPACE    {len([l for l in txt.split(chr(10)) if l != l.rstrip()])}",
 f"FENCED_BLOCKS          {len(fences)}",
 f"FENCE_PARSE_FAILURES   {parse_fail or 'NONE'}",
 f"FENCE_DUPLICATE_PAYLOADS {dup_payload or 'NONE'}",
 f"STRUCTURE_FAILURES     {positive or 'NONE'}",
 f"SHAPE_AUDIT_RESULT     {'FAIL' if (viol or dup or rep or positive) else 'PASS'}",
 "SCOPE                  row grammar, envelope shape and publication integrity only;"
 " no relation label is verified"]
# `core` is the block published in 16.5 and the only block compared against it.
# diff_out is printed after it and is deliberately outside the compared region,
# so running with a prior-version argument cannot falsify publication integrity.
print('\n'.join(core + diff_out))

# ---- publication-integrity verdict, printed AFTER and never self-compared -
# Locate the published block by SECTION, searching after the heading. Anchoring on a
# prose string would find this script's own copy of it, which precedes 16.5 in the file.
pub, mh = None, re.search(r'^### 16\.5 Generated evidence', txt, re.M)
if mh:
    seg = txt[mh.end():]
    o = seg.find('\n' + BT + '\n')
    if o >= 0:
        s = o + len('\n' + BT + '\n')
        pub = seg[s:seg.index('\n' + BT, s)]
match = 'NO_PUBLISHED_BLOCK' if pub is None else ('IDENTICAL' if pub == '\n'.join(core) else 'DIVERGENT')
print('\n'.join([
 "",
 "-- publication integrity (excluded from the compared block above) --",
 f"SHIPPED_BYTES_EXECUTED   {shipped_state}",
 f"PUBLISHED_EVIDENCE_MATCH {match}",
 f"PUBLICATION_INTEGRITY    {'PASS' if (shipped_state == 'IDENTICAL' and match == 'IDENTICAL') else 'FAIL'}"]))
```

**Validation of the auditor, stated precisely (CR-003 §6.5).** Run against v0.2 (`611a782e…feb007`), it reproduces the tallies Cold Review 002 independently recomputed by hand. **That establishes measurement validity for those tallies, as tallies, and nothing more.** It establishes nothing about whether they are the right quantities, whether the envelope is the right scope, or whether any labelled relation is true. v0.3 claimed the auditor *"detects the defect it was built to prevent, on the document that had it"* — **that claim is withdrawn.** The program printed two numbers; a human compared them to prose and found the discrepancy. No code in it reads any prose claim.

**Generated output:** §16.5, pasted verbatim from the program's stdout with no rewrapping.

### 16.5 Generated evidence

Produced by extracting the §16.4 block from this file and running the extracted bytes against this file. Pasted **verbatim and unwrapped** — v0.3's block claimed "not hand-entered" while being hand-rewrapped (CR3-17), and v0.4's block was genuine output of a program that **was not the one it published** (CR4-03). The program now proves both properties itself; see the self-verification block below. Lines are long by design; they are the program's own bytes.

```
ENVELOPE_HEADINGS      1 (must be exactly 1)
NORMATIVE_SP_ROWS      111
UNIQUE_IDS             111
DUPLICATE_IDS          NONE
SHAPE_VIOLATIONS       NONE
DISCLOSED_CONFLICTS    NONE
ROWS_OUTSIDE_ENVELOPE  NONE
LAYER_DIST             {'L1': 11, 'L2': 7, 'AUTHORSHIP UNDER L2': 77, 'L4 DERIVATION': 15, 'L3': 1}
CP_DIST                {'FOUNDER-DIRECTED': 12, 'RCP-CONSTRAINED': 4, 'AUTHOR-PROPOSED': 91, 'UNRESOLVED': 4}
LP_DIST                {'FOUNDER_SEALED_L1': 11, 'COMMISSION_REQUIRED': 7, 'AUTHOR_PROPOSED': 77, 'DERIVED': 15, 'FOUNDER_DIRECTED_L3': 1}
REL_DIST               {'EXACT': 11, 'ELABORATES': 92, 'ORTHOGONAL': 8}
EXACT_ROWS             11 -> ['SP-001', 'SP-004', 'SP-005', 'SP-158', 'SP-018', 'SP-041', 'SP-046', 'SP-090', 'SP-091', 'SP-092', 'SP-164']
ORTHOGONAL_ROWS        8 -> ['SP-171', 'SP-014', 'SP-016', 'SP-029', 'SP-048', 'SP-054', 'SP-072', 'SP-081']
ONTOLOGY_ROWS          6 -> ['SP-029', 'SP-101', 'SP-039', 'SP-048', 'SP-060', 'SP-140']
REPRESENTATION_HITS    0 -> NONE
FT_ROWS                17
Q_ROWS                 16
DOCKET_ITEMS           11
TRAILING_WHITESPACE    0
FENCED_BLOCKS          12
FENCE_PARSE_FAILURES   NONE
FENCE_DUPLICATE_PAYLOADS NONE
STRUCTURE_FAILURES     NONE
SHAPE_AUDIT_RESULT     PASS
SCOPE                  row grammar, envelope shape and publication integrity only; no relation label is verified
```

**Diff-mode output against v0.4, demonstrating the CR3-05 check.** Printed outside the compared region by design, so a diff run cannot falsify publication integrity:

```
DIFF_BASE              OURSELF-RCP-RC0001-DURABLE-DAILY-RITUAL-LEDGER-SEMANTICPROGRAM-v0.4-CANDIDATE.md
ROWS_ADDED             5 -> ['SP-167', 'SP-168', 'SP-169', 'SP-170', 'SP-171']
ROWS_REMOVED           0 -> []
ROWS_CHANGED           5 -> ['SP-095', 'SP-151', 'SP-152', 'SP-155', 'SP-159']
UNMARKED_CHANGED_ROWS  0 -> NONE
```

**Publication integrity — the `CR4-03` repair, self-reported.** This block is excluded from the comparison above, so it cannot certify itself:

```
-- publication integrity (excluded from the compared block above) --
SHIPPED_BYTES_EXECUTED   IDENTICAL
PUBLISHED_EVIDENCE_MATCH IDENTICAL
PUBLICATION_INTEGRITY    PASS
```

**Cross-checks a reviewer should run, each bounded to what it measures:**

```
ENVELOPE_HEADINGS        must be exactly 1, or the envelope is undefined
EXACT_ROWS               count only. Section 17.1 must justify each ID substantively;
                         the machine cannot check that and does not claim to
ORTHOGONAL_ROWS          count only. Section 17.3 justifies each row by hand;
                         the auditor is NOT the authority for this judgment
ONTOLOGY_ROWS            row IDs only. No PROHIBITS verdict is emitted
UNMARKED_CHANGED_ROWS    must be NONE when run against the prior version
ROWS_OUTSIDE_ENVELOPE    must be NONE
REPRESENTATION_HITS      0, for the listed terms in SP rows only; prose is unscanned
FENCE_PARSE_FAILURES     must be NONE — a published program that cannot parse is not evidence
FENCE_DUPLICATE_PAYLOADS must be NONE — catches a duplicated body that still parses
SHIPPED_BYTES_EXECUTED   must be IDENTICAL, or you did not run what this file publishes
PUBLISHED_EVIDENCE_MATCH must be IDENTICAL, or the numbers above are not this program's
```

**What a reviewer should still not conclude from any of it.** `SHAPE_AUDIT_RESULT PASS` on **v0.2 is still PASS** — the auditor cannot detect the six defects Cold Review 002 confirmed there, and `PUBLICATION_INTEGRITY PASS` does not change that by one line. Publication integrity proves the numbers are honestly sourced. It does not make them the right numbers, and no structural check ever will.

---

## 17. Provenance entailment review — SP-R03 surface 4 · SP-R04 surfaces 3, 6, 10, 11

`EXACT` is a substantive judgment, falsifiable by a reviewer. A mechanical script may audit completeness; it may never award `EXACT`.

**Nine attacks applied to every claim:** missing source member · extra candidate member · narrower proposition · wider proposition · added precondition · removed consequence · changed subject · changed temporal boundary · changed quantifier or modality.

### 17.1 Re-audit of every EXACT claim

**Coverage boundary, stated (CR3-16).** This subsection audits **every `EXACT` claim in the document**, which is exactly the eleven rows the auditor enumerates in §16.5 plus nothing else. v0.3 carried a twelfth `EXACT` judgment in §10's relation column, structurally invisible to the auditor's `^\| (SP-\d{3}) ` regex and absent from this audit; that row is reclassified to `ELABORATES` in §10, so no `EXACT` claim now lies outside this table.

| Clause | Source proposition | Attacks applied | Result |
|---|---|---|---|
| SP-001 | P-L1-A: "Durable Daily Ritual Ledger / Ritual / Entry / idle → active → complete / begin / record / complete / + invalid transition law / + durability / + canonical ordering / + restart preservation / + equivalent state traces"; "A substrate-neutral semantic reality" | member-for-member both directions; all eleven members present in each; "substrate-neutral" matches the source word; v0.2's unsourced "observable" remains removed | **EXACT** · **declared residual (CR-003):** the quantifier "whose preserved meaning **includes**" is softer than a closed enumeration. It is retained because the founder's register is itself additive ("+ …") and a closed reading would overclaim exhaustiveness; the softening is disclosed rather than silently carried |
| SP-004 | P-L1-A five exclusions; P-L1-B six exclusions; P-L1-C seven non-goals | missing member — succeeded against v0.2, closed in v0.3; **rendering attack succeeded against v0.3 (CR3-15)**: P-L1-C is a semicolon-terminated bullet list, re-rendered as a comma list with an added article, under a lead-in claiming "literally and in full". Now reproduced in the source's own form, article removed, lead-in withdrawn. The "no AI" / "No generative AI" extent difference is preserved, not resolved, and docketed as A-08 | **EXACT** · falsify by naming a source exclusion absent from SP-004, or a rendering difference |
| SP-005 | P-L1-B: "semantic equivalence ≠ structural equivalence ≠ visual identity ≠ binary identity"; P-L1-C: "Even if both apps look immaculate" | **changed-subject attack succeeded against v0.3 (CR3-15)**: three of four comparanda were renamed — "structural equivalence" → "matching component structure", "visual identity" → "visual **similarity**", "binary identity" → "matching binaries" — and §17.2 then miscounted a four-term chain as three identity kinds. The founder's four terms are restored verbatim | **EXACT** |
| SP-158 | P-L1-B constitutional law 5: "Adaptation is a governed act. A substrate-specific workaround requires explicit authorization."; P-L1-C Emitter FORBIDDEN AUTHORITY: "invent capability adaptations" | quoted verbatim, both renderings byte-checked against the pins after CR4-M2 found the period and the connective "correspondingly" added in v0.4; the clause reproduces and asserts nothing further. The authored consequence is separated into SP-159, per the SP-090/SP-094 technique | **EXACT** · falsify by showing the quotation differs from the pin |
| SP-018 | P-L1-B worked trace: `state = complete` and `entries[0].status = complete` as separately named fields | changed subject — the clause says "the founder worked trace exposes", not "requires"; asserts nothing about the fields' relationship. **CR3-14 confirmed the row is faithful**; the two tables that misused it are corrected | **EXACT** |
| SP-041 | P-L1-A and P-L1-B, each carrying `idle → active → complete` and the list `begin` / `record` / `complete` as two separate unlabelled registers | **extra-candidate-member attack succeeded against v0.3 (CR3-09)**: L1 supplies no operation→edge mapping, and `active —record→ active` appears in no pin — L1's chain has two arrows. v0.3 asserted all three edges as "the founder-sealed transitions". SP-041 is now reproduction only; the mapping moved to SP-163 as `AUTHOR-PROPOSED` | **EXACT** · falsify by exhibiting L1 text assigning an operation to an edge |
| SP-046 | P-L1-A "+ durability", "+ restart preservation"; P-L1-B vector's post-restart Entry fields | **scope attack succeeded against v0.3 (CR3-15)**: the row was scoped by "a **contemplated** restart", a qualifier set by the `AUTHOR-PROPOSED` clauses SP-050 and SP-052 — an `EXACT` row whose extent depended on authored text. The qualifier is removed; the restart/destruction boundary is drawn in SP-050 and SP-052 where it belongs | **EXACT** |
| SP-090 | P-L1-B: "the oracle **might require**: …"; "If both substrates satisfy that normalized semantic trace, they conform." | modality and added-precondition attacks both succeeded against v0.2 and were closed in v0.3 by splitting off SP-094. **CR-003 recorded this as the best repair in the document and it is carried forward unchanged.** Re-verified: all six predicates reproduced, "might require" preserved | **EXACT** |
| SP-091 | P-L1-C: "Reference trace = Normalized Web trace = Normalized iOS trace, **for every required vector**" | changed-subject attack succeeded against v0.2 and was repaired in v0.3. **Extra-candidate-member attack then succeeded against v0.3 (CR3-01)**: an authored second sentence — "Comparison is over the presented sequence per SP-152" — sat inside the sealed row, and the phrase "presented sequence" occurs **0 times** across all three pins. That sentence is now SP-095, `AUTHOR-PROPOSED`. SP-091 is the founder's sentence alone | **EXACT** · falsify by finding the second sentence's proposition in L1 |
| SP-092 | P-L1-C Fail list, all eight items, plus "Even if both apps look immaculate" | member-for-member on all eight. **Changed-subject attack succeeded against v0.3 (CR3-15)**: "embodiments" was substituted for the founder's "**apps**" without report. The founder's word is restored and the term mapping is recorded in §15 | **EXACT** |
| SP-164 | P-L1-B constitutional law 2: "Conformance vectors originate from canonical semantics, never from Web or iOS implementations." | quoted verbatim; reproduces and asserts nothing further. The authored consequence is separated into SP-165 | **EXACT** · falsify by showing the quotation differs from the pin |

**Carried forward from v0.3's re-audit:** SP-093 remains `ELABORATES` — the generalization from the founder's specific SwiftUI/React/persistence examples to "runtime and presentation differences" is authored.

**`EXACT` claims: 11.** Nine survive from v0.3's set of nine, **six** of them repaired after a successful attack (SP-004, SP-005, SP-041, SP-046, SP-091, SP-092 — **six rows**, three of them repaired again in v0.5 under CR4-04, CR4-05 and CR4-06, plus the SP-091→SP-095 and SP-005→SP-172 splits). **CORRECTED (CR4-M1):** v0.4 wrote "four of them" and "five rows" over a parenthetical enumerating six — the tally-overstatement class CR-003 found in v0.3, recurring at reduced amplitude. Two are new, and both are verbatim reproductions of founder constitutional laws that v0.3 carried no surface for at all (SP-158 law 5, SP-164 law 2).

### 17.2 Attacks attempted that did not succeed

Stated precisely, because v0.3's version of this subsection was **false as written** (CR3-15): it claimed all nine attacks were attempted against SP-005, SP-018, SP-046 and SP-092 and none succeeded, while three of those four rows were in fact defective.

- **SP-018** — all nine attempted; none succeeded. The row survives as written, and CR-003 independently confirmed it is faithful.
- **SP-090** — all nine attempted against the repaired row; none succeeded. Independently re-verified by CR-003 against L1-72:106–122.
- **SP-158, SP-164** — the reproduction rows: member-for-member and modality attacks attempted; none succeeded. These are quotations, and the attack surface is correspondingly small.
- **SP-005, SP-041, SP-046, SP-091, SP-092, SP-004** — attacks **did** succeed against the v0.3 text of each; the repairs are recorded in §17.1 and the successful attack is named in every case rather than the row simply being rewritten.
- **SP-001** — eight of nine attacks failed; the quantifier-softening attack partially succeeds and the residual is declared in §17.1 rather than dismissed.

### 17.3 Non-EXACT relations — hand-justified, not delegated

**§17's own bound, restated: a mechanical script may audit completeness; it may never award a relation.** v0.3 stated that bound correctly for `EXACT` and then departed from it for `ORTHOGONAL`, naming the auditor's regex output "the authoritative enumeration" (CR3-03). The auditor reads the label the author typed and is structurally incapable of detecting a mislabelled row — which is precisely the defect CR-002 B.1-F2 found on SP-132. **The auditor supplies the count. This subsection supplies the judgment.**

`ELABORATES` rows add precision within regions the source leaves undefined. The load-bearing cases are SP-024 (the source says "canonical ordering" but supplies no comparator), SP-071 (equivalent traces required, no admission rule supplied), SP-050 (restart named, boundary undefined), SP-093, SP-094, SP-095, SP-096, SP-150–SP-157 (law 3 requires typed explicit capability loss but supplies no accounting mechanism), SP-159, SP-162, SP-163 and SP-165.

**Every `ORTHOGONAL` row, with its argument.** The test each must pass: *satisfiable or not without affecting any L1 proposition.*

| Clause | Argument | Verdict |
|---|---|---|
| SP-014 | No ledger fact is required to be hidden; confidentiality is not a semantic guarantee. No pin contains any proposition about confidentiality, access control, or who may read a fact. An embodiment that hid facts and one that hid none would both leave every L1 proposition — the scope list, the progression, the operations, the acceptance predicates — untouched | **ORTHOGONAL** |
| SP-016 | No operation grants, transfers, revokes, or establishes authority. L1 contains no authority-transfer proposition anywhere; the closest founder material is P-L1-C's *Emitter* FORBIDDEN AUTHORITY, which governs the compiler's emitter, not the ledger's operations | **ORTHOGONAL** |
| SP-029 | An **existence** prohibition on confirmer / amender / invalidator / Reporter / Assertion / Adjudicator / Adjudication / Establishment constructs. L1 **does** speak to one of them — `Adjudication` is a canonical-stack stage (P-L1-A:25, P-L1-B:21), protocol layer 11 (P-L1-C:26), the subject of constitutional law 6, and forbidden to the emitter (P-L1-C:55). v0.4's justification claimed the opposite and was false (CR4-12). The relation is `ORTHOGONAL` on **scope**, the same argument the SP-016 row makes: SP-029 now says "in this SemanticProgram's ontology", and a stage-2 artifact carrying no adjudication construct neither asserts nor denies the stage-8 one L1 requires. Had the scope limiter been absent, the honest relation would have been `CONFLICTS`. What *would* engage L1 is requiring one as a **precondition** of the founder trace — and that proposition lives in SP-039, correctly labelled `ELABORATES` against P-L3-FD01. The existence prohibition itself is an authored minimality choice | **ORTHOGONAL** |
| SP-048 | No correction, amendment, deletion, supersession, invalidation, scheduling, or world-fact adjudication transition, and no fourth state-changing operation. L1 lists three operations; **it never states that there are only three.** The closure is an authored minimality choice, and the row says so | **ORTHOGONAL** |
| SP-054 | A change in who is observing is not a discontinuity. L1's discontinuity material concerns restart and durability; observer identity appears in no pin | **ORTHOGONAL** |
| SP-072 | A late invocation is judged against the state at its admission position, not the state when intent was formed. L1 contains no proposition about intent formation, and no notion of an invocation being "late". **Adjacency disclosed:** this row sits next to the ordering surface, where L1 does speak ("+ canonical ordering", "+ equivalent state traces"). It stays `ORTHOGONAL` because those L1 propositions constrain the *order of admitted invocations and their traces*, and are satisfied identically under either reading of intent-formation time; the ordering law itself is carried by SP-071 and SP-070, both `ELABORATES` | **ORTHOGONAL** |
| SP-081 | Retrying a rejected operation is a new presented element at a later position; a prior refusal neither reserves a future success nor suppresses the retry's outcome. L1 contains no retry proposition. Both readings leave the invalid-transition law and the acceptance predicates untouched | **ORTHOGONAL** |

**Reclassified out of `ORTHOGONAL` on this re-audit (CR3-03), reducing the set from 9 to 7:**

- **SP-010** → `ELABORATES`. It restates a founder exclusion — P-L1-A "no auth", P-L1-B "No authentication". A clause restating an L1 proposition elaborates it; it is not orthogonal to it.
- **SP-055** → `ELABORATES`. Its revised text carries P-L1-B law 3 content directly: *"presented intent is never silently removed."* That is the law, not a proposition independent of it.

**Adopted `CONFLICTS` rows: 0.** The auditor reports this as `DISCLOSED_CONFLICTS`, a disclosure metric rather than a failure condition — v0.3's gate failed a document for labelling a row honestly `CONFLICTS` while passing one that concealed the same fact (CR-003 PROBE-A3). A gate that punishes candour selects for concealment.

---

## 18. SP-R05 exit gate

**The standing rule, earned across four reviews:** *changing the description of a defect is not repairing the mechanism that permits it.* Each line names the mechanism, not the description.

| Required | Result |
|---|---|
| `CR4-01` adjudicated **before** repair | **YES** — §0.6, classification `B · SOURCE_SUFFICIENT_WITH_DERIVATION`, with the grounding record's digest recomputed against the commission's citation |
| no capability vocabulary invented | **YES** — zero new semantic terms. Loss is named by clause identity drawn from a set the document already publishes. No substrate-limitation enum exists in this file |
| `CR4-01` structurally repaired or explicit BLOCK | **REPAIR IMPLEMENTED** — SP-167 closes the requirement set, SP-168 makes invocation computed rather than declared, SP-169 imposes two-sided exactness, SP-170 applies `INV-RC-KERNEL-4`, SP-152 compares the set |
| the CR-003 §3.5 pair rerun against the repair | **YES** — G′ names `{ SP-022 }`, H′ names `{ SP-024 }`, divergence at presented index 3 (FT-13); the coarse-common-label escape is closed by FT-16 |
| **CR3-B01 preserved closed** | **YES** — no clause bearing on the count's derivation was reopened. SP-043 and SP-102 are untouched; SP-094 gains only CR4-02's DaySlot pin |
| every CR-004 finding dispositioned | **YES** — 1 BLOCKING + 11 MATERIAL + 5 MINOR, the actual §4 set rather than the erroneous headline total of 7 |
| `CR4-03` repaired by rule, not by seam | **YES** — fence `compile()`, duplicate-payload scan, shipped-bytes re-extraction and comparison, published-evidence comparison. The v0.4 defect **FAILs** under the new auditor |
| the shipped auditor executes from artifact bytes | **YES** — extracted from this file and run; `SHIPPED_BYTES_EXECUTED IDENTICAL`, `PUBLISHED_EVIDENCE_MATCH IDENTICAL`, `PUBLICATION_INTEGRITY PASS` |
| new founder decisions required | **0** — A-09, A-10 and A-11 *disclose* pre-existing decisions; none must be answered for this revision to be lawful |
| protocol boundary not crossed | **YES** — RCP §5.3's vocabulary and R-04's record schema are declined at SP-171 and reserved at A-10. No RCP or F-05 text is amended |
| founder docket not silently resolved | **YES** — three items added, all `OPEN` or flagged; A-07's divergence from CR004 is recorded and *not* overruled |
| `EXACT` claims affected re-audited | **YES** — SP-005, SP-046 and SP-091 repaired after successful CR-004 attacks; §17.1's tally corrected |
| v0.4 byte-preserved | **YES** — `7c680b02…2cf48f`, untouched; it remains the exact subject of Cold Review 004 |
| Cold Review 004 byte-preserved | **YES** — `7ce5feac…d1a50`, unedited including its arithmetic defect |
| prior lineage byte-preserved | **YES** — v0.3, v0.2, v0.1, CR-001…CR-003, SLR-01-R1, custody, commission, RCP draft all unmodified |
| HBC `e350205` intact | **YES** — the HBC child repository at `projects/hbc-html`: 30 tracked, 0 modified, 0 staged. *Stated with its repository, because this claim does not verify against the governance repository and Cold Review 004 nearly recorded it as a defect for that reason* |

### 18.1 What the author may and may not claim

```
CR4-01 REPAIR IMPLEMENTED
AUTHOR-SIDE COUNTEREXAMPLE          PASS   (FT-13 and FT-16, run by the author)
INDEPENDENT CLOSURE                 NOT YET ESTABLISHED
CR3-B01                             CLOSED — by Cold Review 004, not by this document
```

**`CR4-01 CLOSED` is not claimed and may not be inferred.** Closure is an adjudication and no author-side movement performs it. `CR3-B01 CLOSED` appears above **only** as a citation of an independent reviewer's finding; this document does not re-earn it and would have no standing to.

**Every line in this section is an author-side claim.** Cold Review 001 found nine defects in a document self-reporting 14/14 PASS. Cold Review 002 found six in its successor, Cold Review 003 nineteen in *its* successor — one BLOCKING and introduced by the previous repair — and Cold Review 004 found twelve in v0.4, including a BLOCKING defect **inside the repair v0.4 rated `IMPOSSIBLE`**. The prior probability that this document is defect-free is low, and the correct posture toward this table is suspicion.

### 18.2 Known residuals carried into Cold Review 005

Declared rather than left for a reviewer to find.

1. **The requirement set is this document's clause set** (SP-167) — a derivation, not source. If RealityIR later declares a different requirement granularity, the failed-requirement sets computed here do not automatically transfer.
2. **`T(A)`'s domain makes any authored answer look decided** (§13.1). Any question this document's clauses already settle collapses to `|Y| = 1`. A-09 is flagged for this; repairing it means changing what `T` ranges over, which is beyond CR004's mandate.
3. **A-11's admissible set is unenumerated**, so no closure class is earned for the accounting question at all.
4. **Coordinate vocabulary is still unreconciled** (CR4-10). §15 pins two coordinates; SP-013, SP-021, SP-025, SP-053, SP-070, SP-072, SP-081, SP-110 and SP-111 use *position* or *ordinal* in further senses. SP-175 supplies the post-boundary observation, but does not unify the vocabulary.
5. **The Semantic Source Map has no surface here** (CR4-M3). P-L1-C seals it as a `TRACEABILITY REQUIREMENT`. SP-167's requirement identity is a *precondition* for it and not the thing itself; the map spans TargetIR and RealityIR, which this movement may not author. **Recorded as an acknowledged omission with a stated reason — v0.4 omitted it silently.**
6. **`SHAPE_AUDIT_RESULT PASS` on v0.2 is still PASS**, and `PUBLICATION_INTEGRITY PASS` does not improve that by one line. The auditor proves the numbers are honestly sourced, never that they are the right numbers.
7. **The required-vector set is a singleton** (SP-096), so the SP-152 barrier is never exercised against the reference trace.
8. **SP-169's exactness is falsifiable but not mechanically checkable** from the conformance record alone: refuting a named or omitted requirement requires access to the substrate, not just the record. This is strictly better than v0.4, where the record could not be refuted *at all* because the vocabulary was the embodiment's own — but it is not a machine check.
9. **SP-003's external-claim prohibition is not witness-falsifiable** (CR3-18), unchanged.
10. **No FT row witnesses recorded-intent-versus-accepted-fact** (§14 Q14), unchanged.
11. **The `ELABORATES` and `ORTHOGONAL` relations are author judgments.** §17.3 argues each one; an argument is not an adjudication.

---

## 19. Terminal boundary

```
CANDIDATE                     v0.5 · CANDIDATE_READY_FOR_COLD_REVIEW_005
REVISION SUBJECT              v0.4 · 7c680b02…2cf48f   PRESERVED · UNMODIFIED
REPAIR MANDATE                Cold Review 004 · 7ce5feac…d1a50 · SP-R05, bounded
COLD REVIEW 001 SUBJECT       3e675d9e…551537   PRESERVED · UNMODIFIED
COLD REVIEW 002 SUBJECT       611a782e…feb007   PRESERVED · UNMODIFIED
COLD REVIEW 003 SUBJECT       55c590ea…dd7f8e   PRESERVED · UNMODIFIED
COLD REVIEW 004 SUBJECT       7c680b02…2cf48f   PRESERVED · UNMODIFIED
CR4-01 REPAIRABILITY          B · SOURCE_SUFFICIENT_WITH_DERIVATION   (adjudicated first)
CR4-01                        REPAIR IMPLEMENTED · INDEPENDENT CLOSURE NOT ESTABLISHED
CR3-B01                       CLOSED   by Cold Review 004 · PRESERVED · NOT REOPENED
CAPABILITY VOCABULARY         NONE INVENTED
RCP §5.3 VOCABULARY           NOT INSTALLED · NOT EXTENDED   (A-10)
R-04 RECORD SCHEMA            RESERVED · NOT PRE-EMPTED
FOUNDER DECISIONS A-01–A-11   NOT RESOLVED   (5 OPEN · 0 PARTIALLY_DECIDED · 6 OPERATIVELY_DECIDED)
NEW FOUNDER DECISIONS         0   (A-09/A-10/A-11 disclose pre-existing ones)
SEMANTICPROGRAM SEAL          NOT GRANTED
REALITY COMPILER              NOT PROVEN
FOUNDER ADJUDICATION          NOT PERFORMED
REQUIREMENT EXTRACTION        NOT AUTHORIZED
REPRESENTATION SELECTION      NOT AUTHORIZED
IMPLEMENTATION                NOT AUTHORIZED
CAPABILITY RESOLVER           NOT IMPLEMENTED
PROTOCOL / RCP / F-05         NOT MUTATED
COMMISSION AMENDMENT          NOT AUTHORIZED
HBC MUTATION                  NOT AUTHORIZED
GIT STAGING / COMMIT / PUSH   NOT AUTHORIZED
NEXT LAWFUL GATE              lineage-independent Cold Review 005
```

**Independence limitation.** Authored by the session that authored v0.2, v0.3, v0.4, SLR-01 and SLR-01-R1. Not cold, not blind, not lineage-independent. Cold Reviews 001–004 were lineage-independent but **not** model-independent and **not** external; no rung above lineage-independence has been reached in this cascade, and external review remains blocked by transport custody rather than by anything semantic.

Rollback before any staging is removal of this one untracked file. No predecessor is modified by this movement.

---

*Capability may be refused. It may not be forgotten. The difference between those two is the whole compiler.*

*A count that outlives the sequence it was derived over is not a measurement. It is a memory pretending to be one.*

*And a type whose extension is chosen by the party being measured is not a type. It is a courtesy. The repair is not a better word for the loss — it is refusing to let the loser supply the word.*
