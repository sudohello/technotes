/*
Title: Computer Vision
Decription: Computer Vision
Author: Bhaskar Mangal
Date: 
Tags: Computer Vision
*/

# Applications of Image Processing and Computer Vision with Python and OpenCV

## Image Search Engine
* http://www.pyimagesearch.com/2014/01/27/hobbits-and-histograms-a-how-to-guide-to-building-your-first-image-search-engine-in-python/
* http://www.pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/
* http://www.pyimagesearch.com/2014/01/15/the-3-types-of-image-search-engines-search-by-meta-data-search-by-example-and-hybrid/

### Types
* meta-data
* CBIR (search by example)
* Hybrid

If you are relying on tags and keywords supplied by actual people, you are building a search by meta-data image search engine. If your algorithm analyzes the image itself and quantifies the image by extracting features, then you are creating a search by example search engine and are performing Content Based Image Retrieval (CBIR). If you are using both keyword hints and features together, you are building a hybrid approach of the two.

**Goal**
The goal, given a query image from one of our five different categories, is to return the category’s corresponding images in the top 10 results.

An **image descriptor** defines how we are quantifying an image, hence extracting features from an image is called describing an image. The output of an image descriptor is a feature vector, an abstraction of the image itself. Simply put, it is a list of numbers used to represent an image.

More complex image descriptors make use of term frequency-inverse document frequency weighting (tf-idf) and an inverted index

cv2.normalize(hist)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Required argument 'dst' (pos 2) not found

https://github.com/mconigliaro/smtptester/issues/2

### The complete guide to building an image search engine with Python and OpenCV
* http://www.pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/


# Basic Image Manipulation
* http://www.pyimagesearch.com/2014/01/20/basic-image-manipulations-in-python-and-opencv-resizing-scaling-rotating-and-cropping/
* https://stackoverflow.com/questions/11764575/python-2-7-3-opencv-2-4-after-rotation-window-doesnt-fit-image


## Edge Detection

### Zero-parameter, automatic Canny edge detection with Python and OpenCV
* http://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/

automatically detect edges in images using the Canny edge detector, without providing thresholds to the function.

This trick simply takes the median of the image, and then constructs upper and lower thresholds based on a percentage of this median. In practice, sigma=0.33  tends to obtain good results.
* cv2.imshow("Original",image)
* cv2.imshow("Edges", np.hstack([wide,tight,auto]))

Once you find edges in your images, you can use the cv2.findContours function to find the actual objects that correspond to these edges. For an example of doing object detection with contours, please see this post.

### Removing contours from an image using Python and OpenCV
* http://www.pyimagesearch.com/2015/02/09/removing-contours-image-using-python-opencv/

### Accessing Individual Superpixel Segmentations with Python
* http://www.pyimagesearch.com/2014/12/29/accessing-individual-superpixel-segmentations-python/

## Shape Detection & Analysis
- http://www.pyimagesearch.com/2016/02/01/opencv-center-of-contour
- https://en.wikipedia.org/wiki/Image_moment
- http://docs.opencv.org/trunk/dd/d49/tutorial_py_contour_features.html
- https://en.wikipedia.org/wiki/Ramer–Douglas–Peucker_algorithm
- http://www.pyimagesearch.com/2014/05/19/building-pokedex-python-comparing-shape-descriptors-opencv/
- http://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/
- http://www.pyimagesearch.com/2015/04/20/sorting-contours-using-python-and-opencv

* For more advanced shapes, or shapes that have substantial variances in how they appear (such as noisy contours), you might need to train your own custom object detector.
	- http://www.pyimagesearch.com/2014/11/10/histogram-oriented-gradients-object-detection/

* Pedestrian detector
  - For pedestrian detection you typically wouldn’t use the grayscale pixels values. It would be better to extract features from the image, normally Histogram of Oriented Gradients and then train a pedestrian detector on these features
  - http://www.pyimagesearch.com/2014/11/10/histogram-oriented-gradients-object-detection/
  - http://www.pyimagesearch.com/2015/11/09/pedestrian-detection-opencv/

* Detecting overlapping shapes
	- For overlapping shapes, I would suggest the watershed algorithm
	- http://www.pyimagesearch.com/2015/11/02/watershed-opencv/

* Detect the texture of an object
  - to detect the texture of an object, Local Binary Patterns plus an SVM would work well
  - http://www.pyimagesearch.com/2015/12/07/local-binary-patterns-with-python-opencv/

* For circle detection
	- http://www.pyimagesearch.com/2014/07/21/detecting-circles-images-using-opencv-hough-circles/

**Quantifying Image using Color**
- http://www.pyimagesearch.com/2014/01/22/clever-girl-a-guide-to-utilizing-color-histograms-for-computer-vision-and-image-search-engines/
- http://www.pyimagesearch.com/2014/03/03/charizard-explains-describe-quantify-image-using-feature-vectors/

++Distribution of Colors in an image++
- A histogram represents the distribution of colors in an image.
- A histogram can be visualized as a graph (or plot) that gives a high-level intuition of the intensity (pixel value) distribution.
- A RGB color space in this example, so these pixel values will be in the range of 0 to 255.
- When plotting the histogram, the X-axis serves as our “bins”. If we construct a histogram with 256 bins, then we are effectively counting the number of times each pixel value occurs. In contrast, if we use only 2 (equally spaced) bins, then we are counting the number of times a pixel is in the range [0, 128) or [128, 255]. The number of pixels binned to the X-axis value is then plotted on the Y-axis.
- By simply examining the histogram of an image, you get a general understanding regarding the contrast, brightness, and intensity distribution.
- In context of image search engines, histograms can serve as feature vectors (i.e. a list of numbers used to quantify an image and compare it to other images).
- Comparing the “similarity” of color histograms can be done using a distance metric. Common choices include: Euclidean, correlation, Chi-squared, intersection, and Bhattacharyya
- cv2.calcHist function in OpenCV to build our histograms.
- mask: A mask is a uint8  image with the same shape as our original image, where pixels with a value of zero are ignored and pixels with a value greater than zero are included in the histogram computation. Using masks allow us to only compute a histogram for a particular region of an image

## Learning Objectives
**Assumptions**
- assume that images with similar color distributions have similar content.

1. Compute the center of a contour
  * Compute the center of a contour/shape region
    - [opencv-center-of-contour](http://www.pyimagesearch.com/2016/02/01/opencv-center-of-contour/)
2. Perform shape detection & identification
  * Recognize various shapes, such as circles, squares, rectangles, triangles, and pentagons using only contour properties.
    - [opencv-shape-detection](http://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/)
3. Determining object color with OpenCV
  * Label the color of a shape
    - [determining-object-color-with-opencv](http://www.pyimagesearch.com/2016/02/15/determining-object-color-with-opencv/)

**How do I compute the center of a contour?**
(1) detect the outline of each shape in the image, followed by
(2) computing the center of the contour — also called the centroid of the region.


**Image pre-processing steps**
* Conversion to grayscale.
* Blurring to reduce high frequency noise to make our contour detection process more accurate.
* Binarization of the image. Typically edge detection and thresholding are used for this process. In this post, we’ll be applying thresholding.

**contour approximation**
- Contour approximation is an algorithm for reducing the number of points in a curve with a reduced set of points — thus the term approximation.
- This algorithm is commonly known as the Ramer-Douglas-Peucker algorithm, or simply the split-and-merge algorithm.
- Contour approximation is predicated on the assumption that a curve can be approximated by a series of short line segments. This leads to a resulting approximated curve that consists of a subset of points that were defined by the original cruve.
- Contour approximation is actually already implemented in OpenCV via the `cv2.approxPolyDP`  method.
- In order to perform contour approximation, we first compute the perimeter of the contour followed by constructing the actual contour approximation
- Common values for the second parameter to `cv2.approxPolyDP`  are normally in the range of 1-5% of the original contour perimeter.

**Why did you use the Ramer-Douglas-Peucker algorithm to reduce the set of points, instead of using the convex hull ?**
The contour approximation algorithm and Convex Hull algorithm are used for two separate purposes. As the name implies, contour approximation is used to reduce the number of points along a contour by “simplifying” the contour based on a percentage of the perimeter. Your resulting contour approximation is this a simplification of the shape by utilizing points that are already part of the shape.
The convex hull on the other hand is the smallest convex set that contains all points along the contour — it is, by definition, not a simplification of the contour shape and the resulting convex hull actually contains points that are not part of the original shape.

In this case, I used contour approximation because I wanted to reduce the number of (x, y)-coordinates that comprise the contour, while ensuring that all points in the resulting approximation were also part of the original shape.


**How To Describe and Quantify an Image Using Feature Vectors**
- http://www.pyimagesearch.com/2014/03/03/charizard-explains-describe-quantify-image-using-feature-vectors/

**What is an Image Feature Vector?**
Image Feature Vector: An abstraction of an image used to characterize and numerically quantify the contents of an image. Normally real, integer, or binary valued. Simply put, a feature vector is a list of numbers used to represent an image.
- This image descriptor handles the logic necessary to quantify an image and represent it as a list of numbers.

* What type of image descriptor you are going to use?
* What are you trying to characterize?
  - the color of an image and extracting color features?
  - the texture?
  - or the shape of an object in an image?
* What is the expected output of your image descriptor?
* How can we use this as a feature vector if it’s multi-dimensional?
A: simply flatten it.

1. define image descriptor
2. selected an image descriptor, you need to apply your image descriptor to an image.
- The output of your image descriptor is a feature vector: the list of numbers used to characterize your image.

### Image Descriptors

#### Color Feature Vector
- represent the distribution of colors in the image. There are different ways:-

1. **Raw Pixel Intensities**
- The most basic **color feature vector** you can use is the **raw pixel intensities** themselves. While we don’t normally use this representation in image search engines, it is sometimes used in machine learning and classification contexts, and is worth mentioning.
-  image is represented as NumPy array, it’s quite simple to compute the raw pixel representation of an image:
```python
raw=image.flatten()
```
2. **Mean of Color Channels**
- A simple method to quantify the color of an image is to compute the mean of each of the color channels.
- We can compute the mean of each of the color channels by using the cv2.mean method. This method returns a tuple with four values, our color features. The first value is the mean of the blue channel, the second value the mean of the green channel, and the third value is the mean of red channel. Remember, OpenCV stores RGB images as a NumPy array, but in reverse order. We actually read them backwards in BGR order, hence the blue value comes first, then the green, and finally the red.
```python
means=cv2.mean(image)
```
3. **Color Mean and Standard Deviation**
- In order to grab both the mean and standard deviation of each channel, we use the cv2.meanStdDev function, which not surprisingly, returns a tuple — one for the means and one for the standard deviations, respectively. Again, this list of numbers serves as our color features.
- combine the means and standard deviations into a single color feature vector
```python
(means, stds) = cv2.meanStdDev(image)
stats = np.concatenate([means, stds]).flatten()
```
4. **3D color histogram**
```python
hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
```

 I know think of SIFT as the best example of a “feature descriptor” or just “descriptor” and GIST as the best example of “image descriptor.”

**Terms**
1. image descriptor
  - data get from the whole image
  - An image descriptor is applied globally and extracts a single feature vector.
2. feature descriptor
  - data get from the local point of an image(a small region)
  - Feature descriptors on the other hand describe local, small regions of an image
  - You’ll get multiple feature vectors from an image with feature descriptors. 
3. descriptor == feature descriptor
4. feature vector
  - a bunch of data which could feed to the machine learning algo
  - A feature vector is a list of numbers used to abstractly quantify and represent the image.
  - Feature vectors can be used for machine learning, building an image search engine, etc.
  - **sometimes feature descriptor == feature vector because** they could feed to the machine learning algo and extract from the local point of an image

#### Texture Feature Vectors

1. **Haralick texture**
  - the GLCM matrix isn’t used directly as a feature vector. You instead compute statistics on this matrix, such as Haralick texture.
  - The mahotas library has a good implementation of Haralick texture features.
  - http://murphylab.web.cmu.edu/publications/boland/boland_node26.html
  - http://mahotas.readthedocs.io/en/latest/api.html#mahotas.features.haralick

**How we can leverage the Lab color space along with the Euclidean distance to tag, label, and determine the color of objects in images?**
- https://en.wikipedia.org/wiki/Lab_color_space
- https://en.wikipedia.org/wiki/Color_space

**The Lab color space** describes mathematically all perceivable colors in the three dimensions L for lightness and a and b for the color opponents green–red and blue–yellow.

**So why are we using the L*a*b* color space rather than RGB or HSV for labelling the color of the detected objects?**
- Well, in order to actually label and tag regions of an image as containing a certain color, we’ll be computing the Euclidean distance between our dataset of known colors (i.e., the lab  array) and the averages of a particular image region.
- The known color that minimizes the Euclidean distance will be chosen as the color identification.
- And unlike HSV and RGB color spaces, the Euclidean distance between L*a*b* colors has actual perceptual meaning 
- Euclidean_distance
  - https://en.wikipedia.org/wiki/Euclidean_distance

## Blur detection with OpenCV
- http://www.pyimagesearch.com/2015/09/07/blur-detection-with-opencv/
- https://pdfs.semanticscholar.org/8c67/5bf5b542b98bf81dcf70bd869ab52ab8aae9.pdf
- http://academic.mu.edu/phys/matthysd/web226/Lab02.htm
- http://homepages.inf.ed.ac.uk/rbf/HIPR2/log.htm
- http://ijssst.info/Vol-15/No-2/data/3251a237.pdf

**How to compute the amount of blur in an image using OpenCV, Python, and the Laplacian operator**
we simply convolve our input image with the Laplacian operator and compute the variance.If the variance falls below a predefined threshold, we mark the image as “blurry”.

- You simply take a single channel of an image (presumably grayscale) and convolve it with the following 3 x 3 kernel:
- And then take the variance (i.e. standard deviation squared) of the response.
- If the variance falls below a pre-defined threshold, then the image is considered blurry; otherwise, the image is not blurry.
- The reason this method works is due to the definition of the Laplacian operator itself, which is used to measure the 2nd derivative of an image.
- The reason this method works is due to the definition of the Laplacian operator itself, which is used to measure the 2nd derivative of an image. The Laplacian highlights regions of an image containing rapid intensity changes, much like the Sobel and Scharr operators. **And, just like these operators, the Laplacian is often used for edge detection.**
- The cv2.Laplacian function, as the name suggests, computes the Laplacian of the input image. This function is built-in to OpenCV. The var() method is a NumPy function. It computes the statistical variance of a set of data, which in this case is the Laplacian — hence the name “Variance of the Laplacian”.


**Assumption**
* The assumption here is that if an image contains high variance then there is a wide spread of responses, both edge-like and non-edge like, representative of a normal, in-focus image. But if there is very low variance, then there is a tiny spread of responses, indicating there are very little edges in the image. As we know, the more an image is blurred, the less edges there are.
* variance statistic the variance is only useful if your input images can actually “vary”.

**Tricks**
* the trick here is setting the correct threshold which can be quite domain dependent.
* This method tends to work best in environments where you can compute an acceptable focus measure range and then detect outliers.
*  To handle situations where only the subject of the image is blurry, I would suggest performing saliency detection (which I’ll do a blog post on soon) and then only computing the focus measure for the subject ROI of the image.
* You normally choose your threshold on a dataset-to-dataset basis by trial and error.
* Laplace filter is very sensitive with noise.

**Deblur**
* There are methods to “deblur” images; however, the results are less than satisfactory at the moment. If you’ve ever used Photoshop before, you’ve likely played around with these filters. They don’t work all that great, and “deblurring” is still a very active area of research.

* **Is it possible to find blur directions? Can we get two floating point values representing x-blur and y-blur?**
++Adrian Rosebrock++: Sure, absolutely. But for this, I wouldn’t use the Laplacian. I would compute the Sobel kernel in both the x and y directions. See this blog post for more information on the Sobel operator.

* **when the image is pure color or close to pure color even the image is clearness.The reason is that pure color image variance of Laplacian is close too.So,how to deal with this problem?**
++Adrian Rosebrock++: This blur detection method (as well as other blur detection methods) tend to examine the gradient of the image. If there is no gradient in the image (meaning pure color with no “texture”), there the variance will clearly be low. There are non-gradient based methods for blur detection and they are detailed in this survey paper on blur detection — I would suggest giving that a read.

* **We noticed that the moving person/object is always blur on the captured frame. Is this normal? Can we capture frames with moving opbjects that are not blur? What are the limitations?**
++Adrian Rosebrock++: Motion blur can be a bit of a problem, especially because when humans watch a video stream we tend to not “see” motion blur — we just see a fluid set of frames moving in front of us. However, if you were to hit “pause” in the middle of the stream, you would likely see motion blur. Ways to get around motion blur can involve using a very high FPS camera or using methods to detect the amount of blur and then choose a frame with minimal blur.

* **How would I got about implementing blur detection on a region of interest? (I assume I just slice the array) But what if that ROI is not a rectangle, but something made with a mask? For example, I want to focus on a face? Is the best way to just find the ROI, then find the largest rectangle I can slice out of it?**
++Adrian Rosebrock++: How you find and determine your ROI is up to you and is highly dependent on what you are trying to accomplish. Edge detection, thresholding, contour extraction, object detection, etc. can all be used for determining what your ROI is. Once you have your ROI, you would need to compute the bounding box for it, extract the ROI via array slicing, and then compute the blur value.

## Image Pyramids with Python and OpenC
- http://www.pyimagesearch.com/2015/03/16/image-pyramids-with-python-and-opencv/

- utilizing the Histogram of Oriented Gradients image descriptor and a Linear SVM to detect objects in images. This 6-step framework can be used to easily train object classification models. A critical aspect of this 6-step framework involves image pyramids and sliding windows.

**Image Pyramid**
- An “image pyramid” is a multi-scale representation of an image.
- Utilizing an image pyramid allows us to find objects in images at different scales of an image. And when combined with a sliding window we can find objects in images in various locations.
- At the bottom of the pyramid we have the original image at its original size (in terms of width and height). And at each subsequent layer, the image is resized (subsampled) and optionally smoothed (usually via Gaussian blurring).
- The image is progressively subsampled until some stopping criterion is met, which is normally a minimum size has been reached and no further subsampling needs to take place.

## Sliding Windows for Object Detection with Python and OpenCV
- https://www.pyimagesearch.com/2015/03/23/sliding-windows-for-object-detection-with-python-and-opencv/

**What is a sliding window?**
- In the context of computer vision (and as the name suggests), a sliding window is rectangular region of fixed width and height that “slides” across an image.
- Combined with image pyramids we can create image classifiers that can recognize objects at varying scales and locations in the image.


## Histogram of Oriented Gradients (HOG) and Object Detection
- http://www.pyimagesearch.com/2014/11/10/histogram-oriented-gradients-object-detection/
- https://gurus.pyimagesearch.com/lesson-sample-histogram-of-oriented-gradients-and-car-logo-recognition/#
- https://github.com/JeanKossaifi/python-hog/blob/master/hog/histogram.py
- http://www.learnopencv.com/histogram-of-oriented-gradients/

We have object detection using:
* keypoints
* local invariant descriptors
* bag-of-visual-words models
* [Histogram of Oriented Gradients (HOG)](http://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf)
* [deformable parts models](http://cs.brown.edu/~pff/papers/lsvm-pami.pdf)
* [Exemplar SVMs](http://www.cs.cmu.edu/~efros/exemplarsvm-iccv11.pdf)
* Deep Learning with pyramids to recognize objects at different scales!

**Semi Rigid Objects**
- A semi-rigid object is something that has a clear form and structure, but can change slightly — consider how a human walks. We put one foot in front of the other, maybe move our arms a bit. The form is clearly the same, but it does change a little bit.
- HOG is good at detect semi-rigid object
- HOG can be used to detect semi-rigid objects like humans provided that our poses are not too deviant from our training data.
- Finally, smoke is definitely not a semi-rigid object. Smoke diffuses into the air and has no real shape or form.
- image pyramid itself that allows you to detect objects at different scales of the image
- The sliding window simply allows you to detect objects at different locations.

* **Dont you apply non maximal suppression on each level separately?
Because if you apply across all levels then you are comparing between bounding boxes of different sizes.**
++Adrian Rosebrock:++ No, NMS is only applied after all bounding boxes are applied across all layers of the image pyramid. You resize each of your detected bounding boxes based on the ratio of the original image size to the current image size. This ensures that all bounding boxes are recorded at the same scale even though you are working with multiple scales of the image.

* ** why can’t we vary the window size instead of varying the image size(image pyramid)?**
++Adrian Rosebrock:++ Consider the HOG image descriptor which is commonly used for sliding windows and image pyramid. The size of the image/ROI passed into the HOG descriptor is influenced by the input image size. If you change the sliding window size, you change the output dimensionality of the descriptor. If all descriptors do not have the same dimensionality then you can’t apply a machine learning model to them. Because of this, the sliding window tends to be a fixed parameter in the model.
* Can we run this code on a GPU instead of using the CPU?
++Adrian Rosebrock:++ You can push the computation to the GPU, but you would need to recode using C++. The Python + OpenCV bindings do not have access to the GPU.

- You would simply maintain a list of bounding boxes for each of the unique classes reported by the SVM. From there, you would apply non-maxima suppression for each set of bounding boxes. NMS is meant to merge overlapping bounding boxes, either based on their spatial dimensions, or the probability returned by your SVM (where higher probabilities are preferred over the lower ones). If your bounding boxes are not overlapping, then NMS will not suppress them.

* **Let me ask the question a different way. If you train your classifier with images that are 140×100 (these are random subsets of the 280×200 target image), how do you get a bounding box around the target image with the NMS?**
++Adrian Rosebrock:++You would take the entire set of bounding boxes and apply NMS based on either (1) the bounding box coordinates (such as the bottom-right corner) or (2) the probability associated with the bounding box. Again, NMS isn’t used to actually generate the bounding box surrounding an object, it’s used to suppress bounding boxes that have heavy overlap.
- Why not just apply a dilation or closing morphological operation to close the gaps in between the footprints? From there, thresholding and contour detection will give you the footprint regions.
- If you’re using sliding windows in conjunction with image pyramids, you need to keep track of ratio of the original image height to the current pyramid height. You can use this scale to multiply the bounding box coordinates and obtain them for the original image size.
- NumPy automatically prevents the out of bound error by treating the index as an array slice. If you try to slice an array past the actual bounds of the array, it simply returns all the elements along that dimension.

**HOG Descriptors**
- HOG descriptors for quantifying and representing both shape and texture.
- HOG is implemented in both OpenCV and scikit-image. The OpenCV implementation is less flexible than the scikit-image implementation
- The cornerstone of the HOG descriptor algorithm is that appearance of an object can be modeled by the distribution of intensity gradients inside rectangular regions of an image
- Implementing this descriptor requires dividing the image into small connected regions called cells, and then for each cell, computing a histogram of oriented gradients for the pixels within each cell. We can then accumulate these histograms across multiple cells to form our feature vector.
-  we can perform block normalization to improve performance. To perform block normalization we take groups of overlapping cells, concatenate their histograms, calculate a normalizing value, and then contrast normalize the histogram. By normalizing over multiple, overlapping blocks, the resulting descriptor is more robust to changes in illumination and shadowing.
-   Furthermore, performing this type of normalization implies that each of the cells will be represented in the final feature vector multiple times but normalized by a slightly different set of neighboring cells.

### steps for computing the HOG descriptor.
1. **Normalizing the image prior to description.** (optional)
There are three main normalization methods that we can consider:
	* **Gamma/power law normalization**
		*  we take the $\log(p)$ of each pixel p in the input image.
		*  This approach is perhaps an “over-correction” and hurts performance
	* **Square-root normalization**
		* we take the $\sqrt(p)$ of each pixel p in the input image.
		* square-root normalization compresses the input pixel intensities far less than gamma normalization
		* square-root normalization actually increases accuracy rather than hurts it
	* **Variance normalization**
		* we compute both the mean $\mu$ and standard deviation $\sigma$ of the input image. All pixels are mean centered by subtracting the mean from the pixel intensity, and then normalized through dividing by the standard deviation: $p' = (p - \mu) / \sigma$.

2. **Gradient computation**
Compute the image gradient in both the x and y direction. We’ll apply a convolution operation to obtain the gradient images:
$G_{x} = I \star D_{x} and G_{y} = I \star D_{y}$
where I is the input image, $D_{x}$ is our filter in the x-direction, and $D_{y}$ is our filter in the y-direction.


## Non-Maximum Suppression for Object Detection in Python
- http://www.pyimagesearch.com/2014/11/17/non-maximum-suppression-object-detection-python

**Histogram of Oriented Gradients for Objection Detection** method can be broken into a 6-step process, including:
- Sampling positive images
- Sampling negative images
- Training a Linear SVM
- Performing hard-negative mining
- Re-training your Linear SVM using the hard-negative samples
- Evaluating your classifier on your test dataset, utilizing non-maximum suppression to ignore redundant, overlapping bounding boxes


## (Faster) Non-Maximum Suppression in Python
- http://www.pyimagesearch.com/2015/02/16/faster-non-maximum-suppression-python/
- http://www.computervisionblog.com/2011/08/blazing-fast-nmsm-from-exemplar-svm.html


- we instead vectorize the code using the np.maximum  and np.minimum  functions — this allows us to find the maximum and minimum values across the axis rather than just individual scalars.
- You have to use the np.maximum  and np.minimum  functions here — they allow you to mix scalars and vectors. The np.max  and np.min  functions do not

**overlapping bounding boxes**
-  To handle the removal overlapping bounding boxes (that refer to the same object) we can either use non-maximum suppression on the Mean-Shift algorithm. 

## Pedestrian Detection OpenCV
- http://www.pyimagesearch.com/2015/11/09/pedestrian-detection-opencv/
- http://www.pyimagesearch.com/2015/11/16/hog-detectmultiscale-parameters-explained/
- http://blog.dlib.net/2015/02/dlib-1813-released.html

OpenCV ships with a pre-trained HOG + Linear SVM model that can be used to perform pedestrian detection in both images and video streams

* **I used your example to detect people on video, now i need to know is there a way how to tracke them, i know about camshift and meanshift, but i dk how to implement them an implement them to multiple people just detected, can you please help me?**
++Adrian Rosebrock:++ CamShift and MeanShift can get quite complicated for multiple objects. It’s honestly too much to try to explain in a single comment. I’ll try to do a blog post on this topic in the near future. In the meantime, you might want to look at correlation tracking which is part of the dlib library

- So if I understand your question correctly, you would like to mount a camera on top of the roof of car, then take this car for a drive, and then count the number of cars that pass it as it’s driving around?

That is indeed possible with computer vision — but it’s also a very challenging project since you’ll need to train a machine learning classifier to recognize cars at various viewing angles.

* **Great post! Im wondering how hard it is to track pedestrians? What I mean is: you have a camera stream with pedestrians. Assuming the above script works fine, I’m able to mark pedestrians. The question is how can I track individual personas? I want to mark them as numbers and track them as long as they’re visible. Once they’re gone, they’re gone. When a new pedestrian appears it bumps the counter and starts tracking that person…**
++Adrian Rosebrock:++ Tracking is a bit more challenging, but absolutely doable. I would suggest starting with basic CamShift. However, the biggest downside is that CamShift (by definition) utilizes the histogram of the ROI (in this case, the histogram of the person region). This can easily fail. So, a better approach would be to use MOSSE or correlation trackers — I’ve been meaning to do a blog post on them, but just haven’t had the time. Finally, the easiest method that I suggest doing is computing the centroid of each ROI between frames. Compute the Euclidean distances between the centroid sets between frames. The centroid that minimizes the distance between the consecutive frames is thus your “match”. You can use this method to “track” objects as they enter and leave view of the camera.

- My plan is to have an app that counts how many people enter a place… Like shop for example, or a house. The stretch goal is to detect faces and to check if that person Has visited the place before

- I personally haven’t done any Android development, but you won’t be able to get a Python + OpenCV script to run on an Android device. You’ll need to rewrite the program to use Java + OpenCV.
- Calling cv2.destroyAllWindows will close any windows. Then, you just need to call .release() on the VideoCapture object.
- Are you referring to the HOG descriptor? If so, no. The HOG descriptor is defined in terms of an image ROI (width and height). This is a fixed value. Changing the spatial dimensions would alter the HOG descriptor and you would ultimately have to retrain the detector. My suggestion is that if you want to alter the dimensions, you should train your own detector.
- If you want to use the setSVMDetector method you would need to train your detector using OpenCV’s built-in tools. This is the only way to create a model compatible with setSVMDetector. Otherwise, you should be training your model using other machine learning libraries such as scikit-learn, etc. (highly recommended).
- Using scikit-learn’s method is slower in most cases (Python versus compiled C/C++). I’ve found dlib’s detector to be much more accurate and just as speedy as OpenCV’s though.
- The pedestrian detectors provided by OpenCV are not used to detect people in dense crowds. For that you should consider applying face detection; specifically methods that are tuned to dense crowds. Deep learning has had some success here.

- https://medium.com/@mithi/vehicles-tracking-with-hog-and-linear-svm-c9f27eaf521a

### Keeywords
* NMS - non-maximum suppression
	- to remove redundant and overlapping bounding boxes.

## Interfacing openCV+python with Web Interface
- http://www.pyimagesearch.com/2015/05/11/creating-a-face-detection-api-with-python-and-opencv-in-just-5-minutes/


## Q&A from Blog Comments
- So if I understand your question correctly, you are using a background that is lighter than the shapes themselves? And after thresholding your shapes appear as “black” on a “white” background? Am I understanding that correctly? If so, simply invert the threshold step to make the shapes “white” on a “black” background.

* **I only want to detect the shapes and ignore all the text in the image.**
++Adrian Rosebrock++: I would compute the solidity of the shape which is the area of the contour divided by the convex hull area. Text will have a lower solidity than a rectangle which should be equal to one.

* **In my image, I have a square and lozenge shape and I want to distinguish between them, how can I do that?**
++Adrian Rosebrock++: I would suggest using either:
1. Contour properties, such as extent, solidity, and aspect ratio.
2. Features, such Hu Moments or Zernike Moments.

* **Is there a way to save the results of the image classification into a new image?**
++Adrian Rosebrock++: if you are trying to extract each individual square, I would compute the bounding box and extract it using array slicing. You can then write the region to disk using the `cv2.imwrite `function.


* **i apply GLCM texture feature, the output is matrix, is this feature vector?**
++Adrian Rosebrock++: Typically, the GLCM matrix isn’t used directly as a feature vector. You instead compute statistics on this matrix, such as Haralick texture. The mahotas library has a good implementation of Haralick texture features.

* **detect pedestrian in a gray-scale image**
For pedestrian detection you typically wouldn’t use the grayscale pixels values. It would be better to extract features from the image, normally Histogram of Oriented Gradients and then train a pedestrian detector on these features.

## Matplot and Images
* http://www.pyimagesearch.com/2014/11/03/display-matplotlib-rgb-image/
* http://docs.opencv.org/trunk/d1/db7/tutorial_py_histogram_begins.html

## Digital Photography, Images & Histograms
* http://www.cambridgeincolour.com/tutorials.htm
* http://www.cambridgeincolour.com/tutorials/histograms1.htm
* http://www.cambridgeincolour.com/tutorials/bit-depth.htm
* http://www.cambridgeincolour.com/tutorials/histograms2.htm

### Histograms
* http://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram.html

- A histogram can tell you whether or not your image has been properly exposed, whether the lighting is harsh or flat, and what adjustments will work best.
- Each pixel in an image has a color which has been produced by some combination of the primary colors red, green, and blue (RGB).
- Each of these colors can have a **brightness value ranging from 0 to 255 for a digital image with a bit depth of 8-bits**.
- A RGB histogram results when the computer scans through each of these RGB brightness values and counts how many are at each level from 0 through 255.
- http://www.cambridgeincolour.com/tutorials/image-noise.htm
- An extension to the histogram, the color correlogram, can be used to encode a spatial relationship amongst pixels.

**Drawbacks**
- color histograms, by definition ignore both the shape and texture of the object(s) in the image.
- histograms also disregard any spatial information (i.e. where in the image the pixel value came from)
- color histograms simply have no way to “model” what a shoe or a shirt is.
- color histograms are sensitive to “noise”, such as changes in lighting in the environment the image was captured under and quantization errors (selecting which bin to increment). Some of these limitations can potentially be mitigated by using a different color space than RGB (such as HSV or L*a*b*).

**conclusion**
- Histograms are still widely used as image descriptors.
- They are dead simple to implement and very fast to compute.
- And while they have their limitations, they are very powerful when used correctly and in the right context.

* I wanted an **equal density histogram** for my research purpose. Is there some way of specifying the bins with calcHist rather than the size of the bin. I **donot want equal sized bins**.If the first bin is from 1 to 10 then the second may be from 11to 16 and so on.
++Adrian Rosebrock++: If you’re looking for non-equal sized bins, I probably wouldn’t use the cv2.calcHist function for this. Instead, the NumPy’s histogram function will give you the fine-grained control that you’re looking for.

#### Types
* RGB HISTOGRAMS
* LUMINANCE HISTOGRAMS (luminosity histograms)
* COLOR HISTOGRAMS

### Tones
- The region where most of the brightness values are present is called the "tonal range."
- histograms should merely be representative of the tonal range in the scene
- Conditions of ordinary and even lighting, when combined with a properly exposed subject, will usually produce a histogram which peaks in the center, gradually tapering off into the shadows and highlights.

### HIGH AND LOW KEY IMAGES
- Although most cameras will produce midtone-centric histograms when in an automatic exposure mode, the distribution of peaks within a histogram also depends on the tonal range of the subject matter
- Images where most of the tones occur in the shadows are called "low key," whereas with "high key" images most of the tones are in the highlights.
- Since cameras measure reflected as opposed to incident light, they are unable to assess the absolute brightness of their subject.
- Before the photo has been taken, it is useful to assess whether or not your subject matter qualifies as high or low key. Since cameras measure reflected as opposed to incident light, they are unable to assess the absolute brightness of their subject. As a result, many cameras contain sophisticated algorithms which try to circumvent this limitation, and estimate how bright an image should be. These estimates frequently result in an image whose average brightness is placed in the midtones. This is usually acceptable, however high and low key scenes frequently require the photographer to manually adjust the exposure, relative to what the camera would do automatically. A good rule of thumb is that you will need to manually adjust the exposure whenever you want the average brightness in your image to appear brighter or darker than the midtones.
- **Detail can never be recovered when a region becomes so overexposed that it becomes solid white. When this occurs the highlights are said to be ++"clipped"++ or ++"blown"++.**
- The histogram is a good tool for knowing whether clipping has occurred since you can readily see when the highlights are pushed to the edge of the chart. Some clipping is usually ok in regions such as specular reflections on water or metal, when the sun is included in the frame or when other bright sources of light are present. Ultimately, the amount of clipping present is up to the photographer and what they wish to convey.

### CONTRAST
Contrast is a measure of the difference in brightness between light and dark areas in a scene.
- A histogram can also describe the amount of contrast.
- Broad histograms reflect a scene with significant contrast, whereas narrow histograms reflect less contrast and may appear flat or dull.
- Contrast can have a significant visual impact on an image by emphasizing texture.
- The high contrast water has deeper shadows and more pronounced highlights, creating texture which "pops" out at the viewer.
- Contrast can also vary for different regions within the same image due to both subject matter and lighting.
- directly exposed areas have higher contrast. 
- areas in the scene with diffuse, reflected light have lower contrast.

### Luminosity & Color
Although RGB histograms are the most commonly used histogram, other types are more useful for specific purposes.
* **how luminosity and color both vary within an image? , and how this translates into the relevant histogram.**
* Luminance* histograms are more accurate than RGB histograms at describing the perceived brightness distribution or "luminosity" within an image.
* Luminosity takes into account the fact that the human eye is more sensitive to green light than red or blue light.
* **Luminance refers to the absolute amount of light emitted by an object per unit area, whereas luminosity refers to the perceived brightness of that object by a human observer.**
* luminosity histograms keep track of the location of each color pixel, RGB histograms discard this information.
* An RGB histogram produces three independent histograms and then adds them together, irrespective of whether or not each color came from the same pixel.
* Whereas RGB and luminance histograms use all three color channels, a color histogram describes the brightness distribution for any of these colors individually. This can be more helpful when trying to assess whether or not individual colors have been clipped.
* Regions where individual color channels are clipped lose all texture caused by that particular color. However, these clipped regions may still retain some luminance texture if the other two colors have not also been clipped.
* Individual color clipping is often not as objectionable as when all three colors clip, although this all depends upon what you wish to convey.


## Tips about OpenCV
* When accessing pixel values in OpenCV + NumPy, you actually specify them in (y, x) order rather than (x, y) order. Thus, you need to use: image[cY, cX]
* OpenCV represents RGB images as multi-dimensional NumPy arrays…but in reverse order! This means that images are actually represented in BGR order rather than RGB!
* cv2.findContours method is implemented to scan from bottom to top. If you would like to sort contours,
* The cv2.findContours function will not return contours in a specific order. You should sort your contours if you expect them to be in a given order.
* split the image into its three channels: blue, green, and red. Normally, we read this is a red, green, blue (RGB). However, OpenCV stores the image as a NumPy array in reverse order: BGR. This is important to note. We then initialize a tuple of strings representing the colors.
* 2D histogram stored in OpenCV as a 2D NumPy array

## OpenCV Snippets
```python
(B, G, R) = cv2.split(image)
merged = cv2.merge([B, G, R])
```
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image = mpimg.imread("chelsea-the-cat.png")
plt.imshow(image)
plt.show()


### OpenCV functions Used

```python
import cv2

# cv2.imread, cv2.imshow, cv2.imwrite
## read, show and write image
image=cv2.imread(imagePath)
# cv2.split
## split the image in three channels (b,g,r)
channels=cv2.split(image)

# Histogram
## cv2.calcHist(images, channels, mask, histSize, ranges)

```


## Tips on Image Processing Concepts
* Blurring (also called “smoothing”) is used to smooth high frequency noise in the image. Simply put, this allows us to ignore the details in the image and focus on what matters — the shapes. So by blurring, we smooth over less interesting regions of the image, allowing the thresholding and contour extraction phase to be more accurate.
* Regions of an image can be characterized by both color histograms and by basic color channel statistics such as mean and standard deviation.
* If we used a 256 bins for each dimension in a 2D histogram, our resulting histogram would have 65,536 separate pixel counts. Not only is this wasteful of resources, it’s not practical. Most applications using somewhere between 8 and 64 bins when computing multi-dimensional histograms.

# Video Processing
* http://www.pyimagesearch.com/2016/01/04/unifying-picamera-and-cv2-videocapture-into-a-single-class-with-opencv/

## Extras
* [install-opencv-3-0-and-python-2-7-on-ubuntu](http://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-python-2-7-on-ubuntu/)
* [python-command-line-arguments-argv-example](https://www.cyberciti.biz/faq/python-command-line-arguments-argv-example/)
* [Resolved: Matplotlib figures not showing up or displaying](http://www.pyimagesearch.com/2015/08/24/resolved-matplotlib-figures-not-showing-up-or-displaying/)


## Maths & Stats
* https://en.wikipedia.org/wiki/Histogram
* https://en.wikipedia.org/wiki/Data_binning

## Keywords
* CBIR - Content Based Image Retrieval systems

## Photogrammetry, Land Mobile Mapping Systems
* https://books.google.co.in/books?id=tWUfPdng_o0C&pg=PA143&lpg=PA143&dq=georefering+coordinate+quantization&source=bl&ots=dIYRLPxXbR&sig=xLL1W6mDe8fMhBCGfp0kL7csQgI&hl=en&sa=X&ved=0ahUKEwiF6KiAqfDUAhXFPo8KHQRBC1MQ6AEIPjAE#v=onepage&q=georefering%20coordinate%20quantization&f=false

- parameters that care critical to properly operating a mobile mapping system for different platforms
  - sensor placement
  - sensor synchronization
  - system calubation
  - sensors' initial alignment
- The road edge detection procedure is based on the integration of the extended Kalman filther with the Canny edge detector and the Hough transform
- Kalman filter is suitable for the real-time evaluation of multi0sensor system integration

## Further Readings
* https://en.wikipedia.org/wiki/Hough_transform

### Blogs
* http://www.computervisionblog.com/2011/08/blazing-fast-nmsm-from-exemplar-svm.html

### github
https://github.com/huyouare/CS231n

## image-recognition-and-object-detection-part1
- http://www.learnopencv.com/image-recognition-and-object-detection-part1/
- https://github.com/huyouare/CS231n/blob/master/assignment1/cs231n/features.py
- http://www.learnopencv.com/histogram-of-oriented-gradients/

### Udacity Self-Driving Card Nano Degree
* https://github.com/udacity/CarND-Term1-Starter-Kit
* https://github.com/SealedSaint/CarND-Term1-P1
* https://github.com/priya-dwivedi/CarND
* https://medium.com/towards-data-science/automatic-vehicle-detection-for-self-driving-cars-8d98c086b161
* https://medium.com/@MSqalli/lane-detection-446986c44021

## Detecting Lane Lines

* 1st implementation pipeline major steps:
	- Grayscale
	- Gaussian Blur
	- Canny Edge Detection
	- Region of Interest — Create Vertices
	- Hough Transform — Average Lines
	- Draw Lines


* 2nd implementation pipeline major steps:
	- Distortion correction
	- Create a binary image

Image distortion occurs when a camera looks at 3D objects in the real world and transforms them into a 2D image. This transformation isn’t always perfect and distortion can result in a change in apparent size, shape or position of an object. So we need to correct this distortion to give the camera an accurate view of the image. This is done by computing a camera calibration matrix by taking several chessboard pictures of a camera and using cv2.calibrateCamera() function.


## Image Processing
- http://www.bogotobogo.com/python/python_numpy_batch_gradient_descent_algorithm.php
- http://www.scipy-lectures.org/
- https://www.scipy.org/scikits.html
- http://scikit-image.org/

**scikit-image**
- scikit-image is a Python package dedicated to image processing, and using natively NumPy arrays as image objects.
- For basic image manipulation, such as image cropping or simple filtering, a large number of simple operations can be realized with NumPy and SciPy only

## Deep Learning
* https://github.com/cvjena/cn24


## Maths
* **how the histogram is normalized?**
* **how a vector of length 3 is normalized?**
	* Let's say we have a RGB color vector [ 128, 64, 32 ]. The length of this vector is $\sqrt{128^2 + 64^2 + 32^2}$ = 146.64. This is also called the L2 norm of the vector. Dividing each element of this vector by 146.64 gives us a normalized vector [0.87, 0.43, 0.22]. 
	* normalizing a vector removes the scale.

## Datasets
- http://vasc.ri.cmu.edu/idb/html/face/frontal_images/
- [INRIA Person Dataset](http://pascal.inrialpes.fr/data/human/)
- Vechile Datasets
	- http://www.gti.ssr.upm.es/data/Vehicle_database.html
- Traffic Sign, Vechine Datasets
	- [LISA](http://cvrr.ucsd.edu/LISA/datasets.html)
	- [BelgiumTSC](http://btsd.ethz.ch/shareddata/)
- http://groups.csail.mit.edu/vision/datasets/ADE20K/

## sklearn
- http://scikit-learn.org/stable/tutorial/basic/tutorial.html#learning-and-predicting

* scikit-learn works on any numeric data stored as numpy arrays or scipy sparse matrices. Other types that are convertible to numeric arrays such as pandas DataFrame are also acceptable.
* scikit-learn comes with a few standard datasets, for instance the iris and digits datasets for classification and the boston house prices dataset for regression.
* A dataset is a dictionary-like object that holds all the data and some metadata about the data. This data is stored in the `.data` member, which is a `n_samples`, `n_features` array.
* In the case of supervised problem, one or more response variables are stored in the `.target` member.
* The data is always a 2D array, shape (n_samples, n_features)

### Model Persistance
- http://scikit-learn.org/stable/modules/model_persistence.html#model-persistence
- http://thiagomarzagao.com/2015/12/07/model-persistence-without-pickles/
- https://stackoverflow.com/questions/10592605/save-classifier-to-disk-in-scikit-learn

After training a scikit-learn model, it is desirable to have a way to persist the model for future use without having to retrain.

In order to rebuild a similar model with future versions of scikit-learn, additional metadata should be saved along the pickled model:
- The training data, e.g. a reference to a immutable snapshot
- The python source code used to generate the model
- The versions of scikit-learn and its dependencies
- The cross validation score obtained on the training data

This should make it possible to check that the cross-validation score is in the same range as before.

## What is Openscouring?
- http://openscoring.io/
- Predictive Model Markup Language (PMML)

### Need for openscouring, PMML!!
- https://news.ycombinator.com/item?id=7903634
- From what I understand they want to persist the trained model in a language independent way, so you can train the models with whatever language or framework you wish and then save it to a format that can be used by any other language or framework to classify unseen instances.

### What does your production machine learning pipeline look like?
- https://news.ycombinator.com/item?id=13821217

**What the heck is data turking?**
- Using something like Mechanical Turk to manually add ground truth data to something, though we don't use Mechanical Turk but rather other providers.

- https://blogs.dropbox.com/tech/2016/08/fast-and-accurate-document-detection-for-scanning/
**DNNs are quite expensive, both in terms of computation time and memory usage. Therefore, they are usually difficult to deploy on mobile devices.**

**Canny Edge Detection**
- https://en.wikipedia.org/wiki/Canny_edge_detector

**Hough Transform**
- https://en.wikipedia.org/wiki/Hough_transform
- https://en.wikipedia.org/wiki/Duality_(mathematics)
Once we have an accurate edge map, we’d like to find straight lines in it. For this, we use the venerable Hough transform, a technique that lets individual data points “vote” for likely solutions to a set of equations

**OCR**
- https://blogs.dropbox.com/tech/2017/04/creating-a-modern-ocr-pipeline-using-computer-vision-and-deep-learning/
- Optical Character Recognition (OCR) pipeline for our mobile document scanner. We used computer vision and deep learning advances such as bi-directional Long Short Term Memory (LSTMs), Connectionist Temporal Classification (CTC), convolutional neural nets (CNNs)
-  the need to apply Optical Character Recognition, or OCR. This process extracts actual text from our doc-scanned image. Once OCR is run, we can then enable the following features
	- Extract all the text in scanned documents and index it, so that it can be searched for later
	- Create a hidden overlay so text can be copied and pasted from the scans saved as PDFs
- we built the first version of the mobile document scanner, we used a commercial off-the-shelf OCR library, in order to do product validation before diving too deep into creating our own machine learning-based OCR system.
- First, there was a cost consideration: having our own OCR system would save us significant money as the licensed commercial OCR SDK charged us based on the number of scans
- Second, the commercial system was tuned for the traditional OCR world of images from flat bed scanners, whereas our operating scenario was much tougher, because mobile phone photos are far more unconstrained, with crinkled or curved documents, shadows and uneven lighting, blurriness and reflective highlights, etc. Thus, there might be an opportunity for us to improve recognition accuracy.
- Traditionally, OCR systems were heavily pipelined, with hand-built and highly-tuned modules taking advantage of all kinds of conditions they could assume to be true for images captured using a flatbed scanner. For example, one module might find lines of text, then the next module would find words and segment letters, then another module might apply different techniques to each piece of a character to figure out what the character is, etc. Most methods rely on binarization of the input image as an early stage, and this can be brittle and discards important cues. The process to build these OCR systems was very specialized and labor intensive, and the systems could generally only work with fairly constrained imagery from flat bed scanners.
- Perhaps the most important reason for building our own system is that it would give us more control over own destiny, and allow us to work on more innovative features in the future.

Most commercial machine learning projects follow three major steps:
- Research and prototyping to see if something is possible
- Productionization of the model for actual end users
- Refinement of the system in the real world

**Research and Prototyping**
Our initial task was to see if we could even build a state of the art OCR system at all.




**Dropbox Case study**
- https://blogs.dropbox.com/tech/2016/08/fast-and-accurate-document-detection-for-scanning/

## Commercial AI Services
- https://www.crowdflower.com/use-case/image-annotation/



- https://apihandyman.io/do-you-really-know-why-you-prefer-rest-over-rpc/

The actual OCR service uses OpenCV and TensorFlow, both written in C++ and with complicated library dependencies; so security exploits are a real concern. We’ve isolated the actual OCR portion into jails using technologies like LXC, CGroups, Linux Namespaces, and Seccomp to provide isolation and syscall whitelisting, using IPCs to talk into and out of the isolated container. If someone compromises the jail they will still be completely separated from the rest of our system.

## Deep Learning in Computer Vision
- https://www.coursera.org/learn/ml-foundations/lecture/xpkT7/application-of-deep-learning-to-computer-vision

## Learnign Resources

### CUDA, GPU, Python - How To
- https://developer.nvidia.com/how-to-cuda-python
- https://nvidia.qwiklab.com/quests/6?locale=en

## Uses Cases for VidTeq/MMI
### Text form the photographs
- POI - autofill
- Number Plate Masking - Automatic License Plate Recognition system (ALPR)

### Needle in Haystack problems
#### Image Categorization/Classification
- Poi
- Traffic Sign Detection and extraction

#### Structure Segmentation and Re-construction
- Road Edges, Lanes

# POC - Proof of Concepts

## Traffic Sign Detection
- https://medium.com/@waleedka/traffic-sign-recognition-with-tensorflow-629dffc391a6

## Take Away

1. finding the optimal architecture of a ConvNet for a given task remains mainly empirical
2. **Occam's razor**: Given two models that perform more or less equally, you should always prefer the one that is less complex.
3. convolutional neural networks in some uses cases have outperformed human accuracy levels
4. convolutional neural networks are still computationally very demanding
5. When the data is small, deep learning algorithms don’t perform that well. This is because deep learning algorithms need a large amount of data to understand it perfectly
6. In Machine learning, most of the applied features need to be identified by an expert and then hand-coded as per the domain and data type.
7. Deep learning algorithms try to learn high-level features from data. This is a very distinctive part of Deep Learning and a major step ahead of traditional Machine Learning. Therefore, deep learning reduces the task of developing new feature extractor for every problem.
8. State of the art deep learning algorithm ResNet takes about two weeks to train completely from scratch. Whereas machine learning comparatively takes much less time to train, ranging from a few seconds to a few hours.
9. This is turn is completely reversed on testing time. At test time, deep learning algorithm takes much less time to run. Whereas, if you compare it with k-nearest neighbors (a type of machine learning algorithm), test time increases on increasing the size of data. Although this is not applicable on all machine learning algorithms, as some of them have small testing times too.

https://www.analyticsvidhya.com/blog/2017/04/comparison-between-deep-learning-machine-learning/
https://www.analyticsvidhya.com/learning-path-learn-machine-learning/
https://www.analyticsvidhya.com/blog/2016/08/deep-learning-path/
http://www.kdnuggets.com/2016/04/deep-learning-vs-svm-random-forest.html
https://www.quora.com/Will-deep-learning-make-other-Machine-Learning-algorithms-obsolete

___
# Math
**Singular Value Decomposition (SVD)**
* https://en.wikipedia.org/wiki/Singular_value_decomposition
* https://diego.assencio.com/?index=82209f7b8bc7c143f4419238ef16c129
* http://www.frankcleary.com/svd/
* http://www.frankcleary.com/svdimage/

In linear algebra, the singular value decomposition (SVD) is a factorization of a real or complex matrix.
- The SVD of an m×nm×n real matrix AA is the factorization A=UΣVTA=UΣVT, where UU is an m×mm×m real orthogonal matrix, ΣΣ is an m×nm×n diagonal matrix with real nonnegative values along its diagonal (called the singular values of AA) and VV is an n×nn×n real orthogonal matrix. Every matrix has an SVD
```python
import numpy as np

np.linalg.svd(A,full_matrices=false)
```

**Applications of SVD**
* This has applications in image compression
* Reducing the dimensionality of data by selecting the most import components.
* Singular value decomposition can be used to classify similar objects (for example, news articles on a particular topic).  $\vec a_i$'s will have similar  $\vec v_i$'s. Recall that  a⃗ i=U∗Σ∗v⃗ ia→i=U∗Σ∗v→i , that is each column  v⃗ iv→i  of  VV  defines the entries in that column,  a⃗ ia→i , of our data matrix,  AA . Let's label V with the identities of the posts using a DataFrame
* VV  can be displayed as an image. Notice how the similar posts (1 and 4, 2 and 3) have similar color values in the first two rows

## Terms and Definitions
**Homogeneous Coordinates** Or **Projective Coordinates**
* coordinates in projective space are called "homogeneous coordinates."
* Projective geometry has an extra dimension, called WW, in addition to the XX, YY, and ZZ dimensions
* For the purposes of 3D software, the terms "projective" and "homogeneous" are basically interchangeable with "4D."
* Quaternions look a lot like homogeneous coordinates. Both are 4D vectors, commonly depicted as (X,Y,Z,W)(X,Y,Z,W). However, quaternions and homogeneous coordinates are different concepts, with different uses.

**References**
- https://en.wikipedia.org/wiki/Homogeneous_coordinates
-  They have the advantage that the coordinates of points, including points at infinity, can be represented using finite coordinates.
- easily represented by a matrix

**Projective Geometry, Space, Plane**
- https://en.wikipedia.org/wiki/Projective_geometry
- https://en.wikipedia.org/wiki/Projective_space
- https://en.wikipedia.org/wiki/Projective_plane
- http://www.nptel.ac.in/courses/Webcourse-contents/IIT-Delhi/Computer%20Aided%20Design%20&%20ManufacturingI/mod2/06.htm
- http://www.tomdalling.com/blog/modern-opengl/explaining-homogenous-coordinates-and-projective-geometry/
- https://math.stackexchange.com/questions/1339676/what-is-homogeneous-coordinates-why-is-it-necessary-in-2d-transformation


# Book Notes: Computer Vision Algorithims and Application

For example, if someone comes to me and asks for a good edge detector, my first question is usually to ask why? What kind of problem are they trying to solve and why do they believe that edge detection is an important component?

If they are trying to locate faces, I usually point out that most successful face detectors use a combination of skin color detection (Exercise 2.8) and simple blob features Section 14.1.1; they do not rely on edge detection.

If they are trying to match door and window edges in a building for the purpose of 3D reconstruction, I tell them that edges are a fine idea but it is better to tune the edge detector for long edges (see Sections 3.2.3 and 4.2) and link them together into straight lines with common vanishing points before matching.

Thus, it is better to think back from the problem at hand to suitable techniques, rather than to grab the first technique that you may have heard of. This kind of working back from problems to solutions is typical of an engineering approach to the study of vision and reflects my own background in the field.

* First, I come up with a detailed problem definition and decide on the constraints and specifications for the problem.
* Then, I try to find out which techniques are known to work, implement a few of these, evaluate their performance.
* Finally make a selection.
* In order for this process to work, it is important to have realistic test data, both synthetic, which can be used to verify correctness and analyze noise sensitivity, and real-world data typical of the way the system will finally be used.
* The book often uses a statistical approach to formulating and solving computer vision problems. Where appropriate, probability distributions are used to model the scene and the noisy image acquisition process.
* physics, Euclidean and projective geometry, statistics, and optimization.

## Chapter 2
Geometric image formation (Section 2.1) deals with points, lines, and planes, and how these are mapped onto images using projective geometry and other models (including radial lens distortion).
Photometric image formation (Section 2.2) covers radiometry, which describes how light interacts with surfaces in the world, and optics, which projects light onto the sensor plane.
Finally, Section 2.3 covers how sensors work, including topics such as sampling and aliasing, color sensing, and in-camera compression

* vectors $\textbf v$ are lower case **bold**
* matrices $\textbf M$ are UPPER case **bold**
* scalars $\textit (T, s)$ are Mixed case *italic*
* Unless otherwise noted, vectors operate as column vectors, i.e., they post-multiply matrices, M v, although they are sometimes written as comma-separated parenthesized lists x = (x, y) instead of bracketed column vectors $\textbf x = [x \space y]^T$
* Some commonly used matrices are $\textbf R$ for rotations, $\textbf K$ for calibration matrices, and $\textbf I$ for the identity matrix
* Homogeneous coordinates (Section 2.1) are denoted with a tilde over the vector, e.g., $\tilde x= (\tilde x, \tilde y,\tilde w) = \tilde w(x, y, 1) = \tilde w \mathbf{\bar x}\space in\space P^2$. The cross product operator in matrix form is denoted by [ ] × .

### MathJax Notations
* Eg
> $\mathbf{\vec X} = \left[x_1,x_2,\ldots,x_n \right]^T$
>`$\mathbf{\vec X} = \left[x_1,x_2,\ldots,x_n \right]^T$`
* Eg
>$\tilde x= (\tilde x, \tilde y,\tilde w) = \tilde w(x, y, 1) = \tilde w \mathbf{\bar x}\space in\space P^2$
>`$\tilde x= (\tilde x, \tilde y,\tilde w) = \tilde w(x, y, 1) = \tilde w \mathbf{\bar x}\space in\space P^2$`



# Online Course Materials and ebooks

* http://www.connellybarnes.com/work/class/2017/intro_vision/
* http://web.stanford.edu/class/cs231a/
* http://www.cs.utoronto.ca/~fidler/teaching/2017/CSC420.html
* http://www.cs.ubc.ca/~nando/340-2008/lectures/l4.pdf
* http://cms.brookes.ac.uk/staff/FabioCuzzolin/files/week3.pdf
* http://inside.mines.edu/~whoff/courses/EENG512/lectures/
* http://www.cs.washington.edu/education/courses/455/
* http://www.cs.washington.edu/education/courses/576/
* http://vision.stanford.edu/teaching/cs223b/
* http://www.cs.washington.edu/education/courses/558/06sp/
* http://graphics.cs.cmu.edu/courses/15-463/
* **Computer Graphics**
	* https://graphics.stanford.edu/courses/cs348b-03/readings.html

[Python]
* http://cs231n.github.io/python-numpy-tutorial/
* http://www.pyimagesearch.com/2014/01/12/my-top-9-favorite-python-libraries-for-building-image-search-engines/
* http://www.ma.iup.edu/~hedonley/math122/image/
* [skimage](http://tonysyu.github.io/scikit-image/api/skimage.io.html)
* http://www.unixuser.org/~euske/python/pdfminer/
>PDFMiner is a tool for extracting information from PDF documents. Unlike other PDF-related tools, it focuses entirely on getting and analyzing text data.

**Books**
* **Computer Vision**
	- http://szeliski.org/Book/
	- Ballard and Brown 1982;
	- Faugeras 1993; Nalwa 1993; Trucco and Verri 1998; Forsyth
and Ponce 2003).
* **Math**
	- (Golub and Van Loan 1996) for matrix algebra
	- (Strang 1988) for linear algebra
* **Image Processing**
	- image processing, there are a number of popular textbooks, including
		- Crane 1997
		- Gomes and Velho 1997
		- Jähne 1997
		- Pratt 2007
		- Russ 2007
		- Burger and Burge 2008
		- Gonzales and Woods 2008
* **Statistics and Machine Learning**
	- Chris Bishop’s (2006)
	>This book is a wonderful and comprehensive introduction with a wealth of exercises.
* **Computer Graphics**
	- http://dept.cs.williams.edu/~morgan/cgpp/about.xml
	- computer graphics (Foley, van Dam, Feiner et al. 1995)

**Research Groups**
* http://vision.in.tum.de/data/software
* http://graphics.stanford.edu/papers/aerial_scanning/
* https://www.microsoft.com/en-us/research/research-area/computer-vision/

**Business Applications**
* http://www.cs.ubc.ca/~lowe/vision.html

**Navvis**
* http://www.navvis.com/markets/overview/

## SfM vs SLAM
http://www.computervisionblog.com/2016/01/why-slam-matters-future-of-real-time.html
http://www.cs.cmu.edu/~hebert/geom.html


## Hardware Configuration
https://www.quora.com/Ill-be-using-my-computer-for-heavy-computation-computer-vision-algorithms-training-and-neural-nets-What-would-be-a-good-configuration-for-a-PC-laptop

I use to work with 13Mpx to 6K, 16b raw images or video sequences. Here are the specifications I recommend for such work:
* > 16Gb RAM: it will be really important in order to be able to process a lot of data simultaneously
* Big storage space, with a size depending on what you have to store. It might be located on a shared network. My experience showed me that unless you write a lot of temporary data, SSD disk are not really useful to improve performance.
* Multi-core processor: that is important if you want to used OpenMP and to process easily some of your heaviest algorithms on several threads.
* The GPU is not really important. You just have to pick a chipset that support your favorite parallel computing platform (CUDA, OpenCL...).

That seem to be the minimum requirements in order to work with a lot of images. Sometimes, when I need to process a lot of images with very complex algorithm destined to be hard coded on an ASIC chip, I need more power. Therefore I send jobs on about ten computers all night and get the resulting images the next morning.


https://www.quora.com/What-laptop-computer-should-I-purchase-for-deep-learning-How-much-will-it-cost

So laptop wise I would find the cheapest nvidia gtx 1080 laptop

However, if you want to train lots of small networks, or do some basic training before deploying your training script on a heavy machine, and are hell bent on buying a laptop for training, I’d suggest you buy a gaming laptop.

Asus and Acer have good options here. You can run Linux on it like a pro.
These have decent GPUs, and give you good performance for training small networks.
This is more convenient than setting up an external GPU on another laptop.


https://cloud.google.com/blog/big-data/2017/05/an-in-depth-look-at-googles-first-tensor-processing-unit-tpu

**CudaVsOpenCL**
https://wiki.tiker.net/CudaVsOpenCL

https://ai.google 
http://www.nvidia.com/object/imaging_comp_vision.html

## Getting started - build Image Processing based website
[Ref: 1](https://www.quora.com/How-can-I-build-a-website-using-Python-to-do-image-processing-and-machine-learning)
For the problem of using an X-ray dataset to identify a disease, and build a website around it, here are the technologies and skills you’ll want to start with.

1. [Python programming with OpenCV](http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html) : This will allow you to do things like read in image files, manipulate them, and read images into your code (as matrices of RGB values).
2. Basic machine learning — Check out this beginner course on machine learning algorithms : [Machine Learning | Coursera](https://www.coursera.org/learn/machine-learning). This will allow you to learn how to extract features from the X-ray images and train a classifier using these features and labels for each of the images
3. Once you have some of the basics, you can move on to using libraries to do the actual machine learning work such as [Scikit-learn](http://scikit-learn.org/stable/tutorial/index.html) — you can extract your features and port them into one of the classifiers that are pre-built, and obtain a trained model you can then use to predict classes for future data.
4. Python web programming via [Django](https://docs.djangoproject.com/en/1.11/intro/tutorial01/) or [Flask](http://flask.pocoo.org/docs/0.12/tutorial/) to create a web server and a frontend HTML page to upload images, transform them to a matrix, extract features, and predict a class using the classifier built in 3) . The result can then be shown to the user.

## Tutorial in Web application development
https://towardsdatascience.com/how-to-build-a-machine-learning-as-a-rails-developer-739cc57ea01c

Rather than having a complicated machine learning application that did some complicated neural network-deep learning-artificial intelligence-stochastic gradient descent-linear regression-bayesian machine learning magic


## Blog posts
https://towardsdatascience.com/my-next-two-years-de448d3141a

## Open Courses
https://web.stanford.edu/class/cs377s/syllabus.htm

## Computer Vision in browser
https://docs.opencv.org/trunk/df/d0a/tutorial_js_intro.html

Web Virtual Reality (WebVR) and Augmented Reality (WebAR)


Emscripten is an LLVM-to-JavaScript compiler. It takes LLVM bitcode - which can be generated from C/C++ using clang, and compiles that into asm.js or WebAssembly that can execute directly inside the web browsers. . Asm.js is a highly optimizable, low-level subset of JavaScript. Asm.js enables ahead-of-time compilation and optimization in JavaScript engine that provide near-to-native execution speed. WebAssembly is a new portable, size- and load-time-efficient binary format suitable for compilation to the web. WebAssembly aims to execute at native speed. WebAssembly is currently being designed as an open standard by W3C.