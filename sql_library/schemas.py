from typing import Union

from pydantic import BaseModel


class BookBase(BaseModel):
    isbn: str
    name: str


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True

class CustomerBase(BaseModel):
    name: str
    birth_day: str
    address: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True

class LoanBase(BaseModel):
    date: str

class LoanCreate(LoanBase):
    pass

class Loan(LoanBase):
    id: int
    customer_id: int
    book_id: int

    class Config:
        orm_mode = True