---
Title: R&D Problem Statements
Decription: R&D Problems Statements
Author: Bhaskar Mangal
Date: 
Last Updated: 15th-Mar-2019
Tags: R&D Problems Statements
---


**Table of Contents**
* TOC

{:toc}


## R&D Problem Statements

### A) Sensor Fusion, SfM, Geometry Extraction
Given video stream or image sequences or street image, GPS and IMU data.
* Extract road geometries like edges of the road, marking polygons etc with the depth and respective latitude, longitude, altitude, yaw, pitch and roll  parameters.
* Use end-to-end AI pipeline.
  * [Deep Learning SfM](deep-learning-sfm.md)
  * [Slam](slam.md)
  * [3D-Machine Learning](https://github.com/mangalbhaskar/3D-Machine-Learning)
  * [Deep Learning Datasets And Creation](deep-learning-datasets-and-creation.md)
* Provide the extracted data in Apollo OpenDrive format
  * [Apollo Auto](https://github.com/ApolloAuto/apollo)


### B) Application of Extracted data
* Localisation of Self-driving car using the prior knowledge of High Definition Map (Map constructed previously)
  * [Mechanics Of Self-driving Car](https://github.com/mangalbhaskar/technotes/blob/master/mechanics-of-self-driving-car.md)
  * [Autonomous Vechile Tech](https://github.com/mangalbhaskar/technotes/blob/master/autonomous-vechile-tech.md)
