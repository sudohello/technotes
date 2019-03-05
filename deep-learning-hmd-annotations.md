--
Title: HMD (HD Map Database) Category Hierarchy
Description: HMD (HD Map Database) Category Hierarchy
Author: Bhaskar Mangal
Date: 29th-Jan-2019
Last updated: 05th-Mar-2019
Tags: HMD (HD Map Database) Category Hierarchy
---

**Table of Contents**
* TOC
{:toc}

[TOC]

## HMD (HD Map Database) Category Hierarchy
> Conceptual Framework


* Three level category hierarchy
* singular form
* First letter is in capital
* separated by underscore
* Each L1 has label at L2 same as the L1 label to provide a fallback in case of ambiguity
* Void is ultimate fallback case
* Unlabeled is the last resort when cannot be put under void either
* this category hierarchy tree provides the conceptual framework to cover 100% pixels for complete Urban scene segmentation and self-driving car
* out of these HMD category were further shortlisted
* Actual Label vs classification label - Actual label names should not communicate classification type for examples:
  * actual label would be 'person' and it can be further classified as based on certain attribution as rider, motorcyclist, pedestrian, hawker
  * likewise: traffic_sign (different types), pole (electric, high_tension, telephone) and booth (phone, traffic_police, dairy, pan_shop, tent_shop, coconut)
* Annotation attributions would further provide an option to classify labeled object and provide other metadata too
  * Annotation_Quality, Collection_Type, Behaviour/Activities, Position, Velocity, Acceleration, Orientation, Material, Text, Usability, Occlusion, Truncated Marking
* Image File attributions provides other type of metadata
  * Scene_Type, Weather_Condition, View_Point, Image_Quality


**L0,L1: hierarchy for HMD Dataset**

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



**L0,L1,L2: complete hierarchy for HMD Dataset**
* the numbers indicates the frequency of occurrence in the DoI (Datasets of Interest) which were analyzed and compared at L0 and Ln levels.


|   |                 |   |                       |   |                        |   |                  |   |              |   |               |   |                                 |   |                             |   |                        |   |                       | 
|---|-----------------|---|-----------------------|---|------------------------|---|------------------|---|--------------|---|---------------|---|---------------------------------|---|-----------------------------|---|------------------------|---|-----------------------| 
|   | **Living**      |   | **Human**             |   | **Animal**             |   | **Reptile**      |   | **Rodent**   |   | **Bird**      |   |                                 |   |                             |   |                        |   |                       | 
|   |                 | 3 | human                 | 3 | animal                 |   | reptile          |   | rodent       |   | bird          |   |                                 |   |                             |   |                        |   |                       | 
|   |                 |   | pedestrian            |   | cow                    |   | snake            |   | rat          |   | pigeon        |   |                                 |   |                             |   |                        |   |                       | 
|   |                 | 5 | rider                 |   | dog                    |   |                  |   | squirrel     |   | crow          |   |                                 |   |                             |   |                        |   |                       | 
|   |                 |   | motorcyclist          |   | cat                    |   |                  |   |              |   |               |   |                                 |   |                             |   |                        |   |                       | 
|   |                 | 5 | person                |   | goat                   |   |                  |   |              |   |               |   |                                 |   |                             |   |                        |   |                       | 
|   |                 |   | hawker                |   | sheep                  |   |                  |   |              |   |               |   |                                 |   |                             |   |                        |   |                       | 
|   |                 |   | traffic_police_person |   | horse                  |   |                  |   |              |   |               |   |                                 |   |                             |   |                        |   |                       | 
|   |                 |   | cyclist               |   | camel                  |   |                  |   |              |   |               |   |                                 |   |                             |   |                        |   |                       | 
|   |                 |   |                       |   |                        |   |                  |   |              |   |               |   |                                 |   |                             |   |                        |   |                       | 
|   | **Non_Living**  |   | **Object**            |   | **Structure**          |   | **Place**        |   | **Surface**  |   | **Road**      |   | **Road_Marking**                |   | **Vehicle**                 |   | **Building**           |   | **Construction**          | 
|   |                 | 3 | object                |   | structure              |   | place            |   | surface      | 6 | road          |   | road_marking                    | 5 | vehicle                     | 6 | building               | 3 | contruction           | 
|   |                 | 2 | banner                | 4 | bridge                 |   | parking_lot      | 4 | flat         |   | road_pile     |   | yellow_line                     | 6 | bicycle_or_cycle            |   | theater                |   | construction_material | 
|   |                 | 2 | bench                 | 4 | guard_rail             |   | auto_stand       | 3 | ground       |   | road_obstacle |   | white_line:continious:right     | 6 | car                         |   | parlour                |   | construction_site     | 
|   |                 | 4 | billboard             | 3 | rail_track             | 4 | parking          |   | parking      |   |               |   | white_line:continious:left      | 4 | caravan                     |   | spa                    |   |                       | 
|   |                 | 5 | pole                  | 5 | sidewalk               |   | playfield        |   | hump         |   |               |   | white_line:broken:right         | 2 | ego_vehcile                 |   | medical_store          |   |                       | 
|   |                 | 2 | street_light          | 4 | tunnel                 |   | garbage_dumpyard |   | pothole      |   |               |   | white_line:broken:left          | 6 | motorcycle_or_bike          |   | bank                   |   |                       | 
|   |                 |   | roadside_spot_light   | 4 | wall                   |   |                  |   | speed_braker |   |               |   | white_line:broken:lane_marking  |   | train                       |   | hotel                  |   |                       | 
|   |                 | 2 | traffic_sign_frame    | 2 | curb_cut               |   |                  |   | manhole      |   |               |   | white_line:continious:stop_line |   | truck                       |   | fruit_stall            |   |                       | 
|   |                 | 6 | traffic_light         |   | curb                   |   |                  |   |              |   |               |   | road_marker                     | 2 | trailer                     |   | convention_hall        |   |                       | 
|   |                 | 4 | traffic_sign          |   | platform               |   |                  |   |              |   |               |   | zebra_crossing                  |   | van                         |   | cricket_stadium        |   |                       | 
|   |                 | 2 | traffic_cone          |   | bus_stop_platform      |   |                  |   |              |   |               |   |                                 |   | jeep                        |   | temple                 |   |                       | 
|   |                 |   | traffic_pole          |   | metro_station_platform |   |                  |   |              |   |               |   |                                 |   | cement_truck                |   | art_gallery            |   |                       | 
|   |                 |   | flyover_pillar        |   | skywalk_platform       |   |                  |   |              |   |               |   |                                 |   | auto_rikshaw                |   | school                 |   |                       | 
|   |                 |   | wire                  |   | flyover_playform       |   |                  |   |              |   |               |   |                                 |   | tractor                     |   | college                |   |                       | 
|   |                 | 2 | garbage_can           |   | compound               |   |                  |   |              |   |               |   |                                 |   | ego_vehicle                 |   | park                   |   |                       | 
|   |                 |   | building_name_board   |   | height_restriction     |   |                  |   |              |   |               |   |                                 |   | invalid_carriage            |   | public_toilet          |   |                       | 
|   |                 |   | tower                 |   | junction               |   |                  |   |              |   |               |   |                                 |   | motorcycle_rig              |   | atm                    |   |                       | 
|   |                 |   | vehicle_number_plate  |   | round_about            |   |                  |   |              |   |               |   |                                 |   | sidecar                     |   | electric_power_station |   |                       | 
|   |                 |   | barrigade             |   | divider                |   |                  |   |              |   |               |   |                                 |   | hawker_cart                 |   | metro_station          |   |                       | 
|   |                 |   | reflector             |   | ramp                   |   |                  |   |              |   |               |   |                                 |   | tanga                       |   | polic_station          |   |                       | 
|   |                 |   | drainage_cap          |   | overpass               |   |                  |   |              |   |               |   |                                 |   | bullock_cart                |   | milk_dairy             |   |                       | 
|   |                 |   | transformer           |   | underpass              |   |                  |   |              |   |               |   |                                 |   | camel_cart                  |   |                        |   |                       | 
|   |                 |   |                       |   | footpath               |   |                  |   |              |   |               |   |                                 |   | pulled_rikshaw              |   |                        |   |                       | 
|   |                 |   | signage               |   | tollgate               |   |                  |   |              |   |               |   |                                 |   | ambulance                   |   |                        |   |                       | 
|   |                 |   | solar_panel           |   | petrol_bunk            |   |                  |   |              |   |               |   |                                 |   | tempo_traveller_or_mini_bus |   |                        |   |                       | 
|   |                 |   |                       |   | bus_bay                |   |                  |   |              |   |               |   |                                 |   | goods_van                   |   |                        |   |                       | 
|   |                 |   | cctv_camera           |   | auto_stand             |   |                  |   |              |   |               |   |                                 |   | traffic_police_jeep         |   |                        |   |                       | 
|   |                 |   |                       |   | gate                   |   |                  |   |              |   |               |   |                                 |   | luggage_auto                |   |                        |   |                       | 
|   |                 |   | roadside_junction_box | 6 | fence                  |   |                  |   |              |   |               |   |                                 |   | lorry                       |   |                        |   |                       | 
|   |                 |   | booth                 |   | grill                  |   |                  |   |              |   |               |   |                                 |   | petrol_carrier              |   |                        |   |                       | 
|   |                 |   | tent                  |   | statue                 |   |                  |   |              |   |               |   |                                 |   | fire_brigade                |   |                        |   |                       | 
|   |                 |   | speed_sensor          |   | support                |   |                  |   |              |   |               |   |                                 |   | jcb                         |   |                        |   |                       | 
|   |                 |   | umbrella              |   | pavement               |   |                  |   |              |   |               |   |                                 |   | road_tanker                 |   |                        |   |                       | 
|   |                 |   | airplane              |   | railing                |   |                  |   |              |   |               |   |                                 |   | petrol_tanker               |   |                        |   |                       | 
|   |                 |   | luggage               |   | roof                   |   |                  |   |              |   |               |   |                                 |   | water_tanker                |   |                        |   |                       | 
|   |                 |   | accessory             |   | clock_tower            |   |                  |   |              |   |               |   |                                 |   | lorry_tiffer                |   |                        |   |                       | 
|   |                 |   | net                   |   |                        |   |                  |   |              |   |               |   |                                 |   | volvo_bus                   |   |                        |   |                       | 
|   |                 |   | kite                  |   |                        |   |                  |   |              |   |               |   |                                 |   | cycle_rikshaw               |   |                        |   |                       | 
|   |                 |   | garbage_pile          |   |                        |   |                  |   |              |   |               |   |                                 |   | tvs_luna_mopet              |   |                        |   |                       | 
|   |                 |   |                       |   |                        |   |                  |   |              |   |               |   |                                 |   | garbage_trolley             |   |                        |   |                       | 
|   |                 |   |                       |   |                        |   |                  |   |              |   |               |   |                                 |   | garbage_truck               |   |                        |   |                       | 
|   |                 |   |                       |   |                        |   |                  |   |              |   |               |   |                                 |   |                             |   |                        |   |                       | 
|   | **Hand_Signal** |   |                       |   |                        |   |                  |   |              |   |               |   |                                 |   |                             |   |                        |   |                       | 
|   |                 |   |                       |   |                        |   |                  |   |              |   |               |   |                                 |   |                             |   |                        |   |                       | 
| 4 | **Nature**      |   | **Sky**               |   | **Water**              |   | **Earth**        |   | **Fire**     |   | **Terrain**   |   | **Vegetation**                  |   | **Snow**                        |   |                        |   |                       | 
|   |                 | 6 | sky                   | 2 | water                  |   | stone            |   | fire         | 3 | terrain       | 5 | vegetation                      |   |                             |   |                        |   |                       | 
|   |                 |   | cloud                 |   | river                  |   | rock             |   |              | 2 | mountain      |   | grass                           |   |                             |   |                        |   |                       | 
|   |                 |   |                       |   | sea                    |   | soil             |   |              |   | desert        |   | plant                           |   |                             |   |                        |   |                       | 
|   |                 |   |                       |   |                        |   | mud              |   |              |   | hill          |   | flower                          |   |                             |   |                        |   |                       | 
|   |                 |   |                       |   |                        |   | stone            |   |              |   |               |   | leaf                            |   |                             |   |                        |   |                       | 
|   |                 |   |                       |   |                        |   | debris           |   |              |   |               |   | dry_leaf                        |   |                             |   |                        |   |                       | 
|   |                 |   |                       |   |                        |   | gravel           |   |              |   |               |   | potted_plant                    |   |                             |   |                        |   |                       | 
|   |                 |   |                       |   |                        |   | sand             |   |              |   |               | 2 | tree                            |   |                             |   |                        |   |                       | 
|   |                 |   |                       |   |                        |   |                  |   |              |   |               |   | tree_leaf_branch                |   |                             |   |                        |   |                       | 
|   |                 |   |                       |   |                        |   |                  |   |              |   |               |   | tree_trunk                      |   |                             |   |                        |   |                       | 
|   |                 |   |                       |   |                        |   |                  |   |              |   |               |   | branch                          |   |                             |   |                        |   |                       | 
|   |                 |   |                       |   |                        |   |                  |   |              |   |               |   | moss                            |   |                             |   |                        |   |                       | 
|   |                 |   |                       |   |                        |   |                  |   |              |   |               |   |                                 |   |                             |   |                        |   |                       | 
|   | **Void**        |   | **Void**              |   | **Loose_Material**     |   |                  |   |              |   |               |   |                                 |   |                             |   |                        |   |                       | 
|   |                 | 4 | void                  |   | loose_material         |   |                  |   |              |   |               |   |                                 |   |                             |   |                        |   |                       | 
|   |                 |   | fog                   |   | garbage                |   |                  |   |              |   |               |   |                                 |   |                             |   |                        |   |                       | 
|   |                 |   | smoke                 |   |                        |   |                  |   |              |   |               |   |                                 |   |                             |   |                        |   |                       | 
|   |                 |   | dust                  |   |                        |   |                  |   |              |   |               |   |                                 |   |                             |   |                        |   |                       | 
|   |                 |   |                       |   |                        |   |                  |   |              |   |               |   |                                 |   |                             |   |                        |   |                       | 
| 3 | **Unlabeled**   |   |                       |   |                        |   |                  |   |              |   |               |   |                                 |   |                             |   |                        |   |                       | 



# A picture is worth a thousand words - So Tell The Story Right!
> Introduction to Computer Vision AI in HD Map creation

"A picture is worth a thousand words", an idiom is highly relevant in the context of AI and never before the importance of this phrase could have been understood by an AI Engineer, given the recent breakthroughs of Deep Learning techniques in Computer Vision. Many people like me have been fallen in love with the Computer Vision AI. We are no where near to human cognition, but it has started to tickle our grey matters and I believe that someday we would achieve this human machine dream.

A picture can tell a story of different things, and the story teller can narrate it in innumerable ways if not infinite. And, that's the exact challenge the AI Engineer face it today when trying to train machines which can be as intelligent as human.

The tactical item in front of an AI Engineer is to find out on what task of computer vision, the person has to ask the team to annotate for **'learning by example'** methodology, confusingly referred as 'supervised training'.

And this was the exact problem in front of me when I need to create the annotation work-flow for using AI in High Definition (HD) Map creation.


## “All I Got To Do Is Tell The Story Right”!

That's the motivation, when one can tell many things about and from a single street image, one needs to find out the exact question for which there's less ambiguity in answering and understanding by most of the people. Asking different types of question gives a different story line and one can narrate at length the nuts and bolts of the level of details in a street image. Setting the tone i.e. the context of story is what makes it interesting for the audience.

In other words, asking the specific questions on the kind of business problem in HD Map creation AI can be used to solve, and what problems to be taken first, what kind of investment is needed and what MoV (Measured Organization Value) it would bring on the table i.e. faster, cheaper, efficient or growth; last but not the least are these efforts and investments are sustainable in future when skilled resource hiring, retention and secluded nature of work poses high risks to justify such huge investment from the company's perspective.

So, it started with the identification of potential applications of Artificial Intelligence in GIS for HD Map creation by looking at the working examples, researches. Use-cases emerged for instance extracting 3D geometries like road edges, lane markings; providing clipped and segmented images that can be correlated with the GIS point map objects like traffic sign, pole, signage etc.; extract text and symbols from the road imageries; building footprint, road, pois, green cover extractions from satellite and/or drone images; semantic image search from lakhs of images, rooftop shape detection and extraction and so on.

And, we'd all the raw materials, satellite images, street image sequences (mono and stereo), video routes and point cloud data (PCD) generated from traditional SfM techniques, 3D annotations on PCD as point, line for geographic features, sensor data (IMU, CAN, GPS) collected and processed from our custom rig; handcrafted 3D building models at LoD-2.3 and LoD-5 and all of this data is georeferenced. Finally, myself to tickle the AI neurons with single machine with 8 GB 1080 Nvidia, 32 GB Ram, 2TB HDD having lakhs of driving image sequences. The quest for me was to find out, how to use Deep Learning techniques to get something meaningful out of these gigs of street images (to start with) that can be used for creation of High Definition Maps for self-driving cars.

With the few months of effort able to get some grasp of solving computer vision tasks such as classification, detection and segmentation using deep learning techniques. I explored different architectures and zeroed on to Mask RCNN, then, state of art for instance segmentation focused on accuracy rather than response time. Also explored and experimented with annotation tools & process, commercial vision APIs & annotation services, cloud infrastructure, technology stack & deep learning frameworks - both open source & propriety and different popular datasets for urban scene understanding, self-driving car dataset (only images) and common objects; of course basis of ML and DL. Deep Learning techniques for detection and segmentation were kind of reached some SotA (State of the Art) benchmarks that seems good enough for us to adapt and they have also shown huge potential on SLAM, SfM, single and stereo image to 3D, depth maps; also, shown good results directly on computer vision tasks on 3D datasets; and many of these were experimented in house to come to arrive to an understanding and certain conclusions for a creating a sustaining AI program in GIS.


With these insights, as the next step, I need to identify of objects in street images for annotating for computer vision tasks. I segregated them into two stages for identification of street objects as **stage-1** and **stage-2**, based on the maturity of deep learning techniques and complexity where:
* **stage-1**
  - detection/segmentation of map specific objects, ex: pole, tree, traffic-sign that can be mapped to point objects
  - probable use-case is used to create new map layers like traffic sign, green cover.
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
| * can be augmented with other sequential camera sensor data | cannot be augmented with sequential sensor data       |


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


## Comparison of datasets (CoD) Analysis

Once, I'd the higher level understanding and framework to identify the categories for specific computer vision tasks, the next challenging was to come up with the object labels a.k.a. categories and category hierarchy such that it leverage common understanding of public dataset in urban scene and self-driving and common objects. The motivation for doing so are:
- as creating a huge dataset on which be able to do hyper-tuning is expensive, one should be able to cross-train across public-datasets with in house created categories for building expertise on hyper tuning; hyper-tuning on small datasets would results in over-fitting
- quantitatively able to measure the quality of annotations by annotators, which is by comparing the stats with the benchmarks
- possibility to provide public datasets with the same labels of public datasets, without compromising our own unique labels
- develop intuition on how the labels should be allocated by deducing some pattern
- finding relevance of these labels with the Indian street scene context
- understanding the annotation tools used, format in which these annotations stored, retrieval and visualizing the created annotations
- at the same-time, look from the perspective of commercial AI annotation service provider
- possibilities on AI assisted annotation
- extension to other type of computer vision tasks annotations like key-point, polygon, point, 2D cuboid for images, videos and point cloud data


In nutshell, listed Category Hierarchy, Annotation Tools, Annotation Storage formats etc. for identified Computer Vision Tasks (detection and instance segmentation).

1. **Documentation of Category Hierarchy for publicly available Computer Vision Datasets for AI**
  * Document the object hierarchy (along with the id, category label etc) in an excel sheet for following types of datasets:
    * Common Objects
    * Self-Driving-Car
    * Scene understanding
2. **Documentation Of AI Annotation Tools**
  * AI annotation tool used
  * annotation storage format
3. **Category Challenge**
  * Internal task to come up with the category labels from our own datasets
4. **Comparison And Mapping Of Category Hierarchy - Internal & External**
  * category and category hierarchy used
  * conventions on storing and releasing the AI datasets
  * different types of AI annotations on same images i.e. specific to computer vision tasks
5. **Analise and propose the category label and hierarchy**
  * key criteria is that one should be able to cross-train across public-datasets with new categories ex: using cityscape dataset with new vehicle types specific to Indian context


### Analysis on Datasets of Interest (DoI)

Approach:
* normalization of labels for comparison
  - singular and plural form are considered as same e.g. vehicle in `cityscape` and vehicles in `idd` are considered as same
  - converted to lowercase
  - spaces were replaced with underscore
* category hierarchy were identified from DoI and first compared at L0 level(referring as top or generic level), with L1, L2,...,Ln are more specific as we go further down
* frequency distribution of labels based on alphabetical order were noted for at least two matches
* kitti, cityscape, idd, mapillary, apolloscape, coco_stuff, coco_things were compared at L0 and labels are put into consecutive columns in excel sheet
* each label is manually alphabetically sorted in the excel sheet, such that only the common label across all columns (i.e. datasets) remain in the same line
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
* created a new criteria for L0 level such that when compared L0 and Ln across datasets, if Ln from any of the dataset is matching to the L0 of at least one dataset, it's considered as L0 in the new hierarchy levels
* L0 Label is assigned a 'starting alphabet letter' to indicate it's considered as the L0 label in the new hierarchy
* L0 and Ln compare and new hierarchy pattern evolved:


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
2. scalable's computer vision task specific annotation nature is interesting and relevant for the work-flow
3. Researchers develop their own annotation tool and work-flow and hence process is still evolving
4. Open-source AI annotation tools in public domain is in nascent stage with first such good tool available in year 2016
5. PASCAL VOC (imagenet), MS COCO, VGG are common formats in which AI annotations are stored and generally used as industry standard
6. Images and annotations are stored separately at the same level of directory structure


## Key Indicators on Work-flow (KIW)
1. Labeling policy, work-flow should evolve with clear instructions is required, with the ability to flag exceptions
2. Workflow needs to be Iterative process to be able to consume annotations on a daily basis rather than wait for a week or months to get them to the AI training desk. And, such process should be scriptable rather than manual management.
3. Quantification from the beginning of the workflow: task allocation, productivity of annotator, quality of annotations by each annotator, quality specifications and benchmarks for the annotations needs to be evolved.
4. Quick visualization and stats on the annotations per image per release etc should be done once using scripts. Manual process is time consuming and error prone and not sustainable over months. This is essential from the understanding of dataset mix and creating splits for AI training on a continuous basis. 
5. Trade off between quality of expected prediction and usability in HD Map creation from AI machine output w.r.t. input annotations in terms annotation quality, time and cost needs to be understood. This is essential in terms of MoVs, setting the right expectations, and to measure the success of AI program.


## New Labeling Scheme, Annotation process and Workflow
Based on this analysis I was able to come up with the new generic hierarchy for annotation process, where following are the core foundation ideas:

- Singular form of label to be used
- lowercase and instead of space used underscore to separate two words in a label
- Optimal label name has to be selected i.e.
	- less ambiguous in nature
	- not too generic and not too specific
- providing additional attribution at the annotation level and at the image level provides the opportunity for cover complex scenarios without re-labeling 
	- For instance, classification of a type of object should not be the part of the label name rather as the annotation attribute, ex: label is person but the same can be classified as pedestrian, rider, cyclist in additional attribution property Truncated, Marking are some of the identified annotation attributes
- Additional annotation attributes can provide an opportunity to create dynamic labeling scheme to create unique labels for AI datasets if required
- Annotation_Quality, Collection_Type, Behaviour_Or_Activity, Position  Velocity, Acceleration, Orientation, Material, Text, Usability, Occlusion, 
- File level /Image attributions are also created: Scene_Type, Weather_Condition, View_Point, Image_Quality
- time-cost-matrix is created as a tool for decision making
- category_hierarchy, labelling_policy, annotation_job, annotation_task_details, classification details were defined clearly
- For each labels visual clip icon and image clipped sample needs to be provided as a annotation aid in the tool
- Before that, in the category_hierarchy Google image search was done to get the intuition
  - based on the image samples what I got I further fine tunned the label names till I get expected output
  - I found out that, we as human have general conception in the Indian context but has more than one meaning
  - examples of ambiguous label:
    + junction_box changed to roadside_junction_box
    + tanker changed to road_tanker
- I also identified the labels which are highly specific to Indian Context and majority of them were under Vehicles
- Finally, provided the following annotation_job:
  * object_detection_segmentation - ods
    * with fine Annotation_Quality for Annotation_Type of bbox and polygon for 32 categories spanning across 3 L0 hierarchy
  * object_recognition_classification - orc
    * traffic_sign, pole and booth
* these jobs assigned as annotation_tasks to each annotators
* release management and directories were sorted out


## Keywords


* CoD - Comparison of datasets
* DoI - Datasets of Interest
* KIW - Key Indicators on Workflow


* HMD - HD Map Database, HD Map Dataset
* AIDS - AI Datasets
* AIL - Annotations, Images, Labels
* PDB - Prediction Database
* ePDB - execption Prediction Database


* APA - AI Predictive Attributes
* MAL - MMI AI Language


* AICATS - AI Categories
* annon - annotation
* train/tr - training
* val/vl - validation
* test/tt - testing
