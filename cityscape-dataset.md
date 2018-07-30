/*
Title: Citiyscape Database Overview
Decription: Citiyscape Database Overview
Author: Bhaskar Mangal
Date:
Last updated: 30th-Jul-2018
Tags: Citiyscape Database Overview
*/

**Table of Contents**

[TOC]

## Citiyscape Databset, Scripts, Calibration Overview
This document mainly covers the details and content from these two documents regarding cityscape dataset, "Main PDF document" and "Supplement Reading for cityscape".

### References
* [Main PDF document](https://www.cityscapes-dataset.com/wordpress/wp-content/papercite-data/pdf/cordts2016cityscapes.pdf)
*[Supplement Reading for cityscape](https://www.cityscapes-dataset.com/wordpress/wp-content/papercite-data/pdf/cordts2016cityscapes-supplemental.pdf)
* [cityscapesScripts](https://github.com/mcordts/cityscapesScripts)
* [csCalibration.pdf](https://github.com/mcordts/cityscapesScripts/blob/master/docs/csCalibration.pdf)
* [dataset-overview](https://www.cityscapes-dataset.com/dataset-overview/)
* [fine annotations](https://www.cityscapes-dataset.com/examples/#fine-annotations)
* [coarse annotations](https://www.cityscapes-dataset.com/examples/#coarse-annotations)
* [Infactory calibration of multiocular camera systems](https://pdfs.semanticscholar.org/2938/6b5153b653a5246b9bdeaa4e05c758a92174.pdf)


### Tools
* [LabelMe: A database and web-based tool for image annotation](https://www.cs.ubc.ca/~murphyk/Papers/labelmeIJCV08.pdf)
* [Label Me: Web Annotation Tool](http://labelme.csail.mit.edu/Release3.0/)

### Other datasets & Image Parsing
* [MIT scene parsing challenge 2016](http://sceneparsing.csail.mit.edu/index_challenge.html)

### Other approaches & references
* [Semantic Instance Annotation of Street Scenes by 3D to 2D Label Transfer](http://www.cvlibs.net/publications/Xie2016CVPR.pdf)
* [Annotations of 3D Point Cloud](http://gfx.cs.princeton.edu/pubs/_2015_EIF/index.php)
 
### Summary
* Cityscape dataset is large-scale dataset tailored for autonomous driving in an urban environment. Autonomous cars implements different types of deep neural networks (DNNs) for decision making. DNNs require training; they are data hungry algorithms and thus require large and varied datasets for training to be more effective and accurate. Cityscape in the public domain plugs this gap along with others, but boosts to excel in terms of dataset size, annotation richness, scene variability, and complexity compared with other publicly available datasets like CamVid, Leuven, DUS, KITTI.


### Conclusion
People behind Cityscape dataset have documented details of their approach and process in concise manner. Looking into it has provided us with an insight on the annotation process & tools, effort-cost estimation, benchmark process and other details like annotation groups, classes, labeling policy, annotation tools, and data acquisition setup.
1. If we plan to publish part of our work to add to Cityscape or as a parallel project, it's advisable to extend their groups-classes definitions as they are carefully crafted to be compatible with other datasets.
2. To start the annotation process we need to focus on 'Road survey items' by extending their list with ours.
3. Further annotation tools used by them needs to be explored and to find commercial and open-source alternatives for the same.
4. Research on how the PCD annotations are carried, cost-effort estimation, tools available, storage and delivery options, projection of 3D annotations back to 2D etc.


### Notes
- Annotation classes, labeling policy may not be good enough for Indian Urban scene for instance challenges in particular for semantic modeling and labeling Indian road condition depends on consistency and availability of road markings, service roads, fragile boundaries between roads and curbs, sidewalks.
- In my view point we can look into cityscape dataset for inspiration, but evolve our own set of rules, conventions, annotation classifications, labeling policies.
- We need to understand benchmarking workflow and process.
- Developing benchmarking is out of the scope currently. It's required when using Deep learning neural networks or related technology to automate the annotations.
- Our focus should be particularly on Road survey items and their grouping/categorization, color encoding and attribution
- There are other smaller dataset available publically for urban scene understanding - KITTI Vision Benchmark Suite, CamVid, Leuven, Daimler Urban Segmentation, Caltech Pedestrian Dataset
- There are publically available image dataset for deep learning (Deep neural network training) ImageNet, PASCAL VOC, PASCAL-Context, Microsoft COCO
- pixelwise annotation of images at very large scale is labor-intensive and only little labeled data is available.
- It takes ~1.5hrs on average for a single image for pixelwise annotation & quality control
- Algorithms need to take a larger range of scales and object sizes into account to score well in our benchmark.


### Discussion minutes
Output of annotations needs to be delivered separately and specifically for 4 different targets, and are as given below:-
1. For Autonomous Car
2. For ADAS
3. For Web (WebGL)
4. For DNN ( Deep Neural Networks)


### Keywords
* DNN - Deep Neural Netowrks
* CNN - Convolutional Neural Network
* CRFs - Conditional Random Fields
* RNNs - Recurrent Neural Networks
* MCG - Multiscale Combinatorial Grouping


### What is Cityscape Dataset?
- It's a dataset for training Deep Neural Networks (DNN)
- It is a large-scale dataset to train and test approaches for pixel-level and instance-level semantic labeling, like object detection and deep learning approaches.
- It consists of diverse stereo video sequences created to develop semantic understanding of complex urban scene and streets from 50 different cities.
- Provides in-depth analysis of the dataset characteristics
- Provides performance evaluation of several state-of-the-art approaches based on their benchmark.
- Dataset size, annotation richness, scene variability, and complexity


### What are the other large-scale public datasets for DNN?
Following datasets allow deep neural networks to develop their full potential:-
- ImageNet
- PASCAL VOC
- PASCAL-Context
- Microsoft COCO


### What are the similar datasets like cityscape?
To develop understanding complex traffic scenes and driving scenarios, research can be linked to following datasets:-
- KITTI Vision Benchmark Suite
- CamVid
- Leuven
- Daimler Urban Segmentation
- Caltech Pedestrian Dataset

### How the urban scene datasets compared to cityscape dataset?
- They are smaller datasets
- More general settings
- do not fully capture the variability and complexity of real-world inner-city traffic scenes.
- Whereas, cityscape dataset is tailored for autonomous driving in an urban environment.


### What are the characteristics of cityscape dataset?
- Provides both pixel-level semantic labeling and instance-level semantic labeling in both annotations and evaluation metrics
- Provides depth information through stereo vision
- Recently published dataset for suburban traffic scenes
- Data recording and annotation methodology was designed to capture the high variability of outdoor street scenes
- Dataset over span of several months, covering spring, summer, and fall in 50 cities
- Mainly in Germany but also in neighboring countries


### Do we need to develop Internal Tools?
- We can look into cityscape annotation scripts for reference


### What needs to be annotated from the PCD and reference Images?
* We need to measure, analyze & geo-tag various assets of interest
- potholes
- speed breakers
- road/alert signs
- traffic signals
- overhead bridges
- lane markers
- road & lane widths
- speed profiles
- road borders
- guard rails
- distance tracking
- curvature tracking etc.

Following are the existing road survey items identified:-
- Road Edge / Curb
- Road Divider
- Road Markings	
- U- Turn
- Lay-by / Parking
- Traffic Signals
- Sign Board
- Lighting Column / Poles
- Trees
- Road Banner / Billboard
- Vehicles
- Buildings
- Naala / Lakes / River
- Footpath / Walking Path
- Pedestrian Crossing (over / Under)
- Roundabout
- Rail Track / Rail Gate
- Manhole / Pothole
- Speed Breaker
- Person / Animal / Birds


### Cityscape - Data Acquisition & Data Specifications
- Images were recorded with an automotive-grade 22 cm baseline stereo camera using 1/3 in CMOS 2 MP sensors (OnSemiAR0331) with rolling shutters at a frame-rate of 17 Hz.
- The sensors were mounted behind the windshield and yield high dynamic-range (HDR) images with 16 bits linear color depth.
- Each 16 bit stereo image pair was subsequently debayered and rectified
-  Extrinsic and Intrinsic calibration using traditional process:
  * [In-factory calibration of multiocular camera systems](https://pdfs.semanticscholar.org/2938/6b5153b653a5246b9bdeaa4e05c758a92174.pdf)
- To ensure calibration accuracy setup was recalibrated n-site before each recording session
- For comparability and compatibility with existing datasets they also provide low dynamic-range (LDR) 8 bit RGB images that are obtained by applying a logarithmic compression curve. Such tone mappings are common in automotive vision, since they can be computed efficiently and independently for each pixel.
- To facilitate highest annotation quality, they applied a separate tone mapping to each image. The resulting images are less realistic, but visually more pleasing and proved easier to annotate.
- 5000 images were manually selected from 27 cities for dense pixel-level annotation, aiming for high diversity of foreground objects, background, and overall scene layout.
- The annotations were done on the 20th frame of a 30-frame video snippet, which they provide in full to supply context information.
- For the remaining 23 cities, a single image every 20sec or 20m driving distance (whatever comes first) was selected for coarse annotation, yielding 20 000 images in total.
- Different data items provided as a part of cityscape dataset:-
1. Rectified 16 bit HDR and 8 bit LDR stereo image pairs
2. Corresponding annotations
3. Vehicle odometry
4. outside temperature
5. GPS tracks


### Classes and annotations
* [LabelMe: A database and web-based tool for image annotation](https://www.cs.ubc.ca/~murphyk/Papers/labelmeIJCV08.pdf)
- 5000 fine pixel-level annotations consist of layered polygons using Label Me web annotation tool.
- Annotation and quality control required more than 1.5 h on average for a single image.
- Annotators were asked to label the image from back to front such that no object boundary was marked more than once, thus implicitly providing depth ordering of the objects in the scene.
- The annotators were instructed to make use of the depth ordering and occlusions of the scene to accelerate labeling, analogously to LabelMe.
- Annotations can be easily extended to cover additional or more fine-grained classes
- 20 000 coarse pixel-level annotations, accuracy on object boundaries was traded off for annotation speed.
- Coarse annotation aim is to correctly annotate as many pixels as possible within a given span of less than 7 min of annotation time per image. This was achieved by labeling coarse polygons under the sole constraint that each polygon must only include pixels belonging to a single object class.
- 30 visual classes for annotation were defined, which are grouped into eight categories: flat, construction, nature, vehicle, sky, object, human, and void.

**Classes were selected:**
* based on their frequency
* Relevance from an application standpoint
* Practical considerations regarding the annotation effort
* To facilitate compatibility with existing datasets


#### Quality Control and Quality Assessment
- Refer main PDF document: cordts2016cityscapes.pdf


#### Dataset splits
- Annotated images are split into separate training, validation, and test sets
- Refer main PDF document: cordts2016cityscapes.pdf


#### Statistical analysis
- Comparison of cityscape with others based on:-
  * Annotation volume and density
  * The distribution of visual classes
  * Scene complexity
- CamVid (Cambridge) consists of ten minutes of video footage with pixel-wise annotations for over 700 frames.
- DUS (Heidelberg) consists of a video sequence of 5000 images from which 500 have been annotated
- KITTI (Karlsruhe)
- DUS and CamVid seem more aligned with Cityscapes


### How the annotations would be stored and delivered?


### Is grouping of different survey items required? If yes, define groups?


### What are the different attributes for each identified items? And, how are they will be stored?


### Design overview

#### References
* [dataset-overview](https://www.cityscapes-dataset.com/dataset-overview/)

#### Different Parameters
- Type of annotations
- The meta information provided
- The camera perspective
- The type of scenes and their size
- The selected datasets are either of large scale or focus on street scenes

#### Types of Annotations
Semantic, Instance-wise, Dense pixel annotations

#### Annotations classes and groups
* [fine annotations](https://www.cityscapes-dataset.com/examples/#fine-annotations)
* [coarse annotations](https://www.cityscapes-dataset.com/examples/#coarse-annotations)
* [Complete list of groups and classes](https://www.cityscapes-dataset.com/dataset-overview/)

- fine (5000 images) and coarse(20000 images) annotations
- group consists of classes; example - group 'flat' consists of classes - road, sidewalk, parking, rail track, where as the definition of the classes are as follows:-
- Total 30 classes
- Overlaid colors encode semantic classes

* Road
Part of ground on which cars usually drive, i.e. all lanes, all directions, all streets. Including the markings on the road. Areas only delimited by markings from the main road (no texture change) are also road, e.g. bicycle lanes, roundabout lanes, or parking spaces. This label does not include curbs.
* Sidewalk
Part of ground designated for pedestrians or cyclists. Delimited from the road by some obstacle, e.g. curbs or poles (might be small), not only by markings. Often elevated compared to the road. Often located at the sides of a road. This label includes a possibly delimiting curb, traffic islands (the walkable part), or pedestrian zones (where usually cars are not allowed to drive during day-time).
* parking (+)
Parking lots and driveways. Not for regular driving, but rather to park a vehicle. Different texture than road. In ambiguous cases where the driveway is not separated from the sidewalk (e.g. a building entrance), labeled as sidewalk.

* rail track (+)
All kind of rail tracks that are non-drivable by cars, e.g. subway and train rail tracks, while tram rail tracks are usually drivable by cars and therefore part of road.
* Single instance annotations are available. However, if the boundary between such instances cannot be clearly seen, the whole crowd/group is labeled together and annotated as group, e.g. car group.
+ This label is not included in any evaluation and treated as void (or in the case of license plate as the vehicle mounted on).


#### Labeling policy
- Foreground and background considerations e.g tree in front of a house or transparent car windows


### FAQs
- How to label the content of the scene semantically?
* Scene recognition - aims to determine the overall scene category
* Object-centric - detecting dynamic subset of scene constituents
* Scene labeling - identify the individual constituent parts of a whole scene and their interrelations


## Cityscape Calibration
As provided in the calibration pdf file of citiscape:-
1. Coordinate Systems
They defined three coordinate systems:
* (1) The vehicle coordinate system V according to ISO 8855 with the origin on the ground below of the rear axis center, x pointing in driving direction, y pointing left, and z pointing up;
* (2) The camera coordinate system C with the origin in the camera’s optical center and same orientation;
* (3) The image coordinate system I with the origin in the top-left image pixel, u pointing right, v pointing down.
2. Coordinate Transformation
Refer the pdf for equations

3. Parameters
- Extrinsic and intrinsic calibration parameters of the camera are provided in the folder camera.
- The camera translation parameters xextrinsic, yextrinsic, zextrinsic are given in meters.
- The rotational parameters yawextrinsic, pitchextrinsic, rollextrinsic in radians.
- The intrinsic parameters fx, fy, u0, v0 in pixels.
- Within the folder vehicle, they provided vehicle odometry consisting of speed [m/s] and yaw rate [rad/s] according to the vehicle coordinate system (V ).
- Further, they included the outside temperature [◦C], the GPS latitude [◦N], longitude [◦E], and heading [◦].
