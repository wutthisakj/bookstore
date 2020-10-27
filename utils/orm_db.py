import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.const import DB_URL
from sqlalchemy import (
    MetaData,
    create_engine,
    Table,
    Column,
    Integer,
    Text,
    ARRAY,
)

metadata = MetaData()
engine = create_engine(DB_URL)
metadata.create_all(engine)

authors = Table(
    "authors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", Text),
    Column("books", ARRAY(Text)), 
)


