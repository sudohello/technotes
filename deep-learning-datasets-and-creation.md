---
Title: Datasets and Data Creation for Training Machines
Decription: Datasets and Data Creation for Training Machines
Author: Bhaskar Mangal
Date: 24th-Jul-2018
Last updated: 22nd-Oct-2018
Tags: Datasets and Data Creation for Training Machines
---

**Table of Contents**
* TOC
{:toc}


## Datasets and Data Creation for Training Machines


## Creation for Training Machines


## Image Labeling Tools
* https://github.com/ox-vgg/via - simple, intutive, best
  - http://www.robots.ox.ac.uk/~vgg/blog/author/abhishek-dutta.html
  - http://www.robots.ox.ac.uk/~vgg/software/via/
  - http://www.robots.ox.ac.uk/~vgg/software/via/via-1.0.6.html
  - http://www.robots.ox.ac.uk/~vgg/blog/vgg-image-annotator.html
* https://en.wikipedia.org/wiki/List_of_manual_image_annotation_tools
* https://www.researchgate.net/post/Can_anyone_suggest_an_image_labeling_tool_for_object_detection
* https://github.com/tzutalin/labelImg
  - `git clone https://github.com/tzutalin/labelImg.git`
* http://sloth.readthedocs.io/en/latest/
* https://github.com/yuyu2172/image-labelling-tool
* https://blog.playment.io/training-data-for-computer-vision/
* https://alpslabel.wordpress.com/
* https://github.com/commaai/commacoloring
* https://www.quora.com/What-is-the-best-image-labeling-tool-for-object-detection
* https://github.com/Labelbox/Labelbox/blob/master/LICENSE
* https://oclavi.com/
* https://playment.io/image-annotation/
* https://blog.playment.io/training-data-for-computer-vision/
* https://github.com/davisking/dlib/tree/master/tools/imglab
```bash
git clone https://github.com/davisking/dlib.git
cmake -DCMAKE_C_COMPILER=/usr/bin/gcc-6 -DCMAKE_CXX_COMPILER=/usr/bin/g++-6 ..
```
* Amazon Mechanical Turk
  - https://www.mturk.com/
  Amazon Mechanical Turk (MTurk) operates a marketplace for work that requires human intelligence. The MTurk web service enables companies to programmatically access this marketplace and a diverse, on-demand workforce. Developers can leverage this service to build human intelligence directly into their applications.

  While computing technology continues to improve, there are still many things that human beings can do much more effectively than computers, such as identifying objects in a photo or video, performing data de-duplication, transcribing audio recordings or researching data details. Traditionally, tasks like this have been accomplished by hiring a large temporary workforce (which is time consuming, expensive and difficult to scale) or have gone undone.

  MTurk aims to make accessing human intelligence simple, scalable, and cost-effective. Businesses or developers needing tasks done (called Human Intelligence Tasks or “HITs”) can use the robust MTurk API to access thousands of high quality, global, on-demand Workers—and then programmatically integrate the results of that work directly into their business processes and systems. MTurk enables developers and businesses to achieve their goals more quickly and at a lower cost than was previously possible.
* VoTT - https://github.com/Microsoft/VoTT/blob/master/README.md

## Labelling
- https://github.com/udacity/self-driving-car
- http://aid-driving.eu/active-learning-and-labeling/
- add situation-specific label
  *  for each image if it was day, rainy, if there were roadworks, close traffic participants (or far away), and many more things.
  * Image Properties
    - Roadworkds:
    - Cloudy
    - Traffic participants close
    - Traffic participants far
    - City
    - Rainy
    - Day
  * Transfer learning is the practice of taking an existing neural network trained on a specific task and retraining this neural network on another task. 
  * By using transfer learning we profit from existing lower level filters. By training on all classes at the same time the gradients from other classes influence the upper layers!

## Dataset Management
- https://autonomous-driving.org/2018/06/16/dataset-management-for-machine-learning/

## Dataset / Data source / Datasource for ML / Deep Learning / Computer Vision Datasets
**Extensive List of Datasets**
- https://projet.liris.cnrs.fr/voir/wiki/doku.php?id=datasets
- https://handong1587.github.io/computer_vision/2015/09/24/datasets.html

* **[CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html)**
  - One popular toy image classification dataset is the CIFAR-10 dataset. This dataset consists of 60,000 tiny images that are 32 pixels high and wide. Each image is labeled with one of 10 classes (for example “airplane, automobile, bird, etc”). These 60,000 images are partitioned into a training set of 50,000 images and a test set of 10,000 images.
  - https://www.cs.toronto.edu/~kriz/cifar.html
* **Pima Indians**
* **Ionosphere**
  - http://cv-tricks.com/tensorflow-tutorial/understanding-alexnet-resnet-squeezenetand-running-on-tensorflow/
* Image segmentations
  - https://aws.amazon.com/public-datasets/spacenet/
  - http://www.cvlibs.net/datasets/kitti/eval_road.php
* Viva
  - http://cvrr.ucsd.edu/vivachallenge/index.php/signs/sign-detection/
* LISA
  - http://cvrr.ucsd.edu/LISA/lisa-traffic-sign-dataset.html
  - https://www.codemade.io/lisa-traffic-sign-dataset/
* COCO
  - http://cocodataset.org/#home
  - COCO is a large-scale object detection, segmentation, and captioning dataset
* PASCAL VOC
  - http://host.robots.ox.ac.uk/pascal/VOC/
  ```bash
  wget -c http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtrainval_06-Nov-2007.tar
  wget -c http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtest_06-Nov-2007.tar
  wget -c http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar
  ```
*  MNIST, then notMNIST, another famous one is cifar-10, cifar-100, and for driverless cars, we have GTSRB (Traffic sign recognition), GTSDB (Traffic sign detection) 
* **Inria**
  - A large set of marked up images of standing or walking people
  - http://pascal.inrialpes.fr/data/human/
  ```bash
  wget -c ftp://ftp.inrialpes.fr/pub/lear/douze/data/INRIAPerson.tar
  ```
* http://course.fast.ai/datasets

**Caltech-UCSD Birds-200-2011**
* http://www.vision.caltech.edu/visipedia/CUB-200-2011.html
* Warning: Images in this dataset overlap with images in ImageNet. Exercise caution when using networks pretrained with ImageNet (or any network pretrained with images from Flickr) as the test set of CUB may overlap with the training set of the original network.


## AI datasets Search Engines
* http://classif.ai/

### Traffic Sign Datasets
* **German**
  - http://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset
* **LISA: Laboratory for Intelligent Safe Automobiles**
  - http://cvrr.ucsd.edu/LISA/lisa-traffic-sign-dataset.html
* **Belgium**
  - https://btsd.ethz.ch/shareddata/
  - The images in this dataset are in an old .ppm format
  - Images are square-ish, but have different aspect ratios
  - The image quality is great, and there are a variety of angles and lighting conditions
  - The traffic signs occupy most of the area of each image, which allows to focus on object classification and not have to worry about finding the location of the traffic sign in the image (object detection).
  - Generally, neural network will take a fixed-size input, so some preprocessing is required.
  - Dataset considers all speed limit signs to be of the same class, regardless of the numbers on them. That’s fine, as long as we know about it beforehand and know what to expect.
  - Labels 26 and 27 are interesting to check
  - What are the sizes of the images? - The sizes seem to hover around 128x128.
  - This tells me that the image colors are the standard range of 0–255.
  * **Additional Notes**
    - There is one directory for each of the 62 classes (00000 - 00061)
    - Each directory contains the corresponding training images and one  text file with annotations, eg. GT-00000.csv [headers: Filename;Width;Height;Roi.X1;Roi.Y1;Roi.X2;Roi.Y2;ClassId]
    - In total are 4591 images for training.
    - On average for each physically distinct traffic sign there are 3 images available.
    - The images are PPM images (RGB color)
    - Names are:
      - XXXXX_YYYYY.ppm, XXXXX - pole number
      - running number for the views where the traffic sign is annotated. There is no temporal order of the images

### **Self Driving Car Datasets Semantic Segmentation**
- https://blog.playment.io/self-driving-car-datasets-semantic-segmentation/
* [CamVid](http://mi.eng.cam.ac.uk/research/projects/VideoRec/CamVid/)
  - http://mi.eng.cam.ac.uk/research/projects/VideoRec/CamVid/
* [KITTI - Karlsruhe Institute of Technology and Toyota Technological Institute](http://www.cvlibs.net/datasets/kitti/)
  - http://www.cvlibs.net/datasets/kitti/
  - http://www.cvlibs.net/datasets/kitti/eval_road.php
* [DUS - Daimler Urban Segmentation](http://www.6d-vision.com/scene-labeling)
  - http://www.6d-vision.com/scene-labeling
  - http://www.6d-vision.com/home
* [CityScapes](https://www.cityscapes-dataset.com/)
  - https://www.cityscapes-dataset.com/
  - https://www.cityscapes-dataset.com/benchmarks/
* [Mapillary Vista](https://blog.mapillary.com/product/2017/05/03/mapillary-vistas-dataset.html)
  - https://blog.mapillary.com/product/2017/05/03/mapillary-vistas-dataset.html
  - https://www.mapillary.com/dataset/vistas
* [Synthia](http://synthia-dataset.com/download-2/)
  - http://synthia-dataset.net/ 
* [Udacity](https://github.com/udacity/self-driving-car/tree/master/datasets)
  - https://github.com/udacity/self-driving-car/tree/master/datasets


### 3D Datasets
- https://hackernoon.com/announcing-the-matterport3d-research-dataset-815cae932939
- https://niessner.github.io/Matterport/
- https://arxiv.org/pdf/1709.06158.pdf

### Others
- https://en.wikipedia.org/wiki/List_of_datasets_for_machine_learning_research
* Free datasets are available from places like Kaggle.com and UCI. 
  - https://www.kaggle.com/datasets
  - https://archive.ics.uci.edu/ml/datasets.html

## Datasets Detailed Review

1. [Cityscape](cityscape-dataset.md)
2. [Mapillary](mapillary-dataset.md)

## Dataset Pre-processing
* http://shubhagrawal.in/2016/10/13/machine-learning-data-preprocessing/

# TBD
* https://www.kaggle.com/learn/machine-learning
* https://github.com/CPFL/Autoware
* https://maptools.tier4.jp/
* http://www.aisantec.co.jp/english/
* http://shubhagrawal.in/2016/08/01/creating-launcher-for-any-executable-file-linux/
* http://home.bharathh.info/
