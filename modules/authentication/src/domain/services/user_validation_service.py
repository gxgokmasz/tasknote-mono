from typing import Protocol

from ...domain.models import IUserModel


class IUserValidationService(Protocol):
    def validate_username(self, username: str) -> None: ...

    def validate_password(self, password: str, orm_user: IUserModel) -> None: ...

    def validate_email(self, email: str) -> None: ...
