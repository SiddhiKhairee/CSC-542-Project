# Bird Species Classification using Deep Learning

A computer vision project that classifies bird images into 20 species using deep learning.  
The project uses **PyTorch**, **CNN architectures**, and **transfer learning with ResNet18** to train an image classifier on a subset of a bird dataset.

---

## Project Overview

This project builds an image classification pipeline that:

1. Loads bird image data using custom dataset loaders
2. Applies data augmentation and normalization
3. Trains deep neural networks for classification
4. Evaluates performance on a held-out test set

Two model approaches are implemented:

- **Custom CNN architecture**
- **Transfer Learning using pretrained ResNet18**

Transfer learning significantly improves performance by leveraging pretrained ImageNet features.

---

## Dataset

The dataset contains bird images with metadata files used for loading and splitting the data.

Required dataset files:

