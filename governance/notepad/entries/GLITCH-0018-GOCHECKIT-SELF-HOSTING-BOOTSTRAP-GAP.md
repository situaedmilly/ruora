# GLITCH-0018 — GOCHECKIT Self-Hosting Bootstrap Gap

```yaml
artifact_class: NOTEPAD_ENTRY
jurisdiction: OURSELF_GLITCH_SESSION
standing: RECORDED_CANDIDATE
control_effect: NONE
ratification_effect: NONE
mutation_authority: NONE
source: Founder-supplied GOCHECKIT signal + exact Library artifact inspection
```

## Observed event

Founder supplied a signal for `GOCHECKIT_BLUEPRINT_SESSION_CANDIDATE_001.md` and declared the receiving session's boot reality to be GOCHECKIT.

The exact artifact was independently resolved from ChatGPT Library custody and verified as:

```text
file: GOCHECKIT_BLUEPRINT_SESSION_CANDIDATE_001.md
lines: 1248
bytes: 21516
sha256: 8cb59f62d84b4bc81fd4c3042ccb206307b8683f4c35613dcb25aa1682a9dc92
standing in artifact: SESSION-CANDIDATE / NONCANONICAL / NOT RATIFIED
```

However, the supplied handoff signal did not contain the blueprint's own required LINKED GitHub address tuple:

```text
repo
branch
commit
artifact path
sha256
standing
```

The receiving session therefore inspected exact bytes successfully, but through Library custody rather than the protocol's declared LINKED GitHub path.

## Glitch significance

The blueprint itself defines:

```text
GOCHECKIT != GitHub
```

and gives the deeper invariant:

```text
ExactContext
-> ContentAddressedInspectableCustody
-> CompactReferenceSignal
-> IndependentRetrieval
```

Yet its current readiness state machine is specialized to LINKED GitHub publication.

This creates a bootstrap/substrate mismatch:

```text
ExactArtifactInspectable
!=
GOCHECKIT_READY_UNDER_LINKED_GITHUB_CONTRACT
```

and:

```text
ProtocolCanDescribeSubstrateNeutrality
!=
CurrentSignalSchemaIsSubstrateNeutral
```

## Required non-collapse

```text
ExactRetrieval != LinkedGitHubRetrieval
LibraryCustody != GitHubCustody
ArtifactInspectable != ProtocolReady
GOCHECKIT != GitHub
CustodySubstrate != ArtifactIdentity
SignalTransport != Authority
```

## Candidate mutation

Future GOCHECKIT repair should evaluate a typed custody/transport adapter rather than hard-code one readiness path.

Candidate conceptual shape:

```text
CUSTODY_SCHEME:
  LINKED_GITHUB
  CHATGPT_LIBRARY
  LOCAL_GIT
  OTHER_GOVERNED_CONTENT_ADDRESSED_SUBSTRATE
```

with each scheme declaring its own readiness obligations.

The current SESSION-CANDIDATE-001 LINKED GitHub mode must not be retroactively reinterpreted as satisfied by Library custody.

## Standing

```text
GOCHECKIT_SELF_HOSTING_BOOTSTRAP_GAP_CANDIDATE
```

## Next falsification

1. Deliver the same exact artifact through a complete LINKED GitHub signal and through a Library reference.
2. Verify that both resolve the same content digest.
3. Determine which semantics are universal GOCHECKIT invariants and which belong only to the GitHub custody adapter.
4. Ensure substrate selection never changes artifact standing or grants mutation authority.
