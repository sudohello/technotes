/*
Title: Reverse Engineering
Decription: Reverse Engineering
Author: Bhaskar Mangal
Date: 
Tags: Reverse Engineering
*/

# Reverse Engineering

## Decompilers

https://reverseengineering.stackexchange.com/questions/4624/how-do-i-reverse-engineer-so-files-found-in-android-apks
- https://onlinedisassembler.com/odaweb/
- https://retdec.com/
- https://www.frida.re/
- https://medium.com/@oleavr/build-a-debugger-in-5-minutes-1-5-51dce98c3544
You can also try a dynamic approach by hooking APIs and observing arguments and return values. This will allow you to look at data going into crypto APIs, which may help a lot when dealing with network protocols. Check out the Frida instrumentation toolkit for an open source cross-platform solution (Android, iOS, Windows, Mac and Linux). There's a tutorial showing how to build an interactive instrumentation tool in a few minutes, which injects code into the “Yo” app on iOS and plots network connections using Google Maps.
- https://derevenets.com/

Use android-ndk, https://developer.android.com/ndk/downloads/index.html.

You can use the toolchains inside the ndk to perform the type of disassembling you want to. For e.g. if I decompile an apk and get a .so library out of it, I will do :

./android-ndk-r15b/toolchains/arm-linux-androideabi-4.9/prebuilt/darwin-x86_64/bin/arm-linux-androideabi-objdump -T "SAMPLE.so | less

To get an objdump


https://github.com/yegord/snowman.git

./configure -qtnamespace QT -platform linux-g++-64 -release -confirm-license -opensource -no-audio-backend -nomake examples -prefix $HOME/opt/qt-5.6.1-64 && make && make install



https://askubuntu.com/questions/829310/how-to-upgrade-cmake-in-ubuntu