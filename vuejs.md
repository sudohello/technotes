---
Title: VueJs
Decription: VueJs
Author: Bhaskar Mangal
Date: 13th-Mar-2018
Tags: VueJs
---

**Table of Contents**
* TOC
{:toc}


## VueJs

## vue-cli
* https://tutorials.kode-blog.com/vue-js-tutorial
```bash
npm install --global vue-cli
#
vue --help
vue -V
```

## Vue.js with PHP
https://codeburst.io/using-vue-js-components-in-php-applications-e5bfde8763bc

**Project Structure**
The sources of our bundle are located in the src/ folder. The main file which includes all other files is called main.js. We will place Vue.js components in the src/components/ subfolder, style sheets in src/styles/ and images in src/images/.
Note that only images which are directly used by our bundle need to be placed here. That includes, for example, background images used by the style sheets. Images which are only used by the PHP application should be located somewhere else, so they are not mixed together.
The webpack configuration file is placed in src/build/ so it doesn’t clutter the root folder of our application.
The generated bundle is placed in the assets/ folder. It contains the minimized script and style sheet and all images which are copied from src/images/. You can change the location of the bundle, but you have to modify the example configuration accordingly.
Other files and folders, for example app/ and lib/, are part of the PHP application. Their names may be different, but it’s not really important, because webpack will not touch them.
Remember that when you deploy the application to a production server, do not include the src/ and node_modules/ folders. Everything that you need to deploy will be placed in the assets/ folder.

```bash
mkdir -p app assets/css assets/images assets/js lib src/build src/components src/images src/styles

npm i -g vue-cli

npm install --save deck.gl
npm install --save mapbox-gl

```

## Tutorials
https://designhammer.com/blog/reusable-vuejs-components-part-1-introduction

## Resources
https://github.com/vuejs/awesome-vue
