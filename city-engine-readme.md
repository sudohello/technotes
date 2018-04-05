/*
Title: City Engine
Decription: City Engine
Author: Bhaskar Mangal
Date: 17th Feb 2018
Tags: City Engine
*/

# City Engine

## Tutorials
* http://desktop.arcgis.com/en/cityengine/latest/tutorials/tutorial-6-basic-shape-grammar.htm

## 3d Model Samples
* https://free3d.com/3d-model/venice-14698.html

## Troubleshooting
* **Importing M3d Models**
- https://geonet.esri.com/thread/64410

## References
* https://sites.google.com/site/surendragurjariitr/home

virtual visualization of Archeological site of India
create a virtual 3D city model by using procedural modeling

image based virtual 3D campus modeling
Image based modeling is easy than Grammar based or rule based 3D modeling

CityEngine works mainly on Grammar based modeling

http://www.esri.com/esri-news/arcuser/winter-2016/creating-a-3d-campus-scene-using-esri-cityengine
http://www.gismanual.com/ce_fromscratch/


## City Engine Scripts - MMI

++**Errors**++
[arcgispro-py3] C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3>python
 D:\City_Engine\scripts\Update_bounds_Of_Grid.py
D:\City_Engine\projects\whitefield\rawdata\I5_bu_region_region\I5_grid_region_re
gion.shp
Make Fields: SUCCESS
ERROR: module 'arcpy' has no attribute 'mapping'
UPDATE Bounds: FAIL
module 'arcpy' has no attribute 'mapping'
Script completed

[arcgispro-py3] C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3>python
 D:\City_Engine\scripts\Update_bounds_Of_Grid.py
D:\City_Engine\projects\whitefield\rawdata\I5_bu_region_region\I5_grid_region_re
gion.shp
ERROR: module 'arcpy.mp' has no attribute 'MapDocument'
UPDATE Bounds: FAIL
module 'arcpy.mp' has no attribute 'MapDocument'
Script completed

Solution:
=============


http://pro.arcgis.com/en/pro-app/arcpy/mapping/migratingfrom10xarcpymapping.htm
- arcpy.mapping.MapDocument(mxd_path) needs to be replaced with arcpy.mp.ArcGISProject(aprx_path)

------------
[arcgispro-py3] C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3>python
 D:\City_Engine\scripts\Update_bounds_Of_Grid.py
D:\City_Engine\projects\whitefield\rawdata\I5_bu_region_region\I5_grid_region_re
gion.shp
ERROR: D:\City_Engine\projects\whitefield\rawdata\I5_bu_region_region\Untitled.m
xd
UPDATE Bounds: FAIL
D:\City_Engine\projects\whitefield\rawdata\I5_bu_region_region\Untitled.mxd
Script completed


Solution:
=============
- create new project file in the data directory and use the project file name in the script

**MXD FIle**
MXD is a file extension for a map document used by ArcMap. ArcMap is a component of ArcGIS, a GIS (geographic information system) software suite. GIS enables you to envision the geographic aspects of a body of data.

https://community.esri.com/thread/118201

Map documents (mxd) are part of ArcGIS Desktop, not ArcGIS Pro.  ArcGIS Pro is organized differently and has Project files (aprx), similar to the old ArcView Project files (apr).

 

Once you create a new ArcGIS Pro project, you can import MXDs as maps within the project.





[arcgispro-py3] C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3>python
 D:\City_Engine\scripts\Update_bounds_Of_Grid.py
D:\City_Engine\projects\whitefield\rawdata\I5_bu_region_region\I5_grid_region_re
gion.shp
ERROR: module 'arcpy.mp' has no attribute 'ListDataFrames'
UPDATE Bounds: FAIL
module 'arcpy.mp' has no attribute 'ListDataFrames'
Script completed

https://pro.arcgis.com/en/pro-app/arcpy/mapping/migratingfrom10xarcpymapping.htm


**Tutorials**
1. Arcpy.mp
http://pro.arcgis.com/en/pro-app/arcpy/mapping/introduction-to-arcpy-mp.htm

2. Migration from Arc GIS Desktop to Arc GIS PRO
https://community.esri.com/thread/206207-arcpy-arcgis-pro
http://pro.arcgis.com/en/pro-app/arcpy/mapping/migratingfrom10xarcpymapping.htm
http://desktop.arcgis.com/en/arcmap/latest/analyze/arcpy-mapping/listdataframes.htm