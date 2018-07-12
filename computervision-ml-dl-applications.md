/*
Title: Computer Vision ML, DL Applications
Decription: Computer Vision ML, DL Applications
Author: Bhaskar Mangal
Date: 30 Jun 2018
Last Updated: 12 Jul 2018
Tags: Computer Vision ML, DL Applications
*/

# Computer Vision
**Provide APIs in Computer Vision using Deep Learning for Geospatial Industry**
* [Programme Slides](https://github.com/mangalbhaskar/dia/blob/master/AI-programme-slides.pdf)

## Problem Statements
1. Signage Layer Extraction for Map
  * a. Trees, Signage, Road Signs,Traffic
  Signals, Poles
  * b. In combination with photogrammetry
  (point clouds) to get higher accurate
  geolocation
2. Number Plate Recognition
  **Potential use cases:**
  * a. In traffic camera feeds for traffic
  rules violation detection
  * b. Toll both automation
3. Vehicle Detection & Recognition
**Potential use cases:**
* a. In traffic camera feeds
   ­ - Vehicle counts
   ­ - Traffic density estimation
* b. Parking lots vacancy detection
* c. Accident / collision detection
4. Pedestrian Detection & Face Recognition
**Potential use cases:**
* a. Surveillance & security like ATM,
Malls, Real Estate
5. Road Profile Extraction for Map
**Potential use cases:**
* a. Edge detection ­ road, footpath,
road markings
* b. In combination with photogrammetry
(point clouds) to get higher accurate
geolocation
6. Cross­road / Junction Identification
7. Text Extraction for Signage Layer
8. Complete Urban scene Classification & Segmentation
9. Content retrieval based on above 

**Other problem statements**
- Face detection 
- Removing motion blur
- Assisted Driving
  * Pedistrian and Car Detection
  * Lane Detection
    - Collision warning systems with adaptive cruise control
    - Lane departure warning systems
    - Rear object detection systems
- Iris recogni@on
- Visually defined search
- Object search in video
- Visual descrip@on – visual words
- Image representa@on using visual words
- Organizing photo collections
- Visual dictionary

## Setup
* [System Setup - start here](https://github.com/mangalbhaskar/linuxscripts/blob/master/README.md#start-here---the-big-bang-theory)
* [Getting Started for Image Processing, Computer Vision, Machine Learning and Deep Learning for GIS](https://github.com/mangalbhaskar/technotes#getting-started-for-image-processing-computer-vision-machine-learning-and-deep-learning-for-gis)

## Study Materials
* [Getting Started for Image Processing, Computer Vision, Machine Learning and Deep Learning for GIS](https://github.com/mangalbhaskar/technotes#getting-started-for-image-processing-computer-vision-machine-learning-and-deep-learning-for-gis)

### **Image processing, Computer Vision**
* [Computer Vision](https://github.com/mangalbhaskar/technotes/blob/master/computer-vision.md)
* [Image Processing](https://github.com/mangalbhaskar/technotes/blob/master/image-processing.md)
* [OpenCV with Python](https://github.com/mangalbhaskar/technotes/blob/master/opencv-with-python.md)
* [Photogrammetry](https://github.com/mangalbhaskar/technotes/blob/master/photogrammetry.md)
* [visualSfM](https://github.com/mangalbhaskar/technotes/blob/master/visualSfM.md)
* [SLAM](https://github.com/mangalbhaskar/technotes/blob/master/slam.md)
* [Image based Navigation](https://github.com/mangalbhaskar/technotes/blob/master/image-based-navigation.md)

### **Deep Learning**
* [AI Programme Slides](https://github.com/mangalbhaskar/dia/blob/master/AI-programme-slides.pdf)
* [AI ML DL Problem Statements](https://github.com/mangalbhaskar/technotes/blob/master/ai-ml-dl-problem-statements.md)
* [Deep Learning](https://github.com/mangalbhaskar/technotes/blob/master/deep-learning.md)
* [Deep Learning Applications](https://github.com/mangalbhaskar/technotes/blob/master/deep-learning-applications.md)
* [Tensorflow](https://github.com/mangalbhaskar/technotes/blob/master/tensorflow.md)
* [mechanics-of-self-driving-car](https://github.com/mangalbhaskar/technotes/blob/master/mechanics-of-self-driving-car.md)

### **Machine Learning**
* [Machine Learning](https://github.com/mangalbhaskar/technotes/blob/master/machine-learning.md)
* [ML for Mobile and Web Applications](https://github.com/mangalbhaskar/technotes/blob/master/ml-for-mobile-and-web-applications.md)
* [CBIR](https://github.com/mangalbhaskar/technotes/blob/master/cbir.ml.md)

### **Mathematics, Statistics and Statistical Learning**
* [Statistics](https://github.com/mangalbhaskar/technotes/blob/master/stats.md)
* [Introduction to Statistical Learning Using R - ISLR (Book notes)](https://github.com/mangalbhaskar/technotes/blob/master/islr-book-notes.md)
* [Mathematics](https://github.com/mangalbhaskar/technotes/blob/master/maths.md)

### **Data Analytics and Visualization**
* [D3.js](https://github.com/mangalbhaskar/technotes/blob/master/d3.js.md)
* [Data Analytics](https://github.com/mangalbhaskar/technotes/blob/master/data-analytics.md)
* [Data Visualization in Web](https://github.com/mangalbhaskar/technotes/blob/master/data-visualization-in-web.md)

## Dataset / Data source/ Datasource for ML

### Computer Vision Datasets
- https://projet.liris.cnrs.fr/voir/wiki/doku.php?id=datasets
- https://handong1587.github.io/computer_vision/2015/09/24/datasets.html

#### Traffic Sign
**Datasets**
* German
  - http://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset
* LISA: Laboratory for Intelligent Safe Automobiles
  - http://cvrr.ucsd.edu/LISA/lisa-traffic-sign-dataset.html
* Belgium
  - https://btsd.ethz.ch/shareddata/
  - The images in this dataset are in an old .ppm format
  - Images are square-ish, but have different aspect ratios
  - The image quality is great, and there are a variety of angles and lighting conditions
  - The traffic signs occupy most of the area of each image, which allows to focus on object classification and not have to worry about finding the location of the traffic sign in the image (object detection).
  - Generally, neural network will take a fixed-size input, so some preprocessing is required.
  - Dataset considers all speed limit signs to be of the same class, regardless of the numbers on them. That’s fine, as long as we know about it beforehand and know what to expect.
  - Labels 26 and 27 are interesting to check
  - What are the sizes of the images? - The sizes seem to hover around 128x128.
  - This tells me that the image colors are the standard range of 0–255.

**self-driving-car-datasets-semantic-segmentation**
- https://blog.playment.io/self-driving-car-datasets-semantic-segmentation/
* [CamVid](http://mi.eng.cam.ac.uk/research/projects/VideoRec/CamVid/)
  - http://mi.eng.cam.ac.uk/research/projects/VideoRec/CamVid/
* [KITTI - Karlsruhe Institute of Technology and Toyota Technological Institute](http://www.cvlibs.net/datasets/kitti/)
  - http://www.cvlibs.net/datasets/kitti/
  - http://www.cvlibs.net/datasets/kitti/eval_road.php
* [DUS - Daimler Urban Segmentation](http://www.6d-vision.com/scene-labeling)
  - http://www.6d-vision.com/scene-labeling
  - http://www.6d-vision.com/home
* [CityScapes](https://www.cityscapes-dataset.com/)
  - https://www.cityscapes-dataset.com/
  - https://www.cityscapes-dataset.com/benchmarks/
* [Mapillary Vista](https://blog.mapillary.com/product/2017/05/03/mapillary-vistas-dataset.html)
  - https://blog.mapillary.com/product/2017/05/03/mapillary-vistas-dataset.html
  - https://www.mapillary.com/dataset/vistas
* [Synthia](http://synthia-dataset.com/download-2/)
  - http://synthia-dataset.net/ 

### Others
- https://en.wikipedia.org/wiki/List_of_datasets_for_machine_learning_research
* Free datasets are available from places like Kaggle.com and UCI. 
  - https://www.kaggle.com/datasets
  - https://archive.ics.uci.edu/ml/datasets.html

## Traffic Light
* https://medium.freecodecamp.org/recognizing-traffic-lights-with-deep-learning-23dae23287cc
  - https://github.com/davidbrai/deep-learning-traffic-lights
  - https://challenge.getnexar.com/challenge-1
  - https://arxiv.org/abs/1602.07360

## Traffic Sign
* https://arxiv.org/pdf/1712.04391.pdf
* https://hackernoon.com/traffic-signs-classification-with-deep-learning-b0cb03e23efb
* http://www.deeplearningbook.org/
* https://towardsdatascience.com/recognizing-traffic-signs-with-over-98-accuracy-using-deep-learning-86737aedc2ab
* https://github.com/chandansaha2014/Real-time-Traffic-Sign-Recognition
* https://becominghuman.ai/build-a-neural-network-based-traffic-sign-classification-system-with-98-5-ed42a9273a20
* https://ip.cadence.com/uploads/901/cnn_wp-pdf
* https://mc.ai/resnet-for-traffic-sign-classification-with-pytorch/
**Traffic Sign Recognition with TensorFlow**
* https://medium.com/@waleedka/traffic-sign-recognition-with-tensorflow-629dffc391a6
* https://github.com/waleedka/traffic-signs-tensorflow

**Details**
* Detect and recognize iconic symbol and text strings contained in road panels
* Different types of traffic signs as Information signs, Warning signs, Mandatory signs and prohibited signs are used and these signs helps driver to achieve efficient navigation and safe driving.
* The major problem are changing lighting conditions in outdoor environments, the obstructions of objects between the cameras and the traffic panels [5], partially damaged traffic signs, long exposure of sunlights lead to faded color. 
* computer vision technique is carried out frequently The road sign can be categorized to three properties by color (blue, red, green and brown), shape (circular, square, triangular and octagonal) and the inner part of the sign [4], which plays a major role in the detection stage in traffic sign detection and recognisation.
* The speed and efficiency of the detection and recognisation of the traffic sign plays the important role in the system.

**techniques in detection and recognisation of Traffic Signs**
- overview of the system
- Detection stage used to extract the traffic sign based on the
  - hape and color features,
- Recognisaton stage to classify the traffic sign

**concludes**
* It is normally based on color or shape segmentation algorithms
  - The color segmentation is usually a binary mask to separate the interested target objects from the background.
  - The region of interest is determined by the connected components
  - The shape features are extracted in the binary image to detect the sign by verifying the hypothesis of the sign. The recognisation stage determines the type of traffic sign 

**Goal**
1. Classify traffic signs using a simple convolutional neural network.

**Tips**
- do Exploratory Data analysis. Knowing data well from the start saves a lot of time later.
- Pre-process and Handling Images of Different Sizes
- In early development use a smaller size because it leads to faster training, which allows to iterate faster
- Experiment with 16x16 and 20x20, but if they were too small that pick 32x32 which is easy to recognize and reduces the size of the model and training data by a factor of 16 compared to 128x128
- Get and print the min() and max() values. It’s a simple way to verify the range of the data and catch bugs early.
- Activation function: ReLU, sigmoid, tanh, fully connected layer, logits vector
- convert logits to probabilities using the softmax function if needed. If not needed, get the index of the largest value, which corresponds to the id of the label. The `argmax` op does that.
  - https://www.quora.com/What-are-the-benefits-of-using-rectified-linear-units-vs-the-typical-sigmoid-activation-function
  - http://cs231n.github.io/neural-networks-1/
- `cross-entropy` is the most common function for classification tasks.
- **Cross-entropy is a measure of difference between two vectors of probabilities**
  - https://jamesmccaffrey.wordpress.com/2013/11/05/why-you-should-use-cross-entropy-error-instead-of-classification-error-or-mean-squared-error-for-neural-network-classifier-training/
  - http://neuralnetworksanddeeplearning.com/chap3.html#the_cross-entropy_cost_function
- Convert labels and the logits to probability vectors. The function `sparse_softmax_cross_entropy_with_logits()` simplifies that
  - It takes the input as generated logits and the groundtruth labels
  - It does three things:
    * converts the label indexes of shape [None] to logits of shape [None, 62] (one-hot vectors)
    * then it runs softmax to convert both prediction logits and label logits to probabilities
    * and finally calculates the cross-entropy between the two
- This generates a loss vector of shape `[None]` (1D of length = batch size), which we pass through `reduce_mean()` to get one single number that represents the loss value.
```bash
loss = tf.reduce_mean(
        tf.nn.sparse_softmax_cross_entropy_with_logits(logits, labels_ph)
      )
```
- Choosing the optimization algorithm is another decision to make.
  - ADAM optimizer has shown to converge faster than simple gradient descent
  - http://sebastianruder.com/optimizing-gradient-descent/index.html
```bash
train = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)
```
- The last node in the graph is the initialization op, which simply sets the values of all variables to zeros (or to random values or whatever the variables are set to initialize to).
```bash
init = tf.initialize_all_variables()
```
- Notice that the code above doesn’t execute any of the ops yet. It’s just building the graph and describing its inputs. The variables we defined above, such as init, loss, predicted_labels don’t contain numerical values. They are references to ops that we’ll execute next.
- "Training Loop" is where we iteratively train the model to minimize the loss function. Before we start training, though, we need to create a **Session** object

**Pre-processing**
**Handling Images of Different Sizes**
- Most image classification networks expect images of a fixed size. So we need to resize all the images to the same size.
- our first model will do as well.
- If the images have different aspect ratios, then some of them will be stretched vertically or horizontally.
  - Is that a problem? May not be in some cases, because when the differences in aspect ratios are not that large and a person can recognize the images when they’re stretched then the model should be able to do so as well.

**Minimum Viable Model**
- start with the simplest possible model
- A one layer network that consists of one neuron per label.
- This network has `62` neurons and each neuron takes the RGB values of all pixels as input.
- Effectively, each neuron receives `32*32*3=3072` inputs. This is a fully-connected layer because every neuron connects to every input value
- Once this works end to end, expanding on it is much easier than building something complex from the start.

**Building the TensorFlow Graph**
- TensorFlow encapsulates the architecture of a neural network in an execution graph.
- The graph consists of operations (Ops for short) such as Add, Multiply, Reshape, …etc.
- These ops perform actions on data in tensors (multidimensional arrays).
- First, Graph object. TensorFlow has a default global graph, but I don’t recommend using it. Global variables are bad in general because they make it too easy to introduce bugs. Hence, create the graph explicitly.
```
graph = tf.Graph()
```
- define Placeholders for the images and labels. The placeholders are TensorFlow’s way of receiving input from the main program
- The shape of the images_ph placeholder is `[None, 32, 32, 3]`. It stands for [batch size, height, width, channels] (often shortened as NHWC) . The None for batch size means that the batch size is flexible, which means that we can feed different batch sizes to the model without having to change the code.
- Pay attention to the order of your inputs because some models and frameworks might use a different arrangement, such as NCHW.
- If layer expects input as a one-dimensional vector, flatten the images first.
```
# Flatten input from: [None, height, width, channels]
# To: [None, height * width * channels] == [None, 3072]
images_flat = tf.contrib.layers.flatten(images_ph)
```

**Loss Function and Gradient Descent**

### Potential Applications
- Intelligent Transportation Systems (ITS)
- Traffic Surveillance System
- ADAS

### Paper Reviews
1. TRAFFIC-SIGN RECOGNITION FOR AN INTELLIGENT VEHICLE/DRIVER ASSISTANT SYSTEM USING HOG 
- http://aircconline.com/cseij/V6N1/6116cseij02.pdf
- To recognize the traffic sign, the system has been proposed with three phases. They are Traffic board Detection, Feature extraction and Recognition. The detection phase consists of RGBbased colour thresholding and shape analysis, which offers robustness to differences in lighting situations. A Histogram of Oriented Gradients (HOG) technique was adopted to extract the features from the segmented output. Finally, traffic signs recognition is done by k-Nearest Neighbors (k-NN) classifiers. It achieves an classification accuracy upto 63%. 

2. AUTOMATED TRAFFIC SIGN BOARD CLASSIFICATION SYSTEM
- https://wireilla.com/papers/ijcsa/V5N1/5115ijcsa06.pdf
- Intelligent sign board classification method based on blob analysis in traffic surveillance
- A Sign board is modelled as a rectangular patch and classified via blob analysis. By processing the blob of sign boards, the meaningful features are extracted. Tracking moving targets is achieved by comparing the extracted features with training data. After classifying the sign boards the system will intimate to user in the form of alarms, sound waves. The experimental results show that the proposed system can provide real-time and useful information for traffic surveillance. 

3. SURVEY-AN EXPLORATION OF VARIOUS TECHNIQUES FOR SIGN DETECTION IN TRAFFIC PANELS
- http://www.arpnjournals.com/jeas/research_papers/rp_2015/jeas_0515_2045.pdf
- a survey of the traffic sign detection and recognition, to detail the system for driver assistance to ensure safe journey

4. Indian Traffic Sign Detection and Classification Using Neural Networks
- http://ijoes.vidyapublications.com/paper/Vol19/03-Vol19.pdf

5. ROAD AND TRAFFIC SIGN DETECTION AND RECOGNITION 
- http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.104.2523&rep=rep1&type=pdf

6. Real Time Detection and Recognition of Indian Traffic Signs using Matlab
- https://www.ijser.org/researchpaper/real-time-detection-and-recognition-of-indian-traffic-signs-using-matlab.pdf

## Face Detection
- https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/
- https://www.pyimagesearch.com/2018/07/09/face-clustering-with-python/

**Face recognition with OpenCV, Python, and deep learning**
* with deep learning you know that we typically train a network to:
  - Accept a single input image
  - And output a classification/label for that image
* deep metric learning
  - Instead, of trying to output a single label (or even the coordinates/bounding box of objects in an image), we are instead outputting a real-valued feature vector
* For the dlib facial recognition network, the output feature vector is 128-d (i.e., a list of 128 real-valued numbers) that is used to quantify the face. Training the network is done using triplets
*  Facial recognition via deep metric learning involves a “triplet training step.” The triplet consists of 3 unique face images — 2 of the 3 are the same person. The NN generates a 128-d vector for each of the 3 face images. For the 2 face images of the same person, we tweak the neural network weights to make the vector closer via distance metric.
* Here we provide three images to the network:
  - Two of these images are example faces of the same person.
  - The third image is a random face from our dataset and is not the same person as the other two images.
* Our network architecture for face recognition is based on **ResNet-34** from the **Deep Residual Learning for Image Recognition** paper by He et al., but with fewer layers and the number of filters reduced by half.
* The network itself was trained by Davis King on a dataset of ~3 million images. On the **Labeled Faces in the Wild (LFW)** dataset the network compares to other state-of-the-art methods, reaching 99.38% accuracy.
- Davis King (the creator of dlib)
- Adam Geitgey (the author of the face_recognition module we’ll be using shortly)
- [face_recognition](https://github.com/ageitgey/face_recognition)
- [dlib](http://dlib.net/)
```bash
sudo pip install dlib
# OR, compile from: git clone https://github.com/davisking/dlib.git # preferred for GPU, CUDA support
#
sudo pip install face_recognition
#pyimagesearch utility
sudo pip install imutils
```

## Semantic Segmentation
- https://github.com/tensorflow/models/tree/master/research/deeplab
- https://ai.googleblog.com/2018/03/semantic-image-segmentation-with.html

## Docker Containers for ML
- https://hub.docker.com/r/waleedka/modern-deep-learning/
- https://github.com/floydhub/dl-docker
- https://github.com/floydhub/dl-setup

## Mapillary
* https://github.com/lopuhin/mapillary-vistas-2017
* https://github.com/mapillary/mapillary_vistas
* https://arxiv.org/pdf/1803.05675.pdf
* http://cs231n.stanford.edu/reports/2017/pdfs/633.pdf

**Training on Mapillary dataset**
- https://oslandia.com/en/2018/05/07/deeposlandia-0-4-has-been-released/
- https://github.com/Oslandia/deeposlandia

## ML/DL libraries
* [dlib](http://dlib.net/) — a toolkit for real-world machine learning, computer vision, and data analysis in C++ (with Python bindings included, when appropriate).