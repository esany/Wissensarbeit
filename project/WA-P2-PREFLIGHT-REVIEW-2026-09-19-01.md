# WA-P2-PREFLIGHT-REVIEW-2026-09-19-01

Status: **independent qualitative review evidence / NEEDS CORRECTION / no implementation authority**

Review target: PR #35 — `P2: fidelity manifest preflight and bounded admission proposal`

Reviewed baseline:
- canonical `main@63883532af7834b5e46a84cef665ef4cfaa25a98`
- reviewed PR head: `a81809bf16d5442ad487938ddd47179e26de8ef5`
- `implementation_allowed=false`
- no P2 implementation present in the reviewed diff

## Review result

**NEEDS CORRECTION**

The Existing-Owner fit, rejection of a new state/truth layer, most F1–F11 negative invariants, and the general admission boundary survived review.

One material gap did not:

> The preflight could still be satisfied by a semantically conservative near-full/full context dump. That would preserve uncertainty, authority, readiness, NONE states and provenance while failing the positive `BB-CONTEXT` capability of producing a genuinely bounded, task-relevant execution context.

A second coupled gap is selection provenance:

> Deterministic fidelity checks may validate a compile against an explicit structured selection/materiality inventory, but they must not silently decide real-world materiality themselves. The implementation contract must bind the judgement-based selection basis and validate fidelity relative to it.

## Required minimal correction

No new architecture, Requirement, Building Block, state owner or failure-family is required.

The corrected preflight/admission must require:

1. at least one structured positive fixture with explicit required/material refs and explicit non-required/irrelevant refs;
2. compiled execution context retains all required/material refs and excludes the explicit irrelevant refs, so a full dump deterministically fails;
3. selection/materiality basis is bound as judgement provenance/input; deterministic validation checks fidelity to that basis rather than claiming the materiality decision itself is proven;
4. compile provenance/fidelity output does not neutralize boundedness by being forced into the same execution payload; result review must assess combined context + provenance overhead;
5. the admission boundary excludes hidden deterministic relevance/materiality classifiers, unproven caller include-lists without selection provenance, and safe near-full-dump implementations.

## Authority boundary

This review:
- does not admit implementation;
- does not authorize merge of PR #35;
- does not accept any later implementation result;
- does not authorize merge of a later implementation PR;
- does not create later programme priority.

Required sequence after correction remains: normal assurance, focused independent re-review, and only on CONFIRM may PR #35 be considered for canonical promotion. Separate implementation admission would still be required afterward.
