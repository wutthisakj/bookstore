from pydantic import BaseModel
from typing import List


class Author(BaseModel):
    id: int
    name: str
    books: List[str]
    


    