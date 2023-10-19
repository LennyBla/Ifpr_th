from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from tmdb import get_json
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

# Habilita o CORS (permite que o Svelte acesse o FastAPI)
origins = [
    "http://localhost",
    "http://localhost:5173",
    #"http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ATIVIDADE 1

@app.get("/filme/{title}")
async def find_movie(title: str):
    """ 
    procura filmes pelo titulo e ordena pelos mais populares 
    Exemplo: /filme/avatar
    """
    return {"title": title}

@app.post("/user/create")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Cria um novo usuário.
    Verifica se o email já está registrado.
    """
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, 
            detail="Email already registered"
        )
    new_user = crud.create_user(db=db, user=user)
    return new_user

@app.delete("/user/delete")
def delete_user(user: schemas.UserModel, db: Session = Depends(get_db)):
    """
    Deleta um usuário.
    """
    db_user = crud.delete_user(db, user.id)
    user.name = None
    user.email = None
    user.password = None
    user.id = None
    return db_user

@app.get("/user/get")
def get_user(user: schemas.UserModel, db: Session = Depends(get_db)):
    """
    Obtém informações de um usuário.
    """
    db_user = crud.get_user(db, user.id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = None
    user.email = None
    user.password = None
    user.id = None
    return db_user

@app.put("/user/update")
def update_user(user: schemas.UserModel, db: Session = Depends(get_db)):
    """
    Atualiza informações de um usuário.
    """
    db_user = crud.update_user(db, user)
    user.name = user.name
    user.email = user.email
    user.password = user.password
    return db_user

# ATIVIDADE 2

@app.get("/artista/filmes")
async def find_filmes_artista(personId: int):
    """
    Busca os filmes mais populares de um artista.
    Exemplo: /artista/filmes?personId=1100
    """
    data = get_json(
        f"/discover/movie?with_people={personId}"
    )
    results = data['results']
    filtro = []

    for movie in results:
        filtro.append({
            "title": movie['original_title'],
            "image": f"https://image.tmdb.org/t/p/w185{movie['poster_path']}"
        })

    return filtro

@app.get("/filmes")
async def filmes_populares(limit=3):
    """
    Obtem os filmes mais populares usando endpoint discover.
    """
    data = get_json(
        "/discover/movie?sort_by=vote_count.desc"
    )
    results = data['results']
    filtro = []

    for movie in results:
        filtro.append({
            "title": movie['original_title'],
            "image": f"https://image.tmdb.org/t/p/w185{movie['poster_path']}"
        })

    return filtro

@app.get("/artistas/{name}")
async def get_artista(name: str):
    """
    Obtém informações de artistas.
    """
    artist_name = get_json(
        "/search/person", f"?query={name}&language=en-US"
    )
    results = artist_name['results']
    filtro = []

    for artist in results:
        artist_id = get_json(
            f"/person/{artist['id']}?language=en-US&sort_by=vote_count.desc"
        )
        filtro.append({
            'id': artist_id['id'],
            'name': artist_id['name'],
            'biography': artist_id['biography'],
            'image': artist_id['profile_path'],
        })

    return filtro

# Users

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# source env/bin/activate
# uvicorn pycine:app --reload
# npm run dev