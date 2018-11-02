autopep8 0.9.1 requires pep8>=1.4.5, which is not installed.
tensorrt 4.0.0.3 requires pycuda>=2016.1.2, which is not installed.
tensorrt 4.0.0.3 has requirement argparse>=1.4.0, but you'll have argparse 1.2.1 which is incompatible.
uff 0.3.0 has requirement argparse>=1.4.0, but you'll have argparse 1.2.1 which is incompatible.

    x86_64-linux-gnu-gcc -pthread -fwrapv -Wall -O3 -DNDEBUG -fno-strict-aliasing -Wdate-time -D_FORTIFY_SOURCE=2 -g -fstack-protector-strong -Wformat -Werror=format-security -fPIC -DBOOST_PYTHON_SOURCE=1 -DHAVE_CURAND=1 -DPYGPU_PACKAGE=pycuda -DBOOST_THREAD_DONT_USE_CHRONO=1 -DPYGPU_PYCUDA=1 -DBOOST_MULTI_INDEX_DISABLE_SERIALIZATION=1 -DBOOST_THREAD_BUILD_DLL=1 -Dboost=pycudaboost -DBOOST_ALL_NO_LIB=1 -Isrc/cpp -Ibpl-subset/bpl_subset -I/usr/local/lib/python2.7/dist-packages/numpy/core/include -I/usr/include/python2.7 -c src/cpp/cuda.cpp -o build/temp.linux-x86_64-2.7/src/cpp/cuda.o
    In file included from src/cpp/cuda.cpp:1:0:
    src/cpp/cuda.hpp:14:18: fatal error: cuda.h: No such file or directory
    compilation terminated.
    error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
    
    ----------------------------------------
Command "/usr/bin/python -u -c "import setuptools, tokenize;__file__='/tmp/pip-install-v9wdlz/pycuda/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /tmp/pip-record-ehy320/install-record.txt --single-version-externally-managed --compile" failed with error code 1 in /tmp/pip-install-v9wdlz/pycuda/
You are using pip version 10.0.1, however version 18.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.


----------------

VLC skins

https://www.deviantart.com/kryptonsyt/art/VLC-Slim-Beam-Black-Skin-437200484
https://www.deviantart.com/diagoo1/art/VLC-Slim-Beam-Black-Skin-Edited-By-Diagoo1-713250049

~/.local/share/vlc/skins2

---

https://askubuntu.com/questions/65023/are-there-any-ubuntu-based-equivalents-of-corel-draw-pagemaker-photoshop-and-q

* How to open pagemaker file in Ubuntu or Android?


----

CNN Increamental Learning

http://www.robots.ox.ac.uk/~vgg/practicals/cnn/
https://www.microsoft.com/en-us/research/wp-content/uploads/2014/11/Error-Driven-Incremental-Learning-in-Deep-Convolutional-Neural-Network-for-Large-Scale-Image-Classification.pdf
https://www.researchgate.net/post/What_are_the_techniques_for_incremental_training_of_Convolutional_Neural_Networks_without_doing_full_training_as_new_classes_are_added_to_data

https://www.quora.com/Can-we-train-deep-neural-networks-in-an-online-incremental-manner-specifically-for-non-stationary-time-series

http://www.anthology.aclweb.org/D/D15/D15-1053.pdf
https://arxiv.org/abs/1511.06964


https://en.wikipedia.org/wiki/Adaptive_resonance_theory

Adaptive resonance theory (ART) is a theory developed by Stephen Grossberg and Gail Carpenter on aspects of how the brain processes information. It describes a number of neural network models which use supervised and unsupervised learning methods, and address problems such as pattern recognition and prediction.

the problem of acquiring new knowledge without disrupting existing knowledge that is also called incremental learning.

Increamental Learning Papers
https://arxiv.org/pdf/1712.02719.pdf
Incremental Learning in Deep Convolutional Neural Networks Using Partial Network Sharing
17 Sep 2018


https://www.techleer.com/articles/506-yolov3-an-incremental-improvement/
