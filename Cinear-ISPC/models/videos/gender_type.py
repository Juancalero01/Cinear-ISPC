from dataclasses import dataclass


@dataclass
class Gender_type:
    id: int
    gender_type: str

    def __repr__(self) -> str:
        return self.gender_type
