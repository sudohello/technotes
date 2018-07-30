/*
Title: Tools
Decription: Tools
Author: Bhaskar Mangal
Date: 11 Jul 2018
Last Updated: 11 Jul 2018
Tags: Tools
*/


## Video Editors
* https://filmora.wondershare.com/video-editor/free-linux-video-editor.html
* [shotcut](https://www.shotcutapp.com/download/)
* [openshot](https://www.openshot.org/)

## utilities
openssh-client,openssh-server,dos2unix,tree,chromium-browser,unrar
vim,vim-gtk
sublime-text-installer

## version control
git,cvs,tkcvs

## exif tool
libimage-exiftool-perl

## Used in openCV
doxygen,doxygen-gui,graphviz

## Pre-requisite for CUDA, cuDNN, tensorflow etc.
python-numpy,python-dev,python-pip,python-wheel

## Misc
libexif-dev,ntp,libconfig++-dev,kino
wine (ppa:ubuntu-wine/ppa)

## vncserver
ubuntu-desktop,gnome-panel,gnome-settings-daemon,metacity,nautilus,gnome-terminal,vnc4server

## VLC
vlc,browser-plugin-vlc

## java
default-jre,default-jdk,openjfx,ant

## graphics

inkscape (ppa:inkscape.dev/stable), gimp (ppa:otto-kesselgulasch/gimp), meshlab (ppa:zarquon42/meshlab)
Blender

### visual effects (VFX) industry from the perspective of being either an artist, compositor, video editor, or systems engineer.
#### Natron
https://natron.fr/download/?os=Linux&d=https://downloads.natron.fr/Linux/releases/64bit/files/Natron-2.2.7-Linux-x86_64bit.tgz

### Terrain Generation
* picogen, povray, yafray, wings3D

## sound
audacity (ppa:ubuntuhandbook1/audacity)

## php 7.0 (ppa:ondrej/php)
php7.0,php7.0-cli,php7.0-fpm,php7.0-gd,php7.0-json,php7.0-mysql,php7.0-readline,php7.0-xml,php7.0-mbstring

## apache2
apache2,libapache2-mod-php,php-mcrypt,php-mysql,libapache2-mod-php7.0

## Database, Filesystem
### Postgres
python-pip,python-dev,libpq-dev,postgresql,postgresql-contrib,pgadmin3

### Elastic Search
elasticsearch

## look & feel
compizconfig-settings-manager, compiz-plugins

# computer vision, datasciene, photogrammetry etc.
octave, ros
nodejs

# Screen Recorders
* https://askubuntu.com/questions/4428/how-to-record-my-screen
* https://www.unixmen.com/vokoscreen-a-new-screencasting-tool-for-linux/
vokoscreen (ppa:vokoscreen-dev/vokoscreen)

# Screen-capture/Screen-shots
* http://tipsonubuntu.com/2015/04/13/install-the-latest-shutter-screenshot-tool-in-ubuntu/
shutter (ppa:shutter/ppa)

# Youtube downloader
* https://www.lifewire.com/download-youtube-videos-p2-2202105
youtube-dl ytd-gtk

# Markdown editors
* https://www.maketecheasier.com/markdown-editors-linux/
* https://www.maketecheasier.com/best-markdown-editor-for-windows/

## Remarkable
* http://remarkableapp.github.io
* http://remarkableapp.github.io/files/remarkable_1.87_all.deb

sudo apt -y install python3-bs4 wkhtmltopdf
sudo dpkg -i remarkable_1.87_all.deb

## Haroopad (my fav)
* http://pad.haroopress.com/user.html

# Teamviewer
* https://askubuntu.com/questions/453157/how-to-install-teamviewer-on-14-04
* https://community.teamviewer.com/t5/Knowledge-Base/Installation-of-TeamViewer-on-a-Ubuntu-system/ta-p/45
* https://www.teamviewer.com/en/download/linux/

----------
## How To's
Installation of software on Ubuntu
Additing ppa repositories
Automating configuration settings
-Adding unique line in ~/.bashrc file using script - helpful for 
Nvidia Graphics card driver installation on Ubuntu
CUDA Installation (CUDA toolkit)
cuDNN, tensorflow setup
Troubleshoot errors during installaions etc.
How do I add a PPA in a shell script without user input?
https://askubuntu.com/questions/304178/how-do-i-add-a-ppa-in-a-shell-script-without-user-input
should-i-auto-remove-this-packages
https://askubuntu.com/questions/696431/should-i-auto-remove-this-packages

## References
### Comprehensive listing of Opensource softwares for all purposes:
* http://www.linuxrsp.ru/win-lin-soft/table-eng.html

### graphics
* https://en.wikipedia.org/wiki/Comparison_of_3D_computer_graphics_software
* https://en.wikibooks.org/wiki/Blender_3D:_Noob_to_Pro

### Terrain Generation
* https://en.wikibooks.org/wiki/Blender_3D:_Noob_to_Pro/Quickie_Texture
* https://en.wikipedia.org/wiki/Bump_mapping
* https://en.wikipedia.org/wiki/Heightmap
* https://en.wikipedia.org/wiki/Digital_elevation_model
* https://en.wikipedia.org/wiki/Terragen
* https://ubuntuforums.org/showthread.php?t=851846
* http://www.bottlenose.net/share/fracplanet/index.htm
* https://en.wikipedia.org/wiki/Picogen
* http://picogen.org/
* https://hubalternative.com/top-10-picogen-alternatives
* http://vterrain.org/Packages/Artificial/
#### povray
* http://www.povray.org/
* https://charmie11.wordpress.com/2016/01/29/pov-ray-3-7-installation-on-ubuntu-14-04/
#### wings3d
* http://www.wings3d.com/

### 2D-3D Floor Plans, Architecture
* https://en.wikipedia.org/wiki/Sweet_Home_3D
* https://sourceforge.net/projects/sweethome3d/files/SweetHome3D/stats/map


game@game-pc:~/Downloads$ sudo apt install libjpeg62
Reading package lists... Done
Building dependency tree       
Reading state information... Done
You might want to run 'apt-get -f install' to correct these:
The following packages have unmet dependencies:
 teamviewer:i386 : Depends: libjpeg62:i386 but it is not going to be installed
                   Depends: libxtst6:i386 but it is not going to be installed
E: Unmet dependencies. Try 'apt-get -f install' with no packages (or specify a solution).

teamviewer_12.0.76279_i386.deb
sudo dpkg --add-architecture i386;
sudo apt-get update; 
sudo dpkg -i teamviewer_12.0.76279_i386.deb
sudo apt-get -f install

## R, R-studio
* https://www.rstudio.com/products/rstudio/download-server/
* https://download2.rstudio.org/rstudio-server-1.0.143-amd64.deb
* https://www.digitalocean.com/community/tutorials/how-to-set-up-r-on-ubuntu-14-04
* https://cran.r-project.org
* https://cran.r-project.org/bin/linux/ubuntu/README

```r-base gdebi-core```

## Tutorials

https://www.r-bloggers.com/mini-ai-app-using-tensorflow-and-shiny/
https://www.analyticsvidhya.com/blog/2016/02/complete-tutorial-learn-data-science-scratch/


```
x <- c (1 ,3 ,2 ,5)
x
y = c (1 ,6 ,2, 2)
y
?c
length(x)
x+y
ls()
rm(x)
rm ( list = ls () ) #remove all objects at once
?matrix
y = matrix ( data = c (1 ,2 ,3 ,4) , nrow =2 , ncol =2)
x = matrix ( c (1 ,2 ,3 ,4) ,2 ,2)
matrix ( c (1 ,2 ,3 ,4) ,2 ,2) #matrix is printed to the screen but is not saved for future calculations.

A = matrix (1:16 ,4 ,4)
A
A[2,3] #[row,col]
dim(A)

x = rnorm (50) #creates standard normal random variables with a mean of 0 and a standard deviation of 1
y = x + rnorm (50 , mean =50 , sd =.1)
cor ( x , y )

set.seed(1303) #to reproduce the exact same set of random numbers
rnorm(50)

set.seed(3)
y=rnorm(100)
mean(y)
var(y)
sqrt(var(y))
sd(y)

#seq(a,b) makes a vector of integers between a and b
seq (1 ,10)
seq(0,1,length=10) #makes a sequence of 10 numbers that are equally spaced between 0 and 1
seq(-pi,pi,length=50)

plot(x,y) #produces a scatterplot of the numbers in x versus the numbers in y
plot (x ,y,xlab="this is the x - axis", ylab="this is the y - axis", main="Plot of X vs Y")


pdf("figure.pdf") #save to pdf
plot(x,y,col="green")
dev.off()

#contour plots
seq(-pi,pi,length=50)
y=x
f=outer(x,y,function(x,y) cos(y)/(1+ x^2))
contour(x,y,f)
contour(x,y,f,nlevels=45)

fa=(f-t(f))/2
contour(x,y,fa,nlevels=15)

#heatmap
image(x,y,fa)

#3D plot
persp(x,y,fa )

jpeg("figure.jpeg") #save to jpeg image
persp(x,y,fa,theta=30,phi=20)
dev.off()

```
matrix() - function can be used to create a matrix of numbers
dim()    - outputs the number of rows followed by the number of columns of a given matrix
sqrt()   - function returns the square root of each element of a vector or matrix
rnorm()  - function generates a vector of random normal variables, with first argument n the sample size
cor()    - function to compute the correlation between
mean()   - functions can be used to compute the mean of a vector of numbers
var()    - functions can be used to compute variance of a vector of numbers
sd()     - Applying sqrt() to the output of var() will give the standard deviation. Or we can simply use the sd() function
plot()   - function is the primary way to plot data in R; scatterplots of the quantitative variables
pdf()    - save to pdf file
jpeg()   - save to jpeg file
dev.off()- indicates to R that we are done creating the plot
seq()    - create a sequence of numbers
contour()- creates contour plots
image()  - function works the same way as contour() , except that it produces a color-coded plot whose colors depend on the z value (heatmap)
persp()  - produce a three-dimensional plot. The arguments theta and phi control the angles at which the plot is viewed.

* `?funcname`  will always cause R to open a new help file window with additional information about the function **funcname**
* CTRL + L - to clear commandline screen


### Loading Data
* http://www-bcf.usc.edu/~gareth/ISL/data.html

```
#text file

## R store it as an object called Auto, in a format referred to as a data frame.
Auto=read.table("~/Downloads/ISLR-dataset/Auto.data.txt",header=T,na.strings="?")
fix(Auto)
dim(Auto)

#csv
Auto=read.csv("~/Downloads/ISLR-dataset/Auto.csv",header=T,na.strings="?")

#remove rows with missing observations
Auto=na.omit(Auto)

names(Auto)
plot(Auto$mpg, Auto$cylinders)

attach(Auto)
plot(cylinders,mpg )

```
read.table()  - importing a data set into R
              - option header=T (or header=TRUE )
              - na.strings tells R that any time it sees a particular character or set of characters (such as a question mark), it should be    treated as a missing element of the data matrix

write.table() - to export data
fix()         - function can be used to view data in a spreadsheet like window
na.omit()     - function to simply remove rows contain missing observations
names()       - to check the variable names
as.factor()   - function converts quantitative variables into qualitative variables

- scatter plot
- bloxplot
* data frame

## Chat
* https://matrix.to/#/#qgis:matrix.org
* https://gitter.im/
* discord

## Misc
https://gis.stackexchange.com/questions/133090/map-box-gl-mature-appropriate-for-own-osm-tileserver
https://openmaptiles.org/docs/website/mapbox-gl-js/
https://gis.stackexchange.com/questions/125037/self-hosting-mapbox-vector-tiles
https://github.com/spatialdev/PGRestAPI
https://github.com/spatialdev/streetside-js

https://openmaptiles.org/
https://www.mapbox.com/maki-icons/

