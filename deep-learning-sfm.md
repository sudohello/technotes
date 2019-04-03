---
Title: Deep Learning for SfM
Decription: Deep Learning for SfM
Author: Bhaskar Mangal
Date: 17th-Dec-2018
Last Updated: 17th-Dec-2018
Tags: Deep Learning, SfM
---

**Table of Contents**
* TOC
{:toc}


## Deep Learning for Structure-from-Motion (SfM)
* https://www.slideshare.net/PetteriTeikariPhD/deconstructing-sfmnet
* http://www.computervisionblog.com/2016/01/why-slam-matters-future-of-real-time.html
* http://geometricdeeplearning.com/

### pose estimates
Random forests versus Neural Networks — What's best for camera localization?
Daniela Massiceti ; Alexander Krull ; Eric Brachmann ; Carsten Rother ; Philip H.S. Torr
Robotics and Automation (ICRA), 2017 IEEE International Conference on; https://doi.org/10.1109/ICRA.2017.7989598

Camera Relocalization by Computing Pairwise Relative Poses Using Convolutional
Neural Network
Zakaria Laskar, Iaroslav Melekhov, Surya Kalia, Juho Kannala
https://arxiv.org/abs/1707.09733

DSAC - Differentiable RANSAC for Camera Localization
Eric Brachmann, Alexander Krull, Sebastian Nowozin, Jamie Shotton, Frank Michel, Stefan Gumhold, Carsten Rother
https://arxiv.org/abs/1611.05705

Deep 6-DOF Tracking
Mathieu Garon, Jean-François Lalonde
https://arxiv.org/abs/1703.09771

### Computer Vision Recap
* https://www.cc.gatech.edu/~hays/compvision/
* https://www.cc.gatech.edu/~hays/compvision/proj6/



### SfM-Net
* https://arxiv.org/find/cs/1/au:+Vijayanarasimhan_S/0/1/0/all/0/1

### SLAM
* http://wp.doc.ic.ac.uk/thefutureofslam/programme/
* https://www.quora.com/Has-someone-tried-to-incorporate-deep-learning-and-SLAM

## Commercial
* http://www.create4d.com

## Research Paper Hubs
* https://kilthub.cmu.edu



## TBD
* https://medium.com/datadriveninvestor/5-fundamental-ai-principles-993528a7d9ed



## 6DoF Estimations

* https://arxiv.org/pdf/1612.00496.pdf
We first regress the orientation and object dimensions before combining these estimates with geometric constraints to produce a final 3D pose. This is in contrast to previous techniques that attempt to directly regress to pose.

A state of the art 2D object detector [3] is extended by training a deep convolutional neural network (CNN) to regress the orientation of the object’s 3D bounding box and its dimensions.

Given estimated orientation and dimensions and the constraint that the projection of the 3D bounding box fits tightly into the 2D detection window, we recover the translation and the object’s 3D bounding box

We introduce three additional performance metrics measuring the 3D box accuracy: distance to center of box, distance to the center of the closest bounding box face, and the overall bounding box overlap with the ground truth box, measured using 3D Intersection over Union (3D IoU) score.


## [Motion R-CNN](https://github.com/simonmeister/motion-rcnn)
* https://github.com/simonmeister/motion-rcnn
* https://drive.google.com/file/d/18hSyz2Wgd-cb-Psju5_oPUyZyE3T3k7j/view

* develop deep neural networks which can, given sequences of images, segment the image pixels into object instances, and estimate the location and 3D motion of each object instance relative to the camera
* Inspired by the accurate segmentation results of Mask R-CNN, we thus propose Motion R-CNN, which combines the scalable instance segmentation capabilities of Mask R-CNN with the end-to-end instance-
level 3D motion estimation approach introduced with SfM-Net. For this, we naturally integrate 3D motion prediction for individual objects into the per-RoI Mask R-CNN head in parallel to classification, bounding box refinement and mask prediction. For each RoI, we predict a single 3D rigid object motion together with the object pivot in camera space in this way.
* As a foundation for image matching, we extend the ResNet [24] backbone of Mask R-CNN to take two concatenated images as input, similar to FlowNetS
* This results in a fully integrated end-to-end network architecture for segmenting pixels into instances and estimating the motion of all detected instances without any limitations as to the number or variety of object instances (Figure 4).
* Eventually, we want to extend our method to include depth prediction, yielding the first end-to-end deep network to perform 3D scene flow estimation in a principled and scalable way from the consideration of individual objects. For now, we will assume that RGB-D frames are given to break down the problem into manageable pieces.
* tackle motion estimation at the instance-level with end-to-end deep networks and derive optical flow from the individual object motions.


* Object classes
* 2D bounding boxes
* Instance masks
* 3D Instance motions (R, t) & pivots Object




slanted plane models - more accurate, more time
end-to-end approach based on learning would be preferable - less accurate, but faster

**Search Phrases**
* 3D scene understanding
* end-to-end deep learning approaches to motion estimation
* Deep networks in optical flow estimation
* 3D camera ego-motion
* Slanted plane methods for 3D scene flow
* Motion Estimation Algorithm Based on the Region of Interest
* Instance Scene Flow
* scene flow and optical flow estimation
* End-to-end deep networks for 3D rigid motion estimation
* End-to-end deep networks for camera pose estimation
* estimating the 6-DOF camera pose from a single RGB frame
* estimating depth and camera ego-motion from monocular video

**Architectures**
* Motion-RCNN
* SfM-Net




## ApolloAuto
* https://github.com/ApolloAuto/apollo/blob/master/docs/specs/3d_obstacle_perception.md
* https://github.com/ApolloAuto/apollo/blob/master/docs/specs/traffic_light.md


Core software modules running on the Apollo 3.5 powered autonomous vehicle include:

Perception — The perception module identifies the world surrounding the autonomous vehicle. There are two important submodules inside perception: obstacle detection and traffic light detection.
Prediction — The prediction module anticipates the future motion trajectories of the perceived obstacles.
Routing — The routing module tells the autonomous vehicle how to reach its destination via a series of lanes or roads.
Planning — The planning module plans the spatio-temporal trajectory for the autonomous vehicle to take.
Control — The control module executes the planned spatio-temporal trajectory by generating control commands such as throttle, brake, and steering.
CanBus — The CanBus is the interface that passes control commands to the vehicle hardware. It also passes chassis information to the software system.
HD-Map — This module is similar to a library. Instead of publishing and subscribing messages, it frequently functions as query engine support to provide ad-hoc structured information regarding the roads.
Localization — The localization module leverages various information sources such as GPS, LiDAR and IMU to estimate where the autonomous vehicle is located.
HMI - Human Machine Interface or DreamView in Apollo is a module for viewing the status of the vehicle, testing other modules and controlling the functioning of the vehicle in real-time.
Monitor - The surveillance system of all the modules in the vehicle including hardware.
Guardian - A new safety module that performs the function of an Action Center and intervenes should Monitor detect a failure.

localization method is RTK-based
Multiple Sensor Fusion (MSF) 

## 3D-RCNN
* http://openaccess.thecvf.com/content_cvpr_2018/papers/Kundu_3D-RCNN_Instance-Level_3D_CVPR_2018_paper.pdf