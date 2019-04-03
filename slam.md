---
Title: SLAM
Decription: SLAM
Author: Bhaskar Mangal
Date: 
Tags: SLAM
---

**Table of Contents**
* TOC
{:toc}


## SLAM
SLAM consists of	multipleparts:
- data reading,	datamapping, robot state,	state	update and map update
- it is 2D or 3D

## References
* http://www.openslam.org/
* http://robots.stanford.edu/probabilistic-robotics/
* http://robots.stanford.edu/probabilistic-robotics/errata.html
* https://ocw.mit.edu/courses/aeronautics-and-astronautics/16-412j-cognitive-robotics-spring-2005/projects/1aslam_blas_repo.pdf
* http://home.wlu.edu/~levys/students/BreezySLAM_SurajBajracharya.pdf
* https://stackoverflow.com/questions/1080533/slam-algorithm
* https://github.com/randvoorhies/SimpleSLAM
* https://github.com/KarthickPN/Kalman-and-Bayesian-Filters-in-Python
* https://www.analyticsinsight.net/future-ar-slam-technology-slam/


Probabilistic	Robotics (Thrun	etal.2005)
  - it is a field of robotics that involves robots in environment subject to uncertainity

**Algorithims for Localization**

* Monte Carlo Localization (Doucet et al 2001)
  - it approximates the robot's position on a map using particles
  - each particle is a hypothesis of the position and bearing of robot

* Kalman Filter (Kalman 1960)
- uses measurements over time containing noises and inaccuracies and produces estimates of unknown variables that are more precise than when based on sigle measurements
- laser sensor and odometry (wheel-rotation sensors)
- 

https://blog.fortrabbit.com/file-based-cms-2016

## V-REP
* http://www.coppeliarobotics.com/
* https://github.com/simondlevy/vrep-ubuntu

SLAM algorithms	from OpenSLAM.org:
DP-­‐SLAM	  (Eliazar	  and	  Parr	  2003),	
 - It uses particle filter to maintain a joint probability distribution over maps and robot positions
TinySLAM	Bajracharya	16 (a.k.a. CoreSLAM) (Steux	and	Hamzaoui 2010)
  - using the most recent map and the new odometry, CoreSLAM guesses the best new position and updates the map accordingly

http://www.swig.org/

SWIG is a software development tool that connects programs written in C and C++ with a variety of high-level programming languages. SWIG is used with different types of target languages including common scripting languages such as Javascript, Perl, PHP, Python, Tcl and Ruby. The list of supported languages also includes non-scripting languages such as C#, Common Lisp (CLISP, Allegro CL, CFFI, UFFI), D, Go language, Java including Android, Lua, Modula-3, OCAML, Octave, Scilab and R. Also several interpreted and compiled Scheme implementations (Guile, MzScheme/Racket, Chicken) are supported. SWIG is most commonly used to create high-level interpreted or compiled programming environments, user interfaces, and as a tool for testing and prototyping C/C++ software.



## Ref
* http://grauonline.de/wordpress/?page_id=1282