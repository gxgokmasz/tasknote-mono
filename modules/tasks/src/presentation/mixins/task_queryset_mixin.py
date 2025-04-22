import inject

from ...domain.entities import Task
from .authenticated_user_mixin import AuthenticatedUserMixin


class TaskQuerysetMixin(AuthenticatedUserMixin):
    def get_user_tasks(self) -> list[Task]:
        logged_in_user = self.get_logged_in_user()

        get_user_tasks_use_case = inject.instance("GetUserTasksUseCase")
        user_tasks = get_user_tasks_use_case.execute(logged_in_user["id"])

        return user_tasks

    def get_active_tasks(self) -> list[Task]:
        return [task for task in self.get_user_tasks() if task.deactivated_at is None]
