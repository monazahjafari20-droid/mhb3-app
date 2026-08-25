[app]
# (str) Title of your application
title = MHB3 App
package.name = mhb3app
package.domain = org.mhb3
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
# حتما NDK و API را روی نسخه های پایدار بگذار
android.api = 34
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
# نسخه پلتفرم برای بیلد (مهم)
p4a.branch = master
log_level = 2
