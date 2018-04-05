/*
title: ROS
decription: ROS
Author: Bhaskar Mangal
Date: 
tags: ROS
*/

# ROS

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
