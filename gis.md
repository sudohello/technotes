---
Title: GIS
Decription: GIS
Author: Bhaskar Mangal
Date: 
Last Updated: 06-Jul-2018
Tags: GIS
---

**Table of Contents**
* TOC
{:toc}


## GIS

## GIS Foundations
* [Open Source Geospatial Foundation](https://www.osgeo.org/)

## Online Data Converter
* https://mygeodata.cloud/result
> best online convertor so far
* https://geoconverter.hsr.ch/

## Online viewers, tools, apis
* http://www.geoapi.org/
* https://www.geomatys.com/en/home/
* http://geojsonlint.com/
* http://mapshaper.org/
* http://geojsonlint.com/
* https://www.osgeo.org/projects/gvsig/

### Mapbox GL Viewer
https://bl.ocks.org/fxi/b7f1af5981432296bfafec70a95fd9b6

### KML Viewer
http://kmlviewer.nsspot.net/	

## Elevation Profiling

SRTM, GMTED, NED and ETOPO1 DEMs

### SRTM Topography
- https://en.wikipedia.org/wiki/Interferometric_synthetic-aperture_radar

https://www2.jpl.nasa.gov/srtm/index.html
- https://dds.cr.usgs.gov/srtm/version2_1/Documentation/SRTM_Topo.pdf
- https://dds.cr.usgs.gov/srtm/version2_1/Documentation/Quickstart.pdf

**Download**
http://earthexplorer.usgs.gov/


NASA released elevation data generated from NASA’s Shuttle Radar Topography Mission digital topographic data.
We can use the data freely. Elevation data version 2.1 can be downloaded from the distribution site.
Download a zip file that contains elevation data of the area you are interested in from under the version2_1/SRTM3
directory. The zip file contains a .hgt file, which is readable by the GDAL.

**RADAR INTERFEROMETRY**
www.its.caltech.edu/~ee157/lecture_note/Radar.pdf

### Mapzen
https://mapzen.com/documentation/elevation/elevation-service

Currently, the underlying data sources for the service are a mix of SRTM, GMTED, NED and ETOPO1 DEMs. These sets provide global coverage at varying resolutions up to approximately 10 meters. It should be noted that both SRTM and GMTED fill oceans and other bodies of water with a value of zero to indicate mean sea level; in these areas, ETOPO1 provides bathymetry (as well as in regions which are not covered by NED, SRTM and GMTED). Many other classical DEM-related issues occur in these datasets. It is not uncommon to see large variations in elevation in areas with large buildings and other such structures. Mapzen is considering how to best integrate other sources such as NRCAN and is always looking for better datasets. If you find any data issues or can suggest any supplemental open datasets, please add an issue in this GitHub repository.


## Scale

**Map Scales**
* Verbal
	- one inch equal (represents) to 63,360 inches
* Representative Fraction - RF
	- Expressed as a ratio in the same units
	- 1:2,000 means that one inch (or one meter) on the map represents 2,000 inches (or meters) on the ground
* Graphic Scale - Bar
	- The graphic bar places visual measure of ground distances on the map

**Scale Defines:**
- precision of the location
- level of details
- what features are shown
- how features are shown

**Samell Scale**
- ex => 1:250000
- large area coverage on map

**Large Scale**
- ex => 1:10000
- small area coverage on map

**Types of scale**
>(with common operations)

* Nominal
	- frequency
	- aggregate
* Ordinal
	- median
	- percentile
* Interval
	- airthmatic mean
	- standard deviation
	- correlation and regression analysis
* Ratio
	- all matematical operations with real numbers


	WMS, WFS, WCS	

	WMS (Web Map Service) WFS (Web Feature Service) WCS (Web Coverage Service)
1.GetCapabilities:
Request metadata about the
service 1. GetCapabilities:
Request metadata about the
service 1. GetCapabilities:
Returns service-level metadata
and a brief description of the
data collection
2.GetMap:
Request a map image 2. DescribeFeatureType:
Request Feature type
information 2. DescribeCoverage:
Returns a full description of one
or more coverages.
3. GetFeatureInfo (optional):
Request information about
features in the map 3. GetCoverage:
3. GetFeature:
Request GML-encoded features Return coverage in a well-
known coverage format.
from the WFS service


OGC Standard Format for spatial data:
- WKT, WKB, GML (2004), KML (2008)

SRID - Spatial Reference ID
- SRID defines the coordinate system and datum
- Operation between object require them to have same SRID
- SRID for geography is 4326 (also referred to as WGS84)
- Default SRID for geometry is 0

++Spatial Features++
**Types of Objects**
- points (0-D)
- lines (1-D)
- area (2-D)
- surfaces
- volumes (3-D)

## GIS Courses

## MIT Open GIS
https://libguides.mit.edu/gis/tutorials

### iihs - working-with-gis
- http://iihs.co.in/working-with-gis/

 * Learners will gain an understanding of geospatial tools techniques and their applications
 hands-on experience with GIS open source software.
 * Learners will be equipped with skills for:
	 - data acquisition
	 - data creation
	 - map digitization
	 - conducting analysis to visualize geospatial information
	 - communicate effectively with maps

	 Professionals – INR 9000/-
Students – INR 6500/-

Discounted Price for Professionals – INR 7000/-
Discounted Price for Students – INR 5000/-

For further details contact Prashanth on +91 98849 51580 / prashanthc@iihs.ac.in

### iitd - gislab
* http://gisserver.civil.iitd.ac.in/gislab/

## TUtorials
http://duspviz.mit.edu/tutorials/geocoding/

## Basics
**Coordinate system**

Coordinates reference systems, geoids, latitudes and longitudes, projections, datums, ellipsoids

- http://gisgeography.com/latitude-longitude-coordinates/
- http://gisgeography.com/vertical-datum/
- http://gisgeography.com/horizontal-datum/

A geographic coordinate system defines three-dimensional coordinates based on the Earth’s surface. It contains an angular unit of measure, prime meridian and datum (which contains the spheroid).

Longitudes: X-coordinates are between -180 and +180, which are called longitudes.
Latitudes: Y-values are between -90 and +90 degrees, which are called latitudes.

**What is a Horizontal Datum?**
A datum describes the shape of the Earth. In mathematical terms, it defines the radius, major and minor axis and flattening for an ellipsoid.

- latitudes and longitude positions (Geographic Coordinate Systems) are based on a spheroid or ellipsoid surfaces that approximate the surface of the earth – a datum.
- Datums are used in projections, monitoring the Earth’s crust, survey boundary delineation and more. All coordinates are referenced to a datum
- A datum defines the radius, inverse flattening, semi-major axis and semi-minor axis for an ellipsoid.
WGS84 datum:

Semi-major axis: 6,378,137.0m
Semi-minor axis: 6,356,752.3m
Inverse flattening: 294.978698214

**What is a Vertical Datum?**
We need a consistent starting point to compare flood and ground elevations. Enter the vertical datum.

vertical datum as a surface of zero elevation to which heights can be referred to.

++Tidal Datums vs Vertical Geodetic Datums++
**Tidal datums** reflect the interface between water and land and is defined by the tidal variation. 

**A Verical Geodetic datum** is a reference surface of zero elevation to which heights are referred to over a large geographic extent
- These datums are used to measure height (altitude) and depth (depression) above and below mean sea level.
-  A geodetic datum reference might use a tidal datum as a start point.


Orthometric – This height represents the distance between the Earth surface and geoid at a specific point. Surveyors usually refer to orthometric heights. When you take the height at the peak of a mountain. It’s an orthometric height measured as a distance between the surface and the geoid.

The Geoid – The geoid coincides with mean sea level as if you are imagining it as an extension under (or over) land areas. The geoid is an equipotential surface at which gravity is normal – closely approximating mean sea level. This is because of the varying densities that are present in the Earth at different places. There are gravity anomalies with undulations differing from place-to-place.

Land and mountains prevent us from the seeing the geoid surface on the Earth. The Earth’s interior differs in density everywhere. This means that gravity varies everywhere on the Earth. This is why we measure gravity or the gravitational equipotential surface. We can then infer that this is how water would settle and model it mathematically. The geoid then gives a true zero surface for measuring elevations.

Reference Ellipsoid – The reference ellipsoid is a mathematical model of the shape of the Earth with the major axis along the equatorial radius. It approximates the geoid, but mostly coincides with geodetic network computations which point coordinates (latitude and longitude) are referred to.


 A highly accurate surveying technique called geodetic leveling was used to measure height differences across the country. 


If we say that flood waters will rise 25 feet, what exactly is “25 feet” referenced to? We need a consistent starting point to compare flood and ground elevations. This is why consistent vertical datums and mean sea level are so important. Effective floodplain management depends on accurate surveying.

To handle the ups-and-downs, we have the vertical datum which gives a place to put the zero measurement with mean sea level as the basis for our ups-and-downs. This is called the geoid.

## Opensource GIS Tools

http://gisgeography.com/free-gis-software/
http://wgbis.ces.iisc.ernet.in/foss/index.php?option=com_content&task=view&id=28&Itemid=52

1. [QGIS – Formerly Quantum GIS](http://qgis.org/)
-	Automate map production, process geospatial data, and generate drool-worthy cartographic figures.
map like a rock star
- [Semi-automatic Classification Plugin (SCP)](https://fromgistors.blogspot.com/)
- [dzetsaka : Classification tool](https://github.com/lennepkade/dzetsaka/)

2. [gVSIG](http://www.gvsig.com/en)
- The CAD tools are impressive on gvSIG. Thanks to the OpenCAD Tools, you can trace geometries, edit vertices, snap and split lines and polygons.
- users can perform supervised classification, band algebra and decision trees.
3. Whitebox GAT
swiss-army knife of [LiDAR data](http://gisgeography.com/top-6-free-lidar-data-sources/)
4. [SAGA GIS](http://www.saga-gis.org/)
- SAGA GIS (System for Automated Geoscientific Analyses)
- lifesaver in terrain analysis
- If you have a DEM, and don’t know what to do with it – you NEED to look at SAGA GIS
- SAGA GIS a prime choice for environmental modeling and other applications
- Ideal for most remote sensing needs because of its rich library grid, imagery and terrain processing modules
- analyses and manipulation, it flourishes with terrain tools like TPI, TWI and soil classification. It also has some rudimentary tools for photogrammetry and support vector machine (SVM).
5. [GRASS GIS](https://grass.osgeo.org/)
- (Geographic Resources Analysis Support System)
- option for analysis, image processing, digital terrain manipulation and statistics.
- it offers image classification, PCA, edge detection, radiometric corrections, 3D, geostatistics analysis and filtering options
- key feature of GRASS is the LiDAR processing and analysis. You can filter LiDAR points, create contours and generate DEMs
6. [MapWindow](http://www.mapwindow.org/)
- OS: MS Windows
- you can do GIS without the dependency of commercial GIS software.
7. [ILWIS](http://52north.org/communities/ilwis)
- OS: MS Windows
- Integrated Land and Water Information Management
- digitizing, editing, displaying geographic data
- for planners, biologists, water managers and geospatial users.
-  also used for remote sensing with tools for image classification, enhancements and spectral band 
manipulation
- It is equipped with stereoscopy and anaglyph tools to create stereo pairs from two aerial photographs
- if you have satellite data, ILWIS has image classification techniques to create land cover classes
8. [GeoDa](https://geodacenter.asu.edu/software/downloads)
- used to introduce new users into spatial data analysis
- main functionality is geostatistics.
- used in a range of areas such as economic development health and real estate.
- http://geodacenter.github.io/
9. [uDig](http://udig.refractions.net/)
- option for basic mapping.
10. [OpenJump](http://www.openjump.org/)
- more complete free GIS software package.
11. [Diva GIS](http://www.diva-gis.org/)
- OS: MS Windows
- specializes in mapping biological richness and diversity distribution including DNA data.
- possible to extract climate data for all locations on the land.
12. [FalconView]
- it can be used for combat flight planning
- In SkyView mode, you can fly-through even using MXD files.
- It supports various types of display like elevation, satellite, LiDAR, KMZ and MrSID.
13. [OrbisGIS](http://www.orbisgis.org/)
14. [TerraLib](http://www.terralib.org/)

## Data Collection

Collector for ArcGIS
Fulcrum Data Collector
QField Experimental (Not sure if Apple compatible)

## open source remote sensing software
- http://gisgeography.com/open-source-remote-sensing-software-packages/

Satellite and aerial imagery provides answers for environmental change, weather forecasting, disaster management, food security and other remote sensing applications. Remote sensing software processes images and provides solutions to local or global issues.


This open source remote sensing software list fills a wide range of disciplines like photogrammetry, OBIA, LiDAR, SAR and more.

- http://www.sensum-project.eu/remote-sensing-tool

- open satellite data
- [ORFEO Toolbox (OTB): Optical and Radar Federated Earth Observation](http://orfeo-toolbox.org/)
	- https://www.orfeo-toolbox.org/CookBook/Installation.html#linux-64bit
- [PolSARPro](https://earth.esa.int/web/polsarpro)
- [InterImage](http://www.lvc.ele.puc-rio.br/projects/interimage/)
	- It specializes in automatic image interpretation, which is pretty neat.
- [OSSIM](https://trac.osgeo.org/ossim/)
	- high performance open source remote sensing software application
	- https://github.com/ossimlabs/ossim
- **[E-foto](http://www.efoto.eng.uerj.br/en)**
	- digital photogrammetry specialist
	- The core functionality is photo triangulation, stereoscopic modeling, digital elevation model extraction and terrain correction.
- [SNAP/NEST](http://step.esa.int/main/)
	- great for processing synthetic aperture radar data
	- http://step.esa.int/downloads/5.0/installers/esa-snap_all_unix_5_0.sh

### 3D GIS

**open-source-gis-software-3d-map**
- http://grindgis.com/blog/open-source-gis-software-3d-map

1. QGIS (QGIS2Threejs)
- http://qgis2threejs.readthedocs.io/en/docs-release/Tutorial.html
In GIS world 3D means that has X, Y and Z coordinates. Z coordinate is used to draw height. 3D map helps better understanding of the object, in GIS 3D map might be  TIN image, Digital Elevation Model or any GIS layer with elevation values. To plot these GIS layer with Z value or TIN image or DEM data you need a special kind of GIS software. So here are few 3D free GIS software that will help you create and visualize your 3D data.

**GIS 3D map might be**
- TIN image
- Digital Elevation Model (DEM)
- any GIS layer with elevation values.

2. GRASS GIS
- also runs in QGIS by using plugins
- capability of displaying 3D or 4D images
- also support the voxel

3. Blender

Blender: Blender is another opens source 3D graphics software which is used for creating animation movies, visual effects, art, 3D prints and many more. Some of the 3D GIS processing can be achieved using Blender such as building Terrain model, 3D airphoto and more. You can also create shaded relief map on Blender, here is step by step tutorial. QGIS can be used heavily to create a terrain model, here is a video tutorial using QGIS and Blender to create Terrain model. There are numbers of GIS add ons for blender, Addons collection.


- http://gislab.dirap.unipa.it/prin2007.html

## Image Classification in GIS
- http://gisgeography.com/image-classification-techniques-remote-sensing/

[bit depth](http://gisgeography.com/bit-depth/)
http://gisgeography.com/rasterization-vectorization/


## Vectorize Image Files Automatically
http://gisgeography.com/how-to-vectorize-image-arcscan/
- Esri’s ArcScan
- Autodesk Raster-to-Vector Conversion
- Trimble Ecognition
- QGIS Edge Extraction

## Inspirations
- http://storymaps.arcgis.com/en/

## Blogs to Follow

* [gisgeography.com](http://gisgeography.com)
**Topics to Read**
http://gisgeography.com/georeferencing/

## Indoor Mapping
- https://stackoverflow.com/questions/44213925/how-to-use-leaflet-indoor-plugin-and-draggble-object-in-leaflet-1-0-3
- https://github.com/wrld3d/wrld-indoor-maps-api/blob/master/TUTORIAL.md

## Mapbox Layer
https://www.mapbox.com/help/mapbox-arcgis-qgis/


## Terrain Cartography
- https://en.wikipedia.org/wiki/Terrain_cartography
- https://en.wikipedia.org/wiki/Terrain
- https://en.wikipedia.org/wiki/Terrain_rendering

Terrain or relief is an essential aspect of physical geography, and as such its portrayal presents a central problem in cartography, and more recently GIS and geovisualization.

**Terrain or relief**
- Terrain or relief (also topographical relief) involves the vertical and horizontal dimensions of land surface.
- This is usually expressed in terms of the elevation, slope, and orientation of terrain features.
- Terrain affects surface water flow and distribution. Over a large area, it can affect weather and climate patterns.

**Topographic Map**
- https://en.wikipedia.org/wiki/Topographic_map
- a topographic map is a type of map characterized by large-scale detail and quantitative representation of relief, usually using contour lines, but historically using a variety of methods.
- A contour line is a line connecting places of equal elevation.

**Topography**
- https://en.wikipedia.org/wiki/Topography
- It is the study of the shape and features of the surface
- The topography of an area could refer to the surface shapes and features themselves, or a description (especially their depiction in maps).

### Different ways to Model Elevation
- http://gisgeography.com/dem-dsm-dtm-differences/

#### GIS elevation models - Types of DEM
- https://en.wikipedia.org/wiki/Digital_elevation_model

A digital elevation model (DEM) is a digital model or 3D representation of a terrain's surface — commonly for a planet (including Earth), moon, or asteroid — created from terrain elevation data.

* DEM - digital elevation model
	- DEM is often used as a generic term for DSMs and DTMs, only representing height information without any further definition about the surface.
	- Often used Interchangable with DTM
* DTM - digital terrain model
	- DTM represents the bare ground surface without any objects like plants and buildings
	- A digital elevation model is a bare-earth raster grid referenced to a vertical datum. When you filter out non-ground points such as bridges and roads, you get a smooth digital elevation model. The built (powerlines, buildings and towers) and natural (trees and other types of vegetation) aren’t included in a DEM.
	- In some countries, a DTM is actually synonymous with a DEM
	- bare-earth elevation model is particularly useful in
		* hydrology
			-  Hydrologists use DEMs to delineate watersheds, calculate flow accumulation and flow direction.
		* soil mapping
			- DEMs assist in mapping soils which is a function of elevation (as well as geology, time and climate).
		* land use planning
			- Terrain stability - Areas prone to avalanches are high slope areas with sparse vegetation. This is useful when planning a highway or residential subdivision.
* DSM - digital surface model
	- DSM represents the earth's surface and includes all objects on it.
	- Because objects extrude from the Earth useful in 3D modeling for:
		* telecommunications
		* urban planning
			- Urban planners use DSM to check how a proposed building would affect the viewshed of residents and businesses.
			- Along a transmission line, DSMs can see where and how much vegetation is encroaching
		* Aviation
			- DSMs can determine runway obstructions in the approach zone
	- 

#### TIN - triangulated irregular network
	- https://en.wikipedia.org/wiki/Triangulated_irregular_network
	- TIN is a representation of a continuous surface consisting entirely of triangular facets
	> TIN overlaid with contour lines
	[!Alt](images/gis/Digitales_Geländemodell.png)

#### Contours
	- https://en.wikipedia.org/wiki/Contour_line
	- **Contour Lines**
		- A contour line (also isoline, isopleth, isarithm, or equipotential curve) of a function of two variables is a curve along which the function has a constant value, so that the curve joins points of equal value
		- a contour line for a function of two variables is a curve connecting points where the function has the same particular value
		- The gradient of the function is always perpendicular to the contour lines
		- When the lines are close together the magnitude of the gradient is large: the variation is steep
		- slope, pits and peaks
	- **Contour Map**
		- It is a map illustrated with contour lines, for example a topographic map, which thus shows valleys and hills, and the steepness or gentleness of slopes.[4] The contour interval of a contour map is the difference in elevation between successive contour lines.
		- The configuration of these contours allows map readers to infer relative gradient of a parameter and estimate that parameter at specific places


## Civil Survey

**Cadastral Survey**
- https://en.wikipedia.org/wiki/Cadastral_survey
- A cadastre (also spelled cadaster), using a cadastral survey or cadastral map, is a comprehensive register of the real estate or real property's metes-and-bounds of a country

* https://earth.esa.int/web/guest/home
* https://www.mapbox.com/mapbox-gl-js/example/third-party/


## Footprint Extration 
- http://www.charim.net/use/74

* ML, Image Processing
	- https://gis.stackexchange.com/questions/247000/extracting-building-footprints-from-sentinel-2-imagery
	- http://www.rasor.eu/wiki/index.php/RASOR_QGIS_plugins
	- https://medium.com/the-downlinq/object-detection-on-spacenet-5e691961d257
	- https://aws.amazon.com/public-datasets/spacenet/

- http://www.ierek.com/news/index.php/2016/08/08/can-mix-urban-planning-remote-sensing-make-future/

## qGIS plugins
* http://www.qgistutorials.com/en/docs/using_gme_connector.html
* https://research.csc.fi/open-gis-data

**Removing Silver Polygons**
* https://gis.stackexchange.com/questions/11004/removing-small-spaces-slivers-between-polygons
* https://github.com/ptabriz/Geovisualization-with-Blender
* https://blenderartists.org/
* https://github.com/domlysz/BlenderGIS

Alignment of continuous video onto 3D point clouds.
[Unreal Engine 4: Point Cloud processing](https://www.youtube.com/watch?v=NvKF5Sv5qpk)

## Webtools
* [mapshaper.org](https://mapshaper.org/)

## GTFS - General Transit Feed Specification
* https://developers.google.com/transit/gtfs/
* https://en.wikipedia.org/wiki/General_Transit_Feed_Specification
* https://www.conveyal.com/

The General Transit Feed Specification (GTFS) defines a common format for public transportation schedules and associated geographic information.

### Multimodal Transportation
* https://en.wikipedia.org/wiki/Multimodal_transport
Multimodal transport (also known as combined transport) is the transportation of goods under a single contract, but performed with at least two different means of transport; the carrier is liable (in a legal sense) for the entire carriage, even though it is performed by several different modes of transport (by rail, sea and road, for example). The carrier does not have to possess all the means of transport, and in practice usually does not; the carriage is often performed by sub-carriers (referred to in legal language as "actual carriers"). The carrier responsible for the entire carriage is referred to as a multimodal transport operator, or MTO.

**opentripplanner**
* http://www.opentripplanner.org/
* https://github.com/opentripplanner/OpenTripPlanner

### Journey Planner
* https://en.wikipedia.org/wiki/Journey_planner

Trip planning or Journey planning is sometimes distinguished from route planning,[4] where route planning is typically thought of as using private modes of transportation such as driving, walking, or cycling, normally using a single mode at a time.

Trip or Journey planning by contrast would make use of at least one public transport mode which operates according to published schedules; given that public transport services only depart at specific times (unlike private transport which may leave at any time), an algorithm must therefore not only find a path to a destination, but seek to optimise it so as to minimise the waiting time incurred for each leg.

A journey planner, trip planner, or route planner is a specialised search engine used to find an optimal means of travelling between two or more given locations, sometimes using more than one transport mode

Searches may be optimised on different criteria, for example fastest, shortest, least changes, cheapest.
They may be constrained for example to leave or arrive at a certain time, to avoid certain waypoints, etc.

A single journey may use a sequence of several modes of transport, meaning that the system may know about public transport services as well as transport networks for private transportation.

## Weather API
* https://wxtiles.com/pricing/
* https://api.weather.com/v3/TileServer/tile/cloudsFcst?ts=1522297800&xyz=11722:7597:14&apiKey=8191cad7cb99410f91cad7cb99110fc6
* http://openweathermap.org/api
* https://www.weatherbug.com

### Pricing
* http://openweathermap.org/price

## Mapbox API
* https://www.mapbox.com/api-documentation/
* https://www.mapbox.com/blog/tags/weather/

## AR - Augmented Reality with location based applications
* https://blog.mapbox.com/mapbox-ar-2f065374eacb


## Reference
* http://spatialreference.org/

## GIS Formats
https://gisgeography.com/gis-formats/

## Tricks

* polygon to centerline
- skeleton algorithm

* https://www.udcus.com/blog/2017/06/28/creating-centerlines-postgis-and-arcgis
* https://gis.stackexchange.com/questions/114541/extracting-centerline-of-a-complex-polygon-in-postgis-python/203928
* https://gis.stackexchange.com/questions/290805/is-it-possible-to-convert-polygon-to-centerline-linestring
* https://lists.osgeo.org/pipermail/postgis-users/2008-January/018215.html

**FME for cesium 3D tiler.**
* https://knowledge.safe.com/questions/55696/converting-from-geojson-to-cesium-3d-tiles.html
* https://www.safe.com/integrate/cesium-3d-tiles/


**HD Vector Maps**
* echopiatech.com
* https://www.thasler.com/blog/


## Post-gis
* http://www.postgis.us/


## [SOTMA - State Of The Map Asia](https://stateofthemap.asia/): **2018**

### **1st Day**
* Pukar
	- sarkar - bazar - janta
	- govt - private - people
	- private ltd + social org -> social policy impact=>govt
	* Mapping provides visibility in social issues, helps in stakeholder management; impact policy changes and execution
	* Addressing encoding scheme: dharavi
* Strategies to handle community building and sustenance:
	- After reaction -> follow-up, people development, knowledge transfer, mapathons, handover to built community, exit strategy
	- university involvement
	- developing graduate students participation
	- youth involvement
	- internship programme: 4 days intense training, 2-3 months
* some osm tools used for village mapping:
	- GPX loggers, OSM Trackers
* kerala flood disaster management
	- people sending 'SOS message with geo-location'
	- `https://process.keralarescue.in/`
	- `https://keralarescue.in/map/`
* Some keywords:
	* HOT - Humanitarian OpenStreetMap Team
	* sensinglocal
	* PTWebEditor
	* OpenMapTIles
	* Native language mapping
	* OpenData Collect
	* OpenMapKit
	* OpenGeoData
	* `petabencana.id/map/jakarta`
	* `secondarycities.state.gov`
	* `katmandulivinglabs.org`
	* wikimedia maps, wikidata, wikipedia
		* no wikimedia mpas dedicated team
		* `#opendata`
		* gov data portal: `data.gov.in`
		* not many volunteers to add data to osm
		* Level 0 openstreetmap editor
		* osm:
			- no standard way how rivers are added: as a line, shape
			- CC0 licesnsing
			- vandalism
		* HOTOSM Tasks
	* OSM allows commercialisation
	* NRSC


**Thoughts and Ideas**
* TBD: connect: pukar+goonj
* some social issues:
	- water consumption
	- waste generation & management
	- open and green spaces
	- consumption patterns
	- logistics
	- farmers suicide
	* osm-d (osm-data): open geo-analytics
	* crowd-sourcing ma creation: people participation, monetisation benefit for contributors
	* CSR: contribution to osm during natural disaster, eg: facebook during kerala floods
	* Digital Charity: donating geo-data to osm


### **2nd Day**
**Business of Geospatial Data in Asia**
* Maps are never done! (forever...)
* time to respond rather the perfect, accurate map
* everyone will create their own dataset
* landmark distortion
	- in-accurate cadastral data
	- leading to land acquisitions
* yahoo opendata: `webscope data`
* good amount of effort data scrubbing, engineering, regulartory, legal, disambiguity
	- to figure out data company can give back; at the same time protect business, customers v/s opendata
	- company ownership gives sense of security, protection - bring trust wrt data
	- get interns to work on the data and publish their works
* West, European Geodata V/s India, Asian countries Geodata
	* structured vs unstructured
	* policies vs no policies
		- example: rules when two vechiles are approaching each other in perpendicular directions, who goes first 
	* predictive vs unpredictive
	* batch, solid state vs highly dynamic, fluid, requirement of more realtime data
* Big Data problem in GIS
	- sources, shapes; Volume; Velocity
* Huge gap: Development to release gap
	- realtime
	- more latency batch process
* [veditum.org](https://www.veditum.org/)
* **Visualizing Flood Propogation with OSM and DEM**
	- https://github.com/pratapvardhan
* **How to bring Veracity, Trust (trust, conformity to facts, accuracy)?**
	* Use AI - get evidences, AI not yet completely reliable
	* build redundancy for veracity
	* Traditional go & collect
	*  Grab:
		- Grab-NUS AI Lab
			* using to cut travel time in city traffic
	*  Accenture:
		- some GIS data -> what kind of <xxx>
		- Used AI in Computer Vision to audit and replace `telecom poles`
* Geospatial media commnication - stats and survey
	* Geospatial regulation bill in 2016 -> put to cold storage
* mapping of auroville
	* geomatic studioportal (gisaf)
	* python:
		- is swiff army knief to glue heterogenous pieces
		- aiohttp, geopandas (also for generating map)
		- gdal (osgeo)
		- Folium (leaflet)
		- JupyterLab
	* [https://gis.auroville.org.in/dashboard](https://gis.auroville.org.in/dashboard)


**Working with OSM Map and Data**
* [taginfo](https://taginfo.openstreetmap.org/)
* [hotosm](https://www.hotosm.org/)
* https://www.openstreetmap.org/
	- three geometryies: poin, line, ploygon -> object/feature
		* https://mapschool.io/img/vector_types.png
	- each feature, many key-value
		* https://wiki.openstreetmap.org/wiki/Map_Features
		* anyone can add any-key value pair, nobody stops you but be responsible
	- osm editing
		* https://www.openstreetmap.org/edit
* https://mapschool.io/
* OSM - free and open, without legal and technical resitrictions
	- ODbl: share-aline, attribute, keep-open

**Extract data:**
* what can be extracted:
	* taginfo, map_features
	* key-value pair: `amenity=atm`, `highway=residential`
	* tags never separated by spaces but underscors
* overpass API
	* http://overpass-turbo.eu/
	* queries:
	```javascript
	name=traffic_sign
	amenity=hospital
	amenity=hospital and "building:levels"=*
	amenity=hospital and (phone=* or email=*)
	## query in "<polygon_name>"
	amenity=hospital and building=hospital in "karnataka, India"
	#
	## regular expression is supported
	amenity=hospital and name~/[Ll]ife/
	## around something
	amenity=hospital around "IIMB"
	## Using `in` vs `around`
	```
	* nodes: yellow have geo-coordinates, red does not have
	* Mapcss: https://wiki.openstreetmap.org/wiki/MapCSS/0.1
	* Changing tile server
		- settings -> map
	* Download / Export data:
* Data format
	* node : a single point
	* way: an ordered list of nodes, polyline, plygon
	* relations: logical grouping of nodes and ways
* **OSM Bulk downloaders:**
	- http://export.hotosm.org/
	- http://download.bbbike.org/osm/
	- http://download.geofabrik.de/
	- http://www.geofabrik.de
	- http://umap.openstreetmap.fr/en/
* **Create Maps - `uMap`**
	- http://umap.openstreetmap.fr/en/map/new/#6/51.000/2.000
* https://github.com/poornibadrinath/workshops/tree/gh-pages/OSM-Session-CEPT


## Version Management of Geospatial Data


### [geogig](http://geogig.org)
- http://geogig.org/docs/start/installation.html#start-installation
- http://geogig.org/docs/start/tutorial.html




