from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class TaskUpdateDTO:
    id: int

    title: str
    priority: int
    description: str | None

    finish_date: date | None
