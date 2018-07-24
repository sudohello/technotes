/*
Title: Datasets and Data Creation for Training Machines
Decription: Datasets and Data Creation for Training Machines
Author: Bhaskar Mangal
Date: 24th-Jul-2018
Last updated: 24th-Jul-2018
Tags: Datasets and Data Creation for Training Machines
*/

**Table of Contents**

[TOC]

# Datasets and Data Creation for Training Machines


## Creation for Training Machines

### Image Labeling Tools
* https://en.wikipedia.org/wiki/List_of_manual_image_annotation_tools
* https://www.researchgate.net/post/Can_anyone_suggest_an_image_labeling_tool_for_object_detection
* https://github.com/tzutalin/labelImg
* http://sloth.readthedocs.io/en/latest/
* https://github.com/yuyu2172/image-labelling-tool
* https://blog.playment.io/training-data-for-computer-vision/
* https://alpslabel.wordpress.com/
* https://github.com/commaai/commacoloring
* https://www.quora.com/What-is-the-best-image-labeling-tool-for-object-detection
* https://github.com/Labelbox/Labelbox/blob/master/LICENSE
* `git clone https://github.com/tzutalin/labelImg.git`
* https://oclavi.com/

## Dataset / Data source / Datasource for ML / Deep Learning / Computer Vision Datasets
- https://projet.liris.cnrs.fr/voir/wiki/doku.php?id=datasets
- https://handong1587.github.io/computer_vision/2015/09/24/datasets.html
* **CIFAR-10**
  - One popular toy image classification dataset is the CIFAR-10 dataset. This dataset consists of 60,000 tiny images that are 32 pixels high and wide. Each image is labeled with one of 10 classes (for example “airplane, automobile, bird, etc”). These 60,000 images are partitioned into a training set of 50,000 images and a test set of 10,000 images.
  - http://www.cs.toronto.edu/~kriz/cifar.html
* **Pima Indians**
* **Ionosphere**
  - http://cv-tricks.com/tensorflow-tutorial/understanding-alexnet-resnet-squeezenetand-running-on-tensorflow/
* Image segmentations
  - https://aws.amazon.com/public-datasets/spacenet/
  - http://www.cvlibs.net/datasets/kitti/eval_road.php

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

### Others
- https://en.wikipedia.org/wiki/List_of_datasets_for_machine_learning_research
* Free datasets are available from places like Kaggle.com and UCI. 
  - https://www.kaggle.com/datasets
  - https://archive.ics.uci.edu/ml/datasets.html

## Datasets Detailed Review

### Mapillary
https://github.com/Oslandia/deeposlandia
https://www.mapillary.com/dataset/vistas?pKey=q0GhQpk20wJm1ba1mfwJmw
https://github.com/mapillary/mapillary_vistas/tree/master/mapillary_vistas
https://research.mapillary.com/img/publications/ICCV17a.pdf

#### Research Paper reviews
**Visual scene understanding**
* Reference: The Mapillary Vistas Dataset for Semantic Understanding of Street Scenes, Gerhard Neuhold, Tobias Ollmann, Samuel Rota Bulò, Peter Kontschieder, Mapillary Research, research@mapillary.com
* Scene recognition puts the emphasis on providing a global description of a scene, typically summarized at a single scene category level
* Object detection focuses on finding object instances and their categories within a scene, typically localized using bounding-boxes
* Semantic segmentation emphasizes on providing a finer-grained prediction of the semantic category each pixels belongs to
* Instance-specific semantic segmentation adds the difficulty of identifying the pixels that compose each object instance, thus integrating semantic segmentation with fine-grained object detection

**Challanges & Opportunities**
- Visual scene understanding belongs to the most fundamental and challenging goals in computer vision
- Top-performing algorithms for visual scene understanding are nowadays developed using deep learning
- Training of deep learning models requires a substantial amount of (annotated) data and computational resources
- Availability of large-scale datasets such as ImageNet [48], Places [63], PASCAL VOC [10], PASCAL-Context [39], Microsoft COCO [30], ADE20K [65] and YouTube-8M [1] is of major importance for both, the scientific and industrial communities
- Integrating synthetically-rendered data from sources like the Grand Theft Auto V engine [45], Synthia [46] or semantic instance labeling via 3D to 2D label transfer [56]
- To gain deeper understanding of the complex interactions between e.g. traffic participants in street-level images, a lot of research efforts and investments have recently gone into designing and creating datasets which were used to train deep models for this specific task, such as CamVid [3], the KITTI Vision Benchmark Suite [12], Leuven [23], Daimler Urban Segmentation [49] and Cityscapes [6]

**Characterstics of such datasets:**
- Total number of fine-grained annotated images
- The overall number of object categories, are restricted to specific capturing areas, or urban scenes, thus strongly biasing the appearance of the elements to be analysed.
- In addition, such datasets may suffer from a bias towards specific capturing modalities due to the usage of a sole imaging sensor and therefore not properly covering the spectrum of available sensor noise or overly strict specifications on camera mounting.

**Mapillary datasets**
- new dataset for semantic segmentation of urban, countryside and off-road scenes comprising
- The proposed dataset is designed to capture the broad range of outdoor scenes available around the world
- 25 000 densely-annotated street level images into 66 object categories
- featuring locations from all around the world
- taken from a diverse source of image capturing devices
- Images are annoted in a fine-grained style by using polygons for annotation and contain instance-specific object annotations for 37 object categories
- dataset is 5× larger than Cityscapes (in terms of fine-grained annotations)
- exhibits a significantly larger variability in terms of geographic origins and number of object categories
- visually covers parts of Europe, North and South America, Asia, Africa and Oceania, consequently addressing the global spectrum of possible object appearances
- a statistical protocol for quality assurance (QA), such that targeted annotation accuracies for precision and recall can be monitored and verified
- The dataset is also available as commercial edition with annotations for 100 object classes (with instance-specific annotations for 58 classes), providing more detailed semantics for autonomous driving specific categories
- Raw images data is available for anyone to explore under a CC-BY-SA license agreement with repository of ≈140 million images
- Characterize our dataset according to the targeted distributions for geographical and seasonal distribution, weather conditions, viewing perspectives, capturing time, image resolution, i.e. the diversity of images taken in the wild.
- The dataset properties for the complete dataset in terms of training and validation data (18 000 + 2 000 images, respectively). The remaining 5 000 test images are sampled proportionally to the geographic training data distribution and their annotation characteristics remain undisclosed
- In order to accept an image for the semantic annotation process, several criteria have to be met:
  - First, the image resolution has to be at least full HD, i.e. a minimum width/height of 1920× 1080 was imposed
  - Additionally, ≈ 90% of the images should be selected from road/sidewalk views in urban areas and the remaining ones from highways, rural areas 3 and off-road
  - Images with strong wide-angle view (focal length below 10mm) or 360 ◦ images were removed
  - Degraded images exhibiting strong motion blur, rolling shutter artifacts, interlacing artifacts, major windshield reflections or containing dominant image parts from the capturing vehicle/device (like car hood, camera mount or wipers) were removed as well
  - a small amount of distortion for motion blur was accepted, as long as individual objects could still be recognized and precisely annotated
  - images can belong to a sequence (i.e. a series of images taken with either manual, pre-fixed or distance-depending capture rate), we restrict to selecting images with unique views on a scene to avoid redundant labeling of image content.

Categories.
- 66 visual object categories, mostly pertaining to a street-level scene domain
- The categories are organized into 7 root-level groups, namely:
  * object
  * construction
  * human
  * marking
  * nature
  * void
  * animal
- Each root-level group is organized into different macro-groups
- 69 professional annotators, annotation time is at around 94 minutes per image (include 15 mins of 1st QA)
- 5 annotator to 1 QA
- second QA process guided by a modified variant of the four-eyes principle
- categorization, process inspired by cityscape - annotating the images with object categories from back to front, i.e. annotation is typically started with sky (the most distant category to the camera center) and gradually works closer to the camera. In this way, a z-ordering for individual object layers can be imposed, allowing to rasterize the final label images.
- a second (and therefore different) annotation provider revisits selected images and is incentivized to spot errors measured by the weighted intersection over union criterion as typically used to assess the performance for instance-specific semantic segmentation

* https://github.com/mapillary/mapillary_tools
The criteria to add categories to the annotation process were driven by several factors. Inspired by earlier works like Cityscapes [6] and SIFT Flow [31], we used the street-level and nature categories therein. In addition, taking a closer look at open map initiatives like www.openstreetmap.org inspired many of class selections in root- and macro-categories object, barrier and flat. To help with recognition tasks in research for autonomous driving, special emphasis was put on properly annotating different classes within macro-groups vehicle or traffic sign.

* https://playment.io/image-annotation/
* https://blog.playment.io/training-data-for-computer-vision/

