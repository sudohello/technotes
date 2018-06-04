/*
Title: Hardware Configuration
Decription: Hardware Configuration
Author: Bhaskar Mangal
Date: 11th-Feb-2018
Tags: Hardware Configuration
*/

# Hardware Configuration
Assembling decent system for Multi purpose:
* Computer Vision and Image Processing
* Machine Learning
* Deep Learning
* 3D GIS - Photogrammetry, Point Cloud, LiDAR, 3D Modelling
* Data Analysis, Data Visualization
* VR/AR
* VFX

## Building System Summary
* Final build requirements
	- understanding and selection of different PC components requried
	- power requriements, system parts compatibility
	- exterts feedback/review on configuration
	- market availability, local vendor support
	- choose the lower budget of the possible: Motherboard, PSU, Graphics Card, Monitor, CPU Cooler
* Configuration selection online tools
	- https://pcpartpicker.com/

## My Builds
https://pcpartpicker.com/list/G6Gp9J
https://pcpartpicker.com/list/fVzbtg

## Initially Shortlisted Components
**CPU**
* Intel - Core i7-7700K 4.2GHz Quad-Core Processor - BX80677I77700K
* Intel - Core i7-8700K
**CPU Cooler**
* CRYORIG - H7 49.0 CFM CPU Cooler
**Graphics Card**
* Zotac - GeForce GTX 1080 Ti 11GB AMP Extreme - ZT-P10810C-10P
* Zotac - GeForce GTX 1080 Ti 11GB AMP Edition - ZT-P10810D-10P
ZT-P10810**C**-10P / ZT-P10810**D**-10P / ZT-P10810**F**-10P
**Cabinet**
* Cooler Master - MasterBox Lite 5 RGB ATX Mid Tower Case
**Motherboard**
* Gigabyte - GA-Z270X-Gaming 7 ATX LGA1151 Motherboard - GA-Z270X-Gaming 7
* Gigabyte - GA-Z270X-Gaming 9 EATX LGA1151 Motherboard
**RAM**
* Corsair - Vengeance LPX 16GB (1 x 16GB) DDR4-3000 Memory
**HDD**
* Seagate - Barracuda 2TB 3.5" 7200RPM Internal Hard Drive
**SDD**
* Samsung 960 Evo NVMe PCIe M.2 250GB
**PSU [ 750W 80+ Gold Certified Fully-Modular ATX ]**
* Cooler Master - 750W 80+ Gold Certified Fully-Modular ATX Power Supply - RS750-AFBAG1-US
**Monitor [ minimum 1920x1080 ]**
* 1 x Acer - GN246HL 24.0" 1920x1080 144Hz Monitor
**Optical Drive**
* DVD RW
**OS:**
* Microsoft - Windows 10 Pro OEM 64-bit

* H270 vs Z270
* Aorus Z370 Gaming 7 
* Asus - STRIX Z270-E GAMING ATX LGA1151 Motherboard
* gigabyte z270x aorus gaming 5
* Motherboard Gigabyte GA-Z270- Gaming 3

https://www.gigabyte.com/Motherboard/GA-Z270-Gaming-3-rev-10#kf
http://www.trustedreviews.com/reviews/gigabyte-ga-z270-gaming-k3
https://www.pcper.com/reviews/Motherboards/ASUS-Strix-Z270E-Gaming-Motherboard-Review
https://www.asus.com/in/Motherboards/ROG-STRIX-Z270E-GAMING/

**Key points**
- The form factor, chipset, connectivity and price are the key attributes when picking a motherboard
- The physical size of the board
- how many memory sockets are board includes
- how fast the memory can go
- right storage connections for the SSDs and hard disks you want to install.
- PCI-Express sockets – some motherboards include full-length x16 slots that only run at 4x speed, which is no good if you want to run dual-graphics. And make sure you have enough PCI-Express x1 connectors for expansion cards

## Building Deep Learning Machine, Computer Vision
- https://blog.prolego.io/build-your-1st-deep-learning-rig-6f749f63798d
- https://medium.com/mlreview/choosing-components-for-personal-deep-learning-machine-56bae813e34a
- https://github.com/charlesq34/DIY-Deep-Learning-Workstation
- https://medium.com/@sanzgiri/my-new-deep-learning-rig-from-costco-62ceac7d48fa
- https://medium.com/@SocraticDatum/getting-started-with-gpu-driven-deep-learning-part-1-building-a-machine-d24a3ed1ab1e
- https://www.slideshare.net/PetteriTeikariPhD/deep-learning-workstation
- https://www.quora.com/Ill-be-using-my-computer-for-heavy-computation-computer-vision-algorithms-training-and-neural-nets-What-would-be-a-good-configuration-for-a-PC-laptop
- https://blog.slavv.com/picking-a-gpu-for-deep-learning-3d4795c273b9
- https://medium.com/mlreview/choosing-components-for-personal-deep-learning-machine-56bae813e34a

I use to work with 13Mpx to 6K, 16b raw images or video sequences. Here are the specifications I recommend for such work:
* > 16Gb RAM: it will be really important in order to be able to process a lot of data simultaneously
* Big storage space, with a size depending on what you have to store. It might be located on a shared network. My experience showed me that unless you write a lot of temporary data, SSD disk are not really useful to improve performance.
* Multi-core processor: that is important if you want to used OpenMP and to process easily some of your heaviest algorithms on several threads.
* The GPU is not really important. You just have to pick a chipset that support your favorite parallel computing platform (CUDA, OpenCL...).

That seem to be the minimum requirements in order to work with a lot of images. Sometimes, when I need to process a lot of images with very complex algorithm destined to be hard coded on an ASIC chip, I need more power. Therefore I send jobs on about ten computers all night and get the resulting images the next morning.


- https://www.quora.com/What-laptop-computer-should-I-purchase-for-deep-learning-How-much-will-it-cost

So laptop wise I would find the cheapest nvidia gtx 1080 laptop

However, if you want to train lots of small networks, or do some basic training before deploying your training script on a heavy machine, and are hell bent on buying a laptop for training, I’d suggest you buy a gaming laptop.

Asus and Acer have good options here. You can run Linux on it like a pro.
These have decent GPUs, and give you good performance for training small networks.
This is more convenient than setting up an external GPU on another laptop.


**Deep Learning Computer Configuration**
- https://towardsdatascience.com/build-a-deep-learning-rig-for-800-4434e21a424f
- https://medium.com/@saxenarohan97/semantic-segmentation-of-urban-street-scenes-in-mathematica-7d0fac13f3cd

## Systems of following configuration
1. i7 8th Generation minimum
2. 1x16 GB RAM module (expandable to 64 GB), No of RAM Slots (Minimum 4 Slots)
3. 2 TB HDD, 7200 RPM
4. 250 GB SSD, M.2 evo
5. Nvidia GTX 1080 / Nvidia GTX 1080 TI
6. No of PCIe Slots ( Minimum 2 Slots ), No. of PCIe lanes
7. SSD and SATA Slots (if you is concerned)
8. Thunderbolt 3.0 support

- https://www.mdcomputers.in/gtx-1080-ti

**Mobtherboard: Things to Keep in Mind:**
- Form Factor (i.e ATX, Micro ATX, EATX etc..)
- No of PCIe Slots ( Minimum 2 Slots)
- Maximum RAM Supported ( 64 GB Preferred)
- No of RAM Slots (Minimum 4 Slots)
- SSD and SATA Slots (if you is concerned)
- Have a motherboard with PCIe 3.0

**GPU**
- Ideally a GPU, to perform at its full capacity requires 16 PCI-e Lanes.

**CPU**
- For Deep learning applications, As mentioned earlier, The CPU is responsible mainly for the data processing and communicating with GPU.
- Hence, The number of cores and threads per core is important if we want to parallelize all that data preparation.
- It is advised to choose a multi core system (Preferably 4 Cores)to handle these tasks.
- Things to Keep in Mind:
	* Socket Type
	* No of Cores
	* Cost
	* make sure that your processor actually supports PCIe 3.0 if you have a motherboard with PCIe 3.0

**RAM, RAM Clock speed**
- For Deep learning applications it is suggested to have a minimum of 16GB memory (Jeremy Howard Advises to get 32GB). 
- Regarding the Clock, The higher the better. It ideally signifies the Speed — Access Time but a minimum of 2400 MHz is advised.

**Storage**
- https://gadgets.ndtv.com/laptops/reviews/nvidia-geforce-gtx-1080-ti-founders-edition-review-1668021
- https://gamefaqs.gamespot.com/boards/916373-pc/74658289
- SSD — Datasets in use + OS (Costly! Min: 128 GB Recommended)
- HDD — Misc User Data (Cheaper! Min: 2 TB Recommended 7200RPM)

**PSU - Power Supply Unit**

## Mobos (Motherboards)
- https://www.gigabyte.com/Motherboard/GA-Z270X-Gaming-9-rev-10#kf

**ASUS PRIME Z270-A LGA1151**
- https://www.asus.com/in/Motherboards/PRIME-Z270-A/specifications/

**Thunderbold**
- https://thunderbolttechnology.net/sites/default/files/Thunderbolt3_TechBrief_FINAL.pdf
- https://en.wikipedia.org/wiki/Thunderbolt_(interface)

**Overclocking**
- https://www.hardocp.com/article/2017/01/03/gigabyte_z270x_gaming_7_lga_1151_motherboard_review/7

**Asus Maximus IX Hero, Gigabyte Z270 Gaming 7, and MSI Z270 Gaming M7,**
https://www.pcgamer.com/the-best-z270-motherboard/
http://gistgear.com/Motherboards_Gaming_z270_1151.aspx

## PCIe vs Thunderbolt
http://www.tested.com/tech/457440-theoretical-vs-actual-bandwidth-pci-express-and-thunderbolt/
1. **PCIe - PCI Express**
  - what exactly does it mean when you have a PCIe 2.0 x8 connection?
  - And does it make a difference whether your connection is x8 or x16?
  - PCIe slots of different physical sizes and also different PCIe generations.

* A physical PCIe x16 slot can accommodate a x1, x4, x8, or x16 card, and can run a x16 card at x16, x8, x4, or x1.
* A PCIe x4 slot can accommodate a x1 or x4 card but cannot fit a x16 card. 

**What is PCIe**

A PCIe connection consists of one or more data-transmission lanes, connected serially. Each lane consists of two pairs of wires, one for receiving and one for transmitting. You can have one, four, eight, or sixteen lanes in a single consumer PCIe slot--denoted as x1, x4, x8, or x16. Each lane is an independent connection between the PCI controller and the expansion card, and bandwidth scales linearly, so an eight-lane connection will have twice the bandwidth of a four-lane connection. This helps avoid bottlenecks between, say, the CPU and the graphics card. If you need more bandwidth, just use more lanes.

Gigatransfers per second (GT/s)

**Maximum Theoritical PCIe x.x lane throughput**
* A single PCIe 1.0 (or 1.1) lane can carry up to 2.5 (GT/s) in each direction simultaneously.
* For PCIe 2.0, that increases to 5GT/s
* A single PCIe 3.0 lane can carry 8GT/s.

**After overhead, the maximum per-lane data rate**
* PCIe 1.0 is eighty percent of 2.5GT/s. That gives us two gigabits per second, or 250MB/s (remember, eight bits to a byte). The PCIe interface is bidirectional, so that's 250MB/s in each direction, per lane.
* PCIe 2.0 doubles the per-lane throughput to 5GT/s, which gives us 500MB/s of actual data transfer per lane.
* PCIe 3.0 lane, at 8GT/s, can send 985MB/s. That's not quite twice 500MB/s, but it's close enough for marketing purposes.

**Encoding**
- PCIe 1.* and 2.0 use 8b/10b encoding (like SATA does),  they lose 20 percent of their theoretical bandwidth to overhead
- PCIe 3.0 and above use a more efficient encoding scheme called 128b/130b, so the overhead is much less--only 1.54 percent

- What that means is that a PCIe 3.0 x4 connection (3.94GB/s) should have nearly the same bandwidth as PCIe 1.1 x16, or PCIe 2.0 x8 (both 4GB/s)
- Modern GPUs use a x16 PCIe 2.0 or 3.0 interface. That doesn't mean they always run at x16 speed, though.

Many motherboards have multiple physical x16 slots, but a smaller number of actual of PCIe lanes available
- On a Z87 (Haswell) or Z77 (Ivy Bridge) desktop, the CPU has 16 PCIe 3.0 lanes.
- Intel chipsets have an additional eight PCIe 2.0 lanes, but those are typically used for sound cards, RAID cards, and so forth.

2. DDR3 vs DDR4
3. PSU

* make sure that your processor actually supports PCIe 3.0 if you have a motherboard with PCIe 3.0.

**Thunderbolt**
Thunderbolt is a data transfer interface that can pass through both PCI Express and DisplayPort signals, depending on what it is plugged into. 
A Thunderbolt controller consists of two bidirectional data channels, with each channel containing an input and an output lane. The Thunderbolt chips on each end of the cable take in both DisplayPort 1.1a and a four-lane PCIe 2.0 bus. Each channel is independent, and can either carry DisplayPort or PCIe, but not both. Each direction in each channel has a theoretical maximum throughput of 10Gbps--the same as two PCIe 2.0 lanes.

so the maximum theoretical throughput of a single Thunderbolt channel is 1GB/s in each direction. 

## PCIe Lanes

Your m.2 drive will use the chipset lanes and will not be handicapped at all.  Your GPU can run at 16x.  Even if for some reason it couldn't (which it can) 8x is more than enough for your GPU.  There is no way a 1070 can saturate 8x PCIe 3.0.

**Intel 8700**
* You get 16 full-speed PCIe lanes from the CPU:
* Paired with a Z370 board, you also get a further 24 PCIe lanes from the chipset
* Note that the chipset lanes all share a higher latency ~x4 PCIe 3.0 link to the CPU. So although it's great for things like networking and one or two high speed NVMe drives, those chipset lanes aren't optimal for anything ultra-performance sensitive like GPUs.

**Intel 8700K**
* PCI Express Revision 3.0
* PCI Express Configurations ‡ Up to 1x16, 2x8, 1x8+2x4
* Max # of PCI Express Lanes 16

**Maximum Theoritical PCIe x.x lane throughput**

A single PCIe 1.0 (or 1.1) lane can carry up to 2.5 (GT/s) in each direction simultaneously.
For PCIe 2.0, that increases to 5GT/s
A single PCIe 3.0 lane can carry 8GT/s.


**After overhead, the maximum per-lane data rate**

PCIe 1.0 is eighty percent of 2.5GT/s. That gives us two gigabits per second, or 250MB/s (remember, eight bits to a byte). The PCIe interface is bidirectional, so that's 250MB/s in each direction, per lane.
PCIe 2.0 doubles the per-lane throughput to 5GT/s, which gives us 500MB/s of actual data transfer per lane.
PCIe 3.0 lane, at 8GT/s, can send 985MB/s. That's not quite twice 500MB/s, but it's close enough for marketing purposes.

**[What-is-the-difference-between-the-PCIe-lanes-from-the-CPU-and-the-ones-from-the-motherboard-Is-there-a-performance-difference](https://www.quora.com/What-is-the-difference-between-the-PCIe-lanes-from-the-CPU-and-the-ones-from-the-motherboard-Is-there-a-performance-difference)**
- The pcie lanes for the cpu are the maximum amount of pcie lanes supported on the motherboard. The long pcie slots on the motherboard are x16, and the only pcie devices (with exceptions) that use this amount of bandwidth are gpu’s. So a single gpu takes up 16 lanes, if your cpu is a 28 lane then you now have 12 lanes left.

* **Have you heard of m.2, u.2, and esata?**
	- They all use x4 pcie 3.0 lanes
	- So if you then have two m.2 drives and one u.2 drive on top of your graphics card you are now using 28 pcie lanes, which is the max the cpu can handle.

* **Well what if you add more pcie devices?**
	- The motherboard will automatically restrict the bandwidth for some devices (in the motherboard manual it will tell you which ports will be effected and when).
	- This means that if you have two graphics cards with a 28 lane cpu, since this takes up 32 lanes, the motherboard will only allow x8 bandwidth to both cards.
	- This is a problem with newer cards since they need the full x16 bandwidth, and is partly the reason people are saying “sli is dying”. It doesn’t effect performance a lot, but enough that if you’re doing sli you want to make sure you have a 40 lane cpu.

* the pcie lanes for the chipset are for lower bandwidth devices, such as usb ports and audio cards
* This shows how the chipset pcie lanes get 8gbs and 6gbs
* while, the cpu pcie x16 lanes get 15gbps. This is because everything using cpu pcie lanes are devices that interact directly with the cpu no matter what. 
* The chipset lanes are all devices that can interact with the cpu sometimes, but also interact with the storage and external devices.
* So yes there is a perfomance difference, the cpu lanes get more priority and bandwidth, and the chipset lanes are lower bandwidth.
* Chipset lanes are typically used for things like M.2 storage, capture cards, or other peripherals that use pcie lanes
* For the DMI ( Direct Media Interface ), with 3 version the chipset will support DDR4, more pcie lanes, and more USB3.0 etc. more info https://en.wikipedia.org/wiki/Direct_Media_Interface


**If we add single GPU, does it use PCI E lanes from the chipset or from the processor?**
- the GPU, which can only be plugged in your motherboard's single PCIe x16 slot, uses the x16 lanes coming from the processor.

https://www.bit-tech.net/reviews/tech/cpus/intel-core-i7-8700k-coffee-lake-and-z370-chipset-review/2/


## GPU/Graphics Card
Zotac Nvidia GTX 1080 Ti 11GB
http://www.pc-specs.com/gpu/Nvidia/1000_Series/GeForce_GTX_1080_Ti_Zotac_AMP!/3874/Compatible_Motherboards
ZOTAC ZT-P10810F-10P GeForce GTX 1080 Ti AMP Extreme Core Edition 11GB GDDR5X 352-bit Gaming Graphics Card VR Ready

https://www.zotac.com/us/product/graphics_card/zotac-geforce-gtx-1080-ti-amp-extreme-core-edition
http://www.ign.com/articles/the-best-geforce-gtx-1080-ti

http://www.tomshardware.com/answers/id-3485339/7700-7700k-gtx-1080.html

GPU GeForce® GTX 1080 Ti
CUDA cores 3584
Video Memory 11GB GDDR5X
Memory Bus 352-bit
Engine Clock Base: 1645 MHz 
Boost: 1759 MHz
Memory Clock 11.2 GHz
PCI Express 3.0
Display Outputs 3 x DisplayPort 1.4 
HDMI 2.0b 
DL-DVI-D 
HDCP Support Yes
Multi Display Capability Quad Display
Recommended Power Supply 600W
Power Consumption 320W
Power Input Dual 8-pin
DirectX 12 API feature level 12_1
OpenGL 4.5
Cooling 3 x 90mm fans
Slot Size 2.5-Slot
SLI Yes, SLI HB Bridge Supported
Supported OS Windows 10 / 8 / 7
Card Length 325 x 148 x 56.6mm (12.8 x 5.83 x 2.23in)
Accessories 2 x Dual 6-pin to 8-pin mesh wrapped power adapter 
Driver disk 
User Manual


### GPU v/s TPU
- https://cloud.google.com/blog/big-data/2017/05/an-in-depth-look-at-googles-first-tensor-processing-unit-tpu

### Founders Edition V/s After Market
- https://steamcommunity.com/discussions/forum/11/350543738456345935/

**Aftermarket:**
- Reduce Noise.
- Better Cooling.
- Better overclocking. *optional*
- Cost less or about the same.
- Comes in many themes depending on the brand you pick.

**Founder:**
- More Noise, due it chamber and one small fan.
- Can overheat which cause throttling, due it chamber and one small fan.
- Overclocking. *optional*
- Cost more or about the same.
- Comes in only one theme.

**842735-which-1080-ti-is-better-strix-oc-vs-aorus-xtreme**
https://www.mdcomputers.in/index.php?route=product/search&search=gtx%201080%20ti&description=true
https://linustechtips.com/main/topic/842735-which-1080-ti-is-better-strix-oc-vs-aorus-xtreme/

* different coolers, PCBs and binning
* Both cards are "binned" in the sense that they're guaranteed to run at a certain clockspeed out of the box but GPU Boost 3.0 mostly negates that. Overclocking potential will always be dependent on the silicon lottery.


## CPU/Processor
http://www.cpu-world.com/Compare/490/Intel_Core_i7_i7-7700_vs_Intel_Xeon_E3-1240L_v5.html
https://browser.geekbench.com/processors/1792

**Overclocking**
https://communities.intel.com/thread/113498

**Overclocking default supported Memory bandwidth**
https://linustechtips.com/main/topic/770398-does-intel-core-i7-7700k-support-more-than-ddr4-2400/

**Intel Core i7 vs Xeon**
So, should you go with a Core i7 or Xeon processor? It really comes down to what you are using your system for. If you are planning on using your system for gaming, home or business use, the i7 will be the better option for you. However, if you are looking for a high-powered system to run video rendering or 3D software, you may want to look into getting a Xeon.
https://www.avadirect.com/blog/intel-core-i7-vs-xeon/
http://bwindia.net/content/bupc-intel-e3-v5-range-xeon-processor-family

1. i7 7700
Intel - Core i7-7700 3.6GHz Quad-Core Processor

https://www.intel.in/content/www/in/en/products/processors/core/i7-processors/i7-7700.html
DDR4-2133/2400, DDR3L-1333/1600 @ 1.35V
Max # of PCI Express Lanes 16
PCI Express Configurations ‡ Up to 1x16, 2x8, 1x8+2x4
PCI Express Revision 3.0

## RAM

**What is ram module**
A memory module is another name for a RAM chip. It is often used as a general term used to describe SIMM, DIMM, and SO-DIMM memory. While there are several different types of memory modules available, they all serve the same purpose, which is to store temporary data while the computer is running.Feb 11, 2008
Memory Module Definition - The Tech Terms Computer Dictionary
- https://techterms.com/definition/memorymodule

This is because most computers only accept one type of memory. Therefore, if you decide to upgrade you computer's RAM, make sure the memory modules you buy are compatible with your machine.
- https://www.kingston.com/en/memory/resources/ddr3_1600

## HDD,SSD,SsHD

**Hard Disk - HDD**
* What is better a Sshd or HDD?
SSHD stand for solid-state hybrid drive. It's a traditional hard disk with a small amount of solid-state storage built in, typically 8GB or so. The drive appears as a single device to Windows (or any other operating system), and a controller chip decides which data is stored on the SSD and what's left on the HDD.Apr 10, 2017

**SSD vs SSHD**
Which is the best hard drive to buy? - Tech Advisor
	- https://www.techadvisor.co.uk/buying-advice/pc-upgrades/ssd-vs-sshd-3520515/

**HDD Cache**
WHAT IS HARD DRIVE CACHE AND WHAT DOES IT DO?
https://www.pcmech.com/article/what-is-hard-drive-cache-and-what-does-it-do/
main hard drive specs, like capacity, read/write speeds, and platter rotation speeds

Hard drive cache is often known as the disk buffer. By that name, its purpose becomes a little more clear. It acts as temporary memory for the hard drive as it reads and writes data to the permanent storage on the platters.

You can think of a hard drive’s cache as being like RAM specifically for the hard drive.

**SDD**
 SATA 850 Evo
 Samsung 960 Evo 1TB - This is one of the fastest SSDs on the market.
 EVGA 850G2 

## Motherboards (mobos)
** Hardware Guides for Deep Learning
http://timdettmers.com/2015/03/09/deep-learning-hardware-guide/

ASUS ROG MAXIMUS VIII IMPACT LGA1151 Mini ITX DDR4 Motherboards

- H270 vs Z270
https://www.pugetsystems.com/labs/articles/Z270-H270-Q270-Q250-B250---What-is-the-Difference-876/
- z270 supports full overclocking, maximum PCIe lanes


## PSU - Power supply unit
- PCIe connectors of your PSU are able to support a 8pin+6pin connector with one cable.
- You can calculate the required watts by adding up the watt of your CPU and GPUs with an additional 100-300 watts for other components and as a buffer for power spikes.
- Another important thing is to buy a PSU with high power efficiency rating – especially if you run many GPUs and will run them for a longer time.
- Your motherboard should have enough PCIe ports to support the number of GPUs you want to run (usually limited to four GPUs, even if you have more PCIe slots); remember that most GPUs have a width of two PCIe slots, so you will need 7 slots to run 4 GPUs 
- PCIe 2.0 is okay for a single GPU, but PCIe 3.0 is quite cost efficient with respect to cost-performance even for a single GPU; for multiple GPUs always buy PCIe 3.0 boards which will be a boon when you do multi-GPU computing as the PCIe connection will be the bottleneck here.
- The motherboard choice is straightforward: Just pick a motherboard that supports the hardware components that you want.
- When you select a case, you should make sure that it supports full length GPUs that sit on top of your motherboard. Most cases support full length GPUs, but you should be suspicious if you buy a small case. Check its dimensions and specifications; you can also try a google image search of that model and see if you find pictures with GPUs in them.


EPS 8-pin power connectors

The RM850x and RM1000x are fully modular power supplies sporting an 80 PLUS Gold certification and 100% Japanese capacitors. The RM1000x in conjunction with the Noctua fans made for an incredibly quiet dual Xeon server and most of the time the power supply was in “Zero RPM Fan Mode” which was nice.

- http://www.guru3d.com/articles-pages/geforce-gtx-1080-ti-review,7.html
Here is Guru3D's power supply recommendation:

Nvidia GeForce GTX 1080 Ti  - On your average system the card requires you to have a 600~650 Watts power supply unit.
If you are going to overclock your GPU or processor, then we do recommend you purchase something with some more stamina. And remeber, a PSU is the most efficient at 50% load. So if you use 400 Watts on average (SLI), the most energy friendly powersupply would be an 800 Watt model. There are many good PSUs out there, please do have a look at our many PSU reviews as we have loads of recommended PSUs for you to check out in there.

**What could happen if your PSU can't cope with the load is:**
- Bad 3D performance
- Crashing games
- Spontaneous reset or imminent shutdown of the PC
- Freezing during gameplay
- PSU overload can cause it to break down

**What is Power Efficiency - 80+ certifications: Gold, Silver and Bronze**
- http://www.hardwaresecrets.com/understanding-the-80-plus-certification/
- http://www.corsair.com/en-eu/blog/2012/august/80-plus-platinum-what-does-it-mean-and-what-is-the-benefit-to-me
- http://www.hardwaresecrets.com/understanding-the-80-plus-certification/2/
 -https://www.neweggbusiness.com/smartbuyer/over-easy/power-supply-certification-mean/

The 80 PLUS program tests computer power supplies for efficiency at 20%, 50% and 100% loads. Initially, power supplies only needed to be 80% efficient to earn certification. Over the years as power supplies became more and more efficient, new standards such as Bronze, Silver, Gold, and Platinum were created.


**PCI-e Power - Does 6 + 2 Equal 8?**
- https://superuser.com/questions/992085/pci-e-power-does-6-2-equal-8
- http://www.playtool.com/pages/psuconnectors/connectors.html

**Fully Modular, Semi-modular, Non-modular**
- http://www.corsair.com/en-us/hx-series-hx750-750-watt-80-plus-platinum-certified-fully-modular-psu-na
- http://us.coolermaster.com/product/Detail/powersupply/series/v750.html

**Number of PINS**
one 6-pin and one 8-pin
https://forum-en.msi.com/index.php?topic=280978.0
When a video board says 8+6 for power requirements it means one 8-pin connector and one 6-pin connector from your power supply. Take on PCI-E 6+2 connector from your PSU and use it for the 8-pin connector on the video board. Take another 6+2 connector and only use the 6-pin part in the 6-pin socket on your video board. I hope I explained that well enough.

## Coolers, Cooling
- Cooling is important and it can be a significant bottleneck which reduces performance more than poor hardware choices do.
- You should be fine with a standard heat sink for your CPU, but what for your GPU you will need to make special considerations.
- Modern GPUs will increase their speed – and thus power consumption – up to their maximum when they run an algorithm, but as soon as the GPU hits a temperature barrier – often 80 °C – the GPU will decrease the speed so that the temperature threshold is not breached. This enables best performance while keeping your GPU safe from overheating.
- The easiest and most cost efficient work-around is to flash your GPU with a new BIOS which includes a new, more reasonable fan schedule which keeps your GPU cool and the noise levels at an acceptable threshold (if you use a server, you could crank the fan speed to maximum speed which is otherwise not really bearable on a noise level).
- You can also overclock your GPU memory with a few MHz (30-50) and this is very safe to do. The software for flashing BIO is a program designed for Windows, but you can use wine to call that program from your Linux/Unix OS.
- The other option is to use to set a configuration for your Xorg server (Ubuntu) where you set the option “coolbits”. This works very well for a single GPU, but if you have multiple GPUs where some of them are headless, i.e. they have no monitor attached to them, you have to emulate a monitor which is hard and hacky.

CPU cooler for 7700k, 8700K

**CRYORIG**
- https://www.kitguru.net/components/cooling/dominic-moass/cryorig-h7-air-cooler-review/
- http://www.pcgameware.co.uk/reviews/cpu-coolers/cryorig-h7-cpu-cooler-review/
CRYORIG - H7 49.0 CFM CPU Cooler
H45 Cooler
cpu cooler
CRYORIG - H7 49.0 CFM CPU Cooler
Cryorig H5 Universal, R1 Universal, or R1 Ultimate?
Dark Rock Pro 3
Scythe Mugen 5

**Noctua's NH-D15**
- http://www.tomshardware.com/answers/id-3337005/cpu-cooler-7700k.html
Noctua's NH-D15 Versus Five High End Closed Loop Liquid Coolers
- http://www.relaxedtech.com/reviews/noctua/nh-d15-versus-closed-loop-liquid-coolers/1
- http://www.relaxedtech.com/reviews/noctua/nh-d15/1

## Monitors
- 1920x1080 22 inch

## Cabinets/Cases
- http://www.coolermaster.com/case/mid-tower/masterbox-lite-5-rgb/
- https://www.techspot.com/products/cases/cooler-master-masterbox-lite-5.167026/
Cases:
Full tower - Corsair 780T
Mid tower - Corsair Crystal Series 570X RGB
ITX – Realan E-MINI series I5

## Keyboards

**Mechanical vs Rubber Dome**
- https://mechanicalkeyboards.com/define_mechanical_keyboard.php
- https://mechanicalkeyboards.com/learn.php
- https://en.wikipedia.org/wiki/Touch_typing

## Sound Card

## Wireless Network Card/ LAN Card

## Builds
**HTPC [ Home Theater Build ]**
https://mediaexperience.com/updated-htpc-recommendations/
In order to get the best audio quality, I chose a bit more expensive ASUS Maximus VIII Impact motherboard that has a dedicated sound card (SupremeFX). 

**Builds**
http://www.tomshardware.com/answers/id-3359396/opinion-build-7700k-1080.html

## Keywords
* Founder Edition
* After market - means, over clocking
* OC - Over clocking
* Mobos - Motherboard
* siliconlottery - https://siliconlottery.com/
* HEDT - High End Desktop
* DMI - direct media interface
	- DMI is the communication lane between the CPU and the Chipset/PCH.
* FSB - Front Side Bus
* QPI - Quick Path Interconnect
* TDP - Thermal Design Power
* HSIO - high-speed input-output

## other references
- http://cpu.userbenchmark.com/Compare/Intel-Core-i7-7700-vs-Intel-Core-i3-7100/3887vs3891

**Deliding Cooler**
https://www.pcgamer.com/meet-the-overclocker-who-made-delidding-your-cpu-idiot-proof/
https://www.tweaktown.com/guides/8039/cpu-deliding-quick-guide/index.html
https://www.ekwb.com/blog/what-is-delidding/

What is processor deliding, how does it benefit CPU overclocking and temperatures, how do you do, and what are the risks? Let's find out.

**deepfence**
https://deepfence.io/
https://www.sdxcentral.com/articles/news/ai-and-rules-drive-deepfence-app-focused-container-security/2018/02/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3B6oV4nCo0Txa0LDned7skHg%3D%3D

**Thunderbold**
https://thunderbolttechnology.net/sites/default/files/Thunderbolt3_TechBrief_FINAL.pdf
https://en.wikipedia.org/wiki/Thunderbolt_(interface)

**Overclocking**
https://www.hardocp.com/article/2017/01/03/gigabyte_z270x_gaming_7_lga_1151_motherboard_review/7