---
Title: HD Map
Decription: HD Map
Author: Bhaskar Mangal
Date: 18th-Apr-2018
Tags: HD Map
---

**Table of Contents**
* TOC
{:toc}


## HD Map

## High Definiton Mapping - Motivation
Autonomous vehicles will require many system redundancies to deal with unforeseen circumstances. A High Definition Map is required for precise localization of the vehicle, relative to road boundaries and intersections, under all conditions.

While other sensors such as radar and LiDAR may provide redundancy for object detection – the camera is the only real-time sensor for driving path geometry and other static scene semantics (such as traffic signs, on-road markings, etc.). Therefore, for path sensing and foresight purposes, only a highly accurate map can serve as the source of redundancy. In order for the map to be a reliable source of redundancy, it must be updated with an ultra-high refresh rate to secure its low Time to Reflect Reality (TTRR) qualities.

To address the challenge of creating High Definition Map, we are proposing to develope and setup the technology roadmap to create High Definiton Maps. This will build the solid foundation to explore the future possibilities to explore the option of building and proliferation of Advanced Driver Assistance Systems (ADAS) suited for Indian road and traffic conditions. This when coupled with harnessing the power of the crowd will provide High Definition Map to be built and maintain in near-real-time an accurate map of the environment. The solution possiblly be comprised of three layers: harvesting agents (any camera-equipped vehicle), map aggregating server (cloud), and map-consuming agents (autonomous vehicle).

## Blogs
- https://www.rmsi.com/solutions/navigation-mapping/indoor-mapping/
- https://www.geospatialworld.net/blogs/hd-maps-autonomous-vehicles/
- https://newsroom.intel.com/press-kits/autonomous-driving-intel/

### Mapillary
http://geoawesomeness.com/
https://blog.mapillary.com/update/2018/03/29/mapping-and-machines-level-up-with-ai.html
https://blog.mapillary.com/product/2017/10/18/mapillary-verifier-tool.html
https://blog.mapillary.com/update/2017/10/12/human-in-the-loop.html
https://blog.mapillary.com/update/2015/01/27/traffic-signs.html

## HD Vector Map
https://blog.mapbox.com/mobileye-roadbook-high-precision-hd-maps-distributed-at-scale-9b4e692d29f
https://blog.mapbox.com/millimeter-precision-hd-vector-maps-874327d8327c
https://github.com/mapbox/vtzero/
https://github.com/mapbox/awesome-vector-tiles
https://blog.mapbox.com/hd-vector-maps-open-standard-335a49a45210
https://github.com/mapbox/vector-tile-spec/issues/103

Mobileye’s RoadBook™


## Learning Resources on Latest Technology Items
https://twitter.com/hashtag/machinelearning?src=hash
https://twitter.com/hashtag/computervision?src=hash

## Interesting Viz
https://public.tableau.com/profile/kizley.benedict#!/vizhome/BangaloresBusRoutes/BMTCRoutes
http://bl.ocks.org/vlandham/raw/9216751/


https://github.com/geohacker/bmtc

## Advance Visualization
https://blog.mapbox.com/hello-mapbox-and-keplergl-4d71fc8e1d02
https://uber.github.io/kepler.gl/#/

## Autonomous Driving
- https://github.com/CPFL/Autoware
- https://github.com/OSSDC
- https://github.com/commaai/openpilot
- https://github.com/marsauto/europilot - to ber explored
- https://www.openmotors.co/
- https://www.nvidia.com/en-us/self-driving-cars/drive-platform/
- https://sourceforge.net/projects/stanforddriving/

## Self Driving Cars
- https://www.liveedu.tv/guides/x/self-driving-cars/history/

## Tools
- https://github.com/mapillary/mapillary_tools

## Map Examples
https://tjukanov.org/bubbling-trains/


## Google Maps Features/News
https://www.justinobeirne.com/google-maps-moat


## Image Processing
https://www.analyticsvidhya.com/blog/2014/12/image-processing-python-basics/

## Future Videos
https://www.youtube.com/watch?v=nOU_t4bqEJg&feature=youtu.be&t=33s

## Hardware Requirements
* https://support.pix4d.com/hc/en-us/articles/202559159-Recommendations-for-Hardware-and-Software-Configuration#gsc.tab=0

###Equipment

1. **Stereo Color Cameras**

	Data Sheet: https://www.ptgrey.com/support/downloads/10132
Getting Started Manual: https://www.ptgrey.com/support/downloads/10154
Software & Firmware Download: https://www.ptgrey.com/downloads

2. **GPS & IMU**

	* [Spatial Dual Data Sheet - PDF](http://www.advancednavigation.com.au/sites/advancednavigation.com.au/files/Spatial%20Dual%20Datasheet.pdf)
	* [Spatial Dual Software](http://www.advancednavigation.com.au/product/spatial-dual#software)

3. **Lidar**

    * ++**Option 1: Velodyne** - VLP 16 is shortlisted++
        * [DataSheet - PDF](http://velodynelidar.com/docs/datasheet/63-9229_Rev-D_Puck%20_Spec%20Sheet_Web.pdf)
        * [Velodyne Lidar VLP-16 : User Manual](http://velodynelidar.com/docs/manuals/63-9243%20Rev%20B%20User%20Manual%20and%20Programming%20Guide,VLP-16.pdf)
        * [Velodyne Lidar VLP-16 : Interface Box](Interface Box: http://velodynelidar.com/docs/notes/63-9259%20REV%20C%20MANUAL,INTERFACE%20BOX,HDL-32E,VLP-16,VLP-32_Web-S.pdf)
        * [Velodyne Lidar VLP-16 : Wiring Diagram](http://velodynelidar.com/docs/diagrams/86-0107%20REV%20A%20WIRING%20DIAGRAM,%20VLP-16.pdf)

    * **Option 2: Trimble**
        * [DataSheet - PDF](http://trl.trimble.com/dscgi/ds.py/Get/File-667710/MX2%20Single%20Head%20Offsets.pdf)

        **NOTE:** Trying to get more information on the Interfaces, user manuals etc.

    * **Option3: Quanergy**

        * [General Information](http://quanergy.com/m8/)

        **NOTE:** Trying to get more information on the Interfaces, user manuals etc.

## Software Requirements
### Photoscan
The number of photos that can be processed by PhotoScan depends on the available RAM and
reconstruction parameters used. Assuming that a single photo resolution is of the order of 10 MPx, 2GB
RAM is sufficient to make a model based on 20 to 30 photos. 12GB RAM will allow to process up to
200-300 photographs

- Batch processing
- scheduling tasks
- merging multiple files
- compute stats
- spatial index
- add projections

## Software Product Comparisions
* http://www.pi3dscan.com/index.php/instructions/item/agisoft-vs-capturingreality
* http://www.agisoft.com/forum/index.php?topic=3237.0
* https://www.reddit.com/r/3DScanning/comments/3vh6vu/comparison_between_reality_capture/

## Responsibilities and Expectations
Responsibilities and expectations will be as follows:-
* Will be working in the it replay system.
* Will work closely with Navada for specification and definition of replay system. customers will be MapMyIndia team (internal or its customers).
* Will work closely with Senthil as your internal customer. He will help you in feature definition as required by 20+ internal annotators.
* The feature set should be convenient for them, it should be user friendly and stable for their consumption.
* Will also participate in it recording system just to ensure your inputs are in required formats.
* The execution should be based on the technologies and methodologies vidteq has been using, such as adobe air or java cordova plus the html/css/javascript based frame work.

##Project objectives
###Summary
The process of understanding, analyzing and communicating the large spatial datasets output from multiple bumblebee camera, lidar and GPS is difficult; the data is time and location dependant 3-dimensional dataset. Visualization techniques can help to better understand the raw data, formulate suitable analysis methods and presents results.

We have identified chain of multiple toolsets under commercial and opensource categories for visualization of stereo images, GPS tracks and Lidar data. These tools can be used in combination for processing, visualization and analysis.

We are inspired and motivated to provide a cost effective custom software and techniques to process and visualize stereo data from 6 stereo cameras, 1 GPS and 1 lidar.

The effort here is to provide some type of data visualization to help communicate the wealth of information contained in the different type of datasets. One of the major challenges is the integration of data from a variety of sources while maintaining their geometric, topologic, semantic, and visual properties.

The tool should be able to evaluate and visualize the data coming from Record system, good enough to start annotation.

The goal of the project is to precisely measure any object in the view.

###High level specifications provided
* It Replay System should have multiple windows showing maps with point shoot and windows for each camera.
* Lidar also should have its own window for deeper look, otherwise it might be merged with camera window.
* There has to be a measuring tool to measure any element in the picture.
* The exact gui requirement of measuring tools will be finalized based on annotators requirement (need to work with Senthil for the same).

###High level specifications and future roadmap identified

++Assumptions:++
* Calibration
* Check for cosistency at the pre-processing stage

1. Data Collection
2. Processing
	* GPS data prcessing and trajector generation
	* LiDAR range processing and XYZ point cloud generation
	* Point cloud classification
3. Client
	* Visual inspection of data
	* Ground control points comparison
4. Data delivery/distribution

++Input++:
* Set of csv files, with each row pointing out the files to be processed and analyzed from the stereo camera, Lidar and GPS devices.
* Calibration files for stereo camera and Lidar

++Output++:
* Stereo image depth map and 3D ploint cloud data
* Accuracy: accurate within ++X centimeters++ positionally and ++Y centimeters++ vertically.
* The time and cost for creating 3D models ...........
* Level of Detail is X (LoDX)

## Discussion minutes

* Replay system at the high level can be broken down to three main components:-
	1. **Data Processing & Analysis Module**: Processing, visualization and analysis of Stereo Images & LiDar data.
	2. **Geo-referencing Module**: Visualization of Stereo and LiDar Data on Map
	3. **GUI Module**: Presentation


### 1. Data Processing & Analysis Module

#### A) Stereo Vision Module
**Introduction**
Stereo vision systems needs to be designed, built, and calibrated. All images obtained from the calibrated stereo systems would be processed using stereo system tools or stereo vision module.

**Goal**
1. Ability to measure the distance of the objects from the camera.
2. Ability to extract information about the length and width of the objects in addition to the distance from the camera.
	* By clicking on a point in the figure of the component view, the (X, Y, Z) information about that point is extracted. By clicking on the left and right side of the shelf and subtracting the X value, a calculation for width of the shelf can be found. Performing the same at the top and bottom of the shelf and subtracting the Y value will give a calculation for the height.
	* The results of the measured and calculated size of the end of the shelf are shown with the percent error

**Overview**
	The stereo system sends a left and right image of the 3-D scene it is viewing to the Stereo Vision Module. With these images, the calibration data, and re-projection data from calibration, the program rectifies the images, correlates the pixels, and re-projects the 2-D points to a 3-D point cloud. A point cloud is simply a set of X, Y, Z coordinates extracted from the x and y pixel coordinates and the disparity associated with each point. This point cloud is then imported to Quick Terrain Modeler (APL, 2003) where it can be viewed, edited, and analyzed. In addition, the color image taken by the stereo camera can be overlaid onto of the point cloud creating a texture map.

**Inputs**: Left & Right images, calibration file, reprojection matrix (per camera).

* Steps
	1. rectify, correlate and re-project images
	2. outputs the 3D point cloud
	3. view, edit, analyze 3D point clouds and overlay color texture
	4. Computation & identification of accuracies of x, y, and z distance measurements that were produced by re-projection
* Two ways of working:-
	1. Process Automatically and ouput the point cloud
	2. Load images, process them and display disparity maps and rectified pairs.

**1. rectify, correlate and re-project images**
* ++Rectification++: In order to rectify the two images sent to the module, there must be a **calibration file** present that was created from calibrating the same stereo system that captured the left and right images.
	* The effects of the rectification process are also easy to see by the objects in the left and right image being horizontally aligned, lined up on the green lines marking the epipolar lines.
	* From the rectified images, the correlation routine can be run on the image set, computing disparity values for each pixel. The disparity map for the rectified images, where brighter intensities represent objects that are closer to the camera. From the disparity map, the depth of each pixel can be computed and re-projected into a 3-D point cloud representing the 3-D scene.
	* ++Calibration File++: This file contains the following information: left and right camera matrices, left and right distortion vectors, rotation matrix, and translation vector. ( **++Camera Calibration Guide++** )

* ++Correlation++: The rectified pair of images is sent to the correlation routine to find matching pixels in the image.
	* Stereo Controls can be used for adjusting correlation variables.

**2. outputs the 3D point cloud**
* After viewing the results of the correlation process, a point cloud can be created and saved for viewing in a 3-D modeler. A point cloud is created by a set of (X, Y, Z) points determined by the pixel location in the image and the disparity found by the correlation process.
* The disparity for each point is used to first determine the Z distance of the point to the camera. Using the measured distance Z, the X and Y values are also determined for each pixel.
* The X and Y values correspond to the real world distance of a point from the camera center in meters.

**3. view, edit, analyze 3D point clouds and overlay color texture**
* Once the point cloud is generated and each point is saved to a text file, it is loaded into a viewer where it can be edited and viewed.
* In a viewer such as [**++Quick Terrain Modeler++**](http://appliedimagery.com/), the color image that was taken with the left and right black and white images can be overlaid as a texture map on top of the point cloud, to provide a realistic looking model of the terrain viewed from the stereo system.

	* Un-gridded 3-D Point Cloud generated from stereo vision system with height coloration overlay.
	* A wire mesh gridded surface model with a color map overlaid based on distance of the points from the stereo system.

**Tips**
* The stereo vision routines process images in a grayscale format.
* Stereo images can be used for a color texture overlay onto the 3D point cloud.
* The accuracy of distance measurement is directly related to camera orientation/position accuracy.
* Any motion of the cameras after calibration will result in error when row aligning the image planes during the rectification process.
* Accelerometers can be attached to the cameras for estimating deflection angles, and therefore to correct for small rotational changes of the cameras.

**Courses**
* https://courses.cs.washington.edu/courses/cse455/09wi/Lects/lect16.pdf [1 to 17]
* http://dusk.geo.orst.edu/gis/465lec.html


**References**
* Main References:
	* https://github.com/openMVG/openMVG/
	* http://scholar.lib.vt.edu/theses/available/etd-12232009-222118/unrestricted/Short_NJ_T_2009.pdf
	* https://www.youtube.com/watch?v=PR9tlFay0U8


#### B) LiDar Module

##### Overview


##### Wireframe conceptualizaion
* geo-referencing and data processing & analysis done w.r.t. each other context like side-by-side.
* geo-referencing and data processing & analysis done independently side-by-side.

##### Development Platform
* Environment - WebGL, JavaFX
* Tools
* Requirements
	* JDK, JRE 1.7+
	* WebGL 2.0 enabled browser

##### References
* WebGL
	* http://webglfundamentals.org/webgl/lessons/webgl-setup-and-installation.html
* Other References
	* http://opencv.org/about.html
	* http://docs.opencv.org/2.4.11/doc/tutorials/introduction/desktop_java/java_dev_intro.html
* JavaFX
	* Tutorials


**NOTE:** *Content below this is about the theoritical undestranding, concepts, references, toolsets, data samples. Project specific details to be mentoined above this section*

## High Definition (HD) Road Mapping System:-
1. A stereo camera and lidar based recording jig
2. Backend system to store HD Maps

### Summary
* Detailed tool evaluations are in progress
* Next milestone is to get one point cloud data through the pipe

### Terminology

#### DOT
* Single position (lat long)
* Multiple shots of stereo images in different directions
* Lidar data point cloud around this position
	* All points are lat long agnostic, centered around Dot

#### PCD - Point cloud data
* PCD-C - Point cloud data derived from Stereo images - Camera
* PCD-L – Point cloud data derived from Lidar
* PCD-G – Point cloud data Geo-referenced and merged

#### Frame of reference
* Car/Dot centric cloud - Angular coverage around car/dot center
* Geo Centric cloud – geo referenced cloud data
* Object centric cloud - Angular coverage around any object under
observation
	* Useful for creating 360 of an object and annotate/measure it

#### TPCD
* Tiled Point Cloud Data, uses WMS tile boundary

### Data Flow Block Diagram
* Data Plane should be scriptable/automatable
* Annotations are human interaction
* Supervision/nightly cron may be needed

#### ++Tool Point A Dot Visualizer++
* Offline Usage

#### ++Dot Visualizer - purpose++
* To see health of data (how TBD)
* Steer through data, dot to dot – to and from
* One dot at a time
* May be a play mode where dots can be played in sequence
* Calling to Tool chain B (stereo processor)
* Picture/lidar cloud alignment tool (TBD)
* Tool should comfortably handle the resolution required – because data is bulky

#### ++Tool Point B Stereo Depth Processor++
* Takes left right images as input (TBD because of triclops)
* Gives out PCD-C
	* Dot centric co-ordinates
* Compute intensive work, May need software license
* Tools – Closed source
	* TriClops from Point Grey itself
	* Others
* Tools – Open source
	* Estereo – an elementary software
	* Reality capture
* Tools – If we write
	* Possibly repetition TBD (estimation needed)

#### ++Tool Point C Geo Referencer++
* XYZ calculation with respect to Dot lat long
	* XYZ – lat,long,altitude
* Accurate geo position of DOT needed
* Merges PCD-L and PCD-C
	* RMS error should be reduced
	* Needs a Provision for manual alignment of clouds
* Outputs PCD-G
	* Which potentially can be projected over Dig Maps

#### ++Tool Point D Dot to TPCD Overlap processor++
* Petches corresponding TPCD
* Merges PCD-G points onto TPCD and writes back
* There is a problem of error accumulation
	* Needs to be mitigated
* There is problem of infinite accumulation of points
	* We need a mechanism to smoothen the grains
* Imagine it goes through same road 10 times
* And we ran system 10 times
* Same TPCD with object will be accumulated with PCD from 10 runs
* So data gets accumulated -
	* Are you merging or are you replacing?

##### Dot to TPCD overlap processing
> Dot to TPCD overlap processing
![Alt Text](Dot to TPCD overlap processing.png "Dot to TPCD overlap processin")

#### ++Tool Point E TPCD storage++
* TPCD is convenient data structure to keep PCD in small/consistent and scalable sets
* TPCD has color attribute to each point in the cloud
* Standard directory structure and naming convention
* Welknown WMS boundaries
	* Zoom 18 or 19 or 20 or 21
	* depending on resolution of camera
	* Depending on file size/number of files

#### ++Tool Point F PCD Visualizer++
* PCD-C, PCD-L are point centered cloud
* PCD-G is point centered cloud but with offset of dot position
* TPCD is geo centered cloud and tiled
* TPCD visualization
	* Needs a mechanism to fetch all the tiles in the view and show them abutting each other
	* It is like Openlayer
* Tools Closed source
	* Arc gis
	* mapInfo
* Tools open source
	* Veloview
* Tools – if we write – No use to write such software
	* But Plugins for TPCD visualization needs to be written

#### ++Tool Point G Annotation Software++
* Annotation is done over the PCD visualizer
* Annotation is currently manual
* In future Neural network/AI can be used
* Can do
	* Boxing
	* Measuring
	* Attributing
	* Classifying
* This is like our own plugin on top of purchased software
	* Like arcgis, mapinfo or veloview

### ++Resolution and Error budgeting++
* TBD


### ++Available Tools & Softwares++


### ++Recommendation for Tools & Softwares++

1. Terrain Model Creation/Manipulation - Terresterial
* Structure from Motion (SFM)
  - Agisoft Photoscan
  
* Point Cloud Manipulation
  *  Cloud Compare
    - PCD viewer and editor
  * I-Site studio from Maptek
    - Point Cloud Manipulation
    - Tin Creation, 3D mapping, & Orientation Analysis
    
2. 3D mapping - Once you have a terrain model, you have to be able to use it or it is just a pretty picture (or animation)
  * I-site studio
    - Pros: It has CAD tools that allow you to draw directly on the point cloud; that is, you can orient the model to a desired look direction, and using the mouse-- click click--you can draw a line that snaps to the closest point in the point cloud, forming a 3D line.
    - Cons: Downside in using  i-site for this application is that there is no ability to attach attributes to the line elements
  * ArcGIS pro
    - Pros: Overcomes the con of i-site studio
    - Cons:  Difficult to figure out how to best import the 3D surface model into ArcGIS Pro

3. 3D Model Building
  * I-site studio
    Cons: the model building capabilities are limited; mostly extrusions and a few other things
  
  * Move (Midland valley)
    Pros:
    - The biggest pro in Move is the rich 3D model building capability linked with tools for restoration, or the alternative, to do forward kinematic modeling.  Thus, if you can construct a 3D model in this software, you can, theoretically, also restore it and test for 3D balance, etc.
    - Other great points are the software can visualize colored point clouds (with a caveat below).
    - Also, the software has some slick tools for model construction, like extruding along a curved surface, or extending a surface along a line (potentially a curved line), joining and cutting surfaces, etc.
    Cons:
    - Like all this 3D software it has a seriously steep learning curve.  You almost have to take a short course from Midland Valley, or have someone who knows the software at least get you started.
    - Beyond that, the biggest weakness I see in Move is a rather mediocre visualization engine.  What I mean by that is that the software easily chokes on large models, even on a fancy computer.  I had originally hoped I could use the software for live 3D mapping in the field, but that is hopeless.  You need a VERY GOOD GPU to run this software well.  One example is that although you can in theory visualize a colored point cloud, the realities are that these gigantic point clouds we generate from SFM usually just make the software choke—think watching the little stop watch dial spinning for hours…  What that means is that you really need to do your interpretation of the surface model elsewhere (e.g. we use i-site) and then just do your model building in Move.
  * Geomodeler (Intrepid)
    
  * Leapfrog Geo (Leapfrog)
  Cons:
  -  inability to import our nice colored point clouds; so you could visualize your data in the same model that you are working in.

## Wireframe
1. Bare-Minimum Replay System
	- view only
	- intitution building
2. 2D toolbox -Lz, Sz, RMS error, intereaction of each dot data
3. 3D toolbox - Pure point cloud data visualization

* z-value from lidar and stereo-processing when hovered on the image (L/R)
* Calculate and show the root mean square error for evey pixel. Where, Lz - lidar depth; Sz - stereo depth


## FAQs/Meetings/Demos

### 30th-Jan'17
1. See in detail the different components of the Jig and the Gaze Software and the underlying processes 
2. Results of a small run when mounted on a vehicle and monitoring performance on full FPS of the camera 
3. This run will also include running the Jig by changing multiple locations of the camera on the vehicle 
4. A detailed analysis on the outputs captured by the camera and the GPS/ IMU 

5. Detailed Discussion on the Maze Software and answer of your queries including finalisation of the final process 
6. Detailed discussion on timeline analysis for the pending work like Lidar Integration, Stereo Camera integration and storage/ processing 
7. Detailed discussions on the tools for Maze and understanding the underlying effort/ costs 
8. Anything else you would like to discuss.
---
9. What is the triclops output?
  * Triclops to compute disparity/depth maps
  * disparity/depth maps
    - Points that are closer in the image are displayed as a lighter color of gray and invalid points are displayed as completely black.
  * depth map to be taken as input to generate PCL
  
## FAQs
```Q. What we are trying to do in totality?```
	- We will collect data from multiple stereo cameras, 360 degree Lidar and high precision GPS instruments mounted on a car. We will collect data at lest for 50 Kms.
	- Our main objective is to measure the dimensions of the objects from the stereo images and lidar data with high accuracy and geo-reference these objects accurately (+/- 1 meters in terms of lat-lon).
	- This provides the researchers with the novel dataset with opportunities for 3D map building and autonomous driving research.

```Q. Why we are building the replay system?```
	- we want to do measurement of object such as height of the object
	- geo-reference the object accurately (+/- 1 meter, in terms of lat-lon)
	- 3D model of a object, so that we can generate other views, like isometric, top or side views
	- just watch the replay (like VidTeq website/videomap)

> Ans. **This objective is to measure the dimensions of the objects with high accuracy and geo-reference these objects accurately of +/- 1 meters in terms of lat-lon.**

```Q. What are the top commercial softwares for handling the stereo images/lidar data?```
	- there's no single tool to do all the items listed in the question WHY?
	- are we sure.
	- is the cost prohibitive
	- are they obscelence
	- plugings for the well established existing software such as arc-gis, mapinfo, ROS, qgis

```Q. what are the open source alternatives?```

```Q. What are their capabilities?```
	- do they handle disparity data?
	- can they handle disparity data to point cloud data
	- given that we have disparity, what factors makes the value of z errorneous (This is a research topic)
		- single pixel gets the contribution from the object which has the depth varrying
		- every pixel correspondance to some surface at whatever distance,
		- if the pixel is pure, i mean the pixel correspondance to the surface, where every part of the surface is at the same distance (z-value)
		- will get accurate z
		- purity of pixel is also due to resolution, better the resolution, better the purity of pixel.
		- goining for higher resolution is the easiest way to get the better data, but that will come at higher cost
		- there more similar issues which is diluting the value of z
	- Is it required to be the part of our project scope?

```Q. What is the impact of calibration or lack of it on error budget?```
	- are their any self-correcting algorith, which can self rectify the calibration issues.

```Q. what are calibration parameters?```
	- (guess work)
	- baseline distance(b) and focal length (f) are the main parameters
	- how much of delta change in b and f can eff4ect the z calculation
	- is there any algorith to derive b and f from the pixel itself
	- is there any algorith that doesn't depend or minimaly depends on b and f (self-correcting)
	- how does camera tilt affects the calibration
	- how close the GPS (geo-reference) shoiuld be to the lidar; how does it effect the accuracy
	- likwise for the multiple stereo camera

## Conventions
```Q. What is dot?```
	- dot is a synchronized point which has a accurate gps value w.r.t. frame of reference of spatial dual.
	- synchronization of lidar and cameras using triggers (hardware pulse triggers)
	- it's a 4-tuple of (lat,lon,altitude,time) and it might have additional attributes such as pitch, yaw, roll
	- In 1-dot there may be one or more frames of lidar and one or more frames of bumblebee data.
	- eash of these frames will have a pre-set value of offset of the dot's 4-tuple. This offset is the calibration value and it will have an error budget.
	- higher the value this offset, accuracy of frame comes down.
	- we might need more and more reference point in order to reduce the error, which is nothing but more computation.
	- NOTE:- the data from the camera and lidar they cross-reference each other
	- consecutive dots can also cross-=reference the same point-cloud data
	- the parallax generated by dot-to-dot can also improve the root mean square point data cloud error
	- what is included
 
## Courses
* https://classroom.udacity.com/courses/cs373/lessons/48739381/concepts/487122860923
* https://www.udacity.com/self-driving-car

## Forums
* https://www.capturingreality.com/forum/viewtopic.php?f=3&t=192&start=10

## Blogs
* https://autodeskremake.squarespace.com/blog/2016/11/1/the-dos-and-donts-of-photogrammetry

## Tutorials
* http://paulbourke.net/miscellaneous/photoscantutorial/

## Photogrammetry Experts to follow on internet
* Wishgranter

## TBD
- does zoning is required for HD maps? How relevant it is?
- LoD level for road and road network?
  - what we can see in different sceneraios?
  - what we can't see?
    - underground pipelines, tunnels, sewage
      - does it create threat or opportunity
    - eletromagnetic radiations
      - can these cause interference to the autonomous vehicle's sensors
  - vertical objects, protusions, hanging cabels, electric cabels, road blockages during thunder storm or otherwise
  - u-turns, reverse, narrow roads, kaccha roads, water lodging
  - natural and man made disasters and calimities impact - floods, thrunderstorm impact: road blockages, dangerous electric cabels, fire, typoons
  - Drone networks, sky corridors