from pydantic import BaseModel

class UserBase(BaseModel):
    #name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class MovieBase(BaseModel):
    tmdb_id: str
    title: str

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int

class FavoritosBase(BaseModel):
    tmdb_id: str

class FavoritosCreate(FavoritosBase):
    pass

class Favoritos(FavoritosBase):
    id: int
