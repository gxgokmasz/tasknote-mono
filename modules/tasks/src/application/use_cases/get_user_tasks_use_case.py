from ...domain.entities import Task
from ..services import ITaskService


class GetUserTasksUseCase:
    def __init__(self, task_service: ITaskService) -> None:
        self.task_service = task_service

    def execute(self, user_id: int) -> list[Task] | None:
        user_tasks = self.task_service.get_user_tasks(user_id)

        return user_tasks
