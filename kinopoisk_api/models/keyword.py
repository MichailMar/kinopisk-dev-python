from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class MovieInfo(BaseModel):
    id: Optional[int] = None

class Keyword(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    updatedAt: Optional[datetime] = None
    createdAt: Optional[datetime] = None
    movies: Optional[MovieInfo] = None

class KeywordList(BaseModel):
    docs: Optional[List[Keyword]] = None
    total: Optional[int] = None
    limit: Optional[int] = None
    page: Optional[int] = None
    pages: Optional[int] = None
