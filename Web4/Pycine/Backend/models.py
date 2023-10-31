from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
 
    # Adicione a relação 'favoritos'
    favoritos = relationship("Favorito_movie", back_populates="user")

class Movier(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    tmdb_id= Column(String)
    title_id= Column(String)
    is_active = Column(Boolean, default=True)
    
class Favorito_movie(Base):
    __tablename__ = 'favorito_movie'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.id'), primary_key=True)
    
    # Adicione as relações 'user' e 'movie'
    user = relationship("User", back_populates="favoritos")
    movie = relationship("Movier", back_populates="favoritos")


#CLASSE Q É MAPEADA TABELA DO SQLITE
