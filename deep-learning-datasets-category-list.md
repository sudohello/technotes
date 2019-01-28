---
Title: Listing Category Hierarchy, Annotation Tools for AI
Decription: Datasets and Data Creation for Training Machines
Author: Bhaskar Mangal
Date: 04th-Jan-2019
Last updated: 07th-Jan-2019
Tags: Listing Category Hierarchy, Annotation Tools for AI
---


**Table of Contents**
* TOC
{:toc}


## Listing Category Hierarchy, Annotation Tools for AI

1. **Documentation of Category Hierarchy for publically available Computer Vision Datasets for AI**
  * Document the object hierarchy (along with the id, categlory label etc) in an excel sheet for following types of datasets:
    * Common Objects
    * Self-Driving-Car
    * Scene understanding
2. **Documentation Of AI Annotation Tools**
3. **Category Challange**
  * Internal task to come up with the category labels from our own datasets
4. **Comparision And Mapping Of Category Hierarchy - Internal & External**

## References

* [Deep Learning Datasets And Creation](deep-learning-datasets-and-creation.md)
* [Self Driving Car Datasets Semantic Segmentation](https://blog.playment.io/self-driving-car-datasets-semantic-segmentation/)
* [Worlds Largest Driving Dataset](https://blog.getnexar.com/introducing-bdd100k-the-worlds-largest-driving-dataset-b4e157bf2632)
* [Semantic Segmentation Datasets List](https://github.com/mrgloom/awesome-semantic-segmentation#datasets)


## **Self-driving Car (Autonomy) vs Urban Scene Difference Criteria**
  
| Self-driving Car (Autonomy)                                 | Urban Scene                                           |
|:------------------------------------------------------------|:------------------------------------------------------|
| * Contains images only from the driver's perspective        | contains from walking, and non-road scene perspective |
| * Outdoor images only                                       | Outdoor images only                                   |
| * contains sequential camera frames                         | not a pre-condition                                   |
| * can be aumgented with other sequential camera sensor data | cannot be agumented with sequential sensor data       |



## **Datasets of Interest (DoI)**

### **Common Objects**
1. [MS COCO - things, stuff, panoptic](mscoco-dataset.md)
  * **[MS COCO](http://cocodataset.org/#home)**
  * [what-object-categories-labels-are-in-coco-dataset](https://tech.amikelive.com/node-718/what-object-categories-labels-are-in-coco-dataset/)

### **Self-Driving-Car Datasets Semantic Segmentation**
2. [ApolloScape](apolloscape-dataset.md)
  * **[ApolloScape](http://apolloscape.auto/index.html)**
3. [BDD](bdd-dataset.md)
  * **[BDD100K - Berkeley DeepDrive](https://bdd-data.berkeley.edu/)**
4. [IDD - Indian Driving Dataset](idd-dataset.md)
5. [KITTI](http://www.cvlibs.net/datasets/kitti/)
  * **[KITTI Dataset](http://www.cvlibs.net/datasets/kitti/)**

### **Scene understanding Datasets**
6. [Cityscape](cityscape-dataset.md)
  * **[CityScapes Dataset](https://www.cityscapes-dataset.com/)**
  * https://www.cityscapes-dataset.com/dataset-overview/
7. [MVD - Mapillary](mapillary-dataset.md)
  * **[Mapillary Vista Dataset: MVD](https://blog.mapillary.com/product/2017/05/03/mapillary-vistas-dataset.html)**
8. [ADE20K](ade20k-dataset.md)
  * **[ADE20K Dataset](http://groups.csail.mit.edu/vision/datasets/ADE20K/)**


## **Annotatino Service Provides for AI**
* [playment.io](https://playment.io/image-annotation/)


## Labelling Policy

Labeling Policy
Labeled foreground objects must never have holes, i.e. if there is some background visible ‘through’ some foreground object, it is considered to be part of the foreground. This also applies to regions that are highly mixed with two or more classes: they are labeled with the foreground class. Examples: tree leaves in front of house or sky (everything tree), transparent car windows (everything car).