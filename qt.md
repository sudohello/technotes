---
Title: QT
Decription: QT
Author: Bhaskar Mangal
Date: 14th-Apr-2018
Tags: QT
---

**Table of Contents**
* TOC
{:toc}


## QT

## QT Installations from Source
- https://www.ics.com/blog/how-compile-qt-source-code-linux
- https://stackoverflow.com/questions/47100545/how-to-build-qtwebengine-5-10-from-source
- https://wiki.qt.io/Building_Qt_5_from_Git
- https://wiki.qt.io/Building_Qt_for_Embedded_Linux
- http://amin-ahmadi.com/2017/10/16/how-to-build-qt-from-source-codes/
_ [Main](https://wiki.qt.io/Building_Qt_5_from_Git)

**Configure Options**
https://doc.qt.io/archives/qtopia4.3/buildsystem/over-configure-options-qt-1.html


* install all dependencies: wiki.qt.io/Building_Qt_5_from_Git
1) build qt 5.10
```bash
git clone git://code.qt.io/qt/qt5.git qt5
cd qt5
perl init-repository --module-subset=default,-qtwebengine
./configure -developer-build -opensource -nomake examples -nomake tests
make
```
2) after qt5.10 builded same steps
```bash
git clone git://code.qt.io/qt/qt5.git qwebeng
cd qwebeng
perl init-repository --module-subset=qtwebengine,qtwebplugin,qtwebsoskets,qtwebview
cd qtwebengine
/yourQt5.10dir/base/bin/qmake
make -j
```

$ /path/to/qt/configure -developer-build -xplatform android-g++ -android-ndk /opt/android-ndk -android-sdk /opt/android-sdk -nomake tests -nomake examples -opensource -confirm-license


./configure -developer-build -xplatform android-g++ -nomake examples -nomake tests -opensource -confirm-license




./configure -prefix QtNew -release -opensource -confirm-license -static -qt-xcb -no-glib -no-pulseaudio -no-alsa -opengl desktop -nomake examples -nomake tests 

WARNING: gperf is required to build QtWebEngine.

WARNING: bison is required to build QtWebEngine.

WARNING: flex is required to build QtWebEngine.

# ubuntu 16.04 install bison
# https://www.howtoinstall.co/en/ubuntu/xenial/gperf
sudo apt install gperf


```bash
sudo apt install bison build-essential gperf flex ruby python libasound2-dev libbz2-dev libcap-dev \
libcups2-dev libdrm-dev libegl1-mesa-dev libgcrypt11-dev libnss3-dev libpci-dev libpulse-dev libudev-dev \
libxtst-dev gyp ninja-build libssl-dev libxcursor-dev libxcomposite-dev libxdamage-dev libxrandr-dev \
libfontconfig1-dev libxss-dev libsrtp0-dev libwebp-dev libjsoncpp-dev libopus-dev libminizip-dev \
libavutil-dev libavformat-dev libavcodec-dev libevent-dev

sudo apt install -y mesa-common-dev libglu1-mesa-dev

sudo apt install flex bison gperf libicu-dev libxslt-dev ruby

sudo apt install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev

sudo apt install libssl-dev libxcursor-dev libxcomposite-dev libxdamage-dev libxrandr-dev libdbus-1-dev libfontconfig1-dev libcap-dev libxtst-dev libpulse-dev libudev-dev libpci-dev libnss3-dev libasound2-dev libxss-dev libegl1-mesa-dev gperf bison

sudo apt install libasound2-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev
```

git submodule foreach --recursive "git clean -dfx" && git clean -dfx
git checkout 5.10
git submodule update --init --recursive
perl init-repository -f
./configure -nomake examples -nomake tests -opensource -confirm-license -skip qtquick1
./configure -developer-build -nomake examples -nomake tests -opensource -confirm-license -skip qtquick1


work -I/home/game/softwares/qt5/qtbase/include/QtCore -I/usr/include/c++/5 -I/usr/include/x86_64-linux-gnu/c++/5 -I/usr/include/c++/5/backward -I/usr/lib/gcc/x86_64-linux-gnu/5/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/5/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include qml/qdeclarativecontext.h -o .moc/moc_qdeclarativecontext.cpp
graphicsitems/qdeclarativetextinput.cpp: In member function ‘void QDeclarativeTextInput::setCursorVisible(bool)’:
graphicsitems/qdeclarativetextinput.cpp:517:17: error: ‘class QWidgetLineControl’ has no member named ‘setCursorBlinkPeriod’
     d->control->setCursorBlinkPeriod(on?QApplication::cursorFlashTime():0);

https://bugreports.qt.io/browse/QTBUG-61564
./init-repository --branch --module-subset=essential && ./configure --opensource --developer-build --confirm-license -nomake examples -nomake tests && make

run ./init-repository --branch -f before configure
or
add -skip qtquick1 to configure (since it's most probably not used anyways by you?)

http://wiki.qt.io/Unix_shell_tricks_for_developing_Qt




LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/softwares/qt5/qtbase/lib
PATH=$PATH:$HOME/softwares/qt5/qtbase/bin
