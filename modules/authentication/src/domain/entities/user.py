import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class User:
    public_id: uuid.UUID
    id: int

    username: str
    email: str
    password: str

    is_active: bool
    is_staff: bool
    is_superuser: bool

    created_at: datetime
    updated_at: datetime
    deactivated_at: datetime | None
