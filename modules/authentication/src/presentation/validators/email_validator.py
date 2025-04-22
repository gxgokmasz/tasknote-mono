from ...domain.services import IUserValidationService


class EmailValidator:
    def __init__(self, user_validation_service: IUserValidationService) -> None:
        self.user_validation_service = user_validation_service

    def __call__(self, email: str) -> None:
        self.user_validation_service.validate_email(email)
