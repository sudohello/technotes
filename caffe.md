CXX/LD -o python/caffe/_caffe.so python/caffe/_caffe.cpp
python/caffe/_caffe.cpp:11:31: fatal error: numpy/arrayobject.h: No such file or directory
compilation terminated.
Makefile:507: recipe for target 'python/caffe/_caffe.so' failed
make: *** [python/caffe/_caffe.so] Error 1


https://groups.google.com/forum/#!topic/caffe-users/3NHh06RhWd4

make clean && make all && make pycaffe

In the Makefile.config:

# NOTE: this is required only if you will compile the python interface.
# We need to be able to find Python.h and numpy/arrayobject.h.
PYTHON_INCLUDE := /usr/include/python2.7 \
		/usr/lib/python2.7/dist-packages/numpy/core/include \
		/usr/local/lib/python2.7/dist-packages/numpy/core/include
# Anaconda Python distribution is quite popular. Include path:


INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial /usr/include
LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib /usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu/hdf5/serial


change self.param_str_ to self.param_str in $FRCN_ROOT/lib/roi_data_layer/layer.py"

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
