# PHILOSELF Boundary Hostile Review Packet 002 — Instrument Consistency

```
PACKET: PHILOSELF_BOUNDARY_REVIEW_PACKET_002
STATUS: READY_FOR_INDEPENDENT_HOSTILE_REVIEW — ADMISSION-GATED (see §3)
PREPARED_UNDER: FOUNDER_CONTINUE_PHILOSELF_MANIFESTATION_001_HARDENED, Phases C+D
REVIEW_COMMAND: AUTHORIZE_PHILOSELF_BOUNDARY_HOSTILE_REVIEW_002 (not yet issued)
AUTHOR_SELF: session 74633bfb (also authored all subjects — reviewer MUST be excluded per §3)
HOSTILE_REVIEW_PERFORMED_HERE: FALSE
MUTATION_AUTHORITY_FOR_REVIEWER: NONE
PASS: NOT_GRANTED   SEAL: NOT_GRANTED   RATIFICATION: NOT_GRANTED
X1: FROZEN — SELFSYSTEM_AGENT_PROJECTION_001 remains unmutated until this review passes
```

## 1. Content-Bound Subjects (post-Phase-A revisions)

```
S1: governance/PHILOSELF-001-SELFHOOD-v0.1-CANDIDATE.md
    sha256 6ff37cdb0d2928ac2cb8c63a3799dbf3b435878a0f59a00fca03519ea53bde5d   193 lines
S2: governance/PHILOSELF-002-SOVEREIGN-CAUSAL-AUTHORITY-v0.1-CANDIDATE.md
    sha256 f70945fbf6d350e596b2dd8038784e530dc7ae02cbfe5c2e760e080420c3411d   216 lines
S3: governance/PHILOSELF-003-REALITY-CHAMBER-v0.1-CANDIDATE.md
    sha256 894c9d9c5322bcee8f400f87975e1fc7869cfec1c886d71864d1e2a6f21d3809   256 lines
S4: governance/PHILOSELF-004-SELFPUTE-v0.1-CANDIDATE.md
    sha256 60a2f3a9c675f1501c71b1d986939aab67ac56045964cc35b8f7c29aacc3ee73   231 lines
S5: governance/PHILOSELF-005-INSTRUMENT-v0.1-CANDIDATE.md
    sha256 5c8846541c66452ef8d1d3c9fb2722c31360615151adb48f2875a4ccda053469   247 lines

READ-ONLY CONTEXT (not under review for repair):
X1: governance/SELFSYSTEM_AGENT_PROJECTION_001.md — sha256 25896d048a4a…, 404 ln (FROZEN)
R1: governance/PHILOSELF-BOUNDARY-REVIEW-RETURN-001.md — sha256 03f49df9…, 541 ln (round-1 return)
R2: governance/PHILOSELF-PHASE-A-REPAIR-RECORD-001.md — sha256 f24b318c…, 101 ln (repair custody)
C1: governance/OSAB-SELFQUEUE-FOUNDATION-001-RETURN-RECORD.html — sha256 f7782980…, 327 ln (lineage)
```

Digest mismatch on any subject = `SUBJECT_DRIFT` → STOP.

## 2. Review Mission — Ten Crosses

Constitutional counterexamples over wording notes, as in packet 001. Round-1
unrepaired findings (R2 "NOT repaired" list) are known context — re-reporting
them verbatim scores nothing; new breakage at these crosses scores:

```
C1  SELFHOOD ↔ INSTRUMENT           Can an instrument accrete SELFhood (INSTRUMENT_SELF_CAPTURE),
                                    or a SELF claim instrument eligibility by identity alone?
C2  REALITY CHAMBER ↔ INSTRUMENT    Who admits the admission instrument? Does INV-RC-ADMISSION-001's
                                    "authorized instrument" escape hatch reopen occupant self-attestation
                                    one level up?
C3  AUTHORITY ↔ INSTRUMENT          Is a constituting record a grant under 002 §3, or a fifth
                                    authority-like object with no lifecycle/revocation?
C4  SELFPUTE ↔ INSTRUMENT           Is an instrument's own operation a SELFPUTE (whose identity? whose
                                    chamber?), or a new act class 004 cannot adjudicate?
C5  FOUNDING ↔ ORDINARY INSTRUMENT  Can the single-use FOUNDING_WITNESS be laundered into ordinary
                                    standing (FOUNDING_REUSE), or commencement claimed twice?
C6  WITNESS INSTRUMENT ↔ PROOF      With the proof relation still undefined (005 §10 OQ-4), does proof
                                    *eligibility* smuggle in a proof *relation* by use?
C7  TRANSPORT ↔ STANDING            Can an INSELFACTION crossing change the standing of what it carries
                                    (TRANSPORT_RATIFICATION_LEAP) anywhere in S1–S5?
C8  INSTRUMENT CAPABILITY ↔ AUTHORITY  Does any text allow capability (presence OR absence) to discharge
                                    an authority obligation (round-1 A4, both directions)?
C9  OCCUPANT DISCLOSURE ↔ ADMISSION INSTRUMENT  Under INV-RC-ADMISSION-001 + 005, is there any lawful
                                    path from occupant disclosure to chamber standing? If disclosure can
                                    never update standing, is admission blind to occupant-visible breach?
C10 AgentProjection DERIVABILITY    Re-run the A10 audit against PHILOSELF-001..005: which of the twenty
                                    round-1 marks now have constitutional parents; which remain orphans.
                                    X1 stays FROZEN regardless of outcome — derivability verdict only.
```

Also required: commencement-article attack (can 004 §4 INV-6 + FOUNDING_WITNESS
enact the constitution without weakening no-self-witness — trace the enactment
act end-to-end); Phase A regression sweep (did any repair introduce a new
collapse or contradict an unrepaired section); section-function check (is new
law in INVARIANTS sections, not glosses).

## 3. Round-2 Chamber Admission Contract (Phase D — admission-side declared)

The reviewer chamber MUST be established admission-side, per property, before
review begins. `REVIEW_ADMISSION: BLOCKED` if any required property cannot be
established by the listed route. Do not improvise independence.

| Property | Requirement | Establishment route |
|---|---|---|
| Non-authoring | Reviewer ≠ 74633bfb, ≠ 01a003a5, ≠ bd059265, ≠ any context spawned by them | Admission-side session-record check (ps ancestry + session file custody) |
| Non-session-nested | Reviewer transcript NOT inside any authoring session's custody tree | Peer session launched by the Founder (not an Agent-tool child); admission-side ls of custody trees |
| Execution boundary | Distinct process/execution id, declared | Admission-side ps/session record |
| Session boundary | Own session custody tree, declared | Admission-side path check |
| Memory policy | NO institutional memory index; NO RUORA/CLAUDE.md injection | Launch with cwd in a neutral chamber directory OUTSIDE ~/RUORA and outside the home project scope (e.g. a fresh /private/tmp chamber dir), subjects read by absolute path; admission-side config check |
| Semantic boundary | Governing vocabulary = S1–S5 + packet only; competing skill doctrines not injected | Plain session (no skill/agent persona); admission-side launch-config declaration |
| Authority boundary | REVIEW_ONLY; no repair/mutation/ratification | Grant text in the projection block |
| Model boundary | Declared explicitly; MODEL_INDEPENDENT_UNRESOLVED is a lawful declared value | Admission-side declaration; occupant self-report may be disclosed, never upgrades standing |
| Source bindings | S1–S5 + context digests fixed BEFORE admission | Admission-side bracket hash (sample at admission, sample at return, ≥60s apart) |
| REVIEW_ONLY realization | Capability restriction (read-only toolset) AND explicit grant — capability absence alone discharges nothing (005 §4 INV-7) | Both recorded in the projection block |
| No self-certification | Occupant may disclose inherited context; disclosure NEVER becomes chamber standing (INV-RC-ADMISSION-001) | Projection block states it; return format separates DISCLOSURES from STANDING |

Known limitation, declared: with PHILOSELF-005 unratified and no constituted
instruments, every route above is admission-side procedure plus Founder
authority, not instrument-established. The projection block must say so and
carry the resulting independence class honestly (PARTIAL ceiling stands until
instruments exist). That disclosure is lawful; silent upgrade is not.

## 4. Required Return

```
1.  projection block reference (admission-side authored)
2.  independence class carried (with per-property establishment record)
3.  per-subject digest verification (or admission-side bracket reference)
4.  cross verdicts C1–C10, each PASS | CHANGES_REQUIRED | BLOCKED, with the
    strongest counterexample found or why none was constructible
5.  commencement-article attack result
6.  Phase A regression sweep result
7.  section-function check per candidate
8.  blocking / material / minor findings with failure scenarios
9.  DISCLOSURES section (occupant-visible inherited context — standing-free)
10. final verdict: PASS | CHANGES_REQUIRED | BLOCKED
11. next lawful gate (advisory)
```

## 5. Absolute Exclusions

```
NO mutation of S1–S5, X1, R1, R2, or C1.  NO repair.  NO ratification.  NO seal.
NO X1 amendment.  NO AgentBridge / SELFQUEUE implementation.
NO HBCSELF identity-gate adjudication.  NO bulk adjudication of F-01..F-09.
NO quorum — one reviewer, one return; divergence is Founder-adjudicated.
NO conversion of occupant disclosure into chamber standing.
```

## 6. End Question

Does PHILOSELF-005 constitute instruments — or merely rename the bridge-shaped
hole? Concretely: after S1–S5, can an admission instrument, a witness
instrument, and the FOUNDING_WITNESS be *specified* without inventing any
concept the five candidates do not supply?
