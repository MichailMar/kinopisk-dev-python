from typing import List, Optional
from pydantic import BaseModel

class Review(BaseModel):
    userRating: Optional[float] = None
    updatedAt: Optional[str] = None
    createdAt: Optional[str] = None
    id: Optional[int] = None
    movieId: Optional[int] = None
    title: Optional[str] = None
    type: Optional[str] = None
    review: Optional[str] = None
    date: Optional[str] = None
    author: Optional[str] = None
    authorId: Optional[int] = None

class ReviewList(BaseModel):
    docs: Optional[list[Review]] = None
    total: Optional[int] = None
    limit: Optional[int] = None
    page: Optional[int] = None
    pages: Optional[int] = None
