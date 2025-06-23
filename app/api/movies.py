from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.movie import Movie, MovieCreate
from app.crud import movies as crud

router = APIRouter() 

@router.post("/filmes/", response_model=Movie)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie)

@router.get("/filmes/", response_model=list[Movie])
def list_movies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_movies(db, skip, limit)
