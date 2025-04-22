import uuid
from datetime import date, datetime
from typing import Literal, Protocol


class ITaskModel(Protocol):
    public_id: uuid.UUID
    id: int

    title: str
    description: str | None
    is_done: bool

    user_id: int

    priority: Literal[1, 2, 3]

    finish_date: date | None
    created_at: datetime
    updated_at: datetime
    deactivated_at: datetime | None

    def deactivate(self) -> None: ...

    def activate(self) -> None: ...
