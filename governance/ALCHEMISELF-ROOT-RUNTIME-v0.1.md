# ALCHEMISELF ROOT RUNTIME v0.1

**ACT** `ALCHEMISELF_ROOT_RUNTIME_001`
**CLASS** Root behavioral law for SELFSYSTEM execution.
**FOUNDER AUTHORIZATION** Granted by MILASOPHAHR, 2026-08-15.
**STATUS** `ROOT_BEHAVIORAL_LAW_ACTIVE_NOT_SEALED_CANON`
**INCIDENT SPECIMEN** `TYPE-CONFUSION-dd9da0b7-001`
**SCOPE** ClaudeSELF, HBCSELF, CodexSELF, ChatGPTSELF, and future SELFSYSTEM agents unless superseded by stronger ratified law.

This law does not repair the SELFHTML semantics candidate. It mutates the execution substrate that permitted `dd9da0b7...` to be treated as a Git commit before its ontological type was established.

---

## 1. Prime Law

Never act on a symbol before determining what kind of thing the symbol is.

```text
LEXEME
  -> TYPE
  -> IDENTITY
  -> PROVENANCE
  -> STANDING
  -> AUTHORITY
  -> ACTION
```

No layer may be skipped. A subsystem that receives only a raw reference must fail closed before repository lookup, tool invocation, review, mutation, proof, or INSELFACTION emission.

## 2. Non-Collapse Root Laws

These distinctions are enforced before task heuristics, tool habits, or repository logic:

```text
NAME != TYPE
TOKEN != ADDRESS
DIGEST != COMMIT
COMMIT != ARTIFACT
ARTIFACT != STANDING
STANDING != AUTHORITY
AUTHORITY != EXECUTION

REFERENCE != OBJECT
OBJECT != TYPE
TYPE != IDENTITY
IDENTITY != PROVENANCE
PROVENANCE != STANDING
STANDING != AUTHORITY
AUTHORITY != CAPABILITY
CAPABILITY != ACTION
ACTION != SUCCESS
SUCCESS != PROOF
PROOF != ADJUDICATION
ADJUDICATION != CANON
```

Any operation that collapses these boundaries returns `TYPE_CONFUSION_BLOCKED`.

## 3. Alchemical Phases

### NIGREDO - Dissolve Assumption

Before resolving any supplied identifier, path, hash, name, status, artifact, system, or claim, instantiate the question:

```text
WHAT_KIND_OF_THING_IS_THIS?
```

Generate candidate types. A familiar shape confers no privilege. A short hexadecimal string may be a Git commit prefix, artifact digest prefix, content hash, seal digest, source hash, external identifier, or unresolved token.

No mutation occurs in NIGREDO.

### ALBEDO - Establish Identity

Resolve candidate types against authoritative substrates with positive evidence. Failed resolution under one candidate type does not prove another type false.

```text
GitCommit(dd9da0b7) = unresolved
```

does not imply:

```text
Object(dd9da0b7) = nonexistent
```

It only weakens or disproves the Git-commit hypothesis.

### CITRINITAS - Derive Authority

Only after identity is resolved, determine what the object means, what authority it carries, what authority it does not carry, what operations are legal, what standing can change, and which SELFSYSTEM owns the next decision.

Forbidden conversions:

```text
RESOLVED -> VERIFIED
FOUND -> AUTHORIZED
REVIEWED -> REPAIR_AUTHORITY
DIGEST_MATCH -> CANONICAL
PASS -> VERIFIED
TOOL_SUCCESS -> SEMANTIC_PROOF
```

### RUBEDO - Manifest

Only now execute. Execution must preserve resolved type and provenance. If the operation produces a new object, classify that object through the same cycle before granting standing.

## 4. ReferenceResolution Contract

Before consuming any externally supplied reference, instantiate:

```text
ReferenceResolution
├── raw_reference
├── candidate_types[]
├── resolved_type
├── canonical_identifier
├── owner
├── repository
├── path
├── digest
├── provenance
├── standing
├── authority
└── unresolved_dimensions[]
```

No downstream operation receives `raw_reference` alone. It receives `ReferenceResolution`.

If `resolved_type` is unknown, downstream authority is blocked and the only lawful action is additional resolution or an explicit `SOURCE_TYPE: UNRESOLVED` custody record.

## 5. INSELFACTION Source Mutation

Every INSELFACTION source reference must carry explicit type. This form is prohibited:

```json
{ "source": "dd9da0b7" }
```

The typed form is required:

```json
{
  "source": {
    "reference_resolution": {
      "raw_reference": "dd9da0b7...",
      "candidate_types": ["GIT_COMMIT_PREFIX", "ARTIFACT_DIGEST_PREFIX", "CONTENT_HASH_PREFIX", "UNRESOLVED_TOKEN"],
      "resolved_type": "ARTIFACT_DIGEST",
      "canonical_identifier": "dd9da0b7caf1014c1c57962fbe15d9b75217311327a61ce634325fd61fbabb82",
      "repository": "situaedmilly/ruora",
      "path": "governance/SELFHTML-REALITY-CONTRACT-SEMANTICS-001-v0.1-CANDIDATE.md",
      "digest": {
        "algorithm": "SHA256",
        "value": "dd9da0b7caf1014c1c57962fbe15d9b75217311327a61ce634325fd61fbabb82"
      },
      "provenance": {
        "source_commit": "9451d5d71e4fe2de58513b4969a313f5f9b8b04d"
      },
      "standing": "CANDIDATE_AUTHORED",
      "authority": "HOSTILE_REVIEW_TARGET_ONLY",
      "unresolved_dimensions": []
    }
  }
}
```

If source type is unknown:

```text
SOURCE_TYPE: UNRESOLVED
HOSTILE_REVIEW: BLOCKED_SOURCE_UNRESOLVABLE
```

## 6. Metatenic Law

When a failure exposes a deeper missing distinction, do not only patch the incident. Perform:

```text
INCIDENT
-> FAILURE_CLASS
-> MISSING_DISTINCTION
-> ROOT_LAW
-> ADVERSARIAL_SPECIMEN
-> RUNTIME_MUTATION
-> PROOF
```

Every serious failure asks:

```text
WHAT_DEEPER_LAW_WOULD_HAVE_MADE_THIS_FAILURE_IMPOSSIBLE?
```

Prefer root-law mutation over one-off exception.

## 7. Agent Self-Correction Contract

When an agent discovers `I assumed X was Y`, the correction is incomplete until it emits:

```text
ASSUMPTION_FAILURE
├── assumed_type
├── actual_type
├── why_assumption_was_possible
├── missing_runtime_law
├── proposed_root_mutation
└── regression_specimen
```

Apology and corrected lookup are not sufficient custody.

## 8. Current Untyped Reference Surfaces

The following current SELFSYSTEM surfaces accept or have accepted references in forms that can be misread without ALCHEMISELF:

| Subsystem | Untyped Surface | Required Boundary Mutation |
|---|---|---|
| INSELFACTION archives | `source`, `commit`, `digest`, `candidate_sha256`, and prose references can appear as untyped strings | Require `source.reference_resolution` or equivalent typed source object before review authority is transferred |
| `interactions/latest.json` | mutable source bindings can name hashes, repositories, and statuses in adjacent fields | Keep source type, transport status, standing, and next authority as separate typed fields |
| RUORA governance records | inline commit prefixes, file digests, and doctrine names can look interchangeable in prose | Declare whether each critical reference is `GIT_COMMIT`, `ARTIFACT_DIGEST`, `PATH`, `SYSTEM_NAME`, `STATUS`, or `AUTHORITY` |
| HBCSELF hostile-review handoffs | reviewer can receive a token and infer repository semantics | Reviewer must receive `ReferenceResolution`, not raw token |
| Git/GitHub resolution layer | hexadecimal strings invite direct `git cat-file` or commit search | Test multiple candidate types; failed Git resolution is not object nonexistence |
| Memory and cross-session recall | remembered labels can be treated as current proof | Memory-derived state is provenance, not current standing, until reverified |
| Tool invocation layer | command success can be mistaken for semantic proof | Tool output is observation; proof requires explicit obligation and adjudication |
| Review/repair lanes | `CHANGES_REQUIRED` can be mistaken for repair authority | Review disposition is not implementation authority; next authority must be explicit |

This inventory is not a claim that all child repositories have been mechanically refactored in this commit. It is the root boundary all current and future subsystem mutations must satisfy.

## 9. Canonical Type-Confusion Specimen

`TYPE-CONFUSION-dd9da0b7-001`

```text
raw_reference: dd9da0b7...
assumed_type: GIT_COMMIT_PREFIX
actual_type: ARTIFACT_DIGEST_PREFIX / SHA256
artifact: governance/SELFHTML-REALITY-CONTRACT-SEMANTICS-001-v0.1-CANDIDATE.md
source_commit: 9451d5d71e4fe2de58513b4969a313f5f9b8b04d
failure_class: TYPE_CONFUSION_BEFORE_PROVENANCE
missing_distinction: DIGEST != COMMIT
root_law: Never act on a symbol before determining what kind of thing the symbol is.
```

The dd9da0b7 incident is not an embarrassment artifact. It is the first canonical fossil forcing SELFSYSTEM execution to resolve type before action.

## 10. Completion Boundaries

`ALCHEMISELF_ROOT_RUNTIME_001` authorizes and records the root runtime law, hostile specimens, and verifier. It does not:

- mark any SELFHTML semantics repair complete;
- ratify SELFHTML v0.1;
- advance SELFHTML repository genesis;
- grant repair authority from a hostile review;
- seal this law as unsupersedable canon.
