INSTALLED_APPS = [
    "grappelli",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "compressor",
    "django_cotton.apps.SimpleAppConfig",
    "django_htmx",
    "modules.global_app",
    "modules.authentication",
    "modules.tasks",
    "tailwind",
    "modules.theme",
    # "django_browser_reload",
]

TAILWIND_APP_NAME = "modules.theme"
