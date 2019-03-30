---
Title: FiveAI Dataset Overview
Decription: FiveAI Dataset Overview
Author: Bhaskar Mangal
Date: 30th-Mar-2019
Last updated: 30th-Mar-2019
Tags: FiveAI Dataset Overview
---


**Table of Contents**
* TOC
{:toc}


## [ FiveAI -Brook_Roberts_A_Dataset_for_ECCV_2018_paper - best](https://five.ai/)
+ https://five.ai/datasets
* semi-automated method that allows for efficient labelling of image sequences by utilising an estimated road plane in 3D based on where the car has driven and projecting labels from this plane into all images of the sequence.
* in urban environments
* road segmentation
* ego lane segmentation
* lane instance segmentation
* A semi-automated annotation method for lane instances in 3D, requiring only inexpensive dash-cam equipment
* Road surface annotations in dense traffic scenarios despite occlusion
* Experimental results for road, ego-lane and lane instance segmentation using a CNN
* **In order to remove parts where the car moves very slowly or stands still (which is common in urban environments), we only include frames that are at least 1m apart according to the GPS**
* Finally, we split the recorded data into sequences of 200m in length, since smaller sequences are easier to handle (e.g. no need for key-frame bundle adjustment, and faster loading times).
* **Hardware & Setup**
* standard Nextbase 402G dashcam recording at a resolution of 1920x1080 at 30 frames per second and compressed with the H.264 standard
* The camera was mounted on the inside of the car windscreen, roughly along the centre line of the vehicle and approximately aligned with the axis of motion
* **Data Acquisition**
* remove parts where the car moves very slowly or stands still (which is common in urban environments)
* only included frames that are at least 1m apart according to the GPS
* split the recorded data into sequences of 200m in length, since smaller sequences are easier to handle (e.g. no need for key-frame bundle adjustment, and faster loading times)
* **Video Annotation**
* The initial annotation step is automated and provides an estimate of the road surface in 3D space, along with an estimate for the ego-lane
* Then the estimates are corrected manually and further annotations are added in the road surface space. The labels are then projected into the 2D camera views, allowing the annotation of all images in the sequence at once
* Given a dash-cam video sequence of N frames from a camera with unknown intrinsic and extrinsic parameters, the goal is to determine the road surface in 3D and project an estimate of the ego-lane onto this surface.
* To this end, we first apply OpenSfM [29], a structure from motion algorithm, to obtain the 3D camera locations c i and poses R i for each frame i ∈ {1, ..., N } in a global coordinate system, as well as the camera projective transform P (·), which includes the estimated focal length and distortion parameters (R i ∈ R 3×3 are 3D rotation matrices)
* OpenSfM reconstructions are not perfect, and failure cases are filtered during the manual annotation process.
* **Dataset Statistics and Split**
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
* **Two segmentation tasks - Road and Ego-Lane Segmentation**
* Road/Non-Road detection (ROAD
* Ego/Non-Ego/Non-Road lane detection (EGO)
* **baseline**
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

