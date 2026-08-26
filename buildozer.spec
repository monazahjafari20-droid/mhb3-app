[app]
title = MHB3 App
package.name = mhb3app
package.domain = org.mhb3
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt,ttf,otf,db,html,css,js
version = 1.0.0

requirements = python3.10,kivy,kivymd,flask,reportlab,python-docx,jdatetime,arabic-reshaper,requests,python-bidi

orientation = portrait
fullscreen = 0

[buildozer]
android.api = 30
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
p4a.branch = master
log_level = 2

# ★★★ حیاتیترین خط: استفاده از SDK گیتهاب به جای دانلود مجدد ★★★
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724
