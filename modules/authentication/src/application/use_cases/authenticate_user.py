from django.http import HttpRequest

from ...domain.entities import User
from ..dtos import UserLoginDTO
from ..services import IUserService


class AuthenticateUserUseCase:
    def __init__(self, user_service: IUserService) -> None:
        self._user_service = user_service

    def execute(self, user: UserLoginDTO, request: HttpRequest) -> User | None:
        authenticated_user = self._user_service.authenticate_user(user, request)

        return authenticated_user
