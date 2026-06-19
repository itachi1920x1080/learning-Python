# Day 16: Deep Learning Fundamentals

This directory contains exercises for Day 16, focusing on introductory deep learning concepts using both PyTorch and TensorFlow/Keras.

## Files Included

- **`day6_ex.py`**: 
  - Demonstrates how to use PyTorch to load and preprocess the MNIST dataset.
  - Utilizes `torchvision.datasets` and `torchvision.transforms` for data transformation and `torch.utils.data.DataLoader` for batching the data.

- **`day7_ex.py`**:
  - Implements Convolutional Neural Networks (CNNs) using TensorFlow and Keras.
  - Trains two different CNN architectures (a baseline model and an improved model with Dropout layers) on the CIFAR-10 dataset for image classification.
  - Evaluates the models using categorical cross-entropy and accuracy metrics.

## How to Run

To run the PyTorch dataset preparation exercise:
```bash
python day6_ex.py
```

To run the TensorFlow CNN training script:
```bash
python day7_ex.py
```
