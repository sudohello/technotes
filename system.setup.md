/*
Title: Ubuntu System Setup
Decription: Ubuntu System Setup
Author: Bhaskar Mangal
Date: 02 May 2018
Updated: 02 May 2018
Tags: Ubuntu System Setup
*/

# System Setup
Assembling decent system for Multi purpose:
* Computer Vision and Image Processing
* Machine Learning
* Deep Learning
* 3D GIS - Photogrammetry, Point Cloud, LiDAR, 3D Modelling
* Data Analysis, Data Visualization
* VR,AR
* VFX

## Hardware/PC configuration
* [System Configuration Research - What & Why](hardwares-configs.md)

## OS Installation and setting up directories
**Install git, gparted, vim-gtk and sublime editor**
```bash
sudo -E apt-get update
## Essential for New Machine Setup
sudo -E apt-get -q -y install git
sudo -E apt-get -q -y install gparted
sudo -E apt-get -q -y install vim-gtk
#
# install sublime (optional)
#./sublimetexteditor.install.sh
```

* **partition using gparted**

* **creating data directories, mount points**
```bash
#
# get UUID of datadrive disk/partition
#
sudo blkid
ls -l /dev/disk/by-uuid/
#
# make an entry in the file and mount the partition
#
UUID=98083c67-4779-4603-85ac-fd5bb2f6ef37       /media/thanos/datadrive                  ext4    rw,auto,nofail,nodev,nosuid     0       2
#
# mount the disk/partition
#
sudo mount -a
cd /media/thanos/datadrive/thanos
#
# Move the data folders to the data partitions
#
rsync -aXS $HOME/Documents .
rsync -aXS $HOME/Downloads .
rsync -aXS $HOME/Music .
rsync -aXS $HOME/Pictures .
rsync -aXS $HOME/Videos .
rsync -aXS $HOME/softwares .
cd
sudo umount -a
#
# Create the mount points under /mnt
# creating the mounts under /media would come as a data drive in the file manager, hence avoid it
#
sudo vi /etc/fstab
```
* Sample working fstab entry
```
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/sda1 during installation
UUID=e2d95887-9a55-4f96-8064-0d7dc5aaa3c9 /               ext4    errors=remount-ro 0       1
# swap was on /dev/sda5 during installation
UUID=33852ea4-4036-4c2f-b1cb-6ccaac3500f9 none            swap    sw              0       0
#
UUID=98083c67-4779-4603-85ac-fd5bb2f6ef37       /mnt/datadrive                  ext4    rw,auto,nofail,nodev,nosuid     0       2
/mnt/datadrive/thanos/Documents                 /home/thanos/Documents          none    bind                            0       0
/mnt/datadrive/thanos/Downloads                 /home/thanos/Downloads          none    bind                            0       0
/mnt/datadrive/thanos/Pictures                  /home/thanos/Pictures           none    bind                            0       0
/mnt/datadrive/thanos/Music                     /home/thanos/Music              none    bind                            0       0
/mnt/datadrive/thanos/Videos                    /home/thanos/Videos             none    bind                            0       0
/mnt/datadrive/thanos/softwares                 /home/thanos/softwares          none    bind                            0       0
```

## Software Stack setup begins

1. Get the technotes and linuxscripts repo from github (optional)
```bash
git clone https://github.com/mangalbhaskar/linuxscripts.git $HOME/softwares/linuxscripts
mkdir -p $HOME/Documents/content
git clone https://github.com/mangalbhaskar/technotes.git $HOME/Documents/content/technotes
#
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

### Sequence of Software Installed
* [Nvidia Driver -> 390.1](nvidia.driver.install.sh)
```
Manual Driver Installation
```
* [vim-gtk](vim.install.sh)
* [SublimeText 3 editor](sublimetexteditor.install.sh)
* [vlc](vim.install.sh)
* [utils.install.sh](utils.install.sh)
* [php, composer and php extensions](php.install.sh)
* [apache2 -> this installed latest PHP version (currently, version=7.2)](apache2.install)
* [nodejs -> nodejs=9.11.1, npm=5.6.0](nodejs.install.sh)
* opencv pre-requisites for computer vision and deep learning
* [java -> JDK:1.8](java.install.sh)
```bash
source java.install.sh
```
* [python -> 2.7+](python.install.sh)
```bash
sudo pip install pip -U
sudo apt remove python-pip
sudo apt remove python-scipy
#
python --version
#Python 2.7.12
#
pip --version
#pip 10.0.1 from /usr/local/lib/python2.7/dist-packages/pip (python 2.7)
#
```

```bash
sudo pip install -r requirements.py.md -U
sudo pip list | grep -iE "numpy|scipy|matplotlib|scikit-learn|Flask|pandas|sympy|scikit-image|statsmodels|seaborn|vtk|Mayavi"
#
#Flask                         1.0.2                 
#matplotlib                    2.2.2                 
#mayavi                        4.5.0                 
#umpy                         1.14.3                
#pandas                        0.22.0                
#scikit-image                  0.13.1                
#scikit-learn                  0.19.1                
#scipy                         1.1.0                 
#seaborn                       0.8.1                 
#statsmodels                   0.8.0                 
#sympy                         1.1.1                 
#vtk                           8.1.0
```

* [postgres](postgres.install.sh)
* [Cuda -> 9.1](cuda.install.sh)
```bash
source cuda.install.sh
```
* [Inkscape - graphics](inkscape.graphics.install.sh)
* [gimp - graphics](gimp.graphics.install.sh)
* [Ceres Solver -> 1.14.0](ceres-solver.install.sh)
* [proj -> VER="4.9.3"](proj.install.sh)
* [tiff -> VER="4.0.8"](tiff.install.sh)
* [geotiff -> VER="1.4.2"](geotiff.install.sh)
* [lasZip -> git clone](laszip.install.sh)
* [geoos -> VER="3.6.1"](geos.install.sh)
* boost -> 1.64.0
* libkml -> compilation errors
* cmake, ccmake upgrade to 3.11.0
* install android SDK
* install android NDK
* install android studio (optional)
* gdal
* MySQL
* lzma, jsoncpp, libarchive, libhash
* VTK -> 8.1.0 (python wrapper and group images, group web)
* lasperf
* grassgis
* pgpointcloud
* geowave - not installed
* pdal with compressin and las-perf, python fails, without python installed
* entwine - manual fix openssl1.1 api changes
* greyhound -failed
openscenegraph
hexbin
pcl
#* pdal
zlib
QT 5.10+
CloudCompare
meshlab

##
* MPI is a parallel computing standard that allows programs to take advantage of multiple processors. There are two competing MPI implementations available on most Linux distributions: mpich and openmpi. 

```
sudo apt-get install libmpich-dev
```


# CUnit - Automation test suite for C
# https://mysnippets443.wordpress.com/2015/03/07/ubuntu-install-cunit/
#sudo apt-get install libcunit1 libcunit1-doc libcunit1-dev
```
sudo apt install libcunit1 libcunit1-dev
```

* The Computational Geometry Algorithms Library (CGAL) is a C++ library that aims to provide easy access to efficient and reliable algorithms in computational geometry.
```
sudo apt-get install libcgal-dev # install the CGAL library
sudo apt-get install libcgal-demo # install the CGAL demos
```
sudo apt-get install libxerces-c-dev
sudo apt install libjsoncpp-dev

sudo apt-get install libqt5x11extras5-dev
sudo apt-get install qttools5-dev

 sudo apt install libsuitesparseconfig4.4.6 libsuitesparse-dev
 sudo apt install metis libmetis-dev

* Boost Python
* OpenCV
* QT -> 5.10+ [skipped, be careful if unsuccessul can mess up your system]

**TIPs**
* Follow the above `Software Installation sequence` to avoid grief and have maximum features supports
* Always check the pre-requisites and proper recommedned versions are installed.
```bash
#
# for apt/apt-get installation
apt-cache policy <packageName>
#
# for python/pip
pip list
#
```

**References**
1. GIS Software Setup
* [howto-install-latest-geospatial-software-on-linux](http://scigeo.org/articles/howto-install-latest-geospatial-software-on-linux.html#environment_vars)

https://blackbricksoftware.com/bit-on-bytes/169-scikit-image-installation-for-ubuntu-16-04
https://www.udacity.com/wiki/creating-network-graphs-with-python#how-to-install-networkx
- numpy, pandas, matplotlib, scipy, sklearn, skimage

 sudo apt install python-networkx
 sudo pip install -U scikit-image
- before opencv



#Flask                         0.12.2     
#matplotlib                    2.2.2      
#numpy                         1.14.2     
#pandas                        0.22.0     
#scikit-learn                  0.19.1     
#scipy                         1.0.1
----

##

https://www.zdnet.com/article/what-are-the-best-raspberry-pi-alternatives-everything-you-need-to-know-about-pi-rivals

https://www.nds-association.org/