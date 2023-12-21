from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Cover(BaseModel):
    url: Optional[str] = None
    previewUrl: Optional[str] = None

class Category(BaseModel):
    category: Optional[str] = None
    slug: Optional[str] = None
    moviesCount: Optional[int] = None
    cover: Optional[Cover] = None
    name: Optional[str] = None
    updatedAt: Optional[datetime] = None
    createdAt: Optional[datetime] = None

class CategoryList(BaseModel):
    docs: Optional[list[Category]] = None
    total: Optional[int] = None
    limit: Optional[int] = None
    page: Optional[int] = None
    pages: Optional[int] = None
