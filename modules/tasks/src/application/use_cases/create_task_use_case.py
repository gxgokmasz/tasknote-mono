from ...domain.entities import Task
from ..dtos import TaskCreateDTO
from ..services import ITaskService


class CreateTaskUseCase:
    def __init__(self, task_service: ITaskService) -> None:
        self.task_service = task_service

    def execute(self, task: TaskCreateDTO) -> Task:
        created_task = self.task_service.create_task(task)

        return created_task
