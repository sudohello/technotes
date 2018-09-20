CXX/LD -o python/caffe/_caffe.so python/caffe/_caffe.cpp
python/caffe/_caffe.cpp:11:31: fatal error: numpy/arrayobject.h: No such file or directory
compilation terminated.
Makefile:507: recipe for target 'python/caffe/_caffe.so' failed
make: *** [python/caffe/_caffe.so] Error 1


https://groups.google.com/forum/#!topic/caffe-users/3NHh06RhWd4

In the Makefile.config:

# NOTE: this is required only if you will compile the python interface.
# We need to be able to find Python.h and numpy/arrayobject.h.
PYTHON_INCLUDE := /usr/include/python2.7 \
		/usr/lib/python2.7/dist-packages/numpy/core/include \
		/usr/local/lib/python2.7/dist-packages/numpy/core/include
# Anaconda Python distribution is quite popular. Include path:
