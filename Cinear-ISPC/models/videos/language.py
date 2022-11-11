from dataclasses import dataclass


@dataclass
class Language:
    id: int
    language: str

    def __repr__(self) -> str:
        return self.language
