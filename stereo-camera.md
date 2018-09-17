---
Title: Stereo Camera
Decription: Basics of Stereo Photogrammetry
Author: Bhaskar Mangal
Date: 18 Dec 2016
Placing: 1
Tags: Stereo Camera, Photogrammetry, Concept
---

**Table of Contents**
* TOC
{:toc}


## Stereo Camera

A **stereo camera** is a type of **camera** with two or more lenses with a separate image sensor or film frame for each lens. This allows the **camera** to simulate human binocular vision, and therefore gives it the ability to capture three-dimensional images, a process known as **stereo** photography. Not all two-lens cameras are used for taking stereoscopic photos

* Stereo bases/Baseline - Distances between the two camera lenses
* The distance between the lenses in a typical stereo camera (the intra-axial distance) is about the distance between one's eyes (known as the intra-ocular distance) and is about 6.35 cm.
* Depth plays an important role in determining an environment around a system, as it can provide distances from the system to objects within the surroundings. Therefore, it is important to have a means to obtain this data without knowing it a priori, and one such way to calculate distance automatically is with a stereo vision system. 3-D un-gridded surface points, known as point clouds, were generated from a stereo vision system.
* The key to stereo vision processing is that the relation of the left camera with respect to the right camera is known. This knowledge of positioning and characterization of a stereo system is known as a calibrated stereo system. Any deviation from the calibration state will introduce errors that will corrupt the data obtained from stereo processing.
* Calibration - In order to apply stereo ranging techniques with a reasonable level of accuracy, it is important to calibrate the camera system. The calibration process provides numerical values for intrinsic camera parameters such as focal length, and extrinsic parameters such as relative orientation angles between the two cameras.
* Rectification of a stereo image pair is the process of transforming (“warping”) the two images so that corresponding points lie on the same image rows. Rectification is commonly performed to improve the speed of the search for stereo correspondences.
* During correlation, un-distorted and rectified images from the left and right camera are used to match points from one image to the other. In order to determine the distance from the camera, the disparity needs to be found, change in location of points in the left image to the right. It follows that there must be an overlap in the two images so that a point in the left image also exists in the right image and a correspondence can be found.
* 3-D Re-projection - Re-projecting 2-D points from a set of images to 3-D points is accomplished using the disparity values for each pixel.
* Resolution of the cameras plays an important role in the overall accuracy of the stereo system. Resolution often refers to the number of pixels in the sensor array of the camera, which is typically a CCD (charge-coupled device) containing a rectangular array of light-sensitive elements. For many applications the effective resolution is of interest, and this term refers to the area within the 3-D scene which projects onto a single pixel of the sensor array. Effective resolution therefore depends on the focal length of the lens and on the distance of the camera from the imaged surface in the scene. It is common to refer to the effective resolution using units of pixels per inch (PPI), and for convenience this may be considered in one dimension only. Figure 15 contains plots of effective resolution for several sensor array sizes and at several depths.
* The field of view and focal length of the lens are inversely related. By increasing the focal length, the field of view can be reduced and simultaneously increase the effective resolution.
* When considering a stereo vision system, the field of view is important as there needs to be a significant amount of overlap in the images from the two cameras. Naturally, stereo ranging is possible only for 3-D scene points that appear in the images of both cameras.


#### Applications of Stereo Camera

* These can be used to calculate a [depth map](https://en.wikipedia.org/wiki/Depth_map) through advanced [image processing](https://en.wikipedia.org/wiki/Image_processing) techniques

* Stereo cameras are sometimes mounted in cars to detect the lane's width and the proximity of an object on the road

* In April 2015, Intel has revealed a camera that can fit in a smartphone to serve various depth sensing applications such as changing the focus of a photo after it has been taken, 3D scanning and gesture control.

#### Stereo Images

> **How do we get 3D from Stereo Images?**
> ![Alt Test](disparity.png "Disparity")

> **How do we get 3D from Stereo Images?**
> ![Alt Test](projection-of-stereo-images.png "Projection")
The method of detemining depth from disparity (d) is called triangulation. Note that the depth is inversly proportional to disparity.

Notes:
* An anaglyph is a superposition of a left-eye and right-eye image, using different colours for each. (Red-Cyan Composite Anaglyphs)
* Photogrammetry is the science of making measurements from photographs, especially for recovering the exact positions of surface points.
* Accuracy/Error estimation:
	I suggest you verify the depth measured in your images by measuring it in the real world. If there was a way to verify the measurement you did in the images .. in the images then you probably would have used that way to measure depth in the first place. Measure the distance from your camera to some object in the real world, and measure the size of the object perpendicular to the axis of one of the camera's. Then also measure the distance and size in your images. You use the size measure in the real world combined with the size of the object in pixels in the image to scale the distance you calculate. The result should match the distance you mesaured.

#### Data Samples
* http://cms.mapmart.com/samples.aspx

#### References
* https://people.duke.edu/~ng46/topics/stereo.htm
* http://www.3djournal.com/001/gallery.php
* https://en.wikipedia.org/wiki/Photogrammetry#Stereophotogrammetry
* http://www.photomodeler.com/downloads/10_Photogrammetry_Common_Questions.pdf
* http://www.photomodeler.com/downloads/ScanningWhitePaper.pdf
* https://www.harrisgeospatial.com/docs/generatingepipolarimages.html
* http://docs.opencv.org/3.1.0/dd/d53/tutorial_py_depthmap.html
* http://paulbourke.net/stereographics/stereophoto/
* http://www.zjucvg.net/index.html
* https://github.com/anshulpaigwar/ROS-queries-and-solutions/wiki/PointClouds-using-Flycapture-and-Triclops-SDK-and-Integration-with-ros:
* http://proceedings.spiedigitallibrary.org/proceeding.aspx?articleid=730582
* http://paulbourke.net/stereographics/
* http://stereo.jpn.org/eng/stphmkr/
* https://www.researchgate.net/post/Can_anyone_share_sample_program_for_stereo_images
* http://stackoverflow.com/questions/21775081/how-to-create-a-depth-map-from-pointgrey-bumblebee2-stereo-camera-using-triclops
* http://stackoverflow.com/questions/1407902/libraries-to-get-depth-map-from-stereo-images?rq=1
* https://sourceforge.net/projects/estereo/files/EStereo/

##### Videos
* [Stereo Vision Overview](https://www.youtube.com/watch?v=Ckd1KJZreVE)
##### Tools
* [Paraview](http://www.paraview.org/)
* [Veloview](https://github.com/Kitware/VeloView)
* [Point Cloud Library (PCL)](http://www.pointclouds.org/downloads/)
* [Robot Operating System-ROS: rviz](http://wiki.ros.org/rviz)
  * http://wiki.ros.org/but_calibration_camera_velodyne
  * http://pcl.ros.org
* http://homepages.inf.ed.ac.uk/rbf/CVonline/SWEnvironments.htm

##### Other References
* [Stereo Camera](https://en.wikipedia.org/wiki/Stereo_camera)
* [Stereo-mapping](https://github.com/introlab/rtabmap/wiki/Stereo-mapping)
* http://vision.psych.umn.edu/users/kersten/kersten-lab/shadows.html
* http://www.science.gov/topicpages/0-9/3d+stereo+visualization.html
* http://vibotudg.weebly.com/uploads/2/6/7/2/26729959/mscv_ddg_lq.pdf
* http://velodynelidar.com/
* http://www.mrpt.org/MalagaUrbanDataset
* http://83.212.134.96/robotics/wp-content/uploads/2011/12/review-of-stereo-matching-algorithms-for-3d-vision.pdf
* [Computer Vision Applications and Algorithms](http://soe.rutgers.edu/~meer/TEACHTOO/PAPERS/Szeliskistereodraft.pdf)
* SLAM
	* https://openslam.org/
	* https://en.wikipedia.org/wiki/Simultaneous_localization_and_mapping
* [opencl](https://www.khronos.org/opencl/)
* [CUDA](http://www.nvidia.com/object/cuda_home_new.html)
* http://www.mobileye.com/
* http://aecmag.com/comment-mainmenu-36/1038-laser-scanning-vs-image-based-modelling
* http://leica-geosystems.com/products/laser-scanners/software/leica-cyclone/leica-cyclone-publisher-and-truview
* http://instaar.colorado.edu/tpb/syllabus.html
* http://www.cs.ubc.ca/~lowe/vision.html

* Image processing
* [Python](https://docs.python.org/3/tutorial/controlflow.html)
  * [openCV](http://docs.opencv.org/3.1.0/index.html)
  * [openCV with QT](https://wiki.qt.io/OpenCV_with_Qt)
	* [Octave alternative to matlab; with image processing toolbox](http://wiki.octave.org/Octave_for_Debian_systems)

### Camera calibration

#### Why?
Camera calibration is necessary to obtain a geometric relationship between the real world and the camera plane. This is important in as we require a scene to be measured, build 3D model, project back on the real world.

#### Definitions

1. Camera calibration can be defined as finding the camera parameters that affect the imaging process and that allow one to obtain relationships between the image plane and the three dimensional world.

2. Camera Calibration is the estimation of extrinsic and intrinsic parameters is called camera calibration. 
  - Typically uses a 3D object of known geometry with image featuresthat can be located accurately
* Intrinsic camera parameters:
  - Perspective projection parameter: focal length
  - Distortion due to optics: radial distortion parameters k1, k2
  - Transformation from camera frame to pixel coordinates



**++Intrinsic calibration++**
It involves computing the internal parameters of the camera which are normally:-

* Image centre or principal point p = (px; py)
  - Typically this point is not at the centre (width/2, height/2) of the image
* Focal length (f)
  - This is the distance from the centre of the lens to the principal point.
* Aspect ratio (r)
  - Refers to the relative vertical and horizontal scaling of the image
* Skew (k)
  - Is a factor that depends on the angle between the vertical and horizontal axis
* Lens distortion
  - This is usually modelled by radial distortion (which is due to the spherical shape of the lens) and sometimes an additional tangential distortion component (normally due to bad positioning of the lens)

* ++Intrinsic calibration++ of a single camera is the task of estimating the internal parameters specifying its operation, normally consisting of focal length, aspect ratio, principal point and radial distortion coefficients.
  
**Extrinsic calibration**
It involves the computation of a rotation matrix R and a translation vector t that relates the camera frame with the world coordinate frame.
- It consist of a six degree of freedom transformation: three for rotation and three for translation

* ++Extrinsic calibration++ means determining the relative poses (3D translation and rotation) of a set of ++rigidly connected cameras++
  
**Keyterms and keyphrases**
- Projection matrix P
- Internal camera parameters K
- Position of the camera relative to the world described by a Rotation matrix R and a Translation vector t
- Epipole
- Epipolar Plane
- Epipolar line
- Epipolar Geometry
- Baseline
- Image Plane
- auto-calibration of stereo rigs
- multi-camera rig calibration
- recover the configuration of a camera rig with two and four cameras in a variety of configurations
- sequential auto-calibration of a single camera

#### Classical & Auto-calibration Methods

* Classical/Standard Approach
  - Calibration is done by traditional approaches were a chessboard pattern is presented to the cameras and the extrinsics are recovered with OpenCV or Matlab calibration libraries.
  - Another approach is to manually create a very distinguished feature that is detected by all cameras in a number of frames during a video sequence, a bright spot is created by a laser pointer which is waved on a working volume and detected by all cameras.

#### METHODOLOGY

##### A. Plane Based Claibration (For Internal parameters)
- Use Camera Calibration Toolbox for Matlab
- This calibration technique makes use of a regularly gridded checkered pattern where the metric size of the rectangulars is known.  
- This grid is flat, and therefore multiple images of the calibration grid are acquired at different distances and orientations.
- The images are then automatically corrected for the radial distortion by the toolbox
- These corrected images are used to do a stereo calibration between the left and the right camera using the toolbox
- In the stereo calibration, all intrinsic and extrinsic parameters are recomputed together with all the uncertainties so as to minimize the  reprojection errors on both cameras for all calibration grid locations.

**The purpose of the standard calibration is two-fold:-**
* Firstly, it allows to determine the intrinsic calibration for the two cameras. We assume that these parameters are not changing over time.
* Secondly, one of the objectives of this work is to avoid having to do the extrinsic calibration in the field each time that the stereo system geometry is changed. However, the standard stereo calibration is performed for comparison purposes.

##### B. Synchronization With a Flashing Light
* When recording the same scene by two unsynchronized cameras, there will be a slight time inconsistency between them. This is because their recording start times are not exactly the same. To synchronize the cameras, the frame difference of the resulting video sequences must be determined.
* One of the simplest ways to do this is to capture a simultaneous event that can easily be recognized in both video sequences, such as a flashing light. When the frame of the flashing light event is found in both images sets, the time lag or frame difference between the left and right camera is then known.

##### C. Synchronization From Motion Consistency
* The reasoning behind this approach is that sudden movements of the stereo camera create distinctive patterns of image motion that are easy to correlate and therefore help determine the time lag.

##### D. Estimation of rotation velocities
* From the acquired video, the extracted image sequences are corrected for the radial distortion.

##### E. Determining the frame shift
* Since the left and right cameras are not started at the same time, there will be a time difference for the rotation events. Although the rotation angle transformation between the two cameras is similar, there are still slight differences, because they are placed at opposite ends of the bar.

#### Exercises

* Analyse and understand the advantages and disadvantages of using calibrated or uncalibrated cameras
* To recover the extrinsic parameters of a multi-camera system
 
#### References

* http://www.cambridgeincolour.com/tutorials/camera-lenses.htm
* [Fundamental of Camera Calibration](https://www.youtube.com/watch?v=4-thTdR7Blg)
* [Stereo Rig Calibration](https://www.youtube.com/watch?v=DDjfhYxqp3w)
* [Matlab Toolbox for Camera Calibration with a complete documentation](https://www.vision.caltech.edu/bouguetj/calib_doc/)
* [Octabe implementation of the Matlab Claibration Tutorial](http://www.sparetimelabs.com/cameracalib/cameracalib.php)
* https://www.vision.caltech.edu/bouguetj/calib_doc/htmls/example5.html
* [Lens Focal Length and Stereo Baseline Calculator](https://nerian.com/support/resources/calculator/)
* Computer Vision Video Courses
  * [Computer Vision for Visual Effects (ECSE-6969) Lectures Spring 2014](https://www.youtube.com/channel/UCaiJlKxXamoODQtlx486qJA)
