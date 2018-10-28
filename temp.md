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
