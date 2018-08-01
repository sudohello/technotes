/*
Title: Machine Learning, Deep Neural Network & Computer Vision
Decription: Machine Learning, Deep Neural Network & Computer Vision
Author: Bhaskar Mangal
Date: Jul-2017
Last Updated: Jul-2017
Tags: Machine Learning, Deep Neural Network & Computer Vision
*/

## Machine Learning, Deep Neural Network & Computer Vision
>**Follow BDC-Team here:-**
> Blog, forum, k-bank, scripts
>[![Alt Blog, forum, k-bank](logos/blogger-logo-2.png "Blog, Forum, knowledge-bank"  "width:65px;margin-right:20px")](http://hdmapforselfdrivingcar.blogspot.in/) [![Alt Scripts](logos/git-hub-2.png "Scripts"  "width:23px;")](https://github.com/mangalbhaskar/linuxscripts)

**by [Bhaskar Mangal](http://www.bhaskarmangal.com/)**
Jul 2017
* [GIS Accuracy Standards - **27^th^-Jul 2017 @ Scholar's Den Group** ](gis-accuracy-standards.md)
* [Click here to view ++Main Presentation - **Jul 2017** ppt++](ppts-pdfs/ml-app-in-adv-map-creation.pdf)
* [Click here to view ++Main Presentation - **May 2017** Nvidia Driveworks and DNN](ppts-pdfs/nvidia-driveworks-dnn.pdf)
* [Click here to view - **May 2017** Nvidia Driveworks](nvidia-driveworks.md)


[TOC]

## 1) Achievements
- Learnings on:
	- basics of machine learning
	- basics math, python, statistics
	- deep neural networks, convolution neural networks
		- architectures, frameworks
		- pre-trained models, training, transfer learning, hyper-parameter tuning
	- machine setups, hardware requirements
	- productionization pipeline for ML and CNN
- Hands on with basic computer vision use-cases using **machine learning techniques**
	- edge detections
	- object detections
	- hand written digit classification
	- pedestrian detection
	- cat-dog classification
	- blur detection
- Hands on converging machines on some of the **pre-defined CNN architectures**
	- hand written digit classification
	- cat-dog classification
	- urban scene pixel level segmentation and classification

## 2) Results
[Click Here to see some of the results](ml-app-in-adv-map-creation-results.md)

## 3) ML, Deep Learning Project Readiness
* **Basic understanding and Hands-on on the following areas:-**
	* Machine Learning
		- Supervised and Unsupervised Learning methodologies, algo
	* Traditional Computer vision
	* DNN/CNN concepts – back-propogation, architectures etc, frameworks
		- Frameworks used: Caffe, tensorFlow, Keras
		- converged machines (SegNet, VGG16, LeNet architectures)
	* Data analysis and Data visualization using python and R
	* Techstack:
		- python, openCV3, scipy, numpy, sklearn, matplot, pandas, R
* **Experienced in:**
	- REST API specification, design and implementation in PHP, Javascript
	- Database handling PostgresSQL, PostGIS
	- End-to-End WebApplication design and development in PHP, JS - UI, UX
* **Technology Stack**
	- python with python bindings of openCV
	- python with python based image/data processing packages: sklearn, pandas, matplot
	- python with NN frameworks: keras, Caffe, Tensorflow
	- Ubuntu LTS 14.04, 16.04

* **Studied the Driveworks CNN workflow**
	- Looked and went through the Driveworks CNN workflow pipeline
	- TensorRT (Nvidia) framework on top of Tensorflow/Caffe

* **Productionization Pipeline**
	- Studied different available work-flows
	- No standardized architectures
	- Depends of Business Goal and Problem statement
	- **How the deployment is done in self-driving cars, robots or drones?**
	> by Marek Bardoński, Senior Deep Learning Research Engineer at NVIDIA
I’ll describe it on a Tesla’s car example - other objects have a similar process.

	After the company have a model designed and trained in one of the popular deep learning frameworks, it’s exported to the NVIDIA’s inference tool - TensorRT - and compiled as a library for inference. Then, the computer in the car equipped with one or more GPUs (eg. DrivePX2) have a control program calling this library each time the inference is required.
	It’s reading input from the camera, and calling TensorRT via API to provide inference - recognizing what’s on the image or outputting the image segments. Everything is done as C++ API calls and often it’s on a real-time operating system like QNX.
[Click here for reference](https://www.quora.com/What-is-the-easiest-way-to-deploy-a-machine-learning-model-say-a-regression-for-production)

## 4) Uses Cases for VidTeq/MMI

**Text from the photographs**
- POI - auto-fill
- Number Plate Masking - Automatic License Plate Recognition system (ALPR)
- Face obfuscation
- OCR (Optical Character Recognition)

**Image Categorization/Classification**
>Needle in Haystack problems

- Poi
- Traffic Sign Detection and Extraction

**Structure Segmentation and Re-construction**
- Road Edges
- Lanes

**CBIR (Content Based Image Retrival)**
- Image search based on different query filters

## 5) Details on Neural Networks (NN), Deep Neural Network (DNN), Convolution Neural Netowork (CNN)
* **Architecture** - number of layers, stacking of different layers, layer parameters etc.
	* Architectures are problem specific
	* Existing architures
	* custom - problem specific
* **Training/Learning**
	* Pre-trained Models with following Architecture
		- LeNet, VGG16
		- SegNet (Specialized CNN architecture for Road/Urban scene pixel segmentation)
	* **Converged Machines**
		* a) with CNN for 6 Days of training for 26K iterations on camvid dataset of 367 images
			* identified road segmentation CNN archs - SegNet, Dialation, Enet
			* trained SegNet (using caffe framework) for 26K iterations on camvid samples with accuracy of around 66% (followed the tutorial)
			* ran it against gaze samples of 4th-Apr'17
			* the research paper used a larger dataset  with accuracy of 88% - need to reach this was practical usage of this model
			* 66% accuracy is not good enough for segmentation purpose
			* Reached computation bottleneck - Need workstation with at least 12GB pascal based graphics card
		* b) converged for MNIST data (Hand written digitis dataset)
			* with accuracy of ~99.28% using CNN compared to last weeks ~96%
			* Code and model was available for Keras CNN framework
		* In the original SegNet paper they have trained on multiple datasets with over 3500+ images
* **Transfer Learning**
	- studied, not attempted
* **Hyperparameter Tuning**
	- studied, not attempted
	- specific to dataset, problem at hand
* **Problems Attempted**
	* Hand digit recognition
	* Cat-dog classification
	* Urban scene classification and segmentation - using SegNet

* **Architectures studied**
	* LeNet
	* VGG16
	* Segnet
	* Dialtion

* **Datasets sources**
	* camvid, imagenet, kaggle, cifar, mnist etc.

* **Technology**
	* without NN frameworks, write custom code for optimization, back-propogation algorithm
		* using C/C++, Python
	* frameworks (good support for Python bindings)
		* Caffe
		* Tensorflow
		* Keras

## 6) Proposed approach
* Identify 1 or 2 uses cases and solve using ML, computer vision techniques
* provide the production pipeline based on the requirements
* POC
* Deploy Internally
* Stabilize workflow, improve accuracy, tuning
* Provide Deep Learning pipeline
* Deploy parallel to ML pipeline

## 7) Productionization of Machine Learning Models

![Alt ml](images/ai-ml-dl/ml-production.webp)
>Distinguishing on these two dimensions, we can classify the productionalization of machine learning models using a 2-by-2 matrix.
>
>**Source:** [Do-most-machine-learning-algorithms-run-in-batch-or-do-they-run-every-time-they-get-a-new-bit-of-data](https://www.quora.com/Do-most-machine-learning-algorithms-run-in-batch-or-do-they-run-every-time-they-get-a-new-bit-of-data/answer/H%C3%A5kon-Hapnes-Strand)

### How the Learning/Training Happens?
**First of all, we need to distinguish on the type of learning. There are two ways of training machine learning models:**
* **Offline learning**: The model is trained once on historical data. After the model is deployed to production, it remains constant, although it’s possible to re-train the model if it becomes unstable, which will often happen.
* **Online learning**: The model is constantly being updated as new data arrives. This is especially useful for time series data, such as sensor data or financial instruments, because an online learning algorithm can pick up temporal effects. It’s also useful for websites with huge amounts of data, such as Google or Quora.

### How the algorithim make predictions?
**Secondly, we need to distinguish on how the algorithm makes predictions:**
* **Batch predictions**: The algorithm generates a table of predictions based on its input data. This is often good enough for data that is not time-dependent, or when the output isn’t required to be totally fresh all the time.
* **On-demand predictions**: Predictions are being made in real-time using the input data that is available at the time of the request, which typically comes in the form of a REST call.

### What are the type of use cases based on Training and Prediction methodologies?
4 Different Modes of deployment:

1. **Offline Batch Predictions - Forecast**
	* You get your input data as a file, train a model, and make a forecast
	* more like an experiment than actually putting something into production, although this paradigm is also common in business intelligence
2. **Offline On-demand Predictions - Web service**
	* more common way to embed machine learning into applications
	* the model is trained on historical data offline
	* but it uses fresh data to make predictions
	* The service always uses the latest data available to make predictions, but the model remains constant.
3. **Online Batch Predictions - Automated machine learning**
	* very hot topic these days
	* includes automating the entire training, cross-validation and model selection process
	* An algorithm that retrains itself and makes repeated batch predictions in intervals
	* Uses the latest data available to both train the model and generate predictions
	* This methodology can’t be used in real-time, though, because it takes time to train the model(s)
	* least utilized method out of the four
4. **Online On-demand Predictions - Online Learning**
	* most dynamic way to productionalize machine learning
	* The learning algorithm is hooked to a (big) data stream and continuously trains itself as new data comes in.
	* A constantly updated model is immediately accessible as a web service
	* Technically, this is the most challenging setup to achieveit has mostly been used by the big players so far

### Best Practices for ML Model deployment in Production

**Storage**
- Separate the models, that is, the hyperparameters and feature weights, from the rest of the workflow.
- There are model management frameworks based on both SQL databases and REST APIs.
- There are also things like the Openscoring library[2] , which uses a standard markup language known as PMML to store models.
- **If your ground truth is inaccurate, you’ve already set an upper limit to how good your precision and recall can be. If your ground truth is grossly inaccurate, that upper limit is pretty low.**
- So the best advice we can offer in this case is to log everything. Throw it all in HDFS, whether you need it now or not. In the future, you can always use this data to backfill new data stores if you find it useful. This can be invaluable in responding to a new attack vector.
- **HDFS** - The Hadoop Distributed File System ( HDFS ) is a distributed file system designed to run on commodity hardware.
- version your trained models
- in-house experiments framework that we use to deploy new models and test them against subsets of user traffic to see how they are doing as we ramp up a new model.

At the end of the day, **there is NO generic deployment scheme that fits every problem and every company**. Deciding what practices to use, and implementing them, is at the heart of what machine learning engineering is all about.
- At a high level
	– depending on what volume of incoming data you need to process
	- on the size of the model
	- on how often it's updated
	- on what stack/tools you're using, etc
- you've got two choices:
	- (a) use the same tools you used to build the model to run it
	- or (b) run it using different tools than you used to build it.

**References**
* [How-do-you-take-a-machine-learning-model-to-production](https://www.quora.com/How-do-you-take-a-machine-learning-model-to-production)
* [Do-most-machine-learning-algorithms-run-in-batch-or-do-they-run-every-time-they-get-a-new-bit-of-data](https://www.quora.com/Do-most-machine-learning-algorithms-run-in-batch-or-do-they-run-every-time-they-get-a-new-bit-of-data/answer/H%C3%A5kon-Hapnes-Strand)