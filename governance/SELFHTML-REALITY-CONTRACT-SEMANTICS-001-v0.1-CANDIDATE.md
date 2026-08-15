# SELFHTML REALITY CONTRACT SEMANTICS 001 · v0.1 CANDIDATE

**ACT** `SELFHTML_REALITY_CONTRACT_SEMANTICS_001` — authorized by `SELFHTML-FOUNDER-DISPOSITION-001` Ruling 3 upon durable recording of Rulings 1–2.
**AUTHORED** 2026-08-14 · session `bd059265`
**STATUS** `HOSTILE_REVIEW_CHANGES_REQUIRED_BOUNDED_REPAIR_APPLIED` — HR-001/HR-002/HR-003 author-claims-repaired; **not re-reviewed since this repair; ratification and repository genesis remain BLOCKED** until a delta review runs. Not ratified, not sealed. **No clause below is closed by this document.**
**PREDECESSORS** Adoption doctrine `f3ed35a2…5e12` · Design packet `2cfdecd1…1f85` · Founder disposition 001 (ancestor `e350205f`, topology, strata direction) · Hostile review `ISA-20260815-SELFHTML-HBC-HOSTILE-REVIEW-DISPOSITION-002` (`self-communication@9e83759e`) · Founder ruling `FOUNDER_RULING_SELFHTML_SEMANTICS_001_STANDING_DISPOSITION_SPLIT_001` (this repair's authority)
**AUTHORITY LIMIT** Doctrine/semantics only. No repository creation (step 5), no schema files, no compiler code, no HBC mutation, no shared-ontology extraction (Ruling 4 regress guard), no event-registry implementation, no browser tooling.
**PROVENANCE MARKS** `[F]` = Founder-directed, dictated in the adoption/glitch/disposition acts. `[A]` = author-proposed, derived by this session to complete the type system; every `[A]` clause is an attack surface for the hostile review.

---

## RS-000 · The central law `[F]`

```
Client Intent ≠ Reality Contract ≠ Semantic Graph ≠ HTML Artifact
             ≠ Rendered State ≠ Observed Evidence ≠ Adjudicated Proof
```

No stage of the compiler may collapse two adjacent terms. Serialize the reality contract, never the page; HTML is evidence of compilation, not source. YAML (or any transport) supplies encoding only — graph semantics live in this ontology, never in syntax.

---

## RS-100 · Typed status strata

**RS-101 `[F/A REVISED — `FOUNDER_RULING_SELFHTML_SEMANTICS_001_STANDING_DISPOSITION_SPLIT_001`]` Four strata, disjoint by type.** A status is never one word; it is a coordinate in up to four orthogonal strata. `v0.1` published three and let a fourth (disposition) hide inside epistemic standing — the defect `HR-001`/`HR-002`/`HR-003` all trace back to in some form. Corrected:

| Stratum | Question it answers | Closed value set | Ordered? |
|---|---|---|---|
| **Observation status** | What happened when observation was attempted? | `OBSERVED` · `NOT_OBSERVED` · `NOT_WITNESSED` · `OBSERVATION_FAILED` | No — mutually exclusive outcomes of one attempt, not a scale |
| **Proof-obligation result** | Did evidence satisfy a specific obligation? | `PASS` · `FAIL` · `INCOMPLETE` | No |
| **Epistemic standing** `[A, re-derived]` | What is the evidential/epistemic grounding of this claim? | `VERIFIED` · `DECLARED` · `INFERRED` · `UNCLAIMED` | **No — categorical.** See RS-101a |
| **Disposition** `[F, new axis]` | What governed outcome has been applied to this object? | `REJECTED` · `DEFERRED` (absence = no disposition applied; not itself a named value) | No — a governed act, not a scale |
| **Witness state** `[A, new — repairs RS-602]` | Does this transition have a witness binding declared at all? | `BOUND` · `UNBOUND` | No — structural, not observational |

**RS-101a `[A]` Standing re-derivation, tested against the four required properties.** `VERIFIED` (a covering obligation returned `PASS` on admissible evidence, RS-103.3), `DECLARED` (asserted in the contract, no evidence trace), `INFERRED` (derived via an RS-303 rule from an observation, not independently checked), `UNCLAIMED` (no assertion made at all — the default before any declaration) are: **mutually intelligible on one axis** — all four answer "how is this claim grounded," none smuggles in an outcome or an act; **operationally discriminable** — each has a distinct, checkable derivation condition, none collapses into another; **non-overloaded** — `REJECTED`/`DEFERRED` are withdrawn from this set entirely (RS-101b); **sufficient for v0.1** — covers unasserted, asserted-without-evidence, rule-derived, and obligation-checked, which is every grounding path this candidate currently authors.

**No total ordering is authorized.** `VERIFIED > DECLARED > INFERRED` (or any permutation) was tested and rejected: every place `v0.1` implicitly leaned on an order (`RS-721`'s "stronger than", `RS-304`'s "at most", `RS-502`'s "nothing stronger") is restatable as **explicit set membership or direct equality** without comparing magnitudes (RS-721 below; `RS-304`/`RS-502` carry the same wording defect and are corrected here as directly necessitated surfaces — no new law, no restructuring, the ordering-flavored words are withdrawn). No SELFHTML v0.1 operation was found that requires comparing two standings for magnitude. Falsifier per the ruling: `DECLARED` and `INFERRED` are genuinely incomparable — an author's direct assertion and a rule-derived conclusion are different *kinds* of grounding, not points on one scale — so a total order would be false on its face, not merely unproven.

**RS-101b `[F]` Disposition, minimally derived.** `REJECTED` and `DEFERRED` are the only disposition values this candidate currently requires; no third value (e.g. an explicit "active"/"accepted") is authored, because absence of a disposition already and unambiguously means "no governed outcome has been applied — proceed normally." Mirroring the standing vocabulary was considered and rejected: disposition answers a different question (a decision made *about* a claim) than standing (the claim's *own* grounding), and reusing words across them is exactly the defect being repaired.

**RS-101c `[A]` Witness state, attacked before retention (RS-602's repair).** Candidate `WITNESSED`/`NOT_WITNESSED` was rejected as the vocabulary: it would re-collide with `NOT_WITNESSED`'s existing, narrower, correct meaning in observation status (RS-102). The witness question decomposes into two already-typed concerns: (1) *is a witness event bound to this transition at all* — a contract-structural fact, fixed at parse/normalize time, independent of any runtime attempt — answered by the new `BOUND`/`UNBOUND` pair; (2) *did the bound event occur* — already fully answered by the pre-existing observation-status stratum, reused verbatim, no new vocabulary needed. `UNBOUND` is not a substitute for standing (it says nothing about evidential grounding), disposition (no governed outcome is implied), execution result (`PASS`/`FAIL`/`INCOMPLETE` are untouched), availability, or admissibility — it answers exactly one question and no other.

**RS-102 `[A]` Stratum value distinctions.** `NOT_OBSERVED` = no observation was attempted. `NOT_WITNESSED` = observation of this class is outside the instrument's current capability, stated honestly (the inherited HBC null) — **and only that**; it is never used for an absent witness *binding* (RS-101c/RS-602). `OBSERVATION_FAILED` = an attempt ran and errored. These three may never be folded into one value: an unattempted observation, an impossible one, and a broken one license different downstream moves. `UNBOUND` (witness state) and `UNCLAIMED` (standing) are likewise distinct from each other and from all three observation-status values: `UNBOUND` describes a transition's contract structure; `UNCLAIMED` describes a claim's assertion state; neither is an observation outcome.

**RS-103 `[A/F]` Coherence laws (composition constraints across strata).**

1. An obligation may return `PASS` only if **every** observation it requires has status `OBSERVED` and satisfies the obligation's predicate.
2. An obligation may return `FAIL` only on an `OBSERVED` violation. `OBSERVATION_FAILED`, `NOT_OBSERVED`, and `NOT_WITNESSED` yield `INCOMPLETE`, never `FAIL` — instrument trouble is not evidence of subject failure (inherited from RC-0001 SP-179: instrument inadequacy ≠ subject failure ≠ silence-as-conformance).
3. `VERIFIED` standing on a claim requires at least one obligation covering that claim returning `PASS` on evidence *capable of establishing it* (RS-303). `PASS` alone does not confer `VERIFIED` — an obligation may pass while covering only part of a claim.
4. No stratum value may be derived from another stratum by renaming. `PASS ≠ VERIFIED`; `OBSERVED ≠ PASS`; `NOT_WITNESSED ≠ FAIL`; and, newly stated, `REJECTED ≠ VERIFIED-failure`, `DEFERRED ≠ INCOMPLETE`, `UNBOUND ≠ NOT_WITNESSED` — every inequality is load-bearing.
5. **`[F]` Disposition presupposes an asserted claim.** A disposition may be applied only where standing `≠ UNCLAIMED`. `UNCLAIMED + REJECTED` and `UNCLAIMED + DEFERRED` are illegal: a governed outcome cannot be applied to a claim that was never made. All nine combinations of `{DECLARED, INFERRED, VERIFIED} × {none, REJECTED, DEFERRED}` are legal, including `VERIFIED + REJECTED` (a claim may be well-grounded and still rejected on grounds unrelated to its truth) and `INFERRED + REJECTED`, `VERIFIED + DEFERRED`, `DECLARED + DEFERRED` (the ruling's own worked examples).
6. **`[F]` Standing and disposition transitions never side-effect each other.** A disposition change (e.g. `DEFERRED → REJECTED`) leaves standing untouched if the evidential grounding did not change: `DECLARED + DEFERRED → DECLARED + REJECTED` is representable without any standing transition. Conversely, a standing change (e.g. `DECLARED → VERIFIED`, new evidence arrives) never silently clears or alters an existing disposition: a previously `REJECTED` claim that is later verified becomes `VERIFIED + REJECTED` — still rejected, now also verified — until a **separate**, disposition-authorized act changes the disposition.
7. **`[F]` Authority is separate per axis.** Standing-transition authority belongs to the RS-700 obligation chain — mechanical, evidence-driven, exercised by the compiler's proof stages. Disposition-transition authority belongs to the adjudication plane (RS-711's fourth plane; adoption doctrine ruling 9) — governance-driven, exercised by whatever process performs `PROMOTE`/`CORRECT`/`REJECT`-class acts at whatever granularity that plane operates. **Authority to adjudicate disposition does not confer authority to alter epistemic standing, and vice versa.** `v0.1` collapsed this structurally: by housing `REJECTED`/`DEFERRED` inside the standing field, the only authority ever modeled for them was the obligation chain's — there was no disposition-authority concept at all, because there was no disposition axis to hold one. This repair resolves that collapse as a direct consequence of RS-101/RS-101b, not as a separate patch.

**RS-104 `[A]` Falsifier.** Exhibit any artifact surface where one word does double duty across strata (a `VERIFIED` that means "the check passed", a `FAIL` recorded off a failed instrument, a disposition value used as a standing, a witness-binding gap reported as `NOT_WITNESSED`), and RS-100 is breached.

---

## RS-200 · Semantic relation × epistemic standing

**RS-201 `[F]` Orthogonality law.** Every edge in the semantic graph is a pair:

```
edge = (SEMANTIC_RELATION, EPISTEMIC_STANDING)
```

WHAT is asserted is independent of HOW established it is. `INTENDS_TRANSITION + DECLARED`, `SUPPORTS + VERIFIED`, `SUPPORTS + INFERRED` are all well-formed and all distinct.

**RS-202 `[A]` Initial closed relation set** (v0.1 — extensible only by a governed revision, never per-project ad hoc): `SUPPORTS` · `CONTEXTUALIZES` · `ENABLES` · `INTENDS_TRANSITION` · `DEPENDS_ON` · `REALIZES` · `WITNESSES`. `INTENDS_TRANSITION` additionally carries `from`/`to` state references.

**RS-203 `[F]` Intention is not established outcome.** `offer transforms visitor` is inexpressible. The lawful form is `offer INTENDS_TRANSITION recognition→initiation, standing: DECLARED`. Conversion language may not acquire factual standing by phrasing.

**RS-204 `[F]` Regress guard.** The (relation, standing) pattern is recorded as `SHARED_ONTOLOGY_EXTRACTION_CANDIDATE` (disposition Ruling 4). This gate defines it **for SELFHTML only** and extracts nothing into ecosystem law.

---

## RS-300 · State ontology, events, and the inference law

**RS-301 `[F]` Two state classes.** `observable` states are established by direct observation of runtime events (`arrived`, `engaged`, `initiated`). `inferred` states are propositions about the visitor (`recognition`, `desire`, `trust`) that no instrument reads directly. An inferred state always carries its evidence basis and `standing: INFERRED`. Analytics does not read minds.

**RS-302 `[F]` Event strata.** `BrowserEvent ≠ SELFDARDEvent`. Browser events are runtime substrate; SELFDARD events are semantic IR drawn from a **closed, versioned vocabulary** with classes `OBSERVATION` · `STATE_TRANSITION` · `INTERACTION` · `INTENT`. Arbitrary browser event strings never become institutional semantics. (The full registry is implementation-time — step 6/7 — not authored here.)

**RS-303 `[F]` The inference object.** Every mapping from observation to proposition is a typed object `O —r→ P`:

```yaml
mapping:
  source:      { event: browser.section_visible, standing: OBSERVED }
  target:      { proposition: visitor.exposed_to_identity_surface }
  inference:   { rule: visibility_threshold, standing: VERIFIED }
  output:      { standing: INFERRED }
```

The chain is always `EVENT → OBSERVATION → PROPOSITION → INFERENCE → STANDING`, never `EVENT → whatever semantic state sounds desirable`.

**RS-304 `[A]` Standing propagation laws.**

1. A mapper's output standing **is** `INFERRED` — not a ceiling, an equality — whenever the target proposition ranges over an unobserved interior (visitor cognition, intent, valuation). **(Wording only, RS-101a: standing is unordered, so "at most" no longer type-checks; the rule was always a fixed assignment, not a bound.)**
2. Output standing may be `VERIFIED` only when the target proposition is itself directly observable and was `OBSERVED` — in which case the mapping is a relabeling within the observation class, and its SELFDARD class must be `OBSERVATION`, not `STATE_TRANSITION`.
3. An `OBSERVATION`-class SELFDARD event may derive only from direct browser observations — never from an inference output. Inference outputs enter as propositions with standing, not as observations.
4. The inference **rule** carries its own standing, independent of any output it produces: a `VERIFIED` rule (validated threshold) can still only mint `INFERRED` conclusions about cognition.
5. Unlawful by construction: `visitor.recognized_identity: VERIFIED` absent evidence capable of establishing recognition. The mapper is the laundering surface; these laws are its guard.

**RS-305 `[A]` Falsifier.** Exhibit any path by which a browser event reaches a semantic state carrying standing stronger than its inference chain licenses, and RS-300 is breached.

---

## RS-400 · The RealityContract object

**RS-401 `[F]` The load-bearing object.** `𝓡 = (I, Γ, Σ, C, E, T, W, D, K)`:

| Component | Semantics |
|---|---|
| `I` identity | who/what this reality is — id, archetype; a SELF identity **candidate** reference, never an identity claim (`runtime projection ≠ SELF identity`) |
| `Γ` intentions | goals as declared intents; each is `DECLARED` until adjudicated — goals never self-establish |
| `Σ` states | RS-301's two classes, with initial/desired markings; `desired` is intent, not prediction |
| `C` capabilities | RS-500 semantic capabilities with their `requires` sets |
| `E` relationships | RS-200 edges — always (relation, standing) pairs |
| `T` transitions | RS-600 transition objects |
| `W` witness obligations | references into the EvidenceContract (RS-720) — what must be witnessed for this reality's claims |
| `D` differentiation | references into the DifferentiationContract (RS-730) — what sameness must be resisted |
| `K` constraints | hard invariants the compiler may never trade away |

**RS-402 `[F]` Four contracts, not one file.** `ManifestationSpec = R + A + E + D`: RealityContract (what reality is desired) · AuthorityContract (what this manifestation may claim/do) · EvidenceContract (what must be witnessed) · DifferentiationContract (what sameness must be resisted). Each validates independently; a defect in one never silently invalidates or excuses another. `[A]` Cross-references between contracts are by identity, never by copied content — one fact, one home.

---

## RS-500 · Capability ontology

**RS-501 `[F]` Capabilities are semantic, realizers are downstream.** A capability (`establish_authority`, `initiate_relationship`) declares `requires` — semantic preconditions (identity, distinction, admissible_proof), not components. SELFponents are **capability realizers** (`AuthorityRevealer`, `ProofSurface`, `DistinctionEngine`…), resolved by the compiler as `Capability → PrimitiveSet`. DOM structure (`<section>`, `<article>`) is a further downstream binding and appears nowhere in a RealityContract.

**RS-502 `[A]` Realization is a claim requiring proof, not a compile-time award.** That the compiler emitted realizers for a capability establishes `capability.realized: DECLARED` — not `VERIFIED`. `VERIFIED` is reachable only through the RS-700 obligation chain. **(Wording only, RS-101a: "nothing stronger" presupposed an ordering; the rule is a fixed assignment at emission time, not a bound.)** The compiler never awards `witnessed` for having emitted something `[F]`.

**RS-503 `[A]` Capability ≠ authority** (inherited law, adoption doctrine ruling 10). A capability says what the manifestation *can* mean/do; only the AuthorityContract says what it *may*. A realized capability exceeding granted authority is a compilation error, not a feature.

---

## RS-600 · Transition ontology

**RS-601 `[A, REVISED — replays the `HR-003` self-contradiction]` Two transition kinds, never conflated.** *System transitions* (state machine of the manifestation itself — observable, deterministic, testable) may reach standing `VERIFIED` by direct observation — precisely RS-304.2's condition: the target proposition is itself directly observable and was `OBSERVED`. *Intended visitor transitions* (`INTENDS_TRANSITION` edges — asserted at standing `DECLARED`) reach at most `INFERRED` through an RS-303 mapper chain — precisely RS-304.1's condition: visitor cognition is never itself the direct object of observation, so no chain terminating in a cognitive proposition may output `VERIFIED`. **These are two disjoint cases, fully determined by which RS-304 condition the target proposition satisfies — not an absolute rule with a hedge.** `[Before/after, per this repair's replay:]` the prior text said "may never be [`VERIFIED`], short of evidence actually capable of establishing the visitor's state" in one sentence — asserting an absolute prohibition and immediately exempting from it, without saying what the exemption's condition was or where it was governed. That was not a standing/disposition confusion (`REJECTED`/`DEFERRED` do not appear in this clause); it was an independent, self-contained contradiction, and the standing/disposition split (RS-101) does not touch it. It is resolved directly here by naming RS-304's actual governing condition instead of re-asserting the ambiguity.

**RS-602 `[A, REVISED — repairs `HR-001`]` Transitions bind evidence prospectively, and witness state is not observation status.** Every transition either binds at least one SELFDARD event as its witness (`WITNESS_STATE: BOUND`) or does not (`UNBOUND`) — a contract-structural fact, fixed at parse/normalize time (RS-101c), never itself a runtime status. An `UNBOUND` transition is not thereby illegal, but by RS-103.1 no obligation covering it can ever return `PASS` — it can never produce an `OBSERVED` result, because nothing was bound to observe. Once a transition is `BOUND`, whether its witness event actually occurred at runtime is reported through the pre-existing observation-status stratum exactly as any other observation — `OBSERVED` / `NOT_OBSERVED` / `NOT_WITNESSED` / `OBSERVATION_FAILED` — and `NOT_WITNESSED` there retains RS-102's sole original meaning: the instrument is incapable of this observation class. **The prior wording used `NOT_WITNESSED` for the `UNBOUND` case; that reuse is withdrawn**, not merely relabeled — `UNBOUND` and `NOT_WITNESSED` now name genuinely different failure loci (authoring-time absence vs. runtime instrument incapability) and neither may stand in for the other.

---

## RS-700 · Proof obligations and the three contracts

**RS-710 `[F]` The obligation chain.** `Capability → Proof Obligation → Required Observation → Evidence → Adjudication`. An obligation names: its claim; its requirements; its required evidence classes — `SOURCE_OBSERVATION`, `DOM_OBSERVATION`, `RENDER_OBSERVATION`, each individually required or not (the inherited three-class law, adoption doctrine §7); and its closed verdict set. **If the required observation cannot be made, say `NOT_WITNESSED`. Never "probably fine."**

**RS-711 `[A]` Verdicts are per-obligation, strata-typed.** An obligation's record carries all three strata per RS-100 (observations' statuses, the obligation result, the claim's resulting standing). No obligation aggregates another's verdict; aggregation is adjudication's job (a fourth, separate plane — adoption doctrine ruling 9) and is out of this gate's scope beyond the boundary statement.

**RS-720 `[A]` AuthorityContract semantics.** Closed enumeration of grants: backend authority · canonical state · payment authority · identity claims · data collection · mutation · external services `[F list]`. Default for any unenumerated authority is **DENIED** — fail-closed, inherited from the HBC kernel. The compiler consumes this contract as a *constraint*, never as a menu: no stage may widen a grant, and the emitted artifact must be statically incapable of exceeding it where static incapability is expressible.

**RS-721 `[A, REVISED — repairs `HR-002`]` EvidenceContract semantics.** Enumerates: claims requiring witness · proof sources · render observations · interaction observations · runtime observations `[F list]`. Every claim in the RealityContract whose standing is `VERIFIED` **or** `INFERRED` must trace to an EvidenceContract entry — both values require evidence by construction (RS-103.3, RS-303), so an untraceable claim cannot lawfully carry either. A claim with no EvidenceContract entry is capped at `DECLARED` (if asserted) or remains `UNCLAIMED` (if never asserted) — never `VERIFIED` or `INFERRED` by construction. **This is a membership test over `{VERIFIED, INFERRED}`, not a magnitude comparison** — the prior "stronger than `DECLARED`" wording presupposed an ordering RS-101a found unnecessary and withdrew; no comparison relation is invoked here or required by this clause.

**RS-730 `[A]` DifferentiationContract semantics.** Enumerates resisted sameness: category norms · generic structures · competitor resemblance · identity dilution `[F list]`. Consumed by the `differentiate` stage as typed axes `Δ = (Δ_semantic, Δ_structural, Δ_visual, Δ_responsive, Δ_interaction, Δ_authority, Δ_evidence)` `[F]`. Each axis reports RS-100 strata independently; **no universal green check** — one axis's `PASS` launders nothing about another `[F]`.

---

## RS-800 · Compiler stage boundaries

**RS-801 `[F pattern]` Four-field stage contracts.** Every stage declares `INPUT / OUTPUT / INVARIANTS / FORBIDDEN AUTHORITY` — the founder's sealed L1 stage-contract pattern, inherited deliberately. `[A]` v0.1 boundary table:

| Stage | INPUT → OUTPUT | FORBIDDEN AUTHORITY (minimum) |
|---|---|---|
| Parse | contract text → Reality Contract AST | interpret meaning; repair invalid input (fail closed) |
| Normalize | AST → Semantic Graph IR | invent nodes/edges; strengthen any standing |
| Critique | Semantic Graph IR → findings | mutate the graph; adjudicate |
| Capability resolution | graph + registry → realizer plan | invent capabilities; exceed AuthorityContract; choose DOM |
| Target IR | realizer plan → HTML Target IR | reinterpret semantic law; drop constraints `K` |
| SELFponent bind | Target IR → SELFponent graph | widen authority; alter capability semantics |
| Emit | SELFponent graph → HTML/CSS/JS | invent capability adaptations; weaken invariants; authorize execution; adjudicate success |
| Observe | runtime → event graph / evidence | mint SELFDARD events outside the closed vocabulary; strengthen standing (RS-304) |
| Witness/differentiate/prove | artifact + evidence → proof records | award verdicts without required observations; aggregate across obligations |
| Adjudicate | proof records → PROMOTE/CORRECT/REJECT | (separate plane; out of this gate's scope beyond existence) |

**RS-802 `[F]` Reproducibility binding.** Every manifestation binds `contract_digest`, `ontology_version`, `primitive_registry`, `compiler_version`, `artifact_digest` — the same contract under different compiler/primitive versions is a different reality; the IP is the contract + ontology + lineage, the artifact is disposable evidence.

---

## RS-900 · What this gate does NOT settle

Carried `UNRESOLVED` (adoption doctrine §8 + new): custody format · browser observation engine · adjudication schema · mutation-proposal schema · primitive completeness · INSELFACTION relation · the concrete SELFDARD event registry · schema serialization format · the full SEMANTIC_RELATION extension procedure · Δ-axis measurement instruments · which `4792500b` deltas (if any) ever earn promotion. Repository genesis remains step 5. Shared-ontology extraction remains prohibited.

## RS-910 · Self-assessment and next gate

`[A]` Known weakest surfaces, offered to the hostile review rather than hidden: RS-202's relation set is author-proposed and minimally motivated — attack its necessity/sufficiency; RS-304's propagation laws have no formal semantics for "capable of establishing" (RS-103.3 shares this); RS-801's FORBIDDEN AUTHORITY cells are minima, not proven complete; the coherence laws (RS-103) have not been adversarially replayed against constructed counterexamples.

**RS-911 `[A]` Bounded repair record — 2026-08-15, session `bd059265`, under `FOUNDER_RULING_SELFHTML_SEMANTICS_001_STANDING_DISPOSITION_SPLIT_001`.** `HR-001` (RS-602), `HR-002` (RS-721), `HR-003` (RS-601) repaired; RS-101 restructured to four strata with standing narrowed and unordered, disposition and witness-state introduced as new axes; RS-304/RS-502 given minimal wording-only fixes for coherence with the new unordered standing. **Not touched, still open:** the secondary surfaces from the same hostile review — RS-304/RS-103's "capable of establishing" formalization, RS-202's relation-set necessity/sufficiency, RS-801's FORBIDDEN AUTHORITY completeness — and the broader four-closure set raised in the Founder's own post-review commentary (evidence-admissibility formalization `Admissible(E,P,C)`, relation-family repair, complete `Stage_i = (Input_i, Output_i, Invariant_i, ForbiddenAuthority_i)` for every stage including `ADJUDICATE`, and a cross-contract conflict-terminal matrix `Resolve(R,A,E,D)`), all explicitly named as a *possible future* v0.2 scope, not yet authorized. **This repair does not claim the hostile review passed, and does not close it — only an independent reviewer may.**

**Verdict: `CANDIDATE_BOUNDED_REPAIR_APPLIED — AWAITING_DELTA_REVIEW`.** Next lawful gate: a delta hostile review scoped to HR-001/HR-002/HR-003 plus the new RS-101/RS-101a/RS-101b/RS-101c axes — ideally session-independent from `bd059265`, which authored both this repair and the original candidate. Repository genesis (sequence step 5) remains blocked until that review returns a disposition other than `CHANGES_REQUIRED`.
