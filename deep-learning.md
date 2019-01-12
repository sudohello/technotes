---
Title: Deep Learning
Decription: Deep Learning
Author: Bhaskar Mangal
Date: 
Last updated: 24th-Oct-2018
Tags: Deep Learning
---

**Table of Contents**
* TOC
{:toc}


## Deep Learning
* Refer: [Machine Learning](machine-learning.md)
* **References**
  * **Lecture Slides**
    * http://wavelab.uwaterloo.ca/wp-content/uploads/
      * http://wavelab.uwaterloo.ca/wp-content/uploads/2017/04/



**The Task T**
* Machine learning algorithms are usually described in terms of how the algorithm should process an example x ∈ R n .
* Each entry x j of x is called a feature.
* Example : Features in an image can be its pixel values.


**Common Machine Learning Tasks**
* Classification: Find f (x) : R n ⇒ {1, ....., k} that maps examples x to one of k classes.
* Regression: Find f (x) : R n ⇒ R that maps examples to the real line.


**The Experience E**
* classified into two classes: **supervised** and **unsupervised** based on what kind of experience they are allowed to have during the learning process.
* usually allowed to experience an entire **dataset**


**Categorizing Algorithms Based On E**
* Unsupervised learning algorithms experience a dataset containing many features, then learn useful properties of the structure of this dataset.
* Supervised learning algorithms experience a dataset containing features, but each example is also associated with a label or target


**Dataset Splits**
We usually split our dataset to three subsets: train, val, test.
* E is usually experiencing train and val sets.
* P is usually evaluated on test set.
* https://cs230-stanford.github.io/train-dev-test-split.html
* https://cs230-stanford.github.io/
* https://www.coursera.org/learn/machine-learning-projects
* https://www.coursera.org/lecture/machine-learning-projects/train-dev-test-distributions-78P8f
* https://stats.stackexchange.com/questions/19048/what-is-the-difference-between-test-set-and-validation-set
* https://stackoverflow.com/questions/38250710/how-to-split-data-into-3-sets-train-validation-and-test
* https://stats.stackexchange.com/questions/9357/why-only-three-partitions-training-validation-test/9364#9364
* **train**
  * The training set is used to fit the models
* **dev / train-dev/ val / cross-validation** -> all are same
  * the validation set is used to estimate prediction error for model selection
  * The validation set is used for model selection
  * estimate model properties:
    * mean error for numeric predictors
    * classification errors for classifiers
    * recall and precision for IR-models etc.
* **test**
  * the test set is used for assessment of the generalization error of the final chosen model
  * estimate the accuracy of the selected approach
  * the test set for final model (the model which was selected by selection process) prediction error
  * Ideally, the test set should be kept in a “vault,” and be brought out only at the end of the data analysis
* Different Splits Strategies
  * case-1
    * Training set (60% of the original data set)
    * Cross-Validation set (20% of the original data set
    * Test set (20% of the original data set)

* https://web.stanford.edu/~hastie/ElemStatLearn/
* https://web.stanford.edu/~hastie/ElemStatLearn/printings/ESLII_print12.pdf


**Performance Measure P**
* A quantitative measure of performance is required in order to evaluate a machine’s ability to learn
  * P depends on task T
  * **P** is usually the **accuracy of the model**
  *  Another equivalent measure is the **error rate** (also called the expected 0-1 loss)
* The ability to perform well on new, unseen input data is called **generalization**
  * we try to **minimize some error measure** called the **training error**. This is **standard optimization**
  * What differentiates machine learning from standard optimization is that **we care to minimize the generalization error**, the **error evaluated on the test set**
* **Q) Is minimizing over training set error guaranteed to provide parameters that minimize the test set error?**
  * Yes
* The factors that determine how well a machine learning algorithm performs is its ability to:
  * Make the training error small
  * Make the gap between training and test error small
* **Underfitting:** Underfitting occurs when the model is **not able to obtain a sufficiently low error value on the training set**
* **Overfitting:** Overfitting occurs when the **gap between the training error and test error is too large**
* **Capacity:** Capacity is a model’s **ability to fit a wide variety of functions**
  * There is a direct relation between the model’s capacity and whether it will overfit or underfit
  * Models with **low capacity** may **struggle to fit the training set**
  * Models with **high capacity** can **overfit by memorizing properties** of the training set that do not serve them well on the test set
* **Controlling Capacity: The Hypothesis Space**
  * **Hypothesis Space:** the **set of functions that the learning algorithm is allowed to select** as being the solution
  * Increase the model’s capacity by **expanding the hypothesis space**
* **Controlling The Capacity: Regularization**
  * **Regularization** is **any modification we make to a learning algorithm** that is **intended to reduce its generalization error but not its training error**
  * Regularization can be used as a way to **give preference to one solution in our hypothesis space** (more general than restricting the space itself)


**Hyperparameters and Validation Sets**
* **Hyperparameters** are **any variables** that **affect the behavior** of the learning algorithm, **but are not adapted by the algorithm itself**
* **test-train-val split**
  * train set: **learning is performed**
  * val set: **choice of hyperparameters** is done by evaluation
* **Construction of a train-val-test split**
  * Split the data set to **train-test** at a **1 : 1 ratio**
  * Then, split the train set to **train-val** at a **4 : 1 ratio**
* **Q) What happens when the same test set has been used repeatedly to evaluate performance of different algorithms over many years?**


**Estimators, Bias and Variance**
* **Point estimation** is an attempt to **provide the single ”best” prediction θ̂ of some quantity of interest θ**. This quantity might be a scalar, vector, matrix, or even a function.
* **Bias measures** the **expected deviation** of the estimate from the true value of the function or parameter
* The **variance Var(θ̂)** of an estimator provides a **measure of how we would expect the estimate we compute from data to vary** as we independently resample the dataset from the underlying data generating process
* **Bias-Variance Trade Off**
  * **Q) How to choose between two estimators, one with large bias and the other with large variance?**
  * **MSE: Mean-Square Error** of the estimates, incorporates both bias and variance components
  * The relationship between bias and variance is tightly linked to the machine learning concepts of capacity, underfitting and overfitting


**Consistency**
* Consistency is a desirable property of estimators
* It insures that as the number of data points in our data set increase, our point estimate converges to the true value of θ
* convergence here is in probability
* Consistency of an estimator ensures that the bias will diminish as our training data set grows
* It is better to choose consistent estimators with large bias over estimators with small bias and large variance. **Q) Why?**


**Maximum likelihood (ML) Estimation**
* **Maximum likelihood (ML)** is a principle used to derive estimators
* Maximum likelihood can be viewed as a minimization of the dissimilarity between p̂ data and p model . **Q) How?**
* Maximum likelihood can be shown to be the best estimator, asymptotically in terms of its rate of convergence as m → ∞
* The estimator derived by ML is consistent. However, certain conditions are required for consistency to hold:
  * The true distribution p data must lie within the model family p model (.; θ). Otherwise, no estimator can recover p data even with infinite training examples
  * There needs to exist a unique θ. Otherwise, ML will recover p data but will not be able to determine the true value of θ used in the data generation process
* Under these conditions, you are guaranteed to improve the performance of your estimator with more training data


**Optimization**
* Optimization refers to the task of either minimizing or maximizing some function f (x) by altering the value of x
* f(x) is called an **objective function**. In context of machine learning, it is also called the **loss**, **cost**, or **error** function
* **Gradient Based Optimization**
  * Using The Derivative For Optimization
  * The derivative of a function specifies **how to scale a small change in input in order to obtain the corresponding change in output**
  * The derivative is useful for optimization **because it allows knowledge of how to change x to improve f(x)**
  * minimum, maximum, saddle point
  * Global vs Local Optimal Points
* **Gradient Descent**
  * Gradient descent converges when all the elements in the gradient are almost equal to zero
* **Stochastic Gradient Descent - SGD**
  * Nearly all of deep learning is powered by one optimization algorithm: SGD
  * Motivation behind SGD: The cost function used by a machine learning algorithm often decomposes as a sum over training examples of some per-example loss function
  * SGD relies on the fact that the gradient is an expectation, hence can be approximated with a small set of samples


**Challanges that Motivates Deep Learning**
* The mechanisms used to achieve generalization in traditional machine learning are insufficient to learn complicated functions in high-dimensional spaces
* The challenge of generalizing to new examples becomes exponentially more difficult when working with high-dimensional data
* **The Curse Of Dimensionality**
  * Many machine learning problems become exceedingly difficult when the number of dimensions in the data is high
  * This is because the number of distinct configurations of a set of variables increase exponentially as the number of variables increase
* **Local Constancy And Smoothness Regularization**
  * In order to generalize well, machine learning algorithms need to be guided by prior beliefs about what kind of function they should learn
  * most widely used priors is the **smoothness** or **local constancy** prior
  * A function is said to have local constancy if it **does not change much within a small region of space**,Example: K nearest neighbors
* **manifold learning**
  * A manifold is a connected region in space. Mathematically, it is a set of points, associated with a neighborhood around each points
  * From any point, the surface of the manifold appears as a euclidean space
  * Example: We observe the world as a 2-D plane, whereas in fact it is a spherical manifold in 3-D space
  * Manifold Learning: Most of R n consists of invalid input. Interesting input occurs only along a collection of manifolds embedded in R n
  * Conclusion: probability mass is highly concentrated
  * Probability distributions in natural data (images, text strings, and sound) is highly concentrated
  * Examples encountered in natural data are connected to each other by other examples, with each example being surrounded by similar data



**Concepts**
* prior probability distribution p(θ)
* posterior distribution
* High entropy distributions
* uniform and Gaussian distributions
* Bayes rule, Bayesian Statistics, Bayesian Linear Regression
* Maximum a posteriori estimation (MAP)



**Deep Learning**
* **Feedforward:** Information flows from the input x through some intermediate steps, all the way to the output y. There is no Feedback connections.
* **Neural Networks:** **Neural** because these models are loosely inspired by neuroscience, **Networks** because these models can be represented as a composition of many functions
* **Different Layers**
  * First layer is called the **input layer**
  * The final layer is called the **output layer**
  * The layers in between, input and output layers are called **hidden layers**
* **Depth:** The **length of the chain of functions** in a neural network is called its depth
* **Width:** The **dimensionality of the hidden layers** of a neural network is called its width
* **Training Data**
  * The training data provides us with noisy approximations
  * Only the output of the neural network is specified for each example
  * The training data does not specify what the network should do with its hidden layers, the network itself must decide how to modify these layers to best implement an approximation
  * This is referred to as **representation learning**

### Bulding Blocks of Deep Learning

#### **Designing Deep Learning Algorithms**
* Specify and optimization procedure, cost function, and model family
* Design considerations specific to the cost function and the model family
* **Conclusions**
  * the standard choice to increase the capacity of feedforward networks is to go deeper, rather than wider
  * Choosing a deep model encodes a very general belief that the function we want to learn should involve composition of several simpler functions. The prior helps us overcome the curse of dimensionality!


#### **Cost Function**
* The cost function is a measure of how well our algorithm performs
* Training is performed through minimizing the cost function
* As with traditional machine learning algorithms, most neural networks are trained using maximum likelihood
* The cost function in that case referred to as the **cross entropy** between between the **training data** and the **model distribution**


#### **Output Layer**
* The choice of cost function is tightly coupled with the choice of output unit
* This is because the form of the cross-entropy function depends on how the output is represented


#### **The Output Layer: Linear Units**
* A simple kind of output unit is one based on an affine transformation with no non-linearity
* Using maximum likelihood estimation, the cost function will be the Mean Square Error
* Classification With Linear Output Units, and Multiclass SVM Cost Function
* Define the Multi-Class SVM Loss also called the **Hinge Loss**


#### **The Output Layer: Softmax Units**
* **Softmax functions** are most often used as the **output of a classifier**, to represent the probability distribution over K different classes
* Softmax function on a vector z is applied element wise

#### **The Output Layer: Other Output Types**
* linear, softmax output units
* **Sigmoid** units are sometimes used for binary classification
* **Gaussian mixture models** are employed in mixture density networks


#### **Hidden Units**
* Hidden units are what makes deep learning unique
* Generally, all hidden units discussed in start off with a linear transformation of the input
* The linear transformation is followed by an **element wise**, **nonlinear function g(z)** . This function is usually called the **activation function**


#### **Activation functions**
* **The Rectified Linear Units: ReLU**
  * The ReLU hidden unit are the default choice of activation function for Feedforward Neural Networks
  * The ReLU hidden unit use the function `max(0, z)` as its activation function
  * ReLUs are easy to optimize because they are very similar to linear units
  * Derivative through ReLU remain large whenever the unit is active
  * The derivative is also consistent, and the gradient direction is far more useful for learning than it would be with activation functions that introduce second order effects
  * One drawback of ReLUs is that they cannot learn via gradient based methods on examples for which their activation function is zero
  * However, this drawback is not as sever as what we refer to as the **”dead”** ReLU phenomenon
  * A large gradient flowing through a ReLU neuron could cause the weights to update in such a way that the neuron will never activate on any datapoint again
  * If this happens, then the gradient flowing through the unit will forever be zero from that point on. That is, the ReLU units can irreversibly die during training since they can get knocked off the data manifold
* **Leaky ReLu**
  * The **Leaky ReLu** tries to remedy the ”dead” ReLU problem by allowing learning to proceed even with z ≤ 0
  * This is done through extending the activation function to be: `g(z) = max(0, z) + α min(0, z)`. `α` is usually set to `0.1`
* **Parametric ReLu**
  * **Parametric ReLu** uses the same concept as the Leaky Relu, but treats `α` as a **learnable parameter**
* **Maxout ReLu**
  * Maxout units can be thought of as a generalization to the ReLU units
  * Maxout units can learn a piecewise linear, convex function with up to k pieces. This can be thought of as **learning the activation function itself**
  * With large enough k, Maxout units can learn to approximate any convex function up to an arbitrary fidelity
  * The Maxout units enjoy the benefetis of ReLUs with out having any of their drawbacks
  * Because each unit is driven by multiple filters, Maxout units have some redundancy that helps them to resist a phenomenon called **catastrophic forgetting**, in which **neural networks forget how to perform tasks that they were trained on in the past**
  * However, each Maxout unit is now parametrized by k weight vectors instead of just one,so Maxout units typically need more regularization than ReLUs
* **Sigmoidal Units**
  * Prior to the introduction of ReLUs, most neural networks used the sigmoid activation function
  * The sigmoid activation function ”squashes” its input to a value between 0 and 1
  * The sigmoid function has seen frequent use historically since it has a nice interpretation as the firing rate of a neuron: from not firing at all (0) to fully-saturated firing at an assumed maximum frequency
  * sigmoidal units have been abandoned in Feedforward Neural Networks because:
    * Sigmoidal units saturate and kill gradients
      * When the value of z is at the 0 tail of the sigmoid function, the local gradient is very small. This will result in the sigmoid ”Killing” the gradient and almost no signal will flow through the neuron to its weights and recursively to its data. If the value of z is on the 1 tail (when the initial weights are very large for example), then the gradient is also almost zero and the network will barely learn
    * The outputs of Sigmoidal units are not zero-centered. This is less sever than gradient killing, but also affects the gradient decent dynamics
* **Tanh Units**
  * Tanh is one other non-linearity that was used prior to ReLUs
  * The Tanh unit attempts to fix the zero-centering problem of the sigmoidal unit
  * However, the tanh function also has the sigmoid function’s same gradient killing characteristics
  * Tanh units is almost always favoured over the sigmoidal unit
* **Sigmoidal and Tanh Units**
  * Recurrent networks, many probabilistic models, and some autoencoders have additional requirements that rule out the use of piecewise linear activation functions and make sigmoidal and tanh units more appealing despite the drawbacks of saturation


### **Computing the Derivation: Back-Propogation**
* **Forward Propagation And Back Propagation**
  * When we use the a feedforward neural network to accept an input x and produce an output ŷ, information flows from the input to the cost function J(θ)
  * During training, we need to update the parameters according to the cost function. **Back Propagation** or **Backprop** for short, allows us to propagate information from the cost function through the parameters.
* **Backprop**
  * Backprop is not the whole learning algorithm, it is **merely a method to compute the derivatives**
  * It **can be used to compute the derivative of any function**, and **is not limited to deep neural networks training**
  * Backprop relies on **applying the chain rule recursively**
  * **Modifying the parameters** is done by SGD or other **optimization algorithms**
  * Backprop can be easily understood when applied on computational graphs


#### **Universal Approximation Properties Of Feedforward Neural Networks**
* The No Free Lunch theorem shows that there is no universally superior machine learning algorithm. Feedforward networks provide a universal system for representing functions, in the sense that, given a function, there exists a feedforward network that approximates the function. There is no universal procedure for examining a training set of specific examples and choosing a function that will generalize to points not in the training set
* The universal approximation theorem says that there exists a network large enough to achieve any degree of accuracy we desire, but the theorem does not say how large this network will be. The single hidden layer might be infeasably large. Furthermore, it may fail to generalize well due to overfitting.
* In many circumstances, using deeper models can reduce the number of units in each hidden layer that are required to represent the desired function and can reduce the amount of generalization error.



### **Regularization For Deep Models**
* **Regularization** is any **modification** made to the learning algorithm with an intention to **lower the generalization error** but **not the training error**
* most regularization strategies are based on **regularizing estimators**. This is done through **reducing variance** at the **expense of increasing the bias** of the estimator
* An effective regularizer is one that **decreases the variance significantly** while **not overly increasing the bias**
* **three regimes** concerning the **capacity of models** where the model either:
  1. Excludes the true data generating process which induces bias (underfitting)
  2. Matches the true data generating process
  3. Includes the true data generating process, but also includes many other possible candidates, which results in variance dominating the estimation error (overfitting)
* The goal of regularization is to take the model from the third to the second regime
* **controlling the complexity of the model** is **not a simple matter** of finding the right model size and the right number of parameters, because:
  * we never have access to the true data generating distribution - extremely complicated domains (images, text and audio sequences)
  * the data generating process is almost certainly outside the chosen model family
* Instead, deep learning **relies on finding the best fitting model as a large model that has been regularized properly**


#### **Regularization Strategies**
1. **Parameter Norm Penalities**
  * most traditional form of regularization
  * This approach **limits the capacity of the model** by **adding the penalty** `Ω(θ)` to the objective function
  * `α ∈ [0, ∞)` is a **hyperparameter** that **weights the relative contribution of the norm penalty to the value of the objective function**
  * When the optimization procedure tries to minimize the objective function, it will also decrease some measure of size of the parameters θ
  * The bias terms in the affine transformations of deep models usually require less data to be fit and are usually left unregularized
  * Without loss of generality, we will assume we will be regularizing only the weights w
  * **L2 Norm Parameter Regularization**
    * The L2 parameter norm penalty, also **known as weight decay** drives `w` closer to the origin by adding the regularization term
    * The weights **multiplicatively shrink** by a constant factor at each step
    * L2 norm penalty can be interpreted as a MAP Bayesian Inference with a Gaussian prior on the weights
  * **L1 Norm Parameter Regularization**
    * L1 norm penalty can be interpreted as a MAP Bayesian Inference with a Isotropic Laplace Distribution prior on the weights
2. **Data Augmentation**
  * for consistent estimators, the best way to get better generalization is to train on more data
  * under most circumstances, data is limited and labelling is an extremely tedious task
  * **Dataset Augmentation** provides a cheap and easy way to increase the amount of your training data
    * **Color jitter** is a very effective method to augment datasets. It is also extremely easy to apply
      * **Fancy PCA** was proposed by Krizhevsky et al. in the famous Alex net paper. It is a way to perform color jitter on images
    * **Horizontal Flipping** is applied on data that **exhibit horizontal asymmetry**
      * Care must be taken to propagate the labels through this transformation
      * Horizontal flipping can be applied to **natural images** and **point clouds**
      * one can **double the amount of data** through horizontal flipping
  * Many other task specific dataset augmentation algorithms exist
  * It is highly advised to always use dataset augmentation
  * be careful not to alter the correct output!
  * Example: `b` and `d`, horizontal flipping
  * Furthermore, **when comparing two machine learning algorithms** train **both** with **either** augmented or non-augmented dataset.Otherwise, no subjective decision can be made on which algorithm performed better
3. **Noise Robustness**
  * **Noise Injection** can be thought of as a form of regularization
  * The addition of noise with infinitesimal variance at the input of the model is equivalent to imposing a penalty on the norm of the weights (Bishop, 1995)
  * Noise can be **injected at different levels** of deep models
  * **Noise Robustness : Noise Injection on Weights**
    * Noise added to weights can be interpreted as a more traditional form of regularization
    * This form of regularization encourages the parameters to go to regions of parameter space where small perturbations of the weights have a relatively small influence on the output
    * In other words, it pushes the model into regions where the model is relatively insensitive to small variations in the weights, finding points that are not merely minima, but minima surrounded by flat regions (Hochreiter and Schmidhuber, 1995)
  * **Noise Robustness : Noise Injection on Outputs**
    * Most datasets have some amount (A LOT!) of mistakes in the y labels. Minimizing our cost function on wrong labels can be extremely harmful
    * One way to remedy this is to explicitly model the noise on labels
    * This is done through setting a probability for which we think the labels are correct
    * This probability is easily incorporated into the cross entropy cost function **analytically**
    * An example is **label smoothing**
  * **Noise Robustness : Label Smoothing**
    * It has the advantage of preventing the pursuit of hard probabilities without discouraging correct classification
4. **Early Stopping**
  * **Motivation**
    * When training models with sufficient representational capacity to overfit the task, we often observe that training error decreases steadily over time, while the error on the validation set begins to rise again
    * The occurrence of this behaviour in the scope of our applications is almost certain
    * This means we can obtain a model with better validation set error (and thus,hopefully better test set error) by returning to the parameter setting at the point in time with the lowest validation set error
    * This is termed **Early Stopping**
    * **Practical Issues**
      * one of the most used regularization strategies in deep learning
      * Early stopping can be thought of as a **hyperparameter selection method**, where **training time** is the **hyperparameter** to be chosen
      * However, a portion of data should be reserved for validation
      * Choosing the training time automatically can be done through a single run through the training phase, the only addition being the evaluation of the validation set error at every n iterations. This is usually done on a second GPU
      * Overhead for writing parameters to disk is negligible
    * First Strategy, To exploit all of our precious training data we can:
      * a) Employ early stopping
      * b) Retrain using all of the data up to the point that was determined during early stopping
        * **Q)** Do we train for the same number of parameter updates or for the same number of epochs(passes through training data)?
    * A second strategy to exploit the full training dataset would be to:
      * a) Employ early stopping    
      * b) Continue training with the parameters determined by early stopping, using the validation set data
      * This strategy avoids the high cost of retraining the model from scratch, but is not well-behaved
      * Since we no longer have a validation set, we cannot know if generalization error is improving or not. Our best bet is to stop training when the training error is not decreasing much any more
5. **Parameter Tying**
  * Parameter Tying refers to explicitly forcing the parameters of two models to be close to each other, through the norm penalty
6. **Parameter Sharing**
  * Parameter Sharing imposes much stronger assumptions on parameters through forcing the parameter sets to be equal
7. **Multitask Learning**
  * Multitask Learning is a way to improve generalization by pooling the examples arising out of several tasks
  * Multitask learning is a form of parameter sharing
  * Improved generalization and generalization error bounds can be achieved because of the shared parameters, for which statistical strength can be greatly improved in proportion with the increased number of examples for the shared parameters, compared to the scenario of single-task models
  * Intuitively, the additional task imposes constraints on the parameters in the shared layers, preventing overfitting
  * Improvement in generalization only occurs when there is something shared across the tasks at hand
8. **Bagging**
  * Bagging (short for **bootstrap aggregating**) is a technique for reducing generalization error through combining several models
  * Train k different models on k different subsets of training data, constructed to have the same number of examples as the original dataset through random sampling from that dataset **with replacement**. Have all of the models **vote** on the output for test examples
  * Techniques employing bagging are called **ensemble models**
  * The reason that Bagging works is:
    * different models will usually not all make the same errors on the test set.This is a direct results of training on k different subsets of the training data, where each subset is missing some of the examples from the original dataset
    * Other factors such as differences in random initialization, random selection of mini-batches,differences in hyperparameters, or different outcomes of non-deterministic implementations of neural networks are often enough to cause different members of the ensemble to make **partially independent errors**
9. **Ensemble Models**
  * The only disadvantage of ensemble models is that they do not provide us with a scalable way to improve performance. Usually, ensemble models of more than 2-3 networks become too tedious to train and handle.
10. **Dropout**
  * Dropout provides a computationally inexpensive but powerful method of regularizing a broad family of models
  * Dropout provides an inexpensive approximation to training and evaluating a bagged ensemble of exponentially many neural networks
  * Specifically, dropout trains the ensemble consisting of all sub-networks that can be formed by removing non-output units from an underlying base network
  * it is very computationally cheap, using dropout during training requires only O(n) computation per example per update,to generate n random binary numbers and multiply them by the state
  * It works well with nearly any model that uses a distributed representation and can be trained with stochastic gradient descent
  * Though the cost per-step of applying dropout to a specific model is negligible,the cost of using dropout in a complete system can be significant
  * keep in mind that for very large datasets, regularization confers little reduction in generalization error. In these cases, the computational cost of using dropout and larger models may outweigh the benefit of regularization
  * **Training with Dropout**
    * To train with dropout,we use a minibatch-based learning algorithm that makes small steps, such as stochastic gradient descent
    * Each time we load an example into a minibatch, we randomly sample a different binary mask to apply to all of the input and hidden units in the network
    * The mask for each unit is sampled independently from all of the others
    * Typically, the probability of including a hidden unit is `0.5`, while the probability of including an input unit is `0.8`
    * Dropout allows us to represent an exponential number of models with a tractable amount of memory
    * Dropout removes the need to accumulate model votes at the inference stage
    * Dropout can intuitively be explained as forcing the model to learn with missing input and hidden units
    * Dropout training has some **intricacies**:
      * At training time, we are **required** to divide the output of each unit by the probability of that unit’s dropout mask
      * The **goal is** to make sure that the **expected total input to a unit at test time** is **roughly the same** as the **expected total input to that unit at train time**, even though **half the units at train time are missing on average**
11. **Adversarial Training**
  * In many cases, neural networks have begun to reach human performance when evaluated on an i.i.d. test set
  * However, szegedy et al.(2014) found that even networks that have achieved human accuracy, have a 100% error rate on examples that have been intentionally constructed to ”fool” the network
  * the modified example is so similar to the original one, human observers cannot tell the difference
  * These examples are called **adversarial examples**
  * Adversarial examples are interesting in the context of regularization because one can reduce the error rate on the original i.i.d.test set via adversarial training - training on adversarially perturbed examples from the training set
  * Adversarial training discourages highly sensitive linear behaviour through explicitly introducing a local constancy prior into supervised neural nets


### **Optimization for Training Deep Models**
* Newton’s Method, Conjugate Gradients, Broyden-Fletcher-Goldfarb-Shanno Algorithms (BFGS), Limited Memory BFGS (L-BFGS).
* this problem is so important and so expensive, a specialized set of optimization techniques have been developed for solving it
* Finding the parameters θ of a neural network that significantly reduces a cost function J(θ)
* **First Order Optimization Algorithms**
  * Optimization algorithms that use only the **gradient** are termed first order optimization algorithms
  * First order algorithms are optimal for neural network training since the target loss functions can be decomposed to a sum over training data
* **Second Order Optimization Algorithms**
  * Optimization algorithms that make use of the **Hessian matrix** are termed second order optimization algorithms
  * Hessian Matrix is a matrix of second derivatives
  * The simplest second order optimization algorithm is **Newton’s Method**
  * The **condition number** of the matrix is the ratio of the magnitude of the largest singular value to the smallest
* **Lipschitz Continuity**
  * In the context of deep learning, we sometimes gain some guarantees by restricting ourselves to functions that are either Lipschitz continuous or have Lipschitz continuous derivatives
  * A Lipschitz continuous function is a function f whose rate of change is bounded by a Lipschitz constant L
  * This property is useful because it allows us to quantify our assumption that a small change in the input made by an algorithm such as gradient descent will have a small change in the output
* **How Learning Differs From Pure Optimization?**
* the Loss function can be written as an average over the training set
* **empirical risk minimization**
  * Rather than optimizing the risk directly, we optimize the empirical risk, and hope that the risk decreases significantly as well
  * in the context of deep learning, we cannot usually use empirical risk minimization
* We should rely on a slightly different approach, in which the quantity that we actually optimize is even more different from the quantity that we truly want to optimize
* **Surrogate Loss Functions**
  * Instead of minimizing empirical risk, we minimize surrogate loss functions
  * A surrogate loss function acts as a proxy to empirical risk while being ”nice” enough to be optimized efficiently
  * Example: SVM loss is a surrogate to the 0-1 loss for classification
* **Batch and Minibatch Algorithms**
  * One aspect of machine learning algorithms that separates them from general optimization algorithms is that the objective function usually decomposes as a sum over the training examples
  * The gradient in this case is also an expectation over training data
  * Computing this expectation exactly is very expensive as it requires evaluating the model on every example in the entire dataset
  * optimization algorithms usually converge faster if they are allowed to rapidly compute approximate estimates of the gradient rather than slowly computing exact gradients
  * Another consideration that motivates the estimation of the gradient from a small number of samples is the **redundancy in the training set**
  * Optimization algorithms that **use the entire training set** to compute the gradient are called **batch or deterministic gradient methods**
  * Ones that use a **single training example** for that task are called **stochastic or online gradient methods**
  * Most of the algorithms we use for deep learning fall somewhere in between
  * These are called **minibatch** or **minibatch stochastic methods**
  * Larger batches provide a more accurate estimate of the gradient, but with less than linear returns
  * Multicore architectures are usually underutilized by extremely small batches.This motivates using some absolute minimum batch size, below which there is no reduction in the time to process a minibatch
  * Small batches can offer a regularizing effect. The best generalization error is often achieved with batch size of 1 (Wilson and Martinez, 2003)
  * It is **extremely crucial** that minibatches are sampled at **random**
* **Model identifiability Problem**
  * A model is said to be identifiable if a suffeciently large training set can rule out all but one setting of the model’s parameters
  * In fact, if we have m layers with n hidden units each, there are n!^m ways of arranging the hidden units to obtain equivalent models
  * **weight space symmetry**
  * Local minima are only truly problematic if they have a much higher cost than the global minimum
  * it is not important to find a true global minimum. We can do with finding a point in parameter space that has low but not minimal cost
* In lower dimensional spaces, local minima and maxima are common
* In higher dimensional spaces, local minima and maxima are rare, saddle points are much more common
* **Plateaus, Saddle Points, and Other Flat Regions**
* The proliferation of saddle points in high dimensional spaces  explains why second order methods have failed to replace gradient decent for deep learning
* Dauphin et al. (2014) introduced a **saddle-free Newton Method** for second order optimization
* Second-order methods remain difficult to scale to large neural networks, but this saddle-free approach holds promise if it could be scaled
* **Cliffs And Exploding Gradients**
  * Neural networks with many layers often have extremely steep regions reassembling cliffs
  * **Cliffs** result from the multiplication of several large weights together
  * Gradients do not specify the optimal step size, but only the optimal direction within and infinitesimal region
  * **Long Term Dependencies:** Arises when the computational graph is very deep. The result of this problem is vanishing and exploding gradients
* **Initialization is really important** - initialization is very important for stable performance of our optimization algorithms
* We almost never arrive to a global minimum, our goal is to reduce the generalization error rather than the cost function itself



### **Parameter Initialization Strategies**
* **The initial point can effect:**
  * the speed of convergence
  * the quality of the final solution
  * if the algorithm converges all together
* points of comparable cost will have a different generalization error!
* we have very primitive understanding on the effect of the initial point on generalization, which offers no guidance in the selection procedure
* **Good Characteristics Of Initial Parameters**
* Breaking The Weight Space Symmetry
  * If two hidden units with the same activation function are connected to the same inputs, then these units must have different initial parameters
* **random initialization**
  * If we have at most as many outputs as inputs, we could use **Gram-Schmidt orthogonalization on an initial weight matrix**, and be guaranteed that each unit computes a very different function from each other unit
  * Random Initialization is performed by setting the biases to a constant (0 or 0.01 in most cases)
  * Weights are initialized by sampling from either a Gaussian or a uniform distribution (the choice doesn’t seem to matter much)
  * The scale of the initial distribution, however, does have a large effect on both the outcome of the optimization procedure and on the ability of the network to generalize
  * Larger initial weights will yield a stronger symmetry breaking effect, helping to avoid redundant units. (Also prevents loss of signal in forward pass)
  * However, initial weights that are too large may result in exploding values during forward propagation or back-propagation. (**choas** in RNNs)
* **Normalized (Xavier) Initialization**
  * A rule of the thumb is to **always use xavier initialization** when **training ReLU based networks from scratch**


## **First Order Optimization Algorithms**
* SGD Varients: **SGD**, **Momentum**, **Nestrov Momentum**, **AdaGrad**, **RMS-Prop**, **Adam**
* Stochastic Gradient Decent (SGD) and its variants are probably the most used optimization techniques for deep model training
* The learning rate is an essential parameter
* **In practice, it is necessary to gradually decrease the learning rate over time**
  * This is because SGD gradient estimation introduces a source of noise, caused by the random minibatch sampling
  * However, the true gradient becomes closer to 0 as we converge to a minimum
* In practice, it is common to decay the learning rate linearly until iteration `τ` according to: `ek = (1 − α)e0 + αeτ`
* `α = k/τ`
* After iteration τ we keep `e` constant
* Choosing `eτ` , `e0` and `τ` is more of an art than a science
* **This is done by monitoring the learning curves that plot the objective functions as a function of time**
* **Large oscillations implies one is using a large e0**
* Gentle oscillations are fine, especially if we are using a stochastic cost functions
* Typically, the **optimal initial learning rate**, in terms of total training time and the final cost value, is higher than the learning rate that yields the best performance after the first 100 iterations or so
* It is usually best to monitor the first several iterations and use a learning rate that is higher than the best-performing learning rate at this time, but not so high that it causes severe instability
* `τ` is chosen as the number of iterations it takes for the algorithm to go through a few hundred passes through the training set. `eτ` is chosen to be approximately 1% of `e0`
* **Momentum**
  * Momentum tries to remedy the slowness of SGD especially in face of high curvature, small but consistent gradients, or noisy gradients
  * The momentum algorithm accumulates an exponentially decaying moving average of past gradients and continues to move in their direction
  * Analogous to rolling a ball with mass and gravity on the topology of the objective function
  * `α ∈ [0, 1]` is a **hyperparameter** that **determines how quickly the contributions of previous gradients exponentially decay**. In practice, `α` is set to be `0.5`, `0.9` and `0.99`
* **Nestrov Momentum**
  * The difference between Nesterov momentum and standard momentum is where the gradient is evaluated
  * With Nesterov momentum the **gradient is evaluated after the current velocity is applied**
  * Thus one can interpret Nesterov momentum as attempting to add a correction factor to the standard method of momentum
* **AdaGrad**
  * AdaGrad **individually adapts the learning rates of all model parameters** by **scaling them inversely proportional to the square root** of the **sum of all of their historical squared values**
  * The parameters with the largest partial derivative of the loss have a correspondingly rapid decrease in their learning rate, while parameters with small partial derivative shave a relatively small decrease in their learning rate
  * The net effect is greater progress in the more gently sloped directions of parameter space
  * AdaGrad performs well for some but not all deep learning models
  * Empirically it has been found that for training deep neural network models the accumulation of squared gradients from the beginning of training can result in a premature and excessive decrease in the effective learning rate
* **RMSProp**
  * RMSProp modifies AdaGrad to perform better in the non-convex setting by changing the gradient accumulation into an exponentially weighted moving average
  * RMSProp uses an exponentially decaying average to discard history from the extreme past so that it can converge rapidly after finding a convex bowl, as if it were an instance of the AdaGrad algorithm initialized within that bowl
  * Effective and practical optimization algorithm for deep neural networks
  * **It is currently one of the go-to optimization methods being employed routinely by deep learning practitioners**
* **Adam (adaptive moments)**
  * Adam (adaptive moments) is a **variant of RMSProp** and momentum with a few important distinctions
  * First, in Adam, momentum is incorporated directly as an estimate of the first order moment (with exponential weighting) of the gradient
  * Second, Adam includes bias corrections to the estimates of both the first-order moments (the momentum term) and the (uncentered) second-order moments to account for their initialization at the origin
  * **Always use Adam, it is fairly robust to the choices of hyperparameters and available in many deep learning packages**


### **Optimization Strategies And Meta-Algorithms**
* Batch Norm, Coordinate Descent, Polyak Averaging, Greedy Supervised Pretraining.
* **Batch Normalization** (Ioffe and Szegedy, 2015) is one of the most exciting innovations in optimizing neural networks
  * It is not an optimization algorithm, but a method of **adaptive reparameterization**
  * Training a deep model involves parameter updates for each layer via gradient direction under the assumptions that other layers are not changing
  * In practice, all layers are updated simultaneously. This can cause unexpected results in optimization
  * It is very hard to choose an appropriate learning rate, because the effects of an update to the parameters for one layer depends so strongly on all of the other layers
  * Second order optimization methods tries to remedy this phenomenon by taking into account second order effects. However, in very deep networks, the effects of higher order effects is very prominent
  * **Solution**: Batch normalization provides an elegant way of reparametrizing almost any deep network
  * It can be applied to any layer, and the reparametrization significantly **reduces the problem of coordinating updates across many layers**
  * Improves gradient flow through the network
  * Allows higher learning rates
  * Reduces the strong dependence on initialization
  * Acts as a form of regularization in a funny way, and slightly reduces the need for dropout, maybe?
* **Greedy Supervised Pretraining**
  * Greedy algorithms can be computationally much cheaper than algorithms that solve for the best joint solution, and the quality of a greedy solution is often acceptable if not optimal.
  * Greedy algorithms may also be followed by a fine tuning stage in which a joint optimization algorithm searches for an optimal solution to the full problem
  * Initializing the joint optimization algorithm with a greedy solution can greatly speed it up and improve the quality of the solution it finds
* To improve optimization, the best strategy is not always to improve the optimization algorithm
* In practice, it is more important to choose a model family that is easy to optimize than to use a powerful optimization algorithm
* model design strategies can help to make optimization easier; Example: auxiliary losses, skip connections


### **Convolutional Neural Networks (ConvNets)**
* ConvNets are a specialized kind of neural networks for processing data that has a **known grid like topology**
* Example of such data can be 1-D time series data sampled at regular intervals, or 2-D images
* these networks employ the mathematical convolution operator
* Convolutions are a special kind of linear operators that can be used instead of general matrix multiplication
* machine learning libraries implement cross-correlation while calling it convolutions
* **Why Use Convolution**
  * Convolutions leverage three important ideas that can help improve a machine learning system:
    * Sparse Interactions
      * Sparse connectivity is achieved by making the kernel smaller than the input
      * This allows the network to efficiently describe complicated interactions between many variables by constructing such interactions from simple building blocks that each describe only sparse interactions
    * Parameter Sharing
      * It refers to using the same parameter for more than one function in a model
      * Convolutional layers heavily apply this concept through applying the same kernel to every position of the input
      * This does not affect the runtime at inference, but it affects the memory requirement per layer as we now have to store only k parameters
      * Convolution is dramatically more efficient than dense matrix multiplication in terms of memory requirements and statistical efficiency
    * Equivariant Representation
      * A function `f(x)` is equivariant to a function `g(x)` if `f(g(x)) = g(f(x))`
      * Convolution operators are equivariant to translation of the input
      * Convolution is not naturally equivariant to some other transformations, such as changes in the scale or rotation of an image. Other mechanisms are necessary for handling these kinds of transformations
  * convolutions provide a way to handle input of different sizes
* In practice, **three hyperparameters** **control the size** of the **output** of a convolutional layer:
  * The output **depth** of the volume is a hyper parameter and **corresponds** to the **number of filters** we would like to use, each learning to look for something different in the input
  * The output **width** and **height** are **controlled by** the **stride** we use **to slide each filter** and the **padding** we use **to expand the input**
* Compute the **size of the output volume**, assuming that the filters are `m × m` and we have `K filters`.
  * $W_out = \frac{W_in - m + 2Padding}{Stride + 1}$
  * $H_out = \frac{H_in - m + 2Padding}{Stride + 1}$
  * $D_out = K$
* The number of parameters in a convolutional layer:
  * `Parameters = m^2 × k × D_in + k` 
  * This is due to the layer having `m^2 × D` in weights for `k` filters and `k` biases
* The backward pass for a convolution operation (for both the data and the weights) is also a convolution (but with spatially-flipped filters)
* `1 × 1` convolutions are used to **manipulate the depth of the output volume**. They can be thought of **as a dot product through a depth slice**
* Many variations of convolution exist such as **Dilated Convolutions** and **Deformable Convolutions**
* Receptive Field
* Output Volume size


### **Pooling Layers**
* A pooling function replaces the output of the previous layer, with a summary statistic of the nearby outputs
* Pooling helps to make representations become approximately invariant to small translation of the input. If we translate the input a small amount, the output of the pooling layer will not change
* The use of pooling can be viewed as adding an infinitely strong prior that the function the layer learns must be invariant to small translations. When this assumption is correct, it can greatly improve the statistical efficiency of the network
* Average Pooling
* Max Pooling
* If the pools do not overlap, pooling loses valuable information about where things are. We need this information to detect precise relationships between the parts of an object.
* Alternatively, Just use a larger stride every once in a while to shrink down the input size
* **Discarding pooling layers** has also been **found to be important** in training good generative models, such as **variational autoencoders (VAEs)** or **generative adversarial networks (GANs)**
* **Region Of Interest (ROI) Pooling**
  * It is an operation widely used in object detection tasks using convolutional neural networks
  * The operation was proposed in Fast RCNN paper in 2015
  * Its purpose is to **perform max pooling on inputs of non-uniform sizes to obtain fixed-size feature maps**
  * This **enables** training architectures **containing RPNs** in an **end-to-end** fashion
  * ROI pooling employes three steps to transform the input regions to similar size feature vectors:
    * Divide the region proposal into equal-sized sections (the number of which is the same as the dimension of the output)
    * Find the largest value in each section
    * Copy these max values to the output buffer
  * For training a network in an end-to-end fashion, ROI pooling layers need to be (sub)differentiable
  * Backpropagation Through ROI Pooling
  * ROI pooling has different goals than regular pooling
  * It allows the network to reuse the feature map for all ROIs
  * It also allows obtaining same size feature vectors from multimodal input

### **Capsules - alternative to Pooling**
* Geoffrey Hinton On Pooling, he proposed **”capsules”** (subnetworks in networks) as an alternative to pooling
* https://medium.com/mlreview/deep-neural-network-capsules-137be2877d44
* https://hackernoon.com/what-is-a-capsnet-or-capsule-network-2bfbe48769cc


### **Practical Considerations for Training Deep Models**
* **A machine learning practitioner also needs to know**:
  * how to choose an algorithm for a particular application
  * how to monitor and respond to feedback obtained from experiments
  * how to use this feedback in order to improve a machine learning system
* **We need to know:**
  * when to collect more data
  * increase or decrease the capacity of our model
  * add or remove regularization
  * improve the optimization algorithm
  * or simply just debug the software implementation of the model
* Each one of the above operations is **extremely time consuming** and it is **very important** to us that we **know exactly where we went wrong**
* In practice, one can usually do much better with a correct application of a commonplace algorithm than by sloppily applying an obscure algorithm
* **Methodology**
  * **Determine your goals**
    * what error metric to use
    * your target value for this error metric
    * These goals and error metrics should be driven by the problem that the application is intended to solve
  * **Establish a working end-to-end pipeline**
    * This should be done as soon as possible
    * should include the estimation of the appropriate performance metrics
  * **Instrument the system well to determine bottlenecks in performance**
    * Diagnose which components are performing worse than expected
    * whether it is due to overfitting, underfitting, or a defect in the data or software
  * **Repeatedly make incremental changes**
    * This includes gathering new data
    * adjusting hyperparameters
    * changing algorithms, based on specific findings from your instrumentation
* **Determining The Goals Of The System**
  * **Performance Metrics**
    * Determining which **error metric** to use is the most important first step for designing a deep learning system
    * This is because your error metric will guide all your future actions
    * The second step is determining the value of the **error metric to beat**
    * Keep in mind that for most applications, it is **impossible to achieve zero error**, reasons:
      * Imperfect optimization procedure
      * Not enough training data
      * The real data distribution is not part of the model distribution family
      * Even with infinite training data and the ability to recover the true data distribution, there is a minimum error bound that a system can achieve, reasons:
        * The input features may not contain complete information about the output variable
        * The process to be estimated might be inherently stochastic

    * **Q)** how can we determine what minimum performance measure is required?
    * **Academic Setting**
      * Standard benchmarks for almost all applications already exist
      * The result to beat is the best performing published algorithm on those benchmarks
      * Keep in mind to not compare apples to oranges
      * **Do not** compare **two algorithms** that have been **trained with different training data**
      * **Do not** compare **ensembles of networks** to a **single network**
    * **Applications Setting**
      * We usually have some idea of the error rate that is necessary for an application to be safe,cost-effective, or appealing to consumers
      * In this setting, every method to get a performance boost should be used. This includes:
        * collecting more data
        * model ensembles
        * empirically determined thresholds
        * dataset augmentation
  * **Default Baselines**
    * After choosing performance metrics and goals, the next step in any practical application is to establish a reasonable end-to-end system as soon as possible
    * deep learning research progresses quickly, so better default algorithms are likely to become available regularly
    * You should never use a cannon to hunt a rabbit
    * If your problem does not fall in the **AI-Complete** category, then you will likely do well with a simple statistical model such as **linear SVMs** or **logistic regression**
    * If your problem falls in the **AI-Complete** category, **choose the base architecture** based on the structure of the problem
    * **Supervised learning problems**:
      * With **fixed small size input vectors** will most likely use **feed forward Fully Connected Networks**
      * With **with input variables** that has **known topological structure** will most likely use **feed forward Convolutional Networks**
      * With **input or output** that are **sequences**, **trees**, or **graphs** should use **gated recurrent networks** such as **LSTMs** or **GRUs**
    * **Unsupervised learning problems**
      * should consider **VAEs** or **GANs**
    * **Image Feature Extractors**
      * VGG-16, ResNet-101, or Inception-V3
    * **Object Detection Baseline Models (2D)**
      * Faster-RCNN, YOLO-9000, RFCNs
    * **Semantic Segmentation**
      * Segnet, fully convolutional network
    * **Optimizers**
      * ADAM, RMS-Prop. (Both with a decaying learning rate)
      * Apply batch norm when possible
    * **Regularization**
      * **Early stopping** should universally be used
      * **Dropout** is an easy regularizer to implement
      * Be careful to **try batch norm first**, since it might remove the necessity to use dropout
* **The Design Process**
  * After establishing an end-to-end baseline, train and test on the dataset at hand:
    * **Always plot** the **training** and **validation errors**
  * There are **three scenarios** that machine learning practitioners usually face:
    * The training set error remains high
    * The training set error decreases, but the validation set error remains high
    * Both training and validation set errors are low
* **Design Process Steps:**
  1. Determine Performance Metrics
  2. Establish a Working End-to-End System
  3. Is training Set Error High?
    a) If Yes, then:
      * Bigger Model
      * Train Longer
      * Redesign the Architecture
    b) if No, then ask another question
  4. Is Validation Set Error High?
    a) If Yes, then:
      * Gather More Data
      * Add Regularization
      * Re-design the architecture
    b) If No, then proceed
  5. Debug High Training & Validation Errors
  6. Is Test-Validation Set Error High?
    a) If Yes, then:
      * Gather More Data
      * Data Synthesis
      * Re-design the architecture
    b) if No, then ask another question
  7. Is Test Set Error High
    a) If Yes, then:
      * Get more Test-Validatin Data
    b) If No, then re-think deign process
* **High Training Error: Debugging**
  * **Is the optimizer code running correctly?**
    * If you implemented the gradient functions yourself, **make sure** the gradient is correct via gradient checks.
    * **Is** the learning rate **correct**?
  * **Does the model have high enough capacity?**
    * **Make sure** the model is able to overfit a small portion of the dataset
  * **Did you train for a reasonable amount of epochs?**
  * If all else fails, you need to **rethink your architecture**
* **High Validation Error: Debugging**
  * **Do you have enough training data?**
    * Collect more training data
    * use dataset augmentation methods
  * **Are you overfitting?**
    * Employ regularization strategies
  * If all else fails, you need to **rethink your architecture**
* **What If Nothing Helps?**
  * very pathological case
  * This case is illustrated as the validation set having a different distribution than the actual test set
  * This case motivates us to rethink the design process
* **Hyperparameter Selection: Manual Tuning**
  * Choosing hyperparameters manually requires following understanding:
    * what the hyperparameters do
    * the exact relationship betweenthe hyperparameters, training error, generalization error, and computational resources
  * The **primary goal** of manual hyperparameter search is to **adjust the effective capacity of the model** to match the complexity of the task
  * **Effective Capacity** is governed by three factors:
    * The **representational capacity** of the model
    * The ability of the learning algorithm to **successfully optimize the cost function**
    * The degree to which the cost function and the training procedure regularize the model
  * **Some common hyperparameters and their effect on the effective capacity**
    * **Number Of Hidden Units**
      * Increases representational capacity when increased and hence increase effective capacity
      * Increasing the number of hidden units increases both time and memory required for essentially every operation on the model
    * **Convolutional Kernel Width**
      * Increases the number of parameters in the model when increased and hence increase effective capacity
      * A wider kernel results in a narrower output dimension, reducing model capacity unless you use implicit zero padding to reduce this effect
      * Wider kernels require more memory for parameter storage and increase runtime, but a narrower output reduces memory cost
    * **Implicit Padding**
      * Adding implicit zeros before convolution keeps the representation size large
      * Increasing the size of the padding increases the effective capacity of the model
      * Implicit padding increases the size of the input and hence increases the time and memory cost of most operations
    * **Weight Decay Coefficient**
      * Decreasing the weight decay coefficient frees the model parameters to become larger hence increasing the effective capacity of the model
    * **Dropout Rate**
      * Dropping units less often gives the units more opportunities to conspire with each other to fit the training set
    * **Learning Rate**
      * Perhaps the most important hyperparameter
      * **If you have time to tune only one hyperparameter, do that for the learning rate**
      * The learning rate controls the effective capacity of the model in a complex way
      * The **effective capacity is the highest** when the **learning rate is correct**
* **Hyperparameter Selection: Automatic Tuning**
  * The ideal learning algorithm just takes a dataset and outputs a function, without requiring hand-tuning of hyperparameters
  * Manual hyperparameter tuning can work very well when:
    * the user has a good starting point, such as one determined by others having worked on the same type of application and architecture
    * or when the user has months or years of experience in exploring hyperparameter values for neural networks applied to similar tasks
  * **Automatic Hyperparameter Selection** algorithms wrap around the learning algorithm and choose its hyperparameters
  * Hyperparameter optimization algorithms often have their own hyperparameters, such as the range of values that should be explored for each of the learning algorithm’s hyperparameters. These however are much easier to determinate
* The current state of deep learning allows us to tackle inference tasks that can be done by humans in less than one second
* It also allows us to tackle a set of tasks that is very hard for human beings to perform. This set is the set of prediction tasks


### Performance Measures

* **Proposal Recall**
  * Measure of how much of the objects that the proposals extract from the ground truth set
  * `R = (No. of correctly detected rectangles) / (No. of rectangles in the database)`
* **Precision**
  * Measure of how many of the actual positive detection are indeed true objects
  * `P = (No. of correctly detected rectangles) / (Total number of detected rectangles)` 
* Average Precision
* Average Localization Precision
* Average Orientation Similarity
* IoU - Intersection of Union


### TBD
* Curriculum Learning
* unsupervised learning models
* few shot
* one shot
* zero shot learning
* domain adaptation
* adversarial examples
* Generative models


### References
* https://github.com/vdumoulin/conv_arithmetic
* https://arxiv.org/pdf/1603.07285.pdf


### Keywords
* i.i.d - [independent and identically distributed](https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables) 



## Questions
* **Q)** Is minimizing over training set error guaranteed to provide parameters that minimize the test set error?
* **Q)** What happens when the same test set has been used repeatedly to evaluate performance of different algorithms over many years?
* **Q)** How to choose between two estimators, one with large bias and the other with large variance?
* **Q)** Why it is better to choose consistent estimators with large bias over estimators with small bias and large variance?
* **Q)** How Maximum likelihood can be viewed as a minimization of the dissimilarity between p̂ data and p model?
* **Q)** How to determine that the performance of estimator would increase with more training data?
* **Q)** What is the computational cost for computing the stochastic gradient descent?
* **Q)** How does exponential increase in the distinc configurations of a set of variables affect ML algorithms?
* **Q)** Is there a way to represent a complex function that has many more regions to be distinguished than the number of training examples?
* **Q)** Why is it called softmax?
* **Q)** How to make convolution with maxout activation?
  * https://stackoverflow.com/questions/45009051/how-to-make-convolution-with-maxout-activation
  * https://towardsdatascience.com/activation-functions-and-its-types-which-is-better-a9a5310cc8f
* **Q)** What is the difference between L2 and L1 norm penalty when applied to machine learning models ? But what happens over the entire course of training in both?
  * The L2 Norm penalty **decays the components of the vector w that do not contribute much to reducing the objective function**
  * On the other hand, the **L1 norm penalty provides solutions that are sparse**. This **sparsity** property can be thought of as a **feature selection** mechanism
* **Q)** How Learning Differs From Pure Optimization?
* **Q)** What is the problem with empirical risk minimization?
  * Empirical risk minimization is prone to overfitting. Models with high enough capacity can simply memorize the training set
* **Q)** What Minibatch Size Should We Use?
* **Q)** What are the implications of the proliferation of saddle points in the cost functions of deep models?
* **Q)** How to define convolution operator mathematically?
* **Q)** What is a Capsule Network?
  * https://hackernoon.com/what-is-a-capsnet-or-capsule-network-2bfbe48769cc
* **Q)** how can we determine what minimum performance measure is required?



## Notes
* [Deep Learning Frameworks, Toolchain, Libraries](deep-learning-frameworks.md)
* [Datasets and Data Creation for Deep Learning](deep-learning-datasets-and-creation.md)

## Debugging Neural Networks
* https://www.quora.com/The-convolutional-neural-network-Im-trying-to-train-is-settling-at-a-particular-training-loss-value-and-a-training-accuracy-just-after-a-few-epochs-What-can-be-the-possible-reasons



## FAQs - Technical Questions

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
---
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

---

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
	* https://en.wikipedia.org/wiki/Convolutional_neural_network
	* http://cv-tricks.com/tensorflow-tutorial/training-convolutional-neural-network-for-image-classification/
When designing the architecture of a neural network you have to decide on:
- How do you arrange layers?
- Which layers to use?
- How many neurons to use in each layer etc.?
Once you have decided the architecture of the network;
- the second biggest variable is the weights(w) and biases(b) or the parameters of the network.
- What is the objective of the training?
The objective of the training is to get the best possible values of the all these parameters which solve the problem reliably. For example, when we are trying to build the classifier between dog and cat, we are looking to find parameters such that output layer gives out probability of dog as 1(or at least higher than cat) for all images of dogs and probability of cat as 1((or at least higher than dog) for all images of cats.

You can find the best set of parameters using a process called Backward propagation, i.e. you start with a random set of parameters and keep changing these weights such that for every training image we get the correct output. There are many optimizer methods to change the weights that are mathematically quick in finding the correct weights. GradientDescent is one such method(Backward propagation and optimizer methods to change the gradient is a very complicated topic. But we don’t need to worry about it now as Tensorflow takes care of it).
- Which architectures should I use? Should I create my own architecture to get started with?
	- There are many standard architectures which work great for many standard problems. Examples being AlexNet, GoogleNet, InceptionResnet, VGG etc. In the beginning, you should only use the standard network architectures. You could start designing networks after you get a lot of experience with neural nets. Hence, let’s not worry about it now.

**Machine Learning** and the role it plays in computer vision, image classification, and deep learning.
- http://neuralnetworksanddeeplearning.com/index.html
- http://neuralnetworksanddeeplearning.com/chap1.html
once we've learned a good set of weights and biases for a network, it can easily be ported to run in Javascript in a web browser, or as a native app on a mobile device. 

I had to make specific choices for the number of epochs of training, the mini-batch size, and the learning rate, ηη. As I mentioned above, these are known as hyper-parameters for our neural network, in order to distinguish them from the parameters (weights and biases) learnt by our learning algorithm.


But if we were coming to this problem for the first time then there wouldn't be much in the output to guide us on what to do. We might worry not only about the learning rate, but about every other aspect of our neural network. We might wonder if we've initialized the weights and biases in a way that makes it hard for the network to learn? Or maybe we don't have enough training data to get meaningful learning? Perhaps we haven't run for enough epochs? Or maybe it's impossible for a neural network with this architecture to learn to recognize handwritten digits? Maybe the learning rate is too low? Or, maybe, the learning rate is too high? When you're coming to a problem for the first time, you're not always sure.

we need to develop heuristics for choosing good hyper-parameters and a good architecture.

support vector machine or SVM
* http://peekaboo-vision.blogspot.in/2010/09/mnist-for-ever.html
* http://neuralnetworksanddeeplearning.com/chap2.html
	- algorithm for computing such gradients, an algorithm known as backpropagation.
  - how quickly the cost changes when we change the weights and biases.

**Interview Excerpt**
* https://www.pyimagesearch.com/2018/07/02/an-interview-with-francois-chollet/
People gravitate towards incremental architecture tricks that kinda seem to work if you don’t test them adversarially. They use weak baselines, they overfit to the validation set of their benchmarks. Few people do ablation studies (attempting to verify that your empirical results are actually linked to the idea you’re advancing), do rigorous validation of their models (instead of using the validation set as a training set for hyperparameters), or do significance testing.

We should remember that the purpose of research is to create knowledge. It’s not to get media coverage, nor is it to publish papers to get a promotion.

Mathematical notation can be a huge accessibility barrier, and it isn’t at all a requirement to understand deep learning clearly. Code can be in many cases a very intuitive medium to work with mathematical ideas.

* **How to understand / calculate FLOPs of the neural network model?**
  * http://imatge-upc.github.io/telecombcn-2016-dlcv/slides/D2L1-memory.pdf

● Estimating neural network memory consumption
● Mini-batch sizes and gradient splitting trick
● Estimating neural network computation (FLOP/s)
● Calculating effective aperture sizes


## Research Papers
* https://github.com/ujjwalkarn/deeplearning-papernotes
* https://www.research.ibm.com/artificial-intelligence/publications/2018/download/pdf/scalingAI.pdf


## References
* http://lvdmaaten.github.io/tsne/
	- t-Distributed Stochastic Neighbor Embedding (t-SNE)
* http://cs231n.github.io/classification/
* http://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf
* http://people.csail.mit.edu/torralba/shortCourseRLOC/index.html
* https://www.coursera.org/learn/machine-learning
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


## MOOC Courses
* https://www.coursera.org/learn/neural-networks
* http://cs231n.github.io/
* http://deeplearning.net/tutorial/
* http://www.fast.ai/2017/09/08/introducing-pytorch-for-fastai/
* http://course.fast.ai/
* http://imatge-upc.github.io/telecombcn-2016-dlcv/
* https://towardsdatascience.com/how-to-learn-deep-learning-in-6-months-e45e40ef7d48
* https://towardsdatascience.com/lets-code-a-neural-network-in-plain-numpy-ae7e74410795



**Central repository for all lectures on deep learning at UPC ETSETB TelecomBCN.**
* https://github.com/telecombcn-dl/lectures-all
* https://github.com/telecombcn-dl/2016-dlcv
* https://github.com/telecombcn-dl/2017-dlsl
* https://github.com/telecombcn-dl/2018-dlsl
* https://github.com/telecombcn-dl/lectures-all/blob/master/computer-vision.md


## **Currentyly Reading**
* https://github.com/telecombcn-dl/lectures-all/blob/master/computer-vision.md
* http://insightdata.ai/


## AL-ML-DL blogs
- http://www.fast.ai/2018/07/12/auto-ml-1/
- http://www.fast.ai/2018/04/30/dawnbench-fastai/
- https://www.forbes.com/sites/nvidia/2018/08/02/how-swiss-federal-railway-is-improving-passenger-safety-with-the-power-of-deep-learning/#10fc74a650e3
- https://www.linkedin.com/pulse/how-set-up-nvidia-gpu-enabled-deep-learning-development-tianyi-pan
- https://hackernoon.com/setting-up-your-gpu-machine-to-be-deep-learning-ready-96b61a7df278
- http://timdettmers.com/2014/09/21/how-to-build-and-use-a-multi-gpu-system-for-deep-learning/
- https://becominghuman.ai/setting-up-deep-learning-gpu-environment-5651564ff936



### **AutoML and Neural Architecture Search**
- As it’s name suggests, AutoML is one field in particular that has focused on automating machine learning, and a subfield of AutoML called neural architecture search is currently receiving a ton of attention.
- https://www.youtube.com/watch?v=kSa3UObNS6o
- The term AutoML has traditionally been used to describe automated methods for model selection and/or hyperparameter optimization.
- https://www.automl.org/automl/
- AutoML provides a way to select models and optimize hyper-parameters. It can also be useful in getting a baseline to know what level of performance is possible for a problem.
- What Pichai refers to as using **“neural nets to design neural nets”** is known as **neural architecture search**; typically **reinforcement learning** or **evolutionary algorithms** are used to design the **new neural net architectures**.
  - NASNet:1800 GPU days (the equivalent of almost 5 years for 1 GPU) 
  - AmoebaNet: 3150 GPU days (the equivalent of almost 9 years for 1 GPU)
  - Efficient Neural Architecture Search (ENAS): 16hrs, 1 GPU
  - DARTS - Differentiable architecture search (DARTS)
    - To learn a network for Cifar-10, DARTS takes just 4 GPU days, compared to 1800 GPU days for NASNet and 3150 GPU days for AmoebaNet (all learned to the same accuracy). This is a huge gain in efficiency! 
- how can humans and computers work together to make machine learning more effective?


## Deep Learning, CCN Terms and Concepts
* https://github.com/ml4a/ml4a.github.io/blob/master/_chapters/neural_networks.md

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
* Overfitting
	- https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html
	* Since we only have few examples, our number one concern should be overfitting. Overfitting happens when a model exposed to too few examples learns patterns that do not generalize to new data, i.e. when the model starts using irrelevant features for making predictions.
	* For instance, if you, as a human, only see three images of people who are lumberjacks, and three, images of people who are sailors, and among them only one lumberjack wears a cap, you might start thinking that wearing a cap is a sign of being a lumberjack as opposed to a sailor. You would then make a pretty lousy lumberjack/sailor classifier.
	* Data augmentation is one way to fight overfitting, but it isn't enough since our augmented samples are still highly correlated.
	*  Your main focus for fighting overfitting should be the **entropic capacity** of your model --how much information your model is allowed to store. A model that can store a lot of information has the potential to be more accurate by leveraging more features, but it is also more at risk to start storing irrelevant features. Meanwhile, a model that can only store a few features will have to focus on the most significant features found in the data, and these are more likely to be truly relevant and to generalize better.
* **Entropy**
	* https://en.wikipedia.org/wiki/Entropy_(information_theory)
	* Generally, information entropy is the average information of all possible outcomes.
	* There are different ways to modulate **entropic capacity**. The main one is the choice of **the number of parameters in your model**, i.e.
		- the number of layers
		- the size of each layer
		- weight regularization
			- such as L~1~ or L~2~ regularization, which consists in forcing model weights to taker smaller values.
		- Data augmentation
		- Dropout
			- Dropout also helps reduce overfitting, by preventing a layer from seeing twice the exact same pattern, thus acting in a way analoguous to data augmentation (you could say that both dropout and data augmentation tend to disrupt random correlations occuring in your data).
*  Dilated Convolutions


### Neural Network Zoo
* [neural network zoo prequel: cells and layers](https://www.asimovinstitute.org/author/fjodorvanveen/)
* [neural network zoo](http://www.asimovinstitute.org/neural-network-zoo/)


### Options in User Interface for Model Selection and Traning
**Deep Learning Key Terms**
1. Select Dataset
	* Dataset Summary:
		- Image Size: 256x256
		- Image Type: COLOR
		- DB backend: lmdb
		- Create DB (train): 4501 images
		- Create DB (val): 1499 images
2. Solver Options
	* Training epochs - How many passes through the training data?
	* Shuffle Train Data - For every epoch, shuffle the data before training
	* Snapshot interval (in epochs)
		- How many epochs of training between taking a snapshot?
	* Validation interval (in epochs)
		- How many epochs of training between running through one pass of the validation data?
	* Random seed
		- If you provide a random seed, then back-to-back runs with the same model and dataset should give identical results.
	* Batch size
		- How many images to process at once. If blank, values are used from the network definition. (accepts comma separated list)
	* Batch Accumulation
		- Accumulate gradients over multiple batches (useful when you need a bigger batch size for training but it doesn't fit in memory).
	* Solver type
		- What type of solver will be used?
		- NESTEROV: Nesterov's accelerated gradient (NAG)
		- ADAGRAD: Adaptive gradient (AdaGrad)
		- RMSPROP">RMSprop
		- ADADELTA">AdaDelta
		- ADAM">Adam
	* RMS decay value
		- If the gradient updates results in oscillations the gradient is reduced by times 1-rms_decay. Otherwise it will be increased by rms_decay.
	* Base Learning Rate
		- Affects how quickly the network learns. If you are getting NaN for your loss, you probably need to lower this value. (accepts comma separated list)
3. Data Transformations
	* Subtract Mean
		- Subtract the mean file or mean pixel for this dataset from each image.
		- None, Image, Pixel
	* Crop Size
		- If specified, during training a random square crop will be taken from the input image before using as input for the network.
	* Data Augmentations
		- Flipping: Randomly flips each image during batch preprocessing.
			* None, Horizontal, Vertical, Horizontal and/or Vertical
		- Quadrilateral Rotation - Randomly rotates (90 degree steps) each image during batch preprocessing.
			* None; 0, 90 or 270 degrees; 0 or 180 degrees; 0, 90, 180 or 270 degrees
		- Rotation (+- deg) (ARBITRARY_ROTATION) - "The uniform-random rotation angle that will be performed during batch preprocessing.
		- SCALING: Rescale (stddev) - Retaining image size, the image is rescaled with a +-stddev of this parameter. Suggested value is 0.07.
		- NOISE: Noise (stddev) - Adds AWGN (Additive White Gaussian Noise) during batch preprocessing, assuming [0 1] pixel-value range. Suggested value is 0.03.
		- HSV Shifting - Augmentation by normal-distributed random shifts in HSV color space, assuming [0 1] pixel-value range.
			* Hue: 0.02, Saturation: 0.04, Value: 0.06
4. Networks
	* Standard Networks
	* Previous Networks
	* Pretrained Networks
	* Custom Network
5. Framework
	* Caffe
	* Torch


### What are Convolutional Neural Networks and why are they important?
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


### Data Divide
Split your training set into training set and a validation set. Use validation set to tune all hyperparameters. At the end run a single time on the test set and report performance.


Cross-validation. In cases where the size of your training data (and therefore also the validation data) might be small, people sometimes use a more sophisticated technique for hyperparameter tuning called cross-validation. Working with our previous example, the idea is that instead of arbitrarily picking the first 1000 datapoints to be the validation set and rest training set, you can get a better and less noisy estimate of how well a certain value of k works by iterating over different validation sets and averaging the performance across these. For example, in 5-fold cross-validation, we would split the training data into 5 equal folds, use 4 of them for training, and 1 for validation. We would then iterate over which fold is the validation fold, evaluate the performance, and finally average the performance across the different folds.


In practice. In practice, people prefer to avoid cross-validation in favor of having a single validation split, since cross-validation can be computationally expensive. The splits people tend to use is between 50%-90% of the training data for training and rest for validation.


It is worth considering some advantages and drawbacks of the Nearest Neighbor classifier. Clearly, one advantage is that it is very simple to implement and understand. Additionally, the classifier takes no time to train, since all that is required is to store and possibly index the training data. However, we pay that computational cost at test time, since classifying a test example requires a comparison to every single training example. This is backwards, since in practice we often care about the test time efficiency much more than the efficiency at training time. In fact, the deep neural networks we will develop later in this class shift this tradeoff to the other extreme: They are very expensive to train, but once the training is finished it is very cheap to classify a new test example. This mode of operation is much more desirable in practice.


## WebGL GPU based Deep Learning in Browser
* https://github.com/transcranial/keras-js
* https://news.ycombinator.com/item?id=12302932
* https://erkaman.github.io/regl-cnn/src/demo.html
* https://github.com/uber/horovod
* http://timdettmers.com/2017/04/09/which-gpu-for-deep-learning/


** Hardware Guides for Deep Learning
* http://timdettmers.com/2015/03/09/deep-learning-hardware-guide/

**References**
* http://www.deeplearningbook.org/
* https://blog.udacity.com/2015/06/a-beginners-git-github-tutorial.html
* https://in.udacity.com/course/how-to-use-git-and-github--ud775


### Training on ImageNet
* https://medium.com/syncedreview/tencent-ml-team-trains-imagenet-in-record-four-minutes-d3d85eff2062


### References
* https://www.pyimagesearch.com/2017/03/20/imagenet-vggnet-resnet-inception-xception-keras/
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


#### News/Articles
* http://www.dailymail.co.uk/sciencetech/article-3371075/See-world-eyes-driverless-car-town-Interactive-tool-reveals-autonomous-vehicles-navigate-streets.html
* http://www.sanborn.com/highly-automated-driving-maps-for-autonomous-vehicles/
* https://medium.com/@Synced


## AI Patents
* https://medium.com/syncedreview/epo-issues-first-guidelines-on-ai-patents-995a797109c6


## Machine Learning
* https://elitedatascience.com/learn-machine-learning
* https://www.datacamp.com/community/tutorials/deep-learning-python#gs.ny4aO4s


## Object Detection
* https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10/blob/master/README.md
* https://www.pyimagesearch.com/2018/05/14/a-gentle-guide-to-deep-learning-object-detection/
* https://www.pyimagesearch.com/2017/09/11/object-detection-with-deep-learning-and-opencv/
* https://www.pyimagesearch.com/2017/09/18/real-time-object-detection-with-deep-learning-and-opencv/
* https://www.pyimagesearch.com/deep-learning-computer-vision-python-book/


## Street View Image Segmentation

**Segmentation**
* https://medium.com/nanonets/nanonets-how-to-use-deep-learning-when-you-have-limited-data-f68c0b512cab
* https://medium.com/nanonets/how-to-do-image-segmentation-using-deep-learning-c673cc5862ef
* https://blog.goodaudience.com/using-convolutional-neural-networks-for-image-segmentation-a-quick-intro-75bd68779225
* https://github.com/subodh-malgonde/semantic-segmentation
* http://www.cvlibs.net/datasets/kitti/eval_road.php
* https://github.com/udacity/CarND-Semantic-Segmentation/


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


**References**
* [MULTI-SCALE CONTEXT AGGREGATION BY DILATED CONVOLUTIONS](https://arxiv.org/pdf/1511.07122.pdf)


The dilated convolution operator has been referred to in the past as “convolution with a dilated filter”


### Road Segmentation
* http://mi.eng.cam.ac.uk/projects/segnet/tutorial.html


**SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Segmentation**
* https://www.youtube.com/watch?v=G15Dg2QoI_M


**How to Simulate a Self-Driving Car**
* https://www.youtube.com/watch?v=EaY5QiZwSP4
* https://medium.com/self-driving-cars/term-1-in-depth-on-udacitys-self-driving-car-curriculum-ffcf46af0c08
* https://github.com/udacity/self-driving-car-sim
* https://hackernoon.com/five-skills-self-driving-companies-need-8546d2aba7c1
* https://developers.google.com/edu/c++/getting-started
* https://github.com/CPFL/Autoware


#### caffe-segnet

**Errors while installation**
* hdf5 dir not found HDF5_DIR-NOTFOUND
https://github.com/NVIDIA/DIGITS/issues/156


#### keras-segnet
* https://github.com/imlab-uiip/keras-segnet
```bash
sudo pip install pandas
```

model.add(Convolution2D(112,3,3, border_mode='same',init='uniform',input_shape=(136,136,3),dim_ordering='tf',name='conv_1.1'))
model.add(Conv2D(112,(3,3), border_mode='same',kernel_initializer='uniform',input_shape=(136,136,3),dim_ordering='tf',name='conv_1.1'))

* https://github.com/tensorflow/cleverhans/issues/109

Convolutional2D -> CONV2D with following parameters have changed name/format:-
 Conv2D(10, 3, 3) becomes Conv2D(10, (3, 3))
 kernel_size can be set to an integer instead of a tuple, e.g. Conv2D(10, 3) is equivalent to Conv2D(10, (3, 3))
subsample -> strides
border_mode -> padding
nb_filter -> filters


## LeNet – Convolutional Neural Network in Python

* http://www.pyimagesearch.com/2016/08/01/lenet-convolutional-neural-network-in-python/
* http://www.pyimagesearch.com/2016/07/25/convolutions-with-opencv-and-python/

convolutional, activation, and pooling layers, fully-connected layer, activation, another fully-connected, and finally a softmax classifier

In many ways, LeNet + MNIST is the “Hello, World” equivalent of Deep Learning for image classification.

* https://www.pyimagesearch.com/pyimagesearch-gurus/
- Common splits include the standard 60,000/10,000, 75%/25%, and 66.6%/33.3%. I’ll be using 2/3 of the data for training and 1/3 of the data for testing later in the blog post.
* http://opencv.org/
* https://medium.com/@acrosson/installing-nvidia-cuda-cudnn-tensorflow-and-keras-69bbf33dce8a
* http://chrisstrelioff.ws/sandbox/2014/06/04/install_and_setup_python_and_packages_on_ubuntu_14_04.html


In reality, an (image) convolution is simply an element-wise multiplication of two matrices followed by a sum.
* http://www.pyimagesearch.com/2016/08/01/lenet-convolutional-neural-network-in-python/
* http://www.pyimagesearch.com/2016/07/25/convolutions-with-opencv-and-python/
* http://www.pyimagesearch.com/2016/08/01/lenet-convolutional-neural-network-in-python/


**An image is just a multi-dimensional matrix:**
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
- `~/.keras/keras.json`
- The objective of our training is to learn the correct values of weights/biases for all the neurons in the network that work to do classification between dog and cat.
- The Initial value of these weights can be taken anything but it works better if you take normal distributions(with mean zero and small variance).
- There are other methods to initialize the network but normal distribution is more prevalent.


## Learning Keras by Implementing the VGG Network From Scratch
https://hackernoon.com/learning-keras-by-implementing-vgg16-from-scratch-d036733f2d5


## Case Studies


### [MULTI-SCALE CONTEXT AGGREGATION BY DILATED CONVOLUTIONS](https://arxiv.org/pdf/1511.07122.pdf)

The dilated convolution operator has been referred to in the past as “convolution with a dilated filter”

* https://github.com/BVLC/caffe/issues/782
* https://github.com/BVLC/caffe/issues/263
* https://stackoverflow.com/questions/14585598/installing-numba-for-python
  ```bash
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



### Snippets
```bash
python convert.py \
  --caffemodel=~/Documents/ml/dilation/pretrained/dilation8_pascal_voc.caffemodel \
  --code-output-path=./pascal_voc_tf/dil8_net.py \
  --data-output-path=./pascal_voc_tf/ \
  ~/Documents/ml/dilation/models/dilation8_pascal_voc_deploy.prototxt
#
python convert.py def_path=~/Documents/ml/dilation/models/dilation8_pascal_voc_deploy.prototxt --caffemodel=~/Documents/ml/dilation/pretrained/dilation8_pascal_voc.caffemodel --code-output-path=./pascal_voc_tf/dil8_net.py --data-output-path=./pascal_voc_tf/
```


## Nvidia Deep Learning


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
* https://www.nvidia.com/en-us/deep-learning-ai/education/

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


## PyImageSearch
* https://www.pyimagesearch.com/static/cv_dl_resource_guide.pdf
* https://www.pyimagesearch.com/2014/10/13/deep-learning-amazon-ec2-gpu-python-nolearn/


## Latest Research


### 2018
* [automatically-remove-the-background-from-a-photo/]
  - https://news.developer.nvidia.com/this-ai-can-automatically-remove-the-background-from-a-photo/
  - Semantic Soft Segmentation
  - https://www.youtube.com/watch?v=QYIQbfnS9jA


## TBD Notes
* **Drones**
- https://medium.com/nanonets/how-we-flew-a-drone-to-monitor-construction-projects-in-africa-using-deep-learning-b792f5c9c471

**Pedistrian Detection in Survelliance**
- https://github.com/thatbrguy/Pedestrian-Detector
- https://medium.com/nanonets/how-to-automate-surveillance-easily-with-deep-learning-4eb4fa0cd68d
* The most popular variants are the Faster RCNN, YOLO and the SSD networks
* There is always a Speed vs Accuracy vs Size trade-off when choosing an Object Detection algorithm.
* a scalable surveillance system should be able to interpret low quality images.
* Most high performance models consume a lot of memory
* Pocessing Power:
  - The video streams from the cameras are processed frame by frame on a remote server or a cluster.
  - The obvious problem is latency; you need a fast Internet connection for limited delay. Moreover, if you are not using a commerical API, the server setup and maintenance costs can be high.
  * By attaching a small microcontroller, we can perform realtime inference on the camera itself. There is no transmission delay, and abnormalities can be reported faster than the previous method. 
  * Moreover, this is an excellent add on for bots that are mobile, so that they need not be constrained by range of WiFi/Bluetooth available. (such as microdrones).
  * The disadvantage is that, microcontrollers aren’t as powerful as GPUs, and hence you may be forced to use models with lower accuracy.
  - https://medium.freecodecamp.org/how-to-play-quidditch-using-the-tensorflow-object-detection-api-b0742b99065d


**Data Augmentation**
- images in your camera feed maybe of lower quality. So you must train your model to work in such conditions.
- https://medium.com/nanonets/how-to-use-deep-learning-when-you-have-limited-data-part-2-data-augmentation-c26971dc8ced
- add some noise to degrade the image quality of the dataset. We could also experiment with blur and erosion effects.


**Datasets**
- Towncenter
  * http://www.robots.ox.ac.uk/ActiveVision/Research/Projects/2009bbenfold_headpose/project.html#datasets
  ```bash
  pip install -r requirements.txt
  sudo apt-get install protobuf-compiler
  #
  protoc object_detection/protos/*.proto --python_out=.
  export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
  #
  python create_tf_record.py \
      --data_dir=`pwd` \
      --output_dir=`pwd`
  #
  python object_detection/train.py \
  --logtostderr \
  --pipeline_config_path=pipeline.config \
  --train_dir=train
  #
  python object_detection/inference.py \
  --input_dir={PATH} \
  --output_dir={PATH} \
  --label_map={PATH} \
  --frozen_graph={PATH} \
  --num_output_classes=1 \
  --n_jobs=1 \
  --delay=0
  ```


**Commercial APIS**
- https://nanonets.com/
- https://github.com/NanoNets/object-detection-sample-python.git


**Pre-trained Models**
- https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md
Download one of these models, and extract the contents into your base directory. You will receive the model checkpoints, a frozen inference graph, and a pipeline.config file.


**SSD**
- https://towardsdatascience.com/understanding-ssd-multibox-real-time-object-detection-in-deep-learning-495ef744fab
  ```bash
  python object_detection/inference.py \
  --input_dir=test_images \
  --output_dir=test_images_output \
  --label_map=annotations/label_map.pbtxt \
  --frozen_graph=output/frozen_inference_graph.pb \
  --num_output_classes=1 \
  --n_jobs=1 \
  --delay=0
  ```

## References
* http://karpathy.github.io/2015/05/21/rnn-effectiveness/
* https://medium.com/@ageitgey/machine-learning-is-fun-part-3-deep-learning-and-convolutional-neural-networks-f40359318721
* https://en.wikipedia.org/wiki/Precision_and_recall
* https://github.com/tflearn/tflearn/tree/master/examples#tflearn-examples
* https://medium.com/@ageitgey/machine-learning-is-fun-part-8-how-to-intentionally-trick-neural-networks-b55da32b7196


**DNN Security**
* Practical Black-Box Attacks against Machine Learning
  * https://arxiv.org/abs/1602.02697


**Object Detections**
* https://tryolabs.com/blog/2017/08/30/object-detection-an-overview-in-the-age-of-deep-learning/
* https://www.descarteslabs.com/
* https://www.tensorflight.com/
* https://github.com/tensorflow/models/tree/master/research/object_detection
* https://deeplearninganalytics.org/blog/do-pixel-wise-classification


## Backbone Networks

### ResNet - Residual Neural Network
* https://medium.com/@sidereal/cnns-architectures-lenet-alexnet-vgg-googlenet-resnet-and-more-666091488df5
* https://towardsdatascience.com/an-overview-of-resnet-and-its-variants-5281e2f56035
* It achieves a top-5 error rate of 3.57% which beats human-level performance on this dataset.
* https://towardsdatascience.com/the-10-coolest-papers-from-cvpr-2018-11cb48585a49


### **[Mask-Rcnn](deep-learning-maskrcnn.md)**

**GeoAI - thoughts about where AI and GIS intersect**
* https://medium.com/geoai


## Pre-training, Transfer Learning
* http://nlp.fast.ai/classification/2018/05/15/introducting-ulmfit.html#transfer
* https://www.analyticsvidhya.com/blog/2017/06/transfer-learning-the-art-of-fine-tuning-a-pre-trained-model/
* https://www.analyticsvidhya.com/blog/2017/05/neural-network-from-scratch-in-python-and-r/
* https://github.com/alexgkendall/caffe-segnet/issues/3
* http://silverpond.com.au/2017/02/17/how-we-built-and-trained-an-ssd-multibox-detector-in-tensorflow.html
* https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/
- https://www.tensorflow.org/hub/tutorials/image_retraining
- https://towardsdatascience.com/a-comprehensive-hands-on-guide-to-transfer-learning-with-real-world-applications-in-deep-learning-212bf3b2f27a
* https://towardsdatascience.com/transfer-learning-and-image-classification-using-keras-on-kaggle-kernels-c76d3b030649
* Well Transfer learning works for Image classification problems because Neural Networks learn in an increasingly complex way. i.e The deeper you go down the network the more image specific features are learnt.
* The take-away here is that the earlier layers of a neural network will always detect the same basic shapes and edges that are present in both the picture of a car and a person.
* There are different variants of pretrained networks each with its own architecture, speed, size, advantages and disadvantages.


**Transfer Learning**
> I mean a person who can boil eggs should know how to boil just water right?

- https://medium.com/nanonets/nanonets-how-to-use-deep-learning-when-you-have-limited-data-f68c0b512cab



**Removing objects**
* https://www.digitalartsonline.co.uk/tutorials/after-effects/remove-moving-objects-from-video
* https://www.dailymail.co.uk/sciencetech/article-5011649/Adobe-Cloak-AI-automatically-removes-objects-video.html
* https://towardsdatascience.com/background-removal-with-deep-learning-c4f2104b3157?gi=ee87561234c9
* https://greenscreen-ai.boorgle.com/
* https://medium.com/@burgalon/deploying-your-keras-model-35648f9dc5fb
* http://www.fast.ai/


**Currently Reading**
* https://tryolabs.com/blog/2018/01/18/faster-r-cnn-down-the-rabbit-hole-of-modern-object-detection/
* https://github.com/tryolabs/luminoth/tree/master/luminoth/models/fasterrcnn


**IoU - Intersection Of Unionn**
- https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/


**Binary Cross Entropy**
- http://rdipietro.github.io/friendly-intro-to-cross-entropy-loss/


**Online Books**
- https://www.deeplearningbook.org/

**CBIR**
- https://blog.insightdatascience.com/the-unreasonable-effectiveness-of-deep-learning-representations-4ce83fc663cf


**Free Online Course**
* http://course.fast.ai/lessons/lesson1.html
  - http://files.fast.ai/setup/paperspace
* https://www.insightdata.ai/
* https://www.insightdatascience.com/


**Cloud Insfrastructure**
* https://www.paperspace.com/
  - https://github.com/reshamas/fastai_deeplearn_part1/blob/master/tools/paperspace.md
* Cloud TPU
  - https://medium.com/swlh/how-to-train-keras-model-x20-times-faster-with-tpu-for-free-cac6cf5089cb
  - https://techcrunch.com/2017/05/17/the-tensorflow-research-cloud-program-gives-the-latest-cloud-tpus-to-scientists/
  - **What is TPU?**
    * https://en.wikipedia.org/wiki/Tensor_processing_unit
    * A tensor processing unit (TPU) is an AI accelerator application-specific integrated circuit (ASIC) developed by Google specifically for neural network machine learning.


**VoxelNet**
*  VoxelNet: End-to-End Learning for Point Cloud Based 3D Object Detection
* https://www.voxelnet.com/
* https://www.mining3.com/research/voxelnet/
* https://github.com/qianguih/voxelnet
* https://github.com/jeasinema/VoxelNet-tensorflow


## Road Segmentation
* https://roadmaps.csail.mit.edu/roadtracer/


## Computer Vision Conferences, Challanges
* http://www.guide2research.com/topconf/computer-vision

* CVPR : IEEE Conference on Computer Vision and Pattern Recognition, CVPR
* **ICCV : IEEE International Conference on Computer Vision**
  - https://en.wikipedia.org/wiki/International_Conference_on_Computer_Vision
* **ECCV : European Conference on Computer Vision**
* **ICIAR : International Conference on Image Analysis and Recognition**

## Research Publications
* **ArXiv**
  - https://en.wikipedia.org/wiki/ArXiv


## Text based DNN
* https://nlp.stanford.edu/projects/glove/
  - GloVe (trained on Wikipedia).
  - https://github.com/hundredblocks/semantic-search


## Tasks

**Challanges**
* to support training on data from multiple sources at the same time


## AI for GIS tools
* https://github.com/ctu-geoforall-lab/i.ann.maskrcnn
* https://github.com/mnboos/osm-instance-segmentation
* https://github.com/ctu-geoforall-lab-projects/dp-pesek-2018
* http://teselagen.github.io/openVectorEditor/#/Editor


**Commercial tool**
* https://oclavi.com/


## **Deep Learning in Autonomy**
* https://www.slideshare.net/yuhuang/3d-interpretation-from-single-2d-image-for-autonomous-driving-121650450
* Topics
  - NMS: Non maximal supression
    - https://arxiv.org/pdf/1705.02950.pdf
  - convert the segmentation mask to polygon
    - https://github.com/cocodataset/cocoapi/issues/39
    - https://docs.opencv.org/trunk/d4/d73/tutorial_py_contours_begin.html
    - https://gist.github.com/hellpanderrr/2c08af0f07eed4782234
    - http://blog.thehumangeo.com/2014/05/12/drawing-boundaries-in-python/
* **Camera based Lane Detection**
  - https://www.slideshare.net/yuhuang/camerabased-lane-detection-by-deep-learning
  - DVCNN - Dual View CNN for accurate lane detection
  - VPGNet - Vanishing Point Guided Network for lane and road marking detection and recogition
  - SCNN - Spatial CNN
    * probability maps of baseline - ReNet, MRFNet, ResNet-101, SCNN


## **Deep Learning: 3D Re-Construction, Analysis**
- https://sites.google.com/site/yorkyuhuang/home/tutorial/deep-learning-1/deeplearningforscenereconstruction
- https://www.slideshare.net/yuhuang/deep-learning-for-3d-scene-reconstruction-and-modeling
* **LIFT**
  - Learned Invariant Feature Transform
  - https://www.eccv2016.org/files/posters/S-4A-08.pdf
* **MatchNet**
  - Matchnet is a deep learning approach for patch-based local image matching
  - http://www.cs.unc.edu/~xufeng/cs/papers/cvpr15-matchnet.pdf
  - https://github.com/hanxf/matchnet
* **PoseNet**
  * https://github.com/tensorflow/tfjs-models/tree/master/posenet
  * https://medium.com/tensorflow/real-time-human-pose-estimation-in-the-browser-with-tensorflow-js-7dd0bc881cd5
* **Pixel2Mesh**
  * https://arxiv.org/pdf/1804.06032.pdf
  * https://github.com/nywang16/Pixel2Mesh
  * TFLearn to be installed
    - http://tflearn.org/installation/
    - `sudo pip install tflearn`
* **Researchers**
  * https://github.com/B-C-WANG?tab=stars
* **Graph CNN**
  * https://github.com/tkipf/gcn
  * http://tkipf.github.io/graph-convolutional-networks/
  * https://www.inference.vc/how-powerful-are-graph-convolutions-review-of-kipf-welling-2016-2/
* **3D-R2N2**
  * https://github.com/chrischoy/3D-R2N2
  * errors:
  AbstractConv2d Theano optimization failed: there is no implementation available supporting the requested options. Did you exclude both "conv_dnn" and "conv_gemm" from the optimizer?



#### CSE291-100

* https://cse291-i.github.io/
* https://github.com/Fire-Sale/Machine-Learning-for-3D-Data/tree/master/Slides
* https://github.com/timzhang642/3D-Machine-Learning


## DeepLearning in Remote Sensing
* [object-detection-with-deep-learning-on-aerial-imagery](https://medium.com/data-from-the-trenches/object-detection-with-deep-learning-on-aerial-imagery-2465078db8a9)
* [car-localization-and-counting-with-overhead-imagery](https://medium.com/the-downlinq/car-localization-and-counting-with-overhead-imagery-an-interactive-exploration-9d5a029a596b)


###**[SpaceNetChallenge](https://github.com/SpaceNetChallenge/)**

* https://medium.com/the-downlinq/getting-started-with-spacenet-data-827fd2ec9f53


####**Building Foorprint Detection**


####**road-detection in Satellite Imagery**

* https://devblogs.nvidia.com/solving-spacenet-road-detection-challenge-deep-learning/


## TBD:
* http://www.themtank.org/a-year-in-computer-vision


## Conventions
* BBOX: Top(y),Left(x),Width,Height,Label


## Adversarial Vision Challanges
* https://medium.com/@wielandbr/reading-list-for-the-nips-2018-adversarial-vision-challenge-63cbac345b2f
* https://ai.googleblog.com/2018/09/introducing-unrestricted-adversarial.html
* https://github.com/google/unrestricted-adversarial-examples
* https://tsenghungchen.github.io/show_adapt_tell/

## Deep Learning Toolkits


### [gluon-cv](https://gluon-cv.mxnet.io/index.html)
* GluonCV: a Deep Learning Toolkit for Computer Vision
* GluonCV provides implementations of state-of-the-art (SOTA) deep learning algorithms in computer vision. It aims to help engineers, researchers, and students quickly prototype products, validate new ideas and learn computer vision.
* GluonCV features:
  * training scripts that reproduce SOTA results reported in latest papers,
  * a large set of pre-trained models,
  * carefully designed APIs and easy to understand implementations,
  * community support.


## Deep Learning Using Keras
* ImageNet: VGGNet, ResNet, Inception, and Xception with Keras
* https://www.pyimagesearch.com/2017/03/20/imagenet-vggnet-resnet-inception-xception-keras/
* https://keras.rstudio.com/reference/application_inception_resnet_v2.html


### [keras-tutorial-using-pre-trained-imagenet-models](https://www.learnopencv.com/keras-tutorial-using-pre-trained-imagenet-models/)
* VGG16
* InceptionV3
* ResNet
* MobileNet
* Xception
* InceptionResNetV2

**a) Loading a Model**
- first import the python module containing the respective models
- load the model architecture
- load the weights for the networks
**b) Loading and pre-processing an image**
- **Load the image.**
  * load the image using any library such as OpenCV, PIL, skimage etc. 
  * This is done using the load_img() function. Keras uses the PIL format for loading images. Thus, the image is in width x height x channels format.
- **Pre-processing**
  * conver the image in the right format - Convert the image from PIL format to Numpy format ( height x width x channels ) using image_to_array() function
  * create network input format: example some networks would accept a 4-dimensional Tensor as an input of the form ( batchsize, height, width, channels)  
  * Based on how the model was trained, image may need to be normalized by subtracting the mean of the ImageNet data or other dataset, because the network would have trained on the images after this pre-processing
  * Preprocess the input by subtracting the mean value from each channel of the images in the batch
**c)Get the Result from Network**
- Get the result & Convert the result to human-readable format


### [keras-tutorial-transfer-learning-using-pre-trained-models](https://www.learnopencv.com/keras-tutorial-transfer-learning-using-pre-trained-models/)

**[Transfer Learning](http://cs231n.github.io/transfer-learning/)**
* ConvNet as fixed feature extractor
* Fine-tuning the ConvNet
* Pretrained models


**When and how to fine-tune?**
1. How do you decide what type of transfer learning you should perform on a new dataset? 
  * 2 most important ones are:
    - a) the size of the new dataset (small or big)
    - b) its similarity to the original dataset (e.g. ImageNet-like in terms of the content of images and the classes, or very different, such as microscope images)
  *  Keeping in mind that ConvNet features are more generic in early layers and more original-dataset-specific in later layers
    * a) New dataset is small and similar to original dataset
      - no fine-tuning due to overfitting concerns
      - the best idea might be to train a linear classifier on the CNN codes
    * b) New dataset is large and similar to the original dataset
      - have more confidence that we won’t overfit if we were to try to fine-tune through the full network
    * c) New dataset is small but very different from the original dataset
      - data is small, it is likely best to only train a linear classifier
      - dataset is very different, it might not be best to train the classifier form the top of the network, which contains more dataset-specific features. Instead, it might work better to train the SVM classifier from activations somewhere earlier in the network
    * d) New dataset is large and very different from the original dataset
      - dataset is very large, we may expect that we can afford to train a ConvNet from scratch
      - in practice it is very often still beneficial to initialize with weights from a pretrained model
      - we would have enough data and confidence to fine-tune through the entire network
2. Practical Advice
  * a) Constraints from pretrained models
    - a pretrained network, you may be slightly constrained in terms of the architecture you can use for your new dataset.
  * b) Learning rates
    -  use a smaller learning rate for ConvNet weights because we expect that the ConvNet weights are relatively good, so we don’t wish to distort them too quickly and too much (especially while the new Linear Classifier above them is being trained from random initialization)
  * **Data pre-processing**
    * PCA/Whitening in these notes for completeness, but these transformations are not used with Convolutional Networks.
    * However, it is very important to zero-center the data, and it is common to see normalization of every pixel as well.
    * An **important point** to make about the preprocessing is that any preprocessing statistics (e.g. the data mean) must only be computed on the training data, and then applied to the validation / test data. E.g. computing the mean and subtracting it from every image across the entire dataset and then splitting the data into train/val/test splits would be a mistake. Instead, the mean must be computed only over the training data and then subtracted equally from all splits (train/val/test).
  * **Weight Initialization**
    * there is no source of asymmetry between neurons if their weights are initialized to be the same
    * we still want the weights to be very close to zero, but, not identically zero
    * it is common to initialize the weights of the neurons to small numbers and refer to doing so as **symmetry breaking**
    * The idea is that the neurons are all random and unique in the beginning, so they will compute distinct updates and integrate themselves as diverse parts of the full network
    * he implementation for one weight matrix might look like `W = 0.01* np.random.randn(D,H)`, where randn samples from a zero mean, unit standard deviation gaussian. With this formulation, every neuron’s weight vector is initialized as a random vector sampled from a multi-dimensional gaussian, so the neurons point in random direction in the input space.
    * It’s not necessarily the case that smaller numbers will work strictly better. For example, a Neural Network layer that has very small weights will during backpropagation compute very small gradients on its data (since this gradient is proportional to the value of the weights). This could greatly diminish the “gradient signal” flowing backward through a network, and could become a concern for deep networks.
    * **Calibrating the variances with 1/sqrt(n)**: One problem with the above suggestion is that the distribution of the outputs from a randomly initialized neuron has a variance that grows with the number of inputs. It turns out that we can normalize the variance of each neuron’s output to 1 by scaling its weight vector by the square root of its fan-in (i.e. its number of inputs). That is, the recommended heuristic is to initialize each neuron’s weight vector as: `w = np.random.randn(n) / sqrt(n)`, where n is the number of its inputs. 
    * gives the initialization `w = np.random.randn(n) * sqrt(2.0/n)`, and is the current recommendation for use in practice in the specific case of neural networks with ReLU neurons.
    * **Sparse initialization**
  * **Initializing the biases**
    * some people like to use small constant value such as 0.01 for all biases because this ensures that all ReLU units fire in the beginning and therefore obtain and propagate some gradient. However, it is not clear if this provides a consistent improvement (in fact some results seem to indicate that this performs worse) and it is more common to simply use 0 bias initialization.
  * http://arxiv-web3.library.cornell.edu/abs/1502.01852
  * In practice, the current recommendation is to use `ReLU` units and use the `w = np.random.randn(n) * sqrt(2.0/n)`
  * **Batch Normalization.**
    * alleviates a lot of headaches with properly initializing neural networks by explicitly forcing the activations throughout a network to take on a unit gaussian distribution at the beginning of the training. 
    * The core observation is that this is possible because normalization is a simple differentiable operation
    *  In the implementation, applying this technique usually amounts to insert the BatchNorm layer immediately after fully connected layers (or convolutional layers), and before non-linearities
    * **it has become a very common practice to use Batch Normalization in neural networks**
    * In practice networks that use Batch Normalization are significantly more robust to bad initialization
    * batch normalization can be interpreted as doing preprocessing at every layer of the network, but integrated into the network itself in a differentiable manner
* **Regularization** - ways of controlling the capacity of Neural Networks to **prevent overfitting**
  * **L2 regularization**
    - implemented by penalizing the squared magnitude of all parameters directly in the objective
    - The L2 regularization has the intuitive interpretation of heavily penalizing peaky weight vectors and preferring diffuse weight vectors
    - L2 loss is much harder to optimize than a more stable loss such as softmax
    - the L2 loss is less robust because outliers can introduce huge gradients.
  * **L1 regularization**
    -  has the intriguing property that it leads the weight vectors to become sparse during optimization (i.e. very close to exactly zero).
    - In other words, neurons with L1 regularization end up using only a sparse subset of their most important inputs and become nearly invariant to the “noisy” inputs
    - final weight vectors from L2 regularization are usually diffuse, small numbers
  * **Elastic net regularization**
    - combine the L1 regularization with the L2 regularization
  * **Max norm constraints**
    -  One of its appealing properties is that network cannot “explode” even when the learning rates are set too high because the updates are always bounded.
  * **Dropout**
    - extremely effective, simple
    - While training, dropout is implemented by only keeping a neuron active with some probability p (a hyperparameter), or setting it to zero otherwise
    - During training, Dropout can be interpreted as sampling a Neural Network within the full Neural Network, and only updating the parameters of the sampled network based on the input data. 
  * stochastic pooling, fractional pooling, and data augmentation
  * **Bias regularization**
    *  it is not common to regularize the bias parameters because they do not interact with the data through multiplicative interactions, and therefore do not have the interpretation of controlling the influence of a data dimension on the final objective
    * Regularizing the bias rarely leads to significantly worse performance. This is likely because there are very few bias terms compared to all the weights, so the classifier can “afford to” use the biases if it needs them to obtain a better data loss.
  * **Per-layer regularization**
    * not very common to regularize different layers to different amounts
  * **In practice**
    * It is most common to use a single, global L2 regularization strength that is cross-validated. It is also common to combine this with dropout applied after all layers. The value of p=0.5 is a reasonable default, but this can be tuned on validation data.
* **Loss functions**
  * **data loss**,  in a supervised learning problem measures the compatibility between a prediction (e.g. the class scores in classification) and the ground truth label. 
  * The data loss takes the form of an average over the data losses for every individual example.
  * Squared hinge loss
  * cross-entropy loss (used by Softmax classifier)
  * Hierarchical Softmax
  * with Softmax, where the precise value of each score is less important: It only matters that their magnitudes are appropriate
  * structured SVM loss
*  **Regression**
  * is the task of predicting real-valued quantities, such as the price of houses or the length of something in an image
  * it is common to compute the loss between the predicted quantity and the true answer and then measure the L2 squared norm, or L1 norm of the difference
  * When faced with a regression problem, first consider if it is absolutely inadequate to quantize the output into bins. For example, if you are predicting star rating for a product, it might work much better to use 5 independent classifiers for ratings of 1-5 stars instead of a regression loss. Classification has the additional benefit that it can give you a distribution over the regression outputs, not just a single output with no indication of its confidence.


**Data Pre-processing**
* http://cs231n.github.io/neural-networks-2/
* **Mean subtraction**
  * It involves subtracting the mean across every individual feature in the data
  * has the geometric interpretation of centering the cloud of data around the origin along every dimension
  *  In numpy, this operation would be implemented as: `X -= np.mean(X, axis = 0)`. With images specifically, for convenience it can be common to subtract a single value from all pixels (e.g. `X -= np.mean(X))`, or to do so separately across the three color channels.
* **Normalization**
  * normalizing the data dimensions so that they are of approximately the same scale
  * There are two common ways of achieving this normalization
    * a) One is to divide each dimension by its standard deviation, once it has been zero-centered: `(X /= np.std(X, axis = 0))`
    * b) Another form of this preprocessing normalizes each dimension so that the min and max along the dimension is -1 and 1 respectively
  -  It only makes sense to apply this preprocessing if you have a reason to believe that different input features have different scales (or units), but they should be of approximately equal importance to the learning algorithm
  - In case of images, the relative scales of pixels are already approximately equal (and in range from 0 to 255), so it is not strictly necessary to perform this additional preprocessing step.
* **PCA (Principal Component Analysis) and Whitening**
  * used for dimensionality reduction
  * the data is first centered
  * compute the covariance matrix that tells us about the correlation structure in the data
  * The (i,j) element of the data covariance matrix contains the covariance between i-th and j-th dimension of the data
  * the diagonal of this matrix contains the variances
  * the covariance matrix is symmetric and positive semi-definite
  * compute the **singular-value decomposition - SVD** factorization of the data covariance matrix
  * where the columns of U are the eigenvectors and S is a 1-D array of the singular values.
  * To decorrelate the data, we project the original (but zero-centered) data into the eigenbasis
  * Notice that the columns of U are a set of orthonormal vectors (norm of 1, and orthogonal to each other), so they can be regarded as basis vectors
  ```python
  # Assume input data matrix X of size [N x D]
  X -= np.mean(X, axis = 0) # zero-center the data (important)
  cov = np.dot(X.T, X) / X.shape[0] # get the data covariance matrix
  #
  U,S,V = np.linalg.svd(cov)
  #
  Xrot = np.dot(X, U) # decorrelate the data
  Xrot_reduced = np.dot(X, U[:,:100]) # Xrot_reduced becomes [N x 100]
  ```
  * After this operation, we would have reduced the original dataset of size [N x D] to one of size [N x 100], keeping the 100 dimensions of the data that contain the most variance
  * It is very often the case that you can get very good performance by training linear classifiers or neural networks on the PCA-reduced datasets, obtaining savings in both space and time
  * **whitening**
    * The whitening operation takes the data in the eigenbasis and divides every dimension by the eigenvalue to normalize the scale
    * The geometric interpretation of this transformation is that if the input data is a multivariable gaussian, then the whitened data will be a gaussian with zero mean and identity covariance matrix.
    ```python
    # whiten the data:
    # divide by the eigenvalues (which are square roots of the singular values)
    Xwhite = Xrot / np.sqrt(S + 1e-5)
    ```
    * Exaggerating noise. Note that we’re adding 1e-5 (or a small constant) to prevent division by zero. One weakness of this transformation is that it can greatly exaggerate the noise in the data, since it stretches all dimensions (including the irrelevant dimensions of tiny variance that are mostly noise) to be of equal size in the input. This can in practice be mitigated by stronger smoothing (i.e. increasing 1e-5 to be a larger number).


**process of learning the parameters and finding good hyperparameters**
* http://cs231n.github.io/neural-networks-3/
* **Gradient Checks**
  * Use the centered formula
  * Use relative error for the comparison
  * Use double precision
  * Stick around active range of floating point
    * http://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html
  * Kinks in the objective
    * Kinks refer to non-differentiable parts of an objective function, introduced by functions such as ReLU (max(0,x)), or the SVM loss, Maxout neurons, etc
  * Use only few datapoints
  * Be careful with the step size h
  * Gradcheck during a “characteristic” mode of operation
  * Don’t let the regularization overwhelm the data
  * Remember to turn off dropout/augmentations
  * Check only few dimensions
* **Before learning: sanity checks Tips/Tricks**
  * Look for correct loss at chance performance
  * increasing the regularization strength should increase the loss
  * Overfit a tiny subset of data
    - Lastly and most importantly, before training on the full dataset try to train on a tiny portion (e.g. 20 examples) of your data and make sure you can achieve zero cost. For this experiment it’s also best to set regularization to zero, otherwise this can prevent you from getting zero cost. Unless you pass this sanity check with a small dataset it is not worth proceeding to the full dataset.
    - For instance, if your datapoints’ features are random due to some bug, then it will be possible to overfit your small training set but you will never notice any generalization when you fold it your full dataset.
* **Quantities to monitor during training Neural Network**
  * get intuitions about different hyperparameter settings and how they should be changed for more efficient learning
  * The x-axis of the plots below are always in units of epochs, which measure **how many times every example has been seen** during training in expectation (e.g. one epoch means that every example has been seen once)
  * It is preferable to track epochs rather than iterations since the number of iterations depends on the arbitrary setting of batch size.
  * **Loss**
    * The first quantity that is useful to track during training is the loss
    * it is evaluated on the individual batches during the forward pass
    * With low learning rates the improvements will be linear
    * With high learning rates they will start to look more exponential
    * Higher learning rates will decay the loss faster, but they get stuck at worse values of loss. This is because there is too much "energy" in the optimization and the parameters are bouncing around chaotically, unable to settle in a nice spot in the optimization landscape
    * The amount of “wiggle” in the loss is related to the batch size
    * When the batch size is 1, the wiggle will be relatively high
    * When the batch size is the full dataset, the wiggle will be minimal because every gradient update should be improving the loss function monotonically (unless the learning rate is set too high).
    * https://lossfunctions.tumblr.com/
  * **Train/Val accuracy**
    * plot can give you valuable insights into the amount of overfitting in your model
    * The gap between the training and validation accuracy indicates the amount of overfitting
    * very small validation accuracy compared to the training accuracy, indicating strong overfitting (note, it's possible for the validation accuracy to even start to go down after some point). When you see this in practice you probably want to increase regularization (stronger L2 weight penalty, more dropout, etc.) or collect more data.
    * The other possible case is when the validation accuracy tracks the training accuracy fairly well. This case indicates that your model capacity is not high enough: make the model larger by increasing the number of parameters
  * **Ratio of weights:updates**
    * track the ratio of the update magnitudes to the value magnitudes. Note: updates, not the raw gradients (e.g. in vanilla sgd this would be the gradient multiplied by the learning rate)
    * You might want to evaluate and track this ratio for every set of parameters independently
    * A rough heuristic is that this ratio should be somewhere around `1e-3`. If it is lower than this then the learning rate might be too low. If it is higher then the learning rate is likely too high.
  * **Activation / Gradient distributions per layer**
    * An incorrect initialization can slow down or even completely stall the learning process
    * plot activation/gradient histograms for all layers of the network
    * Intuitively, it is not a good sign to see any strange distributions - e.g. with tanh neurons we would like to see a distribution of neuron activations between the full range of [-1,1], instead of seeing all neurons outputting zero, or all neurons being completely saturated at either -1 or 1
  * **First-layer Visualizations**
    * when one is working with image pixels it can be helpful and satisfying to plot the first-layer features visually
    * Noisy features indicate could be a symptom: Unconverged network, improperly set learning rate, very low weight regularization penalty
    * Nice, smooth, clean and diverse features are a good indication that the training is proceeding well


**Parameter updates**
Once the analytic gradient is computed with backpropagation, the gradients are used to perform a parameter update. There are several approaches for performing the update:
* **Vanilla update**
  * The simplest form of update is to change the parameters along the negative gradient direction (since the gradient indicates the direction of increase, but we usually wish to minimize a loss function).
  ```python
      # Vanilla update
    x += - learning_rate * dx
  ```
  * where `learning_rate` is a hyperparameter - a fixed constant. When evaluated on the full dataset, and when the learning rate is low enough, this is guaranteed to make non-negative progress on the loss function.
* **Momentum update**
  * enjoys better converge rates on deep networks
  * motivated from a physical perspective of the optimization problem
  * In particular, the loss can be interpreted as the height of a hilly terrain (and therefore also to the potential energy since U=mgh and therefore U∝h )
  * Initializing the parameters with random numbers is equivalent to setting a particle with zero initial velocity at some location
  * The optimization process can then be seen as equivalent to the process of simulating the parameter vector (i.e. a particle) as rolling on the landscape
  *  A typical setting is to start with momentum of about 0.5 and anneal it to 0.99 or so over multiple epochs.
* **Nesterov Momentum**
  * consistenly works slightly better than standard momentum
  * Instead of evaluating gradient at the current position (red circle), we know that our momentum is about to carry us to the tip of the green arrow. With Nesterov momentum we therefore instead evaluate the gradient at this "looked-ahead" position
* **Annealing the learning rate**
  * it is usually helpful to anneal the learning rate over time
  * Good intuition to have in mind is that with a high learning rate, the system contains too much kinetic energy and the parameter vector bounces around chaotically, unable to settle down into deeper, but narrower parts of the loss function. Knowing when to decay the learning rate can be tricky: Decay it slowly and you’ll be wasting computation bouncing around chaotically with little improvement for a long time. But decay it too aggressively and the system will cool too quickly, unable to reach the best position it can. There are three common types of implementing the learning rate decay:
    * **Step decay:**
    * **Exponential decay:**
    * **1/t decay:**
  * In practice, we find that the step decay is slightly preferable because the hyperparameters it involves (the fraction of decay and the step timings in units of epochs) are more interpretable than the hyperparameter k. Lastly, if you can afford the computational budget, err on the side of slower decay and train for a longer time
* **Second order methods**
  *  [L-BFGS](http://en.wikipedia.org/wiki/Limited-memory_BFGS) to work on mini-batches is more tricky and an active area of research
  * SGD variants based on (Nesterov’s) momentum are more standard because they are simpler and scale more easily
* **Per-parameter adaptive learning rate methods**
  * generally the learning rate are manipulated globally and equally for all parameters
  * Tuning the learning rates is an expensive process
  * adaptive methods:
    * **Adagrad** is an adaptive learning rate method 
    * **RMSprop** is a very effective
    * **Adam** looks a bit like RMSProp with momentum
* **Hyperparameter optimization**
  * The most common hyperparameters in context of Neural Networks include:
    * the initial learning rate
    * learning rate decay schedule (such as the decay constant)
    * regularization strength (L2 penalty, dropout strength)
  * there are many more relatively less sensitive hyperparameters, for example:
    * in per-parameter adaptive learning methods
    * the setting of momentum and its schedule, etc.
  * ** tips and tricks for performing the hyperparameter search:**
    * **Implementation**
      - writes a model checkpoints (together with miscellaneous training statistics such as the loss over time) to a file
      - useful to include the validation performance directly in the filename, so that it is simple to inspect and sort the progress
      - inspect the checkpoints &  plot their training statistics, etc
    * **Prefer one validation fold to cross-validation**
      - In most cases a **single validation set** of respectable size substantially simplifies the code base, without the need for cross-validation with multiple folds
    * **Hyperparameter ranges**
      - Search for hyperparameters on log scale
      - Learning rate and regularization strength have multiplicative effects on the training dynamics. For example, a fixed change of adding 0.01 to a learning rate has huge effects on the dynamics if the learning rate is 0.001, but nearly no effect if the learning rate when it is 10. This is because the learning rate multiplies the computed gradient in the update.
      - Therefore, it is much more natural to consider a range of learning rate multiplied or divided by some value, than a range of learning rate added or subtracted to by some value. Some parameters (e.g. dropout) are instead usually searched in the original scale
    * **Prefer random search to grid search**
      - randomly chosen trials are more efficient for hyper-parameter optimization than trials on a grid
      -  Performing random search rather than grid search allows you to much more precisely discover good values for the important ones.
* **Evaluation**




### Exercises

1. **Reading, Writing & Converting Images**
  * Loading images using different libraries such as OpenCV, PIL, skimage etc
  * handle image arrays to-and-fro between different image libraries
  * convert loaded images into numpy array
  * convert numpy image array into network input format
  * saving numpy image array to image, visualize images
2. **Manipulate Numpy Image array**
  * Calculate Mean of Image
  * Subract Mean of Image, visualiize and save the new array to new image
  * Image re-size, padding, splitting
  * RBG to grey channel
  * visualize histograms of RGB channels, observe and analyze image highlights, midtownes, exposure and other properties from the image graphs


**Notes:**
* Numpy format  ( height x width x channels[RGB] )
* Keras format  ( width x height x channels[RGB] )
* OpenCV format ( height x width x channels[BGR] )
* Mean is an array of three elements obtained by the average of R, G, B pixels of all images


## TBD
* http://www.senseforth.ai/
* https://online.stanford.edu/
* https://online.stanford.edu/courses