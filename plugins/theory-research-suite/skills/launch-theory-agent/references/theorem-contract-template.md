# Theorem contract template

Use this template to convert an informal research direction into an object
that multiple agents can scrutinize without silently changing the problem.

## 1. Research objective

Write one sentence of the form:

> Construct/prove/refute **X** such that **Y**, against **algorithm class A**,
> using at most/at least **resource B**, under **assumption C**.

Name the asymptotic or security parameter. Distinguish an absolute theorem
from a theorem schema or conjecture.

## 2. Mathematical setting

Define:

- objects and dimensions;
- domain and distributions;
- maps, models, losses, or invariants;
- allowed regularity and numerical assumptions;
- public, secret, sampled, and externally chosen quantities.

State exact identities before asymptotic approximations.

## 3. Order of play and quantifiers

Write the experiment chronologically. Then write the main value or theorem
with quantifiers.

For a uniform computational claim, prefer:

\[
\inf_{A\in\mathcal A_{\rm uniform}(B(n))}
\mathbb E_{s\sim\Pi_n}
\left[L(A(\operatorname{view}(s)))\right].
\]

The algorithm is selected before `s`. A pointwise expression such as
`\mathbb E_s inf_A` may allow an algorithm that hardcodes the witness for each
fixed instance and is therefore unsuitable for a complexity lower bound.

Specify whether the result is:

- average-case or worst-case;
- task-indexed or task-agnostic;
- uniform or nonuniform;
- proper or improper;
- deterministic, randomized, SQ, sample-based, first-order, or general-time.

## 4. Resource accounting

Charge every action that can use problem-dependent information:

- oracle/sample/statistical queries;
- preprocessing;
- validation and calibration;
- hyperparameter or optimizer search;
- canonicalization or representation recovery;
- training and inference used by the solver.

State the machine model or query oracle precisely enough to interpret an
exponential claim.

## 5. Success metric

Define a bounded operational metric whenever possible. State:

- positive/benign threshold;
- negative-case threshold;
- constant or asymptotic gap;
- expectation, probability, or quantile;
- finite-horizon or convergence criterion.

Parameter distance, gradient angle, or optimizer response is not an
operational metric unless the theorem proves that it forces this success gap.

## 6. Victory conditions

Use multiple levels when appropriate:

- **Victory A:** strongest unconditional theorem.
- **Victory B:** strongest conditional theorem under a named assumption.
- **Victory C:** rigorous restricted-class or query lower bound.
- **Victory D:** explicit efficient breaker, remover, or impossibility theorem
  ruling out the proposed family.
- **Victory E:** sharply falsifiable candidate with every missing lemma named.

For separations, require an explicit efficient positive-side algorithm and, if
claiming a threshold rather than impossibility, an explicit upper-bound
algorithm at or above the hard resource scale.

## 7. Non-results

List tempting substitutes that do not satisfy the objective. Common examples:

- a result for one optimizer or learning rate;
- a local response discrepancy;
- ordinary NP-hardness advertised as an exponential lower bound;
- an exponential number of formal candidates without excluding compressed
  algorithms;
- a reduction that assumes its decoding lemma;
- a hard task whose positive side is equally hard;
- a task-indexed construction described as task-agnostic;
- a pointwise lower bound with nonuniform hardcoding;
- hidden numerical degeneracy or unmatched resources.

## 8. Independent stress audit

Require every proposed route to answer:

1. What is the simplest legal bypass?
2. Can an improper solution achieve low loss without recovering the intended
   structure?
3. Does the public view leak the witness?
4. Is the hardness in the transformation or merely in the downstream task?
5. Can a global algebraic operation solve what is described as a combinatorial
   search?
6. Is the assumption strong enough for the claimed time exponent?
7. Does every low-loss output decode to the hard object required by the
   reduction?

## 9. Evidence and stopping rules

Use evidence labels:

- `proved`: complete argument checked against the contract;
- `derived`: follows from written calculations, but not fully independently
  audited;
- `conditional pass`: proof survives audit after explicit local repairs;
- `hypothesized`: plausible route with a missing bridge;
- `blocked`: next lemma is equivalent to the original problem or lacks an
  actionable test;
- `refuted`: a legal counterexample or bypass exists;
- `unknown`: insufficient evidence.

Stop only at an audited victory condition or a precise frontier containing the
strongest survivor, smallest breaker, and exact next lemma.
