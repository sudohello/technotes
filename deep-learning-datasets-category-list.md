---
Title: Listing Category Hierarchy for Computer Vision Datasets for AI
Decription: Datasets and Data Creation for Training Machines
Author: Bhaskar Mangal
Date: 04th-Jan-2019
Last updated: 07th-Jan-2019
Tags: Listing Category Hierarchy for Computer Vision Datasets for AI
---


**Table of Contents**
* TOC
{:toc}


# Listing Category Hierarchy for Computer Vision Datasets for AI

## **Task:**

* Document the object hierarchy (along with the id, categlory label etc) in an excel sheet for following types of datasets:
  * Common Objects
  * Self-Driving-Car
  * Scene understanding
* Note: individual worksheet/excel sheet per dataset
* List of different datasets are given below


**Common Objects**
* **[MS COCO](http://cocodataset.org/#home)**
* [what-object-categories-labels-are-in-coco-dataset](https://tech.amikelive.com/node-718/what-object-categories-labels-are-in-coco-dataset/)


**Self-Driving-Car Datasets Semantic Segmentation**
* **[CityScapes Dataset](https://www.cityscapes-dataset.com/)**
* **[Mapillary Vista Dataset: MVD](https://blog.mapillary.com/product/2017/05/03/mapillary-vistas-dataset.html)**
* **[ApolloScape](http://apolloscape.auto/index.html)**
* **[BDD100K - Berkeley DeepDrive](https://bdd-data.berkeley.edu/)**
* **[KITTI Dataset](http://www.cvlibs.net/datasets/kitti/)**

**Scene understanding Datasets**
* **[ADE20K Dataset](http://groups.csail.mit.edu/vision/datasets/ADE20K/)**


## References

- [self-driving-car-datasets-semantic-segmentation](https://blog.playment.io/self-driving-car-datasets-semantic-segmentation/)
- [the-worlds-largest-driving-dataset](https://blog.getnexar.com/introducing-bdd100k-the-worlds-largest-driving-dataset-b4e157bf2632)
- [semantic-segmentation datasets list](https://github.com/mrgloom/awesome-semantic-segmentation#datasets)



**Datasets Detailed Review / Overview**
1. [Cityscape](cityscape-dataset.md)
  * https://www.cityscapes-dataset.com/dataset-overview/
2. [Mapillary](mapillary-dataset.md)
3. [ApolloScape](apolloscape-dataset.md)
4. [MS COCO](mscoco-dataset.md)
5. [ade20k](ade20k-dataset.md)


## **Annotatino Service Provides for AI**
* [playment.io](https://playment.io/image-annotation/)


## Labelling Policy

Labeling Policy
Labeled foreground objects must never have holes, i.e. if there is some background visible ‘through’ some foreground object, it is considered to be part of the foreground. This also applies to regions that are highly mixed with two or more classes: they are labeled with the foreground class. Examples: tree leaves in front of house or sky (everything tree), transparent car windows (everything car).