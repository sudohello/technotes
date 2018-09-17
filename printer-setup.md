---
Title: Printer Setup
Decription: Printer Setup
Author: Bhaskar Mangal
Date: 14th-Apr-2018
Tags: Printer Setup
---

**Table of Contents**
* TOC
{:toc}


## Printer Setup

## HP LaserJet Pro MFP M132nw Printer
https://support.hp.com/in-en/document/c05228191
http://www8.hp.com/in/en/products/printers/product-detail.html?oid=9365431


* **Requirements**
- Setup the printer in Linux anbd Windows over wifi
- Able to print from Desktop, Laptop, smart phones connected over wifi
- To the extreme end, able to print documents remotely
- mobile printing over wifi

### Drivers
- [How To MFP 132nw](https://support.hp.com/us-en/product/hp-laserjet-pro-mfp-m132-series/9365375/model/9365377/drivers)
- https://support.hp.com/us-en/document/c01174360
- https://developers.hp.com/hp-linux-imaging-and-printing
- [FAQs  before installing](https://developers.hp.com/hp-linux-imaging-and-printing/downloads)

**HPLIP: HP Linux Imaging and Printing**
The HP Linux Imaging and Printing project provides printing support for 2,745 printer models including DeskJets, OfficeJets, PhotoSmarts, Business Inkjets, LaserJets, LaserJet Multi-function Printers (MFPs), Edgeline MFPs, and Printer-Scanner-Copiers (PSCs).
- [Support4ed Printers](https://developers.hp.com/hp-linux-imaging-and-printing/supported_devices/index)
- [Installaing latest HPLIP](https://developers.hp.com/hp-linux-imaging-and-printing/install/installtree)

```bash
# printer drivers
dpkg -l hplip
# https://askubuntu.com/questions/770243/hp-laserjet-wont-print-16-04-lts
sudo hp-setup -i
# other commands
lpq
lpc status
lpstat -a
hp-firmware
```

## Troubleshooting
* Facing exactly these issues
https://ubuntuforums.org/showthread.php?t=2335391

## References
https://developers.hp.com/hp-linux-imaging-and-printing/install/manual/index.html

./configure --with-hpppddir=/usr/share/ppd/HP --libdir=/usr/lib64 --prefix=/usr --enable-udev-acl-rules --enable-qt4 --disable-libusb01_build --enable-doc-build --disable-cups-ppd-install --disable-foomatic-drv-install --disable-foomatic-ppd-install --disable-hpijs-install --disable-udev_sysfs_rules --disable-policykit --enable-cups-drv-install --enable-hpcups-install --enable-network-build --enable-dbus-build --enable-scan-build --enable-fax-build

'./configure --with-hpppddir=/usr/share/ppd/HP --libdir=/usr/lib --prefix=/usr --enable-qt4 --disable-qt5 --enable-doc-build --disable-cups-ppd-install --disable-foomatic-drv-install --disable-libusb01_build --disable-foomatic-ppd-install --disable-hpijs-install --disable-class-driver --disable-udev_sysfs_rules --disable-policykit --enable-cups-drv-install --enable-hpcups-install --enable-network-build --enable-dbus-build --enable-scan-build --enable-fax-build --enable-apparmor_build'

Printer Name: HP_LaserJet_MFP_M129-M134
PPD File: drv:///hp/hpcups.drv/hp-laserjet_mfp_m129-m134.ppd
Fax Name: HP_LaserJet_MFP_M129-M134_fax


MISSING DEPENDENCIES
--------------------
Following dependencies are not installed. HPLIP will not work if all REQUIRED dependencies are not installed and some of the HPLIP features will not work if OPTIONAL dependencies are not installed.
Package-Name         Component            Required/Optional   
pyqt5-dbus           gui_qt5              REQUIRED            
libnetsnmp-devel     network              REQUIRED            
sane-devel           scan                 REQUIRED            
python-dbus          fax                  REQUIRED            
pyqt5                gui_qt5              REQUIRED            
libtool              base                 REQUIRED            
cups-image           base                 REQUIRED            
python-notify        gui_qt5              OPTIONAL            
xsane                scan                 OPTIONAL  


sudo apt install pyqt4-dev-tools pyqt5-dev pyqt5-dev-tools pyqt4.qsci-dev pyqt5.qsci-dev
pip3 install pyqt5


Following dependencies are not installed. HPLIP will not work if all REQUIRED dependencies are not installed and some of the HPLIP features will not work if OPTIONAL dependencies are not installed.
Package-Name         Component            Required/Optional   
pyqt5-dbus           gui_qt5              REQUIRED            
pyqt4-dbus           gui_qt4              REQUIRED            
pyqt5                gui_qt5              REQUIRED    


Running 'sudo apt-get install --assume-yes python-qt4-dbus'
Please wait, this may take several minutes...
Running 'sudo apt-get install --assume-yes python-dbus.mainloop.pyqt5'
Please wait, this may take several minutes...
Running 'sudo apt-get install --assume-yes gtk2-engines-pixbuf'
Please wait, this may take several minutes...
Running 'sudo apt-get install --assume-yes python-pyqt5'
Please wait, this may take several minutes...
error: A required dependency 'pyqt5-dbus (PyQt 5 DBus - DBus Support for PyQt5)' is still missing.
error: A required dependency 'pyqt5 (PyQt 5- Qt interface for Python (for Qt version 4.x))' is still missing.


RUNNING POST-PACKAGE COMMANDS
-----------------------------
OK


RE-CHECKING DEPENDENCIES
------------------------
error: A required dependency 'pyqt5-dbus (PyQt 5 DBus - DBus Support for PyQt5)' is still missing.
error: A required dependency 'pyqt5 (PyQt 5- Qt interface for Python (for Qt version 4.x))' is still missing.
error: Installation cannot continue without these dependencies.



SECURITY PACKAGES
-----------------
AppArmor is installed. 
AppArmor protects the application from external intrusion attempts making the application secure


HPLIP-3.16.3 exists
HPLIP-3.18.3

./configure --with-hpppddir=/usr/share/ppd/HP --libdir=/usr/lib --prefix=/usr --enable-qt4 --disable-qt5 --enable-doc-build --disable-cups-ppd-install --disable-foomatic-drv-install --disable-libusb01_build --disable-foomatic-ppd-install --disable-hpijs-install --disable-class-driver --disable-udev_sysfs_rules --disable-policykit --enable-cups-drv-install --enable-hpcups-install --enable-network-build --enable-dbus-build --enable-scan-build --enable-fax-build --enable-apparmor_build


## Setting up Mobile Printing

### USB reverse tethering

There is a solution for unrooted devices

I know this is a late answer, but as all existing answers suggest that USB reverse tethering is only possible if either your device is rooted or has system support for reverse tethering, I though it'd be worth pointing out there's one more option:

A few months ago, I was looking for a solution that would allow me to use my laptop's Internet connection on an unrooted Android device, but I just couldn't find a solution. Eventually, I started to develop my own solution. The result is an app that works on devices running Android 4.0 or higher on client side, and all major desktop OSs on the host side.


http://salutepc.altervista.org/usb-reverse-tethering-no-root-android-linux-automatic-mode.html