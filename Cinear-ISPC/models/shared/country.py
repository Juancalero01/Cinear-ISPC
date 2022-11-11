from dataclasses import dataclass


@dataclass
class Country:
    id: int
    country: str

    def __repr__(self) -> str:
        return self.country
