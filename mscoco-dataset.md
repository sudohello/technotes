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


## [Ms COCO Dataset](http://cocodataset.org/#home) Overview
* http://cocodataset.org/#home
* Back in 2014 Microsoft created a dataset called COCO (Common Objects in COntext) to help advance research in object recognition and scene understanding.
* COCO is a large-scale object detection, segmentation, and captioning dataset. COCO has several features:
* COCO was one of the first large scale datasets to annotate objects with more than just bounding boxes, and because of that it became a popular benchmark to use when testing out new detection models.
* The format COCO uses to store annotations has since become a de facto standard, and if you can convert your dataset to its style, a whole world of state-of-the-art model implementations opens up.

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


## **COCO and Mapillary Joint Recognition**
* https://research.mapillary.com/eccv18/

## Text Recognition
* https://vision.cornell.edu/se3/coco-text-2/

## coco-stuff
* https://github.com/nightrome/cocostuff
* COCO-Stuff augments all 164K images of the popular COCO [2] dataset with pixel-level stuff annotations. These annotations can be used for scene understanding tasks like semantic segmentation, object detection and image captioning.



## [pycococreator](https://github.com/waspinator/pycococreator/)
* https://github.com/waspinator/pycococreator/
* pycococreator takes care of all the annotation formatting details and will help convert your data into the COCO format
* the whole reason we’re trying to make a COCO dataset isn’t because it’s the best way of representing annotated images, but because everyone else is using it.

## **Create you Own COCO type annotation dataset**
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