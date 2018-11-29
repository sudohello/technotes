---
Title: ADE20K Dataset
Decription: ADE20K Dataset
Author: Bhaskar Mangal
Date: 29th-Nov-2018
Last updated: 29th-Nov-2018
Tags: ADE20K Dataset
---

**Table of Contents**
* TOC
{:toc}


## [ADE20K Dataset](http://groups.csail.mit.edu/vision/datasets/ADE20K) Overview
* http://groups.csail.mit.edu/vision/datasets/ADE20K/
* Scene parsing, or recognizing and segmenting objects
* ADE20K dataset, spanning diverse annotations of:
  * scenes
  * objects
  * parts of objects
  * in some cases even parts of parts
* 150 object
* stuff classes
* 25k images of the complex everyday scenes containing a variety of objects in their natural spatial context
* On average there are 19.5 instances and 10.5 object classes per image
* Cascade Segmentation Module is proposed
  *  to parse a scene into stuff, objects, and object parts in a cascade and improve over the baselines
* scene parsing networks can lead to applications such as:
  * image content removal
  *   scene synthesis
* constructed benchmarks for scene parsing and instance segmentation
* provided baseline performances
* evaluated the effect of **synchronized batch normalization**
  * found that a reasonably large batch size is crucial for the semantic segmentation performance
* Set: Training, Validation, Test, Consistency (annotations used for checking the annotation consistency)


## papers
* https://www.groundai.com/project/semantic-understanding-of-scenes-through-the-ade20k-dataset/