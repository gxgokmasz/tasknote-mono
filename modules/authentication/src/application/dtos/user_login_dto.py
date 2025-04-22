from dataclasses import dataclass


@dataclass(frozen=True)
class UserLoginDTO:
    identifier: str
    password: str
