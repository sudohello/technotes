/*
Title: GRUB
Decription: GRUB 
Author: Bhaskar Mangal
Date: 
Tags: GRUB, Ubuntu
*/


## Ubuntu, GRUB
sudo blkid
https://www.cyberciti.biz/faq/linux-force-fsck-on-the-next-reboot-or-boot-sequence/

sudo touch /forcefsck

/etc/init/mountall.conf file,

/etc/rc.sysinit file


https://askubuntu.com/questions/521831/ubuntu-server-vm-hangs-after-begin-running-scripts-init-bottom-done

https://bugs.launchpad.net/ubuntu/+source/upstart/+bug/430272


## Update initramfs
* https://ubuntugenius.wordpress.com/2010/05/24/fix-a-failed-initramfs-update-do-it-before-you-reboot/
```
update-initramfs -u
update-initramfs -u -k all
```

* https://www.linux.com/learn/kernel-newbie-corner-initrd-and-initramfs-whats

ideas of initrd and initramfs, and what they're for and, most importantly

**initrd - initial ram disk**

the bootloader's job to pass control to the kernel, hand it the "initrd" (initial ram disk), let the kernel mount it and get what it needs, whereupon the kernel can toss the initrd and replace it with the real root filesystem

```
# gunzip -c /boot/initrd-2.6.31.img > /tmp/my_initrd
# cpio -it < /tmp/my_initrd         #examine contents
# cpio -i < /tmp/my_initrd          #unload
```

**initramfs (initial RAM file system)**
It is what I call an even earlier potential root file system that you can build into the kernel image itself. And because of its location (internal to the kernel), it will (if it exists) take precedence.
The initial RAM filesystem is a ramfs which is loaded by the boot loader (loadlin or lilo) and that is mounted as root before the normal boot procedure. It is typically used to load modules needed to mount the "real" root file system, etc.

```
sudo mount /dev/sdXY /mnt
sudo mount --bind /dev /mnt/dev
sudo mount --bind /dev/pts /mnt/dev/pts
sudo mount --bind /proc /mnt/proc
sudo mount --bind /sys /mnt/sys
sudo chroot /mnt
update-initramfs -c -k x.x.x-xx-generic
for example if your kernel system 4.4.0-31-generic
update-initramfs -c -k 4.4.0-31-generic
```
dpkg –configure -a
apt-get update

**hangs after "Begin: Running /scripts/init-bottom".**

* https://askubuntu.com/questions/177299/scripts-slowing-boot
* displayed the scripts that ran at startup with
```
initctl list
```
/usr/share/initramfs-tools/init

sudo apt-get install bootchart
