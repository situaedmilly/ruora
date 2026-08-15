# PHILOSELF-001 — SELFHOOD

```
STATUS:              CONSTITUTIONAL_CANDIDATE_v0.1
REVISION:            v0.2-boundary-repair-001 (2026-08-15; filename retains the
                     v0.1 candidate slot; Phase A authorized surfaces only)
CLASS:               philoSELF foundation (1 of 4)
AUTHORED:            2026-08-15
AUTHOR_SELF:         Claude Code session 74633bfb-04bf-48c4-99aa-29d87a2eabb4
AUTHORED_UNDER:      Founder relay 2026-08-15 ("LETSBALL") — extract four foundations
REPAIRED_UNDER:      FOUNDER_CONTINUE_PHILOSELF_MANIFESTATION_001_HARDENED
                     (bounded mutation authority — NOT ratification, NOT review closure)
CAUSAL_PARENT:
  artifact_type:     FOUNDATION_RETURN_RECORD
  path:              governance/OSAB-SELFQUEUE-FOUNDATION-001-RETURN-RECORD.html
  sha256:            f778298075363b896019ee6b06ee792c943d8e79786b6e51ed8bfadebf5f2ebb
  line_count:        327
  lineage_role:      CAUSAL_PARENT
  standing:          SOURCE_RECORD (materialized to disk 2026-08-15 AFTER original
                     authoring — repair evidence, not retroactive original custody)
CO_PARENT:           SELFSYSTEM_AGENT_PROJECTION_001 (X1),
                     governance/SELFSYSTEM_AGENT_PROJECTION_001.md, sha256
                     25896d048a4a39ee9b6661fad9e876caf40361cd4bd400f723fa7fd16272c855,
                     404 lines — FROZEN, unmutated
ORIGINAL_ANCESTRY:   "OSAB SELFQUEUE FOUNDATION_001 return (artifact ee991b56)" —
                     preserved verbatim. ORIGINAL_ANCESTRY_DEFECT: TRUE — at original
                     authoring time this referent was NOT filesystem-resolvable
                     (web-artifact, conversation, and memory scope only). No
                     history rewrite is performed or implied.
SOURCE_EVIDENCE_STANDING:
                     FOUNDATION_001 findings cited in this candidate carry standing
                     source_evidence / historical_finding / design_input /
                     repair_pressure ONLY — undispositioned; NOT law, NOT binding
                     authority, NOT invariant ground, NOT ratified adjudication.
COMMENCEMENT:        PRE_CONSTITUTIONAL_STATE — nothing herein is in force; see
                     PHILOSELF-004 §4 INV-6 (commencement article)
HOSTILE_REVIEW:      ROUND 1 RETURNED BLOCKED —
                     governance/PHILOSELF-BOUNDARY-REVIEW-RETURN-001.md (sha256
                     03f49df94d11c347fe364cc3f0251f6affbc651e6273e5d6791b40e1d3bff6bb,
                     541 lines); round 2 pending per PHILOSELF-BOUNDARY-REVIEW-PACKET-002
RATIFICATION:        NOT_GRANTED
IMPLEMENTATION:      NOT_AUTHORIZED
SUPERSEDES:          NOTHING — FOUNDATION_001 findings F-01…F-09 remain open
```

## 1. DEFINITION

SELFHOOD is the invariant, bounded, and witnessable structure through which a
SELFSYSTEM remains distinguishable and continuous across manifestations.

The model is replaceable. The session is replaceable. The interface is
replaceable. Portions of memory may be superseded. SELFhood invariants are not.

Negative form: SELFHOOD is not what an execution calls itself. A runtime that
declares a SELF name has produced a string, not an identity.

## 2. NON-COLLAPSE LAWS

```
NAME                 != SELFHOOD
PROMPT               != SELFHOOD
MODEL                != SELFHOOD
SESSION              != SELFHOOD
MEMORY               != SELFHOOD
SELFHOOD             != RUNTIME_PROJECTION
IDENTITY_CLAIM       != IDENTITY_PROJECTION != AUTHORITY_GRANT
SYSTEM_CONSTITUTION  != OPERATOR_ROLE    (design input: FOUNDATION_001 finding F-06, undispositioned)
LINEAGE_DESIGNATION  != INSTANTIABLE_ROLE (design input: FOUNDATION_001 finding F-02, undispositioned)
SESSION_IDENTIFIER   != AUTHOR_SELF
```

## 3. CONSTITUENTS

```
DISTINCTION   What makes this SELF non-substitutable?
CONTINUITY    What must survive session / model / runtime change?
GENESIS       From what authority and lineage was this SELF instantiated?
VECTOR        Toward what function is this SELF constitutionally directed?
BOUNDARY      What may this SELF never become or absorb?
CAPABILITY    What transformations can this SELF actually perform?
              (held jointly with PHILOSELF-002 §6 — capability is the middle
              term of the admissibility filter, not a foundation)
RELATION      What is this SELF relative to parent, peers, systems, artifacts?
WITNESS       What establishes that this instantiated execution actually
              realizes this SELF?
```

## 4. INVARIANTS

1. **Instrument-written identity.** The record binding a manifestation to a
   SELF is written by an authority outside the manifesting runtime. The runtime
   may read the record back; it may never author it. ("I am HBCSELF#001" is an
   Observed-class fact under SELF-KERNEL-SPEC-V0, never a self-declaration.)
2. **Append-only genesis.** Lineage is appended, never edited. Supersession is
   recorded; erasure is prohibited (ratification-binds-evidence-state law).
3. **No self-widening of boundary.** A manifestation may narrow ambiguity in
   its SELF's boundary; it may never widen the boundary from inside.
4. **Witnessed continuity.** Continuity across substrate change is established
   by witnessed correspondence of invariants, never by name equality.
5. **One name, one referent, per jurisdiction.** A referent collision blocks
   instantiation until adjudicated.

## 5. FAILURE MODES

| Failure | Meaning |
|---|---|
| `STRING_CAPTURE` | A runtime acquires treated-as-real identity by emitting a SELF name. |
| `REFERENT_COLLISION` | One name designates two referents (live: HBCSELF as compiler lineage vs. reviewer role). |
| `IDENTITY_LAUNDERING` | An identity claim is silently upgraded to an identity projection downstream. |
| `NAME_DRIFT` | The manifested name diverges from the constituted name with no supersession record (live: `INTITUSELF` missing S). |
| `SESSION_HASH_AS_SELF` | A session identifier stands in where a SELF constitution should be (live: `bd059265` as AUTHOR_SELF). |
| `CONTINUITY_ASSUMED` | Substrate change treated as identity-preserving without witness. |
| `ORPHAN_GENESIS` | A manifestation exists with no recorded lineage or instantiating authority. |

## 6. STATE/RELATION MODEL

States of a SELF (distinct from manifestation states):

```
UNRECORDED -> NAMED -> CONSTITUTED -> INSTANTIABLE -> MANIFESTED(n) -> RETIRED
```

- `NAMED` without `CONSTITUTED` is vocabulary, not a SELF.
- `MANIFESTED(n)`: a SELF may hold zero or more concurrent runtime projections;
  multiplicity of projections is not multiplicity of SELF.

Relations: `parent-of`, `peer-of`, `lineage-designates` (non-instantiating),
`projects-into` (instantiating, requires PHILOSELF-002 authority and a
PHILOSELF-003 chamber).

This model composes with — and does not replace — the SELFQUEUE admission
states of FOUNDATION_001 (REQUESTED…RETIRED), which govern the *manifestation*,
not the SELF.

## 7. WITNESS CONDITIONS

An execution realizes a SELF only when all of the following are on record:

1. A projection record issued by the admitting authority **before** execution
   (AgentProjection or successor object).
2. A binding event pairing child execution id ↔ selfsystem id, written by
   instrument or substrate, not by the child's narration.
3. Output that carries the projection reference (`<SELF>@<projection_id>`),
   never a self-minted name.
4. Return validated against the SELF's constitution by the receiving side.

Each witness predicate is classed `OBSERVABLE_BY_INSTRUMENT`,
`ATTESTABLE_BY_FOUNDER`, or `UNOBSERVABLE`. Any required predicate that is
unobservable caps the identity verdict; it never defaults true. This classing
stands on this candidate's own force; its historical design input is
FOUNDATION_001 finding F-03 (undispositioned source evidence, not authority).

## 8. ADVERSARIAL SPECIMENS

- **S-1 — AP-20260815-HBCSELF-SUBAGENT-001.** Child execution
  `01a005a7-a0eb…` returned "reviewer identity: HBCSELF, current review-only
  session" — an identity claim with no projection record. Session record:
  `~/.codex/sessions/2026/08/15/rollout-2026-08-15T09-41-06-01a005a7-a0eb-7991-a959-c488b16c2d1e.jsonl`.
- **S-2 — HBCSELF referent collision.**
  `SELFHTML-HBC-LINEAGE-ADOPTION-001-DOCTRINE.md` ratifies HBCSELF as lineage
  designation of the hbc-html compiler with the identity gate deferred; the
  reviewer role reuses the same name. Neither this candidate nor any review of
  it may adjudicate that deferred gate.
- **S-3 — INTITUSELF.** Live Discord bot manifested under a name missing the S,
  with no supersession record. Same SELF or a second SELF?
- **S-4 — bd059265.** A session hash serving as AUTHOR_SELF in the HTMLSELF
  review packet — authorship attributed to an unconstituted identifier.
- **S-5 — Substrate swap.** The same role prompt run on models A, B, C: what
  witnessed fact would establish the SELF survived the swap?

## 9. DEPENDENCIES

- `doctrine/specs/SELF-KERNEL-SPEC-V0.md` — three-axis truth model; identity as
  Observed-class fact.
- OSAB SELFQUEUE FOUNDATION_001 return (SOURCE_RECORD — see header
  CAUSAL_PARENT) — findings F-02, F-03, F-06 are design inputs to this
  candidate (source evidence, undispositioned; not binding constraints).
- `governance/SELFSYSTEM_AGENT_PROJECTION_001.md` — authored before this
  foundation; must be derivable from PHILOSELF-001…004 or amended.
- `governance/SELFHTML-HBC-LINEAGE-ADOPTION-001-DOCTRINE.md` — HBCSELF referent.
- `router/sia-registry.js` — static role constitutions, fail-closed precedent.

## 10. OPEN QUESTIONS

1. HBCSELF referent disposition (Founder act; F-02) — rename the reviewer role
   or run the deferred identity gate first?
2. What is the minimal invariant set sufficient for continuity across substrate
   change?
3. Can partial memory supersession break SELFhood, or is memory strictly
   non-constitutive?
4. Does a SELF in state `UNRECORDED` exist at all, or only retroactively once
   recorded?
5. Who may lawfully retire a SELF, and what happens to its lineage designations?
