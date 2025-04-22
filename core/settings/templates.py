import os

from .base import BASE_DIR

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(
                BASE_DIR.child("modules")
                .child("global_app")
                .child("src")
                .child("common")
                .child("presentation")
                .child("templates")
            ),
            os.path.join(
                BASE_DIR.child("modules")
                .child("authentication")
                .child("src")
                .child("presentation")
                .child("templates")
            ),
            os.path.join(
                BASE_DIR.child("modules")
                .child("tasks")
                .child("src")
                .child("presentation")
                .child("templates")
            ),
        ],
        "APP_DIRS": False,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "libraries": {
                "input_tags": "modules.global_app.src.common.presentation.templatetags.input_tags",
            },
            "loaders": [
                (
                    "django.template.loaders.cached.Loader",
                    [
                        "django_cotton.cotton_loader.Loader",
                        "django.template.loaders.filesystem.Loader",
                        "django.template.loaders.app_directories.Loader",
                    ],
                )
            ],
            "builtins": [
                "django_cotton.templatetags.cotton",
            ],
        },
    },
]

COTTON_DIR = "partials"
