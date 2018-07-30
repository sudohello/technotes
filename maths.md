/*
Title: Maths
Decription: Maths
Author: Bhaskar Mangal
Date: 
Updated: 16th May 2018
Tags: Maths
*/

# Mathematics

## [Mathematical optimization: finding minima of functions](https://en.wikipedia.org/wiki/Mathematical_optimization)
- ScipyLectures-simple.pdf

Mathematical optimization deals with the problem of finding numerically minimums (or maximums or zeros)
of a function. In this context, the function is called **cost function**, or **objective function**, or **energy**.

- https://en.wikipedia.org/wiki/Convex_function

**Scalar Function, Vector Function, Scalr Field, Vector Field**
http://web.mit.edu/wwmath/vectorc/scalar/intro.html
- A scalar valued function is a function that takes one or more values but returns a single value.
- A n-variable scalar valued function acts as a map from the space Rn to the real number line. 
- http://www.solitaryroad.com/c251.html

### Gradient_descent
- http://en.wikipedia.org/wiki/Gradient_descent
- https://en.wikipedia.org/wiki/Preconditioner
- Gradient descent basically consists in taking small steps in the direction of the gradient, that is the direction of the steepest descent.
- We can see that very anisotropic (ill-conditioned) functions are harder to optimize.
- The more a function looks like a quadratic function (elliptic iso-curves), the easier it is to optimize.
- one of the problems of the simple gradient descent algorithms, is that it tends to oscillate across a valley, each time following the direction of the gradient, that makes it cross the valley

### Conjugate gradient descent
The conjugate gradient solves this problem by adding a friction term: each step depends on the two last values of the gradient and sharp turns are reduced.

### Newton and quasi-newton methods
- https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization
- https://en.wikipedia.org/wiki/Hessian_matrix

## Linear Programming
https://en.wikipedia.org/wiki/Linear_programming

Linear programming (LP, also called linear optimization) is a method to achieve the best outcome (such as maximum profit or lowest cost) in a mathematical model whose requirements are represented by linear relationships. Linear programming is a special case of mathematical programming (mathematical optimization).

More formally, linear programming is a technique for the optimization of a linear objective function, subject to linear equality and linear inequality constraints.

## Singular-Value Decomposition (SVD)
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

## Matrix Algebra
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


## Vector Algebra and Vector Calculus
http://farside.ph.utexas.edu/teaching/336k/Newtonhtml/node148.html

## Vector Calculus
http://web.mit.edu/wwmath/vectorc/index.html


## Concepts crucial for Image Processing

Different types of transformations:

**Affine Transformation**
- https://en.wikipedia.org/wiki/Affine_transformation
- Examples of affine transformations include translation, scaling, homothety, similarity transformation, reflection, rotation, shear mapping, and compositions of them in any combination and sequence.
- Projective Transformation
- Geometric Transformation

- [Real Coordinate Space]
	- https://en.wikipedia.org/wiki/Real_coordinate_space#Matrix_notation
	- With component-wise addition and scalar multiplication, it is the prototypical real vector space and is a frequently used representation of Euclidean n-space
	- any n-dimensional real vector space is isomorphic to the vector space Rn.
	- **Matrix Notation**
		- In standard matrix notation, each element of Rn is typically written as a column vector or row vector
		- The coordinate space Rn may then be interpreted as the space of all n × 1 column vectors, or all 1 × n row vectors with the ordinary matrix operations of addition and scalar multiplication
		- Linear transformations from Rn to Rm may then be written as m × n matrices which act on the elements of Rn via left multiplication (when the elements of Rn are column vectors) and on elements of Rm via right multiplication when they are row vectors)
		- Any linear transformation is a continuous function
		- In mathematics, the **standard basis** (also called natural basis) for a Euclidean space is the set of unit vectors pointing in the direction of the axes of a Cartesian coordinate system.
- [vector space]
	- https://en.wikipedia.org/wiki/Vector_space
	- https://en.wikipedia.org/wiki/Euclidean_vector
	- https://en.wikipedia.org/wiki/Zero_element
	- Any vector space may be considered as an affine space
	- also called a **linear space**
	- It is a collection of objects called vectors, which may be added together and multiplied ("scaled") by numbers, called scalars
	- Scalars are often taken to be real numbers, but there are also vector spaces with scalar multiplication by complex numbers, rational numbers, or generally any field
	- Euclidean vectors are an example of a vector space
- [Affine Space]
	- https://en.wikipedia.org/wiki/Affine_space
	- In mathematics, an affine space is a geometric structure that generalizes the properties of Euclidean spaces in such a way that these are independent of the concepts of distance and measure of angles, keeping only the properties related to parallelism and ratio of lengths for parallel line segments.
	- **In an affine space, there is no distinguished point that serves as an origin. Hence, no vector has a fixed origin and no vector can be uniquely associated to a point.**
	- In an affine space, there are instead displacement vectors, also called translation vectors or simply translations, between two points of the space.[1] Thus it makes sense to subtract two points of the space, giving a translation vector, but it does not make sense to add two points of the space. Likewise, it makes sense to add a displacement vector to a point of an affine space, resulting in a new point translated from the starting point by that vector.
	- Adding a fixed vector to the elements of a linear subspace of a vector space produces an affine subspace. One commonly says that this affine subspace has been obtained by translating (away from the origin) the linear subspace by the translation vector.
	- ** In finite dimensions, such an affine subspace is the solution set of an inhomogeneous linear system.**
- [Euclidean Space]
	- https://en.wikipedia.org/wiki/Euclidean_space
	- points of the space are specified with collections of real numbers, and geometric shapes are defined as equations and inequalities
	- This approach brings the tools of algebra and calculus to bear on questions of geometry and has the advantage that it generalizes easily to Euclidean spaces of more than three dimensions
	- Euclidean spaces have finite dimension
	-  One of the basic tenets of Euclidean geometry is that two figures (usually considered as subsets) of the plane should be considered equivalent (congruent) if one can be transformed into the other by some sequence of translations, rotations and reflections
	- clearly define the notions of distance, angle, translation, and rotation for a mathematically described space
	- https://en.wikipedia.org/wiki/Frame_of_reference
	- https://en.wikipedia.org/wiki/Abstraction
	- Euclidean space is an abstraction detached from actual physical locations, specific reference frames, measurement instruments, and so on
	- A purely mathematical definition of Euclidean space also ignores questions of units of length and other physical dimensions
	- the distance in a "mathematical" space is a number, not something expressed in inches or metres
	- The reason for working with arbitrary vector spaces instead of Rn is that it is often preferable to work in a coordinate-free manner (that is, without choosing a preferred basis). For then:
		* the vectors in the vector space correspond to the points of the Euclidean plane
		* the addition operation in the vector space corresponds to translation, and
		* the inner product implies notions of angle and distance, which can be used to define rotation.
	- A Euclidean space is not technically a vector space but rather an affine space, on which a vector space acts by translations, or, conversely, a Euclidean vector is the difference (displacement) in an ordered pair of points, not a single point
	- standard inner product (also known as the dot product) on Rn
	- Usually, the angle is considered a dimensionless quantity, but there are different units of measurement, such as radian (preferred in pure mathematics and theoretical physics) and degree (°) (preferred in most applications)
- [Dimensions]
	- https://en.wikipedia.org/wiki/Dimension#High-dimensional_space
- [Quaternion]
	- https://en.wikipedia.org/wiki/Quaternion
	- Used in three-dimensional computer graphics, computer vision
	- In practical applications, they can be used alongside other methods, such as Euler angles and rotation matrices, or as an alternative to them, depending on the application
- [Geometry]
	- https://en.wikipedia.org/wiki/Geometry
- [System_of_linear_equations]
	- https://en.wikipedia.org/wiki/System_of_linear_equations
	- In mathematics, a system of linear equations (or linear system) is a collection of two or more linear equations involving the same set of variables
	- the theory of linear systems is the basis and a fundamental part of linear algebra
	- A system of linear equations is homogeneous if all of the constant terms are zero
	- where {\displaystyle x_{1},x_{2},\ldots ,x_{n}} x_{1},x_{2},\ldots ,x_{n} are the unknowns, {\displaystyle a_{11},a_{12},\ldots ,a_{mn}} a_{11},a_{12},\ldots ,a_{mn} are the coefficients of the system, and {\displaystyle b_{1},b_{2},\ldots ,b_{m}} b_{1},b_{2},\ldots ,b_{m} are the constant terms.
	- **Vector Equation**
		- One extremely helpful view is that each unknown is a weight for a column vector in a linear combination.
	- **Matrix Equation**
		- The vector equation is equivalent to a matrix equation of the form
- [Nonlinear_system]
	- https://en.wikipedia.org/wiki/Nonlinear_system
	- In mathematics and physical sciences, a nonlinear system is a system in which the change of the output is not proportional to the change of the input
	- most systems are inherently nonlinear in nature
	-  the behavior of a nonlinear system is described in mathematics by a nonlinear system of equations, which is a set of simultaneous equations in which the unknowns (or the unknown functions in the case of differential equations) appear as variables of a polynomial of degree higher than one or in the argument of a function which is not a polynomial of degree one
	-  in a nonlinear system of equations, the equation(s) to be solved cannot be written as a linear combination of the unknown variables or functions that appear in them
- [Linear Map]
	- https://en.wikipedia.org/wiki/Linear_map
	- Linear maps can often be represented as matrices, and simple examples include rotation and reflection linear transformations
	- **a linear map is a mapping V → W between two modules (including vector spaces) that preserves the operations of addition and scalar multiplication**

- **[Affine transformation]**
	- vector algebra uses matrix multiplication to represent linear maps
	- vector addition to represent translations
	- Using an augmented matrix and an augmented vector, it is possible to represent both the translation and the linear map using a single matrix multiplication.
	- **Ordinary matrix-vector multiplication always maps the origin to the origin, and could therefore never represent a translation, in which the origin must necessarily be mapped to some other point. By appending the additional coordinate "1" to every vector, one essentially considers the space to be mapped as a subset of a space with an additional dimension.**  In that space, the original space occupies the subset in which the additional coordinate is 1. Thus the origin of the original space can be found at {\displaystyle (0,0,\dotsc ,0,1)} {\displaystyle (0,0,\dotsc ,0,1)}
	- A translation within the original space by means of a linear transformation of the higher-dimensional space is then possible (specifically, a shear transformation). The coordinates in the higher-dimensional space are an example of homogeneous coordinates. If the original space is Euclidean, the higher dimensional space is a real projective space.
	- **The advantage of using homogeneous coordinates is that one can combine any number of affine transformations into one by multiplying the respective matrices. This property is used extensively in computer graphics, computer vision and robotics.**
	* Properties preserved - 	An affine transformation preserves:
	* collinearity between points: three or more points which lie on the same line (called collinear points)continue to be collinear after the transformation.
	* parallelism: two or more lines which are parallel, continue to be parallel after the transformation.
	* convexity of sets: a convex set continues to be convex after the transformation. Moreover, the extreme * points of the original set are mapped to the extreme points of the transformed set.[3]
	* ratios of lengths along a line: for distinct collinear points {\displaystyle p_{1}} p_{1}, {\displaystyle p_{2}} p_{2}, {\displaystyle p_{3}} p_{3}, the ratio of {\displaystyle {\overrightarrow {p_{1}p_{2}}}} {\overrightarrow {p_{1}p_{2}}} and {\displaystyle {\overrightarrow {p_{2}p_{3}}}} {\overrightarrow {p_{2}p_{3}}} is the same as that of {\displaystyle {\overrightarrow {f(p_{1})f(p_{2})}}} {\overrightarrow {f(p_{1})f(p_{2})}} and {\displaystyle {\overrightarrow {f(p_{2})f(p_{3})}}} {\overrightarrow {f(p_{2})f(p_{3})}}.
	* barycenters of weighted collections of points.
	- If there is a fixed point, we can take that as the origin, and the affine transformation reduces to a linear transformation. This may make it easier to classify and understand the transformation
	- describing a transformation as a rotation by a certain angle with respect to a certain axis may give a clearer idea of the overall behavior of the transformation than describing it as a combination of a translation and a rotation. However, this depends on application and context.
	- **Affine transformations scale, rotate, translate, mirror and sheer images**
	- The Affine transforms are applicable to the registration process where two or more images are aligned (registered), an example of image registration is the generation of panoramic images that are the product of multiple images stitched together.
	- **affine transformations do not facilitate projection onto a curved surface or radial distortions**

- **[Projective transformation]**
	- https://en.wikipedia.org/wiki/Projective_transformation

### Distortions
https://en.wikipedia.org/wiki/Distortion_(optics)
http://cctvcad.com/videocad_help/index.html?about_distortion.htm
http://www.cctvcad.com/cctv_design_software.html

### Mathematical Terms and Definitions
* **Isomorphism**
	- https://www.britannica.com/science/isomorphism-mathematics
	- https://en.wikipedia.org/wiki/Isomorphism
* **Axiom**
	- https://en.wikipedia.org/wiki/Axiom
	- An axiom or postulate is a statement that is taken to be true, to serve as a premise or starting point for further reasoning and arguments
* **Barycenter**
	- https://en.wikipedia.org/wiki/Barycenter
	- The barycenter (or barycentre; from the Ancient Greek βαρύς heavy + κέντρον centre[1]) is the center of mass of two or more bodies that are orbiting each other, which is the point around which they both orbit.
* **Augmented Matrix**
	- https://en.wikipedia.org/wiki/Augmented_matrix
	- an augmented matrix is a matrix obtained by appending the columns of two given matrices, usually for the purpose of performing the same elementary row operations on each of the given matrices.
* **basis**
	- https://en.wikipedia.org/wiki/Basis_(linear_algebra)
	- In mathematics, a set of elements (vectors) in a vector space V is called a basis, or a set of basis vectors, if the vectors are linearly independent and every vector in the vector space is a linear combination of this set
* **Linear_independence**
	- https://en.wikipedia.org/wiki/Linear_independence
	- In the theory of vector spaces, a set of vectors is said to be linearly dependent if one of the vectors in the set can be defined as a linear combination of the others; if no vector in the set can be written in this way, then the vectors are said to be linearly independent. These concepts are central to the definition of dimension.[
* **Linear Combination**
	- https://en.wikipedia.org/wiki/Linear_combination
	- In mathematics, a linear combination is an expression constructed from a set of terms by multiplying each term by a constant and adding the results (e.g. a linear combination of x and y would be any expression of the form ax + by, where a and b are constants).[1][2][3] The concept of linear combinations is central to linear algebra and related fields of mathematics


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


## Radians
* https://betterexplained.com/articles/intuitive-guide-to-angles-degrees-and-radians/
* https://en.wikipedia.org/wiki/Radian#Reasons_why_radians_are_preferred_in_mathematics

"Much of physics (and life!) involves leaving your reference frame and seeing things from another’s viewpoint."

Degrees measure angles by how far we tilted our heads. Radians measure angles by distance traveled.
Radians are the empathetic way to do math — a shift from away from head tilting and towards the mover’s perspective.
Radians are a count of distance in terms of “radius units”, and I think of “radian” as shorthand for that concept.
it helps to think of radians as “distance” traveled on a unit circle.

we encounter the concept of “mover’s distance” quite a bit
* We use “rotations per minute” not “degrees per second” when measuring certain rotational speeds.
* When a satellite orbits the Earth, we understand its speed in “miles per hour”, not “degrees per hour”. Now divide by the distance to the satellite and you get the orbital speed in radians per hour.

https://instacalc.com
https://www2.clarku.edu/~djoyce/trig/tangents.html


Degrees have their place: in our own lives, we’re the focal point and want to see how things affect us. How much do I tilt my telescope, spin my snowboard, or turn my steering wheel?

With natural laws, we’re an observer describing the motion of others. Radians are about them, not us.
Because radians are in terms of the mover, equations “click into place”. Converting rotational to linear speed is easy, and ideas like sin(x)/x make sense.

http://canvas.projekti.info/ebooks/Math%20-%20Better%20Explained.pdf

## Sensors - calculate things like orientation, position, and velocity.
* https://www.sparkfun.com/pages/accel_gyro_guide
* http://www.unmannedsystemstechnology.com/company/inertial-labs/

## Better Explained Math
Takeaway: What an Aha! moment feels like
If I did my job, one of the approaches above (line-up, making a square, taking the average) clicked. Aha! That's why the formula works!

The goal of learning is to experience the concept firsthand. Then, the formula becomes a shorthand description of what you know. It's like reading sheet music: it's a description of a song, but not the same as experiencing it yourself.

Our goal is to find analogies, diagrams, examples, and plain-English descriptions that help bring concepts to life.

Happy math,

-Kalid