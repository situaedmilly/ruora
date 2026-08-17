# GLITCH-0017 — Complete-Context Manifestation + Linked-GitHub Signal Protocol

```yaml
artifact_class: NOTEPAD_ENTRY
jurisdiction: OURSELF_GLITCH_SESSION
standing: RECORDED_CANDIDATE
control_effect: NONE
ratification_effect: NONE
mutation_authority: NONE
source: Founder-supplied session protocol candidate
```

## Observed shift

Founder introduced a session-level transport/custody protocol for large or semantically fragile outputs produced by CLAUDESELF or CODEXSELF:

```text
COMPLETE CONTEXT
-> INSPECTABLE ARTIFACT
-> VERIFIED BYTES
-> BOUNDED GIT CUSTODY
-> LINKED GITHUB PUBLICATION WHEN AUTHORIZED
-> COMPACT IDENTITY SIGNAL
-> CHATGPTSELF INSPECTION
-> FOUNDER CONTROLS NEXT TRANSITION
```

The protocol attempts to replace Founder-mediated copy/paste transport with exact artifact-reference transport.

## Core recovered law

```text
DO NOT TRANSPORT MEANING BY MEMORY
WHEN EXACT CONTEXT CAN BE TRANSPORTED BY REFERENCE.
```

This is a strong transport principle, but it creates several new non-collapse requirements.

## Required non-collapse

```text
SessionOutput != Artifact
Artifact != SourceTruth
ArtifactCreation != Adoption
GitCommit != Ratification
GitPush != ConstitutionalPromotion
GitHubPresence != CanonicalStanding
LinkedGitHubVisibility != Authority
ArtifactObservation != RuntimeObservation
GO_CHECK_IT != GO_APPROVE_IT
GO_CHECK_IT != GO_RATIFY_IT
```

## Runtime-separation law

The shared custody/handoff protocol must not collapse runtime identity:

```text
ClaudeSELFReality != CodexSELFReality
ClaudeSELFContext != CodexSELFContext
SharedManifestationProtocol != SharedRuntimeReality
```

A receiving SELF may inspect the manifested artifact but must not claim direct observation of the producing runtime when it only observed the artifact.

## New glitch risks

### 1. Artifact-totalization risk

A "complete context" artifact can become a shadow transcript or universal session dump if completeness is interpreted without a reportability boundary.

Required:

```text
CompleteReportableContext != EntirePrivateSessionState
CompleteContext != PrivateChainOfThought
CompleteContext != Secrets
```

The artifact must preserve all reportable context needed for independent review while excluding private cognition, credentials, tokens, and prohibited sensitive material.

### 2. Reference freshness risk

Exact-reference transport is only reliable if the reference still resolves to the intended bytes.

Required:

```text
ReferenceResolvedNow != ReferenceWasAlwaysFresh
BranchName != ImmutableSubjectIdentity
MutableBranchTip != ContentAddress
```

A compact handoff should prefer commit + artifact path + digest, not branch name alone.

### 3. Custody-channel authority risk

The transport protocol itself must never create write authority.

```text
ProtocolInstruction != FileMutationAuthority
FileMutationAuthority != CommitAuthority
CommitAuthority != PushAuthority
PushAuthority != RepositoryWideAuthority
```

### 4. Receiver-independence risk

The receiving SELF may independently inspect the artifact, but independence is not guaranteed merely because the runtime differs.

```text
CrossRuntimeReview != IndependentReviewAutomatically
ArtifactRetrieval != ReviewSeparation
```

Independence may require fresh session, bounded input, no repair authority, and explicit reviewer separation depending on the gate.

### 5. Transport success versus semantic sufficiency

A byte-perfect transfer may still omit the wrong thing if the producing SELF's reportable-context boundary was defective.

```text
ByteIntegrity != ContextSufficiency
ContextSufficiency != SemanticCorrectness
```

Therefore the receiving SELF must be allowed to return `SOURCE_CONTEXT_INCOMPLETE` even when hashes match.

## Candidate transport object

A future compact signal may be modeled as:

```yaml
CONTEXT_SIGNAL:
  runtime_identity:
  repository:
  branch:
  commit:
  artifact_path:
  artifact_digest:
  artifact_standing:
  predecessor_ref:
  source_target_digest:
  mutation_scope:
  publication_result:
  reportability_boundary:
  signal: GO_CHECK_IT
```

This is a transport/custody reference object only.

```text
ContextSignal != AuthorityGrant
ContextSignal != StandingPromotion
ContextSignal != ReviewVerdict
```

## Failure-state discipline

Preserve explicit stop classes such as:

```text
REPOSITORY_UNRESOLVED
DESTINATION_UNRESOLVED
LINKED_GITHUB_REMOTE_NOT_AVAILABLE
TARGET_INTEGRITY_MISMATCH
SOURCE_CONTEXT_INCOMPLETE
UNEXPECTED_STAGED_PATH
REPOSITORY_POLICY_BLOCK
BRANCH_PROTECTION_BLOCK
PUSH_REJECTED
ARTIFACT_VERIFICATION_FAILED
ARTIFACT_TRUNCATED
AUTHORITY_SCOPE_UNRESOLVED
```

Prime law:

```text
Failure != PermissionToImprovise
```

## Standing

```text
COMPLETE_CONTEXT_REFERENCE_TRANSPORT_CANDIDATE
```

This entry records the protocol's architectural value and attack surface. It does not ratify the protocol estate-wide.

## Next falsification

1. Use one exact large-output specimen from CLAUDESELF and one from CODEXSELF under equivalent publication authority.
2. Require commit+path+digest signals and independently retrieve both from linked GitHub.
3. Verify that receiver conclusions are based on artifact bytes, not Founder paraphrase.
4. Deliberately mutate a branch tip after signal issuance and prove the pinned commit still resolves correctly.
5. Deliberately provide a byte-perfect but semantically incomplete report and verify `SOURCE_CONTEXT_INCOMPLETE` can still fire.
6. Test private-repository metadata disclosure against the NOTEPAD privacy findings.
7. Test whether a producing session can manifest a review artifact without becoming the independent reviewer.
