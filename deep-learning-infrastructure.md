---
Title: Deep Learning Infrastructure
Decription: Deep Learning Infrastructure
Author: Bhaskar Mangal
Date: 23rd-Jan-2019
Last Updated: 23rd-Jan-2019
Tags: Deep Learning Infrastructure

---

**Table of Contents**
* TOC
{:toc}


[TOC]


# Deep Learning Infrastructure

## 1. Requirements

### Technology assesment
* **Some of the Programming Langauges for AI:**
  - Lisp, Python, Julia, scala, Haskell
* **C/C++**
  - required for production/deleviry of the AI to mobile apps, embedded systems and to some extent to web apps
  - lean, high performanant, low memory footprint, highly optimised
* **JS, nodejs**
  - avaiable as browser based
  - experimental
  - quick adaption and setup
  - potential candidate for future
* **Matlab**
  - Researchers heaven
  - high usage in university in initial phases
  - algorithim development
  - quick results for skilled resources
  - matlab now provides production quality solutions
* **R**
  - Researchers heaven
  - potential toolkit for data scientist
  - statistical toolbox
* **cython**
  - c-extension of python
  - combines the ease of Python and the speed of native code
  - potential usage for production of python models to mobile and emedded systems
* **Python - shortlisted**
  - ease of use, popularity, good community support
  - software engineer's swiss army toolbox
  - out-of-the-box support for almost every other AI tools & frameworks
  - provides all the required frameworks, toolkits for computer vision, datascience and deep learning with ease and under the same technology umberella
  - migration to python 3 is mandatory
    + 10+ years in existance (December 3, 2008 first release)
    + Official notice: Jan 2020 end of python 2 developement support


### **Hardware & Software requirements**
+ [Deep Learning Hardware](https://github.com/mangalbhaskar/technotes/blob/master/deep-learning-hardware.md)
+ [Deep Learning Frameworks, Toolkits and Libraries](https://github.com/mangalbhaskar/technotes/blob/master/deep-learning-frameworks.md)


+ **Recommended hardware configuration:**
	+ minimum 8 GB Nvidia GPU, 16 GB RAM, 2 TB HDD
+ **Programming langauge:**
	+ Python
+ **Frameworks:**
	+ Theano, Caffe, TensorFlow, Keras
+ **Low level Tech stack for GPU**
  + CUDA (kind of mandatory)
  + cuDNN
  + TensorRT -  deep learning inference runtime for production deployment
  + [Nvidia Stack](https://developer.nvidia.com/deep-learning-software):
    + CUDA, cuDNN
    + NCCL cuBLAS, cuSPARSE, TensorRT
    + DeepStream SDK, Optical Flow SDK, Transfer Learning Toolkit
    + Nvidia-docker
+ **Dependencies**
  + CUDA, cuDNN, BLAS, Boost, protobuf, glog, gflags, hdf5 etc.
  + opencv
  + python secific packages
+ **AI-ML-DL Technology Stack**
  - focus to provide optimized ML and deep learning algorithims and stand tools and processes
  - Deep Learning Frameworks
    * opensource, proprierty
    * Python/C++
      * Theano, PyTorch
      * Caffe, TensorFlow, TFLearn, Keras
      * Caffe2, ck-caffe, Chainer, paddlepaddle, MXNet, MatConvNet
      * Digits (RAD tool for DL)
      * dlib (library)
    * Java: Deeplearning4j
  - **Toolkits & Libraries**
    * Computer Vision, Image processing
    * Datascience (statistics, visualization - 2D/3D)
    * Machine Learning
    * Web Server Interface
  - **DevOps Tools**
    * Release & package management
    * docker


## 2. Problem Statement
  - Identification, Articulation and Selection
  - focus on 2D Images (RGB)
  - Image processing and Computer Vision applications
  - defining MoV (Measured Organisational Value)


## 3. Lesson learned from the Past Experiences
  - Challanges in adption
    - no standard rules and conventions
    - hard coding
    - selection of annotation tool
  - Secluded nature of work
  - Stakeholder management
  - Work visibility & understanding the nature of work
  - Setting the right expectations
  - Providing MoVs (Measured Organisational Values)
  - Continious experiments
  - Lack of knowledge sharing, lack of organized approach for information management
  - higher degree of redundancy in effort when different people work on similar problems
  - Lack of proper knowledge Transfer at the end of effort by the dedicated resource
  - Shortage of skilled resources and high cost


## 4. Different Approaches for starting in AI (Deep Learning in Computer vision)
  * **hard-core AI work**
    - 1. create architecture
    - 2. implement from scratch from paper -(no transfer learned model used but implement in house)
  * **application and practical usage**
    - 3. pre-trained models, transfer learning ---->
    - 4. our own dataset with training (on #3)
    - 5. usage, tooling, CBR


## 5. Current Setup
  - based on lessons learned, effort to lower and mitigate risks, hence a proposal on sustainable AI programme

![ALT ](images/ai-ml-dl/ai-infra-setup.png)

## 6. Conclusion & Future Proposal


## 7. References
  * [The Lisp approach to AI (Part 1)](https://medium.com/ai-society/the-lisp-approach-to-ai-part-1-a48c7385a913)
  * [The languages of Artificial Intelligence](https://developer.ibm.com/articles/cc-languages-artificial-intelligence/)
  * [Deep Learning Hardware](https://github.com/mangalbhaskar/technotes/blob/master/deep-learning-hardware.md)
  * [Deep Learning Frameworks, Toolkits and Libraries](https://github.com/mangalbhaskar/technotes/blob/master/deep-learning-frameworks.md)
  * [History_of_Python](https://en.wikipedia.org/wiki/History_of_Python)
  * [cuDNN](https://developer.nvidia.com/cudnn)


## Extras

### Nvidia Deep Learning Stack
* **Deep Learning Primitives (cuDNN)**: High-performance building blocks for deep neural network applications including convolutions, activation functions, and tensor transformations
* **Multi-GPU Communication (NCCL)**: Collective communication routines, such as all-gather, reduce, and broadcast that accelerate multi-GPU deep learning training
* **Deep Learning Inference Engine (TensorRT)**: High-performance deep learning inference runtime for production deployment
* **Deep Learning for Video Analytics (DeepStream SDK)**: High-level C++ API and runtime for GPU-accelerated transcoding and deep learning inference
* **Optical Flow for Video Inference (Optical Flow SDK)**: Set of high-level APIs that expose the latest hardware capability of Turing GPUs dedicated for computing the optical flow of pixels between images. Also useful for calculating stereo disparity and depth estimation.
* **High level SDK for tuning domain specific DNNs (Transfer Learning Toolkit)**: Enabling end to end Deep Learning workflows for industries
* **AI enabled Annotation for Medical Imaging (AI-Assisted Annotation SDK)**: AI-assisted annotation for medical imaging related data labeling
* **Deep Learning GPU Training System (DIGITS)**: Rapidly train highly accurate deep neural network (DNNs) for image classification, segmentation and object detection tasks
* **Linear Algebra (cuBLAS)**: GPU-accelerated BLAS functionality that delivers 6x to 17x faster performance than CPU-only BLAS libraries
* **Sparse Matrix Operations (cuSPARSE)**: GPU-accelerated linear algebra subroutines for sparse matrices that deliver up to 8x faster performance than CPU BLAS (MKL), ideal for applications such as natural language processing

