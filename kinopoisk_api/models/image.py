from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Image(BaseModel):
    movieId: Optional[int] = None
    updatedAt: Optional[datetime] = None
    createdAt: Optional[datetime] = None
    type: Optional[str] = None
    language: Optional[str] = None
    url: Optional[str] = None
    previewUrl: Optional[str] = None
    height: Optional[int] = None
    width: Optional[int] = None

class ImageList(BaseModel):
    docs: Optional[list[Image]] = None
    total: Optional[int] = None
    limit: Optional[int] = None
    page: Optional[int] = None
    pages: Optional[int] = None
