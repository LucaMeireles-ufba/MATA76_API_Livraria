from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/authors/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db=db, author=author)

@app.get("/books/", response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books

@app.get("/books/{books_isbn}", response_model=schemas.Book)
def read_book_bt_isbn(book_isbn: int, db: Session = Depends(get_db)):
    return crud.get_book_by_isbn(db=db, book_isbn=book_isbn)

@app.post("/books/", response_model = schemas.Book)
def create_book(book: schemas.BookCreate, author_id: int, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book, author_id=author_id)
