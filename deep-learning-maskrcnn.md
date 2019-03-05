---
Title: Instance Segmentation with Mask-rcnn
Decription: Instance Segmentation with Mask-rcnn
Author: Bhaskar Mangal
Date: 
Last Updated: 05th-Mar-2019
Tags: Instance Segmentation with Mask-rcnn
---


**Table of Contents**
* TOC
{:toc}


## Object Detectors
* https://medium.com/@jonathan_hui/design-choices-lessons-learned-and-trends-for-object-detections-4f48b59ec5ff


### Region based
* https://medium.com/@jonathan_hui/what-do-we-learn-from-region-based-object-detectors-faster-r-cnn-r-fcn-fpn-7e354377a7c9
* Fast R-CNN, Faster R-CNN, R-FCN and FPN
* Sliding-window detectors
  - slide windows from left and right, and from up to down to identify objects using classification
  - To detect different object types at various viewing distances, we use windows of varied sizes and aspect ratios
* CNN Classifier - SVM (Support Vector Machine)
  * SVM - linear, non-linear using kernel trick
* BBox Regressor
* Instead of a brute force approach, **region proposal method** is used - to create **ROIs (Region of Interests)** for object detection
* **Selective Search (SS)**, we start with each individual pixel as its own group


**R-CNN**
* R-CNN makes use of a region proposal method 
* The regions are warped into fixed size images and feed into a CNN network individually.
* It is then followed by fully connected layers to classify the object and to refine the boundary box.
* With far fewer but higher quality ROIs, R-CNN run faster and more accurate than the sliding windows


**Fast R-CNN**
* Instead of extracting features for each image patch from scratch, we use a feature extractor (a CNN) to extract features for the whole image first.
* also use an external region proposal method, like the selective search, to create ROIs which later combine with the corresponding feature maps to form patches for object detection
* We warp the patches to a fixed size using ROI pooling 
* Fixed size ROI are feed to fully connected layers for classification and localization (detecting the location of the object)

* By not repeating the feature extractions, Fast R-CNN cuts down the process time significantly
* One major takeaway for Fast R-CNN is that the whole network (the feature extractor, the classifier, and the boundary box regressor) can be trained end-to-end with multi-task losses (classification loss and localization loss). This improves accuracy.
* ROI Pooling
  - Because Fast R-CNN uses fully connected layers, we apply ROI pooling to warp the variable size ROIs into in a predefined size shape

**Faster R-CNN**
* Fast R-CNN depends on an external region proposal method like selective search. This algorithms run on CPU and they are slow.
* Faster R-CNN adopts similar design as the Fast R-CNN except it replaces the region proposal method by an internal deep network **region proposal network (RPN)** and the ROIs are derived from the feature maps instead.
* The new **region proposal network (RPN)** is more efficient and run at 10 ms per image in generating ROIs.
* Faster R-CNN uses a classifier with 2 possible classes: one for the “have an object” category and one without (i.e. the background class).


**Region-based Fully Convolutional Networks (R-FCN)**
* R-FCN improves speed by reducing the amount of work needed for each ROI. 
* The region-based feature maps above are independent of ROIs and can be computed outside each ROI
* This process to map score maps and ROIs to the vote array is called position-sensitive ROI-pool

**FPN**

**R-FCN**

**Mask R-CNN**


### Single shot
* https://medium.com/@jonathan_hui/what-do-we-learn-from-single-shot-object-detectors-ssd-yolo-fpn-focal-loss-3888677c5f4d
* SSD and YOLO (YOLOv2 and YOLOv3)
* how a pyramid of multi-scale feature maps will improve accuracy, in particular for small objects that usually perform badly for single shot detectors
* Focal loss and RetinaNet on how it solve class imbalance problem during training
## Object Detect & Segmentation
* https://stackoverflow.com/questions/49502475/visualizing-the-detection-process-in-mask-rcnn
* https://medium.com/@jonathan_hui/image-segmentation-with-mask-r-cnn-ebe6d793272
* https://blog.athelas.com/a-brief-history-of-cnns-in-image-segmentation-from-r-cnn-to-mask-r-cnn-34ea83205de4


## **Mask-RCNN**

* https://github.com/facebookresearch/Detectron
* https://github.com/matterport/Mask_RCNN
* https://github.com/CharlesShang/FastMaskRCNN - just for basics
* https://medium.com/@jonathan_hui/image-segmentation-with-mask-r-cnn-ebe6d793272
* https://medium.com/neuromation-io-blog/neuronuggets-segmentation-with-mask-r-cnn-c76d363b67fb
* https://blog.athelas.com/a-brief-history-of-cnns-in-image-segmentation-from-r-cnn-to-mask-r-cnn-34ea83205de4


**Explanation Videos**
part1-mask-rcnn-architecture-how-faster-rcnn-works.mp4
* part 1: https://www.youtube.com/watch?v=QSYd61jOa8M
part2-mask-rcnn-architecture-how-fcn-fully-convolutional-networks-works-for-semantic-segmentation.mp4
* part 2: https://www.youtube.com/watch?v=UdZnhZrM2vQ
part3-mask-rcnn-architecture-how-roi-pooling-roi-warping-roi-align-work.mp4
* part 3: https://www.youtube.com/watch?v=XGi-Mz3do2s


**mask-rcnn-iccv-2017-author-kaiminppt**
* https://www.youtube.com/watch?v=g7z4mkfRjI4&list=PLe6h2Vdf1gFENsJ0W2bUlOGoLWrZdzK8n
* https://www.youtube.com/watch?v=Ul25zSysk2A&list=PLkRkKTC6HZMxZrxnHUDYSLiPZxiUUFD2C
* https://www.youtube.com/watch?v=UdZnhZrM2vQ&list=PLjh3zPDW5j_v20KQvJb9Q5puTC4AjK7jK


### Matterport Mask-rcnn
* https://www.reddit.com/r/MachineLearning/comments/8mqywx/best_implementation_of_mask_rcnn_p/
* https://github.com/matterport/Mask_RCNN
* https://github.com/matterport/Mask_RCNN/releases
* https://github.com/matterport/Mask_RCNN/wiki
* how the model works and show how to use it in a real application.
* uses a ResNet101 + FPN backbone.
* Region Proposal Network (RPN)
  * The RPN is a lightweight neural network that scans the image in a sliding-window fashion and finds areas that contain objects. If several anchors overlap too much, we keep the one with the highest foreground score and discard the rest (referred to as Non-max Suppression - NMS)
```
sudo pip3 install pycocotools imgaug IPython[all]
```


### Mask-rcnn With Opencv
* https://www.pyimagesearch.com/2018/11/19/mask-r-cnn-with-opencv/


### Cityscape on MXNet
* https://github.com/TuSimple/mx-maskrcnn
* https://mxnet.incubator.apache.org/versions/master/install/
* https://towardsdatascience.com/building-a-custom-mask-rcnn-model-with-tensorflow-object-detection-952f5b0c7ab4
* https://patrickwasp.com/train-a-mask-r-cnn-model-on-your-own-dataset/


### Mask-rcnn Docker
* https://github.com/waspinator/deep-learning-explorer/tree/master/mask-rcnn

### Visualize Saliency
* `visualize_saliency`
* https://pastebin.com/WvjLqabs
* https://raghakot.github.io/keras-vis/visualizations/saliency/
* https://www.findbestopensource.com/product/matterport-mask-rcnn


## Splash of Color
* **splash-of-color-instance-segmentation-with-mask-r-cnn-and-tensorflow**
* https://engineering.matterport.com/splash-of-color-instance-segmentation-with-mask-r-cnn-and-tensorflow-7c761e238b46


## Idly Dosa Dataset
* https://www.linkedin.com/pulse/mask-rcnn-custom-data-set-idly-vada-dosa-abhilash-reddy-yerasi
* https://github.com/abhiyerasi


## Mask-rcnn-webcam
* https://github.com/benjamintanweihao/mask-rcnn-webcam


## Snagging Parking Spaces With Mask-r-cnn
* https://medium.com/@ageitgey/snagging-parking-spaces-with-mask-r-cnn-and-python-955f2231c400
* valid parking spaces are just places containing non-moving cars
* The bounding box of each car here is actually a parking space! We don’t need to actually detect parking spaces if we can detect stationary cars.
* if we can detect cars and figure out which ones aren’t moving between frames of video, we can infer the locations of parking spaces.
* “old school” to “new school”


## 4K video, Video
* https://www.youtube.com/watch?v=OOT3UIXZztE
* https://github.com/karolmajek/Mask_RCNN
* https://github.com/priya-dwivedi/Deep-Learning/blob/master/Mask_RCNN/Mask_RCNN_Videos.ipynb

## Car Damage Detection
* https://www.analyticsvidhya.com/blog/2018/07/building-mask-r-cnn-model-detecting-damage-cars-python/
* https://github.com/priya-dwivedi/Deep-Learning/blob/master/Mask_RCNN
* https://github.com/priya-dwivedi/Deep-Learning


## Segmenting Nuclei in Microscopy Images / Automatic Nucleus Detection
* https://github.com/matterport/Mask_RCNN/tree/master/samples/nucleus
* https://towardsdatascience.com/instance-segmentation-automatic-nucleus-detection-a169b3a99477


## Reconstructing 3D buildings from aerial LiDAR
* https://medium.com/geoai/reconstructing-3d-buildings-from-aerial-lidar-with-ai-details-6a81cb3079c0
* Pros and Cons
  + At this point, after four weeks of training and as we have reached the training plateau on the given set of Miami data, we can draw some conclusions: while the neural network prediction accuracy did not achieve the accuracy of human editors, the speed (60,000 segments per hour from a single NVIDIA Quadro GP100 GPU versus 70 per man hour) and negligible marginal cost at which neural network predictions can be produced, makes a pre-trained Mask R-CNN service a great helper tool which will significantly reduce the cost of creating and maintaining 3D city models. With this new tool in the workflow, human editors, instead of starting from rasterized LiDAR point cloud and manually digitizing roof segments, can now focus on fine tuning AI-offered 3D building multipatches using standard editing tools.


## **Multi-Net for Autonomous driving**
* road segmentation, classification and car detection
* http://mi.eng.cam.ac.uk/~cipolla/publications/inproceedings/2018-IV-multinet.pdf
* https://github.com/MarvinTeichmann/MultiNet
* https://towardsdatascience.com/road-scene-understating-using-deep-learning-c3610f6b1c4


## KittiSeg, KittiBox
- KittiSeg: road segmentation
- https://github.com/MarvinTeichmann/KittiSeg
- KittiBox a similar projects to perform state-of-the art detection. And finally the MultiNet repository contains code to jointly train segmentation, classification and detection. KittiSeg and KittiBox are utilized as submodules in MultiNet.


## Deep-learning On Aerial Imagery
* https://www.azavea.com/blog/2017/05/30/deep-learning-on-aerial-imagery/
* Parking Lot Vehicle Detection Using Deep Learning - https://medium.com/geoai/parking-lot-vehicle-detection-using-deep-learning-49597917bc4a
* https://github.com/crowdAI/crowdai-mapping-challenge-mask-rcnn
* https://www.crowdai.org/challenges/mapping-challenge - main for aerial imagery annotation
  * https://www.crowdai.org/challenges/mapping-challenge/dataset_files
* https://www.missingmaps.org/learn/


### Image to OSM
* https://github.com/jremillard/images-to-osm


### AI for GIS Tools
* https://github.com/ctu-geoforall-lab/i.ann.maskrcnn


### Satellite - Buildingfootprint extraction
* https://github.com/yorku-ausml/deep_satellite_image_segmentation
* http://openaccess.thecvf.com/content_cvpr_2018_workshops/papers/w4/Zhao_Building_Extraction_From_CVPR_2018_paper.pdf


### CrowdAI - Mapping Challange
* https://github.com/crowdAI/mapping-challenge-round2-starter-kit
* https://www.crowdai.org/challenges/mapping-challenge
* https://github.com/crowdAI/crowdai-mapping-challenge-mask-rcnn/blob/master/Prediction-and-Submission.ipynb

**Best Trained Model on satellite images**  
- https://github.com/neptune-ml/open-solution-mapping-challenge
- 0.943 Average Precision, 0.954 Average Recall
```bash
git clone https://github.com/neptune-ml/open-solution-mapping-challenge.git
#
## set paths in neptune.yaml
data_dir:              /path/to/data
meta_dir:              /path/to/data
masks_overlayed_prefix: masks_overlayed
experiment_dir:        /path/to/work/dir
#
## change erosion/dilation setup in neptune.yaml if you want to. Suggested setup
border_width: 0
small_annotations_size: 14
erode_selem_size: 0
dilate_selem_size: 0
#
## prepare target masks and metadata for training
python main.py -- prepare_masks
python main.py -- prepare_metadata --train_data --valid_data --test_data
#
## Train model
python main.py -- train --pipeline_name unet_weighted
#
## Evaluate model and predict on test data:
## Change values in the configuration file neptune.yaml. Suggested setup:
tta_aggregation_method: gmean
loader_mode: resize
erode_selem_size: 0
dilate_selem_size: 2
#
##
python main.py -- evaluate_predict --pipeline_name unet_tta --chunk_size 1000
```

train.tar.gz
Training Set : 280741 tiles (as 300x300 pixel RGB images) of satellite imagery with the corresponding annotations in MS COCO format

pretrained_weights.h5
Pretrained Weights from the Mask-rcnn based baseline solution

val.tar.gz
Validation Set : 60317 tiles (as 300x300 pixel RGB images) of satellite imagery with the corresponding annotations in MS COCO format

LICENSE.md
License under which this dataset is released

test_images.tar.gz
Test Set : 60697 tiles (as 300x300pixel RGB images) of satellite imagery

File Size
805 MB

```bash
Dataset location
Now we expect that you have downloaded all the files in the datasets section and untar-ed them to have the following structure :

├── data
|   ├── pretrained_weights.h5 (already included in this repository)
│   ├── test
│   │   └── images/
│   │   └── annotation.json
│   ├── train
│   │   └── images/
│   │   └── annotation.json
│   └── val
│       └── images/
│       └── annotation.json
```

## Mask-RCNN Hyperparameters
* epochs
* batch-size
* learning-rate
  * `0.01`, `0.001`
* weight decay
* regularization strength, weight decay
  * `1e-4`, `1e-3`
* data augmentation


**problems in training**
* high bias & high variance


**Reporting**
* mAP - mean Average Precision scores for each hyperparameters
* Average Precision  (AP)
* Average Recall     (AR)
* IoU


## Notes from Original Mask-RCNN Paper 

We report the standard COCO metrics including AP (averaged over IoU thresholds)
AP 50 , AP 75 , and AP S , AP M , AP L (AP at different scales)

AP is evaluating using mask IoU

we train using the union of 80k train images and a 35k subset of val images (trainval35k), and report ablations on the remaining 5k val images (minival). We also report results on test-dev


outperform baseline variants of previous state-of-the-art models.
This includes MNC [10] and FCIS the winners of the COCO 2015 and 2016 segmentation challenges, respectively
Mask R-CNN with ResNet-101-FPN backbone outperforms FCIS+++
which includes multi-scale train/test, horizontal flip test, and online hard example mining (OHEM)

Fully convolutional networks (FCN)
multi-layer perceptrons (MLP, fully-connected)

Backbone Architecture
* Better backbones bring expected gains: deeper networks do better, FPN outperforms C4 features, and ResNeXt improves on ResNet.
* It benefits from deeper networks (50 vs. 101) and advanced designs including FPN and ResNeXt.
* We note that not all frameworks automatically benefit from deeper or advanced networks

Experiments on Cityscapes:
* report instance segmentation results on the Cityscapes [7] dataset. This dataset has fine annotations for 2975 train, 500 val, and 1525 test images. It has 20k coarse training images without instance annotations, which we do not use.
* All images are 2048×1024 pixels
* The instance segmentation task involves 8 object categories
* numbers of instances on the fine training set are
  * person: 17.9k
  * rider: 1.8k
  * car: 26.9k
  * truck: 0.5k
  * bus: 0.4k
  * train: 0.2k
  * mcycle: 0.7k
  * bicycle: 3.7k
* Instance segmentation performance on this task is measured by the COCO-style mask AP (averaged over IoU thresholds); AP 50 (i.e., mask AP at an IoU of 0.5) is also reported

* Mask R-CNN models with the ResNet-FPN-50 backbone; we found the 101-layer counterpart performs similarly due to the small dataset size We train with image scale (shorter side) randomly sampled from [800, 1024], which reduces overfitting; inference is on a single scale of 1024 pixels.
* We use a mini-batch size of 1 image per GPU (so 8 on 8 GPUs) and train the model for 24k iterations, starting from a learning rate of 0.01 and reducing it to 0.001 at 18k iterations. It takes ∼ 4 hours of training on a single 8-GPU machine under this setting
* Without using the coarse training set, our method achieves 26.2 AP on test, which is over 30% relative improvement over the previous best en- try (DIN), and is also better than the concurrent work of SGN’s 25.0.
* Both DIN and SGN use fine + coarse data. Compared to the best entry using fine data only (17.4 AP), we achieve a ∼ 50% improvement
* For the person and car categories, the Cityscapes dataset exhibits a large number of within-category overlapping instances (on average 6 people and 9 cars per image)
* We argue that within-category overlap is a core difficulty of instance segmentation. Our method shows massive improvement on these two categories over the other best entries (relative ∼ 40% improvement on person from 21.8 to 30.5 and ∼ 20% improvement on car from 39.4 to 46.9), even though our method does not exploit the coarse data
* A main challenge of the Cityscapes dataset is training models in a low-data regime, particularly for the categories of truck, bus, and train, which have about 200-500 traiing samples each
* We show that using COCO pretraining is an effective strategy on this dataset.
* initialize the corresponding 7 categories in Cityscapes from a pre-trained COCO Mask R-CNN model (rider being randomly initialized). We fine-tune this model for 4k iterations in which the learning rate is reduced at 3k iterations, which takes ∼ 1 hour for training given the COCO model
* This indicates the important role the amount of training data plays
* we observed a bias between the val and test AP
* found that this **bias** is mainly caused by the truck, bus, and train categories, with the fine-only model having val/test AP of 28.8/22.8, 53.5/32.2, and 33.0/18.6, respectively
* This suggests that there is a **domain shift** on these categories, which also have little training data
* for the person and car categories we do not see any such bias (val/test AP are within ±1 point)


* ImageNet-5k pre-training
* Scale augmentation at train time further improves results
* During training, we randomly sample a scale from [640, 800] pixels and we increase the number of iterations to 260k (with the learning rate reduced by 10 at 200k and 240k iterations)
* upgrading the 101-layer ResNeXt to its 152-layer counterpart deeper model can still improve results on COCO
* recently proposed non-local (NL) model [43], we achieve 40.3 mask AP and 45.0 box AP
```
BACKBONE_SHAPES 
[
  [512 512]
  [256 256]
  [128 128]
  [ 64 64]
  [ 32 32]
]
DETECTION_MIN_CONFIDENCE 0.7
IMAGE_MAX_DIM 2048
IMAGE_MIN_DIM 800
IMAGE_PADDING True
IMAGE_SHAPE [2048 2048 3]
MINI_MASK_SHAPE (224, 224)
LEARNING_RATE 0.002
MASK_SHAPE [56, 56]
MINI_MASK_SHAPE (224, 224)
TRAIN_ROIS_PER_IMAGE 128
```
* `build_rpn_targets`
* `./mrcnn/utils.py`
  * `compute_ap`
    ```python
    """Compute Average Precision at a set IoU threshold (default 0.5).
    Returns:
    mAP: Mean Average Precision
    precisions: List of precisions at different class score thresholds.
    recalls: List of recall values at different class score thresholds.
    overlaps: [pred_boxes, gt_boxes] IoU overlaps.
    """
    ```
  * `compute_ap_range`
  * `compute_recall`
* `./mrcnn/visualize.py`
  * `plot_precision_recall`
  * `plot_overlaps`
* Convolution layers are independent of the input size; only their kernel size matter.


**Anchors**
```python
# BACKBONE                       resnet101

backbone_shapes = modellib.compute_backbone_shapes(config, config.IMAGE_SHAPE)

 # [[480 480]
 # [240 240]
 # [120 120]
 # [ 60  60]
 # [ 30  30]]

# BACKBONE_STRIDES               [4, 8, 16, 32, 64]
# RPN_ANCHOR_SCALES              (32, 64, 128, 256, 512)
# RPN_ANCHOR_RATIOS              [0.5, 1, 2]
# RPN_ANCHOR_STRIDE              1
anchors = utils.generate_pyramid_anchors(config.RPN_ANCHOR_SCALES, 
                                          config.RPN_ANCHOR_RATIOS,
                                          backbone_shapes,
                                          config.BACKBONE_STRIDES, 
                                          config.RPN_ANCHOR_STRIDE)

## utils.generate_anchors

## model.py

<!-- [x, y, width, height] i.e. [left, top, width, height] -->

@build_rpn_targets`
# Handle COCO crowds
# A crowd box in COCO is a bounding box around several instances. Exclude
# them from training. A crowd box is given a negative class ID.
```

* Frequently used Numpy Functions:
```bash
np.zeros
np.ones
np.where
np.amax
np.argmax
np.arange
np.sum
np.random.choice
np.random.randint
np.random.shuffle
np.split
np.sort
np.abs
np.hstack
np.copy
np.any
```


## Extras

* How to calculate the dice coefficient or hausdorff distance of output of test images?
* http://www.wad.ai/challenge.html
* https://research.mapillary.com/publication/cvpr18a/
* http://pyparis.org/static/slides/Rapha%C3%ABl%20Delhome-2d4267d1.pdf
* https://github.com/mapillary/mapillary_vistas 
* https://github.com/parachutel/deeplabv3plus_on_Mapillary_Vistas
* http://densepose.org/
* https://docs.supervise.ly/neural-networks/examples/mask_rcnn/
* https://supervise.ly/
* https://deepsystems.ai/
* https://www.cityscapes-dataset.com/benchmarks/
* https://roadbotics.com
* https://deepsystems.ai/solutions/road-defects-detection


## **Matterport - Mask-RCNN Training**
- https://archive.org/details/github.com-matterport-Mask_RCNN_-_2017-11-03_10-28-11
- https://stackoverflow.com/questions/49684468/mask-r-cnn-for-object-detection-and-segmentation-train-for-a-custom-dataset
* You need to have all your annotations.
* All of those need to be converted to VGG Polygon schema (yes i mean polygons). I have added a sample VGG Polygon format at the end of this answer.
* You need to divide your custom dataset into train, test and val
* The annotation by default are looked with a filename via_region_data.json inside the individual dataset folder. For eg for training images it would look at train\via_region_data.json. You can also change it if you want.
* Inside Samples folder you can find folders like Balloon, Nucleus, Shapes etc. Copy one of the folders. Preferably balloon. We will now try to modify this new folder for our custom dataset.
* Inside the copied folder, you will have a .py file (for balloon it will be balloon.py), change the following variables
* ROOT_DIR : the absolute path where you have cloned the project
* DEFAULT_LOGS_DIR : This folder will get bigger in size so change this path accordingly (if you are running your code in a low disk storage VM). It will store the .h5 file as well. It will make subfolder inside the log folder with timestamp attached to it.
* `.h5` files are roughly 200 - 300 MB per epoch. But guess what this log directory is Tensorboard compatible. You can pass the timestamped subfolder as --logdir argument while running tensorboard.
* This `.py` file also has two classes - one class with suffix as Config and another class with suffix as Dataset.
* https://codesign.blog/2018/07/11/mask-r-cnn-mask-r-cnn-for-object-detection-and-instance-segmentation-on-keras-and-tensorflow-2/
```python
vars(dataset).keys()
dict_keys(['_image_ids', 'image_info', 'class_info', 'source_class_ids', 'num_classes', 'class_ids', 'class_names', 'num_images', 'class_from_source_map', 'image_from_source_map', 'sources'])
```
* http://www.immersivelimit.com/tutorials/using-mask-r-cnn-on-custom-coco-like-dataset
* https://patrickwasp.com/train-a-mask-r-cnn-model-on-your-own-dataset/
  * **Mask-rcnn results back to COCO format**
    * https://github.com/waspinator/deep-learning-explorer/blob/master/mask-rcnn/notebooks/mask_rcnn.ipynb


## Errors

* https://medium.com/@lisulimowicz/tensorflow-cpus-and-gpus-configuration-9c223436d4ef
* https://databricks.com/tensorflow/using-a-gpu
* https://github.com/matterport/Mask_RCNN/issues/635


## https://github.com/matterport/Mask_RCNN/issues/849
```bash
Loading weights  $HOME/ai-ml-dl/external/Mask_RCNN/logs/coco20181128T1811/mask_rcnn_coco_0002.h5
Traceback (most recent call last):
  File "road.py", line 580, in <module>
    model.load_weights(weights_path, by_name=True)
  File "$HOME/ai-ml-dl/external/Mask_RCNN/mrcnn/model.py", line 2130, in load_weights
    saving.load_weights_from_hdf5_group_by_name(f, layers)
  File "/usr/local/lib/python3.6/dist-packages/keras/engine/saving.py", line 1017, in load_weights_from_hdf5_group_by_name
    str(weight_values[i].shape) + '.')
ValueError: Layer #391 (named "mrcnn_bbox_fc"), weight <tf.Variable 'mrcnn_bbox_fc/kernel:0' shape=(1024, 8) dtype=float32_ref> has shape (1024, 8), but the saved weight has shape (1024, 324).
```

### https://github.com/matterport/Mask_RCNN/issues/566
* `from keras.engine import topology`
* change it to: `from keras.engine import saving`


### In the Visualize Activations section
  * InvalidArgumentError: input_image:0 is both fed and fetched.
  * https://github.com/matterport/Mask_RCNN/issues/934
  * https://stackoverflow.com/questions/39307108/placeholder-20-is-both-fed-and-fetched
  * https://github.com/matterport/Mask_RCNN/pull/1211
  * Fix:
    - https://github.com/matterport/Mask_RCNN/pull/1211/commits/4cdc5014d3aa58e770080f84caf6ec51aa791d02

### Error when checking input: expected input_image_meta to have shape (13,) but got array with shape (27,)
* https://github.com/matterport/Mask_RCNN/issues/514
* https://github.com/matterport/Mask_RCNN/issues/899
* https://github.com/matterport/Mask_RCNN/issues/410
```bash
#
$HOME/virtualmachines/virtualenvs/py_3-6-5_2018-11-20/lib/python3.6/site-packages/tensorflow/python/ops/gradients_impl.py:112: UserWarning: Converting sparse IndexedSlices to a dense Tensor of unknown shape. This may consume a large amount of memory.
  "Converting sparse IndexedSlices to a dense Tensor of unknown shape. "
#
$HOME/virtualmachines/virtualenvs/py_3-6-5_2018-11-20/lib/python3.6/site-packages/keras/engine/training_generator.py:47: UserWarning: Using a generator with `use_multiprocessing=True` and multiple workers may duplicate your data. Please consider using the`keras.utils.Sequence class.
  UserWarning('Using a generator with `use_multiprocessing=True`'
```

### Keras Training Stops at First Epoch When using CNNs
* https://github.com/keras-team/keras/issues/9476
* https://stackoverflow.com/questions/51557940/python-keras-cnn-stuck-on-epoch-1
* https://github.com/matterport/Mask_RCNN/issues/287
* https://github.com/keras-team/keras/issues/8595#issuecomment-416111215
* https://github.com/matterport/Mask_RCNN/issues/1105

### OOM
```
    self._session._session, self._handle, args, status, None)
  File "/home/alpha/virtualmachines/virtualenvs/py_3-6-5_2018-11-21/lib/python3.6/site-packages/tensorflow/python/framework/errors_impl.py", line 519, in __exit__
    c_api.TF_GetCode(self.status.status))
tensorflow.python.framework.errors_impl.ResourceExhaustedError: OOM when allocating tensor with shape[1,512,480,480] and type float on /job:localhost/replica:0/task:0/device:GPU:0 by allocator GPU_0_bfc
   [[Node: rpn_model/rpn_conv_shared/convolution = Conv2D[T=DT_FLOAT, _class=["loc:@train...propFilter"], data_format="NCHW", dilations=[1, 1, 1, 1], padding="SAME", strides=[1, 1, 1, 1], use_cudnn_on_gpu=true, _device="/job:localhost/replica:0/task:0/device:GPU:0"](fpn_p2/BiasAdd, rpn_conv_shared/kernel/read)]]
Hint: If you want to see a list of allocated tensors when OOM happens, add report_tensor_allocations_upon_oom to RunOptions for current allocation info.

   [[Node: mul_262/_5269 = _Recv[client_terminated=false, recv_device="/job:localhost/replica:0/task:0/device:CPU:0", send_device="/job:localhost/replica:0/task:0/device:GPU:0", send_device_incarnation=1, tensor_name="edge_21888_mul_262", tensor_type=DT_FLOAT, _device="/job:localhost/replica:0/task:0/device:CPU:0"]()]]
Hint: If you want to see a list of allocated tensors when OOM happens, add report_tensor_allocations_upon_oom to RunOptions for current allocation info.
```
* https://github.com/keras-team/keras/issues/4161
* https://stackoverflow.com/questions/51960471/where-is-the-session-created-in-mask-rcnn
* https://github.com/matterport/Mask_RCNN/issues/225
```python
import tensorflow as tf
from keras.backend.tensorflow_backend import set_session
tf_config = tf.ConfigProto()
tf_config.gpu_options.per_process_gpu_memory_fraction = 0.2
set_session(tf.Session(config=tf_config))
```

  File "/home/alpha/virtualmachines/virtualenvs/py_3-6-5_2018-11-21/lib/python3.6/site-packages/tensorflow/python/client/session.py", line 1340, in _extend_graph
    tf_session.ExtendSession(self._session)
tensorflow.python.framework.errors_impl.InvalidArgumentError: Cannot assign a device for operation 'ROI/rpn_non_max_suppression/NonMaxSuppressionV3': Could not satisfy explicit device specification '/device:GPU:0' because no supported kernel for GPU devices is available.
Registered kernels:
  device='CPU'

https://github.com/tensorflow/tensorflow/issues/2292

* `tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)`

```
config = tf.ConfigProto()
config.gpu_options.allocator_type = 'BFC'
config.gpu_options.allow_growth = True
with tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)) as sess:
```


* https://stackoverflow.com/questions/44813939/could-not-satisfy-explicit-device-specification-devicegpu0-because-no-devic
Try using sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)). This will resolve the problem if it couldn't place an operation on the GPU. Since some operations have only CPU implementation.

Using allow_soft_placement=True will allow TensorFlow to fall back to CPU when no GPU implementation is available.


```
2019-02-26 01:03:18.634030: I tensorflow/core/common_runtime/bfc_allocator.cc:680] Stats: 
Limit:                  1701026201
InUse:                  1655737344
MaxInUse:               1661266176
NumAllocs:                    2822
MaxAllocSize:             51380224

2019-02-26 01:03:18.634074: W tensorflow/core/common_runtime/bfc_allocator.cc:279] **************************************************************************************************__
2019-02-26 01:03:18.634094: W tensorflow/core/framework/op_kernel.cc:1318] OP_REQUIRES failed at conv_ops.cc:398 : Resource exhausted: OOM when allocating tensor with shape[1,64,960,960] and type float on /job:localhost/replica:0/task:0/device:GPU:0 by allocator GPU_0_bfc
Traceback (most recent call last):
  File "train.py", line 359, in <module>
    main(args)
  File "train.py", line 352, in main
    train(mode, cfg)
  File "train.py", line 143, in train
    layers=stage.LAYERS)
  File "/home/alpha/Documents/ai-ml-dl/external/Mask_RCNN/mrcnn/model.py", line 2391, in train
    use_multiprocessing=True,
  File "/home/alpha/virtualmachines/virtualenvs/py_3-6-5_2018-11-21/lib/python3.6/site-packages/keras/legacy/interfaces.py", line 91, in wrapper
    return func(*args, **kwargs)
  File "/home/alpha/virtualmachines/virtualenvs/py_3-6-5_2018-11-21/lib/python3.6/site-packages/keras/engine/training.py", line 1415, in fit_generator
    initial_epoch=initial_epoch)
  File "/home/alpha/virtualmachines/virtualenvs/py_3-6-5_2018-11-21/lib/python3.6/site-packages/keras/engine/training_generator.py", line 213, in fit_generator
    class_weight=class_weight)
  File "/home/alpha/virtualmachines/virtualenvs/py_3-6-5_2018-11-21/lib/python3.6/site-packages/keras/engine/training.py", line 1215, in train_on_batch
    outputs = self.train_function(ins)
  File "/home/alpha/virtualmachines/virtualenvs/py_3-6-5_2018-11-21/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py", line 2666, in __call__
    return self._call(inputs)
  File "/home/alpha/virtualmachines/virtualenvs/py_3-6-5_2018-11-21/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py", line 2636, in _call
    fetched = self._callable_fn(*array_vals)
  File "/home/alpha/virtualmachines/virtualenvs/py_3-6-5_2018-11-21/lib/python3.6/site-packages/tensorflow/python/client/session.py", line 1454, in __call__
    self._session._session, self._handle, args, status, None)
  File "/home/alpha/virtualmachines/virtualenvs/py_3-6-5_2018-11-21/lib/python3.6/site-packages/tensorflow/python/framework/errors_impl.py", line 519, in __exit__
    c_api.TF_GetCode(self.status.status))
tensorflow.python.framework.errors_impl.ResourceExhaustedError: OOM when allocating tensor with shape[1,64,960,960] and type float on /job:localhost/replica:0/task:0/device:GPU:0 by allocator GPU_0_bfc
   [[Node: conv1/convolution = Conv2D[T=DT_FLOAT, data_format="NCHW", dilations=[1, 1, 1, 1], padding="VALID", strides=[1, 1, 2, 2], use_cudnn_on_gpu=true, _device="/job:localhost/replica:0/task:0/device:GPU:0"](conv1/convolution-0-TransposeNHWCToNCHW-LayoutOptimizer, conv1/kernel/read)]]
Hint: If you want to see a list of allocated tensors when OOM happens, add report_tensor_allocations_upon_oom to RunOptions for current allocation info.

   [[Node: mul_262/_5269 = _Recv[client_terminated=false, recv_device="/job:localhost/replica:0/task:0/device:CPU:0", send_device="/job:localhost/replica:0/task:0/device:GPU:0", send_device_incarnation=1, tensor_name="edge_21888_mul_262", tensor_type=DT_FLOAT, _device="/job:localhost/replica:0/task:0/device:CPU:0"]()]]
Hint: If you want to see a list of allocated tensors when OOM happens, add report_tensor_allocations_upon_oom to RunOptions for current allocation info.
```
