---
Title: Open CV with Python
Decription: Open CV with Python
Author: Bhaskar Mangal
Date: 
Last Updated: 25th-Jul-2018
Tags: Open CV with Python
---

**Table of Contents**
* TOC
{:toc}


## Open CV with Python

## Intro
* https://github.com/arrybn/opencv_intro
* https://docs.google.com/presentation/d/1BAnB-vFKhyoCQB8D7WyudHWu96ceJl08p18EkRcnWvY/edit#slide=id.g35928e288c_0_334


https://stackoverflow.com/questions/13685771/opencv-python-calcopticalflowfarneback

https://www.quora.com/What-is-the-reason-Lena-S%C3%B6derbergs-photo-is-used-widely-to-test-algorithms-in-image-processing

* Conceptually, a byte is an integer ranging from 0 to 255. Throughout real-time graphics applications today, a pixel is typically represented by one byte per channel, though other representations are also possible.
* An OpenCV image is a 2D or 3D array of type numpy.array
* An 8-bit grayscale image is a 2D array containing byte values.
* A 24-bit BGR image is a 3D array, also containing byte values.

* We may access these values by using an expression like image[0, 0] or image[0, 0, 0].
  - The first index is the pixel's y coordinate, or row, 0 being the top.
  - The second index is the pixel's x coordinate, or column, 0 being the leftmost.
  - The third index (if applicable) represents a color channel.


* http://gdcm.sourceforge.net/wiki/index.php/Main_Page

* **GDCM : Grassroots DICOM library**
Whenever medical data, especially medical image data, is generated in a clinical environment, that data must be stored such that it can be retrieved by the same hospital either immediately, or after several years to determine the effectiveness of a course of treatment and to allow comparisons of multiple images for the same patient.

Digital Imaging and Communications in Medicine (DICOM) is a standard that governs this capability by specifying handling, storing, printing, and transmitting information in medical imaging.

Grassroots DICOM (GDCM) is an implementation of the DICOM standard designed to be open source so that researchers may access clinical data directly. GDCM includes a file format definition and a network communications protocol, both of which should be extended to provide a full set of tools for a researcher or small medical imaging vendor to interface with an existing medical database.

## Installation
https://github.com/rememberlenny/Flask-Person-Detector
https://github.com/jayrambhia/Install-OpenCV

## OpenCV.js
https://docs.opencv.org/trunk/df/d0a/tutorial_js_intro.html

OpenCV.js leverages Emscripten to compile OpenCV functions into asm.js or WebAssembly targets, and provides a JavaScript APIs for web application to access them.

## Video with OpenCV

### writing-to-video-with-opencv
* https://www.pyimagesearch.com/2016/02/22/writing-to-video-with-opencv/