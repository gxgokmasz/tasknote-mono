from datetime import datetime
from typing import Protocol

from ..models import ITaskModel


class ITaskRepository(Protocol):
    def create_task(
        self,
        task_title: str,
        user_id: int,
        task_priority: int,
        task_description: str | None,
        task_finish_date: datetime | None,
    ) -> ITaskModel: ...

    def find_task_by_public_id(self, task_public_id: str) -> ITaskModel | None: ...

    def get_user_tasks(self, user_id: int) -> list[ITaskModel] | None: ...

    def update_task(
        self,
        task_id: int,
        task_title: str,
        task_priority: int,
        task_description: str | None,
        task_finish_date: datetime | None,
    ) -> ITaskModel: ...

    def deactivate_task(self, task_id: int) -> None: ...

    def toggle_task_done(self, task_id: int) -> None: ...
