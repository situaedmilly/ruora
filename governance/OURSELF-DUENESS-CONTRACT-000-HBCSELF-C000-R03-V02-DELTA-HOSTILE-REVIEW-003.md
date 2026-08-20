# OURSELF-DUENESS-CONTRACT-000 — HBCSELF-C000-R03 v0.2-DELTA HOSTILE REVIEW 003

```
CUSTODY STATUS:    REVIEW ARTIFACT — CUSTODY-BOUND POST-EXECUTION AND
                   POST-RELAY, on separate Founder authorization
                   ("Custody-bind C000-R03, then authorize the scoped
                   v0.3 repair").
CHAMBER EXECUTED:  2026-08-20 by HBCSELF-C000-R03 (fresh context-blind
                   subagent; hostile semantic review scoped to the v0.2
                   delta; read-only; no writes performed; not a repair
                   agent, not an author)
SUBJECT:           OURSELF-DUENESS-CONTRACT-000-v0.2-CANDIDATE @ 2b392e5,
                   specifically its delta over v0.1 @ c43a203, checked
                   against C000-R01 @ 6c4d318 and C000-R02 @ 2b53dc1.
VERDICT:           CHANGES_REQUIRED — F-1 FULLY_CLOSED; new BLOCKING
                   finding R03-1 (declared-vs-actual input-surface
                   integrity ungoverned — the "does the rule lie about
                   its declared inputs" attack, one layer deeper than
                   R02 tested); 2 non-blocking (R03-2, R03-3) coupled to
                   R03-1.
KEY FINDING:       specimen G closed only for HONEST declarations. L-16 +
                   extended L-8 check declared-vs-basis; nothing checks
                   declared-vs-actual. Same defect species as v0.1's F-1
                   (load-bearing closure claim asserted as outcome-
                   sentence, no enforceable mechanism) recurring at L-16's
                   own meta-level.
PROPAGATION:       R03-1 weakens the Third-wall ruling's "sufficient
                   regardless of access" claim (F-2) and the amended L-3's
                   practical guarantee (item g) — both inherit L-16's gap
                   rather than being independently defective.
MINIMALITY/ANTI-RESURRECTION/SCOPE-FIDELITY: all clean — TRUE / 15/15 PASS
                   / F-3,F-4,F-5 genuinely untouched.
RELAY RECORD:      full return relayed unmodified to the Founder before
                   this custody act, per Founder command.
CUSTODY LAW:       ReviewCustodied != RepairAuthorized. This commit binds
                   the review to lineage; it authorizes NOTHING by itself
                   — the scoped v0.3 repair is a separate act, executed
                   as its own commit, after this one.
TRANSMISSION NOTE: Chamber text below is preserved verbatim, including
                   its leading and trailing lines. This custody header is
                   the only authoring-session addition. Bytes recovered
                   from the chamber's own session transcript (agent
                   ac397a44d578c1677), final message, unmodified; 24,117
                   B, sha256
                   b2c5279b4fcef6ea193cf08c2aa9cc69329193df050f8bfaed03a21286d58943.
```

---

# HBCSELF-C000-R03 — LINEAGE-INDEPENDENT HOSTILE REVIEW OF OURSELF-DUENESS-CONTRACT-000 v0.2 CANDIDATE (bounded repair delta)

```
CHAMBER:      HBCSELF-C000-R03 (context-blind; hostile semantic review;
              read-only; NOT a repair agent, NOT an author, NOT an
              implementer; NO mutation/repair/implementation authority)
SUBJECT:      OURSELF-DUENESS-CONTRACT-000-v0.2-CANDIDATE @ 2b392e5,
              specifically the DELTA over v0.1 @ c43a203
```

---

## 1. Pin/lineage verification

Parent-pointer walk performed via `git show --no-patch --format='%H %P'`:

| Commit | Parent (recorded) | Matches expected chain? |
|---|---|---|
| c43a203 | 7c4486b | YES (v0.1's base) |
| 6c4d318 | c43a203 | YES (R01 → v0.1) |
| 2b53dc1 | 6c4d318 | YES (R02 → R01) |
| 2b392e5 | 2b53dc1 | YES (v0.2 → R02) |

Chain `c43a203 → 6c4d318 → 2b53dc1 → 2b392e5` confirmed linear, no forks, no gaps, all on `governance/living-symbolic-transmission-morphology-000-custody`. b4c80e4's own parent (055841c) also confirmed, consistent with both R01's and R02's citations.

**Remote-containment:** enumerated all `refs/remotes/*` (github and selfpi remotes) via `git for-each-ref refs/remotes`. None of c43a203, 6c4d318, 2b53dc1, or 2b392e5 appear among any remote ref's reachable history as checked by `git branch -r --contains 2b392e5` / `--contains c43a203` (both empty). **All four target commits remain UNPUSHED**, consistent with every artifact's own self-declared status.

**v0.2's stated evidence-basis commit references** (b4c80e4, 6c4d318, 2b53dc1, 055841c, 7c4486b): all five exist in the branch's commit graph (verified in `git log --oneline`), all five are cited with roles that match their actual custody headers (b4c80e4 = DUE-01 required basis; 6c4d318 = R01, F-1 finding; 2b53dc1 = R02, predicate-closure finding; 055841c = ADJ-02, neighboring/untouched; 7c4486b = pressure-only, cited nowhere as authority). **Accurate.**

**Verdict: PASS — pin/lineage verification clean.**

---

## 2. F-1 closure grade: **FULLY_CLOSED**

R01's F-1 required two components. Checking the actual seated text in 2b392e5:

**(a) Promote to a first-class numbered law stated as a testable equivalence.** L-15 (§3): *"For any x ∉ BasisRefSet, mutating x while BasisRefSet and ContractVersion remain fixed MUST leave D and DuenessDispositionID unchanged."* This is a numbered law (not prose), phrased as a testable equivalence (fixed antecedent, required-identical consequent) — satisfies (a) exactly as R01 specified, including integration into §10's law table.

**(b) A dedicated §11 kill-matrix row distinct from row 15.** Row 21: *"Non-basis perturbation… same admitted BasisRefSet + ContractVersion, mutate any x∉BasisRefSet between runs → D and DuenessDispositionID MUST be bytewise identical (L-15)."* Row 15 remains the original held-vs-absent UNRESOLVED/L-3 test, untouched. Row 21 is genuinely distinct in subject (arbitrary non-basis mutation vs. UNRESOLVED indistinguishability) — satisfies (b).

Both components of F-1 are present, correctly worded, and correctly cross-referenced. **FULLY_CLOSED.**

---

## 3. Predicate-closure / specimen-G closure grade: **PARTIALLY_CLOSED** (this is the decisive section)

### 3a. What R02 actually demanded

R02's specimen G (item 7 of 2b53dc1, ambient-read matrix row G): *"invokes a deterministic external function whose input/state is unbound into B"* — ruled VALID (i.e., a live attack) because *"determinism defeats T-1's replay-test detection... and the input dependency is unenumerated, so no reviewer-authored perturbation row can target it."* R02's repair-surface items (c) and (d) called for: a declared, complete input surface on the `rule` field (c), and an admission-time check of that declared surface against BasisRefSet classes ∪ contract-pinned constants (d), with INADMISSIBLE on violation.

### 3b. What v0.2 actually built

§2's `rule` field now requires *"a declared, complete input surface"* with an enumerated (not single-case) ambient-read exclusion. L-16 states the rule must be checked at admission and that *"a rule found to consume any input outside its declared surface is nonconformant… regardless of whether that input is itself deterministic."* §7's L-8 EXTENDED performs the actual admission-time check: *"the gate additionally verifies that the contract's declared rule input surface (§2) is a subset of the admitted basis-ref classes ∪ contract_constants. A contract whose rule declares — or is found to consume — any input outside that union is INADMISSIBLE."*

For the literal specimen G as R02 described it — an author who **honestly declares** that their rule invokes an external function whose input isn't in the basis — L-16 + extended L-8 closes it cleanly: the declaration itself would fail the subset check at admission, before any replay testing is even relevant. **This much is FULLY_CLOSED.**

### 3c. The sharper attack: does the rule LIE about its declared surface?

Attack the word "declares." Nothing in §2's schema, §3's L-16, or §7's L-8 EXTENDED describes **any mechanism that verifies a rule's declared input surface is actually complete and truthful.** The schema requires the author to *declare* the surface; the admission gate checks the *declared* surface against the basis. There is no static analysis, no sandboxing/capability restriction, no code-level audit, no witness constitution for the declaration act itself — nothing analogous to the witness-constitution machinery §7/L-8 already requires for basis-ref *classes*. A rule authored to consume `current_system_health()` while declaring only its two legitimate basis-ref inputs would pass the admission-time check exactly as written, because the check operates entirely on the **declared** surface, not the **actual** one.

v0.2 is aware this gap exists — that is precisely what the phrase *"or is found to consume"* in L-8 EXTENDED gestures at, and precisely what item e's new reason-class (`PREDICATE_INPUT_UNDECLARED`, triggered by *"runtime detection of an L-16 breach escaping admission-time detection"*) exists to catch. But **"found to consume" and "runtime detection" name an outcome, not a mechanism.** No instrument is specified: no code-inspection procedure, no sandbox trap, no capability-restriction enforcement, no logging/audit requirement, nothing that would actually cause a lying declaration to be *found*. §11 row 22 restates the law's required *result* ("if escaping detection… detection at runtime yields UNRESOLVED/PREDICATE_INPUT_UNDECLARED") but, like v0.1's original F-1 defect, supplies no apparatus by which a hostile reviewer or an implementer could verify this detection is even possible, let alone exercised.

This is the same defect *species* R01 originally attacked in v0.1 (a load-bearing determinism/closure claim asserted only as an outcome-sentence, with no dedicated testable mechanism) — recurring one layer deeper, at the meta-level of L-16 itself. **L-16 governs declared-vs-basis. Declared-vs-actual is left ungoverned**, covered only by an unenforced promissory phrase.

### 3d. Grade and reasoning

- Specimen G as R02 literally scoped it (honest declaration of an unenumerated dependency): **FULLY_CLOSED.**
- The meta-level "does the rule lie about its own inputs" gap (declared-vs-actual): **NOT_CLOSED** — acknowledged in vocabulary (`PREDICATE_INPUT_UNDECLARED`) but not in mechanism.

Combined grade: **PARTIALLY_CLOSED**, with a genuine new residual gap surfaced. This gap is not disqualifying of the repair's good-faith effort — v0.2 correctly implements everything R02 explicitly specified — but it means v0.2's claim to have closed "predicate closure" is broader than what the text actually establishes. See Finding R03-1 below.

---

## 4. F-2/tripartite-wall closure grade: **PARTIALLY_CLOSED**

The Third-wall ruling (§3) chooses R02's option (a): rule EvaluatorCanAccess as ADJ-02-stratum matter, referenced not redefined, and asserts *"L-1/L-2/L-15/L-16 are sufficient at this stratum regardless of access: even where EvaluatorCanAccess(X) is true, L-15/L-16 forbid X's influence on D unless X ∈ BasisRefSet."*

Tested against the laws as actually written: **the logical structure is sound in principle** — IF L-16's admission-time check reliably prevents any rule from consuming X ∉ BasisRefSet, and L-15 guarantees D is invariant under mutation of any x ∉ BasisRefSet, then together they do foreclose X's influence regardless of technical access, making a standalone access-law genuinely redundant.

But this soundness is **inherited, not independent** — it rests entirely on L-16's enforcement being airtight. Section 3 above establishes that it is not: a rule with `EvaluatorCanAccess(X) = true` and `X ∉ BasisRefSet` that **falsely declares** a narrower input surface than it actually consumes would clear L-8 EXTENDED's admission check and could influence D in exactly the way the Third-wall ruling claims is foreclosed. The scenario the ruling declares impossible ("EvaluatorCanAccess(X) ∧ X∉BasisRefSet still influencing D") is not, in fact, impossible under the text as written — it is merely undetected-until-runtime, and even then only if the unspecified runtime-detection mechanism exists and fires.

**Grade: PARTIALLY_CLOSED** — the jurisdictional ruling itself is a legitimate, well-reasoned application of R02's option (a), and the *derivation* is valid; but its factual guarantee is only as strong as L-16, and L-16 has the gap found in §3 above. This is not a new independent defect — it is finding R03-1 propagating into F-2's closure claim.

---

## 5. Item e (reason-class) coherence finding

`PREDICATE_INPUT_UNDECLARED` is correctly integrated as a register **entry** (not a new register, not a new top-level D value) — consistent with the existing four-entry pattern (CONTRACT_SET_INCOHERENT, BASIS_REF_UNESTABLISHABLE, BASIS_MEDIA_UNKNOWN, SUBJECT_SEAT_TIER_UNADJUDICABLE) and with R02's own item-9 ruling that this must not be a new object.

The tension the charter asks to pressure is real: if L-16 is an *admission*-time check, how can a breach of it "escape" and later be caught at "runtime"? The resolution is coherent in principle (admission-time checks the *declared* surface; runtime could in principle observe *actual* consumption), but as found in §3, **no runtime-detection mechanism is named anywhere in the document.** This means item e's reason-class is well-formed vocabulary with an **unspecified, possibly unfireable trigger** — closer to an honest admission that L-16 cannot be perfectly enforced at admission for all cases than to a functioning fail-closed path. It is not literally dead code (the vocabulary slot is legitimate and would activate if any detection mechanism is later specified), but as currently seated it names a destination with no road to it.

---

## 6. Item g (L-3 generalization) finding

v0.1 L-3: *"UNRESOLVED over held matter MUST be bytewise indistinguishable from UNRESOLVED over absent matter…"* — single D-value, binary held/absent axis.

v0.2 L-3: *"No result value (NOTHING_DUE, DUE, or UNRESOLVED) may be bytewise distinguishable… between the case where unadmitted matter X is held and the case where X is absent."* — broadened to all three D-values, **but the axis of indistinguishability is still binary held-vs-absent.**

R02's actual finding (item g's source) was that a predicate-closure violation could let X's **value** shape which of DUE/NOTHING_DUE is returned — a continuous risk (X=5 vs. X=10, both *held*), not merely a presence/absence risk (X held vs. X absent). The generalized L-3 text does not test value-a-vs-value-b for held X; it only tests held-vs-absent across a wider set of result values. So the wording genuinely widens *which* result channels are covered but does **not** widen the *axis* of the leak being tested — it remains implicitly binary.

The Repair Ledger's own claimed conformance consequence ("even if it escaped detection, its [X's] value could not lawfully leak through any result channel under the generalized L-3") **overclaims what the seated L-3 text establishes.** That consequence is only true if L-16 has already foreclosed any live value-dependence on undeclared X in the first place — which, per §3 above, it has not fully done. This is the same residual gap (R03-1) surfacing a third time: L-16's incompleteness leaves both the Third-wall ruling (§4) and L-3's practical guarantee (§6) resting on a floor that has a hole in it.

---

## 7. Minimality re-audit: **TRUE**

`contract_constants` is a schema-field addition to the DuenessContract — an object already adjudicated as the single lawful mint (DUE-01, ADJUDICATED_NECESSITY). Under the estate's anti-mint discipline (DUE-01/ApparentMissingPrimitive), a "primitive" is a new occurrence species/object type (the killed examples — EvaluationContext, Epoch, DueClaim, DUENESS_CONFLICT, REMAINS_DUE-edge — are all exactly this: new nouns with independent standing). `contract_constants` is not a new noun; it is a typed field within an already-minted schema, structurally identical in kind to `basis_ref_classes` or `due_species`, which were never separately challenged as primitives. Likewise, "declared input surface" is a property of the pre-existing `rule` field, not a new object.

This tracks R02's own item-12 minimality ruling almost exactly: R02 explicitly rejected minting `Predicates(C)`/`Inputs(P)` as new quantified objects and required the substance be seated as extensions of §2's `rule` field and §7/L-8's admission gate instead. v0.2 did precisely that. The zero-new-primitives claim is not an independent achievement of v0.2 so much as a faithful implementation of R02's ruling — but it is **accurate**, not overclaimed.

---

## 8. Internal coherence findings

- §2's `rule` field ("declared… complete input surface," "basis_ref_classes or a value in contract_constants") cross-references cleanly with §3's L-16 ("declared input surface… checked… against BasisRefSet classes ∪ contract_constants") and §7's L-8 EXTENDED (same phrase, same union). No terminological drift found across the three sites.
- §11 rows 21–23 correctly exercise what §3 and the Third-wall ruling claim: row 21 tests L-15 exactly, row 22 tests L-16/specimen G exactly (including the escaping-detection branch), row 23 tests the foreign-SELF-state/ADJ-02-crossing case (item f) exactly, deferring correctly to ADJ-02's crossings-only witness law rather than re-adjudicating it.
- §10's table entries for L-16, the amended L-3, and the Third-wall ruling are each honestly self-flagged "NOT YET independently hostile-reviewed" — accurate given this is that review.
- §12's citation "per C000-R02 item 10 finding" is verified accurate against R02's own section numbering (item 10 = MICROAUTO2_WITHOUT_PREDICATE_CLOSURE, §14 of 2b53dc1).
- No numbering collisions: L-15/L-16 are new numbers with no prior claimant; L-3 is amended in place (correct — not renumbered, avoiding a collision); §11 rows 21–23 extend past the highest existing row (20/R4) with no overlap. The pre-existing row-16 gap (jumping 15→M→17) is inherited from v0.1, not introduced here.

**No new internal contradictions found.** The one substantive coherence weakness is the one already identified: L-16's "or is found to consume" clause and item e's runtime-detection trigger reference each other without either naming the detection mechanism — an internal *incompleteness*, not a *contradiction*.

---

## 9. Anti-resurrection re-check: **PASS, 15/15 undisturbed**

Spot-checked `contract_constants` and every other v0.2 addition against DUE-01's kill list: `contract_constants` are pinned, versioned, immutable scalar values named at admission — not a context object (kill 1), not a time/epoch construct (kill 2), not a claim-species (kill 5), not a conflict-species (kill 3), not an edge (kill 4/REMAINS_DUE). `PREDICATE_INPUT_UNDECLARED` is a reason-register entry, not a new object (matches R02's own item-13 ruling that this doesn't count against the primitive ceiling). No v0.2 addition touches ResponsibleActorClass/Instance, DueID-as-object, BasisState-as-projection, or any of the other nine kills. **None of DUE-01's 15 kills are reintroduced under any name.**

---

## 10. Scope-fidelity check: **PASS**

- **F-3** (occurrence-species gloss, §14): v0.1's original sentence is preserved verbatim; v0.2 appends one new sentence scoped explicitly to *this repair's own additions* ("This v0.2 repair additionally introduces no new occurrence species") — this does not claim to resolve F-3's original open question about the gloss itself.
- **F-4** (ADJ-02 interface predicate / 8th UNRESOLVED item, §13): explicitly flagged unchanged — *"F-4's proposed 8th item — the concrete ADJ-02 interface predicate — is NOT added here; F-4 is out of this repair's scope."*
- **F-5** (pure-function framing): no language touching this appears anywhere in v0.2; §15's custody declaration explicitly states *"F-3, F-4, and F-5 remain open and unrepaired."*

None of F-3/F-4/F-5 are silently repaired, silently worsened, or silently claimed-closed. **Scope discipline held.**

---

## 11. Numbered findings list

**R03-1 — BLOCKING.** L-16 (§3) and L-8 EXTENDED (§7) check a rule's *declared* input surface against BasisRefSet classes ∪ contract_constants, but no mechanism anywhere in the artifact verifies that a rule's declared surface is actually *complete and truthful*. A rule could declare a narrow, compliant surface while its actual authored behavior consumes additional undeclared input (including input reachable precisely because `EvaluatorCanAccess(X)` is true for some `X ∉ BasisRefSet`) and pass admission-time review as written. The artifact acknowledges this residual via the phrase "or is found to consume" (§2, §7) and via the `PREDICATE_INPUT_UNDECLARED` reason-class (§4), but names no instrument, no witness constitution, and no procedure for how such consumption would ever be "found." This directly weakens: (a) the claim that specimen G is fully closed (§3 above — closed only for honest declarations), (b) the Third-wall ruling's claim that L-15/L-16 foreclose X's influence "regardless of access" (§4 above), and (c) the Repair Ledger's claim that the generalized L-3 doubly prohibits value-leakage (§6 above), since all three depend on L-16 having no gap of exactly this shape. A repair would need to either name a concrete detection mechanism (and give it its own witness constitution and §11 kill-matrix row exercising a *dishonest* declaration, not just an *absent* one) or explicitly add this as a named item in §13's UNRESOLVED register, matching the register's own stated purpose and the precedent R01 set with F-4.

**R03-2 — NON-BLOCKING (coupled to R03-1).** Item e's reason-class `PREDICATE_INPUT_UNDECLARED` is vocabulary-coherent but its trigger condition ("runtime detection… escaping admission-time detection") has no named apparatus, making it presently unfireable as specified. Should be resolved alongside R03-1, not independently — repairing R03-1's detection mechanism would automatically give this reason-class a real trigger.

**R03-3 — NON-BLOCKING (coupled to R03-1).** The amended L-3 (§4, item g) broadens the *set* of result values covered (NOTHING_DUE/DUE/UNRESOLVED, not UNRESOLVED alone) but not the *axis* of indistinguishability, which remains binary held-vs-absent rather than covering value-a-vs-value-b for different held values of X. The Repair Ledger's claim that this "doubly prohibits" value-leakage overstates what the text establishes independent of L-16's soundness. Non-blocking on its own terms (R02's literal item g is satisfied — the set-broadening is real and correct), but its practical guarantee inherits R03-1's gap.

No other findings survived the charter's attacks. F-1's closure (§2) and the minimality claim (§7) are clean; anti-resurrection and scope-fidelity are clean.

---

## 12. Overall verdict: **CHANGES_REQUIRED**

Trajectory note: v0.2 is a careful, disciplined, narrowly-scoped repair that correctly and completely implements everything R01 and R02 explicitly specified in their literal text — F-1's two components, items c/d/e/f/g all present, worded, and cross-referenced exactly where the repair ledger says they are, minimality correctly seated as R02 ruled it must be, zero kill-resurrection, zero scope creep into F-3/F-4/F-5. This is a *better-behaved* repair than v0.1 was as a candidate: v0.1 had one blocking gap (F-1) from an under-specified law; v0.2 has zero gaps against its own stated repair targets. Its single blocking finding here (R03-1) is not a failure to do what R01/R02 asked — it is a **new gap this chamber found by pursuing the charter's sharpest possible attack**, one layer deeper than either prior review tested: R02 tested whether a *honest* unenumerated dependency could hide from replay-testing (yes, and v0.2 closes it); this chamber tested whether a *dishonest* declared-surface claim could hide from admission-testing (yes, and v0.2 does not yet close it). The pattern is structurally identical to v0.1→R01: a load-bearing closure claim asserted as an outcome-sentence without a dedicated testable/enforceable mechanism. The estate's own discipline (which blocked v0.1 on exactly this shape of defect) requires the same standard applied here.

---

## 13. Exact repair surface needed (description only, no text authored)

A future bounded repair of R03-1 would need to contain:
- A named mechanism (or an explicit, honest refusal to claim one exists yet, moved into §13's UNRESOLVED register) for verifying that a rule's declared input surface is complete and truthful — e.g., a witness constitution for the declaration act itself, analogous to the witness constitution already required for basis-ref classes (§7/L-8).
- If no such mechanism is presently constructible, the "or is found to consume" language in §2 and §7 should be either removed (since it currently promises an unspecified capability) or explicitly demoted to a named, honestly-scoped UNRESOLVED item — following the same discipline v0.1 already applies to U-9, the clock authority, and the admitting-jurisdiction seat.
- A §11 kill-matrix row (or an explicit amendment to row 22) that exercises a *dishonestly declared* rule specifically — distinct from row 22's current framing, which tests only an *honestly declared but unenumerated* dependency (i.e., row 22 as written tests "declares… a function whose input is not in BasisRefSet," which is the honest case; a dishonest-declaration row would need to test "declares a narrower surface than it actually consumes").
- A corresponding note in the Third-wall ruling (§4 above) and in L-3's generalization (§6 above) acknowledging that both currently rest on L-16's soundness and would need re-verification once/if the detection mechanism is seated.

---

## 14. Terminal disposition line

**CANDIDATE_REVIEWED (v0.2 DELTA) — CHANGES_REQUIRED, ONE BLOCKING FINDING (R03-1), TWO NON-BLOCKING FINDINGS (R03-2, R03-3) COUPLED TO IT. `CandidateAuthored != CandidateReviewed != Ratified != Implemented` — none of those next states are entered by this review.**

## 15. Next lawful gate

Founder disposition on whether to authorize a further-narrowed repair of R03-1 (declaration-integrity mechanism or honest UNRESOLVED-register demotion) before any hostile review of a hypothetical v0.3, or a lineage-independent review scoped specifically to R03-1 if the Founder prefers a fresh chamber to re-adjudicate this finding independently first.

---

This chamber performed no writes, no repair, no implementation, no ratification, no push, and no mutation anywhere in `/Users/millysituated/RUORA` or any other location. All actions were `git show`/`git log`/`git branch`/`git for-each-ref` reads against the pinned commits c43a203, 6c4d318, 2b53dc1, 2b392e5, and b4c80e4. This message is the entire return.