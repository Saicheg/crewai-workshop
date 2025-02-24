import datetime
from typing import List
from pydantic import BaseModel

class VideoInformation(BaseModel):
    url: str
    title: str
    description: str

class VideosInformation(BaseModel):
    videos: List[VideoInformation]
