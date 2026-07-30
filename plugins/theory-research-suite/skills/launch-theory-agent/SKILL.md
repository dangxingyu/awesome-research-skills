---
name: launch-theory-agent
description: Formalize a mathematical or theoretical research problem, write a self-contained cyclic research prompt, launch independent construction and stress-test subagents, and iterate through proof-gate extraction, independent auditing, and synthesis. Use when the user asks to launch theory agents, explore a theorem or separation with subagents, turn a research question into a multi-agent proof search, apply a cyclic prompt to theoretical work, or rigorously seek a proof, counterexample, lower bound, construction, or impossibility result.
---

# Launch Theory Agent

Turn an informal theory question into a falsifiable theorem contract before
launching agents. Run a cyclic research process that rewards explicit lemmas,
counterexamples, and audited reductions rather than parallel brainstorming.

## Select the operating mode

Infer the mode from the request:

- **Launch mode:** Prepare the workspace and actually spawn subagents when the
  user asks to launch, explore with agents, or run the cyclic process.
- **Prepare-only mode:** Write the contract and launch prompt without spawning
  agents only when the user explicitly asks for a prompt, plan, or skill
  artifact rather than execution.
- **Continue mode:** Reuse an existing theory workspace, registry, and reports.
  Do not restart completed cycles.

Using this skill in launch mode counts as an explicit request for subagent
work. Use collaboration subagents, not user-owned Codex threads.

## Read the reusable references

Before creating the theory workspace, read:

1. [theorem-contract-template.md](references/theorem-contract-template.md)
2. [cyclic-agent-prompt.md](references/cyclic-agent-prompt.md)

Read any problem-specific source files the user supplies. If a cited paper or
web page is essential and its contents are unavailable locally, retrieve it
before formalizing the statement.

## Phase 1: Understand before launching

Inspect the current project with `rg --files` and `rg`. Identify:

- the current claim or toy result;
- why it is insufficient;
- the intended model, mathematical objects, and asymptotic parameter;
- the legal algorithm/adversary class;
- the resource being separated;
- assumptions the user accepts;
- existing constructions, failed attempts, and known bypasses.

Do not launch an agent while the central quantifiers remain ambiguous. Make a
reasonable narrow assumption when it preserves the user's intent; state it in
the contract. Ask the user only when different choices would define materially
different research problems.

## Phase 2: Write the theorem contract

Choose an existing research directory when one is obvious. Otherwise create:

```text
<project-root>/theory_search/<problem-slug>/
├── problem.md
├── prompt-cyclic.md
├── registry.md
├── tracks/
├── agent_reports/
├── audits/
└── scratch/
```

Write `problem.md` before `prompt-cyclic.md`. Follow the contract template and
make these items explicit:

1. mathematical setting and notation;
2. order of play and quantifier order;
3. allowed information and algorithm class;
4. charged resources and asymptotic parameter;
5. exact success metric;
6. primary and fallback victory conditions;
7. non-results that do not count;
8. numerical, regularity, or matchedness constraints;
9. required explicit upper-bound algorithm or remover, when relevant;
10. evidence labels and stopping conditions.

For complexity claims, quantify one uniform algorithm before the instance or
concept. Reject pointwise minima that allow a different hardcoded algorithm
for every instance.

For operational separations, measure end-to-end success. A gradient
discrepancy, parameter distance, or hard canonical form is not sufficient
unless it forces the declared loss or risk gap.

## Phase 3: Build the cyclic launch prompt

Copy and specialize the structure in `references/cyclic-agent-prompt.md`.
Make `prompt-cyclic.md` self-contained enough that an agent with no chat
history can work from it.

Include:

- absolute paths to the contract and relevant project sources;
- the exact target and allowed theorem variants;
- at least two materially different construction seeds;
- mandatory stress-test questions;
- an approach registry schema;
- explicit non-results;
- a cyclic protocol;
- a file path unique to each agent;
- a strict return contract.

Do not encode an expected answer as a fact. Label speculative seeds as
unproved. Preserve enough independence that different agents can discover
different breakers.

## Phase 4: Launch a diverse first wave

Check available collaboration capacity. Prefer three subagents when capacity
allows:

1. **Primary constructor:** Develop the most natural explicit construction or
   proof route.
2. **Orthogonal constructor:** Use a materially different mechanism,
   assumption, or formulation.
3. **Independent stress-test / impossibility agent:** Seek legal bypasses,
   counterexamples, quantifier bugs, and polynomial algorithms.

Use fewer agents if the problem admits fewer genuinely independent tracks.
Never spend two slots on paraphrases of the same mechanism.

Prefer `fork_turns="none"` after the workspace prompt is self-contained. Give
each agent:

- the shared prompt path;
- a concise role overlay;
- a unique output path under `agent_reports/`;
- a prohibition on editing another agent's report;
- a requirement to state equations, reductions, algorithms, or
  counterexamples rather than only recommendations.

Keep synthesis ownership with the root agent. Agents may update run-local
tables in their own reports; only the root edits the shared registry.

## Phase 5: Run the cycles

Do not stop after the first wave.

### Cycle 1: Independent construction or refutation

Require the smallest explicit object for which the mechanism could work.
Require immediate falsification attempts. Record:

| Approach | Exact candidate | Proved lemma | Breaker tried | Status | Next falsifier |
|---|---|---|---|---|---|

Keep routes independent until each has concrete mathematics.

### Cycle 2: Proof-gate extraction

Read every first-wave report yourself. For each survivor:

- separate algebraic lemmas from genuine hardness assumptions;
- identify the exact missing bridge;
- mark a route `blocked` if the bridge merely restates the original problem;
- assign the candidate to a different agent for independent audit;
- request constant tracking, quantifier checking, and edge cases.

Use `followup_task` for a completed agent or spawn a fresh auditor if capacity
and independence warrant it.

### Cycle 3: Removal stress test

Make the strongest legal defender or counterexample explicit. Test:

- direct decoding or trivial normalization;
- alternate coordinates, gauges, or canonicalizations;
- improper solutions that bypass the intended witness;
- information leakage through inputs, labels, metadata, or checkpoints;
- numerical degeneracy;
- hidden nonuniformity;
- uncharged computation or oracle calls;
- compressed algorithms for an apparently exponential search space.

A breaker must give an executable procedure or a precise mathematical
argument. A defense must explain exactly which assumption or budget the
breaker violates.

### Cycle 4: Synthesis and redirection

Write a synthesis under `tracks/` and update `registry.md` with only concise,
audited facts. Classify every route as:

- `proved`;
- `derived`;
- `conditional pass`;
- `hypothesized`;
- `blocked`;
- `refuted`;
- `unknown`.

Redirect the next cycle toward the smallest unresolved lemma, not the most
attractive narrative. Reopen a blocked route only after a new invariant,
reduction, or construction appears.

Repeat while agents produce concrete progress. Stop when a victory condition
is audited, every route has a precise blocker, or another cycle would only
repeat existing arguments.

## Phase 6: Validate the result

Before calling any result a theorem, verify:

- every symbol and distribution is defined;
- the quantifier order matches the complexity claim;
- all resource accounting is end-to-end;
- the benign or positive side has an explicit algorithm;
- the lower-bound side covers every algorithm in the declared class;
- any-low-loss output yields the hard witness when a reduction needs that;
- constants do not vanish after normalization;
- finite-precision or regularity claims are stated honestly;
- a claimed exponential result uses an assumption strong enough to imply it;
- independent audit findings are incorporated, not relegated to footnotes.

When useful, run small symbolic or numerical falsification scripts in
`scratch/`, but never treat experiments as proofs.

## Final response

Lead with the strongest surviving result and its scope. Link:

- `problem.md`;
- `prompt-cyclic.md`;
- the latest synthesis;
- the decisive construction reports and audits;
- `registry.md`.

State clearly whether the outcome is:

1. a complete audited proof;
2. a complete negative or removal result;
3. a conditional theorem;
4. a derived construction with named missing lemmas; or
5. a refutation with the smallest legal breaker.

Do not merge complementary partial results into a stronger theorem that no
single construction satisfies.
