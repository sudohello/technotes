---
Title: Ubuntu System Setup
Decription: Ubuntu System Setup
Author: Bhaskar Mangal
Date: 02 May 2018
Updated: 11 May 2018
Tags: Ubuntu System Setup
---

**Table of Contents**
* TOC
{:toc}


## System Setup
**Assembling decent system for Multi purpose:**
* Computer Vision and Image Processing
* Machine Learning
* Deep Learning
* 3D GIS - Photogrammetry, Point Cloud, LiDAR, 3D Modelling
* Data Analysis, Data Visualization
* VR,AR
* VFX

## Hardware/PC configuration
* [System Configuration Research - What & Why](hardwares-configs.md)

## OS Installation and setting up directories
* Replace `<primaryUserName>` with your username
* **TBD:** this setup needs to evolve for sharing same programme resources with other users in the server or shared environment
* **Install git, gparted, vim-gtk and sublime editor**
```bash
sudo -E apt-get update
## Essential for New Machine Setup
sudo -E apt-get -q -y install git
sudo -E apt-get -q -y install gparted
sudo -E apt-get -q -y install vim-gtk
#
# install sublime (optional)
#./sublimetexteditor.install.sh
```

* **partition using gparted**

* **creating data directories, mount points**
```bash
#
# get UUID of datadrive disk/partition
#
sudo blkid
ls -l /dev/disk/by-uuid/
#
# make an entry in the file and mount the partition
#
UUID=98083c67-4779-4603-85ac-fd5bb2f6ef37       /media/<primaryUserName>/datadrive                  ext4    rw,auto,nofail,nodev,nosuid     0       2
#
# mount the disk/partition
#
sudo mount -a
cd /media/<primaryUserName>/datadrive/<primaryUserName>
#
# Move the data folders to the data partitions
#
rsync -aXS $HOME/Documents .
rsync -aXS $HOME/Downloads .
rsync -aXS $HOME/Music .
rsync -aXS $HOME/Pictures .
rsync -aXS $HOME/Videos .
rsync -aXS $HOME/softwares .
cd
sudo umount -a
#
# Create the mount points under /mnt
# creating the mounts under /media would come as a data drive in the file manager, hence avoid it
#
sudo vi /etc/fstab
```
* Sample working fstab entry
```
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/sda1 during installation
UUID=e2d95887-9a55-4f96-8064-0d7dc5aaa3c9 /               ext4    errors=remount-ro 0       1
# swap was on /dev/sda5 during installation
UUID=33852ea4-4036-4c2f-b1cb-6ccaac3500f9 none            swap    sw              0       0
#
UUID=98083c67-4779-4603-85ac-fd5bb2f6ef37       /mnt/datadrive                  ext4    rw,auto,nofail,nodev,nosuid     0       2
/mnt/datadrive/<primaryUserName>/Documents                 /home/<primaryUserName>/Documents          none    bind                            0       0
/mnt/datadrive/<primaryUserName>/Downloads                 /home/<primaryUserName>/Downloads          none    bind                            0       0
/mnt/datadrive/<primaryUserName>/Pictures                  /home/<primaryUserName>/Pictures           none    bind                            0       0
/mnt/datadrive/<primaryUserName>/Music                     /home/<primaryUserName>/Music              none    bind                            0       0
/mnt/datadrive/<primaryUserName>/Videos                    /home/<primaryUserName>/Videos             none    bind                            0       0
/mnt/datadrive/<primaryUserName>/softwares                 /home/<primaryUserName>/softwares          none    bind                            0       0
```

## Software Stack setup begins
* [Refer Linuxscripts repo README for Software Setup - what, why, how and sequences for maximum feature set](https://github.com/mangalbhaskar/linuxscripts)
