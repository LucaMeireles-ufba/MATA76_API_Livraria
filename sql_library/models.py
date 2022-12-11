from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    isbn = Column(String, unique=True, index=True)
    name = Column(String)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = Column(String, ForeignKey("authors.name"))
    year_publication = Column(Integer)
    publishing_company = Column(String)
    description = Column(String)
    shelf_location = Column(String)
    status = Column(String)

    author = relationship("Author", back_populates="work")

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    work = relationship("Book", back_populates="author")

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    birth_day = Column(String)
    address = Column(String)

class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
