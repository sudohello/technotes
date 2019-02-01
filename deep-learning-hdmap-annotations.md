
# A picture is worth a thousand words - So Tell The Story Right!
> Introduction to Computer Vision AI in HD Map creation

"A picture is worth a thousand words", an idiom is highly relevant in the context of AI and never before the importance of this phrase could have been understood by an AI Engineer, given the recent breakthroughs of Deep Learning techniques in Computer Vision. Many people like me have been fallen in love with the Computer Vision AI. We are no where near to human cognition, but it has started to tickle our grey matters and I believe that someday we would achieve this human machine dream.

A picture can tell a story of different things, and the story teller can narrate it in innumerable ways if not infinite. And, that's the extact challange the AI Engineer face it today when trying to train machines which can be as intelligent as human.

The tactical item in front of an AI Engineer is to find out on what task of computer vision, the person has to ask the team to annotate for **'learning by example'** methodology, confusingly referred as 'supervised training'.

And this was the exact problem in front of me when I need to create the annotation workflow for using AI in High Definition (HD) Map creation.


[TOC]



## “All I Got To Do Is Tell The Story Right”!

That's the motivation, when one can tell many things about and from a single street image, one needs to find out the extact question for which there's less ambiguity in answering and understanding by most of the people. Asking different types of question gives a different story line and one can narrate at length the nuts and bolts of the level of details in a street image. Setting the tone i.e. the context of story is what makes it interesting for the audience.

In other words, asking the specific questions on the kind of business problem in HD Map creation AI can be used to solve, and what problems to be taken first, what kind of investment is needed and what MoV (Measured Organisation Value) it would bring on the table i.e. faster, cheaper, efficient or growth; last but not the least are these efforts and invements are sustainiable in future when skilled resource hiring, retention and secluded nature of work poses high risks to justify such huge investment from the company's perspective.

So, it started with the identification of potential applications of Artifical Intellegience in GIS for HD Map creation by looking at the working examples, researches. Usecases emerged for instance extracting 3D geometries like road edges, lane markings; providing clipped and segmented images that can be coorelated with the gis point map objects like traffic sign, pole, signage etc.; extract text and symbols from the road imageries; building footprint, road, pois, green cover extractions from satellite and/or drone images; semantic image search from lakhs of images, rooftop shape detection and extraction and so on.

And, we'd all the raw materials, satellite images, street image sequences (mono and stereo), video routes and point cloud data (PCD) generated from traditional SfM techniques, 3D annotations on PCD as point, line for geographics features, sensor data (IMU, CAN, GPS) collected and processed from our custom rig; handcrafted 3D building models at LoD-2.3 and LoD-5 and all of this data is georeferenced. Finally, myself to tickle the AI neurons with single machine with 8 GB 1080 Nvidia, 32 GB Ram, 2TB HDD having lakhs of driving image sequences. The quest for me was to find out, how to use Deep Learning techniques to get something meaningful out of these gigs of street images (to start with) that can be used for creation of High Definition Maps for self-driving cars.

With the few months of effort able to get some grasp of solving computer vision tasks such as classification, detection and segmentation using deep learning techniques. I explored different architectures and zeroed on to Mask RCNN, then, state of art for instance segmentation focused on accuracy rather than response time. Also explored and experimented with annotation tools & process, commercial vision APIs & annotation services, cloud infrastructure, technology stack & deep learning frameworks - both open source & proprietry and different popular datasets for urban scene undertanding, selfdriving car dataset (only images) and common objects; of course basis of ML and DL. Deep Learning techniques for detection and segmentation were kind of reached some SotA (State of the Art) benchmarks that seems good enough for us to adapt and they have also shown huge potential on SLAM, SfM, single and setero image to 3D, depth maps; also, shown good results directly on computer vision tasks on 3D datasets; and many of these were experimented in house to come to arrive to an understanding and certain conclusions for a creating a sustaining AI programme in GIS.


With these insights, as the next step, I need to indentify of objects in street images for annotating for computer vision tasks. I segregated them into two stages for identification of street objects as **stage-1** and **stage-2**, based on the maturity of deep learning techniques and complexity where:
* **stage-1**
  - detection/segmentation of map specific objects, ex: pole, tree, traffic-sign that can be mapped to point objects
  - probable usecase is used to create new map layers like traffic sign, green cover.
* **stage-2**
  - geometric extraction like line, polygon with higher precision than humans with 3D/depth output that can be used directly to create maps
  - road specific geometries edges, curbs, lanes etc
  - Deep Learning has huge potential but so far old school SfM is still best for outdoor scenes for 2D to 3D

Further, relevance of identified categories must map to following 3 classification:-
1. HD Map dataset
2. Self-driving car dataset
3. Unknown

## **Datasets of Interest (DoI)**
We looked into details 8 key public datasets

### Types of Dataset
In the public domain, there exists mainly 2 types of datasets **self-driving** and **urban scene**. We came up with the criteria to mark the clear differentiator to be classified as either of these as there seems to be a confusion in the references available in wild.

**Self-driving Car (Autonomy) vs Urban Scene Difference Criteria**

| Self-driving Car (Autonomy)                                 | Urban Scene                                           |
|:------------------------------------------------------------|:------------------------------------------------------|
| * Contains images only from the driver's perspective        | contains from walking, and non-road scene perspective |
| * Outdoor images only                                       | Outdoor images only                                   |
| * contains sequential camera frames                         | not a pre-condition                                   |
| * can be aumgented with other sequential camera sensor data | cannot be agumented with sequential sensor data       |


**References**
* [Deep Learning Datasets And Creation](deep-learning-datasets-and-creation.md)
* [Self Driving Car Datasets Semantic Segmentation](https://blog.playment.io/self-driving-car-datasets-semantic-segmentation/)
* [Worlds Largest Driving Dataset](https://blog.getnexar.com/introducing-bdd100k-the-worlds-largest-driving-dataset-b4e157bf2632)
* [Semantic Segmentation Datasets List](https://github.com/mrgloom/awesome-semantic-segmentation#datasets)


### **Common Objects**
1. [MS COCO - things, stuff, panoptic](mscoco-dataset.md)
  * **[MS COCO](http://cocodataset.org/#home)**
  * [what-object-categories-labels-are-in-coco-dataset](https://tech.amikelive.com/node-718/what-object-categories-labels-are-in-coco-dataset/)

### **Self-Driving-Car Datasets Semantic Segmentation**
2. [ApolloScape](apolloscape-dataset.md)
  * **[ApolloScape](http://apolloscape.auto/index.html)**
3. [BDD](bdd-dataset.md)
  * **[BDD100K - Berkeley DeepDrive](https://bdd-data.berkeley.edu/)**
4. [IDD - Indian Driving Dataset](idd-dataset.md)
5. [KITTI](http://www.cvlibs.net/datasets/kitti/)
  * **[KITTI Dataset](http://www.cvlibs.net/datasets/kitti/)**

### **Scene understanding Datasets**
6. [Cityscape](cityscape-dataset.md)
  * **[CityScapes Dataset](https://www.cityscapes-dataset.com/)**
  * https://www.cityscapes-dataset.com/dataset-overview/
7. [MVD - Mapillary](mapillary-dataset.md)
  * **[Mapillary Vista Dataset: MVD](https://blog.mapillary.com/product/2017/05/03/mapillary-vistas-dataset.html)**
8. [ADE20K](ade20k-dataset.md)
  * **[ADE20K Dataset](http://groups.csail.mit.edu/vision/datasets/ADE20K/)**


## Comparission of datasets (CoD) Analysis

Once, I'd the higher level understanding and framework to identify the categories for specific computer vision tasks, the next challange was to come up with the object labels a.k.a. categories and category hierarchy such that it leverage common understanding of public dataset in urban scene and self-driving and common objects. The motivation for doing so are:
- as creating a huge dataset on which be able to do hyper-tuning is expensive, one should be able to cross-train across public-datasets with in house created categories for building expertise on hyper tuning; hyper-tuning on small datasets would results in overfitting
- quantitevely able to measure the quality of annotations by annotators, which is by comparing the stats with the benchmarks
- possibility to provide public datasets with the same labels of public datasets, without compromising our own unique labels
- develope intution on how the labels should be allocated by deducing some pattern
- finding relevance of these labels with the Indian street scene context
- understanding the annotation tools used, format in which these annotations stored, retrival and visualizing the created annotations
- at the sametime, look from the perspective of cmmerical AI annotation service provider
- possibilities on AI assisted annotation
- extension to other type of computer vision tasks annotations like keypoint, polygon, point, 2D cuboid for images, videos and point cloud data


In nutshell, listed Category Hierarchy, Annotation Tools, Annotaiton Storage formats etc. for identified Computer Vision Tasks (detection and instance segmentation).

1. **Documentation of Category Hierarchy for publically available Computer Vision Datasets for AI**
  * Document the object hierarchy (along with the id, categlory label etc) in an excel sheet for following types of datasets:
    * Common Objects
    * Self-Driving-Car
    * Scene understanding
2. **Documentation Of AI Annotation Tools**
  * ai annotation tool used
  * annotation storage format
3. **Category Challange**
  * Internal task to come up with the category labels from our own datasets
4. **Comparision And Mapping Of Category Hierarchy - Internal & External**
  * category and category hierarchy used
  * conventions on storing and releasing the ai datasets
  * different types of ai annotations on same images i.e. specific to computer vision tasks
5. **Analyse and propose the category label and hierarchy**
  * key crietria is that one should be able to cross-train across public-datasets with new categories ex: using cityscape dataset with new vehicle types specific to Indian context


### Analysis on Datasets of Interest (DoI)

Approach:
* normalization of labels for comparission
  - singular and plural form are considered as same e.g. vechile in cityscape and vechiles in idd are considered as same
  - converted to lowercase
  - spaces were replaced with underscore
* category hierarchy were identified from DoI and first compared at L0 level(referring as top or generic level), with L1, L2,...,Ln are more specific as we go futher down
* frequency distribution of labels based on alphabatical order were noted for at least two matches
* kitti, cityscape, idd, mapillary, apolloscape, coco_stuff, coco_things were compared at L0 and labels are put into consequtive columns in excel sheet
* each label is manually alphabatically sorted in the excel sheet, such that only the common label across all columns (i.e. datasets) remain in the same line
* L0 frequency distribution:


| Frequency 		    | Letter | Label Name       |
|:------------------|:-------|:-----------------|
| 2                 | a      | animal           |
|                   | b      | building         |
|                   | r      | roadside_objects |
| 3                 | c      | construction     |
|                   | f      | flat             |
|                   | h      | human            |
|                   | o      | object           |
| 4                 | n      | nature           |
|                   | v      | vehicle          |
|                   |        | void             |
| 5                 | s      | sky              |

* After comparing at L0 level, the last leaf node of category hierarchy from each datasets were compared i.e. Ln
* created a new criteria for L0 level such that when compared L0 and Ln across datasets, if Ln from any of the dataset is matching to the L0 of at least one dataset, it's considered as L0 in the new heirarchy levels
* L0 Label is assigned a 'starting alphapet letter' to indicate it's considered as the L0 label in the new heirarchy
* L0 and Ln compare and new heirarchy pattern evolved:


| L0 Label   | L0+n Label         | Frequency |
|:-----------|:-------------------|:----------|
| a          | animal             | 3         |
| b          | building           | 6         |
|            | banner             | 2         |
|            | bench              | 2         |
|            | bicycle            | 6         |
|            | billboard          | 4         |
|            | bridge             | 4         |
| c          | construction       | 3         |
|            | car                | 6         |
|            | caravan            | 4         |
|            | curb-cut           | 2         |
|            | drivable           | 2         |
|            | dynamic            | 2         |
| e          | ego_vehicle        | 2         |
| f          | flat               | 4         |
|            | fence              | 6         |
| g          | ground             | 3         |
|            | guard_rail         | 4         |
| h          | human              | 3         |
|            | mountain           | 2         |
|            | motorcycle         | 6         |
| n          | nature             | 4         |
| o          | object             | 3         |
| p          | person             | 5         |
|            | pole               | 5         |
|            | parking            | 4         |
| r          | roadside_objects   | 2         |
|            | road               | 6         |
|            | rail_track         | 3         |
|            | rider              | 5         |
| s          | sky                | 6         |
|            | sidewalk           | 5         |
|            | static             | 2         |
|            | street_light       | 2         |
|            | tree               | 2         |
|            | terrain            | 3         |
|            | traffic_sign_frame | 2         |
|            | traffic_light      | 6         |
|            | traffic_sign       | 4         |
|            | traffic_cone       | 2         |
|            | trash_can          | 2         |
|            | truck              | 6         |
|            | train              | 2         |
|            | trailer            | 2         |
|            | tunnel             | 4         |
| u          | unlabeled          | 3         |
| v          | vehicle            | 5         |
| v          | void               | 4         |
|            | vegetation         | 5         |
| w          | water              | 2         |
|            | wall               | 5         |


### Conclusions
Following conclusions were drawn:-

1. VGG Via annotation is the web based simplest tool meeting our requirements, probably few enhancements are needed to adopt to the factory setup.
2. scalable's computer vision task specific annotation nature is interesting and relevant for the workflow
3. Researchers develope their own annotation tool and workflow and hence process is still evolving
4. Opensource AI annotation tools in public domain is in nacent stage with firt such good tool available in year 2016
5. PASCAL VOC (imagenet), MS COCO, VGG are common formats in which AI annotations are stored and generally used as industry standard
6. Images and annotations are stored separately at the same level of directory structure


## Key Indicators on Workflow (KIW)
1. Labeling policy, workflow should evolve with clear instructions is required, with the ability to flag exceptions
2. Workflow needs to be Iterative process to be able to consume annotations on a daily basis rather than wait for a week or months to get them to the AI training desk. And, such process should be scriptable rather than manual management.
3. Quantificaion from the begining of the workflow: task allocation, productivity of annotator, quality of annotations by each annotator, quality specifications and benchmarks for the annotations needs to be evolved.
4. Quick visualization and stats on the annotations per image per release etc should be done once using scripts. Manual process is time consuming and error prone and not sustainable over months. This is essential from the understanding of dataset mix and creating splits for AI training on a continous basis. 
5. Trade off between quality of expected prediction and usability in HD Map creation from AI machine output w.r.t. input annotations in terms annotation quality, time and cost needs to be understood. This is essential in terms of MoVs, setting the right expectations, and to measure the success of AI programme.


## New Labeling Scheme, Annotation process and Workflow
Based on this analysis I was able to come up with the new genric heirarchy for annotation process, where following are the core foundation ideas:

- Singluar form of label to be used
- lowercase and instead of space usded underscore to separate two words in a label
- Optimal label name has to be selected i.e.
	- less ambigious in nature
	- not too generic and not too specific
- providing additional attribution at the annotation level and at the image level provides the oppotunity for cover complex scenarios without re-labelling 
	- For instance, classification of a type of object should not be the part of the label name rather as the annotation attribute, ex: label is person but the same can be classified as pedistrian, rider, cyclist in additional attribution property Truncated, Marking are some of the identified annotation attributes
- Additional annotation attributes can provide an opportunity to create dynamic labelling scheme to create unquie labels for AI datasets if rquired
- Annotation_Quality, Collection_Type, Behaviour_Or_Activity, Position  Velocity, Acceleration, Orientation, Material, Text, Usability, Occulusion, 
- File level /Image attributions are also created: Scene_Type, Weather_Condition, View_Point, Image_Quality
- time-cost-matrix is created as a tool for decision making
- category_hierarchy, labelling_policy, annotation_job, annotation_task_details, classification details were defined clearly
- For each labels visual clip icon and image clipped sample needs to be provided as a annotation aid in the tool
- Before that, in the category_hierarchy google image search was done to get the intitution
  - based on the image samples what I got I further fine tunned the label names till I get expected output
  - I found out that, we as human have general conception in the Indian context but has more than one meaning
  - examples of ambigious label:
    + junction_box changed to roadside_junction_box
    + tanker changed to road_tanker
- I also identified the labels which are highly specific to Indian Context and majority of them were under Vechiles
- Finally, provided the following annotation_job:
  * object_detection_segmentation - ods
    * with fine Annotation_Quality for Annotation_Type of bbox and polygon for 32 categories spanning accross 3 L0 hierarchy
  * object_recognition_classification - orc
    * traffic_sign, pole and booth
* these jobs assigned as annotation_tasks to each annotators
* release management and directories were sorted out


## HDM - High Definition Map Dataset
Over the time this dataset what we would probably be released as **High Definition Map** dataset

### HDM Category Hierarchy

* Three level category hierarchy
* singular form
* First letter is in capital
* separated by underscore
* Each L1 has label at L2 same as the L1 label to provide a fallback in case of ambiguity
* Void is ultimate fallback case
* Unlabeled is the last resort when cannot be put under void either
* this category hierarchy tree provides the conceptual framework to cover 100% pixels for complete Urban scene segmentation
* out of these HDM category were further shortlisted


**L0 and L1**

|             |        |                |         |         |         |              |         |          |              |
|:------------|:-------|:---------------|:--------|:--------|:--------|:-------------|:--------|:---------|:-------------|
| Living      |        |                |         |         |         |              |         |          |              |
|             | Human  | Animal         | Reptile | Rodent  | Bird    |              |         |          |              |
|             |        |                |         |         |         |              |         |          |              |
| Non_Living  |        |                |         |         |         |              |         |          |              |
|             | Object | Structure      | Place   | Surface | Road    | Road_Marking | Vehicle | Building | Construction |
|             |        |                |         |         |         |              |         |          |              |
| Hand_Signal |        |                |         |         |         |              |         |          |              |
|             |        |                |         |         |         |              |         |          |              |
| Nature      |        |                |         |         |         |              |         |          |              |
|             |        |                |         |         |         |              |         |          |              |
|             | Sky    | Water          | Earth   | Fire    | Terrain | Vegetation   | Snow    |          |              |
|             |        |                |         |         |         |              |         |          |              |
| Void        |        |                |         |         |         |              |         |          |              |
|             | Void   | Loose_Material |         |         |         |              |         |          |              |
|             |        |                |         |         |         |              |         |          |              |
| Unlabeled   |        |                |         |         |         |              |         |          |              |
