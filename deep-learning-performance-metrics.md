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
* AUC - Area Under Curve
* AP - average precision
* ROC curve - Receiver Operating Characteristic curve


## Metrics
* https://www.pyimagesearch.com/2018/05/14/a-gentle-guide-to-deep-learning-object-detection/
* https://medium.com/@jonathan_hui/map-mean-average-precision-for-object-detection-45c121a31173
* https://stackoverflow.com/questions/36274638/map-metric-in-object-detection-and-computer-vision
* https://github.com/rafaelpadilla/Object-Detection-Metrics
* http://dcs.gla.ac.uk/~ronanc/papers/cumminsAIRS11_2.pdf
* https://arxiv.org/pdf/1310.5103.pdf

* https://sanchom.wordpress.com/tag/average-precision/ -> Best Reference on Performance metrics and Average Precision
* https://stats.stackexchange.com/questions/157012/area-under-precision-recall-curve-auc-of-pr-curve-and-average-precision-ap


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
  * Detections output by a method were assigned to ground truth objects satisfying the overlap criterion in order ranked by the (decreasing) confidence output
  * Multiple detections of the same object in an image were considered false detections e.g. 5 detections of a single object counted as 1 correct detection and 4 false detections – it was the responsibility of the participant’s system to filter multiple detections from its output

- Multiple label Classification evaluation
- Bounding box evaluation
- Evaluation of the segmentation taster
  + A common measure used to evaluate segmentation methods is the percentage of pixels correctly labelled.

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
* https://sanchom.wordpress.com/tag/average-precision/
* https://stackoverflow.com/questions/36274638/map-metric-in-object-detection-and-computer-vision
* https://stats.stackexchange.com/questions/157012/area-under-precision-recall-curve-auc-of-pr-curve-and-average-precision-ap

## mAP - mean Average Precision
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

### PPTs
* http://deeplearning.csail.mit.edu/presentation_tutorial_interpretability_slide.pdf
* http://deeplearning.csail.mit.edu/xg_tutorial.pdf
* http://deeplearning.csail.mit.edu/instance_ross.pdf
* http://sunw.csail.mit.edu


## Graphs
* How do I plot Precision-Recall graphs for Content-Based Image Retrieval?
https://stackoverflow.com/questions/25799107/how-do-i-plot-precision-recall-graphs-for-content-based-image-retrieval-in-matla#25811041

* https://stackoverflow.com/questions/31407844/is-it-possible-that-precision-recall-curve-or-a-roc-curve-is-a-horizontal-line

Yes, you can. If you perfectly separate the data into two piles, then you go vertically from zero to 1 true-positive-rate without any false positives (the vertical line) as your threshold passes over your pile of true positives, then from 0 to 1 false-positive-rate as your threshold passes over your pile of true negatives.

If you can get the same ROC curve from a test set, you are golden. If you can get the same ROC curve evaluated on 5 different k-fold cross validation test sets, you are platinum.



Take the time and think about what the plots actually tell you. You basically performed perfect predictions on the test set. Is this normal? No. Often problems tackled with machine learning techniques are much harder. Perfect predictions are usually not possible. Or did I make some mistakes in my code? In your code? Probably not. In your testing? Maybe. We don't know. I would suggest trying a cross validation instead. Maybe your problem is very easy to learn. Maybe your test set is problematic. A cross validation will show that.




https://stackoverflow.com/questions/28200786/how-to-plot-scikit-learn-classification-report


using seaborn heatmap

 ['precision', 'recall', 'f1-score', 'support']

visualizing the confusion matrix
classification report


https://stackoverflow.com/questions/30746460/how-to-interpret-scikits-learn-confusion-matrix-and-classification-report

Classification report must be straightforward - a report of P/R/F-Measure for each element in your test data.
In Multiclass problems, it is not a good idea to read Precision/Recall and F-Measure over the whole data any imbalance would make you feel you've reached better results. That's where such reports help.


Coming to confusion matrix, it is much detailed representation of what's going on with your labels. So there were 71 points in the first class (label 0). Out of these, your model was successful in identifying 54 of those correctly in label 0, but 17 were marked as label 4. Similarly look at second row. There were 43 points in class 1, but 36 of them were marked correctly. Your classifier predicted 1 in class 3 and 6 in class 4.


Actual class on y-axis, Predicted class on x-axis
An ideal classifiers with 100% accuracy would produce a pure diagonal matrix which would have all the points predicted in their correct class.

F Measure is harmonic mean of Precision and Recall. Be sure you read details about these. 
https://en.wikipedia.org/wiki/Precision_and_recall


Confusion Matrix tells us about the distribution of our predicted values across all the actual outcomes.Accuracy_scores, Recall(sensitivity), Precision, Specificity and other similar metrics are subsets of Confusion Matrix. F1 scores are the harmonic means of precision and recall. Support columns in Classification_report tell us about the actual counts of each class in test data.

https://github.com/cocodataset/cocoapi/issues/56



https://classeval.wordpress.com/introduction/basic-evaluation-measures/
https://stackoverflow.com/questions/39033880/plot-confusion-matrix-sklearn-with-multiple-labels#39034386


https://machinelearningmastery.com/generate-test-datasets-python-scikit-learn/

https://bbabenko.github.io/prs/