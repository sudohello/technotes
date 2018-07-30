/*
Title: Image Processing & Photography
Decription: Image Processing & Photography
Author: Bhaskar Mangal
Date: 03rd May 2018
Last Updated: 17th May 2018
Tags: Image Processing & Photography
*/

**Table of Contents**

[TOC]

# Image Processing

## Photography

**bit depth**
- https://www.cambridgeincolour.com/tutorials/bit-depth.htm
- Bit depth quantifies how many unique colors are available in an image's color palette in terms of the number of 0's and 1's, or "bits," which are used to specify each color.
- This does not mean that the image necessarily uses all of these colors, but that it can instead specify colors with that level of precision
- For a grayscale image, the bit depth quantifies how many unique shades are available
- Images with higher bit depths can encode more shades or colors since there are more combinations of 0's and 1's available

**primary color & color channel**
- Every color pixel in a digital image is created through some combination of the three primary colors: red, green, and blue
- Each primary color is often referred to as a "color channel" and can have any range of intensity values specified by its bit depth.

**bits per channel**
- The bit depth for each primary color is termed the "bits per channel"

**bits per pixel (bpp)**
- The "bits per pixel" (bpp) refers to the sum of the bits in all three color channels and represents the total colors available at each pixel. 

**true color**
- Most color images from digital cameras have 8-bits per channel and so they can use a total of eight 0's and 1's.
- This allows for `2^8` or `256` different combinations—translating into 256 different intensity values for each primary color. When all three primary colors are combined at each pixel, this allows for as many as `2^(8*3)` or `16,777,216` different colors, or **true color**
- This is referred to as 24 bits per pixel since each pixel is composed of three 8-bit color channels
- The human eye can only discern about 10 million different colors, so saving an image in any more than 24 bpp is excessive if the only intended purpose is for viewing
- The available bit depth settings depend on the file type. Standard JPEG and TIFF files can only use 8-bits and 16-bits per channel, respectively.

**RGB histogram**
- https://www.cambridgeincolour.com/tutorials/histograms1.htm
- Each pixel in an image has a color which has been produced by some combination of the primary colors red, green, and blue (RGB).
- Each of these colors can have a brightness value ranging from 0 to 255 for a digital image with a bit depth of 8-bits.
- A RGB histogram results when the computer scans through each of the RGB brightness values and counts how many are at each level from 0 through 255. 

**tonal range**
- The region where most of the brightness values are present is called the "tonal range" 
- Although most cameras will produce midtone-centric histograms when in an automatic exposure mode, the distribution of peaks within a histogram also depends on the tonal range of the subject matter. 

**low key and high key**
- Images where most of the tones occur in the shadows are called "low key"
- Images where most of the tones occur in the highlights are called "high key"

**clipped" or "blown**
- Since cameras measure reflected as opposed to incident light, they are unable to assess the absolute brightness of their subject.
- Detail can never be recovered when a region becomes so overexposed that it becomes solid white. When this occurs the highlights are said to be "clipped" or "blown"

**Contrast**
- A histogram can also describe the amount of contrast. Contrast is a measure of the difference in brightness between light and dark areas in a scene. 
- Contrast can have a significant visual impact on an image by emphasizing texture
- The high contrast subject has deeper shadows and more pronounced highlights, creating texture which "pops" out at the viewer
- Directly exposed areas, produces deeper shadows, and stronger highlights
- Diffuse, reflected light produces lower contrast

https://www.cambridgeincolour.com/tutorials/histograms2.htm


**Image noise**
- https://www.cambridgeincolour.com/tutorials/image-noise.htm
- Image noise is the digital equivalent of film grain for analogue cameras
- For digital images, this noise appears as random speckles on an otherwise smooth surface and can significantly degrade image quality
- It is sometimes desirable since it can add an old-fashioned, grainy look which is reminiscent of early film
- Some noise can also increase the apparent sharpness of an image
- Noise increases with the sensitivity setting in the camera, length of the exposure, temperature, and even varies amongst different camera models

**SIGNAL TO NOISE RATIO (SNR)**
- Some degree of noise is always present in any electronic device that transmits or receives a "signal"
- A sufficiently high SNR clearly separate the image information from background noise
- A low SNR would produce an image where the "signal" and noise are more comparable and thus harder to discern from one another

**ISO SPEED**
- A camera's "ISO setting" or "ISO speed" is a standard which describes its absolute sensitivity to light
- ISO settings are usually listed as factors of 2, such as ISO 50, ISO 100 and ISO 200 and can have a wide range of values
- Higher numbers represent greater sensitivity and the ratio of two ISO numbers represents their relative sensitivity, meaning a photo at ISO 200 will take half as long to reach the same level of exposure as one taken at ISO 100 (all other settings being equal).
- ISO speed is analogous to ASA speed for different films, however a single digital camera can capture images at several different ISO speeds.
- This is accomplished by amplifying the image signal in the camera, however this also amplifies noise and so higher ISO speeds will produce progressively more noise.

**TYPES OF NOISE**
- Digital cameras produce three common types of noise:
	* random noise
		- Short Exposure, High ISO Speed
		- less objectionable random noise is usually much more difficult to remove without degrading the image
	* fixed pattern noise
		- Long Exposure, Low ISO Speed
		- fixed pattern noise appears more objectionable, it is usually easier to remove since it is repeatable. A camera's internal electronics just has to know the pattern and it can subtract this noise away to reveal the true image.
	* banding noise
		- Susceptible Camera, Brightened Shadows
		- Banding noise is most visible at high ISO speeds and in the shadows, or when an image has been excessively brightened.
		- Banding noise can also increase for certain white balances, depending on camera model.

**how image noise varies**
- according to color or "chroma," luminance, intensity and size or spatial frequency.
- noise variation based on ISO and color channel

**CHARACTERISTICS**
- Noise can also vary within an individual image
- Digital cameras, darker regions will contain more noise than the brighter regions; with film the inverse is true
- Brighter regions have a stronger signal due to more light, resulting in a higher overall SNR
- This means that images which are underexposed will have more visible noise — even if you brighten them up to a more natural level afterwards
- Increasing ISO speed always produces higher noise
- The greater the area of a pixel in the camera sensor, the more light gathering ability it will have — thus producing a stronger signal. As a result, cameras with physically larger pixels will generally appear less noisy since the signal is larger relative to the noise. This is why cameras with more megapixels packed into the same sized camera sensor will not necessarily produce a better looking image.
- a stronger signal does not necessarily lead to lower noise since it is the relative amounts of signal and noise that determine how noisy an image will appear.

Noise is also composed of two elements: fluctuations in color and luminance.
- Color or "chroma" noise is usually more unnatural in appearance and can render images unusable if not kept under control.
- Noise reduction software can be used to selectively reduce both chroma and luminance noise, however complete elimination of luminance noise can result in unnatural or "plasticy" looking images.

Noise fluctuations can also vary in both their magnitude and spatial frequency,
- The term "fine-grained" was used frequently with film to describe noise whose fluctuations occur over short distances, which is the same as having a high spatial frequency. 
- The magnitude of noise is usually described based on a statistical measure called the "standard deviation," which quantifies the typical variation a pixel will have from its "true" value.
- The blue and green channels will usually have the highest and lowest noise, respectively, in digital cameras with Bayer arrays


**Camera Sensors**
https://www.cambridgeincolour.com/tutorials/camera-sensors.htm
https://www.cambridgeincolour.com/tutorials/digital-camera-sensor-size.htm

- A digital camera uses an array of millions of tiny light cavities or "photosites" to record an image. When you press your camera's shutter button and the exposure begins, each of these is uncovered to collect photons and store those as an electrical signal. Once the exposure finishes, the camera closes each of these photosites, and then tries to assess how many photons fell into each cavity by measuring the strength of the electrical signal. The signals are then quantified as digital values, with a precision that is determined by the bit depth. The resulting precision may then be reduced again depending on which file format is being recorded (0 - 255 for an 8-bit JPEG file).
- Since these cavities are unable to distinguish how much they have of each color
- To capture color images, a filter has to be placed over each cavity that permits only particular colors of light

**Bayer array**
- Virtually all current digital cameras can only capture one of three primary colors in each cavity, and so they discard roughly 2/3 of the incoming light. As a result, the camera has to approximate the other two primary colors in order to have full color at every pixel. The most common type of color filter array is called a Bayer array
- A Bayer array consists of alternating rows of red-green and green-blue filters [RG-GB]
- Redundancy with green pixels produces an image which appears less noisy and has finer detail than could be accomplished if each color were treated equally
- Not all digital cameras use a Bayer array, however this is by far the most common setup. For example, the Foveon sensor captures all three colors at each pixel location, whereas other sensors might capture four colors in a similar array: red, green, blue and emerald green

**BAYER DEMOSAICING**
- Bayer "demosaicing" is the process of translating this Bayer array of primary colors into a final image which contains full color information at each pixel. 
- Other demosaicing algorithms exist which can extract slightly more resolution, produce images which are less noisy, or adapt to best approximate the image at each location.

**DEMOSAICING ARTIFACTS**
- The most common artifact is moiré (pronounced "more-ay"), which may appear as repeating patterns, color artifacts or pixels arranged in an unrealistic maze-like pattern
- These artifacts depend on both the type of texture and software used to develop the digital camera's RAW file.
- This is an unavoidable consequence of any system that samples an otherwise continuous signal at discrete intervals or locations.
-  For this reason, virtually every photographic digital sensor incorporates something called an optical low-pass filter (OLPF) or an anti-aliasing (AA) filter.

* how does your digital camera's sensor size influence different types of photography?
- Much confusion often arises on this topic because there are both so many different size options, and so many trade-offs relating to depth of field, image noise, diffraction, cost and size/weight.
- Sensor sizes currently have many possibilities, depending on their use, price point and desired portability

**CROP FACTOR & FOCAL LENGTH MULTIPLIER**
- The crop factor is the sensor's diagonal size compared to a full-frame 35 mm sensor.
- It is called this because when using a 35 mm lens, such a sensor effectively crops out this much of the image at its exterior (due to its limited size).
- The focal length multiplier relates the focal length of a lens used on a smaller format to a 35 mm lens producing an equivalent angle of view, and is equal to the crop factor. This means that a 50 mm lens used on a sensor with a 1.6X crop factor would produce the same field of view as a 1.6 x 50 = 80 mm lens on a 35 mm full frame sensor
- The lens focal length does not change just because a lens is used on a different sized sensor — just its angle of view
- A 50 mm lens is always a 50 mm lens, regardless of the sensor type.
- At the same time, "crop factor" may not be appropriate to describe very small sensors because the image is not necessarily cropped out (when using lenses designed for that sensor).
- 35 mm Equivalent Focal Length

**LENS SIZE AND WEIGHT CONSIDERATIONS**
- Smaller sensors require lighter lenses (for equivalent angle of view, zoom range, build quality and aperture range).

**DEPTH OF FIELD REQUIREMENTS**
- As sensor size increases, the depth of field will decrease for a given aperture (when filling the frame with a subject of the same size and distance). 
- This is because larger sensors require one to get closer to their subject, or to use a longer focal length in order to fill the frame with that subject. 
- This means that one has to use progressively smaller aperture sizes in order to maintain the same depth of field on larger sensors. 
- A shallower depth of field may be desirable for portraits because it improves background blur
- A larger depth of field is desirable for landscape photography

**INFLUENCE OF DIFFRACTION**
- the diffraction-limited depth of field is constant for all sensor sizes
- This factor may be critical when deciding on a new camera for your intended use, because more pixels may not necessarily provide more resolution (for your depth of field requirements).
- In fact, more pixels could even harm image quality by increasing noise and reducing dynamic range (next section).

**PIXEL SIZE: NOISE LEVELS & DYNAMIC RANGE**
- Larger sensors generally also have larger pixels (although this is not always the case), which give them the potential to produce lower image noise and have a higher dynamic range. 
- **DYNAMIC RANGE** describes the range of tones which a sensor can capture below when a pixel becomes completely white, but yet above when texture is indiscernible from background noise (near black). 
- Larger pixels have a greater volume — and thus a greater range of photon capacity — these generally have a higher dynamic range
- Larger pixels receive a greater flux of photons during a given exposure time (at the same f-stop), so their light signal is much stronger
- Even if two sensors have the same apparent noise when viewed at 100%, the sensor with the higher pixel count will produce a cleaner looking final print.

**COST OF PRODUCING DIGITAL SENSORS**
- costs increase proportional to the square of sensor area (a sensor 2X as big costs 4X as much)
- the relative cost of a larger sensor is likely to remain significantly more expensive (per unit area) when compared to some smaller size.

**OTHER CONSIDERATIONS**
- Some lenses are only available for certain sensor sizes (or may not work as intended otherwise), which might also be a consideration if these help your style of photography.
- One notable type is tilt/shift lenses, which allow one to increase (or decrease) the apparent depth of field using the tilt feature
- Fast ultra-wide angle lenses (f/2.8 or larger) aren't as common for cropped sensors, which may be a deciding factor if needed in sports or photojournalism

**CONCLUSIONS: OVERALL IMAGE DETAIL & COMPETING FACTORS**
- Depth of field is much shallower for larger format sensors, however one could also use a smaller aperture before reaching the diffraction limit (for your chosen print size and sharpness criteria)

**Which option has the potential to produce the most detailed photo?**
- Larger sensors (and correspondingly higher pixel counts) undoubtedly produce more detail if you can afford to sacrifice depth of field.
- If you wish to maintain the same depth of field, larger sensor sizes do not necessarily have a resolution advantage
- The diffraction-limited depth of field is the same for all sensor sizes. In other words, if one were to use the smallest aperture before diffraction became significant, all sensor sizes would produce the same depth of field — even though the diffraction limited aperture will be different
- If depth of field is the limiting factor, the required exposure time increases with sensor size for the same sensitivity.
- On the other hand, exposure times may not necessarily increase as much as one might initially assume, because larger sensors generally have lower noise (and can thus afford to use a higher sensitivity ISO setting while maintaining similar perceived noise)
- Ideally, perceived noise levels (at a given print size) generally decrease with larger digital camera sensors (regardless of pixel size).


**LENS DIFFRACTION & PHOTOGRAPHY**
- Diffraction is an optical effect which limits the total resolution of your photography — no matter how many megapixels your camera may have.
- It happens because light begins to disperse or "diffract" when passing through a small opening (such as your camera's aperture). This effect is normally negligible, since smaller apertures often improve sharpness by minimizing lens aberrations.
- However, for sufficiently small apertures, this strategy becomes counterproductive — at which point your camera is said to have become diffraction limited. Knowing this limit can help maximize detail, and avoid an unnecessarily long exposure or high ISO speed
- For an ideal circular aperture, the 2-D diffraction pattern is called an "airy disk," after its discoverer George Airy
- The width of the airy disk is used to define the theoretical maximum resolution for an optical system (defined as the diameter of the first dark circle).
- When the diameter of the airy disk's central peak becomes large relative to the pixel size in the camera (or maximum tolerable circle of confusion), it begins to have a visual impact on the image. Once two airy disks become any closer than half their width, they are also no longer resolvable (Rayleigh criterion).
- **Diffraction thus sets a fundamental resolution limit that is independent of the number of megapixels, or the size of the film format. It depends only on the f-number of your lens, and on the wavelength of light being imaged.**
- One can think of it as the smallest theoretical "pixel" of detail in photography. Furthermore, the onset of diffraction is gradual; prior to limiting resolution, it can still reduce small-scale contrast by causing airy disks to partially overlap.

**Technical NOTES**
- The light in the middle of the visible spectrum has wavelength of `~550 nm`
- Typical digital SLR cameras can capture light with a wavelength of anywhere from `450 to 680 nm`
- The physical pixels do not actually occupy 100% of the sensor area, but instead have gaps in between.
- Some cameras have pixels which are slightly rectangular, in which case diffraction will reduce resolution more in one direction than the other.
- The aperture in reality are polygonal with 5-8 sides
- Camera manufacturers leave some pixels unused around the edge of the sensor
- Since not all manufacturers specify the number of used vs. unused pixels, only used pixels were considered when calculating the fraction of total sensor area. The pixel sizes above are thus slightly larger than if measured (but by no more than 5%).

- contrast or acutance 
- noise (ISO) vs shutter speed
-  f-number as being important (which describes focal length relative to aperture size).

**RESOLUTION DEFINITIONS**
- If it's not simply the pixel size, how does one define the resolution of a digital camera?
- The real-world resolution limit of a Bayer array is typically around 1.5X as large as the individual pixels.
- **Resolution** describes the camera's ability to distinguish between closely spaced elements of detail, such as the two sets of lines shown above.

**DIGITAL CAMERAS: COLOR vs. LUMINOSITY DETAIL**
https://www.cambridgeincolour.com/tutorials/lens-quality-mtf-resolution.htm

**SHARPNESS**
- https://www.cambridgeincolour.com/tutorials/sharpness.htm
- Photos require both high acutance and resolution to be perceived as critically sharp
- Sharpness is ultimately limited by your camera equipment, image magnification and viewing distance
- Two fundamental factors contribute to the perceived sharpness of an image: resolution and acutance.
- **Acutance** describes how quickly image information transitions at an edge, and so high acutance results in sharp transitions and detail with clearly defined borders.
- For digital cameras, resolution is limited by your digital sensor, whereas acutance depends on both the quality of your lens and the type of post-processing.
-  Acutance is the only aspect of sharpness which is still under your control after the shot has been taken, so acutance is what is enhanced when you digitally sharpen an imag
- Sharpness is also significantly affected by your camera technique. Even small amounts of camera shake can dramatically reduce the sharpness of an image. Proper shutter speeds, use of a sturdy camera tripod and mirror lock-up can also significantly impact the sharpness of your prints.

**SHARPENING: UNSHARP MASK**
- An "unsharp mask" is actually used to sharpen an image, contrary to what its name might lead you to believe. Sharpening can help you emphasize texture and detail, and is critical when post-processing most digital images
- Unsharp masks are probably the most common type of sharpening, and can be performed with nearly any image editing software
- An unsharp mask cannot create additional detail, but it can greatly enhance the appearance of detail by increasing small-scale acutance.
- http://www.largeformatphotography.info/unsharp/
- https://www.cambridgeincolour.com/tutorials/local-contrast-enhancement.htm
- https://www.cambridgeincolour.com/tutorials/image-sharpening.htm


**DIGITAL IMAGE INTERPOLATION**
- https://www.cambridgeincolour.com/tutorials/image-interpolation.htm
- It happens anytime you resize or remap (distort) your image from one pixel grid to another.
- Image resizing is necessary when you need to increase or decrease the total number of pixels.
- Whereas, remapping can occur under a wider variety of scenarios: correcting for lens distortion, changing perspective, and rotating an image.
- Even if the same image resize or remap is performed, the results can vary significantly depending on the interpolation algorithm.
- It is only an approximation, therefore an image will always lose some quality each time interpolation is performed.
- Interpolation works by using known data to estimate values at unknown points.
- Image interpolation works in two directions, and tries to achieve a best approximation of a pixel's color and intensity based on the values at surrounding pixels.
- Therefore results quickly deteriorate the more you stretch an image, and interpolation can never add detail to your image which is not already present.
- Interpolation also occurs each time you rotate or distort an image.
- All non-adaptive interpolators attempt to find an optimal balance between three undesirable artifacts: edge halos, blurring and aliasing
- Adaptive interpolators may or may not produce the above artifacts, however they can also induce non-image textures or strange pixels at small-scales

**ANTI-ALIASING**
- Anti-aliasing is a process which attempts to minimize the appearance of aliased or jagged diagonal edges, termed "jaggies." 
- Anti-aliasing removes these jaggies and gives the appearance of smoother edges and higher resolution.


**TYPES OF INTERPOLATION ALGORITHMS**
- Common interpolation algorithms can be grouped into two categories:adaptive and non-adaptive.
- Adaptive methods change depending on what they are interpolating (sharp edges vs. smooth texture)
- Non-adaptive methods treat all pixels equally
- Non-adaptive algorithms include: nearest neighbor, bilinear, bicubic, spline, sinc, lanczos and others

**Human Eye**
- The human eye is more sensitive to green light than both red and blue light
- The human eye can only discern about 10 million different colors
- Human vision perception has twice the acuity in luminance vs. color
- Human eye is equivalent to 576 megapixel camera

**OPTICAL vs. DIGITAL ZOOM**
- A camera performs an optical zoom by moving the zoom lens so that it increases the magnification of light before it even reaches the digital sensor.
- In contrast, a digital zoom degrades quality by simply interpolating the image — after it has been acquired at the sensor.
- Digital zoom should be almost entirely avoided, unless it helps to visualize a distant object on your camera's LCD preview screen

**Tools**
* de-noising
	- https://ni.neatvideo.com/download
	- https://www.picturecode.com/download.php

## Digital Image Processing
- https://en.wikipedia.org/wiki/Digital_image_processing

**Digital image processing is the only practical technology for:**
* Classification
* Feature extraction
* Multi-scale signal analysis
* Pattern recognition
* Projection

**Some techniques which are used in digital image processing include:**
* Anisotropic diffusion
* Hidden Markov models
* Image editing
* Image restoration
* Independent component analysis
* Linear filtering
* Neural networks
* Partial differential equations
* Pixelation
* Principal components analysis
* Self-organizing maps
* Wavelets

**Digital image transformations**
* Filtering
	- Digital filters are used to blur and sharpen digital images.
	- Filtering can be performed in the spatial domain by convolution with specifically designed kernels (filter array), or in the frequency (Fourier) domain by masking specific frequency regions.

## Image Processing in Python

- OpenSource Computer Vision, more commonly known as OpenCV, is a more advanced image manipulation and processing software than PIL, Pillow
- In Python, image processing using OpenCV is implemented using the `cv2` and `NumPy` modules
- [Image Processing using **Pillow**](https://pillow.readthedocs.io/en/3.0.x/handbook/tutorial.html)
- [**OpenCV** (computer vision)](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)
- **scipy.ndimage** : for nd-arrays. Basic filtering, mathematical morphology, regions properties
	- ScipyLectures-simple.pdf
- **mahotas**
	- http://luispedro.org/software/mahotas/
- **ITK** (3D images and registration)
- http://pythoninformer.com/python-libraries/numpy/numpy-and-images/

**Some Common tasks in image processing:**
1. Input/Output, displaying images
2. Basic manipulations:
	- Geometrical transformations: cropping, flipping, rotating, ...
	- Statistical information
3. Image filtering:
	- Blurring/smoothing
	- Sharpening
	- Denoising
	- Mathematical morphology
4. Image segmentation: labeling pixels corresponding to different objects
5. Classification
6. Feature extraction:
	- Edge detection
	- Segmentation
7. Measuring objects properties: ndimage.measurements
8. Registration


**Image manipulation and processing using Numpy and Scipy**
- submodule `scipy.ndimage` provides functions operating on n-dimensional NumPy arrays
- Image = 2D numerical array, 3D: CT, MRI, 2D + time, or 4D
- dtype is uint8 for 8-bit images (0-255)

## 1. Input/Output, displaying images
```python
from scipy import ndimage
from scipy import misc
f = misc.face()
misc.imsave('face.png', f) # uses the Image module (PIL)
#
import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()
#
face = misc.imread('face.png') # type: <type 'numpy.ndarray'>
face.shape, face.dtype
#
# Opening raw files (camera, 3-D images)
face.tofile('face.raw') # Create raw file
face_from_raw = np.fromfile('face.raw', dtype=np.uint8)
face_from_raw.shape
#
# For large data, use np.memmap for memory mapping: data are read from the file, and not loaded into memory
face_memmap = np.memmap('face.raw', dtype=np.uint8, shape=(768, 1024, 3))
#
# Working on a list of image files
#
for i in range(10):
	im = np.random.randint(0, 256, 10000).reshape((100, 100))
	misc.imsave('random_%02d .png' % i, im)

from glob import glob
filelist = glob('random*.png')
filelist.sort()
```
**displaying image**
- [plot_display_face.py](py/plot_display_face.py)
```python
import scipy.misc
import matplotlib.pyplot as plt

f = scipy.misc.face(gray=True)

plt.figure(figsize=(10, 3.6))

plt.subplot(131)
plt.imshow(f, cmap=plt.cm.gray)

plt.subplot(132)
# plt.imshow(f, cmap=plt.cm.gray, vmin=30, vmax=200)
plt.imshow(f, cmap=plt.cm.gray,interpolation='bilinear')
plt.axis('off')

plt.subplot(133)
plt.imshow(f, cmap=plt.cm.gray)
plt.contour(f, [50, 200])
plt.axis('off')

plt.subplots_adjust(wspace=0, hspace=0., top=0.99, bottom=0.01, left=0.05,
                    right=0.99)
plt.show()
```
**Interpolation Methods**
- https://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
- [interpolation_filters.py](py/interpolation_filters.py)

## 2. Basic manipulations
- Images are arrays: use the whole numpy machinery
- Creating a cicular mask
```python
from scipy import misc
import numpy as np
#
face = misc.face(gray=True)
lx,ly = face.shape
X,Y=np.ogrid[0:lx,0:ly]
mask = (X - lx/2)**2 + (Y - ly/2)**2 > lx*ly/4
face = misc.face()
face[mask] = 0
#
import matplotlib.pyplot as plt
plt.imshow(face)
plt.show()
```

### a. Geometrical transformations: cropping, flipping, rotating, ...
- [plot_geom_face.py](py/plot_geom_face.py)
```python
# Cropping
crop_face = face[lx // 4: - lx // 4, ly // 4: - ly // 4]
# Flipping up<-->down
flipped = np.flipud(face)

from scipy import ndimage
rotate1 = ndimage.rotate(face,45)
rotate2 = ndimage.rotate(face,45,reshape=False)
```

### b. Statistical information
```python
from scipy import misc
import numpy as np
#
face = misc.face(gray=True)
face.mean()
face.max()
face.min()
np.histogram(face)
```

## 3. Image filtering
> one of the most critical aspect and place to innovate

- Filtering is **replacing the value of pixel(s)** by **a function**
- What type of a function?
- The function of **values of neighbourhood (nbh) pixels**
- What neighbourhood means? Define It.
- Neighbourhood can be: sqaure, disk or more complicated structuring element

### a. Blurring/smoothing
- https://www.scipy-lectures.org/advanced/image_processing/auto_examples/plot_blur.html
```python
from scipy import misc
from scipy import ndimage
#
face = misc.face(gray=True)
#
# Gaussian filter
blurred_face = ndimage.gaussian_filter(face, sigma=3)
very_blurred = ndimage.gaussian_filter(face, sigma=5)
#
# Uniform filter
local_mean = ndimage.uniform_filter(face, size=11)
```

### b. Sharpening
```python
import scipy
from scipy import ndimage
import matplotlib.pyplot as plt

f = scipy.misc.face(gray=True).astype(float)

blurred_f = ndimage.gaussian_filter(f, 3)
filter_blurred_f = ndimage.gaussian_filter(blurred_f, 1)
alpha = 30
//y = mx + c
sharpened = alpha * (blurred_f - filter_blurred_f) +  blurred_f
```
Your FD 674610018453 has been opened on 17-05-2018.
https://blog.ndustrial.io/temperature-gradient-maps-with-mapbox-gl-9f97fb44d5f2
https://blog.ndustrial.io/digital-twins-or-digital-doppelgangers-cd04957252af
https://github.com/dismedia/gradient2d
https://medium.com/vizzuality-blog/saving-the-with-how-we-used-webgl-and-pixi-js-for-temporal-mapping-2cffaed60b91

### c. Create Noise and Denoising
- A Gaussian filter smoothes the noise out. . . and the edges as well
- Most local linear isotropic filters blur the image ( ndimage.uniform_filter )
- A median filter preserves better the edges
- Median filter: better result for straight boundaries (low curvature)
- `ndimage.distance_transform_bf`
- Other rank filter: `ndimage.maximum_filter`, `ndimage.percentile_filter`
- Other local non-linear filters: `Wiener ( scipy.signal.wiener )`, etc.
- More denoising filters are available in `skimage.denoising`
```python
from scipy import misc

f = misc.face(gray=True)
f = f[230:290, 220:320]
#
# Create Noise
//y = c + mx
noisy = f + 0.4 * f.std() * np.random.random(f.shape)
#
gauss_denoised = ndimage.gaussian_filter(noisy, 2)
med_denoised = ndimage.median_filter(noisy, 3)
```

### d. Mathematical morphology
- https://en.wikipedia.org/wiki/Mathematical_morphology
- http://cmm.ensmp.fr/~serra/cours/index.htm
Mathematical morphology (MM) is a theory and technique for the analysis and processing of geometrical structures, based on set theory, lattice theory, topology, and random functions. MM is most commonly applied to digital images, but it can be employed as well on graphs, surface meshes, solids, and many other spatial structures.

```python
```
- Granulometry (morphology)
	- https://en.wikipedia.org/wiki/Granulometry_%28morphology%29
	- In mathematical morphology, granulometry is an approach to compute a size distribution of grains in binary images, using a series of morphological opening operations.

## 4. Image segmentation: labeling pixels corresponding to different objects

## 5. Classification

## 6. Feature Extraction

### a. Edge detection
- Use a gradient operator (Sobel) to find high intensity variations:
- `sx = ndimage.sobel(im, axis=0, mode='constant')`

### b. Segmentation
- Histogram-based segmentation (no spatial information)
```python
hist, bin_edges = np.histogram(img, bins=60)
```
- spectral clustering function of the scikit-learn in order to segment glued objects.
- Measuring objects properties
	* mean
	* Analysis of connected components
	* Find region of interest enclosing object
	* Other spatial measures: ndimage.center_of_mass , ndimage.maximum_position , etc.

## [scikit-image / skimage](http://scikit-image.org/)
- **Scikit-image is an image processing toolbox for SciPy**
- 0.13.x documentation: http://scikit-image.org/docs/0.13.x/
- 0.13.x User Guide: http://scikit-image.org/docs/0.13.x/user_guide/getting_started.html
- scikit-image is a Python package dedicated to image processing, and using natively NumPy arrays as image objects
- basic operations such as masking and labeling are a prerequisite
- **image** np.ndarray
- **pixels** array values: a[2, 3]
- **channels** array dimensions
- **image encoding** dtype ( np.uint8 , np.uint16 , np.float )
- **filters** functions ( numpy , skimage , scipy )
```python
import skimage
from skimage import data
from skimage import filters
#
camera = data.camera()
filters.gaussian(camera,1)
```
- most functions are in subpackages
- Most scikit-image functions take NumPy ndarrays as arguments
- http://scikit-image.org/docs/stable/auto_examples/

**Input/output, data types and colorspaces**
- `skimage.data_dir` = `/usr/local/lib/python2.7/dist-packages/skimage/data`
- imsave also uses an external plugin such as PIL
```python
from skimage import io
import os
filename = os.path.join(skimage.data_dir, 'camera.png')
# reading image files
camera = io.imread(filename)
logo = io.imread('http://scikit-image.org/_static/img/logo.png')
io.imsave('local_logo.png', logo)
```
- Image ndarrays can be represented either by integers (signed or unsigned) or floats
- Different integer sizes are possible: 8-, 16- or 32-bytes, signed or unsigned.
- Careful with overflows with integer data types
```python
camera_multiply = 3 * camera
```
- An important (if questionable) skimage convention: float images are supposed to lie in [-1, 1] (in order to have comparable contrast for all float images)
```python
from skimage import img_as_float
camera_float = img_as_float(camera)
camera.max(), camera_float.max()
```
- Some image processing routines need to work with float arrays, and may hence output an array with a different type and the data range from the input array
- Utility functions are provided in skimage to convert both the dtype and the data range, following skimage’s conventions: 'util.img_as_float`, `util.img_as_ubyte` , etc.
- http://scikit-image.org/docs/stable/user_guide/data_types.html
```python
from skimage import filters
camera_sobel = filters.sobel(camera)
camera_sobel.max()
```

## Exercises
- https://code.tutsplus.com/tutorials/image-processing-using-python--cms-25772
- https://www.analyticsvidhya.com/blog/2014/12/image-processing-python-basics/
- http://www.scipy-lectures.org/advanced/image_processing/

## References
- http://www.scipy-lectures.org/intro/index.html
- http://docs.python-guide.org/en/latest/scenarios/imaging/
- https://www.codementor.io/isaib.cicourel/image-manipulation-in-python-du1089j1u
- https://www.quora.com/in/What-is-the-best-way-to-learn-image-processing-using-Python
- http://effbot.org/imagingbook/pil-index.htm
- https://www.datasciencecentral.com/profiles/blogs/deep-learning-amp-art-neural-style-transfer-an-implementation

### git
https://github.com/jacobrosenthal/drop-analysis

## Image Processing for Computer Vision
- International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences - ISPRS Archives

**Image-processing:**
Scikit-image
* Other, more powerful and complete modules:
	- OpenCV (Python bindings)
	- CellProfiler
	- ITK with Python bindings

### Radiometrically improve the image quality
https://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XL-5-W4/315/2015/isprsarchives-XL-5-W4-315-2015.pdf
Motion blur, sensor noise, jpeg artifacts, wrong depth of field are just some of the possible problems that are negatively affecting automated 3D reconstruction methods.

how the radiometric pre-processing of image datasets (particularly in RAW format) can help in improving the performances of state-of-the-art automated image processing tools. Beside a review of common pre-processing methods, an efficient pipeline based on color enhancement, imageenoising, RGB to Gray conversion and image content enrichment is presented.

to minimize typical failure causes by SIFT-like algorithms (Apollonio et al., 2014) due to changes in the illumination conditions or low contrast blobs areas

Propossed Image pre-processing pipeline:-
1. Color balancing and Exposure equalization
The aim is essentially to have radiometrically-calibrated images ensuring the consistency of surface colors along all the images (i.e. as much similar as possible RGB values for homologous pixels).

Starting from captured RAW images our workflow includes:
- exposure compensation
- optical correction
- sharpen
- color balance

converting all images to the camera’s native linear color space
features (i.e., orientation, exposure and framed surfaces)
using an appropriate color space from the beginning of the image processing.

2. Enhancement: Image denoising
Image noise is defined in the ISO 15739 standard as “unwanted variations in the response of an imaging system” (ISO 15739, 2003). It is formed when incoming light is converted from photons to an electrical signal and originates from the camera sensor, its sensitivity and the exposure time as well as by digital processing (or all these factors together). Noise type includes:-

* **Fixed pattern noise (‘hot’ and ‘cold’ pixels):** it is due to sensor defects or long time exposure, especially with high temperatures. Fixed pattern noise always appears in the same position.
* **Random noise:** it includes intensity and color fluctuations above and below the actual image intensity. They are always random at any exposure and more influenced by ISO speed.
* **Banding noise:** it is caused by unstable voltage power and is characterized by the straight band in frequency on the image. It is highly camera-dependent and more visible at high ISO speed and in dark image. Brightening the image or white balancing can increase the problem

In real-world photographs, the highest spatial-frequency detail consists mostly of variations in brightness (‘luminance detail’) rather than variations in hue (‘chroma detail’):

* **Luminance noise** is composed of noisy bright pixels that give the image a grainy appearance. High-frequency noise is prevalent in the luminance channel, which can range from fine grain to more distinct speckle noise. This type of noise does not significantly affect the image quality and can be left untreated or only minimally treated if needed.

* **Chrominance noise** appears as clusters of colored pixels, usually green and magenta. It occurs when the luminance is low due to the inability of the sensor to differentiate color in low light levels. As a result, errors in the way color is recorded are visible and hence the appearance of color artifacts in the demosaicked image.


Under all these considerations, the noise model can be approximated with two components:
* a) A signal-independent **Gaussian noise modeling** the fixed pattern noise (FPN)
	- Anscombe transform by Makitalo & Foi (2011) and Foi (2011), argue that, when combined with suitable forward and inverse variance-stabilizing transformations (VST), algorithms designed for homoscedastic Gaussian noise work just as well as ad-hoc algorithms based on signal-dependent noise models
	- This explains why the noise is assumed to be uniform, white and Gaussian, having previously applied a VST to the noisy image to take into account the Poisson component.
* b) A signal-dependent **Poisson noise modeling** the temporal (random) noise, called Shot Noise.
	- Wavelet-based denoising methods (Nowak & Baraniuk, 1997; Kolaczyk, 1999) propose adaptation of the transform threshold to the local noise level of the Poisson process

- A patch-based algorithm denoises each pixel by using knowledge of (a) the patch surrounding it and (b) the probability density of all existing patches
- Typical noise reduction software reduces the visibility of noise by smoothing the image, while preserving its details. The classic methods estimate white homoscedastic noise only, but they can be adapted easily to estimate signal- and scale-dependent noise

**The main goals of image denoising algorithms are:**
* Perceptually flat regions should be as smooth as possible and noise should be completely removed from these regions;
* Image boundaries should be well preserved and not blurred;
* Texture detail should not be lost;
* The global contrast should be preserved (i.e. the low-frequencies of denoised and input images should be equal);
* No artifacts should appear in the denoised image.

Numerous methods have been developed to meet these goals, **but they all rely on the same basic method to eliminate noise: averaging**
- The concept of averaging is simple, but determining which pixels to average is not
- To meet this challenge, four denoising principles are normally considered:
	* Transform thresholding (sparsity of patches in a fixed basis)
	* Sparse coding (sparsity on a learned dictionary)
	* Pixel averaging and block averaging (image self-similarity)
	* Bayesian patch-based methods (Gaussian patch model)

The current state-of-the-art denoising recipes are in fact a smart combination of all these ingredients.

**denoise algorithms**
	* Imagenomic Noiseware
	* Adobe Camera RAW denoise
	* Non-Local Bayesian filter
	* Noise Clinic
	* Color Block Matching 3D (CBM3D) filter

3. Enhancement: RGB to gray conversion
	* Most image-based 3D reconstruction algorithms are conceptually designed to work on grayscale images instead of the RGB triple
	* **Color to grayscale conversion can be seen as a dimensionality reduction problem**. This operation should not be underestimated, since there are many different properties that need to be preserved
	* In most of the cases isoluminant color changes are usually not preserved during the RGB to Gray conversion.
	* In general, RGB to Gray conversion method mainly focus on the reproduction of color images with grayscale mediums, with the goal of a perceptual accuracy in terms of the fidelity of the converted image. **These kinds of approaches are not designed to fulfill the needs of image matching algorithms where local contrast preservation is crucial during the matching process.** This was observed also in Lowe (2004) where the candidate keypoints with low contrast are rejected in order to decrease the ambiguity of the matching process.

**RGB to Gray conversion can be done in:**
* **Color Space (linear or non-linear):** the CIE Y method is a widely used conversion, based on the CIE 1931 XYZ color space. It takes the XYZ representation of the image and uses Y as the grayscale value
* **Image Space (called functional):** following Benedetti et al. (2012), they can be divided in three groups:
	1. a) **trivial methods**
				- they are the most basic and simple ones
				- they do not take into account the power distribution of the color channels
				- They lose a lot of image information
				- as for every pixel they discard two of the three color values, or discard one value averaging the remaining ones, not taking into account any color properties
				- Despite this loss, they are commonly used for their simplicity
				- A typical trivial method is the RGB Channel Filter that selects a channel between R, G or B and uses this channel as the grayscale value (afterwards called **GREEN2GRAY**)
	2. b) **direct methods**
				- the conversion is a linear function of the pixel’s color values
				- Typically, this class of functions takes into account the spectrum of different colors
				- The Naive Mean direct method takes the mean of the color channels
				- The advantage, compared to the other trivial ones, is that it takes information from every channel, though it does not consider the relative spectral power distribution of the RGB channels
				- The most popular of these methods is **RGBtoGRAY** that uses the NTSC CCIR 601 luma weights, with the formula `Y′= 0.2989R+0.5870G+0.1140B`
	3. c) **chrominance direct methods**
				- they are based on more advanced color spaces,trying to mitigate the problem related to isoluminant colors
				- they are local functions of the image pixels
				- they assign different grayscale values to isoluminant colors, altering the luminance information using the chrominance information
				- Chrominance direct methods can be performed either locally (Smith et al., 2008; Kim et al., 2009) or globally (Grundland & Dodgson, 2007).
				- Local methods make pixels in the color image not processed in the same way and usually rely on the local chrominance edges for enhancement.
				- Global methods strive to produce one mapping function for the whole image thus producing same luminance for the same RGB triplets and high-speed conversion

**Algorithims**
* GREEN2GRAY;
* Matlab RGB2GRAY;
* GRUNDLAND-DODGSON
* REALTIME
* **Bruteforce Isoluminants Decrease (BID)**
	The aim was to preserve the consistency between the images considering the following matching requirements
	- Feature discriminability:
	- Chrominance awareness:
	- Global mapping
	- Color consistency
	- Grayscale preservation
	- Unsupervised algorithm
	BID computes the statistical properties of the input dataset with the help of a representative collection of image patches
	It takes in input and analyses simultaneously the whole set of images that need to be matched Differently from other similar solutions as the Multi-Image Decolorize method
	BID has its foundation in the statistics of extreme-value distributions of the considered images and presents a more flexible strategy, adapting dynamically channel weights depending on specific input images, in order to find the most appropriate weights for a given color image

4. Enhancement: Image content enhancement - Adaptive Median Filter
- Low-texture surface such as plaster causes difficulties for feature detection
- such as the **Difference-of-Gaussian (DoG)** function, which extracts features in pixel level and compares them with adjacent ones and in stereo-matching algorithms
- The **Wallis filter** (Wallis, 1976), is a digital image processing function
	- that enhances the contrast levels and flattens the different exposure to achieve similar brightness in the images.
  - The filter is normally applied in order to optimize image datasets for subsequent image-matching procedures
  - Wallis uses two parameters to control the enhancement’s amount,
  	- the contrast expansion factor A
  	- and the brightness forcing factor B
	- The algorithm is adaptive and adjusts pixel brightness values in local areas only, contrary to a global contrast filter, which applies the same level of contrast throughout an entire image
	- The resulting image contains 	greater detail in both low and high-level contrast regions concurrently, ensuring that good local enhancement is achieved throughout the entire image
	- The Wallis filter requires the user to accurately set a target mean and standard deviation in order to locally adjusts areas and match the user-specified target values.
	- Firstly the filter divides the input image into neighboring square blocks with a user-defined size (‘window size’) in order to calculate local statistics. Then mean (M) and standard deviation (S) of the unfiltered image are calculated for each individual block based on the grey values of the pixels and the resulting value is assigned to the central cell of each block.
	- The mean and standard deviation values of all other cells in the block are calculated from this central cell by bilinear interpolation.
	- In this way, each individual pixel gets its own initial local mean and standard deviation based on surrounding pixel values.

## Performance, Quality
The performances of the pre-processing strategies previously described are reported using:
- The statistical output of the bundle adjustment (reprojection error)
- The number of points in the dense point cloud
- An accuracy evaluation of the dense matching results

## Tips
- blur fights noise at the cost of image detail
- Noise is a by-product of sharpness

## Keywords
* ICC profile
* luminance, luma - Luminance refers to brightness
* chrominance, chroma, chromatic (noise) - chrominance refers to color

## Search Phrases
* what is luminance and chrominance in image processing
	- https://www.quora.com/What-is-the-difference-between-luminance-and-chrominance-as-far-as-image-editing-is-concerned
	- https://wolfcrow.com/blog/understanding-luminance-and-chrominance/

With respect to noise reduction, luma and chroma have different characteristics due to how they are captured and how we perceive them. First, a little background info.

**Sensor and mosaic:**
- In a typical sensor, white lights are filtered into RGB components and captured by individual sensor cells. Each cell captures only one of the 3 primary light colors. A typical grid pattern contains 50% green, 25% red and 25% blue cells with green occupying two diagonal spots in a 2x2 group.

**Color space:**
- We all know about the RGB channels, you are probably familiar with hus, sat, value (HSV) color space. The fact is, the color space can be transformed into any number of orientation given 3 relatively orthogonal axis. One interesting color space is YCbCr used in TV transmission. Similar to lab color, the color space is specified in luminance, blue and red components. The interesting thing is, human vision perception has twice the acuity in luminance vs. color. TV transmission takes advantage of this characteristic and pack twice the luma resolution than chroma.

**Why are there more green than red and blue in a sensor?**
- Because green is most representative (closest to the orientation) of luma, it serves as a stand-in for luma channel. In fact, luma is a mix of about 60% green, 30% red and 10% blue.

**How do we make use of this information?**
- We know luminance contain twice the spatial resolution.
- Luminance is the main contributor to sharpness.
- We know chrominance is lower resolution
- Chrominance can tolerate more low pass filtering (read blurring).
- We also know blue sensors is less dense, and must be boosted because it has the lowest input level. Therefore blue channel tend to be the noisiest.

One way to tackle noise is to isolate the noise source and filter only the necessary channel with the appropriate amount. Examine individual RGB channels, and see if blue channel contributes most of the noise. Convert to lab color and see if luma channel is noisy. Perhaps filter more aggressively in chroma instead of luma channels. That’s the underlying approach, but in practice, lightroom color noise slider does a decent job.


* what-is-the-difference-between-cie-lab-cie-rgb-cie-xyy-and-cie-xyz
	- https://wolfcrow.com/blog/what-is-the-difference-between-cie-lab-cie-rgb-cie-xyy-and-cie-xyz/


## [Mathematical optimization: finding minima of functions](https://en.wikipedia.org/wiki/Mathematical_optimization)
- ScipyLectures-simple.pdf Notes

* Mathematical optimization deals with the problem of finding numerically minimums (or maximums or zeros)
of a function. In this context, the function is called **cost function**, or **objective function**, or **energy**.
* Here, we are interested in using scipy.optimize for black-box optimization: we do not rely on the mathe-
matical expression of the function that we are optimizing.

**Knowing your problem**
- The scale of an optimization problem is pretty much set by the **dimensionality of the problem**, i.e. the number of scalar variables on which the search is performed.
- how to determine dimensionality of the problem
	* https://disco.ethz.ch/courses/fs11/seminar/paper/samuel-1.pdf
-  What are the dimensionality estimation methods of a data set
- Convex vs Concave function
- `scipy.optimize.minimize_scalar()` uses **Brent’s method** to find the minimum of a function
- gradient descent
- conjugate gradient descent, `optimize.minimize(f, [2, -1], method="CG")`
- Gradient methods need the Jacobian (gradient) of the function. They can compute it numerically, but will perform better if you can pass them the gradient: `optimize.minimize(f, [2, 1], method="CG", jac=jacobian)`
- Newton and quasi-newton methods
- Newton method `optimize.minimize(f, [2,-1], method="Newton-CG", jac=jacobian)`
- Let’s compute the Hessian, `optimize.minimize(f, [2,-1], method="Newton-CG", jac=jacobian, hess=hessian)
- At very high-dimension, the inversion of the Hessian can be costly and unstable (large scale > 250).`
- Newton optimizers should not to be confused with Newton’s root finding method, based on the same principles, scipy.optimize.newton()
- Quasi-Newton methods: approximating the Hessian on the fly
- BFGS: BFGS (Broyden-Fletcher-Goldfarb-Shanno algorithm) refines at each step an approximation of the Hessian
- A gradient descent algorithm do not use: its a toy, use scipy’s optimize.fmin_cg

### References
- http://www.stanford.edu/~boyd/cvxbook/


## Definitions

### Luminance (Y)
* In scientific terms, the brightness of light is measured in terms of Luminance

## Colorspaces
- Color images are of shape (N, M, 3) or (N, M, 4) (when an alpha channel encodes transparency)
- Routines converting between different colorspaces (RGB, HSV, LAB etc.) are available in `skimage.color` : `color.rgb2hsv , color.lab2rgb` etc.

## 3D images
- 3D images (for example MRI or CT images)

## skimage

### Image preprocessing / enhancement
Goals: denoising, feature (edges) extraction, . . .

**Local filters**
- Local filters replace the value of pixels by a function of the values of neighboring pixels. The function can be linear or non-linear.
- Neighbourhood: square (choose size), disk, or more complicated structuring element.
```python
from skimage import filters
from skimage import data
text = data.text()
hsobel_text = filters.sobehl_h(text)
```

**Non-local filters**
- Non-local filters use a large region of the image (or all the image) to transform the value of one pixel
```python
from skimage import exposure
from skimage import data
camera = data.camera()
camera_equalized = exposure.equalize_hist(camera)
```

### Mathematical Morphology
- `from skimage import morphology`
- Erosion = minimum filter. Replace the value of a pixel by the minimal value covered by the structuring element.
- `np.zeros((7,7), dtype=np.uint8)`

* Mathematical Morphology seems to be the crucial aspect in image processing
- Grayscale mathematical morphology
	Mathematical morphology operations are also available for (non-binary) grayscale images (int or float type).Erosion and dilation correspond to minimum (resp. maximum) filters.
- Higher-level mathematical morphology are available: tophat, skeletonization, etc.
- Basic mathematical morphology is also implemented in `scipy.ndimage.morphology`. The `scipy.ndimage` implementation works on arbitrary-dimensional arrays
```python
from skimage.morphology import disk
filters.median(coins_zoom, disk(1))
#
from skimage import restoration
restoration.denoise_tv_chambolle(coins_zoom, weight=0.1)
#
filters.gaussian(coins, sigma=2)
```

### Image segmentation
* `skimage` provides several utility functions that can be used on label images (ie images where different discrete values identify different regions).
* Functions names are often self-explaining: `skimage.segmentation.clear_border() , skimage.segmentation.relabel_from_one() , skimage. morphology.remove_small_objects()`, etc.

**Binary segmentation: foreground + background**
* Histogram-based method: [Otsu thresholding](https://en.wikipedia.org/wiki/Otsu%27s_method)
- The Otsu method is a simple heuristic to find a threshold to separate the foreground from the background
```python
val = filters.threshold_otsu(camera)
#
import nummpy as np
from skimage import data, exposure, img_as_float
image = img_as_float(data.camera())
np.histogram(image,bins=2)
exposure.histogram(image, nbins=2)
```
- Once you have separated foreground objects, it is use to separate them from each other. For this, we can assign a different integer labels to each one.

**Watershed segmentation**
- Marker based methods
- If you have markers inside a set of regions, you can use these to segment the regions.
	- https://en.wikipedia.org/wiki/Watershed_(image_processing)
	* `skimage.morphology.watershed()`
	* The Watershed is a region-growing approach that fills “basins” in the image
	```python
	from skimage.morphology import watershed
	from skimage.feature import peak_local_max
	```

**Random Walker Segmentation**
- `skimage.segmentation.random_walker()`
- similar to the Watershed
- with a more “probabilistic” approach
- based on the idea of the diffusion of labels in the image

### Measuring regions’ properties
* compute the size and perimeter of the two segmented regions
* `from skimage import measure` and `scipy.ndimage.measurements`

### Data visualization and interaction
- Meaningful visualizations are useful when testing a given processing pipeline.
	* Visualize binary result
	* Visualize contour

### Feature extraction for computer vision
Geometric or textural descriptor can be extracted from images for:
* classify parts of the image (e.g. sky vs. buildings)
* match parts of different images (e.g. for object detection)
* many other applications in [Computer Vision](https://en.wikipedia.org/wiki/Computer_vision)

#### Corner_detection
	- https://en.wikipedia.org/wiki/Corner_detection
	- Corner detection is an approach used within computer vision systems to extract certain kinds of features and infer the contents of an image. Corner detection is frequently used in:
		* **motion detection**
		* **image registration**
		* **video tracking**
		* **image mosaicing**
		* **panorama stitching**
		* **3D modelling**
		* **object recognition**
	- Corner detection overlaps with the topic of [interest point detection](https://en.wikipedia.org/wiki/Interest_point_detection)
		* Interest point detection is a recent terminology in computer vision that refers to the detection of interest points for subsequent processing.		
	- In practice, however, most corner detectors are sensitive not specifically to corners, but to local image regions which have a high degree of variation in all directions.

**detecting corners using Harris detector**

```python
from skimage.transform import warp, AffineTransform
```
* `skimage.transform.wrap`
	- Warp an image according to a given coordinate transformation.
	- `wrap(image, inverse_map, map_args={}, output_shape=None, order=1, mode='constant', cval=0.0, clip=True, preserve_range=False)`
* `skimage.transform.AffineTransform`

http://scikit-image.org/docs/dev/auto_examples/features_detection/plot_matching.html
http://scikit-image.org/docs/dev/auto_examples/transform/plot_matching.html

## Concepts

### Edge detection
- Edges are caused by 'DISC' discontunity. D-Depth, I-Illumination, S-Surface Normal, C-color
- An edge is a place of rapid change in the image intensity function
- Identify sudden changes (discontinuities) in changes (discontinuities) in an image
- Image gradient, gradient direction
- Gradient points in the direction of most rapid increase in intensity
- edge strength is given by the gradient magnitude

* Concept of Limits is fundamental to understand
	* https://brilliant.org/wiki/limits-of-functions/
* Directional Derivative & Gradient
	* http://homepage.divms.uiowa.edu/~jsimon/COURSES/M028Spring07/HANDOUTS/DirectionalDerivative_v2.pdf
	* http://homepage.divms.uiowa.edu/~jsimon/COURSES/M028Spring07/HANDOUTS/
	* http://homepage.divms.uiowa.edu/~jsimon/COURSES/M028Spring07/M28Sp07CourseDescr.pdf
	* https://math.stackexchange.com/questions/2678655/the-gradient-as-a-limit-of-a-difference-quotient

Math Software	
* https://www.maplesoft.com/whatismaple.aspx
* http://www.sagemath.org/
* https://cocalc.com/help?session=default
* https://mathics.github.io/
* https://github.com/mathics/Mathics/wiki/Installing

Calculus II
https://qmplus.qmul.ac.uk/course/view.php?id=3107

uiowa jsimon calculas II


http://homepage.divms.uiowa.edu/~dstewart/classes/22m026/index.xhtml

http://www.sfu.ca/outlines.html?2015/spring/math/152/d100


 "software is only free if your time is worthless".
 a spokesperson from SAS once said, "You'd never fly in an airplane designed by open source software" to which Boeing responded "we use open source software to design our airplanes"

The advantage of free software is that it never dies; someone can always, if they want/need, pick it up and use/extend it

if you want to you could stick with the old versions, or make changes yourself, or pay someone to. These avenues just aren't open with closed source software.

Mathics is a general-purpose computer algebra system (CAS). It is meant to be a free, lightweight alternative to Mathematica.

All Raspberry Pi's have Mathematica licenses, so there's one cheap way in.

Symbolic manipulation. That's the only reason Mathematica is used in academia. If you're in the academia and want to do numeric computations you would use something like R or Matlab.



* Mathematica equivalents:
	- Sage
	- Mathics
	- symbolic computation: Rymbolic + sympy 
* Matlab equivalents
	- Octave
	- R
	- Pandas

https://github.com/mathics/IMathics
https://www.open.wolframcloud.com/



## Edge Detection
https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/
https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/segbench/


## Convolution
https://en.wikipedia.org/wiki/Convolution

In mathematics (and, in particular, functional analysis) convolution is a mathematical operation on two functions (f and g) to produce a third function, that is typically viewed as a modified version of one of the original functions, giving the integral of the pointwise multiplication of the two functions as a function of the amount that one of the original functions is translated

It has applications that include probability, statistics, computer vision, natural language processing, image and signal processing, engineering, and differential equations[

Visual comparison of convolution, cross-correlation and autocorrelation.

https://math.stackexchange.com/questions/255929/can-someone-intuitively-explain-what-the-convolution-integral-is

https://colah.github.io/posts/2014-07-Understanding-Convolutions/

## Courses
http://www.cs.cmu.edu/~ph/869/www/869.html
http://www.cs.cmu.edu/~ph/869/www/notes/notes.html
http://www.cs.cmu.edu/~seitz/course/3DPhoto.html

S. Seitz edge detections


https://esrimedia.maps.arcgis.com/apps/MapTour/index.html?appid=badd7a119a4143869c560a3e90ff3993
https://storymaps.arcgis.com/en/

https://www.geospatialworld.net/blogs/bim-vs-gis-or-bim-and-gis/

## Tutorials
http://corochann.com/basic-image-processing-tutorial-1220.html
