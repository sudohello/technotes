/*
Title: Maths
Decription: Maths
Author: Bhaskar Mangal
Date: 
Updated: 16th May 2018
Tags: Maths
*/

## Mathematics

### Singular-Value Decomposition (SVD)
- https://blog.statsbot.co/singular-value-decomposition-tutorial-52c695315254
- examples and applications
	* Useful in machine learning and in both descriptive and predictive statistics
	* psychology and sociology, climate and atmospheric science, and astronomy
- Other terms include:
	* factor analysis
	* principal component (PC) decomposition
	* empirical orthogonal function (EOF)

**Technical introduction**
- Singular value decomposition is a method of decomposing a matrix into three other matrices

### Matrix Algebra
- orthogonal matrix
- diagonal matrix
- square matrix
- transpose
- Identity matrix
- eigenvalues
- determinant of a square matrix
- inverse of a square matrix
- sigular matrix: A square matrix that does not have a matrix inverse. A matrix is singular if its determinant is 0.
	- mathworld.wolfram.com/SingularMatrix.html


### Vector Algebra and Vector Calculus
http://farside.ph.utexas.edu/teaching/336k/Newtonhtml/node148.html

## Misc
enhancing the Euclidean plane by the addition of these points at infinity where parallel lines meet, and resolving the difficulty with infinity by calling them “ideal points.” By adding these points at infinity, the familiar Euclidean space is transformed into a new type of geometric object, projective space.

projective space – it is just an extension of Euclidean space in which two lines always meet in a point, though sometimes at mysterious points at infinity.

points at infinity- They are the points represented by homogeneous coordinates in which the last coordinate is zero.

The Euclidean space IR n can be extended to a projective space IP n by representing points as homogeneous vectors. It turns out that the points at infinity in the two-dimensional projective space form a line, usually called the line at infinity. In three-dimensions they form the plane at infinity.

A more general type of transformation is that of applying a linear transformation to IR n , followed by a Euclidean transformation moving the origin of the space. We may think of this as the space moving, rotating and finally stretching linearly possibly by different ratios in different directions. The resulting transformation is known as an affine transformation.

Euclidean space is uniform, so is projective space

We have seen that projective space can be obtained from Euclidean space by adding a line (or plane) at infinity. We now consider the reverse process of going backwards. This discussion is mainly concerned with two and three-dimensional projective space.

However, in projective space, there is no concept of which points are at infinity – all points are created equal.

The geometry of the projective plane and a distinguished line is known as affine geometry and any projective transformation that maps the distinguished line in one space to the distinguished line of the other space is known as an affine transformation. Affine geometry is seen as
specialization of projective geometry, in which we single out a particular line (or plane – according to the dimension) and call it the line at infinity.

Note that a circle is not a concept of affine geometry, since arbitrary stretching of the plane, which preserves the line at infinity, turns the circle into an ellipse. Thus, affine geometry does not distinguish between circles and ellipses.

show that by singling out some special feature of the line or plane at infinity affine geometry becomes Euclidean geometry

 
The equation for a circle in homogeneous coordinates (x, y, w) is of the form
$(x − aw)^2 + (y − bw)^2 = r^2w^2$

absolute conic and is one of the key geometric entities

we may consider 3D Euclidean space to be derived from projective space by singling out a particular plane as the plane at infinity and specifying a particular conic lying in this plane to be the absolute conic.

Perpendicularity of lines in space is not a valid concept in affine geometry, but belongs to Euclidean geometry. The perpendicularity of lines may be defined in terms of the absolute conic.

In applying projective geometry to the imaging process, it is customary to model the world as a 3D projective space.

Different camera matrices representing the image formation from the same centre of projection reflect only different coordinate frames for the set of rays forming the image. Thus two images taken from the same point in space are projectively equivalent. It is only when we start to measure points in an image, that a particular coordinate frame for the image needs to be specified. Only then does it
become necessary to specify a particular camera matrix.

all images acquired with the same camera centre are equivalent – they can be mapped onto each other by a projective transformation without any information about the 3D points or position of the camera centre.

**Calibrated cameras**
For a camera not located on the plane at infinity, the plane at infinity in the world maps one-to-one onto the image plane. This is because any point in the image defines a ray in space that meets the plane at infinity in a single point. Thus, the plane at infinity in the world does not tell us anything new about the image. The absolute conic, however being a conic in the plane at infinity must project to a conic in the image. The resulting image curve is called the Image of the Absolute Conic, or IAC. If the location of the IAC is known in an image, then we say that the camera is calibrated.

unless something is known about the calibration of the two cameras, the ambiguity in the reconstruction is expressed by a more general class of transformations – projective transformations.

The basic tool in the reconstruction of point sets from two views is the fundamental matrix, which represents the constraint obeyed by image points x and x  if they are to be images of the same 3D point. This constraint arises from the coplanarity of the camera centres of the two views, the images points and the space point.

A pair of camera matrices P and P  uniquely determine a fundamental matrix F, and conversely, the fundamental matrix determines the pair of camera matrices, up to a 3D projective ambiguity. Thus, the fundamental matrix encapsulates the complete projective geometry of the pair of cameras, and is unchanged by projective transformation of 3D.

for two views, the basic algebraic entity is the fundamental matrix, for three views this role is played by the trifocal tensor. The trifocal tensor is a 3 × 3 × 3 array of numbers that relate the coordinates of corresponding points or lines in three views. Just as the fundamental matrix is determined by the two camera matrices, and determines them up to projective transformation, so in three views, the trifocal tensor is determined by the three camera matrices, and in turn determines them, again up to projective transformation. Thus, the trifocal tensor encapsulates the relative projective geometry of the three cameras.

The most basic relationship between image entities in three views concerns a correspondence between two lines and a point. We consider a correspondence $x↔l^{'}↔l{''}$ between a point x in one image and two lines $l{'}$ and $l{''}$ in the other two images. This relationship means that there is a point X in space that maps to x in the first image, and to points $x{'}$ and $x{''}$ lying on the lines $l{'}$ and $l{''}$ in the other two images. The coordinates of these three images are then related via the trifocal tensor relationship:
$$\sum_{ijk} x^i l^{'}_jl^{''}_kT_i^{jk} = 0$$

The 27 elements of the tensor are not independent, however, but are related by a set of so called *internal constraints*.

**n-view reconstruction**
The tensor method does not extend to more than four views, however, and so reconstruction from more than four views becomes more difficult.
* One way to proceed is to reconstruct the scene bit by bit, using three-view or two-view techniques. Such a method may be applied to any image sequence, and with care in selecting the right triples to use, it will generally succeed.
* There are methods that can be used in specific circumstances. The task of reconstruction becomes easier if we are able to apply a simpler camera model, known as the affine camera. This camera model is a fair approximation to perspective projection whenever the distance to the scene is large compared with the difference in depth between the back and front of the scene. If a set of points are visible in all of a set of n views involving an **affine camera**, then a well-known algorithm, the **factorization algorithm**, can be used to compute both the structure of the scene, and the specific camera models in one step using the **Singular Value Decomposition**. Its main difficulties are the use of the affine camera model, rather than a full projective model, and the requirement that all the points be visible in all views.
* This method has been extended to **projective cameras** in a method known as **projective factorization**. Although this method is generally satisfactory, it can not be proven to converge to the correct solution in all cases. Besides, it also requires all points to be visible in all images.
* Other methods for n-view reconstruction involve various assumptions, such as
knowledge of four coplanar points in the world visible in all views, or six or seven points that are visible in all images in the sequence. Methods that apply to specific motion sequences, such as linear motion, planar motion or single axis (turntable) motion have also been developed.
* The dominant methodology for the general reconstruction problem is **bundle adjustment**. This is an iterative method, in which one attempts to fit a non-linear model to the measured data (the point correspondences). The advantage of bundle-adjustment is that it is a very general method that may be applied to a wide range of reconstruction and optimization problems. It may be implemented in such a way that the discovered solution is the Maximum Likelihood solution to the problem, that is a solution that is in some sense optimal in terms of a model for the inaccuracies of image measurements. Unfortunately, bundle adjustment is an iterative process, which can not be guaranteed to converge to the optimal solution from an arbitrary starting point. Much research in reconstruction methods seeks easily computable non-optimal solutions that can be used as a starting point for bundle adjustment. An initialization step followed by bundle adjustment is the generally preferred technique for reconstruction.

**Transfer**
Another useful application of projective geometry is that of transfer. given the position of a point in one (or more) image(s), determine where it will appear in all other images of the set.

**Euclidean reconstruction**
In uncalibrated cameras important parameters such as the focal length, the geometric centre of the image (the principal point) and possibly the aspect ratio of the pixels in the image are unknown. If a complete calibration of each of the cameras is known then it is possible to remove some of the ambiguity of the reconstructed scene.
* Projective reconstruction is insufficient for many purposes, such as application to computer graphics, since it involves distortions of the model that appear strange to a human used to viewing a Euclidean world.
* In projective reconstruction, which is all that is possible without knowing something about the calibration of the cameras or the scene.
* In order to obtain a reconstruction of the model in which objects have their correct (Euclidean) shape, it is necessary to determine the calibration of the cameras.
* determining the Euclidean structure of the world is equivalent to specifying the plane at infinity and the absolute conic. In fact, since the absolute conic lies in a plane, the plane at infinity, it is enough to find the absolute conic in space.
* knowledge of the camera calibration is equivalent to being able to determine the Euclidean structure of the scene.

**Auto-calibration**
* Generally given three cameras known to have the same calibration, it is possible to determine the absolute conic, and hence the calibration of the cameras.
	* Knowing the plane at infinity
	* Auto-calibration given square pixels in the image

From point matches between images, it is possible to carry out first a projective reconstruction of the point set, and determine the motion of the camera in the chosen projective coordinate frame. Using auto-calibration techniques, assuming some restrictions on the calibration of the camera that captured the image sequence, the camera may be calibrated, and the scene subsequently transformed to its true Euclidean structure.

**3D graphical models**
Knowing the projective structure of the scene, it is possible to find the epipolar geometry relating pairs of images and this restricts the correspondence search for further matches to a line – a point in one image defines a line in the other image on which the (as yet unknown) corresponding point must lie. In fact for suitable scenes, it is possible to carry out a dense point match between images and create a dense 3D model of the imaged scene. This takes the form of a triangulated shape model that is subsequently shaded or texture-mapped from the supplied images and used to generate novel views.

**video augmentation**
Automatic reconstruction techniques have recently become widely used in the film industry as a means for adding artificial graphics objects in real video sequences.

* The most important requirement for realistic insertion of an artificial object in a video sequence is to compute the correct motion of the camera. Unless the camera motion is correctly determined, it is impossible to generate the correct sequences of views of the graphics model in a way that will appear consistent with the background video. Generally, it is only the motion of the camera that is important here; we do not need to reconstruct the scene, since it is already present in the existing video, and novel views of the scene visible in the video are not required. The only requirement is to be able to generate correct perspective views of the graphics model.
* It is essential to compute the motion of the camera in a Euclidean frame. It is not enough merely to know the projective motion of the camera. This is because a Euclidean object is to be placed in the scene. Unless this graphics object and the cameras are known in the same coordinate frame, then generated views of the inserted object will be seen to distort with respect to the perceived structure of the scene seen in the existing video.
* Once the correct motion of the camera, and its calibration are known the inserted object may be rendered into the scene in a realistic manner. If the change of the camera calibration from frame to frame is correctly determined, then the camera may change focal length (zoom) during the sequence. It is even possible for the principal point to vary during the sequence through cropping.

Under perspective imaging certain geometric properties are preserved, such as collinearity (a straight line is imaged as a straight line), whilst others are not, for example parallel lines are not imaged as parallel lines in general. Projective geometry models this imaging and also provides a mathematical representation appropriate for computations.

The important issue of what should be minimized in a cost function, e.g. algebraic or geometric or statistical measures, is described at length.

The rank of a matrix is the maximum number of independent rows (or, the maximum number of independent columns).


http://vision.in.tum.de/research/vslam/lsdslam

Assembling a mobile mapping and navigation system involves three main aspects: System Design, Choice of Sensors, and Methods for Localization and Mapping.

Iterative Extended Kalman Filter (IEKF)
point-to-plane iterative closest point (ICP)

efficient perception and pose estimation are critical

 because of imperfections in synchronization, pose estimation, control, and other sources, the resulting map accuracy and resolution can be rather poor.

To quantify the mapping errors, a reference map is often captured in stop-and-go mode where the imaging sensor is only activated when the platform has halted its movements. It is agreed for terrestrial applications that perception data captured while the platform is stationary can yield higher quality data because motion blur and any other robot motion induced errors are avoided

existing mobile mapping systems either solely operates in stop-and-go or in full-kinematic mode. The former approach is hindered by the slow data acquisition and the latter may lack accuracy.

system that can operate in both modes has not yet been developed; specifically one that can capture higher density, stability and accuracy data when it is parked and lower quality but continuous data while it is moving.

Monocular cameras are passive sensors that can capture a 2D array of light intensity information instantaneously. Although they are sensitive to the ambient illumination and the information they encapsulate for SLAM is dependent on the scene’s texture, being a bearing-only sensor [19] it is largely independent of the object’s reflectance properties and can observe details as far as their pixel resolution allows. Stereo cameras can further perceive depth from a single exposure station based on triangulation, a process similar to how human vision operates [20]. LiDAR systems on the other hand are active sensors that acquire 2D scan lines by measuring distance (based on the time-of-flight principle) and bearing information point-by-point at high speed. The third dimension is obtained either by the platform’s trajectory (for 2D scanners) or by a rotating head/mirror (for 3D scanners). They can observe dense geometric information over homogeneous surfaces under any illumination conditions.
