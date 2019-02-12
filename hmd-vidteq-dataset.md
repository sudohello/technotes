---
Title: HDD Dataset
Decription: HDD Dataset
Author: Bhaskar Mangal
Date: 18th-Jan-2019
Last updated: 18th-Jan-2019
Tags: HDD Dataset
---

**Table of Contents**
* TOC
{:toc}


## High-Definition Map Dataset - (HMD)
* Selection of categories specific from HD Map perspective
* Images of clipped, segmented objects used as datalayers in Map creation pipeline
* Possibility of correlating and combining the clipped/segmented images w.r.t. point cloud of the same place
* objective of able to **perform cloaking**:
  * during prediction removal of moving objects
  * reconstruction of occluded static scene and sttic objects from the previous and next image frames
* Synthetic image generation from 3D modeling and augmentation for specific object categories during training
* Simple and complex Image augmentation w.r.t. no-augmentation comparissions
* Cross-training with other public datasets
  * mix subsets of new categories in available public datasets
  * mix public datasets 
* Quatification Strategies, Process & Matrices
* Conclusion


### A. Perspective
1. self-driving car perspective
2. High Definition Map perspective
3. Unknown

### B. Objective
High diversity in:-
+ **Computer vision objectives for Annotations**
  * classification
  * object detection
  * semantic segmentation
  * instance semantic segmentation
  * Lane
+ **Object Attributions**
  * Occulsions
  * Truncations
  * Color
+ **Image Tagging**
  * geographic
  * environmental
    * scene type
    * time of day
  * weather conditions
  * quality of image
+ **2D Geometries for Annotations**
  *  Point
  *  Line
  *  BBox (Rectangle)
  *  Polygon
  *  circle, ellipse
  *  Bezier curves
+ **3D Geometries for Annotations**
  * Cuboid
+ **Annotation Data**
  * Images
    - Frame sequences
    - Aerial
    - Territorial
  * Videos
  * Point Cloud

### C. Quantification
+ **Annotator and Annotation Process**
  + Quality of Annotation
  + People, Time and cost
+ **Dataset**
  + based on perspective and objective
  + w.r.t. Per Image
    * number of annotations
    * categories
    * type of annotation
    * avg. number of pixels, size, aspect ratio
    * histogram stats - highlights, midtones, shadows
    * blurryness, sharpness, contrast, saturation, hue
  + w.r.t. Total pixels
  + w.r.t. per categories
    * total number of images
    * % of images
    * attributions


### D. Dataset splits

+ different mix
+ compare different mix w.r.t. same training and architecture


### E. Comparission with Benchmarks

+ w.r.t. more similar datasets
+ w.r.t. less similar datasets
+ training results of same architecture on the more or less similar datasets


## Category Selection