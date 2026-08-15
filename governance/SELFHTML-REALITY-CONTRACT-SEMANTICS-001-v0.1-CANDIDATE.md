# SELFHTML REALITY CONTRACT SEMANTICS 001 · v0.1 CANDIDATE

**ACT** `SELFHTML_REALITY_CONTRACT_SEMANTICS_001` — authorized by `SELFHTML-FOUNDER-DISPOSITION-001` Ruling 3 upon durable recording of Rulings 1–2.
**AUTHORED** 2026-08-14 · session `bd059265`
**STATUS** `CANDIDATE_AWAITING_HOSTILE_REVIEW` (sequence step 4). Not ratified, not sealed, not reviewed. **No clause below is closed by this document.**
**PREDECESSORS** Adoption doctrine `f3ed35a2…5e12` · Design packet `2cfdecd1…1f85` · Founder disposition 001 (ancestor `e350205f`, topology, strata direction)
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

**RS-101 `[F]` Three strata, disjoint by type.** A status is never one word; it is a coordinate in up to three orthogonal strata:

| Stratum | Question it answers | Closed value set |
|---|---|---|
| **Observation status** | What happened when observation was attempted? | `OBSERVED` · `NOT_OBSERVED` · `NOT_WITNESSED` · `OBSERVATION_FAILED` |
| **Proof-obligation result** | Did evidence satisfy a specific obligation? | `PASS` · `FAIL` · `INCOMPLETE` |
| **Epistemic standing** | What standing does the underlying claim possess? | `VERIFIED` · `DECLARED` · `INFERRED` · `DEFERRED` · `REJECTED` |

**RS-102 `[A]` Stratum value distinctions.** `NOT_OBSERVED` = no observation was attempted. `NOT_WITNESSED` = observation of this class is outside the instrument's current capability, stated honestly (the inherited HBC null). `OBSERVATION_FAILED` = an attempt ran and errored. These three may never be folded into one value: an unattempted observation, an impossible one, and a broken one license different downstream moves.

**RS-103 `[A]` Coherence laws (composition constraints across strata).**

1. An obligation may return `PASS` only if **every** observation it requires has status `OBSERVED` and satisfies the obligation's predicate.
2. An obligation may return `FAIL` only on an `OBSERVED` violation. `OBSERVATION_FAILED`, `NOT_OBSERVED`, and `NOT_WITNESSED` yield `INCOMPLETE`, never `FAIL` — instrument trouble is not evidence of subject failure (inherited from RC-0001 SP-179: instrument inadequacy ≠ subject failure ≠ silence-as-conformance).
3. `VERIFIED` standing on a claim requires at least one obligation covering that claim returning `PASS` on evidence *capable of establishing it* (RS-303). `PASS` alone does not confer `VERIFIED` — an obligation may pass while covering only part of a claim.
4. No stratum value may be derived from another stratum by renaming. `PASS ≠ VERIFIED`; `OBSERVED ≠ PASS`; `NOT_WITNESSED ≠ FAIL` — each inequality is load-bearing.

**RS-104 `[A]` Falsifier.** Exhibit any artifact surface where one word does double duty across strata (a `VERIFIED` that means "the check passed", a `FAIL` recorded off a failed instrument), and RS-100 is breached.

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

1. A mapper's output standing is at most `INFERRED` whenever the target proposition ranges over an unobserved interior (visitor cognition, intent, valuation).
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

**RS-502 `[A]` Realization is a claim requiring proof, not a compile-time award.** That the compiler emitted realizers for a capability establishes `capability.realized: DECLARED` — nothing stronger. `VERIFIED` is reachable only through the RS-700 obligation chain. The compiler never awards `witnessed` for having emitted something `[F]`.

**RS-503 `[A]` Capability ≠ authority** (inherited law, adoption doctrine ruling 10). A capability says what the manifestation *can* mean/do; only the AuthorityContract says what it *may*. A realized capability exceeding granted authority is a compilation error, not a feature.

---

## RS-600 · Transition ontology

**RS-601 `[A]` Two transition kinds, never conflated.** *System transitions* (state machine of the manifestation itself — observable, deterministic, testable). *Intended visitor transitions* (`INTENDS_TRANSITION` edges — `DECLARED` intents whose realization is at most `INFERRED` through RS-303 chains). A system transition may be `VERIFIED` by direct observation; an intended visitor transition may never be, short of evidence actually capable of establishing the visitor's state.

**RS-602 `[A]` Transitions bind evidence prospectively.** Every transition names the SELFDARD events that witness it. A transition with no witnessing event is `NOT_WITNESSED` by construction and must say so — it is not thereby illegal, but it can never contribute to a `PASS`.

---

## RS-700 · Proof obligations and the three contracts

**RS-710 `[F]` The obligation chain.** `Capability → Proof Obligation → Required Observation → Evidence → Adjudication`. An obligation names: its claim; its requirements; its required evidence classes — `SOURCE_OBSERVATION`, `DOM_OBSERVATION`, `RENDER_OBSERVATION`, each individually required or not (the inherited three-class law, adoption doctrine §7); and its closed verdict set. **If the required observation cannot be made, say `NOT_WITNESSED`. Never "probably fine."**

**RS-711 `[A]` Verdicts are per-obligation, strata-typed.** An obligation's record carries all three strata per RS-100 (observations' statuses, the obligation result, the claim's resulting standing). No obligation aggregates another's verdict; aggregation is adjudication's job (a fourth, separate plane — adoption doctrine ruling 9) and is out of this gate's scope beyond the boundary statement.

**RS-720 `[A]` AuthorityContract semantics.** Closed enumeration of grants: backend authority · canonical state · payment authority · identity claims · data collection · mutation · external services `[F list]`. Default for any unenumerated authority is **DENIED** — fail-closed, inherited from the HBC kernel. The compiler consumes this contract as a *constraint*, never as a menu: no stage may widen a grant, and the emitted artifact must be statically incapable of exceeding it where static incapability is expressible.

**RS-721 `[A]` EvidenceContract semantics.** Enumerates: claims requiring witness · proof sources · render observations · interaction observations · runtime observations `[F list]`. Every claim in the RealityContract with standing stronger than `DECLARED` must trace to an EvidenceContract entry; a claim with no evidence binding is capped at `DECLARED` by construction.

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

`[A]` Known weakest surfaces, offered to the hostile review rather than hidden: RS-202's relation set is author-proposed and minimally motivated — attack its necessity/sufficiency; RS-304's propagation laws have no formal semantics for "capable of establishing" (RS-103.3 shares this); RS-801's FORBIDDEN AUTHORITY cells are minima, not proven complete; the coherence laws (RS-103) have not been adversarially replayed against constructed counterexamples. **Verdict: `CANDIDATE_AUTHORED — AWAITING_HOSTILE_REVIEW`.** Next lawful gate: sequence step 4, a hostile review of this document — ideally session-independent from `bd059265`, which authored every `[A]` clause here.
