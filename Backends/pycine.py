from fastapi import FastAPI
from tmdb import get_json

app = FastAPI()

from fastapi.middleware.cors import (
     CORSMiddleware
)
# habilita CORS (permite que o Svelte acesse o fastapi)
origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:5173/UserList",
    "http://localhost:5173/favorites",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========================================================

# ATIVIDADE 1

@app.get("/filme/{title}")
async def find_movie(title: str):
    """ 
    procura filmes pelo titulo e ordena pelos mais populares 
    Exemplo: /filme/avatar
    """
    return {"title": title}

# ========================================================

# ATIVIDADE 2

@app.get("/artista/filmes")
async def find_filmes_artista(personId: int):
    """ 
    busca os filmes mais populares de um artista 
    Exemplo: /artista/filmes?personId=1100
    """
    return {"id": personId}

# ========================================================

@app.get("/filmes")
async def filmes_populares():
    data = get_json(
        "/discover/movie", "?sort_by=vote_count.desc"
    )
    results = data['results']
    filtro = []
    for movie in results:
        filtro.append({"title": movie['original_title'],
                       "image": f"https://image.tmdb.org/t/p/w185{movie['poster_path']}",
                       "tmdb_id": movie['id']})
    return filtro

@app.get("/artistas/{name}")
async def get_artista(name: str):
    artist_name = get_json(
        "/search/person", f"?query={name}&language=en-US"
    )

    results = artist_name['results']
    filtro = []

    for artist in results:
        artist_id = get_json("/person", f"/{artist['id']}?language=en-US")
        filtro.append({
            'id': artist_id['id'],
            "name": artist_id['name'],
            'rank': artist_id['popularity'],
            'biography': artist_id['biography'],
            "profile_path": artist_id['profile_path']
        })
    filtro.sort(reverse=True, key=lambda artist:artist['rank'])
    return filtro

# USERS
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

models.Base.metadata.create_all(bind=engine)

## favorita o filme
@app.post("/favorites/{user_id}/{tmdb_id}", response_model=schemas.Movie)
def favorite_movie(user_id:int, tmdb_id:int, db: Session = Depends(get_db)):
    return crud.favorite_movie(db=db, user_id = 1, tmdb_id=tmdb_id)

# PEGA TODOS OS FILMES FAVORITADOS
@app.get("/favorites", response_model=list[schemas.Movie])
def get_favorites(db: Session = Depends(get_db)):
    return crud.get_favorites(db=db)

## USERS ##

@app.get("/users", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


## ATUALIZAZÇAO DE USUARIO
@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user = crud.update_user(db, user_id=user_id, user=user)
    return db_user

## DELETAR USUARIO
@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    crud.delete_user(db, user_id=user_id)
    return db_user



@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# source env/bin/activate
# uvicorn pycine:app --reload
# npm run dev