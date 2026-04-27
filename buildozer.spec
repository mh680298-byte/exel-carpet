[app]
# نام اپ نهایی
title = CarpetMap
# نام پکیج داخلی (نباید فاصله یا حروف بزرگ داشته باشه)
package.name = carpetmap
# دامنه معکوس برای پکیج
package.domain = org.example
# فایل اصلی Kivy
source.dir = .
source.include_exts = py, png, jpg, kv, atlas
# نسخه برنامه
version = 1.0
# آیکن اپ (اختیاری)
#icon.filename = icon.png

# در صورت نیاز به فایل‌های اضافی داخل apk
# source.include_patterns = assets/*

# تنظیمات buildozer برای Android
requirements = python3, kivy
orientation = portrait

# اگر برنامه به دسترسی خاص مثل فایل یا اینترنت نیاز دارد:
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# --------------------------------------------------
# 🎯 نسخه‌های SDK و NDK ثابت‌سازی‌شده
# --------------------------------------------------
android.api = 33
android.sdk = 33
android.ndk = 25b
android.minapi = 21

# لایسنس SDK را خودکار قبول کن
android.accept_sdk_license = True

# پلتفرم هدف
android.archs = arm64-v8a

# --------------------------------------------------
# تنظیمات اضافی برای کاهش خطا در CI
# --------------------------------------------------
# از سیستم‌عامل GitHub استفاده می‌کنیم، نیازی به virtualenv در CI نیست
builddir = ./.buildozer
# در buildو CI همیشه مسیرهای ثابت نگه‌دار
log_level = 2

# --------------------------------------------------
# اختیاری: اگر از Excel یا ماژول‌های خاص استفاده می‌کنی
# --------------------------------------------------
# requirements = python3, kivy, pandas, openpyxl

# --------------------------------------------------
# تنظیمات خروجی و نام فایل
# --------------------------------------------------
android.entrypoint = org.kivy.android.PythonActivity
android.allow_backup = True
# مسیر خروجی build
bin.dir = bin
