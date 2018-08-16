/*
Title: Deep Learning  - Traffic Sign Detection and Classification
Decription: Traffic Sign Detection and Classification
Author: Bhaskar Mangal
Date: 06th-Aug-2018
Last Updated: 06th-Aug-2018
Tags: Computer Vision ML, DL Applications
*/


**Table of Contents**

[TOC]

##  Deep Learning  - Traffic Sign Detection and Classification

* https://github.com/xfqbuaa/Traffic-Signs-Detect-German
Experiments results show that, by combining the Haar Cascade and deep convolutional neural networks show that the joint learning greatly enhances the capability of detection and still retains its realtime performance
* https://medium.com/the-pointscene-diaries/online-point-cloud-viewers-e680dbbe76d9
* https://github.com/david-vazquez/mcv-m5/tree/master/code
* https://github.com/georgesung/ssd_tensorflow_traffic_sign_detection
* https://github.com/fabioperez/transito-cv
* https://github.com/handong1587/handong1587.github.io/blob/master/_posts/deep_learning/2015-10-09-object-detection.md
* https://github.com/topics/traffic-sign-detection



Traffic Sign Detection and Recognition
* https://www.researchgate.net/publication/317607639_Deep_learning_traffic_sign_detection_recognition_and_augmentation
  - Combine Haar Cascade and DNN
* https://arxiv.org/pdf/1802.10019.pdf
  - Simultaneous Traffic Sign Detection and Boundary Estimation using Convolutional Neural Network
  - TRAFFIC sign detection has been a traditional problem for intelligent vehicles, especially as a preceding step for traffic sign recognition which provides useful information such as directions and alerts for autonomous driving or driver assistance systems. Recently, traffic sign detection has received another attention from navigation systems for intelligent vehicles, where traffic signs can be used as distinct landmarks for mapping and localization. Different from natural landmarks such as corner points or edges, traffic signs have standard appearance such as shapes, colors, and patterns defined by strict regulations. This forms a primary reason that traffic signs are a preferable choice as landmarks for high-definition map reconstruction, as it allows efficient and robust landmark detection and matching under various conditions.
  - Traffic sign detection system where the position and precise boundary of traffic signs are predicted simultaneously
  - Key terms:
    * Traffic sign detection, traffic sign boundary estimation
  * Based on the recent advances in CNN-based object detection for object bounding box prediction [5], [6], [7], but tailored to predict the 2D poses and shape labels of planar targets.
  * The 2D pose of a planar target can be encoded as an 8- dimensional vector, e.g., the coordinates of four vertices, and it can be accurately predicted by CNN which simultaneously predicts the score of each shape label.
  * Using the predicted 2D poses and shape labels, the boundary corners of a traffic sign are computed by projecting the boundary corners of a corresponding template image of the sign into the image coordinate using the predicted pose
  * By using the templates of traffic signs, our method effectively utilizes strong prior information of target shapes.
    * detection rates higher than 0.88 mean average precision (mAP)
    * boundary estimation error less than 3 pixels with respect to input resolution of 1280 × 720 pixels


  https://github.com/upul/Traffic-Signs
  https://github.com/MiguelPF/Traffic-Sign-Detection---Recognition-System
  https://github.com/AutoModelCar/AutoModelCarWiki/wiki/traffic-sign-detection


  https://github.com/ghostbbbmt/Traffic-Sign-Classification

https://github.com/topics/traffic-signs?l=python
SSD - Single Shot MultiBox Detector

https://github.com/georgesung/ssd_vehicle_detection

Start Here:
* https://github.com/georgesung/ssd_tensorflow_traffic_sign_detection
* TypeError: Expected int32, got list containing Tensors of type '_Message' instead.


http://cvrr.ucsd.edu/LISA/lisa-traffic-sign-dataset.html

Viva
http://cvrr.ucsd.edu/vivachallenge/index.php/signs/sign-detection/


SSD
https://arxiv.org/abs/1512.02325
https://github.com/weiliu89/caffe/tree/ssd

SSD v/s Faster R-CNN
- Even the fastest high-accuracy detector, Faster R-CNN, operates at only 7 frames per second (FPS)

https://www.codemade.io/lisa-traffic-sign-dataset/
https://navoshta.com/traffic-signs-classification/

https://github.com/weiliu89/caffe/tree/ssd
https://github.com/balancap/SSD-Tensorflow
https://github.com/ljanyst/ssd-tensorflow.git
http://jany.st/post/2017-11-05-single-shot-detector-ssd-from-scratch-in-tensorflow.html

http://moegelmose.com/p10/report.pdf
http://moegelmose.com/p10/

------------

Object Detection Datasets
- http://host.robots.ox.ac.uk/pascal/VOC/
```bash
wget -c http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtrainval_06-Nov-2007.tar
wget -c http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtest_06-Nov-2007.tar
wget -c http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar
```
----------------
Indian Traffic Sign Charts
http://delhi.gov.in/wps/wcm/connect/2ec0370049174a1a9328d762068aeed4/Road+Traffic+Signs+Recognition+Chart.pdf?MOD=AJPERES&lmod=-1350425976
https://www.timescale.com/
Open-source 
time-series database 
powered by PostgreSQL


http://trafficsigns.co.in/
https://www.quora.com/How-many-types-of-traffic-signs-are-there-in-India


As per IRC (Indian Roads Congress) Road Signs are for indications on the road the road signs are categorized into 3 types:
• Mandatory Signs or Regulatory Signs.
• Cautionary Signs or Warning or Precautionary.
• Informatory Signs.



These Traffic Light Signals are In India !!

Red - To Stop the Traffic

This means that you should stop your vehicle immediately and you would be required to wait until there is green light.

Yellow - Caution

There are many of you who would be entering into the intersection area and they need to wait until the light switches to amber and then only move carefully. Stop, as you see the amber light.

Green - Go on

You need to pass through the crossing in a careful manner and whenever view the arrow and then proceed forward through the help of indicator.

Flashing Signals

Whenever you see the flashing signals, it means complete halt and then move according to the intersection safely.

Pedestrian Signals

These signals are meant for the people who cross the intersections in safest manner. In case, you see the red figure of human on the traffic signal post, then never enter the road. When the signal would start flashing and then only cross the road. You should immediately stop yourself, if you were to cross the road.

Moreover, these traffic rules and regulations are meant for your safety and you need to follow them in the best possible way.


http://cvit.iiit.ac.in/autorickshaw_detection/index.html

https://data.world/datasets/india
===================

1. Highway maintenance: Check the presence and condition of signs along major
roads.
2. Sign inventory: Similarly to the above task, creating an inventory of signs in city
environments.
3. Driver support systems: Assist the driver by informing of current restrictions,
limits, and warnings.
4. Intelligent autonomous vehicles: Any autonomous car that is to drive on public roads must have a means of obtaining the current traffic regulations. This can
be done through TSR.

=================
* Evaluation
  - Accuracy
    * detection rates  with mean Average Precision (mAP)
  - Errors
  - Speed
    * Often detection speed is measured in seconds per frame (SPF),


