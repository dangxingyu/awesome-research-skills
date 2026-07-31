# Prediction protocol

A prediction here is an instrument for understanding, not a forecast to be
graded. Writing outcome branches externalizes the implicit model of the
problem; when a result lands, the diff between predicted and observed
localizes which assumption was wrong. Judge predictions by how well they
localize error, not by hit rate.

## Writing outcome branches

Work backward from moves. List the next moves the result could trigger, then
partition the outcome space by them: one branch per distinct next move, and
outcomes that lead to the same move merge into one branch. Aim for 2-4
branches plus the surprise branch.

A branch set is vacuous when every branch has nonzero weight and the same
implication — that is hedging, not predicting. Test: if no branch's
realization would change the plan, the experiment does not deserve its slot.

Example, for "ablate component C":

- Branch A — metric drops by more than the declared threshold. Implication:
  C is load-bearing; keep it and analyze why. Next: mechanism experiment.
- Branch B — metric is flat. Implication: C is removable; simplify the
  method and weaken the claim accordingly. Next: rerun headline comparison
  without C.
- Surprise — metric improves. Verify first; if real, the story about C's
  role is wrong, which is more interesting than either predicted branch.

A bad version of the same branch set: "C helps a lot / helps somewhat /
helps little" — surface gradations with one shared implication.

## Credences

Give each branch a coarse credence (steps of 0.05-0.1), summing to roughly 1
including surprise. Label them beliefs to falsify. Their job is to force a
stand and make surprise well-defined; do not tune them for calibration and
do not present them as estimates. A branch below 0.05 either merges into
surprise or stays as a named long shot with a stated reason.

## The surprise branch

Mandatory for every experiment, with this pre-committed order:

1. **Verify** the anomaly is real. Bugs, data leakage, and measurement or
   evaluation error are the first suspects; a surprising result is the
   strongest signal to audit the pipeline, not to celebrate.
2. **Localize** the assumption — in the contract or in the branch set — that
   the verified result breaks.
3. **Reassess** whether the anomaly is more interesting than the original
   question. If it is, record a pivot proposal as a new kernel candidate
   rather than silently rewriting the plan.

Never absorb a surprising result into the nearest predicted branch after the
fact.

## Ordering experiments

Prioritize by, in order:

1. **Implication divergence:** branches lead to genuinely different moves.
2. **Genuine uncertainty:** no branch carries credence above about 0.9.
3. **Cost:** cheaper first at equal information.

Stage 1 must be the cheapest experiment that can kill the project. An
experiment whose branches all imply the same next move is monitoring, not
research; schedule it late or drop it.

## After a result

Record the observed branch in `predictions.md` beside the prediction, and
update the roadmap's status marks. On surprise, run the protocol above. When
reporting with `write-experiment-reports`, include predicted versus observed
per experiment; the pre-registered branch set is the defense against
post-hoc rationalization.
