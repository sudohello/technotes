---
Title: R
Decription: R
Author: Bhaskar Mangal
Date: 
Tags: R
---

**Table of Contents**
* TOC
{:toc}


## R

## Statistics Terms
* Standard Deviation
* Mean/Average
* Median
* Variance
* R^2^ Statistics
* Correlation
* Percentile
* Weighted Avegrage
* TSS - Total Sum of Squares
* RSS - Residual Sum of Squares
* RSE - Residual Standard Error
* SE - Standard Error

## Installing R, R-studio
* https://www.rstudio.com/products/rstudio/download-server/
* https://download2.rstudio.org/rstudio-server-1.0.143-amd64.deb
* https://www.digitalocean.com/community/tutorials/how-to-set-up-r-on-ubuntu-14-04
* https://cran.r-project.org
* https://cran.r-project.org/bin/linux/ubuntu/README

```r-base gdebi-core```

## Basics
* https://www.r-bloggers.com/mini-ai-app-using-tensorflow-and-shiny/
* https://www.analyticsvidhya.com/blog/2016/02/complete-tutorial-learn-data-science-scratch/

```bash
x <- c (1 ,3 ,2 ,5)
x
y = c (1 ,6 ,2, 2)
y
?c
length(x)
x+y
ls()
rm(x)
rm ( list = ls () ) #remove all objects at once
?matrix
y = matrix ( data = c (1 ,2 ,3 ,4) , nrow =2 , ncol =2)
x = matrix ( c (1 ,2 ,3 ,4) ,2 ,2)
matrix ( c (1 ,2 ,3 ,4) ,2 ,2) #matrix is printed to the screen but is not saved for future calculations.

A = matrix (1:16 ,4 ,4)
A
A[2,3] #[row,col]
dim(A)

x = rnorm (50) #creates standard normal random variables with a mean of 0 and a standard deviation of 1
y = x + rnorm (50 , mean =50 , sd =.1)
cor ( x , y )

set.seed(1303) #to reproduce the exact same set of random numbers
rnorm(50)

set.seed(3)
y=rnorm(100)
mean(y)
var(y)
sqrt(var(y))
sd(y)

#seq(a,b) makes a vector of integers between a and b
seq (1 ,10)
seq(0,1,length=10) #makes a sequence of 10 numbers that are equally spaced between 0 and 1
seq(-pi,pi,length=50)

plot(x,y) #produces a scatterplot of the numbers in x versus the numbers in y
plot (x ,y,xlab="this is the x - axis", ylab="this is the y - axis", main="Plot of X vs Y")


pdf("figure.pdf") #save to pdf
plot(x,y,col="green")
dev.off()

#contour plots
seq(-pi,pi,length=50)
y=x
f=outer(x,y,function(x,y) cos(y)/(1+ x^2))
contour(x,y,f)
contour(x,y,f,nlevels=45)

fa=(f-t(f))/2
contour(x,y,fa,nlevels=15)

#heatmap
image(x,y,fa)

#3D plot
persp(x,y,fa )

jpeg("figure.jpeg") #save to jpeg image
persp(x,y,fa,theta=30,phi=20)
dev.off()
```
>---
matrix() 	- function can be used to create a matrix of numbers
dim()    	- outputs the number of rows followed by the number of columns of a given matrix
sqrt()   	- function returns the square root of each element of a vector or matrix
rnorm()  	- function generates a vector of random normal variables, with first argument n the sample size
cor()    	- function to compute the correlation between
mean()   	- functions can be used to compute the mean of a vector of numbers
var()    	- functions can be used to compute variance of a vector of numbers
sd()     	- Applying sqrt() to the output of var() will give the standard deviation. Or we can simply use the sd() function
plot()   	- function is the primary way to plot data in R; scatterplots of the quantitative variables
hist()	 	- function to plot a histogram
pairs()  	- function creates a scatterplot matrix i.e. a scatterplot for every pair of variables for any given data set
pdf()    	- save to pdf file
jpeg()   	- save to jpeg file
dev.off()	- indicates to R that we are done creating the plot
seq()    	- create a sequence of numbers
contour()	- creates contour plots
image() 	- function works the same way as contour() , except that it produces a color-coded plot whose colors depend on the z value (heatmap)
persp()	  - produce a three-dimensional plot. The arguments theta and phi control the angles at which the plot is viewed.
q()				- shut/quits R
* `?funcname`  will always cause R to open a new help file window with additional information about the function **funcname**
* CTRL + L - to clear commandline screen

## Loading Data
* http://www-bcf.usc.edu/~gareth/ISL/data.html

```bash
#text file

## R store it as an object called Auto, in a format referred to as a data frame.
Auto=read.table("~/Downloads/ISLR-dataset/Auto.data.txt",header=T,na.strings="?")
fix(Auto)
dim(Auto)

#csv
Auto=read.csv("~/Downloads/ISLR-dataset/Auto.csv",header=T,na.strings="?")

#remove rows with missing observations
Auto=na.omit(Auto)

names(Auto)
plot(Auto$mpg, Auto$cylinders)

attach(Auto)
plot(cylinders,mpg)
cylinders=as.factor(cylinders)
plot(cylinders,mpg,col="red")

hist(mpg,col=2,breaks=15)

plot(cylinders,mpg,col="red",varwidth=T,horizontal=T)

pairs(Auto)
pairs(~ mpg + displacement + horsepower + weight + acceleration, Auto)

# Interactive plot to display the property of the data points by click
plot(horsepower,mpg)
identify(horsepower,mpg,name)

# numerical summary of each variable in a data set
# For qualitative variables such as name , R will list the number of observations that fall in each category
summary(Auto)

# summary of just a single variable
summary(mpg)

```

>---
read.table()  - importing a data set into R. option header=T (or header=TRUE ). na.strings tells R that any time it sees a particular character or set of characters (such as a question mark), it should be    treated as a missing element of the data matrix
write.table() - to export data
fix()         - function can be used to view data in a spreadsheet like window
na.omit()     - function to simply remove rows contain missing observations
names()       - to check the variable names
as.factor()   - function converts quantitative variables into qualitative variables
summary()			- function produces a numerical summary of each variable in a particular data set
                      - The individual components of a summary object by name
?summary.lm           - to see what is available
summary(lm.fit)$r.sq  - gives the R^2
summary(lm.fit)$sigma - gives the RSE
vif()                 - part of the car package, can be used to compute variance inflation factors (VIF)
                      - The car package is not part of the base R installation.
                      - It must be downloaded the first time you use it via the install.packages option in R
identify()		- in conjuction with plot(), provides a useful identify() interactive method for identifying the value for a particular variable for points on a plot. We pass in three arguments to identify() : the x-axis variable, the y-axis variable, and the variable whose values we would like to see printed for each point.
savehistory()	- save a record of all of the commands that we typed in the most recent session
loadhistory()	- load that history from the saved session history

library()             - load libraries, or groups of functions and library data sets that are not included in the base R distribution.
install.packages()    - R will automatically download the package and installs it.
[ Installing package into ‘/home/bhaskar/R/x86_64-pc-linux-gnu-library/3.4’ (as ‘lib’ is unspecified) ]
	
abline()              - function can be used to draw any line, not just the least squares regression line.
par()                 - it tells R to split the display screen into separate panels so that multiple plots can be viewed simultaneously

lm()                  - linear regression model
                      - also accommodate non-linear transformations of the predictors

lm(y~x, data)         - y is response, x is predictor, data is dataset
lm(y~x1+x2+x3, data)  - multiple linear regression model using least squares, here it's used to fit a model with three predictors- x1,x2,& x3
lm(y~., data)         - order to perform a regression using all of the predictors
lm(y~.-x1, data)      - perform a regression using all of the variables but one (x1)


residuals()           - we can compute the residuals from a linear regression fit
rstudent()            - will return the studentized residuals, and we can use this function to plot the residuals against the fitted values
hatvalues()           - Leverage statistics can be computed for any number of predictors using the function
which.max()           - identifies the index of the largest element of a vector
update()
anova()               - to further quantify the extent to which the quadratic fit is superior to the linear fit
                      - it performs a hypothesis test comparing the two models
                      - The null hypothesis is that the two models fit the data equally well
                      - and the alternative hypothesis is that the full model is superior.
I(x^2)                - predictor x to the power 2 - produces square fit, x^3 produces cubic fit
poly()                - to create the polynomial within lm()
 
<functionName>() {}   - create user defined function


**library ( MASS )**
- The MASS library contains the Boston data set, which records medv (median house value) for 506 neighborhoods around Boston.
- Simple Linear Regression
  * using the lm() function to fit a simple linear regression lm() model, with medv as the response and lstat as the predictor. The basic syntax is lm(y∼x,data) , where y is the response, x is the predictor, and data is the data set in which these two variables are kept.

```
lm.fit=lm(medv~lstat, data=Boston)
summary(lm.fit)
names(lm.fit)
coef(lm.fit)

# to obtain a confidence interval for the coefficient estimates
confint(lm.fit)

# predict() function can be used to produce confidence intervals,
#and prediction intervals for the prediction of medv for a given value of lstat
predict(lm.fit, data.frame(lstat=(c(5,10,15))), interval="confidence")
predict(lm.fit, data.frame(lstat=(c(5,10,15))), interval="prediction")

plot(Boston$lstat,Boston$medv, pch="+") # change symbol
abline(lm.fit)
# lwd=3 command causes the width of the regression line to be increased by a factor of 3
# this works for the plot() and lines() functions also
abline(lm.fit, lwd=3, col="red")

# split the display screen into separate panels, here in 2×2 grid of panels.
par(mfrow=c(2,2))

#
x=hatvalues(lm.fit)
plot(x)
# which observation has the largest leverage statistic.
which.max(x)

#


```






**data frame**

## References
* https://www.digitalocean.com/community/tutorials/how-to-set-up-r-on-ubuntu-14-04
* https://cran.r-project.org
* https://cran.r-project.org/bin/linux/ubuntu/README

# Image Processing in R
* http://blog.thedigitalgroup.com/rajendras/2015/06/12/image-processing-and-analysis-in-r/

# Deep Learning in R

## References
* https://www.r-bloggers.com/deep-learning-in-r-2/
* http://blog.revolutionanalytics.com/2017/02/deep-learning-in-r.html

### Other Books & References
* The Elements of Statistical Learning (ESL) by Hastie, Tibshirani, and Friedman was first published in 2001.


# Geospatial Analysis in R and GRASS GIS

While R is a general data analysis environment, it has been extensively used for modelling and simulation. The R data analysis programming language and environment is an extensible system which can be connected directly to GRASS. R onsists of a base package and extensions. R comprise packages for point pattern analysis, geostatistics, exploratory spatial data analysis and spatial econometrics. The R/GRASS interface substantially improves the geospatial analysis capabilities of GRASS. 