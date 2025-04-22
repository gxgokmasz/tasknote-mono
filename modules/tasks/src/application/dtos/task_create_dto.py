from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class TaskCreateDTO:
    title: str

    user_id: int

    priority: int
    description: str | None

    finish_date: date | None
