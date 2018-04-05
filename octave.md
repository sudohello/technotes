/*
Title: Octave
Decription: Octave
Author: Bhaskar Mangal
Date: 
Tags: Octave
*/

# Octave

~/.octaverc
This file is used to make personal changes to the default Octave environment.
A message will be displayed as each of the startup files is read if you invoke Octave with the --verbose option but without the --silent option.

## Getting Help

* List all functions
```help --list```


* Search for the string STR in the documentation of all functions in the current function search path.
```lookfor```

* you can get more help on the function by simply including the name as an argument to help
```help plot```


* Matrix
> A = [2,0;3,2]
A =

   2   0
   3   2

** Diagonal Matric
> eye(3)
ans =

Diagonal Matrix

   1   0   0
   0   1   0
   0   0   1
