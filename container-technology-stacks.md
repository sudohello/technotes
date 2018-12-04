---
Title: Container Technology Stack
Decription: Container Technology Stack
Author: Bhaskar Mangal
Date: 4th-Dec-2018
Last Updated: 4th-Dec-2018
Tags: Container Technology Stack
---

**Table of Contents**
* TOC
{:toc}


## Container Technology Stack

**VM vs Container**
* The key difference between containers and VMs is while the hypervisor abstracts an entire device, containers just abstract the operating system kernel.
* This, in turn, means one thing VM hypervisors can do that containers can't is to use different operating systems or kernels
* With Docker or other container technologies, all containers must use the same operating system and kernel.

### Docker
* [docker_the_end_of_virtualization - 22st-Feb-2018](https://www.theregister.co.uk/2018/02/22/docker_the_end_of_virtualization/)
* [what-is-docker-and-why-is-it-so-darn-popular - 21st-Mar-2018](https://www.zdnet.com/article/what-is-docker-and-why-is-it-so-darn-popular/)
* https://www.zdnet.com/article/docker-libcontainer-unifies-linux-container-powers/
* https://www.docker.com/docker-news-and-press/industry-leaders-unite-create-project-open-container-standards



* Founder: Docker founder ... Solomon Hykes
* Docker, however, is built on top of [LXC](https://linuxcontainers.org/). Like with any container technology, as far as the program is concerned, it has its own file system, storage, CPU, RAM, and so on. 
* you can run Docker containers on essentially any operating system or cloud. This gives it an advantage over the others


**Docker Tools**
* https://www.docker.com/community/open-source
* https://www.midvision.com/10-open-source-docker-tools-you-should-be-using/
* https://codecondo.com/orchestration-open-source-docker-tools/
* Orchestration Open Source Docker Tools


**Docker Alternatives**
* [CoreOS, now Red Hat's Rkt](https://coreos.com/rkt/)
* [LXD by Canonical](https://www.zdnet.com/article/ubuntu-lxd-not-a-docker-replacement-a-docker-enhancement/)


### Moby
* https://mobyproject.org/
* An open framework to assemble specialized container systems without reinventing the wheel.
* Moby is an open framework created by Docker to assemble specialized container systems without reinventing the wheel. It provides a “lego set” of dozens of standard components and a framework for assembling them into custom platforms.

## Container Orhestration
In the level above containers, container orchestration, Docker does has a serious competitor: Kubernetes.
* Like any other element of your IT infrastructure, containers need to be monitored and controlled. Otherwise, you literally have no idea what's running on your servers.

**cloud orchestration tools**
* https://insights.hpe.com/articles/the-basics-explaining-kubernetes-mesosphere-and-docker-swarm-1702.html
* Docker Swarm
* **Kubernetes**
* Mesosphere 


### Kubernetes


### Istio
* https://www.zdnet.com/article/beyond-kubernetes-istio-network-service-mesh/

First, Docker transformed how we ran applications. Then, Kubernetes changed how we managed containers. Now, the open-source project Istio is building on both to add a network service mesh.


## Microservices


## Cloud Cost Monitoring and Optimization
* [rightscale](https://www.rightscale.com/)

## [CNCF](https://www.cncf.io/)
CNCF is an open source software foundation dedicated to making cloud native computing universal and sustainable. Cloud native computing uses an open source software stack to deploy applications as microservices, packaging each part into its own container, and dynamically orchestrating those containers to optimize resource utilization. Cloud native technologies enable software developers to build great products faster.