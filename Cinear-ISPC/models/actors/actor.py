from dataclasses import dataclass


@dataclass
class Actor:
    id: int
    name: str
    last_name: str
    gender_type: int
    country: int

    def __repr__(self) -> str:
        return f'{self.name} {self.last_name}'
