---
title: Book Notes - Learning Geospatial Analysis with Python, 2nd Edition
---

**Table of Contents**
* TOC
{:toc}


## Book Notes - Learning Geospatial Analysis with Python

## Kewords
* geographic search engines
* spatio, temporal geospatial database design
* standards
  * ISO 19115-1,19115-2

## Organisations
* OSM - open street map
* OGC - Open Geospatial Consortium
  * https://www.opengeospatial.org/standards/cat
  * CSW - Catalog Service for the Web: to manage metadata


## Python Geospatial related Libraries
* [pycsw](http://pycsw.org)
  - pycsw is an OGC CSW server implementation written in Python. Started in 2010 (more formally announced in 2011), p
  - pycsw allows for the publishing and discovery of geospatial metadata via numerous APIs (CSW 2/CSW 3, OpenSearch, OAI-PMH, SRU), providing a standards-based metadata and catalogue component of spatial data infrastructure
  - pycsw is Open Source, released under an MIT license, and runs on all major platforms (Windows, Linux, Mac OS X)

### Chapter-1:
Knowledge of geospatial concepts and data as well as the ability to build custom geospatial processes is where the geospatial work in the near future lies.

However, in geospatial analysis, the concepts modeled are, well, real-world objects! The domain of geospatial analysis is the Earth and everything on it. Trees, buildings, rivers, and people are all examples of objects within a geospatial system.


Geospatial analysis helps people make better decisions. It doesn't make the decision for you, but it can answer critical questions that are at the heart of the choice to be made and often cannot be answered any other way.

Geospatial analysis is the best approach to understanding our world more efficiently and deeply.


* **Thematic maps**
  * They have been used as guides to start (and end) wars, stop deadly diseases in their tracks, win elections, feed nations, fight poverty, protect endangered species, and rescue those impacted by disaster. Thematic maps may be the most useful models ever created.
  * Some example fields include spatial representation, temporal extent, and lineage
* **Spatial Indexing**
* **Metadata**
  * Geospatial metadata can be represented by several possible standards. One of the most prominent standards is the international standard, ISO 19115-1, which includes hundreds of potential fields to describe a single geospatial dataset.
  * Additionally, the ISO 19115-2 includes extensions for geospatial imagery and gridded data.
  * **geographics search engines**: Modern metadata can be ingested by geographic search engines making it potentially discoverable by other systems automatically
* **Map projections**
  * If you take any three-dimensional object and flatten it on a plane, such as your screen or a sheet of paper, the object is distorted.
  * There is no one-size-fits-all solution to map projections
  * The choice of projection is always a compromise of gaining accuracy in one dimension in exchange for error in another
  * Projections are typically represented as a set of over 40 parameters as either XML or a text format called Well-Known Text (WKT), which is used to define the transformation algorithm
  * The **International Association of Oil & Gas Producers (IOGP)** maintains a registry of the most known projections. The organization was formerly known as the **European Petroleum Survey Group (EPSG)**
  * The entries in the registry are still known as **EPSG codes**
  * At the last count, this registry contained over 5,000 entries.
  * Earlier days, most geospatial data formats do not provide a way to store the projection information. This information is stored in an ancillary file as text or XML usually
  * Now, nearly every data format has added a metadata format that defines the projection or places it in the file header if supported.
  * **Google Mercator** OR **Web Mercator**: **EPSG:3857 (or the deprecated EPSG:900913)**
    - used for Google Maps
  * Geospatial portal projects such as OpenStreetMap.org and NationalAtlas.gov have consolidated datasets for much of the world in common projections.
* **Geodetic Datum or Datum**
  * Closely related to map projections are geodetic datums.
  * A datum is a model of the Earth's surface used to match the location of features on the Earth to a coordinate system. One common datum is called WGS 84 that is used by GPS devices.
* **Rendering**
  * Geographic data including points, lines, and polygons are stored numerically as one or more points, which come in (x,y) pairs or (x,y,z) tuples. The x represents the horizontal axis on a graph. The y represents the vertical axis. The z represents terrain elevation
  * Another important factor is screen coordinates versus world coordinates. Geographic data is stored in a coordinate system representing a grid overlaid on the Earth, which is three-dimensional and round.
  * Screen coordinates, also known as pixel coordinates, represent a grid of pixels on a flat, two-dimensional computer screen
  * Mapping x and y world coordinates to pixel coordinates is fairly straightforward and involves a simple scaling algorithm.
  * However, if a z coordinate exists, then a more complicated transform must be performed to map coordinates from three-dimensional space to a two-dimensional plane. These transformations can be computationally costly and therefore slow if not handled correctly.
  * Lossless methods use tricks to reduce the file size without discarding any data
  * Lossy compression algorithms reduce the file size by reducing the amount of data in the image while avoiding a significant change in the appearance of the image.
* **Images as Data**
  * **Any numerical array can be represented on a computer as an image**
  * It is important in geospatial analysis to think of images as a numeric array because mathematical formulas are used to process them.
  * In remotely sensed images, each pixel represents both space (location on the Earth of a certain size) and the reflectance captured as light reflected from the Earth at this location into space. So, each pixel has a ground size and contains a number representing the intensity.
  * As each pixel is a number, we can perform mathematical equations on this data to combine data from different bands and highlight specific classes of objects in the image.
  * If the wavelength value is beyond the visible spectrum, we can highlight features not visible to the human eye. Substances such as chlorophyll in plants can be greatly contrasted using a specific formula called Normalized Difference Vegetation Index (NDVI).
* **Remotesensing and Color**
  * Computer screens display images as combinations of Red, Green, and Blue (RGB) to match the capability of the human eye. Satellites and other remote sensing imaging devices can capture light beyond this visible spectrum
  * On a computer, wavelengths beyond the visible spectrum are represented in the visible spectrum so that we can see them. These images are known as **false color** images
  * In remote sensing, for instance, **infrared light makes moisture highly visible**. This phenomenon has a variety of uses such as monitoring ground saturation during a flood or **finding hidden leaks in a roof** or levee.


**Different types of `essential` GIS processes commonly used in geospatial analysis**
* **Data structures**
  * consisting of, at a minimum, an x horizontal value and a y vertical value to represent a location on the Earth
* a point may also contain a z value
* ancillary values are possible including measurements or timestamps
* Vector data typically represents topographic features better than raster data
* Vector data has better accuracy potential and is more precise.
* However, to collect vector data on a large scale is also traditionally more costly than raster data.


**Bounding Box** and **Convex Hull**
* Two other important terms related to vector data structures are bounding box and
convex hull.
  * The bounding box or minimum bounding box is the smallest possible square that contains all of the points in a dataset.
  * The convex hull of a dataset is similar to the bounding box, but instead of a square, it is the smallest possible polygon that can contain a dataset.


**Buffer**
* A buffer operation can be applied to spatial objects including points, lines, or
polygons
* This operation creates a polygon around the object at a specified distance.
* **Usage examples**
  * **Buffer operations** are used for **proximity analysis**, for example, establishing a safety zone around a dangerous area


**Dissolve**
* A dissolve operation creates a single polygon out of **adjacent polygons**
* **Usage examples**
  * A common use for a dissolve operation is to merge two adjacent properties in a tax database that have been purchased by a single owner.
  * Dissolves are also used to simplify data extracted from remote sensing


**Generalize**
* Objects that have more points than necessary for the geospatial model can be generalized to reduce the number of points used to represent the shape.
* It is a data optimization technique to simplify data for the efficiency of computing or better visualization.
* **Usage example**
  * his technique is useful in web-mapping applications. Computer screens have a resolution of 72 dots per inch (dpi). Highly-detailed point data, which would not be visible, can be reduced so that less bandwidth is used to send a visually equivalent map to the user:


**Intersection**
* An intersection operation is used to see if one part of a feature intersects with one or more features.
* **Usage example**
  * This operation is for spatial queries in **proximity analysis** and is often a follow-on operation to a buffer analysis


**Merge**
* A merge operation combines two or more non-overlapping shapes in a single multishape object
* **Multishape objects** mean that the shapes **maintain separate geometries** but are **treated as a single feature** with a **single set of attributes** by the GIS


**Point in polygon**
* A fundamental geospatial operation is checking to see whether a point is inside a polygon
* If the point is on the boundary of the polygon, it is considered inside
* can be very slow on a large number of points
* The most common and efficient algorithm to detect if a point is inside a polygon is called the **ray casting** algorithm
* **Usage example**
  * This one operation is the atomic building block of many different types of spatial queries


**Union**
* It is similar to dissolve, but in this case, the polygons are **overlapping** as opposed to being adjacent
* **Usage example**
  * This operation is used to clean up automatically-generated feature datasets from remote sensing operations

**Join**
* spatial joins, combine the attributes to two features in the same way that you do in a SQL join, but the relation is based on the spatial proximity of the two features.


**Geospatial rules about polygons**
* There are several general rules of thumb regarding polygons that are different from mathematical descriptions of polygons
* Polygons must have at least four points—the first and last points must be the same
* A polygon boundary should not overlap itself
* A polygon in a layer inside another polygon is considered as a hole in the underlying polygon

* A polygon is by definition a closed shape, which means that the first and last vertices of the polygon are identical
* The data format that you use to store your geospatial data may also dictate how polygons are defined

**Image Band mathematics**


* In array math, arrays are treated as single units, which are added, subtracted, multiplied, and divided
* in an array, the corresponding numbers in each row and column across multiple arrays are computed simultaneously


### Chapter-6: Python and Remote Sensing
It's important to note that NumPy references the array locations as y,x (row, column) instead of the usual x, y (column, row) format that we work with in spreadsheets and other software:
* load the image to a NumPy array using gdal_array , and then we'll immediately save it back to a new GeoTIFF file
Images in NumPy are multidimensional arrays in the order of band, height, and width.


## Ideas
* In remote sensing, for instance, **infrared light makes moisture highly visible**. This phenomenon has a variety of uses such as monitoring ground saturation during a flood or **finding hidden leaks in a roof** or levee.
  * This concept can be potentially used for **indoor scanning and mapping to find out leaks in the building**
