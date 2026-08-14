# RC-0001 SEMANTICPROGRAM v0.4 — LINEAGE-INDEPENDENT COLD REVIEW 004

**DATE** 2026-08-13
**SUBJECT** `governance/OURSELF-RCP-RC0001-DURABLE-DAILY-RITUAL-LEDGER-SEMANTICPROGRAM-v0.4-CANDIDATE.md`
**SUBJECT DIGEST** `7c680b0286d79f8c6af162223bdfe62789f0123a5e28e28dcf855873df2cf48f` — verified before reading
**VERDICT** `CHANGES_REQUIRED`
**AUTHORITY LIMIT** Adjudication and report only. No repair, no proposed clause text, no v0.5, no staging, no seal.

---

## 0. Classification — recorded verbatim as mandated

```
LINEAGE-INDEPENDENT       YES
MODEL-INDEPENDENT         NO
EXTERNAL                  NO
TRANSPORT-INDEPENDENT     no claim required
LOCAL SOURCE SUFFICIENCY  REQUIRED
```

**The limit, stated plainly.** I share an architecture with whatever authored the subject. My **negative** results — "I attacked this and could not construct an escape" — are therefore **weaker evidence** than my positive ones. Where I report that v0.4 survived an attack, treat that as *this reviewer failed to break it*, not as *it is unbreakable*. The positive constructions in §4 are re-verifiable by anyone; the negative results in §2 and §4.10 are not.

### 0.1 Evidence digests — independently computed at open and re-verified at close

| Role | File | SHA-256 | Open | Close |
|---|---|---|---|---|
| **SUBJECT** | `…SEMANTICPROGRAM-v0.4-CANDIDATE.md` | `7c680b02…2cf48f` | ✓ | ✓ |
| Prior subject | `…v0.3-CANDIDATE.md` | `55c590ea…dd7f8e` | ✓ | ✓ |
| Prior subject | `…v0.2-CANDIDATE.md` | `611a782e…1feb007`¹ | ✓ | ✓ |
| Prior subject | `…v0.1-CANDIDATE.md` | `3e675d9e…551537` | ✓ | ✓ |
| Defect register 001 | `…COLD-REVIEW-001.md` | `54de4a52…626276f` | ✓ | ✓ |
| Defect register 002 | `…COLD-REVIEW-002.md` | `bdd8c218…c46167e` | ✓ | ✓ |
| **Repair mandate — CR-003** | `…COLD-REVIEW-003.md` | `d9afbcb4…c848b1` | ✓ | ✓ |
| Lineage adjudication | `…SLR-01-R1-…md` | `a506352e…14e68c6` | ✓ | ✓ |
| Custody witness (KNOWN INCOMPLETE) | `…SOURCE-CUSTODY-001.md` | `0f61f7bb…88734600` | ✓ | ✓ |
| Authoring commission (L2) | `…AUTHORING-COMMISSION.md` | `9a04124a…5cc04e` | ✓ | ✓ |
| L1 container | Codex rollout `019ff7ee…` | `cee97abe…d81ebe` | ✓ | ✓ |

¹ full value `611a782e7abdf323de6567497d4da372ff011142d44de16c6f53c2a9d1feb007`. All ten governance digests and the container match the mandate exactly.

**L1 pins — extracted by me with the documented `jq` command, not adopted from any record:**

```
jq -j 'select(.ordinal==N) | .payload.content | map(.text) | join("\n")' <container>

P-L1-A  ordinal 59  4cfd687b2ea9cdbcf366c29a60b124e76cf0f9cce9fb4de897d812b69b3f4bb5  ✓
P-L1-B  ordinal 72  796a3588fbd8fbc611b62f6bba2267d462dd42f92f865a876f82e3387190e221  ✓
P-L1-C  ordinal 85  e951c1bc4f3fdb0fdfe4f133624acfd521dfedb7240bbdb80a0fe4147d82b8e3  ✓
```

**Every `EXACT` test in §5 runs against those extracted bytes.** `SOURCE-CUSTODY-001` was opened only to identify what "HBC" denotes (§4.11); it was never used as a substitute for L1, and its known-incomplete §3 normalization underwrites no finding here.

### 0.2 BC-001-BOUNDARY — the transport rule, as a boundary condition only

The corpus is untracked in git, contained in no commit and on no remote; it cannot be exposed to a remote receiver. That condition is classified **transport custody only**, affects **zero SemanticProgram clauses**, and is orthogonal to CR3-B01.

```
BC-001-BOUNDARY  — observed and honoured
    I used only verified local authoritative sources.
    I did NOT treat unavailable transport custody as semantic absence.
    I did NOT infer source content from transport metadata.
    I did NOT waive any semantic test because transport is unavailable.
    I did NOT upgrade this local review into external independence.
    No required semantic source was unavailable LOCALLY.
    Therefore: proceed. Not BLOCKED.
```

**Transport custody was used as evidence for nothing in this review, in either direction.** It is not evidence that v0.4 is correct, and it is not a defect of v0.4. It remains a separate custody status outside this verdict. The verdict below rests entirely on semantic findings; had the transport condition been the only remaining issue, this review would have returned `PASS`.

**BC-001-FINDING** — the substantive question put to me under that label — is answered separately at §3.

---

## 1. Headline

| | |
|---|---|
| **CR3-B01** | **`CLOSED`** — the blocker is genuinely repaired by mechanism, not by description |
| CR-003 regression | 13 CLOSED · 6 PARTIALLY_CLOSED · **1 NOT_CLOSED** · 0 REGRESSED (+ CR-09 and the CR-002 residue CLOSED) |
| **New BLOCKING findings** | **1** — `CR4-01`, the loss-class vocabulary |
| New MATERIAL findings | 7 · New MINOR findings | 5 |
| Docket truth | **NOT ACCURATE** — I derive 3 OPEN · **1 PARTIALLY_DECIDED** · **4 OPERATIVELY_DECIDED**; v0.4 claims 3 · 0 · 5 |
| §16.5 mechanical tallies | **ACCURATE** — byte-reproduced by my own run. CR-003's overstatement finding does **not** recur |
| §16.4 auditor as published | **DOES NOT EXECUTE** — SyntaxError; body duplicated with a divergent copy |
| PASS threshold | 8 of 15 lines met |

**v0.4 is a substantially better document than its predecessor, and the blocker that gated this review is closed.** It is not ratifiable, because the repair of CR3-04 did not hold: the defect Cold Review 003 constructed at §3.5 reconstructs against v0.4 by a route the repair does not close, and the candidate rates that repair `IMPOSSIBLE`.

---

## 2. THE FIRST ATTACK — CR3-B01

### 2.1 The original counterexample, reconstructed from Cold Review 003's own register

I read CR-003 §2's CR3-B01 entry and reconstructed the defect from it, without reference to v0.4's account of what it repaired. v0.4's §0.5, its §16.2 repair-mode column, §18 and §18.2 are **author-side claims** and were treated throughout as an adversary's assertions.

The defect: v0.3 deleted the phrase "over the supplied trace" from SP-043 and SP-102 (`grep -c "supplied trace"`: v0.2 → 2, v0.3 → 0) and replaced it with a cumulative increment rule under "append-only and strictly monotonic", which affirmatively bars a reset. The count then had an increment rule, monotonicity and append-only-ness, and **no scope, no initial value, no reset point**. SP-094's initial condition named three L-facts and could not name the count, because SP-102 makes it a T-fact, SP-103 makes the classes disjoint, and SP-104 says "no preservation obligation ranges over T-facts."

CR-003's trace:

```
DaySlot 1
  instantiate        state=idle, pending=0, history=∅, illegal_count=0     [SP-040]
  present complete   ADMITTED; idle → SP-160 step 1 → INVALID_TRANSITION
                     SP-043 → illegal_count = 1
                     SP-035: every L-fact unchanged
  DaySlot boundary   SP-053 "idle remains idle"; T-facts persist (SP-102 monotonic)

DaySlot 2 — state=idle · durable Entry history EMPTY · pending EMPTY
            ↑ SP-094's stated initial condition, all three conjuncts, verbatim
  begin ; record("Reflect") ; complete ; restart     all four ADMITTED
  OBSERVE  five values ✓   illegal_transition_count = 1  ✗ founder requires 0
```

The load-bearing sentence was **"No clause is violated."**

### 2.2 My re-run against v0.4 — the decisive test

I re-ran that exact trace against v0.4's normative SP rows alone. **The load-bearing sentence is destroyed**, because v0.3's SP-043 was an *increment rule* and v0.4's is a *definition*:

> **SP-043** — "For a presented sequence `P`, `illegal_transition_count(P)` is **the number of elements of `P`** whose SP-160 result is `INVALID_TRANSITION`. Its value at the first element of `P` is zero; it increments by exactly one when and only when an element of `P` yields `INVALID_TRANSITION`; and **no earlier presented sequence contributes to it**."

An embodiment that reaches DaySlot 2, presents `⟨begin, record("Reflect"), complete, restart⟩` as its own presented sequence and reports count 1 is asserting that a four-element sequence containing **zero** `INVALID_TRANSITION` elements has count 1. That contradicts SP-043 directly. The counterexample now violates a clause, which is exactly what it previously did not do.

All three things CR-003 named as missing are supplied by normative rows:

| Missing in v0.3 | Supplied in v0.4 |
|---|---|
| scope | SP-043 — "derived over one presented sequence and has no existence outside it" |
| initial value | SP-043 — "its value at the first element of `P` is zero" |
| reset point | SP-102 — "each presented sequence begins with an empty T-fact set" |

Over the required vector the count is now **entailed**, not contingent on history: `begin` from idle, `record` from active, `complete` from active-with-pending are all lawful under SP-163, and `restart` is not an invocation, so SP-160 ("Every **admitted invocation** yields exactly one normative result") assigns it no result and it cannot increment. `count = 0` is forced.

### 2.3 The six commissioned attacks

**(1) Does the scoping close the hole or relocate it?** Closed for the founder predicate. The boundary is drawn by SP-102 and SP-043. I tested the obvious relocation targets:

- *Relocation to `entries.count`* — **fails.** SP-094 explicitly pins "empty durable Entry history" in the initial condition, so a prior day's Entries cannot inflate the count. I constructed this attack before reading the candidate's account and it does not land.
- *Relocation to the DaySlot coordinate* — **lands, but on a different requirement.** See `CR4-02` (§4.2); it defeats SP-091's equality, not the six founder acceptance values.

**(2) A presented sequence spanning a DaySlot boundary or a restart — v0.4 SURVIVES CLEANLY.** This attack fails, and it is the one I expected to succeed, because the founder's own required vector ends with `restart`. Three independent normative rows admit it: SP-150 defines the presented sequence as "of invocations **and discontinuity boundaries**"; SP-156 makes a boundary "a presented element under SP-150" whose "only lawful disposition is `ADMITTED`"; SP-050's T-fact cell says the restart makes "presented index advances by one" — continuing the sequence, not terminating it. **No clause anywhere states that a restart or a DaySlot boundary begins a new presented sequence.** The founder's four-element vector is one presented sequence, and founder-vector satisfiability is intact.

**(3) Satisfaction by a proper suffix — all routes closed.** Enumerated:

| Route | Disposition |
|---|---|
| proper suffix of a longer `P` | Blocked explicitly — SP-094: "A proper suffix of a longer presented sequence is not this required vector, however closely its L-facts resemble the stated initial condition." |
| prefix or infix | Blocked by SP-094's "is a complete presented sequence in its own right". The *specific* denial names suffixes only; the general phrase carries the rest. |
| disposition sub-selection — present `⟨complete, begin, record, complete, restart⟩`, dispose element 1 `CAPABILITY_UNSUPPORTED` so the admitted subsequence equals the vector | Blocked by SP-094's "Every element must be disposed `ADMITTED`." This requirement is doing real work. |
| `view` interleaving to manufacture positions | Blocked — SP-111: `view` "occupies no position". |

**(4) Does "each presented sequence begins with an empty T-fact set" contradict preservation, durability or monotonicity?** **No.** SP-104 — "no preservation obligation ranges over T-facts" — is the enabling clause and it is explicit. I checked SP-046, SP-049, SP-050, SP-051, SP-084 and SP-103: every durability and preservation obligation in the document ranges over L-facts. The attack fails. Two wording tensions survive as MINOR (`CR4-11`).

**(5) Is the count now under-counted?** Five routes tested, no defect. `CAPABILITY_UNSUPPORTED` elements never reach SP-160 and so are uncounted — but SP-152 compares dispositions by presented index, SP-155 forbids non-veridical disposition, and SP-094 requires all-`ADMITTED` for the required vector. Refusal-precedence masking is impossible: SP-160 evaluates state legality first and "evaluation stops", so an element both state-illegal and content-deficient yields `INVALID_TRANSITION`, never the content reason. `view` is excluded by SP-111. Unpresented invocations have "no program presence" (SP-055).

**(6) Can two embodiments disagree on where one presented sequence ends and the next begins?** **I could not construct a divergence.** SP-150 makes the presented sequence the *conformance input*; SP-121 confirms it is given ("the order is a component of that input"); SP-165 requires vectors to originate from canonical semantics. Sequence extent is therefore not an embodiment degree of freedom. **Reported as a negative result, and weak** — see §0.

I separately note that **no clause defines where one presented sequence begins or ends** (29 uses of the term, zero delimitation rule). This is inert today because SP-096 bounds the required-vector set to the SP-094 singleton, which pins the sequence exactly. It is recorded as `CR4-09` and goes live the moment that bound is lifted.

### 2.4 Disposition

```
CR3-B01    CLOSED
```

**Decisive test:** the CR-003 day-2 trace, re-run against v0.4's normative rows with the candidate's explanation set aside, now requires the embodiment to assert that a four-element sequence containing zero `INVALID_TRANSITION` elements has an illegal-transition count of 1 — a direct contradiction of SP-043's definitional form. The repair is structural. The count is a function of the sequence, not an accumulator over history.

This is the strongest repair in the document, and I say so plainly.

---

## 3. BC-001-FINDING — the question, answered

**The premise, verified by me against the pins rather than taken from the mandate.** `grep -inE "illegal|transition_count"` across all three extracted pins returns exactly one hit: **P-L1-B line 120, `illegal_transition_count = 0`**, inside the worked trace. P-L1-C line 104 carries the unrelated fail-list phrase "illegal transition behavior"; P-L1-A carries nothing. There is **no scoping language anywhere** — I searched the pins for `reset`, `scope`, `per-`, `session`, `count`, `DaySlot`, `day`. L1 contains **no DaySlot concept at all**; "Daily" occurs only inside the artifact name "Durable Daily Ritual Ledger". **Confirmed: mentioned once, nowhere scoped.**

Further, and under-reported: the founder's frame is *"the oracle **might require**"* — modalized, not asserted.

**My answer.** v0.4's presented-sequence scoping is **legitimate authored elaboration in form** — it is labelled `AUTHOR-PROPOSED`, SP-095 discloses that "presented sequence" occurs zero times across all three pins (I verified: 0/0/0), and SP-094 marks its own initial-condition qualification and modality promotion as authored. That discipline is real.

**But the choice is not neutral, and it is not docketed.** SP-043 and SP-102 both carry `—` in the Open-decision column, and I checked all eight docket items: none covers it. The scoping makes the count **structurally incapable of expressing cumulative illegality across sequences in a durable *daily* ledger** — which is precisely the reading v0.3 took, and which is equally consistent with the founder's single unscoped mention. Two materially different answers to "what is the count derived over?" are each consistent with L1's silence, and v0.4 installs one of them by authorship while leaving the docket silent.

**Determination: this is a founder decision given operative force without docketing.** It does not reopen CR3-B01 — the scoping is a sound repair *given* the choice — but the choice itself belongs on the docket. Recorded as `CR4-07`, MATERIAL. This is a question I was asked to answer, not evidence that v0.4 is correct, and I have not treated it as such.

---

## 4. FRESH FINDINGS

Weighted above regression, per the mandate. Thirteen findings. Each carries a concrete trace or enumeration and a stated falsifier.

### 4.1 `CR4-01` — the loss class is embodiment-authored and uncalibrated; CR-003 §3.5 reconstructs — **BLOCKING**

**Clauses attacked:** SP-151, SP-152, SP-155; §16.1 gate S-07; §0.5 row 2; §16.2 CR3-04; FT-13.

v0.4's central repair moves the capability *type* inside the compared surface. SP-152 now compares "the same disposition and — where that disposition is `CAPABILITY_UNSUPPORTED` — **the same loss class**". That is correct in shape. The defect is that **the loss class's extension is set by the party being tested**:

> **SP-151** — "a **loss class**: the embodiment's declared identification of *which semantic capability it lacks*. **The loss class is drawn from the embodiment's published capability declaration**, is fixed before the run, and is never silent."

I searched every occurrence of "loss class" in v0.4 and every occurrence of `loss` in all three pins. **No clause enumerates the loss-class vocabulary, closes it, fixes its granularity, individuates "semantic capability", or establishes a shared registry.** §15 gained a *Position vocabulary* (CR3-06) and a *Content vocabulary* (CR3-07) in v0.4 and gained **no loss-class vocabulary** — though the loss class is the surface CR3-04 flagged. L1 supplies none either.

**Concrete trace — CR-003 §3.5's sequence, unchanged.** Presented `P = ⟨begin, record("A"), record("B"), complete⟩`.

| # | Element | G″ — cannot hold a 2nd pending contribution | H″ — can hold two, cannot preserve their canonical order, so declines | Compare |
|---|---|---|---|---|
| 1 | `begin` | `ADMITTED` | `ADMITTED` | ✓ |
| 2 | `record("A")` | `ADMITTED` | `ADMITTED` | ✓ |
| 3 | `record("B")` | `CAPABILITY_UNSUPPORTED` / `SECOND_RECORD_UNSUPPORTED` | `CAPABILITY_UNSUPPORTED` / `SECOND_RECORD_UNSUPPORTED` | **EQUAL** |
| 4 | `complete` | `ADMITTED` → Entries `[A]` | `ADMITTED` → Entries `[A]` | ✓ |

Each embodiment publishes, before the run, a declaration containing that single coarse class. Clause check, exhaustive: **SP-150** ✓ total, one disposition per element. **SP-151** ✓ typed T-fact, class drawn from the published declaration, fixed pre-run, never silent. **SP-152** ✓ same disposition, same loss class, identical `ADMITTED` outcomes. **SP-155** ✓ — it requires *truth*, never *specificity*; neither embodiment can in fact admit element 3, so neither declaration is false. **SP-156** n/a. **SP-157** ✓ both consume presented index 3, neither an admission ordinal. **SP-159** ✓ neither substitutes, approximates, reorders, nor invents an adaptation. **SP-093** ✓ nothing was *erased by normalization*; the class was **declared** coarse. **SP-131** ✓ the comparand is "the one this SemanticProgram assigns", and the program assigns no loss class. **SP-038** ✓ requires disposed ≠ absent, not class ≠ class.

**G″ and H″ compare EQUAL. No clause is violated.** H″'s loss is **canonical ordering** — a member of P-L1-A's sealed scope list and of P-L1-C's Fail list — and it is invisible in the compared record. This is Cold Review 003 §3.5 reproduced against the document that claims to have made it impossible.

**Both readings of SP-151's closing sentence fail.** "Two embodiments lacking different capabilities therefore carry different loss classes." Read *descriptively* (the "therefore" signals a derived conclusion), the conclusion does not follow: nothing establishes an injection from lacked-capability to declared class, and the definitional content makes the mapping embodiment-chosen. Read *normatively* as an injectivity requirement, the trace **still conforms**, because no clause individuates "semantic capability" — at coarse granularity G″ and H″ lack *the same* capability, so they are permitted, indeed required, to carry the same class.

**Two further routes, needing no coarse token:**
- *False negative by homograph.* G lacks capacity and declares `LIMIT`; H lacks canonical ordering and declares `LIMIT`. Each is veridical within its own declaration. SP-152 compares equal.
- *False positive by synonym.* Two embodiments with the identical loss, one declaring `CAPACITY_EXCEEDED` and the other `CAPACITY_LIMIT`, are reported **nonconforming**, with no clause saying which was wrong. This is CR-003 §3.5's second reading, relocated from the disposition token to the loss class.

**Why it is a defect.** P-L1-B constitutional law 3 requires capability loss to be "**typed** and explicit." v0.4's own diagnosis of v0.3 — "v0.3 achieved explicit and stopped short of typed" — applies unchanged to v0.4: explicit is achieved, and the type's discriminating power is set by the tested party. This also constitutes a **hidden semantic input**: the embodiment's published capability declaration is an input to the conformance judgment that is not part of the presented sequence, not defined by the SemanticProgram, and absent from §14's crosswalk.

**Internal tension v0.4 created and did not see.** SP-165, new in v0.4, forbids a vector "whose expected values are read off an embodiment's observed behaviour — it would make the target its own oracle and prove only that an implementation agrees with itself." SP-151 makes the loss class — a value SP-152 compares to reach the conformance verdict — come from the tested embodiment's own declaration. The loss class escapes SP-165's literal scope, but SP-165's own rationale condemns it.

**Consequences:** §0.5 row 2 and §16.2 rate CR3-04 `IMPOSSIBLE` — **false**. §16.1 gate S-07 claims "PASS — and **now genuinely typed**" — **false**. FT-13's expected result does not follow from any clause, and FT-13's own falsifying column ("a loss of canonical ordering … reported as the same fact as a loss of capacity") is *realized* by the trace above. A-07's `OPERATIVELY_DECIDED` is false (§6).

**Falsified by:** exhibiting any clause that (a) enumerates or closes the loss-class vocabulary, (b) fixes the individuation of "semantic capability", or (c) imposes a minimality or maximal-specificity obligation on a declared class. I searched for all three and found none.

### 4.2 `CR4-02` — the required vector does not determine its own reference trace on the DaySlot coordinate — **MATERIAL**

**Clauses attacked:** SP-094, SP-019, SP-023, SP-091, SP-093, SP-114.

SP-094 pins the required vector's initial condition to **three** conjuncts: "initial state idle with empty durable Entry history and empty pending". SP-019's complete L-fact set has more members than that, and `view(n)` returns **all** of them (SP-110), and SP-114 makes the witness compare `view(n)` across substrates.

**Unpinned by SP-094:** Ledger identity, Ritual identity, and **current DaySlot ordinal**.

**Concrete construction.** Both embodiments satisfy SP-094's three stated conjuncts verbatim.

```
Embodiment W   fresh ledger. DaySlot ordinal = 1. state idle, history ∅, pending ∅.
Embodiment S   same ledger and ritual identity, having passed six idle DaySlot
               boundaries with no invocations.
               SP-053 "idle remains idle"; SP-074 "A missed idle DaySlot creates no Entry".
               DaySlot ordinal = 7. state idle, history ∅, pending ∅.

Present to both:  ⟨ begin, record("Reflect"), complete, restart ⟩   all ADMITTED

Six founder acceptance values: IDENTICAL and correct for both.
view(n) at every n:            DIFFERS — current DaySlot ordinal 1 vs 7.
```

**Normalization cannot rescue it.** SP-093 permits erasing only "structural, visual, binary, runtime, and presentation differences". The DaySlot ordinal is none of those — **SP-023 declares it semantic** ("a monotonically ordered logical recurrence partition **whose ordinal is semantic**") and SP-070 lists it among "the only ordering facts". So the divergence survives normalization, and SP-091 — a `FOUNDER_SEALED_L1 / EXACT` row requiring "the reference semantic trace and each normalized target trace must be equal" — fails, **while neither embodiment violates any clause**.

The candidate's own trace suite exhibits this: **FT-01 runs the required vector with no DaySlot specified; FT-14 runs it at DaySlot 2.** Two runs of the sole required vector whose traces cannot be equal.

**Why it is a defect.** It is CR3-B01's shape — a founder-sealed requirement fails while every normative clause holds — on a third coordinate. CR-003's B.4-F6 disposition already warned the vector was "still not self-sufficient, now on a different coordinate"; that warning was answered for the count and not for the rest of SP-019.

**Graded MATERIAL, not BLOCKING, and I state why:** unlike CR3-B01 it defeats none of the six founder acceptance values, and a harness that runs both embodiments from a common start avoids it entirely. It nonetheless defeats the PASS line *founder vector — self-sufficient*.

**Falsified by:** any clause pinning the initial DaySlot ordinal for the required vector; or restricting the compared trace to the six acceptance values; or declaring the DaySlot ordinal's value non-semantic or normalizable.

### 4.3 `CR4-03` — the §16.4 auditor as published does not execute, and its body is duplicated with a divergent copy — **MATERIAL**

**I ran this myself.** §16.4 line 663 instructs: "save as `sp-evidence-audit.py`, run `python3 sp-evidence-audit.py <this file> [prior version]`." Doing literally that:

```
File "sp-evidence-audit.py", line 116
    ```.*?^```', '', norm, flags=re.M | re.S)
                  ^
SyntaxError: unterminated string literal (detected at line 116)
```

**The published apparatus produces no output at all.**

**Cause.** The fenced block runs from document line 666 to 869. Line 781 is document line 692 with its first 26 characters (`norm_nofence = re.sub(r'^`) deleted — a paste artifact. Lines 781–869 are a second, headless copy of the program body. My `diff` of document lines 692–780 against 781–869 returns exactly two hunks:

```
< norm_nofence = re.sub(r'^```.*?^```', '', norm, flags=re.M | re.S)      (doc 692)
> ```.*?^```', '', norm, flags=re.M | re.S)                               (doc 781)

< ft = len([l for l in L if re.match(r'^\| FT-\d{2} · ', l)])             (doc 726)
> ft = len([l for l in L if re.match(r'^\| FT-\d{2} ', l)])               (doc 815)
```

**The copies are not identical, and the divergence is substantive.** Copy 2's FT regex omits the `· ` separator, so it also matches document line 627 — a §16.3 prose-table row that is not a falsifying trace at all. I ran both:

| Extraction | `FT_ROWS` | Result |
|---|---|---|
| Copy 1 (doc 666–780) | **16** | reproduces §16.5 **byte-identically** |
| Copy 2 (doc 666–691 + 781–869, head repaired) | **17** | **contradicts §16.5** |
| The published block, verbatim | — | **SyntaxError, no output** |

Nothing in §16.4, §16.5, §16.6, §18 or anywhere else acknowledges the duplication.

**Why it is a defect.** §18's exit gate claims "embedded auditor rerun | **YES** — §16.5, regenerated to a fixpoint and **byte-reproducing**", and CR3-17's repair claim is "A `diff` of a fresh run against the block now matches, which is what the section invites." A fresh run of the published script **errors**. The section's own invitation cannot be accepted. This is the CR-001 CR-09 / CR3-17 concern — evidence-apparatus integrity — recurring in the apparatus that was rebuilt to answer it.

**In fairness, and this matters:** the *content* of §16.5 is correct. See §7.

**Falsified by:** showing document lines 726 and 815 are byte-identical, or that saving the fenced block and running it produces output.

### 4.4 `CR4-04` — SP-005 carries authored normative law inside a `FOUNDER_SEALED_L1 / EXACT` row — **MATERIAL**

The four-term chain is byte-faithful; I compared against my extracted P-L1-B lines 92–104. SP-005 does not stop there:

> **Founder (L1-72:92–104, complete):** "We should explicitly distinguish: / semantic equivalence / ≠ / structural equivalence / ≠ / visual identity / ≠ / binary identity" … "What must remain equal are the declared observable semantics."
>
> **Candidate (SP-005):** …the chain, then — **"A conforming embodiment preserves the acceptance predicates of this SemanticProgram through semantic equivalence; structural equivalence, visual identity, and binary identity are each distinct from it and none substitutes for it."**

That sentence is **not present in L1 at all**. It is a normative conformance condition on embodiments referencing "this SemanticProgram" — an artifact the founder never saw. "acceptance predicates" occurs in L1 only at law 4 and in P-L1-C's emitter list and fail list, never joined to the ≠ chain.

**This is structurally the identical defect CR3-01 found on SP-091 and rated MATERIAL.** v0.4 applied the SP-090/SP-094 split technique to SP-091→SP-095, SP-158→SP-159 and SP-164→SP-165, and did not apply it to SP-005. **CR3-01's repair is row-local, not class-local.**

**Falsified by:** exhibiting L1 text asserting that a conforming embodiment preserves acceptance predicates through semantic equivalence, or showing the sentence is non-normative.

### 4.5 `CR4-05` — SP-091 silently drops the founder's dual-substrate cardinality — **MATERIAL**

> **Founder (P-L1-C lines 89–97), extracted by me:**
> ```
> Pass
>
> Reference trace
>      =
> Normalized Web trace
>      =
> Normalized iOS trace
>
> for every required vector.
> ```
>
> **Candidate SP-091 (`EXACT`, `FOUNDER_SEALED_L1`):** "For every required vector, the reference semantic trace and **each normalized target trace** must be equal."

Two departures. First, "Reference trace" becomes "reference **semantic** trace" — a word inserted into a claimed-exact reproduction, and §17.1's own citation quotes the source correctly as "Reference trace", so the audit row and the clause it audits disagree. Second, and materially: **two named traces become an unbounded quantifier over an undefined target set.**

I searched v0.4 exhaustively. **"iOS" occurs 3 times in 1074 lines — all inside SP-164's quotation and two §17.1 citations. No normative clause fixes the target set at two, or names Web and iOS.** The founder's Pass condition is a three-way equality that cannot be vacuous; SP-091's is satisfied by an empty or singleton target set. The proposition is **strictly weaker** than the one it claims to reproduce exactly — a hit on two of §17's own nine attacks (narrower proposition, changed quantifier).

The dropped material is not incidental. The founder titles the proof **"RC-0001 · Dual-Substrate Semantic Preservation"** (P-L1-A:41, P-L1-B:142) and fixes the topology as "**TWO** independently lowered targets → **TWO** observed trace sets → ONE conformance judgment" (P-L1-C:81–85). §16.1's gate table has no gate for it.

The asymmetry is visible inside the document: CR3-08 forced v0.4 to *declare* the required-vector quantifier bound (SP-096). The target-set quantifier gets no such declaration.

**Falsified by:** exhibiting a v0.4 clause fixing the embodiment or target set at two, or naming Web and iOS normatively.

### 4.6 `CR4-06` — SP-046 promotes a hedged worked example to unhedged universal law under an `EXACT` seal — **MATERIAL**

> **SP-046 (`EXACT`, `FOUNDER_SEALED_L1`):** "Once complete, an Entry and its content, status, and relative order survive a restart."

L1's unhedged support is two bare register lines: "+ durability", "+ restart preservation" (P-L1-A:52–53). Neither names *what* is preserved. The field list — content, status, relative order — is drawn **solely** from P-L1-B's worked trace, which the founder modalized as "the oracle **might require**". SP-046 states it flatly and universally (any Entry, not the one-Entry example) and composes three separate register items into one law binding relative order to restart survival.

**The document convicts itself.** SP-094 says in terms that "the promotion from 'might require' to 'must produce' **are authored, not founder-sealed**" and is labelled `AUTHOR-PROPOSED / ELABORATES` accordingly. SP-046 performs the same promotion, keeps `FOUNDER_SEALED_L1 / EXACT`, and receives no split. §17.1's SP-046 row discusses only the CR3-15 "contemplated" scope attack and never applies attack #9 (changed quantifier or modality), despite §17 asserting all nine were applied to every claim.

**Falsified by:** exhibiting unhedged L1 text naming content, status and relative order as what survives a restart.

### 4.7 `CR4-07` — the count's scoping is an undocketed founder decision given operative force — **MATERIAL**

Established at §3. L1 mentions the count once and never scopes it; v0.4 installs presented-sequence scoping by authorship; SP-043 and SP-102 carry `—` in the Open-decision column; no docket item covers it; and the opposite reading (v0.3's) is equally consistent with the silence and produced a BLOCKING defect. Two materially different answers to a founder silence, one installed, none docketed.

**Falsified by:** a docket item covering the derivation scope of the illegal-transition count, or L1 text scoping it.

### 4.8 `CR4-08` — §13.0's branch mapping is not a partition, and v0.4 affirmatively asserts that it is — **MATERIAL**

> **§13.0:** "The deleted conjunct is restored. **The three branches are now mutually exclusive and jointly exhaustive over a non-empty `Adm(A)`.**"

The rule:

```
YES for all members of Adm(A)                        → OPEN
YES for some members of Adm(A) and NO for others     → PARTIALLY_DECIDED
NO for all but one member of Adm(A)                  → OPERATIVELY_DECIDED
```

**Overlap 1 — singleton `Adm`.** Let `Adm(A) = {x}`. Branch 3's "all but one" ranges over `∅`; a universal quantification over the empty set is vacuously TRUE, so branch 3 fires. If `T(x) = YES`, branch 1 also fires. **Both.** And **every one of the five `OPERATIVELY_DECIDED` items has a singleton `Adm` by §13.1's own cells**: A-01 "**D only**", A-04 "**A only**", A-05 "**A only**", A-06 "**A only**", A-07 "**(a) only**".

**Overlap 2 — `|Adm| ≥ 2` with exactly one YES.** Branch 2 ("YES for some and NO for others") and branch 3 ("NO for all but one") both fire.

Branch 3's extension is a proper subset of (branch 1 ∪ branch 2) over every non-empty `Adm`. **Under §13.0 as written, `OPERATIVELY_DECIDED` is never the unique output of the rule.** CR-003 §4.1(a) caught the OPEN/PARTIALLY_DECIDED overlap; v0.4 closed that one and asserted a partition without checking branch 3 against either neighbour.

**Arity defect, compounding.** `T` is written as a *binary* predicate over pairs ("can **two** embodiments adopting **different** ones both satisfy"), while all three branches quantify over *single* members. On a singleton there is no pair, so `T` has no instance and no branch determinately fires. Under either reading, the five `OPERATIVELY_DECIDED` labels are produced by the admissibility filter's singleton output plus an unstated convention, never by `T`.

**Falsified by:** a stated tie-break or priority order among the branches. §13.0 contains none — it claims mutual exclusivity, which is the opposite.

### 4.9 `CR4-09` — SP-019's "complete L-fact set" is falsified by SP-053 and SP-075 — **MATERIAL**

> **SP-019:** "The **complete** L-fact set is: Ledger identity; Ritual identity; current-state value; current DaySlot ordinal; ordered pending contributions while present; durable ordered Entries with content and status; and canonical history order."
>
> **SP-053, "L-facts that survive" column:** "Ledger and Ritual identity; pending contributions; completed Entries; **origin DaySlots**; canonical order."
>
> **SP-075:** "An active interval crossing a DaySlot boundary **retains its originating DaySlot** for the Entries produced when it later completes."

**Trace.** Present `⟨begin, record("A"), ⟨DaySlot boundary⟩, complete⟩` from idle at DaySlot 1. Immediately after the boundary, the L-facts available under SP-019 are `state=active`, `current DaySlot=2`, `pending=["A"]`. **Nothing in SP-019 records that the interval originated at DaySlot 1**, and it is not recoverable from canonical history order because the contribution is not yet in history. Either SP-019 is exhaustive and SP-075's retention obligation ranges over a fact the program does not carry — a contradiction — or SP-019 is not exhaustive.

**Why it matters beyond the contradiction.** Four of the five `OPERATIVELY_DECIDED` docket justifications have the form "requires an X as semantic fact; **SP-019 carries none**". That inference presupposes SP-019's exhaustiveness. **The presupposition is false.** I checked each label for an independent ground and all four surviving ones have one (§6), so this flips no label — but it falsifies the docket's stated reasoning.

Pre-existing since v0.2 (SP-019, SP-053 and SP-075 are byte-identical across v0.3 and v0.4) and never found; CR-003 §4.4 relied on the self-description without testing it.

**Falsified by:** showing "origin DaySlots" is derivable from an SP-019 member at every position, or that SP-019's "complete" is not a completeness claim.

### 4.10 `CR4-10` — the CR3-06 coordinate separation was not propagated; `view`'s domain is specified three inconsistent ways — **MATERIAL**

**§15's own claim is false.** "Two coordinates are now named separately and **neither is called 'position' unqualified**." Counterexamples in *normative* rows: **SP-013** ("at an identified operation **position**"), **SP-110** ("from any operation **position** `n`"), **SP-111** ("defined at every operation **position** … occupies no **position**"), **SP-081** ("at a later **position**"), **SP-021** ("canonical history **position**"), **SP-025** ("canonical **position**"), **SP-070** ("Admission **position** ordinal"), **SP-072** ("at its admission **position**"), plus **SP-053**'s T-fact cell ("**position** advances by one") and **§6.1** ("At operation **position** `n`"). §15 pins two names; at least four more coordinate terms remain in use.

**The substantive consequence.** SP-157: "Only `ADMITTED` **invocations** additionally receive an SP-071 admission ordinal." SP-051: "A restart **invokes no operation**." So a restart consumes **no admission ordinal**. But SP-112 (the CR3-05 repair) defines `view`'s determinism over "a given **admission ordinal** `n`", while §6.1 and FT-10 require `view` to be defined one step past a restart — "`view(n+1) = view(n)`". **Under SP-157 that `n+1` does not exist.** SP-050 says the restart advances the *presented index*; SP-053 says *position* advances. Three names, one effect, no reconciliation.

**And it reaches the founder vector.** §11.1 evaluates the five L-fact acceptance values by "SP-110 `view` at the **final admission ordinal**". For `⟨begin, record("Reflect"), complete, restart⟩` the admission ordinals are begin=1, record=2, complete=3, and `restart` has none — so the final admission ordinal is **3, before the restart**. The founder placed `restart` in the trace to exercise restart preservation ("+ restart preservation" is a sealed scope member; "restart semantics" is on P-L1-C's fail list), and the observation row does not reach past it. Since SP-096 makes this the **only** required vector, **RC-0001's entire required-vector suite never observes anything after a restart.**

**Bounded honestly:** no conformance *escape* follows. A state-losing embodiment is still caught by SP-046, SP-050 ("An L-fact survives exactly or the restart law is violated") and SP-084 as clauses. This is a witnessing gap and a falsified self-description, not a leak. §16.2's CR3-06 post-repair claim — "Neither reading survives; the position-indexed witness surface cannot misalign" — is overstated.

**Falsified by:** a clause assigning the restart an admission ordinal, or an instrument evaluating the acceptance values at a post-restart index, or a scope limiter reconciling SP-110 with SP-112.

### 4.11 `CR4-11` — SP-121's stated reason is false under the disposition regime — **MATERIAL**

SP-121 is **byte-identical in v0.3 and v0.4** and carries no change marker:

> "Two embodiments given the same presented sequence necessarily receive the same admission order, **because the order is a component of that input**."

v0.4 repaired precisely this error form in §7.1, for the T-fact stream: "v0.3's law here read 'the same presented sequence yields the same stream', which Repair 1 makes false by construction." The same reasoning applies here and was not applied.

**Trace.** Presented `⟨begin, record("A"), record("B"), complete⟩`. E1 admits all four → admission ordinals 1, 2, 3, 4. E2 disposes `record("B")` `CAPABILITY_UNSUPPORTED` → ordinals 1, 2, and `complete` at **3**, not 4 (SP-157: unsupported elements consume no admission ordinal). Same presented sequence, different admission-ordinal assignment.

The admitted sequence is **not** "a component of that input" — it is the image of the presented sequence under the embodiment's disposition function. Under the relative-order reading SP-121's conclusion survives but its justification is wrong; under the ordinal-assignment reading the conclusion is false too.

**Falsified by:** showing that "admission order" in SP-121 denotes only relative order, and that the row's justification is not a normative claim.

### 4.12 `CR4-12` — §17.3's `ORTHOGONAL` justification for SP-029 rests on a premise L1 falsifies — **MATERIAL**

> **§17.3, SP-029 row:** "**L1 asserts nothing about these constructs in either direction.**"

False, from my own extraction, for `Adjudication`:

```
P-L1-A:25   Adjudication                              ← stage in the canonical stack
P-L1-B:21   Adjudication                              ← again, in the frozen doctrine stack
P-L1-B:38   6. Witness ≠ judgment. … adjudication determines whether that occurrence satisfies law.
P-L1-C:26   11. Adjudication + Promotion Boundary     ← required protocol layer
P-L1-C:55       adjudicate success                    ← forbidden to the emitter
```

SP-029's clause text carries **no scope limiter** — "No confirmer, amender, invalidator, Reporter, Assertion, Adjudicator, **Adjudication**, or Establishment construct **exists** …" — while its `ORTHOGONAL` neighbours all carry one (SP-014 "by this SemanticProgram", SP-016 "No RC-0001 operation", SP-054 "of this program").

A charitable scope reading ("exists in this program's ontology"; the SemanticProgram is stage 2 and Adjudication is stage 8) rescues the *verdict* — but **it is not the defence §17.3 mounts**. §17.3 forecloses it by denying L1 says anything at all, whereas the parallel SP-016 row makes exactly the scope argument. v0.4's own §10 assigns this ontology "`CONFLICTS` when it gates the founder trace", so the document elsewhere knows the relation is not unconditionally orthogonal.

This is the class CR3-03 rebuilt §17.3 to eliminate: a relation awarded on an argument that does not survive contact with the source. I record the **justification** as defective and do **not** assert that SP-029 conflicts with L1 — the scope reading is available.

**Falsified by:** exhibiting a scope limiter in SP-029's clause text, or L1 text showing Adjudication is not a required stage.

### 4.13 Minor findings

| ID | Finding | Severity |
|---|---|---|
| `CR4-M1` | **§17.1's own tally is internally inconsistent.** "Nine survive from v0.3's set of nine, **four of them** repaired here after a successful attack (SP-004, SP-005, SP-041, SP-046, SP-091, SP-092 — **six** repairs across **five** rows plus SP-091's split)" — the parenthetical lists **six** row IDs, and §17.2 confirms six rows had successful attacks. "Four" and "five rows" are both wrong. Exactly the tally-overstatement class CR-003 found in v0.3, at reduced amplitude. *Falsified by:* a reading on which "four" ranges over CR3-15's subset only — but the parenthetical enumerates all six. | MINOR |
| `CR4-M2` | **SP-158 alters a quotation and disagrees with its own audit.** Founder P-L1-C:51 reads `    invent capability adaptations` with **no** period; SP-158 renders it `invent capability adaptations.` with the period **inside** the quotation marks; §17.1's citation of the same row renders it without. SP-158's stated falsifier is "falsify by showing the quotation differs from the pin." It differs. SP-158 also adds the authored connective "correspondingly", while §17.1 audits it as "reproduces and asserts **nothing further**". | MINOR |
| `CR4-M3` | **The Semantic Source Map has zero surface in v0.4.** `source map`, `sourcemap`, `CapabilityDecision`, `traceab` — **0 occurrences** in 1074 lines. P-L1-C seals it in the status block as `TRACEABILITY REQUIREMENT / Semantic Source Map`. Exclusion is likely correct on the merits (the founder frames it as belonging in the Protocol artifact), but v0.4 explicitly scoped out constitutional laws 1/4/6/7 with a stated rationale and extended no such disclosure here. The founder's chain is **not** silently symmetrized — it is omitted entirely. | MINOR |
| `CR4-M4` | **§16.1's 9/9 rationale mischaracterizes two founder laws.** "Laws 1, 4, 6 and 7 concern emitters, adaptation mechanics and promotion." Law 1's first sentence — "Reference semantics are normative" — has *reference semantics*, this artifact's own layer, as its subject. Law 6 — "Witness ≠ judgment" — has witness and adjudication as its subject, and v0.4 **does** carry a witness surface (SP-013, SP-051, §6.1, §11.1). No substantive contradiction of law 6 was found; the defect is that a PASS gate rests on a rationale false for two of its four members. | MINOR |
| `CR4-M5` | **§15 binds none of the founder's acceptance vocabulary.** §15 pins `canonical`, `durable`, `pending`, `view`, `disposition`, `loss class`, `present`, `absent`, `presented index`, `admission ordinal` — and **none** of `entries`, `entries.count`, `entries[0]`, `state`, `status`. No clause states that `entries` is indexed, that indexing is zero-based, or that `[0]` denotes the first element under SP-024 canonical order. The founder's own `[0]` notation arguably fixes zero-basing by fiat, which is why this is MINOR — but §15 is the section whose job this is. | MINOR |

---

## 5. `EXACT` claims — audited against bytes I extracted

**Count verified independently: 11.** Derived two ways (`grep -E '\| *EXACT *\|'` over the whole file, and a word-boundary sweep excluding `EXACTLY_ONE`), both yielding the same set, and matching §16.5's enumeration. **No `EXACT` judgment exists outside SP rows** — §10's Ledger·Ritual cell now reads `ELABORATES (RECLASSIFIED, CR3-16)`, so CR3-16's escape is genuinely closed.

`SP-001 · SP-004 · SP-005 · SP-018 · SP-041 · SP-046 · SP-090 · SP-091 · SP-092 · SP-158 · SP-164`

| Row | Verdict against extracted bytes |
|---|---|
| **SP-090** | **EXACT MATCH.** All six predicates in founder order, character-exact; "might require" preserved; "If both substrates satisfy that normalized semantic trace, they conform" reproduced. The strongest row in the document — I could not break it on any of the nine attacks. |
| **SP-164** | **EXACT MATCH** against P-L1-B:34, modulo the list numeral. |
| **SP-041** | **EXACT / normalization-only.** Both registers verified present in both pins. The "two separate unlabelled registers" parse is authored segmentation but it **narrows** rather than widens, and the operation→edge inference is correctly exiled to SP-163 as `AUTHOR-PROPOSED`. §17.1's "L1's chain has two arrows" is true. |
| **SP-018** | **EXACT.** Faithful and self-limiting. |
| **SP-004** | **NORMALIZATION-ONLY.** All three registers verified member-for-member (5 / 6 / 7). The "no AI" / "No generative AI" extent difference is genuinely preserved and docketed. Its own falsifier ("or a rendering difference") is hit — P-L1-C's `* `-prefixed vertical bullets are rendered inline — but the substantive repair is sound. |
| **SP-092** | **NORMALIZATION-ONLY.** All eight fail-list items verified in order; only the quoted fragment's case and terminal period differ. |
| **SP-001** | **NORMALIZATION + light referent transfer.** "substrate-neutral" is the founder's word, but his referent is "A substrate-neutral **semantic reality**"; v0.4 re-attaches it to the Ledger. The eleven members verified. |
| **SP-158** | **NORMALIZATION-ONLY, own falsifier hit** — see `CR4-M2`. Law 5 itself is verbatim-correct against P-L1-B:37. |
| **SP-005** | **SUBSTANTIVE DIFFERENCE** — `CR4-04`. Authored normative sentence inside a sealed row. |
| **SP-091** | **SUBSTANTIVE DIFFERENCE** — `CR4-05`. Quantifier widening plus silent drop of the founder's dual-substrate cardinality. |
| **SP-046** | **SUBSTANTIVE DIFFERENCE** — `CR4-06`. Modality promotion under an `EXACT` seal. |

**§11's founder trace and acceptance predicates — verified character by character.** All six predicates are reproduced faithfully in SP-090 and §11.1: `state = complete`, `entries.count = 1`, `entries[0].content = "Reflect"`, `entries[0].status = complete`, `history_order = canonical`, `illegal_transition_count = 0`. The vector `⟨ begin, record("Reflect"), complete, restart ⟩` matches the founder's four events in order. **Nothing dropped, nothing renamed.** Seven qualifiers v0.4 adds that the founder did not write — all-`ADMITTED` disposition, the three-conjunct initial condition, the presented-sequence scoping, the proper-suffix denial, the "might require" → "must produce" promotion, "same Ledger identity" on restart, and the content-presence precondition — **all land in `AUTHOR-PROPOSED` clauses and are labelled as such.** That is disciplined and I record it as such.

Two structural observations: §11.1 renders the founder's unqualified sixth predicate as scoped "over this presented sequence", disclosed inline to SP-043/SP-102; and the section titled "Founder-sealed trace and acceptance predicates" has four of its seven rows `AUTHOR-PROPOSED`, so the heading overclaims its contents.

---

## 6. Docket adjudication — all eight, tested second-order

I read the clause set from the normative SP rows (§0.4: "Only **SP** rows are normative"), not from §13's summary, and applied the test independently. Both constructions are shown per item; materiality is judged by SP-092's divergence surfaces filtered through SP-093's erasability.

| Item | Candidate | **Mine** | Divergence |
|---|---|---|---|
| A-01 | OPERATIVELY_DECIDED | **OPERATIVELY_DECIDED** | Label correct; one justification component unsound |
| A-02 | OPEN | **OPEN** | Label correct; the v0.4 C-inadmissibility "correction" is wrong |
| A-03 | OPEN *(reclassified)* | **OPEN** | **None.** Reclassification verified sound |
| A-04 | OPERATIVELY_DECIDED | **OPERATIVELY_DECIDED** | None |
| A-05 | OPERATIVELY_DECIDED | **OPERATIVELY_DECIDED** | None |
| A-06 | OPERATIVELY_DECIDED | **OPERATIVELY_DECIDED** | None |
| **A-07** | **OPERATIVELY_DECIDED** | **PARTIALLY_DECIDED** | **DIVERGES — MATERIAL** |
| A-08 | OPEN | **OPEN** | None; withdrawal rationale for (c) uses the wrong set operation |

**Derived tally: OPEN 3 · PARTIALLY_DECIDED 1 · OPERATIVELY_DECIDED 4.** v0.4 reports 3 · 0 · 5. **The class v0.4 reports as `0` is non-empty.**

**A-01 — confirmed OPERATIVELY_DECIDED.** *Construction 1 (D):* state exposed with no owner attribution; `view(n)` returns exactly SP-019's members. Conforms. *Construction 2 (A, "Ritual owns state"):* the value is stored on the SP-017 Ritual object; `view(n)` returns the same members, no eighth field. **This also conforms** — SP-093 licenses "differing internal object graphs" and SP-103 defines L-facts as *observable*, so an unexposed ownership relation is not an L-fact. The candidate's stated ground for A's inadmissibility is therefore wrong, but D and A are observationally identical, so they are **not materially different**. B is excluded because a state-bearing Entry in the durable set makes `entries.count = 2` on the founder vector, failing SP-094, and SP-030 says begin "creates no Entry"; C is excluded by SP-040, SP-053 and SP-075, which all carry a single scalar state. Outcome survives on materiality rather than on the cited ground.

**A-02 — confirmed OPEN; justification wrong.** *Construction 1 (A, one predicate two projections)* and *Construction 2 (B, distinct causally coupled facts)* both satisfy SP-018 and SP-101 ("Both readings are admitted"). I attacked A with `⟨…, complete, ⟨boundary⟩⟩`, where SP-053 makes "complete becomes idle" while SP-049 keeps `entries[0].status = complete`; a projection may be a function of the predicate plus the cycle coordinate, so **the attack failed and A survives**. *Construction 3 (C, distinct completion scopes):* v0.4 newly declares C inadmissible as positing "a scope-identity fact SP-019 does not carry". But SP-034 already says "success changes current state to complete, **causes one complete Entry per pending contribution to exist**", and the scope identity is carried by SP-019's DaySlot ordinal plus SP-024's "the active interval associated with that DaySlot", SP-075 and SP-053's "origin DaySlots". **C is admissible and conforming.** v0.3 had this right; **v0.4's correction is a regression.** MINOR.

**A-03 — confirmed OPEN; the reclassification is sound, and it is not wrong in the widening direction.** *Construction 1 (A):* the pending contribution bears Entry identity from creation; `complete` transitions its status. *Construction 2 (B):* the contribution is a non-Entry; `complete` creates the Entry. Both conform — SP-026 says "Both models are **normatively admitted**", SP-022 defers expressly, SP-140 voids any FT row discriminating them. C is genuinely excluded by SP-022's "**creates**" and SP-030's "creates no Entry". `Adm = {A,B}`, `T` = YES for both → branch 1 → OPEN. `PARTIALLY_DECIDED` was reachable only under v0.2's rule. The exclusivity-conjunct restoration is **inert for this item** (with two YES members only branch 1 fires); its real effect is the `CR4-08` overlap on the five singletons.

**A-04 / A-05 / A-06 — confirmed OPERATIVELY_DECIDED, each on a ground independent of SP-019's falsified exhaustiveness.** A-04: SP-070 closes the ordering-fact list at three and SP-120 places the civil mapping in input construction, so a conforming timezone variant is immaterial. A-05: SP-029 is an *existence* prohibition, and SP-070, SP-110 and SP-048 independently exclude an orthogonal authority layer; the only surviving variant is SP-093-erasable. A-06: SP-048 ("no fourth state-changing operation is admitted") and SP-025 (immutability) exclude B and C on their face. **These four should not be re-decided.**

**A-07 — DIVERGES. I derive PARTIALLY_DECIDED.** §13.1 poses a **compound** question — "does RC-0001 admit an invocation-capability precondition, **and how is capability loss accounted for**" — and the admissible-alternatives cell answers only the first conjunct. §13.2 concedes this in prose ("the accounting half of A-07 is therefore an authored installation awaiting adjudication, **not a closed question**") while the label and the summary tally treat the compound question as closed.

*Gate conjunct — decided; I agree.* (b) and (c) violate SP-130, SP-039 and SP-131; (c) additionally violates SP-094's four-element vector. `Adm(gate) = {(a)}`.

*Accounting conjunct — not decided.* The two constructions are **α** (fine-grained loss-class vocabulary: `PENDING_CAPACITY_1` vs `CANONICAL_ORDERING_UNSUPPORTED`, so SP-152 reports divergence) and **β** (coarse vocabulary: both declare `SECOND_RECORD_UNSUPPORTED`, so SP-152 reports conformance) — the construction established at `CR4-01`. Both satisfy SP-150, SP-151, SP-152, SP-155, SP-156, SP-157. They are materially different: on the identical presented sequence they yield **opposite conformance verdicts for the same pair of substrates**, an SP-092 divergence on normalization and acceptance predicates, not SP-093-erasable.

Branch 2 fires: YES for (a)+α and (a)+β, NO for every (b)/(c) variant → **PARTIALLY_DECIDED**, with (b) and (c) listed as excluded.

*Falsified by:* reading SP-151's closing sentence as normative injectivity rather than as the consequence-claim its "therefore" signals. That reading kills β — but it then imposes a **joint** obligation across two independently authored, embodiment-local vocabularies with no registry and no granularity rule, which neither embodiment can discharge unilaterally, converting a decided question into an unsatisfiable clause and a hidden semantic input. Either horn defeats `OPERATIVELY_DECIDED`.

**A-08 — confirmed OPEN, and the docket's best-handled item.** *Construction 1 (a):* an embodiment containing a non-generative classifier conforms. *Construction 2 (b):* an embodiment containing no AI conforms. SP-166 states there is no clause of the form "an embodiment containing X is nonconforming" for any register member — I verified this by exhaustive sweep of the SP rows. §13.2's disclosure that A-08 is open **by inertness** is candid and correct. One MINOR blemish: (c) is withdrawn as "extensionally identical to (a)" via *intersection*, while §13.2's next paragraph reads the register **conjunctively** (a union, i.e. (b)). The withdrawal is right either way; the stated ground is not.

**Open decisions given operative force.** I swept every SP row carrying A-02, A-03 or A-08. **A-08: clean.** **A-02: clean** — SP-101 affirmatively guards both readings. **A-03: one non-neutral phrasing** — SP-034's "causes one complete Entry per pending contribution to exist" reads, on one parse, as deciding that the Entry comes into existence at `complete`; SP-026's express admission of both models forces the other parse for clause-set consistency, so this is not operative force, but SP-034 does not defer the way SP-022 does. MINOR.

**A distinct observation, offered to the founder rather than as a finding.** SP-112, SP-152, SP-121 and SP-091 together make any *observable* difference between two jointly admitted alternatives a conformance failure. So every genuinely OPEN item is open only in unobservable internal structure. v0.4 discloses this for A-08 and not for A-02 or A-03. On a `PASS` the founder surface would be three questions with no observable consequence in this SemanticProgram; the disclosure A-08 receives is owed to all three. I could not construct a trace refuting this, and flag it as a reading rather than a proof.

---

## 7. The §16.4 auditor

### 7.1 My independent run

Copy 1 (document lines 666–780), extracted and run by me against v0.4:

```
ENVELOPE_HEADINGS      1 (must be exactly 1)
NORMATIVE_SP_ROWS      102        UNIQUE_IDS 102        DUPLICATE_IDS NONE
SHAPE_VIOLATIONS       NONE       DISCLOSED_CONFLICTS NONE
ROWS_OUTSIDE_ENVELOPE  NONE
REL_DIST               {'EXACT': 11, 'ELABORATES': 84, 'ORTHOGONAL': 7}
EXACT_ROWS             11 -> [SP-001, SP-004, SP-005, SP-158, SP-018, SP-041,
                              SP-046, SP-090, SP-091, SP-092, SP-164]
FT_ROWS 16 · Q_ROWS 16 · DOCKET_ITEMS 8 · TRAILING_WHITESPACE 0
STRUCTURE_FAILURES     NONE       SHAPE_AUDIT_RESULT PASS
```

Diff mode against v0.3: `ROWS_ADDED 12 · ROWS_REMOVED 0 · ROWS_CHANGED 21 · UNMARKED_CHANGED_ROWS 0 -> NONE`.

**`diff` of my run against §16.5: IDENTICAL, both the 22-line metric block and the 5-line diff block.** I also reproduced the counts by hand without the script (102 unique SP rows from 120 raw matches, EXACT 11, ORTHOGONAL 7, ELABORATES 84; 11+84+7 = 102, and LAYER/CP/LP distributions each sum to 102).

**§16.5's tallies are accurate. Cold Review 003's finding that v0.3's tallies were overstated does NOT recur.** Stated plainly: on this axis v0.4 survives, and the "21 changed / 12 added" enumeration is true.

### 7.2 Proves · counts · cannot do

| Class | Content |
|---|---|
| **PROVES** | field-token arity per SP row (lookahead-guarded, so adjacent duplicate tokens are caught); SP-ID uniqueness within the visible set; presence of the FT/Q/docket surfaces; that the envelope heading string occurs exactly once |
| **COUNTS** | label distributions, row tallies, `EXACT`/`ORTHOGONAL`/`ONTOLOGY` row lists — as tallies, with no verification that any label is true |
| **CANNOT DO** | reach L1, custody, or any prior version except the optional diff argument; establish source fidelity, semantic entailment, or state-machine determinacy; establish that a relation label is TRUE |

The header comment is **substantially honest** — markedly better than v0.3's — with two inaccuracies. It **overclaims** "envelope well-formedness": the only test is `nhead == 1`, which does not check the envelope has a body or coherent structure. It **under-admits** in the other direction: `REPRESENTATION_HITS` is a *content-vocabulary* check and a hard FAIL condition, so a content judgment ships inside a gate disclaimed as shape-only. Not admitted anywhere: diff mode is **optional**, and the prior-version argument is **entirely unauthenticated**.

### 7.3 The new positive checks are gameable

All five are presence tests with threshold ≥ 1 (`nhead != 1`, `not sp`, `ft == 0`, `q == 0`, `dk == 0`). **There is no expected-count assertion anywhere** — nothing pins 102 SP rows, 16 FT rows, 16 Q rows or 8 docket items. PROBE-A2 (empty file) now FAILs, but the gap between "empty" and "correct" is one row per surface. A five-line document consisting of one SP row, one FT row, one Q row, one docket row and the envelope heading returns `SHAPE_AUDIT_RESULT PASS`.

**Can it PASS while the document is semantically broken? Yes.** Three concrete constructions:

1. **The barrier clause can be inverted with no marker required.** `MARKER` is searched anywhere in the current row and is **not per-revision**, so any row that already carries a marker is exempt forever — **12 of the 21 changed rows already carried one in v0.3**. Inverting SP-152 from "conform only if … the same disposition" to "conform even if … a different disposition" yields `ROWS_CHANGED 1 -> ['SP-152'] · UNMARKED_CHANGED_ROWS 0 -> NONE · PASS`. **§0.5 row 8 and §16.2 rate CR3-05 `IMPOSSIBLE`; that rating is not earned.**
2. **An adjudicating Operator can be reintroduced.** Adding a row establishing a contested assertion and its binding adjudication moves `ONTOLOGY_ROWS` from 6 to 7 — **listed, not failed**, because the PROBE-A9 verdict withdrawal removed the only teeth. §16.3 claims this prohibition is "Not reintroduced by any repair here"; the auditor cannot check that.
3. **An unaudited `EXACT` claim can be manufactured.** Promoting any already-marked row from `ELABORATES` to `EXACT` yields `EXACT_ROWS 12` and `PASS`, falsifying §17.1's own coverage-boundary claim — "exactly the eleven rows the auditor enumerates in §16.5 plus nothing else" — which is the remedy §17.1 offers for CR3-16.

Additional holes verified: `ROWS_REMOVED` and unmarked `ROWS_ADDED` are **not failure conditions** (SP-001 can be deleted, or a permissive row added unmarked, and both PASS); the diff base is unauthenticated (passing the document as its own prior, or an empty file, satisfies the CR3-05 check trivially); the row scanner is defeated by **one leading space** or a four-digit ID, silently dropping a clause from the normative envelope while leaving it visible to every human reader; smuggled-clause detection requires **all four** metadata fields, so omitting one makes a post-envelope clause invisible; and any `A-` plus two digits satisfies the docket cross-reference, including a nonexistent `A-99`.

**Fence handling.** The stripping regex deletes any SP row inside a fenced block with no diagnostic, so a clause placed in §2.0's diagram fence or §6.1's witness fence is invisible to the auditor while reading as normative to a human. And because line 781 (`CR4-03`) begins with three backticks, the auditor's fence pairing is **offset from the rendered document for the remainder of the file** — the auditor's own comment states the intended invariant ("a row-shaped line inside a code fence is not a clause"), and from line 781 onward that invariant is inverted.

**In fairness:** §16.4's probe table is accurate on every row I tested, and the rebuilt auditor genuinely catches the empty file, the duplicated envelope heading, four-field smuggled rows, duplicate field tokens, duplicate IDs and representation leakage inside SP rows. It is a real improvement. It is simply not a semantic instrument — exactly as its own header says.

### 7.4 §16.6's non-row declaration is incomplete

§16.6 declares non-row changes "by hand" because the diff covers SP rows only. A section-level comparison against v0.3 finds **five changed regions absent from that list**: §0.2's source pins (two rows added, one Layer cell changed), §0.5 (entirely rewritten), §4.0 (header changed and a sentence appended — §16.6 declares §3.0, §4.2, §6 and §8 headers but not §4.0), **§11's lead paragraph** (rewritten; §16.6 declares only "§11.1's derivation table"), and the document header block (four new fields). §11 is *"Founder-sealed trace and acceptance predicates"* — the home of the acceptance predicate. **This is the species of defect CR3-05 named: text edited under a completeness assurance.** MATERIAL. *Falsified by:* showing the list was illustrative rather than exhaustive; its phrasing reads as exhaustive to me, but that is a reading.

---

## 8. Cold Review 003 regression — every finding

**13 CLOSED · 6 PARTIALLY_CLOSED · 1 NOT_CLOSED · 0 REGRESSED.** Mechanisms were tested, not the presence of language describing them.

| Finding | Disposition | Test that produced it |
|---|---|---|
| **CR3-B01** | **CLOSED** | §2. CR-003's day-2 trace re-run: reporting count 1 over a four-element sequence with zero `INVALID_TRANSITION` elements now contradicts SP-043's definitional form. Scope, initial value and reset point all supplied by normative rows |
| CR3-01 | **CLOSED** | SP-091 reduced to the founder's sentence; the authored comparison rule split into SP-095 (`AUTHOR-PROPOSED`). Verified. The same defect *class* survives at SP-005 — recorded as fresh `CR4-04`, not as a CR3-01 failure, because CR3-01 named SP-091 |
| CR3-02 | **CLOSED** | §7.1's T-fact law restated as a function of presented sequence **and** capability resolution; §14 Q9–Q12 re-cited to normative clauses. Verified. SP-121 carries the same error form — fresh `CR4-11` |
| CR3-03 | **PARTIALLY_CLOSED** | §17.3 now hand-justifies all seven `ORTHOGONAL` rows and reclassifies two; the regex is demoted to a count. But SP-029's justification rests on a premise L1 falsifies — `CR4-12` |
| **CR3-04** | **NOT_CLOSED** | `CR4-01`. `CAPABILITY_DEGRADED` is genuinely withdrawn and the loss class genuinely enters SP-152 — but the vocabulary is embodiment-local and ungoverned, and CR-003 §3.5's G′/H′ pair reconstructs as G″/H″ comparing **equal**. Claimed `IMPOSSIBLE`; it is not |
| CR3-05 | **PARTIALLY_CLOSED** | Deleted text restored to SP-050, SP-071, SP-113; SP-112 repaired; four false headers corrected; `UNMARKED_CHANGED_ROWS 0` reproduced by my own run. But the marker check is vacuous for the 12 of 21 rows already marked in v0.3, additions and removals are unchecked, the diff base is unauthenticated, and §16.6's non-row list omits five regions including §11. Claimed `IMPOSSIBLE`; not earned |
| CR3-06 | **PARTIALLY_CLOSED** | SP-157 does separate the coordinates and I could not misalign the element-keyed comparison. But §15's "neither is called 'position' unqualified" is falsified by ten normative uses, and `view`'s domain is specified three inconsistent ways — `CR4-10` |
| CR3-07 | **CLOSED** | SP-162 fixes presence as supply; I traced every downstream consumer (SP-160 step 2, SP-032, SP-033, SP-034, SP-035, SP-043, SP-020, SP-021) and found no refusal-precedence hole and no predicate an empty-content Entry satisfies that it should not. CR-003's E1/E2 divergence is unavailable. A residual gap — no clause defines the content **value domain**, leaving a supplied sentinel undetermined — is real but speculative, and I record it here rather than reopening the finding |
| CR3-08 | **PARTIALLY_CLOSED** | SP-096 genuinely declares the singleton bound. But SP-155 makes misreporting *unlawful*, not *detectable*: RC-0001's instruments (SP-013, SP-114) do not reach substrate ground truth, so two embodiments that can both admit an element and both dispose it unsupported are indistinguishable in observation. §16.2 claims "Two embodiments can no longer conform by both misreporting" while §18.2 residual 7 concedes the obligation "is not mechanically checkable". Both cannot be true. Claimed `EXPLICITLY_DETECTABLE`; not earned |
| CR3-09 | **CLOSED** | SP-041 reduced to reproduction of L1's two registers; SP-163 carries the mapping as `AUTHOR-PROPOSED` and discloses that the `record` self-loop appears in no pin. I enumerated the 3×3 domain: total, unambiguous, no operation with zero or two edges |
| CR3-10 | **CLOSED** | §11.1 split — five L-facts from SP-110, the sixth from the SP-013 witness stream. Structurally correct: SP-110's codomain is the L-fact set and SP-102 places the count in the T-fact set |
| CR3-11 | **CLOSED** | SP-164 reproduces law 2 verbatim (verified against P-L1-B:34); SP-165 states the authored consequence and is correctly labelled |
| CR3-12 | **CLOSED** | SP-158 reproduces law 5 verbatim (verified against P-L1-B:37); SP-159's premise — that RC-0001 contains no authorization mechanism — verified. Minor quotation residue at `CR4-M2` |
| CR3-13 | **CLOSED** | SP-156 makes `ADMITTED` a boundary's only lawful disposition. I enumerated the disposition space: invocation → {`ADMITTED`, `CAPABILITY_UNSUPPORTED`}, boundary → {`ADMITTED`}. Exhaustive, no gap. For a boundary an embodiment cannot admit, SP-156 and SP-159 both lead to nonconformance, which is the correct outcome |
| CR3-14 | **CLOSED** | SP-018's citations withdrawn from §16.1 S-02 and §10 and re-pointed to SP-041/SP-163. Verified in place |
| CR3-15 | **PARTIALLY_CLOSED** | SP-004, SP-005, SP-046 and SP-092 were the four named rows. SP-004 and SP-092 are repaired to normalization-only residue. **SP-005 still carries authored law** (`CR4-04`) and **SP-046 still promotes modality** (`CR4-06`), both under `EXACT`. §17.2 is rewritten accurately, but §17.1's own tally miscounts (`CR4-M1`) |
| CR3-16 | **CLOSED** | §10's Ledger·Ritual relation reclassified to `ELABORATES`; my independent sweep confirms all 11 `EXACT` judgments are SP rows inside §17.1's audit, with none outside |
| CR3-17 | **PARTIALLY_CLOSED** | §16.5 is byte-reproducing — I verified by `diff` against my own run. But the published script **does not execute** (`CR4-03`), so the reproduction the section invites cannot be performed as instructed |
| CR3-18 | **CLOSED** | Three non-discriminating falsifiers withdrawn; the discriminating one retained; §12.2 downgraded to `PARTIALLY_CLOSED`; the uncoverable residual named; §14 Q14's citation withdrawn. The gap is recorded rather than concealed, which is what the finding asked for |
| CR3-19 | **CLOSED** | SP-166 states the register's operative status; §13.2 discloses A-08's openness by inertness; S-06 marked `PASS as REPRODUCED, not as ENFORCED` |
| **CR-001 CR-09 regression** | **CLOSED** | The rename to `SHAPE_AUDIT_RESULT` and the "row grammar and nothing else" disclaimer are both restored, and the disclaimer now lives inside the program so output and bound cannot be separated. Header-accuracy residue at §7.2 |
| **CR-002 residue** (B.2-F7, B.4·SP-041, B.4·SP-001, A-03) | **CLOSED** | All four dispositioned in §16.2 and traceable to CR3-02, CR3-09, §17.1's declared SP-001 residual and §13.1 respectively |

---

## 9. PASS-threshold table

| Condition | Required | **Determination** | Basis |
|---|---|---|---|
| CR3-B01 | CLOSED | **MET** | §2 |
| all other CR003 findings | CLOSED | **NOT MET** | 1 NOT_CLOSED (CR3-04), 6 PARTIALLY_CLOSED |
| new blocking findings | 0 | **NOT MET** — 1 | `CR4-01` |
| L1 contradictions | 0 | **MET, qualified** | No clause contradicts L1 on a reading I can establish. SP-029 is contradictory on its literal reading but survives on an available scope reading; the *justification* is false either way (`CR4-12`) |
| hidden semantic inputs | 0 | **NOT MET** | The embodiment's published capability declaration (`CR4-01`); the content value domain (§8, CR3-07 residual) |
| docket truth | accurate | **NOT MET** | A-07 mislabelled; §13.0's partition claim false; the filter's exhaustiveness ground falsified; A-02's correction a regression |
| silent capability loss | impossible / detectable | **MET** | Attacked SP-150 totality, SP-151, SP-154, SP-038 and SP-055; found no route by which a presented element leaves no trace. `CR4-01` is *untyped* loss, not *silent* loss |
| capability ≠ permission | preserved | **MET** | SP-153, SP-131, SP-105, SP-130 hold; the Operator gate is not restored; SP-159 closes the adaptation route |
| founder vector | self-sufficient | **NOT MET** | `CR4-02` (DaySlot coordinate); `CR4-10` (acceptance values evaluated pre-restart); `CR4-M5` (four unbound acceptance tokens) |
| L/T non-interference | preserved | **MET** | SP-103, SP-104, SP-105 hold; the count is a T-fact consistently everywhere; SP-105 forbids any transition evaluation reading a T-fact |
| ordered admission | preserved | **MET, qualified** | The mechanism holds; SP-121's stated *reason* is false under the disposition regime (`CR4-11`) |
| restart semantics | coherent | **NOT MET** | `CR4-10` — `view`'s domain is specified three inconsistent ways and §6.1/FT-10's `view(n+1)` does not exist under SP-157 |
| provenance relationships | substantively valid | **NOT MET** | `CR4-04`, `CR4-05`, `CR4-06` |
| local source packet | sufficient | **MET** | All ten governance artifacts and the L1 container available and digest-matched locally; all three pins extracted |
| transport custody | not used as semantic evidence | **MET** | §0.2 |

**8 of 15 met.**

---

## 10. Verdict

```
COLD REVIEW 004               CHANGES_REQUIRED

CR3-B01                       CLOSED
NEW BLOCKING                  1   (CR4-01)
NEW MATERIAL                  7   (CR4-02 … CR4-12)
NEW MINOR                     5   (CR4-M1 … CR4-M5)
CR003 REGRESSION              13 CLOSED · 6 PARTIALLY_CLOSED · 1 NOT_CLOSED · 0 REGRESSED
DOCKET (derived)              3 OPEN · 1 PARTIALLY_DECIDED · 4 OPERATIVELY_DECIDED
PASS THRESHOLD                8 / 15
```

Not `BLOCKED`: every required semantic source was available locally, and the transport-custody condition — which affects zero clauses — played no part in this verdict.

Not `PASS`: one new BLOCKING finding, one CR-003 finding not closed, and seven threshold lines unmet.

**Had this returned `PASS`, it would have meant only `READY_FOR_FOUNDER_ADJUDICATION`.** A `PASS` from this review would not ratify the SemanticProgram, would not seal it, and would not authorize extraction, representation selection, RealityIR, implementation or RC-0001 execution. It does not return `PASS`, so none of that arises.

**What v0.4 got right, recorded so the record is not one-sided.** The blocker is genuinely closed by mechanism. §16.5's tallies are accurate and byte-reproducible — the defect Cold Review 003 found there does not recur. SP-090 is exact and unbreakable on all nine attacks. CR3-09, CR3-13, CR3-16 and CR3-18 are mechanically closed. The `EXACT` set is fully enumerable and fully audited for the first time. §18.2's declared residuals are honest, and §12.2's refusal to overstate FT-11's closure is the right posture. The three MATERIAL provenance findings are **recurrences of the CR3-01 and CR3-15 classes at rows the repair did not reach** — a scope failure in the repair, not a regression in method.

---

## 11. Self-limitation

**What I did not test.** RealityIR, emitter, oracle or target-layer questions (out of scope). The commission's procedural conformance beyond the clauses cited. Whether any alternative loss-class governance exists elsewhere in the corpus outside my evidence set. The content value domain question (`CR3-07` residual) rests on positing a sentinel value; I flagged it rather than grading it. I did not attempt an exhaustive mutation search of the auditor — my sample of gaming constructions is illustrative, not complete. I did not verify v0.2 or v0.1 beyond their digests. I read no session transcript, no other job directory, and no narrative-of-the-author document.

**Where I nearly recorded a false positive, disclosed.** §18's exit-gate line "HBC `e350205` intact — 30 tracked, 0 modified, 0 staged" does not verify against the RUORA governance repository, whose HEAD is different, which has 196 tracked files and one modified tracked file. I was one step from recording it as a defect. On investigation **HBC is a separate child repository** at `projects/hbc-html`, whose actual state is HEAD `e350205f12c140b8216090b935f874cbbc454dee`, 30 tracked, 0 modified, 0 staged, only `output/` untracked. **The claim is TRUE and the finding was killed.** I record this because a fabricated defect costs as much as a missed one.

**What non-model-independence means here.** I share an architecture with whatever authored v0.4. My **positive** results — the `CR4-01` trace, the `CR4-02` construction, the `CR4-03` SyntaxError and byte-diff, the `CR4-05` and `CR4-04` byte comparisons against extracted L1, the `CR4-08` quantifier analysis, the `CR4-09` trace — are re-verifiable by anyone in minutes and do not depend on my reasoning being sound. My **negative** results — CR3-B01's six attacks surviving, silent capability loss remaining impossible, capability ≠ permission preserved, L/T non-interference holding, no two-embodiment divergence on sequence extent — are **weak evidence**, because I may share the blind spots of the author. A model-independent or external review could plausibly break what I could not.

**Transport custody.** Not used as semantic evidence at any point, in either direction. The corpus's untracked state is the pre-existing BC-001-BOUNDARY condition and underwrites no finding, no disposition and no threshold determination in this document.

---

## 12. Integrity block

**All artifacts byte-unchanged at close**, independently recomputed:

```
v0.4 SUBJECT      7c680b0286d79f8c6af162223bdfe62789f0123a5e28e28dcf855873df2cf48f  UNCHANGED
v0.3              55c590ead44e38248a7f97405c8cb23740018df4bd9b154a8a0fd3df99dd7f8e  UNCHANGED
v0.2              611a782e7abdf323de6567497d4da372ff011142d44de16c6f53c2a9d1feb007  UNCHANGED
v0.1              3e675d9ebd1e8bbb25193625ef9ca784146d8d639e57d5f5fe9dfaee46551537  UNCHANGED
COLD REVIEW 001   54de4a52ffa4f63086cbc19d30e7d7beb49b5c61cc1b37a2605da187e626276f  UNCHANGED
COLD REVIEW 002   bdd8c218ade5e37f0b23605ec2f789ae6f72b74855aa036eb9905039fc46167e  UNCHANGED
COLD REVIEW 003   d9afbcb47f9813430ea763126f80aa25e617012ef80aa6996e0c03d33dc848b1  UNCHANGED
SLR-01-R1         a506352ae82bd889034b5972dc2b090185aac3c6ac58f6bbc083f7d4614e68c6  UNCHANGED
SOURCE-CUSTODY-001 0f61f7bb41ccdb74d00cb679f00df36b74d4221398835068bb4e5bf388734600 UNCHANGED
AUTHORING COMMISSION 9a04124a25ec3dc9c281d73a4f6bce7ecb7a0619a0d9890f9a51fd5ce5dcc04e UNCHANGED
L1 CONTAINER      cee97abe168b011e8cc2bf1d69009d755f8c744998302c76743ac432a7d81ebe  UNCHANGED, read-only
```

```
FILES CREATED BY THIS REVIEW   1
    governance/OURSELF-RCP-RC0001-SEMANTICPROGRAM-v0.4-LINEAGE-INDEPENDENT-COLD-REVIEW-004.md
SCRATCH                        /Users/millysituated/.claude/jobs/fcf1e66c/tmp/  (read-only analysis only)
GIT INDEX                      NOTHING STAGED  (git diff --cached → 0 entries)
GIT OPERATIONS                 NONE — no add, commit, push, branch or tag
CANDIDATE EDITED               NO        PRIOR ARTIFACTS EDITED   NO
REPAIRS PROPOSED               NONE      CLAUSE TEXT AUTHORED     NONE
L1 CONTAINER                   READ ONLY — never copied, imported, or written to
SECRET-BEARING MATERIAL        none read, printed, or requested
REPOSITORY BOUNDARY            not expanded beyond /Users/millysituated/RUORA
```

**One working-tree observation, reported rather than adjudicated.** `git status` shows ` M doctrine/self_axiom.md` — a tracked file outside `governance/`, modified in the working tree. Its mtime is **2026-08-01**, twelve days before v0.4 was authored and before this review began; I did not touch it, and it bears on no finding here. The HBC child repository is clean at its declared baseline (§11).

---

*A count that is scoped to the sequence it is derived over is a measurement. That repair holds.*

*But a type whose extension is chosen by the party being measured is not a type. It is a courtesy.*
