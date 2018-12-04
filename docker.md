---
Title: Docker
Decription: Docker
Author: Bhaskar Mangal
Date: 25th Apr 2018
Tags: Docker
---

**Table of Contents**
* TOC
{:toc}


## Docker
- https://www.docker.com/what-docker
- https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/
- http://www.channelfutures.com/open-source/why-docker-so-popular-explaining-rise-containers-and-docker

**From Virtual Machine to Container**

**Why Docker is darn Popular**
- https://www.zdnet.com/article/what-is-docker-and-why-is-it-so-darn-popular/

**What is Docker**
- https://github.com/floydhub/dl-docker#what-is-docker
- https://www.docker.com/what-docker

### Docker CE
Docker Community Edition (CE) is ideal for developers and small teams looking to get started with Docker and experimenting with container-based apps. Docker CE has three types of update channels, stable, test, and nightly
The Docker CE package is now called docker-ce.
For Ubuntu 16.04 and higher, the Linux kernel includes support for OverlayFS, and Docker CE uses the overlay2 storage driver by default. If you need to use aufs instead, you need to configure it manually.

**Installation**
- https://docs.docker.com/install/linux/docker-ce/ubuntu/#prerequisites
- https://docs.docker.com/install/linux/docker-ce/ubuntu/#set-up-the-repository
- Install using the repository - Before you install Docker CE for the first time on a new host machine, you need to set up the Docker repository. Afterward, you can install and update Docker from the repository
  ```bash
  ## uninstall
  sudo apt-get remove docker docker-engine docker.io
  sudo apt-get update
  ## Install packages to allow apt to use a repository over HTTPS:
  sudo apt-get install \
      apt-transport-https \
      ca-certificates \
      curl \
      software-properties-common

  ## Add Docker’s official GPG key
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  #
  ## Verify that you now have the key with the fingerprint 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88, by searching for the last 8 characters of the fingerprint.
  sudo apt-key fingerprint 0EBFCD88
  #
  ## Use the following command to set up the stable repository. You always need the stable repository, even if you want to install builds from the edge or test repositories as well.
  sudo add-apt-repository \
     "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
     $(lsb_release -cs) \
     stable"
  sudo apt-get update
  #
  ## List the versions available in your repo
  apt-cache madison docker-ce
  ##  Install a specific version by its fully qualified package name, which is package name (docker-ce) “=” version string (2nd column), for example, docker-ce=18.03.0~ce-0~ubuntu.
  # sudo apt-get install docker-ce=<VERSION>
  #
  ##  installs the highest possible version
  sudo apt-get install docker-ce
  #
  ## Verify that Docker CE is installed correctly by running the hello-world image
  sudo docker run hello-world
  ```
**Configuration as non-root**
* https://docs.docker.com/install/linux/linux-postinstall/
* If you don’t want to preface the docker command with sudo, create a Unix group called docker and add users to it. When the Docker daemon starts, it creates a Unix socket accessible by members of the docker group.
  ```bash
  sudo groupadd docker
  sudo usermod -aG docker $USER
  #
  ## verify
  docker run hello-world
  ```
Docker Community Edition (CE) is ideal for developers and small teams looking to get started with Docker and experimenting with container-based apps. Docker CE has three types of update channels, stable, test, and nightly:

Stable gives you latest releases for general availability.
Test gives pre-releases that are ready for testing before general availability.
Nightly gives you latest builds of work in progress for the next major release.

* Docker uses its own images. The images are created by a script that includes every step of the installation from a bare server. 

## Moby
- https://mobyproject.org/

Moby is an open framework created by Docker to assemble specialized container systems without reinventing the wheel. It provides a “lego set” of dozens of standard components and a framework for assembling them into custom platforms. At the core of Moby is a framework to assemble specialized container systems.

## FAQs
* http://blog.thoward37.me/articles/where-are-docker-images-stored/
```bash
sudo docker images
sudo cat /var/lib/docker/image/overlay2/repositories.json
```



web server
database
messaging
orchestration


DockerFile -> Image (template) -> Container