---
Title: Javascript
Decription: Javascript
Author: Bhaskar Mangal
Date: 
Tags: Javascript
---

**Table of Contents**
* TOC
{:toc}


## Javascript

## Dat-GUI
- https://github.com/dataarts/dat.gui
dat.gui
A lightweight graphical user interface for changing variables in JavaScript.
Get started with dat.GUI by reading the tutorial at http://workshop.chromeexperiments.com/examples/gui.

## JavaScript Releases: ES2016 and Beyond
- https://javascriptplayground.com/es2016-and-beyond/

## [ReactJs](https://reactjs.org/)
> A JavaScript library for building user interfaces

## Ecmascript
https://codeburst.io/javascript-wtf-is-es6-es8-es-2017-ecmascript-dca859e4821c

https://codeburst.io/javascript-understanding-the-weird-parts-d1d0e7061ebf
https://www.tutorialspoint.com/es6/es6_overview.htm

- variable hoisting
	- Variable hoisting allows the use of a variable in a JavaScript program, even before it is declared.
	- The concept of hoisting applies to variable declaration but not variable initialization
	- It is recommended to always declare variables at the top of their scope (the top of global code and the top of function code), to enable the code resolve the variable’s scope.
- Function hoisting
	- Like variables, functions can also be hoisted. Unlike variables, function declarations when hoisted, hoists the function definition rather than just hoisting the function’s name.
- dynamic typing, un-typed language
- variable declaration: var, ES6:let,const
	- const:
			- creates a read-only reference to a value.
			-  Constants are block-scoped, much like variables defined using the let statement
			- The value of a constant cannot change through re-assignment, and it can't be re-declared.
			- A constant requires an initializer. This means constants must be initialized during its declaration.
			- The value assigned to a const variable is immutable.
- global scope, local scope, ESt6: block scope
- Rest Parameters
Rest parameters are similar to variable arguments in Java. Rest parameters doesn’t restrict the number of values that you can pass to a function. However, the values passed must all be of the same type. In other words, rest parameters act as placeholders for multiple arguments of the same type.

To declare a rest parameter, the parameter name is prefixed with three periods, known as the spread operator. The following example illustrates the same.
```javascript
function fun1(...params) { 
   console.log(params.length); 
}  
fun1();  
fun1(5); 
fun1(5, 6, 7); 
```
https://www.tutorialspoint.com/es6/es6_functions.htm
- ES6, a function allows the parameters to be initialized with default values, if no values are passed to it or it is undefined.
- Anonymous Function
	-  Functions that are not bound to an identifier (function name) are called as 
anonymous functions.
	-  An anonymous function is usually not accessible after its initial creation.
-  An anonymous function is usually not accessible after its initial creation.
-  An anonymous function is usually not accessible after its initial creation.
- Function expression and function declaration are not synonymous. Unlike a function expression, a function declaration is bound by the function name
The fundamental difference between the two is that, function declarations are parsed before their execution. On the other hand, function expressions are parsed only when the script engine encounters it during an execution
- Immediately Invoked Function Expressions (IIFEs)
	- can be used to avoid variable hoisting from within blocks.
	- It allows public access to methods while retaining privacy for variables defined within the function.
	- This pattern is called as a self-executing anonymous function.
	
Generator Functions
- The function can yield control back to the caller at any point.
- When you call a generator, it doesn’t run right away. Instead, you get back an 
iterator. The function runs as you call the iterator’s next method.
- Generators are denoted by suffixing the function keyword with an asterisk; otherwise, their syntax is identical to regular functions


http://qnimate.com/post-series/ecmascript-6-complete-tutorial/
https://caniuse.com/
http://kangax.github.io/compat-table/es6/

https://codeburst.io/es6-tutorial-for-beginners-5f3c4e7960be
http://ccoenraets.github.io/es6-tutorial/

http://vancelucas.com/blog/dont-transpile-javascript-for-node-js/

**does react really need nodeJS on the frontend ENV?**
https://stackoverflow.com/questions/41838728/does-react-really-need-nodejs-on-the-frontend-env

https://www.contentful.com/blog/2017/04/04/es6-modules-support-lands-in-browsers-is-it-time-to-rethink-bundling/
http://exploringjs.com/es6/ch_modules.html#sec_modules-vs-scripts
https://medium.com/dailyjs/es6-modules-node-js-and-the-michael-jackson-solution-828dc244b8b
https://medium.com/@gimenete/how-javascript-bundlers-work-1fc0d0caf2da
https://webpack.github.io/
http://browserify.org/
https://hackernoon.com/import-export-default-require-commandjs-javascript-nodejs-es6-vs-cheatsheet-different-tutorial-example-5a321738b50f


* **what is a JavaScript bundler?**
A JavaScript bundler is a tool that puts your code and all its dependencies together in one JavaScript file. There are many of them out there these days, being the most popular ones browserify and webpack.

* **universal JavaScript (aka isomorphic JavaScript).**
	- https://github.com/ericelliott/isomorphic-express-boilerplate
	- https://medium.com/@mjackson/universal-javascript-4761051b7ae9
	- https://medium.com/javascript-scene/how-to-use-es6-for-isomorphic-javascript-apps-2a9c3abe5ea2
	- http://bencentra.github.io/using-es6-slides

* **CommonJS, UMD/AMD**
	- http://wiki.commonjs.org/wiki/CommonJS

https://webpack.js.org/guides/tree-shaking/



https://github.com/umdjs/umd

https://codeutopia.net/blog/2014/12/18/getting-started-with-using-es6-ecmascript-6/

https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript

https://medium.com/@alberto.schiabel/nodejs-in-es6-es7-how-do-you-do-it-in-production-d897c51c729c

https://shinglyu.github.io/web/2016/04/06/minimal_react.html

https://vuejs.org/v2/guide/installation.html


## Register/Unregistert Events - Event Handling
https://developer.mozilla.org/en-US/docs/Web/Guide/Events/Event_handlers
https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener


## Arrays
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce

**Array of Objects to Object**
https://medium.com/dailyjs/rewriting-javascript-converting-an-array-of-objects-to-an-object-ec579cafbfc7
```javascript
const arrayToObject = (array, keyField) =>
   array.reduce((obj, item) => {
     obj[item[keyField]] = item
     return obj
   }, {})
const peopleObject = arrayToObject(peopleArray, "id")
console.log(peopleObject[idToSelect])
```
**Object to Array**
```javascript
const peopleArray = Object.values(peopleObj)
//
const peopleArray = Object.keys(peopleObj).map(i => peopleObj[i])
```

**Sum numbers new approach**
https://medium.com/@chrisburgin95/rewriting-javascript-sum-an-array-dbf838996ed0

## webpack-browserify-gulp-which-is-better
https://www.toptal.com/front-end/webpack-browserify-gulp-which-is-better

* Arrow functions
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions
https://hacks.mozilla.org/2015/06/es6-in-depth-arrow-functions/

* Map Function
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map

* Rest Parameters
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters

* reduce Function
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce
https://medium.freecodecamp.org/reduce-f47a7da511a9

* Fi

## 3D
https://godotengine.org/article/we-should-all-use-gltf-20-export-3d-assets-game-engines
https://blog.mozvr.com/a-saturday-night-gltf-workflow/
https://www.khronos.org/gltf/

## IM
https://gitter.im/

## NPM Runkit Browser based Learning
https://npm.runkit.com/d3-selection-multi

## Apply, Bind, Call
http://javascriptissexy.com/javascript-apply-call-and-bind-methods-are-essential-for-javascript-professionals/

## Map, Filter, Reduce
http://cryto.net/~joepie91/blog/2015/05/04/functional-programming-in-javascript-map-filter-reduce/
http://www.discovermeteor.com/blog/understanding-javascript-map/

## Tips
* 0/0 is NaN
* 4/0 is Infinity

## ES5
* isNaN()
* isFinite()

## TBD
- FileReader
- Worker
