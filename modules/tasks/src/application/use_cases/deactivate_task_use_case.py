from ..services import ITaskService


class DeactivateTaskUseCase:
    def __init__(self, task_service: ITaskService) -> None:
        self.task_service = task_service

    def execute(self, task_id: int) -> None:
        self.task_service.deactivate_task(task_id)
