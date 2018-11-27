---
title: Book Notes - Learning Geospatial Analysis with Python, 2nd Edition
---

**Table of Contents**
* TOC
{:toc}


## Book Notes - Learning Geospatial Analysis with Python


### Chapter-6: Python and Remote Sensing

* load the image to a NumPy array using gdal_array , and then we'll immediately save it back to a new GeoTIFF file
Images in NumPy are multidimensional arrays in the order of band, height, and width.

It's important to note that NumPy references the array locations as y,x (row, column) instead of the usual x, y (column, row) format that we work with in spreadsheets and other software: