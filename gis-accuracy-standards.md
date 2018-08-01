/*
Title: Time Keepers - GIS Accuracy Standards
Decription: Time Keepers - GIS Accuracy Standards
Author: Bhaskar Mangal
Date: Jul-2017
Last Updated: Jul-2017
Tags: Time Keepers - GIS Accuracy Standards
*/


>**Follow here:-**
> Blog, forum, k-bank, scripts
>[![Alt Blog, forum, k-bank](logos/blogger-logo-2.png "Blog, Forum, knowledge-bank"  "width:65px;margin-right:20px")](http://hdmapforselfdrivingcar.blogspot.in/) [![Alt Scripts](logos/git-hub-2.png "Scripts"  "width:23px;")](https://github.com/mangalbhaskar/linuxscripts)

**by [Bhaskar Mangal](http://www.bhaskarmangal.com/)**
27^th^ Jul 2017

**Table of Contents**
[TOC]

##Time Keepers - GIS Accuracy Standards
> A prolog to GIS Survey Standards & Specifications

* [Click here to view ++Main Presentation - **27^th^ Jul 2017** ppt++](ppts-pdfs/gis-accuracy-standards-time-keepers.pdf)
* "Once synchronised, a cesium atomic clock—which harnesses the transition of electron energy levels in cesium atoms to measure time accurately—won't miss a second in 10,000 years. It is far superior to a quartz clock, which needs tuning every few months"
* The International Earth Rotation and Reference Systems Service (IERS), which monitors the earth's rotation through observatories across continents, adjusts Coordinated Universal Time (UTC)—determined by the Bureau International des Poids et Mesures (BIPM) in Paris—accordingly whenever necessary.
* Knowing the exact time may not be important to you and me, but those who use the Global Positioning System (GPS), for example, need an accurate measure, down to the nanosecond. (In one nanosecond, a billionth of a second, light travels 30 cm.) The accuracy of GPS coordinates depends on the accuracy of the time measure given by the atomic clock on the GPS satellite. Dr Banerjee explains. Over 350 atomic clocks around the world compare their time with GPS time and send the data to the BIPM, which calculates UTC as an average of the global atomic clock measures.
* The US has about 150 atomic clocks. In India, apart from NPL, ISRO has a few
* The most accurate clock in the world, the cesium fountain clock developed in France and the US, makes the Rs 35-lakh cesium atomic clock seem antique. It can run for 20 million years without derailing the time measure by even a second. NPL is trying to develop one of these, but has so far met with little success.
* NPL uses INSAT to transmit the correct time, down to the nanosecond, to high-accuracy users. For low-accuracy users who are content watching the milliseconds roll, Dr Banerjee developed a much cheaper alternative that could receive electronic signals from NPL through a phone line. The Tele Clock was launched in 2000 and is now ticking away at the Parliament, airports and railway stations across the country, and even in Nepal and Saudi Arabia. The digital clock automatically dials NPL at regular intervals—maybe once a day—for the correct time, updates itself and disconnects to run on its own quartz mechanism.
* Since 1983 , the standard meter has been redefined as the length of the path traveled in the vacuum by the light for a duration of 1/299 792 458 seconds.

## GIS

### Introduction

**Shape of the Earth**
* We think of the earth as a sphere, when it is actually an ellipsoid, slightly larger in radius at the equator than at the poles.
* Since the **Geoid** varies due to local anomalies, we must approximate it with a ellipsoid.
* Over time, geodetic data have evolved from simple flat surfaces to spheres to complex ellipsoids.
* Flat earth models can be accurate for short distances (i.e., less than 10 km), spherical earth models for approximate global distance calculations, and ellipsoidal earth models for accurate global distance calculations.


**Datum**
A datum (plural datums) is a reference from which measurements are made.
* It is an associated model of the shape of the earth (ellipsoid) to define a Geographic Coordinates.

**Geodetic datum**
* A geodetic datum defines the size and shape of the earth and the origin and orientation of the axis used to define the location of points.
* Horizontal datums are used for describing a point on the earth’s surface, in latitude and longitude or another coordinate system.
* Vertical datums measure elevations or depths.
	* A vertical datum defines the “zero reference” point for elevation, z
	* Eg: NGVD29 (National Geodetic Vertical Datum of 1929), NAVD88 (North American Vertical Datum of 1988)
	* Takes into account a map of gravity anomalies between the ellipsoid and the geoid which are relatively constant.
	* Elevation is measured from the Geoid
* Mean sea level is the surface of constant gravitational potential called geoid
* To perform surveying and Mapping a datum and coordinate system is required.
* **Datum used in Surveying:**
	* Horizontal Datum- (Ellipsoid)
	* Vertical datums – (Geoid/MSL)

**Map Projections**
* A map projection is a mathematical algorithm to transform locations defined on the curved surface of the earth into locations defined on the flat surface of a map.
* The earth is first reduced to a globe and then projected onto a flat surface.
* **Map Distortion**
	* In the process of transforming a curved surface into a flat surface, some geometric properties are modified.
	* The geometric properties that are modified are: Area (important for mass balances) Shape, Direction, Length.
	* The difference between map projections has to do with which geometric properties are modified.
	* Depending on the type of analysis, preserving one geometric property might be more important than preserving another.
	* Equal area projections: Preserves area.
	* Equidistant projections: Preserves the distances between certain points.
* **Types of Projections**
* Conic: Screen is a conic surface.
	* Lamp at the center of the earth. Examples: Albers Equal Area, Lambert Conformal Conic. Good for East-West land areas.
* Cylindrical: Screen is a cylindrical surface.
	* Lamp at the center of the earth. Example: Transverse Mercator. Good for North-South land areas.
* Azimuthal: Screen is a flat surface tangent to the earth.
	* Lamp at the center of the earth (gnomonic), at the other side of the earth (stereographic), or far from the earth (orthographic). Examples: Lambert Azimuthal Equal Area. Good for global views.

**Coordinate Systems**
* A coordinate system is used to locate a point of the surface of the earth.
	* **Global Cartesian coordinates** (x, y, z) for the whole earth
* **Geographic Coordinates**
	* (f, l, z) for the whole earth
	* Earth datum defines the standard values of the ellipsoid and geoid.
	* Latitude (f) and longitude (l) are defined using an ellipsoid.
	* Elevation (z) is defined using a geoid.

* **Projected coordinates**
	* (x, y, z) on a local area of the earth’s surface
	* Universal Transverse Mercator (UTM) - a global system developed by the US Military Services.
		- zones are 6° wide, and go from pole to pole 60 zones cover the earth from East to West Reference Latitude (fo), is the equator
		- Each zone has a Central Meridian (lo)
		- Reference Latitude (fo) is the equator
		- (Xshift, Yshift) = false easting and northing so you never have a negative coordinate
		- Units are meters

* Careful attention must be paid to the projection, datum and coordinate system for every piece of GIS data used.
* Failure to use data from the same system OR change the data (re-project) it to the desired system will result in overlay errors
* Can range some small to SIGNIFICANT Real danger is when the errors are small (possibly unnoticed) Shapefiles, images, grids all have this data inherent in their very creation.
* Usually included in a system of files known as “metadata” or xxxxxx.PRJ file.

## SatNav - Satellite Navigation

**GPS**
* The primary methods of data collection are guided and controlled by the existence and use of accuracy standards. Accuracy standards for primary methods of surveying and mapping have been in existence for many years.
* The most widely used satnav system is the American Global Positioning System. The GPS that’s used by our phones and Google Maps and the Garmins in our cars are operated with the help of the American-owned and American-military-controlled GPS system.
**What is GPS?**
GPS (Global Positioning System) is a global satellite-based navigation system made up of a network of 24 satellites placed into orbit by the U.S. Department of Defense (DoD). It is a U.S.-owned utility that provides users with positioning, navigation, and timing (PNT) services. This system consists of three segments: the space segment, the control segment, and the user segment. GPS is operated and maintained by the U.S. Air Force (Source: HERE). It is currently the world’s most utilized satellite navigation system.

**GLONASS**
* Russia too developed its own global satnav system called GLONASS (GLObal NAvigational Satellite System) at the same time as the US. However, due to financial constraints, it took a long time to be completed and made truly available. As of today, GLONASS and GPS are compatible with each other and both nations make use of each other’s satellites for their own systems.
* Three of these will be geostationary over the Indian Ocean, i.e., they will appear to be stationary in the sky over the region, and four will be geosynchronous – appearing at the same point in the sky at the same time every day.

**NavIC (IRNSS)**
>Navigation with Indian Constellation

* As with all other satnav systems, IRNSS will provide two services: a free one for civilians and a strongly encrypted one for the military. The civilian service is called the Standard Positioning Service (SPS) and will have an accuracy of up to 20 metres while the encrypted Restricted Service (RS), for authorised users only, could possibly have an accuracy of up to 10 cm — standard for most military systems.
* However, just as mobile phones come with a GPS receiver, users will require a special bit of hardware to receive and use IRNSS data. These receivers are currently being manufactured in the country and will be able to download signals from the GPS and GLONASS systems as well.
* IRNSS, aims to be autonomous and independent while still maintaining compatibility with GPS and GLONASS.
* 2 types of services that IRNSS will be offering. The first is called Standard Positioning Service (SPS) which is for civilian use. This will have an accuracy of 20m, while the second is called Restricted Services (RS), which can detect movement of objects by less than 10m.
* GPS services weren’t available to defence forces specially and we needed that thus came NAVIC.
* Indian army used both GPS and GLONASSfor guidance but in 1999 during the kargil war the U.S refused to provide GPS services to India so this lead to the beginning of the Navic program program , now India uses a mix of GLONASS, Navic and GPS in its systems as fail safe mechanism so if one fails the other would still work.
* NavIC ('Navigation with Indian Constellation' whose Hindi meaning is 'sailor' or 'navigator')


**GAGAN**
* IRNSS is independent of India’s existing regional satnav system, GAGAN (GPS Aided GEO Augmented Navigation), built by ISRO in conjunction with the Airports Authority of India.
* Today, GAGAN is primarily used by the commercial airline industry and by scientists studying the ionosphere. As the name suggests, GAGAN takes the help of the American GPS constellation for its functioning.


**GNSS?**
GNSS stands for Global Navigation Satellite System, and is the standard generic term for satellite navigation systems that provide autonomous geo-spatial positioning with global coverage. This term includes e.g. the GPS, GLONASS, Galileo, Beidou and other regional systems. GNSS is a term used worldwide The advantage to having access to multiple satellites is accuracy, redundancy and availability at all times.  Though satellite systems don't often fail, if one fails GNSS receivers can pick up signals from other systems.  Also if line of sight is obstructed, having access to multiple satellites is also a benefit.  Common GNSS Systems are GPS, GLONASS, Galileo, Beidou and other regional systems.
* Global Positioning System (GPS) is owned by the United States.
* GLONASS is owned by Russia.
* The third GNSS- GALILEO of European Union
	* It isn’t completely operational yet, 12 of 30 satellites in orbit.
* The forth BeiDou (Chinese Navigation system)
	* It is a limited test system, its full-scale global navigation system or GNSS also known as COMPASS or BeiDou-2 is currently under construction, it has about 20 satellites in orbit at present.

**Global Navigation Satellite System (GNSS) and Satellite-Based Augmentation System (SBAS)**
* US: GPS (Global Positioning System)/Navstar
	- WAAS, LAS
* Russia: GLONASS (Global Navigation Satellite System)
* European Nations: Galilieo
* China: BeiDou (COMPASS)
* India: NavIC (IRNSS)
	- GAGAN
* Japan
	- MSAS
* France
	- DORIS
* GPS stores the positions of all the statellites in a file called ALMANAC

## GIS Accuracy Standards

* digital cartographic data standards
* Spatial Accuracy Standards for Large-Scale Topographic Maps
* SatNav system

**Caltrans standards for survey accuracy**
* They are based on the standards set by the Federal Geographic Data Committee’s Geospatial Positioning Accuracy Standards

**Geospatial Positioning Accuracy Standards**
* methodology for reporting the accuracy of horizontal coordinate values and vertical coordinate values for clearly defined features where the location is represented by a single point coordinate

* **survey monuments**
such as brass disks and rod marks; prominent landmarks, such as church spires, standpipes, radio towers, tall chimneys, and mountain peaks; and targeted photogrammetric control points.


It provides a means to directly compare the accuracy of coordinate values obtained by one method (e.g., a cartographically-derived value) with that obtained by another method (e.g., a Global Positioning System (GPS) geodetic network survey) for the same point.

**Notes**
Different Satellited/Space based Positioning, Navigation and Timing (PNT) have been developed, initially for the military purpose and extended to public for free of direct user fee.

US and Russia (then Soviet Union) were the first countries to leap fron in space based PNT development.






http://slideplayer.com/slide/9508891/

* Surveyors want grid (X) Easting (Y) Northing (Z) Elevation vertical datum Z Y X
* Surveyors prefer to work in a grid coordinate system coordinates expressed as (X,Y,Z) or Easting, Northing, and Elevation
* Assumed local grid coordinates origin is defined at the Earth’s Surface.
* Pre-defined National Mapping datum origin is defined at (or near) the surface of the reference ellipsoid.
* X and Y axis are perpendicular to each other, in the Local Plane.
* Z axis is perpendicular to the local plane. Prime orientation axis (Y) is Grid North

GPS:
The U.S. Government is committed to meeting and exceeding the minimum levels of service specified in this SPS PS and this commitment is codified in U.S. Law (10 U.S.C. 2281(b)).
- GPS initial operational capability (IOC) in 1993
- GPS has provided positioning, navigation, and timing services to military and civilian users on a continuous worldwide basis since first launch in 1978.
- SPS PS apply only to users of the L1 (1575.42 MHz) Coarse/Acquisition (C/A) signal, since this is the only civil GPS signal that has reached full operational capability
- An unlimited number of users with a civil or military GPS receiver can determine accurate time and location, in any weather, day or night, anywhere in the world.

Global Navigation Satellite System (GNSS) and Satellite-Based Augmentation System (SBAS) providers to ensure compatibility and interoperability of GPS with emerging systems for peaceful, civilian worldwide use.

The Navstar Global Positioning System, hereafter referred to as GPS, is a space-based radionavigation system owned by the United States Government (USG) and operated by the United States Air Force (USAF).

The Precise Positioning Service (PPS) is available primarily to the military of the United States and its allies for users properly equipped with PPS receivers. The Standard Positioning Service (SPS), as initially described in the SPS Signal Specification, was originally designed to provide civil users with a less accurate positioning capability than PPS, through a feature known as Selective Availability (SA). 

http://www.nstb.tc.faa.gov/

**Keywords**
* SPS - Standard Positioning Service
* PNT - (Space based) Positioning, Navigation and Timing
* SIS - Signal-in-Space (accuracy)
* Geo-fences, GNSS road pricing, War driving, Photographic geocoding, Geocaching (like treasure hunting/letterboxing)
* CORS - Continuously Operating Reference Stations
* FBN - Federal Base Network
* CBN - Cooperative Base Network
* UDN - User Densification Network

Local Accuracy (see Appendix A) is an average measure (e.g. mean, median, etc.) of the relative accuracies of the coordinates for a point with respect to other adjacent points at the 95% confidence level.

The Network Accuracy (see Appendix A) of all Cadastral Measurements should be reported per the Federal Geographic Data Committee (FGDC) Geospatial Positioning Accuracy Standards to show the relationship of the cadastral survey relative to the National Spatial Reference System.

FGDC - Federal Geographic Data Committee, Geospatial Positioning Accuracy Standards

A least squares adjustment or other multiple baseline data analysis is performed to produce a weighted mean average to verify the required level of positional accuracy has been achieved.

National Spatial Reference System (NSRS) is defined and managed by the National Geodetic Survey (NGS). It is a consistent national coordinate system that specifies latitude, longitude, height, scale, gravity, and orientation throughout the Nation, as well as how these values change with time. 

**Survey standards** may be defined as the minimum accuracies deemed necessary to meet specific objectives.
**Specifications** are the procedural requirements that will achieve the required accuracy, proving that the survey results weren't a matter of chance, but an indication of the survey's precision.
- Specifications for field procedures
  - Global Positioning System (GPS) Survey Specifications
  - Total Station Survey System (TSSS) Survey Specifications
  - Differential Leveling Survey Specifications

Without the use of proper procedures, chance or compensating gross and systematic errors can produce results that indicate a level of accuracy that has not been met. After standards and specifications, the third requirement that must be met is monument stability
**monument stability**
- Primary control monuments should have an indefinite life span
- while project control monuments need to last at least the life of a project
- Supplemental monuments are set as needed for specific purposes, and don't have a specific life span

**common methodology** for reporting the accuracy of horizontal and vertical coordinate values for clearly defined features where the location is represented by a point. Examples are active survey monuments, such as Continuously Operating Reference Stations (CORS) or VLBI1; passive survey monuments, such as brass disks and rod marks; and temporary points, such as photogrammetric control points or construction stakes.

**Accuracy and Precision**
* Accuracy is the degree of conformity with a standard or a measure of closeness to a true value. Accuracy relates to the quality of the result obtained when compared to the standard.
* **Precision**
  - It is the degree of refinement in the performance of an operation (instrumentation and procedures) or in the statement of a result. The term precise also is applied, to methods and equipment used in attaining results of a high order of accuracy.
  - Precision is indicated by the number of decimal places to which a computation is carried and a result stated.
  - However, calculations are not necessarily made more precise by the use of tables or factors of more decimal places. The actual precision is governed by the accuracy of the source data and the number of significant figures rather than by the number of decimal places.

**Positional and Relative Closure Ratio Accuracy**

* Positional accuracy
* Relative closure ratio (Proportional) accuracy


* **geodetic control surveys**
	- In surveying and mapping large areas, It is first necessary to establish frameworks of horizontal, ertical, and gravity control.
	- A reference system, or datum, is the set of numerical quantities that serves as a common basis.

Three National Geodetic Control Networks have been created by the Government to provide the datums. It is the responsibility of the National Geodetic Survey (NGS) to actively maintain the National Geodetic Control Networks.

These control networks consist of stable, identifiable points tied together by extremely accurate observations. From these observations, datum values (coordinates or gravity) are computed and published. These datum values provide the common basis that is so important to surveying and mapping activities.

It is not feasible for all points in the control networks to be of the highest possible accuracy. Different levels of accuracy are referred to as the "order" of a point

The combination of survey design, instrumentation, calibration procedures, observational techniques, and data reduction methods is known as a measurement system

The user should first compare the distribution and accuracy of current geodetic control with both' immediate and long-term needs. From this basis, requirements for the extent and accuracy of the planned survey are determined. The classification standards of the control networks will help in this formulation. Hereafter, the requirements for the accuracy of the planned survey will be referred to as the "intended accuracy" of the survey. A measurement system is then chosen, based on various factors such as: distribution and accuracy of present control; region of the country; extent, distribution, and accuracy of the desired control; terrain and accessibility of control; and economic factors. 

Vertical Datums Defines a system of zero surface elevation
This surface is then used to reference heights Many vertical datums reference the geoid as a surface of zero elevation The geoid can be described as the surface of the earth if it was completely covered by water. This surface would be smooth but highly irregular reflecting changes in gravity due to the earth irregular surface.

Horizontal Datums Forms the basis of horizontal coordinates
Earth is modeled as an ellipsoid The center of the ellipsoid must coincide with the earths center of mass A datum is then placed on the ellipsoid for reference

World Geodetic System 1984 The reference coordinate system used by GPS
Globally consistent within ± 1 meter Datum is located at where the Prime Meridian and Equator cross

WGS 84 Coordinates WGS 84 are used by GPS systems
Land Surveys conducted with GPS will consist of WGS 84 coordinates with coinciding elevation measurements. WGS 84 Survey Surveys in this raw form are not very useful.
The longitude and latitude are simply references to the WGS 84 datum measured in degrees The elevation is measured in a unit of length from a reference geodic elevation. Longitude and latitude do not provide measurements of length. Without measurements of length, one cannot calculate area, volume, or slope.

Cartesian Coordinates
A better way to represent these data would be in a Cartesian form (X,Y,Z) in units of (length,length,length) - i.e. (m,m,m) or (ft,ft,ft) There is a need to find a practical way to convert (degrees longitude, degrees latitude, m) to (m,m,m)

In order to convert from degrees to meters. Assume that the ellipsoidal based datum of the WGS 84 system can also be modeled as a sphere. Assumptions This allows a constant earthly radius (R) The radius of the earth is approximately 6,371 km (3,959 mi)

Choosing a Datum
In order to assign Cartesian values to WGS 84 coordinates, we must establish a datum from which each point will be referenced from.
A wise choice for a field survey datum would be the minimum observed longitude, latitude, and elevation. Doing this will assure that all the converted data will be positively referenced from the datum.
This will allow for the data to fit exclusively into the first quadrant when plotted.



Once you have a mathematical model of the size and shape of the earth, you can apply a coordinate system to in. Datum provides an origin that gives meaning to the coordinates. When a datum is applied to reality, error is introduced

Different Datum are more accurate for different parts of the world.

GPS has contributed to Datum Development over time
WGS 84 - World Geodetic System 1984
the reference frame upon which all geospatial-intelligence is based
Latest update 2004
NGS - National Geodetic Service
Brass markers are placed to pinpoint locations based on Datum
WGS 84 information -

UTM & State Plane
UTM
The National Imagery and Mapping Agency (NIMA) (formerly the Defense Mapping Agency) adopted a special grid for military use throughout the world called the Universal Transverse Mercator (UTM) grid. In this grid, the world is divided into 60 north-south zones, each covering a strip 6 degrees wide in longitude. These zones are numbered consecutively beginning with Zone 1. In each zone, coordinates are measured north and east in meters.
UTM Info -
State Plane Info -

Geographic Grid Coordinate System
Degrees, Minutes, Seconds
DD MM SSS
Decimal Degrees
DD.MMMMMMMM
Origin
Equator
Prime Meridian

Geographic Coordinates ( , z) Latitude (  ) and Longitude ( ) defined using an ellipsoid, an ellipse rotated about an axis Elevation (z) defined using geoid, a surface of constant gravitational potential Earth datums define standard values of the ellipsoid and geoid 


 Geodesy and Map Projections Geodesy - the shape of the earth and definition of earth datums Map Projection - the transformation of a curved earth to a flat map Coordinate systems - (x,y) coordinate systems for map data 


Geodesy - The science of determining the size and shape of the earth and the precise location of points on its surface.
Map Projection - the transformation of a curved earth to a flat map.
Coordinate systems – Any set of numbers, usually in sets of two or three, used to determine location relative to other locations in two or three dimensions

Mean Sea Level is a surface of constant gravitational potential called the Geoid. Since the Geoid varies due to local anomalies, we must approximate it with a ellipsoid


Types of Coordinate Systems
(1) Global Cartesian coordinates (x,y,z): A system for the whole earth
(2) Geographic coordinates (f, l, z)
Latitude (f) and Longitude (l) defined using an ellipsoid, an ellipse rotated about an axis
Elevation (z) defined using geoid, a surface of constant gravitational potential
Earth datums define standard baseline values of the ellipsoid and geoid



(3) Projected coordinates (x, y, z) on a local area of the earth’s surface
The z-coordinate in (1) and (3) is defined geometrically; in (2) the z-coordinate is defined gravitationally


## Misc
**How do you test the accuracy of satnav systems?**
Misra said, "Academic institutions have been roped in to do ground verification and calibrate data of NavIC to find its accuracy. We have developed digital chips to miniaturise technology (for use in mobiles and handsets) and experiments are on them. The system is being tested all across the country." He said, "After the desi navigation system comes to market, big thing will be to popularise it (as American GPS dominates the navigation system market across the world)."

Explaining the scientific reasons for NavIC's superiority over GPS, Misra said, "Our system has dual frequency (S and L bands). GPS is dependent only on L band. When low frequency signal travels through atmosphere, its velocity changes due to atmospheric disturbances. US banks on atmospheric model to assess frequency error and it has to update this model from time to time to assess the exact error. In India's case, we measure the difference in delay of dual frequency (S and L bands) and can assess the actual delay. Therefore NavIC is not dependent on any model to find the frequency error and is more accurate than GPS."

It will aid terrestrial, aerial and marine navigation, vehicle tracking and fleet management, disaster management, mapping and geodetic data capture, visual and voice navigation for drivers. The service can also be integrated with mobile phones and can be a navigation tool for hikers and travellers. The restricted service will also be used by the military for missile delivery and navigation and tracking of aircraft. In fact, the IAF has already started moving in this direction and made receivers for using the indigenous GPS.

"Poor the accuracy of these atomic clocks, less the accuracy of the distance calculated. For the navigation system, minimum of four satellites are needed, but we already have seven satellites in place. Therefore, Isro will give less weightage to the satellite whose atomic clocks have stopped working and depend on the data from other satellites. Therefore, the overall performance will not get affected."

The clocks of both IRNSS and GALILEO were supplied by SpectraTime.[34][35] ISRO replaced the atomic clocks in two standby NavIC satellites.[8] The setback comes at a time when IRNSS is yet to start commercial operations.


A satellite navigation or "satnav" system is a system of satellites that provide autonomous geo-spatial positioning with global coverage and allow small electronic receivers to determine location (longitude, latitude, and altitude/elevation) using time signals transmitted along a line of sight by radio from satellites. Often times the terms "GNSS" and "GPS" are used interchangeably but there are key differences between the two and solutions for each specific satelite system are available from Telit Wireless Solutions.

## Keywords
* DOP - Dilution of Precision - Geometry of the satellite constellation is evaluated by DOP
* Continuously Operating Reference Stations (CORS) or VLBI
* Precise Positioning Service (PPS)


## References
* https://www.asprs.org/wp-content/uploads/pers/1992journal/jun/1992_jun_835-841.pdf
* http://www.igic.org/resources/standards/map-scale-accuracy/
* http://desktop.arcgis.com/en/arcmap/latest/extensions/data-reviewer/what-is-positional-accuracy-assessment.htm
* http://biondsoftware.com/indiamap.html
* https://en.wikipedia.org/wiki/Total_station
* https://www.fgdc.gov/standards/projects/FGDC-standards-projects/accuracy/part1/chapter1
* https://en.wikipedia.org/wiki/GLONASS
* http://www.gps.gov/systems/gps/performance/accuracy/
* http://wiki.openstreetmap.org/wiki/Accuracy_of_GPS_data
* https://en.wikipedia.org/wiki/Accuracy_and_precision
* https://en.wikipedia.org/wiki/Satellite_navigation
* http://slideplayer.com/slide/5231948/
* https://www.slideshare.net/darpandodiya/gps-global-positioning-system-introduction-history-working-applications
* https://beebom.com/what-is-glonass-and-how-it-is-different-from-gps/
* https://thewire.in/19892/irnss-indias-very-own-gps/
* https://www.hautehorlogerie.org/fr/encyclopedie/lexique-de-lhorlogerie/s/atomique-horloge/
* https://en.wikipedia.org/wiki/Global_Positioning_System
* http://timesofindia.indiatimes.com/home/science/How-Kargil-spurred-India-to-design-own-GPS/articleshow/33254691.cms
* https://en.wikipedia.org/wiki/Indian_Regional_Navigation_Satellite_System
* http://www.insidegnss.com/
* http://www.semiconductorstore.com/blog/2015/What-is-the-Difference-Between-GNSS-and-GPS/1550
* https://en.wikipedia.org/wiki/GNSS_applications
* http://www.gnss.asia/japan
* https://en.wikipedia.org/wiki/World_Geodetic_System
* https://en.wikipedia.org/wiki/Geocaching

### Technical Bits
* https://research.google.com/pubs/jeff.html
* https://research.google.com/pubs/SanjayGhemawat.html
* http://archive.indianexpress.com/news/why-time-will-stop/404201/0
* http://www.nplindia.in/node/1869