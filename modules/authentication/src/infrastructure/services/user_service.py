from django.contrib.auth import login
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpRequest

from ...application.dtos import UserCreateDTO, UserLoginDTO
from ...domain.entities import User
from ...domain.models import IUserModel
from ...domain.repositories import IUserRepository
from ..mappers import UserMapper


class UserService:
    def __init__(self, user_repository: IUserRepository) -> None:
        self._user_repository = user_repository

    def create_user(self, user: UserCreateDTO, request: HttpRequest) -> User:
        created_user = self._user_repository.create_user(
            user.username, user.email, make_password(user.password)
        )
        user_entity = UserMapper.orm_to_entity(created_user)

        self._login_user(request, user_entity, created_user)

        return user_entity

    def authenticate_user(self, user: UserLoginDTO, request: HttpRequest) -> User | None:
        retrieved_user = self._user_repository.find_user_by_username_or_email(user.identifier)

        if retrieved_user and check_password(user.password, retrieved_user.password):
            user_entity = UserMapper.orm_to_entity(retrieved_user)

            self._login_user(request, user_entity, retrieved_user)

            return user_entity

        return

    def _login_user(self, request: HttpRequest, user_entity: User, orm_user: IUserModel) -> None:
        request.session["user"] = UserMapper.entity_to_dict(user_entity)
        login(request, orm_user)
