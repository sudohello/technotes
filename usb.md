---
Title: Linux Troubleshooting
Decription: Linux Troubleshooting
Author: Bhaskar Mangal
Date: 
Tags: Linux Troubleshooting, Ubuntu, DataCard/USB
---

**Table of Contents**
* TOC
{:toc}


## Linux Troubleshooting

## USB / Datacard (Huawei) Setup

```bash
lsusb
#
sudo touch /etc/usb_modeswitch.d/12d1:1f01
sudo -kS usb_modeswitch -J -v 0x12d1 -p 0x1f01
```

https://github.com/vidteq/Gaze/blob/master/Install%20Manual/readme_ubuntu_16.04.txt

#--- sudo open <editor> /etc/modules

raw1394

#--- sudo open <editor> /lib/udev/rules.d/40-usb_modeswitch.rules
#this is optional if dongle doesn't work
ATTR{idVendor}=="12d1", ATTR{idProduct}=="15ca", RUN+="usb_modeswitch '%b/%k'"

ATTR{idVendor}=="12d1", ATTR{idProduct}=="1f01", RUN+="usb_modeswitch '%b/%k'"


sudo apt-get install libcanberra-gtk-module:i386
sudo apt-get install gtk2-engines-murrine:i386 unity-gtk2-module:i386
sudo apt-get install --reinstall gtk2-engines-murrine:i386


apt-get install libatk-adaptor libgail-common

Gtk-Message: Failed to load module "overlay-scrollbar"
Gtk-Message: Failed to load module "gail"
Gtk-Message: Failed to load module "atk-bridge"
Gtk-Message: Failed to load module "unity-gtk-module"

overlay-scrollbar-gtk2:amd64 overlay-scrollbar-gtk3:amd64

GLib-GIO-Message: Using the 'memory' GSettings backend.  Your settings will not be saved or shared with other applications

export GIO_EXTRA_MODULES=/usr/lib/x86_64-linux-gnu/gio/modules/


https://askubuntu.com/questions/558446/my-dconf-gsettings-installation-is-broken-how-can-i-fix-it-without-ubuntu-reins
ldd /usr/lib/x86_64-linux-gnu/gio/modules/libdconfsettings.so

sudo mv /etc/ld.so.conf.d/libc.conf /etc/ld.so.conf.d/xuserlocal.conf
sudo ldconfig
sudo reboot