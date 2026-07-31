---
name: write-experiment-reports
description: Audit experiment code, launch configurations, logs, metrics, and figures; then write a rigorous, reproducible technical report that defines each algorithm and loss, maps algorithms to executed experiments, records settings such as chunk size, learning rate, data, and evaluation, separates measured results from plans, and renders a page-checked PDF. Use for ML or systems experiment reports, internal research readouts, result summaries that need traceability, and Markdown-to-PDF research deliverables.
---

# Write Experiment Reports

Build the report from executable evidence. Make every important claim traceable
to an implementation, run configuration, result artifact, or explicit
derivation.

## Load the guidance

- Read [report-contract.md](references/report-contract.md) before drafting a
  substantial report or auditing an existing one.
- Read [pdf-delivery.md](references/pdf-delivery.md) when the deliverable
  includes PDF or print-ready HTML.
- Use [report-template.md](assets/report-template.md) as a starting structure,
  adapting it to the experiment rather than preserving empty sections.

## Phase 1: Establish the evidence base

Inspect the project before writing. Prefer `rg --files` and `rg`; use `find`
and `grep` when `rg` is unavailable. Locate:

- the implementation of every reported objective and algorithm;
- launch scripts, job specs, resolved configs, and checkpoint metadata;
- data manifests, preprocessing code, and split definitions;
- logs, metric tables, confidence intervals, plots, and result manifests;
- the code revision and environment used for each run;
- existing notes, preregistrations, reports, and declared decision gates,
  including pre-registered prediction ledgers when present (for example
  `research_plans/<slug>/predictions.md` from the `sharpen-research-ideas`
  skill).

Create an evidence ledger with one row per claim or reported number. Record its
source path, run/checkpoint identifier, evidence status, and any caveat.
Distinguish `measured`, `derived`, `implemented-not-run`, `planned`, and
`unknown`. Do not silently promote a plan or default config into an executed
setting.

Resolve conflicts according to what each source can establish:

- Use implementation code for objective semantics and gradient paths.
- Use resolved run configs and launch commands for executed hyperparameters.
- Use logs and result artifacts for measurements.
- Use dataset manifests for data identity and token/example counts.
- Treat prose summaries as navigation aids until corroborated.

If the repository changed after a run, report the run's revision. State
unresolved discrepancies instead of choosing the more convenient value.

## Phase 2: Specify every algorithm

For each algorithm or ablation, define:

1. estimand or intended quantity;
2. observed target and masking rules;
3. model components and inputs;
4. per-example loss;
5. complete optimized objective;
6. coefficients, normalization, clipping, and schedules;
7. every stop-gradient or detach boundary;
8. which parameters receive gradients from each term;
9. training steps in execution order;
10. inference or evaluation decoding.

Define every new term immediately after introducing it. State units and
averaging denominators. If a scalar is overloaded, separate meanings such as
attention context, loader sequence length, target horizon, and MLP chunk size.

Check gradient semantics algebraically. A detached additive baseline may change
the reported scalar loss while leaving the parameter gradient identical. A
detached weight can still bias the main gradient. Name negative controls as
negative controls.

## Phase 3: Map algorithms to experiments

Build an algorithm-to-experiment table before prose. Give every run family a
stable name and record:

- question and falsifiable hypothesis;
- algorithm/objective and exact changed variables;
- fixed controls;
- model, parameter count, initialization, and checkpoint;
- dataset, split, preprocessing, tokenizer, and packing;
- context length, sequence length, chunk size, and prediction horizon;
- optimizer, learning rate, schedule, warmup, precision, and clipping;
- global and per-device batch, gradient accumulation, devices, and seeds;
- steps, tokens/examples, checkpoint selection, and stopping rule;
- evaluation dataset, metric definition, unit of analysis, baselines, and
  uncertainty procedure;
- status and artifact paths.

Use exact token exposure when available. Do not substitute nominal steps for
tokens without showing the conversion. Separate training-time validation from
independent endpoint evaluation.

## Phase 4: Write from claims to evidence

Use an answer-first structure:

1. executive result;
2. algorithms and objectives;
3. common experimental protocol;
4. algorithm-to-experiment map;
5. experiment-specific settings and results;
6. main figure;
7. limitations and failure accounting;
8. decision boundary;
9. reproducibility artifacts.

State the strongest supported result first, including scope and major negative
results. Keep method claims separate from empirical claims. For every
experiment, describe the question, settings that differ from common protocol,
evaluation, result, and interpretation.

Report effect sizes and uncertainty, not only point estimates. Name the
resampling unit and whether comparisons are paired. Make clear when a result
is IID, OOD, checkpoint-selected, repeated-corpus, or token-matched.

When pre-registered predictions exist for an experiment, report predicted
versus observed outcomes and flag surprises explicitly rather than absorbing
them into the nearest prediction.

## Phase 5: Build claim-bearing figures

Choose figures only after the claim-evidence ledger is stable. Each figure must:

- answer a named experimental question;
- show the comparison and uncertainty needed for the claim;
- label dataset, metric, horizon or condition, and directionality;
- distinguish seeds or aggregate them with a declared rule;
- use consistent colors and scales across related panels;
- have a caption that states what is plotted and how uncertainty was computed.

Do not hide a decisive null result in a table while using a decorative plot as
the main figure. Regenerate plots from reviewed source data when possible.

## Phase 6: Render the deliverable

Write Markdown with one level-1 title and use `<!-- PDF_TOC -->` where the
table of contents should appear. Use `\(...\)` and `\[...\]` for math.

Render with the bundled tool:

```bash
python scripts/render_report.py \
  --input path/to/report.md \
  --output path/to/report.pdf \
  --html-output path/to/report.html
```

The script resolves the bundled stylesheet automatically. Install the Python
and KaTeX dependencies described in
[pdf-delivery.md](references/pdf-delivery.md) if they are missing.

## Phase 7: Validate before handoff

Run structural and visual checks:

```bash
python scripts/inspect_pdf.py \
  path/to/report.pdf \
  --contact-sheet path/to/contact-sheet.png \
  --expect-heading "Algorithms" \
  --expect-heading "Experiments"
```

Then inspect the contact sheet and full-resolution pages containing dense
tables, equations, and figures. Verify:

- no blank, clipped, overlapping, or nearly empty accidental pages;
- no unresolved placeholders, math tokens, or render errors;
- readable figures, captions, footnotes, tables, and equations;
- consistent headings, page numbers, and table of contents;
- artifact paths, hashes, dates, and run identifiers are accurate;
- the conclusion does not exceed the evidence ledger.

Re-render after any content or CSS change. Do not call a PDF finished based
only on a successful renderer exit code.

## Deliverables

Return or write:

- the source report;
- the PDF and, when useful, HTML;
- generated figures and reviewed source data;
- a compact artifact manifest with hashes or revision identifiers;
- a short list of unresolved evidence gaps.

Lead the final response with the main conclusion and link the report and PDF.
State any validation step that could not be run.
