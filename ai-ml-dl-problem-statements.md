/*
Title: Udacity - AI/ML/DL Problem statements
Decription: 3D City
Author: Bhaskar Mangal
Date: 
Tags: Udacity - AI/ML/DL Problem statements
*/

## Problem Statements

Over the past several years, machine learning and deep learning has shown remarkable success on some of the world’s most difficult computer science challenges, from image classification and captioning to translation to model visualization techniques

### [Content-based image retrieval (CBIR) systems - Image search Engine](https://www.pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/)

Image search engines that quantify the contents of an image are called Content-Based Image Retrieval (CBIR) systems.

A great example of a Search by Example system is [TinEye](https://www.tineye.com/). TinEye is actually a reverse image search engine where you provide a query image, and then TinEye returns near-identical matches of the same image, along with the webpage that the original image appeared on.

The goals are:
* Define 3 different categories to describe images or based on which search results would be retrieved
* Given a query image from 3 different categories is to return the category’s corresponding images in the top 10 results.

The algorithm analyzes the image itself and quantifies the image by extracting features called image descriptors.

An **image descriptor** defines how we are quantifying an image, hence extracting features from an image is called describing an image. The output of an image descriptor is a feature vector, an abstraction of the image itself. Simply put, it is a list of numbers used to represent an image. Feature vectors can then be compared for similarity by using a distance metric or similarity function. Distance metrics and similarity functions take two feature vectors as inputs and then output a number that represents how “similar” the two feature vectors are. Given two feature vectors, a distance function is used to determine how similar the two feature vectors are. The output of the distance function is a single floating point value used to represent the similarity between the two images.

**4 Steps of Any CBIR System:**
1. ++Defining your image descriptor++
What aspect of the image you want to describe. Are you interested in the color of the image? The shape of an object in the image? Or do you want to characterize texture?
2. ++Indexing your dataset++
apply this image descriptor to each image in your dataset, extract features from these images, and write the features to storage (ex. CSV file, RDBMS etc.) so that they can be later compared for similarity.
3. ++Defining your similarity metric++
Popular choices include the Euclidean distance, Cosine distance, and chi-squared distance, but the actual choice is highly dependent on (1) your dataset and (2) the types of features you extracted.
4. ++Searching++
A user will submit a query image to your system (from an upload form or via a mobile app, for instance) and your job will be to (1) extract features from this query image and then (2) apply your similarity function to compare the query features to the features already indexed. From there, you simply return the most relevant results according to your similarity function.

Machine Learning or Deep Learning approaches can be used to create CBIR.

**Commercial Prospects**
This can be extended to provide commerical image based search services using REST APIs for geospatial datasets. The APIs can retrive images based on multiple different categories like cars, bikes, road signs, pedistrian and traffic signal based image retrival.

### [Automatic License Plate Recognition system (ALPR) and Pedestrian Alert Systems]()
> Face & Vehicle number plate Detections from Urban Scene Images

MapmyIndia collects terrestrial image data using Land Mobile Mapping Systems to provide services like 360 deg Virtual tour (eg: Google's StreetView). Privacy is of paramount concern when this data is published over internet, therefore it's necessary to mask/blur the identity information like human faces and vehicle number plates from the collected images before they can be published over internet. To alleviate these concerns, your task as an employee of MapmyIndia is to use supervised learning techniques to construct a demonstration of a face identification and vehicle number plate identification in offline mode. Also, report the accuracy of identifications of face and vehicle number plate.

**Commercial Prospects**
The proposed solution can be extended to provided dedicated commericial solutions for Automatic License Plate Recognition system (ALPR), ADAS systems for pedestrian detection and alert systems.

### [Automated Traffic Sign detection and Georeferencing Service]()
 Map companies provide annotated map based services and as a part of the map building process annotations are carried out using multiple data sources like satellite images, terrestrial images using Land Mobile Mapping Systems. One of the data layer that is shown on the map is traffic signs approximately at the same location. Traffic-sign from the terrestrial image is identified and marked on the GIS tool with lat/lon, sign interpretation and image. To accelerate the human effort, your task as an employee of MapmyIndia is to use supervised learning techniques to construct a demonstration of traffic-sign detection and identification. Also, report the accuracy of identifications.

**Commercial Prospects**
The proposed solution can be extended to provided dedicated commericial solutions as a REST API for automatically detect traffic signs from the uploaded images and georeference them based on image's lat/lon coordinates.

### [Optical Character Recognition - OCR](http://searchcontentmanagement.techtarget.com/definition/OCR-optical-character-recognition)
OCR (optical character recognition) is the recognition of printed or written text characters by a computer. This involves photoscanning of the text character-by-character, analysis of the scanned-in image, and then translation of the character image into character codes, such as ASCII, commonly used in data processing.

OCR enables you to convert different types of documents, such as scanned paper documents, PDF files or images captured by a digital camera into editable and searchable data.

[Dropbox case study](https://blogs.dropbox.com/tech/2017/04/creating-a-modern-ocr-pipeline-using-computer-vision-and-deep-learning)
[OCR examples](https://www.pyimagesearch.com/category/optical-character-recognition-ocr/)

#### a. Text Boards/Bill Board detections
Detection of Text Boards/Bill Board detections from the terristrial scanned image dataset.

#### b. Text Extraction from Bill boards
Identification of the texts from the Bill boards from the terristrial scanned image dataset and convert them into editable, searchable text and also georeference them.


### [Speech  Recognition]()
Computer analysis of the human voice, especially for the purposes of interpreting words and phrases or identifying an individual voice.

In speech recognition as in many other complex services, neural networks are rapidly replacing previous technologies

### [Voice transcription](https://research.googleblog.com/2015/08/the-neural-networks-behind-google-voice.html)
Voice transcription using Long Short-term Memory Recurrent Neural Networks (LSTM RNNs)—yet another place neural networks are improving useful services. In Voice transcription, there’s more to speech recognition than recognizing individual sounds in the audio: sequences of sounds need to match existing words, and sequences of words should make sense in the language. This is called “language modeling.” Language models are typically trained over very large corpora of text, often orders of magnitude larger than the acoustic data.

### [Urban Scene Segmentation and Classification]()
Urban scene are the images captured from in the hustle-bustle of the city. This is actively looked into with Deep Learning approaches using Convolution Neural Networks (CNN):
- Road sign detections
- vehicle identification
- pedestrian detection
- urban traffic scene segmentation
- face recognition
- hand signals and gesture recognition
- Road segmentation
