[app]
title = MHB3 App
package.name = mhb3app
package.domain = org.mhb3
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt,ttf,otf,db,html,css,js
version = 1.0.0

requirements = python3.11,kivy,kivymd,flask,reportlab,python-docx,jdatetime,arabic-reshaper,requests,python-bidi

orientation = portrait
fullscreen = 0

[buildozer]
android.api = 33
android.minapi = 24
android.ndk = 28c
android.accept_sdk_license = True
p4a.branch = master
log_level = 2
