/*
Title: Tensorflow
Decription: Tensorflow
Author: Bhaskar Mangal
Date: 16th-Apr-2018
Last Updated: 30th-Jul-2018
Tags: Tensorflow
*/

# Tensorflow

## Tensorflow Install
* [tensorflow.install.sh](https://github.com/mangalbhaskar/linuxscripts/blob/master/tensorflow.install.sh)
* https://taesikna.github.io/install_tensorflow.html

## Concepts

### Building the TensorFlow Graph
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

## FAQs
- http://cv-tricks.com/tensorflow-tutorial/save-restore-tensorflow-models-quick-complete-tutorial/
* **What is a TensorFlow Model?**
Tensorflow model primarily contains the network design or graph and values of the network parameters that we have trained. Hence, Tensorflow model has two main files:
a) Meta graph
This is a protocol buffer which saves the complete Tensorflow graph; i.e. all variables, operations, collections etc. This file has .meta extension.
b) Checkpoint file:
This is a binary file which contains all the values of the weights, biases, gradients and all the other variables saved. This file has an extension .ckpt. However, Tensorflow has changed this from version 0.11. Now, instead of single .ckpt file, we have two files

- `checkpoint` - this file simply keeps a record of latest checkpoint files saved
- `.data` - this file contains training variables
- `.meta` - save the network in this file. This file is used to recreate the network using `tf.train.import()`

After the training is done, we want to save all the variables and network graph to a file for future use. So, in Tensorflow, you want to save the graph and values of all the parameters for which we shall be creating an instance of tf.train.Saver() class.

* How does a Tensorflow model look like?
* How to save a Tensorflow model?
* How to restore a Tensorflow model for prediction/transfer learning?
* How to work with imported pretrained models for fine-tuning and modification
```python
def save(self,
  sess,
  save_path,
  global_step=None,
  latest_filename=None,
  meta_graph_suffix="meta",
  write_meta_graph=True,
  write_state=True,
  strip_default_attrs=False):
```

**Importing a pre-trained model**

* Use pre-trained model for fine-tuning, there are two things you need to do:

1. **Create the network**
- You can create the network by writing python code to create each and every layer manually as the original model.
- The network in `.meta` saved file which can be used to recreate the network using `tf.train.import()` function like this:
```python
saver = tf.train.import_meta_graph('my_test_model-1000.meta')
```
- `import_meta_graph` appends the network defined in `.meta` file to the **current graph**. So, this will create the graph/network for you but we still need to load the value of the parameters that we had trained on this graph.

2. **Load the parameters**
We can restore the parameters of the network by calling restore on this saver which is an instance of tf.train.Saver() class.
```python
with tf.Session() as sess:
  new_saver = tf.train.import_meta_graph('my_test_model-1000.meta')
  new_saver.restore(sess, tf.train.latest_checkpoint('./'))
```

**Working with restored models**
- Develop a practical guide to restore any pre-trained model and use it for prediction, fine-tuning or further training. 
- **Note:**
	* When the network is saved, values of the placeholders are not saved.
- Now, when we want to restore it, we not only have to restore the graph and weights, but also prepare a new feed_dict that will feed the new training data to the network.
- We can get reference to these saved operations and placeholder variables via `graph.get_tensor_by_name()` method.
- If we just want to run the same network with different data, you can simply pass the new data via feed_dict to the network.


## Tutorials
* https://github.com/Hvass-Labs/TensorFlow-Tutorials
* https://github.com/MorvanZhou/Tensorflow-Tutorial
* https://learningtensorflow.com/getting_started/

**MNIST**
- https://github.com/Hvass-Labs/TensorFlow-Tutorials/blob/master/01_Simple_Linear_Model.ipynb
 
### Tensorflow
- http://learningtensorflow.com/Visualisation/
TensorFlow is a way of representing computation without actually performing it until asked
**Basics**
* tf.constant
* tf.Variable
* tf.global_variables_initializer()
* tf.Session()
  - session.run(y)
  - session.run(y,feed_dict={})
* tf.placeholder
  - So far we have used Variables to manage our data, but there is a more basic structure, the placeholder. A placeholder is simply a variable that we will assign data to at a later date. It allows us to create our operations and build our computation graph, without needing the data. In TensorFlow terminology, we then feed data into the graph through these placeholders.
  - create a placeholder called x, i.e. a place in memory where we will store value later on
  - Placeholders do not need to be statically sized.