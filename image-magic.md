---
Title: Image Magic
Decription: Image Magic
Author: Bhaskar Mangal
Date: 30th-Jan-2017
Last Updated: 11th-Mar-2019
Tags: Image Magic
---

**Table of Contents**
* TOC
{:toc}


## Image Magic

1. Merge, Split
  - convert images to pdf and vice-versa
  - **Merge and Split PDF documents**
    + https://linuxcommando.blogspot.in/2013/02/splitting-up-is-easy-for-pdf-file.html
    + https://linuxcommando.blogspot.in/2014/01/how-to-split-up-pdf-files-part-2.html
    + https://linuxcommando.blogspot.in/2015/03/how-to-merge-or-split-pdf-files-using.html
    ```bash
    #Merging 2 pdf files (file1 and file2) into a new file (output) is as simple as executing:
    convert file1.pdf file2.pdf output.pdf
    #You can merge a subset of pages instead of the entire input files. Note that page numbers are zero-based
    convert file1.pdf[0] file2.pdf[0-1,3] output.pdf
    # splits up input into 2 files:
    convert input.pdf[0-1] first2output.pdf 
    convert input.pdf[2-3] next2output.pdf
    #
    # https://imagemagick.org/discourse-server/viewtopic.php?t=8707
    #
    convert -density 300 RentalAgreement-2016-17.jpg RentalAgreement-2016-17.pdf
    ```
2. Resize images
  ```bash
  #batch resize
  mogrify -resize 50% *.jpg
  # single image
  convert -resize 50% 1.jpg 1a.jpg
  ```
3. Other Commands
  - **identify**
    + describes the format and characteristics of one or more image files.
  identify

