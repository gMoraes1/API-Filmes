from sqlalchemy.orm import Session
from app.models.movie import Movie
from app.schemas.movie import MovieCreate



def create_movie(db: Session, movie: MovieCreate):
    db_movie = Movie(
        title=movie.title,
        director=movie.director,
        year=movie.year
        

    )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def get_movies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Movie).offset(skip).limit(limit).all()