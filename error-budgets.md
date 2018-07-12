/*
Title: Error Budgets
Decription: Types of Error in Photogrammetry
Author: Bhaskar Mangal
Date: 5 Jan 2017
Placing: 1
Tags: Error Budget, Photogrammetry, Concept
*/

## Error
Reprojection error
Root Mean Square reprojection error averaged over all tie points on all images

Camera Calibration - Internal
Camera Locations (External Calibration)
Total error (m) - root mean square error for X, Y, Z coordinates for all the cameras
Ground Control Points
Error (m) - root mean square error for X, Y, Z coordinates for a GCP location / check point.

Scale Bars
Error (m) - difference between input and estimated values for scale bar length.

Point Cloud Data
Resolution - effective resolution of the exported PCD
Point Density - average number of dense cloud points per square meter

Processing Parameters
Tie Point
The mean key point size value is a mean tie point scale averaged across all projections
Reference coordinate system
For each camera/camera set - accuracy data both for position (i.e. x,y,z coordinates) and orientation (i.e. yaw, pitch, roll angles)

Errors in the Reference pane

Cameras section
Error (m) - distance between the input (source) and estimated positions of the camera
Error (deg) - root mean square error calculated over all three orientation angles
Error (pix) - root mean square reprojection error calculated over all feature points detected on the photo.

ameras Ground Control Points
Total error (m) - root mean square error for X, Y, Z coordinates for all the cameras Ground Control Points
Error (m) - root mean square error for X, Y, Z coordinates for a GCP location / check point.


Markers section
Error (m) - distance between the input (source) and estimated positions of the marker
Error (pix) - root mean square reprojection error for the marker calculated over all photos where marker is visible

Scale Bars section
Error (m) - difference between the input (source) scale bar length and the measured distance between two cameras or markers representing start and end points of the scale bar.

Optimization
