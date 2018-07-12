/*
Title: Case Studies
Placing: 8
*/

**Case Study References**
* http://www.cvlibs.net/publications/Geiger2013IJRR.pdf
* http://www.cvlibs.net/datasets/kitti/index.php
* [Supply Chain of 3D Digitization & the Pipeline](http://3dicons-project.eu/eng/Guidelines-Case-Studies/Guidelines2)
* https://www.cosc.canterbury.ac.nz/research/reports/HonsReps/2009/hons_0908.pdf
* www.mrt.kit.edu/z/publ/download/2013/GeigerAl2013IJRR.pdf
* [photogrammetric-applications-for-cultural-heritage.pdf]( https://content.historicengland.org.uk/content/docs/guidance/draft-photogrammetric-applications-for-cultural-heritage.pdf)

## Case Studies Review

### photogrammetric-applications-for-cultural-heritage.pdf
*  multi-image convergent photogrammetric developments i.e. those using a combination of Structure from Motion (SfM) and Multi-View Stereo (MVS) workflows.

* Photogrammetry Concepts
	* Chief rays, Intersection of two rays to locate object point
	* Collinearity
		- Given the assumption that the object point, camera projection centre and image point are in a straight line, in order to translate between the 2D image coordinate system, with its origin at the centre of the image (as opposed to the principle point, which is the orthogonal projection of the projection centre on the sensor, hence the necessary computation of principle point offset values) and the 3D ‘real-world’ coordinate system of the subject, transformations must be applied. These transformations are known as the collinearity equations, and are based on an ‘ideal’ camera, in other words one in which there are no distortions and planarity of the sensor is assumed. In such a camera, there would be no geometric distortion from the lens imaging system, and the transformation from 3D object space to 2D image space is done using a perfect central projection system. In real cameras there are always geometric distortions which mean that the  image points are slightly out of the positions they should be in according to the idealised central projection
	*  bundle adjustment - a reference to the bundles of light rays converging on the optical centre of each camera
	* Interior and Exterior orientation
		- The model describing the geometric properties of the camera and lens is known as the inner or interior orientation or camera intrinsics. This will include modelling of the lens distortion, usually characterised by:
		 	- four radial lens distortion parameters (k1, k2, k3, k4)
			- two decentring lens distortion parameters (p1, p2)
			- determination of the principal distance - equivalent to the calibrated focal length, this is the distance between the image plane and the perspective centre
			- principal point offset
		- the interior orientation describes the parameters required to allow the principles of collinearity to be applied to distorted images
		- the exterior orientation or camera extrinsics describes the position (X, Y, Z) and attitude (roll, pitch, yaw, or omega, phi, kappa) of the camera’s projection centre when the image was taken.
		- A SfM approach, such as that used by Bundler, Agisoft Photoscan or Pix 4D mapper, for example, performs an automatic calibration using, in the case of digital images, some of the EXIF metadata in the image file as a starting point. This defines the camera’s interior orientation and simultaneously calculates the exterior orientations using tie-points identified on the input images in a process known as bundle adjustment (a reference to the bundles of light rays converging on the optical centre of each camera) which seeks to minimise the reprojection errors between observed and predicted image points. Unless a pre-calibrated camera model is used, it does this for every image allowing an increased freedom in image capture beyond traditional photogrammetric processes, such as the use of zoom lenses and uncalibrated camera set-ups.
    - The resulting ‘model’ will be in an arbitrary coordinate frame (and at an arbitrary scale) if no formal control is available. If accurate control measurements are available (i.e. measured points, rather than those generated automatically), they may be used to orient and scale the output, as well as providing refinements to the computed positions of the cameras and a check on the overall accuracy of the model.

#### Steps in the SfM/MVS process
* The SfM part of the process produces a ‘sparse’ point cloud comprising tie points identified and matched across the input images (other ‘products’ are the interior and exterior orientations for each camera, but these are rarely revisited by the end-user). In order to construct the sparse point cloud, several steps are involved.
1. Identification of features, or interest points (IPs) on the images.
  * IPs should have good repeatability
    -  i.e. the same IPs should be detected across images under different lighting conditions and with different levels of image noise, a quality known as invariance
    -  Algorithms:
      - Scale Invariant Feature Transform, or SIFT (Lowe 2004),
  * a similarly robust descriptor for each is also required, which describes a small area of pixels around each IP, to facilitate matching. Many IP detection algorithms generate this descriptor at the same time as the identification of the IPs themselves. The number of IPs identified on each image is often set by the user – the default value in Agisoft Photoscan, for example, is 40,000 per image.
2. Matching of the identified Interest Points (IPs)
  * IP matching and filtering
    - False matches are filtered out using an outlier detection algorithm such as RANdom SAmple Concensus, or RANSAC (Fischer and Bolles, 1981)
  * Once a robust set of IPs have been identified and matched across image pairs, the SfM algorithm needs to estimate the interior and exterior orientations for each image by combining all of the relative orientations of the image pairs in the form of their fundamental matrices (Verhoeven et al 2013).
  * Once complete, a technique called image triangulation is used to calculate the relative position for each image in every pair
  * The overlapping pairs are now combined to form a single block, the optimisation of which is achieved by a bundle adjustment, so called because it necessitates adjusting the ‘bundles’ of rays between each camera’s projection centre and the set of projected 3D points until a minimal discrepancy between the positions of the observed and re-projected points (the image distance between the initial estimated position of a point and its ‘true’ or measured value) is achieved (ibid).
    - In Agisoft Photoscan, for example, the IPs are termed key points
    - Tie points (the sparse cloud points seen in the model view after alignment) are key points that have at least two projections each, i.e. these are key-points that have been matched on two or more images and which therefore become tie-points
    - When a tie-point limit is used, the software will use only the most reliable tie-points on each photo to fit the threshold set by the user (say, the top 1000 per image), which will result in lower number of sparse cloud points, but chosen only from the most reliable matches.
    - Using very high key-point and tie-point limits is rarely productive: it will result in longer processing time and may also affect the accuracy of the resulting alignment because less reliable key-points might be matched, resulting in less accurate tie points being selected.
3. The result of all this is a scale and orientation independent sparse reconstruction. If a minimum of 3 control points are introduced and used as constraints in the bundle adjustment, they may be used to further reduce errors in the reconstruction (such as the ‘dishing’ or ‘bowl’ effect sometimes seen as a result of processing strips of aerial imagery, for example) and will also define a coordinate reference system for the model.
  - In some workflows this is not possible, but Agisoft Photoscan and Pix 4D mapper, for example, do permit it. For accurate reconstructions, it is better to do this than to follow the SfM/MVS pipeline through to completion, produce the model independently and attempt to define a coordinate system afterwards, since no refinement to the reconstruction parameters is possible.
4. Once the SfM part of the process is complete, the dense MVS reconstruction may be undertaken, which effectively involves the re-projection of most of the pixels in each image to form a dense point cloud, which is similar in appearance to that generated by a terrestrial 3D laser scanner.
  - There are many algorithms available to do this, and different software will use different implementations
  - This dense point cloud may then be used as the basis for the formation of a Triangulated Irregular Network (TIN) or mesh, onto which textures generated from the input images may be projected.

* Measurements from different number of images is possible
  - Single Image, Stereo Pair, Multi Images

#### Errors
##### Repojection Error
* When the 3D positions of the tie points are estimated, those points are reprojected onto the images – the difference between the detected and the reprojected point position on an image is the reprojection
error, and is dependent on both the quality of the camera calibration estimates and (in the
case of manually marked points) the accuracy of the marking. It thus provides a good
indication of the accuracy or otherwise of the reconstruction.

##### Sources of error
* There are two main sources of error in photogrammetric processing
  1. Systematic errors
    - Mainly concerned with factors that affect the interior orientation:
      - a) Sensors: Non-planar sensors, Physical errors in the pixel geometry of the sensor, Non-perpendicularity between the plane of the sensor and the lens axis
        * harder to quantify and correct
        * may in some circumstances be helped by calibration
        * planarity of the sensor may be safely assumed
        * other incorrect interior orientation parameters may be resolved during bundle adjustment
          - these may also be improved to some extent by calibration
      - b) Other: Incorrect lens distortion estimates, Incorrect positioning of the principal point, Refraction
 2. Mistakes
  - incorrect matching of points during automated alignment
    - adjustment may be repeated after manually orienting the problem images
  - incorrect identification and/or measurement of control points
    -  misidentification can usually be found quickly and rectified

#### Workflow
- Different software packages using the SfM/MVS workflow operate in a similar fashion and follow the same basic procedures.
1. Planning
2. Reconnaissance
3. Image acquisition.
4. Image pre-processing.
5. Image import.
6. SfM – calculation of interior and exterior orientation, identification of IPs across image set, formation of sparse point cloud which is based on those IPs.
7. Filtering of points (if available). Removal of points with high reprojection errors.
8. MVS – formation of dense point cloud by parsing all images and projecting most of the pixel data contained in them as 3D points provided they can be matched and identified in at least 2 of the input images.
9. Incorporation of control data, alignment optimisation
10. Dense point cloud editing (optional)
11. High resolution mesh generation
12. Generation of outputs
13. Downstream processing and analysis of these outputs in other software (CAD/GIS etc)
14. Presentation
15. Archive

- At all stages there are several possible refinements to this process, many of which considerably increase the likelihood of generating accurate outputs with verifiably good metric performance. The order in which some parts of this workflow are undertaken varies according to the software being used. For example In Agisoft Photoscan Pro it is often useful to build a low resolution dense point cloud and mesh, mark the control points and use these to redefine the alignment before generating a high resolution set of products.
- Sparse point clouds may be filtered to remove points with high reprojection errors in some software
- In general, the RMS of the reprojection errors should be below 1 pixel; the smaller the value, the better the accuracy of the reconstruction
- one should avoid performing the filtering step more than 3 times, as this can introduce a ‘stepping’ effect into the model, and should also avoid removing too many points as reconstruction can become compromised or impossible
-  If the input images are producing very large reprojection errors which cannot be removed, it is likely that they are either of poor quality, or that the camera calibration parameters cannot be accurately determined.
- Although all images should be checked before passing them through the process (primarily in
order to remove those which are comprehensively out of focus or which exhibit significant
motion blur due to incorrect camera settings), some software offers image quality
assessment functionality: none of these methods are perfect, however, and a visual
inspection of the inputs is advised before processing commences. Individual images which
cannot be correctly aligned may be removed, provided there is sufficient redundancy in the
inputs, or may have to be manually aligned by the addition of control points.
- The whole process may be refined by building a low-accuracy dense point cloud and a low-resolution
mesh (in order to enable semi-automated placement of control), then, after carefully positioning all control points and their coordinates, optimising the image alignment using those control points. This will remove the ‘bowl’ effect (see above) and will also greatly increase the accuracy of the reconstruction, depending of course on the accuracy of the control measurements. It will also necessitate re-initiating the MVS part of the pipeline using the newly refined alignments as a basis.

#### Photography
* In photogrammetry, the quality of outputs is almost wholly dependent on the quality of the
inputs.
* In general, optimal exposure for photogrammetry, as in ‘normal’ photography, involves a
balancing act between aperture, shutter speed and sensor sensitivity (ISO value).
* The aim is to produce clean, sharp images of the subject.
  - One should normally aim to use the fastest shutter speed that conditions allow - (to reduce the chance of blurring)
  - To use the lowest ISO setting possible - (thereby reducing image noise)
  - And, to use the optimum aperture to retain sharpness and appropriate depth of field - (often between f/8 and f/11) across the subject.
#### Calibration
#### Resolution and sensor size
#### Depth of Field (DoF)
  - Depth of field is controlled by the aperture settings
#### Film Speed/sensor sensitivity (ISO)
#### Leneses
	- avoid using Image Stabilisation (IS) or Vibration Reduction (VR) functions on lenses or cameras which offer this capability.
	- Tilt and/or shift lenses should also be avoided.
	- Best results will be obtained using prime (fixed focal length) lenses, especially if these have been calibrated
	- Wide angle lenses (e.g. around 28mm) can be very useful for capturing as much of the subject as possible without introducing too much distortion, reducing the number of images required and improving matches between images; but resolution varies across the image.
	- zoom lenses may be employed,
	Although images produced will appear sharper, systems of this sort generally work by moving either the image sensor itself or an optical element group in the lens at or immediately prior to the point of image capture,	both of which result in a slightly offset principle point. The offset between the principle point and the perspective centre is not written to EXIF (when using a digital camera/lens combination, clearly never in the analogue case), and is extremely difficult to calculate or compensate for.
#### Image Format
- all digital cameras record in RAW (digital negative) files which are minimally processed by the camera
- RAW file is converted to JPEG immediately, and the raw information discarded. In this case, the user or automatic settings (e.g. white balance, sharpening and exposure adjustments) are applied to the raw data when the file is written, and a clipped tonal curve is also applied. Once the file is written, these changes cannot be undone.
- The RAW format, in contrast, allows for altering the image post-capture without affecting the original.
- RAW files also preserve the whole dynamic range offered by the camera. The dynamic range may be characterised as the range of luminance that a camera can capture.
- The RAW file will contain information in three main groups:
	* Data Numbers (DNs) - describing the intensity of signal received by each photodiode (pixel) on the sensor
		- the DNs form a greyscale intensity image, which must then be converted to a colour image by the process known as de-mosaicing, in which the intensity of colour in a particular channel can be determined for each pixel using the CFA data, and the other values (for those channels not represented at that particular point) interpolated from those around it.
	* the configuration of the Colour Filter Array (CFA) overlaid on it
		- The CFA is a colour pattern filter overlaid on the sensor which limits the spectral components gathered by each photodiode to (usually) red, green or blue – the commonest is known as a Bayer array, and favours the green channel over the red and blue channels since this arrangement corresponds most closely to the colour perception of the human eye (Verhoeven, 2010.
	* metadata
- In most cameras, the raw image is recorded using 12 or 14 bits (the ‘bit depth’) per channel. 12 bits offers 4096 shades per channel, 14 bits offers 16,384 shades per channel. When converted to JPEG, which only offers 8 bits per channel (or 256 shades) it clearly cannot transmit all of the information available, so some clipping of the dynamic range is necessary, achieved by the application of a tonal curve which will typically clip highlights at the expense of retaining better detail in the darker areas of the image (ibid.). This reduced dynamic range can result in posterisation in the final images.
- A further consideration with JPEG files is their instability during and after processing. Re-saving a JPEG introduces compression errors, and this is compounded every time the file isre-saved, resulting in gradual degradation of image quality (Hass 2007, Verhoeven 2010).
 - If you are using a camera that will only output images in JPEG format, it is advisable to use settings which yield the largest file size and the lowest compression ratio at capture, and to convert the files to TIFF immediately after download
#### Multispectral Imagery
	- Images derived from sensors operating outside the visible Electro-Magnetic (EM) spectrum may be processed using a normal SfM/MVS photogrammetric workflow, and may therefore be used in conjunction with products derived from ‘normal’ Red, Green, Blue channel (RGB) imagery in a number of useful ways for example comparing and analysing near infra-red (NIR) derived orthophotographs with their RGB counterparts. Eg: thermal imagery has proved useful for detecting features in areas where dense vegetation precluded the use of RGB photography. Thermal imaging sensors are usually very low resolution compared to those in most RGB or modified NIR cameras (typically 640x480 or 320x240 pixels, depending on price), and therefore it is processed separately and formal ground control is usually required to register it with imagery derived from other sources.
#### Image enhancement
	- image enhancement should be avoided, and any functions that change the relative values of the pixel structures in an inconsistent manner should certainly not be used when pre-processing images for photogrammetric purposes.

[Streaming raw video data to disk from multiple 1394 cameras](https://www.ptgrey.com/tan/10580)
[How do I acquire and view 16-bit images from my camera?](https://www.ptgrey.com/KB/10065)
[what-is-camera-raw-and-why-would-a-professional-prefer-it-to-jpg](https://www.howtogeek.com/howto/39811/what-is-camera-raw-and-why-would-a-professional-prefer-it-to-jpg/)

### Control
- Use of externally measured control points for the purpose of model refinement, scaling, orientation and checking:here we are concerned with measured, coordinated points on or around the subject of interest.
- the SfM process itself involves the identification of large numbers of tie points between images, and these constitute an internal control network of sorts in their own right.
- Control for photogrammetry usually comprises a set of clear and unambiguous points which appear in the images and for which the coordinate positions are known.
- Control positions may be in any reference system or coordinate frame, depending on the source data
- software is able to handle projected coordinate systems correctly when you import control data
- a lack of control removes the facility to check for, quantify and mediate error
- Control points are used to:
	* Spatially locate data
	* Scale and orient the data
	* And, significantly, may be used for optimisation of the automatic image alignment and the reduction of non-linear errors in the model
- For accurate survey work it is essential
- Redundancy in your control network is useful – you should attempt to have more control points than you need, so that some of them can be used for optimising, scaling and orienting the project and others may be used afterwards as check points, to verify the accuracy of the reconstruction.
- Few basic considerations; Photogrammetric models are, on their own, scale free:-
	* Number of Control Points
		- a) For scaling
			- A minimum of two control points is needed. These need not be 3D coordinates, but may be points identified at the ends of a line of known length measured between two points visible in the images, e.g. a scale bar
		- b) For scaling and orientation
				- A minimum of 3 points is required, 2 of which must be 3D coordinates (i.e. X, Y, Z values) and one of which need only be 1D (X, Y or Z) – these must all be visible in at least 2 images, but in practice should be visible in many more. In practise, most software will actually require three 3D coordinate values for this.
				- With this number of control points, the model may be scaled, positioned and orientated relative to a coordinate frame
				- thus achieve a degree of absolute accuracy, but the relative accuracy of the model will remain unaffected (i.e. the control points are used for scaling and orientation but do not contribute to adjustments in the formation of the model)
		- c) To refine the estimated image alignment and hence the accuracy of the reconstruction
		 		- you will need more than three 3D points; it is advisable to use more than the minimum.
		- d) To verify the accuracy of the reconstruction afterwards
				- those which are not used to refine the alignment
	* Distribution
		- Try to keep control points evenly distributed
		- It is worth noting that most photogrammetric software that deals with external control has extensive documentation available discussing control points and their use



#### Keywords
* IPs - Interest points


### KITTI www.mrt.kit.edu/z/publ/download/2013/GeigerAl2013IJRR.pdf

Our data is calibrated, synchronized and timestamped, and we provide the rectified and raw image sequences.
Our dataset also contains object labels in the form of 3D tracklets and we provide online benchmarks for stereo, optical flow, object detection and other tasks.
3D bounding box tracklets
and a calibration file
The main purpose of this dataset is to push forward the development of computer vision and robotic algorithms targeted to autonomous driving

mainly focuses on the benchmarks, their creation and use for evaluating state-of-the-art computer vision methods, here we complement this information by providing technical details on the raw data itself

how to access the data
comment on sensor limitations
common pitfalls

that the color cameras lack in terms of resolution due to the Bayer pattern interpolation process and are less sensitive to light.
This is the reason why we use two stereo camera rigs, one for grayscale and one for color.

Timestamps are stored in timestamps.txt and perframe sensor readings are provided in the corresponding data sub-folders

Both, color and grayscale images are stored with loss-less compression using 8-bit PNG files.
The engine hood and the sky region have been cropped
The size of the images after rectification depends on the calibration parameters and is ~0.5 Mpx on average

For each frame, we store 30 different GPS/IMU values in a text file:

While the number of points per scan is not constant, on average each file/frame has a size of  1:9 MB which corresponds to  120; 000 3D points and reflectance values.

http://www.prnewswire.com/news-releases/chinese-ai-startup-tusimple-breaks-ten-records-in-autonomous-driving-technology-300343337.html
http://www.tusimple.com/core-en.html

The raw data development kit provided on the KITTI website2 contains MATLAB demonstration code with C++ wrappers and a readme.txt file which gives further details.

- The script run_demoTracklets.m demonstrates how 3D bounding box tracklets can be read from the XML files and projected onto the image plane of the cameras.
- The projection of 3D Velodyne point clouds into the image plane is demonstrated in run_demoVelodyne.m. See Fig. 6 for an illustration.
- The script run_demoVehiclePath.m shows how to read and display the 3D vehicle trajectory using the GPS/IMU data. It makes use of convertOxtsToPose(), which takes as input GPS/IMU measurements and outputs the 6D pose of the vehicle in Euclidean space.
- The function loadCalibrationCamToCam() can be used to read the intrinsic and extrinsic calibration parameters of the four video sensors.
- The other 3D rigid body transformations can be parsed with loadCalibrationRigid()

* details about the benchmarks and evaluation metrics for several computer vision and robotic tasks such as
- stereo, optical flow, visual odometry, SLAM, 3D object detection and 3D object tracking

Pointto-Plane ICP algorithm.
 s(i) 2 N2 . . . . . . . . . . . . original image size (1392  512)
 K(i) 2 R33 . . . . . . . . . calibration matrices (unrectified)
 d(i) 2 R5 . . . . . . . . . . distortion coefficients (unrectified)
 R(i) 2 R33 . . . . . . rotation from camera 0 to camera i
 t(i) 2 R13 . . . . . translation from camera 0 to camera i
 s(i)
rect 2 N2 . . . . . . . . . . . . . . . image size after rectification
 R(i)
rect 2 R33 . . . . . . . . . . . . . . . rectifying rotation matrix
 P(i)
rect 2 R34 . . . . . . projection matrix after rectification

pincushion distortion effect

### Bumblebee2 to point cloud data

* https://github.com/shaboinkin/PointCloud

* http://www.lelaps.de/projects.html
  * https://www.youtube.com/watch?v=be6hVu6N0-s
  * https://sourceforge.net/projects/qcv/

### https://www.cosc.canterbury.ac.nz/research/reports/HonsReps/2009/hons_0908.pdf

1. Before disparity generation can be performed, a camera system needs to be calibrated to calculate its intrinsic and extrinsic parameters that define its internal geometry, and helps provide a relation between 3D world coordinates and 3D camera coordinates.
2. Disparity images provide us with a means to calculate 3D depths of points within an image, relying on cameras set up in a stereo pair for its generation
3. Evaluation of our algorithms 3D depth accuracy
  - we created a test environment to calculate the accuracy of the 3D depth calculations, ground plane estimation, and cricket ball tracking from our algorithm

* Areas of computer vision:
  - plane estimation, and object tracking
* Image segmentation
* Object tracking techniques



Before stereo correspondence can be applied to an image pair, they must first go through undistortion and rectification.
- Undistortion is the process of removing any unwanted lens distortion apparent on the image, this is due to the low focal length (wider angle of view) of a lens.
- Rectification is the process of reprojecting the two image planes from our camera system so that they both lie in the same plane. Doing this provides row-aligned images where feature points of both images reside on the same row, greatly speeding up the process of stereo correspondence, as it only needs to look over one row instead of the entire image to find corresponding feature points.
  - As the rectification reprojects the image plane seen, information could be lost if the two cameras are not looking at the same scene from the same direction. To make this rectification retain as much of the original image planes as possible, it is best to set up the two cameras such that their image planes are coplanar and their principle rays are parallel.

 - In the coplanar configuration of the cameras, there's an inverse relationship between disparity and depth relationship  because of which the accurate depth measurements can only be performed on objects close enough to the camera system so that they can both see in their respective image planes.




### 3D Reconstruction from Multiple Images

**Reference**: CS231a-FinalReport-sgmccann.pdf

#### Objective
The objective of this report is to identify the various approaches to generating sparse 3D reconstructions using the Structure from Motion (SfM) algorithms and the methods to

#### Available Packages

++1. Image to Point Cloud Data generation++
* The majority of the current open-source software software/toolkits are based on the Bundler package, a Structure from Motion system for unordered image collections developed by N. Snavely
* Bundler generates a sparse 3D reconstruction of the scene.
* For dense 3D reconstruction, the preferred approach seems to be to use the multi view stereo packages CMVS and PMVS, developed by Y. Furukawa
* **Bundler**, **CMVS** and **PMVS**
  * Are all command line tools
  * GUI Tools - A number of other projects have developed integrated toolkits and visualization packages based on these tools
    * **OSM Bundler** - a project to integrate Bundler, CMVS and PMVS into Open Street Map
    * **Python Photogrammetry Toolbox (PPT)** - a project to integrate Bundler, CMVS and PMVS into an open-source photogrammetry toolbox by the archeological community
    * **Visual SFM** - a highly optimized and well integrated implementation of Bundler, PMVS and CMVS. Of particular note are the inclusion of a GPU based SIFT algorithm (SiftGPU) and a multi-core implementation of the Bundle Adjustment algorithm. The use of these packages allows VisualSFM to perform incremental Structure from Motion in near linear time.
* The SIFT algorithm was used to compare the images
* The SURF algorithm to detect keypoints and compute de-scriptors.
* SiftGPU finds the camera positions
* PMVS creates a pointcloud from the matched photos

#### Technical Approach

##### Sorting the Photo Collection

##### Feature Detection and Matching

##### Structure From Motion

**Self Calibration/Auto Calibration**
* When dealing with the situation where the intrinsic camera parameters are unknown, one can run the Self Calibration (also known as Auto Calibration) process to estimate the camera parameters from the image features. Possible techniques for Self Calibration include using:-
  * The single-view metrology constraints
  * The direct approach using the Kruppa equations
  * The algebraic approach
  * The stratified approach

###### SfM using Two Images
###### SfM using Multiple Images
With two images, we can reconstuct up to a scale factor. However, this scale factor will be different for each pair of images. How can we find a common scale so that multiple images can be combined?

* Iterative Closest Point (ICP) algorithm
  - Where we triangulate more points and see how they fit into our existing scene geometry
* Perspective N-Point (PnP) algorithm
  - Also known as camera pose estimation, where we try to solve for the position of a new camera using the scene points we have already found

##### Multi View Stereo

* The Multi View Stereo algorithms are used to generate a dense 3D reconstruction of the object or scene.
* The techniques are usually based on the measurement of a consistency function, a function to measure whether \this 3D model is consistent with the input images" ? Generally, the answer is not simple due to the effects of noise and calibration errors.

One of the following two approaches are generally used to build the dense 3D model:

 ++2. visualization of point clouds++
 Several packages are available for visualization of point clouds, notably MeshLab, Cloud- Compare and the Point Cloud Library (PCL) which integrates nicely with OpenCV.

#### Conclusion
* The Structure from Motion and Multi View Stereo algorithms provide viable methods for building 3D models of objects, buildings and scenes. The key issues with the algorithms are they are fairly CPU and memory intensive, especially when trying to do reconstruction at large scale.

* The Visual SFM implementation was found to be much faster than the other toolkits (a few seconds per image vs many seconds to a few minutes per image for others). This was mainly due to use of the GPU for SIFT and the implementation of a multicore bundle adjustment algorithm.

* More work is required to determine how to reconstruct complete 3D models and transform them into meshes that can then be imported into standard 3D modelling software.

### [Supply Chain of 3D Digitization & the Pipeline](http://3dicons-project.eu/eng/Guidelines-Case-Studies/Guidelines2)

Existing tools and methodologies are integrated in a complete supply chain of 3D digitization pipeline which covers all technical and logistic aspects to create 3D models. Each stage in the processing pipeline is interrelated. Data capture, post processing and 3D publishing activities normally occur sequentially after each other. Final potential publishing methodology, and travel back up the supply chain to identify what are the most appropriate capture and modelling techniques to provide this online 3D solution. The interlinked stages are:-
1. 3D Data Capture Techniques
2. Post Processing of 3D Content
3. 3D Publishing Methodology
4. Metadata
5. Licensing & IPR Considerations

#### I. Capture Data - 3D acquisition technologies
>- Non-contact systems are divided into active (those which emit their own electromagnetic energy for surface detection) and passive (those which utilise ambient electromagnetic energy for surface detection).

The capabilities of the different technologies vary in terms of several criteria which must be considered and balanced when formulating appropriate campaign strategies. These include:-
  * Resolution – the minimum quantitative distance between two consecutive measurements.
  * Accuracy - what is the maximum level of recorded accuracy?
  * Range – how close or far away can the device record and object?
  * Sampling rate – the minimum time between two consecutive measurements?
  * Cost – what is the expense of the equipment and software to purchase or lease?
  * Operational environmental conditions – in what conditions will this method work, i.e. is a dark working  environment required?
  * Skill requirements – is extensive training required to carry out the data capture technique?
  * Use – what the 3D data will be used for, i.e. scientific analysis or visualisation?
  * Material – from what substance is the artefact/monument fabricated?

There are significant variations between the capabilities of different approaches. For example, triangulation techniques can produce greater accuracy than time-of-flight, but can only be used at relatively short range. Where great accuracy is a requirement, this can normally only be achieved with close access to the heritage object to be digitized (< 1m). If physical access to the artefact is diffcult or requires the construction of special scaffolding, other constraints need consideration (e.g. using an alternative non-invasive techniques). Alternatively, if physical access is impractical without unacceptable levels of invasive methods, then sensing from a greater distance maybe required utilising direct distance measurement techniques (TOF, Phase Deviation) leading to less accurate results. When selecting the appropriate methodology, consideration must also be given to the length of time available to carry out the data collection process and the relative speed of data capture of each technology.

##### Short Range Techniques

###### Laser Triangulation (LT)
  - The method is based on an instrument that carries a laser source and an optical detector. The laser source emits light in the form of a spot, a line or a pattern on the surface of the object while the optical detector captures the deformations of the light pattern due to the surface’s morphology. The depth is computed by using the triangulation principle.

###### Structured Light (SL)
  - also known as fringe projection systems - is another popular active acquisition method that is based on projecting a sequence of different alternated dark and bright stripes onto the surface of an object and extracting the 3D geometry by monitoring the deformations of each pattern. By examining the edges of each line in the pattern, the distance from the scanner to the object’s surface is calculated by trigonometric triangulation.

##### Long & Mid Range Techniques

###### Time-Of-Flight (TOF)
  - also known as terrestrial laser scanning - is an active method commonly used for the 3D digitisation of architectural heritage (e.g. an urban area of cultural importance, a monument, an excavation, etc). The method relies on a laser rangefinder which is used to detect the distance of a surface by timing the round-trip time of a light pulse. By rotating the laser and sensor (usually via a mirror), the scanner can scan up to a full 360 degrees around itself. The accuracy of such systems is related to the precision of its timer. For longer distances (modern systems allow the measurement of ranges up to 6km), TOF systems provide excellent results. An alternative approach to TOF scanning is Phase-Shift (PS), also an active acquisition method, used in closer range distance measurements systems. Again they are based on the round trip of the laser pulse but instead of timing the trip they measure the wavelength phase difference between the outgoing and return laser pulse to provide a more precise measurement.

##### Multi Scale Image based Methods

###### Traditional Photogrammetry

* **In principle, image-based methods involves:-**
    * stereo calibration
    * feature extraction
    * feature correspondence analysis, and
    * depth computation based on corresponding points

    It involves the challenging task of correctly identifying common points between images. Photogrammetry is the primary image-based method that is used to determine the 2D and 3D geometric properties of the objects that are visible in an image set.

* **Fundamental photogrammetric problem**
  - The determination of:
  1. Camera interior and exterior orientation parameters
    * the attitude
    * the position of the camera
    * the intrinsic geometric characteristics of the camera
  2. The determination of the 3D coordinates of points on the images

  - Photogrammetry can be divided into two categories:-
    * Aerial photogrammetry
      - images are acquired via overhead shots from an aircraft or an UAV.
    * Terrestrial photogrammetry
      - images are captured from locations near or on the surface of the earth. Additionally, when the object size and the distance between the camera and object are less than 100m then terrestrial photogrammetry is also defined as close range photogrammetry.
  - Accuracy of photogrammetric measurements
    The accuracy of photogrammetric measurements is largely a function of:-
      * camera’s optics quality, and
      * sensor resolution
    Current commercial and open photogrammetric software solutions are able to quickly perform tasks such as ++camera calibration++, ++epipolar geometry computations++ and ++textured map 3D mesh generation++. When combined with accurate measurements derived from a total station for example it can produce models of high accuracy for scales of 1:100 and even higher.

##### Semi Automated Image Based Methods

###### Structure-From-Motion (SFM)
  - SFM is considered an extension of stereo vision, where instead of image pairs the method attempts to reconstruct depth from a number of unordered images that depict a static scene or an object from arbitrary viewpoints. Apart from the ++feature extraction phase++, ++the trajectories of corresponding features over the image collection++ are also computed. The method mainly uses the corresponding features, which are shared between different images that depict overlapping areas, to calculate the intrinsic and extrinsic parameters of the camera. These parameters are related to the ++focal length++, ++the image format++, ++the principal point++, ++the lens distortion coefficients++, ++the location of the projection centre++ and ++the image orientation in 3D space++. To improve the accuracy of calculating the camera trajectory within the image collection:
  - minimise the projection error, and
  - prevent the error-built up of the camera position tracking

###### Dense Multi-View 3D Reconstruction (DMVR)



#### II. Modelling - 3D Post Processing
> - 3D post-processing is a complex procedure consisting of a sequence of processing steps that result in the direct improvement of acquired 3D data, and its transformation into visually enriched geometric representations.
- The results of the post-processing phase are 3D geometric representations accompanied by complementary 2D media, which are the digital assets ready to be converted (or embedded) into the final web publishing formats.

##### Post-Process A - Geometric reconstruction
- Relevant techniques which must be chosen based upon:-
	- The morphological complexity of the object
	- THe scale of the object
	- What the final model will be used for

###### Automatic meshing from a dense 3D point cloud
- The simple criteria for choosing and evaluating 3D geometric reconstruction technique is the degree of consistency of the 3D model compared to the real object.
- Reconstructions can be Interactive or semi-automatic based on:-
	* relevant profiles
	* primitives adjustment
	* technical iconography - plans, cross-sections and elevation
	* artistic iconography - sketches, paintings, etc.

###### Point cloud data
Digitised the initial results (raw data) can be represented by a series of three dimensional data points in a coordinate system commonly called a point cloud. The processing of point clouds involves following phases:-
1. Cleaning Phase - The cleaning phase involves the removal of all the non-desired data.
2. Alignment Phase

++Characteristic of Raw Data++

1. ++Non-desired data++
	- It would include the poorly captured surface areas (e.g. high deviation between laser beam and surface’s normal), the areas that belong to other bjects (e.g. survey apparatus, people), the outlying points and any other badly captured areas.

2. ++Data Noise++
	- Noise can be described as the random spatial displacement of vertices around the actual surface that is being digitised. Compared to active scanning techniques such as laser scanning, image based techniques suffer more from noise artefacts. Noise fifiltering is in an essential step that requires cautious application as it effects the fifine morphological details been described by the data.

###### Processing mesh data

> **Production of a surfaced or “wrapped” 3D model**
The transformation of point cloud data into a surface of triangular meshes is the procedure of grouping triplets of point cloud vertices to compose a triangle. Several processes must be completed to produce a topologically correct 3D mesh model.

++1. Mesh Cleaning++
- Incomplete or problematic data - Discontinuities (e.g. holes) in the data are introduced in each partial scan due to occlusions, accessibility limitation or even challenging surface properties.
- Additional problems identified in a mesh may include spikes, unreferenced vertices, and nonmanifold edges, and these should also be removed during the cleaning stage.

++2. Mesh Simplification or Decimation++
- Mesh simplification methods reduce the amount of data ( i.e. by reducing the number of vertices of a triangulated mesh) required to describe the surface of an object while retaining the geometrical quality of the 3D model (i.e. while maintaining the overall appearance of the object) within the specifications of a given application.
- It's required because, the size of the raw data is often prohibitive for interactive visualisation applications.

**Methods**
* quadric edge collapse decimation
	- This method merges the common vertices from adjacent triangles that lie on flat surfaces, aiming to reduce the polygons number without sacrificing significant details from the object.

**Softwares**
- MeshLab
- Geomagic Wrap

3. Mesh Retopologisation
	- Extreme simplification of complex meshes
	- Decimating a mesh at an extreme level can be achieved by an empirical technique called retopology

**Retopology**
- This is a 3D modelling technique, where special tools are used by the operator to generate a simpler version of the original dense model, by utilising the original topology as a supportive underlying layer. This technique keeps the number of polygons at an extreme minimum, while at the same time allow the user to select which topological features should be preserved from the original geometry.

**Softwares** - that can be used to perform the retopology technique include:
- 3D Coat
- Mudbox
- Blender
- ZBrush
- GSculpt
- Meshlab Retopology Tool ver 1.2.
	- Mesh retopologisation can be a time consuming process, however, it produces better quality light weight topology than automatic decimation. It also facilitates the creation of humanly recognizable texture maps.

++ 4. Texture Mapping++

**2D relief maps**
- They can carry high frequency information about detailed topological features such as bumps, cracks and glyphs. Keeping this type of morphological features in the actual 3D mesh data requires a huge amount of additional polygons. However, expressing this kind of information as a 2D map and applying it while rendering the geometry
can be by far more efficient.

**Displacement maps**
- They are generated using specialised 3D data processing software. The software compares the distance from each texel on the surface of the simplified mesh against the surface of the original mesh and creates a 2D bitmap-based displacement map.

**Different texture maps** - which can be employed to enhance the display of a lightweight 3D model:-
- UV map
- Normal map
- Image map
- Ambient occlusion map (DISCOVERY PROGRAMME)

**Software**
- xNormal (open source)
	-  xNormal is an application to generate normal / ambient occlusion / displacement maps. It can also project the texture of the highpoly model into the lowpoly mesh ( complete texture transfer, even with different topologies ).

##### Post-Process B - Model structuring

A geometric 3D reconstruction of an artefact, architectural detail or an archaeological site generally leads to the representation of a single (and complex) geometric mesh or a collection of geometric entities organized according to several criteria.
According to the chosen model structuring strategy, the final dataset structure (including geometry and visual enrichment) can
be composed in several ways.

##### Post-Process C - Visual enrichment of 3D models
The visual enrichment techniques described below are ordered from those that ensure a strong geometric consistency with the real object to techniques that introduce increasing approximations:

* Texture extraction and projection starting from photographs finely oriented on the 3D model (e.g. image bsed modelling, photogrammetry)
* Texturing by photographic samples of the real materials of the artefact
* Tecturing by generic shaders
* Reconstructions can be Interactive or semi-automatic based on:-
	* relevant profiles
	* primitives adjustment
	* technical iconography - plans, cross-sections and elevation
	* artistic iconography - sketches, paintings, etc.

##### Post Process D - Hypothetical reconstruction
- Some specfific technical and methodological issues with 3D graphical representation of missing (or partially destroyed) heritage buildings are often integrated in 3D reconstruction approaches.
- the methodological approaches for the creation of hypothetical reconstructions can be based on the integration of 3D metric data of existing parts of the object together with the reconstruction of the object’s shapes starting from graphical representations of the artefact/monument. Depending upon the source material available 3D may be created based upon a combination of the following methods:-
	- the 3D acquisition of existing parts
	- previou 2D surveys of existing parts
	- non-metric iconographic sources of the studied artefact
	- iconographoc sources

##### Creating complementary 2D media (derived from the 3D model)
- 2D media can be produced in different ways, depending on:-
* **The type of 3D source**
	- point cloud
	- geometric model
	- visually enriched 3D model
* **The fifinal visualization type**
	- static
	- dynamic
	- interactive
This additional content can be used to visualise content which cannot be successfully visualised through an interactive 3D web model, e.g. renderings of highly detailed 3D models or visualisation of full point cloud datasets.

1. Static Images
	* 3D renderings of visually enriched models from several perspectives
	* Elevations, plans and sections of point cloud data
	* Images highlighting specific features of the cultral object
2. Animation
	* Turn table video
	* Flythough animation and video tours
	* Structural animation
	* Temporal animation
3. Interactive Images
	* Panoramas
	* VR Objects

#### III. 3D Publishing Methodology
##### Online publication technologies
###### 3D PDF
###### HTML5/WebGL
###### Unity3D/UnReal
###### Pseudo-3D


---

### KITTI

**Reference**
* [Google Book Review](https://books.google.co.in/books?id=igFxpngN1lsC&pg=PA242&lpg=PA242&dq=stereo+camera+and+velodyne+calibration&source=bl&ots=WQeHtdaFNd&sig=KbEMP5u9MkDM4q8DOsEPetKDlBU&hl=en&sa=X&ved=0ahUKEwiHyryBuJLRAhWIvo8KHTQyBowQ6AEIUjAI#v=onepage&q=stereo%20camera%20and%20velodyne%20calibration&f=false)

Avineon India used a combination of Bentley Map, MicroStation, and third-party software to successfully generate a highly accurate 3D model from LiDAR point-cloud data, orthophotos, stereo pairs, oblique images, digital terrain models, and vectorized datasets. - See more at: https://www.bentley.com/en/project-profiles/avineon-india_creation-of-3d-city-model-for-city-of-brussels-using-lidar-point-cloud-data

* KITTI
	* The dataset provides accurate 3D bounding boxes for object classes such as cars, vans, trucks, pedestrians, cyclist and trams. It obtain this information by manually labeling objects in 3D point clouds produced by Velodyne system, and projecting them back into the image. This results in tracklets with accurate 3D poses, which can be used to asses the performance of algorithms for 3D orientation estimation and 3D tracking.
	* Challanges
		* collection of large amounts of data in real time
		* the calibration of diverse sensors working at different rates
		* the generation of ground truth minimizing the amount of supervision required
		* the selection of the appropriate sequences and frames for each benchmark
		* development of the metrics for each task
	* Sensors and Data Acquisition
		*  Color images are very useful for tasks such as segmentatioin and object detection, but provide lower contrast and sensitivity compared to their grayscale counterparts, which is of key importance in stereo matching and optical flow estimation.
	* Sensor calibration
		* Accurate sensor calibration is key for obtaining reliable ground truth. Calibration pipeline:-
			* Calibrate the video cameras intrinsically and extrinsically and rectify the input images
			* Find the 3D rigid motion parameters which relate the coordinate system of the laser scanner the localization unit and the reference camera.
			* Camera-to-Camera and GPS/IMU-to-Velodyne registration methods are fully automatic, the Velodyne-to-Camera calibration requires the user to manually select a small number of correspondences between the laser and the camera images. This was necessary as existing techniques for this task are not accurate enough to compute ground truth estimates.
				* **Camera-to-Camera calibration**: TO automatically calibrate the intrinsic and extrinsic parametes of the cameras, mounted the checkerboard patters onto the walls and detect corners in the calibration images. Based on gradient information and discrete energy-minimization, assigned corners to checkerboards, match them between the cameras and optimize all parameters by minimizing the average reprojection error.
				* **Velodyne-to-Camera calibration**: Registering the laser scanner with the cameras is non-trivial as correspondences are hard to establish due to the large amount of noise in the reflectance values. Therefore, rely on semi-automatic technique

* * Errors
	* caliration and laser measurement errors
	* error of the trajectory end-point
	*  

## References & Dataset
* http://adas.cvc.uab.es/elektra/datasets/stereo/
* http://adas.cvc.uab.es/webfiles/ppt/MED2016.pdf
* https://github.com/dhernandez0/sgm/blob/master/main.cu
* https://github.com/dhernandez0/sgm
* http://adas.cvc.uab.es/elektra/datasets/
* http://www.pi3dscan.com/index.php/instructions/item/agisoft-vs-capturingreality
* http://wedidstuff.heavyimage.com/index.php/2013/07/12/open-source-photogrammetry-workflow/
* http://3dstereophoto.blogspot.in/p/software.html
* http://opencvpython.blogspot.in/2012/05/install-opencv-in-windows-for-python.html
* https://sourceforge.net/projects/opencvlibrary/
* http://www.academia.edu/29948794/Development_and_Status_of_Image_Matching_in_Photogrammetry
* http://www.lidarmap.org/
* https://www.blendernation.com/2016/10/24/free-photo-scanning-workflow-visualsfm-meshlab-blender
* https://www.cis.rit.edu/~cnspci/references/dip/urban_extraction/leberl2010.pdf
* https://erget.wordpress.com/2014/04/27/producing-3d-point-clouds-with-a-stereo-camera-in-opencv/
* https://erget.wordpress.com/2014/02/01/calibrating-a-stereo-camera-with-opencv/
* https://erget.wordpress.com/2014/02/28/calibrating-a-stereo-pair-with-python/
* https://erget.wordpress.com/2014/03/13/building-an-interactive-gui-with-opencv/
* http://erget.github.io/StereoVision/
* http://docs.opencv.org/2.4/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html#stereobm
* https://hackaday.io/project/12037-diy-stereo-camera/log/39655-visualsfm-and-related
* https://trac.fawkesrobotics.org/wiki/Plugins/bumblebee2
* https://www.youtube.com/watch?v=lOwWNV9rpcc&list=PL3cpeZTQSqXf6UMOLCLevpChaH6-mC5Sj&index=7
* https://en.wikipedia.org/wiki/Visual_odometry

## Datasets/Benchmark suite
### Cityscape Dataset, benchmark suite
* https://www.cityscapes-dataset.com/dataset-overview/

### The KITTI Dataset, benchmark suite
* http://www.cvlibs.net/datasets/kitti/index.php

## Exercises/Tutorials
* VisualSFM, MeshLab, Blender
  * Tutorial 1
    * http://www.creativeshrimp.com/free-photo-scanning-tutorial.html
    * https://youtu.be/GEAbXYDzUjU
  * Tutorial 2
    * http://flightriot.com/visualsfm-cmvs-post-processing-tutorial/
  * http://www.academia.edu/3649828/Generating_a_Photogrammetric_model_using_VisualSFM_and_post-processing_with_Meshlab

## Nasa Free Software Suites
* http://software.nasa.gov/

## Literature Review

### Photogrammetric applications for cultural heritage

**References**
  -[photogrammetric-applications-for-cultural-heritage.pdf](https://content.historicengland.org.uk/content/docs/guidance/draft-photogrammetric-applications-for-cultural-heritage.pdf)

## Notes
* multi-image convergent photogrammetric developments i.e. those using a combination of Structure from Motion (SfM) and Multi-View Stereo (MVS) workflows.

## Photogrammetry Concepts
* **Chief ray**
  - Intersection of two rays to locate object point
* **Collinearity**
  - Given the assumption that the object point, camera projection centre and image point are in a straight line, in order to translate between the 2D image coordinate system, with its origin at the centre of the image (as opposed to the principle point, which is the orthogonal projection of the projection centre on the sensor, hence the necessary computation of principle point offset values) and the 3D ‘real-world’ coordinate system of the subject, transformations must be applied. These transformations are known as the collinearity equations, and are based on an ‘ideal’ camera, in other words one in which there are no distortions and planarity of the sensor is assumed. In such a camera, there would be no geometric distortion from the lens imaging system, and the transformation from 3D object space to 2D image space is done using a perfect central projection system. In real cameras there are always geometric distortions which mean that the  image points are slightly out of the positions they should be in according to the idealised central projection.
* **Bundle Adjustment**
  - A reference to the bundles of light rays converging on the optical centre of each camera
* **Interior and Exterior orientation**
  - The model describing the geometric properties of the camera and lens is known as the inner or interior orientation or camera intrinsics. This will include modelling of the lens distortion, usually characterised by:
    - four radial lens distortion parameters (k1, k2, k3, k4)
    - two decentring lens distortion parameters (p1, p2)
    - determination of the principal distance - equivalent to the calibrated focal length, this is the distance between the image plane and the perspective centre
    - principal point offset
  - the interior orientation describes the parameters required to allow the principles of collinearity to be applied to distorted images
  - the exterior orientation or camera extrinsics describes the position (X, Y, Z) and attitude (roll, pitch, yaw, or omega, phi, kappa) of the camera’s projection centre when the image was taken.
  - A SfM approach, such as that used by Bundler, Agisoft Photoscan or Pix 4D mapper, for example, performs an automatic calibration using, in the case of digital images, some of the EXIF metadata in the image file as a starting point. This defines the camera’s interior orientation and simultaneously calculates the exterior orientations using tie-points identified on the input images in a process known as bundle adjustment (a reference to the bundles of light rays converging on the optical centre of each camera) which seeks to minimise the reprojection errors between observed and predicted image points. Unless a pre-calibrated camera model is used, it does this for every image allowing an increased freedom in image capture beyond traditional photogrammetric processes, such as the use of zoom lenses and uncalibrated camera set-ups.
  - The resulting ‘model’ will be in an arbitrary coordinate frame (and at an arbitrary scale) if no formal control is available. If accurate control measurements are available (i.e. measured points, rather than those generated automatically), they may be used to orient and scale the output, as well as providing refinements to the computed positions of the cameras and a check on the overall accuracy of the model.

### Steps in the SfM/MVS process
* The SfM part of the process produces a ‘sparse’ point cloud comprising tie points identified and matched across the input images (other ‘products’ are the interior and exterior orientations for each camera, but these are rarely revisited by the end-user). In order to construct the sparse point cloud, several steps are involved.
1. Identification of features, or interest points (IPs) on the images.
  * IPs should have good repeatability
  i.e. the same IPs should be detected across images under different lighting conditions and with different levels of image noise, a quality known as invariance
    -  Algorithms:
      - Scale Invariant Feature Transform, or SIFT (Lowe 2004),
  * a similarly robust descriptor for each is also required, which describes a small area of pixels around each IP, to facilitate matching. Many IP detection algorithms generate this descriptor at the same time as the identification of the IPs themselves. The number of IPs identified on each image is often set by the user – the default value in Agisoft Photoscan, for example, is 40,000 per image.
2. Matching of the identified Interest Points (IPs)
  * IP matching and filtering
    - False matches are filtered out using an outlier detection algorithm such as RANdom SAmple Concensus, or RANSAC (Fischer and Bolles, 1981)
  * Once a robust set of IPs have been identified and matched across image pairs, the SfM algorithm needs to estimate the interior and exterior orientations for each image by combining all of the relative orientations of the image pairs in the form of their fundamental matrices (Verhoeven et al 2013).
  * Once complete, a technique called image triangulation is used to calculate the relative position for each image in every pair
  * The overlapping pairs are now combined to form a single block, the optimisation of which is achieved by a bundle adjustment, so called because it necessitates adjusting the ‘bundles’ of rays between each camera’s projection centre and the set of projected 3D points until a minimal discrepancy between the positions of the observed and re-projected points (the image distance between the initial estimated position of a point and its ‘true’ or measured value) is achieved (ibid).
    - In Agisoft Photoscan, for example, the IPs are termed key points
    - Tie points (the sparse cloud points seen in the model view after alignment) are key points that have at least two projections each, i.e. these are key-points that have been matched on two or more images and which therefore become tie-points
    - When a tie-point limit is used, the software will use only the most reliable tie-points on each photo to fit the threshold set by the user (say, the top 1000 per image), which will result in lower number of sparse cloud points, but chosen only from the most reliable matches.
    - Using very high key-point and tie-point limits is rarely productive: it will result in longer processing time and may also affect the accuracy of the resulting alignment because less reliable key-points might be matched, resulting in less accurate tie points being selected.
3. The result of all this is a scale and orientation independent sparse reconstruction. If a minimum of 3 control points are introduced and used as constraints in the bundle adjustment, they may be used to further reduce errors in the reconstruction (such as the ‘dishing’ or ‘bowl’ effect sometimes seen as a result of processing strips of aerial imagery, for example) and will also define a coordinate reference system for the model.
  - In some workflows this is not possible, but Agisoft Photoscan and Pix 4D mapper, for example, do permit it. For accurate reconstructions, it is better to do this than to follow the SfM/MVS pipeline through to completion, produce the model independently and attempt to define a coordinate system afterwards, since no refinement to the reconstruction parameters is possible.
4. Once the SfM part of the process is complete, the dense MVS reconstruction may be undertaken, which effectively involves the re-projection of most of the pixels in each image to form a dense point cloud, which is similar in appearance to that generated by a terrestrial 3D laser scanner.
  - There are many algorithms available to do this, and different software will use different implementations
  - This dense point cloud may then be used as the basis for the formation of a Triangulated Irregular Network (TIN) or mesh, onto which textures generated from the input images may be projected.

* Measurements from different number of images is possible
  - Single Image, Stereo Pair, Multi Images

### Errors
#### Repojection Error
* When the 3D positions of the tie points are estimated, those points are reprojected onto the images – the difference between the detected and the reprojected point position on an image is the reprojection
error, and is dependent on both the quality of the camera calibration estimates and (in the
case of manually marked points) the accuracy of the marking. It thus provides a good
indication of the accuracy or otherwise of the reconstruction.

#### Sources of error
* There are two main sources of error in photogrammetric processing
  1. Systematic errors
    - Mainly concerned with factors that affect the interior orientation:
      - a) Sensors: Non-planar sensors, Physical errors in the pixel geometry of the sensor, Non-perpendicularity between the plane of the sensor and the lens axis
        * harder to quantify and correct
        * may in some circumstances be helped by calibration
        * planarity of the sensor may be safely assumed
        * other incorrect interior orientation parameters may be resolved during bundle adjustment
          - these may also be improved to some extent by calibration
      - b) Other: Incorrect lens distortion estimates, Incorrect positioning of the principal point, Refraction
 2. Mistakes
  - incorrect matching of points during automated alignment
    - adjustment may be repeated after manually orienting the problem images
  - incorrect identification and/or measurement of control points
    -  misidentification can usually be found quickly and rectified

## Photogrammetry Workflow
- Different software packages using the SfM/MVS workflow operate in a similar fashion and follow the same basic procedures.
1. Planning
2. Reconnaissance
3. Image acquisition.
4. Image pre-processing.
5. Image import.
6. SfM – calculation of interior and exterior orientation, identification of IPs across image set, formation of sparse point cloud which is based on those IPs.
7. Filtering of points (if available). Removal of points with high reprojection errors.
8. MVS – formation of dense point cloud by parsing all images and projecting most of the pixel data contained in them as 3D points provided they can be matched and identified in at least 2 of the input images.
9. Incorporation of control data, alignment optimisation
10. Dense point cloud editing (optional)
11. High resolution mesh generation
12. Generation of outputs
13. Downstream processing and analysis of these outputs in other software (CAD/GIS etc)
14. Presentation
15. Archive

- At all stages there are several possible refinements to this process, many of which considerably increase the likelihood of generating accurate outputs with verifiably good metric performance. The order in which some parts of this workflow are undertaken varies according to the software being used. For example In Agisoft Photoscan Pro it is often useful to build a low resolution dense point cloud and mesh, mark the control points and use these to redefine the alignment before generating a high resolution set of products.
- Sparse point clouds may be filtered to remove points with high reprojection errors in some software
- In general, the RMS of the reprojection errors should be below 1 pixel; the smaller the value, the better the accuracy of the reconstruction
- one should avoid performing the filtering step more than 3 times, as this can introduce a ‘stepping’ effect into the model, and should also avoid removing too many points as reconstruction can become compromised or impossible
-  If the input images are producing very large reprojection errors which cannot be removed, it is likely that they are either of poor quality, or that the camera calibration parameters cannot be accurately determined.
- Although all images should be checked before passing them through the process (primarily in
order to remove those which are comprehensively out of focus or which exhibit significant
motion blur due to incorrect camera settings), some software offers image quality
assessment functionality: none of these methods are perfect, however, and a visual
inspection of the inputs is advised before processing commences. Individual images which
cannot be correctly aligned may be removed, provided there is sufficient redundancy in the
inputs, or may have to be manually aligned by the addition of control points.
- The whole process may be refined by building a low-accuracy dense point cloud and a low-resolution
mesh (in order to enable semi-automated placement of control), then, after carefully positioning all control points and their coordinates, optimising the image alignment using those control points. This will remove the ‘bowl’ effect (see above) and will also greatly increase the accuracy of the reconstruction, depending of course on the accuracy of the control measurements. It will also necessitate re-initiating the MVS part of the pipeline using the newly refined alignments as a basis.

### Photography
* In photogrammetry, the quality of outputs is almost wholly dependent on the quality of the
inputs.
* In general, optimal exposure for photogrammetry, as in ‘normal’ photography, involves a
balancing act between aperture, shutter speed and sensor sensitivity (ISO value).
* The aim is to produce clean, sharp images of the subject.
  - One should normally aim to use the fastest shutter speed that conditions allow - (to reduce the chance of blurring)
  - To use the lowest ISO setting possible - (thereby reducing image noise)
  - And, to use the optimum aperture to retain sharpness and appropriate depth of field - (often between f/8 and f/11) across the subject.
#### Calibration
#### Resolution and sensor size
#### Depth of Field (DoF)
  - Depth of field is controlled by the aperture settings
#### Film Speed/sensor sensitivity (ISO)
#### Leneses
  - avoid using Image Stabilisation (IS) or Vibration Reduction (VR) functions on lenses or cameras which offer this capability.
  - Tilt and/or shift lenses should also be avoided.
  - Best results will be obtained using prime (fixed focal length) lenses, especially if these have been calibrated
  - Wide angle lenses (e.g. around 28mm) can be very useful for capturing as much of the subject as possible without introducing too much distortion, reducing the number of images required and improving matches between images; but resolution varies across the image.
  - zoom lenses may be employed,
  Although images produced will appear sharper, systems of this sort generally work by moving either the image sensor itself or an optical element group in the lens at or immediately prior to the point of image capture, both of which result in a slightly offset principle point. The offset between the principle point and the perspective centre is not written to EXIF (when using a digital camera/lens combination, clearly never in the analogue case), and is extremely difficult to calculate or compensate for.
#### Image Format
- all digital cameras record in RAW (digital negative) files which are minimally processed by the camera
- RAW file is converted to JPEG immediately, and the raw information discarded. In this case, the user or automatic settings (e.g. white balance, sharpening and exposure adjustments) are applied to the raw data when the file is written, and a clipped tonal curve is also applied. Once the file is written, these changes cannot be undone.
- The RAW format, in contrast, allows for altering the image post-capture without affecting the original.
- RAW files also preserve the whole dynamic range offered by the camera. The dynamic range may be characterised as the range of luminance that a camera can capture.
- The RAW file will contain information in three main groups:
  * Data Numbers (DNs) - describing the intensity of signal received by each photodiode (pixel) on the sensor
    - the DNs form a greyscale intensity image, which must then be converted to a colour image by the process known as de-mosaicing, in which the intensity of colour in a particular channel can be determined for each pixel using the CFA data, and the other values (for those channels not represented at that particular point) interpolated from those around it.
  * the configuration of the Colour Filter Array (CFA) overlaid on it
    - The CFA is a colour pattern filter overlaid on the sensor which limits the spectral components gathered by each photodiode to (usually) red, green or blue – the commonest is known as a Bayer array, and favours the green channel over the red and blue channels since this arrangement corresponds most closely to the colour perception of the human eye (Verhoeven, 2010.
  * metadata
- In most cameras, the raw image is recorded using 12 or 14 bits (the ‘bit depth’) per channel. 12 bits offers 4096 shades per channel, 14 bits offers 16,384 shades per channel. When converted to JPEG, which only offers 8 bits per channel (or 256 shades) it clearly cannot transmit all of the information available, so some clipping of the dynamic range is necessary, achieved by the application of a tonal curve which will typically clip highlights at the expense of retaining better detail in the darker areas of the image (ibid.). This reduced dynamic range can result in posterisation in the final images.
- A further consideration with JPEG files is their instability during and after processing. Re-saving a JPEG introduces compression errors, and this is compounded every time the file isre-saved, resulting in gradual degradation of image quality (Hass 2007, Verhoeven 2010).
 - If you are using a camera that will only output images in JPEG format, it is advisable to use settings which yield the largest file size and the lowest compression ratio at capture, and to convert the files to TIFF immediately after download
#### Multispectral Imagery
  - Images derived from sensors operating outside the visible Electro-Magnetic (EM) spectrum may be processed using a normal SfM/MVS photogrammetric workflow, and may therefore be used in conjunction with products derived from ‘normal’ Red, Green, Blue channel (RGB) imagery in a number of useful ways for example comparing and analysing near infra-red (NIR) derived orthophotographs with their RGB counterparts. Eg: thermal imagery has proved useful for detecting features in areas where dense vegetation precluded the use of RGB photography. Thermal imaging sensors are usually very low resolution compared to those in most RGB or modified NIR cameras (typically 640x480 or 320x240 pixels, depending on price), and therefore it is processed separately and formal ground control is usually required to register it with imagery derived from other sources.
#### Image enhancement
  - image enhancement should be avoided, and any functions that change the relative values of the pixel structures in an inconsistent manner should certainly not be used when pre-processing images for photogrammetric purposes.

[Streaming raw video data to disk from multiple 1394 cameras](https://www.ptgrey.com/tan/10580)
[How do I acquire and view 16-bit images from my camera?](https://www.ptgrey.com/KB/10065)
[what-is-camera-raw-and-why-would-a-professional-prefer-it-to-jpg](https://www.howtogeek.com/howto/39811/what-is-camera-raw-and-why-would-a-professional-prefer-it-to-jpg/)

### Control
- Use of externally measured control points for the purpose of model refinement, scaling, orientation and checking:here we are concerned with measured, coordinated points on or around the subject of interest.
- the SfM process itself involves the identification of large numbers of tie points between images, and these constitute an internal control network of sorts in their own right.
- Control for photogrammetry usually comprises a set of clear and unambiguous points which appear in the images and for which the coordinate positions are known.
- Control positions may be in any reference system or coordinate frame, depending on the source data
- software is able to handle projected coordinate systems correctly when you import control data
- a lack of control removes the facility to check for, quantify and mediate error
- Control points are used to:
  * Spatially locate data
  * Scale and orient the data
  * And, significantly, may be used for optimisation of the automatic image alignment and the reduction of non-linear errors in the model
- For accurate survey work it is essential
- Redundancy in your control network is useful – you should attempt to have more control points than you need, so that some of them can be used for optimising, scaling and orienting the project and others may be used afterwards as check points, to verify the accuracy of the reconstruction.
- Few basic considerations; Photogrammetric models are, on their own, scale free:-
  * Number of Control Points
    - a) For scaling
      - A minimum of two control points is needed. These need not be 3D coordinates, but may be points identified at the ends of a line of known length measured between two points visible in the images, e.g. a scale bar
    - b) For scaling and orientation
        - A minimum of 3 points is required, 2 of which must be 3D coordinates (i.e. X, Y, Z values) and one of which need only be 1D (X, Y or Z) – these must all be visible in at least 2 images, but in practice should be visible in many more. In practise, most software will actually require three 3D coordinate values for this.
        - With this number of control points, the model may be scaled, positioned and orientated relative to a coordinate frame
        - thus achieve a degree of absolute accuracy, but the relative accuracy of the model will remain unaffected (i.e. the control points are used for scaling and orientation but do not contribute to adjustments in the formation of the model)
    - c) To refine the estimated image alignment and hence the accuracy of the reconstruction
        - you will need more than three 3D points; it is advisable to use more than the minimum.
    - d) To verify the accuracy of the reconstruction afterwards
        - those which are not used to refine the alignment
  * Distribution
    - Try to keep control points evenly distributed
    - It is worth noting that most photogrammetric software that deals with external control has extensive documentation available discussing control points and their use


#### Keywords
* IPs - Interest points

## Google Search Keywords/phraes
* using the 3D depth map for 3D motion tracking
* Gridding lidar point cloud data to generate Digital Elevation Models (DEMs)
  * http://www.opentopography.org/otsoftware/points2grid
* Photogrammetry with stereo compilation
* Lidar georeferenced images
* optical flow fields are obtained by projecting the 3D points into the next frame
* stereo matching and optic flow, estimating egomotion (3D motion)
* (3D Analyst, Spatial Analyst, Geostatistical Analyst) ArcGIS, ESRI
* Streetside Photogrammetric Dense Matching and Kinematic Lidar

## Keywords

* Stereo Camera
* LiDAR - Light Detection And Ranging
* DTM - Digital Terrain Models
* DSM - Digtial Surface Models
* CHM - Canopy Height Models
* DEM - Digital Elevation Models
* SLAM - Simultaneous Localization And Mapping
* RTAB-Map - Real-Time Appearance-Based Mapping
* Autonomous and semi-autonomous systems
* Computer vision
* Stereo Vision
* Baseline - stereo vision system, cameras are horizontally aligned and separated by a distance known as the baseline.
* Disparity Map
* Stereo Ranging
* Interpolation - It is a tool used in image tasks such as zooming, shrinking, rotation, and geometric corrections. Defined, interpolation is the process of using known data to estimate values at unknown locations (Gonzalez & Woods, 2008).
* PPS - Pulse Per Second (PPS signal)
* NMEA $GPRMC message
* Triangulation - The method of determining depth from disparity d is called triangulation.
* Orthophoto / orthophotograph / orthoimage - It is an aerial photograph or image geometrically corrected ("orthorectified") such that the scale is uniform: the photo has the same lack of distortion as a map.
* point-cloud data
* stereo pairs
* LAS - LASer File Format
* 3D Reconstruction
* Stereo matching
* 3D Reprojection
* Odometry - It is the use of data from motion sensors to estimate change in position over time. It is used by some legged or wheeled robots to estimate their position relative to a starting location.
* Visual odometry - It is the process of determining equivalent odometry information using sequential camera images to estimate the distance traveled. Visual odometry allows for enhanced navigational accuracy in robots or vehicles using any type of locomotion on any surface.
* Sparse Visual Odometery
* Monocular or stereo visual odometry
* Laser-based SLAM
* combine visual and LIDAR information
* optical flow
* 3D object detection
* 3D object annotations
* localization system - The system which provides the position information to the nodes is called localization system.
* calibration and synchronization
* benchmarking
* egomotion - Egomotion is defined as the 3D motion of a camera within an environment. In the field of computer vision, egomotion refers to estimating a camera's motion relative to a rigid scene. An example of egomotion estimation would be estimating a car's moving position relative to lines on the road or street signs being observed from the car itself. The estimation of egomotion is important in autonomous robot navigation applications.
* occlusion/occluded
* entropy
* Training set and Test set
* True positive
* Scaffolding
* Telementry
* SIFT descriptor - Scale Invariant Feature Transform descriptor
* SAR - Synthetic Aperture Radar
* CCD - coherent change Detection
* TIN - Triangular Irregular Network
* Stereophotogrammetry - is the technique of using two or more cameras to reconstruct the 3D coordinates of an object. It is a non-intrusive mapping technique, independent of scale. Those new algorithms, gathered under the name 'Structure from Motion' are able to extract 3D points from a sequence of 2D images
* Terrestrial Stereophotogrammetry
* Inverse Distance Weighting (IDW)
* calculated the errors (standard error, standard deviation, root mean square error (RMSEZ))
* The root-mean-square deviation (RMSD) or root-mean-square error (RMSE) is a frequently used measure of the differences between values (sample and population values) predicted by a model or an estimator and the values actually observed. The RMSD represents the sample standard deviation of the differences between predicted values and observed values.
* Curbs - represents the edge of the road and are detected using the Haar wavelet
* GPU programming (CUDA, OpenCL-Open Computing Language)
* CUDA® is a parallel computing platform and programming model invented by NVIDIA. It enables dramatic increases in computing performance by harnessing the power of the graphics processing unit (GPU).
* OpenCL™ (Open Computing Language) is the open, royalty-free standard for cross-platform, parallel programming of diverse processors found in personal computers, servers, mobile devices and embedded platforms. OpenCL greatly improves the speed and responsiveness of a wide spectrum of applications in numerous market categories from gaming and entertainment to scientific and medical software.
* PCL - The Point Cloud Library (or PCL) is a large scale, open project [1] for 2D/3D image and point cloud processing.
* Decimation
* UGVs - Unmanned Ground Vehicles
* UAVs - Unmanned Aerial Vehicles
* SUA - Small Unmanned Aircraft
* SIFT - Scale Invariant Feature Transform
* VRML - Virtual Reality Modeling Language
* Deep Zoom Image or Deep Zoom Collection
* Telementry - the process of recording and transmitting the readings of an instrument
* GNSS - Global Navigation Satellite Systems
* TST - Total Station Theodolite
* GSD - Ground Sample Distance - the distance on the ground between pixel centres in the image
* SfM - Structure from Motion
* MVS - Multi-View Stereo
* TIN - Triangulated Irregular Network or mesh
* NDVI - normalized difference vegetation index
* HDR - High Dynamic Range imaging

## File Formats

### .TIFF
- Tagged Image File Format

### .pts
A pts file extension is mainly related to a special text based format that contains 3D data in so-called PointCloud. PointCloud is basically a 3D coordinate system, in which points are usually defined by X, Y, and Z coordinates. Used to describe external surface of an object.
* https://www.file-extensions.org/pts-file-extension

https://www.ptgrey.com/KB/10193
