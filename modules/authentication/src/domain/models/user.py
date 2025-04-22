import uuid
from datetime import datetime
from typing import Protocol


class IUserModel(Protocol):
    public_id: uuid.UUID
    id: int

    username: str
    email: str
    password: str

    is_active: bool
    is_staff: bool
    is_superuser: bool

    date_joined: datetime
    updated_at: datetime
    deactivated_at: datetime | None

    def deactivate(self) -> None: ...

    def activate(self) -> None: ...
