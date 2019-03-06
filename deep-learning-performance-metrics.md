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
* https://stackoverflow.com/questions/36274638/map-metric-in-object-detection-and-computer-vision
* [PASCAL VOC 2007, Sec 4.2 Evaluation of Results](http://homepages.inf.ed.ac.uk/ckiw/postscript/ijcv_voc09.pdf)
  * Evaluation of results on multi-class datasets
  * (i) for the classification task, images contain instances of multiple classes, so a “forced choice” paradigm such as that adopted by Caltech 256 (Griffin et al 2007) – “which one of m classes does this image contain?” – cannot be used; 
  * (ii) the prior distribution over classes is significantly nonuniform so a simple accuracy measure (percentage of correctly classified examples) is not appropriate.
  * In the absence of information about the cost or risk of misclassifications, it is necessary to evaluate the trade-off between different types of classification error
  * (iii) evaluation measures need to be algorithmindependent
  * for classification “is there a car in the image?”, and for detection “where are the cars in the image (if any)?”
  * A separate “score” is computed for each of the classes. 
  * For the classification task, participants submitted results in the form of a confidence level for each image and for each class, with larger values indicating greater confidence that the image contains the object of interest. 
  * For the detection task, participants submitted a bounding box for each detection, with a confidence level for each bounding box.
  * The provision of a confidence level allows results to be ranked such that the trade-off between false positives and false negatives can be evaluated, without defining arbitrary costs on each type of classification error.
  * For a given task and class, the precision/recall curve is computed from a method’s ranked output. Recall is defined as the proportion of all positive examples ranked above a given rank. Precision is the proportion of all examples above that rank which are from the positive class. The AP summarises the shape of the precision/recall curve, and is defined as the mean precision at a set of eleven equally spaced recall levels [0,0.1,...,1]:
  * The precision at each recall level r is interpolated by taking the maximum precision measured for a method for which the corresponding recall exceeds r
  * The intention in interpolating the precision/recall curve in this way is to reduce the impact of the “wiggles” in the precision/recall curve, caused by small variations in the ranking of examples
  * It should be noted that to obtain a high score, a method must have precision at all levels of recall – this penalises methods which retrieve only a subset of examples with high precision (e.g. side views of cars).
  * The use of precision/recall and AP replaced the “area under curve” (AUC) measure of the ROC curve used in VOC2006 for the classification task
  * This change was made to improve the sensitivity of the metric (in VOC2006 many methods were achieving greater than 95% AUC), to improve interpretability (especially for image retrieval applications), to give increased visibility to performance at low recall, and to unify the evaluation of the two main competitions.


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

