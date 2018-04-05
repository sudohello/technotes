/*
Title: ISLR Book Notes
Decription: ISLR Book Notes
Author: Bhaskar Mangal
Date: 
Tags: ISLR Book Notes
*/

# ISLR book notes
> Introduction to Statistical Learning Using R

Statistical learning has emerged as a new subfield in statistics, focused on supervised and unsupervised modeling and prediction

## Terms & keywords
* continuous or quantitative output value.
* regression problem
* linear regression- is used for predicting quantitative values
* linear discriminant analysis
* logistic regression
* generalized linear models - for an entire class of statistical learning methods that include both linear and logistic regression as special cases
* generalized additive models - for a class of non-linear extensions to generalized linear models
* non-linear relationship
* categorical or qualitative output
* classification problem
* classification and regression trees
* quadratic discriminant analysis model
* clustering problem - grouping individuals according to their observed characteristics
* principal components
* clustering analysis
* K-nearest neighbor classifier
* training data
* thin-plate spline
* flexible
* tran or fit
* overfitting
* confidence interval
* prediction intervals
* irreducible error
* reducible error
* error term
* population regression line/plane
* Model Bias
* SVM - Support Vector Machines
* hinge loss

# Unsupervised learning
The goal is to discover interesting things about the measurements on X~1~, X~2~, ...,X~p~
**Is there an informative way to visualize the data?**
**Can we discover subgroups among the variables or among the observations?**
Unsupervised learning refers to a diverse set of techniques for answering questions such as these.
* Unsupervised learning is often performed as part of an exploratory data analysis.

Two particular types of unsupervised learning:
* **principal components analysis**, a tool used for data visualization or data pre-processing before supervised techniques are applied.
* **clustering**, a broad class of methods for discovering unknown subgroups in data.

## Principal component analysis (PCA)
- PCA refers to the process by which principal components are computed, and the subsequent use of these components in understanding the data.
- PCA is an unsupervised approach, since it involves only a set of features X~1~, X~2~, ...,X~p~, and no associated response Y.
- Produce derived variables for use in supervised learning problems
- a tool for data visualization (visualization of the observations or visualization of the variables)
- we would like to find a low-dimensional representation of the data that captures as much of the information as possible; then we can plot the observations in this low-dimensional space.
- PCA provides a tool to find a low-dimensional representation of a data set that contains as much as possible of the variation.
- The idea is that each of the n observations lives in p-dimensional space, but not all of these dimensions are equally interesting.
- the concept of interesting is measured by the amount that the observations vary along each dimension.
- **first principal component** of a set of features  X~1~, X~2~, ...,X~p~ is the normalized linear combination of the features
- Given a n × p data set X, how do we compute the first principal component? Since we are only interested in variance, we assume that **each of the variables in X has been centered to have mean zero** (that is, the column means of X are zero).
- https://www.youtube.com/watch?v=WaHQ9-UXIIg&feature=youtu.be&t=25s
- After the first principal component Z~1~ of the features has been determined, we can find the second principal component Z~2~. The second principal component is the linear combination of X~1~,...,X~p~ that has maximal variance out of all linear combinations that are uncorrelated with Z~1~
- Principal component load and pricipal component score
- PCA looks to find a low-dimensional representation of the observations that explain a good fraction of the variance;

## Clustering
- Clustering looks to find homogeneous subgroups among the observations.
- the two best-known clustering approaches:
	- K-means clustering
	- Hierarchical clustering
- Cluster features
	- on the basis of observations
	- identify subgroups amonth the features
- Cluster observations
	- on the basis of features
	- identify subgroups among the observations


### K-means clustering
- Number of clusters are pre-defined
- partitioning a data set into K distinct, non-overlapping clusters.
- a good clustering is one for which the within-cluster variation is as small as possible
- We want to partition the observations into K clusters such that the total within-cluster variation, summed over all K clusters, is as small as possible
- THere are many possible ways to define within-cluster variation. THe most common choice is **squared Euclidean distance**
- The within-cluster variation for the kth cluster is the sum of all of the pairwise squared Euclidean distances between the observations in the kth cluster, divided by the total number of observations in the kth cluster.
- since there are almost K^n^ ways to partition `n` observations into `K` clusters. This is a huge number unless K and n are tiny!
- The cluster centroids are computed as the mean of the observations assigned to each cluster.
- K-means algorithm finds a local rather than a global optimum
- The problem of selecting K is far from simple

### Hierarchical clustering
- NUmber of clusters are not known
- Output is a tree-like visual representation of the observations, called a **dendrogram**
- dendrogram that allows us to view at once the clusterings obtained for each possible number of clusters, from 1 to n.
- most common type of hierarchical clustering **bottom-up or agglomerative clustering**; dendrogram is generally depicted as an upside-down tree.

**How the dendrogram is built?**
**How to interpret a dendrogram?**
- As we move up the dendrogram, some leaves begin to fuse into branches. These correspond to observations that are similar to each other.
- As we move higher up the tree, branches themselves fuse, either with leaves or other branches. The earlier (lower in the tree) fusions occur, the more similar the groups of observations are to each other. On the other hand, observations that fuse later (near the top of the tree) can be quite different.
- look for the point in the tree where branches containing those two observations are first fused. The height of this fusion, as measured on the vertical axis, indicates how different the two observations are.
- Thus, observations that fuse at the very bottom of the tree are quite similar to each other, whereas observations that fuse close to the top of the tree will tend to be quite different.
- hierarchical clustering can sometimes yield worse (i.e. less accurate) results than K-means clustering for a given number of clusters.
- We have a concept of the dissimilarity between pairs of observations, but how do we define the dissimilarity between two clusters if one or both of the clusters contains multiple observations? The concept of dissimilarity between a pair of observations needs to be extended to a pair of groups of observations. This extension is achieved by developing the notion of linkage, which defines the dissimilarity between two groups of observations. The four most common types of linkage—complete, average, single, and centroid.


# Supervised learning
In the supervised learning setting, we typically have access to a set of p features X~1~, X~2~, ...,X~p~, measured on n observations, and a response Y also measured on those same n observations. The goal is then to predict Y using X~1~, X~2~, ...,X~p~.

**Methods:**
* regression
* classification

## Classical linear methods for regression and classification

* logistic regression
* linear discriminant analysis
* Linear regression is used for predicting quantitative values
* Fisher proposed linear discriminant analysis in 1936
* At the beginning of the nineteenth century, Legendre and Gauss published papers on the method of least squares, which implemented the earliest form of what is now known as linear regression
* model, intuition, assumptions, and trade-offs behind each of the methods
* applying statistical learning methods to real-world problems one elementary course in statistics: Background in linear regression; problem - choosing the best method for a given application; cross-validation and the bootstrap, which can be used to estimate the accuracy of a number of different methods
* reducible error
* irreducible error
* principal components analysis, K-means clustering, and hierarchical clustering
* The inputs go by different names, such as predictors, independent variables, features, or sometimes just variablesThe output variable—in often called the response or dependent variable
* In general, as the flexibility of a method increases, its interpretability decreases.
* Principal components regression
* Linear regression
	* Assumption: Relationship between predictors and response is additive and linear
	* The linear assumption states that the change in the response of Y due to one-unti change in X~j~ is constant regardless of the value of X~j~
	* It also means that the effect of change in a predictor X~j~ is independent of the values of the other predictors.
* **interaction term** (X~1~X~2~) removes the additive nature of the linear regression
* Logistic regression
* Lasso
* Stepwise selection
* Ridge regression
* Partial least squares
* Least Squares
* Generalized Additive Models (GAMs) Trees
* Bagging
* Boosting
* Support Vector Machines
* Model example:
**Y = f (X) + e**
	- error term
	- f represents the systematic information that X provides about Y
	- f is some fixed but unknown function
	- f that connects the input variable to the output variable is in general unknown.
	- one must estimate f based on the observed points
	- overall, the errors have approximately mean zero
	- In general, the function f may involve more than one input variable
	- statistical learning refers to a set of approaches for estimating f
	- tools for evaluating the estimates obtained
	- we may wish to estimate f : prediction and inference, or a combination of the two
	- Depending on whether our ultimate goal is prediction, inference, or a combination of the two, different methods for estimating f may be appropriate
* We will always assume that we have observed a set of ***n*** different data points
* observations are called the **training data** because these observations are used to train, or teach, our method how to estimate f
* most statistical learning methods for this task can be characterized as either **parametric** or **non-parametric**. We now briefly discuss these two types of approaches
* The model-based approach is referred to as parametric; it reduces the problem of estimating f down to one of estimating a set of parameters
* fitting a more flexible model requires estimating a greater number of parameters
* These more complex models can lead to a phenomenon known as overfitting the data, which essentially means they follow the errors, or noise, too closely.
* Non-parametric methods do not make explicit assumptions about the functional form of f . Instead they seek an estimate of f that gets as close to the data points as possible without being too rough or wiggly.

++**Prediction**++
- f is treated as a black box
- Y depends on two quantities, which we will call the reducible error and the irreducible error
- Y is also a function of , which, by definition, cannot be predicted using X
- The quantity  may con-tain unmeasured variables that are useful in predicting Y : since we don’t measure them, f cannot use them for its prediction. The quantity  may also contain unmeasurable variation
- the irreducible error will always provide an upper bound on the accuracy of our prediction for Y. This bound is almost always unknown in practice

++**Inference**++
- understand the relationship between X and Y , or more specifically, to understand how Y changes as a function of X 1 , . . . , X p
- f cannot be treated as a black box
- Which predictors are associated with the response?
- What is the relationship between the response and each predictor?
- Can the relationship between Y and each predictor be adequately summarized using a linear equation, or is the relationship more complicated?

++**Problem Statements**++
* Determine that here is an association between advertising and sales
	- goal is to develop an accurate model that can be used to predict sales on the basis of the TV , radio , and newspaper media budgets

* a plot of income versus years of education
	- predict income using years of education

* a plot income as a function of years of education and seniority
	- f is a two-dimensional surface that must be estimated based on the observed data

* From the blood sample, predict patient’s risk for a severe adverse reaction to a particular drug
	- X(1,2...p) are characteristics of a patient’s blood sample measured in a lab for N patients. Y is a variable encoding the patient’s risk for a severe adverse reaction to a particular drug i.e. patients for whom the estimate of Y is high. Predict Y given X for N patients.

* A company that is interested in conducting a direct-marketing campaig. For the campaign to be effective, identify individuals who will respond positively to a mailing, based on observations of demographic variables measured on each individual. The company simply wants an accurate model to predict the response using the predictors and  not interested in obtaining a deep understanding of the relationships between each individual predictor and the response. (modeling for prediction)
	- the demographic variables serve as predictors
	- response to the marketing campaign (either positive or negative) serves as the outcome

* Advertising data, to answer (modeling for inference)
	- Which media contribute to sales?
	- Which media generate the biggest boost in sales?
	- How much increase in sales is associated with a given increase in TV advertising?

**(modeling for inference)**
* Involves modeling the brand of a product that a customer might purchase based on variables such as price, store location, discount levels, competition price, and so forth.
	- How each of the individual variables affects the probability of purchase?
	  - What effect will changing the price of a product have on sales?

**(modeling both for prediction and inference)**
* real estate setting, one may seek to relate values of homes to inputs such as crime rate, zoning, distance from a river, air quality, schools, income level of community, size of houses, and so forth.
	- how much extra will a house be worth if it has a view of the river? (**inference problem**)
	- predicting the value of a home given its characteristics: is this house under- or over-valued? (**prediction problem**)


* non-linear methods
	- tree-based methods,
	- including bagging, boosting, and random forests. Support vector machines, a set of approaches for performing both linear and non-linear classification,


* Q. why would we ever choose to use a more restrictive method instead of a very flexible approach?

**Supervised v/s Unsupervised Learning**
- For each observation of the predictor measurement(s) x i , i = 1, . . . , n there is an associated response measurement y i . We wish to fit a model that relates the response to the predictors, with the aim of accurately predicting the response for future observations (prediction) or better understanding the relationship between the response and the predictors (inference).

- unsupervised learning describes the somewhat more challenging situation in which for every observation i = 1, . . . , n, we observe a vector of measurements x i but no associated response y i . It is not possible to fit a linear regression model, since there is no response variableto predict. In this setting, we are in some sense working blind; the situation is referred to as unsupervised because we lack a response variable that can supervise our analysis.
- cluster analysis, or clustering
- The goal of cluster analysis is to ascertain, on the basis of x 1 , . . . , x n , whether the observations fall into relatively distinct groups

**Semi-supervised Learning**
- In this setting, we wish to use a statistical learning method that can incorporate the m observations for which response measurements are available as well as the n − m observations for which they are not.

market segmentation study
- we might observe multiple characteristics (variables) for potential customers
- zip code, family income, and shopping habits
- believe that the customers fall into different groups, such as big spenders versus low spenders.
- If the information about each customer’s spending patterns were available, then a supervised analysis would be possible.
- However, this information is not available—that is, we do not know whether each potential customer is a big spender or not.
- we can try to cluster the customers on the basis of the variables measured, in order to identify distinct groups of potential customers.


**Regression v/s Classification Problems**
Variables can be characterized as either:
- Quantitative - take on numerical values
- Or, Qualitative (also known as categorical) - take on values in one of K different classes, or categories
- We tend to refer to problems with a quantitative response as regression problems
- while those involving a qualitative response are often referred to as classification problems.

We tend to select statistical learning methods on the basis of whether the response is quantitative or qualitative; i.e. we might use linear regression when quantitative and logistic regression when qualitative. However, whether the predictors are qualitative or quantitative is generally considered less important.

++**Measuring the Quality of Fit**++
- we need to quantify the extent to which the predicted response value for a given observation is close to the true response value for that observation.
- In the regression setting, the most commonly-used measure is the **mean squared error (MSE)**.
- we are interested in the accuracy of the predictions that we obtain when we apply our method to previously unseen test data.
- We want to choose the method that gives the lowest test MSE, as opposed to the lowest training MSE.

average training MSE as a function of flexibility, or more formally the degrees of freedom, for a number of smoothing splines
The degrees of freedom is a quantity that summarizes the flexibility of a curve;

As the flexibility of the statistical learning method increases, we chobserve a monotone decrease in the training MSE and a U-shape in the test MSE. This is a fundamental property of statistical learning that holds regardless of the particular data set at hand and regardless of the statistical method being used.

When a given method yields a small training MSE but a large test MSE, we are said to be overfitting the data. This happens because our statistical learning procedure is working too hard to find patterns in the training data, and may be picking up some patterns that are just caused by random chance rather than by true properties of the unknown function f.

Regardless of whether or not overfitting has occurred, we almost always expect the training MSE to be smaller than the test MSE because most statistical learning methods either directly or indirectly seek to minimize the training MSE.

**Estimating test MSE using the training data**
- cross-validation - is a way to estimate the test MSE using the training data

++**The Bias-Variance Trade-Off**++
- The U-shape observed in the test MSE curves (Figures 2.9–2.11) turns out to be the result of two competing properties of statistical learning methods.
- the expected test MSE, for a given value x 0 , can always be decomposed into the sum of three fundamental quantities: the variance of fˆ (x 0 ), the squared bias of f ˆ (x 0 ) and the variance of the error terms ***e***

**What do we mean by the variance and bias of a statistical learning method?**
Good test set performance of a statistical learning method requires low variance as well as low squared bias. This is referred to as a trade-off because it is easy to obtain a method with extremely low bias but high variance (for instance, by drawing a curve that passes through every single training observation) or a method with very low variance but high bias (by fitting a horizontal line to the data). The challenge lies in finding a method for which both the variance and the squared bias are low.

- Variance refers to the amount by which f ˆ would change if we estimated it using a different training data set.
- if a method has high variance then small changes in the training data can result in large changes in fˆ
- On the other hand, bias refers to the error that is introduced by approximating a real-life problem, which may be extremely complicated, by a much simpler model.
- As a general rule, as we use more flexible methods, the variance will increase and the bias will decrease.


**The Classification Setting**
- The most common approach for quantifying the accuracy of our estimate fˆ is the training error rate, the proportion of mistakes that are made if we apply our estimate f ˆ to the training observations
- **Training Error Rate & Test Error Rate**
	- computes the fraction of incorrect classifications
- **Indicator Variable**

- **Bayes classifier**: test error rate is minimized, on average, by a classifier that assigns each observation to the most likely class, given its predictor values.
	- conditional probilility
	- predictor vector (Pr)
	- Bayes decision boundary
	- The Bayes classifier produces the lowest possible test error rate, called the Bayes error rate
	- The Bayes error rate is analogous to the irreducible error
	- Bayes classifier serves as an unattainable gold standard against which to compare other methods
- **K-nearest neighbors (KNN) classifier**


- In both the regression and classification settings, choosing the correct level of flexibility is critical to the success of any statistical learning method. The bias-variance tradeoff, and the resulting U-shape in the test error, can make this a difficult task
	- various methods for estimating test error rates
	- choosing the optimal level of flexibility for a given statistical learning method.

**Types of Graphs**
- scatter plots
- contour plots
- box plots
- histograms

## Linear Regression
* very simple approach for supervised learning
* linear regression is a useful tool for predicting a quantitative response
* widely used statistical learning method


Suppose that in our role as statistical consultants we are asked to suggest, on the basis of this data, a marketing plan for next year that will result in high product sales. What information would be useful in order to provide such a recommendation?

>a synergy effect, while in statistics it is called an interaction effect.

`“≈” as “is approximately modeled as”.`

>Y ≈ β~0~ + β~1~ X
>
>ŷ = β̂~0~ + β̂~1~x
>where, ŷ indicates a prediction of Y on the basis of X = x
>called as **Least Square Regression Line**

>sales ≈ β~0~ + β~1~× TV

- regression of Y onto X (Y is to X)
- regression of sales onto TV (sales is to TV)
- β̂~0~ and β̂~1~ are two unknown constants that represent the intercept and slope terms in the linear model. Together, β̂~0~ and β̂~1~ are known as the model coefficients or parameters.
- coefficient β̂~0~ and β̂~1~ are Least Square Regression Coefficients
- Use training data to produce estimates β̂~0~ and β̂~1~ for the model coefficients
- Given ***n*** observation pairs, each of which consists of a measurement of X and a measurement of Y
- goal is to obtain coefficient estimates β̂~0~ and β̂~1~ such that the linear model
(3.1) fits the available data well—that is, so that
>y~i~ ≈ β̂~0~ + β̂~1~ x~i~
>for i = 1, . . . , n.
- we want to find an intercept β̂~0~ and a slope β̂~1~ such that the resulting line is as close as possible to the n = 200 data points.
- number of ways of measuring closeness, most common approach involves minimizing the least squares criterion
- e~i~ = y~i~ − ŷ~i~ represents the ith residual—this is the difference between the ith observed response value and the ith response value that is predicted by our linear model.
- **Residual Sum of Squares (RSS)** as
>RSS = e~1~^2^ + e~2~^2^ + ... + e~n~^2^

We assume that the true relationship between X and Y takes the form `Y = f(X) + e` for some unknown function f , where ***e*** is a mean-zero random error term. If f is to be approximated by a linear function, then we can write this relationship as:
>Y = β~0~ + β~1~X + e
**population regression line**, which is the best linear approximation to the true relationship between X and Y

Here,
* ++β~0~ is the intercept term++ — that is, the expected value of Y when X = 0
* ++β~1~ is the slope++ — the average increase in Y associated with a one-unit increase in X
* ++***e*** is the error term++ — It is a catch-all for what we miss with this simple model: the true relationship is probably not linear, there may be other variables that cause variation in Y , and there may be measurement error. We typically assume that the error term is independent of X.

- in real applications, we have access to a set of observations from which we can compute the least squares line; however, the population regression line is unobserved
- The sample mean and the population mean are different, but in general the sample mean will provide a good estimate of the population mean.
- The analogy between linear regression and estimation of the mean of a random variable is an apt one based on the concept of bias
- an unbiased estimator does not systematically over- or under-estimate the true parameter
- The average of μ̂’s over many data sets will be very close to μ, but that a single estimate μ̂ may be a substantial underestimate or overestimate of μ
- we answer this question by computing the **standard error** of μ̂, written as SE(μ̂)
>Var(μ̂) = SE(μ̂)^2^ = σ^2^/n
>**standard error**
>How far off will that single estimate of μ̂ (sample mean) be from μ (popullation mean)?
>where, σ is the **standard deviation** of each of the realizations y~i~ of Y
>* the standard error tells us the average amount that this estimate μ̂ differs from the actual value of μ.
>* also tells us how this deviation shrinks with n—the more observations we have, the smaller the standard error of μ̂.

- **Residual Standard Error (RSE)**
	- it is the average amount that the response will deviate from the true regression line
	- The RSE provides an absolute measure of lack of fit of the model to the data.
	- Since it is measured in the units of Y , it is not always clear what constitutes a good RSE.
	- R^2^ statistic provides an alternative measure of fit
- Standard errors can be used to compute confidence intervals
- Standard errors can also be used to perform **hypothesis tests** on the coefficients
- t-statistic
- p-value
- quantify the extent to which the model fits the data. The quality of a linear regression fit is typically assessed using two related quantities: the **residual standard error (RSE)** and the **R^2^ statistic**


- **total sum of squares (TSS)**
	- TSS measures the total variance in the response Y
	- can be thought of as the amount of variability inherent in the response before the regression is performed
	- In contrast, RSS measures the amount of variability that is left unexplained after performing the regression
	- Hence, `(TSS − RSS)` measures the amount of variability in the response that is explained (or removed) by performing the regression, and R^2^ measures the proportion of variability in Y that can be explained using X

- **R^2^ statistic**
	- It always takes on a value between 0 and 1
	- It is independent of the scale of Y
	- It takes the form of a proportion—the proportion of variance
	- An R^2^ statistic that is close to 1 indicates that a large proportion of the variability in the response has been explained by the regression. A number near 0 indicates that the regression did not explain much of the variability in the response; this might occur because the linear model is wrong, or the inherent error σ 2 is high, or both.
- The R^2^ statistic  has an interpretational advantage over the RSE, since unlike the RSE, it always lies between 0 and 1.
- However, it can still be challenging to determine what is a good R^2^ value, and in general, this will depend on the application.
- The R^2^ statistic is a measure of the linear relationship between X and Y
- **Correlatio Cor(X, Y )** is also a measure of the linear relationship between X and Y
- This suggests that we might be able to use r = Cor(X, Y ) instead of R 2 in order to assess the fit of the linear model
- in the simple linear regression setting, R 2 = r 2 . In other words, the squared correlation and the R 2 statistic are identical.
- In multiple linear regression problem, in which we use several predictors simultaneously to predict the response. The concept of correlation between the predictors and the response does not extend automatically to this setting, since correlation quantifies the association between a single pair of variables rather than between a larger number of variables. R^2^ fills this role.

**Multiple Linear Regression**

>Y = β~0~ + β~1~X~1~ + β~2~X~2~ + · · · + β~p~X~p~ + e
>where,
>* p distinct predictors
>* X~j~ represents the jth predictor and β~j~ quantifies the association between that variable and the response. We interpret β~j~ as the average effect on Y of a one unit increase in X~j~, holding all other predictors fixed.

- the first step in a multiple regression analysis is to compute the F-statistic
- to examine the associated p-value
- Alternative hypothesis test  for multiple linear regressiong is performed by computing the **F-statistic**
- F-statistic follows an F-distribution
- How large does the F-statistic need to be before we can reject H~0~ and conclude that there is a relationship? It turns out that the answer depends on the values of n and p.
- If p > n, i.el number of predictors are greater than number of observations, the coefficients cannot be estimated using F-statistics, and this **high dimensional** setting can be approached using **dorward selection**
- The task of determining which predictors are associated with the response, in order to fit a single model involving only those predictors, is referred to as **variable selection**
- Various statistics can be used to judge the quality of a model. These include:
	* Mallow’s C~p~
	* Akaike information criterion (AIC)
	* Bayesian information criterion (BIC)
	* adjusted R^2^
- Unfortunately, there are a total of 2^p^ models that contain subsets of p variables, when p=2 total models to consider are 2^2^=4 models
- Unless p is very small, we cannot consider all 2 p models, and instead we need an automated and efficient approach to choose a smaller set of models to consider. There are three classical approaches for this task:
	* **Forward selection**
		- We begin with the null model—a model that contains an intercept but no predictors.
		- We then fit p simple linear regressions and add to the null model the variable that results in the lowest RSS
		- We then add to that model the variable that results in the lowest RSS for the new two-variable model
		- This approach is continued until some stopping rule is satisfied.
	* **Backward selection**
		- We start with all variables in the model, and remove the variable with the largest p-value—that is, the variable that is the least statistically significant.
		- The new (p − 1)-variable model is fit, and the variable with the largest p-value is removed.
		- This procedure continues until a stopping rule is reached
	* **Mixed selection**
- Backward selection cannot be used if p > n, while forward selection can always be used.
- Forward selection is a greedy approach, and might include variables early that later become redundant

- The non-linear pattern cannot be modeled accurately using linear regression.

- How much will Y vary from Ŷ ? We use prediction intervals to answer this question. Prediction intervals are always wider than confidence intervals, because they incorporate both the error in the estimate for f (X) (the reducible error) and the uncertainty as to how much an individual point will differ from the population regression plane (the irreducible error).

- Qualitative Predictors
- Quantitative Predictors


1. Is there a relationship between advertising sales and budget?
fitting a multiple regression model of sales onto predictors and testing the Null hyposthesis H~0~. Use F-statistic to accept or reject null hypothesis
2. How strong is the relationship?
- RSE to measure SD (Standard deviation) of the response from the pupullation regression line
- R^2^ to estimate the variablibity in the response that is explained by predictors
3. Which media contributes to the sales?
- examine the p-values associated with each predictor’s t-statistic
4. How large is the effect of each medium on sales?
- standard error
- Collinearity analysis
- VIF scores - Variance Inflation Factor scores for measuring collinearity
- simple linear regression to assess association of each medium individually
5. How accurately can we predict future sales?
- depends on whether we wish to predict individual response or average response
- for individual response accuracy - use prediction interval
- for average response accuracy - use confidence interval
6. Is the relationship linear?
- use residual plots to identify non-linearity
- linear relationships  display no patterns in residual plots
- use transformations of predictors to accomodate non-linear relationships in the linear regression model
7. Is there synergy among the advertising medium?
- linear regression model assumes additive relationship between the predictors and the response
- In additive relationship, the effect of each predictors on the response is unrelated to the values of the other predictors
- use interaction term in the linear regression model in order to accomodate non-additive relationships
- A small p-value associated with the interaction term indicates the presence of such relationship

**Parametric V/s Non-parametric methods**
* Linear regression is an example of a parametric approach because it assumes a linear function form for f(X)
  - Advantages:
    - the coefficients have simple interpretations
    - tests of statistical significance can be easily performed
  - Disadvantages
    - hey make strong assumptions about the form of f (X). If the specified functional form is far from the truth, and prediction accuracy is our goal, then the parametric method will perform poorly. For instance, if we assume a linear relationship between X and Y but the true relationship is far from linear, then the resulting model will provide a poor fit to the data, and any conclusions drawn from it will be suspect.
 
* In contrast, non-parametric methods do not explicitly assume a parametric form for f (X), and thereby provide an alternative and more flexible approach for performing regression.
- One of the simplest and best-known non-parametric methods is K-nearest neighbors regression (KNN regression).
- The KNN regression method is closely related to the KNN classifier

- as the extent of non-linearity increases, there is little change in the test set MSE for the non-parametric KNN method, but there is a large increase in the test set MSE of linear regression.
- in reality, even when the true relationship is highly non-linear, KNN may still provide inferior results to linear regression.
- in higher dimensions, KNN often performs worse than linear regression
- The decrease in performance as the dimension increases is the commoin problem for KNN and reslts rom the fact that in higher dimensions there is effectively reduction in the sample size
- curse of dimensionality i.e. the K observations that are nearest to a given test observation x~0~ may be very far away from x~0~ in p-dimensional space when p is large, leading to a very poor prediction of f(x~0~) and hence a poor KNN fit.
- As a general rule, parametric methods will tend to outperform non-parametric approaches when there is a small number of observations per predictor



http://dreamdragon.github.io/vatic/

sudo a2enmod cgi
sudo a2enmod include

## Classification
- qualitative variables are referred to as categorical
- Predicting a qualitative response for an observation can be referred to as classifying that observation, since it involves assigning the observation to a category, or class.
- There are many possible classification techniques, or classifiers, that one might use to predict a qualitative response.
- widely-used classifiers:
  * logistic regression
  * linear discriminant analysis
  * K-nearest neighbors
  * genaralised additive models
  * trees
  * Random forests
  * Boosting
  * Support Vector machines
- in general there is no natural way to convert a qualitative response variable with more than two levels into a quantitative response that is ready for linear regression
- the classifications that we get if we use linear regression to predict a binary response will be the same as for the linear discriminant analysis (LDA)


### Keywords
* maximum likelihood
* odds
* log-odds or logit
* likelihood function
* confounding
* Bayes’ theorem
* Bayes classifier
* density function
* prior probability
* posterior probability
* normal distribution
* multivariate normal distribution
* Gaussian distribution
* multivariate Gaussian distribution
* Decision Boundary
* Bayes error rate
* LDA test error rate
* mean vector
* common covariance matrix
* overfitting
* confusion matrix

### Logistic Regression
- logistic function will always produce an S-shaped curve
- Odds are traditionally used instead of probabilities in horse-racing, since they relate more naturally to the correct betting strategy
- the logistic regression model has a logit that is linear in X

$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$


$p(X)=\frac{1+e^{\beta_0+\beta_1X}}{1+e}$

We seek to estimate $ \beta_0, \beta_1 \backepsilon \hat p(x_i)$ (Predicted probability) of default for each individual, corresponds as closely as possible to the individual's observed default status.

#### Multiple Logistic Regression

#### Logistic Regression for $>2$ Response Classes

### Linear Discriminant Analysis (LDA)
* LDA classifier results from assuming that the observations within each class come from a normal distribution with a class-specific mean vector $\mu$ and a common variance $\sigma^2$ , and plugging estimates for these parameters into the **Bayes classifier**.
* To implement LDA:
	- Estimate $\mu_k, \pi_k, \sigma^2$
	- Compute decision boundary
* LDA is trying to approximate the Bayes classifier, which has the lowest total error rate out of all classifiers (if the Gaussian model is correct).
* How well does the LDA classifier perform?

**multivariate Gaussian distribution**
* The multivariate Gaussian distribution assumes that each individual predictor follows a one-dimensional normal distribution, with some correlation between each pair of predictors.
* The higher the ratio of parameters p to number of samples n, the more we expect this overfitting to play a role. For these data we don’t expect this to be a problem, since p = 4 and n = 10, 000.

Mean: $\mu$
Variance: $\sigma^2$
Standard Deviation: $\sigma$
Prior probability : $\pi_k$

##

##

## Support Vector Machines
Our goal is to develop a classifier based on the training data that will correctly
classify the test observation using its feature measurements.
There are number of approaches for this task, such as:-
- Linear discriminant analysis
- Logistic regression
- Classification trees
- Bagging
- Boosting

We will now see a new approach that is based upon the concept of a separating hyperplane.

### Hyperplace Concept


In order to construct a classifier based upon a separating hyperplane, we must have a reasonable way to decide which of the infinite possible separating hyperplanes to use.

### Maximal Margin Classifier
A natural choice is the maximal margin hyperplane (also known as the optimal separating hyperplane), which is the separating hyperplane that is farthest from the training observations. That is, we can compute the (perpendicular) distance from each training observation to a given separating hyperplane; the smallest such distance is the minimal distance from the observations to the hyperplane, and is known as the margin. The maximal margin hyperplane is the separating hyperplane for which the margin is largest—that is, it is the hyperplane that has the farthest minimum distance to the training observations. We can then classify a test observation based on which side of the maximal margin hyperplane it lies. This is known as the **maximal margin classifier**.
- Although the maximal margin classifier is often successful, it can also lead to overfitting when p (Dimensionality) is large.
- the maximal margin hyperplane depends directly on only a small subset of the observations is an important property that will arise later in this chapter when we discuss the support vector classifier and support vector machines.
- the fact that the maximal margin hyperplane is extremely sensitive to a change in a single observation suggests that it may have overfit the training data.

### Support Vector Classifier or soft margin classifier
The generalization of the maximal margin classifier to the non-separable case is known as the support vector classifier.
- Rather than seeking the largest possible margin so that every observation is not only on the correct side of the hyperplane but also on the correct side of the margin, we instead allow some observations to be on the incorrect side of the margin, or even the incorrect side of the hyperplane. (The margin is soft because it can be violated by some of the training observations.)
- In practice, C is treated as a tuning parameter that is generally chosen via cross-validation.
- As with the tuning parameters, **C controls the bias-variance trade-off** of the statistical learning technique.
- only observations that either lie on the margin or that violate the margin will affect the hyperplane, and hence the classifier obtained, in other words, an observation that lies strictly on the correct side of the margin does not affect the support vector classifier.
- Observations
that lie directly on the margin, or on the wrong side of the margin for their class, are known as **support vectors**. These observations do affect the support vector classifier.
- support vector classifier is a natural approach for classification in the two-class setting, if the boundary between the two classes is linear.

### Support Vector Machines
a general mechanism for converting a linear classifier into one that produces non-linear decision boundaries. We then introduce the support vector machine, which does this in an automatic way.
- the performance of linear regression can suffer when there is a nonlinear relationship between the predictors and the outcome.
- The non-linear decision boundaries between classes can be dealt by enlarging the feature space using quadratic, cubic, and even higher-order polynomial functions of the predictors.
- SVM allows us to enlarge the feature space used by the support vector classifier in a way that leads to efficient computations
- support vector machine (SVM) is an extension of the support vector classifier that results from enlarging the feature space in a specific way, susing kernels
- how an SVM compares to LDA
- How can we extend SVMs to the more general case where we have some arbitrary number of classes?
- It turns out that the concept of separating hyperplanes upon which SVMs are based does not lend itself naturally to more than two classes. Though a number of proposals for extending SVMs to the K-class case have been made, the two most popular are the one-versus-one and one-versus-all approaches.
- it turns out that the hinge loss function is closely related to the loss function used in logistic regression
- Due to the similarities between their loss functions, logistic regression and the support vector classifier often give very similar results.
- When the classes are well separated, SVMs tend to behave better than logistic regression; in more overlapping regimes, logistic regression is often preferred.
- The choice of tuning parameter is very important and determines the extent to which the model underfits or over- fits the data


# Machine Learning with Python

## SVM on MINIST with Python
- https://martin-thoma.com/svm-with-sklearn/



# Markdown editors
https://github.com/karthik/markdown_science/wiki/Tools-to-support-your-markdown-authoring
https://stackedit.io/

# Typesetting
* https://en.wikipedia.org/wiki/TeX

# Mathematical Symbols
* https://en.wikipedia.org/wiki/List_of_mathematical_symbols


## MathJax
http://docs.mathjax.org/en/latest/mathjax.html
http://blog.yhat.com/posts/rodeo-1.1-markdown.html

$$\begin{array}{r l}
\max & z = \sum_{j=1}^{n} c_j x_j & \\
\text{s.t.} & \sum_{j=1}^{n} \bar a_{ij} x_{j} + \max_{S_i \subseteq J_i, |S_i| = \Gamma_i} { \sum_{j \in S_i} \hat a_{ij} y_j } \leq b_i & \forall\, i=1,\dotsc,m \\
& x_j \leq y_j & \forall\, j=1,\dotsc,n\\
& x_j \geq 0,y_j \geq 0  & \forall\, j=1,\dotsc,n
\end{array}$$


MathJax is an open-source JavaScript display engine for LaTeX, MathML, and AsciiMath notation that works in all modern browsers. It was designed with the goal of consolidating the recent advances in web technologies into a single, definitive, math-on-the-web platform supporting the major browsers and operating systems, including those on mobile devices.

https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference

$\hat x$
$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$

- \alpha, \beta, \omega, \gamma, \delta
>$\alpha, \beta, \omega, \gamma, \delta$

**Uppercase:**
- \Gamma, \Delta, \Omega
>$\Gamma, \Delta, \Omega$


## Research Institutes
* [Pascal Network](http://www.pascal-network.org/)
