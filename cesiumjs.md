/*
Title: Cesium
Decription: Cesium
Author: Bhaskar Mangal
Date: 
Tags: Cesium
*/

# Cesium
* https://news.ycombinator.com/item?id=12404740

Cesium does have a flat earth projection built in as well (there's a wireframe globe in top right of main page demo, and clicking it allows you to switch between 3D and 2D).

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


## Browser Support of WebGL
In terms of browser support: http://caniuse.com/#feat=webgl
http://webglstats.com/ is great.

## glTF - GL Transmission Format
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

## gltf viewer
* https://www.virtualgis.io/gltfviewer/

## 3D Model sketchup to Cesium
* http://cubecities.blogspot.in/2015/04/a-how-to-guide-for-exploring-3d.html

Also, check these links:
http://cubecities.com/generator/Cesium1.7.1/WFC-Example/loadModel.html

## [3D Tiles](https://github.com/AnalyticalGraphicsInc/3d-tiles)
* [Introducing 3D Tiles](https://cesium.com/blog/2015/08/10/introducing-3d-tiles)
* [3d Tiles Specifications by Cesium](https://github.com/AnalyticalGraphicsInc/3d-tiles)
* [3D geospatial to the web](https://cesium.com/blog/2016/09/06/3d-tiles-and-the-ogc)
* [Community Standard Justification Document (docx)](https://portal.opengeospatial.org/files/70040)

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

