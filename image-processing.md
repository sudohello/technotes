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

**OPTICAL vs. DIGITAL ZOOM**
- A camera performs an optical zoom by moving the zoom lens so that it increases the magnification of light before it even reaches the digital sensor.
- In contrast, a digital zoom degrades quality by simply interpolating the image — after it has been acquired at the sensor.
- Digital zoom should be almost entirely avoided, unless it helps to visualize a distant object on your camera's LCD preview screen

**Tools**
* de-noising
	- https://ni.neatvideo.com/download
	- https://www.picturecode.com/download.php

## Image Processing in Python

- OpenSource Computer Vision, more commonly known as OpenCV, is a more advanced image manipulation and processing software than PIL, Pillow
- In Python, image processing using OpenCV is implemented using the `cv2` and `NumPy` modules
- [Image Processing using Pillow](https://pillow.readthedocs.io/en/3.0.x/handbook/tutorial.html)
- [Image Processing using OpenCV](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)
- ScipyLectures-simple.pdf

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
```python
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
