---
Title: Deep Learning Performance Metrics
Decription: Deep Learning Performance Metrics
Author: Bhaskar Mangal
Date: 05th-Mar-2019
Last Updated: 05th-Mar-2019
Tags: Deep Learning Performance Metrics
---


**Table of Contents**
* TOC
{:toc}


## Keywords
* precision
* recall
* IoU
* mAP
* TP - True Positive; TN - True Negative
* FP - False Positive; FN - False Negative
* F1 Score


## Metrics
* https://www.pyimagesearch.com/2018/05/14/a-gentle-guide-to-deep-learning-object-detection/
* https://medium.com/@jonathan_hui/map-mean-average-precision-for-object-detection-45c121a31173


## Precision 
* Precision measures how accurate is your predictions
* i.e. the percentage of your positive predictions are correct
* TP/(TP+FP) i.e. True Positive divided by Total predictions


## Recall
* Recall measures how good you find all the positives
* For example, we can find 80% of the possible positive cases in our top K predictions
* TP/(TP+FN) i.e True Positive divided by sum of True and False Negative predictions

**For example, in the testing for cancer:**
* Precision = True Positive / total positive results
* Recall = True Positive / total cancer cases


## F1 Score
* `2 * (precision * recall)/(precision + recall)`


### IoU - Intersection over Union
* IoU measures how much overlap between 2 regions
* This measures how good is our prediction in the object detector with the ground truth (the real object boundary)
* Comparing predicted detections to the ground-truth with Intersection over Union
* https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/
* https://zhenye-na.github.io/2018/05/22/intersection-over-union-for-object-detection.html
* https://medium.com/@venuktan/vectorized-intersection-over-union-iou-in-numpy-and-tensor-flow-4fa16231b63d


## AP - Average Precision


## mAP - mean Average Precision
* https://stackoverflow.com/questions/36274638/map-metric-in-object-detection-and-computer-vision
* mAP is the metric to measure the accuracy of object detectors
* It is the average of the maximum precisions at different recall values



Any algorithm that provides predicted bounding boxes (and optionally class labels) as output can be evaluated using IoU. More formally, in order to apply IoU to evaluate an arbitrary object detector, we need:

The ground-truth bounding boxes (i.e., the hand-labeled bounding boxes from our testing set that specify where an image our object is).
The predicted bounding boxes from our model.
If you want to compute recall along with precision, you’ll also need the ground-truth class labels and predicted class labels.


## **Reporting**
* mAP - mean Average Precision scores for each hyperparameters
* Average Precision  (AP)
* Average Recall     (AR)
* IoU


## TBD
* https://www.kaggle.com/learn/machine-learning
* https://github.com/CPFL/Autoware
* https://maptools.tier4.jp/
* http://www.aisantec.co.jp/english/
* http://shubhagrawal.in/2016/08/01/creating-launcher-for-any-executable-file-linux/
* http://home.bharathh.info/

