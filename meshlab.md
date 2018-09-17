---
Title: MeshLab
Decription: MeshLab
Author: Bhaskar Mangal
Date: 
Tags: MeshLab
---

**Table of Contents**
* TOC
{:toc}


## Install QT
* https://info.qt.io/download-qt-for-application-development

## Install CloudCompare
* https://github.com/CloudCompare/CloudCompare/blob/master/BUILD.md

1. QT
2. libLAS
	- libLAS is a library and set of command-line tools for working with the lidar LAS format. It is also used by GRASS 7 to import LAS files.
	- It is recommended to first install custom builds of proj, tiff, geotiff, and gdal.
		- **PROJ** is a cartographic projection library which most other GIS software depends on. It contains the share/proj/epsg file of the geospatial reference EPSG code numbers and allows for transformation of coordinates in different projection systems.
		- geotiff
			- https://www.liblas.org/compilation.html#using-unix-makefiles-on-linux
		- GDAL
			- GDAL/OGR is a powerful library and set of utilities for dealing with raster and vector data. It is used by many other geospatial projects (GRASS GIS, QGIS, etc).
			- http://scigeo.org/articles/howto-install-latest-geospatial-software-on-linux.html#gdal
			- http://www.gdal.org/
		- lasZip
			- http://www.laszip.org/
		- tiff
		- geotiff
			GeoTIFF is a library for geospatial TIFF images. It is used by most raster-enabled GIS software. GeoTIFF builds on proj and libtiff, so these should be installed first.
		- geoos
			- GEOS is a spatial geometry library frequently used in GIS software and spatial databases.
			- http://trac.osgeo.org/geos/
		- libkml
			- libkml is a KML library. It is used by GDAL and other GIS software to read/write KML files
			- https://code.google.com/archive/p/libkml
			- http://scigeo.org/articles/howto-install-latest-geospatial-software-on-linux.html#libkml
			- https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/libkml/libkml-1.2.0.tar.gz

3. zlib
* http://www.zlib.net/
* https://downloads.sourceforge.net/project/libpng/zlib/1.2.11/zlib-1.2.11.tar.gz?r=http%3A%2F%2Fwww.zlib.net%2F&ts=1497520924&use_mirror=excellmedia

```bash
sudo apt-get -y install libgeotiff-dev
sudo apt-get install libkml-dev
sudo apt-get install gdal-bin python-gdal
#
sudo add-apt-repository ppa:ubuntugis/ppa

# proj installation, after installation test:
proj
Rel. 4.9.3, 15 August 2016
usage: proj [ -bCeEfiIlormsStTvVwW [args] ] [ +opts[=arg] ] [ files

# tiff.install.sh, test
tiffinfo

# GeoTIFF

```
# GIS Utilities
* http://scigeo.org/articles/howto-install-latest-geospatial-software-on-linux.html


# Install MeshLab
* http://meshlabstuff.blogspot.in/2009/09/meshing-point-clouds.html

```bash
sudo -E apt-add-repository ppa:zarquon42/meshlab
sudo -E apt -y update
sudo -E apt -y install meshlab
```

#

http://spatialreference.org/

https://blender.stackexchange.com/questions/13637/draping-2d-image-over-point-cloud-or-mesh

http://labins.org/
http://callumprentice.github.io/apps/street_cloud/index.html
