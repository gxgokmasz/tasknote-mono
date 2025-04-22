from django.apps import apps
from django.db.models import Q

from ...domain.models import IUserModel


class UserRepository:
    def __init__(self) -> None:
        self._user_model = apps.get_model("authentication", "User")

    def create_user(self, username: str, email: str, password: str) -> IUserModel:
        orm_user = self._user_model.objects.create(
            username=username, email=email, password=password
        )

        return orm_user

    def find_user_by_username_or_email(self, identifier: str) -> IUserModel | None:
        try:
            orm_user = self._user_model.objects.get(Q(username=identifier) | Q(email=identifier))

            return orm_user
        except self._user_model.DoesNotExist:
            return
