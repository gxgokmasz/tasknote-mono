from ...domain.entities import User
from ...domain.models import IUserModel


class UserMapper:
    @staticmethod
    def orm_to_entity(orm_user: IUserModel) -> User:
        return User(
            orm_user.public_id,
            orm_user.id,
            orm_user.username,
            orm_user.email,
            orm_user.password,
            orm_user.is_active,
            orm_user.is_staff,
            orm_user.is_superuser,
            orm_user.date_joined,
            orm_user.updated_at,
            orm_user.deactivated_at,
        )

    @staticmethod
    def entity_to_dict(user: User) -> dict:
        return {
            "public_id": str(user.public_id),
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "password": user.password,
            "is_active": user.is_active,
            "is_staff": user.is_staff,
            "is_superuser": user.is_superuser,
            "created_at": user.created_at.isoformat(),
            "updated_at": user.updated_at.isoformat(),
            "deactivated_at": user.deactivated_at.isoformat() if user.deactivated_at else None,
        }
