---
Title: IDD - Indian Driving Dataset Overview
Decription: IDD - Indian Driving Dataset Overview
Author: Bhaskar Mangal
Date: 09th-Jan-2019
Last updated: 09th-Jan-2019
Tags: IDD - Indian Driving Dataset Overview
---

**Table of Contents**
* TOC
{:toc}


## **[IDD - Indian Driving Dataset](http://idd.insaan.iiit.ac.in/)**
* https://github.com/AutoNUE/public-code
* http://cvit.iiit.ac.in/scene-understanding-challenge-2018/


**Key highlights**
* consists of 10,004 finely annotated images (frames of video sequence)
* 34 classes
* collected from 182 drive sequences
* **Indian Roads**
  - unstructured environment
  - The variety of traffic participants in Indian roads is larger, including novel classes such as autorickshaws or animals
  - The within-class diversity is also higher, for example, since vehicles span a larger range of manufacturing years and ply with larger variation in wear
  - the proportion of motorcycles
  - multiple riders on two-wheeled vehicles
  - **Background classes also display greater diversity**
    + city scenes rich in novel classes such as billboards
  - traffic participants have lower adherence to traffic rules
  - motions can be sudden
  - complex obstructions might be present
  - drivable areas can be ambiguous
  - traffic lanes need not correspond to lane markings on the road
  - **Ambiguous Road Boundaries**
    + Road sides can have muddy terrain, while also being drivable to some extent
    + Roads themselves can be covered by dirt or mud, making the boundaries very ambiguous
  - **Diversity of Vehicles and Pedestrians**
    + variety of unique vehicles like auto-rickshaws
    + for standard categories like cars, the appearance variations are higher due to greater wear and tear
    + the frequency and variety of trucks and buses are also high
    + large number of motorbikes with multiple persons riding it
    + Bikes and autorickshaws are also less likely to follow traffic discipline
    + fewer correlation between traffic participants and road signage such as lanes or traffic lights
  + **Extensive Use of Information Boards**
    + billboards appear extensively
  ** **Diversity of Ambient Conditions**
    ** Lighting variation
      + images at various times of the day, including mid-day, dawn and dusk
      + images have heavy shadows, which are common during a long summer season
      + scenes with heavily clouded skies
    * The greater variation in particulate matter due to fog, dust or smog also leads to significant appearance variation 
* Bangalore and Hyderabad cities in India and their outskirts
* The driving conditions in these localities are highly unstructured due to multiple reasons:
  - these cities are rapidly growing and have a lot of construction near the roads
  - pedestrians and jaywalkers are aplenty in these road images
  - high density of motorbikes and trucks on the road
* **Frame Selection**
  * We chose images from one of the forward facing cameras of a stereo pair, for fine annotation
  * Images were sampled at varying rates from the video sequence
  * with denser sampling around crowded and special interest places like traffic junctions
* These images were annotated very finely, by layered polygon masks similar to Cityscapes 
* Mix of urban and rural areas, highway, single lane and double lane roads with a variety of traffic
* **USP**
  - algorithms are largely untested in their ability to generalize to road conditions that are significantly more diverse and unstructured
  - label hierarchy is attuned to the autonomous navigation problem
* The label set is expanded in comparison to popular benchmarks such as Cityscapes, to account for new classes.
+ 4 levels of the hierarchy with 30 (level 4), 26 (level 3), 16 (level 2) and 7 (level 1) labels, respectively, giving different complexity levels for training models
+ variations in weather and lighting
+ other ambient factors such as
  +  air quality
  +  dust
+ For instance, while the notion of a drivable area in Europe is largely de- fined by classes such as roads or lanes that have distinct appearances, it is more ambiguous in our dataset and likely also informed by semantic cues such as presence of dynamic traffic participants. Thus, we include labels for safely driv- able and non-drivable areas
* the number of object classes and within-class diversity of appearance are higher for IDD
* **Comparission with cityscape**
  * Cityscape models do not distinguish between the road and possible unsafe drivable area on both sides of the road
  * Road boundaries in Cityscapes are very well defined and usually flanked on both sides by barriers or sidewalks.
* **Label Hierarchy & Annotation**
  * total of 34 labels in the fine annotations.
  * it is difficult to completely avoid ambiguity between some labels
  * designed a 4 level label hierarchy having 7 (level 1), 16 (level 2), 26 (level 3) and 30 (level 4) labels
  * Each level defines a category as the union of labels in the succeeding level
  * added fall-back labels whenever appropriate so that highly ambiguous objects can be given labels
* **Training Annotators**
  * For labeling the dataset, the annotation team was first asked to re-annotate images from the Cityscapes dataset. The difference between the annotations were subsequently shown to the annotators. This process was done until the annotators were achieving greater than 95% accuracy with respect to the Cityscapes ground truth labels
* **Statistical Analysis and Dataset Splits**




**Tools and Code for working with dataset**
* https://github.com/AutoNUE/public-code
```bash
git clone https://github.com/AutoNUE/public-code.git
```


**[Dataset Structure](https://github.com/AutoNUE/public-code#dataset-structure)**
* The structure is similar to the cityscapes dataset.


**Labels**
* See [helpers/anue_labels.py](https://github.com/AutoNUE/public-code/blob/master/helpers/anue_labels.py)


## References
* https://ai.intel.com/iiit-hyderabad-and-intel-release-worlds-first-dataset-for-driving-in-india/
* http://idd.insaan.iiit.ac.in/evaluation/leader-board/


## Keywords
* **ANUE**, **AutoNUE** - Autonomous Navigation in Unstructured Environments


## TBD
motivates problems such as few-shot learning.

