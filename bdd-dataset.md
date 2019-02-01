
---
Title: BDD100K Dataset Overview
Decription: BDD100K Dataset Overview
Author: Bhaskar Mangal
Date: 09th-Jan-2019
Last updated: 09th-Jan-2019
Tags: BDD100K Dataset Overview
---


**Table of Contents**
* TOC
{:toc}


## [Berkeley Deepdrive](https://deepdrive.berkeley.edu/)
**Abstract**
* Driving imagery is becoming plentiful, but annotation is slow and expensive, as annotation tools have not kept pace with the flood of data. Our first contribution is the design and implementation of a scalable annotation system that can provide a comprehensive set of image labels for large-scale driving datasets
* new driving dataset, facilitated by tooling, which is an order of magnitude larger than previous efforts, and is comprised of over 100K videos with diverse kinds of annotations including image level tagging, object bounding boxes, drivable areas, lane markings, and full-frame instance segmentation.
* The dataset possesses geographic, environmental, and weather diversity, which is useful for training models so that they are less likely to be surprised by new conditions

* comprehensive annotations that are necessary for a complete driving system
* Like Mapillary Vista Dataset, our data is crowdsourced, however, our dataset is collected solely from drivers, with each annotated image corresponding to a video se-
quence, which enables some interesting applications for modeling temporal dynamics.

suitable for
all kinds of annotations needed in a driving database, such as
* bounding box
* semantic instance segmentation
* lane detection


Many open source annotation tools are
targeted to one specific task, such as single object classification or vehicle/pedestrian
detection, however, no existing open source tool is available to support various types of
annotations for such a large driving database.


* annotation work must be easily accessible to workers
* the annotation progress needs to be monitorable
* concurrent annotation sessions need to be supported.

* Bezier curve
* Copy shared boundaries
  - function to automatically duplicate shared boundaries and make it possible for a
polygon to share boundaries with its neighbors
  - For example, when drawing a polygon A, if A’s boundary partly overlaps with poly-
gon B, which has already been drawn, the annotator can let the system automatically
generate the shared boundary by clicking on two desired endpoints. In addition, ade-
quate visual feedback is also implemented to smooth out the annotation process. The
copy shared boundary feature not only provides unique and cleaner boundaries between
adjacent objects, but also reduces the annotation time significantly. According to the our
user study, in which annotators were asked to label 20 images with 842 polygons, the
time to draw a polygon was reduced by 36% on average when using this technique
* Extensibility
  - Vision tasks are mostly about regrouping pixels on the images and assigning semantic
meanings to them
    - For example, when only the object location and extent are needed,
bounding boxes are easier to annotate and recognize
* six weather conditions, six scene types, and three distinct times of day, for each image
* uch diversity enables us to study domain transfer and generalize our object detection model well on new test sets
* Image Tagging
  - **Weather**
    + Clear
    + Partly Cloudy
    +  Overcast
    +  Rainy
    +  Snowy
    +  Foggy
  - **Scene**
    + Residential
    + Highway
    + City street
    + Parking Lot
    + Gas Stations
    + Tunnel
  - **Hours**
    + Dawn/Dusk
    + Daytime
    + Night
* Attributes: truncation, occlusion, and traffic light color
  - **Occlusion**
    + Occluded
    + Not
  - **Truncation**
    + Truncated
    + Not
  - The light colors of all traffic lights are identified
* many different scene types
  * crowded
  * persons per image
  * total number of unique persons
  * pedestrians
* Lane
  * The lane marking detection is critical for vision-based vehicle localization and trajectory planing
  * Distribution of different types of lanes and drivable areas
  * Lanes alone are not sufficient to decide road affordability for driving.
  * A lane can not be driven on if occupied
  * Lane category - 8 main categories with attributes of continuity and direction
    - Road Curb
    - Double White
    - Double Yellow
    - Double Other
    - Single White
    - Single Yellow
    - Single Other
    - Crosswalk
  * Lane direction
    - Parallel
    - Vertical
  * Lane continuity
    - Full
    - Dashed
  * Drivable areas
    - Drivable
    - Alternative
* **semantic instance segmentation**


## BDD100K Dataset
* https://github.com/ucbdrive/bdd-data
* https://bair.berkeley.edu/blog/2018/05/30/bdd/


**Toolkit**
* https://github.com/ucbdrive/bdd-data


* **Dataformat**
* https://github.com/ucbdrive/bdd-data/blob/master/doc/format.md


## Annotation Tool
* https://www.scalabel.ai
* https://www.scalabel.ai/doc/create-project.html


## References
* http://classif.ai/dataset/berkeley-deepdrive-video/
* https://github.com/gy20073/BDD_Driving_Model/