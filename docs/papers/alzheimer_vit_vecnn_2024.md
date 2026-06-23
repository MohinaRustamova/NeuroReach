# Vision Transformer-equipped CNNs for Alzheimer's Disease Diagnosis
**Authors:** Zhao et al.
**Published:** Frontiers in Neurology, December 2024
**DOI:** 10.3389/fneur.2024.1490829
**Access:** Open Access

---

## What They Did
Zhao et al. proposed VECNN (Vision transformer-equipped Convolutional Neural
Networks), a 3D CNN architecture enhanced with ViT-inspired components for
automated Alzheimer's disease diagnosis using 3D MRI scans.

- **Dataset:** ADNI — 2,248 3D MRI scans from 818 participants (188 AD,
  401 MCI, 229 HC), 1.5T T1-weighted sMRI only
- **Task:** 3-class classification — Healthy Control (HC), Mild Cognitive
  Impairment (MCI), Alzheimer's Disease (AD)
- **Architecture:** 3D ResNet-50 backbone modified with:
  - Swin Transformer-inspired block ratio (1:1:3:1 instead of 3:4:6:3)
  - Non-overlapping 4×4×4 stem convolution to reduce redundancy
  - Spatial separable convolution to mimic self-attention efficiently
  - GELU activation instead of ReLU
- **Training:** AdamW optimizer, lr=5e-5, batch size 16, 150 epochs,
  10-fold cross-validation
- **Results:** 92.14% accuracy, 93.27% sensitivity, 89.95% specificity
  on HC/MCI/AD task

---

## Key Takeaways
1. **CNN backbone + ViT components beats pure approaches** — the authors
   chose CNN as the backbone and embedded ViT-inspired mechanisms rather
   than using a pure ViT, because pure ViT is computationally too expensive
   for 3D volumetric data.

2. **Pretraining still matters** — ResNet-50 initialized following ViT
   training procedures; pretrained weights remain essential for convergence
   even in hybrid architectures.

3. **Non-overlapping stem convolution reduces redundancy** — replacing
   the standard 7×7 conv stem with 4×4×4 non-overlapping convolution
   improved accuracy by 0.29%, showing that ViT-style patching benefits
   CNN architectures too.

4. **Spatial separable convolution approximates self-attention cheaply** —
   depthwise + pointwise convolution mimics the weighted sum in
   self-attention at a fraction of the computational cost.

5. **3D vs 2D tradeoff** — 3D scans capture richer spatial information
   but require heavy preprocessing (skull stripping, bias field correction,
   registration) and significant compute. 2D slice-based approaches
   sacrifice some spatial context but are far more practical in
   low-resource settings.

---

## Gaps & Relevance to NeuroReach
1. **No cross-scanner domain adaptation** — the study uses only 1.5T
   ADNI scans. No evaluation across different scanner types or field
   strengths. This is the exact gap NeuroReach addresses with CORAL
   domain adaptation between OASIS and ADNI.

2. **Single dataset evaluation** — results are reported only on ADNI.
   No generalization testing to external datasets, making robustness
   claims limited.

3. **3D preprocessing is not feasible in low-resource settings** —
   skull stripping, bias field correction, and spatial registration
   require specialized software (FSL, ANTs) and computational resources
   unavailable in many Central Asian hospitals. NeuroReach's 2D
   slice-based approach is more deployable in these contexts.

4. **No accessibility focus** — the paper targets clinical settings
   with full infrastructure. NeuroReach explicitly targets early
   screening in underserved communities where neurologists are scarce.

5. **3-class vs 4-class** — VECNN classifies HC/MCI/AD. NeuroReach
   targets 4-class severity staging (Non Demented / Very Mild / Mild /
   Moderate Dementia), a finer-grained and clinically more informative
   task.

---

## How This Informs NeuroReach
- Validates the ViT + medical imaging direction
- Confirms ADNI is the right dataset for domain adaptation experiments
- Justifies 2D slice approach as a practical, deployable alternative
  to 3D volumetric methods
- Strengthens the CORAL motivation — cross-scanner generalization
  is an open and important problem
