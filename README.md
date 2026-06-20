# 🧠 NeuroReach

> AI-powered early screening and assistive support for Alzheimer's disease, 
> Autism Spectrum Disorder, and neurological disabilities — built for 
> underserved communities in Central Asia.

![Status](https://img.shields.io/badge/Status-In%20Progress-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Python](https://img.shields.io/badge/Python-3.10+-blue)

---

## The Problem

In Central Asia, millions of people live with undiagnosed or poorly managed 
neurological conditions. Specialist access is critically limited. 
Alzheimer's is caught too late. Autism goes unscreened in children. 
Assistive tools exist only in English and Western contexts.

NeuroReach is being built to change that.

---

## Modules

| Module | Description | Status |
|--------|-------------|--------|
| 🔵 Alzheimer's Early Detection | ViT-based MRI classifier + cognitive assessment | 🚧 In Progress |
| 🟣 Autism Spectrum Screening | Behavioral + facial expression analysis | 📋 Planned |
| 🟢 Assistive Communication Tool | AI-powered communication for limited motor/speech | 📋 Planned |

---

## Tech Stack

- **Deep Learning:** PyTorch, timm (ViT), MONAI
- **NLP:** HuggingFace Transformers
- **Experiment Tracking:** Weights & Biases
- **Deployment:** FastAPI, HuggingFace Spaces, Docker
- **Data:** ADNI, OASIS, ABIDE

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
