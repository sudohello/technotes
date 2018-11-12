---
Title: Github
Decription: Github
Author: Bhaskar Mangal
Date: 
Tags: Github
---

**Table of Contents**
* TOC
{:toc}


## Git LFS
* https://git-lfs.github.com/
An open source Git extension for versioning large files
Git Large File Storage (LFS) replaces large files such as audio samples, videos, datasets, and graphics with text pointers inside Git, while storing the file contents on a remote server like GitHub.com or GitHub Enterprise.

## Version Control Management of GIS Data
* http://geogig.org/
* https://www.locationtech.org/content/geogig-git-approach-geospatial
---
* http://archaeogeek.github.io/aging_githubtalk/#/30
* https://www.directionsmag.com/article/1613
* https://gis.stackexchange.com/questions/61978/implementing-version-control-system-for-geospatial-data

## Github Pages, Jekyll sites
* https://blog.github.com/2015-01-06-how-github-uses-github-to-document-github/
* https://pages.github.com/
* https://dita.xml.org/
* travis-ci
  - https://blog.github.com/2015-01-06-how-github-uses-github-to-document-github/#testing-our-site
  - https://travis-ci.com/
> By committing to using the same hosting features we provide to every GitHub user, we were able to provide better documentation, faster. Our internal workflow has made us more productive, and enabled us to provide features we never could before, such as versioned content.


* CI: Continious Integration
* CD: Continious Deveopment

**How I Setup Jekyll on GitHub Pages**
* https://opensource.com/business/15/7/continuous-integration-and-continuous-delivery-documentation

* https://chrisyeh96.github.io/2017/08/05/setting-up-jekyll-on-github-pages.html

* https://enterprise.github.com/downloads/en/markdown-cheatsheet.pdf

**Best guide is github help itself**
* https://pages.github.com/
* https://help.github.com/articles/configuring-a-publishing-source-for-github-pages/
* https://stackoverflow.com/questions/35978862/github-pages-why-do-i-need-a-gh-pages
* https://idratherbewriting.com/documentation-theme-jekyll/mydoc_publishing_github_pages.html



**Custom Domain for github pages**
* https://help.github.com/articles/quick-start-setting-up-a-custom-domain/


## hubbots and chatops
- https://blog.github.com/2015-01-06-how-github-uses-github-to-document-github/

## Webhooks
- https://developer.github.com/webhooks/

## Git, GitHub, bitbucket, gitbook

## Git
https://try.github.io/levels/1/challenges/1
https://php.earth/docs/interop/git
https://git-scm.com/doc
https://git-scm.com/
https://git-scm.com/book/en/v1/Getting-Started-About-Version-Control

**Basic Concetps**
https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone

**Git Ignore Templates**
https://github.com/github/gitignore

**difference-between-git-and-cvs**
https://stackoverflow.com/questions/802573/difference-between-git-and-cvs

### Git Installation on Ubuntu
- https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-16-04

## Setup your new Code Repo
- https://gist.github.com/mindplace/b4b094157d7a3be6afd2c96370d39fad
- https://gist.github.com/c0ldlimit/4089101

**Help Articles from GitHUB**
- https://help.github.com/articles/creating-a-new-repository/
- https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/

1. Using your terminal/command line, get inside the folder where your project files are kept: cd /path/to/my/codebase.
2. Check if git is already initialized: git status
3. Initialize git repository (git init)
4. Create a remote, empty folder/repository on Github
5. Connect your local project folder to your empty folder/repository on Github - copy the github repo URL

```bash
#
# Create a new repository on the command line
#
touch README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin [copied web url of github repo]
git push -u origin master
#
# Push an existing repository from the command line
#
git remote add origin [copied web url of github repo]
git push -u origin master
```

## How To's

* **How to add an existing project to github using the command line?**
  * https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/

* https://stackoverflow.com/questions/3620633/what-is-the-difference-between-pull-and-clone-in-git

```bash
sudo apt-get install git-core
```

**Sparse Checkout**
-  git 1.7.0 (Feb. 2012)
* http://schacon.github.io/git/git-read-tree.html#_sparse_checkout
* https://stackoverflow.com/questions/600079/how-do-i-clone-a-subdirectory-only-of-a-git-repository#13738951

"sparse clone" and "sparse fetch"  are not supported

The steps to do a sparse clone are as follows:
```bash
mkdir <repo>
cd <repo>
git init
git remote add -f origin <url>
```
This creates an empty repository with your remote, and fetches all objects but doesn't check them out. Then do:
```bash
git config core.sparseCheckout true
```
Now you need to define which files/folders you want to actually check out.
```bash
echo "some/dir/" >> .git/info/sparse-checkout
echo "another/sub/tree" >> .git/info/sparse-checkout
```
update your empty repo with the state from the remote:
```bash
git pull origin master
```

## Git Commands

### Plugins/External Utils
**diff tools**
- https://www.slant.co/topics/1324/~diff-tools-for-git#6
- https://github.com/so-fancy/diff-so-fancy


## Tricks
- https://stackoverflow.com/questions/1947430/git-remove-directory
- https://stackoverflow.com/questions/6313126/how-to-remove-a-directory-from-git-repository
**use this to leave the local copy alone but remove from version control**
```bash
git rm -r -f --cached DirectoryName
git rm -r --cached myFolder
```

## Git Ignore Setup/Templates
- https://www.atlassian.com/git/tutorials/saving-changes/gitignore

* Global Git ignore rules
```bash
# create and confic git ignore file
touch ~/.gitignore
git config --global core.excludesFile ~/.gitignore
# Debugging .gitignore files
git check-ignore -v debug.log
```
* The best practice would be to place the .gitignore file in the root directory. This means one .gitignore file for one entire repo. This makes managing the ignored files more effectively. 
```bash
# in the project root directory
touch .gitignore
#ls -1d .git*
.git
.gitignore
# more help
git help gitignore
# or
man gitignore
#
!/*.csv
!/*.json
!/*.geojson
!/*.xlsx
!/*.xls
#
# Ignore everything inside data/ directory
/data/**
# Except for subdirectories(won't be commited anyway if there is no commited file inside)
!/data/**/
# And except for *.foo files
!*.*
```
- http://kbroman.org/github_tutorial/pages/init.html
- https://wpism.com/publish-local-project-github-command-line/
- https://gist.github.com/wlbr/1685405
```bash
sudo groupadd git
sudo delgroup git
sudo adduser git
sudo deluser git
#
git clone git@maze:/home/bhaskar/public_html/3Dmap/mapboxgl/smartcity
```

## Git multiple remote repository
- https://stackoverflow.com/questions/849308/pull-push-from-multiple-remote-locations/12795747#12795747
```bash
#
git remote -v
#
git remote add alt <remoteURL>
#git remote add alt https://github.com/mangalbhaskar/linuxscript-2.git
git remote -v
#
git push alt
#
git config -e
git config -help
#
git remote remove alt
git remote -help
#
git remote set-url origin --push --add https://github.com/mangalbhaskar/linuxscript-2.git
git remote set-url origin --push --delete https://github.com/mangalbhaskar/linuxscript-2.git
#
```

## Rebase / Rebasing
- “I want to base my changes on what everybody has already done.”
* https://git-scm.com/book/en/v2/Git-Branching-Rebasing
* https://www.atlassian.com/git/tutorials/merging-vs-rebasing
* https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase
```bash
git rebase --help
```
**Proposal:**
1. Create a github fork of release which was used to make local changes
2. push all the local changes to the forked (master branch) [ensure its working]
3. create a release tag [ name it according to stable release of mapboxgl which was used]
4. create a 'dev' branch
5. when the latest stable release is out form the mapboxgl branch:
- create the branch 'patch' from the dev branch, which would be used for merging
- add mapbox gl as the secondary remote repo
- rebase this branch with the latest mapboxgl release
- sanity check and commit
- move this branch to the latest dev branch
- delete the patch branch
6. make a release with the release tag

## FAQs
* **what-is-the-difference-between-git-pull-and-git-fetch**
  - https://stackoverflow.com/questions/292357/what-is-the-difference-between-git-pull-and-git-fetch
  - The take away is to keep in mind that there are often at least three copies of a project on your workstation. One copy is your own repository with your own commit history. The second copy is your working copy where you are editing and building. The third copy is your local "cached" copy of a remote repository.
* **what does git recursive and no-recursive options and what they do?**
  - `--recursive` and `--no-recursive`
  - https://stackoverflow.com/questions/3796927/how-to-git-clone-including-submodules
    - With `version 2.13` of Git and later, `--recursive` has been deprecated and `--recurse-submodules` should be used instead
    - `-j8` is an optional performance optimization that became available in `version 2.8`, and fetches up to 8 submodules at a time in parallel — `see man git-clone`. Example:
    - `git clone --recurse-submodules -j8 git://github.com/foo/bar.git`
  - https://github.com/git-lfs/git-lfs/issues/1309
  - https://medium.com/@porteneuve/mastering-git-submodules-34c65e940407
* **What are Git submodules?**
  - https://git-scm.com/docs/git-submodule
  - **Submodules**, like subtrees, aim to reuse code from another repo somewhere inside your own repo’s tree. The goal is usually to benefit from central maintenance of the reused code across a number of container repos, without having to resort to clumsy, unreliable copy-pasting.


## Cloning between two or more machines
* References
  * https://stackoverflow.com/questions/2816369/git-push-error-remote-rejected-master-master-branch-is-currently-checked/
* base and non-bare repo
  * https://stackoverflow.com/questions/5540883/whats-the-practical-difference-between-a-bare-and-non-bare-repository#5541917
  * git init, which will create a non-bare repo with no remote specified. 
  A bare repository is nothing but the .git folder itself i.e. the contents of a bare repository is same as the contents of .git folder inside your local working repository.

Use bare repository on a remote server to allow multiple contributors to push their work.
Non-bare - The one which has working tree makes sense on the local machine of each contributor of your project.
* clone the repo from another machine
```bash
USER="blah"
IP="168.4.1.6"
REMOTE_PATH="/home/$USER/Documents/codeRepo"
URL="$USER@$IP:$REMOTE_PATH"
PROG_DIR="$HOME/Documents/codeRepo"
## Clone the git repo under `$HOME/Documents/<repoName>`
git clone $URL $PROG_DIR
```

* https://stackoverflow.com/questions/804545/what-is-this-git-warning-message-when-pushing-changes-to-a-remote-repository/28262104#28262104
* On the remote repo:
```bash
git config receive.denyCurrentBranch updateInstead
```


## Internal Repository Setup
**How to setup internal remote repository management system on the dedicated server?**
* https://news.ycombinator.com/item?id=7197548
* https://stackoverflow.com/questions/11430186/internal-repository-setup
1. On the server run the following command in a directory you want to use...
```bash
git init --bare
```
This creates an empty/bare repository on the server.

2. On the client run the following command in an existing git repository (assume you know how to do this)...
```bash
git remote add myserver <url/path>
```
This adds a remote / link to your server. Path can be local, remote (http, ssh, etc).
  - On a local file system use: ~/myrepo/example.git
  - Using ssh: ssh://username@example.org/~/myrepo/example.git
  - Using http: http://username@example.org/myrepo/example.git
3. To push code to your server do the following...
```bash
git push myserver master
```
This pushes your commits up to the remote server. Where 'myserver' is the alias you gave to your remote location
```bash
git pull myserver master
```
With git pull you download/pull all the commits from the server.


## **Git Repo setup on Server**
**Steps that worked for me:**
* On Server
```bash
mkdir -p $HOME/Documents/git-repo/<repoName>
cd $HOME/Documents/git-repo/<repoName>
git init --bare
```
* On the client - origin (first time setup)
```bash
cd $HOME/Documents/<repoName>
git remote -v
git remote remove origin
git remote add origin <userName>@<IP>:/home/<userName>/Documents/git-repo/<repoName>/
git push --set-upstream origin master
git push origin master
```

**All other clients**
* Clone
```bash
cd $HOME/Documents
git clone <userName>@<IP>:/home/<userName>/Documents/git-repo/<repoName>
```
* Pull latest changes - For any additional changes, update the clients
```bash
##
cd $HOME/Documents/<repoName>
git pull
```
* Push changes, after committing the local changes
```bash
git push
```


### How to Run Your Own Git Server
* https://www.linux.com/learn/how-run-your-own-git-server
* https://intercom.help/gitprime/data-setup-and-security/git-hosts/using-gitprime-with-an-internal-server-or-behind-a-firewall


## Git Hub Education - Student and Teacher Collaboration
* https://github.com/education

## Subversion (SVN) Client Support
* https://help.github.com/articles/support-for-subversion-clients/
* https://github.com/telecombcn-dl/2016-dlcv/tree/gh-pages/slides


## Fork / Forking
* https://help.github.com/articles/renaming-a-repository/
* https://guides.github.com/activities/forking/
* https://github.com/octocat/Spoon-Knife - Practice Repo