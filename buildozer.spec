### This setting is designed to comply with Google’s policy, such as applying a 16KB page size and Android SDK 35 or higher  ###
[app]
title = myAPP
package.name = myAPP
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
source.include_patterns = font/*,images/*.png
source.exclude_exts = spec,txt
source.exclude_dirs = tests, bin, venv, __pycache__
version = 0.9.9

requirements = python3,kivy==2.3.1,kivymd==1.2.0,sdl2_ttf,pillow,android,beautifulsoup4,soupsieve,requests==2.31.0,typing_extensions,plyer==2.1.0,pyjnius,olefile==0.47

presplash.filename = %(source.dir)s/images/presplash.png
icon.filename = %(source.dir)s/images/favicon.png
orientation = portrait,landscape
osx.python_version = 3
osx.kivy_version = 2.3.1
fullscreen = 0

android.permissions = android.permission.INTERNET, android.permission.ACCESS_NETWORK_STATE, android.permission.VIBRATE, android.permission.WRITE_EXTERNAL_STORAGE, android.permission.FOREGROUND_SERVICE

android.api = 35
android.minapi = 24
android.sdk = 35
android.ndk = 28
android.ndk_api = 24
android.private_storage = True

android.archs = arm64-v8a
android.add_linking_options = -Wl,--warn-shared-textrel

p4a.branch = develop

android.gradle_dependencies = androidx.appcompat:appcompat:1.6.1, androidx.activity:activity:1.6.1
android.enable_androidx = True
android.add_packaging_options = "jniLibs/useLegacyPackaging=true"

android.cmake_options = -DCMAKE_POLICY_VERSION_MINIMUM=3.18, -DCMAKE_C_FLAGS="-O2 -fPIC", -DCMAKE_CXX_FLAGS="-O2 -fPIC"

android.add_gradle_options = android.bundle.enableUncompressedNativeLibs=false

android.allow_backup = True
android.allow_cleartext_traffic = True

[buildozer]
log_level = 0
warn_on_root = 1

[android.manifest]
application.resizeableActivity = true
activity.screenOrientation = unspecified

application.largeHeap = true
application.hardwareAccelerated = true

uses-feature.android.hardware.screen.portrait = false
uses-feature.android.hardware.screen.landscape = false
