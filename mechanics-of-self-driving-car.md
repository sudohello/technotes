---
Title: Mechanics of Self-Driving Car
Decription: Mechanics of Self-Driving Car
Author: Bhaskar Mangal
Date: 
Tags: Mechanics of Self-Driving Car
---


**Table of Contents**
* TOC
{:toc}


## Mechanics of Self-Driving Car

This section is the quest to understand and educate myself on the mechanics of self-driving cars, automobiles and related technologies.

The majority of self-driving vehicle control systems implement a deliberative architecture, meaning that they are capable of making intelligent decisions by 1) maintaining an internal map of their world and 2) using that map to find an optimal path to their destination that avoids obstacles (e.g. road structures, pedestrians and other vehicles) from a set of possible paths. Once the vehicle determines the best path to take, the decision is dissected into commands, which are fed to the vehicle’s actuators. These actuators control the vehicle’s steering, braking and throttle.

GPS estimates can be off by many meters due to signal delays caused by changes in the atmosphere and reflections off of buildings and surrounding terrain, and inertial navigation units accumulate position errors overtime. Therefore, **localization algorithms will often incorporate map or sensor data previously collected from the same location to reduce uncertainty**.

## Drive by wire (DbW)
Drive by wire, DbW, by-wire, Steer-by-wire, or x-by-wire technology in the automotive industry is the use of electrical or electro-mechanical systems for performing vehicle functions traditionally achieved by mechanical linkages.

## On-Board Diagnostic (OBD)

### What is OBD?

OBD stands for “On-Board Diagnostics.” It is a computer-based system originally designed to reduce emissions by monitoring the performance of major engine components.

A basic OBD system consists of an ECU (Electronic Control Unit), which uses input from various sensors (e.g., oxygen sensors) to control the actuators (e.g., fuel injectors) to get the desired performance. The “Check Engine” light, also known as the MIL (Malfunction Indicator Light), provides an early warning of malfunctions to the vehicle owner. A modern vehicle can support hundreds of parameters, which can be accessed via the DLC (Diagnostic Link Connector) using a device called a scan tool.

A new class of devices are being developed that capture your cars computer sensor data using your vehicles on-board diagnostic port (OBD II is available on cars built from 1996 on) and adds a layer of additional features on top.
There are two kinds of on-board diagnostic systems: OBD-I and OBD-II.

### What Data is Available from OBD?
* https://en.wikipedia.org/wiki/OBD-II_PIDs
* http://www.obdsol.com/knowledgebase/on-board-diagnostics/what-data-is-available-from-obd/

### What is an OBD Adapter?

### Choosing an OBD Adapter
* Cost
* Time to market
* Supported OBD protocols
* Physical size/form factor
* Connection type: USB, RS232, WiFi, Bluetooth, UART, etc
* Special features: upgradeable firmware, low current mode, enhanced commands

### What is controller area network (CAN)

With new technologies, products and inventions, many of the mechanical systems in an automobile were slowly being replaced by electronics systems, wherein one electronic device needs to communicate with others to operate.

- To address this, Robert Bosch in 1986, first released the new communication protocol called **CAN** (Controller Area Network), to enable coomucation between different electornic modules.
- It laid down the rules through which the various electronic devices can exchange information with each other over a common serial bus
- CAN provide a mechanism which is incorporated in the hardware and the software by which different electronic modules can communicate with each other using a common cable.
- Before CAN was introduced in the automobiles, each electronic device was connected to other device using the wires (point to point wiring) which worked fine, when the functions in the system were limited.
- Industries like Railway, Aircrafts, medical etc to adopt CAN protocol in their systems.
- Every electronic device (also known as the node) which needs to communicate using the CAN protocol is connected with each other via a common serial bus to transmit and receive messages.
- Node has
	- Host controller (ECU/MCU) 
	- CAN controller
		- CAN controller is a chip which can either be added separately or embedded inside the host controller of the node.
	- CAN transceiver
	- CAN does not follow the master-slave architecture which means every nodes has the access to read and write data on the CAN bus.
	- CAN is a message based protocol
		- Message is a packet of data which carries information
		-  In a message based protocol every message is identified by a predefined unique ID rather than the destination addresses
	- CAN uses the existing OSI reference model to transfer data among nodes connected in a network.
	- CAN facilitates multi-domain communication
	- The complexity of the node can range from a simple I/O device up to an embedded computer with a CAN interface and sophisticated software
	- The node may also be a gateway allowing a standard computer to communicate over a USB or Ethernet port to the devices on a CAN network.
	- CAN is a low-level protocol and does not support any security features intrinsically. There is also no encryption in standard CAN implementations, which leaves these networks open to man-in-the-middle packet interception. 

> electrical engineering convention that power sources are terminated at female connectors.
> In telecommunications and computer networks, multiplexing (sometimes contracted to muxing) is a method by which multiple analog or digital signals are combined into one signal over a shared medium.

Controller Area Network or CAN protocol is a method of communication between various electronic devices embedded in an automobile, like
* engine control unit
* active suspension
* antilock braking/ABS
* gear control
* lighting control
* air conditioning
* airbags
* spark ignition engine - engine control
* transmission control unit
	-  changes the ratio of gear automatically with the changing speed
* central locking
* cruise control
* electric power steering
* power windows
* doors
* mirror adjustment
* audio systems
* battery and recharging systems

**Domain**
Electronic devices implanted in a vehicle can be classified under different domain. It's a group of electronic devices that have almost similar requirements to work in the system, like:
- CD/DVD PLAYER, GPS system, monitors and displays etc. form a single domain.
- Air conditioning and climate control, dashboards, wipers, lights doors etc. form one domain

A subsystem may need to control actuators or receive feedback from sensors.

**Different Domains**
* Power Train - engine control
* Chassis - ABS, ASC
* Body - Dash board, Climate control, Wipers
* Telemetric -  CD/DVD player, for GPS Multimedia
* Passive Safety - ROllover sensors, Air bag system and belt pretensions

## Terms, Keywords, Definitions
* SDC - Self-Driving-Car
* SDV - Self-Driving-Vehicle
* ECU - Electronic Control Units
* DbW - Drive by Wire
* CAN - Controller Area Network
	* Controller Area Network or CAN protocol is a method of communication between various electronic devices embedded in an automobile
* Actuator
	* An actuator is a component of a machine that is responsible for moving or controlling a mechanism or system. An actuator requires a control signal and a source of energy. The control signal is relatively low energy and may be electric voltage or current, pneumatic or hydraulic pressure, or even human power. When the control signal is received, the actuator responds by converting the energy into mechanical motion. [Read more on Actuator here](https://en.wikipedia.org/wiki/Actuator)
* OBD - On-board Diagnostics
	* **On-board diagnostics** is an automotive term referring to a vehicle's self-diagnostic and reporting capability. OBD systems give the vehicle owner or repair technician access to the status of the various vehicle subsystems

## References
* https://www.wired.com/2015/04/cost-of-sensors-autonomous-cars/
* https://www.theguardian.com/technology/2016/may/26/self-driving-cars-whos-building-them-and-how-do-they-work
* https://twitter.com/hashtag/selfdriving
* https://medium.com/self-driving-cars/term-1-in-depth-on-udacitys-self-driving-car-curriculum-ffcf46af0c08

### DbW
* https://en.wikipedia.org/wiki/Drive_by_wire
* http://auto.howstuffworks.com/car-driving-safety/safety-regulatory-devices/drive-by-wire1.htm

### OBD
* http://www.team-bhp.com/forum/technical-stuff/144108-board-diagnostics-obd-dummies.html
* http://www.team-bhp.com/forum/technical-stuff/42229-techspec-understanding-board-diagnostics-also-known-ecu-ecm-ems.html
* http://www.archer-soft.com/en/blog/top-6-automotive-diagnostic-software
* https://www.dgtech.com/vsi-2534/
* https://en.wikipedia.org/wiki/On-board_diagnostics
* http://www.obdsol.com/knowledgebase/on-board-diagnostics
* https://en.wikipedia.org/wiki/OBD-II_PIDs
* http://www.obdsol.com/knowledgebase/on-board-diagnostics/what-data-is-available-from-obd/


#### OBD, CAN Bus for SelfDriving Car
* https://medium.com/@mslavescu/introduction-to-obd-ii-and-can-bus-for-self-driving-cars-6b9f9a2a8775
* https://medium.com/self-driving-cars/autonomous-security-564571bf6373
* https://en.wikipedia.org/wiki/CAN_bus
* https://www.engineersgarage.com/article/what-is-controller-area-network
* https://www.engineersgarage.com/articles/sensors
