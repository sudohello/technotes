/*
Title: Indoor Mapping
Decription: Indoor Mapping
Author: Bhaskar Mangal
Date: 
Tags: Indoor Mapping
*/

# Indoor Mapping

https://www.tecmint.com/freefilesync-compare-synchronize-files-in-ubuntu/

https://www.prezent3d.com/
http://bashooka.com/coding/html-css-based-presentation-slides/


https://www.aconvert.com/video/mkv-to-gif/

## wrld3d
https://www.wrld3d.com/blog/a-sneak-peek-into-our-indoor-mapping-rd/
https://www.wrld3d.com/wrld.js/latest/docs/leaflet/L.Map/
https://github.com/wrld3d/wrld.js/tree/master
https://github.com/topics/leafletjs?l=javascript&o=desc&s=forks

## B-Plan NavVis

On the same line we have some more examples. Like check these couple of links:-
http://www.narayanahealth.org/contact-us (click on virtual tour)
Indoor map for NH on google maps

Different verticals for Indoor Mapping:-
https://www.wrld3d.com/3d-maps/indoor-mapping/

Also, review these NavVis based implementations:-
panorama-digital  - Retail
deutsches-museum  - Museum
munich-airport  - Airport

With NavVis in place we can provide solutions: A, B and C as given below:

**A. Virtual Tours**
i) 360 degree views - simple panorama - multiple of them integrated in a single window
ii) 360 degree view with depth perception and multiple points of panorama in short distance

1. VidTeq's 360 view - (i)
2. Google's Streetview for indoors - (ii)
3. NavVis's Indoor Mapping - (ii)


**B. Indoor Maps**
- vector maps, can see the indoor floor plan
- 2D/3D vector maps, CAD drawings integrated on google maps or open streetmap
- Indoor pois are marked

1. Google Indoor Maps
2. NavVis Indoor Maps

**C. Indoor Navigation**
- For indoor: from one poi to another poi
- non-realtime: cannot determine user's indoor location accurately

1. NavVis Indoor Navigation

**D. Indoor Navigation with IPS (Indoor Positioning Systems)**
- When integrated with IPS :
    - It can get provide accurate position of the user
    - This provides routing/navigation from/to user's current position
    - This is generally integrated with Indoor Mapping technology
- This is quite hot market in US and UK and there are quite handful of vendors into this space.
- Example: https://www.accuware.com



## [Physical Web](https://github.com/google/physical-web)
* https://github.com/google/physical-web
* https://google.github.io/physical-web/faq
* https://www.beaconzone.co.uk/blog/beacons-are-not-for-spamming-customers/
* https://community.estimote.com/hc/en-us/articles/115001474168-Eddystone-URL-and-Physical-Web-All-You-Need-to-Know
* https://kontakt.io/beacon-basics/ibeacon-and-eddystone/

The **Physical Web** is an open approach to enable quick and seamless interaction swith physical objects and locations.

* **[exploring-the-physical-web-without-buying-beacons](https://medium.com/@urish/exploring-the-physical-web-without-buying-beacons-efae51e36c2e)**
https://github.com/dburr/linux-ibeacon

https://community.estimote.com/hc/en-us/articles/202254358-How-do-I-build-my-first-app-Useful-resources
https://www.postscapes.com/googles-physical-web-suggests-urls-not-apps-are-the-future-of-the-internet-of-things/

```bash
hciconfig -a 
```
https://github.com/nirmankarta/PyBeacon
https://www.domoticz.com/forum/viewtopic.php?t=10640
https://www.beaconzone.co.uk/blog/eddystone-url-doesnt-work-on-android-oreo-8-0/


### Implications
* https://bkon.zendesk.com/hc/en-us/articles/115003406628-Is-it-possible-to-push-messages-or-notifications-from-a-Physical-Web-beacon-

emerging technology like Google's Services Workers and designing Progressive Web Apps that will allow users to opt in to push messages from individual websites

## [Push Notifications On The Open Web](https://developers.google.com/web/updates/2015/03/push-notifications-on-the-open-web)


## [Progressive Web Apps](https://developers.google.com/web/progressive-web-apps)


# Indoor Mapping
* http://wiki.openstreetmap.org/wiki/Simple_Indoor_Tagging
* http://wiki.openstreetmap.org/wiki/Indoor_Mapping
* https://www.wrld3d.com/3d-maps/indoor-mapping-pricing/
* https://www.jibestream.com/blog/what-is-the-best-system-for-achieving-blue-dot-indoors
* https://www.jibestream.com/blog/jibetalking-indoor-phone-positioning-ibeacon-vs-nfc-vs-gps-and-eddystone

**Blue Dot**
* https://slaminfo.indoo.rs/technology/blue-dot/
* https://slaminfo.indoo.rs/slam-revolution/
* http://www.esa.int/Our_Activities/Navigation/Galileo/What_is_Galileo


WE SUPPORT MULTIPLE POSITIONING PROVIDERS

WHAT POSITIONING SERVICE FITS YOUR NEEDS?
There are a number of technologies that can help finding your position indoors. WiFi triangulation, BLE beaconing technology, sensor fusion platforms and geomagnetic field fingerprinting are probably your best options. We’ve got experience in using all of these, and there is no clear answer as to which technology is best. They all come with their pros and cons, and it depends on the use case what technology we recommend. We see ourselves as a positioning-agnostic service that can work with more or less any positioning provider, and we take pride in advising our customers the best fit for their needs and budget.

https://www.mazemap.com/

**Standard GPS, solution is not functional indoors. So how do you go about finding your way indoors?**
When you move from the outdoor GPS environment into a building you can be guided using an app on your phone that is connected to an Indoor Positioning System (IPS).
Although IPS's do not have an industry standard like GPS does, there are a variety of technologies that can be used to help you find your way.

This is achieved using the same real-time location recognition as a GPS nav system in your car. The equivalent to this for the indoors is referred to as 'Blue Dot' wayfinding.

## 'Blue Dot' wayfinding

## Technology
* https://blog.beaconstac.com/2015/07/ibeacon-vs-nfc-vs-gps-which-indoor-location-technology-will-your-business-benefit-from/
* https://venturebeat.com/2015/07/14/google-embraces-bluetooth-low-energy-beacons-launches-open-format-eddystone-apis-and-management-tools/
* https://www.otherworld.io/

** location technologies**
– Wi-Fi
- iBeacon (Bluetooth Low Energy)
- NFC
- GPS (Satellite based navigation)

Unfortunately, each of these technologies have their own limitations and businesses need to use the right combination of two or more based on their budget and what they are trying to achieve

1. Accessibility
2. Range and Accuracy


**What is accessibility?**

The ability of the indoor location technology to be “tapped into” or accessed by a consumer or business is defined as Accessibility.

No matter which technology you opt to go ahead with for your business, you need to have some basic infrastructure such as a transmitter, a receiver and a data service, in place to determine the location.

**What is range and accuracy?**
Range is defined as the distance that the signal travels. In general context, the range of any indoor location technology is dependent on the configuration, power settings and environment in which it is deployed. For example, a WiFi or Bluetooth signal will demonstrate a wider range outdoors without any obstruction than in a multi-surface indoor setting.

At the same time, the reliability of the signal within a given range, and the tolerance of that signal when accounting for environmental factors is referred to as Accuracy.


Bluetooth Beacons
Beacons are tiny pieces of hardware which emit Bluetooth signals to phones. Beacons use BLE (Bluetooth Low Energy) to communicate with smartphones and let them know the distance they are away from a particular beacon. A large network of Beacons is required to provide the accuracy necessary for an IPS.

The pros: The accuracy of Bluetooth Beacons is thought to be the most reliable and best compared to the alternatives. Also, depending on the desired use case, the business can configure the Beacon network to be more or less accurate through settings and the number of beacons installed.

The cons: There is a substantial upfront hardware/ install cost associated with Bluetooth Beacons. Also, depending on the venue and their IT protocols, increased BLE network traffic may not be favored.


**Product Pricing Parameters**
* Price per building
  - size of buildings: number of floors, square meters
* Private / Public
* Building Floorplan Updates
  - Pay per update
* Customizable Maps: Icons and Colors
  - Extra functionality for extended control of POIs, such as custom icons and colors of rooms. Not fully included in the Basic bundle, but if your needs are small and specific, we allow for an ad-hoc billing for these services
* Wayfinding: Indoor Paths
* Wayfinding: Indoor Blue Dot Integration
* Facility Management Integration

Product Bundle
2 to 4 from Basic to Enterprice packages

We have a BASIC bundle, and an ENTERPRISE package with extended platform possibilities.
Compare, and see which one is best for you, and consult us if you are in doubt.






**Eyedog Wayfinding**
http://www.eyedog.mobi/blue-dot-navigation/

**indooratlas**
http://www.indooratlas.com/pricing/

Our pricing is simple – you pay as your app grows. We offer the best suitable business model for your use case. For details, please contact us.

* Location based pricing
* Monthly active users
* Revenue share model

What Are Indoor Positioning Systems (IPS)Indoor positioning systems (IPS) locate people or objects inside a building using radio signals, geomagnetic fields, inertial sensor data, barometric pressure, camera data or other sensory information collected by a smartphone device or tablet. These systems are used to detect and track a position. Just think of it as GPS, but for indoors.


https://app.indooratlas.com/locations/add


**Here Map**
https://wego.here.com/?map=12.92078,77.68891,19,satellite


**Maze Map**
https://www.mazemap.com/pricing

**steerpath**
https://steerpath.com/

**wayfindingpro**
https://www.wayfindingpro.com/sdk/

**indoorway**
https://www.indoorway.com/developers/

**mapsindoors**
https://www.mapspeople.com/become-a-partner/
https://mapsindoors.github.io/
https://mapsindoors.github.io/web/

**proximi**
https://proximi.io/

**wrld3d**
Coverage:
- United States, Canada, UK & Ireland, Scandinavia, the Arabian Peninsula, Japan, Australia, Brazil, France, Spain and Thailand

BUILD

Add your own building data and easily manage your places.
Standard procedural rendering.
Your data is public on WRLD, any applications built on our platform can go inside your building.
FREE

Map usage license required for usage in an app

See Example
PRIVATE

Add your own building data and easily manage your places.
Standard procedural rendering.
Your data is private on WRLD, only you control access to inside your building.
$1,400 ANNUAL

Map usage license required for usage in an app

See Example
LANDMARK

Add your own building data and easily manage your places.
Custom hand modeling of your buildings so they are recognizable and branded.
Your data is private on WRLD, only you control access to inside your building.
$2,300 ANNUAL

Map usage license required for usage in an app

See Example
ENTERPRISE

Desire to map new territories outside our current coverage*
Multiple buildings or locations
Custom interior detailing
On-premise requirements



**advanced pedestrian dead-reackoning**
https://en.wikipedia.org/wiki/Dead_reckoning

In navigation, dead reckoning is the process of calculating one's current position by using a previously determined position, or fix, and advancing that position based upon known or estimated speeds over elapsed time and course.

[EYEDOG INDOOR POSITIONING SYSTEM](http://www.eyedog.mobi/indoor-navigation-system/)

When choosing for the Eyedog IPS Module on top of the regular mobile wayfinding service, Eyedog offers by default the most advanced indoor positioning system available in the market today. It can operate indoors and outdoors without relying on infrastructure such as WiFi Access Points, Bluetooth Beacons or even GPS. So, no external hardware required! And it works without having ever visited the facility before, meaning that no finger-printing is required and no internet connection is required when operational! The IPS uses advanced pedestrian dead-reackoning and is totally software based. It processes data from the accelerometers and gyroscopes built into mobile devices, applying Machine Learning and Artificial Intelligence (AI) techniques to achieve unrivalled accuracy. The accuracy range is 0,1m - 3,0 meters, the refresh rate is 10 times per second and no maintenance is required. 


http://www.eyedog.mobi/blue-dot-navigation/

## Standards
* Eddystone
* iBeacon
* [Altbeacon](http://altbeacon.org/) by [radiusnetworks](http://radiusnetworks.com/)
The AltBeacon specification defines the format of the advertisement message that Bluetooth Low Energy proximity beacons broadcast. The AltBeacon specification is intended to create an open, competitive market for proximity beacon implementations.

## References
http://geoawesomeness.com/list-top-100-geospatial-start-ups-companies-world/
https://angel.co/indoor-positioning

http://www.marketsandmarkets.com/PressReleases/indoor-location.asp
http://www.mapmyindia.com/indoor-mapping/applications_benefits

Market Research
https://globenewswire.com/news-release/2017/03/07/932976/0/en/Indoor-Positioning-and-Navigation-Market-Set-to-Play-Vital-Role-in-Increasingly-Massive-Retail-Stores.html

http://industryarc.com/Report/43/global-indoor-positioning-navigation-market.html

https://speakerdeck.com/sos/indoor-location-primer-at-place-london-2014-number-placelondon


https://www.photoxels.com/panasonic-linkray/

https://hackaday.com/2017/05/04/ultrasonic-tracking-beacons/
http://electronicsforu.com/india-corner/roshni-indoor-navigation-system-visually-impaired

http://www.clovetech.com/
https://www.davidrumsey.com/


## Blogs on IPS and Indoor Maps
https://www.extremetech.com/extreme/126843-think-gps-is-cool-ips-will-blow-your-mind
https://www.extremetech.com/computing/109033-keep-your-sanity-at-the-mall-with-an-internal-positioning-system-ips
https://www.indolytics.com/future-indoor-positioning-system/

https://www.slideshare.net/RossMcDonald1/using-qgis-to-create-3d-indoor-maps
https://github.com/wrld3d/wrld-indoor-maps-api

## OSRM
Open Source Routing Engine
http://map.project-osrm.org


## Leaflet Indoor Map
https://github.com/cbaines/leaflet-indoor
http://www.cbaines.net/projects/osm/leaflet-indoor/examples/
http://subathrathanabalan.com/2015/10/25/indoor-map-mapbox/

## Open Street Map - OSM for IndoorMap
https://www.geospatialworld.net/article/openstreetmap-to-create-indoor-maps/

## Leaflet Realtime Data
https://github.com/perliedman/leaflet-realtime

## mapbox gl
https://bl.ocks.org/danswick/e25b783434a7c52ee8e2
https://www.mapbox.com/mapbox-gl-js/example/3d-extrusion-floorplan/

**Follow this blog**
http://googlemapsmania.blogspot.in/2017/01/indoor-mapping-with-mapbox-gl.html
http://www-personal.umich.edu/~yonghah/rooms3d/
https://bl.ocks.org/danswick/e25b783434a7c52ee8e2


Google Web Mercator, which can be referenced by the code 'EPSG:3857'.

### Heatmap Layer
https://www.mapbox.com/mapbox-gl-js/example/heatmap-layer/

### 3D buildings
https://www.mapbox.com/mapbox-gl-js/example/3d-buildings/
**Along with zoning information**
http://www.sarahmakesmaps.com/blog/



## Indoor Mapping Tech Companies and Technologies
http://www.kaarta.com/

## Indoormaps Examples
https://www.mapspeople.com/mapsindoors/
http://3dcampus.arcgis.com/EsriCampusViewer2017/

## OSM Indoor Mapping
https://agile-online.org/conference_paper/cds/agile_2014/agile2014_82.pdf
https://www.gim-international.com/content/article/mapping-the-indoor-world
http://wiki.openstreetmap.org/wiki/IndoorOSM - Dont Use this, defunct
https://wiki.openstreetmap.org/wiki/Simple_Indoor_Tagging - current spec

https://www.youtube.com/watch?v=60Ab7f8YZ7w
http://europe.foss4g.org/2015/Mapping%20parties