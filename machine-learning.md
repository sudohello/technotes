/*
Title: ML - Machine Learning
Decription: Machine Learning
Author: Bhaskar Mangal
Date:
Last Updates: 06th Jun 2018
Tags: Machine Leaning, ML, Machine Learning in Python
*/

# Machine Learning

## scikit-learn: machine learning in Python: `sklearn` python package
> scikit-learn: machine learning in Python

- Scikit-learn also implements a large variety of different performance metrics that are available via the metrics module. For example, we can calculate the classification accuracy of the perceptron on the test set
```python
from sklearn.cross_validation import train_test_split # deprecated and use model_selection module instead
from sklearn.model_selection import train_test_split
```
```python
from sklearn.metrics import accuracy_score
print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))
#
# Here, y_test are the true class labels and y_pred are the class labels that we predicted previously
```

### References
* ScipyLectures-simple.pdf
* [Check the Refresher in Python and related packages](https://github.com/mangalbhaskar/pragmatic-approach-4-learning-data-visualisation/blob/master/chapter-1/python-in-nutshell.md)
* [islr-book-notes (Introduction to Statistical Learning Using R)](https://github.com/mangalbhaskar/technotes/blob/master/islr-book-notes.md)

### Documentation
* http://scikit-learn.org

### Tutorials
* https://www.youtube.com/watch?v=r4bRUvvlaBw
* https://github.com/jakevdp/sklearn_tutorial

### What is machine learning?
- Machine Learning is about building programs with tunable parameters that are adjusted automatically so as to improve their behavior by adapting to previously seen data
- Machine Learning can be considered a subfield of Artificial Intelligence since those algorithms can be seen as building blocks to make computers learn to behave more intelligently by somehow generalizing rather that just storing and retrieving data items like a database system would do

**Two very simple machine learning tasks:**
1. First is a **classification** task
	- A classification algorithm may be used to draw a dividing boundary between the two clusters of points
2. Second is **regression** task
	- A simple best-fit line to a set of data
	- This is an example of fitting a model to data, but our focus here is that the model can make generalizations about new data

**data matrix**
- Machine learning algorithms implemented in scikit-learn expect data to be stored in a two-dimensional array or matrix
- arrays can be either numpy arrays, or in some cases `scipy.sparse` matrices
- The size of the array is expected to be `[n_samples, n_features]`
	* **n_samples**: The number of samples
		- each sample is an item to process (e.g. classify)
		- A sample can be a document
		- a picture
		- a sound
		- a video
		- an astronomical object
		- a row in database or CSV file
		- or whatever you can describe with a fixed set of quantitative traits
	* **n_features**: The number of features or distinct traits that can be used to describe each item in a quantitative manner
		- Features are generally real-valued
		- but may be boolean or discrete-valued in some cases
		- The number of features must be fixed in advance
		- there must be a fixed number of features for each sample
		- feature number `i` must be a similar kind of quantity for each sample
		- However it can be very high dimensional (e.g. millions of features) with most of them being zeros for a given sample. This is a case where scipy.sparse matrices can be useful, in that they are much more memory-efficient than numpy arrays
- `scikit-learn` is imported as `sklearn`
- http://www.scipy-lectures.org/packages/scikit-learn/auto_examples/plot_iris_scatter.html
```python
from sklearn.datasets import load_iris
iris = load_iris()
iris.feature_names
n_samples, n_features = iris.data.shape
#
# The information about the class of each sample is stored in the target attribute of the dataset:
iris.target
#
# The names of the classes are stored in the last attribute, namely target_names
iris.target_names
#
# This data is four-dimensional, but we can visualize two of the dimensions at a time using a scatter plot:
```
* scikit-learn already support multiclass classification by default via the One-vs.-Rest (OvR) method
* The Iris dataset contains the measurements of 150 iris flowers from three different species: Setosa, Versicolor, and Virginica
* Iris dataset, consisting of 150 samples and 4 features, can then be written as a 150 × 4 matrix $x \epsilon  R^{150*4}$
```python
from sklearn import datasets
datasets.load_iris()
#
from sklearn.model_selection import train_test_split
train_test_split(X, y, test_size=0.3, random_state=0)
#
from sklearn.preprocessing import StandardScaler
StandardScaler()
#
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)
```


## Basic principles of machine learning with scikit-learn
- Every algorithm is exposed in scikit-learn via an **Estimator** object
- linear regression is: `sklearn.linear_model.LinearRegression`
- Estimator parameters: All the parameters of an estimator can be set when it is instantiated
```python
from sklearn.linear_model.LinearRegression import LinearRegression
import numpy as np
model = LinearRegression(normalize=True)
# LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=True)
x,y = np.array([0,1,2]), np.array([0,1,2])
X = x[:,np.newaxis]
model.fit(X,y)
model.coef_
```
- Fitting on data
- Estimated parameters:
	* When data is fitted with an estimator, parameters are estimated from the data at hand
	* All the estimated parameters are attributes of the estimator object ending by an underscore

## **Supervised Learning: Classification and regression**
- In Supervised Learning, we have a **dataset consisting of both features and labels**
- The **task is to construct an estimator** which is able to **predict the label of an object given the set of features**
- There is one or more unknown quantities associated with the object which needs to be determined from other observed quantities
- Supervised learning is further broken down into two categories:
	* **classification**
		- In classification, the **label is discrete**
		- K nearest neighbors (kNN) is one of the simplest learning strategies
			* given a new, unknown observation, look up in your reference database which ones have the closest features and assign the predominant class
```python
from sklearn.linear_model.LinearRegression import LinearRegression
model = LinearRegression(normalize=True)
model.fit
model.predict
#
from sklearn import neighbors
knn = neighbors.KNeighborsClassifier(n_neoghbors=1)
knn.fit
knn.predict
```
	* **regression**
		- In regression, the **label is continuous**

- **Scikit-learn strives to have a uniform interface across all methods.**
	- Given a scikit-learn estimator object named model , the following methods are available:
		* `model.fit`: fit training data
		* **For supervised learning** applications, this accepts two arguments: the **data** `X` and the **labels** `y`
		* **For unsupervised learning** applications, this accepts only a single argument, the **data** `X`
	```python
	model.fit(X,y)
	model.fit(X)
	```
	- In supervised estimators:
		* `model.predict`
			- given a trained model, predict the label of a new set of data
			- This method accepts one argument, the new data and returns the learned label for each object in the array
		* `model.predict_proba`
			- For classification problems, some estimators also provide this method
			- returns the probability that a new observation has each categorical label
		* `model.score`
			- For classification or regression problems
			- Scores are between 0 and 1
			- with a larger score indicating a better fit
	- In unsupervised estimators:
		* `model.transform`
			- given an unsupervised model, transform new data into the new basis
		* `model.fit_transform`
			- more efficiently performs a fit and a transform on the same input data

**Regularization: what it is and why it is necessary**
The core idea behind regularization is that we are going to **prefer models that are simpler**, for a certain definition of "simpler", even if they lead to more errors on the train set
* Train errors Suppose you are using a 1-nearest neighbor estimator. How many errors do you expect on your train set?
	- Train set error is not a good measurement of prediction performance. You need to leave out a test set
	- In general, we should accept errors on the train set
* Regularization is ubiquitous in machine learning
* Most scikit-learn estimators have a parameter to tune the amount of regularization
	- For instance, with k-NN, it is ‘k’, the number of nearest neighbors used to make the decision
	- k=1 amounts to no regularization: 0 error on the training set, whereas large k will push toward smoother decision boundaries in the feature space
* For classification models (linear separation, non-linear separation), the decision boundary, that separates the class expresses the complexity of the model. For instance, a linear model, that makes a decision based on a linear combination of features, is more complex than a non-linear one.

## **Estimators: Classifiers and Regressors**
**Properties**
- The classifier or regressor essentially “memorizes” all the samples it has already seen
- To really test how well this algorithm does, we need to try some samples it hasn’t yet seen

### **Classifier**
**Different classifiers**
* K-nearest neighbors: `from sklearn.neighbors import KNeighborsClassifier`
	- The K-neighbors classifier is an instance-based classifier
	- The K-neighbors classifier predicts the label of an unknown point based on the labels of the K nearest points in the parameter space
* Gaussian Naives: `from sklearn.naive_bayes import GaussianNB`
* support vectors machines: `from sklearn.svm import LinearSVC`

**hyperparameters** are the parameters set when you instantiate the classifier: for example, the n_neighbors in `clf = KNeighborsClassifier(n_neighbors=1)`
* For KNeighborsClassifier we use n_neighbors between 1 and 10
* For LinearSVC , use loss='l2' and loss='l1'
* Note that GaussianNB does not have any adjustable hyperparameters

* With the default hyper-parameters for each estimator, which gives the best f1 score on the validation set?
* For each classifier, which value for the hyperparameters gives the best results for the digits data?

### **Regressor**
**Properties**

**Different regressors**
* LinearRegression is: `sklearn.linear_model.LinearRegression`
* GradientBoostingRegressor : `from sklearn.ensemble import GradientBoostingRegressor`
* DecisionTreeRegressor: `from sklearn.tree import DecisionTreeRegressor`
	- instance-based model named “decision tree”


## **FAQs**
* **What is instance-based model named “decision tree”?**
	- https://en.wikipedia.org/wiki/Instance-based_learning
	- In machine learning, instance-based learning (sometimes called memory-based learning[1]) is a family of learning algorithms that, instead of performing explicit generalization, compares new problem instances with instances seen in training, which have been stored in memory.
	- Examples of instance-based learning algorithm are the k-nearest neighbor algorithm, kernel machines and RBF networks.[3]:ch. 8 These store (a subset of) their training set; when predicting a value/class for a new instance, they compute distances or similarities between this instance and the training instances to make a decision.
	- To battle the memory complexity of storing all training instances, as well as the risk of overfitting to noise in the training set, instance reduction algorithms have been proposed


* [how-to-list-all-attributes-of-sklearn-datasets-object](https://stackoverflow.com/questions/35105474/how-to-list-all-attributes-of-sklearn-datasets-object)
```python
from sklearn.datasets load_iris, load_digits
iris = load_iris()
iris.keys()
## ['target_names', 'data', 'target', 'DESCR', 'feature_names']
#
digits = load_digits()
digits.keys()
## ['images', 'data', 'target_names', 'DESCR', 'target']
```

## Case Studies

### 1. [Netflix_Prize](https://en.wikipedia.org/wiki/Netflix_Prize)

### 2. Iris: What kind of iris has 3cm x 5cm sepal and 4cm x 2cm petal?
```python
from sklearn.datasets load_iris
iris = load_iris()
iris.feature_names
n_samples, n_features = iris.data.shape
iris.target
iris.target_names
#
from sklearn import neighbors
X,y = iris.data, iris.target
knn = neighbors.KNeighborsClassifier(n_neoghbors=1)
knn.fit(X,y)
iris.target_names[knn.predict([[3,5,4,2]])]
#
# KNN - plot the decision boundaries for each class
```

### 3. [Supervised Learning: Classification of Handwritten Digits](http://www.scipy-lectures.org/packages/scikit-learn/auto_examples/plot_digits_simple_classif.html)

* Plot the first few samples of the digits dataset and a 2D representation built using PCA, then do a simple classification
* **Plot the data: images of digits**
```python
from sklearn.datasets import load_digits
digits = load_digits()
#
from matplotlib import pyplot as plt
fig = plt.figure(figsize=(6, 6))  # figure size in inches
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
#
for i in range(64):
  ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
  ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
  # label the image with the target value
  ax.text(0, 7, str(digits.target[i]))
plt.imshow()
```
*  **Visualizing the Data on its principal components**
	- A good first-step for many problems is to visualize the data using a **Dimensionality Reduction technique**
	- [Principal Component Analysis (PCA)](https://en.wikipedia.org/wiki/Principal_component_analysis)
	- PCA seeks orthogonal linear combinations of the features which show the greatest variance, and as such, can help give you a good idea of the structure of the data set
	- Plot a projection on the 2 first principal axis
```python
plt.figure()
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
proj = pca.fit_transform(digits.data)
plt.scatter(proj[:, 0], proj[:, 1], c=digits.target, cmap="Paired")
plt.colorbar()
```
* **Classification**
	- For most classification problems, it’s nice to have a **simple**, **fast** method to provide a **quick baseline classification**
	- If the simple and fast method is sufficient, then we don’t have to waste CPU cycles on more complex models
	- If not, we can use the results of the simple method to give us clues about our data
	- One good method to keep in mind is Gaussian Naive Bayes: `sklearn.naive_bayes.GaussianNB`
		* Gaussian Naive Bayes fits a Gaussian distribution to each training label independantly on each feature, and uses this to quickly give a rough classification.
		* It is generally not sufficiently accurate for real-world data, but can perform surprisingly well, for instance on text data
	- **STEPS:**
		* split the data into training and validation sets
			- Why did we split the data into training and validation sets?
		* train the model
		* use the model to predict the labels of the test data
```python
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
#
## split the data into training and validation sets
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target)
#
## train the model
clf = GaussianNB()
clf.fit(X_train, y_train)
#
## use the model to predict the labels of the test data
predicted = clf.predict(X_test)
expected = y_test
#
## Plot the prediction
fig = plt.figure(figsize=(6, 6))  # figure size in inches
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
#
## plot the digits: each image is 8x8 pixels
for i in range(64):
    ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
    ax.imshow(X_test.reshape(-1, 8, 8)[i], cmap=plt.cm.binary,
              interpolation='nearest')
#
    ## label the image with the target value
    if predicted[i] == expected[i]:
        ax.text(0, 7, str(predicted[i]), color='green')
    else:
        ax.text(0, 7, str(predicted[i]), color='red')
```
* **Quantitative Measurement of Performance**
	- We’d like to measure the performance of our estimator without having to resort to plotting examples.
	- A simple method might be to simply compare the number of matches
	- there are other more sophisticated metrics that can be used to judge the performance of a classifier: several are available in the `sklearn.metrics` submodule
		* **classification_report**
			- One of the most useful metrics is the `sklearn.metrics.classification_report`
			- Which combines several measures and prints a table with the results
		* **confusion matrix**
			- Another enlightening metric **for this sort of multi-label classification** is a `sklearn.metrics.confusion_matrix`
			- It helps us visualize which labels are being interchanged in the classification errors
	- **STEPS:**
		1. First print the number of correct matches
		2. The total number of data points
		3. And now, the ration of correct predictions
		4. Print the classification report
		5. Print the confusion matrix
```python
# 1
matches = (predicted == expected)
print(matches.sum())
# 2
print(len(matches))
# 3
matches.sum() / float(len(matches))
#
# 4
from sklearn import metrics
print(metrics.classification_report(expected, predicted))
# 5
print(metrics.confusion_matrix(expected, predicted))
#
plt.show()
```

### 4. Supervised Learning: Regression of Housing Data
- regression problem: learning a continuous value from a set of features
- simple Boston house prices set, available in scikit-learn
- This records measurements of 13 attributes of housing markets around Boston, as well as the median price
- **can you predict the price of a new market given its attributes?**
- It often helps to **quickly visualize pieces of the data** using **histograms**, **scatter plots**, or **other plot types**
```python
from sklearn.datasets import load_boston
data = load_boston()
import matplotlib.pyplot as plt
plt.figure(figsize=(4, 3))
plt.hist(data.target)
plt.xlabel('price ($1000s)')
plt.ylabel('count')
plt.tight_layout()
```

**Feature Selection**
- Sometimes, in Machine Learning it is useful to use feature selection to decide which features are the most useful for a particular problem
- Automated methods exist which quantify this sort of exercise of choosing the most informative features

**Predicting Home Prices: a Simple Linear Regression**
- There are many possibilities of regressors to use
- A particularly simple one is **LinearRegression: this is basically a wrapper around an ordinary least squares calculation**

## **Measuring prediction performance**
- The **averaged f1-score** is often used as a convenient measure of the overall performance of an algorithm. It appears in the bottom row of the classification report; it can also be accessed directly: `metrics.f1_score`
- **Regression metrics** In the case of regression models, we need to use different metrics, such as **explained variance**

### **Overfitting**
- Learning the parameters of a prediction function and testing it on the same data is a methodological mistake: a model that would just repeat the labels of the samples that it has just seen would have a perfect score but would fail to predict anything useful on yet-unseen data
- To avoid over-fitting, we have to define two different sets
	* a training set X_train, y_train which is used for learning the parameters of a predictive model
	* a testing set X_test, y_test which is used for evaluating the fitted predictive model
	* In scikit-learn such a random split can be quickly computed with the `sklearn.model_selection.train_test_split` function

### Model Selection via Validation
### Cross-validation

## Problem Statements
http://blog.thepixelary.com/post/174286685782/blender-for-computer-vision-machine-learning
* Object classification, more commonly known as object recognition, is simple: supply the computer with enough photos of something, along with a descriptor of exactly where it is in each photo, and the computer will learn how to recognize it. This process takes thousands or even tens of thousands of photos.
* So the main challenge is, how to you find enough images to feed the ML algorithm?
While it might be possible to rely on a Google Image search, we still need to tag individual photos with the outline of the toilet seat. This tagging is a manual process that has to happen for each of the photos we need

Rather than collecting real photos and tagging them manually, we decided it would be faster to generate all the images with CGI, and then feed those images back into the computer. This approach has a few distinct advantages over crowd-sourced photo labelling:

* We can generate pixel-perfect masks and depth data for the ML system automatically.
* We can cover a comprehensive range of washroom design, layout, lighting and colors.
* The image generation system we build can be used for other things in the future.

## Future Infrastructure of ML/AI Datacenters
https://cloud.google.com/compute/
https://cloud.google.com/compute/pricing


## Supervised Learning
> Making predictions about the future

* The main goal in supervised learning is to learn a model from labeled training data that allows us to make predictions about unseen or future data.
* we know the right answer beforehand when we train our model

### Key concepts
* One of the key ingredients of supervised machine learning algorithms is to define an objective function that is to be optimized during the learning process.
* This objective function is often a cost function that we want to minimize.

#### Chapter 2
* understanding of the basic concepts of linear classifiers for supervised learning
* implemented a perceptron
* how we can train adaptive linear neurons efficiently via a vectorized implementation of gradient descent and on-line learning via stochastic gradient descent

#### Chapter 3
* Introduction to the concepts of popular classification algorithms
	- differences between several supervised learning algorithms for classification
* Using the scikit-learn machine learning library
* Questions to ask when selecting a machine learning algorithm

#### Chapter 4

#### Chapter 5
* useful techniques, including graphical analysis such as learning curves, to detect and prevent overfitting.

**Choosing a classification algorithm**
Choosing an appropriate classification algorithm for a particular problem task requires practice: each algorithm has its own quirks and is based on certain assumptions.
* no single classifier works best across all possible scenarios
* In practice, it is always recommended that you **compare the performance of at least a handful of different learning algorithms** to select the best model for the particular problem. These may **differ in**:
	* the number of features or samples
	* the amount of noise in a dataset
	* and whether the classes are linearly separable or not
* the performance of a classifier, computational power as well as predictive power, **depends heavily on the underlying data that are available for learning**


**SSE (Sum of Squared Errors)**
* The main advantage of this continuous linear activation function is—in contrast to the unit step function—that the cost function becomes differentiable.
* Another nice property of this cost function is that it is convex;
* thus, we can use a simple, yet powerful, optimization algorithm called gradient descent to find the weights that minimize our cost function to classify the samples in the given dataset.

**Gradient Descent**
* the principle behind gradient descent as climbing down a hill until a local or global cost minimum is reached.
* In each iteration, we take a step away from the gradient where the step size is determined by the value of the learning rate as well as the slope of the gradient
* In practice, it often requires some experimentation to find a good learning rate $\eta$ for optimal convergence.
* different learning rates $\eta= 0.1$ and $\eta= 0.0001$ to start with and plot the cost functions versus the number of epochs to see how well the Adaline implementation learns from the training data.
* The **learning rate $\eta$** , as well as the **number of epochs n_iter**, are the so-called **hyperparameters** of the perceptron and Adaline learning algorithms.
* different techniques to automatically find the values of different hyperparameters that yield optimal performance of the classification model.
* Many machine learning algorithms that we will encounter throughout this book require some sort of feature scaling for optimal performance.
* Gradient descent is one of the many algorithms that benefit from feature scaling.
* **feature scaling method called ++standardization++**, which gives data the property of a standard normal distribution. The mean of each feature is centered at value 0 and the feature column has a standard deviation of 1.
* For example, to standardize the j th feature, we simply need to subtract the sample mean $\mu_j$ from every training sample and divide it by its standard deviation $\sigma_j$:
* $\hat x_j=\frac{x_j-\mu_j}{\sigma_j}$
* minimize a cost function by taking a step into the opposite direction of a gradient that is calculated from the whole training set, this is why this approach is sometimes also referred to as batch gradient descent.

**Stochastic Gradient Descent (SGD)**
* alternative to the batch gradient descent algorithm is **stochastic gradient descent**, sometimes also called **iterative or on-line gradient descent**.
* Instead of updating the weights based on the sum of the accumulated errors over all samples x^i^. We update the weights incrementally for each training sample.
* Stochastic gradient descent can be considered as an approximation of gradient descent, it typically reaches convergence much faster because of the more frequent weight updates.
* gradient is calculated based on a single training example, the error surface is noisier than in gradient descent, which can also have the advantage that stochastic gradient descent can escape shallow local minima more readily
* To obtain accurate results via stochastic gradient descent, it is important to present it with data in a random order, which is why we want to shuffle the training set for every epoch to prevent cycles
* In stochastic gradient descent implementations, the fixed learning rate η is often replaced by an adaptive learning rate that decreases over time.
* Stochastic gradient descent does not reach the global minimum but an area very close to it. By using an adaptive learning rate, we can achieve further annealing to a better global minimum
* Another advantage of stochastic gradient descent is that we can use it for online learning.
* random_state parameter for reproducibility of the initial shuffling of the training dataset after each epoch

**mini-batch learning**
* A compromise between batch gradient descent and stochastic gradient descent is the so-called mini-batch learning.
* Mini-batch learning can be understood as applying batch gradient descent to smaller subsets of the training data—for example, 50 samples at a time.
* The advantage over batch gradient descent is that convergence is reached faster via mini-batches because of the more frequent weight updates.
* mini-batch learning allows us to replace the for-loop over the training samples in Stochastic Gradient Descent (SGD) by vectorized operations, which can further improve the computational efficiency of our learning algorithm.

**online learning**
* In online learning, model is trained on-the-fly as new training data arrives.
* This is especially useful if we are accumulating large amounts of data—for example, customer data in typical web applications.
* Using online learning, the system can immediately adapt to changes and the training data can be discarded after updating the model if storage space in an issue.


### Classification

A supervised learning task with discrete class labels, such as in the previous e-mail spam-filtering example, is also called a classification task.

Classification for predicting class labels Classification is a subcategory of supervised learning where the goal is to predict the categorical class labels of new instances based on past observations. Those class labels are discrete, unordered values that can be understood as the
group memberships of the instances.

### Regression

Another subcategory of supervised learning is regression, where the outcome signal is a continuous value. The prediction of continuous outcomes, is also called regression analysis.

In regression analysis, we are given a number of predictor (explanatory) variables and a continuous response variable (outcome), and we try to find a relationship between those variables that allows us to predict an outcome.

## Reinforcement Learning
> Solving interactive problems

In reinforcement learning, the goal is to develop a system (agent) that improves its performance based on interactions with the environment.
Since the information about the current state of the environment typically also includes a so-called reward signal, we can think of reinforcement learning as a field related to supervised learning. However, in reinforcement learning this feedback is not the correct ground truth label or value, but a measure of how well the action was measured by a reward function. Through the interaction with the environment, an agent can then use reinforcement learning to learn a series of actions that maximizes this reward via an exploratory trial-and-error approach or deliberative planning.

* we define a measure of reward for particular actions by the agent

## Unsupervised Learning
> Discovering hidden structures

* we are dealing with unlabeled data or data of unknown structure
* we are able to explore the structure of our data to extract meaningful information without the guidance of a known outcome variable or reward function

### Clustering/Unsupervised Classification
> Finding subgroups

* Clustering is an exploratory data analysis technique that allows us to organize a pile of information into meaningful subgroups (clusters) without having any prior knowledge of their group memberships.

### Dimensionality Reduction
> Data compression, Visualization

* Often we are working with data of high dimensionality—each observation comes with a high number of measurements—that can present a challenge for limited storage space and the computational performance of machine learning algorithms.
* commonly used approach in feature preprocessing to remove noise from data, which can also degrade the predictive performance of certain algorithms, and compress the data onto a smaller dimensional subspace while retaining most of the relevant information.
* useful for visualizing data

## Roadmap for building Machine Learning System
![Alt ML workflow](images/ai-ml-dl/ml-predictive-modeling-workflow.jpg)

### Preprocessing – getting data into shape
* Raw data rarely comes in the form and shape that is necessary for the optimal performance of a learning algorithm.
* Many machine learning algorithms also require that the selected features are on the **same scale for optimal performance**
	* often achieved by transforming the features in the range [0, 1]
	* a standard normal distribution with zero mean and unit variance
* Some of the selected features may be highly correlated and therefore redundant to a certain degree
	* dimensionality reduction techniques are useful for compressing the features onto a lower dimensional subspace
		* less storage space is required
		* and the learning algorithm can run much faster
* randomly divide the dataset into a separate training and test set
	* performs well on the training set but also generalizes well to new data
	* use the training set to train and optimize machine learning model
	* keep the test set until the very end to evaluate the final model

### Learning/Training
* each classification algorithm has its inherent biases, and no single classification model enjoys superiority if we don't make any assumptions about the task
* In practice, it is therefore essential to compare at least a handful of different algorithms in order to train and select the best performing model
* But before we can compare different models, we first have to decide upon a metric to measure performance. One commonly used metric is classification accuracy, which is defined as the proportion of correctly classified instances.
* **how do we know which model performs well on the final test dataset and real-world data if we don't use this test set for the model selection but keep it for the final model evaluation?**
	- different cross-validation techniques can be used where the training dataset is further divided into training and validation subsets in order to estimate the generalization performance of the model
* we also cannot expect that the default parameters of the different learning algorithms provided by software libraries are optimal for our specific problem task.
	* make use of hyperparameter optimization techniques that help us to fine-tune the performance of the model
	* Intuitively, think of those hyperparameters as parameters that are not learned from the data but represent the knobs of a model that we can turn to improve its performance

**The five main steps that are involved in training a machine learning algorithm can be summarized as follows:-**
1.	 Selection of features.
2.	 Choosing a performance metric.
3.	 Choosing a classifier and optimization algorithm.
4.	 Evaluating the performance of the model.
5.	 Tuning the algorithm.

### Evaluating models and predicting unseen data instances
* use the test dataset to estimate how well it performs on this unseen data to estimate the generalization error
* Note that the parameters for the previously mentioned procedures—such as feature scaling and dimensionality reduction—are solely obtained from the training dataset, and the same parameters are later re-applied to transform the test dataset, as well as any new data samples—the performance measured on the test data may be overoptimistic otherwise.
* If satisfied with its performance, we can now use this model to predict new, future data

## Neural networks
* **single-layer neural network**
	- Perceptron
		* it never converges if the classes are not perfectly linearly separable
	- Adaline (ADAptive LInear NEuron)
		* the **identity function**  $\phi(z)=z$ as the **activation function**
* **Logistic Regression**
	- simple yet more powerful algorithm for linear and binary classification problems: logistic regression. Note that, in spite of its name, logistic regression is a model for classification, not regression
	- linear model for binary classification that can be extended to multiclass classification via the OvR technique.
	- **odds ratio**, which is the odds in favor of a particular event. The odds p ratio can be written as $\frac{p}{( 1 − p )}$ , where p stands for the probability of the positive event.
	- **logit function**, which is simply the logarithm of the odds ratio (log-odds)
	- we are actually interested in is predicting the probability that a certain sample belongs to a particular class, which is the inverse form of the logit function. It is also called the logistic function, sometimes simply abbreviated as sigmoid function due to its characteristic S-shape.
	- In logistic regression, this **activation function** simply becomes the **sigmoid function**
	- The output of the sigmoid function is then interpreted as the probability of particular sample belonging to class
	* **Interpretation:**
		- the probability of particular sample belonging to class 1 $\phi(z)=P(y=1 | x;w)$, given its features x parameterized by the weights w
	- The predicted probability can then simply be converted into a binary outcome via a quantizer (unit step function)
	- Logistic regression is used in weather forecasting, for example, to not only predict if it will rain on a particular day but also to report the chance of rain.
	- logistic regression can be used to predict the chance that a patient has a particular disease given certain symptoms

## Tech Stack
* Python with packages
	- NumPy
	- SciPy
	- scikit-learn (open source machine learning library)
	- matplotlib
	- pandas

## My Notes
**standardized the training data**, before trainining a model
- **Cross-validation**
	- data split in trining and testing dataset
	- in different ratio and can be: 30% testing 70% training
- **feature scaling**
	- Many machine learning and optimization algorithms also require feature scaling for optimal performance.
- Using the fit method, StandardScaler estimated the parameters $\mu$ (sample mean) and $\sigma$ (standard deviation) for each feature dimension from the training data
- By calling the transform method, we then standardized the training data using those estimated parameters μ and σ . Note that we used the same scaling parameters to standardize the test set so that both the values in the training and test dataset are comparable to each other.
- finding an appropriate learning rate requires some experimentation
- If the learning rate is too large, the algorithm will overshoot the global cost minimum. If the learning rate is too small, the algorithm requires more epochs until convergence, which can make the learning slow—especially for large datasets
- Instead of the misclassification error, many machine learning practitioners report the classification accuracy of a model, which is simply calculated as follows:`1 - misclassification error`
- plot the decision regions of our newly trained perceptron model and visualize how well it separates the different samples.
- the perceptron algorithm never converges on datasets that aren't perfectly linearly separable, which is why the use of the perceptron algorithm is typically not recommended in practice

## Keywords
* Adaline - **ADA**ptive **LI**near **NE**uron
* number of epochs - number of passes over the training set
* Overfitting means that the model captures the patterns in the training data well, but fails to generalize well to unseen data.

## Bonus Section
* [Why does vectorized code run faster than looped code?](https://www.reddit.com/r/explainlikeimfive/comments/4namsc/eli5why_does_vectorized_code_run_faster_than/)


## Maths
* Vectors
	- row vector and column vectors
* Matrix
* Probability
	- http://www.math-only-math.com/odds-and-probability.html

## Numpy
```python
np.meshgrid
np.vstack
np.hstack
np.dot
np.where
np.exp
np.arange
# np.arange(-7, 7, 0.1)
np.random.permutation

from numpy.random import seed

```

## matplotlib
```python
import matplotlib.pyplot as plt

plt.plot
plt.axvline
plt.axhline
plt.axhspan
plt.yticks
plt.ylim
plt.xlabel
plt.ylabel
plt.legend
# plt.legend(loc='upper left')

plt.contourf
plt.scatter
plt.show
```
