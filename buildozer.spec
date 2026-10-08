[app]

title = Abdo Saad Cyber Lab
package.name = abdosaadcyberlab
package.domain = org.abdosaad

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas

version = 0.1

requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b

android.archs = arm64-v8a

android.accept_sdk_license = True


[buildozer]

log_level = 2
warn_on_root = 1
