CHANGES_REQUIRED

# RC-0001 SemanticProgram v0.2 — lineage-independent cold review 002

**REVIEWED SUBJECT** `governance/OURSELF-RCP-RC0001-DURABLE-DAILY-RITUAL-LEDGER-SEMANTICPROGRAM-v0.2-CANDIDATE.md`
**SUBJECT SHA-256** `611a782e7abdf323de6567497d4da372ff011142d44de16c6f53c2a9d1feb007`
**REVIEW AUTHORITY** Read-only semantic falsification plus this one report file.
**AUTHORITY LIMIT** No candidate repair, commission amendment, founder adjudication, sealing, requirement extraction, representation selection, implementation, HBC mutation, staging, commit, or push.
**REVIEWED AT** 2026-08-13

**VERDICT** `CHANGES_REQUIRED`

The v0.2 repair movement is substantially real. Five of the seven mandated surfaces are repaired in the strong sense the candidate claims — the defect is made *mechanically unreachable*, not merely denied in prose. The candidate's own mechanical audit (§16.4) reproduces exactly under independent recomputation on every count I could test. That is a materially better document than v0.1.

It nevertheless cannot pass, for four independent reasons, each with a constructed counterexample:

1. **SP-132 moves an outcome-affecting gate outside the modeled boundary.** SP-131 seals exactly one vector (SP-090) and leaves every other required vector exposed. Two embodiments satisfying every normative SP clause produce different RC-0001 traces for the same presented vector.
2. **Three `EXACT` claims are overclaimed** (SP-004, SP-090, SP-091), one of them by the candidate's own stated falsification condition.
3. **Refusal-class selection is nondeterministic** (SP-033/SP-035/SP-043), which makes `illegal_transition_count` — a founder oracle field — implementation-dependent. FT-08 asserts one branch the normative clauses leave open, reproducing the exact CR-03 pattern SP-140 was written to abolish.
4. **SP-090 carries an undeclared precondition** and its declared one is insufficient to entail its own oracle.

---

## 0. Review classification and eligibility

| Classification | Result | Basis |
|---|---|---|
| LINEAGE-INDEPENDENT | **YES** | I did not author v0.1, v0.2, the commission, SLR-01/R1, Cold Review 001, or any predecessor. I hold no prior RC-0001 task turns and acquired no authorship history during this review. I read only the admitted packet plus the one L1 container. |
| MODEL-INDEPENDENT | **NO** | This review establishes no different model lineage. |
| EXTERNAL | **NO** | Performed inside the same operating environment as the subject's custody chain. |
| BLIND | **NO** — recorded honestly | Ambient context was supplied before the packet: a project-level `CLAUDE.md` (SELF/RUORA/ÆTHERNET/ÆXIOM ontology, repository boundary, security boundary), an auto-memory file carrying two prior lessons (*"corpus absence is not proof of absence"*, *"verify custody records against their own sources"*), a skills catalog naming OURSELF, SELFgraph, and RUORA projects, and the git status of an unrelated repository. None of it was used as semantic evidence for any finding below. The second memory lesson did influence *method* — it is why I recomputed §16.4 rather than accepting it — and I record that influence rather than conceal it. |

**Authority order applied.** L1 raw founder seal controls founder meaning. L2 commission controls procedure. L3 is valid founder-directed input that does not supersede L1. L4 records (custody, reconciliation, Cold Review 001) are derived evidence and were never treated as authority over founder meaning. The known-incomplete custody record was treated as a provenance witness only, never as an exhaustive register.

I did not open the superseded candidate `72a1bf7f…ff2447`. No governance file outside the admitted packet was read as authority.

**ELIGIBILITY GATE** `PASS`.

---

## 1. Packet admission — digests computed before content was read

| Role | Path / selector | Expected SHA-256 | Actual SHA-256 | Admission |
|---|---|---|---|---|
| SUBJECT · v0.2 | `…SEMANTICPROGRAM-v0.2-CANDIDATE.md` | `611a782e7abdf323de6567497d4da372ff011142d44de16c6f53c2a9d1feb007` | identical | **PASS** |
| Prior subject · v0.1 | `…SEMANTICPROGRAM-v0.1-CANDIDATE.md` | `3e675d9ebd1e8bbb25193625ef9ca784146d8d639e57d5f5fe9dfaee46551537` | identical | **PASS** |
| Cold Review 001 | `…v0.1-LINEAGE-INDEPENDENT-COLD-REVIEW-001.md` | `54de4a52ffa4f63086cbc19d30e7d7beb49b5c61cc1b37a2605da187e626276f` | identical | **PASS** |
| L2 · authoring commission | `…SEMANTICPROGRAM-AUTHORING-COMMISSION.md` | `9a04124a25ec3dc9c281d73a4f6bce7ecb7a0619a0d9890f9a51fd5ce5dcc04e` | identical | **PASS** |
| L4 · corrected lineage reconciliation | `…SLR-01-R1-CORRECTED-SOURCE-LINEAGE-RECONCILIATION.md` | `a506352ae82bd889034b5972dc2b090185aac3c6ac58f6bbc083f7d4614e68c6` | identical | **PASS** |
| L4 · source custody (known incomplete) | `…SOURCE-CUSTODY-001.md` | `0f61f7bb41ccdb74d00cb679f00df36b74d4221398835068bb4e5bf388734600` | identical | **PASS** |
| L1 container | `rollout-2026-08-12T17-43-58-019ff7ee…d677.jsonl` | `cee97abe168b011e8cc2bf1d69009d755f8c744998302c76743ac432a7d81ebe` | identical | **PASS** |
| P-L1-A · ordinal 59 | `jq -j 'select(.ordinal==59)…'` | `4cfd687b2ea9cdbcf366c29a60b124e76cf0f9cce9fb4de897d812b69b3f4bb5` | identical | **PASS** |
| P-L1-B · ordinal 72 | `jq -j 'select(.ordinal==72)…'` | `796a3588fbd8fbc611b62f6bba2267d462dd42f92f865a876f82e3387190e221` | identical | **PASS** |
| P-L1-C · ordinal 85 | `jq -j 'select(.ordinal==85)…'` | `e951c1bc4f3fdb0fdfe4f133624acfd521dfedb7240bbdb80a0fe4147d82b8e3` | identical | **PASS** |

**PACKET ADMISSION `PASS` · 10/10 · zero mismatches · zero packet failures.**

No evidence is blocked. This verdict is caused by confirmed defects, not by missing evidence.

---

## 2. PASS A · regression of Cold Review 001 findings against v0.2

Each finding was re-run by attempting to construct a counterexample that survives the v0.2 clause set. Testing the mechanism, not the presence of language describing the mechanism.

| # | Finding | Disposition | Decisive basis |
|---|---|---|---|
| CR-01 | Founder vector succeeds only after an unstated Operator is supplied | **CLOSED** | SP-030/SP-032/SP-034 preconditions are now state-and-content biconditionals with no invoker term. SP-130 admits no invocation-capability precondition. §11.1's derivation discharges every precondition from the founder's own written trace. **Counterexample attempted:** embodiment I applies a substrate-supplied admission filter and refuses `begin` on the sealed vector. **It fails** — SP-131 expressly ranges over models "supplied by a substrate" and over any "admission model", and declares such a model *nonconforming, not an alternative reading*. CR-01's own stated repair boundary ("permission testing may remain an orthogonal authored surface only if it cannot cause the exact L1 vector to reject") is met exactly. The residue on **other** vectors is a new defect (B.1-F1), not CR-01 surviving. |
| CR-02 | A-01 and A-02 not open in the operative envelope | **CLOSED** | SP-018 restated to the literal two-field observation and nothing further; its §17.1 falsification condition ("show SP-018 asserts anything about their *relationship*") holds under inspection. SP-101 expressly admits both the one-predicate and two-coupled-predicate readings and voids any clause excluding either. A-02 reclassified OPEN with the v0.1 recommendation withdrawn. A-01 disclosed as installed rather than labeled open. **Counterexample attempted:** find a v0.2 clause that still excludes model M1. **None found.** A residual *classification-consistency* defect between A-01 and A-02 is reported at B.3-F5. |
| CR-03 | A-03 has two lawful models while FT-03 silently chooses one | **CLOSED** | SP-140 voids any FT row discriminating an admitted alternative; FT-03 is restricted to consequences shared by both models with an explicitly inert branch note; v0.1's "creates an Entry early" clause is withdrawn. **Counterexample attempted:** audit all ten FT rows for a surviving A-03 discriminator. FT-01, FT-03, FT-07, FT-10 all speak of *complete* Entries or of L-fact identity, which both models satisfy. **No A-03 discriminator survives.** (SP-140 does, however, have a second unnoticed subject — see B-F3.) |
| CR-04 | A-04, A-05, A-06 are OPEN labels over selected behavior | **CLOSED** | All three reclassified OPERATIVELY_DECIDED with the installed branch named. **Counterexample attempted for each:** A-05 alternative B is genuinely excluded by SP-029 ("no … construct *exists*") and SP-039 (operations "require no … authoritative-world-answer precondition"); A-06 alternative B is genuinely excluded by SP-025 and SP-048; A-04 alternatives B/C are genuinely excluded from the *in-program* question by SP-019's L-fact set carrying no timezone or civil-boundary fact. **All three exclusions verified.** |
| CR-05 | Concurrency has no canonical semantic order | **CLOSED** | SP-071 makes total admission order a component of the *input*, assigned before any transition evaluation. SP-120 excludes any presentation not yielding a total order as **not RC-0001 input** and declares such a vector malformed. SP-121 states the barrier. **Counterexample attempted:** reproduce CR-05's two-serialization divergence. **It fails** — given one input, evaluation is a deterministic fold; and the residual simultaneity case is *excluded from the proof* rather than silently admitted. This is the model repair of the packet, and it is instructive: SP-120 **excludes** the ambiguous input, where SP-132 **admits** it. That contrast is the whole of finding B.1-F1. |
| CR-06 | Restart is both invisible and a new semantic event | **CLOSED** | SP-103 partitions facts into disjoint L/T classes; SP-102 places position ordinal, outcome stream, restart markers, and illegal count in T; SP-051's preservation obligation ranges only over L; SP-104 states the witness law. **Counterexample attempted:** the full B.2 trace with three restarts, two of them consecutive. **No contradiction arises** — see §4. A narrower drafting tension between SP-051's "the outcome stream is otherwise unchanged" and SP-104's "no preservation obligation ranges over T-facts" is reported at B.2-F7 as `PLAUSIBLE`; it is reconciled by T-facts being a pure function of the input trace, and no two conforming implementations can differ because of it. |
| CR-07 | inspect is state-neutral but not fact-neutral; freshness undefined | **CLOSED** | `inspect` is withdrawn as an operation. SP-110 makes observation a total projection; SP-111 forbids emission, position occupancy, illegal-count contribution, and any effect on acceptance/refusal/ordering/outcome; SP-112 makes `view(n)` single-valued per input trace and position; SP-113 dissolves freshness by position-indexing rather than by imposing a staleness bound. **Counterexample attempted:** construct an observation that mutates a T-fact, or two observations disagreeing at one position. **Both fail** on SP-111 and SP-112 respectively. The second-program defect is genuinely gone. |
| CR-08 | SP-004 is not an `EXACT` restatement of the founder non-goals | **PARTIALLY_CLOSED** | The generalization defect **is** repaired: the literal register is restored and "distribution readiness"/"target-code sophistication" are split into SP-100 as `AUTHOR-PROPOSED`. But SP-004 pins **P-L1-B** and claims to reproduce the exclusions "literally", while omitting P-L1-B's sixth exclusion. SP-004 therefore still fails **its own §17.1 falsification condition**, which reads: *"Show a term in SP-004 not in the source, or a source exclusion missing."* One is missing. See B.4. |
| CR-09 | The provenance audit is structural, not semantic | **CLOSED** | CR-09's stated repair boundary was: *"rename the result as a metadata-shape audit and require semantic entailment review separately. Do not weaken or discard the structural check."* All three are done. §16.4 is renamed and explicitly disclaims what it cannot prove; §17 adds a per-clause entailment argument with a stated falsification condition; the structural check is retained. **The mechanism is closed — and it worked:** §17 is falsifiable, and I falsified three of its ten conclusions. Those false conclusions are separate findings (B.4), not CR-09 surviving. Two inaccuracies in the retained structural scan are reported at B-F8/B-F9. |

**PASS A RESULT — 8 CLOSED · 1 PARTIALLY_CLOSED · 0 NOT_CLOSED · 0 REGRESSED.**

Not 9/9. The threshold fails on CR-08.

### 2.1 Seven repair surfaces — independent effectiveness

| # | Surface | Claimed mode | Independent result |
|---|---|---|---|
| 1 | Operator gate | IMPOSSIBLE | **EFFECTIVE for the founder vector** (SP-131). **NOT EFFECTIVE for other vectors** — B.1-F1. |
| 2 | False-open docket | DETECTABLE | **EFFECTIVE**, with one misapplication of its own test — B.3-F5. |
| 3 | A-03 / FT-03 contamination | IMPOSSIBLE | **EFFECTIVE for A-03.** SP-140 has an unnoticed second subject — B-F3. |
| 4 | Concurrent ordering | IMPOSSIBLE | **EFFECTIVE.** Strongest repair in the packet. |
| 5 | Restart fact creation | IMPOSSIBLE | **EFFECTIVE.** |
| 6 | inspect trace semantics | IMPOSSIBLE | **EFFECTIVE.** |
| 7 | Provenance entailment | DETECTABLE | **MECHANISM EFFECTIVE, OUTPUT FALSE** — three overclaims survive (B.4). |

**5/7 fully effective. 7/7 traceably addressed.**

---

## 3. PASS B.1 · does SP-132 remove authority, or relocate it out of sight?

> **Question under pressure.** SP-132 is a successful repair only if pre-boundary refusal cannot cause two implementations receiving the same semantic input to produce different RC-0001 traces.

### B.1-F1 — **CONFIRMED DEFECT** — SP-132 relocates an outcome-affecting gate outside the conformance boundary; SP-131 seals only one vector

**Clauses:** SP-132, SP-131, SP-130, SP-071, SP-091, SP-055, SP-080, SP-121, §17.3.

SP-132 permits a capability model to exist "outside the SemanticProgram boundary as a substrate-level admission filter", and routes anything it refuses through SP-055: *"an invocation that never reached the boundary and therefore has no program presence"* — no L-fact, no T-fact, **no outcome**.

SP-071 defines the program's input as a totally ordered sequence of **admitted** invocation records. Admission is therefore the filter's output, not the vector's content. **The consequence is that "the SemanticProgram input" becomes a substrate-dependent quantity**, and SP-091's antecedent — *"For the same SemanticProgram input"* — becomes unverifiable from outside any single substrate.

SP-131 blocks this, but its scope is exactly one vector: *"may cause the **SP-090 founder vector** to produce any outcome other than the one SP-090 states."* It does not range over arbitrary required vectors. P-L1-C requires equality **"for every required vector."**

**Counterexample (constructed, survives the full v0.2 clause set).**

Required vector V2, presented identically to both substrates:

```
begin ; record("A") ; record("B") ; complete
```

- **Embodiment W** — no admission filter. All four invocations admitted.
  `view(final)`: state `complete`, Entries `[A, B]`, `illegal_transition_count = 0`.
- **Embodiment I** — a substrate-level admission filter expressly permitted by SP-132 refuses `record("B")` (any role, quota, or capability rule). That invocation never reaches the boundary.
  I's SemanticProgram input is `begin ; record("A") ; complete`.
  `view(final)`: state `complete`, Entries `[A]`, `illegal_transition_count = 0`.

**Clause-by-clause conformance check for embodiment I:**

| Clause | Does I violate it? | Why not |
|---|---|---|
| SP-131 | **No** | V2 is not the SP-090 founder vector. SP-131's scope is exhausted. |
| SP-130 | No | The refused invocation never reached the boundary; nothing that *did* reach it was capability-gated. |
| SP-132 | No | This is precisely the permitted construct. |
| SP-055 | No | SP-132 expressly assigns the refusal to SP-055's "not presented" class. |
| SP-080 | No | Ranges only over *admitted* invocations. |
| SP-071 / SP-120 / SP-121 | No | These govern admission **order**, not admission **membership**. Both embodiments received a total order. |
| SP-091 | No | Its antecedent is "the same SemanticProgram input". I's input differs. The conditional is vacuously satisfied. |

**Both embodiments satisfy every normative SP clause, and their traces differ.** The conformance oracle (SP-114) observes the divergence and no clause attributes it to anyone.

**Consequence, stated against L1.** This is not merely a determinacy gap; it contradicts founder law. P-L1-B constitutional law 3 reads:

> *"Capability loss is typed and explicit. No emitter silently 'figures something out.'"*

SP-132 makes capability loss **untyped and invisible by construction** — its defining consequence is that the refusal produces no fact of any kind. That is the exact opposite of typed and explicit. P-L1-B law 4 — *"Emitters may translate representation, not law"* — is also engaged, since a substrate filter changes which transitions occur.

**Contrast that proves the defect is avoidable.** CR-05's repair faced the identical structural problem — an outcome-affecting decision that must happen before the boundary — and solved it correctly: SP-120 declares an under-determined presentation **malformed and not runnable**. SP-132 instead declares the under-determined presentation **admissible and silent**. The candidate already owns the right pattern; it simply did not apply it here.

**Answer to B.1:** SP-132 does **not** remove authority from RC-0001 semantics. It relocates an outcome-affecting gate outside the modeled boundary, where conformance cannot see it. The repair is successful for the SP-090 vector alone.

### B.1-F2 — **CONFIRMED DEFECT** — §17.3's `ORTHOGONAL` justification for SP-132 is false

§17.3 states that the `ORTHOGONAL` rows "are each satisfiable-or-not **without affecting any L1 proposition**." B.1-F1 exhibits SP-132 affecting two L1 propositions: P-L1-C's "Reference trace = Normalized Web trace = Normalized iOS trace, for every required vector", and P-L1-B constitutional law 3. SP-132's relation mark is therefore unearned on §17.3's own stated criterion.

---

## 4. PASS B.2 · the L-fact / T-fact partition, attacked hard

### 4.1 Full trace evaluation

```
begin
record("Reflect")
restart
restart
complete
restart
```

Initial condition per SP-040: state `idle`, pending count 0, durable history empty (assumed empty; see B.4-F6 on why SP-090's own precondition does not secure this).

| n | Input | Governing clause | L-facts after n | T-facts after n |
|---|---|---|---|---|
| — | initial | SP-040 | state `idle`; DaySlot `D0`; pending `[]`; Entries `[]` | position 0; stream `[]`; markers 0; illegal 0 |
| 1 | `begin` | SP-030 — state is `idle` ⇒ succeeds | state `active`; DaySlot `D0`; pending `[]`; Entries `[]` | position 1; stream `[accepted begin]`; illegal 0 |
| 2 | `record("Reflect")` | SP-032 — state `active` ∧ content present ⇒ succeeds | state `active`; pending `["Reflect"]`; Entries `[]` | position 2; stream `+[accepted record]`; illegal 0 |
| 3 | `restart` | SP-050, SP-051 | **unchanged** — state `active`; pending `["Reflect"]`; Entries `[]` | position 3; `+1 restart-boundary marker`; illegal 0 |
| 4 | `restart` | SP-050, SP-051 | **unchanged** — state `active`; pending `["Reflect"]`; Entries `[]` | position 4; `+1 restart-boundary marker`; illegal 0 |
| 5 | `complete` | SP-034 — state `active` ∧ pending ≥ 1 ⇒ succeeds | state `complete`; pending `[]`; Entries `[E1("Reflect", complete)]` | position 5; `+[accepted complete]`; illegal 0 |
| 6 | `restart` | SP-050, SP-051 | **unchanged** — state `complete`; pending `[]`; Entries `[E1]` | position 6; `+1 restart-boundary marker`; illegal 0 |

**Terminal observation** `view(6)`: `state = complete`, `entries.count = 1`, `entries[0].content = "Reflect"`, `entries[0].status = complete`, `history_order = canonical`, `illegal_transition_count = 0`.

### 4.2 The six required questions

**Which facts are L-facts? Which are T-facts?**

*L-facts* (SP-019, closed list): Ledger identity; Ritual identity; current-state value; current DaySlot ordinal; ordered pending contributions while present; durable ordered Entries with content and status; canonical history order.

*T-facts* (SP-102, closed list): the operation position ordinal (1…6); the ordered operation-outcome stream (`accepted begin`, `accepted record`, `accepted complete`); the restart-boundary markers (three: n = 3, 4, 6); the derived illegal-transition count over the supplied trace (0).

SP-103 makes the classes disjoint — *"No fact belongs to both classes"* — and the partition is exhaustive over everything this trace produces. Nothing in the trace is unclassified.

**Does each restart preserve all prior L-facts?** **Yes, at all three boundaries.** SP-051: *"A restart invokes no operation and changes no L-fact."* SP-050's survival column names identity, current state, DaySlot, pending contributions, completed Entries, and canonical order, and its destruction column reads *"None. No L-fact is required to be destroyed."* The decisive case is n = 3 → n = 4, **two consecutive restarts with no intervening operation**: since restart's L-fact footprint is empty, restart is idempotent on L-facts, and any number of consecutive restarts preserves `state = active` and `pending = ["Reflect"]`. This is the exact configuration in which v0.1's SP-051/§6.2 contradiction became visible, and it does not arise in v0.2.

**Can T-facts affect future transition evaluation?** **No, and this is mechanically visible rather than merely asserted.** The three state-changing clauses state their preconditions as **biconditionals over L-facts alone**:

- SP-030 — succeeds "**when and only when** current state is idle";
- SP-032 — "**when and only when** current state is active and content is present";
- SP-034 — "**when and only when** current state is active and at least one pending contribution exists".

Because acceptance is fixed by an *iff* whose right-hand side mentions only L-facts and the presented content, no T-fact can enter the determination. Concretely: at n = 5, `complete` evaluates identically whether zero, two, or ten thousand restart markers precede it, because the marker count is a T-fact and no precondition reads it. This is the load-bearing observation of the whole partition, and it does not depend on SP-103 or SP-104 being believed — it follows from the biconditional form of SP-030/SP-032/SP-034.

**Can sequence position alter ledger meaning?** **No, beyond determining the order in which transitions are evaluated — which is the definition of a state machine, not a leak.** Position is a T-fact (SP-102). Entry ordering is governed by SP-024 (ascending DaySlot ordinal, then ascending *successful-record order*) and SP-044 (pending order = accepted record admission order). These key off the *input* order, which SP-071 makes a component of the input rather than a T-fact the program reads back. Two L-fact sets with identical values at different positions remain distinguishable (§3.2), but that is a distinction of observation index, not of ledger meaning.

**Can an implementation inspect T-facts and thereby change later L-facts?** **No.** I attempted three routes and all fail:

1. *Read the restart-marker count and refuse `complete`.* Violates SP-034's "when and only when" — with state `active` and pending ≥ 1, success is mandatory.
2. *Read the outcome stream and alter Entry content or order.* Violates SP-034 ("one complete Entry per pending contribution in canonical order"), SP-044, and SP-024.
3. *Read the illegal count and change acceptance.* Same biconditional violation as (1).

**Are two implementations allowed different T-facts while still semantically equivalent?** **No — given the same admitted input.** The T-fact stream is a *pure function* of the input sequence, derivable from SP-071 (order fixed by input) + SP-030–SP-035 (outcome fixed by L-state) + SP-080 (exactly one outcome per admitted invocation) + SP-050/SP-051 (exactly one marker per discontinuity), by induction on position. §7.1 states the same result. SP-114 makes the witness compare T-fact streams across substrates, so divergence is a conformance failure.

**The qualification matters:** *given the same admitted input*. Under B.1-F1, SP-132 permits the admitted input itself to differ between substrates presented with the same vector — at which point different T-facts become permissible. The partition is sound; the input boundary beneath it is not.

**Verdict on the partition: it does not leak, and the prohibition is mechanically visible in the normative clauses** (the biconditional form of SP-030/SP-032/SP-034), not merely asserted in the prose of §6.2.

### B.2-F7 — **PLAUSIBLE** — SP-051 and SP-104 are in drafting tension over T-fact preservation

SP-104 states *"no preservation obligation in this program ranges over T-facts."* SP-051's T-fact-effect column states *"Exactly one boundary marker; **the outcome stream is otherwise unchanged**"*, and §6.2 renders this as the equation `T-facts(n+1) = T-facts(n) + one restart-boundary marker` — which is, read literally, a preservation obligation ranging over T-facts.

**Two readings.** Under the narrow reading — SP-051 describes what restart *emits* (one marker and nothing else), not what *persists* — the clauses are consistent. Under the literal reading of §6.2's equation, they conflict.

**Why this is not consequential.** §0.4 denies §6.2 normative force ("Prose … create no semantic law"), and the T-fact stream is a pure function of the input trace, so it need not be *preserved* — it is *recomputable*. SP-043 and SP-102 both describe the illegal count as "derived over the supplied trace", confirming the functional reading. I attempted the counterexample — embodiment W carries the T-fact stream across a restart, embodiment I discards it and recomputes — and **the two cannot diverge**, because both must equal the function of the input trace.

Reported as `PLAUSIBLE` drafting tension, not a defect. It should be resolved by wording, not by mechanism.

### 4.3 One structural observation, not a defect

SP-110 defines `view(n)` with a T-fact (the position ordinal) as its *argument* and the L-fact set as its value. The classes remain disjoint as *facts* (SP-103), but the observation relation couples them: the L-fact set is only well-defined relative to a position. Since positions are input-determined, `view(n)` remains input-determined and purity is unaffected. Recorded for completeness; no finding.

---

## 5. PASS B.3 · docket truth, second-order test

For each item I constructed two implementations choosing different answers and tested both against the full normative clause set.

| Item | Declared | Impl-1 vs Impl-2 constructed | Both conform? | Declared classification accurate? |
|---|---|---|---|---|
| **A-01** state ownership | OPERATIVELY_DECIDED (D installed) | Impl-1 exposes an owner coordinate in `view(n)`; Impl-2 exposes an ownerless projection | **No** — Impl-1's `view(n)` returns a fact outside SP-019's *complete* L-fact set, diverging from Impl-2 under SP-110/SP-112 | **ACCURATE as a label**, but its stated justification is self-contradicting — see B.3-F5 |
| **A-02** complete operation vs state | OPEN | M1: one predicate projected into `state` and `entries[].status`; M2: two causally coupled predicates | **Yes** — SP-018 asserts only the literal two-field observation; SP-101 expressly admits both and voids any excluding clause; SP-034 is satisfied by both. No admitted operation can produce `state=complete` with `status≠complete`, so M1 and M2 are observationally indistinguishable | **ACCURATE** — T(A-02) = YES for all alternatives |
| **A-03** record and Entry creation | PARTIALLY_DECIDED (A, B open; C excluded) | Impl-A: pending contribution already bears Entry identity; Impl-B: identity conferred at `complete` | **Yes** — SP-026 admits both; SP-140 bars discrimination; all ten FT rows speak of *complete* Entries or L-fact identity, which both satisfy. Alternative C is genuinely excluded by SP-022's requirement that a contribution be **created** | **ACCURATE.** One residual ambiguity noted below |
| **A-04** daily → civil mapping | OPERATIVELY_DECIDED (A installed) | Impl-1 pure logical ordinal; Impl-2 carries a timezone fact defining the boundary | **No** — Impl-2 requires a fact absent from SP-019's complete L-fact set and would violate SP-070's closed list of ordering facts | **ACCURATE** for the in-program question. Note that an embodiment *deriving* boundary placement from a clock remains lawful, since SP-071 makes boundaries an input component — that is outside the docket question as phrased |
| **A-05** world-fact authority layer | OPERATIVELY_DECIDED (A installed) | Impl-1 no layer; Impl-2 gates `complete` on a world-fact confirmation | **No** — Impl-2 violates SP-039 (operations "require no … authoritative-world-answer precondition"), SP-029 ("no … construct **exists** in v0.2"), and SP-060 | **ACCURATE** |
| **A-06** correction of completed Entry | OPERATIVELY_DECIDED (A installed) | Impl-1 immutable; Impl-2 offers a correction operation | **No** — Impl-2 violates SP-025 ("no admitted operation deletes it, rewrites its content, changes its status, or replaces its canonical position") and SP-048 | **ACCURATE** |
| **A-07** invocation-capability precondition | OPERATIVELY_DECIDED (no gate installed) | Impl-1 no gate; Impl-2 in-program capability precondition; **Impl-3 substrate-level filter under SP-132** | Impl-2 **No** (violates SP-130). **Impl-3 Yes** — and it produces different traces (B.1-F1) | **INCOMPLETE** — accurate for the in-boundary question, but the disclosure does not record that SP-132 leaves the outcome-affecting residue undecided and unobservable |

### B.3-F5 — **CONFIRMED DEFECT** — §13.0's closure test is applied inconsistently to A-01 and A-02

§13.0 defines the test and its mapping:

```
T(A): Can two embodiments, each adopting a different admitted alternative of A,
      both conform to every operative SP clause in this document?

YES for all alternatives     → OPEN
YES for some, NO for others  → PARTIALLY_DECIDED
NO for all but one           → OPERATIVELY_DECIDED
```

§13.1 assigns A-01 `OPERATIVELY_DECIDED` with this justification:

> "Alternatives A, B, C are **not excluded in principle** but are unobservable under v0.2 and therefore **untestable**."

"Not excluded in principle … untestable" is a statement that T(A-01) returns **YES for every alternative** — which the document's own rule maps to `OPEN`, not `OPERATIVELY_DECIDED`. The recorded justification contradicts the recorded label.

This is not merely pedantic, because **A-02 is in the identical epistemic position and receives the opposite label.** For both items the alternatives are observationally indistinguishable under v0.2's L-fact set; A-02 is called `OPEN` and A-01 is called `OPERATIVELY_DECIDED`. Two structurally identical situations, two different closure classes.

**The label itself is defensible** on the reading §13.2 supplies — *"Selecting A, B, or C requires adding an owner coordinate to SP-019"* — under which the alternatives are observable claims and genuinely excluded. That reading is the one I applied in the table above. But then §13.1's "not excluded in principle" is simply false and should read "excluded from v0.2's observable domain", and A-02 warrants re-examination under the same standard.

**Consequence:** repair surface 2's mechanism is sound but was not applied uniformly. A founder reading §13.1 receives an inconsistent account of why two questions with the same structure closed differently.

### Residual on A-03 — `PLAUSIBLE`

Under Impl-A, a pending contribution bearing Entry identity has, by SP-021, a canonical history position. SP-019 lists "ordered pending contributions while present" and "durable ordered Entries with content and status" as separate L-facts, and it is not stated whether an Entry-identified pending contribution appears in the second slot before `complete`. If it may, `view(n)` diverges between Impl-A and Impl-B mid-trace. The natural reading — pending things occupy the pending slot only — makes both models agree, and every FT row is written to count *complete* Entries, which preserves the agreement. Recorded as `PLAUSIBLE` ambiguity, not a confirmed defect.

### Minor — §13.1's A-03 cell

The A-03 row's Closure-class cell reads **OPEN** while its own Installed/excluded cell, the correction line two rows below, and the summary line all read `PARTIALLY_DECIDED`. Self-disclosed and self-corrected, but the table cell is wrong as printed.

---

## 6. PASS B · fresh attacks beyond CR-01…CR-09

### B-F3 — **CONFIRMED DEFECT** — refusal-class selection is nondeterministic, making `illegal_transition_count` implementation-dependent

**Clauses:** SP-035, SP-033, SP-043, SP-034, FT-08, SP-090, SP-091, SP-140.

SP-035: *"A refused complete … emits a rejected complete outcome identifying `INVALID_TRANSITION` **or** `NO_RECORDED_CONTENT`."*
SP-043: *"A state-illegal begin, record, or complete … **contributes one** to the illegal-transition count … `MISSING_CONTENT` and `NO_RECORDED_CONTENT` refusals are non-state refusals and **do not contribute** to that count."*

**No precedence rule exists for the case where both refusal conditions hold simultaneously.** That case is reachable and is not exotic — it is the second half of the candidate's own FT-08.

**Counterexample.** Pre-state: `complete`, pending `[]`, Entries `[E1]`. Input: `complete`.
Both of SP-034's conjuncts fail: the state is not `active`, **and** no pending contribution exists.

- **Embodiment W** identifies the refusal `INVALID_TRANSITION`. By SP-043 sentence 1 (a state-illegal `complete`), `illegal_transition_count` **increments to 1**.
- **Embodiment I** identifies the refusal `NO_RECORDED_CONTENT`. By SP-043 sentence 2, it is a non-state refusal and **does not contribute**; the count remains **0**.

Both satisfy SP-035, which permits either identifier. SP-043's two sentences both apply and reach opposite conclusions with no tie-break. The result is two different T-fact outcome streams and two different values of `illegal_transition_count` for the same input.

**Why this is material.** `illegal_transition_count` is one of the six founder oracle fields in SP-090 and P-L1-B. P-L1-C's Fail list names both **"illegal transition behavior"** and **"failure semantics"** as divergence dimensions that fail the proof. SP-091 requires trace equality; SP-114 compares T-fact streams. This is direct nondeterminacy in a founder-sealed acceptance predicate.

**The second-order finding.** FT-08 *asserts* one branch — "B rejected `INVALID_TRANSITION`, changes no L-fact, **increments illegal count**" — that the normative clauses leave open. Under §0.4, FT rows add no law. Under **SP-140**, *"An FT row that discriminates an admitted alternative is void, not authoritative."* FT-08 therefore either (a) is void by SP-140, leaving the ambiguity unresolved and RC-0001 nondeterministic on failure semantics, or (b) is doing normative work it is expressly forbidden to do.

**This is precisely the CR-03 pattern SP-140 was written to abolish, surviving in a different row.** Repair surface 3 found and fixed one instance (FT-03/A-03) and did not sweep for others. The same test applied to SP-033 (`INVALID_TRANSITION` **or** `MISSING_CONTENT`) shows the identical structure for `record` presented at `idle` with absent content.

The smallest repair boundary is a precedence rule in SP-033/SP-035 (for example, state legality is evaluated first and its refusal identifier dominates), which would make FT-08 lawful again. **I do not choose that rule.**

### B-F8 — **CONFIRMED DEFECT** — §16.4's ontology scan misreports its own result

§16.4 states:

> "Assertion / Adjudication / Adjudicator / Establishment / Reporter appear in **exactly three** normative rows — SP-029, SP-039, SP-060 — each of which prohibits them. CONTESTED: 0 occurrences."

Recomputed over the normative envelope (§§1–16, rows carrying an SP identifier), those terms appear in **six** rows:

| Row | Sense |
|---|---|
| SP-029 | prohibitive — as reported |
| SP-039 | prohibitive — as reported |
| SP-060 | prohibitive — as reported |
| **SP-048** | **prohibitive — omitted from the report** ("no … world-fact **adjudication** transition exists") |
| SP-101 | governance sense ("until A-02 is **adjudicated**") |
| SP-140 | governance sense ("until the item is **adjudicated**") |

Separately, `CONTESTED` occurs once inside §§1–16 (the §10 L3-reconciliation row "PENDING / CORROBORATED / **CONTESTED** / REJECTED / SUPERSEDED / STANDING | not adopted"), and `contest status` occurs in normative row SP-039. The scan reports "0 occurrences" over an envelope that contains them.

**Materiality: LOW in direction, real in kind.** Every omitted occurrence is either prohibitive or governance-sense, so the *conclusion* the scan supports — that this revision did not reopen the adjudication gate Cold Review 001 §4 recorded as a `REFUTED CONCERN` — **survives, and I independently confirm it**. But §16.4 is the one component the candidate presents as mechanically verified, and CR-09's repair boundary expressly required retaining the structural check for what it actually proves. A mechanical claim that does not reproduce is a defect regardless of the direction of its error.

### B-F9 — **CONFIRMED DEFECT** — §17.3's `ORTHOGONAL` enumeration omits one row

§16.4 correctly counts `ORTHOGONAL 10`. §17.3 then enumerates the `ORTHOGONAL` rows as "SP-010, SP-014, SP-016, SP-048, SP-054, SP-055, SP-072, SP-081, SP-132" — **nine**. Recomputation gives ten: the list omits **SP-029**.

SP-029 therefore receives no relation justification anywhere in §17, which is the section whose entire purpose (repair surface 7) is that every relation claim carry a falsifiable argument. Beyond the count, SP-029's `ORTHOGONAL` mark is itself questionable: FD-01 and Cold Review 001 §4 treat the absence of the Assertion/Adjudication/Establishment gate as load-bearing for founder-vector success, which is not "satisfiable-or-not without affecting any L1 proposition". Recorded as `PLAUSIBLE` on the classification, `CONFIRMED` on the omission.

### Attacks attempted that FAILED — reported as failures

Honest record of adversarial attempts that found nothing:

| Attack | Result |
|---|---|
| Reproduce CR-05's two-serialization divergence under SP-071/SP-120/SP-121 | **Failed.** Order is an input component; the residue is excluded as malformed. |
| Make `view` emit a T-fact, occupy a position, or contribute to the illegal count | **Failed.** SP-111 forecloses all four explicitly. |
| Make `view(n)` return two values at one position, or make staleness semantic | **Failed.** SP-112 (single-valued per input trace and position) and SP-113 (position-indexing dissolves freshness). |
| Find an FT row still discriminating an A-03 alternative | **Failed** across all ten rows. |
| Break the L/T partition with consecutive restarts | **Failed.** Restart is L-fact idempotent; see §4. |
| Make a T-fact influence a transition precondition | **Failed.** SP-030/SP-032/SP-034 are biconditionals over L-facts. |
| Diverge the T-fact stream between two implementations on one admitted input | **Failed.** The stream is a pure function of the input trace. |
| Reintroduce Assertion / Adjudication / Establishment as a gate anywhere in v0.2 | **Failed.** Independently confirmed: the `REFUTED CONCERN` was not reopened. |
| Falsify §16.4's structural counts | **Failed on every count.** Independently recomputed over §§1–16: **82 SP rows, 82 unique, 0 duplicates; EXACT 10 / ELABORATES 62 / ORTHOGONAL 10 / CONFLICTS 0; LP = FOUNDER_SEALED_L1 10, FOUNDER_DIRECTED_L3 1, COMMISSION_REQUIRED 4, AUTHOR_PROPOSED 53, DERIVED 14; FT rows 10; Q rows 16; docket items 7; trailing whitespace 0; UNRESOLVED rows 4 (SP-101, SP-026, SP-027, SP-047), all naming an A item.** Every figure reproduces exactly. The scan errors are confined to the two narrative claims at B-F8/B-F9. |
| Find an adopted `CONFLICTS` row | **Failed.** Zero, confirmed. |
| Find a representation, storage, or implementation selection leaking into a normative row | **Failed.** §15's firewall holds. |

---

## 7. PASS B.4 · provenance entailment — hardest version

For each of the ten `EXACT` clauses I attempted to prove `source proposition ≠ candidate proposition` by narrowing, widening, added precondition, removed consequence, stronger quantifier, weaker quantifier, changed subject, or changed temporal boundary. Founder source is quoted verbatim from the hash-verified L1 pins.

| Clause | Founder source text (verbatim, pinned) | Attack result | Verdict |
|---|---|---|---|
| **SP-001** | P-L1-A: `"Durable Daily Ritual Ledger / Ritual / Entry / idle → active → complete / begin / record / complete / + invalid transition law / + durability / + canonical ordering / + restart preservation / + equivalent state traces"`; P-L1-A: `"A substrate-neutral semantic reality can be lowered into materially different runtimes"` | All eleven source members appear in SP-001; no member is added. "substrate-independent" is sourced to "substrate-neutral". **Weaker quantifier attempted:** SP-001 says preserved meaning "**includes**" the list, which does not close the set, whereas the source presents a closed enumeration and P-L1-C adds *"RC-0001 should also be frozen against scope creep"*. Closure is carried by SP-004 instead. Non-material. | **HOLDS** (`PLAUSIBLE` minor openness) |
| **SP-004** | P-L1-A: `"No auth, no cloud, no camera, no AI, no networking."` · P-L1-B: `"No cloud. No authentication. No generative AI. No camera. No networking. No seductive product surface hiding compiler defects."` · P-L1-C: `"The first proof is not: beautiful UI; production architecture; App Store readiness; sophisticated Swift; sophisticated React; generalized storage abstraction; reusable design system."` | **REMOVED CONSEQUENCE — attack succeeds.** SP-004 pins P-L1-B and claims to state the exclusions "**literally**", but reproduces only five of P-L1-B's six. **`"No seductive product surface hiding compiler defects"` is omitted.** It is in the same list, the same grammatical form, and the same block as the five that were kept, and it is substantive — it is the exclusion that guards the proof against a product surface concealing compiler defects, which is the founder's stated reason for choosing a boring subject. SP-004 fails **its own §17.1 falsification condition**: *"or a source exclusion missing."* The seven P-L1-C non-goals are reproduced exactly and that half of CR-08 is genuinely repaired. | **`EXACT` FALSE — CONFIRMED** |
| **SP-005** | P-L1-B: `"semantic equivalence ≠ structural equivalence ≠ visual identity ≠ binary identity"`; `"What must remain equal are the declared observable semantics."` · P-L1-C: `"Even if both apps look immaculate."` | The clause restates the non-identity law and its substitution consequence. No narrowing, widening, or added precondition found. | **HOLDS** |
| **SP-018** | P-L1-B: `"state = complete / entries.count = 1 / entries[0].content = \"Reflect\" / entries[0].status = complete / history_order = canonical / illegal_transition_count = 0"` | The source does name a top-level `state` and a per-Entry `entries[0].status`, both taking `complete`. SP-018 asserts that literal observation "and nothing further", and I confirm it asserts nothing about their relationship — the CR-02 defect is genuinely gone. | **HOLDS** |
| **SP-041** | P-L1-A: `"idle → active → complete"`, `"begin / record / complete"`, `"+ invalid transition law"` | **Attack partially succeeds.** §17.1's argument claims the clause "binds the three operations to the **three progression edges**" — but the source progression `idle → active → complete` has **two** edges, not three. The third transition SP-041 asserts, `active —record→ active`, is a self-loop the source never draws. It is soundly *derivable* from P-L1-B's worked trace (if `record` changed state, the subsequent `complete` could not apply), but derivation is `ELABORATES`, not "adds no semantic information". The closure clause is well supported by "+ invalid transition law" over a closed operation set. | **`PLAUSIBLE` overclaim; §17.1's stated argument is factually wrong about the source** |
| **SP-046** | P-L1-A: `"+ durability"`, `"+ restart preservation"` · P-L1-B: worked trace `begin / record("Reflect") / complete / restart` with unchanged post-restart Entry fields | Entry content, status, and relative order surviving restart is exactly what the post-restart oracle shows. No divergence found. | **HOLDS** |
| **SP-090** | P-L1-B: `"For event trace: begin / record(\"Reflect\") / complete / restart — the oracle **might require**: state = complete / entries.count = 1 / entries[0].content = \"Reflect\" / entries[0].status = complete / history_order = canonical / illegal_transition_count = 0"` | **ADDED PRECONDITION + STRONGER MODALITY — attack succeeds on two grounds.** (i) SP-090 prepends *"From an idle state with an empty current cycle"*, which the source does not contain. It is load-bearing: without it, `begin` could be refused and the oracle would not hold. Adding a load-bearing precondition is definitionally not "adds no semantic information". (ii) The source hedges — *"the oracle **might** require"* — presenting the values as illustrative; SP-090 states categorically what the trace "**yields**" and marks it `FOUNDER_SEALED_L1`. That converts an illustration into a seal. §17.1's falsification condition is "Byte-compare against P-L1-B"; the six values byte-compare, but the clause is not confined to those six. | **`EXACT` FALSE — CONFIRMED** |
| **SP-091** | P-L1-C: `"Pass — Reference trace = Normalized Web trace = Normalized iOS trace — for every required vector."` | **CHANGED SUBJECT + WEAKENED QUANTIFIER — attack succeeds.** The source quantifies universally over **required vectors** — things presented to both substrates. SP-091 replaces this with a conditional on **"the same SemanticProgram input"** — the post-admission sequence, which SP-071 + SP-132 make substrate-dependent. The substitution converts an unconditional universal obligation into a conditional whose antecedent no external party can verify. **This is B.1-F1 viewed from the provenance side, and it is the mechanism by which that counterexample escapes:** an embodiment that filters an invocation has changed its "SemanticProgram input" and thereby exited SP-091's scope, while remaining squarely inside the source's "every required vector". | **`EXACT` FALSE — CONFIRMED** |
| **SP-092** | P-L1-C: `"Fail — Any one of these diverges: legal transition behavior / illegal transition behavior / durable state / restart semantics / ordering / failure semantics / normalization / acceptance predicates"` + `"Even if both apps look immaculate."` | All eight divergence dimensions reproduced in the source's own terms and order; none added, none omitted; the "immaculate" consequence carried. A clean literal restatement and a genuine v0.2 improvement. | **HOLDS** |
| **SP-093** | P-L1-B: `"Reference semantics are normative. Emitted source, UI, database layout, and framework structure are projections."`; `"SwiftUI may construct one lifecycle differently from React. Local persistence may use SwiftData/Core Data on one side and IndexedDB on the other. Their internal object graphs can differ completely."` | The five erasable classes (structural, visual, binary, runtime, presentation) each map to a source example; the prohibition on erasing what the Fail list tests is sourced to P-L1-C. Mild categorization of the source's examples into class names. | **HOLDS** (`PLAUSIBLE` mild generalization) |

**B.4 RESULT — `EXACT` overclaims: 3 CONFIRMED (SP-004, SP-090, SP-091) · 2 PLAUSIBLE (SP-041, SP-001) · 5 hold cleanly.**

§17.2's claim *"Unearned `EXACT` relationships remaining: **0**"* is **false**. The candidate explicitly invited this falsification — *"This is a claim a reviewer is invited to falsify, not a mechanical result"* — and the invitation was well made: the §17 mechanism is exactly what made these three findable. Repair surface 7 built a working instrument and then misread its own output.

### B.4-F6 — **CONFIRMED DEFECT** — SP-090's declared precondition does not entail its own oracle

Beyond the entailment question, SP-090's added precondition is *itself insufficient*. It declares "an empty **current cycle**", but its oracle asserts `entries.count = 1`, and per SP-019 `entries` denotes **durable ordered Entries** across the ledger — not the current cycle. SP-040 expressly permits the initial condition to "contain Entries preserved from earlier DaySlots", and SP-049 preserves them across DaySlot transitions.

**Counterexample.** Initial state: `idle`, current cycle empty, durable history `[E_prior]` from DaySlot D0 — a configuration SP-040 explicitly admits. Run the founder vector at D1. Result: `entries.count = 2`, not 1. SP-090's stated precondition is satisfied; its oracle fails.

The clause requires an **empty durable history**, and declares only an empty current cycle. That gap is an **undeclared founder input** in the strict CR-01 sense: the sealed vector needs an initial condition the clause does not supply.

---

## 8. PASS C · residual-gap adjudication of `SP-R02-GAP-01`

**ANSWER: D — the commission was misread. §6.11 does not require an RC-0001 invocation-capability boundary.** Consequence B follows: the requirement is satisfiable without restoring authority as a transition precondition.

### 8.1 What §6.11 actually says

> Provide minimal substrate-independent traces that include:
> - one successful operation;
> - one refused operation;
> - one contemplated discontinuity;
> - **one observer disagreement or visibility boundary, if the program permits either;**
> - **one authority boundary;**
> - one temporal, duplicate, or conflict edge case;
> - one pair of outcomes that look similar operationally but differ semantically.

The conditional "if the program permits either" attaches to the observer bullet alone. The authority bullet is unconditional. **So the requirement is live** — options A and D both survive that reading, and the question turns on what "authority" means in this commission.

### 8.2 The commission defines "authority" as confirmation authority, not invocation capability

The commission uses the term consistently, and never once in the capability sense:

- **§6.2** — *"Observation and authority must be modeled separately; ability to see a fact does not imply **power to confirm it**."*
- **§6.8 "Authority and confirmation semantics"** — *"Specify which states **count without confirmation**, which **require confirmation**, **who can confer it**, whether it can be **revoked**, and whether recorded intent must remain distinguishable from accepted fact."*

Throughout, authority is the **power to confer or withhold confirmation on a fact**. Nowhere does the commission equate authority with permission to invoke an operation. Those are different concepts, and §6.11's bullet inherits §6.2/§6.8's sense — it is the same document's vocabulary.

### 8.3 The candidate mapped the requirement onto the wrong concept

v0.1's FT-05 read, verbatim:

> `FT-05 · authority boundary | pure Observer attempts begin at idle → inspect | begin rejected INVOCATION_NOT_PERMITTED; state remains idle; no Entry`

That is an **invocation-capability** trace wearing an authority label. It was never a §6.11 authority-boundary trace in the commission's sense. **Withdrawing it therefore removed nothing that §6.11 required** — it removed the direct expression of the CR-01 defect, which is exactly what CR-01 demanded.

§12.2's premise — *"Under v0.2 there is no in-program authority boundary to exercise, because capability was removed"* — rests on the conflation. Capability was removed; **confirmation authority was never located in capability**, so its boundary is untouched.

### 8.4 v0.2 already answers §6.8 and already contains the authority boundary

v0.2's answer to §6.8 is complete and negative, which the commission expressly permits:

| §6.8 question | v0.2 answer | Clause |
|---|---|---|
| which states count without confirmation | all of them — lawful transition suffices | SP-060 |
| which require confirmation | none | SP-060, SP-039 |
| who can confer it | nobody; no such construct exists | SP-029, SP-016 |
| whether it can be revoked | inapplicable; no correction or invalidation transition | SP-048, SP-025 |
| recorded intent distinguishable from accepted fact | yes — pending content is visibly pending | SP-022, SP-064 |

And the boundary itself is normatively load-bearing in v0.2, in **SP-003**: *"Entry status complete means the program's complete transition succeeded … it is **not independent proof that an external-world act occurred**."* That line — ledger authority stops at the ledger — is the authority boundary. It is stated, sourced, and operative. What §12.1 lacks is a **trace row designated to exercise it**, not the boundary.

### 8.5 Why this is a coverage gap, not a semantic impossibility

I record, without authoring a repair, that a §6.11-shaped trace over the existing clause set is constructible in principle: any trace whose content-bearing `record` would tempt an embodiment to adjudicate the content's world-truth exercises SP-003/SP-060/SP-061/SP-064, and its falsifying observation is content-sensitive acceptance or a required confirmation step — both already forbidden by SP-032's content-blind biconditional and SP-039. **I am not inventing an authority mechanism to make commission test 8 green; the mechanism is already in the candidate.** Selecting and writing that row is authorship, and it is not mine to perform.

### 8.6 Adjudication

```
A · genuinely required and currently absent      REJECTED — required, but not the thing
                                                  the candidate says is absent
B · satisfiable without restoring authority as
    a transition precondition                     TRUE, and follows from D
C · conflicts with L1/FD-01, exposing a
    commission-level reconciliation defect        REJECTED — no conflict exists once
                                                  authority is read as confirmation
                                                  authority. The commission needs no
                                                  amendment.
D · misread; does not require an RC-0001
    authority boundary of the kind withdrawn      ADOPTED
```

**`SP-R02-GAP-01` is not a genuine commission-level tension between §6.11 and the CR-01 repair.** It is a §12.1 coverage gap produced by mapping "authority boundary" onto invocation capability. No commission amendment is required, so **no block verdict is returned**.

**But the gap is still open at review time.** §12.1 contains no designated authority-boundary trace, §12.2 mischaracterizes the reason, and A-07 is described as determining "whether `SP-R02-GAP-01` is a real gap" when in fact A-07 does not control it — the answer does not depend on the capability decision at all. Commission acceptance test 8 is therefore still not green, and **commission residual gaps ≠ 0**.

The candidate deserves credit for disclosing the gap rather than self-waiving it. Disclosure is not closure, and the binding threshold line is explicit that it cannot be.

---

## 9. Commission acceptance — cold re-run

| Test | v0.1 cold | v0.2 author | **v0.2 cold** | Reason |
|---|---|---|---|---|
| 1 exact target path | PASS | PASS | **PASS** | authorized locus occupied |
| 2 substrate-independent | PASS | PASS | **PASS** | no mechanism selected |
| 3 provenance on every clause | FAIL | PASS | **FAIL** | three `EXACT` overclaims survive (B.4) |
| 4 operation success/refusal/consequence | FAIL | PASS | **FAIL** | refusal-class nondeterminacy (B-F3) |
| 5 discontinuity survival/destruction/order/degradation | FAIL | PASS | **PASS** | L/T partition holds under attack (§4) |
| 6 observer/confidentiality/authority separated | FAIL | PASS | **PASS** | projection removes the second trace program; concepts separated at SP-011 |
| 7 time and daily explicit or unresolved | FAIL | PASS | **PASS** | A-04 disclosed with installed branch; exclusion verified |
| 8 high-risk falsifying traces | FAIL | PASS with gap | **FAIL** | authority-boundary row absent (Pass C); FT-08 discriminates an open alternative (B-F3) |
| 9 Q1–Q16 crosswalk | FAIL | PASS | **FAIL** | Q2 (truth after refusal) is nondeterminate under B-F3 |
| 10 unresolved docket complete | FAIL | PASS | **PASS** | closure classes applied; A-07 added; inconsistency at B.3-F5 is disclosure quality, not completeness |
| 11 no representation future | PASS | PASS | **PASS** | §15 firewall holds |
| 12 no implementation machinery | PASS | PASS | **PASS** | verified |
| 13 unratified and unsealed | PASS | PASS | **PASS** | header and §19 accurate |
| 14 exact commands, hashes, Git state | PASS MECH | PASS MECH | **PASS MECHANICALLY** | §16.4 counts reproduce exactly; two narrative scan claims wrong (B-F8/B-F9) |

**Cold commission acceptance: 10 PASS / 4 FAIL.** v0.1 cold was 6 PASS / 8 FAIL. Real, measurable movement.

---

## 10. Threshold checklist

| Requirement for `PASS` | Result | Basis |
|---|---|---|
| Cold Review 001 findings 9/9 CLOSED | **FAIL** — 8 CLOSED, 1 PARTIALLY_CLOSED | CR-08 (§2) |
| seven repair surfaces 7/7 effective | **FAIL** — 5/7 fully effective | surfaces 1 and 7 (§2.1) |
| L1 contradictions 0 | **FAIL** — 1 | SP-132 vs P-L1-B constitutional law 3 (B.1-F1) |
| undeclared founder inputs 0 | **FAIL** — 1 | SP-090's empty-history precondition (B.4-F6) |
| docket classifications accurate | **PARTIAL** — 6/7 accurate; A-07 incomplete; A-01 justification self-contradicting | B.3, B.3-F5 |
| unordered concurrency impossible/excluded | **PASS** | SP-071 serializes; SP-120 excludes; attack failed |
| restart contradiction absent | **PASS** | full B.2 trace; no contradiction |
| L/T leakage absent | **PASS** | biconditional preconditions make it mechanically visible (§4.2) |
| `view(n)` semantic mutation impossible | **PASS** | SP-111, SP-112, SP-113; attacks failed |
| FT-03 decides A-03 | **NO — PASS** | branch-parameterized; no FT row discriminates A-03 |
| `EXACT` overclaims 0 | **FAIL** — 3 confirmed | SP-004, SP-090, SP-091 (B.4) |
| founder vector self-sufficient | **PARTIAL** — self-sufficient as to invoker/capability; not as to initial history | §11.1 verified; B.4-F6 |
| **commission residual gaps 0** | **FAIL** — 1 open | `SP-R02-GAP-01`: §12.1 coverage gap survives (Pass C) |

**The last line is binding, and it fails.** `SP-R02-GAP-01` remains open at review time. Under Pass C it is *not* the commission-level tension the candidate describes — it is narrower and more repairable than disclosed — but §12.1 still contains no authority-boundary trace and commission test 8 is still not green. v0.2 cannot receive `PASS` for having disclosed the gap well, and five other threshold lines fail independently.

**VERDICT: `CHANGES_REQUIRED`.**

Not `BLOCKED`: no packet evidence was missing, no digest mismatched, no founder authority was required to reach these findings, and the resolution requires no commission amendment.

---

## 11. Repair boundary for a v0.3 movement

Stated as boundaries, not as chosen semantics. This review selects no alternative and adjudicates no docket item.

1. **SP-132 / SP-091** — close the substrate-filter channel. The candidate already owns the correct pattern at SP-120: *exclude* the under-determined presentation rather than admit it silently. Either generalize SP-131 beyond the SP-090 vector to every required vector, or make pre-boundary refusal a typed, observable capability-loss fact as P-L1-B constitutional law 3 requires. Do not leave admission membership substrate-determined.
2. **SP-033 / SP-035 / SP-043** — supply a precedence rule for co-occurring refusal conditions, so `illegal_transition_count` is a function of the input. Then re-derive FT-08 under SP-140.
3. **Sweep SP-140 across all ten FT rows**, not only FT-03. FT-08 shows the surface was patched at one site.
4. **SP-004** — restore P-L1-B's sixth exclusion, or narrow the pin so the clause does not claim literal coverage of a source it partly reproduces.
5. **SP-090** — declare the actual initial condition its oracle requires, and either demote to `ELABORATES` or confine the `EXACT` claim to the six oracle values, recording the founder's "might require" modality.
6. **SP-091** — restore the source's subject ("every required vector"), not "the same SemanticProgram input".
7. **SP-041** — correct §17.1's argument, which describes three progression edges where the source draws two; consider `ELABORATES`.
8. **§13.1** — apply T(A) uniformly to A-01 and A-02, correct the A-03 cell, and record A-07's out-of-boundary residue.
9. **§16.4 / §17.3** — correct the ontology scan row count and add SP-029 to the `ORTHOGONAL` enumeration.
10. **§12.1 / §12.2** — add the confirmation-authority boundary trace and correct §12.2's account of why v0.1's FT-05 was withdrawn. Decouple `SP-R02-GAP-01` from A-07.

A repaired v0.3 requires another lineage-independent review before founder adjudication.

---

## 12. Terminal authority

```
COLD REVIEW 002 RESULT        CHANGES_REQUIRED
COLD REVIEW 001 SUBJECT       3e675d9e…551537 · PRESERVED · UNMODIFIED
COLD REVIEW 002 SUBJECT       611a782e…eb007 · PRESERVED · UNMODIFIED
CANDIDATE REPAIR              NOT PERFORMED
FOUNDER DECISIONS A-01–A-07   NOT RESOLVED
SEMANTICPROGRAM SEAL          NOT GRANTED
FOUNDER ADJUDICATION          NOT PERFORMED
REQUIREMENT EXTRACTION        NOT AUTHORIZED
REPRESENTATION SELECTION      NOT AUTHORIZED
IMPLEMENTATION                NOT AUTHORIZED
PROTOCOL MUTATION             NOT AUTHORIZED
COMMISSION AMENDMENT          NOT AUTHORIZED · NOT REQUIRED (Pass C)
HBC MUTATION                  NOT AUTHORIZED
GIT STAGING / COMMIT / PUSH   NOT AUTHORIZED
NEXT LAWFUL GATE              bounded v0.3 repair under separate authority
```

`COLD REVIEW PASS` was not returned, and would in any case mean only `READY_FOR_FOUNDER_ADJUDICATION` — not a seal, not ratification, and no downstream authority.

---

## 13. Integrity block

### 13.1 Packet integrity at close

All ten packet digests recomputed at close and **unchanged** from admission: subject `611a782e…eb007`, v0.1 `3e675d9e…551537`, Cold Review 001 `54de4a52…6276f`, commission `9a04124a…dcc04e`, SLR-01-R1 `a506352a…4e68a6`, custody `0f61f7bb…734600`, L1 container `cee97abe…d81ebe`, and the three L1 text pins `4cfd687b…f4bb5` / `796a3588…190e221` / `e951c1bc…2b8e3`.

### 13.2 Files modified by this review

**Exactly one file was created:**

```
/Users/millysituated/RUORA/governance/OURSELF-RCP-RC0001-SEMANTICPROGRAM-v0.2-LINEAGE-INDEPENDENT-COLD-REVIEW-002.md
```

It did not exist before this review (verified absent at admission). **No other file in any repository was created, modified, deleted, or renamed.** No candidate was repaired. No commission was amended. No custody record was mutated. No founder decision was adjudicated. No seal was granted.

Working files used during analysis were confined to `/tmp` and are outside every repository boundary.

### 13.3 Git state — nothing staged

```
GOVERNANCE REPOSITORY   /Users/millysituated/RUORA
BRANCH                  main
HEAD                    7387fe4083ea30558f4799f6ec48b3b0b6e64eb8   (unchanged)
STAGED PATHS            0
TRACKED MODIFIED        1   (doctrine/self_axiom.md — pre-existing, untouched,
                             not opened as evidence)
STATUS ENTRIES          34 before this report
AUTHORIZED OUTPUT       this file, untracked and unstaged
```

No `git add`, `git commit`, `git push`, or staging operation of any kind was performed. The pre-existing modified tracked file and all pre-existing untracked paths were preserved and were not opened as semantic evidence.

The session's working directory (`/Users/millysituated/RUORA/projects/epistemic-systems-metrology`, HEAD `8097d18`) is a **separate repository** from the governance repository above and was not modified. This explains the difference between the ambient session git snapshot and the governance HEAD recorded here; it is not evidence drift.

### 13.4 HBC untouched — verified

```
HBC PATH                /Users/millysituated/RUORA/projects/hbc-html
HEAD                    e350205f12c140b8216090b935f874cbbc454dee   ✓ matches required baseline
TRACKED FILES           30                                          ✓ matches required baseline
TRACKED CHANGES         0                                           ✓ matches required baseline
STAGED PATHS            0
UNTRACKED               output/  (pre-existing; not created, opened, or modified
                        by this review)
```

**HBC was not opened, modified, staged, or treated as evidence.** No renewed HBC integrity or suitability claim is made beyond the live Git metadata above.

### 13.5 Reviewer honesty record

Where I could not break something, I said so: §6 records eleven attacks that failed, including a full independent recomputation of §16.4 that reproduced the candidate's counts exactly. Findings I could not fully establish are marked `PLAUSIBLE` (B.2-F7, the A-03 residual, SP-041, SP-001, SP-093, SP-029's classification) rather than promoted to `CONFIRMED`. Ambient context received before the packet is disclosed in full at §0, including the one place it influenced method rather than conclusion.

---

*v0.2 built an instrument sharp enough to cut its own author. Three of its ten `EXACT` claims fell to the falsification conditions it wrote for itself — which is what a working instrument looks like. The remaining defect of consequence is that one gate was moved outside the room rather than taken apart, and the room is where conformance can see.*
