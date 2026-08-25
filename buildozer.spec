[app]
# (str) Title of your application
title = MHB3 App

# (str) Package name
package.name = mhb3app

# (str) Package domain
package.domain = org.mhb3

# (str) Source code directory
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json,txt,ttf,otf,db,html,css,js

# (str) Version of your application
version = 1.0.0

# (list) Requirements (Python packages for Android)
requirements = python3.10,kivy,kivymd,flask,reportlab,python-docx,jdatetime,arabic-reshaper,requests,python-bidi

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

[buildozer]
# (int) Android API level
android.api = 30

# (int) Minimum API level
android.minapi = 21

# (str) NDK version
android.ndk = 25b

# (bool) Accept SDK licenses automatically
android.accept_sdk_license = True

# (str) Branch of python-for-android
p4a.branch = master

# (str) Log level (2 for debug)
log_level = 2
