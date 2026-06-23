# From CNNs to Vision Transformers: A Survey on Addressing Domain Shift
# and Adaptation Concepts in Medical Image Analysis
**Author:** Kaan Arik
**Published:** Archives of Computational Methods in Engineering, Springer, 2026
**DOI:** 10.1007/s11831-026-10702-8
**Access:** Open Access

---

## What They Did
Arik (2026) presents a comprehensive narrative review of 160 peer-reviewed
studies (2020–2025) examining how CNN and Vision Transformer architectures
address domain shift in medical imaging. Rather than proposing a new method,
the survey maps the landscape of domain adaptation strategies, identifies
when each architecture family is most appropriate, and highlights critical
gaps in evaluation practice.

Key contributions:
- Taxonomy of domain-shift types: scanner/acquisition shift, protocol shift,
  population shift, institution-level shift, modality shift, label/concept shift
- Framework comparing CNN, ViT, and hybrid CNN-ViT behavior across each
  shift type
- Categorization of adaptation strategies: adversarial learning, feature
  alignment (MMD, CORAL, Optimal Transport), self-supervised pretraining,
  and meta-learning/few-shot adaptation
- Critique of standard evaluation metrics (accuracy, Dice) as insufficient
  for domain-shift robustness — argues for domain-wise, worst-case, and
  calibration-aware reporting

---

## Key Takeaways

1. **CORAL is a validated feature alignment method for scanner shift** —
   the survey explicitly lists Deep CORAL among proven statistical feature
   alignment strategies for cross-scanner and cross-protocol domain shift.
   This directly validates NeuroReach's notebook 05 approach.

2. **ViT superiority is conditional, not universal** — ViTs outperform CNNs
   when global anatomical context is informative and pretraining is
   large-scale. They can underperform CNNs in small-data settings or when
   local morphology dominates. NeuroReach's setup (ImageNet-pretrained
   ViT-B/16, large OASIS dataset) fits the conditions where ViT is expected
   to be advantageous.

3. **CNNs overfit scanner-specific textures under domain shift** — the survey
   identifies this as a fundamental weakness of CNN inductive bias. This
   directly motivates moving from ResNet18 baseline to ViT + CORAL in
   NeuroReach.

4. **Scanner/acquisition shift is the most tractable domain-shift type** —
   when source and target domains share clinical semantics but differ in
   acquisition appearance (e.g., different MRI field strengths), feature
   alignment methods like CORAL are identified as the most appropriate
   strategy. OASIS (mixed scanners) → ADNI (1.5T standardized) is exactly
   this scenario.

5. **2D slice-based approaches are justified for low-resource deployment** —
   the survey notes that 3D volumetric methods carry prohibitive compute
   requirements and heavy preprocessing pipelines (skull stripping, bias
   correction), making them impractical in resource-constrained clinical
   settings. NeuroReach's 2D approach is explicitly the more deployable
   alternative.

6. **Average metrics are insufficient for domain shift evaluation** — the
   survey argues that reporting only pooled accuracy hides per-domain
   failure. NeuroReach's evaluation should report per-class F1, confusion
   matrix analysis, and cross-domain performance drop (OASIS test accuracy
   vs ADNI test accuracy before and after CORAL).

---

## Gaps Relevant to NeuroReach

1. **No study combines ViT + CORAL for Alzheimer's MRI** — the survey
   covers ViT-based domain adaptation broadly but identifies no work
   applying ViT + statistical feature alignment specifically to Alzheimer's
   severity staging. This is NeuroReach's primary novelty claim.

2. **No 4-class severity staging with domain adaptation** — existing
   domain adaptation studies on Alzheimer's use binary or 3-class
   classification (HC/MCI/AD). NeuroReach targets finer-grained 4-class
   staging (Non Demented / Very Mild / Mild / Moderate), which is both
   harder and more clinically informative.

3. **No evaluation in low-resource or Central Asian deployment contexts** —
   the survey identifies this as a general gap: most studies assume
   well-resourced clinical infrastructure. NeuroReach explicitly frames
   its contribution around deployability in underserved settings.

4. **Standardized cross-scanner benchmarks are missing** — the survey
   calls for standardized multi-site evaluation protocols. NeuroReach's
   OASIS → ADNI cross-scanner experiment directly addresses this need.

---

## How This Informs NeuroReach

- Provides theoretical justification for choosing CORAL over adversarial
  methods: lower complexity, proven for scanner/protocol shift, works
  with unlabeled target data
- Confirms that ViT + feature alignment is an emerging and underpopulated
  research direction — strengthens novelty argument
- Provides citation support for the claim that CNN baselines overfit
  scanner-specific textures, motivating the ViT upgrade
- Frames the evaluation strategy: report domain-wise metrics and
  cross-domain performance drop, not just overall accuracy
- Can be cited directly in the paper's related work section to establish
  the research gap NeuroReach fills
