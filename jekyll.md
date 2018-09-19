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

## Tutorials
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

* [Collections](https://jekyllrb.com/docs/collections/)

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

## Themes
- http://jekyllthemes.org/
- http://pixyll.com/

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



## References, People, web-ste samples
- https://www.taniarascia.com/make-a-static-website-with-jekyll/
- http://www.gwern.net/
- https://github.com/planetjekyll/awesome-jekyll
- https://github.com/planetjekyll/awesome-jekyll-plugins
- https://github.com/tmm1/pygments.rb


## Liquid
* https://github.com/Shopify/liquid/wiki/Liquid-for-Designers

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