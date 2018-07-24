/*
Title: QGIS
Decription: qGIS
Author: Bhaskar Mangal
Date: 
Tags: qGIS
*/

# qGIS

## Tools
* http://www.mapshaper.org
* http://geojson.io

## FAQs
- To get a bounding box in QGIS as a new vector layer:
Menu -> Vector -> Research Tools -> Polygon from layer extent

https://gis.stackexchange.com/questions/85192/qgis-get-extent-of-layer

- Convert data types

https://gist.github.com/YKCzoli/b7f5ff0e0f641faba0f47fa5d16c4d8d


## Loading Data
https://gis.stackexchange.com/questions/199403/loading-geojson-into-qgis

## Working with Terrain Data
http://www.qgistutorials.com/en/docs/working_with_terrain.html
http://qgis.spatialthoughts.com/2012/03/working-with-terrain-data-in-qgis.html
https://gis.stackexchange.com/questions/138060/how-to-effectively-merge-srtm-1-arc-data


## Tutorials
- http://www.sarahmakesmaps.com/blog/2016/3/mapping-jersey-city
- https://www.gislounge.com/a-web-mapping-tutorial-for-beginners/
- [open-source-qgis-review-guide](http://gisgeography.com/open-source-qgis-review-guide/)


### Saptial Analysis

#### Spatial Joins
- http://www.qgistutorials.com/en/docs/performing_spatial_joins.html

### How to build a 3D map of a city using QGIS and Mapbox
- http://www.storybench.org/build-3d-map-city-using-qgis-mapbox/

http://wiki.openstreetmap.org/wiki/QGIS

https://anitagraser.com/2014/03/15/3d-viz-with-qgis-three-js/
http://members.chello.at/~graser/Qgis2threejs/


http://aashrithaa.com/nemmadhi-township/
http://www.gokuldhamhousing.com/wp-content/uploads/2017/07/Gokuldham-Housing-Broucher.pdf
http://www.gokuldhamhousing.com/wp-content/uploads/2017/06/application-form.pdf

http://www.mca.gov.in/

http://www.mca.gov.in/mcafoportal/checkCompanyName.do

http://mscs.dac.gov.in/

http://mscs.dac.gov.in/Proposals/ALL_REG_MSCS.pdf


http://sahakara.kar.gov.in/Listofsocieties.html

http://mscs.dac.gov.in/UserRegistered.aspx


### Working with elevation data
https://qgis2threejs.readthedocs.io/en/docs-release/Tutorial.html

## 3D in QGis
- https://geogeek.xyz/download-qgis-3.html
- http://planet.qgis.org/planet/tag/3d/


CRS setting
Horizontal unit of SRTM data is degree, whereas vertical unit is meter. For appropriate visualization, you need to transform the DEM data to a projected CRS. QGIS can perform the CRS transformation on the fly.

So, let’s enable the On The Fly CRS transformation and change the map CRS to a projected CRS.

Click the CRS icon CRS status icon in the bottom-right corner of the window to open the project properties dialog. Activate the Enable 'on the fly' CRS transformation checkbox and then select a suitable CRS for the DEM extent. If you don’t know which CRS is best suited, select the Spherical Mercator projection (EPSG:3857), which is adopted by many web maps.


### DEM
http://qgis2threejs.readthedocs.io/en/docs-release/Tutorial.html

### Problem Statements

Build 3D map that represents
- the average price per square meter of every lot in <areaName>/<city>
a) Obtain shapefiles with the heights and geometries of the buildings/lots within your desired city
b) dataset with the properties for sale and their respective prices

The geometry of lots.
The number of floors of each building on these lots.
Go to www.properati.com.ar/data to obtain a dataset with information about all properties for sale.

A borough is a town that has its own government. It also can be a part of a big city that has powers of self-government. Manhattan is just one of the five boroughs that make up New York City

 total nursing home capacity for each borough, we can use the attribute Capacity which can join to the boundaries layer.


## To Follow
**Blogs**
- [Free and Open Source GIS Ramblings](https://anitagraser.com/)
> written by Anita Graser aka Underdark

**githubs**
- https://github.com/anitagraser/


## GIS Data sources
http://projects.datameet.org/indian_village_boundaries/

http://opengovernanceindia.org/nlyxmwe/bescom-summary-report


https://data.gov.in/keywords/gis
http://wgbis.ces.iisc.ernet.in/foss/index.php?option=com_content&task=view&id=28&Itemid=52
http://iihs.co.in/working-with-gis/
https://cis-india.org/openness/publications/ogd-report
http://www.osgeo.in/

http://wgbis.ces.iisc.ernet.in/energy/paper/osgeo_foss4g_grass/index.htm



https://blog.mapillary.com/update/2014/12/15/sfm-preview.html
https://github.com/mapillary/OpenSfM
https://blog.mapillary.com/update/2015/10/26/panorama-connections.html
https://blog.mapillary.com/update/2015/11/10/pointclouds.html
https://blog.mapillary.com/2016/01/05/how-mapillary-works-with-cities.html
https://d1ufht5lu1kgia.cloudfront.net/blog/navigation/reconstruction.html#file=data/iVioRpbW-oZa0issidL1tg/reconstruction.json.compressed&res=640&img=03PQphaD0hKxVSHwphmobg

https://fatfreeframework.com/3.6/home

**Links for some building heights data + ITPL high resolution images:**
https://en.wikipedia.org/wiki/List_of_tallest_buildings_in_Bangalore
https://www.emporis.com/city/100247/bangalore-india
http://www.ascendas-singbridge.com/our-properties/india/science-business-and-it-parks/International-Tech-Park-Bangalore

**Extras:**
https://www.quora.com/Why-are-there-no-regulations-like-FSI-or-minimum-distance-between-buildings-for-apartment-buildings-in-Bangalore
http://www.mybdasites.com/viewtopic.php?t=4086
https://content.magicbricks.com/property-news/all-you-need-to-know-about-floor-area-ratio/81918.html
https://en.wikipedia.org/wiki/Floor_area_ratio

**the number of floors for any site depends on following factors : **
1. FAR - Floor Area Ratio = Total Built up Area / Plot Area
2. Width of the Road
3. Size of the Plot
4. Total Height of the building constructed
5. SetBack Area

## Plugins
**Install from file**

Downloading release code
Download the code from here.
Extract from zip file.
Rename folder to QgisCartoDB.
Copy the plugin folder to $HOME/.qgis2/python/plugins/
Install the QGIS Plugin · gkudos/qgis-cartodb Wiki · GitHub
https://github.com/gkudos/qgis-cartodb/wiki/Install-the-QGIS-Plugin


##

- https://gis.stackexchange.com/questions/10117/clipping-raster-with-vector-boundaries-using-qgis
- www.geospatialPython.com


http://www.sensum-project.eu/remote-sensing-tool

## Mapbox Vector Tiles in qGIS
https://gis.stackexchange.com/questions/138512/add-vector-tile-sources-to-qgis


## qGIS Plugin
* ImportPhotos

Import Photos

This tool can be used to import Geo-Tagged photos (jpg or jpeg) as points to QGIS. The user is able to select a folder with photos and only the geo-tagged photos will be taken. Then a geoJSON point file will be created which will contain the name of the picture, its directory, the date and time taken, altitude, longitude, latitude, azimuth, north and camera maker and model. The plug-in doesn’t need any third party applications to work. It has two buttons; the one is to import geotagged photos, and the other one is to be able to click on a point and display the photo along with information regarding the date time and altitude. Mac users please refer to the Read Me file for further guidance.

* Instagram2qgis

Search and downloading Instagram images.

Search and downloading Instagram images and create a point shapefile with them.You need install some additional Python libraries:instagram,httplib2,requests,simplejson,six

* MagicWand

MagicWand

This plugin adds tools that help with photo-interpretation. For more details: https://github.com/GianlucaSilvestri/MagicWa


Open Aerial Map (OAM)

Open Aerial Map (OAM) client to upload, search, and download imagery and metadata

OpenAerialMap QGIS plugin allows QGIS users to communicate with various OAM services, acting as a desktop client for OAM. Through this plugin, users can upload, search, and download imagery, as well as create and edit OIN-conformed metadata in a simple way. It also supports some raster image processing such as reprojection and file format conversion, as well as triggering the creation of tile services.


## Setting up OSM
https://gis.stackexchange.com/questions/89503/collaborative-map-editing-using-local-openstreetmap-server
https://ircama.github.io/osm-carto-tutorials/tile-server-ubuntu/

## Editors
* geojson.io
https://www.datavizforall.org/transform/geojsonio/
https://github.com/mapbox/geojson.io


## Raster Image Processing
* http://www.qgistutorials.com/en/docs/raster_mosaicing_and_clipping.html
* https://spymesat.com/faq.html
* https://en.wikipedia.org/wiki/Satellite_imagery

There are four types of resolution when discussing satellite imagery in remote sensing:

Resolutions of Remote Sensing
1. Spatial (what area and how detailed)
spatial resolution is defined as the pixel size of an image representing the size of the surface area (i.e. m2) being measured on the ground, determined by the sensors' instantaneous field of view (IFOV);
2. Spectral (what colors – bands)
3. Temporal (time of day/season/year)
4. Radiometric (color depth)

imagery has been spatially rectified so that it will properly align with other data sets.

**What is spatial resolution in remote sensing?**
http://www.edc.uri.edu/nrs/classes/NRS409/RS/Lectures/HowRemoteSensonWork.pdf

**How do you measure spatial resolution?**
The measure of how closely lines can be resolved in an image is called spatial resolution, and it depends on properties of the system creating the image, not just the pixel resolution in pixels per inch (ppi). ... In effect, spatial resolution refers to the number of independent pixel values per unit length.

**spatial-resolution-of-google-earth-imagery**
https://gis.stackexchange.com/questions/11395/spatial-resolution-of-google-earth-imagery
http://www.landinfo.com/QuickBird.htm
https://www.researchgate.net/post/How_can_I_get_high_resolution_satellite_images
https://mysocialblade.blogspot.com/2018/06/how-satellite-capture-photos-through.html
http://learningweather.psu.edu/

QuickBird 60cm Global High-Resolution Satellite Imagery

Quickbird images are distributed by DigitalGlobe, so if they are not into the first site I cited it is difficult you can find any in the web. However often for research project DigitalGlobep rovided small images for free, so maybe it can be worth to try to contact them directly.
For AVIRIS see here: http://aviris.jpl.nasa.gov/data/free_data.html

Some link you can download satellite data
https://www.satimagingcorp.com/gallery/high-resolution/
https://www.researchgate.net/deref/http%3A%2F%2Fearthexplorer.usgs.gov
https://www.researchgate.net/deref/http%3A%2F%2Flandsat.usgs.gov%2FLandsat_Search_and_Download.php
http://www.digitalglobe.com/
http://landsat.usgs.gov/
http://bhuvan.nrsc.gov.in/data/download/index.php
http://www.satimagingcorp.com/
http://www.esa.int/Our_Activities/Observing_the_Earth
http://www.nrsa.gov.in/
http://glcf.umd.edu/data/
http://xtgeo.com/
http://www.nrsa.gov.in/
http://bhuvan.nrsc.gov.in/data/download/index.php
http://visibleearth.nasa.gov/
https://www.quora.com/Why-are-satellite-maps-of-USA-clearer-than-that-of-India-when-zoomed-to-street-level


In 2016,
Digitalglobe provide 30x30cm to 50x50cm satellite pictures. Pricing is around $18 per square kilometer. Minimum order is 25 km^2.
https://www.digitalglobe.com/

http://gisgeography.com/free-satellite-imagery-data-list/

There is an easy tool http://orbitalviews.eu/ which shows the most current Sentinel-2 picture of every searched location. You can switch to NDVI, Water Needs etc. ..There is also a live view which visualizes MODIS data.

https://www.youtube.com/watch?v=l6nitzE5rEg

My suggestion is to define first your task and after that look for data and software.
It also depends what you call high resolution. USGS provides data from MODIS and Landssat having coarse (500m) and middle (30m) spatial resolution. Other option for free high resolution imagery (1m, panchromatic) at no cost is also from USGS - Orbview sensor.
Some data suppliers such as DigitalGlobe might offer some data under educational initiatives, but you should communicate your request directly.



**How_can_i_create_a_Digital_Elevation_Model_from_satellite_Images**
https://www.researchgate.net/post/How_can_i_create_a_Digital_Elevation_Model_from_satellite_Images
If you have stereo pair of satellite images or overlapping aerial photographs or even UAV acquired imagery, you can use a standard GIS software to generate a DEM based on the principles of Photogrammetry. There are open source as well as commercially available softwares which can do the job. ERDAS Imagine LPS Suite, ENVI, ArcGIS, PCI Geomatica, NASA's Ames Stereo Pipeline, Pix4D, Drone2Map, etc. are some of the names in the business. The internet has made our lives much easier nowadays. It might be a good idea to google for 'dem generation with stereo' and you will get thousands of results.
Hope this gives you some hint. 
http://www.crisp.nus.edu.sg/~research/dem/dem.htm
https://ti.arc.nasa.gov/tech/asr/groups/intelligent-robotics/ngt/stereo/
https://www.youtube.com/watch?v=rDnWYh36d3c
https://www.youtube.com/watch?v=WoTZj77F08M
https://www.orfeo-toolbox.org/


There is a great free tool from IGN in France - MicMac. It allows you to generate DEM from all kind of source images. One of the great points is that it allows to generate DEM from uncalibrated cameras, e.g. from a UAV flight. have a look into http://logiciels.ign.fr/?Telechargement,20

The DEM Extraction Module requires a separate license.
A digital elevation model (DEM) is a regularly spaced raster grid of elevation values of a surface terrain. You can use DEMs to produce maps such as contour maps, orthophoto maps, and perspective maps. You can also use DEMS for route planning in the construction of highways and railways. In remote sensing, DEMs are used in mapping, orthorectification, and land classification.
The DEM Extraction Module enables you to extract elevation data from scanned or digital aerial photographs, or from an along track or an across track pushbroom satellite acquisition, such as those from the ALOS PRISM, ASTER, CARTOSAT-1, FORMOSAT-2, GeoEye-1, IKONOS, KOMPSAT-2, OrbView-3, QuickBird, RapidEye, SPOT, WorldView-1, WorldView-2, or Ziyuan-3A satellites. Along track stereo images are acquired on the same orbital pass by a satellite which usually has more than one sensor looking at the Earth from different angles. Across track stereo images are those taken by the same sensor on multiple orbits.
The DEM Extraction Module also supports Digital Point Positioning Data Base (DPPDB) data.
The DEM extraction process requires a stereo pair of images containing rational polynomial coefficients (RPC) positioning from aerial photography or pushbroom sensors. RPCs are used to generate tie points and to calculate the stereo image pair relationship. DEM extraction does not currently support replacement sensor model (RSM) positioning.
The DEM Extraction Module is comprised of DEM Extraction Wizard and three DEM
tools: DEM Editing Tool, Stereo Pair 3D Measurement Tool, and Epipolar 3D Cursor Tool.
You will find below a summary of key functionalities of DEM Extraction module associated with ENVI software.
- DEM extraction is a multi-step, decision-making process that involves setting numerous parameters. You can run the steps individually from the Toolbox, or from within the DEM Extraction Wizard. The Wizard guides you through nine steps. It presents you with objective parameters, such as minimum/maximum elevation of the area of interest, as well as other strategy parameters that depend upon the terrain relief, cultural content, image quality, shadowing, and the desired speed of operation.
As with the DEM Extraction Wizard, you can extract a relative or absolute DEM from a stereo pair of images using the Stereo Pair 3D Measurement Tool and Epipolar 3D Cursor Tool.
- The Stereo Pair 3D Measurement Tool allows you to select a common point from two stereo images and calculate an elevation value for that point (see The Stereo Pair 3D Measurement Tool for information about this tool).
- The Epipolar 3D Cursor tool allows you to perform 3D measurements in a 3D stereo viewing environment based on an existing epipolar stereo pair of images. You can view an anaglyph of epipolar images and adjust the apparent height of the cursor to extract elevation data (see The Epipolar 3D Cursor Tool for information about this tool).

http://www.prashantsurveys.com/3d-city-mapping-and-smart-city-survey.php


3D city models are digital models of urban areas that represent terrain surfaces, sites, buildings, vegetation, infrastructure and landscape elements as well as related objects (e.g., city furniture) belonging to urban areas. Their components are described and represented by corresponding two-dimensional and three-dimensional spatial data and geo-referenced data.

We at "Prashant Surveys" use the combined technology of 3D Mobile LiDAR & UAV (unmanned aerial vehicle) / drone for preparing the 3d base map up to the accuracy of +/- 5 cms. By this technology we can capture and generate 3D point cloud data sets and photographs, which are the basic requirements of 3D modeling.

The drawings and data sets thus generated are to the scale of 1:500 or 1:1,000 which is sufficient for development of smart city of any size.

In some cases, the combined technology of 3D Mobile LiDAR & High Resolution Satellite images can be used for generating the 3D base map up to the accuracy of +/- 20 cms. This method is more cost effective for small to medium sized municipal councils and cities which require about 1: 2,500 or 1:5,000 scale mapping.


https://medium.com/@anttilip/comparison-of-spatial-resolutions-in-satellite-images-3185963a2e96
http://sentinel-pds.s3-website.eu-central-1.amazonaws.com/


**Map Scale**

https://rechneronline.de/scale/
https://www.buyaplan.co.uk/blog/posts/3-1-200-1-500-1-1250-scale-confused
1: 1250 scale: means 1 metre on the map represents 1250 metres on the ground.

1: 200 scale: means 1 metre on the map represents 200 metres on the ground. Therefore it's a far more detailed map than the 1:1250 scale.

https://en.wikipedia.org/wiki/Ordnance_Survey

Ordnance Survey (OS) is a national mapping agency in the United Kingdom which covers the island of Great Britain. It is one of the world's largest producers of maps. Since 1 April 2015 it has operated as Ordnance Survey Ltd, a government-owned company, 100% in public ownership.

https://blog.google/products/earth/keeping-earth-up-to-date-and-looking/ 

https://medium.com/google-earth/imagery-update-explore-your-favorite-places-in-google-earth-5da3b28e4807