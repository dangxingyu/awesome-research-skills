# Experiment Report Contract

Use this contract to audit a report before drafting prose. Omit fields that are
truly irrelevant, but do not omit fields merely because they are difficult to
recover.

## 1. Evidence ledger

Create one row per material claim:

| Claim ID | Exact claim | Status | Source | Run/checkpoint | Test or derivation | Caveat |
|---|---|---|---|---|---|---|
| C1 | ... | measured | `results.json` | `run_x/step_y` | paired bootstrap | ... |

Allowed status labels:

- `measured`: directly produced by an executed evaluation;
- `derived`: follows from shown measurements or algebra;
- `implemented-not-run`: present in code but not executed;
- `planned`: specified but not executed;
- `unknown`: evidence is missing or contradictory.

Record result provenance at the granularity needed to reproduce the number.
A directory name alone is insufficient when it contains multiple checkpoints,
splits, or metric definitions.

## 2. Algorithm contract

For each algorithm, fill the following fields.

### Quantity and target

- What conditional or population quantity is intended?
- What finite-sample target is observed?
- Which positions/examples are valid?
- What boundaries, padding, or missing values are masked?
- Is the target detached from the model that produces it?
- Is the target stationary, moving, bootstrapped, truncated, or normalized?

### Model and prediction

- Which representation is read?
- Which layers, pooling, concatenation, or normalization are used?
- What is the output parameterization?
- How is a prediction decoded for evaluation?
- What extra parameters, FLOPs, memory, or latency are introduced?

### Objective

Write the per-example loss and the full optimized loss. For each term, state:

- coefficient and schedule;
- reduction order and denominator;
- units and normalization statistics;
- clipping or binning;
- target distribution, if categorical;
- gradient path and detach boundaries;
- parameters updated by the term.

For a joint objective,

\[
\mathcal L(\theta,\phi)
=
\mathcal L_{\mathrm{main}}(\theta)
+ \lambda \mathcal L_{\mathrm{aux}}(\theta,\phi),
\]

state whether the auxiliary input is detached. If it is detached, the
auxiliary loss does not update \(\theta\), regardless of its presence in the
reported scalar objective.

### Execution

List training operations in actual order:

1. read and transform the batch;
2. run the model and retain required activations;
3. construct targets and masks;
4. update running statistics;
5. compute main and auxiliary objectives;
6. scale, accumulate, and synchronize gradients;
7. clip, step optimizer, and update scheduler;
8. save checkpoints and evaluation artifacts.

## 3. Experiment contract

Use a common-protocol section for truly shared values, then give overrides for
each experiment.

| Field | Required detail |
|---|---|
| Purpose | Falsifiable question and decision rule |
| Algorithm | Exact objective/mode and implementation path |
| Changed variables | Variables intentionally changed from the control |
| Fixed controls | Initialization, data order, token budget, and other controls |
| Model | Architecture, parameter count, checkpoint, trainable modules |
| Data | Dataset version, split, filters, preprocessing, tokenizer, packing |
| Shape terms | Context length, loader sequence length, chunk size, horizon |
| Optimizer | Type, betas, epsilon, weight decay, clipping |
| Schedule | Peak/base LR, warmup, decay, per-module LR |
| Batch | Per-device and global batch, accumulation, device count |
| Runtime | Precision, parallelism, compiler/kernel settings, hardware |
| Exposure | Steps, exact tokens/examples, epochs or corpus repetitions |
| Replication | Seeds and what the seed controls |
| Selection | Checkpoint and stopping rule |
| Evaluation | Split, sample count, metric, aggregation, baselines |
| Uncertainty | Resampling unit, pairing, interval/test, multiplicity |
| Artifacts | Config, logs, checkpoints, metrics, plots, manifest |

Never let `chunk_size` stand alone. Qualify it, for example:

- `attention_context_length`;
- `loader_sequence_length`;
- `value_mlp_chunk_size`;
- `future_target_horizon`;
- `evaluation_block_size`.

These quantities can be numerically equal while having different semantics.

## 4. Result contract

For each experiment, report:

1. question;
2. setting and deviations from common protocol;
3. evaluation and uncertainty;
4. result with units;
5. interpretation bounded by the test;
6. failure modes or unresolved alternatives;
7. next decision.

When comparing algorithms, verify that token exposure, checkpoint selection,
data order, evaluation examples, and metric implementation are comparable.
Label non-comparable results instead of computing a misleading delta.

## 5. Decision contract

End with a decision that follows from preregistered or explicitly stated
criteria:

- proceed;
- proceed conditionally;
- revise and rerun;
- stop the approach;
- retain only a narrower claim.

Separate scientific survival of the idea from engineering viability. A probe
can establish information in a representation while an online head fails on
throughput, transfer, calibration, or downstream utility.
