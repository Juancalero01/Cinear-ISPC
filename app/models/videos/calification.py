from dataclasses import dataclass


@dataclass
class Calification:
    id: int
    calification: int

    def __repr__(self) -> str:
        return self.calification
