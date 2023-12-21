from typing import List, Optional
from pydantic import BaseModel

class Still(BaseModel):
    url: Optional[str] = None
    previewUrl: Optional[str] = None

class Episode(BaseModel):
    number: Optional[int] = None
    name: Optional[str] = None
    enName: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    still: Optional[Still] = None
    airDate: Optional[str] = None
    enDescription: Optional[str] = None

class Poster(BaseModel):
    url: Optional[str] = None
    previewUrl: Optional[str] = None

class Doc(BaseModel):
    updatedAt: Optional[str] = None
    createdAt: Optional[str] = None
    movieId: Optional[int] = None
    number: Optional[int] = None
    episodesCount: Optional[int] = None
    episodes: Optional[list[Episode]] = None
    poster: Optional[Poster] = None
    name: Optional[str] = None
    enName: Optional[str] = None
    duration: Optional[int] = None
    description: Optional[str] = None
    enDescription: Optional[str] = None
    airDate: Optional[str] = None

class SeasonModel(BaseModel):
    docs: Optional[list[Doc]] = None
    total: Optional[int] = None
    limit: Optional[int] = None
    page: Optional[int] = None
    pages: Optional[int] = None
