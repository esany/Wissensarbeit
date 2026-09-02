# Pilot closure: generic learnings

## Boundary and provenance

- Source case: `esany/pflege-arnshaugk-historie`
- Case return: persisted in the source repository as external pilot review input
- Authority: evidence and candidates only; no requirement, method, architecture,
  or implementation is accepted by this closure

Project-specific observations, entities, sources, research questions, and product
ideas are deliberately absent here. They belong to the case repository. This file
records only generic lessons that fit the existing Wissensarbeit mechanisms.

## Dispositioned learnings

| Learning | Existing mechanisms sharpened | Disposition |
|---|---|---|
| Material state must not exist only in conversation | `BB-STATE`, `BB-TRACE`, `BB-LEARN` | Require conversation harvesting to a canonical reference before closure. |
| Context compression can introduce semantic drift | `BB-CONTEXT`, `BB-ASSURE` | Verify material assertions and unresolved states against lossless references. |
| Useful compression is lossless-by-reference | `BB-CONTEXT`, `BB-DERIVE` | Optimize token volume only after reference coverage and fidelity hold. |
| Co-creation and elicitation precede requirement promotion | `BB-INTEGRATE`, `BB-REQUIREMENTS` | Keep proposals as candidates until the authorized lifecycle decision. |
| Pilot evidence changes the generic core only after Generic-Fit | `BB-INTEGRATE`, `BB-DESIGN` | Prefer sharpening an existing mechanism; case-only evidence stays case-specific. |
| Case isolation prevents overfitting | `BB-BOOTSTRAP`, `BB-STATE`, `BB-LEARN` | Return case semantics to the source repository; retain only generic evidence here. |

No new building block is introduced. The six scenarios in
`regression-scenarios.json` are executable inputs with explicit expected outcomes,
not prose labels that merely describe desired behavior.

## Pilot definition of done

The pilot is complete when all of the following are true:

1. Project-specific findings are returned to the case repository as review input.
2. Every generic learning has an explicit disposition against existing mechanisms.
3. No open pilot question requires further domain work to close the generic pilot.
4. Wissensarbeit contains no case-domain model, accepted case requirement, or case
   architecture.
5. The six generic regressions execute in CI and compare computed outcomes with
   explicit expected values.
6. Token reduction is accepted only when context fidelity is unchanged.

Open questions may continue in the case repository. They do not hold this generic
pilot open and do not silently become framework requirements.
