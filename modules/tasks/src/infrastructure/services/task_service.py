from ...application.dtos import TaskCreateDTO, TaskUpdateDTO
from ...domain.entities import Task
from ...domain.repositories import ITaskRepository
from ..mappers import TaskMapper


class TaskService:
    def __init__(self, task_repository: ITaskRepository) -> None:
        self.task_repository = task_repository

    def create_task(self, task: TaskCreateDTO) -> Task:
        created_task = self.task_repository.create_task(
            task.title, task.user_id, task.priority, task.description, task.finish_date
        )
        task_entity = TaskMapper.orm_to_entity(created_task)

        return task_entity

    def find_task_by_public_id(self, task_public_id: str):
        retrieved_task = self.task_repository.find_task_by_public_id(task_public_id)
        task_entity = TaskMapper.orm_to_entity(retrieved_task)

        return task_entity

    def get_user_tasks(self, user_id: int) -> list[Task] | None:
        user_tasks = self.task_repository.get_user_tasks(user_id)
        task_entities = [TaskMapper.orm_to_entity(orm_task) for orm_task in user_tasks]

        return task_entities

    def update_task(self, task: TaskUpdateDTO) -> Task:
        updated_task = self.task_repository.update_task(
            task.id, task.title, task.priority, task.description, task.finish_date
        )
        task_entity = TaskMapper.orm_to_entity(updated_task)

        return task_entity

    def deactivate_task(self, task_id: int) -> None:
        self.task_repository.deactivate_task(task_id)

    def toggle_task_done(self, task_id: int) -> None:
        self.task_repository.toggle_task_done(task_id)
