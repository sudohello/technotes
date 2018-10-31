---
Title: Deep Learning Commercial Solutions
Decription: Deep Learning Commercial Solutions
Author: Bhaskar Mangal
Date: 29th-Oct-2018
Last updated: 30th-Oct-2018
Tags: Deep Learning Commercial Solutions
---

## Deep Learning Commercial Solutions
* https://goberoi.com/comparing-the-top-five-computer-vision-apis-98e3e3d7c647
* https://www.datasciencecentral.com/profiles/blogs/comparison-of-the-top-cloud-apis-for-computer-vision

## Sample App for Testing Commercial APIs
**cloudy_vision**
* https://github.com/goberoi/cloudy_vision
  - As of 30th-Oct-2018
    - old and not updated, 2yrs
    - 59 forks
* https://github.com/Projet-TAMIS/cloudy_vision
* https://github.com/StyriaAI/cloudy_vision
* https://github.com/dee-me-tree-or-love/cloudy_vision - google OCR


## 1. [Google](https://cloud.google.com/vision/)
> **Free trial requires to furnish Credit Card details**

**Cloud Vision Products**
* **Vision API**
The Vision API allows you to easily integrate vision detection features in your applications, including image labeling, face and landmark detection, optical character recognition (OCR), object localization, and tagging of explicit content.
* **AutoML Vision**
AutoML Vision enables you to train your own, custom machine learning models to classify your images according to labels that you define.
* **Vision Product Search**
Vision Product Search allows retailers to create a set of products and of reference images that visually describe the product from a set of viewpoints.

### **Vision API**
* The Google Vision API was released on December 2nd 2015
In more detail, the API lets you annotate images with the six following features.

* LABEL_DETECTION: executes Image Content Analysis on the entire image and provides relevant labels (i.e. keywords & categories).
  - The API returns something very similar to the JSON structure above for each uploaded image. Each label is basically a string (the description field) and comes with a relevance score (0 to 1) and a Knowledge Graph reference.
  - You can specify how many labels the API should return at request time and the labels will be sorted by relevance
* TEXT_DETECTION: performs Optical Character Recognition (OCR) and provides the extracted text, if any.
  - Google Vision API, everything is encapsulated in a REStful API that simply returns a string and its bounding box.
  -  able to recognize multiple languages, and will return the detected locale together with the extracted text.
* FACE_DETECTION: detects faces, provides facial key points, main orientation, emotional likelihood, and the like.
  - Face detection aims at localizing human faces inside an image. It’s a well-known problem that can be categorized as a special case of a general object-class detection problem
  - It is NOT the same as Face Recognition
  - FACE_DETECTION feature, you will obtain the following:
    * The face position (i.e. bounding boxes);
    * The landmarks positions (i.e. eyes, eyebrows, pupils, nose, mouth, lips ears, chin, etc.), which include more than 30 points;
    * The main face orientation (i.e. roll, pan, and tilt angles);
    * Emotional likelihoods (i.e. joy, sorrow, anger, surprise, etc), plus some additional information (under exposition likelihood, blur likelihood, headwear likelihood, etc.).
* LANDMARK_DETECTION: detects geographic landmarks.
* LOGO_DETECTION: detects company logos.
* SAFE_SEARCH_DETECTION: determines image safe search properties on the image (i.e. the likelihood that an image might contain violence or nudity).

**Notes:**
- The API only accepts a series of base64-encoded images as input
- Labels are selected among thousands of object categories and mapped to the official Google Knowledge Graph. This allows image classification and enhanced semantic analysis, understanding, and reasoning.

**References**
* https://developers.google.com/knowledge-graph/
* https://www.google.com/intl/bn/search/about/
* https://json-ld.org/
* https://github.com/w3c/json-ld-wg
* https://schema.org/
* https://code.tutsplus.com/tutorials/how-to-use-the-google-cloud-vision-api-in-android-apps--cms-29009
* https://cloud.google.com/vision/docs/quickstart-client-libraries#before-you-begin
* https://cloudacademy.com/blog/google-vision-api-image-analysis/
```bash
export GOOGLE_APPLICATION_CREDENTIALS="$AI_HOME/auth/My Project-fae27866938b.json"
#
sudo pip install --upgrade google-cloud-vision
##composer require google/cloud-vision
##npm install --save @google-cloud/vision
```
* Enable Billing
https://console.developers.google.com/billing/
* Sample Code
```python
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'fruitbowl.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)
```


## 2. [Amazon](https://aws.amazon.com/rekognition/)


## 3. [Microsoft](https://azure.microsoft.com/en-us/free/ai/)
  * https://azure.microsoft.com/en-us/services/cognitive-services/


## 4. [Cloudsight](https://cloudsight.ai)


## 5. [IBM Watson](https://console.bluemix.net/docs/services/watson/index.html#about)
> **No Credit Card required for free trial:**

**curl - ex1**
```bash
curl -X POST -u "apikey:<your-key>" \
--form "images_file=@fruitbowl.jpg" \
"https://gateway.watsonplatform.net/visual-recognition/api/v3/classify?version=2018-03-19"
```

**Python SDK**
* https://github.com/watson-developer-cloud/
```bash
sudo pip install --upgrade watson-developer-cloud
```


## 6. [Clarifai](https://www.clarifai.com/)

**curl - ex1**
* https://samples.clarifai.com/metro-north.jpg
```bash
curl -X POST \
-H "Authorization: <your-key>" \
-H "Content-Type: application/json" \
-d '
{
  "inputs": [
    {
      "data": {
        "image": {
          "url": "fruitbowl.jpg"
        }
      }
    }
  ]
}'\
https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs
```

**python sdk**
```bash
sudo pip install --upgrade clarifai
```