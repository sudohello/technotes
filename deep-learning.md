/*
Title: Deep Learning
Decription: Deep Learning
Author: Bhaskar Mangal
Date: 
Tags: Deep Learning
*/

1. https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/
2. http://cv-tricks.com/tensorflow-tutorial/training-convolutional-neural-network-for-image-classification/
3. http://scs.ryerson.ca/~aharley/vis/conv/flat.html
4. http://scs.ryerson.ca/~aharley/neural-networks/
* some primer for matlab helpful to go through the NN code in the above link
	http://mathesaurus.sourceforge.net/matlab-numpy.html
	http://www.cert.org/flocon/2011/matlab-python-xref.pdf
	https://www.tutorialspoint.com/matlab/matlab_arrays.htm
	https://stackoverflow.com/questions/8625990/size-function-in-matlab
As you know, matlab deals mainly with matrices. So, the size function gives you the dimension of a matrix depending on how you use it. For example:
1. If you say size(A), it will give you a vector of size 2 of which the first entry is the number of rows in A and the second entry is the number of columns in A.
2. If you call size(A, 1), size will return a scalar equal to the number of rows in A.
3. If you call size(A, 2), size will return a scalar equal to the number of columns in A.

A scalar like scale in your example is considered as a vector of size 1 by 1. So, size(scale, 2) will return 1, I believe.

Hope this clarifies.

---
* **How many nodes to have in the hidden layer?**
	* The size of the input layer is fixed by the input space (e.g. one node per input pixel), and the size of the output layer is fixed by the output space (e.g. one node per category, in a classification task), but the inner hidden layer has no limitations on size. If the hidden layer is too small, it won't be able to separate out important "patterns" in the high-dimension space it works in. If the layer is too large, the relative contribution of each node will be small, and it will probably take longer to train. The ideal number of nodes depends on the problem the network is tasked with.
* **How to initialize the weights?**
	* Is it better to initialize all of the weights to 1, or initialize them randomly? Most sources seem to agree it's better to initialize the weights randomly, because this seems to decrease the probability that the optimization algorithm will get stuck in a bad local minimum. There are also recommendations to initialize the weights to small numbers (i.e. close to 1), so that no weight overpowers the others from the outset.
* **Stopping criteria?**
	* When do we stop training? Do we attempt to reach a certain error rate in the classification of the input set? Or do we iterate a specified number of times? It's probably best to give the algorithm a combination of different stopping criteria.
* **Learning rate?**
	* Many sources recommend damping the dqdq (for any node qq in the network) with a learning rate, which is usually somewhere around 0.3. This helps make sure that the gradient descent does not jump past a local minimum and miss it entirely.
* **How to feed in training data?**
	* Given a large set of input data, it may be tempting to train the network on a small portion of it until it excels there, and then gradually increase the data set size. This will not work: getting the network to excel on a small portion of the data will over-fit the network to that data. To learn new information afterward, the network will essentially have to forget what it learned before. A better way to train the network is to sample randomly (or in some uniform manner) from the overall dataset, so that the node never over-fits to its input.


# Technical Questions

* How can I train a CNN with insufficient and not-so-good data?
* How do I classify images with non-rectangle shape with CNN?
* Why should we give an images with a fixed size for traditional CNN, whereas for FCN we can give an image with an arbitrary image size?
* Why do l need to apply PCA whitening to my images (black and white) before training my convolutional neural network (CNN)?
* What are the different types of input vectors used for an image in a neural network?
* How does the conversion of last layers of CNN from fully connected to fully convolutional allow it to process images of different size?
* How do I read image data for CNN in python?
	- https://www.quora.com/How-do-I-read-image-data-for-CNN-in-python
	- http://pillow.readthedocs.io/en/3.0.x/handbook/tutorial.html#using-the-image-class


* What-is-the-main-difference-between-a-Bayessian-neural-network-and-other-convolutional-neural-networks
	- A Bayesian network is a graphical model that works by modeling dependencies between nodes, by considering the conditional dependence (where zero implies independence). On the other hand Bayesian Convolutional Neural Networks are an adaptation of CNNs that helps to prevent overfitting and are therefore preferred in problems where CNNs are the appropriate DL model but there is insufficient data (and standard CNNs would therefore overfit on this small set of data as they very rapidly overfit). This is done by the introduction of uncertainity estimation in Bayesian Convolutional Neural Networks. There is an excellent paper explaining applications of Bayesian Convolutional Neural Nets by Gal and Ghahramani (2016).
	- CNN is a NN with convolutional and pooling layers which can randomly initialize (or uniform or xavier) its weights and biases whereas Bayesian NN takes prior distribution on its weights and biases.
	* https://www.quora.com/What-is-the-main-difference-between-a-Bayessian-neural-network-and-other-convolutional-neural-networks

https://en.wikipedia.org/wiki/Convolutional_neural_network

http://cv-tricks.com/tensorflow-tutorial/training-convolutional-neural-network-for-image-classification/

When designing the architecture of a neural network you have to decide on:
- How do you arrange layers?
- Which layers to use?
- How many neurons to use in each layer etc.?

Once you have decided the architecture of the network;
- the second biggest variable is the weights(w) and biases(b) or the parameters of the network.

The objective of the training is to get the best possible values of the all these parameters which solve the problem reliably. For example, when we are trying to build the classifier between dog and cat, we are looking to find parameters such that output layer gives out probability of dog as 1(or at least higher than cat) for all images of dogs and probability of cat as 1((or at least higher than dog) for all images of cats.

You can find the best set of parameters using a process called Backward propagation, i.e. you start with a random set of parameters and keep changing these weights such that for every training image we get the correct output. There are many optimizer methods to change the weights that are mathematically quick in finding the correct weights. GradientDescent is one such method(Backward propagation and optimizer methods to change the gradient is a very complicated topic. But we don’t need to worry about it now as Tensorflow takes care of it).

	



---
* There are many standard architectures which work great for many standard problems. Examples being AlexNet, GoogleNet, InceptionResnet, VGG etc. In the beginning, you should only use the standard network architectures. You could start designing networks after you get a lot of experience with neural nets. Hence, let’s not worry about it now.


# Intro
machine learning and the role it plays in computer vision, image classification, and deep learning.

http://neuralnetworksanddeeplearning.com/index.html

http://neuralnetworksanddeeplearning.com/chap1.html
once we've learned a good set of weights and biases for a network, it can easily be ported to run in Javascript in a web browser, or as a native app on a mobile device. 

I had to make specific choices for the number of epochs of training, the mini-batch size, and the learning rate, ηη. As I mentioned above, these are known as hyper-parameters for our neural network, in order to distinguish them from the parameters (weights and biases) learnt by our learning algorithm.


But if we were coming to this problem for the first time then there wouldn't be much in the output to guide us on what to do. We might worry not only about the learning rate, but about every other aspect of our neural network. We might wonder if we've initialized the weights and biases in a way that makes it hard for the network to learn? Or maybe we don't have enough training data to get meaningful learning? Perhaps we haven't run for enough epochs? Or maybe it's impossible for a neural network with this architecture to learn to recognize handwritten digits? Maybe the learning rate is too low? Or, maybe, the learning rate is too high? When you're coming to a problem for the first time, you're not always sure.

we need to develop heuristics for choosing good hyper-parameters and a good architecture.

support vector machine or SVM

http://peekaboo-vision.blogspot.in/2010/09/mnist-for-ever.html

http://neuralnetworksanddeeplearning.com/chap2.html
  algorithm for computing such gradients, an algorithm known as backpropagation.
  how quickly the cost changes when we change the weights and biases.

# Deep Learning

* Neural netowrk
* feed-forward network
* recursive neural network
* gradient descent
* sigmoid function
* sigmoidal neuron
* learning rate
* delta rule
* stochastic gradient descent
* logit
* backpropogation
* overfiting
* validation
* cross-validation
* Bias trick
* center your data
* high-dimensional column vectors/points
	* https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/vectors/v/real-coordinate-spaces
* score function
* loss function (cost function or the objective)
	* The loss function quantifies our unhappiness with predictions on the training set
* SVM - Support Vector Machine
* Multiclass Support Vector Machine
	* The Multiclass Support Vector Machine "wants" the score of the correct class to be higher than all other scores by at least a margin of delta
	* regularization function is not a function of the data, it is only based on the weights. Including the regularization penalty completes the full Multiclass Support Vector Machine loss, which is made up of two components: the data loss (which is the average loss LiLi over all examples) and the regularization loss.
* hinge loss
* squared hinge loss SVM (or L2-SVM), which uses the form max(0,−)^2^
* Regularization
* Regularization penalty R(W)
* CNN
	- Convolutional Neural Networks are a powerful artificial neural network technique. They expect and preserve the spatial relationship between pixels in images by learning internal feature representations using small squares of input data. Feature are learned and used across the whole image, allowing for the objects in your images to be shifted or translated in the scene and still detectable by the network. There are ++three types of layers++ in a Convolutional Neural Network:
		- **Convolutional Layers** comprised of filters and feature maps.
		- **Pooling Layers** that down sample the activations from feature maps.
		- **Fully-Connected Layers** that plug on the end of the model and can be used to make predictions.
* Principal Component Analysis
	- It’s a method to reduce the dimensionality of a dataset. There are others, like Fisher transform
	-  It’s simpler and easier to understand or even visualize.


## CCN terms
* Objective of Training
* Model
* Inference or prediction
* batch-size
* itration
* epoch
* ground-truth
* learning rate
* backward propogation
* Layers - convolution, Pooling (MaxPooling), fully-connected layer, flattening layer
* strides
* activation map
* kernet
* sigmoid neuron, RELU, TanH
* filter
* padding
* parameters
* placeholders, inputs
* optimization
* validation
* network design
* non-linear function activation functions
	* Sigmoid function
	>$ \sigma(x) = \frac{1}{1 + e^{-x}} $

https://github.com/ml4a/ml4a.github.io/blob/master/_chapters/neural_networks.md

## Tutorials

### Tensorflow
* http://cv-tricks.com/artificial-intelligence/deep-learning/deep-learning-frameworks/tensorflow-tutorial/

http://rodrigob.github.io/are_we_there_yet/build/classification_datasets_results.html
https://stackoverflow.com/questions/26575587/cant-install-scipy-through-pip
https://github.com/duguyue100/cs231n-practice/blob/master/cs231nlib/utils.py
https://github.com/cs231n/cs231n.github.io
http://vision.stanford.edu/teaching/cs231n/
http://karpathy.github.io/2015/03/30/breaking-convnets/
http://ccsubs.com/video/yt:GUtlrDbHhJM/cs231n-winter-2016-lecture-5-neural-networks-part-2-jhuz800c650-mp4/subtitles?lang=en
https://devhub.io/repos/xiaohu2015-cs231n-assignment
http://planetmath.org/vectorpnorm
http://cs231n.github.io/convolutional-networks/

Split your training set into training set and a validation set. Use validation set to tune all hyperparameters. At the end run a single time on the test set and report performance.

Cross-validation. In cases where the size of your training data (and therefore also the validation data) might be small, people sometimes use a more sophisticated technique for hyperparameter tuning called cross-validation. Working with our previous example, the idea is that instead of arbitrarily picking the first 1000 datapoints to be the validation set and rest training set, you can get a better and less noisy estimate of how well a certain value of k works by iterating over different validation sets and averaging the performance across these. For example, in 5-fold cross-validation, we would split the training data into 5 equal folds, use 4 of them for training, and 1 for validation. We would then iterate over which fold is the validation fold, evaluate the performance, and finally average the performance across the different folds.


In practice. In practice, people prefer to avoid cross-validation in favor of having a single validation split, since cross-validation can be computationally expensive. The splits people tend to use is between 50%-90% of the training data for training and rest for validation.

It is worth considering some advantages and drawbacks of the Nearest Neighbor classifier. Clearly, one advantage is that it is very simple to implement and understand. Additionally, the classifier takes no time to train, since all that is required is to store and possibly index the training data. However, we pay that computational cost at test time, since classifying a test example requires a comparison to every single training example. This is backwards, since in practice we often care about the test time efficiency much more than the efficiency at training time. In fact, the deep neural networks we will develop later in this class shift this tradeoff to the other extreme: They are very expensive to train, but once the training is finished it is very cheap to classify a new test example. This mode of operation is much more desirable in practice.

http://lvdmaaten.github.io/tsne/
t-Distributed Stochastic Neighbor Embedding (t-SNE)

http://www.cs.ubc.ca/research/flann/
What is FLANN?
FLANN is a library for performing fast approximate nearest neighbor searches in high dimensional spaces. It contains a collection of algorithms we found to work best for nearest neighbor search and a system for automatically choosing the best algorithm and optimum parameters depending on the dataset.
FLANN is written in C++ and contains bindings for the following languages: C, MATLAB and Python.





http://cs231n.github.io/classification/
http://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf
http://people.csail.mit.edu/torralba/shortCourseRLOC/index.html

# Deep Learning Toolchain

## Theano
Theano is a Python library for fast numerical computation to aid in the development of deep learning models. At it’s heart Theano is a compiler for mathematical expressions in Python. It knows how to take your structures and turn them into very efficient code that uses NumPy and efficient native libraries to run as fast as possible on CPUs or GPUs.

## TensorFlow
TensorFlow is a Python library for fast numerical computing created and released by Google. Like Theano, TensorFlow is intended to be used to develop deep learning models. With the backing of Google, perhaps used in some of it’s production systems and used by the Google DeepMind research group, it is a platform that we cannot ignore. Unlike Theano, TensorFlow does have more of a production focus with a capability to run on CPUs, GPUs and even very large clusters.

## Keras
A difficulty of both Theano and TensorFlow is that it can take a lot of code to create even very simple neural network models. These libraries were designed primarily as a platform for research and development more than for the practical concerns of applied deep learning. The Keras library addresses these concerns by providing a wrapper for both Theano and TensorFlow. It provides a clean and simple API that allows you to define and evaluate deep learning models in just a few lines of code.

## scikit-learn
The scikit-learn library is a general purpose machine learning framework in Python built on top of SciPy. Scikit-learn excels at tasks such as evaluating model performance and optimizing model hyperparameters in just a few lines of code. Keras provides a wrapper class that allows you to use your deep learning models with scikit-learn.


# Keras
* https://keras.io/
* https://github.com/fchollet/keras




## Datasets
* **CIFAR-10**
	- One popular toy image classification dataset is the CIFAR-10 dataset. This dataset consists of 60,000 tiny images that are 32 pixels high and wide. Each image is labeled with one of 10 classes (for example “airplane, automobile, bird, etc”). These 60,000 images are partitioned into a training set of 50,000 images and a test set of 10,000 images.
	- http://www.cs.toronto.edu/~kriz/cifar.html
* **Pima Indians**


* **Ionosphere**

http://cv-tricks.com/tensorflow-tutorial/understanding-alexnet-resnet-squeezenetand-running-on-tensorflow/


## References
* ml-class . org
* http://cs231n.github.io/convolutional-networks/
* http://cs231n.stanford.edu/
* https://github.com/cberzan/highway-sfm
* https://www.cse.wustl.edu/~furukawa/
* https://github.com/mapillary/OpenSfM
* http://blog.mapillary.com/product/2017/05/03/mapillary-vistas-dataset.html
* http://blog.mapillary.com/update/2016/10/31/denser-3d-point-clouds-in-opensfm.html
* http://blog.mapillary.com/update/2016/09/27/semantic-segmentation-object-recognition.html
* http://openmvg.readthedocs.io/en/latest/software/SfM/IncrementalSfM/
* http://vhosts.eecs.umich.edu/vision//projects/ssfm/
* http://cvgl.stanford.edu/resources.html
* http://cvgl.stanford.edu/3d-r2n2/
* http://www.cs.cornell.edu/~asaxena/learningdepth/ijcv_monocular3dreconstruction.pdf
* http://www.theia-sfm.org/sfm.html

## Books
* https://leonardoaraujosantos.gitbooks.io/artificial-inteligence/content/chapter1.html


Adaptive structure from motion with a contrario model estimation
Incremental SfM
[ACSfM]	Adaptive structure from motion with a contrario model estimation. Pierre Moulon, Pascal Monasse, and Renaud Marlet. In ACCV, 2012.

We consider the task of 3-d depth estimation from a single still image. We take a supervised learning approach to this problem, in which we begin by collecting a training set of monocular images (of unstructured indoor and outdoor environments which include forests, sidewalks, trees, buildings, etc.) and their corresponding ground-truth depthmaps. Then, we apply supervised learning to predict the value of the depthmap as a function of the image.

# NumPy - Numerical Python
> NumPy is an acronym for "Numeric Python" or "Numerical Python"

* http://www.python-course.eu/matrix_arithmetic.php

## Scalars
* It's possible to create multidimensional arrays in numpy. Scalars are zero dimensional.
```python
x = np.array(42) #scalar```

## Vectors
## 1-demensional Arrays
* 1-dimenional array - better known to some as **vectors**
```python
F = np.array([1, 1, 2, 3, 5, 8, 13, 21])
```

### Two- and Multidimensional Arrays
* 2-dimensional array
```python
A = np.array([ [3.4, 8.7, 9.9], 
               [1.1, -7.8, -0.7],
               [4.1, 12.3, 4.8]])
```

## Shape of an Array
* The "shape" of an array is a tuple with the number of elements per axis (dimension).
```python
import numpy as np
A=np.array([[1,2,3],[4,5,6]])
A.ndim
np.shape(A)
A.shape #outputs (2,3)
type(A)
A.shape=(3,2) #change the shape
```

## Indexing and Slicing
```python
S = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(S[2:5])
print(S[:4])
print(S[6:])
print(S[:])

A = np.array([
[11,12,13,14,15],
[21,22,23,24,25],
[31,32,33,34,35],
[41,42,43,44,45],
[51,52,53,54,55]])

# The reshape function is used to construct the two-dimensional array. 
X = np.arange(28).reshape(4,7)
print(X)

#A[start:stop:step]
print(X[::2, ::3])

E = np.ones((2,3))
Z = np.zeros((2,4)


# We can create identity arrays with the function identity:
# identity(n, dtype=None)
np.identity(4)

# Another way to create identity arrays provides the function eye. It returns a 2-D array with ones on the diagonal and zeros elsewhere.
# eye(N, M=None, k=0, dtype=float)
np.eye(5, 8, k=1, dtype=int)

# Array concatination
x = np.array([11,22])
y = np.array([18,7,6])
z = np.array([1,3,5])
c = np.concatenate((x,y,z))
```
>Attention: Whereas slicings on lists and tuples create new objects, a slicing operation on an array creates a view on the original array. So we get an another possibility to access the array, or better a part of the array. From this follows that if we modify a view, the original array will be modified as well.

**Arrays v/s Lists**
* http://pythoncentral.io/the-difference-between-a-list-and-an-array/
* https://stackoverflow.com/questions/1514553/how-to-declare-an-array-in-python
```
from array import array
```

# SciPy - Scientific Python
> SciPy extends the capabilities of NumPy with further useful functions for minimization, regression, Fourier-transformation and many others.

* http://www.scipy-lectures.org/index.html


# Matplotlib
Python in combination with Numpy, Scipy and Matplotlib can be used as a replacement for MATLAB.


# Tutorials
## LeNet – Convolutional Neural Network in Python

* http://www.pyimagesearch.com/2016/08/01/lenet-convolutional-neural-network-in-python/
* http://www.pyimagesearch.com/2016/07/25/convolutions-with-opencv-and-python/

convolutional, activation, and pooling layers, fully-connected layer, activation, another fully-connected, and finally a softmax classifier

In many ways, LeNet + MNIST is the “Hello, World” equivalent of Deep Learning for image classification.

https://www.pyimagesearch.com/pyimagesearch-gurus/

- Common splits include the standard 60,000/10,000, 75%/25%, and 66.6%/33.3%. I’ll be using 2/3 of the data for training and 1/3 of the data for testing later in the blog post.


http://scikit-learn.org/stable/
https://keras.io/
- It’s a minimalist, modular neural network library that can use either Theano or TensorFlow as a backend.
- Keras is a high-level neural networks API, written in Python and capable of running on top of either TensorFlow or Theano. It was developed with a focus on enabling fast experimentation. Being able to go from idea to result with the least possible delay is key to doing good research.
```
sudo apt-get install python-numpy python-scipy -y
sudo apt-get install python-yaml -y
sudo apt-get install libhdf5-serial-dev -y
sudo pip install keras==1.0.8
```


http://opencv.org/

```
sudo -H pip install -U scikit-learn
```
Image processing in Python
http://scikit-image.org/
https://scikits.appspot.com/scikit-image
- scikit-image is a collection of algorithms for image processing
```
sudo -H pip install scikit-image
```


https://medium.com/@acrosson/installing-nvidia-cuda-cudnn-tensorflow-and-keras-69bbf33dce8a

http://chrisstrelioff.ws/sandbox/2014/06/04/install_and_setup_python_and_packages_on_ubuntu_14_04.html



In reality, an (image) convolution is simply an element-wise multiplication of two matrices followed by a sum.http://www.pyimagesearch.com/2016/08/01/lenet-convolutional-neural-network-in-python/

http://www.pyimagesearch.com/2016/07/25/convolutions-with-opencv-and-python/
http://www.pyimagesearch.com/2016/08/01/lenet-convolutional-neural-network-in-python/



an image is just a multi-dimensional matrix
-  image has a width (# of columns) and a height (# of rows), just like a matrix.
-  images also have a depth to them — the number of channels in the image.
-  for a standard RGB image, we have a depth of 3 — one channel for each of the Red, Green, and Blue channels, respectively.

- we can think of an image as a big matrix and kernel or convolutional matrix as a tiny matrix that is used for blurring, sharpening, edge detection, and other image processing functions.
- this tiny kernel sits on top of the big image and slides from left-to-right and top-to-bottom, applying a mathematical operation (i.e., a convolution) at each (x, y)-coordinate of the original image.
- blurring (average smoothing, Gaussian smoothing, median smoothing, etc.)
- edge detection (Laplacian, Sobel, Scharr, Prewitt, etc.), 
- sharpening
- all of these operations are forms of hand-defined kernels that are specifically designed to perform a particular function. is there a way to automatically learn these types of filters? And even use these filters for image classification and object detection?
- Convolution is simply the sum of element-wise matrix multiplication between the kernel and neighborhood that the kernel covers of the input image.

* Open Data for Deep Learning
	- https://deeplearning4j.org/opendata
	- https://www.kaggle.com/c/dogs-vs-cats

* http://cv-tricks.com/tensorflow-tutorial/training-convolutional-neural-network-for-image-classification/
- Neural Networks are essentially mathematical models to solve an optimization problem.
- In this example, you can see that the weights are the property of the connection, i.e. each connection has a different weight value while bias is the property of the neuron.
- The networks which have many hidden layers tend to be more accurate and are called deep network and hence machine learning algorithms which uses these deep networks are called deep learning.
- Typically, all the neurons in one layer, do similar kind of mathematical operations and that’s how that a layer gets its name(Except for input and output layers as they do little mathematical operations)

* Convolutional Layer
* Pooling Layer
	- Pooling layer is mostly used immediately after the convolutional layer to reduce the spatial size(only width and height, not depth). This reduces the number of parameters, hence computation is reduced. 
	- The most common form of pooling is Max pooling where we take a filter of size $F*F$ and apply the maximum operation over the $F*F$ sized part of the image.
* Fully Connected Layer
	- If each neuron in a layer receives input from all the neurons in the previous layer, then this layer is called fully connected layer.
	- The output of this layer is computed by matrix multiplication followed by bias offset.


$cost=0.5\sum_{i=0}^n(y_{actual} - y_{prediction})^2$

~/.keras/keras.json

- The objective of our training is to learn the correct values of weights/biases for all the neurons in the network that work to do classification between dog and cat.
- The Initial value of these weights can be taken anything but it works better if you take normal distributions(with mean zero and small variance).
- There are other methods to initialize the network but normal distribution is more prevalent.

http://www.ee.co.za/article/anatomy-mobile-mapping-system.html

http://www.pointcloudviz.com/
  
# Concepts

## Overfitting
=> https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html

* Since we only have few examples, our number one concern should be overfitting. Overfitting happens when a model exposed to too few examples learns patterns that do not generalize to new data, i.e. when the model starts using irrelevant features for making predictions.
* For instance, if you, as a human, only see three images of people who are lumberjacks, and three, images of people who are sailors, and among them only one lumberjack wears a cap, you might start thinking that wearing a cap is a sign of being a lumberjack as opposed to a sailor. You would then make a pretty lousy lumberjack/sailor classifier.
* Data augmentation is one way to fight overfitting, but it isn't enough since our augmented samples are still highly correlated.
*  Your main focus for fighting overfitting should be the **entropic capacity** of your model --how much information your model is allowed to store. A model that can store a lot of information has the potential to be more accurate by leveraging more features, but it is also more at risk to start storing irrelevant features. Meanwhile, a model that can only store a few features will have to focus on the most significant features found in the data, and these are more likely to be truly relevant and to generalize better.

**Entropy**
* https://en.wikipedia.org/wiki/Entropy_(information_theory)
- Generally, information entropy is the average information of all possible outcomes.

* There are different ways to modulate **entropic capacity**. The main one is the choice of **the number of parameters in your model**, i.e.
	- the number of layers
	- the size of each layer
	- weight regularization
		- such as L~1~ or L~2~ regularization, which consists in forcing model weights to taker smaller values.
	- Data augmentation
	- Dropout
		- Dropout also helps reduce overfitting, by preventing a layer from seeing twice the exact same pattern, thus acting in a way analoguous to data augmentation (you could say that both dropout and data augmentation tend to disrupt random correlations occuring in your data).

## Learning Keras by Implementing the VGG Network From Scratch
https://hackernoon.com/learning-keras-by-implementing-vgg16-from-scratch-d036733f2d5


## What are Convolutional Neural Networks and why are they important?
* https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/

In CNN terminology, the 3×3 matrix is called a ‘filter‘ or ‘kernel’ or ‘feature detector’ and the matrix formed by sliding the filter over the image and computing the dot product is called the ‘Convolved Feature’ or ‘Activation Map’ or the ‘Feature Map‘. It is important to note that filters acts as feature detectors from the original input image.

we can perform operations such as Edge Detection, Sharpen and Blur just by changing the numeric values of our filter matrix before the convolution operation [8] – this means that different filters can detect different features from an image, for example edges, curves etc. More such examples are available in Section 8.2.4 here.

In practice, a CNN learns the values of these filters on its own during the training process (although we still need to specify parameters such as number of filters, filter size, architecture of the network etc. before the training process). The more number of filters we have, the more image features get extracted and the better our network becomes at recognizing patterns in unseen images.

The size of the Feature Map (Convolved Feature) is controlled by three parameters that we need to decide before the convolution step is performed:
* Depth - Depth corresponds to the number of filters we use for the convolution operation.
* Stride - Stride is the number of pixels by which we slide our filter matrix over the input matrix.
* Zero-padding - Sometimes, it is convenient to pad the input matrix with zeros around the border, so that we can apply the filter to bordering elements of our input image matrix.

### Introducing Non Linearity (ReLU)
- **ReLU** stands for Rectified Linear Unit and is a non-linear operation. Other non linear functions such as tanh or sigmoid.
- ReLU is an element wise operation (applied per pixel) and replaces all negative pixel values in the feature map by zero.
- The purpose of ReLU is to introduce non-linearity in our ConvNet, since most of the real-world data we would want our ConvNet to learn would be non-linear
- Convolution is a linear operation – element wise matrix multiplication and addition, so we account for non-linearity by introducing a non-linear function like ReLU
- The ReLU operation applied to the feature maps provides the output feature map referred to as the **Rectified feature map**.

### The Pooling Step
- The function of Pooling is to progressively reduce the spatial size of the input representation
- Spatial Pooling (also called subsampling or downsampling) reduces the dimensionality of each feature map but retains the most important information.
- Spatial Pooling can be of different types: Max, Average, Sum etc.
- In case of Max Pooling, we define a spatial neighborhood (for example, a 2×2 window) and take the largest element from the rectified feature map within that window. Instead of taking the largest element we could also take the average (Average Pooling) or sum of all elements in that window. In practice, Max Pooling has been shown to work better.
- pooling operation is applied separately to each feature map (notice that, due to this, we will get three output maps from three input rectified feature maps.
- makes the input representations (feature dimension) smaller and more manageable
- reduces the number of parameters and computations in the network, therefore, controlling overfitting
- makes the network invariant to small transformations, distortions and translations in the input image (a small distortion in input will not change the output of Pooling – since we take the maximum / average value in a local neighborhood).
- helps us arrive at an almost scale invariant representation of our image (the exact term is “equivariant”). This is very powerful since we can detect objects in an image no matter where they are located 

**basic building blocks of any CNN**
- Convolution, ReLU & Pooling layers
- The output of the last Pooling Layer acts as an input to the Fully Connected Layer, which we will discuss in the next section.
- The output from the convolutional and pooling layers represent high-level features of the input image.
- In general, the more convolution steps we have, the more complicated features our network will be able to learn to recognize.
- In a traditional feedforward neural network we connect each input neuron to each output neuron in the next layer. That’s also called a fully connected layer, or affine layer. In CNNs we don’t do that. Instead, we use convolutions over the input layer to compute the output. This results in local connections, where each region of the input is connected to a neuron in the output. Each layer applies different filters, typically hundreds or thousands, and combines their results. During the training phase, a CNN automatically learns the values of its filters based on the task you want to perform.


### Fully Connected Layer
- The Fully Connected layer is a traditional Multi Layer Perceptron that uses a softmax activation function in the output layer (other classifiers like SVM can also be used)
- The purpose of the Fully Connected layer is to use the high-level features of the input image provided as an output from the convolutional and pooling layer, for classifying the input image into various classes based on the training dataset.
- The sum of output probabilities from the Fully Connected Layer is 1. This is ensured by using the Softmax as the activation function in the output layer of the Fully Connected Layer.

The **Softmax function** takes a vector of arbitrary real-valued scores and squashes it to a vector of values between zero and one that sum to one.

### Putting it all together – Training using Backpropagation
- Convolution + Pooling layers act as Feature Extractors from the input image while Fully Connected layer acts as a classifier.




### References
* http://cs.nyu.edu/~fergus/tutorials/deep_learning_cvpr12/
* https://ujjwalkarn.me/2016/08/09/quick-intro-neural-networks/
* http://mlss.tuebingen.mpg.de/2015/slides/fergus/Fergus_1.pdf
* https://github.com/rasbt/python-machine-learning-book/blob/master/faq/difference-deep-and-normal-learning.md
* https://www.quora.com/How-is-a-convolutional-neural-network-able-to-learn-invariant-features
#### Convolutional Neural Networks
* http://cs231n.github.io/convolutional-networks/
* http://www.wildml.com/2015/11/understanding-convolutional-neural-networks-for-nlp/
* https://docs.gimp.org/en/plug-in-convmatrix.html
* http://colah.github.io/posts/2014-07-Understanding-Convolutions/

### Feature_extraction_using_convolution
* http://deeplearning.stanford.edu/wiki/index.php/Feature_extraction_using_convolution


### Image Segmentations & Classification
The process of classifying each part of an image in different categories is called “image segmentation”.
* http://qucit.com/implementation-of-segnet/
* https://github.com/kjw0612/awesome-deep-vision

the last layer for a sigmoid one. The role of a softmax layer is to force the model to take a decision in a classification problem. Say you want to classify a pixel in one of three classes. A neural network will typically produce a vector of 3 probabilities, some of which can be close to each other, like [0.45, 0.38, 0.17].
But what you really want is just to know to which class this pixel belongs! Taking the maximum probability will give you a [1, 0, 0] vector which is what you want, but the max function isn’t differentiable, so your model can’t learn if you use it. A soft max is a kind of differentiable max, it won’t exactly give you a [1, 0, 0] vector, but something really close


The role of a sigmoid function is to output a value between 0 and 1, we use it to obtain the probability that a given pixel is a building pixel, thus obtaining something similar to a heatmap of this probability for each image.

* http://nghiaho.com/?p=1765
* https://devblogs.nvidia.com/parallelforall/exploring-spacenet-dataset-using-digits/
* https://aws.amazon.com/public-datasets/spacenet/

* http://nicolovaligi.com/converting-deep-learning-model-caffe-keras.html

**companies Involved**
*  DigitalGlobe, CosmiQ Works, and NVIDIA; SpaceNet

#### Keywords
*  Dilated Convolutions

#### References
* [MULTI-SCALE CONTEXT AGGREGATION BY
DILATED CONVOLUTIONS](https://arxiv.org/pdf/1511.07122.pdf)

The dilated convolution operator has been referred to in the past as “convolution with a dilated filter”

### Road Segmentation
* http://mi.eng.cam.ac.uk/projects/segnet/tutorial.html

SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Segmentation 

https://www.youtube.com/watch?v=G15Dg2QoI_M

How to Simulate a Self-Driving Car
https://www.youtube.com/watch?v=EaY5QiZwSP4


https://medium.com/self-driving-cars/term-1-in-depth-on-udacitys-self-driving-car-curriculum-ffcf46af0c08

https://github.com/udacity/self-driving-car-sim

https://hackernoon.com/five-skills-self-driving-companies-need-8546d2aba7c1

https://developers.google.com/edu/c++/getting-started

https://github.com/CPFL/Autoware

#### News/Articles
* http://www.dailymail.co.uk/sciencetech/article-3371075/See-world-eyes-driverless-car-town-Interactive-tool-reveals-autonomous-vehicles-navigate-streets.html
* http://www.sanborn.com/highly-automated-driving-maps-for-autonomous-vehicles/


#### caffe-segnet

**Errors while installation**
* hdf5 dir not found HDF5_DIR-NOTFOUND
https://github.com/NVIDIA/DIGITS/issues/156

#### keras-segnet
* https://github.com/imlab-uiip/keras-segnet
```
sudo pip install pandas
```

model.add(Convolution2D(112,3,3, border_mode='same',init='uniform',input_shape=(136,136,3),dim_ordering='tf',name='conv_1.1'))
model.add(Conv2D(112,(3,3), border_mode='same',kernel_initializer='uniform',input_shape=(136,136,3),dim_ordering='tf',name='conv_1.1'))

https://github.com/tensorflow/cleverhans/issues/109

Convolutional2D -> CONV2D with following parameters have changed name/format:-
 Conv2D(10, 3, 3) becomes Conv2D(10, (3, 3))
 kernel_size can be set to an integer instead of a tuple, e.g. Conv2D(10, 3) is equivalent to Conv2D(10, (3, 3))
subsample -> strides
border_mode -> padding
nb_filter -> filters

## python

Recap of ways to create a 1-d array
array(a):
Creates an array from the list a.
linspace(start, stop, num):
Returns num evenly spaced numbers over an interval from start to stop inclusive. [num=50 if omitted.]
logspace(start, stop, num):
Returns num logarithmically spaced numbers over an interval from 10^{\mathrm{start}} to 10^{\mathrm{stop}} inclusive. [num=50 if omitted.]
arange([start,] stop[, step,], dtype=None):
Returns data points from start to end, exclusive, evenly spaced by step. [step=1 if omitted. start=0 and step=1 if both are omitted.]
zeros(num, dtype=float):
Returns an an array of 0s with num elements. Optional dtype argument can be used to set data type; left unspecified, a float array is made.
ones(num, dtype=float):
Returns an an array of 1s with num elements. Optional dtype argument can be used to set data type; left unspecified, a float array is made.


We see that NumPy calculates the logarithm where it can, and returns nan (not a number) for an illegal operation, taking the logarithm of a negative number, and -inf, or -\infty for the logarithm of zero.We see that NumPy calculates the logarithm where it can, and returns nan (not a number) for an illegal operation, taking the logarithm of a negative number, and -inf, or -\infty for the logarithm of zero.

These kinds of operations with arrays are called vectorized operations because the entire array, or “vector”, is processed as a unit. Vectorized operations are much faster than processing each element of arrays one by one.

### SfM
* http://nghiaho.com/?p=2379


# Case Studies

## [MULTI-SCALE CONTEXT AGGREGATION BY DILATED CONVOLUTIONS](https://arxiv.org/pdf/1511.07122.pdf)

The dilated convolution operator has been referred to in the past as “convolution with a dilated filter”

* https://github.com/BVLC/caffe/issues/782
* https://github.com/BVLC/caffe/issues/263
* https://stackoverflow.com/questions/14585598/installing-numba-for-python

```
#python caffe path
#custom
export CAFFE_ROOT=$HOME/Documents/ml/caffe-segnet
#export PATH=$PATH:$CAFFE_ROOT/build/tools
export PYTHONPATH=$CAFFE_ROOT/python
# Install numba
sudo pip install numba
#
python predict.py dilation10_cityscapes.caffemodel 1.jpg
usage: predict.py [-h] [-o OUTPUT_PATH] [--gpu GPU]
                  [{pascal_voc,camvid,kitti,cityscapes}] [input_path]
predict.py: error: argument dataset: invalid choice: 'dilation10_cityscapes.caffemodel' (choose from 'pascal_voc', 'camvid', 'kitti', 'cityscapes')
#correct command
python predict.py pascal_voc 1.jpg
```

* https://github.com/richzhang/colorization/issues/2


Using CPU
[libprotobuf ERROR google/protobuf/text_format.cc:274] Error parsing text-format caffe.NetParameter: 297:13: Message type "caffe.ConvolutionParameter" has no field named "dilation".
WARNING: Logging before InitGoogleLogging() is written to STDERR
F0628 20:12:54.126731 13129 upgrade_proto.cpp:928] Check failed: ReadProtoFromTextFile(param_file, param) Failed to parse NetParameter file: models/dilation10_cityscapes_deploy.prototxt
*** Check failure stack trace: ***
Aborted (core dumped)

 Network initialization done.
[libprotobuf WARNING google/protobuf/io/coded_stream.cc:537] Reading dangerously large protocol message.  If the message turns out to be larger than 2147483647 bytes, parsing will be halted for security reasons.  To increase the limit (or to disable these warnings), see CodedInputStream::SetTotalBytesLimit() in google/protobuf/io/coded_stream.h.
[libprotobuf WARNING google/protobuf/io/coded_stream.cc:78] The total number of bytes read was 537496438
F0629 00:41:04.755961 18550 syncedmem.hpp:33] Check failed: *ptr host allocation of size 4464377856 failed
*** Check failure stack trace: ***
Aborted (core dumped)


**protobuff**
* https://github.com/google/protobuf/blob/master/src/README.md
* https://github.com/google/protobuf                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      





python convert.py \
  --caffemodel=~/Documents/ml/dilation/pretrained/dilation8_pascal_voc.caffemodel \
  --code-output-path=./pascal_voc_tf/dil8_net.py \
  --data-output-path=./pascal_voc_tf/ \
  ~/Documents/ml/dilation/models/dilation8_pascal_voc_deploy.prototxt


python convert.py def_path=~/Documents/ml/dilation/models/dilation8_pascal_voc_deploy.prototxt --caffemodel=~/Documents/ml/dilation/pretrained/dilation8_pascal_voc.caffemodel --code-output-path=./pascal_voc_tf/dil8_net.py --data-output-path=./pascal_voc_tf/

## Pre-training, Transfer Learning
* https://www.analyticsvidhya.com/blog/2017/06/transfer-learning-the-art-of-fine-tuning-a-pre-trained-model/
* https://www.analyticsvidhya.com/blog/2017/05/neural-network-from-scratch-in-python-and-r/

https://github.com/alexgkendall/caffe-segnet/issues/3

## Tutorials
## Machine Learning
https://elitedatascience.com/learn-machine-learning
https://www.datacamp.com/community/tutorials/deep-learning-python#gs.ny4aO4s

## Python
https://elitedatascience.com/learn-python-for-data-science


## WebGL GPU based deep learning in browser
* https://github.com/transcranial/keras-js
* https://news.ycombinator.com/item?id=12302932
* https://erkaman.github.io/regl-cnn/src/demo.html

https://github.com/uber/horovod
http://timdettmers.com/2017/04/09/which-gpu-for-deep-learning/


** Hardware Guides for Deep Learning
http://timdettmers.com/2015/03/09/deep-learning-hardware-guide/


## MOOC Courses
https://www.coursera.org/learn/neural-networks
