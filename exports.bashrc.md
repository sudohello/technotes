---
Title: Ubuntu Exports Bash
Decription: Ubuntu Exports Bash
Author: Bhaskar Mangal
Date: 23rd Jan 2018
Tags: Ubuntu Exports Bash
---

**Table of Contents**
* TOC
{:toc}


## Custom New System Configuration: ~/.bashrc
```bash
alias lt='ls -lrt'
alias scripts='cd $HOME/softwares/linuxscripts'
alias technotes='cd $HOME/Documents/content/technotes'
# Virtual Environment Wrapper
#source /usr/local/bin/virtualenvwrapper.sh
#--
export PATH="$PATH:$HOME/softwares/linuxscripts"
#--
export CMAKE_ROOT="/usr/local"
export CMAKE_MODULE_PATH="/usr/local/share/cmake-3.11"
#--
export CUDA_HOME="/usr/local/cuda"
export PATH="/usr/local/cuda/bin:$PATH"
#--
export PATH="$HOME/softwares/proj-4.9.3/build/bin:$PATH"
export PATH="$HOME/softwares/tiff-4.0.8/build/bin:$PATH"
export PATH="$HOME/softwares/libgeotiff-1.4.2/build/bin:$PATH"
export PATH="$HOME/softwares/geos-3.6.1/build/bin:$PATH"
export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"
export PATH="$JAVA_HOME/bin:$PATH"
#--
export PATH="$PATH:$HOME/softwares/emsdk:$HOME/softwares/emsdk/clang/e1.37.36_64bit:$HOME/softwares/emsdk/node/8.9.1_64bit/bin:$HOME/softwares/emsdk/emscripten/1.37.36"
export EMSDK="$HOME/softwares/emsdk"
export EM_CONFIG="$HOME/.emscripten"
export BINARYEN_ROOT="$HOME/softwares/emsdk/clang/e1.37.36_64bit/binaryen"
export EMSCRIPTEN="$HOME/softwares/emsdk/emscripten/1.37.36"
#--
export FBX_SDK="$HOME/softwares/fbxsdk"
export FBX_SDK_LIBRARY_FILE="$HOME/softwares/fbxsdk/lib"
export FBX_SDK_INCLUDE_DIR="$HOME/softwares/fbxsdk/include"
#--
export ANDROID_SDK_ROOT="$HOME/android/sdk"
export ANDROID_NDK_ROOT="$HOME/android/ndk/android-ndk-r16b"
#--QT
#PATH="$HOME/softwares/qt5/qtbase/bin:$PATH"
PATH="/usr/local/bin:$PATH"
#--
export PYTHONPATH="/usr/local/lib/python2.7/dist-packages:$PYTHONPATH"
#export PYTHONPATH="$PYTHONPATH:/usr/local/lib/python3.5/dist-packages"
#--
export LINUX_SCRIPTS_PATH="$HOME/softwares/linuxscripts/cmd"
export PATH="$LINUX_SCRIPTS_PATH:$PATH"
#--
export LD_LIBRARY_PATH="/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH"
export LD_LIBRARY_PATH="/usr/lib/jvm/java-1.8.0-openjdk-amd64/jre/lib/amd64/server:$LD_LIBRARY_PATH"
export LD_LIBRARY_PATH="/usr/lib/x86_64-linux-gnu/hdf5/serial:$LD_LIBRARY_PATH"
export LD_LIBRARY_PATH="/usr/lib/x86_64-linux-gnu/gtk-2.0/modules:$LD_LIBRARY_PATH"
#export LD_LIBRARY_PATH="/usr/lib/x86_64-linux-gnu/gtk-3.0/modules:$LD_LIBRARY_PATH"
export LD_LIBRARY_PATH="/usr/lib:/usr/local/lib:$LD_LIBRARY_PATH"
#export LD_LIBRARY_PATH="$HOME/softwares/qt5/qtbase/lib:$LD_LIBRARY_PATH"
#--Boost
#export BOOST_ROOT="$HOME/softwares/boost_1_67_0"
export BOOST_LIBRARYDIR="/usr/local/lib"
export BOOST_INCLUDEDIR="/usr/local/include"
#--
export PATH="$HOME/softwares/faber/build/scripts-2.7:$PATH"
```