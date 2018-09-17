---
Title: Nvidia Graphics cards/GPU
Decription: Nvidia Graphics cards/GPU
Author: Bhaskar Mangal
Date: May-2017
Last Updated: May-2017
Tags: Nvidia Graphics cards/GPU
---

**Table of Contents**
* TOC
{:toc}


## Nvidia Graphics cards/GPU
GPUs had evolved into highly parallel multi-core systems allowing very efficient manipulation of large blocks of data.
- processing large blocks of data is done in parallel
- Whether for the host computer or the GPU device, all CUDA source code is now processed according to C++ syntax rules.
- Interoperability with rendering languages such as OpenGL is one-way, with OpenGL having access to registered CUDA memory but CUDA not having access to OpenGL memory.

### Brand Name

#### Grpahics Cards Business
* GeForce, Quadro, NVS, Tesla

#### SoC Business
* Tegra
	- mobile ARM SoCs
	- for self driving cars, deep learning
	- Jetson, Parker, Erista, DRIVE ( CX, PX, PX2 ), Xavier
	- SoC or self-driving cars: DRIVE ( CX, PX, PX2 )
		- DRIVE PX 2 is the open AI car computing platform
		- AI Super computer for self-driving cars: Xavier

### Graphics Card Target Market based on Device

#### Desktop GPUs
* **GeForce** - GeForce is a brand of graphics processing units (GPUs) designed by Nvidia. It is intended for the high-margin PC gaming market, and later diversification of the product line covered all tiers of the PC graphics market, ranging from cost-sensitive. The GeForce architecture is moving toward general-purpose graphics processor unit (GPGPU).

#### Mobile GPUs

#### Workstation GPUs
* **Quadro** - Quadro is Nvidia's brand for graphics cards intended for use in workstations running professional computer-aided design (CAD), computer-generated imagery (CGI), digital content creation (DCC) applications.

#### Mobile Workstation GPUs
* **Quadro Go (GL) & Quadro FX Go series**

#### Grid GPUs

#### Console GPUs

### Target Market based on Industry

#### Entertainment
- **GeForce** for entertainment

#### Professional
- **Quadro** for professional visualization

#### HPC and Supercomputing applications
- **Tesla** for HPC and supercomputing applications
- Nvidia Tesla is Nvidia's brand name for their products targeting stream processing and/or general purpose GPU.
- For Pascal for AI Super computing

#### Business Graphics Solutions
- The Nvidia **Quadro NVS** graphics processing units (GPUs) provide business graphics solutions for manufacturers of small, medium, and enterprise-level business workstations. The Nvidia Quadro NVS desktop solutions enable multi-display graphics for businesses such as financial traders.

## How to select Graphics card for our requirement?
* Understand the SDK/framework being used requirement for CUDA, cuDNN
* CUDA compute capabilities required
* Based on type of system to be used for - Desktop, Workstation, Mobile Workstation
* Nvidia support for that generation of GPU based on GPU microarchitecture
* Driver availability, CUDA toolkit, cuDNN for the underline Operating system

### Check the CUDA compute capability for the selected model
As per [Wikipedia CUDA article](https://en.wikipedia.org/wiki/CUDA):-
* CUDA works with all Nvidia GPUs from the G8x series onwards, including GeForce, Quadro and the Tesla line.
* CUDA SDK 6.5: Last Version with support for Tesla with Compute Capability 1.x
* CUDA SDK 7.5 support for Compute Capability 2.0 – 5.x (Fermi, Kepler, Maxwell)
* CUDA SDK 8.0 support for Compute Capability 2.0 – 6.x (Fermi, Kepler, Maxwell, Pascal)
* Next CUDA SDK Version no support for Fermi (2.x)


### Graphics Card/GPU Microarchitecture
```
(prior microarchitectures) < Tesla < Fermi(2010) < Kepler(2012) < Maxwell(2014) < Pascal(2016-2017) < Volta( 2017-2018)
```

## CUDA
* CUDA provides both a low level API and a higher level API. The initial CUDA SDK was made public on 15 February 2007, for Microsoft Windows and Linux.
* CUDA is a parallel computing platform and application programming interface (API) model created by Nvidia.[1] It allows software developers and software engineers to use a CUDA-enabled graphics processing unit (GPU) for general purpose processing – an approach termed GPGPU (General-Purpose computing on Graphics Processing Units).
* CUDA (Compute Unified Device Architecture) platform is a software layer that gives direct access to the GPU's virtual instruction set and parallel computational elements, for the execution of compute kernels.[2]
	- a compute kernel is a routine compiled for high throughput accelerators (such as GPUs), DSPs or FPGAs, separate from (but used by) a main program
	- The CUDA platform is designed to work with programming languages such as C, C++, and Fortran.
	- This accessibility makes it easier for specialists in parallel programming to use GPU resources, in contrast to prior APIs like Direct3D and OpenGL, which required advanced skills in graphics programming.
	- Also, CUDA supports programming frameworks such as OpenACC and OpenCL.[2] 
		- OpenACC (for open accelerators) is a programming standard for parallel computing developed by Cray, CAPS, Nvidia and PGI.
		- Open Computing Language (OpenCL) is a framework for writing programs that execute across heterogeneous platforms consisting of central processing units (CPUs), graphics processing units (GPUs), digital signal processors (DSPs), field-programmable gate arrays (FPGAs) and other processors or hardware accelerators. 
* C/C++ programmers use 'CUDA C/C++', compiled with nvcc
* Fortran programmers can use 'CUDA Fortran'
* In addition to libraries, compiler directives, CUDA C/C++ and CUDA Fortran, the CUDA platform supports other computational interfaces,
	- Khronos Group's OpenCL
	- Microsoft's DirectCompute
	- OpenGL Compute Shaders
	- C++ AMP
	- Third party wrappers are also available for: Python, Perl, Fortran, Java, Ruby, Lua, Haskell, R, MATLAB, IDL, and native support in Mathematica.

## GPUs in Computer game Industry
* Here, GPUs are used for:
	- graphics rendering
	- for game physics calculations (physical effects such as debris, smoke, fire, fluids)
	- **PhysX** is a proprietary realtime physics engine middleware SDK. PhysX was authored at NovodeX, an ETH Zurich spin-off. In 2004, NovodeX was acquired by Ageia, and in February 2008, Ageia was acquired by Nvidia
	- **Bullet** is a physics engine which simulates collision detection, soft and rigid body dynamics. It has been used in video games as well as for visual effects in movies. Erwin Coumans, its main author, worked for Sony Computer Entertainment US R&D from 2003 until 2010, for AMD until 2014, and he now works for Google.
The Bullet physics library is free and open-source software subject to the terms of the zlib License. The source code is hosted on GitHub, before 2014 it was hosted on Google Code.

### Brand (Marketing name for graphics cards)
- Comparison tables: Desktop GPUs

```
GeForce 256 series - 1999-00
GeForce2 series - 2000-01
GeForce3 series - 2001
GeForce4 series - 2002-04
GeForce FX (5xxx) series - 2003-04
GeForce 6 (6xxx) series - 2004-06
GeForce 7 (7xxx) series - 2005-07 - Last series on AGP cards (pre-Tesla)
GeForce 8 (8xxx) series - 2006-08 - Tesla (microarchitecture)
- The third major GPU architecture developed by Nvidia, Tesla (microarchitecture) represents the company's first unified shader architecture

- CUDA Compute Capability 1.1, 1.2
GeForce 9 (9xxx) series - 2008-09 - Tesla (microarchitecture)

- Compute Capability: 1.1
GeForce 100 series - 2009 - Tesla (microarchitecture)
GeForce 200 series - 2008-09 - Tesla (microarchitecture)

- CUDA Compute Capability 1.1, 1.2, 1.3
GeForce 300 series - 2009-10 - Tesla (microarchitecture)
GeForce 400 series - 2010-11 - Fermi (microarchitecture)
GeForce 500 series - 2011 - Fermi (microarchitecture)
GeForce 600 series - 2012-13 - Kepler (microarchitecture)
GeForce 700 series - 2013-14 - Kepler (microarchitecture)
GeForce 900 series - 2014-16 - Maxwell (microarchitecture)
( This is like Krish and Krish 3 naming, 700 and 900 series has overlap in microacrhitecture )
GeForce 10 series - 2016-17 -  Pascal (microarchitecture)
```
## Nvidia SoC, AI Supercomputers for Self-driving Cars

### Tegra
- **Tegra** is a system on a chip (SoC) series developed by Nvidia for mobile devices such as smartphones, personal digital assistants, and mobile Internet devices.
- **SoC** : A system on a chip or system on chip (SoC or SOC) is an integrated circuit (also known as an "IC" or "chip") that integrates all components of a computer or other electronic systems.

```
Tegra2 < Tegra3 < Tegra4 < TegraK1 < TegraX1 < TegraP1(codenamed "Parker") < Xavier
```
### Drive CX, PX, PX2, Xavier
```
Drive CX < Drive PX < Drive PX 2(Autocruise) < Drive PX 2(Autochauffeur) < Xavier AI Car Supercomputer (2017)
```

* **Drive CX**
	- Single Tegra X1 SoC
* **Drive PX (2015)**
	- Two Tegra X1 SoCs
	- The Nvidia Drive PX is a series of computers aimed at providing autonomous car and driver assistance functionality powered by deep learning.

* **Drive PX2**
	- The Nvidia Drive PX 2 is based on one or two Tegra Parker SoCs
	- Two real world board configurations:
		- for Autocruise (point to point): 1x Tegra Parker
			- Connect data from 8 cameras,LIDAR,radar,ultrasonic sensors
		- for Autochauffeur(highway cruise capability): 2x Tegra Parker + 2 Pascal GPU's
			- full Autonomy (no driver)
* **Xavier**
	- AI supercomputer (single chip)
	-  Xavier SoC, volta architecture

## References
- https://en.wikipedia.org/wiki/List_of_Nvidia_graphics_processing_units
- https://en.wikipedia.org/wiki/GeForce
- https://en.wikipedia.org/wiki/Nvidia_Quadro-https://en.wikipedia.org/wiki/CUDA
- https://en.wikipedia.org/wiki/PhysX
- https://en.wikipedia.org/wiki/Bullet_(software)
- https://en.wikipedia.org/wiki/OpenACC
- https://en.wikipedia.org/wiki/OpenCL
- https://en.wikipedia.org/wiki/Drive_PX-series
- https://en.wikipedia.org/wiki/Tegra#Comparison
- http://www.anandtech.com/show/10714/nvidia-teases-xavier-a-highperformance-arm-soc
- https://gputechconf2017.smarteventscloud.com/connect/sessionDetail.ww?SESSION_ID=112513
- https://www.gputechconf.jp/assets/files/1062.pdf
- https://www.slideshare.net/shri123/drive-px-2
- https://gputechconf2017.smarteventscloud.com/connect/sessionDetail.ww?SESSION_ID=112513
- https://gputechconf2017.smarteventscloud.com/connect/search.ww#loadSearch-searchPhrase=driveworks&searchType=session&tc=0&sortBy=titleSort&p=%3Fdo-search
- https://www.youtube.com/watch?v=iIcCyxN_RC0 (Miguel Sainz)
- http://www.academia.edu/27756684/NVIDIA_Tesla_P100_NVIDIA_Tesla_P100 (Miguel Sainz)

## Disclaimer
All the content here are provided with references (mostly from the wikipedia articles, as is) and the intent is to consolidate in concise format for research and educational purpose. The content under different headings are the result of interpretation, understanding and in no means to reflect or provide false information, thus citation needed.