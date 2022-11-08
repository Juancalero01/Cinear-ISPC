from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    last_name: str
    email: str
    password: str
    country: int

    def __repr__(self) -> str:
        return f'{self.name} {self.last_name}'
