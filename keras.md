---
title: keras
Decription: keras
Author: Bhaskar Mangal
Date: 26th-Dec-2018
Last Updated: 26th-Dec-2018
Tags: keras, Deep Learning Framework
---

**Table of Contents**
* TOC
{:toc}


## Keras

* https://elitedatascience.com/keras-tutorial-deep-learning-in-python
* https://uwaterloo.ca/data-science/sites/ca.data-science/files/uploads/files/keras_tutorial.pdf

```python
import keras
import keras.backend as K
import keras.layers as KL
import keras.engine as KE
import keras.models as KM
#
## Core layers
KL.Dense
KL.Dropout
KL.Activation
KL.Flatten
#
## CNN Layers
KL.Conv2D
KL.MaxPooling2D
KL.BatchNormalization
KL.ZeroPadding2D
KL.Dense
KL.Conv2DTranspose
KL.UpSampling2D
##
KL.Lambda
KL.add
KL.Concatenate
KL.Reshape
KL.Input
KL.TimeDistributed
#
##
KE.Layer
#
##
KM.Model
#
##
K.squeeze
K.int_shape
K.abs
K.cast
K.less
K.equal
K.not_equal
K.sparse_categorical_crossentropy
K.binary_crossentropy
K.switch
K.mean
K.sum
K.reshape
K.learning_phase
K.function
K.shape
```


## Layers
* Recurrent layers, LSTM, GRU etc.
* 1D Convolutional layers
* 2D Convolutional layers
* Autoencoders can be built with any other type of layer
* Dropout
* Noise
* Pooling
* Normalization
* Embedding


## Losses
* **Error loss:**
  * rmse
  * mse
  * mae
  * mape
  * msle
* **Hinge loss**:
  * squared hinge
  * hinge
* **Class loss:**
  * binary_crossentropy
  * categorical_crossentropy


## Optimizers
All optimizers can be customized via parameters.

* SGD
* Adagrad
* Adadelta
* Rmsprop
* Adam

## Activations
* sigmoid
* tanh
* ReLu
* softplus
* hard sigmoid
* linear
* Advanced activations implemented as a layer (after desired neural layer)
* Advanced activations: LeakyReLu, PReLu, ELU, Parametric Softplus, Thresholded linear and Thresholded Relu


## Regulizers


## Constraints

  
## Utilities

* **Architecture/Weight Saving and Loading**
  * Model architectures can be saved and loaded
  * Model parameters (weights) can be saved and loaded
* **Callbacks**
  * Allow for function call during training
  * Callbacks can be called at different points of training batch or epoch)
  * Existing callbacks: Early Stopping, weight saving after epoch
  * Easy to build and implement, called in training function, fit()
* **Model Type**
  * **Sequential**
    * Sequential models are linear stack of layers
    * Treat each layer as object  that feeds into the next
  * **Graph**
    * Optimized over all outputs
    * Graph model allows for two or more independent networks to diverge or merge
    * Allows for multiple separate inputs or outputs
    * Different merging layers (sum or concatenate)


## Application Examples
* sentiment transitions