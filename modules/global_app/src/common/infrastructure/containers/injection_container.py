import inject

from modules.authentication.src.infrastructure.containers import configure_authentication_container
from modules.tasks.src.infrastructure.containers import configure_tasks_container


def configure_injection_containers() -> None:
    def config(binder: inject.Binder) -> None:
        configure_authentication_container(binder)
        configure_tasks_container(binder)

    inject.configure(config, once=True)
