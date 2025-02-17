[app]
# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp
version = 1.0.0
# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy,kivymd,pillow

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (list) Permissions
android.permissions = android.permission.INTERNET, android.permission.WRITE_EXTERNAL_STORAGE

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (int) Log level
log_level = 2
