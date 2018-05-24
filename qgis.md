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
