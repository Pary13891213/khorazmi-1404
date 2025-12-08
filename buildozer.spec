[app]

title = Khorazmi 1404
package.name = khorazmi_1404
package.domain = org.khorazmi
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,ttf,wav,mp3
version = 0.1

# فایل اصلی برنامه
entrypoint = main.py

# آیکون (دلخواه)
icon.filename = %(source.dir)s/images/Neon.png

# کتابخانه‌های پایتون
requirements = python3,kivy

# اسکرین جهت اجرای اپ
orientation = portrait

# اجازه‌ها (در صورت نیاز)
android.permissions = INTERNET

# مخفی‌سازی نوار دکمه‌ها
fullscreen = 0

#
[buildozer]
log_level = 2
warn_on_root = 0

[app]
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
