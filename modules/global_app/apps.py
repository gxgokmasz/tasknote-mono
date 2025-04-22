from django.apps import AppConfig

from .src.common.infrastructure.containers import configure_injection_containers


class GlobalAppConfig(AppConfig):
    name = "modules.global_app"

    def ready(self):
        configure_injection_containers()
