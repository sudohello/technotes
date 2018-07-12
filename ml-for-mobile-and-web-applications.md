/*
Title: ML for Mobile and Web Applications
Decription: ML for Mobile and Web Applications
Author: Bhaskar Mangal
Date:
Tags: ML Production Pipeline, ML for Mobile and Web Applications
*/



## How to implement ML for Mobile and Web Apps
- https://www.analyticsvidhya.com/blog/2017/02/6-deep-learning-applications-beginner-python/
- https://us.pycon.org/2016/schedule/presentation/1614/
- https://www.credera.com/blog/credera-site/how-to-implement-machine-learning-in-your-apps/
- https://www.quora.com/How-can-I-implement-machine-learning-algorithms-in-a-web-application
- https://medium.com/@amirziai/a-flask-api-for-serving-scikit-learn-models-c8bcdaa41daa
- http://machinelearningmastery.com/deploy-machine-learning-model-to-production/


If the choice is PHP or Python for implementing ML algos, go with Python--no question.

Many core components of modern Machine Learning like logical regressions, linear regressions, nueral networks, etc... requires liner Algebra to implement efficiently (as far as I know)

PHP is not know for having a deverse and widely accepted range libraries for handling such math well, so implementing your algo in php is probably a poor choice.

Python has some great ones like numpy that are excellent for this purpose and a number of higher level libraries like tensorflow, theoano, keras, etc... to provide various levels ML abstraction.

### Embedding a Machine Learning Model into a Web Application
- https://cmry.github.io/notes/serialize
- https://github.com/cmry/cmry.github.io/blob/master/sources/serialize_sk.py
- http://www.stat.berkeley.edu/~ledell/docs/data_science_stack.html
- https://github.com/amirziai/sklearnflask/
- https://blog.algorithmia.com/cloud-hosted-deep-learning-models/

- https://www.quora.com/What-is-the-easiest-way-to-deploy-a-machine-learning-model-say-a-regression-for-production
Azure Machine Learning. It doesn’t take any parameters and there is no response. It simply imports some data from a database, runs a machine learning model in an R script and exports the results back to the database. That way, I can get a full set of predictions on-demand. This is a neat trick to sidestep the hassle of deploying models from R.


### Best Practices for ML Model deployment in Porduction
- online learning
- automated ML
- It is generally good practice to separate the models, that is, the hyperparameters and feature weights, from the rest of the workflow.
- There are model management frameworks based on both SQL databases and REST APIs.
- There are also things like the Openscoring library[2] , which uses a standard markup language known as PMML to store models.
- At the end of the day, there is no generic deployment scheme that fits every problem and every company. Deciding what practices to use, and implementing them, is at the heart of what machine learning engineering is all about. Data scientists tend to focus heavily on algorithms, but I think there are a lot of interesting problems to solve on the infrastructure and deployment side of machine learning as well
- https://www.quora.com/How-do-you-take-a-machine-learning-model-to-production
![Alt](images/ai-ml-dl/ml-production.webp)
- At a high level
	– depending on what volume of incoming data you need to process
	- on the size of the model
	- on how often it's updated
	- on what stack/tools you're using, etc
- you've got two choices:
	- (a) use the same tools you used to build the model to run it
	- or (b) run it using different tools than you used to build it.
- **If your ground truth is inaccurate, you’ve already set an upper limit to how good your precision and recall can be. If your ground truth is grossly inaccurate, that upper limit is pretty low.**
- So the best advice we can offer in this case is to log everything. Throw it all in HDFS, whether you need it now or not. In the future, you can always use this data to backfill new data stores if you find it useful. This can be invaluable in responding to a new attack vector.
- **HDFS** - The Hadoop Distributed File System ( HDFS ) is a distributed file system designed to run on commodity hardware.
- version your trained models
- in-house experiments framework that we use to deploy new models and test them against subsets of user traffic to see how they are doing as we ramp up a new model.


- https://www.quora.com/Do-most-machine-learning-algorithms-run-in-batch-or-do-they-run-every-time-they-get-a-new-bit-of-data/answer/H%C3%A5kon-Hapnes-Strand

**First of all, we need to distinguish on the type of learning. There are two ways of training machine learning models:**

* **Offline learning**: The model is trained once on historical data. After the model is deployed to production, it remains constant, although it’s possible to re-train the model if it becomes unstable, which will often happen.

* **Online learning**: The model is constantly being updated as new data arrives. This is especially useful for time series data, such as sensor data or financial instruments, because an online learning algorithm can pick up temporal effects. It’s also useful for websites with huge amounts of data, such as Google or Quora.

**Secondly, we need to distinguish on how the algorithm makes predictions:**
* **Batch predictions**: The algorithm generates a table of predictions based on its input data. This is often good enough for data that is not time-dependent, or when the output isn’t required to be totally fresh all the time.
* **On-demand predictions**: Predictions are being made in real-time using the input data that is available at the time of the request, which typically comes in the form of a REST call.


**Forecast**
- The most common way to practice machine learning is offline batch predictions. This is how Kaggle competitions are run, for instance. You get your input data as a file, train a model, and make a forecast. This is more like an experiment than actually putting something into production, although this paradigm is also common in business intelligence.

**Web service**
- A more common way to embed machine learning into applications, is through a web service. Again, the model is trained on historical data, but it uses fresh data to make predictions. It seems strange to call a web service model offline, but it’s only the actual training that’s performed offline. The service always uses the latest data available to make predictions, but the model remains constant.

**Automated machine learning**
- A very hot topic these days is automated machine learning. That includes automating the entire training, cross-validation and model selection process. By doing that, you can have an algorithm that retrains itself and makes repeated batch predictions in intervals, using the latest data available to both train the model and generate predictions. This methodology can’t be used in real-time, though, because it takes time to train the model(s). It’s probably the least utilized method out of the four.

**Online learning**
- This is the most dynamic way to productionalize machine learning. The learning algorithm is hooked to a (big) data stream and continuously trains itself as new data comes in. A constantly updated model is immediately accessible as a web service. Technically, this is the most challenging setup to achieve, and it has mostly been used by the big players so far.

- https://www.quora.com/What-is-the-easiest-way-to-deploy-a-machine-learning-model-say-a-regression-for-production

**How the deployment is done in self-driving cars, robots or drones?**
> by Marek Bardoński, Senior Deep Learning Research Engineer at NVIDIA
I’ll describe it on a Tesla’s car example - other objects have a similar process.

After the company have a model designed and trained in one of the popular deep learning frameworks, it’s exported to the NVIDIA’s inference tool - TensorRT - and compiled as a library for inference. Then, the computer in the car equipped with one or more GPUs (eg. DrivePX2) have a control program calling this library each time the inference is required.

It’s reading input from the camera, and calling TensorRT via API to provide inference - recognizing what’s on the image or outputting the image segments. Everything is done as C++ API calls and often it’s on a real-time operating system like QNX.

https://en.wikipedia.org/wiki/QNX

Another example was my first attempt at using deep learning that actually did not reach into production (yet, it will in time). I managed to achieve excellent classification performance, far exceeding everything available at the time. However like most early adopters, we did not have the available GPU resources to use in production and using the CPU did not meet the runtime requirements. We resorted to dumping the deep algorithm and using the classics until we got the hardware infrastructure.

So you see, my answer is look at it like any project and ballance the complexities of schedule available resources and meeting user requirements.

- http://machinelearningmastery.com/building-a-production-machine-learning-infrastructure/

In industry, faster is always better and slower has to be justified, meaning accuracy can often take a back seat.
Experiments drive understanding.

**AirBnB Casse Study**
- https://medium.com/airbnb-engineering/architecting-a-machine-learning-system-for-risk-941abbba5a60
We can get around the drawbacks of R while maintaining its advantages by building a pipeline based on Python and scikit-learn. Scikit-learn is a Python package that supports many standard machine learning models, and includes helpful utilities for validating models and performing feature transformations. We find that Python is a more natural language than R for ad-hoc data manipulation and feature extraction.
Deployment and testing can also be performed automatically in Python by using its standard network libraries to interface with Openscoring. Standard model performance tests (precision recall, ROC curves, etc.) are carried out using sklearn’s built-in capabilities. Sklearn does not support PMML export out of the box, so have written an in-house exporter for particular sklearn classifiers. When the PMML file is uploaded to Openscoring, it is automatically tested for correspondence with the scikit-learn model it represents. Because feature-transformation, model building, model validation, deployment and testing are all carried out in a single script, a data scientist or engineer is able to quickly iterate on a model based on new features or more recent data, and then rapidly deploy the new model into production.
- Our process was very successful for some models, but for others we encountered poor precision-recall. Initially we considered whether we were experiencing a bias or a variance problem, and tried using more data and more features. However, after finding no improvement, we started digging deeper into the data, and found that the problem was that our ground truth was not accurate.
- A unique challenge of working at a hyper-growth company is that landscape fundamentally changes year-over-year, and pipelines need to adjust to account for this. As our data and logging pipelines improve, investing in improved learning algorithms will become more worthwhile, and we will likely shift to testing new algorithms, incorporating online learning, and expanding on our model building framework to support larger data sets
- some of the most important opportunities to improve our models are based on insights into our unique data, feature selection, and other aspects our risk systems that we are not able to share publicly.

**[Uber: michelangelo ML platform](https://eng.uber.com/michelangelo/)**
> Must Read

We designed Michelangelo specifically to provide scalable, reliable, reproducible, easy-to-use, and automated tools to address the following six-step workflow:  
* Manage data
* Train models
* Evaluate models
  - Keeping track of these trained models (e.g. who trained them and when, on what data set, with which hyper-parameters, etc.), evaluating them, and comparing them to each other are typically big challenges when dealing with so many models and present opportunities for the platform to add a lot of value.
  - The information is easily available to the user through a web UI and programmatically through an API, both for inspecting the details of an individual model and for comparing one or more models with each other.
  - **For every model that is trained in Michelangelo, we store a versioned object in our model repository in Cassandra that contains a record of:**
    - Who trained the model
    - Start and end time of the training job
    - Full model configuration (features used, hyper-parameter values, etc.)
    - Reference to training and test data sets
    - Distribution and relative importance of each feature
    - Model accuracy metrics
    - Standard charts and graphs for each model type (e.g. ROC curve, PR curve, and confusion matrix for a binary classifier)
    - Full learned parameters of the model
    - Summary statistics for model visualization
* Deploy models
  - end-to-end support for managing model deployment via the UI or API and three modes in which a model can be deployed:
* Make predictions
* Monitor predictions

## Online Machine Learning
- https://en.wikipedia.org/wiki/Online_machine_learning

## ML APIs
- https://www.kdnuggets.com/2015/12/machine-learning-data-science-apis.html
- https://www.credera.com/blog/credera-site/how-to-implement-machine-learning-in-your-apps/
- https://www.quora.com/How-can-I-implement-machine-learning-algorithms-in-a-web-application

## ML Courses
- https://medium.freecodecamp.org/every-single-machine-learning-course-on-the-internet-ranked-by-your-reviews-3c4a7b8026c0


# End-to-End ML Application
**References:**
> TBD: relative links not working in pico cms
- [python-in-nutshell](python-in-nutshell.md)
- [data-visualization-in-python](data-visualization-in-python.md)

## Web-frameworks available

* **Python**
  - Flask
  - Django
  - Falcon
  - Hug and many more
* **R**
  - plumber


## HTTP server
http://gunicorn.org/

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resources, and fairly speedy.
```bash
sudo pip install gunicorn
```

## Example: Hello world
- https://groups.google.com/forum/#!topic/comp.lang.python/tEBMAJ41Wag
```python
#!/usr/bin/env python
def main():
  print "Content-type: text/html"
  print ""
  print "Hello world!"
#
if __name__ == "__main__":
  main()
```
Start Http Server
```
gunicorn --bind 0.0.0.0:8000 hello-world:app
curl http://localhost:8000/hello-world.py
```

## Python with Apache
- https://python-forum.io/Thread-Run-Python-CGI-from-Apache?pid=1675
- https://www.digitalocean.com/community/tutorials/how-to-set-up-an-apache-mysql-and-python-lamp-server-without-frameworks-on-ubuntu-14-04

```bash
# disable multithreading processes
#
sudo a2dismod mpm_event
#
# give Apache explicit permission to run scripts
#
sudo a2enmod mpm_prefork cgi
#
# modify the actual Apache configuration, to explicitly declare Python files as runnable file and allow such executables
#
sudo vi /etc/apache2/sites-enabled/000-default.conf
```

Add the following right after the first line, which reads <VirtualHost *:80\>.
```bash
#
sudo a2enmod cgi
#
sudo vi sudo vi /etc/apache2/mods-available/php7.0.conf
#
<Directory /home/*/public_html/*/cgi-bin>
    Options +ExecCGI
    SetHandler cgi-script
    AddHandler cgi-script .py 
</Directory>
#
```

## Flask
- https://www.tutorialspoint.com/flask/
- https://github.com/jay3dec/PythonFlaskMySQLApp---Part-1
- https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972

### Flask with Apache
- https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
- http://csparpa.github.io/blog/2013/03/how-to-deploy-flask-applications-to-apache-webserver.html

### WSGI: modwsgi
- https://code.google.com/archive/p/modwsgi/wikis/QuickConfigurationGuide.wiki

**WSGI Application Script File**
WSGI is a specification of a generic API for mapping between an underlying web server and a Python web application. WSGI itself is described by Python PEP 0333. The purpose of the WSGI specification is to provide a common mechanism for hosting a Python web application on a range of different web servers supporting the Python programming language.

**Mounting The WSGI Application**
There are a number of ways that a WSGI application hosted by mod_wsgi can be mounted against a specific URL. These methods are similar to how one would configure traditional CGI applications.

Require **WSGI module**
```bash
sudo apt-get install libapache2-mod-wsgi python-dev
#
sudo a2enmod wsgi
```
-http://modwsgi.readthedocs.io/en/develop/configuration-directives/WSGIScriptAlias.html
```bash
<IfModule mod_userdir.c>
    <Directory /home/*/public_html>
        #php_admin_flag engine Off
    </Directory>
    <Directory /home/*/public_html/*/cgi-bin>
        Options +ExecCGI
        SetHandler cgi-script
        AddHandler cgi-script .py 
    </Directory>
    <Directory /home/*/public_html/*/wsgi-bin>
        Options +ExecCGI
        SetHandler wsgi-script
        AddHandler wsgi-script .wsgi
    </Directory>
</IfModule>
```
**Getting Started:mod_wsgi**
http://modwsgi.readthedocs.io/en/develop/getting-started.html

**Sample Application with Flask**
http://www.bogotobogo.com/python/Flask/Python_Flask_HelloWorld_App_with_Apache_WSGI_Ubuntu14.php

## Errors

**Template Not Found**
- https://stackoverflow.com/questions/23435150/python-flask-render-template-not-found
- https://stackoverflow.com/questions/23846927/flask-unable-to-find-templates

**Errors/Warnings in setup/execution**
- The installed version of numexpr 2.4.3 is not supported in pandas and will be not be used. The minimum supported version is 2.4.6
- UserWarning: Trying to unpickle estimator DecisionTreeClassifier from version pre-0.18 when using version 0.18.1. This might lead to breaking code or invalid results. Use at your own risk.

## Tutorials
- http://flask.pocoo.org/docs/0.12/quickstart/#rendering-templates

## WebApps with Flask
- https://www.fullstackpython.com/web-analytics.html
- http://blog.yhat.com/posts/pandas-google-analytics.html

## Serialization

### pickle
- It's similar to creating .rda files in R Programming.

### dill
- https://pypi.python.org/pypi/dill
dill extends python’s pickle module for serializing and de-serializing python objects to the majority of the built-in python types. Serialization is the process of converting an object to a byte stream, and the inverse of which is converting a byte stream back to on python object hierarchy.

**Install: dill**
```bash
sudo pip install dill
```

### h5py
- h5py could also be an alternative.

## Creating ML API using Flask
- https://github.com/pratos/flask_api
- https://www.analyticsvidhya.com/blog/2017/09/machine-learning-models-as-apis-using-flask/
- [Machine Learning models as APIs using Flask](https://render.githubusercontent.com/view/ipynb?commit=dac6eb737b58b73f9b9b323a9a39c0d1fe8cbfee&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f707261746f732f666c61736b5f6170692f646163366562373337623538623733663962396233323361396133396330643166653863626665652f6e6f7465626f6f6b732f4d4c2532304d6f64656c732532306173253230415049732532307573696e67253230466c61736b2e6970796e62&nwo=pratos%2Fflask_api&path=notebooks%2FML+Models+as+APIs+using+Flask.ipynb&repository_id=103313016&repository_type=Repository#no1)

## Paid Courses
https://www.udemy.com/machine-learning-course-with-python/?couponCode=CODESTARS&siteID=rjqiUzH_Hec-2IXJ8GHGJe3fyubxBjnbnw&LSNPUBID=rjqiUzH%2FHec

## Example Apps
* https://github.com/delsner/flask-angular-data-science


## References
https://www.superdatascience.com/machine-learning/
https://www.freetutorials.us/

## Object Detections
https://www.pyimagesearch.com/2018/05/14/a-gentle-guide-to-deep-learning-object-detection/
https://www.pyimagesearch.com/2017/09/11/object-detection-with-deep-learning-and-opencv/
https://www.pyimagesearch.com/2017/09/18/real-time-object-detection-with-deep-learning-and-opencv/
https://www.pyimagesearch.com/deep-learning-computer-vision-python-book/

## Map Views
https://elections.indianexpress.com/karnataka-elections-result-overview/


## Deep Learning

### What framework(s) are you currently using to train deep learning models?
**caffe**
http://caffe.berkeleyvision.org/
- Caffe (with DIGITS interface) 

**chainer**
https://chainer.org/

**Deeplearning4j: Open-source, Distributed Deep Learning for the JVM**
https://deeplearning4j.org/
Eclipse Deeplearning4j is a deep learning programming library written for Java and the Java virtual machine and a computing framework with wide support for deep learning algorithms.

**paddlepaddle**
http://paddlepaddle.org/

**MXNet**
https://mxnet.apache.org/
Apache MXNet is a modern open-source deep learning framework used to train, and deploy deep neural networks

**MatConvNet**
www.vlfeat.org/matconvnet/
MatConvNet is a MATLAB toolbox implementing Convolutional Neural Networks (CNNs) for computer vision applications

**PyTorch**
https://pytorch.org/
PyTorch is an open source machine learning library for Python, based on Torch, used for applications such as natural language processing.

**Theano**
Theano is a numerical computation library for Python. In Theano, computations are expressed using a NumPy-esque syntax and compiled to run efficiently on either CPU or GPU architectures.

**keras**
https://keras.io/
Keras is an open source neural network library written in Python. It is capable of running on top of TensorFlow, Microsoft Cognitive Toolkit, Theano, or MXNet.


**TensorRT 4.0**
NVIDIA TensorRT is a high-performance deep learning inference optimizer and runtime for deep learning applications.

TensorRT works across all NVIDIA GPUs using the CUDA platform. The following files are for use for Linux servers and workstations running NVIDIA Quadro, GeForce, and Tesla GPUs. NVIDIA recommends Tesla V100, P100, P4, and P40 GPUs for production deployment.

* Support for Text Translation and Natural Language Processing use cases (OpenNMT, GNMT)
* Support for Speech use cases (Deep Speech 2)

**digits**
https://developer.nvidia.com/digits
The NVIDIA Deep Learning GPU Training System (DIGITS) puts the power of deep learning into the hands of engineers and data scientists. DIGITS can be used to rapidly train the highly accurate deep neural network (DNNs) for image classification, segmentation and object detection tasks.

DIGITS simplifies common deep learning tasks such as managing data, designing and training neural networks on multi-GPU systems, monitoring performance in real time with advanced visualizations, and selecting the best performing model from the results browser for deployment. DIGITS is completely interactive so that data scientists can focus on designing and training networks rather than programming and debugging.


### What network architectures most closely resemble ones you use now?
* Alexnet
* GoogLeNet/Inception (v1, v2, v3, v4, v5, other variations)
* Resnet (18/50/101/152, other variations)
* VGG (16, 19, other variations)
* BigLSTM, OpenNMT
* DeepSpeach
* Faster RCNN variations
* YOLO/SSD variations
* SqueezeNet
* GAN


### Which of the following best describes your application area (choose one)? *
* Image and Video applications
* Signal and Speech applications
* Text and Document applications
* Multimodal (combination of the above)

### Which of the following would you say is the main bottleneck for deployment? *
* Throughput
* Latency
* Ease of deployment
* Ease of updating model
* Maintainability

### Nvidia Education

https://www.nvidia.com/en-us/deep-learning-ai/education/


deep learning courses
 - you’ll learn how to train, optimize, and deploy neural networks
accelerated computing courses,
  - you’ll learn how to assess, parallelize, optimize, and deploy GPU-accelerated computing applications

INSTRUCTOR-LED WORKSHOPS
ONLINE COURSES
ONLINE MINI COURSES


* Explore the fundamentals of deep learning for Computer Vision.
  - Explore the fundamentals of deep learning by training neural networks and using results to improve performance and capabilities.
  - Learn how to start solving problems with deep learning.
  - Learn how to train a deep neural network to recognize handwritten digits.
  - Explore how deep learning works and how it will change the future of computing.
  - Learn how to detect objects using computer vision and deep learning by identifying a purpose-built network and using end-to-end labeled data.
  - Implement common deep learning workflows such as Image Classification and Object Detection.
  - Experiment with data, training parameters, network structure, and other strategies to increase performance and capability.
  - Deploy your networks to start solving real-world problems
* Explore Fundamentals of Deep Learning for Multiple Data Types
* Explore how convolutional and recurrent neural networks can be combined to generate effective descriptions of content within images and video clips. 
* Learn to deploy deep learning to applications that recognize and detect images in real time.
* Learn how to design, train, and deploy deep neural networks for autonomous vehicles.
* Learn how to train a generative adversarial network (GAN) to generate images, explore techniques to make video style transfer, and train a denoiser for rendered images.
* Learn how to combine computer vision and natural language processing to describe scenes using deep learning.
* Learn how to make predictions from structured data.
* Learn how to classify both image and image-like data using deep learning by converting radio frequency (RF) signals into images to detect a weak signal corrupted by noise.


1. Fundamentals of Deep Learning for Computer Vision
  - Implement common deep learning workflows such as Image Classification and Object Detection.
  - Experiment with data, training parameters, network structure, and other strategies to increase performance and capability.
  - Deploy your networks to start solving real-world problems
  - On completion of this course, you will be able to start solving your own problems with deep learning
  * Learning Objectives: What You'll Learn
    - Identify the ingredients required to start a Deep Learning project.
    - Train a deep neural network to correctly classify images it has never seen before.
    - Deploy deep neural networks into applications.
    - Identify techniques for improving the performance of deep learning applications.
    - Assess the types of problems that are candidates for deep learning.
    - Modify neural networks to change their behavior.
2. Learn how to train a network using TensorFlow and the MSCOCO dataset to generate captions from images and video by:
  - Implementing deep learning workflows like image segmentation and text generation
  - Comparing and contrasting data types, workflows, and frameworks
  - Combining computer vision and natural language processing
  * Upon completion, you’ll be able to solve deep learning problems that require multiple types of data inputs
3. Deep Learning for Digital Content Creation Using GANs and Autoencoders
Learn techniques for designing, training, and deploying neural networks for digital content creation.
  - Train a Generative Adversarial Network (GAN) to generate images
  - Explore the architectural innovations and training techniques used to make arbitrary video style transfer
  - Train your own denoiser for rendered images
  - Upon completion of this course, you’ll be able to start creating digital assets using deep learning approaches
4. Deep Learning for Finance Trading Strategy
Linear techniques like principal component analysis (PCA) are the workhorses of creating ‘eigenportfolios’ for use in statistical arbitrage strategies. Other techniques using time series financial data are also prevalent. But now, trading strategies can be advanced with the power of deep neural networks.
  - Prepare time series data and test network performance using training and test datasets
  - Structure and train a LSTM network to accept vector inputs and make predictions
  - Use the Autoencoder as anomaly detector to create an arbitrage strategy
  - Upon completion, you’ll be able to use time series financial data to make predictions and exploit arbitrage using neural networks.



* AUTONOMOUS VEHICLES
* GAME DEVELOPMENT AND DIGITAL CONTENT
  - Deep Learning for Digital Content Creation Using GANs and Autoencoders Explore the latest techniques for designing, training, and deploying neural networks for digital content creation.


## Labs
https://nvidia.qwiklab.com/focuses/40?parent=catalog

* Free datasets are available from places like Kaggle.com and UCI. 
  - https://www.kaggle.com/datasets
  - https://archive.ics.uci.edu/ml/datasets.html
* Crowdsourced datasets are built through creative approaches - e.g. Facebook asking users to "tag" friends in their photos to create labeled facial recognition datasets
* More complex datasets are generated manually by experts - e.g. asking radiologists to label specific parts of the heart.

**Training vs. programming**
- The fundamental difference between artificial intelligence (AI) and traditional programing is that AI learns while traditional algorithms are programmed. 
- Artificial intelligence takes a different approach. Instead of providing instructions, we provide examples.
- We could show our robot thousands of labeled images of bread and thousands of labeled images of other objects and ask our robot to learn the difference. Our robot could then build its own program to identify new groups of pixels (images) as bread.

The "deep" in deep learning refers to many layers of artificial neurons, each of which contribute to the network's performance.
Processing huge datasets through deep networks is made possible by parallel processing, a task tailor made for the GPU.


**how do we expose artificial neural networks to data?**
**how to load data into a deep neural network to create a trained model that is capable of solving problems with what it learned, not what a programmer told it to do.**


Since a computer "sees" images as collections of pixel values, it can't do anything with visual data unless it learns what those pixels represent.


What if we could easily convert handwritten digits to the digital numbers they represent?

We could help the post office sort piles of mail by post code. This is the problem that motivated Yann LeCun. He and his team put together the dataset and neural network that we'll use today and painstakingly pioneered much of what we know now about deep learning.
We could help teachers by automatically grading math homework. This the problem that motivated the team at answer.ky, who used Yann's work to easily solve a real world problem using a workflow like what we'll work through now.
We could solve countless other challenges. What will you build?


http://yann.lecun.com/
http://answer.ky/

We're going to train a deep neural network to recognize handwritten digits 0-9. This challenge is called "image classification," where our network will be able to decide which image belongs to which class, or group.


It's important to note that this workflow is common to most image classification tasks, and is a great entry point to learning how to solve problems with Deep Learning.


Inside the folder train_small there were 10 subfolders, one for each class (0, 1, 2, 3, ..., 9). All of the handwritten training images of '0's are in the '0' folder, '1's are in the '1' folder, etc.
- This data is labeled. Each image in the dataset is paired with a label that informs the computer what number the image represents, 0-9. We're basically providing a question with its answer, or, as our network will see it, a desired output with each input. These are the "examples" that our network will learn from.
- Each image is simply a digit on a plain background. Image classification is the task of identifying the predominant object in an image. For a first attempt, we're using images that only contain one object. We'll build skills to deal with messier data in subsequent labs.
- http://yann.lecun.com/exdb/mnist/
- This data comes from the MNIST dataset which was created by Yann LeCun. It's largely considered the "Hello World," or introduction, to deep learning.

Also like the brain, these "networks" only become capable of solving problems with experience, in this case, interacting with data. 

Throughout this lab, we'll refer to "networks" as untrained artificial neural networks and "models" as what networks become once they are trained (through exposure to data).

For image classification (and some other tasks), DIGITS comes pre-loaded with award-winning networks.

However, to start, weighing the merits of different networks would be like arguing about the performance of different cars before driving for the first time. 

Building a network from scratch would be like building your own car. Let's drive first. We'll get there.

Creating a new model in DIGITS is a lot like creating a new dataset.


- Classification
- Segmentation
- Object Detection
- Processing
- Other

**epoch**
We need to tell the network how long we want it to train. An epoch is one trip through the entire training dataset. Set the number of Training Epochs to 5 to give our network enough time to learn something, but not take all day. This is a great setting to experiment with.

We need to define which network will learn from our data. Since we stuck with default settings in creating our dataset, our database is full of 256x256 color images. Select the network AlexNet, if only because it expects 256x256 color images.

* LeNet  Original paper [1998] 28x28 (gray)
  - http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf
* AlexNet  Original paper [2012] 256x256 
  - http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional
* GoogLeNet  Original paper [2014] 256x256
  - http://arxiv.org/abs/1409.4842

We'll dig into this graph as a tool for improvement, but the bottom line is that after 5 minutes of training, we have built a model that can map images of handwritten digits to the number they represent with an accuracy of about 87%!


Inference
Now that our neural network has learned something, inference is the process of making decisions based on what was learned. The power of our trained model is that it can now classify unlabeled images.

test our trained model. 
- you can test a single image or a list of images.

It worked! (Try again if it didn't). You took an untrained neural network, exposed it to thousands of labeled images, and it now has the ability to accurately predict the class of unlabeled images. Congratulations!

Note that that same workflow would work with almost any image classification task. You could train AlexNet to classify images of dogs from images of cats, images of you from images of me, etc. If you have extra time at the end of this lab, theres another dataset with 101 different classes of images where you can experiment.


* https://jorditorres.org/research-teaching/tensorflow/first-contact-with-tensorflow-book/first-contact-with-tensorflow/
* http://deeplearning.net/tutorial/
* http://www.deeplearningitalia.com/wp-content/uploads/2017/12/Dropbox_Chollet.pdf

# Deep Learning Starting
**Provide APIs in Computer Vision using Deep Learning for Geospatial Industry**
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

## ML/DL Laptop
* Dell Latitude 5590 CTO
- i7 8th generation, 6 cores, 8/16 GB RAM, Nvidia GTX 1050 Ti 4GB


https://vimeo.com/245073446
https://oslandia.com/en/2016/03/16/osgeo-cs-2016-report-point-clouds/
https://oslandia.com/en/2016/11/08/py3dtiles/