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


## Web Worker API
* How Web Workers work?
* How you can use the APIs to create new workers?
* How to communicate between a worker and the context that spawned it?
* How you can build an application with Web Workers?
* **API**
	* Worker
	* SharedWorker
	* ServiceWorker
	* ServiceWorkerContainer
	* ServiceWorkerRegistration

**Using Web Workers**
- you can spawn a Web Worker to perform the tasks
- and add an event listener to listen to messages from the Web Worker as they are sent

Using Web Workers is fairly straightforward—you create a Web Worker object and pass in a JavaScript file to be executed. Inside the page you set up an event listener to listen to incoming messages and errors that are posted by the Web Worker and if you want to communicate from the page to the Web Worker, you call postMessage to pass in the required data. The same is true for the code in the Web Worker JavaScript file—event handlers must be set up to process incoming messages and errors, and communication with the page is handled with a call to postMessage.

- **Inline Workers**
  - Inline Web Workers—a feature that can be used only if your browser also supports the File System API (Blob Builder or File Writer)
  - In that case you can programmatically find the script block, and write the Web Worker JavaScript file to disk
  - `<script id="myWorker" type="javascript/worker">`
- **Shared Workers**
  - A shared Web Worker is like a normal Web Worker, but it can be shared across multiple pages on the same origin
  - Shared Web Workers introduce the notion of ports that are used for PostMessage communication
  - Shared Web Workers can be useful for data synchronization among multiple pages (or tabs) on the same origin or to share a long-lived resource (like a WebSocket) among several tab
  - `sharedWorker = new SharedWorker(sharedEchoWorker.js');`
- Data passed between the main page and workers is copied, not shared
- Objects are serialized as they're handed to the worker, and subsequently, de-serialized on the other end
- Uses structured cloning algo
- The structured cloning algorithm can accept JSON and a few things that JSON can't — like circular references


1. [Using_web_workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)
Workers may spawn more workers if they wish. So-called sub-workers must be hosted within the same origin as the parent page.
**Dedicated worker**
- `var w = new Worker('worker.js');` //js file
- `postMessage()`
- `onmessage(e)` //e.data 
- `terminate()`
- `close()`

**Shared worker**
- `var sw = new SharedWorker("worker.js");`
- `sw.port.onmessage = function(e)` //e.data
- `onconnect(e)`
- `port.onmessage = function(e)` //inside onconnect
- `port.postMessage = function(e)`
- One big difference is that with a shared worker you have to communicate via a port object — an explicit port is opened that the scripts can use to communicate with the worker (this is done implicitly in the case of dedicated workers)
- The port connection needs to be started either implicitly by use of the onmessage event handler or explicitly with the start() method before any messages can be posted. Calling start() is only needed if the message event is wired up via the addEventListener() method
- When using the start() method to open the port connection, it needs to be called from both the parent thread and the worker thread if two-way communication is needed

**sub-workers**
- Workers may spawn more workers if they wish. So-called sub-workers must be hosted within the same origin as the parent page. Also, the URIs for subworkers are resolved relative to the parent worker's location rather than that of the owning page. This makes it easier for workers to keep track of where their dependencies are
- Spawning a new shared worker is pretty much the same as with a dedicated worker, but with a different constructor name

- Thread Safety - concurrency concerns
  * However, since web workers have carefully controlled communication points with other threads, it's actually very hard to cause concurrency problems. There's no access to non-threadsafe components or the DOM. And you have to pass specific data in and out of a thread through serialized objects. So you have to work really hard to cause problems in your code.
- Content security policy
  * Workers are considered to have their own execution context, distinct from the document that created them
  * `Content-Security-Policy: script-src 'self'`
  * this will prevent any scripts it includes from using eval(). However, if the script constructs a worker, code running in the worker's context will be allowed to use eval()
  * To specify a content security policy for the worker, set a Content-Security-Policy response header for the request which delivered the worker script itself
  * The exception to this is if the worker script's origin is a globally unique identifier (for example, if its URL has a scheme of data or blob). In this case, the worker does inherit the CSP of the document or worker that created it

## Use cases
* Using Web Workers to Improve Image Manipulation Performance
	- https://www.sitepoint.com/using-web-workers-to-improve-image-manipulation-performance/
	- https://johnresig.com/blog/web-workers/
* Automating image optimization for Web
	- https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/automating-image-optimization/

## References
- http://apress.jensimmons.com/v5/pro-html5-programming/ch10.html
- https://developer.mozilla.org/en-US/docs/Web/API/Worker/Worker
- [Web Worker Specifications](https://html.spec.whatwg.org/multipage/workers.html#runtime-script-errors-2)

## Browser Support
- https://caniuse.com/#search=webworkers