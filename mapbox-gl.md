/*
Title: Mapbox GL
Decription: Mapbox GL
Author: Bhaskar Mangal
Date: 12th Feb 2018
Tags: Mapbox GL
*/

** Table of Contents**

[TOC]

# Mapbox GL
```javascript
tileDomain = (window.location.hostname.includes("strava") ? 'http://{s}-globalheat.strava.com' :'http://' + window.location.hostname + ':9000');

tileDomains = ['http://' + window.location.hostname + ':9000']

if (window.location.hostname.includes("labs")) {
  tileDomains = [
    '//heatmap-external-a.strava.com',
    '//heatmap-external-b.strava.com',
    '//heatmap-external-c.strava.com'
  ]
}
tileDomains.map( function(d) { return d + path } )

 map.once('sourcedata', addHeatLayer)


   afterLayer = false
    map.style.stylesheet.layers.forEach(function(layer) {
      if (layer.id == 'waterway-label') {
        afterLayer = layer.id
      }
    })

    map.addLayer(getLayer(), afterLayer)
```

1. Layer Sequencing
2. Toggle Different Base Map Layers like raster/satellite, to vector MMI, to vector Mapbox
3. Popup handling

**UI:**
1. Layer Controls
2. Style Controls - Custom styling control

**Use case to be implemented based on challanges**
- show the base layer style switcher only when the base layer style are loaded and applied.
- favicon to be introduced (is it possible to use SVG favicon?)
- svg icons framework
- debug panel
	- Underline data properties/attributes: json, table
	- Derived from geodata structural properties:
		- Area information [ Sq. Meters; Sq. Kilometers; Sq. Feet	15907.40; Acres	0.37; Sq. Miles	0.00 ]
	  -	Volume information
- Info panel for different layers
- lat-lon location under mouse move: 6 digit/10 digit display
- Edit Tools

## MapBoxGL Games
* https://blog.kuntzsch.me/stepping-up-my-web-mapping-game-mapbox-gl-and-d3/
* https://blog.mapbox.com/make-your-own-cartography-game-with-mapbox-gl-at-our-workshop-in-bengaluru-2d3a5e1cd680
* https://bl.ocks.org/DeEgge/ba386d71b5d0157e2195da02a3d4453b

## Customization
**Layer Control**
* http://leafletjs.com/examples/layers-control/
* https://gis.stackexchange.com/questions/130471/how-to-switch-base-layer-programmatically-in-mapbox-leaflet
* https://github.com/mapbox/mapbox-gl-js/issues/5489
* https://github.com/mapbox/mapbox-gl-js/issues/3979

## Working with geojson
* https://www.mapbox.com/help/working-with-large-geojson-data/
* http://bl.ocks.org/ryanbaumann/04c442906638e27db9da243f29195592/33e8d3520feecf0912f489689ca4a5c01bdfcbfc
* https://github.com/osm2vectortiles/osm2vectortiles
* https://openmaptiles.org/
* https://github.com/mapbox/mapbox-gl-leaflet

**Draw Control**
* https://bl.ocks.org/danswick/083a0b48c2cc78c4a08d
* https://github.com/mapbox/mapbox-gl-draw
* https://github.com/mapbox/mapbox-gl-draw/blob/master/docs/MODES.md#available-custom-modes

**Drag and drop Geojson Files**
* https://bl.ocks.org/fxi/b7f1af5981432296bfafec70a95fd9b6

**Custom Control**
* https://codepen.io/sergei-zelinsky/pen/gGOZjE
* http://www.material-ui.com/#/components/svg-icon

**Pitch Control**
* http://fuzzytolerance.info/blog/2017/01/30/Pitch-toggle-control-for-Mapbox-GL-JS/

* **Changing BaseMap**
https://github.com/mapbox/mapbox-gl-js/issues/2267

* **Add WMS Layer**
* https://www.mapbox.com/mapbox-gl-js/example/wms/
* http://www.vidteq.com/vs/tilecache.php?LAYERS=BANG_BUTTERFLY&FORMAT=image%2Fpng&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&STYLES=&SRS=EPSG%3A4326&BBOX=77.34375,12.83203125,77.51953125,13.0078125&WIDTH=256&HEIGHT=256
* http://www.vidteq.com/vs/tilecache.php?LAYERS=BANG_BUTTERFLY&FORMAT=image/png&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&STYLES=&SRS=EPSG:4326&BBOX={bbox-epsg-4326}&WIDTH=256&HEIGHT=256
* https://geodata.state.nj.us/imagerywms/Natural2015?bbox={bbox-epsg-3857}&format=image/png&service=WMS&version=1.1.1&request=GetMap&srs=EPSG:3857&width=256&height=256&layers=Natural2015'

**Forums**
* https://github.com/mapbox/mapbox-gl-js/issues/3552
* [pitch is hardcoded to 60 because of tile loading and label rendering issues]
    * https://github.com/mapbox/mapbox-gl-js/issues/3731

**Style Layer Picker**
```html
data:image/svg+xml;charset=utf-8,<svg viewBox='0 0 20 20' xmlns='http://www.w3.org/2000/svg'><title>HUD_basemap_icon</title><path d='M9.325 11.64c.405.283.945.283 1.35 0l8.179-4.752a.338.338 0 0 0-.043-.581l-8.285-3.183a1.184 1.184 0 0 0-1.052 0L1.189 6.307a.338.338 0 0 0-.043.581l8.179 4.753zm9.486-.71l-2.238-1.11-5.152 2.994a2.572 2.572 0 0 1-1.421.424 2.58 2.58 0 0 1-1.421-.424L3.43 9.818 1.19 10.93a.338.338 0 0 0-.044.581l8.179 5.678c.405.282.945.282 1.35 0l8.179-5.678a.337.337 0 0 0-.043-.58z' fill='%23242528' fill-rule='evenodd'/></svg>
```
* https://www.mapillary.com/app/?lat=12.291465261038326&lng=41.63047318341364&z=1.5&mapStyle=esri

**Terrain & Elevation**
* https://www.mapbox.com/mapbox-gl-js/example/toggle-layers/
* https://blog.mapbox.com/satellite-map-with-contours-ff1b1ff735e6
* https://stackoverflow.com/questions/38467973/mapbox-gl-js-contour-lines-elevation
* https://github.com/mapbox/mapbox-studio-satellite-outdoors.tm2
* https://github.com/mapbox/mapbox-gl-styles/blob/1ac5e784907e50c2284c7cc59169ac64ce4e885c/styles/satellite-v7.json#L713-L739

**3D Terrain with Three.js**
- https://blog.mapbox.com/bringing-3d-terrain-to-the-browser-with-three-js-410068138357
- https://www.mapbox.com/bites/00332/#13.4682/36.3524/-112.5928/-138.4134/0.0001
- https://www.mapbox.com/blog/terrain-rgb/
- https://openmaptiles.github.io/klokantech-terrain-gl-style/#13.25/47.0819/8.5846/-172/47
- https://openmaptiles.github.io/klokantech-terrain-gl-style/style-cdn.json
- https://openmaptiles.com/contours/
- https://www.mapbox.com/vector-tiles/mapbox-terrain/
- https://free.tilehosting.com/data/v3.json?key=RiS4gsgZPZqeeMlIyxFo
```html
  <script>
      mapboxgl.setRTLTextPlugin('https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-rtl-text/v0.1.0/mapbox-gl-rtl-text.js');
      var map = new mapboxgl.Map({
        container: 'map',
        style: 'style-cdn.json',
        attributionControl: true,
        hash: true
      });
      map.addControl(new mapboxgl.NavigationControl());
  </script>
```

**Cool Examples**
* https://www.mapbox.com/mapbox-gl-js/example/scroll-fly-to/
* https://www.mapbox.com/help/make-a-heatmap-with-mapbox-gl-js/
* https://blog.mapbox.com/labels-for-navigation-in-mapbox-gl-d9220fa51762
* https://blog.mapbox.com/labels-for-navigation-in-mapbox-gl-d9220fa51762
* https://www.mapbox.com/mapbox-gl-js/example/hover-styles/

**Toggle and restricted bounds**
* http://geo-odyssey.com/links/stack.html
* https://www.mapbox.com/help/define-camera/

**Height**
* http://thinkingspatial.com/category/uncategorized/
* https://tutel.me/c/programming/questions/43891269/rotated+points+in+mapbox+are+skewed
* https://javascript.wekeepcoding.com/article/10428523/mapbox-gl-js%3A+Adjust+visible+area+%26+bearing+to+a+given+line%2C+for+a+given+pitch
* https://www.getbounds.com/blog/data-driven-styling-3d-polygons-and-vector-tiles-with-mapbox-gl-js/

**To look**
* https://www.ovrdc.org/apps/accident-explorer.html#8.61/39.1469/-83.4514
* https://www.ovrdc.org/apps/block-group-explorer.html#6.61/40.217/-80.713

## Data Driven Colors and Popups
* https://gis.stackexchange.com/questions/195202/mapbox-gl-and-styling-for-data-driven-labels

**Map Markers**
* https://bl.ocks.org/danswick/4906b495e0b206758f71
* https://www.mapbox.com/mapbox-gl-js/example/custom-marker-icons/

**Embedding YouTube Video URLs**
* https://stackoverflow.com/questions/19836015/youtube-url-in-video-tag
* https://stackoverflow.com/questions/28539536/mapbox-non-geographic
```
Refused to display 'https://www.youtube.com/watch?v=aONXZopnY2c' in a frame because it set 'X-Frame-Options' to 'SAMEORIGIN'.

Refused to display in a frame because it set 'X-Frame-Options' to 'SAMEORIGIN'.
```

**Save GeoJSON**
* https://bl.ocks.org/danswick/36796153bd86ce982a59043cbe0ac8f7

## Icons & Fonts
* https://github.com/mapbox/mapbox-gl-js/issues/3605
* http://fontastic.me/
* https://stevebennett.me/category/mapmaking/

## NPM based development
* https://www.npmjs.com/package/@ivelander/mapbox-gl

## Underground
* https://github.com/elliotleelewis/TubeMap

## 3D Floor Changer
* http://www-personal.umich.edu/~yonghah/rooms3d/

## MapboxGL City Examples with New UI Features
* https://developmentactivity.melbourne.vic.gov.au/
* https://data.melbourne.vic.gov.au/Property-Planning/3D-Development-Activity-Model-Footprints/def8-4wbt
* https://data.melbourne.vic.gov.au/
* https://ubilabs.net/en/news/data-driven-raster-layer-mapbox-lg-2016-09-05
* https://www.behance.net/gallery/24276859/City-Layouts
* https://density.ubilabs.net/

## urban-surveillance
* http://www.sarahmakesmaps.com/blog/2014/7/17/urban-surveillance
* https://www.skylinewebcams.com/en/webcam/malta/malta/traffic/traffic-cam15.html
* http://www.btis.in/transport/traffic

## Noise Pollution
* https://github.com/lukasmartinelli/osm-noise-pollution
* http://lukasmartinelli.ch/gis/2016/04/03/openstreetmap-noise-pollution-map.html
* http://lukasmartinelli.ch/maps/noise-pollution.html#12.16/47.3805/8.5341
* `mapbox://styles/morgenkaffee/cimi6phf0007wcem3cyr9cl3o`

## Directions
* https://www.mapbox.com/help/how-directions-work/

## Raster in Mapbox GL
* https://medium.com/@Scarysize/data-driven-raster-layer-with-mapbox-gl-bdb3b747ae22

## maptalks js
* https://maptalks.org/

## Tiling
* http://www.azimuth1.com/blog/sar-topo-tech-notes.html
* https://github.com/klokantech/maputnik
* https://stackoverflow.com/questions/31487520/mapbox-gl-using-external-maps

## Traffic
* https://github.com/mapbox/mapbox-gl-traffic
* https://bl.ocks.org/danswick/f4aa01a046385eb69313499b7934f425
* https://www.mapbox.com/vector-tiles/mapbox-traffic-v1/

## Mapbox V/s Google
* https://nextjuggernaut.com/blog/google-vs-mapbox/

## Query Features
* https://ovrdc.github.io/gis-tutorials/mapbox/03-query-features/#4/39.94/-95.52

## Map Designs
* https://ovrdc.github.io/
* https://github.com/ovrdc/material-maps
* https://ovrdc.github.io/material-maps/

## MapboxGl plugins
* https://github.com/lukasmartinelli/mapbox-gl-inspect

## Google Maps Enterprise
* https://enterprise.google.com/maps/pricing/

## SDKs on MapboxGL
* https://developers.airmap.com/v2.0/docs/customize-the-map
* https://sdk.boundlessgeo.com/filter/index.html
* https://blog.mapbox.com/creating-vector-tiles-from-raster-datasets-f8c9dc652c97

## Mapbox API
* https://www.mapbox.com/api-documentation/
* https://www.mapbox.com/blog/tags/weather/

## AR - Augmented Reality with location based applications
* https://blog.mapbox.com/mapbox-ar-2f065374eacb

## Extra Reading
http://chairnerd.seatgeek.com/vector-venue-maps-using-mapboxgl/

## Data Driven Styling
* https://blog.mapbox.com/announcing-expressions-in-gl-js-a72b55d0a6af
* https://www.mapbox.com/help/mapbox-gl-js-expressions/
* https://www.mapbox.com/mapbox-gl-js/style-spec/#expressions-interpolate
* https://www.mapbox.com/mapbox-gl-js/style-spec/#expressions
* https://www.mapbox.com/mapbox-gl-expressions/
* https://medium.com/uber-design/crafting-data-driven-maps-b0835b620554
1. Scatter plots
2. Hex Bins
	- great for showing density

- trick is to find following at different zome levels:
	- sizing
	- opacity
	- stroke thickness
- color scales
	- core brand colors (Aqua) as the primary
	- **sequential color scale**:
		- to accent the extents (highs and lows)
	- **diverging color scale**:
		- that is great when you want to accent the mean of your dataset and expose data that significantly ‘diverge’ from the norm.

## Mapbox GL Style Specifications
- https://github.com/mapbox/mapbox-gl-js/blob/master/src/style-spec/reference/v8.json#L161
- https://github.com/mapbox/mapbox-gl-js/issues/3360
**Metadata Examples**
- https://github.com/mapbox/mapbox-gl-styles/blob/master/styles/bright-v8.json
```javascript
  Style.prototype.serialize = function serialize () {
        var this$1 = this;

        return util.filterObject({
            version: this.stylesheet.version,
            name: this.stylesheet.name,
            metadata: this.stylesheet.metadata,
            light: this.stylesheet.light,
            center: this.stylesheet.center,
            zoom: this.stylesheet.zoom,
            bearing: this.stylesheet.bearing,
            pitch: this.stylesheet.pitch,
            sprite: this.stylesheet.sprite,
            glyphs: this.stylesheet.glyphs,
            transition: this.stylesheet.transition,
            sources: util.mapObject(this.sourceCaches, function (source) { return source.serialize(); }),
            layers: this._order.map(function (id) { return this$1._layers[id].serialize(); })
        }, function (value) { return value !== undefined; });
    };

        StyleLayer.prototype.serialize = function serialize () {
        var output       = {
            'id': this.id,
            'type': this.type,
            'source': this.source,
            'source-layer': this.sourceLayer,
            'metadata': this.metadata,
            'minzoom': this.minzoom,
            'maxzoom': this.maxzoom,
            'filter': this.filter,
            'layout': this._unevaluatedLayout && this._unevaluatedLayout.serialize(),
            'paint': this._transitionablePaint && this._transitionablePaint.serialize()
        };

        if (this.visibility === 'none') {
            output.layout = output.layout || {};
            output.layout.visibility = 'none';
        }

        return util.filterObject(output, function (value, key) {
            return value !== undefined &&
                !(key === 'layout' && !Object.keys(value).length) &&
                !(key === 'paint' && !Object.keys(value).length);
        });
    };
```

**OnClick**
* https://gis.stackexchange.com/questions/186533/highlight-feature-with-click-in-mapbox-gl
* http://thinkingspatial.com/mapbox-gl-js-click-and-hover-events/
* https://www.mapbox.com/mapbox-gl-js/example/queryrenderedfeatures-around-point/
* https://stackoverflow.com/questions/42978952/how-to-find-all-layers-in-mapboxgl-ultimately-i-want-to-show-custom-layer-only?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

**Query Similar Features**
* https://www.mapbox.com/mapbox-gl-js/example/query-similar-features/
* querySourceFeatures
```
// Query all rendered features from a single layer
Map.prototype.queryRenderedFeatures = function queryRenderedFeatures (geometry    
```
* https://www.mapbox.com/mapbox-gl-js/example/using-box-queryrenderedfeatures/
```
@param {string} [options.localIdeographFontFamily=null] If specified, defines a CSS font-family
```

## MapboxGL Indoor Map
* https://bl.ocks.org/danswick/e25b783434a7c52ee8e2

## MapboxGL JS snippets

```javascript
.OpenButton[_ngcontent-axr-52] {
    background-color: rgba(33,43,54,.3);
    background-image: url(data:image/svg+xml;charset=utf-8,%3Csvg viewBox='0 0 20 20' xmlns='http://w….877 0 0 1 4 6.117v-.234z' fill='%23FFF' fill-rule='evenodd'/%3E%3C/svg%3E);
    background-position: 50%;
    background-repeat: no-repeat;
    background-size: 20px 20px;
    border-radius: 30px;
    height: 30px;
    width: 30px;
}

.LayerIcon[_ngcontent-axr-4] {
    margin: 5px 0 0 5px;
    width: 20px;
    height: 20px;
    background: url(data:image/svg+xml;charset=utf-8,%3Csvg viewBox='0 0 20 20' xmlns='http://w…37.337 0 0 0-.043-.58z' fill='%23242528' fill-rule='evenodd'/%3E%3C/svg%3E);
}
```
* https://www.mapbox.com/mapbox-gl-js/example/mapbox-gl-draw/
* https://www.mapbox.com/mapbox-gl-js/example/playback-locations/
* https://www.mapbox.com/mapbox-gl-js/example/toggle-layers/
```javascript
    map.addLayer({
        'id': 'museums',
        'type': 'circle',
        'source': 'museums',
        'layout': {
            'visibility': 'visible'
        },
        'paint': {
            'circle-radius': 8,
            'circle-color': 'rgba(55,148,179,1)'
        },
        'source-layer': 'museum-cusco'
    });
```
* https://www.mapbox.com/mapbox-gl-js/example/heatmap-layer/
```
    loadURL(url        , options   
                           
                            
      = {}) {
        this.fire('dataloading', {dataType: 'style'});

        const validate = typeof options.validate === 'boolean' ?
            options.validate : !mapbox.isMapboxURL(url);

        url = mapbox.normalizeStyleURL(url, options.accessToken);
        const request = this.map._transformRequest(url, ajax.ResourceType.Style);

        ajax.getJSON(request, (error, json) => {
            if (error) {
                this.fire('error', {error});
            } else if (json) {
                this._load((json     ), validate);
            }
        });
    }
    
    loadURL(url        , options   
                           
                            
      = {}) {
        this.fire('dataloading', {dataType: 'style'});

        const validate = typeof options.validate === 'boolean' ?
            options.validate : !mapbox.isMapboxURL(url);

        url = mapbox.normalizeStyleURL(url, options.accessToken);
        const request = this.map._transformRequest(url, ajax.ResourceType.Style);

        ajax.getJSON(request, (error, json) => {
            if (error) {
                this.fire('error', {error});
            } else if (json) {
                this._load((json     ), validate);
            }
        });
    }
```

## Layer Ordering
* https://github.com/mapbox/mapbox-gl-js/issues/1349
* https://bl.ocks.org/ryanbaumann/e5cd12a01ef72ab620a2a58b71b1aa6b/38d6cdb6fe1ca54b17ed30dc8db77fb550a99d3d

## OpenMapTiles in MapboxgL
* https://openmaptiles.org/docs/style/mapbox-gl-style-spec/
* http://docs.geoserver.org/stable/en/user/styling/mbstyle/reference/spec.html

## web tools
* https://github.com/mapbox/geojson.io
* http://gree.github.io/tesspathy/

## WebApp Security
**XSS**
* https://haacked.com/archive/2009/06/25/json-hijacking.aspx/
* https://betterexplained.com/articles/using-json-to-exchange-data/

## Environment API
**Weather**
https://weather.com/en-IN/weather/interactive/l/INKA0310:1:IN?layer=clouds
**weather-along-your-route**
* https://blog.mapbox.com/map-the-weather-along-your-route-ae5d6d89e1f4
* https://www.mapbox.com/bites/00328/#6.5/38.508/-121.456

## Mapbox GL Different Eye Poping Stlye Examples
- [Medieval Melbourne](https://bl.ocks.org/stevage/eef4001fe752c7c6b82af3237a102b8c)
    - blog: https://stevebennett.me/tag/mapbox/

## Time based mapbox gl examples
- https://www.mapbox.com/help/show-changes-over-time/
http://bl.ocks.org/ryanbaumann/04c442906638e27db9da243f29195592

## Conditions
- https://blog.mapbox.com/announcing-expressions-in-gl-js-a72b55d0a6af
- https://www.mapbox.com/mapbox-gl-js/style-spec/#expressions-variable-binding
```
["has", string]


["case",
    condition: boolean, output: OutputType, condition: boolean, output: OutputType, ...,
    default: OutputType
]: OutputType

[
    "case",
    ["has", maxHeight], output:number,
    default:5
]:number
```
* https://help.github.com/articles/basic-writing-and-formatting-syntax/
* https://bl.ocks.org/DoctorBud/23aca14dcfde5f680870d77f39569e73

**setGeoJSONSourceData**
* https://github.com/mapbox/mapbox-gl-js/issues/929
* https://github.com/mapbox/mapbox-gl-js/issues/1399
* to convert the tile coordinate to geographic coordinate i found a solution : SphericalMercator.bbox
    * https://github.com/mapbox/mapbox-studio-classic/blob/5ac2ead1e523b24c8b8ad8655babb66389166e87/ext/sphericalmercator.js
```
map.showTileBoundaries =true;
map.on('dataloading', function (e) {
    if(!e.tile)return;
    var coord = e.tile.coord;
    var mec = new SphericalMercator({size : 512});
    var test = mec.bbox(coord.x, coord.y, coord.z);
    console.log(coord.z + '/' + coord.x + '/' + coord.y + ' : ' + test.toString()); 
})

```
*  https://github.com/gbif/maps

**Wind Data**
* https://github.com/mapbox/mapbox-gl-js/issues/4045
* https://www.mapbox.com/bites/00319/wind.html
* https://blog.mapbox.com/mapping-wind-barbs-to-show-speed-and-direction-4d3078add03d

**toppojson support**
* https://github.com/mapbox/mapbox-gl-js/issues/2920
* https://github.com/developmentseed/mapbox-gl-topojson

**CSV**
* https://github.com/thadk/mapbox-gl-csv
* http://thadk.net/mapbox-gl-csv/?access_token=pk.eyJ1IjoidW5lcGdyaWQiLCJhIjoiY2lzZnowenUwMDAzdjJubzZyZ3R1bjIzZyJ9.uyP-RWjY-94qCVajU0u8KA

**Mapillary with Mapbox GL JS**
* https://porter.io/github.com/mapillary/mapillary-js
* https://bl.ocks.org/oscarlorentzon/0b7c5763225029268fce0324af2b2b3a
* http://mapillary.github.io/mapillary-js/
* https://github.com/mapillary/mapillary-js/issues
* https://www.gislounge.com/the-future-of-street-level-photos-in-mapping/
* https://porter.io/github.com/mapillary/mapillary-js

**Mapillary Vista Dataset**
* https://techcrunch.com/2017/05/03/mapillary-open-sources-25k-street-level-images-to-train-automotive-ai-systems/
* https://www.mapillary.com/pricing

**UI Layer tools**
* https://bl.ocks.org/danswick/7f76b15f7ef80391e933

# Image Zooming
* https://en.wikipedia.org/wiki/Photosynth
* https://en.wikipedia.org/wiki/Deep_Zoom
* https://openseadragon.github.io/
* https://github.com/openseadragon/openseadragon
```
wget https://github.com/openseadragon/openseadragon/releases/download/v2.3.1/openseadragon-bin-2.3.1.tar.gz
```
* http://openseadragon.github.io/#examples-and-features
* https://github.com/lovasoa/dezoomify
* http://ophir.alwaysdata.net/dezoomify/dezoomify.html

# OSM
* https://wiki.openstreetmap.org/wiki/OSMTracker_(Android)
* http://learnosm.org/

# Cloud Platforms
* https://www.heroku.com/


# GIS

**TMS**
* http://wiki.osgeo.org/wiki/Tile_Map_Service_Specification
* http://www.osgeo.org/

**Traffic Signs**
* https://www.citylab.com/transportation/2017/02/how-to-teach-a-car-a-traffic-sign/516030/

## Editors
* https://mapcreator.here.com/mapcreator/12.974842709373405,77.64419906004497,18,0,0
* https://blog.mapillary.com/update/2018/05/18/editing-in-map-creator-with-mapillary-imagery.html
https://www.openstreetmap.org/user/Nighto/diary/37313


## Imagery in GIS
* https://www.gislounge.com/imagery-use-gis/

**Sun and Moon Position phases**
* https://github.com/mourner/suncalc

**maptalks**
* http://maptalks.org/examples/en/3d/polygon-altitude/

**GTFS**
* https://medium.com/@Scarysize/gently-gutting-gtfs-part-1-7a7f54a36ba0
* https://developers.route360.net/guide/gl-polygons
```
// get bounds for fiiting view
var bbox = turf.bbox(geojsonPolygons);
map.fitBounds(bbox, {padding: 20});
```
* https://parallel.co.uk/

## Princings
* https://developers.route360.net/pricing/

## Vector Tile Self Hosting
* https://gis.stackexchange.com/questions/188141/mapbox-sdk-is-it-free-if-you-host-your-own-vector-tiles
* https://geovation.github.io/build-your-own-static-vector-tile-pipeline
* https://openmaptiles.org/docs/host/tileserver-gl/

## 3D Tilings
* https://cesium.com/blog/2017/07/12/the-next-generation-of-3d-tiles/

**Using glTF for streaming CityGML 3D City Models**
* https://www.slideshare.net/planetarnie/using-gltf-for-streaming-citygml-3d-city-models-64486544?next_slideshow=1
* https://cesium.com/blog/2017/07/26/aerometrex-melbourne/
* https://cesium.com/blog/2017/05/26/arcade-game-results/
* https://govhack-toolkit.readthedocs.io/technical/making-maps/
* https://www.toptal.com/web/the-roadmap-to-roadmaps-a-survey-of-the-best-online-mapping-tools
* https://www.toptal.com/web/the-roadmap-to-roadmaps-a-survey-of-the-best-online-mapping-tools
https://tutel.me/c/gis/questions/136995/wfs+to+vector+tiles
* https://github.com/mapbox/vt2geojson
* https://github.com/mapbox/geojson-vt
* https://gis.stackexchange.com/questions/180182/how-to-tile-geojson-data
* http://tilestache.org/doc/
* https://www.sitepoint.com/3d-maps-with-eegeo-and-leaflet/
* https://www.mapbox.com/bites/00093/
* http://bl.ocks.org/lxbarth/4019660
* https://www.ryanbaumann.com/blog/2017/5/29/big-data-vector-heatmaps-with-mapbox-gl
* http://commons.pelagios.org/2017/11/building-the-roman-empire-vector-tile-map/

**CSV to Geojson mapbox gl**
* https://bl.ocks.org/danswick/effa94375f9ed24cea9f
**custom source layers**
* https://github.com/mapbox/mapbox-gl-js/issues/2920

**Geojson Tile server**
* https://gis.stackexchange.com/questions/193095/generating-and-hosting-vector-tiles-from-geojson-no-errors-but-no-data
* https://www.npmjs.com/package/geojson-tile-server
* https://github.com/TNOCS/geojson-tile-server.git
```bash
git clone https://github.com/TNOCS/geojson-tile-server.git
cd geojson-tile-server
yarn
yarn build
```

* https://github.com/mapbox/mapbox-gl-js/issues/2120
Tiled GeoJSON isn't supported. If you want to use tiled data, you need to provide it in vector tile format.
* https://www.arden.nl/getting-started-with-mapbox-gl-js/
* https://hvv.live/

**Vector Tile 3rd Parties Business Models**
* https://www.jawg.io/en/
* http://maptalks.org/examples/en/3d/polygon-altitude/
* http://maptalks.org/examples/en/style/line-arrow/
* http://maptalks.org/examples/en/3d/line-draw-altitude/#3d_line-draw-altitude
* https://github.com/maptalks/maptalks.js

**Animations mapbox gl**
* https://medium.com/@Scarysize/the-moving-city-visualizing-public-transport-877f581ca96e

## Mapbox GL SVG Layer
* https://github.com/mapbox/mapbox-gl-js/issues/5390
* https://bl.ocks.org/shimizu/5f4cee0fddc7a64b55a9

## Some References
* https://www.npmjs.com/package/geojson2mvt
* https://capitalplanning.nyc.gov/facilities
* https://connect.boundlessgeo.com/docs/suite/enterprise/latest/dataadmin/vectortiles/tutorial.html
* http://schwanksta.com/blog/vector-tiles-introduction-pt1

## 3D Line, 3D Roads, 3D Plane, 3D Curves, Extrusions
* https://stackoverflow.com/questions/47283304/mapbox-extruding-lines
* https://github.com/peterqliu/threebox
* https://github.com/cheeaun/3d-earth
* https://bl.ocks.org/mpmckenna8
* http://waplam.loan/list/openstreetmap-3d
* http://alteredqualia.com/three/examples/webgl_road.html
* https://stackoverflow.com/questions/45506426/convert-bezier-into-a-plane-road-in-three-js
* https://whsjs.readme.io/docs/extrude
* https://mattdesl.svbtle.com/drawing-lines-is-hard
* http://codeflow.org/entries/2012/aug/05/webgl-rendering-of-solid-trails/
* https://discourse.libcinder.org/t/smooth-efficient-perfect-curves/925
* https://www.shadertoy.com/view/lts3Df
* https://github.com/spite/THREE.MeshLine

## FAQs
* https://gis.stackexchange.com/questions/tagged/mapbox-gl-js?sort=unanswered&pageSize=50

## LiDAR to mapbox GL
* https://blog.mapbox.com/add-lidar-to-mapbox-43f7e3912424

## Custom Draw Tool
* https://medium.com/nycplanninglabs/building-a-custom-draw-mode-for-mapbox-gl-draw-1dab71d143ee
* https://github.com/NYCPlanning/labs-zola/blob/907c950e5173bd129b21781acafc1a5e950f5ad7/app/components/main-map.js#L238-L299
* https://popfactfinder.planning.nyc.gov/#12.25/40.724/-73.9868
* https://zola.planning.nyc.gov/#13.51/40.7119/-73.8922

## Image integration, Styling
* https://www.mapbox.com/help/gl-dds-map-tutorial/
* https://hackernoon.com/visualizing-uber-and-lyft-usage-in-san-francisco-928208b1978a
* https://www.mapbox.com/resources/guide-to-map-design-part-1.pdf
* https://github.com/mapbox/mapbox-gl-js/issues/3107
* https://bl.ocks.org/wboykinm/60945616feb3fc5ecacd2288c1493c3c
* https://github.com/mapbox/mapbox-gl-js/issues/4403
* https://bl.ocks.org/mbostock/4163057
* https://blog.mapbox.com/shading-and-lighting-3d-features-in-mapbox-gl-js-e544695cd64
* https://blog.mapbox.com/introducing-data-driven-styling-in-mapbox-gl-js-f273121143c3
```
"interpolate",
                ["linear"],
                ["heatmap-density"],
                0, "rgba(33,102,172,0)",
                0.2, "rgb(103,169,207)",
                0.4, "rgb(209,229,240)",
                0.6, "rgb(253,219,199)",
                0.8, "rgb(239,138,98)",
                1, "rgb(178,24,43)"

```
* https://www.mapbox.com/mapbox-gl-js/example/filter-markers-by-input/
* https://www.mapbox.com/mapbox-gl-js/example/measure/
* https://www.mapbox.com/mapbox-gl-js/example/drag-a-point/
* https://blog.mapbox.com/introducing-heatmaps-in-mapbox-gl-js-71355ada9e6c
* http://turfjs.org/docs/#circle
* https://gis.stackexchange.com/questions/240134/mapbox-gl-js-source-loaded-event
* https://www.mapbox.com/mapbox-gl-js/example/scroll-fly-to/
* http://vidteq.com/cgi-bin/outflv.pl?city=bangalore&img=IND_BLR_POI_0_22_77.610600_12.964267
* http://vidteq.com/cgi-bin/outflv.pl?city=bangalore&img=IND_BLR_POI_21_1035040_77.731677_12.986564
* http://vidteq.com/cgi-bin/outflv.pl?city=bangalore&img={IMAGE_NAME}