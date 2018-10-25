---
Title: CBIR
Decription: CBIR
Author: Bhaskar Mangal
Date: 28th Apr 2018
Tags: CBIR
---

**Table of Contents**
* TOC
{:toc}


## CBIR or Image Search Engine

* http://www.pyimagesearch.com/2014/01/27/hobbits-and-histograms-a-how-to-guide-to-building-your-first-image-search-engine-in-python/
* http://www.pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/
* http://www.pyimagesearch.com/2014/01/15/the-3-types-of-image-search-engines-search-by-meta-data-search-by-example-and-hybrid/

**PPTs**
* https://www.slideshare.net/xavigiro/d1l5-contentbased-image-retrieval-upc-2018-deep-learning-for-computer-vision
* https://en.wikipedia.org/wiki/Recommender_system#Content-based_filtering

### Building an image search service from scratch
> The unreasonable effectiveness of Deep Learning Representations

* we can search for similar images in a broad way
* or by conditioning on a particular class our model was trained on

* https://blog.insightdatascience.com/the-unreasonable-effectiveness-of-deep-learning-representations-4ce83fc663cf
* https://twitter.com/EmmanuelAmeisen
* https://github.com/hundredblocks/semantic-search
-  building your own representations, both for image and text data, and efficiently do similarity Search

There is a simpler method, which is similar to word embeddings. If we find an expressive vector representation, or embedding for images, we can then calculate their similarity by looking at how close their vectors are to each other. This type of search is a common problem that is well studied, and many libraries implement fast solutions (we will use Annoy here). In addition, if we calculate these vectors for all images in our database ahead of time, this approach is both fast (one forward pass, and an efficient similarity search), and scalable. Finally, if we manage to find common embeddings for our images and our words, we could use them to do text to image search!

1. **How do we actually use deep learning representations to create a search engine?**

**Goals:**
* To have a search engine that can take in images and output either similar images or tags,
* And, take in text and output similar words, or images.


To get there, we will go through three successive steps:

- Searching for similar images to an input image (Image → Image)
- Searching for similar words to an input word (Text → Text)
- Generating tags for images, and searching images using text (Image ↔ Text)

To do this, we will use embeddings, vector representations of images and text. Once we have embeddings, searching simply becomes a matter of finding vectors close to our input vector.
The way we find these is by calculating the cosine similarity between our image embedding, and embeddings for other images. Similar images will have similar embeddings, meaning a high cosine similarity between embeddings.

**Cosine similarity**
* https://en.wikipedia.org/wiki/Cosine_similarity
* Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them.
* The cosine of 0° is 1, and it is less than 1 for any angle in the interval (0,π] radians. It is thus a judgment of orientation and not magnitude: two vectors with the same orientation have a cosine similarity of 1, two vectors oriented at 90° relative to each other have a similarity of 0, and two vectors diametrically opposed have a similarity of -1, independent of their magnitude. The cosine similarity is particularly used in positive space, where the outcome is neatly bounded in {\displaystyle [0,1]} [0,1].
* These bounds apply for any number of dimensions, and the cosine similarity is most commonly used in high-dimensional positive spaces.
* For example, in information retrieval and text mining, each term is notionally assigned a different dimension and a document is characterised by a vector where the value in each dimension corresponds to the number of times the term appears in the document. Cosine similarity then gives a useful measure of how similar two documents are likely to be in terms of their subject matter.[
* The technique is also used to measure cohesion within clusters in the field of data mining

* dataset contains a category and a set of captions for every image
  - http://vision.cs.uiuc.edu/pascal-sentences/
* word embeddings that have been pre-trained on Wikipedia
  - https://nlp.stanford.edu/projects/glove/

1. **Image -> Image**
**What do we mean by generating embeddings?**
We will use our pre-trained model up to the penultimate (next to last) layer, and store the value of the activations. Generally, this would be layer output which is before the final classification layer.

- Use DNN to generate image features, and store them to disk; re-use them without needing to do inference again. Embeddings allow for huge efficiency gains
  * Each image is now represented by a sparse vector of fixed size ( 4096 )
  * The reason the vector is sparse is that we have taken the values after the activation function, which zeros out negatives.
- On top of storing them to disk, build a index/fast index of the embeddings
  * Build a fast index of the embeddings using [Annoy](https://github.com/spotify/annoy), which will allow us to very quickly find the nearest embeddings to any given embedding.
- Using embeddings to search through images
  * simply take in an image, get its embedding
  * and look in the fast index to find similar embeddings, and thus similar images
  * This is especially useful since image labels are often noisy, and there is more to an image than its label.
  * Labeling images as unique categories is quite limiting, which is why we hope to use more nuanced representations
  * This approach perform wells to find similar images, in general, but sometimes we are only interested in part of the image.

**Semi-supervised search**
* Sometimes we are only interested in part of the image. For example, given an image of a cat and a bottle, we might be only interested in similar cats, not similar bottles.
* A common approach to solve this issue is to:
  - Use an object detection model first, detect our cat and do image search on a cropped version of the original image
  - This adds a huge computing overhead, which we would like to avoid if possible
* There is a simpler “hacky” approach:
  - By re-weighing the activations i.e. use weighted embeddings 
  - We do this by loading the last layer of weights we had initially discarded
  - and only use the weights tied to the index of the class we are looking for to re-weigh our embedding

**Limitations:**

This is a great step forward, but since we are using a model pre-trained on Imagenet, we are thus limited to the 1000 Imagenet classes. These classes are far from all-encompassing (they lack a category for people, for example), so we would ideally like to find something more flexible. In addition, what if we simply wanted to search for cats without providing an input image?


In order to do this, we are going to use more than simple tricks, and leverage a model that can understand the semantic power of words.

2. **Text -> Text**
* Embeddings for text -  we can use a similar approach to index and search for words.
* We loaded a set of pre-trained vectors from GloVe, which were obtained by crawling through all of Wikipedia and learning the semantic relationships between words in that dataset.
* Just like before, we will create an index, this time containing all of the GloVe vectors (this model is far from perfect, but it will get us started)
* Then, we can search our embeddings for similar words. which returns this list of [word, distance]

let’s try to incorporate both words and images in our model.
* Using the distance between embeddings as a method for search is a pretty general method, but our representations for words and images seem incompatible.
* The embeddings for images are of size 4096, while those for words are of size 300 — how could we use one to search for the other?
* In addition, even if both embeddings were the same size, they were trained in a completely different fashion, so it is incredibly unlikely that images and related words would happen to have the same embeddings randomly. **We need to train a joint model.**

3. **Image <-> Text**

Create a hybrid model that can go from words to images and vice versa
* https://papers.nips.cc/paper/5204-devise-a-deep-visual-semantic-embedding-model
* http://course.fast.ai/lessons/lesson11.html

- The idea is to combine both representations by re-training our image model and changing the type of its labels.
- Usually, image classifiers are trained to pick a category out of many (1000 for Imagenet). What this translates to is that — using the example of Imagenet — the last layer is a vector of size 1000 representing the probability of each class. This means our model has no semantic understanding of which classes are similar to others: classifying an image of a cat as a dog results in as much of an error as classifying it as an airplane.
- For our hybrid model, we replace this last layer of our model with the **word vector of our category**
- This allows our model to learn to map the semantics of images to the semantics of words, and means that similar classes will be closer to each other (as the word vector for cat is closer to dog than airplane)
-  Instead of a target of size 1000, with all zeros except for a one, we will predict a semantically rich word vector of size 300.


**Setup**
```bash
git clone https://github.com/hundredblocks/semantic-search.git $AI_HOME/external
cd $AI_HOME/external/semantic-search
sudo pip install -r requirements.txt
sudo pip install -r requirements_all.txt
```
* Requirement already satisfied: urllib3<1.25,>=1.20; python_version == "2.7" in /usr/local/lib/python2.7/dist-packages (from botocore->streamlit) (1.23)
tensorrt 4.0.0.3 requires pycuda>=2016.1.2, which is not installed.
tensorrt 4.0.0.3 has requirement argparse>=1.4.0, but you'll have argparse 1.2.1 which is incompatible.

```bash
python downloader.py
wget -c http://nlp.stanford.edu/data/glove.6B.zip -P $AI_DATA/data/
cd $AI_DATA/data
unzip glove.6B.zip
ln -s $AI_DATA/data/glove.6B $AI_HOME/external/semantic-search/models/
```
* https://stackoverflow.com/questions/37439993/python-pip-argparse-upgrade
```bash
sudo pip install argparse --upgrade
import argparse
argparse.__version__
#
python train.py --model_save_path my_model.hdf5 --checkpoint_path checkpoint.hdf5 --glove_path models/glove.6B --dataset_path dataset --num_epochs 50
```

## Extras
**openalpr**
an open source Automatic License Plate Recognition library 
* https://github.com/openalpr/openalpr/wiki/OpenALPR-Design

**streamlit-demo**
https://github.com/treuille/insight-streamlit-demo
https://github.com/fivethirtyeight/uber-tlc-foil-response/tree/master/uber-trip-data
http://streamlit.io/docs/tutorial/
http://streamlit.io/docs/
```bash
vi $HOME/.streamlit/config.yaml
```
```bash
client:
  remotelyTrackUsage: false
proxy:
  useNode: false
  waitForConnectionSecs: 30
```
* create file: `st_hello.py`
```bash
import streamlit as st
st.write('Hello, world')
```
* run the app
```bash
python st_hello.py
#
## it starts at
# http://localhost:8501/?name=st_hello
```

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


## Recommendation Systems, Semantic Search Engines
* http://mahout.apache.org/docs/latest/algorithms/recommenders/
* https://towardsdatascience.com/semantic-code-search-3cd6d244a39c
* https://en.wikipedia.org/wiki/Semantic_search



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

## Problem statements
1. image analysis: image classification, object detection and object segmentation
2. automatically analyse the semantic contents of images and videos as it is just the content that determines the relevance in most of the potential uses
3.  image similarity assessment

- The problem is formulated as a supervised learning problem in which a training set of labelled images is provided.

One important aspect of image content is the object composition: the identities and positions of the objects the images contain.

* Our approach for the classification task is based on fused classifications by numerous global image features, including histograms of local features.
* The object detection combines similar classification of automatically extracted image segments and the previously obtained scene type lassifications
* The object segmentations are obtained in a straightforward fashion from the detection results.


**Datasets Availability**
https://en.wikipedia.org/wiki/List_of_datasets_for_machine_learning_research

- Facial recognition
- Action recognition
- Object detection and recognition
- Handwriting and character recognition
- Aerial images
- Text data
- News articles
- Messages
- Twitter and tweets
- Sound data
- Music
- Signal data
- Motion-tracking
- Animal
- Plant

## Image Annotation Tools
* https://en.wikipedia.org/wiki/List_of_manual_image_annotation_tools
* https://github.com/wkentaro/labelme
* https://github.com/CSAILVision/LabelMeAnnotationTool
* https://en.wikipedia.org/wiki/LabelMe

## Drone Data Solutions
http://huviair.com/
https://geospoc.com/
https://www.dronedeploy.com/
https://flylitchi.com/
https://pix4d.com/


1. Master the complete workflow using DroneDeploy, Litchi and Pix4D. Start your own UAV mapping business right away!
2. Learn to work with Pix4D & DroneDeploy outputs on QGIS, AutoCAD & Google Earth. Start your own UAV mapping business now!
3. Master the use of Ground Control Points (GCPs) to make your UAV mapping projects absolutely survey grade!!

**opencv compilation failed for the following modules**
- sfm
- dnn
- js(depends on dnn)