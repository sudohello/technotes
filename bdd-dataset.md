
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


## Semantic Instance Segmentation
* data is mainly from the US
* fine-grained, pixel-level annotations for images from each of the 5,683 video clips randomly sampled from the whole dataset
* 40 object classes
* The whole set is split into 3 parts for:
  - training (3,683 images)
  - validation (500 images)
  - testing (1,500 images)
* We observe **long-tail effects** even on our dataset
  - There are almost 60,000 car instances, but only tens for trailer and train, and several hundreds for rider and motorcycle
  - presents a long-tail effect with more than 10 cars and poles per image, but only tens of trains in the whole dataset
* there is not much domain difference for the weather
* different time of the day and different scene types have large performance discrepancies - Domain Discrepancy Experiments with Faster-RCNN
* contains information on
  - weather conditions
  - daytime
  - scene location
* clear weather, city street and daytime are chosen as training domains
* the model trained on daytime performs poorly on the other time of the day, mainly nighttime, which indicates that **lighting is still an important factor for model transfer**
* Also, the model trained on city street images also performs poorly out-of-domain, mainly highway and residential area, which confirms that **context change is important for domain transfer**
* We find that there is a dramatic domain shift between Cityscapes and BDD dataset
  - Especially, because of infrastructure difference, the model trained on Cityscapes is confused by some simple categories such as sky and traffic signs
* We convert our semantic segmentation to label maps with training indices specified in Cityscapes
  - dilated residual networks which perform well on Cityscapes
  - use their pre-trained model on Cityscapes and and train the models with the same hyperparameters on BDD dataset
  - The performance drops significantly for objects that move on the road, such as riders and motorcycles
* **DRN-D-38** network
* contributions
  - 1) a robust video annotation system
  - 2) a comprehensive large-scale driving dataset with extensive annotations
  - comprehensive annotations that are necessary for a complete driving system


## Lanes and Drivable Area

* **Lanes**
  - Red lanes are vertical and blue lanes are parallel
  - (a) We label all the visible lane boundaries
  - (b) Not all marking edges are lanes for vehicles to follow, such as pedestrian crossing
  - (c) Parallel lanes can also be along the current driving direction
  - methodology behind our choices for lane annotation
    + Usually, the continuity of a lane marking is essential for making a “driving-across” decision, so we labeled it independently as an important attribute
    + Similarly, the direction of a lane marking is also significant for autonomous driving
    + For example:
      * if a lane marking is parallel to the passing car, it may serve to guide cars and separate lanes
      * if it is vertical, it can be treated as a sign of deceleration or stop
* **Drivable Area**
  - **Conditions beyond lane markings direct our driving decisions, and are relevant for designing autonomous driving algorithms:**
  - Lanes alone are not sufficient to decide road affordability for driving
  - Although most of the time, the vehicle should stay between the lanes, it is common that no clear lane marking exists
  - In addition, the road area is shared with all other vehicles
  - A lane can not be driven on if occupied
  - The drivable area is divided into two different categories
  - **directly drivable area**
    + red regions are directly drivable
    + ”directly drivable area” defines the area that the driver is currently driving on – it is also the region where the driver has priority over other cars or the “right of the way”
  - **alternatively drivable area**
    + blue ones are alternative
    + “alternatively drivable are” is a lane the driver is currently not driving on, but could do so – via changing lanes
    + Although drivable areas can be confined within lane markings, they are also related to locations of other vehicles
  - Although the directly and alternatively drivable areas are visually indistinguishable, they are functionally different, and requires potential algorithms to recognize blocking objects and scene context
  - on highway or city street, where traffic is closely regulated, drivable areas are mostly within lanes and they do not with the vehicles or objects on the road
  - in residential areas, the lanes are sparse and annotators can judge what is drivable based on the surroundings



**Drivable area prediction by segmentation**
* The segmentation predicts the drivable area with lanes
* the segmentation model learns to interpolate in areas that has no lane markings
* the drivable area detection is converted to 3-way segmentation task (background, directly, and alternatively drivable) by ignoring the region ID
* trained **DRN-D-22** model on the **70000 training images**
  - the model learns to split the road according to the lanes and extrapolate the drivable area to unmarked space
  - The mIoU for directly and alternatively drivable areas is 77.6% and 59.7%, respectively
  - However, the same model achieves 94.4% IoU on road segmentation which indicates that techniques beyond segmentation may be required to solve the drivable area problem



