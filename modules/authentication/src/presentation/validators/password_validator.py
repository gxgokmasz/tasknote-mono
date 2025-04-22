from ...domain.models import IUserModel
from ...domain.services import IUserValidationService


class PasswordValidator:
    def __init__(self, user_validation_service: IUserValidationService) -> None:
        self.user_validation_service = user_validation_service

    def __call__(self, password: str, orm_user: IUserModel) -> None:
        self.user_validation_service.validate_password(password, orm_user)
