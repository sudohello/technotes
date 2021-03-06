---
title: Caffe
---

**Table of Contents**
* TOC
{:toc}


## Caffe AI Framework
1. train.prototxt
This is the network architecture you define for your training.  You define all the layers you need, including data layer, convolutional layer, pooling, ReLU, etc. More examples of the prototxt file could be found in the caffe model zoo. (where trained network architecture is hosted)

describes the network structure, including number of layer, type of layer, number of neurons in each layer, etc

The tricker component of train.prototxt is the data layer. 

2. solver.prototxt
This contains all the hyper-parameters you have for your training.

3. deploy.prototxt
The deploy prototxt is basically a duplicate of the train prototxt. This makes sense since you want your test data to be forwarded to the same network architecture. The only difference is that you have to replace the data layer in train.prototxt with a specification of the input data dimension.

4. data
Caffe supports different data types to be used for training. The simplest but slowest is to use a txt file with actual image path and label written in each line. But this has a latency for data fetching from the memory, and could significantly slow down your training process.

using lmdb files as data source. Caffe will allocate memory onto GPU and fetch data from there, thus a big speedup for training. But it’s less straightforward creating lmdb format data file

you have your data ready, you specify its path in your train.prototxt inside the data layer.

5. [optinal] solver2.prototxt
If you want to decay your learning rate after a certain amount of training iteration, you would specify another solver prototxt here with reduced learning rate. This file is optional and is only needed when you want to restart your training with a different set of hyper-parameters.

**References**
* https://stackoverflow.com/questions/29529959/caffe-understanding-expected-lmdb-datastructure-for-blobs
* http://caffe.berkeleyvision.org/tutorial/net_layer_blob.html
* http://caffe.berkeleyvision.org/tutorial/layers.html
* https://github.com/BVLC/caffe/blob/master/src/caffe/proto/caffe.proto
* https://stackoverflow.com/questions/29529959/caffe-understanding-expected-lmdb-datastructure-for-blobs
* https://ceciliavision.wordpress.com/2016/02/29/caffe-what-files-do-you-need-to-train-your-own-network/


## Compiling and Installation
* py-faster-rcnn with CUDA 9.0 and cuDNN 7.1

**Errors**
* https://groups.google.com/forum/#!topic/caffe-users/3NHh06RhWd4
```bash
CXX/LD -o python/caffe/_caffe.so python/caffe/_caffe.cpp
python/caffe/_caffe.cpp:11:31: fatal error: numpy/arrayobject.h: No such file or directory
compilation terminated.
Makefile:507: recipe for target 'python/caffe/_caffe.so' failed
make: *** [python/caffe/_caffe.so] Error 1
```bash
* Fix for the above error:
In the Makefile.config:
```
# NOTE: this is required only if you will compile the python interface.
# We need to be able to find Python.h and numpy/arrayobject.h.
PYTHON_INCLUDE := /usr/include/python2.7 \
		/usr/lib/python2.7/dist-packages/numpy/core/include \
		/usr/local/lib/python2.7/dist-packages/numpy/core/include
# Anaconda Python distribution is quite popular. Include path:
```
* `make clean && make all && make pycaffe`
* hdf5 error fixes: find out where hdf5 libs are located and add them to the pats in make file
```bash
INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial /usr/include
LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib /usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu/hdf5/serial
```
* Training errors:
```bash
change self.param_str_ to self.param_str in $FRCN_ROOT/lib/roi_data_layer/layer.py"
```
, line 87, in setup

/lib/rpn/anchor_target_layer.py", line 27

/lib/rpn/proposal_target_layer.py", line 25


  File "/home/game/Documents/ai-ml-dl/external/py-faster-rcnn/tools/../lib/rpn/proposal_target_layer.py", line 166, in _sample_rois
    fg_inds = npr.choice(fg_inds, size=fg_rois_per_this_image, replace=False)
  File "mtrand.pyx", line 1192, in mtrand.RandomState.choice
TypeError: 'numpy.float64' object cannot be interpreted as an index

fg_inds = npr.choice(fg_inds, size=int(fg_rois_per_this_image), replace=False)


    rois_per_image, self._num_classes)
  File "/home/game/Documents/ai-ml-dl/external/py-faster-rcnn/tools/../lib/rpn/proposal_target_layer.py", line 181, in _sample_rois
    bg_inds = npr.choice(bg_inds, size=bg_rois_per_this_image, replace=False)
  File "mtrand.pyx", line 1192, in mtrand.RandomState.choice
TypeError: 'numpy.float64' object cannot be interpreted as an index


    rois_per_image, self._num_classes)
  File "/home/game/Documents/ai-ml-dl/external/py-faster-rcnn/tools/../lib/rpn/proposal_target_layer.py", line 188, in _sample_rois
    labels[fg_rois_per_this_image:] = 0
TypeError: slice indices must be integers or None or have an __index__ method


**Change it to the following**
    fg_rois_per_this_image = int(min(fg_rois_per_image, fg_inds.size))    

    bg_rois_per_this_image = int(min(bg_rois_per_this_image, bg_inds.size))



* https://github.com/rbgirshick/py-faster-rcnn/issues/198
```bash
I1006 14:25:06.882606 19555 net.cpp:816] Ignoring source layer prob
Traceback (most recent call last):
  File "./tools/train_net.py", line 113, in <module>
    max_iters=args.max_iters)
  File "/home/bhaskar/Documents/ai-ml-dl/external/py-faster-rcnn/tools/../lib/fast_rcnn/train.py", line 157, in train_net
    pretrained_model=pretrained_model)
  File "/home/bhaskar/Documents/ai-ml-dl/external/py-faster-rcnn/tools/../lib/fast_rcnn/train.py", line 51, in __init__
    pb2.text_format.Merge(f.read(), self.solver_param)
AttributeError: 'module' object has no attribute 'text_format'
```
* Fix for `AttributeError: 'module' object has no attribute 'text_format'`
```bash
vi lib/fast_rcnn/train.py
import google.protobuf.text_format
```
* training
```bash
./tools/train_net.py --weights data/imagenet_models/ZF.v2.caffemodel --imdb basketball_train --cfg experiments/cfgs/config.yml --solver models/basketball/solver.prototxt --iter 0
#
lt /home/bhaskar/Documents/ai-ml-dl/external/py-faster-rcnn/output/marker/train/basketball_iter_0.caffemodel
#
 ./tools/train_net.py --weights output/marker/train/basketball_iter_0.caffemodel --imdb basketball_train --cfg experiments/cfgs/config.yml --solver models/basketball/solver.prototxt --iter 10000
#
## error:
 smooth_L1_loss_layer.cpp:54] Not Implemented Yet
```
* https://github.com/rbgirshick/py-faster-rcnn/issues/130
* https://blog.csdn.net/qq_14975217/article/details/51495844
```bash
./tools/train_net.py --weights output/marker/train/basketball_iter_0.caffemodel --imdb basketball_train --cfg experiments/cfgs/config.yml --solver models/basketball/solver.prototxt  --iter 10000
 ./tools/test_net.py --gpu 0 --def models/basketball/test.prototxt --net output/marker/train/basketball_iter_0.caffemodel --imdb basketball_val --cfg experiments/cfgs/config.yml
 ./tools/train_net.py --gpu 0 --weights data/imagenet_models/VGG16.v2.caffemodel --imdb basketball_train --cfg experiments/cfgs/config.yml --solver models/basketball/solver.prototxt --iter 0
```

In file: lib./rpn/proposal_target_layer.py: get_bbox_regression_labels:
* https://github.com/rbgirshick/py-faster-rcnn/issues/9
```bash
cls = clss[ind]
#
## Change it to:
cls = int(clss[ind])
```
* Imagenet basketball
```baah
./tools/train_net.py --gpu 0 --weights data/faster_rcnn_models/ZF_faster_rcnn_final.caffemodel --imdb basketball_train --cfg experiments/cfgs/config.yml --solver models/basketball/solver.prototxt --iter 0
#
./tools/train_net.py --gpu 0 --weights output/marker/train/zf_faster_rcnn_basketball_iter_0.caffemodel --imdb basketball_train --cfg experiments/cfgs/config.yml --solver models/basketball/solver.prototxt --iter 10000
#
./tools/test_net.py --gpu 0 --def models/basketball/test.prototxt --net output/marker/train/zf_faster_rcnn_basketball_iter_10000.caffemodel --imdb basketball_val --cfg experiments/cfgs/config.yml
```
* INRIAPerson
```bash
./tools/train_faster_rcnn_alt_opt.py --gpu 0 --net_name INRIA_person --weights $HOME/Documents/ai-ml-dl-data/data/imagenet/VGG_CNN_M_1024.v2.caffemodel --imdb inria_train --cfg data/INRIA_Person_devkit/config.yml
```
* <custom>
```bash
solverprototxt="$HOME/Documents/ai-ml-dl-data/data/<custom>/traffic_sign_detection/2/faster_rcnn_end2end/prototxt/solver.prototxt"
caffemodel="$HOME/Documents/ai-ml-dl-data/data/imagenet/VGG16_faster_rcnn_final.caffemodel"
cfg="$HOME/Documents/ai-ml-dl-data/data/<custom>/traffic_sign_detection/2/faster_rcnn_end2end/faster_rcnn_end2end.<custom>.yml"
./tools/train_net.py --gpu 0 --weights $caffemodel --imdb <custom>_train --cfg $cfg --solver $solverprototxt --iter 10
```

## Object Detections
* https://cv-tricks.com/object-detection/faster-r-cnn-yolo-ssd/
* https://medium.com/@jonathan_hui/object-detection-speed-and-accuracy-comparison-faster-r-cnn-r-fcn-ssd-and-yolo-5425656ae359
* https://storage.googleapis.com/openimages/web/challenge_visualizer/index.html?set=relationships&c=wears

**Series**
* https://tryolabs.com/blog/2017/08/30/object-detection-an-overview-in-the-age-of-deep-learning/
* https://tryolabs.com/blog/2018/01/18/faster-r-cnn-down-the-rabbit-hole-of-modern-object-detection/
- https://medium.com/@ageitgey/machine-learning-is-fun-80ea3ec3c471

## Training py-faster-rcnn
**Train Faster-RCNN**
* https://github.com/xinleipan/py-faster-rcnn-with-new-dataset
* https://github.com/deboc/py-faster-rcnn/blob/master/help/Readme.md
* https://huangying-zhan.github.io/2016/09/22/detection-faster-rcnn - **nice tutorial**
* https://github.com/deboc/py-faster-rcnn/tree/master/help - **INRIAPerson**
```bash
cd $FRCN_ROOT/data/INRIA_Person_devkit/data
ln -s $HOME/Documents/ai-ml-dl-data/data/INRIAPerson/Train/annotations/ Annotations
ln -s $HOME/Documents/ai-ml-dl-data/data/INRIAPerson/Train/pos/ Images
mkdir ImageSets
ls Annotations/ -m | sed s/\\s/\\n/g | sed s/.txt//g | sed s/,//g > ImageSets/train.txt
```
* https://www.dropbox.com/s/iywkgsrx2fx6t5q/basketball.tar.gz?dl=0
* http://caffe.berkeleyvision.org/gathered/examples/finetune_flickr_style.html


**Researchers**
https://www.cc.gatech.edu/~parikh/

**Web Challanges**
* https://storage.googleapis.com/openimages/web/challenge.html

**New Tools, Frameworks. libraries**
* https://github.com/tryolabs/luminoth

