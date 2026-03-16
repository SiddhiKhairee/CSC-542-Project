# Bird Species Classification using Deep Learning

A computer vision project that classifies bird images into **20 bird species** using deep learning.
The project implements both a **custom Convolutional Neural Network (CNN)** and **transfer learning with ResNet18** to compare performance on an image classification task.

---

# Project Overview

This project builds an end-to-end image classification pipeline that:

* Loads and processes bird image datasets
* Applies data augmentation for better generalization
* Trains deep neural networks for classification
* Evaluates performance on a held-out test set

Two different model approaches are explored:

1. **Custom CNN architecture**
2. **Transfer Learning using pretrained ResNet18**

Transfer learning allows the model to leverage features learned from large datasets like ImageNet to improve classification accuracy.

---

# Dataset

The dataset contains bird images along with metadata files that describe image paths, labels, and train/test splits.
This project uses the **Caltech-UCSD Birds dataset (CUB-200)**.

You can download the dataset here:

Dataset link:
https://www.kaggle.com/datasets/veeralakrishna/200-bird-species-with-11788-images

After downloading, extract it and place it in the following structure:

Dataset structure:

```
dataset/
│
├── images20/
│   ├── class_1/
│   ├── class_2/
│   ├── class_3/
│   └── ...
│
├── images.txt
├── image_class_labels.txt
└── train_test_split.txt
```

### Dataset Metadata Files

| File                     | Description                                                |
| ------------------------ | ---------------------------------------------------------- |
| `images.txt`             | Maps image IDs to image file paths                         |
| `image_class_labels.txt` | Maps image IDs to bird species labels                      |
| `train_test_split.txt`   | Indicates whether an image belongs to training or test set |

The project trains models on **20 bird species classes**.

---

# Model Architectures

## 1. Custom CNN

The custom convolutional network includes several convolution blocks followed by fully connected layers.

Architecture:

```
Conv2D
BatchNorm
ReLU
MaxPool

Conv2D
BatchNorm
ReLU
MaxPool

Conv2D
BatchNorm
ReLU
MaxPool

Flatten
Fully Connected Layer
Dropout
Output Layer (20 classes)
```

---

## 2. Transfer Learning (ResNet18)

A pretrained **ResNet18 model** is used as the feature extractor.

The final classification layer is replaced with a custom classifier for the bird dataset.

Architecture:

```
Pretrained ResNet18 Backbone
↓
Fully Connected Layer
↓
ReLU Activation
↓
Dropout
↓
Output Layer (20 classes)
```

---

# Data Augmentation

To improve model generalization, the following augmentations are applied to training images:

* Image resizing
* Random cropping
* Random horizontal flipping
* Image normalization

Testing images use deterministic preprocessing:

* Resize
* Center crop
* Normalization

---

# Training Configuration

| Parameter     | Value                   |
| ------------- | ----------------------- |
| Batch Size    | 32                      |
| Optimizer     | AdamW                   |
| Learning Rate | 0.001                   |
| Loss Function | CrossEntropyLoss        |
| Epochs        | 10                      |
| Device        | GPU (CUDA if available) |

---

# Project Structure

```
bird-classification/
│
├── KYS.ipynb
├── baseline.ipynb
├── README.md
├── dataset_formatter.py
├── txt_split_formatter.py
│
└── dataset/
    ├── images20/
    ├── images.txt
    ├── image_class_labels.txt
    └── train_test_split.txt
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/bird-classification.git
cd bird-classification
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

Update the dataset path inside the notebook:

```python
DATA_ROOT = "path_to_dataset"
```

Then open and run the notebook:

```
KYS.ipynb
```

The notebook will:

1. Load the dataset
2. Apply preprocessing and augmentations
3. Train the CNN and ResNet models
4. Evaluate performance on the test set

---

# Example Training Output

```
Epoch 1: Loss 1.89, Train Accuracy 45.2%
Epoch 5: Loss 0.83, Train Accuracy 74.5%
Epoch 10: Loss 0.42, Train Accuracy 88.1%

Test Accuracy: 84.3%
```

---

# Technologies Used

* Python
* PyTorch
* Torchvision
* NumPy
* Matplotlib
* PIL

---

# Future Improvements

Possible extensions for this project:

* Train on the full bird species dataset
* Experiment with deeper architectures (ResNet50, EfficientNet)
* Add model checkpointing and early stopping
* Build an inference pipeline for new images
* Deploy the model using Flask or FastAPI

---

# Author

Computer Vision project developed to explore deep learning techniques for image classification and transfer learning.
