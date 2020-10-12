from fastapi import Query
from pydantic import BaseModel
import enum

class Role(str, enum.Enum):
    admin: str = "admin"
    personel: str = "personel"

class User(BaseModel):
    name: str
    password: str
    mail: str = Query(..., regex=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    role: Role
