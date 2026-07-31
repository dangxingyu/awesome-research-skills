# Cyclic theory-agent prompt template

Specialize all bracketed fields. Keep the resulting launch prompt
self-contained and use absolute paths.

---

# CYCLIC THEORY RESEARCH: [PROBLEM NAME]

## Source of truth

Read, in order:

1. `[ABSOLUTE PATH]/problem.md`
2. `[ABSOLUTE PATH]/registry.md`
3. `[RELEVANT SOURCE FILES]`

The theorem contract in `problem.md` controls. Do not silently weaken its
algorithm class, numerical assumptions, task order, or success metric.

Write your full report to `[UNIQUE OUTPUT PATH]`. Do not edit another agent's
report or the shared registry.

## Role

You are the **[PRIMARY CONSTRUCTOR / ORTHOGONAL CONSTRUCTOR /
INDEPENDENT STRESS-TESTER / INDEPENDENT AUDITOR]**.

[ONE PARAGRAPH ROLE OVERLAY. Specify a mechanism or stress-test objective, not
an expected conclusion.]

## Exact objective

Obtain one of:

1. [VICTORY A];
2. [VICTORY B];
3. [VICTORY C];
4. an explicit legal algorithm or counterexample satisfying [VICTORY D].

The result must use one uniform algorithm before the instance quantifier when
claiming computational or query hardness.

## Construction seeds

Treat each seed as unproved:

1. **[SEED A].** [Smallest concrete mechanism and why it might work.]
2. **[SEED B].** [Materially different mechanism.]
3. **Negative route.** Search for a theorem showing that the proposed family
   always admits [RELEVANT BYPASS CLASS].

Do not allocate all effort to the first aesthetically attractive seed.

## What counts as progress

Produce at least one:

- explicit mathematical construction;
- fully stated lemma with proof;
- reduction with a simulator and decoder;
- legal counteralgorithm with resource analysis;
- smallest counterexample;
- symbolic or numerical falsification tied to a precise claim.

Status prose and lists of possible future ideas are not progress by
themselves.

## Non-results

Do not present:

- [PROBLEM-SPECIFIC NON-RESULT 1];
- [PROBLEM-SPECIFIC NON-RESULT 2];
- a pointwise hardcoded lower bound;
- ordinary NP-hardness as an exponential-time theorem;
- a reduction whose any-solution decoding step is assumed;
- an exponential candidate count without excluding compressed algorithms;
- a local or infinitesimal discrepancy instead of the declared operational
  success gap.

## Mandatory stress-test questions

For every survivor:

1. Can a direct algebraic normalization remove the obstruction?
2. Can an improper solution bypass the intended witness?
3. Does public information leak the hidden object?
4. Is a task or oracle query being used without charge?
5. Does a matrix/convex/dynamic-programming representation compress the
   apparent search?
6. Are any singular values, margins, or constants vanishing with dimension?
7. Does the reduction simulate the complete view of the alleged solver?
8. Does every low-loss or successful output yield the hard object?
9. Is the positive side actually efficient under the same accounting?
10. Is the claim task-indexed, average-case, or restricted-class while being
    described more broadly?

Add problem-specific breakers from `problem.md`.

## Run-local registry

Maintain:

| Approach | Exact candidate | Proved lemma | Breaker tried | Status | Next falsifier |
|---|---|---|---|---|---|

Use `proved`, `derived`, `conditional pass`, `hypothesized`, `blocked`,
`refuted`, or `unknown`.

## Cyclic protocol

### Cycle 1: construct independently

Write the smallest explicit object for which your mechanism might work.
Attempt to break it immediately.

### Cycle 2: extract proof gates

Separate algebraic obligations from new complexity or information-theoretic
assumptions. If the missing lemma merely restates the goal, mark the route
blocked.

### Cycle 3: act as the adversary

Try direct decoding, alternative coordinates, improper solutions, leaked
information, numerical edge cases, and compressed algorithms. Give the actual
procedure or counterexample.

### Cycle 4: synthesize and redirect

Update the registry, preserve exact blockers, and redirect effort to the
smallest falsifiable lemma. Revisit a blocked route only when a new invariant
or reduction appears.

Repeat while a cycle produces concrete mathematical progress.

## Return contract

Return exactly one of:

1. a complete proof satisfying a victory condition;
2. a complete negative/removal result;
3. the strongest rigorously derived survivor, its exact scope, the smallest
   legal breaker, and one sharply stated missing lemma.

Include:

- formal statement;
- construction or algorithm;
- proof or derivation;
- resource and quantifier audit;
- adversarial audit;
- evidence labels;
- exact follow-up task for an independent agent.

Never combine different partial constructions into a theorem that no single
construction satisfies.

---

## Role overlays

Use one overlay per agent.

### Primary constructor

Pursue the mechanism most directly suggested by the problem. Track constants
and edge cases from the start. You must still attempt the strongest obvious
bypass before reporting a survivor.

### Orthogonal constructor

Avoid the primary mechanism. Change at least one of the mathematical language,
hardness assumption, dual formulation, or proof technique. The purpose is to
discover a genuinely independent route or impossibility barrier.

### Independent stress-tester

Assume the proposed statement is false or overstated. Construct the strongest
legal solver, normalization, improper predictor, counterexample, or
quantifier flaw. If all breakers fail, isolate exactly why.

### Independent auditor

Do not extend the candidate creatively until its written proof has been
checked line by line. Verify algebra, quantifiers, constants, runtime,
finite-precision qualifications, reduction simulation, and any-solution
decoding. Return `PASS`, `CONDITIONAL PASS`, or `FAIL` with a minimal patch or
counterexample.
