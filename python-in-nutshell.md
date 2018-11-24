---
title: Python In Nutshell
---

**Table of Contents**
* TOC
{:toc}


## Python In Nutshell

## Basics
* http://www.astro.ufl.edu/~warner/prog/python.html

### Variables
* Variables in Python follow the standard nomenclature of an alphanumeric name beginning in a letter or underscore.
* Variable names are case sensitive.
* Variables do not need to be declared and their datatypes are inferred from the assignment statement.
* Variable Scope: Most variables in Python are local in scope to their own function or class
* Global Variables: Global variables, however, can be declared with the global keyword.

### Datatypes
Python supports the following data types:
* boolean (True/False)
* integer
* long
* float
* string
* list
* object
* None
* tuple
* dictionary

```python
bool = True
name = "Craig"
age = 26
pi = 3.14159
print(name + ' is ' + str(age) + ' years old.')

# Scope
a = 1
b = 2
def Sum():
   global a, b
   b = a + b
Sum()
print(b)
```

### Statements and Expressions
* print

```python
print "Hello World"
print('Print works with or without parenthesis')
print("and single or double quotes")
print("Newlines can be escaped like\nthis.")
print("This text will be printed"),
print("on one line becaue of the comma.")
```
* input
* raw_input
* The assignment statement: Assigns a value to a variable.
* import

```python
name = raw_input("Enter your name: ")
a = int(raw_input("Enter a number: "))
print(name + "'s number is " + str(a))
a = b = 5
a = a + 4
print a,b

a = b = 5 #The assignment statement
b += 1 #post-increment
c = "test"
import os,math #Import the os and math modules
from math import * #Imports all functions from the math module
```

### Operators

* Arithmatic: `+, -, *, /, and % (modulus), // (modulus)`
* Comparison: `==, !=, <, >, <=, >=`
* Logical: `and, or, not`
* Exponentiation: `**`
* Execution: `os.system('ls -l') #Requires import os`

### Maths
* Maths: Requires `import math`
* Absolute Value: `a = abs(-7.5)`
* Arc sine: `x = asin(0.5) #returns in rads`
* Ceil (round up): `print(ceil(4.2))`
* Cosine: `a = cos(x) #x in rads`
* Degrees: `a = degrees(asin(0.5)) #a=30`
* Exp: `y = exp(x) #y=e^x`
	- https://stackoverflow.com/questions/31951980/what-exactly-does-numpy-exp-do
	- The exponential function is e^x where e is a mathematical constant called Euler's number, approximately 2.718281. This value has a close mathematical relationship with pi and the slope of the curve e^x is equal to its value at every point. np.exp() calculates e^x for each value of x in your input array.
* Floor (round down): `a = floor(a+0.5)`
* Log: `x = log(y); #Natural Log`
   `x = log(y,5); #Base-5 log`
* Log Base 10: `x = log10(y)`
* Max: `mx = max(1, 7, 3, 4) #7`
   `mx = max(arr) #max value in array`
* Min: `mn = min(3, 0, -1, x) #min value`
* Powers: `x = pow(y,3) #x=y^3`
* Radians: `a = cos(radians(60)) #a=0.5`
* Random #: Random number functions require import random
   `random.seed() #Set the seed based on the system time.`
   `x = random() #Random number in the range [0.0, 1.0)`
   `y = randint(a,b) #Random integer in the range [a, b]`
* Round: `print round(3.793,1; #3.8 - rounded to 1 decimal`
   `a = round(3.793,0) #a=4.0`
* Sine: `a = sin(1.57) #in rads`
* Square Root: `x = sqrt(10) #3.16...`
* Tangent: `print tan(3.14)# #in rads`

### Strings

### Arrays
* https://www.thegeekstuff.com/2013/08/python-array/
* Arrays in basic Python are actually lists that can contain mixed datatypes
* Array Indices begin at 0, like other Python sequences (and C/C++). In contrast, in Fortran or Matlab, indices begin at 1.
* Creating lists
	* A list can be created by defining it with [].
	* A numbered list can also be created with the range function which takes start and stop values and an increment.
```python
list = [2, 4, 7, 9]
list2 = [3, "test", True, 7.4]
a = range(5) #a = [0,1,2,3,4]
a = range(10,0,-2) #a = [10,8,6,4,2]
b = range(5,-5,-1) #b = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]
```
* An empty list can be initialized with [] and then the append command can be used to append data to the end of the list:
```python
a=[]
a.append("test")
a.append(5)
print a
```
* Finally, if you want a list to have a predetermined size, you can create a list and fill it with None's:
```python
length=7
a=[None]*length
a[5] = "Fifth"
a[3] = 6
print len(a)
```
* Removing from lists: The pop method can be used to remove any item from the list
* Creating arrays: An array can be defined by one of four procedures: zeros, ones, arange, or array. zeros creates an array of a specified size containing all zeros:
```python
import numpy as np
np.random.randn()  #int
np.random.randn(1) #1D
np.random.randn(1,5) #2D
np.zeros(5) #array([ 0.,  0.,  0.,  0.,  0.])
np.zeros(5,dtype=int) #array([0, 0, 0, 0, 0])
np.ones(5) #array([ 1.,  1.,  1.,  1.,  1.])
np.arange(10,-11,-1) #array([ 10,   9,   8,   7,   6,   5,   4,   3,   2,   1,   0,  -1,  -2, -3,  -4,  -5,  -6,  -7,  -8,  -9, -10])
z=np.arange(10) #array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.append(z,4) #array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4])
```
*  Core Python has an array data structure, but it’s not nearly as versatile, efficient, or useful as the NumPy array. We will not be using Python arrays at all. Therefore, whenever we refer to an “array,” we mean a “NumPy array.”

* Multi-dimensional lists: Because Python arrays are actually lists, you are allowed to have jagged arrays. Multi-dimensional lists are just lists of lists:
```python
a=[[0,1,2],[3,4,5]] #List
type(a) #<type 'list'>
len(a) #length
import numpy as np
z=np.asarray(a)
z.ndim
z.shape
np.size(z)
np.append(z,np.array([0,0]))
#
# Iterate over list
b=[1,3,4,5]
for i in range(len(b)): #range or xrange can be used
	print b[i]
# Slicing
a=[0, 1, 1, 2, 3, 5, 8, 13]
# Syntax: a[start:end:step]
# (-)ve sign means look from the end
#
# Range
range(10)      # makes a list of 10 integers from 0 to 9
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range(3,10)    # makes a list of 10 integers from 3 to 9
#[3, 4, 5, 6, 7, 8, 9]
range(0,10,2)  # makes a list of 10 integers from 0 to 9
                        # with increment 2
#[0, 2, 4, 6, 8]
```

### set
* https://www.programiz.com/python-programming/set

A set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable (which cannot be changed).

However, the set itself is mutable. We can add or remove items from it.

Sets can be used to perform mathematical set operations like union, intersection, symmetric difference etc.

* `add()`, `update()`, `remove()`, `discard()`, `pop()`, `clear()`
* **Union**
  - Union of A and B is a set of all elements from both sets
  - Union is performed using `|` operator. Same can be accomplished using the method `union()`
* **Intersection**
  - Intersection of A and B is a set of elements that are common in both sets
  - Intersection is performed using `&` operator. Same can be accomplished using the method `intersection()`
* **Difference**
  - Difference of A and B (A - B) is a set of elements that are only in A but not in B. Similarly, B - A is a set of element in B but not in A
  - Difference is performed using `-` operator. Same can be accomplished using the method `difference()`
* **Symmetric Difference**
  - Symmetric Difference of A and B is a set of elements in both A and B except those that are common in both
  - Symmetric difference is performed using `^` operator. Same can be accomplished using the method `symmetric_difference()`

```python
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
#
# Union:
# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)
#
# Intersection:
# use & operator
# Output: {4, 5}
print(A & B)
#
# Difference:
# use - operator on A
# Output: {1, 2, 3}
print(A - B)
#
# Symmetric Difference:
# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)
#
A = frozenset([1, 2, 3, 4])
#
# initialize my_set
my_set = set("apple")

# check if 'a' is present
# Output: True
print('a' in my_set)

# check if 'p' is present
# Output: False
print('p' not in my_set)
```
* Membership Test - We can test if an item exists in a set or not, using the keyword `in`
* While tuples are immutable lists, frozensets are immutable sets
* Using a for loop, we can iterate though each item in a set.
* Built-in functions like all(), any(), enumerate(), len(), max(), min(), sorted(), sum() etc. are commonly used with set to perform different tasks


### Tupels
* **Tuples are lists that are immutable**. That is, once defined, the individual elements of a tuple cannot be changed.
* A tuple is written as a sequence of numbers enclosed in round parentheses
* Whereas a list is written as a sequence of numbers enclosed in square brackets
```python
t=(1, 1, 2, 3, 5, 8, 13)
type(t) #<type 'tuple'>
```

### Namedtupels
- https://stackoverflow.com/questions/2970608/what-are-named-tuples-in-python
- https://www.reddit.com/r/Python/comments/38ee9d/intro_to_namedtuple/

* **What are named tuples?**
  * Named tuples are basically easy-to-create, lightweight object types. Named tuple instances can be referenced using object-like variable dereferencing or the standard tuple syntax
  * namedtuple is a factory function for making a tuple class. With that class we can create tuples that are callable by name also
* **How to use them?**
  * They can be used similarly to `struct` or other common record types, except that they are immutable. They were added in Python 2.6 and Python 3.0
  * common to represent a point as a tuple (x, y). This leads to code like the following:
  ```python
  pt1 = (1.0, 5.0)
  pt2 = (2.5, 1.5)
  #
  from math import sqrt
  line_length = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
  ```
  * Using a named tuple it becomes more readable:
  ```python
  from collections import namedtuple
  Point = namedtuple('Point', 'x y')
  pt1 = Point(1.0, 5.0)
  pt2 = Point(2.5, 1.5)
  Point._make([1,2]) ##  Make a namedtuple from a list of values
  #
  from math import sqrt
  line_length = sqrt((pt1.x-pt2.x)**2 + (pt1.y-pt2.y)**2)
  ```
  * named tuples are still backwards compatible with normal tuples, s
  ```python
  line_length = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
  ```python
  use tuple unpacking
  ```python
  x1, y1 = pt1
  ```
* **Why/when should I use named tuples instead of normal tuples?**
  * you should use named tuples instead of tuples anywhere you think object notation will make your code more pythonic and more easily readable
  * You can also replace ordinary immutable classes that have no functions, only fields with them
  * You can use them instead of an object if you would otherwise use an object with unchanging data attributes and no functionality.
  * You can even use your named tuple types as base classes
  * `**_asdict()**`: You may just want to use a dictionary in this situation. Named tuples can be converted to dictionaries using `pt1._asdict()` which returns `{'x': 1.0, 'y': 5.0}` and can be operated upon with all the usual dictionary functions. Or use **slotted object** or **namedlist**
  ```python
  class Point(namedtuple('Point', 'x y')):
    [...]
  ```
  * as with tuples, attributes in named tuples are immutable:
  ```python
  Point = namedtuple('Point', 'x y')
  pt1 = Point(1.0, 5.0)
  pt1.x = 2.0 ## AttributeError: can't set attribute
  pt1._asdict() ## OrderedDict([('x', 1.0), ('y', 5.0)])

  ```
* **Why/when should I use normal tuples instead of named tuples?**
* **Is there any kind of "named list" (a mutable version of the named tuple)?**
  * You're looking for either a slotted object that implements all of the functionality of a statically sized list or a subclassed list that works like a named tuple (and that somehow blocks the list from changing in size.)


### NamedLists
* https://pypi.python.org/pypi/namedlist
```python
from namedlist import namedlist
Point = namedlist('Point', 'x y')
p = Point(1, 3)
p.x = 2
assert p.x == 2
assert p.y == 3
#
# Specific default value for all vields as same
Point = namedlist('Point', 'x y', default=3)
# per field default value
Point = namedlist('Point', [('x', 0), ('y', 100)])
```

### Record Type: `rcdtype`
* http://code.activestate.com/recipes/576555/
```python
from rcdtype import *
Point = recordtype('Point', 'x y')
vars(Point) ## dumps the object
pt1 = Point(1.0, 5.0)
pt1 = Point(1.0, 5.0)
pt1.x = 2.0
print(pt1[0])
```

### Numpy Array
* Numpy Array (**type 'numpy.ndarray'**) is similar to a list but where all the elements of the list are of the same type.
* The elements of a NumPy array, or simply an array, are usually numbers, but can also be boolians, strings, or other objects
* When the elements are numbers, they must all be of the same type. For example, they might be all integers or all floating point numbers.
```python
import numpy as np
x=[1,2,3,4,5]
a=np.array(x)
```
* **linspace or logspace functions**
	* The linspace function creates an array of N evenly spaced points between a starting point and an ending point. The form of the function is linspace(start, stop, N). If the third argument N is omitted, then N=50.
```python
linspace(0, 10, 5) # array([  0. ,  2.5,  5. ,  7.5, 10. ])
```
	* logspace that produces evenly spaced points on a logarithmically spaced scale. The arguments are the same as those for linspace except that start and stop refer to a power of 10. That is, the array starts at $10^{\mathrm{start}}$ and ends at $10^{\mathrm{stop}}$.
* **arange**
The third way arrays can be created is using the NumPy arange function, which is similar to the Python range function for creating lists.
	* arange(start, stop, step). If the third argument is omitted step=1. If the first and third arguments are omitted, then start=0 and step=1.


#### References
* http://www.physics.nyu.edu/pine/pymanual/html/chap3/chap3_arrays.html


## Careful TIps
* Note though, that as per **[PEP8](https://www.python.org/dev/peps/pep-0008/)** a single underscore is considered a “weak "internal use" indicator” with its own behavior. Careful when making use of functions that start with ` _!`

## PEP8
* https://www.python.org/dev/peps/pep-0008/

## FAQ's
* **OOPS in python**
  * http://dirtsimple.org/2004/12/python-is-not-java.html
* **Python Module vs Class and when to use them**
  * https://softwareengineering.stackexchange.com/questions/329348/classes-vs-modules-in-python
  * You can create multiple instances of a class, but you cannot create instances of a module. You could compare modules to static classes or singletons.
* **Dynamic Loading module, class**
  * https://stackoverflow.com/questions/8790003/dynamically-import-a-method-in-a-file-from-a-string
  * https://docs.python.org/3.5/library/importlib.html
* **Paths**
```python
import os
os.path.dirname(__file__) # relative directory path
os.path.abspath(__file__) # absolute file path
os.path.basename(__file__) # the file name only
## full current dir path
os.path.dirname(os.path.abspath(__file__))
```
* **Importing files from different folder**
  * https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
  ```python
  # some_file.py
  import sys
  sys.path.insert(0, '/path/to/application/app/folder')
  import file
  ##
  ## OR
  sys.path.append('/path/to/application/app/folder')
  ```
  * When modules are in parallel locations
  ```python
  import sys
  sys.path.append('../')
  ```
* **listing content of directories**
  - https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
  ```python
  import glob, os
  os.chdir("/mydir")
  for file in glob.glob("*.txt"):
      print(file)

  import os
  for file in os.listdir("/mydir"):
      if file.endswith(".txt"):
          print(os.path.join("/mydir", file))

  import os
  for root, dirs, files in os.walk("/mydir"):
      for file in files:
          if file.endswith(".txt"):
               print(os.path.join(root, file))
  ```
* one-line-list-comprehension-if-else-variants
  * https://stackoverflow.com/questions/17321138/one-line-list-comprehension-if-else-variants
  * x if y else z is the syntax for the expression you're returning for each element. Thus you need:
  ```python
  [ x if x%2 else x*100 for x in range(1, 10) ]
  ```
  * The confusion arises from the fact you're using a filter in the first example, but not in the second. In the second example you're only mapping each value to another, using a ternary-operator expression.
  * With a filter, you need:
  ```python
  [ EXP for x in seq if COND ]
  ```
  * Without a filter you need:
  ```python
  [ EXP for x in seq]
  ```
* **Matplotlib: save plot to numpy array**
  * https://stackoverflow.com/questions/7821518/matplotlib-save-plot-to-numpy-array
* **how-to-downcase-the-first-character-of-a-string?**
  * https://stackoverflow.com/questions/3840843/how-to-downcase-the-first-character-of-a-string
  ```python
  ## One-liner which handles empty strings and None
  fclower = lambda s: s[:1].lower() + s[1:] if s else ''
  fclower(None) # ''
  fclower('') # ''
  fclower('MARTINEAU') # 'mARTINEAU'
  #
  fcupper = lambda s: s[:1].upper() + s[1:] if s else ''
  ```
* **How to convert one data type to other data type?**
  * https://www.datacamp.com/community/tutorials/python-data-type-conversion
* **How to split string to various data types?**
  * https://stackoverflow.com/questions/34515139/split-string-to-various-data-types
  * List comprehension: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
  * https://docs.python.org/3/library/stdtypes.html#str.isdigit
  ```python
  y='1;0.9971295;1920;1080;126.76472;150.67957;118.44906;111.22757'
  [int(i) if i.isdigit() else i for i in s.split('|')]
  #
  ```
* **How to join a list of strtings or numbers to a string?**
  * https://stackoverflow.com/questions/3590165/join-a-list-of-items-with-different-types-as-string-in-python
  ```python
  x=[1,2,3,4,]
  print ';'.join(str(i) for i in x)
  #
  y=['1', '2', '3', '4']
  ";".join(y)
  #
  ```
* **How to detect empty generators?**
  * no simple way
  * https://bytes.com/topic/python/answers/44490-empty-lists-vs-empty-generators
  * create a flag; loop and change the flag, break; check the flag
* **How to delete Files?**
  ```python
  os.path.exists(fileName) and os.remove(fileName)
  ```
* **How to insert at index in a List?**
  * https://stackoverflow.com/questions/14895599/insert-an-element-at-specific-index-in-a-list-and-return-updated-list
  ```python
  a = [1, 2, 4]
  b = a[:]
  b.insert(2, 'a') # [1, 2, 'a', 4]
  ```
* **How to Convert List to Dicitionary?**
  * https://stackoverflow.com/questions/4576115/convert-a-list-to-a-dictionary-in-python
```python
a='l;m;n'.split(';')
b={a[i]: i for i in range(0, len(a), 1)} ## b={'m': 1, 'l': 0, 'n': 2}
```
* **How to preserve order in dicitionary?: Use ordereddict**
  * https://pymotw.com/2/collections/ordereddict.html
  * https://stackoverflow.com/questions/15711755/converting-dict-to-ordereddict
  * YAML - orderedlist: https://gist.github.com/oglops/c70fb69eef42d40bed06
  * https://stackoverflow.com/questions/5121931/in-python-how-can-you-load-yaml-mappings-as-ordereddicts
  ```python
  import collections

  print 'Regular dictionary:'
  d = {}
  d['a'] = 'A'
  d['b'] = 'B'
  d['c'] = 'C'
  d['d'] = 'D'
  d['e'] = 'E'

  for k, v in d.items():
      print k, v

  print '\nOrderedDict:'
  d = collections.OrderedDict()
  d['a'] = 'A'
  d['b'] = 'B'
  d['c'] = 'C'
  d['d'] = 'D'
  d['e'] = 'E'

  for k, v in d.items():
      print k, v
  ```
* **How to find the version of installed library?**
```python
import pandas as pd
pd.__version__
```
* **What are different file read and write modes?**
  * https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
  * `r` read only
  * `w` write only
  * `a` append
  * `r+` reading, and writing both
  * `b` is for binary
  * `rb`, `r+b` mode is open the binary file in read or write mode
  * `wb`
  * On Unix, it doesn’t hurt to append a 'b' to the mode, so you can use it platform-independently for all binary files
  * On Windows makes a distinction between text and binary files; the end-of-line characters in text files are automatically altered slightly when data is read or written.
* **How to read/edit EXIF and Custom Metatags in image?**
  * https://stackoverflow.com/questions/27815719/editing-updating-the-data-of-photo-metadata-using-pyexiftool
  * https://github.com/ianare/exif-py
  * https://stackoverflow.com/questions/28588696/python-exiftool-combining-subject-and-keyword-tags
  * **Custom Meta Tags**
  * https://stackoverflow.com/questions/8586940/writing-complex-custom-metadata-on-images-through-python#8590271
  * https://stackoverflow.com/questions/9808451/how-to-add-custom-metadata-to-opencv-numpy-image
  * https://wiki.gnome.org/Projects/gexiv2
* **How to list only files in a directory?**
  * https://stackoverflow.com/questions/14176166/list-only-files-in-a-directory
* **How to check empty Variables?**
  * https://stackoverflow.com/questions/9573244/most-elegant-way-to-check-if-the-string-is-empty-in-python
  * https://stackoverflow.com/questions/10545385/how-to-check-if-a-variable-is-empty-in-python
  * mpty strings are "falsy" which means they are considered false in a Boolean context, so you can just do this:
  ```python
  if myString == "":
  ``` 
* **Compare string with all values in an array**
  * https://stackoverflow.com/questions/2783969/compare-string-with-all-values-in-array
  * If you only want to know if any item of d is contained in paid[j], as you literally say:
    ```python
    if any(x in paid[j] for x in d):
    ```
  * If you also want to know which items of d are contained in paid[j]:
    ```python
    contained = [x for x in d if x in paid[j]]
    ```
  * get the first item of d contained in paid[j] - (and None if no item is so contained)
    ```python
    firstone = next((x for x in d if x in paid[j]), None)
    ```
* **How to read and preocess a huge csv file?**
  * https://stackoverflow.com/questions/17444679/reading-a-huge-csv-file
  * Reading all rows into a list, then processing that list. **Don't do that**
  * Process your rows as you produce them. If you need to filter the data first, use a generator function:
  ```python
  import csv

  def getstuff(filename):
    with open(filename, "rb") as f:
      datareader= csv.reader(f)
      yield next(datareader) # yield the header row
      for row in datareader:
        yield row

  for row in getstuff("sample.csv"):
    print(row)
  ```
  * https://stackoverflow.com/questions/8009882/how-to-a-read-large-file-line-by-line-in-python#8010133
  ```python
  with open("sample.csv",'r') as f:
  for line in f:
    print(line)
  ```
* **How to check and create directories?**
  * https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output
  * https://docs.python.org/3/library/os.html#os.makedirs

* **How to view all the defined variables in python shell?**
```python
dir() #will give you the list of in scope variables:
globals() #will give you a dictionary of global variables
locals() #will give you a dictionary of local variables
vars()
vars().keys()
vars().values()
```
	* https://stackoverflow.com/questions/633127/viewing-all-defined-variables
* **How to create function with optional arguments?**
  * https://stackoverflow.com/questions/9539921/how-do-i-create-a-python-function-with-optional-arguments
* **How to install using `pip`?**
```shell
sudo pip install numpy
```
* **How to setup & publish project dependencies?**
	* create txt file, say name requirements, each line mention package name ex: ploty=version (optional)
```shell
sudo pip install -r requirements
```
* **List all python pakages**
```bash
pip freeze
pip list
```
* **Which version of python should pip point to, by default? Can it be changed?**
* **How to reinstall pip? How to fix `pip` topoint to python2 instead of python3, when python points to v2 and python3 points to v3?**
- https://askubuntu.com/questions/780502/ubuntu-16-pip-install-installs-to-python-3-instead-of-2
```bash
pip freeze
pip list
#
pip -V
#pip 10.0.0 from /home/game/.local/lib/python3.5/site-packages/pip (python 3.5)
#
pip2 -V
#pip 10.0.0 from /home/game/.local/lib/python2.7/site-packages/pip (python 2.7)
#
sudo python -m pip install -U --force-reinstall pip
```

* **Which python points to which version**
```bash
python -V
#Python 2.7.12
#
python2 -V
#Python 2.7.12
#
python3 -V
#Python 3.5.2
```
* **How to preserve files downloaded by pip after failed installation?** 
- https://superuser.com/questions/769565/how-to-preserve-files-downloaded-by-pip-after-failed-installation
```bash
sudo pip install -d $HOME/softwares/pip-cache
sudo pip3 install -d $HOME/softwares/pip-cache
```

* **How to automatically-creating-directories-with-file-output?
- https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output
```python
import os
import errno

filename = "/foo/bar/baz.txt"
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

with open(filename, "w") as f:
    f.write("FOOBAR")
```


## TIPs
* Use python shell to learn and ``help()`` command to learn the details of the functions


## Setting up for Web Application development
- https://optimalbi.com/blog/2016/03/31/apache-meet-python-flask/
- [scientific packages](https://www.nyayapati.com/srao/2014/05/how-to-install-numpy-scipy-pandas-matplotlib-and-scikit-learn-on-mavericks/)
- http://geoffboeing.com/2016/03/scientific-python-raspberry-pi/
- https://unix.stackexchange.com/questions/37313/how-do-i-grep-for-multiple-patterns-with-pattern-having-a-pipe-character
- https://www.thegeekstuff.com/2011/10/grep-or-and-not-operators/
```bash
sudo pip install numpy
sudo pip install scipy
sudo pip install pandas
sudo pip install matplotlib
sudo pip install scikit-learn
sudo pip install Flask
#
pip list | grep -E 'numpy|scipy|pandas|matplotlib|scikit-learn|Flask'
sudo pip list --format=legacy | grep -E 'h5py|pillow|numpy|scikit-learn|tensorflow|keras|cv2'
sudo pip list --format=columns | grep -E 'h5py|pillow|numpy|scikit-learn|tensorflow|keras|cv2'
#
#Flask                         0.12.2     
#matplotlib                    2.2.2      
#numpy                         1.14.2     
#pandas                        0.22.0     
#scikit-learn                  0.19.1     
#scipy                         1.0.1      
```
* **Install form the directory**
```bash
sudo pip install `ls -1 | tr '\n' ' '`
```

**Natural Language Toolkit**
- https://www.nltk.org/

**Installing scikit-learn; Python Data Mining Library**
- https://calebshortt.com/2016/01/15/installing-scikit-learn-python-data-mining-library/
```python
import scipy
scipy.__version__
'1.0.1'
#
import numpy as np
np.__version__
'1.14.2'
#
import flask
flask.__version__
'0.12.2'
```
**Templating Engine**
* Jinja
  - Jinja is a **template engine** for the Python programming language and is licensed under a BSD License created by Armin Ronacher. It is similar to the Django template engine but provides Python-like expressions while ensuring that the templates are evaluated in a sandbox. It is a text-based template language and thus can be used to generate any markup as well as sourcecode.


## Basic Python Concepts

**Book notes**
1. ScipyLectures-simple.pdf

**List Comprehensions**
`[i**2 for i in range(4)]`

**Mutable Types**
- dictionary
- list

**IMMutable Types**
- sting
- tuble: Tuples are lists that are immutable

**Standalone scripts may also take command-line arguments**
- Importing objects from modules
```python
import sys
print sys.argv
#
# Don’t implement option parsing yourself. Use modules such as optparse , argparse or
:mod‘docopt‘.
#
import os
os.listdir('.')
dir(os)
```

### **Modules & Packages**
* https://www.programiz.com/python-programming/modules

**What are modules in Python?**
Modules refer to a file containing Python statements and definitions.

A file containing Python code, for e.g.: example.py, is called a module and its module name would be example.

We use modules to break down large programs into small manageable and organized files. Furthermore, modules provide reusability of code.

We can define our most used functions in a module and import it, instead of copying their definitions into different programs.

- Modules are cached: if you modify demo.py and re-import it in the old session, you will get the old one.
```python
reload(demo)
```
- Sometimes we want code to be executed when a module is run directly, but not when it is imported by another module. if __name__ == '__main__' allows us to check whether the  module is being run directly.
```python
if __name__ == '__main__':
	do_something_here
```
- A directory that contains many modules is called a package
- A package is a module with submodules (which can have submodules themselves, etc.)
- A special file called __init__.py (which may be empty) tells Python that the directory is a Python package, from which modules can be imported.
```python
import scipy
scipy.__file__
#
import scipy.ndimage.morphology
#
from scipy.ndimage import morphology
```

### **Standard Library**
* **os module**
	- operating system functionality - A portable way of using operating system dependent functionality.
```python
os.getcwd() #Current directory: #(returns "a string representing the current working directory")
os.chdir(path) #("change the current working directory to path")
os.listdir(os.curdir) #List a directory
os.mkdir('junkdir') #Make a directory:
os.rename('junkdir', 'foodir') #Rename the directory
os.rmdir('foodir') #Delete directory
os.remove('junk.txt') #Delete file
#
# os.path: path manipulations
# os.path provides common operations on pathnames.
a = os.path.abspath('junk.txt')
os.path.split(a)
os.path.dirname(path) #(returns "the directory name of pathname path")
os.path.realpath(path) #(returns "the canonical path of the specified filename, eliminating any symbolic links encountered in the path")
os.path.basename(a)
os.path.splitext(os.path.basename(a))
os.path.exists('junk.txt')
os.path.isfile('junk.txt')
os.path.isdir('junk.txt')
os.path.expanduser('~/local')
os.path.join(os.path.expanduser('~'), 'local', 'bin')
#
## The  constants:
__file__
#
## To get the full path to the directory a Python file is contained in, write this in that file
dir_path = os.path.dirname(os.path.realpath(__file__))
#
# Running an external command
#
os.system('ls')
#
# Walking a directory
# os.path.walk generates a list of filenames in a directory tree
#
for dirpath, dirnames, filenames in os.walk(os.curdir):
	for fp in filenames:
		print os.path.abspath(fp)
#
# Environment Variables
#
os.environ['PYTHONPATH']
os.getenv('PYTHONPATH')
```

* **urllib**
- URL handling library
```python
import urllib
import os

file = 'airfares.txt'
url = 'http://www.stat.ufl.edu/~winner/data/airq4.dat'
if not os.path.exists(file):
	urllib.urlretrieve(url,file)
#
data = pandas.read_csv(file,sep=' +',header=0,names=['city1', 'city2', 'pop1', 'pop2','dist', 'fare_2000', 'nb_passengers_2000','fare_2001', 'nb_passengers_2001'])
data = pandas.read_csv(file,sep=' +',header=0,names=['city1', 'city2', 'pop1', 'pop2','dist', 'fare_2000', 'nb_passengers_2000','fare_2001', 'nb_passengers_2001'])
#
```
__main__:1: ParserWarning: Falling back to the 'python' engine because the 'c' engine does not support regex separators (separators > 1 char and different from '\s+' are interpreted as regex); you can avoid this warning by specifying engine='python'.

* **sh module**
  - Which provides much more convenient ways to obtain the output, error stream and exit code of the external command.
```python
#
# Alternative to os.system
#
import sh
com = sh.ls()
print com.exit_code
```
* **shutil**
  - high-level file operations
	- The shutil provides useful file operations:
		- shutil.rmtree : Recursively delete a directory tree.
		- shutil.move : Recursively move a file or directory to another location.
		- shutil.copy : Copy files or directories.

* **glob**
  - Pattern matching on files
	- The glob module provides convenient file pattern matching. example: Find all files ending in .txt
```python
import glob
glob.glob('*.txt')
```

* **sys module**
	- system-specific information
  - System-specific information related to the Python interpreter
  - Which version of python are you running and where is it installed
```python
import sys
sys.platform
sys.version
sys.prefix
sys.argv # List of command line arguments passed to a Python script
sys.path # List of strings that specifies the search path for modules. Initialized from PYTHONPATH
```

* **pickle**
  - easy persistence
  - Useful to store arbitrary objects to a file
  - **Not safe or fast!**
  - **TBD**: alternative to pickle
```python
import pickle
l = [1, None, 'Stan']
pickle.dump(l, file('test.pkl', 'w'))
pickle.load(file('test.pkl'))
```
* **timeit**
- https://docs.python.org/2/library/timeit.html
```python
import timeit
timeit.timeit(stmt='t=[i**2 for i in range(1000)]',number=100)
timeit.timeit(stmt='t=[i**2 for i in range(1000)]',number=1000)
timeit.timeit(stmt='t=[i**2 for i in range(1000)]',number=10000)
```

**Exception Handling**
- Exceptions are raised by errors in Python
- There are different types of exceptions for different errors
- Capturing and reraising an exception
- Use exceptions to notify certain conditions are met (e.g. StopIteration) or not (e.g. custom error raising)

**Object-oriented programming (OOP)**
- Python supports object-oriented programming (OOP)
- class, methods, attributes
- constructor: `__init__`

**Iterators, generator expressions and generators**
* **Iterator**
	- An iterator is an object adhering to the iterator protocol — basically this means that it has a next method, which, when called, returns the next item in the sequence, and when there’s nothing to return, raises the StopIteration exception.
	- When used in a loop, StopIteration is swallowed and causes the loop to finish. But with explicit invocation,
we can see that once the iterator is exhausted, accessing it raises an exception.
```python
num=[1,2,3]
it=iter(num)
next(it)
next(it)
next(it)
next(it) # StopIteration Exception
```
* **Generator expressions**
	- A second way in which iterator objects are created is through generator expressions
	- the basis for list comprehensions
	- a generator expression must always be enclosed in parentheses or an expression
	- If round parentheses are used, then a generator iterator is created
	- If rectangular parentheses are used, the process is short-circuited and we get a list
	- The list comprehension syntax also extends to dictionary and set comprehensions
	- A set is created when the generator expression is enclosed in curly braces
	- A dict is created when the generator expression contains “pairs” of the form key:value.
```python
(i for i in num) # generator is created
[i for in num] # list is created
#
{i for i in range(3)} # set is created: set([0, 1, 2])
#
# in old Pythons the index variable ( i ) would leak, and in versions >= 3 this is fixed.
{i:i**2 for i in range(3)} # dictionary is created: {0: 0, 1: 1, 2: 4}
```
* **Generators**
	- A generator is a function that produces a sequence of results instead of a single value
	- A third way to create iterator objects is to call a generator function
	- A generator is a function containing the keyword `yield`
	- When a normal function is called, the instructions contained in the body start to be executed. When a generator is called, the execution stops before the first instruction in the body.
	- An invocation of a generator function creates a generator object, adhering to the iterator protocol.
	- As with normal function invocations, concurrent and recursive invocations are allowed
	- When next is called, the function is executed until the first yield 
	- Each encountered yield statement gives a value becomes the return value of next
	- After executing the yield statement, the execution of this function is suspended
	- execution is strictly single-threaded, but the interpreter keeps and restores the state in between the requests for the next value
	- Usefulness: it is easier for the author of the generator to understand the state which is kept in local variables, as opposed to instance attributes, which have to be used to pass data between consecutive invocations of next on an iterator object
	- When an iterator is used to power a loop, the loop becomes very simple
	- When the generator resumes execution after a yield statement, the caller can call a method on the generator object to either pass a value into the generator, which then is returned by the yield statement, or a different method to inject an exception into the generator
	- `throw(type, value=None, traceback=None)`
	- `send(value)` equivalent to `g.next() and g.send(None)` # raise type, value, traceback
	- `close()` method, which can be used to force a generator that would otherwise be able to provide more values to finish immediately
```python
def f():
	yield 1
	yield 2
#
gen=f()
#
next(f)	# 1
next(f) # 2
next(f) # StopIteration
```

* **Decorators**
  - Since functions and classes are objects, they can be passed around. Since they are mutable objects, they can be modified. The act of altering a function or class object after it has been constructed but before it is bound to its name is called decorating
  - Decorators can be applied to functions and to classes
  - Decorators can be stacked — the order of application is bottom-to-top, or inside-out.
  - The only requirement on decorators is that they can be called with a single argument

* **Context managers**: `with` statement
	- A context manager is an object with __enter__ and __exit__ methods which can be used in the with statement
	- Use cases:
		* Using generators to define context managers: use a decorator to turn generator functions into context managers
```python
with manager as var:
  do_something(var)
#
# simplest case equivalent to
var = manager.__enter__()
try:
	do_something(var)
finally:
	manager.__exit__()
#
# calls close and can be used as a context manager itself
with open('/tmp/file', 'a') as f:
	f.write('more contents\n')
```

* **Others**
```python
# Return a list of tuples, where each tuple contains the i-th element
## from each of the argument sequences.  The returned list is truncated
### in length to the length of the shortest argument sequence.
#
zip
```

### Debugging

* pyflakes
	- Detects syntax errors, missing imports, typos on names
	- Integrating pyflakes (or flake8) in your editor or IDE is highly recommended, it does yield productivity gains.
* pylint
* pychecker
* pyflakes
* flake8
* nosetests
* gdb for the C-debugging part
* python debugger, pdb
	- https://docs.python.org/library/pdb.html
* pycharm
  - https://www.jetbrains.com/help/pycharm/debugging-your-first-python-application.html

**Debugging segmentation faults using gdb - Pg322**
- http://wiki.python.org/moin/DebuggingWithGdb


You can launch a Python program through pdb by using pdb myscript.py or python -m pdb myscript.py.

There are a few commands you can then issue, which are documented on the pdb page.

Some useful ones to remember are:

b: set a breakpoint
c: continue debugging until you hit a breakpoint
s: step through the code
n: to go to next line of code
l: list source code for the current file (default: 11 lines including the line being executed)
u: navigate up a stack frame
d: navigate down a stack frame
p: to print the value of an expression in the current context

If you don't want to use a command line debugger, some IDEs like Pydev have a GUI debugger.



### Optimizing Code
- http://packages.python.org/line_profiler/
- https://docs.python.org/library/timeit.html
- No optimization without measuring! Measure: profiling, timing
- use timeit to time elementary operations:
- with switches -l, --line-by-line and -v, --view to use the line-by-line profiler and view the results in addition to saving them
- Profiler: `cProfile`
```bash
python -m cProfile -o demo.prof demo.py
```

**Commonly encountered tricks to make code faster**
- moving computation or memory allocation outside a for loop
- Vectorizing for loops
	* Find tricks to avoid for loops using numpy arrays. For this, masks and indices arrays can be useful.
- Broadcasting
	* Use broadcasting to do operations on arrays as small as possible before combining them.
- Be easy on the memory: use views, and not copies
	* Copying big arrays is as costly as making simple numerical operations on them
- Beware of cache effects
	* Memory access is cheaper when it is grouped: accessing a big array in a continuous way is much faster than random access. This implies amongst other things that smaller strides are faster

### Sparse Matrices
- scipy.sparse
- PyAMG
- Pysparse

## NumPy
- creating and manipulating numerical data
- NumPy, the core tool for performant numerical computing with Python
- closer to hardware (efficiency)
- designed for scientific computation (convenience)
- Memory-efficient container that provides fast numerical operations
- **Applications:**
	- values of an experiment/simulation at discrete time steps
	- signal recorded by a measurement device, e.g. sound wave
	- pixels of an image, grey-level or colour
	- 3-D data measured at different X-Y-Z positions, e.g. MRI scan
- Different data-types allow us to store data more compactly in memory, but most of the time we simply work with floating point numbers.
- The default data type for number array is floating point
- Few datatypes:
```python
dtype('int64')
dtype('float64')
dtype('complex128')
dtype('bool')
dtype('S7') #strings containing max. 7 letters
#
int32
int64
uint32
uint64
```
- Array Indices begin at 0, like other Python sequences (and C/C++). In contrast, in Fortran or Matlab, indices begin at 1.
- Usual python idiom for reversing a sequence is supported
- For multidimensional arrays, indexes are tuples of integers
- In 2D, the first dimension corresponds to rows, the second to columns.
- for multidimensional a , a[0] is interpreted by taking all elements in the unspecified dimensions.
- Slicing: Arrays, like other Python sequences can also be sliced
- A slicing operation creates a view on the original array, which is just a way of accessing array data. Thus the original array is not copied in memory.
- The axes of an array describe the order of indexing into the array e.g. acis refers to the first index coodrinate
- The shape of an array is a tuple indicating the number of elements along each axis.
- An existing array `a` has an attribute `a.shape` which contains this tuples
- Array functions
```python
import numpy as np
#
np.lookfor('create array')
#
help(np.array)
#
# 1-D Array
a = np.array([0, 1, 2, 3])	# 1D
b = np.array([[0, 1, 2], [3, 4, 5]]) #2D: 2 x 3 array
c = np.array([[[1], [2]], [[3], [4]]])	#3D
type(a)
a.ndim
a.shape
a.dtype
np.shape(a)
len(a)
#
# Evenly spaced
a = np.arange(10) # 0 .. n-1 (!)
a[2:9:3] # [start:end:step]
#
# by number of points
np.linspace(0, 1, 6) # start, end, num-points
np.linspace(0, 1, 5, endpoint=False)
#
np.ones((3, 3)) # reminder: (3, 3) is a tuple
np.zeros((2, 2))
np.eye(3)
np.diag(np.array([1, 2, 3, 4]))
np.random.rand(4) # Gaussian
np.random.seed(1234) # Setting the random seed
#
np.lookfor(np.empty)
help(np.empty)
#
# explicitly specify which data-type
np.array([1, 2, 3], dtype=float)
#
# complex number/datatype
np.array([1+2j, 3+4j, 5+6*1j])
#
# Exercise
# Odd number counting backwards using np.linspace
np.linspace(1,20,20,dtype='int')[::2][::-1]
# Even number counting forward using np.linspace
np.linspace(2,21,20,dtype='int')[::2]
#
np.arange(0,51,10)[:,np.newaxis]
#
# Tiling array
# np.tile
a=np.array([(4,3),(2,1)])
np.tile(a,(2,3))
```
- `np.may_share_memory()` to check if two arrays share the same memory block. Note  however, that this uses heuristics and may give you false positives.
- NumPy arrays can be indexed with slices, but also with boolean or integer arrays (masks). This method is called fancy indexing. It creates copies not views
```python
import numpy as np
#
# copy(); np.copy()
a=np.arange(10)
c=a[::2].copy()
#
# np.may_share_memory
np.may_share_memory(a,c)
np.sqrt
np.nonzero
#
# Return an array representing the indices of a grid.
x, y = np.indices((1, 1))
#
np.searchsorted
#
```
- **masking:** Indexing with a mask can be very useful to assign a new value to a sub-array
- NumPy arrays can be indexed with slices, but also with boolean or integer arrays (masks). This method is called **fancy indexing**. It creates copies not views
```python
import numpy as np
np.random.seed(3)
a=np.random.randint(0, 21, 15) # 15 numbers between 0 and 21
mask=(a%3==0)
extract_from_a = a[mask]
a[mask] = 0
```
- Indexing can be done with an array of integers, where the same index is repeated several time
```python
import numpy as np
a = np.arange(0, 100, 10)
a[[2, 3, 2, 4, 2]]
a[[7,9]]=0
a[[7,9]]=[70,90]
```
- When a new array is created by indexing with an array of integers, the new array has the same shape as the array of integers
```python
import numpy as np
a=np.arange(10)
idx=np.array([[3,4],[9,7]])
idx.shape
a[idx]
```
- **Numerical operations on arrays**
- Elementwise operations: Basic operations on numpy arrays (addition, etc.) are elementwise
```python
import numpy as np
x=np.arange(1,11) # (start,stop,step)
x+1
x-2
x*2
x**2
2**x
#
# Array-wise comparisons
y=np.arange(1,11)
x==y
x>y
np.array_equal(x,y)
#
# Logical operations
np.logical_or(x,y)
np.logical_and(x,y)
np.all([True, True, False]) # Test whether `all` array elements along a given axis evaluate to True
np.any([True, True, False]) #  Test whether `any` array element along a given axis evaluates to True
#
# Transcendental functions
np.sin(x)
np.log(x)
np.exp(x)
#
# Computing sums
x=np.arange(5)
np.sum(x)
x.sum()
#
# Sum by rows and by columns
x=np.array([[1,1],[2,2]])
x.sum(axis=0) # columns (1st dimension)
x.sum(axis=1) # rows (2nd dimension)
#
# Unique Values
np.unique(x)
#
# cummulative sum
x.cumsum()
#
# Same idea in higher dimensions
#
x=np.array([[1,2],[3,4]])
x.min()
x.min(axis=0)
x.min(axis=1)
x.max()
x.max(axis=0)
x.max(axis=1)
x.argmin() # index of minimum
x.argmax() # index of maximum
#
# Datatype
a=np.arange(10)
a.shape,type(a),a.ndim,a.dtype # ((10,), <type 'numpy.ndarray'>, 1, dtype('int64'))
#
b=np.arange(10).astype(float) # ((10,), <type 'numpy.ndarray'>, 1, dtype('float64'))
b.shape,type(b),b.ndim,b.dtype
```
- Array multiplication is not matrix multiplication
- Array multiplication is Elementwise operations
```python
import numpy as np
x=np.ones((3,3))
c*c
c**c # c to the power of c
```
- Matrix multiplication
```python
c.dot(c)
```
- **Transposition**
- The transposition is a view
```python
import numpy as np
help(np.triu) # Upper triangle of an array
help(np.tril) # Lower triangle of an array
x=np.ones((3,3))
np.triu(x)
a=np.triu(x,1)
a.T
```
- **Some Useful Transformations**
```python
# Flip array in the up/down direction.
np.flipud(x)
```
- **Linear algebra**
- `numpy.linalg` implements basic linear algebra such as solving linear systems, singular value  decomposition, etc. However, it is not guaranteed to be compiled using efficient routines
- instead of `numpy.linalg` use of `scipy.linalg`
- **Statistics**
```python
import numpy as np
x=np.arange(1,11)
#
x.mean()
np.mean(x)
#
x.median() # AttributeError: 'numpy.ndarray' object has no attribute 'median'
np.median(x)
#
x.std()
np.std(x)
#
np.random.normal(0,1,n)
np.random.uniform(0.5, 1.0, n)
```
- **loading data**
- [populations.txt](https://www.scipy-lectures.org/_downloads/populations.txt)
```python
import numpy as np
data=np.loadtxt('data/populations.txt')
year, hares, lynxes, carrots = data.T # trick: columns to variables
#
import matplotlib.pyplot as plt
plt.axes([0.2,0.1,0.5,0.8])
plt.plot(year, hares, year, lynxes, year, carrots)
plt.legend(('Hare','Lynx','Carrot'),loc=(1.05,0.5))
plt.show()
```
- **Broadcasting**
- It’s also possible to do operations on arrays of different sizes if NumPy can transform these arrays so that they all have the same size: this conversion is called broadcasting.
- to solve a problem whose output data is an array with more dimensions than input data
- A lot of grid-based or network-based problems can also use broadcasting.
- Some Errors in broadcasting
	* IndexError: shape mismatch: indexing arrays could not be broadcast together with shapes (384,) (512,)
```python
import numpy as np
a = np.tile(np.arange(0, 40, 10), (3, 1)).T
b = np.array([0, 1, 2])
a+b
```
- For instance, if we want to compute the distance from the origin of points on a 10x10 grid, we can do:
- `np.ogrid()` function allows to directly create vectors x and y of the previous example, with two “significant dimensions”
- `np.mgrid` directly provides matrices full of indices for cases where we can’t (or don’t want to) benefit from broadcasting
- `np.mgrid`, `np.ogrid`, `np.meshgrid`
```python
import numpy as np
import matplotlib.pyplot as plt
x, y = np.arange(5), np.arange(5)[:, np.newaxis] # defining x and y variables in a single line
distance = np.sqrt(x ** 2 + y ** 2) # linear distance formula
plt.pcolor(distance)
plt.colorbar()
plt.show()
#
# np.ogrid
x,y=np.ogrid[0:5,0:5]
#
# np.mgrid
x1,y1=np.mgrid[0:5,0:5]
#
#
n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)
```
- **Array shape manipulation**
- ++Flattening++: Higher dimensions: last dimensions ravel out “first”.
- ++Reshaping++: ndarray.reshape may return a view or copy. To understand this you need to learn more about the memory layout of a numpy arrays
- ++Adding a dimension++: Indexing with the `np.newaxis` object allows us to add an axis to an array
- ++Dimension shuffling++:
- ++Resizing++: Size of an array can be changed with `ndarray.resize`
- ++Sorting data++: `np.sort`
- `np.argsort, np.argmax, np.argmin, np.random.shuffle(a),  np.random.random`
```python
import numpy as np
#
# Flattening
a = np.array([[1, 2, 3], [4, 5, 6]])
a.ravel()
a.T.ravel()
a.flatten()
#
# Reshaping
a.ravel().reshape((2,3))
a.ravel().reshape((2,-1)) # unspecified (-1) value is inferred
#
# Adding a dimension
z = np.array([1, 2, 3])
z[:,np.newaxis]
#
# Dimension shuffling
a = np.arange(4*3*2).reshape(4, 3, 2)
b = a.transpose(1, 2, 0)
#
# Resizing
a = np.arange(4)
a.resize((8,))
#
# others
## Generate a NumPy array of 10,000 random numbers
b=np.random.randint(1000, size=10000)
a=np.random.randint(0,40,10)
a
np.random.shuffle(a)
a
np.max(a) # max value
np.argmax(a) # index of max value
a[np.argmax(a)]==a.max()
```
-  As a general rule, NumPy should be used for larger lists/arrays of numbers, as it is significantly more memory efficient and faster to compute on than lists.
- **How to square or raise to a power (elementwise) a 2D numpy array?**
  - https://stackoverflow.com/questions/25870923/how-to-square-or-raise-to-a-power-elementwise-a-2d-numpy-array
  - The fastest way is to do `a*a` or `a**2` or `np.square(a)` whereas `np.power(a, 2)` showed to be considerably slower
- **Universal functions**
  - Ufunc performs and elementwise operation on all elements of an array.
  - http://wiki.cython.org/MarkLodato/CreatingUfuncs

- **chararray**
	- chararray: vectorized string operations
	- `.view()` has a second meaning: it can make an ndarray an instance of a specialized ndarray subclass
```python
x = np.array(['a', ' bbb', ' ccc']) # type: <type 'numpy.ndarray'>
y = x.view(np.chararray) # type: <class 'numpy.core.defchararray.chararray'>
y.lstrip(' ').upper()
```
- **maskedarray**
	- Masked arrays are arrays that may have missing or invalid entries
	- Not all NumPy functions respect masks, for instance np.dot , so check the return types.
	- The masked_array returns a view to the original array
```python
x = np.array([1, 2, 3, -99, 5])
mx = np.ma.masked_array(x, mask=[0, 0, 0, 1, 0]) # type: <class 'numpy.ma.core.MaskedArray'>
mx # masked_array(data = [1 2 3 -- 5],mask = [False False False True False],fill_value = 999999)
```

- **matrix**
	- `np.matrix`
	- always 2-D
	- * is the matrix product, not the elementwise one
```python
np.matrix([[1, 0], [0, 1]]) * np.matrix([[1, 2], [3, 4]]) # type: <class 'numpy.matrixlib.defmatrix.matrix'>
```
- **Summary**
	- Know how to create arrays : array , arange , ones , zeros .
	- Know the shape of the array with array.shape , then use slicing to obtain different views of the array: array[::2] , etc. Adjust the shape of the array using reshape or flatten it with ravel.
	- Obtain a subset of the elements of an array and/or modify their values with masks
	- Know miscellaneous operations on arrays, such as finding the mean or max ( array.max() , array.mean() ). No need to retain everything, but have the reflex to search in the documentation (online docs, help() , lookfor() )
	- master the indexing with arrays of integers, as well as broadcasting. Know more NumPy functions to handle various array operations
- numpy.lookfor looks for keywords inside the docstrings of specified module
- `numexpr` is designed to mitigate cache effects in array computing
```python
import numpy as np
np.pi
#
a=np.arange(0,11)
a.strides
#
# some functions
help()
str()
len()
```
- other functions
```python
import nummpy as np
from skimage import data, exposure, img_as_float
image = img_as_float(data.camera())
np.histogram(image,bins=2)
```
**Tutorials**
* https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-39.php

## Matplotlib
- 2D plotting package
- start with basic visualization of data arrary
- pyplot: provides a procedural interface to the matplotlib object-oriented plotting library
- **TBD**: Learn about `figure` and `subplot`
- Figures, Subplots, Axes and Ticks
```python
import numpy as np
import matplotlib.pyplot as plt

# 1D plotting
# line-plot
x=np.linspace(0,3,20)
y=np.linspace(0,9,20)
plt.plot(x,y)
plt.show()
plt.plot(x, y, 'o') # dot plot
#
# 2D arrays (such as images)
image = np.random.rand(30, 30)
plt.imshow(image, cmap=plt.cm.hot)
plt.colorbar()
plt.show()
#
import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
plt.plot(X, C)
plt.plot(X, S)
plt.show()
# commands
plt.plot
#
plt.figure
fig = plt.figure(figsize=(6, 6)) # figure size in inches
fig.subplots_adjust
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
#
plt.subplot
plt.xlim
plt.ylim
plt.xticks
plt.yticks
plt.set_xticklabels
plt.set_yticklabels
plt.gca() # gca stands for 'get current axis'
plt.legend
plt.annotate
plt.close
plt.show
plt.text
plt.title
#
plt.imshow
plt.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
plt.imshow(digits.images[i], cmap=plt.cm.gray, interpolation='nearest')
plt.imshow(digits.images[i], cmap="gray", interpolation='nearest')
#
plt.axes
plt.pie
plt.bar
plt.scatter
plt.quiver
plt.contour
plt.contourf
plt.pcolormesh
plt.scatter
# Automatically adjust subplot parameters to give specified padding
plt.tight_layout
#
# Create color maps
from matplotlib.colors import ListedColormap
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
```
* **Subplots**
	- https://matplotlib.org/gallery/subplots_axes_and_figures/subplots_demo.html
* **Legend**
	- https://matplotlib.org/2.0.2/users/legend_guide.html

### Examples
* https://stackoverflow.com/questions/34768717/matplotlib-unable-to-save-image-in-same-resolution-as-original-image

There are two factors at play here:

An Axes doesn't take up the entire Figure by default
In matplotlib, the Figure's size is fixed, and the contents are stretched/squeezed/interpolated to fit the figure. You want the Figure's size to be defined by its contents.
To do what you want to do, there are three steps:

Create a figure based on the size of the image and a set DPI
Add a subplot/axes that takes up the entire figure
Save the figure with the DPI you used to calculate figure's size
Let's use a random Hubble image from Nasa http://www.nasa.gov/sites/default/files/thumbnails/image/hubble_friday_12102015.jpg. It's a 1280x1216 pixel image.

Here's a heavily commented example to walk you through it:

```python
import matplotlib.pyplot as plt

# On-screen, things will be displayed at 80dpi regardless of what we set here
# This is effectively the dpi for the saved figure. We need to specify it,
# otherwise `savefig` will pick a default dpi based on your local configuration
dpi = 80

im_data = plt.imread('hubble_friday_12102015.jpg')
height, width, nbands = im_data.shape

# What size does the figure need to be in inches to fit the image?
figsize = width / float(dpi), height / float(dpi)

# Create a figure of the right size with one axes that takes up the full figure
fig = plt.figure(figsize=figsize)
ax = fig.add_axes([0, 0, 1, 1])

# Hide spines, ticks, etc.
ax.axis('off')

# Display the image.
ax.imshow(im_data, interpolation='nearest')

# Add something...
ax.annotate('Look at This!', xy=(590, 650), xytext=(500, 500),
            color='cyan', size=24, ha='right',
            arrowprops=dict(arrowstyle='fancy', fc='cyan', ec='none'))

# Ensure we're displaying with square pixels and the right extent.
# This is optional if you haven't called `plot` or anything else that might
# change the limits/aspect.  We don't need this step in this case.
ax.set(xlim=[0, width], ylim=[height, 0], aspect=1)

fig.savefig('test.jpg', dpi=dpi, transparent=True)
plt.show()
```

### mpl_toolkits - Basic 3D in Matplotlib
https://matplotlib.org/1.4.3/mpl_toolkits/index.html


## Scipy: High Level Scientific Computing

- `scipy` is the core package for scientific routines in Python
- The scipy package contains various toolboxes dedicated to common issues in scientific computing
- it is meant to operate efficiently on numpy arrays, so that numpy and scipy work hand in hand
- Scipy’s routines are optimized and tested, and should therefore be used when possible
- Its different submodules correspond to different applications, such as interpolation, integration, optimization, image processing, statistics, special functions, etc.
- scipy is composed of task-specific sub-modules, some are:-
	* scipy.cluster - Vector quantization / Kmeans
	* scipy.constants - Physical and mathematical constants
	* scipy.fftpack - Fast Fourier transforms
	* scipy.integrate - Numerical integration routines
	* scipy.interpolate - Interpolation
	* scipy.io - Data/File input and output
	* scipy.linalg - Linear algebra routines/operations
	* scipy.ndimage - Image manipulation: n-dimensional image package
	* scipy.odr - Orthogonal distance regression
	* scipy.optimize - Optimization and fit
	* scipy.signal - Signal processing
	* scipy.sparse - Sparse matrices
	* scipy.spatial - Spatial data structures and algorithms
	* scipy.special - Special functions/Any special mathematical functions
	* scipy.stats - Statistics and random numbers
```python
import numpy as np
from scipy import stats # same for other sub-modules
from scipy import io as spio
```

### Statistics and random numbers: `scipy.stats`
- `scipy.stats.ttest_1samp()` tests if the population mean of data is likely to be equal to a given value.
- It returns `T-statistic` and the `p-value`
```python
from scipy import stats
stats.ttest_1samp(data['VIQ'], 0)
```
- to To test if the difference of a mean between two groups for a particular variable is significant. Do a 2-sample t-test with `scipy.stats.ttest_ind()`
```python
from scipy import stats
stats.ttest_ind(viq_f,viq_m)
```

### Linear algebra operations: `scipy.linalg`

```python
scipy.linalg.det() # determinant of a square matrix
scipy.linalg.inv() # inverse of a square Matrix
#
# SVD - Singular Value Decomposition
a=np.arange(9).reshape((3,3))+np.diag([1,0,1])
u,s,v=linalg.svd(a)
## verify svd
aa=u.dot(np.diag(s)).dot(v)
np.allclose(a,aa)
```
- principal component analysis (PCA) or SVD: PCA is a technique for dimensionality reduction, i.e. an algorithm
to explain the observed variance in your data using less dimensions.
- independent component analysis (ICA): ICA is a source seperation technique, for example to unmix multiple signals that have been recorded through multiple sensors. Doing a PCA first and then an ICA can be useful if you have more sensors than signals.

### Interpolate: `scipy.interpolatescipy.interpolate`
- is useful for fitting a function from experimental data and thus evaluating points where no measure exists
- example: Maximum wind speed prediction at the Sprogø station for a more advanced spline interpolation
```python
scipy.interpolate.interp1d
scipy.interpolate.interp2d
```

### Optimization and fit: `scipy.optimize`
- Optimization is the problem of finding a numerical solution to a minimization or equality
- this package provides algorithms for function minimization (scalar or multi-dimensional), curve fitting and root finding.
- least squares curve fitting
- http://www.scipy-lectures.org/intro/scipy/auto_examples/plot_curve_fit.html
- If the function is a smooth function, gradient-descent based methods are good options. The `lBFGS` algorithm is a good choice in general
- A possible issue with this approach is that, if the function has local minima, the algorithm may find these local minima instead of the global minimum depending on the initial point x0
- If we don’t know the neighborhood of the global minimum to choose the initial point, we need to resort to 
costlier global optimization
- To find the global minimum, we use `scipy.optimize.basinhopping()` (added in version 0.12.0 of Scipy). It combines a local optimizer with sampling of starting points
```python
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

# Seed the random number generator for reproducibility
np.random.seed(0)

x_data = np.linspace(-5, 5, num=50)
y_data = 2.9 * np.sin(1.5 * x_data) + np.random.normal(size=50)

def test_func(x, a, b):
    return a * np.sin(b * x)

params, params_covariance = optimize.curve_fit(test_func, x_data, y_data, p0=[2, 2])
print(params)
#
# plot the resulting curve on the data
plt.figure(figsize=(6, 4))
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, test_func(x_data, params[0], params[1]), label='Fitted function')
plt.legend(loc='best')
plt.show()
#
optimize.minimize(f, x0=0)
optimize.minimize(f, x0=0, method="L-BFGS-B")
#
# global minimum
optimize.basinhopping(f, 0)
optimize.minimize(f, x0=1,bounds=((0, 10), ) )
```
- Minimizing functions of several variables: To minimize over several variables, the trick is to turn them into a function of a multi-dimensional variable (a vector)
- `optimize.minimize_scalar()` is a function with dedicated methods to minimize functions of only one variable
- Filters should be created using the scipy filter design code
- Exercise
```python
temp_max = np.array([17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18])
temp_min = np.array([-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58])
```
- Optimization of a two-parameter function
```python
import numpy as np
# Define the function that we are interested in
def sixhump(x):
	return ((4 - 2.1*x[0]**2 + x[0]**4 / 3.) * x[0]**2 + x[0] * x[1] + (-4 + 4*x[1]**2) * x[1] **2)

# Make a grid to evaluate the function (for plotting)
x = np.linspace(-2, 2)
y = np.linspace(-1, 1)
xg, yg = np.meshgrid(x, y)
#
# (AxisConcatenator) |  Translates slice objects to concatenation along the second axis.
help(np.c_)
#
np.dstack([xg.flat,yg.flat])
np.vstack
#
import matplotlib.pyplot as plt
plt.figure()
plt.imshow(sixhump([xg, yg]), extent=[-2, 2, -1, 1])
plt.colorbar()
#
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(xg, yg, sixhump([xg, yg]), rstride=1, cstride=1,
cmap=plt.cm.jet, linewidth=0, antialiased=False)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.set_title('Six-hump Camelback function')
#
from scipy import optimize
x_min = optimize.minimize(sixhump, x0=[0, 0])
plt.figure()
# Show the function in 2D
plt.imshow(sixhump([xg, yg]), extent=[-2, 2, -1, 1])
plt.colorbar()
# And the minimum that we've found:
plt.scatter(x_min.x[0], x_min.x[1])
plt.show()
#
# variety of filters
from scipy import ndimage
from scipy import signal
#
# fft - fast fourier transform
from scipy import fftpack
#
np.random.standard_normal
np.copy(face).astype(np.float)
```
- image blur by convolution with a Gaussian kernel
- Image denoising by FFT


## Mayavi: 3D plotting with Mayavi

- Example
```python
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')
plt.show()
```
* Image plane widgets
* Isosurfaces

## Other Libraries/Packages/Extensions/Modules

### Cython
- http://cython.org/
- https://en.wikipedia.org/wiki/Cython
- Cython is an optimising static compiler for both the Python programming language and the extended Cython programming language (based on Pyrex). It makes writing C extensions for Python as easy as Python itself
- Cython is a superset of the Python programming language, designed to give C-like performance with code that is mostly written in Python
- Cython is a compiled language that generates CPython extension modules. These extension modules can then be loaded and used by regular Python code using the import statement

### PIL
- https://en.wikipedia.org/wiki/Python_Imaging_Library
- PIL is the Python Imaging Library
- PIL is one of the core libraries for image manipulation in Python. Unfortunately, its development has stagnated, with its last release in 2009

### Pillow
- http://python-pillow.org/
- https://pillow.readthedocs.io/
- Actively-developed fork of PIL called Pillow - it’s easier to install, runs on all operating systems, and supports Python 3
```bash
# Installation
pip install Pillow
```

## Image Processing in Python
- image-processing.md

**Some Common tasks in image processing:**
1. Input/Output, displaying images
2. Basic manipulations:
	- Geometrical transformations: cropping, flipping, rotating, ...
	- Statistical information
3. Image filtering:
	- Blurring/smoothing
	- Sharpening
	- Denoising
	- Mathematical morphology
4. Image segmentation: labeling pixels corresponding to different objects
5. Classification
6. Feature extraction:
	- Edge detection
	- Segmentation
7. Measuring objects properties: ndimage.measurements
8. Registration

## Interfacing with C/C++
- A process commonly referred to wrapping.
- Cython is the most modern and advanced. In particular, the ability to optimize code incrementally by adding types to your Python code is unique.
- These four techniques are perhaps the most well known ones, of which Cython is probably the most advanced one and the one you should consider using first
	* Python-C-Api
	* Ctypes
	* SWIG
	* Cython

## Statistics in Python
* Standard scientific Python environment (numpy, scipy, matplotlib)
* Pandas
* [Statsmodels](http://statsmodels.sourceforge.net/stable/example_formulas.html)
* [Seaborn](http://seaborn.pydata.org)
	- Seaborn is a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics: `import seaborn as sns`

**Why Python for statistics?**
- When it comes to building complex analysis pipelines that mix statistics with e.g. image analysis, text mining, or control of a physical experiment, the richness of Python is an invaluable asset.

- multiple observations or samples described by a set of different attributes or features

## Pandas
* data-frame
	- We will store and manipulate this data in a pandas.DataFrame , from the pandas module. It is the Python equivalent of the spreadsheet table
	- It is different from a 2D numpy array as it has named columns, can contain a mixture of different data types by column, and has elaborate selection and pivotal mechanisms.

The installed version of numexpr 2.4.3 is not supported in pandas and will be not be used The minimum supported version is 2.4.6

```
sudo pip list | grep numexpr
sudo pip install -U numexpr
```
- **numexpr:** for accelerating certain numerical operations. numexpr uses multiple cores as well as smart chunking and caching to achieve large speedups. If installed, must be Version 2.1 or higher.
- numexpr (2.6.5), numpy (1.14.3)
```python
import pandas
data = pandas.read_csv('brain_size.csv',sep=';',na_values=".")
data.shape
data.columns
data['Gender']
data[data['Gender'] == 'Female']
data[data['Gender'] == 'Female']['VIQ'].mean()	
```
- pandas can input data from SQL, excel files, or other formats
- data is a pandas.DataFrame , that resembles R’s dataframe
- A pandas.DataFrame can also be seen as a dictionary of 1D ‘series’, eg arrays or lists.
- 3 numpy arrays can be exposed as a pandas.DataFrame
```python
pandas.DataFrame({'t': t, 'sin': sin_t, 'cos': cos_t})
```
- For a quick view on a large dataframe, use its describe method: `pandas.DataFrame.describe()`
- `groupby`: splitting a dataframe on values of categorical variables
- Other common grouping functions are **median**,**count** (useful for checking to see the amount of missing values in different subsets) or **sum**
- Groupby evaluation is lazy, no work is done until an aggregation function is applied.
```python
gGender = data.groupby('Gender')
for gender, value in gGender['VIQ']:
	print((gender, value.mean()))
gGender.mean()
#
gGender.boxplot()
```
- Pandas comes with some plotting tools ( `pandas.tools.plotting` , using `matplotlib` behind the scene) to display statistics of the data in dataframes

**Hypothesis testing**
- comparing two groups
- t-test: the simplest statistical tes
- 2 sample test
- “paired test”, or “repeated measures test”
- T-tests assume Gaussian errors.
- Wilcoxon signed-rank test - it that relaxes this Gaussian errors assumption
- non paired case is the **Mann–Whitney U test**: `scipy.stats.mannwhitneyu()`
- non parametric statistics to test the difference between a variable in two groups

## Statsmodel
**Given two set of observations, x and y, we want to test the hypothesis that y is a linear function of x**
- `y=mx+c+e`
```python
import numpy as np
m = -5
x = np.linspace(-5,5,20)
e = 4*np.random.normal(size=x.shape)
y = -5 + 3*x + e
data = pandas.DataFrame({'x':x,'y':y})
#
from statsmodels.formula.api import ols
model = ols("y ~ x", data).fit()
model.summary()
```
- Statsmodels uses a statistical terminology: the y variable in statsmodels is called ‘endogenous’ while the x variable is called exogenous.
- y (endogenous) is the value you are trying to predict
- x (exogenous) represents the features you are using to make the prediction
- http://statsmodels.sourceforge.net/devel/endog_exog.html
- non-float data type or categorical value, statsmodels is able to automatically infer this

**Categorical variables: comparing groups or multiple categories**
```python
model = ols("VIQ ~ Gender + 1", data).fit()
data = pandas.read_csv('brain_size.csv', sep=';', na_values=".")
#
# An integer column can be forced to be treated as categorical using
model = ols('VIQ ~ C(Gender)', data).fit()
#
# We can remove the intercept using - 1 in the formula, or force the use of an intercept using + 1
```
- By default, statsmodels treats a categorical variable with K possible values as K-1 ‘dummy’ boolean variables (the last level being absorbed into the intercept term). This is almost always a good default choice - however, it is possible to specify different encodings for categorical variables
- http://statsmodels.sourceforge.net/devel/contrasts.html
```python
import pandas
import
data_fisq = pandas.DataFrame({'iq': data['FSIQ'], 'type': 'fsiq'})
data_piq = pandas.DataFrame({'iq': data['PIQ'], 'type': 'piq'})
data_long = pandas.concat((data_fisq, data_piq))
#
from statsmodels.formula.api import ols
model = ols("iq ~ type", data_long).fit()
model.summary()
#
# t-test
stats.ttest_ind(data['FSIQ'], data['PIQ'])
```

**Multiple Regression: including multiple factors**
- Consider a linear model explaining a variable z (the dependent variable) with 2 variables x and y:
```python
z = x*c1 + y*c2 + i + e
```
- Such a model can be seen in 3D as fitting a plane to a cloud of (x, y, z) points.

## Seaborn
**More visualization: seaborn for statistical exploration**
- http://seaborn.pydata.org
- http://lib.stat.cmu.edu/datasets/CPS_85_Wages
- http://gael-varoquaux.info/stats_in_python_tutorial/auto_examples/plot_wage_data.html
- Seaborn changes the default of matplotlib figures to achieve a more “modern”, “excel-like” look. It does that upon import. You can reset the default using:
	```python
	from matplotlib import pyplot as plt
	plt.rcdefaults()
	```
	- `lmplot`: plotting a univariate regression
	```python
	import seaborn
	seaborn.lmplot(y='VIQ',x='Height',data=data)
	```
- http://seaborn.pydata.org/tutorial/aesthetics.html
- To compute a regression that is less sentive to outliers, one must use a robust model.
- Formulate a single model that tests for a variance of slope across the two populations. This is done via an “interaction”.
- http://www.statsmodels.org/devel/example_formulas.html#multiplicative-interactions

## [Sympy](http://www.sympy.org/en/index.html)
- Symbolic Mathematics in Python
- What is SymPy? SymPy is a Python library for symbolic mathematics
- It aims to become a full-featured computer algebra system (CAS) while keeping the code as simple as possible in order to be comprehensible and easily extensible. SymPy is written entirely in Python.
- SymPy defines three numerical types: Real , Rational and Integer
- SymPy uses mpmath in the background, which makes it possible to perform computations using arbitrary-precision arithmetic.
- That way, some special constants, like e, pi , oo (Infinity), are treated as symbols and can be evaluated with arbitrary precision
- mathematical infinity, called `oo`
```python
import sympy as sym
a = sym.Rational(1, 2)
sym.pi**2
sym.pi.evalf()
(sym.pi + sym.exp(1)).evalf()
#
# mathematical infinity
sym.oo > 99999
```

## Key Learnings in Stats
* Hypothesis testing and p-values give you the significance of an effect / difference.
* Formulas (with categorical variables) enable you to express rich links in your data.
* Visualizing your data and fitting simple models give insight into the data.
* Conditionning (adding factors that can explain all or part of the variation) is an important modeling aspect that changes the interpretation.

## [Scikit-image: image processing](http://scikit-image.org/)
- scikit-image is a Python package dedicated to image processing, and using natively NumPy arrays as image objects

### References
- http://pymc-devs.github.io/pymc/
- http://greenteapress.com/thinkstats2/thinkstats2.pdf

## Online Practice Tools
- https://www.dataquest.io

## Contribution to documentation
- Refer: Pg 310

## References

1. List Comprehensions
  - https://www.analyticsvidhya.com/blog/2016/01/python-tutorial-list-comprehension-examples/
  - https://stackoverflow.com/questions/30245397/why-is-list-comprehension-so-faster/30245489
2. Profiling and Timing Code
	- https://jakevdp.github.io/PythonDataScienceHandbook/01.07-timing-and-profiling.html

http://josephcslater.github.io/scipy-numpy-matplotlib-pylab.html

## TBD List
- Pg 72: for now skipping to next chaptrer - matplotlib
- Pg 313: debugging code

## Python IDEs and Editors
- https://www.techradar.com/news/best-ide-for-python
- http://ubuntuhandbook.org/index.php/2018/03/pycharm-2018-1-released/
- https://cewing.github.io/training.codefellows/assignments/day01/sublime_as_ide.html
- https://wiki.python.org/moin/PythonEditors

**Pyzo**
http://www.pyzo.org/install_linux.html#install-linux
```bash
sudo python3 -m pip install pyzo
```

## Python - Building Interactive GUI
**Tool Suite**
* Enthought Tool Suite
	- The Enthought Tool Suite enable the construction of sophisticated application frameworks for data analysis, 2D plotting and 3D visualization

The main packages of the Enthought Tool Suite are:
* Traits
	- component based approach to build our application
* Kiva
	- 2D primitives supporting path based rendering, affine transforms, alpha blending and more.
* Enable
	- object based 2D drawing canvas.
* Chaco
  - plotting toolkit for building complex interactive 2D plots.
* Mayavi
	- 3D visualization of scientific data based on VTK.
* Envisage
	- application plugin framework for building scriptable and extensible applications

- wxPython, PyQt or PySide
- Numpy and Scipy

## Mayavi - 3D plotting
- `Mayavi` is an interactive 3D plotting package.
- `matplotlib` can also do simple 3D plotting, but Mayavi relies on a more powerful engine ( VTK ) and is more suited to displaying large or complex data

**Mlab: the scripting interface**
- `mayavi.mlab` module provides simple plotting functions to apply to numpy arrays, similar to matplotlib

## `sklearn` ML python package
* scikit-learn: machine learning in Python
* [Refer here: sklearn: Machine Learning in Python](https://github.com/mangalbhaskar/technotes/blob/master/machine-learning.md)

**Documentation**
* http://scikit-learn.org

**Tutorials**
* https://www.youtube.com/watch?v=r4bRUvvlaBw
* https://github.com/jakevdp/sklearn_tutorial
* https://github.com/ujjwalkarn/DataSciencePython

## Description on Different Python Packages
* **imutils (0.4.6)**
A series of convenience functions to make basic image processing functions such as translation, rotation, resizing, skeletonization, displaying Matplotlib images, sorting contours, detecting edges, and much more easier with OpenCV and both Python 2.7 and Python 3.


## Gif, Videos in Python
* https://www.idiotinside.com/2017/06/06/create-gif-animation-with-python/
```bash
sudo pip install imageio MoviePy
```

* http://free-tutorials.org/two-python-modules-moviepy-and-images2gif-part-001/
```
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
canvas = FigureCanvas(fig)
```

## Different Python Environments
* [Anaconda](https://anaconda.org/)
  - Anaconda is the most widely used Python distribution for data science and comes pre-loaded with all the most popular libraries and tools
  - https://docs.anaconda.com/anaconda/packages/pkg-docs

## [iPython](https://ipython.org/)
- iPython: Interactive Python

**ipython-jupyter**
- https://www.datacamp.com/community/blog/ipython-jupyter

## [Jupyter](https://jupyter.org/)
* The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.
* The Jupyter project is the successor to the earlier **IPython Notebook**, which was first published as a prototype in 2010. 

**[Getting Started](http://jupyter.readthedocs.io/en/latest/content-quickstart.html)**
* http://jupyter.readthedocs.io/en/latest/content-quickstart.html
* https://www.dataquest.io/blog/jupyter-notebook-tutorial/
- The Jupyter Notebook is an incredibly powerful tool for interactively developing and presenting data science projects.
- A notebook integrates code and its output into a single document that combines visualisations, narrative text, mathematical equations, and other rich media.

* **[important terminology](http://jupyter.readthedocs.io/en/latest/glossary.html#term-kernel)**
- A kernel provides programming language support in Jupyter. IPython is the default kernel. Additional kernels include R, Julia, and many more.

* **installing Jupyter and creating notebook**
```bash
sudo pip install jupyter
sudo pip3 install jupyter
```

* **[Configurations](http://jupyter.readthedocs.io/en/latest/projects/jupyter-directories.html)**
- Config files are stored by default in the `~/.jupyter` directory.
- To list the config directories currrently being used:
```bash
jupyter --paths
```
- Jupyter uses a search path to find installable data files

* **how to run and save notebooks**
```bash
# the current working directory will be the start-up directory
jupyter notebook
sudo jupyter notebook --allow-root
python /usr/local/bin/IPython
sudo python -m pip install -U --force-reinstall pip
```

- The first line of /usr/local/bin/ipython is "#!/usr/bin/python3" I could edit that line to use python instead of python3 or it was as simple as run with:
* **share and publishe notebooks online**

**How to run an .ipynb Jupyter Notebook from terminal?**
An IPYNB file is a notebook document used by Jupyter Notebook, an interactive computational environment designed to help scientists work with the Python language 
`.ipynb`
```bash
ipython nbconvert --to python <YourNotebook>.ipynb
#
# From the command line you can convert a notebook to python with this command:
ipython nbconvert --to python <YourNotebook>.ipynb
#
# You may have to install the python mistune package:
#
sudo pip install mistune
```
* **How do I convert a IPython Notebook into a Python file via commandline?**
  - https://stackoverflow.com/questions/17077494/how-do-i-convert-a-ipython-notebook-into-a-python-file-via-commandline#19779226
  ```bash
  jupyter-nbconvert --to script demo.ipynb
  ```
* Convert Python files to IPython Notebook Files: `.py` to `'.ipyb`
  - https://www.webucator.com/blog/2015/07/bulk-convert-python-files-to-ipython-notebook-files-py-to-ipynb-conversion/


## Caffe, TensorFlow, Keras for Python2 and Python3

* some Issues:
```bash
usr/lib/python3.6/importlib/_bootstrap.py:219: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility. Expected 96, got 88
  return f(*args, **kwds)
```

## Images
- https://matplotlib.org/gallery/images_contours_and_fields/image_clip_path.html#sphx-glr-gallery-images-contours-and-fields-image-clip-path-py

1. Reading Images in python - Input/output, data types and colorspaces
* skimage
- `skimage.data_dir` = `/usr/local/lib/python2.7/dist-packages/skimage/data`
- imsave also uses an external plugin such as PIL
```python
from skimage import io
import os
filename = os.path.join(skimage.data_dir, 'camera.png')
# reading image files
camera = io.imread(filename)
logo = io.imread('http://scikit-image.org/_static/img/logo.png')
io.imsave('local_logo.png', logo)
```
* matplotlib
```python
import matplotlib.pyplot as plt
plt.imread('MarshOrchid.jpg')
plt.imshow()
plt.show()
```
* cv2 (openCV)
* pillow, PIL

## Misc Topics, Keywords etc
* `__import__`
* `getattr`

## OOP in Python
> Object Oriented Programming in Python

* Classes and objects in Python
* `self` and `__init__`
  - https://www.programiz.com/article/python-self-why
  * The use of self makes it easier to distinguish between instance attributes (and methods) from local variables.
  * `self` is not yet a keyword in Python, like this in C++ and Java
  * `__init__` is not a constructor but `__init__` gets called when we create an object
  * Technically speaking, constructor is a method which creates the object itself. In Python, this method is `__new__`
  * __new__() is always called before __init__()
  * Generally, __init__() is used to initialize a newly created object while __new__() is used to control the way an object is created.
  * One practical use of __new__() however, could be to restrict the number of objects created from a class.
* Function Decorators
  - https://www.programiz.com/python-programming/decorator

## Snippets
* Listing Files in a directory
```python
# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
import glob
print(glob.glob("/home/adam/*.txt"))
```

## Encoding, Decoding
- https://stackoverflow.com/questions/15092437/python-encoding-utf-8

## PyYAML
* https://stackoverflow.com/questions/20352794/pyyaml-is-producing-undesired-python-unicode-output
```bash
## write
configFileName = "paths.yml"
#
with open(configFileName, 'w') as f:
  yaml.safe_dump(cfg, f, default_flow_style=False)
#
## read
with open(configFileName, 'r') as f:
  cfg = yaml.load(f)
```


## Flask
* https://stackoverflow.com/questions/33241050/trailing-slash-triggers-404-in-flask-path-rule
* https://stackoverflow.com/questions/10434599/how-to-get-data-received-in-flask-request


## Top Python Projects in 2018
* https://hackernoon.com/50-popular-python-open-source-projects-on-github-in-2018-c750f9bf56a0


## Assertions (assert) in Python
* https://dbader.org/blog/python-assert-tutorial
* https://www.journaldev.com/15791/python-assert

## Snipets
```python
np.arange(3, 6) # array([3, 4, 5])
2**np.arange(3, 6) # array([ 8, 16, 32])
```

## Annoy
* https://github.com/spotify/annoy
* Annoy (Approximate Nearest Neighbors Oh Yeah) is a C++ library with Python bindings to search for points in space that are close to a given query point. It also creates large read-only file-based data structures that are mmapped into memory so that many processes may share the same data.

## urllib, urlparse
* https://stackoverflow.com/questions/29358403/no-module-named-urllib-parse-how-should-i-install-it#37526119
  ```python
  * try:
      from urllib.parse import urlparse
      from urllib.parse import urljoin
  except ImportError:
      from urlparse import urljoin
      from urlparse import urlparse
   ```

## Python based web servers

* SimpleHTTPServer
* gunicorn
* tornado

### gunicorn
* https://cloud.google.com/appengine/docs/flexible/python/runtime
* Recommended Gunicorn configuration
* Most applications, however, will need to further configure the WSGI server. Instead of specifying all of the settings on the entrypoint, create a gunicorn.conf.py file in your project root directory, where your app.yaml is located, and specify it in your entrypoint:
```bash
gunicorn -c gunicorn.conf.py -b :$PORT
```
* http://docs.gunicorn.org/en/19.3/settings.html
* http://docs.gunicorn.org/en/stable/run.html



## Asynchronous, non-blocking network I/O; Streaming; Websocket
**Tornado**
- https://www.tornadoweb.org/en/stable/
- Tornado is different from most Python web frameworks. It is not based on WSGI, and it is typically run with only one thread per process.


**streamlit-demo**
https://github.com/treuille/insight-streamlit-demo
https://github.com/fivethirtyeight/uber-tlc-foil-response/tree/master/uber-trip-data
http://streamlit.io/docs/tutorial/
http://streamlit.io/docs/
```bash
vi $HOME/.streamlit/config.yaml
```
```bash
client:
  remotelyTrackUsage: false
proxy:
  useNode: false
  waitForConnectionSecs: 30
```
* create file: `st_hello.py`
```bash
import streamlit as st
st.write('Hello, world')
```
* run the app
```bash
python st_hello.py
#
## it starts at
# http://localhost:8501/?name=st_hello
```

### **Asynchronous**
* How to create an asynchronous streaming websocket with Autobahn?
* https://stackoverflow.com/questions/21653519/python-server-for-streaming-request-body-content
* https://stackoverflow.com/questions/4962808/asynchronous-http-calls-in-python
* https://stackoverflow.com/questions/10555292/ideal-method-for-sending-multiple-http-requests-over-python

* **grequests**
  - https://stackoverflow.com/questions/9110593/asynchronous-requests-with-python-requests
  - https://github.com/kennethreitz/grequests
  - GRequests allows you to use Requests with Gevent to make asynchronous HTTP Requests easily.
  - **Note:** You should probably use requests-futures instead.
* **Twisted**
  - https://github.com/twisted/twisted
  - Twisted is an event-driven networking engine written in Python and licensed under the open source ​MIT license. Twisted runs on Python 2 and an ever growing subset also works with Python 3.
  - https://twistedmatrix.com/trac/
  - Twisted does not rely on threads for doing multiple things at once. Rather, it takes a cooperative multitasking approach---your main script starts the reactor and the reactor calls functions that you set up. Your functions must return control to the reactor before the reactor can continue working.
  - `sudo pip install twisted`
  - https://stackoverflow.com/questions/14712752/using-inlinecallbacks
  - https://twistedmatrix.com/documents/current/api/twisted.internet.defer.html
  - https://hackedbellini.org/development/writing-asynchronous-python-code-with-twisted-using-inlinecallbacks/
* **requests-futures**
  - https://github.com/ross/requests-futures
* **txrequests**
  - https://pypi.org/project/txrequests/
  - https://github.com/tardyp/txrequests
  - `sudo pip install txrequests`
  - https://programtalk.com/python-examples/txrequests.Session/
* **concurrent futures**
  - https://docs.python.org/dev/library/concurrent.futures.html
* **autobahn**
  * https://github.com/crossbario/autobahn-python
Autobahn|Python is a subproject of Autobahn and provides open-source implementations of

The WebSocket Protocol
The Web Application Messaging Protocol (WAMP)
for Python 2 and 3, and running on Twisted and asyncio.

You can use Autobahn|Python to create clients and servers in Python speaking just plain WebSocket or WAMP.
WebSocket allows bidirectional real-time messaging on the Web and beyond, while WAMP adds real-time application communication on top of WebSocket.
WAMP provides asynchronous Remote Procedure Calls and Publish & Subscribe for applications in one protocol running over WebSocket. WAMP is a routed protocol, so you need a WAMP Router to connect your Autobahn|Python based clients. We provide Crossbar.io, but there are other options as well.

* https://wamp-proto.org/implementations/index.html#routers
* https://crossbar.io/

## WAMP - Web Application Messaging Protocol
* https://wamp-proto.org/
- WAMP is an open standard WebSocket subprotocol that provides two application messaging patterns in one unified protocol: Remote Procedure Calls + Publish & Subscribe.
- Using WAMP you can build distributed systems out of application components which are loosely coupled and communicate in (soft) real-time.


## Websockets
* https://www.html5rocks.com/en/tutorials/websockets/basics/
1. The Problem: Low Latency Client-Server and Server-Client Connections

Latency is a time interval between the stimulation and response, or, from a more general point of view, a time delay between the cause and the effect of some physical change in the system being observed.

2005 - AJAX

Push, Comet, Flash, XHR Multipart, [htmlfiles](http://cometdaily.com/2007/10/25/http-streaming-and-internet-explorer/) - html streaming
 Long Pooling, 

WebSocket: Bringing Sockets to the Web
http://dev.w3.org/html5/websockets/

The WebSocket specification defines an API establishing "socket" connections between a web browser and a server. In plain words: There is an persistent connection between the client and the server and both parties can start sending data at any time.



## HTTP2
* https://hyper.readthedocs.io/en/latest/


## Web utilities
* https://httpbin.org/
  - A simple HTTP Request & Response Service.

## Adoption of Python as Main Line System Language - Challanges & Solutions
* https://bytes.com/topic/python/answers/841071-eggs-virtualenv-apt-best-practices

I have basically recommended that we only install the python base (core language) from apt, and that everything else should be installed into virtual environments. But I wanted to check to see how other enterprises are handling this issue? Are you building python from scratch, or using
specific sets of .deb packages, or some other process. Suggestions on build/rollout tools (like zc.buildout, Paver, etc) would also be appreciated.

Any insight into the best way to have a consistent, repeatable, controllable development and production environment would be much appreciated.

* This is the exact way we are deploying our software. You can even use the virtualenv --no-site-packages option to completely isolate the VE from the underlying system site-packages.
* I would recommend that all you install into the system python is virtualenv, and maybe some uncritical C-modules such as psycopg2.
* Currently there is much going on regarding setuptools. A fork, "Distribute" has been announced, and "pyinstall" by Ian Bicking, an easy_install replacement that deals with some of it's ancestors shortcomings.

## Virtual Environment, Isolated Python Environment
* https://tech.instacart.com/freezing-pythons-dependency-hell-in-2018-f1076d625241
* https://www.bluetin.io/isolated-python-environment-guide/
* https://www.sitepoint.com/virtual-environments-python-made-easy/
* https://docs.python-guide.org/dev/virtualenvs/
* https://medium.freecodecamp.org/manage-multiple-python-versions-and-virtual-environments-venv-pyenv-pyvenv-a29fb00c296f

* Every Python project sharing the same dependencies
* Isolate projects with its own specific dependencies
* [python-virtual-environments-a-primer](https://realpython.com/python-virtual-environments-a-primer/)

**How & Where python packages are stored? When Virtual Environment is required?**
* There are a few different locations where these packages can be installed on system
* most system packages are stored in a child directory of the path stored in `sys.prefix`
```python
import sys
sys.prefix
#
#'/usr'
```
* third party packages installed using [easy_install](https://pythonhosted.org/setuptools/easy_install.html) or [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)) are typically placed in one of the directories pointed to by site.getsitepackages:
```python
import site
site.getsitepackages()
## ['/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages']
```
* by default, every project on your system will use these same directories to store and retrieve site packages (third party libraries)
* At first glance, this may not seem like a big deal, and it isn’t really, for system packages (packages that are part of the standard Python library), but it does matter for site packages.
* This is a real problem for Python since it can’t differentiate between versions in the site-packages directory. So both v1.0.0 and v2.0.0 would reside in the same directory with the same name
* This is where virtual environments and the virtualenv/venv tools come into play
* Virtual environments: isolated independent environments that can have both a specific version of Python and of any project-specific packages installed within them, without affecting any other projects.
* There are no limits to the number of environments you can have since they’re just directories containing a few scripts. Plus, they’re easily created using the virtualenv or pyenv command line tools



**Tools: Setting up and using a virtual environment for Python projects**
* venv / pyvenv
* pyenv
* pyenv-virtualenv
* virtualenv

**What is the difference between venv, pyvenv, pyenv, virtualenv, virtualenvwrapper, pipenv, etc?**
* https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe
* **Recommendation for beginners:**
  - This is my personal recommendation for beginners: start by learning virtualenv and pip, tools which work with both Python 2 and 3 and in a variety of situations, and pick up the other tools once you start needing them.

**Managing Virtual Environments**
* While virtual environments certainly solve some big problems with package management, they’re not perfect. After creating a few environments, you’ll start to see that they create some problems of their own, most of which revolve around managing the environments themselves. 
* To help with this, the virtualenvwrapper tool was created. It’s just some wrapper scripts around the main virtualenv tool.
* A few of the more useful features of virtualenvwrapper are that it:
  * Organizes all of your virtual environments in one location
  * Provides methods to help you easily create, delete, and copy environments
  * Provides a single command to switch between environments
```bash
pip install virtualenvwrapper
```


* After a while, though, you might end up with a lot of virtual environments littered across your system, and its possible you’ll forget their names or where they were placed.

* In addition, there is nuance around whether or not you should freeze all packages to patch versions.
* The hope is that if you don’t freeze any versions, you get free upgrades from all those upstream library developers. In reality what you’ll notice are the bugs and breaking changes that randomly get introduced into your continuous integration pipeline, or that the next developer to checkout your project needs to spend 30 minutes figuring out the dependency versions that work, rather than what the most recent versions are. It’s difficult to track down the source of these breakages, because they’re not in your own code and the changes were not tracked or intentional. The same logic applies to patch version changes in Python itself.

### Python Setup Configurations

**Update-alternatives**
* **Use update alternative for multiple python2 version or python3 version**
  * https://askubuntu.com/questions/609623/enforce-a-shell-script-to-execute-a-specific-python-version

**version checks**
* https://stackoverflow.com/questions/6141581/detect-python-version-in-shell-script


### virtualenv
* https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv
* virtualenv is a tool to create isolated Python environments. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.
```bash
pip install virtualenv
virtualenv --version
cd my_project_folder
virtualenv my_project
## alternatively
virtualenv --no-site-packages name-of-environment
virtualenv -p /usr/bin/python2.7 my_project
## export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2.7
source my_project/bin/activate
## From now on, any package that you install using pip will be placed in the my_project folder, isolated from the global Python installation
## Install packages as usual
deactivate
## To delete a virtual environment, just delete its folder. (
```
* After a while, though, you might end up with a lot of virtual environments littered across your system, and its possible you’ll forget their names or where they were placed.
* Running virtualenv with the option `--no-site-packages` will not include the packages that are installed globally. This can be useful for keeping the package list clean in case it needs to be accessed later. [This is the default behavior for virtualenv 1.7 and later.]
* “freeze” the current state of the environment packages. This will create a requirements.txt file, which contains a simple list of all the packages in the current environment, and their respective versions.
```bash
pip freeze > requirements.txt
#
## Later it will be easier for a different developer (or you, if you need to re-create the environment) to install the same packages using the same versions:
pip install -r requirements.txt
```
* Version Control Ignores - exclude the virtual environment folder from source control by adding it to the ignore list
  * https://docs.python-guide.org/writing/gotchas/#version-control-ignores
  ```bash
  ## Disabling Bytecode (.pyc) Files
  export PYTHONDONTWRITEBYTECODE=1
  #
  ## Removing Bytecode (.pyc) Files
  find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete
  ```
  * `.gitignore`
  ```bash
  *.py[cod]     # Will match .pyc, .pyo and .pyd files.
  __pycache__/  # Exclude the whole folder
  ```


### virtualenvwrapper
* https://virtualenvwrapper.readthedocs.io/en/latest/index.html
* `virtualenvwrapper` provides a set of commands which makes working with virtual environments much more pleasant. It also places all your virtual environments in one place.
* Organizes all of your virtual environments in one place.
* Wrappers for managing your virtual environments (create, delete, copy).
* Use a single command to switch between environments.
* Tab completion for commands that take a virtual environment as argument.
* User-configurable hooks for all operations (see Per-User Customization).
* Plugin system for more creating sharable ext
* Installation: To install (**make sure virtualenv is already installed!**):
* https://virtualenvwrapper.readthedocs.io/en/latest/install.html
  - virtualenvwrapper should be installed into the same global site-packages area where virtualenv is installed.
  - An alternative to installing it into the global site-packages is to add it to your user local directory (usually `~/.local`).
  ```bash
  sudo pip install virtualenv
  sudo pip install virtualenvwrapper
  mkdir $HOME/.virtualenvs
  ##
  export WORKON_HOME=$HOME/.virtualenvs
  # export PROJECT_HOME=$HOME/Devel
  source /usr/local/bin/virtualenvwrapper.sh
  ```
* Usage
```bash
## creates the my_project folder inside ~/.virtualenvs
mkvirtualenv my_project
## workon also deactivates whatever environment you are currently in, so you can quickly switch between environments.
workon my_project
#
deactivate
rmvirtualenv my_project
```
* other commands:
```bash
## List all of the environments.
lsvirtualenv
#
## Navigate into the directory of the currently activated virtual environment, so you can browse its site-packages, for example.
cdvirtualenv
#
## Like the above, but directly into site-packages directory.
cdsitepackages
#
## Shows contents of site-packages directory.
lssitepackages
```
* **Activating-the-virtualenv-of-two-different-version-of-python**
  * https://stackoverflow.com/questions/45809731/activating-the-virtualenv-of-two-different-version-of-python
* **Run programs from one virtual environment while another one is active**
* **How can we run 3 different python applications on 3 different python versions on same machine?** - best illustration: virtualenv, virtualenvwrapper, supervisor
  * http://rafiqnayan.blogspot.com/2018/03/deploy-python-application-with-gunicorn.html
  ```bash
  sudo apt install supervisor
  ```
  * This will actually install two softwares - supervisord and supervisorctl. supervisord is the daemon process that'll monitor and run the gunicorn processes. supervisorctl is the controller interface to interact with supervisord e.g. start, stop, restart.
  * We've to write a configuration file for supervisord. The file will contain which applications we want to run and how to run them.
  ```text

  For our 3 applications, our configuration file may look like the following:

  [supervisord]
  logfile = $HOME/supervisor/log/supervisord.log

  [program:analytics-app]
  environment=ANALYTICS_APP_CONFIG=$HOME/app_config/analytics_app.cfg
  directory=/var/www/apps/analytics-app
  command=/var/www/apps/analytics-app/venv/bin/gunicorn --bind 0.0.0.0:8001 wsgi:app

  [program:android-api-app]
  directory=/var/www/apps/android-api-app
  command=/var/www/apps/android-api-app/venv/bin/gunicorn --bind 0.0.0.0:8002 wsgi:app

  [program:auth-api-app]
  directory=/var/www/apps/auth-api-app
  command=/var/www/apps/auth-api-app/venv/bin/gunicorn --bind 0.0.0.0:8003 wsgi:app

  [unix_http_server]
  file = $HOME/supervisor/supervisor.sock
  chmod = 0777
  username = blah
  password = 123456

  [supervisorctl]
  serverurl = unix://$HOME/supervisor/supervisor.sock
  username = blah
  password = 123456

  [rpcinterface:supervisor]
  supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface
  ```
* pygpu installation
  - http://deeplearning.net/software/libgpuarray/installation.html#step-by-step-install
  - https://github.com/roebius/deeplearning_keras2/issues/3
  - https://github.com/openwrt/packages/issues/616
  - http://queirozf.com/entries/setup-keras-theano-backend-and-gpu-on-ubuntu-16-04
  - https://www.robberphex.com/2016/05/521
  - https://theano.readthedocs.io/en/master/install_ubuntu.html

  python setup.py build_ext -L $MY_PREFIX/lib -I $MY_PREFIX/include
* **Process Managers**
  * [supervisord](http://supervisord.org/introduction.html)
    - Supervisor is a client/server system that allows its users to control a number of processes on UNIX-like operating systems
  * [circus](https://github.com/circus-tent/circus)
    - Circus is a program that runs and watches processes and sockets. Circus can be used as a library or through the command line
    - https://circus.readthedocs.io/en/latest/
  - https://stackoverflow.com/questions/32290292/is-there-a-supervisor-for-python-3
  - https://stackoverflow.com/questions/19796883/supervisord-for-python-3

### Installing Packages
* Do you want to install OpenCV only in virtualenv or just make OpenCV work in virtualenv? 
  - https://stackoverflow.com/questions/31389655/install-opencv-into-a-virtual-environment
  - https://stackoverflow.com/questions/13312139/opencv-and-python-virtualenv/19213369#19213369
  - copying the shared objects produced from the opencv installation to my virtual environment, seemed to do the trick

**install OpenCV only in virtualenv**
* https://www.pyimagesearch.com/2015/06/15/install-opencv-3-0-and-python-2-7-on-osx/
* provide virtual env path to `cmake` or set it in `ccmake` before compiling and installing

**just make OpenCV work in virtualen**: best way
* compile and install python bindings systemwide and them copy to respective virtualenv
* https://stackoverflow.com/questions/37188623/ubuntu-how-to-install-opencv-for-python3
```bash
cp /usr/local/lib/python2.7/dist-packages/cv2.so <pathToVirtualEnv>/lib/python2.7/site-packages
cp /usr/local/lib/python3.6/dist-packages/cv2.cpython-36m-x86_64-linux-gnu.so  <pathToVirtualEnv>/lib/python3.6/site-packages
```


### Best Practices
* Don’t rely on humans to follow best practices. Write code to do it for them.
* Use a fresh `virtualenv` for each project
* `pip freeze > requirements.txt` on every change
* Specify your exact Python version in `runtime.txt`
* Project code should be organized in a Python module

## Packaging, Distribution
* https://packaging.python.org/glossary/#term-source-distribution-or-sdist
* http://sunnybala.com/2018/09/10/python-etch-a-sketch.html

**What is a Python egg?**
* https://stackoverflow.com/questions/2051192/what-is-a-python-egg
* Egg packaging has been superseded by Wheel packaging
* Same concept as a .jar file in Java, it is a .zip file with some metadata files renamed .egg, for distributing code as bundles.
* http://svn.python.org/projects/sandbox/trunk/setuptools/doc/formats.txt
```bash
A "Python egg" is a logical structure embodying the release of a specific version of a Python project, comprising its code, resources, and metadata. There are multiple formats that can be used to physically encode a Python egg, and others can be developed. However, a key principle of Python eggs is that they should be discoverable and importable. That is, it should be possible for a Python application to easily and efficiently find out what eggs are present on a system, and to ensure that the desired eggs' contents are importable.

The .egg format is well-suited to distribution and the easy uninstallation or upgrades of code, since the project is essentially self-contained within a single directory or file, unmingled with any other projects' code or resources. It also makes it possible to have multiple versions of a project simultaneously installed, such that individual programs can select the versions they wish to use.
```
* Wheel and Egg are both packaging formats that aim to support the use case of needing an install artifact that doesn’t require building or compilation, which can be costly in testing and production workflows.
* The Egg format was introduced by setuptools in 2004, whereas the Wheel format was introduced by PEP 427 in 2012.
* Wheel is currently considered the standard for built and binary packaging for Python.


**Wheel V/s Egg**
* https://packaging.python.org/discussions/wheel-vs-egg/

### Running Python's PDB debugger with Docker, Flask and Gunicorn
* https://www.fullstackpython.com/blog/python-3-flask-gunicorn-ubuntu-1804-bionic-beaver.html
* https://blog.lucasferreira.org/howto/2017/06/03/running-pdb-with-docker-and-gunicorn.html
* https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-using-the-convenience-script

## Lore
* https://github.com/instacart/lore
  - Lore is a python framework to make machine learning approachable for Engineers and maintainable for Data Scientists.


## Python Guides
* https://docs.python-guide.org/


**Python in GIS**
* http://toblerity.org/shapely/
  * pip install shapely
* http://toblerity.org/fiona/
  * loading gis data
**Resources**
* https://sites.google.com/site/yorkyuhuang/home/tutorial - very interesting k-bank slides
* http://www.akshaysoam.com/#/projects
