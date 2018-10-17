---
Title: Deep Learning Architectures
Decription: Deep Learning Architectures
Author: Bhaskar Mangal
Date: 25th-Aug-2018
Last updated: 25th-Aug-2018
Tags: Deep Learning Architectures

---


**Table of Contents**
* TOC
{:toc}


## Deep Learning Model Architectures
* **VGG**
  - https://arxiv.org/abs/1409.1556
  - VGG is a convolutional neural network model proposed by K. Simonyan and A. Zisserman from the University of Oxford in the paper “Very Deep Convolutional Networks for Large-Scale Image Recognition” 
  - VGG16 (also called OxfordNet) is a convolutional neural network architecture named after the Visual Geometry Group from Oxford, who developed it. It was used to win the ILSVR (ImageNet) competition in 2014
  - https://www.cs.toronto.edu/~frossard/post/vgg16/
  - https://disq.us/url?url=https%3A%2F%2Farxiv.org%2Fpdf%2F1409.1556.pdf%3Aoht-Wy0GgkCV6vMv1CR-PdCLMYg&cuid=4253828
  - https://gist.github.com/ksimonyan/211839e770f7b538e2d8#file-readme-md
* **AlexNet**
  - https://kratzert.github.io/2017/02/24/finetuning-alexnet-with-tensorflow.html
  - http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf
* **LeNet**
  - one of the canonical network architectures for image classification
  -  how to implement LeNet in TensorFlow, highlighting data preparation, training and testing, and configuring convolutional, pooling, and fully-connected layers.
* **SqueezeNet**
  - https://arxiv.org/abs/1602.07360
  - https://github.com/DeepScale/SqueezeNet
  - a small CNN architecture called “SqueezeNet” that achieves AlexNet-level accuracy on ImageNet with 50x fewer parameters
  - https://gab41.lab41.org/lab41-reading-group-squeezenet-9b9d1d754c75
  - making a network smaller by starting with a smarter design versus using a clever compression scheme
  - Strategy 1. Make the network smaller by replacing 3x3 filters with 1x1 filters
    - https://iamaaditya.github.io/2016/03/one-by-one-convolution/
  - Strategy 2. Reduce the number of inputs for the remaining 3x3 filters
    - “squeeze” layers are convolution layers that are made up of only 1x1 filters
    -  “expand” layers are convolution layers with a mix of 1x1 and 3x3 filters.
    - By reducing the number of filters in the “squeeze” layer feeding into the “expand” layer, they are reducing the number of connections entering these 3x3 filters thus reducing the total number of parameters
    -  paper call this specific architecture the “fire module” and it serves as the basic building block for the SqueezeNet architecture.
  - Strategy 3. Downsample late in the network so that convolution layers have large activation maps.
    - The authors believe that by decreasing the stride with later convolution layers and thus creating a larger activation/feature map later in the network, classification accuracy actually increases
    - Having larger activation maps near the end of the network is in stark contrast to networks like VGG where activation maps get smaller as you get closer to the end of a network.
    - https://arxiv.org/abs/1412.1710
    - a delayed down sampling that leads to higher classification accuracy.
    - One of the surprising things I found with this architecture is the lack of fully-connected layers. What’s crazy about this is that typically in a network like VGG, the later fully connected layers learn the relationships between the earlier higher level features of a CNN and the classes the network is trying to identify. That is, the fully connected layers are the ones that learn that noses and ears make up a face, and wheels and lights indicate cars. However, in this architecture that extra learning step seems to be embedded within the transformations between various “fire modules”.
* **SqueezeNext: Hardware-Aware Neural Network Design**
  - https://arxiv.org/abs/1803.10615
* **NiN - Network In Network**
  - https://arxiv.org/abs/1312.4400
* **ResNet**
  - ResNet-18,ResNet-34
  - https://arxiv.org/abs/1512.03385
  - https://mc.ai/resnet-for-traffic-sign-classification-with-pytorch/
* **Mask R-CNN**
  - https://arxiv.org/abs/1703.06870
* **SSD - Single Shot MultiBox Detector**
  - https://arxiv.org/abs/1512.02325
  - https://github.com/weiliu89/caffe/tree/ssd
* **Detectron**
  - https://github.com/facebookresearch/Detectron
* **NASNet**
  * Automl-for-large-scale-image
  * https://ai.googleblog.com/2017/11/automl-for-large-scale-image.html


## Comparision of Model Architectures
* **SSD v/s Faster R-CNN**
  - Even the fastest high-accuracy detector, Faster R-CNN, operates at only 7 frames per second (FPS)

## Deep Learning Models
 * Convolutions
 * RNN
 * LSTM
 * BiRNN
 * BatchNorm
 * PReLU
 * Residual networks
 * Generative networks