---
Title: Android App Development
Decription: Android App Development
Author: Bhaskar Mangal
Date: 
Tags: Android App Development
---

**Table of Contents**
* TOC
{:toc}


## Android App Development

## Development Environment Setup
* https://www.tutorialspoint.com/android/android_eclipse.htm
* https://www.javatpoint.com/how-to-setup-android-for-eclipse-ide
* https://www.monect.com/



### Android to PC
* https://github.com/koush/electron-chrome.git
* https://www.firstpost.com/tech/news-analysis/how-to-stream-video-from-your-android-device-to-a-pc-and-vice-versa-3587791.html


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



## Design Patterns in Android
https://www.raywenderlich.com/109843/common-design-patterns-for-android


https://digital.deutsches-museum.de/virtuell/#?image=764&core.init.lon=-0.60&core.init.lat=-0.24

https://de.navvis.com/pb2017-new
www.navvis.com/iv.dm-bp
https://de.navvis.com/bologna_fiere


http://iv.columbus-interactive.net/kunsthalle/#?image=1&core.init.lon=-2.08&core.init.lat=-0.76&fov=100.0

https://www.youtube.com/watch?v=1hIznGqq8S0
https://www.youtube.com/watch?v=nxC2wynlnIQ

## Kotlin V/s Java
https://arctouch.com/blog/kotlin-vs-java/

## Sublime Text Configurations

https://packagecontrol.io/packages/PackageResourceViewer

## Best References for Android
https://github.com/aritraroy/UltimateAndroidReference