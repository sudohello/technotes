---
Title: Software Engineering
Decription: Software Engineering
Author: Bhaskar Mangal
Date: 
Tags: Software Engineering
---

**Table of Contents**
* TOC
{:toc}


## Software Engineering

[DSL - Domain-specific_language](https://en.wikipedia.org/wiki/Domain-specific_language)

**SRS, FRS, BRS**
SRS means software requirement specification; FRS – functional requirement specification; BRS – business requirement specification. ... A system analyst is responsible for SRS creation, while developers – for FRS. BRS is a duty of a business analyst.

* http://www.jrobbins.org/ics121f03/lesson-spec-design.html
* http://searchsoftwarequality.techtarget.com/tip/Ambiguous-software-requirements-lead-to-confusion-extra-work

Negative, or inverse, requirements state what the system will not do. Here's an example from an actual project: "All users with three or more accounts should not be migrated." Try to rephrase negative requirements into a positive sense: "The system shall migrate only users having fewer than three accounts."


Negative, or inverse, requirements state what the system will not do. Try to rephrase negative requirements into a positive sense.

## Agile Development
https://pm.stackexchange.com/questions/15467/srs-for-an-agile-project

http://agilemodeling.com/essays/agileRequirements.htm
http://agilemodeling.com/essays/amdd.htm
https://www.mountaingoatsoftware.com/blog/can-a-traditional-srs-be-converted-into-user-stories

## MDD
http://searchsoftwarequality.techtarget.com/definition/model-driven-development
https://en.wikipedia.org/wiki/Model-driven_engineering
https://en.wikipedia.org/wiki/Model-driven_architecture

## data-flow diagrams (DFDs)
	
## Diagram Designing Tools
https://stackoverflow.com/questions/9207092/are-there-any-good-free-lightweight-linux-uml-design-tools
https://softwareengineering.stackexchange.com/questions/72459/uml-modeling-tool-for-linux
https://graphicdesign.stackexchange.com/questions/16629/drawing-block-diagram

Dia, StarUML and argoUML, Visual Paradigm, POPP/POI (Plain Old PowerPoint/Impress), gliffy.com, yEd, Red Koda. Most of them work under Linux.


http://alexdp.free.fr/violetumleditor/page.php
http://www.bouml.fr/
http://staruml.io/
https://sourceforge.net/projects/dia-installer/files/
http://www.yworks.com/products/yed
https://kivio.en.uptodown.com/ubuntu
http://astah.net/editions/professional
https://umbrello.kde.org/
http://www.umlet.com/
http://argouml.tigris.org/
http://www.jave.de/

## OOP
https://scotch.io/bar-talk/s-o-l-i-d-the-first-five-principles-of-object-oriented-design#openclosed-principle

**Dependency injection**
https://en.wikipedia.org/wiki/Dependency_injection

In software engineering, dependency injection is a technique whereby one object (or static method) supplies the dependencies of another object. A dependency is an object that can be used (a service). An injection is the passing of a dependency to a dependent object (a client) that would use it. The service is made part of the client's state.[1] Passing the service to the client, rather than allowing a client to build or find the service, is the fundamental requirement of the pattern.

## Programming

**KebabCase**
* http://wiki.c2.com/?KebabCase
The naming style used in LispLanguage and related languages. All lowercase with - separating words.

```bash
looks-like-this
```
**Snake_case**
* https://en.wikipedia.org/wiki/Snake_case
Snake case (or snake_case) is the practice of writing compound words or phrases in which the elements are separated with one underscore character (_) and no spaces, with each element's initial letter usually lowercased within the compound and the first letter either upper or lower case—as in "foo_bar" and "Hello_world". It is commonly used in computer code for variable names, and function names, and sometimes computer filenames.[1] At least one study found that readers can recognize snake case values more quickly than camelCase.[2]

**Camel_case**
* https://en.wikipedia.org/wiki/Camel_case
Camel case (stylized as camelCase or CamelCase; also known as camel caps or more formally as medial capitals) is the practice of writing 


**Mixins**
- https://en.wikipedia.org/wiki/Mixin
* In object-oriented programming languages, a Mixin is a class that contains methods for use by other classes without having to be the parent class of those other classes.
* Mixins encourage code reuse and can be used to avoid the inheritance ambiguity that multiple inheritance can cause or to work around lack of support for multiple inheritance in a language.

## Reactive Programming
- https://en.wikipedia.org/wiki/Reactive_programming
- https://medium.com/@kevalpatel2106/what-is-reactive-programming-da37c1611382


https://bootstrap-vue.js.org/docs/components/navbar/
https://medium.com/@mbostock/a-better-way-to-code-2b1d2876a3a0

## [Dataflow Programming](https://en.wikipedia.org/wiki/Dataflow_programming)
- dataflow languages are inherently parallel and can work well in large, decentralized systems
- Data flow has been proposed as an abstraction for specifying the global behavior of distributed system components: in the live distributed objects programming model, distributed data flows are used to store and communicate state, and as such, they play the role analogous to variables, fields, and parameters in Java-like programming languages

## System Primer
* https://github.com/donnemartin/system-design-primer

## Terms
**heisenbug**
* https://en.wikipedia.org/wiki/Heisenbug
In computer programming jargon, a heisenbug is a software bug that seems to disappear or alter its behavior when one attempts to study it.[1] The term is a pun on the name of Werner Heisenberg, the physicist who first asserted the observer effect of quantum mechanics, which states that the act of observing a system inevitably alters its state. In electronics the traditional term is probe effect, where attaching a test probe to a device changes its behavior.

**Monkey Patch/Patching**
* https://en.wikipedia.org/wiki/Monkey_patch
A monkey patch is a way for a program to extend or modify supporting system software locally (affecting only the running instance of the program).
* https://stackoverflow.com/questions/5626193/what-is-monkey-patching#5626250
No, it's not like any of those things. It's simply the dynamic replacement of attributes at runtime.
For instance, consider a class that has a method get_data. This method does an external lookup (on a database or web API, for example), and various other methods in the class call it. However, in a unit test, you don't want to depend on the external data source - so you dynamically replace the get_data method with a stub that returns some fixed data.

**cooperative multitasking approach or simple multitasking**
https://en.wikipedia.org/wiki/Computer_multitasking#Cooperative_multitasking.2Ftime-sharing

**sscce - Short, Self Contained, Correct (Compilable), Example**
http://sscce.org/
Short (Small) - Minimise bandwidth for the example, do not bore the audience.
Self Contained - Ensure everything is included, ready to go.
Correct - Copy, paste, (compile,) see is the aim.
Example - Displays the problem we are trying to solve.

**comet**
https://en.wikipedia.org/wiki/Comet_(programming)
Comet is a web application model in which a long-held HTTPS request allows a web server to push data to a browser, without the browser explicitly requesting it.[1][2] Comet is an umbrella term, encompassing multiple techniques for achieving this interaction. All these methods rely on features included by default in browsers, such as JavaScript, rather than on non-default plugins. The Comet approach differs from the original model of the web, in which a browser requests a complete web page at a time.[3]