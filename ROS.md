---
title: ROS
decription: ROS
Author: Bhaskar Mangal
Date: 
tags: ROS
---

**Table of Contents**
* TOC
{:toc}


## ROS

## ROS - Installation
**References**
* http://wiki.ros.org/indigo/Installation/Ubuntu
* http://answers.ros.org/question/188732/e-unable-to-locate-package-ros-indigo-desktop-full/
* http://wiki.ros.org/kinetic/Installation/Ubuntu

* **Setup your sources.list**
```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```
* **Set up your keys**
```bash
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
```
* **Installation**
  - Desktop-Full Install: (Recommended) : ROS, rqt, rviz, robot-generic libraries, 2D/3D simulators, navigation and 2D/3D perception
```bash
sudo apt-get update
sudo apt-get install ros-kinetic-desktop-full
```
* **Initialize rosdep**
  - Before you can use ROS, you will need to initialize rosdep. rosdep enables you to easily install system dependencies for source you want to compile and is required to run some core components in ROS.
```bash
sudo rosdep init
rosdep update
```
* **Environment setup**
```bash
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

* **Getting rosinstall**
  - rosinstall is a frequently used command-line tool in ROS that is distributed separately. It enables you to easily download many source trees for ROS packages with one command.
```bash
sudo apt-get install python-rosinstall
```

### ROS Commands
* List packages
  > rospack list-names

* Install packages
  > sudo apt-get install ros-"your ros distro"-"package-name"
  > sudo apt-get install ros-kinetic-image-view
  > sudo apt-get install ros-kinetic-stereo-image-proc

* Install package dependencies - rosdep is a tool you can use to install system dependencies required by ROS packages.
  > rosdep install [package]

**Using ROS**

* roscore is the first thing you should run when using ROS.
  > roscore

* rosnode displays information about the ROS nodes that are currently running. The rosnode list command lists these active nodes:
  > rosnode list

* The rosnode info command returns information about a specific node:-
  > rosnode info /rosout

* List service.
  > rosservice list
* Show service description.
  > rosservice type spawn | rossrv show
* Create a new turtle by creating a service.
  > rosservice call spawn 2 2 0.2 ""
* ROS parameter list.
  > rosparam list
* Set and get background colors using rosparam
  > rosparam set background_r 150
  > rosparam get background_g
* Display parameters
  > rosparam get /
* Save parameters
  > rosparam dump params.yaml
* Load parameters into new namespace copy
  > rosparam load params.yaml copy
  > rosparam get copy/background_b

#### PCL in ROS
**References**
* http://www.pointclouds.org/documentation/tutorials/

#### Rviz in Stereo

**References**
* http://wiki.ros.org/stereo_image_proc
* http://wiki.ros.org/image_view#stereo_view
* http://docs.ros.org/api/sensor_msgs/html/index-msg.html
* [Install packages in ROS](http://answers.ros.org/question/196766/how-to-install-packages-under-ros/)
* [ROS Package lists](http://www.ros.org/browse/list.php?package_type=package&distro=groovy)
* http://wiki.ros.org/FAQ
* http://wiki.ros.org/ROS/Tutorials/rosdep

* Install rviz
  > rosdep install rviz


##### Required Image processing Packages

* stereo_image_proc
  > Stereo and single image rectification and disparity processing. This package contains the stereo_image_proc node, which sits between the stereo camera drivers and vision processing nodes.
* stereo_msgs
  > stereo_msgs contains messages specific to stereo processing, such as disparity images.
* stereo_synchronizer
  > stereo_synchronizer
* stereo_wall_detection
  > Detects planar structures (e.g., walls) from stereo cameras point clouds (usually generated usi
* camera1394
  > IEEE 1394 Digital Camera driver
* camera1394stereo
  > This is a modified version of the ROS driver for devices supporting the IEEE 1394 Digital Camer
* camera_application
  > Camera Application
* camera_calibration
  > camera_calibration allows easy calibration of monocular or stereo cameras using a checkerboard
* camera_calibration_parsers
  > camera_calibration_parsers contains routines for reading and writing camera calibration parameters.
* camera_calibration_standalone
  > Simple tools for stereo camera calibration (to be deprecated by dcam/ost from ros-pkg).
* camera_info_manager
  > This package provides a C++ interface for camera calibration information. It provides CameraIn.
* camera_info_manager_py
  > Python interface for camera calibration information. This ROS package provides a CameraInfo int...
* camera_pose_calibration
  > camera_pose_calibration
* camera_pose_toolkits
  > camera_pose_toolkits
* camera_self_filter
* image_view
  > A simple viewer for ROS image topics. Includes a specialized viewer for stereo + disparity images....
* image_view2
  > A simple viewer for ROS image topics with draw-on features

### Octave
Installation (opensource alternative to MatLab)

**References**
* http://wiki.octave.org/Octave_for_Debian_systems

```
sudo apt-get install octave
```
## OpenCV
Compilation and Installation (opensource Computer Vision Lib)

### References
* http://answers.opencv.org/question/60804/how-to-build-docs-for-opencv-300-rc1/
* http://askubuntu.com/questions/771601/problem-with-cmake
* http://www.linuxfromscratch.org/blfs/view/cvs/general/opencv.html
* http://stackoverflow.com/questions/17386551/how-to-build-opencv-with-java-under-linux-using-command-linegonna-use-it-in-ma

### Required packages
```bash
sudo apt-get install --assume-yes build-essential cmake git
sudo apt-get install --assume-yes build-essential pkg-config unzip ffmpeg qtbase5-dev python-dev python3-dev python-numpy python3-numpy
sudo apt-get install --assume-yes libopencv-dev libgtk-3-dev libdc1394-22 libdc1394-22-dev libjpeg-dev libpng12-dev libtiff5-dev libjasper-dev
sudo apt-get install --assume-yes libavcodec-dev libavformat-dev libswscale-dev libxine2-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev
sudo apt-get install --assume-yes libv4l-dev libtbb-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev
sudo apt-get install --assume-yes libvorbis-dev libxvidcore-dev v4l-utils

sudo apt-get install --assume-yes ffmpeg python3-dev python3-numpy
sudo apt-get install --assume-yes libopencv-dev libgtk-3-dev libdc1394-22-dev
sudo apt-get install --assume-yes libxine2-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev
sudo apt-get install --assume-yes libv4l-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev
sudo apt-get install --assume-yes libvorbis-dev libxvidcore-dev v4l-utils
```


## Updating libpng
Updating to libpng 1.6.28
* http://www.linuxfromscratch.org/blfs/view/7.6/general/libpng.html
* http://stackoverflow.com/questions/33634402/how-to-check-libpng-version
```bash
readelf -d  libpng.so |grep SONAME
identify -list format | grep PNG
```

## Configure Java using Alternatives
* http://askubuntu.com/questions/315646/update-java-alternatives-vs-update-alternatives-config-java
```bash
update-java-alternatives -l
update-alternatives --config java
```
**Install JNI**
```bash
ls $JAVA_HOME/include/jni.h
```
- FindJNI. Since the "FindJNI" module of cmake 3 doesn't support the detection of Oracle Java 8, we have to add our Java 8 directories manually. Therefore, locate the file FindJNI.cmake in your cmake directory,e.g /home/foo/bar/cmake-3.2.2-Linux-x86_64/share/cmake-3.2/Modules/FindJNI.cmake
- Goto the JAVA_APPEND_LIBRARY_DIRECTORIES variable and add the path to your java lib architecture directory, e.g. /home/foo/bar/jdk1.8.0_45/lib/amd64
- Goto the JAVA_AWT_INCLUDE_DIRECTORIES variable and add the path to your java include directory, e.g. /home/foo/bar/jdk1.8.0_45/include

### Compile and Build OpenCV
```bash
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D WITH_V4L=ON -D WITH_QT=ON -D WITH_OPENGL=ON -D WITH_CUBLAS=ON -DCUDA_NVCC_FLAGS="-D_FORCE_INLINES"
```

Note: check how many cpu core you have or use default for using single core
```
make -j $(($(nproc) + 1))
make -j 2 // number of cores of CPU, do not run on all the cores, it will hang and will not compile
make -j //takes default cores as 1, use this
```
#### Stack Trace after running make, find out what is not avaiable and try to install based on requirements

```
curretly have gstreamer 0.10.36
gstreamer-base-1.0 gstreamer-video-1.0 gstreamer-app-1.0 gstreamer-riff-1.0 gstreamer-pbutils-1.0

libavresample
libgphoto2
ippicv_linux_20151201.tgz
OpwnBLAS lib
Atlas
Doxygen

JNI
Matlab

/usr/lib/x86_64-linux-gnu/libvtkRenderingPythonTkWidgets.so
/usr/lib/vtk

Unavailable ( if graphics card with cuda enabled, following needs to be installed)
cudaarithm cudabgsegm cudacodec cudafeatures2d cudafilters cudaimgproc cudalegacy cudaobjdetect cudaoptflow cudastereo cudawarping cudev java

Media I/O
GDAL No
GDCM No
Video I/O
FFMPEG
avresample No
Microsoft Kinect libs - OpenNI "OpenNI PrimeSensor Modules" OpenNI2
PvAPI
GigEVisionSDK
Aravis SDK
UniCap
UniCal ucil
V4L/V4L2
XIMEA
Xine
gphoto2
```

**Install missing components**
```
sudo apt-get install --assume-yes doxygen
sudo apt-get install --assume-yes graphviz
sudo apt-get install --assume-yes doxygen-gui
```
You can run doxygen-gui using:
```
doxywizard
```



## Tutorials
* http://library.isr.ist.utl.pt/docs/roswiki/Documentation.html

**Setting up Environment**
* http://library.isr.ist.utl.pt/docs/roswiki/ROS(2f)Tutorials(2f)InstallingandConfiguringROSEnvironment.html

```bash
mkdir ~/ros_workspace
```


## Catkin
catkin is the official build system of ROS and the successor to the original ROS build system, rosbuild. catkin combines CMake macros and Python scripts to provide some functionality on top of CMake's normal workflow

In ROS terminology, source code is organized into 'packages' where each package typically consists of one or more targets when built.

Build systems that are used widely in software development are
- GNU Make
- GNU Autotools
- CMake
- Apache Ant (used mainly for Java)

## References
* http://wiki.ros.org/catkin/conceptual_overview
* http://wiki.ros.org/catkin/Tutorials
* http://wiki.ros.org/catkin/workspaces
* http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment
* http://wiki.ros.org/ROS/Tutorials#Beginner_Level

# GIS Open Source Data
* http://gisgeography.com/free-global-dem-data-sources/
* http://gisgeography.com/top-6-free-lidar-data-sources/

Elevation data is abundant. It’s just a matter of finding the right one to suit your needs.From spaceborne to airborne, from Earth to Mars – you now have the right tools to position yourself vertically on any location of the planets.

## Opensource Global DEM Data
* Space Shuttle Radar Topography Mission (SRTM)
* ASTER Global Digital Elevation Model
  - ASTER GDEM is a 30 m resolution for 80% of globe not just for USA. This is for version 1 and 2
* JAXA’s Global ALOS 3D World
  -  it is the most precise global-scale elevation data at this time
* Light Detection and Ranging (LiDAR) 
  -  nothing beats LiDAR really in terms of coverage and accuracy. Filtering ground returns, you can build an impressive DEM from LiDAR.


### LiDAR DEM
* Open Topography
  - Open Topography is a collaborative data repository for LiDAR users.
  - Intuitive web map displays LiDAR points as downloadable data with metadata

* USGS Earth Explorer


## Commercial DEM Data
* WorldDEM
- http://www.geo-airbusds.com/en/4529-worlddem-reaching-new-heights

## Keywords
* PRISM - Panchromatic Remote-sensing Instrument for Stereo Mapping
* ALOS - Advanced Land Observing Satellite

## OSM 3D Tagging
* http://wiki.openstreetmap.org/wiki/3D_development
* http://wiki.openstreetmap.org/wiki/3D_tagging
* https://gis.stackexchange.com/questions/207960/how-to-download-osm-3d-building-data
