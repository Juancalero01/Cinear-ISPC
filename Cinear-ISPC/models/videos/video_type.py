from dataclasses import dataclass


@dataclass
class Video_type:
    id: int
    video_type: str

    def __repr__(self) -> str:
        return self.video_type
