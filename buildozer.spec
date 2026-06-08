[app]
title = Al Yusr Lab
package.name = alyusrlab
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.api = 33
android.minapi = 21
android.sdk = 23
android.ndk = 25b
android.entrypoint = org.kivy.android.PythonActivity
android.presplash_color = #FFFFFF
android.archs = arm64-v8a,armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 0
