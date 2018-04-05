/*
Title: WebGL
Decription: WebGL 
Author: Bhaskar Mangal
Date: 
Tags: WebGL
*/

## WebGL

* http://www.webglinsights.com/
* http://webglreport.com/
is a great way to get WebGL implementation details for the current browser, especially when debugging browser- or device-specific problems.
* http://jshint.com/

For performance:
- avoid object allocation in the render loop
- Reuse objects and arrays where possible
- avoid built-in array methods such as map and filter
- Each new object creates more work for the Garbage Collector, and in some cases, GC pauses can freeze an application for multiple frames every few seconds.
- query attribute and uniform locations only at initialization
- do not update a uniform each frame; instead update it only when it changes.
- Save memory and improve performance by ensuring that contexts are created with the alpha, depth, stencil, antialias, and preserveDrawingBuffer options set to false, unless otherwise needed. Note that alpha, depth, and antialias are enabled by default and must be explicitly disabled.
- If shrinking the browser window results in massive speed gains, consider using a half-resolution framebuffer during mouse interaction

For portability, keep space requirements of varyings and uniforms within the limits of the GLSL ES spec. Consider using vec4 variables instead of float arrays, as they potentially allow for tighter packing. See A.7 in the GLSL ES spec

Non-power-of-two textures require linear or nearest filtering, and clamp-to-border or clamp-to-edge wrapping. Mipmap filtering and repeat wrapping are not supported.

Always enable strict mode via the “use strict” directive. It slightly alters JavaScript semantics so that many silent errors turn into runtime exceptions and can even help the browser better optimize our code.

Tips form different chapters
- Create new textures, rather than changing the dimensions or format of old ones
- Avoid use of gl.TRIANGLE_FAN, as it may be emulated in software.
- Pass data back and forth from Web Workers using transferable objects whenever possible.
- To save a lot of API calls, use vertex array objects (VAOs) or interleave static vertex data.
- Be vigilant about using requestAnimationFrame—ensure that most, if not all, of your WebGL work lives inside it
- Avoid using common text-based 3D data formats, such as Wavefront OBJ or COLLADA, for asset delivery. Instead, use formats optimized for the web, such as glTF or SRC.

**What happens between when a WebGL function is called in JavaScript and when Firefox calls the native graphics API?**
This includes datatype conversion, error checking, state tracking, texture conversion, draw call validation, shader source transformation, and compositing. Knowledge of these details helps us optimize our WebGL code; for example, by knowing how data copying, data conversion, and error checking work in ­ texImage2D and texSubImage2D, we can call these functions in such a way as to get their fastest path.


## Chapter 1
WebGL - GPU-accelerated 3D graphics through a JavaScript API.

While applications don’t need to handle these differences themselves, being familiar with the ways in which WebGL calls are vali- dated, modified, translated, and finally issued to the hardware provides developers with the tools to create efficient WebGL applications across implementations and platforms.

Browsers handle the calls made in WebGL by interpreting them and issuing graphics commands to the underlying hardware using a native graphics API.

In mobile browsers, these native commands are extremely similar to WebGL, because the vast majority of mobile graphics drivers implement OpenGL ES, on which WebGL is directly based.

On  the desktop, things become slightly more complicated; OpenGL ES drivers are not available for some desktop operating systems. Under Linux and OS X, the support path is clear, as desktop OpenGL is the native 3D graphics API for those platforms and is widely and robustly supported. Windows, on the other hand, has its own challenges. While desktop OpenGL drivers exist for Windows, most games and other applications which make use of the GPU instead utilize Direct3D, Microsoft’s 3D graphics API. Even if a user’s machine is known to have WebGL-capable hardware, it cannot be guaranteed that the user has OpenGL drivers installed at all.

By contrast, Direct3D drivers are installed with the operating sytem. Requiring OpenGL drivers, then, would be a barrier for a large number of Windows users, keeping them from easily being able to experience WebGL—a significant downside for an emerging web API.

For this reason, Google initiated the ANGLE project. ANGLE began as an implementation of OpenGL ES 2.0, the native 3D API on which WebGL 1.0 is directly based, built on top of Direct3D 9

This implementation is used both by Google Chrome and Mozilla Firefox on Windows as the backend for WebGL. Chrome also uses ANGLE for hardware- accelerated rendering support across the entire browser, from page rendering to hardware-accelerated video.

ANGLE’s shader translator, used to translate shaders from the OpenGL ES Shading Language (ESSL) into Direct3D’s High Level Shading Language (HLSL), also functions as a shader validator for WebGL and is used in that capacity not just on Windows, but also on.
In 2013, a Direct3D 11 rendering backend was added to ANGLE, allowing WebGL implementations the ability to make use of a newer native API.
Direct3D 11 additionally provides all the necessary features for ANGLE to support OpenGL ES 3.0.

**Computer Graphics courses and Articles etc**
* https://www.siggraph.org/

Readings
Interactive Computer Graphics: A Top-Down Approach
Interactive 3D Graphics Udacity course

demand for skilled WebGL developers is high.

how WebGL is reaching beyond games into areas such as neurological data visualization researchers presenting massive model rendering and educators providing advice on migrating graphics courses to WebGL

## WebVR
* https://webvr.info/
* https://experiments.withgoogle.com/webvr



## FOnt

https://stackoverflow.com/questions/25956272/better-quality-text-in-webgl

https://www.udacity.com/course/interactive-3d-graphics--cs291


https://github.com/tangrams/unity-terrain-example


## WebGL 2
https://webgl2fundamentals.org/



https://npm.runkit.com/react-map-gl-alt
https://npm.runkit.com/react-map-gl-3

https://blog.risingstack.com/the-react-way-getting-started-tutorial/


## List of WebGL Frameworks
https://en.wikipedia.org/wiki/List_of_WebGL_frameworks