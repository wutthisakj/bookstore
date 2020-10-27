import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.db_object import db

# from databases import Database

# from utils.const import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER

#from utils.orm_db import authors

# async def connect_db():
#     db = Database(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")
#     await db.connect()
#     return db

# async def disconnect_db(db):
#     await db.disconnect()

async def execute(query, is_many, values=None):
    #db = await connect_db()
    #try:
    if is_many:
        await db.execute_many(query=query, values=values)
    else:
        await db.execute(query=query, values=values)
    #except Exception as e:
        
    #await disconnect_db(db)

async def fetch(query, is_one, values=None):
    """
    Param 1: Query string
    Param 2: True for getting One row , False for many rows
    Param 3: values for the query
    Return data in dict format"""
    #db = await connect_db()

    if is_one:
        result = await db.fetch_one(query=query, values=values)
        if result is None:
            out = None
        else:
            out = dict(result)
    else:
        result = await db.fetch_all(query=query, values=values)
        if result is None:
            out = None
        else:
            out = []
            for row in result:
                out.append(dict(row))
    
    #await disconnect_db(db)
    return out

#query = "insert into books values(:custom, :name, :author, :year)"
#values = [{"custom": "isbn2", "name": "book2", "author": "author2", "year": 2018},
#          {"custom": "isbn3", "name": "book3", "author": "author3", "year": 2020}]

#query = "select * from books where isbn=:isbn"
#values ={"isbn": "isbn2"}

#query = "select * from books"

# async def test_orm():
#     query = authors.select().where(authors.c.name=="author2")
#     print(query)
#     out = await fetch(query, True)
#     print(out)

#import asyncio
#loop = asyncio.get_event_loop()
#loop.run_until_complete(test_orm())
