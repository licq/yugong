from pathlib import Path
from dataclasses import dataclass
import json

@dataclass
class Video:
    title: str
    url: str
    duration: int
    thumbnail: str
    description: str
    views: int
    published: str
    channel: str
    channel_url: str
    uploader: str
    ext: str
    file: Path
    acodec: str
    audio_file: Path = None

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Video(title={self.title}, uploader={self.uploader}, url={self.url}, duration={self.duration}, thumbnail={self.thumbnail}, description={self.description}, views={self.views}, published={self.published}, channel={self.channel}, channel_url={self.channel_url})"

    def from_dict(data: dict):
        return Video(
            title=data["title"],
            url=data["webpage_url"],
            duration=data["duration"],
            thumbnail=data["thumbnail"],
            description=data["description"],
            views=data["view_count"],
            published=data["upload_date"],
            channel=data["channel"],
            channel_url=data["channel_url"],
            uploader=data["uploader"],
            ext=data["ext"],
            acodec=data["acodec"],
            file=None
        )

    @classmethod
    def from_json(cls, data: str):
        return cls.from_dict(json.loads(data))