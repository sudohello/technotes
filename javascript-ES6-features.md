---
Title: JS ES6
Decription: JS ES6
Author: Bhaskar Mangal
Date: 
Tags: JS ES6
---

**Table of Contents**
* TOC
{:toc}


## Browser Compatibility
* https://kangax.github.io/compat-table/es6/

## ES6 Feature sets 
* https://www.sitepoint.com/the-es6-conundrum/

ES6 features:

* **Arrow functions** as a short-hand version of an anonymous function.
* **Block-level scope** using let instead of var makes variables scoped to a block (if, for, while, etc.)
* **Classes** to encapsulate and extend code.
* **Constants** using the const keyword.
* **Default parameters** for functions like foo(bar = 3, baz = 2)
* **Destructuring** to assign values from arrays or objects into variables.
* **Generators** that create iterators using function* and the yield keyword.
* **Map**, a Dictionary type object that can be used to store key/value pairs. and Set as a collection object to store a list of data values.
* **Modules** as a way of organizing and loading code.
* **Promises** for async operations avoiding callback hell
* **Rest parameters** instead of using arguments to access functions arguments.
* **Template Strings** to build up string values including multi-line strings.

# Design Patterns
## Prototypal Inheritance
* https://medium.com/javascript-scene/3-different-kinds-of-prototypal-inheritance-es6-edition-32d777fa16c9

I prefer a factory function using `Object.create()`. (In JavaScript, any function can create new objects. When it’s not a constructor function, it’s called a factory function):

## Functionalities
**Assign**
* https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Object/assign

The Object.assign() method is used to copy the values of all enumerable own properties from one or more source objects to a target object. It will return the target object.
It uses [[Get]] on the source and [[Set]] on the target, so it will invoke getters and setters. 

