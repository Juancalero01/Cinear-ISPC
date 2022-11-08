from dataclasses import dataclass
from datetime import date


@dataclass
class Post:
    id: int
    post_detail: str
    post_title: str
    post_subtitle: str
    post_date: date
    fk_user: int
    fk_video: int

    def __repr__(self) -> str:
        return self.post_title
