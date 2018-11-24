---
Title: Jekyll
Decription: Jekyll
Author: Bhaskar Mangal
Date: 19th-Aug-2018
Tags: Jekyll
---

**Table of Contents**
* TOC
{:toc}

## Jekyll


## Highlights
**write reusable content**
- https://blog.github.com/2015-01-06-how-github-uses-github-to-document-github/#content-references
- https://jekyllrb.com/docs/datafiles/

**Versioned documentation**

**Testing Content Generation**
* HTMLProofer
  - It is a set of tests to validate your HTML output. These tests check if your image references are legitimate, if they have alt tags, if your internal links are working, and so on. It's intended to be an all-in-one checker for your output.
  - https://github.com/gjtorikian/html-proofer



## Quick Start
```bash
# runs a local development server at http://localhost:4000 by default, _site
jekyll serve
#  builds the site to _site. , then copy _site to hosting provider
jekylle build
```

* **_config.yml**

```bash
Edit the _config.yml file according to these instructions:

title: The title of your website, as you want it to appear in the header of the webpage.
email: Your email address.
description: A description of your website that will be used in search engine results and the site’s RSS feed.
baseurl: Fill in the quotation marks with a forward slash followed by the name of your website folder (e.g. “/JekyllDemo”) to help locate the site at the correct URL.
url: Replace “http://yourdomain.com” with “localhost:4000” to help locate your local version of the site at the correct URL.
twitter_username: Your Twitter username (do not include @ symbol).
github_username: Your GitHub username.
```

* **datafiles - Read data from CSV, JSON or YAML files into your Liquid templates**
  - Data files give you access information from CSV, JSON or YAML files on your Jekyll site. You can almost treat these files like a database.



## Tutorials
- [Learn Jekyll](https://learn.cloudcannon.com/) - best to get started
  - https://learn.cloudcannon.com/jekyll/permalinks/
  - https://learn.cloudcannon.com/jekyll/converting-a-static-site-to-jekyll/ - relevant when want to adopt good html template to jekyll site
- https://www.siteleaf.com/blog/tags/tutorial/
- https://www.siteleaf.com/blog/jekyll-from-scratch/
- https://jekyllrb.com/docs/static-files/
- https://code.tutsplus.com/articles/building-static-sites-with-jekyll--net-22211
**Full**
- https://css-tricks.com/building-a-jekyll-site-part-1-of-3/

**What is Jekyll?**
- Jekyll is a static website generator built on Ruby. It takes Markdown text (your site’s content) and Liquid templates (your site’s theme) and outputs simple HTML that can be hosted pretty much anywhere.

**Configuration**
- https://jekyllrb.com/docs/configuration/
- https://ben.balter.com/2015/02/20/jekyll-collections/

**[Collections](https://jekyllrb.com/docs/collections/)**
  - https://halfelf.org/2015/jekyll-collections/
  - https://ben.balter.com/2015/02/20/jekyll-collections/

## Github Pages workflow with Jekyll
* https://blog.github.com/2015-01-06-how-github-uses-github-to-document-github/
* https://github.com/gjtorikian/jekyll-html-pipeline
* https://github.com/gjtorikian/extended-markdown-filter

## Search Option for Jekyll Sites

### Lunr
>  full text search with Lunr
* https://lunrjs.com/
* https://lunrjs.com/guides/getting_started.html
* https://github.com/olivernn/lunr.js
- 
Lunr.js is a small, full-text search library for use in the browser. It indexes JSON documents and provides a simple search interface for retrieving documents that best match text queries.

* why a server-side search solution is needed?

* https://idratherbewriting.com/2016/03/23/release-of-documentation-theme-for-jekyll-50/
integrate with something like Algolia or Swiftype to provide a more powerful search feature or integrate something from Apache Solr

## Links
- https://stackoverflow.com/questions/25826770/jekyll-using-links-to-internal-markdown-files


## Jekyll with Apache Web Server
- https://www.christopherrung.com/tutorial/2015/05/07/apache-and-jekyll/
```bash
# cd /path/to/jekyll/blog/
#sudo jekyll build -d /var/www/
cd ~/Documents/content/technotes-site
jekyll build -d ~/public_html/jekyll-sites/tnotes/
```

## Relative URLs
- https://byparker.com/blog/2014/clearing-up-confusion-around-baseurl/
- https://www.digitalocean.com/community/tutorials/controlling-urls-and-links-in-jekyll
- https://jekyllrb.com/news/2016/10/06/jekyll-3-3-is-here/

## github with jekyll
**Getting started with GitHub Pages**
- https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/
- https://github.community/t5/Support-Protips/Getting-started-with-GitHub-Pages-Part-1-Publishing-a-single/ba-p/237
- https://github.community/t5/Support-Series/Getting-Started-with-GitHub-Pages-Part-2-Using-an-Official/ba-p/2030
- https://help.github.com/articles/adding-a-jekyll-theme-to-your-github-pages-site-with-the-jekyll-theme-chooser/
- https://help.github.com/articles/user-organization-and-project-pages/
- https://help.github.com/articles/adding-a-jekyll-theme-to-your-github-pages-site-with-the-jekyll-theme-chooser/

**Setting up your GitHub Pages site locally with Jekyll**
- https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/

## Installation
* http://sharadchhetri.com/2014/06/30/install-jekyll-on-ubuntu-14-04-lts/

## To be explored
- this is what is required:
  * http://www.m-renaud.com/resources/
  * http://www.gwern.net/
  * https://stackoverflow.com/questions/17118551/generating-a-list-of-pages-not-posts-in-a-given-category
  * Jekyll Collections to be explored

* Building Image Heavy Jekyll Site
  - http://benwilhelm.com/the-website/nerd-stuff/2014/12/21/building-an-image-heavy-jekyll-site/
    *  use grunt.js for managing development and deployment tasks. In order to create versions of my photos at different sizes (thumbnail, medium, large, etc), I created a grunt task using grunt-image-resize which scans the originals folder and creates corresponding images at multiple resolutions in folders called thumbs, medium, and large.


https://packery.metafizzy.co/
http://terrymun.github.io/Fluidbox/demo/index.html

https://olivierpieters.be/blog/2016/02/26/creating-a-jekyll-image-gallery


## Create your Own Theme
* https://medium.com/@jameshamann/creating-your-own-jekyll-theme-gem-1f8180a0e4b8


## Themes/Templates
- http://jekyllthemes.org/
- http://pixyll.com/
- https://www.wowthemes.net/jekyll-themes-templates/
- https://html5up.net/
  * https://html5up.net/parallelism

**Marketing**
* Hydra
  - https://github.com/CloudCannon/hydra-jekyll-template
  - https://proud-alligator.cloudvent.net/


**Presentations**
* Levytsroman
  * https://github.com/LevytsRoman/levytsroman.github.io
  * https://levytsroman.github.io/
    - nice flickering image effect

**Tutorials and Documentation themes**
* Base
  * https://github.com/CloudCannon/base-jekyll-template
  * https://orange-ape.cloudvent.net/ - best
    - https://github.com/CloudCannon/base-jekyll-template
* git-hub Documentation theme
  * https://github.com/tomjoht/documentation-theme-jekyll
  * https://idratherbewriting.com/documentation-theme-jekyll/pdf/mydoc.pdf


**Image / Photography**
* pintereso
  - https://www.wowthemes.net/pintereso-free-bootstrap-jekyll-theme/
  - https://github.com/wowthemesnet/template-pintereso-bootstrap-jekyll
* lens
  - https://andrewbanchich.github.io/lens-jekyll-theme/

**Resumes**
* highlights
  - https://andrewbanchich.github.io/highlights-jekyll-theme/

**Blogging**
  - https://github.com/chesterhow/tale
  - https://chesterhow.github.io/tale/about/


## Jekyll as headles CMS
- https://www.storyblok.com/tp/headless-cms-jekyll

```bash
jekyll build
jekyll build --watch
```
https://app.netlify.com/sites/elegant-mirzakhani-b5ecb7/settings/domain
Your site is secured by Let’s Encrypt, a non-profit organization that provides free HTTPS (SSL/TLS) certificates to millions of sites.

- http://yaml.org/

- https://jekyllrb.com/docs/frontmatter/

**Creating Layouts**
- https://jeremenichelli.io/2015/07/building-blog-jekyll-creating-layouts/
- Different markdowns
  * karmdown
  * redcarpet

  https://www.taniarascia.com/make-a-static-website-with-jekyll/

  https://www.taniarascia.com/2017-into-2018/

  https://www.pcworld.com/article/2686467/privacy/how-to-use-the-tor-browser-to-surf-the-web-anonymously.html


## Jekyll Plugins and Hacks
* https://learn.cloudcannon.com/jekyll/gemfiles-and-the-bundler/
* Gemfile
```bash
source 'https://rubygems.org'

gem 'jekyll', '3.1.6'

group :jekyll_plugins do
  gem 'jekyll-feed'
  gem 'jekyll-seo-tag'
end
```
* Install Gem using bundler and start jekyll
```bash
gem install bundler
bundle install
bundle exec jekyll serve
```
* **Pagination**
  - https://jekyllrb.com/docs/pagination/
  - https://github.com/sverrirs/jekyll-paginate-v2/tree/master/examples
  - https://mademistakes.com/til/static-files/
  - https://github.com/fadhilnapis/jekyll-multi-paginate

**Introduction to Jekyll Plugins**
* https://learn.cloudcannon.com/jekyll/using-jekyll-plugins/

**Display all images/files from a directory on a jekyll powered website**
  * https://stackoverflow.com/questions/9204091/display-all-images-from-a-directory-on-a-jekyll-powered-website#9212302
  * https://jekyllrb.com/docs/static-files/
  * https://stackoverflow.com/questions/17677094/jekyll-for-loop-over-all-images-in-a-folder
  * https://bitbucket.org/christianspecht/code-examples/src/tip/jekyll-gallery-example/



## References, People, web-ste samples
- https://www.taniarascia.com/make-a-static-website-with-jekyll/
- http://www.gwern.net/
- https://github.com/planetjekyll/awesome-jekyll
- https://github.com/planetjekyll/awesome-jekyll-plugins
- https://github.com/tmm1/pygments.rb


## Liquid
* https://github.com/Shopify/liquid/wiki/Liquid-for-Designers
* https://shopify.github.io/liquid/

## cheatseet
* https://learn.cloudcannon.com/jekyll-cheat-sheet/


## FAQs
* How to Add Table of Contents?
  - http://www.seanbuscay.com/blog/jekyll-toc-markdown/

```pre
* TOC
{:toc}
```

## Tutorials
**building-blog-jekyll-creating-layouts**
* https://jeremenichelli.io/2015/07/building-blog-jekyll-creating-layouts/

## Jekyll Websites
* http://www.cagrimmett.com/category/photography/
* https://macwright.org/2016/05/03/the-featherweight-website.html
* https://github.com/cagrimmett/jekyll-tools


## Sinpets
```bash
sudo gem install redcarpet rb-pygments
sudo gem install $(cat requirements.txt)
#
gem sources -r https://rubygems.org/
gem sources -a http://rubygems.org/
gem install gem_name --source http://rubygems.org
#to install the gem locally, from your local directory.
gem install --local aoifes_roman.gem
gem list -r

```
**Syntax highlighter**
* http://jekyll-windows.juthilo.com/3-syntax-highlighting/

## Image Processing in Web
* https://lokeshdhakar.com/projects/color-thief/