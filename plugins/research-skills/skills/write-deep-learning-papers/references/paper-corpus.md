# Representative Paper Corpus and Writing Lessons

## Contents

1. Selection method
2. Kaiming He
3. Kaifeng Lyu
4. Tengyu Ma
5. Percy Liang
6. Cross-corpus synthesis

## 1. Selection method

This is a representative, not exhaustive, corpus, curated on 2026-07-13. Papers were selected from the researchers' official publication pages using a mix of author emphasis, awards or venue recognition, field influence, and coverage of distinct paper archetypes. The source pages are [Kaiming He](https://people.csail.mit.edu/kaiming/), [Kaifeng Lyu](https://kaifeng.ac/), [Tengyu Ma](https://ai.stanford.edu/~tengyuma/), and [Percy Liang](https://cs.stanford.edu/~pliang/papers/).

The lessons below are abstractions from argument structure and evidence design. They are not instructions to imitate an author's wording or persona.

## 2. Kaiming He

### Deep Residual Learning for Image Recognition

- **Source:** [arXiv:1512.03385](https://arxiv.org/abs/1512.03385), CVPR 2016.
- **Core result:** Residual parameterization makes substantially deeper networks easier to optimize and enables accuracy gains from depth.
- **Why it belongs:** It is the signature ResNet paper and won the CVPR 2016 Best Paper Award; He's official page identifies ResNets as his best-known work.
- **Writing lesson:** Start from a falsifiable anomaly: deeper plain networks have higher *training* error, so the degradation is not ordinary overfitting. Use a constructive thought experiment—the added layers could implement identity—to motivate the parameterization. Test the explanation with matched plain/residual networks before expanding to benchmarks and transfer.

### Mask R-CNN

- **Source:** [arXiv:1703.06870](https://arxiv.org/abs/1703.06870), ICCV 2017.
- **Core result:** A parallel mask branch extends Faster R-CNN to instance segmentation; RoIAlign fixes spatial misalignment and is critical to mask quality.
- **Why it belongs:** ICCV 2017 Marr Prize; a durable framework spanning segmentation, detection, and keypoints.
- **Writing lesson:** A paper can be conceptually simple without being technically trivial. State the one-line extension early, then identify the apparently minor implementation detail that controls performance. Use component ablations and task generalization to show both necessity and breadth.

### Momentum Contrast for Unsupervised Visual Representation Learning

- **Source:** [arXiv:1911.05722](https://arxiv.org/abs/1911.05722), CVPR 2020.
- **Core result:** A queue plus momentum encoder creates a large, consistent dictionary for contrastive learning and yields strong transfer.
- **Why it belongs:** A central self-supervised learning paper, presented orally and nominated for best paper at CVPR 2020.
- **Writing lesson:** Reframe a busy literature through one shared abstraction—contrastive learning as dictionary lookup. Derive two design requirements (large and consistent), map each to a mechanism, and validate representations on downstream transfer rather than relying only on the pretraining benchmark.

### Masked Autoencoders Are Scalable Vision Learners

- **Source:** [arXiv:2111.06377](https://arxiv.org/abs/2111.06377), CVPR 2022.
- **Core result:** An asymmetric encoder-decoder and high masking ratio make masked image modeling efficient, scalable, and transferable.
- **Why it belongs:** CVPR 2022 oral and best-paper nominee; one of He's highlighted self-supervised learning works.
- **Writing lesson:** Ask why a successful idea in one modality behaves differently in another. Reason from the nature of the signal—image redundancy versus language density—to motivate a non-obvious design choice. Connect simplicity to measurable scale, training efficiency, and downstream transfer.

## 3. Kaifeng Lyu

### Gradient Descent Maximizes the Margin of Homogeneous Neural Networks

- **Source:** [arXiv:1906.05890](https://arxiv.org/abs/1906.05890), ICLR 2020.
- **Core result:** Under stated conditions, gradient flow/descent on homogeneous models increases a normalized margin and converges in objective value to a KKT point of a max-margin problem.
- **Why it belongs:** ICLR 2020 oral; a foundational contribution on implicit bias in deep homogeneous models.
- **Writing lesson:** State the open theoretical question, build from the best-understood special case, and identify exactly which assumptions are weakened. Keep the formal conclusion precise—KKT is not global optimality. Use experiments to test the predicted quantity while openly noting cases outside the proof, such as networks with biases.

### Reconciling Modern Deep Learning with Traditional Optimization Analyses: The Intrinsic Learning Rate

- **Source:** [arXiv:2010.02916](https://arxiv.org/abs/2010.02916), NeurIPS 2020.
- **Core result:** For normalized networks, the product of learning rate and weight decay acts as an intrinsic learning-rate parameter governing equilibrium behavior.
- **Why it belongs:** It connects optimization theory to commonly used normalization and training schedules.
- **Writing lesson:** Organize the paper around a mismatch between classical analysis and modern practice. Introduce one named quantity that compresses the mechanism, then triangulate with SDE analysis, realistic experiments, and a clearly labeled conjecture. Separate what is proved, observed, and proposed.

### Understanding the Generalization Benefit of Normalization Layers: Sharpness Reduction

- **Source:** [arXiv:2206.07085](https://arxiv.org/abs/2206.07085), NeurIPS 2022.
- **Core result:** In scale-invariant normalized networks with weight decay, finite-step gradient descent can exhibit an implicit sharpness-reduction bias near a minimizer manifold.
- **Why it belongs:** A representative theory-and-experiments paper on normalization, optimization dynamics, and generalization.
- **Writing lesson:** Define a familiar but ambiguous concept carefully for the problem's invariances. Connect a formal local analysis to an observed training regime, test the prediction in simplified and neural settings, and end with the gap between theorem conditions and broader empirical behavior.

### Safety Alignment Should Be Made More Than Just a Few Tokens Deep

- **Source:** [arXiv:2406.05946](https://arxiv.org/abs/2406.05946), ICLR 2025.
- **Core result:** Current alignment often changes primarily the first few output-token distributions; this "shallow safety alignment" helps explain several jailbreak modes, and two prototype interventions improve robustness in tested settings.
- **Why it belongs:** ICLR 2025 Outstanding Paper Award and oral presentation.
- **Writing lesson:** Name a unifying failure mode, show how it explains several previously separate observations, and then test interventions derived from that explanation. Preserve defensive relevance while explicitly stating that prototype mitigations are not complete defenses.

## 4. Tengyu Ma

### Identity Matters in Deep Learning

- **Source:** [arXiv:1611.04231](https://arxiv.org/abs/1611.04231), ICLR 2017.
- **Core result:** Identity parameterization improves the optimization landscape of deep linear residual networks; accompanying theory, expressivity results, and experiments motivate simple residual architectures.
- **Why it belongs:** An early theory-to-practice treatment of the principle behind residual networks.
- **Writing lesson:** Elevate an architectural trick into a general design principle. Use a tractable model for a clean theorem, state the nonlinear extension as open, and let the theory inspire a deliberately stripped-down empirical architecture.

### Provable Guarantees for Self-Supervised Deep Learning with Spectral Contrastive Loss

- **Source:** [arXiv:2106.04156](https://arxiv.org/abs/2106.04156), NeurIPS 2021.
- **Core result:** An augmentation-graph formulation and spectral contrastive loss yield downstream linear-probe guarantees without the unrealistic conditional-independence assumption used by prior theory.
- **Why it belongs:** A notable bridge between realistic augmentation-based self-supervision, spectral graph theory, and competitive experiments.
- **Writing lesson:** Identify the precise assumption preventing prior theory from explaining practice. Replace it with a concrete structure that both supports a theorem and suggests an implementable objective. State what the abstraction omits, including optimizer implicit bias.

### An Explanation of In-context Learning as Implicit Bayesian Inference

- **Source:** [arXiv:2111.02080](https://arxiv.org/abs/2111.02080), ICLR 2022.
- **Core result:** In-context learning can emerge from latent-concept inference in coherent pretraining documents; a mixture-of-HMM analysis and controlled synthetic dataset reproduce several large-model phenomena.
- **Why it belongs:** An influential mechanistic explanation of in-context learning that combines theorem, synthetic testbed, and real-model observations.
- **Writing lesson:** Use a small controlled world to isolate a surprising large-scale phenomenon. Explain the distribution mismatch directly, prove a result in the toy world, and show which qualitative behaviors the toy world reproduces without claiming it fully explains real language models.

### Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training

- **Source:** [arXiv:2305.14342](https://arxiv.org/abs/2305.14342), ICLR 2024.
- **Core result:** Lightweight diagonal-Hessian estimates plus coordinate-wise update clipping yield a practical second-order optimizer with roughly a twofold speedup over AdamW in the reported GPT pretraining settings.
- **Why it belongs:** A strong example of optimization research evaluated with end-to-end compute and wall-clock accounting.
- **Writing lesson:** Begin with the operational cost of the bottleneck. Explain how each mechanism addresses a failure of prior methods, compare at equal target loss, and report steps, total compute, and wall-clock rather than a single proxy.

## 5. Percy Liang

### On the Opportunities and Risks of Foundation Models

- **Source:** [arXiv:2108.07258](https://arxiv.org/abs/2108.07258), 2021 report.
- **Core result:** The report defines and organizes the foundation-model paradigm around emergence, homogenization, capabilities, applications, technology, and societal impact.
- **Why it belongs:** It supplied a durable vocabulary and interdisciplinary research agenda for foundation models; Liang was an equal-contribution corresponding author.
- **Writing lesson:** A broad report still needs a small number of organizing concepts. Define the object carefully, explain why existing terms are insufficient, build a visible taxonomy, and trace technical choices to downstream and societal consequences.

### Holistic Evaluation of Language Models

- **Source:** [arXiv:2211.09110](https://arxiv.org/abs/2211.09110), TMLR 2023.
- **Core result:** HELM supplies a taxonomy, broad and multi-metric standardized evaluation, explicit recognition of missing coverage, dense model comparisons, and released raw artifacts.
- **Why it belongs:** A landmark benchmark/evaluation paper led by Liang that treats transparency and evaluation design as research contributions.
- **Writing lesson:** Start with the decision-shaping role of benchmarks. Define the design space before choosing datasets, disclose omissions, measure multiple desiderata on the same scenarios, standardize adaptation, and make raw predictions available for independent analysis.

### Data Selection for Language Models via Importance Resampling

- **Source:** [arXiv:2302.03169](https://arxiv.org/abs/2302.03169), NeurIPS 2023.
- **Core result:** DSIR scales classical importance resampling through hashed n-gram features, selects 100M documents efficiently, and links a data metric to downstream performance in the reported studies.
- **Why it belongs:** A clean data-centric method paper connecting formal problem setup, scalable implementation, and downstream evaluation.
- **Writing lesson:** Turn an informal heuristic practice into an explicit distribution-matching problem. Justify the approximation needed for scale, quantify its runtime, introduce a diagnostic metric, and test whether the metric predicts downstream behavior.

### DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining

- **Source:** [arXiv:2305.10429](https://arxiv.org/abs/2305.10429), NeurIPS 2023 spotlight.
- **Core result:** Group-DRO domain reweighting on a small proxy model produces mixture weights that improve much larger-model training in the tested Pile and GLaM settings.
- **Why it belongs:** A notable data-centric scaling paper coauthored by both Liang and Ma.
- **Writing lesson:** Decompose an expensive problem into reference, proxy, and full-scale stages. Make the scale-transfer claim explicit, compare downstream accuracy and steps-to-target, and devote discussion to reference-model choice, domain granularity, and limits of transfer across scale.

## 6. Cross-corpus synthesis

### Shared high-value moves

1. **Lead with a precise phenomenon.** Degradation, spatial misalignment, shallow safety alignment, unrealistic independence assumptions, or incomparable evaluation each gives the paper a concrete antagonist.
2. **Name a compact principle.** Residual learning, large-and-consistent dictionaries, intrinsic learning rate, augmentation graphs, emergence and homogenization, or holistic evaluation makes the insight portable.
3. **Keep method and explanation coupled.** The design follows from the stated failure; ablations, theorems, or controlled examples test that connection.
4. **Use simple models without disguising the gap.** Theory papers explain exactly what the tractable setting captures, then use experiments to probe relevance rather than treating the theorem as a proof of all practice.
5. **Evaluate the claimed object.** Representation papers emphasize transfer; optimizer papers report end-to-end cost; benchmark papers expose coverage and trade-offs; safety papers test relevant attacks and defenses.
6. **Treat limits as part of the result.** Strong papers name untested regimes, local assumptions, proxy choices, metric limitations, and incomplete defenses.

### Distinct emphases worth preserving

- **He:** empirical compression—one clear failure, one minimal mechanism, decisive ablations, and broad transfer.
- **Lyu:** formal scope—careful quantities, explicit assumptions, theorem/observation/conjecture separation, and mechanistic experiments.
- **Ma:** theory-practice bridges—tractable abstractions paired with controlled simulations or realistic scale tests.
- **Liang:** evaluation as infrastructure—taxonomy, standardization, visible incompleteness, multi-metric trade-offs, and released artifacts.

Use these as complementary lenses. Do not force an empirical architecture paper into the structure of a 160-page report, or a local convergence theorem into the rhetoric of a universal method.
