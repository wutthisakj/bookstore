import datetime
from typing import Dict, List, Tuple, Set
from pydantic import BaseModel

class Book(BaseModel):
    name: str
    price: float = 10.0
    year: datetime.datetime

book1 = {"name": "book1", "price": 11.0, "year": datetime.datetime.now()}
book_object = Book(**book1)

def print_book(book: Book):
    print(book)

print_book(book_object)

