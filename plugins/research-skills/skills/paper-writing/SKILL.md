---
name: paper-writing
description: Plan, draft, revise, or audit machine-learning and mathematical research papers. Use for paper stories and outlines, titles, abstracts, introductions, methods, experiments, theorem and proof exposition, figure captions, LaTeX prose, and submission checks; do not use for ordinary nontechnical or creative prose.
---

# Paper Writing

Produce a paper that is easy to skim, hard to misread, and possible to verify. An expert should recover the main story from the title, abstract, introduction, main results, and figure captions. A careful reader should find the definitions, assumptions, evidence, and reproducibility details needed to check it.

## Load only the relevant guidance

- For story design, hierarchical outlines, titles, abstracts, introductions, methods, experiments, related work, discussions, conclusions, or paragraph development, read [references/story-and-sections.md](references/story-and-sections.md).
- For theorem statements, mathematical setup, proof sketches, lemmas, appendix proofs, definition order, notation, or cross-reference deferrals, read [references/math-and-proof-writing.md](references/math-and-proof-writing.md).
- For a raw argument that should become one compact theorem with a detailed proof, read both [references/math-and-proof-writing.md](references/math-and-proof-writing.md) and [references/core-theorem-rewrite.md](references/core-theorem-rewrite.md).
- For technical drafting, substantive polishing, paragraph acceptance, first-use terminology checks, stale-definition checks, or corrections that supersede paper content, read [references/review-workflow.md](references/review-workflow.md).
- For sentence-level editing, terminology, equations, figures, captions, citations, source organization, or LaTeX conventions, read [references/style-and-latex.md](references/style-and-latex.md).
- For deadline planning, a full-paper audit, submission, anonymization, reproducibility, or an arXiv release, read [references/checklists.md](references/checklists.md).
- To apply the argument patterns of ResNet, Central Flows, River Valley, or Fantastic Pretraining Optimizers, read [references/exemplar-patterns.md](references/exemplar-patterns.md).

## Work from evidence

Inspect the available draft, notes, results, figures, proofs, code, and reviews before writing. Preserve the authors' actual contribution, notation, conventions, and level of certainty.

- Distinguish measured results, observations, derivations, theorems, interpretations, hypotheses, plans, and unknowns.
- Never invent results, citations, assumptions, baselines, numerical values, proof steps, implementation details, or causal explanations.
- Use a visible placeholder or list a gap when evidence is missing. Ask the user only when a missing choice would materially change the paper.
- Do not strengthen a claim for rhetorical effect. Null or contradictory results that affect the central claim remain part of the paper.
- For a method grounded in code, verify how core materials are produced, how information moves between participants, and which capabilities the reported experiments actually use.
- A request to review or explain authorizes findings, not edits. An edit request authorizes only the relevant paper artifacts.

## Use stable, literal terminology

Use established technical terms or describe the action directly. Avoid invented jargon and unfamiliar compound labels for ordinary operations. Introduce a new name only when it identifies a genuine recurring concept and the author has adopted it. Apply the same standard to outline headings, paragraph summaries, prose, notation, and figure labels.

## Plan long drafts before writing prose

For a new draft or substantial rewrite longer than one subsection, first return an English hierarchical outline and wait for explicit approval. The user may waive this gate.

The outline must:

- use one nested numbered list for manuscript content;
- number sections, subsections, paragraphs, and paragraph-development points at the levels relevant to the requested scope;
- restart paragraph numbering within each subsection and development-point numbering within each paragraph;
- give every paragraph one complete-sentence claim or job;
- enumerate beneath it the definitions, reasoning, evidence, qualifications, and transitions it will develop, in reading order;
- show where the main theorem, experiment, figure, example, and limitation enter;
- keep unresolved choices, evidence inventories, and presentation notes outside the manuscript hierarchy.

When revising an outline, return the complete updated hierarchy and preserve stable labels wherever the structure is unchanged, unless the user explicitly requests an excerpt or diff. Treat the approved hierarchy, including every development point, as the drafting contract. Ask before making a material structural departure.

The approval gate does not apply to one subsection or a shorter passage, narrow copyedits, diagnostics, or prose already covered by an approved outline.

## Draft top down

1. Form a compact story spine that connects the problem, tension, central method or theory, mechanism, discriminating predictions, decisive evidence, scope, and significance.
2. Build a claim-evidence ledger. For every important claim, record its scope, supporting theorem or experiment, falsifier or control, main caveat, and draft location.
3. Convert the spine and ledger into the required paragraph-level outline.
4. Draft each paragraph to fulfill its approved job and development points. Establish technical objects before interpreting them, except in a genuine introduction or section overview.
5. Audit the resulting prose against the outline, reader comprehension, terminology order, mathematical or factual correctness, and downstream definition use.

If the desired story conflicts with the evidence, revise the story.

## Make technical prose locally complete

Naming a concept, announcing a theorem, or promising a later explanation does not fulfill a requirement to define, explain, preview, compare, or justify it. Map every paragraph obligation to sentences that actually perform the work.

Technical sections must establish their central objects, operations, assumptions, success events, and measured quantities precisely enough for local reading. Earlier informal familiarity does not replace technical setup.

Outside an introduction or genuine section overview, define an object before commenting on its role, implications, advantages, or restrictions. When a necessary mention precedes its definition, mark it immediately with `(defined later in~\Cref{...})`, point to the location that actually defines it, and provide enough local meaning for the current reasoning. A cross-reference does not itself define a term.

## Audit substantive technical prose

For technical drafting and substantive polishing, follow [references/review-workflow.md](references/review-workflow.md). When independent agents are available, keep outline compliance, prefix-only reader comprehension, and first-use terminology review as distinct checks. Use a downstream stale-definition review when definitions are introduced or reorganized. Reconcile all findings against the same final candidate before accepting the prose.

If independent review is unavailable, perform the same evidence-based checks directly and disclose that independent approval remains unavailable. Never treat a readability pass as evidence of outline compliance or factual correctness.

## Replace corrected material cleanly

When a correction supersedes a claim, theorem, proof, definition, or interpretation, make the corrected version the sole canonical account. Remove stale statements, notation, proof arguments, caveats, examples, captions, comments, and cross-references that depend on the discarded version. Mention revision history only when the user asks for an erratum, change log, reviewer response, or historical comparison.

Search the affected sources for remnants and verify every remaining term, symbol, and reference against the corrected account. Use the superseded-content audit in [references/review-workflow.md](references/review-workflow.md).

## Revise in descending order of leverage

1. Scientific validity and claim accuracy.
2. Story spine and section order.
3. Claim-evidence alignment, controls, uncertainty, and reproducibility.
4. Paragraph logic, definitions, theorem exposition, figures, and captions.
5. Sentence precision, notation, citations, and LaTeX.
6. Formatting and submission checks.

Do not polish text that is likely to be deleted after a structural correction.

## Return a usable result

- For planning, return the story spine, complete hierarchical outline, planned figures or theorems, and separate open decisions.
- For an approved draft or short passage, return publication-ready prose followed only by consequential evidence gaps.
- For revision, provide the revised text or patch first, then summarize substantive changes and claims needing author verification.
- For review, prioritize high-leverage issues and distinguish validity, evidence, exposition, reproducibility, and copyediting.
- Preserve the author's technical voice while removing avoidable complexity.
