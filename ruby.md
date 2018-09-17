---
Title: Ruby on Rails
Decription: Ruby on Rails
Author: Bhaskar Mangal
Date: 17th May 2018
Last Updates: 6th Jun 2018
Tags: Ruby on Rails
---

**Table of Contents**
* TOC
{:toc}


## Ruby, Ruby on Rails, Ruby Gems
* https://www.railstutorial.org/book/beginning
* http://guides.rubyonrails.org/getting_started.html
* https://github.com/rbenv/rbenv
* https://github.com/opf/openproject/blob/stable/7/docs/installation/manual/README.md
* https://www.learnenough.com/story

**Indoduction**
* **Ruby** is a **Programming Language**
* **Rails or Ruby on Rails (ROR)** is an Application Development Framework, with a focus on **Web Application Development**.  Rails uses the MVC pattern.
* **[Ruby Gems](http://guides.rubygems.org/)** is a **package manager** for the Ruby programming language that provides a standard format for distributing Ruby programs and libraries (in a self-contained format called a "gem"), a tool designed to easily manage the installation of gems, and a server for distributing them.
  - The gem command is used to build, upload, download, and install Gem packages. Gem Usage
  - RubyGems is very similar to apt-get, portage, and yum in functionality.
**Bundler**
Bundler is a **package manager** that will aid you in installing all the Jekyll dependencies.

**Details**
* Ruby is a programming language, like php or C++, a set of keywords and symbols with which you can write programs. Ruby is a good general purpose programming language, because it is easy to learn and read, and has some very powerful features. With Ruby you can write all sorts of programs, from desktop applications (with e.g. MacRuby) to command line scripts for automating actions on a computer.
* Rails is a set of tools and abstractions (mostly in the form of modules and classes) that makes writing web applications easier and helps make them simpler to maintain. It helps you write MVC or model-view-controller web applications, which is a way of saying that it makes it easy to separate your logic into functions relating to data access (model), rendering data to the user (view), and business logic (controller). It also has affordances for making it easier to: route requests to specific actions; generate database schemas and migrations; organize and deliver JavaScript, css, and image assets; write and execute automated tests; write html templates with formatting and markup helpers; write more powerful, expressive, and readable code with ActiveSupport utilities; validate data objects; and tons more.

M - Model 
This is the representation of the real world in data. So whatever information your application will handle will be represented in the Model.

V - View
This is how the application will interact with the User. Such things as templates and styles will determine the overall look of the application. 

C - Controller
This is the Business Logic of the Application, or how the Application will behave. In general it takes the form of 'when X then Y', often Event Based programming.

The disciplines involved in creating the UI (User Interface) are substantially different from that involved in Data Modelling, which again differ from coding the Business Logic. Separating them using the MVC pattern means that different people, with different core skills can work on each area without necessarily depending on each other.

* https://rvm.io/

## Jekyll
- Installation
  * https://jekyllrb.com/docs/installation/#requirements

## Themes
- https://github.com/jekyll/minima
- https://github.com/pages-themes/minimal
- https://github.com/mmistakes/minimal-mistakes
- https://github.com/mmistakes/jekyll-theme-basically-basic



https://www.contributor-covenant.org/
## Errors
```
Building native extensions. This could take a while...
ERROR:  Error installing jekyll:
  ERROR: Failed to build gem native extension.

    current directory: /var/lib/gems/2.5.0/gems/http_parser.rb-0.6.0/ext/ruby_http_parser
/usr/bin/ruby2.5 -r ./siteconf20180819-22173-lyhwuo.rb extconf.rb
mkmf.rb can't find header files for ruby at /usr/lib/ruby/include/ruby.h
extconf failed, exit code 1
```
- https://stackoverflow.com/questions/11496591/ruby-gem-permission-denied-var-lib-gems-using-ubuntu
- https://stackoverflow.com/questions/20559255/error-while-installing-json-gem-mkmf-rb-cant-find-header-files-for-ruby/20561594
```bash
ruby -v
gem -v
sudo gem update --system
sudo apt install -y ruby-dev
# sudo apt install -y ruby`ruby -e 'puts RUBY_VERSION[/\d+\.\d+/]'`-dev
sudo gem install bundler jekyll
```
*
bundle install
bundle show
bundle show <gemName>


https://hugogiraudel.com/2013/02/21/jekyll/

* [Jekyll - static website generator](jekyll.md)


https://www.smashingmagazine.com/2016/08/using-a-static-site-generator-at-scale-lessons-learned/