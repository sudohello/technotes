---
Title: PHP SLIM
Decription: PHP SLIM
Author: Bhaskar Mangal
Date: 19th-Apr-2018
Tags: PHP SLIM
---

**Table of Contents**
* TOC
{:toc}


## SLIM Framework
- https://www.slimframework.com
- https://scotch.io/tutorials/getting-started-with-slim-3-a-php-microframework
- https://phpocean.com/tutorials/back-end/workouts-with-slim-3-create-a-simple-website/48
- http://www.kode-blog.com/slim-framework-twig-template-tutorial
- https://www.slimframework.com/docs/v3/tutorial/first-app.html

```bash
#Install slim
composer require slim/slim "^3.0"
#Install Twig
composer require slim/twig-view
```
**Routing**
https://discourse.slimframework.com/t/slim-3-routing-best-practices-and-organization/93/4

**slim-config-yaml**
https://github.com/techsterx/slim-config-yaml
```bash
composer require techsterx/slim-config-yaml
```
**SLIM: Blade template**
https://github.com/clickcoder/slim-blade
```bash
composer require clickcoder/slim-blade
```
**slim 3 skeleton project**
- https://github.com/aurmil/slim3-skeleton

**Zero to Hero - Virtual Env**
- http://jeremykendall.net/2014/07/28/from-zero-to-slim-framework-getting-your-first-project-off-the-ground/

**Rest API with Slim**
- https://www.phpflow.com/php/create-simple-rest-api-using-slim-framework/

https://www.sitepoint.com/writing-a-restful-web-service-with-slim/
http://ryanszrama.com/blog/06-28-2015/hello-you-slim-framework-3x

**SLIM, Twig, Angular**
https://medium.com/@rachitmishra/configuring-slim-twig-angular-js-13aba6116bfe

## Accessing Query Parameters in Slim
- https://stackoverflow.com/questions/8125064/slim-php-and-get-parameters

### PSR-7 in Slim
- https://www.slimframework.com/docs/v3/objects/request.html

## Routing
- https://github.com/nikic/FastRoute#defining-routes
```php
#
// This route
$r->addRoute('GET', '/user/{id:\d+}[/{name}]', 'handler');
// Is equivalent to these two routes
$r->addRoute('GET', '/user/{id:\d+}', 'handler');
$r->addRoute('GET', '/user/{id:\d+}/{name}', 'handler');

// Multiple nested optional parts are possible as well
$r->addRoute('GET', '/user[/{id:\d+}[/{name}]]', 'handler');

// This route is NOT valid, because optional parts can only occur at the end
$r->addRoute('GET', '/user[/{id:\d+}]/{name}', 'handler');
##
$r->get('/get-route', 'get_handler');
$r->post('/post-route', 'post_handler');
```

## REST API
- http://coenraets.org/blog/2011/12/restful-services-with-jquery-php-and-the-slim-framework/