from datetime import date, datetime

from django.apps import apps
from django.utils import timezone

from ...domain.models import ITaskModel


class TaskRepository:
    def __init__(self) -> None:
        self.task_model = apps.get_model("tasks", "Task")

    def create_task(
        self,
        title: str,
        user_id: int,
        priority: int = 1,
        description: str = None,
        finish_date: date = None,
    ) -> ITaskModel:
        orm_task = self.task_model.objects.create(
            title=title,
            user_id=user_id,
            description=description,
            priority=priority,
            finish_date=finish_date,
        )

        return orm_task

    def find_task_by_public_id(self, task_public_id: str) -> ITaskModel | None:
        try:
            orm_task = self.task_model.objects.get(public_id=task_public_id)

            return orm_task
        except self.task_model.DoesNotExist:
            return

    def get_user_tasks(self, user_id: int) -> list[ITaskModel] | None:
        orm_tasks = self.task_model.objects.filter(user_id=user_id)

        return orm_tasks

    def update_task(
        self,
        task_id: int,
        title: str,
        priority: int,
        description: str | None,
        finish_date: datetime | None,
    ) -> ITaskModel:
        orm_task, _ = self.task_model.objects.update_or_create(
            {
                "title": title,
                "priority": priority,
                "description": description,
                "finish_date": finish_date,
            },
            id=task_id,
        )

        return orm_task

    def deactivate_task(self, task_id: int) -> None:
        orm_task = self.task_model.objects.get(id=task_id)
        orm_task.deactivated_at = timezone.now()
        orm_task.save()

    def toggle_task_done(self, task_id: int) -> None:
        orm_task = self.task_model.objects.get(id=task_id)
        orm_task.is_done = not orm_task.is_done
        orm_task.save()
