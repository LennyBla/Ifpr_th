from fastapi import Depends, FastAPI, HTTPException

from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
import uvicorn
from tmdb import get_json
from fastapi.middleware.cors import (CORSMiddleware)

app = FastAPI()

# habilita CORS (permite que o Svelte acesse o fastapi)
origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:5174",
    "http://127.0.0.1/5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/filmes")
async def filmes_populares(limit=3):
    """ Obtem os filmes mais populares usando endpoint discover """
    data = get_json(
        "/discover/movie", "?sort_by=vote_count.desc"
    )
    results = data['results']
    filtro = []

    for movie in results:
        filtro.append({
            "id": movie['id'],
            "title": movie['original_title'],
            "image": f"https://image.tmdb.org/t/p/w185{movie['poster_path']}",
            "overview": movie['overview']
            }),

    
    return filtro
@app.get("/artista/{name}")
async def get_artista(name : str):

    artist_name = get_json(
        "/search/person", f"?query={name}&language=en-US"
    )

    results = artist_name['results']
    filtro = []
    
    for artist in results:
        artist_id = get_json(
            "/person", f"/{artist['id']}?language=en-US&sort_by=vote_count.desc"
        )
        filtro.append({
            'id': artist_id['id'],
            'name': artist_id['name'],
            'biography' : artist_id['biography'],
            'image' : artist_id['profile_path'],
        })
        
    return filtro

# users
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 3 ENDPOINTS

#Criar novo usuario
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

#Apresentar todos usuários
@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

#Apresentar um usuário
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User not found")
    return crud.delete_user(db=db, user_id=user_id)


@app.post("/filmes/", response_model=schemas.Favoritos)
async def favoritar_filme(favorito: schemas.Favoritos, db: Session = Depends(get_db)):
    # db_favorito = crud.favoritar(db, tmdb_id = favorito.tmdb_id)
    # if db_favorito:
    #     raise HTTPException(status_code=400, detail="Movie already registered")
    return crud.favoritar(db=db, favorito=favorito)

@app.post("/users/favoritos/{movie_id}", response_model=schemas.Movie)
def favorite_movie(user_id: int, movie_id: int, movie_data: schemas.MovieBase, db: Session = Depends(get_db)):
    # Verificar se o filme já existe no banco de dados

    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not db_movie:
        new_movie = models.Movie(**movie_data.model_dump())
        db.add(new_movie)
        db.commit()
        db.refresh(new_movie)
        db_movie = new_movie

    # Marcar o filme como favorito para o usuário
    stmt = models.favorito.insert().values(user_id=user_id, movie_id=db_movie.id)
    db.execute(stmt)
    db.commit()

    return db_movie
# =========================================================================
# Atividade 1
@app.get("/users/{user_id}/favorito", response_model=list[schemas.Movie])
def get_favorito_movies(user_id: int, db: Session = Depends(get_db)):
    # Consulte o banco de dados para obter os filmes favoritos do usuário
    user = db.query(models.User).filter(models.User.id == user_id).first()
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    favorito_movies = db.query(models.Movie).join(models.favorito).filter(models.favorito.c.user_id == user_id).all()
    return favorito_movies
    
# source env/bin/activate
# uvicorn pycine:app --reload
# npm run dev
# source env/bin/activate
# uvicorn pycine:app --reload
# npm run dev
