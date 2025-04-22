from typing import Protocol

from ..models import IUserModel


class IUserRepository(Protocol):
    def create_user(self, username: str, email: str, password: str) -> IUserModel: ...

    def find_user_by_username_or_email(self, identifier: str) -> IUserModel | None: ...
