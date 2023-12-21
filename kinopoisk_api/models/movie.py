from typing import List, Optional, Union
from datetime import datetime

from pydantic import BaseModel

class ExternalId(BaseModel):
    kpHD: Optional[str] = None
    imdb: Optional[str] = None
    tmdb: Optional[int] = None

class Name(BaseModel):
    name: Optional[str] = None
    language: Optional[str] = None
    type: Optional[str] = None

class NetworkItem(BaseModel):
    name: Optional[str] = None
    logo: Optional[dict] = None

class Network(BaseModel):
    items: Optional[list[NetworkItem]] = None

class Fact(BaseModel):
    value: Optional[str] = None
    type: Optional[str] = None
    spoiler: Optional[bool] = None

class ImagesInfo(BaseModel):
    postersCount: Optional[int] = None
    backdropsCount: Optional[int] = None
    framesCount: Optional[int] = None

class Rating(BaseModel):
    kp: Optional[float] = None
    imdb: Optional[float] = None
    tmdb: Optional[float] = None
    filmCritics: Optional[float] = None
    russianFilmCritics: Optional[float] = None
    await_: Optional[float] = None


class Votes(BaseModel):
    kp: Optional[Union[str, int]] = None
    imdb: Optional[float] = None
    tmdb: Optional[float] = None
    filmCritics: Optional[float] = None
    russianFilmCritics: Optional[float] = None
    await_: Optional[float] = None

class Logo(BaseModel):
    url: Optional[str] = None

class Poster(BaseModel):
    url: Optional[str] = None
    previewUrl: Optional[str] = None

class Backdrop(BaseModel):
    url: Optional[str] = None
    previewUrl: Optional[str] = None

class Teaser(BaseModel):
    size: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    site: Optional[str] = None
    type: Optional[str] = None

class Trailer(BaseModel):
    size: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    site: Optional[str] = None
    type: Optional[str] = None

class Video(BaseModel):
    teasers: Optional[list[Teaser]] = None
    trailers: Optional[list[Trailer]] = None

class Genre(BaseModel):
    name: Optional[str] = None

class Country(BaseModel):
    name: Optional[str] = None

class Person(BaseModel):
    description: Optional[str] = None
    profession: Optional[str] = None
    enProfession: Optional[str] = None
    id: Optional[int] = None
    photo: Optional[str] = None
    name: Optional[str] = None
    enName: Optional[str] = None

class ReviewInfo(BaseModel):
    count: Optional[int] = None
    positiveCount: Optional[int] = None
    percentage: Optional[str] = None

class SeasonInfo(BaseModel):
    number: Optional[int] = None
    episodesCount: Optional[int] = None

class Budget(BaseModel):
    value: Optional[int] = None
    currency: Optional[str] = None

class Fees(BaseModel):
    world: Optional[dict] = None
    russia: Optional[dict] = None
    usa: Optional[dict] = None

class Premiere(BaseModel):
    bluray: Optional[str] = None
    dvd: Optional[str] = None
    country: Optional[str] = None
    world: Optional[str] = None
    russia: Optional[str] = None
    digital: Optional[str] = None
    cinema: Optional[str] = None

class SimilarMovie(BaseModel):
    rating: Optional[Rating] = None
    year: Optional[int] = None
    name: Optional[str] = None
    enName: Optional[str] = None
    alternativeName: Optional[str] = None
    poster: Optional[Poster] = None
    id: Optional[int] = None
    type: Optional[str] = None

class SequelAndPrequel(BaseModel):
    rating: Optional[Rating] = None
    year: Optional[int] = None
    name: Optional[str] = None
    enName: Optional[str] = None
    alternativeName: Optional[str] = None
    poster: Optional[Poster] = None
    id: Optional[int] = None
    type: Optional[str] = None

class WatchabilityItem(BaseModel):
    logo: Optional[Logo] = None
    url: Optional[str] = None
    name: Optional[str] = None

class Watchability(BaseModel):
    items: Optional[List[WatchabilityItem]] = None

class ReleaseYears(BaseModel):
    start: Optional[int] = None
    end: Optional[int] = None

class Audience(BaseModel):
    count: Optional[int] = None
    country: Optional[str] = None

class MovieList(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None



class Award(BaseModel):
    title: Optional[str] = None
    year: Optional[int] = None

class Nomination(BaseModel):
    award: Optional[Award] = None
    title: Optional[str] = None

class Awards(BaseModel):
    nomination: Optional[Nomination] = None
    winning: Optional[bool] = None
    updateAt: Optional[datetime] = None
    createdAt: Optional[datetime] = None
    movieId: Optional[int] = None

class AwardsModel(BaseModel):
    docs: Optional[list[Awards]] = None
    total: Optional[int] = None
    limit: Optional[int] = None
    page: Optional[int] = None
    pages: Optional[int] = None

class MovieModel(BaseModel):
    id: Optional[int] = None
    externalId: Optional[ExternalId] = None
    names: Optional[list[Name]] = None
    type: Optional[str] = None
    typeNumber: Optional[int] = None
    isSeries: Optional[bool] = None
    networks: Optional[list[Network]] = None
    updatedAt: Optional[str] = None
    createdAt: Optional[str] = None
    facts: Optional[list[Fact]] = None
    imagesInfo: Optional[ImagesInfo] = None
    name: Optional[str] = None
    alternativeName: Optional[str] = None
    enName: Optional[str] = None
    year: Optional[int] = None
    description: Optional[str] = None
    shortDescription: Optional[str] = None
    slogan: Optional[str] = None
    status: Optional[str] = None
    rating: Optional[Rating] = None
    votes: Optional[Votes] = None
    movieLength: Optional[int] = None
    ratingMpaa: Optional[str] = None
    ageRating: Optional[int] = None
    logo: Optional[Logo] = None
    poster: Optional[Poster] = None
    backdrop: Optional[Backdrop] = None
    videos: Optional[Video] = None
    genres: Optional[list[Genre]] = None
    countries: Optional[list[Country]] = None
    persons: Optional[list[Person]] = None
    reviewInfo: Optional[ReviewInfo] = None
    seasonsInfo: Optional[list[SeasonInfo]] = None
    budget: Optional[Budget] = None
    fees: Optional[Fees] = None
    premiere: Optional[Premiere] = None
    similarMovies: Optional[list[SimilarMovie]] = None
    sequelsAndPrequels: Optional[list[SequelAndPrequel]] = None
    watchability: Optional[Watchability] = None
    releaseYears: Optional[list[ReleaseYears]] = None
    top10: Optional[int] = None
    top250: Optional[int] = None
    ticketsOnSale: Optional[bool] = None
    totalSeriesLength: Optional[int] = None
    seriesLength: Optional[int] = None
    audience: Optional[list[Audience]] = None
    lists: Optional[List[str]] = None

class MovieList(BaseModel):
    docs: list[MovieModel]