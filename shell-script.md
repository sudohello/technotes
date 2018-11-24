---
Title: Shell Script
Decription: Shell Script
Author: Bhaskar Mangal
Date: 
Tags: Shell Script
---

**Table of Contents**
* TOC
{:toc}


## Shell Script

## Tricks

1. How do I search a file for a particular linem then comment out using a bash script?

## Multipile line: comment and un-comment
- https://stackoverflow.com/questions/1676632/whats-a-quick-way-to-comment-uncomment-lines-in-vim
- https://stackoverflow.com/questions/2462794/indent-or-comment-several-text-lines-with-vi

down vote
For those tasks I use most of the time block selection.

Put your cursor on the first # character, press CtrlV (or CtrlQ for gVim), and go down until the last commented line and press x, that will delete all the # characters vertically.

For commenting a block of text is almost the same:

First, go to the first line you want to comment, press CtrlV. This will put the editor in the VISUAL BLOCK mode.
Then using the arrow key and select until the last line
Now press ShiftI, which will put the editor in INSERT mode and then press #. This will add a hash to the first line.
Then press Esc (give it a second), and it will insert a # character on all other selected lines.
For the stripped-down version of vim shipped with debian/ubuntu by default, type : s/^/# in the third step instead.


## script-that-exports-enviromental-variables-cannot-export-them
* https://unix.stackexchange.com/questions/399281/script-that-exports-enviromental-variables-cannot-export-them
* https://stackoverflow.com/questions/16618071/can-i-export-a-variable-to-the-environment-from-a-bash-script-without-sourcing-i
* in `env.vars`:
  ```bash
  foo=test
  ```
  * test script:
  ```bash
  eval `cat env.vars`
  echo $foo         # => test
  sh -c 'echo $foo' # => 
  #
  export eval `cat env.vars`
  echo $foo         # => test
  sh -c 'echo $foo' # => test
  #
  # a better one
  export `cat env.vars`
  echo $foo         # => test
  sh -c 'echo $foo' # => test
  ```

## FAQs
* **What is the meaning of IFS=$'\n' in bash scripting?**
  * https://unix.stackexchange.com/questions/184863/what-is-the-meaning-of-ifs-n-in-bash-scripting
  * IFS stands for "internal field separator". It is used by the shell to determine how to do word splitting, i. e. how to recognize word boundaries.
* **Internal Variables**
  * http://tldp.org/LDP/abs/html/internalvariables.html
* **Is double square brackets [[ ]] preferable over single square brackets [ ] in Bash?**
  * https://stackoverflow.com/questions/669452/is-double-square-brackets-preferable-over-single-square-brackets-in-ba
  * `[[` has fewer surprises and is generally safer to use. But it is not portable - POSIX doesn't specify what it does and only some shells support it (beside bash, I heard ksh supports it too). For example, you can do
