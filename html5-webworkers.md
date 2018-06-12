/*
Title: Javascript Web workers, Web Sockets
Decription: Javascript
Author: Bhaskar Mangal
Date: 12th Jun 2018
Last Updated: 12th Jun 2018
Tags: Javascript Web workers, Web Sockets
*/

# Javascript Web workers
- HTML5 Web Workers provide background-processing capabilities to web applications and typically run on separate threads so that JavaScript applications using Web Workers can take advantage of multicore CPUs
- Separating long-running tasks into Web Workers also avoids the dreaded slow-script warnings
- Web Worker might use Web Sockets or Server-Sent Events to talk to the back-end server


## UX Motivations
Do not want certain tasks to interfere with the interactivity of the web page itself:
* background processing, background number crunching
* keep local copies of data
* reduce the amount of network overhead in your applications
* listens for broadcast news messages from a back-end server
	- posting messages to the main web page as they are received from the back-end server
	- This Web Worker might use Web Sockets or Server-Sent Events to talk to the back-end server

## What you CAN DO with Web Workers?

## What you CANNOT DO with Web Workers?
As powerful as Web Workers are, there are also certain things they cannot do. 
- For example, when a script is executing inside a Web Worker it cannot access the web page’s window object ( window.document), which means that Web Workers don’t have direct access to the web page and the DOM AP
- Although Web Workers cannot block the browser UI, they can still consume CPU cycles and make the system less responsive


## Using Web Workers
- you can spawn a Web Worker to perform the tasks
- and add an event listener to listen to messages from the Web Worker as they are sent


Using Web Workers is fairly straightforward—you create a Web Worker object and pass in a JavaScript file to be executed. Inside the page you set up an event listener to listen to incoming messages and errors that are posted by the Web Worker and if you want to communicate from the page to the Web Worker, you call postMessage to pass in the required data. The same is true for the code in the Web Worker JavaScript file—event handlers must be set up to process incoming messages and errors, and communication with the page is handled with a call to postMessage.

## How Web Workers work?

## How you can use the APIs to create new workers?

## How to communicate between a worker and the context that spawned it?

## How you can build an application with Web Workers?


## Use cases
* Using Web Workers to Improve Image Manipulation Performance
	- https://www.sitepoint.com/using-web-workers-to-improve-image-manipulation-performance/
	- https://johnresig.com/blog/web-workers/
* Automating image optimization for Web
	- https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/automating-image-optimization/

## References
http://apress.jensimmons.com/v5/pro-html5-programming/ch10.html

## Browser Support
- https://caniuse.com/#search=webworkers