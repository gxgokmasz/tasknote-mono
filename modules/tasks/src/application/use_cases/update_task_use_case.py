from ...domain.entities import Task
from ..dtos import TaskUpdateDTO
from ..services import ITaskService


class UpdateTaskUseCase:
    def __init__(self, task_service: ITaskService) -> None:
        self.task_service = task_service

    def execute(self, task: TaskUpdateDTO) -> Task:
        updated_task = self.task_service.update_task(task)

        return updated_task
