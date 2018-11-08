---
Title: Geospatial Temporal Analysis
Decription: Geospatial Temporal Analysis
Author: Bhaskar Mangal
Date: 23rd Jan 2018
Tags: Geospatial Temporal Analysis
---

**Table of Contents**
* TOC
{:toc}


## Geospatial Temporal Analysis

## Geospatial Data Models

- [Department of Civil Engineering IIT KANPUR](http://gi.iitk.ac.in/gi/ph-d-thesis/)
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4298078/

geographical spatiotemporal process.
To understand the temporal and spatial change, a geographic object's attribute data should be derived directly from real-time observation by a sensor.

For example, air quality changes can be monitored in a certain place over a certain time period. Air quality is a geographic phenomenon that depends on a variety of air pollutants such as carbon monoxide or fine particulate matter. When the concentrations of some air pollutants reach a certain degree, an air pollution event occurs. 

According to the pollution degree, several pollution states are determined, e.g., mild contamination and serious contamination. The changes in air quality in the place during the time period are a spatiotemporal process. 


Sensor (Sensor): Various sensors containing space-borne, air-borne, and ground sensors.
Observation (Observation): The behaviour of observable attributes from various sensors provides observational data for the model.
Geographic Object (Geo-Object): Either physical entities or social phenomenon formed naturally or artificially, expressed with clear boundaries or not, as the objects of GIS research in the real world.
Object (Object): Single entity in the real world; a Geo-Object can contain one or multiple objects.
Spatiotemporal Process (StProcess): The Spatiotemporal Process is a periodized change process of a complex geographic phenomenon in a timeline, and the processes refer to a series of Geo-Objects and their interactions.
Simulation (Simulation): Simulation is the imitation of the operation of a real-world process or system over time.
Event (Event): An event is an occurrence of the Geo-Object change, and is the reason for the change of Geo-Objects.
State (State): A snapshot of a geographic object at a point of time in the change process.
Change Function (ChFunction): In the time of research, the correspondence between an instant and the values of geospatial and thematic properties. This function can be derived from industry, scientific computing, and relevant experience.


- A geographic object consists of three basic indivisible features: time, space, and thematic attributes
- A geographic object contains both unchangeable attributes and time-varying attributes.
- Time-varying attributes are associated with state sequences. The time-varying attributes may be different at different states.
- A sensor is a special geo-object that contains self-parameters and observations.
- The sensor, described by its metadata, is a tool to observe the spatial attributes and the thematic attributes of geographic objects; therefore, a sensor is the primary means of obtaining the changed information of a geographic object. 

Complex spatiotemporal changes in geographical phenomena refer to three core things: spatiotemporal processes, geographic objects, and events.
To support the spatiotemporal process, it should reveal the relationships between geographic objects, events, and spatiotemporal processes. 

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4298078/figure/Fig3/
https://www.geospatialworld.net/article/gis-to-predict-air-pollution-level-in-mining-region/

 http://www.epa.gov/airdata

https://www.witpress.com/Secure/elibrary/papers/AIR00/AIR00043FU.pdf
 kriging as the gridding method. 


## Mapbox-GL with D3.js
https://bl.ocks.org/etpinard/9cce3976acc33770bd1212adcc95c9fe
https://www.mapbox.com/mapbox-gl-js/example/3d-extrusion-floorplan/
https://www.mapbox.com/mapbox-gl-js/example/timeline-animation/

## Tools
https://geotrellis.io/
- GeoTrellis is a geographic data processing engine for high performance applications.
https://geopyspark.readthedocs.io/en/latest/