from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class Place(BaseModel):
    value: Optional[str] = None

class Spouse(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    divorced: Optional[bool] = None
    divorcedReason: Optional[str] = None
    sex: Optional[str] = None
    children: Optional[int] = None
    relation: Optional[str] = None

class Profession(BaseModel):
    value: Optional[str] = None

class Fact(BaseModel):
    value: Optional[str] = None

class Movie(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    alternativeName: Optional[str] = None
    rating: Optional[float] = None
    general: Optional[bool] = None
    description: Optional[str] = None
    enProfession: Optional[str] = None

class PersonModel(BaseModel):
    id: Optional[int] = None
    updatedAt: Optional[datetime] = None
    createdAt: Optional[datetime] = None
    name: Optional[str] = None
    enName: Optional[str] = None
    photo: Optional[str] = None
    sex: Optional[str] = None
    growth: Optional[float] = None
    birthday: Optional[str] = None
    death: Optional[str] = None
    age: Optional[int] = None
    birthPlace: Optional[list[Place]] = None
    deathPlace: Optional[list[Place]] = None
    spouses: Optional[Spouse] = None
    countAwards: Optional[int] = None
    profession: Optional[list[Profession]] = None
    facts: Optional[list[Fact]] = None
    movies: Optional[list[Movie]] = None

class PersonList(BaseModel):
    docs: Optional[list[PersonModel]] = None
    total: Optional[int] = None
    limit: Optional[int] = None
    page: Optional[int] = None
    pages: Optional[int] = None



class Award(BaseModel):
    title: Optional[str]
    year: Optional[int]

class Nomination(BaseModel):
    award: Optional[Award]
    title: Optional[str]

class MovieInfo(BaseModel):
    id: Optional[int]
    name: Optional[str]
    rating: Optional[float]

class AwardRecord(BaseModel):
    nomination: Optional[Nomination]
    winning: Optional[bool]
    updatedAt: Optional[datetime]
    createdAt: Optional[datetime]
    personId: Optional[int]
    movie: Optional[MovieInfo]

class AwardList(BaseModel):
    docs: Optional[list[AwardRecord]]
    total: Optional[int]
    limit: Optional[int]
    page: Optional[int]
    pages: Optional[int]