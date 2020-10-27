from pydantic import BaseModel, Schema
from models.author import Author
from utils.const import ISBN_DESCRIPTION
class Book(BaseModel):
    isbn: str = Schema(None, desscription=ISBN_DESCRIPTION)
    name: str
    author: Author
    year: int = Schema(None, gt=1900, lt=2100)
