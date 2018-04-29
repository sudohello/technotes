/*
Title: CBIR
Decription: CBIR
Author: Bhaskar Mangal
Date: 28th Apr 2018
Tags: CBIR
*/

## CBIR or ge Search Engine

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

## Create a CBIR (content based image retrival) system
Feature extraction for content based image retrieval
The key point about content based image retrieval is the feature extraction.

- https://blog.sicara.com/keras-tutorial-content-based-image-retrieval-convolutional-denoising-autoencoder-dc91450cc511

The features correspond to the way we represent an image on a high level. How to describe the colours on an image? Its texture? The shapes on it? The features we extract should also allow an efficient retrieval of the images. This is especially true if we have a big image database.

**Many ways to extract these features**
1. One way is to use what we call hand crafted features. Examples are:
	a. histogram of colours **to define colours**
	b. histogram of oriented gradients (HOG) **to define shapes**
2. Other descriptors like SIFT and SURF have proven to be robust **for image retrieval applications**
3. Another possibility is to use deep learning algorithms




## Software Issuses
**python-tk**
https://stackoverflow.com/questions/20044559/how-to-pip-or-easy-install-tkinter

    raise ImportError, str(msg) + ', please install the python-tk package'
ImportError: No module named _tkinter, please install the python-tk package


Traceback (most recent call last):
  File "hog.py", line 3, in <module>
    from skimage.feature import hog
ImportError: No module named skimage.feature

    image = color.rgb2gray(data.astronaut())
AttributeError: 'module' object has no attribute 'astronaut'
- https://github.com/scikit-image/scikit-image/issues/1326


```bash
# tkinter
#http://www.tkdocs.com/tutorial/install.html
sudo apt install python-tk
# scikit
#http://scikit-image.org/docs/dev/install.html
sudo apt-get install python-skimage
sudo apt remove --purge python-skimage
#
pip uninstall scikit-learn
#
sudo -H pip install scikit-learn
# http://scikit-image.org/docs/0.12.x/install.html
sudo -H pip install scikit-image
```

import sklearn
sklearn.__path__
dir(sklearn)

## Questions
* What is feed forward neural network
* What are HOG descriptors used to describe?
HOG descriptors are mainly used to describe the structural shape and appearance of an object in an image, making them excellent descriptors for object classification. However, since HOG captures local intensity gradients and edge directions, it also makes for a good texture descriptor.
- https://gurus.pyimagesearch.com/lesson-sample-histogram-of-oriented-gradients-and-car-logo-recognition/