from dataclasses import dataclass


@dataclass
class Gender:
    id: int
    gender: str

    def __repr__(self) -> str:
        return self.gender
