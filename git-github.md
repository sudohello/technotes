/*
Title: Github
Decription: Github
Author: Bhaskar Mangal
Date: 
Tags: Github
*/

# Git, GitHub, bitbucket, gitbook

## Git
https://try.github.io/levels/1/challenges/1
https://php.earth/docs/interop/git
https://git-scm.com/doc
https://git-scm.com/

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
## FAQs
**what-is-the-difference-between-git-pull-and-git-fetch**
- https://stackoverflow.com/questions/292357/what-is-the-difference-between-git-pull-and-git-fetch


The take away is to keep in mind that there are often at least three copies of a project on your workstation. One copy is your own repository with your own commit history. The second copy is your working copy where you are editing and building. The third copy is your local "cached" copy of a remote repository.

