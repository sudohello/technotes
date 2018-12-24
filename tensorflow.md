---
Title: Tensorflow
Decription: Tensorflow
Author: Bhaskar Mangal
Date: 16th-Apr-2018
Last Updated: 30th-Jul-2018
Tags: Tensorflow
---

**Table of Contents**
* TOC
{:toc}


## Tensorflow

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
 

* **Documentations**
  - https://www.tensorflow.org/versions/master/api_guides/python/array_ops#to_float
  * TensorFlow is a way of representing computation without actually performing it until asked
* **Tutorials**
  - https://www.tensorflow.org/tutorials/
  - http://learningtensorflow.com/Visualisation/


## **Basics**
* tf.Tensor
* tf.constant
* tf.Variable, tf.get_variable, tf.contrib.eager.Variable
* `tf.global_variables_initializer()`
  - This function returns a single operation responsible for initializing all variables in the `tf.GraphKeys.GLOBAL_VARIABLES` collection
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
* `tf.truncated_normal` in module `tensorflow.python.ops.random_ops`
  - `truncated_normal(shape, mean=0.0, stddev=1.0, dtype=tf.float32, seed=None, name=None)`
  - Outputs random values from a truncated normal distribution.
  - The generated values follow a normal distribution with specified mean and standard deviation, except that values whose magnitude is more than 2 standard deviations from the mean are dropped and re-picked.
  - A tensor of the specified shape filled with random truncated normal values

## [Tensor](https://www.tensorflow.org/guide/tensors)

**Tensor, Rank, Shape, Data types**
- A tensor is a generalization of vectors and matrices to potentially higher dimensions. Internally, TensorFlow represents tensors as n-dimensional arrays of base datatypes.
- `tf.Tensor` in module `tensorflow.python.framework.ops`
- It is n-dimensional array of cells
- A tensor has **dataType** and **shape**
- Each element in the Tensor has the same data type, and the data type is always known.
- The shape (that is, the number of dimensions it has and the size of each dimension) might be only partially known.
- Some types of tensors are special:
  * tf.constant
  * tf.Variable
  * tf.placeholder
  * tf.SparseTensor
- the value of a tensor is immutable, expect for `tf.Variable` tensor;  which means that in the context of a single execution tensors only have a single value. 
- However, evaluating the same tensor twice can return different values; for example that tensor can be the result of reading data from disk, or generating a random number.
* A **string** is treated as a single item in TensorFlow, not as a sequence of characters. It is possible to have scalar strings, vectors of strings, etc.
* `rank` is synonymous to `n-dimension`
* The `shape` of a tensor is the number of elements in each dimension.
* `tf.shape`, `tf.reshape`
* The number of elements of a tensor is the product of the sizes of all its shapes.
* when reshaped, the number of elements of the reshaped Tensors has to match the original number of elements.
* `tf.DType`, [Ref](https://www.tensorflow.org/api_docs/python/tf/DType)
  * float: 16,32,64
  * int: 8,16,32,64
  * bool
  * string
  * complex (64,128)
  * Other types:
    * uint (8,16,32,64) # `u` means `unsigned`
    * qint (8,16,32)  3 # `q` means `quantized`
    * quint (8,16)
    * resource (mutable resource)
    * variant (arbitary types)
    * `_ref` suffix are defined for reference-typed tensors
    * **TBD - what it means:**
      - half, single, double precision
      - signed and unsigned
      - quantized
* If you don't, TensorFlow chooses a datatype that can represent your data
* TensorFlow converts Python integers to `tf.int32` and python floating point numbers to `tf.float32`
* TensorFlow uses the same rules numpy uses when converting to arrays.
* Evaluating Tensors: `tensor.eval`

**Misc Functions**
* `tf.as_dtype` function converts numpy types and string type names to a `DType` object.
* `tf.cast` - cast tensor from one datatype to another
- tf.zeros
- tf.ones

## [Tensorflow Debugger](https://www.tensorflow.org/guide/debugger)
- tfdbg
* Printing Tensor values
```python
t = <<some tensorflow operation>>
tf.Print(t, [t])  # This does nothing
t = tf.Print(t, [t])  # Here we are using the value returned by tf.Print
result = t + 1  # Now when result is evaluated the value of `t` will be printed.
```

## [Variables](https://www.tensorflow.org/guide/variables)
* `tf.Variable` in module  `tensorflow.python.ops.variables`
* `tf.get_variable` in module `tensorflow.python.ops.variable_scope`
* `tf.contrib.eager.Variable` in module `tensorflow.python.ops.resource_variable_ops`
* Basic Usage
```python
mammal = tf.Variable("Elephant", tf.string)
ignition = tf.Variable(451, tf.int16)
floating = tf.Variable(3.14159265359, tf.float64)
its_complicated = tf.Variable(12.3 - 4.85j, tf.complex64)
#
mystr = tf.Variable(["Hello"], tf.string)
cool_numbers  = tf.Variable([3.14159, 2.71828], tf.float32)
first_primes = tf.Variable([2, 3, 5, 7, 11], tf.int32)
its_very_complicated = tf.Variable([12.3 - 4.85j, 7.5 - 6.23j], tf.complex64)
#
mymat = tf.Variable([[7],[11]], tf.int16)
myxor = tf.Variable([[False, True],[True, False]], tf.bool)
linear_squares = tf.Variable([[4], [9], [16], [25]], tf.int32)
squarish_squares = tf.Variable([ [4, 9], [16, 25] ], tf.int32)
rank_of_squares = tf.rank(squarish_squares)
mymatC = tf.Variable([[7],[11]], tf.int32)
#
my_image = tf.zeros([10, 299, 299, 3])  # batch x height x width x color
r = tf.rank(my_image) # After the graph runs, r will hold the value 4.
#
my_variable = tf.get_variable("my_variable", [1, 2, 3])
my_int_variable = tf.get_variable("my_int_variable", [1, 2, 3], dtype=tf.int32, initializer=tf.zeros_initializer)
other_variable = tf.get_variable("other_variable", dtype=tf.int32, initializer=tf.constant([23, 42]))
```
* By default every, tf.Variable gets placed in the following two collections:
  - tf.GraphKeys.GLOBAL_VARIABLES --- variables that can be shared across multiple devices,
  - tf.GraphKeys.TRAINABLE_VARIABLES --- variables for which TensorFlow will calculate gradients.
* If you don't want a variable to be trainable, add it to the tf.GraphKeys.LOCAL_VARIABLES collection instead.
```python
my_local = tf.get_variable("my_local", shape=(), collections=[tf.GraphKeys.LOCAL_VARIABLES])
my_non_trainable = tf.get_variable("my_non_trainable", shape=(), trainable=False)
```
* Partical usage
```python
import tensorflow as tf

w = tf.truncated_normal([3,3,128,128], dtype=tf.float32, stddev=1e-1)
kernel = tf.Variable(w, name="weights")
#
c = tf.constant(0.0, shape=[128], dtype=tf.float32)
biases = tf.Variable(a, trainable=True, name='biases')
```
* Initializing variables - Before a variable can be used, it must be initialized.
* When programming in the low-level TensorFlow API (that is, when explicitly creating graphs and sessions), variables must be explicitly initialized
* On the otherhand, most high-level frameworks such as tf.contrib.slim, tf.estimator.Estimator and Keras automatically initialize variables for before training a model
* `tf.global_variables_initializer()`
  - This function returns a single operation responsible for initializing all variables in the `tf.GraphKeys.GLOBAL_VARIABLES`
  - by default does not specify the order in which variables are initialized
  - `initializer=tf.zeros_initializer()`
  - Any time you use the value of a variable in a context in which not all variables are initialized (say, if you use a variable's value while initializing another variable), it is best to use variable.initialized_value() instead of variable:
```python  
v = tf.get_variable("v", shape=(), initializer=tf.zeros_initializer())
w = tf.get_variable("w", initializer=v.initialized_value() + 1)
```
* `my_variable.initializer` initialize variables explicitly
* `tf.report_uninitialized_variables()` provides list of variables not yet initialized

## [Graphs and Sessions](https://www.tensorflow.org/guide/graphs)
* [Introduction to **Dataflow Programming**](https://en.wikipedia.org/wiki/Dataflow_programming)
  - Dataflow is a common programming model for parallel computing
  - In a dataflow graph:
    * the nodes represent units of computation
    * the edges represent the data consumed (input) or produced (output) by a computation

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


## Models in TensorFlow Repo
* **Object Detections**
- https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md
- https://github.com/tensorflow/models/issues/1962
```
cd $HOME/Documents/ai-ml-dl/external/models/research
protoc -I=./ --python_out=./ ./object_detection/protos/*.proto
#
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
# Test
python object_detection/builders/model_builder_test.py
python3 object_detection/builders/model_builder_test.py
jupyter notebook object_detection/object_detection_tutorial.ipynb
```

## Different Saved Model Formats
**What is up with all the different saved file formats?**
- https://www.tensorflow.org/mobile/prepare_models

* **graph_transforms:summarize_graph**
tool to print out information about the inputs and outputs it finds from the graph structure. 
```bash
export TF_HOME=$HOME/softwares/tensorflow
cd $TF_HOME
bazel run tensorflow/tools/graph_transforms:summarize_graph -- --in_graph="$HOME/Documents/ai-ml-dl/external/models/research/object_detection/ssd_mobilenet_v1_coco_2017_11_17/frozen_inference_graph.pb"
#
## output
Found 1 possible inputs: (name=image_tensor, type=uint8(4), shape=[?,?,?,3]) 
No variables spotted.
Found 4 possible outputs: (name=detection_boxes, op=Identity) (name=detection_scores, op=Identity) (name=num_detections, op=Identity) (name=detection_classes, op=Identity) 
Found 6818239 (6.82M) const parameters, 0 (0) variable parameters, and 1680 control_edges
Op types used: 1878 Const, 549 Gather, 452 Minimum, 360 Maximum, 305 Reshape, 197 Sub, 184 Cast, 183 Greater, 180 Split, 180 Where, 146 Add, 135 Mul, 128 StridedSlice, 124 Shape, 114 Pack, 108 ConcatV2, 97 Squeeze, 93 Slice, 93 Unpack, 90 ZerosLike, 90 NonMaxSuppressionV2, 35 Relu6, 34 Conv2D, 28 Switch, 27 Identity, 23 Enter, 13 Tile, 13 DepthwiseConv2dNative, 13 Merge, 13 RealDiv, 12 BiasAdd, 10 Range, 9 ExpandDims, 9 TensorArrayV3, 7 NextIteration, 5 Assert, 5 TensorArrayWriteV3, 5 TensorArraySizeV3, 5 Exit, 5 TensorArrayGatherV3, 4 TensorArrayScatterV3, 4 TensorArrayReadV3, 4 Fill, 3 Transpose, 3 Equal, 2 Exp, 2 GreaterEqual, 2 Less, 2 LoopCond, 1 TopKV2, 1 All, 1 Size, 1 Sigmoid, 1 ResizeBilinear, 1 Placeholder, 1 LogicalAnd
To use with tensorflow/tools/benchmark:benchmark_model try these arguments:
bazel run tensorflow/tools/benchmark:benchmark_model -- --graph=/home/bhaskar/Documents/ai-ml-dl/external/models/research/object_detection/ssd_mobilenet_v1_coco_2017_11_17/frozen_inference_graph.pb --show_flops --input_layer=image_tensor --input_layer_type=uint8 --input_layer_shape=-1,-1,-1,3 --output_layer=detection_boxes,detection_scores,num_detections,detection_classes
(reverse-i-search)`transform&apos;: bazel run tensorflow/tools/graph_^Cansforms:summarize_graph -- --in_graph=&quot;$HOME/Documents/ai-ml-dl/external/models/research/object_detection/ssd_mobilenet_v1_coco_2017_11_17/frozen_inference_graph.pb&quot;
```
- https://www.tensorflow.org/mobile/optimizing#binary_size
- https://www.tensorflow.org/mobile/optimizing#how_to_profile_your_model
* **graph_transforms:transform_graph**
```bash

bazel run tensorflow/tools/graph_transforms:transform_graph -- \
--in_graph=$HOME/Documents/ai-ml-dl/external/models/research/object_detection/ssd_mobilenet_v1_coco_2017_11_17/frozen_inference_graph.pb \
--out_graph=$HOME/Documents/ai-ml-dl/external/models/research/object_detection/ssd_mobilenet_v1_coco_2017_11_17/optimized_frozen_inference_graph.pb --inputs='image_tensor' --outputs='detection_boxes,detection_scores,num_detections,detection_classes' \
--transforms='strip_unused_nodes(type=float, shape="-1,-1,-1,3")
  fold_constants(ignore_errors=true)
  fold_batch_norms
  fold_old_batch_norms'
```
* **benchmark:benchmark_model**
```bash
export TF_HOME=$HOME/softwares/tensorflow
cd $TF_HOME
bazel run tensorflow/tools/benchmark:benchmark_model -- --graph=/home/bhaskar/Documents/ai-ml-dl/external/models/research/object_detection/ssd_mobilenet_v1_coco_2017_11_17/frozen_inference_graph.pb --show_flops --input_layer=image_tensor --input_layer_type=uint8 --input_layer_shape=-1,-1,-1,3 --output_layer=detection_boxes,detection_scores,num_detections,detection_classes
##
## Output
Init ops:
Input layers: [image_tensor]
Input shapes: [-1,-1,-1,3]
Input types: [uint8]
Output layers: [detection_boxes,detection_scores,num_detections,detection_classes]
Target layers: []
Num runs: [1000]
Inter-inference delay (seconds): [-1.0]
Inter-benchmark delay (seconds): [-1.0]
Num threads: [-1]
Benchmark name: []
Output prefix: []
Show sizes: [0]
Warmup runs: [1]
Loading TensorFlow.
```
**What are the minimum device requirements for TensorFlow?**
* how many FLOPs are required for a model, and then use that to make rule-of-thumb estimates of how fast they will run on different devices.
  -  For example, a modern smartphone might be able to run 10 GFLOPs per second, so the best you could hope for from a 5 GFLOP model is two frames per second, though you may do worse depending on what the exact computation patterns are.
  - For memory usage, you mostly need to make sure that the intermediate buffers that TensorFlow creates aren’t too large, which you can examine in the benchmark output too.

**Speed**
- One of the highest priorities of most model deployments is figuring out how to run the inference fast enough to give a good user experience.
*  estimate of how many operations are needed to run the graph.
  - this is done by rough estimate of this by using the benchmark_model tool.
* For an example, a high-end phone from 2016 might be able to do 20 billion FLOPs per second, so the best speed you could hope for from a model that requires 10 billion FLOPs is around 500ms. On a device like the Raspberry Pi 3 that can do about 5 billion FLOPs, you may only get one inference every two seconds.


## Convert Models from Caffe to Tensorflow
- https://github.com/ethereon/caffe-tensorflow

## Tensorflow Ecosystem
* https://www.tensorflow.org/ecosystem/


### Tensor Hub
* https://www.tensorflow.org/hub/
* https://medium.com/tensorflow/introducing-tensorflow-hub-a-library-for-reusable-machine-learning-modules-in-tensorflow-cdee41fa18f9
TensorFlow Hub is a library for the publication, discovery, and consumption of reusable parts of machine learning models. A module is a self-contained piece of a TensorFlow graph, along with its weights and assets, that can be reused across different tasks in a process known as transfer learning. Transfer learning can:
Train a model with a smaller dataset,
Improve generalization, and
Speed up training.


# Artifical Life
https://en.wikipedia.org/wiki/Artificial_life

## Zero Player Games
- https://en.wikipedia.org/wiki/Zero-player_game
- https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
- https://jakevdp.github.io/blog/2013/08/07/conways-game-of-life/
A zero-player game or no-player game is a game that has no sentient players.

In computer games, the term refers to programs that use artificial intelligence rather than human players.

In addition, some fighting and real-time strategy games can be put into zero-player mode where one AI plays against another AI.



**How to prevent tensorflow from allocating the totality of a GPU memory?**
* https://stackoverflow.com/questions/34199233/how-to-prevent-tensorflow-from-allocating-the-totality-of-a-gpu-memory
* You can set the fraction of GPU memory to be allocated when you construct a tf.Session by passing a tf.GPUOptions as part of the optional config argument:
  ```python
  # Assume that you have 12GB of GPU memory and want to allocate ~4GB:
  gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.333)

  sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))
  ```
* The per_process_gpu_memory_fraction acts as a hard upper bound on the amount of GPU memory that will be used by the process on each GPU on the same machine. Currently, this fraction is applied uniformly to all of the GPUs on the same machine; there is no way to set this on a per-GPU basis.

