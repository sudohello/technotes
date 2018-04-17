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


1. Layer Sequencing
2. Toggle Different Base Map Layers like raster/satellite, to vector MMI, to vector Mapbox
3. Popup handling

UI:
1. Layer Controls
2. Style Controls - Custom styling control

Use case to be implemented based on challanges
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
https://blog.kuntzsch.me/stepping-up-my-web-mapping-game-mapbox-gl-and-d3/
https://blog.mapbox.com/make-your-own-cartography-game-with-mapbox-gl-at-our-workshop-in-bengaluru-2d3a5e1cd680
https://bl.ocks.org/DeEgge/ba386d71b5d0157e2195da02a3d4453b



## Customization
- Layer Control
http://leafletjs.com/examples/layers-control/
https://gis.stackexchange.com/questions/130471/how-to-switch-base-layer-programmatically-in-mapbox-leaflet
https://github.com/mapbox/mapbox-gl-js/issues/5489
https://github.com/mapbox/mapbox-gl-js/issues/3979

## Working with geojson
https://www.mapbox.com/help/working-with-large-geojson-data/

http://bl.ocks.org/ryanbaumann/04c442906638e27db9da243f29195592/33e8d3520feecf0912f489689ca4a5c01bdfcbfc
https://github.com/osm2vectortiles/osm2vectortiles

https://openmaptiles.org/

https://github.com/mapbox/mapbox-gl-leaflet

**Draw Control**
https://bl.ocks.org/danswick/083a0b48c2cc78c4a08d
https://github.com/mapbox/mapbox-gl-draw
https://github.com/mapbox/mapbox-gl-draw/blob/master/docs/MODES.md#available-custom-modes

**Custom Control**
https://codepen.io/sergei-zelinsky/pen/gGOZjE

http://www.material-ui.com/#/components/svg-icon

**Pitch Control**
http://fuzzytolerance.info/blog/2017/01/30/Pitch-toggle-control-for-Mapbox-GL-JS/

* **Changing BaseMap**
https://github.com/mapbox/mapbox-gl-js/issues/2267

* **Add WMS Layer**
https://www.mapbox.com/mapbox-gl-js/example/wms/


http://www.vidteq.com/vs/tilecache.php?LAYERS=BANG_BUTTERFLY&FORMAT=image%2Fpng&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&STYLES=&SRS=EPSG%3A4326&BBOX=77.34375,12.83203125,77.51953125,13.0078125&WIDTH=256&HEIGHT=256


http://www.vidteq.com/vs/tilecache.php?LAYERS=BANG_BUTTERFLY&FORMAT=image/png&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&STYLES=&SRS=EPSG:4326&BBOX={bbox-epsg-4326}&WIDTH=256&HEIGHT=256

https://geodata.state.nj.us/imagerywms/Natural2015?bbox={bbox-epsg-3857}&format=image/png&service=WMS&version=1.1.1&request=GetMap&srs=EPSG:3857&width=256&height=256&layers=Natural2015'
            ],


**Forums**
https://github.com/mapbox/mapbox-gl-js/issues/3552

[pitch is hardcoded to 60 because of tile loading and label rendering issues]
https://github.com/mapbox/mapbox-gl-js/issues/3731



**Style Layer Picker**
data:image/svg+xml;charset=utf-8,<svg viewBox='0 0 20 20' xmlns='http://www.w3.org/2000/svg'><title>HUD_basemap_icon</title><path d='M9.325 11.64c.405.283.945.283 1.35 0l8.179-4.752a.338.338 0 0 0-.043-.581l-8.285-3.183a1.184 1.184 0 0 0-1.052 0L1.189 6.307a.338.338 0 0 0-.043.581l8.179 4.753zm9.486-.71l-2.238-1.11-5.152 2.994a2.572 2.572 0 0 1-1.421.424 2.58 2.58 0 0 1-1.421-.424L3.43 9.818 1.19 10.93a.338.338 0 0 0-.044.581l8.179 5.678c.405.282.945.282 1.35 0l8.179-5.678a.337.337 0 0 0-.043-.58z' fill='%23242528' fill-rule='evenodd'/></svg>

https://www.mapillary.com/app/?lat=12.291465261038326&lng=41.63047318341364&z=1.5&mapStyle=esri


**Terrain & Elevation**
https://www.mapbox.com/mapbox-gl-js/example/toggle-layers/
https://blog.mapbox.com/satellite-map-with-contours-ff1b1ff735e6
https://stackoverflow.com/questions/38467973/mapbox-gl-js-contour-lines-elevation

https://github.com/mapbox/mapbox-studio-satellite-outdoors.tm2

https://github.com/mapbox/mapbox-gl-styles/blob/1ac5e784907e50c2284c7cc59169ac64ce4e885c/styles/satellite-v7.json#L713-L739

**3D Terrain with Three.js**
- https://blog.mapbox.com/bringing-3d-terrain-to-the-browser-with-three-js-410068138357
- https://www.mapbox.com/bites/00332/#13.4682/36.3524/-112.5928/-138.4134/0.0001
- https://www.mapbox.com/blog/terrain-rgb/
- https://openmaptiles.github.io/klokantech-terrain-gl-style/#13.25/47.0819/8.5846/-172/47
- https://openmaptiles.github.io/klokantech-terrain-gl-style/style-cdn.json
- https://openmaptiles.com/contours/
- https://www.mapbox.com/vector-tiles/mapbox-terrain/
- https://free.tilehosting.com/data/v3.json?key=RiS4gsgZPZqeeMlIyxFo
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


**Cool Examples**
https://www.mapbox.com/mapbox-gl-js/example/scroll-fly-to/
https://www.mapbox.com/help/make-a-heatmap-with-mapbox-gl-js/
https://blog.mapbox.com/labels-for-navigation-in-mapbox-gl-d9220fa51762
https://blog.mapbox.com/labels-for-navigation-in-mapbox-gl-d9220fa51762
https://www.mapbox.com/mapbox-gl-js/example/hover-styles/
**Toggle and restricted bounds**
http://geo-odyssey.com/links/stack.html

https://www.mapbox.com/help/define-camera/

**Height**
http://thinkingspatial.com/category/uncategorized/
https://tutel.me/c/programming/questions/43891269/rotated+points+in+mapbox+are+skewed

https://javascript.wekeepcoding.com/article/10428523/mapbox-gl-js%3A+Adjust+visible+area+%26+bearing+to+a+given+line%2C+for+a+given+pitch

https://www.getbounds.com/blog/data-driven-styling-3d-polygons-and-vector-tiles-with-mapbox-gl-js/


**To look**
https://www.ovrdc.org/apps/accident-explorer.html#8.61/39.1469/-83.4514

https://www.ovrdc.org/apps/block-group-explorer.html#6.61/40.217/-80.713


## Data Driven Colors and Popups
https://gis.stackexchange.com/questions/195202/mapbox-gl-and-styling-for-data-driven-labels

**Map Markers**

https://bl.ocks.org/danswick/4906b495e0b206758f71
https://www.mapbox.com/mapbox-gl-js/example/custom-marker-icons/

**Embedding YouTube Video URLs**

https://stackoverflow.com/questions/19836015/youtube-url-in-video-tag
https://stackoverflow.com/questions/28539536/mapbox-non-geographic

Refused to display 'https://www.youtube.com/watch?v=aONXZopnY2c' in a frame because it set 'X-Frame-Options' to 'SAMEORIGIN'.

Refused to display in a frame because it set 'X-Frame-Options' to 'SAMEORIGIN'.

**Save GeoJSON**
https://bl.ocks.org/danswick/36796153bd86ce982a59043cbe0ac8f7

## Icons & Fonts
https://github.com/mapbox/mapbox-gl-js/issues/3605
http://fontastic.me/


https://stevebennett.me/category/mapmaking/

## NPM based development
https://www.npmjs.com/package/@ivelander/mapbox-gl

## Underground
https://github.com/elliotleelewis/TubeMap

## 3D Floor Changer
http://www-personal.umich.edu/~yonghah/rooms3d/

## MapboxGL City Examples with New UI Features
https://developmentactivity.melbourne.vic.gov.au/

https://data.melbourne.vic.gov.au/Property-Planning/3D-Development-Activity-Model-Footprints/def8-4wbt
https://data.melbourne.vic.gov.au/

https://ubilabs.net/en/news/data-driven-raster-layer-mapbox-lg-2016-09-05

https://www.behance.net/gallery/24276859/City-Layouts

https://density.ubilabs.net/

## urban-surveillance
http://www.sarahmakesmaps.com/blog/2014/7/17/urban-surveillance
https://www.skylinewebcams.com/en/webcam/malta/malta/traffic/traffic-cam15.html
http://www.btis.in/transport/traffic

## Noise Pollution
https://github.com/lukasmartinelli/osm-noise-pollution
http://lukasmartinelli.ch/gis/2016/04/03/openstreetmap-noise-pollution-map.html
http://lukasmartinelli.ch/maps/noise-pollution.html#12.16/47.3805/8.5341
mapbox://styles/morgenkaffee/cimi6phf0007wcem3cyr9cl3o

## Directions
https://www.mapbox.com/help/how-directions-work/

## Raster in Mapbox GL
https://medium.com/@Scarysize/data-driven-raster-layer-with-mapbox-gl-bdb3b747ae22

## maptalks js
https://maptalks.org/

## Tiling
http://www.azimuth1.com/blog/sar-topo-tech-notes.html
https://github.com/klokantech/maputnik
https://stackoverflow.com/questions/31487520/mapbox-gl-using-external-maps

## Traffic
https://github.com/mapbox/mapbox-gl-traffic
https://bl.ocks.org/danswick/f4aa01a046385eb69313499b7934f425
https://www.mapbox.com/vector-tiles/mapbox-traffic-v1/


## Mapbox V/s Google
https://nextjuggernaut.com/blog/google-vs-mapbox/


## Query Features
https://ovrdc.github.io/gis-tutorials/mapbox/03-query-features/#4/39.94/-95.52


## Map Designs
https://ovrdc.github.io/
https://github.com/ovrdc/material-maps
https://ovrdc.github.io/material-maps/

## MapboxGl plugins
https://github.com/lukasmartinelli/mapbox-gl-inspect

## Google Maps Enterprise
https://enterprise.google.com/maps/pricing/


============
UI
https://www.htmllion.com/css3-toggle-switch-button.html
https://1stwebdesigner.com/css-snippets-radio-toggles-switches/
https://dcrazed.com/html5-css3-accordion-tabs/


=--------------
https://cheapticket.in/b2c/booking/3078966



http://robdodson.me/javascript-design-patterns-singleton/

## Single Page App - SPA
https://engineering.door2door.io/a-single-page-application-with-react-and-mapbox-gl-f96181a7ca7f


===============
## OnClick
https://gis.stackexchange.com/questions/186533/highlight-feature-with-click-in-mapbox-gl
http://thinkingspatial.com/mapbox-gl-js-click-and-hover-events/
https://www.mapbox.com/mapbox-gl-js/example/queryrenderedfeatures-around-point/

https://stackoverflow.com/questions/42978952/how-to-find-all-layers-in-mapboxgl-ultimately-i-want-to-show-custom-layer-only?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

**Query Similar Features**
https://www.mapbox.com/mapbox-gl-js/example/query-similar-features/


querySourceFeatures

* // Query all rendered features from a single layer
Map.prototype.queryRenderedFeatures = function queryRenderedFeatures (geometry    

https://www.mapbox.com/mapbox-gl-js/example/using-box-queryrenderedfeatures/

* @param {string} [options.localIdeographFontFamily=null] If specified, defines a CSS font-family

## SDKs on MapboxGL
https://developers.airmap.com/v2.0/docs/customize-the-map
https://sdk.boundlessgeo.com/filter/index.html

https://blog.mapbox.com/creating-vector-tiles-from-raster-datasets-f8c9dc652c97

## Mapbox API
https://www.mapbox.com/api-documentation/
https://www.mapbox.com/blog/tags/weather/

## AR - Augmented Reality with location based applications
https://blog.mapbox.com/mapbox-ar-2f065374eacb


## Extra Reading
http://chairnerd.seatgeek.com/vector-venue-maps-using-mapboxgl/

## Data Driven Styling
https://blog.mapbox.com/announcing-expressions-in-gl-js-a72b55d0a6af
https://www.mapbox.com/help/mapbox-gl-js-expressions/
https://www.mapbox.com/mapbox-gl-js/style-spec/#expressions-interpolate
https://www.mapbox.com/mapbox-gl-js/style-spec/#expressions
https://www.mapbox.com/mapbox-gl-expressions/

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

## MapboxGL Indoor Map
https://bl.ocks.org/danswick/e25b783434a7c52ee8e2


## MapboxGL snippets

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

https://www.mapbox.com/mapbox-gl-js/example/mapbox-gl-draw/
https://www.mapbox.com/mapbox-gl-js/example/playback-locations/
https://www.mapbox.com/mapbox-gl-js/example/toggle-layers/
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

https://www.mapbox.com/mapbox-gl-js/example/heatmap-layer/

## Layer Ordering
https://github.com/mapbox/mapbox-gl-js/issues/1349
https://bl.ocks.org/ryanbaumann/e5cd12a01ef72ab620a2a58b71b1aa6b/38d6cdb6fe1ca54b17ed30dc8db77fb550a99d3d


## OpenMapTiles in MapboxgL
https://openmaptiles.org/docs/style/mapbox-gl-style-spec/
http://docs.geoserver.org/stable/en/user/styling/mbstyle/reference/spec.html


=============
## web tools
https://github.com/mapbox/geojson.io
http://gree.github.io/tesspathy/


## WebApp Security
**XSS**
https://haacked.com/archive/2009/06/25/json-hijacking.aspx/


https://betterexplained.com/articles/using-json-to-exchange-data/

## Environment API
**Weather**
https://weather.com/en-IN/weather/interactive/l/INKA0310:1:IN?layer=clouds


## MapboxGL js snippets

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

## Mapbox GL Style Specifications
- https://github.com/mapbox/mapbox-gl-js/blob/master/src/style-spec/reference/v8.json#L161
- https://github.com/mapbox/mapbox-gl-js/issues/3360
**Metadata Examples**
- https://github.com/mapbox/mapbox-gl-styles/blob/master/styles/bright-v8.json

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

    ## Mapbox GL Different Eye Poping Stlye Examples
    - [Medieval Melbourne](https://bl.ocks.org/stevage/eef4001fe752c7c6b82af3237a102b8c)
        - blog: https://stevebennett.me/tag/mapbox/
