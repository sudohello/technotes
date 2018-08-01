# Machine Leanring (ML) & CNN Experiments
[<< Back](ml-app-in-adv-map-creation.md)

## ML
> python + openCV3 python bindings


**Edge Detections**
>**Source Image**
![ALT img](images/ai-ml-dl/ml-results/lane.png)
>**Edges**
![ALT img](images/ai-ml-dl/ml-results/edges-auto.jpg)
>**Lane**
![ALT img](images/ai-ml-dl/ml-results/edges-lane.jpg)

>**GAZE Image (0.8 MP PointGrey Mono Camera)**
![ALT img](images/ai-ml-dl/ml-results/gaze-sample/040417_145638_16363225_color_l_43.jpg)
>**Edges**
![ALT img](images/ai-ml-dl/ml-results/gaze-sample/edges-auto.jpg)
>**Lane**
![ALT img](images/ai-ml-dl/ml-results/gaze-sample/edges-lane.jpg)

**Shape Detections**
>**GAZE Image (0.8 MP PointGrey Mono Camera)**
![ALT img](images/ai-ml-dl/ml-results/gaze-sample/040417_145638_16363225_color_l_43.jpg)
>**Shape (Contours)**
![ALT img](images/ai-ml-dl/ml-results/gaze-sample/ml-shape.jpg)
>**Shape (Contours with labels)**
![ALT img](images/ai-ml-dl/ml-results/gaze-sample/ml-shape-labels.jpg)


**Blurr Detection**
>**GAZE Image (0.8 MP PointGrey Mono Camera)**
![ALT img](images/ai-ml-dl/ml-results/gaze-sample/blur-images.jpg)

## CNN
* SegNet
	* Python
	* Caffe framework
	* Trained on CamVid dataset of 367 Images
	* 6 Days, 26K iterations
	* Unable to train on GPU due to memory issues
	* [SegNet Tutorial Reference](http://mi.eng.cam.ac.uk/projects/segnet/tutorial.html)
**SegNet CamVid Training Results**
>**Source Image**
![ALT img](images/ai-ml-dl/segnet-results/f1-pic.png)
>**Ground Truth**
![ALT img](images/ai-ml-dl/segnet-results/f1-truth.png)
>**Prediction**
![ALT img](images/ai-ml-dl/segnet-results/f1-predict.png)

>**GAZE Image (0.8 MP PointGrey Mono Camera)**
![ALT img](images/ai-ml-dl/segnet-results/gz-f1-pic.png)
![ALT img](images/ai-ml-dl/segnet-results/gz-f1-predict.png)
**Web Demo Output**
![ALT img](images/ai-ml-dl/segnet-results/gz-webdemo-predict.png)