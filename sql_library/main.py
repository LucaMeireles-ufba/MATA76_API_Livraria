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

### AUTORES ###

@app.post("/authors/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db=db, author=author)

### LIVROS ###

@app.get("/books/", response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books

@app.get("/book/{book_isbn}", response_model = schemas.Book)
def read_book_by_isbn(book_isbn: int, db: Session = Depends(get_db)):
    return crud.get_book_by_isbn(db=db, book_isbn=book_isbn)

@app.post("/books/", response_model = schemas.Book)
def create_book(book: schemas.BookCreate, author_id: int, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book, author_id=author_id)

@app.put("/book/", response_model = schemas.Book)
def update_book(book_id: int, name: str, db : Session=Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.update_book(db, book_id, name)

@app.delete("/book/", response_model = schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.remove_book(db, book_id)

### CLIENTES ###

@app.get("/customers/", response_model = list[schemas.Customer])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_customers(db, skip=skip, limit=limit)

@app.get("/customer/{customer_id}", response_model = schemas.Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    return crud.get_customer(db, customer_id=customer_id)

@app.post("/customers/", response_model = schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db, customer=customer)

### EMPRÉSTIMOS ###

@app.get("/loans/", response_model = list[schemas.Loan])
def read_loans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_loans(db, skip=skip, limit=limit)

@app.get("/loan/{loan_id}", response_model=schemas.Loan)
def read_loan(loan_id: int, db: Session = Depends(get_db)):
    db_loan = crud.get_loan(db=db, loan_id=loan_id)
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan

@app.post("/loans/", response_model=schemas.Loan)
def create_loan(loan: schemas.LoanCreate, customer_id: int, book_id: int, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db=db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    db_book = crud.get_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="book not found")
    return crud.create_loan(db=db, loan=loan, customer_id=customer_id, book_id=book_id)