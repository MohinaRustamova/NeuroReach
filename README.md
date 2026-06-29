# 🧠 NeuroReach
AI-powered early screening and assistive support for Alzheimer's disease, Autism Spectrum Disorder, and neurological disabilities — built for underserved communities in Central Asia.

![Status](https://img.shields.io/badge/status-in%20progress-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10+-yellow)

---

## The Problem

In Central Asia, millions of people live with undiagnosed or poorly managed neurological conditions. Specialist access is critically limited. Alzheimer's is caught too late. Autism goes unscreened in children. Assistive tools exist only in English and Western contexts.

**NeuroReach is being built to change that.**

---

## Modules

| Module | Description | Status |
|---|---|---|
| 🔵 Alzheimer's Early Detection | ViT-based MRI classifier with cross-domain adaptation | ✅ Complete |
| 🟣 Autism Spectrum Screening | Q-CHAT-10 behavioral screening with XGBoost + SHAP explainability | ✅ Complete |
| 🟢 Assistive Communication Tool | AI-powered communication for limited motor/speech | 📋 Planned |

---

## Module 1 Results — Alzheimer's Early Detection

### Datasets
- **Source domain:** OASIS (86,000 MRI images, 4 classes)
- **Target domain:** ADNI v2 (122 subjects, 22,960 DICOM files, 3 classes: CN / MCI / AD)

### Results

| Model | Test Domain | Accuracy | Notes |
|---|---|---|---|
| ResNet18 (CNN) | OASIS | 99.89% | Baseline |
| ViT-B/16 (3-class) | OASIS | 99.85% | Source model |
| ResNet18 zero-shot | ADNI | 30.37% | Domain gap |
| ViT + CORAL (unsupervised) | ADNI | 35.56% | No labels needed |
| ViT fine-tuned (27 subjects) | ADNI | 70.56% ± 4.77% | Few-shot |
| ViT + CORAL fine-tuned | ADNI | 64.02% ± 4.96% | DA + fine-tune |
| **ViT fine-tuned (122 subjects)** | **ADNI** | **86.11% ± 1.99%** | **Best model** |

### Key Findings
- Domain shift reduces accuracy from 99.85% to 30.37% without adaptation
- CORAL domain adaptation improves zero-shot performance: 30.37% → 35.56%
- Label space consistency + balanced sampling: 70.56% → 86.11%
- Best deployment model: ViT-B/16 fine-tuned on 122 labeled ADNI subjects

---

## Module 2 Results — Autism Spectrum Screening

### Dataset
- Q-CHAT-10 Toddler ASD Screening Dataset (Thabtah, 2018)
- 1,054 samples, 10 behavioral features, binary classification
- Language support: Uzbek (native Q-CHAT-10 question mapping)

### Results

| Model | Accuracy | F1 Score | ROC-AUC | CV Mean |
|---|---|---|---|---|
| **XGBoost** | **97.63%** | **98.27%** | **99.89%** | **95.61% ± 0.88%** |
| LightGBM | 97.16% | 97.93% | 99.75% | — |

### Key Findings
- Behavioral questions (A9, A7, A6, A5, A2) are the strongest ASD predictors
- Demographic features (sex, ethnicity, family history) contribute minimally
- SHAP explainability identifies which specific behaviors flagged each child
- Model is fair across sex and ethnicity groups
- Class imbalance handled via `scale_pos_weight` — no resampling needed
- First Uzbek-language ASD screening tool for Central Asian communities

---

## Tech Stack

- **Deep Learning:** PyTorch, timm (ViT), MONAI
- **Machine Learning:** XGBoost, LightGBM, SHAP (explainability)
- **NLP:** HuggingFace Transformers
- **Experiment Tracking:** Weights & Biases
- **Deployment:** FastAPI, HuggingFace Spaces, Vercel
- **Data:** ADNI, OASIS, Q-CHAT-10

---

## Project Structure

NeuroReach/

├── docs/papers/          # Literature notes

├── data/                 # Data access instructions (no raw data)

├── notebooks/            # Exploration and experiments

├── src/

│   ├── datasets/         # Data loading and preprocessing

│   ├── models/           # Model architectures

│   ├── training/         # Training loops and configs

│   ├── utils/            # Helper functions

│   └── uzbek_mapping.py  # Uzbek language mapping for ASD screening

└── experiments/          # W&B configs and results

---

## Author

**Mohina Rustamova** — Undergraduate Researcher, New Uzbekistan University
Research focus: Computer Vision, Domain Adaptation, Vision Transformers
Published: ICECCO 2026 (IEEE/Scopus)
