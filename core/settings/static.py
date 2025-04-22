import os

from decouple import config

from .base import BASE_DIR

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR.child("static"))

COMPRESS_ROOT = STATIC_ROOT

COMPRESS_ENABLED = True

COMPRESS_OFFLINE = False if config("MOD") == "DEVELOPMENT" else True

STATICFILES_DIRS = [
    os.path.join(
        BASE_DIR.child("modules")
        .child("global_app")
        .child("src")
        .child("common")
        .child("presentation")
        .child("staticfiles")
    ),
]
