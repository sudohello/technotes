/*
Title: Linux Administration, Tools setup
Decription: nitty gritty of Linux
Author: Bhaskar Mangal
Date: 20 Jan 2017
Tags: Linux, Administration, Tools, Softwares
*/

# Software & Tools Setup Help

## Linux Administration

### Network Analysis
**how-do-i-get-ip-of-installed-network-printer**
* https://askubuntu.com/questions/643584/how-do-i-get-ip-of-installed-network-printer
* http://manpages.ubuntu.com/manpages/zesty/en/man1/arp-scan.1.html
* https://stackoverflow.com/questions/13669585/how-to-get-a-list-of-all-valid-ip-addresses-in-a-local-network

```bash
//finding printer
lpoptions  -p <printer_name> | awk '{for (i=1; i<=NF; i++) {if ($i ~ /device-uri/) {print $i}}}'
//example
lpoptions  -p TOSHIBA_e-STUDIO2330C | awk '{for (i=1; i<=NF; i++) {if ($i ~ /device-uri/) {print $i}}}' device-uri=socket://192.168.20.43
lpoptions  -p HL2240D | awk '{for (i=1; i<=NF; i++) {if ($i ~ /device-uri/) {print $i}}}' device-uri=socket://10.4.71.140
//To get an overview lpinfo
lpinfo -v | grep -P '://'
//
netstat -r
//nmap, arp-scan
sudo apt-get install arp-scan
sudo arp-scan --interface=eth0 --localnet
sudo arp-scan --interface=enp9s0 --localnet
//Where eth0 is your device (or wlan0). You can find your device with:
ifconfig
//
sudo apt-get install nmap
nmap -sT <adress_or_address_range>
nmap -sT 10.4.71.*
nmap -sP 10.4.71.*
//
lspci -knn
lsusb
//
cat /etc/lsb-release; uname -a
lspci -nnk | grep -iA2 net
lsusb
iwconfig
rfkill list all
lsmod

```
HL 2240D - Brother
* https://ubuntuforums.org/showthread.php?t=1627516
* http://support.brother.com/g/b/downloadtop.aspx?c=in&lang=en&prod=hl2240d_all
* http://support.brother.com/g/b/downloadhowto.aspx?c=in&lang=en&prod=hl2240d_all&os=128&dlid=dlf006893_000&flang=4&type3=625
* https://askubuntu.com/questions/787950/setting-up-brother-hl-2240-printer
* http://daeken.com/hacking-the-belkin-network-usb-hub
* https://www.ifixit.com/Teardown/Belkin+F5L009+Network+USB+Hub+Teardown/10455
* https://github.com/daeken/pybelkusb/blob/master/blog.md

r8712u

install-printer-connected-to-belkin-router-usb-port

https://ubuntuforums.org/showthread.php?t=1947015

network usb hub f5l009 v2 driver ubuntu 16.04


### Ethernet related debugging

```
ifconfig -a
lshw -C network
lspci -nn | grep Ethernet
dmesg | grep eth0
cat /etc/network/interfaces
ip link
nmcli d
nmcli networking connectivity
nmcli networking off
nmcli networking on

systemctl status netowrking.service
journalctl -xe

service network-manager restart

logical name: enp9s0


SUBSYSTEM=="net", ACTION=="add", ATTR{address}=="xx:xx:xx:xx:xx:xx", NAME="eth0"
```

### Software management on Ubuntu
**References**
* http://unix.stackexchange.com/questions/159094/how-to-install-a-deb-file-by-dpkg-i-or-by-apt
* https://wiki.debian.org/ListInstalledPackages

#### Commands
* apt-get
* dpkg
```
sudo dpkg -i /path/to/deb/file followed by sudo apt-get install -f.
```

* dpkg-query
	* List all installed packages
```
dpkg-query -l
```
___

* Cache
	- /var/cache/apt/archives/
	- move your deb file to  directory
* Repository
	- APT maintains the package index which is a database of available packages available in repo defined in /etc/apt/sources.list file and in the /etc/apt/sources.list.d directory.

## Software Development Tools

### API Development
* [Postman](https://www.getpostman.com/)

## Linux (Ubuntu) Toolchain Setup
### scp, sftp, ssh, rsync
* http://askubuntu.com/questions/94665/what-is-a-program-similar-to-winscp

### LDAP

## ROS - Installation
**References**
* http://wiki.ros.org/indigo/Installation/Ubuntu
* http://answers.ros.org/question/188732/e-unable-to-locate-package-ros-indigo-desktop-full/
* http://wiki.ros.org/kinetic/Installation/Ubuntu

* **Setup your sources.list**

```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

* **Set up your keys**

```
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
```

* **Installation**
	- Desktop-Full Install: (Recommended) : ROS, rqt, rviz, robot-generic libraries, 2D/3D simulators, navigation and 2D/3D perception

```
sudo apt-get update
sudo apt-get install ros-kinetic-desktop-full
```

* **Initialize rosdep**
	- Before you can use ROS, you will need to initialize rosdep. rosdep enables you to easily install system dependencies for source you want to compile and is required to run some core components in ROS.

```
sudo rosdep init
rosdep update
```

* **Environment setup**

```
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

* **Getting rosinstall**
	- rosinstall is a frequently used command-line tool in ROS that is distributed separately. It enables you to easily download many source trees for ROS packages with one command.

```
sudo apt-get install python-rosinstall
```

### ROS Commands
* List packages
	> rospack list-names

* Install packages
	> sudo apt-get install ros-"your ros distro"-"package-name"
	> sudo apt-get install ros-kinetic-image-view
	> sudo apt-get install ros-kinetic-stereo-image-proc

* Install package dependencies - rosdep is a tool you can use to install system dependencies required by ROS packages.
	> rosdep install [package]

**Using ROS**

* roscore is the first thing you should run when using ROS.
	> roscore

* rosnode displays information about the ROS nodes that are currently running. The rosnode list command lists these active nodes:
	> rosnode list

* The rosnode info command returns information about a specific node:-
	> rosnode info /rosout

* List service.
	> rosservice list
* Show service description.
	> rosservice type spawn | rossrv show
* Create a new turtle by creating a service.
	> rosservice call spawn 2 2 0.2 ""
* ROS parameter list.
	> rosparam list
* Set and get background colors using rosparam
	> rosparam set background_r 150
	> rosparam get background_g
* Display parameters
	> rosparam get /
* Save parameters
	> rosparam dump params.yaml
* Load parameters into new namespace copy
	> rosparam load params.yaml copy
	> rosparam get copy/background_b

#### PCL in ROS
**References**
* http://www.pointclouds.org/documentation/tutorials/

#### Rviz in Stereo

**References**
* http://wiki.ros.org/stereo_image_proc
* http://wiki.ros.org/image_view#stereo_view
* http://docs.ros.org/api/sensor_msgs/html/index-msg.html
* [Install packages in ROS](http://answers.ros.org/question/196766/how-to-install-packages-under-ros/)
* [ROS Package lists](http://www.ros.org/browse/list.php?package_type=package&distro=groovy)
* http://wiki.ros.org/FAQ
* http://wiki.ros.org/ROS/Tutorials/rosdep

* Install rviz
	> rosdep install rviz


##### Required Image processing Packages

* stereo_image_proc
	> Stereo and single image rectification and disparity processing. This package contains the stereo_image_proc node, which sits between the stereo camera drivers and vision processing nodes.
* stereo_msgs
	> stereo_msgs contains messages specific to stereo processing, such as disparity images.
* stereo_synchronizer
	> stereo_synchronizer
* stereo_wall_detection
	> Detects planar structures (e.g., walls) from stereo cameras point clouds (usually generated usi
* camera1394
	> IEEE 1394 Digital Camera driver
* camera1394stereo
	> This is a modified version of the ROS driver for devices supporting the IEEE 1394 Digital Camer
* camera_application
	> Camera Application
* camera_calibration
	> camera_calibration allows easy calibration of monocular or stereo cameras using a checkerboard
* camera_calibration_parsers
	> camera_calibration_parsers contains routines for reading and writing camera calibration parameters.
* camera_calibration_standalone
	> Simple tools for stereo camera calibration (to be deprecated by dcam/ost from ros-pkg).
* camera_info_manager
	> This package provides a C++ interface for camera calibration information. It provides CameraIn.
* camera_info_manager_py
	> Python interface for camera calibration information. This ROS package provides a CameraInfo int...
* camera_pose_calibration
	> camera_pose_calibration
* camera_pose_toolkits
	> camera_pose_toolkits
* camera_self_filter
* image_view
	> A simple viewer for ROS image topics. Includes a specialized viewer for stereo + disparity images....
* image_view2
	> A simple viewer for ROS image topics with draw-on features

### Octave
Installation (opensource alternative to MatLab)

**References**
* http://wiki.octave.org/Octave_for_Debian_systems

```
sudo apt-get install octave
```
## OpenCV
Compilation and Installation (opensource Computer Vision Lib)

### References
* http://answers.opencv.org/question/60804/how-to-build-docs-for-opencv-300-rc1/
* http://askubuntu.com/questions/771601/problem-with-cmake
* http://www.linuxfromscratch.org/blfs/view/cvs/general/opencv.html
* http://stackoverflow.com/questions/17386551/how-to-build-opencv-with-java-under-linux-using-command-linegonna-use-it-in-ma

### Required packages

```
sudo apt-get install --assume-yes build-essential cmake git
sudo apt-get install --assume-yes build-essential pkg-config unzip ffmpeg qtbase5-dev python-dev python3-dev python-numpy python3-numpy
sudo apt-get install --assume-yes libopencv-dev libgtk-3-dev libdc1394-22 libdc1394-22-dev libjpeg-dev libpng12-dev libtiff5-dev libjasper-dev
sudo apt-get install --assume-yes libavcodec-dev libavformat-dev libswscale-dev libxine2-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev
sudo apt-get install --assume-yes libv4l-dev libtbb-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev
sudo apt-get install --assume-yes libvorbis-dev libxvidcore-dev v4l-utils

sudo apt-get install --assume-yes ffmpeg python3-dev python3-numpy
sudo apt-get install --assume-yes libopencv-dev libgtk-3-dev libdc1394-22-dev
sudo apt-get install --assume-yes libxine2-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev
sudo apt-get install --assume-yes libv4l-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev
sudo apt-get install --assume-yes libvorbis-dev libxvidcore-dev v4l-utils
```
### Find number of cores in Linux
[how-to-know-number-of-cores-of-a-system-in-linux](http://unix.stackexchange.com/questions/218074/how-to-know-number-of-cores-of-a-system-in-linux)
```
cat /proc/cpuinfo | grep "cpu cores"
```

* http://www.tutorialspoint.com/articles/how-to-install-doxygen-on-ubuntu
* http://stackoverflow.com/questions/16963579/generate-graphs-and-diagrams-with-doxygen
* http://askubuntu.com/questions/315646/update-java-alternatives-vs-update-alternatives-config-java

### Updating libpng
Updating to libpng 1.6.28
* http://www.linuxfromscratch.org/blfs/view/7.6/general/libpng.html
* http://stackoverflow.com/questions/33634402/how-to-check-libpng-version

```
readelf -d  libpng.so |grep SONAME
identify -list format | grep PNG
```

### Configure Java using Alternatives
* http://askubuntu.com/questions/315646/update-java-alternatives-vs-update-alternatives-config-java

```
update-java-alternatives -l
update-alternatives --config java
```

### Install JNI

```
ls $JAVA_HOME/include/jni.h
```

- FindJNI. Since the "FindJNI" module of cmake 3 doesn't support the detection of Oracle Java 8, we have to add our Java 8 directories manually. Therefore, locate the file FindJNI.cmake in your cmake directory,e.g /home/foo/bar/cmake-3.2.2-Linux-x86_64/share/cmake-3.2/Modules/FindJNI.cmake
- Goto the JAVA_APPEND_LIBRARY_DIRECTORIES variable and add the path to your java lib architecture directory, e.g. /home/foo/bar/jdk1.8.0_45/lib/amd64
- Goto the JAVA_AWT_INCLUDE_DIRECTORIES variable and add the path to your java include directory, e.g. /home/foo/bar/jdk1.8.0_45/include

### Compile and Build OpenCV

```
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D WITH_V4L=ON -D WITH_QT=ON -D WITH_OPENGL=ON -D WITH_CUBLAS=ON -DCUDA_NVCC_FLAGS="-D_FORCE_INLINES"
```

Note: check how many cpu core you have or use default for using single core
```
make -j $(($(nproc) + 1))
make -j 2 // number of cores of CPU, do not run on all the cores, it will hang and will not compile
make -j //takes default cores as 1, use this
```
#### Stack Trace after running make, find out what is not avaiable and try to install based on requirements

```
curretly have gstreamer 0.10.36
gstreamer-base-1.0 gstreamer-video-1.0 gstreamer-app-1.0 gstreamer-riff-1.0 gstreamer-pbutils-1.0

libavresample
libgphoto2
ippicv_linux_20151201.tgz
OpwnBLAS lib
Atlas
Doxygen

JNI
Matlab

/usr/lib/x86_64-linux-gnu/libvtkRenderingPythonTkWidgets.so
/usr/lib/vtk

Unavailable ( if graphics card with cuda enabled, following needs to be installed)
cudaarithm cudabgsegm cudacodec cudafeatures2d cudafilters cudaimgproc cudalegacy cudaobjdetect cudaoptflow cudastereo cudawarping cudev java

Media I/O
GDAL No
GDCM No
Video I/O
FFMPEG
avresample No
Microsoft Kinect libs - OpenNI "OpenNI PrimeSensor Modules" OpenNI2
PvAPI
GigEVisionSDK
Aravis SDK
UniCap
UniCal ucil
V4L/V4L2
XIMEA
Xine
gphoto2
```

**Install missing components**
```
sudo apt-get install --assume-yes doxygen
sudo apt-get install --assume-yes graphviz
sudo apt-get install --assume-yes doxygen-gui
```
You can run doxygen-gui using:
```
doxywizard
```



## CVS Setup

* set the following in .bashrc file (under the home dir)

```
export CVSROOT=":pserver:<username>@<IP>:<port>/<path>/CVS_REPO"
alias cvstt='cvs status 2>/dev/null | grep ^File | grep -v Up-to'
cvs login
```

## Apache2 Installation

Refer: [apache guide](apache.html)

## Exports & Aliases

Use as per requirements

* In .bashrc file (under home dir), read more on bashrc

```
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64
export PATH=/usr/lib/jvm/java-1.8.0-openjdk-amd64/bin:$PATH
export TOMCAT_HOME=/usr/share/tomcat5
export LD_LIBRARY_PATH=/usr/local/lib
export MALLOC_CHECK_=0

export LD_LIBRARY_PATH=/usr/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/lib/libflycapture-c.so:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/lib/libflycapture.so:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/home/gaze/Documents/vidteq/software/gazeRecord/myDll:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/home/gaze/Documents/flyCapture:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/home/gaze/Downloads/gps/lib:$LD_LIBRARY_PATH

export LD_LIBRARY_PATH=/usr/lib/jvm/java-1.8.0-openjdk-amd64/jre/lib/amd64/server:$LD_LIBRARY_PATH

alias huawai="echo gaze | sudo -kS touch /etc/usb_modeswitch.d/12d1:1f01; echo gaze | sudo -kS usb_modeswitch -J -v 0x12d1 -p 0x1f01;"
alias vpn="echo gaze | sudo -kS openvpn --config ~/Downloads/fw-udp-1194-gaze-config.ovpn;"
alias gazerecord="cd /home/gaze-in/Documents/vidteq/software/gazeRecord"
alias gazehtml="cd /home/gaze-in/Documents/vidteq/software/gazeRecord/www"
alias gazecpp="cd /home/gaze-in/Documents/vidteq/software/gazeRecord/service"
alias gaze="cd /home/gaze-in/Documents/vidteq/software/gazeRecord/service/bin; echo gaze | sudo -kS ./gaze"
```



* **Mount samba as dir**
sudo apt install nfs-common 
sudo apt install smb4k 
sudo mount -t cifs //<IP>/samba5 /mnt/samba121 -o username=<username>,workgroup=<workgroup-name>

* **message to linux to linux user**
* https://unix.stackexchange.com/questions/99460/sending-messages-to-another-user

talk —
mesg — Control if (non-root) users can send messages to your terminal.
wall — Send a message to all logged-in users.
who — Report which users are logged in to the system.
write — Send a message to another user.

* https://askubuntu.com/questions/61995/chat-over-lan-from-linux-to-linux
netcat / nc

On PC 1, type: nc -l 55555

On PC 2, type: nc $IP 55555, where $IP equals the local IP address of PC 1 [e.x. 192.168.2.50]

* **Enable Remote Desktop Connection on Ubuntu**
* https://askubuntu.com/questions/4474/enable-remote-vnc-from-the-commandline
```bash
gconftool-2 --set --type=bool /desktop/gnome/remote_access/enabled true
gconftool-2 -a /desktop/gnome/remote_access
gsettings list-keys org.gnome.Vino
```
/usr/lib/vino/vino-server

* What is **/dev/null**?
* What is the purpose of outputting to /dev/null like that, and what does the 2>&1 mean?
```
some command > /dev/null 2>&1
# So, the STDOUT is redirected to the bit-bucket(trash) and the STDERR is redirected to where the STDOUT is located: the bit-bucket.
```
* https://askubuntu.com/questions/12098/what-does-outputting-to-dev-null-accomplish-in-bash-scripts

  - `>/dev/null` redirects the command standard output to the null device, which is a special device which discards the information written to it
  - `2 >&1` redirects the standard error stream to the standard output stream (stderr = 2, stdout = 1).

In practice it prevents any output from the command (both stdout and stderr) from being displayed. It's used when you don't care about the command output.

STDIN is represented by 0, STDOUT by 1, and STDERR by 2.


/dev/null is the bit-bucket: the place where you dump anything you don't need.


## Disk Space Monitoring
https://askubuntu.com/questions/413358/disk-is-full-but-cannot-find-big-files-or-folders
```
sudo du -sch /root/*
du -sch .[!.]* * |sort -h

#https://askubuntu.com/questions/36111/whats-a-command-line-way-to-find-large-files-directories-to-remove-and-free-up
find / -size +10M -size -12M -ls
#
sudo du -sx /* 2>/dev/null | sort -n
#
sudo du -aBM 2>/dev/null | sort -nr | head -n 10
```


## Creating a bootable Ubuntu USB
- http://cyberciti.biz

```bash
df
sudo umount /dev/sdb1
sudo dd if=ubuntu-16.04.3-desktop-amd64.iso of=/dev/sdb bs=1M status=progress
```
You can also do

    sudo -s
and you don't have to put "sudo" in front of everything!


# Mounting
```bash
#FAT
sudo mount -t vfat -o rw,noauto,async,user,umask=1000 /dev/sdb1 /media/tmp/
mount -l -t vfat,fat,msdos
```

## install-chdk-on-your-canon-camera-using-linux




https://scribblesandsnaps.com/2010/11/16/install-chdk-on-your-canon-camera-using-linux/
https://askubuntu.com/questions/458743/cannot-format-my-sd-card
```bash
# Format with Fat16
sudo mkfs.vfat -F16 /dev/sdb1
#
echo -n BOOTDISK | sudo dd bs=1 count=8 seek=64 of=/dev/sdbx
#Replace the sdbx part with the actual name of the small FAT16 partition
```

dd bs=1 count=72 seek=0 conv=notrunc if=/dev/

sudo mount -t vfat -o rw,noauto,async,user,umask=1000 /dev/sdb1 /mnt/tmp

df | grep -e \"/$\" | sed s/[s/]/\\ /g | awk '{print $2\" \"$3 }' | sed s/\\ /s/g

printf \"BOOTDISK\" | dd bs=1 count=8 seek=0x40 conv=notrunc of=/dev/disk"

diskutil list


## Tools
* **Bulk Rename**
http://www.webupd8.org/2016/03/quickly-batch-rename-files-in-linux.html
```bash
sudo add-apt-repository ppa:nilarimogard/webupd8
sudo apt-get update
sudo apt-get install metamorphose2
```
* *Flatten Directory Structure**
https://superuser.com/questions/91307/copying-only-jpg-from-a-directory-structure-to-another-location-linux
https://ubuntuforums.org/showthread.php?t=1385966

find . -type f \( -iname "*.jpg" -o -iname "*.jpeg" \) -exec cp '{}' /cpjpg \;

find ./ -name '*.jpg' -exec cp '{}' ./ \;

sudo apt-get install feh
feh -Fzr -D 5 ~/Images

https://www.lifewire.com/feh-command-line-image-viewer-4054068

* **Merge and Split PDF documents**
	- https://linuxcommando.blogspot.in/2013/02/splitting-up-is-easy-for-pdf-file.html
	- https://linuxcommando.blogspot.in/2014/01/how-to-split-up-pdf-files-part-2.html
	- https://linuxcommando.blogspot.in/2015/03/how-to-merge-or-split-pdf-files-using.html
```bash
#Merging 2 pdf files (file1 and file2) into a new file (output) is as simple as executing:
convert file1.pdf file2.pdf output.pdf
#You can merge a subset of pages instead of the entire input files. Note that page numbers are zero-based
convert file1.pdf[0] file2.pdf[0-1,3] output.pdf
# splits up input into 2 files:
convert input.pdf[0-1] first2output.pdf 
convert input.pdf[2-3] next2output.pdf
#
# https://imagemagick.org/discourse-server/viewtopic.php?t=8707
#
convert -density 300 RentalAgreement-2016-17.jpg RentalAgreement-2016-17.pdf
```

* **Remove password from PDF**
https://askubuntu.com/questions/828720/how-to-remove-the-password-from-a-pdf
```bash
sudo apt get install pdftk
pdftk /path/to/input.pdf input_pw <yourpassword> output out.pdf
```

* **PDF Editors**
http://www.linuxandubuntu.com/home/5-best-linux-pdf-editors

## Audio

### USB Soundcard
https://blog.ostermiller.org/ubuntu-usb-audio/


## Data Streaming
https://code.tutsplus.com/tutorials/building-with-the-twitter-api-using-real-time-streams--cms-22194
https://kraken-php.com/

https://www.reddit.com/r/PHP/comments/573fuh/kraken_distributed_async_php_framework/
https://github.com/reactphp



## Wifi troubleshooting
sudo lshw -C network
lspci -nnk | grep 0280 -A2

07:00.0 Network controller [0280]: Broadcom Corporation BCM43142 802.11b/g/n [14e4:4365] (rev 01)
	Subsystem: Dell Wireless 1704 802.11n + BT 4.0 [1028:0016]
	Kernel modules: bcma, wl

sudo modprobe wl && dmesg | grep wl
modprobe: ERROR: could not insert 'wl': Exec format error


sudo apt-get purge bcmwl-kernel-source
sudo apt-get update
sudo apt-get install bcmwl-kernel-source


==========
https://askubuntu.com/questions/139157/booting-ubuntu-with-acpi-off-grub-parameter?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
https://wiki.ubuntu.com/DebuggingACPI
 acpi=off 

UEFI: Unified-Extensible-Firmware-Interface
 http://whatis.techtarget.com/definition/Unified-Extensible-Firmware-Interface-UEFI

Unified Extensible Firmware Interface (UEFI)

Unified Extensible Firmware Interface (UEFI) is a specification for a software program that connects a computer's firmware to its operating system (OS). UEFI is expected to eventually replace BIOS.

https://www.howtogeek.com/56958/htg-explains-how-uefi-will-replace-the-bios/


**SSDs**
/dev/nvme stands for SSDs


Make the change permanent:
In Ubuntu, open terminal from the dash or press Ctrl+Alt+T, execute this to edit grub: gksudo gedit /etc/default/grub.
Find the line starting with GRUB_CMDLINE_LINUX_DEFAULT and append acpi=off to its end, make it look like: GRUB_CMDLINE_LINUX_DEFAULT="quiet splash acpi=off"

## wget
https://stackoverflow.com/questions/1078524/how-to-specify-the-location-with-wget

-O is the option to specify the path of the file you want to download to.

wget <file.ext> -O /path/to/folder/file.ext
-P is prefix where it will download the file in the directory

wget <file.ext> -P /path/to/folder

## compress, uncompress
https://stackoverflow.com/questions/18402395/how-to-uncompress-a-tar-gz-in-another-directory

tar -xzf bar.tar.gz -C foo


**Check installed library version**
https://askubuntu.com/questions/434154/how-to-get-the-list-of-installed-library-packages-only
/sbin/ldconfig -p
The -v option will show the libraries version.

**/usr/bin/ld: final link failed: No space left on device**
http://www.ubuntu-forum.de/artikel/61799/final-link-failed-no-space-left-on-device.html

<!-- /usr/bin/ld: final link failed: No space left on device
collect2: error: ld returned 1 exit status
features/CMakeFiles/pcl_features.dir/build.make:1107: recipe for target 'lib/libpcl_features.so.1.8.1.99' failed
make[2]: *** [lib/libpcl_features.so.1.8.1.99] Error 1
CMakeFiles/Makefile2:1438: recipe for target 'features/CMakeFiles/pcl_features.dir/all' failed
make[1]: *** [features/CMakeFiles/pcl_features.dir/all] Error 2
Makefile:160: recipe for target 'all' failed
make: *** [all] Error 2 -->


df -i 
free -m
grep tmpfs /etc/fstab
mount |grep \/tmp


# Directory Space
du -h --max-depth=1 | sort -hr