# {{Experiment Title}}: Experimental Report

Status date: {{YYYY-MM-DD}}. Code revision: `{{git revision}}`.

<!-- PDF_TOC -->

## 1. Executive result

State the strongest supported positive or negative result, its scope, the
decision it supports, and the most important limitation.

## 2. Algorithms

### 2.1 Estimand and observed target

Define the intended quantity, finite-sample target, masks, and stop-gradient
semantics.

### 2.2 Model and prediction

Define inputs, architecture, parameterization, and evaluation decoding.

### 2.3 Loss objectives

Write every per-example loss and the complete optimized objective. Define each
new term, coefficient, normalization, reduction, and gradient path.

### 2.4 Training algorithm

List the operations for one optimizer step in execution order.

## 3. Common experimental protocol

### 3.1 Model and implementation

Record architecture, parameter counts, code paths, initialization, precision,
parallelism, and hardware.

### 3.2 Data

Record dataset version, splits, filters, preprocessing, tokenizer, packing,
context length, sequence length, and exact exposure.

### 3.3 Optimization

Record optimizer, learning rate, schedule, warmup, clipping, batch,
accumulation, devices, steps, seeds, and checkpoint selection.

### 3.4 Evaluation

Define every metric, dataset, baseline, unit of analysis, interval or test,
pairing, and aggregation rule.

## 4. Algorithm-to-experiment map

| Experiment | Question | Algorithm | Changed settings | Fixed controls | Evaluation | Status |
|---|---|---|---|---|---|---|
| {{run family}} | {{question}} | {{objective}} | {{overrides}} | {{controls}} | {{protocol}} | {{status}} |

## 5. Experiments and results

### 5.1 {{Experiment name}}

**Question.** {{Falsifiable question}}

**Setting.** {{Overrides from common protocol, including chunk size and LR}}

**Evaluation.** {{Dataset, metric, baselines, uncertainty}}

**Result.** {{Effect size with units and uncertainty}}

**Interpretation.** {{Bounded conclusion and alternatives}}

## 6. Main figure

![{{Descriptive figure label}}]({{relative/path/to/figure.png}})

**Figure 1.** {{What is plotted, datasets, aggregation, and uncertainty.}}

## 7. Limitations and failure accounting

List missing controls, failed runs, non-comparable results, distribution
limits, compute costs, and evidence gaps that change interpretation.

## 8. Decision boundary

State the criteria and resulting proceed, revise, narrow, or stop decision.

## 9. Reproducibility artifacts

| Artifact | Path or identifier | Hash/revision | Purpose |
|---|---|---|---|
| Code | `{{path}}` | `{{revision}}` | implementation |
| Config | `{{path}}` | `{{hash}}` | executed settings |
| Results | `{{path}}` | `{{hash}}` | reported metrics |
| Figure data | `{{path}}` | `{{hash}}` | plot source |
