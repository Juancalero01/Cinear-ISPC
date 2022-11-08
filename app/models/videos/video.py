from dataclasses import dataclass
from datetime import date, time


@dataclass
class Video:
    id: int
    title: str
    launch_year: date
    video_duration: time
    fk_actor: int
    fk_language: int
    fk_video_type: int
    fk_gender: int
    fk_calification: int

    def __repr__(self) -> str:
        return self.title
