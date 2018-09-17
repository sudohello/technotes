---
Title: apt-get Errors
Decription: apt-get Errors
Author: Bhaskar Mangal
Date: 5 Jan 2017
Placing: 1
Tags: apt-get Errors
---

**Table of Contents**
* TOC
{:toc}


## Apt Get Errors
```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
```
W: GPG error: https://artifacts.elastic.co/packages/5.x/apt stable Release: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY D27D666CD88E42B4

https://askubuntu.com/questions/749241/problem-with-apt-get-update-some-index-files-failed-to-download


http://www.pcl-users.org/missing-package-for-Ubuntu-16-04-td4042009.html


Err:14 http://ppa.launchpad.net/v-launchpad-jochen-sprickerhof-de/pcl/ubuntu xenial/main amd64 Packages
  404  Not Found
Ign:15 http://ppa.launchpad.net/v-launchpad-jochen-sprickerhof-de/pcl/ubuntu xenial/main i386 Packages
Ign:17 http://ppa.launchpad.net/v-launchpad-jochen-sprickerhof-de/pcl/ubuntu xenial/main all Packages
Ign:19 http://ppa.launchpad.net/v-launchpad-jochen-sprickerhof-de/pcl/ubuntu xenial/main Translation-en_IN
Ign:22 http://ppa.launchpad.net/v-launchpad-jochen-sprickerhof-de/pcl/ubuntu xenial/main Translation-en
Ign:23 http://ppa.launchpad.net/v-launchpad-jochen-sprickerhof-de/pcl/ubuntu xenial/main amd64 DEP-11 Metadata
Ign:24 http://ppa.launchpad.net/v-launchpad-jochen-sprickerhof-de/pcl/ubuntu xenial/main DEP-11 64x64 Icons
Fetched 103 kB in 16s (6,253 B/s)
Reading package lists... Done
W: The repository 'http://ppa.launchpad.net/v-launchpad-jochen-sprickerhof-de/pcl/ubuntu xenial Release' does not have a Release file.
N: Data from such a repository can't be authenticated and is therefore potentially dangerous to use.
N: See apt-secure(8) manpage for repository creation and user configuration details.
E: Failed to fetch http://ppa.launchpad.net/v-launchpad-jochen-sprickerhof-de/pcl/ubuntu/dists/xenial/main/binary-amd64/Packages  404  Not Found
E: Some index files failed to download. They have been ignored, or old ones used instead.


https://askubuntu.com/questions/65911/how-can-i-fix-a-404-error-when-using-a-ppa-or-updating-my-package-lists
