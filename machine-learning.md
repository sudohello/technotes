/*
Title: ML - Machine Learning
Decription: Machine Learning
Author: Bhaskar Mangal
Date: 
Tags: Machine Leaning, ML
*/

# Machine Learning

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

### scikit-learn
```python
from sklearn.cross_validation import train_test_split # deprecated and use model_selection module instead
from sklearn.model_selection import train_test_split
```
Scikit-learn also implements a large variety of different performance metrics that are available via the metrics module. For example, we can calculate the classification accuracy of the perceptron on the test set.
```python
from sklearn.metrics import accuracy_score
print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))

# Here, y_test are the true class labels and y_pred are the class labels that we predicted previously
```

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

## scikit-learn
* scikit-learn already support multiclass classification by default via the One-vs.-Rest (OvR) method

## Datasets for Machine Learning

### Iris dataset
* The Iris dataset contains the measurements of 150 iris flowers from three different species: Setosa, Versicolor, and Virginica

Iris dataset, consisting of 150 samples and 4 features, can then be written as a
150 × 4 matrix $x \epsilon  R^{150*4}$

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


## sklearn
```python
from sklearn import datasets
datasets.load_iris()

from sklearn.model_selection import train_test_split
train_test_split(X, y, test_size=0.3, random_state=0)

from sklearn.preprocessing import StandardScaler
StandardScaler()

from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)

```
