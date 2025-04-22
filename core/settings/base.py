from decouple import config
from unipath import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = True if config("MOD") == "DEVELOPMENT" else False

ALLOWED_HOSTS = ["*"] if config("MOD") == "DEVELOPMENT" else []

INTERNAL_IPS = [
    "localhost",
    "127.0.0.1",
]

RATE_LIMIT = 100 if config("MOD") == "DEVELOPMENT" else 30

RATE_LIMIT_TIME = 60

ROOT_URLCONF = "core.urls"

WSGI_APPLICATION = "core.wsgi.application"

GRAPPELLI_ADMIN_TITLE = "Tasknote Admin"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
