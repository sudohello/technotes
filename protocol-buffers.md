https://developers.google.com/protocol-buffers/docs/overview

https://stackoverflow.com/questions/29529959/caffe-understanding-expected-lmdb-datastructure-for-blobs

http://caffe.berkeleyvision.org/tutorial/net_layer_blob.html

http://caffe.berkeleyvision.org/tutorial/layers.html
https://github.com/BVLC/caffe/blob/master/src/caffe/proto/caffe.proto

https://stackoverflow.com/questions/29529959/caffe-understanding-expected-lmdb-datastructure-for-blobs


https://ceciliavision.wordpress.com/2016/02/29/caffe-what-files-do-you-need-to-train-your-own-network/
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


#---------------

Training py-faster-rcnn
https://huangying-zhan.github.io/2016/09/22/detection-faster-rcnn


https://huangying-zhan.github.io/2016/09/22/detection-faster-rcnnhttps://www.dropbox.com/s/iywkgsrx2fx6t5q/basketball.tar.gz?dl=0

https://www.dropbox.com/s/iywkgsrx2fx6t5q/basketball.tar.gz?dl=0


http://caffe.berkeleyvision.org/gathered/examples/finetune_flickr_style.html


https://github.com/rbgirshick/py-faster-rcnn/issues/198
I1006 14:25:06.882606 19555 net.cpp:816] Ignoring source layer prob
Traceback (most recent call last):
  File "./tools/train_net.py", line 113, in <module>
    max_iters=args.max_iters)
  File "/home/bhaskar/Documents/ai-ml-dl/external/py-faster-rcnn/tools/../lib/fast_rcnn/train.py", line 157, in train_net
    pretrained_model=pretrained_model)
  File "/home/bhaskar/Documents/ai-ml-dl/external/py-faster-rcnn/tools/../lib/fast_rcnn/train.py", line 51, in __init__
    pb2.text_format.Merge(f.read(), self.solver_param)
AttributeError: 'module' object has no attribute 'text_format'


vi lib/fast_rcnn/train.py
import google.protobuf.text_format


./tools/train_net.py --weights data/imagenet_models/ZF.v2.caffemodel --imdb basketball_train --cfg experiments/cfgs/config.yml --solver models/basketball/solver.prototxt --iter 0

lt /home/bhaskar/Documents/ai-ml-dl/external/py-faster-rcnn/output/marker/train/basketball_iter_0.caffemodel

 ./tools/train_net.py --weights output/marker/train/basketball_iter_0.caffemodel --imdb basketball_train --cfg experiments/cfgs/config.yml --solver models/basketball/solver.prototxt --iter 10000


 smooth_L1_loss_layer.cpp:54] Not Implemented Yet

 https://github.com/rbgirshick/py-faster-rcnn/issues/130
 https://blog.csdn.net/qq_14975217/article/details/51495844



./tools/train_net.py --weights output/marker/train/basketball_iter_0.caffemodel --imdb basketball_train --cfg experiments/cfgs/config.yml --solver models/basketball/solver.prototxt  --iter 10000


 ./tools/test_net.py --gpu 0 --def models/basketball/test.prototxt --net output/marker/train/basketball_iter_0.caffemodel --imdb basketball_val --cfg experiments/cfgs/config.yml


 $ ./tools/train_net.py --gpu 0 --weights data/imagenet_models/VGG16.v2.caffemodel --imdb basketball_train --cfg experiments/cfgs/config.yml --solver models/basketball/solver.prototxt --iter 0
