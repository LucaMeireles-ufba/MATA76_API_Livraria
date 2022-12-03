from sqlalchemy.orm import Session

from . import models, schemas


def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()


def get_authors(db: Session, skip: int = 0, limit: int = 0):
    return db.query(models.Author).offset(skip).limit(limit).all()

def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def get_book_by_isbn(db: Session, book_isbn: int):
    return db.query(models.Book).filter(models.Book.isbn == book_isbn).first()

def create_book(db: Session, book: schemas.BookCreate, author_id: int):
    db_book = models.Book(isbn=book.isbn, name=book.name, author_id=author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()

def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(name=customer.name, birth_day=customer.birth_day, address=customer.address)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_loans(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Loan).offset(skip).limit(limit).all()

def get_loan(db: Session, loan_id: int):
    return db.query(models.Loan).filter(models.Loan.id == loan_id).first()

def create_loan(db: Session, loan: schemas.LoanCreate, customer_id: int, book_id: int):
    db_loan = models.Loan(date = loan.date, customer_id=customer_id, book_id=book_id)
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan
