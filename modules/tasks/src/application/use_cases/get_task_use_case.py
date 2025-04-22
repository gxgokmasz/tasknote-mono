from ...domain.entities import Task
from ..services import ITaskService


class GetTaskUseCase:
    def __init__(self, task_service: ITaskService) -> None:
        self.task_service = task_service

    def execute(self, task_public_id: str) -> Task | None:
        task = self.task_service.find_task_by_public_id(task_public_id)

        return task
