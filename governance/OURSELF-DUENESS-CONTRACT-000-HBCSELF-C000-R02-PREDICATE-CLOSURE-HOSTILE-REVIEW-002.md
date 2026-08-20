# OURSELF-DUENESS-CONTRACT-000 — HBCSELF-C000-R02 PREDICATE-CLOSURE HOSTILE REVIEW 002

```
CUSTODY STATUS:    REVIEW ARTIFACT — CUSTODY-BOUND POST-EXECUTION AND
                   POST-RELAY, on separate Founder authorization
                   ("custody-bind C000-R02, then authorize the widened
                   v0.2 repair").
CHAMBER EXECUTED:  2026-08-20 by HBCSELF-C000-R02 (fresh context-blind
                   subagent; narrow-scope hostile semantic review; read-only;
                   no writes performed; not a repair agent, not an author)
SCOPE DISCIPLINE:  predicate closure ONLY. F-2 through F-5 (R01's other
                   findings) explicitly NOT re-adjudicated; they stand as
                   R01 left them.
SUBJECT:           OURSELF-DUENESS-CONTRACT-000-v0.1-CANDIDATE @ c43a203,
                   read against R01's F-1 finding @ 6c4d318, DUE-01
                   necessity discipline @ b4c80e4 (background only) — all
                   re-verified PASS by this chamber independently.
PRIMARY RESULT:    PredicateClosure EXTENDS_F1 — F-1's scoped repair is
                   extensional/behavioral (numbered law + replay row);
                   predicate closure is intensional/structural
                   (admission-time input-surface check). Decisive
                   countercase: specimen G, a deterministic external
                   function with an unbound/unenumerated input — passes
                   every replay test indefinitely while remaining
                   constitutionally open. Ruling: NOT SUBSUMED_BY_F1, NOT
                   ORTHOGONAL, NOT CONTRADICTS — a strict superset: F-1's
                   floor plus a genuine additional structural requirement.
VERDICT:           CHANGES_REQUIRED_TO_REPAIR_SCOPE (not a re-verdict of
                   the whole candidate; R01's CHANGES_REQUIRED/F-1 stands).
                   Blocking finding R02-1: F-1's literal scoped repair is
                   necessary but NOT sufficient — could pass while
                   specimen-G-class violations remain silently possible.
MINIMALITY:        PASS — 0 new formal primitives required. Substance of
                   predicate closure expressed by extending existing §2
                   (rule field), §7/L-8 (admission gate), and the existing
                   reason register (one new reason-class entry, not a new
                   register) — not by minting Predicates(C)/Inputs(P) as
                   proposed in the pressure return.
ADDITIONAL FINDING: the anti-leak law L-3 is broader in its true scope than
                   currently written — an undeclared read of held X can
                   leak X's VALUE through the primary DUE/NOTHING_DUE
                   channel, not merely its presence through UNRESOLVED.
                   Generalization needed (item g).
MICROAUTO2_WITHOUT_PREDICATE_CLOSURE: UNSAFE — the bounded-write-set safety
                   claim becomes unfalsifiable, not merely untested, if an
                   unenumerated dependency can move D outside the
                   instrumented set. Independent of §14's current
                   implementation ban.
REPAIR SURFACE NAMED (not authored): (c) generalize §2's "no clock" to a
                   full enumerated ambient-read exclusion; (d) extend
                   §7/L-8's admission gate to check declared input surface
                   against BasisRefSet-classes ∪ contract-pinned-fields,
                   INADMISSIBLE on violation; (e) one reason-class addition
                   to the existing register; (f) resolve the foreign-SELF-
                   state ambiguity, coupled to R01's still-open F-2; (g)
                   generalize L-3's anti-leak principle beyond
                   UNRESOLVED-only/presence-absence-only.
RELAY RECORD:      full return relayed unmodified to the Founder before
                   this custody act, per Founder command.
CUSTODY LAW:       ReviewCustodied != RepairAuthorized. This commit binds
                   the review to lineage; it authorizes NOTHING by itself
                   — the widened v0.2 repair is a separate act, authorized
                   in the same Founder transmission but executed as its
                   own commit, after this one.
TRANSMISSION NOTE: Chamber text below is preserved verbatim, including its
                   leading and trailing lines. This custody header is the
                   only authoring-session addition. Bytes recovered from
                   the chamber's own session transcript (agent
                   a53b4b7c00444e275), final message, unmodified; 17,673
                   B, sha256
                   e95fa527edf6706e7a7cf56a28d1116f102715c59d6228c4185c4d99bd225dad.
```

---

# HBCSELF-C000-R02 — Return

## 1. Target integrity

- `c43a203` verified present, `git cat-file -t` → `commit`. Subject line: "governance: author OURSELF-DUENESS-CONTRACT-000 v0.1 CANDIDATE (semantic doctrine only)." Parent: `7c4486b`. Confirmed via `git show --no-patch`.
- `6c4d318` verified present, parent = `c43a203` (exact match — direct child, correct lineage). Subject: "governance: custody-bind HBCSELF-C000-R01 lineage-independent hostile review 001 of DUENESS-CONTRACT-000 v0.1."
- `b4c80e4` verified present, parent `055841c`, consistent with the chain both documents cite.
- Full lineage walk (`git log --oneline --graph`) on `governance/living-symbolic-transmission-morphology-000-custody` confirms linear order: `b4c80e4 → 7c4486b → c43a203 → 6c4d318`, matching both artifacts' own custody headers.
- **Remote-containment check:** `git branch -vv` shows this branch carries **no** `[github/...]` upstream marker (unlike several sibling worktree branches that do). `git ls-remote github | grep -E "c43a203|6c4d318"` returned **empty**. `git branch -r --contains c43a203` also empty. **Both target commits are UNCUSTODIED on the remote** — consistent with R01's own note ("consistent with the candidate's own UNPUSHED declaration"). This session adds no push; containment status is unchanged by this review.
- **PIN VERIFICATION: PASS** for both files, both fully read via `git show <sha>:<path>` (not by filesystem path), full text reproduced above in this session's tool output.

## 2. Reviewer independence (item 0)

This chamber performed **no** v0.1 authorship, **no** R01 authorship, **no** repair, **no** v0.2 participation. It holds **no** mutation authority, **no** repair authority, **no** implementation authority. All actions this session were `git show`/`git log`/`git branch`/`git ls-remote` reads only. No file was written, edited, staged, or committed.

## 3. R01/F-1 identity — exact restatement

From `6c4d318`, F-1 (the sole BLOCKING finding of R01):

> **F-1 — BLOCKING.** Attacks: §3's unlabeled closed-basis law ("Anything outside the BasisRefSet cannot influence the result") and §11's kill matrix. The non-basis-perturbation invariant — the candidate's answer to the charter's sharpest attack (M2) — is asserted only as prose, carries no L-number or T-number..., and has no dedicated conformance-testable row in §11.... A repair would need to: (a) promote the closed-basis invariance to a first-class numbered law stated as a testable equivalence (same admitted basis + contract, arbitrary mutation of any x∉BasisRefSet ⇒ disposition and DispositionID unchanged), integrated into the §10 law table; (b) add a corresponding row to the §11 kill matrix exercising exactly this perturbation, distinct from row 15's narrower held-vs-absent indistinguishability test.

R01's custody header additionally records, explicitly **uncustodied and not adjudicated by R01's own charter**:

> POST-RETURN PRESSURE HELD (uncustodied, NOT metabolized here): Founder's "predicate closure" attack — ClosedBasis + OpenPredicate = OpenComputation; a contract rule may consult ambient state (e.g. current_system_health()) even when the basis is properly enumerated. Not tested by this chamber's charter; recorded in memory as scope-candidate matter for a future review pass or v0.2, authored by no one yet.

This is decisive procedural fact: R01 explicitly did not adjudicate predicate closure. This review is the first adjudication of it.

## 4. Root kill verdict (item 1)

Countermodel: C contains predicate P reading x∉B from ambient state. Against the actual text of c43a203: §3 states "Anything outside the BasisRefSet cannot influence the result; an evaluator observed consuming an unlisted input is nonconformant," and §2 defines `rule` as "total, computable, authored function **over the admitted basis**... no model evaluation, no prose parsing, no clock." By these two clauses, the candidate's own text **already declares** such a C malformed/nonconformant — B could not lawfully be called closed under such a C, by the artifact's own words. The root claim is **not structurally killed** by this countermodel; the candidate already asserts the exclusion.

But the exclusion is asserted, not enforced: §3's clause is exactly the prose R01 already found PRESENT_AS_PROSE_ONLY (no L/T-number, no kill-matrix row), and §2's "no clock" is a *named, specific* exclusion, not a general ambient-read exclusion. So: **root claim survives at the level of stated intent; its enforceability gap is identical territory to F-1, not a new kill.**

## 5. Predicate closure verdict (item 2 — necessity ruling)

The literal candidate law as proposed (`∀P∈Predicates(C), Inputs(P) ⊆ B ∪ ContractConstants(C)`) introduces a new quantified object, `Predicates(C)`, not present in c43a203's vocabulary (the schema treats `rule` as one atomic "authored function," never decomposed into named predicates). Under anti-mint discipline, this exact form is **not necessary** — the same substance is expressible by strengthening two *already-adopted* fields instead of minting a new one:
- §2's `rule` clause (which already says "over the admitted basis," but only names one specific forbidden channel — clock — not a general one), and
- §7/L-8's contract-admission gate (which already performs an admission-time structural check, for witnessability of named classes — extending its check to input-surface-declaration is the same kind of act, not a new kind of act).

**Ruling: the SUBSTANCE of predicate closure is necessary; the literal proposed FORM (new `Predicates(C)`/`Inputs(P)` objects) is not.** Necessity is real but must be seated as an extension of existing structures, not a new primitive.

## 6. M2/non-basis-perturbation under the candidate's own text (item 3)

Under c43a203 as committed: D is *claimed* to remain invariant under x∉B perturbation (§3's prose), but this is **merely claimed in unlabeled prose** — not established by any numbered law, not exercised by any §11 kill-matrix row. This is not a new finding; it is R01's M2 grading (`PRESENT_AS_PROSE_ONLY`) confirmed independently against the primary text.

## 7. Ambient-read matrix (item 4)

| # | Specimen | Ruling | Reason |
|---|---|---|---|
| A | reads current clock | **INVALID** | §2 explicitly forbids "no clock"; §3 explicitly: "There is no Epoch input... time-triggered dueness is BLOCKED until a clock authority is seated." Named and closed. |
| B | reads current branch HEAD | **VALID** | Not a named exclusion anywhere; covered only by the general unlabeled §3 prose — exactly the M2/F-1 gap generalized to a concrete ambient-repo-state case. |
| C | reads foreign SELF state | **UNRESOLVED** | Straddles §3's basis-admission membrane's third conjunct ("no exposure or independence membrane (ADJ-02 stratum) protects the ref") — which stratum owns this is exactly R01's non-blocking F-2 (tripartite-wall) gap, itself unresolved. |
| D | reads hidden model context | **INVALID** | §3 explicitly requires evaluator non-cognition ("the evaluator must be non-cognitive, or its own basis reads constitute exposure crossings..."). Named and forbidden, even though the concrete ADJ-02 interface is unspecified (R01's F-4, non-blocking). |
| E | reads network availability | **VALID** | Same category as B — no named exclusion; only the general unlabeled prose applies. |
| F | invokes a nondeterministic function | **INVALID** | Directly contradicts T-1 (numbered root theorem) and §2's "computable" requirement; already caught by T-1's own existing kill-matrix replay tests (500× same-basis, restart, R4) — same-basis nondeterminism surfaces there. |
| G | invokes a deterministic external function whose input/state is unbound into B | **VALID** | The sharpest case: determinism defeats T-1's replay-test detection (same output across a stable test window), and the input dependency is unenumerated, so no reviewer-authored perturbation row can target it. This is the case predicate closure exists to close, and F-1's proposed *behavioral* fix cannot close it by construction. |

## 8. Functional-purity verdict (item 5)

"Same B + same C → same D" (T-1 as written) is **not sufficient** if C may perform undeclared reads — specimen G demonstrates a scenario where T-1 could hold empirically across every executed replay while B is not actually closed, because the hidden dependency's value happened not to change during testing. A stronger property is required: closed predicates enforced at admission time, not only tested at replay time.

**PureFunctionNecessityDisposition: PREDICATE_CLOSURE_REQUIRED**

## 9. Undeclared-read failure semantics (item 6)

Two cases, both already representable in the existing vocabulary — **no new enum value required**:
- **Detected at contract admission** (structural declaration check, extending L-8's existing gate pattern): the contract is **INADMISSIBLE**, per L-8's own precedent language — "Refusal at admission, never admitted-then-perpetually-UNRESOLVED." This is not a `D` value at all; it is a pre-evaluation gate rejection, already the candidate's own mechanism for a structurally analogous case (unwitnessable classes).
- **Detected at runtime** (an evaluator caught consuming an unlisted input, per §3): **UNRESOLVED**, with a new *reason-class* appended to the existing typed reason register (which already holds four entries: CONTRACT_SET_INCOHERENT, BASIS_REF_UNESTABLISHABLE, BASIS_MEDIA_UNKNOWN, SUBJECT_SEAT_TIER_UNADJUDICABLE) — e.g. `PREDICATE_INPUT_UNDECLARED`. This is a register *entry*, not a register *object*, and not a fourth top-level `D` value.

No silently-admitted value, no inferred value, no model intuition, no dynamically expanded B is used in either path — both fail closed within the existing three-value + reason-register machinery.

## 10. Anti-leak result (item 7)

L-3 as written governs only bytewise indistinguishability **between UNRESOLVED-over-held and UNRESOLVED-over-absent**. A predicate-closure violation (an undeclared read of held X) is a **broader** leak than L-3 currently scopes: it can make `DUE` vs `NOTHING_DUE` itself vary with X's actual (unadmitted) value — not merely reveal X's presence/absence through an UNRESOLVED channel, but leak X's *value* through the primary disposition channel. **This is a new leak channel beyond what L-3, as currently worded, covers** (same underlying principle, generalized from UNRESOLVED-only/presence-absence-only to all three D-values/full-value-leak) — it is not created by predicate closure itself, but by its *absence*, and it strengthens rather than duplicates L-3.

## 11. PredicateClosure ↔ F-1 relation — PRIMARY RESULT (item 8)

**EXTENDS_F1.**

Reasoning: Both F-1 and predicate closure attack the same textual location (§3's unlabeled closed-basis clause) and the same underlying claim (T-1's sufficiency). They are not the same defect under a different name (ruling out SUBSUMED_BY_F1 in either direction) because they operate at different layers: F-1's repair, as R01 scoped it, is purely **extensional/behavioral** — promote the claim to a numbered law and test it via replay perturbation rows. Predicate closure is **intensional/structural** — require the rule's declared input surface to be checked against B at admission time. Specimen G above shows these are not interchangeable: a finite, reviewer-authored replay matrix (F-1's fix as literally scoped) cannot detect a deterministic dependency on unenumerated external state, because no one knows to author a perturbation row against a dependency they don't know exists. Only an admission-time declaration-and-check requirement (extending L-8, the candidate's own existing precedent for exactly this kind of structural gate) can close that residual gap.

They are not CONTRADICTS_F1 (no opposing direction — both push toward the same strengthening), not ORTHOGONAL_TO_F1 (same subject, same clause, not independent), not UNRELATED, not UNRESOLVED (the relation is determinate given the text). Predicate closure is a **strict superset**: F-1's fix as a necessary floor, plus an additional admission-time structural requirement that F-1's stated repair scope does not itself contain.

## 12. Minimality result (item 9)

No revival of EvaluationContext, Epoch, DueClaim, DUENESS_CONFLICT, a new witness object, a new register, or a new evaluator species — none of these are implicated. Predicate closure's substance is fully expressible as:
- an extension to §2's `rule` field (generalize "no clock" to a declared, enumerated exclusion of all ambient-read channels, not one named case),
- an extension to §7/L-8's admission gate (check the declared input surface ⊆ admitted basis-ref classes ∪ contract's own pinned fields),
- promotion of §3's prose per F-1's already-scoped repair, and
- one additional reason-class in the *existing* reason register.

**Minimality: PASS. Zero new formal primitives required** — see item 5/9 for why `Predicates(C)`/`Inputs(P)` as literally proposed should NOT be minted as new objects.

## 13. New primitives required

**0.** (One new reason-*value* — e.g. `PREDICATE_INPUT_UNDECLARED` — is a register *entry*, not a new primitive/object, and does not count against this ceiling.)

## 14. MICROAUTO2_WITHOUT_PREDICATE_CLOSURE (item 10)

**UNSAFE.**

Reasoning (report only, no implementation touched): MICROAUTO's genesis-specimen safety case (§12, L-14 "BoundedNoEffectWitness") depends on an instrumented write-set being a *complete* account of what could be affected. If predicate closure is unresolved, an undeclared/unbound dependency (specimen G's case) could influence a disposition without appearing in the named, instrumented write-set — making the "bounded" claim itself unfalsifiable rather than merely untested. This is independent of MICROAUTO's current prohibition status (§14 already bars its implementation entirely); the ruling concerns whether the *safety claim* would be trustworthy once attempted, not whether it is currently authorized.

## 15. Blocking findings

**R02-1 — BLOCKING (widens F-1's binding repair scope).** F-1's repair, as R01 literally scoped it (promote closed-basis prose to a numbered law + add one behavioral kill-matrix row), is necessary but **not sufficient** to close the predicate-closure gap. Left as scoped, a repair could satisfy F-1's letter (numbered law, passing replay tests) while specimen-G-class violations (deterministic, unbound, unenumerated external dependencies) remain silently possible. The repair surface must be widened — see item 17.

No other blocking findings arise from this narrow charter; F-2 through F-5 stand as R01 left them (out of this review's scope, not re-adjudicated).

## 16. Final verdict (narrow-scope disposition)

**CHANGES_REQUIRED_TO_REPAIR_SCOPE** — not a re-verdict of the whole candidate (R01's CHANGES_REQUIRED / F-1 stands), but a determination that when F-1 is eventually repaired, its scope as R01 wrote it must be **widened**, not executed as literally stated, or the repair will leave a live, previously-unadjudicated gap (predicate closure / specimen G) unclosed.

## 17. Exact repair surface (description only — no text authored)

A lawful future repair of F-1 (whoever authors it, under whatever future authorization) would need to contain, in addition to R01's original (a)/(b):
- (c) A structural extension to §2's `rule` field: require the authored rule to declare its complete input/read surface at authoring time, generalizing "no clock" into an enumerated exclusion of all ambient-read channels (clock, repository/HEAD state, network, foreign SELF state, hidden model context, undeclared memory, environment) — not merely restate "over the admitted basis" as prose.
- (d) A structural extension to §7/L-8's contract-admission gate: the gate must check the declared input surface (per (c)) against BasisRefSet classes ∪ the contract's own pinned fields, and rule the contract INADMISSIBLE if any declared or discovered input lies outside that union — using L-8's own existing "refusal at admission, never admitted-then-perpetually-UNRESOLVED" language as precedent, not a new mechanism.
- (e) One reason-class addition to the existing typed reason register (e.g., for the runtime-detection path, per item 6) — not a new register.
- (f) Explicit disposition of the C-specimen ambiguity (foreign SELF state) — this is coupled to R01's already-standing, non-blocking F-2 (tripartite wall) and should be closed in the same repair pass if F-2 is being touched, to avoid re-opening the same stratum question twice.
- (g) A note generalizing L-3's anti-leak principle beyond UNRESOLVED-only/presence-absence-only, per item 10 above, so that closing predicate closure does not leave a narrower but still-live value-leak channel through DUE/NOTHING_DUE.

No replacement law text, no numbering, no matrix-row wording is authored here — this chamber names what the surface must contain, not its content.

## 18. Next lawful gate

The next lawful act is Founder disposition on whether to authorize a widened F-1 repair (incorporating items (c)–(g) above) as part of, or instead of, R01's originally scoped (a)/(b) repair, before any v0.2 authoring begins.

---

This chamber performed **no writes, no repair, no implementation, no ratification, no push, and no mutation** anywhere in `/Users/millysituated/RUORA` or any other location. All actions were `git show`/`git log`/`git branch`/`git ls-remote` reads against the pinned commits `c43a203`, `6c4d318`, and `b4c80e4`. This message is the entire return.