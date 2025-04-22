from ...domain.entities import Task
from ...domain.models import ITaskModel


class TaskMapper:
    @staticmethod
    def orm_to_entity(orm_task: ITaskModel) -> Task:
        return Task(
            orm_task.public_id,
            orm_task.id,
            orm_task.title,
            orm_task.description,
            orm_task.is_done,
            orm_task.user_id,
            orm_task.priority,
            orm_task.finish_date,
            orm_task.created_at,
            orm_task.updated_at,
            orm_task.deactivated_at,
        )
