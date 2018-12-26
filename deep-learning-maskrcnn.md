

## **Mask-RCNN**
  - https://github.com/priya-dwivedi/Deep-Learning
  - https://github.com/facebookresearch/Detectron
  - https://github.com/matterport/Mask_RCNN
  - https://github.com/matterport/Mask_RCNN/releases
    ```
    sudo pip3 install pycocotools imgaug IPython[all]
    ```
  - https://github.com/CharlesShang/FastMaskRCNN - just for basics
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


mask-rcnn-iccv-2017-author-kaiminppt
* https://www.youtube.com/watch?v=g7z4mkfRjI4&list=PLe6h2Vdf1gFENsJ0W2bUlOGoLWrZdzK8n

* https://www.youtube.com/watch?v=Ul25zSysk2A&list=PLkRkKTC6HZMxZrxnHUDYSLiPZxiUUFD2C
* https://www.youtube.com/watch?v=UdZnhZrM2vQ&list=PLjh3zPDW5j_v20KQvJb9Q5puTC4AjK7jK



* https://github.com/matterport/Mask_RCNN/wiki


https://www.reddit.com/r/MachineLearning/comments/8mqywx/best_implementation_of_mask_rcnn_p/



### Mask-rcnn Docker
* https://github.com/waspinator/deep-learning-explorer/tree/master/mask-rcnn

### **matterport/Mask_RCNN**
- https://github.com/matterport/Mask_RCNN
- https://github.com/matterport/Mask_RCNN/releases
- https://github.com/matterport/Mask_RCNN/wiki

* how the model works and show how to use it in a real application.
* uses a ResNet101 + FPN backbone.
* Region Proposal Network (RPN)
  * The RPN is a lightweight neural network that scans the image in a sliding-window fashion and finds areas that contain objects. If several anchors overlap too much, we keep the one with the highest foreground score and discard the rest (referred to as Non-max Suppression - NMS)

#### **Mask-RCNN Training**
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

**Case Studies**
* **splash-of-color-instance-segmentation-with-mask-r-cnn-and-tensorflow**
  * https://engineering.matterport.com/splash-of-color-instance-segmentation-with-mask-r-cnn-and-tensorflow-7c761e238b46
  - baloon: done
* video
  * https://github.com/priya-dwivedi/Deep-Learning/blob/master/Mask_RCNN/Mask_RCNN_Videos.ipynb


```python
vars(dataset).keys()
dict_keys(['_image_ids', 'image_info', 'class_info', 'source_class_ids', 'num_classes', 'class_ids', 'class_names', 'num_images', 'class_from_source_map', 'image_from_source_map', 'sources'])
```

* http://www.immersivelimit.com/tutorials/using-mask-r-cnn-on-custom-coco-like-dataset
* https://patrickwasp.com/train-a-mask-r-cnn-model-on-your-own-dataset/
  * **Mask-rcnn results back to COCO format**
    * https://github.com/waspinator/deep-learning-explorer/blob/master/mask-rcnn/notebooks/mask_rcnn.ipynb

#### Issues
* https://github.com/matterport/Mask_RCNN/issues/849
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


#### Images to OSM
* https://github.com/jremillard/images-to-osm


#### Applications in other projects:
* 4K video
  * https://www.youtube.com/watch?v=OOT3UIXZztE
  * https://github.com/karolmajek/Mask_RCNN
* Segmenting Nuclei in Microscopy Images.  - https://github.com/matterport/Mask_RCNN/tree/master/samples/nucleus
* splash of color
* image to osm - https://github.com/jremillard/images-to-osm
* Reconstructing 3D buildings from aerial LiDAR
  - https://medium.com/geoai/reconstructing-3d-buildings-from-aerial-lidar-with-ai-details-6a81cb3079c0
  - Pros and Cons
    * At this point, after four weeks of training and as we have reached the training plateau on the given set of Miami data, we can draw some conclusions: while the neural network prediction accuracy did not achieve the accuracy of human editors, the speed (60,000 segments per hour from a single NVIDIA Quadro GP100 GPU versus 70 per man hour) and negligible marginal cost at which neural network predictions can be produced, makes a pre-trained Mask R-CNN service a great helper tool which will significantly reduce the cost of creating and maintaining 3D city models. With this new tool in the workflow, human editors, instead of starting from rasterized LiDAR point cloud and manually digitizing roof segments, can now focus on fine tuning AI-offered 3D building multipatches using standard editing tools.

**Car Damage**
* https://www.analyticsvidhya.com/blog/2018/07/building-mask-r-cnn-model-detecting-damage-cars-python/


**Multi-Net for Autonomous driving**
* road segmentation, classification and car detection
* http://mi.eng.cam.ac.uk/~cipolla/publications/inproceedings/2018-IV-multinet.pdf
* https://github.com/MarvinTeichmann/MultiNet
* https://towardsdatascience.com/road-scene-understating-using-deep-learning-c3610f6b1c4

**KittiSeg, KittiBox**
- KittiSeg: road segmentation
- https://github.com/MarvinTeichmann/KittiSeg
- KittiBox a similar projects to perform state-of-the art detection. And finally the MultiNet repository contains code to jointly train segmentation, classification and detection. KittiSeg and KittiBox are utilized as submodules in MultiNet.


**deep-learning-on-aerial-imagery**
* https://www.azavea.com/blog/2017/05/30/deep-learning-on-aerial-imagery/
* Parking Lot Vehicle Detection Using Deep Learning - https://medium.com/geoai/parking-lot-vehicle-detection-using-deep-learning-49597917bc4a
* https://github.com/crowdAI/crowdai-mapping-challenge-mask-rcnn
* https://www.crowdai.org/challenges/mapping-challenge - main for aerial imagery annotation
  * https://www.crowdai.org/challenges/mapping-challenge/dataset_files
* https://www.missingmaps.org/learn/


* CrowdAI - Mapping Challange
  - https://github.com/crowdAI/mapping-challenge-round2-starter-kit
  - https://www.crowdai.org/challenges/mapping-challenge
  - https://github.com/crowdAI/crowdai-mapping-challenge-mask-rcnn/blob/master/Prediction-and-Submission.ipynb

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
Pretrained Weights from the Mask RCNN based baseline solution

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
* https://github.com/matterport/Mask_RCNN/issues/566
  - `from keras.engine import topology`
  - change it to: `from keras.engine import saving`


**AI for GIS Tools**
https://github.com/ctu-geoforall-lab/i.ann.maskrcnn


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

Average Precision  (AP)
Average Recall     (AR)
IoU


https://stackoverflow.com/questions/36274638/map-metric-in-object-detection-and-computer-vision

## Setting up datasets links for Mask-Rcnn:

```bash
MRCNN_ROOT=$AI_HOME/external/Mask_RCNN
# cd $MRCNN_ROOT/datasets
wget -c https://github.com/matterport/Mask_RCNN/releases/download/v2.1/balloon_dataset.zip -P $AI_DATA/data/balloon_dataset.zip
unzip -q $AI_DATA/data/balloon_dataset.zip -d $AI_DATA/data/balloon_dataset
mkdir $MRCNN_ROOT/datasets
ln -s $AI_DATA/data/balloon_dataset/balloon $MRCNN_ROOT/datasets/balloon
ln -s $AI_DATA/data/ms-coco $MRCNN_ROOT/datasets/coco
ln -s $AI_DATA/data/crowd-ai-mapping $MRCNN_ROOT/datasets/crowd-ai-mapping
```

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



https://github.com/matterport/Mask_RCNN/issues/635


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
```



https://github.com/benjamintanweihao/mask-rcnn-webcam