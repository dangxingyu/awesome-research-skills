# Deep Learning Paper Writing Playbook

## Contents

1. Core principles
2. Choose the paper archetype
3. Create the claim-evidence ledger
4. Design the story
5. Draft each section
6. Match evidence to claims
7. Write theory clearly
8. Write benchmark and systems papers clearly
9. Improve figures, tables, and prose
10. Handle citations, limitations, and uncertainty
11. Revise efficiently

## 1. Core principles

### Make the contribution compressible

A reader should be able to state the paper's problem, insight, method, and strongest evidence in four sentences. If the paper requires a list of loosely related contributions, identify which one changes the reader's understanding and make the others supporting results.

### Lead from a concrete tension

Strong deep learning papers often begin with a specific failure or mismatch rather than a broad claim that the field is important. Useful openings include:

- a method that should improve with depth but becomes harder to optimize;
- a common explanation that conflicts with measured behavior;
- an effective technique whose crucial design variable is unknown;
- an evaluation practice that prevents fair comparison;
- a capability that appears without an explicit training objective.

Name the tension precisely, show one representative piece of evidence early, and state what resolving it enables.

### Prefer a minimal causal story

Explain why the proposal should work. Distinguish the essential mechanism from engineering that makes it competitive. A small number of well-motivated design choices is easier to test, remember, and trust than a bundle of tricks.

### Pair every claim with a test

The paper's experimental or theoretical structure should mirror its claims. If a sentence in the abstract cannot be traced to a theorem, figure, table, qualitative analysis, or clearly labeled hypothesis, weaken or remove it.

### Make incompleteness visible

State the domain, data, architectures, scales, assumptions, and metrics covered. Explicitly identify important settings not covered. This increases trust and prevents a scoped result from reading as universal.

## 2. Choose the paper archetype

### Empirical method

Use when the primary contribution is an algorithm, architecture, objective, or training procedure validated experimentally.

Recommended flow:

1. Phenomenon or bottleneck.
2. Mechanistic intuition.
3. Minimal method.
4. Main controlled comparison.
5. Ablations that isolate each design claim.
6. Transfer, scale, robustness, or efficiency evidence.
7. Failure cases and limitations.

### Theory

Use when the main contribution is a formal explanation or guarantee.

Recommended flow:

1. Real phenomenon and why existing analysis misses it.
2. Formal setting and assumptions.
3. Informal statement of the main result.
4. Exact theorem and proof roadmap.
5. Consequences, examples, or counterexamples.
6. Experiments that test whether the modeled mechanism appears in realistic settings.
7. Assumption and extrapolation limits.

### Benchmark or evaluation

Use when the main contribution is a taxonomy, dataset, protocol, metric suite, or comparative study.

Recommended flow:

1. Decision the evaluation should support.
2. Taxonomy of the full design space.
3. Transparent selection criteria.
4. Standardized protocol and contamination controls.
5. Coverage matrix, including missing regions.
6. Findings, trade-offs, and sensitivity analyses.
7. Released artifacts, versioning, and maintenance plan.

### Systems or efficiency

Use when the main contribution changes cost, throughput, memory, latency, or operational feasibility.

Recommended flow:

1. Bottleneck and end-to-end cost model.
2. Method and source of expected savings.
3. Quality-matched resource comparison.
4. Wall-clock, compute, memory, and hardware accounting.
5. Scaling behavior and Pareto frontier.
6. Amortization assumptions and deployment constraints.

## 3. Create the claim-evidence ledger

Use a table like this before drafting:

| ID | Exact claim | Scope | Evidence | Falsifier/control | Caveat | Draft location |
|---|---|---|---|---|---|---|
| C1 | Method A reduces steps to target loss | Model family M, data D, budget B | Learning curves over seeds | Tuned baseline at equal tokens and hardware | No claim beyond tested scale | Abstract, Fig. 2 |

Classify claims:

- **Descriptive:** what was measured.
- **Comparative:** better, faster, smaller, or more robust than a specified baseline.
- **Causal/mechanistic:** a component or mechanism produces an effect.
- **Theoretical:** follows under stated assumptions.
- **Generalization:** transfers across data, models, tasks, or scales.
- **Normative:** recommends what researchers or practitioners should do.

The required evidence rises in that order. A correlation does not establish a mechanism. A theorem in a simplified model does not prove behavior in a modern network. A result on several benchmarks does not justify a universal statement.

## 4. Design the story

### One-sentence central claim

Use this pattern:

> For [scope], [method or principle] addresses [precise problem] because [mechanism], as supported by [strongest evidence].

If the sentence contains several independent "and" clauses, split the project or demote secondary claims.

### Contribution list

Write contributions as claims with evidence, not as a table of contents.

Weak:

> We propose a method, run experiments, and provide analysis.

Stronger:

> We identify X as the failure mode; derive Y as a minimal correction; and show through Z that the correction holds under the stated conditions.

### Reviewer-objection map

Before drafting, list the most damaging plausible objections:

- Is the gain from extra compute, data, parameters, or tuning?
- Is the baseline current and comparably optimized?
- Does the evaluation leak target information?
- Does the theorem assume away the phenomenon it claims to explain?
- Is the metric a credible proxy for the stated goal?
- Does a result transfer beyond one seed, model, dataset, or scale?
- Are costs shifted elsewhere rather than removed?

Place the answer where the objection naturally arises; do not defer all defenses to an appendix.

## 5. Draft each section

### Title

Name the object and contribution. Prefer concrete nouns and verbs over claims such as "novel," "unified," or "towards" unless they add real scope information. A subtitle can expose the mechanism or evaluation setting.

### Abstract

Use six moves, usually in 150–250 words unless the venue says otherwise:

1. **Context:** one sentence establishing the important problem.
2. **Gap:** one sentence naming the precise failure or unknown.
3. **Insight:** the explanatory idea.
4. **Method/result:** what the paper introduces or proves.
5. **Evidence:** the strongest quantitative or formal result with scope.
6. **Boundary/implication:** what follows, without expanding beyond the evidence.

Do not include results absent from the paper, vague superlatives, or a numerical gain without the task, baseline, and comparison condition.

### Introduction

Aim for this paragraph logic:

1. What important capability or decision is at stake?
2. What concrete observation shows the current approach is inadequate?
3. Why is the obvious explanation or fix insufficient?
4. What is the paper's principle or hypothesis?
5. How is it operationalized?
6. What evidence supports it?
7. What are the scoped contributions and limits?

An early figure can carry the motivating phenomenon, method schematic, or main result. The introduction should let a reader predict the rest of the paper.

### Related work

Organize by the decisions that distinguish approaches, not by a chronological list. For each cluster:

1. State the shared objective.
2. Name the relevant design axis or assumption.
3. Position the present work factually.
4. Avoid dismissive novelty claims.

Use a comparison table when several methods vary across three or more repeated attributes. Verify every comparison and cite primary sources.

### Method

Start with the interface: inputs, outputs, training signal, and intended use. Define notation before use, then give the high-level algorithm before details. Separate essential components from optional implementation choices.

For each component, state:

- what problem it solves;
- why the chosen form is appropriate;
- its computational cost;
- the ablation or theorem that tests it.

Include pseudocode when prose and equations do not make execution order unambiguous.

### Experiments

Open with questions, not datasets. A useful sequence is:

1. Does the main claim hold under the primary protocol?
2. Which component causes the effect?
3. Is the comparison fair under matched resources?
4. How stable is the result across seeds, hyperparameters, and evaluation choices?
5. Where does it transfer or scale?
6. Where does it fail?

For every result, specify enough context to interpret it: dataset/split, model, training budget, selection rule, metric direction, uncertainty, and baseline tuning. Separate confirmatory tests from exploratory analysis.

### Discussion and limitations

Distinguish:

- what was established;
- the proposed explanation;
- plausible alternatives not ruled out;
- tested boundary conditions;
- untested settings;
- practical and societal consequences.

Prefer specific limits ("tested only on decoder-only models up to X scale") to generic disclaimers ("more work is needed").

## 6. Match evidence to claims

### Baselines

Use strong, relevant, comparably tuned baselines. Match or report:

- data and preprocessing;
- parameter count or effective capacity;
- training tokens/steps and optimizer budget;
- search/tuning budget;
- augmentation and regularization;
- hardware and precision for efficiency claims;
- decoding/evaluation protocol.

If perfect matching is impossible, state the asymmetry and avoid a causal interpretation.

### Ablations

An ablation should answer a design question. Prefer a small set of hypothesis-driven interventions over many toggles. Include interactions when the story depends on a combination of components.

### Uncertainty and statistics

Report seeds or repeated measurements when randomness affects the conclusion. Show distributions or confidence intervals when point estimates hide variance. Reserve "statistically significant" for an actual prespecified statistical test; otherwise say "larger," "consistent," or "within noise" as supported.

### Efficiency

Report both quality and resources. Distinguish:

- optimization steps;
- examples or tokens processed;
- FLOPs or accelerator-hours;
- wall-clock time;
- peak memory;
- inference cost;
- one-time preprocessing or proxy-training cost.

State what is amortized and over how many uses.

### Leakage and contamination

Document data provenance, de-duplication, target access, benchmark reuse, prompt tuning, validation decisions, and model pretraining overlap when known. Treat possible contamination as uncertainty, not as proof of invalidity or safety.

## 7. Write theory clearly

### State the bridge to practice

Name the real phenomenon first. Then explain which part the formal model captures and which parts it removes. A useful sequence is:

1. empirical phenomenon;
2. obstacle to existing analysis;
3. simplified model;
4. new concept or quantity;
5. informal theorem;
6. formal theorem;
7. practical prediction;
8. experiment or example testing that prediction.

### Handle assumptions honestly

For every major theorem, explain:

- what each assumption buys technically;
- whether it is observable or testable;
- whether realistic systems satisfy it exactly, approximately, or not at all;
- what breaks without it.

Do not translate convergence to a stationary/KKT point into global optimality. Do not translate an asymptotic result into a finite-compute guarantee without a rate that supports it.

### Structure proofs for readers

Give a proof roadmap with the main invariant, decomposition, or reduction. Keep routine algebra and auxiliary lemmas in appendices, but leave the conceptual step in the main text. Use examples and counterexamples to clarify theorem scope.

## 8. Write benchmark and systems papers clearly

### Treat evaluation as a designed measurement system

State the object of evaluation, the decisions the benchmark should support, stakeholders, scenarios, metrics, adaptation rules, and aggregation choices. Provide a taxonomy before selecting a subset, then expose the subset and omissions in a coverage matrix.

Avoid a single leaderboard score when important trade-offs exist. Report per-scenario and per-metric results, sensitivity to prompts/decoding/adaptation, and Pareto frontiers where relevant.

### Treat system boundaries explicitly

For efficiency or systems work, diagram the whole pipeline. State whether data collection, filtering, proxy training, compilation, indexing, evaluation, and retries are inside or outside the cost comparison. Report failures and tail behavior, not only average throughput.

## 9. Improve figures, tables, and prose

### Figures and tables

Each main figure should answer one question. Captions should state the setup, metric direction, uncertainty, and takeaway without requiring a hunt through the text. Use consistent colors and ordering across figures. Do not encode the only distinction by color.

Recommended main-paper visuals:

- motivating failure or phenomenon;
- method schematic;
- main quality comparison;
- ablation or mechanism test;
- scaling, robustness, or efficiency frontier;
- failure case or coverage matrix.

### Paragraphs

Use a claim -> evidence -> interpretation -> transition structure. Put the topic sentence first. Keep one job per paragraph. Define a term once and use it consistently.

### Sentences

Prefer concrete subjects and verbs. Replace "It can be seen that" with the observation. Replace "significantly" with a number or remove it. Use "suggests" for evidence compatible with an explanation and "shows" only when the evidence rules out relevant alternatives.

Avoid throat-clearing, repeated contribution claims, undefined acronyms, stacked parentheticals, and adjectives that substitute for evidence.

## 10. Handle citations, limitations, and uncertainty

### Citations

Cite the primary source for a method, theorem, dataset, or empirical fact. Verify title, authors, year, venue, and the exact proposition supported. A citation does not transfer all claims from the cited paper; phrase the local claim narrowly.

Use current literature search when novelty, state of the art, or venue positioning matters. Never invent a BibTeX entry or cite from memory when verification is possible.

### Limitations and broader impacts

Discuss limitations that affect interpretation, adoption, or harm. Relevant categories include compute concentration, data licensing and privacy, demographic or geographic coverage, misuse, environmental cost, accessibility, brittle metrics, and dependency on closed models or APIs.

Do not use a limitations section to introduce untested defenses or to neutralize an overclaim. Fix the overclaim in the main text.

## 11. Revise efficiently

Use passes in this order:

1. **Claim pass:** remove or scope unsupported claims.
2. **Structure pass:** make every section support the central claim.
3. **Evidence pass:** add controls, uncertainty, and missing experimental details.
4. **Reader pass:** define terms, add signposts, and fix figure/caption independence.
5. **Compression pass:** delete repetition and move nonessential detail to appendices.
6. **Consistency pass:** notation, terminology, numbers, citations, and cross-references.

When time is short, prioritize scientific validity, abstract/figure fidelity, and baseline fairness over stylistic polish.
