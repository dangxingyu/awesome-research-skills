---
name: write-deep-learning-papers
description: Plan, draft, revise, or review rigorous deep learning and machine learning research papers, including empirical method papers, theory papers, benchmark/evaluation papers, and systems papers. Use when asked to turn research notes, results, plots, proofs, code, or an existing manuscript into an abstract, outline, section, full draft, rebuttal-oriented revision, or submission-readiness review without inventing evidence or citations.
---

# Write Deep Learning Papers

Produce a clear scientific argument whose claims are no stronger than the available evidence. Optimize for reviewer comprehension, technical precision, and reproducibility rather than ornamental prose.

## Load the guidance

- Read [references/writing-playbook.md](references/writing-playbook.md) before drafting or substantially revising a paper.
- Read [references/review-checklist.md](references/review-checklist.md) before calling a draft submission-ready.
- Read [references/paper-corpus.md](references/paper-corpus.md) when choosing a paper archetype, studying successful rhetorical moves, or explaining the provenance of this skill's guidance.
- Use [assets/system-prompt.md](assets/system-prompt.md) when the user wants a standalone prompt for another model or agent.

## Establish the research contract

Infer what is available from the user's files and prompt before asking questions. Record, at least internally:

1. Target genre: empirical method, theory, benchmark/evaluation, systems, position/report, or hybrid.
2. Intended venue or audience, if known.
3. One-sentence problem, one-sentence central claim, and the strongest evidence supporting it.
4. Evidence status for every important statement: `measured`, `proved`, `derived`, `observed`, `hypothesized`, `planned`, or `unknown`.
5. Missing information that would materially change the argument.

Never fill an evidence gap with plausible-looking numbers, experiments, theorem conditions, citations, implementation details, or claims of novelty. Use `[NEEDS INPUT: ...]` when progress is still possible; ask a concise question only when the missing choice changes the paper's direction.

## Build the argument before the prose

Create a claim-evidence ledger. For each main claim, state:

- the exact claim and its scope;
- the evidence that tests it;
- the comparison, control, theorem, or ablation that could falsify it;
- the main caveat;
- where the evidence appears in the draft.

Then form the story spine:

1. Important problem or observed phenomenon.
2. Precise failure, gap, or unresolved question.
3. Explanatory principle or design insight.
4. Method, theorem, dataset, or evaluation that operationalizes the insight.
5. Evidence matched to each claim.
6. Boundary conditions, limitations, and remaining questions.

If the ledger and story disagree, revise the story. Do not hide contradictory or null results that affect the central claim.

## Draft by paper archetype

- **Empirical method:** problem -> minimal design idea -> algorithm -> controlled comparisons -> ablations -> transfer/scale/robustness -> limitations.
- **Theory:** phenomenon -> formal setting -> assumptions -> informal theorem -> formal results -> proof map -> experiments or examples testing relevance -> scope limits.
- **Benchmark/evaluation:** decision need -> taxonomy/design space -> selection principles -> measurement protocol -> coverage and omissions -> findings and trade-offs -> artifacts and maintenance.
- **Systems/efficiency:** operational bottleneck -> cost model -> method -> end-to-end resource accounting -> quality-cost frontier -> scaling and failure analysis.
- **Hybrid:** keep one primary archetype and use the others only to support it.

Use the playbook's section templates selectively. Preserve useful venue conventions and the user's established notation and voice.

## Run evidence-aligned review passes

Review in this order:

1. **Scientific validity:** assumptions, leakage, controls, uncertainty, comparability, confounders, and claim strength.
2. **Argument:** one central contribution, coherent section order, and explicit answers to likely reviewer objections.
3. **Reproducibility:** data provenance, splits, preprocessing, models, objectives, hyperparameters, seeds, compute, evaluation, and artifact availability.
4. **Presentation:** abstract fidelity, readable figures, defined notation, local paragraph logic, consistent terminology, and concise prose.

Report unresolved blockers separately from optional improvements. When rewriting supplied text, preserve meaning unless explicitly identifying a scientific correction.

## Deliver useful artifacts

For a full drafting task, normally provide:

1. research contract and assumptions;
2. claim-evidence ledger;
3. proposed outline;
4. requested draft or revision;
5. evidence gaps and risky claims;
6. checklist results and next experiments, if applicable.

For a narrow request, return only the requested section plus material caveats. Cite primary sources and verify bibliographic facts when citations are in scope.
