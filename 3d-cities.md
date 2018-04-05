/*
Title: 3D City
Decription: 3D City
Author: Bhaskar Mangal
Date: 29th Nov 2017
Tags: 3D City
*/

** Table of Contents**

[TOC]

## 3D Map Libraries
* [3d-map-library-roundup](https://blog.webkid.io/3d-map-library-roundup/)
* [OSM Simple_3D_buildings](http://wiki.openstreetmap.org/wiki/Simple_3D_buildings)
* http://wiki.openstreetmap.org/wiki/Frameworks

**Summary of different JS libraries:**
* Open Source Js for 3D geospatial data rendering
	- Mapbox GL
	- Vizicities
	- OSMBuildings GL
	- Tangram
	- Cesium
	- OpenLayers 3 (OL3)
* Commercial
	- CityEngine
	- Wrld3D

**About 3D Map libraries**
1. **Mapbox GL**
Mapbox GL is, as the name implies, a Mapbox product. It’s available as a Javascript Library but also as a native IOS version (Android is coming soon). If you see it at the first glance, it looks like a normal slippy map, but because it uses WebGL to render the map you have much more possibilities. The team behind it just published a blog post where they describe new features like perspective mode (you can now tilt the map) and touch support for mobile devices.
2. **vizicities**
It is based on THREE.js and uses OpenStreetMaps data to render the buildings, water and park areas.
3. **OSMBuildings GL**
OSMBuildings was first created as a pseudo 3D library that could be used on top of Leaflet or Open Layers. The new GL version now comes with its own map engine called MapGL. It’s a very lightweight library that doesn’t use THREE.js or other webGL helpers. You can use standard tile servers for the basemap and it is easy to use GeoJSON as an additional input to the OpenStreetMap data. The library was created by Jan Marsch.
4. **Tangram**
With Tangram you can create own shaders which can lead to very new map styles like a matrix or a lego city. To tell your map how it should look like you write a yaml file where you define the type of camera, lights, styles and much more. Tangram maps are build on top of Leaflet.
5. **Cesium**
Cesium is a globe and map engine that can render 3D and 2D Maps. There are different plugins like VR or Leap Motion support to extend the core functionality. The library focuses on dynamic data visualizations so you can import collada files, draw vectors from GeoJSON, create camera flights and use standard tile servers.
6. **Open Layers 3**
7. **Leaflet plugin**
	- geojson
	- non WebGL plugin
	- https://github.com/kekscom/L.Line3
8. **[wrld3d](https://www.wrld3d.com/3d-maps/indoor-mapping/)**
Check out our 3D mapping platform, it's free to use and its a true ready build 3D environment. Available on web, mobile, VR, AR, Unity and Desktop. www.wrld3d.com Share with us what you think on Twitter @wrld3d
9. **WebGL for 3D**


## Data format for 3D City

* Rendering format and Geospatial Standards for 3D City data.
* 3D Geospatial Standards References
	* [3d-geospatial-open-standards-v0 ( most concise notes on 3D Geospatial standards)](https://justobjects.nl/3d-geospatial-open-standards-v0/)
	* [From_point_cloud_to_web_3D_through_CityGML](https://www.researchgate.net/publication/235635196_From_point_cloud_to_web_3D_through_CityGML)

### GeoJson

### TopoJSON
* https://github.com/topojson/topojson
**GeoJson v/s TopoJson**
TopoJSON is an extension of GeoJSON that encodes topology. 

### City GML
* https://www.citygml.org/
* https://www.3dcitydb.org/3dcitydb/demos/

### Commercial services for 3D city Data
* [CityGML Wiki - Commercial_Software](http://www.citygmlwiki.org/index.php?title=Commercial_Software)
* [Buy city models with different LoD](https://www.turbosquid.com/3d-models/3d-city-road-street-building/320842)

## Details on 3D Map Libraries

### OSM buildings
* http://wiki.openstreetmap.org/wiki/Simple_3D_buildings


### Tangram
* https://mapzen.com/documentation/tangram/Tangram-Overview/
* https://www.citylab.com/design/2015/03/a-mesmerizing-futuristic-map-with-animated-traffic-and-glowing-buildings/388285/
* https://mapzen.com/blog/tilting-ikeda/
* http://blog.mapillary.com/update/2015/08/04/tangram.html

**with OSM buildings**
* https://mapzen.com/blog/getting-crafty/
http://www.instructables.com/id/What-is-Pepakura-and-how-to-start/

Why I shortlisted Tangram?
1. Built as a leaftlet plugin
2. Opensource
3. Quickly makes beautiful and useful 2D and 3D maps.
4. WebGL
5. Shader programming code can be injected at run time
6. Animation

### Leaflet
* http://joshuafrazier.info/leaflet-basics/
* https://yorkstreetlabs.com/blog/plot-a-multiple-segment-flight-path-with-leafletjs-and-openstreetmap
* http://bl.ocks.org/sigon426/11283563
**vector data**
* https://www.tutorialspoint.com/leafletjs/leafletjs_vector_layers.htm
**KML**
* https://harrywood.co.uk/maps/examples/leaflet/kml.view.html

#### Leaftlet + Mapbox
* https://blog.mapbox.com/mapbox-%EF%B8%8F-leaflet-d60b1be96615

Leaflet can easily integrate with Mapbox, support GeoJSON overlays, as well as nearly any other data source your mapping-heart desires. 

The main map for Leaflet is made of raster tiles. 

Limitations of raster tiles
The limitations of raster tiles become apparent for users who are interested in creating a dynamic web mapping experience — particularly those visualizing data. 

#### GeoJson Examples
* http://leafletjs.com/examples/geojson/

#### D3.js + LeafletJs - Data Visualization & Analytics
* http://adilmoujahid.com/posts/2016/08/interactive-data-visualization-geospatial-d3-dc-leaflet-python/
* https://www.toptal.com/javascript/a-map-to-perfection-using-d3-js-to-make-beautiful-web-maps

### Mapbox GL
* https://www.mapbox.com/bites/00273/

**Mapbox GL 3D Buildings**
* http://thinkingspatial.com/mapbox-gl-js-3d-buildings/

**Indoor 3D Map**
https://122e4e-mapbox.global.ssl.fastly.net/mapbox-gl-js/example/3d-extrusion-floorplan/

### WebGL for 3D Terrain
* **Large scale Terrain:** - very interesting
	* https://github.com/felixpalmer/lod-terrain
	* http://felixpalmer.github.io/lod-terrain/presentation/
* Other References:
	* https://webglfundamentals.org/webgl/lessons/webgl-how-it-works.html
	* https://www.youtube.com/watch?time_continue=1&v=5AGx0_2xI6Y
	* https://webdesign.tutsplus.com/tutorials/create-an-isometric-layout-with-3d-transforms--cms-27134\
	* https://www.smashingmagazine.com/2012/01/adventures-in-the-third-dimension-css-3-d-transforms/
	* https://webdesign.tutsplus.com/articles/css3-transitions-and-transforms-from-scratch--webdesign-4975
	* http://westciv.com/tools/3Dtransforms/index.html
	* https://developer.apple.com/library/content/documentation/InternetWeb/Conceptual/SafariVisualEffectsProgGuide/Using2Dand3DTransforms/Using2Dand3DTransforms.html

### Cesium - Details
1. Cesium started as a software development effort to bring 3D geospatial to the web.
2. Cesium provides 3D, 2D, and 2.5D (what we call Columbus View), all through
a single API

**[3d-scans](https://cesium.com/blog/2017/03/06/3d-scans/)**

[3D WFS Query Demonstration Using GeoServer](https://www.youtube.com/watch?v=SsNlYwbfso8)

@[Alt 3D WFS Query Demonstration Using GeoServer](https://www.youtube.com/watch?v=SsNlYwbfso8)

@[Alt Cesium 3D Tiles Massive Models example - AGI HQ](https://www.youtube.com/watch?v=5Q3RGl1k7x8)

**[massive-models](https://cesium.com/blog/2017/02/21/massive-models/)**
As part of cesium.com, we have been working on a tiling pipeline for converting massive models from glTF into 3D Tiles. The vision is to be able to fly into a city, walk into a building, and inspect the individual bolts on the superstructure or admire a high resolution 3D capture of the interior marble work.

@[Alt massive-models](https://www.youtube.com/watch?v=Fr_sQWROW20)

#### glTF - GL Transmission Format
using glTF, an emerging industry-standard format for 3D models on the web by the Khronos Group, the consortium behind WebGL and COLLADA.
* https://www.khronos.org/gltf
* https://www.khronos.org/assets/uploads/developers/library/overview/gltf-overview.pdf
* https://www.khronos.org/news/press/khronos-finalizes-gltf-1.0-specification

**[What is glTF?](https://en.wikipedia.org/wiki/GlTF)**
- glTF (GL Transmission Format) is a runtime asset delivery format for GL APIs: WebGL, OpenGL ES, and OpenGL developed by the Khronos Group 3D Formats Working Group and first announced at HTML5DevConf 2016. glTF is an efficient, interoperable asset delivery format that compresses the size of 3D scenes and models, and minimizes runtime processing by applications using WebGL and other APIs. glTF also defines a common publishing format for 3D content tools and services.
- glTF, which was then called WebGL TF (WebGL Transmissions Format)
- In March 2013, Cesium adopted glTF instead of "designing yet another asset format."
- On October 19, 2015, the glTF 1.0 specification was announced
  - adopted by Oculus (now facebook), microsoft

**[glTF 2.0 was published June 5, 2017](https://www.khronos.org/news/press/khronos-releases-gltf-2.0-specification)**
The new version has many breaking changes from the original, the most visual being the introduction of Physically based rendering to the core spec.
- glTF is for 3D, much like "MP3 of Audio", "JPEG of 2D images" and "MPEG for videos"
- glTF 2.0 is fully graphics API and operating system-independent, opening up endless possibilities for sharing 3D between applications, across desktop, web, mobile, and virtual and augmented reality.
- The release of glTF 2.0 delivers a significant upgrade to glTF 1.0, an extensible, runtime neutral, open standard format for real-time delivery of 3D assets, which describes full scenes with compact transmission and fast load time.
- the release of glTF 2.0 adds Physically Based Rendering (PBR) for portable, consistent description of materials. In glTF 1.0, a material was defined with a GLSL shader, which suited WebGL, but was problematic when importing a glTF model into a Direct3D or Metal application. Through using PBR, visually arresting glTF 2.0 models are now consistently portable to any rendering API. A PBR material is defined by a few concise parameters that can be used to generate shaders for any rendering API. glTF 2.0 defines a simple to implement, but powerful, PBR model that provides high-quality materials, and yet, is scalable to suit the capabilities of different classes of platform and device.

**[Laytest glTF Specifications here](https://github.com/KhronosGroup/glTF)**


## Tiling for 3D City
* https://openmaptiles.org/docs/
* http://bl.ocks.org/Sumbera/ba554bb5cc8dfe4d7866
* https://github.com/mapbox/mapbox-gl-js/issues/4296

**Types:**
- Raster Tile
- Vector Tiles
	* **Mabbox**
	* **Tangaram**
	* **OSM**
	* **ESRI vector tiling**
		* http://esri.maps.arcgis.com/home/item.html?id=f0b44a7e86b84109920e23e1e09d38a8
- 3D Tiles
	* **Cesium**

### LOD for Tiles for 3D Map
* http://sampleserver6.arcgisonline.com/arcgis/rest/services/Toronto/ImageServer
* https://www.sitepoint.com/canvas-vs-svg-choosing-the-right-tool-for-the-job/
* https://blog.webkid.io/fancy-map-effects-with-css/
* https://gis.stackexchange.com/questions/90061/3d-perspective-on-maps-in-leaflet-cartodb
* https://github.com/OSMBuildings/OSMBuildings
* http://maps.stamen.com/#toner/10/37.7783/-122.3547
* https://stamen.com/
* http://acadia.org/projects/4979CR
* https://github.com/ded/reqwest
* https://mapzen.com/
* https://www.tizen.org/about
* https://mapzen.com/pricing/
* https://github.com/mapbox/mapbox.js/
* https://github.com/mapbox/mapbox-gl-js
* https://stackoverflow.com/questions/35069753/mapbox-gl-js-vs-mapbox-js
* https://en.wikipedia.org/wiki/Protocol_Buffers
* https://stackoverflow.com/questions/16830824/google-maps-using-three-js-and-webgl

### Vector Tiles
* https://en.wikipedia.org/wiki/Vector_tiles
* http://docs.opengeospatial.org/per/16-068r4.html
* https://stevebennett.me/category/mapmaking/
* https://en.wikipedia.org/wiki/Tiled_web_map
* https://www.mapbox.com/get-directions/#16/12.97/77.5975?coordinates=77.7473,12.9716;77.59796,12.96991
* http://project-osrm.org/
* https://blog.mapbox.com/dive-into-large-datasets-with-3d-shapes-in-mapbox-gl-c89023ef291https://blog.mapbox.com/dive-into-large-datasets-with-3d-shapes-in-mapbox-gl-c89023ef291
* http://www.cybercity3d.com/
* https://github.com/lukasmartinelli/osm-liberty
* https://enable-cors.org/

As of early 2015, there is no dominant standard for vector tiles
Protocol buffers (Mapbox)
Mapbox have defined an open standard for vector map tiles called "vector-tile-spec" which uses Google protocol buffers for space-efficient data serialisation. Web Mercator is the projection of reference, but vector tiles may be used to represent data with any projection and tile extent scheme.[7] It is also tied to the Mapnik rendering engine, using a "serialized version of the internal data that Mapnik uses"
In March 2015, Esri, the dominant geospatial software maker, announced that they would be supporting Mapbox's vector tiles standard in both server and client platforms

**Vector Tiles**
* https://gis.stackexchange.com/questions/190390/how-to-load-a-vector-tile-layer-in-a-leaflet-map
* https://mapzen.com/projects/vector-tiles/
* https://openmaptiles.org/
* https://giswiki.hsr.ch/Vector_Tiles

**Vector Tiles Providers**
* MapBox Map Styles
* MapZen Vector Tiles
* OpenMapTiles.org (formerly OSM2VectorTiles) by Klokan Technologies and Geometa Lab

**Vector Tiles Readers/Clients we know:**
* Leaflet with MapBox GL extension
* OpenLayers 3
* Syling editor and inspector: http://maputnik.com/editor/#14.99/47.2253/8.8160
* Plugin for Mapbox GL JS to view the view ans inspect VT features: https://github.com/lukasmartinelli/mapbox-gl-inspect
* MapTiler
* Vector Tiles Reader QGIS Plugin


**Vector Tiles Generators/Servers:**
t-rex - MVT server. Serves tiles from PostGIS supporting custom tile grids. single executable written in Rust by Pirmin Kalberer, Sourcepole. https://github.com/pka/t-rex/
Tileserver - A lightweight tileserver to share code paths with tilequeue for tile generation. Written in a single Python file by Ian Dees. https://github.com/tilezen/tileserver
Tiler - Command line tool for converting GeoJSON, Shapefiles or PostGIS layer to raw Vector Tiles (or MBTiles). Written in Python (avail. as Docker container) by Geovation. https://github.com/Geovation/tiler
tippecanoe - Build vector tilesets from large collections of GeoJSON features. Written in CPP (OSX only?) by Mapbox. https://github.com/mapbox/tippecanoe
GeoServer for creating Vector Tiles in GeoJSON, TopoJSON, and MapBox Vector Tiles format for all the vector data formats it supports. https://github.com/geoserver/geoserver/tree/master/src/community/vectortiles
ArcGIS Pro
For software around vector tiles see https://github.com/mapbox/awesome-vector-tiles

* http://suite.opengeo.org/docs/latest/dataadmin/vectortiles/install.html
* https://maps3d.io/
* http://bl.ocks.org/letmaik/e71eae5b3ae9e09f8aeb288c3b95230b

### Raster V/s Vector
* http://vector-conversions.com/vectorizing/raster_vs_vector.html

### [3D Tiles](https://github.com/AnalyticalGraphicsInc/3d-tiles)
* [Introducing 3D Tiles](https://cesium.com/blog/2015/08/10/introducing-3d-tiles)
* [3d Tiles Specifications by Cesium](https://github.com/AnalyticalGraphicsInc/3d-tiles)
* [3D geospatial to the web](https://cesium.com/blog/2016/09/06/3d-tiles-and-the-ogc)
* [Community Standard Justification Document (docx)](https://portal.opengeospatial.org/files/70040)
* https://cesium.com/blog/2015/08/10/introducing-3d-tiles/
* https://groups.google.com/forum/#!topic/cesium-dev/tCCooBxpZFU%5B1-25%5D
3D Tiles are an open specification for streaming massive heterogeneous 3D geospatial datasets.
They are the foundation for the streaming 3D buildings, for streaming point clouds, trees, vector data, and other massive geospatial datasets.
The primary purpose of 3D Tiles is to improve streaming and rendering performance of massive heterogeneous datasets.
* https://cesium.com/blog/2015/08/10/introducing-3d-tiles/
  - The foundation of 3D Tiles is a spatial data structure that enables Hierarchical Level of Detail (HLOD) so only visible tiles are streamed - and only those tiles which are most important for a given 3D view. Tile payloads can be binary and context-aware compressed, e.g., using Open3DGC or oct-encoding.
Instead of relying on 2D constructs such as zoom levels, 3D Tiles are based on geometric error for Level-Of-Detail (LOD) selection and a tunable pixel error.
  - In 3D Tiles, bounding volumes are 3D, not 2D cartographic extents
  - 3D Tiles the tiling scheme is adaptable, in all three dimensions, depending on the models in the dataset and their distribution.
  - Traditional geospatial features, such as polygons and polylines, can be extruded or drawn above the surface. But 3D Tiles go beyond points, polylines, and polygons, to account for full 3D models with meshes, materials, and a node hierarchy.
* https://gis.stackexchange.com/questions/239264/current-status-of-open-source-3d-gis-software-and-libraries


In order to efficiently stream these datasets for visualization, 3D Tiles is the specification evolved for streaming massive heterogeneous 3D geospatial datasets. Heterogeneous 3D geospatial datasets includes:
- point clouds
- terrain
- 3D buildings
- trees
- vector data

To expand on Cesium’s terrain and imagery streaming, 3D Tiles will be used to stream 3D content, including buildings, trees, point clouds, and vector data.
- Bringing techniques from graphics research, the movie industry, and the game industry to 3D geospatial.
- 3D Tiles define a spatial data structure and a set of tile formats designed for 3D and optimized for streaming and rendering.
- Tiles for 3D models use glTF, the WebGL runtime asset format developed by Khronos, which the Cesium team heavily contributes to.
- CZML, a JSON schema for describing time-dynamic 3D scenes
- quantized-mesh for efficiently streaming terrain
- glTF, the runtime 3D model format we co-created with Khronos

The foundation of 3D Tiles is a spatial data structure that enables Hierarchical Level of Detail (HLOD) so only visible tiles are streamed - and only those tiles which are most important for a given 3D view. Tile payloads can be binary and context-aware compressed, e.g., using Open3DGC or oct-encoding.
- Instead of relying on 2D constructs such as zoom levels, 3D Tiles are based on geometric error for Level-Of-Detail (LOD) selection and a tunable pixel error. This allows performance/visual-quality tuning and is built for multiple “zoom levels” in the same view.
- In 3D Tiles, bounding volumes are 3D, not 2D cartographic extents
- In 2D, the tiling scheme is often based on the Web Mercator projection. Web Mercator is not ideal for 3D because the poles project to infinity and also because the NGA does not recommend Web Mercator for DoD application.
- In contrast, in 3D Tiles the tiling scheme is adaptable, in all three dimensions, depending on the models in the dataset and their distribution.
- Traditional geospatial features, such as polygons and polylines, can be extruded or drawn above the surface
- But 3D Tiles go beyond points, polylines, and polygons, to account for full 3D models with meshes, materials, and a node hierarchy
- 3D Tiles support interactive selection and styling
- **Intreractive Selection**
  - Even with **WebGL optimizations such as batching**, 3D Tiles allow for individual model interaction such as highlighting on mouseover, or removing a 3D building
  - Tiles can contain metadata for each model to allow additional interaction, such as querying third-party web services using a building ID
- **Stylable**
  - Metadata for individual models, such as building height or year built, can be used for shading at runtime without writing code. Styles can be changed on-the-fly.
  - Height-dependent building color demonstrating 3D Tile styling
- **Adaptable**
  - Traditional quadtree subdivision, used in TMS for example, is sufficient for map tiles and 2D, but it is suboptimal for 3D and non-uniform dataset distributions.
  - 3D Tiles enable adaptive spatial subdivision in 3D, including **k-d trees**, **quadtrees**, **octrees**, **grids**, and other spatial data structures
- **Flexible**
  - 3D Tiles allow both replacement and additive refinement.
  - With traditional 2D map tiles, when the user zooms in, the visible map tiles are replaced with new higher-resolution map tiles. This is called **refinement**. In a sense, a subset of the same content is downloaded again, but at a higher resolution. We call this replacement refinement, and it is a reasonable solution for imagery tiles and even 3D terrain.
  - However, more flexibility is needed for other 3D datasets such as buildings and point clouds. For example, instead of essentially downloading the same building multiple times as the viewer zooms in, 3D Tiles rather stream just new buildings. We call this additive refinement. Additive refinement has the additional benefit that child tiles can be rendered as they are downloaded, as opposed to replacement refinement, which requires that all of a parent’s children be downloaded first.
- **Heterogeneous**
  - 3D Tiles are heterogeneous because there is no one-size-fits-all for 3D datasets. Batched models (e.g., buildings) need a different representation from instanced models (e.g., trees), which need a different representation from point clouds, and so on.
  - 3D Tiles support heterogeneous datasets by enabling adaptive subdivision, flexible refinement, and an extendable set of tile formats.
  - The heterogeneous nature of 3D Tiles allows discrete levels of detail combined with HLOD so, for example, a 3D building could be a billboard and label at one LOD, an extruded footprint at a higher LOD, a 3D model at the next LOD, and a textured 3D model at the highest LOD.
- **Temporal**
  - Cesium is designed for time-dynamic visualizations, such as of satellites and UAV. The next step is to extend this to 3D Tiles so users can, for example, see topography or snow cover change over time with massive time-dynamic terrain and point clouds.

**the-next-generation-of-3d-tiles**
- A truly 3D vector tile for heterogeneous classification
- Time-dynamic streaming
- A 3D analytics-enabled styling language
- Fast compression
- Implicit tiling schemes
- An even more engaged community and ecosystem

### Other Technologies
* **Google Draco compression for 3D**
  - https://opensource.googleblog.com/2017/01/introducing-draco-compression-for-3d.html
  - https://github.com/google/draco
Draco is a library for compressing and decompressing 3D geometric meshes and point clouds.

We are building the commercial Cesium Composer platform to provide 3D tiling for a diverse array of datasets such as photogrammetry models, CAD, 3D buildings, and point clouds. We expect to see many 3D Tiles projects—from exporters to converters to rendering engines—continue to emerge from the Cesium team and the entire community.

## Point Cloud Data - Browser Based Rendering

**PCD rendering engines:-**
* cesium
* potree
	* [Potree_Rendering_Large_Point_Clouds_in_Web_Browsers](https://www.researchgate.net/publication/309358171_Potree_Rendering_Large_Point_Clouds_in_Web_Browsers)
* plas.io
* [itowns] (itowns-project.org)
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


## LoD Concept - Level of Details and Positional Errors
* http://www.tandfonline.com/doi/full/10.1080/15230406.2017.1279986

**LoD (Level of Details) concept in 3D city specification:**
* https://github.com/tudelft3d/Random3Dcity
* http://www.gdmc.nl/publications/reports/GISt62.pdf
* http://filipbiljecki.com/publications/2014_ceus_lod_formalisation.pdf

two considered qualities of geographical data – LOD and accuracy.
While there is an association between the two (representations at finer scales tend to be of higher quality (Heuvelink, 1998 Heuvelink, G. B. M. (1998). Uncertainty analysis in environmental modelling under a change of spatial scale. Nutrient Cycling in Agroecosystems, 50(1), 255–264. doi:10.1023/A:1009700614041
[Crossref], [Web of Science ®], [Google Scholar]
)), these are two independent concepts (Chrisman, 1991 Chrisman, N. (1991). The error component in spatial data. In P. A. Longley, M. F. Goodchild, D. J. Maguire, & D. W. Rhind (Eds.), Geographical information systems: Principles and applications (pp. 165–174). Harlow, UK: Longmans.
 [Google Scholar]
). For instance, a national government may produce a GIS dataset in which buildings are modeled in a coarse but accurately derived representation, and a municipality may produce a dataset of a city in finer detail but with less accuracy due to an inferior acquisition technique (e.g. automatic reconstruction from lidar instead of terrestrial measurements).


### Errors
https://www.iso.org/standard/32575.html
http://inspire-regadmin.jrc.ec.europa.eu/dataspecification/themes/lu/Chapter7.pdf

3D geoinformation at fine LODs may in fact be too complex for certain spatial analyses. Hence, the data are occasionally generalized to reduce complexity while attempting to preserve usability. By generalizing the models to a point at which their complexity is sufficiently reduced but at the same time their usability is not compromised by the reduced LOD.

For instance, the standard ISO 19157 on geographic data quality defines several types of errors, for example:
completeness
topological
positional
thematic (attribute)
and temporal errors
Geographic information – Data quality. Geneva: International Organization for Standardization.
Analysis-induced error
there will usually be error induced by the imperfection of the empirical models and other factors behind a spatial analysis. 


investigate the propagation of positional error in point clouds to the calculation of various topographic attributes, such as slope, aspect, and watershed area.

propagation of positional error from terrestrial laser scanning to the measurement of snow volume.

Positional errors are omnipresent in GIS and they have been much discussed in the literature



The concept of LOD in 3D GIS is somewhat different from the one in cartography and imagery

 In rasters, detail is simply quantified as the size of pixels (spatial resolution). Hence it is straightforward to line up different representations (e.g. orthophotos with pixel sizes of 10, 20, and 50 cm). 

In maps, the LOD is tied to scale: each scale series (e.g. 1:10k, 1:20k, and 1:50k) contains a certain amount of detail that ought to be mapped. However, in 3D city modeling the distinction is not as straightforward, due to the digital environment and involvement of different features, which results in different understandings of measuring detail.

LOD1 is a block model
  - LOD1 is usually produced by extruding footprints 
LOD2 is a generalized model containing basic roof shapes
  - LOD2 can be acquired automatically from lidar data
LOD3 is an architecturally detailed model containing openings and facade detail
  - LOD3 usually involves substantial manual work or is obtained after conversion from architectural sources

These LODs roughly reflect the different outcomes of different acquisition techniques. 

Moreover, LOD3 models are rarely used in spatial analyses and we are not aware of any LOD3 model produced on a large spatial scale due to excessive costs of acquisition. Hence LOD3 is a good choice as ground truth reference data.

Hence, it is important to investigate different magnitudes of positional error (standard deviation ).

Our approach assumes that there is no correlation in the errors in different dimensions.

We follow the assumption of uncorrelated errors in coordinates.
3D city models are often acquired in different acquisition campaigns
* footprints
  - acquired with a geodetic survey
  - from ground measurements
* the elevation of the building
  - acquired with airborne laser scanning
  - guessed from the number of storeys

Comparing errors (%) of two datasets with opposite qualities:
a fine detailed (LOD2) model acquired with poor accuracy, and a coarse model (LOD1) acquired with higher accuracy.

- LOD1 acquired with higher accuracy is a much better choice than the finer LOD2 acquired with poorer accuracy
- For all analyses, planar error has a larger effect than error in the vertical coordinates. However, the degree of such influence differs, and this behavior is mostly exhibited in the estimation of solar irradiation.

projection errors
together with the errors caused by ignoring terrain elevation – affect the building footprint dimensions

## 3D Spatial Analysis
* Geographic information may be used to predict the energy demand of households based on the morphology of a building
* 3D city models are frequently used to estimate the solar irradiation of building rooftops for determining the suitability of installing photovoltaic panels
* Based on the distribution of building stock, population estimation can be conducted.
* 3D city models may be used for a variety of purposes, for instance, estimating the noise pollution at a location
* 3D city models may be used for different kinds of visibility analyses, and therefore quantified in different ways: binary (a point in space is visible or not), distance (range) of visibility, the area or volume visible from a point, number of buildings that have visual access to a feature, and population that has visual access to a point
* simulations estimating the wind flow
* noise pollution estimations
  - roof shapes are an important factor to consider in noise pollution estimations
* **1. Area of the building envelope**
- 3D city models are suitable to calculate the area of the exposed building shell. This information is useful in planning energy-efficient retrofitting, estimating indoor thermal comfort and energy consumption, analyzing the urban heat island effect, and further similar applications
* **2. Gross volume of a building**
- Estimation of the volume of buildings is useful in various analyses, such as urban planning, estimating the stock of materials in the building sector, waste management, population estimation, quantifying development densities, energy estimation, and predicting thermal comfort
* **3. Solar irradiation of rooftops**
- Estimating the insolation (solar exposure) of buildings is one of the most prominent spatial analyses using 3D city models. The solar irradiation of rooftops is calculated based on the orientation and inclination of roofs, among other factors, which involve spatial operations that are all prone to errors.
- This application has wide applicability, for example, assessing the suitability of installing solar panels, preventing overheating, and predicting house prices
- Typically the annual exposure to sun is estimated and quantified in kWh/m^2
- LOD does not have a significant influence on shadow estimation.
* Procedural modeling involves generating geographical data based on a set of customized rules to represent a specific setting

LOD2 is a better choice than LOD1 in all three spatial analyses, as it resembles the abstracted phenomena in more detail. 
LOD2 may come at a significantly higher cost but for a marginal improvement.
LOD2 conceptually derives the same volume as LOD3, because the details brought by LOD3 (e.g. windows, facade details, awnings, chimneys) do not bring any difference to the computation of volume. Hence,  ignoring acquisition errors at this point, it appears that LOD3 does not bring any benefit over LOD2 when it comes to the computation of gross volume.

**conclusion**
- A major finding of this paper is that taking care of the accuracy of the data is more important than striving to produce data of a finer LOD, at least in the spatial analyses that we considered.
- The difference in the performance of LOD1 and LOD2 is so small that it appears that in many cases it is not worth acquiring an LOD2
- The leap between LOD2 and LOD3 is much larger than between LOD1 and LOD2. Hence it would be beneficial to strive toward the large-scale production of LOD3. However, such an advancement does not yet appear imminent: while many LOD3 models of limited spatial extent have been produced and used in various analyses, their production will remain expensive and wide coverage will not be feasible for some time.
- Taking into account the realization of the 3D models, positional error has a substantial effect on the errors of the quantities estimated in this study (building envelope area, gross volume, and solar irradiation of rooftops).
- Positional error dominates over the error induced by a coarse LOD. 

(i) the positional error is in many cases significantly more dominant than representation error;
(ii) as a result of this, in a lot of instances there is no need to go for a high representation level (LOD3) because the added value will vanish due to acquisition error;
(iii) the two considered errors are not additive;
(iv) error propagation is case specific, hence there is no general conclusion that can be drawn for all spatial analyses;
(v) when disturbed with larger positional errors a lower representation may give better results in a spatial analysis than a higher representation disturbed with the error of the same magnitude.

- LOD in 3D GIS and scale in 2D GIS are related but different concepts
- Scale in 2D is mainly associated with accuracy and precision, with less detail on small-scale maps, while for 3D that relation does not always hold.
- In 3D data of coarse detail at a high precision/accuracy level is common, regardless of the spatial scale.

### Questions
* What should the minimum accuracy and LOD available in the data be, so that these are usable for accurately calculating the volume of buildings?
* At what LOD and at what accuracy should a 3D model be acquired to be usable for a particular spatial analysis?
* Is it beneficial to acquire a dataset of a fine LOD if the acquisition technique has poor accuracy?
* Whether a certain spatial analysis can take advantage of this finer detail? (First, as modeling data at finer LODs comes at a higher cost)

**Projects**
https://github.com/tudelft3d/val3dity
https://github.com/tudelft3d/azul

http://www.cityjson.org/en/0.2/

## SatelliteViewer
http://apps.agi.com/SatelliteViewer/?Status=Operational
http://www.agi.com/news/blog
## GIS Data Quality Standards

## GIS Data Sources

**best-free-gis-data-sources-raster-vector**
* http://gisgeography.com/best-free-gis-data-sources-raster-vector/

**free-satellite-imagery-data-list**
* http://gisgeography.com/free-satellite-imagery-data-list/

**free-global-dem-data-sources**
* http://gisgeography.com/free-global-dem-data-sources/

## Working with Openstreet Data
* https://blog.mapbox.com/mapping-3d-building-features-in-openstreetmap-7685ee12712a
* https://blog.mapbox.com/3d-building-data-for-san-francisco-73a9e885f788
* http://wiki.openstreetmap.org/wiki/Mapbox_GL
* https://blender.stackexchange.com/questions/62619/how-to-import-3d-buildings-from-openstreetmap-to-blender
* www.sarahmakesmaps.com/maps/


### Open Data Sources
* https://www.wikidata.org

### OSM Data Editors
**JOSM**
* https://josm.openstreetmap.de/
JOSM is an extensible editor for ​OpenStreetMap (OSM) for ​Java 8

## Javascript Map examples
* https://codepen.io/stevepepple/post/javascript-geospatial-examples
* https://bl.ocks.org/andrewxhill

### Visualizations
* https://bl.ocks.org/

## Projections

### [Web Mercator](https://en.wikipedia.org/wiki/Web_Mercator)**
- It is a variant of the Mercator projection and is the de facto standard for Web mapping applications.
- It is used by virtually all major online map providers, including Google Maps, Bing Maps, OpenStreetMap, Mapquest, Esri, Mapbox, and many others
- Its official EPSG identifier is EPSG:3857
- Web Mercator - Google Web Mercator, Spherical Mercator, WGS 84 Web Mercator or WGS 84/Pseudo-Mercator
- the Web Mercator uses the spherical formulas at all scales whereas large-scale Mercator maps normally use the ellipsoidal form of the projection.
- The discrepancy is imperceptible at the global scale but causes maps of local areas to deviate slightly from true ellipsoidal Mercator maps at the same scale. This deviation becomes more pronounced further from the equator, and can reach as much as 35 km on the ground
- While the Web Mercator's formulas are for the spherical form of the Mercator, geographical coordinates are required to be in the WGS 84 ellipsoidal datum
- The benefit is that the spherical form is much simpler to calculate, saving many computing cycles
- Due to slow adoption by standards body European Petroleum Survey Group (EPSG), the Web Mercator is represented by a confusing series of standard names and ids, including OpenLayers:900913, EPSG:3785 and EPSG:3857.

### [Mercator](https://en.wikipedia.org/wiki/Mercator_projection)**

**Visualizing-Spatial-Data**
* https://cesiumjs.org/tutorials/Visualizing-Spatial-Data/

**Cesium Tutorials**
* https://cesiumjs.org/tutorials/
* https://github.com/AnalyticalGraphicsInc/cesium/wiki/Tutorials-Details

**Presentations & K-bank**
* https://cesium.com/presentations/

**Cesium Development - using Sandcastle**
* https://cesiumjs.org/Cesium/Apps/Sandcastle/index.html?src=Imagery%20Layers.html&label=Showcases
* https://mapsapidocs.digitalglobe.com/docs/maps-api-cesiumjs-3d-globe

**Internal Development Assets**
http://10.4.71.121/local/jayashree/maze/mazeTpcd.php
http://10.4.71.121/local/jayashree/maze/mazeDeck.php
http://10.4.71.121/local/jayashree/maze/cesium/Apps/

**Commercial: Cesium Composer**
* [3d-tiles-pioneers](https://cesium.com/3d-tiles-pioneers/)

## Keywords & Definitions

* HLOD - Hierarchical Level of Detail
* [SRS - Spatial Reference System](https://en.wikipedia.org/wiki/Spatial_reference_system)
A spatial reference system (SRS) or coordinate reference system (CRS) is a coordinate-based local, regional or global system used to locate geographical entities. A spatial reference system defines a specific map projection, as well as transformations between different spatial reference systems.

**DPI vs PPI**
++DPI - Dots per Inch++
This is the amount of ink dots the printer will put on each pixel of your image. The DPI is set by the actual printer device and it is not something in the image for the graphic designer to manipulate.

++PPI - Pixels per Inch++
Digital raster images are measured in pixels, or picture elements. How many pixels per inch is determined by the device you create the digital image with: camera, scanner, or graphics software and can be modified with a photo/paint editing software.

**[accelerometer](https://en.wikipedia.org/wiki/Accelerometer)**
An accelerometer is a device that measures proper acceleration;


**[gyroscope](https://en.wikipedia.org/wiki/Gyroscope)**
A gyroscope (from Ancient Greek γῦρος gûros, "circle" and σκοπέω skopéō, "to look") is a spinning wheel or disc in which the axis of rotation is free to assume any orientation by itself. When rotating, the orientation of this axis is unaffected by tilting or rotation of the mounting, according to the conservation of angular momentum. Because of this, gyroscopes are useful for measuring or maintaining orientation.[1][2]

Applications of gyroscopes include inertial navigation systems where magnetic compasses would not work.

**[magnetometer](https://en.wikipedia.org/wiki/Magnetometer)**
A magnetometer is an instrument that measures magnetism—either magnetization of magnetic material like a ferromagnet, or the direction, strength, or the relative change of a magnetic field at a particular location. A compass is a simple example of a magnetometer, one that measures the direction of an ambient magnetic field.

**[altimeter](https://en.wikipedia.org/wiki/Altimeter)**
An altimeter or an altitude meter is an instrument used to measure the altitude of an object above a fixed level. The measurement of altitude is called altimetry, which is related to the term bathymetry, the measurement of depth under water.

**[Odometer](https://en.wikipedia.org/wiki/Odometer)**
An odometer or odograph[1][2] is an instrument for measuring the distance travelled by a vehicle, such as a bicycle or automobile. 



The system supports connection of a high resolution wheel speed sensor or odometer which allows it to maintain accurate data through GPS outages and continue surveys through tunnels and other areas where GPS signals are not available. It also supports kinematic post processing with Advanced Navigation's Kinematica post processing software.

 From the velocity and orientation data, slip, oversteer and understeer can be calculated. The velocity and acceleration data can be used to calculate improvements to braking and accelerating. Position can be used to determine the deviation from the optimum track position. Spatial Dual’s high vibration tolerance and dynamic range means there are no concerns about engine or road vibration. Spatial Dual also supports data output to data acquisition systems such as Dewesoft products.


http://gpsworld.com/advanced-navigation-releases-gnssins-post-processing-software/

ls: Maperitive, OSM2World, osmconvert, OSM-mapsplit, Osmosis, OSM-splitter.﻿

https://www.youtube.com/watch?v=i4ySFm4ey9U


http://docs.geoserver.org/stable/en/user/extensions/printing/protocol.html
https://gis.stackexchange.com/questions/132242/what-are-the-differences-between-tms-xyz-wmts




## Open Source Geospatial communities and forum to follow
* http://www.opengeospatial.org/
* http://www.web3d.org/
Founded in 1997, we are an International, non-profit, member-funded, industry standards development organization. We develop and maintain royalty-free ISO standards for web-based 3D graphics. Our standard   X3D (Extensible 3D) originated from VRML and is available in XML, Compressed Binary, and classic VRML formats. X3D is open, royalty free, extensible, interoperable, and runs on all platforms including desktops, tablets, and phones. Our members are from business, academia, government and the military.

**[SIGGRAPH](https://en.wikipedia.org/wiki/SIGGRAPH)**
- SIGGRAPH (short for Special Interest Group on Computer GRAPHics and Interactive Techniques) is the name of the annual conference on computer graphics (CG) convened by the ACM SIGGRAPH organization. The first SIGGRAPH conference was in 1974. The conference is attended by tens of thousands of computer professionals. Past SIGGRAPH conferences have been held in Los Angeles, Dallas, New Orleans, Boston, Vancouver, and elsewhere in North America.

**Khronos Group**
-  Khronos is the governing body behind many graphics standards, such as OpenGL, Collada, and WebGL
- The Khronos Group is an industry consortium creating open standards to enable the authoring and acceleration of parallel computing, graphics, vision and neural nets on a wide variety of platforms and devices. Khronos standards include Vulkan®, OpenGL®, OpenGL® ES, OpenGL® SC, WebGL™, SPIR-V™, OpenCL™, SYCL™, OpenVX™, NNEF™, COLLADA™, OpenXR™ and glTF™. Khronos members are enabled to contribute to the development of Khronos specifications, are empowered to vote at various stages before public deployment, and are able to accelerate the delivery of their cutting-edge accelerated platforms and applications through early access to specification drafts and conformance tests.


# Misc
http://www.indiageospatialforum.org/2015/ppt/Vinod_Bothale.pdf
https://bim-international.com/wp-content/uploads/2016/03/LOD-Specification-2015.pdf

Similarly as traditional 2D geo-datasets, 3D city models are an approximation of the real world: features are modelled at a particular grade and certain elements are simplified or omitted.
The quantity and mixture of content is driven by the intended use of the 3D city model, provenance of the base data, acquisition technique, invested funds, and spatial scale.
The amount of detail that is captured in a 3D model, both in terms of geometry and attributes, is collectively referred to as the level of detail (LOD), indicating how thoroughly a spatial extent has been modelled. As a result, the LOD is an essential concept in geographical information science (GIS) and 3D city modelling.

Having the LOD in mind when planning the acquisition of data is essential for proper budgeting of resources, and the LOD determines the acquisition technologies that ought to be employed as different LODs are a result of different data acquisition approaches, e.g. it drives the minimum point cloud density when using airborne laser scanning, and determines whether a particular acquisition technique is sufficient or requires additional acquisition means.

LOD does not refer only to the amount of geometric data, but also to the semantic richness.
Data is subject to conversion, which usually depends on its LOD. After the dataset is acquired, the LOD influences the storage aspect, substantially influencing the storage footprint, and necessitating compression and integration techniques.

Quality control is another aspect in the life cycle of the 3D city model where the LOD is consulted in order to ensure that all bits of data have been presented according to the specified LOD.

Once the data is ready for dissemination, the LOD drives aspects such as the exchange of data, materialisation (3D printing), streaming, and delivery; topics all relevant for interoperability.

**Problem Area**
LOD concept in 3D city modelling, this topic has not been investigated extensively, and there has been no holistic research that encompasses the complete pipeline. The term LOD has often been used interchangeably with scale, accuracy, and quality, and it has been largely used colloquially to generally point out the richness of a geographical dataset, without standardisation and formalisation.

Unlike the explicit notions of scale in cartography, triangles in computer graphics, and resolution in rasters, determining the level of detail in 3D city modelling is a subjective task

The five LODs of the OGC CityGML 2.0. The standard attempts to assign standardised classes to generally differentiate grades of 3D data. The geometric detail and the semantic complexity increase with each level. This LOD categorisation is well known in the 3D GIS community, however, it is not without shortcomings.

Once acquired, processing the data without the understanding of the LOD may introduce errors, and quality control cannot be performed rigorously if an LOD standard is not present.

- rooftop Insolation, the exposure to the sun’s rays, should not be confused with insulation, the action or state of
keeping something insulated from unwanted loss of heat or from the intrusion of sound by interposing
adequate material.
- shadow analysis
- windflow analysis

It may lead to the acquisition of an inadequate dataset, not only insufficiently detailed, but also overly detailed, leading to unnecessary costs that do not bring a tangible benefit.

Finally, the lack of a well founded framework on the LOD concept inhibits maintaining and updating a dataset. For example, keeping the LOD consistent during maintenance is of utmost importance for change detection. Otherwise, an arising detail in the new version of a dataset may present an old feature that was not acquired in the previous acquisition campaign, rather than a change in the real world.

**How should we consider, integrate, and improve the concept of level of detail in 3D city modelling?**
**how does the LOD influence the quality of spatial analyses?**
**Whether it is worth acquiring a finer LOD if the acquisition method is not proportionally accurate, and vice-versa?**

- Type of 3D geoinformation
- how the data is acquired
- what are the applications of 3D geoinformation

spatial analyses and concrete examples of 3D geoinformation put into operation
an emphasis is put into cataloguing uses of 3D city models


Part I: Framework and specification
- formalises the LOD concept in 3D city modelling
  - investigates the current status of the LOD concept
  - present practices of stakeholders in the 3D GIS community,
  - identifies the main shortcomings of the current LOD approaches
  - the relationship of the LOD concept to its progenitor in computer graphics
- whether there are multiple valid variants of the same LOD, depending on the acquisition technique that is employed to generate a 3D city model.
- exposes several different variants of data that are of the same LOD, naming them geometric references

presents an approach to realising 3D city models in the newly defined LOD specification with procedural modelling

In GIS, generalisation is used to reduce the LOD of a dataset: from a finer to a coarser LOD, thus removing complexity while preserving usability.
augment LOD using machine learning techniques

**Influence of positional errors induced during the acquisition process** 
The LOD concept is closely related to errors; given that acquisition techniques that are capable of producing data at finer LOD are usually more accurate, this results in a strong association between the level of detail and level of accuracy. However, inverse situations (i.e. coarse detail acquired with high accuracy, and vice-versa) are frequently becoming the case with the advent of volunteered geoinformation and new acquisition techniques.

---

Chapter 2: Background
- different types of 3D geographic information

Three-dimensional geoinformation is data that describes geographic features in 3D space with a set of (x, y, z) coordinates.
This general definition results in encompassing a broad notion of different forms of data, such as:
- movement trajectories in 3D space
- digital elevation models (DEMs)
- 3D geological models

One of the subsets of 3D geoinformation are 3D city models, which are usually defined as a representation of an urban environment with a three dimensional geometry of common urban objects and structures, with buildings as the most prominent feature
This idea leaves some ambiguity leading to different interpretations
of what 3D city models are
- some researchers consider point clouds as 3D city models
- while others include polygon meshes in that context
- the definition is complicated by the fact that different types of data may be combined together

- define 3D city models

3D city models are defined as structured objects described by their boundary surfaces that may be semantically enriched

LOD has an analogy:
- point clouds are characterised by density and voxels by resolution
- Both may be considered as equivalents to the LOD concept in 3D city modelling

- current mechanisms for producing 3D city models
- covers their usability in different application domains
- describes the concept of level of detail in building information modelling


## MMI APIs
https://mt1.mapmyindia.com/advancedmaps/v1/siwqp8sagdytkdzh95bd95e3hiv7mo5q/still_map/12/2933/1898.png
https://mt1.mapmyindia.com/advancedmaps/v1/siwqp8sagdytkdzh95bd95e3hiv7mo5q/still_map/15/9155/11954.png

## Data Visualization
https://bocoup.com/services/datavis

## Cartography
http://www.axismaps.com/guide/

## Blogs on Maps
https://bocoup.com/blog/exploring-new-technologies-for-making-maps-vector-tiles-webgl-part-one

## Extras
* **sublime text editor shortcut**
	* https://gist.github.com/eteanga/1736542

# Showcase
https://eng.uber.com/deck-gl-framework/

**Deck GL**
> 3D Visualization over map, mapboxgl, deckgl

http://uber.github.io/deck.gl/#/documentation/overview/introduction
http://uber.github.io/deck.gl/#/
http://gnavvy.me/



**People, Blogs to Follow**
https://twitter.com/philogb

https://www.census.gov/

**3D geojson viewer**
https://github.com/maptime-ams/geojson-3d
http://mapmeld.com/majurojs/3d/

*map GIS tools online**
http://geojson.io/#map=18/12.98056/77.72202

https://gis.stackexchange.com/questions/115433/online-wkt-and-geojson-viewer
http://mapshaper.org/

amount payable 6044/-

https://gis.stackexchange.com/questions/230939/cesium-load-geometry-as-geojson


1. mine to map every buildings in a city
http://www.sarahmakesmaps.com/blog/2016/3/mapping-jersey-city

digitized all of the building
some basic classification by zoning and land use


OSM's iD-editor, JOSM, the JOSM BuildingTools plugin, QGIS, and the qgis2web plugin

 I've been working on some computer vision algorithms that automate this part of the process and I did use them here. 

 http://sml2198.github.io/maptime-sv/2015-10-18_OSM/GISday.html
 https://josm.openstreetmap.de/wiki/Introduction

JOSM
https://josm.openstreetmap.de/wiki/Introduction
 http://wiki.openstreetmap.org/wiki/JOSM/Plugins/BuildingsTools

https://www.openstreetcam.org/details/5537/215

able to classify all of the buildings by height and age too,

https://github.com/tomchadwin/qgis2web
oin the buildings with assessor data for ownership and evaluation information


https://www.gislounge.com/a-web-mapping-tutorial-for-beginners/

http://www.mcdemarco.net/blog/2015/03/26/scms/

https://bauncms.com/download


https://blog.mapbox.com/dive-into-large-datasets-with-3d-shapes-in-mapbox-gl-c89023ef291

https://www.mapbox.com/bites/00273


https://gis.stackexchange.com/questions/20404/assign-multiple-colors-to-features-within-a-single-vector-layer


# mapboxgl
https://www.mapbox.com/mapbox-gl-js/example/filter-features-within-map-view/
https://www.mapbox.com/help/analysis-with-turf/
https://bl.ocks.org/danswick/83a8ddff7fb9193176a975a02a896792

**Get BBOX**
https://stackoverflow.com/questions/35673704/how-do-i-get-the-bounding-box-of-a-mapboxgl-geojsonsource-object

**measure**
https://www.mapbox.com/mapbox-gl-js/example/measure/

**Data Driven Style**
https://www.ryanbaumann.com/blog/2016/1/23/mapbox-gl-create-data-driven-styles

https://www.mapbox.com/mapbox-gl-js/api/
https://bl.ocks.org/andrewharvey/c1fdbebafe3fc46d743ba9514e4d64b2

**Color Building with height**
http://thinkingspatial.com/blog/

http://thinkingspatial.com/mapbox-gl-js-3d-buildings/


https://github.com/peterqliu/threebox
http://bl.ocks.org/boeric/f6ddea14600dc5093506

**Lidar**
https://bl.ocks.org/ryanbaumann/2f66eecfe687338a1c2331003e7ec950

## Data Viz
https://www.mapbox.com/mapbox-gl-js/example/live-update-feature/
https://www.mapbox.com/mapbox-gl-js/example/animate-point-along-line/

https://blogs.esri.com/esri/arcgis/2017/11/24/scene-viewer-point-cloud-smart-mapping/
http://desktop.arcgis.com/en/cityengine/latest/get-started/cityengine-whats-new.htm
http://cartographymaster.eu/wp-content/theses/2015_Dobraja_Thesis.pdf

https://gis.stackexchange.com/questions/173862/how-to-determine-when-mapbox-gl-js-flyto-has-arrived

## Mapbox + Digital Globe Maps
https://mapsapidocs.digitalglobe.com/docs/maps-api-mapbox-gl



**WMS tiles with vecotr tiles on MapboxGL**
http://bl.ocks.org/Sumbera/ba554bb5cc8dfe4d7866
* Image Overlay
https://www.mapbox.com/mapbox-gl-js/example/image-on-a-map/

**Mabpbox GL Mesh**
3D terrain insight using mapboxGL:-

https://blog.mapbox.com/bringing-3d-terrain-to-the-browser-with-three-js-410068138357
https://www.mapbox.com/bites/00332/#13.2701/69.505/20.7514/77.9588/27.6729
http://www.pheelicks.com/2014/03/rendering-large-terrains/


https://labs.strava.com/heatmap/#12.25/37.69460/55.71483/hot/run
https://blog.mapbox.com/global-elevation-data-6689f1d0ba65



  glyphs:"mapbox://fonts/mapbox/{fontstack}/{range}.pbf"
  https://api.mapbox.com/fonts/v1/mapbox/DIN%20Offc%20Pro%20Medium,Arial%20Unicode%20MS%20Regular/0-255.pbf?access_token=pk.eyJ1IjoidW5lcGdyaWQiLCJhIjoiY2lzZnowenUwMDAzdjJubzZyZ3R1bjIzZyJ9.uyP-RWjY-94qCVajU0u8KA


  https://blender.stackexchange.com/questions/62619/how-to-import-3d-buildings-from-openstreetmap-to-blender

http://demo.f4map.com/#lat=42.1405936&lon=-0.4082753&zoom=18&camera.theta=64.244&camera.phi=-35.982

## Forums
https://github.com/iTowns/itowns/issues/183
https://github.com/Oslandia/building-server


## OSM 3D
https://wiki.openstreetmap.org/wiki/3D_development
https://wiki.openstreetmap.org/wiki/Glosm

https://osmbuildings.org/blog/2018-03-21_3d_model_repository/
https://3dmr.eu/
https://osmbuildings.org/blog/2018-02-28_level_of_detail/
https://gitlab.com/n42k/3dmr

## Showcase and Similar Examples, References
https://github.com/adius/CityViz

## WebGL
http://www.senchalabs.org/philogl/demos.html
http://www.glge.org/
https://github.com/evanw/lightgl.js

## Commercials, Business Models
* [ArcGIS REST API](https://developers.arcgis.com/pricing/)
* [osmbuildings](https://osmbuildings.org/data/)
