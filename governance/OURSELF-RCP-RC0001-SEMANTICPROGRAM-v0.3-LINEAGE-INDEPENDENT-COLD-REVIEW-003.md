# RC-0001 SEMANTICPROGRAM v0.3 — LINEAGE-INDEPENDENT COLD REVIEW 003

**VERDICT** `CHANGES_REQUIRED`
**DATE** 2026-08-13
**SUBJECT** `governance/OURSELF-RCP-RC0001-DURABLE-DAILY-RITUAL-LEDGER-SEMANTICPROGRAM-v0.3-CANDIDATE.md`
**SUBJECT DIGEST** SHA-256 `55c590ead44e38248a7f97405c8cb23740018df4bd9b154a8a0fd3df99dd7f8e` — computed by this review before any content was read; matches the mandate.

**AUTHORITY OF THIS RECORD.** This is an adjudication, not a repair. No clause is proposed, no
revision is drafted, no artifact in the evidence set is modified. Even a `PASS` here would mean
only `READY_FOR_FOUNDER_ADJUDICATION`; it would not ratify the SemanticProgram. This review
returns `CHANGES_REQUIRED`, which is weaker still.

---

## 0. Epistemic classification and packet integrity

### 0.1 Classification — recorded verbatim as mandated

```
LINEAGE-INDEPENDENT     YES
MODEL-INDEPENDENT       NO
EXTERNAL                NO
```

This reviewer authored no artifact in this corpus and received no author-side account of whether
any repair is good. No session transcript, job directory, or narrative-of-the-author document was
consulted. **The independence claimed is lineage independence only.** A defect visible only to a
differently-trained reader could survive this review unremarked, and the strength of every negative
finding below ("I could not construct X") is bounded by that.

### 0.2 Evidence-set digests — independently computed

| Role | File | SHA-256 | Match |
|---|---|---|---|
| Subject | `…SEMANTICPROGRAM-v0.3-CANDIDATE.md` | `55c590ea…dd7f8e` | ✓ |
| Prior subject (CR-001) | `…SEMANTICPROGRAM-v0.1-CANDIDATE.md` | `3e675d9e…551537` | ✓ |
| Prior subject (CR-002) | `…SEMANTICPROGRAM-v0.2-CANDIDATE.md` | `611a782e…feb007` | ✓ |
| Defect register 001 | `…v0.1-LINEAGE-INDEPENDENT-COLD-REVIEW-001.md` | `54de4a52…76276f` | ✓ |
| Defect register 002 | `…v0.2-LINEAGE-INDEPENDENT-COLD-REVIEW-002.md` | `bdd8c218…46167e` | ✓ |
| Lineage adjudication | `…SLR-01-R1-CORRECTED-SOURCE-LINEAGE-RECONCILIATION.md` | `a506352a…4e68c6` | ✓ |
| Custody witness (KNOWN INCOMPLETE) | `…SOURCE-CUSTODY-001.md` | `0f61f7bb…734600` | ✓ |
| Authoring commission (L2) | `…SEMANTICPROGRAM-AUTHORING-COMMISSION.md` | `9a04124a…5dcc04e` | ✓ |
| L1 container | Codex rollout `019ff7ee-…-74a0aae7d677.jsonl` | `cee97abe…d81ebe` | ✓ |

### 0.3 L1 extraction — performed by this review, not adopted

Extracted read-only with the mandated method, blocks joined with LF, no terminal LF:

```
jq -j 'select(.ordinal==N) | .payload.content | map(.text) | join("\n")' <container>
```

| Pin | ordinal | text SHA-256 recomputed | Match |
|---|---|---|---|
| P-L1-A | 59 | `4cfd687b2ea9cdbcf366c29a60b124e76cf0f9cce9fb4de897d812b69b3f4bb5` | ✓ |
| P-L1-B | 72 | `796a3588fbd8fbc611b62f6bba2267d462dd42f92f865a876f82e3387190e221` | ✓ |
| P-L1-C | 85 | `e951c1bc4f3fdb0fdfe4f133624acfd521dfedb7240bbdb80a0fe4147d82b8e3` | ✓ |

**Every `EXACT` test below was run against these extracted bytes** — not against the candidate's
quotation of the founder, and not against SOURCE-CUSTODY-001 §3, which the mandate records as a
known-incomplete normalization and which this review used for nothing.

---

## 1. LAYER 1 — REGRESSION CLOSURE

Method rule applied throughout: **test the mechanism, not whether v0.3 contains language
describing the mechanism.** v0.3 §16.2's own dispositions were treated as an adversary's
assertions and re-derived independently.

### 1.1 Cold Review 001 — all nine findings

| ID | Defect | Disposition | Test that produced it |
|---|---|---|---|
| CR-01 | Founder vector succeeds only after an unstated Operator is supplied | **CLOSED** | Walked all four vector steps against SP-030/SP-032/SP-034 preconditions: each discharges on state + content string alone. SP-130 forbids any invocation-capability precondition; SP-039 forbids Assertion/Adjudicator/capability preconditions; §11.1 supplies no principal. No Operator is reachable. |
| CR-02 | A-01 and A-02 not open in the operative envelope | **CLOSED** | SP-018 now states only the literal two-field observation and disclaims further assertion; SP-101 expressly admits both readings of the state/status relation; A-02 is labelled OPEN with no installed branch. The v0.1 `EXACT` distinctness claim that excluded a model is gone. (SP-018 is nonetheless *cited* for the state progression in §16.1 S-02 and §10 — see CR3-14.) |
| CR-03 | A-03 has two lawful models while FT-03 silently chooses one | **CLOSED** | SP-140 voids any FT row that discriminates an admitted alternative; FT-03 restricts its falsifiable content to consequences shared by both A-03 models and carries an explicit inert branch note. Re-ran FT-03 under A-03(A) and A-03(B): identical falsifiers. |
| CR-04 | A-04/A-05/A-06 are OPEN labels over selected behaviour | **CLOSED** | All three now carry `OPERATIVELY_DECIDED` with a named installed branch, and the cited exclusions (SP-019's closed L-fact set; SP-029's existence prohibition; SP-048's no-correction closure) were each read in full and do entail the exclusion claimed. |
| CR-05 | Concurrency has no canonical semantic order | **CLOSED** | SP-071 (total order, ordinal assigned before evaluation), SP-120 (undetermined-order vector is malformed and may not be run), SP-121 (divergent Entry sets impossible for one input) all survive. FT-05/FT-06 exercise both limbs. *Note:* v0.3 deleted SP-071's definition of the sequence's element domain — this creates a new gap (CR3-06) but does not reopen CR-05. |
| CR-06 | Restart is both invisible and a new semantic event | **CLOSED** | SP-103 disjoint partition, SP-102 places boundary markers in T, SP-104 witness law, SP-105 forbids transition evaluation reading a T-fact. Re-ran the CR-002 six-step trace `begin; record("Reflect"); restart; restart; complete; restart`: no contradiction. |
| CR-07 | `inspect` state-neutral but not fact-neutral; freshness undefined | **CLOSED** | `inspect` is withdrawn as an operation (§4.2, §10); SP-110–SP-113 replace it with a total projection emitting no T-fact and occupying no position; SP-113 disclaims currentness. *Residue:* v0.3 silently deleted "or maximum-staleness" from SP-113 inside a section labelled unchanged (CR3-05). |
| CR-08 | SP-004 is not an `EXACT` restatement of the founder non-goals | **CLOSED** | Member-for-member against raw L1: P-L1-A's five exclusions quoted verbatim; P-L1-B's six quoted verbatim including "No seductive product surface hiding compiler defects"; all seven P-L1-C non-goals present in source order. Zero source members absent. (The phrase "literally and in full" overstates the third register's rendering — CR3-15, MINOR — but no member is lost.) |
| CR-09 | The provenance audit is structural, not semantic | **PARTIALLY_CLOSED, with one component REGRESSED** | Three parts. **(i) §17's entailment review — genuinely repaired**: it states the correct bound (*"A mechanical script may audit completeness; it may never award `EXACT`"*) and supplies nine-attack arguments for all nine `EXACT` rows; I used it to falsify SP-091. **(ii) §17.3 then delegates the `ORTHOGONAL` enumeration to the same script** — a substantive entailment judgment by §0.3 — reinstating the defect for those nine rows (CR3-03). **(iii) REGRESSED:** CR-002 closed CR-09 partly on the rename and disclaimer. v0.2 §16.4 was headed *"Metadata-shape audit — **renamed per CR-09**"* and opened *"**This audit proves row grammar and nothing else.** It cannot establish source fidelity, semantic entailment, or state-machine determinacy."* **v0.3 deletes both**, replaces them with *"the script governs"*, and adds a global `AUDIT_RESULT PASS` token that v0.2's block did not contain (`grep -c AUDIT_RESULT` on v0.2 → 0). v0.3's only surviving disclaimer covers `EXACT` alone. I re-ran CR-09's own decisive counterfactual against v0.3's auditor and **it still succeeds** (§6.4, PROBE-1/PROBE-5). |

**CR-001 tally: 8 CLOSED · 1 PARTIALLY_CLOSED · 0 NOT_CLOSED · 0 REGRESSED.**
v0.3 §18 claims **9/9 CLOSED**. That claim is **not sustained**.

### 1.2 Cold Review 002 — every finding, including the three v0.3 §16.2 omits

| ID | Defect | Disposition | Test that produced it |
|---|---|---|---|
| CR-08 (carried) | SP-004 register incomplete | **CLOSED** | §1.1 above. |
| B.1-F1 | SP-132 relocates an outcome-affecting gate outside the conformance boundary | **CLOSED** | The **comparison mechanism changed**; this is not a relocation. v0.2 SP-091's antecedent was "the same SemanticProgram input" (post-filter, substrate-dependent); v0.3 SP-152 compares the **presented sequence** and adds a per-element disposition-equality predicate that did not exist in v0.2 in any form. Full construction at §3. Residual bound at CR3-08. |
| B.1-F2 | §17.3's `ORTHOGONAL` justification for SP-132 is false | **CLOSED** | SP-132 withdrawn entirely; my own auditor run confirms `ORTHOGONAL_ROWS 9` and the list excludes SP-132. |
| B.2-F7 | SP-051 / SP-104 drafting tension over T-fact preservation (`PLAUSIBLE`) | **PARTIALLY_CLOSED** | The tension is removed — by **deleting** SP-051's "the outcome stream is otherwise unchanged" (byte-diff against v0.2 confirms). But CR-002 reconciled B.2-F7 on the premise that *"T-facts [are] a pure function of the input trace, and no two conforming implementations can differ because of it."* **Repair 1 makes that premise false**: SP-102 places the disposition record in the T-fact set, and dispositions are substrate-dependent by construction. See CR3-02. |
| B.3-F5 | §13.0's closure test applied inconsistently to A-01 and A-02 | **PARTIALLY_CLOSED** | A-01's self-contradicting note is corrected and an admissibility criterion is added. But the new criterion is two-valued, its output mapping was made non-exclusive by the repair itself, and **the same defect class now appears in A-03** — a label not derivable from the document's own rule. §4. |
| B-F3 | Refusal-class selection nondeterministic; `illegal_transition_count` implementation-dependent | **CLOSED at the precedence level** | I enumerated the full Cartesian `state × content-condition × operation` (18 cells) and had it independently re-enumerated. **18/18 EXACTLY_ONE, 0 ZERO, 0 MULTIPLE.** The `complete`@idle collision (C06) is closed by a mechanism — step 1's "and evaluation stops" — not by prose. SP-031/033/035 were rewritten to derive from SP-160 rather than restate the old disjunction. §5.2. |
| B-F8 | §16.4's ontology scan misreports its own result | **CLOSED as a count** | I ran v0.3's auditor against v0.2 myself: `ONTOLOGY_ROWS 6`, matching CR-002's independent hand recomputation against v0.2's prose claim of 3. The *count* is repaired. The `PROHIBITS` *classification* attached to it is not a measurement — see §6.4 PROBE-A9. |
| B-F9 | §17.3's `ORTHOGONAL` enumeration omits one row | **PARTIALLY_CLOSED** | The count is now machine-generated and correct (9, verified). But the repair **deleted the per-row substantive justification rather than correcting it**, leaving nine `ORTHOGONAL` entailment judgments with zero justification and a regex as their stated authority. CR3-03. |
| B.4 · SP-004 | `EXACT` overclaim | **CLOSED** | §1.1. |
| B.4 · SP-090 | `EXACT` overclaim (modality + added precondition) | **CLOSED** | Byte-checked against L1-72:106–122. All six predicates reproduced exactly; the founder's **"might require"** is preserved verbatim; the requirement and the initial condition are moved to SP-094 marked `AUTHOR-PROPOSED`. **This is the single best repair in the document** and I record it as fully successful. |
| B.4 · SP-091 | `EXACT` overclaim (changed subject) | **NOT_CLOSED** | The founder's subject *"for every required vector"* is correctly restored — and then an authored operative sentence is appended **inside the same `FOUNDER_SEALED_L1 / EXACT` row**. CR3-01. |
| B.4 · SP-041 | `EXACT` overclaim (`PLAUSIBLE`; absent from §16.2) | **PARTIALLY_CLOSED** | The fourth-*operation* widening is genuinely repaired and correctly relocated to SP-048 as `AUTHOR-PROPOSED`. The operation→edge mapping and the `active —record→ active` self-loop are **not in L1 at all** and were never audited. CR3-09. |
| B.4 · SP-001 | `EXACT` overclaim (`PLAUSIBLE`; absent from §16.2) | **CLOSED** | Member-for-member verified against L1-59:43–54: all eleven members present in both directions; "substrate-neutral" matches L1-59:60 exactly; the unsourced "observable" is removed. Residual quantifier softening ("whose preserved meaning **includes**") is MINOR. |
| B.4-F6 | SP-090's declared precondition does not entail its own oracle | **PARTIALLY_CLOSED** | The undeclared *initial history* input is now explicit and declared authored. But the vector is **still not self-sufficient**, now on a different coordinate, and v0.3's own edits caused it. **CR3-B01, BLOCKING.** |
| Pass C · SP-R02-GAP-01 | §12.1 has no designated authority-boundary trace | **PARTIALLY_CLOSED** | Tested cause and symptom separately. **Cause — CORRECTED:** v0.2's §12.2 asserted a genuine §6.11-vs-CR-01 tension; v0.3's §12.2 restates Pass C's answer D correctly, records `A-07 RELATION: none`, and invents no ontology. That repair is real. **Symptom — nominally filled only:** FT-11 is a designated row, but under v0.3's own governing repair criterion (*"either makes the defect impossible or makes it explicitly detectable"*) it makes almost nothing newly detectable — CR3-18. v0.3's `STATUS CLOSED` overstates. |
| §13.1 A-03 cell (Minor) / A-03 residual (`PLAUSIBLE`) | A-03 disclosure quality | **NOT_CLOSED** | Superseded and worsened: A-03's label is now underivable from v0.3's own rule. §4. |

**CR-002 tally: 10 CLOSED · 5 PARTIALLY_CLOSED · 2 NOT_CLOSED.**
v0.3 §16.2 claims **12/12 dispositioned**; it dispositions twelve and omits four (B.2-F7, B.4·SP-041,
B.4·SP-001, the A-03 residual).

### 1.3 The mandate's specific Layer 1 instruction

> *Verify the capability repair changed the comparison mechanism rather than moving the hole again.
> A relocation that leaves an outcome-affecting gate outside the compared surface is NOT_CLOSED
> regardless of how it is labelled.*

**The comparison mechanism genuinely changed.** SP-152 is a new compared surface with a new
equality predicate; it is not v0.2's clause relabelled. The chain closes end to end and I traced
every link: SP-150 assigns → SP-102 places the disposition record in the T-fact set → SP-013 and
SP-114 make the witness observe it → SP-152 supplies the equality predicate → SP-093 forbids
normalizing away any distinction needed to evaluate SP-091, which routes to SP-152. **B.1-F1 is
CLOSED.** I say that plainly, and §3 shows the work.

---

## 2. LAYER 2 — FRESH SEMANTIC ATTACK

Each finding carries a concrete trace or enumeration and an explicit falsifier. Findings that did
not survive my own scrutiny were killed and are recorded as such in §2.20.

### CR3-B01 — `illegal_transition_count` lost its scope; the founder vector is not self-sufficient — **BLOCKING**

**Clauses attacked:** SP-043, SP-102, SP-094, SP-040, SP-090 · **founder predicate:** L1-72:120.

**Mechanical fact, verified by grep on both files:**

```
v0.2 SP-102: "…and the derived illegal-transition count over the supplied trace."
v0.2 SP-043: "…contributes one to the illegal-transition count derived over the supplied trace."
grep -c "supplied trace"   v0.2 → 2      v0.3 → 0
```

**v0.3 deleted the scoping phrase from both clauses** and replaced it with a cumulative rule —
SP-043 *"increments by exactly one when and only when the SP-160 result is `INVALID_TRANSITION`"* —
under SP-102's *"append-only and strictly monotonic"*, which affirmatively bars any reset. The
count now has an increment rule, monotonicity and append-only-ness, and **no scope, no initial
value and no reset point**. I searched for `reset`, `per-run`, `per-vector`, `per-trace`,
`initiali[sz]`, `starts at`, `zero at`: no relevant clause exists.

SP-094's initial condition names exactly three things — *"from initial state idle with empty
durable Entry history and empty pending"* — all three L-facts. It cannot name the count, because
the count is a **T-fact** (SP-102), SP-103 makes the classes disjoint, and SP-104 says *"no
preservation obligation ranges over T-facts."*

**Trace — day 2 of a Durable *Daily* Ritual Ledger. SP-017 makes one instance span DaySlots.**

```
DaySlot 1
  instantiate           state=idle, pending=0, history=∅, illegal_count=0        [SP-040]
  present  complete     ADMITTED; state idle → SP-160 step 1 → INVALID_TRANSITION
                        SP-043 → illegal_count = 1
                        SP-035: every L-fact unchanged → idle, pending 0, history ∅
  DaySlot boundary      SP-053 "idle remains idle"; T-facts persist (SP-102 monotonic)

DaySlot 2 — state = idle · durable Entry history = EMPTY · pending = EMPTY
            ↑ SP-094's stated initial condition, all three conjuncts, verbatim

  begin ; record("Reflect") ; complete ; restart      all four ADMITTED
  OBSERVE  state=complete ✓  entries.count=1 ✓  content="Reflect" ✓
           status=complete ✓  history_order=canonical ✓
           illegal_transition_count = 1               ✗  SP-094 and L1-72:120 require 0
```

**No clause is violated.** SP-040 ✓ (satisfied at instantiation). SP-094's three stated conjuncts ✓.
SP-043 ✓ (incremented exactly once for exactly one `INVALID_TRANSITION`). SP-102 ✓ (0→1, monotonic).
SP-160 ✓. SP-150/SP-152 ✓ (every element `ADMITTED`, both embodiments). SP-104 ✓. SP-053 ✓.
**The founder's sealed acceptance predicate fails while every normative clause holds.**

This is not a contrived edge. For a *daily* ledger only day 1 can be a fresh instance, so **every
subsequent run of the founder vector is exposed.** A restart variant is equally available.
FT-02's expected `illegal count 1` is unsound for the same reason.

**Why it is a regression.** Two v0.2→v0.3 edits jointly opened it, and §16.2 presents one of them
as a repair: (i) "over the supplied trace" deleted from SP-043 and SP-102; (ii) SP-090's
cycle-scoped *"empty current cycle"* replaced, per the B.4-F6 disposition, by the strictly
L-fact-scoped *"empty durable Entry history"*. Under v0.2's wording the count was derived over the
supplied trace and was 0 for the vector regardless of history. **v0.2 was sound on this coordinate
and v0.3 is not.**

**Falsified by:** any clause that scopes the count to the presented sequence or required vector,
adds `illegal_transition_count = 0` to SP-094's initial condition, or permits a boundary reset.
None exists, and SP-102's "strictly monotonic" bars the third.

### CR3-01 — SP-091 carries authored operative law inside a `FOUNDER_SEALED_L1 / EXACT` row — **MATERIAL**

**Clause:** SP-091 · **Controlling bytes:** L1-85:89–97.

SP-091 in full: *"For every required vector, the reference semantic trace and each normalized
target trace must be equal. **Comparison is over the presented sequence per SP-152.**"* — marked
`L1 | FOUNDER-DIRECTED | FOUNDER_SEALED_L1 | EXACT | P-L1-C`.

P-L1-C on this point is, in its entirety:

```
Pass
Reference trace  =  Normalized Web trace  =  Normalized iOS trace
for every required vector.
```

**Verified: the string `presented sequence` occurs 0 times in L1-59, L1-72 and L1-85.** SP-152 is
`AUTHOR-PROPOSED / ELABORATES`. The second sentence is therefore an **extra candidate member** —
the first attack on §17.1's own list of nine — and **§17.1's audit of SP-091 does not mention it
at all.** The first sentence is a correct repair; the second is authored law wearing a founder seal.

This is not cosmetic. §0.5 makes the capability repair governed by "SP-150–SP-154, **SP-091**", and
§16.2 calls SP-091's restatement "also the capability-leak closure." So a `FOUNDER_SEALED_L1` row
is now **parameterized by an `AUTHOR-PROPOSED` clause** — its normative content changes if SP-152
changes. Under the FD-01 ladder (§0.1) that inverts the authority order, and it is the precise
failure L1-59:39 names: *"authority must travel through compilation without being collapsed into
meaning."* The document already knows the correct technique — it applied it one row earlier, to
SP-090/SP-094.

**Falsified by:** L1 text containing the second sentence's proposition (none exists), or a split of
SP-091 on the SP-090/SP-094 pattern.

### CR3-02 — §7.1's T-fact observation law is falsified by Repair 1 — **MATERIAL**

**Clauses:** §7.1 (T-fact row), SP-102, SP-150, SP-151, SP-152.

§7.1 states, of the class *"dispositions, operation outcomes, restart markers, illegal-transition
count"*: **"the same presented sequence yields the same stream."**

Dispositions are T-facts (SP-102). SP-152's entire purpose is that two embodiments **given the same
presented sequence** produce **different** dispositions — that is how divergence is detected. So
§7.1's law is false by construction of the repair, and false specifically of the class it lists first.

This also destroys the premise on which CR-002 reconciled B.2-F7: *"T-facts [are] a pure function of
the input trace, and no two conforming implementations can differ because of it."* After SP-150,
T-facts are a function of `(presented sequence, substrate capability)`.

§7.1 is not an SP row, so §0.4 denies it normative force — but §14 cites §7.1 as the answering
instrument for Q9, Q10, Q11 and Q12, all marked `ANSWERABLE`.

**Falsified by:** showing dispositions are not T-facts, or that §7.1's row does not include them.
It names them first.

### CR3-03 — §17.3 delegates a substantive entailment judgment to a regex — **MATERIAL**

**Clauses:** §17 opening, §17.3, §16.5.

§17 opens correctly: *"A mechanical script may audit completeness; **it may never award `EXACT`**."*
§17.3 then states: *"The enumeration in this subsection is **deliberately not hand-listed** … The
auditor's `ORTHOGONAL_ROWS` output in §16.5 is the **authoritative enumeration**."*

`ORTHOGONAL` is, by §0.3, a **substantive entailment judgment** of exactly the same kind as `EXACT`.
The auditor's `ORTHOGONAL_ROWS` is computed by `re.search(r'\| ORTHOGONAL \|', l)` — **it reads the
label the author typed.** It is structurally incapable of detecting a mislabelled row, which is
precisely the defect CR-002 B.1-F2 found (a false `ORTHOGONAL` on SP-132). The repair for the
*miscount* deleted the per-row justification, so **nine `ORTHOGONAL` relations now carry zero
substantive justification** and a circular authority.

Two look wrong on inspection: **SP-010** ("Participant identity proof and *authentication* mechanics
are outside RC-0001") restates L1-59:41 "no auth" / L1-72:64 "No authentication" — a clause
restating a founder exclusion elaborates an L1 proposition rather than being orthogonal to it; and
**SP-055**, whose revised text carries L1-72 law-3 content ("presented intent is never silently
removed") while labelled `ORTHOGONAL`.

**Falsified by:** per-row justification that each of the nine is satisfiable-or-not without
affecting any L1 proposition. None is offered.

### CR3-04 — `CAPABILITY_DEGRADED` has no denotation, no assignment rule and no coverage — **MATERIAL**

**Clauses:** SP-150, SP-151, SP-152, SP-153, SP-093, FT-12, §15.

Mechanical facts, verified: **`CAPABILITY_DEGRADED` occurs at exactly two lines** in the whole
document — the §2.0 ASCII diagram and SP-150's enumeration. **`loss class` occurs exactly once**
(SP-151). §0.4: *"Only **SP** rows are normative"* — the diagram is not one. §15 pins six
subject-local terms and defines neither `degraded` nor `loss class`.

Three consequences, each with a trace, at §5.1.3. In summary:

1. **No definition.** SP-153 (*"decides only whether a presented element reaches the
   SemanticProgram"*) forces a binary domain, so `CAPABILITY_DEGRADED` must mean *does not reach* —
   operationally identical to `CAPABILITY_UNSUPPORTED`. The ordinary meaning (element processed with
   reduced fidelity) is thereby **excluded**, leaving the token denoting nothing distinct.
2. **No assignment criterion.** No clause says which of the two non-`ADMITTED` labels an element
   receives. SP-131 speaks of *"the one this SemanticProgram assigns it"* — an assignment function
   no clause defines. So SP-152 can declare two behaviourally identical embodiments nonconforming
   because one typed `DEGRADED` and the other `UNSUPPORTED`.
3. **The typing never enters the comparison.** SP-152 compares *"the same disposition"* — a
   three-token alphabet. It never mentions SP-151's `loss class`, and SP-093 affirmatively licenses
   erasing anything not needed to evaluate SP-090–SP-092. **L1-72 law 3 requires capability loss to
   be "typed and explicit"; v0.3 makes it explicit but leaves the type outside the compared surface.**

**Coverage:** FT-12 is titled "capability disposition visibility" and exercises **only**
`CAPABILITY_UNSUPPORTED`; §2.0's worked argument likewise. **The `CAPABILITY_DEGRADED` branch has
zero trace coverage and zero worked example anywhere in v0.3.**

**Falsified by:** a clause defining `CAPABILITY_DEGRADED`, assigning it by rule, or requiring loss
classes to be equal.

### CR3-05 — "CARRIED FORWARD UNCHANGED / preserved verbatim" is false, and one such edit broke a clause — **MATERIAL**

I byte-diffed every SP row v0.2 → v0.3. **54 rows changed; 39 carry no `REVISED`/`NEW` marker.**
Most de-annotation is benign. The following sit under headers asserting verbatim preservation:

| Section | Header claim | Reality |
|---|---|---|
| §3.0 | "CARRIED FORWARD UNCHANGED … preserved verbatim" | SP-102 is labelled **REVISED** and SP-105 **NEW** inside that very table; SP-103, SP-104 edited |
| §4.2 | "CARRIED FORWARD UNCHANGED" | SP-110–SP-114 all edited |
| §6 | "CARRIED FORWARD UNCHANGED … Preserved verbatim" | SP-055 labelled **REVISED** inside that table; SP-050, SP-051, SP-052, SP-053, SP-054 edited |
| §8 | "CARRIED FORWARD UNCHANGED … Preserved verbatim" | SP-071, SP-120, SP-121, SP-070, SP-073, SP-083 edited |
| §16.3 | "deliberately not touched: … SP-071, SP-120, SP-121 … SP-110–SP-114" | false for all eight |
| §18 | "concurrency unchanged **YES** / `view(n)` unchanged **YES**" | false as to text |

**Normative text was deleted under these headers:**

- SP-050 lost *"No L-fact is required to be destroyed."*
- SP-051 lost *"the outcome stream is otherwise unchanged."*
- SP-071 lost *"of admitted invocation records and discontinuity boundaries"* — the clause's
  definition of its own element domain, which is the direct cause of CR3-06.
- SP-113 lost *"or maximum-staleness"*.
- SP-112: *"input trace of the same Ledger"* → *"presented sequence"*.

**That last edit falsified the clause.** SP-112 asserts *"`view(n)` has exactly one value for a
given presented sequence and position."* Under SP-150, two embodiments sharing a presented sequence
may differ in disposition and therefore in L-facts, so `view(3)` differs (§3, embodiments W and I).
**v0.2's wording ("input trace" = post-admission) was true; v0.3's is false.** A clause declared
"deliberately not touched" was silently edited into falsehood by the repair.

Nine source pins back to Cold Review 001 findings were also stripped (`P-L4-CR1 CR-05/CR-06/CR-07`,
`§7`), removing the traceability that makes CR-001 closure checkable.

**Falsified by:** showing any listed diff is wrong. Reproduce with `grep -m1 "^| SP-071 |"` on both files.

### CR3-06 — position semantics for non-`ADMITTED` elements are underdetermined — **MATERIAL**

**Clauses:** SP-071, SP-151, SP-110, SP-112, SP-013, SP-050, SP-053, §15.

§15: *"`position` means only the **SP-071 admission ordinal**."* SP-071: *"Every **admitted
invocation** receives exactly one position ordinal **at admission**."* SP-151: a non-`ADMITTED`
disposition *"**occupies a position in the trace**."* The author wrote the advancing clause twice
for non-invocation elements (SP-050, SP-053: *"position advances by one"*) and **did not write it in
SP-151.** Two readings survive:

- **P1 · position-consuming.** Then position 3 exists in embodiment I but is not an *operation*
  position (the element never reached transition law, SP-153), so it falls outside SP-110's domain
  — and SP-112's totality claim has an unacknowledged hole.
- **P2 · admission-only.** Then in embodiment I `complete` occupies ordinal 3 while in W it occupies
  4; **the same ordinal names different presented elements across substrates**, and SP-013's
  requirement to observe L-facts *"at an identified operation position"* compares a `record` against
  a `complete`.

**This does not reopen the capability leak** — SP-152 is element-keyed, not position-keyed, so
divergence still localizes at `record("B")`. It breaks the position-indexed witness surface, not
the disposition comparison. I state that plainly.

**Falsified by:** a clause stating whether a non-`ADMITTED` disposition advances the SP-071 ordinal.

### CR3-07 — the content-presence predicate is undefined — **MATERIAL**

**Clauses:** SP-032, SP-033, SP-160 step 2, SP-130, §15.

SP-032 requires *"content is present as a semantic value"* and also calls the result a
*"content-bearing contribution"* — two phrases pulling opposite ways. SP-160 step 2 yields
`MISSING_CONTENT` *"for record without content."* **No clause defines presence, emptiness,
whitespace handling, or arity**, and §15 — the clause whose job is pinning subject-local meanings —
omits `content` and `present`.

Trace, `record("")` at `state = active`, both elements `ADMITTED` in both embodiments:

| | E1 · *presence = a value was supplied* | E2 · *presence = a non-empty value* |
|---|---|---|
| `record("")` | ACCEPTED; pending `[""]` | `MISSING_CONTENT`; no pending |
| `complete` | ACCEPTED; state complete; entries `[""]` | `NO_RECORDED_CONTENT`; state still active |

Neither violates any clause: SP-032 does not say what "present" means; both applied SP-160's
precedence correctly *given their predicate*; SP-043 counts 0 in both. It propagates: for
`begin; record(""); complete; complete`, E1 reaches `illegal_transition_count = 1` (fourth element
is state-illegal) and E2 reaches `0` — divergence on a **founder acceptance predicate**, from a
step-2 ambiguity surfacing as a step-1 outcome one position later.

SP-152 **does** detect the divergence (second conjunct: `ADMITTED` outcomes differ), so this is
"explicitly detectable" under v0.3's own repair criterion and is not a leak. But SP-091's
**reference** trace is undefined for such a vector, so there is no normative answer to compare
against. Collateral: `MISSING_CONTENT` is a named refusal class whose reachability is
embodiment-determined and which **no FT row exercises**.

**Falsified by:** any clause fixing the presence predicate. None exists.

### CR3-08 — the reference anchor has a singleton quantifier domain; the barrier is never exercised against the reference — **MATERIAL**

**Clauses:** SP-091, SP-094, SP-152, §15, §0.4.

L1-85 states Pass as a three-way equality **anchored on a Reference trace**. SP-091 carries the
anchor "for every required vector" — but §15 states *"The candidate contains no … RequiredVectors"*,
and the only required vector defined anywhere is SP-094's, which mandates *"every element disposed
`ADMITTED`"*. Therefore:

- On the one reference-anchored vector, **no non-`ADMITTED` disposition can lawfully appear** — the
  Repair-1 barrier is never exercised there.
- On every other presented sequence the only applicable check is **SP-152**, a two-embodiment
  mutual-agreement predicate stated as "conform **only if**" — a necessary condition with no
  reference anchor and no sufficiency.
- FT rows cannot close the gap: §0.4 says *"FT rows are derived witnesses adding no law."*

**Consequence: nothing requires a disposition to be veridical.** A fully capable embodiment may
dispose any element `CAPABILITY_UNSUPPORTED`; paired with a genuinely limited one doing the same,
SP-152 is satisfied and SP-091 is not engaged. The comparison detects **divergence between
embodiments**; it never compares a record against the substrate's actual capability.

**Falsified by:** a required vector other than SP-094's, or a clause enumerating the required-vector
set, or a veridicality obligation.

### CR3-09 — SP-041's `EXACT` covers a transition mapping L1 never wrote — **MATERIAL**

**Clause:** SP-041 · **Controlling bytes:** L1-59:46–49, L1-72:49–52 (byte-identical four-line blocks):

```
idle → active → complete
begin
record
complete
```

That is all L1 contains. Two facts follow. **L1 supplies no operation→edge mapping** — the chain and
the operation list are separate, unlabelled registers. And **`active —record→ active` is not an edge
in L1's chain at all**; L1's chain has two arrows, and the record self-loop appears nowhere in any
pin. SP-041 asserts all three as *"the founder-sealed transitions."*

The inference is defensible under an entailment reading (L1-72's trace reaching `state = complete`
with `illegal_transition_count = 0` requires record to be state-preserving if the chain is
exhaustive) — but it is derivation from an illustration the founder himself modalized as *"might
require"*, and §17.1 applies a **member-for-member** standard to SP-001 and SP-092. Applied
consistently, SP-041's arrows are candidate members with no source member. §17.1 audits only the
fourth-*operation* widening. The document demonstrably knows the correct move: SP-048 declares the
fourth-operation closure *"an authored minimality choice, not a founder-sealed prohibition."* The
identical reasoning applies to the within-three-operation closure and was not applied.

Downstream, **SP-161 rests the entire SP-160 precedence justification** on *"the invalid-transition
law is founder-sealed at P-L1-A."* The law's **existence** is sealed (L1-59:50 "+ invalid transition
law"); its **edge content** is authored. The precedence rule stands on its own merits; its stated
justification is stronger than the bytes support.

**Falsified by:** L1 text assigning an operation to an edge, or containing a record self-loop. I
searched all three pins; neither exists.

### CR3-10 — the founder vector's sixth value is not obtainable from the instrument §11.1 cites — **MATERIAL**

§11.1's `observation` row derives *"the six SP-090 values"* from *"SP-110 `view` at final position."*
But SP-110 defines `view(n)` as a function to *"the complete **L-fact** set"*; SP-102 places
`illegal_transition_count` in the **T-fact** set; and SP-111 states `view` *"never contributes to the
illegal-transition count."* Five of the six predicates are L-facts under SP-019 and lie in `view`'s
codomain; **the sixth does not.** It is reachable only through SP-013's witness stream, which §11.1
does not invoke.

**Falsified by:** a §11.1 derivation naming SP-013, or a clause placing the count in `view`'s codomain.

### CR3-11 — constitutional law 2 has no operative surface — **MATERIAL**

L1-72:34, verbatim: *"2. Conformance vectors originate from canonical semantics, never from Web or
iOS implementations."* This is the anti-circularity law. v0.3 legislates about vectors — SP-120
declares them malformed and unrunnable, SP-094 adopts one, SP-091 quantifies over all — and carries
**no origination constraint**. `originate` occurs **0 times**. Nothing forbids a vector's input
sequence and expected values from being lifted from an implementation.

Bounding this fairly: laws 1, 4, 5, 6 and 7 concern emitters, adaptation and promotion, which SP-002
and §15 legitimately scope outside the SemanticProgram layer. Law 3 is repaired and gated (S-07).
**Law 2 is the one omission not covered by that scoping**, because v0.3 legislates about vectors and
is silent only here.

### CR3-12 — constitutional law 5 is never engaged; degradation is unauthorized adaptation — **MATERIAL**

L1-72:37, verbatim: *"5. Adaptation is a governed act. A substrate-specific workaround requires
explicit authorization."* L1-85:51, Emitter **FORBIDDEN AUTHORITY**: *"invent capability adaptations."*

`CAPABILITY_DEGRADED` is by construction a substrate-specific adaptation. v0.3 supplies **no
authorization concept whatsoever** — verified: the only `authoriz` hits in v0.3 concern the
document's own authority limits, none concerns capability adaptation. An embodiment unilaterally
invents its own adaptation and its own loss-class label. §16.1's S-07 gate scores PASS against law 3
alone, so this is untested by the candidate's own conformance section.

### CR3-13 — SP-150's disposition domain contradicts SP-050 for boundary elements — **MATERIAL**

SP-150 makes discontinuity boundaries **elements of the presented sequence** receiving one of three
dispositions. SP-050's row states, under **Permitted degradation**: *"**None.** An L-fact survives
exactly or the restart law is violated."* SP-151 requires every non-`ADMITTED` disposition to name
*"its loss class"* — **there is no defined loss class for a boundary whose permitted degradation is
None.** SP-150 and SP-050 cannot both be satisfied on their face for a degraded boundary, and no
clause says which governs.

The substantive survival law does still bind — SP-046 and SP-084 are unconditional and do not say
"an ADMITTED restart" — so **this is not a route to silent L-fact loss.** I state that plainly.
Detection is split: a mis-disposed restart inside the founder vector is caught three ways (SP-094's
"every element disposed `ADMITTED`", FT-01, FT-10's missing-boundary-marker falsifier). **A
mis-disposed DaySlot boundary is caught by nothing** — FT-09 is the only DaySlot row and carries no
disposition falsifier.

### CR3-14 — SP-018's declared self-limit is violated by two derived tables — **MINOR**

SP-018 ends *"This clause states that literal observation **and nothing further**."* It is then cited
as evidence for propositions it disclaims: §16.1 gate S-02 lists SP-018 under the L1 surface
"idle → active → complete; begin, record, complete", and §10 cites SP-018 for "core state remains
idle / active / complete." SP-018 says nothing about the progression; SP-041 does. The row is
faithful; the misuse is in the tables.

### CR3-15 — residual `EXACT` paraphrase and two false self-audit claims — **MINOR**

- **SP-005** renames three comparanda of a four-term founder chain (L1-72:94–100
  `semantic equivalence ≠ structural equivalence ≠ visual identity ≠ binary identity`): structural
  equivalence → "matching component structure"; visual identity → "visual **similarity**"; binary
  identity → "matching binaries". §17.1 calls these *"exactly the three named identity kinds"* —
  a four-term chain miscounted, with "structural equivalence" called an identity kind.
- **SP-046** is scoped by *"a **contemplated** restart"*, a scope set by `AUTHOR-PROPOSED` SP-050 and
  SP-052. An `EXACT` row whose scope is set by authored clauses is not exact.
- **SP-092** substitutes "embodiments" for the founder's *"apps"* (L1-85:112), unreported.
- **SP-004** says *"literally and in full"* and §17.1 says *"verbatim"*: true for P-L1-A and P-L1-B
  (both quoted exactly); **false for P-L1-C**, a semicolon bullet list re-rendered as an unquoted
  comma list with an added article. All seven members present, so CR-08 is still CLOSED.
- Consequently **§17.2 is false as written**: *"Against SP-005, SP-018, SP-046, and SP-092 all nine
  attacks were attempted and none succeeded."*

### CR3-16 — a tenth `EXACT` judgment lies outside both audits — **MINOR**

The §10 reconciliation table carries an `L1 relation` column, and one row reads
`| Ledger · Ritual | program container and Ritual-under-test | EXACT | SP-001, SP-017 |`. The
auditor's `^\| (SP-\d{3}) ` regex structurally cannot see it, and §17.1 is titled *"Re-audit of
**every** `EXACT` claim"* while auditing nine. Substantively the row is also not exact: L1-59:43–45
names "Durable Daily Ritual Ledger / Ritual / Entry" as co-members of one list and never says the
Ledger is a "program container" or the Ritual "under test"; one of its two governing clauses
(SP-017) is itself `AUTHOR-PROPOSED / ELABORATES`.

### CR3-17 — §16.5's evidence block was hand-edited after generation — **MINOR**

§16.5 states *"Produced by running the §16.4 script against this file. **Not hand-entered**, not
reconciled against prose."* I extracted the §16.4 source byte-exact and ran it. **The values are
confirmed genuine — all 17 metrics identical.** But the block is **22 lines and the program emits
17**: `LP_DIST`, `EXACT_ROWS`, `ORTHOGONAL_ROWS` and `ONTOLOGY_ROWS` have been hand-rewrapped with
manual continuation indentation. A reviewer who does the literal thing §16.5 invites — `diff` the
run against the block — gets a mismatch. §0.5 records Repair 6's mode as **IMPOSSIBLE**; the block
demonstrably still passes through a manual editing step.

### CR3-18 — FT-11 names the confirmation boundary; it does not exercise it — **MATERIAL**

FT-11 is the designated §6.11 authority-boundary row and the sole coverage claimed for
SP-R02-GAP-01. I tested each of its four falsifiers for discriminating power over the existing suite:

| FT-11 falsifier | Test result |
|---|---|
| "completion withheld pending a confirmation act" | Already impossible under SP-034's biconditional (*"succeeds **when and only when** current state is active and at least one pending contribution exists"*) and already falsified by FT-01's "state other than complete". **Duplicate.** |
| "a distinct confirmed/unconfirmed surface exposed on state or Entry" | An extra field lies outside SP-019's **complete** L-fact set, which SP-110 projects — already nonconforming at clause level, and by the very argument §13.1 uses to make A-01's alternatives inadmissible. **Adds a designated trace for an existing clause prohibition; this is FT-11's only non-duplicative content.** |
| "Entry status complete **presented as evidence** the external act occurred" | **Not evaluable by the witness at all.** SP-114 bounds the witness's domain to *"`view(n)` and the T-fact stream"*; SP-013 the same. "Presented as evidence" is neither an L-fact nor a T-fact, and SP-002 excludes presentation from the program's meaning. **No conformance run can fail on it.** |
| "a confirming role required to exist for the trace to succeed" | FT-01's falsifying column already reads *"any need for a capability, role, or adjudication input"*, and SP-039 forbids it normatively. **Verbatim duplicate.** |

**The input is also non-contrastive.** FT-11's qualifier *"presented with no confirming actor,
authority, or external attestation anywhere in the sequence"* cannot be varied: the presented-sequence
grammar (SP-150 — invocations and discontinuity boundaries, over SP-041/SP-048's closed three-operation
set) has no way to present a confirming actor. There is no complementary vector. FT-11's input differs
from FT-01's only by the content string and the absence of `restart`.

**Pass-while-broken construction.** Embodiment X implements v0.3's semantics exactly and publishes, in
its contract and interface, that `status = complete` certifies the practice occurred in the world.
`view(n)` identical, T-fact stream identical, every element `ADMITTED`. X passes falsifiers 1, 2 and 4,
and falsifier 3 is outside the witness's observable domain. **X passes FT-11 while violating SP-003 —
the exact clause FT-11 names as its basis.**

FT-11 also never observes the pending state between `record` and `complete`, so it does not exercise
SP-064, its other cited basis, and commission §6.8's "recorded intent distinguishable from accepted
fact" question remains untested. §14's Q14 cites FT-11 for "required unconfirmed intent"; that
citation is not supported by the row's content.

**Falsifier for this finding:** exhibit one embodiment that passes FT-01…FT-10 and FT-12 but fails
FT-11. I attempted a construction across all four falsifiers and could not produce one.

### CR3-19 — the founder exclusion register is entirely inert — **MINOR**

There is **no clause of the form "an embodiment containing X is nonconforming"** for any X in any of
the three pins. SP-004 is grammatically reportorial and nothing consumes its output; SP-002 runs the
other way, placing mechanisms outside the program's *meaning* rather than prohibiting them; the
auditor's `REPTERMS` scan contains no AI term. §16.1 gate S-06 records *"founder exclusions … PASS"*
without saying whether it means **reproduced** or **enforced**; it is defensible only under the
former. Non-enforcement at the SemanticProgram layer is defensible by design (§15 forbids
implementation content), which is why this is MINOR — but it is also **why A-08 is open** (§5.3),
and the docket does not disclose that.

### 2.20 Attacks that FAILED — reported as failures

Recorded so the founder can see what was tested and held.

| Attack | Result |
|---|---|
| Second SP-160 collision — full 18-cell Cartesian, enumerated twice independently | **FAILED.** 18/18 EXACTLY_ONE. §5.2. |
| Silent omission of `record("B")` from the presented sequence | **FAILED.** SP-150 totality + SP-154 nonconformance + SP-038 + revised SP-055 all block it. |
| Normalizing the disposition *value* away | **FAILED.** SP-093 forbids erasing distinctions needed to evaluate SP-091, which routes to SP-152. |
| Transition law reading a disposition to alter behaviour | **FAILED.** SP-105 forbids any transition evaluation reading a T-fact. |
| Two normalizations diverging on the compared surface | **FAILED.** SP-093's "may not erase any distinction needed to evaluate SP-090 through SP-092" blocks the lexical-sort construction I attempted. *(A finding to this effect was raised in my fan-out and killed here.)* |
| `entries[0].status = complete` strained or unentailed | **FAILED.** Entailed twice over, by SP-020 and SP-034, independently of A-02's open relation. |
| A-08 silently resolved by an operative clause | **FAILED.** §5.3. |
| Restart or DaySlot boundary producing a second SP-160-style collision in §6 | **FAILED.** SP-051 and SP-053 are total over all three states; SP-075 agrees on active-carry. |
| Auditor hard-coding an expected value so it passes regardless of content | **FAILED.** No numeric constants; every mutation that touched a metric moved that metric. |
| Duplicate SP-ID evading the auditor | **FAILED.** Genuinely caught (§6.4 PROBE-6). |
| **T→L breach: dispositions are T-facts (SP-102), so a T-fact determines which L-facts exist, breaking the partition's one-way direction** | **FAILED — and I record it because it is the most tempting wrong finding in this area.** A fan-out line proposed it as BLOCKING; I rejected it. Capability resolution is the **common cause** of both the L-fact outcome and the disposition T-fact; the T-fact is the *record* of the decision, not its input. No transition evaluation reads it, so SP-105 holds and the partition's one-way direction survives. What is true is weaker and already recorded as CR3-02: the T-fact stream is no longer a **pure function of the presented sequence**. The genuine residue in SP-153's wording is at §5.1.1, MINOR. |

---

## 3. LAYER 3 — COUNTEREXAMPLE CONSTRUCTION

### 3.1 The exact sequence that broke v0.2

Presented sequence **P = ⟨ begin, record("A"), record("B"), complete ⟩** (SP-150: RC-0001's
conformance input). Initial state idle, pending 0, durable history empty.

**Embodiment W** — unbounded pending contributions.
**Embodiment I** — substrate supports at most one pending contribution per active interval.

| # | Presented element | W disposition | W result (SP-160) | W L-facts after | I disposition | I result | I L-facts after |
|---|---|---|---|---|---|---|---|
| 1 | `begin` | `ADMITTED` | step 3 accepted (SP-030) | active, pending `[]` | `ADMITTED` | accepted | active, pending `[]` |
| 2 | `record("A")` | `ADMITTED` | step 3 accepted (SP-032) | active, pending `[A]` | `ADMITTED` | accepted | active, pending `[A]` |
| **3** | **`record("B")`** | **`ADMITTED`** | step 3 accepted | active, pending `[A,B]` | **`CAPABILITY_UNSUPPORTED`** | **no result — never reaches transition law (SP-153)** | active, pending `[A]` |
| 4 | `complete` | `ADMITTED` | step 3 accepted (SP-034) | complete, entries `[A,B]` | `ADMITTED` | accepted | complete, entries `[A]` |

Compared disposition vectors: **⟨A, A, A, A⟩ vs ⟨A, A, CAPABILITY_UNSUPPORTED, A⟩.**

### 3.2 Divergence detection — the required test

SP-152: *"Two embodiments conform only if **every presented element receives the same disposition**
and every `ADMITTED` element produces the same outcome."*

**Divergence is detected at element 3 — the disposition for `record("B")` — and it is detected there
before any Entry-count difference arises at element 4.** The repair does what §2.0 claims.

### 3.3 The three mandated failure modes, each attacked

| Failure mode | Result | Blocking clause, quoted |
|---|---|---|
| **(a) silently omit that element** | **IMPOSSIBLE** | SP-150: *"The disposition function is total: **no presented element may be absent from the record**."* SP-154: *"An embodiment that silently narrows the presented sequence **fails RC-0001 regardless of the ledger state it reaches**."* SP-038: *"Every capability-disposed element is distinguishable from an absent element by its disposition T-fact."* |
| **— via v0.2's escape route** (claim it was "never presented") | **CLOSED** | SP-055 as revised: *"An invocation presented but capability-disposed is accounted for under SP-150 and is **not 'absent.'**"* The presented sequence is the conformance input (SP-150), so an embodiment cannot redefine what was presented. |
| **(b) normalize the dispositions away** | **IMPOSSIBLE for the disposition value** | SP-093: normalization *"may not erase any distinction needed to evaluate SP-090 through SP-092."* SP-091 routes to SP-152, which compares dispositions. *Bound: the block runs through SP-091's **authored** second sentence — see CR3-01.* **NOT blocked for the `loss class`** — §3.5. |
| **(c) still produce an equivalent conformance record** | **IMPOSSIBLE via `CAPABILITY_UNSUPPORTED`** | The disposition record is a T-fact (SP-102); SP-013 requires the witness to observe *"the complete T-fact stream **including dispositions**"*; SP-114 compares that stream across substrates. |

Further escapes attempted and blocked: dispose `ADMITTED` then refuse (SP-160 yields accepted for
active + content; a rejection diverges under SP-152's second conjunct); admit but drop the Entry at
`complete` (SP-034 violated, `view(n)` divergence under SP-114); read the disposition in the
transition law (SP-105).

**LAYER 3 CORE RESULT: v0.3 SURVIVES.** I could not construct a conforming implementation that
silently omits `record("B")`, normalizes its disposition away, or produces an equivalent
conformance record. **CR-002 B.1-F1 is CLOSED.**

### 3.4 Residual bounds on that survival

Two, both recorded above and neither reopening the leak:

- **CR3-08** — the barrier is exercised only by SP-152 (embodiment-to-embodiment). SP-091's
  reference anchor quantifies over a required-vector set of size one, on which SP-094 mandates every
  element `ADMITTED`, so the barrier never engages against the reference. Nothing requires a
  disposition to be **veridical**.
- **CR3-06** — position alignment between W and I is undetermined, so the *position-indexed* witness
  surface (SP-013, SP-110) misaligns even though the *element-keyed* SP-152 comparison does not.

### 3.5 The separate `CAPABILITY_DEGRADED` attack

**Construction.** Same presented sequence P. Both embodiments pass the SP-094 founder vector with
every element `ADMITTED`.

- **G′** — cannot hold a second pending contribution. Disposes `record("B")` `CAPABILITY_DEGRADED`,
  loss class `CAPACITY_EXCEEDED`.
- **H′** — *can* hold two contributions but **cannot preserve their canonical order**, so it declines
  rather than reorder. Disposes `record("B")` `CAPABILITY_DEGRADED`, loss class
  `ORDER_NOT_PRESERVABLE`.

| # | Presented | G′ disp / loss class | H′ disp / loss class | Same? |
|---|---|---|---|---|
| 1 | `begin` | `ADMITTED` | `ADMITTED` | ✓ |
| 2 | `record("A")` | `ADMITTED` | `ADMITTED` | ✓ |
| 3 | `record("B")` | `CAPABILITY_DEGRADED` / `CAPACITY_EXCEEDED` | `CAPABILITY_DEGRADED` / `ORDER_NOT_PRESERVABLE` | **disposition ✓ · loss class ✗** |
| 4 | `complete` | `ADMITTED` → entries `[A]` | `ADMITTED` → entries `[A]` | ✓ |

**Clause-by-clause conformance check for the G′/H′ pair:**

| Clause | Violated? | Why not |
|---|---|---|
| SP-150 | No | every element has exactly one disposition |
| SP-151 | No | each non-`ADMITTED` disposition is a typed T-fact with a loss class |
| SP-152 | **No** | *"the same disposition"* — both `CAPABILITY_DEGRADED`; every `ADMITTED` element's outcome identical |
| SP-153 | No | no legality decision, no L-fact write, no Participant permission |
| SP-154 | No | nothing removed without a typed disposition |
| SP-131 | No | comparand is *"the one this SemanticProgram assigns it"* — none is assigned |
| SP-093 | No | expressly permits erasing distinctions not needed for SP-090–SP-092; the loss class is not |
| SP-091 / SP-092 | No | not engaged — §15 declares no `RequiredVectors`; the sole vector is SP-094's, all-`ADMITTED` |
| SP-038 | No | requires distinguishing disposed from **absent**, not one loss class from another |
| FT-12 | n/a | §0.4: FT rows add no law; and its falsifier (`[A]` and `[A,B]` both conforming) does not fire — both report `[A]` |

**Result — two readings, and both are defects:**

1. **The typing is decorative.** H′'s loss is **canonical ordering** — a member of P-L1-A's sealed
   scope list and a named axis on P-L1-C's Fail list. That loss is invisible in the compared record
   because it was expressed as a generic token. L1-72 law 3 requires capability loss to be *"typed
   and explicit"*; v0.3 achieves explicit and stops short of typed.
2. **The label is unassignable.** No clause distinguishes `CAPABILITY_DEGRADED` from
   `CAPABILITY_UNSUPPORTED`, and SP-153 makes them operationally identical. So SP-152 can also fire
   *falsely*: two embodiments with identical behaviour, one typing `DEGRADED` and the other
   `UNSUPPORTED`, are declared nonconforming with no clause saying which was wrong.

**Severity adjudication — I downgraded this from BLOCKING.** G′ and H′ are observably identical at
every position; no divergent semantics escapes the compared surface, so there is no leak. It is
`MATERIAL`. But the PASS-threshold line *"degraded capability ambiguity | absent"* fails on it
regardless of severity: the term has two occurrences, no definition, no assignment rule, and no
trace coverage.

---

## 4. LAYER 4 — FOUNDER-DECISION INTEGRITY

### 4.1 v0.3's own rule, stated as a decision procedure

> **Sharpened test.** An alternative is **admissible** only if it is realizable as observable
> semantics under the current L-fact set. An alternative that asserts a semantic fact the program
> does not carry is not a conforming implementation choice — it is a request to change SP-019.
>
> **T(A):** Considering only admissible alternatives, can two embodiments adopting different ones
> both satisfy every normative SP clause?
> `YES for all` → OPEN · `YES for some` → PARTIALLY_DECIDED · `NO for all but one` → OPERATIVELY_DECIDED

**INPUTS** the alternative set Alt(A); SP-019's L-fact set; the normative SP clause set.
**STAGE 1** filter Alt(A) → Adm(A). **STAGE 2** evaluate T(A) over Adm(A). **STAGE 3** map to a class.

**Two defects in the rule itself:**

- **(a) The output mapping is non-exclusive — and the repair caused it.** v0.2 read
  `YES for some, **NO for others** → PARTIALLY_DECIDED (list which are excluded)`. v0.3 deleted
  "NO for others". "YES for all" now also satisfies "YES for some", so **OPEN and PARTIALLY_DECIDED
  overlap.** The edit that was meant to sharpen the classifier blunted its output mapping.
- **(b) The criterion has two readings.** *"realizable as observable semantics"* is an observability
  test; *"asserts a semantic fact the program does not carry"* is an assertion test. They differ for
  any alternative positing an internal fact it never exposes in `view(n)`. I adopt the unified
  assertion reading below as the more natural one, and note that under the observability reading
  A-01 and A-04 would both flip to OPEN.

### 4.2 My independent classification versus the candidate's

Derived by applying the rule from the alternative sets before reading §13.1's cells.

| Item | Question | My classification | Candidate | Divergence |
|---|---|---|---|---|
| A-01 | Which entity owns observable state? | `OPERATIVELY_DECIDED` (D) | `OPERATIVELY_DECIDED` | — |
| A-02 | Relation between invoking `complete` and observing state complete | `OPEN` | `OPEN` | — |
| **A-03** | Does `record` create an Entry, mutate one, or create a non-Entry contribution? | **`OPEN`** | `PARTIALLY_DECIDED` | **DIVERGES** |
| A-04 | What maps a logical DaySlot to a civil day? | `OPERATIVELY_DECIDED` (A) | `OPERATIVELY_DECIDED` | — |
| A-05 | Does RC-0001 need a world-fact/authority layer? | `OPERATIVELY_DECIDED` (A) | `OPERATIVELY_DECIDED` | — |
| A-06 | Can completed Entry meaning later be corrected? | `OPERATIVELY_DECIDED` (A) | `OPERATIVELY_DECIDED` | — |
| A-07 | Invocation-capability precondition, and capability-loss accounting | `OPERATIVELY_DECIDED` (a) | `OPERATIVELY_DECIDED` | — (part 2 caveat below) |
| A-08 | "no AI" vs "No generative AI" | `OPEN` | `OPEN` | — |

**My tally: 3 OPEN · 0 PARTIALLY_DECIDED · 5 OPERATIVELY_DECIDED.**
**Candidate's claim: `2 OPEN / 1 PARTIALLY_DECIDED / 5 OPERATIVELY_DECIDED`.**

**The mandate's question — is `2 / 1 / 5` entailed by the normative clauses? NO.**

Arithmetic note: the eight §13.1 rows *do* sum to the summary line, and the auditor's
`DOCKET_ITEMS 8` is correct. The defect is in one label, not in the addition.

### 4.3 The A-03 divergence, shown

Rule application, step by step:

1. **Adm(A-03) = {A, B}.** §13.1 itself filters C: *"C inadmissible — SP-022 requires the
   contribution be *created*, excluding a pre-existing Entry mutated by `record`."* I verified SP-022
   and agree.
2. **T(A-03) over Adm(A-03).** SP-026, a normative clause, states: *"Both models are **normatively
   admitted**; see SP-140."* SP-140 voids any FT row that discriminates them. So two embodiments
   adopting A and B respectively **both satisfy every normative SP clause**.
3. **T is YES for every member of Adm(A-03)** → the rule's first branch, `YES for all` → **OPEN.**

`PARTIALLY_DECIDED` is reachable only under **v0.2's superseded rule**, where all listed
alternatives stayed in T(A)'s domain and C returned NO. **The label survived the repair; the rule
that generated it did not.** §13.1's own "Installed branch" cell for A-03 reads *"none between A and
B"* — which is what OPEN describes.

This is CR-002 B.3-F5's defect class — a label inconsistent with the document's own test — surviving
in a different row, which is itself the pattern §4.0 says SP-160 was written to abolish.

### 4.4 Reverse check — do the cited clauses entail the five `OPERATIVELY_DECIDED` verdicts?

Each cited clause read in full and tested. **All five hold; no reverse defect.**

- **A-01** — SP-019 self-describes as *"The **complete** L-fact set"* and carries no owner coordinate. Entails.
- **A-04** — SP-019 carries no timezone or participant-day fact; SP-070 independently closes the ordering-fact list to three. Entails.
- **A-05** — SP-029 is an **existence** prohibition (*"No confirmer, amender, invalidator, Reporter, Assertion, Adjudicator, Adjudication, or Establishment construct exists"*), strong enough to exclude even a non-gating layer. Entails.
- **A-06** — SP-048 excludes both a correction transition and a fourth operation. Entails; SP-025 alone would not have, and SP-048 is correctly cited.
- **A-07 part 1** — SP-130 (*"admits **no invocation-capability precondition**"*) and SP-131. Entails.

**A-07 caveat (MINOR).** §13.1 reframes A-07 into two questions — *"is there a gate, **and how is
capability loss accounted for**"* — but the admissible-alternatives cell enumerates only the gate
alternatives (a)/(b)/(c). **No alternative accounting scheme is enumerated anywhere in the corpus**,
yet §13.2 records an installed answer ("total typed accounting"). A founder cannot decide against
unenumerated alternatives.

**A-02 justification (MINOR).** §13.1 asserts *"A, B, C all admissible."* Under the assertion
reading, alternative C (distinct completion scopes) asserts a scope-identity fact SP-019 does not
carry and is inadmissible. `OPEN` still follows from {A, B}, so the **label is right and the
justification is wrong** — the same shape as the A-01 note CR-002 caught, one row over.

**A-08 alternative set (MINOR).** §13.2's alternative (c) *"both stand and the **intersection**
governs"* is extensionally identical to (a): the intersection of {all AI} and {generative AI} is
{generative AI}. Three alternatives, two extents.

---

## 5. THE THREE ELEVATED ATTACKS

### 5.1 Capability disposition must not become permission by another route

| # | §5.1 prohibition | Verdict | Mechanism |
|---|---|---|---|
| 1 | Alter the transition law for an admitted operation | **BLOCKED** | SP-105: *"No transition evaluation may read a T-fact."* + SP-102 makes dispositions T-facts + SP-160 determines results from state and content alone. A real mechanism. |
| 2 | Mutate L-facts | **BLOCKED for direct writes; SP-153's wording overstates** | See 5.1.1. |
| 3 | Grant a Participant permission | **Forbidden in law; unenforceable from the compared record** | See 5.1.2. |
| 4 | Silently delete a presented element | **BLOCKED** | SP-150 totality + SP-151 *"never silent"* + SP-154 nonconformance + SP-038 + revised SP-055. The strongest part of the repair. |
| 5 | Disappear before comparison | **BLOCKED for the disposition value; NOT blocked for the loss class** | Value: SP-102 → SP-013 → SP-114 → SP-152, with SP-093 forbidding erasure. Loss class: SP-093 permits it (§3.5). |
| 6 | Identical presented sequences with different dispositions not proof-visible as different | **HOLDS — v0.3 survives** | SP-152, §3.2. |

**5.1.1 (MINOR).** SP-153's *"never alters an L-fact"* is true only *de dicto*. Presented
`begin; record("A"); complete`: an embodiment disposing element 2 `CAPABILITY_UNSUPPORTED` reaches
element 3 with pending empty, so SP-160 step 2 yields `NO_RECORDED_CONTENT` instead of acceptance,
and the final L-fact set is `{active, []}` rather than `{complete, [A]}`. The **disposition changed
the L-fact outcome** without writing an L-fact. SP-152 catches the divergence at elements 2 and 3, so
this is not a leak — but the blanket phrasing is quotable later to argue degradation is
L-fact-neutral, which §3.5 shows it is not.

**5.1.2 (MATERIAL).** SP-010 makes a Participant *"a logical principal **presented to** the
SemanticProgram"*, so the disposition function's domain includes it. A Participant-keyed resolver
("this substrate supports only principal P1") is forbidden by SP-153's text, but nothing in the
disposition machinery excludes it and **SP-151 does not require the loss class to disclose the
ground of the loss.** From the compared record, `CAPABILITY_UNSUPPORTED(record)` is indistinguishable
from a capacity limit. Detection would additionally require a vector varying Participant; SP-094's
vector has no Participant term and §15 declares no `RequiredVectors` exist. **The invariant rests on
prose plus a vector nobody is obliged to run.**

**5.1.3** — the `CAPABILITY_DEGRADED` enumeration is at §3.5; the finding is CR3-04.

### 5.2 SP-160 must be TOTAL, not merely prioritized — the Cartesian enumeration

**Domains derived from v0.3's own text.** States `S = {idle, active, complete}` (SP-040, SP-041).
Operations `O = {begin, record, complete}` (SP-030/032/034; SP-048 closes any fourth). Content
condition `CC = {SAT, UNSAT}`, instantiated per operation by SP-160 step 2 itself — for `record`,
content present / absent; for `complete`, pending ≥ 1 / pending = 0; for `begin`, **vacuous**
(SP-031: *"begin has no content condition"*). **|S| × |O| × |CC| = 3 × 3 × 2 = 18 cells.**

| # | state | op | CC | state-legal? | SP-160 path | normative result | verdict |
|---|---|---|---|---|---|---|---|
| C01 | idle | begin | vac | ✓ | step 3 | ACCEPTED | EXACTLY_ONE |
| C02 | idle | begin | vac | ✓ | step 3 | ACCEPTED | EXACTLY_ONE (degenerate ≡C01) |
| C03 | idle | record | present | ✗ | step 1 | INVALID_TRANSITION | EXACTLY_ONE |
| C04 | idle | record | absent | ✗ | step 1, **stops** | INVALID_TRANSITION | EXACTLY_ONE (overlap resolved) |
| C05 | idle | complete | pending≥1 | ✗ | step 1 | INVALID_TRANSITION | EXACTLY_ONE (**unreachable**) |
| **C06** | **idle** | **complete** | **pending=0** | ✗ | step 1, **stops** | **INVALID_TRANSITION** | **EXACTLY_ONE — the v0.2 collision, closed** |
| C07 | active | begin | vac | ✗ | step 1 | INVALID_TRANSITION | EXACTLY_ONE |
| C08 | active | begin | vac | ✗ | step 1 | INVALID_TRANSITION | EXACTLY_ONE (degenerate ≡C07) |
| C09 | active | record | present | ✓ | step 2 pass → 3 | ACCEPTED | EXACTLY_ONE |
| C10 | active | record | absent | ✓ | step 2 | MISSING_CONTENT | EXACTLY_ONE *(cell membership undefined — CR3-07)* |
| C11 | active | complete | pending≥1 | ✓ | step 3 | ACCEPTED | EXACTLY_ONE |
| C12 | active | complete | pending=0 | ✓ | step 2 | NO_RECORDED_CONTENT | EXACTLY_ONE |
| C13 | complete | begin | vac | ✗ | step 1 | INVALID_TRANSITION | EXACTLY_ONE |
| C14 | complete | begin | vac | ✗ | step 1 | INVALID_TRANSITION | EXACTLY_ONE (degenerate ≡C13) |
| C15 | complete | record | present | ✗ | step 1 | INVALID_TRANSITION | EXACTLY_ONE |
| C16 | complete | record | absent | ✗ | step 1, **stops** | INVALID_TRANSITION | EXACTLY_ONE (overlap resolved) |
| C17 | complete | complete | pending≥1 | ✗ | step 1 | INVALID_TRANSITION | EXACTLY_ONE (**unreachable**) |
| C18 | complete | complete | pending=0 | ✗ | step 1, **stops** | INVALID_TRANSITION | EXACTLY_ONE (FT-08 trace B) |

```
TOTAL CELLS   18      EXACTLY_ONE  18      ZERO  0      MULTIPLE  0
OVERLAP CELLS  4  (C04, C06, C16, C18) — all resolved by step 1's "and evaluation stops"
DEGENERATE     3  (begin has no content condition)      UNREACHABLE  2  (C05, C17)
```

**Unreachability proof for C05/C17** (`pending > 0 ⇒ state = active`): SP-040 initializes pending
to zero; pending is created only by a successful `record`, which requires and preserves `active`
(SP-032); pending is cleared by a successful `complete` (SP-034); no transition returns
`active → idle` (SP-041 lists none; SP-050/SP-051 preserve current state exactly; SP-053 maps
*"active remains active"*); and idle is entered only initially or from `complete`, where pending is
already zero, with SP-042 making complete terminal within the DaySlot. Unreachability is not
load-bearing — both cells are EXACTLY_ONE anyway.

**RESULT: SP-160's precedence is TOTAL and UNAMBIGUOUS over the three state-changing operations.**
No ZERO cell (step 3 is an unconditional catch-all). No MULTIPLE cell (the only structural overlap
is *state-illegal ∧ content-UNSAT*, and step 1's hard cut makes step 2 unreachable in all four).
SP-033 and SP-035 independently restate the same precedence, so there is no clause-vs-clause
disagreement. **I found no second collision. There is none in this product**, and I ran the
enumeration twice by independent routes to be sure.

**Refusal reason is deterministic in kind and observable** across all 13 distinct reachable cells:
the reason is a field of the outcome (SP-031/033/035), outcomes are T-facts (SP-102), the witness
observes the complete stream (SP-013). **B-F3 is closed at the precedence level.**

**Where SP-160 nonetheless fails the mandate's standard.** *"Every admitted operation over every
admitted pre-state has exactly one normative result"* fails not in the precedence but in the
**domain map for the CC dimension** — the predicate deciding which cell a concrete element occupies
(CR3-07) — and downstream of step 1 in the unscoped counter (CR3-B01). Both are mechanism defects
demonstrable with traces in which no clause is violated.

**Boundaries.** SP-160 correctly scopes itself to invocations; restart and DaySlot boundaries are
governed totally by SP-051 and SP-053 with no collision. The residual defect there is CR3-13.

### 5.3 A-08 must not be author resolution of founder inconsistency

**Both strings verified byte-exact against raw L1**, not against the candidate's or custody's quotation:

- **L1-59:41** — `No auth, no cloud, no camera, no AI, no networking`
- **L1-72:64** — `No cloud. No authentication. No generative AI. No camera. No networking. No seductive product surface hiding compiler defects.`

The registered extent difference is real and correctly stated.

**The real test — does any operative clause behave as though one interpretation already governs?**
I searched the whole document for `AI`, `generative`, `artificial`, `machine learning`, and every
other exclusion-register member (`cloud`, `network`, `camera`, `auth`), and read §2, §5, §11, §14 and
§15 in full. **Every hit on AI is either SP-004 itself or a docket/review row about A-08.** No clause
permits non-generative AI. No clause forbids all AI. No clause scopes any prohibition in a way that
makes sense under only one reading. The new clauses SP-094, SP-105, SP-150–SP-154, SP-160, SP-161 and
the new traces FT-11, FT-12 were each checked individually; none discriminates A-08.

**FINDING: A-08's `OPEN` label is CORRECT and A-08 is not silently resolved.** I state that plainly
and did not manufacture a defect here.

**But — as the mandate requires me to say explicitly — preserving both strings is not what makes
A-08 open, and the docket does not disclose the real reason.** A-08 is open **by inertness**: there
is no clause of the form "an embodiment containing X is nonconforming" for *any* founder exclusion
(CR3-19). §13.1's *"no normative clause depends on the difference"* is true because **no clause
depends on the exclusion register at all.** A-08 would therefore remain "open" no matter how
carelessly it were handled, and the first clause that tried to enforce an exclusion would force the
question immediately.

One sub-observation, expressly **not** a resolution: SP-004's lead-in *"are, literally and in full:"*
ranges over all three registers conjunctively, which leans extensionally toward alternative (b) — the
union. The per-pin attribution holds them apart and no clause reads the set, so no operative
consequence follows. This is the closest the document comes to leaning, and it leans **against** the
narrower phrasing used elsewhere in the author's prose. The `OPEN` label stands.

---

## 6. THE EMBEDDED MECHANICAL AUDITOR — HOSTILE TREATMENT

### 6.1 Independent run and byte comparison against §16.5

I extracted the §16.4 source byte-exact from the fence (lines 542–592) and ran
`python3 <script> <v0.3>`. **All 17 metric values reproduce §16.5 exactly.** The block is
**not byte-identical**: it is 22 lines to the program's 17, with `LP_DIST`, `EXACT_ROWS`,
`ORTHOGONAL_ROWS` and `ONTOLOGY_ROWS` hand-rewrapped. Equal after whitespace normalization; zero
value divergence. **§16.5's figures are CONFIRMED; §16.5's "not hand-entered" is REFUTED** (CR3-17).

### 6.2 What it PROVES, what it COUNTS, what it ASSERTS

| Class | Count | Checks |
|---|---|---|
| **PROVES** | 2 | (i) **field-token arity** — each SP row carries exactly one token from each of four closed vocabularies. The only genuine structural entailment in the program. (ii) **SP-ID uniqueness** within the envelope. |
| **COUNTS** | 11 | scope split; SP-row line-shape match; `\| CONFLICTS \|` string absence; `\| UNRESOLVED \|` + `A-0N` substring co-occurrence; four label distributions; `EXACT_ROWS`; `ORTHOGONAL_ROWS`; the 16-term representation denylist; `FT_ROWS`; `Q_ROWS`; `DOCKET_ITEMS`; `TRAILING_WHITESPACE`. |
| **ASSERTS** | 2 | (i) the **ontology `PROHIBITS` verdict**, derived from the presence of the word "no" or "not" anywhere on the line. (ii) **`AUDIT_RESULT`**. |

The program reads only `sys.argv[1]`. **It cannot compare against L1, against custody, or against
any prior version.** Every `EXACT` / `ELABORATES` / `ORTHOGONAL` judgment is taken at face value from
the label the author typed.

### 6.3 What makes `AUDIT_RESULT = PASS` — from the code, not the prose

`PASS` ⟺ `viol == [] and dup == [] and rep == []`, i.e. exactly and only:

1. every SP row has arity-1 on LAYER, CP, LP, REL;
2. no SP row contains the literal `| CONFLICTS |`;
3. no `| UNRESOLVED |` row lacks an `A-0[1-9]` substring **anywhere on the line**;
4. no SP-ID repeats within the envelope;
5. no SP row contains any of 16 hard-coded representation terms.

**All five are absence predicates. There is no positive requirement whatsoever** — no minimum row
count, no FT coverage, no docket count, no `EXACT`/§17.1 agreement. **11 of the 17 emitted metrics
are reported but ungated.**

### 6.4 Semantic defects that pass while `AUDIT_RESULT = PASS` — probes I ran myself

All probes were run on scratch copies under the job tmp dir. **v0.3 was never modified.**

| Probe | Construction | Result |
|---|---|---|
| **PROBE-1** | Invert SP-041's transition law entirely ("complete —begin→ idle … Every transition of begin, record, or complete is lawful from every state"), negate SP-160's determinism clause ("may yield any number of results, chosen by the embodiment"), and gut FT-12 to `none \| none \| none \| none`. Metadata fields untouched. | **PASS, every metric unchanged** |
| **PROBE-5** | Append `\| SP-999 \| An embodiment may silently discard any presented element. \| L1 \| FOUNDER-DIRECTED \| FOUNDER_SEALED_L1 \| EXACT \| P-L1-A \| — \|` **after** the `## 17.` boundary | **PASS**, `EXACT_ROWS` still 9 — the row is invisible |
| **PROBE-A9** | Insert a clause that **installs** the prohibited ontology: *"An **Adjudicator** construct is admitted: a Participant may raise an **Assertion** and the ledger **adjudicates** it as a **contested** world-fact. This is **not** optional."* | **PASS**, `ONTOLOGY_ROWS 6→7` with the new row classified **`PROHIBITS`** — because it contains the word "not" |
| **PROBE-A5** | Insert a second `## 17. Provenance entailment (forward reference)` heading after §6 | **PASS**, envelope truncated: rows 90→62, `FT_ROWS 12→0`, `Q_ROWS 16→0`, `DOCKET_ITEMS 8→0`, `EXACT 9→6` |
| **PROBE-A3** | Relabel one row's relation from `ORTHOGONAL` to the honest `CONFLICTS`, content unchanged | **FAIL** — `SHAPE_VIOLATIONS [('SP-010','ADOPTED_CONFLICTS',1)]`. **The gate punishes candour: concealment passes, disclosure fails.** |
| **PROBE-A2** | An **empty file** | **PASS** |
| **PROBE-A2b** | **v0.2** — the document CR-002 found six confirmed defects in | **PASS** |
| **PROBE-6** (control) | Duplicate an SP-ID | **FAIL** — genuinely caught. The auditor is sound here. |

Further blind spots confirmed by the fan-out and consistent with my probes: a row-shaped line placed
**inside the auditor's own code fence** is ingested as a normative founder-sealed clause; the 16-term
`REPTERMS` denylist misses Postgres/Redis/JSON/ORM/"on disk" and scans SP rows only; renumbering a
clause while 14 others still cite it is invisible; `DOCKET_ITEMS` caps silently at A-09; adjacent
duplicate field tokens evade the arity check because `re.findall` is non-overlapping.

**§17, §18 and §19 are entirely outside the declared envelope.** The section whose own text reads
*"Every line above is an author-side claim"* is the section the auditor cannot see.

### 6.5 Bounding the v0.2 replication — the mandate's specific instruction

I ran v0.3's auditor against v0.2 myself. It reproduces `ONTOLOGY_ROWS 6` and `ORTHOGONAL_ROWS 10`
(list including SP-029 and SP-132) against v0.2's prose claims of 3 and 9, matching CR-002's
independent hand recomputation. **§16.4's validation claim is CONFIRMED in full.**

> **Precise, narrow statement of what that evidences.** Running the §16.4 program over v0.2
> reproduces exactly the structural and lexical tallies that Cold Review 002 independently
> recomputed by hand. This establishes **measurement validity for those tallies, as tallies, and
> nothing more.** It establishes nothing about whether those tallies are the right quantities,
> whether the envelope is the right scope, whether any labelled relation is true, or whether
> `AUDIT_RESULT` discriminates sound documents from unsound ones. On the direct evidence it does
> not: **v0.2 returns `AUDIT_RESULT PASS`, and so does an empty file.**

**Consequently §16.4's claim *"The auditor detects the defect it was built to prevent, on the
document that had it"* is NOT supported.** The auditor **printed two numbers**; a human compared them
to v0.2's prose and found the discrepancy. No code in the program reads any prose claim.

### 6.6 Every claim v0.3 rests on the auditor, bounded

| Claim | Status |
|---|---|
| §16.4 "regenerates every mechanical claim in this section" | **Supported** for the 17 emitted metrics only |
| §16.4 "Any figure … the script contradicts is wrong, and the script governs" | **Partially supported** — true where the script emits a figure; 11 of 17 are ungated and most figures in v0.3 lie outside its output |
| §16.5 "Produced by running the script … not hand-entered" | **Values supported; byte-identity REFUTED** (CR3-17) |
| §16.4 v0.2 validation (`ONTOLOGY 6` / `ORTHOGONAL 10`) | **Supported — independently confirmed** |
| §16.4 "detects the defect it was built to prevent" | **NOT supported** — `AUDIT_RESULT` on v0.2 is PASS; detection was human |
| §16.5 `EXACT_ROWS must equal the 9 clauses justified in §17.1` | **Left side supported; the equality NOT supported** — §17.1 is outside the envelope, so the machine cannot check it even in principle |
| §16.5 `ONTOLOGY_ROWS 6, every one classified PROHIBITS` | **Count supported; classification NOT supported** — PROBE-A9 |
| §16.5 `FT_ROWS 12 (10 + FT-11 + FT-12)` | **Count supported; decomposition NOT supported** — line-shape only |
| §16.5 `DOCKET_ITEMS 8` | **Count supported for A-01…A-09 shapes; item identity not measured; A-10+ invisible** |
| §16.5 `REPRESENTATION_HITS 0` | **Supported only for the 16 listed terms in SP rows**; prose unscanned |
| §16.5 `AUDIT_RESULT PASS` as evidence of candidate health | **NOT supported** |
| §16.5 `UNIQUE_IDS 90` / `DUPLICATE_IDS NONE` | **Supported** within the envelope; does not establish completeness |
| §16.5 `SHAPE_VIOLATIONS NONE` | **Supported**, with the adjacency hole |
| §17 "A mechanical script may audit completeness; it may never award `EXACT`" | **Correct bound, and I confirm it. Credit where due — this is v0.3 bounding its own auditor accurately, and §17.3 then departs from it for `ORTHOGONAL`** |

**A disclosure that v0.2 carried and v0.3 dropped.** v0.2's §16.4 was headed *"Metadata-shape audit —
**renamed per CR-09**"* and opened: *"**This audit proves row grammar and nothing else.** It cannot
establish source fidelity, semantic entailment, or state-machine determinacy."* v0.3 deletes the
CR-09-mandated rename and the disclaimer, substitutes *"Any figure in this document that the script
contradicts is wrong, and **the script governs**"*, and adds a global `AUDIT_RESULT` verdict token
that v0.2's block did not contain (verified: `grep -c AUDIT_RESULT` on v0.2 → 0). v0.3's only
surviving disclaimer scopes to `EXACT`. **The evidence apparatus grew a pass/fail verdict at the same
moment it lost the sentence saying what it cannot prove** — and §6.4's probes show that verdict is
`PASS` for a semantically inverted document, for a document with three metrics collapsed to zero, for
v0.2, and for an empty file.

**The defect is not that the counts are wrong. The counts are right.** The defect is the gap between
what is counted and what `AUDIT_RESULT = PASS` is presented as licensing — and §17.3's delegation of
a substantive entailment judgment to the same instrument (CR3-03). **The auditor has become a
miniature of the earlier provenance problem for `ORTHOGONAL`, while correctly avoiding it for
`EXACT`.**

Minor robustness notes: no `encoding=` on `read_text()`, so the program crashes under a non-UTF-8
locale despite the "any reviewer can run" promise; no argv guard; and `dict(Counter(...))` preserves
first-encounter order, so any byte-comparison of §16.5 is sensitive to clause **ordering**, not only
clause content.

---

## 7. PASS-THRESHOLD TABLE — DETERMINATION PER LINE

| Condition | Required | Determination | Basis |
|---|---|---|---|
| CR-001 defects | 9/9 CLOSED | **NOT MET** — 8 CLOSED, 1 PARTIALLY_CLOSED | CR-09 (§1.1) |
| CR-002 defects | all CLOSED | **NOT MET** — 11 CLOSED, 4 PARTIALLY_CLOSED, 2 NOT_CLOSED | §1.2 |
| capability silent loss | impossible | **MET** | §3.3 — SP-150/151/154/038 + revised SP-055; every escape blocked |
| capability ≠ permission | preserved | **PARTIAL → NOT MET** | Preserved in law (SP-153, SP-130, SP-131); unenforceable from the compared record (§5.1.2) |
| degraded capability ambiguity | absent | **NOT MET** | CR3-04, §3.5 — two occurrences, no definition, no assignment rule, no coverage |
| transition-result nondeterminism | absent | **NOT MET** | SP-160 itself is total (18/18, §5.2), but the step-2 antecedent predicate is undefined (CR3-07) |
| L1 contradictions | 0 | **NOT MET** | 0 by assertion; by silence in an operative surface: law 2 (CR3-11), law 5 (CR3-12) |
| EXACT overclaims | 0 | **NOT MET** | CR3-01 (SP-091), CR3-09 (SP-041), CR3-15 (SP-005, SP-046), CR3-16 (the tenth, unaudited) |
| docket classifications | accurate | **NOT MET** | A-03 (§4.3); classifier non-exclusive (§4.1) |
| A-08 silently resolved | NO | **MET** | §5.3 — verified against raw L1 and by exhaustive operative-clause search |
| FT-11 coverage | substantive | **NOT MET** | CR3-18 — three of four falsifiers duplicate existing coverage, the fourth is outside the witness's domain, and embodiment X passes FT-11 while violating SP-003 |
| SP-R02-GAP-01 | CLOSED | **NOT MET** — PARTIALLY_CLOSED | §1.2 — cause genuinely corrected; symptom nominally filled only |
| L/T non-interference | holds | **MET** | SP-105 makes the one-way direction normative; no transition evaluation reads a T-fact; verified over the six-step trace |
| founder vector | self-sufficient | **NOT MET** | **CR3-B01, BLOCKING** — the count coordinate; plus CR3-10 (the citing instrument cannot return the sixth value) |
| auditor claims | bounded to measurements | **NOT MET** | §6.6 — three claims exceed what the program measures; §17.3 delegates a substantive judgment to it |
| new blocking defects | 0 | **NOT MET** — 1 | CR3-B01 |

**Lines met: 3 of 16.**

---

## 8. VERDICT

```
COLD REVIEW 003 RESULT        CHANGES_REQUIRED
```

Not `BLOCKED`: no packet evidence was missing, every digest matched, the L1 container extracted
cleanly at all three pins, and no finding required founder authority to reach.

Not `PASS`: thirteen threshold lines fail, one of them on a `BLOCKING` defect (CR3-B01) that defeats a
founder-sealed acceptance predicate with a trace violating no clause — and that v0.3's own edits
introduced.

**Even a `PASS` here would have meant only `READY_FOR_FOUNDER_ADJUDICATION`. It would not ratify the
SemanticProgram.** This review returns less than that.

### 8.1 What v0.3 got right — recorded because a review that only accuses is not a review

- **The capability repair is real.** SP-152 is a genuinely new compared surface with a new equality
  predicate, not v0.2's clause relabelled. The v0.2 counterexample is closed, and I could not
  reconstruct it by any route.
- **SP-160's precedence is total.** 18/18 cells, enumerated twice independently. The
  `complete`@idle collision is closed by a mechanism, not by prose.
- **The SP-090/SP-094 split is the best repair in the document.** The founder's *"might require"* is
  preserved verbatim and the authored requirement is correctly demoted. Its lesson was simply not
  carried one row down to SP-091.
- **§17's stated bound on the auditor is correct** and I confirm it.
- **The auditor's counting machinery is sound**, and its v0.2 replication is genuine, non-trivial
  evidence of measurement validity for those tallies.
- **A-08 is genuinely open and genuinely not silently resolved.**
- **§18's closing paragraph is honest**: *"Every line above is an author-side claim."* It was correct
  to say so.

---

## 9. SELF-LIMITATION

### 9.1 What this review did NOT test

- **Semantics of the commission and the RCP protocol themselves.** I tested v0.3 against L1, L2 §§
  cited in the crosswalk, and the two prior reviews. I did not audit the commission or the protocol
  for internal consistency.
- **SOURCE-CUSTODY-001's omissions.** I verified its digest and then used it for nothing, per the
  mandate. Whether its incompleteness has consequences elsewhere is untested here.
- **P-L3-A and P-L3-FD01 byte verification.** These L3 pins are cited by many clauses. I did not
  extract or hash them; L1 controls and L3 cannot supersede it, so no finding turns on them — but
  no clause resting solely on an L3 pin was provenance-checked.
- **Ordinals other than 59, 72, 85.** The mandate pins three. Founder material elsewhere in the
  container was not read, so I cannot rule out an L1 statement that would change an `EXACT` verdict.
- **Exhaustive enumeration beyond the three state-changing operations.** The 18-cell Cartesian is
  complete for `{begin, record, complete}`. Interactions of restart and DaySlot boundaries with
  arbitrary disposition assignments were spot-checked, not enumerated.
- **Numbering gaps.** Sixteen SP-ID gaps exist. I did not investigate whether any represents a
  silently withdrawn clause other than SP-132.
- **The 39 unmarked clause edits individually.** I diffed all of them and read the ones under
  verbatim-preservation headers in full. The remainder were classified as de-annotation on
  inspection, not verified line by line for semantic consequence.
- **Whether my own killed findings were killed correctly.** §2.20 lists attacks I abandoned; each
  could in principle have been abandoned in error.

### 9.2 What non-model-independence means for the strength of this review

I am lineage-independent, not model-independent. I did not author v0.2 and received no author-side
account — but I share an architecture and training distribution with whatever authored the subject.
**A defect that is invisible to this class of reader is invisible to this review.** The specific
risks:

- **Shared blind spots.** Where the candidate's reasoning is wrong in a way this architecture finds
  natural, I am likely to find it natural too. The `EXACT` judgments are the most exposed: they turn
  on entailment intuitions rather than on mechanical checks.
- **Convergent framing.** I largely accepted the candidate's own vocabulary — L-fact/T-fact,
  presented sequence, disposition — because it is the vocabulary the clauses are written in. A
  reviewer who rejected that framing might find defects in the framing itself that I cannot see.
- **Fan-out does not add independence.** Parts of this review were run as parallel attack lines and
  every finding they returned was re-verified by me against the primary sources before being
  recorded — several were downgraded and one was killed outright. But those lines share my
  architecture, so their agreement is **corroboration of execution, not of judgment.**

**Negative results in this review are therefore weaker than positive ones.** "I could not construct
an escape" (§3) should be read as bounded by that limit. "Here is a trace in which the founder
predicate fails and no clause is violated" (CR3-B01) is not — it is checkable by anyone.

**External review remains unperformed.** Nothing here substitutes for it.

---

## 10. INTEGRITY BLOCK — RE-VERIFIED AT CLOSE

### 10.1 Every evidence artifact byte-unchanged

Digests recomputed after all analysis was complete and compared against §0.2:

| File | Digest at close | Unchanged |
|---|---|---|
| v0.3 candidate (subject) | `55c590ead44e38248a7f97405c8cb23740018df4bd9b154a8a0fd3df99dd7f8e` | ✓ |
| v0.2 candidate | `611a782e7abdf323de6567497d4da372ff011142d44de16c6f53c2a9d1feb007` | ✓ |
| v0.1 candidate | `3e675d9ebd1e8bbb25193625ef9ca784146d8d639e57d5f5fe9dfaee46551537` | ✓ |
| Cold Review 001 | `54de4a52ffa4f63086cbc19d30e7d7beb49b5c61cc1b37a2605da187e626276f` | ✓ |
| Cold Review 002 | `bdd8c218ade5e37f0b23605ec2f789ae6f72b74855aa036eb9905039fc46167e` | ✓ |
| SLR-01-R1 | `a506352ae82bd889034b5972dc2b090185aac3c6ac58f6bbc083f7d4614e68c6` | ✓ |
| SOURCE-CUSTODY-001 | `0f61f7bb41ccdb74d00cb679f00df36b74d4221398835068bb4e5bf388734600` | ✓ |
| Authoring commission | `9a04124a25ec3dc9c281d73a4f6bce7ecb7a0619a0d9890f9a51fd5ce5dcc04e` | ✓ |
| L1 container | `cee97abe168b011e8cc2bf1d69009d755f8c744998302c76743ac432a7d81ebe` | ✓ |

The L1 container was opened read-only and never copied, imported, or written to. It remains outside
the RUORA boundary.

### 10.2 Git state — nothing staged

```
git diff --cached --name-only   →  (empty)
git reflog -1                   →  7387fe4 HEAD@{0}: commit: chore(governance): exclude
                                   chambers/ runtime infrastructure from doctrine repo
```

Nothing staged, nothing committed, nothing pushed by this review. The reflog's most recent entry is
`HEAD@{0}` and predates this review; no commit was created during it. The RC-0001 corpus — including
the subject — is **untracked** (`??`) in this repository, so no git operation could have altered it,
and §10.1's digests confirm it did not. One pre-existing unstaged modification
(`doctrine/self_axiom.md`) predates this review, is recorded in CR-001 §10.2 and CR-002 §13.3, and
was not touched.

**One discrepancy, reported rather than smoothed over.** The environment snapshot supplied to this
reviewer at session start described `HEAD` as `8097d18 ESM-C0-REALIZATION-SCOPE-ADJUDICATION-001`
with a clean tree. **That commit does not exist in this repository** — `git cat-file -t 8097d18`
returns *"Not a valid object name"*, and it appears nowhere in the reflog. Actual `HEAD` is
`7387fe4`. I cannot account for the difference from inside the review's authority, and I did not
investigate beyond confirming it. It does not affect any finding: every conclusion above rests on
file digests I computed directly, not on repository metadata, and all nine are byte-identical at
open and close. **But an integrity block that had simply asserted "git state clean, as recorded"
would have been false, and a reviewer relying on the supplied snapshot rather than on the
repository would not have noticed.** That is the same failure mode this review charges against
v0.3's "CARRIED FORWARD UNCHANGED" labels (CR3-05), and it would be improper to apply the standard
only outward.

### 10.3 Files created by this review

Exactly one, at the authorized path:

```
governance/OURSELF-RCP-RC0001-SEMANTICPROGRAM-v0.3-LINEAGE-INDEPENDENT-COLD-REVIEW-003.md
```

All auditor extraction, mutation probes, and scratch analysis were confined to the job tmp
directory. **v0.3 and v0.2 were never modified; every probe ran on a copy.** No secret-bearing
material was read, printed, or requested. The repository boundary was not expanded.

### 10.4 Terminal boundary

```
COLD REVIEW 003               CHANGES_REQUIRED
BLOCKING DEFECTS              1   (CR3-B01)
MATERIAL DEFECTS              13
MINOR DEFECTS                 5
PASS-THRESHOLD LINES MET      3 / 16
CR-001                        8 CLOSED · 1 PARTIALLY_CLOSED (one component REGRESSED)
CR-002                        10 CLOSED · 5 PARTIALLY_CLOSED · 2 NOT_CLOSED
DOCKET                        3 OPEN · 0 PARTIALLY_DECIDED · 5 OPERATIVELY_DECIDED
                              (candidate claims 2 / 1 / 5)
COLD REVIEW 001 SUBJECT       3e675d9e…551537   PRESERVED · UNMODIFIED
COLD REVIEW 002 SUBJECT       611a782e…feb007   PRESERVED · UNMODIFIED
COLD REVIEW 003 SUBJECT       55c590ea…dd7f8e   PRESERVED · UNMODIFIED
FOUNDER DECISIONS A-01–A-08   NOT RESOLVED
SEMANTICPROGRAM SEAL          NOT GRANTED
FOUNDER ADJUDICATION          NOT PERFORMED
GIT STAGING / COMMIT / PUSH   NOT PERFORMED · NOT AUTHORIZED
```

This review proposes nothing. It adjudicates and reports.
