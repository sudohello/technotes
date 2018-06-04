var entity = that.viewer.entities.add({
   model : {
     uri : "cesium/Apps/SampleData/models/17093806060776.gltf"
     ,modelMatrix :Cesium.Matrix4.IDENTITY
  }
});

**https://cesiumjs.org/NewYork/main.js**
https://s3.amazonaws.com/cesiumjs/3DTiles/NewYorkCityGml.zip
https://s3.amazonaws.com/cesiumjs/3DTiles/NewYork.zip
http://cesium.entwine.io/?resource=half-dome

https://mediatum.ub.tum.de/doc/1291310/file.pdf
http://cartographymaster.eu/wp-content/theses/2017_Moradi_Thesis.pdf

https://onesky.xyz/data-explorer/
https://github.com/wangzhongliang/cesium-network-routing

http://www.liedman.net/geojson-path-finder/

https://stackoverflow.com/questions/27473327/load-gltf-model-in-cesium-js
http://cubecities.blogspot.com/2015/04/a-how-to-guide-for-exploring-3d.html

http://svgjs.com/
https://github.com/svgdotjs/svg.js


https://www.hel.fi/helsinki/en/administration/information/general/3d/3d

http://zmapping.com/

https://www1.nyc.gov/site/doitt/initiatives/3d-building.page
http://docs.opengeospatial.org/per/17-046.html

**Key Phrases**
3D Tiles using AGI’s processing tool into Cesium

https://github.com/AnalyticalGraphicsInc/3d-tiles
https://cesium.com/presentations/files/3DTilesInAction.pdf


AR
https://support.glitch.com/t/suggestions-on-how-to-upload-a-collection-of-assets-that-need-to-be-in-a-fixed-structure/1191/13

3D Tiles

http://www.sitesee.io/news/3dtiles
http://www.xyht.com/spatial-itgis/add-3d-tiles-cesium-1-36-make-3d-virtual-scenes/
https://www.safe.com/integrate/cesium-3d-tiles/
https://www.npmjs.com/package/3d-tiles-tools

https://knowledge.safe.com/questions/47430/transform-gdb-model-to-cesium-3d-tiles.html

https://cesiumjs.org/demos/3DCityDB/


3D Tiler
https://groups.google.com/forum/#!topic/cesium-dev/xLkYIuku9hA
https://groups.google.com/forum/#!topic/cesium-dev/osXQ-TXtZHQ
https://groups.google.com/forum/#!topic/cesium-dev/zh6GvW9T7VE
It's up to you how you want to organize buildings among tiles. If the buildings have simple geometry it is usually a good idea to combine multiple into a single b3dm tile. Otherwise if the buildings are complex, they can split up into multiple tiles. In the end its less about buildings and more about geometry and how you wish to subdivide it.

There aren't too many publicly available tools that will convert source data into 3d-tiles yet. However we are working on some internal tools and would be glad to test out your data if you would like. You can contact me at slilley@agi.com.

Let us know if you have more 3D Tiles questions.

https://www.hel.fi/helsinki/en/administration/information/general/3d/view/view-the-models

## gltf viewers
* https://gltf-viewer.donmccurdy.com/
* https://pissang.github.io/clay-viewer/editor/
* https://sandbox.babylonjs.com/

## gltf models
https://www.8thwall.com/gltf/
https://github.com/AnalyticalGraphicsInc/cesium/issues/927

## CZML - Cesium Language
https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/CZML-Guide

b3dm is part of the 3D Tiles specification, and indeed b3dm uses glTF as its payload to deliver 3d geometry.

A single glTF file delivers a (relatively) small amount of localized 3D geometry, along with materials, textures, and other metadata needed to render it on a client. The 3D Tiles standard provides a mechanism to specify a hierarchy of geo-located glTFs at different resolutions. For example, a vehicle may be easily portrayed in a single glTF file, but a whole city with all of its buildings and trees would need to be broken up into 3D Tiles, using multiple glTF files internally.


## 3D City DB
https://github.com/3dcitydb
https://www.gis.bgu.tum.de/startseite/
**Demos**
http://www.3dcitydb.org/3dcitydb-web-map/1.4/3dwebclient/index.html?title=Berlin_Demo&batchSize=1&latitude=52.517479728958044&longitude=13.411141287558161&height=534.3099172951087&heading=345.2992773976952&pitch=-44.26228062802528&roll=359.933888621294&layer_0=url%3Dhttp%253A%252F%252Fwww.3dcitydb.net%252F3dcitydb%252Ffileadmin%252Fmydata%252FBerlin_Demo%252FBerlin_Buildings_rgbTexture_ScaleFactor_0.3%252FBerlin_Buildings_rgbTexture_collada_MasterJSON.json%26name%3DBrlin_Buildings_rgbTexture%26active%3Dtrue%26spreadsheetUrl%3Dhttps%253A%252F%252Fwww.google.com%252Ffusiontables%252FDataSource%253Fdocid%253D19cuclDgIHMqrRQyBwLEztMLeGzP83IBWfEtKQA3B%2526pli%253D1%2523rows%253Aid%253D1%26cityobjectsJsonUrl%3D%26minLodPixels%3D100%26maxLodPixels%3D1.7976931348623157e%252B308%26maxSizeOfCachedTiles%3D200%26maxCountOfVisibleTiles%3D200


http://www.3dcitydb.org/3dcitydb-web-map/1.4/ThirdParty/Cesium/Assets/IAU2006_XYS/IAU2006_XYS_15.json
http://www.3dcitydb.org/3dcitydb-web-map/1.4/ThirdParty/Cesium/Assets/approximateTerrainHeights.json

options = {
	active:true
	,cityobjectsJsonUrl:""
	,maxCountOfVisibleTiles:"200"
	,maxLodPixels:"1.7976931348623157e+308"
	,maxSizeOfCachedTiles:"200"
	,minLodPixels:"100"
	,name:"Brlin_Buildings_rgbTexture"
	,thematicDataUrl:"https://www.google.com/fusiontables/DataSource?docid=19cuclDgIHMqrRQyBwLEztMLeGzP83IBWfEtKQA3B&pli=1#rows:id=1"
	,url:"http://www.3dcitydb.net/3dcitydb/fileadmin/mydata/Berlin_Demo/Berlin_Buildings_rgbTexture_ScaleFactor_0.3/Berlin_Buildings_rgbTexture_collada_MasterJSON.json"
}

http://www.3dcitydb.net/3dcitydb/fileadmin/mydata/Berlin_Demo/Berlin_Buildings_rgbTexture_ScaleFactor_0.3/Berlin_Buildings_rgbTexture_collada_MasterJSON.json
{
	"version": "1.0.0",
	"layername": "Berlin_Buildings_rgbTexture",
	"fileextension": ".kml",
	"displayform": "collada",
	"minLodPixels": 140,
	"maxLodPixels": -1,
	"colnum": 303,
	"rownum": 242,
	"bbox":{ 
		"xmin": 13.081395902431,
		"xmax": 13.761645524869,
		"ymin": 52.3321529013468,
		"ymax": 52.6663731823943
	}
}

https://masterschool.eitdigital.eu/about-us/news-events/article/student-journey-from-a-finnish-start-up-to-san-francisco/



## References
* The best workflows and tips for cinematographers and filmmakers:
	- https://wolfcrow.com/

## Interesting Web Tech URLs
https://simpl.info/index.html

## Vector Based Utilities
https://www.netvlies.nl/tips-updates/overig/cases/creating-an-interactive-svg-metro-map-with-jointjs/

https://github.com/LukeOwlclaw/SvgNaviMap

**Research Papers on Indoor Maps**
https://www.researchgate.net/publication/269306547_Simple_indoor_routing_on_SVG_maps

A Journey from IFC Files to Indoor Navigation


https://github.com/wangzhongliang/cesium-network-routing

https://onesky.xyz/data-explorer/

http://hg.grauw.nl/grauw-lib/file/tip/src/uri.js
http://www.grauw.nl/
https://github.com/gregjacobs/Autolinker.js
https://github.com/kvz/phpjs
https://github.com/Pomax/fontmetrics.js
http://knockoutjs.com/
https://github.com/SteveSanderson/knockout-es5
NoSleep.js v0.5.0 - git.io/vfn01
chroma.js - JavaScript library for color conversions
ColorBrewer colors for chroma.js
https://github.com/jquery/PEP