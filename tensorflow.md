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
* https://github.com/jtoy/awesome-tensorflow

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
* Documentations
  - https://www.tensorflow.org/versions/master/api_guides/python/array_ops#to_float
* Tutorials
  - https://www.tensorflow.org/tutorials/
  - http://learningtensorflow.com/Visualisation/
* TensorFlow is a way of representing computation without actually performing it until asked


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
* InteractiveSession
* Memory footprint of the python session:
```bash
import resource
print("{} Kb".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
```
* tf.slice
* tf.matmul


**Visualisation with TensorBoard**
- https://www.tensorflow.org/guide/graph_viz
* TensorBoard currently supports five visualizations: scalars, images, audio, histograms, and graphs.
```python
writer = tf.summary.FileWriter("outputDir", sess.graph)
# sess.run code
writer.close()
```
* View the summary:
```bash
tensorboard --logdir=path/to/outputDir
```
- webserver starts: `6006` port
- Scopes:
```python
with tf.name_scope("Scope-A"):
  c =tf.div(b,2, name="Divide")
```
- [Tensor-Board-Debugger (TDB) - dev stagnated](https://github.com/ericjang/tdb)

**Reading Files**
- supports reading larger datasets, specifically so that the data is never all kept in memory at once
- also has support for writing custom data handlers
  * https://www.tensorflow.org/extend/new_data_formats
- basics of reading a CSV file, using TensorFlow, and using that data in a graph
- `tf.reduce_sum`
- `tf.Print` -  It basically logs the current values in the second parameter
- tf.pack
- tf.train.shuffle_batch
  * to batch together multiple lines into a single variable. This is more useful for larger datasets than reading on a row-by-row basis
  * a good target is to load as much data as you can in a single batch, but not too much that it overloads your computer’s RAM
  * As another aside, not all of the data is returned when using a batch – if the batch doesn’t fill, it isn’t returned.

**TensorFlow in AWS**
- http://learningtensorflow.com/aws/
Amazon Web Services (AWS) is a secure cloud services platform, which offers compute power, database storage, content delivery and other functionality to help businesses scale and grow. Additionally, Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers.
- https://aws.amazon.com/ec2/pricing/

* elementwise operation
  - An elementwise operation, where the elements from each list are considered in turn, added together and then the results combined
* broadcasting
  - if we add a one-dimensional array to a two-dimensional matrix
  - the array was broadcasted to the shape of the matrix, resulting in the array being added to each row of the matrix. Using this terminology, a matrix is a list of rows.
- tf.shape

**Training and Convergence**
- Gradient Descent
  - Gradient Descent is a learning algorithm that attempts to minimise some error. Which error do you ask? Well that is up to us, although there are a few commonly used methods.
  * Different ways to define error:
    - defined as the square of the differences
  - 'train_op = tf.train.GradientDescentOptimizer(0.01).minimize(error)'

**Optimizers**
TensorFlow has a whole set of types of optimisation, and has the ability for your to define your own as well (if you are into that sort of thing).
- https://www.tensorflow.org/versions/master/api_docs/python/tf/train#optimizers
- The listed ones are:
  * GradientDescentOptimizer
  * AdagradOptimizer
  * MomentumOptimizer
  * AdamOptimizer
  * FtrlOptimizer
  * RMSPropOptimizer

**Plotting the error**
- windowed average here – using `np.mean(errors[i-50:i])`

**Randomness**
- “weights” have to be set to initial values.
- One option for this is to start with all the weights as zeros, and go from there.  However, this causes issues algorithmically - basically, the gradients of errors have trouble fixing errors. Instead, we often set these weights to random values. After that point, the model learns and adjusts.
- generating random numbers, this includes distributions like uniform, normal and others.

* **Uniform distributions** are like those you get when you roll a dice - there is a set of values, and they are all equally likely.
```python
x = tf.random_uniform((6, 4), seed=42)
from matplotlib import pyplot as plt
#
plt.hist(x  .flatten())
plt.show()
```
  - A uniform distribution can be quite useful for initialising weights in machine learning models, if you don’t have any other information to go by.
  -  It is also a “bounded” distribution, whereby it has a set minimum and maximum value, and the random values cannot fall outside that range
  - To change the range, for instance to 0 and 10, you multiply by the range and add the minimum. There is an exercise on this at the end of the lesson.
* **Normal distributions** are the standard taught in statistics classes, where the data has a mean that is more likely, and a “bell-shaped” curve around it.
```python
x = tf.random_normal((600, 4), seed=42)
x1 =  tf.random_normal((10000,), seed=42, mean=170, stddev=15)
from matplotlib import pyplot as plt
#
plt.hist(x  .flatten())
plt.show()
```
  - This distribution, by default, has a mean of around 0 and a standard deviation of 1.
  - The values are not bounded, but become highly unlikely the further from the mean you stray, with the standard deviation setting the rate of decrease in likelihood.
  - In practice, around 60% of values fall within a “radius” of one standard deviation from the mean in each direction, and 99% fall within 4 standard deviations.

**Classifying With Linear Models**
- called supervised machine learning or classification
- The task is to try and work out the relationship between some input data and an output value.
-  In practical terms, the input data could be measurements, such as height or weight, and the output value would be the expected prediction, such as “cat” or “dog”.

**Linear Equations**
- `tf.solve`

**3D**
- TensorFlow is not just a deep learning library - it is a library for performing manipulations on numbers, and as such it can perform tasks that many other libraries can.
- A 3D object can be modelled as a series of triangles in three-dimensional space
- triangle is created from three of these 3D points. A point itself can be represented as a vector with size (3,). An array of these is a matrix of size (n, 3), where n is the number of points we have.

* Translation
  - A translation is a simple move: up/down, left/right, forward/backwards, or some combination of these.
  - It is created by simply adding a vector to each point.
  - If you add the same vector to all points, then the whole object will move in unison.
* Rotation
  - A rotation is formed by creating the dot product or a rotating matrix and the original points
  - Rotating an object first requires you to determine which axis you are rotating over
  - To rotate around a particular axis, set that axis’ value to zeros, with a 1 in the related axis
  - theta is the number of degrees to rotate the object.
  - There are three matrices you need:
    * Rotating around the x-axis
    ```python
    [[1,0,0],
     [0, cos \theta, sin \theta],
     [0, -sin \theta, cos \theta]]
    ```
    * Rotating around the y-axis
    ```python
    [[cos \theta, 0, -sin \theta],
    [0,1,0],
    [sin \theta, 0, cos \theta]]
    ```
    * Rotating around the z-axis
    ```python
    [[cos \theta, sin \theta, 0],
    [-sin \theta, cos \theta, 0],
    [0,0,1]]
    ```
  - You take a point, compute the dot product with one of these matrices, and then the point is rotated around the relevant axis.
  - We can also compute the dot product of one of these (3, 3) matrices against our (n, 3) points matrix. However, for a dot product to work, you need to have the inner dimensions matrix (and n is not necessarily 3)
  -  Therefore, you need to put the points matrix first - then it becomes a dot product of a (n, 3) matrix with a (3, 3) matrix
**TensorFlow Learn**
- TensorFlow Learn, which is the new name for a package called skflow
- It is a machine learning wrapper, based to the scikit-learn API, allowing you to perform data mining with ease.
* Machine Learning
  - Machine Learning is the idea that you build algorithms that learn from data, in order to perform actions on new data.
  - In this context, what this means is that we have some input training data, and the expected outcome - the training targets.
  - There are also variants called regression and clustering
  -  In data mining, you should never evaluate your data on the same data you used to train. The potential problem is called “overfitting”, where the model learns exactly what it needs to for the training data, but is unable to predict well on new unseen data. To address this, we need to split our training and testing data.
  - Accuracy Measurements:
    * https://en.wikipedia.org/wiki/F1_score

## API
- https://www.tensorflow.org/api_docs/python/

* tf.constant
* tf.solve
* tf.stack
* tf.matmul
* tf.to_float
* tf.cos, tf.sin
* tf.float32
* tf.add, tf.multiply, tf.div
* tf.py_func
  - https://www.tensorflow.org/api_docs/python/tf/py_func
  - Wraps a python function and uses it as a TensorFlow op.
  -  allows us to take a python function and turn it into a node in TensorFlow.
* `tf.device`
* `python -c "import tensorflow as tf; print(tf.__version__)"`


## GPU supprt
- http://learningtensorflow.com/lesson10/
* What types of operations should I send to the GPU?
  -  if the step of the process can be described such as “do this mathematical operation thousands of times”, then send it to the GPU.
  - Examples include matrix multiplication and computing the inverse of a matrix
  - many basic matrix operations are prime candidates for GPUs. 
  - As an overly broad and simple rule, other operations should be performed on the CPU.
  - There is also a cost to changing devices and using GPUs. GPUs don’t have direct access to the rest of your computer (except, of course for the display). Due to this, if you are running a command on a GPU, you need to copy all of the data to the GPU first, then do the operation, then copy the result back to your computer’s main memory. TensorFlow handles this under the hood, so the code is simple, but the work still needs to be performed.
```python
with tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)):
    # Run your graph here
```


## Distributed Computing with TensorFlow
* http://learningtensorflow.com/lesson11/
- TensorFlow supports distributed computing, allowing portions of the graph to be computed on different processes, which may be on completely different servers! 
- In addition, this can be used to distribute computation to servers with powerful GPUs, and have other computations done on servers with more memory, and so on
- TensorFlow works a bit like a server-client model. The idea is that you create a whole bunch of workers that will perform the heavy lifting. You then create a session on one of those workers, and it will compute the graph, possibly distributing parts of it to other clusters on the server.
- In order to do this, the main worker, the master, needs to know about the other workers. This is done via the creation of a ClusterSpec, which you need to pass to all workers. A ClusterSpec is built using a dictionary, where the key is a “job name”, and each job contains many workers.
```python
# reates a ClusterSpect with a job name of “local” and two worker processes.
import tensorflow as tf
cluster = tf.train.ClusterSpec({"local": ["localhost:2222", "localhost:2223"]})
#
# Next up, we start the process. To do this, we graph one of these workers, and start it:
server = tf.train.Server(cluster, job_name="local", task_index=1)
```
*
```python
##
# Get task number from command line
import sys
task_number = int(sys.argv[1])
#
import tensorflow as tf
#
cluster = tf.train.ClusterSpec({"local": ["localhost:2222", "localhost:2223"]})
server = tf.train.Server(cluster, job_name="local", task_index=task_number)
#
print("Starting server #{}".format(task_number))
#
server.start()0
server.join()
```
**Map and Reduce**
- MapReduce is a popular paradigm for performing large operations
  *  The first step is known as a map, which means “take this list of things, and apply this function to each of them”. 
    - “How can I split this problem into subproblems that can be solved independently?” - there is your map.
  * The second step is a reduce, which means “take this list of things, and combine them using this function”.
    -  Second, “How can I combine the answers to form a final result?” - there is your reduce.
    -  A common reduce operation is sum - i.e “take this list of numbers and combine them by adding them all up”, which can be performed by creating a function that adds two numbers. 

* In distributed TensorFlow, performing map and reduce operations is a key building block of many non-trivial programs. Example:
  - an ensemble learning may send individual machine learning models to multiple workers, and then combine the classifications to form the final result. 


# Artifical Life
https://en.wikipedia.org/wiki/Artificial_life

## Zero Player Games
- https://en.wikipedia.org/wiki/Zero-player_game
- https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
- https://jakevdp.github.io/blog/2013/08/07/conways-game-of-life/
A zero-player game or no-player game is a game that has no sentient players.

In computer games, the term refers to programs that use artificial intelligence rather than human players.

In addition, some fighting and real-time strategy games can be put into zero-player mode where one AI plays against another AI.