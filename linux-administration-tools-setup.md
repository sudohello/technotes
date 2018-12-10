---
Title: Linux Administration, Tools setup
Decription: nitty gritty of Linux
Author: Bhaskar Mangal
Date: 20 Jan 2017
Updated: 12 Jul 2018
Tags: Linux, Administration, Tools, Softwares
---

**Table of Contents**
* TOC
{:toc}


## Software & Tools Setup Help

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
lpoptions  -p TOSHIBA_e-STUDIO2330C | awk '{for (i=1; i<=NF; i++) {if ($i ~ /device-uri/) {print $i}}}' device-uri=socket://<IP_ADDRESS>
lpoptions  -p HL2240D | awk '{for (i=1; i<=NF; i++) {if ($i ~ /device-uri/) {print $i}}}' device-uri=socket://<IP_ADDRESS>
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

* **API Development**
	* [Postman](https://www.getpostman.com/)

## Linux (Ubuntu) Toolchain Setup
* scp, sftp, ssh, rsync
* http://askubuntu.com/questions/94665/what-is-a-program-similar-to-winscp

## LDAP

**Find number of cores in Linux**
- [how-to-know-number-of-cores-of-a-system-in-linux](http://unix.stackexchange.com/questions/218074/how-to-know-number-of-cores-of-a-system-in-linux)
```bash
cat /proc/cpuinfo
#
cat /proc/cpuinfo | grep "cpu cores"
grep -m 1 'cpu cores' /proc/cpuinfo
# Another useful utility is dmidecode which outputs per socket information.
sudo dmidecode -t 4 | grep -E 'Socket Designation|Count'
sudo dmidecode -t 4 | egrep -i "Designation|Intel|core|thread"
```
* http://www.tutorialspoint.com/articles/how-to-install-doxygen-on-ubuntu
* http://stackoverflow.com/questions/16963579/generate-graphs-and-diagrams-with-doxygen
* http://askubuntu.com/questions/315646/update-java-alternatives-vs-update-alternatives-config-java
* https://askubuntu.com/questions/668538/cores-vs-threads-how-many-threads-should-i-run-on-this-machine
- You will find how many threads you can run on your machine by running htop or ps command that returns number of process on your machine.
- If you want to calculate number of all users process, you can use one of these commands:
```bash
ps -aux| wc -l
ps -eLf | wc -l
#Calculating number of an user process:
ps --User root | wc -l
#
# lscpu
# CPU(s):              4
# On-line CPU(s) list: 0-3
# Thread(s) per core:  1
# Core(s) per socket:  4
# Socket(s):           1 ## physical CPU (socket) 
#
```
- To get a complete picture you need to look at the number of threads per core, cores per socket and sockets. If you multiply these numbers you will get the number of CPUs on your system.
```bash
CPUs = Threads per core X cores per socket X sockets
```
- CPUs are what you see when you run `htop` (these do not equate to physical CPUs).
- The output of `nproc` corresponds to the CPU count from `lscpu`
- The cpu cores reported by `/proc/cpuinfo` corresponds to the Core(s) per socket reported by `lscpu`
```bash
nproc -all
top
htop
#
lscpu | grep -E '^Thread|^Core|^Socket|^CPU\('
```


## CVS Setup
* set the following in .bashrc file (under the home dir)
```bash
export CVSROOT=":pserver:<username>@<IP>:<port>/<path>/CVS_REPO"
alias cvstt='cvs status 2>/dev/null | grep ^File | grep -v Up-to'
cvs login
```

## Apache2 Installation
* Refer: [apache guide](apache.md)

## Exports & Aliases
Use as per requirements
* In .bashrc file (under home dir), read more on bashrc
```bash
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64
export PATH=/usr/lib/jvm/java-1.8.0-openjdk-amd64/bin:$PATH
export TOMCAT_HOME=/usr/share/tomcat5
export LD_LIBRARY_PATH=/usr/local/lib
export MALLOC_CHECK_=0
#
export LD_LIBRARY_PATH=/usr/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/lib/libflycapture-c.so:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/lib/libflycapture.so:$LD_LIBRARY_PATH
#
export LD_LIBRARY_PATH=/usr/lib/jvm/java-1.8.0-openjdk-amd64/jre/lib/amd64/server:$LD_LIBRARY_PATH
#
alias huawai="echo <userName> | sudo -kS touch /etc/usb_modeswitch.d/12d1:1f01; echo <userName> | sudo -kS usb_modeswitch -J -v 0x12d1 -p 0x1f01;"
alias vpn="echo <userName> | sudo -kS openvpn --config ~/Downloads/fw-udp-1194-<userName>-config.ovpn;"
```

## Mounting
**mount read, write**
```bash
sudo mount -o rw /dev/sda1 /media/tmp/
```

```bash
#FAT
sudo mount -t vfat -o rw,noauto,async,user,umask=1000 /dev/sdb1 /media/tmp/
mount -l -t vfat,fat,msdos
```

**mount NTFS**
```bash
sudo mount -t ntfs -o nls=utf8,umask=0222 /dev/sdb1 /media/windows
```

* **Mount samba as dir**
```bash
sudo apt install nfs-common
sudo apt install smb4k
sudo apt install cifs-utils
sudo mount -t cifs //<IP>/samba5 /mnt/samba121 -o username=<username>,workgroup=<workgroup-name>
```
* https://serverfault.com/questions/414074/mount-cifs-host-is-down
```bash
sudo mount -t cifs //<IP>/<sharedDirName> /media/<mountPoint> --verbose -o username=<userName>,domain=<domainName>,vers=1.0
```
- if `vers=1.0` is not provided in `Ubuntu 18.04 LTS` it throws error `host is down`
- `sharedDirName` is not the name of the folder on the file system, rather the shared folder name
```bash
sudo umount /media/<mountPoint>
```
- check `mount.local.sh` under linuxscripts for example
* https://wiki.samba.org/index.php/Mounting_samba_shares_from_a_unix_client

**Mount Points in mtab and fstab**
- https://askubuntu.com/questions/607149/change-permissions-to-a-specific-user-in-ubuntu-12-04
```bash
cat /etc/mtab
sudo vi /etc/fstab
sudo apt install exfat-utils
```

**Safe mounting**
- https://askubuntu.com/questions/14365/mount-an-external-drive-at-boot-time-only-if-it-is-plugged-in
- http://techmonks.net/nofail-and-nobootwait-mount-options-in-fstab-prevent-boot-problems/
```bash
LABEL=Series  /mnt/filer/Series  xfs  auto,nofail,nodev,noexec,nouser,noatime  0  2
UUID=XXXXXXXXXXXXXXX    /myhdd ntfs  auto,nofail,noatime,rw,user    0   0
```

## **Sending message to linux to linux user**
* https://unix.stackexchange.com/questions/99460/sending-messages-to-another-user
```bash
talk —
mesg — Control if (non-root) users can send messages to your terminal.
wall — Send a message to all logged-in users.
who — Report which users are logged in to the system.
write — Send a message to another user.
```
* https://askubuntu.com/questions/61995/chat-over-lan-from-linux-to-linux
	- `netcat / nc`
	- On PC 1, type: `nc -l 55555`
	- On PC 2, type: `nc $IP 55555`, where $IP equals the local IP address of PC 1 [e.x. 192.168.2.50]

* **Enable Remote Desktop Connection on Ubuntu**
* https://askubuntu.com/questions/4474/enable-remote-vnc-from-the-commandline
```bash
gconftool-2 --set --type=bool /desktop/gnome/remote_access/enabled true
gconftool-2 -a /desktop/gnome/remote_access
gsettings list-keys org.gnome.Vino
```
* `/usr/lib/vino/vino-server`

* What is **/dev/null**?
* What is the purpose of outputting to /dev/null like that, and what does the 2>&1 mean?
```bash
some command > /dev/null 2>&1
# So, the STDOUT is redirected to the bit-bucket(trash) and the STDERR is redirected to where the STDOUT is located: the bit-bucket.
```
* https://askubuntu.com/questions/12098/what-does-outputting-to-dev-null-accomplish-in-bash-scripts

  - `>/dev/null` redirects the command standard output to the null device, which is a special device which discards the information written to it
  - `2 >&1` redirects the standard error stream to the standard output stream (stderr = 2, stdout = 1).

In practice it prevents any output from the command (both stdout and stderr) from being displayed. It's used when you don't care about the command output.
STDIN is represented by 0, STDOUT by 1, and STDERR by 2.
`/dev/null` is the bit-bucket: the place where you dump anything you don't need.

* https://askubuntu.com/questions/698669/setup-remmina-for-remote-desktop-connection
1. In order to be able to use Remmina, you need first to activate certain options of the "Desktop Sharing" screen (Dash -> Desktop Sharing) on both computers:
2. On the Desktop Sharing Preferences:

Activate the option "Allow other users to view your desktop"
Activate the option "Allow other users to control your desktop"
For security's sake, also:

Activate the option "You must confirm each access to this machine"
Activate the option "Require the user to enter this password" and provide a password
Once the configuration is done, you can simply open Remmina, create a new connection and specify the connection to the other computer using VNC (virtual network computing) protocol and using the password you used in the "Desktop Sharing" screen. Hint: You can ignore the field "user".



**Other Remote Desktop Control Option**
* Teamviewer
* Anydeck
  * https://websiteforstudents.com/how-to-install-anydesk-on-ubuntu-16-04-17-10-18-04-desktop/


## Disk Space Monitoring
* https://askubuntu.com/questions/413358/disk-is-full-but-cannot-find-big-files-or-folders
```bash
sudo du -sch /root/*
du -sch .[!.]* * |sort -h
#
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

```bash
sudo -s
```
and you don't have to put "sudo" in front of everything!

## Install-chdk-on-your-canon-camera-using-linux
- https://scribblesandsnaps.com/2010/11/16/install-chdk-on-your-canon-camera-using-linux/
- https://askubuntu.com/questions/458743/cannot-format-my-sd-card
```bash
# Format with Fat16
sudo mkfs.vfat -F16 /dev/sdb1
#
echo -n BOOTDISK | sudo dd bs=1 count=8 seek=64 of=/dev/sdbx
#Replace the sdbx part with the actual name of the small FAT16 partition
```
```bash
dd bs=1 count=72 seek=0 conv=notrunc if=/dev/
#
sudo mount -t vfat -o rw,noauto,async,user,umask=1000 /dev/sdb1 /mnt/tmp
#
df | grep -e \"/$\" | sed s/[s/]/\\ /g | awk '{print $2\" \"$3 }' | sed s/\\ /s/g
#
printf \"BOOTDISK\" | dd bs=1 count=8 seek=0x40 conv=notrunc of=/dev/disk"
#
diskutil list
#
```

**fdisk**
- https://gist.github.com/keithmorris/b2aeec1ea947d4176a14c1c6a58bfc36

## Tools
* **Bulk Rename**
http://www.webupd8.org/2016/03/quickly-batch-rename-files-in-linux.html
```bash
sudo add-apt-repository ppa:nilarimogard/webupd8
sudo apt-get update
sudo apt-get install metamorphose2
```

**Flatten Directory Structure**
- https://superuser.com/questions/91307/copying-only-jpg-from-a-directory-structure-to-another-location-linux
- https://ubuntuforums.org/showthread.php?t=1385966
- https://www.lifewire.com/feh-command-line-image-viewer-4054068
```bash
find . -type f \( -iname "*.jpg" -o -iname "*.jpeg" \) -exec cp '{}' /cpjpg \;
#
find ./ -name '*.jpg' -exec cp '{}' ./ \;
#
sudo apt-get install feh
feh -Fzr -D 5 ~/Images
```


## Feh
* https://wiki.archlinux.org/index.php/feh
* https://www.maketecheasier.com/feh-image-viewer/
* https://unix.stackexchange.com/questions/395011/feh-warns-on-text-files
* https://raspberrypi.stackexchange.com/questions/38511/auto-reload-new-images-in-feh-image-viewer
```bash
feh -Y -x -q -D 1 -B white -F -Z -z -r .
#
feh -Y -q -D 1 -R 5 -B white .
feh -Y -q -D 1 -R 5 -B white -Z -g 640x480 -d --draw-tinted --draw-exif --title "Traffic Sign Detection of Gaze Images" .
#
feh -Y -q -D 1 -R 5 -B white -Z -z --scale-down -d --draw-tinted --title "Traffic Sign Detection of Gaze Images" .
#
feh -ZXrFD 5 ./
```

     h [toggle_pause]
             Pause/Continue the slideshow.  When it is paused, it will not automatically change slides based on --slideshow-delay.

     i [toggle_info]
             Toggle info display (see --info)

**Image viewers**
* eoq
* geeqie
	- https://en.wikipedia.org/wiki/Geeqie
* feh


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
sudo apt install pdftk
pdftk /path/to/input.pdf input_pw <yourpassword> output out.pdf
```
* **Merge PDF files**
```bash
pdfunite 1.pdf 2.pdf 12.pdf
```
* **PDF Editors**
- http://www.linuxandubuntu.com/home/5-best-linux-pdf-editors

## Sounds
**how-to-turn-off-the-beep-only-in-bash-tab-complete**
- https://unix.stackexchange.com/questions/73672/how-to-turn-off-the-beep-only-in-bash-tab-complete
- https://serverfault.com/questions/26405/how-do-i-turn-off-the-beep-in-the-terminal-in-linux
* https://www.cyberciti.biz/faq/how-to-linux-disable-or-turn-off-beep-sound-for-terminal/
Open Gnome terminal

## bash script
* error codes, exiting scripts
- https://stackoverflow.com/questions/1378274/in-a-bash-script-how-can-i-exit-the-entire-script-if-a-certain-condition-occurs

`Click on Settings > Preferences > Silence Terminal Bell`

## Audio


### USB Soundcard
- https://blog.ostermiller.org/ubuntu-usb-audio/


## Data Streaming
- https://code.tutsplus.com/tutorials/building-with-the-twitter-api-using-real-time-streams--cms-22194
- https://kraken-php.com/
- https://www.reddit.com/r/PHP/comments/573fuh/kraken_distributed_async_php_framework/
- https://github.com/reactphp


## Wifi troubleshooting
```bash
sudo lshw -C network
sudo lshw -class network
lspci -nnk | grep 0280 -A2
# 07:00.0 Network controller [0280]: Broadcom Corporation BCM43142 802.11b/g/n [14e4:4365] (rev 01)
# 	Subsystem: Dell Wireless 1704 802.11n + BT 4.0 [1028:0016]
# 	Kernel modules: bcma, wl
#
sudo modprobe wl && dmesg | grep wl
modprobe: ERROR: could not insert 'wl': Exec format error
dmesg | grep wl
dkms status -m broadcom-wl
#
sudo apt-get purge bcmwl-kernel-source
sudo apt-get update
sudo apt-get install bcmwl-kernel-source
```
- https://unix.stackexchange.com/questions/69199/wireless-not-working-after-update-network-unclaimed
- https://askubuntu.com/questions/770490/broadcom-wireless-drivers-unclaimed-after-installing-update-16-04
```bash
sudo apt-get install --reinstall bcmwl-kernel-source
#
cat /etc/modprobe.d/iwlwifi.conf
```
1 # /etc/modprobe.d/iwlwifi.conf
2 # iwlwifi will dyamically load either iwldvm or iwlmvm depending on the
3 # microcode file installed on the system.  When removing iwlwifi, first
4 # remove the iwl?vm module and then iwlwifi.
5 remove iwlwifi \
6 (/sbin/lsmod | grep -o -e ^iwlmvm -e ^iwldvm -e ^iwlwifi | xargs /sbin/rmmod) \
7 && /sbin/modprobe -r mac80211
```bash
sudo lshw -C network
# product: RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
```
- https://askubuntu.com/questions/840772/how-to-create-this-etc-pm-config-d-config
- https://askubuntu.com/questions/413663/whats-the-purpose-of-etc-pm-config-d-and-power-d/413684
- https://ubuntuforums.org/archive/index.php/t-2004690.html
```bash
# Add one line:
sudo gedit /etc/pm/config.d/config
SUSPEND_MODULES="iwlwifi"
```

## UEFI Loading Issues
- https://askubuntu.com/questions/139157/booting-ubuntu-with-acpi-off-grub-parameter?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
- https://wiki.ubuntu.com/DebuggingACPI
- `acpi=off` 

**UEFI**: Unified-Extensible-Firmware-Interface
- http://whatis.techtarget.com/definition/Unified-Extensible-Firmware-Interface-UEFI
- Unified Extensible Firmware Interface (UEFI) is a specification for a software program that connects a computer's firmware to its operating system (OS). UEFI is expected to eventually replace BIOS.
- https://www.howtogeek.com/56958/htg-explains-how-uefi-will-replace-the-bios/

**SSDs**
* `/dev/nvme` stands for SSDs

**grub making changes**
- Make the change permanent:
- In Ubuntu, open terminal from the dash or press Ctrl+Alt+T, execute this to edit grub: gksudo gedit /etc/default/grub.
- Find the line starting with GRUB_CMDLINE_LINUX_DEFAULT and append acpi=off to its end, make it look like: GRUB_CMDLINE_LINUX_DEFAULT="quiet splash acpi=off"

## wget

**how-to-specify-the-location-with-wget**
https://stackoverflow.com/questions/1078524/how-to-specify-the-location-with-wget
```bash
#-O is the option to specify the path of the file you want to download to.
#
wget <file.ext> -O /path/to/folder/file.ext
#-P is prefix where it will download the file in the directory
#
wget <file.ext> -P /path/to/folder
```

**wget-resume-continue-broken-download**
https://www.garron.me/en/bits/wget-resume-continue-broken-download.html
Example:
```bash
wget -c http://releases.ubuntu.com/18.04/ubuntu-18.04-desktop-amd64.iso
```

## compress, uncompress
- https://stackoverflow.com/questions/18402395/how-to-uncompress-a-tar-gz-in-another-directory
```bash
tar -xzf bar.tar.gz -C foo
```

## Terminal Multiplexers
- Screens, byobu, Gauake,
* https://www.digitalocean.com/community/tutorials/how-to-install-and-use-screen-on-an-ubuntu-cloud-server
* https://askubuntu.com/questions/449597/is-there-any-user-friendly-alternative-to-screen
* https://www.slant.co/topics/4018/~terminal-multiplexers
* https://www.linuxlinks.com/terminalmultiplexers/
* https://linuxconfig.org/an-introduction-to-terminal-multiplexers
* I guess you all know this: you are connected to your server with SSH and in the middle of compiling some software (e.g. a new kernel) or doing some other task which takes lots of time, and suddenly your connection drops for some reason, and you lose your labour. This can be very annoying, but fortunately there is a small utility called screen which lets you reattach to a previous session so that you can finish your task. This short tutorial shows how to use screen for just this purpose.


**Check installed library version**
* https://askubuntu.com/questions/434154/how-to-get-the-list-of-installed-library-packages-only
* `/sbin/ldconfig -p`
* The -v option will show the libraries version.

**/usr/bin/ld: final link failed: No space left on device**
* http://www.ubuntu-forum.de/artikel/61799/final-link-failed-no-space-left-on-device.html

<!-- /usr/bin/ld: final link failed: No space left on device
collect2: error: ld returned 1 exit status
features/CMakeFiles/pcl_features.dir/build.make:1107: recipe for target 'lib/libpcl_features.so.1.8.1.99' failed
make[2]: *** [lib/libpcl_features.so.1.8.1.99] Error 1
CMakeFiles/Makefile2:1438: recipe for target 'features/CMakeFiles/pcl_features.dir/all' failed
make[1]: *** [features/CMakeFiles/pcl_features.dir/all] Error 2
Makefile:160: recipe for target 'all' failed
make: *** [all] Error 2 -->

```bash
df -i 
free -m
grep tmpfs /etc/fstab
mount |grep \/tmp
```

## Directory Space
```bash
du -h --max-depth=1 | sort -hr
```

## Change Hostname/Computer name
* http://ubuntuhandbook.org/index.php/2014/04/change-hostname-ubuntu1404/
```bash
hostname NEW_NAME_HERE
sudo vi /etc/hostname
sudo vi /etc/hosts
```

## Get the UUID of the block device
* https://help.ubuntu.com/community/UsingUUID
```bash
 sudo blkid
ls -l /dev/disk/by-uuid/
```

## System Setup

### Move Home folder
- https://www.maketecheasier.com/move-home-folder-ubuntu/

### Running the script on bootup
- https://stackoverflow.com/questions/2062543/running-a-script-with-the-help-of-grub-and-menu-lst

### Remote and Local File transfer

#### rsync
```bash
rsync -aXS
```
#### scp
- https://stackoverflow.com/questions/11304895/how-to-scp-a-folder-from-remote-to-local
* To copy all from Local Location to Remote Location (Upload)
```bash
scp -r /path/from/destination username@hostname:/path/to/destination
```
* To copy all from Remote Location to Local Location (Download)
```bash
scp -r username@hostname:/path/from/destination /path/to/destination
```
* Custom Port where xxxx is custom port number
```bash
 scp -r -P xxxx username@hostname:/path/from/destination /path/to/destination
```
* Copy on current directory from Remote to Local
```bash
scp -r username@hostname:/path/from/file .
```
* Help:
	-r Recursively copy all directories and files
	Always use full location from /, Get full location by pwd
	scp will replace all existing files
	hostname will be hostname or IP address
	if custom port is needed (besides port 22) use -P portnumber
	. (dot) - it means current working directory, So download/copy from server and paste here only.
	- **Note**: Sometimes the custom port will not work due to the port not being allowed in the firewall, so make sure that custom port is allowed in the firewall for incoming and outgoing connection

### User and Group details
- http://geek-university.com/linux/uid-user-identifier-gid-group-identifier/

**Enabling Intel Onboard Graphics**
* https://askubuntu.com/questions/989946/cannot-change-resolution-with-8th-gen-intel-cpu-in-ubuntu-16-04/1002662#1002662
```bash
sudo vi /etc/default/grub
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash i915.alpha_support=1"
sudo update-grub
sudo reboot
```

**System Information**
```bash
sudo lshw -short
#
efibootmg1 -v
#
```

**xorg crashed with SIGABRT in OSAbort**
- update/re-install following:
```bash
sudo apt install xserver-xorg-core-hwe-16.04 apt apt-utils dpkg libapparmor1 libapt-inst2.0 libapt-pkg5.0 libaudit-common libaudit1 libblkid1 libgcrypt20 libmount1 libpam-modules libpam-modules-bin libpam-systemd libpam0g libprocps4 libsmartcols1 libsystemd0 mount procps systemd util-linux uuid-runtime
```

## Interesting Terminologies and Command in Linux
* https://www.tecmint.com/20-funny-commands-of-linux-or-linux-is-fun-in-terminal/
* https://www.lopezferrando.com/30-interesting-shell-commands/

* Shebang - The #! syntax used in scripts
  - https://en.wikipedia.org/wiki/Shebang_(Unix)
	- https://bash.cyberciti.biz/guide/Shebang
	- The #! syntax used in scripts to indicate an interpreter for execution under UNIX / Linux operating systems
  * Some typical shebang lines:
    * `#!/bin/sh` – Execute the file using the Bourne shell, or a compatible shell, with path `/bin/sh`
    * `#!/bin/bash` – Execute the file using the Bash shell.
    * `#!/bin/csh -f` – Execute the file using csh, the C shell, or a compatible shell, and suppress the execution of the user’s .cshrc file on startup
    * `#!/usr/bin/perl -T` – Execute using Perl with the option for taint checks
    * `#!/usr/bin/env python` – Execute using Python by looking up the path to the Python interpreter automatically via env
    * `#!/bin/false` – Do nothing, but return a non-zero exit status, indicating failure. Used to prevent stand-alone execution of a script file intended for execution in a specific context, such as by the . command from sh/bash, source from csh/tcsh, or as a .profile, .cshrc, or .login file.
    Shebang lines may include specific options that are passed to the interpreter. However, implementations vary in the parsing behavior of options; for portability, only one option should be specified without any embedded whitespace. Further portability guidelines are found below.

* man - The man command is used to format and display the man pages
	- www.linfo.org/man.html
	- The man pages are a user manual that is by default built into most Linux
* finger - user information lookup program
	- https://www.systutorials.com/docs/linux/man/1-finger/	
* yes - output a string repeatedly until killed
* date
* flock - manage locks from shell scripts
* xkill - kill a client by its X resource
* touch - change file timestamps
* nice - run a program with modified scheduling priority
* make - GNU make utility to maintain groups of programs
* whereis - locate the binary, source, and manual page files for a command
* unzip - list, test and extract compressed files in a ZIP archive
  * Unzip files in particular directory or folder under Linux or UNIX: `unzip blah.zip -d /tmp`
* mount - mount a filesystem
* umount - unmount file systems
* strip - Discard symbols from object files
* sleep - delay for a specified amount of time
* uptime - Tell how long the system has been running
* watch - execute a program periodically, showing output fullscreen
* cat
	- Copy to clipboard: `cat file.txt | xclip -selection clipboard`
* tac  - cat backwards (starting from the end)
	- `tac file`
* nohup - run a command immune to hangups, with output to a non-tty
	- `nohup ./script.sh &`
	- Keep program running after leaving SSH session
* split - Split long file in files with same number of lines
	- `split -l LINES -d file.txt output_prefix`
* timeout - Run a command for a limited time
	- `timeout 10s ./script.sh`
* time - Check resources' usage of command
	- `/usr/bin/time -v ls`
* comm - Combine lines from two sorted files
	- `comm file1 file2`
* shuf - Randomize lines in file
```bash
cat file.txt | sort -R
cat file.txt | sort -R | head  # Pick a random msambple
#
# Even better (suggested by xearl in Hacker news):
shuf file.txt
```
* namei - Check permissions of each directory to a file
	- `namei -l /path/to/file.txt`
* ls
	- Prepend line number: `ls | nl`
	- List file by size: `ls -lS`
* w - Who is logged in?
	- `w`
* find
```bash
find . -size 20c             # By file size (20 bytes)
find . -name "*.gz" -delete  # Delete files
find . -exec echo {} \;      # One file by line
./file1
./file2
./file3
find . -exec echo {} \+      # All in the same line
./file1 ./file2 ./file3
```
* mtr - nice traceroute
	- `mtr google.com`
* readlink
	- Get full path of file: `readlink -f file.txt`
* rename
	- Rename selected files using a regular expression: `rename 's/\.bak$/.txt/' *.bak`
* rev - reverse lines characterwise
	- `rev file`

* **bash-script-to-replace-char-in-variable**
	- https://www.linuxquestions.org/questions/programming-9/bash-script-to-replace-char-in-variable-251992/
```bash
VER="1.64.0"
DIR="boost_"$(echo $VER | sed -e 's/\./_/g')
echo $DIR ## boost_1_64_0
```

* **lib linking**
	- Libraries have been installed in:
  - `/usr/local/lib`
```
If you ever happen to want to link against installed libraries
in a given directory, LIBDIR, you must either use libtool, and
specify the full pathname of the library, or use the `-LLIBDIR'
flag during linking and do at least one of the following:
   - add LIBDIR to the `LD_LIBRARY_PATH' environment variable
     during execution
   - add LIBDIR to the `LD_RUN_PATH' environment variable
     during linking
   - use the `-Wl,-rpath -Wl,LIBDIR' linker flag
   - have your system administrator add LIBDIR to `/etc/ld.so.conf'

See any operating system documentation about shared libraries for
more information, such as the ld(1) and ld.so(8) manual pages.
----------------------------------------------------------------
```


## `sed` command
* https://unix.stackexchange.com/questions/112023/how-can-i-replace-a-string-in-a-files


## Utilities
* Open and Edit Large text files
  * https://askubuntu.com/questions/28847/text-editor-to-edit-large-4-3-gb-plain-text-file
  * https://joe-editor.sourceforge.io/
  * https://stackoverflow.com/questions/1591723/working-with-huge-files-in-vim
  * http://stoopidsimple.com/lfhex
  * Another method is to use split. Split the file into 8 pieces and manipulate the files with a editor. After  hat, you reassemble the files again
    ```bash
    split -b 53750k <your-file>
    cat xa* > <your-file>
    SYNOPSIS
           split [OPTION]... [INPUT [PREFIX]]
    -a, --suffix-length=N
                  use suffixes of length N (default 2)
           -b, --bytes=SIZE
                  put SIZE bytes per output file
           -C, --line-bytes=SIZE
                  put at most SIZE bytes of lines per output file
           -d, --numeric-suffixes
                  use numeric suffixes instead of alphabetic
           -l, --lines=NUMBER
                  put NUMBER lines per output file
    ```
* Sublime Text Editor - [sublime-text-editor.md]
* Beyond Compare - Comparing text Files
	- http://www.scootersoftware.com/download.php?zz=kb_linux_install
```bash
#Terminal Install
sudo apt install libqtwebkit4
wget -c http://www.scootersoftware.com/bcompare-4.2.6.23150_amd64.deb
sudo apt update
sudo apt install gdebi-core
sudo gdebi bcompare-4.2.6.23150_amd64.deb
# Terminal Uninstall
sudo apt remove bcompare
```
* FreeFileSync
	- https://freefilesync.org/tutorials.php
	- `wget -c https://freefilesync.org/download/FreeFileSync_10.2_Linux_64-bit.tar.gz`

* **Ubuntu Software Installers**
	- apt, apt-get
	- deb
	- snapd
	- flatpak
		* https://flatpak.org/setup/
		* https://flatpak.org/setup/Ubuntu/
		* **Install Flatpak**
		       sudo add-apt-repository ppa:alexlarsson/flatpak
	       sudo apt update
	       sudo apt install flatpak
	   * **Install the Software Flatpak plugin**
	    ```bash
	    sudo apt install gnome-software-plugin-flatpak
	    ```

* **Video Editor**
	- http://developer.pitivi.org/Install_with_flatpak.html?gi-language=undefined#getting-flatpak
	- https://itsfoss.com/best-video-editing-software-linux/
	- https://www.blackmagicdesign.com/products/davinciresolve/
- Flowblade
	- https://jliljebl.github.io/flowblade/download.html
- shotcut
	* https://shotcut.org/
```bash
wget -c https://github.com/mltframework/shotcut/releases/download/v18.08/shotcut-linux-x86_64-180801.tar.bz2
```
	- openshot
* LaTeX
	- https://www.latex-project.org/get/
	- https://www.latex-tutorial.com/installation/
* Screenshot and Screencasting
	- https://www.tecmint.com/take-or-capture-desktop-screenshots-in-ubuntu-linux/
* Blender Tutorials
	- http://www.paulcaggegi.com/video-editing-using-the-blender-vse/
* **Ubuntu 18.04 UI Customization**
	- https://askubuntu.com/questions/966576/customizing-tray-taskbar-date-display-in-ubuntu-beginning-with-17-10
	- http://ubuntuhandbook.org/index.php/2018/04/remove-trash-icon-ubuntu-18-04-desktop/
```bash
sudo apt install gnome-tweak-tool
gnome-tweaks
```

## Ubuntu 18.04 Shortcuts
- https://askubuntu.com/questions/747541/how-do-i-easily-switch-between-windows-rather-than-applications-with-alttab-in
* You can use `Alt+` (the key above Tab) to cycle between windows of the same application.
* You can even mix Alt+Tab to cycle between application and `Alt+` to cycle between windows of the selected application.
* There is an exposition of the rationale in this blog post from Canonical's Didier Roche. It's part of a series discussing the development of gnome integration in Ubuntu 17.10.

**/GnomeShell/Extensions**
- https://gitlab.gnome.org/GNOME/gnome-shell-extensions
- https://wiki.gnome.org/Projects/GnomeShell/Extensions

**Shortcut keys**
- https://help.ubuntu.com/stable/ubuntu-help/shell-keyboard-shortcuts.html.en
- https://www.makeuseof.com/tag/10-useful-ubuntu-keyboard-shortcuts-that-you-might-not-know-of/
- How do I show the full path in file browser rather than buttons to folders?
	- https://ubuntuforums.org/showthread.php?t=1494643
	- https://www.howtogeek.com/189777/how-to-show-the-location-entry-instead-of-the-breadcrumb-bar-in-nautilus-in-ubuntu-14.04/
	* `ctrl+L` in Nautilus File Browser
```bash
sudo apt install dconf-tools
dconf-tools
```
	* org/gnome/nautilus/preferences/show-image-thumbnails
		- `local-only` to `always`
		- `aways-use-localation-entry` if path is required instead of breadcrumbs buttins
* ALT+Tab, gnome extensions
- http://tipsonubuntu.com/2017/10/24/enable-slick-3d-alt-tab-task-switcher-ubuntu-17-10/
- `sudo apt install chrome-gnome-shell`
- https://unix.stackexchange.com/questions/120098/how-to-show-the-tree-view-in-left-pane-of-nautilus
- https://askubuntu.com/questions/973128/drag-and-drop-not-working-inside-nautilus-on-ubuntu-17-10
```bash
gsettings set org.gnome.nautilus.preferences use-experimental-views false
# use dconf-editor
```
* cloumn/block select in the console
	- `ctrl`+`alt`+`Left mouse key drag and release`


The closest thing I've found is Ctrl+Alt+Tab which allows switching between applications, windows, searching.



* opening-current-directory-from-a-terminal-onto-a-file-browser
	- https://unix.stackexchange.com/questions/244970/opening-current-directory-from-a-terminal-onto-a-file-browser
	- `nautilus .`
	- `gio open .`

* BUG: alt+arrow, super + arrow will switch between the virtual consoles.
- https://bugs.launchpad.net/ubuntu/+source/gnome-shell/+bug/1508146
alt + left/right arrows switch between tty consoles, cannot disable
+ alt + left/right arrows switch between tty consoles (Gnome Shell
+ vanishes), cannot disable

```bash
sudo dumpkeys |grep -v -E '^(\W+)alt(\W+)keycode (105|106) = (Incr|Decr)_Console' |sudo loadkeys
```
* Reset default settings
https://www.omgubuntu.co.uk/2017/10/how-to-reset-ubuntu-desktop-to-default
```bash
dconf reset -f /
```

**Mac-like file browser**
* https://softwarerecs.stackexchange.com/questions/19835/osx-like-finder-file-manager-for-linux-ubuntu
* https://askubuntu.com/questions/1020183/how-to-split-the-screen-in-gnome-files-nautilus-file-manager
* https://askubuntu.com/questions/256986/how-to-achieve-list-tree-view-in-nautilus
* Nautilus
* Dolhpin
* Nemo
* Pantheon
* thunar
* Dolphin is quite similar to nautilus in terms of file browsing and user interface concept in general. 
* pcmanfm: `sudo apt install pcmanfm`
* caja: `sudo apt-get install caja`

Required features:
* split pane
* tree view: `gsettings set org.gnome.nautilus.list-view use-tree-view true`
* mac-like file browsing

* https://itsfoss.com/gnome-tricks-ubuntu/

**Mac-OS look linke**
* https://www.ubuntupit.com/ubuntu-mac-theme-tutorial-make-ubuntu-look-like-mac-os/



## Different Bash commands
- `nohup` - run a command immune to hangups, with output to a non-tty
- `rsync` - a fast, versatile, remote (and local) file-copying tool
- `watch` - execute a program periodically, showing output fullscreen
- `tr`

* https://www.linuxnix.com/shell-scripting-convert-a-string-from-lowercase-to-uppercase/
* https://www.cyberciti.biz/faq/linux-unix-shell-programming-converting-lowercase-uppercase/
```bash
ls *.JPG | tr '[A-Z]' '[a-z]'
## replace width with comma separated entries
ls -m
```
**Rename all files in a directory to upper case**
```bash
for i in *; do mv "$i" "${i^^}"; done
```
**Rename all items in a directory to lower case**
* http://www.bashoneliners.com/oneliners/oneliner/?page=5
```bash
for i in *.JPG; do mv $i ${i,,}; done
```
* https://superuser.com/questions/71028/batch-converting-png-to-jpg-in-linux
* The simplest solution is like most already posted. A simple bash for loop.
```bash
for i in *.png ; do convert "$i" "${i%.*}.jpg" ; done
#For some reason I tend to avoid loops in bash so here is a more unixy xargs approach, using bash for the name-mangling.
#
ls -1 *.png | xargs -n 1 bash -c 'convert "$0" "${0%.*}.jpg"'
#The one I use. It uses GNU Parallel to run multiple jobs at once, giving you a performance boost. It is installed by default on many systems and is almost definitely in your repo (it is a good program to have around).
#
ls -1 *.png | parallel convert '{}' '{.}.jpg'
#The number of jobs defaults to the number of processes you have. I found better CPU usage using 3 jobs on my dual-core system.
#
ls -1 *.png | parallel -j 3 convert '{}' '{.}.jpg'
#And if you want some stats (an ETA, jobs completed, average time per job...)
#
ls -1 *.png | parallel --eta convert '{}' '{.}.jpg'
#There is also an alternative syntax if you are using GNU Parallel.
#
parallel convert '{}' '{.}.jpg' ::: *.png
#And a similar syntax for some other versions (including debian).
#
parallel convert '{}' '{.}.jpg' -- *.png
#
```
## Installing Adobe Flash Player and Plugin for browser
* https://websiteforstudents.com/installing-the-latest-flash-player-on-ubuntu-17-10/
```bash
sudo add-apt-repository "deb http://archive.canonical.com/ $(lsb_release -sc) partner"
sudo apt update
sudo apt install adobe-flashplugin browser-plugin-freshplayer-pepperflash
```


## System Sensor monitors
* https://help.ubuntu.com/community/SensorInstallHowto
```bash
sudo apt install lm-sensors
sudo sensors-detect
sudo service kmod start
watch sensors
man sensors.conf
#
sudo apt install psensor
#
```


## Hardware Info Utilities
* http://hardinfo.org/
* http://goodies.xfce.org/

## BLE connectivity
* Sensortag command line tool for Python Bluetooth Low Energy access

## Games for Ubuntu
* Pocket Tank
* Scorched3D
* Wormux
* Atomic Tanks
* Xscorch
```bash
sudo apt install scorched3d
```


## Diff and Merge Tools for Ubuntu
- https://askubuntu.com/questions/2946/what-are-some-good-gui-diff-and-merge-applications-available-for-ubuntu
- https://www.slant.co/topics/5882/~linux-diff-tools
- https://www.linuxlinks.com/difftools/

* Diffuse -	Tool for merging and comparing text files
* [Meld](http://meldmerge.org/) - Diff viewer and merge tool for GNOME
	- Installations:
	- https://www.linuxhelp.com/how-to-install-meld-tool-in-ubuntu/
```bash
sudo apt install meld
```
* xxdiff - File and directories comparator and merge tool
* KDiff3	- Text difference analyzer for up to 3 input files
* Kompare	- KDE diff tool
* DiffMerge - 	Visually compare and merge files
* vimdiff
* GNU Diffutils (diff)
* P4Merge
* tkdiff - https://packages.ubuntu.com/trusty/tkdiff
	- `sudo apt install tkcvs`

* Get ubuntu version and code name
```bash
lsb_release -sc
#bionic
lsb_release -sr
#18.04
```

## Connect to VPN
```bash
sudo -E apt -q -y install openvpn
#
cd $HOME/Documents/bmangal/vpn
sudo openvpn --config fw-udp-1194-bhaskar.ovpn
```

dconf-editor

/org/gnome/desktop/interface/can-change-accels

make it true

killall nautilus && UBUNTU_MENUPROXY= nautilus 

http://tipsonubuntu.com/2018/04/22/re-enable-new-document-option-ubuntu-18-04/
https://itsfoss.com/add-new-document-option/

https://linuxconfig.org/how-to-create-desktop-shortcut-launcher-on-ubuntu-18-04-bionic-beaver-linux

* Enabe New Document Option
```bash
touch ~/Templates/Empty\ Document
```

## Student-Teacher, Remote Access and Sharing
* https://www.fractuslearning.com/tools-student-teacher-communication/
* https://www.makeuseof.com/tag/12-excellent-free-screen-sharing-and-remote-access-tools-you-havent-heard-of-yet/
* join.me
* https://openmeetings.apache.org/downloads.html
* https://www.linux.com/learn/using-screen-remote-interaction

* https://discoverpraxis.com/

## ssh
* https://stackoverflow.com/questions/9299651/git-says-warning-permanently-added-to-the-list-of-known-hosts
```bash
**Known Hosts added here**
~/.ssh/known_hosts
#
**ssh config**
~/.ssh/config
#
-o "UserKnownHostsFile /dev/null"
#
ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null user@host
```

## ffmpeg

https://superuser.com/questions/525249/convert-avi-xvid-to-mp4-h-264-keeping-the-same-quality#525253

* convert `avi` to `mp4`
```bash
ffmpeg -i input.avi -c:v libx264 -crf 19 -preset slow -c:a aac -b:a 192k -ac 2 out.mp4
```

**checking version of installed softwares**
* https://tech.amikelive.com/node-841/command-cheatsheet-checking-versions-of-installed-software-libraries-tools-for-deep-learning-on-ubuntu-16-04/#more-841

## Encrypting Storage Drives
* https://www.howtogeek.com/115955/how-to-quickly-encrypt-removable-storage-devices-with-ubuntu/
* https://askubuntu.com/questions/500981/how-to-encrypt-external-devices


**LUKS (Linux Unified Key Setup) encryption**
Ubuntu’s Disk Utility uses LUKS (Linux Unified Key Setup) encryption, which may not be compatible with other operating systems. However, the drive will be plug-and-play with any Linux system running the GNOME desktop.
```bash
sudo apt install cryptsetup
```


**How to use WD “My Passport” with Ubuntu Linux**
https://community.wd.com/t/how-to-use-wd-my-passport-with-ubuntu-linux/9115
https://www.quora.com/Is-the-WD-Passport-hard-disk-compatible-with-Linux-OS
https://www.quora.com/Is-the-WD-Passport-hard-disk-compatible-with-Ubuntu
https://www.youtube.com/watch?v=lCshVeh0Prg


sudo apt-get install guvcview

The following additional packages will be installed:
  libguvcview-2.0-2 libwebcam0 uvcdynctrl uvcdynctrl-data


http://www.linux-commands-examples.com/uvcdynctrl
https://support.lenovo.com/in/en/solutions/ht072130


http://derekmolloy.ie/kernel-gpio-programming-buttons-and-leds/
https://fossbytes.com/dont-put-tape-on-your-webcam-this-app-alerts-you-when-someone-uses-your-webcam/
http://www.techytalk.info/webcam-settings-control-ubuntu-linux/


## Technical Events

**Dec 2018**

* https://www.eventbrite.com/e/free-seminar-on-artificial-intelligence-tickets-53001882056?aff=ebdssbcitybrowse
* https://www.eventshigh.com/bangalore/technology
* http://ieeebangalore.org/


Live in Nature. Do Yoga. Learn to Code. Code for India.

https://www.switchup.org/rankings/best-coding-bootcamps