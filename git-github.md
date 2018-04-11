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