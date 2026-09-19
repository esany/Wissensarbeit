# WA-P2-PREFLIGHT-REREVIEW-2026-09-19-02

Status: **focused independent qualitative re-review evidence / NEEDS CORRECTION / no implementation authority**

Review target: PR #35 — `P2: fidelity manifest preflight and bounded admission proposal`

Reviewed state:
- canonical `main@63883532af7834b5e46a84cef665ef4cfaa25a98`
- reviewed PR head: `88464f1706d8c9934e9e2e7a553a6cadeee65a87`
- GitHub Actions assurance Run #101: SUCCESS
- `implementation_allowed=false`
- no P2 implementation present

## Re-review result

**NEEDS CORRECTION**

The prior correction successfully closed the selection/materiality-provenance gap:

- selection/materiality remains judgement-based;
- deterministic validation is relative to a bound selection basis;
- hidden relevance/materiality classifiers are excluded;
- caller include-lists without selection provenance are excluded;
- no new truth/state/architecture owner was introduced.

The remaining material gap is narrower:

> The corrected positive P1 contract deterministically rejects a literal full dump, but it does not yet support its stronger prose claim that a near-full dump deterministically fails.

A provenance-bound judgement could classify 99 of 100 candidate refs as required/material and one as irrelevant. The compiler could faithfully emit the 99 required refs and satisfy the current P1 predicate while still demonstrating almost no positive boundedness.

## Required minimal correction

No new architecture, classifier, state owner, global token ratio or general near-full detector is required.

The positive structured fixture must instead freeze a closed candidate universe and an exact expected output set:

- declare a closed candidate-ref universe `U`;
- partition it completely into required/material `R` and non-required/irrelevant `I`;
- require `R ∩ I = ∅` and `R ∪ I = U`;
- require execution refs to equal `R` exactly;
- freeze at least one concrete fixture in which `R` is visibly a bounded proper subset of `U` and `I` contains several refs, so the fixture demonstrates non-trivial reduction;
- treat any output containing refs outside `R`, or missing refs in `R`, as FAIL.

The contract must not generalize this fixture into a claim that arbitrary real-world "near-fullness" is deterministically decidable. Real-world boundedness, material sufficiency and usefulness remain judgement dimensions for result review.

## Authority boundary

This re-review:
- does not admit implementation;
- does not authorize merge of PR #35;
- does not accept any later implementation result;
- does not authorize merge of a later implementation PR;
- does not create later programme priority.

After the contract correction and normal assurance, the next gate remains focused independent qualitative re-review.
