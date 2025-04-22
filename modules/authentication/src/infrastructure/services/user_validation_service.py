from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from ...domain.models import IUserModel
from ...domain.repositories import IUserRepository


class UserValidationService:
    def __init__(self, user_repository: IUserRepository) -> None:
        self._user_repository = user_repository

    def validate_username(self, username: str) -> None:
        retrieved_user = self._user_repository.find_user_by_username_or_email(username)

        if retrieved_user is not None:
            raise ValidationError("Um usuário com esse nome de usuário já existe.")

    def validate_password(self, password: str, orm_user: IUserModel) -> None:
        try:
            validate_password(password, orm_user)
        except ValidationError as e:
            raise ValidationError(e.messages)

    def validate_email(self, email: str) -> None:
        retrieved_user = self._user_repository.find_user_by_username_or_email(email)

        if retrieved_user is not None:
            raise ValidationError("Um usuário com esse endereço de email já existe.")
