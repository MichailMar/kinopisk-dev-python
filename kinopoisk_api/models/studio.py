from typing import  Optional
from pydantic import BaseModel

class MovieInfo(BaseModel):
    id: Optional[int]

class Studio(BaseModel):
    id: Optional[str]
    subType: Optional[str]
    title: Optional[str]
    updatedAt: Optional[str]
    createdAt: Optional[str]
    type: Optional[str]
    movies: Optional[MovieInfo]

class StudioList(BaseModel):
    docs: Optional[list[Studio]]
    total: Optional[int]
    limit: Optional[int]
    page: Optional[int]
    pages: Optional[int]
