from dataclasses import dataclass


@dataclass(frozen=True)
class UserCreateDTO:
    username: str
    email: str
    password: str
