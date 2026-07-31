# Narrowing playbook

Operators and tests for turning a vague idea into one falsifiable project
without losing the kernel.

## Vagueness dimensions

Diagnose which dimensions are underdetermined, then apply that dimension's
operators. Most ideas are vague in one or two dimensions.

### Phenomenon unclear

Symptom: "I think X happens" with no concrete instance to point at.

- **Minimal demonstration:** construct the smallest setting in which X could
  visibly occur or visibly fail to occur.
- **Existence-first experiment:** before measuring how much, establish
  whether at all.
- **Effect-size probe:** a toy run that bounds whether the effect is large
  enough to study at the intended scale.

### Question unclear

Symptom: the phenomenon is known but no falsifiable question is on the table.

- **Contrast pair:** state X and the counterfactual world in which the
  candidate explanation is false; the question is what distinguishes them.
- **Formal quantity extraction:** name the number that moves if the idea is
  right, and its units.
- **Decision relevance:** name the choice that depends on the answer.

### Formalization unclear

Symptom: the question is clear but the model, testbed, or definitions are not.

- **Smallest nontrivial model:** the least machinery that can still express
  the question.
- **Testbed menu:** enumerate 2-3 concrete settings with one-line costs and
  what each can and cannot show.
- **Assumption budget:** list simplifying assumptions and check the intended
  conclusion does not secretly rely on one of them.

### Method unclear

Symptom: target and setting are fixed but the approach is open.

- **Baseline first:** the dumbest method that could work defines the floor.
- **Oracle probe:** run the method with privileged information; if even the
  oracle fails, the target is malformed, not the method.
- **Ablate from the nearest existing method** rather than inventing from
  scratch.

### Framing unclear

Symptom: the work is doable but the reason it matters wobbles.

- **Audience test:** name the reader who changes behavior if the claim holds.
- **Nearest-paper triangulation:** position against 2-3 real papers, not a
  strawman literature.
- **Claim-strength ladder:** write the weakest publishable claim and the
  strongest defensible claim; pick the rung the evidence can hold.

## Candidate quality bar

Every candidate must have: a trace back to the kernel; a mechanism distinct
from every other candidate; a named cheapest decisive experiment; a named
main risk; and a novelty label (`verified`, `suspected`, `unknown`) backed by
search or honestly marked `unknown`.

## Kill tests

1. **Falsifiability:** state the observation that would refute the claim. If
   none exists, the candidate is a framing, not a project.
2. **Feasibility:** the cheapest decisive experiment fits the declared
   compute, data, and time. Decisive means at least one plausible outcome
   forces a decision.
3. **Confound check:** describe the most boring world that produces the same
   positive result. If that world survives the experimental design, redesign
   or kill.
4. **Priority check:** search for the nearest existing result. Adjacent work
   alone is not a kill; a candidate dies only if the specific claim is
   already answered.
5. **So-what:** name who acts differently if the claim is true. Pure
   understanding is a valid answer only when the interview declared
   understanding as the success shape.

## Selection rubric

Score surviving candidates on kernel fit, expected information of the
stage-1 experiment, feasibility margin, and novelty confidence. Prefer the
candidate whose stage-1 experiment is cheap and able to kill it. Break ties
toward what the interview marked as the user's itch. Record scores and the
selection rationale in `candidates.md`; the decision is made autonomously,
not by asking the user.

## Anti-patterns

- **Premature convergence:** elaborating the first interpretation instead of
  generating rivals.
- **Paraphrase diversity:** candidates that differ in wording but share one
  mechanism.
- **Novelty hallucination:** "to our knowledge" without a search.
- **Questionnaire fatigue:** asking in dribs across phases. Interview once,
  early, then decide.
- **Wish-list plan:** linear tasks with no kill criteria and no branch that
  changes anything.
- **Kernel drift:** the selected project no longer contains the original
  itch. Re-anchor, or record the departure as a deliberate, user-visible
  decision.
