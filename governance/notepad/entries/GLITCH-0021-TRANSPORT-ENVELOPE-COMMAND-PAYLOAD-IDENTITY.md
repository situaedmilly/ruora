# GLITCH-0021 — Transport Envelope / Command Payload Identity

```yaml
artifact_class: NOTEPAD_ENTRY
jurisdiction: OURSELF_GLITCH_SESSION
standing: RECORDED_CANDIDATE
control_effect: NONE
ratification_effect: NONE
implementation_effect: NONE
mutation_authority: NONE
predecessor: GLITCH-0017-COMPLETE-CONTEXT-LINKED-GITHUB-SIGNAL-PROTOCOL
source: Founder-directed recovery of transport/command constitution after WFC truncation witness
```

## Observed glitch

A transport envelope was complete while the command payload it referenced was absent.

Observed sequence:

```text
TRANSPORT ENVELOPE
+ BOOT 002
+ PAYLOAD BOUNDARY START
+ reference to COMPLETE ORIGINAL FOUNDER REVIEW WFC
+ PAYLOAD BOUNDARY END

but

COMPLETE ORIGINAL FOUNDER REVIEW WFC = ABSENT
```

The receiving HBCSELF correctly returned:

```text
STOP_WFC_INCOMPLETE
```

The semantic review did not begin and no verdict was issued.

This reveals a transport/command distinction not fully explicit in GLITCH-0017.

## Constitutional distinction

```text
TransportEnvelope != CommandPayload
EnvelopeComplete != PayloadComplete
PayloadBoundaryPresent != PayloadPresent
PayloadPresent != PayloadIntact
PayloadIntact != SubjectVerified
SubjectVerified != ReviewerIndependent
ReviewerIndependent != ReviewExecuted
ReviewExecuted != VerdictIssued
```

The command's identity therefore cannot be established by transport intent, wrapper identity, or payload label alone.

Prime law:

```text
COMMAND IDENTITY REQUIRES PAYLOAD IDENTITY,
NOT MERELY COMMAND INTENT.
```

## Original / reconstruction / new occurrence law

```text
RecoveredOriginal
!=
ReconstructedEquivalent
!=
NewReviewCommand
```

A missing original payload may not be silently regenerated and represented as the original command.

If exact original bytes are recoverable, they remain the preferred subject.

If exact original bytes are not recoverable:

```text
ORIGINAL_COMMAND_NOT_RECOVERED
```

must be preserved, and any replacement must be explicitly typed as a new command occurrence.

## Candidate transport object

```yaml
TransportEnvelope:
  envelope_id:
  envelope_version:
  transport_profile_ref:
  sender_ref:
  receiver_ref:
  payload_class:
  payload_identity_ref:
  payload_boundary_start:
  payload_boundary_end:
  expected_payload_lines:
  expected_payload_bytes:
  expected_payload_sha256:
  envelope_sha256:
  issued_at:
```

The envelope transports and identifies a payload. It does not substitute for it.

```text
EnvelopeRefersToPayload != EnvelopeContainsPayload
EnvelopeDigest != PayloadDigest
```

## Candidate command payload object

```yaml
CommandPayload:
  command_occurrence_id:
  command_class:
  command_version:
  complete_text:
  line_count:
  byte_count:
  sha256:
  first_heading:
  last_heading:
  terminus:
  source_occurrence_ref:
  standing:
```

The payload identity must be independently checkable from the transport envelope.

## Dual-digest law

A transport occurrence carrying a consequential command should preserve at least two distinct content identities:

```text
ENVELOPE_DIGEST
PAYLOAD_DIGEST
```

Required verification:

```text
VerifyEnvelope(envelope)
AND
VerifyPayload(payload)
AND
Envelope.payload_identity_ref == VerifiedPayloadIdentity
```

A valid envelope around an invalid, absent, partial, or substituted payload must fail closed.

## Transport admission chain

```text
ENVELOPE RECEIVED
        ↓
ENVELOPE VERIFIED
        ↓
PAYLOAD PRESENCE VERIFIED
        ↓
PAYLOAD IDENTITY VERIFIED
        ↓
PAYLOAD COMPLETENESS VERIFIED
        ↓
SUBJECT VERIFIED
        ↓
REVIEWER / EXECUTOR ELIGIBILITY VERIFIED
        ↓
COMMAND ADMITTED FOR TREATMENT
        ↓
COMMAND EXECUTION OR REVIEW MAY BEGIN
```

No stage inherits the next stage automatically.

## Failure states

```text
STOP_ENVELOPE_INCOMPLETE
STOP_PAYLOAD_ABSENT
STOP_PAYLOAD_INCOMPLETE
STOP_PAYLOAD_DIGEST_MISMATCH
STOP_PAYLOAD_IDENTITY_UNRESOLVED
STOP_ORIGINAL_COMMAND_NOT_RECOVERED
STOP_SUBJECT_DRIFT
STOP_INDEPENDENCE_NOT_ESTABLISHED
```

Prime failure law:

```text
TransportFailure != PermissionToReconstruct
MissingPayload != PermissionToInfer
SemanticConfidence != TransportIntegrity
```

## Relation to GLITCH-0017

GLITCH-0017 established:

```text
DO NOT TRANSPORT MEANING BY MEMORY
WHEN EXACT CONTEXT CAN BE TRANSPORTED BY REFERENCE.
```

GLITCH-0021 sharpens the command case:

```text
DO NOT TRANSPORT A COMMAND BY REFERENCE TO AN ABSENT PAYLOAD.
```

A reference is sufficient only when it resolves to the exact intended payload bytes under the declared transport contract.

```text
ReferenceTo(X) != PresenceOf(X)
WrapperIntegrity != PayloadCompleteness
ByteIntegrity != ContextSufficiency
```

## HOLLASELF / GOCHECKIT relation candidate

This glitch is compatible with the emerging HOLLASELF/GOCHECKIT separation without adopting new HOLLASELF doctrine:

```text
HOLLASELF-like signal
= compact transport signal

GOCHECK treatment
= receiver-local inspection workflow

TransportEnvelope
= payload-bearing or payload-addressing carrier

CommandPayload
= exact consequential instruction subject
```

Preserve:

```text
Signal != Payload
Payload != Authority
GOCHECK != Approval
TransportSuccess != SemanticValidity
```

## Falsifiers

1. Complete envelope with no payload -> `STOP_PAYLOAD_ABSENT`.
2. Complete envelope with truncated payload -> `STOP_PAYLOAD_INCOMPLETE`.
3. Correct line count but wrong bytes -> `STOP_PAYLOAD_DIGEST_MISMATCH`.
4. Correct payload label but substituted text -> identity mismatch.
5. Exact payload recovered from prior custody -> classify `RECOVERED_ORIGINAL`.
6. Semantically equivalent rewrite -> classify `RECONSTRUCTED_EQUIVALENT`, never original.
7. Founder issues replacement review command -> classify `NEW_REVIEW_COMMAND`.
8. Exact payload + contaminated reviewer -> `STOP_INDEPENDENCE_NOT_ESTABLISHED`.
9. Exact payload + subject drift -> `STOP_SUBJECT_DRIFT`.
10. Envelope hash passes while payload hash fails -> treatment prohibited.

## Standing

```text
TRANSPORT_COMMAND_CONSTITUTION_CANDIDATE
RECORDED_CANDIDATE
NONCANONICAL
NOT_RATIFIED
NOT_IMPLEMENTED
```

This entry records a recovered constitutional distinction and its observed failure witness. It does not ratify a transport protocol, create HOLLASELF, create a runtime command system, or grant execution authority.

## Next lawful pressure

```text
RECOVER OR AUTHOR AN EXACT COMMAND PAYLOAD
→ BIND ENVELOPE AND PAYLOAD IDENTITIES SEPARATELY
→ TRANSMIT TO A FRESH ELIGIBLE RECEIVER
→ VERIFY TRANSPORT
→ VERIFY SUBJECT
→ VERIFY ELIGIBILITY
→ ONLY THEN EXECUTE THE REQUESTED TREATMENT
```
