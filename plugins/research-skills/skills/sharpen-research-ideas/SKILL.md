---
name: sharpen-research-ideas
description: Turn a vague research idea, hunch, or observation into one crisp, falsifiable project idea and an executable project plan. Interview the user once, early, to capture the idea's kernel, constraints, and taste; generate materially different candidate projects; kill-test and select autonomously; write a project contract; then build a prediction-annotated experiment roadmap where every experiment declares 2-4 outcome branches, their implications, coarse credences, and a pre-committed surprise protocol. Use when asked to narrow down a vague idea, scope a project, turn a hunch into a research plan, decide which experiment to run first, or map experiments and their possible outcomes before running them.
---

# Sharpen Research Ideas

Narrow a vague idea into one falsifiable project and a plan that states its
predictions before anything runs. Preserve the user's kernel exactly; kill
weak variants with evidence rather than enthusiasm; treat the final plan as a
set of beliefs to be falsified, not a promise.

## Select the operating mode

Infer the mode from the request:

- **Interactive mode (default):** The user is present. Run exactly one
  interview round in Phase 1, then complete every later phase without
  blocking on the user.
- **Autonomous mode:** The user asked for a full pass without questions, or
  the run is non-interactive. Skip the interview, make narrow assumptions
  that preserve the kernel, and list them in the contract.
- **Revision mode:** A `research_plans/<slug>/` workspace already exists and
  the user is reacting to the contract or roadmap. Update the affected
  artifacts in place. Do not restart phases whose inputs did not change, and
  do not re-interview.

The Phase 1 interview is the only point in the workflow that may block on the
user. Later phases never ask; they decide and record the rationale.

## Read the reusable references

1. [narrowing-playbook.md](references/narrowing-playbook.md) before Phase 2.
2. [prediction-protocol.md](references/prediction-protocol.md) before Phase 6.
3. [project-contract-template.md](references/project-contract-template.md)
   when writing the contract.
4. [roadmap-template.md](assets/roadmap-template.md) when drawing the roadmap.

## Phase 1: Capture the kernel, then interview once

Restate the vague idea. Extract the **kernel**: the observation, intuition,
or itch that must survive narrowing, written near-verbatim in the user's own
terms. Everything else — setting, method, formalization, framing — is
negotiable. Record it in `kernel.md`; every later candidate must trace back
to it.

Inventory context before asking anything: notes, code, prior experiments,
and related drafts in the project. Do not ask a question the files already
answer.

In interactive mode, run one batched interview. Keep it short and concrete;
prefer reactions to options over open questions. Cover only the gaps that
survive the inventory:

- what itches: the phenomenon, the technique, or the application;
- resources: compute, data, time, and deadline;
- the success shape: paper, understanding, tool, or demo;
- non-negotiables and already-rejected directions;
- adjacent work the user already knows or is responding to.

This is the last user input the workflow assumes.

## Phase 2: Diagnose where the idea is vague

Classify which dimensions are underdetermined: phenomenon, question,
formalization, method, or framing. Definitions, symptoms, and the narrowing
operators for each dimension are in the playbook. Most vague ideas are vague
in one or two dimensions; do not redo dimensions the user has already fixed.

## Phase 3: Diverge into candidate projects

Generate 3-5 materially different crispenings that each preserve the kernel.
No two candidates may be paraphrases of the same mechanism. For each, record
in `candidates.md`:

- a one-sentence claim or question;
- how it traces back to the kernel;
- nearest neighbors in the literature — search when tools allow; label
  novelty `verified`, `suspected`, or `unknown`, and never assert novelty
  without evidence;
- the cheapest decisive experiment;
- the main risk.

## Phase 4: Kill-test and select — without the user

Apply the kill tests from the playbook to every candidate:

1. Is the central claim falsifiable as stated?
2. Is the cheapest decisive experiment within the declared resources?
3. Would a positive result actually support the interesting claim, or does a
   boring confound explain it equally well?
4. Has the specific claim already been answered, as far as available search
   can tell?
5. Who acts differently if the claim is true?

Rank the survivors and select one autonomously. Do not present the fork to
the user; the Phase 1 interview was the input channel. Record the selection
rationale in `candidates.md`, and keep the runner-ups: they become pivot
branches in the plan, not discards.

## Phase 5: Write the project contract

Follow the contract template. `contract.md` must state: title; one-sentence
claim; the kernel verbatim; setting and objects; the central falsifiable
hypothesis; what evidence would disprove it; success criteria; scope and
non-goals; the novelty statement with evidence labels; resource budget; and,
in autonomous mode, every assumption made in place of user input.

## Phase 6: Predict, then plan

Follow the prediction protocol. For each candidate experiment, write the
outcome tree before deciding the experiment order:

- **2-4 outcome branches, partitioned by implication.** If two outcomes lead
  to the same next move, merge them into one branch. Branch count comes from
  the distinctions that change decisions, not from surface differences.
  Enumerating everything predicts nothing.
- **A coarse credence per branch**, labeled as beliefs to falsify, not
  calibrated estimates. Their job is to force a stand and make surprise
  well-defined.
- **A mandatory surprise branch** ("none of the above") with the
  pre-committed protocol: verify the result is real — bugs, leakage, and
  measurement error are the first suspects — then localize which assumption
  broke, then assess whether the anomaly is more interesting than the
  original question and decide on a pivot.

Order experiments by implication divergence across branches, genuine
uncertainty, and cost. Stage 1 must be the cheapest experiment that can kill
the project. Deprioritize any experiment whose branches all imply the same
next move, however standard it looks.

Record the ledger in `predictions.md`: one row per experiment and branch,
with outcome class, credence, implication, and next move. Assemble `plan.md`
as a decision tree using the roadmap template: experiments as nodes,
predicted branches as labeled edges, surprise branches dashed, runner-up
candidates as pivot targets, and kill criteria explicit. Mark where sibling
skills take over: `launch-theory-agent` for theory branches,
`write-experiment-reports` after runs complete, `write-deep-learning-papers`
for the endgame.

## Workspace

```text
<project-root>/research_plans/<idea-slug>/
├── kernel.md
├── candidates.md
├── contract.md
├── predictions.md
└── plan.md
```

## Final response

Lead with the one-sentence project idea and the first concrete action (the
stage-1 experiment). Show the roadmap — render it inline when the platform
supports it, otherwise link `plan.md` — and invite reactions branch by
branch: which outcomes look interesting, doubtful, or wrong. Reactions enter
revision mode; they do not restart the pipeline. In autonomous mode, list
the assumptions that most deserve checking. Present the plan as falsifiable
beliefs, not a schedule.

## Do not

- converge on the first concrete interpretation of the idea;
- ask the user questions after Phase 1 — batch everything early;
- claim novelty without search evidence;
- write hedge-everything outcome lists that assign every result nonzero
  weight and identical implications;
- deliver a linear task list without kill criteria or pivots;
- rationalize a surprising result after the fact instead of running the
  surprise protocol.
