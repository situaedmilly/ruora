# RC0001-L1-CUSTODY-001 — L1 FOUNDER-SEAL CUSTODY MANIFEST

**ACT** Durable repository custody of the external L1 Founder-seal source.
**AUTHORIZATION** `AUTHORIZE_RC0001_L1_CONTAINER_CUSTODY_001_REISSUE` — Founder, 2026-08-13.
**RECORDED** 2026-08-13

---

## 1. Custody record

```
source_path          ~/.codex/sessions/2026/08/12/
                     rollout-2026-08-12T17-43-58-019ff7ee-9e35-7101-915e-74a0aae7d677.jsonl
source_sha256        cee97abe168b011e8cc2bf1d69009d755f8c744998302c76743ac432a7d81ebe
source_size          494995 bytes
source_mtime         2026-08-12 17:54:20

custody_copy_path    governance/evidence/RC0001-L1-CUSTODY-001/
                     L1-FOUNDER-SEAL-SOURCE-20260812.jsonl
custody_copy_sha256  cee97abe168b011e8cc2bf1d69009d755f8c744998302c76743ac432a7d81ebe
custody_copy_size    494995 bytes

custody_relation     BYTE_IDENTICAL_SNAPSHOT
authority_effect     NONE
semantic_effect      NONE
lineage_effect       DURABLE_CUSTODY_ONLY
```

Byte identity established by `cmp` (exit 0) and by independent SHA-256 recomputation of both
objects. The source digest was recomputed immediately before the copy, not carried forward from an
earlier observation.

## 2. Founder evidence-class disposition

`FOUNDER_DISPOSITION_RC0001_L1_EVIDENCE_CLASS_001` classifies this object as
**`DOCTRINE_ROOT_CUSTODY_EVIDENCE`**.

It is **not** a member of the `GOVERNED_NON_GIT_RUNTIME_EVIDENCE` class described by `.gitignore`
(`/runtime/agentbridge/`, `chambers/`, `projects/`). That class governs operational, runtime, and
disposable evidence stores whose continuing canonical value does not depend on repository-level
custody. L1 differs in kind: it is a root provenance and authority witness already digest-pinned by
RC-0001 governance artifacts, and loss of its exact source bytes would make those lineage claims
non-reproducible.

```
RUNTIME_EVIDENCE  ≠  DOCTRINE_ROOT_CUSTODY_EVIDENCE
```

The ruling applies **only** to L1 custody.

## 3. Mutation-admissibility basis — scoped quiescence

The RC-0001 governance corpus was **not** globally quiescent at execution: the artifact
`…SEMANTICPROGRAM-v0.5-CANDIDATE.md` was under active authorship by a concurrent front throughout.

Founder ratification established that quiescence is evaluated over the **authorized read/write-set**,
not the whole corpus. Every object in this act's write-set was witnessed stable across three
observations with an identical instrument:

| Witness | Observed at | L1 source | HEAD | index | target path |
|---|---|---|---|---|---|
| 1 | 2026-08-13 22:29:21 | `cee97abe…` | `7387fe4` | 0 staged | absent |
| 2 | 2026-08-13 22:31:15 | `cee97abe…` | `7387fe4` | 0 staged | absent |
| 3 | 2026-08-13 22:40:24 | `cee97abe…` | `7387fe4` | 0 staged | absent |
| execution | immediately pre-copy | `cee97abe…` | `7387fe4` | 0 staged | absent |

`…v0.5-CANDIDATE.md` is **outside this write-set**, was not read as evidence for this act, and was
not touched. Its concurrent mutation does not bear on this custody act. CR-004
(`7ce5feac…`) and v0.4 (`7c680b02…`) were byte-stable across the same interval.

Staging was exact-path only. HEAD and index were re-verified immediately before staging.

## 4. Extraction reproducibility

The extraction procedure downstream RC-0001 artifacts use against this container is **recovered
exactly**, not reconstructed — preserved verbatim in Cold Review 004 §0.1:

```
jq -j 'select(.ordinal==N) | .payload.content | map(.text) | join("\n")' <container>
```

`EXTRACTION_RECIPE_RECONSTRUCTION_REQUIRED` does **not** apply.

## 5. What this custody act does not do

- **Does not ratify L1 content.** The bytes are preserved; their meaning is not adjudicated here.
- **Does not widen L1 authority.** Authority is unchanged in kind and scope.
- **Does not reinterpret the Founder seal.** No clause, pin, or extraction is re-read or restated.
- **Does not supersede the original Codex rollout.** The external session artifact remains the
  origin; this is a snapshot of it, not a replacement for it.
- **Does not amend `.gitignore`.** No ignore rule is added, removed, or altered.
- **Does not make runtime evidence Git-governed.** The non-Git runtime evidence class is untouched;
  no general rule is established by this act.
- **Does not admit CR-004**, authorize a v0.5 mutation, open REALRAP or any other front, or unfreeze
  HBC (`e350205`) or RealityIR.

## 6. Record debt remaining after this act

The RC-0001 lineage is still uncommitted: v0.4, CR-004, and the other RC-0001 artifacts remain
untracked in the working tree. This act secures the **root witness only**. The eleven-file
digest-bound admission packet remains outstanding under
`RC0001_CR004_RECORD_ADMISSION_002`.
