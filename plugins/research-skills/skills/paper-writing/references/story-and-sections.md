# Story and section design

## Start with a reader contract

Before drafting, write down:

- **Problem:** What specific question or task does the paper address?
- **Stakes:** Why should this audience care now?
- **Tension:** What observation, limitation, contradiction, or decision makes the problem nontrivial?
- **Conceptual move:** What is the one idea the reader should remember?
- **Mechanism:** Why should that idea work?
- **Evidence:** Which theorem, experiment, or comparison most directly supports it?
- **Boundary:** Where does the claim stop?

If any answer requires “and” several times, the paper may contain multiple stories. Choose a primary one and make secondary contributions support it.

## Choose the primary paper archetype

Use one primary archetype to organize the argument:

- **Empirical method:** concrete failure, minimal design idea, controlled comparison, mechanism-testing ablations, transfer or scale, and failure modes.
- **Theory:** motivating phenomenon, formal setting, assumptions, interpretable theorem, proof map, consequences or examples, and scope limits.
- **Benchmark or evaluation:** decision need, design-space taxonomy, selection principles, measurement protocol, coverage and omissions, findings, and maintained artifacts.
- **Systems or efficiency:** operational bottleneck, end-to-end cost model, method, quality-matched resource comparison, scaling behavior, and deployment limits.
- **Hybrid:** choose one primary archetype and use the others only to support its central claim.

Do not add a theorem, benchmark grid, systems claim, or method merely to make the paper appear broader.

## Convert the story into a claim--evidence outline

Use a hierarchical outline before full prose. Each node should be a claim or communicative job, not merely a topic.

Weak outline item:

> 4.2 Learning-rate experiments

Stronger outline item:

> 4.2 Larger learning rates improve long-horizon progress by moving the trajectory into flatter regions

For every major claim, record:

- the evidence that supports it;
- the alternative explanation or confound that must be ruled out;
- the figure, table, theorem, or example that carries the evidence;
- the precise scope of the conclusion.

Missing evidence discovered during outlining is a research task, not a prose problem.

## Approval gate for long drafts

For a new draft or substantial rewrite whose scope exceeds one subsection, the outline is a user review artifact rather than an internal planning step.

Return the outline before prose. It should contain:

- the story spine and section hierarchy;
- one complete sentence bullet for each planned paragraph;
- the evidence, theorem, figure, example, or citation role attached to each paragraph;
- transitions that explain why one paragraph leads to the next;
- unresolved author decisions and missing evidence.

Stop after presenting the outline. Incorporate the user's changes and show a revised outline when they materially affect the structure. Begin prose only after the user explicitly approves the outline or says to proceed. Once approved, treat the outline as the drafting contract. Ask before making a material structural departure that emerges during drafting.

This gate applies to introductions, full multi-part sections, several sections, and whole papers. It does not apply to a single subsection or shorter passage, local copyediting, analysis without drafting, or work for which the user explicitly says to skip the outline stage.

## Outline paragraphs before writing them

After the section outline is stable, write one bullet for every planned paragraph. Each bullet should state the paragraph's single point as a complete, direct sentence. Read only the bullets and revise until they form a coherent argument.

Then expand each bullet into one paragraph:

- use the bullet, or a refined version of it, as the opening sentence;
- add only evidence, explanation, qualification, or transition that serves that point;
- split the paragraph when a second point could stand as its own bullet;
- delete the paragraph when its bullet does not advance the section's argument.

This intermediate outline keeps sentence polishing from hiding a structural problem.

## Titles

Prefer a short title with a distinctive phrase that identifies the object and contribution. Avoid titles so broad that they could describe an entire field. A subtitle can pair a memorable concept with a precise setting.

Check that the title does not overclaim beyond the strongest result.

## Abstract

Write one self-contained paragraph. A reliable sequence is:

1. setting and stakes;
2. specific tension or gap;
3. proposed concept, method, theory, or protocol;
4. mechanism or scope;
5. decisive theoretical or empirical evidence;
6. main quantitative result when it matters;
7. significance or limitation.

Do not turn the abstract into a table of contents. Include the results that change the reader's belief, not every result in the paper. Expand acronyms only when they recur or are central.

## Introduction

A strong introduction often makes these moves:

1. **Setting:** define the object and why it matters.
2. **Tension:** show the concrete failure, anomaly, practical constraint, or unreliable convention.
3. **Question:** state the question in a form the paper will answer.
4. **Idea:** name the conceptual move and contrast it with the standard picture.
5. **Mechanism:** explain the idea using a running example, decomposition, construction, or cartoon.
6. **Contributions and evidence:** state results as claims, with enough numbers or theorem content to be meaningful.
7. **Scope:** say what the paper does not yet explain or test when that boundary prevents misreading.

Place an opening figure early when the central idea is visual. It should function as a graphical abstract: the caption states the main takeaway, explains encodings, and connects panels into an argument.

Avoid beginning with a broad history of the field. Cite directly relevant work while creating the tension; defer a fuller conceptual comparison to related work.

## Method or model section

Open with the section's question and a roadmap if it is long. A useful order is:

1. motivating example or failure of the baseline;
2. intuitive description of the method or model;
3. formal definition;
4. important design choices and why they are necessary;
5. implementation or computational implications;
6. predictions, invariants, or comparisons the method creates.

Define the simplest core case first, then generalize. Separate the essential idea from engineering choices. If the method is a reformulation, show the original and new forms side by side and explain what becomes easier.

## Experiments

Every experiment should answer a question. Organize subsections by questions or claims, not by the order in which runs were performed.

For each experiment, state:

1. **Question or hypothesis.** What uncertainty does this experiment resolve?
2. **Discriminating design.** Why can this comparison answer the question? Name matched factors, controls, and possible confounds.
3. **Setup.** Give the information needed to interpret the result; move exhaustive reproducibility details to an appendix when appropriate.
4. **Result.** Lead with the observed pattern and the relevant magnitude or uncertainty.
5. **Interpretation.** State exactly what the result supports and what it does not establish.
6. **Failure or robustness.** Probe scale, dataset, seed, hyperparameter, ablation, or boundary when it is relevant to the claim.

Use tables when exact values or many categorical comparisons matter. Use plots when trend, variation, scaling, or trajectory is the message. Do not use a large result table as a substitute for a stated question.

For benchmarks, define fairness operationally: tuning budget, search space, compute accounting, data order, evaluation point, model scale, and uncertainty. A negative result is persuasive only when the protocol gives competing methods a credible chance.

## Related work

Organize related work by the conceptual axes needed to locate the contribution. For each closest line of work, say:

- what object or setting it studies;
- what result or mechanism it establishes;
- the exact dimension on which the present paper differs.

Be specific and neutral. Prefer “Theorem 2 assumes X, whereas our result handles Y” to “prior work is unrealistic.” Do not imply that absence from the bibliography means absence from the literature; verify citations before making novelty claims.

## Discussion and conclusion

Use discussion to answer “How should the reader now think differently?” Connect the result to a broader principle without outrunning the evidence. Explain meaningful limitations as boundaries on the model, method, or evaluation—not as ceremonial caveats.

The conclusion should answer the introduction's question, restate the changed mental model, and identify the most consequential boundary or future direction. Do not merely repeat the abstract sentence by sentence.

## Paragraph test

For each paragraph, ask:

- What single job does it perform?
- Does the first sentence state that job?
- Does each later sentence develop, support, qualify, or transition from it?
- Would the paper still make sense to an expert reading only paragraph openings?
- Is the transition to the next paragraph causal or logical rather than merely topical?

If a paragraph has two equally important points, split it. If its point appears only at the end, move the point forward and retain the ending as implication or transition.
