# YOLOv3-An-Incremental-Improvement


This repo contains from-scratch implementation for YOLOv3 Object Detection model defined in [paper](https://pjreddie.com/media/files/papers/YOLOv3.pdf).

The project can be described in the underlying steps:
- Reading the paper and understanding how the model operates: including understanding concepts like bounding box prediction, Anchor boxes, and intersection over union metrics.
- Building Yolov3 model using pytorch.
- Building dataset class and performing data augmentation on the [The PASCAL Visual Object Classes](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/index.html#devkit) using Albumentations lib.
- Recreate Yolov3 Loss function.
- Perform non-max suppression to improve the output of the model.
- Train the model on the [PASCAL-VOC dataset](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/index.html#devkit).
- Evaluate our trained model and the model with predefined weights using mean average precision metric.

Skills developed: pandas | pytorch | Neural Networks | Quality metrics | Data Preparation | Model Evaluation | Data modeling | python.

This project was an exam project done by [Anwar Ibrahim](https://github.com/Anwar9Ibrahim) and Fares Ghazzawi for the MLDM course, HSE, Russian Federation (2022-2023).

