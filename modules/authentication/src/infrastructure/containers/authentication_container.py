import inject

from ...application.services import IUserService
from ...application.use_cases import AuthenticateUserUseCase, CreateUserUseCase
from ...domain.repositories import IUserRepository
from ...domain.services import IUserValidationService
from ..repositories import UserRepository
from ..services import UserService, UserValidationService
from .providers import Factory, Singleton


def configure_authentication_container(binder: inject.Binder) -> None:
    user_repository = Singleton(UserRepository)

    user_service = Singleton(UserService, user_repository=user_repository)
    user_validation_service = Singleton(UserValidationService, user_repository=user_repository)

    authenticate_user_use_case = Factory(AuthenticateUserUseCase, user_service=user_service)
    create_user_use_case = Factory(CreateUserUseCase, user_service=user_service)

    binder.bind_to_provider(IUserRepository, user_repository)

    binder.bind_to_provider(IUserService, user_service)
    binder.bind_to_provider(IUserValidationService, user_validation_service)

    binder.bind_to_provider("AuthenticateUserUseCase", authenticate_user_use_case)
    binder.bind_to_provider("CreateUserUseCase", create_user_use_case)
