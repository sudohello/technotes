
### ApolloScape - Apollo Dataset
- Refer: [apolloscape-dataset.md](apolloscape-dataset.md)
- https://arxiv.org/pdf/1803.06184.pdf
- ApolloScape, billed as the world’s largest open-source dataset for autonomous driving technology.
- http://apolloscape.auto/index.html
- provided by Baidu, Inc.
- Scene Parsing
- Includes:
  * RGB videos
  * high resolution images
  * per pixel annotation
  * survey- grade dense 3D points with semantic segmentation
  * stereoscopic video
  * panoramic images
  * continuous collection will:
    * further add more sensors, such as stereoscopic video and panoramic images;
    * and cover a wide range of environment, weather, and traffic conditions.
- http://apolloscape.auto/scene.html

**Summary**
- mid-size SUV with high resolution cameras and a Riegl acquisition system. 
- each image is tagged with high-accuracy pose information at cm accuracy
- and the static background point cloud has mm relative accuracy. 
- not limited to 2D/3D scene understanding, localization, transfer learning, and driving simulation
- Image frames in our dataset are collected every one meter by our acquisition system with resolution 3384 x 2710
- It is expected that the released dataset will include 200K image frames with corresponding pixel-level annotations and pose information. Instance-level annotations are available for a subset of the dataset. Depth maps for static background will also be provided.
- As of March 8, 2018, released the first part of the dataset that contains 74555 video frames and their pixel-level and instance-level annotations.
- On March 21, 2018, added the second part of the data set, including 43592 depth images for static background of road01_ins and road02_ins
- On April 03, 2018，the Scene Parsing data set cumulatively provides 146,997 frames with corresponding pixel-level annotations and pose information，depth maps for static background.
- The dataset is divided into three subsets for training, validation and testing respectively
- The semantic annotations for testing images are not provided.
- All the pixels in the ground truth annotations for testing images are labeled as 255
- The files that contain image lists of training, validation, and testing subsets will be provided soon.

**Class Definitions**
* 25 different labels covered by five groups
  * Others
  * Sky
  * movable object
  * flat
  * Road obstacles
  * Roadside objects
  * void
  * Building
  * Natural
  * Unlabeled
*  There are two IDs, class ID and train ID, assigned to each pixel. The train ID is the one used for training and can be modified as needed. The value 255 indicates the ignoring labels that currently are not evaluated during the testing phase. The class ID is used to represent the label in ground truth labels
