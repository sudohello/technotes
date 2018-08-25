/*
Title: Point Cloud
Decription: Point Cloud Data
Author: Bhaskar Mangal
Date: 12th Jul 2018
Last Updated: 12th Jul 2018
Tags: Point Cloud Data, PCD
*/

** Table of Contents**

[TOC]

# PCD - Point Cloud Data

## Showcase / Examples on Internet
* [second national Lidar survey of the Netherlands, AHN2, with 640 billion points](http://ahn2.pointclouds.nl)

## PCD Browser Based Rendering

**PCD rendering engines:-**
* cesium
* potree
	* [Potree_Rendering_Large_Point_Clouds_in_Web_Browsers](https://www.researchgate.net/publication/309358171_Potree_Rendering_Large_Point_Clouds_in_Web_Browsers)
* plas.io
* [itowns](http://www.itowns-project.org/)
* [Entwine](http://potree.entwine.io/)
* [Greyhound](https://github.com/hobu/greyhound)

Currently, Cesium is the core engine powering the PCD rendering in the browser and there are newer frameworks and technologies evolving on the top of it.

Here, in cesium, we also have the specifications defined for the Tiling the Point Cloud Data.
* https://github.com/AnalyticalGraphicsInc/3d-tiles/tree/master/TileFormats/PointCloud
* At this point of time it's worth mentioning following apart from above tools, entwine & greyhound (open source) build on top of cesium, potree.
	* PPT on entwine: https://cesiumjs.org/presentations/EntwineOGC.pptx

keywords in context of PCD processing/rendering:-
* Coordinate quantization (single/double  precision floating point error)
* modifiable nested octree (MNO) structure
* EDL - Eye-Dome-Lighting
* LOD - Level of Details

## Point Could Data Management - Indexing, Tiling, Streaming
* **[Entwine](https://entwine.io)**
	- https://github.com/connormanning/entwine
	- Entwine is a data organization library for massive point clouds, designed to conquer datasets of hundreds of billions of points as well as desktop-scale point clouds. Entwine can index anything that is PDAL-readable, and can read/write to a variety of sources like S3 or Dropbox. Builds are completely lossless, so no points will be discarded even for terabyte-scale datasets.
* **[py3dtiles](https://github.com/Oslandia/py3dtiles)**
	- https://github.com/Oslandia/py3dtiles
	- Python module to manage 3DTiles format.
	- For now, only the Point Cloud and the Batched 3D Model specifications are supported.
	- py3dtiles is currently used by LOPoCS, a server streaming Point Cloud from Postgis, to send data to Cesium
* **[LOPoCS](https://github.com/Oslandia/lopocs)**
	- https://github.com/Oslandia/lopocs
	- LOPoCS is a point cloud server written in Python, allowing to load Point Cloud from a PostgreSQL database thanks to the pgpointcloud extension.
	- The current version of LOPoCS provides a way to load Point Cloud from PostgreSQL to the following viewers:
		* Cesium thanks to the 3DTiles format
		* Potree viewer : viewer with LAZ compressed data.
* **PgPointCloud**
	- https://github.com/pgpointcloud/pointcloud
	- A PostgreSQL extension for storing point cloud (LIDAR) data

**References**
* [Point clouds in PostgreSQL: store and publish](https://oslandia.com/wp-content/uploads/2018/05/Lemoine-Oslandia-Pointcloud.pdf)
* https://entwine.io
* https://oslandia.com/en/2016/03/16/osgeo-cs-2016-report-point-clouds/
* https://oslandia.com/en/2016/11/08/py3dtiles/
**Videos**
* https://vimeo.com/245073446
* https://vimeo.com/189285883


## Point Cloud Tools
* http://speck.ly/
* https://hobu.co/
* http://potree.entwine.io/
	Seems to use these three components -
	* https://entwine.io/ - data organization library for massive point clouds
	* https://github.com/connormanning/entwine
	* https://github.com/hobu/greyhound - point cloud streaming framework
	* https://github.com/potree/potree - webgl viewer for large point clouds
* PDAL
	- https://www.pdal.io/workshop/pdal-introduction.html
	- PDAL is Point Data Abstraction Library, and it is an open source software for translating and processing point cloud data. It is not limited to just LiDAR data, although the focus and impetus for many of the tools have their origins in LiDAR.
* https://github.com/LI3DS/
* http://www.or3d.co.uk/products/software/veesus/arena4d-data-studio/


## Research Papers and respective tools
* [Taming the beast: Free and open-source massive point cloud web visualization](https://pdfs.semanticscholar.org/84bf/29d37c50115451975a25256150394b7e7da3.pdf)
	- [AHN2 3D viewer and download tool (Accessed 2015-10-23)](http://ahn2.pointclouds.nl/)
	- [Massive PotreeConverter. (Accessed 2015-10-23)](https://github.com/NLeSC/Massive-PotreeConverter)
	- [AHN pointcloud viewer (Accessed 2015-10-23)](https://github.com/NLeSC/ahn-pointcloud-viewer)
	- [AHN pointcloud viewer web service. (Accessed 2015-10-23)](https://github.com/NLeSC/ahn-pointcloud-viewer-ws)

## StreetView tech
- https://medium.com/@nocomputer/creating-point-clouds-with-google-street-view-185faad9d4ee


## Point Cloud Classification Benchmarks
- [semantic3d: Large-Scale Point Cloud Classification Benchmark!](http://semantic3d.net/)


## Misc Tools
- https://openframeworks.cc/about/
- https://openframeworks.cc/download/

## Vector Tiling
- https://geovation.github.io/build-your-own-static-vector-tile-pipeline

- https://www.graphhopper.com/blog/

