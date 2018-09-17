---
Title: GIS Maping Stack
Decription: GIS Maping Stack
Author: Bhaskar Mangal
Date: 
Tags: GIS Maping Stack
---

**Table of Contents**
* TOC
{:toc}


## GIS Maping Stack

## [Mapnik^1^](http://wiki.openstreetmap.org/wiki/Mapnik)
- Mapnik is an open source toolkit for rendering maps. Among other things, it is used to render the five main Slippy Map layers on the OpenStreetMap website. It supports a variety of geospatial data formats and provides flexible styling options for designing many different kinds of maps.
- [Mapnik^2^](https://github.com/mapnik/mapnik/wiki/About-Mapnik) is a Free Toolkit for developing mapping applications. It is written in modern C++ and has Python bindings that support fast-paced agile development. It can comfortably be used for both desktop map design and web development. Mapnik is about making beautiful maps. It uses the AGG graphics library, which offers world-class anti-aliasing rendering with subpixel accuracy for geographic data.


### Mapnik Styles
There are a number of external tools that can assist in the creation of Mapnik styles. They offer styling languages that are more compact and easier to read and write than Mapnik's built-in XML language.

* Cascadenik
* Spreadnik
* TileMill
* Kosmtik
* Quantumnik QGIS plugin - for creating Mapnik styles using a more graphical interface.

### Data Sources
Mapnik can use data from different sources: it can directly process
- OSM data
- PostGIS databases
- shapefiles and more

PostGIS is the most common approach for rendering OSM data with Mapnik. OSM can be loaded by a tool such as:
- Osmosis
- osm2pgsql
- Imposm

It can be accessed via SQL queries and GIS functions defined in a Mapnik style. This approach can be used for more advanced renderings, and is the main datasource used by the Standard OpenStreetMap layer.

## [TileMill](http://wiki.openstreetmap.org/wiki/TileMill)
- TileMill is a design environment developed by MapBox for cartography, constituting Mapnik as a renderer, CartoCSS as a stylesheet language, and a locally-served web interface with node.js as a server and based on Backbone.js for the client.Jan 9, 2017
TileMill - OpenStreetMap Wiki


## Installation

### Ubuntu Installation
If you are intending to install Tilemill from a package/ppa, do not follow the directions below in order to avoid package conflicts. Instead, directly proceed to install Tilemill. Mapnik will automatically be installed with your Tilemill installation because it is available in the TileMill PPA.
* https://github.com/mapnik/mapnik/wiki/UbuntuInstallation
* https://tilemill-project.github.io/tilemill/docs/linux-install/
* https://ircama.github.io/osm-carto-tutorials/tilemill-ubuntu/
* https://askubuntu.com/questions/900097/when-sudo-apt-get-install-npm-nodejs-legacy

```bash
lsb_release -a

LSB Version:	core-9.20160110ubuntu0.2-amd64:core-9.20160110ubuntu0.2-noarch:security-9.20160110ubuntu0.2-amd64:security-9.20160110ubuntu0.2-noarch
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.1 LTS
Release:	16.04
Codename:	xenial
```

```
sudo apt-get install -y libgtk2.0-dev libwebkit-dev libwebkitgtk-dev
```

Err:34 http://ppa.launchpad.net/bzindovic/suitesparse-bugfix-1319687/ubuntu xenial/main amd64 Packages
  404  Not Found

Err:41 http://ppa.launchpad.net/grass/grass-stable/ubuntu xenial/main amd64 Packages
  404  Not Found

## Tile Server Ubuntu
* https://ircama.github.io/osm-carto-tutorials/tile-server-ubuntu/
* https://ircama.github.io/osm-carto-tutorials/osm-rendering-process/
* https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/
* https://blog.mapbox.com/using-tilemills-raster-colorizer-e7600fd42dd9
* https://www.e-education.psu.edu/geog585/node/711
* https://gist.github.com/springmeyer/2164897


## References
* http://mapsurfernet.com/blog/benchmarking-mapping-toolkits-in-tile-seeding
* https://github.com/mapnik/mapnik/wiki/UbuntuInstallation


## Keywords & Definitions
* **[Slippy Map](http://wiki.openstreetmap.org/wiki/Slippy_Map)**
  - It is, in general, a term referring to modern web maps which let you zoom and pan around (the map slips around when you drag the mouse).


## Bash Tutorials
* https://www.cyberciti.biz/faq/bash-for-loop/
* https://stackoverflow.com/questions/15580144/how-to-concatenate-multiple-lines-of-output-to-one-line
* https://stackoverflow.com/questions/20688552/assigning-the-output-of-a-command-to-a-variable-in-a-shell-script
```bash
apt-cache search mapnik | cut -d' ' -f1 |awk '{print}' ORS=' '
apt-cache search mapnik | cut -d' ' -f1 |tr '\n' ' '
output=$(apt-cache search mapnik | cut -d' ' -f1 |tr '\n' ' ');apt-cache policy $output

find $PWD -name <fileName>
```

* https://askubuntu.com/questions/275965/how-to-list-all-variables-names-and-their-current-values
```
print env
env
declare -p
declare -xp
( set -o posix ; set ) | less
compgen -v | while read line; do echo $line=${!line};done
```
### Using multiple compilers
* https://stackoverflow.com/questions/448457/how-to-use-multiple-versions-of-gcc
* https://codeyarns.com/2015/02/26/how-to-switch-gcc-version-using-update-alternatives/
* https://gist.github.com/application2000/73fd6f4bf1be6600a2cf9f56315a2d91
```bash
gcc -v
ls -ltr $(which gcc)
ls -ltr $(which g++)
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 100 --slave /usr/bin/g++ g++ /usr/bin/g++-5
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 50 --slave /usr/bin/g++ g++ /usr/bin/g++-6
sudo update-alternatives --config gcc
```
## apt-get

### Errors
Fetched 18.0 MB in 56s (321 kB/s)                                                                                                                                                       
Segmentation fault (core dumped)
Reading package lists... Error!
W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: http://dl.google.com/linux/chrome/deb stable Release: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 6494C6D6997C215E
N: Skipping acquire of configured file 'main/binary-i386/Packages' as repository 'http://rodeo-deb.yhat.com rodeo InRelease' doesn't support architecture 'i386'
W: Failed to fetch http://dl.google.com/linux/chrome/deb/dists/stable/Release.gpg  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 6494C6D6997C215E
E: Failed to fetch store:/var/lib/apt/lists/partial/archive.canonical.com_ubuntu_dists_xenial_partner_binary-i386_Packages.gz  Hash Sum mismatch
E: Failed to fetch https://dl.bintray.com/ornis/CloudCompare/dists/xenial/Release  No Hash entry in Release file /var/lib/apt/lists/partial/dl.bintray.com_ornis_CloudCompare_dists_xenial_Release which is considered strong enough for security purposes
E: Failed to fetch store:/var/lib/apt/lists/partial/in.archive.ubuntu.com_ubuntu_dists_xenial_main_dep11_Components-amd64.yml.gz  Hash Sum mismatch
W: Some index files failed to download. They have been ignored, or old ones used instead.
E: Problem executing scripts APT::Update::Post-Invoke-Success 'if /usr/bin/test -w /var/cache/app-info -a -e /usr/bin/appstreamcli; then appstreamcli refresh > /dev/null; fi'
E: Sub-process returned an error code

postgresql-9.5-postgis-2.3

**Reading package lists... Error!**
* https://unix.stackexchange.com/questions/139441/reading-package-lists-error


Reading package lists... Done
N: Skipping acquire of configured file 'main/binary-i386/Packages' as repository 'http://rodeo-deb.yhat.com rodeo InRelease' doesn't support architecture 'i386'
W: GPG error: http://dl.google.com/linux/chrome/deb stable Release: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 6494C6D6997C215E
W: The repository 'http://dl.google.com/linux/chrome/deb stable Release' is not signed.
N: Data from such a repository can't be authenticated and is therefore potentially dangerous to use.
N: See apt-secure(8) manpage for repository creation and user configuration details.
E:
E: Some index files failed to download. They have been ignored, or old ones used instead.

* http://www.danielgm.net/cc/forum/viewtopic.php?t=1762
* https://bintray.com/ornis/CloudCompare/CloudCompare/view/readmore#read

sudo add-apt-repository --remove ppa:romain-janvier/cloudcompare

**google chrome error**
* https://askubuntu.com/questions/599112/google-chrome-ppa-upgrade-invalid-signature

* This fixed the above error
```bash
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
```

**remove-architecture**
* https://askubuntu.com/questions/66875/how-to-disable-multiarch-support
dpkg --remove-architecture i386


down vote
First of all, remove all i386-packages like so:

sudo apt-get remove --purge `dpkg --get-selections | grep i386 | awk '{print $1}'`
Please note: Skype, Steam, teamviewer etc. might be purged as well.

Then proceed with fossfreedoms advices.

## Install Mapnik on ubuntu 16.04
* https://github.com/mapnik/mapnik/wiki/UbuntuInstallation
```
apt-cache  showpkg libboost-all-dev
```

* https://stackoverflow.com/questions/12578499/how-to-install-boost-on-ubuntu

## Install boot 1.64 (>=1.61 required, apt-get has 1.58)
```
./bootstrap.sh --prefix=/usr/local
user_configFile=`find $PWD -name user-config.jam`
echo "using mpi ;" >> $user_configFile
#Find CPU cores:
cat /proc/cpuinfo | grep "cpu cores" | uniq | awk '{print $NF}'
# set the path properly
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
sudo sh -c 'echo "/usr/local/lib" >> /etc/ld.so.conf.d/local.conf'
```

**Errors**
* paths not set properly
```
.sconf_temp/conftest_17: error while loading shared libraries: libboost_regex.so.1.64.0: cannot open shared object file: No such file or directory
Checking if boost_regex was built with ICU unicode support... (cached) no
```
* mapbox/geometry sub module is not cloned by default
```
# Error
# include/mapnik/geometry/point.hpp:26:37: fatal error: mapbox/geometry/point.hpp: No such file or directory
# 
git submodule init
git submodule update --init deps/mapbox/geometry
#other sub modules initialization
git submodule update --init test/data
git submodule update --init test/data-visual
```
* error: use of ‘auto boost::spirit::x3::detail::call
- https://github.com/mapnik/mapnik/issues/3587
```
# Error Stack
/usr/local/include/boost/spirit/home/x3/core/call.hpp:72:28: error: use of ‘auto boost::spirit::x3::detail::call(F, const Context&, mpl_::true_) [with F = mapnik::json::grammar::{anonymous}::<lambda(const auto:6&)>; Context = boost::spirit::x3::context<boost::spirit::x3::attr_context_tag, mapnik::json::json_value, boost::spirit::x3::context<boost::spirit::x3::where_context_tag, boost::iterator_range<const char*>, boost::spirit::x3::context<boost::spirit::x3::rule_val_context_tag, std::pair<std::__cxx11::basic_string<char>, mapnik::json::json_value>, boost::spirit::x3::context<boost::spirit::x3::parse_pass_context_tag, bool, boost::spirit::x3::context<mapnik::json::grammar::keys_tag, const std::reference_wrapper<boost::bimaps::bimap<boost::bimaps::unordered_set_of<std::__cxx11::basic_string<char> >, boost::bimaps::set_of<int> > >, boost::spirit::x3::context<boost::spirit::x3::skipper_tag, const boost::spirit::x3::char_class<boost::spirit::char_encoding::standard, boost::spirit::x3::space_tag>, boost::spirit::x3::unused_type> > > > > >; mpl_::true_ = mpl_::bool_<true>]’ before deduction of ‘auto’
         return detail::call(f, attr_context, is_callable<F(decltype(attr_context) const&)>());
                            ^
scons: *** [src/json/generic_json_grammar_x3.o] Error 1
scons: building terminated because of errors.
Makefile:23: recipe for target 'src/json/libmapnik-json.a' failed
make: *** [src/json/libmapnik-json.a] Error 2

## https://github.com/mapnik/mapnik/issues/3667


```
**Upgrade gcc from 5.4.1 to gcc-6**
- https://askubuntu.com/questions/746369/how-can-i-install-and-use-gcc-6-on-xenial
```bash
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt-get update
sudo apt-get install gcc-6 g++-6
# check version
gcc-6 --version | head -n 2
# configure the gcc
gcc -v
ls -ltr $(which gcc)
ls -ltr $(which g++)
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 100 --slave /usr/bin/g++ g++ /usr/bin/g++-5
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 50 --slave /usr/bin/g++ g++ /usr/bin/g++-6
sudo update-alternatives --config gcc
# **Note:** that this does not make gcc 6 your default compiler and this is probably best at the moment until this most recent version matures a little...
# 
## Error Stack
In file included from /usr/local/include/boost/geometry/strategies/transform/matrix_transformers.hpp:25:0,
                 from /usr/local/include/boost/geometry/strategies/strategies.hpp:104,
                 from /usr/local/include/boost/geometry/geometry.hpp:50,
                 from include/mapnik/geometry/boost_adapters.hpp:33,
                 from include/mapnik/geometry/correct.hpp:27,
                 from include/mapnik/json/create_geometry.hpp:27,
                 from include/mapnik/json/feature_grammar_x3_def.hpp:33,
                 from src/json/feature_grammar_x3.cpp:24:
/usr/local/include/boost/qvm/mat.hpp: In member function ‘boost::qvm::mat<T, Rows, Cols>::operator R() const’:
/usr/local/include/boost/qvm/mat.hpp:28:23: error: expected primary-expression before ‘(’ token
                 assign(r,*this);
                       ^
scons: *** [src/json/feature_grammar_x3.o] Error 1
scons: building terminated because of errors.
Makefile:23: recipe for target 'src/json/libmapnik-json.a' failed
make: *** [src/json/libmapnik-json.a] Error 2

```


```bash
# ./configure stack
bhaskar@maze:~/Documents/mapnik$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
bhaskar@maze:~/Documents/mapnik$ cat /etc/ld.so.conf.d/local.conf
/usr/local/lib
bhaskar@maze:~/Documents/mapnik$ ./configure
scons: Reading SConscript files ...

Welcome to Mapnik...

Configuring build environment...
SCons CONFIG found: 'config.py', variables will be inherited...
Configuring on Linux in *release mode*...
CXX c++ (Ubuntu 5.4.0-6ubuntu1~16.04.4) 5.4.0 20160609
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
Checking for freetype-config... yes
Checking for dlfcn.h support ... yes
Checking if compiler (c++) supports -std=c++14 flag... (cached) yes
Checking for C library z... yes
Checking for C++ library icuuc... yes
Checking for ICU version >= 4.2... found: icu 55.1
(cached) Checking for C++ library harfbuzz... yes
Checking for HarfBuzz version >= 0.9.34... found: HarfBuzz 1.0.1
Checking for HarfBuzz with freetype support
(cached) yes
Searching for boost libs and headers... (cached) 
Found boost libs: /usr/local/lib
Found boost headers: /usr/local/include
Checking for C++ header file boost/version.hpp... yes
Checking for Boost version >= 1.61... yes
Found boost lib version... 1_64
Checking for C++ library boost_system... yes
Checking for C++ library boost_filesystem... yes
Checking for C++ library boost_regex... yes
Checking for C++ library boost_program_options... yes
Checking whether Boost was compiled with C++11 scoped enums ... yes
Checking if boost_regex was built with ICU unicode support... (cached) yes
Checking for C library jpeg... yes
Checking for C library proj... yes
Checking for C library png... yes
Checking for C library webp... yes
Checking for C library tiff... yes
Checking for pkg-config... yes
Checking for requested plugins dependencies...
Checking for gdal-config --libs... yes
Checking for gdal-config --cflags... yes
Checking for name of gdal library... gdal
Checking for C++ library gdal... yes
Checking if gdal is ogr enabled... yes
Checking for gdal-config --libs... yes
Checking for gdal-config --cflags... yes
Checking for name of ogr library... gdal
Checking for C++ library gdal... yes
Checking for pg_config... yes
Checking for pg_config... yes
Checking for C library sqlite3... yes
Checking if SQLite supports RTREE... (cached) yes
Checking for cairo... yes
Checking for cairo lib and include paths...  yes
Checking for cairo freetype font support ... yes

All Required dependencies found!

Overwriting and re-saving file 'config.py'...
Will hold custom path variables from commandline and python config file(s)...

Configure completed: run `make` to build or `make install`
```

**node-mapnik**
* https://github.com/mapnik/node-mapnik
* http://mapnik.org/
* https://github.com/mapbox/awesome-vector-tiles


## Mapping
https://www.mapbox.com/mapping/

## GIS Software For Ubuntu
http://scigeo.org/articles/howto-install-latest-geospatial-software-on-linux.html#geos


Misc Tools & Libraries
These are other miscellaneous libraries/tools that are often needed as dependencies for other geospatial/scientific software described above.
MPI
MPI is a parallel computing standard that allows programs to take advantage of multiple processors. There are two competing MPI implementations available on most Linux distributions: mpich and openmpi. Generally, mpich is older and more compatible, particularly on CentOS, but both implementations have their own advantages.
Here I will describe how to install the mpich or openmpi MPI implementations from standard repositories on CentOS and Ubuntu. These libraries can then be used by boost, hdf5, flann, VTK, PCL, and other software.
Note: There also exists the openmp multiprocessing API, which is installed by default on CentOS and Ubuntu through the libgomp and libgomp1 packages, respectively. 