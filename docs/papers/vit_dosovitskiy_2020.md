[first_paper.pdf](https://github.com/user-attachments/files/29213764/first_paper.pdf)

# An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale
**Authors:** Dosovitskiy et al. (Google Brain)  
**Venue:** ICLR 2021  
**Link:** https://arxiv.org/abs/2010.11929  

## What They Did
Proposed Vision Transformer (ViT) — a pure Transformer applied directly to 
images with no convolutional layers. Images are split into fixed-size 16×16 
patches, each patch is flattened and linearly projected into an embedding, 
and the resulting sequence is fed into a standard Transformer encoder. A 
learnable CLS token is prepended to the sequence, and its final state is used 
for classification via an MLP head. Position embeddings are added to preserve 
spatial order. The model is pretrained on large datasets (ImageNet-21k, 
JFT-300M) and fine-tuned on downstream tasks.

## Key Method
- **Patch tokenization:** 224×224 image → 196 patches of size 16×16
- **Linear projection:** each patch mapped to embedding dimension D=768
- **CLS token:** learnable token prepended to sequence; its output = image representation
- **Position embeddings:** 1D learnable embeddings added to preserve spatial order
- **Transformer encoder:** L=12 layers of Multi-Head Self-Attention + MLP + LayerNorm + residual connections
- **Fine-tuning:** pretrained head removed, zero-initialized linear layer with K outputs attached
- **ViT-B/16 config:** 12 layers, 768 hidden dim, 12 heads, 86M parameters

## Results
- ViT-H/14 achieves 88.55% on ImageNet — beats ResNet152 (87.54%) with 4x less compute
- On medical imaging (Retinopathy): 76.6% — promising but not brain MRI
- On small datasets (ImageNet only): ViT underperforms ResNet due to lack of inductive bias
- Requires 14M–300M images for pretraining to surpass CNNs
- Scales better than ResNet — no performance saturation observed

## Attention Map Insights
- Lower layers: some heads attend locally, others globally simultaneously
- Deeper layers: most heads attend across the entire image
- Model attends to semantically relevant regions automatically (Figure 6)
- Attention distance analogous to receptive field size in CNNs but global from early layers

## What I Take From It
Pretrained ViT-B/16 (ImageNet-21k weights) is the right choice for fine-tuning 
on OASIS MRI dataset. Self-attention captures long-range dependencies across 
distributed brain regions — more suited for Alzheimer's detection than local 
CNN filters which build receptive fields slowly. Attention maps provide built-in 
explainability showing which brain regions the model flags — clinically valuable 
for neurologists. Fine-tuning hyperparameters from Appendix B (lr=0.001–0.03, 
cosine decay, batch size 512) serve as starting point for notebook 04.

## Gaps Identified
- No experiments on brain MRI or neurological imaging
- No evaluation under domain shift (different MRI scanners/hospitals)
- No discussion of class imbalance in medical datasets
- Attention maps shown qualitatively only — no clinical validation
- All datasets are natural images — medical imaging behavior not characterized

## Relevance to NeuroReach Module 1
These gaps are exactly what NeuroReach addresses: ViT fine-tuned on OASIS 
brain MRI with class imbalance handling, followed by CORAL domain adaptation 
across ADNI scanner domains, with attention map visualization for clinical 
explainability.
