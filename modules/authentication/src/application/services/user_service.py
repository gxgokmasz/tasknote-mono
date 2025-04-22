from typing import Protocol

from django.http import HttpRequest

from ...domain.entities import User
from ..dtos import UserCreateDTO, UserLoginDTO


class IUserService(Protocol):
    def create_user(self, user: UserCreateDTO, request: HttpRequest) -> User: ...

    def authenticate_user(self, user: UserLoginDTO, request: HttpRequest) -> User | None: ...
