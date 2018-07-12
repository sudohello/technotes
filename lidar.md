/*
Title: LiDAR - Light Detection And Ranging
Decription: Basics of LiDAR
Author: Bhaskar Mangal
Date: 20 Dec 2016
Placing: 1
Tags: LiDAR, Photogrammetry, Concept
*/

### Lidar - Light Detection And Ranging

* Lidar (Light detection and ranging) is a popularly used technology to collect dense and precise data of topographic structures of the surface of the earth.
* LiDAR (Light Detection and Ranging) is a new approach to high-resolution surface model generation.
* Point cloud or positional vector data can be processed from raw lidar data. Point cloud datasets are generally visualized directly as a point cloud or in a derived form as a mesh. Additionally, raw lidar datasets contain noise due to instrumental errors and atmosphere. Hence, proper pre-processing and filtering are necessary for both managing large scale dataset as well as for denoising.
* Lidar data is monochromatic or grey scale. Colors can be added by mapping high resolution images on Lidar data with Geospatial referencing. [video](https://www.youtube.com/watch?v=TXK26JomCyU)

#### How Lidar works
A LiDAR scanner traces a narrow laser beam across a regular grid of sample points and measures the arrival time of reflected light for each sample point. Based on this time and the constant speed of light, the scanner can report the 3D positions of surface points lying inside a pyramidal region of space. Larger regions can be surveyed by aligning and merging multiple individual LiDAR scans. LiDAR's main benefits are accuracy of each sample point, and speed, i.e., the number of sample points that can be measured in a given time period.

#### Applications of Lidar
* The lidar (Light Detection and Ranging) technology is heavily used for flood-modeling and similar applications, such as, bathymetry, geomorphology, glacier modeling, etc.
* Airborne LiDAR mounts a downwards-pointing LiDAR scanner on a low-flying aircraft and is used to gather high-resolution DEMs (digital elevation models) of the Earth's surface. Data gathered by airborne LiDAR is generally treated as a height field and resampled to a regular grid of elevation postings.
* Terrestrial or tripod LiDAR, on the other hand, mounts a horizontally pointing LiDAR scanner on a tripod to gather ultra high-resolution 3D data of natural and man-made structures. Tripod LiDAR is typically treated as a "point cloud" sampling of arbitrary surfaces, and not resampled to a grid. It can generate samplings with sample spacings of less than a centimeter, and accuracies of around 2mm per sample.

#### Creation of DEM from LiDAR data

A Digital Elevation Model (DEM) is the generic name for any raster data containing elevation data. There are 3 types of DEMs that lidar2dems can generate:

Digital Terrain Model (DTM) - This is the calculated elevation using only points classified as ground.
Digtial Surface Model (DSM) - This is the calculated elevation using the highest non-ground points. In forested areas this corresponds to the absolute elevation of the top of the canopy, but it could also be the roofs of buildings or other structures.
Canopy Height Model (CHM) - This is the difference between the DSM and DTM, which is presumed to be a forested area, thus 'Canopy Height'.

lidar2dems uses the PDAL library (and associated dependencies) for doing the actual point processing and gridding of point clouds into raster data.

#### LiDar VLP-16 Velodyne

> **Overview of the LiDAR VLP-16 3D Imaging System**
![Alt Text](Overview of the LiDAR VLP-16 3D Imaging System.png "VLP-16")

The VLP-16 creates 360º 3D images by using 16 laser/detector pairs mounted in a compact housing. The housing rapidly spins to scan the surrounding environment.
* The IP address for each VLP-16 is set at the factory to 192.168.1.201, but can be changed by the user via the WebServer GUI.
* The VLP-16 is only compatible with network cards that have either MDI or AUTO MDIX capability.

** Output:**
* Up to 0.3 million poin* ts/second
* 100 Mbps Ethernet Connection
* UDP packets containing
	* Distances
	* Calibrated relectivities
	* Rotation angles
	* Synchronized time stamps (ìs resolution)
* $GPRMC NMEA sentence from GPS receiver (GPS not included)

> **VLP 16 DSR Channel**
![Alt Text](VLP-DSR-channel.png "VLP 16 DSR Channel")

**GPS**
* The VLP-16 can synchronize its data with precision, GPS-supplied time pulses enabling users to determine the exact firing time of each laser.
* External synchronization requires a user supplied GPS receiver generating a synchronization Pulse Per Second (PPS) signal and a NMEA $GPRMC message (Appendix B). The $GPRMC message provides minutes and seconds in Coordinated Universal Time. Upon synchronization, the sensor will read the minutes and seconds from the $GPRMC message and use that to set the sensor’s time stamp to the number of microseconds past the hour per UTC time. Synchronizing the VLP-16’s timestamps to UTC allows third party software to easily geo-reference the LiDAR data into a point cloud.
* The user must configure their GPS device to issue a once-a-second synchronization pulse (PPS, 0-5V, rising edge), typically output over a dedicated wire, and issue a once-a-second NMEA standard $GPRMC sentence. No other output message from the GPS will be accepted by the VLP-16.

**Geo-referencing**
The sensors can synchronize their data with precise GPS-supplied time. Synchronizing to the GPS pulse-per-second (PPS) signal provides the ability to compute the exact firing time of each data point which aids in geo-referencing and other applications.

**Unique features include:-**
* Horizontal Field of View (FOV) of 360°
* Rotational speed of 5-20 rotations per second (adjustable)
* Vertical Field of View (FOV) of 30°
* Returns of up to 100 meters (useful range depends on application)

Most users will elect to create their own application-specific point cloud tracking and plotting and/or storage scheme. There are several fundamental steps to this process:-

**1. Establish communication with the VLP-16**
	The VLP-16 outputs two separate broadcast UDP packets. By using a network monitoring tool such as Wireshark (https://www.wireshark.org/download.html) you can capture and observe the packets as they are generated by the unit.

**2. Parse the data packets for rotational angle, measured distance, and reported calibrated reflectivities**
	Your software needs to read the data packet from the Ethernet port, and extract the azimuth, elevation angle, distance to the object, and time stamp. Once the data is identified, proceed to the next step.
	The VLP-16 outputs two types of UDP Ethernet packets: Data Packets and Position Packets.
> **VLP-16 Data Packet Formet**
![Alt Text](VLP-16-data-packet.png "Data Packet")

**3. Calculate X, Y, Z coordinates from reported rotational angle, measured distance, and vertical angle dependent on laser ID**
	The VLP-16 reports coordinates in spherical coordinates (r, ω, α). Consequently, a transformation is necessary to convert to XYZ coordinates. The vertical/elevation angle (ω is fixed and is given by the Laser ID (Appendix A). The position of the return in the data packet indicates the Laser ID. The horizontal angle/azimuth (α) is reported at the beginning of every other firing sequence, and the distance is reported in the two distance bytes. With this information X, Y, Z coordinates can be calculated for each measured point. Points with distances less than one meter should be ignored. The conversion is shown in Figure 8 on the following page.

**4. Plot or store the data as needed**
	The calculated X, Y, Z data is typically stored for later processing and/or it is displayed on a computer as a series of point clouds. The VLP-16 has the capability to synchronize its data with GPS precision time via a Pulse Per Second (PPS) signal from a GPS receiver. A synchronized timestamp from the VLP-16 sensor may be used to match the data stream from the sensor with the data stream from the attached external GPS receiver and/or Inertial Measurement Unit (IMU).

> **Spherical to XYZ Conversion**
![Alt Text](spherical-to-cartesian-coordinate.png "spherical-to-cartesian-coordinat")

**References**
* [VLP 16 User manual](63-9243 Rev B User Manual and Programming Guide,VLP-16.pdf)

#### Data formats for Lidar Data
* .las; .laz
* .pcap
* .csv

**What is the LAS Format?**

The LASer (LAS) File Format file format is a public file format for the interchange of 3-dimensional point cloud data data between data users. Although developed primarily for exchange of lidar point cloud data, this format supports the exchange of any 3-dimensional x,y,z tuplet. This binary file format is a alternative to proprietary systems or a generic ASCII file interchange system used by many companies. The problem with proprietary systems is obvious in that data cannot be easily taken from one system to another. There are two major problems with the ASCII file interchange. The first problem is performance because the reading and interpretation of ASCII elevation data can be very slow and the file size can be extremely large, even for small amounts of data. The second problem is that all information specific to the lidar data is lost. The LAS file format is a binary file format that maintains information specific to the lidar nature of the data while not being overly complex.
http://www.asprs.org/misc/las-key-list.html


#### Data Samples & Videos
* https://www.youtube.com/watch?v=7BUFxkyH1r0
* https://midas3.kitware.com/midas/community/29
* http://masc.cs.gmu.edu/wiki/PCL
* http://masc.cs.gmu.edu/wiki/MapGMUData2016Spring
* https://github.com/Kitware/VeloView/tree/master/share

#### Tutorials & Workshops
* http://www.opentopography.org/learn/tutorials
* http://applied-geosolutions.github.io/lidar2dems/tut/exploring-point-clouds.html


#### References
* [Lidar](http://idav.ucdavis.edu/~okreylos/ResDev/LiDAR/)
* [Remote Interactive Visualization of Parallel Implementation of Structural Feature Extraction of Three-dimensional Lidar Point Cloud - PDF](http://iiitb.ac.in/GVCL/pubs/2014_KumariAsheSreevalsanNair_preprint.pdf)
* [An Overview of Lidar Point Cloud Processing Software - PDF](http://ncalm.cive.uh.edu/sites/ncalm.cive.uh.edu/files/files/publications/reports/GEM_Rep_2007_12_001.pdf)
* http://www.gcc.tu-darmstadt.de/home/proj/fssr/
* [photomodeler](http://www.photomodeler.com/downloads/downloads14.html)
* http://lidarnews.com/

##### Tools & Softwares
* [List_of_programs_for_point_cloud_processing](https://en.wikipedia.org/wiki/List_of_programs_for_point_cloud_processing)
* https://rapidlasso.com/
* http://plas.io/
* http://www.terrasolid.com/products/terrascanpage.php
* https://github.com/LAStools/LAStools
* http://keckcaves.org/software/start
* https://github.com/KeckCAVES/LidarViewer
* https://www.cs.unc.edu/~isenburg/lastools/download/
* https://www.cs.unc.edu/~isenburg/
* http://www.mrpt.org/list-of-mrpt-apps/
* http://potree.org/
* https://github.com/potree/potree
* http://vcg.isti.cnr.it/nexus/
* http://3dhop.net/howto.php#ht_modelprep
* https://github.com/simonfuhrmann/mve
* http://www.gcc.tu-darmstadt.de/home/proj/fssr/
* http://www.gcc.tu-darmstadt.de/home/proj/mve/index.en.jsp
* http://opentopo.sdsc.edu/tools/listTools
* Fugroviewer (2.0 and up) by Fugro
* QT Modeler (7.1.6 and up) by Applied Imagery
* ERDAS IMAGINE (14.1 and up) by Hexagon Geospatial
* Global Mapper (13.1 and up) by Blue Marble Geo
* Trimble RealWorks (8.1 and up) by Trimble Navigation Limited
* ENVI LiDAR (5.1 and up) by Exelis VIS
* FME (2012 and up) by Safe Software
* TopoDOT by Certainty3D
* Pointools by Bentley Systems
* Pix4uav by Pix4D
* Opensource; CloudCompare by Daniel Girardeau-Montaut;  http://www.danielgm.net/cc/
* Commercial; clouds2max; http://www.clouds2max.com/system-and-software-requirements/
* SURE by nframes
* Pointfuse by Arithmetica
* LAStools by rapidlasso - fast tools to catch reality
* plas.io 3D Web Viewer by Hobu Inc.
* RiProcess by RIEGL LMS GmbH
* CloudPro by Leica Geosystems AG
* Optech LMS (3.0 and up) by Teledyne Optech
* Leica LIDAR Survey Studio LSS (2.2 and up) by Leica Geosystems AG
* FUSION (3.40 and up) by Bob McGaughey of the USDA
* ZEB1 by 3D Laser Mapping
* OCAD (11.4.0 and up) by OCAD Inc.
* Gexcel R3 by Gexcel
* Voyager (1.3 and up) by Voyager GIS
* LIDAR Analyst (5.2 or 6.0 and up) by TEXTRON Systems
* TerraScan, TerraMatch, TerraPhoto, and TerraSlave (015.xxx and up) by Terrasolid
* Carlson (2016 and up) by Carlson Software
* Remote Sensing Software by Joanneum Research Forschungsgesellschaft mbH
* LiMON Viewer by Dephos Software
* Scanopy by imagination
* WinGeoTransform by KLT Assoc
* BayesStripAlign by BayesMap Solutions, LLC
* Point Cloud Technology by Point Cloud Technology, GmbH
* Scalypso by Ingenieurbuero Dr.-Ing. R. Koenig
* Photogrammetry Software by Menci Software
* TcpMDT by Aplitop
* PhotoMesh by SmartEarth
* QINSy - Quality Integrated Navigation System by Quality Positioning Services (QPS) B.V.
* Potree Converter (1.0 and up) by Markus Schuetz
* FLAIM by Fugro GeoServices B.V.
* ScanLook by LiDAR USA
* GRASS GIS (7.0 and up) by Open Source Geospatial Foundation (OSGeo)
* OPALS by TU Vienna
* Scop++ (5.5.3 and up) by Trimble and TU Vienna
* DTMaster (6.0 and up) by Trimble INPHO
* Pythagoras by Pythagoras BVBA
* EspaEngine by ESPA Systems
* Blaze Point Cloud and Blaze Terra by Eternix Ltd
* ReportGen (2.9.0 and up), by PDF3D
* OrbitGIS by Orbit
* PFMABE Software by PFMABE Software
* K2Vi by AAM Group
* Card/1 (8.4 and up) by IB&T GmbH
* SceneMark by XtSense GmbH
* LiS by LASERDATA
* PointCloudViz by mirage
* Geoverse by euclideon
* PointCab by PointCab GmbH
* Z+F SynCaT Mobile Mapping Software by Z+F Zoller+Frohlich
* LidarViewer by routescene
* 3Dsurvey by Modri Planet d. o. o.
