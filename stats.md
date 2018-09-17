---
Title: Stats
Decription: Stats
Author: Bhaskar Mangal
Date: 
Tags: Stats
---

**Table of Contents**
* TOC
{:toc}


## Statistics

## Median
**References**
- https://en.wikipedia.org/wiki/Median

The median is a simple measure of central tendency.
* It may be thought of as the "middle" value of a data set
* To find the median, we arrange the observations in order from smallest to largest value. If there is an odd number of observations, the median is the middle value. If there is an even number of observations, the median is the average of the two middle values.

**Characterisctics**
* The basic advantage of the median in describing data compared to the mean (often simply described as the "average") is that it is not skewed so much by extremely large or small values, and so it may give a better idea of a 'typical' value. 
* The median can be used as a measure of location when a distribution is skewed, when end-values are not known, or when one requires reduced importance to be attached to outliers, e.g., because they may be measurement errors.
* A median is only defined on ordered one-dimensional data
* It is independent of any distance metric.
* A geometric median, on the other hand, is defined in any number of dimensions.
* It has the property of minimizing the sum of distances for one-dimensional data
* The median is one of a number of ways of summarising the typical values associated with members of a statistical population; thus, it is a possible location parameter.
* The median is the 2nd quartile, 5th decile, and 50th percentile
* A median can be worked out for ranked but not numerical classes
* median is used as a location parameter in descriptive statistics

different measures of location and dispersion are often compared on the basis of how well the corresponding population values can be estimated from a sample of data. 
### Keywords
* Quartile
* Decile
* Percentile
* measure of variability: the range, the interquartile range, the mean absolute deviation, and the median absolute deviation.

## Geometric median
**References**
- https://en.wikipedia.org/wiki/Geometric_median

## Standard Deviation

## References
* https://en.wikipedia.org/wiki/Moment_(mathematics)
* https://en.wikipedia.org/wiki/Image_moment

## Skewness 

## Geometry

## Euclidean Space
**References**
- https://en.wikipedia.org/wiki/Euclidean_space


## Hypothesis testing
- comparing two groups
- t-test: the simplest statistical tes
- 2 sample test
- “paired test”, or “repeated measures test”
- T-tests assume Gaussian errors.
- Wilcoxon signed-rank test - it that relaxes this Gaussian errors assumption
- non paired case is the Mann–Whitney U test
- Given two set of observations, x and y, we want to test the hypothesis that y is a linear function of x

**[ordinary least squares (OLS) or linear least squares](https://en.wikipedia.org/wiki/Ordinary_least_squares)**
- In statistics, ordinary least squares (OLS) or linear least squares is a method for estimating the unknown parameters in a linear regression model.

- Post-hoc hypothesis testing: analysis of variance (ANOVA)

## Types of Disctributions
- Gaussian distributions
- Normal distributions
- Probability distributions


## Robust_statistics
- https://en.wikipedia.org/wiki/Robust_statistics
- To compute a regression that is less sentive to outliers, one must use a robust model.


## Misc
* Multilinear regression model, calculating fit, P-values, confidence intervals etc.
	- if required, first flatten the data
	- conver data into dataframes
	- fit the model
	- perform ANOVA - Analysis of Variance on the fitted (linear) model
	- plot the fitted model
	- retrieve the parameter estimates
	- inference, interpretations
	- calculate total run time of the script
* Multiple Regression


## Problem Statements
* Air fares before and after 9/11
	- This is a business-intelligence (BI) like application.
	- What is interesting here is that we may want to study fares as a function of the year, paired accordingly to the trips, or forgetting the year, only as a function of the trip endpoints.
	* Using statsmodels’ linear models, we find that both with an OLS (ordinary least square) and a robust fit
	* Make a dataframe whith the year as an attribute, instead of separate columns