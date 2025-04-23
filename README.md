# U-Net Pathogen Segmentation on Petri Dishes

This project applies a U-Net–based deep learning model to segment and quantify pathogen growth on Petri dish images. The approach leverages transfer learning to achieve expert-level accuracy in detecting and measuring pathogen area, enabling fast and reproducible evaluation.

## 📄 Contents

- `Model.ipynb`: A complete Jupyter Notebook that walks through:
  - Dataset setup and preprocessing
  - U-Net model architecture and training loop
  - Inference and mask generation
  - Visualization of predictions vs ground truth
  - Statistical evaluation of model performance
  - Final writeup and walkthrough of code

## 📊 Key Findings

- The model explains over 82% of the variance in manual measurements (R² = 0.828)
- Achieves a low mean absolute error (MAE = 2.89%)
- Strong inverse correlation with manual measurement effort (r = -0.91)
