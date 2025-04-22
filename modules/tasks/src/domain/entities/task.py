import uuid
from dataclasses import dataclass
from datetime import date, datetime


@dataclass(frozen=True)
class Task:
    public_id: uuid.UUID
    id: int

    title: str
    description: str
    is_done: bool

    user_id: int

    priority: int

    finish_date: date | None
    created_at: datetime
    updated_at: datetime
    deactivated_at: datetime | None
