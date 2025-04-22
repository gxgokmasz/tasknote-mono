from importlib import import_module

from django.apps import AppConfig
from django.utils.module_loading import module_has_submodule


class TasksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "modules.tasks"

    def ready(self) -> None:
        from .src.infrastructure import admin  # noqa

    def import_models(self):
        self.models = self.apps.all_models[self.label]

        if module_has_submodule(self.module, "src.infrastructure.models"):
            models_module_name = "%s.%s" % (self.name, "src.infrastructure.models")
            self.models_module = import_module(models_module_name)
