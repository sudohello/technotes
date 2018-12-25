

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
Loading weights  /home/alpha/Documents/ai-ml-dl/external/Mask_RCNN/logs/coco20181128T1811/mask_rcnn_coco_0002.h5
Traceback (most recent call last):
  File "road.py", line 580, in <module>
    model.load_weights(weights_path, by_name=True)
  File "/home/alpha/Documents/ai-ml-dl/external/Mask_RCNN/mrcnn/model.py", line 2130, in load_weights
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

