---
Title: Ms COCO Dataset Overview
Decription: Ms COCO Dataset Overview
Author: Bhaskar Mangal
Date:
Last updated: 27th-Nov-2018
Tags: Ms COCO Dataset Overview
---

**Table of Contents**
* TOC
{:toc}


## Ms COCO Dataset Overview

http://cocodataset.org/#home
COCO is a large-scale object detection, segmentation, and captioning dataset. COCO has several features:

Object segmentation
Recognition in context
Superpixel stuff segmentation
330K images (>200K labeled)
1.5 million object instances
80 object categories
91 stuff categories
5 captions per image
250,000 people with keypoints

https://github.com/aleju/imgaug (pip3 install imgaug)

Download and install the Python COCO tools from https://github.com/waleedka/coco
That's a fork from the original https://github.com/pdollar/coco with a bug
fix for Python 3.
I submitted a pull request https://github.com/cocodataset/cocoapi/pull/50
If the PR is merged then use the original repo.
Note: Edit PythonAPI/Makefile and replace "python" with "python3".


## **Create you Own COCO type annotation dataset**
* https://www.programcreek.com/python/example/94653/pycocotools.coco.COCO
* https://patrickwasp.com/create-your-own-coco-style-dataset/