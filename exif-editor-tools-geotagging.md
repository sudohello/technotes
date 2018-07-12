/*
Title: Geo-Tagging Images & Geo Tags
Description: How to geo-tag images (post-processing)
Author: Bhaskar Mangal
Date: 28 Mar 2017
Placing: 1
Tags: Geo Tagging, ExifTool, Exif Tag
*/

## Geo-Tagging Images

### Setup of Exif Tools
1. Download ExifTool, ExifToolGUI
    [ExifTool](http://www.sno.phy.queensu.ca/~phil/exiftool/)
    [ExifToolGUI](http:\\u88.n24.queensu.ca\exiftool\forum\index.php\topic,2750.0.html)
2. Install ExifTool & ExifToolGUI
    - Unzip ExifTool archive
    - Unzip ExifTool GUI archive into the same directory (Doesn't matter if it's in Windows directory)
    - Move jhead.exe and jpegtran.exe out of their folder and into the same directory as the other two.
    - Rename ExifTool(-k).exe to ExifTool.exe
* Reference: ["exiftool not found" for ExifToolGUI](http:\\u88.n24.queensu.ca\exiftool\forum\index.php?topic=3336.0)


### GeoTags - Geotagging with ExifTool
The ExifTool geotagging feature adds GPS tags to images based on data from a GPS track log file. The GPS track log file is loaded, and linear interpolation is used to determine the GPS position at the time of the image, then the following tags are written to the image (if the corresponding information is available):

GPSLatitude      GPSLongitude      GPSAltitude          GPSDateStamp
GPSLatitudeRef   GPSLongitudeRef   GPSAltitudeRef       GPSTimeStamp
GPSTrack         GPSSpeed          GPSImgDirection      GPSPitch        
GPSTrackRef      GPSSpeedRef       GPSImgDirectionRef   GPSRoll
*Note: GPSPitch and GPSRoll are not standard tags, and must be user-defined.


* Reference:
    * [Geo Tags](http:\\www.sno.phy.queensu.ca\~phil\exiftool\geotag.html)
    * [GPS Tags](http:\\www.sno.phy.queensu.ca\~phil\exiftool\TagNames\GPS.html)

### [Geotag Images With Location Data in a csv file](http://photo.stackexchange.com/questions/61490/how-can-i-geotag-images-with-location-data-in-a-csv-file)

```ExifTool -csv="\path\to\csvfile.csv" \directory\path\```

**Example:**

```ExifTool -csv="C:\Users\Admin\Desktop\bhaskar\geotag-35-85.csv" "C:\Users\Admin\Desktop\6cam test\13\49\04"```


```ExifTool "-GPS:all<XMP-exif:all" "-GPS:GPSLongitudeRef<Composite:GPSLongitudeRef" "-GPS:GPSLatitudeRef<Composite:GPSLatitudeRef" "-GPS:GPSAltitudeRef<Composite:GPSAltitudeRef" "C:\Users\Admin\Desktop\6cam test\13\49\04\"```
