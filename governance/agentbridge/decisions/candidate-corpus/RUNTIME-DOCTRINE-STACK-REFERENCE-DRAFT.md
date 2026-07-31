---
STATUS: REFERENCE_DRAFT
CANONICAL: NO
DECOMPOSITION_PROPOSED: YES
DECOMPOSITION_EXECUTED: NO
REQUIRES_RECONCILIATION_WITH:
- ruora.md
- self_axiom.md
- existing RUORA doctrine corpus
---

# OURSELF Runtime Doctrine Stack

The deep pattern across websites, SaaS products, mobile apps, games, spatial systems, and agent interfaces is this:

The product surface may change. The runtime laws should not.

Apple’s current guidance emphasizes preserving context across platforms, adapting to multiple input methods, and treating accessibility as foundational. Android similarly treats quality as a combination of user value, experience, technical quality, privacy, and safety across many device forms. Unreal separates persistent runtime systems, session rules, replicated state, controllers, actors, and world presentation. AWS’s SaaS guidance elevates tenant context into a first-class architectural construct that must travel through every layer. W3C defines accessibility through perceivable, operable, understandable, and robust behavior, with testable conformance rather than aesthetic intention.

These disciplines converge into a foundation for RUORA runtime doctrine.

⸻

The root distinction

RUORA Doctrine
defines why the technology exists
Domain Doctrine
defines what the experience means
Runtime Doctrine
defines how experience behaves over time
Authority Doctrine
defines who may change canonical truth
Host Doctrine
defines where the experience executes
Projection Doctrine
defines how reality becomes perceivable
Evidence Doctrine
defines what proves an event occurred
Memory Doctrine
defines what survives

The same runtime doctrine can govern:

* websites,
* SaaS platforms,
* mobile applications,
* iMessage-style games,
* console games,
* desktop systems,
* Bubble applications,
* Unreal experiences,
* AI agents,
* spatial realms,
* future hardware.

Not because they use identical code.

Because they obey identical manifestation laws.

⸻

Doctrine 1: The Phenomenon Precedes the Interface

Every product must begin with a human phenomenon, not a screen inventory.

Phenomenon
→ intended state transition
→ runtime behavior
→ projection
→ components

Bad foundation:

Dashboard
Profile
Settings
Notifications

Correct foundation:

Orientation
Recognition
Coordination
Commitment
Recovery
Competition
Belonging
Completion
Inheritance

A FriendshipLAB page might specialize mutual recognition.

A game screen might specialize anticipation under uncertainty.

A SaaS dashboard might specialize operational clarity.

The visual system is downstream.

Runtime requirement

Every Realm Manifest must declare:

{
  "phenomenon": "mutual recognition",
  "participant_state_before": "unlocated",
  "participant_state_after": "relationally oriented",
  "failure_state": "false familiarity"
}

⸻

Doctrine 2: Every Product Is a Persistent Runtime, Not a Collection of Pages

A page is a projection into a runtime that may survive navigation, backgrounding, device interruption, or world transitions.

Android explicitly requires apps to behave correctly when they enter the background, return from the app switcher, sleep, lock, lose network access, or experience other interruptions. Unreal similarly distinguishes persistent GameInstance systems from level-specific rules and world objects.

Runtime
├── identity
├── current state
├── pending intents
├── authority receipts
├── environment
├── active projection
├── evidence
└── recovery position

Law

Navigation must not be mistaken for lifecycle.

Changing pages does not necessarily:

* start a new session,
* end a task,
* clear pending intent,
* discard evidence,
* reset atmosphere,
* terminate the participant’s current phenomenon.

⸻

Doctrine 3: Intent Is Not Canonical Mutation

The participant expresses intent.

The runtime carries it.

Authority decides whether reality changes.

Participant
→ intent
→ validation
→ authority
→ receipt
→ reconciliation
→ projection refresh

Permanent laws:

CLICK ≠ MUTATION
DISPATCH ≠ ACCEPTANCE
CALLBACK ≠ RECEIPT
RECEIPT ≠ TRUTH unless validated and correlated

This applies everywhere:

* a Bubble form,
* a SaaS billing change,
* a multiplayer action,
* a mobile gesture,
* a game purchase,
* an agent command,
* a relationship declaration.

Product-specific authority

Bubble application:
Bubble backend may be Authority Adapter
SaaS:
tenant-aware service may be Authority Adapter
Game:
authoritative server may be Authority Adapter
Offline application:
local signed ledger may be Authority Adapter
Read-only website:
no mutation authority exists

⸻

Doctrine 4: Host and Authority Must Remain Separate

A technology may perform both roles, but the roles must never collapse conceptually.

Host Adapter
= rendering, input, device capability, execution environment
Authority Adapter
= validation, canonical mutation, revision, receipts

Examples:

React host + Supabase authority
HTML host + Bubble authority
Unreal host + multiplayer server authority
Mobile host + OURSELF backend authority
ChatGPT Site host + read-only API authority

This allows substrate migration without rewriting domain meaning.

⸻

Doctrine 5: Every Runtime Needs Orthogonal State Planes

Do not create one giant state enum.

Different concerns must remain independent.

Universal planes:

Lifecycle
Projection
Authority
Connectivity
Attention
Evidence
Recovery
Environment

A SaaS runtime might use:

Lifecycle:
BOOTING / ACTIVE / SUSPENDED / TERMINATED
Authority:
SYNCED / PENDING / CONFLICTED / REFUSED
Connectivity:
ONLINE / DEGRADED / OFFLINE
Projection:
OVERVIEW / DETAIL / EDIT / REVIEW

A game might use:

Session:
LOBBY / ACTIVE / PAUSED / COMPLETE
Player:
SPAWNING / ALIVE / DOWNED / ELIMINATED
Network:
SYNCHRONIZED / PREDICTING / RECONCILING

Unreal’s gameplay framework already separates persistent game instance, game rules, shared game state, player state, controllers, pawns, cameras, and world objects instead of forcing all behavior into one class.

Law

A state should belong to the smallest runtime organ that can truthfully own it.

⸻

Doctrine 6: Projection Is a Registration, Not a Kernel Branch

No universal runtime should contain:

if (page === "friendship") {}
if (page === "journey") {}
if (page === "momentum") {}

Instead:

Kernel
→ Projection Registry
   ├── friendship.connection
   ├── journey.today
   ├── momentum.booking
   ├── mancav3.weekly-picks
   └── ureel.orientation

Each projection package declares:

* input state,
* derived view state,
* permitted intents,
* atmosphere,
* geometry,
* accessibility behavior,
* host requirements,
* exit behavior.

Substrate test

A projection must survive movement between compatible hosts without redefining domain meaning.

⸻

Doctrine 7: Atmosphere Is Runtime State

Visual energy cannot be a decorative CSS layer pasted on after logic.

It must be derived from lawful state.

State
→ atmosphere tokens
→ geometry
→ motion
→ sound
→ interaction rhythm

Examples:

PENDING
→ softened contrast
→ restrained motion
→ visible uncertainty
CONFLICTED
→ split geometry
→ divergent light
→ explicit comparison
AUTHORIZED
→ focus convergence
→ stable spatial anchor
COMPLETED
→ release of interaction pressure
→ preserved evidence visibility

Law

Visual intensity must never imply authority that does not exist.

A glowing “success” state before a receipt arrives is an authority lie.

⸻

Doctrine 8: Motion Must Communicate Causality

Motion is not garnish.

It answers:

* What changed?
* Why did it change?
* Where did it come from?
* What remains?
* What is now possible?

Apple advises using predictable positioning and natural transitions to preserve context, and warns that intense or uncontrolled motion can create discomfort, especially in spatial environments.

Motion classes

ORIENTATION MOTION
reveals location
CAUSAL MOTION
shows what caused a transition
AUTHORITY MOTION
shows pending, accepted, refused, conflicted
MEMORY MOTION
preserves continuity across projection changes
EXIT MOTION
shows what is released and what survives

Prohibition

No motion may:

* conceal delay,
* simulate progress,
* imply success prematurely,
* obstruct focus,
* override reduced-motion preference,
* move the world without participant control in immersive contexts.

⸻

Doctrine 9: Accessibility Is a Runtime Capability

Accessibility cannot be a final audit.

W3C organizes accessible systems around being perceivable, operable, understandable, and robust. WCAG 2.2 adds explicit concerns including unobscured focus, target size, alternatives to dragging, consistent help, redundant entry, and accessible authentication. Its principles also apply beyond websites through WCAG2ICT guidance for mobile and non-web software.

The environment runtime must detect or receive:

reduced motion
contrast preference
text scaling
screen reader
keyboard
touch
pointer
voice
switch input
safe areas
viewport
audio availability
haptic availability

Each phenomenon must have more than one perceptual route.

Light
+ text
Sound
+ visual indicator
Spatial change
+ focus movement
Color
+ shape or label
Gesture
+ button or keyboard action

Law

No Realm may require one body, one sense, one input method, or one device posture.

⸻

Doctrine 10: Interruption Is a First-Class Runtime Event

Real life interrupts software.

Software must not treat interruption as corruption.

Interruption classes:

USER INTERRUPTION
switching apps, pausing, leaving
DEVICE INTERRUPTION
sleep, lock, rotation, battery pressure
NETWORK INTERRUPTION
offline, timeout, partial response
AUTHORITY INTERRUPTION
service unavailable, stale receipt, conflict
SOCIAL INTERRUPTION
another participant acts
TEMPORAL INTERRUPTION
deadline passes, window changes, day continues overnight

Android’s current quality guidance explicitly recommends testing workflows while notifications, calls, network changes, battery changes, and system load interrupt the experience.

Every interruption needs

pause law
persistence law
resume law
expiry law
conflict law
participant explanation

⸻

Doctrine 11: Evidence Must Be Native to the Runtime

Observability cannot be added only after deployment.

Every meaningful mutation should create evidence:

intent_id
actor
target
source_revision
authority
receipt_status
result_revision
occurred_at
processed_at
artifact_hash
failure_reason

The runtime needs three observability planes:

TRACES
What path did the event take?
METRICS
How often and how well is the system behaving?
LOGS / RECEIPTS
What exact fact was recorded?

For RUORA, this becomes:

No declaration without execution.
No execution without evidence.
No evidence without memory.

Distinction

Product analytics answer:

What are users doing?

Runtime evidence answers:

What did the system claim, attempt, authorize, refuse, and reconcile?

⸻

Doctrine 12: Memory Must Be Layered

Do not call all stored data “memory.”

View Memory
temporary local UI condition
Session Memory
survives navigation or temporary interruption
Canonical Memory
authority-owned state
Evidence Memory
immutable or versioned receipts
Semantic Memory
derived meaning
Participant Memory
explicitly retained personal context
Institutional Memory
governance, revisions, decisions, doctrine

Law

Derived memory must never silently overwrite source memory.

An inference may become a new linked record.

It may not erase the evidence it interpreted.

⸻

Doctrine 13: Tenant Context Must Travel Through the Whole SaaS Runtime

For SaaS products, tenant identity cannot exist only in the database query.

AWS describes tenant context as a first-class security construct that must travel through the architecture alongside user identity, while tenant isolation must prevent one tenant from accessing another tenant’s resources.

Universal SaaS receipt:

{
  "tenant_id": "tenant-001",
  "actor_id": "user-007",
  "intent_id": "intent-123",
  "authority_policy": "tenant-admin",
  "resource_scope": "tenant-001/project-4"
}

Law

IDENTITY WITHOUT TENANT CONTEXT
=
INCOMPLETE AUTHORIZATION

Required across:

* UI state,
* API calls,
* queues,
* logs,
* caches,
* search,
* background jobs,
* model prompts,
* exports,
* audit records.

⸻

Doctrine 14: Games Require World, Rule, Player, and Projection Separation

A game runtime is not merely a visual application with points.

World
what exists
Rules
what is lawful
Player State
what belongs to the participant
Controller
how intent enters
Authority
who validates play
Projection
what is perceived
Session
what begins and ends
Persistent Memory
what survives levels or matches

Unreal’s gameplay framework makes these distinctions explicit, including persistent GameInstance, server-side GameMode, shared GameState, PlayerState, controllers, pawns, cameras, and actors.

RUORA game doctrine

Player input
≠ player action
Player action
≠ authoritative world mutation
Local prediction
≠ canonical outcome
Animation
≠ gameplay truth

This matters for:

* iMessage games,
* multiplayer systems,
* mobile games,
* console experiences,
* social challenges,
* UREEL worlds.

⸻

Doctrine 15: Value Must Exist on First Use and Over Time

Google’s app-quality guidance makes a useful distinction: a high-quality app must be useful or fun on first use and continue delivering value over time; adding more features can reduce value when it creates clutter or instability.

Every RUORA product must define:

Immediate Value
What changes during the first meaningful interaction?
Returning Value
Why does the second session matter?
Compounding Value
What becomes more useful because history exists?
Exit Value
What does the participant retain after leaving?

Law

Retention must emerge from compounding value, not engineered dependency.

⸻

Doctrine 16: Every Runtime Needs a Truthful Exit

Most products engineer entry and ignore departure.

Exit is part of the phenomenon.

Exit classes:

temporary pause
completed session
abandoned action
authority refusal
subscription cancellation
game loss
account deletion
realm transition
product retirement

Every exit must answer:

* What was saved?
* What was not?
* What remains pending?
* What can be resumed?
* What was deleted?
* What evidence survives?
* What authority was released?
* What should the participant expect next?

Exit Signature

Release
→ preserve context
→ communicate consequence
→ expose recovery
→ seal evidence

⸻

Doctrine 17: The Runtime Must Fail Truthfully

Failure must never be disguised as completion.

UNKNOWN
≠ EMPTY
OFFLINE
≠ REFUSED
TIMEOUT
≠ FAILED AUTHORITY
HOST ERROR
≠ PARTICIPANT ERROR
PARTIAL
≠ COMPLETE

Every domain should support truthful outcomes such as:

INCOMPLETE
PENDING
CONFLICTED
UNAVAILABLE
REFUSED
CANCELLED
PARTIALLY_PRESERVED

No streak, engagement metric, or visual narrative may manufacture success.

⸻

Doctrine 18: Runtime Evolution Requires Proven Adoption

New THISNIGGACRAZY concepts cannot jump from inspiration into the kernel.

Research
→ Concept Registry
→ Isolated prototype
→ measurable contract
→ accessibility variant
→ performance witness
→ hostile review
→ domain adoption
→ cross-domain proof
→ kernel candidacy

Kernel promotion test

A concept becomes universal only when:

implemented by two unrelated domains
+
same mechanics
+
different meanings
+
zero domain leakage
+
stable host boundaries
+
stable authority boundaries

Before that, it remains:

DOMAIN CAPABILITY
or
EXPERIMENTAL PROJECTION PRIMITIVE

⸻

The universal RUORA runtime anatomy

RUORA Runtime
├── Genesis
│   ├── boot
│   ├── identity binding
│   ├── manifest validation
│   └── initial authority state
│
├── Lifecycle
│   ├── enter
│   ├── suspend
│   ├── resume
│   ├── recover
│   └── exit
│
├── Environment
│   ├── device
│   ├── viewport
│   ├── modality
│   ├── accessibility
│   ├── connectivity
│   └── host capability
│
├── Projection
│   ├── registration
│   ├── derived view
│   ├── geometry
│   └── atmosphere
│
├── Interaction
│   ├── input
│   ├── intent
│   ├── friction
│   └── local optimistic state
│
├── Authority
│   ├── permission
│   ├── revision
│   ├── validation
│   └── canonical receipt
│
├── Reconciliation
│   ├── correlation
│   ├── conflict
│   ├── rollback
│   └── projection refresh
│
├── Evidence
│   ├── trace
│   ├── metric
│   ├── receipt
│   └── provenance
│
├── Memory
│   ├── view
│   ├── session
│   ├── canonical
│   ├── semantic
│   └── institutional
│
└── Exit
    ├── preservation
    ├── release
    ├── retirement
    └── inheritance

⸻

Product specialization matrix

Product type	Runtime specialization
Website	orientation, navigation, content projection, conversion, truthful exit
SaaS	tenancy, permissions, billing state, collaboration, auditability
Mobile app	interruption, background/resume, offline state, device capabilities
Mobile game	session lifecycle, player state, prediction, progression, rewards
Console/PC game	world persistence, controllers, camera, rules, replication
Bubble application	Bubble host adapter, Bubble authority adapter, workflow receipts
AI agent	command authority, tool scope, approval, execution evidence, memory
Social platform	identity context, relationship authority, moderation, shared state
Spatial/XR	comfort, field of view, spatial anchoring, body-safe motion
Operating system	process lifecycle, capability security, resource arbitration, continuity

⸻

Twelve canonical doctrine documents

Do not create one 1,500-page monolith. Create a constitutional set:

RUNTIME-DOCTRINE-00
RUORA Runtime Constitution
RUNTIME-DOCTRINE-01
Phenomenon and State Transition
RUNTIME-DOCTRINE-02
Lifecycle and Interruption
RUNTIME-DOCTRINE-03
Intent, Authority, and Receipts
RUNTIME-DOCTRINE-04
Projection, Atmosphere, and Geometry
RUNTIME-DOCTRINE-05
Evidence, Observability, and Memory
RUNTIME-DOCTRINE-06
Host and Authority Adapters
RUNTIME-DOCTRINE-07
Accessibility and Environment
RUNTIME-DOCTRINE-08
Privacy, Identity, and Tenant Context
RUNTIME-DOCTRINE-09
Failure, Recovery, and Exit
RUNTIME-DOCTRINE-10
Domain Packages and Substrate Independence
RUNTIME-DOCTRINE-11
Concept Promotion and Kernel Evolution

Each document should include:

Present Truth
Foundational Law
Definitions
Owned Responsibilities
Forbidden Responsibilities
State Model
Authority Model
Failure Model
Evidence Requirements
Accessibility Law
Host Variants
Product Specializations
Falsification Tests
Promotion Criteria
Nonclaims

⸻

Deepest synthesis

Traditional product engineering asks:
What screens and features do we need?
RUORA runtime engineering asks:
What phenomenon is being entered?
What state may change?
Who may authorize the change?
How is that change perceived?
What survives interruption?
What evidence proves it?
What memory inherits it?
How does the participant exit truthfully?

That doctrine can govern every RUORA product without forcing every product to become the same application.

One constitutional runtime doctrine
+
many domain ontologies
+
many projection frequencies
+
many host technologies
+
many authority systems
=
one coherent OURSELF technology civilization
