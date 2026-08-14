# RC0001-SLR-01-R1 — CORRECTED SOURCE-LINEAGE RECONCILIATION

**STATUS** `RECONCILIATION_COMPLETE` · two principal verdicts returned
**FOUNDER ACT** 2026-08-13: *"Authorize SLR-01-R1, but with one precondition: do not let the defective §3 normalization become the authority surface."*
**AUTHORITY** Read-only lineage adjudication + this one new artifact.
**AUTHORITY LIMIT** No candidate repair · no relocation · no commission amendment · no SemanticProgram authorship · no cold review · no implementation · no HBC mutation · no staging · no commit · no seal.
**SUPERSEDES** `SLR-01` (`4d42d83b…c508d2f`) as the operative lineage reconciliation. SLR-01 is preserved unmodified and cited as derived evidence.

---

## 0. Governing source precedence

This reconciliation judges against the raw pinned founder record, not against any summary of it.

```
1  PINNED RAW FOUNDER RECORD      controlling evidence
2  SOURCE-CUSTODY-001             custody/provenance witness only;
                                  NOT authoritative where its normalization
                                  omits source material
3  AUTHORING COMMISSION           authoring procedure and required questions
4  CURRENT CANDIDATE              subject being classified
5  SEMANTIC REVIEW · SLR-01       derived evidence only
```

**Carried correction, as directed:**

> `SOURCE-CUSTODY-001` §3 is incomplete as a normalization. Its omissions do not diminish the authority of the byte-pinned founder source.

### 0.1 Evidence pins

```
RAW FOUNDER RECORD    cee97abe168b011e8cc2bf1d69009d755f8c744998302c76743ac432a7d81ebe
                      494995 bytes · 93 records · 2026-08-12
  FS-A ordinal 59     4cfd687b2ea9cdbcf366c29a60b124e76cf0f9cce9fb4de897d812b69b3f4bb5
  FS-B ordinal 72     796a3588fbd8fbc611b62f6bba2267d462dd42f92f865a876f82e3387190e221
  FS-C ordinal 85     e951c1bc4f3fdb0fdfe4f133624acfd521dfedb7240bbdb80a0fe4147d82b8e3
SOURCE-CUSTODY-001    0f61f7bb41ccdb74d00cb679f00df36b74d4221398835068bb4e5bf388734600
AUTHORING COMMISSION  9a04124a25ec3dc9c281d73a4f6bce7ecb7a0619a0d9890f9a51fd5ce5dcc04e
CURRENT CANDIDATE     72a1bf7f869b76057e65d07884d1c0d35f6d8794b4acb87fe9428acf48ff3a47
SEMANTIC REVIEW       d478350af4ca2feafa26e3f41d9525bd91c2bc5042006022aab296afc784b438
SLR-01                4d42d83b7c30a9fc785b83962e0264b6d8610fe4fe744fb9a7c10fc2bc508d2f
EXTRACTION BLOCKER    6f254f7f0e2c77de4c020900075de1733d27cf8147832357b41a705526bef917
RCP v0.1 DRAFT        1aa3698c29ca9d471390d8943ab64afd7e5a5d943645062fe64451ba0938c776
```

All three founder-message digests were independently recomputed by the method `SOURCE-CUSTODY-001` §1.2 states — UTF-8 text value, blocks joined with one LF, no terminal LF — and all three reproduce exactly. All five custody excerpts are byte-exact substrings of their designated source and of no other.

---

## 1. The source hierarchy is four founder layers, not two

The previous work treated "founder source" as one thing. It is four, and the distinction is the whole finding.

```
L1  FOUNDER-SEALED SCOPE        2026-08-12   FS-A / FS-B / FS-C
                                Ritual · Entry · idle → active → complete ·
                                begin · record · complete · invalid transition
                                law · durability · canonical ordering ·
                                restart preservation · equivalent state traces ·
                                acceptance predicates · prohibitions · non-goals

L2  WRITTEN AUTHORING COMMISSION 2026-08-13  9a04124a…dcc04e
                                authored by a session that did not admit L1

L3  IN-SESSION FOUNDER DIRECTION 2026-08-13  this session's commissioning message
                                Ledger · Ritual · RitualOccurrence ·
                                PlannedOccurrence · CompletionObservation ·
                                Correction · Day · Participant · Observer ·
                                AuthorityDecision · ten operations · six statuses ·
                                the observer septuple · three discontinuities

L4  LATER FOUNDER ACTS           2026-08-13  hold · SLR-01 · custody · this R1
```

**L3 does not contain L1's vocabulary. L1 does not contain L3's.** Neither the commission nor the candidate ever had L1 in view. The candidate is a faithful elaboration of **L3**.

### 1.1 The mechanical proof

Whole-word counts, case-insensitive, computed over the pinned sources.

| L1 sealed member | raw source | candidate | commission |
|---|---:|---:|---:|
| `Ritual` | 4 | 23 | 13 |
| `Entry` | 2 | **0** | **0** |
| `idle` | 2 | **0** | **0** |
| `begin` | 4 | **0** | **0** |
| `invalid transition` | 1 | **0** | **0** |
| `canonical ordering` | 2 | **0** | **0** |
| `equivalent state traces` | 1 | **0** | **0** |
| `acceptance predicates` | 3 | **0** | **0** |
| `state normalization` | 2 | **0** | **0** |
| `durability` | 1 | 1 (named, undefined) | 0 |
| `restart` | 4 | 2 (as `D-a`) | 0 |

| candidate construct | candidate | raw source | commission |
|---|---:|---:|---:|
| `Assertion` | 43 | **0** | **0** |
| `Actor` | 41 | **0** | 1 |
| `Reporter` | 16 | **0** | **0** |
| `ESTABLISHED` | 18 | **0** | 1 |
| `REPORTED` / `UNREPORTED` | 10 / 8 | **0** | 1 / 0 |
| `supersede` | 6 | **0** | **0** |
| `CONTESTED` | 3 | **0** | **0** |
| `Establishment` | 3 | **0** | **0** |
| `Day` | 49 | **0** | 5 |

The two vocabularies are very nearly disjoint. The single sealed entity `Entry` — one of only two entities the founder named — appears nowhere in the candidate or the commission.

### 1.2 Where the substitution actually happened

Every clause the candidate marks `FOUNDER-DIRECTED` traces to **real founder text in L3**, and **none** of it to L1:

| candidate `FOUNDER-DIRECTED` content | L3 | L1 |
|---|---:|---:|
| `scheduled` / `performed` / `accepted as authoritative` chain | 2 / 3 / 1 | 0 / 0 / 0 |
| `exactly one answer` stands | 1 | 0 |
| observer septuple (`WHO MAY REPORT`, `WHO MAY AUTHORIZE`) | 1 / 1 | 0 / 0 |
| `page reload` · `process restart` · `device restart` | 2 / 2 / 2 | 0 / 0 / 0 |
| `CONTESTED` · `ESTABLISHED` · `ACCEPTED` · `PROPOSED` | 5 / 17 / 14 / 23 | 0 / 0 / 0 / 0 |

**The candidate did not fabricate provenance.** It cited founder direction that exists. The defect is that the commission's four-class taxonomy has no term for *"founder-directed later, and unreconciled with founder-sealed scope."* `FOUNDER-DIRECTED` covers both L1 and L3 identically, so a later direction that displaces sealed scope is marked exactly like the sealed scope it displaces.

**That taxonomy gap is the mechanism by which the substitution became invisible.** It is why the nine-class scheme this movement was given is load-bearing rather than bureaucratic.

---

## 2. Custody findings

### SLR-R1-CUSTODY-01

```
FINDING     SOURCE-CUSTODY-001 §3 omits founder-sealed material present
            in its own pinned source:
              · the prohibition list — no auth · no cloud · no camera ·
                no generative AI · no networking
              · the seven scope-creep non-goals
              · acceptance predicates
CLASS       DERIVED NORMALIZATION OMISSION
EFFECT      §3 cannot be used as an exhaustive founder-scope register.
SOURCE      unaffected — pinned founder excerpts remain available.
AUTHORITY
```

Verified mechanically: each term occurs in the pinned source, and **zero** times in the custody record's own normative voice once the verbatim §2 excerpt blocks are excluded.

### SLR-R1-CUSTODY-02 — larger, and not previously reported

The omission is not confined to §3. **The §2 excerpt set itself drops founder-sealed RC-0001 material**, so the gap cannot be repaired by reading custody's excerpts more carefully.

Absent from all five excerpts:

```
FS-B  the seven constitutional laws — including law 4:
      "Emitters may translate representation, not law. Authority, invariants,
       transition legality, and acceptance predicates survive intact."
FS-B  the spinal law:
      "One canonical semantic program, interpreted by one normative operational
       model, produces equivalent observable state traces across materially
       different substrates."
FS-B  THE CONCRETE RC-0001 CONFORMANCE VECTOR (below)
FS-C  the Pass condition: reference trace = normalized Web trace =
      normalized iOS trace, for every required vector
FS-C  the four-field stage contract: INPUT · OUTPUT · INVARIANTS ·
      FORBIDDEN AUTHORITY
FS-A  the authority-non-collapse law: "Founder intent says what is desired.
      It does not silently become permission."
```

The most consequential omission is a **founder-authored conformance vector for RC-0001 itself**:

```
event trace                     oracle requirement
  begin                           state = complete
  record("Reflect")               entries.count = 1
  complete                        entries[0].content = "Reflect"
  restart                         entries[0].status = complete
                                  history_order = canonical
                                  illegal_transition_count = 0
```

```
CLASS       SOURCE OMISSION FROM CUSTODY EXCERPT SET
EFFECT      Custody §4 negative-pins "exact Entry content schema" and
            "complete conformance-vector set" as NOT SUPPLIED. Both are
            literally true — exact, complete — and both are operationally
            misleading: PARTIAL Entry content schema (content, status) and
            ONE concrete acceptance vector WERE supplied by the founder and
            appear nowhere in custody.
SOURCE      unaffected.
AUTHORITY
```

Custody's §2 preamble does disclaim — *"Text outside the excerpts is not imported as subject-specific SemanticProgram law"* — and custody's declared scope was the proof **subject**. That disclaimer covers the general doctrine material. It does not cover the conformance vector, the Pass condition, or `acceptance predicates`, all of which are RC-0001 proof-subject material by any reading.

### SLR-R1-COMM-01

```
FINDING     The authoring commission's §3.1 admitted-source table does not
            include the raw founder record. Its five admitted sources are the
            in-session founder act, the extraction blocker, the NF01/NF02
            counter-falsification, the RCP v0.1 draft, and MASTER_BLUEPRINT
            (negative pin only).
CLASS       SOURCE-ADMISSION GAP
EFFECT      Commission §3.2's reasoning — "'Ritual' does not specify obligation,
            completion, refusal, or consequence… These are authoring questions,
            not facts concealed inside the name" — is sound against its admitted
            sources and wrong against the record. The founder HAD specified a
            state progression, three operations, an invalid-transition law, and
            a concrete acceptance vector, one day earlier.
CONSEQUENCE Every artifact downstream of the commission inherited the gap:
            candidate, semantic review, and SLR-01 alike. The lineage break is
            systemic, not authorial.
```

### SLR-R1-REV-01

The semantic review (`d478350a…84b438`) evaluated the candidate against the commission. It could not test scope fidelity to L1, because L1 was not in custody when it ran. Its twenty-five findings remain valid within their frame and are **not** re-litigated here. Its frame is now known to be incomplete.

---

## 3. Reconciliation 1 — proof-subject scope (source facts)

These are facts about what the founder said. They are not judgments about the candidate.

| Sealed element | Class | Direct source |
|---|---|---|
| Proof identity `RC-0001 · Dual-Substrate Semantic Preservation` | `FOUNDER_SEALED` | FS-A |
| Proof subject `Durable Daily Ritual Ledger` | `FOUNDER_SEALED` | FS-A, FS-B |
| Entity `Ritual` | `FOUNDER_SEALED` | FS-A, FS-B |
| Entity `Entry` | `FOUNDER_SEALED` | FS-A, FS-B |
| Progression `idle → active → complete` | `FOUNDER_SEALED` | FS-A, FS-B |
| Operation `begin` | `FOUNDER_SEALED` | FS-A, FS-B |
| Operation `record` | `FOUNDER_SEALED` | FS-A, FS-B |
| Operation `complete` | `FOUNDER_SEALED` | FS-A, FS-B |
| Invalid-transition / transition-legality law | `FOUNDER_SEALED` | FS-A, FS-B, FS-C |
| Durability / persistence semantics | `FOUNDER_SEALED` | FS-A, FS-B, FS-C |
| Restart preservation / behavior / semantics | `FOUNDER_SEALED` | FS-A, FS-B, FS-C |
| Canonical ordering | `FOUNDER_SEALED` | FS-A, FS-B, FS-C |
| Equivalent observable / normalized state traces | `FOUNDER_SEALED` | FS-A, FS-B, FS-C |
| Failure semantics | `FOUNDER_SEALED` | FS-B, FS-C |
| State normalization | `FOUNDER_SEALED` | FS-B, FS-C |
| **Acceptance predicates** | `FOUNDER_SEALED` | FS-B law 4, FS-C emitter invariants, FS-C Fail list |
| Entry fields `content`, `status` | `FOUNDER_SEALED` | FS-B vector |
| `history_order = canonical` | `FOUNDER_SEALED` | FS-B vector |
| `illegal_transition_count = 0` | `FOUNDER_SEALED` | FS-B vector |
| Semantic ≠ structural ≠ visual ≠ binary identity | `FOUNDER_SEALED` | FS-B |
| Proof topology (1 program → 2 targets → 1 judgment) | `FOUNDER_SEALED` | FS-C |
| Pass condition: reference = normalized Web = normalized iOS | `FOUNDER_SEALED` | FS-C |
| No auth · no cloud · no camera · no generative AI · no networking | `FOUNDER_EXCLUSION` | FS-A, FS-B |
| Not: beautiful UI · production architecture · App Store readiness · sophisticated Swift · sophisticated React · generalized storage abstraction · reusable design system | `FOUNDER_EXCLUSION` | FS-C |

### 3.1 Pinned semantics — stated only as the founder stated them

Per instruction, these are not backfilled from later protocol vocabulary.

```
durability            The founder wrote "+ durability" and "persistence
                      semantics" and "durable state". The ONLY discontinuity
                      the founder names is restart. No storage mechanism, no
                      survival boundary, and no degradation allowance is stated.
                      SwiftData/Core Data and IndexedDB are named as examples of
                      implementation freedom, NOT as requirements.

canonical ordering    The founder wrote "+ canonical ordering", "canonical
                      ordering", "ordering", and the vector line
                      "history_order = canonical". What is ordered is history.
                      No ordering key, comparator, tie-break, or total-order
                      oracle is stated. The founder did NOT say ordering is
                      by wall clock.

acceptance predicates The founder wrote that acceptance predicates "survive
                      intact" across emitters (FS-B law 4), that emitters must
                      "preserve acceptance predicates" (FS-C), and that their
                      divergence is a Fail condition (FS-C). NO acceptance
                      predicate is itself defined, except by the one worked
                      vector in FS-B.
```

Each of these is `FOUNDER_SEALED` as a **named obligation** and `UNRESOLVED` as a **semantics**. That pairing is the accurate record. Treating the name as the semantics is the error commission §3.2 correctly warned against — and it remains an error in the direction the commission did not anticipate.

### 3.2 The sealed ambiguities — classified, not resolved

```
A-01   Does idle → active → complete belong to Ritual, to Entry, to both,
       or to another semantic object?
       FOUNDER_SEALED TEXT:      YES
       SEMANTIC INTERPRETATION:  UNRESOLVED

A-02   `complete` is listed both as a state and as an operation.
       What is the exact state/action relationship?
       FOUNDER_SEALED TEXT:      YES
       SEMANTIC INTERPRETATION:  UNRESOLVED
```

**Material evidence bearing on A-01, recorded without resolving it.** The FS-B vector distinguishes a top-level `state = complete` from a per-entry `entries[0].status = complete`. Two distinct state-bearing surfaces appear in one founder-authored vector. This is evidence, not a resolution: the vector does not say the top-level `state` is the `Ritual`'s, and one worked example is not a specification. Recorded as `FD-02` in §8.

A third ambiguity follows from the same evidence and is newly raised here:

```
A-03   Is `record` the operation that creates an Entry, and is `entries[]`
       therefore the Ritual's Entry collection?
       FOUNDER_SEALED TEXT:      PARTIAL — the vector shows record("Reflect")
                                 followed by entries[0].content = "Reflect"
       SEMANTIC INTERPRETATION:  UNRESOLVED
```

---

## 4. Reconciliation 2 — authoring obligations (procedure facts)

The commission governs how the candidate must be authored. Its authority over procedure is undiminished by SLR-R1-COMM-01; only its source completeness is affected.

| Obligation | Class | Commission cite |
|---|---|---|
| Exactly one authorized target path | `COMMISSION_REQUIRED` | §2.3 |
| Four-class provenance mark on every normative clause | `COMMISSION_REQUIRED` | §4 |
| Exact source cited for every `FOUNDER-DIRECTED` clause | `COMMISSION_REQUIRED` | §4 |
| No promotion of `AUTHOR-PROPOSED` to `FOUNDER-DIRECTED` by tone or repetition | `COMMISSION_REQUIRED` | §4 |
| Observation and authority modeled separately | `COMMISSION_REQUIRED` | §6.2 |
| Operation refusal **conditions and refusal outcome** | `COMMISSION_REQUIRED` | §6.4 |
| Per-discontinuity survival, destruction, ordering, permitted degradation | `COMMISSION_REQUIRED` | §6.6 |
| Seven falsifying-trace classes | `COMMISSION_REQUIRED` | §6.11 |
| Founder decision docket in the §6.12 shape | `COMMISSION_REQUIRED` | §6.12 |
| Q1–Q16 crosswalk table | `COMMISSION_REQUIRED` | §7.1 |
| Who must observe, who must not, when observers must agree | `COMMISSION_REQUIRED_QUESTION` | §6.7 |
| Whether recorded intent must remain distinguishable from accepted fact | `COMMISSION_REQUIRED_QUESTION` | §6.8 |
| Which states count without confirmation; who confers it; revocability | `COMMISSION_REQUIRED_QUESTION` | §6.8 |

**The load-bearing law, applied.** §6.8 asks whether recorded intent must remain distinguishable from accepted fact. That makes the distinction a **question the SemanticProgram must answer and provenance-mark**. It does not make an Establishment layer commission-mandated.

SLR-01 held that commission §§6.2/6.7/6.8 *mandate* the observer/authority architecture the candidate delivers, and used that to scope its verdict away from semantic substitution. **That holding is withdrawn.** The commission mandates the questions; the candidate's answers are its own.

---

## 5. Reconciliation 3 — candidate answers

Evaluated as answers proposed by the author unless an actual founder source independently establishes them.

### 5.1 Construct-level provenance matrix

| Construct | Class | Evidence |
|---|---|---|
| `Ritual` | `FOUNDER_SEALED` | L1 and L3 agree |
| `Ledger` | `FOUNDER_SEALED` | in the sealed subject name; L3 restates |
| `Day` (as entity) | `FOUNDER_DIRECTED_LATER` | L3 entity list; "Daily" in sealed name is not an entity |
| `Occurrence` | `FOUNDER_DIRECTED_LATER` | L3 `RitualOccurrence`; author shortened |
| `Actor` | `AUTHOR_PROPOSED` | L3 gave `Participant` + `Observer`; author collapsed to one bearer + roles |
| `Assertion` | `AUTHOR_PROPOSED` | L3 gave `CompletionObservation`; renaming is an authored semantic choice |
| `Adjudication` | `AUTHOR_PROPOSED` | L3 gave `AuthorityDecision`; renaming and the `STANDING`/`SUPERSEDED` property are authored |
| Roles `MAY/DID REPORT`, `MAY/DID AUTHORIZE`, `MAY CORRECT` | `FOUNDER_DIRECTED_LATER` | L3 septuple, verbatim |
| §5.1 derivation — `MAY/DID OBSERVE` fall outside the program | `AUTHOR_PROPOSED` | author's own derivation from §1.1; candidate flags it for attack |
| §1.1 "The ledger never knows what happened" | `AUTHOR_PROPOSED` | no founder source at either layer |
| §1.2 "two reporters may assert incompatibly while exactly one answer stands" | `FOUNDER_DIRECTED_LATER` | L3 `exactly one answer`; candidate marks it `FOUNDER-DIRECTED` — under-specified, not false |
| `scheduled ≠ performed ≠ observed ≠ accepted as authoritative` | `FOUNDER_DIRECTED_LATER` | L3 |
| `UNREPORTED` / `REPORTED` / `ESTABLISHED` | `AUTHOR_PROPOSED` | three of L3's six candidate statuses declined, one renamed; the triple is authored |
| `CONTESTED` declined as stored status, retained as derived predicate | `AUTHOR_PROPOSED` | authored derivation |
| `supersede` operation | `AUTHOR_PROPOSED` | L3 gave `Correction`; author collapsed it into an operation on adjudications |
| Discontinuities `D-a` … `D-h` | `AUTHOR_PROPOSED` | L3 named three substrate mechanisms; author restated as one semantic class and added five |
| Traces A–E | `DERIVED` | A from L3's worked example; B–E authored |
| Observation/authority separation *as a modeling requirement* | `COMMISSION_REQUIRED` | commission §6.2 |
| Intent-vs-accepted-fact *as a question* | `COMMISSION_REQUIRED_QUESTION` | commission §6.8 |
| `Entry` | `UNSUPPORTED` — **sealed member absent from the candidate** | L1 ×2, candidate ×0 |
| `begin` · `idle` · `active` | `UNSUPPORTED` — sealed members absent | L1, candidate ×0 |
| invalid-transition law as a named law | `UNSUPPORTED` — sealed member absent | L1 ×1, candidate ×0 |
| canonical ordering · equivalent state traces · state normalization · acceptance predicates | `UNSUPPORTED` — sealed members absent | L1, candidate ×0 |
| §6.1 establishment law — *"established by an Adjudication standing for it, nothing else"* | **`CONTRADICTORY`** | see SLR-R1-SEM-01 |
| `FOUNDER-DIRECTED` marks that do not distinguish L1 from L3 | **`CONTRADICTORY`** to commission §4 | see SLR-R1-PROV-01 |

### SLR-R1-SEM-01 — the sharpest finding

```
FINDING     Candidate §6.1: "An occurrence's answer is established by an
            Adjudication standing for it — nothing else. Not the number of
            assertions, not their agreement, not their recency…"

            The founder's own sealed conformance vector establishes
            state = complete from the operation `complete` alone. It contains
            no assertion, no reporter, no authority, and no adjudication.

CLASS       CONTRADICTORY
EFFECT      Under the candidate's establishment law the founder's own RC-0001
            acceptance vector is UNSATISFIABLE — it would require an
            adjudication act the founder's trace does not contain.
SCOPE       This is a genuine contradiction, not mere disjointness. It is the
            one place where the candidate does not merely omit sealed material
            but would rule it out.
NOT DECIDED Whether the founder intends L3 to supersede L1 (see FD-01). If
            supersession is intended, this ceases to be a contradiction and
            becomes a deliberate replacement.
```

### SLR-R1-PROV-01

```
FINDING     The candidate's FOUNDER-DIRECTED marks cite real founder text at
            L3 but never cite a digest-pinned act, and cannot distinguish L1
            from L3. Commission §4 requires the exact source for every
            FOUNDER-DIRECTED clause.
CLASS       CONTRADICTORY to commission §4
EFFECT      A reader cannot tell sealed scope from later direction. This is
            the mechanism that made the substitution undetectable to the
            author, the reviewer, and SLR-01 alike.
NOT BLAME   The four-class taxonomy the commission itself imposes has no term
            for the distinction. The author could not have marked it correctly
            using the vocabulary they were given.
```

---

## 6. Acceptance-test status

### 6.1 Commission §10 — carried forward unchanged

These measure candidate-against-commission. Admitting the raw source does not disturb them, so SLR-01's derivation stands and is not re-litigated.

```
PASS 4   ·   PARTIAL 3   ·   FAIL 7
FAIL: T1 path · T3 provenance marks · T4 refusal outcome ·
      T5 discontinuity destruction/degradation · T8 trace coverage ·
      T9 §7 crosswalk · T10 §6.12 docket
```

### 6.2 Sealed-scope conformance — new, and not expressible by commission §10

The commission has no test for fidelity to L1, because it never admitted L1.

```
S-01  Sealed entities present                    FAIL  — Entry absent
S-02  Sealed operations present                  FAIL  — begin, record,
                                                        complete absent
S-03  Sealed state progression present           FAIL  — idle/active/complete
                                                        absent; a different
                                                        triple is used
S-04  Sealed obligations addressed               FAIL  — canonical ordering,
                                                        equivalent state traces,
                                                        state normalization,
                                                        acceptance predicates
                                                        all absent
S-05  Founder exclusions registered              FAIL  — no prohibition list,
                                                        no non-goals
S-06  Founder acceptance vector satisfiable      FAIL  — SLR-R1-SEM-01

SEALED-SCOPE CONFORMANCE:   0 / 6
```

---

## 7. Path authority — independent verdict

Kept orthogonal to semantic quality, as directed.

```
AUTHORIZED_PATH
  governance/OURSELF-RCP-RC0001-DURABLE-DAILY-RITUAL-LEDGER-SEMANTICPROGRAM-v0.1-CANDIDATE.md
  STATUS: EMPTY — verified this movement

CURRENT_CANDIDATE_PATH
  governance/OURSELF-RCP-RC0001-SEMANTICPROGRAM-DDRL-v0.1-CANDIDATE.md
  STATUS: EXISTS · PRESERVED · UNMODIFIED

COMMISSION §2.3   "No other file is authorized for mutation by this commission."

ARTIFACT_PATH_VERDICT:   UNAUTHORIZED
```

The candidate's own §5 header records the path as `AUTHOR-CHOSEN` and states *"No path was authorized by the commissioning document."* That statement is false — §2.3 authorized exactly one — and it was made in good faith by an author who did not have the commission. The founder subsequently confirmed the author-chosen path **on that false premise**. Path authority therefore remains unrepaired by that confirmation.

---

## 8. Founder decision docket

Framed, not ratified.

```
FD-01   SCOPE RECONCILIATION
        QUESTION      Does the in-session direction (L3: Occurrence /
                      Assertion / Adjudication / Establishment) SUPERSEDE the
                      2026-08-12 sealed scope (L1: Ritual / Entry /
                      idle → active → complete / begin / record / complete),
                      or must the RC-0001 SemanticProgram serve L1?
        ALTERNATIVES  (a) L3 supersedes L1 — RC-0001's subject is the
                          assertion/adjudication ledger; SLR-R1-SEM-01 is
                          resolved as deliberate replacement; FS-B's vector is
                          withdrawn as a proof vector.
                      (b) L1 governs; L3 is a richer reading that must be
                          expressed in terms of Ritual/Entry and must leave
                          FS-B's vector satisfiable.
                      (c) Both stand as two SemanticPrograms; RC-0001 names
                          which one it proves.
        CONSEQUENCE   (a) discards the only founder-authored acceptance vector
                          in existence, and with it the concrete meaning of
                          `canonical ordering` and `acceptance predicates`.
                      (b) requires re-authoring most of the candidate's core.
                      (c) requires a second commission and defers RC-0001.
        RC-0001       Blocking. No representation adequacy test can run against
                      a subject whose identity is undecided.
        RECOMMENDATION  AUTHOR-PROPOSED: (b). L1 is the only layer carrying a
                      falsifiable acceptance vector, and RC-0001's entire value
                      is that a vector exists to diverge from.
        STATUS        FOUNDER_DECISION_REQUIRED

FD-02   A-01 · STATE OWNERSHIP
        QUESTION      Does idle → active → complete belong to Ritual, Entry,
                      both, or another object?
        EVIDENCE      FS-B's vector distinguishes top-level `state` from
                      per-entry `entries[0].status`. Evidence only; one worked
                      example is not a specification.
        STATUS        FOUNDER_DECISION_REQUIRED

FD-03   A-02 · STATE/ACTION RELATIONSHIP
        QUESTION      `complete` is both a state and an operation. Is the
                      operation the transition into the state, or are they
                      distinct semantic objects sharing a name?
        STATUS        FOUNDER_DECISION_REQUIRED

FD-04   A-03 · ENTRY CREATION
        QUESTION      Does `record` create an Entry, and is `entries[]` the
                      Ritual's Entry collection?
        STATUS        FOUNDER_DECISION_REQUIRED

FD-05   CUSTODY NORMALIZATION
        QUESTION      Should a corrective successor to SOURCE-CUSTODY-001 be
                      authored, carrying the omitted excerpts and a complete
                      register?
        NOTE          SOURCE-CUSTODY-001 must not be edited in place; its
                      digest and its defect both belong in lineage.
        STATUS        FOUNDER_DECISION_REQUIRED
```

The candidate's own five unresolved items (`U-1` … `U-5`) remain open and are not superseded by this docket. They are questions inside L3's frame; FD-01 asks whether that frame governs.

---

## 9. Verdicts

```
RC0001_SEMANTIC_LINEAGE:     PARTIALLY_AUTHORIZED_ELABORATION
```

Decomposed, because the single label understates the structure:

```
authorized      commission-required chambers — observer/authority separation,
                explicit unresolved states, contamination firewall, trace
                construction
authorized      elaboration of founder direction at L3, which is a genuine
                founder act
NOT authorized  by omission — six classes of founder-sealed member absent
                (S-01 … S-05); no founder act withdrew them
CONTRADICTORY   one construct — §6.1's establishment law renders the founder's
                own sealed acceptance vector unsatisfiable (SLR-R1-SEM-01)
```

`UNAUTHORIZED_DRIFT` is explicitly **not** returned. The author followed a founder act and had no access to the sealed record; neither did the commission that bound them. Placing the fault at the authoring layer would repeat SLR-01's error of locating a break where the evidence does not put it.

```
RC0001_ARTIFACT_CUSTODY:     NONCOMPLIANT
```

Sole ground: the §2.3 authorized path is empty and the candidate occupies an unauthorized path. Independent of semantic quality.

```
CANDIDATE_DISPOSITION:       REAUTHOR_AT_AUTHORIZED_PATH
```

Recommended, **conditional on FD-01**, and not performed here. Grounds: the sealed core is absent rather than defective, so there is little to repair; the establishment mechanism is contradictory rather than incomplete; and the existing provenance marks rest on a taxonomy that cannot express the distinction that produced the drift. The current artifact should be **preserved unmodified as superseded input** — its observer/authority analysis, its collapse arguments, and its five unresolved questions are the most valuable material in the lineage and should be carried into the re-authoring, not discarded.

If the founder prefers not to answer FD-01 yet, the correct substitute disposition is `HOLD`. No disposition is executed by this record.

---

## 10. Integrity evidence

```
CREATED    governance/OURSELF-RCP-RC0001-SLR-01-R1-CORRECTED-SOURCE-LINEAGE-RECONCILIATION.md
MODIFIED   none
STAGED     0
COMMITTED  none
```

One tracked RUORA file, `doctrine/self_axiom.md`, carries an uncommitted modification dated 2026-08-01 — twelve days before this movement. It is the pre-existing working-tree state that commission §12 places outside the movement, it was not read or written here, and it is reported rather than omitted so that `MODIFIED none` is verifiable rather than merely asserted.

```
RAW FOUNDER RECORD     digest reverified · 3/3 message digests recomputed · MATCH
SOURCE-CUSTODY-001     0f61f7bb…734600   UNCHANGED
AUTHORING COMMISSION   9a04124a…dcc04e   UNCHANGED
CURRENT CANDIDATE      72a1bf7f…ff3a47   UNCHANGED
SEMANTIC REVIEW        d478350a…84b438   UNCHANGED
SLR-01                 4d42d83b…508d2f   UNCHANGED · SUPERSEDED, NOT MODIFIED
AUTHORIZED §2.3 PATH   EMPTY
HBC HEAD               e350205f12c140b8216090b935f874cbbc454dee
HBC TRACKED FILES      30 · TRACKED CHANGES 0 · STAGED 0
```

**Independence limitation, stated as required.** This reconciliation was authored by the same session that authored the candidate, the semantic review, and SLR-01. It is **not** cold, blind, or lineage-independent. Its principal safeguard is that its decisive findings are mechanical — digest recomputation, byte-comparison, and whole-word counts over pinned sources — and are reproducible by any later party from the pins in §0.1 without trusting this document's reasoning. Its judgments, unlike its counts, remain lineage-dependent.

Three of this movement's findings are corrections against its own author's prior work: SLR-R1-PROV-01 supersedes SLR-01's account of where the provenance defect lies; §4's withdrawal reverses SLR-01's holding that the candidate's architecture was commission-mandated; and SLR-R1-CUSTODY-02 reports an omission this session did not detect when it first verified the custody record.

---

## 11. Next boundary

```
REPAIR AUTHORITY                 NONE
RELOCATION AUTHORITY             NONE
RE-AUTHORING AUTHORITY           NONE — requires FD-01 and a founder act
COMMISSION AMENDMENT AUTHORITY   NONE
COLD-REVIEW AUTHORITY            NONE
IMPLEMENTATION AUTHORITY         NONE
HBC MUTATION AUTHORITY           NONE
```

**Binding condition on any future cold review.** A reviewer given the candidate must receive the raw founder record, the commission, **and** this record. A reviewer given the candidate plus `SOURCE-CUSTODY-001` alone would validate against a register missing the founder's exclusions, acceptance predicates, and the only acceptance vector that exists.

---

*The record is controlling. Every summary of it, including this one, is evidence about the record and not a substitute for it.*
