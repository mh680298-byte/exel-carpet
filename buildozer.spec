[app]
title = Rug Color Reader
package.name = rugreader
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xlsx,xlsm
version = 0.1
requirements = python3,kivy==2.2.1,openpyxl==3.1.2
orientation = portrait
fullscreen = 0
android.permissions = READ_EXTERNAL_STORAGE
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 30

# برای Ubuntu 24.04 این خط رو اضافه کن
android.ndk_version = 23b

[buildozer]
log_level = 2
warn_on_root = 1
