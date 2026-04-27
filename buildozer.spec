[app]

title = CarpetMap
package.name = carpetmap
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv

version = 0.1

requirements = python3,kivy

orientation = portrait

fullscreen = 0


[buildozer]

log_level = 2

warn_on_root = 1


[app:android]

android.api = 33
android.minapi = 21
android.arch = armeabi-v7a
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True
