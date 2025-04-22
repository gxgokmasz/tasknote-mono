from django.http import HttpRequest

from ...domain.entities import User
from ..dtos import UserCreateDTO
from ..services import IUserService


class CreateUserUseCase:
    def __init__(self, user_service: IUserService) -> None:
        self._user_service = user_service

    def execute(self, user: UserCreateDTO, request: HttpRequest) -> User:
        created_user = self._user_service.create_user(user, request)

        return created_user
