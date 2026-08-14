# RC0001-CR004-ABBREVIATED-DIGEST-ERRATA-001

**CLASS** Append-only successor errata. **This record does not edit, reproduce, replace, or
reinterpret Cold Review 004.**
**AUTHORIZATION** `AUTHORIZE_RC0001_CR004_ABBREVIATED_DIGEST_ERRATA_001` — Founder, 2026-08-13.
**DISCOVERED BY** `RC0001_CR004_RECORD_ADMISSION_002`, during pre-staging digest verification.

---

## 1. Errata record

```
errata_id                       RC0001-CR004-ABBREVIATED-DIGEST-ERRATA-001
target_record_id                OURSELF-RCP-RC0001-SEMANTICPROGRAM-v0.4-
                                LINEAGE-INDEPENDENT-COLD-REVIEW-004.md
target_record_sha256            7ce5feac4bc20c7dd7987e368e397912db0627203e85a5705d5144fff96d1a50
admission_commit                7d3e2c6686771bd838eaae5826ed762c20025a52

affected_fields                 [ §0.1 evidence-digest table, row "Lineage adjudication"
                                , §0.1 evidence-digest table, row "Authoring commission (L2)" ]

content_mismatch                false
representation_defect           true
admission_validity_effect       none
cold_review_verdict_effect      none
successor_lineage_effect        none
correction_method               SUCCESSOR_ERRATA_ONLY
```

## 2. The two defects

Both are confined to the **abbreviated display column** of §0.1. Neither appears in the record's
closing full-digest witness, and neither corresponds to any difference in reviewed bytes.

### Defect 1 — `SLR-01-R1-CORRECTED-SOURCE-LINEAGE-RECONCILIATION.md`

```
displayed_value   a506352e…14e68c6                                          (§0.1, line 34)
correct_value     a506352ae82bd889034b5972dc2b090185aac3c6ac58f6bbc083f7d4614e68c6
```

The eighth character of the displayed prefix reads `e`; the artifact's eighth digest character is
`a`. The displayed suffix `14e68c6` is correct.

### Defect 2 — `DURABLE-DAILY-RITUAL-LEDGER-SEMANTICPROGRAM-AUTHORING-COMMISSION.md`

```
displayed_value   9a04124a…5cc04e                                           (§0.1, line 36)
correct_value     9a04124a25ec3dc9c281d73a4f6bce7ecb7a0619a0d9890f9a51fd5ce5dcc04e
```

The displayed prefix `9a04124a` is correct. The displayed suffix `5cc04e` matches neither the final
six characters (`dcc04e`) nor the final seven (`5dcc04e`) of the digest; it is consistent with
`5dcc04e` rendered with one character dropped. This errata records the observable discrepancy and
does not adjudicate its cause.

## 3. Authority precedence — stated, not inferred

`authoritative_witness_reference`: **Cold Review 004's closing full-digest witness block**, headed
*"All artifacts byte-unchanged at close, independently recomputed"*.

That block is the authoritative content-binding witness for this admission because:

1. it explicitly records the **complete** SHA-256 of every reviewed artifact;
2. it is the record's own **closing verification** step, executed for that purpose;
3. its values **reproduce the exact disk bytes and the exact committed bytes** — verified 11/11 at
   `7d3e2c6`;
4. the §0.1 table is **representational shorthand** for reader orientation, not the verification act.

**Digest length alone does not create authority.** A longer value is necessary for content binding
but is not what confers precedence; the closing block controls because the record's own structure
and execution history designate it as the verification witness, and its values reproduce the bytes.

```
AUTHORITATIVE WITNESS DESIGNATION  ≠  DIGEST LENGTH  ≠  DISPLAY POSITION
DISPLAY ASSERTION  ≠  CONTENT-BINDING ASSERTION  ≠  AUTHORITATIVE VERIFICATION WITNESS
```

The two defective abbreviations are therefore **not competing proofs**. They are defective
representations of a proof that is itself correct.

## 4. Verification state at the time of this errata

```
CR-004 §0.1 abbreviated display        DEFECTIVE   (2 of 11 rows)
CR-004 closing full-digest witness     CORRECT     (10 of 10 rows)
Disk bytes                             CORRECT     (11 of 11)
Committed bytes at 7d3e2c6             CORRECT     (11 of 11)
```

Yielding the four-way disposition:

```
content_binding            VERIFIED
representation_consistency DEFECTIVE
admission_disposition      ALLOW
corrective_obligation      ERRATA_REQUIRED
```

`DisplayDefect ⇏ ContentFailure` · `ContentVerified ⇏ RepresentationCorrect` ·
`RepresentationDefect ⇒ ErrataObligation` · `ErrataObligation ⇏ AdmissionInvalid`

## 5. Semantic effect

This errata establishes **only** that Cold Review 004 contains two abbreviated-display transcription
defects.

It does **not** establish: different reviewed bytes; different lineage; a different Cold Review 004
verdict; ratification of v0.4; validity of v0.5; authority for Cold Review 005; or repair of CR4-01.

**Cold Review 004 remains `CHANGES_REQUIRED` — 1 BLOCKING, 7 MATERIAL, 5 MINOR. CR4-01 remains
BLOCKING.**

## 6. Non-blocking rule

`ERRATA OWED ≠ SUCCESSOR BLOCKED.`

This obligation is discharged by the existence of this record. It does not gate Cold Review 005 or
any other successor act, because the defect is localized to a non-authoritative representation, does
not alter the reviewed subject, and does not touch the authoritative witness. v0.5 binds Cold Review
004 by its **correct full SHA-256** (`7ce5feac…f96d1a50`), not by either defective abbreviation.

A successor is blocked only if fresh evidence shows the authoritative full-digest witness was wrong,
the reviewed bytes differ, or a successor bound a defective abbreviated value.
