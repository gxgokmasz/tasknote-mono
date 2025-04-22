from ...domain.services import IUserValidationService


class UsernameValidator:
    def __init__(self, user_validation_service: IUserValidationService) -> None:
        self.user_validation_service = user_validation_service

    def __call__(self, username: str) -> None:
        self.user_validation_service.validate_username(username)
