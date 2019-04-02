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


## Generate MS COCO style dataset
* https://stackoverflow.com/questions/45545187/create-ms-coco-style-dataset
* https://patrickwasp.com/create-your-own-coco-style-dataset/
* https://github.com/jsbroks/imantics
* https://patrickwasp.com/create-your-own-coco-style-dataset/

## [Ms COCO Dataset](http://cocodataset.org/#home) Overview
* http://cocodataset.org/#home
* Back in 2014 Microsoft created a dataset called COCO (Common Objects in COntext) to help advance research in object recognition and scene understanding.
* COCO is a large-scale object detection, segmentation, and captioning dataset. COCO has several features:
* COCO was one of the first large scale datasets to annotate objects with more than just bounding boxes, and because of that it became a popular benchmark to use when testing out new detection models.
* The format COCO uses to store annotations has since become a de facto standard, and if you can convert your dataset to its style, a whole world of state-of-the-art model implementations opens up.

**Annotations Includes:**
* Object segmentation (pixel-level)
* Recognition in context
* Superpixel stuff segmentation
* keypoint annotations for person instances
* 330K images (>200K labeled)
* 1.5 million object instances
* 80 object categories
* 91 stuff categories
* 5 captions per image
* 250,000 people with keypoints

**Different Tasks**
* object detection with bounding boxes and segmentation masks
  * focuses on **thing classes** (person, car, elephant)
* joint detection and person keypoint estimation
  * requires localization of person keypoints in challenging, uncontrolled conditions. The keypoint challenge involves simultaneously detecting people and localizing their keypoints (person locations are not given at test time).
* stuff segmentation
  * focuses on **stuff classes** (grass, wall, sky)
* Scene Semantic Segmentation
  * focuses on to segment the image into object and stuff categories


**Different Challanges**

* **COCO Detection Challenge**
  * [2017](http://cocodataset.org/#detection-2017)
* **COCO Keypoint Challenge**
  * [2017](http://cocodataset.org/#keypoints-2017)
* **COCO Stuff Challenge**
  * [2017](http://cocodataset.org/#stuff-2017)
* **Places Challenges**
  * [2017](http://cocodataset.org/#stuff-2017)
    * (1) scene parsing
    * (2) instance segmentation
    * (3) semantic boundary detection
      * Semantic Boundary Detection is to detect the boundaries of each object instance in the images
      * Boundary detection is relevant to edge detection, but focuses more on the association of boundary and their object instances


**Download**
* http://cocodataset.org/#download

**talks**
* https://places-coco2017.github.io/

**Labels in Coco Dataset**
* [what-object-categories-labels-are-in-coco-dataset](https://tech.amikelive.com/node-718/what-object-categories-labels-are-in-coco-dataset/)



* **Performance**
The performance of the algorithms will be evaluated on:
  * the **mean of pixel-wise accuracy**
  * the **Intersection over Union (IoU) averaged over all individual categories**
*  **Evaluation Metrics:**
  * Average Precision (AP)
  * F-measure at optimal dataset scale (F-ODS)
  * Class accuracy
  * Pixel accuracy
  * Mean IOU
  * FW IOU


### Object Detection: **detection task**
* Bounding Box, Instance Segmentation
* [Task](http://cocodataset.org/#detection-2018)
  * the object detection task addresses thing classes (person, car, elephant)
* [Evaluation](http://cocodataset.org/#detection-eval)
* the categories field of the annotation structure stores the mapping of category id to category and supercategory names
* the list of objects for the 2014 and 2017 releases are the same, which are **80 objects from the original 91 object categories in the paper**
* https://github.com/amikelive/coco-labels
* For **2014**, use "train", "val", "minival", or "valminusminival"
* For **2017**, only "train" and "val" annotations are available



### Stuff Segmentation: **Stuff Segmentation Task**
* https://github.com/nightrome/cocostuff
* https://github.com/nightrome/cocostuffapi
* http://cocodataset.org/#stuff-2018
  * The COCO Stuff Segmentation Task is designed to push the state of the art in semantic segmentation of stuff classes
  * this task focuses on stuff classes (grass, wall, sky)
* http://cocodataset.org/#stuff-eval
* COCO-Stuff augments all 164K images of the popular COCO [2] dataset with pixel-level stuff annotations. These annotations can be used for scene understanding tasks like semantic segmentation, object detection and image captioning.
* **91 stuff classes**
* Stuff covers about 66% of the pixels in COCO
* It allows to explain important aspects of an image, including scene type; which thing classes are likely to be present and their location; as well as geometric properties of the scene
* To be compatible with COCO, COCO-Stuff has **91 thing classes (1-91)**, **91 stuff classes (92-182)** and **1 class "unlabeled" (0)**
* **11 of the thing classes of COCO** do not have any segmentation annotations **(blender, desk, door, eye glasses, hair brush, hat, mirror, plate, shoe, street sign, window)**
* The classes **desk**, **door**, **mirror** and **window** could be **either stuff** or **things** and therefore occur in both COCO and COCO-Stuff. To avoid confusion suffix is added **"-stuff"** or **"-other"** to those classes in COCO-Stuff
* Full list of classes in stuff: [Labels in COCO-Stuff](https://github.com/nightrome/cocostuff/blob/master/labels.md)

* https://github.com/nightrome/cocostuff10k#annotation-tool

### Panoptic Segmentation
* http://cocodataset.org/#panoptic-2018
* The definition of **'panoptic'** is **"including everything visible in one view"**
* goal of advancing the state of the art in scene segmentation
* Panoptic segmentation addresses both stuff and thing classes, unifying the typically distinct semantic and instance segmentation tasks.
* http://cocodataset.org/#panoptic-eval
* concept:
  * things are countable objects such as people, animals, tools - **object detections**
  * Stuff classes are amorphous regions (i.e. Lacking definite form; shapeless; no particular type; anomalous; Lacking organization; formless) of similar texture or material such as grass, sky, road

### Keypoint Detection


### Text Recognition
* https://vision.cornell.edu/se3/coco-text-2/


### **COCO and Mapillary Joint Recognition**
* https://research.mapillary.com/eccv18/



## **Image Augmentation**
* https://github.com/aleju/imgaug `pip3 install imgaug`


## Data Format
* http://cocodataset.org/#format-data


### Explore MS COCO dataset


### [pycococreator](https://github.com/waspinator/pycococreator/)
* https://github.com/waspinator/pycococreator/
* pycococreator takes care of all the annotation formatting details and will help convert your data into the COCO format
* the whole reason we’re trying to make a COCO dataset isn’t because it’s the best way of representing annotated images, but because everyone else is using it.


### [pycocotools](https://github.com/cocodataset/cocoapi)
* [pycoco - with fix from crowdAI](https://github.com/crowdai/coco)
* **Note:** If you are using `Python3.*`, then there are chances that pycocotools will not work for you. In that case, install it from this fork :
```bash
pip3 install git+https://github.com/crowdai/coco.git#subdirectory=PythonAPI
```


**waleedka**
Download and install the Python COCO tools from https://github.com/waleedka/coco
That's a fork from the original https://github.com/pdollar/coco with a bug fix for Python 3. I submitted a pull request https://github.com/cocodataset/cocoapi/pull/50
If the PR is merged then use the original repo.
Note: Edit PythonAPI/Makefile and replace "python" with "python3".


### [panopticapi](https://github.com/cocodataset/panopticapi)
* **COCO panoptic segmentation is stored in a new format; Unlike COCO detection format** that stores each segment independently, COCO panoptic format stores all segmentations for an image in a single PNG file. This compact representation naturally maintains non-overlapping property of the panoptic segmentation.

**Converters**
* Mainly interested for conversion from **coco detection format** to **coco panoptic format** and vice-versa
* https://github.com/cocodataset/panopticapi/blob/master/CONVERTERS.md
* Note that panoptic segmentation does not allow different segments to overlap
* From COCO detection format to COCO panoptic format
* From COCO panoptic format to COCO detection formats


**Issues**
* https://github.com/cocodataset/cocoapi/issues/181
* https://github.com/facebookresearch/Detectron/issues/100
* https://github.com/cocodataset/panopticapi/issues/2
```bash
## colors fix
git clone https://github.com/mangalbhaskar/panopticapi.git
##
python converters/panoptic2detection_coco_format.py \
  --input_json_file $AI_DATA/data/ms-coco/annotations/panoptic_val2017.json \
  --output_json_file $AI_DATA/data/ms-coco/annotations/panoptic_instances_val2017.json \
  --segmentations_folder $AI_DATA/data/ms-coco/panoptic_val2017
```
* Error:
```bash
Traceback (most recent call last):
  File "converters/panoptic2detection_coco_format.py", line 152, in <module>
    args.things_only)
  File "converters/panoptic2detection_coco_format.py", line 118, in convert_panoptic_to_detection_coco_format
    category.pop('color')
KeyError: u'color'
```
* viz
```bash
python visualization.py --colors \
 --input_json_file $AI_DATA/data/ms-coco-1/annotations/panoptic_val2017.json \
 --segmentations_folder $AI_DATA/data/ms-coco-1/panoptic_val2017 \
 --img_folder $AI_DATA/data/ms-coco-1/val2017
```

### **Annotation Keys**

**coco things - 2014, 2017; coco stuff 2017**
```bash
ann: dict_keys(['segmentation', 'area', 'iscrowd', 'image_id', 'bbox', 'category_id', 'id'])
```
* coco things 2014
  * `annotations/instances_val2014.json`
  * `annotations/instances_train2014.json`
  * `annotations/instances_minival2014.json`
  * `annotations/instances_valminusminival2014.json`
* coco things 2017
  * `annotations/instances_val2017.json`
  * `annotations/instances_train2017.json`
* coco stuff 2017
  * `annotations/stuff_val2017.json`
  * `annotations/stuff_train2017.json`


**coco panoptic 2017**
* `annotations/panoptic_train2017.json`
  ```bash
  ann: dict_keys(['segments_info', 'file_name', 'image_id'])
  ```
* classes (BG is not part of the spec, only there as as part of running it with mask-rcnn)
  ```bash
  Classes: ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush', 'banner', 'blanket', 'bridge', 'cardboard', 'counter', 'curtain', 'door-stuff', 'floor-wood', 'flower', 'fruit', 'gravel', 'house', 'light', 'mirror-stuff', 'net', 'pillow', 'platform', 'playingfield', 'railroad', 'river', 'road', 'roof', 'sand', 'sea', 'shelf', 'snow', 'stairs', 'tent', 'towel', 'wall-brick', 'wall-stone', 'wall-tile', 'wall-wood', 'water-other', 'window-blind', 'window-other', 'tree-merged', 'fence-merged', 'ceiling-merged', 'sky-other-merged', 'cabinet-merged', 'table-merged', 'floor-other-merged', 'pavement-merged', 'mountain-merged', 'grass-merged', 'dirt-merged', 'paper-merged', 'food-other-merged', 'building-other-merged', 'rock-merged', 'wall-other-merged', 'rug-merged']
  Total Classes: 134
```



### **Class Names and corresponding Ids**
* http://cocodataset.org/#download
* Download **train2014**
  ```bash
  wget -c http://images.cocodataset.org/annotations/annotations_trainval2014.zip
  wget -c http://images.cocodataset.org/zips/train2014.zip
  wget -c http://images.cocodataset.org/zips/val2014.zip
  wget -c https://dl.dropboxusercontent.com/s/s3tw5zcg7395368/instances_valminusminival2014.json.zip?dl=0
  wget -c http://images.cocodataset.org/zips/test2014.zip
  wget -c http://images.cocodataset.org/annotations/image_info_test2014.zip
  ```
* Download **train2017**: Stuff
  * https://github.com/nightrome/cocostuff
    ```bash
    wget -c http://images.cocodataset.org/zips/train2017.zip
    wget -c http://images.cocodataset.org/zips/val2017.zip  
    wget -c http://images.cocodataset.org/zips/test2017.zip
    wget -c http://images.cocodataset.org/annotations/image_info_test2017.zip
    #
    ## Stuff+thing PNG-style annotations on COCO 2017 trainval
    wget -c http://calvin.inf.ed.ac.uk/wp-content/uploads/data/cocostuffdataset/stuffthingmaps_trainval2017.zip
    ## Stuff-only COCO-style annotations on COCO 2017 trainval
    wget -c http://calvin.inf.ed.ac.uk/wp-content/uploads/data/cocostuffdataset/stuff_trainval2017.zip

    ## stuff_annotations_trainval2017
    wget -c http://images.cocodataset.org/annotations/stuff_annotations_trainval2017.zip
    ## Thing-only COCO-style annotations on COCO 2017 trainval
    wget -c http://images.cocodataset.org/annotations/annotations_trainval2017.zip
    ## 2017 Panoptic Train/Val annotations
    wget -c http://images.cocodataset.org/annotations/panoptic_annotations_trainval2017.zip
    ```
* To get the list of class names, you'd load the dataset
* The model classifies objects and returns class IDs, which are integer value that identify each class. Some datasets assign integer values to their classes and some don't.
* For example, in the MS-COCO dataset, the 'person' class is 1 and 'teddy bear' is 88. The IDs are often sequential, but not always. The COCO dataset, for example, has classes associated with class IDs 70 and 72, but not 71.
* For details on class names and corresponding ids refer:
  * https://github.com/crowdAI/mapping-challenge-starter-kit.git
    * `[Dataset Utils.ipynb](https://github.com/crowdAI/mapping-challenge-starter-kit/blob/master/Dataset%20Utils.ipynb)`
    * This list is generated using the above code for **train2014** dataset: [mscoco-dataset-segmentation-categories.md](mscoco-dataset-segmentation-categories.md)


## **Create you Own `COCO type annotation` dataset**
* https://www.programcreek.com/python/example/94653/pycocotools.coco.COCO
* https://patrickwasp.com/create-your-own-coco-style-dataset/
* COCO uses JSON (JavaScript Object Notation) to encode information about a dataset
* There are several variations of COCO, depending on if its being used for **object instances**, **object keypoints**, or **image captions** 
* object instances format which goes something like this:
```json
{
 "info": "info",
 "licenses": ["license"],
 "categories": ["category"],
 "images": ["image"],
 "annotations": ["annotation"]
}
```
* The “info”, “licenses”, “categories”, and “images” lists are straightforward to create, but the “annotations” can be a bit tricky
* describe our dataset using python lists and dictionaries and later export them to json.
```python
INFO = {
    "description": "Example Dataset",
    "url": "https://github.com/waspinator/pycococreator",
    "version": "0.1.0",
    "year": 2018,
    "contributor": "waspinator",
    "date_created": datetime.datetime.utcnow().isoformat(' ')
}

LICENSES = [
    {
        "id": 1,
        "name": "Attribution-NonCommercial-ShareAlike License",
        "url": "http://creativecommons.org/licenses/by-nc-sa/2.0/"
    }
]

CATEGORIES = [
    {
        'id': 1,
        'name': 'square',
        'supercategory': 'shape',
    },
    {
        'id': 2,
        'name': 'circle',
        'supercategory': 'shape',
    },
    {
        'id': 3,
        'name': 'triangle',
        'supercategory': 'shape',
    },
]
```
* All we have to do is loop through **each image jpeg** and its **corresponding annotation pngs** and let pycococreator generate the correctly formatted items
* There are two types of annotations COCO supports, and their format depends on whether the annotation is of a single object or a “crowd” of objects.
* Single objects are encoded using a list of points along their contours, while crowds are encoded using column-major RLE (Run Length Encoding).
* RLE is a compression method that works by replaces repeating values by the number of times they repeat. For example `0 0 1 1 1 0 1`  would become `2 3 1 1`. Column-major just means that instead of reading a binary mask array left-to-right along rows, we read them up-to-down along columns.
* The tolerance option in pycococreatortools.create_annotation_info() changes how precise contours will be recorded for individual objects. The higher the number, the lower the quality of annotation, but it also means a lower file size. `2` is usually a good value to start with.


## annotations
* things - pycocotools
  * createIndex: 
  * dict_keys(['info', 'licenses', 'images', 'type', 'annotations', 'categories'])
  * `dataset['info']`
    * {'description': 'COCO 2014 Dataset', 'url': 'http://cocodataset.org', 'version': '1.0', 'year': 2014, 'contributor': 'COCO Consortium', 'date_created': '2017/09/01'}
  * `dataset['licenses']`
    ```json
    [
      {
        "url": "http://creativecommons.org/licenses/by-nc-sa/2.0/",
        "id": 1,
        "name": "Attribution-NonCommercial-ShareAlike License"
      },
      {
        "url": "http://creativecommons.org/licenses/by-nc/2.0/",
        "id": 2,
        "name": "Attribution-NonCommercial License"
      },
      {
        "url": "http://creativecommons.org/licenses/by-nc-nd/2.0/",
        "id": 3,
        "name": "Attribution-NonCommercial-NoDerivs License"
      },
      {
        "url": "http://creativecommons.org/licenses/by/2.0/",
        "id": 4,
        "name": "Attribution License"
      },
      {
        "url": "http://creativecommons.org/licenses/by-sa/2.0/",
        "id": 5,
        "name": "Attribution-ShareAlike License"
      },
      {
        "url": "http://creativecommons.org/licenses/by-nd/2.0/",
        "id": 6,
        "name": "Attribution-NoDerivs License"
      },
      {
        "url": "http://flickr.com/commons/usage/",
        "id": 7,
        "name": "No known copyright restrictions"
      },
      {
        "url": "http://www.usa.gov/copyright.shtml",
        "id": 8,
        "name": "United States Government Work"
      }
    ]
    ```
  * `dataset['annotations'][0].keys()`
    * dict_keys(['segmentation', 'area', 'iscrowd', 'image_id', 'bbox', 'category_id', 'id'])
    * iterate through all annotations
    * create **image_to_annotation map** i.e. image_id maps to annotation hash
    * create **annotation_map** i.e. annotation_id maps to annotation hash
  * `dataset['images'][0].keys()`
    * dict_keys(['license', 'url', 'file_name', 'height', 'width', 'date_captured', 'id'])
    * create **image_map** i.e. image_id maps to image hash
  * `dataset['categories'][0].keys()`
    * dict_keys(['supercategory', 'id', 'name'])
    * create **category_map** i.e. category_id to category hash
  * `dataset['annotations'][0].keys()` and `dataset['categories'][0].keys()`
    * iterate over annotations
    * create **category_to_image_map** i.e. annotation['category_id'] maps to annotation['image_id']

  * Crowd types are stored with a flad iscrowd; and dynamically negatiave class ID is used
   # Is it a crowd? If so, use a negative class ID.
                if annotation['iscrowd']:
                    # Use negative class ID for crowds
                    class_id *= -1
## Misc
* https://github.com/adiprasad/unsup-hard-negative-mining-mscoco

