# 🧠 NeuroReach

AI-powered early screening and assistive support for Alzheimer's disease, Autism Spectrum Disorder, and neurological disabilities — built for underserved communities in Central Asia.

[![Status](https://img.shields.io/badge/Status-In%20Progress-blue)](https://github.com/MohinaRustamova/NeuroReach)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://python.org)

---

## The Problem

In Central Asia, millions of people live with undiagnosed or poorly managed neurological conditions. Specialist access is critically limited. Alzheimer's is caught too late. Autism goes unscreened in children. Assistive tools exist only in English and Western contexts.

NeuroReach is being built to change that.

---

## Modules

| Module | Description | Status |
|--------|-------------|--------|
| 🔵 Alzheimer's Early Detection | ViT-based MRI classifier with cross-domain adaptation | ✅ Complete |
| 🟣 Autism Spectrum Screening | Behavioral + facial expression analysis | 📋 Planned |
| 🟢 Assistive Communication Tool | AI-powered communication for limited motor/speech | 📋 Planned |

---

## Module 1 Results — Alzheimer's Early Detection

### Datasets
- **Source domain**: OASIS (86,000 MRI images, 4 classes)
- **Target domain**: ADNI v2 (122 subjects, 22,960 DICOM files, 3 classes: CN / MCI / AD)

### Results

| Model | Test Domain | Accuracy | Notes |
|-------|------------|----------|-------|
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

## Tech Stack

- **Deep Learning**: PyTorch, timm (ViT), MONAI
- **NLP**: HuggingFace Transformers
- **Experiment Tracking**: Weights & Biases
- **Deployment**: FastAPI, HuggingFace Spaces, Docker
- **Data**: ADNI, OASIS, ABIDE

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

│   └── utils/            # Helper functions

└── experiments/          # W&B configs and results

---

## Author

**Mohina Rustamova** — Undergraduate Researcher, New Uzbekistan University
Research focus: Computer Vision, Domain Adaptation, Vision Transformers
Published: ICECCO 2026 (IEEE/Scopus)
