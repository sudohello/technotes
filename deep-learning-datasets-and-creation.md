---
Title: Datasets and Data Creation for Training Machines
Decription: Datasets and Data Creation for Training Machines
Author: Bhaskar Mangal
Date: 24th-Jul-2018
Last updated: 05th-Mar-2019
Tags: Datasets and Data Creation for Training Machines
---

**Table of Contents**
* TOC
{:toc}


## Types of Annotations and Applications for Computer Vision in AI


**Different Annotations by [playment.io](https://playment.io) for AI provided as commercial Services**

* [Image Annotation](https://playment.io/image-annotation/)
  * **Bounding Boxes**
  * **Cuboids**
      * Three dimensional bounding of vehicles, pedestrians, cyclists & obstacles on the road
  * **Points and Lines**
      * higher precision
  * **Polygons**
      * pixel perfect polygonal annotations
  * **Semantic Segmentation**
      * semantic segmentations with single pixel accuracy
  * **Object Recognition**
      * recognize all the objects in an image
* [Bounding Box Annotation](https://playment.io/bounding-box-annotation-tool)
  * **Quantification**
    * **Time per annotation**: Lowest
    * **Cost per annotation**: Least Expensive
    * **Shape perception**: Absent
    * **Spatial perception**: Present
  * **USE CASES**
      * **a) Object localization for Self-driving cars**
          * Extensively used to train autonomous driving perception models for pedestrians, traffic signs, lane obstacles, etc
      * **b) Object Detection for e-commerce**
          * Used to train visual search machine learning models for recognition of various fashion accessories and furniture
      * **c) Damage detection for Insurance**
          * Identification of car damage, roof damage or safety parameters from live world images to train machine learning models that detect the degree of damage for insurance claims
      * **d) Drone and Robot training**
          * Labelled images for training smart surveillance drones and robots to identify a variety of objects
* [Semantic Segmentation](https://playment.io/semantic-segmentation-tool)
  * **Quantification**
    * **Time per annotation**: Highest
    * **Cost per annotation**: Most Expensive
    * **Shape perception**: Present
    * **Spatial perception**: Absent
  * **USE CASES**
      * **a) Instance segmentation for feature detection / Panoptic segmentation**
          * Used for training perception models in non-environmental objects of interest
          * Used to individually segment objects of the same class by assigning instance unique IDs to each object
      * **b) Full pixel semantic segmentation**
          * High utility in autonomous vehicles and safety surveillance cameras where information of every pixel is critical and may influence the accuracy of the perception model
          * used in applications such as autonomous driving, robotics, and image search
* [3D Cuboids Annotation](https://playment.io/3d-cuboids-annotation-tool)
  * **Quantification**
    * **Time per annotation**: High
    * **Cost per annotation**: Expensive
    * **Shape perception**: Absent
    * **Spatial perception**: Present
  * **USE CASES**
      * **a) Camera based perception in autonomous vehicles**
          * Used to train computer vision models for spatial cognition from 2D images or videos. Relative distance of each mobile object from the ego car and vanishing point can be measured
      * **b) In-doors spatial distribution of objects**
          * Used to build 3D simulated worlds from 2D information captured by cameras
* [Line Annotation](https://playment.io/line-annotation-tool)
  * **Quantification**
    * **Time per annotation**: High
    * **Cost per annotation**: Expensive
    * **Shape perception**: Present
    * **Spatial perception**: Absent
  * **USE CASES**
      * **a) Lane detection for self-driving cars**
          * Well-defined different kinds of lanes for ego car, bicycle, opposite direction traffic, divergence etc
* [Landmark Annotation](https://playment.io/landmark-annotation-tool)
  * **Quantification**
    * **Time per annotation**: High
    * **Cost per annotation**: Expensive
    * **Shape perception**: Absent
    * **Spatial perception**: Present
  * **USE CASES**
      * **a)Point annotation for satellite imagery**
          * Used to detect and count minute objects like houses or trees in a area, cars in parking lots, etc
      * **b) Landmarking for pose-point annotations**
          * Detect poses of sports players for sports analytics, facial features for face recognition, prediction of pedestrians motion for autonomous vehicles
* [Polygonal Segmentation](https://playment.io/polygonal-segmentation-tool)
  * **Quantification**
    * **Time per annotation**: Moderate
    * **Cost per annotation**: Expensive
    * **Shape perception**: Present
    * **Spatial perception**: Absent
  * **USE CASES**
      * **a) Object localization from satellite and drone images**
          * Used to best approximate the shape of objects captured from distant cameras
      * **b) Detection of irregular shapes**
          * Good for detection models for logos, street sign boards, facial and pose features in sports analytics, etc
      * **c) Coarse Semantic Segmentation**
          * Coarse segmentation for weak supervision of your models to improve your model accuracy
* [Video Annotation](https://playment.io/video-annotation-tool)
  * **Quantification**
    * **Time per annotation**: Low
    * **Cost per annotation**: Least Expensive
    * **Shape perception**: Absent
    * **Spatial perception**: Absent
  * **USE CASES**
      * **a) Object tracking for Self-driving cars**
         * Extensively used to train autonomous driving prediction models for vehicles, pedestrians, cyclists, lanes, etc
* [3d Point Cloud](https://playment.io/3D-point-cloud)
  * **Quantification**
    * **Time per annotation**: Unknown
    * **Cost per annotation**: Unknown
    * **Shape perception**: Unknown
    * **Spatial perception**: Unknown
  * **USE CASES**
      - **a) 3D box annotation for object detection**
          * Get 3D coordinates, yaw, heading and tracklets of objects accurate up to 1cm with 3D boxes
      - **b) 3D Segmentation**
          * Leverage this data to understand how objects are moving in the environment
      - **c) Polyline annotation for lane tracking**
          * Polyline annotation in 3D point cloud data is used to provide guided navigation path and edge case delimiters during the navigation for such situations


## Datasets and Data Creation for Training Machines


## Creation for Training Machines


## Annotatino Service Provides for AI
* [playment.io](https://playment.io/image-annotation/)
  * [API for AI Annotations](https://docs.playment.io/reference#welcome)


## AI Annotation Tools

**Summary**

| S.No. | AI Annotation Apps                  | Tech Stack                           | Website                                                                                                   | Online Demo                              | Source Code                                                     |
|-------|-------------------------------------|--------------------------------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------|-----------------------------------------------------------------|
| 1     | via                                 | js                                   |                                                                                                           |                                          | https://github.com/ox-vgg/via.git                               |
| 2     | scalabel                            | js, nodejs, python – loclhost server | https://www.scalabel.ai                                                                                   |                                          | https://github.com/ucbdrive/scalabel.git                        |
| 3     | AutoNUE (based on cityscapeScripts) | python                               |                                                                                                           |                                          | https://github.com/AutoNUE/public-code                          |
| 4     | labelImg                            | python                               |                                                                                                           |                                          | https://github.com/tzutalin/labelImg                            |
| 5     | cityscapeScripts                    |                                      |                                                                                                           |                                          | https://github.com/mcordts/cityscapesScripts/                   |
| 6     | LabelMe                             |                                      |                                                                                                           | http://labelme.csail.mit.edu/Release3.0/ | https://github.com/CSAILVision/LabelMeAnnotationTool            |
| 7     | LabelBox                            | cloud based tool                     |                                                                                                           |                                          | https://github.com/Labelbox/Labelbox                            |
| 8     | RectLabel                           |                                      | https://rectlabel.com/                                                                                    |                                          | https://github.com/ryouchinsa/Rectlabel-support                 |
| 9     | VoTT                                | nodejs, python-2.7                   |                                                                                                           |                                          | https://github.com/Microsoft/VoTT/blob/master/README.md         |
| 10    | imgLab                              | c++                                  |                                                                                                           |                                          | https://github.com/davisking/dlib/tree/master/tools/imgla       |
| 11    | COCO UI                             | js, python – localhost server        |                                                                                                           |                                          | https://github.com/tylin/coco-ui                                |
| 12    | LIBLABEL                            | MATLAB                               |                                                                                                           |                                          | http://www.cvlibs.net/software/liblabel/                        |
| 13    | CVAT                                | python                               |                                                                                                           |                                          | https://github.com/opencv/cvat                                  |
| 14    | Anno-Mage                           | python                               | http://www.virajmavani.me/saiat/                                                                          |                                          | https://github.com/virajmavani/semi-auto-image-annotation-tool/ |
| 15    | Sloth                               | python                               | https://cvhci.anthropomatik.kit.edu/~baeuml/projects/a-universal-labeling-tool-for-computer-vision-sloth/ | https://sloth.readthedocs.io/en/latest/  | https://github.com/cvhciKIT/sloth                               |
| 16    | LabelID                             | nodejs, mongoDB                      | https://sweppner.github.io/labeld/                                                                        |                                          | https://github.com/sweppner/labeld                              |
| 17    | ALPS Label                          | wordpress plugin                     | https://alpslabel.wordpress.com/                                                                          |                                          | https://alpslabel.wordpress.com/2017/01/26/alt/                 |
| 18    | imgAnnotation                       |                                      |                                                                                                           |                                          | https://github.com/alexklaeser/imgAnnotation                    |



* **VGG VIA** - recomended
  * https://github.com/ox-vgg/via - simple, intutive, best
    - http://www.robots.ox.ac.uk/~vgg/blog/author/abhishek-dutta.html
    - http://www.robots.ox.ac.uk/~vgg/software/via/
    - http://www.robots.ox.ac.uk/~vgg/software/via/via-1.0.6.html
    - http://www.robots.ox.ac.uk/~vgg/blog/vgg-image-annotator.html
  ```bash
  git clone https://github.com/ox-vgg/via.git
  git checkout via-2.0.5
  ```
  * VGG VIA tool saves the annotations in a JSON file, and each mask is a set of polygon points
  * No documentation for the format, but it’s pretty easy to figure out by looking at the generated JSON
* **labelImg**
  * https://github.com/tzutalin/labelImg
    - `git clone https://github.com/tzutalin/labelImg.git`
* **LabelBox**
  * https://github.com/Labelbox/Labelbox/blob/master/LICENSE
  * https://www.labelbox.com/
  * https://github.com/Labelbox/Labelbox/tree/master/custom-interfaces/classification
* **[RectLabel](https://rectlabel.com/)**
  * https://rectlabel.com/ 
* **VoTT**
  * https://github.com/Microsoft/VoTT/blob/master/README.md
* **LabelMe**
  * https://github.com/wkentaro/labelme
  * https://github.com/CSAILVision/LabelMeAnnotationTool
  * https://en.wikipedia.org/wiki/LabelMe
* **imglab**
  * https://github.com/davisking/dlib/tree/master/tools/imglab
  ```bash
  git clone https://github.com/davisking/dlib.git
  cmake -DCMAKE_C_COMPILER=/usr/bin/gcc-6 -DCMAKE_CXX_COMPILER=/usr/bin/g++-6 ..
  ```
* **[scalabel](https://www.scalabel.ai/)** - 2D,3D, Images, Videos, Point Clouds
  * `git clone https://github.com/ucbdrive/scalabel.git`
  * https://github.com/ucbdrive/scalabel
* **[CVAT](https://github.com/opencv/cvat)**
  * https://github.com/opencv/cvat
* **[SLOTH](https://github.com/cvhciKIT/sloth)**
  * https://cvhci.anthropomatik.kit.edu/~baeuml/projects/a-universal-labeling-tool-for-computer-vision-sloth/ 
  * https://github.com/cvhciKIT/sloth
  * https://sloth.readthedocs.io/en/latest/
* **[LIBLABEL](http://www.cvlibs.net/software/liblabel/)**
  * Lightweight Semantic/Instance Annotation Tool
  * MATLAB
* **[LabelID](https://github.com/sweppner/labeld)**
  * https://sweppner.github.io/labeld/
* **[ALPS Label](https://alpslabel.wordpress.com/)**
  *  https://alpslabel.wordpress.com/2017/01/26/alt/
* **[CoCo UI](https://github.com/tylin/coco-ui)**
  * https://github.com/tylin/coco-ui
  * The tool used to annotate the COCO dataset.
* **[imgAnnotation](https://github.com/alexklaeser/imgAnnotation)**
  * https://github.com/alexklaeser/imgAnnotation
* **[PixelAnnotationTool](https://github.com/abreheret/PixelAnnotationTool)**
  * https://github.com/abreheret/PixelAnnotationTool
  * v1.0.0 - 5 Oct 2017 
  * v1.3.2 - Feb 2019
  * Qt >= 5.x; CMake >= 2.8.x; OpenCV >= 2.4.x 

## **Image Process Tools/Apps**
* **ImageSegmentation**
  * https://github.com/AKSHAYUBHAT/ImageSegmentation
  * https://www.eraseimage.com/
* **commacoloring**
  * https://github.com/commaai/commacoloring
  * https://commacoloring.herokuapp.com/
  * based on `js-segment-annotator`
* **js-segment-annotator**
  * https://github.com/kyamagu/js-segment-annotator
  * http://kyamagu.github.io/js-segment-annotator/?view=index
* **Color Extractor**
  * **ColorThief - get dominant color in an image**
    * https://www.abeautifulsite.net/how-to-get-the-dominant-colors-of-an-image-with-javascript
    * https://lokeshdhakar.com/projects/color-thief/
    * [javascript] - https://github.com/lokesh/color-thief
    * [PHP] - https://github.com/ksubileau/color-thief-php
  * https://ourcodeworld.com/articles/read/403/top-5-best-image-color-extraction-javascript-and-jquery-plugins


**Summary**

| S.No. | Image Processing Apps                         | Tech Stack                    |  | Online Demo                                               | Source Code                                      |
|-------|-----------------------------------------------|-------------------------------|--|-----------------------------------------------------------|--------------------------------------------------|
| 1     | JS Segment Annotator                          | js                            |  | http://kyamagu.github.io/js-segment-annotator/?view=index | https://github.com/kyamagu/js-segment-annotator  |
| 2     | commacoloring (based on JS Segment Annotator) | js, python – localhost server |  | https://commacoloring.herokuapp.com/                      | https://github.com/commaai/commacoloring         |
| 3     | Color Thief JS                                | js                            |  | https://lokeshdhakar.com/projects/color-thief/            | https://github.com/lokesh/color-thief            |
| 4     | Color Thief PHP                               | php                           |  |                                                           | https://github.com/ksubileau/color-thief-php     |
| 5     | ImageSegmentation                             | js, FabricJS                  |  | https://www.eraseimage.com/                               | https://github.com/AKSHAYUBHAT/ImageSegmentation |



## **Vector Editing Tools/Apps**


**Summary**

| S.No. | Vector Editing Apps |
|-------|---------------------|
| 1     | Vector Editor       |


* **Vector Editors**
  * http://teselagen.github.io/openVectorEditor/#/Editor



**Credit: [Excelsheet Data to Markdown table](https://thisdavej.com/copy-table-in-excel-and-paste-as-a-markdown-table/)**

## **Listing of Tools**
* https://en.wikipedia.org/wiki/List_of_manual_image_annotation_tools
* https://www.researchgate.net/post/Can_anyone_suggest_an_image_labeling_tool_for_object_detection
* http://sloth.readthedocs.io/en/latest/
* https://github.com/yuyu2172/image-labelling-tool
* https://blog.playment.io/training-data-for-computer-vision/
* https://alpslabel.wordpress.com/
* https://www.quora.com/What-is-the-best-image-labeling-tool-for-object-detection
* https://oclavi.com/
* https://playment.io/image-annotation/
* https://blog.playment.io/training-data-for-computer-vision/
* https://www.deepvideoanalytics.com/
* https://prodi.gy/

## Amazon Mechanical Turk - MTurk
- https://www.mturk.com/
Amazon Mechanical Turk (MTurk) operates a marketplace for work that requires human intelligence. The MTurk web service enables companies to programmatically access this marketplace and a diverse, on-demand workforce. Developers can leverage this service to build human intelligence directly into their applications.

While computing technology continues to improve, there are still many things that human beings can do much more effectively than computers, such as identifying objects in a photo or video, performing data de-duplication, transcribing audio recordings or researching data details. Traditionally, tasks like this have been accomplished by hiring a large temporary workforce (which is time consuming, expensive and difficult to scale) or have gone undone.

MTurk aims to make accessing human intelligence simple, scalable, and cost-effective. Businesses or developers needing tasks done (called Human Intelligence Tasks or “HITs”) can use the robust MTurk API to access thousands of high quality, global, on-demand Workers—and then programmatically integrate the results of that work directly into their business processes and systems. MTurk enables developers and businesses to achieve their goals more quickly and at a lower cost than was previously possible.

**Using MTurk**
* http://labelme.csail.mit.edu/Release3.0/browserTools/php/mechanical_turk.php

**Annotating images with bounding boxes using Amazon Mechanical Turk**
* https://blog.mturk.com/tutorial-annotating-images-with-bounding-boxes-using-amazon-mechanical-turk-42ab71e5068a
* https://blog.mturk.com/tutorial-measuring-the-accuracy-of-bounding-box-image-annotations-from-mturk-ad3dfcdf8aa0

**A beginner’s guide to crowdsourcing ML training data with Python and MTurk**
* https://blog.mturk.com/tutorial-a-beginners-guide-to-crowdsourcing-ml-training-data-with-python-and-mturk-d8df4bdf2977

**Key Terms**
* HIT - Human Intelligence Task


## Labelling for AI datasets

**Format**
* There isn’t a universally accepted format to store segmentation masks
* Some datasets save them as PNG images, others store them as polygon points, and so on

**Loading the Dataset**
* To handle all these cases,implementation should provide a Dataset class that is inherited from and then override a few functions to read your data in whichever format it happens to be.

**Tools**

**Labeling for Self-Driving Cards**
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


## Image Augmentation Utilities

* [imgaug](https://github.com/aleju/imgaug)
  ```bash
  pip3 install imgaug
  ```


## Training and Prediction on Multiple Datasets for Object Detections/Segmentation

**Challenges**
* Every Open dataset available have their own way of classification and labels. It's OK as everyone and as an individual labels and categories text can be given in innumerable ways
* Some datasets assign integer values to their classes and some don't
* They have different storage formats
* Everyone has desire or need to have different category groups and labels
* In order to explore the labels and ids, may require to download the entire dataset and then programatically load to determine the category details
* there cannot be one soultion fit all but still should be possible to switch between context without manual intervention at the time of use


**Other Challenges**
* `pre-trained` and custom models have their own labelling schemes
* no easy way to manage and explore labels (i.e. class_names and ids and not the polygons or segmentation)
* most of the time these label mapping is the part of the python code in general due to convenience
* addition of new labels and categories
* `text -> image` based searching in CBIR becomes cumbersome for incremental workflows
* different business use cases may require:
  * to label data differently
  * to use only subset of labels, hence detections
    - here, we may not want to disable the detections of superset but in the final output turn-off selectively; high ROI item from commericalisation perpective
  * example: categorization, labeling for **self-driving car** vs **smartcity** vs **indoors** vs **maps** even though they may share common objects but different grouping may be desired for each of these business verticals


**Area of Research**
* **Incremental learning** vs **transfer learning**
* Is it possible to keep the memory of previously learned categorization, when training for new category without having to provide the whole training dataset of previous training?


**what is needed got multi-dataset training**
* **Open Datasets**
  * different datasets needs to be downloaded in common repository
    - to avoid duplication and waste of resources as these are huge size
    - should be stored in external storage and mapped to AI servers; use symlnks to individual code repositories
* **Data Exploratory Tools**
  * ipython notebooks and python apis are generally available for most of the popular datasets
  * use these to explore and extract required data for the control sheets
* **Control Sheets**
  * Mapping of labels, categories across multiple datasets with the custom dataset
  * With versioning and other release management aspects
  * individual csv files for different datasets, with proper naming convetions
* **Annotation Label API**
  * A common api to be created and used in individual code repository for training, evaluation and predictions
* **Annotation Tools**
  * Flexibility to use any custom or open source tools for annotations
  * use the control sheets
    * integrated with APIs or simply imports in annotation tool to get all categorisations


## Dataset Management
- https://autonomous-driving.org/2018/06/16/dataset-management-for-machine-learning/


## Dataset / Data source / Datasource for ML / Deep Learning / Computer Vision Datasets


### AI datasets Search Engines
* http://classif.ai/


### Dataset APIs
**MS COCO Dataset API**
* [pycocotools](https://github.com/cocodataset/cocoapi)
* [pycoco - with fix from crowdAI](https://github.com/crowdai/coco)
  - Note: If you are using `Python3.*`, then there are chances that pycocotools will not work for you. In that case, install it from this fork :
  ```bash
  pip3 install git+https://github.com/crowdai/coco.git#subdirectory=PythonAPI
  ```
* More details, refer: [MS COCO](mscoco-dataset.md)


### **Datasets Detailed Review / Overview**

1. [Cityscape](cityscape-dataset.md)
2. [MVD - Mapillary](mapillary-dataset.md)
3. [ApolloScape](apolloscape-dataset.md)
4. [MS COCO - things, stuff, panoptic](mscoco-dataset.md)
5. [ADE20K](ade20k-dataset.md)
6. [IDD - Indian Driving Dataset](idd-dataset.md)
7. [BDD](bdd-dataset.md)


### **Extensive List of Datasets**
- https://projet.liris.cnrs.fr/voir/wiki/doku.php?id=datasets
- https://handong1587.github.io/computer_vision/2015/09/24/datasets.html
- https://www.analyticsvidhya.com/blog/2018/03/comprehensive-collection-deep-learning-datasets/
- https://martin-thoma.com/sota/
- SotA - State of the Arts
- https://github.com/nightrome/really-awesome-semantic-segmentation
* [50 free Machine Learning Datasets: Image Datasets - 22nd-Oct-2018](https://blog.cambridgespark.com/50-free-machine-learning-datasets-image-datasets-241852b03b49)


* **[Imagenet](http://image-net.org/download)**
  - http://www.image-net.org/
  - http://image-net.org/download-API
  - http://image-net.org/download
* **[OpenImages](https://github.com/openimages/dataset)**
  - https://storage.googleapis.com/openimages/web/index.html
  - https://github.com/openimages/dataset
  - https://ai.googleblog.com/2018/04/announcing-open-images-v4-and-eccv-2018.html
* **Tencent**
  - https://medium.com/syncedreview/tencent-open-sources-its-massive-multi-labeled-image-dataset-7b0b3dd5373f
* **Google JFT-300M**
  - https://arxiv.org/pdf/1707.02968.pdf
  - https://ai.googleblog.com/2017/07/revisiting-unreasonable-effectiveness.html
* **Pima Indians**
* **Ionosphere**
  - http://cv-tricks.com/tensorflow-tutorial/understanding-alexnet-resnet-squeezenetand-running-on-tensorflow/
* **Image segmentations**
  - https://aws.amazon.com/public-datasets/spacenet/
  - http://www.cvlibs.net/datasets/kitti/eval_road.php
* **[MS COCO](http://cocodataset.org/#home)**
  - **Detailed Overview**: [MS COCO](mscoco-dataset.md)
  - http://cocodataset.org/#home
  - COCO is a large-scale object detection, segmentation, and captioning dataset
  - https://github.com/cocodataset
  - http://cocodataset.org/#overview
  - **Annnotation Format**
    * https://github.com/cocodataset/cocoapi/issues/111
    ```bash
    git clone https://github.com/cocodataset/cocoapi.git
    ```
  * Download train2014
    ```bash
    wget -c http://images.cocodataset.org/annotations/annotations_trainval2014.zip
    wget -c http://images.cocodataset.org/zips/train2014.zip
    wget -c http://images.cocodataset.org/zips/val2014.zip
    wget -c https://dl.dropboxusercontent.com/s/s3tw5zcg7395368/instances_valminusminival2014.json.zip?dl=0
    ```
  * **coco stuff**
    * https://github.com/nightrome/cocostuff
* **PASCAL**
  * PASCAL VOC 2006
  * PASCAL VOC 2007
  * PASCAL VOC 2008
  * PASCAL VOC 2009
  * PASCAL VOC 2010
  * PASCAL VOC 2011 incl. SBD
  * PASCAL VOC 2012
  * PASCAL Context
  * PASCAL Person Part
  - http://host.robots.ox.ac.uk/pascal/VOC/
    ```bash
    wget -c http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtrainval_06-Nov-2007.tar
    wget -c http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtest_06-Nov-2007.tar
    wget -c http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar
    ```
* **Inria**
  - A large set of marked up images of standing or walking people
  - http://pascal.inrialpes.fr/data/human/
  ```bash
  wget -c ftp://ftp.inrialpes.fr/pub/lear/douze/data/INRIAPerson.tar
  ```
* **[https://vision.in.tum.de/data](https://vision.in.tum.de/data)**
  * https://vision.in.tum.de/data/datasets/rgbd-dataset/download
  * https://vision.in.tum.de/data/datasets
  * softwres: https://vision.in.tum.de/data/software
*  **Misc**
  * MNIST
  * notMNIST
  * **[CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html)**
    - One popular toy image classification dataset is the CIFAR-10 dataset. This dataset consists of 60,000 tiny images that are 32 pixels high and wide. Each image is labeled with one of 10 classes (for example “airplane, automobile, bird, etc”). These 60,000 images are partitioned into a training set of 50,000 images and a test set of 10,000 images.
    - https://www.cs.toronto.edu/~kriz/cifar.html
  * cifar-100
* **fast.ai**
  * http://course.fast.ai/datasets
* **Viva**
  - http://cvrr.ucsd.edu/vivachallenge/index.php/signs/sign-detection/
* **LISA**
  - http://cvrr.ucsd.edu/LISA/lisa-traffic-sign-dataset.html
  - https://www.codemade.io/lisa-traffic-sign-dataset/
* **Caltech-UCSD Birds-200-2011**
  * http://www.vision.caltech.edu/visipedia/CUB-200-2011.html
  * Warning: Images in this dataset overlap with images in ImageNet. Exercise caution when using networks pretrained with ImageNet (or any network pretrained with images from Flickr) as the test set of CUB may overlap with the training set of the original network.
* **Chinsese Dataset**
  * https://ctwdataset.github.io/
* **LabelMe Facade**
* **SIFT Flow / LabelMe Outdoor**
* **LM+SUN**
* **SUN RGB-D**
* **SUN**
* **MSRC (21/23/v2 and 9/13/v1)**
* **NYUD (1 or 2)**
* **Stanford Background**
* **Barcelona**
* **Sowerby**
* **Corel**
* **TU Graz**
* **MINC (Materials in Context)**
* **Etrims**
* **Geometric Context (Gatech)**
* **Cross Category Object Recognition (CORE)**
* **MHMS 11**
* **Leuven (+stereo augmented)**
* **Google Street View**
* **MDRS3 - Multi-Domain Road Scene Semantic Segmentation**
* **Vaihingen (ISPRS contest)**
* **2D-3D-S (Stanford)**
* **NICTA/DATA61 2D-3D**
* **CMU VMR**
* **Flickr MFC**
* **GTA / Playing for Benchmarks [Richter ICCV 17]**
* **Cross-city dataset [Yi-Hsin Chen]**
* **[QMUL Multiview Face Dataset](http://www.eecs.qmul.ac.uk/~sgg/QMUL_FaceDataset/)**

### Remote Sensing
**Building Footprint Extraction**

* **[spacenet](https://spacenetchallenge.github.io/)**
  * Localizes building footprints in pixel level in high-resolution satellite imagery
  * https://spacenetchallenge.github.io/
  * https://spacenetchallenge.github.io/datasets/datasetHomePage.html
* **crowd-ai**
  * **Satellite Images: Building Footprint**
    * https://unitar.org/unosat/
    * https://www.unglobalpulse.org/
  * **Main web site for reference:** https://www.crowdai.org/challenges/mapping-challenge
  * **[Baseline](https://github.com/crowdai/crowdai-mapping-challenge-mask-rcnn)**
    ```bash
    git clone https://github.com/crowdAI/crowdai-mapping-challenge-mask-rcnn.git
    ```
  * **[Round-1 Starter Kit](https://github.com/crowdAI/mapping-challenge-starter-kit)**
    ```bash
    git clone https://github.com/crowdAI/mapping-challenge-starter-kit.git
    ```
  * **[Round-2 Starter Kit](https://github.com/crowdAI/mapping-challenge-round2-starter-kit)**
  * **open solution**
    * https://github.com/neptune-ml/open-solution-mapping-challenge


### Traffic Sign Datasets
* **German**
  * GTSRB (Traffic sign recognition)
  * GTSDB (Traffic sign detection) 
  - http://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset
* **[LISA: Laboratory for Intelligent Safe Automobiles](http://cvrr.ucsd.edu/LISA/lisa-traffic-sign-dataset.html)**
  - http://cvrr.ucsd.edu/LISA/lisa-traffic-sign-dataset.html
* **[Belgium](https://btsd.ethz.ch/shareddata/)**
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


### **Self Driving Car (Autonomous, Autonomy) Datasets Semantic Segmentation**
- [self-driving-car-datasets-semantic-segmentation](https://blog.playment.io/self-driving-car-datasets-semantic-segmentation/)
- [the-worlds-largest-driving-dataset](https://blog.getnexar.com/introducing-bdd100k-the-worlds-largest-driving-dataset-b4e157bf2632)
- [semantic-segmentation datasets list](https://github.com/mrgloom/awesome-semantic-segmentation#datasets)


**Differentiate Different Types of Computer Vision based Datasets used in AI**

**Self-driving Car (Autonomy) vs Urban Scene**
  
| Self-driving Car (Autonomy)                                 | Urban Scene                                                  |
|:------------------------------------------------------------|:-------------------------------------------------------------|
| * Contains images only from the driver's perspective        | Contains images from walking, and non-road scene perspective |
| * Outdoor images only                                       | Outdoor images only                                          |
| * Contains sequential camera frames                         | Not a pre-condition                                          |
| * Can be aumgented with other sequential camera sensor data | Cannot be agumented with sequential sensor data              |


**Mostly, autonomous navigation focus on:-**
* structured driving environments
* well-delineated infrastructure such as lanes
* small number of well-defined categories for traffic participants
* low variation in object or background appearance 
* strict adherence to traffic rules


**Dataset Comparison**
* [semantic-segmentation-datasets-for-urban-driving-scenes](https://autonomous-driving.org/2018/07/15/semantic-segmentation-datasets-for-urban-driving-scenes/)


| Dataset Name     | Year | Labeled Images for Training | Classes | Multiple Cities | Environment                                           | Usage                                    | Location                                                         | Details                                                                                                         | Details |    |    |    |    |    |    |
|:-----------------|:-----|:----------------------------|:--------|:----------------|:------------------------------------------------------|:-----------------------------------------|:-----------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------|:--------|:---|:---|:---|:---|:---|:---|
| KITTI            |      | 200                         | 34      | No              | Daylight                                              | * semantic segmentation                  | * Karlsruhe in Germany in rural areas and on highways            |                                                                                                                 |         |    |    |    |    |    |    |
|                  |      |                             |         |                 |                                                       | * 2D and 3D object detection             |                                                                  |                                                                                                                 |         |    |    |    |    |    |    |
|                  |      |                             |         |                 |                                                       | * object tracking                        |                                                                  |                                                                                                                 |         |    |    |    |    |    |    |
|                  |      |                             |         |                 |                                                       | * road/lane detection                    |                                                                  |                                                                                                                 |         |    |    |    |    |    |    |
|                  |      |                             |         |                 |                                                       | * scene flow                             |                                                                  |                                                                                                                 |         |    |    |    |    |    |    |
|                  |      |                             |         |                 |                                                       | * depth evaluation                       |                                                                  |                                                                                                                 |         |    |    |    |    |    |    |
|                  |      |                             |         |                 |                                                       | * optical flow                           |                                                                  |                                                                                                                 |         |    |    |    |    |    |    |
|                  |      |                             |         |                 |                                                       | * semantic instance level segmentation   |                                                                  |                                                                                                                 |         |    |    |    |    |    |    |
| Cityscapes       | 2016 | 3478                        | 34      | Yes             | Daylight                                              | * semantic understanding of urban scenes | * 50 cities of Germany and neighboring countries                 | 5k fine annotated and 20k weakly annotated images                                                               |         |    |    |    |    |    |    |
| Mapillary Vistas | 2017 | 20k                         | 66      | Yes             | Daylight, rain, snow, fog, haze, dawn, dusk and night |                                          | * North and South America, Europe, Africa, and Asia              | similar to the Cityscapes dataset; added a new tricycle class which covers all kinds of three-wheeled vehicles. |         |    |    |    |    |    |    |
| ApolloScape      | 2018 | 147k                        | 36      | No              | Daylight, snow, rain, foggy                           |                                          |                                                                  |                                                                                                                 |         |    |    |    |    |    |    |
| BDD100K          |      | 8000                        | 19      | Yes             | Daylight, rain, snow, fog, haze, dawn, dusk and night | * object detection                       | * different areas of US. Infrastructure and highway traffic sign | * 800 times larger than ApolloScape dataset                                                                     |         |    |    |    |    |    |    |
|                  |      |                             |         |                 |                                                       | * Lane detection                         |                                                                  |                                                                                                                 |         |    |    |    |    |    |    |
|                  |      |                             |         |                 |                                                       | * drivable area                          |                                                                  |                                                                                                                 |         |    |    |    |    |    |    |
|                  |      |                             |         |                 |                                                       | * semantic instance segmentation         |                                                                  |                                                                                                                 |         |    |    |    |    |    |    |
|                  |      |                             |         |                 |                                                       | * self drivingcar dataset (biggest)      |                                                                  |                                                                                                                 |         |    |    |    |    |    |    |
| IDD              | 2018 |                             | 30      | No              | Daylight                                              |                                          |                                                                  |                                                                                                                 |         |    |    |    |    |    |    |




* **[CamVid Dataset](http://mi.eng.cam.ac.uk/research/projects/VideoRec/CamVid/)**
  - **CamVid**: Cambridge Video
  - http://mi.eng.cam.ac.uk/research/projects/VideoRec/CamVid/
* **[KITTI Dataset](http://www.cvlibs.net/datasets/kitti/)**
  - **KITTI**: Karlsruhe Institute of Technology and Toyota Technological Institute
  - http://www.cvlibs.net/datasets/kitti/
  - http://www.cvlibs.net/datasets/kitti/eval_road.php
* **[DUS Dataset](http://www.6d-vision.com/scene-labeling)**
  - **DUS**: Daimler Urban Segmentation
  - http://www.6d-vision.com/scene-labeling
  - http://www.6d-vision.com/home
* **[CityScapes Dataset](https://www.cityscapes-dataset.com/)**
  * **Detailed Overview**: [Cityscape](cityscape-dataset.md)
  - https://www.cityscapes-dataset.com/
  - https://www.cityscapes-dataset.com/benchmarks/
* **[Mapillary Vista Dataset: MVD](https://blog.mapillary.com/product/2017/05/03/mapillary-vistas-dataset.html)**
  - **MVD**: Mapillary Vista Dataset
  - **Detailed Overview**: [Mapillary](mapillary-dataset.md)
  - https://blog.mapillary.com/product/2017/05/03/mapillary-vistas-dataset.html
  - https://www.mapillary.com/dataset/vistas
* **[Synthia Dataset](http://synthia-dataset.net/download-2/)**
  - http://synthia-dataset.net/ 
* **[Udacity Dataset](https://github.com/udacity/self-driving-car/tree/master/datasets)**
  - https://github.com/udacity/self-driving-car/tree/master/datasets
* **[ApolloScape](http://apolloscape.auto/index.html)**
  - **Detailed Overview**: [apolloscape-dataset.md](apolloscape-dataset.md)
* **[FCAV](https://fcav.engin.umich.edu/sim-dataset)**
  * Driving in the Matrix: Can Virtual Worlds Replace Human-Generated Annotations for Real World Tasks?
  - https://arxiv.org/abs/1610.01983
  - https://fcav.engin.umich.edu/safety-pilot-dataset
  - https://fcav.engin.umich.edu/sim-dataset
  - https://github.com/umautobots/driving-in-the-matrix
  - https://github.com/umautobots/GTAVisionExport
* **[BDD 100K - Berkeley DeepDrive](https://bdd-data.berkeley.edu/)**
  * https://blog.getnexar.com/introducing-bdd100k-the-worlds-largest-driving-dataset-b4e157bf2632
  * https://bdd-data.berkeley.edu/wad-2018.html
  * https://deepdrive.berkeley.edu/
* **[IDD - Indian Driving Dataset](http://idd.insaan.iiit.ac.in/)**
* TBD
  * https://robotcar-dataset.robots.ox.ac.uk/downloads/
  * http://cvgl.stanford.edu/projects/objectnet3d
  * https://comma.ai/
  * https://medium.com/@comma_ai/a-panda-and-a-cabana-how-to-get-started-car-hacking-with-comma-ai-b5e46fae8646
  * https://github.com/commaai/opendbc
  * https://github.com/commaai
  * https://devblogs.nvidia.com/deep-learning-self-driving-cars/
  * https://hackernoon.com/mit-6-s094-deep-learning-for-self-driving-cars-2018-lecture-2-notes-e283b9ec10a0
  * https://medium.com/@mslavescu/introduction-to-obd-ii-and-can-bus-for-self-driving-cars-6b9f9a2a8775
  * https://www.slideshare.net/jwiegelmann/machine-learning-for-selfdriving-cars
  * https://medium.com/@maxdeutsch/how-to-build-a-self-driving-car-in-one-month-d52df48f5b07
  * https://medium.com/@subodh.malgonde/building-an-actual-self-driving-car-53f67ca41566
  * https://news.voyage.auto/an-introduction-to-the-can-bus-how-to-programmatically-control-a-car-f1b18be4f377
  * https://www.csselectronics.com/screen/page/simple-intro-to-can-bus/language/en
  * https://www.csselectronics.com/screen/page/reverse-engineering-can-bus-messages-with-wireshark

  



### Scene understanding Datasets
* **[MIT Places Dataset](http://places.csail.mit.edu/)**
  * http://places.csail.mit.edu/
* **[ADE20K Dataset](http://groups.csail.mit.edu/vision/datasets/ADE20K/)**
  * **Detailed Overview**: [ade20k](ade20k-dataset.md)
  * Deals with: (1) scene parsing, (2) instance segmentation, (3) semantic boundary detection. More details, refer: http://placeschallenge.csail.mit.edu/
  * http://groups.csail.mit.edu/vision/datasets/ADE20K/
  * pixel-wise annotated image dataset for scene parsing. Scene parsing network are also proposed to detect and segment visual concepts from any input images.
  * https://gluon-cv.mxnet.io/build/examples_datasets/ade20k.html


### 3D Datasets
- **[Matterport Dataset](https://niessner.github.io/Matterport/)**
  - https://hackernoon.com/announcing-the-matterport3d-research-dataset-815cae932939
  - https://matterport.com/blog/2017/09/20/announcing-matterport3d-research-dataset/
  - https://niessner.github.io/Matterport/
  - https://arxiv.org/pdf/1709.06158.pdf
- Trimble 3D Warehouse
- Yobi3D
- ShapeNet - Semantic annotation knowledge bases
  * https://drive.google.com/file/d/1Z8gt4HdPujBNFABYrthhau9VZW10WWYe/view
- [OpenSurfaces](http://opensurfaces.cs.cornell.edu/)
  * http://opensurfaces.cs.cornell.edu/


### Face Datasets
* https://github.com/jian667/face-dataset


### Others
- https://en.wikipedia.org/wiki/List_of_datasets_for_machine_learning_research
* Free datasets are available from places like Kaggle.com and UCI. 
  - https://www.kaggle.com/datasets
  - https://archive.ics.uci.edu/ml/datasets.html


## Dataset Pre-processing
* http://shubhagrawal.in/2016/10/13/machine-learning-data-preprocessing/


## Dataset Creation Effort Statistics

After working hard to collect your images and annotating all the objects, you have to decide what format you’re going to use to store all that info. 
* https://venturebeat.com/2018/10/22/googles-fluid-annotation-uses-ai-to-speed-up-image-dataset-annotation/
* Labeling a single pic in the popular Coco+Stuff dataset, for example, takes 19 minutes; tagging the whole dataset of 164,000 images would take over 53,000 hours.
* Different Sets:
  * Training
  * Validation
  * Test
  * Consistency (annotations used for checking the annotation consistency)


## Fluid Annotation - Google
* https://venturebeat.com/2018/10/22/googles-fluid-annotation-uses-ai-to-speed-up-image-dataset-annotation/
* https://ai.googleblog.com/2018/10/fluid-annotation-exploratory-machine.html
* https://fluidann.appspot.com/ - Demo
* An Exploratory Machine Learning–Powered Interface for Faster Image Annotation
* machine learning–powered interface for annotating the class label and outline of every object and background region in an image, accelerating the creation of labeled datasets by a factor of 3x
* Fluid Annotation starts from the output of a strong semantic segmentation model, which a human annotator can modify through machine-assisted edit operations using a natural user interface.
* Interface empowers annotators to choose what to correct and in which order, allowing them to effectively focus their efforts on what the machine does not already know
* More precisely, to annotate an image we first run it through a pre-trained semantic segmentation model (Mask-RCNN). This generates around 1000 image segments with their class labels and confidence scores. The segments with the highest confidences are used to initialize the labeling which is presented to the annotator. Afterwards, the annotator can:
  * Change the label of an existing segment choosing from a shortlist generated by the machine
  * Add a segment to cover a missing object. The machine identifies the most likely pre-generated segments, through which the annotator can scroll and select the best one
  * Remove an existing segment
  * Change the depth-order of overlapping segments


**Other commetitors applying AI in annotation**
* Scale - https://venturebeat.com/2018/08/07/scale-raises-18-million-to-label-data-from-autonomous-car-companies-like-lyft-and-embark/
* https://supervise.ly/


## AI Database Creation Companies
* https://www.kinetica.com/
  - Combine a GPU database, real-time location visualization, and the power of AI
  - https://www.kinetica.com/solutions/


## Business, News, Blogs
* [ai-databases-what-they-are-and-why-your-business-should-care](https://in.pcmag.com/ibm-watson-analytics/117335/ai-databases-what-they-are-and-why-your-business-should-care) - TBD:cross-links
  * "An AI database is a subset of a general database," said Radalj. "Right now, AI databases are very popular. But a lot of solutions use distributed components. [Apache] Spark, [Hadoop] MapReduce and HDFS are always spinning back and forth rather than in-memory
  * "This gives you an idea of what an extreme difference there is in what vendors are doing. Some are trying to pass off advanced analytics as ML—and it isn't. And others are doing ML at such an advanced level that's beyond what most businesses can comprehend at the moment."
  * **"Data Availability"** and **"Data Ingestion"** are key; **"Data Shipping"**
  * Kinetica doesn't separate CPU and GPU compute nodes versus storage nodes
  * solutions use an **orchestrator** like IBM Symphony to schedule work across various components
  * Kinetica stresses function shipping against co-located resources, with advanced optimization to minimize data shipping"
  * **goal is to create a workflow in which the faster batch ingestion, streaming, and querying generate model results that can immediately be applied to BI**
  * "It's easier to quickly provision, prototype, and test. The word 'modeling' is thrown about in AI, but it's all about cycling through different approaches—the more data, the better—[and] running them again and again, testing, comparing, and coming up with the best models"


## Keywords
* GPU Databases
* Data Streaming
* data warehousing
* in-memory database
* orchestrator
* unified model training process


## Creating and Veryfing Dataset
* https://blog.goodaudience.com/part-1-preparing-data-before-training-yolo-v2-and-v3-deepfashion-dataset-3122cd7dd884


## Road Analysis
video dataset for:
road segmentation
ego lane segmentation
lane instance segmentation

(1) noticing that driving the car is itself a form of annotation and that cars mostly travel along lanes
(2) propagating manual label adjustments from a single view to all images of the sequence
(3) accepting non-labelled parts in ambiguous situations

Previous lane detection work has focused on detecting the components of lane boundaries, and then applying clustering to identify the boundary as a whole

More recent methods use CNN based segmentation [2,4], and RNNs [11] for detecting lane boundaries.

However, visible lane boundaries can be interrupted by occlusion or worn markings, and by themselves are not associated with a specific lane instance.


### Datasets
* TuSimple
* NYC3DCars
* KITTI-Road
* Daimler Used
* Yotta
* Caltech Lanes
* Brook_Roberts_A_Dataset_for_ECCV_2018_paper - best


### [Brook_Roberts_A_Dataset_for_ECCV_2018_paper - best](https://five.ai/)
* https://five.ai/datasets
* A semi-automated annotation method for lane instances in 3D, requiring only inexpensive dash-cam equipment
* Road surface annotations in dense traffic scenarios despite occlusion
* Experimental results for road, ego-lane and lane instance segmentation using a CNN

#### Hardware & Setup
* standard Nextbase 402G dashcam recording at a resolution of 1920x1080 at 30 frames per second and compressed with the H.264 standard
* The camera was mounted on the inside of the car windscreen, roughly along the centre line of the vehicle and approximately aligned with the axis of motion

#### Data Acquisition
* remove parts where the car moves very slowly or stands still (which is common in urban environments)
* only included frames that are at least 1m apart according to the GPS
* split the recorded data into sequences of 200m in length, since smaller sequences are easier to handle (e.g. no need for key-frame bundle adjustment, and faster loading times)

#### Video Annotation
* The initial annotation step is automated and provides an estimate of the road surface in 3D space, along with an estimate for the ego-lane
* Then the estimates are corrected manually and further annotations are added in the road surface space. The labels are then projected into the 2D camera views, allowing the annotation of all images in the sequence at once

Given a dash-cam video sequence of N frames from a camera with unknown intrinsic and extrinsic parameters, the goal is to determine the road surface in 3D and project an estimate of the ego-lane onto this surface.

To this end, we first apply OpenSfM [29], a structure from motion algorithm, to obtain the 3D camera locations c i and poses R i for each frame i ∈ {1, ..., N } in a global coordinate system, as well as the camera projective transform P (·), which includes the estimated focal length and distortion parameters (R i ∈ R 3×3 are 3D rotation matrices)

OpenSfM reconstructions are not perfect, and failure cases are filtered during the manual annotation process.


#### Dataset Statistics and Split
* The full annotated set includes 402 sequences, 23, 979 images in total, and thus on average 60 images per sequence
* In total, there were 47,497 lane instances annotated, i.e. 118.2 per sequence
* Instance IDs are consistent across a sequence, i.e. consecutive frames will use the same instance ID for the same lane
* the annotators have been instructed to categorise each sequence according the scene type: urban, highway or rural
* We split the data into two sets, for training and testing. The train set comprises 360 sequences and a total of 21, 355 frames, while the test set includes 42 sequences and 2, 624 frames
* The test set was selected to include the same urban/motorway/rural distribution as the train set
* measured the average annotation time per scene type, and find that there is a large variation, with an urban scene taking roughly 3 times longer than a highway or countryside scene of similar length
  * This is due to the varying complexity in terms of the road layout, which is caused by various factors: the frequency of junctions and side roads, overall complexity of lane structure and additional features such as traffic islands and cycle lanes that are typically not found outside of an urban setting.
* Scene Type:
  * urban/motorway/rural
* Annotation type:
  * annotation density
  * non-road
  * road
  * ego-lane
  - #instances (per sequence) - mean/median/min/max
* Average annotation time in seconds
  - Scene type
  - per sequence
  - per image
* Agreement of the annotators
  * IoU, std, AP
* The annotation quality is measured through agreement between the two annotators on 12 randomly selected sequences.
* We measure the agreement on these overlapping labels via Intersection-over-Union (IoU) and agreement of instances using Average Precision (AP)

**Two segmentation tasks - Road and Ego-Lane Segmentation**
* Road/Non-Road detection (ROAD
* Ego/Non-Ego/Non-Road lane detection (EGO)


**baseline**
* used the well studied SegNet architecture, trained independently for both the EGO and ROAD experiments
* provide ROAD and EGO cross-database results for CityScapes (fine), Mapillary and KITTI Lanes
* For each dataset, we use 10% of training sequences for validation
* During training, we pre-process each input image by resizing it to have a height of 330px and extracting a random crop of 320 × 320px
* use the ADAM optimiser
* with a learning rate of 0.001 which we decay to 0.0005 after 25000 steps and then to 0.0001 after 50000 steps
* trained for 100, 000 training steps
* select the model with the best validation loss
* mini batch size was 2
* optimisation was performed on a per pixel cross entropy loss
* train one separate model per dataset and per task
* This leads to 4 models for ROAD, trained on our data, CityScapes (fine), Mapillary and KITTI Lanes. EGO labels are only available for the UM portion of KITTI Lanes and our data, hence we train 2 models for EGO
* For each model we report the IoU
* report the average IoU and F1 across classes for each task
* additionally the F1 score as it is the default for KITTI
* measure each model on held out data from every dataset
* For CityScapes and Mapillary the held out sets are their respective pre-defined validation sets
* The exception to this scheme is KITTI Lanes which is very small
and has no available annotated held out set.
* It should also be noted that the results are not directly comparable to the intended evaluation of CityScapes, Mapillary or KITTI Lanes due to the different treatment of the road occluded by vehicle:
* trend between the datasets:
  - Firstly, the highest IoUs are achieved when training and testing subsets are from the same data
  - This points to an overall generalisation issue; no dataset (including our own) achieves the same performance on other data.
  - The model trained on KITTI shows the worst cross-dataset average
    + This is not surprising, since it is also the smallest set (it contains only 289 images for the ROAD task and 95 images for the EGO task)
  - Cityscapes does better, but there is still a bigger gap to ours and Mapillary, probably due to lower diversity
  - Mapillary is similar to ours in size and achieves almost the same performance
  - The slightly lower results could be due to its different viewpoints, since it contains images taken from non-road perspectives, e.g. side-walks.
  - The current state of the art for instance segmentation on Cityscapes is MaskRCNN
  - Average Precision (AP) measures calculated as described for the MS-COCO [40] instance segmentation task
  - we calculate the AP across images and across IoU thresholds of detected lanes pixels assigned to embedding cluster centroids) and ground truth lanes. True and false positives are counted in the following way: (1) A detection is a true positive when it overlaps a ground truth instance with an IoU above some threshold and (2) a detection is a false positive when it does not sufficiently overlap any ground truth instance
