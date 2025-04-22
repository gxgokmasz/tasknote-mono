import dj_database_url
from decouple import config

DATABASE_USER = config("DATABASE_USER")

DATABASE_PASSWORD = config("DATABASE_PASSWORD")

DATABASE_HOST = config("DATABASE_HOST")

DATABASE_PORT = config("DATABASE_PORT")

DATABASE_NAME = config("DATABASE_NAME")

DATABASES = {
    "default": dj_database_url.parse(
        f"mysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}",
        conn_max_age=600,
        conn_health_checks=True,
    )
}

MIGRATION_MODULES = {
    "authentication": "modules.authentication.src.infrastructure.migrations",
    "tasks": "modules.tasks.src.infrastructure.migrations",
}

REDIS_HOST = config("REDIS_HOST")

REDIS_PORT = config("REDIS_PORT")

REDIS_DB = config("REDIS_DB")

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

DJANGO_REDIS_IGNORE_EXCEPTIONS = True

DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS = True

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

SESSION_CACHE_ALIAS = "default"
