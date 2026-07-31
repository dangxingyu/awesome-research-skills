# Submission-Readiness Checklist

Use this checklist after the argument and evidence are stable. Mark an item `N/A` only with a reason.

## 1. Central argument

- [ ] The paper has one central claim that can be stated in one sentence.
- [ ] The title and abstract describe the same contribution as the main results.
- [ ] The introduction names a precise gap, not only a broad important area.
- [ ] Each listed contribution is a claim with identifiable evidence.
- [ ] The conclusion does not expand the scope beyond the results.

## 2. Claim integrity

- [ ] Every abstract claim maps to a theorem, figure, table, or labeled analysis.
- [ ] `show`, `prove`, `suggest`, `observe`, and `hypothesize` are used according to evidence strength.
- [ ] Novelty and state-of-the-art claims were checked against current primary literature.
- [ ] "Significant" refers to a statistical test or has been replaced with precise language.
- [ ] Correlational results are not written as causal mechanisms.
- [ ] Local, asymptotic, simplified-model, and finite-scale results are scoped correctly.
- [ ] Null and contradictory results material to the claim are reported.

## 3. Related work and citations

- [ ] Primary sources support each technical or historical claim.
- [ ] Bibliographic fields and links are verified.
- [ ] The comparison to prior work uses factual design axes rather than dismissive labels.
- [ ] Concurrent or closely related work is distinguished precisely.
- [ ] Dataset, model, metric, and code creators receive appropriate credit.

## 4. Method and theory

- [ ] Inputs, outputs, objectives, notation, and execution order are unambiguous.
- [ ] Essential components are separated from optional engineering choices.
- [ ] Computational and memory complexity are stated where relevant.
- [ ] Every theorem states assumptions, quantifiers, probability, and conclusion precisely.
- [ ] The practical phenomenon captured by each theoretical model is explicit.
- [ ] The proof roadmap identifies the conceptual step; appendices contain enough detail to verify it.
- [ ] Claims such as stationary point, KKT point, local optimum, and global optimum are not conflated.

## 5. Experimental design

- [ ] Each experiment answers a stated research question or tests a claim.
- [ ] Baselines are relevant, strong, and comparably tuned.
- [ ] Data, parameters, training budget, tuning budget, and evaluation protocol are matched or differences disclosed.
- [ ] Main conclusions hold across enough seeds or repeated measurements.
- [ ] Uncertainty is visible in tables or plots when it affects interpretation.
- [ ] Ablations isolate hypothesized mechanisms and important interactions.
- [ ] Hyperparameter sensitivity and selection rules are reported.
- [ ] Transfer, scale, robustness, and failure regimes match the breadth of the claims.
- [ ] Data leakage, contamination, de-duplication, and target access are assessed.

## 6. Efficiency and systems

- [ ] Quality is matched when comparing speed or cost.
- [ ] Steps, tokens/examples, compute, wall-clock, hardware, precision, and peak memory are reported as applicable.
- [ ] One-time preprocessing, proxy training, search, compilation, indexing, and retry costs are included or excluded explicitly.
- [ ] Amortization assumptions are stated.
- [ ] Average and tail behavior are distinguished when deployment latency or reliability matters.

## 7. Benchmark and evaluation design

- [ ] The object of evaluation and intended decisions are stated.
- [ ] A taxonomy or design space precedes subset selection.
- [ ] Selection priorities and missing coverage are explicit.
- [ ] Adaptation, prompting, decoding, aggregation, and metric direction are standardized and documented.
- [ ] Sensitivity to evaluation choices is measured.
- [ ] Important trade-offs are not hidden by a single aggregate score.
- [ ] Raw predictions, prompts, or sufficient artifacts are available when promised.

## 8. Reproducibility

- [ ] Data sources, licenses, splits, filtering, preprocessing, and statistics are documented.
- [ ] Architecture, initialization, objective, optimizer, schedule, batch size, regularization, and stopping criteria are documented.
- [ ] Random seeds and software/hardware environments are documented.
- [ ] Evaluation code, model selection, and checkpoint choice are documented.
- [ ] Claimed artifacts exist, links work, and release limitations are stated.

## 9. Figures, tables, and prose

- [ ] Each main visual answers one question and is cited in order.
- [ ] Captions state setup, metric direction, uncertainty, and takeaway.
- [ ] Axes, units, legends, colors, and rounding are consistent and legible.
- [ ] Color is not the only carrier of meaning.
- [ ] Numbers agree across text, tables, figures, and appendix.
- [ ] Every acronym and symbol is defined before use.
- [ ] Each paragraph has one job and begins with its main point.
- [ ] Repetition, throat-clearing, and evidence-free adjectives are removed.

## 10. Limitations, ethics, and compliance

- [ ] Limitations are specific enough to change how a reader interprets or uses the work.
- [ ] Broader impacts address relevant data, privacy, licensing, bias, misuse, access, labor, and environmental issues.
- [ ] Safety claims distinguish prototype evidence from a complete defense.
- [ ] Human-subject, data-governance, and disclosure requirements are satisfied where applicable.
- [ ] Venue format, anonymity, page limits, checklist, artifact, and supplemental rules are satisfied.

## Final report

End the review with four lists:

1. **Blocking scientific issues**
2. **Unsupported or risky claims**
3. **Reproducibility gaps**
4. **Optional clarity and polish improvements**

Do not label the paper submission-ready while any blocking scientific issue remains.
