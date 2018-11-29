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


## Types of Image Annotations and Applications
* Semantic Segmentation
* This is especially the case for pixel-wise prediction tasks such as semantic segmentation, used in applications such as autonomous driving, robotics, and image search.



## Datasets and Data Creation for Training Machines


## Creation for Training Machines


## Image Labeling / Annotation Tools
* **VGG VIA**
  * https://github.com/ox-vgg/via - simple, intutive, best
    - http://www.robots.ox.ac.uk/~vgg/blog/author/abhishek-dutta.html
    - http://www.robots.ox.ac.uk/~vgg/software/via/
    - http://www.robots.ox.ac.uk/~vgg/software/via/via-1.0.6.html
    - http://www.robots.ox.ac.uk/~vgg/blog/vgg-image-annotator.html
  * VGG VIA tool saves the annotations in a JSON file, and each mask is a set of polygon points
  * No documentation for the format, but it’s pretty easy to figure out by looking at the generated JSON
* **labelImg**
  * https://github.com/tzutalin/labelImg
    - `git clone https://github.com/tzutalin/labelImg.git`
* **commacoloring**
  * https://github.com/commaai/commacoloring
  * https://commacoloring.herokuapp.com/
  * based on `js-segment-annotator`
* **js-segment-annotator**
  * https://github.com/kyamagu/js-segment-annotator
  * http://kyamagu.github.io/js-segment-annotator/?view=index
* **LabelBox**
  * https://github.com/Labelbox/Labelbox/blob/master/LICENSE
  * https://www.labelbox.com/
  * https://github.com/Labelbox/Labelbox/tree/master/custom-interfaces/classification
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
* **ImageSegmentation**
  * https://github.com/AKSHAYUBHAT/ImageSegmentation
  * https://www.eraseimage.com/
* **CoCo UI**
  * https://github.com/tylin/coco-ui
  * The tool used to annotate the COCO dataset.
* **Color Extractor**
  * **ColorThief - get dominant color in an image**
    * https://www.abeautifulsite.net/how-to-get-the-dominant-colors-of-an-image-with-javascript
    * https://lokeshdhakar.com/projects/color-thief/
    * [javascript] - https://github.com/lokesh/color-thief
    * [PHP] - https://github.com/ksubileau/color-thief-php
  * https://ourcodeworld.com/articles/read/403/top-5-best-image-color-extraction-javascript-and-jquery-plugins
* **Vector Editors**
  * http://teselagen.github.io/openVectorEditor/#/Editor
* **Listing of Tools**
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
2. [Mapillary](mapillary-dataset.md)
3. [ApolloScape](apolloscape-dataset.md)
4. [MS COCO](mscoco-dataset.md)


### **Extensive List of Datasets**
- https://projet.liris.cnrs.fr/voir/wiki/doku.php?id=datasets
- https://handong1587.github.io/computer_vision/2015/09/24/datasets.html
- https://www.analyticsvidhya.com/blog/2018/03/comprehensive-collection-deep-learning-datasets/
- https://martin-thoma.com/sota/
- SotA - State of the Arts

* **Imagenet**
  - http://www.image-net.org/
  - http://image-net.org/download-API
  - http://image-net.org/download
* **OpenImages**
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
* **MS COCO**
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
* **PASCAL VOC**
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
* ApolloScape
* FCAV
  * Driving in the Matrix: Can Virtual Worlds Replace Human-Generated Annotations for Real World Tasks?
  - https://arxiv.org/abs/1610.01983
  - https://fcav.engin.umich.edu/safety-pilot-dataset
  - https://fcav.engin.umich.edu/sim-dataset
  - https://github.com/umautobots/driving-in-the-matrix
  - https://github.com/umautobots/GTAVisionExport


### 3D Datasets
- Matterport 
  - https://hackernoon.com/announcing-the-matterport3d-research-dataset-815cae932939
  - https://matterport.com/blog/2017/09/20/announcing-matterport3d-research-dataset/
  - https://niessner.github.io/Matterport/
  - https://arxiv.org/pdf/1709.06158.pdf
- Trimble 3D Warehouse
- Yobi3D
- ShapeNet - Semantic annotation knowledge bases
  * https://drive.google.com/file/d/1Z8gt4HdPujBNFABYrthhau9VZW10WWYe/view

### Others
- https://en.wikipedia.org/wiki/List_of_datasets_for_machine_learning_research
* Free datasets are available from places like Kaggle.com and UCI. 
  - https://www.kaggle.com/datasets
  - https://archive.ics.uci.edu/ml/datasets.html

## Dataset Pre-processing
* http://shubhagrawal.in/2016/10/13/machine-learning-data-preprocessing/

## Dataset Creation
After working hard to collect your images and annotating all the objects, you have to decide what format you’re going to use to store all that info. 
* https://venturebeat.com/2018/10/22/googles-fluid-annotation-uses-ai-to-speed-up-image-dataset-annotation/
* Labeling a single pic in the popular Coco+Stuff dataset, for example, takes 19 minutes; tagging the whole dataset of 164,000 images would take over 53,000 hours.

## Fluid Annotation
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

## TBD
* https://www.kaggle.com/learn/machine-learning
* https://github.com/CPFL/Autoware
* https://maptools.tier4.jp/
* http://www.aisantec.co.jp/english/
* http://shubhagrawal.in/2016/08/01/creating-launcher-for-any-executable-file-linux/
* http://home.bharathh.info/
