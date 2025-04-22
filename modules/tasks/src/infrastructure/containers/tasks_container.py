import inject

from ...application.services import ITaskService
from ...application.use_cases import (
    CreateTaskUseCase,
    DeactivateTaskUseCase,
    GetTaskUseCase,
    GetUserTasksUseCase,
    ToggleTaskDoneUseCase,
    UpdateTaskUseCase,
)
from ...domain.repositories import ITaskRepository
from ..repositories import TaskRepository
from ..services import TaskService
from .providers import Factory, Singleton


def configure_tasks_container(binder: inject.Binder) -> None:
    task_repository = Singleton(TaskRepository)

    task_service = Singleton(TaskService, task_repository=task_repository)

    create_task_use_case = Factory(CreateTaskUseCase, task_service=task_service)
    deactivate_task_use_case = Factory(DeactivateTaskUseCase, task_service=task_service)
    get_task_use_case = Factory(GetTaskUseCase, task_service=task_service)
    get_user_tasks_use_case = Factory(GetUserTasksUseCase, task_service=task_service)
    toggle_task_done_use_case = Factory(ToggleTaskDoneUseCase, task_service=task_service)
    update_task_use_case = Factory(UpdateTaskUseCase, task_service=task_service)

    binder.bind_to_provider(ITaskRepository, task_repository)

    binder.bind_to_provider(ITaskService, task_service)

    binder.bind_to_provider("CreateTaskUseCase", create_task_use_case)
    binder.bind_to_provider("DeactivateTaskUseCase", deactivate_task_use_case)
    binder.bind_to_provider("GetTaskUseCase", get_task_use_case)
    binder.bind_to_provider("GetUserTasksUseCase", get_user_tasks_use_case)
    binder.bind_to_provider("ToggleTaskDoneUseCase", toggle_task_done_use_case)
    binder.bind_to_provider("UpdateTaskUseCase", update_task_use_case)
