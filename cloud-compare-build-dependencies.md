---
Title: CloudCompare
Decription: CloudCompare
Author: Bhaskar Mangal
Date: 
Tags: CloudCompare
---

**Table of Contents**
* TOC
{:toc}


## CloudCompare

### References
* [Cross Section Tool](http://www.cloudcompare.org/doc/qCC/CloudCompare_cross_section_tool_V2.pdf)
* [User Manual - v2.6.1 ](http://www.cloudcompare.org/doc/qCC/CloudCompare%20v2.6.1%20-%20User%20manual.pdf)


## cloud-compare-build-dependencies

sudo apt-get install git build-essential cmake qt5-default qtscript5-dev libssl-dev qttools5-dev qttools5-dev-tools qtmultimedia5-dev libqt5svg5-dev libqt5webkit5-dev libsdl2-dev libasound2 libxmu-dev libxi-dev freeglut3-dev libasound2-dev libjack-jackd2-dev libxrandr-dev libqt5xmlpatterns5-dev libqt5xmlpatterns5 libqt5xmlpatterns5-private-dev

https://github.com/CloudCompare/CloudCompare

git clone https://github.com/CloudCompare/CloudCompare.git
cd CloudCompare
mkdir build
cd build 
cmake ..
cmake-gui ..
then select PCL
configure
generate
close 
make
sudo make install


INSTALL_QFACETS_PLUGIN
 CMake Error at plugins/qFacets/CMakeLists.txt:8 (message):
   ShapeLib is required to compile this plugin (enable OPTION_USE_SHAPE_LIB)


INSTALL_QGMMREG_PLUGIN

 CMake Warning at plugins/qGMMREG/CMakeLists.txt:12 (find_package):
   By not providing "FindVXL.cmake" in CMAKE_MODULE_PATH this project has
   asked CMake to find a package configuration file provided by "VXL", but
   CMake did not find one.

   Could not find a package configuration file provided by "VXL" with any of
   the following names:

     VXLConfig.cmake
     vxl-config.cmake

   Add the installation prefix of "VXL" to CMAKE_PREFIX_PATH or set "VXL_DIR"
   to a directory containing one of the above files.  If "VXL" provides a
   separate development package or SDK, be sure it has been installed.



 CMake Error at plugins/qGMMREG/CMakeLists.txt:24 (message):
   VXL is required to compile qGMMReg (VXL_DIR)



 CMake Warning at plugins/qGMMREG/GMMREG/C++/CMakeLists.txt:15 (FIND_PACKAGE):
   By not providing "FindVXL.cmake" in CMAKE_MODULE_PATH this project has
   asked CMake to find a package configuration file provided by "VXL", but
   CMake did not find one.

   Could not find a package configuration file provided by "VXL" with any of
   the following names:

     VXLConfig.cmake
     vxl-config.cmake

   Add the installation prefix of "VXL" to CMAKE_PREFIX_PATH or set "VXL_DIR"
   to a directory containing one of the above files.  If "VXL" provides a
   separate development package or SDK, be sure it has been installed.


INSTALL_QHOUGH_NORMALS_PLUGIN
 CMake Error at plugins/qHoughNormals/CMakeLists.txt:10 (message):
   No Eigen root directory specified (EIGEN_ROOT_DIR)




 CMake Warning at plugins/qSRA/CMakeLists.txt:9 (message):
   qSRA plugin works best with dxflib support! (enable OPTION_USE_DXF_LIB)

