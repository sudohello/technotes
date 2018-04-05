/*
Title: Android App Development
Decription: Android App Development
Author: Bhaskar Mangal
Date: 
Tags: Android App Development
*/

# Android App Development

**Table of Contents**

[TOC]

## Development Environment Setup
* https://www.tutorialspoint.com/android/android_eclipse.htm
* https://www.javatpoint.com/how-to-setup-android-for-eclipse-ide

### Eclipse
* https://stuff.mit.edu/afs/sipb/project/android/docs/sdk/installing/installing-adt.html

#### ADT Plugin for Eclipse
* http://dl-ssl.google.com/android/eclipse/


## Android Directory Structure & Best Practices
* https://www.supinfo.com/articles/single/4036-android-studio-structure-and-naming-best-practices
* https://github.com/futurice/android-best-practices
* http://blog.smartlogic.io/2013-07-09-organizing-your-android-development-code-structure/
* https://medium.com/@rey5137/how-i-organize-android-project-structure-5ed9b849dc30

## ADB
- https://developer.android.com/studio/command-line/adb.html#devicestatus
- https://android.stackexchange.com/questions/69108/how-to-start-root-shell-with-android-studio

Install the app on your device (from play store)
Download the apk from device to your desktop. You need to have adb working. To inspect Yelp app
```
adb devices # this should give the device_id in case you have multiple devices
adb -s device_id shell pm list packages | grep -i yelp # find yelp's package name
adb -s device_id shell pm path com.yelp.android # this gives apk path
adb -s device_id pull com.yelp.android-2.apk # pull the apk to the deskto
```
### Screen Recording and Snapshots
- https://www.androidauthority.com/android-customization-screen-recording-adb-599331/

## GUI

### layouts
* https://www.tutorialspoint.com/android/android_user_interface_layouts.htm

**Drawer Layout**
* https://developer.android.com/reference/android/support/v4/widget/DrawerLayout.html

## Trainings & Tutorials
- https://developer.android.com/training/building-location.html

### Material Design UI
- https://www.sitepoint.com/material-design-android-design-support-library/


### Theme
- https://developer.android.com/training/material/theme.html


## Android Internals
https://www.raywenderlich.com/155838/responsive-ui-tutorial-android

### Fundamentals
- https://developer.android.com/guide/components/fundamentals.html
- Android apps can be written using Kotlin, Java, and C++ languages. 
- The Android SDK tools compile your code along with any data and resource files into an APK, an Android package, which is an archive file with an .apk suffix. One APK file contains all the contents of an Android app and is the file that Android-powered devices use to install the app.
- each app is a different user.
- Each process has its own virtual machine (VM), so an app's code runs in isolation from other apps.
- The Android system implements the principle of least privilege.

**App components**
App components are the essential building blocks of an Android app. Each component is an entry point through which the system or a user can enter your app. Some components depend on others.

There are four different types of app components:
- Activities
  - An activity is the entry point for interacting with the user. It represents a single screen with a user interface. 
- Services
  - A service is a general-purpose entry point for keeping an app running in the background for all kinds of reasons.
  - It is a component that runs in the background to perform long-running operations or to perform work for remote processes.
  - A service does not provide a user interface
- Broadcast receivers
  - A broadcast receiver is a component that enables the system to deliver events to the app outside of a regular user flow, allowing the app to respond to system-wide broadcast announcements.
  - Because broadcast receivers are another well-defined entry into the app, the system can deliver broadcasts even to apps that aren't currently running.
  -  Although broadcast receivers don't display a user interface, they may create a status bar notification to alert the user when a broadcast event occurs. 
- Content providers
  - A content provider manages a shared set of app data that you can store in the file system, in a SQLite database, on the web, or on any other persistent storage location that your app can access.

* Each type serves a distinct purpose and has a distinct lifecycle that defines how the component is created and destroyed.
* A unique aspect of the Android system design is that any app can start another app’s component.

**Intent**
* Three of the four component types—activities, services, and broadcast receivers—are activated by an asynchronous message called an intent. Intents bind individual components to each other at runtime. You can think of them as the messengers that request an action from other components, whether the component belongs to your app or another.

**The manifest file**
Before the Android system can start an app component, the system must know that the component exists by reading the app's manifest file, AndroidManifest.xml. Your app must declare all its components in this file, which must be at the root of the app project directory.

### API References
**Framework API**
https://developer.android.com/reference/classes.html
**Support API v/s Framework API**
https://developer.android.com/reference/android/support/classes.html
https://developer.android.com/topic/libraries/support-library/index.html

#### View and ViewGroup Classes
* https://developer.android.com/reference/android/view/View.html

**View**
- This class represents the basic building block for user interface components. A View occupies a rectangular area on the screen and is responsible for drawing and event handling.
- View is the base class for widgets, which are used to create interactive UI components (buttons, text fields, etc.). 
- The ViewGroup subclass is the base class for layouts, which are invisible containers that hold other Views (or other ViewGroups) and define their layout properties.

## FAQs
* What is the difference between xmlns: app: and xmlns: Android?
  - https://www.quora.com/What-is-the-difference-between-xmlns-app-and-xmlns-Android
  - https://stackoverflow.com/questions/36044383/whats-the-use-of-app-namespace-in-android-xml
  - https://stackoverflow.com/questions/7119359/why-this-line-xmlnsandroid-http-schemas-android-com-apk-res-android-must-be

## User Interface Development Guide
* https://developer.android.com/guide/topics/ui/index.html
* https://developer.android.com/guide/topics/ui/overview.html

### Layouts
- https://developer.android.com/guide/topics/ui/declaring-layout.html#CommonLayouts

**Linear Layouts**
- https://developer.android.com/reference/android/widget/LinearLayout.html
- https://developer.android.com/guide/topics/ui/layout/linear.html

- A layout that arranges other views either horizontally in a single column or vertically in a single row.
- LinearLayout is a view group that aligns all children in a single direction, vertically or horizontally.
- You can specify the layout direction with the android:orientation attribute.

**Relative Layout**
- https://developer.android.com/guide/topics/ui/layout/relative.html

- RelativeLayout is a view group that displays child views in relative positions.
- The position of each view can be specified as relative to sibling elements (such as to the left-of or below another view) or in positions relative to the parent RelativeLayout area (such as aligned to the bottom, left or center).


**Recycler View**
- https://developer.android.com/guide/topics/ui/layout/recyclerview.html
- design and implement a dynamic user interface that runs efficiently


* view holder
   - The view holder objects are managed by an adapter
* layout manager
* adapter
  - The adapter creates view holders as needed.
  - The adapter also binds the view holders to their data. I


**list view**
- https://developer.android.com/guide/topics/ui/layout/listview.html

- ListView is a view group that displays a list of scrollable items.
- The list items are automatically inserted to the list using an Adapter.
- Adapter pulls content from a source such as an array or database query and converts each item result into a view that's placed into the list.


**Grid View**
- https://developer.android.com/guide/topics/ui/layout/gridview.html

- GridView is a ViewGroup that displays items in a two-dimensional, scrollable grid. The grid items are automatically inserted to the layout using a ListAdapter.


**Coordinator Layout**
https://developer.android.com/reference/android/support/design/widget/CoordinatorLayout.html

CoordinatorLayout is a super-powered FrameLayout. CoordinatorLayout is intended for two primary use cases:
- As a top-level application decor or chrome layout
- As a container for a specific interaction with one or more child views

**Frame Layout**
https://developer.android.com/reference/android/widget/FrameLayout.html
FrameLayout is designed to block out an area on the screen to display a single item. Generally, FrameLayout should be used to hold a single child view, because it can be difficult to organize child views in a way that's scalable to different screen sizes without the children overlapping each other. You can, however, add multiple children to a FrameLayout and control their position within the FrameLayout by assigning gravity to each child, using the android:layout_gravity attribute.

Child views are drawn in a stack, with the most recently added child on top. The size of the FrameLayout is the size of its largest child (plus padding), visible or not (if the FrameLayout's parent permits). Views that are GONE are used for sizing only if setConsiderGoneChildrenWhenMeasuring() is set to true.


#### App  Widget
- https://developer.android.com/guide/topics/appwidgets/index.html

- App Widgets are miniature application views that can be embedded in other applications (such as the Home screen) and receive periodic updates

### Web Views
- https://developer.android.com/guide/webapps/webview.html


Android WebView is used to display web page in android. The web page can be loaded from same application or URL. It is used to display online content in android activity.


E/libEGL: validate_display:255 error 3008 (EGL_BAD_DISPLAY)

**Krpano WebView**
https://krpano.com/forum/wbb/index.php?page=Thread&postID=61064

https://diego.org/2015/01/07/embedding-crosswalk-in-android-studio/
https://github.com/dougdiego/CrosswalkDemo
https://software.intel.com/en-us/html5/articles/why-use-crosswalk-for-android-builds


https://krpano.com/tours/corfu/

**Errors**
12-01 14:27:48.793 20338-20503/com.vidteq.indoormap E/Surface: getSlotFromBufferLocked: unknown buffer: 0xb92d4958
12-01 14:27:48.802 20338-20503/com.vidteq.indoormap D/OpenGLRenderer: endAllActiveAnimators on 0xb929ff68 (RippleDrawable) with handle 0xb98702d8
12-01 14:27:48.814 20338-20338/com.vidteq.indoormap I/chromium: [INFO:CONSOLE(5)] "The key "target-densitydpi" is not supported.", source: https://krpano.com/tours/corfu/ (5)

12-01 14:27:09.899 20338-20503/com.vidteq.indoormap E/Surface: getSlotFromBufferLocked: unknown buffer: 0xb934d1f8
12-01 14:27:09.955 20338-20759/com.vidteq.indoormap E/libEGL: validate_display:255 error 3008 (EGL_BAD_DISPLAY)
12-01 14:27:48.793 20338-20503/com.vidteq.indoormap E/Surface: getSlotFromBufferLocked: unknown buffer: 0xb92d4958

http://www.petelepage.com/blog/2013/02/viewport-target-densitydpi-support-is-being-deprecated/

* error javascript is required to view this panorama -> Enable javascript
* how-can-i-see-javascript-errors-in-webview-in-an-android-app
  - https://stackoverflow.com/questions/14859970/how-can-i-see-javascript-errors-in-webview-in-an-android-app
* Denied starting an intent without a user gesture, URI http://realview.mapmyindia.com/player/lucknow

## Rxbindings
https://academy.realm.io/posts/donn-felker-reactive-android-ui-programming-with-rxbinding/
https://go.pardot.com/l/210132/2017-08-10/9drkd?_ga=2.268130566.941323488.1512379306-1019531213.1512379306  

## Data Calls
**Loaders**
- https://developer.android.com/guide/components/loaders.html

## UI Templates
https://code.tutsplus.com/articles/7-android-templates-to-inspire-your-next-project--cms-25412
http://mediumwell.com/responsive-adaptive-mobile/


https://developer.android.com/guide/practices/screens_support.html

**TIPS**
- creating UI objects is a resource-intensive operation.
- keep your layout hierarchy flat, which improves performance.


http://garbtech.co.uk/android-implementing-a-google-maps-search-box-with-autocompletetextview-and-geocoder-api/
https://www.sitepoint.com/material-design-android-design-support-library/


1. Search Bar
https://stackoverflow.com/questions/31136527/add-search-toolbar-over-google-map-like-in-native-android-app

**Android UI Design and development**
* Layout Editor
  - https://developer.android.com/studio/write/layout-editor.html
* Contraint Layout
  - https://developer.android.com/training/constraint-layout/index.html
  - https://codelabs.developers.google.com/codelabs/constraint-layout/#0
* Layout Inspector
  - https://developer.android.com/studio/debug/layout-inspector.html
  - https://developer.android.com/studio/debug/pixel-perfect.html
  - Hierarchy Viewer (abandoned)
https://code.tutsplus.com/tutorials/android-tools-using-the-hierarchy-viewer--mobile-6997

android empty view hierarchy
  [2017-12-11 14:09:43 - hierarchyviewer]Missing forwarded port for ZX1D62H9VS

**Load and Parse JSON**
https://stackoverflow.com/questions/9605913/how-to-parse-json-in-android

**how-to-use-asynctask**
https://stackoverflow.com/questions/18289623/how-to-use-asynctask/18289746#18289746

**Retrofit - consuming JSON**
https://www.androidtutorialpoint.com/networking/retrofit-android-tutorial/

Retrofit is a networking library developed by Square through which we can seamlessly capture JSON response from Web. Now we don’t need any JSON Parser to parse the data. Retrofit literally composed of all features required for web services. You don’t need any AsyncTask, HttpurlConnection or JsonParser. I would suggest you to read more about advantages of Retrofit Android here: Retrofit vs Volley and AsyncTask.

https://github.com/square/retrofit
https://github.com/hotchemi/redpen-android/blob/master/app/build.gradle


https://www.journaldev.com/13639/retrofit-android-example-tutorial

https://github.com/square/retrofit/tree/master/retrofit-converters/gson
https://github.com/square/okhttp/tree/master/okhttp-logging-interceptor
https://github.com/google/gson

```
    compile 'com.squareup.okhttp3:okhttp:3.9.1'
    compile 'com.squareup.okhttp3:logging-interceptor:3.9.1'
    compile 'com.google.code.gson:gson:2.8.2'
    compile ('com.squareup.retrofit2:retrofit:2.3.0') {
        exclude module: 'okhttp'
    }
    compile 'com.squareup.retrofit2:converter-gson:2.3.0'
```

https://www.journaldev.com/13629/okhttp-android-example-tutorial


https://stackoverflow.com/questions/36634466/retrofit-2-0-request-get-to-a-json-file-as-endpoint

https://www.androidtutorialpoint.com/tips-tricks/automatic-getters-and-setters-generation-in-android-studio


**Log**
https://developer.android.com/reference/android/util/Log.html

**API sniffing**
https://blog.kulman.sk/hacking-a-mobile-api-and-how-to-protect-yourself/
http://docs.mitmproxy.org/en/stable/install.html
https://github.com/mitmproxy/mitmproxy/releases
https://www.telerik.com/fiddler

http://eliasbagley.github.io/reverseengineering/2016/12/02/reverse-engineering-instagram-api.html

https://www.frida.re/

## RESTAPI
https://blog.mwaysolutions.com/2014/06/05/10-best-practices-for-better-restful-api/

## Advance UI Layouts
- https://github.com/codepath/android_guides/wiki/Handling-Scrolls-with-CoordinatorLayout
ftp://ftp.micronet-rostov.ru/linux-support/books/programming/Mobile-Apps/Oreilly.Head.First.Android.Development.Jul.2012.pdf
https://passhojao.com/attachments/15acab2deac1aedbee41031f5ac4249a9bccaf0e/store/feeaca9131fb0f208b51d66e1545f17c77c8750e77931d4709d5606f5028/Head-First-Android-Development-2015.pdf

## Event Handling in Android
* **button-onclicklistener-in-android**
  - https://android--examples.blogspot.in/2015/01/button-onclicklistener-in-android.html

* **Bottomsheet Callback handling**
  - https://stackoverflow.com/questions/35618998/how-to-implement-bottom-sheets-using-new-design-support-library-23-2
  - http://droidmentor.com/exploring-bottom-sheets-in-android/
  - http://www.hidroh.com/2016/06/17/bottom-sheet-everything/
  - https://medium.com/android-bits/android-bottom-sheet-30284293f066
  - https://github.com/material-components/material-components-android/blob/master/lib/src/android/support/design/widget/BottomSheetBehavior.java
  ```java
  /** The bottom sheet is dragging. */
  public static final int STATE_DRAGGING = 1;
  /** The bottom sheet is settling. */
  public static final int STATE_SETTLING = 2;
  /** The bottom sheet is expanded. */
  public static final int STATE_EXPANDED = 3;
  /** The bottom sheet is collapsed. */
  public static final int STATE_COLLAPSED = 4;
  /** The bottom sheet is hidden. */
  public static final int STATE_HIDDEN = 5;
  /** The bottom sheet is half-expanded (used when mFitToContents is false). */
  public static final int STATE_HALF_EXPANDED = 6;
```

**View Visibilities**
- https://stackoverflow.com/questions/6950168/what-is-the-difference-between-the-int-used-by-view-visible-and-normal-ints


## Size Units in Android

* sp - scaled pixel
* dp


### Errors
https://stackoverflow.com/questions/37004069/errorjack-is-required-to-support-java-8-language-features


* **java.lang.RuntimeException: Unable to start activity ComponentInfo**

 java.lang.RuntimeException: Unable to start activity ComponentInfo{com.vidteq.indoormap/com.vidteq.indoormap.MainActivity}: android.os.NetworkOnMainThreadException

 https://stackoverflow.com/questions/19740604/how-to-fix-networkonmainthreadexception-in-android

 our Exception actually tells you exactly what you are doing wrong. You are not using another thread to perform NetworkOperations. Instead, you perform the network operation on your UI-Thread, which cannot (does not) work on Android.

Your code that connects to the url should be executed for example inside an AsyncTasks doInBackground() method, off the UI-Thread.

### Design
https://android-developers.googleblog.com/2015/05/android-design-support-library.html


#### Icons
- https://material.io/guidelines/style/icons.html#icons-product-icons

### AppCompatActivity
https://developer.android.com/reference/android/support/v7/app/AppCompatActivity.html
- Base class for activities that use the support library action bar features.
- You can add an ActionBar to your activity when running on API level 7 or higher by extending this class for your activity and setting the activity theme to Theme.AppCompat or a similar theme.

https://developer.android.com/topic/libraries/support-library/index.html

### Fragment
- A Fragment is a piece of an application's user interface or behavior that can be placed in an Activity.
- Though Fragment defines its own lifecycle, that lifecycle is dependent on its activity: if the activity is stopped, no fragments inside of it can be started; when the activity is destroyed, all fragments will be destroyed.
- Fragments can be used as part of your application's layout, allowing you to better modularize your code and more easily adjust your user interface to the screen it is running on

**how the layout xml are related to fragments**
- https://developer.android.com/training/basics/fragments/creating.html
- Support Library or v7 appcompat

### Activity
- https://developer.android.com/reference/android/app/Activity.html

An activity is a single, focused thing that the user can do. 
- Almost all activities interact with the user, so the Activity class takes care of creating a window for you in which you can place your UI with setContentView(View). 

### Support Library
- https://developer.android.com/topic/libraries/support-library/features.html
The Support Libraries provide a wide range of classes for building apps, from fundamental app components, to user interface widgets, to media handling, to TV app components. Many of the classes are backward compatible implementations, but some of them are new features in their own right.

**App Components**
These Support Library classes provide backward-compatible implementations of important, core platform features. These implementation typically extend earlier versions of the class to handle new methods and features added in more recent releases of the platform. Some of these classes are complete, static implementations of the framework APIs.

**User Interface**
These support library classes provide implementations of key user interface widgets and behaviors, and help you create more modern app interfaces on earlier devices. A few of these widgets are only available through the support library.

1. General-purpose layout containers
- **RecyclerView** - Creates a layout for displaying long lists, using a strategy to avoid high memory consumption. This class allows you to create a limited window view into a larger data set, thus avoiding consuming large amounts of memory when displaying the list. 
- **ViewPager** - Provides a layout that allows the user to flip left and right through pages of data.
- **GridLayout** - Provides a layout with its children in a rectangular grid, supporting arbitrary spans of contiguous cells and flexible space distribution. 
- **PercentFrameLayout and PercentRelativeLayout** - Provide layouts that support percentage based dimensions and margins for its child views and content.
- **FrameLayout**
  - https://developer.android.com/reference/android/widget/FrameLayout.html
  - FrameLayout is designed to block out an area on the screen to display a single item. 
  - Generally, FrameLayout should be used to hold a single child view, because it can be difficult to organize child views in a way that's scalable to different screen sizes without the children overlapping each other. 
  - Child views are drawn in a stack, with the most recently added child on top. 

2. Special-purpose layout containers
These support classes provide compatible implementations of specific layout patterns, such as drawer views that can be pulled from the edge of the screen, sliding panels, and nesting lists within lists.
- **DrawerLayout**
  - https://developer.android.com/reference/android/support/v4/widget/DrawerLayout.html
  - https://developer.android.com/training/implementing-navigation/nav-drawer.html
  - Creates a layout that allows for interactive drawer views to be pulled out from the edge of the view window.
- **SlidingPaneLayout** - Provides a horizontal, multi-pane layout for use at the top level of an app user interface for creating layouts that can smoothly adapt across many different screen sizes, expanding on larger screens and collapsing to fit on smaller screens.
- **NestedScrollView** - A scrolling layout that supports nesting of other scrolling views, allowing you to create lists, with items containing an additional, child lists. These nested lists can contain items that scroll horizontally or vertically, separately from the parent list.
- **SwipeRefreshLayout** - Provides a layout to support refreshing data for lists or other layout with a finger swipe gesture.

3. Views, dialogs, and widgets

**Material Design**
**Graphics**
**Accessibility**
**Media Playback**
**TV Apps**
**Utilities**

#### v4-Support-Library V/s v7-Support-Library
- https://stackoverflow.com/questions/18271429/difference-between-android-support-v7-appcompat-and-android-support-v4

## Blogs
https://android-developers.googleblog.com/2015/05/android-design-support-library.html

## Misc
http://www.agilemodeling.com/artifacts/sequenceDiagram.htm
http://indalog.ual.es/WWW/ecbs05.pdf

**compiling-vs-transpiling**
https://www.stevefenton.co.uk/2012/11/compiling-vs-transpiling/
**Kotlin**
https://kotlinlang.org/
**Native Development Kit (NDK)**
https://developer.android.com/ndk/index.html
**Cutom Components**
https://developer.android.com/guide/topics/ui/custom-components.html
**Vector Drawable**
https://www.youtube.com/watch?v=wlFVIIstKmA

## Lifecycles
https://github.com/fernandodev/android-training/wiki/2.-Lifecycle,-Application,-Activities-and-Fragments

**fragments**
https://developer.android.com/guide/components/fragments.html
https://github.com/codepath/android_guides/wiki/Creating-and-Using-Fragments

**Multiple screen size support**
https://developer.android.com/guide/practices/screens_support.html

## Errors
**Error:Jack is required to support java 8 language features**
- https://stackoverflow.com/questions/38223882/retrolambda-jack-is-required-to-support-java-8-warning-fix
	
* ```
Error:Jack is required to support java 8 language features. Either enable Jack or remove sourceCompatibility JavaVersion.VERSION_1_8.
```




### Android Issues

#### Gradle - Android Studio
**importing navvis sdk in android studio errors**
1. WARN - nal.AbstractExternalSystemTask - Cause: error in opening zip file
- zip file was corrupted, download manually in ${HOME}/.gradle folder or set the gradle to local path manually

https://stackoverflow.com/questions/42591546/gradle-sync-failed-cause-error-in-opening-zip-file-corrupt-dependency-cache



## APK decompilation
- https://github.com/TheZ3ro/apk2java-linux

## MMI SDK

**Setup your project**
Follow these steps to add the SDK to your project –
- Create a new project in Android Studio
- Copy the SDK jar file to project libs/ folder
- Add the following permissions to your AndroidManifest.xml file
**AndroidManifest.xml**
```
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```

- Add Gson library to your project: "compile 'com.google.code.gson:gson:2.3'"
  * https://stackoverflow.com/questions/37048731/gson-library-in-android-studio
  * https://guides.codepath.com/android/Leveraging-the-Gson-Library

- Add your API keys to the SDK
  * Make the following function calls in the Application Class -
```
LicenceManager.getInstance().setRestAPIKey("your_rest_api_key");
LicenceManager.getInstance().setMapSDKKey("your_java_script_key");
#
public class DemoApplication extends Application {

   @Override
   public void onCreate() {
       super.onCreate();
       LicenceManager.getInstance().setRestAPIKey("your_rest_api_key");
       LicenceManager.getInstance().setMapSDKKey("your_java_script_key");
   }
}
```

**References**
* [How to add Jar files](https://stackoverflow.com/questions/16608135/android-studio-add-jar-as-library)
* [Appplication Class](https://github.com/codepath/android_guides/wiki/Understanding-the-Android-Application-Class)

**Application Class**
- The Application class, or any subclass of the Application class, is instantiated before any other class when the process for your application/package is created.
- This class is primarily used for initialization of global state before the first Activity is displayed.
- uses of a custom application class:
  * Specialized tasks that need to run before the creation of your first activity
  * Global initialization that needs to be shared across all components (crash reporting, persistence)
  * Static methods for easy access to static immutable data such as a shared network client object
- never store mutable shared data inside the Application object since that data might disappear or become invalid at any time.
- store any mutable shared data using persistence strategies such as files, SharedPreferences or SQLite

## NavVis Campusnet

**AndroidManifest.xml**
```
<uses-sdk android:minSdkVersion="21" android:targetSdkVersion="25" />
    <uses-feature android:glEsVersion="30000" />
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.BLUETOOTH" />
    <uses-permission android:name="android.permission.BLUETOOTH_ADMIN" />
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
    <uses-permission android:name="android.permission.CAMERA" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    <uses-feature android:name="android.hardware.sensor.accelerometer" />
    <uses-feature android:name="android.hardware.camera" android:required="false" />
    <uses-feature android:name="android.hardware.camera.autofocus" android:required="false" />
    <uses-feature android:name="android.hardware.sensor.gyroscope" android:required="false" />
    <uses-feature android:name="android.hardware.sensor.compass" android:required="false" />
    <uses-feature android:name="android.hardware.bluetooth_le" android:required="false" />
    <uses-feature android:name="android.hardware.bluetooth" android:required="false" />
    <uses-feature android:name="android.hardware.wifi" android:required="false" />
    <uses-feature android:name="android.hardware.sensor.barometer" android:required="false" />
    <uses-feature android:name="android.hardware.location" android:required="false" />
    <uses-feature android:name="android.hardware.sensor.light" android:required="false" />
    <uses-feature android:name="android.hardware.sensor.proximity" android:required="false" />
    <uses-feature android:name="android.hardware.screen.landscape" android:required="false" />
    <uses-feature android:name="android.hardware.screen.portrait" android:required="false" />
    <uses-feature android:name="android.hardware.location.gps" android:required="false" />
    <meta-data android:name="com.google.android.gms.version" android:value="@integer/google_play_services_version" />
    <meta-data android:name="android.support.VERSION" android:value="25.3.1" />
```

## NavVis SDK

Attribute uses-feature#30000@glEsVersion at AndroidManifest.xml:24:19-46 is not a valid hexadecimal 32 bit value, found 30000

https://medium.com/@notestomyself/how-to-include-external-aar-file-using-gradle-6604b378e808

- altebeacon
- babric.io - tracking and mobile usage stats

## Camera Lib
https://github.com/Fotoapparat/Fotoapparat


## Lambda Expressions - USING LAMBDA EXPRESSIONS IN ANDROID
http://www.techjini.com/blog/using-lambda-expressions-android/


## FAQs

**Java**
* java-deep-clone**
  - https://alvinalexander.com/java/java-deep-clone-example-source-code
  - https://stackoverflow.com/questions/64036/how-do-you-make-a-deep-copy-of-an-object-in-java
* deep copy vs shallow copy**
  - http://www.jusfortechies.com/java/core-java/deepcopy_and_shallowcopy.php

**Android**
https://stackoverflow.com/questions/7181526/how-can-i-make-my-custom-objects-parcelable


* parcelable-vs-java-serialization
  - https://www.3pillarglobal.com/insights/parcelable-vs-java-serialization-in-android-app-development

Passing primitive data types like string, integer, float, etc. through intents is quite easy in Android. All you have to do is put the data with unique key in intents and send it to another activity. If a user wants to send Java objects through intent, Java class should be implemented using the Parcelable interface. Serialization, on the other hand, is a Java interface that allows users to implement the interface which gets marked as Serializable.

**parceable and deep copy**
  - https://gist.github.com/patrickhammond/732d20b6e89fda23be1b
  - https://developer.android.com/reference/android/os/Bundle.html
  - https://stackoverflow.com/questions/12363503/passing-a-custom-object-from-one-activity-to-another-parcelable-vs-bundle
  - https://developer.android.com/guide/components/activities/parcelables-and-bundles.html
  - https://stackoverflow.com/questions/28495830/android-convert-parcelable-to-json/28496138

**Parceable complex Objects**
- https://www.survivingwithandroid.com/2015/05/android-parcelable-tutorial-list-class-2.html

inner classes
variable with other class reference
boolean

```
# read
this.enable = in.readByte() != 0; // enable == true if byte != 0
# write
dest.writeByte((byte) (enable ? 1 : 0)); // if enable == true, byte == 1
```
enum

https://stackoverflow.com/questions/6201311/how-to-read-write-a-boolean-when-implementing-the-parcelable-interface


**Bundle**
- http://droidista.blogspot.in/2011/06/passing-complex-objects-to-another_04.html

https://stackoverflow.com/questions/10107442/android-how-to-pass-parcelable-object-to-intent-and-use-getparcelable-method-of

# Desgin Patterns
**Singleton Pattern**
http://www.java2novice.com/java_constructor_examples/singleton/

Java Singleton Class Example Using Private Constructor
We can make constructor as private. So that We can not create an object outside of the class.
This property is useful to create singleton class in java.
Singleton pattern helps us to keep only one instance of a class at any time.
The purpose of singleton is to control object creation by keeping private constructor.

**Best Implementations on Singleton Patterns**
https://www.journaldev.com/1377/java-singleton-design-pattern-best-practices-examples
**Inner Classes**
https://www.journaldev.com/996/java-inner-class

**Java Reflection**
https://www.journaldev.com/1789/java-reflection-example-tutorial

Java Reflection provides ability to inspect and modify the runtime behavior of application. Reflection in Java is one of the advance topic of core java. Using java reflection we can inspect a class, interface, enum, get their structure, methods and fields information at runtime even though class is not accessible at compile time. We can also use reflection to instantiate an object, invoke it’s methods, change field values.


In Java, items with the final modifier cannot be changed!

This includes final classes, final variables, and final methods:

A final class cannot be extended by any other class
A final variable cannot be reassigned to another value
A final method cannot be overridden


https://stackoverflow.com/questions/19151911/static-classes-and-final-classes-in-java

**Static Class**
https://docs.oracle.com/javase/tutorial/java/javaOO/nested.html

**URL,URI**
https://stackoverflow.com/questions/3487389/convert-string-to-uri

**Retrofit2**
https://futurestud.io/tutorials/retrofit-2-how-to-change-api-base-url-at-runtime-2


http://www.vogella.com/tutorials/AndroidLibraryProjects/article.html

## Understanding Context in Android
https://blog.mindorks.com/understanding-context-in-android-application-330913e32514

**Context switching in Android**
MainActivity.this

https://www.quora.com/In-Android-coding-what-does-MainActivity-this-do-and-what-are-MainActivity-and-this-separately-class-keyword-etc

https://stackoverflow.com/questions/22966601/what-is-different-between-mainactivity-this-vs-getapplicationcontext

Which context to use?
There are two types of Context:

Application context is associated with the application and will always be same throughout the life of application -- it does not change. So if you are using Toast, you can use application context or even activity context (both) because toast can be displayed from anywhere with in your application and is not attached to a specific window. But there are many exceptions, one exception is when you need to use or pass the activity context.

Activity context is associated with to the activity and can be destroyed if the activity is destroyed -- there may be multiple activities (more than likely) with a single application. And sometimes you absolutely need the activity context handle. For example, should you launch a new activity, you need to use activity context in its Intent so that the new launching activity is connected to the current activity in terms of activity stack. However, you may use application's context too to launch a new activity but then you need to set flag Intent.FLAG_ACTIVITY_NEW_TASK in intent to treat it as a new task.

Let's consider some cases:

MainActivity.this refers to the MainActivity context which extends Activity class but the base class (activity) also extends Context class, so it can be used to offer activity context.

getBaseContext() offers activity context.

getApplication() offers application context.

getApplicationContext() also offers application context.

- http://www.cs.dartmouth.edu/~campbell/cs65/lecture08/lecture08.html


This explanation is probably missing some subtle nuances but it should give you a better understanding of why one works but the other doesn't.

The difference is that MainActivity.this refers to the the current activity (context) where as the getApplicationContext() refers to the Application class.

The important differences between the 2 is that the Application class never has any UI associations and as such has no window token.

Long story short: For UI items that need context use the Activity.

## Floating Search

https://material.io/guidelines/patterns/search.html

## Recycle View
- https://www.androidhive.info/2016/01/android-working-with-recycler-view/

-----------

# Gaming Engine + GIS

## Unreal
https://wiki.unrealengine.com/Building_On_Linux


## GIS

Applications

* **Game Development**
https://80.lv/articles/the-mapbox-unity-sdk-launched/
https://blog.mapbox.com/bringing-real-world-places-into-your-game-b9f21bf869eb
https://blog.mapbox.com/drive-around-your-map-bd8c4536f431

https://github.com/ue4plugins/StreetMap

**Unreal Engine**
https://github.com/EpicGames/Signup

**Unity 3D**
https://blogs.unity3d.com/2015/08/26/unity-comes-to-linux-experimental-build-now-available/
https://forum.unity.com/threads/unity-on-linux-release-notes-and-known-issues.350256/page-2


* **Watershed Analysis**
https://en.wikipedia.org/wiki/Watershed
https://water.usgs.gov/edu/watershed.html
https://science.howstuffworks.com/environmental/conservation/issues/watershed1.htm
https://en.wikipedia.org/wiki/Drainage_basin

* **Noise Level Predictions**
https://sites.google.com/site/noiselevelprediction/
https://sites.google.com/site/elevationmapcreator/


* **APIs**
https://blog.mapbox.com/global-elevation-data-6689f1d0ba65
http://www.sarahmakesmaps.com/blog/2016/3/mines-and-mapbox


http://www.xmswiki.com/wiki/GSDA:GSDA

http://www.aw3d.jp/en/products/
http://www.opentopography.org/index.php
http://www.terrainmap.com/


https://maps-for-free.com/

Intention

The vision of Maps-For-Free is to offer free worldwide relief maps and other layers which can easily be integrated into existing map projects.

MFF-maps are released under Creative Commons CC0. You are free to adapt and use the relief maps and relief layer for commercial purposes without attributing the original author or source. Although not required, a link to maps-for-free.com is appreciated.

SRTM

SRTM (Shuttle Radar Topography Mission) was developed to collect three-dimensional measurements of the Earth's surface to generate a near-global digital elevation model (DEM). The mission was a cooperative project between the National Aeronautics and Space Administration (NASA), the National Geospatial-Intelligence Agency (NGA) of the U.S. Department of Defense (DoD), and the German and Italian space agencies.

SRTM flew on board the Space Shuttle Endeavour in February 2000 and used an interferometric radar system to map the topography of Earth's surface. Endeavour was launched in an orbit with an inclination of 57 degrees which allowed to map all of the Earth's landmass that lies between 60 degrees North and 56 degrees South.

SRTM data was processed into geographic tiles, each of which represents one by one degree of latitude and longitude. A degree of latitude measures 111 kilometers North South, a degree of longitude measures 111 kilometers East West or less, decreasing away from the equator. Each tile of this dataset contains 1201x1201 samples which is equipollent to a 90 m grid resolution at equator. All tiles together represent an image sized 432000 x 139200 pixel.

For technical reasons data are available between 60 degrees North and 56 degrees South latitud only. The relative horizontal accuracy is about ± 15 m, the relative vertical accuracy about ± 6 m. The original data came with data voids indicating insufficient contrast in the radar data. These data voids tend to occur over water bodies (lakes, rivers, coasts, etc.), areas with snow cover and in mountainous regions.

The original SRTM data are available from USGS.

GTOPO30

GTOPO30 is another free geographic dataset with a resolution of 43200 x 21600 pixel used to cover regions where SRTM data are not available. Streaky regions denote areas where data voids were extrapolated or where SRTM data were replaced by the lower resolution GTOPO30 data.

The relief maps are elevation maps, i.e. the coloring does not reflect the natural colors of scenic objects. Because one color is used for each ground level, some rivers and other objects may appear in unnatural colors. Lowland areas containing only few elevation information appear most likely single-colored.

In some cases the SRTM or GTOPO30 dataset failed to include small islands, and in other cases the islands are slightly mispositioned.

The GTOPO data are also available from USGS.

VMap0

VMap0 provides worldwide coverage of geo-spatial data and is equivalent to a scale of 1:1000000. The data are structured following the Vector Product Format (VPF) and can be downloaded from GIS-Lab. Most of the MFF-layers are based on one of the thematic data vmap0 layer.

Hans Braxmeier, Donaustraße 13, 89231 Neu-Ulm, Germany, mail@braxmeier.de, 01-01-2017

==================================

Context Understanding in Android
https://stackoverflow.com/questions/3572463/what-is-context-on-android

Recycler View
http://hmkcode.com/android-simple-recyclerview-widget-example/

* Building Android Library
https://android.jlelse.eu/things-i-wish-i-knew-when-i-started-building-android-sdk-libraries-dba1a524d619
https://github.com/nisrulz/android-tips-tricks#extra--android-libraries-built-by-me

* Module Based Development
https://medium.com/prismapp/modular-android-project-93dcd7f5b42
https://wiki.appcelerator.org/display/guides2/Android+Module+Development+Guide


https://openvisualfx.com/2017/07/26/intro-to-compositing-in-natron/
https://github.com/ue4plugins/StreetMap

http://learnosm.org
https://wiki.openstreetmap.org/wiki/Video_tutorials

https://en.wikipedia.org/wiki/List_of_3D_rendering_software
http://www.geniusdv.com/news_and_tutorials/2009/03/open_souce_3d_alternativeblender.php

http://wiki.openstreetmap.org/wiki/Blender
https://blender.stackexchange.com/questions/62619/how-to-import-3d-buildings-from-openstreetmap-to-blender
https://github.com/vvoovv/blender-osm/wiki/Import-OpenStreetMap-(.osm)


https://github.com/domlysz/BlenderGIS

https://github.com/domlysz/BlenderGIS/wiki/Install-and-usage

http://wiki.openstreetmap.org/wiki/Unity
http://barankahyaoglu.com/dev/openstreetmap-in-unity3d/

http://infinity-code.com/en/products/real-world-terrain

http://barankahyaoglu.com/dev/pokemongo-clone-using-mapzen-api-unity3d/

http://wiki.openstreetmap.org/wiki/Blender#blender-osm:_OpenStreetMap_and_Terrain_for_Blender

## Mapbox vector tile specifications
https://www.mapbox.com/vector-tiles/specification/
https://github.com/mapbox/vector-tile-spec
https://github.com/mapbox/awesome-vector-tiles

https://github.com/google/protobuf

http://schwanksta.com/blog/vector-tiles-introduction-pt1

https://stackoverflow.com/questions/39347389/attribute-already-defined-with-incompatible-format-original-attribute-defined-h

http://abhiandroid.com/materialdesign/toolbar


## Search Activity in ActionBar - TBD
https://www.sitepoint.com/better-user-interfaces-android-action-bar/

**Give toolbar to each fragment!**
> Or how did we change global toolbar to small local toolbars

https://medium.com/@programmerr47/give-toolbar-to-each-fragment-52c3a996deb5


https://developer.android.com/training/basics/fragments/fragment-ui.htmlhttps://developer.android.com/training/basics/fragments/fragment-ui.html

https://stackoverflow.com/questions/19722979/implementing-multiple-fragments-in-a-single-activity-dynamically


**All about fragments basics**
https://github.com/codepath/android_guides/wiki/Creating-and-Using-Fragments


https://developer.android.com/training/appbar/index.html
http://www.theappguruz.com/blog/android-working-android-actionbar

https://guides.codepath.com/android/using-the-app-toolbar


http://www.androidhello.com/Android-examples-codes/Android-Code-Examples.php?Code_Examples_Programs=3687&Code_examples=Demonstration_of_using_fragments_to_implement_different_activity_layouts._:_Fragment_%C2%AB_UI_%C2%AB_Android


http://www.vogella.com/tutorials/Android/article.html

https://google-developer-training.gitbooks.io/android-developer-fundamentals-course-practicals/content/en/Unit%202/43_pc_tab_navigation.html

https://medium.com/@lucasurbas/making-android-toolbar-responsive-2627d4e07129

https://www.codota.com/android/methods/android.content.res.Resources.Theme/resolveAttribute



###Google Maps

http://www.androidhive.info/2013/08/android-working-with-google-maps-v2/

**Fake GPS location
https://github.com/codepath/android_guides/wiki/Google-Maps-Fragment-Guide



https://www.androidhive.info/2017/12/android-working-with-bottom-sheet/

## Back Key Handling

public boolean onKeyDown(int keyCode, KeyEvent event) {}

keycode:4
event: {
 action=ACTION_DOWN
 ,keyCode=KEYCODE_BACK
 ,scanCode=0
 ,metaSate=0
 ,flages=0x48
 ,repeatCount=0
 ,eventTime=27330534,
 ,downTime=26330534
 ,deviceId=-1
 ,source=0x101
}

getFragmentManager required android.support.v4.app.Fragment  found android.app.Fragment

https://stackoverflow.com/questions/38284378/error-required-androidsupport-v4-fragmentmanager-found-android-app-fragment

https://gunhansancar.com/best-practice-to-instantiate-fragments-with-arguments-in-android/


java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.Object java.lang.ref.WeakReference.get()' on a null object reference
                                                                                  at android.support.design.widget.BottomSheetBehavior.onInterceptTouchEvent(BottomSheetBehavior.java:287)
                                                                                  at android.support.design.widget.CoordinatorLayout.performIntercept(CoordinatorLayout.java:460)


https://stackoverflow.com/questions/17014470/keep-action-bar-stable-during-activity-transition-animation/36248564


## Rempte Loggin for denuggin Android Applications
Remote logging is the solution that helps to debug the problem. Remote logging the right set of information could provide valuable information that would be difficult to gather otherwise, and could help unveil unexpected behaviours and bugs. 

https://android.jlelse.eu/android-remote-logger-library-for-debugging-343443bd38b7

HyperLog is a utility logger library for Android on top of standard Android Log class for debugging purpose. This is a simple library that will allow Android apps or library to store log message into the database so that developer can pull the logs from the database into the file or push the logs to your server for debugging from the database as a file.

https://github.com/hypertrack/hyperlog-android
https://github.com/hypertrack/hyperlog-android/tree/master/hyperlog-demo

https://www.androidcode.ninja/android-http-client/

requestb
https://requestb.in/1lswbi61?inspect

## FCM Notification
https://firebase.google.com/docs/cloud-messaging/

## Volley Library
http://www.technotalkative.com/android-volley-library-example/


**Native lib**
https://reverseengineering.stackexchange.com/questions/4624/how-do-i-reverse-engineer-so-files-found-in-android-apks

## Fab and Bottomshteet
https://lab.getbase.com/introduction-to-coordinator-layout-on-android/


## GIS, PCD and other resources
http://nerdxchange.github.io/

https://github.com/Oslandia/lopocs


## Infor, Warnings and Error Messages
**Skipped 83 frames!  The application may be doing too much work on its main thread.**
01-18 14:02:52.969 9424-9424/com.ceinfo.sampleapplication I/Choreographer: Skipped 83 frames!  The application may be doing too much work on its main thread.
- https://stackoverflow.com/questions/14678593/the-application-may-be-doing-too-much-work-on-its-main-thread
- https://stackoverflow.com/questions/11254523/android-runonuithread-explanation


W/Adreno-ES20: <core_glTexImage2D:501>: GL_INVALID_OPERATION

01-18 14:02:53.043 9424-10154/com.ceinfo.sampleapplication D/ConnectivityManager.CallbackHandler: CM callback handler got msg 524290


01-18 14:02:52.701 9424-9424/com.ceinfo.sampleapplication I/art: Rejecting re-init on previously-failed class java.lang.Class<com.android.webview.chromium.WebViewContentsClientAdapter$6>


01-18 14:02:53.353 9424-10175/com.ceinfo.sampleapplication E/libEGL: validate_display:255 error 3008 (EGL_BAD_DISPLAY)


01-18 14:02:53.446 9424-10175/com.ceinfo.sampleapplication W/VideoCapabilities: Unrecognized profile 2130706433 for video/avc
01-18 14:02:53.465 9424-10175/com.ceinfo.sampleapplication W/VideoCapabilities: Unrecognized profile/level 0/3 for video/mpeg2
01-18 14:02:53.503 9424-10175/com.ceinfo.sampleapplication I/VideoCapabilities: Unsupported profile 4 for video/mp4v-es
01-18 14:05:13.922 9424-9439/com.ceinfo.sampleapplication I/art: Background sticky concurrent mark sweep GC freed 167859(8MB) AllocSpace objects, 52(2016KB) LOS objects, 35% free, 21MB/33MB, paused 4.077ms total 190.987ms


http://0dff6467.ngrok.io/mmioffice/api/block_routing?destination_latitude=12.982967&destination_longitude=77.641527&destination_z=11.407388&source_latitude=12.982755&source_longitude=77.641556&source_z=6.330339




## NavVis Routing
Mobile:
http://10.4.71.19:8080/mmi/api/block_routing?source_longitude=77.268940844553&source_latitude=28.550433972165&destination_longitude=77.268940844553&destination_latitude=28.550433972165
Web:
http://10.4.71.19:8080/mmioffice/api/route?simplify=1&sourcePoiId=28&targetPoiId=6


Mobile Routing API
http://182.76.28.84:8080/MMI06Jan/api/block_routing?source_longitude=77.268940844553&source_latitude=28.550433972165&destination_longitude=77.268940844553&destination_latitude=28.550433972165

http://0dff6467.ngrok.io/mmioffice/api/block_routing?destination_latitude=12.982823&destination_longitude=77.641524&destination_z=7.541952&source_latitude=12.982755&source_longitude=77.641556&source_z=6.330339

Web Routing API
http://182.76.28.84:8080/MMI06Jan//api/route?simplify=1&sourcePoiId=28&targetPoiId=6

http://www.vogella.com/tutorials/AndroidTools/article.html



http://182.76.28.84:8080/MMI06Jan/version.json
https://a.tiles.mapbox.com/v4/mapbox.streets/9/256/255.png?access_token=pk.eyJ1IjoibmF2dmlzIiwiYSI6ImNpcWIzMWM1NjAwOGloeG5zMHRmZ2lxczYifQ.BkHod770NEWxRIyNqb8QZw.png
http://182.76.28.84:8080/MMI06Jan/api/site_info/geometry
http://182.76.28.84:8080/MMI06Jan/api/camera_heads
http://182.76.28.84:8080/MMI06Jan/api/tiled_maps
http://182.76.28.84:8080/MMI06Jan/api/site_model?propagate_polygon_from_parent=true
http://182.76.28.84:8080/MMI06Jan/data/bundle_b905ee3f-878c-45c0-8390-e2aca9127bc2/building_5/map_tiles/6/0/0/0.png
http://182.76.28.84:8080/MMI06Jan/data/bundle_b905ee3f-878c-45c0-8390-e2aca9127bc2/building_5/map_tiles/7/0/0/0.png
http://182.76.28.84:8080/MMI06Jan/data/bundle_b905ee3f-878c-45c0-8390-e2aca9127bc2/building_5/map_tiles/8/0/0/0.png
https://a.tiles.mapbox.com/v4/mapbox.streets/9/272/178.png?access_token=pk.eyJ1IjoibmF2dmlzIiwiYSI6ImNpcWIzMWM1NjAwOGloeG5zMHRmZ2lxczYifQ.BkHod770NEWxRIyNqb8QZw.png
http://182.76.28.84:8080/MMI06Jan/api/poi_types
http://182.76.28.84:8080/MMI06Jan/api/edges
http://182.76.28.84:8080/MMI06Jan/api/nodes
http://182.76.28.84:8080/MMI06Jan/api/images
http://182.76.28.84:8080/MMI06Jan/api/wifi/compressed
http://182.76.28.84:8080/MMI06Jan/api/wifi/conditionals?detector_false_negative=0.5&detector_false_positive=0.1&unscanned_area_probability=0.5
http://182.76.28.84:8080/MMI06Jan/api/pois

http://182.76.28.84:8080/MMI06Jan/api/camera_heads
http://182.76.28.84:8080/MMI06Jan/api/camera_heads/pano/tiles/pano-01.obj
http://182.76.28.84:8080/MMI06Jan/api/block_routing?destination_latitude=28.550477&destination_longitude=77.268936&destination_z=4.613518&source_latitude=28.550620&source_longitude=77.268984&source_z=3.230880
http://182.76.28.84:8080/MMI06Jan/data/bundle_b905ee3f-878c-45c0-8390-e2aca9127bc2/building_5/map_tiles/7/1/0/0.png
http://182.76.28.84:8080/MMI06Jan/data/2018-01-06_11.33.18/pano/tiles/r0/0/00092-pano-tex-r0-20.jpg

/opt/NavVis/tools/scripts/templates/template-application.yaml

  1 spring:
  2   datasource:
  3     url: jdbc:postgresql://localhost:5432/routing
  4     username: navvis
  5     password: Ks3ihHZm;=)
  6 

db_url = "jdbc:postgresql://" + db_host + ":" + db_port + "/" + db_name

http://10.4.71.19:8080/mmi2/api/site_info/geometry
{"center_longitude":52.90975165756458,"center_latitude":28.550640315785554,"width":9450516.415901689}

http://10.4.71.19:8080/mmioffice/api/site_info/geometry
{"center_longitude":45.31205285818783,"center_latitude":12.982743430470244,"width":1.3973270081875918E7}

http://10.4.71.19:8080/mmi/api/site_info/geometry
{"center_longitude":52.90970528920729,"center_latitude":28.550640315788257,"width":9450498.704897897}

http://182.76.28.84:8080/MMI06Jan/api/site_info/geometry
{"center_longitude":52.90971144768285,"center_latitude":28.550622898869204,"width":9450510.601716114}

http://182.76.28.84:8080/vidteq/api/site_info/geometry
{"center_longitude":52.9097032716141,"center_latitude":28.550638790681347,"width":9450499.261943098}

http://182.76.28.84:8080/MMI_FF_15May_01/api/site_info/geometry
{"center_longitude":52.9097032716141,"center_latitude":28.550638790681347,"width":9450499.261943098}


**Routing Debuging**
http://182.76.28.84:8080/vidteq/api/block_routing?destination_latitude=28.550828&destination_longitude=77.268892&destination_z=0.433196&source_latitude=28.550647&source_longitude=77.268949&source_z=-0.042632

http://182.76.28.84:8080/vidteq/api/block_routing?destination_latitude=28.550806&destination_longitude=77.268963&destination_z=2.618006&source_latitude=28.550647&source_longitude=77.268949&source_z=-0.042632

http://182.76.28.84:8080/vidteq/api/block_routing?destination_latitude=28.550716&destination_longitude=77.268923&destination_z=1.678779&source_latitude=28.550647&source_longitude=77.268949&source_z=-0.042632

http://182.76.28.84:8080/vidteq/api/block_routing?destination_latitude=28.550706&destination_longitude=77.268928&destination_z=8.830527&source_latitude=28.550647&source_longitude=77.268949&source_z=-0.042632

https://a.tiles.mapbox.com/v4/mapbox.streets/19/374675/218728.png?access_token=pk.eyJ1IjoibmF2dmlzIiwiYSI6ImNpcWIzMWM1NjAwOGloeG5zMHRmZ2lxczYifQ.BkHod770NEWxRIyNqb8QZw.png


## Android with Mapbox GL SDK
https://stackoverflow.com/questions/31487520/mapbox-gl-using-external-maps

repositories {
  mavenCentral()
}
 
dependencies {
  implementation 'com.mapbox.mapboxsdk:mapbox-android-sdk:5.3.1'
}



## Mapbox GL

* Map Events, Popups
https://ovrdc.github.io/gis-tutorials/mapbox/03-query-features/#5.06/42.868/-109.372/0.5/2
https://www.mapbox.com/mapbox-gl-js/example/popup-on-click/
https://ovrdc.github.io/gis-tutorials/mapbox/03-query-features/#5.06/42.868/-109.372/0.5/2
https://bl.ocks.org/danswick/2f72bc392b65e77f6a9c
https://www.mapbox.com/mapbox-gl-js/plugins/
https://bl.ocks.org/danswick/36796153bd86ce982a59043cbe0ac8f7

http://www.navvis.lmt.ei.tum.de/view/#
http://www.navvis.lmt.ei.tum.de/view.pc/
http://www.navvis.lmt.ei.tum.de/about/

https://stackoverflow.com/questions/1527803/generating-random-whole-numbers-in-javascript-in-a-specific-range