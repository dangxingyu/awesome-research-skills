---
name: paper-writing
description: Plan, draft, revise, or audit machine-learning and mathematical research papers. Use for paper stories and outlines, titles, abstracts, introductions, related work, theorem and proof exposition, experiment narratives, figure captions, LaTeX prose, or submission checks; do not use for ordinary nontechnical or creative prose.
---

# Paper Writing

Make the paper easy to skim, hard to misread, and possible to verify. An expert should recover the central argument from the title, abstract, introduction, main results, and figure captions. A careful reader should find the assumptions, evidence, and reproducibility details needed to check it.

## Load only the relevant guidance

- For story design, outlines, titles, abstracts, introductions, related work, methods, experiments, discussions, or conclusions, read [references/story-and-sections.md](references/story-and-sections.md).
- To study the argument patterns of ResNet, Central Flows, River Valley, or Fantastic Pretraining Optimizers, read [references/exemplar-patterns.md](references/exemplar-patterns.md).
- For mathematical setup, theorem statements, proof sketches, lemmas, appendix proofs, or a core-theorem rewrite, read [references/math-and-proof-writing.md](references/math-and-proof-writing.md).
- For sentence-level revision, terminology, citations, equations, figures, captions, source organization, or LaTeX conventions, read [references/style-and-latex.md](references/style-and-latex.md).
- For deadline planning, a full-paper audit, conference submission, anonymization, reproducibility, or an arXiv release, read [references/checklists.md](references/checklists.md).

## Establish the evidence contract

Inspect the available manuscript, notes, results, figures, proofs, code, and reviews before writing. Preserve the authors' actual contribution, notation, conventions, and level of certainty.

Record the paper's primary question, central claim, scope, strongest supporting evidence, main alternative explanation, and most important missing evidence. Distinguish what is measured, observed, derived, proved, hypothesized, planned, or unknown.

Never invent results, citations, assumptions, baselines, numbers, proof steps, or causal explanations. Do not strengthen a claim for rhetorical effect. Use a visible placeholder when drafting can continue, and ask the user only when a missing choice would materially change the paper.

## Gate long drafts with an outline

Before creating or substantially rewriting anything longer than one subsection, return a hierarchical outline instead of full prose. Include:

- a compact story spine;
- one complete-sentence bullet for every planned paragraph and its communicative job;
- the theorem, experiment, figure, example, or citation role attached to each paragraph;
- transitions between major parts;
- unresolved author choices and missing evidence.

Stop and wait for explicit approval. Treat the approved outline as the drafting contract. If drafting reveals a material structural change, show the proposed change before continuing. This gate does not apply to one subsection or a shorter passage, narrow copyedits, diagnostics, prose covered by an approved outline, or a request that explicitly waives the gate.

## Build and draft top down

1. Form a story spine that connects the problem, tension, conceptual move, mechanism, main result, evidence, scope, and significance.
2. Build a claim-evidence ledger. For each important claim, record its scope, supporting theorem or experiment, falsifier or control, main caveat, and draft location.
3. Turn the spine and ledger into the paragraph-level outline.
4. Draft for layered reading. Put each paragraph's point first, keep terminology stable, and make theorem statements and captions carry real information.
5. Audit the draft item by item against the approved outline and claim-evidence ledger. Check definitions before use, assumption visibility, numerical consistency, proof pointers, experiment fairness, and scope language.

If the desired story conflicts with the evidence, revise the story. Null or contradictory results that affect the central claim remain part of the paper.

## Connect every claim to support

- A theorem needs visible assumptions, a crisp conclusion, an interpretation, and a proof pointer.
- An experiment needs a stated question, a discriminating comparison, the observed result, uncertainty where relevant, and a bounded conclusion.
- A figure needs a takeaway. Its caption should explain the setup, encodings, and conclusion without requiring a search through the body.
- A related-work comparison should identify the exact object, assumption, or evaluation condition being compared.
- A limitation should identify where the method, evidence, or interpretation may fail and why that boundary matters.

## Replace corrected material cleanly

When a correction supersedes a claim, theorem, proof, definition, or interpretation, make the corrected version the sole canonical account. Remove stale statements, notation, caveats, captions, comments, and cross-references that depend on the discarded version. Mention revision history only when the user asks for an erratum, change log, reviewer response, or historical comparison.

## Revise in descending order of leverage

1. Scientific validity and claim accuracy.
2. Central argument and section order.
3. Evidence, controls, uncertainty, and reproducibility.
4. Paragraph logic, theorem exposition, figures, and captions.
5. Sentence precision, notation, citations, and LaTeX.
6. Formatting and submission checks.

Do not polish text that is likely to be deleted after a structural correction.

## Return a usable result

- For planning, return the story spine, claim-evidence outline, planned figures or theorems, and open decisions.
- For an approved draft or a short passage, return publication-ready prose followed only by consequential evidence gaps.
- For revision, provide the revised text or patch first, then summarize substantive changes and claims needing author verification.
- For review, prioritize a small number of high-leverage issues and distinguish scientific validity, evidence, exposition, reproducibility, and copyediting.
- Preserve the author's technical voice while removing avoidable complexity.
